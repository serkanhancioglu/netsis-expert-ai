"""Baslik capraz dogrulamasi: Turkce noktali/noktasiz I tuzagi.

Tek bir HTTP oturumu yuzlerce dokumana hizmet ettigi icin sunucu tarafinda bir
karisiklik A dokumaninin govdesini B'nin dosyasina sessizce yazabilir. Indirilen
belgenin <h1> basligi agactaki adla karsilastirilarak bu yakalanir.

Kontrol fazla hassas olursa ise yaramaz: 2.328 dokumanluk gercek bir calismada
"e-Fatura icin ..." ile "e-Fatura Icin ..." farkli sanildi. Sebep Python'un
casefold()'unun "I" harfini "i" + birlesen nokta olarak cozmesiydi.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from netsis_scraper.cli import _normalise  # noqa: E402


def esit(a: str, b: str) -> bool:
    return _normalise(a) == _normalise(b)


def test_turkish_dotted_i_is_not_a_mismatch():
    """Gercek calismada yasanan yanlis alarm."""
    assert esit(
        "e-Fatura için İlaç-Tıbbi Cihaz Senaryosu Desteği",
        "e-Fatura İçin İlaç-Tıbbi Cihaz Senaryosu Desteği",
    )


def test_all_four_turkish_i_forms_are_equivalent():
    for a, b in [("İ", "i"), ("I", "ı"), ("İ", "ı"), ("i", "I")]:
        assert esit(a, b), f"{a!r} ile {b!r} esit sayilmali"


def test_case_and_whitespace_are_ignored():
    assert esit("Fatura  İşlemleri", "fatura işlemleri")
    assert esit("  Kayıt\n", "KAYIT")


def test_genuinely_different_titles_still_mismatch():
    """Kontrolun asil isi bu: gercek bir icerik karismasini yakalamak.

    Gercek calismada bulundu - agacta '14.09.2026 ... Sematron Degisiklikleri'
    yazan dugum, govdesinde bambaska bir belge dondurdu.
    """
    assert not esit(
        "14.09.2026 Tarihinde Uygulanacak Şematron Değişiklikleri",
        "Giriş/Çıkış Hareketlerini İlişkilendir İşlemi",
    )
    assert not esit("Stok Kartı", "Cari Kartı")


def test_unicode_forms_are_normalised():
    """Ayni harfin farkli kod dizileri esit sayilmali (NFC/NFD)."""
    assert esit("Ölçek", "Ölçek")
