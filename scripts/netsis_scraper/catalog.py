"""Dokuman hiyerarsisini (agac) alir, CSV girdisiyle eslestirir ve cikti yollarini planlar.

Hiyerarsi, portalin kendi API'sinden gelir::

    GET https://polaris.logo.com.tr/api/Documents/GetAuthorizedTrees?product=netsis-3-enterprise

Yanit ``{"Public": "<cift kodlanmis JSON>", "Others": []}`` bicimindedir. Cozuldugunde
her dugumde ``name``, ``doc_url``, ``page_id``, ``slug_name`` ve ``children`` alanlari bulunur.
``doc_url`` degeri, CSV'deki baglantilarin base64 govdesiyle birebir aynidir; iki kaynak
bu alan uzerinden eslestirilir.
"""

from __future__ import annotations

import base64
import binascii
import csv
import dataclasses
import io
import json
import logging
import urllib.parse
from pathlib import Path
from typing import Iterable, Iterator, Sequence

import requests

from netsis_scraper import config
from netsis_scraper.paths import (
    MAX_SEGMENT_LENGTH,
    SegmentAllocator,
    sanitize_segment,
    shorten_relative_path,
)

log = logging.getLogger(__name__)


# --------------------------------------------------------------------------------------
# Portal baglantilarinin base64 govdesi
# --------------------------------------------------------------------------------------

def _looks_like_doc_url(text: str) -> bool:
    """Cozulen metnin gercekten bir dokuman adresi olup olmadigini dogrular."""
    return text.startswith("external") and "cid=" in text and "link=" in text


def decode_detail_segment(segment: str) -> str | None:
    """`/detail/<segment>` parcasini cozer ve ``external?cid=...`` metnini dondurur.

    Portalin Angular kodu bu parcayi uc bicimde uretebiliyor ve okurken de ayni sirayla
    deniyor; burada aynisi uygulanir:

    1. **base64url** - CSV'deki baglantilarin tamami boyledir
       (``btoa(unescape(encodeURIComponent(x)))`` + ``+ -> -``, ``/ -> _``, ``=`` kirpilmis).
    2. **cift URL kodlamasi** - dokuman govdesindeki ic baglantilar boyledir
       (ornek: ``external%253Fcid%253D...``).
    3. **tek URL kodlamasi** - eski baglantilar icin son care.

    Her adimin sonucu ``external...cid=...link=`` kalibina uyuyor mu diye dogrulanir;
    uymuyorsa bir sonraki bicim denenir. Hicbiri tutmazsa ``None`` doner.
    """
    if not segment:
        return None
    segment = segment.strip()

    normalized = segment.replace("-", "+").replace("_", "/")
    normalized += "=" * (-len(normalized) % 4)
    try:
        candidate = base64.b64decode(normalized, validate=False).decode("utf-8")
    except (binascii.Error, UnicodeDecodeError, ValueError):
        candidate = ""
    if _looks_like_doc_url(candidate):
        return candidate

    for _ in range(2):
        segment = urllib.parse.unquote(segment)
        if _looks_like_doc_url(segment):
            return segment

    return None


def doc_url_from_link(href: str) -> str | None:
    """Bir ``href`` degerinden dokuman adresini cikarir (portal ya da DYS baglantisi)."""
    if not href:
        return None
    cleaned = href.split("#", 1)[0].strip()
    if "/detail/" in cleaned:
        return decode_detail_segment(cleaned.rsplit("/detail/", 1)[1])
    # Dogrudan DYS adresi: https://dys.logo.cloud/external?cid=...
    parsed = urllib.parse.urlsplit(cleaned)
    if parsed.path.strip("/").endswith("external") and parsed.query:
        candidate = f"external?{parsed.query}"
        return candidate if _looks_like_doc_url(candidate) else None
    return None


def encode_detail_segment(doc_url: str) -> str:
    """``external?cid=...`` metnini portal baglantisindaki base64 govdesine cevirir."""
    raw = base64.b64encode(doc_url.encode("utf-8")).decode("ascii")
    return raw.replace("+", "-").replace("/", "_").rstrip("=")


def portal_url(doc_url: str, product: str = config.DEFAULT_PRODUCT) -> str:
    """Bir dugumun insan tarafindan acilabilir portal adresini uretir."""
    return f"{config.PORTAL_BASE_URL}/docs/{product}/detail/{encode_detail_segment(doc_url)}"


# --------------------------------------------------------------------------------------
# Agac dugumu
# --------------------------------------------------------------------------------------

@dataclasses.dataclass(slots=True)
class DocNode:
    """Agactaki tek bir dokuman."""

    page_id: str
    name: str
    doc_url: str
    breadcrumb: tuple[str, ...]        # kok dahil, kendi adi dahil
    depth: int
    order: int                          # kardesleri arasindaki sirasi (0 tabanli)
    is_branch: bool                     # alt basliklari var mi
    slug_name: str = ""
    version: str = ""
    relative_path: Path = dataclasses.field(default_factory=Path)
    in_csv: bool = False

    @property
    def key(self) -> str:
        """Durum veritabaninda kullanilan kararli birincil anahtar."""
        return self.doc_url

    @property
    def parent_breadcrumb(self) -> tuple[str, ...]:
        return self.breadcrumb[:-1]


# --------------------------------------------------------------------------------------
# Agacin alinmasi
# --------------------------------------------------------------------------------------

def fetch_catalog(
    session: requests.Session,
    product: str = config.DEFAULT_PRODUCT,
    timeout: tuple[float, float] | None = None,
) -> dict:
    """Hiyerarsi agacini API'den indirir ve cozulmus sozluk olarak dondurur."""
    url = f"{config.CATALOG_API_BASE}/api/Documents/GetAuthorizedTrees"
    timeout = timeout or (config.CONNECT_TIMEOUT, config.READ_TIMEOUT)
    log.info("Hiyerarsi agaci aliniyor: %s?product=%s", url, product)
    response = session.get(url, params={"product": product}, timeout=timeout)
    response.raise_for_status()
    payload = response.json()
    return _decode_catalog_payload(payload)


def _decode_catalog_payload(payload: dict) -> dict:
    """API yanitindaki cift kodlanmis ``Public`` alanini coz.

    ``Others`` alani yetkili kullanicilara ozel agaclari tasir; anonim erisimde bos
    gelir ama gelirse ayni bicimde cozulup koke eklenir.
    """
    public_raw = payload.get("Public")
    if not public_raw:
        raise ValueError("Agac yanitinda 'Public' alani bos geldi.")

    root = json.loads(public_raw)
    if isinstance(root, str):          # cift kodlama: once metin, sonra JSON
        root = json.loads(root)

    extras: list[dict] = []
    for other in payload.get("Others") or []:
        try:
            decoded = json.loads(other)
            if isinstance(decoded, str):
                decoded = json.loads(decoded)
        except (TypeError, ValueError):
            log.warning("'Others' icindeki bir agac cozulemedi, atlaniyor.")
            continue
        if isinstance(decoded, list):
            extras.extend(x for x in decoded if isinstance(x, dict))
        elif isinstance(decoded, dict):
            extras.append(decoded)

    if extras:
        log.info("%d adet ek (yetkiye bagli) agac koke eklendi.", len(extras))
        root.setdefault("children", []).extend(extras)

    return root


def load_cached_catalog(path: Path) -> dict:
    """Daha once diske yazilmis agaci okur (cevrimdisi calisma icin)."""
    return json.loads(path.read_text(encoding="utf-8"))


def save_catalog_cache(path: Path, root: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(root, ensure_ascii=False, indent=1, sort_keys=True),
        encoding="utf-8",
    )


# --------------------------------------------------------------------------------------
# Agacin duzlestirilmesi
# --------------------------------------------------------------------------------------

def flatten(root: dict) -> list[DocNode]:
    """Agaci, gezinme sirasini koruyan duz bir listeye cevirir."""
    nodes: list[DocNode] = []

    def walk(raw: dict, trail: tuple[str, ...], depth: int, order: int) -> None:
        name = (raw.get("name") or "").strip() or "Adsiz"
        doc_url = raw.get("doc_url") or ""
        children = raw.get("children") or []
        breadcrumb = trail + (name,)
        if doc_url:
            nodes.append(
                DocNode(
                    page_id=str(raw.get("page_id") or ""),
                    name=name,
                    doc_url=doc_url,
                    breadcrumb=breadcrumb,
                    depth=depth,
                    order=order,
                    is_branch=bool(children),
                    slug_name=raw.get("slug_name") or "",
                    version=raw.get("version") or "",
                )
            )
        else:
            log.warning("doc_url alani olmayan dugum atlandi: %s", " / ".join(breadcrumb))
        for index, child in enumerate(children):
            if isinstance(child, dict):
                walk(child, breadcrumb, depth + 1, index)

    walk(root, (), 0, 0)
    return nodes


# --------------------------------------------------------------------------------------
# Cikti yollarinin planlanmasi
# --------------------------------------------------------------------------------------

def plan_paths(
    nodes: Sequence[DocNode],
    *,
    number_prefix: bool = False,
    max_relative_path: int = config.MAX_RELATIVE_PATH,
) -> None:
    """Her dugum icin ``relative_path`` alanini doldurur (yerinde degistirir).

    Kurallar:

    * Alt basligi olan dugum bir klasor olur; kendi icerigi o klasorun icine
      ``index.md`` olarak yazilir. Boylece hem hiyerarsi hem de kendi metni korunur.
    * Yaprak dugum, ust klasorunun icinde ``<ad>.md`` olur.
    * Ayni klasordeki cakisan adlar ``(2)``, ``(3)`` ekiyle ayrilir; karsilastirma
      Windows/macOS gibi buyuk-kucuk harf duyarsiz dosya sistemleri icin
      kucuk harfe indirgenerek yapilir.
    * Goreli yol ``max_relative_path`` sinirini asarsa parcalar kisaltilir; bu sinir
      cikti klasorunun yerinden bagimsizdir, yani cikti her makinede aynidir.
    """
    allocator = SegmentAllocator()
    # Agactaki her dugumun (breadcrumb -> guvenli klasor adi) esleme tablosu.
    directory_for: dict[tuple[str, ...], tuple[str, ...]] = {(): ()}

    # Kok dugumu ciktinin en ustune serelim: kokun kendi adi klasor olmasin.
    root_breadcrumb = nodes[0].breadcrumb if nodes else ()
    if root_breadcrumb:
        directory_for[root_breadcrumb] = ()

    ordered = sorted(nodes, key=lambda n: (n.depth, n.breadcrumb))
    for node in ordered:
        parent_dir = directory_for.get(node.parent_breadcrumb)
        if parent_dir is None:
            # Ust dugum agacta doc_url'siz oldugu icin atlanmis olabilir; adindan uret.
            parent_dir = tuple(
                sanitize_segment(part) for part in node.parent_breadcrumb[1:]
            )
            directory_for[node.parent_breadcrumb] = parent_dir

        label = sanitize_segment(node.name)
        if number_prefix:
            label = f"{node.order + 1:03d} {label}"
            if len(label) > MAX_SEGMENT_LENGTH:
                label = label[:MAX_SEGMENT_LENGTH].rstrip(" .-")

        if node.breadcrumb == root_breadcrumb:
            # Kok dugumun kendi icerigi ciktinin en ustundeki index.md olur.
            node.relative_path = Path(config.BRANCH_DOCUMENT_FILENAME)
            continue

        if node.is_branch:
            unique = allocator.allocate(parent_dir, label)
            own_dir = parent_dir + (unique,)
            directory_for[node.breadcrumb] = own_dir
            parts = list(own_dir) + [config.BRANCH_DOCUMENT_FILENAME]
        else:
            unique = allocator.allocate(parent_dir, f"{label}.md")
            parts = list(parent_dir) + [unique]

        # Butce cikti klasorunun uzunlugundan bagimsizdir; boylece ayni agac her
        # makinede birebir ayni dosya adlarini uretir.
        parts = shorten_relative_path(parts, max_relative_path)
        node.relative_path = Path(*parts)


# --------------------------------------------------------------------------------------
# CSV girdisi
# --------------------------------------------------------------------------------------

def check_absolute_path_lengths(
    nodes: Sequence[DocNode], output_dir: Path, limit: int = 259
) -> list[tuple[int, Path]]:
    """Mutlak yolu Windows sinirini asacak dokumanlari bulur (uyari amacli).

    Yol butcesi bilerek goreli tutulur; buradaki kontrol yalnizca kullaniciya
    "cikti klasorunu daha kisa bir yere alin" demek icindir.
    """
    base = len(str(output_dir)) + 1
    too_long = [
        (base + len(str(node.relative_path)), node.relative_path)
        for node in nodes
        if base + len(str(node.relative_path)) > limit
    ]
    return sorted(too_long, reverse=True)


def read_link_csv(path: Path) -> list[tuple[str, str]]:
    """Kullanicinin ``Baslik;URL`` bicimli CSV dosyasini okur.

    Dosya UTF-8 BOM ile baslayabilir, satir sonlari CRLF olabilir ve ayirici
    noktali virguldur; ucu de burada ele alinir. Ayirici otomatik sezilir.
    """
    raw = path.read_bytes().decode("utf-8-sig")
    sample = raw[:4096]
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=";,\t|")
        delimiter = dialect.delimiter
    except csv.Error:
        delimiter = ";" if sample.count(";") >= sample.count(",") else ","

    rows: list[tuple[str, str]] = []
    for line_no, row in enumerate(csv.reader(io.StringIO(raw), delimiter=delimiter), 1):
        if not row or not any(cell.strip() for cell in row):
            continue
        if len(row) < 2:
            log.warning("CSV %s: %d. satirda URL sutunu yok, atlandi: %r", path, line_no, row)
            continue
        title, url = row[0].strip(), row[1].strip()
        if not url.lower().startswith("http"):
            # Basliksiz/tersine yazilmis satirlar icin ikinci bir sans.
            if title.lower().startswith("http"):
                title, url = url, title
            else:
                log.warning("CSV %s: %d. satirda gecerli URL yok, atlandi: %r", path, line_no, row)
                continue
        rows.append((title, url))
    return rows


def csv_doc_urls(rows: Iterable[tuple[str, str]]) -> dict[str, str]:
    """CSV satirlarini ``doc_url -> baslik`` esleme tablosuna cevirir."""
    mapping: dict[str, str] = {}
    for title, url in rows:
        _, _, segment = url.partition("/detail/")
        decoded = decode_detail_segment(segment)
        if decoded:
            mapping[decoded] = title
        else:
            log.warning("CSV baglantisinin base64 govdesi cozulemedi: %s", url)
    return mapping


def annotate_csv_membership(nodes: Sequence[DocNode], wanted: dict[str, str]) -> dict[str, int]:
    """Agac dugumlerini CSV ile eslestirir ve kapsama ozetini dondurur."""
    tree_urls = {node.doc_url for node in nodes}
    for node in nodes:
        node.in_csv = node.doc_url in wanted
    missing = sorted(set(wanted) - tree_urls)
    for doc_url in missing:
        log.warning("CSV'de olup agacta bulunmayan dokuman: %s (%s)", wanted[doc_url], doc_url)
    return {
        "csv_rows": len(wanted),
        "tree_nodes": len(nodes),
        "matched": sum(1 for node in nodes if node.in_csv),
        "csv_only": len(missing),
        "tree_only": len(tree_urls - set(wanted)),
    }


def select_nodes(
    nodes: Sequence[DocNode],
    *,
    include_branches: bool,
    csv_filter: bool,
) -> list[DocNode]:
    """Indirilecek dugumleri secer; agactaki gezinme sirasini korur."""
    selected: list[DocNode] = []
    for node in nodes:
        if csv_filter and not node.in_csv:
            continue
        if node.is_branch and not include_branches:
            continue
        selected.append(node)
    return selected


def iter_breadcrumb_labels(node: DocNode) -> Iterator[str]:
    """Kok adini atlayarak okunabilir kirinti yolu uretir."""
    yield from node.breadcrumb[1:]
