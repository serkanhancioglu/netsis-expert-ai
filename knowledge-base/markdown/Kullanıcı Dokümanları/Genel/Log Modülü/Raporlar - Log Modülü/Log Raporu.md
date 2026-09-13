---
title: "Log Raporu"
page_id: "24753643"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Genel"
  - "Log Modülü"
  - "Raporlar / Log Modülü"
  - "Log Raporu"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Log Modülü / Raporlar / Log Modülü / Log Raporu"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTMwMDBlNDY4LTNiM2QtNGRkYi04NDU4LTc3YzYxZjE4YjA5OSZsaW5rPTk0NzFhZGY0LWIyNzctNGFkNy1iZGM4LTAzZTI1OTg0Zjg0NCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=3000e468-3b3d-4ddb-8458-77c61f18b099&link=9471adf4-b277-4ad7-bdc8-03e25984f844&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "log-raporu_41169733_24753643.html"
source_version: "2022-09-16T15:26:35.080+03:00"
source_bytes: 368607
fetched_at: "2026-09-13T04:18:29+00:00"
generator: "netsis-scraper 1.0.0"
---
# Log Raporu

Log Raporu; Genel Bölümü'nde, "Raporlar/Log Modülü" menüsünün altında yer alır. Log Raporu ekranı; Ön Sorgulama, Kısıt, Sıralama ve Ölçekleme sekmelerinden oluşur.

**Ön Sorgulama**

![](../../../../_assets/fa4a90eb33ad52f8b58c.png)

Log Raporu Ön Sorgulama sekmesinde yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| Log Raporu Ekranı |  |
| --- | --- |
| Başlangıç Tarihi | Log raporu için başlangıç tarih kısıdı verilen alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile takvim kullanılarak tarih seçimi yapılabilir. Tarih alanının sağ tarafında yer alan kısım saat belirtmek için kullanılır. |
| Bitiş Tarihi | Log raporu için bitiş tarih kısıdı verilen alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile takvim kullanılarak tarih seçimi yapılabilir. Tarih alanının sağ tarafında yer alan kısım saat belirtmek için kullanılır. |
| Kullanıcı İsim | Hangi kullanıcıya ait bilgilerin alınacağını belirleyen alandır. Boş bırakılması halinde tüm Netsis kullanıcılarının log edilmiş bilgilerini listeler. |
| Login Adı | Çalışılan herhangi bir makineye bağlanılan login ismine ait bilgilerin alınmasını belirleyen alandır. |
| Modül ve Program | Netsis sisteminde modüllerin ve modül içindeki menü seçeneklerinin birer numarası bulunur. Log kayıtları yapılırken, hangi modülün hangi seçeneğinden yapıldığına dair, modül ve program numarası da kaydedilir. Listelenmesi istenen bir modüle ya da modül içindeki menü seçeneğine ait kayıtlar varsa, "Modül" ve "Program" alanlarından numaralar belirlenebilir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, modül ve modüle bağlı program seçimi yapılır. Modül ve Program Numaraları, "Kullanıcı İşlemleri" modülünden izlenebilir. |
| Anahtar Saha 1,2,3,4,5,6 | "Modül" ve "Program" alanlarında yapılan seçime göre anahtar saha alanları kullanılır. Örneğin; Modül alanında "Fatura", Program alanında "Satış Faturası" seçildiğinde, **"Belge No"** Anahtar Sahası olarak görüntülenerek, belge numarası için de kısıt verilmesi sağlanır. |
| İşlem Tipi | Log sisteminde tanımlı beş temel işlem vardır. Bunlar; Kayıt, Düzeltme, İptal, Operasyon ve Hepsi seçenekleridir. Alanın sağ tarafında yer alan aşağı ok butonu ile işlem tipleri arasından seçim yapılır. Log raporu almak için işlem tipi kısıdının verilmesini sağlar. |
| Menü Başlık | Raporda kullanılması istenen menü başlığının seçildiği alandır. Boş bırakıldığında tüm menülerin log bilgilerine ulaşılır. Örneğin;"Cari Hesap Kayıtları" gibi bir kısıt verilebilir. "Menü Başlık" alanının sağ tarafında yer alan Üç Nokta ![](../../../../_assets/5098b020c5e814c92501.png) butonu ile, "Menü Başlık" ekranı görüntülenir. ![](../../../../_assets/141e480a6763118cee64.png) "Menü Başlık" ekranından, farenin sol tuşu ile istenen menü başlığına tıklanarak seçim yapılır. Hepsini Seç ![](../../../../_assets/38b31798a0012cc13233.jpg) butonu, başlıkların hepsinin seçilmesini, Seçimleri Kaldır ![](../../../../_assets/9f77dcdb92897fa07bf9.png) butonu ise işaretli başlık seçimlerinin kaldırılmasını sağlar. Tamam ![](../../../../_assets/39d77b8716226638d9ce.jpg) butonu ile seçimler kaydedilir. İptal ![](../../../../_assets/973111d004995dca0113.jpg) butonu, seçimlerden vazgeçilerek ekranın kapatılmasını sağlar. |
| Dosya Adı | Programda hangi "Tablo" ismine ait kayıtların raporu alınacaksa ilgili tablo adının girilmesi gerekir. Örneğin;**TBLCASABIT** gibi bir kısıt verilebilir. "Dosya Adı" alanının sağ tarafında yer alan Üç Nokta ![](../../../../_assets/5098b020c5e814c92501.png) butonu ile, "Dosya Adı" ekranı görüntülenir. ![](../../../../_assets/3a7d1a78e41b93ca1025.png) "Dosya Adı" ekranından, farenin sol tuşu ile istenen menü başlığına tıklanarak seçim yapılır. Hepsini Seç ![](../../../../_assets/38b31798a0012cc13233.jpg) butonu, başlıkların hepsinin seçilmesini, Seçimleri Kaldır ![](../../../../_assets/9f77dcdb92897fa07bf9.png) butonu ise işaretli başlık seçimlerinin kaldırılmasını sağlar. Tamam ![](../../../../_assets/39d77b8716226638d9ce.jpg) butonu ile seçimler kaydedilir. İptal ![](../../../../_assets/973111d004995dca0113.jpg) butonu, seçimlerden vazgeçilerek ekranın kapatılmasını sağlar. |
| Açıklama | Log edilen kayıtların kayıt içeriklerinin tutulduğu, değişken bölüm içinde bulunan bilgilere ait kriterin tanımlandığı alandır. Örneğin; İncelenmesi istenen log kayıtları için bir belge numarasının olduğu varsayıldığında; "Açıklama" alanına numara girilerek, o belgeye ait tüm log kayıtları listelenebilir. Girilen numara bilgisi ile; kaydın herhangi bir sahasında var olan, belge üst (başlık) bilgileri, cari hareket, stok hareket, muhasebe entegrasyon gibi Log edilmiş olan tüm kayıtlar listelenir. Burada tutulan kolonun formatı XML oldugu için, sadece belli bir sahada geçen bir bilgi de aranabilir. Örneğin; Stok sabit tablosunda Stok Kodu 0014 olan kaydın loglarının gösterilmesi için; **\<stok_kodu\>0014** yazılabilir. |
| Program Adı | İlgili modülün program dosyasına kısıt verilmesi için kullanılan alandır. Örneğin; Fatura.Dll şeklinde bir kısıt verilebilir. |
| Detay Bilgi Basılsın | Detay bilgi istenmediği zaman, Log kayıtlarının sabit bilgileri (Kullanıcı İsmi, Modül No, Program No, Menü Seçeneği gibi) listelenir. Detay bilgi istendiği zaman ise, her log kaydı için iki satır bilgi listelenir. 2. satırda log edilen kaydın içeriğinde yer alan değişken bilgiler listelenir. Log edilen kayıt, operasyon tipli ise, operasyona ait bir açıklama bilgisi verilir. Genelde bu bilgi operasyonun aşamalarını belgeleyen (işleme başlandı, işlem bitti) ifadelerden oluşur. Log raporunun "Operasyon" alanında; Artı tuşu ![(plus)](../../../../_assets/8bc1079dc378a6219e99.svg) Yeni kayıt, Doğrulama (Tik) tuşu ![(tick)](../../../../_assets/72b3afd8b2fe319fbd82.svg) Düzeltilmiş kayıt, Çarpı tuşu ![(error)](../../../../_assets/1ba848ff48d1f78bde03.svg) İptal edilmiş kayıt anlamına gelir. Eğer operasyon alanında hiç bir işaret yoksa, ilgili kaydın rapor, hata ya da operasyon kaydı olduğu anlamına gelir. Yani, Log raporu Html formatında bir rapordur. |
| Rapor Gösterim Tipi | Rapor gösterim tipinin seçildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile, Grid (Tarihler Satırda) veya Html seçenekleri arasından seçim yapılır. Rapor gösterim tipi olarak "Grid (Tarihler Sütunda)" seçeneğinin seçilmesi, değişim olan her tablo için değişiklik tarihinin sütunda gösterilmesini sağlar. Hangi tarihte ne değişiklik yapıldığı, kırmızı ile işaretlenerek kullanıcıya gösterilir. |
| Sayfa Başına Satır Sayısı | Sayfa başına ayarlanacak satır sayısının girildiği alandır. |
| ![](../../../../_assets/7ba39f9046a578093326.png) Rapor | Yukarıdaki alanlara girilen bilgiler doğrultusunda, rapor almak için kullanılan butondur. Butonun sağ tarafında yer alan aşağı ok tuşu, "Gelişmiş Rapor" seçeneğinin kullanılmasını sağlar. Kullanıcı, "Gelişmiş Rapor" seçeneği ile ekrana gelen tablo üzerinde hesaplama yapabilir. Bu seçenek sayesinde, 13684 satırın üstündeki raporlamaların da tek sayfa üzerinden raporlanması sağlanır. "Rapor" seçeneği Text Dosya, Excel Dosya, VTS Format, HTML kayıt türlerini desteklerken, "Gelişmiş Rapor" seçeneği Excel Workbook, Excel Template, Excel 97-2003 Workbook, Excel 97-2003 Template, Comma Delimited, Text Document, Web Page, XML Document, PDF Document kayıt türlerini destekler. |
| ![](../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Ön Sorgulama sekmesinde verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Log raporu almak için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki Log raporu alma işleminde kullanılmak üzere saklanır. |
| ![](../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | Log raporu ekranı hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Log raporu almak için verilen kısıtların iptal edildiği butondur. |

**Kısıt**

**![](../../../../_assets/d3d8a554060c777436e7.png)**

| Log Raporu Ekranı |  |
| --- | --- |
| Sahalar | Log raporu almak için kısıt verilmesi istenen alanlar yer alır. ![](../../../../_assets/b050fee00ab65632b16d.jpg) butonu ile istenen alanlar "kısıt verilecek sahalar" kısmına eklenir. |
| Kısıt Verilecek Sahalar | Log raporu almak için kısıt verilen sahaların yer aldığı alandır. ![](../../../../_assets/a19640feaa753a52d048.jpg) butonu ile istenmeyen alanlar çıkarılır. |
| Eşit, Küçük, Küçük veya Eşit, Büyük, Büyük veya Eşit, Arasında, Benziyor, Eşit Boş, Eşit Değil, İçinde Eşit Değil | **Eşit;** İşaretlenen alanda belli bir sabit koşula göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "001" olan stok için liste alınacaksa "Eşit" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "001" girilir. Bu durumda, sadece "001" numaralı Stok Kodu için liste alınır. **Küçük;** İşaretlenen alanda belli bir değerden küçük olanlar koşuluna göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "100" olan stok için liste alınacaksa "Küçük" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" girilir. Bu durumda, "100'den küçük" numaralı Stok Kodu için liste alınır. **Küçük veya Eşit;** İşaretlenen alanda belli bir değere eşit veya küçük olanlar koşuluna göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "100" olan stok için liste alınacaksa "Küçük veya Eşit" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" girilir. Bu durumda, "100 ve 100'den küçük" numaralı Stok Kodu için liste alınır. **Büyük;** İşaretlenen alanda belli bir değerden büyük olanlar koşuluna göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "100" olan stok için liste alınacaksa "Büyük" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" girilir. Bu durumda, "100'den büyük" numaralı Stok Kodu için liste alınır. **Büyük veya Eşit;** İşaretlenen alanda belli bir değere eşit veya büyük olanlar koşuluna göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "100" olan stok için liste alınacaksa "Büyük veya Eşit" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" girilir. Bu durumda, "100 ve 100'den büyük" numaralı Stok Kodu için liste alınır. **Arasında;** Seçilen alanla ilgili bir aralık tanımlanması istendiğinde kullanılması gereken seçenektir. Eğer belli bir başlangıç ve bitiş değeri arasında kalan değerlerle ilgili kısıt verilecekse kullanılması gereken seçenektir. Örneğin; Stok Kodu kıstasında, "Arasında" seçeneği seçilip \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" ve yine \<tab\> tuşu ile ilerlenerek altta bulunan alana "200" yazıldığı varsayılsın. Böylece stok kodu 100 ile 200 arasındaki stok kodları için liste alınır. **Benziyor;** Cari ile ilgili kayıt ararken cari hesabın ismi tam olarak bilinmiyorsa benziyor seçeneği kullanılır. Örneğin; cari hesabın isminin CANEL ya da CENEL olacağı düşünülüyorsa, buseçeneği seçtikten sonra alanın sağ tarafındaki kayıt alanına "C_NEL" yazıldığında, raporda cari ismi "C" ile başlayan ikinci karakteri herhangi bir karakter olan fakat sonu "NEL" ile biten kayıtlar listelenir. **Eşit Boş;** **Eşit Değil;** |
| İse / Değil ise | **İse;** Raporda seçilen Eşit, Küçük ve Eşit, Büyük, Büyük ve Eşit, Arasında ve Benziyor seçeneklerindeki belirlemeler olumlu (dahil) anlamını taşıyorsa "İse" seçeneği işaretlenir. Örneğin; stok kodunda "Eşit" seçildiğinde ve "0101" kodu girildiği varsayıldığında, "İse" seçeneği işaretlenirse, rapora stok kodu "0101" olan stokların dahil edileceği anlaşılır. **Değil İse;** Raporda seçilen Eşit, Küçük ve Eşit, Büyük, Büyük ve Eşit, Arasında ve Benziyor seçeneklerindeki belirlemeler olumsuz (hariç) anlamını taşıyorsa "Değil İse" seçeneği işaretlenir. Örneğin; stok kodunda "Eşit" seçildiğinde ve "0101" kodu girildiği varsayıldığında, "Değil İse" seçeneği işaretlendiğinde, raporda stok kodu "0101" olanların haricindeki stokların listeleneceği anlaşılır. |
| ![](../../../../_assets/c7275efbddc154ea1579.jpg) | Yapılan tanımlamaların onaylanması için kullanılan butondur. |
| ![](../../../../_assets/df428ea63894bc744f9a.jpg) | Yapılan tanımlamaların iptal edilmesi için kullanılan butondur. |
| ![](../../../../_assets/7ba39f9046a578093326.png) | Yukarıdaki alanlara girilen bilgiler doğrultusunda, rapor almak için kullanılan butondur. Butonun sağ tarafında yer alan aşağı ok tuşu, "Gelişmiş Rapor" seçeneğinin kullanılmasını sağlar. Kullanıcı, "Gelişmiş Rapor" seçeneği ile ekrana gelen tablo üzerinde hesaplama yapabilir. Bu seçenek sayesinde, 13684 satırın üstündeki raporlamaların da tek sayfa üzerinden raporlanması sağlanır. "Rapor" seçeneği Text Dosya, Excel Dosya, VTS Format, HTML kayıt türlerini desteklerken, "Gelişmiş Rapor" seçeneği Excel Workbook, Excel Template, Excel 97-2003 Workbook, Excel 97-2003 Template, Comma Delimited, Text Document, Web Page, XML Document, PDF Document kayıt türlerini destekler. |
| ![](../../../../_assets/e3223333470668512f5f.jpg) | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) | Ön Sorgulama sekmesinde verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Log raporu almak için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki Log raporu alma işleminde kullanılmak üzere saklanır. |
| ![](../../../../_assets/4ad6cc61ca2c42a19c85.jpg) | Log raporu ekranı hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) | Log raporu almak için verilen kısıtların iptal edildiği butondur. |

**Sıralama**

**![](../../../../_assets/9c85c4eb54067d9f62c1.png)**

| Log Raporu Ekranı |  |
| --- | --- |
| Sahalar | Log raporu almak için kısıt verilirken sıralanması istenen alanlar yer alır. ![](../../../../_assets/b050fee00ab65632b16d.jpg) butonu ile istenen alanlar "sıralama sahaları" kısmına eklenir. |
| Sıralama Sahaları | Log raporu almak için kısıt verilirken sıralama yapılacak sahaların yer aldığı alandır. ![](../../../../_assets/a19640feaa753a52d048.jpg) butonu ile istenmeyen alanlar çıkarılır. |
| Sıralama | Sıralamanın ne şekilde yapılacağının belirlendiği alandır. Artan ve Azalan olmak üzere iki seçenekten oluşur. **Artan;** Artan seçeneğin işaretlenmesi halinde, bilgiler küçükten büyüğe sıralı şekilde listelenir. **Azalan;** Azalan seçeneğinin işaretlenmesi halinde, bilgiler büyükten küçüğe sıralı şekilde listelenir. |
| Değişimde Toplam | Bu alan işaretlendiğinde, sıralanan bilgi her değiştiğinde ara toplam alınır. |
| Birinci Saha Değ. Baş. Saha | "Değişimde Toplam" seçeneği işaretlendiğinde, sıralanan bilgi her değiştiğinde ara toplam alınır. Bu durumda raporda, sıralı alanın içerdiği bilginin aynı kaldığı kayıt grubu için, sıralı alanın değeri başlık olarak yazılır. Başlıkların daha anlamlı olması açısından, başlık olarak sıralı alan bilgisinden daha farklı bir bilginin yazılması sağlanır. Örneğin; Sıralı Saha - 1’de (grup koduna göre sıralatılan bir raporda), eğer grup kodlarının isimleri tanımlı ise (Grup Kodu Girişi bölümünden tanımlanmış ise) sıralama grup koduna göre yapılmasına rağmen, başlık olarak **grup kodu bilgisi** yerine, **grup ismi bilgisi** yazılır. Böylece grup kodlarına yabancı olan ya da bilmeyen bir kullanıcı için, raporun daha anlaşılır olması sağlanır. |
| ![](../../../../_assets/c7275efbddc154ea1579.jpg) | Yapılan tanımlamaların onaylanması için kullanılan butondur. |
| ![](../../../../_assets/df428ea63894bc744f9a.jpg) | Yapılan tanımlamaların iptal edilmesi için kullanılan butondur. |
| Kırılımda Kayıt Sayısı | "Değişimde Toplam" alanının işaretlendiği durumlarda, her ara toplam için listelenen satır kayıt sayısının alınmasını sağlayan seçenektir. |
| Kümüle Döküm | Raporda dökülecek bilgilerin toplam olarak tek kalemde görüntülenmesi istendiğinde işaretlenmesi gereken seçenektir. Sıralama alanlarında tanımlanan en son sahada kümülasyon yapılır. **Örneğin;** Stok hareket kayıtları ile ilgili bir rapor alındığında, "Kümüle Döküm" seçeneği işaretlenmezse o stoka ait kayıtlar hareket bazında satır satır listelenir. "Kümüle Döküm" seçeneği işaretlenirse, her bir stok koduna ait hareketler kümüle olarak tek satırda toplanır ve o şekilde listelenir. |
| ![](../../../../_assets/7ba39f9046a578093326.png) | Yukarıdaki alanlara girilen bilgiler doğrultusunda, rapor almak için kullanılan butondur. Butonun sağ tarafında yer alan aşağı ok tuşu, "Gelişmiş Rapor" seçeneğinin kullanılmasını sağlar. Kullanıcı, "Gelişmiş Rapor" seçeneği ile ekrana gelen tablo üzerinde hesaplama yapabilir. Bu seçenek sayesinde, 13684 satırın üstündeki raporlamaların da tek sayfa üzerinden raporlanması sağlanır. "Rapor" seçeneği Text Dosya, Excel Dosya, VTS Format, HTML kayıt türlerini desteklerken, "Gelişmiş Rapor" seçeneği Excel Workbook, Excel Template, Excel 97-2003 Workbook, Excel 97-2003 Template, Comma Delimited, Text Document, Web Page, XML Document, PDF Document kayıt türlerini destekler. |
| ![](../../../../_assets/e3223333470668512f5f.jpg) | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. > [!NOTE]<br>> **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) | Ön Sorgulama sekmesinde verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Log raporu almak için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki Log raporu alma işleminde kullanılmak üzere saklanır. |
| ![](../../../../_assets/4ad6cc61ca2c42a19c85.jpg) | Log raporu ekranı hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) | Log raporu almak için verilen kısıtların iptal edildiği butondur. |

**Ölçekleme**

Standart raporlarda miktar, fiyat, tutar, kur, döviz tutarı, döviz fiyatı, firma döviz tutarı ve oran alanları için ölçekleme yapılmasını sağlayan sekmedir.

![](../../../../_assets/98d59e217e5d4191461b.png)

**Örneğin;** Fiyat ve tutar alanlarına 1.000 yazılması, fiyat ve tutara getirilecek verilerin 1.000'e bölüneceği anlamına gelir.
