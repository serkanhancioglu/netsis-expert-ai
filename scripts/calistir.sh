#!/usr/bin/env bash
# =============================================================================
#  Netsis dokuman indirici - macOS / Linux baslatici
#
#  Kullanim:
#    ./calistir.sh                    tamamini indirir
#    ./calistir.sh --limit 20         once 20 dokumanla dener
#    ./calistir.sh --retry-failed     hatali kalanlari yeniden dener
#    ./calistir.sh --output /yol      ciktiyi baska yere yazar
#    ./calistir.sh --help             butun secenekler
#
#  Sanal ortam kurulamazsa sistem Python'u ile devam eder; bu calisir bir yoldur.
# =============================================================================

set -uo pipefail
cd "$(dirname "$0")"

# Turkce karakterler: bazi sunucularda locale C oldugu icin garantiye al.
export PYTHONUTF8=1
export PYTHONIOENCODING=utf-8

echo
echo "================================================================"
echo " Netsis dokumantasyon indirici"
echo "================================================================"
echo

# ------------------------------------------------------------------ python bul
PY=""
for candidate in "${PYTHON:-}" python3 python; do
    [ -n "$candidate" ] || continue
    command -v "$candidate" >/dev/null 2>&1 || continue
    if "$candidate" -c 'import sys; raise SystemExit(0 if sys.version_info >= (3, 10) else 1)' 2>/dev/null; then
        PY="$candidate"
        break
    fi
done

if [ -z "$PY" ]; then
    echo " HATA: Python 3.10 veya uzeri bulunamadi."
    echo "       macOS : brew install python@3.12"
    echo "       Ubuntu: sudo apt install python3 python3-venv python3-pip"
    exit 1
fi
echo " Python $("$PY" -c 'import sys; print(sys.version.split()[0])') bulundu."

# ------------------------------------------------- sanal ortam (basarisiz olabilir)
RUNPY="$PY"
if [ -x ".venv/bin/python" ]; then
    RUNPY=".venv/bin/python"
    echo " Sanal ortam hazir."
else
    echo " Sanal ortam kuruluyor (.venv) ..."
    if "$PY" -m venv .venv >/dev/null 2>&1 && [ -x ".venv/bin/python" ]; then
        RUNPY=".venv/bin/python"
        echo " Sanal ortam hazir."
    else
        echo
        echo " Sanal ortam kurulamadi (izin ya da python3-venv eksikligi olabilir)."
        echo " Sistem Python'u ile devam ediliyor - bu tamamen calisir bir yoldur."
        echo
    fi
fi

# ---------------------------------------------------------------- bagimliliklar
if "$RUNPY" -c 'import requests, bs4' >/dev/null 2>&1; then
    echo " Bagimliliklar zaten kurulu."
else
    echo " Bagimliliklar kuruluyor ..."
    "$RUNPY" -m pip install --quiet --disable-pip-version-check -r requirements.txt >/dev/null 2>&1 \
        || "$RUNPY" -m pip install --quiet --disable-pip-version-check --user -r requirements.txt >/dev/null 2>&1 \
        || true
    if ! "$RUNPY" -c 'import requests, bs4' >/dev/null 2>&1; then
        echo
        echo " HATA: requests ve beautifulsoup4 kurulamadi. Elle deneyin:"
        echo "       $RUNPY -m pip install -r requirements.txt"
        exit 1
    fi
fi

# ---------------------------------------------------------------- cikti yeri
CIKTI=()
HEDEF=""
if ! printf '%s\n' "$@" | grep -q -- '--output'; then
    HEDEF="../knowledge-base/markdown"
    [ -d "../knowledge-base" ] || HEDEF="./netsis-docs"
    if ! mkdir -p "$HEDEF" 2>/dev/null || ! touch "$HEDEF/.yazma-testi" 2>/dev/null; then
        echo
        echo " UYARI: $HEDEF klasorune yazilamiyor."
        echo "        Cikti $HOME/netsis-docs klasorune yonlendiriliyor."
        HEDEF="$HOME/netsis-docs"
        mkdir -p "$HEDEF"
    fi
    rm -f "$HEDEF/.yazma-testi"
    CIKTI=(--output "$HEDEF")
fi

echo
echo " Indirme basliyor. Tamami yaklasik 35 dakika surer."
echo " Durdurmak icin Ctrl-C - ayni komutu tekrar calistirdiginizda"
echo " kaldigi yerden devam eder, indirilenler tekrar indirilmez."
echo
echo " Bu betigi bir yapay zeka aracinin komut calistiricisindan degil,"
echo " dogrudan bir terminalden calistirin: onlarin zaman siniri isi"
echo " yarida keser. Parcali gitmek isterseniz --limit 300 kullanin."
echo

"$RUNPY" -m netsis_scraper "${CIKTI[@]}" "$@"
SONUC=$?

echo
case "$SONUC" in
    0)   echo " Bitti." ;;
    130) echo " Durduruldu. Ilerleme kaydedildi; ayni komutla devam edebilirsiniz." ;;
    *)   echo " Bazi dokumanlar indirilemedi (cikis kodu $SONUC)."
         echo " Yeniden denemek icin: ./calistir.sh --retry-failed" ;;
esac
[ -n "$HEDEF" ] && echo " Cikti klasoru: $(cd "$HEDEF" 2>/dev/null && pwd || echo "$HEDEF")"
exit "$SONUC"
