---
title: "Kapasite Planlama Sıkça Sorulan Sorular"
page_id: "50687665"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Kapasite Planlama Sıkça Sorulan Sorular"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Kapasite Planlama Sıkça Sorulan Sorular"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTc0MjM2OTBiLWJjMjQtNDQ3YS1iNzU3LTczNGQ4Yzc1M2FkNyZsaW5rPTA4NWQ5ZDM2LTNiNjItNDgyOS05YzQzLTc2MzNmOTNmN2EyNSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=7423690b-bc24-447a-b757-734d8c753ad7&link=085d9d36-3b62-4829-9c43-7633f93f7a25&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "kapasite-planlama-sikca-sorulan-sorular_80090437_50687665.html"
source_version: "2022-05-24T14:11:17.137+03:00"
source_bytes: 5651
fetched_at: "2026-09-13T04:25:16+00:00"
generator: "netsis-scraper 1.0.0"
---
# Kapasite Planlama Sıkça Sorulan Sorular

**Kapasite planlamanın amaçları nelerdir?**

Belirli bir döneme dair üretim planını gerçekleştirmek için gereksinim duyulacak kaynaklar ile aynı dönem dâhilinde üretimde kullanılacak mevcut kaynakları karşılaştırarak muhtemel kapasite darboğazlarını öngörmek veya mevcut atıl kapasitenin nasıl değerlendirilebileceğine dair çıkar yolları tespit etmektir. Aynı zamanda kapasitenin yetmediği durumlarda darboğazların tespit edildikten sonra önüne geçilmesi için bir üretim planı oluşturmaktır.

**Kapasite planlama uygulamasının kullanımı için ek modül lisansı gerektirir mi?**

MRP modül lisansına sahip olunmalıdır.

**Kapasite planlama uygulamasının etkin bir şekilde kullanılabilmesi için ne gibi tanımlamalar önemlidir?**

MRP Parametrelerinde kapasite planlama sekmesi bulunmaktadır. Bu bölümde öncelikle işletme vardiyaları ve çalışma takvimi tanımlanmalıdır. MRP modülünden kapasite planlama sırasında kullanılacak ürün rotaları ve gerçekleştirilecek operasyonlar, üretim süreleri, iş istasyonlarında bulunan makineler tanımlanmalıdır. Aynı zamanda hazırlık ve transfer sürelerinin de tanımlanarak kapasite planlama yapılırken dikkate alınması sağlanabilir.

**İleri üretim çizelgeleme uygulamasını kullanan işletmelerde tanımlanan makine, rota ve üretim süreleri kapasite planlamada kullanılabilir mi?**

MRP Parametreleri-Kapasite Planlama-Kapasite Planlama Parametrelerinde yer alan Planlama Verisi seçeneğinde Çizelgeleme Üzerinden Getirilsin desteği bulunmaktadır. Bu seçim yapıldığında kapasite planlaması ileri üretim çizelgelemede tanımlanan bilgiler üzerinden oluşturulmaktadır.

**MRP ile kapasite planlama çalıştırıldığında iş emirleri ihtiyaç tarihine planlanıyor ancak ihtiyaç tarihinde işletmedeki makine ve kaynaklar için kapasite yeterli değil. Bu gibi durumların önüne geçmek için kapasite sonuçlarını dikkate alarak planlamanın oluşturulması sağlanabilir mi?**

Kapasite planlama sırasında ilgili periyotta işletme kaynakları için yeterli kapasite bulunmadığı durumlarda oluşacak darboğazların önüne geçmek için dengeleme politikası seçeneği bulunmaktadır. Geriye Doğru Dengeleme Yapılsın parametresinin seçilmesi halinde kapasite kontrol edilerek ihtiyaçlar makinelerin uygun olduğu önceki tarihlere planlanmaktadır.

**Planlanan bir iş için üretiminin gerçekleştirileceği makinede kapasite yeterli olmadığından işin farklı tarihlere bölünerek gerçekleştirilmesi gerekiyor. Aynı işin farklı tarihlere ve alternatif iş merkezlerine bölünerek planlanması sağlanabilir mi?**

Kapasite planlamada geriye doğru dengeleme yapılması durumunda "Kapasite Planlama Parametreleri" bölümünden "İhtiyaçlar Bölünebilsin" seçeneği işaretlenmelidir. Bu sayede kapasite durumları kontrol edilerek ihtiyaçlar farklı tarihlere bölünecektir. Örneğin; 2 hafta sonra tamamlanması gereken 500 adetlik bir iş emri ihtiyacının 300 adetlik kısmı 1. haftaya, kalan 200 adetlik kısmı 2. haftaya planlanmaktadır.

**MRP çalıştırılırken, kapasitenin dikkate alınarak ihtiyaçların belirlenmesi için ne yapılmalıdır?**

Malzeme Gereksinim Planlama menüsünden MRP raporu çalıştırılmadan önce "Kapasite Kullanımları Kontrol Edilsin" parametresi işaretlenmelidir.

**Kapasite planlama sonuç raporlarının farklı periyodlarda görüntülenmesi sağlanabilir mi?**

Kapasite Planlama sekmesinden "Kapasite Sonuç Rapor Gösterimi" alanından sonuç raporunun istenilen periyod bazında görüntülenmesi sağlanabilir.
