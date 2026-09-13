"""Agac dugumu adlarini her isletim sisteminde guvenli dosya yollarina cevirir.

Kaynak basliklar Turkce ve serbest metindir: ``Raporlar/MRP``, ``Ek-1 (Yurt Ici)``,
``9.0.43.1 - Ekim 2022`` gibi. Windows'ta yasak karakterler, ayrilmis adlar, sondaki
nokta/bosluk ve 260 karakterlik MAX_PATH siniri; macOS/Windows'ta ise buyuk-kucuk harf
duyarsizligindan kaynaklanan cakismalar burada ele alinir.
"""

from __future__ import annotations

import hashlib
import re
import unicodedata

#: Windows'ta dosya adinda kullanilamayan karakterler.
_ILLEGAL_CHARS = re.compile(r'[<>:"/\\|?*\x00-\x1f\x7f]')

#: Windows'ta ayrilmis aygit adlari (uzantidan bagimsiz olarak yasaktir).
_RESERVED_NAMES = frozenset(
    {"CON", "PRN", "AUX", "NUL"}
    | {f"COM{i}" for i in range(1, 10)}
    | {f"LPT{i}" for i in range(1, 10)}
)

#: Gorsel olarak yasak karakterlerin okunakli karsiliklari.
_REPLACEMENTS = {
    "/": "-",
    "\\": "-",
    ":": " -",
    "*": "+",
    "?": "",
    '"': "'",
    "<": "(",
    ">": ")",
    "|": "-",
}

_WHITESPACE = re.compile(r"\s+")

#: Tek bir yol parcasinin en fazla kac karakter olabilecegi.
MAX_SEGMENT_LENGTH = 80


def sanitize_segment(name: str, max_length: int = MAX_SEGMENT_LENGTH) -> str:
    """Tek bir baslik metnini guvenli bir klasor/dosya adina cevirir.

    Bilgi kaybini en aza indirmek icin yasak karakterler silinmek yerine okunabilir
    esdeglerine cevrilir (``Raporlar/MRP`` -> ``Raporlar-MRP``).
    """
    if not name:
        return "adsiz"

    # Unicode'u normalize et: gorsel olarak ayni olan farkli kod dizileri tek bicime gelsin.
    text = unicodedata.normalize("NFC", str(name))

    # Yumusak tire, sifir genislikli bosluk gibi gorunmez karakterleri temizle.
    text = "".join(ch for ch in text if unicodedata.category(ch) != "Cf")

    for bad, good in _REPLACEMENTS.items():
        text = text.replace(bad, good)

    # Geriye kalan kontrol karakterlerini at.
    text = _ILLEGAL_CHARS.sub("", text)

    # Bosluklari tekille, bas/sondaki bosluk ve noktalari kirp.
    text = _WHITESPACE.sub(" ", text).strip().strip(". ")

    # Tamami noktalama isaretinden olusan bir ad (ornegin "///" -> "---") anlam
    # tasimaz ve bazi araclarda secenek gibi gorunur; yer tutucuya cevir.
    if not text or all(unicodedata.category(ch).startswith("P") for ch in text):
        return "adsiz"

    # Windows ayrilmis adlarini bozmadan isaretle.
    if text.upper() in _RESERVED_NAMES or text.upper().split(".")[0] in _RESERVED_NAMES:
        text = f"_{text}"

    if len(text) > max_length:
        # Kesme sonucu iki farkli baslik ayni ada dusmesin diye kisa bir ozet ekle.
        digest = hashlib.sha1(text.encode("utf-8")).hexdigest()[:6]
        text = f"{text[: max_length - 7].rstrip(' .-')}~{digest}"

    return text


class SegmentAllocator:
    """Ayni ust klasor icinde benzersiz alt ad uretir.

    Windows ve macOS dosya sistemleri buyuk-kucuk harf duyarsizdir; bu yuzden
    benzersizlik kontrolu kucuk harfe indirgenmis ad uzerinden yapilir.
    """

    def __init__(self) -> None:
        self._taken: dict[tuple[str, ...], set[str]] = {}

    def allocate(self, parent: tuple[str, ...], desired: str) -> str:
        used = self._taken.setdefault(parent, set())
        candidate = desired
        suffix = 2
        while candidate.casefold() in used:
            tail = f" ({suffix})"
            head = desired
            if len(head) + len(tail) > MAX_SEGMENT_LENGTH:
                head = head[: MAX_SEGMENT_LENGTH - len(tail)].rstrip(" .-")
            candidate = f"{head}{tail}"
            suffix += 1
        used.add(candidate.casefold())
        return candidate


def shorten_relative_path(parts: list[str], budget: int) -> list[str]:
    """Toplam yol uzunlugu ``budget`` karakteri asiyorsa parcalari kisaltir.

    Once her parcaya uygulanabilecek en buyuk ortak ust sinir ikili arama ile bulunur,
    sonra bu siniri asan her parca kisaltilir. Kisaltilan her parcaya, iki farkli
    basligin ayni ada dusmemesi icin kisa bir sha1 ozeti eklenir. Boylece derin
    agaclarda bile Windows MAX_PATH sinirinin altinda kalinir.
    """
    parts = list(parts)
    if not parts:
        return parts

    separators = max(0, len(parts) - 1)

    def total(ps: list[str]) -> int:
        return sum(len(x) for x in ps) + separators

    if total(parts) <= budget:
        return parts

    def truncate(segment: str, cap: int) -> str:
        if len(segment) <= cap:
            return segment
        digest = hashlib.sha1(segment.encode("utf-8")).hexdigest()[:6]
        keep = max(1, cap - 7)
        return f"{segment[:keep].rstrip(' .-')}~{digest}"

    #: Kisaltilan bir parca "~abc123" ekiyle birlikte en az bu kadar yer kaplar.
    min_cap = 8
    low, high = min_cap, max(len(x) for x in parts)
    best: list[str] | None = None
    while low <= high:
        cap = (low + high) // 2
        candidate = [truncate(x, cap) for x in parts]
        if total(candidate) <= budget:
            best = candidate
            low = cap + 1
        else:
            high = cap - 1

    if best is None:
        # Butce cok dar: her parcayi en kucuk anlamli boyuta indir ve oyle birak.
        best = [truncate(x, min_cap) for x in parts]
    return best
