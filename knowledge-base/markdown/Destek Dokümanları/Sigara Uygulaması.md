---
title: "Sigara Uygulaması"
page_id: "104104619"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Sigara Uygulaması"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Sigara Uygulaması"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTY5ZjkxY2Q5LTBmOWQtNGI3OS04MDVhLWQ3MTFlYTQ2NWQ0MSZsaW5rPTQ3YmJkZTI5LTM5MjItNDMyYi1hY2VhLWM1ODM4Y2RiZTRlYiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=69f91cd9-0f9d-4b79-805a-d711ea465d41&link=47bbde29-3922-432b-acea-c5838cdbe4eb&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "sigara-uygulamasi_104104619_104104619.html"
source_version: "2023-02-08T13:58:22.740+03:00"
source_bytes: 587128
fetched_at: "2026-09-13T04:23:40+00:00"
generator: "netsis-scraper 1.0.0"
---
# Sigara Uygulaması

Netsis içerisinde sigara uygulaması hakkında ayrıntılı bilgiye bu dokümandan ulaşılır.

Muhasebe\\Entegre\\Kayıt\\Entegrasyon Kodları menüsü altındaki Sigara Uygulaması sekmesi üzerinden "Sigara Özel KDV Uygulaması" parametresi ile kullanım aktif hale getirilir.

![](../_assets/3e9437ad13a242fe70a1.png)

Bu ekran üzerinden çalışacak muhasebe kodlarının seçimi yapılır. Ayrıca sigara uygulamasının dahil olacağı cari ve stoklar için cari ve stok kartındaki rapor kodları ya da kullanıcı tanımlı sahalardan hangi alanlarına SIGARA yazılacağı seçimi yapılır. Bu seçimler kaydedildiğinde özel parametre tanımları ekranına alttaki şekilde özel parametreler sistem tarafından otomatik eklenecektir.

![](../_assets/ce17d6c6900188f4aae6.png)

**Stok ve Cari Kart Üzerinde Yapılması Gereken Düzenlemeler**

Stok kartları için seçilen parametreye göre ilgili alan için SIGARA yazılmalıdır.

Örneğimizde stoklar için kod4 alanı seçili olduğunda bu alana SIGARA yazılmıştır.

![](../_assets/a19bdfe9de044e63ead1.png)

Stok kartındaki fiyat 1 alanına bakkala satış fiyatı , fiyat 4 alanına ise stoğun nihai satış fiyatı yazılmalıdır. Eğer özel fiyat sistemi var ise fiyat listesindeki fiyat 4 alanına yazılmalıdır.

![](../_assets/ea47280076033ecc0d18.png)

Cari hesap kayıtları ekranında ise yine entegrasyon kodlarında belirtilen parametre alanına uygun olarak değer alanına SIGARA yazılmalıdır. Örneğimizde cari için kod 4 seçili olduğundan rapor kodları kod-4 alanına SIGARA yazılmıştır.

![](../_assets/37bf428da604315bb811.png)

**Fatura Girişi ve Hesaplamaları**

İlgili cari için kdv dahil sigara stoklarını içeren fatura girişi yapılır.

![](../_assets/f5f2140cb81dc4a2128d.png)

![](../_assets/219d298988bfc7473129.png)

![](../_assets/dcb5c0db3d8a36a3fe3d.png)

**Hesaplamalar**

|  | *A* | *B* | *C* | *D* |
| --- | --- | --- | --- | --- |
| *1* | *Nihai Satış Fiyatı (Karton)* | *18.000* | *KDV Dahil* | *Satış Fiyatı 4* |
| *2* | *Bakkala Satış Fiyatı (Karton)* | *14.080* | *KDV Dahil* | *Satış Fiyatı* |
| *3* |  | *2.745,76* | *KDV* | *=B1-(B1/1,18)* |
| *4* |  | *11.334,24* | *600 Gelir hesabı* | *=B2-B3* |
| *5* |  | *2.040,16* | *391 x hesabı* | *=B4\*0,18* |
| *6* |  | *705,60* | *391 y hesabı* | *=B3-B5* |
| *7* |  | *14080,00* |  | *=B4+B5+B6* |

![](../_assets/893e16e00843458c0030.png)

**Sigara Uygulaması Özel Parametreler**

B Formu kayıtlarına sigara faturalarının KDV Dahil edilmesi isteniyor ise; **MUHASEBE\\SIGARAKDV** özel parametresi kullanılmalıdır. DEGER alanına TBLFATUIRS' daki alanlar kısıt olarak verilmelidir. Fatura üst bilgilerindeki özel kod1, özel kod2 ya da açıklama alanı kullanılabilir. Örneğin sigara faturası kesilen faturanın özelkod2 alanına S yazılırsa ve bu faturaların b formuna kdv dahil tutarın gelmesi için özel parametrede değer alanına KOD2='S' şeklinde tanımlama yapılmalıdır.

**'EFATURA','SIGARAKDV'** özel parametresi eklenmiştir. İlgili özel parametre tanımlandığında Toplu e-Fatura Oluşturma ekranına "Sigara Faturası Oluşturulsun" seçeneği eklenir. Seçenek işaretlendiğinde, "Sigara Uygulaması" kullanılmayan durumlarda da e-Fatura oluştururken, sigara faturası gibi oluşturulması sağlanmıştır.

**FATURA\\SIGARAISKONTO** özel parametresi kullanıldığında Sigara uygulamasında genel iskontonun entegrasyona atılması desteklendi.
