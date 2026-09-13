---
title: "İhracat e-Fatura Uygulaması"
page_id: "34213486"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "İhracat e-Fatura Uygulaması"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / İhracat e-Fatura Uygulaması"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTQ4YTExNzRiLTc4MmItNGVjMC05MWIxLWE4YTA4ZDljMTI4NCZsaW5rPTAyOTEwNGJkLTJiMGMtNGRkYy1iMDdmLTEzMGI2Y2Q4ODdjNCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=48a1174b-782b-4ec0-91b1-a8a08d9c1284&link=029104bd-2b0c-4ddc-b07f-130b6cd887c4&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ihracat-e-fatura-uygulamasi_82575557_34213486.html"
source_version: "2022-11-03T09:11:03.767+03:00"
source_bytes: 2084120
fetched_at: "2026-09-13T04:25:45+00:00"
generator: "netsis-scraper 1.0.0"
---
# İhracat e-Fatura Uygulaması

İhracat e-Fatura Uygulaması ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

#### Genel Uygulama

İhracat e-fatura uygulaması, ihracat e-fatura uygulamasına kayıtlı bulunan mükelleflerin ihracat faturalarının da e-fatura olarak düzenlemesine zorunluluk getirilmesiyle kullanılacak olan uygulamadır.

İhracat e-Fatura Uygulaması'nın kurulumu aşağıdaki gibidir:

- Netsis 9.0.5 ile beraber, Netsis Entegre paketini kullanan müşterinin dekont modülünde "İthalat – İhracat İşlemleri Lisansı" bulunması gerekmektedir. Netsis Standart veya Enterprise paketi kullanan müşterilerin dış ticaret modülü lisansı bulunması gerekmektedir.
- Bu lisanslar ile beraber e-fatura parametreleri içerisinde bulunan "İhracat Faturaları E-Fatura Olarak Oluşturulsun" parametresi aktif olarak gelir.

![](../_assets/9dbd6d7ee565b0024f53.png)

- Ardından bu ekranda "İhracat Faturaları Belge Birim Kodlarınızı Buradan Girebilirsiniz" yazısı üzerine tıklayarak açılan çoklu seri giriş ekranı içerisinde "Belge Birim Kod" belirlenebilir.

#### ![](../_assets/8715840b9d0fc52ffe3d.png)
Tanımlamalar

İhracat e-fatura kullanmadan önce; **Lojistik/Satış-Fatura-Kayıt-E-Fatura İşlemleri-Paket Tanımları** ya da **Lojistik–Satış-Dış Ticaret-Kayıt-Paket Tanımları** ekranından Paket koduna ait "Paket Markası" ve "Paket Cinsi" tanımlamaları yapılmalıdır.

#### ![](../_assets/2082cf6be52dc572a1db.png)
Lojistik/Satış-Fatura-Kayıt-E-Fatura İşlemleri-Ödeme Açıklamaları ya da Lojistik/Satış-Dış Ticaret-Kayıt-Ödeme Açıklamaları ekranından Ödeme tipine ait "Uluslararası Ödeme Kodu" tanımlaması yapılmalıdır.
![](../_assets/ad181a059144a3a7581f.png)
Kullanım

İhracat e-fatura kullanımı Fatura ya da Dış Ticaret modülü kullanılarak iki farklı şekilde yapılabilir.

Fatura Modülünden e-İhracat faturası oluşturmak için gerekli bilgiler aşağıdaki şekildedir:

- İhracat e-fatura süreci satış irsaliyesinden başlar. (Lojistik/Satış\>Fatura-Kayıt-Satış İrsaliyesi) Satış İrsaliyesi girerken ihracat e-faturası serisi kullanılır. Bu seri ile birlikte ithalat/ihracat tipli irsaliye oluşturulur.
- Oluşan irsaliyenin toplamlar sekmesinde "E-Devlet Özel/İstisna Kodu:301" olarak atılacaktır. Bu adımdan sonra ekranda sağ tık sonrası "İhracat Bilgileri'ne" girilerek çeki listesi oluşturulur.

![](../_assets/c74b613a9a555f6a4e55.png)

- Oluşturulan irsaliyelerde "Ödeme Şekli", "Nakliye Tipi", "Gümrük Tarife Kodu (GTİP)" ve "Paket Tipi" tanımlamalarının yapılması **zorunludur.**
- İhracat Bilgileri ekranında stok koduna çift tıklanarak paket tipi girilebilecek olan ekran açılır. Bu ekranda stok parçalı ya da bir bütün olarak paketlenebilir.

![](../_assets/5f5c73fe1c7d12929c8d.png)

- İhracat bilgileri ekranı kapatıldıktan sonra "Tamam" butonu ile irsaliye tamamlanır. İhracat e-fatura taslağı oluşturulmamış irsaliyelere ait ihracat bilgileri yine bu ekrandan değiştirilebilir.

![](../_assets/49794c1a33dcfdac52b5.png)

Fatura Modülünden e-İhracat faturası oluşturulurken dikkat edilmesi gerekenler aşağıdaki şekildedir:

- Çeki listesi oluşturulmayan ihracat e-faturası oluşturulamaz.
- Kalem bilgilerine girilen tüm stoklar için Gümrük Tarife Kodu (Stok Kartı-Ek Bilgiler-Gümrük Tarife Kodu) tanımlı olmak zorundadır. GTİP'siz stok girilmiş ise kalem silinip tanımlama sonrasında girişi tekrar yapılmalıdır.

Dış Ticaret Modülünden e-ihracat faturası oluşturmak için gerekli bilgiler aşağıdaki şekildedir:

- İhracat e-fatura süreci proforma fatura oluşturma ile başlar. (Lojistik–Satış-Dış Ticaret-İşlemler-İhracat İşlemleri-Dosya İşlemleri-Siparişlerim-Proforma Oluştur)
- Proforma fatura numarası girerken ihracat e-faturası serisi kullanılır.

![](../_assets/bf135beb734947610825.png)

- Oluşturulan proformanın Detay Gösterme ekranında, "Gümrük Tarife Kodu (GTİP)", "Nakliye Tipi", "Ödeme Şekli" ve "Paket Tipi" tanımlamalarının yapılması **zorunludur.**
![](../_assets/58918d4b12f859fa2760.png)

**Gümrük Tarife Kodu (GTİP):** Stoklara ait gümrük tarife kodları stok kartından gelebilir. Stok kartında tanımlı değilse, "Detay Gösterme-Kalem Bilgileri-Sağ tık-Gümrük Tarife Kodu Değişikliği" ile mevcut GTİP değiştirilebilir ya da yeni atama yapılabilir.

**Nakliye Tipi:** "Detay Gösterme-Nakliye-Nakliye Tipi" alanından doldurulur.
![](../_assets/62e53f8291e8a95de121.png)
**Ödeme Şekli:** "Detay Gösterme-Ödeme Bilgileri-Ödeme Şekli" alanından doldurulur.

![](../_assets/84fc0d842131652e6ffe.png)
**Paket Tipi:** "Detay Gösterme-Çeki Listesi-Paket Tipi" alanından doldurulur.
![](../_assets/7e18f4af470267e2528a.png)
e-ihracat Faturası Oluşturmak için aşağıdaki adımlar izlenir:

- Satış irsaliyesi oluşturulduktan sonra, toplu e-fatura oluşturma işlemi ile ihracat e-fatura taslağı oluşturulur. Belge tipi "İhracat Faturaları" olarak seçilmelidir.![](../_assets/c53d471e42eecba15a3a.png)
- Dış ticaret modülü kullanılıyorsa, toplu e-fatura oluşturma işlemi ile ihracat e-fatura taslağı oluşturulmalıdır. Belge tipi "İhracat Faturaları" olarak seçilmeli fakat "Dış Ticaret Modülünden Oluşsun (Proforma)" parametresi işaretlenmelidir. Böylece proforma faturalar listelenmesi sağlanır.

![](../_assets/9ad296dfafae26804dc4.png)

- Ön ekrandaki seçime göre faturalar listelenir.
![](../_assets/7525ea00d519094c7aeb.png)
- Taslağı oluşturulan faturalara; Gümrük ve Ticaret Bakanlığı'nın bilgileride otomatik olarak eklenir. Girişi yapılan "Ödeme Şekli", "Nakliye Tipi", "Gümrük Tarife Kodu (GTİP)" "Paket Tipi" bilgileri de oluşan XML içeriğinde gönderilir.
- GİB'e gönderilen e-fatura senaryosu otomatik olarak 'ihracat faturası' tipinde olacaktır.

![](../_assets/d6a23d1fbc309913da82.png)

![](../_assets/96562422f291c95bbf4d.png)

"Giden kutusu zarf bazında" ekranında, sistem yanıtlarına "GTB REF NO", "GTB GÇB TECİL NO" ve "GTB FİİLİ İHRACAT TARİHİ" alanları eklenmiştir. Bu alanlar; Gümrük Ticaret Bakanlığı ve GİB'den gelen uygulama yanıt zarfı içerisinde gelen bilgiler ile dolacaktır.

Fatura gönderildiğinde öncelikle teknik kontrolleri yapılacak ve bu kontrollerde herhangi bir sorun tespit edilmezde GİB den dönecek olan "sistem yanıtı" zarfında aynı zamanda takip numarası olarak kullanılacak olan referans numarası bilgisi de gelecektir. Netsis Zarf (Giden Kutusu) ekranında bu bilgi yanıt zarfı bölümünden takip edilebilir.

![](../_assets/84345b7b1e50394b5a96.png)
Aynı zamanda GTB nin e-fatura portalından da bu bilgi kontrol edilebilir.

![](../_assets/bfbc29143d1d28317398.png)

Eğer ihracat işlemlerinde herhangi bir sorun tespit edilmezse GTB gönderdiğimiz zarfı onaylayarak "uygulama yanıtı" dönecektir ve bu uygulama yanıtının içinde Netsis ihracat faturasının kapatmasında kullanılacak olan Gümrük Çıkış Beyanname numarası ile birlikte Fiili ihracat tarihi bilgisi gelecektir.

**GTB REF NO:** Gümrük Bakanlığı'ndan gelen 23 haneli Referans numarasıdır.

**GTB GÇB TECİL NO:** Gümrük Çıkış Beyannamesinin Tescil Numarasıdır. Kabul tipi uygulama yanıtlarında zorunludur.

**GTB FİİLİ İHRACAT TARİHİ:** İhraç mallarının gümrük çıkış kapısından çıktığı tarihtir. Kabul tipi uygulama yanıtlarında zorunludur.

Ancak uygulama yanıtı kabul geldiğinde ihracat kapatma işlemi yapılabilecektir. Uygulama yanıtı olarak ret cevabı geldiğinde yeni bir satış irsaliyesi ile ihracat e-faturası yeniden oluşturulması gerekir.

İhracat firmasının gönderdiği zarfları Gümrük bakanlığı yetkilileri red edebildiği gibi süreci hızlandırmak için ihracat firmasının yetkilileri de sorun tespit edilebilecek faturaları GTB'nin portalından red edebileceklerdir.

#### ![](../_assets/994d3e50eb7d20ee739e.png)

Dizayn

Dizaynda tanımlanabilecek yeni XML etiketleri (tag) ise aşağıdaki gibidir:

![](../_assets/e71635efcd16041bc87c.png)

InvoiceLine-DeliveryAddress-StreetName: Teslim adresi sokak adı bilgisidir. InvoiceLine-DeliveryAddress-BuildingName: Teslim adresi bina adı bilgisidir. InvoiceLine-DeliveryAddress-BuildingNumber: Teslim adresi bina numarası bilgisidir. InvoiceLine-DeliveryAddress-CityName: Teslim adresi il bilgisidir. InvoiceLine-DeliveryAddress-PostalZone: Teslim adresi posta kodu bilgisidir. InvoiceLine-DeliveryAddress-CountryName: Teslim adresi ülke bilgisidir. PaymentTerms-Note: Ödeme bilgileri not alanıdır. PaymentTerms-PenaltySurchargePercent: Ödeme bilgileri ceza ücreti bilgisidir. PaymentTerms-Amount: Ödeme bilgileri tutar bilgisidir. PaymentTermsPenaltyAmount: Ödeme bilgileri ceza tutarı bilgisidir. PaymentTerms-PaymentDueDate: Ödeme bilgileri ödeme tarihi bilgisidir. BuyerCustomerParty-PartyTaxScheme-Registration: Müşteri vergi dairesi bilgisi girilir. BuyerCustomerParty-PartyTaxScheme-CompanyID: Müşteri vergi numarası bilgisi girilir.
