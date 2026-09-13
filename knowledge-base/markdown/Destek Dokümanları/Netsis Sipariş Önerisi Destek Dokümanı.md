---
title: "Netsis Sipariş Önerisi Destek Dokümanı"
page_id: "159547423"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis Sipariş Önerisi Destek Dokümanı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis Sipariş Önerisi Destek Dokümanı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTEyZjZjNTQwLTFmNjktNGUyNC04Y2Q1LTc3ZDQ4MmNmYmNmZCZsaW5rPTViMDZhMTFkLTc5YTMtNDcwOS05MDgwLWI3MmMzOTlkMmY0OSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=12f6c540-1f69-4e24-8cd5-77d482cfbcfd&link=5b06a11d-79a3-4709-9080-b72c399d2f49&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-siparis-onerisi-destek-dokumani_159547423_159547423.html"
source_version: "2024-11-25T18:10:56.037+03:00"
source_bytes: 1239605
fetched_at: "2026-09-13T04:22:30+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis Sipariş Önerisi Destek Dokümanı

Netsis Sipariş Önerisi ile program tarafından otomatik olarak bulunan sipariş öneri miktarlarının izlenebilmesi ve düzenleme yapılabilmesi sağlanmaktadır.

Sipariş ön izleme öncesinde gerekli parametre ve tanımlamaların yapılması gerekmektedir.

Tanımlama ve işlem adımları detayları aşağıdaki gibidir.

İlkolarak"SiparişÖnerisiParametreleri"ekranındailgilitanımlamalarınyapılması gerekmektedir.

Parametreleri ekranında yer alan parametreler ve içerdiği bilgiler şunlardır:

**Önceki Database:** "Hesaplamada Geri Gidilecek Gün" parametresi için kullanılacak şirket isminin girildiği alandır. Ortalama kullanım miktarı hesaplanırken, "Hesaplamada Geri Gidilecek Gün" alanına girilen gün değeri, şirketin içinde bulunduğu tarihten daha eski bir tarihe gidilmesini gerektiriyorsa, bu alana girilecek şirketin stok hareketlerinden bilgi alınır.

**Fiyat:** Stokların ABC kodlarının bulunmasında baz alınacak fiyatın belirlendiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile, fiyat seçenekleri arasından seçim yapılır. Seçilecek olan satış ve alış fiyatları (fiyat listeleri kullanılıyor ise), ilgili fiyat listelerinden alınarak, diğer fiyatlar ise stok kartlarından aktarılır.

**Yaratılış Geri Gidilecek Gün**: Daha önce açılmış olan stoklar için "Ortalama Kullanım Miktarı" hesaplanmasını sağlayan alandır.

Örneğin: Yaratılış Geri Gidilecek gün sayısı olarak 100 değeri girildiğinde, tanımlanma (kayıt) tarihi 100 günden fazla olan stoklar için ortalama kullanım miktarı hesaplanır.

**Hesaplamada Geri Gidilecek Gün:** Ortalama kullanım miktarı hesaplanırken, başlangıç tarihi olarak bu alana girilen gün değeri kadar geri gidilir. Bulunan tarihten hesaplamanın yapıldığı tarihe kadar olan stok çıkış hareketleri (muhtelif, irsaliye, kapalı fatura, açık fatura, muhtelif fatura), dikkate alınır. Bulunan başlangıç tarihi, içinde bulunulan şirketten elde edilemiyorsa, "Önceki Database" alanında girilen şirketten ulaşılır.

**Bölen:** Bulunacak ortalama kullanım miktarının günlük, haftalık, aylık, altı aylık veya yıllık olarak hesaplanması sağlayan alandır.

"Hesaplamada Geri Gidilecek Gün" ve "Bölen" alanlarına girilen değerlere göre, istenen tarih aralığındaki ortalama satış miktarı hesaplanabilir.

Parametre girişinin ardından "ABC Tanımlama" ekranından ABC kodları tanımlanmalıdır.

Bu bölüm ürünler için önem kodlarının tanımlandığı bölümdür.

ABC Tanımlama ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

**ABC Kodu:** En fazla 8 karakterden oluşacak önem kodunun alfa numerik olarak tanımlandığı alandır. ABC kodu tanımlamadaki amaç; stoktaki malları en önemliden en önemsize doğru sıralamak ve buna göre stokta bulundurulması gereken miktarın hesaplanmasını sağlamaktır.

**Katsayı:** Stokların elde ne kadar süreyle bulundurulması gerektiği ve buna göre satıcıya ne kadar sipariş verileceği ile ilgili hesaplama yapılmasını sağlayan alandır. Girilen katsayı değeri, ortalama kullanım miktarı hesaplamasının yapıldığı döneme göre değişir. Yani, haftalık ortalama satış miktarı hesaplatıldığında; girilen 2 katsayısı, stokta 2 haftalık (2\*7=14) malın bulundurulması gerektiğini ifade eder.

**Tutar:** Bir malın hangi önem kodunda olduğu bu alana girilen tutar ile belli olmaktadır.

Tanımlamaların ardından öncelikle OKM-ABC İzleme ardından Sipariş Önerisi Hazırlık işlemi gerçekleştirilmektedir. Tüm bu bilgilere göre sipariş önerisi hazırlık çalıştırıldığında aşağıdaki formüle göre ihtiyaç hesaplanmaktadır.

Ortalama Kullanım Miktarı X Katsayı – (Stok Bakiyesi +++ Satıcı Sipariş Bakiyesi)

++ **+Müşteri** **Sipariş** **Bakiyesi**

Tanımlama ve işlem adımları aşağıda örneklendirilmiştir.

Öncelikle "Sipariş Önerisi Parametreleri" ekranından tanımlamalar gerçekleştirilmektedir.

![](../_assets/62de5161ef6ffddafc5d.png)

Sonrasında "ABC Tanımlama" ekranında ürünler için önem kodları tanımlanmaktadır.

![](../_assets/d2d8eecf854de03a1713.png)

Yukarıdaki parametrelere göre; Satış miktarı / bölen = 40 / 4 = 10 olarak ortalama kullanım miktarı bulunmaktadır.
![](../_assets/5857da28a426f0b008ef.png)

ABC analizinde ise, Ortalama kullanım miktarı \* satış fiyatı = 10 \* 90 = 900 TL olduğu için B grubuna dahil olacaktır.

Sırasıyla OKM-ABC İzleme ardından Sipariş Önerisi Hazırlık işlemi gerçekleştirildikten sonra yine yukarıda paylaşılan formüle göre ihtiyaç hesaplanmaktadır.
![](../_assets/3ef564a412c418eaff5b.png)

![](../_assets/159339b31f3a3da85077.png)
Ortalama Kullanım Miktarı X Katsayı – (Stok Bakiyesi + Satıcı Sipariş Bakiyesi) + Müşteri Sipariş Bakiyesi 10 x 2 – (-15 +0) + 0 = 35 adet.

Verilen sipariş önerisi değiştirilememekte ancak oluşturulacak siparişin miktarına müdahale edilebilmektedir.

![](../_assets/cb57308f773e1335e9d0.png)
