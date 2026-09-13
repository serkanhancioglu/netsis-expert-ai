---
title: "Sipariş Bazında Rezervasyon Sistemi"
page_id: "50684713"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Sipariş Bazında Rezervasyon Sistemi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Sipariş Bazında Rezervasyon Sistemi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWZjMmE4NWFkLWJiMTYtNGNmZi04MzhlLTg5NTk1NmU5ZjgyMiZsaW5rPTc1NmUxYjFiLTg2YzEtNDhjOS05NjM4LTkyYjBkNGM1M2Y5NyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=fc2a85ad-bb16-4cff-838e-895956e9f822&link=756e1b1b-86c1-48c9-9638-92b0d4c53f97&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "siparis-bazinda-rezervasyon-sistemi_90669645_50684713.html"
source_version: "2022-11-03T09:58:24.117+03:00"
source_bytes: 3342849
fetched_at: "2026-09-13T04:26:36+00:00"
generator: "netsis-scraper 1.0.0"
---
# Sipariş Bazında Rezervasyon Sistemi

Sipariş Bazında Rezervasyon Sistemi ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

MRP sistemi, tüm hesaplamalarını müşteri siparişleri ile ilişkilendirerek yapacak şekilde revize edilmiştir.

Yeni MRP'de aşağıdaki yenilikler sağlanmıştır:

- Halihazırda iş emirlerine yapılan malzeme rezervasyonları dikkate alınmakla birlikte, serbest malzeme stokların kullanımı da kendi içinde yine müşteri siparişleri ile ilişkilendirilmektedir.
- Halihazırda iş emirlerine rezerve edilmiş malzemeler ile müşteri sipariş bağlantılı olarak açılmış iş emirlerinin MRP çalışması sırasında öne giren bir başka siparişle ilişkilendirilmemesi ve araya giren müşteri siparişleri için yeni ihtiyaçlar çıkarılması sağlanmıştır.
- İş emirlerine ya da müşteri siparişlerine istinaden yapılan ÜSK ile mamul ambarına girmiş ve henüz teslim edilmemiş mamullerin, kendi müşteri siparişi dışında herhangi bir başka siparişe teslimat olarak önerilmemesi sağlanmıştır.
- Sipariş bağlantılı DAT ile mamul ambarında müşteri siparişlerine rezerve edilen mamullerin de yine aynı şekilde bir başka siparişe teslimat olarak önerilmemesi sağlanmıştır.
- Varsa serbest mamul stokları yeni gelen siparişlerle ilişkilendirilmekte, yoksa yeni ihtiyaçlar çıkarılmaktadır.
- Çıkan ihtiyaçlar için önerilen ve istenirse otomatik olarak açılabilen iş emirleri ve tedarikçi siparişleri de müşteri siparişleri ile ilişkilendirilir (rezerve edilir).
- Eğer üretim şekli itibariyle alt seviye malzeme ve bazı yarı mamullerin müşteri siparişi bazında ayırt edilmeden kümüle olarak tedariği veya üretilmesi gerekiyorsa, bu bileşenler için kümülasyon desteği de sağlanmıştır.

Parametreler:

Uygulamanın aktif hale gelebilmesi için MRP modül parametrelerinden "Sipariş Bazında Rezervasyon Sistemi" seçilmiş olmalıdır.

Sipariş satırı bazında satıcı siparişi ve iş emri parametreleri otomatik işaretli gelecek, değiştirilemeyecektir. Satıcı siparişinde müşteri sipariş numarasının yazılacağı saha belirlenmelidir.

![](../_assets/5b6c7abb0e73b42940d8.png)

**Örnek Uygulama-1**

STOK_1 ve STOK_2 mamullerine ait reçeteler aşağıdaki gibidir:

![](../_assets/612d9f9c555a5c8970dd.png)

![](../_assets/fbd3401dba20ebb0eb6f.png)

Reçetelerdeki bileşenler için stok planlama kayıtları aşağıdaki gibidir:

| **Stok** **Kodu** | Politika | **Min.Sipariş**<br>**Mik.** | **Parti**<br>**Büyüklüğü** | **Nakliye**<br>**Süresi** | **Yükleme** **Günü** |
| --- | --- | --- | --- | --- | --- |
| Hammadde7 | Kesikli | 50 | - | 1 | - |
| Hammadde8 | Sabit | 50 | 50 | 1 | - |
| Hammadde9 | Sabit | 200 | 100 | 2 | - |

27.08.2020 tarihinde girilmiş iki adet müşteri siparişi aşağıdaki gibidir:

| **Müşteri** **Sipariş** **No** | **Cari** **Kodu** | **Sip.** **Tarih** | **Sip.** **Teslim**<br>**Tarih** | **Stok** **Kodu** | Miktar |
| --- | --- | --- | --- | --- | --- |
| MM0000000000052 | D001 | 26.08.2020 | 10.09.2020 | STOK_1 | 500 |
| MM0000000000052 | D001 | 26.08.2020 | 09.09.2020 | STOK_2 | 750 |
| MM0000000000053 | D001 | 26.08.2020 | 10.09.2020 | STOK_1 | 250 |
| MM0000000000053 | D001 | 26.08.2020 | 13.09.2020 | STOK_2 | 350 |

İlgili siparişleri içerecek şekilde öncelikli olarak Gereksinim Planlama işlemi çalıştırılır. Ardından Malzeme Gereksinim Planlama aşağıdaki parametrelere göre çalıştırılarak ihtiyaçlar belirlenir.

![](../_assets/ffc84a1bd35354f1cb11.png)

![](../_assets/b487b57e210397b1c9ed.png)

Elde edilen MRP sonucuna göre ortaya çıkan satıcı siparişleri ve iş emri önerileri dengeleme ekranlarından aşağıdaki gibi izlenebilir.

![](../_assets/a7437c8207540ccccd7e.png)

![](../_assets/f930b38a9e0d89bd354e.png)

Stok planlama kayıtlarında **parti** **büyüklüğü** **ve** **minimum** **sipariş** bilgisi yer alan stokların müşteri siparişlerindeki teslim tarihlerinin aynı ya da farklı olduğuna bakılmaksızın fazla ihtiyaç çıkarmamak adına kümülasyon işlemi otomatik yapılmaktadır. Kümülasyon işlemi yapılırken Yükleme Günü alanındaki bilgiye göre kümülasyon gerçekleşmektedir. Bu nedenle de HAMMADDE8 için MM0000000000052 ve MM0000000000053 siparişlerinde ayrı ayrı 250 ve 500'lük ihtiyaçlar çıkarmak yerine Yükleme Günü "Gün" olarak belirtilmesinden dolayı aynı güne kümüle ederek 750 adetlik ihtiyaç çıkarmıştır.

HAMMADDE9 ve HAMMADDE7 için ise yine yukarıdaki nedenlerden dolayı Yükleme Günü "Gün" olarak belirtildiği için ilgili stokların Teslim Tarihlerine göre kümülasyon işlemi gerçekleşmiştir. Buna göre stok planlama kayıtlarında HAMMADDE9 için 200 adetlik parti büyüklüğü tanımlandığı için 52 nolu siparişin ikinci satırındaki 750 adetlik HAMMADDE9 ihtiyacına istinaden 800 adetlik satıcı siparişi çıkarıldığı görülmektedir. HAMMADDE7 içinde stok planlama kayıtlarındaki bilgilere göre farklı teslim tarihleri için ayrı ayrı 350, 750 ve 750 adetlik satıcı siparişleri ihtiyaç olarak belirlenmiştir. 52 ve 53 nolu siparişlerdeki STOK_1 satırları için teslim tarihleri (10.09.2020) aynı olmasına rağmen MRP tarafından bu satırlar için iki ayrı iş emri müşteri siparişi bazında açılmıştır.

**Alt Seviye Yarı Mamul ve Malzemeler için Kümülasyon**

Tamamen müşteri siparişi detayında çalışan yeni MRP sisteminde (sipariş bazında rezervasyon), tedarikçilere verilecek siparişlerde veya üretilecek yarı mamullerde satıcı siparişlerinin ve iş emirlerinin bu detayda açılması istenmeyen malzeme ve yarı mamullerde kümülasyon yapılabilmektedir. Daha önceki MRP uygulamalarında dengeleme ekranı kullanımı var ise, kümülasyon işlemi bu ekran üzerinden yapılmaktaydı. Detaylı MRP uygulaması ile dengeleme ekranında kümülasyon işlemi yapmaya gerek kalmamaktadır, program bu işlemi MRP çalıştırma aşamasında otomatik yapmaktadır.

Stok bazında kümülasyon yapılacak (sipariş bazında takip edilmeyecek) stoklar için Stok modülü altında stok planlama kayıtlarında Planlama-2 sekmesinde "Satıcı Sipariş ve Planlama Yöntemi veya İş Emri ve Planlama Yöntemi" seçeneğinin "Sipariş bazında değil" şeklinde seçilmesi gerekmektedir.

Öte yandan hammaddelerin ya da mamullerin tümü için kümülasyon yapılmak isteniyor ise, stok bazında tek tek bu parametreyi işaretlemek yerine MRP parametrelerinde yer alan iş emirlerinin/satıcı siparişlerinin müşteri sipariş satırı bazında planlanması parametrelerini kapatmak yeterli olacaktır.
![](../_assets/540731f54688ff237b7d.png)

Kümülasyon yapılması istenen malzeme ve yarı mamuller için ne şekilde kümüle edilmesi gerektiği, Stok Planlama Kayıtları ya da Müşteri/Satıcı Stok Kayıtlarında Yükleme Günü sahalarında belirtilir.

![](../_assets/2c1112abc1adc1fbce06.png)

Örneğin çıkan tüm ihtiyaçların ayın 1'ine kümüle edilebilmesi için Yükleme Günü, Ay/1 seçilmelidir. Her hafta Salı günü için bir kümülasyon yapılacaksa Hafta/Salı değeri girilmelidir.

![](../_assets/38ee4b89445dcfb84b94.png)

**Örnek Uygulama-2**

Örnek Uygulama-1'de verilen 52 ve 53 nolu siparişileri dikkate alınacak olursa ve STOK_1 mamülü için iş emirlerinin haftalık olarak Perşembe gününe kümüle edilmesi, HAMMADDE9 için ise satıcı siparişlerinin haftanın Perşembe ve Cuma günlerine göre kümüle edilmesini isteniyorsa aşağıdaki gibi tanımlama yapmak gerekmektedir.

| **Stok** **Kodu** | **Satıcı** **Siparişi** **ve** **Planlama**<br>**Yöntemi** | **İş** **Emri** **ve** **Planlama**<br>**Yöntemi** | **Yükleme** **Günü** |
| --- | --- | --- | --- |
| **STOK_1** | Varsayılan | Sipariş Bazında değil | Hafta/Perşembe |
| **HAMMADDE9** | Sipariş Bazında değil | Varsayılan | Çoklu Hafta/Perşembe-Cuma |

Not: Bu aşamada "Çoklu Hafta" veya "Çoklu Ay" tanımlamalarında sondan başa doğru gitmek gerekmektedir.

Örneğin; haftanın Perşembe ve Cuma günleri için tanımlama yapılacaksa ekran üzerinde ilk satırda Cuma ardından ikinci satırda Perşembe günü tanımlanmalıdır (alttaki örnek resimde görülebilir).

![](../_assets/880d322db5b7bf7df588.png)

MRP çalıştırdığımızda aşağıdaki sonuçlar ortaya çıkacaktır:

![](../_assets/7925ae8621799063fc19.png)

![](../_assets/b43b1d311fc2dffc719a.png)

Dengeleme ekranında, satıcı siparişi oluşturma aşamasına gelindiğinde farklı teslim tarihli müşteri siparişleri için ortaya çıkan HAMMADDE9 ihtiyaçları haftanın Perşembe ve Cuma günlerine denk gelen 04.09.2020 ve 11.09.2020 bildirim(yükleme) tarihlerine çıkarılmıştır (MRP raporu). Bu hammaddenin teslim tarihleri ise 2 günlük nakliye süresi sebebiyle 06.09.2020 ve 13.09.2020 olacaktır (Dengeleme ekranı).

Bu aşamada HAMMADDE9 için tanımlanmış olan 200 adetlik minimum sipariş miktarı önem kazanmaktadır. MRP sonucunda HAMMADDE9 için 720 ve 300 adetlik iki ayrı kalem ihtiyaç çıkmasına rağmen direkt olarak bu miktarlar minimum sipariş miktarına tamamlanmaz. İlgili stok kümüle edileceği için kümüle miktar üzerinden minimum sipariş miktarı kontrolu yapılır. Böylece fazladan sipariş açılmasının önüne geçilmiş olacaktır.

Dengeleme ekranında minimum sipariş miktarının 200 ve parti büyüklüğünün 100 olması sebebi ile 750 adetlik miktar 800 adete tamamlanmıştır. 300 adetlik miktar minimum siparişi ve parti büyüklüğünü karşıladığı için bu miktarda değişiklik yapılmamıştır.

![](../_assets/4220d7ce4ea0ab96dfd4.png)

Dengeleme ekranında iş emirlerinin açılması aşamasına gelindiğinde STOK_1 için açılacak iş emri için de yükleme günü (yani iş emri tarihi), haftanın Perşembe gününe denk gelen 10.09.2020 olarak belirlenmiş ve iş emri
ihtiyaçları bu tarihe kümüle edilmiştir.

**Malzeme Rezervasyonu ve Serbest Stok**

Alımı yapılan malzemeler, satıcı siparişinde müşteri sipariş numarası detayı olsa dahi henüz herhangi bir iş emrine ya da müşteri siparişine rezerve edilmiş durumda değildir. Bu malzemeler, serbest stok olarak düşünülmelidir. Serbest stoklar MRP tarafından araya giren yeni siparişler için kullanılacaktır. Sistemdeki serbest stokların MRP tarafından herhangi bir ihtiyaç yerine ilgili müşteri siparişinde kullanılması için, bu siparişe ait iş emrine rezerve edilmesi gerekmektedir.

Örneğin; MRP sonuçlarına göre satıcı siparişlerini ve iş emirlerini açtıktan sonra, kümüle takip edilen HAMMADDE9 stoğu için alış irsaliyesi ile stok girişinin yapılmış olduğunu varsayalım. YARIMAMUL3 (reçetesinde HAMMADDE9 bulunan yarımamul) için açılmış iş emirlerine HAMMADDE9 stokunu rezerve etmek için iki adet yöntem bulunmaktadır:

1-Üretim modülünde İşlemler menüsü altından "İş Emri Malzeme Talep Ekranı" yardımıyla aşağıda görüldüğü gibi ilgili iş emirlerine gerekli HAMMADDE9 miktarları rezerve edilebilir.

![](../_assets/c905051ac76150916bcb.png)

![](../_assets/617af58d468441125045.png)

2.Depolar arası transfer yardımıyla iş emrine stok rezerve edilebilir. Bu işlemin yapılabilmesi için satış fatura parametrelerinde "Üretim reçeteleri getirilsin mi?" parametresinin işaretli olması gerekmektedir.

![](../_assets/d6e09587f3b17b4f30d5.png)

Kalem bilgilerinde İş emri no alanına ilgili iş emri numarası yazılarak, Reçete Getirme fonksiyonu kullanıldığında malzemeler aynı anda hem üretim deposuna çıkmış olacak hem de ilgili iş emrine rezerve edilmiş olacaktır.
![](../_assets/de54448262028798774d.png)

Satın almada min.sipariş miktarı ve/veya parti büyüklükleri MRP, rezervasyonları yapılmış olan mevcut siparişler için rezerve stokları kullanır. Yeni siparişler için ise önce serbest stokları kullanır, yetmediği durumda yeni satıcı siparişi / iş emri önerisi getirir.

**Mamul Rezervasyonu**

Herhangi bir sipariş için açılan iş emrinden üretim sonu kaydı yapıldığında, üretilen mamul otomatik olarak ilgili iş emrinde numarası bulunan müşteri siparişine rezerve olmaktadır. Yeni siparişler için tekrardan MRP çalıştırıldığında, iş emrine bağlı üretilmiş mamul miktarı yeni siparişler için kullanılmamakta, bu siparişler için yeni iş emirleri önerilmektedir.

Sisteme aşağıdaki bilgiler yer alacak şekilde yeni bir müşteri siparişi girilir. Bu müşteri siparişi için ihtiyaç belirlenebilmesi adına Gereksinim Planlama ve Malzeme Gereksinim Planlama işlemleri çalıştırılır.

| **Müşteri** **Sipariş** **No** | **Cari** **Kodu** | **Sip.** **Tarih** | **Sip.** **Teslim**<br>**Tarih** | **Stok** **Kodu** | Miktar |
| --- | --- | --- | --- | --- | --- |
| MM0000000000054 | D001 | 28.08.2020 | 10.09.2020 | STOK_1 | 300 |
| MM0000000000054 | D001 | 28.08.2020 | 10.09.2020 | STOK_2 | 275 |

MRP sonuç raporuna göre iş emri dengelemeleri yapıldıktan sonra, 10.09.2020 tarihli STOK_2 için açılmış iş emrine ait üretim sonu kaydı girilerek STOK_2 mamülünün sisteme girişi sağlanır. Bu şekilde sisteme girişi yapılan STOK_2 mamülü 54 nolu müşteri siparişi için rezerve edilmiş olmaktadır.

![](../_assets/913dc930e0bc16f44ba1.png)

Üretim, siparişe bağlı iş emri kaydı ile gerçekleştirildiğinden dolayı yeni açılacak olan müşteri siparişleri için ihtiyaç hesaplandığında başka siparişe rezerve edilmiş miktarlar dikkate alınmayacaktır.

Aşağıdaki sipariş örneği sisteme tanımlandığında, üretim sonu kaydı gerçekleşen siparişe bağlı iş emirleri dengeleme ekranına gelmeyecektir. Bu nedenlede sistem bu sipariş için yeni bir iş emri önerecektir.

| **Müşteri** **Sipariş** **No** | **Cari** **Kodu** | **Sip.** **Tarih** | **Sip. Teslim** **Tarih** | **Stok** **Kodu** | Miktar |
| --- | --- | --- | --- | --- | --- |
| MM0000000000055 | D001 | 28.08.2020 | 14.09.2020 | STOK_2 | 300 |

![](../_assets/bf5c08b2db976f8ca9ae.png)

Not: Rezervasyon sistemi kullanıldığında, MRP çalıştırıldıktan sonra dengeleme ekranlarından iş emirleri/siparişler açılırsa sistem açılan bu belgeleri otomatikman ihtiyaç çıkarılan müşteri siparişine bağlamaktadır.

Mamullerin, elle Depolar Arası Transfer kaydı yaparak da müşteri siparişine rezerve edilebilmesi sağlanmıştır. Bunun için satış fatura parametrelerinde "DAT ve Ambar Giriş-Çıkış fişinde sipariş no sorulsun mu?" parametresinin işaretlenmesi ve DAT kaydı sırasında ilgili müşteri sipariş numarasının girilmiş olması gerekmektedir.

![](../_assets/489985c20f8b99fe20c8.png)![](../_assets/455f76cc2c883134ee05.png)

Ticari mallar için MRP çalıştırılıyorsa MRP parametrelerinde "Reçetesi olmayan stokları MGP'ye dahil et"parametresi işaretlenerek, yine aynı şekilde bu mallar için de MRP, müşteri siparişine istinaden yapılan DAT kayıtlarını rezerve edecek, başka bir müşteri siparişi için kullanmayacaktır.

Rezervasyon miktarının hesabında dikkate alınmayacak bileşenler için : Stok / Stok Planlama Kayıtları / Rezerve Miktar Hesabına Dâhil Edilmesin parametresi işaretlenmelidir.

**Asgari Limite Tamamlama**

MRP uygulamasında malzeme, yarı mamul ve mamuller için istenirse asgari stok seviyeleri tanımlanarak stokların bu seviyelerin altına düşmemesi sağlanabilir. MRP'nin hesapladığı ihtiyaçlar müşteri siparişi bağlantılı olacağından (kümülasyon yapılmadığı durumda) asgari stok seviyesine tamamlamak için açılması önerilecek satıcı siparişleri ve iş emirleri herhangi bir müşteri siparişi ile ilişkilendirilmeyerek ayrı satırlar halinde
oluşacaktır.

**Eşlenen Mevcut Belge Miktarları Arttırılsın**

MRP çalışması sırasında ekranda sorgulanan Eşlenen Mevcut Belge Miktarları Arttırılsın seçeneği ile, MRP çalışması sırasında gelen ek siparişler nedeniyle oluşacak ek ihtiyaçlar için yeni bir satıcı siparişi veya iş emri açılmaksızın, bu belgelerin miktarları arttırılabilmektedir. Ancak belge miktarının arttırılabilmesi için eğer ilgili malzeme ya da mamul kümülasyonlu ise, yukarıda anlatılan kümülasyon kurallarına göre, kümülasyonsuz (sipariş bazında) ise, sadece sipariş numarası ve satırı eşlenen belgelerde artırım yapılabilmektedir.

**İleri Tarihli Belgelerle Eşleştirme**

MRP çalışması sırasında ekranda sorgulanan bu seçenek, müşteri sipariş tarihinin öne çekildiği durumlarda MRP'nin bu müşteri siparişine ait açılmış olan ileri tarihli iş emirleri ve satıcı siparişlerinin tarihlerini geri çekmesi için kullanılır. Bu seçenek işaretlenmediğinde MRP, ileri tarihli iş emri ve satıcı siparişlerini işleme almaksızın, teslim tarihi öne çekilen müşteri siparişi için yeni ihtiyaçlar oluşturacak, ileri tarihli iş emri ve satıcı siparişlerinin ise boşa çıktıklarından dolayı iptal edilmeleri gerektiğini önerecektir.

İleri Tarihli Belgelerle Eşleştirme seçeneği işaretlendiğinde stoka üretimi yapılan (kümülasyonlu) yarı mamuller ya da satın alınan malzemeler için de MRP, öncelikle ileri tarihli iş emri ve satıcı siparişleri varsa bunları öne çekecek ve kalan ihtiyaçlar için yeni sipariş/iş emirleri açılmasını önerecektir.
