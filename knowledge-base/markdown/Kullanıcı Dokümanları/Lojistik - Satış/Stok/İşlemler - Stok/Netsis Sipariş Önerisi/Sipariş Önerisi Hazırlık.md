---
title: "Sipariş Önerisi Hazırlık"
page_id: "22803768"
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
  - "Sipariş Önerisi Hazırlık"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Stok / İşlemler / Stok / Netsis Sipariş Önerisi / Sipariş Önerisi Hazırlık"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWExODVmNDU0LTlmMjktNGQ1MC1hZjgyLTdhMDUxM2RmZTQ1ZiZsaW5rPTk0Yzg2YjljLTA3ZGMtNGQ4NS05NGY2LWY4MGYyMGUyM2JmZSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=a185f454-9f29-4d50-af82-7a0513dfe45f&link=94c86b9c-07dc-4d85-94f6-f80f20e23bfe&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "siparis-onerisi-hazirlik_29997083_22803768.html"
source_version: "2022-10-26T10:10:39.173+03:00"
source_bytes: 50637
fetched_at: "2026-09-13T04:04:46+00:00"
generator: "netsis-scraper 1.0.0"
---
# Sipariş Önerisi Hazırlık

Sipariş Önerisi Hazırlık, Finans Bölümü'nde, "İşlemler/Stok " menüsünün altında yer alır. Sipariş Önerisi Hazırlık, stoklar için bulunan ortalama kullanım miktarları ve ABC kodları dikkate alınarak, satıcılara verilmesi gereken sipariş miktarlarının hesaplanması için kullanılan bölümdür. Sipariş Önerisi Hazırlık; Ön Sorgulama, Genel Kısıtlar ve Ölçekleme sekmelerinden oluşur.

Sipariş önerisi hazırlık işleminde aşağıdaki formül kullanılır:

Sipariş Önerisi = Ortalama Kullanım Miktarı X Katsayı – (Stok Bakiyesi + Satıcı Sipariş Bakiyesi) + Müşteri Sipariş Bakiyesi

**Ön Sorgulama**

Sipariş Önerisi Hazırlık ekranı Ön Sorgulama sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Netsis Sipariş Önerisi Ekranı |  |
| --- | --- |
| Stok Kodu | Sipariş öneri miktarı hesaplamak için stok kodu kısıdı verilen alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, stok kodları arasından seçim yapılır. |
| Grup Kodu | Sipariş öneri miktarı hesaplamak için grup kodu kısıdı verilen alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile grup kodları arasından seçim yapılır. |
| Kod-1/2/3/4/5 | Sipariş öneri miktarı hesaplamak için, önceden tanımlaması yapılan Kod-1/2/3/4/5 kısıdının verildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile kodlar arasından seçim yapılır. |
| Sadece Esnek Yapılandırılabilir Stoklar Dökülsün | Sadece esnek yapılandırılan stokların raporlanması istendiğinde işaretlenmesi gereken seçenektir. |
| Özellikler | Esnek yapılandırma özellik kısıdının verildiği alandır. Alanın sağ tarafında yer alan üç nokta ![](../../../../../_assets/5098b020c5e814c92501.png) butonu ile, esnek yapılandırma rehberinden seçim yapılır. |
| ![](../../../../../_assets/a8eb576ad165012b70f6.png) Tamam | Yukarıdaki alanlara girilen bilgiler doğrultusunda, Sipariş öneri miktarı hesaplamak için kullanılan butondur. |
| ![](../../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Genel Kısıt sekmesinde verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Sipariş öneri miktarı hesaplamak için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki Netsis sipariş önerisi işleminde kullanılmak üzere saklanır. |
| ![](../../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | Sipariş önerisi hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) İptal | Sipariş öneri miktarı hesaplamak için verilen kısıtların iptal edildiği butondur. |

**Genel Kısıtlar**

Sipariş Önerisi Hazırlık ekranı Genel Kısıtlar sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Netsis Sipariş Önerisi Ekranı |  |
| --- | --- |
| Tarih | Sipariş öneri miktarı hesaplanırken, baz alınması istenen tarihin girildiği alandır. Hesaplama yapılırken, sadece girilen tarihteki stok, satıcı ve müşteri sipariş bakiyeleri dikkate alınır. |
| Şubelerde Çalıştırılsın | Sipariş öneri miktarının şubeler için de hazırlanması istendiğinde işaretlenmesi gereken seçenektir. |
| Şube Kodu Aralığı | "Şubeler Çalıştırılsın" seçeneği işaretlenmişse, hangi şube kodları için sipariş öneri miktarı hesaplanacağı ile ilgili aralık girilen alandır. Şube kodu aralığı boş bırakılmaz ve sipariş öneri miktarı hesaplanması istenen şube aralığının mutlaka kaydedilmesi gerekir. |
| Detaylı/Kümüle | "Şubeler Çalıştırılsın" seçeneği işaretlenmişse, sipariş önerisinin kümüle mi, yoksa detaylı mı hesaplanacağı ile ilgili seçeneğin belirlendiği alandır. **"Detaylı"** seçeneği işaretlendiğinde; merkez ve şubeler için ayrı sipariş öneri miktarı hesaplanır. **"K****ümüle"** seçeneği işaretlendiğinde ise; şube çıkış ve merkez çıkış miktarları hesaplanarak, merkez stok kartları için sipariş öneri miktarı hesaplanır. |
| Depo Kodu Aralığı | Sipariş önerisi hazırlanması istenen lokal depolar için kod aralığı girilen alandır. Tüm lokal depolar için sipariş önerisi hazırlanacak ise depo kodu aralığı boş bırakılır. |
| Detaylı/Kümüle | **"Detaylı"** seçeneği işaretlendiğinde, stok kartlarının lokal depo kodları bazında sipariş önerisi hazırlanır. **"Kümüle"** seçeneği işaretlendiğinde ise, lokal depo kodları bazında değil, her bir stok için kümüle sipariş önerisi hazırlanır. |
| ![](../../../../../_assets/a8eb576ad165012b70f6.png) Tamam | Yukarıdaki alanlara girilen bilgiler doğrultusunda, Sipariş öneri miktarı hesaplamak için kullanılan butondur. |
| ![](../../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Genel Kısıt sekmesinde verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Sipariş öneri miktarı hesaplamak için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki Netsis sipariş önerisi işleminde kullanılmak üzere saklanır. |
| ![](../../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | Sipariş önerisi hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) İptal | Sipariş öneri miktarı hesaplamak için verilen kısıtların iptal edildiği butondur. |

**Ölçekleme**

Standart raporlarda miktar, fiyat, tutar, kur, döviz tutarı, döviz fiyatı, firma döviz tutarı ve oran alanları için ölçekleme yapılmasını sağlayan sekmedir.

**Örneğin:** Fiyat ve tutar alanlarına 1.000 yazılması, fiyat ve tutara getirilecek verilerin 1.000'e bölüneceği anlamına gelir.
