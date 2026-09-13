"""Sabitler ve calisma ayarlari.

Buradaki uc adres, Logo'nun Angular tabanli dokuman portalinin (`polaris.logo.cloud`)
canli yapilandirmasindan (`/assets/config/app.config.json`) dogrulanarak alinmistir:

* ``DYS_APP_URL``            -> https://dys.logo.cloud       (iframe'in gosterdigi Vaadin uygulamasi)
* ``CONFIG.TOKEN.API_URI``   -> https://polaris.logo.com.tr  (hiyerarsi/agac API'si)
* Portal onyuzu              -> https://polaris.logo.cloud   (kullanicinin gordugu adres)
"""

from __future__ import annotations

import dataclasses
from pathlib import Path

# --------------------------------------------------------------------------------------
# Uzak servis adresleri
# --------------------------------------------------------------------------------------

#: Dokuman icerigini barindiran Vaadin 8 uygulamasi (iframe hedefi).
DYS_BASE_URL = "https://dys.logo.cloud"

#: Hiyerarsi agacini donen REST API.
CATALOG_API_BASE = "https://polaris.logo.com.tr"

#: Kullanicinin tarayicida gordugu portal (CSV'deki baglantilarin ana adresi).
PORTAL_BASE_URL = "https://polaris.logo.cloud"

#: Varsayilan urun kodu. CSV'deki baglantilarda `/docs/<product>/detail/...` olarak gecer.
DEFAULT_PRODUCT = "netsis-3-enterprise"

#: Vaadin uygulamasinin DOM kok kimligi. Onyukleme (bootstrap) istegi ile dogrulanir;
#: burada yalnizca ilk deneme icin bir baslangic degeri olarak tutulur.
FALLBACK_APP_ID = "ROOT-2521314"
FALLBACK_THEME = "documentservice"

#: Sunucuya kendimizi tanittigimiz kimlik. Iletisim adresi eklemek nezaket geregidir.
USER_AGENT = (
    "netsis-expert-ai-docs-fetcher/1.0 "
    "(+https://github.com/serkanhancioglu/netsis-expert-ai; "
    "Mozilla/5.0 compatible)"
)

# --------------------------------------------------------------------------------------
# Cikti duzeni
# --------------------------------------------------------------------------------------

#: Ayni klasorde hem alt basliklari hem kendi icerigi olan dugumun dosya adi.
BRANCH_DOCUMENT_FILENAME = "index.md"

#: Gorsellerin yazildigi, cikti kokune gore tek ve ortak klasor.
ASSETS_DIRNAME = "_assets"

#: Calisma durumunun tutuldugu SQLite dosyasi (cikti kokune gore).
STATE_FILENAME = ".netsis-scraper-state.sqlite3"

#: Hiyerarsi agacinin diske alinan kopyasi (cevrimdisi tekrar calistirma icin).
CATALOG_CACHE_FILENAME = ".netsis-catalog.json"

# --------------------------------------------------------------------------------------
# Ag davranisi
# --------------------------------------------------------------------------------------

#: Sunucuyu yormamak icin ayni anda calisan is parcacigi sayisi.
DEFAULT_CONCURRENCY = 3

#: Iki istek arasinda global olarak beklenen en kisa sure (saniye).
DEFAULT_MIN_INTERVAL = 0.35

#: Bir dokuman icin en fazla kac kez yeniden denenecegi.
DEFAULT_MAX_ATTEMPTS = 5

#: Baglanti kurma ve okuma zaman asimlari (saniye).
CONNECT_TIMEOUT = 20.0
READ_TIMEOUT = 180.0

#: Yeniden denemeye deger HTTP durum kodlari.
RETRYABLE_STATUS = frozenset({408, 425, 429, 500, 502, 503, 504})

#: Ustel bekleme tabani ve tavani (saniye).
BACKOFF_BASE = 1.5
BACKOFF_CAP = 60.0

#: Bir Vaadin oturumunun cerezi ~1900 sn sonra duser. Guvenli tarafta kalmak icin
#: her is parcacigi oturumunu bu surede bir tazeler.
SESSION_MAX_AGE = 1500.0

#: Tek bir dokuman akisinin kabul edilen en buyuk boyutu (bayt). Ornek kumede en
#: buyuk dokuman 2.8 MB idi; 64 MB fazlasiyla emniyetli bir ust sinirdir.
MAX_STREAM_BYTES = 64 * 1024 * 1024


@dataclasses.dataclass(slots=True)
class Settings:
    """Tek bir calisma icin cozulmus ayarlar."""

    output_dir: Path
    product: str = DEFAULT_PRODUCT
    concurrency: int = DEFAULT_CONCURRENCY
    min_interval: float = DEFAULT_MIN_INTERVAL
    max_attempts: int = DEFAULT_MAX_ATTEMPTS
    image_mode: str = "files"          # files | inline | skip
    promote_bold_headings: bool = False  # kalin paragraflari baslik say
    include_branches: bool = True      # alt basligi olan dugumler de indirilsin mi
    number_prefix: bool = False        # klasor/dosya adlarina sira numarasi eklensin mi
    max_path_length: int = 240         # Windows MAX_PATH icin guvenli ust sinir
    force: bool = False                # tamamlanmis dokumanlari da yeniden indir
    retry_failed: bool = False         # yalnizca hatali kalanlari yeniden dene
    limit: int | None = None           # ilk N dokuman (deneme amacli)
    dry_run: bool = False
    keep_html: bool = False            # ham HTML kopyasi da saklansin mi
    offline_catalog: bool = False      # agaci agdan degil onbellekten oku
    verbose: bool = False

    @property
    def assets_dir(self) -> Path:
        return self.output_dir / ASSETS_DIRNAME

    @property
    def state_path(self) -> Path:
        return self.output_dir / STATE_FILENAME

    @property
    def catalog_cache_path(self) -> Path:
        return self.output_dir / CATALOG_CACHE_FILENAME
