---
title: "Stok Özel Parametreleri"
page_id: "47076028"
product: "netsis-3-enterprise"
depth: 4
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Stok"
  - "Stok Özel Parametreleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Stok / Stok Özel Parametreleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTJjMzNhZGYyLTdmODMtNDhlZi04NTM1LTJjMjM0MTA0NGI1MyZsaW5rPWE5ZWI3NDM1LWMwYzAtNDAyNS1iYmJhLTMyYTcwOTgwOTRhMSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=2c33adf2-7f83-48ef-8535-2c2341044b53&link=a9eb7435-c0c0-4025-bbba-32a7098094a1&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "stok-ozel-parametreleri_47076038_47076028.html"
source_version: "2022-11-01T14:47:12.410+03:00"
source_bytes: 2897
fetched_at: "2026-09-13T04:05:30+00:00"
generator: "netsis-scraper 1.0.0"
---
# Stok Özel Parametreleri

Stok özel parametrelerinin tanımlanması için "[Özel Parametre Tanımlamaları](<../../Genel/Yardımcı Programlar/Kayıt - Yardımcı Programlar/Özel Parametre Tanımları.md>)" ekranı kullanılır.

Stok Kartı "Dosya Saklama" Alanında, Gösterimin Son Eklenenden İlk Eklenene Doğru Yapılmasının Sağlanması için tanımlanması gereken özel parametre aşağıdaki şekildedir:

| Özel Parametre Tanımlamaları Ekranı |  |
| --- | --- |
| Grup Kodu | STOK |
| Anahtar | DOSYA_KAYIT_TARIHINE_GORE_GELSIN |

Stok Hareket Kayıtları Ekranında, Gride Tanımlanan Filtrenin Bir Sonraki Kayda Geçildiğinde de Tanımlı Kalmasının Sağlanması için tanımlanması gereken özel parametre aşağıdaki şekildedir:

| Özel Parametre Tanımlamaları Ekranı |  |
| --- | --- |
| Grup Kodu | STOK |
| Anahtar | GRIDFILTRE |

İlgili özel parametre tanımlandığında, Grid'deki filtreler sonraki veya önceki kayda geçerken sıfırlanmaz.
