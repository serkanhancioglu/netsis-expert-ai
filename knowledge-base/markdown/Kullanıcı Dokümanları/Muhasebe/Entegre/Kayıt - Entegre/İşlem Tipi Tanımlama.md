---
title: "İşlem Tipi Tanımlama"
page_id: "24741007"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Muhasebe"
  - "Entegre"
  - "Kayıt / Entegre"
  - "İşlem Tipi Tanımlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Entegre / Kayıt / Entegre / İşlem Tipi Tanımlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWM4MzZkZjVlLTBjYTktNDc1MS1iNTNlLTU1NTAxZWYyMWVlYiZsaW5rPTI3ZWNhNjFhLTkzZTktNGQzZS1hYTcxLTNhMGVkZDM0NmIxNSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=c836df5e-0ca9-4751-b53e-55501ef21eeb&link=27eca61a-93e9-4d3e-aa71-3a0edd346b15&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "islem-tipi-tanimlama_41164154_24741007.html"
source_version: "2022-09-22T11:04:49.130+03:00"
source_bytes: 39028
fetched_at: "2026-09-13T04:14:45+00:00"
generator: "netsis-scraper 1.0.0"
---
# İşlem Tipi Tanımlama

İşlem Tipi Tanımlama, Muhasebe Bölümü'nde, "Kayıt/Entegre" menüsünün altında yer alır. İşlem Tipi Tanımlama, Entegrasyona ön muhasebe modüllerinden aktarılan kayıtların farklı hale getirilmesi, farklı fişlerde toplanması ve pek çok amaca yönelik değişik tanımlamaların yapılmasını sağlayan bölümdür.

"Entegrasyon" modülüne "Ön Muhasebe" modüllerinden aktarılan kayıtlar, işlem yerlerine göre yedi ayrı bölümde birikir ve buna göre entegre edilir. Entegrasyon kayıtları bölümlerinde bazı kayıtlar bir arada oluşur. Aynı entegrasyon kayıtları bölümüne değişik modüllerden entegre olan kayıtların ayrı fişlerde toplanması istendiği zaman, ya da aynı modülden aktarılan fakat farklı içeriklerde bir araya getirilmesi istenen kayıtlar için farklı işlem tipi tanımlaması yapılabilir.

**Örneğin,** İade satış faturaları satıcı borç mahsubu bölümüne aktarılır fakat "Borç Çek/Senetleri" modüllerinden girilen kayıtlar da aynı bölüme entegre olur. İade satış faturalarının ayrı bir fişte, satıcılara ciro edilen çek ve senetlerin ayrı bir fişte entegre olması istendiği zaman "İşlem Tipi Tanımlaması" yapılır. "Seçenekli Aktarma" bölümünde işlem tipine göre aktarma yapılarak ayrı fişlerde oluşturulması sağlanır. Aynı durum dekont mahsubuna aktarılan kayıtlar içinde geçerlidir. Hem çek tahsili hem karşılıksız çek kaydı aynı mahsup bölümüne aktarılır.

"İşlem Tipi Tanımlamasını" gerektiren başka bir neden ise dekont işlemleri ile ilgilidir. [Entegrasyon Kayıtları](<Entegrasyon Kayıtları.md>) → Dekont sekmesine değişik modüllerden ve bir çok bölümden kayıtlar entegre olarak aktarılır. Fatura → Depolar Arası Transfer İşlemleri, Ambar Giriş/Çıkış Fişleri Kayıtları gibi değişik amaçlı fakat aynı modülden entegre olan kayıtlar vardır. Böyle durumlarda depolar arası transferlerin ayrı, ambar giriş/çıkış fişlerinin ayrı mahsup fişlerinde oluşturulması istenir.

![](../../../../_assets/5ac372a44a7bf26bfef0.png)

İşlem Tipi Tanımlama ekranında yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| İşlem Tipi Tanımlama Ekranı |  |
| --- | --- |
| **İşlem Kodu** | Sekiz karakter uzunluğunda sayısal ve alfabetik kod tanımlamasının yapıldığı alandır. |
| **İşlem Açıklama** | İlgili işlem tipine ait açıklamanın girildiği alandır. "İşlem Tipi Tanımlamaları" bu bölümden tanımlandıktan sonra kayıt bölümlerinde kullanılabilir. Herhangi bir parametresi yoktur. Modüllerde, kayıt bölümlerinden istenen işlem tipi işaretlenerek kayıtlara devam edilir. Modüllerde işlem tipi seçimi için ortak işlem tipi rehberi kullanılır. İşlem tipine göre aktarım, "Seçenekli Aktarma" bölümündeki sorgulamaya verilen işlem koduna göre yapılabilir. Yardımcı Programlar → Kayıt → [Şirket-Şube Parametreleri](<../../Muhasebe Modülü/Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/Genel Tanımlar/Yardımcı Programlar-Şirket-Şube Parametreleri.md>) → “Otomatik İşlem Tipi” seçeneği işaretlendiğinde işlem tipi takibi program tarafından otomatik olarak yapılır. Böylece, kullanıcıların işlem yaptıkları menülerde, işlem tiplerini değiştirmeme/unutma gibi durumlardan kaynaklanan hatalar ortadan kaldırılır. Bunun için farklı menülerden yapılan işlemlere, farklı işlem tipleri belirleyen bir işlem tipi rehberi hazırlanır. Firmalar, işlem tipi rehberini kullanmadan işlemlerini yapabilir ve program yaptıkları işleme ait işlem tipini otomatik olarak entegrasyona aktarır. "İşlem Tipi Tanımlama" bölümüne, işlem tipleri otomatik olarak aktarılır ve istendiği zaman üzerinde değişiklik yapılabilir ya da yeni işlem tipleri eklenebilir. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır. İşlem Tipi Tanımlama kaydının iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
