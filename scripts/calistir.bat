@echo off
REM Netsis dokuman indirici - Windows baslatici
REM
REM Kullanim:
REM   calistir.bat                 -> tamamini indirir (.\netsis-docs klasorune)
REM   calistir.bat --limit 20      -> once 20 dokumanla dener
REM   calistir.bat --retry-failed  -> hatali kalanlari yeniden dener
REM
REM Ek secenekler icin: calistir.bat --help

setlocal
cd /d "%~dp0"

REM Turkce karakterlerin konsolda dogru gorunmesi icin UTF-8 kod sayfasi.
chcp 65001 >nul

where py >nul 2>&1 && (set "PY=py -3") || (set "PY=python")

%PY% -c "import sys; sys.exit(0 if sys.version_info>=(3,10) else 1)" 2>nul
if errorlevel 1 (
  echo HATA: Python 3.10 veya uzeri gerekiyor. https://www.python.org/downloads/
  pause
  exit /b 1
)

if not exist ".venv" (
  echo ^>^> Sanal ortam olusturuluyor ^(.venv^) ...
  %PY% -m venv .venv
)

call .venv\Scripts\activate.bat

echo ^>^> Bagimliliklar denetleniyor ...
python -m pip install --quiet --upgrade pip
python -m pip install --quiet -r requirements.txt

echo ^>^> Indirme basliyor. Durdurmak icin Ctrl-C; ayni komutla kaldigi yerden devam eder.
python -m netsis_scraper --output .\netsis-docs %*

echo.
echo Bitti. Cikti klasoru: %cd%\netsis-docs
pause
