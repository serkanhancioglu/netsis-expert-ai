"""Bilgi tabani indeksi, depodaki JSON semasina uyuyor mu?"""

import csv
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from netsis_scraper import catalog  # noqa: E402
from netsis_scraper.manifest import FIELDS, build_rows, write_manifest  # noqa: E402

SCHEMA_PATH = (
    Path(__file__).resolve().parents[2]
    / "knowledge-base" / "metadata" / "articles-manifest.schema.json"
)


def _node(name, breadcrumb, relative, version="2021-08-23T09:00:11.553+03:00"):
    node = catalog.DocNode(
        page_id="1", name=name,
        doc_url="external?cid=a&link=b&tenantId=c&hideName=True",
        breadcrumb=tuple(breadcrumb), depth=len(breadcrumb) - 1, order=0,
        is_branch=False, slug_name="x.html", version=version,
    )
    node.relative_path = Path(relative)
    return node


def _sample_nodes():
    return [
        _node("Döviz İsimleri Tanımlama",
              ["Kök", "Kullanıcı Dokümanları", "Genel", "Döviz Takibi", "Döviz İsimleri Tanımlama"],
              "Kullanıcı Dokümanları/Genel/Döviz Takibi/Döviz İsimleri Tanımlama.md"),
        _node("Sürüm Notu",
              ["Kök", "Sürüm Dokümanları", "9.0.61 - Ocak 2025"],
              "Sürüm Dokümanları/9.0.61 - Ocak 2025.md", version=""),
    ]


def test_columns_match_the_schema_exactly():
    """Sema `additionalProperties: false` diyor; fazladan sutun kabul edilmez."""
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    assert set(FIELDS) == set(schema["properties"]), "sutunlar sema ile ayni olmali"
    assert set(schema["required"]) <= set(FIELDS)


def test_rows_satisfy_every_schema_constraint():
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    rows = build_rows(_sample_nodes(), product="netsis-3-enterprise", run_date="2026-09-13")
    path_pattern = re.compile(schema["properties"]["relative_path"]["pattern"])

    for row in rows:
        assert set(row) == set(FIELDS)
        for field in schema["required"]:
            assert row[field], f"{field} bos olamaz"
        assert row["version"] == schema["properties"]["version"]["const"]
        assert row["language"] in schema["properties"]["language"]["enum"]
        assert path_pattern.match(row["relative_path"]), row["relative_path"]
        assert re.match(r"^\d{4}-\d{2}-\d{2}$", row["last_updated"]), row["last_updated"]
        assert row["source_url"].startswith("https://")


def test_module_comes_from_the_third_breadcrumb_level():
    rows = build_rows(_sample_nodes(), product="p", run_date="2026-09-13")
    assert rows[0]["module"] == "Genel"
    assert rows[1]["module"] == "9.0.61 - Ocak 2025"


def test_missing_source_version_falls_back_to_run_date():
    rows = build_rows(_sample_nodes(), product="p", run_date="2026-09-13")
    assert rows[0]["last_updated"] == "2021-08-23", "kaynak surum damgasi kullanilmali"
    assert rows[1]["last_updated"] == "2026-09-13", "damga yoksa calisma tarihi"


def test_article_ids_are_stable_and_unique():
    a = build_rows(_sample_nodes(), product="p", run_date="2026-09-13")
    b = build_rows(_sample_nodes(), product="p", run_date="2026-09-13")
    assert [r["article_id"] for r in a] == [r["article_id"] for r in b]
    assert len({r["article_id"] for r in a}) == len(a)


def test_written_csv_round_trips(tmp_path):
    target = tmp_path / "articles-manifest.csv"
    count = write_manifest(target, build_rows(_sample_nodes(), product="p"))
    assert count == 2
    with open(target, encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 2
    assert list(rows[0]) == list(FIELDS)
    assert rows[0]["relative_path"].startswith("markdown/")


def test_extended_fields_are_populated():
    rows = build_rows(
        _sample_nodes(), product="p", run_date="2026-09-13",
        hashes={"external?cid=a&link=b&tenantId=c&hideName=True": "f" * 64},
    )
    row = rows[0]
    assert row["breadcrumb"].startswith("Kullanıcı Dokümanları / Genel /")
    assert row["depth"].isdigit()
    assert row["is_section"] in ("true", "false")
    assert row["doc_cid"] == "a", "page_id 112 dugumde bos; kimlik cid'den gelmeli"
    assert row["content_sha256"] == "f" * 64


def test_content_hash_is_empty_when_unknown():
    rows = build_rows(_sample_nodes(), product="p", run_date="2026-09-13")
    assert rows[0]["content_sha256"] == ""
