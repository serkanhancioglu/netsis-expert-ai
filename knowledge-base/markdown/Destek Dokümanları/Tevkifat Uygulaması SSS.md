---
title: "Tevkifat Uygulaması SSS"
page_id: "66250687"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Tevkifat Uygulaması SSS"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Tevkifat Uygulaması SSS"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWRlYmE0NGM0LWJiZTUtNDBlNi1iNmIxLTczMGM5YjRjMWZiMyZsaW5rPTZmMmQzMGIzLTQxYjEtNDhmYi05ZmNmLTI4MDgzZTFiOTJlZiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=deba44c4-bbe5-40e6-b6b1-730c9b4c1fb3&link=6f2d30b3-41b1-48fb-9fcf-28083e1b92ef&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "tevkifat-uygulamasi-sss_80088399_66250687.html"
source_version: "2022-12-07T16:07:06.670+03:00"
source_bytes: 2018760
fetched_at: "2026-09-13T04:24:24+00:00"
generator: "netsis-scraper 1.0.0"
---
# Tevkifat Uygulaması SSS

**Fatura** **belgelerinde** **tevkifat** **hesaplanması** **için** **ne** **yapılmalıdır?**

Fatura parametrelerinde ek maliyet sekmesinde Ek Maliyet-2 alanına "TEVKİFAT" yazılmalı ve Tevkifat Oranı Pay/Payda bilgisi ilgili alana girilmelidir.

![](../_assets/22b2bb757bb0b7240608.png)

Fatura Toplamlar sekmesinde TEVKİFAT alanına -1 yazıp tab tuşuna basıldığında parametrelerde belirlenen orana göre tevkifat hesaplanması sağlanacaktır.

![](../_assets/ee0a2d6d7a38eee62047.png)

**Satır** **bazında** **tevkifat** **uygulaması** **için** **tanımlama** **nasıl** **olmalıdır?**

FATURA, SATIRBAZITEVKIFAT özel parametresi tanımlaması yapılmalıdır. Parametrenin değer sahasına, Özel Kod-2'nin FATURASTSABIT view'ındaki hangi sahanın tercih edildiği bilgisi girilmelidir. Örneğin özel kod-2 girişi icin stok kartı kod-5 sahası kullanılıyor ise, özel parametrede değer sahası KOD_5 şeklinde tanımlanmalıdır.

**Çoklu** **tevkifat** **oran** **tanımlama** **nasıl** **yapılır?**

Fatura parametreleride özel kod-2 işaretli olmalıdır. Çoklu Tevkifat Oran Tanımlama ekranından da farklı oranlara göre alış ve satış hesapları tanımlanmalıdır. Fatura üst bilgilerde ilgili özel kod-2 seçimi yapılarak çoklu tevkifat uygulaması kullanılabilmektedir.

![](../_assets/57d2b005aecf6e52c899.png)![](../_assets/10806103f8b1d8a53386.png)

**Gerekli** **tanımlamalar** **yapılmasına** **rağmen** **fatura** **toplamlarında** **tevkifat** **girilecek** **alan** **pasif** **gelmektedir.** **Neler** **kontrol** **edilmelidir?**

Satır bazı tevkifat uygulaması için özel parametre tanımlı olması durumda fatura toplamlarında tevkifat alanı pasif gelecektir. Çünkü satır bazı tevkifat uygulamasının kullanılması halinde toplam sayfasında ek maliyet 2 sahasına "-1" degeri girilmeden tevkifat tutarı hesaplanacaktır.

**Alış/Satış faturalarında KDV üzerinden hesaplanan tevkifatın ayrı bir muhasebe** **hesabına** **atılması nasıl** **sağlanabilir?**

Fatura parametrelerinde ek maliyet sekmesinde "KDV hesabı tevkifata göre detaylandırılsın" parametresi işaretlenmelidir. Aşağıdaki gibi Tevkifat Kdv hesap kodları tanımlanmalıdır.

![](../_assets/9e10cdb5975a77a5e7d8.png)![](../_assets/77d3a839c4455b684090.png)

**Serbest meslek** **makbuzunda** **tevkifat** **destekleniyor** **mu?**

Serbest Meslek Makbuzu'nda Çoklu Tevkifat desteklenmektedir. Tevkifat Kodu alanından seçilen tevkifat oranlarına göre belge bazında farklı tevkifatlar hesaplatılabilmektedir. Her belgede aynı tevkifat oranının kullanılması durumunda DEKONT\\TEVKIFAT özel parametresi tanımlanarak Değer alanına sabit olacak tevkifat oranı girilebilir.
![](../_assets/11e86692aaa9fbeacafa.png)

FATURA\\SATIRBAZITEVKIFATISARETSIZ özel parametresi tanımlanmalıdır.

**Tevkifatlı** **fatura** **işlenirken** **"Yapılamadı"** **uyarısı** **alındığında** **ne** **yapılmalıdır?**

Fatura parametrelerinde KDV hesabı tevkifata göre detaylandırılsın parametresi işaretli olmasına rağmen muhasebe hesaplar tanımlı olmayabilir.

**Faturalarda** **tevkifat** **tanımlaması** **olmasına** **rağmen** **tevkifat** **hesaplanmamaktadır?**

Fatura parametrelerinde ek maliyet sekmesinde Ek Maliyet -2 alanında TEVKİFAT yazılması gerekirken TEVKIFAT yazılmış olabilir. Belge tutarı fatura parametreleri ek maliyet sekmesinde tanımlanan fatura alt limitinin altında kalıyor olabilir.

**Cari** **bazında** **tevkifat** **hesaplatılabilir** **mi?**

Fatura parametrelerinde ek maliyet sekmesinde Tevkifat Cari Bazında Hesaplansın parametresi işaretlenmelidir. Cari hesap cari kartttaki hangi Alfasayısal kullanıcı tanımlı sahanın kullanılacağı belirtilmelidir. Örneğin Alfasayısal kullanıcı tanımlı saha 1 kullanılacaks KULL1S seçilmelidir.. Cari karttta belirtilen Kullanıcı Tanımlı saha E ise tevkifat hesaplanacak, H ise tevkifat hiç hesaplanmayacaktır.

![](../_assets/14b75b73d5601c6edc7e.png)
