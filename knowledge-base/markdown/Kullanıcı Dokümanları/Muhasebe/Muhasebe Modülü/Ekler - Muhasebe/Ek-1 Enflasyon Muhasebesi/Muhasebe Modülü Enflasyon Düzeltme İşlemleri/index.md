---
title: "Muhasebe Modülü Enflasyon Düzeltme İşlemleri"
page_id: "24740856"
product: "netsis-3-enterprise"
depth: 6
is_section: true
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Muhasebe"
  - "Muhasebe Modülü"
  - "Ekler / Muhasebe"
  - "Ek-1 Enflasyon Muhasebesi"
  - "Muhasebe Modülü Enflasyon Düzeltme İşlemleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / Ekler / Muhasebe / Ek-1 Enflasyon Muhasebesi / Muhasebe Modülü Enflasyon Düzeltme İşlemleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWM2NWQ5YTkyLTZhYTMtNGQ2YS04MGJiLTAxMWRjYjRiYzZjMyZsaW5rPWMzOGUxYTYyLTk3NWUtNDllZi1iZmJkLWUzYzhiYjY4Yjg0NiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=c65d9a92-6aa3-4d6a-80bb-011dcb4bc6c3&link=c38e1a62-975e-49ef-bfbd-e3c8bb68b846&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "muhasebe-modulu-enflasyon-duzeltme-islemleri_41162257_24740856.html"
source_version: "2022-12-12T16:20:13.170+03:00"
source_bytes: 4731
fetched_at: "2026-09-13T04:14:27+00:00"
generator: "netsis-scraper 1.0.0"
---
# Muhasebe Modülü Enflasyon Düzeltme İşlemleri

Muhasebe Modülü Enflasyon Düzeltme İşlemleri ile ilgili ayrıntılı bilgiye bu dokümandan ulaşılabilir.

Logo Netsis Enflasyon Muhasebesi uygulamasında, Enflasyon Muhasebesi (VUK) ve IAS 29 (SPK) olmak üzere iki şekilde düzeltme yapılır.

**Örneğin;**

150-001 hesap kodu TL mizanın 100 olduğu varsayıldığında;

Enflasyon düzeltmesi uygulandığı zaman (endekslenerek yeni değeri bulunduğunda) 110 TL olması gerekir. Bu durumda 10 TL tutarındaki fark işlenir.

**Enflasyon Muhasebesi (VUK) Uygulaması :** Düzeltme farkları enflasyon fark hesaplarına işlenir.

150-001 hesabın enflasyon fark hesabının 150-999 olduğu varsayıldığında;

| Hesap Kodu | TL.Tutar | Toplam |
| --- | --- | --- |
| 150-001 | 100 | 100 |
| 150-999 | 10 | 10 |
| **Enflasyonlu Toplam** |  | **110** |

Program 10 TL tutarındaki farkı, enflasyon fark hesabına işler.

**IAS 29 uygulaması :** Enflasyon düzeltmeleri ikinci bir defter varmış gibi, hareketler üzerinde farklı alanlarda saklanır (**Düzeltme Tipi, Düzeltilmiş Tutar**).

| Hesap Kodu | TL.Tutar | Düzeltilmiş Tutar |
| --- | --- | --- |
| 150-00 | 100 | 100 |
| 150-001 | 0 | 10 |
| **Toplam** | **100** | **110** |

Program 10 TL tutarındaki farkı, hesabın kendi kodunun ikinci alanına (düzeltilmiş tutar) işler ve bu kaydın TL tutarı olmaz.

**Enflasyon Muhasebesi + IAS 29 uygulaması :** Eğer her iki uygulama mevcut ise, programın düzeltme işlemi sonucu hesaplarda oluşacak değerler aşağıdaki şekildedir.

| Hesap Kodu | TL.Tutar | Düzeltilmiş Tutar |
| --- | --- | --- |
| 150-001 | 100 | 110 |
| 150-999 | 10 | 0 |
| **Toplam** | **110** | **110** |

Program hem fark hesabına 10 TL hem de hesabın kendisine düzeltilen tutara 10 TL işler. (Düzeltilmiş tutarlar ayrı raporlanır ve normal koşullar altında resmi defterlerde görünmez. Enflasyon fark hesabına işlenen düzeltme ise resmi defterlerde görünür.)
