---
title: "Dövizli Senetler Yeniden Değerleme Listesi / Borç Senetleri"
page_id: "24740351"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Borç Senetleri"
  - "Raporlar / Borç Senetleri"
  - "Dövizli Senetler Yeniden Değerleme Listesi / Borç Senetleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Borç Senetleri / Raporlar / Borç Senetleri / Dövizli Senetler Yeniden Değerleme Listesi / Borç Senetleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTRiODk2ZjRhLWIxY2ItNGMyOC1iOGJkLTRiNjMxMjE1ZjAyYyZsaW5rPTY2ZDUwNTA4LTBhZDktNDlmYy05NGRlLTAyZDViNWVmNGRhMSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=4b896f4a-b1cb-4c28-b8bd-4b631215f02c&link=66d50508-0ad9-49fc-94de-02d5b5ef4da1&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "dovizli-senetler-yeniden-degerleme-listesi-borc-senetleri_34218677_24740351.html"
source_version: "2022-12-13T10:39:32.640+03:00"
source_bytes: 516521
fetched_at: "2026-09-13T04:12:26+00:00"
generator: "netsis-scraper 1.0.0"
---
# Dövizli Senetler Yeniden Değerleme Listesi / Borç Senetleri

Borç senetleri modülü Dövizli Senetler Yeniden Değerleme Listesi bölümü, Finans Bölümü'nde, "Raporlar/Borç Senetleri" menüsünün altında yer alır. Borç senetleri modülü Dövizli Senetler Yeniden Değerleme Listesi bölümü, Borç Senetleri → Kayıt → [Borç Senetleri Parametreleri](<../Kayıt - Borç Senetleri/Borç Senetleri Parametreleri.md>) → "Döviz Uygulaması Var" parametresi işaretlenerek dövizli senet kayıtları oluşturulduğunda, meydana gelen kur farkı tutarlarının listesini almayı sağlar. Genel Kısıtlar, Ölçekleme ve Yazıcı Seçenekleri sekmelerinden oluşur.

**Genel Kısıtlar**

![](../../../../_assets/a38d2d1ca1acc2950b2c.png)

Borç senetleri modülü Dövizli Senetler Yeniden Değerleme Listesi bölümü Genel Kısıtlar sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Dövizli Senetler Yeniden Değerleme Listesi Ekranı |  |
| --- | --- |
| Yeniden Değerlemede Baz Alınacak Tarih | Kur farkı hesaplamasında baz alınacak tarihin girildiği alandır. Girilen senetlerin döviz tutarları ve yeniden değerleme tarihinde sorgulanan tarihteki kur değerlerine göre tekrar hesaplanarak oluşan tutarlar, daha önce girilen "Senet Tutarı" alanındaki tutar bilgisinden çıkartılarak (artı ya da eksi) kur farkı olarak listelenir.<br>Kur farkı hesaplamalarının yapılması için "Yeniden Değerlendirmede Baz Alınacak Tarih" alanında girilen tarihteki kur değerinin, Döviz Takibi → Kayıt → "[Döviz Kurları Girişi](<../../../Genel/Döviz Takibi/Kayıt - Döviz Takibi/Döviz Kurları Girişi.md>)" bölümüne önceden girilmesi gerekir. Yeniden değerleme tarihinde herhangi bir kur değerinin bulunmaması durumunda, kur farkı hesaplamaları 0 (sıfır) olarak çıkar ve hesaplanmaz. Bu bölümden alınan listelere, portföydeki banka tahsil ve teminata ciro edilen ve henüz ödenmeyen senetler dahil edilmez. Dövizli senetlerin kur farkı kayıtlarının, Borç Senetleri → İşlemler → [Dövizli Senetler Kur Farkı Kaydı](<../../Müşteri Senetleri/İşlemler - Müşteri Senetleri/Dövizli Senetler Kur Farkı Kaydı.md>) bölümünden muhasebeye entegre edilmeden önce bu bölümden liste alınması ve gerekli kontrollerin yapılması gerekir. |
| Döviz Çevrim Tipi | Dövizli senetler yeniden değerleme listesi almak için döviz çevrim tipinin seçildiği alandır. Döviz Alış, Döviz Satış, Efektif Alış ve Efektif Satış seçeneklerinden oluşur. |
| ![](../../../../_assets/7ba39f9046a578093326.png) | Yukarıdaki alanlara girilen bilgiler doğrultusunda, rapor almak için kullanılan butondur. Butonun sağ tarafında yer alan aşağı ok tuşu, "Gelişmiş Rapor" seçeneğinin kullanılmasını sağlar. Kullanıcı, "Gelişmiş Rapor" seçeneği ile ekrana gelen tablo üzerinde hesaplama yapabilir. Bu seçenek sayesinde, 13684 satırın üstündeki raporlamaların da tek sayfa üzerinden raporlanması sağlanır. "Rapor" seçeneği Text Dosya, Excel Dosya, VTS Format, HTML kayıt türlerini desteklerken, "Gelişmiş Rapor" seçeneği Excel Workbook, Excel Template, Excel 97-2003 Workbook, Excel 97-2003 Template, Comma Delimited, Text Document, Web Page, XML Document, PDF Document kayıt türlerini destekler. |
| ![](../../../../_assets/e3223333470668512f5f.jpg) | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. > [!NOTE]<br>> **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) | Genel Kısıt sekmesinde verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Dövizli senetler yeniden değerleme listesi almak için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki dövizli senetler yeniden değerleme listesi alma işleminde kullanılmak üzere saklanır. |
| ![](../../../../_assets/4ad6cc61ca2c42a19c85.jpg) | Dövizli senetler yeniden değerleme listesi almak için standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) | Dövizli senetler yeniden değerleme listesi almak için verilen kısıtların iptal edildiği butondur. |

**Ölçekleme**

Standart raporlarda miktar, fiyat, tutar, kur, döviz tutarı, döviz fiyatı, firma döviz tutarı ve oran alanları için ölçekleme yapılmasını sağlayan sekmedir.

![](../../../../_assets/fdf3a18f981729def59e.png)

**Örneğin;**

Fiyat ve tutar alanlarına 1.000 yazılması, fiyat ve tutara getirilecek verilerin 1.000'e bölüneceği anlamına gelir.

**Yazıcı Seçenekleri**

![](../../../../_assets/72b61f72efbd730f283d.png)

| Dövizli Senetler Yeniden Değerleme Listesi Ekranı |  |
| --- | --- |
| Ekran | Raporun ekrandan alınması için işaretlenmesi gereken seçenektir. Hiçbir değişiklik yapılmaması durumunda, raporda ekran seçeneği işaretli olduğu için, rapor yine ekrandan alınır. |
| Yazıcı | Raporun yazıcıdan alınması için işaretlenmesi gereken seçenektir |
| Toplam Sayfa | Rapor yazıcıya döküldüğü zaman yazıcıdan kaç sayfa çıkarılacağının gösterildiği alandır. Kullanıcı, raporu yazıcıya göndermeden önce bu seçeneği işaretleyerek ![](../../../../_assets/21c20c78203acae9cce6.jpg)butonuna basarsa, yazıcıya dökülecek sayfa adedi ekranda görüntülenir. ![](../../../../_assets/b2e157c1e0713bfefb94.png) |
| Dövizli Senetler Yeniden Değerleme Listesi Ekranı | Yazıcı Seçenekleri - Yönlendirme |
| Dikey | Raporun sadece yazıcı seçeneği ile bastırılması durumunda kullanılan seçenektir. Döküm yapılacak kağıdın genişliğine göre rapor dikey veya yatay olarak alınabilir. Bu seçenekte hiçbir değişiklik yapılmaması durumunda otomatik olarak "Dikey" işaretlenmiş olduğu için rapor dikey şekilde basılır. Ekran seçeneğinde bu parametrenin herhangi bir işlevi yoktur. |
| Yatay | Raporun sadece yazıcı seçeneği ile bastırılması durumunda kullanılan seçenektir. Döküm yapılacak kağıdın genişliğine göre rapor dikey veya yatay olarak alınabilir. Raporun kağıda yatay olarak basılması için işaretlenmesi gereken seçenektir. Ekran seçeneğinde bu parametrenin herhangi bir işlevi yoktur. |
| Dövizli Senetler Yeniden Değerleme Listesi Ekranı | Yazıcı Seçenekleri |
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
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) | Genel Kısıt sekmesinde verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Dövizli senetler yeniden değerleme listesi almak için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki dövizli senetler yeniden değerleme listesi alma işleminde kullanılmak üzere saklanır. |
| ![](../../../../_assets/4ad6cc61ca2c42a19c85.jpg) | Dövizli senetler yeniden değerleme listesi almak için standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) | Dövizli senetler yeniden değerleme listesi almak için verilen kısıtların iptal edildiği butondur. |
