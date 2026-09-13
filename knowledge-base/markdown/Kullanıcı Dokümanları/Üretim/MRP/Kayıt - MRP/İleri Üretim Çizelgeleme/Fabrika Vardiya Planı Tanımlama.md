---
title: "Fabrika Vardiya Planı Tanımlama"
page_id: "50672752"
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
  - "Fabrika Vardiya Planı Tanımlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Üretim / MRP / Kayıt / MRP / İleri Üretim Çizelgeleme / Fabrika Vardiya Planı Tanımlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWRlZjVjYzFiLTNkNjEtNDA0Yi04MDMyLTc3MWU4M2YzZjQ3YiZsaW5rPWQ3OTM1NjQ1LWI4NzItNDZhNC1iY2E0LTQ2ODc0M2UwY2E5YyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=def5cc1b-3d61-404b-8032-771e83f3f47b&link=d7935645-b872-46a4-bca4-468743e0ca9c&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "fabrika-vardiya-plani-tanimlama_50672753_50672752.html"
source_version: "2022-10-18T15:14:05.343+03:00"
source_bytes: 23930
fetched_at: "2026-09-13T04:19:41+00:00"
generator: "netsis-scraper 1.0.0"
---
# Fabrika Vardiya Planı Tanımlama

Fabrika Vardiya Planı Tanımlama, Üretim Bölümü'nde Kayıt/MRP menüsünün altında yer alır. İşletmede var olan tüm vardiyalar tanımlandıktan sonra ilgili vardiyalardan oluşan çalışma takviminin oluşturulması için kullanılan bölümdür. Farklı vardiya planlarının oluşturulmasına yardımcı olur. Farklı vardiya planlarıyla çizelgeleme çalıştırılarak farklı senaryoları karşılaştırılması mümkündür.

Fabrika Vardiya Planı Tanımlama ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Fabrika Çalışma Takvimi Ekranı |  |
| --- | --- |
| Vardiya Plan No | Her bir vardiya için bir plan numarasının verilmesi gerekir. İlgili vardiya için plan numarasının tanımlandığı alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile plan numaralarına ulaşılır. |
| Açıklama | "Vardiya Plan No" alanından tanımlanan vardiya plan numarası için açıklama bilgisi girilen alandır. |
| Varsayılan | Varsayılan vardiya planının belirlenmesi için kullanılan seçenektir. Bu seçeneğin bir vardiya için işaretli olduğu durumlarda, Vardiya Plan Numarası sorulan ekranlara otomatik olarak bu vardiya planı gelir. |
| Başlangıç/Bitiş Tarihi | Oluşturulan vardiya planının geçerlilik tarihlerinin girildiği alandır. "Bitiş Tarihi" boş bırakıldığı takdirde, ilgili vardiya planı süresiz olarak geçerli kılınır. |
| Haftanın Günleri | Vardiyanın geçerli olacağı günün seçildiği alandır. Vardiya planını oluştururken, seçilen vardiyaların zaman bakımından çakışması halinde, kullanıcıya bir uyarı mesajı gelir. Plan oluşturma sırasında<br>bu duruma dikkat edilmesi gerekir. |
| ![](../../../../../_assets/1e3c53b44cef11bbab9e.png) Yeni Vardiya Planı | Ekrandan çıkış yapılmasına gerek kalmadan, yeni bir vardiya planı oluşturmak için kullanılan butondur. |
| ![](../../../../../_assets/952d1f7c29194aaea7c5.png) Vardiya Planını Sil | Tanımlanan vardiya planının silinmesi için kullanılan butondur. Silinmesi istenen kaydın üzerine fare ile çift tıklanarak seçim yapılan kaydın silinmesini sağlar. |
| ![](../../../../../_assets/df8d3011c14ca81e3752.png) Vardiya Plan Kopyala | İstenen bir vardiyanın, numarası belirlenecek başka bir vardiyaya kopyalanması için kullanılan butondur. |
| ![](../../../../../_assets/0fd06cd30fbc696fcf68.png) Değişikliği Kaydet | Vardiya planının alt gride atılarak kaydedilmesini sağlayan butondur. |
| ![](../../../../../_assets/5eab42f5400e4ba72a3b.png) Değişiklikleri İptal Et | Vardiya planında yapılan değişikliklerin iptal edilmesi için kullanılan butondur. |
| ![](../../../../../_assets/385c6b6a8cc91fb78a14.png) Başka Güne Kopyala | Kullanıcı tarafından belirlenecek gün ya da günlere kopyalama yapılması için kullanılan butondur. |
| ![](../../../../../_assets/9346373f98bcfa25a2d6.png) Plan İzleme | İçinde bulunulan günden itibaren 1 haftanın vardiya planı olarak görüntülenmesi için kullanılan butondur. |

Ekranın üst kısmında bulunan grid alandaki seçim kutucuklarından vardiya planına alınması istenen kayda çift tıklanması gerekir. Vardiyalar için gün seçimi konusunda özelden genele bir hiyerarşik yapı vardır.

**Örneğin;**

Haftanın tüm günleri için seçim yapılmış bir vardiya ile sadece Pazar günü için seçim yapılmış bir vardiya birlikte bir vardiya planı oluşturursa, en özel geçerli olacak şekilde bir çalışma mantığı yürütülür. Yani, bu örnekte Pazar günleri için "Pazar" seçimli vardiya, diğer günler için haftanın tüm günleri için seçilmiş vardiya geçerli olur.
Vardiya planları için belirlenen Başlangıç-Bitiş tarihlerine göre dönemsel çakışma olması durumunda ise, çizelgelemenin çalıştırıldığı tarihe en yakın başlangıç tarihine sahip vardiya planı geçerli olur.
