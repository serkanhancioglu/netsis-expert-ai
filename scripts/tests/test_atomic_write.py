"""Atomik yazimin Windows yol sinirini asmamasi.

Gercek bir Windows calismasinda iki dokuman su hatayla dustu:

    FileNotFoundError: ...\\.Enflasyon Muhasebesine Baslama (...).md.10348.39920.tmp

Hedef dosya 247 karakterdi (260 sinirinin altinda, yazilabilir) ama gecici ad
".<hedef>.<pid>.<tid>.tmp" kalibiyla 264'e cikiyordu. Yol butcesi yalnizca son
dosya adini olcuyordu, gecici adi degil.
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from netsis_scraper.cli import _temp_path, write_atomic  # noqa: E402

UZUN_AD = "Enflasyon Muhasebesine Başlama (Enflasyon Muhasebesi Vergi Usul Kanunu).md"


def test_temp_name_is_never_longer_than_the_target():
    """Asil kural bu: gecici ad hedeften uzun olursa yol siniri asilabilir."""
    for ad in (UZUN_AD, "kısa.md", "a" * 120 + ".md", "index.md"):
        hedef = Path("/tmp/x") / ad
        assert len(_temp_path(hedef).name) <= len(hedef.name), ad


def test_normal_names_get_the_thirteen_character_form():
    temp = _temp_path(Path("/tmp/x") / UZUN_AD)
    assert re.fullmatch(r"\.[0-9a-f]{8}\.tmp", temp.name), temp.name


def test_very_short_targets_drop_the_tmp_suffix_to_stay_short():
    """4 karakterlik bir hedefte 13 karakterlik gecici ad yine sinir riski olurdu."""
    temp = _temp_path(Path("/tmp/x") / "a.md")
    assert len(temp.name) <= len("a.md")
    assert re.fullmatch(r"\.[0-9a-f]+", temp.name), temp.name


def test_temp_file_sits_next_to_the_target():
    """Baska bir diske dusmemeli; os.replace yalnizca ayni birimde atomiktir."""
    hedef = Path("/tmp/derin/klasor") / UZUN_AD
    assert _temp_path(hedef).parent == hedef.parent


def test_concurrent_writers_get_distinct_temp_names():
    hedef = Path("/tmp/x") / UZUN_AD
    assert len({_temp_path(hedef).name for _ in range(200)}) == 200


def test_write_creates_the_file_and_leaves_no_temp(tmp_path):
    hedef = tmp_path / UZUN_AD
    write_atomic(hedef, "içerik")
    assert hedef.read_text(encoding="utf-8") == "içerik"
    assert not list(tmp_path.glob(".*.tmp")), "gecici dosya temizlenmedi"


def test_write_replaces_existing_content(tmp_path):
    hedef = tmp_path / "a.md"
    write_atomic(hedef, "eski")
    write_atomic(hedef, "yeni")
    assert hedef.read_text(encoding="utf-8") == "yeni"


def test_parent_directories_are_created(tmp_path):
    hedef = tmp_path / "bir" / "iki" / "üç" / UZUN_AD
    write_atomic(hedef, "x")
    assert hedef.is_file()


def test_deep_real_path_stays_under_windows_limit(tmp_path):
    """Agactaki en derin gercek yol + gecici ad, 260 sinirini asmamali."""
    taban = r"C:\Users\Serkan\Documents\netsis-expert-ai\knowledge-base\markdown"
    goreli = (
        r"Kullanıcı Dokümanları\Muhasebe\Muhasebe Modülü\Ekler - Muhasebe"
        r"\Ek-1 Enflasyon Muhasebesi\Demirbaş Modülü" + "\\" + UZUN_AD
    )
    hedef_uzunluk = len(taban) + 1 + len(goreli)
    gecici_uzunluk = hedef_uzunluk - len(UZUN_AD) + len(_temp_path(Path(UZUN_AD)).name)
    assert hedef_uzunluk < 260, "test verisi zaten siniri asiyor"
    assert gecici_uzunluk < 260, f"gecici yol {gecici_uzunluk} karakter, sinir 260"
