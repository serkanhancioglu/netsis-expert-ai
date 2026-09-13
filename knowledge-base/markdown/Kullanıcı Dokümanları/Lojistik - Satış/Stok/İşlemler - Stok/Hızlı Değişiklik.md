---
title: "Hızlı Değişiklik"
page_id: "22803651"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Stok"
  - "İşlemler / Stok"
  - "Hızlı Değişiklik"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Stok / İşlemler / Stok / Hızlı Değişiklik"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTNjYzE1MWNmLTFmN2YtNGNjOS05Nzg2LTYwODllNDU5NzQ5OCZsaW5rPTkyNzdiOGZhLWRiMmEtNDFhOS1hZWMwLWVlNjJhNDQ1MDFlZiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=3cc151cf-1f7f-4cc9-9786-6089e4597498&link=9277b8fa-db2a-41a9-aec0-ee62a44501ef&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "hizli-degisiklik_29995365_22803651.html"
source_version: "2022-10-26T09:08:38.763+03:00"
source_bytes: 73049
fetched_at: "2026-09-13T04:04:29+00:00"
generator: "netsis-scraper 1.0.0"
---
# Hızlı Değişiklik

Hızlı Değişiklik, Finans Bölümü'nde, "İşlemler/Stok" menüsünün altında yer alır. Stok sabit bilgilerinin toplu olarak değiştirilmesi amacı ile kullanılan işlemdir. Hızlı Değişiklik; Stok isimleri, KDV oranları, rapor kodları, grup kodları, ölçü birimleri, satış fiyatları, döviz fiyatları ve buna benzer bilgilerin toplu olarak değiştirilmesini sağlar. İşlem öncesi Aralık/Maske tanımlamasının yapılmaması halinde, yapılan değişiklik tüm sabit kartları etkiler. Bu nedenle, işlem yapmadan önce mutlaka yedek alınması gerekir. Sadece sabit kayıtlarda, stok sabit ek kayıtlarında ve stok planlama kayıtlarında değişiklik yapılabilir. Stok hareketleriyle ilgili kayıtlar (fatura, irsaliye, müstahsil makbuzu, sipariş kayıtları) bu bölümden değiştirilmez. "Hızlı Değişiklik" ekranı; Tablo seçimi, Aralık / Maske, Sıralama ve Değiştir olmak üzere dört sekmeden oluşur.

**Tablo Seçimi**

Hızlı Değişiklik ekranı Tablo Seçimi sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Hızlı Değişiklik Ekranı |  |
| --- | --- |
| Değişiklik Yapılacak Tablo | Hızlı değişiklik yapılacak alanın bağlı olduğu tablo seçilir. Stok Sabit, Stok Sabit Ek ve Stok Planlama tablolarındaki alanlar için hızlı değişiklik yapılır. |

**Aralık / Maske**

Aralık/Maske, değişiklik yapılacak stoklar için kısıt verilmesi amacıyla kullanılan sekmedir.

"Stok Kartı Sahaları" alanına, "Tablo Seçimi" sekmesinde belirlenen tabloda bulunan sahalar getirilir.

Hızlı Değişiklik ekranı Aralık/Maske sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Hızlı Değişiklik Ekranı |  |
| --- | --- |
| Cari Kartı Sahaları | Hızlı değişiklik için kısıt verilmesi istenen alanlar yer alır. Ekle ![](../../../../_assets/b050fee00ab65632b16d.jpg) butonu ile istenen alanlar "kısıt verilecek sahalar" kısmına eklenir. |
| Kısıt Verilecek Sahalar | Hızlı değişiklik için kısıt verilen sahaların yer aldığı alandır. Çıkar ![](../../../../_assets/a19640feaa753a52d048.jpg) butonu ile istenmeyen alanlar çıkarılır. |
| Eşit, Küçük, Küçük veya Eşit, Büyük, Büyük veya Eşit, Arasında, Benziyor, Eşit Boş, Eşit Değil, İçinde Eşit Değil | **Eşit:** İşaretlenen alanda belli bir sabit koşula göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "001" olan stok için liste alınacaksa "Eşit" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "001" girilir. Bu durumda, sadece "001" numaralı Stok Kodu için liste alınır. **Küçük:** İşaretlenen alanda belli bir değerden küçük olanlar koşuluna göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "100" olan stok için liste alınacaksa "Küçük" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" girilir. Bu durumda, "100'den küçük" numaralı Stok Kodu için liste alınır. **Küçük veya Eşit:** İşaretlenen alanda belli bir değere eşit veya küçük olanlar koşuluna göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "100" olan stok için liste alınacaksa "Küçük veya Eşit" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" girilir. Bu durumda, "100 ve 100'den küçük" numaralı Stok Kodu için liste alınır. **Büyük:** İşaretlenen alanda belli bir değerden büyük olanlar koşuluna göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "100" olan stok için liste alınacaksa "Büyük" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" girilir. Bu durumda, "100'den büyük" numaralı Stok Kodu için liste alınır. **Büyük veya Eşit:** İşaretlenen alanda belli bir değere eşit veya büyük olanlar koşuluna göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "100" olan stok için liste alınacaksa "Büyük veya Eşit" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" girilir. Bu durumda, "100 ve 100'den büyük" numaralı Stok Kodu için liste alınır. **Arasında:** Seçilen alanla ilgili bir aralık tanımlanması istendiğinde kullanılması gereken seçenektir. Eğer belli bir başlangıç ve bitiş değeri arasında kalan değerlerle ilgili kısıt verilecekse kullanılması gereken seçenektir. Örneğin; Stok Kodu kıstasında, "Arasında" seçeneği seçilip \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" ve yine \<tab\> tuşu ile ilerlenerek altta bulunan alana "200" yazıldığı varsayılsın. Böylece stok kodu 100 ile 200 arasındaki stok kodları için liste alınır. **Benziyor:** Cari ile ilgili kayıt ararken cari hesabın ismi tam olarak bilinmiyorsa benziyor seçeneği kullanılır. Örneğin; cari hesabın isminin CANEL ya da CENEL olacağı düşünülüyorsa, bu seçeneği seçtikten sonra alanın sağ tarafındaki kayıt alanına "C_NEL" yazıldığında, raporda cari ismi "C" ile başlayan ikinci karakteri herhangi bir karakter olan fakat sonu "NEL" ile biten kayıtlar listelenir. **Eşit Boş:** Seçilen sahada hiçbir bilgi olmadığında kullanılan seçenektir. Bu seçenek alfanumerik sahalar için geçerlidir. Sıfırdan büyük veya sıfıra eşit bilgilerin aranması durumunda "Eşit", "Büyük Eşit", "Küçük Eşit" seçenekleri kullanılabilir. **Eşit Değil:** Raporda seçilen Eşit, Küçük ve Eşit, Büyük, Büyük ve Eşit, Arasında, Benziyor ve Eşit Boş seçeneklerindeki belirlemeler olumsuz (hariç) anlamını taşıyorsa "Eşit Değil" seçeneği işaretlenir. Örneğin; stok kodunda "Eşit" seçildiğinde ve "0101" kodu girildiği varsayıldığında, "Eşit Değil" seçeneği işaretlendiğinde, raporda stok kodu "0101" olanların haricindeki stokların listeleneceği anlaşılır. |
| İse/Değil ise | **İse:** Raporda seçilen Eşit, Küçük ve Eşit, Büyük, Büyük ve Eşit, Arasında ve Benziyor seçeneklerindeki belirlemeler olumlu (dahil) anlamını taşıyorsa "İse" seçeneği işaretlenir. Örneğin; stok kodunda "Eşit" seçildiğinde ve "0101" kodu girildiği varsayıldığında, "İse" seçeneği işaretlenirse, rapora stok kodu "0101" olan stokların dahil edileceği anlaşılır. **Değil İse:** Raporda seçilen Eşit, Küçük ve Eşit, Büyük, Büyük ve Eşit, Arasında ve Benziyor seçeneklerindeki belirlemeler olumsuz (hariç) anlamını taşıyorsa "Değil İse" seçeneği işaretlenir. Örneğin; stok kodunda "Eşit" seçildiğinde ve "0101" kodu girildiği varsayıldığında, "Değil İse" seçeneği işaretlendiğinde, raporda stok kodu "0101" olanların haricindeki stokların listeleneceği anlaşılır. |
| Ve/Veya | **Ve:** Seçilen sahalarda zorunlu Genel kredi sözleşmeleri koşulu sağlar. **Örnek 1:** Karmaşık bir stok kodlaması olduğu varsayıldığında; Bu kodlardan iki tanesinin raporda çıkması isteniyor fakat bu iki stok kodunun ortak hiçbir özelliği yok. Bu durumda, "Stok Kodu" sahası iki kez kısıt verilecek sahalar bölümüne aktarılır. 1.Stok Kodu kıstasında eşit Genel kredi sözleşmeleri sı kurularak ilk stok kodu girilir ve "VE" bağlacı işaretlenir. Daha sonra 2. Stok Kodu seçilerek yine eşit Genel kredi sözleşmeleri ile diğer bir stok kodu yazılır. Böylece, raporda sadece bu iki stok koduna ait bilgi alınır. Bu seçenekte tanımlanan her koşulun olması zorunludur. Yani, tanımlanan iki stok kodundan biri bile mevcut değil ise, rapor bilgi vermez. **Örnek 2:** Grup kodu 1, Kod 1 alanı 2 ve Kod 2 alanı 3 olan stoklarla ilgili bir liste alınması istendiğinde; Verilen tanımlamalarda "VE" bağlacı kullanılırsa, mutlaka bu üç kısıta da sahip olan stoklar aranır ve bulunursa listelenir. Üç kısıttan herhangi birine sahip olmayan stoklar raporda listelenmez. **Veya:** Seçilen sahalarda olabilirlik koşulu sağlar. Yani, tanımlanan koşullardan biri bile sağlansa ilgili raporla ilgili bilgi alınabilir. **Örnek 1:** Grup kodu 1, Kod 1 alanı 2 ve Kod 2 alanı 3 olan stoklarla ilgili bir liste alınması istendiğinde; Verilen tanımlamalarda "VEYA" bağlacı kullanılırsa, bu üç kısıttan birine bile sahip olan stoklar aranır ve bulunursa listelenir. |
| ![](../../../../_assets/c7275efbddc154ea1579.jpg) Sakla | Yapılan tanımlamaların onaylanması için kullanılan butondur. |
| ![](../../../../_assets/df428ea63894bc744f9a.jpg) İptal | Yapılan tanımlamaların iptal edilmesi için kullanılan butondur. |

**Sıralama**

"Değiştir" sekmesinde bulunan Onaylı Değiştir ![](../../../../_assets/eca74cf2fe3908d59047.png) butonu kullanıldığında, bilgi değişikliği yapılacak tüm stok kartları sırayla ekrana gelir ve kullanıcının onayı istenir. Sıralama sekmesi, onay sorgulamasının stok sahalarından hangisine göre sıralanacağının belirlenmesi amacıyla kullanılır.

Hızlı Değişiklik ekranı Sıralama sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Hızlı Değişiklik Ekranı |  |
| --- | --- |
| Sahalar | Hızlı değişiklik için sıralanması istenen alanlar yer alır. Ekle ![](../../../../_assets/b050fee00ab65632b16d.jpg) butonu ile istenen alanlar "sıralama sahaları" kısmına eklenir. |
| Sıralama Sahaları | Hızlı değişiklik için sıralama yapılacak sahaların yer aldığı alandır. Çıkar ![](../../../../_assets/a19640feaa753a52d048.jpg) butonu ile istenmeyen alanlar çıkarılır. |
| Sıralama | Sıralamanın ne şekilde yapılacağının belirlendiği alandır. Artan ve Azalan olmak üzere iki seçenekten oluşur. **Artan:** Artan seçeneğin işaretlenmesi halinde, bilgiler küçükten büyüğe sıralı şekilde listelenir. **Azalan:** Azalan seçeneğinin işaretlenmesi halinde, bilgiler büyükten küçüğe sıralı şekilde listelenir. |
| ![](../../../../_assets/c7275efbddc154ea1579.jpg) Sakla | Yapılan tanımlamaların onaylanması için kullanılan butondur. |
| ![](../../../../_assets/df428ea63894bc744f9a.jpg) İptal | Yapılan tanımlamaların iptal edilmesi için kullanılan butondur. |

**Değiştir**

Hızlı Değişiklik ekranı Değiştir sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Değiştir Ekranı |  |
| --- | --- |
| Cari Kartı Sahaları | Bu alanda "Tablo Seçimi" sekmesinde seçilen tabloya ait sahalar listelenir. Bu sahalar arasından değişiklik yapılacak alan seçilerek Ekle ![](../../../../_assets/b050fee00ab65632b16d.jpg) butonu ile istenen alanlar "değiştirilecek sahalar" kısmına eklenir. |
| Değiştirilecek Sahalar | Hızlı değişiklik için sıralama yapılacak sahaların yer aldığı alandır. Çıkar ![](../../../../_assets/a19640feaa753a52d048.jpg) butonu ile istenmeyen alanlar çıkarılır. |
| **![](../../../../_assets/38dd9cc6038d77a3aae2.png)**Data İzle | "Değiştirilecek Sahalar" alanına aktarılan sahalara ait kayıtlı bilgilerin listesine ulaşılmasını sağlayan butondur. **Örneğin:** "Kod-1" sahalarında değişiklik yapılacak ise Data İzle ![](../../../../_assets/38dd9cc6038d77a3aae2.png) butonuna tıklandığında stok kartı kayıtları bölümünde kayıtlı bulunan kod-1 kayıtlarının listesine ulaşılır. ![](../../../../_assets/337a6949546f2380ba48.png) |
| Hangi Sahaya Göre | Sayısal bir alan değiştirileceği durumlarda, hangi sahanın baz alınarak işlem yapılacağı, cari sabit kayıtlarındaki sayısal sahaları içeren rehber yardımı ile seçilir. Değiştirilecek olan saha alfabetik (hesaplama gerektirmeyen) bir saha olarak belirlenmişse bu alan boş bırakılır. |
| Hesap Tipi | Sayısal alanlar için dört tip işlem yapılabilir. Bunlar; Yüzde, Tutar, Çarpım ve Sabittir. Alanın sağ tarafında yer alan aşağı ok butonu ile seçim yapılır. Değiştirilecek olan saha alfabetik (hesaplama gerektirmeyen) bir saha olarak belirlenmişse bu alan boş bırakılır. **Yüzde:** "Yüzde" tipi seçildiğinde, "Sabit Değer" alanına girilecek yüzde değer oranı, “Hangi Sahaya Göre” alanında seçilen sahaya göre artırılır. **Tutar:** "Tutar" tipi seçildiğinde girilecek tutar değeri kadar değiştirilecek sahanın değeri artar. (-) değer girildiğinde değiştirilecek saha üzerinden çıkarma işlemi yapılır. **Çarpım:** "Çarpım" tipinde değiştirilecek sahanın değeri, verilen değerle çarpılarak oluşturulur. **Sabit:** "Sabit" tipi seçildiğinde, değiştirilecek sahada sabit bir değer oluşturulur. Değiştirilecek sahanın değeri, bu alanda yazılan değer olarak değişir. |
| Yuvarlama | Sayısal değişikliklerde hesaplanan sonuç değerinin değişiklik yapılan sahaya aktarılması sırasında yuvarlama yapılması istendiğinde, bu alandaki yuvarlama seçeneklerinden biri seçilir. Alanın sağ tarafında yer alan aşağı ok butonu ile, yuvarlama seçenekleri arasından tercih yapılır. Yuvarlama yapılmasının istenmediği durumlarda bu seçenek boş bırakılır. |
| Yuvarlama Tipi | Hiçbiri, Aşağı, Yukarı seçeneklerinden oluşur. Alanın sağ tarafında yer alan aşağı ok butonu ile seçim yapılır. Değişiklik sırasında hesaplanan sayısal sahanın aşağımı yoksa yukarımı yuvarlanacağı seçilir. Yuvarlama yapılmayacağı durumlarda "Hiçbiri" seçeneği seçilerek ilerlenir. |
| ![](../../../../_assets/c7275efbddc154ea1579.jpg) Sakla | Yapılan tanımlamaların onaylanması için kullanılan butondur. |
| ![](../../../../_assets/df428ea63894bc744f9a.jpg) İptal | Yapılan tanımlamaların iptal edilmesi için kullanılan butondur. |
| **![](../../../../_assets/eca74cf2fe3908d59047.png)**Onaylı Değiştir | Butona basıldığında "Hızlı Değişiklik Onay" ekranı görüntülenir. "Hızlı Değişiklik Onay" ekranında değişiklik yapılacak kayıtlar “Sıralama” sekmesinde verilen sahaya göre sıralı olarak tek tek ekrana gelir. Eğer kullanıcı Değiştir ![](../../../../_assets/ed4eea4ebf44a6bff8ba.png) butonu ile onaylarsa o kayıt için değişiklik yapılır. Vazgeç ![](../../../../_assets/4cd332c42b60e8c1b22b.png) butonuna tıklandığında ise ekran kapatılır. "Hızlı Değişiklik Onay" ekranında değişiklik yapılacak alanın eski değeri “Eski Değer” ve değişiklikten sonra hangi değeri alacağı “Yeni Değer” alanında izlenir. |
| **![](../../../../_assets/ed4eea4ebf44a6bff8ba.png)**Değiştir | Değiştirilecek kayıtlar ile ilgili tanımlamalar yapıldıktan sonra “Değiştir” tuşuna basılırsa “Kısıt” alanında verilen kısıta uygun olan kayıtlar, kullanıcının onayı sorulmadan otomatik olarak değiştirilecektir. Değişiklik işlemi bittikten sonra işlem geri alınamamaktadır. Bu yüzden değişiklik işlemine başlamadan önce yedek alınması önerilmektedir. |
