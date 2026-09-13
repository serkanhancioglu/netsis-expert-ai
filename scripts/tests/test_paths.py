"""Dosya yolu temizleme ve cakisma cozme testleri."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from netsis_scraper.paths import (  # noqa: E402
    MAX_SEGMENT_LENGTH,
    SegmentAllocator,
    sanitize_segment,
    shorten_relative_path,
)


def test_illegal_characters_become_readable():
    assert sanitize_segment("Raporlar/MRP") == "Raporlar-MRP"
    assert sanitize_segment("Rapor: Ozet") == "Rapor - Ozet"
    assert sanitize_segment('a"b|c?d*e') == "a'b-cd+e"


def test_turkish_characters_are_preserved():
    assert sanitize_segment("Iş Emri Kullanım Raporu") == "Iş Emri Kullanım Raporu"
    assert sanitize_segment("Döviz İsimleri Tanımlama") == "Döviz İsimleri Tanımlama"


def test_windows_reserved_names_are_prefixed():
    assert sanitize_segment("CON") == "_CON"
    assert sanitize_segment("com1.txt") == "_com1.txt"
    assert sanitize_segment("Con") == "_Con"


def test_trailing_dots_and_spaces_are_trimmed():
    assert sanitize_segment("  bosluk. ") == "bosluk"
    assert sanitize_segment("9.0.43.1 - Ekim 2022") == "9.0.43.1 - Ekim 2022"


def test_empty_name_gets_placeholder():
    assert sanitize_segment("") == "adsiz"
    assert sanitize_segment("   ") == "adsiz"
    assert sanitize_segment("///") == "adsiz"


def test_long_names_are_shortened_but_stay_unique():
    a = sanitize_segment("x" * 200)
    b = sanitize_segment("x" * 201)
    assert len(a) <= MAX_SEGMENT_LENGTH
    assert a != b, "kesilen iki farkli ad ayni olmamali"


def test_sibling_collisions_are_numbered_case_insensitively():
    allocator = SegmentAllocator()
    assert allocator.allocate(("r",), "Fatura") == "Fatura"
    assert allocator.allocate(("r",), "Fatura") == "Fatura (2)"
    # Windows/macOS buyuk-kucuk harf duyarsizdir: FATURA da cakisir.
    assert allocator.allocate(("r",), "FATURA") == "FATURA (3)"
    # Farkli ust klasorde cakisma yok.
    assert allocator.allocate(("s",), "Fatura") == "Fatura"


def test_path_budget_is_respected():
    parts = ["a" * 90, "b" * 90, "c" * 90]
    result = shorten_relative_path(parts, 120)
    total = sum(len(p) for p in result) + len(result) - 1
    assert total <= 120
    assert len(result) == 3
    assert len(set(result)) == 3, "kisaltma sonrasi parcalar hala ayirt edilebilmeli"


def test_short_paths_are_left_alone():
    parts = ["Genel", "Rapor", "Ozet.md"]
    assert shorten_relative_path(parts, 240) == parts


def _real_path() -> list[str]:
    """Agactaki en uzun gercek yol (7 seviye + dosya adi)."""
    return [
        "Kullanıcı Dokümanları",
        "Muhasebe",
        "Muhasebe Modülü",
        "Ekler - Muhasebe",
        "Ek-1 Enflasyon Muhasebesi",
        "Muhasebe Modülü Enflasyon Düzeltme İşlemleri",
        "Enflasyon Düzeltmeleri - Parasal Kar-Zarar Virmanı.md",
    ]


def test_a_path_with_an_extension_is_actually_shortened():
    """Regresyon: uzanti farkindaligi eklenirken kisaltma tamamen devre disi kalmisti.

    Noktasiz parcalardan olusan test bunu yakalayamiyordu, cunku hata yalnizca
    parcalardan biri nokta icerdiginde tetikleniyordu.
    """
    parts = _real_path()
    original = sum(len(p) for p in parts) + len(parts) - 1
    assert original > 120, "test verisi butceyi asmali, yoksa hicbir sey olculmez"
    result = shorten_relative_path(parts, 120)
    total = sum(len(p) for p in result) + len(result) - 1
    assert total <= 120, f"kisaltma calismadi: {total} > 120"


def test_md_extension_survives_truncation():
    """Kesilen dosya adi .md ile bitmezse `**/*.md` taramalari onu hic gormez."""
    for budget in (180, 150, 120, 90):
        result = shorten_relative_path(_real_path(), budget)
        assert result[-1].endswith(".md"), f"butce={budget}: {result[-1]!r}"


def test_shortening_is_deterministic_and_independent_of_anything_else():
    parts = _real_path()
    assert shorten_relative_path(parts, 120) == shorten_relative_path(list(parts), 120)


def test_different_long_names_stay_distinct_after_truncation():
    a = shorten_relative_path(["ust", "A" * 100 + "bir.md"], 60)
    b = shorten_relative_path(["ust", "A" * 100 + "iki.md"], 60)
    assert a != b, "kesilen iki farkli ad ayni dosyaya dusmemeli"
