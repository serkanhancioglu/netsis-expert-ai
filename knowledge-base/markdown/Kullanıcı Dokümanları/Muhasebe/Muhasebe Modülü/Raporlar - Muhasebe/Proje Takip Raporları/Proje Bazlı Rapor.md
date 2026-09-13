---
title: "Proje Bazlı Rapor"
page_id: "24740759"
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
  - "Proje Takip Raporları"
  - "Proje Bazlı Rapor"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / Raporlar / Muhasebe / Proje Takip Raporları / Proje Bazlı Rapor"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTkyNDFjYTBjLTVkMTAtNDlkMS05NWVkLTQ2M2QyNmRkYjQ0OSZsaW5rPTk5ZWQ0MWRhLTMzMGEtNGFmNy1iMDBhLTJmYWFjMmMzNDYzZiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=9241ca0c-5d10-49d1-95ed-463d26ddb449&link=99ed41da-330a-4af7-b00a-2faac2c3463f&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "proje-bazli-rapor_41161311_24740759.html"
source_version: "2022-10-07T14:07:43.747+03:00"
source_bytes: 240883
fetched_at: "2026-09-13T04:13:55+00:00"
generator: "netsis-scraper 1.0.0"
---
# Proje Bazlı Rapor

Proje Bazlı Rapor, Muhasebe Bölümünde, "Raporlar/Muhasebe Modülü" menüsünün altında yer alır. Proje Bazlı Rapor, Muavin hesap bazında proje kodu kırılımlı borç/alacak tutarlarının listelenmesini sağlayan rapordur. Proje Bazlı Rapor; Ön Sorgulama-1, Ölçekleme ve Yazıcı Seçenekleri sekmelerinden oluşur. "Ön Sorgulama" sekmesinden girilecek başlangıç tarihinden önceki bilgiler devir olarak raporlanır.

**Ön Sorgulama-1**

![](../../../../../_assets/bab78839d2ba3b8235ee.png)

Proje Bazlı Rapor ekranı Ön Sorgulama-1 sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Proje Bazlı Rapor Ekranı |  |
| --- | --- |
| Proje Kodu Aralığı | Proje bazlı rapor almak için proje kodu aralığı kısıtı girilen alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, proje kodları arasından seçim yapılır. |
| Proje Hariç Aralığı | Rapordan hariç tutulması istenen proje kodlarının başlangıç ve bitiş kodlarının tanımlandığı alandır. Tanımlanan proje kodlarının haricindeki proje kodlarının rapora dahil edilmesini sağlar. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg)ile, proje kodları arasından seçim yapılarak kısıt verilir. |
| Hesap Kodu Aralığı | Belli bir aralıktaki hesap koduna ait döküm alınması istendiğinde kullanılan alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılarak kısıt verilir. |
| Hesap Kodu Maskesi | Hesap kodlarına filtre tanımlanarak liste alınmasını sağlayan alandır. Örneğin; ana hesap kodu 1 rakamı ile başlayan hesapların listesi alınacaksa, bu alana %100 değerinin girilmesi gerekir. Maskeleme alanına “\_” tek bir karakter yerine “%” birden fazla bilinmeyen karakter girilebilir. |
| Hesap Hariç Aralığı | Mizan raporundan hariç tutulması istenen hesap kodlarının başlangıç ve bitiş kodlarının tanımlandığı alandır. Tanımlanan hesap kodlarının haricindeki hesap kodlarının rapora dahil edilmesini sağlar. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılarak kısıt verilir. |
| Tarih Fiş Aralığı | Tarih fiş aralığı seçilen alandır. Tarih ve Evrak Tarihi Aralığı seçeneklerinden oluşur. Burada yapılan seçime göre, bu alanın altındaki ekranda ilgili alan için aralık tanımlanır. |
| Tarih | Proje bazlı rapor için başlangıç ve bitiş tarih aralığı kısıtı verilen alandır. |
| Miktar Yazılsın | Raporda, fişlere ait miktar bilgilerinin listelenmesi için kullanılan seçenektir. |
| Bakiye Basılsın | Borç/alacak bakiyelerinin raporda listelenmesi için kullanılan seçenektir. |
| Hesap Detaylı | Hesap detay bilgilerinin raporda listelenmesi için kullanılan seçenektir. |
| Şubeler Dahil Mi? | Rapora şubelerin dahil edilmesi için kullanılan seçenektir. |
| Döviz Yazılsın | Raporda fişlere ait döviz değerleri varsa, bu bilgilerin listelenmesi için kullanılan seçenektir. Ön muhasebe ya da yevmiye fiş kayıtlarından elle kaydedilen döviz değerlerinin listelenmesi için **“Operasyon”**, muhasebede “Enflasyon/Dövize Göre Çevrim” işlemi sonucunda oluşan döviz değerlerinin listelenmesi için **“Firma”** seçeneğinin seçilmesi gerekir. Tüm döviz tiplerine ait değerlerin bir arada alınması için **“Hepsi”**, döviz ile ilgili değerlerin raporda görüntülenmemesi için **“Hiçbiri”** seçeneğinin işaretlenmesi gerekir. |
| ![](../../../../../_assets/7ba39f9046a578093326.png) Rapor | Yukarıdaki alanlara girilen bilgiler doğrultusunda, rapor almak için kullanılan butondur. Butonun sağ tarafında yer alan aşağı ok tuşu, "Gelişmiş Rapor" seçeneğinin kullanılmasını sağlar. Kullanıcı, "Gelişmiş Rapor" seçeneği ile ekrana gelen tablo üzerinde hesaplama yapabilir. Bu seçenek sayesinde, 13684 satırın üstündeki raporlamaların da tek sayfa üzerinden raporlanması sağlanır. "Rapor" seçeneği Text Dosya, Excel Dosya, VTS Format, HTML kayıt türlerini desteklerken, "Gelişmiş Rapor" seçeneği Excel Workbook, Excel Template, Excel 97-2003 Workbook, Excel 97-2003 Template, Comma Delimited, Text Document, Web Page, XML Document, PDF Document kayıt türlerini destekler. |
| ![](../../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | "Ön Sorgulama" sekmesinde verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Rapor almak için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki rapor işleminde kullanılmak üzere saklanır. |
| ![](../../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | "Proje Bazlı Rapor" ekranı hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) İptal | Rapor almak için verilen kısıtların iptal edildiği butondur. |

**Ölçekleme**

Standart raporlarda miktar, fiyat, tutar, kur, döviz tutarı, döviz fiyatı, firma döviz tutarı ve oran alanları için ölçekleme yapılmasını sağlayan sekmedir.

![](../../../../../_assets/b4f14823b1d602a93026.png)

**Örneğin;**

Fiyat ve tutar alanlarına 1.000 yazılması, fiyat ve tutara getirilecek verilerin 1.000'e bölüneceği anlamına gelir.

**Yazıcı Seçenekleri**

**![](../../../../../_assets/4b0703a2fd3199b2f1b5.png)**

| Proje Bazlı Rapor Ekranı |  |
| --- | --- |
| Ekran | Raporun ekrandan alınması için işaretlenmesi gereken seçenektir. Hiçbir değişiklik yapılmaması durumunda, raporda ekran seçeneği işaretli olduğu için, rapor yine ekrandan alınır. |
| Yazıcı | Raporun yazıcıdan alınması için işaretlenmesi gereken seçenektir |
| Toplam Sayfa | Rapor yazıcıya döküldüğü zaman yazıcıdan kaç sayfa çıkarılacağının gösterildiği alandır. Kullanıcı, raporu yazıcıya göndermeden önce bu seçeneği işaretleyerek ![](../../../../../_assets/21c20c78203acae9cce6.jpg)butonuna basarsa, yazıcıya dökülecek sayfa adedi ekranda görüntülenir. ![](../../../../../_assets/b2e157c1e0713bfefb94.png) |
| Proje Bazlı Rapor Ekranı | Yazıcı Seçenekleri - Yönlendirme |
| Dikey | Raporun sadece yazıcı seçeneği ile bastırılması durumunda kullanılan seçenektir. Döküm yapılacak kağıdın genişliğine göre rapor dikey veya yatay olarak alınabilir. Bu seçenekte hiçbir değişiklik yapılmaması durumunda otomatik olarak "Dikey" işaretlenmiş olduğu için rapor dikey şekilde basılır. Ekran seçeneğinde bu parametrenin herhangi bir işlevi yoktur. |
| Yatay | Raporun sadece yazıcı seçeneği ile bastırılması durumunda kullanılan seçenektir. Döküm yapılacak kağıdın genişliğine göre rapor dikey veya yatay olarak alınabilir. Raporun kağıda yatay olarak basılması için işaretlenmesi gereken seçenektir. Ekran seçeneğinde bu parametrenin herhangi bir işlevi yoktur. |
| Proje Bazlı Rapor Ekranı | Yazıcı Seçenekleri |
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
| ![](../../../../../_assets/53859e19eb2737b88a17.jpg) | "Ön Sorgulama" sekmesinde verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Rapor almak için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki rapor işleminde kullanılmak üzere saklanır. |
| ![](../../../../../_assets/4ad6cc61ca2c42a19c85.jpg) | "Proje Bazlı Rapor" ekranı hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) | Rapor almak için verilen kısıtların iptal edildiği butondur. |
