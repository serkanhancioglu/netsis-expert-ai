"""Calisma durumunu SQLite'ta tutar: kaldigi yerden devam etmeyi bu saglar.

Neden JSON degil de SQLite? Dokuman basina bir kayit guncellenir ve is parcaciklari
bunu es zamanli yapar. JSON dosyasi her yazimda bastan yazilmali olur; calisma
ortasinda kesilirse dosya bozulur. SQLite ise WAL kipinde tek islemlik atomik
guncelleme sunar, Ctrl-C ya da elektrik kesintisinde bile tutarli kalir ve Python'un
standart kutuphanesinde bulundugu icin ek bagimlilik getirmez.
"""

from __future__ import annotations

import contextlib
import logging
import sqlite3
import threading
import time
from collections.abc import Iterator
from pathlib import Path
from typing import Any

log = logging.getLogger(__name__)

SCHEMA_VERSION = 1

SCHEMA_SQL = """
PRAGMA journal_mode = WAL;
PRAGMA synchronous = NORMAL;
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS meta (
    key   TEXT PRIMARY KEY,
    value TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS documents (
    doc_url       TEXT PRIMARY KEY,   -- kararli kimlik: external?cid=...&link=...
    page_id       TEXT,
    title         TEXT,
    breadcrumb    TEXT,               -- ' / ' ile birlestirilmis kirinti yolu
    relative_path TEXT,               -- cikti kokune gore .md yolu
    status        TEXT NOT NULL,      -- pending | done | failed | skipped
    attempts      INTEGER NOT NULL DEFAULT 0,
    last_error    TEXT,
    source_bytes  INTEGER,            -- indirilen ham HTML boyutu
    markdown_hash TEXT,               -- uretilen Markdown'in sha256'si
    images        INTEGER NOT NULL DEFAULT 0,
    updated_at    REAL NOT NULL
);

CREATE INDEX IF NOT EXISTS documents_status_idx ON documents(status);
"""


class StateStore:
    """Is parcacigi guvenli durum deposu.

    ``sqlite3`` baglantilari is parcaciklari arasinda paylasilamaz; bu yuzden her
    is parcacigi kendi baglantisini acar, yazimlar tek bir kilitle sirali yapilir.
    """

    def __init__(self, path: Path, *, read_only: bool = False) -> None:
        self.path = path
        self.read_only = read_only
        self._local = threading.local()
        self._write_lock = threading.Lock()
        if not read_only:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with self._connect() as connection:
                connection.executescript(SCHEMA_SQL)
                connection.execute(
                    "INSERT OR REPLACE INTO meta(key, value) VALUES('schema_version', ?)",
                    (str(SCHEMA_VERSION),),
                )

    # -- baglanti yonetimi ---------------------------------------------------------------

    def _connection(self) -> sqlite3.Connection:
        connection = getattr(self._local, "connection", None)
        if connection is None:
            connection = sqlite3.connect(self.path, timeout=30.0, isolation_level=None)
            connection.row_factory = sqlite3.Row
            connection.execute("PRAGMA busy_timeout = 30000")
            self._local.connection = connection
        return connection

    @contextlib.contextmanager
    def _connect(self) -> Iterator[sqlite3.Connection]:
        connection = self._connection()
        yield connection

    def close(self) -> None:
        connection = getattr(self._local, "connection", None)
        if connection is not None:
            connection.close()
            self._local.connection = None

    # -- yazma --------------------------------------------------------------------------

    def upsert_pending(self, rows: list[dict[str, Any]]) -> None:
        """Planlanan dokumanlari kaydeder; var olanlarin durumunu bozmaz."""
        now = time.time()
        with self._write_lock, self._connect() as connection:
            connection.execute("BEGIN IMMEDIATE")
            try:
                connection.executemany(
                    """
                    INSERT INTO documents
                        (doc_url, page_id, title, breadcrumb, relative_path,
                         status, attempts, updated_at)
                    VALUES
                        (:doc_url, :page_id, :title, :breadcrumb, :relative_path,
                         'pending', 0, :now)
                    ON CONFLICT(doc_url) DO UPDATE SET
                        page_id       = excluded.page_id,
                        title         = excluded.title,
                        breadcrumb    = excluded.breadcrumb,
                        relative_path = excluded.relative_path
                    """,
                    [dict(row, now=now) for row in rows],
                )
                connection.execute("COMMIT")
            except Exception:
                connection.execute("ROLLBACK")
                raise

    def mark(
        self,
        doc_url: str,
        status: str,
        *,
        error: str | None = None,
        source_bytes: int | None = None,
        markdown_hash: str | None = None,
        images: int = 0,
        increment_attempt: bool = True,
    ) -> None:
        with self._write_lock, self._connect() as connection:
            connection.execute(
                """
                UPDATE documents SET
                    status        = ?,
                    attempts      = attempts + ?,
                    last_error    = ?,
                    source_bytes  = COALESCE(?, source_bytes),
                    markdown_hash = COALESCE(?, markdown_hash),
                    images        = ?,
                    updated_at    = ?
                WHERE doc_url = ?
                """,
                (
                    status,
                    1 if increment_attempt else 0,
                    error,
                    source_bytes,
                    markdown_hash,
                    images,
                    time.time(),
                    doc_url,
                ),
            )

    def reset_failed(self) -> int:
        with self._write_lock, self._connect() as connection:
            cursor = connection.execute(
                "UPDATE documents SET status='pending', last_error=NULL "
                "WHERE status IN ('failed','skipped')"
            )
            return cursor.rowcount or 0

    def reset_all(self) -> int:
        with self._write_lock, self._connect() as connection:
            cursor = connection.execute(
                "UPDATE documents SET status='pending', attempts=0, last_error=NULL"
            )
            return cursor.rowcount or 0

    # -- okuma --------------------------------------------------------------------------

    def status_of(self, doc_url: str) -> str | None:
        with self._connect() as connection:
            row = connection.execute(
                "SELECT status FROM documents WHERE doc_url = ?", (doc_url,)
            ).fetchone()
        return row["status"] if row else None

    def hash_of(self, doc_url: str) -> str | None:
        """Bu dokumanin en son yazilan govde ozeti (degisiklik tespiti icin)."""
        with self._connect() as connection:
            row = connection.execute(
                "SELECT markdown_hash FROM documents WHERE doc_url = ?", (doc_url,)
            ).fetchone()
        return row["markdown_hash"] if row else None

    def all_hashes(self) -> dict[str, str]:
        """Tamamlanmis her dokumanin govde ozeti (indeks icin)."""
        with self._connect() as connection:
            return {
                row["doc_url"]: row["markdown_hash"]
                for row in connection.execute(
                    "SELECT doc_url, markdown_hash FROM documents "
                    "WHERE status = 'done' AND markdown_hash IS NOT NULL"
                )
            }

    def completed_urls(self) -> set[str]:
        with self._connect() as connection:
            return {
                row["doc_url"]
                for row in connection.execute(
                    "SELECT doc_url FROM documents WHERE status = 'done'"
                )
            }

    def counts(self) -> dict[str, int]:
        with self._connect() as connection:
            return {
                row["status"]: row["n"]
                for row in connection.execute(
                    "SELECT status, COUNT(*) AS n FROM documents GROUP BY status"
                )
            }

    def totals(self) -> dict[str, int]:
        with self._connect() as connection:
            row = connection.execute(
                "SELECT COALESCE(SUM(source_bytes),0) AS bytes, "
                "COALESCE(SUM(images),0) AS images FROM documents WHERE status='done'"
            ).fetchone()
        return {"bytes": row["bytes"], "images": row["images"]}

    def failures(self, limit: int = 100) -> list[sqlite3.Row]:
        with self._connect() as connection:
            return list(
                connection.execute(
                    "SELECT doc_url, title, breadcrumb, attempts, last_error "
                    "FROM documents WHERE status IN ('failed','skipped') "
                    "ORDER BY breadcrumb LIMIT ?",
                    (limit,),
                )
            )
