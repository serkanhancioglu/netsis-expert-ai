# Araştırma betikleri — protokol nasıl çözüldü

Bu klasördeki dosyalar **son ürün değil**, `netsis_scraper` paketinin dayandığı
protokolü ortaya çıkarmak için sırayla çalıştırılan keşif betikleridir. Sakladım ki
site bir gün değişirse aynı yolu tekrar yürüyebilesiniz.

## Sıra ve bulgular

### 1. `probe.js` — tarayıcıyla render denemesi (Playwright)

Portalın bir Angular SPA olduğunu ve içeriğin `<iframe>`'den geldiğini doğrulamak için.

**Sonuç:** Bu ortamda headless Chromium'un TLS el sıkışması proxy tarafından
kesildi. Ama gerek de kalmadı — protokol saf HTTP ile çözüldü. Betiği referans
olarak bıraktım; kendi bilgisayarınızda çalışır.

### 2. `vprobe.py` — Vaadin UIDL el sıkışması

Asıl kırılma noktası. `dys.logo.cloud/external?...` adresinin bir **Vaadin 8**
uygulaması olduğu (`com.lbs.documentservicefrontend.DocumentServiceWidgetSet`)
ve içeriğe UIDL protokolüyle ulaşılabildiği burada bulundu.

**Bulunan zincir:**

```
GET  /external?cid=…&link=…&tenantId=…&hideName=True
     -> vaadin.initApplication("ROOT-2521314", {...,"serviceUrl":"/vaadinServlet"})

POST aynı adres + "&v-<epoch_ms>"   (application/x-www-form-urlencoded)
     v-browserDetails=1&theme=documentservice&v-appId=…&v-sh=…&v-loc=…
     -> {"v-uiId":0,"uidl":"{…}"}
     -> uidl.state["4"].resources.source.uRL
        = https://dys.logo.cloud/stream/?tCid=<uuid>

GET  /stream/?tCid=<uuid>
     -> ASIL DOKÜMAN HTML'İ
```

Bu adımların POST gövdesi **form kodlu** olmalı. JSON gönderilirse sunucu sessizce
önyükleme HTML'ini geri döndürür — hata vermez, sadece yanlış cevap verir.

### 3. `fetchone.py` — tek doküman + hata davranışı

Geçersiz bir `cid`/`link` ile denendiğinde UIDL yanıtında `LbsBrowserFrame` yerine
**`externaShareExpired`** bileşeni ve `theme://images/task_list_warning.svg`
kaynağı geliyor.

**Kritik:** "İlk `resources.source` değerini al" diyen naif bir kod bu uyarı
ikonunun adresini indirmeye çalışır ve anlaşılmaz bir hatayla döner. Bu yüzden
`client.py` yalnızca `http(s)` şemalı ve tercihen `LbsBrowserFrame` kimlikli
kaynakları kabul eder.

### 4. `getsamples.py` / `bigsample.py` — örneklem toplama

64 doküman (14 + 50) indirildi. Dönüşüm kuralları bu gerçek örneklem üzerinde
ölçülerek belirlendi:

| Ölçüm | Sonuç |
|---|---|
| `<h2>`…`<h6>` kullanımı | **0** — hiyerarşi belge içinde değil, ağaçta |
| `<tab>` sahte etiketi | 25 dosyada 224 kez; üç ayrıştırıcı da siliyor |
| Görsel sayısı | 843, bunların yalnızca **210'u benzersiz** (%75 tekrar) |
| Görsel MIME'ı | Hepsi `image/png` diyor; çoğu aslında JPEG (`ffd8ffe0`) |
| İç bağlantılar | base64 değil, **çift URL kodlu** |
| En büyük doküman | 2.8 MB |
| Başarı oranı | 64/64 (4 eşzamanlı işçiyle) |

## Diğer keşifler

**Hiyerarşi API'si** — `main.js` içindeki `GetAuthorizedTrees` çağrısından bulundu:

```
GET https://polaris.logo.com.tr/api/Documents/GetAuthorizedTrees?product=netsis-3-enterprise
```

Tek istekte 2.328 düğümlük tüm ağacı döner (2.7 MB). CSV'deki 1.936 bağlantı bu
ağacın **yaprakları**; kalan 392 düğüm ara bölümler. Eşleşme %100.

**`DYS_APP_URL` nereden geldi** — Angular yapılandırması:

```
GET https://polaris.logo.cloud/assets/config/app.config.json
    -> DYS_APP_URL          = https://dys.logo.cloud
    -> CONFIG.TOKEN.API_URI = https://polaris.logo.com.tr
```

**robots.txt** (13.09.2026) — `polaris.logo.cloud/robots.txt` yalnızca yorum
satırlarından oluşuyor, hiçbir `Disallow` kuralı yok.

## Çalıştırma

Bu betikler `scratchpad` düzenine göre yazıldı ve `trees.json`, `flat_tree.json` gibi
ara dosyalar bekler. Belgesel değeri için olduğu gibi bırakıldı; günlük kullanım için
`python -m netsis_scraper` yeterlidir.
