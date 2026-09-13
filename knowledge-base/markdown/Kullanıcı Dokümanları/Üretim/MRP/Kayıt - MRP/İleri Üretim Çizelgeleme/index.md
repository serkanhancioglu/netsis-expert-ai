---
title: "İleri Üretim Çizelgeleme"
page_id: "50672593"
product: "netsis-3-enterprise"
depth: 5
is_section: true
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Üretim"
  - "MRP"
  - "Kayıt / MRP"
  - "İleri Üretim Çizelgeleme"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Üretim / MRP / Kayıt / MRP / İleri Üretim Çizelgeleme"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTE5YTI5YzQ2LTFmZWYtNDNmYS1iMzhlLTBmM2M5YTUwMDkzNyZsaW5rPTE4NWZiN2FhLWE3ZTItNGQ1MC1iZTQ3LWYwMmVkOTJmYTI4OSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=19a29c46-1fef-43fa-b38e-0f3c9a500937&link=185fb7aa-a7e2-4d50-be47-f02ed92fa289&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ileri-uretim-cizelgeleme_50672610_50672593.html"
source_version: "2022-10-18T11:44:00.233+03:00"
source_bytes: 340449
fetched_at: "2026-09-13T04:19:32+00:00"
generator: "netsis-scraper 1.0.0"
---
# İleri Üretim Çizelgeleme

İleri Üretim Çizelgeleme, Üretim Bölümü'nde Kayıt/MRP menüsünün altında yer alır. İleri Üretim Planlama uygulaması, bir işletmede tamamlanması planlanan siparişlerin hangi istasyonlarda, hangi sırayla ve hangi kaynaklar kullanılarak üretilmesi gerektiğini hesaplamaya ve sonuçları bir Gantt şeması üzerinde çizelgelemeye yarar. Böylece; doğru zamanda, doğru üretim, optimum kaynak kullanımıyla gerçekleştirilir ve işletme hedeflerine ulaşılması sağlanır. Oluşturulan çizelgelere ait çok sayıda rapor seçeneği uygulamada desteklenir. Ek olarak, çizelge üzerindeki iş emri sabitleme, kural tanımları ve benzeri desteklerle, kullanıcının üretim planlarına müdahale etmesi de mümkündür. İleri Üretim Planlama uygulamasının Netsis üzerindeki hangi modüllerden veri aldığına dair bilgi akış diyagramı Ekran Görüntüsü 1’de görüntülenir.

![](../../../../../_assets/a50f2ebf3e263ee26e3c.png)

Uygulamanın uyarısız şekilde çalışması için, modül üzerindeki; vardiya, iş istasyonu, makine, operasyon, kaynak gibi sabit tanımlamaların adım adım ve doğru şekilde yapılması gerekir. İleri Üretim Planlama modülünün girdi ve çıktıları Ekran Görüntüsü 2’de özet halinde gösterilir.

![](../../../../../_assets/d49033ce9d2d7a531d9e.png)

İleri Üretim Planlama modülü kullanılmadan önce işletmeye ait üretim reçete yapısının iyi kurgulanması ve program üzerinde oluşturulması gerekir. Önerilen, her operasyon geçişi için yeni bir Stok Kodu (Yarı Mamul) oluşturulmasıdır. Bu şekilde tanımlama yapıldığı takdirde operasyonlar arasında mamul/yarı mamul stok bakiyesi takibi yapılabilir. Çok sayıda operasyonu olan ve bu şekilde tanımlama yapılmasını istemeyen işletmelerde, birkaç operasyonun birleştirilip, bu operasyonlar tek bir operasyonmuş gibi tanımlama yapılması sağlanabilir. Ancak, bu şekilde çalışacak işletmelerde operasyon tanımlamaları kritiktir. Eğer, ara stok takibinin yapılacağı operasyonlar varsa, birleştirilmesi düşünülen operasyonların bu duruma göre belirlenmesi gerekir.

İleri Üretim Planlama uygulamasının kullanılması için ileri üretim planlama ek lisansına sahip olunması gerekir. Ayrıca lisans sahibi kullanıcıların Üretim → MRP → Kayıt → MRP Parametreleri yolunu izleyerek "MRP II" sekmesindeki “İleri Üretim Planlama” parametresini seçerek uygulamayı aktif hale getirmesi gerekir. Bu işlemleri tamamlayan kullanıcılar, Üretim → MRP → Kayıt → "İleri Üretim Çizelgeleme" menüsü altından “Vardiya Tanımlama” ekranına giriş yaparak uygulamayı kullanmaya başlayabilirler.
