#!/usr/bin/env python3
"""Ayni girdinin her zaman ayni ciktiyi verdigini dogrular.

Iki soruyu ayri ayri sinar:
  A. Yol planlamasi cikti klasorunun yerinden bagimsiz mi
     (bagimli olsaydi ayni agac iki makinede farkli dosya adlari uretirdi)
  B. Donusum isleme sirasindan bagimsiz mi
     (gorsel deposu paylasilan durumdur; sira etkilerse adlandirma kayar)

Kullanim:
    python 09_belirlenimlilik.py AGAC_JSON [ORNEKLEM_KLASORU]
"""
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from netsis_scraper import catalog, config  # noqa: E402
from netsis_scraper.assets import AssetStore  # noqa: E402
from netsis_scraper.convert import MarkdownConverter  # noqa: E402


def plan(root: dict) -> dict[str, str]:
    nodes = catalog.flatten(root)
    catalog.plan_paths(nodes)
    return {n.doc_url: str(n.relative_path) for n in nodes}


def main(tree_json: str, sample_dir: str | None = None) -> int:
    root = json.loads(Path(tree_json).read_text(encoding="utf-8"))
    problems = 0

    print("=== A) Yol planlamasi ===")
    first, second = plan(root), plan(root)
    print(f"  iki cagri ayni mi: {first == second}")
    problems += 0 if first == second else 1

    paths = list(first.values())
    unique = len(set(paths))
    unique_ci = len({p.casefold() for p in paths})
    no_md = sum(1 for p in paths if not p.endswith(".md"))
    over = sum(1 for p in paths if len(p) > config.MAX_RELATIVE_PATH)
    print(f"  yol: {len(paths)}  benzersiz: {unique}  buyuk/kucuk duyarsiz benzersiz: {unique_ci}")
    print(f"  .md ile bitmeyen: {no_md}   butceyi asan: {over}")
    problems += (unique != len(paths)) + (unique_ci != len(paths)) + bool(no_md) + bool(over)

    if sample_dir:
        print("\n=== B) Donusum sirasi ===")
        files = sorted(Path(sample_dir).rglob("*.html"))

        def convert_all(order):
            directory = Path(tempfile.mkdtemp())
            converter = MarkdownConverter(
                asset_store=AssetStore(directory / "_assets"), assets_href_prefix="_assets/"
            )
            output = {
                f.name: converter.convert(f.read_text(encoding="utf-8", errors="replace")).markdown
                for f in order
            }
            names = sorted(p.name for p in (directory / "_assets").rglob("*") if p.is_file())
            return output, names

        forward_md, forward_assets = convert_all(files)
        reverse_md, reverse_assets = convert_all(list(reversed(files)))
        same_md = forward_md == reverse_md
        same_assets = forward_assets == reverse_assets
        print(f"  {len(files)} dosya, ileri vs geri sira")
        print(f"  Markdown ayni mi     : {same_md}")
        print(f"  gorsel adlari ayni mi: {same_assets} ({len(forward_assets)} dosya)")
        problems += (not same_md) + (not same_assets)

    print("\nSONUC:", "SORUN VAR" if problems else "belirlenimli")
    return 1 if problems else 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    raise SystemExit(main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None))
