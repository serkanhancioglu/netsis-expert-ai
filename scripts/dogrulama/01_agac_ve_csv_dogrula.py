#!/usr/bin/env python3
"""Hiyerarsi agacini indirir, CSV ile karsilastirir ve cikti yollarini denetler.

Ne dogrular:
  * Agac API'si kac dugum donuyor, kaci yaprak kaci bolum
  * CSV'deki her baglanti agacta var mi (kapsama)
  * Planlanan cikti yollari benzersiz mi - buyuk/kucuk harf duyarsiz dahil
  * .md uzantisi her yolda duruyor mu
  * En uzun yol Windows 260 sinirinin neresinde

Kullanim:
    python 01_agac_ve_csv_dogrula.py [CSV_DOSYASI]
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
try:
    from netsis_scraper import catalog, config
except ImportError:
    sys.exit("netsis_scraper bulunamadi. Bu betigi kazima araciyla ayni sanal ortamda calistirin.")

import requests


def main(csv_path: str | None = None) -> int:
    session = requests.Session()
    session.headers["User-Agent"] = config.USER_AGENT
    root = catalog.fetch_catalog(session, config.DEFAULT_PRODUCT)
    nodes = catalog.flatten(root)

    branches = sum(1 for n in nodes if n.is_branch)
    print(f"agac dugumu   : {len(nodes)}")
    print(f"  bolum       : {branches}")
    print(f"  yaprak      : {len(nodes) - branches}")

    if csv_path:
        rows = catalog.read_link_csv(Path(csv_path))
        wanted = catalog.csv_doc_urls(rows)
        summary = catalog.annotate_csv_membership(nodes, wanted)
        print(f"\nCSV satiri    : {len(rows)}")
        print(f"  cozulen adres: {summary['csv_rows']}")
        print(f"  agacta bulunan: {summary['matched']}")
        print(f"  CSV'de olup agacta olmayan: {summary['csv_only']}")
        print(f"  agacta olup CSV'de olmayan: {summary['tree_only']}")

    catalog.plan_paths(nodes)
    paths = [str(n.relative_path) for n in nodes]
    longest = max(paths, key=len)
    print(f"\ncikti yolu    : {len(paths)}")
    print(f"  benzersiz   : {len(set(paths))}")
    print(f"  benzersiz (buyuk/kucuk harf duyarsiz): {len({p.casefold() for p in paths})}")
    print(f"  .md ile bitmeyen: {sum(1 for p in paths if not p.endswith('.md'))}")
    print(f"  en uzun     : {len(longest)} karakter")
    print(f"    {longest}")
    for base in (r"C:\netsis", r"C:\Users\kullanici\Documents\netsis-docs"):
        worst = len(base) + 1 + len(longest)
        print(f"  {base:42s} -> en kotu mutlak yol {worst} (sinir 260)")

    problems = (
        len(set(paths)) != len(paths)
        or len({p.casefold() for p in paths}) != len(paths)
        or any(not p.endswith(".md") for p in paths)
    )
    print("\nSONUC:", "SORUN VAR" if problems else "temiz")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1] if len(sys.argv) > 1 else None))
