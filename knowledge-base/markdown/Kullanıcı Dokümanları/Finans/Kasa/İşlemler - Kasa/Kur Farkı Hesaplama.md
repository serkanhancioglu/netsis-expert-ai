---
title: "Kur Farkı Hesaplama"
page_id: "22806445"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Kasa"
  - "İşlemler / Kasa"
  - "Kur Farkı Hesaplama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Kasa / İşlemler / Kasa / Kur Farkı Hesaplama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTkyYmFiMjg3LWY1MmUtNDE1ZS1hYzgyLWU5NDM5Y2FlYTk3YiZsaW5rPTdkNDU4Mjc5LWUxNzUtNGUxZC05ZTNjLWVhMDQxNzcyNThkNCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=92bab287-f52e-415e-ac82-e9439caea97b&link=7d458279-e175-4e1d-9e3c-ea04177258d4&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "kur-farki-hesaplama_24771205_22806445.html"
source_version: "2022-04-05T15:51:24.733+03:00"
source_bytes: 52009
fetched_at: "2026-09-13T04:10:48+00:00"
generator: "netsis-scraper 1.0.0"
---
# Kur Farkı Hesaplama

Kur Farkı Hesaplama, dövizli çalışılan kasalarda, günlük kur değişimlerinden kaynaklanan kur farkı gelirinin/giderinin hesaplanarak kasa hareketlerine işlenmesini sağlayan bölümdür. Kur Farkı Hesaplama, Finans Bölümü'nde, "İşlemler/Kasa" menüsünün altında yer alır. Bu bölüm çalıştırılmadığı sürece kur farkı hesaplanmaz. Bu nedenle eğer günlük olarak kur farklarının hesaplanması isteniyorsa "Kur Farkı Hesaplama" işleminin çalıştırılması gerekir.

![](../../../../_assets/c2e929e9092ce59e54bd.png)

Kur Farkı Hesaplama ekranı Genel Kısıtlar sekmesinin alanları ve içerdiği bilgiler aşağıdaki şekildedir:

| Kur Farkı Hesaplama Ekranı |  |
| --- | --- |
| Kasa Kodu | Kur farkı hesaplatılacak kasa kodunun girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile kasa kodları arasından seçim yapılabilir. |
| Döviz Tipi | Kur farkı hesaplatılacak kasanın döviz tipinin izlendiği alandır. |
| Kasa Tarihi | İçinde bulunulan kasa tarihinin program tarafından aktarıldığı alandır. İstenildiğinde kullanıcı tarafından değişiklik yapılabilir. İşlem sonucunda oluşan kur farkı değeri, bu tarihteki kasa hareketlerine **Muhtelif İşlem** tipinde işlenir. |
| Kur | "Kasa Tarihi" alanında girilen günün kur değerinin program tarafından aktarıldığı alandır. İstenildiğinde kullanıcı tarafından değişiklik yapılabilir. |
| Referans Kodu | Muhasebe → Kayıt → [Muhasebe Parametreleri](<../../../Muhasebe/Muhasebe Modülü/Kayıt - Muhasebe/Muhasebe Parametreleri.md>) → Yevmiye → "Fişlerde Referans Kodu Sorulsun" parametresinin işaretli olduğu durumlarda aktif hale gelen seçenektir. "Muhasebe Modülü/Referans Kodu Kayıtlarında" tanımlanmış referans kodlarından biri bu alana girildiğinde, Kur Farkı Hesaplama işlemi sadece belirtilen referans koduyla girilen kasa kayıtları için çalıştırılır. ![](../../../../_assets/088477bb321d1b20c939.jpg) Rehber butonu yardımıyla referans kodu seçimi yapılabilir. |
| Proje Kodu Kırılım | Yardımcı Programlar → Kayıt → [Şirket/Şube Parametre Tanımları](<../../../Genel/Yardımcı Programlar/Kayıt - Yardımcı Programlar/Şirket - Şube - Parametre Tanımları.md>)nda “Proje Uygulaması Var” parametresinin işaretli olduğu durumlarda aktif hale gelen seçenektir. Kur farkı hesaplama işleminin proje kodu bazında kırılımlı olarak yapılması istendiğinde işaretlenmesi gereken alandır. |
| Proje Kodu | Yardımcı Programlar → Kayıt → [Şirket/Şube Parametre Tanımları](<../../../Genel/Yardımcı Programlar/Kayıt - Yardımcı Programlar/Şirket - Şube - Parametre Tanımları.md>)nda “Proje Uygulaması Var” parametresinin işaretli olduğu durumlarda aktif hale gelen alandır. Belirlenen proje kodu bazında kur farkı hesaplama işlemi yapılır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile proje kodları arasından seçim yapılabilir. |
| Kur Farkı İşlensin | Kur Farkı Hesaplatma işlemi sonucunda oluşan kur farkı değerlerinin kasa hareketlerine işlenmesi istendiğinde işaretlenmesi gereken alandır. Bu alan işaretlendiği zaman hesaplanan kur farkı değeri kasa hareketlerine ,kasa tarihindeki tarihle ve muhtelif işlem tipi ile işlenir. Bu seçenek işaretlenmediğinde ise kur farkı hesaplaması rapor olarak izlenebilir fakat kasa hareketlerine işlenmez. |
| ![](../../../../_assets/21c20c78203acae9cce6.jpg) Rapor | Kur farkı raporu almak için verilen kısıtlara göre Yukarıdaki alanlara girilen bilgiler doğrultusunda, rapor almak için kullanılan butondur. Butonun sağ tarafında yer alan aşağı ok tuşu, "Gelişmiş Rapor" seçeneğinin kullanılmasını sağlar. Kullanıcı, "Gelişmiş Rapor" seçeneği ile ekrana gelen tablo üzerinde hesaplama yapabilir. Bu seçenek sayesinde, 13684 satırın üstündeki raporlamaların da tek sayfa üzerinden raporlanması sağlanır. "Rapor" seçeneği Text Dosya, Excel Dosya, VTS Format, HTML kayıt türlerini desteklerken, "Gelişmiş Rapor" seçeneği Excel Workbook, Excel Template, Excel 97-2003 Workbook, Excel 97-2003 Template, Comma Delimited, Text Document, Web Page, XML Document, PDF Document kayıt türlerini destekler. |
| ![](../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Genel Kısıt sekmesinde verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Kur farkı raporu almak için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki kur farkı raporu işleminde kullanılmak üzere saklanır. |
| ![](../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | Kur farkı raporu ekranı hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Kur farkı raporu almak için verilen kısıtların iptal edildiği butondur. |
