"""HTML -> Markdown donusum testleri."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from netsis_scraper.assets import sniff_extension  # noqa: E402
from netsis_scraper.catalog import (  # noqa: E402
    decode_detail_segment,
    doc_url_from_link,
    encode_detail_segment,
)
from netsis_scraper.convert import MarkdownConverter, protect_pseudo_tags  # noqa: E402


def convert(markup: str, **kwargs) -> str:
    return MarkdownConverter(image_mode="skip", **kwargs).convert(markup).markdown


# -- sahte etiketler ---------------------------------------------------------------------

def test_pseudo_tag_is_preserved_as_text():
    """`<tab>` gecerli bir HTML etiketi degil; hicbir ayristirici korumaz.

    Ornek kumede 64 dosyanin 25'inde 224 kez geciyordu. Onlem alinmazsa kaybolur.
    """
    markup = "<html><body><p>Once <tab> tusuna basin.</tab></p></body></html>"
    assert "<tab>" in protect_pseudo_tags(markup).replace("&lt;", "<").replace("&gt;", ">")
    out = convert(markup)
    assert r"\<tab\>" in out, out
    assert "tusuna basin" in out


def test_known_tags_are_not_escaped():
    assert protect_pseudo_tags("<p><strong>a</strong></p>") == "<p><strong>a</strong></p>"


# -- baslik ve metin ---------------------------------------------------------------------

def test_heading_and_paragraph():
    out = convert("<html><body><h1>Baslik</h1><p>Metin.</p></body></html>")
    assert out.startswith("# Baslik")
    assert "Metin." in out


def test_entities_are_decoded():
    out = convert("<html><body><p>Sa&#287; Tu&#351; &amp; &ccedil;ift</p></body></html>")
    assert "Sağ Tuş & çift" in out


def test_bold_and_italic():
    out = convert("<html><body><p><strong>kalin</strong> ve <em>egik</em></p></body></html>")
    assert "**kalin**" in out
    assert "*egik*" in out


def test_bold_with_surrounding_spaces_is_valid_markdown():
    """`** kalin **` Markdown'da bicimlenmez; bosluk disariya alinmali."""
    out = convert("<html><body><p><strong> kalin </strong></p></body></html>")
    assert "**kalin**" in out
    assert "** kalin **" not in out


# -- kutular ------------------------------------------------------------------------------

def test_information_macro_becomes_callout():
    markup = (
        "<html><body><div class='polaris-information-macro "
        "polaris-information-macro-information'>"
        "<span class='polaris-information-macro-icon'></span>"
        "<div class='polaris-information-macro-body'>Dikkat edin.</div></div></body></html>"
    )
    out = convert(markup)
    assert "> [!NOTE]" in out
    assert "> Dikkat edin." in out


def test_warning_macro_maps_to_warning():
    markup = (
        "<html><body><div class='polaris-information-macro "
        "polaris-information-macro-warning'>"
        "<div class='polaris-information-macro-body'>Uyari.</div></div></body></html>"
    )
    assert "> [!WARNING]" in convert(markup)


# -- tablolar -------------------------------------------------------------------------------

def test_simple_table_becomes_gfm():
    markup = (
        "<html><body><table><tr><th>A</th><th>B</th></tr>"
        "<tr><td>1</td><td>2</td></tr></table></body></html>"
    )
    out = convert(markup)
    assert "| A | B |" in out
    assert "| --- | --- |" in out
    assert "| 1 | 2 |" in out


def test_colspan_table_falls_back_to_html():
    """GFM tablolari colspan ifade edemez; veriyi bozmaktansa HTML birak."""
    markup = (
        "<html><body><table><tr><td colspan='2'>genis</td></tr>"
        "<tr><td>1</td><td>2</td></tr></table></body></html>"
    )
    out = convert(markup)
    assert "<table>" in out
    assert 'colspan="2"' in out


def test_pipe_in_cell_is_escaped():
    markup = "<html><body><table><tr><td>a|b</td><td>c</td></tr></table></body></html>"
    out = convert(markup)
    assert r"a\|b" in out


# -- baglantilar ------------------------------------------------------------------------------

def test_external_link_is_kept():
    out = convert('<html><body><p><a href="https://x.example/y">Bak</a></p></body></html>')
    assert "[Bak](https://x.example/y)" in out


def test_internal_link_is_rewritten_by_resolver():
    href = "https://polaris.logo.cloud/docs/p/detail/" + encode_detail_segment(
        "external?cid=1&link=2&tenantId=3&hideName=True"
    )
    out = convert(
        f'<html><body><p><a href="{href}">Diger</a></p></body></html>',
        link_resolver=lambda _h: "../Genel/Diger.md",
    )
    assert "[Diger](../Genel/Diger.md)" in out


def test_link_with_spaces_is_wrapped_in_angle_brackets():
    out = convert('<html><body><p><a href="a b.md">x</a></p></body></html>')
    assert "[x](<a b.md>)" in out


# -- baglanti kodlamalari -------------------------------------------------------------------

def test_base64_detail_segment_round_trip():
    doc_url = "external?cid=1&link=2&tenantId=3&hideName=True"
    assert decode_detail_segment(encode_detail_segment(doc_url)) == doc_url


def test_double_url_encoded_internal_link_is_decoded():
    """Dokuman govdesindeki ic baglantilar base64 degil, cift URL kodludur."""
    href = (
        "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/"
        "external%253Fcid%253Daaa%2526link%253Dbbb%2526tenantId%253Dccc"
    )
    assert doc_url_from_link(href) == "external?cid=aaa&link=bbb&tenantId=ccc"


def test_non_document_link_returns_none():
    assert doc_url_from_link("https://www.youtube.com/watch?v=abc") is None
    assert doc_url_from_link("") is None


# -- gorseller -----------------------------------------------------------------------------

def test_image_extension_comes_from_magic_bytes_not_mime():
    """Kaynak HTML butun gorselleri image/png diye bildirir ama cogu JPEG'dir."""
    assert sniff_extension(b"\xff\xd8\xff\xe0rest", "image/png") == ".jpg"
    assert sniff_extension(b"\x89PNG\r\n\x1a\nrest", "image/png") == ".png"
    assert sniff_extension(b"GIF89a", "image/png") == ".gif"


def test_skip_mode_drops_images():
    out = convert('<html><body><p><img src="data:image/png;base64,iVBORw0KGgo="/></p></body></html>')
    assert "![" not in out


# -- gomulu icerik ---------------------------------------------------------------------

def test_iframe_inside_inline_context_is_not_lost():
    """Kaynakta YouTube gomuluri <span><strong> icinde, yani satir ici baglamda.

    Yalnizca blok baglaminda iframe arayan bir donusturucu 10 videoyu sessizce yutar.
    """
    markup = (
        "<html><body><p><span><strong>"
        '<iframe class="youtube-player" src="//www.youtube.com/embed/abc123XYZ?wmode=opaque">'
        "</iframe></strong></span></p></body></html>"
    )
    result = MarkdownConverter(image_mode="skip").convert(markup)
    assert result.embeds == 1
    assert "https://www.youtube.com/embed/abc123XYZ" in result.markdown
    assert "abc123XYZ" in result.markdown


def test_protocol_relative_src_gets_https():
    markup = '<html><body><div><iframe src="//example.com/x"></iframe></div></body></html>'
    assert "https://example.com/x" in convert(markup)


# -- ikinci kutu sistemi ----------------------------------------------------------------

def test_bsv_callout_is_transparent_not_a_note_box():
    """`bsv-callout` bir not kutusu DEGIL - sayfa bolumu kapsayicisidir.

    Kaynakta icinde <h2> basliklari ve 28.000 karakterlik tablolar tasiyor. Alinti
    blogu yapmak butun surum notu sayfasini tek bir alintiya cevirirdi.
    """
    markup = (
        "<html><body><div class='bsv-callout bsv-callout-success'>"
        "<h2>Surumde Yer Alan Yenilikler</h2>"
        "<table><tr><th>Sira</th><th>Tanim</th></tr><tr><td>1</td><td>x</td></tr></table>"
        "</div></body></html>"
    )
    out = convert(markup)
    assert "> [!" not in out, "bolum kapsayicisi alintiya cevrilmemeli"
    assert "## Surumde Yer Alan Yenilikler" in out
    assert "| Sira | Tanim |" in out


def test_heading_text_is_plain_not_double_emphasised():
    """Kaynakta bolum basliklarinin cogu <strong> ile sarili."""
    markup = "<html><body><h1>T</h1><h3><span><strong>Bolum</strong></span></h3></body></html>"
    out = convert(markup)
    assert "### Bolum" in out
    assert "**" not in out


def test_punctuation_only_emphasis_is_not_wrapped():
    """Kaynakta yalnizca tirnak isaretini saran <em> etiketleri var; `*"*` bozuktur."""
    out = convert('<html><body><p>Once<em>"</em>sonra</p></body></html>')
    assert '*"*' not in out
    assert '"' in out


# -- alti cizili -------------------------------------------------------------------------

def test_underline_is_preserved_as_html():
    out = convert("<html><body><p><u>alti cizili</u></p></body></html>")
    assert "<u>alti cizili</u>" in out


# -- baslik satiri tespiti ------------------------------------------------------------------

def test_bold_td_row_is_treated_as_header():
    """Tablolarin bir bolumu hic <th> kullanmaz; ilk satiri kalin <td>'dir."""
    markup = (
        "<html><body><table>"
        "<tr><td><p><strong>Ay Kodu</strong></p></td><td><p><strong>Hesap</strong></p></td></tr>"
        "<tr><td>01</td><td>Kasa</td></tr>"
        "</table></body></html>"
    )
    out = convert(markup)
    assert "| Ay Kodu | Hesap |" in out
    assert "| --- | --- |" in out
    assert "| 01 | Kasa |" in out


def test_plain_first_row_is_not_a_header():
    markup = (
        "<html><body><table>"
        "<tr><td>01</td><td>Kasa</td></tr><tr><td>02</td><td>Banka</td></tr>"
        "</table></body></html>"
    )
    out = convert(markup)
    assert "|  |  |" in out          # bos baslik satiri
    assert "| 01 | Kasa |" in out


def test_repeated_thead_is_emitted_once():
    markup = (
        "<html><body><table>"
        "<thead><tr><th>A</th><th>B</th></tr></thead>"
        "<thead><tr><th>A</th><th>B</th></tr></thead>"
        "<tbody><tr><td>1</td><td>2</td></tr></tbody>"
        "</table></body></html>"
    )
    out = convert(markup)
    assert out.count("| A | B |") == 1


def test_colspan_one_is_not_treated_as_a_merge():
    """Kaynakta colspan 792 kez geciyor ve hepsi "1" - yani anlamsiz.

    Varligina bakan bir kod butun tablolari gereksiz yere HTML'e dusururdu.
    """
    markup = (
        "<html><body><table>"
        "<tr><th colspan='1'>A</th><th colspan='1'>B</th></tr>"
        "<tr><td colspan='1'>1</td><td colspan='1'>2</td></tr>"
        "</table></body></html>"
    )
    out = convert(markup)
    assert "| A | B |" in out
    assert "<table>" not in out


# -- basliklar ------------------------------------------------------------------------------

def test_all_heading_levels_are_kept_even_when_they_skip():
    """Kaynakta h1 -> h4 -> h5 gibi atlayan seviyeler var; yeniden numaralandirma yapilmamali."""
    markup = "<html><body><h1>Bir</h1><h4>Dort</h4><h5>Bes</h5></body></html>"
    out = convert(markup)
    assert "# Bir" in out
    assert "#### Dort" in out
    assert "##### Bes" in out


def test_multiple_h1_keeps_all_but_first_is_the_title():
    markup = "<html><body><h1>Ilk</h1><p>x</p><h1>Ikinci</h1></body></html>"
    result = MarkdownConverter(image_mode="skip").convert(markup)
    assert result.title == "Ilk"
    assert result.markdown.count("# ") >= 2
    assert "# Ikinci" in result.markdown


# -- istege bagli baslik yukseltme ---------------------------------------------------------

def promote(markup: str) -> str:
    return MarkdownConverter(image_mode="skip", promote_bold_headings=True).convert(markup).markdown


def test_bold_paragraph_promoted_only_when_enabled():
    markup = "<html><body><h1>T</h1><p><strong>Ön Sorgulama</strong></p></body></html>"
    assert "## Ön Sorgulama" not in convert(markup), "varsayilan olarak kapali olmali"
    assert "## Ön Sorgulama" in promote(markup)


def test_promotion_is_skipped_when_document_has_real_headings():
    """Gercek bolum basligi varsa yapay baslik uretmek yapiyi bozar."""
    markup = (
        "<html><body><h1>T</h1><h2>Gercek Bolum</h2>"
        "<p><strong>Kalin ama baslik degil</strong></p></body></html>"
    )
    out = promote(markup)
    assert "## Gercek Bolum" in out
    assert "## Kalin ama baslik degil" not in out
    assert "**Kalin ama baslik degil**" in out


def test_run_in_label_is_not_promoted():
    """`**Esit Degil:** Raporda ...` bir satir basi etiketidir, baslik degil."""
    markup = (
        "<html><body><h1>T</h1>"
        "<p><strong>Eşit Değil:</strong> Raporda listelenmeyecek kayitlar.</p></body></html>"
    )
    out = promote(markup)
    assert "## " not in out
    assert "**Eşit Değil:**" in out


def test_long_or_sentence_like_bold_is_not_promoted():
    markup = (
        "<html><body><h1>T</h1><p><strong>Bu cümle bir başlık değildir ve nokta ile biter.</strong></p>"
        "</body></html>"
    )
    assert "## " not in promote(markup)


# -- satir sonlari --------------------------------------------------------------------------

def test_br_inside_paragraph_keeps_the_line_break():
    """Kaynakta ~330 paragraf ici <br> var; paragrafi bolmek de silmek de yanlis."""
    out = convert("<html><body><p>Birinci satir<br/>Ikinci satir</p></body></html>")
    assert out == "Birinci satir\nIkinci satir"


def test_paragraph_containing_only_br_is_dropped():
    out = convert("<html><body><p>A</p><p><br/></p><p>B</p></body></html>")
    assert out == "A\n\nB"


def test_leading_br_does_not_create_a_blank_line():
    assert convert("<html><body><p><br/>Metin</p></body></html>") == "Metin"


def test_br_class_variant_behaves_the_same():
    """`atl-forced-newline` sinifi ile duz <br> anlamca ayni; sinifa gore dallanma."""
    a = convert("<html><body><p>A<br/>B</p></body></html>")
    b = convert('<html><body><p>A<br class="atl-forced-newline"/>B</p></body></html>')
    assert a == b == "A\nB"


def test_cell_line_break_becomes_html_br_not_a_newline():
    """GFM satiri tek fiziksel satir olmali; hucre ici satir sonu <br> olur."""
    out = convert("<html><body><table><tr><td>A<br/>B</td><td>C</td></tr></table></body></html>")
    assert "| A<br>B | C |" in out


def test_empty_cell_renders_empty_not_as_stray_br():
    out = convert(
        "<html><body><table><tr><td>A</td><td><p><br/></p></td></tr></table></body></html>"
    )
    assert "| A |  |" in out
    assert "<br>" not in out


def test_paragraph_with_only_an_image_is_kept():
    """308 paragraf yalnizca gorsel iceriyor; 'bos' sayilip silinmemeli."""
    markup = '<html><body><p><img src="data:image/png;base64,iVBORw0KGgo="/></p></body></html>'
    out = MarkdownConverter(image_mode="inline").convert(markup).markdown
    assert out.startswith("![")


def test_nbsp_only_paragraph_is_dropped():
    out = convert("<html><body><p>A</p><p>&#160;&nbsp;</p><p>B</p></body></html>")
    assert out == "A\n\nB"
