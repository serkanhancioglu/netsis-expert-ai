---
title: "Sayım Farkını Satış Hareket İşleme"
page_id: "22803756"
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
  - "Stok Sayım İşlemleri"
  - "Sayım Farkını Satış Hareket İşleme"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Stok / İşlemler / Stok / Stok Sayım İşlemleri / Sayım Farkını Satış Hareket İşleme"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTlhYjhmZTc4LTc5N2ItNGY1ZS1iZTNmLWNiMzRlOTQ3NDM3NiZsaW5rPWJmZDA4ZTRiLTIxMWUtNGFhZC1hYTM3LTE0ZDJjYjUxNTM1NSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=9ab8fe78-797b-4f5e-be3f-cb34e9474376&link=bfd08e4b-211e-4aad-aa37-14d2cb515355&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "sayim-farkini-satis-hareket-isleme_29996799_22803756.html"
source_version: "2022-10-26T09:59:52.170+03:00"
source_bytes: 62618
fetched_at: "2026-09-13T04:04:41+00:00"
generator: "netsis-scraper 1.0.0"
---
# Sayım Farkını Satış Hareket İşleme

Sayım Farkını Satış Hareket İşleme, Lojistik - Satış Bölümü'nde, "İşlemler/Stok" menüsünün altında yer alır. Sayım Farkını Satış Hareket İşleme, sayım ile bilgisayardaki bakiyeler arasında fark veren stokların, sayım sonuçlarına göre "Stok Hareket Kayıtları" bölümünde yer alan bakiyelerin düzenlenmesi için kullanılan işlemdir.

Sayım Farkını Satış Hareket İşleme ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Sayım Farkını Satış Hareket İşleme Ekranı |  |
| --- | --- |
| Sayım Tarihi | Sayım Girişi/ Lokal Depo Sayım Girişi bölümünden girilen stokların sayım tarihinin girildiği alandır. Bu alana sayım bilgisi olmayan herhangi bir tarihin girilmemesi gerekir. |
| Depo Kodu Aralığı | Sayım bilgisinin lokal depo bazında girilmesi halinde kullanılan alandır. Lokal depo kodu aralığı verilmesi halinde, sadece o lokal depoya/depolara ait fark miktarı aktarılır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, depo kodları arasından seçim yapılır. |
| Cari Kodu | Lokal depoları cari koda bağlantılı olarak (örneğin; satış noktaları bazında) tanımlayan firmaların kullandığı alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, cari kodlar arasından seçim yapılır. |
| Hareket Tarihi | Sayım fark miktarlarının stok hareketlerine aktarılması istenen tarihin girildiği alandır. |
| Maliyet İçin Sınır Tarihi | Sayım miktar farkı olan stok hareketlerine aktarım yapılırken, fark birim fiyat ve fark maliyet tutarlarının hesaplanacağı sınır tarihin girildiği alandır. |
| Stok Bakiye İçin Sınır Tarihi | Stok bakiyesinin sayımda girilen miktara göre düzenlenmesi sırasında, dikkate alınması istenen stok bakiyesinin tarihinin girildiği alandır. |
| Maliyet Tipi | Sayım miktar farkı olan stok hareketlerine aktarım yapılırken, fark birim fiyatı ve fark maliyet tutarlarının hesaplanacağı maliyet tipinin seçildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile, maliyet tipleri arasından seçim yapılır. |
| (-) ler Giriş İşlensin | Girilen sayımlarla stok bakiyeleri arasındaki farkın eksi (-) olduğu durumlarda (stok bakiyesinin sayımdan daha düşük olduğu durumlarda stok bakiyesinden sayım farkı çıkarıldığında fark miktarı eksi (-) değer alır) stok bakiyelerinin sayım miktarı ile denk gelmesi için bu farkın giriş olarak aktarılması gerekir. Bu alan da, istendiği zaman eksi (-) değer alan stok sayımın giriş olarak aktarılması için işaretlemesi gereken seçenektir. Dövizli Muhasebe kullanıldığında; program, sayım farklarını işlerken birim döviz maliyetini de bulur ve operasyon döviz tutarına aktarır. Bu işlem sırasında döviz tipi olarak, Yardımcı Programlar → Kayıt → [Şirket - Şube Parametreleri](<../../../../Muhasebe/Muhasebe Modülü/Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/Genel Tanımlar/Yardımcı Programlar-Şirket-Şube Parametreleri.md>)<br>bölümünden kaydedilen firma döviz tipi kullanılır. Bu işlem hesaplanırken, girilen tarih aralığındaki stok hareket kayıtlarının içinden firma döviz tutarlarından faydalanılır. Dolayısıyla, firma döviz tutarlarının oluşması için öncelikle, Stok → İşlemler → [Stok Döviz Çevrim](<../Stok Döviz Çevrim.md>) bölümünün çalıştırılması gerekir. |
| Açıklama | Stok hareket kayıtlarına aktarılacak olan sayım fark miktarlarına ait açıklama bilgisinin girildiği alandır. |
| Mahsup Yapılsın | Stok hareketlerine işlenecek sayım fark sonuçlarının muhasebeleştirilmesi istendiğinde işaretlenmesi gereken seçenektir. İşaretlenmesi ile birlikte ekranın sağ tarafında muhasebe hesap kodlarının girileceği bir alan görüntülenir. ![](../../../../../_assets/c0ae1f38a977ef6292c5.png) Muhasebe kodlarının girilmesiyle, "Sayım Farkını Satış Hareketlerine İşleme" sonucu oluşan sayım fark sonuçları, hem stok hareketlerine hem de muhasebeleşmiş olarak Entegrasyon → Entegrasyon Kayıtları → Dekont mahsubuna aktarılır. |
| Proje Kırılımı Yapılsın | "Proje Kodu Takibi" uygulamasının kullanıldığı durumlarda aktif hale gelen alandır. Proje kodu bazında hareket işlenmesi istendiğinde işaretlenmesi gereken seçenektir. |
| ![](../../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilgilerin onaylanmasını sağlayan butondur. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
