---
title: "ABC Tanımlama"
page_id: "22803773"
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
  - "ABC Tanımlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Stok / İşlemler / Stok / Netsis Sipariş Önerisi / ABC Tanımlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWE3NWQ2MjFjLWFlYTgtNGVkYy1hZGY3LTcxZDgyY2ZhODRiZSZsaW5rPTg1MTFkZTYwLTkyYzgtNGUzZC04Y2MyLWUyMjQwYWY2OTNhZSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=a75d621c-aea8-4edc-adf7-71d82cfa84be&link=8511de60-92c8-4e3d-8cc2-e2240af693ae&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "abc-tanimlama_22804501_22803773.html"
source_version: "2022-10-26T10:22:52.827+03:00"
source_bytes: 8988
fetched_at: "2026-09-13T04:04:50+00:00"
generator: "netsis-scraper 1.0.0"
---
# ABC Tanımlama

ABC Tanımlama, Finans Bölümü'nde, "İşlemler/Stok " menüsünün altında yer alır. Ürünler için önem kodlarının tanımlandığı bölümdür.

ABC Tanımlama ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| ABC Kodlama Ekranı |  |
| --- | --- |
| ABC Kodu | En fazla 8 karakterden oluşacak önem kodunun alfa numerik olarak tanımlandığı alandır. **Örneğin:** A, B, C.., 1,2,3.. veya 01,02 şeklinde tanımlanabilir. ABC kodu tanımlamadaki amaç; stoktaki malları en önemliden en önemsize doğru sıralamak ve buna göre stokta bulundurulması gereken miktarın hesaplanmasını sağlamaktır. **Örneğin:** Firma için satışı en yüksek ve önemli olan stoklar için önem kodu A, satışı orta düzeyde ve önem derecesi daha az olan stoklar için B, satışı düşük ve önem derecesi en az olan stoklar için ise C tanımlaması yapılabilir. |
| Katsayı | Stokların elde ne kadar süreyle bulundurulması gerektiği ve buna göre satıcıya ne kadar sipariş verileceği ile ilgili hesaplama yapılmasını sağlayan alandır. **Örneğin:** Bir mal için hesaplanan aylık ortalama satış miktarı 30, katsayı olarak 2 (aylık hesaplama yapıldığı için) değeri girilmişse, bu maldan stokta en az 60 adet (2 aylık) bulundurulması gerektiği anlaşılır. Girilen katsayı değeri, ortalama kullanım miktarı hesaplamasının yapıldığı döneme göre değişir. Yani, haftalık ortalama satış miktarı hesaplatıldığında; girilen 2 katsayısı, stokta 2 haftalık (2\*7=14) malın bulundurulması gerektiğini ifade eder. |
| Tutar | Bir malın hangi önem kodunda olduğu bu alana girilen tutar ile belli olur. **Örneğin:** ABC Kodu: A (önem derecesi yüksek stok) Katsayı: 2 Tutar: 100 TL olarak girildiği varsayıldığında; [Sipariş Önerisi Parametreleri](<Sipariş Önerisi Parametreleri.md>) ekranındaki alanlara girilen bilgilere göre, ortalama kullanım miktarı bir mal için 30 (satış miktarı/bölen) olarak hesaplandığında, bu değer ile 2 ile çarpılarak 60 rakamı bulunur. Bulunan değer, malın en az 60 adet bulundurulması gerektiğini ifade eder. [Sipariş Önerisi Parametreleri](<Sipariş Önerisi Parametreleri.md>) ekranındaki "Fiyat" alanı "Satış fiyatı-1" olarak seçildiğinde ve bu değer 4 TL olarak girildiğinde, 30 (ortalama kullanım miktarı) X 4 TL =120 TL tutarında bir rakam bulunur. Bu tutar, A önem kodu için girilen tutardan daha büyük bir tutar olduğu için, stokun önem kodu A olur. Bulunan tutara uygun başka bir önem kodu var ise, bu stokun önem kodu başka bir değer alır. **Örneğin:** ```text<br>ABC KODU KATSAYI TUTAR<br>``` ```text<br>A 1 500 TL<br>``` ```text<br>B 2 120 TL<br>``` ```text<br>C 2 50 TL<br>``` Yukarıdaki tanımlamaya göre örnekteki stokun ABC kodu B'dir. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır.

Kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
