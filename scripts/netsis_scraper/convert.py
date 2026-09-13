"""Logo DYS dokuman HTML'ini temiz Markdown'a cevirir.

Kaynak HTML'in olculmus ozellikleri (64 dokumanlik ornek kume uzerinde):

* Her dokuman ``<h1>`` ile baslar; ``<h2>``..``<h6>`` hic kullanilmaz. Bu yuzden
  belge ici baslik hiyerarsisi degil, **agac hiyerarsisi** anlamlidir; o da klasor
  yapisi ve on bilgi (front matter) ile korunur.
* Tablolar ``polarisTable``/``polarisTh``/``polarisTd`` siniflarini kullanir ve
  ``colspan`` iceren tablolar vardir.
* ``div.polaris-information-macro`` bir bilgi/uyari kutusudur.
* Butun gorseller satir ici ``data:`` adresidir.
* Metin icinde gecen ``<tab>`` (klavyedeki Tab tusu) gecerli bir HTML etiketi
  degildir; hicbir ayristirici onu korumaz. 64 dosyanin 25'inde toplam 224 kez
  gecer ve onlem alinmazsa **sessizce kaybolur**. Bu yuzden ayristirmadan once
  bilinmeyen etiketler metne kacislanir.
"""

from __future__ import annotations

import html as html_lib
import logging
import re
from dataclasses import dataclass, field
from typing import Callable, Iterable

from bs4 import BeautifulSoup, NavigableString, Tag

from netsis_scraper.assets import AssetStore

log = logging.getLogger(__name__)


# --------------------------------------------------------------------------------------
# Bilinmeyen (sahte) etiketlerin korunmasi
# --------------------------------------------------------------------------------------

#: HTML5 ve hala karsilasilan eski etiketlerin tamami.
KNOWN_TAGS = frozenset(
    """
    a abbr acronym address area article aside audio b base bdi bdo big blockquote body br
    button canvas caption center cite code col colgroup data datalist dd del details dfn
    dialog div dl dt em embed fieldset figcaption figure font footer form frame frameset h1
    h2 h3 h4 h5 h6 head header hgroup hr html i iframe img input ins kbd label legend li link
    main map mark marquee math menu meta meter nav nobr noframes noscript object ol optgroup
    option output p param picture pre progress q rp rt ruby s samp script search section
    select slot small source span strike strong style sub summary sup svg table tbody td
    template textarea tfoot th thead time title tr track tt u ul var video wbr
    """.split()
)

_TAG_LIKE_RE = re.compile(
    r"<(?P<slash>/?)\s*(?P<name>[A-Za-z][A-Za-z0-9_:-]*)(?P<rest>(?:\"[^\"]*\"|'[^']*'|[^>\"'])*)>"
)


def protect_pseudo_tags(markup: str, counter: dict[str, int] | None = None) -> str:
    """Bilinmeyen etiketleri gorunur metne cevirir.

    Acilis etiketi (``<tab>``) yazarin kastettigi gorunur metindir ve kacislanarak
    korunur. Ayni sahte etiketin kapanisi (``</tab>``) yalnizca artik bir isarettir;
    tarayicida da gorunmez, bu yuzden silinir.
    """
    def replace(match: re.Match[str]) -> str:
        name = match.group("name").lower()
        if name in KNOWN_TAGS:
            return match.group(0)
        if counter is not None:
            counter[name] = counter.get(name, 0) + 1
        if match.group("slash"):
            return ""  # sahte kapanis etiketi: at
        return html_lib.escape(match.group(0))

    return _TAG_LIKE_RE.sub(replace, markup)


# --------------------------------------------------------------------------------------
# Markdown kacislama
# --------------------------------------------------------------------------------------

_INLINE_ESCAPE_RE = re.compile(r"([\\`*_\[\]<>])")
_LINE_START_ESCAPE_RE = re.compile(r"^(\s*)([#>+-]|\d+[.)])(\s)")


def escape_inline(text: str) -> str:
    """Markdown'da anlam tasiyan karakterleri kacislar (metni oldugu gibi gosterir)."""
    return _INLINE_ESCAPE_RE.sub(r"\\\1", text)


def escape_line_start(line: str) -> str:
    """Satir basindaki liste/baslik isaretlerinin yanlislikla yorumlanmasini onler."""
    return _LINE_START_ESCAPE_RE.sub(r"\1\\\2\3", line)


# --------------------------------------------------------------------------------------
# Sonuc
# --------------------------------------------------------------------------------------

@dataclass(slots=True)
class ConversionResult:
    """Bir dokumanin donusum ciktisi ve donusum sirasinda toplanan olcumler."""

    markdown: str
    title: str
    images: int = 0
    image_bytes: int = 0
    tables_gfm: int = 0
    tables_html: int = 0
    internal_links: int = 0
    unresolved_links: int = 0
    pseudo_tags: dict[str, int] = field(default_factory=dict)
    warnings: list[str] = field(default_factory=list)


#: Bir ``doc_url`` degerini cikti agacindaki goreli ``.md`` yoluna ceviren geri cagri.
LinkResolver = Callable[[str], str | None]


# --------------------------------------------------------------------------------------
# Donusturucu
# --------------------------------------------------------------------------------------

_BLOCK_TAGS = frozenset(
    "address article aside blockquote details div dl fieldset figcaption figure footer form "
    "h1 h2 h3 h4 h5 h6 header hgroup hr li main nav ol p pre section table ul".split()
)

#: ``polaris-information-macro-<tur>`` son ekinin GFM uyari kutusuna esleniyor.
_CALLOUT_KINDS = {
    "information": ("NOTE", "Bilgi"),
    "note": ("NOTE", "Not"),
    "tip": ("TIP", "Ipucu"),
    "success": ("TIP", "Basarili"),
    "warning": ("WARNING", "Uyari"),
    "error": ("CAUTION", "Dikkat"),
    "danger": ("CAUTION", "Dikkat"),
}


class MarkdownConverter:
    """HTML belgesini Markdown'a ceviren, durumsuz (yeniden kullanilabilir) donusturucu."""

    def __init__(
        self,
        *,
        asset_store: AssetStore | None = None,
        link_resolver: LinkResolver | None = None,
        image_mode: str = "files",
        assets_href_prefix: str = "",
        parser: str | None = None,
    ) -> None:
        self.asset_store = asset_store
        self.link_resolver = link_resolver
        self.image_mode = image_mode          # files | inline | skip
        self.assets_href_prefix = assets_href_prefix
        self.parser = parser or _pick_parser()

    # -- giris noktasi -------------------------------------------------------------------

    def convert(self, markup: str) -> ConversionResult:
        pseudo: dict[str, int] = {}
        soup = BeautifulSoup(protect_pseudo_tags(markup, pseudo), self.parser)

        for junk in soup.find_all(["script", "style", "noscript"]):
            junk.decompose()

        result = ConversionResult(markdown="", title="", pseudo_tags=pseudo)

        heading = soup.find("h1")
        if heading is not None:
            result.title = _collapse(heading.get_text(" ", strip=True))
        if not result.title and soup.title and soup.title.string:
            result.title = _collapse(soup.title.string)

        body = soup.body or soup
        blocks = list(self._render_children(body, result))
        result.markdown = _join_blocks(blocks)
        return result

    # -- blok duzeyi ---------------------------------------------------------------------

    def _render_children(self, node: Tag, result: ConversionResult) -> Iterable[str]:
        """Bir dugumun cocuklarini blok listesine cevirir.

        Ard arda gelen satir ici parcalar tek bir paragrafta toplanir; boylece
        ``<span>`` yiginlari yuzunden metin parcalanmaz.
        """
        pending: list[str] = []

        def flush() -> Iterable[str]:
            if pending:
                text = _collapse("".join(pending))
                pending.clear()
                if text:
                    yield escape_line_start(text)

        for child in node.children:
            if isinstance(child, NavigableString):
                pending.append(escape_inline(str(child)))
                continue
            if not isinstance(child, Tag):
                continue
            name = child.name.lower()
            if name in _BLOCK_TAGS or name == "br":
                yield from flush()
                yield from self._render_block(child, result)
            else:
                pending.append(self._render_inline(child, result))

        yield from flush()

    def _render_block(self, tag: Tag, result: ConversionResult) -> Iterable[str]:
        name = tag.name.lower()

        if name == "br":
            return

        if name in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            level = int(name[1])
            text = _collapse(self._render_inline(tag, result))
            if text:
                yield f"{'#' * level} {text}"
            return

        if name == "hr":
            yield "---"
            return

        if name in {"ul", "ol"}:
            yield from self._render_list(tag, result, ordered=(name == "ol"), depth=0)
            return

        if name == "table":
            yield from self._render_table(tag, result)
            return

        if name == "pre":
            code = tag.get_text("", strip=False).strip("\n")
            yield "```\n" + code + "\n```"
            return

        if name == "blockquote":
            inner = _join_blocks(list(self._render_children(tag, result)))
            if inner:
                yield _prefix_lines(inner, "> ")
            return

        if name == "div":
            callout = self._callout_kind(tag)
            if callout is not None:
                marker, label = callout
                body_tag = tag.find("div", class_="polaris-information-macro-body") or tag
                inner = _join_blocks(list(self._render_children(body_tag, result)))
                if not inner:
                    return
                yield f"> [!{marker}]\n" + _prefix_lines(inner, "> ")
                return

        # p, div ve diger genel bloklar
        yield from self._render_children(tag, result)

    @staticmethod
    def _callout_kind(tag: Tag) -> tuple[str, str] | None:
        classes = {c.lower() for c in (tag.get("class") or [])}
        if "polaris-information-macro" not in classes:
            return None
        for css in classes:
            if css.startswith("polaris-information-macro-"):
                suffix = css[len("polaris-information-macro-"):]
                if suffix in _CALLOUT_KINDS:
                    return _CALLOUT_KINDS[suffix]
        return _CALLOUT_KINDS["information"]

    def _render_list(
        self, tag: Tag, result: ConversionResult, *, ordered: bool, depth: int
    ) -> Iterable[str]:
        lines: list[str] = []
        indent = "  " * depth
        index = 1
        for item in tag.find_all("li", recursive=False):
            nested: list[str] = []
            inline_parts: list[str] = []
            for child in item.children:
                if isinstance(child, Tag) and child.name and child.name.lower() in {"ul", "ol"}:
                    nested.extend(
                        self._render_list(
                            child, result, ordered=(child.name.lower() == "ol"), depth=depth + 1
                        )
                    )
                elif isinstance(child, NavigableString):
                    inline_parts.append(escape_inline(str(child)))
                elif isinstance(child, Tag):
                    if child.name.lower() in _BLOCK_TAGS:
                        inline_parts.append(
                            " ".join(_collapse(b) for b in self._render_children(child, result))
                        )
                    else:
                        inline_parts.append(self._render_inline(child, result))
            text = _collapse("".join(inline_parts))
            bullet = f"{index}." if ordered else "-"
            lines.append(f"{indent}{bullet} {text}".rstrip())
            lines.extend(nested)
            index += 1
        if lines:
            yield "\n".join(lines)

    # -- tablolar -------------------------------------------------------------------------

    def _render_table(self, tag: Tag, result: ConversionResult) -> Iterable[str]:
        """Basit tablolari GFM'e cevirir; ifade edilemeyenlerde HTML'e duser.

        GFM tablolari ``rowspan``/``colspan`` ve hucre icinde blok icerik ifade
        edemez. Bu durumlarda veriyi bozmaktansa temizlenmis HTML olarak birakmak
        daha dogrudur; Markdown gorunturuculeri ham HTML'i zaten isler.
        """
        rows = tag.find_all("tr")
        if not rows:
            return

        if tag.find("table") is not None:
            yield self._table_as_html(tag, result)
            result.tables_html += 1
            return

        grid: list[list[str]] = []
        header_flags: list[bool] = []
        for row in rows:
            cells = row.find_all(["td", "th"], recursive=False)
            if not cells:
                continue
            for cell in cells:
                span = _int_attr(cell, "colspan")
                rspan = _int_attr(cell, "rowspan")
                if span > 1 or rspan > 1:
                    yield self._table_as_html(tag, result)
                    result.tables_html += 1
                    return
            grid.append([self._cell_text(cell, result) for cell in cells])
            header_flags.append(all(c.name.lower() == "th" for c in cells))

        if not grid:
            return
        width = max(len(r) for r in grid)
        if width == 0:
            return
        grid = [r + [""] * (width - len(r)) for r in grid]

        if header_flags[0]:
            header, body = grid[0], grid[1:]
        else:
            header, body = [""] * width, grid

        lines = [
            "| " + " | ".join(header) + " |",
            "| " + " | ".join(["---"] * width) + " |",
        ]
        lines.extend("| " + " | ".join(row) + " |" for row in body)
        result.tables_gfm += 1
        yield "\n".join(lines)

    def _cell_text(self, cell: Tag, result: ConversionResult) -> str:
        """Hucre icerigini tek satirlik GFM hucresine sigdirir."""
        parts = [_collapse(block) for block in self._render_children(cell, result)]
        text = " ".join(p for p in parts if p)
        text = text.replace("|", "\\|")
        return re.sub(r"\s*\n\s*", "<br>", text).strip()

    def _table_as_html(self, tag: Tag, result: ConversionResult) -> str:
        """Karmasik tabloyu, gorselleri de cozerek sadelestirilmis HTML olarak birakir."""
        clone = BeautifulSoup(str(tag), self.parser)
        for image in clone.find_all("img"):
            source = image.get("src") or ""
            if source.startswith("data:"):
                markdown = self._image_markdown(source, image.get("alt") or "", result)
                replacement = _extract_url(markdown)
                if replacement:
                    image["src"] = replacement
                else:
                    image.decompose()
                    continue
            for attribute in ("style", "class", "width", "height"):
                image.attrs.pop(attribute, None)
        for element in clone.find_all(True):
            if element.name.lower() in {"table", "thead", "tbody", "tr", "th", "td"}:
                for attribute in ("style", "class", "colgroup"):
                    element.attrs.pop(attribute, None)
        for element in clone.find_all(["colgroup", "col"]):
            element.decompose()
        table = clone.find("table")
        return str(table) if table is not None else ""

    # -- satir ici ------------------------------------------------------------------------

    def _render_inline(self, node: Tag | NavigableString, result: ConversionResult) -> str:
        if isinstance(node, NavigableString):
            return escape_inline(str(node))
        if not isinstance(node, Tag):
            return ""

        name = node.name.lower()

        if name == "br":
            return "\n"
        if name == "img":
            return self._image_markdown(node.get("src") or "", node.get("alt") or "", result)
        if name == "a":
            return self._link_markdown(node, result)

        inner = "".join(self._render_inline(child, result) for child in node.children)

        if name in {"strong", "b"}:
            return _wrap(inner, "**")
        if name in {"em", "i"}:
            return _wrap(inner, "*")
        if name in {"del", "s", "strike"}:
            return _wrap(inner, "~~")
        if name in {"code", "kbd", "samp", "tt"}:
            text = _collapse(html_lib.unescape(node.get_text("", strip=False)))
            return f"`{text}`" if text else ""
        if name == "sub":
            return f"<sub>{inner}</sub>" if inner.strip() else ""
        if name == "sup":
            return f"<sup>{inner}</sup>" if inner.strip() else ""
        return inner

    def _image_markdown(self, source: str, alt: str, result: ConversionResult) -> str:
        if self.image_mode == "skip" or not source:
            return ""
        alt_text = escape_inline(_collapse(alt)) if alt else ""

        if not source.startswith("data:"):
            return f"![{alt_text}]({source})"

        if self.image_mode == "inline":
            result.images += 1
            return f"![{alt_text}]({source})"

        if self.asset_store is None:
            return ""
        filename, size = self.asset_store.store_data_uri(source)
        if not filename:
            result.warnings.append("Bir gorsel cozulemedi ve atlandi.")
            return ""
        result.images += 1
        result.image_bytes += size
        return f"![{alt_text}]({self.assets_href_prefix}{filename})"

    def _link_markdown(self, node: Tag, result: ConversionResult) -> str:
        inner = "".join(self._render_inline(child, result) for child in node.children)
        label = _collapse(inner)
        href = (node.get("href") or "").strip()

        if not href:
            return label
        if not label:
            label = escape_inline(href)

        target = href
        if self.link_resolver is not None and "/detail/" in href:
            resolved = self.link_resolver(href)
            if resolved:
                target = resolved
                result.internal_links += 1
            else:
                result.unresolved_links += 1

        return f"[{label}]({_escape_destination(target)})"


# --------------------------------------------------------------------------------------
# Yardimcilar
# --------------------------------------------------------------------------------------

_WS_RE = re.compile(r"[ \t\r\f\v   ]+")
_BLANKS_RE = re.compile(r"\n{3,}")


def _collapse(text: str) -> str:
    """Bosluklari sadelestirir; anlamli satir sonlarini korur."""
    text = _WS_RE.sub(" ", text)
    text = re.sub(r" *\n *", "\n", text)
    return text.strip()


def _join_blocks(blocks: Iterable[str]) -> str:
    cleaned = [b.strip("\n") for b in blocks if b and b.strip()]
    return _BLANKS_RE.sub("\n\n", "\n\n".join(cleaned)).strip()


def _prefix_lines(text: str, prefix: str) -> str:
    return "\n".join(prefix + line if line else prefix.rstrip() for line in text.split("\n"))


def _wrap(inner: str, marker: str) -> str:
    """Bicimlendirmeyi ic bosluklari disarida birakarak uygular (``** x **`` bozuktur)."""
    stripped = inner.strip()
    if not stripped:
        return inner if inner.strip("\n") else ""
    leading = inner[: len(inner) - len(inner.lstrip())]
    trailing = inner[len(inner.rstrip()):]
    return f"{leading}{marker}{stripped}{marker}{trailing}"


def _int_attr(tag: Tag, name: str) -> int:
    try:
        return int(str(tag.get(name, "1")).strip() or 1)
    except (TypeError, ValueError):
        return 1


def _escape_destination(url: str) -> str:
    """Markdown baglanti hedefindeki bosluk ve parantezleri guvenli hale getirir."""
    if not url:
        return url
    if any(ch in url for ch in " ()<>"):
        return "<" + url.replace("<", "%3C").replace(">", "%3E") + ">"
    return url


def _extract_url(markdown_image: str) -> str | None:
    match = re.search(r"\]\(([^)]+)\)", markdown_image or "")
    return match.group(1) if match else None


def _pick_parser() -> str:
    """En hizli kullanilabilir ayristiriciyi secer."""
    try:
        import lxml  # noqa: F401
    except ImportError:
        log.debug("lxml bulunamadi, dahili html.parser kullanilacak (daha yavas).")
        return "html.parser"
    return "lxml"
