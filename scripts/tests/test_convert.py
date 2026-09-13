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
