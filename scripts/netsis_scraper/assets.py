"""Dokuman icine gomulu ``data:`` gorsellerini diske ayirir.

Ornek kumede 64 dokumanda 843 gorsel vardi ve bunlarin yalnizca 210'u benzersizdi
(yuzde 75 tekrar). Bu yuzden gorseller icerik ozetine (sha256) gore adlandirilir ve
tekrar edenler tek dosyaya baglanir.

Ayrica kaynak HTML'de MIME turu **yanlistir**: butun gorseller ``image/png`` olarak
bildirilir ama ornek kumede 843 gorselin cogu aslinda JPEG'dir. Bu nedenle uzanti
bildirilen turden degil, dosyanin sihirli baytlarindan belirlenir.
"""

from __future__ import annotations

import base64
import binascii
import hashlib
import logging
import os
import re
import threading
from pathlib import Path

log = logging.getLogger(__name__)

_DATA_URI_RE = re.compile(r"^data:(?P<mime>[^;,]*)(?P<params>;[^,]*)?,(?P<payload>.*)$", re.DOTALL)

#: Sihirli baytlardan gercek bicimi belirleyen tablo (uzun on ekler once denenir).
_MAGIC: tuple[tuple[bytes, str], ...] = (
    (b"\x89PNG\r\n\x1a\n", ".png"),
    (b"\xff\xd8\xff", ".jpg"),
    (b"GIF87a", ".gif"),
    (b"GIF89a", ".gif"),
    (b"BM", ".bmp"),
    (b"II*\x00", ".tif"),
    (b"MM\x00*", ".tif"),
    (b"%PDF-", ".pdf"),
)

_MIME_FALLBACK = {
    "image/png": ".png",
    "image/jpeg": ".jpg",
    "image/jpg": ".jpg",
    "image/gif": ".gif",
    "image/webp": ".webp",
    "image/bmp": ".bmp",
    "image/tiff": ".tif",
    "image/svg+xml": ".svg",
}


def sniff_extension(payload: bytes, declared_mime: str = "") -> str:
    """Dosya uzantisini once sihirli baytlardan, olmazsa bildirilen MIME'dan bulur."""
    for magic, extension in _MAGIC:
        if payload.startswith(magic):
            return extension
    head = payload[:512].lstrip()
    if head.startswith(b"RIFF") and b"WEBP" in payload[:32]:
        return ".webp"
    if head.startswith(b"<svg") or (head.startswith(b"<?xml") and b"<svg" in payload[:512]):
        return ".svg"
    return _MIME_FALLBACK.get(declared_mime.strip().lower(), ".bin")


class AssetStore:
    """Gorselleri ortak bir klasore yazan, icerik ozetine gore tekilleyen depo.

    Is parcacigi guvenlidir: ayni gorseli iki calisan ayni anda yazmaya calisirsa
    gecici dosya + ``os.replace`` sayesinde sonuc bozulmaz.
    """

    def __init__(self, assets_dir: Path, *, enabled: bool = True, dry_run: bool = False) -> None:
        self.assets_dir = assets_dir
        self.enabled = enabled
        self.dry_run = dry_run
        self._known: dict[str, str] = {}
        self._lock = threading.Lock()
        self.bytes_written = 0
        self.files_written = 0
        self.duplicates_skipped = 0

    def store_data_uri(self, uri: str) -> tuple[str | None, int]:
        """``data:`` adresini diske yazar; ``(dosya adi, bayt sayisi)`` dondurur.

        Cozulemeyen adreslerde ``(None, 0)`` doner; cagiran taraf gorseli atlar.
        """
        if not self.enabled:
            return None, 0

        match = _DATA_URI_RE.match(uri.strip())
        if not match:
            return None, 0
        params = match.group("params") or ""
        if "base64" not in params.lower():
            return None, 0

        raw = re.sub(r"\s+", "", match.group("payload"))
        raw += "=" * (-len(raw) % 4)
        try:
            payload = base64.b64decode(raw, validate=False)
        except (binascii.Error, ValueError):
            log.warning("Bir gorselin base64 govdesi cozulemedi, atlandi.")
            return None, 0
        if not payload:
            return None, 0

        digest = hashlib.sha256(payload).hexdigest()
        with self._lock:
            existing = self._known.get(digest)
            if existing is not None:
                self.duplicates_skipped += 1
                return existing, len(payload)

        filename = f"{digest[:20]}{sniff_extension(payload, match.group('mime'))}"
        if not self.dry_run:
            self._write(filename, payload)

        with self._lock:
            self._known.setdefault(digest, filename)
            self.bytes_written += len(payload)
            self.files_written += 1
        return filename, len(payload)

    def _write(self, filename: str, payload: bytes) -> None:
        self.assets_dir.mkdir(parents=True, exist_ok=True)
        target = self.assets_dir / filename
        if target.exists() and target.stat().st_size == len(payload):
            return  # onceki calismadan kalmis, ayni icerik
        temporary = target.with_name(f".{filename}.{os.getpid()}.{threading.get_ident()}.tmp")
        try:
            temporary.write_bytes(payload)
            os.replace(temporary, target)
        finally:
            temporary.unlink(missing_ok=True)

    def adopt_existing(self) -> int:
        """Onceki calismadan kalan gorselleri tanir; boylece tekrar yazilmazlar."""
        if not self.assets_dir.is_dir():
            return 0
        count = 0
        for path in self.assets_dir.iterdir():
            if not path.is_file() or path.name.startswith("."):
                continue
            stem = path.stem
            if len(stem) == 20 and all(c in "0123456789abcdef" for c in stem):
                # Dosya adi ozetinin ilk 20 hanesi; tam ozeti icerikten dogrula.
                try:
                    digest = hashlib.sha256(path.read_bytes()).hexdigest()
                except OSError:
                    continue
                if digest.startswith(stem):
                    self._known.setdefault(digest, path.name)
                    count += 1
        if count:
            log.info("%d gorsel onceki calismadan devralindi.", count)
        return count
