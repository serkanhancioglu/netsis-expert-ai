---
title: "Ek-5 (Bölgesel Alış/Satış Raporu İçin Yapılması Gerekenler)"
page_id: "29993151"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Stok"
  - "Ekler (Stok)"
  - "Ek-5 (Bölgesel Alış/Satış Raporu İçin Yapılması Gerekenler)"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Stok / Ekler (Stok) / Ek-5 (Bölgesel Alış/Satış Raporu İçin Yapılması Gerekenler)"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTBjOTdkYzg1LTY4YzktNDY3MC1iZjk5LWUzYTRkM2U1ZjVlOSZsaW5rPTYzM2FmOWE1LTZhY2MtNGZiNS1iZWUzLTI4ZWJkYWE0YTMxZiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=0c97dc85-68c9-4670-bf99-e3a4d3e5f5e9&link=633af9a5-6acc-4fb5-bee3-28ebdaa4a31f&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ek-5-bolgesel-alis-satis-raporu-icin-yapilmasi-gerekenler_30001172_29993151.html"
source_version: "2022-11-22T11:37:45.420+03:00"
source_bytes: 328969
fetched_at: "2026-09-13T04:05:29+00:00"
generator: "netsis-scraper 1.0.0"
---
# Ek-5 (Bölgesel Alış/Satış Raporu İçin Yapılması Gerekenler)

Bölgesel alış/satış raporu için yapılması gerekenler ile ilgili ayrıntılı bilgiye bu dokümandan ulaşılır.

Raporda sağlıklı veri alınması için öncelikle, "Cari Hesap Kayıtları" bölümünde bulunan "İl" ve "Ülke" alanlarının doğru şekilde girilmesi gerekir. Bu rapor Türkiye için hazırlandığından dolayı "Ülke Kodu" alanında TR girilmeyen cariler rapora dahil edilmez. "İl" alanına da mutlaka rehberde olan bilgilerin girilmesi gerekir.

![](../../../../_assets/1bcc5081fc7949251031.png)

Bu bilgiler Genel → Yardımcı Programlar → Kayıt → "[Şehir Kayıtları](<../../../Genel/Yardımcı Programlar/Kayıt - Yardımcı Programlar/Şehir Kayıtları.md>)" bölümünde girilen kayıtlardan aktarılır. Programın kurulumu sırasında, Türkiye'deki iller Logo Netsis tarafından ilgili bölüme kaydedilir ve bu kayıtlar üzerinde değişiklik yapılmaması gerekir. Aksi halde, cari kartta il tanımlı olsa da harita ile eşleştirilmez. "Şehir Kayıtları" bölümünde bulunan herhangi bir il için değişiklik yapılması halinde, raporlama sırasında program uyarı verir.

**Örneğin:** Cari il bilgileri girildikten sonra "Şehir Kayıtları" bölümünden İzmir iline ait kayıtta değişiklik yapıldığı varsayılarak rapor alındığında, cari kartlardaki il bilgileri şehir kayıtlarındaki il bilgileri ile eşleştirilemiyorsa, aşağıdaki uyarı ekrana gelir.

![](../../../../_assets/31714d5dde6945df6b48.png)

Uyarı ekranında da belirtildiği gibi, uyuşmazlık yaşanan cariler "Geçersiz Cariler" sekmesinde listelenir.

![](../../../../_assets/0a2e69e98b2b90726dde.png)

Böyle bir durum ile karşılaşıldığında, "Şehir Kayıtları" bölümünden il bilgisinin düzeltilmesi gerekir.
