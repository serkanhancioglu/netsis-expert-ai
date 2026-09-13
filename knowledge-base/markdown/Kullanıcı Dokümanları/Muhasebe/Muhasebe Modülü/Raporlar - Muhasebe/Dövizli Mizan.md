---
title: "Dövizli Mizan"
page_id: "24740783"
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
  - "Dövizli Mizan"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / Raporlar / Muhasebe / Dövizli Mizan"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTY4ZjU5YzMzLTRkZDEtNDA3Yy05ZDAzLTBhMDZhMTIyOWVmYSZsaW5rPTdjOTRlYjNjLTcxODMtNGM1Yi1hOGFjLWYzZDFkZDdmYmZhMSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=68f59c33-4dd1-407c-9d03-0a06a1229efa&link=7c94eb3c-7183-4c5b-a8ac-f3d1dd7fbfa1&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "dovizli-mizan_41161429_24740783.html"
source_version: "2022-10-17T09:45:32.767+03:00"
source_bytes: 308603
fetched_at: "2026-09-13T04:14:00+00:00"
generator: "netsis-scraper 1.0.0"
---
# Dövizli Mizan

Dövizli Mizan, Muhasebe Bölümünde, "Raporlar/Muhasebe Modülü" menüsünün altında yer alır. Dövizli Mizan, "[Tarih Aralıklı Mizan](<Tarih Aralıklı Mizan.md>)" raporunun aynısının, döviz tipleri ve döviz tutarları ile alınmasını sağlayan rapordur. Dövizli Mizan; Ön Sorgulama-1, Ön Sorgulama-2, Ölçekleme ve Yazıcı Seçenekleri sekmelerinden oluşur.

**Ön Sorgulama-1**

![](../../../../_assets/54297bdf41165371ef75.png)

Dövizli Mizan ekranında yer alan Ön Sorgulama-1 sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Dövizli Mizan Ekranı |  |
| --- | --- |
| Hesap Türü (Ana/Grup/Muavin/Hepsi) | Hesap planında hesap türüyle tanımlanan hesaplar bazında mizan alınması için kullanılan alandır. Ana, Grup, Muavin ve Hepsi seçeneklerinden oluşur. **Örneğin;** "Ana" işaretlendiğinde, mizan ana hesaplar bazında listelenir ve diğer hesap türleri görülmez. |
| Hesap Kodu Aralığı | Belli bir aralıktaki hesap koduna ait döküm alınması istendiğinde kullanılan alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılarak kısıt verilir. |
| Hesap Kodu Maskesi | Hesap kodlarına filtre tanımlanarak liste alınmasını sağlayan alandır. **Örneğin;** Ana hesap kodu 1 rakamı ile başlayan hesapların listesi alınacaksa, bu alana %100 değerinin girilmesi gerekir. Maskeleme alanına “\_” tek bir karakter yerine “%” birden fazla bilinmeyen karakter girilebilir. |
| Hesap Hariç Aralığı | Mizan raporundan hariç tutulması istenen hesap kodlarının başlangıç ve bitiş kodlarının tanımlandığı alandır. Tanımlanan hesap kodlarının haricindeki hesap kodlarının rapora dahil edilmesini sağlar. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılarak kısıt verilir. |
| Tarih | Mizan için başlangıç ve bitiş tarih aralığı kısıtı verilen alandır. |
| Miktar Yazılsın | Mizanda, fişlere ait miktar bilgilerinin listelenmesi için kullanılan seçenektir. "Ölçü Birimi" alanının rapora gelmesi için "Miktar Yazılsın" seçeneğinin işaretlenmesi gerekir. |
| Dövizli Bakiye Yazılsın | Bakiye tutarının dövizli olarak listelenmesi için işaretlenen seçenektir. |
| Sıfır Bakiyeliler Dahil Edilsin | Sıfır bakiyeli hesapların raporda listelenmesi için kullanılan seçenektir |
| Hareket Görmemiş Hesaplar Basılsın | Hiç hareket görmeyen hesapların listelenmesi için kullanılan seçenektir. |
| Grup Hesap Toplamı | Grup hesaplar bazında toplam alınarak mizan alınması için kullanılan seçenektir. İşaretlendiğinde, her grup hesap değişiminde o gruba ait toplam alınır. |
| Proje Kodu Kırılımı | Mizan raporunda proje kodu kırılımı yapılması için kullanılan seçenektir. |
| Kapanış Fişleri Hariç Tutulsun | Dövizli mizan raporunda kapanış fişlerinin yer almaması için kullanılan seçenektir. |
| Açılış Fişleri Hariç Tutulsun | Dövizli mizan raporunda açılış fişlerinin yer almaması için kullanılan seçenektir. |
| Parasal Hesap (Evet/Hayır/Hepsi) | Muhasebe → Kayıt → Hesap Planı → "Döviz Bilgileri" sekmesinde yer alan "Parasal Hesap" alanları işaretlenen hesapların mizan raporu alınması için **Evet**, İşaretli olmayan hesapların mizan raporu için **Hayır**, parasal hesap ayrımı yapılmadan tüm hesapların mizan raporu için **Hepsi** seçeneğinin işaretlenmesi gerekir. |
| Değerlensin | Muhasebe → Kayıt → Hesap Planı → "Döviz Bilgileri" sekmesinde yer alan “Düzeltilecek Hesap” alanları işaretlenen hesapların mizan raporu alınması için **Evet**, İşaretli olmayan hesapların mizan raporu için **Hayır**, parasal hesap ayrımı yapılmadan tüm hesapların mizan raporu için **Hepsi** seçeneğinin işaretlenmesi gerekir. |
| Hesap Adı | Raporda listelenecek hesap isimlerinin; "Hesap Planı" ekranında yer alan "Hesap İsmi" alanındaki isim olarak listelenmesi için **Türkçe,** "Hesap Planı" ekranında yer alan "Yabancı Hesap İsmi" alanındaki isim olarak listelenmesi için **Diğer** seçeneğinin işaretlenmesi gerekir. |
| Döviz Yazılsın (Operasyon/Firma/Döviz) | İşaretlenecek seçeneğe göre; ön muhasebede veya yevmiye fiş kayıtlarında elle yapılan işlemlerde kullanılan (operasyon) döviz tipine göre veya Muhasebe → İşlemler → "Dövize Çevrim" bölümünün çalıştırılması ile oluşturulan firma döviz tipine göre mizan alınmasını sağlayan alandır. |
| Döviz Tipi | Raporda listelenmesi istenen döviz tipinin belirlendiği alandır. Tüm döviz tiplerine ait hesapların listelenmesi istendiğinde boş bırakılır. |
| Cari Detay Gösterilsin | Dövizli mizan raporunda cari detay bilgisinin yer alması için kullanılan seçenektir. |
| ![](../../../../_assets/7ba39f9046a578093326.png) Rapor | Yukarıdaki alanlara girilen bilgiler doğrultusunda, rapor almak için kullanılan butondur. Butonun sağ tarafında yer alan aşağı ok tuşu, "Gelişmiş Rapor" seçeneğinin kullanılmasını sağlar. Kullanıcı, "Gelişmiş Rapor" seçeneği ile ekrana gelen tablo üzerinde hesaplama yapabilir. Bu seçenek sayesinde, 13684 satırın üstündeki raporlamaların da tek sayfa üzerinden raporlanması sağlanır. "Rapor" seçeneği Text Dosya, Excel Dosya, VTS Format, HTML kayıt türlerini desteklerken, "Gelişmiş Rapor" seçeneği Excel Workbook, Excel Template, Excel 97-2003 Workbook, Excel 97-2003 Template, Comma Delimited, Text Document, Web Page, XML Document, PDF Document kayıt türlerini destekler. |
| ![](../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Ön Sorgulama sayfasında verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Mizan almak için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki mizan alma işleminde kullanılmak üzere saklanır. |
| ![](../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | Mizan ekranı hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Mizan listesi almak için verilen kısıtların iptal edildiği butondur. |

**Ön Sorgulama-2**

![](../../../../_assets/2306aabeab10151862eb.png)

Dövizli Mizan ekranında yer alan Ön Sorgulama-2 sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Dövizli Mizan Ekranı |  |
| --- | --- |
| Saha Adı | Kısıt sekmesine ![](../../../../_assets/b549ef7a3208cdf4829b.png) tıklanması ile görüntülenir. Tarih aralıklı mizan için baz alınacak saha adı için kısıt verilen alandır. İlgili hücre üzerinde iken klavyede yer alan **Boşluk Çubuğuna** basılarak aktif hale gelen aşağı ok butonu, kısıt verilmesi istenen sahalara ulaşılmasını sağlar. |
| ![](../../../../_assets/7ba39f9046a578093326.png) Rapor | Yukarıdaki alanlara girilen bilgiler doğrultusunda, rapor almak için kullanılan butondur. Butonun sağ tarafında yer alan aşağı ok tuşu, "Gelişmiş Rapor" seçeneğinin kullanılmasını sağlar. Kullanıcı, "Gelişmiş Rapor" seçeneği ile ekrana gelen tablo üzerinde hesaplama yapabilir. Bu seçenek sayesinde, 13684 satırın üstündeki raporlamaların da tek sayfa üzerinden raporlanması sağlanır. "Rapor" seçeneği Text Dosya, Excel Dosya, VTS Format, HTML kayıt türlerini desteklerken, "Gelişmiş Rapor" seçeneği Excel Workbook, Excel Template, Excel 97-2003 Workbook, Excel 97-2003 Template, Comma Delimited, Text Document, Web Page, XML Document, PDF Document kayıt türlerini destekler. |
| ![](../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Ön Sorgulama sayfasında verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Mizan almak için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki mizan alma işleminde kullanılmak üzere saklanır. |
| ![](../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | Mizan ekranı hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Mizan listesi almak için verilen kısıtların iptal edildiği butondur. |

**Ölçekleme**

Standart raporlarda miktar, fiyat, tutar, kur, döviz tutarı, döviz fiyatı, firma döviz tutarı ve oran alanları için ölçekleme yapılmasını sağlayan sekmedir.

![](../../../../_assets/f5c8a5c9b8ec231ce529.png)

**Örneğin;**

Fiyat ve tutar alanlarına 1.000 yazılması, fiyat ve tutara getirilecek verilerin 1.000'e bölüneceği anlamına gelir.

**Yazıcı Seçenekleri**

**![](../../../../_assets/4ffc17671f9c7a9e5687.png)**

| Dövizli Mizan Ekranı |  |
| --- | --- |
| Ekran | Raporun ekrandan alınması için işaretlenmesi gereken seçenektir. Hiçbir değişiklik yapılmaması durumunda, raporda ekran seçeneği işaretli olduğu için, rapor yine ekrandan alınır. |
| Yazıcı | Raporun yazıcıdan alınması için işaretlenmesi gereken seçenektir |
| Toplam Sayfa | Rapor yazıcıya döküldüğü zaman yazıcıdan kaç sayfa çıkarılacağının gösterildiği alandır. Kullanıcı, raporu yazıcıya göndermeden önce bu seçeneği işaretleyerek ![](../../../../_assets/21c20c78203acae9cce6.jpg)butonuna basarsa, yazıcıya dökülecek sayfa adedi ekranda görüntülenir. ![](../../../../_assets/b2e157c1e0713bfefb94.png) |
| Dövizli Mizan Ekranı | Yazıcı Seçenekleri - Yönlendirme |
| Dikey | Raporun sadece yazıcı seçeneği ile bastırılması durumunda kullanılan seçenektir. Döküm yapılacak kağıdın genişliğine göre rapor dikey veya yatay olarak alınabilir. Bu seçenekte hiçbir değişiklik yapılmaması durumunda otomatik olarak "Dikey" işaretlenmiş olduğu için rapor dikey şekilde basılır. Ekran seçeneğinde bu parametrenin herhangi bir işlevi yoktur. |
| Yatay | Raporun sadece yazıcı seçeneği ile bastırılması durumunda kullanılan seçenektir. Döküm yapılacak kağıdın genişliğine göre rapor dikey veya yatay olarak alınabilir. Raporun kağıda yatay olarak basılması için işaretlenmesi gereken seçenektir. Ekran seçeneğinde bu parametrenin herhangi bir işlevi yoktur. |
| Dövizli Mizan Ekranı | Yazıcı Seçenekleri |
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
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) | Ön Sorgulama sayfasında verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Mizan almak için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki mizan alma işleminde kullanılmak üzere saklanır. |
| ![](../../../../_assets/4ad6cc61ca2c42a19c85.jpg) | Mizan ekranı hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) | Mizan listesi almak için verilen kısıtların iptal edildiği butondur. |
