---
title: "Diğer Parasal Olmayan Hesaplar"
page_id: "24740872"
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
  - "Diğer Parasal Olmayan Hesaplar"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / Ekler / Muhasebe / Ek-1 Enflasyon Muhasebesi / Diğer Parasal Olmayan Hesaplar"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTYyOTM0ZjY2LWY5M2UtNGUyYS1hMDc2LTQ4ZGUwMWRiZjZiMCZsaW5rPTg3MzY1OTU5LWZjMjktNGY1My04MGY5LThlNmNhYjAxM2FkZiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=62934f66-f93e-4e2a-a076-48de01dbf6b0&link=87365959-fc29-4f53-80f9-8e6cab013adf&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "diger-parasal-olmayan-hesaplar_41162231_24740872.html"
source_version: "2022-12-12T16:10:15.293+03:00"
source_bytes: 7151
fetched_at: "2026-09-13T04:14:22+00:00"
generator: "netsis-scraper 1.0.0"
---
# Diğer Parasal Olmayan Hesaplar

Diğer Parasal Olmayan Hesaplar ile ilgili ayrıntılı bilgiye bu dokümandan ulaşılabilir.

Stok ve demirbaş dışında kalan diğer parasal olmayan kalemler (Sermaye, İştirakler, Hisse senetleri, Verilen/Alınan Avanslar, Gelecek Dönemlere Ait Giderler ve Gelirler gibi) düzeltme katsayıları kullanılarak düzeltilir. Enflasyon düzeltmesine tabi tutulan bu değerlerin elden çıkarılması ya da başka hesaplara aktarılması gibi işlemlerde yapılan enflasyon düzeltmeleri maliyet addedilir. Yani, elden elden çıkarılan değerin düzeltilmiş değer olması gerekir.

**Örneğin;**

X firmasının 1. ayda 100 birim stok için 1.000 TL/birim tutarında avans ile, 3. ayda yine 100 birim stok için 1.000 TL/birim tutarında avans ödediği ve daha sonra 4. ayda avansı ödenmiş olan 150 birim malın stoklara girildiği varsayıldığında;

Her ay enflasyon oranı %10, düzeltme katsayısı 1.1’dir. Buna göre;

| Ay Kodu | Hesap Kodu | TL Tutar | Açıklama |
| --- | --- | --- | --- |
| 1 | 159-001 | 100\*1000=100,000 | Dönem içi işlemler |
| 2 | 159-999 | 10,000 | 1.ay 159-001 düzeltmesi |
| 3 | 159-001 | 100\*1000=100,000 | Dönem içi işlemler |
| 3 | 159-999 | 10,000 | 2.ay 159-001 düzeltmesi |
| 3 | 159-999 | 1,000 | 2.ay 159-999 düzeltmesi |
| **4** | **159-001** | **\<150\*1,000\>=****\<150,000\>** | **Dönem içi işlemler** |
| 4 | 159-999 | 20,000 | 3.ay 159-001 düzeltmesi |
| 4 | 159-999 | 1,100 | 3.ay 159-999 düzeltmesi |
| **4** | **159-999** | ? | Dönem içi işlem düzeltme |

Yukarıdaki örnekte; 4. ayda aktifleşen 150 birimlik stok maliyeti, verilen avansların düzeltilmiş değerleriyle oluşan maliyeti olmalı. Bu maliyet, gelen stokun alış fiyatı ve düzeltilmiş tutarı tespit edildiğinde yazılabilir. Ancak, çok fazla giriş çıkış olan hesaplarda, çıkış hareketinin hangi girişten kaynaklandığı tespit edilemeyebilir. Bu durumda maliyet, "Ağırlıklı Ortalama" yöntemiyle aşağıdaki şekilde hesaplanır;

Verilen Avanslar Toplam Birim = 200 birim

Verilen Avanslar Toplam Düzeltilmiş Tutar (159-001 + 159-999) = 243.100 TL

Bir Birim Stok Düzeltilmiş Maliyeti = 243.100 / 200 = 1.215,5

Aktifleşen Stok Toplam Düzeltilmiş Maliyeti = 1.215,5 \* 150 = 182.325

**159-999 hesaptan çıkış yapılması gereken tutar: 32.325 TL**

Örnekte olduğu gibi, bu tür parasal olmayan hesapların maliyetlendirme işleminin yapılması sırasında, ilgili hesapla karşılıklı çalışan yevmiye satırlarına düzeltilmiş maliyet bedellerinin taşınması gerekir. Stokun aktif olması için, TL muhasebe açısından yapılması gereken fiş kaydı aşağıdaki tabloda yer alır.

| Hesap Kodu | TL.Tutar |
| --- | --- |
| 159-001 | \<150,000\> |
| 150-001 | 150.000 |

Bu fiş, düzeltilmiş değerler ile birlikte kaydedilseydi;

| Hesap Kodu | TL.Tutar | Açıklama |
| --- | --- | --- |
| 159-001 | \<150,000\> | TL işlem |
| 159-999 | \<32.325\> | Enflasyon fark hesabı |
| 150-001 | 150,000 | TL işlem |
| 150-999 | 32.325 | Enflasyon fark hesabı |

gibi kayıtların oluşması gerekirdi.

> [!NOTE]
> Düzeltilmiş maliyet birebir tespit ediliyorsa virman işleminde bu maliyet girilebilir.
