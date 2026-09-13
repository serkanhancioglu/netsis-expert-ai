---
title: "Stok Hesapları Düzeltme"
page_id: "24740868"
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
  - "Stok Hesapları"
  - "Stok Hesapları Düzeltme"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / Ekler / Muhasebe / Ek-1 Enflasyon Muhasebesi / Stok Hesapları / Stok Hesapları Düzeltme"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWE3NWZlMTM4LTk3MTctNDQwMC1hYmI4LTBkNTgzMWFlYjRmMSZsaW5rPTJlMmFmODVlLTMzZWUtNDE0Mi05YzZjLTRhM2M4MTYzYjVmYSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=a75fe138-9717-4400-abb8-0d5831aeb4f1&link=2e2af85e-33ee-4142-9c6c-4a3c8163b5fa&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "stok-hesaplari-duzeltme_41162307_24740868.html"
source_version: "2022-12-12T16:39:16.663+03:00"
source_bytes: 11803
fetched_at: "2026-09-13T04:14:33+00:00"
generator: "netsis-scraper 1.0.0"
---
# Stok Hesapları Düzeltme

Stok Hesapları Düzeltme ile ilgili ayrıntılı bilgiye bu dokümandan ulaşılabilir.

Toplulaştırılmış yöntemlerden biri belirlenen hesap kodları için, Enflasyon Muhasebesi (VUK), IAS29 (SPK) uygulamalarından birinde ya da her ikisinde düzeltme işlemini yapan ek işlemdir.

**Yıl Kodu:** İşlemin çalıştırılacağı yıl kodudur.

**Ay Kodu:** Düzeltme işlemi yapılacak ay kodudur.

**Tarih:** Düzeltme işlemi sırasında oluşan yevmiye fişinin aktarılacağı tarihtir. Düzeltme ayının (bitiş ayı) son günü ön değer olarak getirilir.

**Dönem Son Ay Düzeltme: "**Basit Ortalama Yönteminde", Logo Netsis "Enflasyon Muhasebesi" çalışma prensibine uyumsuz olarak, geçici vergi dönemi sonunda, dönem sonu ve dönem başı endekslerinin kullanılması suretiyle düzeltme yapılabilir. Her ay düzeltme yapılmaz. Ancak bu işlemin, diğer yönteme sahip hesapların düzeltilmesi için aylık bazda çalıştırılması gerekebilir. Böyle bir durumda, dönem içindeki aylarda "Dönem Son Ay Düzeltme" alanının işaretlenmemesi, her dönemin son ayında işaretlenmesi gerekir.

İşlem, diğer işlemler gibi aylık yapılır.

**Örneğin;**

150-001 hesabın 3. ay için düzeltilmesi istendiğinde ve 3. ay sonu itibariyle TL bakiyesi 1000 TL borç verdiği varsayıldığında, hesap "Basit Ortalama Yöntemi" ile düzeltilir. Bir önceki dönem sonu (12. ay) enflasyon endeksi 1000, 3. ay enflasyon endeksi ise 1100 olduğunda;

```text
Buna göre ortalama düzeltme katsayısı =           1100              = 1.048
```

```text
                                                                     (1000+1100) / 2
```

| Hesap Kodu | TL.Tutar | Düzeltilmiş Tutar | Açıklama |
| --- | --- | --- | --- |
| 150-001 | 1000 | 1000 |  |
| 150-999 | 48 |  |  |
| 150-001 |  | 48 | IAS29 uygulaması varsa |
| **Toplam** | **1048** | **1048** |  |

Yukarıdaki örnekte verilen hesap, "Stok Devir Hızı" yöntemi ile düzeltilir. Devir hızı tablosu aşağıda belirtilir.

| Kırılım | Oran | Durma Günü |
| --- | --- | --- |
| İlk Madde Malzeme | 100 | 60 |
| İşçilik |  |  |
| Amortisman |  | - |
| Genel Üretim Giderleri |  |  |
| Finansman Gideri |  |  |

Bu durumda 60 günlük (2 aylık) düzeltme yapılır. Her iki ayda enflasyon oranının %10 olduğu ve düzeltme katsayısının 1.1 \* 1.1 = 1.21 olduğu varsayıldığında;

| Hesap Kodu | TL.Tutar | Düzeltilmiş Tutar | Açıklama |
| --- | --- | --- | --- |
| 150-001 | 1000 | 1000 |  |
| 150-999 | 210 |  |  |
| 150-001 |  | 210 | IAS29 uygulaması varsa |
| **Toplam** | **1210** | **1210** |  |

151-001 hesap düzeltilir. "Stok Devir Hızı" yöntemi kullanılacağı varsayıldığında, "Devir Hızı Tablosu" aşağıdaki şekilde belirtilir. Her ay için enflasyon oranı %10 olduğunda, dönem sonu itibariyle hesabın TL bakiyesi 1000 TL borç verir.

| Kırılım | Oran | Durma Günü |
| --- | --- | --- |
| İlk Madde Malzeme | 70 | 90 |
| İşçilik | 10 | 30 |
| Amortisman | 10 | - |
| Genel Üretim Giderleri | 10 | 30 |
| Finansman Gideri |  |  |

Dönemin toplam amortisman gideri 1.000.000 TL, amortisman giderinin düzeltilmiş tutarı 1.200.000 TL olduğu varsayıldığında;

```text
İlk Madde Malzeme:
```

TL tutarın %70’i üç aylık endeksle düzeltilir.

(1000\*0.70)\*1.1\*1.1\*1.1 = 932

```text
İşçilik:
```

TL tutarın %10'u bir aylık endeksle düzeltilecek.

(1000\*0.10)\*1.1 = 110

```text
Amortisman:
```

TL.tutarın %10’u ayrıştırılır.

(1000\*0.10) = 100

Eğer verilmişse, Düzeltilmiş Toplam Amortisman/TL Toplam Amortisman katsayısı ile düzeltilir. Verilmemişse, düzeltilmiş amortismanların yarı mamule girdiği varsayılır ve ayrıca düzeltmeye tabi tutulmaz.

**Genel Üretim Giderleri;**

TL.tutarın %10’u bir aylık endeksle düzeltilecek.

(1000\*0.10)\*1.1 = 110

| Düzeltmeler | Hesaplanan Düzeltilmiş Tutar |
| --- | --- |
| İlk Madde Malzeme | 932 |
| İşçilik | 110 |
| Amortisman | 100 |
| Genel Üretim Giderleri | 110 |
| Finansman Gideri | 0 |
| **Toplam** | **1252** |

| Hesap Kodu | TL.Tutar | Düzeltilmiş Tutar | Açıklama |
| --- | --- | --- | --- |
| 151-001 | 1000 | 1000 |  |
| 151-999 | 252 |  |  |
| 151-001 |  | 252 | IAS29 uygulaması varsa |
| **Toplam** | **1252** | **1252** |  |
