---
title: "Görsel Raporlarda Alt Rapor Oluşturma"
page_id: "128583134"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Görsel Raporlarda Alt Rapor Oluşturma"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Görsel Raporlarda Alt Rapor Oluşturma"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTVhOTNlZmQ0LWUwYzEtNGRhZi05NjYyLThhOWZlOTc4ZTc5YiZsaW5rPTljMGYwNjFiLTI4NDYtNDVjOC04YTgzLTY1YWViYTlhMmQ4ZCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=5a93efd4-e0c1-4daf-9662-8a9fe978e79b&link=9c0f061b-2846-45c8-8a83-65aeba9a2d8d&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "gorsel-raporlarda-alt-rapor-olusturma_128583134_128583134.html"
source_version: "2023-12-25T08:30:47.317+03:00"
source_bytes: 1329611
fetched_at: "2026-09-13T04:23:08+00:00"
generator: "netsis-scraper 1.0.0"
---
# Görsel Raporlarda Alt Rapor Oluşturma

Görsel Raporlarda Alt Rapor Oluşturma hakkında ayrıntılı bilgiye bu dokümandan ulaşılır.

Alt Rapor (SubReport), görsel raporlama yapılırken ana rapor içinde başka bir alt raporu göstermek için kullanılan bir rapor bileşenidir. Genellikle, ana rapor içinde daha ayrıntılı bilgilerin gösterimi için kullanılır.

Bu sayede, ana rapor içinde farklı veri kümelerinden alınan veriler birleştirilerek karmaşık raporların daha anlaşılır hale getirilmesi sağlanabilir.

Görsel rapor oluşturmak için, Genel\\Rapor\\Raporlar menüsü "Görsel Rapor" ekranı açılır.

Görsel raporda, ana rapor ve alt rapor verilerinin okunacağı view/tablo nesneleri "Raporlanacak Nesne" alanına eklenir.

Aşağıdaki örnek, müşteri bilgilerini içeren "vw_casabit", sipariş üst bilgileri içeren "vw_sipamas" ve sipariş detay bilgilerini içeren "vw_sipatra" veri tabanı nesneleri ile oluşturulmuştur.
![](../_assets/2f70be6a435166af269a.png)

Raporlanacak nesnelerin seçimi yapıldıktan sonra, sol alt bölümdeki ***"Rapor*** ***Tasarımı"*** seçeneği ile Görsel Rapor Tasarımı ekranı açılır.

![](../_assets/74ee6c8baaeaf9c8bae2.png)

Raporun ilk sayfasında ana raporda gösterilmek istenen veri sahaları ile sayfa tasarımı oluşturulur. Ana rapor ile ilişkili alt raporun eklenmesi için ekran görüntüsünde ok işareti ile belirtilen ***"SubReport Object"*** bileşeni rapor sayfasına eklenerek alt raporun gösterileceği alana konumlandırılır.
Rapor sayfaları sekmesinden alt raporun tasarımının oluşturulacağı sayfaya *"Subreport1"* geçiş yapılır.

![](../_assets/dcf4e5e48712c454ad5e.png)

Bu sayfada, alt rapor içinde gösterilecek veri sahaları rapora eklenir. MasterData band bileşeni içine eklenen alt rapor veri sahalarının üst rapor ile ilişkisini belirlemek için MasterData band nesnesine çift tıklanır ve açılan dataset seçimi ekranındaki ***filter*** alanında ilişkilendirilecek saha isimleri belirtilir.

***Örn; \<vw_sipamas."cari_kodu"\>=\<vw_casabit."cari_kod"\>***

Alt rapor ile ilişkili farklı bir alt rapor eklenmek istendiğinde, "SubReport1" sayfası içinde yeni bir "SubReport Object" bileşeni eklenebilir. Örneğin, ürün bilgilerinin gösterimi için eklenen ikinci subreport bileşeni ekran görüntüsü aşağıdaki gibidir.
![](../_assets/405f84332f1f85132d29.png)

Alt rapor kullanılarak oluşturulan raporun sonuç çıktısı aşağıdaki gibidir.
![](../_assets/6d6d31b16d0a29b3a370.png)
