"""Bilgi tabani indeksini (``articles-manifest.csv``) uretir.

Depodaki ``knowledge-base/metadata/articles-manifest.schema.json`` sozlesmesine
birebir uyar: alanlar, sira ve ``additionalProperties: false`` kisiti dahil.
Boylece kazima ciktisi dogrudan RAG hattina beslenebilir.
"""

from __future__ import annotations

import csv
import datetime as dt
import logging
import os
import re
import uuid
from pathlib import Path
from typing import Iterable, Sequence

from netsis_scraper import catalog

log = logging.getLogger(__name__)

#: Semadaki alan sirasi. Sema ``additionalProperties: false`` dedigi icin
#: bu listeye fazladan sutun eklenemez.
FIELDS = (
    "article_id",
    "title",
    "module",
    "version",
    "source_url",
    "relative_path",
    "language",
    "last_updated",
    "tags",
    "breadcrumb",
    "depth",
    "is_section",
    "doc_cid",
    "content_sha256",
)

#: Semada ``"const": "3 Enterprise"`` olarak sabitlenmis.
PRODUCT_VERSION = "3 Enterprise"

#: Semada ``"enum": ["tr", "en"]``; kaynak dokumanlarin tamami Turkce.
LANGUAGE = "tr"

#: Semadaki ``relative_path`` kalibi: ``^markdown/.+\\.md$``.
PATH_PREFIX = "markdown/"

_ISO_DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})")
_CID_RE = re.compile(r"[?&]cid=([^&]+)")


def _doc_cid(doc_url: str) -> str:
    """Kaynak sistemdeki kalici dokuman kimligi.

    ``page_id`` 2.328 dugumun 112'sinde bos oldugu icin kimlik anahtari olarak
    kullanilamaz; ``cid`` hepsinde dolu ve benzersizdir.
    """
    match = _CID_RE.search(doc_url or "")
    return match.group(1) if match else ""


def _module_of(node: catalog.DocNode) -> str:
    """Makalenin ait oldugu modul adi.

    Kirinti yolu ``Kok / Bolum / Modul / ...`` seklinde ilerler; ``Muhasebe``,
    ``Lojistik - Satis``, ``Uretim`` gibi gercek modul adlari ucuncu seviyededir.
    O seviye yoksa bir ust bolum adi kullanilir.
    """
    trail = node.breadcrumb[1:]          # kok adini atla
    if len(trail) >= 2:
        return trail[1]
    return trail[0] if trail else "Genel"


def _last_updated(node: catalog.DocNode, fallback: str) -> str:
    """Semanin bekledigi ``date`` bicimi (YYYY-MM-DD).

    Agac dugumlerinin cogunda kaynak surum damgasi var
    (``2021-08-23T09:00:11.553+03:00``); olmayanlar icin calisma tarihi yazilir.
    """
    match = _ISO_DATE_RE.match(node.version or "")
    return match.group(1) if match else fallback


def build_rows(
    nodes: Sequence[catalog.DocNode],
    *,
    product: str,
    run_date: str | None = None,
    hashes: dict[str, str] | None = None,
) -> list[dict[str, str]]:
    """Agac dugumlerinden sema uyumlu indeks satirlari uretir.

    ``article_id`` agactaki gezinme sirasina gore verilir; sira kararli oldugu
    icin ayni agac her calismada ayni kimlikleri uretir.

    ``hashes`` verilirse (``doc_url -> markdown govde ozeti``), her satira
    ``content_sha256`` yazilir. RAG hatti boylece hangi makalelerin yeniden
    parcalanip yeniden gomulmesi gerektigini ozet karsilastirarak bulabilir.
    """
    run_date = run_date or dt.date.today().isoformat()
    hashes = hashes or {}
    rows: list[dict[str, str]] = []
    for index, node in enumerate(nodes, start=1):
        relative = PATH_PREFIX + str(node.relative_path).replace(os.sep, "/")
        rows.append(
            {
                "article_id": f"NETSIS-{index:04d}",
                "title": node.name,
                "module": _module_of(node),
                "version": PRODUCT_VERSION,
                "source_url": catalog.portal_url(node.doc_url, product),
                "relative_path": relative,
                "language": LANGUAGE,
                "last_updated": _last_updated(node, run_date),
                "tags": ";".join(node.breadcrumb[1:-1]),
                "breadcrumb": " / ".join(node.breadcrumb[1:]),
                "depth": str(node.depth),
                "is_section": "true" if node.is_branch else "false",
                "doc_cid": _doc_cid(node.doc_url),
                "content_sha256": hashes.get(node.doc_url, ""),
            }
        )
    return rows


def write_manifest(path: Path, rows: Iterable[dict[str, str]]) -> int:
    """Indeksi CSV olarak yazar; satir sonu ve alan sirasi kararlidir."""
    rows = list(rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{uuid.uuid4().hex[:8]}.tmp")
    try:
        with open(temporary, "w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(FIELDS), lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)
    log.info("Bilgi tabani indeksi yazildi: %s (%d makale)", path, len(rows))
    return len(rows)
