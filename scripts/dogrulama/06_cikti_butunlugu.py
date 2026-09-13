#!/usr/bin/env python3
"""Uretilmis Markdown agacinda kirik gorsel ve baglanti arar.

Kismi bir calismada, henuz indirilmemis dokumanlara giden baglantilar dogal
olarak kirik gorunur. Betik bunlari "planlanmis ama henuz yok" diye ayirir;
gercekten hatali olanlari ayrica sayar.

Kullanim:
    python 06_cikti_butunlugu.py CIKTI_KLASORU
"""
import re
import sqlite3
import sys
from pathlib import Path

#: CommonMark'da hedef iki bicimde yazilabilir:
#:   [x](yol.md)              - bosluk ve parantez ICEREMEZ
#:   [x](<yol (parantezli).md>) - <> icinde her sey olabilir
#: Naif bir `\(([^)]+)\)` kalibi ikinci bicimi ilk parantezde keser ve saglam
#: baglantilari kirik sanir. Kaynakta "Ekler (Stok)" gibi klasorler var.
_HEDEF = r"\(\s*(?:<([^<>]*)>|([^()\s]*))"
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]" + _HEDEF)
IMAGE_RE = re.compile(r"!\[[^\]]*\]" + _HEDEF)


def _hedef_metni(match: re.Match) -> str:
    """Eslesmeden hedefi cikarir (hangi bicim kullanildiysa)."""
    return match.group(1) if match.group(1) is not None else (match.group(2) or "")

#: Herhangi bir sema (http, https, ftp, mailto, data ...) mutlak adres demektir.
#: Semayi ARANMADAN once <> sarmalayicisini soymak sart: Markdown, icinde bosluk
#: olan adresleri <...> icine alir ve "(" hemen sonrasina bakan bir kontrol
#: bunlari goreli yol saniyor.
SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")


def _siniflandir(destination: str) -> tuple[str, str]:
    """Baglanti hedefini turune gore ayirir.

    Donen tur: 'yerel' (agac icinde cozulmeli), 'mutlak' (dis adres, bizi
    ilgilendirmez) ya da 'kok-goreli'. Sonuncusu kaynakta kalmis Confluence
    artigidir ('/display/...'): bir dosya agacinda hicbir zaman cozulemez,
    ama bizim uretmedigimiz bir kaynak hatasidir.
    """
    target = destination.strip().strip("<>").strip()
    if not target or target.startswith("#"):
        return "mutlak", target
    if SCHEME_RE.match(target):
        return "mutlak", target
    if target.startswith("/"):
        return "kok-goreli", target
    return "yerel", target.split("#", 1)[0]


def planned_paths(root: Path) -> set[str]:
    db = root / ".netsis-scraper-state.sqlite3"
    if not db.exists():
        return set()
    connection = sqlite3.connect(db)
    try:
        return {row[0] for row in connection.execute("SELECT relative_path FROM documents")}
    finally:
        connection.close()


def main(output_dir: str) -> int:
    root = Path(output_dir).resolve()
    if not root.is_dir():
        sys.exit(f"{root} bir klasor degil")
    planned = planned_paths(root)

    images = broken_images = links = pending = broken = kok_goreli = 0
    examples: list[str] = []

    for md in root.rglob("*.md"):
        body = md.read_text(encoding="utf-8", errors="replace")
        for match in IMAGE_RE.finditer(body):
            tur, hedef = _siniflandir(_hedef_metni(match))
            if tur != "yerel":
                continue
            images += 1
            if not (md.parent / hedef).resolve().exists():
                broken_images += 1
                if len(examples) < 8:
                    examples.append(f"GORSEL {md.relative_to(root)} -> {_hedef_metni(match)}")
        for match in LINK_RE.finditer(body):
            tur, hedef = _siniflandir(_hedef_metni(match))
            if tur == "mutlak":
                continue
            if tur == "kok-goreli":
                kok_goreli += 1
                continue
            links += 1
            target = (md.parent / hedef).resolve()
            if target.exists():
                continue
            try:
                relative = str(target.relative_to(root))
            except ValueError:
                relative = ""
            if relative in planned:
                pending += 1
            else:
                broken += 1
                if len(examples) < 8:
                    examples.append(f"BAGLANTI {md.relative_to(root)} -> {_hedef_metni(match)}")

    print(f"gorsel referansi : {images}, kirik: {broken_images}")
    print(f"goreli baglanti  : {links}")
    print(f"kok-goreli (kaynakta olu Confluence artigi): {kok_goreli}")
    print(f"  planlanmis ama henuz indirilmemis: {pending}")
    print(f"  GERCEKTEN HATALI                 : {broken}")
    for e in examples:
        print("   ", e)
    print("\nSONUC:", "SORUN VAR" if (broken_images or broken) else "temiz")
    return 1 if (broken_images or broken) else 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    raise SystemExit(main(sys.argv[1]))
