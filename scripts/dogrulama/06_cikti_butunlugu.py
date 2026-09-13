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

LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\((?!https?:|mailto:|#)([^)]+)\)")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\((?!https?:|data:)([^)]+)\)")


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

    images = broken_images = links = pending = broken = 0
    examples: list[str] = []

    for md in root.rglob("*.md"):
        body = md.read_text(encoding="utf-8", errors="replace")
        for match in IMAGE_RE.finditer(body):
            images += 1
            if not (md.parent / match.group(1).strip("<>")).resolve().exists():
                broken_images += 1
                if len(examples) < 8:
                    examples.append(f"GORSEL {md.relative_to(root)} -> {match.group(1)}")
        for match in LINK_RE.finditer(body):
            links += 1
            target = (md.parent / match.group(1).strip("<>")).resolve()
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
                    examples.append(f"BAGLANTI {md.relative_to(root)} -> {match.group(1)}")

    print(f"gorsel referansi : {images}, kirik: {broken_images}")
    print(f"goreli baglanti  : {links}")
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
