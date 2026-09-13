@echo off
REM ============================================================================
REM  Netsis dokuman indirici - Windows baslatici
REM
REM  Kullanim:
REM    calistir.bat                    tamamini indirir
REM    calistir.bat --limit 20         once 20 dokumanla dener
REM    calistir.bat --retry-failed     hatali kalanlari yeniden dener
REM    calistir.bat --output C:\yol    ciktiyi baska yere yazar
REM    calistir.bat --help             butun secenekler
REM
REM  NOT: Yonetici olarak calistirmayin. Gerek yok ve sanal ortam kurulumunda
REM       izin hatasina yol acabiliyor.
REM ============================================================================

setlocal EnableExtensions
cd /d "%~dp0"

REM Turkce karakterler. chcp yalnizca etkilesimli konsolu duzeltir; cikti bir
REM dosyaya yonlendirilirse Python yine cp1254 kullanir ve dokumanlardaki
REM ok/tirnak karakterlerinde UnicodeEncodeError firlatir. PYTHONUTF8 kokten cozer.
chcp 65001 >nul 2>&1
set "PYTHONUTF8=1"
set "PYTHONIOENCODING=utf-8"

echo.
echo ================================================================
echo  Netsis dokumantasyon indirici
echo ================================================================
echo.

REM ---------------------------------------------------------------- uyarilar
net session >nul 2>&1
if not errorlevel 1 (
  echo  UYARI: Bu pencere YONETICI olarak acilmis.
  echo         Gerek yok. Yonetici komut istemi System32'de baslar ve sanal
  echo         ortam kurulumunda izin hatasi verebiliyor.
  echo         Sorun yasarsaniz normal bir komut istemiyle tekrar deneyin.
  echo.
)

echo %CD% | find /i "\Temp\" >nul
if not errorlevel 1 (
  echo  UYARI: Gecici klasorden ^(Temp^) calisiyorsunuz.
  echo         ZIP'i once kalici bir yere cikarin, ornegin C:\netsis-scraper
  echo.
)

REM ---------------------------------------------------------------- python bul
set "PY="
py -3 -c "import sys; sys.exit(0 if sys.version_info>=(3,10) else 1)" >nul 2>&1
if not errorlevel 1 set "PY=py -3"

if not defined PY (
  python -c "import sys; sys.exit(0 if sys.version_info>=(3,10) else 1)" >nul 2>&1
  if not errorlevel 1 set "PY=python"
)

if not defined PY (
  echo  HATA: Python 3.10 veya uzeri bulunamadi.
  echo.
  echo        Kurulum: https://www.python.org/downloads/
  echo        Kurarken "Add Python to PATH" secenegini isaretleyin.
  goto :bitir
)

for /f "delims=" %%v in ('%PY% -c "import sys;print(sys.version.split()[0])" 2^>nul') do set "PYVER=%%v"
echo  Python %PYVER% bulundu.

REM ------------------------------------------------- sanal ortam (basarisiz olabilir)
set "RUNPY=%PY%"
set "VENVPY=.venv\Scripts\python.exe"

if exist "%VENVPY%" goto :venv_hazir

echo  Sanal ortam kuruluyor ^(.venv^) ...
%PY% -m venv .venv >nul 2>&1
if exist "%VENVPY%" goto :venv_hazir

echo.
echo  Sanal ortam kurulamadi ^(genellikle izin ya da ensurepip sorunu^).
echo  Sistem Python'u ile devam ediliyor - bu tamamen calisir bir yoldur.
echo.
goto :bagimliliklar

:venv_hazir
set "RUNPY=%VENVPY%"
echo  Sanal ortam hazir.

REM ---------------------------------------------------------------- bagimliliklar
:bagimliliklar
%RUNPY% -c "import requests, bs4" >nul 2>&1
if not errorlevel 1 (
  echo  Bagimliliklar zaten kurulu.
  goto :calistir
)

echo  Bagimliliklar kuruluyor ...
%RUNPY% -m pip install --quiet --disable-pip-version-check -r requirements.txt
%RUNPY% -c "import requests, bs4" >nul 2>&1
if not errorlevel 1 goto :calistir

echo  Kurulum basarisiz. Kullanici klasorune kuruluyor ...
%RUNPY% -m pip install --quiet --disable-pip-version-check --user -r requirements.txt
%RUNPY% -c "import requests, bs4" >nul 2>&1
if not errorlevel 1 goto :calistir

echo.
echo  HATA: requests ve beautifulsoup4 kurulamadi.
echo        Elle deneyin:
echo            %RUNPY% -m pip install -r requirements.txt
goto :bitir

REM ---------------------------------------------------------------- cikti yeri
:calistir
REM Kullanici --output verdiyse ona dokunma; yoksa yazilabilir bir yer sec.
echo %* | find "--output" >nul
if not errorlevel 1 goto :baslat

set "HEDEF=..\knowledge-base\markdown"
if not exist "..\knowledge-base" set "HEDEF=.\netsis-docs"

REM Yazma iznini gercekten sina - varsaymak yerine dene.
mkdir "%HEDEF%" >nul 2>&1
type nul > "%HEDEF%\.yazma-testi" 2>nul
if exist "%HEDEF%\.yazma-testi" goto :yazilabilir

echo.
echo  UYARI: %HEDEF% klasorune yazilamiyor.
echo         Cikti %USERPROFILE%\netsis-docs klasorune yonlendiriliyor.
set "HEDEF=%USERPROFILE%\netsis-docs"
mkdir "%HEDEF%" >nul 2>&1

:yazilabilir
del "%HEDEF%\.yazma-testi" >nul 2>&1

set CIKTI=--output "%HEDEF%"

:baslat
echo.
echo  Indirme basliyor. Tamami yaklasik 35 dakika surer.
echo  Durdurmak icin Ctrl-C - ayni komutu tekrar calistirdiginizda
echo  kaldigi yerden devam eder, indirilenler tekrar indirilmez.
echo.
echo  Bu betigi bir yapay zeka aracinin komut calistiricisindan degil,
echo  dogrudan bir komut isteminden calistirin: onlarin zaman siniri
echo  isi yarida keser. Parcali gitmek isterseniz --limit 300 kullanin.
echo.

%RUNPY% -m netsis_scraper %CIKTI% %*
set "SONUC=%ERRORLEVEL%"

echo.
if "%SONUC%"=="0" (
  echo  Bitti.
) else (
  if "%SONUC%"=="130" (
    echo  Durduruldu. Ilerleme kaydedildi; ayni komutla devam edebilirsiniz.
  ) else (
    echo  Bazi dokumanlar indirilemedi ^(cikis kodu %SONUC%^).
    echo  Yeniden denemek icin: calistir.bat --retry-failed
  )
)
if defined HEDEF echo  Cikti klasoru: %HEDEF%

:bitir
echo.
pause
endlocal
