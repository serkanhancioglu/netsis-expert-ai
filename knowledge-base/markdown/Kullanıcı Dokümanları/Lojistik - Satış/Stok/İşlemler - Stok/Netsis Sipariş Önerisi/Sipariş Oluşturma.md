---
title: "Sipariş Oluşturma"
page_id: "22803766"
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
  - "Sipariş Oluşturma"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Stok / İşlemler / Stok / Netsis Sipariş Önerisi / Sipariş Oluşturma"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWY2MjZmYzczLWUyNDktNDViMi1hYWU0LTMwOTljYWJjOTMzOSZsaW5rPTY4NTRkZTc0LTA4NzctNDM5MS1hZGE4LTI2YmNjZDIxMGVkZCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=f626fc73-e249-45b2-aae4-3099cabc9339&link=6854de74-0877-4391-ada8-26bccd210edd&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "siparis-olusturma_29997210_22803766.html"
source_version: "2022-10-26T10:18:01.260+03:00"
source_bytes: 24582
fetched_at: "2026-09-13T04:04:48+00:00"
generator: "netsis-scraper 1.0.0"
---
# Sipariş Oluşturma

Sipariş Oluşturma, Finans Bölümü'nde, "İşlemler/Stok " menüsünün altında yer alır. Sipariş Oluşturma, Netsis sipariş önerisinin son aşaması olan "Sipariş Oluşturma" bölümü, mallara ait satıcı siparişlerinin oluşturulması için kullanılır. Sipariş Oluşturma; Genel Kısıtlar ve Ön Sorgulama olmak üzere iki sekmeden oluşur.

**Genel Kısıtlar**

Sipariş Oluşturma ekranı Genel Kısıtlar sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Sipariş Oluşturma Ekranı |  |
| --- | --- |
| Stok Kodu | Sipariş oluşturulması için stok kodu kısıtının girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, stok kodları arasından seçim yapılır. |
| Yapılandırma Kodu | Sipariş oluşturulması için yapılandırma kodu kısıtının girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, yapılandırma kodları arasından seçim yapılır. |
| Grup Kodu | Sipariş oluşturulması için grup kodu kısıtının girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, grup kodları arasından seçim yapılır. |
| Kod-1/Kod-2 | Sipariş oluşturulması için kod-1/kod-2 kısıtının girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, kodlar arasından seçim yapılır. |
| Satıcı Kodu | Sipariş oluşturulması için satıcı kodu kısıtının girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, satıcı kodları arasından seçim yapılır. Sadece, girilen aralıktaki satıcı kodlarına ait sipariş oluşturulur. Bu alanın boş bırakılması durumunda, "Sipariş Öneri Hazırlık" sonucu oluşan siparişler sırayla oluşturulur. |
| Fiyat Kodu | Sipariş oluşturulması için fiyat kodu kısıtının girildiği alandır. Sadece, girilen fiyat kodu aralığındaki sipariş oluşturulmasını sağlar. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, fiyat kodları arasından seçim yapılır. |

**Ön Sorgulama**

Sipariş Oluşturma ekranı Ön Sorgulama sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Sipariş Oluşturma Ekranı |  |
| --- | --- |
| Tipi | Sipariş oluşturma tipinin belirlendiği alandır. Yurt içi ve Yurt dışı olmak üzere iki tipten oluşur. |
| Netsis Öneri Tarihi | "Sipariş Önerisi Hazırlık" işleminin çalıştırıldığı ve sipariş miktarlarının baz alınacağı tarihin girildiği alandır. Girilen tarih itibariyle oluşan sipariş miktarlarına göre satıcı siparişleri oluşturulur. |
| Sipariş Tarihi | Oluşacak satıcı siparişleri için baz alınacak tarihin girildiği alandır. |
| Depo Kodu | "Ortalama Kullanım Miktarı" oluşturma işleminde lokal depolar için **"Kümüle"** seçeneği işaretlendiğinde, sipariş için kullanılacak lokal depo kodunun girildiği alandır. "Ortalama Kullanım Miktarı" oluşturma işleminde "Detaylı" seçeneği işaretlendiğinde ise, "Depo Kodu" alanı boş bırakılır. Çünkü, her malın siparişi lokal depolar bazında otomatik olarak oluşur. |
| Proje Kodu | Proje uygulamasının kullanıldığı durumlarda sorgulanan ve oluşturulacak siparişe ait proje kodunun belirlenmesi amacıyla kullanılan alandır. Oluşturulan satıcı siparişlerinde koşul uygulaması kullanılıyorsa, koşuldaki tanımlamalara göre ilgili liste fiyatı, kullanılmıyorsa satıcı kodundaki liste fiyatı baz alınır. Cari kartlarda liste fiyatları yoksa, stok kartlarındaki "Alış Fiyatı-1" alanından aktarılarak oluşturulur. Bu işlem sonucu oluşan satıcı siparişleri, Fatura → Kayıt → [Satıcı Siparişleri](<../../../Fatura/Kayıt - Fatura/Satıcı Siparişleri.md>) bölümünden izlenir. |
| ![](../../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilginin onaylanmasını sağlayan butondur. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgiden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
