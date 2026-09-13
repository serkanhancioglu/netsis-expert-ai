# Netsis Doküman İndirici — Kullanım Kılavuzu

`scripts/netsis_scraper`, Logo Netsis 3 Enterprise dokümantasyonundaki **2.328 sayfayı**
(bunların 1.936'sı elinizdeki CSV'deki yaprak dokümanlar) hiyerarşiyi bozmadan temiz
Markdown dosyalarına çevirir.

---

## 1. Kurulum

Python 3.10 veya üzeri gerekir.

```bash
cd scripts
python -m venv .venv

# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

---

## 2. Hızlı başlangıç

```bash
# Önce 20 dokümanla deneyin (~1 dakika)
python -m netsis_scraper --output ./netsis-docs --limit 20

# Sonuç iyiyse tamamını indirin
python -m netsis_scraper --output ./netsis-docs
```

Çalışma yarıda kesilirse (Ctrl-C, internet kopması, bilgisayar kapanması) **aynı komutu
tekrar çalıştırın** — kaldığı yerden devam eder, indirilmiş dokümanları tekrar indirmez.

---

## 3. Nasıl çalışıyor?

Portal (`polaris.logo.cloud`) bir Angular uygulamasıdır; asıl doküman metni bir
`<iframe>` içindeki **Vaadin 8** uygulamasından gelir. Bu yüzden sayfanın HTML'ini
indirmek yetmez. Script, tarayıcının yaptığı adımların aynısını yapar — ama tarayıcı
çalıştırmadan, sadece HTTP ile:

| Adım | İstek | Ne döner |
|---|---|---|
| 1. Ağaç | `GET polaris.logo.com.tr/api/Documents/GetAuthorizedTrees?product=netsis-3-enterprise` | Tüm hiyerarşi (2.328 düğüm) tek seferde |
| 2. Önyükleme | `GET dys.logo.cloud/external?cid=…` | Vaadin uygulama kimliği + oturum çerezi |
| 3. UIDL | `POST` aynı adres, form gövdeli | İçeriğin gerçek adresi (`/stream/?tCid=…`) |
| 4. Akış | `GET dys.logo.cloud/stream/?tCid=…` | **Asıl doküman HTML'i** |

2. adım her doküman için değil, **her oturum için bir kez** yapılır. Böylece doküman
başına 3 değil 2 istek gider — siteye binen yük üçte bir azalır. Oturum düşerse
kendiliğinden yeniden kurulur.

---

## 4. Çıktı yapısı

```
netsis-docs/
├── index.md                                  # kökün kendi metni
├── Kullanıcı Dokümanları/
│   ├── index.md                              # bölümün kendi metni
│   ├── Genel/
│   │   ├── index.md
│   │   └── Döviz Takibi/
│   │       ├── index.md
│   │       └── Döviz İsimleri Tanımlama.md
│   └── Lojistik - Satış/…
├── Destek Dokümanları/…
├── Sürüm Dokümanları/…
├── _assets/                                  # tüm görseller, içerik özetiyle adlandırılmış
│   ├── 088477bb321d1b20c939.jpg
│   └── …
├── _rapor.txt                                # çalışma özeti
├── .netsis-catalog.json                      # hiyerarşinin yerel kopyası
└── .netsis-scraper-state.sqlite3             # devam edebilmek için durum kaydı
```

Alt başlığı olan bir düğüm **hem klasör hem doküman** olabilir (392 tanesi öyle);
bu durumda kendi metni o klasörün içine `index.md` olarak yazılır. Böylece ne
hiyerarşi ne de içerik kaybolur.

### Her dosyanın başında ne var?

```yaml
---
title: "Döviz İsimleri Tanımlama"
page_id: "24756179"
product: "netsis-3-enterprise"
depth: 5
is_section: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Genel"
  - "Döviz Takibi"
  - "Kayıt"
  - "Döviz İsimleri Tanımlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / …"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/…"
doc_url: "external?cid=…&link=…&tenantId=…&hideName=True"
slug: "doviz-isimleri-tanimlama_24756179_24753949.html"
source_version: "2021-08-23T09:00:11.553+03:00"
source_bytes: 36115
fetched_at: "2026-09-13T01:35:12+00:00"
generator: "netsis-scraper 1.0.0"
---
```

Bu blok, RAG/arama indeksi kurarken hiyerarşiyi ve kaynağı kaybetmemenizi sağlar.

---

## 5. Seçenekler

### Girdi ve çıktı

| Seçenek | Ne yapar |
|---|---|
| `-o, --output KLASÖR` | Markdown ağacının yazılacağı yer (varsayılan `./netsis-docs`) |
| `--csv DOSYA` | `Başlık;URL` listesi. Kapsama karşılaştırması yapılır ve eksikler raporlanır |
| `--only-csv` | Sadece CSV'deki 1.936 dokümanı indir (ara bölümleri atla) |
| `--skip-branches` | Alt başlığı olan ara düğümleri indirme |
| `--number-prefix` | Klasör/dosya adlarına sitedeki sırayı koruyan `001 ` öneki ekle |
| `--keep-html` | Ham HTML kopyalarını da `_html/` altına kaydet |

### Görseller

| Seçenek | Sonuç | Yaklaşık boyut |
|---|---|---|
| `--images files` (varsayılan) | `_assets/` altına ayrı dosyalar, tekrar edenler tekilleştirilir | ~90 MB |
| `--images inline` | `data:` adresi olarak Markdown içinde kalır | ~530 MB, dosyalar okunaksız |
| `--images skip` | Görsel hiç yazılmaz | ~25 MB |

> Ölçüm: 64 dokümanlık örneklemde 843 görselin yalnızca **210'u benzersizdi** (%75 tekrar).
> Bu yüzden varsayılan kip görselleri içerik özetine (sha256) göre adlandırıp tekilleştirir.

### Ağ davranışı

| Seçenek | Varsayılan | Not |
|---|---|---|
| `-j, --concurrency` | `3` | Aynı anda çalışan iş parçacığı |
| `--min-interval` | `0.35` sn | İki istek arasındaki en kısa süre (tüm havuz için ortak) |
| `--max-attempts` | `5` | Doküman başına deneme sayısı |
| `--offline-catalog` | — | Ağacı ağdan değil yerel kopyadan oku |

Sunucu `429` veya `503` dönerse **bütün havuz** kendiliğinden yavaşlar; işler
düzelince kademeli olarak normale döner. `Retry-After` başlığına uyulur.

### Çalışma kipi

| Seçenek | Ne yapar |
|---|---|
| `--limit N` | Sadece ilk N dokümanı işle (deneme için) |
| `--dry-run` | Hiçbir istek yapma, sadece planı göster |
| `--force` | Tamamlanmışlar dahil her şeyi yeniden indir |
| `--retry-failed` | Sadece hatalı kalanları yeniden dene |
| `--max-path-length` | Toplam yol uzunluğu sınırı (Windows için `240` önerilir) |
| `-v` / `-q` | Ayrıntılı günlük / ilerleme çubuğunu gizle |

---

## 6. Siteyi yormamak için alınan önlemler

1. **Doküman başına 2 istek.** Önyükleme oturum başına bir kez yapılır.
2. **Ortak hız sınırı.** Kaç iş parçacığı olursa olsun, iki istek arası en az
   `--min-interval` saniye geçer. Varsayılan ayarla saniyede ~3 istek.
3. **Düşük eşzamanlılık.** Varsayılan 3; tarayıcının tek sayfada açtığı bağlantı
   sayısından azdır.
4. **Uyarlamalı geri çekilme.** `429`/`503` görülünce aralık iki katına çıkar
   (en fazla 8 saniyeye kadar), başarılı isteklerde kademeli olarak geri iner.
5. **Rastgele saçınımlı üstel bekleme.** Yeniden denemeler eşzamanlı yığılmaz.
6. **Kaldığı yerden devam.** Yeniden çalıştırma, indirilmişi tekrar indirmez.
7. **Kimliğini bildirir.** `User-Agent` başlığında proje adresi yer alır.

`robots.txt` (13.09.2026 tarihinde kontrol edildi): `polaris.logo.cloud/robots.txt`
yalnızca yorum satırlarından oluşur, hiçbir `Disallow` kuralı yoktur.

---

## 7. Dönüşümde nelere dikkat edildi

Bunların hepsi 64 dokümanlık gerçek örneklem üzerinde ölçüldü.

**`<tab>` tuzağı.** Metinde geçen `<tab>` (klavyedeki Tab tuşu) geçerli bir HTML
etiketi değildir. `html.parser`, `lxml` ve `html5lib` — **üçü de** bu metni sessizce
siler. 64 dosyanın 25'inde toplam 224 kez geçiyordu. Script ayrıştırmadan önce
bilinmeyen etiketleri metne kaçışlar, böylece `\<tab\>` olarak korunur.

**Görsel MIME'ı yalan söylüyor.** Kaynak HTML bütün görselleri `image/png` diye
bildirir; ölçümde 843 görselin çoğu aslında JPEG çıktı. Uzantı bildirilen türden
değil, dosyanın sihirli baytlarından belirlenir.

**İç bağlantılar base64 değil.** CSV'deki bağlantılar base64url kodludur, ama
doküman içindeki çapraz bağlantılar **çift URL kodludur**
(`detail/external%253Fcid%253D…`). Script portalın kendi kod akışını birebir taklit
eder: önce base64, sonra çift URL çözümü, sonra tek. Örneklemdeki 24 iç bağlantının
**24'ü** de ağaçtaki bir dokümana çözüldü ve göreli `.md` yoluna çevrildi.

**Tablolar.** GFM tabloları `colspan`/`rowspan` ifade edemez. Basit tablolar Markdown
tablosuna çevrilir; `colspan`/`rowspan` içerenler veriyi bozmamak için sadeleştirilmiş
HTML olarak bırakılır (Markdown görüntüleyiciler ham HTML'i zaten işler).

**Belge içi başlık yok.** Örneklemin tamamında `<h2>`…`<h6>` hiç kullanılmıyor; tek
başlık `<h1>`. Yani anlamlı hiyerarşi belge içinde değil **ağaçta**; o da klasör
yapısı ve ön bilgi bloğuyla korunur.

**Bilgi kutuları.** `div.polaris-information-macro` blokları GFM uyarı kutusuna
(`> [!NOTE]`, `> [!WARNING]`) çevrilir.

---

## 8. Sorun giderme

**"Hiyerarşi ağacı alınamadı"** — İnternet/VPN'i kontrol edin. Daha önce başarılı bir
çalışma yaptıysanız script yerel kopyayı kullanır; zorlamak için `--offline-catalog`.

**Çok sayıda `429` uyarısı** — `--min-interval 1.0 -j 2` ile yavaşlatın.

**Windows'ta "yol çok uzun"** — Çıktıyı kısa bir yola alın (`C:\netsis`) ve
`--max-path-length 200` verin. En uzun göreli yol 188 karakterdir; `C:\netsis` ile
toplam 197 karakter olur ve 260 sınırının altında kalır.

**Bazı dokümanlar hatalı** — `--retry-failed` ile yeniden deneyin. Hatalar
`_rapor.txt` dosyasında sebebiyle birlikte listelenir.

**Baştan başlamak** — Çıktı klasöründeki `.netsis-scraper-state.sqlite3` dosyasını
silin ya da `--force` verin.

---

## 9. Testler

```bash
cd scripts
pip install pytest
python -m pytest tests -q
```
