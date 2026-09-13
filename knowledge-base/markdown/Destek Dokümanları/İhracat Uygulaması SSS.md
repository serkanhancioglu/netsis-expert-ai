---
title: "İhracat Uygulaması SSS"
page_id: "150569744"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "İhracat Uygulaması SSS"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / İhracat Uygulaması SSS"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTg0Y2QyZGRkLWRhNGItNGJlOC04Zjg2LWZlMjI5NTc5ZDYwZCZsaW5rPTI5YjQ0MjU3LTRiMmUtNDYzYy05YTdmLWM3MTE0YTg3NTlhMSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=84cd2ddd-da4b-4be8-8f86-fe229579d60d&link=29b44257-4b2e-463c-9a7f-c7114a8759a1&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ihracat-uygulamasi-sss_150569761_150569744.html"
source_version: "2024-10-04T18:08:47.330+03:00"
source_bytes: 4527794
fetched_at: "2026-09-13T04:22:42+00:00"
generator: "netsis-scraper 1.0.0"
---
# İhracat Uygulaması SSS

**Soru** **1:** **İhracat** **Dosya** **İşlemleri** **ekranında** **Fatura** **modülünden** **girilen** **ihracat** **irsaliyelerinin** **görünmemesi** **için ne** **yapılmalıdır?**

**DISTICARET\\FATURADAKIIRSALIYEGELMESIN** özel parametresi tanımlandığında, İhracat Dosya İşlemleri ekranında Fatura modülünden girilen ihracat irsaliyelerinin görünmemesi sağlanmaktadır. Bu parametre tanımlı olmadığında, fatura modülünden girilen irsaliyeler İhracat Dosya İşlemlerinde irsaliye rehberlerinde gelecektir.

**Soru** **2:** **Dış** **ticaret** **modülünde** **DISTICARET/SAYFAYENILENMESIN** **özel** **parametresi** **ne** **işe** **yarar?**

**DISTICARET/SAYFAYENILENMESIN** özel parametresiyle, dış ticaret modülünde ihracat dosyasında gride veri getirmede dosyaya her belge bağlama işlemi sonrası güncel belgeleri getirmek için çıkan popup ekranın kullanıcı istediğinde görüntülenmesi sağlanmıştır. **Yenile** butonu eklenmiş olup, Yenile butonuna basılarak kullanıcının isteğine göre kısıt ekranı getirilmektedir.

![](../_assets/fc8fc5707ec5d9ce8b6e.png)

**Soru 3: İhracat sürecinde oluşan satış irsaliyesi sonrasında stok hareketlerinde irsaliye** **miktarının** **takip** **edilebilmesi** **için** **ne yapılmalıdır?**

Satış Fatura Parametreleri\>İhracat sekmesinde "**İhracat/İthalat** **Miktarları** **Stoklara** **Geçsin**" parametresinin işaretlenmesi gerekir.

![](../_assets/cf4e90cf382fe2d4ceaa.png)

**Soru** **4:** **İthalat/İhracat** **dosya** **işlemlerinde** **seçilen** **belgelerin** **yeni** **grid** **görünümü** **yerine,** **eski** **html** **görünümle** **görüntülenmesi** **için** **ne** **yapılmalıdır?**

**DISTICARET/HTMLGORUNUM/0** özel parametresinin tanımlanması gerekmektedir. Bu özel parametre tanımlanınca aşağıdaki html görünümü gelmektedir.

![](../_assets/bef9ed8618f7f3d0b76d.png)

**Soru** **5:** **Birden** **fazla** **ihracat** **belgesi** **veya** **dosyası için** **toplu** **olarak** **ihracat** **kapatma** **yapılabilir** **mi?**

Dış Ticaret Modülü' nde Toplu İhracat Kapatma ekranından ihracat belgelerinin toplu kapatması yapılır. Toplu ihracat kapatma yaparken aynı döviz cinsinden belgelerin bir arada kapatılması gerekmektedir.

![](../_assets/c7a560c81abe48f92c3d.png)

**Soru** **6: Serbest** **bölge** **işlem** **formu** **ile** **oluşturulan** **e-İhracat** **belgeleri** **satış** **tipli** **oluşturulabilir** **mi?**

9.0.56 seti ile serbest bölge işlem formu ile oluşturulan e-İhracat belgelerinin satış tipi ile oluşturulabilmesi desteklenmektedir.

Dış ticaret modülünden kesilen proforma faturalar gümrüğe gönderilen ve senaryo tipi IHRACAT olan e- belgeler olarak gönderimi sağlanmaktadır. Ancak 5000$ altında olan e-ihracat belgesinin gümrüğe gönderilmeden direkt müşteriye gönderilmesi ve senaryo tipinin IHRACAT olmaması için,
Toplu E-fatura Oluşturma ekranında İşlem Tipi Seçimi sekmesinde Belge Tipi "**İhracat** **Faturaları"** ve **"Dış** **Ticaret** **Modülünden** **Oluşsun** **(Proforma)"** parametreleri ile Ön Sorgulama sekmesinde "**Gümrük** **Beyannamesi** **Düzenlenmesin**" parametresi işaretlenmelidir.

![](../_assets/1126bf9b55f0843f1f71.png)![](../_assets/660f7acf60fc34e175a8.png)

"**Gümrük** **Beyannamesi** **Düzenlenmesin**" parametresi işaretlenerek taslak oluşturulması durumunda e-Fatura senaryosu ilgili carinin kartındaki e-fatura senaryosuna (Temel/Ticari) göre oluşmaktadır.

![](../_assets/fe31d5cefa7ef4cb8224.png)

**Soru** **7:** **İhracat** **e-Faturalarında** **ek** **maliyetler** **nasıl** **girilir?**

İrsaliye belgesinde kalem olarak eklenebilir.

İrsaliye belgesinde ayrı kalem olarak girilmesi durumunda; ilgili navlun ya da sigorta kalemi gride atıldıktan sonra üzerinde sağ klik yapıldığında gelen menülerden "**E-İhracat** **Alt** **Maliyet** **Kalemi** **Ekle**" seçeneği seçilir.

![](../_assets/571edbada23736f1dadb.png)

Eğer Proforma üzerinden süreç yürütülüyorsa; sigorta ve\\veya navlunun ayrı kalem olarak girilmesi durumunda, proforma belgesi düzenlenirken ilgili kalem üzerinde sağ klik yapılarak gelen menülerden "**E-ihracat** **Alt** **Maliyet** **Kalemi Ekle**" seçeneği seçilir.

![](../_assets/3f77dd77b498aed2aa53.png)

İrsaliye belgesinin toplamlar sekmesindeki Ek Maliyet-1/Ek Maliyet-2 alanlarında girilebilir.

![](../_assets/e165c4b96202d38cd193.png)

Proforma faturasında Navlun/Sigorta sekmelerinde girilebilir.

Dış ticarette Sigorta ve Navlun sekmelerinden girilen değerlerin Proforma belgesine yansıtılması için Sigorta Proformaya Eklensin/Nakliye Proformaya Eklensin seçenekleri işaretlenir. Bu durumda girilen değerler belgede Ek Maliyet-1 ve Ek Maliyet-2 alanlarına yansır.

![](../_assets/9b1434f91cdfb78e8bdb.png)![](../_assets/db4af074a7a1b85885bc.png)

**Soru** **8:** **İhracatta** **hangi** **grup** **teslim** **şekilleri** **navlun** **ve** **sigorta** **tutarları** **ihracat kapatmaya** **dahil** **edilmezler?**

İhracatta "E" ve "F" grubu teslim şekillerinde (EXW, FOB,FCA,FAS,vb..), navlun ve sigorta alıcıya aittir. Diğer "C" ve "D" grubu teslim şekillerinde navlun ve sigorta satıcıya aittir. Bu nedenle Dekont Modülünden EXW, FOB, FCA, FAS teslim şekli olan İhracat Kapatmalarda navlun ve sigorta kısımları pasif gelir. Dış Ticaret Modülünde; "E" ve "F" grubu teslim şekillerinde (EXW, FOB,FCA,FAS,vb..), ihracat dosyası içinde navlun ve sigorta girişlerine izin verip, ihracat kapatma ekranında da bu alanlar aktif gelmesine rağmen, kapatma sonrası bu tutarlar dahil edilmezler.

**Soru 9: İhracat Dosya İşlemlerinde, Taslak Fatura üzerinde, daha önceden dosya carisi için** **tanımlanmış acenta, taşıyıcı, sigorta, gümrük kodu, vb bilgilerin otomatik olarak gelmesi** **için** **ne** **yapılmalıdır?**

İhracat Dosyası içinde, Taslak Fatura "**Düzenle**" butonuna basılarak açıldığında **Nakliye** sekmesinde sağ click "**Ön** **tanımlı** **Cari** **Bilgilerini** **Kullan**" menüsünde basıldığında cariye bağlı girilen tüm detay bilgiler getirilmektedir.
![](../_assets/ca8ce5d58873a999fc7b.png)

![](../_assets/1959dff5f79dbad7a0aa.png)

![](../_assets/47590115b722c4838653.png)
