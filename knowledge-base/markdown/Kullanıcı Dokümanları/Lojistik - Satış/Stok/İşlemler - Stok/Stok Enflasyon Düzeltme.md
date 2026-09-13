---
title: "Stok Enflasyon Düzeltme"
page_id: "29995807"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Stok"
  - "İşlemler / Stok"
  - "Stok Enflasyon Düzeltme"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Stok / İşlemler / Stok / Stok Enflasyon Düzeltme"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWE0MmExYWNiLWY3MzgtNDFlOC1hMzEzLTQ5ODVjZTFhYzNjNCZsaW5rPTM3MjJlOWQxLWUwYzItNGFkOC04MDdjLTJhNTgwMTM3MTkyZCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=a42a1acb-f738-41e8-a313-4985ce1ac3c4&link=3722e9d1-e0c2-4ad8-807c-2a580137192d&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "stok-enflasyon-duzeltme_29995830_29995807.html"
source_version: "2022-10-26T09:44:01.653+03:00"
source_bytes: 56291
fetched_at: "2026-09-13T04:04:37+00:00"
generator: "netsis-scraper 1.0.0"
---
# Stok Enflasyon Düzeltme

Stok Enflasyon Düzeltme, Lojistik - Satış Bölümü'nde, "İşlemler/Stok" menüsünün altında yer alır. Stok Enflasyon Düzeltme; Ön Sorgulama, Genel Kısıtlar ve Ölçekleme sekmelerinden oluşur.

Stok Enflasyon Düzeltme bölümünün menüde yer alması için; Muhasebe → Kayıt → [Muhasebe Parametreleri](<../../../Muhasebe/Muhasebe Modülü/Kayıt - Muhasebe/Muhasebe Parametreleri.md>) → Dövizli Muhasebe → IAS29 seçeneğinin işaretlenmesi gerekir.

Enflasyona Göre Değerleme" yapılması için; Döviz Takibi → Kayıt → [Döviz İsimleri Tanımlama](<../../../Genel/Döviz Takibi/Kayıt - Döviz Takibi/Döviz İsimleri Tanımlama.md>) bölümünden, "Enflasyon" isimli bir döviz tanımlamasının yapılması, Döviz Takibi → Kayıt → [Döviz Kurları Girişi](<../../../Genel/Döviz Takibi/Kayıt - Döviz Takibi/Döviz Kurları Girişi.md>) → Devlet İstatistik Enstitüsünün belirlediği endeksin girilmesi, Yardımcı Programlar → Kayıt → [Şirket - Şube Parametre Tanımları](<../../../Genel/Yardımcı Programlar/Kayıt - Yardımcı Programlar/Şirket - Şube - Parametre Tanımları.md>) → "Döviz Tipi" alanına "Enflasyon" isimli dövizin girilip kaydedilmesi gerekir.

Gerekli tanımlamalar yapıldıktan sonra, "Stok Döviz Çevrim" işlemi çalıştırıldığında; ilgili aylardaki stok hareketlerinin "Döviz Tipi" alanında, "Enflasyon" isimli döviz oluşur. Bu işlemlerden sonra, "Enflasyona Göre Değerleme" işlemi çalıştırılır.

**Ön Sorgulama**

Stok Enflasyon Düzeltme ekranı Ön Sorgulama sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Stok Enflasyon Düzeltme Ekranı |  |
| --- | --- |
| Stok Kodu | Stok enflasyon düzeltme için stok kodu kısıdı verilen alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, stok kodları arasından seçim yapılır. |
| Grup Kodu | Stok enflasyon düzeltme için grup kodu kısıdı verilen alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile grup kodları arasından seçim yapılır. |
| Kod-1/2/3/4/5 | Stok enflasyon düzeltme için, önceden tanımlaması yapılan Kod-1/2/3/4/5 kısıdının verildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile kodlar arasından seçim yapılır. |
| Sadece Esnek Yapılandırılabilir Stoklar Dökülsün | Sadece esnek yapılandırılan stokların raporlanması istendiğinde işaretlenmesi gereken seçenektir. |
| ![](../../../../_assets/21c20c78203acae9cce6.jpg) Rapor | Stok enflasyon düzeltme için verilen kısıtlara göre Yukarıdaki alanlara girilen bilgiler doğrultusunda, rapor almak için kullanılan butondur. Butonun sağ tarafında yer alan aşağı ok tuşu, "Gelişmiş Rapor" seçeneğinin kullanılmasını sağlar. Kullanıcı, "Gelişmiş Rapor" seçeneği ile ekrana gelen tablo üzerinde hesaplama yapabilir. Bu seçenek sayesinde, 13684 satırın üstündeki raporlamaların da tek sayfa üzerinden raporlanması sağlanır. "Rapor" seçeneği Text Dosya, Excel Dosya, VTS Format, HTML kayıt türlerini desteklerken, "Gelişmiş Rapor" seçeneği Excel Workbook, Excel Template, Excel 97-2003 Workbook, Excel 97-2003 Template, Comma Delimited, Text Document, Web Page, XML Document, PDF Document kayıt türlerini destekler. |
| ![](../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Genel Kısıtlar ve Kısıt sayfalarında verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Stok enflasyon düzeltme için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki Stok enflasyon düzeltme işleminde kullanılmak üzere saklanır. |
| ![](../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | Stok enflasyon düzeltme ekranı hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Stok enflasyon düzeltme için verilen kısıtların iptal edildiği butondur. |

**Genel Kısıtlar**

Stok Enflasyon Düzeltme ekranı Genel Kısıtlar sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Stok Enflasyon Düzeltme Ekranı |  |
| --- | --- |
| Yıl Kodu | Enflasyona ait düzeltme işlemi belli bir yıl için yapılacaksa, ilgili yıl bilgisinin girildiği alandır. |
| Ay Kodu Aralığı | Enflasyona ait düzeltme işlemi belli aylar için yapılacaksa, ilgili ay aralığının girildiği alandır. **Örneğin;** \7. aya kadar oluşan hareketlerin enflasyona göre düzenlenmesi istendiğinde, "Ay Kodu Aralığı" olarak 01-07 girilir. Bu işlem, "Stok Hareket Kayıtları" bölümünde, 8. aya ait "Döviz Takibi" modülünde tanımlanan enflasyon endeksine göre, E (Miktarı Olmayan Maliyet) tipli bir hareket oluşturur. |
| Düzeltme Tipi | "Yardımcı Programlar" modülünde belirlenen firma döviz tipinin, program tarafından otomatik olarak ekrana getirildiği alandır. Bu alanda, enflasyon için tanımlanmış döviz tipi olması gerekir. |
| Çevrim Türü | "Yardımcı Programlar" modülünde seçilen "Döviz Çevrim Tipinin" program tarafından otomatik olarak ekrana getirildiği alandır. |
| Şubeler Dahil | Enflasyona göre düzeltme işleminin şube hareketleri için de yapılması istendiğinde işaretlenmesi gereken seçenektir. |
| ![](../../../../_assets/21c20c78203acae9cce6.jpg) Rapor | Stok enflasyon düzeltme için verilen kısıtlara göre Yukarıdaki alanlara girilen bilgiler doğrultusunda, rapor almak için kullanılan butondur. Butonun sağ tarafında yer alan aşağı ok tuşu, "Gelişmiş Rapor" seçeneğinin kullanılmasını sağlar. Kullanıcı, "Gelişmiş Rapor" seçeneği ile ekrana gelen tablo üzerinde hesaplama yapabilir. Bu seçenek sayesinde, 13684 satırın üstündeki raporlamaların da tek sayfa üzerinden raporlanması sağlanır. "Rapor" seçeneği Text Dosya, Excel Dosya, VTS Format, HTML kayıt türlerini desteklerken, "Gelişmiş Rapor" seçeneği Excel Workbook, Excel Template, Excel 97-2003 Workbook, Excel 97-2003 Template, Comma Delimited, Text Document, Web Page, XML Document, PDF Document kayıt türlerini destekler. |
| ![](../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Genel Kısıtlar ve Kısıt sayfalarında verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Stok enflasyon düzeltme için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki Stok enflasyon düzeltme işleminde kullanılmak üzere saklanır. |
| ![](../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | Stok enflasyon düzeltme ekranı hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Stok enflasyon düzeltme için verilen kısıtların iptal edildiği butondur. |

**Ölçekleme**

Standart raporlarda miktar, fiyat, tutar, kur, döviz tutarı, döviz fiyatı, firma döviz tutarı ve oran alanları için ölçekleme yapılmasını sağlayan sekmedir.

**Örneğin:** Fiyat ve tutar alanlarına 1.000 yazılması, fiyat ve tutara getirilecek verilerin 1.000'e bölüneceği anlamına gelir.
