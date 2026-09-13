---
title: "Malzeme Gereksinim Planlama Yapılırken Dikkat Edilmesi Gereken Noktalar"
page_id: "50666572"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Üretim"
  - "MRP"
  - "Kayıt / MRP"
  - "Malzeme Gereksinim Planlama"
  - "Malzeme Gereksinim Planlama Yapılırken Dikkat Edilmesi Gereken Noktalar"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Üretim / MRP / Kayıt / MRP / Malzeme Gereksinim Planlama / Malzeme Gereksinim Planlama Yapılırken Dikkat Edilmesi Gereken Noktalar"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTE4NjZiODdjLTc0NzItNDQ1OS1iMzljLTE0ZjYxOGY1NDYyZiZsaW5rPWI3MjBkY2RmLWQ4YjgtNDhiNC04Y2EzLWY0ZjZhOTQwMGE4MyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=1866b87c-7472-4459-b39c-14f618f5462f&link=b720dcdf-d8b8-48b4-8ca3-f4f6a9400a83&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "malzeme-gereksinim-planlama-yapilirken-dikkat-edilmesi-gereken-noktalar_50666574_50666572.html"
source_version: "2022-10-18T11:05:44.833+03:00"
source_bytes: 39964
fetched_at: "2026-09-13T04:19:31+00:00"
generator: "netsis-scraper 1.0.0"
---
# Malzeme Gereksinim Planlama Yapılırken Dikkat Edilmesi Gereken Noktalar

MRP modülünde, malzeme gereksinimi hesaplanırken gereksinim miktarlarını, satıcı siparişlerinin miktarını ve tarihini etkileyecek temin süresi, asgari limit, sipariş politikaları gibi bilgilerin girildiği bölümler şunlardır:

- Stok Modülünde - Müşteri/Satıcı Stok Kayıtları.
- Cari Modülünde - Cari Planlama Kayıtları.
- Stok Modülünde - Stok Planlama Kayıtları.

Müşteri/Satıcı Stok Kayıtları bölümünde hem satıcı hem de stok bazında planlama bilgileri tanımlanır. Böylece, farklı satıcılardan alınan aynı malzemeler için farklı nakliye süreleri, sipariş politikaları, minimum sipariş miktarları girilir.

Cari Planlama Kayıtları bölümünde, sadece satıcılar bazında sipariş politikası, nakliye süresi, bildirim süresi gibi bilgiler girilir.

Stok Planlama Kayıtları bölümünde ise, sadece stok bazında planlama bilgileri girilir.

**Örneğin;**

Bir stok ile ilgili Stok Planlama Kayıtları ekranına "Nakliye Süresi" girildiği zaman, Müşteri/Satıcı Stok Kayıtları bölümünde o stokla ilgili bir bilgiye ulaşılmazsa, girilen nakliye süresinin planlama sırasında tüm satıcılar için aynı olduğu düşünülür.

Bu bilgiler program tarafından yukarıdaki sıraya göre dikkate alınır. Bir stok ile ilgili Müşteri/Satıcı Stok Kayıtları bölümünde tanımlama yapılmışsa, öncelikle buraya bakılır. Müşteri/Satıcı Stok Kayıtları bölümünde bir tanımlama bulunamazsa, Stok Kartı Kayıtları Cari Kodu bölümünde yazılan satıcı ile ilgili Cari Planlama Kayıtlarına bakılır. Burada da bir bilgi bulunamazsa, Stok Planlama Kayıtlarındaki tanımlamalara göre planlama yapılır.

**Üretim/Bildirim Süresi**

Bazı uygulamalarda yan sanayiciye siparişi yükleme tarihinden belirli bir süre öncesinde bildirim yapılması gerekir. Aynı şekilde üretilen yarı mamuller için de, istenilen zamanda elde olması için belirli bir süre önce, üretim emrinin verilmiş olması gerekir.

Üretim/Bildirim Süresi, stok bazında Stok Planlama Kayıtlarında sadece gün olarak girilebilir. Satıcı bazında "Cari Planlama Bilgilerinde" veya satıcı-stok bazında "Müşteri-Satıcı Stok Bilgilerinde" gün/ay/yıl periyotlarından biri seçilerek tanımlama yapılabilir.

Bu süre, MRP çalışması sırasında üretilen yarı mamuller için üretim süresi olarak algılanır. Satıcı siparişlerinde ise MRP ile hesaplanacak yükleme tarihinde belirlenen bildirim süresi kadar önceye gidilerek, bildirim konusunda herhangi bir gecikme olup olmadığı belirlenir.

Bildirimi veya yüklemesi gecikmiş ihtiyaçlar ayrıca raporlanır.

**Nakliye Süreleri**

Nakliye süreleri, hammaddeler için tedarikçiden çıkıp işletmeye teslim edilene kadar geçen süredir. MRP uygulamasında satıcı ya da hammadde bazında farklı nakliye süreleri dikkate alınarak planlama yapılabilir.

Nakliye süreleri istenirse stok bazında detaylı olarak Stok Modülü/Müşteri-Satıcı Stok Bilgileri alanında, istenirse stok detayına girilmeden sadece satıcı bazında Cari Planlama Bilgilerin bölümünden tanımlanabilir.

MRP Uygulamasında, satıcının malı yükleme ve teslim tarihi hesaplanırken nakliye süresine bakılır. Herhangi bir hammadde için Müşteri-Satıcı Stok Kayıtlarında nakliye süresi girilmişse öncelikli olarak buradaki tanımlama dikkate alınır. Burada bir tanımlama yapılmamış ise, satıcının Cari Planlama Kayıtlarındaki tanımlaması dikkate alınır. Eğer burada da herhangi bir tanımlama yoksa, Stok Planlama Kayıtlarında stok bazında tanımlanan nakliye süresi dikkate alınır.

**Yükleme Periyodu ve Günü**

Tedarikçilerin haftanın belirli günlerinde ya da ayın belirli bir gününde yükleme yaptıkları durumda, plan sırasında yükleme günlerinin de dikkate alınması için “Yükleme Periyodu ve Günü” alanları kullanılır.

İstenirse satıcı-stok bazında Müşteri-Satıcı Stok Kayıtlarında, istenirse satıcı bazında Cari Planlama Kayıtlarında yükleme düzeni tanımlanabilir. Periyod tipi olarak "Hafta" seçilirse haftanın hangi günü yükleme yapıldığı, "Ay" seçilirse ayın hangi gününde yükleme yapıldığı belirlenir. Her gün yükleme yapılabiliyorsa periyod tipinin "Günlük" olarak seçilmesi gerekir.

MRP Uygulamasında malzemenin elde olması gereken tarihten nakliye süresi kadar geri gidilerek satıcının malı yüklemesi gereken tarih bulunur. Fakat, ilgili yükleme günü tanımlamalara göre uygun bir gün değilse, bu günden önceki ilk yükleme günü tespit edilerek "Yükleme Tarihi" olarak saptanır ve satıcıya bildirilir. Hesaplanan tarihin, satıcı siparişi yükleme tarihi olduğu unutulmamalıdır.

Herhangi bir hammadde için Müşteri-Satıcı Stok Kayıtlarında yükleme periyodu/günü tanımlanmış ise, öncelikli olarak buradaki tanımlama dikkate alınır. Burada bir tanımlama yapılmamış ise, satıcının Cari Planlama Bilgilerindeki tanımlama dikkate alınır. Eğer burada da herhangi bir tanımlama yoksa, Stok Planlama Kayıtlarında stok bazında tanımlanan periyod tipi ve günü dikkate alınır.

**Örneğin;**

Satıcının 26.03.2020 tarihinde teslim etmesi gereken bir hammadde için nakliye süresi 3 gün olduğu ve yüklemenin her hafta Cuma günü yapıldığı varsayıldığında, MRP sonucunda bulunan yükleme tarihi Cuma gününe denk gelen 21.03.2020 tarihi olacaktır. Bu durumda nakliye süresi 3 gün olduğu için mal 24.03.2020 tarihinde elde olur. Yani gereksinim tarihi olan 26.03.2020 tarihinden iki gün önce. Her gün yükleme yapılıyor olsaydı, yükleme tarihi 23.03.2020 olacaktı.

**Kesinleşme Periyodu ve Süresi**

Tedarikçilerle periyodik bir sipariş sistemi üzerinde anlaşılmışsa, MRP sonuçlarından oluşturulan satıcı siparişlerinin de bu sisteme göre oluşması isteniyorsa “Kesinleşme Süresi” alanı kullanılabilir.

**Örneğin;**

Tedarikçilere her hafta sipariş verildiği düşünüldüğünde, içinde bulunulan haftada verilen sipariş, bir sonraki hafta "Pazartesi" gününden itibaren n (Bilinmeyen) haftalık kesinleşmiş, bundan sonraki n (Bilinmeyen) aylık planlanan sipariş miktarlarını kapsar. Bir sonraki hafta içinde tekrar aynı süreleri kapsayan yeni siparişler verilir. Haftalık ana siparişlerin dışında ek siparişler de verilebilir. Haftalık siparişlerin geçmişe yönelik kayıtları saklanarak sipariş sistemine kaydedilmesi için Fatura modülünde bahsi geçen "Sipariş Revizyon Sisteminin" kullanılması gerekir.

MRP sonuçlarında, kesinleşmiş siparişler başlangıç tarihinden üretim/bildirim süresi kadar sonra başlar. Bu tarihten kesinleşme süresi kadar zaman aralığında bulunan siparişler **kesin** olarak işlenir. Eğer üretim/bildirim süresi zaman aralığında, verilmesi gereken bir sipariş sonucu çıkarsa, bu siparişin daha önceden verilmiş olması gerektiği, gecikmiş olduğu düşünülür. Çünkü, tedarikçinin kendi üretimini yapabilmesi için yeterli zaman kalmamıştır.

**Planlanan Hafta Sayısı**

Kesinleşme süresinden sonra MRP sonuçlarından oluşan satıcı siparişlerinin, Planlanan Siparişler olarak satıcıya bildirilmesi istendiğinde kullanılacak alandır. Kesinleşme süresinin sonrasında verilen siparişler istenen hafta sayısı kadar, haftalara kümüle edilerek, **planlanan haftalık siparişler** oluşturulabilir.

**Planlanan Ay Sayısı**

Planlanan hafta sayısından sonraki tarihlerde, MRP'de oluşan siparişlerin **aylık planlanan sipariş**ler olarak satıcıya bildirilmesi için kullanılan alandır.

**Örneğin;**

Üretim/Bildirim Süresi: 1 hafta

Kesinleşme Süresi : 1 hafta

Planlanan Hafta Sayısı: 1

Planlanan Ay Sayısı : 1

MRP Başlangıç Tarihi: 01/04/2003 ise;

MRP başlangıç tarihinden itibaren, bildirim periyodu cinsinden ilk gün bulununcaya kadar ileri gidilir ve bildirim süresi ilgili günden sonra başlar.

**Örneğin;**

01.04.2020 tarihi Çarşamba gününe denk gelir. Bildirim periyodu "Hafta" olduğu için, bildirim süresi bir sonraki haftanın ilk günü olan 07.04.2020 tarihinde başlar.

07/04/2020-13/04/2020 tarihleri bildirim süresi olarak düşünülür.

MRP sonucunda 14/04/2020-20/04/2020 tarihleri arasında yükleme tarihi bulunan siparişler, ilgili tarihlere günlük ve kesin siparişler olarak işlenir.

21/04/2020-27/04/2020 tarihleri arasında yükleme tarihi bulunan siparişler bir haftaya kümüle edilir. Yükleme Tarihi 21/04/2020 ve Teslim Tarihi 27/04/2020 olan tek satırlık, haftalık planlanan sipariş oluşturulur.

28/04/2020-30/04/2020 tarihleri arasında yükleme tarihi bulunan siparişler kümüle edilerek, Yükleme Tarihi 28/04/2020 ve Teslim Tarihi 30/04/2020 olan tek satırlık, aylık planlanan sipariş olarak oluşturulur.

01/05/2020-31/05/2020 tarihleri arasında yükleme tarihi bulunan siparişler bir aya kümüle edilir. Yükleme Tarihi 01/05/2003 ve Teslim Tarihi 31/05/2003 olan tek satırlık, aylık planlanan sipariş olarak oluşturulur.

**Sipariş Politikası (Parti Büyüklüğü, Lot Size)**

Sipariş politikası; hammadde için katları sipariş edilmesi gereken miktarı, yarı mamul için ise katları ve üretilmesi gereken miktarı ifade eder. Satıcının şart koştuğu veya firma politikası olarak belirlenmiş olan bir sipariş katsayısı varsa belirlenmesi ve sipariş politikası olarak "Sabit Sipariş Büyüklüğü" seçilmesi gerekir. Gerektiği kadar sipariş verilebiliyorsa, bu değerin 0 (sıfır) olarak bırakılması ve sipariş politikası olarak "Kesikli Sipariş Miktarı" seçilmesi gerekir. Özellikle mamul ve yarı mamullerde istenilen miktarlarda üretim mümkün olacağı için, kesikli sipariş miktarının belirlenmesi gerekir.

Sipariş politikası, satıcı ve stok bazında Müşteri-Satıcı Stok Bilgilerinden, stok bazında Stok Planlama Kayıtlarından, Satıcı bazında Cari Planlama Bilgilerinden tanımlanır.

Herhangi bir hammadde/yarı mamul için Müşteri-Satıcı Stok Kayıtlarında sipariş politikası girilmişse, öncelikli olarak buradaki tanımlama dikkate alınır. Burada bir tanımlama yapılmamışsa, satıcının Cari Planlama Kayıtlarındaki tanımlaması dikkate alınır. Eğer burada da herhangi bir tanımlama yoksa, Stok Planlama Kayıtlarında stok bazında tanımlanan sipariş politikası dikkate alınır.

**Örneğin;**

| Stok Kodu | Parti Büyüklüğü |
| --- | --- |
| M1 | 0 (sıfır) |
| H1 | 10 Adet |
| H2 | 5 Adet |

| Seçenek | Stok Kodu | Gereksinim | İş Emri Miktarı | Sipariş Miktarı |
| --- | --- | --- | --- | --- |
| Stok Bakiye Kontrol √ | M1 | 7 | 7 |  |
| Mamul Bakiye Kontrol √ | H1 | 35-12=23 |  | 30 |
|  | H2 | 21-25=0 |  | - |
| Stok Bakiye Kontrol √ | M1 | 10 | 10 |  |
| Mamul Bakiye Kontrol | H1 | 50-12=38 |  | 40 |
|  | H2 | 30-25=5 |  | 5 |
| Stok Bakiye Kontrol | M1 | 10 | 10 |  |
|  | H1 | 50 |  | 50 |
|  | H2 | 30 |  | 30 |

şeklinde hesaplanır.

Reçetede bir yarı mamul olsaydı ve bu yarı mamulün parti büyüklüğü olsaydı, yarı mamulün üretim miktarı bire bir gereksinim kadar olmayacak ve parti büyüklüğüne göre hesaplanacaktı. Bu durumda hammadde gereksinimi de üretim miktarına göre ayarlanacaktı.

**Sipariş Oranı**

MRP ile oluşturulan satıcı siparişlerinin, bir hammadde ihtiyacı için birden fazla satıcıya oranlanarak verilmesi için sipariş oranı kullanılır.

MRP ile, satıcı siparişlerine dönüşecek kayıtlar, Stok-Kayıt-Müşteri-Satıcı Stok Kayıtları bölümündeki "Sipariş Oranı" alanına girilen değer doğrultusunda farklı satıcılara bölüştürülür. Yarı mamullerinin bir kısmını dışarıdan temin eden, bir kısmını üreten firmalar da, bu uygulamayı kullanarak oranlama yapabilir.

MRP'de sipariş oranı konusunda dikkat edilmesi gerekenler şunlardır:

- Sipariş oranı girilmemişse veya satıcılar bazında toplam oran 100%'den az bir değer ise, geriye kalan oran, Stok Kartında "Satıcı Kodu" alanında girilen satıcıya sipariş verilir. Söz konusu stok bir yarı mamul ise, kalan oran için iş emri verilir.
- Sipariş oranları toplamı 100%'den büyük bir değer ise, bu oran kadar fazla sipariş açılır.

**Örneğin;**

Sipariş oranları toplamı 120 ise MRP'de hesaplama yapıldığında 10 adet olması gereken sipariş 12 olarak hesaplanır.

- Müşteri-Satıcı Stok Kayıtları bölümünde yarı mamul için sipariş oranı verildiyse, bu yarı mamulün satın alınacağı düşünülüp, alt seviyelerindeki hammaddeler için MRP'de planlama yapılmaz. Bu bölümde verilen toplam oranın %100'e tamamlanacak şekilde geri kalanı üretilecek miktar olarak hesaplanır ve alt seviyelerine inilerek planlaması yapılır.

Müşteri/Satıcı Stok Kayıtlarındaki sipariş politikası, nakliye süresi, bildirim süresi, yükleme günleri, kesinleşme ve planlama periyodunun MRP‘de dikkate alınması için mutlaka sipariş oranının girilmesi gerekir.

**Örneğin;**

Yukarıdaki örnekte gereksinim miktarları ile tarihlerinin ve sipariş/iş emri miktarları ile tarihlerinin hesaplanma şeklinden bahsedildi. Stok Bakiye Kontrol ve Mamul Bakiye Kontrol seçeneklerinin işaretli olduğunu varsayarak örnek aşağıdaki şekilde tamamlanabilir.

| Tarih | Stok Kodu | Gereksinim | İş Emri Miktarı | Sipariş Miktarı |
| --- | --- | --- | --- | --- |
| 01/08/2020 | M1 | 7 | - | - |
| 30/07/2020 | M1 | - | 7 | - |
| 30/07/2020 | H1 | 23 | - | - |
| 30/07/2020 | H2 | 0 (Sıfır) | - | - |
| 25/07/2020 | H1 | - | - | 30 |

**Stok ve Sipariş Bakiyeleri**

Stok kalemlerinin (Hammadde, Yarı Mamul, Mamul) gereksinimleri hesaplanırken, Stok Bakiye Kontrol seçeneği işaretli ise davranış şekli şöyledir:

Malzemenin gerektiği ilk tarihte; Malzeme Brüt Gereksinimi (Ürün reçetesinden kaynaklanan miktar) - Stok Bakiyesi (Sipariş miktarı) - Bekleyen Satıcı (İş emri miktarı) - Bekleyen İş.

Daha sonraki tarihlerde; Malzeme Brüt Gereksinimi (Ürün reçetesinden kaynaklanan miktar) - Devreden Stok Bakiyesi - Önceki Tarihten Bugüne Kadar Olan Teslimatlar.

**Örneğin;**

30/07/2020 tarihinde H1 hammaddesinin üretim için gerekli miktar 35, eldeki bakiyesi 10,

25/07/2020 teslim tarihli satıcı siparişinden bekleyen teslimatın 2 olduğu varsayıldığında,

30/07/2020 tarihinde H1 için net gereksinim = 35-10-2 = 23 adettir.

| Tarih | Stok Kodu | Üretim Miktarı | Bakiye | Sipariş Giriş | Net Gereksinim |
| --- | --- | --- | --- | --- | --- |
| 30/07/2020 | H1 | 35 | 10 | 2 | 23 |

23 adet H1'in 30/07/2020'de elde olması için 25/07/2020'de sipariş verilmesi gerektiğini ve parti büyüklüğünden dolayı bu siparişin 30 adet olması gerektiği önceki örneklerde bahsedilmişti.

| Tarih | Stok Kodu | Üretim Miktarı | Bakiye | Sipariş Giriş | Net Gereksinim | Sipariş Miktarı |
| --- | --- | --- | --- | --- | --- | --- |
| 25/07/2020 | H1 | - | - | - | - | 30 |
| 30/07/2020 | H1 | 35 | 10 | 2 | 23 |  |

Bu durumda, yapılan planlamadan dolayı 30/07/2020'de elde 30 adet daha H1 olacak. Buradaki 10 adet bakiye ile 2 adet teslimat, gerçekten var olan miktarlardır. 30 adet yeni giriş ise planlamadan oluşan giriştir.

| Tarih | Stok Kodu | Üretim Miktarı | Bakiye | Sipariş Giriş | Net Gereksinim | Sipariş Miktarı | Planlanan Giriş |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 25/07/2020 | H1 | - | - | - | - | 30 |  |
| 30/07/2020 | H1 | 35 | 10 | 2 | 23 | - | 30 |

30/07/2020'de girilmesi planlanan bu 30 adet ile birlikte elde 42 adet H1 bulunacak, bu tarihte 35 adeti sarf edilecek ve geriye elde 7 adet H1 kalacak.

| Tarih | Stok Kodu | Üretim Miktarı | Bakiye | Sipariş Giriş | Net Gereksinim | Sipariş Miktarı | Planlanan Giriş | Devir |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 25/07/2020 | H1 | - | - | ```text<br>-<br>``` | ```text<br>-<br>``` | 30 |  |  |
| 30/07/2020 | H1 | 35 | 10 | ```text<br>2<br>``` | 23 |  | 30 | 7 |

Planlamanın devamında 15/08/2020''de tekrar H1 hammaddesine gereksinim duyulduğu varsayıldığında ve gereksinim duyulan üretim miktarı da (Brüt Gereksinim) yine 35 olduğunda; 30/07/2020'den elde 7 adet H1 devredeceği bir önceki adımda planlanmıştı. Bu durumda tablo aşağıdaki şekilde olacaktır.

| Tarih | Stok Kodu | Üretim Miktarı | Bakiye | Sipariş Giriş | Net Gereksinim | Sipariş Miktarı | Planlanan Giriş | Devir |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 25/07/2020 | H1 | - | - | - | ```text<br>-<br>``` | 30 |  |  |
| 30/07/2020 | H1 | 35 | 10 | 2 | 23 |  | 30 | 7 |
| 10/08/2020 | H1 | - | - | - | ```text<br>-<br>``` | 30 |  |  |
| 15/08/2020 | H1 | 35 | 7 | - | 28 |  | 30 | 2 |

Planlamanın burada bittiği ve yukarıdaki planlama kayıtlarının oluştuğu varsayıldığında, bu plandan iki ayrı liste alınabilir. Bu planlama itibariyle, hangi tarihte ne kadar H1 sarf edilecek?

| Tarih | Stok Kodu | Üretim Miktarı |
| --- | --- | --- |
| 30/07/2020 | H1 | 35 |
| 15/08/2020 | H1 | 35 |

Bu planlama itibariyle, hangi tarihte ne kadar H1 sipariş edilecek?

| Tarih | Stok Kodu | Sipariş Miktarı |
| --- | --- | --- |
| 25/07/2020 | H1 | 30 |
| 10/08/2020 | H1 | 30 |

**Zamanlama Hataları**

İçinde bulunulan günün tarihine çok yakın girilen planlamalarda, temin sürelerinden dolayı içinde bulunulan günün öncesine sarkan gereksinim veya sipariş kayıtları oluşabilir. Program, teslimatı ya da bildirimi gecikmiş kayıtların yanına \* sembolü koyar. Bu sembol ile karşılaşıldığında, yapılan planlamanın fiziksel olarak gerçekleşmesinin olanaksız olduğunun anlaşılması gerekir.

**Örneğin;**

Yukarıdaki örneklerde yapılan planlama 01/08/2020 tarihinde M1 mamulünden 10 adet üretilmesi içindi. Eğer bu planlama 01/08/2020 tarihinde yapılsaydı, bir başka deyişle günün tarihi 01/08/2020 olsaydı, planlama sonucunda çıkan H1 hammaddesinin gereksinim ve sipariş kayıtları aşağıdaki şekilde olacaktı:

| Tarih |  | Stok kodu | Üretim Miktarı | Sipariş Miktarı |
| --- | --- | --- | --- | --- |
| 25/07/20 | \* | H1 | - | 30 |
| 30/07/20 | \* | H1 | 35 |  |
| 10/08/20 |  | H1 | - | 30 |
| 15/08/20 |  | H1 | 35 |  |

**Planlanan Bileşen Değişiklikleri**

MRP'de malzeme gereksinimlerini değiştirecek uygulamalardan biri de reçetelerde geleceğe yönelik yapılacak revizyonlardır. Üretim modülünde yer alan “Planlanan Bileşen Değişikliği” bölümünden kaydedilen revizyon bilgilerinin plana yansıtılarak gereksinim miktarlarının bu doğrultuda hesaplanması gerekir. Bunun için “Planlanan Bileşen Değişikliği” bölümünde “Plana Yansıt” butonunun kullanılması gerekir. "Plana Yansıt" butonu kullanıldığında, revizyonda tanımlanan bileşen değişiklikleri, reçetelerde gerçek anlamda geçerli olmaz ve sadece planlama için kullanılır. Bu bölümde, program revizyon numaralarını sorgulayan bir ekran görüntülenir. Bu ekranda planlamaya yansıtılacak revizyon numarasının seçilmesi ve "Yansıt" butonuna tıklanması yeterlidir. Bundan sonra planlama, yeni bileşenler üzerinden ya da eski bileşenin değişen miktarı üzerinden yapılır.

**Örneğin;**

M1 mamulünün reçetesinde bulunan 001 kodlu hammadde, 10.10.2020 tarihinde, 002 kodlu hammadde ile değiştirilir. 10.10.2020 tarihinde M1 mamulü için yapılan gereksinim planında 001 hammaddesi için değil 002 hammaddesi için ihtiyaç miktarının hesaplanması gerekir.

**Alternatif Malzeme Kullanımı**

Malzeme gereksinimlerini değiştirecek uygulamalardan diğeri ise reçetedeki bileşenler için alternatif malzeme kullanımıdır. MRP'de alternatif malzeme politikalarından sadece “Oranlar” desteklenir. Bu politikada, gerekli olan malzeme miktarı, reçetede veya alternatif tanımında belirlenen oranlara göre bulunur.

**Örneğin;**

Reçetedeki H1 hammadesi için %80, H1’in alternatifi olan H2 hammadesi için %20 oranı girildiğinde, mamul üretimi için 100 birim H1 gerekiyorsa, bunun 80 birimi H1’den, 20 birimi H2’den kullanılır.
