#!/usr/bin/env python3
"""Uretilen articles-manifest.csv dosyasini JSON semasina karsi dogrular.

Semayi tam bir JSON Schema kutuphanesi olmadan, ihtiyac duyulan kisitlar
uzerinden kontrol eder: zorunlu alanlar, sabit degerler, enum'lar, duzenli
ifade kaliplari ve `additionalProperties: false`.

Kullanim:
    python 07_indeks_sema_dogrula.py CSV_DOSYASI [SEMA_DOSYASI]
"""
import csv
import json
import re
import sys
from pathlib import Path


def main(csv_path: str, schema_path: str | None = None) -> int:
    csv_file = Path(csv_path)
    schema_file = Path(schema_path) if schema_path else csv_file.parent / "articles-manifest.schema.json"
    if not schema_file.exists():
        sys.exit(f"sema bulunamadi: {schema_file}")

    schema = json.loads(schema_file.read_text(encoding="utf-8"))
    properties = schema["properties"]
    with open(csv_file, encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    patterns = {
        name: re.compile(spec["pattern"])
        for name, spec in properties.items() if "pattern" in spec
    }
    violations: list[tuple[int, str]] = []
    for index, row in enumerate(rows, start=2):        # 1 = baslik satiri
        if set(row) != set(properties):
            violations.append((index, f"sutunlar uyusmuyor: {sorted(set(row) ^ set(properties))}"))
            continue
        for field in schema["required"]:
            if not row[field]:
                violations.append((index, f"{field} bos"))
        for field, spec in properties.items():
            value = row[field]
            if "const" in spec and value != spec["const"]:
                violations.append((index, f"{field}={value!r}, {spec['const']!r} olmali"))
            if "enum" in spec and value not in spec["enum"]:
                violations.append((index, f"{field}={value!r} enum disinda"))
            if field in patterns and not patterns[field].match(value):
                violations.append((index, f"{field}={value[:40]!r} kalibi tutmuyor"))

    print(f"satir: {len(rows)}   sutun: {len(properties)}   SEMA IHLALI: {len(violations)}")
    for line, message in violations[:20]:
        print(f"  satir {line}: {message}")
    if rows:
        print(f"\nbenzersiz article_id : {len({r['article_id'] for r in rows})}")
        print(f"benzersiz relative_path: {len({r['relative_path'] for r in rows})}")
        if "doc_cid" in properties:
            print(f"benzersiz doc_cid    : {len({r['doc_cid'] for r in rows})}")
        if "content_sha256" in properties:
            print(f"ozeti dolu (indirilmis): {sum(1 for r in rows if r['content_sha256'])}")
    return 1 if violations else 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    raise SystemExit(main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None))
