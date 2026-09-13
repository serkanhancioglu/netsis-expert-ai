---
title: "Siparişte Stoktan Ayırma"
page_id: "115608409"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Siparişte Stoktan Ayırma"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Siparişte Stoktan Ayırma"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWIxNjYxOTQ1LWIzZDktNGI4Ny05OGVlLTQyY2UzYTY3M2Y1OSZsaW5rPWU2ZWNlZDYyLTk1ZDgtNDBiNS1hYmUxLTI3MTc5OGE5ZDBlZiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=b1661945-b3d9-4b87-98ee-42ce3a673f59&link=e6eced62-95d8-40b5-abe1-271798a9d0ef&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "sipariste-stoktan-ayirma_115608409_115608409.html"
source_version: "2023-07-21T09:49:33.927+03:00"
source_bytes: 1421034
fetched_at: "2026-09-13T04:23:17+00:00"
generator: "netsis-scraper 1.0.0"
---
# Siparişte Stoktan Ayırma

Siparişte Stoktan Ayırma hakkında ayrıntılı bilgiye bu dokümandan ulaşılır.

Müşteri siparişlerinin stokta mevcut olduğu ya da temin edilmesi gerekliliğini takip edebilmek için Müşteri Siparişleri modülünde kalem bilgileri ekranında S/B kutucuğu işaretlenerek stoktan ayırma işlemi yapılmaktadır.
.
![](../_assets/ac655003abd8d1c25f5f.png)
Bu durumda müşteri siparişini girerken stoktan ayırmak için (S), temini beklemeye almak için de (B) kodu kullanılır. Müşteri siparişi kaydı sırasında, stok kalemleri bazında karşınıza gelecek olan kutucukta, ilgili stoktan mevcut ise (S)toktan ayır, yoksa temini (B)eklemede şeklinde kayıt girilir.

Buradaki S/B kutucuğu, Satış Parametreleri/Fatura Sipariş sekmesinde "Siparişte Stoktan Ayırma Yapılsın" parametresi işaretli olduğunda aktif olur.

![](../_assets/df9e7fd9ff2599c2acca.png)

Aşağıdaki örnekte elimizde 100 adet mevcut olan stoğumuz için müşteri siparişi girerken 80 adet stoktan ayırma işlemi yapılmıştır.

![](../_assets/f0fcf0ec6ca1d889bbea.png)
![](../_assets/727f6b4b7f0c53b2532c.png)

Yapılan stoktan ayırma işlemi Stok Kartı Kayıtları ekranında Tutar/Miktar Bilgileri kısmında Ayrılmış Stok alanında görülür.

![](../_assets/609a6e5f568270d93bdb.png)
Bu ayrımlar Müşteri Bazında Sipariş Raporu ve Mal Bazında Müşteri/Satıcı Raporu modüllerinde incelenebilir.

![](../_assets/070c34486b511747df32.png)

![](../_assets/a954a7482ffe28933694.png)

Siparişten ayrılan (rezerve edilen) bölüm, aslında stok bakiyesi olmasına rağmen çıkışına izin verilmez.

![](../_assets/134e17493f05b63cc060.png)

Satış Faturası ekranında Sipariş/İrsaliye Bilgileri alanında rehberden ilgili sipariş çağırılarak Fatura Oluştur denildiğinde "Sipariş teslimatınız yapılsın mı? "Ekranı açılır.

![](../_assets/32b599d42683e6366d14.png)

Bu alanda ayrılan stokun istenilen kadarı faturalaştırılır.

![](../_assets/d838836b7ff6580e97b7.png)

80 adet ayrılmış stokun 50 adedi faturalaştırılarak teslim edildiğinde kalan miktar Stok Kartı Kayıtları modülünde Sipariş Bakiyesi kısmında izlenebilir.

![](../_assets/a7a6f4463894aa7db11d.png)

Aynı şekilde carinin bu sipariş için kalan bakiyesi Müşteri Bazında Sipariş Raporu ve Mal Bazında Müşteri/Satıcı Raporu modüllerinde görünür.

![](../_assets/405cbcdfa2d1a8a45ec1.png)
![](../_assets/b4991902904af1384d69.png)
**EK BİLGİ:**
Satış parametreleri/Fatura Sipariş sekmesinde "Siparişte Stoktan Ayırma Yapılsın" parametresi işaretli olduğunda Mamul Rezervasyonu Oluşturma ekranı kullanılamamaktadır. Bu parametre işaretli ise sistemde sipariş bazında rezervasyon açık olsa bile Mamul Rezervasyon Oluşturma ekranı gelmez.
