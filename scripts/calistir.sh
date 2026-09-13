#!/usr/bin/env bash
# Netsis dokuman indirici - macOS / Linux baslatici
#
# Kullanim:
#   ./calistir.sh                 -> tamamini indirir (../knowledge-base/markdown)
#   ./calistir.sh --limit 20      -> once 20 dokumanla dener
#   ./calistir.sh --retry-failed  -> hatali kalanlari yeniden dener
#
# Ek secenekler icin: ./calistir.sh --help

set -euo pipefail
cd "$(dirname "$0")"

# Turkce karakterler icin UTF-8'i garantile (bazi sunucularda locale C olabilir).
export PYTHONUTF8=1
export PYTHONIOENCODING=utf-8

PYTHON="${PYTHON:-python3}"
VENV=".venv"

if ! command -v "$PYTHON" >/dev/null 2>&1; then
  echo "HATA: '$PYTHON' bulunamadi. Python 3.10 veya uzeri kurun." >&2
  exit 1
fi

"$PYTHON" - <<'PYCHECK' || { echo "HATA: Python 3.10 veya uzeri gerekiyor." >&2; exit 1; }
import sys
raise SystemExit(0 if sys.version_info >= (3, 10) else 1)
PYCHECK

if [ ! -d "$VENV" ]; then
  echo ">> Sanal ortam olusturuluyor ($VENV) ..."
  "$PYTHON" -m venv "$VENV"
fi

# shellcheck disable=SC1091
source "$VENV/bin/activate"

echo ">> Bagimliliklar denetleniyor ..."
python -m pip install --quiet --upgrade pip
python -m pip install --quiet -r requirements.txt

echo ">> Indirme basliyor. Durdurmak icin Ctrl-C; ayni komutla kaldigi yerden devam eder."
exec python -m netsis_scraper --output ../knowledge-base/markdown "$@"
