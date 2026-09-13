---
title: "MRP Sonuçlarından Minimum Stok Değeri Oluşturma"
page_id: "50668666"
product: "netsis-3-enterprise"
depth: 5
is_section: true
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Üretim"
  - "MRP"
  - "İşlemler / MRP"
  - "MRP Sonuçlarından Minimum Stok Değeri Oluşturma"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Üretim / MRP / İşlemler / MRP / MRP Sonuçlarından Minimum Stok Değeri Oluşturma"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWZiYmEzNzMzLTY1YTEtNDNhNS1iOWI2LTFiZmU0ZmQ3MmI1ZiZsaW5rPTIzYTYxMTk4LWRkOGUtNDk1MS1hMjM5LWJhMzZlMWVmZjRhYyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=fbba3733-65a1-43a5-b9b6-1bfe4fd72b5f&link=23a61198-dd8e-4951-a239-ba36e1eff4ac&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "mrp-sonuclarindan-minimum-stok-degeri-olusturma_50668908_50668666.html"
source_version: "2022-10-21T09:21:09.373+03:00"
source_bytes: 198658
fetched_at: "2026-09-13T04:20:05+00:00"
generator: "netsis-scraper 1.0.0"
---
# MRP Sonuçlarından Minimum Stok Değeri Oluşturma

MRP Sonuçlarından Minimum Stok Değeri Oluşturma, Üretim Bölümü'nde, "İşlemler/MRP" menüsünün altında yer alır. MRP Sonuçlarından Minimum Stok Değeri Oluşturma işlemi, ihtiyaç kapasitenin belirlenmesi için gerekli hesaplamaları yaparak "Kapasite Tablosu" oluşturur. Seçenekli olarak istenirse, "Malzeme Gereksinim Planlama" sonucu oluşan mamul/yarı mamul ihtiyaçlarını ya da o anda açılan iş emirlerini fabrikanın dikkate alarak, her ikisinin toplam kapasite gereksinimini hesaplar. Kapasite Tablosunda; tarih, mamul kodu ve operasyonlar bazında gereksinim duyulan üretim miktarları için ihtiyaç kapasite bilgisi bulunur.

MRP Sonuçlarından Minimum Stok Değeri Oluşturma işlemi sonucu çıkan rakamlar MRP → Raporlar → Kapasite Raporu bölümünden izlenir.

MRP Sonuçlarından Minimum Stok Değeri Oluşturma ekranı; Genel Kısıtlar, MRP Kısıtları, Ölçekleme ve Yazıcı Seçenekleri sekmesinden oluşur.

**Genel Kısıtlar**

MRP Sonuçlarından Minimum Stok Değeri Oluşturma ekranı Genel Kısıtlar sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| MRP Sonuçlarından Minimum Stok Değeri Oluşturma Ekranı |  |
| --- | --- |
| Stok Kodu | Mrp sonuçlarından minimum stok değeri oluşturma listesi almak için stok kodu kısıdı verilen alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, stok kodları arasından seçim yapılır. |
| Grup Kodu | Mrp sonuçlarından minimum stok değeri oluşturma listesi almak için grup kodu kısıdı verilen alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, grup kodları arasından seçim yapılır. |
| Kod-1,2,3,4 ve Kod-5 | Mrp sonuçlarından minimum stok değeri oluşturma listesi almak için kod-1,2,3,4 ve kod-5 kısıdının verildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, kodlar arasından seçim yapılır. |
| Sadece Esnek Yapılandırılabilir Stoklar Dökülsün | Mrp sonuçlarından minimum stok değeri oluşturma listesi oluşturmak için verilen kısıtların haricinde sadece esnek yapılandırılabilir stokların listelenmesi için kullanılan seçenektir. |
| Özellikler | Stoka ait özellikler, üç nokta ![](../../../../../_assets/5098b020c5e814c92501.png) butonu ile esnek yapılandırma özellik rehberinden belirlenerek, toplu basım için kısıt verilmesini sağlar. "İleri seviyede kısıt vermek için burayı kullanabilirsiniz." yazısının üzerine tıklandığında, aşağıdaki ekranda belirtilen alanlar doldurularak detaylı kısıt verilmesi sağlanır. ![](../../../../../_assets/4b8fefa342af3e1d859b.png) |
| ![](../../../../../_assets/7ba39f9046a578093326.png) Rapor | Yukarıdaki alanlara girilen bilgiler doğrultusunda, rapor almak için kullanılan butondur. Butonun sağ tarafında yer alan aşağı ok tuşu, "Gelişmiş Rapor" seçeneğinin kullanılmasını sağlar. Kullanıcı, "Gelişmiş Rapor" seçeneği ile ekrana gelen tablo üzerinde hesaplama yapabilir. Bu seçenek sayesinde, 13684 satırın üstündeki raporlamaların da tek sayfa üzerinden raporlanması sağlanır. "Rapor" seçeneği Text Dosya, Excel Dosya, VTS Format, HTML kayıt türlerini desteklerken, "Gelişmiş Rapor" seçeneği Excel Workbook, Excel Template, Excel 97-2003 Workbook, Excel 97-2003 Template, Comma Delimited, Text Document, Web Page, XML Document, PDF Document kayıt türlerini destekler. |
| ![](../../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Genel Kısıtlar ve Kısıt sekmelerinde verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Mrp sonuçlarından minimum stok değeri oluşturma listesi almak için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki Mrp Sonuçlarından Minimum Stok Değeri Oluşturma listesi alma işleminde kullanılmak üzere saklanır. |
| ![](../../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | Mrp Sonuçlarından Minimum Stok Değeri Oluşturma ekranı hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) İptal | Mrp sonuçlarından minimum stok değeri oluşturma listesi almak için verilen kısıtların iptal edildiği butondur. |

**MRP Kısıtları**

MRP Sonuçlarından Minimum Stok Değeri Oluşturma ekranı MRP Kısıtları sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| MRP Sonuçlarından Minimum Stok Değeri Oluşturma Ekranı |  |
| --- | --- |
| Başlangıç Tarihi | Mrp sonuçlarından minimum stok değeri oluşturma listesi almak için başlangıç tarihi kısıdı verilen alandır. |
| Baz Alınacak Saha | Mrp sonuçlarından minimum stok değeri oluşturma listesi almak için baz alınacak sahanın belirlendiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile seçim yapılır. |
| İleri Gidilecek Gün | Mrp sonuçlarından minimum stok değeri oluşturma listesi almak için ileri gidilecek günün girildiği alandır. |
| Bölen Gün | Mrp sonuçlarından minimum stok değeri oluşturma listesi almak için bölen günün girildiği alandır. |
| Stok Seviyesi Gün Sayısı Saha | Mrp sonuçlarından minimum stok değeri oluşturma listesi almak için stok seviyesi gün sahasının belirlendiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile seçim yapılır. |
| ![](../../../../../_assets/7ba39f9046a578093326.png) Rapor | Yukarıdaki alanlara girilen bilgiler doğrultusunda, rapor almak için kullanılan butondur. Butonun sağ tarafında yer alan aşağı ok tuşu, "Gelişmiş Rapor" seçeneğinin kullanılmasını sağlar. Kullanıcı, "Gelişmiş Rapor" seçeneği ile ekrana gelen tablo üzerinde hesaplama yapabilir. Bu seçenek sayesinde, 13684 satırın üstündeki raporlamaların da tek sayfa üzerinden raporlanması sağlanır. "Rapor" seçeneği Text Dosya, Excel Dosya, VTS Format, HTML kayıt türlerini desteklerken, "Gelişmiş Rapor" seçeneği Excel Workbook, Excel Template, Excel 97-2003 Workbook, Excel 97-2003 Template, Comma Delimited, Text Document, Web Page, XML Document, PDF Document kayıt türlerini destekler. |
| ![](../../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Genel Kısıtlar ve Kısıt sekmelerinde verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Mrp sonuçlarından minimum stok değeri oluşturma listesi almak için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki Mrp Sonuçlarından Minimum Stok Değeri Oluşturma listesi alma işleminde kullanılmak üzere saklanır. |
| ![](../../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | Mrp Sonuçlarından Minimum Stok Değeri Oluşturma ekranı hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) İptal | Mrp sonuçlarından minimum stok değeri oluşturma listesi almak için verilen kısıtların iptal edildiği butondur. |

**Ölçekleme**

Standart raporlarda miktar, fiyat, tutar, kur, döviz tutarı, döviz fiyatı, firma döviz tutarı ve oran alanları için ölçekleme yapılmasını sağlayan sekmedir.

**Örneğin;**

Fiyat ve tutar alanlarına 1.000 yazılması, fiyat ve tutara getirilecek verilerin 1.000'e bölüneceği anlamına gelir.

**Yazıcı Seçenekleri**

| MRP Sonuçlarından Minimum Stok Değeri Oluşturma Ekranı |  |
| --- | --- |
| Ekran | Raporun ekrandan alınması için işaretlenmesi gereken seçenektir. Hiçbir değişiklik yapılmaması durumunda, raporda ekran seçeneği işaretli olduğu için, rapor yine ekrandan alınır. |
| Yazıcı | Raporun yazıcıdan alınması için işaretlenmesi gereken seçenektir |
| Toplam Sayfa | Rapor yazıcıya döküldüğü zaman yazıcıdan kaç sayfa çıkarılacağının gösterildiği alandır. Kullanıcı, raporu yazıcıya göndermeden önce bu seçeneği işaretleyerek ![](../../../../../_assets/21c20c78203acae9cce6.jpg)butonuna basarsa, yazıcıya dökülecek sayfa adedi ekranda görüntülenir. ![](../../../../../_assets/b2e157c1e0713bfefb94.png) |
| MRP Sonuçlarından Minimum Stok Değeri Oluşturma Ekranı | Yazıcı Seçenekleri - Yönlendirme |
| Dikey | Raporun sadece yazıcı seçeneği ile bastırılması durumunda kullanılan seçenektir. Döküm yapılacak kağıdın genişliğine göre rapor dikey veya yatay olarak alınabilir. Bu seçenekte hiçbir değişiklik yapılmaması durumunda otomatik olarak "Dikey" işaretlenmiş olduğu için rapor dikey şekilde basılır. Ekran seçeneğinde bu parametrenin herhangi bir işlevi yoktur. |
| Yatay | Raporun sadece yazıcı seçeneği ile bastırılması durumunda kullanılan seçenektir. Döküm yapılacak kağıdın genişliğine göre rapor dikey veya yatay olarak alınabilir. Raporun kağıda yatay olarak basılması için işaretlenmesi gereken seçenektir. Ekran seçeneğinde bu parametrenin herhangi bir işlevi yoktur. |
| MRP Sonuçlarından Minimum Stok Değeri Oluşturma Ekranı | Yazıcı Seçenekleri |
| Şirket Adı | Basılsın, Basılmasın ve Detaylı Basılsın olmak üzere üç seçenekten oluşur. Yazıcıdan alınacak raporun her bir sayfasında şirket unvanının yazılması istendiğinde "Basılsın" seçeneğinin kullanılması gerekir. > [!NOTE]<br>> Şirket unvanı Yardımcı Programlar/Şirket/Şube Parametre Tanımları menüsünde tanımlandığı şekilde otomatik olarak ekrana gelir. |
| Başlık Yazılsın | Yazıcıdan alınacak raporun her bir sayfasında, tanımlanan liste başlığının yazılması istendiğinde işaretlenmesi gereken seçenektir. |
| Tarih / Saat Yazılsın | Yazıcıdan alınacak raporun her bir sayfasında sistem tarihi ve saatinin yazılması istendiğinde işaretlenmesi gereken seçenektir. |
| Sayfa No Basılsın | Yazıcıdan alınacak raporun her bir sayfasında sayfa numarasının yazılması istendiğinde işaretlenmesi gereken seçenektir. |
| Taslak Basım | Birden fazla alanın yer aldığı raporlarda, yazıcıdan çıktı alırken kağıttan taşma sorununun çözülmesi ve raporların istenilen formatta ayarlanması için, "Taslak Basım Ayarları" bölümü kullanılır. Taslak basım ayarları her rapor için bir kez yapılır ve saklanır. Böylece, yazıcıdan çıktı alırken tekrar ayarlama yapmaya gerek kalmadan basım yapılır. Raporun "Taslak Basım Ayarlarında" kaydedilmiş formata göre dökülmesi istendiğinde "Taslak Basım" ve "Saklanmış" seçeneklerinin işaretlenmesi gerekir. > [!NOTE]<br>> Basım Dot Matrix (iğne vuruşlu yazıcı) türü bir yazıcıdan alınacaksa, basım ayarları yapılmasa da "Taslak Basım" seçeneğinin işaretlenmesi gerekir. |
| Saklanmış | Raporun "Taslak Basım Ayarlarında" kaydedilmiş formata göre dökülmesi istendiğinde "Taslak Basım" ve "Saklanmış" seçeneklerinin işaretlenmesi gerekir. |
| Perfore Satır Sayısı | Yazıcıya gönderilecek raporun kaç satırlık kağıda basılacağının belirlendiği alandır. 33’lük ya da 66’lık olabilir. Rapor yazıcıya dökülürken kaç satırdan sonra yeni kağıda geçileceği buradaki tanımlamaya göre belirlenir. Standart olarak 66 seçeneği ekrana gelir fakat kullanıcı isterse değişiklik yapabilir. |
| Yazıcı Ayarı Yapılsın | Seçenek işaretlendiğinde, Windows’un “Yazıcı Ayarları” ekrana gelir. Bu ekranda, tanımlı olan yazıcılar arasından seçim yapılır. Rapor ekrandan alındıktan sonra yazıcıya gönderildiği zaman, tanımlanmış olan yazıcı ayarlarına göre basım yapılır. |
| Nüsha Sayısı | Yazıcıdan alınacak dökümlerde, her sayfadan kaç adet basılacağının belirlendiği alandır. |
| Sıfır Basma | Raporda "sıfır" sayısının görüntülenmesinin istenmediği durumlarda işaretlenmesi gereken alandır. Listelenen kayıtlarda sıfır (0) değerini taşıyan alanlar boş olarak izlenir. |
| Dosya İmzala |  |
| Excel Dosya Adı | Ekran ya da yazıcıdan alınacak raporun diske "Excel" formatında bir dosya halinde atılması istendiğinde işaretlenmesi gereken seçenektir. Bu alanda dosyanın hangi dizinde ve hangi isimle oluşturulacağının belirtilmesi gerekir. Excel’in File/Open seçeneği ile Excel'de dosya izlenebilir. |
| Text Dosya Adı | Ekran ya da yazıcıdan alınacak raporun diske "Text" formatında bir dosya halinde atılması istendiğinde işaretlenmesi gereken seçenektir. Bu alanda dosyanın hangi dizinde ve hangi isimle oluşturulacağının belirtilmesi gerekir. Bu dosyaya herhangi bir editör program kullanılarak erişilebilir. |
| HTML Dosya Adı | Ekran ya da yazıcıdan alınacak raporun diske "Html" formatında bir dosya halinde atılması istendiğinde işaretlenmesi gereken seçenektir. Bu alanda dosyanın hangi dizinde ve hangi isimle oluşturulacağının belirtilmesi gerekir. > [!NOTE]<br>> Bu bölümden Excel, Text veya Html formatında oluşturulacak dosyanın doğru ve eksiksiz oluşturulması için tanımlamalar yapıldıktan sonra, raporun tamamının yazıcı ya da ekrandan alınması gerekir. |
| Başlık | Yazıcı ya da ekran dökümleri için rapora genel başlık tanımlanan alandır. "Modül Standart Raporlarında" başlıklar otomatik olarak tanımlı gelir. İstendiğinde bu alandan değiştirilebilir. |
| ![](../../../../../_assets/7ba39f9046a578093326.png) | Yukarıdaki alanlara girilen bilgiler doğrultusunda, rapor almak için kullanılan butondur. Butonun sağ tarafında yer alan aşağı ok tuşu, "Gelişmiş Rapor" seçeneğinin kullanılmasını sağlar. Kullanıcı, "Gelişmiş Rapor" seçeneği ile ekrana gelen tablo üzerinde hesaplama yapabilir. Bu seçenek sayesinde, 13684 satırın üstündeki raporlamaların da tek sayfa üzerinden raporlanması sağlanır. "Rapor" seçeneği Text Dosya, Excel Dosya, VTS Format, HTML kayıt türlerini desteklerken, "Gelişmiş Rapor" seçeneği Excel Workbook, Excel Template, Excel 97-2003 Workbook, Excel 97-2003 Template, Comma Delimited, Text Document, Web Page, XML Document, PDF Document kayıt türlerini destekler. |
| ![](../../../../../_assets/e3223333470668512f5f.jpg) | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. > [!NOTE]<br>> **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../../_assets/53859e19eb2737b88a17.jpg) | Genel Kısıtlar ve Kısıt sekmelerinde verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Mrp sonuçlarından minimum stok değeri oluşturma listesi almak için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki Mrp Sonuçlarından Minimum Stok Değeri Oluşturma listesi alma işleminde kullanılmak üzere saklanır. |
| ![](../../../../../_assets/4ad6cc61ca2c42a19c85.jpg) | Mrp Sonuçlarından Minimum Stok Değeri Oluşturma ekranı hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) | Mrp sonuçlarından minimum stok değeri oluşturma listesi almak için verilen kısıtların iptal edildiği butondur. |
