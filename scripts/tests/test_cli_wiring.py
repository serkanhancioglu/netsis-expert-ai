"""Komut satiri secenekleri gercekten calisma ayarlarina ulasiyor mu?

Bu dosya bir hata sinifina karsi yazildi: ``--promote-bold-headings`` eklendiginde
argparse tanimi, ``Settings`` alani ve donusturucu cagrisi yazilmis ama secenegi
``Settings``'e gecirmek unutulmustu. Bayrak sessizce etkisiz kaldi; hicbir test
patlamadi cunku her parca tek basina dogruydu. Asagidaki test butun secenekleri
tek tek degil topluca denetler, boylece bir dahakine kimse unutamaz.
"""

import dataclasses
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from netsis_scraper import config  # noqa: E402
from netsis_scraper.cli import build_parser  # noqa: E402

#: Bu secenekler bilerek Settings'e gitmez; dogrudan main() icinde kullanilirlar.
#: Yeni bir secenek eklerken ya Settings'e baglayin ya da buraya, sebebiyle birlikte.
_HANDLED_ELSEWHERE = {
    "quiet",      # yalnizca ilerleme gostergesine gecer
    "csv",        # kapsama karsilastirmasi main() icinde yapilir
    "only_csv",   # dugum secimi main() icinde yapilir
    "manifest",   # indeks calisma bitince main() icinde yazilir
}


def _settings_block() -> str:
    source = (Path(__file__).resolve().parents[1] / "netsis_scraper" / "cli.py").read_text(
        encoding="utf-8"
    )
    match = re.search(r"settings = config\.Settings\((.*?)\n    \)", source, re.S)
    assert match, "cli.py icinde Settings(...) cagrisi bulunamadi"
    return match.group(1)


def test_every_cli_option_reaches_settings():
    block = _settings_block()
    used = set(re.findall(r"args\.([a-z_]+)", block))
    options = {a.dest for a in build_parser()._actions if a.dest not in ("help", "version")}
    missing = sorted(options - used - _HANDLED_ELSEWHERE)
    assert not missing, f"Settings'e hic gecmeyen secenekler: {missing}"


def test_every_settings_field_is_filled_from_an_option():
    block = _settings_block()
    assigned = set(re.findall(r"^\s*([a-z_]+)=", block, re.M))
    fields = {f.name for f in dataclasses.fields(config.Settings)}
    missing = sorted(fields - assigned)
    assert not missing, f"argumanla doldurulmayan Settings alanlari: {missing}"


def test_parser_accepts_every_documented_flag():
    parser = build_parser()
    args = parser.parse_args(
        [
            "--output", "cikti", "--limit", "5", "--images", "skip",
            "--promote-bold-headings", "--number-prefix", "--skip-branches",
            "--keep-html", "--refresh", "--dry-run", "-j", "2",
            "--min-interval", "1.0", "--max-attempts", "2",
            "--max-path-length", "150", "--offline-catalog", "-v", "-q",
        ]
    )
    assert args.promote_bold_headings is True
    assert args.refresh is True
    assert args.images == "skip"
    assert args.max_path_length == 150


def test_force_and_refresh_are_distinct_settings():
    """--force her dosyayi yeniden yazar; --refresh yalnizca degiseni."""
    parser = build_parser()
    assert parser.parse_args(["--force"]).refresh is False
    assert parser.parse_args(["--refresh"]).force is False


def test_manifest_option_is_accepted():
    args = build_parser().parse_args(["--manifest", "kb/metadata/articles-manifest.csv"])
    assert str(args.manifest).endswith("articles-manifest.csv")
