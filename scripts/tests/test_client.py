"""Ag katmani: hiz siniri, akis adresi secimi ve karakter kumesi cozumleme."""

import sys
import threading
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pytest  # noqa: E402

from netsis_scraper.client import (  # noqa: E402
    DysClient,
    ExpiredDocumentError,
    PermanentError,
    RateLimiter,
    _resolve_encoding,
)

STREAM = "https://dys.logo.cloud/stream/?tCid=06083527-dd12-4e19-95fd-ea1c4ae653a9"


# -- hiz sinirlayici ------------------------------------------------------------------

def test_rate_limiter_spaces_requests_and_never_starves():
    """Kilit icinde donen bir dongu slotu her turda iteleyip havuzu ac birakirdi."""
    limiter = RateLimiter(0.05)
    stamps: list[float] = []
    lock = threading.Lock()

    def worker():
        for _ in range(5):
            limiter.acquire()
            with lock:
                stamps.append(time.monotonic())

    threads = [threading.Thread(target=worker) for _ in range(4)]
    started = time.monotonic()
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    elapsed = time.monotonic() - started

    assert len(stamps) == 20
    assert 0.8 < elapsed < 3.0, f"20 istek {elapsed:.2f} sn surdu, ~0.95 sn beklenirdi"
    stamps.sort()
    gaps = [b - a for a, b in zip(stamps, stamps[1:])]
    assert min(gaps) >= 0.04


def test_penalise_and_relax_move_the_interval():
    limiter = RateLimiter(0.01)
    limiter.penalise()
    assert limiter._interval > 0.01
    for _ in range(100):
        limiter.relax()
    assert limiter._interval == pytest.approx(0.01, rel=0.2)


# -- akis adresi secimi ---------------------------------------------------------------

def test_prefers_browser_frame_resource():
    uidl = {
        "state": {
            "4": {"id": "LbsBrowserFrame_4", "resources": {"source": {"uRL": STREAM}}},
            "5": {"id": "DmsImage_5", "resources": {"source": {"uRL": "theme://images/x.svg"}}},
        }
    }
    assert DysClient._extract_stream_url(uidl) == STREAM


def test_expired_share_link_is_permanent_not_retried():
    """Gecersiz baglantida UIDL bir uyari ikonu dondurur; bu kalici bir hatadir."""
    uidl = {
        "state": {
            "11": {
                "id": "DmsImage_11",
                "resources": {"source": {"uRL": "theme://images/task_list_warning.svg"}},
            },
            "externaShareExpired": {"id": "externaShareExpired"},
        }
    }
    with pytest.raises(ExpiredDocumentError):
        DysClient._extract_stream_url(uidl)


def test_non_stream_resource_is_rejected():
    """Bicim kisiti olmadan geri donus dali yanlislikla bir varlik indirebilir."""
    uidl = {"state": {"9": {"id": "Foo_9", "resources": {"source": {"uRL": "https://evil.example/x.png"}}}}}
    with pytest.raises(PermanentError):
        DysClient._extract_stream_url(uidl)


def test_missing_resource_is_permanent():
    with pytest.raises(PermanentError):
        DysClient._extract_stream_url({"state": {"1": {"id": "Panel_1"}}})


# -- karakter kumesi ---------------------------------------------------------------------

class _FakeResponse:
    def __init__(self, headers):
        self.headers = headers


def test_charset_comes_from_header_when_present():
    r = _FakeResponse({"Content-Type": "text/html;charset=utf-8"})
    assert _resolve_encoding(r, b"<html>") == "utf-8"


def test_charset_falls_back_to_meta_then_utf8():
    """requests, charset'siz text/* yanitinda ISO-8859-1 varsayar ve Turkceyi bozar."""
    r = _FakeResponse({"Content-Type": "text/html"})
    body = b'<html><head><meta http-equiv="Content-Type" content="text/html; charset=windows-1254">'
    assert _resolve_encoding(r, body) == "windows-1254"
    assert _resolve_encoding(r, b"<html><head><title>x</title>") == "utf-8"
