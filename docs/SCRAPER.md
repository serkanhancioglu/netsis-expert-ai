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
| `--promote-bold-headings` | Bölüm başlığı yerine kullanılan kalın paragrafları `## ` başlığına yükselt (varsayılan **kapalı**, aşağıya bakın) |

### Görseller

| Seçenek | Sonuç | Tahmini toplam boyut |
|---|---|---|
| `--images files` (varsayılan) | `_assets/` altına ayrı dosyalar, tekrar edenler tekilleştirilir | ≤ 370 MB görsel + 28 MB metin |
| `--images inline` | `data:` adresi olarak Markdown içinde kalır | ~640 MB tek parça; RAG için kullanışsız |
| `--images skip` | Görsel hiç yazılmaz | ~28 MB |

> **Bu sayılar nereden geliyor?** 64 dokümanlık gerçek örneklemde ölçüldü ve 2.328
> dokümana doğrusal olarak ölçeklendi: 17,5 MB ham HTML → 0,77 MB Markdown (%4) ve
> 210 benzersiz görsel / 10,2 MB. Görsel rakamı bir **üst sınırdır** — aynı ikonlar
> dokümanlar arasında paylaşıldığı için gerçek toplam bunun altında kalır.
>
> Örneklemdeki 843 görselin yalnızca **210'u benzersizdi**. Tekilleştirme dosya
> sayısını %75 azaltır ama bayt olarak kazancı sadece %11'dir — asıl faydası
> tekrar çalıştırmalarda aynı sonucu vermesi ve yazma sayısını düşürmesidir.

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
| `--refresh` | Her şeyi yeniden indir, **yalnızca içeriği değişmiş** dosyaları yeniden yaz (dönemsel güncelleme için doğru kip) |
| `--force` | Her şeyi yeniden indir **ve** her dosyayı yeniden yaz |
| `--retry-failed` | Sadece hatalı kalanları yeniden dene |
| `--max-path-length` | Çıktı köküne **göreli** yol uzunluğu sınırı (varsayılan `200`) |
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

8. **Devre kesici.** Site bakıma girer ya da paylaşım bağlantıları topluca
   geçersiz olursa, üst üste 12 hata veya son 50 dokümanda %40'ı aşan hata oranı
   çalışmayı durdurur. 2.328 dokümanı tek tek deneyip her birinde 5 kez yeniden
   denemek hem boşuna hem de siteye karşı kaba olurdu.

`robots.txt` (13.09.2026 tarihinde kontrol edildi): `polaris.logo.cloud/robots.txt`
yalnızca yorum satırlarından oluşur, hiçbir `Disallow` kuralı yoktur.

### Veri bütünlüğü kontrolleri

- **Başlık çapraz doğrulaması.** Tek bir HTTP oturumu yüzlerce dokümana hizmet
  ettiği için, sunucu tarafında bir karışıklık A dokümanının gövdesini B'nin
  dosyasına sessizce yazabilir. İndirilen belgenin `<h1>` başlığı ağaçtaki adla
  karşılaştırılır (örneklemde 64/64 örtüşüyor); uyuşmazlık raporlanır.
- **İçerik adresi biçim kısıtı.** Geçersiz bir bağlantıda sunucu `LbsBrowserFrame`
  yerine bir uyarı ikonu döndürür. Script yalnızca
  `https://dys.logo.cloud/stream/?tCid=<uuid>` biçimindeki adresleri kabul eder;
  biçim kısıtı olmadan yanlışlıkla o ikon indirilirdi.
- **Karakter kümesi merdiveni.** `requests`, charset'siz bir `text/*` yanıtında
  `ISO-8859-1` varsayar ve Türkçe metni sessizce bozar. Script sırayla
  `Content-Type` başlığındaki gerçek charset'e, gövdedeki `<meta charset>`'e, sonra
  UTF-8'e bakar.
- **Dosya farkında devam.** Durum veritabanı "tamam" dese bile hedef dosya
  silinmiş ya da boşsa o doküman yeniden indirilir.

### Çıktı belirlenimli (deterministic)

Aynı kaynaktan iki kez indirdiğinizde **birebir aynı** ağacı alırsınız. Bu iki
tasarım kararıyla sağlanır:

1. **Yol bütçesi mutlak yoldan bağımsız.** `--max-path-length` çıktı köküne
   *göreli* yola uygulanır. Bütçeye çıktı klasörünün uzunluğu katılsaydı, klasör
   adı tek karakter uzadığında kısaltma eşiği kayar ve bazı dosyalar yeniden
   adlandırılırdı — yani aynı ağaç iki makinede farklı dosya adları üretirdi.
   (Ölçüldü: 70 karakterlik bir çıktı yolunda 1 karakterlik fark 2.328 yoldan
   5'ini değiştiriyordu.) Windows 260 sınırı ayrıca kontrol edilir ve aşılırsa
   uyarı verilir.

2. **Değişmeyen dosya yeniden yazılmaz.** Değişiklik özeti yalnızca gövdeden
   hesaplanır. `fetched_at` zaman damgası da hesaba katılsaydı her dosya her
   çalışmada değişir; hem değişiklik tespiti işlevsizleşir hem de iki çalışma
   arasındaki `git diff` baştan aşağı gürültü olurdu.

   Bunun asıl faydası `--refresh` kipinde görülür: aylık bir güncelleme
   çalıştırdığınızda her doküman yeniden indirilir ama diskte yalnızca gerçekten
   değişenler yenilenir. Çıktı klasörünü git'te tutuyorsanız `git diff` size tam
   olarak Logo'nun neyi değiştirdiğini gösterir. `--force` bu kontrolü bilerek
   atlar; adı üstünde, her şeyi yeniden yazmak istediğinizde kullanılır.

Kısaltma gerektiğinde dosya adının **gövdesi** kesilir, `.md` uzantısı her zaman
korunur. Aksi halde kesilen dosyalar `**/*.md` taramalarından (MkDocs, çoğu RAG
yükleyicisi) sessizce düşerdi. Varsayılan bütçe 200 ile bugünkü ağaçta hiçbir
dosya kısaltılmıyor (en uzun göreli yol 188 karakter).

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

**Başlıklar seyrek ama var.** 64 dokümanın 57'sinde tek başlık `<h1>`; ancak 7
dokümanda `<h2>`–`<h5>` de kullanılıyor (toplam 45 başlık) ve seviyeler **atlıyor**
(`h1 → h4 → h5`). Sadece `h1` işleyen bir dönüştürücü bu 45 bölüm başlığını düz
paragraf yapardı. Script `h1`–`h6`'yı olduğu gibi korur, yeniden numaralandırmaz.
İki dokümanda birden fazla `<h1>` var (6 ve 3 tane); ilki başlık sayılır, kalanlar
gövde başlığı olarak kalır.

**Gömülü videolar.** İçerik `<iframe class="youtube-player">` ile geliyor ve bunlar
`<span><strong>` içinde, yani **satır içi** bağlamda. Sadece blok bağlamında iframe
arayan bir dönüştürücü örneklemdeki 10 videoyu sessizce yutar. Script bunları
`[Video izle (YouTube: …)](…)` bağlantısına çevirir.

**İki ayrı bilgi kutusu sistemi.** Kaynakta hem `div.polaris-information-macro` hem
de `div.bsv-callout` kullanılıyor. Yalnızca birine bakan bir dönüştürücü diğerini
düz paragraf yapar. İkisi de GFM uyarı kutusuna (`> [!NOTE]`, `> [!TIP]`,
`> [!WARNING]`) çevrilir.

**`colspan` bir tuzak.** Örneklemde `colspan` 792 kez geçiyor ama **hepsi `colspan="1"`**
— yani anlamsız. `rowspan` hiç yok. Varlığına bakan bir kod bütün tabloları gereksiz
yere HTML'e düşürürdü; script değeri okuyup `> 1` mi diye bakar. Sonuç: 141 tablonun
140'ı Markdown tablosu, 1'i (iç içe tablo içerdiği için) HTML.

**Başlık satırı her zaman `<th>` değil.** Tabloların bir bölümü hiç `<th>` kullanmaz;
ilk satırı kalın `<td>`'dir. Sadece `<th>` arayan bir tespit bu tabloları başlıksız
bırakır. Script kalın-`<td>` satırını da başlık kabul eder.

---

## 7b. `--promote-bold-headings` — ne yapar, neden kapalı?

Netsis rapor dokümanlarının hemen hepsi aynı iskeleti kullanır: *Ön Sorgulama,
Kısıt, Sıralama, Ölçekleme, Yazıcı Seçenekleri*. Ama bunlar `<h2>` değil, kalın
paragraf olarak yazılmış. Bu seçenek açıkken script onları `## ` başlığına
yükseltir; arama ve RAG parçalama (chunking) için gezinmeyi belirgin biçimde
kolaylaştırır.

Ölçüm (64 dokümanlık örneklem): **30 dokümanda 152 başlık** yükseltilir.

Yanlış pozitifleri önleyen üç kural:

1. Dokümanda gerçek `<h2>`–`<h6>` ya da birden fazla `<h1>` varsa **hiç** uygulanmaz.
2. Paragraf tamamen kalın olmalı. `**Eşit Değil:** Raporda listelenmeyecek…`
   gibi satır başı etiketleri yükseltilmez.
3. Metin 60 karakterden kısa, en fazla 8 kelime olmalı ve `; : . ,` ile bitmemeli.

Kaynakta olmayan bir yapı ürettiği için **varsayılan olarak kapalıdır**. Ham
sadakat istiyorsanız dokunmayın; arama korpusu kuruyorsanız açın.

---

## 8. Sorun giderme

**"Hiyerarşi ağacı alınamadı"** — İnternet/VPN'i kontrol edin. Daha önce başarılı bir
çalışma yaptıysanız script yerel kopyayı kullanır; zorlamak için `--offline-catalog`.

**Çok sayıda `429` uyarısı** — `--min-interval 1.0 -j 2` ile yavaşlatın.

**Windows'ta "yol çok uzun"** — En uzun göreli yol 188 karakterdir.
`C:\Users\<ad>\Documents\netsis-docs` (37 karakter) ile toplam 226 karakter olur
ve 260 sınırının altında kalır. Yine de uyarı alırsanız çıktıyı kısa bir yola
alın (`C:\netsis`) ya da `--max-path-length 150` verin.

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
