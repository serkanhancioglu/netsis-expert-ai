---
title: "Operasyon-Kaynak Eşleştirme"
page_id: "50666857"
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
  - "Kaynak Yönetimi/MRP"
  - "Operasyon-Kaynak Eşleştirme"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Üretim / MRP / Kayıt / MRP / Kaynak Yönetimi/MRP / Operasyon-Kaynak Eşleştirme"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTQ3YmZjYTBjLTVmZTYtNDBkMi05ZDEyLWI4ZTA4ODJjYzFiZiZsaW5rPTQ1ZGRjYTIxLTc5M2MtNDRmOS05NDNhLWI0YmM5MWI5ZmEzYSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=47bfca0c-5fe6-40d2-9d12-b8e0882cc1bf&link=45ddca21-793c-44f9-943a-b4bc91b9fa3a&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "operasyon-kaynak-eslestirme_50666876_50666857.html"
source_version: "2022-10-19T14:51:03.523+03:00"
source_bytes: 589778
fetched_at: "2026-09-13T04:19:56+00:00"
generator: "netsis-scraper 1.0.0"
---
# Operasyon-Kaynak Eşleştirme

Operasyon Kaynak Eşleştirme, Üretim Bölümü'nde Kayıt/MRP menüsünün altında yer alır. Ürün ve ürün operasyonları bazında kullanılacak kaynakların tanımlandığı ve varsayılan ömür tüketimlerinin tanımlandığı bölümdür. Bu ekranda yapılan tanımlamalar, kaynak kullanımı sırasında otomatik olarak tüketimlerin ekrana getirilmesini sağlar. Kullanıcı, otomatik olarak ekrana gelen bu bilgiler üzerinden istediği değişiklikleri, ekleme ve çıkarmaları yapabilir. Aynı zamanda, İleri Üretim Planlama uygulaması da, bu ekrandan yapılan tanımlara göre yapılır. Hangi ürünün üretiminde hangi kaynaktan kaç adet kullanılacağı bilgisi, Operasyon-Kaynak Eşleştirme ekranından yapılan eşleştirmeler sayesinde bilinir.

Operasyon Kaynak Eşleştirme ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Operasyon-Kaynak Eşleştirme Ekranı |  |
| --- | --- |
| Operasyon Seçimi | Kaynağın kullanıldığı operasyon bilgisinin seçildiği alandır. Operasyon Kodu bazında tanım yapılacağı gibi, Operasyon Grubu veya Tüm Operasyonlar için de tanım yapılabilir. Alanın sağ tarafında yer alan "Operasyon Değer" alanından ilgili değer tanımlaması yapılır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, seçilen operasyona göre değer tanımlanacak kod tanımlaması yapılır. **Örneğin;** OP_GRUP1 operasyon grubundaki tüm operasyonlar aynı kaynağı kullanıyorsa, operasyon grubu üzerinden tanımlama yapmak kolaylık sağlar. |
| Ürün Seçimi | Operasyon Kodu belirlendikten sonra ürün detayında kaynak eşleştirmesi yapmak için ürün detayı verilir. Ürün Kodu bazında tanım yapılacağı gibi, Ürün Grubu veya Tüm Ürünler için de tanım yapılabilir. Alanın sağ tarafında yer alan "Ürün Değer" alanından ilgili değer tanımlaması yapılır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, seçilen ürüne göre değer tanımlanacak kod tanımlaması yapılır. **Örneğin;** Kaynak kullanımı için ürün detayı vermeye gerek yoksa ve ilgili operasyonda tüm ürünler aynı kaynağı kullanıyorsa, Tüm Ürünler üzerinden tanımlama yapmak kolaylık sağlar. |
| ![](../../../../../_assets/4d5937e5d0ca7cc09b74.png) Arama | Yapılandırma bilgilerinden arama yapmak için kullanılan butondur. |
| ![](../../../../../_assets/3d053588ba4269cdcdda.png) Asorti | Asorti bilgisi girmek için kullanılan butondur. |
| Asorti Kodu | Asorti kodunun girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, tanımlanan özellik kodlarına ulaşılır. |
| Asorti Kodu Açıklaması | Asorti koduna ait açıklama bilgisinin otomatik olarak ekrana girildiği alandır. |
| Set Bilgileri | Kullanılacak kaynak bilgilerinin set yapısında tanımı yapılır. Set kavramı, bir arada kullanılacak birden fazla kaynağı küme haline getirmek için kullanılır. Bir setin içine bir veya daha fazla kaynak eklenebilir. Bu kaynaklar üretim sırasında bir arada kullanılır. Aynı şekilde bir operasyon ve ürün kodu için birden fazla set tanımı yapılabilir. Bu durumda her set tanımı birbirinin alternatifi gibi düşünülebilir. **Örneğin;** OP1 için MAMUL1 üretimi sırasında kullanılan kaynakların SET1 ve SET2 gibi iki set şeklinde tanımlandığı varsayıldığında, bu tanımlama şu anlama gelir: MAMUL1 üretimi sırasında OP1 operasyonu yapılırken SET1 **veya** SET2 içindeki kaynaklar kullanılır. |
| Set Öncelik Sırası | Program tarafından otomatik olarak verilen sıra numarasıdır. Kullanıcı isterse set önceliğini değiştirebilir. Set önceliği, ileri üretim planlama sırasında seçilecek kaynakları etkiler. Set önceliği küçük olan tanımlar daha öncelikli hale gelir. Setin içine eklenecek kaynak bilgisi seçimi yapılır. Kaynak Kodu bazında tanım yapılacağı gibi, Kaynak Grubu veya Tüm Kaynaklar için de tanım yapılabilir. Alanın sağ tarafında yer alan "Kaynak Değer" alanından ilgili değer tanımlaması yapılır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, seçilen kaynağa göre değer tanımlanacak kod tanımlaması yapılır. |
| Kaynak Sayısı | Üretim sırasında ilgili kaynaktan kullanılacak sayının girildiği alandır. |
| Ömür Tüketimi | Bir birimlik üretim sırasında ilgili kaynağın ömründen yapılacak tüketim miktarının girildiği alandır. |
| Kaynak Kullanımı Sadece Hazırlık Aşamasında Yapılsın | Kaynak kullanımının sadece hazırlık aşamasında yapılması için kullanılan seçenektir. |
| ![](../../../../../_assets/280f0e4f9243f32ca825.png) Yeni Set Ekle | Yeni set eklemek için kullanılan butondur. Başka bir operasyonun tanımına geçmek için ekranın ilk bölümündeki operasyon bilgisi değiştirilir. ![](../../../../../_assets/35730b32abea7d5873cf.png) **Örneğin;** Yukarıdaki ekran görüntüsünde OP021 operasyonu için MAMUL1 üretimi sırasında kullanılacak kaynaklar SET1 veya SET2 şeklinde tanımlanmıştır. Üretim sırasında bu setlerden bir tanesi seçilerek kullanılacaktır. SET1 kümesi içinde KALIP1 ve TESTERE_01 kaynakları bir arada kullanılırken, SET2 kümesi içinde KALIP2 ve TESTERE_01 kaynakları bir arada kullanılır. |
| ![](../../../../../_assets/94676d2beed44a635592.png) Seti Sil | Tanımlanan ve grid ekrana getirilen setin üzerine fare ile tıklandıktan sonra, seçilen setin silinmesini sağlayan butondur. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır.

Kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.

**Kullanılan Kaynak Girişi**

Üretim kayıtlarının girildiği aşağıdaki ekranlarda kullanılan kaynak girişi desteklenir.

**Üretim Akış Kaydı:** Ekran üzerindeki "Kullanılan Kaynaklar" butonuyla kaynak girişi yapılabilir.

**Üretim Sonu Kaydı:** Grid üzerindeki üretim satırı seçilerek sağ tuş menüsünden kaynak girişi yapılabilir.

**Serbest Üretim Sonu Kaydı:** Grid üzerinde sağ tuş menüsünden kaynak girişi yapılabilir.

Kaynak girişi yapılacak ürün için Operasyon-Kaynak eşleştirmesi bulunuyorsa, bu eşleşmedeki bilgiler otomatik olarak ekrana getirilir. Eğer Operasyon-Kaynak eşleşmesinde birden fazla alternatif set tanımlanmışsa, ekran aşağıdaki gibi "Set Seçimi" sekmesiyle açılır. Aksi durumda bu sekme ekrana gelmez. "Set Seçimi" sekmesinde operasyon bazında tanımlanan alternatif kaynak setleri gösterilir. Tanımlı setlerden biri seçilerek işleme devam edilebilir ya da direkt olarak ikinci sekme üzerinden serbest giriş yapılabilir.

![](../../../../../_assets/ec3d36fc3d94179cb793.png)

Kullanılan Kaynak Girişi sekmesinde Kaynak Kodu seçilerek, üretimde kullanılan kaynak miktarı ve ömür tüketimi girilir. Operasyon-Kaynak eşleşmesine göre kullanılan kaynaklar otomatik olarak ekrana getirilir. Ancak kullanıcı, bu bilgiler üzerinde değişiklik yapabilir veya yeni kaynak kullanımı girebilir.

Üretim Akış Kaydı sırasında girilen kaynak bilgileri, iş emrine bağlı yapılan üretim sonu kayıtlarında otomatik olarak ekrana getirilir. Bu kayıtlar üzerinde düzenleme yapılamaz ancak yeni kaynak kullanımları girilebilir. Kaynak kullanımlarını girmek için üretim akış kaydının kullanılması zorunlu değildir. Üretim sonu kaydı oluşturulurken de kaynak kullanımları girilebilir.

![](../../../../../_assets/c6586ef6228bb5d0fbde.png)
