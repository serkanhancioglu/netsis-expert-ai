---
title: "Satınalma Teklif Değerlendirme Raporu"
page_id: "22803626"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Talep - Teklif"
  - "Raporlar / Talep-Teklif"
  - "Satınalma Teklif Değerlendirme Raporu"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Talep - Teklif / Raporlar / Talep-Teklif / Satınalma Teklif Değerlendirme Raporu"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWY3M2IyZWFjLTViMTEtNDA5Mi1hZGM5LTUwYWJkN2E0ZjdjMCZsaW5rPWUxZjNiNjU2LTFiZDItNDU0Mi1iYzI5LWQwM2ZiNzQ1Njk3NyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=f73b2eac-5b11-4092-adc9-50abd7a4f7c0&link=e1f3b656-1bd2-4542-bc29-d03fb7456977&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "satinalma-teklif-degerlendirme-raporu_41163705_22803626.html"
source_version: "2022-10-27T11:48:36.830+03:00"
source_bytes: 586941
fetched_at: "2026-09-13T04:03:51+00:00"
generator: "netsis-scraper 1.0.0"
---
# Satınalma Teklif Değerlendirme Raporu

Satınalma Teklif Değerlendirme Raporu, Lojistik - Satış Bölümü'nde, "Raporlar/Talep Teklif" menüsünün altında yer alır. Satınalma Teklif Değerlendirme Raporu, bir talebe bağlı birden fazla teklifin olduğu durumlarda girilen tekliflerden en uygun olanının belirlenmesi için kullanılan rapordur. Satınalma tekliflerinden en uygun olanı belirlenirken, girilen tekliflerin her biri toplamlar bazında değerlendirildiği gibi, tekliflerde yer alan stokları kalem bazında da değerlendirerek sonucun tek bir raporda sunulması sağlanır. Rapor çağrıldığında ilk olarak hangi taleplerden oluşan tekliflerin değerlendirileceğini sorgulayan "Satınalma Talep Seçimi" ekranı görüntülenir. İlgili talep kaydına ait kısıt verilerek Tamam ![](../../../../_assets/a8eb576ad165012b70f6.png) butonuna basıldığında tekliflerin sorgulanacağı yeni bir ekrana geçilir. Talep seçimi ekranında kısıt verilmeden Tamam ![](../../../../_assets/a8eb576ad165012b70f6.png) butonuna tıklandığında, "Satınalma Teklif Değerledirme Raporu" ekranına geçilir.

Herhangi bir teklifin değerlendirilmeye alınması için mutlaka, Satınalma Talep kaydı bağlantısının olması gerekir. Talep bağlantısı olmayan teklif kayıtları bu raporda dikkate alınmaz.

Satınalma Teklif Değerlendirme Raporu ekranı; Ön Sorgulama, Kısıt, Sıralama, Ölçekleme ve Yazıcı Seçenekleri sekmesinden oluşur.

"Satınalma Teklif Değerlendirme Raporu" bölümünden, değerlendirmeye dahil edilecek teklifler için kısıt verilir.

Verilen kısıtlar sonrası, aşağıda anlatılan yöntemle teklifler değerlendirilerek sıralama yapılır:

- Teklif kayıtları değerlendirilirken, sadece net fiyat bilgileri dikkate alınır.

Talebinize karşılık dört farklı satıcıdan gelen teklifler aşağıdaki gibi olduğu varsayıldığında ve aşağıdaki gibi bir tablo örneği olduğunda:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | SATICI-1 | SATICI-2 | SATICI-3 | SATICI-4 |
| STOK-1 | 1.000.000 | ----------- | 3.000.000 | 1.000.000 |
| STOK-2 | 2.000.000 | 1.500.000 | 4.100.000 | 3.000.000 |
| STOK-3 | 3.500.000 | 4.500.000 | 3.200.000 | 1.200.000 |
| STOK-4 | 1.500.000 | 3.500.000 | 3.000.000 | 4.000.000 |

Örnekte, sadece Satıcı-2'nin talepte yer alan Stok-1 için teklif vermediği görülür. Teklifler değerlendirilirken, ilk olarak her bir stok için verilen en düşük fiyat bulunur. Daha sonra bu fiyat ilgili stok için verilen diğer fiyatlardan çıkarılır. Herhangi bir fiyat verilmemesi halinde, bu kaydın en uygun teklif olarak değerlendirilmemesi için ilgili hücreye yüksek bir değer atanır. Örnekte; Satıcı-2, Stok-1 için teklif vermediği için, ilgili hücreye 230.000.000 değeri atanır. Stok-1 için verilen en düşük teklif 1.000.000 TL tutarındadır. Bu tutar ilgili satırdaki tutarların hepsinden çıkarılarak 0 (sıfır) tutarı bulunur. Aynı işlem, her stok için ayrı ayrı yapılır.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | SATICI-1 | SATICI-2 | SATICI-3 | SATICI-4 |
| STOK-1 | 0 | 220.000.000 | 2.000.000 | 0 |
| STOK-2 | 500.000 | 0 | 2.600.000 | 1.500.000 |
| STOK-3 | 2.300.000 | 3.300.000 | 2.000.000 | 0 |
| STOK-4 | 0 | 2.000.000 | 1.500.000 | 2.500.000 |

Bu işlemden sonra, herhangi bir sütunda 0 (sıfır) değerinin bulunmaması halinde, ilgili sütundaki en küçük değer, diğer sütundaki değerlerden çıkarılarak 0 (sıfır) değeri elde edilir. Örnekte, Satıcı-3 için 0 (sıfır) değerinin bulunamamasından dolayı, bu cari hesabın verdiği en düşük fiyat teklifi olan 1.500.000 TL değerlendirmede kullanılır.

Böyle bir durumda oluşacak tablo aşağıdaki şekildedir:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | SATICI-1 | SATICI-2 | SATICI-3 | SATICI-4 |
| STOK-1 | 0 | 220.000.000 | 500.000 | 0 |
| STOK-2 | 500.000 | 0 | 1.100.000 | 1.500.000 |
| STOK-3 | 2.300.000 | 3.300.000 | 500.000 | 0 |
| STOK-4 | 0 | 2.000.000 | **0** | 2.500.000 |

"Satınalma Teklif Değerlendirme Raporu" teklifleri iki şekilde değerlendirir. Raporun ilk sayfasında teklifler satıcı cari bazında, ikinci sayfasında da kalem bazında değerlendirilir. Cari bazında yapılan değerlendirmede en çok 0 (sıfır) değerine sahip sütün en iyi tekliftir. Ancak, bu şekilde birden fazla cari varsa sütunun toplamı dikkate alınır ve sıralama buna göre yapılır.

Örnekte, sütun bazında en fazla 0 (sıfır) değerine sahip tekliflerin Satıcı-1 ve Satıcı-4’ten geldiği görülür. Ancak, toplam bazında en düşük teklifi Satıcı-1 verdiği için, ilk sırada bu cari yer alır.

Böyle bir durumda raporun ilk sayfasındaki teklif bazındaki sıralama aşağıdaki gibidir:

![](../../../../_assets/4b675de2ca5dec6f3af1.jpg)

Stok bazında değerlendirme yapılırken satır bazında değerlendirme yapılır. Yani, stok satırlarında 0 (sıfır) değere sahip satın alma teklifleri listelenir. Bir stok için 0 (sıfır) değere sahip birden fazla teklifin bulunması halinde de sıralama teklif numarasına göre yapılır. Bu durumda raporun ikinci sayfasında yer alan stok bazındaki sıralama aşağıdaki gibidir:

![](../../../../_assets/aa7d7926e8292090336a.jpg)

Kalem bazında yapılan değerlendirmede sadece 0 (sıfır) değerine sahip hücreler dikkate alınır. Oysaki, bir teklifin ilk sayfada dikkate alınması için talep bağlantılı olarak ilgili stoklara ait olması yeterlidir.

**Ön Sorgulama**

Ön Sorgulama sekmesi bilgileri aşağıdaki şekildedir:

| Satınalma Teklif Değerlendirme Raporu Ekranı |  |
| --- | --- |
| Belge Tipi | Satınalma teklif değerlendirme raporu almak için belge tipi kısıdı verilen alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile, Satınalma Talep veya Satış Talep tipleri arasından seçim yapılır. |
| Tipi | Satınalma teklif değerlendirme raporu almak için talep tipi kısıdının verildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile; Açık, Kapalı, Onaysız veya Hepsi seçenekleri arasından seçim yapılır. |
| Belge No Aralığı | Satınalma teklif değerlendirme raporu almak için başlangıç ve bitiş belge numarası aralığı kısıdı verilen alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, belge numaraları arasından seçim yapılır. |
| Tarih Aralığı | Satınalma teklif değerlendirme raporu almak için başlangıç ve bitiş tarih aralığı kısıdı verilen alandır. |
| Cari Kodu Aralığı | Satınalma teklif değerlendirme raporu almak için başlangıç ve bitiş cari kod aralığı kısıdı verilen alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, cari kodlar arasından seçim yapılır. |
| Proje Kodu | Satınalma teklif değerlendirme raporu almak için proje kodu kısıdı verilen alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, proje kodları arasından seçim yapılır. Proje Uygulaması için Yardımcı Programlar → Kayıt → [Şirket-Şube Parametreleri](<../../../Muhasebe/Muhasebe Modülü/Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/Genel Tanımlar/Yardımcı Programlar-Şirket-Şube Parametreleri.md>) → "Proje Uygulaması Var" parametresinin işaretlenmesi gerekir. |
| ![](../../../../_assets/7ba39f9046a578093326.png) Rapor | Yukarıdaki alanlara girilen bilgiler doğrultusunda, rapor almak için kullanılan butondur. Butonun sağ tarafında yer alan aşağı ok tuşu, "Gelişmiş Rapor" seçeneğinin kullanılmasını sağlar. Kullanıcı, "Gelişmiş Rapor" seçeneği ile ekrana gelen tablo üzerinde hesaplama yapabilir. Bu seçenek sayesinde, 13684 satırın üstündeki raporlamaların da tek sayfa üzerinden raporlanması sağlanır. "Rapor" seçeneği Text Dosya, Excel Dosya, VTS Format, HTML kayıt türlerini desteklerken, "Gelişmiş Rapor" seçeneği Excel Workbook, Excel Template, Excel 97-2003 Workbook, Excel 97-2003 Template, Comma Delimited, Text Document, Web Page, XML Document, PDF Document kayıt türlerini destekler. |
| ![](../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Ön Sorgulama ve Genel Kısıtlar sekmesinde verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Satınalma teklif değerlendirme raporu almak için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki satınalma teklif değerlendirme raporu işleminde kullanılmak üzere saklanır. |
| ![](../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | Satınalma teklif değerlendirme raporu almak için standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Satınalma teklif değerlendirme raporu almak için verilen kısıtların iptal edildiği butondur. |

**Genel Kısıtlar**

Genel Kısıtlar

| Satınalma Teklif Değerlendirme Raporu Ekranı |  |
| --- | --- |
| Döviz Bilgileri Basılsın | Satınalma teklif değerlendirme raporuna döviz bilgisinin basılması için kullanılan seçenektir |
| ![](../../../../_assets/7ba39f9046a578093326.png) Rapor | Yukarıdaki alanlara girilen bilgiler doğrultusunda, rapor almak için kullanılan butondur. Butonun sağ tarafında yer alan aşağı ok tuşu, "Gelişmiş Rapor" seçeneğinin kullanılmasını sağlar. Kullanıcı, "Gelişmiş Rapor" seçeneği ile ekrana gelen tablo üzerinde hesaplama yapabilir. Bu seçenek sayesinde, 13684 satırın üstündeki raporlamaların da tek sayfa üzerinden raporlanması sağlanır. "Rapor" seçeneği Text Dosya, Excel Dosya, VTS Format, HTML kayıt türlerini desteklerken, "Gelişmiş Rapor" seçeneği Excel Workbook, Excel Template, Excel 97-2003 Workbook, Excel 97-2003 Template, Comma Delimited, Text Document, Web Page, XML Document, PDF Document kayıt türlerini destekler. |
| ![](../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Ön Sorgulama ve Genel Kısıtlar sekmesinde verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Satınalma teklif değerlendirme raporu almak için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki satınalma teklif değerlendirme raporu işleminde kullanılmak üzere saklanır. |
| ![](../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | Satınalma teklif değerlendirme raporu almak için standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Satınalma teklif değerlendirme raporu almak için verilen kısıtların iptal edildiği butondur. |

**Kısıt**

Kısıt sekmesi bilgileri aşağıdaki şekildedir:

| Satınalma Teklif Değerlendirme Raporu Ekranı |  |
| --- | --- |
| Sahalar | Satınalma teklif değerlendirme raporu almak için kısıt verilmesi istenen alanlar yer alır. Ekle ![](../../../../_assets/b050fee00ab65632b16d.jpg) butonu ile istenen alanlar "kısıt verilecek sahalar" kısmına eklenir. |
| Kısıt Verilecek Sahalar | Satınalma teklif değerlendirme raporu almak için kısıt verilen sahaların yer aldığı alandır. Ekle ![](../../../../_assets/a19640feaa753a52d048.jpg) butonu ile istenmeyen alanlar çıkarılır. |
| Eşit, Küçük, Küçük veya Eşit, Büyük, Büyük veya Eşit, Arasında, Benziyor, Eşit Boş, Eşit Değil, İçinde Eşit Değil | **Eşit:** İşaretlenen alanda belli bir sabit koşula göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "001" olan stok için liste alınacaksa "Eşit" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "001" girilir. Bu durumda, sadece "001" numaralı Stok Kodu için liste alınır. **Küçük:** İşaretlenen alanda belli bir değerden küçük olanlar koşuluna göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "100" olan stok için liste alınacaksa "Küçük" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" girilir. Bu durumda, "100'den küçük" numaralı Stok Kodu için liste alınır. **Küçük veya Eşit:** İşaretlenen alanda belli bir değere eşit veya küçük olanlar koşuluna göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "100" olan stok için liste alınacaksa "Küçük veya Eşit" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" girilir. Bu durumda, "100 ve 100'den küçük" numaralı Stok Kodu için liste alınır. **Büyük:** İşaretlenen alanda belli bir değerden büyük olanlar koşuluna göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "100" olan stok için liste alınacaksa "Büyük" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" girilir. Bu durumda, "100'den büyük" numaralı Stok Kodu için liste alınır. **Büyük veya Eşit:** İşaretlenen alanda belli bir değere eşit veya büyük olanlar koşuluna göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "100" olan stok için liste alınacaksa "Büyük veya Eşit" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" girilir. Bu durumda, "100 ve 100'den büyük" numaralı Stok Kodu için liste alınır. **Arasında:** Seçilen alanla ilgili bir aralık tanımlanması istendiğinde kullanılması gereken seçenektir. Eğer belli bir başlangıç ve bitiş değeri arasında kalan değerlerle ilgili kısıt verilecekse kullanılması gereken seçenektir. Örneğin; Stok Kodu kıstasında, "Arasında" seçeneği seçilip \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" ve yine \<tab\> tuşu ile ilerlenerek altta bulunan alana "200" yazıldığı varsayılsın. Böylece stok kodu 100 ile 200 arasındaki stok kodları için liste alınır. **Benziyor:** Cari ile ilgili kayıt ararken cari hesabın ismi tam olarak bilinmiyorsa benziyor seçeneği kullanılır. Örneğin; cari hesabın isminin CANEL ya da CENEL olacağı düşünülüyorsa, bu seçeneği seçtikten sonra alanın sağ tarafındaki kayıt alanına "C_NEL" yazıldığında, raporda cari ismi "C" ile başlayan ikinci karakteri herhangi bir karakter olan fakat sonu "NEL" ile biten kayıtlar listelenir. **Eşit Boş:** Seçilen sahada hiçbir bilgi olmadığında kullanılan seçenektir. Bu seçenek alfanumerik sahalar için geçerlidir. Sıfırdan büyük veya sıfıra eşit bilgilerin aranması durumunda "Eşit", "Büyük Eşit", "Küçük Eşit" seçenekleri kullanılabilir. **Eşit Değil:** Raporda seçilen Eşit, Küçük ve Eşit, Büyük, Büyük ve Eşit, Arasında, Benziyor ve Eşit Boş seçeneklerindeki belirlemeler olumsuz (hariç) anlamını taşıyorsa "Eşit Değil" seçeneği işaretlenir. Örneğin; stok kodunda "Eşit" seçildiğinde ve "0101" kodu girildiği varsayıldığında, "Eşit Değil" seçeneği işaretlendiğinde, raporda stok kodu "0101" olanların haricindeki stokların listeleneceği anlaşılır. |
| İse/Değil ise | **İse:** Raporda seçilen Eşit, Küçük ve Eşit, Büyük, Büyük ve Eşit, Arasında ve Benziyor seçeneklerindeki belirlemeler olumlu (dahil) anlamını taşıyorsa "İse" seçeneği işaretlenir. Örneğin; stok kodunda "Eşit" seçildiğinde ve "0101" kodu girildiği varsayıldığında, "İse" seçeneği işaretlenirse, rapora stok kodu "0101" olan stokların dahil edileceği anlaşılır. **Değil İse:** Raporda seçilen Eşit, Küçük ve Eşit, Büyük, Büyük ve Eşit, Arasında ve Benziyor seçeneklerindeki belirlemeler olumsuz (hariç) anlamını taşıyorsa "Değil İse" seçeneği işaretlenir. Örneğin; stok kodunda "Eşit" seçildiğinde ve "0101" kodu girildiği varsayıldığında, "Değil İse" seçeneği işaretlendiğinde, raporda stok kodu "0101" olanların haricindeki stokların listeleneceği anlaşılır. |
| Ve/Veya | **Ve:** Seçilen sahalarda zorunlu bağlantı koşulu sağlar. **Örnek 1:** Karmaşık bir stok kodlaması olduğu varsayıldığında; Bu kodlardan iki tanesinin raporda çıkması isteniyor fakat bu iki stok kodunun ortak hiçbir özelliği yok. Bu durumda, "Stok Kodu" sahası iki kez kısıt verilecek sahalar bölümüne aktarılır. 1.Stok Kodu kıstasında eşit bağlantısı kurularak ilk stok kodu girilir ve "VE" bağlacı işaretlenir. Daha sonra 2. Stok Kodu seçilerek yine eşit bağlantısı ile diğer bir stok kodu yazılır. Böylece, raporda sadece bu iki stok koduna ait bilgi alınır. Bu seçenekte tanımlanan her koşulun olması zorunludur. Yani, tanımlanan iki stok kodundan biri bile mevcut değil ise, rapor bilgi vermez. **Örnek 2:** Grup kodu 1, Kod 1 alanı 2 ve Kod 2 alanı 3 olan stoklarla ilgili bir liste alınması istendiğinde; Verilen tanımlamalarda "VE" bağlacı kullanılırsa, mutlaka bu üç kısıta da sahip olan stoklar aranır ve bulunursa listelenir. Üç kısıttan herhangi birine sahip olmayan stoklar raporda listelenmez. **Veya:** Seçilen sahalarda olabilirlik koşulu sağlar. Yani, tanımlanan koşullardan biri bile sağlansa ilgili raporla ilgili bilgi alınabilir. **Örnek 1:** Grup kodu 1, Kod 1 alanı 2 ve Kod 2 alanı 3 olan stoklarla ilgili bir liste alınması istendiğinde; Verilen tanımlamalarda "VEYA" bağlacı kullanılırsa, bu üç kısıttan birine bile sahip olan stoklar aranır ve bulunursa listelenir. |
| ![](../../../../_assets/c7275efbddc154ea1579.jpg) Sakla | Yapılan tanımlamaların onaylanması için kullanılan butondur. |
| ![](../../../../_assets/df428ea63894bc744f9a.jpg) İptal | Yapılan tanımlamaların iptal edilmesi için kullanılan butondur. |
| ![](../../../../_assets/7ba39f9046a578093326.png) Rapor | Yukarıdaki alanlara girilen bilgiler doğrultusunda, rapor almak için kullanılan butondur. Butonun sağ tarafında yer alan aşağı ok tuşu, "Gelişmiş Rapor" seçeneğinin kullanılmasını sağlar. Kullanıcı, "Gelişmiş Rapor" seçeneği ile ekrana gelen tablo üzerinde hesaplama yapabilir. Bu seçenek sayesinde, 13684 satırın üstündeki raporlamaların da tek sayfa üzerinden raporlanması sağlanır. "Rapor" seçeneği Text Dosya, Excel Dosya, VTS Format, HTML kayıt türlerini desteklerken, "Gelişmiş Rapor" seçeneği Excel Workbook, Excel Template, Excel 97-2003 Workbook, Excel 97-2003 Template, Comma Delimited, Text Document, Web Page, XML Document, PDF Document kayıt türlerini destekler. |
| ![](../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Ön Sorgulama ve Genel Kısıtlar sekmesinde verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Satınalma teklif değerlendirme raporu almak için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki satınalma teklif değerlendirme raporu işleminde kullanılmak üzere saklanır. |
| ![](../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | Satınalma teklif değerlendirme raporu almak için standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Satınalma teklif değerlendirme raporu almak için verilen kısıtların iptal edildiği butondur. |

**Sıralama**

Sıralama sekmesi bilgileri aşağıdaki şekildedir:

| Satınalma Teklif Değerlendirme Raporu Ekranı |  |
| --- | --- |
| Sahalar | Satınalma teklif değerlendirme raporu almak için sıralanması istenen alanlar yer alır. Ekle ![](../../../../_assets/b050fee00ab65632b16d.jpg) butonu ile istenen alanlar "sıralama sahaları" kısmına eklenir. |
| Sıralama Sahaları | Satınalma teklif değerlendirme raporu almak için sıralama yapılacak sahaların yer aldığı alandır. Çıkar ![](../../../../_assets/a19640feaa753a52d048.jpg) butonu ile istenmeyen alanlar çıkarılır. |
| Sıralama | Sıralamanın ne şekilde yapılacağının belirlendiği alandır. Artan ve Azalan olmak üzere iki seçenekten oluşur. **Artan:** Artan seçeneğin işaretlenmesi halinde, bilgiler küçükten büyüğe sıralı şekilde listelenir. **Azalan:** Azalan seçeneğinin işaretlenmesi halinde, bilgiler büyükten küçüğe sıralı şekilde listelenir. |
| Değişimde Toplam | Bu alan işaretlendiğinde, sıralanan bilgi her değiştiğinde ara toplam alınır. |
| Birinci Saha Değ. Baş. Saha | "Değişimde Toplam" seçeneği işaretlendiğinde, sıralanan bilgi her değiştiğinde ara toplam alınır. Bu durumda raporda, sıralı alanın içerdiği bilginin aynı kaldığı kayıt grubu için, sıralı alanın değeri başlık olarak yazılır. Başlıkların daha anlamlı olması açısından, başlık olarak sıralı alan bilgisinden daha farklı bir bilginin yazılması sağlanır. Örneğin; Sıralı Saha - 1’de (grup koduna göre sıralatılan bir raporda), eğer grup kodlarının isimleri tanımlı ise (Grup Kodu Girişi bölümünden tanımlanmış ise) sıralama grup koduna göre yapılmasına rağmen, başlık olarak **grup kodu bilgisi** yerine, **grup ismi bilgisi** yazılır. Böylece grup kodlarına yabancı olan ya da bilmeyen bir kullanıcı için, raporun daha anlaşılır olması sağlanır. |
| ![](../../../../_assets/c7275efbddc154ea1579.jpg) Sakla | Yapılan tanımlamaların onaylanması için kullanılan butondur. |
| ![](../../../../_assets/df428ea63894bc744f9a.jpg) İptal | Yapılan tanımlamaların iptal edilmesi için kullanılan butondur. |
| Kırılımda Kayıt Sayısı | "Değişimde Toplam" alanının işaretlendiği durumlarda, her ara toplam için listelenen satır kayıt sayısının alınmasını sağlayan seçenektir. |
| Kümüle Döküm | Raporda dökülecek bilgilerin toplam olarak tek kalemde görüntülenmesi istendiğinde işaretlenmesi gereken seçenektir. Sıralama alanlarında tanımlanan en son sahada kümülasyon yapılır. **Örneğin;** Stok hareket kayıtları ile ilgili bir rapor alındığında, "Kümüle Döküm" seçeneği işaretlenmezse o stoka ait kayıtlar hareket bazında satır satır listelenir. "Kümüle Döküm" seçeneği işaretlenirse, her bir stok koduna ait hareketler kümüle olarak tek satırda toplanır ve o şekilde listelenir. |
| ![](../../../../_assets/7ba39f9046a578093326.png) Rapor | Yukarıdaki alanlara girilen bilgiler doğrultusunda, rapor almak için kullanılan butondur. Butonun sağ tarafında yer alan aşağı ok tuşu, "Gelişmiş Rapor" seçeneğinin kullanılmasını sağlar. Kullanıcı, "Gelişmiş Rapor" seçeneği ile ekrana gelen tablo üzerinde hesaplama yapabilir. Bu seçenek sayesinde, 13684 satırın üstündeki raporlamaların da tek sayfa üzerinden raporlanması sağlanır. "Rapor" seçeneği Text Dosya, Excel Dosya, VTS Format, HTML kayıt türlerini desteklerken, "Gelişmiş Rapor" seçeneği Excel Workbook, Excel Template, Excel 97-2003 Workbook, Excel 97-2003 Template, Comma Delimited, Text Document, Web Page, XML Document, PDF Document kayıt türlerini destekler. |
| ![](../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Ön Sorgulama ve Genel Kısıtlar sekmesinde verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Satınalma teklif değerlendirme raporu almak için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki satınalma teklif değerlendirme raporu işleminde kullanılmak üzere saklanır. |
| ![](../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | Satınalma teklif değerlendirme raporu almak için standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Satınalma teklif değerlendirme raporu almak için verilen kısıtların iptal edildiği butondur. |

**Ölçekleme**

Standart raporlarda miktar, fiyat, tutar, kur, döviz tutarı, döviz fiyatı, firma döviz tutarı ve oran alanları için ölçekleme yapılmasını sağlayan sekmedir.

**Örneğin:** Fiyat ve tutar alanlarına 1.000 yazılması, fiyat ve tutara getirilecek verilerin 1.000'e bölüneceği anlamına gelir.

**Yazıcı Seçenekleri**

Yazıcı Seçenekleri sekmesi bilgileri aşağıdaki şekildedir:

| Satınalma Teklif Değerlendirme Raporu Ekranı |  |
| --- | --- |
| Ekran | Raporun ekrandan alınması için işaretlenmesi gereken seçenektir. Hiçbir değişiklik yapılmaması durumunda, raporda ekran seçeneği işaretli olduğu için, rapor yine ekrandan alınır. |
| Yazıcı | Raporun yazıcıdan alınması için işaretlenmesi gereken seçenektir |
| Toplam Sayfa | Rapor yazıcıya döküldüğü zaman yazıcıdan kaç sayfa çıkarılacağının gösterildiği alandır. Kullanıcı, raporu yazıcıya göndermeden önce bu seçeneği işaretleyerek Rapor ![](../../../../_assets/21c20c78203acae9cce6.jpg) butonuna basarsa, yazıcıya dökülecek sayfa adedi ekranda görüntülenir. ![](../../../../_assets/b2e157c1e0713bfefb94.png) |
| Satınalma Teklif Değerlendirme Raporu Ekranı | Yazıcı Seçenekleri - Yönlendirme |
| Dikey | Raporun sadece yazıcı seçeneği ile bastırılması durumunda kullanılan seçenektir. Döküm yapılacak kağıdın genişliğine göre rapor dikey veya yatay olarak alınabilir. Bu seçenekte hiçbir değişiklik yapılmaması durumunda otomatik olarak "Dikey" işaretlenmiş olduğu için rapor dikey şekilde basılır. Ekran seçeneğinde bu parametrenin herhangi bir işlevi yoktur. |
| Yatay | Raporun sadece yazıcı seçeneği ile bastırılması durumunda kullanılan seçenektir. Döküm yapılacak kağıdın genişliğine göre rapor dikey veya yatay olarak alınabilir. Raporun kağıda yatay olarak basılması için işaretlenmesi gereken seçenektir. Ekran seçeneğinde bu parametrenin herhangi bir işlevi yoktur. |
| Satınalma Teklif Değerlendirme Raporu Ekranı | Yazıcı Seçenekleri |
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
| ![](../../../../_assets/7ba39f9046a578093326.png) Rapor | Yukarıdaki alanlara girilen bilgiler doğrultusunda, rapor almak için kullanılan butondur. Butonun sağ tarafında yer alan aşağı ok tuşu, "Gelişmiş Rapor" seçeneğinin kullanılmasını sağlar. Kullanıcı, "Gelişmiş Rapor" seçeneği ile ekrana gelen tablo üzerinde hesaplama yapabilir. Bu seçenek sayesinde, 13684 satırın üstündeki raporlamaların da tek sayfa üzerinden raporlanması sağlanır. "Rapor" seçeneği Text Dosya, Excel Dosya, VTS Format, HTML kayıt türlerini desteklerken, "Gelişmiş Rapor" seçeneği Excel Workbook, Excel Template, Excel 97-2003 Workbook, Excel 97-2003 Template, Comma Delimited, Text Document, Web Page, XML Document, PDF Document kayıt türlerini destekler. |
| ![](../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Ön Sorgulama ve Genel Kısıtlar sekmesinde verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Satınalma teklif değerlendirme raporu almak için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki satınalma teklif değerlendirme raporu işleminde kullanılmak üzere saklanır. |
| ![](../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | Satınalma teklif değerlendirme raporu almak için standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Satınalma teklif değerlendirme raporu almak için verilen kısıtların iptal edildiği butondur. |
