---
title: "Stok Döviz Çevrim"
page_id: "22803738"
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
  - "Stok Döviz Çevrim"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Stok / İşlemler / Stok / Stok Döviz Çevrim"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWExZjMwNGFkLWM4ZjAtNGJjYS04MGE4LTgzOTMyYjg0MzFjNyZsaW5rPTUzZWY1ZjRjLWJiMGMtNDI0YS1hYWZiLWE3ZWRhOWQ3ZjljZCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=a1f304ad-c8f0-4bca-80a8-83932b8431c7&link=53ef5f4c-bb0c-424a-aafb-a7eda9d7f9cd&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "stok-doviz-cevrim_29995798_22803738.html"
source_version: "2022-10-26T09:42:43.563+03:00"
source_bytes: 37235
fetched_at: "2026-09-13T04:04:36+00:00"
generator: "netsis-scraper 1.0.0"
---
# Stok Döviz Çevrim

Stok Döviz Çevrim, Lojistik - Satış Bölümü'nde, "İşlemler/Stok " menüsünün altında yer alır. Stok Döviz Çevrim bölümü, stok hareketlerinde bulunan birim fiyatlardan ve ilgili tarihteki döviz kurlarından yararlanılarak, hareket bazında döviz fiyatlarını oluşturmaya yarar. Dövizli işlemlerde girilen döviz bilgileri, stok hareketlerinin "Döviz Tipi" ve "Döviz Tutarı" alanlarına aktarılır. Bu tutarlar operasyon tutarlarını gösterir. Tüm stokların belli bir döviz tipi baz alınarak değerlerinin hesaplanması ve ortak bir döviz tipinde raporlanması için bu bölümün kullanılması gerekir. "Stok Döviz Çevrim" işleminin çalıştırılması ile oluşan döviz fiyatları, stok hareketlerinde yer alan "Firma Döviz Tutarı" alanına aktarılır.

"Stok Döviz Çevrim" ekranı; Ön Sorgulama, Genel Kısıtlar ve Ölçekleme sekmelerinden oluşur.

**Ön Sorgulama**

Stok Döviz Çevrim ekranı Ön Sorgulama sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Stok Döviz Çevrim Ekranı |  |
| --- | --- |
| Stok Kodu | Stok döviz çevrimi için stok kodu kısıdı verilen alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, stok kodları arasından seçim yapılır. |
| Grup Kodu | Stok döviz çevrimi için grup kodu kısıdı verilen alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile grup kodları arasından seçim yapılır. |
| Kod-1/2/3/4/5 | Stok döviz çevrimi için, önceden tanımlaması yapılan Kod-1/2/3/4/5 kısıdının verildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile kodlar arasından seçim yapılır. |
| Sadece Esnek Yapılandırılabilir Stoklar Dökülsün | Sadece esnek yapılandırılan stokların raporlanması istendiğinde işaretlenmesi gereken seçenektir. |
| ![](../../../../_assets/21c20c78203acae9cce6.jpg) Rapor | Stok döviz çevrimi için verilen kısıtlara göre Yukarıdaki alanlara girilen bilgiler doğrultusunda, rapor almak için kullanılan butondur. Butonun sağ tarafında yer alan aşağı ok tuşu, "Gelişmiş Rapor" seçeneğinin kullanılmasını sağlar. Kullanıcı, "Gelişmiş Rapor" seçeneği ile ekrana gelen tablo üzerinde hesaplama yapabilir. Bu seçenek sayesinde, 13684 satırın üstündeki raporlamaların da tek sayfa üzerinden raporlanması sağlanır. "Rapor" seçeneği Text Dosya, Excel Dosya, VTS Format, HTML kayıt türlerini desteklerken, "Gelişmiş Rapor" seçeneği Excel Workbook, Excel Template, Excel 97-2003 Workbook, Excel 97-2003 Template, Comma Delimited, Text Document, Web Page, XML Document, PDF Document kayıt türlerini destekler. Butonun sağ tarafında yer alan aşağı ok tuşu ile, Stok Döviz Çevrim işleminin Zamanlanmış Görevler'e eklenmesi sağlanır. Seçeneğe tıklandığında, Zamanlanmış Görev Tanımı ekranı üzerinden gereken tanımlamalar yapılır. |
| ![](../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Genel Kısıtlar ve Kısıt sayfalarında verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Stok döviz çevrimi için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki stok döviz çevrim işleminde kullanılmak üzere saklanır. |
| ![](../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | Stok döviz çevrim ekranı hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Stok döviz çevrimi için verilen kısıtların iptal edildiği butondur. |

**Genel Kısıtlar**

Stok Döviz Çevrim ekranı Genel Kısıtlar sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Stok Döviz Çevrim Ekranı |  |
| --- | --- |
| Tarih Aralığı | Döviz fiyatları oluşturulması istenen stok hareketlerine ait tarih aralığının girildiği alandır. |
| Düzeltme Tipi | Yardımcı Programlar → Kayıt → [Şirket - Şube Parametreleri](<../../../Muhasebe/Muhasebe Modülü/Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/Genel Tanımlar/Yardımcı Programlar-Şirket-Şube Parametreleri.md>) bölümünden girilen "Düzeltme Tipinin" otomatik olarak aktarıldığı alandır. Firma döviz tipinin bu bölümden değiştirilmesi mümkün değildir. Sonuç olarak oluşan değerler, her zaman bu döviz cinsinden oluşur. |
| Çevrim Türü | Ekranda belirlenen döviz cinsinin; Döviz Alış, Döviz Satış, Efektif Alış, Efektif Satış kurlarından hangisinin, döviz fiyatlarını oluşturmada baz alınacağı ile ilgili çevrim türü belirlenen alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile çevrim türleri arasından seçim yapılır. "Döviz Çevrim Türü" Yardımcı Programlar → Kayıt → [Şirket - Şube Parametreleri](<../../../Muhasebe/Muhasebe Modülü/Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/Genel Tanımlar/Yardımcı Programlar-Şirket-Şube Parametreleri.md>) bölümünde belirlenir ve bu alan üzerinden değişiklik yapılması mümkün değildir. |
| Şubeler Dahil Edilsin | Dövize Çevrim işleminin şube hareketleri için de yapılması istendiğinde işaretlenmesi gereken seçenektir. |

Bu işlem çalıştırıldığında, ilgili döviz tipinin seçilen döviz türündeki kuru baz alınır. Stok hareketinin işlem tarihinde kur bulunmazsa, o günden önceki kurlar aranır ve bulunan ilk kura göre işlem yapılır.

Döviz tutarları oluşturulurken yapılan hesaplamalar, aşağıda belirtilen koşullarda yapılır:

- İlgili stok hareketinin operasyon döviz tipleri ile, hesaplamada baz alınacak firma döviz tipi aynı ise, operasyon döviz tipi ve tutarı, firma döviz tipi ve tutarı alanlarına aynen aktarılır ve yeni bir hesaplama yapılmaz.
- İlgili stok hareketinin operasyon döviz tipi ile, hesaplamada baz alınacak firma döviz tipi farklı ise, firma döviz tipine göre stok hareket tarihleri baz alınarak firma döviz tutarları hesaplanır ve ilgili alanlara aktarılır.
- İlgili stok hareketinin operasyon döviz tipleri dolu, operasyon döviz tutarları boş ise (örneğin, kur farkı faturaları), firma döviz tutarının hesaplanmayacağı düşünülür. Bu durumda hareketlerdeki operasyon döviz tipi ile, hesaplama yapılacak firma döviz tipi aynı/farklı da olsa hesaplamada kullanılan firma döviz tipi, stok hareket kayıtlarındaki firma döviz tipi alanına aktarılır ve firma döviz tutarı hesaplanmaz.
- İlgili stok hareketinin operasyon döviz tipi ve tutarı boş (TL kayıt yapılmış) ise, hesaplama yapılan firma döviz tipine göre hareket tarihindeki kur baz alınır ve firma döviz tutarı oluşturulur.

Operasyon döviz tip ve tutarının dolu, operasyon döviz tipi ile firma döviz tipinin birbirinden farklı olması durumunda; firma döviz tutarları, parite hesaplaması kullanılarak bulunur. Yani, ilgili hareket tarihindeki her iki döviz tipinin kurları oranlanır ve bulunan pariteye göre firma döviz tutarları oluşturulur.

**Ölçekleme**

Standart raporlarda miktar, fiyat, tutar, kur, döviz tutarı, döviz fiyatı, firma döviz tutarı ve oran alanları için ölçekleme yapılmasını sağlayan sekmedir.

**Örneğin:** Fiyat ve tutar alanlarına 1.000 yazılması, fiyat ve tutara getirilecek verilerin 1.000'e bölüneceği anlamına gelir.
