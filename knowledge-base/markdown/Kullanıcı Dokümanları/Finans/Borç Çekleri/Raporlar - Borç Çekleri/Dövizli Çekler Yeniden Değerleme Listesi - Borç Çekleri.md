---
title: "Dövizli Çekler Yeniden Değerleme Listesi / Borç Çekleri"
page_id: "24740247"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Borç Çekleri"
  - "Raporlar / Borç Çekleri"
  - "Dövizli Çekler Yeniden Değerleme Listesi / Borç Çekleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Borç Çekleri / Raporlar / Borç Çekleri / Dövizli Çekler Yeniden Değerleme Listesi / Borç Çekleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWJlNmM4NWVlLTc1OGEtNGNjZC05MWY0LTBkMjEwNTRhMzc0MiZsaW5rPTE4ZDUwZGJjLTdmYTEtNGI3Yi04ZWJlLTEwZTcxYjg5NTNjNyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=be6c85ee-758a-4ccd-91f4-0d21054a3742&link=18d50dbc-7fa1-4b7b-8ebe-10e71b8953c7&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "dovizli-cekler-yeniden-degerleme-listesi-borc-cekleri_34219181_24740247.html"
source_version: "2022-12-13T16:26:20.623+03:00"
source_bytes: 514667
fetched_at: "2026-09-13T04:12:42+00:00"
generator: "netsis-scraper 1.0.0"
---
# Dövizli Çekler Yeniden Değerleme Listesi / Borç Çekleri

Borç Çekleri modülü Dövizli Çekler Yeniden Değerleme Listesi bölümü, Finans Bölümü'nde Raporlar/Borç Çekleri menüsünün altında yer alır. Borç Çekleri modülü Dövizli Çekler Yeniden Değerleme Listesi bölümü, Borç Çekleri → Kayıt → Borç Çekleri Parametreleri → "Döviz Uygulaması Var" parametresi işaretlenerek dövizli çek kayıtları oluşturulduğunda, meydana gelen kur farkı tutarlarının listesini almayı sağlar. Genel Kısıtlar, Ölçekleme ve Yazıcı Seçenekleri sekmelerinden oluşur.

**Genel Kısıtlar**

![](../../../../_assets/b5579f2b2c2cf5741054.png)

Borç Çekleri modülü Dövizli Çekler Yeniden Değerleme Listesi bölümü Genel Kısıtlar sekmesinde yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| Dövizli Çekler Yeniden Değerleme Listesi Ekranı |  |
| --- | --- |
| Yeniden Değerlemede Baz Alınacak Tarih | Kur farkı hesaplamasında baz alınacak tarihin girildiği alandır. Girilen çeklerin döviz tutarları ve yeniden değerleme tarihinde sorgulanan tarihteki kur değerlerine göre tekrar hesaplanarak oluşan tutarlar, daha önce girilen "Çek Tutarı" alanındaki tutar bilgisinden çıkartılarak (artı ya da eksi) kur farkı olarak listelenir.<br>Kur farkı hesaplamalarının yapılması için "Yeniden Değerlendirmede Baz Alınacak Tarih" alanında girilen tarihteki kur değerinin, Döviz Takibi → Kayıt → "[Döviz Kurları Girişi](<../../../Genel/Döviz Takibi/Kayıt - Döviz Takibi/Döviz Kurları Girişi.md>)" bölümüne önceden girilmesi gerekir. Yeniden değerleme tarihinde herhangi bir kur değerinin bulunmaması durumunda, kur farkı hesaplamaları 0 (sıfır) olarak çıkar ve hesaplanmaz. Bu bölümden alınan listelere, portföydeki banka tahsil ve teminata ciro edilen ve henüz ödenmeyen çekler dahil edilmez. Dövizli çeklerin kur farkı kayıtlarının, Borç Çekleri → İşlemler → [Dövizli Çekler Kur Farkı Kaydı](<../../Müşteri Çekleri/İşlemler - Müşteri Çekleri/Dövizli Çekler Kur Farkı Kaydı.md>) bölümünden muhasebeye entegre edilmeden önce bu bölümden liste alınması ve gerekli kontrollerin yapılması gerekir. |
| Döviz Çevrim Tipi | Dövizli çekler yeniden değerleme listesi almak için döviz çevrim tipinin seçildiği alandır. Döviz Alış, Döviz Satış, Efektif Alış ve Efektif Satış seçeneklerinden oluşur. |
| ![](../../../../_assets/7ba39f9046a578093326.png) Rapor | Yukarıdaki alanlara girilen bilgiler doğrultusunda, rapor almak için kullanılan butondur. Butonun sağ tarafında yer alan aşağı ok tuşu, "Gelişmiş Rapor" seçeneğinin kullanılmasını sağlar. Kullanıcı, "Gelişmiş Rapor" seçeneği ile ekrana gelen tablo üzerinde hesaplama yapabilir. Bu seçenek sayesinde, 13684 satırın üstündeki raporlamaların da tek sayfa üzerinden raporlanması sağlanır. "Rapor" seçeneği Text Dosya, Excel Dosya, VTS Format, HTML kayıt türlerini desteklerken, "Gelişmiş Rapor" seçeneği Excel Workbook, Excel Template, Excel 97-2003 Workbook, Excel 97-2003 Template, Comma Delimited, Text Document, Web Page, XML Document, PDF Document kayıt türlerini destekler. |
| ![](../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Genel Kısıt sekmesinde verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Dövizli çekler yeniden değerleme listesi almak için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki dövizli çekler yeniden değerleme listesi alma işleminde kullanılmak üzere saklanır. |
| ![](../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | Dövizli çekler yeniden değerleme listesi almak için standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Dövizli çekler yeniden değerleme listesi almak için verilen kısıtların iptal edildiği butondur. |

**Ölçekleme**

Standart raporlarda miktar, fiyat, tutar, kur, döviz tutarı, döviz fiyatı, firma döviz tutarı ve oran alanları için ölçekleme yapılmasını sağlayan sekmedir.

![](../../../../_assets/20abbd3ddac47228b56d.png)

**Örneğin;**

Fiyat ve tutar alanlarına 1.000 yazılması, fiyat ve tutara getirilecek verilerin 1.000'e bölüneceği anlamına gelir.

**Yazıcı Seçenekleri**

![](../../../../_assets/71a629972e3a29de2406.png)

| Dövizli Çekler Yeniden Değerleme Listesi Ekranı |  |
| --- | --- |
| Ekran | Raporun ekrandan alınması için işaretlenmesi gereken seçenektir. Hiçbir değişiklik yapılmaması durumunda, raporda ekran seçeneği işaretli olduğu için, rapor yine ekrandan alınır. |
| Yazıcı | Raporun yazıcıdan alınması için işaretlenmesi gereken seçenektir |
| Toplam Sayfa | Rapor yazıcıya döküldüğü zaman yazıcıdan kaç sayfa çıkarılacağının gösterildiği alandır. Kullanıcı, raporu yazıcıya göndermeden önce bu seçeneği işaretleyerek ![](../../../../_assets/21c20c78203acae9cce6.jpg)butonuna basarsa, yazıcıya dökülecek sayfa adedi ekranda görüntülenir. ![](../../../../_assets/b2e157c1e0713bfefb94.png) |
| Dövizli Çekler Yeniden Değerleme Listesi Ekranı | Yazıcı Seçenekleri - Yönlendirme |
| Dikey | Raporun sadece yazıcı seçeneği ile bastırılması durumunda kullanılan seçenektir. Döküm yapılacak kağıdın genişliğine göre rapor dikey veya yatay olarak alınabilir. Bu seçenekte hiçbir değişiklik yapılmaması durumunda otomatik olarak "Dikey" işaretlenmiş olduğu için rapor dikey şekilde basılır. Ekran seçeneğinde bu parametrenin herhangi bir işlevi yoktur. |
| Yatay | Raporun sadece yazıcı seçeneği ile bastırılması durumunda kullanılan seçenektir. Döküm yapılacak kağıdın genişliğine göre rapor dikey veya yatay olarak alınabilir. Raporun kağıda yatay olarak basılması için işaretlenmesi gereken seçenektir. Ekran seçeneğinde bu parametrenin herhangi bir işlevi yoktur. |
| Dövizli Çekler Yeniden Değerleme Listesi Ekranı | Yazıcı Seçenekleri |
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
| ![](../../../../_assets/7ba39f9046a578093326.png) | Yukarıdaki alanlara girilen bilgiler doğrultusunda, rapor almak için kullanılan butondur. Butonun sağ tarafında yer alan aşağı ok tuşu, "Gelişmiş Rapor" seçeneğinin kullanılmasını sağlar. Kullanıcı, "Gelişmiş Rapor" seçeneği ile ekrana gelen tablo üzerinde hesaplama yapabilir. Bu seçenek sayesinde, 13684 satırın üstündeki raporlamaların da tek sayfa üzerinden raporlanması sağlanır. "Rapor" seçeneği Text Dosya, Excel Dosya, VTS Format, HTML kayıt türlerini desteklerken, "Gelişmiş Rapor" seçeneği Excel Workbook, Excel Template, Excel 97-2003 Workbook, Excel 97-2003 Template, Comma Delimited, Text Document, Web Page, XML Document, PDF Document kayıt türlerini destekler. |
| ![](../../../../_assets/e3223333470668512f5f.jpg) | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. > [!NOTE]<br>> **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) | Genel Kısıt sekmesinde verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Dövizli çekler yeniden değerleme listesi almak için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki dövizli çekler yeniden değerleme listesi alma işleminde kullanılmak üzere saklanır. |
| ![](../../../../_assets/4ad6cc61ca2c42a19c85.jpg) | Dövizli çekler yeniden değerleme listesi almak için standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) | Dövizli çekler yeniden değerleme listesi almak için verilen kısıtların iptal edildiği butondur. |
