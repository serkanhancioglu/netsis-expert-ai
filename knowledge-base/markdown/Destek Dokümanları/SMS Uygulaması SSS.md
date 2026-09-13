---
title: "SMS Uygulaması SSS"
page_id: "111247831"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "SMS Uygulaması SSS"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / SMS Uygulaması SSS"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTc0NTExN2MwLTcyZjMtNDQ5Yy1hYzk3LTlkNzA5YTYzMTAxNSZsaW5rPTFlYTMwNDdiLThiNzQtNDgyNi04NzA3LWZkMzBhNjk0ZTRlMyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=745117c0-72f3-449c-ac97-9d709a631015&link=1ea3047b-8b74-4826-8707-fd30a694e4e3&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "sms-uygulamasi-sss_111247850_111247831.html"
source_version: "2023-05-05T16:20:05.253+03:00"
source_bytes: 3194176
fetched_at: "2026-09-13T04:23:27+00:00"
generator: "netsis-scraper 1.0.0"
---
# SMS Uygulaması SSS

**Soru** **1:** **Netsiste** **SMS** **uygulaması** **ile** **neler** **yapılabilir?**

- Firmalar, müşterilerine gönderecekleri SMS' ler ile doğum günü ve bayram kutlamaları yapabilir, kampanyaları ya da yapacakları toplantı ve seminerler hakkında bilgi verebilirler.
- Oluşturulan şablonları kullanarak müşterilere, bayi ve iş ortaklarına toplu olarak SMS gönderimi yapılabilir.
- Program içinde gerçekleştirilen bazı işlemler sonucunda otomatik olarak müşterilerine/iş ortaklarına SMS gönderimi yapılabilir.
- Örneğin satış faturası kesildiğinde, fatura bilgileri otomatik olarak SMS ile gönderilebilir. Girilen satıcı siparişlerinin tedarikçi firmaya SMS ile gönderilmesi veya yapılan bir fiyat değişikliğinin bayilere SMS ile bildirilmesi sağlanabilir.
- Müşterilerin yanı sıra, firma çalışanlarına da farklı amaçlarla SMS gönderilmesi sağlanabilir. Örneğin, sistemdeki bir faturanın, kullanıcı tarafından iptali halinde, bu bilginin departman müdürüne SMS ile gönderilmesi mümkündür.

**Soru 2: SMS gönderimi kim tarafından yapılır? SMS gönderimi için ayrı bir lisans** **alınmalı** **mıdır?**

Netsis SMS uygulamasıyla; SMS' ler e-Logo' ya gönderilir, SMS gönderimleri e-Logo tarafından yapılır. SMS uygulaması ürün ile birlikte ücretsiz verilir. Atılacak SMS' ler için kontör satın alınmalıdır. Kontör almak ve servis sağlayıcı ile sözleşme için e-Logo' ya başvurulmalıdır.

**Soru** **3:** **Netsiste** **SMS** **uygulamasının** **kullanılabillmesi** **için** **ne** **yapılmalıdır?**

SMS uygulamasının kullanılabilmesi için öncelikle Yardımcı Programlar modülünde Kayıt menüsü altında Netsis SMS Servisi menüsünde bulunan **SMS** **Parametreleri** ekranından gerekli tanımlamaların yapılması gerekmektedir. Bu ekrandaki parametreler aşağıda açıklanmıştır.

**SMS** **uygulaması** **var:** SMS uygulamasının program genelinde aktif hale getirilmesi için işaretlenmesi gereken parametredir.

**SMS** **Kullanıcı** **Adı:** e-Logo'dan alınan kullanıcı adının girileceği alandır.

**SMS** **Şifre:** e-Logo'dan alınan şifrenin girileceği alandır.

Gönderici Parametreleri bilgileri yine e-Logo tarafından temin edilecektir.

**Gönderen** **(Orijinator):** SMS' in kim tarafından gönderildiği bilgisinin tanımlanacağı sahadır.

**Gönderen Tel No:** SMS' in hangi telefon numarası tarafından gönderileceği bilgisinin tanımlanacağı sahadır.

Gerekli tanımlamalar yapılıp **Tamam** butonuna basılır.

![](../_assets/47161b9a70f86f47ee13.png)

**Soru** **4:** **Olay** **bazlı** **SMS** **gönderimi** **nasıl** **yapılır?**

Program içinde yapılan bazı işlemler sonrasında otomatik olarak SMS gönderilmesi mümkündür. Bunun için öncelikle hangi cari hesaba, hangi işlemlerden sonra otomatik olarak SMS gönderileceğinin belirlenmesi gerekmektedir.

Cari hesaplara ait cep telefonu numaraları ve SMS işlem seçimi Cari modülünde bulunan **Cari İrtibat** **Bilgileri** bölümünden yapılmaktadır. Olay Bazlı SMS Gönderimi ekranında seçilen işlemler sonrasında cari hesaba ait cep telefonuna otomatik olarak SMS gönderilecektir.

**Soru** **5:** **Örneğin,** **program** **içinde** **müşteri** **siparişi** **girilen** **cariye** **sipariş** **bilgilerinin** **SMS** **yoluyla** **gönderilmesi** **için** **ne yapılmalıdır?**

**Cari** **İrtibat** **Bilgileri** ekranında, **İrtibat** **bilgileri** sekmesinde cariye ait cep telefonu bilgisi girilmeli,

**Eposta/SMS** **Tanımlamaları** sekmesinde yer alan listede Müşteri Siparişi işaretlenmelidir.

![](../_assets/1868ecce36313c94b76d.png)
![](../_assets/5530c7734f37a6342e18.png)

Böylece, sipariş girişinde ayrıca herhangi bir işleme gerek olmadan SMS gönderilebilecektir.

![](../_assets/4832a5e995871ae2dcec.png)
![](../_assets/980c5db8bc0fc29aa4cb.png)

**Soru 6: Carilere gönderilecek SMS' ler için şablon tanımlaması nasıl yapılır? Bu şablona** **göre** **SMS** **nasıl gönderilir?**

Finans\\Cari\\Raporlar\\Ek Listeler**Mektup** **SMS** **Gönderme** ekranında SMS şablon tanımlamasının yapılacağı SMS Şablon Oluşturma sayfası gelir. SMS şablon metni girilmeden önce, şablonun ismi ve kaydedileceği dizin belirlenmelidir. Bunun için Mektup Adı sahasındaki Mektup Bul butonu kullanılabilir. Mektup Bul butonuna basıldığında, Dosya Aç menüsü gelir. Burada dosyanın saklanacağı dizin seçilip **KMS** uzantılı bir dosya ismi verilir. Program, SMS şablonunu bu isimle saklayacak, ileride bu isimdeki SMS şablonu çağırılarak izlenebilecek, gönderilebilecek ve üzerinde değişiklik yapılabilecektir.

![](../_assets/daee8feaaec628777a68.png)![](../_assets/76a578213cdc0212004f.png)

SMS şablonunda her cari hesap için değişkenlik gösterecek bilgiler ekranın alt kısmında "**Sahalar**" bölümünde listelenmiştir. Bu bilgilerden hangileri isteniyorsa, ilgili saha tıklanarak mesaja taşınabilir. Mesajda sabit olacak bilgiler manuel girilmelidir. Şablona girilen metinlerde karakter sayısı 160'ı geçmemelidir.

Şablon tamamlandıktan sonra **Tamam** butonuna basılır. Mektup Adı kısmında dizini verilmiş olan dosyaya bu şablon kopyalanacaktır. SMS gönderilecek cari seçimi yapılır ve gerekli parametreler işaretlendikten sonra **Rapor** butonuna basılır ve kısıtlara uyan sonuçlar listelenir. Mesaj gönderimi yapılır. İşlem tamamlandığında da "**Mesajlar** **e-Logo'ya** **iletildi.**" uyarısı gösterilir.

![](../_assets/0b51d5d6a821e1067756.png)
![](../_assets/6d8b34b42f4c9d8293ff.png)![](../_assets/9bf7800e0232dc4f70b3.png)![](../_assets/56ed42e17a19871f8262.png)

**Soru** **7:** **Netsiste** **serbest** **SMS** **nasıl** **gönderilir?**
Yardımcı Programlar modülü Kayıt menüsü altında Netsis SMS Servisi menüsünde **Serbest** **SMS** **Gönderme** ekranında istenen herhangi bir metin serbest olarak girilerek ve burada belirlenen telefonlara gönderilir.
**Bakiye** **Sorgula:** SMS parametrelerinde tanımlanan hesap bilgilerinin ve kalan kontör sayısının gösterildiği ekrandır.
![](../_assets/c8e39d028b53aa8c2146.png)
Mesajınızı giriniz kısmına mesaj olarak gönderilmek istenen metin girilir.
**Gönderim zamanı belirtiniz:** Mesajın hemen mi yoksa belirtilen tarihte mi gönderileceğinin belirlendiği bölümdür.
**Mesaj gönderilecek numaraları giriniz:** Gönderim yapılacak bilgilerin girildiği bölümdür. Bu bilgiler ekrandan elle girilebileceği gibi hazır bir excel dosyasından, önceden kaydedilmiş bir şablondan veya cari irtibat bilgileri ekranından getirilebilir.
**Yeni Şablon:** Gönderim yapılacak telefon numaraları gruplanıp "Yeni Şablon" butonu ile kaydedilebilir. Bir sonraki gönderimde bu şablon seçilerek daha önceden kaydedilen bu numaraların ekrana otomatik olarak getirilmesi sağlanır. Böylece aynı tip mesajlar için aynı gruptaki numaraların tekrar tekrar girilmesine gerek kalmaz.
![](../_assets/b2430259508f0101840c.png)
Kaydet butonuna basıldığında aşağıdaki bilgi mesajı ekranı gelerek SMS telefon listesi şablonu kaydedilir.
![](../_assets/1592700c276f7b8a7aac.png)
**Telefon:** SMS' in gönderileceği telefon numarasının girileceği sahadır. Telefon numarası, başında sıfır olmadan 10 karakter uzunluğunda girilmelidir. Yanlış formatta girildiğinde program tarafından uyarı verilmektedir.
![](../_assets/02128bb5e24c3c3a27d2.png)

Mesaj bilgisi, SMSin iletileceği telefon girişleri sonrasında Gönder butonuna basılarak SMS gönderimi yapılmaktadır. SMS gönderimi sonrasında **Mesajlar** **e-Logoya** **iletildi** uyarısı ekrana gelir.
![](../_assets/9a8ff8ceb072b775a3b5.png)
![](../_assets/e22629343e3b4fab4ca4.png)![](../_assets/2d77e733cd6a4277ec63.png)
