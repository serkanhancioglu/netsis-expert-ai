---
title: "Netsis İhracat e-Fatura Uygulaması"
page_id: "47084849"
product: "netsis-3-enterprise"
depth: 6
is_section: true
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Fatura"
  - "Kayıt / Fatura"
  - "E-Fatura İşlemleri"
  - "Netsis İhracat e-Fatura Uygulaması"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Fatura / Kayıt / Fatura / E-Fatura İşlemleri / Netsis İhracat e-Fatura Uygulaması"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWFlZDUwOGE5LTFiNjktNGVjOC04MjI2LTIyYmFiOWMzMDBmNCZsaW5rPTNiM2NmNTY4LWIwYmYtNDFlYy1hZTIwLWYwMjlkMTJmZjdiMiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=aed508a9-1b69-4ec8-8226-22bab9c300f4&link=3b3cf568-b0bf-41ec-ae20-f029d12ff7b2&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-ihracat-e-fatura-uygulamasi_47084851_47084849.html"
source_version: "2022-10-24T14:26:33.507+03:00"
source_bytes: 2925
fetched_at: "2026-09-13T04:02:12+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis İhracat e-Fatura Uygulaması

**Genel Uygulama**

İhracat e-Fatura uygulaması, ihracat e-Fatura uygulamasına kayıtlı mükelleflerin ihracat faturalarının e-Fatura olarak düzenlenmesine zorunluluk getirilmesi ile kullanılan bir uygulamadır.

**Kurulum**

Netsis İhracat e-Fatura uygulamasının kurulumu için yapılması gerekenler şunlardır:

- "Netsis Entegre" paketini kullanan firmanın "Dekont" modülünde “İthalat – İhracat İşlemleri Lisansı” bulunması gerekir.
- "Netsis Standard" veya "Enterprise" paketi kullanan firmaların, "Dış Ticaret" modülü lisansının bulunması gerekir.
- Bu lisanslar ile beraber e-Fatura Parametreleri → “İhracat Faturaları e-Fatura Olarak Oluşturulsun” parametresi aktif olarak gelir. “İhracat Faturaları Belge Birim Kodlarınızı Buradan Girebilirsiniz” yazısının üzerine tıklandığında açılan "Çoklu Seri Giriş" ekranı içinde “Belge Birim Kod” belirlenebilir.

**Tanımlamalar**

İhracat e-Fatura kullanmadan önce aşağıdaki tanımlamaların yapılması gerekir:

- Lojistik-Satış → Fatura → Kayıt → e-Fatura İşlemleri → "Paket Tanımları" ya da Lojistik-Satış → Dış Ticaret → Kayıt → "Paket Tanımları" ekranından paket koduna ait “Paket Markası” ve “Paket Cinsi” tanımlamalarının yapıması gerekir.
- Lojistik-Satış → Fatura → Kayıt → e-Fatura İşlemleri → "Ödeme Açıklamaları" ya da Lojistik-Satış → Dış Ticaret → Kayıt → "Ödeme Açıklamaları" ekranından ödeme tipine ait "Uluslararası Ödeme Kodu" tanımlamalarının yapılması gerekir.

**Kullanım**

İhracat e-Fatura kullanımı, "Fatura" ya da "Dış Ticaret" modülü kullanılarak iki farklı şekilde yapılabilir.
