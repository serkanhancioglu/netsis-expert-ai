---
title: "Muavin"
page_id: "24740693"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Muhasebe"
  - "Muhasebe Modülü"
  - "Raporlar / Muhasebe"
  - "Muavin"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / Raporlar / Muhasebe / Muavin"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWE5MjYyYjkzLThlN2MtNDE1ZS05NGU0LWFiNDQxYWE0ZGM4YSZsaW5rPWJjYWE2NzI3LWI4MzMtNDgxZi1iNjFhLTBmOTA1M2I1YWU4NSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=a9262b93-8e7c-415e-94e4-ab441aa4dc8a&link=bcaa6727-b833-481f-b61a-0f9053b5ae85&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "muavin_41158501_24740693.html"
source_version: "2022-10-07T09:43:30.417+03:00"
source_bytes: 317009
fetched_at: "2026-09-13T04:13:43+00:00"
generator: "netsis-scraper 1.0.0"
---
# Muavin

Muavin, Muhasebe Bölümünde, "Raporlar/Muhasebe Modülü" menüsünün altında yer alır. Muavin; sadece muavin hesapların, belirlenen tarih aralığında, tek tek fiş hareket dökümünün alınmasını sağlayan rapordur. Muavin ekranı; Ön Sorgulama-1, Ön Sorgulama-2, Ölçekleme ve Yazıcı Seçenekleri sekmelerinden oluşur.

**Ön Sorgulama-1**

![](../../../../_assets/f534a6e95fb902c14fde.png)

Muavin ekranı Ön Sorgulama-1 sekmesinde yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| Muavin Ekranı |  |
| --- | --- |
| Hesap Kodu Aralığı | Belli bir aralıktaki hesap koduna ait döküm alınması istendiğinde kullanılan alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılarak kısıt verilir. |
| Hesap Kodu Maskesi | Hesap kodlarına filtre tanımlanarak liste alınmasını sağlayan alandır. **Örneğin;** Ana hesap kodu 1 rakamı ile başlayan hesapların listesi alınacaksa, bu alana %100 değerinin girilmesi gerekir. Maskeleme alanına “\_” tek bir karakter yerine “%” birden fazla bilinmeyen karakter girilebilir. |
| Hesap Hariç Aralığı | Muavin raporundan hariç tutulması istenen hesap kodlarının başlangıç ve bitiş kodlarının tanımlandığı alandır. Tanımlanan hesap kodlarının haricindeki hesap kodlarının rapora dahil edilmesini sağlar. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg)ile, hesap kodları arasından seçim yapılarak kısıt verilir. |
| Tarih Fiş Aralığı | Muavin raporu almak için tarih fiş aralığı kısıtı girilen alandır. Tarih ve Evrak Tarihi olarak iki seçenekten oluşur. |
| Tarih | "Tarih Fiş Aralığı" alanında yapılan seçime göre tarih başlangıç ve bitiş aralığı kısıtı verilen alandır. |
| Referans Kodu Aralığı | Referans kodu takibinin yapıldığı durumlarda, referans kodu kısıtı girilen alandır. Muhasebe → Kayıt → [Muhasebe Parametreleri](<../Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/Muhasebe Modülü Tanımlamaları/Muhasebe Parametreleri - Muhasebe.md>) → "Fişlerde Referans Kodu Sorulsun" parametresinin işaretlenmesi ile aktif hale gelir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg)ile, hesap kodları arasından seçim yapılarak kısıt verilir. |
| Referans Kodu Maskesi | Referans kodlarına filtre tanımlayarak liste alınmasını sağlayan alandır. **Örneğin;** Referans kodu 10 ile başlayan kayıtlara ait liste alınması istendiğinde, "Referans Kodu Maskesi" alanına 10% şeklinde bir maskeleme yapılması gerekir. Maskeleme alanına “\_” tek bir karakter yerine “%” birden fazla bilinmeyen karakter girilebilir. |
| Şubeler Dahil Mi? | Muavin raporuna şubelerin dahil edilmesi için kullanılan seçenektir. |
| Miktar Yazılsın | Fişlere ait miktar bilgilerinin muavin raporunda listelenmesi için kullanılan seçenektir. |
| Muhasebe Kodu Toplamlı | Bir yevmiye fişinde aynı muavin hesap koduna birden fazla kayıt girildiği durumlarda, detaylı döküm almak yerine aynı hesap kodlu muavinlerin fiş bazında "Borç/Alacak" toplamlarına göre ayrı ayrı listesinin alınması için kullanılan seçenektir. |
| Bakiye Basılsın | Raporda borç/alacak farkını veren bakiye kolonunun gösterilmesi için işaretlenen seçenektir. |
| Ay Kırılmasında Toplam | Her bir aya ait hareket listesi alınırken ay toplamları alınarak listelenmesi için kullanılan seçenektir. |
| Hesap Kırılmasında Sayfa Başı | Her bir hesap kodu değişiminde dökümün yeni bir sayfadan başlaması için kullanılan seçenektir. |
| Sadece TL Kayıtlar Dökülsün | Sadece TL çalışan hesaplara ait kayıtların raporda listelenmesi için kullanılan seçenektir. Örneğin; hesap dövizli hareket görmüşse, **"Sadece TL Kayıtlar Dökülsün"** seçeneği işaretlendiğinde raporda listelenmez. |
| Hesap Adı | Raporda listelenecek hesap isimlerinin; "Hesap Planı" ekranında yer alan "Hesap İsmi" alanındaki isim olarak listelenmesi için **Türkçe,** "Hesap Planı" ekranında yer alan "Yabancı Hesap İsmi" alanındaki isim olarak listelenmesi için **Diğer** seçeneğinin işaretlenmesi gerekir. |
| ![](../../../../_assets/7ba39f9046a578093326.png) Rapor | Yukarıdaki alanlara girilen bilgiler doğrultusunda, rapor almak için kullanılan butondur. Butonun sağ tarafında yer alan aşağı ok tuşu, "Gelişmiş Rapor" seçeneğinin kullanılmasını sağlar. Kullanıcı, "Gelişmiş Rapor" seçeneği ile ekrana gelen tablo üzerinde hesaplama yapabilir. Bu seçenek sayesinde, 13684 satırın üstündeki raporlamaların da tek sayfa üzerinden raporlanması sağlanır. "Rapor" seçeneği Text Dosya, Excel Dosya, VTS Format, HTML kayıt türlerini desteklerken, "Gelişmiş Rapor" seçeneği Excel Workbook, Excel Template, Excel 97-2003 Workbook, Excel 97-2003 Template, Comma Delimited, Text Document, Web Page, XML Document, PDF Document kayıt türlerini destekler. |
| ![](../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Ön Sorgulama sayfasında verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Muavin almak için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki muavin alma işleminde kullanılmak üzere saklanır. |
| ![](../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | Muavin ekranı hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Muavin listesi almak için verilen kısıtların iptal edildiği butondur. |

**Ön Sorgulama-2**

![](../../../../_assets/7b3c0bfbff32c93788f9.png)

Muavin ekranı Ön Sorgulama-2 sekmesinde yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| Muavin Ekranı |  |
| --- | --- |
| Döviz Yazılsın | Raporda fişlere ait döviz değerleri varsa, bu bilgilerin listelenmesi için kullanılan seçenektir. Ön muhasebe ya da yevmiye fiş kayıtlarından elle kaydedilen döviz değerlerinin listelenmesi için **“Operasyon”**, muhasebede “Enflasyon/Dövize Göre Çevrim” işlemi sonucunda oluşan döviz değerlerinin listelenmesi için **“Firma”** seçeneğinin seçilmesi gerekir. Tüm döviz tiplerine ait değerlerin bir arada alınması için **“Hepsi”**, döviz ile ilgili değerlerin raporda görüntülenmemesi için **“Hiçbiri”** seçeneğinin işaretlenmesi gerekir. |
| Döviz Tipi | Raporda listelenmesi istenen döviz tipinin belirlendiği alandır. Tüm döviz tiplerine ait hesapların listelenmesi istendiğinde boş bırakılır. |
| Açıklama 2/Açıklama 3 Basılsın | Yevmiye fiş kayıtlarındaki Açıklama 2 ve Açıklama 3 alanlarının raporda listelenmesi için kullanılan seçenektir. |
| Proje Kodu Aralığı | Muavin almak için proje kodu aralığı kısıtı girilen alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, proje kodları arasından seçim yapılır. Yardımcı Programlar → Kayıt → [Şirket-Şube Parametre Tanımları](<../../../Genel/Yardımcı Programlar/Kayıt - Yardımcı Programlar/Şirket - Şube - Parametre Tanımları.md>) → "Proje Uygulaması Var" parametresinin işaretlenmesi ile aktif hale gelir. |
| Proje Hariç Aralığı | Raporda belli bir proje koduna ait hesapların hariç tutulması için proje kodu kısıtı verilen alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile proje kodları arasından seçim yapılır. Yardımcı Programlar → Kayıt → [Şirket-Şube Parametre Tanımları](<../../../Genel/Yardımcı Programlar/Kayıt - Yardımcı Programlar/Şirket - Şube - Parametre Tanımları.md>) → "Proje Uygulaması Var" parametresinin işaretlenmesi ile aktif hale gelir. |
| Proje Kodu Basılmasın | Muavin listesinde proje kodlarının basılmaması için kullanılan seçenektir. |
| Madde Numaraları Basılsın | Raporda listelenecek hesaplara ait resmi defter numaralarının (varsa) basılması için kullanılan seçenektir. Madde numaraları, “Resmi Basım” seçeneği işaretlenerek yevmiye defter basımı yapıldığında fişlere aktarılır. "Yevmiye Defter Basımı" ile ilgili detaylı bilgi için; Muhasebe → Raporlar → Kanuni Defter Basımı → [Yevmiye Defteri](<Kanuni Defter Basımı/Yevmiye Defteri.md>) dokümanına bakılabilir. |
| Hareket Görmemiş Hesaplar Basılsın | Hiç hareket görmeyen hesapların listelenmesi için kullanılan seçenektir. |
| Bakiyesi Sıfır Olan Hesaplar Basılmasın | Bakiyesi sıfırdan büyük olan hesapların listelenmesi için kullanılan seçenektir. |
| Kaynak Belge Bilgileri Basılsın | Muavin listesinde kaynak belge bilgilerinin basılması için kullanılan seçenektir. |
| Fiş Tipi Basılsın | Raporda listelenecek olan hesapların ait olduğu fiş tiplerinin (Mahsup/Tediye/Tahsil/Açılış/Kapanış Fişi) basılması için kullanılan seçenektir. |
| Kullanıcı No Basılsın | Kaydı yapan kullanıcının belli olması için kullanılan seçenektir. İşaretlendiğinde kullanıcı numaraları raporda listelenir. |
| Referans Kodu Basılmasın | Muavin listesinde referans kodunun basılmaması için kullanılan seçenektir. |
| Hesap Adı, Açıklama | Muavin listesinde hesap adı ve açıklama uzunluğunun belirlendiği alandır. Alanın sol tarafındaki "Gösterilsin" kutucuğu işaretlendikten sonra, "Uzunluk" alanına değer girişi yapılır. |
| ![](../../../../_assets/7ba39f9046a578093326.png) Rapor | Yukarıdaki alanlara girilen bilgiler doğrultusunda, rapor almak için kullanılan butondur. Butonun sağ tarafında yer alan aşağı ok tuşu, "Gelişmiş Rapor" seçeneğinin kullanılmasını sağlar. Kullanıcı, "Gelişmiş Rapor" seçeneği ile ekrana gelen tablo üzerinde hesaplama yapabilir. Bu seçenek sayesinde, 13684 satırın üstündeki raporlamaların da tek sayfa üzerinden raporlanması sağlanır. "Rapor" seçeneği Text Dosya, Excel Dosya, VTS Format, HTML kayıt türlerini desteklerken, "Gelişmiş Rapor" seçeneği Excel Workbook, Excel Template, Excel 97-2003 Workbook, Excel 97-2003 Template, Comma Delimited, Text Document, Web Page, XML Document, PDF Document kayıt türlerini destekler. |
| ![](../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Ön Sorgulama sayfasında verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Muavin almak için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki muavin alma işleminde kullanılmak üzere saklanır. |
| ![](../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | Muavin ekranı hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Muavin listesi almak için verilen kısıtların iptal edildiği butondur. |

**Ölçekleme**

Standart raporlarda miktar, fiyat, tutar, kur, döviz tutarı, döviz fiyatı, firma döviz tutarı ve oran alanları için ölçekleme yapılmasını sağlayan sekmedir.

**![](../../../../_assets/474ce1870660ea7ad16a.png)**

**Örneğin;**

Fiyat ve tutar alanlarına 1.000 yazılması, fiyat ve tutara getirilecek verilerin 1.000'e bölüneceği anlamına gelir.

**Yazıcı Seçenekleri**

**![](../../../../_assets/2ae4d8b76e48d3484102.png)**

| Muavin Ekranı |  |
| --- | --- |
| Ekran | Raporun ekrandan alınması için işaretlenmesi gereken seçenektir. Hiçbir değişiklik yapılmaması durumunda, raporda ekran seçeneği işaretli olduğu için, rapor yine ekrandan alınır. |
| Yazıcı | Raporun yazıcıdan alınması için işaretlenmesi gereken seçenektir |
| Toplam Sayfa | Rapor yazıcıya döküldüğü zaman yazıcıdan kaç sayfa çıkarılacağının gösterildiği alandır. Kullanıcı, raporu yazıcıya göndermeden önce bu seçeneği işaretleyerek ![](../../../../_assets/21c20c78203acae9cce6.jpg)butonuna basarsa, yazıcıya dökülecek sayfa adedi ekranda görüntülenir. ![](../../../../_assets/b2e157c1e0713bfefb94.png) |
| Muavin Ekranı | Yazıcı Seçenekleri - Yönlendirme |
| Dikey | Raporun sadece yazıcı seçeneği ile bastırılması durumunda kullanılan seçenektir. Döküm yapılacak kağıdın genişliğine göre rapor dikey veya yatay olarak alınabilir. Bu seçenekte hiçbir değişiklik yapılmaması durumunda otomatik olarak "Dikey" işaretlenmiş olduğu için rapor dikey şekilde basılır. Ekran seçeneğinde bu parametrenin herhangi bir işlevi yoktur. |
| Yatay | Raporun sadece yazıcı seçeneği ile bastırılması durumunda kullanılan seçenektir. Döküm yapılacak kağıdın genişliğine göre rapor dikey veya yatay olarak alınabilir. Raporun kağıda yatay olarak basılması için işaretlenmesi gereken seçenektir. Ekran seçeneğinde bu parametrenin herhangi bir işlevi yoktur. |
| Muavin Ekranı | Yazıcı Seçenekleri |
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
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) | Ön Sorgulama sayfasında verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Muavin almak için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki muavin alma işleminde kullanılmak üzere saklanır. |
| ![](../../../../_assets/4ad6cc61ca2c42a19c85.jpg) | Muavin ekranı hakkında standart yardım bilgisi için kullanılan butondur. |
|  | Muavin listesi almak için verilen kısıtların iptal edildiği butondur. |
