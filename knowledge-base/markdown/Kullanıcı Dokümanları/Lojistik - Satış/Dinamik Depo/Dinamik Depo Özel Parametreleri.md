---
title: "Dinamik Depo Özel Parametreleri"
page_id: "95651006"
product: "netsis-3-enterprise"
depth: 4
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Dinamik Depo"
  - "Dinamik Depo Özel Parametreleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Dinamik Depo / Dinamik Depo Özel Parametreleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTMzYTdhNjQ2LThhMWYtNGVlNS1hMzA3LTU1Njg1ZTRkNTBhNiZsaW5rPTA1MzFlN2MwLWQxOTAtNDFkZi1hYWJjLTRlNDY2ODE3NjgyZiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=33a7a646-8a1f-4ee5-a307-55685e4d50a6&link=0531e7c0-d190-41df-aabc-4e466817682f&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "dinamik-depo-ozel-parametreleri_95651006_95651006.html"
source_version: "2022-11-01T14:54:35.057+03:00"
source_bytes: 4353
fetched_at: "2026-09-13T04:06:22+00:00"
generator: "netsis-scraper 1.0.0"
---
# Dinamik Depo Özel Parametreleri

Dinamik Depo özel parametrelerinin tanımlanması için "[Özel Parametre Tanımlamaları](<../../Genel/Yardımcı Programlar/Kayıt - Yardımcı Programlar/Özel Parametre Tanımları.md>)" ekranı kullanılır.

Hücre Yerleştirme ekranında fiş bakiyesinin getirilmesi için tanımlanması gereken özel parametre aşağıdaki şekildedir:

| Özel Parametre Tanımlamaları Ekranı |  |
| --- | --- |
| Grup Kodu | DINDEPO |
| Anahtar | HUCREBAKIYEGETIRME |

Dinamik Depo Hücre Yerleştirme işleminin zorunlu tutulması için tanımlanması gereken özel parametre aşağıdaki şekildedir:

| Özel Parametre Tanımlamaları Ekranı |  |
| --- | --- |
| Grup Kodu | DINDEPO |
| Anahtar | HAREKET_ZORUNLU |

Kalemler alanında Dinamik Depo Hücre Yerleştirme ekranının otomatik açılması için tanımlanması gereken özel parametre aşağıdaki şekildedir:

| Özel Parametre Tanımlamaları Ekranı |  |
| --- | --- |
| Grup Kodu | DINDEPO |
| Anahtar | OTOMATIKISLEM |

Hücre Yerleştirme/Toplama yapılırken depo hareketine belgenin tarihi (stok hareketlerindeki tarih) atılması için - böylece tüm bakiyeler birbirini tutar - tanımlanması gereken özel parametre aşağıdaki şekildedir:

| Özel Parametre Tanımlamaları Ekranı |  |
| --- | --- |
| Grup Kodu | DINDEPO |
| Anahtar | BELGE_TARIHI_KULLANILSIN |
