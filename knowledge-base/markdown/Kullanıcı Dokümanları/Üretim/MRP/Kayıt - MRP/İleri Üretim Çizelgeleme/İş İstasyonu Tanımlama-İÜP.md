---
title: "İş İstasyonu Tanımlama/İÜP"
page_id: "50672741"
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
  - "İş İstasyonu Tanımlama/İÜP"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Üretim / MRP / Kayıt / MRP / İleri Üretim Çizelgeleme / İş İstasyonu Tanımlama/İÜP"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWM2OTI0YTIyLTQ2OGEtNGQ3MS05NDhiLTFlYWQ4ZDgyYmNiMyZsaW5rPTMyNWMwYzI5LTk2NWEtNGRkNy05ZDFmLWY0OWQyMDI4YmMzYSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=c6924a22-468a-4d71-948b-1ead8d82bcb3&link=325c0c29-965a-4dd7-9d1f-f49d2028bc3a&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "is-istasyonu-tanimlama-iup_50672745_50672741.html"
source_version: "2022-10-18T16:29:51.690+03:00"
source_bytes: 14552
fetched_at: "2026-09-13T04:19:36+00:00"
generator: "netsis-scraper 1.0.0"
---
# İş İstasyonu Tanımlama/İÜP

İş İstasyonu Tanımlama İÜP, Üretim Bölümü'nde Kayıt/MRP menüsünün altında yer alır. Vardiya ve Fabrika Çalışma Takvimi tanımlandıktan sonra iş istasyonlarının da tanımlanması için kullanılan bölümdür. İşletmedeki iş istasyonlarının doğru şekilde kurgulanarak, doğru şekilde tanımlanması kritiktir. Her bir operasyon tek başına bir iş istasyonu olabileceği gibi aynı ya da benzer işleri yapan makine grupları da birer iş istasyonu olabilir.

İş İstasyonu Tanımlama ekranı; İstasyon Bilgileri ve Vardiya Planı olmak üzere iki sekmeden oluşur.

**İstasyon Bilgileri**

İş İstasyonu Tanımlama İÜP ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| İş İstasyonu Tanımlama Ekranı |  |
| --- | --- |
| İstasyon Kodu | En fazla 5 karakter uzunluğunda, tanımlanan iş istasyonu için kod girilen alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, her iş istasyonunun bir kod numarasının olması gerekir. |
| İstasyon İsmi | İstasyon koduna ait isim bilgisinin tanımlandığı alandır. Zorunlu bir alan değildir. |
| Departman Kodu | Maliyet muhasebesinin kullanıldığı yerlerde bu alana mamul ana grup kodu girilir. Bunun dışında da raporlama amacıyla istenen bir kod girilebilir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile departman kodlarına ulaşılır. Zorunlu bir alan değildir. |
| Makine Seçim Önceliği | Tanımlanan iş istasyonu için makine seçim önceliği belirlenen alandır. Alanın sap tarafında yer alan aşağı ok butonu ile; Makinede Tanımlı Öncelik Sırası, Yeni/Eski, Hızlı/Yavaş, Maliyet seçenekleri arasından seçim yapılır. Yapılacak seçim, çizelgelemenin çalışma mantığını etkilemez, raporlama amaçlı kullanılır. |
| Açıklama | Tanımlanan iş istasyonu için açıklama bilgisi girilen alandır. |
| Akış Tipli İstasyon | Akış tipli istasyona sahip işletmelerin kullandığı seçenektir. Akış tipli istasyonlarda farklı operasyonlar arka arkaya kesintiye uğramadan yapılır ve araya iş girmesi söz konusu değildir. |
| İlk Makine Kodu | "Akış Tipli İstasyon" seçeneğinin işaretlenmesi ile aktif hale gelen alandır. Akışın başladığı makinenin tanımlanması için kullanılır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, makine kodları arasından seçim yapılır. Eğer ilk makine kodu tanımlanmazsa; akış, ardışık çalışan makinelerin herhangi birinden başlayıp devam edebilir. **Örneğin;** Akış tipli bir istasyonda sırasıyla 1→2→3→4 numaralı makineler varsa ve ilk makine kodu 1 seçildiyse hep 1.makineden başlayıp bu sırada üretim yapılır. Ancak, ilk makine kodu seçili değilse 3. makineden<br>de akış başlayıp 3→4 numara sırasıyla üretim yapılabilir. |
| **Kapasite Planlama Bilgileri** | \+ butonu ile planlama bilgilerinin girileceği alanlar ekrana gelir. “Kapasite Planlama Bilgileri” alanının çizelgeleme açısından bir önemi yoktur. |
| İşçilik Maliyeti | Tanımlanan istasyon için işçilik maliyeti girilen alandır. |
| Genel Üretim Maliyeti | Tanımlanan istasyon için genel üretim maliyetinin girildiği alandır. |
| Hazırlık Süresi | Tanımlanan istasyon için hazırlık süresi girilen alandır. |
| Üretim Süresi | Tanımlanan istasyon için üretim süresi girilen alandır. |
| Hedef Kuyruk Süresi | Tanımlanan istasyon için hedef kuyruk süresi girilen alandır. |
| Ortalama Kuyruk Süresi | Tanımlanan istasyon için ortalama kuyruk süresi girilen alandır. |
| Maksimum Kuyruk Süresi | Tanımlanan istasyon için maksimum kuyruk süresi girilen alandır. |
| Maksimum Kuyruk İzni | Tanımlanan istasyon için maksimum kuyruk izni girilen alandır. |
| Standart Eş Zamanlı Operasyon Sayısı | İlgili vardiyada eş zamanlı olarak yapılacak operasyon sayısını belirleyen alandır. Eş zamanlı operasyon sayısı arttıkça vardiya boyunca yapılacak iş sayısı doğru orantılı olarak artar. |
| Maksimum Eş Zamanlı Operasyon Sayısı | İlgili vardiyada eş zamanlı olarak yapılacak maksimum operasyon sayısını belirleyen alandır. |
| Vardiya Başlangıcı | İlgili vardiyanın başlayacağı saat bilgisinin girildiği alandır. |
| Vardiya Toplam Süresi | İlgili vardiyanın ne kadar süreceğinin girildiği alandır. **Örneğin;** "Vardiya Başlangıcı" olarak 08:00 girildiği ve "Vardiya Toplam Süresi" olarak da 6 saat girildiğini varsayıldığında; ilgili vardiya saat 08:00'da başlar ve saat 14:00'e kadar 6 saat boyunca devam eder. |

**Vardiya Planı**

İstasyon bazında vardiya planı oluşturmak için kullanılan sekmedir. "Fabrika Vardiya Planı Tanımlama" bölümünde bahsedilen ekranla aynıdır. Burada seçilen istasyon için bir vardiya planı oluşturulursa, hiyerarşik olarak fabrika vardiya planından daha özel bir tanımlama olacağı için, istasyon bazındaki vardiya planı kullanılır.
