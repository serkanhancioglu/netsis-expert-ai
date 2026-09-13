---
title: "Tarih Aralıklı Mizan"
page_id: "24740772"
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
  - "Tarih Aralıklı Mizan"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / Raporlar / Muhasebe / Tarih Aralıklı Mizan"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWNjNjkxNjE3LTczZmYtNGIwOC04ODM1LTU4Y2U4M2Q4MTYxNyZsaW5rPWE3ODNmYzkwLTVmMWMtNDcxNy04YjFiLTA1MzhiYWM2ZDZlOSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=cc691617-73ff-4b08-8835-58ce83d81617&link=a783fc90-5f1c-4717-8b1b-0538bac6d6e9&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "tarih-aralikli-mizan_24740778_24740772.html"
source_version: "2022-10-17T09:26:23.930+03:00"
source_bytes: 402592
fetched_at: "2026-09-13T04:13:59+00:00"
generator: "netsis-scraper 1.0.0"
---
# Tarih Aralıklı Mizan

Tarih Aralıklı Mizan, Muhasebe Bölümünde, "Raporlar/Muhasebe Modülü" menüsünün altında yer alır. Tarih Aralıklı Mizan; belirlenen tarih aralığında, ay kısıtlaması getirilmeden mizan alınması için kullanılan bölümdür. Tarih Aralıklı Mizan raporunun diğer mizan raporundan farkı, alınacak dökümün 5 günlük, 3 aylık, 12 aylık gibi zaman dilimlerine göre alınmasıdır. Tarih Aralıklı Mzan; Ön Sorgulama-1, Ön Sorgulama-2, Muhasebe Kısıtları, Ölçekleme ve Yazıcı Seçenekleri sekmelerinden oluşur.

**Ön Sorgulama-1**

![](../../../../_assets/e077b13f63d2fe94beb8.png)

Tarih Aralıklı Mizan ekranı Ön Sorgulama-1 sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Tarih Aralıklı Mizan |  |
| --- | --- |
| Hesap Türü (Ana/Grup/Muavin/Hepsi) | Hesap planında hesap türüyle tanımlanan hesaplar bazında mizan alınması için kullanılan alandır. Ana, Grup, Muavin ve Hepsi seçeneklerinden oluşur. **Örneğin;** "Ana" işaretlendiğinde, mizan ana hesaplar bazında listelenir ve diğer hesap türleri görülmez. |
| Hesap Kodu Aralığı | Belli bir aralıktaki hesap koduna ait döküm alınması istendiğinde kullanılan alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılarak kısıt verilir. |
| Hesap Kodu Maskesi | Hesap kodlarına filtre tanımlanarak liste alınmasını sağlayan alandır. **Örneğin;** Ana hesap kodu 1 rakamı ile başlayan hesapların listesi alınacaksa, bu alana %100 değerinin girilmesi gerekir. Maskeleme alanına “\_” tek bir karakter yerine “%” birden fazla bilinmeyen karakter girilebilir. |
| Hesap Hariç Aralığı | Mizan raporundan hariç tutulması istenen hesap kodlarının başlangıç ve bitiş kodlarının tanımlandığı alandır. Tanımlanan hesap kodlarının haricindeki hesap kodlarının rapora dahil edilmesini sağlar. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılarak kısıt verilir. |
| Tarih | Mizan için başlangıç ve bitiş tarih aralığı kısıtı verilen alandır. |
| Cari Detay Gösterilsin | Cari detayın mizanda gösterilmesi için kullanılan seçenektir. |
| Cari Kodu Aralığı | "Cari Detay Gösterilsin" seçeneğinin işaretlenmesi ile aktif hale gelen alandır. Tarih aralıklı mizan almak için cari kod başlangıç ve bitiş aralık kısıtı verilen alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, kodlar arasından seçim yapılır. |
| Hareket Görmemiş Hesaplar Basılsın | Hiç hareket görmeyen hesapların listelenmesi için kullanılan seçenektir. |
| Kapanış Fişleri Hariç Tutulsun | Tarih aralıklı mizan raporunda kapanış fişlerinin yer almaması için kullanılan seçenektir. |
| Açılış Fişleri Hariç Tutulsun | Tarih aralıklı mizan raporunda açılış fişlerinin yer almaması için kullanılan seçenektir. |
| İşletmeler Dahil Edilsin | "Şubeli Muhasebe Sistemi" kullanıldığında merkez işletmeden girildiğinde aktif hale gelen seçenektir. İşaretlendiğinde "İşletme Kodu Aralığı" alanı aktif hale gelerek işletme aralığı verildiğinde, rapora sadece o işletmelere ait veriler getirilir. İşletme aralığı verilmediğinde ise tüm işletmelere ait veriler rapor ekranına gelir. "İşletmeler Dahil Edilsin" seçeneği işaretlendiğinde "Kümüle Rapor" seçeneği aktif hale gelerek, işaretlenmesi halinde işletmelerin hesap kodu bazında toplam verisini, işaretlenmediği durumlarda ise işletme kodu bazında kırılım yapılarak rapor ekranına veri gelir. |
| Şubeler Dahil | Mizan raporuna şubelerin dahil edilmesi için kullanılan seçenektir. |
| Grup Hesap Toplamı | Grup hesaplar bazında toplam alınarak mizan alınması için kullanılan seçenektir. İşaretlendiğinde, her grup hesap değişiminde o gruba ait toplam alınır. |
| Miktar Yazılsın | Mizanda, fişlere ait miktar bilgilerinin listelenmesi için kullanılan seçenektir. Ayrıca bu seçenek işaretlendiğinde, "Ölçü Birimi" alanının da rapora gelmesi sağlanır. |
| Sıfır Bakiyeliler Dahil Edilsin | Sıfır bakiyeli hesapların raporda listelenmesi için kullanılan seçenektir |
| Hesap Adı | Raporda listelenecek hesap isimlerinin; "Hesap Planı" ekranında yer alan "Hesap İsmi" alanındaki isim olarak listelenmesi için **Türkçe,** "Hesap Planı" ekranında yer alan "Yabancı Hesap İsmi" alanındaki isim olarak listelenmesi için **Diğer** seçeneğinin işaretlenmesi gerekir. |
| Mükellef Tipi | Mizan için mükellef tipi kısıtı verilen alandır. "Gelir Vergisi Mükellefleri İçin" veya "Kurumlar Vergisi Mükellefleri İçin" kısıt verilebilir. |
| ![](../../../../_assets/7ba39f9046a578093326.png) Rapor | Yukarıdaki alanlara girilen bilgiler doğrultusunda, rapor almak için kullanılan butondur. Butonun sağ tarafında yer alan aşağı ok tuşu, "Gelişmiş Rapor" seçeneğinin kullanılmasını sağlar. Kullanıcı, "Gelişmiş Rapor" seçeneği ile ekrana gelen tablo üzerinde hesaplama yapabilir. Bu seçenek sayesinde, 13684 satırın üstündeki raporlamaların da tek sayfa üzerinden raporlanması sağlanır. "Rapor" seçeneği Text Dosya, Excel Dosya, VTS Format, HTML kayıt türlerini desteklerken, "Gelişmiş Rapor" seçeneği Excel Workbook, Excel Template, Excel 97-2003 Workbook, Excel 97-2003 Template, Comma Delimited, Text Document, Web Page, XML Document, PDF Document kayıt türlerini destekler. |
| ![](../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Ön Sorgulama sayfasında verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Mizan almak için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki mizan alma işleminde kullanılmak üzere saklanır. |
| ![](../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | Mizan ekranı hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Mizan listesi almak için verilen kısıtların iptal edildiği butondur. |

**Ön Sorgulama-2**

**![](../../../../_assets/c8ca09af99d219d1bf20.png)**

Tarih Aralıklı Mizan ekranı Ön Sorgulama-2 sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Tarih Aralıklı Mizan Ekranı |  |
| --- | --- |
| Kesin Mizan XML Dosyası Oluşturulsun | Kesin mizan XML dosyası oluşturulması için kullanılan seçenektir. "Kesin Mizan XML Dosyası Oluşturulsun" başlığının üzerine tıklanarak dosya oluşturulur. |
| Saha Adı | Kısıt sekmesine ![](../../../../_assets/b549ef7a3208cdf4829b.png) tıklanması ile görüntülenir. Tarih aralıklı mizan için baz alınacak saha adı için kısıt verilen alandır. İlgili hücre üzerinde iken klavyede yer alan **Boşluk Çubuğuna** basılarak aktif hale gelen aşağı ok butonu, kısıt verilmesi istenen sahalara ulaşılmasını sağlar. |
| ![](../../../../_assets/7ba39f9046a578093326.png) Rapor | Yukarıdaki alanlara girilen bilgiler doğrultusunda, rapor almak için kullanılan butondur. Butonun sağ tarafında yer alan aşağı ok tuşu, "Gelişmiş Rapor" seçeneğinin kullanılmasını sağlar. Kullanıcı, "Gelişmiş Rapor" seçeneği ile ekrana gelen tablo üzerinde hesaplama yapabilir. Bu seçenek sayesinde, 13684 satırın üstündeki raporlamaların da tek sayfa üzerinden raporlanması sağlanır. "Rapor" seçeneği Text Dosya, Excel Dosya, VTS Format, HTML kayıt türlerini desteklerken, "Gelişmiş Rapor" seçeneği Excel Workbook, Excel Template, Excel 97-2003 Workbook, Excel 97-2003 Template, Comma Delimited, Text Document, Web Page, XML Document, PDF Document kayıt türlerini destekler. |
| ![](../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Ön Sorgulama sayfasında verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Mizan almak için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki mizan alma işleminde kullanılmak üzere saklanır. |
| ![](../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | Mizan ekranı hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Mizan listesi almak için verilen kısıtların iptal edildiği butondur. |

**Muhasebe Kısıtları**

**![](../../../../_assets/be137dd9a0c7e5698e27.png)**

Tarih Aralıklı Mizan ekranı Muhasebe Kısıtları sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Tarih Aralıklı Mizan Ekranı |  |
| --- | --- |
| Sahalar | Tarih Aralıklı Mizan raporu almak için kısıt verilmesi istenen alanlar yer alır. Ekle ![](../../../../_assets/b050fee00ab65632b16d.jpg) butonu ile istenen alanlar "kısıt verilecek sahalar" kısmına eklenir. |
| Kısıt Verilecek Sahalar | Tarih Aralıklı Mizan raporu almak için kısıt verilen sahaların yer aldığı alandır. Çıkar ![](../../../../_assets/a19640feaa753a52d048.jpg) butonu ile istenmeyen alanlar çıkarılır. |
| Eşit, Küçük, Küçük veya Eşit, Büyük, Büyük veya Eşit, Arasında, Benziyor, Eşit Boş, Eşit Değil, İçinde Eşit Değil | **Eşit:** İşaretlenen alanda belli bir sabit koşula göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "001" olan stok için liste alınacaksa "Eşit" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "001" girilir. Bu durumda, sadece "001" numaralı Stok Kodu için liste alınır. **Küçük:** İşaretlenen alanda belli bir değerden küçük olanlar koşuluna göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "100" olan stok için liste alınacaksa "Küçük" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" girilir. Bu durumda, "100'den küçük" numaralı Stok Kodu için liste alınır. **Küçük veya Eşit:** İşaretlenen alanda belli bir değere eşit veya küçük olanlar koşuluna göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "100" olan stok için liste alınacaksa "Küçük veya Eşit" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" girilir. Bu durumda, "100 ve 100'den küçük" numaralı Stok Kodu için liste alınır. **Büyük:** İşaretlenen alanda belli bir değerden büyük olanlar koşuluna göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "100" olan stok için liste alınacaksa "Büyük" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" girilir. Bu durumda, "100'den büyük" numaralı Stok Kodu için liste alınır. **Büyük veya Eşit:** İşaretlenen alanda belli bir değere eşit veya büyük olanlar koşuluna göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "100" olan stok için liste alınacaksa "Büyük veya Eşit" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" girilir. Bu durumda, "100 ve 100'den büyük" numaralı Stok Kodu için liste alınır. **Arasında:** Seçilen alanla ilgili bir aralık tanımlanması istendiğinde kullanılması gereken seçenektir. Eğer belli bir başlangıç ve bitiş değeri arasında kalan değerlerle ilgili kısıt verilecekse kullanılması gereken seçenektir. Örneğin; Stok Kodu kıstasında, "Arasında" seçeneği seçilip \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" ve yine \<tab\> tuşu ile ilerlenerek altta bulunan alana "200" yazıldığı varsayılsın. Böylece stok kodu 100 ile 200 arasındaki stok kodları için liste alınır. **Benziyor:** Cari ile ilgili kayıt ararken cari hesabın ismi tam olarak bilinmiyorsa benziyor seçeneği kullanılır. Örneğin; cari hesabın isminin CANEL ya da CENEL olacağı düşünülüyorsa, bu seçeneği seçtikten sonra alanın sağ tarafındaki kayıt alanına "C_NEL" yazıldığında, raporda cari ismi "C" ile başlayan ikinci karakteri herhangi bir karakter olan fakat sonu "NEL" ile biten kayıtlar listelenir. **Eşit Boş:** Seçilen sahada hiçbir bilgi olmadığında kullanılan seçenektir. Bu seçenek alfanumerik sahalar için geçerlidir. Sıfırdan büyük veya sıfıra eşit bilgilerin aranması durumunda "Eşit", "Büyük Eşit", "Küçük Eşit" seçenekleri kullanılabilir. **Eşit Değil:** Raporda seçilen Eşit, Küçük ve Eşit, Büyük, Büyük ve Eşit, Arasında, Benziyor ve Eşit Boş seçeneklerindeki belirlemeler olumsuz (hariç) anlamını taşıyorsa "Eşit Değil" seçeneği işaretlenir. Örneğin; stok kodunda "Eşit" seçildiğinde ve "0101" kodu girildiği varsayıldığında, "Eşit Değil" seçeneği işaretlendiğinde, raporda stok kodu "0101" olanların haricindeki stokların listeleneceği anlaşılır. |
| İse/Değil ise | **İse:** Raporda seçilen Eşit, Küçük ve Eşit, Büyük, Büyük ve Eşit, Arasında ve Benziyor seçeneklerindeki belirlemeler olumlu (dahil) anlamını taşıyorsa "İse" seçeneği işaretlenir. Örneğin; stok kodunda "Eşit" seçildiğinde ve "0101" kodu girildiği varsayıldığında, "İse" seçeneği işaretlenirse, rapora stok kodu "0101" olan stokların dahil edileceği anlaşılır. **Değil İse:** Raporda seçilen Eşit, Küçük ve Eşit, Büyük, Büyük ve Eşit, Arasında ve Benziyor seçeneklerindeki belirlemeler olumsuz (hariç) anlamını taşıyorsa "Değil İse" seçeneği işaretlenir. Örneğin; stok kodunda "Eşit" seçildiğinde ve "0101" kodu girildiği varsayıldığında, "Değil İse" seçeneği işaretlendiğinde, raporda stok kodu "0101" olanların haricindeki stokların listeleneceği anlaşılır. |
| Ve/Veya | **Ve:** Seçilen sahalarda zorunlu bağlantı koşulu sağlar. **Örnek 1:** Karmaşık bir stok kodlaması olduğu varsayıldığında; Bu kodlardan iki tanesinin raporda çıkması isteniyor fakat bu iki stok kodunun ortak hiçbir özelliği yok. Bu durumda, "Stok Kodu" sahası iki kez kısıt verilecek sahalar bölümüne aktarılır. 1.Stok Kodu kıstasında eşit bağlantısı kurularak ilk stok kodu girilir ve "VE" bağlacı işaretlenir. Daha sonra 2. Stok Kodu seçilerek yine eşit bağlantısı ile diğer bir stok kodu yazılır. Böylece, raporda sadece bu iki stok koduna ait bilgi alınır. Bu seçenekte tanımlanan her koşulun olması zorunludur. Yani, tanımlanan iki stok kodundan biri bile mevcut değil ise, rapor bilgi vermez. **Örnek 2:** Grup kodu 1, Kod 1 alanı 2 ve Kod 2 alanı 3 olan stoklarla ilgili bir liste alınması istendiğinde; Verilen tanımlamalarda "VE" bağlacı kullanılırsa, mutlaka bu üç kısıta da sahip olan stoklar aranır ve bulunursa listelenir. Üç kısıttan herhangi birine sahip olmayan stoklar raporda listelenmez. **Veya:** Seçilen sahalarda olabilirlik koşulu sağlar. Yani, tanımlanan koşullardan biri bile sağlansa ilgili raporla ilgili bilgi alınabilir. **Örnek 1:** Grup kodu 1, Kod 1 alanı 2 ve Kod 2 alanı 3 olan stoklarla ilgili bir liste alınması istendiğinde; Verilen tanımlamalarda "VEYA" bağlacı kullanılırsa, bu üç kısıttan birine bile sahip olan stoklar aranır ve bulunursa listelenir. |
| ![](../../../../_assets/c7275efbddc154ea1579.jpg) Sakla | Yapılan tanımlamaların onaylanması için kullanılan butondur. |
| ![](../../../../_assets/df428ea63894bc744f9a.jpg) İptal | Yapılan tanımlamaların iptal edilmesi için kullanılan butondur. |
| ![](../../../../_assets/7ba39f9046a578093326.png) Rapor | Fatura karlılık raporu almak için verilen kısıtlara göre Yukarıdaki alanlara girilen bilgiler doğrultusunda, rapor almak için kullanılan butondur. Butonun sağ tarafında yer alan aşağı ok tuşu, "Gelişmiş Rapor" seçeneğinin kullanılmasını sağlar. Kullanıcı, "Gelişmiş Rapor" seçeneği ile ekrana gelen tablo üzerinde hesaplama yapabilir. Bu seçenek sayesinde, 13684 satırın üstündeki raporlamaların da tek sayfa üzerinden raporlanması sağlanır. "Rapor" seçeneği Text Dosya, Excel Dosya, VTS Format, HTML kayıt türlerini desteklerken, "Gelişmiş Rapor" seçeneği Excel Workbook, Excel Template, Excel 97-2003 Workbook, Excel 97-2003 Template, Comma Delimited, Text Document, Web Page, XML Document, PDF Document kayıt türlerini destekler. |
| ![](../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Ön Sorgulama, Kısıt ve Sıralama sayfalarında verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Tarih Aralıklı Mizan raporu almak için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki fatura karlılık raporu işleminde kullanılmak üzere saklanır. |
| ![](../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | Tarih Aralıklı Mizan raporu ekranı hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Tarih Aralıklı Mizan raporu almak için verilen kısıtların iptal edildiği butondur. |

**Ölçekleme**

Standart raporlarda miktar, fiyat, tutar, kur, döviz tutarı, döviz fiyatı, firma döviz tutarı ve oran alanları için ölçekleme yapılmasını sağlayan sekmedir.

![](../../../../_assets/b44bd247df5d31c3138f.png)

**Örneğin;**

Fiyat ve tutar alanlarına 1.000 yazılması, fiyat ve tutara getirilecek verilerin 1.000'e bölüneceği anlamına gelir.

**Yazıcı Seçenekleri**

**![](../../../../_assets/50be23d835183ae3a020.png)**

| Tarih Aralıklı Mizan Ekranı |  |
| --- | --- |
| Ekran | Raporun ekrandan alınması için işaretlenmesi gereken seçenektir. Hiçbir değişiklik yapılmaması durumunda, raporda ekran seçeneği işaretli olduğu için, rapor yine ekrandan alınır. |
| Yazıcı | Raporun yazıcıdan alınması için işaretlenmesi gereken seçenektir |
| Toplam Sayfa | Rapor yazıcıya döküldüğü zaman yazıcıdan kaç sayfa çıkarılacağının gösterildiği alandır. Kullanıcı, raporu yazıcıya göndermeden önce bu seçeneği işaretleyerek ![](../../../../_assets/21c20c78203acae9cce6.jpg)butonuna basarsa, yazıcıya dökülecek sayfa adedi ekranda görüntülenir. ![](../../../../_assets/b2e157c1e0713bfefb94.png) |
| Tarih Aralıklı Mizan Ekranı | Yazıcı Seçenekleri - Yönlendirme |
| Dikey | Raporun sadece yazıcı seçeneği ile bastırılması durumunda kullanılan seçenektir. Döküm yapılacak kağıdın genişliğine göre rapor dikey veya yatay olarak alınabilir. Bu seçenekte hiçbir değişiklik yapılmaması durumunda otomatik olarak "Dikey" işaretlenmiş olduğu için rapor dikey şekilde basılır. Ekran seçeneğinde bu parametrenin herhangi bir işlevi yoktur. |
| Yatay | Raporun sadece yazıcı seçeneği ile bastırılması durumunda kullanılan seçenektir. Döküm yapılacak kağıdın genişliğine göre rapor dikey veya yatay olarak alınabilir. Raporun kağıda yatay olarak basılması için işaretlenmesi gereken seçenektir. Ekran seçeneğinde bu parametrenin herhangi bir işlevi yoktur. |
| Tarih Aralıklı Mizan Ekranı | Yazıcı Seçenekleri |
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
