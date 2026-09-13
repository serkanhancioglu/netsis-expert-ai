---
title: "Maliyet Muhasebesi / Muhasebe"
page_id: "24740894"
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
  - "Maliyet Muhasebesi / Muhasebe"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / Ekler / Muhasebe / Ek-1 Enflasyon Muhasebesi / Stok ve Maliyet Muhasebesi Modülleri / Maliyet Muhasebesi / Muhasebe"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWVjM2M2ZmZmLTIwYmMtNGIwNS1iN2YzLTMwODRlMmRlZDc1YyZsaW5rPTUzNTNkNjI4LTRkMWUtNDZlMC1hOTM5LWRiYzk1ODE5NTg1OCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=ec3c6fff-20bc-4b05-b7f3-3084e2ded75c&link=5353d628-4d1e-46e0-a939-dbc958195858&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "maliyet-muhasebesi-muhasebe_41162342_24740894.html"
source_version: "2022-12-13T08:22:18.010+03:00"
source_bytes: 5258
fetched_at: "2026-09-13T04:14:37+00:00"
generator: "netsis-scraper 1.0.0"
---
# Maliyet Muhasebesi / Muhasebe

Maliyet Muhasebesi modülü ile ilgili ayrıntılı bilgiye bu dokümandan ulaşılabilir.

Maliyet Muhasebesi Modülünün; stok, demirbaş ve muhasebe modüllerinde düzeltme yapıldıktan sonra, son adım olarak çalıştırılması gerekir. Bu durum, düzeltilmiş maliyetlerin oluşmasından kaynaklanır.

> [!NOTE]
> Enflasyon Muhasebesi (VUK) + IAS29 (SPK) her iki uygulamayı da yapan firmalar, Maliyet Muhasebesi Modülünde ancak uygulamaların birine ait düzeltilmiş maliyetleri hesaplatma işlemi yapabilir. Diğer uygulama için "Toplulaştırılmış Yöntem" uygulamak zorundadır. Hangi uygulama için Toplulaştırılmış Yöntem, hangisi için Maliyet Modülünün kullanılacağı muhasebe parametrelerinde belirlenir.

> [!NOTE]
> Maliyet muhasebesi Modülü düzeltme işlemi ve düzeltilmiş maliyet hesaplamasını ikinci defter mantığında yapar. Bu işlemlerde enflasyon fark hesapları düşünülmez. Ancak oluşturulan mahsup fişlerinin muhasebeleştirilmesi sırasında, fark hesaplarına ayrıştırılarak aktarılır.

**Örneğin;**

Yarı Mamul

ilk madde örneğindeki sarfları dikkate alarak 2. ayda 150 adet yarı mamul üretildiği varsayıldığında (Örnekte, yarı mamul üzerinde ilk madde dışında herhangi bir maliyet faktörünün bulunmadığı düşünülür);

| Stok Kodu | Ay Kodu | G/Ç | Miktar | TL Fiyat | TL Tutar | Düzeltilmiş Tutar |
| --- | --- | --- | --- | --- | --- | --- |
| İlk Madde | 1 | C | 50 | 100 | 5.000 | 5.500 |
| İlk Madde | 2 | C | 100 | 111.33 | 11.333 | 11.667 |
| **Yarı Mamul** | **2** | **G** | **150** | **108.89** | **16.333** | **17.167** |

Maliyet Muhasebesi, yarı mamul ve mamul maliyetlerini hem TL hem de düzeltilmiş olarak çift defter mantığında oluşturur. Düzeltilmiş maliyetleri oluştururken bilgi aldığı tüm modüllerden düzeltilmiş bilgileri alır. Bu nedenle, tüm düzeltme işlemlerinin yapılması gerekir. Gider hesaplarının enflasyon fark hesaplarındaki farkların da alınması için, fark hesaplarının maliyet muhasebesi tanımlarında verilen maskelere uygun olarak açılması (gider hesap maskesinin, hem hesabın kendisini hem de enflasyon fark hesabını kapsaması) gerekir.

Maliyet Muhasebesi Modülünden oluşturulan muhasebe fişleri düzeltilmiş değerlerle oluşacağı için, Enflasyon Muhasebesi işleminde tekrar düzeltmeye tabi tutulmaması gerekir. Bu nedenle, maliyet muhasebesi işlemlerinin tüm düzeltmelerden sonra, son adım olarak yapılması gerekir.
