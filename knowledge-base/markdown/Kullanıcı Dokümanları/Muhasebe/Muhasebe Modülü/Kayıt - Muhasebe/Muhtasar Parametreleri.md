---
title: "Muhtasar Parametreleri"
page_id: "24740521"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Muhasebe"
  - "Muhasebe Modülü"
  - "Kayıt / Muhasebe"
  - "Muhtasar Parametreleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / Kayıt / Muhasebe / Muhtasar Parametreleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWI0YWIwOGQyLTJhOWQtNGQ2OC1hMzc1LWUyZjgwYWJjMjJiMSZsaW5rPTQ0YTgzMDUxLTNmOWEtNDY4Ni1hNjc0LWZhYjIzMGJjMjk0ZiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=b4ab08d2-2a9d-4d68-a375-e2f80abc22b1&link=44a83051-3f9a-4686-a674-fab230bc294f&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "muhtasar-parametreleri_39420322_24740521.html"
source_version: "2022-09-28T17:47:13.993+03:00"
source_bytes: 125311
fetched_at: "2026-09-13T04:12:57+00:00"
generator: "netsis-scraper 1.0.0"
---
# Muhtasar Parametreleri

Muhtasar Parametreleri, Muhasebe Bölümü'nde, "Kayıt/Muhasebe Modülü" menüsünün altında yer alır. Muhtasar Parametreleri, Muhasebe Modülü ile ilgili işlemlere başlamadan önce bazı tanımlamaların yapılmasını sağlayan bölümdür. Aylık veya üç aylık dönemlerde, muhtasar beyanname basımlarının yapılması için gerekli bilgilerin girilmesi gerekir. Beyanname basımlarında, bu bölümden girilen bilgiler baz alınır.

Aşağıdaki parametrelerde sorgulanan muhasebe kodu alanlarına mutlaka muavin hesap kodunun girilmesi gerekir.

"Muhtasar Beyanname Parametreleri" ekranı; Yıl/Ay ve Beyanname olmak üzere iki sekmeden oluşur.

**Yıl/Ay**

![](../../../../_assets/45720374269aac2bd90d.png)

Muhtasar Beyanname Parametreleri ekranı Yıl/Ay sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Muhtasar Beyanname Parametreleri Ekranı |  |
| --- | --- |
| YILI | Muhtasar parametreleri için tanımlanacak yılın belirlendiği alandır. |
| Aylık/Üç Aylık | Muhtasar parametrelerinin alınacağı dönemin belirlendiği alandır. Aylık veya Üç Aylık olmak üzere iki seçenekten oluşur. Hangi aya ya da döneme ait parametre tanımlanacağı ilgili ay işaretlenerek belirtilir. |
| Beyanname Temizle | Seçilen ay için saklanan tüm parametrelerin silinmesini sağlayan butondur. |
| Vergi Dairesi Kodu | Beyanname için vergi dairesi kodu girilen zorunlu bir alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, vergi dairesi kodları arasından seçim yapılır. |
| Parametre Kopyala | İlgili beyanname parametrelerinin kopyalanması için kullanılan butondur. Tıklandığında ekrana gelen "Beyanname Parametre Kopyalama" ekranı ile Şirket, İşletmeler, Kaynak Beyanname ve Vergi Dairesi kodu girilerek kopyalama işlemi gerçekleştirilir. ![](../../../../_assets/1d05c7f6554a0a5b2ba3.png) |

**Beyanname**

Beyanname sekmesi, beyanname parametre tanımlamalarının yapıldığı sekmedir.

![](../../../../_assets/b78cc50dad881940c62e.png)

Muhtasar Beyanname Parametreleri ekranı Beyanname sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Muhtasar Parametreleri |  |
| --- | --- |
| Asgari Ücretler Ayrılsın | Beyanname ekranının sol üst kısmında bulunan seçenektir. İşaretlendiğinde, (personellere ait gelir vergisi matrah ve tutarları personel paketinden aktarılıyorsa, personel şirket kodunun girilmesi gerekir) asgari ücretle çalışan ve diğer çalışanların vergi matrah ve tutarları ayrı yazılır. Vergi matrah ve tutarlarının personel programından aktarılması için, personel paketinde ilgili ay için yeni aya devir veya puantaj rapor hazırlık işleminin çalıştırılması gerekir. İşaretlenmediği zaman, (personel şirket kodları girilmişse) çalışan sayısı toplu olarak basılır. |
| Personel Şirket Kodları | Netsis personel paketinin kullanıldığı durumlarda, muhtasar beyannamede kullanılacak gerekli bilgilerin personel programından aktarılması için, bilgi alınacak şirket kodlarının girildiği alandır. Birden fazla şirketten bilgi alınması istendiğinde, şirket kodlarının arasına virgül (,) koyularak girilmesi gerekir. Şirket aralığında bilgi alınması istendiğinde ise, (alfabetik sıra göz önünde bulundurularak) aralarına iki nokta yan yana (..) girilmesi gerekir. **Örneğin;** ALFA, YAFA gibi. Alanın boş bırakılması halinde; vergi matrah ve tutarları, girilen muhasebe kodlarından aktarılır. Muhtasar beyanname parametreleri girilirken, giriş yapılmasına izin verilen alanların yanında rehber ![](../../../../_assets/088477bb321d1b20c939.jpg) butonu olanların, basım sırasında alan tutarının parametrede belirlenen muhasebe kodundan alınacağı anlamına gelir. Bu alanlarda muhasebe kodları, rehber yardımıyla bulunarak girilir. Diğer giriş yapılmasına izin verilen alanların ise, sabit değerlerle ve elle doldurulması gerekir. |
| ![](../../../../_assets/c7275efbddc154ea1579.jpg) Kaydet | Girilen bilgilerin kaydedilmesi için kullanılan butondur. |
| ![](../../../../_assets/bfd25ffa1947d2603b7a.png) Tüm Alanlar İçin Değeri Oku | Beyanname ekranındaki bilgilerin, daha önce saklanan son değerler ile değiştirilmesi istendiğinde kullanılan butondur. |
| Ödemelerin Tür Kodu | Beyannamede Tablo-I bölümündeki kod cetveli doğrultusunda, uygun ödeme kodunun elle girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile kodlar arasından seçim yapılır. |
| Ödemelerin Gayri Safi Tutarı | Girilen ödeme türlerine, gelir vergisi matrahlarının alınacağı muhasebe kodunun girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile kodlar arasından seçim yapılır. |
| Gelir Vergisi Kesintisi Tutarı | Girilen ödeme türlerine, gelir vergisi tutarının alınacağı muhasebe kodunun girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, kodlar arasından seçim yapılır. Beyan HTML içinde, diğer alanlar da yukarıda anlatılan şekilde doldurulur. Beyannamede herhangi bir değer alması istenmeyen bölümün boş bırakılması gerekir. Parametreler girildikten sonra, ekranın sol üst köşesinde bulunan kaydet butonu ![](../../../../_assets/c7275efbddc154ea1579.jpg)kullanılarak kaydedilir. |
