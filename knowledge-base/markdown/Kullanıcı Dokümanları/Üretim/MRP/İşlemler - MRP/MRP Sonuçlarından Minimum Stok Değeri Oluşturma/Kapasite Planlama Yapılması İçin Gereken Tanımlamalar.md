---
title: "Kapasite Planlama Yapılması İçin Gereken Tanımlamalar"
page_id: "50668916"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Üretim"
  - "MRP"
  - "İşlemler / MRP"
  - "MRP Sonuçlarından Minimum Stok Değeri Oluşturma"
  - "Kapasite Planlama Yapılması İçin Gereken Tanımlamalar"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Üretim / MRP / İşlemler / MRP / MRP Sonuçlarından Minimum Stok Değeri Oluşturma / Kapasite Planlama Yapılması İçin Gereken Tanımlamalar"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTk2YTM3ZmRmLTc2ZWItNDhhOC1hOWRiLTBiZGUyYzk0Yjg3ZSZsaW5rPWYyYjliZTU3LTFlY2QtNDc2Ni04OGU1LTI1YThlMzE0Mjc0MyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=96a37fdf-76eb-48a8-a9db-0bde2c94b87e&link=f2b9be57-1ecd-4766-88e5-25a8e3142743&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "kapasite-planlama-yapilmasi-icin-gereken-tanimlamalar_50668981_50668916.html"
source_version: "2022-10-21T09:41:27.873+03:00"
source_bytes: 19230
fetched_at: "2026-09-13T04:20:06+00:00"
generator: "netsis-scraper 1.0.0"
---
# Kapasite Planlama Yapılması İçin Gereken Tanımlamalar

Kapasite Planlama işleminde çalıştırılması gereken işlemler ve raporun bulduğu sonuçlar aşağıda örneklerle anlatılmıştır.

Fabrikada 3 adet işlem yapılarak üretilen bir mamul olduğu düşünüldüğünde, yapılması gereken tanımlamalar şunlardır; İş İstasyonları, Operasyonlar, Reçete Kaydı (Rota), Üretim Süresi, İhtiyaç Kapasite, Mevcut Kapasite, Gerçekleşen (Simultane) İşlem Birimi, Çalışma Takvimi, Hazırlık Süresi, Geçiş Süresi/Geçiş Miktarı, Simültane Kapasitenin Tamamını Kullanamama, Maliyet Bilgileri.

**İş İstasyonları**

İş İstasyonları; fabrikada bulunan, her biri ayrı işlemlerden sorumlu, kendi içlerinde benzer işlemleri yapan üretim birimlerinden (Makine/İşçi) oluşan üretim merkezleridir.

**Örnek**

IST1: Yıkama istasyonu. 1 adet makine bulunsun.

IST2: Kurutma istasyonu. 1 adet makine bulunsun.

IST3: Yapıştırma istasyonu. 1 işçi bulunsun.

**Operasyonlar**

Operasyonlar, mamulün üretilmesi sırasında yapılan işlemlerdir. Her bir iş istasyonu bir işlem gibi tanımlandığında örnek aşağıdaki şekilde olur.

**Örnek**

OP1: Yıkama.

OP2: Kurutma.

OP3: Yapıştırma.

**Reçete Kaydı (Rota)**

Reçete Kaydı (Rota), kapasite Planlama yapılması için öncelikle rota tanımının yapılması gerekir. Rota, bir mamul/yarı mamulün işlem reçetesidir. Mamulün işlem sırası (Rotası) Üretim → Reçete Kaydı bölümünden yapılır.

**Örnek**

--- M1

--- YM1 – 1 adet

--- HM1 – 1 adet

--- HM2 – 1 adet

--- OP3

--- OP1

--- OP2

şeklinde ürün ağacı tanımlanmış olsun.

**Üretim Süresi**

Üretim Süresi, her bir işlemde bir birim üretim için gereken zamandır. Operasyon bazında tanımlanır. Aynı operasyon için ürün bazında rota tanımı sırasında istendiği zaman değiştirilebilir.

**Örnek**

OP1; 2 saat

OP2; 1 saat

OP3; 0.5 saat olsun.

**İhtiyaç Kapasite**

İhtiyaç Kapasite, planlanan miktarda mamulün üretilmesi için gereken kapasitedir.

**Örnek**

Yukarıda rotası verilen M1 mamulünün 1 birimi için:

YM1

HM1 – 1 adet

HM2 – 1 adet

```text
OP3      0.5 saat
```

Toplam 0.5 saat

M1

YM1 – 1 adet 0.5 saat

OP1 2 saat

OP2 1 saat

Toplam 3.5 saat kapasite ihtiyacı vardır.

M1 mamulünden 100 adet üretilmesi gerekiyor ise:

İhtiyaç Kapasite = 100 \* 3.5 = 350 saat olarak hesaplanır.

**Mevcut Kapasite**

Mevcut Kapasite; bir zaman biriminde, iş istasyonu bazında, fabrikanın sahip olduğu kapasitedir.

Zaman Birimi, Günlük veya Haftalık olabilir. Kapasite, iş istasyonu bazında, operasyon bazında veya fabrika geneli olabilir.

**Örnek**

Yukarıda tanımlanan fabrikada, haftanın her günü 1 vardiya çalışıldığı ve her bir vardiyanın 8 saat olduğu düşünüldüğünde, 1 haftalık zaman biriminde örnek aşağıdaki şekilde olur:

| İstasyon | Mevcut Kapasite |
| --- | --- |
| IST1 | 56 saat |
| IST2 | 56 saat |
| IST3 | 56 saat |

Yukarıda tanımlanan üretimin gerçekleşmesi için örnek aşağıdaki şekilde olur:

| İstasyon | İhtiyaç Kapasite | Mevcut Kapasite | Fark Kapasite |
| --- | --- | --- | --- |
| IST1 | 2 \* 100 = 200 | 56 | \- 144 |
| IST2 | 1 \* 100 = 200 | 56 | \- 144 |
| IST3 | 0.5 \* 100 = 50 | 56 | 6 |

Örnekte, yıkama ve kurutma istasyonlarında kapasitenin eksikliği (Yetmediği), yapıştırma iş istasyonunda ise kapasite fazlalığı kaldığı görülür.

**Gerçekleşen (Simultane) İşlem Birimi**

Örnekte, IST1 ve IST2’deki makinelerin üretim sürecinde darboğaz bir durum oluşturduğu görülür.

Bu iş istasyonlarının kapasitesini arttırmak için her birine aynı işi yapabilen bir makine eklendiği düşünüldüğünde; 100 adet M1’in bir haftalık bir sürede üretilmesi için tablo aşağıdaki şekilde olur:

| İstasyon | Sim. İşlemi | Üretim Süresi | **İhtiyaç** **Kapasitesi** | Mevcut Kapasite | Fark Kapasite |
| --- | --- | --- | --- | --- | --- |
| IST1 : Yıkama | 2 makine | 2 saat (OP1) | 200 | 2 \* 8 \* 7 = 112 | -88 |
| IST2 : Kurutma | 2 makine | 1 saat (OP2) | 100 | 2 \* 8 \* 7 = 112 | 12 |
| IST3 : Yapıştırma | 1 işçi | 0.5 saat (OP3) | 50 | 1 \* 8 \* 7 = 56 | 6 |

Bu durumda IST1’de yine kapasite eksiği oluştuğu fakat IST2’nin kapasitesinin yeterli olduğu gözlemlenir.

**Çalışma Takvimi**

Yukarıdaki örnekte IST2 iş istasyonu her gün bir yerine iki vardiya çalıştırılırsa; 2 makine, günde 16 saatten, 7 gün sonucu 224’lük kapasiteye ulaştırılıp, mevcut kapasitenin ihtiyaç kapasiteyi karşılaması sağlanabilir. Fabrikanın ve iş istasyonlarının çalışma takvimleri, "Takvim" bölümünden tanımlanır. "Takvim" bölümünde, her gün için çalışılan vardiya sayısı tanımlanır. Çalışılmayan - Pazar, Bayram gibi - günlerde vardiya sayıları sıfırlanır. Kapasite planlama, tanımlanan takvimi baz alarak iş istasyonlarının kapasitelerini hesaplar.

**Hazırlık Süresi**

Hazırlık Süresi, makinelerin üretim prosesine (İşlemine) başlamadan önce her üretim için bir kere yapılan işlemler için harcanan süredir. Her makine - simültane işlem - için bir kez bu sürenin geçmesi gerekir. Operasyon bazında - rotada - tanımlanır. Hazırlık süresi bulunan operasyonlar için ihtiyaç planlama hesaplaması sırasında, simültane işlemi \* hazırlık süresi kadar ekstra kapasite ihtiyacı hesaplanır.

**Örnek**

Yukarıdaki örnekte IST2’deki iki adet kurutma makinesinin ikişer saatlik hazırlık süreleri olduğu düşünüldüğünde, ihtiyaç kapasitesi aşağıdaki şekilde değişir:

| İstasyon | Sim. İşl. | Üretim Süresi | İhtiyaç Kapasitesi | Mevcut Kapasite | Fark |
| --- | --- | --- | --- | --- | --- |
| IST1: Yıkama | 2 mak. | 2 saat (OPR1) | 200 | 2\*8\*7=112 | -88 |
| IST2: Kurutma | 2 mak. | 1 saat (OPR2) | 100+(2\*2)=104 | 2\*8\*7=112 | 8 |
| IST3: Yapıştırma | 1 işçi | 0.5 saat (OPR3) | 50 | 1\*8\*7=56 | 6 |

**Geçiş Süresi, Geçiş Miktarı**

Geçiş Süresi, Geçiş Miktarı, bir operasyondan diğerine geçiş sırasında geçen süre ve miktar kısıtlamasının tanımlandığı bölümlerdir. Taşıma ile ilgili problemlerden dolayı oluşabilir.

**Örnek 1**

Bir operasyon sonunda üretilen yarı mamuller kasalara konar ve bu kasalar belli sayıda ürün alır. Bir kasa dolduğunda, herhangi bir taşıma aracıyla başka bir bölüme aktarılır. Burada kasa kapasitesi geçiş miktarı, kasanın diğer bölüme taşınması için geçen süre de geçiş süresidir. Bu bilgiler operasyon bazında - rotada - tanımlanır. Geçiş süresi ihtiyaç kapasitesini etkiler.

**Örnek 2**

Yukarıdaki örnekte OP2’nin geçiş miktarı 20, geçiş süresi 1 saat olsaydı, 100 birimlik mal 5 kerede taşınacak ve her taşıma için 1 saatten 5 saatlik ek kapasiteye ihtiyaç olacaktı.

OP2 için ihtiyaç kapasite aşağıdaki şekildedir:

| İstasyon | **Sim.** **İşlemi** | Üretim Süresi | İhtiyaç Kapasitesi | Mevcut Kapasite | Fark |
| --- | --- | --- | --- | --- | --- |
| IST1: Yıkama | 2 mak. | 2 saat (OPR1) | 200 | 2\*8\*7 = 112 | -88 |
| IST2: Kurutma | 2 mak. | 1 saat (OPR2) | 100+(2\*2)+5=109 | 2\*8\*7 = 112 | 3 |
| IST3: Yapıştırma | 1 işçi | 0.5 saat (OPR3) | 50 | 1\*8\*7 = 56 | 6 |

Geçiş miktarının 1 olması durumunda (Her bir üretilen parçanın sürekli diğer operasyona aktığı durumda) geçiş süresi için ihtiyaç kapasite geçiş süresi \* üretim miktarı olur. Geçiş miktarının 0 (Sıfır) olması, üretimin tamamının bitirilip diğer operasyona başlanacağı anlamına gelir. Bu durumda ihtiyaç kapasite - bir kerede geçiş yapıldığı için - geçiş süresi kadardır.

**Simültane Kapasitenin Tamamını Kullanamama**

İş istasyonlarında birbiriyle benzer iş yapan, kapasiteleri birbirine eşit veya yakın makine/insan olduğu belirtilmişti. Bazen aynı işi yapacak birden fazla makine olduğu halde, bir işin kısıtlı sayıda makinede yapılacağı durumlar ile karşılaşılabilir. Genelde plastik/metal enjeksiyon makinelerinde bu durum görülür. Bunun sebebi, makineye üretilecek olan parçayla ilgili bir kalıp - veya herhangi bir aparat- takılması ve makinenin parçayı bu kalıba göre üretmesinden kaynaklanır. Yani, bir kalıp makineye takıldığında, diğer bir makineye de takılamayacağı için, o ürün için bir anda bir makinenin kapasitesi kullanılabilecek, diğer bir makinenin aynı işi yapma yeteneği bulunsa da, kalıp limitinden dolayı diğer makinenin kapasitesi kullanılamaz. Bu durumda, istasyon tanımı yapılırken; simültane işlem sayısını, makine sayısı kadar fakat operasyon bazında, simültane işlem sayısını kalıp sayısı kadar tanımlamak gerekir.

**Örnek**

Yukarıdaki örnekte, kurutma makinelerine kalıp takma gereksinimi olduğu ve bir mamul için bir kalıp bulunduğu varsayıldığında tablo aşağıdaki şekildedir:

| İstasyon | Sim. İşlemi | İhtiyaç Kapasitesi | Mevcut Kapasite | Fark Kapasite |
| --- | --- | --- | --- | --- |
| IST1: Yıkama | 2 makine | 200 | 112 | \- 88 |
| IST2: Kurutma | 2 makine | 109 | 2\*8\*7=112 | 3 |
| (OP2–Kurutma Opr.) | 1 makine | 109 | 1\*8\*7=56 | \- 53 |
| IST3: Yapıştırma | 1 işçi | 50 | 56 | 6 |

Burada, iş istasyonu bazında kapasitenin yeteceği düşünülse de kalıp kısıtlaması nedeniyle aslında bir darboğaz yaşanacağı görülür.

**Maliyet Bilgileri**

İstendiğinde operasyon bazında birim işçilik ve birim diğer maliyetleri tanımlanabilir. İhtiyaç kapasite maliyeti, mevcut kapasite maliyeti ve fark kapasite maliyeti olarak raporlanabilir.
