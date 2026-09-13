#!/usr/bin/env python3
"""Orneklemden tam calismanin boyutunu tahmin eder.

Tahminleri elle yazmak yerine olcup olceklemek icin. Gorsel rakami bir UST
SINIRDIR: ayni ikonlar dokumanlar arasinda paylasildigi icin gercek toplam
dogrusal tahminin altinda kalir.

Kullanim:
    python 05_boyut_tahmini.py ORNEKLEM_KLASORU [TOPLAM_DOKUMAN]
"""
import statistics
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from netsis_scraper.assets import AssetStore  # noqa: E402
from netsis_scraper.convert import MarkdownConverter  # noqa: E402


def main(sample_dir: str, total: int = 2328) -> int:
    files = sorted(Path(sample_dir).rglob("*.html"))
    if not files:
        sys.exit(f"{sample_dir} icinde .html yok")

    assets_dir = Path(tempfile.mkdtemp()) / "_assets"
    converter = MarkdownConverter(asset_store=AssetStore(assets_dir), assets_href_prefix="_assets/")

    html_bytes = markdown_bytes = 0
    for path in files:
        raw = path.read_text(encoding="utf-8", errors="replace")
        html_bytes += len(raw.encode("utf-8"))
        markdown_bytes += len(converter.convert(raw).markdown.encode("utf-8"))

    asset_files = [p for p in assets_dir.rglob("*") if p.is_file()]
    asset_bytes = sum(p.stat().st_size for p in asset_files)
    n = len(files)
    sizes = [p.stat().st_size for p in files]

    print(f"ORNEKLEM ({n} dokuman)")
    print(f"  ham HTML        : {html_bytes / 1e6:.1f} MB")
    print(f"    en kucuk/orta/en buyuk: {min(sizes)} / {int(statistics.median(sizes))} / {max(sizes)}")
    print(f"  uretilen Markdown: {markdown_bytes / 1e6:.2f} MB  (HTML'in %{100 * markdown_bytes / html_bytes:.0f}'i)")
    print(f"  benzersiz gorsel : {len(asset_files)} dosya, {asset_bytes / 1e6:.1f} MB")

    print(f"\n{total} DOKUMAN ICIN DOGRUSAL TAHMIN")
    print(f"  indirilecek HTML : {html_bytes / n * total / 1e6:.0f} MB")
    print(f"  diskteki Markdown: {markdown_bytes / n * total / 1e6:.0f} MB")
    print(f"  diskteki gorsel  : <= {asset_bytes / n * total / 1e6:.0f} MB, <= {asset_files and len(asset_files) / n * total:.0f} dosya")
    print("  NOT: gorsel rakami ust sinirdir; ikonlar paylasildigi icin gercek")
    print("       toplam bunun altinda kalir.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    raise SystemExit(main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 2328))
