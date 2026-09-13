---
title: "Serbest Raporlarda Table Valued Function Kullanımı"
page_id: "153157731"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Serbest Raporlarda Table Valued Function Kullanımı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Serbest Raporlarda Table Valued Function Kullanımı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWMzNjNlMzhhLTk3MzgtNDA2Mi05NTdkLTcyM2M5ODdlOTM4ZiZsaW5rPTAwM2EzYjU3LTMxOWEtNDJjYi04OTBlLTMyZmM3NWQ5OWQ0MyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=c363e38a-9738-4062-957d-723c987e938f&link=003a3b57-319a-42cb-890e-32fc75d99d43&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "serbest-raporlarda-table-valued-function-kullanimi_153157731_153157731.html"
source_version: "2024-09-26T15:45:12.623+03:00"
source_bytes: 146937
fetched_at: "2026-09-13T04:22:35+00:00"
generator: "netsis-scraper 1.0.0"
---
# Serbest Raporlarda Table Valued Function Kullanımı

Serbest Rapor ve Görsel Rapor ekranlarında Table Valued Function desteği ile parametre kullanımının gerekli olduğu durumlarda, geriye tablo şeklinde değer döndürülerek rapor sonuçları elde edilebilmektedir.

Table Valued Function, parametre alabilen ve sorgu sonucunda geriye bir tablo döndüren fonksiyon tipidir.

Aşağıda, "Tarih" ve "Kasa Kodu" parametrelerini alarak geriye günlük kasa raporunu bir tablo sonucu olarak döndüren Table Valued Function örneği bulunmaktadır.
![](../_assets/e01fda38b3d7f0edad1d.png)

Görsel Rapor ekranı Tanımlı Nesneler alanında, veri tabanında kayıtlı Table-View nesnelerinin yanı sıra Table Function nesneleri de listelenmektedir.

![](../_assets/e5c145eecd74f1761626.png)

Function nesnesi seçim yapıldıktan sonra bir sonraki sekmede raporda gösterilecek sahalar belirlenmektedir.

![](../_assets/cc6dc89c89ae1bb3c1b8.png)

Aralık/Maske sekmesinde ise Function parametreleri seçim yapılarak parametrelere gönderilecek değerlerin girişi yapılmaktadır.

![](../_assets/a71ebc52c311cfb24909.png)

Örnek rapor sonucu aşağıdaki gibidir.

![](../_assets/7f85c5986e229d9adf9c.png)
