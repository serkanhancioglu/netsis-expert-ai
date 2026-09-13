---
title: "Sipariş Önerisi Parametreleri"
page_id: "22803810"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Stok"
  - "İşlemler / Stok"
  - "Netsis Sipariş Önerisi"
  - "Sipariş Önerisi Parametreleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Stok / İşlemler / Stok / Netsis Sipariş Önerisi / Sipariş Önerisi Parametreleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWIxNzQwYjA3LWE3ZjktNGU2NC1hMjVlLWQwNzU3YjFkOTEzMiZsaW5rPTgzNzc3M2EyLTEyZTItNDBlZi1iMjhiLTViOTBmMTdkNTBhZCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=b1740b07-a7f9-4e64-a25e-d0757b1d9132&link=837773a2-12e2-40ef-b28b-5b90f17d50ad&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "siparis-onerisi-parametreleri_29997615_22803810.html"
source_version: "2022-10-26T10:49:20.297+03:00"
source_bytes: 5635
fetched_at: "2026-09-13T04:04:50+00:00"
generator: "netsis-scraper 1.0.0"
---
# Sipariş Önerisi Parametreleri

Sipariş Önerisi Parametreleri ekranı Lojistik-Satış Bölümü'nde, "İşlemler/Stok " menüsünün altında yer alır.

Sipariş Önerisi Parametreleri ekranında yer alan parametreler ve içerdiği bilgiler şunlardır:

| Sipariş Önerisi Parametreleri Ekranı |  |
| --- | --- |
| Önceki Database | "Hesaplamada Geri Gidilecek Gün" parametresi için kullanılacak şirket isminin girildiği alandır. Ortalama kullanım miktarı hesaplanırken, "Hesaplamada Geri Gidilecek Gün" alanına girilen gün değeri, şirketin içinde bulunduğu tarihten daha eski bir tarihe gidilmesini gerektiriyorsa, bu alana girilecek şirketin stok hareketlerinden bilgi alınır. **Örneğin:** 31.03.2018 tarihinde ortalama kullanım miktarı hesaplatıldığı ve hesaplamada geri gidilecek gün olarak 180 gün girildiği varsayıldığında, 90 günlük bilgi, içinde bulunulan şirketin stok hareket kayıtlarından alınır. Kalan 90 günlük bilgi ise, bu alana girilen şirketin stok hareket kayıtlarından alınır. |
| Fiyat | Stokların ABC kodlarının bulunmasında baz alınacak fiyatın belirlendiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile, fiyat seçenekleri arasından seçim yapılır. Bir malın hangi ABC kodunda olduğu, [ABC Tanımlama](<ABC Tanımlama.md>) bölümünde girilen tutarlar dikkate alınarak bulunur. Hesaplanan ortalama kullanım miktarı, bu alandaki fiyat değeri ile çarpılır ve "ABC Tanımlama" bölümünde kaydedilen tutarlar ile karşılaştırılarak, stokların ABC kodları bulunur. Seçilecek olan satış ve alış fiyatları (fiyat listeleri kullanılıyor ise), ilgili fiyat listelerinden alınarak, diğer fiyatlar ise stok kartlarından aktarılır. |
| Yaratılış Geri Gidilecek Gün | Daha önce açılmış olan stoklar için "Ortalama Kullanım Miktarı" hesaplanmasını sağlayan alandır. **Örneğin:** Yaratılış Geri Gidilecek gün sayısı olarak 100 değeri girildiğinde, tanımlanma (kayıt) tarihi 100 günden fazla olan stoklar için ortalama kullanım miktarı hesaplanır. |
| Hesaplamada Geri Gidilecek Gün | Ortalama kullanım miktarı hesaplanırken, başlangıç tarihi olarak bu alana girilen gün değeri kadar geri gidilir. Bulunan tarihten hesaplamanın yapıldığı tarihe kadar olan stok çıkış hareketleri (muhtelif, irsaliye, kapalı fatura, açık fatura, muhtelif fatura), dikkate alınır. Bulunan başlangıç tarihi, içinde bulunulan şirketten elde edilemiyorsa, "Önceki Database" alanında girilen şirketten ulaşılır. |
| Bölen | Bulunacak ortalama kullanım miktarının günlük, haftalık, aylık, altı aylık veya yıllık olarak hesaplanması sağlayan alandır. **Örneğin:** Hesaplamada Geri Gidilecek Gün: 180 Bölen: 6 girildiği varsayıldığında, Aylık ortalama kullanım miktarı 180/6=30 olarak hesaplanır. Hesaplamada Geri Gidilecek Gün: 30 Bölen: 30 girildiği varsayıldığında, Günlük ortalama satış miktarı 30/30=1 olarak hesaplanır. Kısaca, "Hesaplamada Geri Gidilecek Gün" ve "Bölen" alanlarına girilen değerlere göre, istenen tarih aralığındaki ortalama satış miktarı hesaplanabilir. |
