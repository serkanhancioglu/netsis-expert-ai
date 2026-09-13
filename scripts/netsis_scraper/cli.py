"""Komut satiri arayuzu ve calisma akisi.

Akis:

1. Hiyerarsi agacini indir (ya da onbellekten oku) ve duzlestir.
2. Istege bagli CSV ile karsilastir, kapsama raporu ver.
3. Her dokuman icin cikti yolunu planla ve durum veritabanina yaz.
4. Is parcaciklariyla indir -> Markdown'a cevir -> atomik olarak diske yaz.
5. Ozet raporu bas.
"""

from __future__ import annotations

import argparse
import concurrent.futures as futures
import datetime as dt
import hashlib
import logging
import os
import signal
import sys
import threading
import time
from pathlib import Path

import requests

from netsis_scraper import __version__, catalog, config
from netsis_scraper.assets import AssetStore
from netsis_scraper.client import (
    DysClient,
    ExpiredDocumentError,
    FetchError,
    PermanentError,
    RateLimiter,
)
from netsis_scraper.convert import MarkdownConverter
from netsis_scraper.report import Progress, RunReport, human_bytes
from netsis_scraper.store import StateStore

log = logging.getLogger("netsis_scraper")


# --------------------------------------------------------------------------------------
# Argumanlar
# --------------------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="netsis-scraper",
        description=(
            "Logo Netsis 3 Enterprise dokumantasyonunu hiyerarsiyi koruyarak "
            "temiz Markdown dosyalarina cevirir."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ornekler:
  # Once 20 dokumanla dene
  python -m netsis_scraper --output ./netsis-docs --limit 20

  # Tamamini indir (kesilirse ayni komutla kaldigi yerden devam eder)
  python -m netsis_scraper --output ./netsis-docs

  # Yalnizca CSV'deki 1936 baglantiyi indir
  python -m netsis_scraper --output ./netsis-docs --csv Kitap1.csv --only-csv

  # Hatali kalanlari yeniden dene
  python -m netsis_scraper --output ./netsis-docs --retry-failed
""",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")

    group = parser.add_argument_group("Girdi ve cikti")
    group.add_argument(
        "-o", "--output", type=Path, default=Path("netsis-docs"),
        help="Markdown agacinin yazilacagi klasor (varsayilan: ./netsis-docs)",
    )
    group.add_argument(
        "--csv", type=Path, default=None,
        help="'Baslik;URL' bicimli baglanti listesi. Kapsama karsilastirmasi icin kullanilir.",
    )
    group.add_argument(
        "--only-csv", action="store_true",
        help="Yalnizca CSV'de gecen dokumanlari indir (varsayilan: agactaki her sey).",
    )
    group.add_argument(
        "--product", default=config.DEFAULT_PRODUCT,
        help=f"Portal urun kodu (varsayilan: {config.DEFAULT_PRODUCT})",
    )
    group.add_argument(
        "--skip-branches", action="store_true",
        help="Alt basligi olan ara dugumleri indirme, yalnizca yapraklari al.",
    )
    group.add_argument(
        "--number-prefix", action="store_true",
        help="Klasor/dosya adlarina siteki sirayi koruyan '001 ' on eki ekle.",
    )
    group.add_argument(
        "--keep-html", action="store_true",
        help="Ham HTML kopyalarini da '_html' klasorune kaydet.",
    )
    group.add_argument(
        "--promote-bold-headings", action="store_true",
        help=(
            "Kaynakta bolum basligi yerine kullanilan kalin paragraflari ('On Sorgulama', "
            "'Kisit', 'Siralama' gibi) '## ' basligina yukselt. Yalnizca belgede hic "
            "gercek h2-h6 basligi yoksa uygulanir. Arama/RAG icin gezinmeyi kolaylastirir "
            "ama kaynakta olmayan bir yapi uretir; bu yuzden varsayilan olarak kapalidir."
        ),
    )

    group = parser.add_argument_group("Gorseller")
    group.add_argument(
        "--images", choices=("files", "inline", "skip"), default="files",
        help=(
            "files: gorselleri _assets/ altina ayir (varsayilan, tekrar edenler tekillenir); "
            "inline: data: adresi olarak Markdown icinde birak (dosyalar cok buyur); "
            "skip: gorselleri hic yazma."
        ),
    )

    group = parser.add_argument_group("Ag davranisi (siteyi yormamak icin)")
    group.add_argument(
        "-j", "--concurrency", type=int, default=config.DEFAULT_CONCURRENCY,
        help=f"Es zamanli is parcacigi sayisi (varsayilan: {config.DEFAULT_CONCURRENCY})",
    )
    group.add_argument(
        "--min-interval", type=float, default=config.DEFAULT_MIN_INTERVAL,
        help=(
            "Iki istek arasindaki en kisa sure, saniye "
            f"(varsayilan: {config.DEFAULT_MIN_INTERVAL})"
        ),
    )
    group.add_argument(
        "--max-attempts", type=int, default=config.DEFAULT_MAX_ATTEMPTS,
        help=f"Dokuman basina en fazla deneme (varsayilan: {config.DEFAULT_MAX_ATTEMPTS})",
    )
    group.add_argument(
        "--offline-catalog", action="store_true",
        help="Agaci agdan degil, cikti klasorundeki onbellekten oku.",
    )

    group = parser.add_argument_group("Calisma kipi")
    group.add_argument("--limit", type=int, default=None, help="Yalnizca ilk N dokumani isle.")
    group.add_argument("--force", action="store_true", help="Tamamlanmis dokumanlari da yeniden indir.")
    group.add_argument("--retry-failed", action="store_true", help="Yalnizca hatali kalanlari yeniden dene.")
    group.add_argument("--dry-run", action="store_true", help="Hicbir sey indirme/yazma; yalnizca plani goster.")
    group.add_argument("--max-path-length", type=int, default=240,
                       help="Toplam yol uzunlugu ust siniri (Windows icin 240 onerilir).")
    group.add_argument("-v", "--verbose", action="store_true", help="Ayrintili gunluk.")
    group.add_argument("-q", "--quiet", action="store_true", help="Ilerleme cubugunu gizle.")
    return parser


# --------------------------------------------------------------------------------------
# On bilgi (YAML front matter)
# --------------------------------------------------------------------------------------

def _yaml_quote(value: str) -> str:
    """Metni her zaman cift tirnakli, kacisli YAML dizgisi olarak yazar."""
    escaped = (
        str(value)
        .replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("\n", "\\n")
        .replace("\r", "")
        .replace("\t", "\\t")
    )
    return f'"{escaped}"'


def build_front_matter(node: catalog.DocNode, *, product: str, fetched_at: str, source_bytes: int) -> str:
    """Dokumanin kimligini ve agactaki yerini tasiyan YAML on bilgisi uretir."""
    breadcrumb = list(node.breadcrumb)
    lines = [
        "---",
        f"title: {_yaml_quote(node.name)}",
        f"page_id: {_yaml_quote(node.page_id)}",
        f"product: {_yaml_quote(product)}",
        f"depth: {node.depth}",
        f"is_section: {'true' if node.is_branch else 'false'}",
        "breadcrumb:",
    ]
    lines.extend(f"  - {_yaml_quote(part)}" for part in breadcrumb)
    lines.extend(
        [
            f"breadcrumb_path: {_yaml_quote(' / '.join(breadcrumb))}",
            f"source_url: {_yaml_quote(catalog.portal_url(node.doc_url, product))}",
            f"doc_url: {_yaml_quote(node.doc_url)}",
            f"slug: {_yaml_quote(node.slug_name)}",
            f"source_version: {_yaml_quote(node.version)}",
            f"source_bytes: {source_bytes}",
            f"fetched_at: {_yaml_quote(fetched_at)}",
            f"generator: {_yaml_quote(f'netsis-scraper {__version__}')}",
            "---",
            "",
        ]
    )
    return "\n".join(lines)


# --------------------------------------------------------------------------------------
# Atomik dosya yazimi
# --------------------------------------------------------------------------------------

def write_atomic(path: Path, text: str) -> None:
    """Once gecici dosyaya, sonra ``os.replace`` ile hedefe yazar.

    Calisma yarida kesilirse hedefte ya eski ya yeni tam icerik bulunur; yarim
    dosya asla olusmaz. Bu, 'tamamlandi' isaretiyle diskteki gercegin ayrisma
    ihtimalini ortadan kaldirir.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.{threading.get_ident()}.tmp")
    try:
        with open(temporary, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


# --------------------------------------------------------------------------------------
# Calisma
# --------------------------------------------------------------------------------------

class Runner:
    """Planlanan dokumanlari indirir, cevirir ve diske yazar."""

    def __init__(self, settings: config.Settings, nodes: list[catalog.DocNode], quiet: bool) -> None:
        self.settings = settings
        self.nodes = nodes
        self.quiet = quiet
        self.stop_event = threading.Event()
        self.rate = RateLimiter(settings.min_interval)
        self.client = DysClient(
            self.rate, max_attempts=settings.max_attempts, stop_event=self.stop_event
        )
        self.store = StateStore(settings.state_path)
        self.assets = AssetStore(
            settings.assets_dir,
            enabled=(settings.image_mode == "files"),
            dry_run=settings.dry_run,
        )
        # doc_url -> cikti agacindaki goreli .md yolu
        self.path_map = {node.doc_url: node.relative_path for node in nodes}
        self.report = RunReport(output_dir=settings.output_dir, started_at=time.time())
        self._lock = threading.Lock()

    # -- ic baglanti cozucusu -------------------------------------------------------------

    def _resolver_for(self, node: catalog.DocNode):
        """Bu dokumanin konumuna gore goreli baglanti ureten cozucu dondurur."""
        here = (self.settings.output_dir / node.relative_path).parent

        def resolve(href: str) -> str | None:
            doc_url = catalog.doc_url_from_link(href)
            if not doc_url:
                return None
            target = self.path_map.get(doc_url)
            if target is None:
                return None
            relative = os.path.relpath(self.settings.output_dir / target, here)
            return relative.replace(os.sep, "/")

        return resolve

    # -- tek dokuman ----------------------------------------------------------------------

    def process(self, node: catalog.DocNode) -> tuple[str, str]:
        """Bir dokumani isler; ``(durum, etiket)`` dondurur."""
        label = " / ".join(node.breadcrumb[1:]) or node.name
        if self.stop_event.is_set():
            return "skipped", label

        try:
            document = self.client.fetch(node.doc_url)
        except ExpiredDocumentError as exc:
            self.store.mark(node.doc_url, "failed", error=f"Baglanti gecersiz: {exc}")
            log.error("GECERSIZ BAGLANTI: %s", label)
            return "failed", label
        except FetchError as exc:
            self.store.mark(node.doc_url, "failed", error=str(exc))
            log.error("BASARISIZ: %s -> %s", label, exc)
            return "failed", label

        converter = MarkdownConverter(
            asset_store=self.assets,
            link_resolver=self._resolver_for(node),
            image_mode=self.settings.image_mode,
            assets_href_prefix=self._assets_prefix(node),
            promote_bold_headings=self.settings.promote_bold_headings,
        )
        try:
            converted = converter.convert(document.html)
        except Exception as exc:  # donusturucu hatasi bir dokumani gomsun, calismayi degil
            self.store.mark(node.doc_url, "failed", error=f"Donusum hatasi: {exc!r}")
            log.exception("DONUSUM HATASI: %s", label)
            return "failed", label

        fetched_at = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
        text = (
            build_front_matter(
                node,
                product=self.settings.product,
                fetched_at=fetched_at,
                source_bytes=document.byte_length,
            )
            + (converted.markdown or f"# {node.name}\n\n*Bu bolumun kendi metni yok.*")
            + "\n"
        )
        digest = hashlib.sha256(text.encode("utf-8")).hexdigest()

        if not self.settings.dry_run:
            write_atomic(self.settings.output_dir / node.relative_path, text)
            if self.settings.keep_html:
                html_path = (
                    self.settings.output_dir / "_html" / node.relative_path
                ).with_suffix(".html")
                write_atomic(html_path, document.html)

        self.store.mark(
            node.doc_url,
            "done",
            source_bytes=document.byte_length,
            markdown_hash=digest,
            images=converted.images,
        )
        with self._lock:
            self.report.source_bytes += document.byte_length
            self.report.images_referenced += converted.images
            self.report.tables_gfm += converted.tables_gfm
            self.report.tables_html += converted.tables_html
            self.report.embeds += converted.embeds
            self.report.promoted_headings += converted.promoted_headings
            self.report.internal_links += converted.internal_links
            self.report.unresolved_links += converted.unresolved_links
            for name, count in converted.pseudo_tags.items():
                self.report.pseudo_tags[name] = self.report.pseudo_tags.get(name, 0) + count
        return "done", label

    def _assets_prefix(self, node: catalog.DocNode) -> str:
        """Gorsel klasorunun, bu dokumanin bulundugu yere gore goreli adresi."""
        here = (self.settings.output_dir / node.relative_path).parent
        relative = os.path.relpath(self.settings.assets_dir, here)
        return relative.replace(os.sep, "/") + "/"

    # -- tum calisma ------------------------------------------------------------------------

    def run(self, todo: list[catalog.DocNode]) -> RunReport:
        progress = Progress(len(todo), quiet=self.quiet)
        self.assets.adopt_existing()

        if self.settings.dry_run:
            log.info("KURU CALISMA: %d dokuman islenecekti, hicbir istek yapilmadi.", len(todo))
            for node in todo[:20]:
                log.info("  %s", node.relative_path)
            if len(todo) > 20:
                log.info("  ... ve %d tane daha", len(todo) - 20)
            self.report.planned = len(todo)
            self.report.counts = self.store.counts()
            self.report.finished_at = time.time()
            return self.report

        workers = max(1, self.settings.concurrency)
        with futures.ThreadPoolExecutor(max_workers=workers, thread_name_prefix="fetch") as pool:
            pending = {pool.submit(self.process, node): node for node in todo}
            try:
                for future in futures.as_completed(pending):
                    try:
                        status, label = future.result()
                    except Exception as exc:  # beklenmedik hata calismayi durdurmasin
                        node = pending[future]
                        log.exception("Beklenmedik hata: %s", node.name)
                        self.store.mark(node.doc_url, "failed", error=repr(exc))
                        status, label = "failed", node.name
                    progress.advance(status, label)
            except KeyboardInterrupt:
                self.stop_event.set()
                log.warning("Durduruluyor... calisan istekler tamamlaniyor.")
                for future in pending:
                    future.cancel()
                raise
            finally:
                progress.finish()

        self.assets.write_manifest()
        self.report.planned = len(todo)
        self.report.counts = self.store.counts()
        self.report.image_files = self.assets.files_written
        self.report.image_bytes = self.assets.bytes_written
        self.report.image_duplicates = self.assets.duplicates_skipped
        self.report.failures = [
            (row["breadcrumb"] or row["title"] or row["doc_url"], row["doc_url"], row["last_error"] or "")
            for row in self.store.failures(500)
        ]
        self.report.finished_at = time.time()
        return self.report

    def close(self) -> None:
        self.client.close()
        self.store.close()


# --------------------------------------------------------------------------------------
# Giris noktasi
# --------------------------------------------------------------------------------------

def _configure_logging(verbose: bool) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s %(levelname)-7s %(message)s",
        datefmt="%H:%M:%S",
        stream=sys.stderr,
    )
    logging.getLogger("urllib3").setLevel(logging.WARNING)


def _install_signal_handlers(stop_event: threading.Event) -> None:
    def handler(signum, _frame):
        if stop_event.is_set():
            log.warning("Ikinci kesme sinyali alindi, hemen cikiliyor.")
            raise SystemExit(130)
        stop_event.set()
        log.warning(
            "Sinyal %s alindi. Devam eden istekler bitince temiz sekilde durulacak; "
            "ayni komutu tekrar calistirdiginizda kaldigi yerden devam eder.",
            signum,
        )

    for sig in (signal.SIGINT, signal.SIGTERM):
        try:
            signal.signal(sig, handler)
        except (ValueError, OSError, AttributeError):
            pass  # ana is parcacigi degilse ya da platform desteklemiyorsa gec


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    _configure_logging(args.verbose)

    settings = config.Settings(
        output_dir=args.output.expanduser().resolve(),
        product=args.product,
        concurrency=args.concurrency,
        min_interval=args.min_interval,
        max_attempts=args.max_attempts,
        image_mode=args.images,
        include_branches=not args.skip_branches,
        number_prefix=args.number_prefix,
        max_path_length=args.max_path_length,
        force=args.force,
        retry_failed=args.retry_failed,
        limit=args.limit,
        dry_run=args.dry_run,
        keep_html=args.keep_html,
        offline_catalog=args.offline_catalog,
        verbose=args.verbose,
    )
    settings.output_dir.mkdir(parents=True, exist_ok=True)

    # 1) Hiyerarsi agaci
    session = requests.Session()
    session.headers["User-Agent"] = config.USER_AGENT
    try:
        if settings.offline_catalog:
            if not settings.catalog_cache_path.exists():
                log.error("Onbellek bulunamadi: %s", settings.catalog_cache_path)
                return 2
            root = catalog.load_cached_catalog(settings.catalog_cache_path)
            log.info("Hiyerarsi onbellekten okundu.")
        else:
            root = catalog.fetch_catalog(session, settings.product)
            catalog.save_catalog_cache(settings.catalog_cache_path, root)
    except Exception as exc:
        log.error("Hiyerarsi agaci alinamadi: %s", exc)
        if settings.catalog_cache_path.exists():
            log.warning("Onbellekteki agac kullaniliyor: %s", settings.catalog_cache_path)
            root = catalog.load_cached_catalog(settings.catalog_cache_path)
        else:
            return 2
    finally:
        session.close()

    nodes = catalog.flatten(root)
    log.info(
        "Agac cozuldu: %d dugum (%d bolum, %d yaprak).",
        len(nodes),
        sum(1 for n in nodes if n.is_branch),
        sum(1 for n in nodes if not n.is_branch),
    )

    # 2) CSV karsilastirmasi
    if args.csv:
        rows = catalog.read_link_csv(args.csv)
        wanted = catalog.csv_doc_urls(rows)
        summary = catalog.annotate_csv_membership(nodes, wanted)
        log.info(
            "CSV kapsamasi: %d satirin %d tanesi agacta bulundu; "
            "agacta olup CSV'de olmayan %d dugum var.",
            summary["csv_rows"], summary["matched"], summary["tree_only"],
        )
        if summary["csv_only"]:
            log.warning("CSV'de olup agacta bulunmayan %d dokuman var.", summary["csv_only"])
    elif args.only_csv:
        log.error("--only-csv kullanmak icin --csv ile bir dosya vermelisiniz.")
        return 2

    # 3) Yol planlama
    catalog.plan_paths(
        nodes,
        number_prefix=settings.number_prefix,
        max_path_length=settings.max_path_length,
        output_dir_length=len(str(settings.output_dir)),
    )
    selected = catalog.select_nodes(
        nodes, include_branches=settings.include_branches, csv_filter=args.only_csv
    )
    log.info("%d dokuman planlandi.", len(selected))

    runner = Runner(settings, selected, quiet=args.quiet)
    _install_signal_handlers(runner.stop_event)
    exit_code = 0
    try:
        runner.store.upsert_pending(
            [
                {
                    "doc_url": node.doc_url,
                    "page_id": node.page_id,
                    "title": node.name,
                    "breadcrumb": " / ".join(node.breadcrumb[1:]),
                    "relative_path": str(node.relative_path),
                }
                for node in selected
            ]
        )
        if settings.force:
            log.info("--force: %d kayit yeniden indirilecek.", runner.store.reset_all())
        elif settings.retry_failed:
            log.info("--retry-failed: %d hatali kayit yeniden denenecek.", runner.store.reset_failed())

        completed = set() if settings.force else runner.store.completed_urls()
        todo = [node for node in selected if node.doc_url not in completed]
        if settings.retry_failed and not settings.force:
            todo = [
                node for node in todo
                if runner.store.status_of(node.doc_url) in (None, "pending")
            ]
        if settings.limit is not None:
            todo = todo[: max(0, settings.limit)]

        if completed:
            log.info("%d dokuman onceki calismadan tamamlanmis, atlaniyor.", len(completed))
        if not todo:
            log.info("Yapilacak yeni is yok. Her sey guncel.")

        report = runner.run(todo)
        report.planned = len(todo)
        print(report.render())
        report.write(settings.output_dir / "_rapor.txt")

        failed = report.counts.get("failed", 0)
        if failed:
            log.warning(
                "%d dokuman indirilemedi. '%s --retry-failed' ile yeniden deneyebilirsiniz.",
                failed, "python -m netsis_scraper --output " + str(settings.output_dir),
            )
            exit_code = 1
    except KeyboardInterrupt:
        log.warning("Durduruldu. Ilerleme kaydedildi; ayni komutla devam edebilirsiniz.")
        exit_code = 130
    finally:
        runner.close()

    if not settings.dry_run and exit_code in (0, 1):
        log.info(
            "Cikti: %s (%s)",
            settings.output_dir,
            human_bytes(sum(f.stat().st_size for f in settings.output_dir.rglob("*") if f.is_file())),
        )
    return exit_code
