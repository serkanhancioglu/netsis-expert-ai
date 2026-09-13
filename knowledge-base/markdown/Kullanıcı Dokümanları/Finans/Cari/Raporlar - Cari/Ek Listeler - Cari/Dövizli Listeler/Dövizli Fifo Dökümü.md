---
title: "Dövizli Fifo Dökümü"
page_id: "22805684"
product: "netsis-3-enterprise"
depth: 7
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Cari"
  - "Raporlar / Cari"
  - "Ek Listeler / Cari"
  - "Dövizli Listeler"
  - "Dövizli Fifo Dökümü"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Cari / Raporlar / Cari / Ek Listeler / Cari / Dövizli Listeler / Dövizli Fifo Dökümü"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTc1MTA4OTg2LWFhNTMtNDk1MS1hODIwLTI2ZGNlM2U5MDEwNyZsaW5rPWQzYTdhNmM5LTM4OWMtNDljMS1hZTI0LTI0NTAwY2MyNjU5OCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=75108986-aa53-4951-a820-26dce3e90107&link=d3a7a6c9-389c-49c1-ae24-24500cc26598&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "dovizli-fifo-dokumu_29988605_22805684.html"
source_version: "2022-10-31T16:26:02.280+03:00"
source_bytes: 221674
fetched_at: "2026-09-13T04:08:33+00:00"
generator: "netsis-scraper 1.0.0"
---
# Dövizli Fifo Dökümü

Finans Bölümü'nde Raporlar/Cari menüsünün altında yer alır. Dövizli Fifo Dökümü, dövizle çalışan cari hesapların tarih bazında döviz tutarları ve günlük kur ile TL karşılıklarının ilk giren ilk çıkar mantığı ile (FİFO) verildiği rapordur. Dövizli Fifo Dökümü; Ön Sorgulama, Genel Kısıtlar, Kısıt, Sıralama, Ölçekleme ve Yazıcı Seçenekleri sekmelerinden oluşur.

Dövizli Fifo Dökümü raporu alınmadan önce "Ek İşlemler" bölümündeki "Döviz Fifo Maliyet Oluşturma" bölümünün çalıştırılması gerekir.

**Ön Sorgulama**

Dövizli Fifo Dökümü ekranı Ön Sorgulama sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Dövizli Fifo Dökümü Ekranı |  |
| --- | --- |
| Cari Kodu Aralığı | Cariye ait başlangıç ve bitiş kodlarının ![](../../../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu yardımı ile seçilerek, dövizli fifo dökümü için kısıt verilmesini sağlayan alandır. |
| Tip | Dövizli fifo dökümü için tip kısıdının verildiği alandır. Hepsi, Alıcı, Satıcı, Kefil, Toptancı, Müstahsil ve Diğer olmak üzere yedi tip seçenek bulunur. |
| Grup Kodu | Dövizli fifo dökümü için grup kodu kısıdının verildiği alandır. Rehber butonu ![](../../../../../../_assets/088477bb321d1b20c939.jpg) ile grup kodları arasından seçim yapılabilir. |
| Kod-1/2/3/4/5 | Dövizli fifo dökümü için daha önceden tanımlaması yapılan Kod-1/2/3/4/5 kısıdının verildiği alandır. Rehber butonu ![](../../../../../../_assets/088477bb321d1b20c939.jpg) ile kodlar arasından seçim yapılabilir. |
| İl | Dövizli fifo dökümü için il kısıdının verildiği alandır. |
| İlçe | Dövizli fifo dökümü için ilçe kısıdının verildiği alandır. |
| ![](../../../../../../_assets/21c20c78203acae9cce6.jpg) Rapor | Dövizli fifo dökümü için verilen kısıtlara göre Yukarıdaki alanlara girilen bilgiler doğrultusunda, rapor almak için kullanılan butondur. Butonun sağ tarafında yer alan aşağı ok tuşu, "Gelişmiş Rapor" seçeneğinin kullanılmasını sağlar. Kullanıcı, "Gelişmiş Rapor" seçeneği ile ekrana gelen tablo üzerinde hesaplama yapabilir. Bu seçenek sayesinde, 13684 satırın üstündeki raporlamaların da tek sayfa üzerinden raporlanması sağlanır. "Rapor" seçeneği Text Dosya, Excel Dosya, VTS Format, HTML kayıt türlerini desteklerken, "Gelişmiş Rapor" seçeneği Excel Workbook, Excel Template, Excel 97-2003 Workbook, Excel 97-2003 Template, Comma Delimited, Text Document, Web Page, XML Document, PDF Document kayıt türlerini destekler. |
| ![](../../../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Genel Kısıtlar ve Kısıt sayfalarında verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Dövizli fifo dökümü için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki dövizli fifo dökümü işleminde kullanılmak üzere saklanır. |
| ![](../../../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | Dövizli fifo dökümü hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../../../_assets/973111d004995dca0113.jpg) İptal | Dövizli fifo dökümü için verilen kısıtların iptal edildiği butondur. |

**Genel Kısıtlar**

Dövizli Fifo Dökümü ekranı Genel Kısıtlar sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Dövizli Fifo Dökümü Ekranı |  |
| --- | --- |
| Sınır Tarihi | Bu alana girilen tarihe kadar olan tüm hareketler için kısıt verilmesini sağlayan alandır. |
| ![](../../../../../../_assets/21c20c78203acae9cce6.jpg) Rapor | Dövizli fifo dökümü için verilen kısıtlara göre Yukarıdaki alanlara girilen bilgiler doğrultusunda, rapor almak için kullanılan butondur. Butonun sağ tarafında yer alan aşağı ok tuşu, "Gelişmiş Rapor" seçeneğinin kullanılmasını sağlar. Kullanıcı, "Gelişmiş Rapor" seçeneği ile ekrana gelen tablo üzerinde hesaplama yapabilir. Bu seçenek sayesinde, 13684 satırın üstündeki raporlamaların da tek sayfa üzerinden raporlanması sağlanır. "Rapor" seçeneği Text Dosya, Excel Dosya, VTS Format, HTML kayıt türlerini desteklerken, "Gelişmiş Rapor" seçeneği Excel Workbook, Excel Template, Excel 97-2003 Workbook, Excel 97-2003 Template, Comma Delimited, Text Document, Web Page, XML Document, PDF Document kayıt türlerini destekler. |
| ![](../../../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Genel Kısıtlar ve Kısıt sayfalarında verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Dövizli fifo dökümü için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki dövizli fifo dökümü işleminde kullanılmak üzere saklanır. |
| ![](../../../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | Dövizli fifo dökümü hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../../../_assets/973111d004995dca0113.jpg) İptal | Dövizli fifo dökümü için verilen kısıtların iptal edildiği butondur. |

**Kısıt**

Dövizli Fifo Dökümü ekranı Kısıt sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Dövizli Fifo Dökümü Ekranı |  |
| --- | --- |
| Sahalar | Dövizli fifo dökümü için kısıt verilmesi istenen alanlar yer alır. Ekle ![](../../../../../../_assets/b050fee00ab65632b16d.jpg) butonu ile istenen alanlar "kısıt verilecek sahalar" kısmına eklenir. |
| Kısıt Verilecek Sahalar | Dövizli fifo dökümü için kısıt verilen sahaların yer aldığı alandır. Çıkar ![](../../../../../../_assets/a19640feaa753a52d048.jpg) butonu ile istenmeyen alanlar çıkarılır. |
| Eşit, Küçük, Küçük veya Eşit, Büyük, Büyük veya Eşit, Arasında, Benziyor, Eşit Boş, Eşit Değil, İçinde Eşit Değil | **Eşit;** işaretlenen alanda belli bir sabit koşula göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "001" olan stok için liste alınacaksa "Eşit" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "001" girilir. Bu durumda, sadece "001" numaralı Stok Kodu için liste alınır. **Küçük;** işaretlenen alanda belli bir değerden küçük olanlar koşuluna göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "100" olan stok için liste alınacaksa "Küçük" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" girilir. Bu durumda, "100'den küçük" numaralı Stok Kodu için liste alınır. **Küçük veya Eşit:** işaretlenen alanda belli bir değere eşit veya küçük olanlar koşuluna göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "100" olan stok için liste alınacaksa "Küçük veya Eşit" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" girilir. Bu durumda, "100 ve 100'den küçük" numaralı Stok Kodu için liste alınır. **Büyük;** işaretlenen alanda belli bir değerden büyük olanlar koşuluna göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "100" olan stok için liste alınacaksa "Büyük" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" girilir. Bu durumda, "100'den büyük" numaralı Stok Kodu için liste alınır. **Büyük veya Eşit;** işaretlenen alanda belli bir değere eşit veya büyük olanlar koşuluna göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "100" olan stok için liste alınacaksa "Büyük veya Eşit" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" girilir. Bu durumda, "100 ve 100'den büyük" numaralı Stok Kodu için liste alınır. **Arasında;** seçilen alanla ilgili bir aralık tanımlanması istendiğinde kullanılması gereken seçenektir. Eğer belli bir başlangıç ve bitiş değeri arasında kalan değerlerle ilgili kısıt verilecekse kullanılması gereken seçenektir. Örneğin; Stok Kodu kıstasında, "Arasında" seçeneği seçilip \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" ve yine \<tab\> tuşu ile ilerlenerek altta bulunan alana "200" yazıldığı varsayılsın. Böylece stok kodu 100 ile 200 arasındaki stok kodları için liste alınır. **Benziyor;** cari ile ilgili kayıt ararken cari hesabın ismi tam olarak bilinmiyorsa benziyor seçeneği kullanılır. Örneğin; cari hesabın isminin CANEL ya da CENEL olacağı düşünülüyorsa, bu seçeneği seçtikten sonra alanın sağ tarafındaki kayıt alanına "C_NEL" yazıldığında, raporda cari ismi "C" ile başlayan ikinci karakteri herhangi bir karakter olan fakat sonu "NEL" ile biten kayıtlar listelenir. **Eşit Boş;** seçilen sahada hiçbir bilgi olmadığında kullanılan seçenektir. Bu seçenek alfanumerik sahalar için geçerlidir. Sıfırdan büyük veya sıfıra eşit bilgilerin aranması durumunda "Eşit", "Büyük Eşit", "Küçük Eşit" seçenekleri kullanılabilir. **Eşit Değil;** raporda seçilen Eşit, Küçük ve Eşit, Büyük, Büyük ve Eşit, Arasında, Benziyor ve Eşit Boş seçeneklerindeki belirlemeler olumsuz (hariç) anlamını taşıyorsa "Eşit Değil" seçeneği işaretlenir. Örneğin; stok kodunda "Eşit" seçildiğinde ve "0101" kodu girildiği varsayıldığında, "Eşit Değil" seçeneği işaretlendiğinde, raporda stok kodu "0101" olanların haricindeki stokların listeleneceği anlaşılır. |
| İse/Değil ise | **İse;** raporda seçilen Eşit, Küçük ve Eşit, Büyük, Büyük ve Eşit, Arasında ve Benziyor seçeneklerindeki belirlemeler olumlu (dahil) anlamını taşıyorsa "İse" seçeneği işaretlenir. Örneğin; stok kodunda "Eşit" seçildiğinde ve "0101" kodu girildiği varsayıldığında, "İse" seçeneği işaretlenirse, rapora stok kodu "0101" olan stokların dahil edileceği anlaşılır. **Değil İse;** raporda seçilen Eşit, Küçük ve Eşit, Büyük, Büyük ve Eşit, Arasında ve Benziyor seçeneklerindeki belirlemeler olumsuz (hariç) anlamını taşıyorsa "Değil İse" seçeneği işaretlenir. Örneğin; stok kodunda "Eşit" seçildiğinde ve "0101" kodu girildiği varsayıldığında, "Değil İse" seçeneği işaretlendiğinde, raporda stok kodu "0101" olanların haricindeki stokların listeleneceği anlaşılır. |
| Ve/Veya | **Ve;** seçilen sahalarda zorunlu bağlantı koşulu sağlar. **Örnek 1:** Karmaşık bir stok kodlaması olduğu varsayıldığında; Bu kodlardan iki tanesinin raporda çıkması isteniyor fakat bu iki stok kodunun ortak hiçbir özelliği yok. Bu durumda, "Stok Kodu" sahası iki kez kısıt verilecek sahalar bölümüne aktarılır. 1.Stok Kodu kıstasında eşit bağlantısı kurularak ilk stok kodu girilir ve "VE" bağlacı işaretlenir. Daha sonra 2. Stok Kodu seçilerek yine eşit bağlantısı ile diğer bir stok kodu yazılır. Böylece, raporda sadece bu iki stok koduna ait bilgi alınır. Bu seçenekte tanımlanan her koşulun olması zorunludur. Yani, tanımlanan iki stok kodundan biri bile mevcut değil ise, rapor bilgi vermez. **Örnek 2:** Grup kodu 1, Kod 1 alanı 2 ve Kod 2 alanı 3 olan stoklarla ilgili bir liste alınması istendiğinde; Verilen tanımlamalarda "VE" bağlacı kullanılırsa, mutlaka bu üç kısıta da sahip olan stoklar aranır ve bulunursa listelenir. Üç kısıttan herhangi birine sahip olmayan stoklar raporda listelenmez. **Veya;** seçilen sahalarda olabilirlik koşulu sağlar. Yani, tanımlanan koşullardan biri bile sağlansa ilgili raporla ilgili bilgi alınabilir. **Örnek 1:** Grup kodu 1, Kod 1 alanı 2 ve Kod 2 alanı 3 olan stoklarla ilgili bir liste alınması istendiğinde; verilen tanımlamalarda "VEYA" bağlacı kullanılırsa, bu üç kısıttan birine bile sahip olan stoklar aranır ve bulunursa listelenir. |
| ![](../../../../../../_assets/c7275efbddc154ea1579.jpg) Kaydet | Yapılan tanımlamaların onaylanması için kullanılan butondur. |
| ![](../../../../../../_assets/df428ea63894bc744f9a.jpg) İptal | Yapılan tanımlamaların iptal edilmesi için kullanılan butondur. |
| ![](../../../../../../_assets/21c20c78203acae9cce6.jpg) Rapor | Dövizli fifo dökümü için verilen kısıtlara göre Yukarıdaki alanlara girilen bilgiler doğrultusunda, rapor almak için kullanılan butondur. Butonun sağ tarafında yer alan aşağı ok tuşu, "Gelişmiş Rapor" seçeneğinin kullanılmasını sağlar. Kullanıcı, "Gelişmiş Rapor" seçeneği ile ekrana gelen tablo üzerinde hesaplama yapabilir. Bu seçenek sayesinde, 13684 satırın üstündeki raporlamaların da tek sayfa üzerinden raporlanması sağlanır. "Rapor" seçeneği Text Dosya, Excel Dosya, VTS Format, HTML kayıt türlerini desteklerken, "Gelişmiş Rapor" seçeneği Excel Workbook, Excel Template, Excel 97-2003 Workbook, Excel 97-2003 Template, Comma Delimited, Text Document, Web Page, XML Document, PDF Document kayıt türlerini destekler. |
| ![](../../../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Genel Kısıtlar ve Kısıt sayfalarında verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Dövizli fifo dökümü için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki dövizli fifo dökümü işleminde kullanılmak üzere saklanır. |
| ![](../../../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | Dövizli fifo dökümü hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../../../_assets/973111d004995dca0113.jpg) İptal | Dövizli fifo dökümü için verilen kısıtların iptal edildiği butondur. |

**Sıralama**

Dövizli Fifo Dökümü ekranı Sıralama sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Dövizli Fifo Dökümü Ekranı |  |
| --- | --- |
| Sahalar | Dövizli fifo dökümü için sıralanması istenen alanlar yer alır. Ekle ![](../../../../../../_assets/b050fee00ab65632b16d.jpg) butonu ile istenen alanlar "sıralama sahaları" kısmına eklenir. |
| Sıralama Sahaları | Dövizli fifo dökümü için sıralama yapılacak sahaların yer aldığı alandır. Çıkar ![](../../../../../../_assets/a19640feaa753a52d048.jpg) butonu ile istenmeyen alanlar çıkarılır. |
| Sıralama | Sıralamanın ne şekilde yapılacağının belirlendiği alandır. Artan ve Azalan olmak üzere iki seçenekten oluşur. **Artan:** Artan seçeneğin işaretlenmesi halinde, bilgiler küçükten büyüğe sıralı şekilde listelenir. **Azalan:** Azalan seçeneğinin işaretlenmesi halinde, bilgiler büyükten küçüğe sıralı şekilde listelenir. |
| Değişimde Toplam | Bu alan işaretlendiğinde, sıralanan bilgi her değiştiğinde ara toplam alınır. |
| Birinci Saha Değ. Baş. Saha | "Değişimde Toplam" seçeneği işaretlendiğinde, sıralanan bilgi her değiştiğinde ara toplam alınır. Bu durumda raporda, sıralı alanın içerdiği bilginin aynı kaldığı kayıt grubu için, sıralı alanın değeri başlık olarak yazılır. Başlıkların daha anlamlı olması açısından, başlık olarak sıralı alan bilgisinden daha farklı bir bilginin yazılması sağlanır. Örneğin; Sıralı Saha-1’de (grup koduna göre sıralatılan bir raporda), eğer grup kodlarının isimleri tanımlı ise (Grup Kodu Girişi bölümünden tanımlanmış ise) sıralama grup koduna göre yapılmasına rağmen, başlık olarak **grup kodu bilgisi** yerine, **grup ismi bilgisi** yazılır. Böylece grup kodlarına yabancı olan ya da bilmeyen bir kullanıcı için, raporun daha anlaşılır olması sağlanır. |
| ![](../../../../../../_assets/c7275efbddc154ea1579.jpg) Kaydet | Yapılan tanımlamaların onaylanması için kullanılan butondur. |
| ![](../../../../../../_assets/df428ea63894bc744f9a.jpg) İptal | Yapılan tanımlamaların iptal edilmesi için kullanılan butondur. |
| Kırılımda Kayıt Sayısı | "Değişimde Toplam" alanının işaretlendiği durumlarda, her ara toplam için listelenen satır kayıt sayısının alınmasını sağlayan seçenektir. |
| Kümüle Döküm | Raporda dökülecek bilgilerin toplam olarak tek kalemde görüntülenmesi istendiğinde işaretlenmesi gereken seçenektir. Sıralama alanlarında tanımlanan en son sahada kümülasyon yapılır. **Örneğin:** Stok hareket kayıtları ile ilgili bir rapor alındığında, "Kümüle Döküm" seçeneği işaretlenmezse o stoka ait kayıtlar hareket bazında satır satır listelenir. "Kümüle Döküm" seçeneği işaretlenirse, her bir stok koduna ait hareketler kümüle olarak tek satırda toplanır ve o şekilde listelenir. |
| ![](../../../../../../_assets/21c20c78203acae9cce6.jpg) Rapor | Dövizli fifo dökümü için verilen kısıtlara göre Yukarıdaki alanlara girilen bilgiler doğrultusunda, rapor almak için kullanılan butondur. Butonun sağ tarafında yer alan aşağı ok tuşu, "Gelişmiş Rapor" seçeneğinin kullanılmasını sağlar. Kullanıcı, "Gelişmiş Rapor" seçeneği ile ekrana gelen tablo üzerinde hesaplama yapabilir. Bu seçenek sayesinde, 13684 satırın üstündeki raporlamaların da tek sayfa üzerinden raporlanması sağlanır. "Rapor" seçeneği Text Dosya, Excel Dosya, VTS Format, HTML kayıt türlerini desteklerken, "Gelişmiş Rapor" seçeneği Excel Workbook, Excel Template, Excel 97-2003 Workbook, Excel 97-2003 Template, Comma Delimited, Text Document, Web Page, XML Document, PDF Document kayıt türlerini destekler. |
| ![](../../../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Genel Kısıtlar ve Kısıt sayfalarında verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Dövizli fifo dökümü için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki dövizli fifo dökümü işleminde kullanılmak üzere saklanır. |
| ![](../../../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | Dövizli fifo dökümü hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../../../_assets/973111d004995dca0113.jpg) İptal | Dövizli fifo dökümü için verilen kısıtların iptal edildiği butondur. |

**Ölçekleme**

Standart raporlarda miktar, fiyat, tutar, kur, döviz tutarı, döviz fiyatı, firma döviz tutarı ve oran alanları için ölçekleme yapılmasını sağlayan sekmedir.

**Örneğin:** Fiyat ve tutar alanlarına 1.000 yazılması, fiyat ve tutara getirilecek verilerin 1.000'e bölüneceği anlamına gelir.

**Yazıcı Seçenekleri**

Dövizli Fifo Dökümü ekranı Yazıcı Seçenekleri sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Dövizli Fifo Dökümü Ekranı |  |
| --- | --- |
| Ekran | Raporun ekrandan alınması için işaretlenmesi gereken seçenektir. Hiçbir değişiklik yapılmaması durumunda, raporda ekran seçeneği işaretli olduğu için, rapor yine ekrandan alınır. |
| Yazıcı | Raporun yazıcıdan alınması için işaretlenmesi gereken seçenektir |
| Toplam Sayfa | Rapor yazıcıya döküldüğü zaman yazıcıdan kaç sayfa çıkarılacağının gösterildiği alandır. Kullanıcı, raporu yazıcıya göndermeden önce bu seçeneği işaretleyerek Rapor ![](../../../../../../_assets/21c20c78203acae9cce6.jpg)butonuna basarsa, yazıcıya dökülecek sayfa adedi ekranda görüntülenir. ![](../../../../../../_assets/b2e157c1e0713bfefb94.png) |
| Yazıcı Seçenekleri - Yönlendirme |  |
| Dikey | Raporun sadece yazıcı seçeneği ile bastırılması durumunda kullanılan seçenektir. Döküm yapılacak kağıdın genişliğine göre rapor dikey veya yatay olarak alınabilir. Bu seçenekte hiçbir değişiklik yapılmaması durumunda otomatik olarak "Dikey" işaretlenmiş olduğu için rapor dikey şekilde basılır. Ekran seçeneğinde bu parametrenin herhangi bir işlevi yoktur. |
| Yatay | Raporun sadece yazıcı seçeneği ile bastırılması durumunda kullanılan seçenektir. Döküm yapılacak kağıdın genişliğine göre rapor dikey veya yatay olarak alınabilir. Raporun kağıda yatay olarak basılması için işaretlenmesi gereken seçenektir. Ekran seçeneğinde bu parametrenin herhangi bir işlevi yoktur. |
| Yazıcı Seçenekleri |  |
| Şirket Adı | Basılsın, Basılmasın ve Detaylı Basılsın olmak üzere üç seçenekten oluşur. Yazıcıdan alınacak raporun her bir sayfasında şirket unvanının yazılması istendiğinde "Basılsın" seçeneğinin kullanılması gerekir. Şirket unvanı Yardımcı Programlar/Şirket/Şube Parametre Tanımları menüsünde tanımlandığı şekilde otomatik olarak ekrana gelir. |
| Başlık Yazılsın | Yazıcıdan alınacak raporun her bir sayfasında, tanımlanan liste başlığının yazılması istendiğinde işaretlenmesi gereken seçenektir. |
| Tarih/Saat Yazılsın | Yazıcıdan alınacak raporun her bir sayfasında sistem tarihi ve saatinin yazılması istendiğinde işaretlenmesi gereken seçenektir. |
| Sayfa No Basılsın | Yazıcıdan alınacak raporun her bir sayfasında sayfa numarasının yazılması istendiğinde işaretlenmesi gereken seçenektir. |
| Taslak Basım | Birden fazla alanın yer aldığı raporlarda, yazıcıdan çıktı alırken kağıttan taşma sorununun çözülmesi ve raporların istenilen formatta ayarlanması için, "Taslak Basım Ayarları" bölümü kullanılır. Taslak basım ayarları her rapor için bir kez yapılır ve saklanır. Böylece, yazıcıdan çıktı alırken tekrar ayarlama yapmaya gerek kalmadan basım yapılır. Raporun "Taslak Basım Ayarlarında" kaydedilmiş formata göre dökülmesi istendiğinde "Taslak Basım" ve "Saklanmış" seçeneklerinin işaretlenmesi gerekir. Basım Dot Matrix (iğne vuruşlu yazıcı) türü bir yazıcıdan alınacaksa, basım ayarları yapılmasa da "Taslak Basım" seçeneğinin işaretlenmesi gerekir. |
| Saklanmış | Raporun "Taslak Basım Ayarlarında" kaydedilmiş formata göre dökülmesi istendiğinde "Taslak Basım" ve "Saklanmış" seçeneklerinin işaretlenmesi gerekir. |
| Perfore Satır Sayısı | Yazıcıya gönderilecek raporun kaç satırlık kağıda basılacağının belirlendiği alandır. 33’lük ya da 66’lık olabilir. Rapor yazıcıya dökülürken kaç satırdan sonra yeni kağıda geçileceği buradaki tanımlamaya göre belirlenir. Standart olarak 66 seçeneği ekrana gelir fakat kullanıcı isterse değişiklik yapabilir. |
| Yazıcı Ayarı Yapılsın | Seçenek işaretlendiğinde, Windows’un “Yazıcı Ayarları” ekrana gelir. Bu ekranda, tanımlı olan yazıcılar arasından seçim yapılır. Rapor ekrandan alındıktan sonra yazıcıya gönderildiği zaman, tanımlanmış olan yazıcı ayarlarına göre basım yapılır. |
| Nüsha Sayısı | Yazıcıdan alınacak dökümlerde, her sayfadan kaç adet basılacağının belirlendiği alandır. |
| Sıfır Basma | Raporda "sıfır" sayısının görüntülenmesinin istenmediği durumlarda işaretlenmesi gereken alandır. Listelenen kayıtlarda sıfır (0) değerini taşıyan alanlar boş olarak izlenir. |
| Excel Dosya Adı | Ekran ya da yazıcıdan alınacak raporun diske "Excel" formatında bir dosya halinde atılması istendiğinde işaretlenmesi gereken seçenektir. Bu alanda dosyanın hangi dizinde ve hangi isimle oluşturulacağının belirtilmesi gerekir. Excel’in File/Open seçeneği ile Excel'de dosya izlenebilir. |
| Text Dosya Adı | Ekran ya da yazıcıdan alınacak raporun diske "Text" formatında bir dosya halinde atılması istendiğinde işaretlenmesi gereken seçenektir. Bu alanda dosyanın hangi dizinde ve hangi isimle oluşturulacağının belirtilmesi gerekir. Bu dosyaya herhangi bir editör program kullanılarak erişilebilir. |
| HTML Dosya Adı | Ekran ya da yazıcıdan alınacak raporun diske "Html" formatında bir dosya halinde atılması istendiğinde işaretlenmesi gereken seçenektir. Bu alanda dosyanın hangi dizinde ve hangi isimle oluşturulacağının belirtilmesi gerekir. Bu bölümden Excel, Text veya Html formatında oluşturulacak dosyanın doğru ve eksiksiz oluşturulması için tanımlamalar yapıldıktan sonra, raporun tamamının yazıcı ya da ekrandan alınması gerekir. |
| Başlık | Yazıcı ya da ekran dökümleri için rapora genel başlık tanımlanan alandır. "Modül Standart Raporlarında" başlıklar otomatik olarak tanımlı gelir. İstendiğinde bu alandan değiştirilebilir. |
| ![](../../../../../../_assets/21c20c78203acae9cce6.jpg) Rapor | Dövizli fifo dökümü için verilen kısıtlara göre Yukarıdaki alanlara girilen bilgiler doğrultusunda, rapor almak için kullanılan butondur. Butonun sağ tarafında yer alan aşağı ok tuşu, "Gelişmiş Rapor" seçeneğinin kullanılmasını sağlar. Kullanıcı, "Gelişmiş Rapor" seçeneği ile ekrana gelen tablo üzerinde hesaplama yapabilir. Bu seçenek sayesinde, 13684 satırın üstündeki raporlamaların da tek sayfa üzerinden raporlanması sağlanır. "Rapor" seçeneği Text Dosya, Excel Dosya, VTS Format, HTML kayıt türlerini desteklerken, "Gelişmiş Rapor" seçeneği Excel Workbook, Excel Template, Excel 97-2003 Workbook, Excel 97-2003 Template, Comma Delimited, Text Document, Web Page, XML Document, PDF Document kayıt türlerini destekler. |
| ![](../../../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Genel Kısıtlar ve Kısıt sayfalarında verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Dövizli fifo dökümü için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki dövizli fifo dökümü işleminde kullanılmak üzere saklanır. |
| ![](../../../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | Dövizli fifo dökümü hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../../../_assets/973111d004995dca0113.jpg) İptal | Dövizli fifo dökümü için verilen kısıtların iptal edildiği butondur. |
