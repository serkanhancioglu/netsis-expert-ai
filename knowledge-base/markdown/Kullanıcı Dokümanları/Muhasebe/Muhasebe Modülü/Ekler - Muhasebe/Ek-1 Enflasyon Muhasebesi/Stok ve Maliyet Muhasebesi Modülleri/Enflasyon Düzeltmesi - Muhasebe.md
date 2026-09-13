---
title: "Enflasyon Düzeltmesi  / Muhasebe"
page_id: "24740886"
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
  - "Enflasyon Düzeltmesi  / Muhasebe"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / Ekler / Muhasebe / Ek-1 Enflasyon Muhasebesi / Stok ve Maliyet Muhasebesi Modülleri / Enflasyon Düzeltmesi  / Muhasebe"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWViZGQwYmM0LWFiNWEtNGNjNC05MDk4LTJiOTkyYTNiOTFkZSZsaW5rPWE5OWE1NDE4LTU5OTAtNGY3OC1hYmE0LWM5NTViM2U4MmY0OSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=ebdd0bc4-ab5a-4cc4-9098-2b992a3b91de&link=a99a5418-5990-4f78-aba4-c955b3e82f49&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "enflasyon-duzeltmesi-muhasebe_41162338_24740886.html"
source_version: "2022-12-13T08:21:04.947+03:00"
source_bytes: 4360
fetched_at: "2026-09-13T04:14:35+00:00"
generator: "netsis-scraper 1.0.0"
---
# Enflasyon Düzeltmesi / Muhasebe

Enflasyon Düzeltmesi ile ilgili ayrıntılı bilgiye bu dokümandan ulaşılabilir.

Stok kayıtlarında düzeltilmiş tutarların oluşmasından sonra, döneme ait enflasyon düzeltmelerinin yapıldığı işlemdir.

**Yıl Kodu:** İşlemin çalıştırılacağı yıl kodudur.

**Ay Kodu Aralığı:** Yılın ilk ayı ile düzeltmenin yapılacağı ay kodu aralığının girildiği alandır.

Örnekteki stok hareketleri düşünüldüğünde ve işlem 2. ay için çalıştırıldığında, aşağıdaki şekilde düzeltilmiş tutarlar oluşturulur.

| Ay Kodu | İşlem | G/Ç | Miktar | TL.Fiyat | TL.Tutar | Düzeltilmiş Tutar |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Satın Alma | G | 100 | 100 | 10.000 | 10.000 |
| 1 | Sarf | C | 50 | - | - | - |
| 2 | Satın Alma | G | 100 | 120 | 12.000 | 12.000 |
| 2 | Sarf | C | 100 | - | - | - |
| **2-** | **Düzeltme** | **G** |  |  |  | **500** |

\2. ayda oluşan düzeltme kaydı Logo Netsis stok hareketlerine, Tipi ‘E’ (Miktarı Olmayan Maliyet) olan ve TL tutarı bulunmayan (sadece "Düzeltilmiş Tutar" alanında düzeltme değeri bulunan) kayıtlar olarak aktarılır. Düzeltme hareketleri, Muhasebe Modülü ile mutabakat sağlaması açısından girişler, çıkışlar, iade girişler ve iade çıkışlar için ayrı ayrı oluşturulur.

**Vadeli Alış ve Satışlar:** Vadeli alış ve satışların, Muhasebe Modülü bölümünde anlatıldığı gibi enflasyon paylarından arındırılması gerekir. Vade ile ilgili işlem yapılması istendiğinde, aylık ya da yıllık faiz oranı verilmesi gerekir.
