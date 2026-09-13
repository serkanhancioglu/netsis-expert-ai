# netsis-expert-ai

Logo Netsis 3 Enterprise resmi dokümantasyonunu referans alarak teknik destek
sağlayan, hata çözümlerini ve kullanım detaylarını sunan mühendislik asistanı.

## Depo yapısı

| Yol | İçerik |
|---|---|
| `scripts/` | Dokümantasyonu kaynağından çekip temiz Markdown'a çeviren araç |
| `knowledge-base/markdown/` | Üretilen Markdown makaleler (hiyerarşi klasör yapısı olarak korunur) |
| `knowledge-base/metadata/` | Makale indeksi ve alan sözleşmesi |
| `knowledge-base/rag/` | Chunk ve embedding çıktıları (depo dışı) |
| `docs/SCRAPER.md` | Kazıma aracının tam kullanım kılavuzu |

## Bilgi tabanını oluşturma

```bash
cd scripts
pip install -r requirements.txt
python -m netsis_scraper --output ../knowledge-base/markdown
```

Windows'ta `scripts\calistir.bat`, macOS/Linux'ta `scripts/calistir.sh` aynı işi
sanal ortam kurarak yapar. Yaklaşık 35 dakika sürer; yarıda kesilirse aynı komutla
kaldığı yerden devam eder.

**2.328 doküman** indirilir: 1.936 yaprak makale + 392 bölüm sayfası. Bölüm
sayfaları da içerik taşıyabildiği için atlanmaz.

Ayrıntılar: [`docs/SCRAPER.md`](docs/SCRAPER.md) ve
[`knowledge-base/README.md`](knowledge-base/README.md).
