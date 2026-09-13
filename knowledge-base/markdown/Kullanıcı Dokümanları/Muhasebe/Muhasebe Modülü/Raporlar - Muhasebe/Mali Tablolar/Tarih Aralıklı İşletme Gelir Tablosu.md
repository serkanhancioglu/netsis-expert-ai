---
title: "Tarih Aralıklı İşletme Gelir Tablosu"
page_id: "24740801"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Muhasebe"
  - "Muhasebe Modülü"
  - "Raporlar / Muhasebe"
  - "Mali Tablolar"
  - "Tarih Aralıklı İşletme Gelir Tablosu"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / Raporlar / Muhasebe / Mali Tablolar / Tarih Aralıklı İşletme Gelir Tablosu"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTI0MDVjMDQzLTIzOTktNDBhYy1iYWNkLTMzNWQxOGYyYjBiYSZsaW5rPTNhMWUxMmUwLWFlZmUtNDA3MC04NjVjLTEwMDg3NWJiNTNjYyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=2405c043-2399-40ac-bacd-335d18f2b0ba&link=3a1e12e0-aefe-4070-865c-100875bb53cc&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "tarih-aralikli-isletme-gelir-tablosu_41162018_24740801.html"
source_version: "2022-10-17T11:03:03.580+03:00"
source_bytes: 251466
fetched_at: "2026-09-13T04:14:05+00:00"
generator: "netsis-scraper 1.0.0"
---
# Tarih Aralıklı İşletme Gelir Tablosu

Tarih Aralıklı İşletme Gelir Tablosu, Muhasebe Bölümünde, "Raporlar/Muhasebe Modülü" menüsünün altında yer alır. İşletmelerin belli bir dönemdeki tüm gelirleri ile aynı dönemdeki maliyet ve giderleri sonucu elde ettiği dönem net karı/dönem net zararının tarih aralıklı gösterildiği mali tablodur. Tarih Aralıklı İşletme Gelir Tablosu; Genel Kısıtlar, Ölçekleme ve Yazıcı Seçenekleri sekmelerinden oluşur.

**Genel Kısıtlar**

**![](../../../../../_assets/50de4d96a4035226728e.png)**

Tarih Aralıklı İşletme Gelir Tablosu ekranı Genel Kısıtlar sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Tarih Aralıklı İşletme Gelir Bilançosu Ekranı |  |
| --- | --- |
| Tarih | Tarih aralıklı işletme gelir bilançosu için başlangıç ve bitiş tarih aralığı girilen alandır. |
| Önceki Dönem Şirketi | Önceki dönem şirketine ait kayıtların gelir tablosunda listelenmesi için şirket kodunun girildiği alandır. |
| Önceki Dönem Şirketi Veritabanı Kullanıcı İsmi | Önceki dönem şirketi ile bağlantı kurmak için veritabanı kullanıcı isminin girildiği alandır. |
| Önceki Dönem Şirketi Veritabanı Şifresi | Önceki dönem şirketi ile bağlantı kurmak için veritabanı şifresinin (varsa) girildiği alandır. |
| Dipnot Dosyası | Gelir tablosunda dipnot bilgilerinin izlenmesi için dipnot dosyasının olduğu dizinin belirlendiği alandır. Gelir tablosu dipnot dosyası TXT dosya olarak "KAR94.Txt" dosyasında tutulur ve kullanıcı bu dosyaya kendi şirketine ait bilgileri ekleyebilir. |
| Hesap Kodu Maskesi | Hesap kodlarına filtre tanımlanarak liste alınmasını sağlayan alandır. **Örneğin;** Ana hesap kodu 1 rakamı ile başlayan hesapların listesi alınacaksa, bu alana %100 değerinin girilmesi gerekir. Maskeleme alanına “\_” tek bir karakter yerine “%” birden fazla bilinmeyen karakter girilebilir. |
| Proje Kırılımı Var | Yardımcı Programlar → Kayıt → [Şirket-Şube Parametreleri](<../../Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/Genel Tanımlar/Yardımcı Programlar-Şirket-Şube Parametreleri.md>) → “Proje Uygulaması Var” parametresinin işaretlendiği ve proje takibinin yapıldığı durumlarda, sadece belirlenen proje kodları için bilanço alınması ve proje kodları bazında raporlanması için işaretlenen seçenektir. |
| Proje Kodu Aralığı | "Proje Kırılımı Var" seçeneğinin işaretlenmesi ile aktif hale gelen “Proje Kodu Aralığı” alanına, raporlara dahil edilecek tutarların bulunmasında baz alınacak proje kodları için aralık verilir. Proje kodu aralığı verilmesi halinde, sadece bu projeler için girilen tutarlar dikkate alınarak ve proje kodu kırılımlı raporlama yapılır. Proje kırılımlı rapor alınması için mutlaka proje kodu aralığının verilmesi gerekir. Aksi takdirde raporlar, proje kodlarına bakılmaksızın proje kodu detaysız olarak listelenir. Proje kodları, ana muhasebe hesap kodlarının sağında parantez içinde gösterilir. Proje bazında kırılımların raporda izlenmesi için, rapor genel kısıtlarında bulunan “Ayrıntılı” seçeneğinin mutlaka işaretlenmesi gerekir Bunun sebebi ise, kırılımın ana hesap kodları bazında gösterilmesidir. Ana hesap kodları, rapor "Ayrıntılı" olarak alındığında listelenir. "Ayrıntılı" seçeneğinin işaretlenmediği, yani raporun özet olarak alındığı durumlarda, sadece ilgili proje kodları ile girilen tutarlar dikkate alınır fakat proje kodu bazında kırılım gösterilmez. |
| Özet/Ayrıntılı | Grup kodları bazında detaysız olarak gelir tablosu alınması için **"Özet"**, özet gelir tablosunda tablosunda yer almayan, kebir bazında tüm hesap kodları dahil edilerek gelir tablosu alınması için **“Ayrıntılı”** seçeneğinin işaretlenmesi gerekir. |
| Kümülatif/Aylık | Raporun ekrandan ya da yazıcıdan sadece ilgili ay için alınması istendiğinde “**Aylık**”, yıl başından belirlenen aya kadar kümüle olarak alınması istendiğinde ise “**Kümülatif**” seçeneğinin işaretlenmesi gerekir. |
| Klasik Basım Yapılsın | Raporda bulunan başlıkların numaralandırılarak klasik formda basım yapılması için kullanılan seçenektir. Seçeneğin işaretlenmesi ile, ana grup isimlerinin (Dönen Varlıklar, Duran Varlıklar gibi) başına Romen rakamıyla numaralandırma yapılır. diğer grup isimlerinin (Hazır Değerler, Stoklar gibi) başına da grup kodları yerine A, B, C gibi harfler getirilir. Ayrıca, raporlarda ana grup kodları bazında toplam alınabilir. |
| Düzeltilmiş Değerler Basılsın | Muhasebe → Kayıt → [Muhasebe Parametreleri](<../../Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/Muhasebe Modülü Tanımlamaları/Muhasebe Parametreleri - Muhasebe.md>) → "IAS29" seçeneğinin işaretlenmesi ile aktif hale gelen seçenektir. Enflasyon muhasebesine göre düzeltilen değerlerin basılması için kullanılır. |
| Hareket Görmemiş Hesaplar Basılsın | İşletme gelir tablosu raporuna hareket görmeyen hesapların basılması için kullanılan seçenektir. |
| Önceki Dönem Bilgileri Kümüle Dökülsün | Önceki dönem bilgilerinin gelir tablosunda kümüle dökülmesi için kullanılan seçenektir. |
| \12. Ayda Kapanış Fişleri Dahil Edilmesin | İşletme gelir tablosuna 12.ayda kapanış fişlerinin dahil edilmemesi için kullanılan seçenektir. |
| Hesap Adı | Raporda listelenecek hesap isimlerinin; "Hesap Planı" ekranında yer alan "Hesap İsmi" alanındaki isim olarak listelenmesi için **Türkçe,** "Hesap Planı" ekranında yer alan "Yabancı Hesap İsmi" alanındaki isim olarak listelenmesi için **Diğer** seçeneğinin işaretlenmesi gerekir. |
| ![](../../../../../_assets/7ba39f9046a578093326.png) Rapor | Yukarıdaki alanlara girilen bilgiler doğrultusunda, rapor almak için kullanılan butondur. Butonun sağ tarafında yer alan aşağı ok tuşu, "Gelişmiş Rapor" seçeneğinin kullanılmasını sağlar. Kullanıcı, "Gelişmiş Rapor" seçeneği ile ekrana gelen tablo üzerinde hesaplama yapabilir. Bu seçenek sayesinde, 13684 satırın üstündeki raporlamaların da tek sayfa üzerinden raporlanması sağlanır. "Rapor" seçeneği Text Dosya, Excel Dosya, VTS Format, HTML kayıt türlerini desteklerken, "Gelişmiş Rapor" seçeneği Excel Workbook, Excel Template, Excel 97-2003 Workbook, Excel 97-2003 Template, Comma Delimited, Text Document, Web Page, XML Document, PDF Document kayıt türlerini destekler. |
| ![](../../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | "Genel Kısıtlar" sekmesinde verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Gelir tablosu almak için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki gelir tablosu alma işleminde kullanılmak üzere saklanır. |
| ![](../../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | İşletme Gelir Tablosu ekranı hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) İptal | Gelir tablosu almak için verilen kısıtların iptal edildiği butondur. |

**Ölçekleme**

Standart raporlarda miktar, fiyat, tutar, kur, döviz tutarı, döviz fiyatı, firma döviz tutarı ve oran alanları için ölçekleme yapılmasını sağlayan sekmedir.

![](../../../../../_assets/f50e2bacdfb9af867154.png)

**Örneğin;**

Fiyat ve tutar alanlarına 1.000 yazılması, fiyat ve tutara getirilecek verilerin 1.000'e bölüneceği anlamına gelir.

**Yazıcı Seçenekleri**

**![](../../../../../_assets/7e1da31326c6472f2557.png)**

| Tarih Aralıklı İşletme Gelir Tablosu Ekranı |  |
| --- | --- |
| Ekran | Raporun ekrandan alınması için işaretlenmesi gereken seçenektir. Hiçbir değişiklik yapılmaması durumunda, raporda ekran seçeneği işaretli olduğu için, rapor yine ekrandan alınır. |
| Yazıcı | Raporun yazıcıdan alınması için işaretlenmesi gereken seçenektir |
| Toplam Sayfa | Rapor yazıcıya döküldüğü zaman yazıcıdan kaç sayfa çıkarılacağının gösterildiği alandır. Kullanıcı, raporu yazıcıya göndermeden önce bu seçeneği işaretleyerek ![](../../../../../_assets/21c20c78203acae9cce6.jpg)butonuna basarsa, yazıcıya dökülecek sayfa adedi ekranda görüntülenir. ![](../../../../../_assets/b2e157c1e0713bfefb94.png) |
| Tarih Aralıklı İşletme Gelir Tablosu Ekranı | Yazıcı Seçenekleri - Yönlendirme |
| Dikey | Raporun sadece yazıcı seçeneği ile bastırılması durumunda kullanılan seçenektir. Döküm yapılacak kağıdın genişliğine göre rapor dikey veya yatay olarak alınabilir. Bu seçenekte hiçbir değişiklik yapılmaması durumunda otomatik olarak "Dikey" işaretlenmiş olduğu için rapor dikey şekilde basılır. Ekran seçeneğinde bu parametrenin herhangi bir işlevi yoktur. |
| Yatay | Raporun sadece yazıcı seçeneği ile bastırılması durumunda kullanılan seçenektir. Döküm yapılacak kağıdın genişliğine göre rapor dikey veya yatay olarak alınabilir. Raporun kağıda yatay olarak basılması için işaretlenmesi gereken seçenektir. Ekran seçeneğinde bu parametrenin herhangi bir işlevi yoktur. |
| Tarih Aralıklı İşletme Gelir Tablosu Ekranı | Yazıcı Seçenekleri |
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
| ![](../../../../../_assets/53859e19eb2737b88a17.jpg) | "Genel Kısıtlar" sekmesinde verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Gelir tablosu almak için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki gelir tablosu alma işleminde kullanılmak üzere saklanır. |
| ![](../../../../../_assets/4ad6cc61ca2c42a19c85.jpg) | İşletme Gelir Tablosu ekranı hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) | Gelir tablosu almak için verilen kısıtların iptal edildiği butondur. |
