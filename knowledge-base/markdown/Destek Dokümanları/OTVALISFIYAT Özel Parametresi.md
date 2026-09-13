---
title: "OTVALISFIYAT Özel Parametresi"
page_id: ""
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "OTVALISFIYAT Özel Parametresi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / OTVALISFIYAT Özel Parametresi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTlmNTM4OTk5LTJkYmUtNDQ5Ni1iMjJkLWY4NmFmNjllMzlkOSZsaW5rPTA5NzVkNWY4LWRjMDQtNGY5NS1iNTkwLWJmZmZkZmMzZGZlZiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=9f538999-2dbe-4496-b22d-f86af69e39d9&link=0975d5f8-dc04-4f95-b590-bfffdfc3dfef&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "otvalisfiyat-ozel-parametresi.html"
source_version: ""
source_bytes: 2611
fetched_at: "2026-09-13T04:21:59+00:00"
generator: "netsis-scraper 1.0.0"
---
# OTVALISFIYAT Özel Parametresi

Maliye Bakanlığı, ÖTV Genel Tebliği ile araç satışlarında indirim oranı yüksek gösterilerek matrahın düşürülmesini önlemek amacıyla bu oranlara sınırlama getirmiştir. Tebliğe göre, 2 sayılı listedeki motorlu araçlarda hesaplanan ÖTV, alış bedeli üzerinden ilgili oranda hesaplanan tutardan düşük olamaz.

Netsis’te satış faturasında ÖTV’nin alış matrahı üzerinden hesaplanabilmesi için FATURA/OTVALISFIYAT özel parametresi kullanılır. Bu parametre tanımlandığında, kalemler sayfasındaki 'Özel Fiyat' alanı aktif olur ve ÖTV matrahı buradan girilir

Örneğin, %4 ÖTV ile 200.000 TL’ye aldığım aracı 100.000 TL’ye, yani alış matrahının altında bir fiyata sattığımda, Bakanlık ÖTV’nin yine alış matrahı üzerinden ve aynı oranda (%4) hesaplanmasını zorunlu kılmaktadır.

Bunu sağlamak için;

Netsis’te satış faturasında ÖTV’nin alış matrahı üzerinden hesaplanabilmesi için FATURA/OTVALISFIYAT özel parametresi tanımlanır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/ee21a2a7-fe32-45c5-ac8b-198df4dc242f/ozelparam.jpg)

Bu parametre tanımlandığında, kalemler sayfasındaki 'Özel Fiyat' alanı aktif olur ve ÖTV matrahı buradan girilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/ec616f8c-0743-4f00-b738-538ae40354ef/KALEMGIRISIjpg.jpg)

Bu durumda ÖTV, %4 oranla 200.000 TL’lik alış matrahı üzerinden hesaplanarak 8.000 TL olurken, faturada brüt toplam 100.000 TL olarak gösterilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/a73c956f-b58a-4ea1-85c7-fb262fb11db8/TOPLAMLAR.jpg)

Bu yöntemle, ÖTV hesaplamasının uygulanan iskontolardan etkilenmesi engellenmiş olur.
