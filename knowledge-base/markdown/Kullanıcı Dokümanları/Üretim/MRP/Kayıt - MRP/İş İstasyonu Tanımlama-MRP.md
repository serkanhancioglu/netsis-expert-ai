---
title: "İş İstasyonu Tanımlama/MRP"
page_id: "50666613"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Üretim"
  - "MRP"
  - "Kayıt / MRP"
  - "İş İstasyonu Tanımlama/MRP"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Üretim / MRP / Kayıt / MRP / İş İstasyonu Tanımlama/MRP"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWFhNmM0MWMxLTRjODAtNDc2OS1hOWZiLTgzOTI2YzFjZDVkZSZsaW5rPTVmOWU2MjkzLTExOTMtNGRjNi1iNzYzLTVkNzhlOTNhZmNkMiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=aa6c41c1-4c80-4769-a9fb-83926c1cd5de&link=5f9e6293-1193-4dc6-b763-5d78e93afcd2&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "is-istasyonu-tanimlama-mrp_50666614_50666613.html"
source_version: "2022-10-18T16:29:31.457+03:00"
source_bytes: 13607
fetched_at: "2026-09-13T04:19:46+00:00"
generator: "netsis-scraper 1.0.0"
---
# İş İstasyonu Tanımlama/MRP

İş İstasyonu Tanımlama MRP, Üretim Bölümü'nde Kayıt/MRP menüsünün altında yer alır. Aynı türden bir veya birden fazla işin bir arada yapıldığı ve bir veya bir grup işçinin/makinenin çalıştığı üretim birimidir. Üretim merkezi, masraf merkezi gibi de düşünülebilir. İş istasyonları içinde bir veya birden fazla işlem/operasyon yapılabilir. Ürün bazında yapılan işlemlerin sırası ve sayısı değişebilir. Fakat, aynı iş istasyonunda yapılan operasyonların benzer olması ve yerleşim olarak da bir arada bulunması gerekir. Aynı iş istasyonu için hem işçilik hem makine kapasite planlamasının yapılması için de her ikisi için ayrı iş istasyonlarının tanımlanması gerekir.

**Örneğin;**

Bir halı fabrikasında boyama, yıkama ve kurutma işlemlerinin yapıldığı bölümler ayrı iş istasyonlarıdır. Her bir istasyonda yapılan işlem kendi içinde aynıdır.

İş İstasyonu Tanımlama MRP ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| İş İstasyonu Tanımlama Ekranı |  |
| --- | --- |
| İstasyon Kodu | En fazla 5 karakter uzunluğunda, tanımlanan iş istasyonu için kod girilen alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, her iş istasyonunun bir kod numarasının olması gerekir. |
| İstasyon İsmi | İstasyon koduna ait isim bilgisinin tanımlandığı alandır. |
| Departman Kodu | Maliyet muhasebesinin kullanıldığı yerlerde bu alana mamul ana grup kodu girilir. Bunun dışında da raporlama amacıyla istenen bir kod girilebilir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile departman kodlarına ulaşılır. |
| İşçilik Maliyeti | İş istasyonunda standart birim işçilik maliyet tutarlarının girildiği alandır. Bu alana bir tutar girildiğinde, kapasite planlama yapılırken, ihtiyaç işçilik kapasitesi karşılığı gereken standart işçilik maliyeti hesaplanır. |
| Genel Üretim Maliyeti | İş istasyonunda standart genel üretim maliyetinin girildiği alandır. Bu alana bir tutar girildiğinde, kapasite planlama yapılırken, ihtiyaç işçilik kapasitesi karşılığı gereken standart genel üretim maliyeti hesaplanır. |
| Hazırlık Süresi | Tanımlanan iş istasyonunda işleme başlanması için bir hazırlık süresi gerektiğinde, ne kadar bir süre gerektiği girilir. Bu bilgi, ilgili iş istasyonundaki bütün operasyonlar için bir öndeğer niteliğindedir. Kapasite Planlamada operasyon bazında tanımlanan hazırlık süresi dikkate alınır. |
| Üretim Süresi | Tanımlanan iş istasyonunda, 1 birim mamul/yarı mamul üretimi için geçen süredir. Bu bilgi, ilgili iş istasyonundaki bütün operasyonlar için bir öndeğer niteliğindedir. Kapasite Planlamada operasyon bazında tanımlanan üretim süresi dikkate alınır. |
| Hedef Kuyruk Süresi | Bir mamulün hedeflenen kuyrukta bekleme süresidir. Bilgi amaçlı kullanılır. |
| Ortalama Kuyruk Süresi | Ortalama kuyruk süresi program tarafından otomatik olarak hesaplanır. Bilgi amaçlı kullanılır. |
| Maksimum Kuyruk Süresi | Bir mamulün kuyrukta bekleyeceği, hedeflenen maksimum süredir. Bilgi amaçlı kullanılır. |
| Maksimum Kuyruk İzni | Kuyrukta bekleyecek mamul sayısıdır. Bilgi amaçlı kullanılır. |
| Standart Eş Zamanlı Operasyon Sayısı/1,2,3. Vardiya | Vardiyalar bazında, ilgili istasyonda eş zamanlı olarak çalışan işçi/makine sayısıdır. İstasyon mevcut kapasite hesaplamasında bu bilgi dikkate alınır. |
| Maksimum Eş Zamanlı Operasyon Sayısı/1,2,3. Vardiya | İlgili vardiyada eş zamanlı olarak yapılacak maksimum operasyon sayısını belirleyen alandır. |
| Vardiya Başlangıcı | İlgili vardiyanın başlayacağı saat bilgisinin girildiği alandır. |
| Vardiya Toplam Süresi | İlgili vardiyanın ne kadar süreceğinin girildiği alandır. **Örneğin;** "Vardiya Başlangıcı" olarak 08:00 girildiği ve "Vardiya Toplam Süresi" olarak da 6 saat girildiğini varsayıldığında; ilgili vardiya saat 08:00'da başlar ve saat 14:00'e kadar 6 saat boyunca devam eder. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır.

Kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
