# Logo Netsis 3 Enterprise Teknik Bilgi Tabanı

Resmi Logo Netsis 3 Enterprise dokümantasyonundan çıkarılan Markdown makaleler.
AI asistanı için RAG kaynağı olarak kullanılır.

## Bu klasör elle doldurulmaz

İçeriğin tamamı `scripts/netsis_scraper` tarafından üretilir:

```bash
cd scripts
pip install -r requirements.txt
python -m netsis_scraper --output ../knowledge-base/markdown
```

Çıktı klasörü `markdown` adını taşıdığında indeks (`metadata/articles-manifest.csv`)
kendiliğinden yazılır. Çalışma yarıda kesilirse aynı komut kaldığı yerden devam eder.
Aylık güncelleme için `--refresh` kullanın: her şeyi yeniden indirir ama diskte
yalnızca içeriği gerçekten değişmiş dosyaları yeniler, böylece `git diff` size tam
olarak Logo'nun neyi değiştirdiğini gösterir.

## Kaç doküman var?

| | Adet |
|---|---|
| Yaprak makaleler | **1.936** |
| Bölüm (ara başlık) sayfaları | **392** |
| **Toplam** | **2.328** |

Bölüm sayfaları klasör görevi görür ama **kendi içerikleri de olabilir**. Örneklenen
6 bölüm sayfasının 2'sinde gerçek içerik çıktı (biri 30.000 karakter). Bu yüzden
yalnızca 1.936 yaprağı indirmek içerik kaybettirir; script 2.328'inin tamamını alır.

## Klasörler

### `markdown/`
Bilgi tabanının ana içeriği. Kaynaktaki **hiyerarşi klasör yapısı olarak korunur**;
alt başlığı olan bir düğümün kendi metni o klasörün içine `index.md` olarak yazılır.

```
markdown/
├── index.md
├── Kullanıcı Dokümanları/
│   ├── index.md
│   └── Genel/
│       └── Döviz Takibi/
│           ├── index.md
│           └── Döviz İsimleri Tanımlama.md
├── Destek Dokümanları/…
├── Sürüm Dokümanları/…
└── _assets/            # gömülü görseller, içerik özetiyle adlandırılmış
```

Her dosya bir YAML ön bilgi bloğuyla başlar: başlık, kırıntı yolu, kaynak URL,
`doc_url`, sürüm damgası ve `is_stub` (kendi metni olmayan bölüm sayfası mı).

### `metadata/`
- `articles-manifest.schema.json` — indeks alan sözleşmesi.
- `articles-manifest.csv` — script tarafından üretilir (2.328 satır).

Şemadaki alanların çoğu klasik metadata (`title`, `module`, `source_url`,
`last_updated`). RAG için özellikle şunlar var:

| Alan | Ne işe yarar |
|---|---|
| `breadcrumb` | Parçaya bağlam enjeksiyonu — makale hangi modülün neresinden geliyor |
| `depth` | Üst seviye makaleler genel, alt seviyeler özel; sıralamada ağırlık |
| `is_section` | Bölüm sayfalarını indekslemede ayırt etmek için |
| `doc_cid` | Kaynak sistemdeki kalıcı kimlik. `page_id` 2.328 düğümün 112'sinde **boş**, o yüzden anahtar olarak kullanılamaz |
| `content_sha256` | Özet değişmediyse embedding hâlâ geçerli — neyin yeniden gömüleceğini bulmak için |

### `rag/chunks/` ve `rag/embeddings/`
Pipeline çıktıları için ayrılmış; `.gitignore` ile depo dışında tutulur.

## Kaynak hakkında bilinmesi gerekenler

Portal bir Angular SPA; asıl metin `<iframe>` içindeki Vaadin 8 uygulamasından
geliyor, yani sayfanın HTML'ini indirmek yetmiyor. Protokolün nasıl çözüldüğü ve
dönüşümde hangi tuzakların (kaybolan `<tab>` metinleri, yalan söyleyen görsel
MIME'ları, NBSP ile hizalanmış bilanço tabloları) ele alındığı
[`../docs/SCRAPER.md`](../docs/SCRAPER.md) içinde ayrıntılı anlatılıyor.
