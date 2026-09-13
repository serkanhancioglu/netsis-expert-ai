"""Ilerleme gostergesi ve calisma sonu raporu."""

from __future__ import annotations

import logging
import sys
import threading
import time
from dataclasses import dataclass, field
from pathlib import Path

log = logging.getLogger(__name__)


def human_bytes(count: float) -> str:
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if abs(count) < 1024.0 or unit == "TB":
            return f"{count:.1f} {unit}" if unit != "B" else f"{int(count)} B"
        count /= 1024.0
    return f"{count:.1f} TB"


def human_duration(seconds: float) -> str:
    seconds = int(max(0, seconds))
    hours, remainder = divmod(seconds, 3600)
    minutes, secs = divmod(remainder, 60)
    if hours:
        return f"{hours} sa {minutes} dk {secs} sn"
    if minutes:
        return f"{minutes} dk {secs} sn"
    return f"{secs} sn"


class Progress:
    """Ilerlemeyi hem terminalde hem de dosyaya yonlendirildiginde okunakli gosterir.

    Terminalde tek satir yerinde guncellenir; cikti bir dosyaya yonlendirildiginde
    (TTY degilse) belirli araliklarla tek satirlik ozet basilir; boylece gunluk
    dosyasi binlerce satirla sismez.
    """

    def __init__(self, total: int, *, stream=None, quiet: bool = False) -> None:
        self.total = max(0, total)
        self.stream = stream or sys.stderr
        self.quiet = quiet
        self.is_tty = bool(getattr(self.stream, "isatty", lambda: False)())
        self.started = time.monotonic()
        self._done = 0
        self._failed = 0
        self._skipped = 0
        self._last_emit = 0.0
        self._lock = threading.Lock()

    def advance(self, status: str, label: str = "") -> None:
        with self._lock:
            if status == "done":
                self._done += 1
            elif status == "failed":
                self._failed += 1
            else:
                self._skipped += 1
            processed = self._done + self._failed + self._skipped
            now = time.monotonic()
            should_emit = self.is_tty or (now - self._last_emit) >= 10.0 or processed == self.total
            if not should_emit or self.quiet:
                return
            self._last_emit = now
            elapsed = now - self.started
            rate = processed / elapsed if elapsed > 0 else 0.0
            remaining = (self.total - processed) / rate if rate > 0 else 0.0
            line = (
                f"[{processed}/{self.total}] "
                f"tamam:{self._done} hata:{self._failed} atlanan:{self._skipped} "
                f"| {rate:.2f} dok/sn | kalan ~{human_duration(remaining)}"
            )
            if self.is_tty:
                suffix = f" | {label[:48]}" if label else ""
                self.stream.write("\r\033[K" + line + suffix)
            else:
                self.stream.write(line + "\n")
            self.stream.flush()

    def finish(self) -> None:
        if self.is_tty and not self.quiet:
            self.stream.write("\n")
            self.stream.flush()


@dataclass(slots=True)
class RunReport:
    """Calisma sonunda ekrana ve dosyaya yazilan ozet."""

    output_dir: Path
    started_at: float
    finished_at: float = 0.0
    planned: int = 0
    counts: dict[str, int] = field(default_factory=dict)
    source_bytes: int = 0
    images_referenced: int = 0
    image_files: int = 0
    image_bytes: int = 0
    image_duplicates: int = 0
    tables_gfm: int = 0
    tables_html: int = 0
    internal_links: int = 0
    unresolved_links: int = 0
    pseudo_tags: dict[str, int] = field(default_factory=dict)
    failures: list[tuple[str, str, str]] = field(default_factory=list)

    def render(self) -> str:
        duration = self.finished_at - self.started_at
        done = self.counts.get("done", 0)
        failed = self.counts.get("failed", 0)
        pending = self.counts.get("pending", 0)
        skipped = self.counts.get("skipped", 0)

        lines = [
            "",
            "=" * 72,
            " NETSIS DOKUMAN INDIRME - CALISMA OZETI",
            "=" * 72,
            f"  Cikti klasoru      : {self.output_dir}",
            f"  Sure               : {human_duration(duration)}",
            f"  Planlanan dokuman  : {self.planned}",
            f"  Basarili           : {done}",
            f"  Hatali             : {failed}",
            f"  Bekleyen           : {pending}",
            f"  Atlanan            : {skipped}",
            f"  Indirilen ham HTML : {human_bytes(self.source_bytes)}",
            f"  Gorsel (referans)  : {self.images_referenced}",
            f"  Gorsel (dosya)     : {self.image_files} adet, {human_bytes(self.image_bytes)}",
            f"  Tekrar eden gorsel : {self.image_duplicates} (tek dosyaya baglandi)",
            f"  Tablo              : {self.tables_gfm} Markdown, {self.tables_html} HTML olarak birakildi",
            f"  Ic baglanti        : {self.internal_links} cozuldu, {self.unresolved_links} cozulemedi",
        ]
        if self.pseudo_tags:
            detail = ", ".join(f"<{k}> x{v}" for k, v in sorted(self.pseudo_tags.items()))
            lines.append(f"  Korunan sahte etiket: {detail}")

        if self.failures:
            lines.append("")
            lines.append(f"  HATALI DOKUMANLAR ({len(self.failures)}):")
            for breadcrumb, _doc_url, error in self.failures[:40]:
                lines.append(f"    - {breadcrumb}")
                lines.append(f"      {error[:160]}")
            if len(self.failures) > 40:
                lines.append(f"    ... ve {len(self.failures) - 40} tane daha")
            lines.append("")
            lines.append("  Yeniden denemek icin: --retry-failed secenegiyle tekrar calistirin.")

        lines.append("=" * 72)
        return "\n".join(lines)

    def write(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(self.render() + "\n", encoding="utf-8")
