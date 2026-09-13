---
title: "Netsis Word Dizaynı"
page_id: "102284542"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis Word Dizaynı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis Word Dizaynı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWEwNWY3NDY1LTkxYTMtNGE2NS04NjZhLTM4MWU0YjMyZGI5OSZsaW5rPTk0NjVlN2YzLWFhZjEtNDFkNy04ZmYxLTEyODZjMzg3NGU2MyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=a05f7465-91a3-4a65-866a-381e4b32db99&link=9465e7f3-aaf1-41d7-8ff1-1286c3874e63&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-word-dizayni_102284542_102284542.html"
source_version: "2023-01-20T09:05:41.287+03:00"
source_bytes: 879606
fetched_at: "2026-09-13T04:23:42+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis Word Dizaynı

Netsis dizayn modülü içerisinden Word dizaynı hazırlayarak dizaynların saklanabilmesi ve basımlarının yapılabilmesi sağlanabilmektedir. Word dizaynı hakkında ayrıntılı bilgiye bu dokümandan ulaşılır.

**Word dizaynı için İşlem Sırası aşağıda belirtilmiştir:**

1. Dizayn tasarımı yapılmadan önce, şablon dediğimiz, dizaynın dijital ortamda yerleştirilecek olan tasarlanmış matbu formun; bu şekilde bir form tasarlanmamış olup sadece basılan bilginin dijital ortamda saklanması amacı ile kullanılacak olsa dahi, basımın yerleştirileceği boş formun, Word dosyası olarak hazır bulundurulması gerekir.
2. Word çıktısı için yeni bir dizayn tanımlayarak, basılması/saklanması istenen alanlar dizayn kalemlerine eklenmelidir. Dizayn tanımlama işlemi, standart dizayn adımları şeklinde yapılacaktır.
3. Bu aşamada belirlenen sahalar dizayna eklenmiş olacak ancak dizayn sırasında verilse dahi pozisyon bilgileri (satır/sütun) belirlenmemiş olacaktır. Saha pozisyonlarının kağıt üzerinde belirlenebilmesi için, öncelikle dizayna eklenen tüm sahalar, otomatik olarak geçici bir Word dokümanına gelişigüzel aktarılacaktır.
4. Geçici Word dokümanındaki bu sahaların, 1. maddede belirtilen Word dokümanı olarak hazırlanmış şablona kopyala-yapıştır fonksiyonu ile, basılması istenen pozisyona yapıştırılmak suretiyle aktarılması gerekmektedir. Word dosyasına basım/saklama özelliği sadece yeni yapılan dizaynlarda kullanılabilir, mevcut dizaynlar için desteklenmez.

Word dosyasına basım/saklama özelliği sadece yeni yapılan dizaynlarda kullanılabilir, mevcut dizaynlar için desteklenmez. Uygulama ile ilgili yapılması gereken düzenlemeler aşağıda anlatılmaktadır.

**Dizayn Genel Bilgileri**

Öncelikle dizaynın sabit bilgileri girildikten sonra, genel bilgilerinde printer port kısmı Word olarak seçilmelidir.

![](../_assets/8fc25fed3259817f8792.png)

Word seçeneği işaretlendiğinde sağ taraftaki Basım, Sakla, Bas ve Sakla seçenekleri aktif olur.

**Basım**

Bu seçenek işaretlendiğinde şablon olarak hazırlanan Word dosyasındaki forma uygun basım yazıcıdan çıkacaktır. Bu durumda dizayn varsayılan olarak tanımlı olan yazıcıya gönderilir.

**Sakla**

Bu seçenek işaretlendiğinde dizayn yazıcıya gönderilmez. Bunun yerine, dizaynın yapıldığı Word şablonuna uygun olarak yeni bir Word dosyası olarak saklanacaktır. Dizayn basımı yapılacağı zaman, Word dosyanın hangi dizinde yaratılacağını sorgulayan bir pencere açılacaktır.

![](../_assets/ed672261679f26eb35be.png)

**Bas ve Sakla**

Bu seçenek işaretlendiğinde ise şablon olarak hazırlanan Word dosyasındaki forma uygun basım hem yazıcıya gönderilecek hem de yeni bir Word dosyasına aktarılacaktır. Böylece belgelerin hem basımının yapılması hem de basımın yapıldığı şekilde Word dosyası olarak saklanması mümkün olacaktır.

**Yazıcı Kodu**

Basım ya da Bas ve Sakla seçeneği işaretlenmişse, çıktının basıldığı bilgisayarda öndeğer olarak tanımlı yazıcıya gönderilecektir. Kısaca Printer Port sahasında Word seçeneği işaretlendiğinde seçilen yazıcı kodunun herhangi bir önemi yoktur.

**Şablon Dosya Adı**

Dizayna göre basım yapılırken dikkate alınacak Word şablonunun adının girileceği alandır. İşlem sırası bölümünde 1. maddede anlatılan şablon dosya, dizayn öncesinde oluşturulmalı ve dizini ile birlikte burada belirtilmelidir.

**Dizayn Kalem Bilgileri**

Word şablonunda kullanılacak bilgilerin belirlendiği bölümdür. Burada sahalar için koordinat verilmesinden ziyade, basılacak alanlar belirlenmekte ve bu alanlara ilişkin ondalık, uzunluk gibi tanımlamalar yapılmaktadır. Kalem bilgileri tanımlanırken girilen bilgiler daha sonra geçici Word dosyasına aktarılacaktır. Örneğin; tutar sahası için belirlenen ondalık ve uzunluk gibi bilgiler Word'e aktarılırken dikkate alınacaktır. Sadece satır ve sütun bilgileri aktarılmayacaktır. O nedenle boş geçilebilir.

![](../_assets/2091fdd1491b43061856.png)

**Word Aktar**

Dizayn Kalem Bilgilerinde tanımlanan bilgiler ekranın sol alt köşesindeki "Word Aktar" butonu ile öncelikle bir Word belgesine aktarılacaktır. Bu dosya, program tarafından aktarım sırasında oluşturulan geçici bir belge olup, Genel Bilgiler sayfasında verilen şablon belge değildir. Oluşan belgenin içinde, dizayn kalem bilgilerinde tanımlanan her bir saha için bir satır oluşacak ve satırlarda sahalara ait ikonlar olacaktır. İkonlarla birlikte, ilgili sahanın Netsis'te hangi alan numarasına sahip olduğu, alan açıklaması ve saha tipi gibi bilgiler de listelenecektir.

![](../_assets/02960a05a8c6a3610ddf.png)

Aktarım sonucunda oluşan bu dosya saklanabilmektedir. Ya da dizaynın içinden tekrar "Word aktar" butonu kullanılarak oluşturulabilir.

**Şablon Word Dosyasının Hazırlanması**

Dizayn genel bilgilerinde Şablon Dosya Adı sahasına girilen şablon Word dosyasına, içeriğinde alan simgelerinin bulunduğu dosyadan her bir simge sırayla kopyalanıp istenilen satıra yapıştırılarak, şablon Word dosyası için düzenlemeler yapılacaktır. Şablon dosyası oluşturulurken Word uygulamasına ait özellikler kullanılarak başlıklar verilmesi, çerçeveler eklenmesi ve satır arası boşluklar gibi düzenlenlemeler yapılabilir.

**Dikkat! Şablon ile hazırlanan dizaynlara göre belgelerin kalem bilgilerinin basımı için, şablona tablo eklenmelidir.** Kalem bilgilerine ilişkin sahalar da bu tablo içine yerleştirilmelidir. Sonuçta aşağıdaki örnekteki gibi bir Word dosyası oluşturulabilecek ve basım sırasında şablon olarak bu Word dosyası kullanılabilecektir.

![](../_assets/61722a4555e8574fda2e.png)

**Örnek Uygulama**

Satış teklif belgesi üzerinde sağ klik basım ile Word dizaynı seçilir.

![](../_assets/59d02b2d7c964d261d58.png)

Dosya yolu sorgulama ekranı açılır burada belirtilen dizine Word formatında kaydedilir.

![](../_assets/1b5e4c774992849fe7d8.png)

![](../_assets/060d4ac792079a1dc321.png)

![](../_assets/deb1b2194aa5f126e078.png)
