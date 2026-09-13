---
title: "Ek-2 (Ölçü Birimi Uygulamaları)"
page_id: "29993145"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Stok"
  - "Ekler (Stok)"
  - "Ek-2 (Ölçü Birimi Uygulamaları)"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Stok / Ekler (Stok) / Ek-2 (Ölçü Birimi Uygulamaları)"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWE1NGEwNWUxLWVlMTQtNGI3OS1hNTI3LWM0YTJmYjc5MTg1ZCZsaW5rPWU1NTE0Y2JhLWEyNGUtNDc4Ny04NTcxLTQwMDQ0MGIxNWExNCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=a54a05e1-ee14-4b79-a527-c4a2fb79185d&link=e5514cba-a24e-4787-8571-400440b15a14&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ek-2-olcu-birimi-uygulamalari_30000614_29993145.html"
source_version: "2022-11-22T11:33:27.363+03:00"
source_bytes: 309893
fetched_at: "2026-09-13T04:05:27+00:00"
generator: "netsis-scraper 1.0.0"
---
# Ek-2 (Ölçü Birimi Uygulamaları)

Ölçü Birimi Uygulamaları ile ilgili detaylı bilgiye bu dokümandan ulaşılır.

Stokların birden fazla ölçü birimine göre işlem görebilmesi için yapılması gereken tanımlamalar ve bu tanımlamalar sonucu programdaki kullanımlarının anlatıldığı bölümdür.

**Stok Kartında Yapılan Tanımlamalar**

Stok kartında yapılan tanımlamalar aşağıdaki şekildedir:

![](../../../../_assets/19628cb7b8680c7fced2.png)

- Stokların birden fazla ölçü birimine sahip olmaları halinde, "Stok Kartı Kayıtları" ekranında yer alan "Ölçü Birimi" sekmesindeki "Sabit Tanımlamalar" ve "Çoklu Ölçü Birimi" bölümlerinden, stoka ait birden fazla ölçü birimi girişi yapılır.

Stok girişlerinin ne şekilde yapılacağı ile ilgili detaylı bilgi için; Stok → Kayıt → [Stok Kartı Kayıtları](<../Kayıt - Stok/Stok Kartı Kayıtları/index.md>)

- Yukarıdaki örnekte; stok kartı için hem "Sabit Tanımlamalar" hem de "Çoklu Ölçü Birimi" bölümlerinde ölçü birimi girişi yapılmış. "Sabit Tanımlamalar" bölümünde girilen ölçü birimleri Çoklu Girişleri Güncelle ![](../../../../_assets/975d8b87e19407bdc6a7.png) butonu kullanılarak "Çoklu Ölçü Birimi" bölümüne aktarılmış.
- "Sabit Tanımlamalar" bölümünden girilen AD, KG ve PK ölçü birimleri, stok raporlarında ve fatura belgelerinde kullanılır. Ancak "Çoklu Ölçü Birimi" bölümünden girilen ölçü birimlerinin stok raporlarında ve fatura belgelerinde kullanılması için öncellikle "Birim Seçimi" alanlarında "Çoklu Ölçü Birimi" bölümünden girilen ve "Sabit Tanımlamalar" bölümünde bulunmayan iki ölçü birimi seçilir. Dolayısıyla, farklı stoklara farklı sayıda farklı ölçü birimleri tanımlandığı için fatura kaydında ve stok raporlarında ölçü birimi 1,2,3 haricinde **"Birim Seçimi"** bölümünde seçilen iki ölçü birimi de dahil olmak üzere raporlama ve çevrim işlemi yapılır.
- "Çoklu Ölçü Birimi" bölümünden girilen, "Sabit Tanımlamalar" ve "Birim Seçimi" bölümlerinde bulunmayan ölçü birimleri sadece bilgi amaçlıdır. Fatura işlemleri ve stok raporlarında, bu ölçü birimleri için çevrim yapılmaz. Bu durumda, yukarıdaki örneğe göre "Sabit Tanımlamalar" bölümünde bulunmayan ancak "Birim Seçimi" bölümüne girilen KL ve CV ölçü birimleri, fatura ve stok raporlarında kullanılabilir.
- "Çoklu Ölçü Birimi" bölümünde tanımlanan ve "Birim Seçimi" bölümüne girilmeyen Ölçü birimleri (Örneğin; KT), "Sabit Tanımlamalar" bölümünde yer almadığından, çevrim için kullanılmaz. Sadece Rapor Modülünde bulunan "Serbest Raporlar" bölümünden raporlanır.

Faturada stok kaleminin kaydedilmesi sırasında kullanılan ölçü biriminin "Sabit Tanımlamalar" bölümünde bulunan ilk ölçü biriminden farklı olduğu durumlarda, kullanılan ölçü birimine ait bilgi TBLSTHAR tablosundaki OLCUBR alanında saklanır. Ayrıca bu ölçü biriminin kullanıldığı anda tanımlı pay/payda değeri de yine aynı tablodaki CEVRIM alanında saklanır. Dolayısı ile, ölçü birimlerine ait pay/payda değerleri veya "Birim Seçimi" bölümünde girilen ölçü birimlerinde değişiklik yapılmış stoklar için hareket raporu alındığında, geçmişe yönelik hareketlerde tutarsızlık meydana gelir. Bunun için, tanımlanan ölçü birimlerinde ve bunlara ait pay/payda değerleri ile "Birim Seçimi" bölümünde girilen ölçü birimlerinde değişiklik yapılmaması önerilir.

**Raporlarda Ölçü Birimi Kullanımı**

Stok Modülünde bulunan ve ölçü birimi seçimine göre çevrim yapılmasını sağlayan raporlarda, "Ölçü Birimi" alanı aşağıdaki şekilde ekrana gelir. Böylece, "Sabit Tanımlamalar" bölümündeki üç ölçü birimi ve "Birim Seçimi" bölümündeki iki ölçü birimine göre rapor alınması sağlanır.

![](../../../../_assets/a7c155724b77cf30db07.png)

**Fatura Belgelerinde Ölçü Birimi Kullanımı**

Alış ve Satış Parametreleri bölümünde bulunan "Farklı Birimlerden Mal Girişi Yapılsın" ve "Farklı Birimlerden Mal Çıkışı Yapılsın" parametrelerinin işaretlenmesi halinde, fatura belgelerinde "Miktar" alanından önce, girilecek miktarın hangi ölçü birimi üzerinden olacağı ile ilgili belirleme yapılması için en fazla beş adet ölçü biriminin sorgulanacağı "Çevrim Değeri" alanı ekrana gelir. Stok kartında belirlenen ölçü birimlerinden biri seçilerek işleme devam edilir. Aşağıdaki örnekte, stok kartında tanımlı altı adet ölçü birimi olmasına rağmen, bunlardan beş tanesi "Çevrim Değeri" alanına getirilmiş. Bunun sebebi, üçünün "Sabit Tanımlamalar" bölümünde bulunması (AD, KG, PK), ikisinin de "Birim Seçimi" alanlarına (KL, CV) girilmesinden kaynaklanır.

![](../../../../_assets/43a1a448a75c8a838440.png)

**Koşul Kayıtlarında Çoklu Ölçü Birimi Kullanımı**

"Çoklu Ölçü Birimi" özelliği koşul uygulamasında da desteklenir.

Koşul Kayıtları ile ilgili detaylı bilgi için; Cari → Kayıt → Koşul Kayıtları → Detay Koşul Kayıtları

"Detay Koşul Kayıtları" bölümünde, satış işlemlerinde kullanılacak ve ön değer olarak getirilecek ölçü birimi desteği bulunur.

![](../../../../_assets/07e8eda75e97817af9c0.png)

Bu işlemin amacı, aynı malın farklı satıcılardan farklı ölçü birimleri ile alınması halinde, satıcı bazında kullanılan ölçü biriminin ön değer olarak gelmesidir.

**Örneğin:** A malı B satıcısında KL olarak C satıcısından da AD olarak alındığı varsayıldığında, B satıcısına fatura keserken faturada otomatik olarak KL ölçü birimi gelir. İsteğe bağlı değiştirilebilir. Aynı şekilde C satıcısına fatura keserken AD ölçü birimi gelir.

Fatura belgelerinde, "Detay Koşul Kayıtları" bölümünde belirlenen ölçü birimlerinin program tarafından otomatik olarak ekrana getirilmesi için "Faturada Farklı Birimlerden Mal Çıkışı Yapılsın" ve "Sipariş/İrsaliye/Faturada Koşul Uygulaması Kullanılsın" parametrelerinin açık olması gerekir.

**Stok Ölçü Birimi Kayıtlarının Kullanımı**

Stok Ölçü Birimi Kayıtları, tek bir stok ya da ortak özelliklere sahip stok grupları bazında, stok kartında yapılan tanımlamalardan farklı pay/payda değerleri tanımlanması amacıyla kullanılır.

Stok Ölçü Birimi Kayıtlarının kullanılması için; Fatura → Kayıt → Satış Parametreleri → "Ölçü Birimleri Tablodan Okunsun" ve "Ölçü Birimleri Hangi Grup Koduna Göre Getirilsin" parametresinin belirlenmesi gerekir. Stok Ölçü Birimi Kayıtlarının stok kartında girilen ölçü birimleri ile ilişkisini bir örnekle açıklanacak olursa; "Kod-" alanı 'K01' olan stokların kutular halinde satılması halinde, kullanılan ölçü birimlerinin ve bu ölçü birimlerine ait pay/payda değerlerinin aynı olduğu varsayıldığında ve stok kartındaki "Kod-1" alanı 'K01' olan bir stok için girilen ölçü birimleri aşağıdaki şekilde kullanıldığında, "KT" kodlu ölçü biriminin fatura kayıtlarında kullanılması için stok kartında yer alan "Sabit Tanımlamalar" ya da "Çoklu Ölçü Birimi" alanlarında tanımlanması gerekir. Tanımlanan ölçü biriminin "Birim Seçimi" alanlarından birine de girilmesi gerekir. Aksi halde, "Stok Ölçü Birimi Kayıtları" bölümünde söz konusu ölçü birimi için tanımlama yapılsa bile, fatura kayıtlarında kullanılması mümkün değildir.

![](../../../../_assets/4c8802479c078f8e012e.png)

"Kod-1" alanı "K01" olan stokların kutu olarak satılması halinde kullanılacak ölçü birimine ait ortak pay/payda değerlerinin oluşturulması için aşağıda yer alan ekrandaki gibi bir tanımlama yapılır. Stok Ölçü Birimi Kayıtları girildikten sonra, fatura kayıtlarında ilgili stok için "Çevrim Değeri" alanının "KT" olarak seçilmesi gerekir. Böylece, "Çevrim Değeri" alanının yanında bulunan rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) aktif hale gelir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, Stok Ölçü Birimi Kayıtları için yapılan tanımlamalar arasından seçim yapılır.

İlgili ölçü birimi seçildikten sonra, Stok Ölçü Birimi Kayıtları için rehberden seçim yapılmadan direkt miktar girişi yapılırsa; çevrim, stok kartında girilen pay/payda değerlerine göre yapılır.

![](../../../../_assets/d0ac81e8568cd56e9d63.png)

"Çevrim Değeri" alanında "KT" ölçü birimi seçildikten sonra aktif hale gelen rehberde, "Stok Ölçü Birimi Kayıtları" bölümünde girilen değerler seçildikten sonra "Miktar" alanına 1 değeri girilmesine rağmen, "Miktar" alanı stok kartında yer alan "Sabit Tanımlamalar" bölümündeki 1.ölçü birimine çevrilerek 5 olarak değişir. Böylece, çevrim işlemi stok kartında girilen pay/payda değerlerine göre değil, "Stok Ölçü Birimi Kayıtları" bölümünde girilen değerlere göre yapılır.

![](../../../../_assets/31ff692895ca770493a1.png)
