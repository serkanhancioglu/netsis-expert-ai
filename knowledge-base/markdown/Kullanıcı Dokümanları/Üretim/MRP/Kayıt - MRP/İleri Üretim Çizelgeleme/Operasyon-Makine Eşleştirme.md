---
title: "Operasyon-Makine Eşleştirme"
page_id: "50673151"
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
  - "İleri Üretim Çizelgeleme"
  - "Operasyon-Makine Eşleştirme"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Üretim / MRP / Kayıt / MRP / İleri Üretim Çizelgeleme / Operasyon-Makine Eşleştirme"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWU2NjcyMzg4LTkwMDMtNGQzOS1hYjRjLTc1MWY1ZTk3NzI3MiZsaW5rPWIzZDY4YmZhLTY2MGItNDVjZS1hMWYyLTZlYzA3ODgyMmIxOCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=e6672388-9003-4d39-ab4c-751f5e977272&link=b3d68bfa-660b-45ce-a1f2-6ec078822b18&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "operasyon-makine-eslestirme_50673161_50673151.html"
source_version: "2022-10-18T15:10:41.123+03:00"
source_bytes: 24103
fetched_at: "2026-09-13T04:19:40+00:00"
generator: "netsis-scraper 1.0.0"
---
# Operasyon-Makine Eşleştirme

Operasyon Makine Eşleştirme, Üretim Bölümü'nde Kayıt/MRP menüsünün altında yer alır. İleri Üretim Çizelgeleme uygulamasının doğru şekilde çalışması için şimdiye kadar yapılan tanımlamalara ek olarak, yapılması gereken eşleştirmeler bulunur. Bunlardan “Operasyon-Makine” ya da “Makine-Operasyon” eşleştirmesinin eksiksiz olarak tanımlanması zorunludur. Kaynak (Kalıp, Takım gibi) tanımları bulunan kullanıcıların daha doğru sonuç almak için “Operasyon-Kaynak” veya “Makine-Kaynak” eşleştirmesini de yapması gerekir ancak, bu tanımlamalar zorunlu değildir. Operasyon-Makine ya da Makine-Operasyon eşleştirmeleri eksik olan ya da hiç olmayan ürünler için çizelgeleme yapılmaz. Daha önceki bölümlerde de bahsedildiği gibi şimdiye kadar yapılan tanımlamaların; operasyon, kaynak, makine bazında detaylandırıldığı ve özelleştirildiği adım eşleştirme adımıdır.

Operasyon Makine Eşleştirme ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Operasyon-Makine Eşleştirme Ekranı |  |
| --- | --- |
| Operasyon Kodu | Operasyon-Makine eşleştirme ekranı seçilen operasyon için açıldığından dolayı, “Operasyon Kodu” alanına müdahale edilemez. Sistem tarafından otomatik olarak ekrana getirilir. |
| Ürün Seçimi | Ürün Kodu, Ürün Grubu ya da Tümü bazında eşleştirme yapılması için seçim yapılan alandır. Bu alanda yapılacak seçim, eşleştirmenin seçili operasyona gelen hangi ürünler için geçerli olacağını ifade eder. Ürün Kodu ya da Ürün Grubu seçilirse, “Ürün Değer” alanı da eşleştirmenin hangi ürünler veya ürün grupları bazında geçerli olacağı bilgisine göre girilir. |
| Ürün Değer | Ürün Seçimi alanında Ürün Kodu veya Ürün Grubu seçeneklerinin seçilmesi ile aktif hale gelir. Ürün değerinin belirtilmesini sağlar. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, kodlar arasından seçim yapılır. |
| ![](../../../../../_assets/4d5937e5d0ca7cc09b74.png) Arama | Esnek Yapılandırma bilgilerinden arama yapmak için kullanılan butondur. |
| ![](../../../../../_assets/3d053588ba4269cdcdda.png) Asorti | Asorti bilgisi girmek için kullanılan butondur. |
| Yapılandırma Kodu | Yapılandırma kodunun girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, tanımlanan özellik kodlarına ulaşılır. |
| Yapılandırma Kodu Açıklaması | Yapılandırma koduna ait açıklama bilgisinin otomatik olarak ekrana girildiği alandır. |
| İstasyon Kodu Filtresi | Daha önce Operasyon Tanımlama ekranı üzerinden yapılmış tanımlamalara istinaden sistem tarafından otomatik olarak ekrana getirilen koddur. İstenmesi halinde bu kısıt kaldırılarak makinelerin tam listesi görüntülenir. Kısıtı kaldırmak için alandaki istasyon kodunun silinip klavyede yer alan \<tab\> tuşu ile ilerlenir. İlgili operasyonun hangi makinelerde yapılacağı, listede bulunan "Seçim" sütunundaki kutucuklara çift tıklayarak belirlenir. "Seçim" kutucuğu tıklanmış bir makine için “Operasyon Tanımlama” veya “Makine Tanımlama” ekranlarında üretim süresi ve üretim miktarı bilgileri tanımlanmamışsa, program bu alanlara<br>odaklanır ve bu alanlar doldurulmadan seçimin kaydedilmesine izin vermez. |
| Makine Kodu İle Eşleştir | Operasyon-Makine eşleştirmesinin makine kodu ile yapılması için kullanılan sekmedir. |
| Makine Grubu İle Eşleştir | Uygulamada tanımlanan makine gruplarının olması durumunda, bahsedilen tanımlamaların aynı şekilde makine grubu bazında yapılmasını sağlamak için kullanılan sekmedir. |
| ![](../../../../../_assets/0fd06cd30fbc696fcf68.png) Değişikliği Kaydet | Girilen tanımlamaların kaydedilmesi için kullanılan butondur. |
| ![](../../../../../_assets/5eab42f5400e4ba72a3b.png) Değişiklikleri İptal Et | Girilen tanımlamaların iptal edilmesi için kullanılan butondur. |

Ekranın alt bölümünde bulunan grid alanda şimdiye kadar bahsi geçen tanımlama ekranlarındaki alanlar sütunlar halinde bulunur ve bu alanlarda tanımlama yapılması mümkündür. Operasyon-Makine Eşleştirme ekranı ürün bazında tanımlama yapmaya imkan verdiği için ve bu şimdiye kadar yapılan tanımlamalardan daha özel bir tanımlama türü olduğu için, hiyerarşik olarak burada bir tanımlama yapıldıktan sonra, bu ekrandaki tanımlamalar geçerli olur. Yani, daha önce yapılmış tanımlama olsa bile, program bu ekrandaki tanımlamaları baz alır. Aynı hiyerarşik yapı "Ürün Seçimi" alanı için de geçerlidir.

**Örneğin;**

Bir Operasyon-Makine Eşleştirmesi hem “Tümü” için yapılmış hem de “Ürün Kodu” için yapılmışsa, ürün kodu daha özel bir tanımlama olacağı için, geçerli olan bu özel tanım baz alınır.
