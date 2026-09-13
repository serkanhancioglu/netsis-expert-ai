---
title: "Maliyet Oluşturma / Muhasebe"
page_id: "24740891"
product: "netsis-3-enterprise"
depth: 7
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Muhasebe"
  - "Muhasebe Modülü"
  - "Ekler / Muhasebe"
  - "Ek-1 Enflasyon Muhasebesi"
  - "Stok ve Maliyet Muhasebesi Modülleri"
  - "Maliyet Oluşturma / Muhasebe"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / Ekler / Muhasebe / Ek-1 Enflasyon Muhasebesi / Stok ve Maliyet Muhasebesi Modülleri / Maliyet Oluşturma / Muhasebe"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTZlOTQ4OTNmLTE3ZDQtNGNmNi1iZTEwLWFlN2QzZWM4YTE1ZiZsaW5rPTc5MDdmMGRkLTBmNzUtNDFjOS04YzBiLTk1MDRmMDAwNWQyMiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=6e94893f-17d4-4cf6-be10-ae7d3ec8a15f&link=7907f0dd-0f75-41c9-8c0b-9504f0005d22&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "maliyet-olusturma-muhasebe_41162348_24740891.html"
source_version: "2022-12-13T08:24:15.160+03:00"
source_bytes: 2586
fetched_at: "2026-09-13T04:14:37+00:00"
generator: "netsis-scraper 1.0.0"
---
# Maliyet Oluşturma / Muhasebe

Maliyet Oluşturma ile ilgili ayrıntılı bilgiye bu dokümandan ulaşılabilir.

Stok işlemlerindeki son adım maliyet oluşturma işlemidir. İşlemin düzeltmeleri dikkate alması için, enflasyona çevrim ve enflasyon düzeltmesi işlemlerinin yapılması gerekir.

Bu işlemler yapıldığında ve örnekteki hareketler düşünüldüğünde, maliyet oluşturma işlemi TL ve düzeltilmiş maliyetler aşağıdaki şekilde oluşturulur:

| Ay Kodu | İşlem | G/Ç | Miktar | TL.Fiyat | TL.Tutar | Düzeltilmiş Tutar |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Kalan | G | 50 | 100 | 5.000 | 5.000 |
| 2 | Satın Alma | G | 100 | 120 | 12.000 | 12.000 |
| **2** | **Sarf** | **C** | **100** | **113.33** | **11.333** | **11.667** |
| 2 | Düzeltme | G |  |  |  | 500 |
