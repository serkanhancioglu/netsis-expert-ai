---
title: "Karbon Ayak İzi Hesaplama"
page_id: ""
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Karbon Ayak İzi Hesaplama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Karbon Ayak İzi Hesaplama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTMxMmY0MDY2LThmNzctNDE0MC04YmNhLTcwYWI1OWYyZTNhOSZsaW5rPTg1YzE1ZTk1LWFkZjYtNGRhNi1iY2Q5LWFjNmIxMThjNzgzMiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=312f4066-8f77-4140-8bca-70ab59f2e3a9&link=85c15e95-adf6-4da6-bcd9-ac6b118c7832&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "karbon-ayak-izi-hesaplama.html"
source_version: ""
source_bytes: 9838
fetched_at: "2026-09-13T04:21:49+00:00"
generator: "netsis-scraper 1.0.0"
---
# Karbon Ayak İzi Hesaplama

Karbon ayak izi; bireylerin, kurumların veya ürünlerin faaliyetleri sonucu atmosfere saldığı sera gazlarının toplam miktarını ifade eder. Başka bir ifadeyle karbon ayak izi, insanların doğaya bıraktığı çevresel etkinin bir göstergesidir.

Karbon ayak izi, günlük yaşamda yapılan birçok faaliyet sonucu ortaya çıkar. Elektrik kullanımı, ulaşım (araçlar, uçaklar), ısınma (doğalgaz, kömür vb.), gıda üretimi ve tüketimi, ürünlerin üretimi ve taşınması. Bu faaliyetler sonucunda atmosfere karbondioksit ve diğer sera gazları salınır.

9.065 sürümüyle birlikte, faturalar için **Karbon Ayak İzi** hesaplama özelliği desteklenmiştir.

İşletmelerin satın alma ve satış işlemleri esnasında oluşturdukları fatura belgelerinde belge bazında sürdürülebilirlik takibi için gerekli olan tüketim tipi, yakıt tipi, tüketim miktarı gibi veri girişlerinin yapılabilmesi, bu verilere göre belge bazında çevreye bırakılan karbon ayak izinin hesaplanması ve raporlanması desteklenmiştir.

Alış ve Satış Fatura ekranlarında Toplamlar sekmesinde sağ tık menüsüne **Karbon Ayak İzi Hesaplama Bilgi Girişi** eklenmiştir. Bu ekran üzerinde, belgeye ait karbon ayak izi hesaplaması için gerekli olan tüketim tipleri girilir.

Bu ekran üzerinde yer alan fatura numarası ve cari bilgileri ile hangi belge için işlem yapıldığı takip edilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/56ed5f70-f0a7-4acc-bba8-66bb60f4372d/karbon1_de.png)

Tüketim Tipi kısmında, Hava Ulaşımı, Kara Ulaşımı, Elektrik tüketimi, Isınma Değerleri ve Su Tüketimi olmak üzere toplam 5 tane farklı tüketim tipi bulunmaktadır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/2c3d3ba5-1efb-4ef9-aa64-1dc9bc0b408b/karbon2_de.png)

Tüketim tipi olarak **Hava Ulaşımı** seçilmesi durumunda, Uçuş Süresi (Tek Yön) ve Uçuş Sayısı alanları aktif olur. Birim kısmı pasif ama Saat olarak gösterilmektedir.

Örneğin, 3 saatlik bir uçuş süresi ve 2 defa uçuş olduğunda, kayıt gride atıldığında Hava Ulaşımı tüketim tipi için, satır bazında CO2 salınımı kg cinsinden gösterilmektedir. Aynı zamanda dip toplamda da tüm tüketim tipleri için toplam CO2 salınımı ton cinsinden hesaplayarak göstermektedir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/8a6c981b-dbf2-42dd-a0fc-5aad6c2a8f44/karbon3_de.png)

Tüketim tipi olarak **Kara Ulaşımı** seçilmesi durumunda, yakıt türü ve tüketim miktarı kısımları aktif olur. Birim kısmı litre (lt) olacak şekilde pasif görünmektedir. Yakıt türü olarak benzin, lpg, dizel ve fuel-oil seçenekleri mevcuttur.

Örneğin, yakıt türü Benzin olup 500 ltlik bir harcama girildiğinde ve yakıt türü Dizel olup 300 ltlik bir harcama girildiğinde, kayıtlar gride satır bazında atılır. Kara Ulaşımı tüketim tipi için, satır satır yakıt türü bazında CO2 Salınımı kg cinsinden gösterilmektedir. Aynı zamanda dip toplamda da tüm tüketim tipleri için toplam CO2 salınımı ton cinsinden hesaplayarak göstermektedir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/ce58aa14-2110-40de-a734-c007dc7f9eb9/karbon4_de.png)

Tüketim tipi olarak **Elektrik Tüketimi** seçilmesi durumunda, sadece tüketim miktarı aktif olur. Birim kısmı KiloWatSaat (kWh) olacak şekilde pasif görünmektedir.

Örneğin, 1000 kWh bir tüketim girilip kayıt gride atılır. Benzer şekilde Elektrik Tüketim tipi içinde, satır bazında CO2 Salınımı kg cinsinden gösterilmektedir. Aynı zamanda dip toplamda da tüm tüketim tipleri için toplam CO2 salınımı ton cinsinden hesaplayarak göstermektedir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/3ba34d9c-8ee2-4f34-9556-f50ca81a71db/karbon5_de.png)

Tüketim tipi olarak **Isınma Değerleri** seçilmesi durumunda, yakıt türü ve tüketim miktarı kısımları aktif olur. Yakıt türü olarak doğalgaz, kömür, lpg ve fuel-oil seçenekleri mevcuttur. Doğalgaz seçiminde birim m3, kömür seçiminde kg ve lpg/fuel-oil seçiminde ise lt olarak gelmekte ve pasif olarak görünmektedir.

Örneğin, yakıt türü Doğalgaz olup 1000 metreküp (m3) bir harcama girilip kayıt gride atılır. Isınma Değerleri tüketim tipi için, yakıt türü bazında CO2 Salınımı kg cinsinden gösterilmektedir. Aynı zamanda dip toplamda da tüm tüketim tipleri için toplam CO2 salınımı ton cinsinden hesaplayarak göstermektedir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/301095a4-f0cc-49a3-8de8-70f1608709cb/karbon6_de.png)

Son olarak Tüketim tipi olarak **Su Tüketimi** seçilmesi durumunda, sadece tüketim miktarı kısmı aktif olur. Birim kısmı metreküp (m3) olacak şekilde pasif görünmektedir.

Örneğin, 1000 metreküp (m3) bir harcama girilip kayıt gride atılır. Su Tüketimi için, diğer tüketim tiplerinden farkı CO2 salınımını etkileyen bir değer olmadığı için satır bazında bu tüketim tipi için herhangi bir co2 salınımı hesaplanmamaktadır. Bu nedenle toplam değeri etkilememektedir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/821927ec-77ca-4660-8f03-fc089c2e8a9d/karbon7_de.png)

Harcama verilerinin girişi sonrası ilgili ekran kapatılır ve belge tamamlanır.

**Sürdürülebilirlik 360 Raporu**

Belge bazında girilen bu değerleri raporlamak için Sürdürülebilirlik 360 raporu kullanılmaktadır.

Bu raporda Veri Seçimi Bölümünde Su Tüketimi, Elektrik Tüketimi, Isınma, Hava Ulaşımı, Kara Ulaşımı, Karbon Ayak İzi, kara Ulaşımı CO2 Salınımı (Kg), Isınma CO2 Salınımı (Kg), Doğaya Ağaç Borcu seçenekleri bulunmaktadır. Sürdürülebilirlik 260 raporunda görünmesi istenen satırlar seçilerek kaydedilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/bd058c9d-1b3f-42f5-a4f1-6980ac87b4f9/karbon8_de.png)

Veri seçimi sonrasında raporda Karbon Ayak İzi hesaplamaları ile ilgili detay bilgiler görsel olarak raporlanmaktadır. Ayrıca Doğaya Ağaç Borcu kısmında ise, doğaya salınan karbondioksite karşılık ne kadar ağaç dikilmesi gerektiği hesaplanmaktadır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/ecc85f18-2a7b-4dbf-b406-b6fc4e66858d/karbon9_de.png)
