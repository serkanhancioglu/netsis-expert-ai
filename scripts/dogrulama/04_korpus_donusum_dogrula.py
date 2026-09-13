#!/usr/bin/env python3
"""Bir HTML orneklemini toptan cevirir ve ciktiyi bozukluklara karsi tarar.

Olctugu seyler:
  * gorsel, tablo (Markdown / HTML), bilgi kutusu, gomulu video sayilari
  * korunan <tab> sayisi, baslik seviyeleri
  * BOZUKLUK: cift vurgulu baslik (## **x**), gecersiz vurgu (*"*),
    Markdown'a sizmis ham HTML etiketi, Markdown icinde kalmis data: adresi,
    Markdown'a sizmis <script> icerigi

Kullanim:
    python 04_korpus_donusum_dogrula.py ORNEKLEM_KLASORU
"""
import collections
import re
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from netsis_scraper.assets import AssetStore  # noqa: E402
from netsis_scraper.convert import MarkdownConverter  # noqa: E402

SEMANTIC = {"u", "br", "table", "thead", "tbody", "tr", "th", "td", "sub", "sup"}


def main(sample_dir: str) -> int:
    files = sorted(Path(sample_dir).rglob("*.html"))
    if not files:
        sys.exit(f"{sample_dir} icinde .html yok")

    store = AssetStore(Path(tempfile.mkdtemp()) / "_assets")
    converter = MarkdownConverter(asset_store=store, assets_href_prefix="_assets/")

    counts = collections.Counter()
    headings = collections.Counter()
    problems = collections.Counter()
    markdown_bytes = 0

    for path in files:
        result = converter.convert(path.read_text(encoding="utf-8", errors="replace"))
        md = result.markdown
        markdown_bytes += len(md.encode("utf-8"))
        counts["gorsel"] += result.images
        counts["tablo_md"] += result.tables_gfm
        counts["tablo_html"] += result.tables_html
        counts["gomulu"] += result.embeds
        counts["duzen_blogu"] += result.layout_blocks
        counts["bilgi_kutusu"] += md.count("> [!")
        counts["korunan_tab"] += md.count(r"\<tab\>")
        for level in range(1, 7):
            headings[f"h{level}"] += len(re.findall(rf"^{'#' * level} ", md, re.M))

        problems["cift_vurgulu_baslik"] += len(re.findall(r"^#{1,6} \*\*", md, re.M))
        problems["gecersiz_vurgu"] += len(re.findall(r'(?<!\*)\*"\*(?!\*)', md))
        problems["kalan_data_uri"] += md.count("](data:")
        problems["sizan_script"] += len(re.findall(r"AJS\.|PocketQuery|function\s*\(", md))
        for m in re.finditer(r"(\\?)<(/?)([a-zA-Z][a-zA-Z0-9]*)[ >]", md):
            if m.group(1) != "\\" and m.group(3).lower() not in SEMANTIC:
                problems["sizan_ham_etiket"] += 1

    print(f"dosya: {len(files)}   uretilen Markdown: {markdown_bytes / 1e6:.2f} MB")
    print("\nICERIK");  [print(f"  {k:16s}{v}") for k, v in sorted(counts.items())]
    print("\nBASLIKLAR"); [print(f"  {k:16s}{v}") for k, v in sorted(headings.items()) if v]
    print("\nBOZUKLUK TARAMASI")
    for k, v in sorted(problems.items()):
        print(f"  {k:22s}{v}   {'<-- INCELE' if v else ''}")
    return 1 if any(problems.values()) else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1] if len(sys.argv) > 1 else sys.exit(__doc__)))
