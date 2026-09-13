# Netsis Doküman İndirici

Logo Netsis 3 Enterprise dokümantasyonundaki **2.328 sayfayı** (elinizdeki CSV'deki
1.936 doküman + 392 ara bölüm) hiyerarşiyi bozmadan temiz Markdown'a çevirir.

## En hızlı yol

**Windows:** `calistir.bat` dosyasına çift tıklayın.
**macOS / Linux:** `./calistir.sh`

Bu betikler sanal ortamı kurar, bağımlılıkları yükler ve indirmeyi başlatır.
İlk denemeyi küçük tutmak için: `calistir.bat --limit 20`

## Elle çalıştırma

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python -m netsis_scraper --output ./netsis-docs --limit 20   # deneme
python -m netsis_scraper --output ./netsis-docs              # tamamı
```

Çalışma yarıda kesilirse **aynı komutu tekrar çalıştırın** — kaldığı yerden devam eder.

Tam kılavuz: [`../docs/SCRAPER.md`](../docs/SCRAPER.md)

## Dosya düzeni

| Yol | Ne işe yarar |
|---|---|
| `calistir.sh` / `calistir.bat` | Tek tıkla kurulum + çalıştırma |
| `requirements.txt` | `requests`, `beautifulsoup4`, `lxml` |
| `netsis_scraper/config.py` | Adresler, zaman aşımları, varsayılanlar |
| `netsis_scraper/catalog.py` | Hiyerarşi ağacı, CSV eşleştirme, yol planlama |
| `netsis_scraper/client.py` | Vaadin/DYS HTTP istemcisi, hız sınırı, yeniden deneme |
| `netsis_scraper/convert.py` | HTML → Markdown dönüşümü |
| `netsis_scraper/assets.py` | Gömülü görsellerin ayrılması ve tekilleştirilmesi |
| `netsis_scraper/paths.py` | Platformlar arası güvenli dosya adları |
| `netsis_scraper/store.py` | SQLite durum kaydı (kaldığı yerden devam) |
| `netsis_scraper/report.py` | İlerleme göstergesi ve özet rapor |
| `netsis_scraper/cli.py` | Komut satırı ve çalışma akışı |
| `tests/` | 28 birim testi |
| `arastirma/` | Protokolün nasıl çözüldüğünü gösteren keşif betikleri |

## Testler

```bash
pip install pytest
python -m pytest tests -q
```

## Ölçülmüş çalışma verileri

14 dokümanlık canlı testte (3 eşzamanlı işçi):

```
Süre               : 12 sn        ->  1.15 doküman/sn
Başarılı           : 14 / 14
İndirilen ham HTML : 8.3 MB
Görsel             : 67 referans, 66 dosya (6.2 MB), 1 tekrar tekilleştirildi
Tablo              : 6 Markdown
İç bağlantı        : 18 çözüldü, 0 çözülemedi
Korunan <tab>      : 4
```

Ayrıca 64 dokümanlık örneklem üzerinde çevrimdışı dönüşüm doğrulaması:

```
843 görsel  ·  140 Markdown tablosu + 1 HTML tablosu (iç içe)
72 bilgi kutusu  ·  10 YouTube gömülüsü  ·  112 korunan <tab>  ·  13 altı çizili
başlıklar: h1×71  h2×16  h3×21  h4×2  h5×6
bozuk Markdown üretimi: 0 (`*"*` yok, `## **x**` yok)
```

Bu sayıların tamamı, kaynağı bağımsız olarak yeniden ölçen çok ajanlı bir
inceleme ile karşılaştırıldı ve birebir örtüştü.

`--promote-bold-headings` açıkken 30 dokümanda 152 başlık yükseltilir.

Bu hıza göre 2.328 dokümanın tamamı yaklaşık **35 dakika** sürer.

Boyut tahmini (64 dokümanlık örneklemden doğrusal ölçekleme):

| Ne | Tahmin |
|---|---|
| İndirilecek ham HTML (ağ trafiği) | ~640 MB |
| Diskteki Markdown metni | ~28 MB |
| Diskteki görseller (üst sınır) | ≤ 370 MB |

Görsel rakamı üst sınırdır; aynı ikonlar dokümanlar arasında paylaşıldığından
gerçek toplam bunun altında kalır. Görsel istemiyorsanız `--images skip` ile
yalnızca ~28 MB metin indirirsiniz.
