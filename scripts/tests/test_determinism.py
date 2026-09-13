"""Ayni girdi her zaman ayni ciktiyi vermeli.

Cikti agaci depoya girip `git diff` ile izlenecegi icin belirlenimlilik bir
kolaylik degil, gereklilik: gurultulu bir diff, gercek degisiklikleri gizler.
"""

import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pytest  # noqa: E402

from netsis_scraper import catalog, config  # noqa: E402
from netsis_scraper.assets import AssetStore  # noqa: E402
from netsis_scraper.convert import MarkdownConverter  # noqa: E402
from netsis_scraper.manifest import build_rows  # noqa: E402

FIXTURES = Path(__file__).resolve().parent / "fixtures"
TREE = FIXTURES / "tree.json"


def _nodes():
    if not TREE.exists():
        pytest.skip(f"agac orneklemi yok: {TREE}")
    root = json.loads(TREE.read_text(encoding="utf-8"))
    nodes = catalog.flatten(root)
    catalog.plan_paths(nodes)
    return nodes


def test_path_planning_is_independent_of_output_location():
    """Bütçeye çıktı klasörünün uzunluğu katılsaydı, aynı ağaç iki makinede
    farklı dosya adları üretirdi."""
    first = {n.doc_url: str(n.relative_path) for n in _nodes()}
    second = {n.doc_url: str(n.relative_path) for n in _nodes()}
    assert first == second


def test_every_planned_path_is_unique_case_insensitively():
    paths = [str(n.relative_path) for n in _nodes()]
    assert len(paths) == len({p.casefold() for p in paths}), (
        "Windows ve macOS buyuk-kucuk harf duyarsizdir; cakisma veri kaybidir"
    )


def test_every_planned_path_keeps_the_md_extension():
    assert all(str(n.relative_path).endswith(".md") for n in _nodes())


def test_planned_paths_fit_the_budget():
    for node in _nodes():
        assert len(str(node.relative_path)) <= config.MAX_RELATIVE_PATH


def test_manifest_rows_are_stable_across_calls():
    nodes = _nodes()
    a = build_rows(nodes, product="netsis-3-enterprise", run_date="2026-09-13")
    b = build_rows(nodes, product="netsis-3-enterprise", run_date="2026-09-13")
    assert a == b


def test_conversion_is_order_independent():
    """Belgeleri ileri ya da geri sirayla cevirmek ayni ciktiyi vermeli.

    Gorsel deposu paylasilan bir durumdur; sirayla degisen bir cikti, gorsel
    adlandirmasinin isleme sirasina bagli oldugu anlamina gelirdi.
    """
    samples = sorted(FIXTURES.glob("*.html"))
    if not samples:
        pytest.skip(f"HTML orneklemi yok: {FIXTURES}")

    def convert_all(order):
        directory = Path(tempfile.mkdtemp())
        converter = MarkdownConverter(
            asset_store=AssetStore(directory / "_assets"), assets_href_prefix="_assets/"
        )
        return {
            f.name: converter.convert(f.read_text(encoding="utf-8", errors="replace")).markdown
            for f in order
        }

    forward = convert_all(samples)
    backward = convert_all(list(reversed(samples)))
    assert forward == backward
