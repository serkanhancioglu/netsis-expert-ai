"""Logo DYS (Vaadin 8) dokuman servisiyle konusan HTTP istemcisi.

Bir dokumanin metnine ulasmak icin uc adim gerekir; istemci bunlarin ikisini
oturum basina bir kez yaparak sunucu yukunu ucte bir azaltir:

1. **Onyukleme (oturum basina bir kez).** ``GET /external?cid=...`` istegi, icinde
   ``vaadin.initApplication("<appId>", {...})`` bulunan bir kabuk HTML dondurur.
   Buradan uygulama kimligi, tema ve oturum cerezi alinir.
2. **UIDL istegi (dokuman basina).** Ayni adrese ``application/x-www-form-urlencoded``
   govdeyle POST yapilir. Yanit ``{"v-uiId":0,"uidl":"<JSON metni>"}`` seklindedir.
   Cozulen UIDL'in ``state`` agacinda ``LbsBrowserFrame`` bileseninin
   ``resources.source.uRL`` alani gercek icerigin adresidir.
3. **Akis (dokuman basina).** ``GET https://dys.logo.cloud/stream/?tCid=<uuid>``
   istegi asil dokuman HTML'ini dondurur.

Gecersiz veya suresi dolmus bir baglantida UIDL yanitinda ``LbsBrowserFrame`` yerine
``externaShareExpired`` bileseni ve ``theme://images/task_list_warning.svg`` gibi bir
kaynak gelir. Bu durum ``ExpiredDocumentError`` olarak ayrilir; yeniden denenmez.
"""

from __future__ import annotations

import json
import logging
import random
import re
import threading
import time
from dataclasses import dataclass
from typing import Any

import requests
from requests.adapters import HTTPAdapter

from netsis_scraper import config

log = logging.getLogger(__name__)

_BOOTSTRAP_RE = re.compile(
    r'vaadin\.initApplication\(\s*"([^"]+)"\s*,\s*(\{.*?\})\s*\)\s*;', re.DOTALL
)

#: Gecerli bir icerik adresi yalnizca su bicimde olur. Bicim kisiti olmadan, geri
#: donus dalı yanlislikla bir tema ikonunu ya da baska bir varligi indirebilir.
_STREAM_URL_RE = re.compile(
    r"^https://[a-z0-9.-]*\bdys\.logo\.cloud/stream/\?tCid=[0-9a-fA-F-]{36}$"
)

#: Yanit govdesinden karakter kumesini okumak icin.
_META_CHARSET_RE = re.compile(
    rb"""<meta[^>]+charset\s*=\s*["']?\s*([A-Za-z0-9_.:-]+)""", re.IGNORECASE
)


# --------------------------------------------------------------------------------------
# Hatalar
# --------------------------------------------------------------------------------------

class FetchError(Exception):
    """Bu istemcinin urettigi tum hatalarin ortak atasi."""

    retryable = False


class TransientError(FetchError):
    """Gecici sorun: yeniden denemeye deger (ag hatasi, 5xx, 429).

    ``session_fault`` yalnizca sorunun oturumdan kaynaklandigi durumlarda dogrudur
    (yetkilendirme yonlendirmesi, JSON olmayan UIDL yaniti, onyukleme betiginin
    bulunamamasi). Yalnizca akis indirilirken olusan bir ag hatasi icin saglam bir
    oturumu atmak gereksiz yere fazladan istek dogurur.
    """

    retryable = True

    def __init__(
        self, message: str, retry_after: float | None = None, *, session_fault: bool = False
    ) -> None:
        super().__init__(message)
        self.retry_after = retry_after
        self.session_fault = session_fault


class PermanentError(FetchError):
    """Kalici sorun: yeniden denemek bir sey degistirmez (404, bozuk yanit)."""


class ExpiredDocumentError(PermanentError):
    """Paylasim baglantisi gecersiz ya da suresi dolmus."""


# --------------------------------------------------------------------------------------
# Hiz sinirlayici
# --------------------------------------------------------------------------------------

class RateLimiter:
    """Tum is parcaciklarinin paylastigi, en kisa istek araligini garanti eden kilit.

    ``429``/``503`` gorulunce ceza suresi devreye girer ve butun havuz yavaslar;
    her basarili istekte ceza kademeli olarak geri cekilir.
    """

    def __init__(self, min_interval: float) -> None:
        self._base_interval = max(0.0, min_interval)
        self._interval = self._base_interval
        self._next_slot = 0.0
        self._lock = threading.Lock()

    def acquire(self) -> None:
        """Sirasi gelene kadar bekler.

        Slot rezervasyonu kilit altinda **bir kez** yapilir, bekleme kilit disinda
        gerceklesir. Kilit icinde donen bir dongu her turda slotu bir aralik daha
        ileri iterek butun havuzu ac birakirdi.
        """
        with self._lock:
            now = time.monotonic()
            slot = max(now, self._next_slot)
            self._next_slot = slot + self._interval
        delay = slot - time.monotonic()
        if delay > 0:
            time.sleep(delay)

    def penalise(self, factor: float = 2.0, ceiling: float = 8.0) -> None:
        with self._lock:
            self._interval = min(ceiling, max(self._base_interval, self._interval) * factor)
            log.warning("Sunucu yavaslamamizi istedi; istek araligi %.2f sn'ye cikarildi.", self._interval)

    def relax(self) -> None:
        with self._lock:
            if self._interval > self._base_interval:
                self._interval = max(self._base_interval, self._interval * 0.9)


# --------------------------------------------------------------------------------------
# Istemci
# --------------------------------------------------------------------------------------

@dataclass(slots=True)
class Document:
    """Sunucudan alinan ham dokuman."""

    doc_url: str
    html: str
    encoding: str
    byte_length: int
    stream_url: str


class DysClient:
    """Is parcacigi guvenli DYS istemcisi.

    Her is parcacigi kendi ``requests.Session`` nesnesini ve kendi Vaadin oturumunu
    tasir; boylece cerezler karismaz. Oturum ``SESSION_MAX_AGE`` saniye sonra ya da
    bir yetkilendirme yonlendirmesi gorulunce kendiliginden tazelenir.
    """

    def __init__(
        self,
        rate_limiter: RateLimiter,
        *,
        max_attempts: int = config.DEFAULT_MAX_ATTEMPTS,
        stop_event: threading.Event | None = None,
        user_agent: str = config.USER_AGENT,
    ) -> None:
        self._rate = rate_limiter
        self._max_attempts = max(1, max_attempts)
        self._stop = stop_event or threading.Event()
        self._user_agent = user_agent
        self._local = threading.local()

    # -- oturum yonetimi ----------------------------------------------------------------

    def _new_session(self) -> requests.Session:
        session = requests.Session()
        session.headers.update(
            {
                "User-Agent": self._user_agent,
                "Accept-Language": "tr-TR,tr;q=0.9,en;q=0.8",
            }
        )
        adapter = HTTPAdapter(pool_connections=4, pool_maxsize=4, max_retries=0)
        session.mount("https://", adapter)
        session.mount("http://", adapter)
        return session

    def _state(self) -> dict[str, Any]:
        state = getattr(self._local, "state", None)
        if state is None:
            state = {"session": None, "app_id": None, "theme": None, "born": 0.0}
            self._local.state = state
        return state

    def reset_session(self) -> None:
        """Vaadin oturumunu bir sonraki istekte yeniden kurulmak uzere atar."""
        state = self._state()
        session = state.get("session")
        if session is not None:
            session.close()
        state.update({"session": None, "app_id": None, "theme": None, "born": 0.0})

    def _ensure_session(self, doc_url: str) -> tuple[requests.Session, str, str]:
        state = self._state()
        expired = (
            state["session"] is None
            or (time.monotonic() - state["born"]) > config.SESSION_MAX_AGE
        )
        if expired:
            if state["session"] is not None:
                state["session"].close()
            session = self._new_session()
            app_id, theme = self._bootstrap(session, doc_url)
            state.update(
                {"session": session, "app_id": app_id, "theme": theme, "born": time.monotonic()}
            )
        return state["session"], state["app_id"], state["theme"]

    # -- tek tek adimlar ----------------------------------------------------------------

    def _bootstrap(self, session: requests.Session, doc_url: str) -> tuple[str, str]:
        """Kabuk HTML'i indirip uygulama kimligi ile temayi cikarir."""
        url = f"{config.DYS_BASE_URL}/{doc_url.lstrip('/')}"
        response = self._request(session, "GET", url)
        text = response.text

        if "/oauth/authorize" in response.url:
            raise TransientError(
                "Sunucu oturum acma sayfasina yonlendirdi; oturum yeniden kurulacak.",
                session_fault=True,
            )

        match = _BOOTSTRAP_RE.search(text)
        if not match:
            snippet = " ".join(text.split())[:200]
            raise TransientError(
                f"Vaadin onyukleme betigi bulunamadi. Yanit basi: {snippet!r}", session_fault=True
            )

        app_id = match.group(1)
        try:
            bootstrap_config = json.loads(match.group(2))
        except ValueError:
            bootstrap_config = {}
        theme = bootstrap_config.get("theme") or config.FALLBACK_THEME
        log.debug("Vaadin oturumu kuruldu (appId=%s, theme=%s).", app_id, theme)
        return app_id, theme

    def _uidl(
        self, session: requests.Session, doc_url: str, app_id: str, theme: str
    ) -> dict:
        """UIDL POST istegini yapar ve cozulmus durum agacini dondurur."""
        page_url = f"{config.DYS_BASE_URL}/{doc_url.lstrip('/')}"
        stamp = int(time.time() * 1000)
        separator = "&" if "?" in page_url else "?"
        # Tarayicinin gonderdigi alanlarin aynisi; sunucu bunlari bekliyor.
        payload = [
            ("v-browserDetails", "1"),
            ("theme", theme),
            ("v-appId", app_id),
            ("v-sh", "1080"),
            ("v-sw", "1920"),
            ("v-cw", "1600"),
            ("v-ch", "900"),
            ("v-curdate", str(stamp)),
            ("v-tzo", "-180"),
            ("v-dstd", "0"),
            ("v-rtzo", "-180"),
            ("v-dston", "false"),
            ("v-tzid", "Europe/Istanbul"),
            ("v-vw", "1600"),
            ("v-vh", "900"),
            ("v-loc", page_url),
            ("v-wn", f"{app_id}-0.1"),
        ]
        response = self._request(
            session,
            "POST",
            f"{page_url}{separator}v-{stamp}",
            data=payload,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )

        content_type = (response.headers.get("Content-Type") or "").lower()
        if "json" not in content_type:
            raise TransientError(
                f"UIDL yaniti JSON degil ({content_type or 'tur yok'}); oturum dusmus olabilir.",
                session_fault=True,
            )
        try:
            envelope = response.json()
            return json.loads(envelope["uidl"])
        except (ValueError, KeyError, TypeError) as exc:
            raise TransientError(f"UIDL yaniti cozulemedi: {exc}", session_fault=True) from exc

    @staticmethod
    def _extract_stream_url(uidl: dict) -> str:
        """Durum agacindan gercek icerigin adresini bulur.

        ``LbsBrowserFrame`` bileseni tercih edilir; bulunamazsa ``http(s)`` semali
        herhangi bir ``source`` kaynagi kabul edilir. ``theme://`` semali kaynaklar
        (uyari ikonu gibi) icerik degildir ve elenir.
        """
        state = uidl.get("state") or {}
        if not isinstance(state, dict):
            raise PermanentError("UIDL icinde 'state' sozlugu yok.")

        if any("expired" in str(key).lower() for key in state) or any(
            "expired" in str((value or {}).get("id", "")).lower()
            for value in state.values()
            if isinstance(value, dict)
        ):
            raise ExpiredDocumentError(
                "Paylasim baglantisi gecersiz veya suresi dolmus (externaShareExpired)."
            )

        preferred: list[str] = []
        fallback: list[str] = []
        for value in state.values():
            if not isinstance(value, dict):
                continue
            resources = value.get("resources") or {}
            if not isinstance(resources, dict):
                continue
            for resource in resources.values():
                url = (resource or {}).get("uRL") if isinstance(resource, dict) else None
                if not isinstance(url, str) or not url.startswith(("http://", "https://")):
                    continue
                if str(value.get("id", "")).startswith("LbsBrowserFrame"):
                    preferred.append(url)
                else:
                    fallback.append(url)

        for candidate in (preferred, fallback):
            # Bicimi tutmayan adayları ele: uyari ikonu, tema varligi vb.
            valid = [url for url in candidate if _STREAM_URL_RE.match(url)]
            if valid:
                if len(valid) > 1:
                    log.debug("Birden fazla icerik adresi bulundu, ilki kullanildi: %s", valid)
                return valid[0]
            if candidate:
                log.debug("Beklenen bicime uymayan kaynaklar elendi: %s", candidate)

        raise PermanentError("UIDL icinde indirilebilir bir icerik adresi bulunamadi.")

    def _stream(self, session: requests.Session, stream_url: str) -> tuple[bytes, str]:
        """Asil dokuman govdesini indirir; boyut sinirini uygular."""
        response = self._request(session, "GET", stream_url, stream=True)
        chunks: list[bytes] = []
        total = 0
        for chunk in response.iter_content(chunk_size=65536):
            if self._stop.is_set():
                response.close()
                raise TransientError("Calisma kullanici tarafindan durduruldu.")
            if not chunk:
                continue
            total += len(chunk)
            if total > config.MAX_STREAM_BYTES:
                response.close()
                raise PermanentError(
                    f"Dokuman {config.MAX_STREAM_BYTES} bayt sinirini asti ({total} bayt)."
                )
            chunks.append(chunk)
        response.close()
        body = b"".join(chunks)
        return body, _resolve_encoding(response, body)

    # -- ortak istek sarmalayicisi -------------------------------------------------------

    def _request(self, session: requests.Session, method: str, url: str, **kwargs) -> requests.Response:
        """Tek bir HTTP istegi: hiz siniri uygular, durum kodunu siniflandirir."""
        if self._stop.is_set():
            raise TransientError("Calisma kullanici tarafindan durduruldu.")
        self._rate.acquire()
        kwargs.setdefault("timeout", (config.CONNECT_TIMEOUT, config.READ_TIMEOUT))
        try:
            response = session.request(method, url, **kwargs)
        except requests.exceptions.RequestException as exc:
            raise TransientError(f"Ag hatasi: {type(exc).__name__}: {exc}") from exc

        status = response.status_code
        if status in config.RETRYABLE_STATUS:
            if status in (429, 503):
                self._rate.penalise()
            raise TransientError(
                f"Sunucu {status} dondu ({url.split('?')[0]}).",
                retry_after=_parse_retry_after(response.headers.get("Retry-After")),
            )
        if status >= 400:
            raise PermanentError(f"Sunucu {status} dondu ({url.split('?')[0]}).")

        self._rate.relax()
        return response

    # -- disariya acilan tek yontem ------------------------------------------------------

    def fetch(self, doc_url: str) -> Document:
        """Bir dokumanin HTML metnini indirir; gecici hatalarda yeniden dener."""
        last_error: Exception | None = None

        for attempt in range(1, self._max_attempts + 1):
            if self._stop.is_set():
                raise TransientError("Calisma kullanici tarafindan durduruldu.")
            try:
                session, app_id, theme = self._ensure_session(doc_url)
                uidl = self._uidl(session, doc_url, app_id, theme)
                stream_url = self._extract_stream_url(uidl)
                body, encoding = self._stream(session, stream_url)
                text = body.decode(encoding, errors="replace")
                return Document(
                    doc_url=doc_url,
                    html=text,
                    encoding=encoding,
                    byte_length=len(body),
                    stream_url=stream_url,
                )
            except PermanentError:
                raise
            except TransientError as exc:
                last_error = exc
                if getattr(exc, "session_fault", False):
                    self.reset_session()
                if attempt >= self._max_attempts or self._stop.is_set():
                    break
                delay = exc.retry_after if exc.retry_after is not None else _backoff(attempt)
                log.warning(
                    "%s -> %d/%d deneme basarisiz (%s); %.1f sn sonra tekrar denenecek.",
                    _short(doc_url), attempt, self._max_attempts, exc, delay,
                )
                if self._stop.wait(delay):
                    raise TransientError("Calisma kullanici tarafindan durduruldu.") from exc

        raise TransientError(
            f"{self._max_attempts} denemenin tamami basarisiz oldu. Son hata: {last_error}"
        )

    def close(self) -> None:
        self.reset_session()


# --------------------------------------------------------------------------------------
# Yardimcilar
# --------------------------------------------------------------------------------------

def _backoff(attempt: int) -> float:
    """Ustel artan, rastgele saciniml bekleme suresi."""
    raw = min(config.BACKOFF_CAP, config.BACKOFF_BASE ** attempt)
    return raw * (0.5 + random.random() * 0.5)


def _parse_retry_after(value: str | None) -> float | None:
    """``Retry-After`` basligini saniyeye cevirir (yalnizca sayisal bicim)."""
    if not value:
        return None
    try:
        return max(0.0, min(config.BACKOFF_CAP, float(value.strip())))
    except ValueError:
        return None


def _resolve_encoding(response: requests.Response, body: bytes) -> str:
    """Karakter kumesini guvenilir sirayla belirler.

    ``requests`` bir ``text/*`` yanitinda charset yoksa ``ISO-8859-1`` varsayar; bu
    Turkce metni sessizce bozar. ``apparent_encoding`` ise ek bir kutuphaneye
    (chardet/charset_normalizer) baglidir ve kurulu olmayabilir. Bu yuzden sirayla:
    Content-Type basligindaki gercek charset, govdedeki ``<meta charset>``, sonra UTF-8.
    """
    content_type = response.headers.get("Content-Type") or ""
    if "charset=" in content_type.lower():
        charset = content_type.lower().split("charset=", 1)[1].split(";")[0].strip(" \"'")
        if charset:
            return charset

    match = _META_CHARSET_RE.search(body[:4096])
    if match:
        try:
            return match.group(1).decode("ascii")
        except UnicodeDecodeError:
            pass
    return "utf-8"


def _short(doc_url: str) -> str:
    """Gunluk ciktisinda okunabilir olmasi icin doc_url'i kisaltir."""
    match = re.search(r"cid=([0-9a-fA-F-]{8})", doc_url)
    return f"cid:{match.group(1)}" if match else doc_url[:40]
