---
title: "Geçici Vergi Dönemi Enflasyon Düzeltme"
page_id: "147554888"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Geçici Vergi Dönemi Enflasyon Düzeltme"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Geçici Vergi Dönemi Enflasyon Düzeltme"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTY2NWY0MjkxLTM4ZGItNGY4Yy1hNzI2LWVkNTlmYzQ5NzQ4OCZsaW5rPTU4MWI5YTI1LTFmODktNGRjOS1iYjhkLTM1OWQ0ZDY0MDQ4MCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=665f4291-38db-4f8c-a726-ed59fc497488&link=581b9a25-1f89-4dc9-bb8d-359d4d640480&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "gecici-vergi-donemi-enflasyon-duzeltme_147554888_147554888.html"
source_version: "2024-08-13T15:41:17.340+03:00"
source_bytes: 189148
fetched_at: "2026-09-13T04:22:44+00:00"
generator: "netsis-scraper 1.0.0"
---
# Geçici Vergi Dönemi Enflasyon Düzeltme

**Enflasyon** **Düzeltme**

Stok hesapları dışında kalan hesapların enflasyon taşıma işlemi Muhasebe/İşlemler/Enflasyon Düzeltme ekranından yapılır. 1. Geçici vergi döneminde enflasyon düzeltme işleminin yapılmamasına karar verildiği için ilgili hesaplarda düzeltme 2.Geçici vergi döneminde 6 aylık işlemler üzerinden gerçekleştirilir.

Bu nedenle işlem ekranında Ay Kodu Aralığı 01-06 olarak belirlenir. "Dönem Son Ay İçin Düzeltme" parametresi işaretlenir.

![](../_assets/4f6f896e3d71ec2faabe.png)
Bu parametreler ile işlem başlatıldığında uygulama "Düzeltilecek Stok Hesapları" ekranında tanımı olmayan ancak hesap kartında "Düzeltilecek Hesap" işaretli tüm hesaplar için 01-06 aralığındaki tüm hesap hareketlerini işleme alır.

Hareketlere uygulanacak taşıma katsayısı mali tablonun ait olduğu aya ilişkin fiyat endeksinin, her bir kayıt için işlem gördüğü ayın endeksine bölünmesi ile hesaplanır.

Örneğin Ocak kaydı Haziran Yİ-FE / Ocak Yİ-ÜFE hesabından çıkan katsayı ile, Şubat kaydı ise Haziran Yİ-ÜFE / Şubat Yİ-ÜFE hesabından çıkan katsayı ile düzeltilir.

Örnek: Farklı aylarda hareketleri olan bir hesabın 2. Geçici vergi döneminde enflasyon taşıma adımları ve hesaplamalar

İşlem tarihi bazında uygulanacak katsayılar tabloda görüldüğü gibi her ay için Haziran/ İlgili ay endeksinden hesaplanır.

![](../_assets/07291c30bda3f50f48ec.png)

Bulanan katsayılar işlem tarihine göre hesap hareketlerine uygulanır. Hareket bazında uygulanabileceği gibi ay bakiyesine uygulamakta aynı sonucu verir.

Açılış fişi satırları Aralık ayından gelen bakiyeyi içerdiği için Haziran / 2023-Aralık kaysayısı ile taşınır. Bu nedenle 1000TL'lik satıra 0,19493 (Haziran/Aralık 2023) taşıma katsayısı uygulanır.

![](../_assets/1378e4c5aa0ad758caac.png)
İşlem sonunda ay bazında bulunan fark tutarları 6. Aya yine ay bazında farklı fişler olacak şekilde aktarılır. Açıklamada fişin hangi aydaki farktan oluştuğu bilgisi yer alır.
![](../_assets/ba70f136798a5b0462fd.png)
