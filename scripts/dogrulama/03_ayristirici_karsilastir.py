#!/usr/bin/env python3
"""Uc HTML ayristiricisinin `<tab>` sahte etiketini nasil ele aldigini olcer.

Bulgu: html.parser, lxml ve html5lib UCU DE metindeki "<tab>" ifadesini sessizce
siler. Orneklemde 64 dosyanin 25'inde toplam 112 kez geciyor. Kazima araci bu
yuzden ayristirmadan ONCE bilinmeyen etiketleri metne kacisliyor.

Kullanim:
    python 03_ayristirici_karsilastir.py ORNEKLEM_KLASORU
"""
import sys
from pathlib import Path

from bs4 import BeautifulSoup

FRAGMENT = '<p>se&ccedil;ilerek <tab> tu&#351;u ile ilerlendiginde "100" girilir.</tab> devam</p>'


def main(sample_dir: str | None = None) -> int:
    print("=== Kucuk parca uzerinde ===")
    for parser in ("html.parser", "lxml", "html5lib"):
        try:
            text = BeautifulSoup(FRAGMENT, parser).get_text()
        except Exception as exc:
            print(f"  {parser:11s} KULLANILAMIYOR: {exc}")
            continue
        print(f"  {parser:11s} '<tab>' korundu mu: {'<tab>' in text}")
        print(f"              -> {text!r}")

    print("\n=== On kacislama uygulandiginda ===")
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    try:
        from netsis_scraper.convert import protect_pseudo_tags
    except ImportError:
        print("  netsis_scraper bulunamadi, bu bolum atlandi.")
        return 0
    for parser in ("html.parser", "lxml", "html5lib"):
        try:
            text = BeautifulSoup(protect_pseudo_tags(FRAGMENT), parser).get_text()
        except Exception:
            continue
        print(f"  {parser:11s} '<tab>' korundu mu: {'<tab>' in text}")

    if not sample_dir:
        return 0
    print(f"\n=== Gercek dosyalar ({sample_dir}) ===")
    files = sorted(Path(sample_dir).rglob("*.html"))
    with_tab = [f for f in files if "<tab>" in f.read_text(encoding="utf-8", errors="replace")]
    print(f"  toplam dosya: {len(files)}, '<tab>' iceren: {len(with_tab)}")
    total = sum(
        f.read_text(encoding="utf-8", errors="replace").count("<tab>") for f in with_tab
    )
    print(f"  toplam '<tab>' gecisi: {total}")
    lost = kept = 0
    for f in with_tab:
        raw = f.read_text(encoding="utf-8", errors="replace")
        lost += 0 if "<tab>" in BeautifulSoup(raw, "lxml").get_text() else 1
        kept += 1 if "<tab>" in BeautifulSoup(protect_pseudo_tags(raw), "lxml").get_text() else 0
    print(f"  on kacislama YOKKEN metni kaybeden dosya : {lost}/{len(with_tab)}")
    print(f"  on kacislama VARKEN metni koruyan dosya  : {kept}/{len(with_tab)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1] if len(sys.argv) > 1 else None))
