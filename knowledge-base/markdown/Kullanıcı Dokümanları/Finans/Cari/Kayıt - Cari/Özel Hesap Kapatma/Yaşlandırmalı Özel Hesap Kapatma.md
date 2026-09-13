---
title: "Yaşlandırmalı Özel Hesap Kapatma"
page_id: "22803718"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Cari"
  - "Kayıt / Cari"
  - "Özel Hesap Kapatma"
  - "Yaşlandırmalı Özel Hesap Kapatma"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Cari / Kayıt / Cari / Özel Hesap Kapatma / Yaşlandırmalı Özel Hesap Kapatma"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWMzZDQ2OWY4LWIyOGEtNDE3NC04MGM2LTdjOWNmOTc2MjUwMiZsaW5rPWJkMTc0NDM3LWZiMDQtNGNmZC05OWY3LTcxYjUzYzM1ZmM2NCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=c3d469f8-b28a-4174-80c6-7c9cf9762502&link=bd174437-fb04-4cfd-99f7-71b53c35fc64&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "yaslandirmali-ozel-hesap-kapatma_22804809_22803718.html"
source_version: "2022-10-27T09:02:35.557+03:00"
source_bytes: 210384
fetched_at: "2026-09-13T04:07:36+00:00"
generator: "netsis-scraper 1.0.0"
---
# Yaşlandırmalı Özel Hesap Kapatma

Yaşlandırmalı Özel Hesap Kapatma, Finans Bölümü'nde Kayıt/Cari menüsünün altında yer alır. Cari hesap kayıtlarını özel hesap kapatma yöntemiyle takip eden firmaların, bazı sebeplerden dolayı özel hesap kapatma bilgilerinde bozulmalar yaşaması veya belli bir tarihten sonra özel hesap kapatma yöntemini kullanmak isteyen firmaları için düzenlenmiş bölümdür. Daha önce özel hesap kapatma yapıldıysa, yapılan kapatma işlemleri program tarafından kaldırılır ve yeniden düzenlemeye gidilir. Bu bölüme ilk kez girildiğinde, işlemlerle ilgili bir karşılama mesajı ile ekrana gelir.

![](../../../../../_assets/87d97222f2ee6c196c32.png)

"Yaşlandırmalı Özel Hesap Kapatma" sorulacak sınır tarihine kadar olan cari hareket kayıtlarını yaşlandırma (ilk borç ilk alacağa/ ilk alacak ilk borca) mantığına göre kapatır. "Yaşlandırmalı Özel Hesap Kapatma" işlemini başlatmadan önce, "Genel Kısıtlar" sekmesindeki alanların doldurulması gerekir. "Yaşlandırmalı Özel Hesap Kapatma" bölümü; Ön Sorgulama, Genel Kısıtlar, Kısıt, Sıralama, Ölçekleme ve Yazıcı Seçenekleri olmak üzere altı sekmeden oluşur.

**Ön Sorgulama**

Yaşlandırmalı Özel Hesap Kapatma ekranı Ön Sorgulama sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Yaşlandırmalı Özel Hesap Kapatma Ekranı |  |
| --- | --- |
| Cari Kodu Aralığı | Yaşlandırmalı özel hesap kapatma yapılması için cari kod aralığı kısıdının verildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile cari kodlar arasından seçim yapılır. |
| Tip | Yaşlandırmalı özel hesap kapatma işlemi için tip kısıdının verildiği alandır. Hepsi, Alıcı, Satıcı, Kefil, Toptancı, Müstahsil ve Diğer olmak üzere yedi tip seçenek bulunur. |
| Grup Kodu | Yaşlandırmalı özel hesap kapatma işlemi için grup kodu kısıdının verildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile grup kodları arasından seçim yapılabilir. |
| Kod-1/2/3/4/5 | Yaşlandırmalı özel hesap kapatma işlemi için daha önceden tanımlaması yapılan Kod-1/2/3/4/5 kısıdının verildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile kodlar arasından seçim yapılabilir. |
| İl | Yaşlandırmalı özel hesap kapatma işlemi için il kısıdının verildiği alandır. |
| İlçe | Yaşlandırmalı özel hesap kapatma işlemi için ilçe kısıdının verildiği alandır. |
| ![](../../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Yaşlandırmalı özel hesap kapatma işlemi için verilen kısıtların kaydedilmesini sağlayan butondur. |
| ![](../../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Genel Kısıtlar ve Kısıt sekmelerinde verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Yaşlandırmalı özel hesap kapatma işlemi için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki yaşlandırmalı özel hesap kapatma işleminde kullanılmak üzere saklanır. |
| ![](../../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | Yaşlandırmalı özel hesap kapatma işlemi hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) İptal | Yaşlandırmalı özel hesap kapatma işlemi için verilen kısıtların iptal edildiği butondur. |

**Genel Kısıtlar**

Yaşlandırmalı Özel Hesap Kapatma ekranı Genel Kısıtlar sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Yaşlandırmalı Özel Hesap Kapatma Ekranı |  |
| --- | --- |
| Dövizli Kapama (Evet/Hayır) | Cari hareket kayıtlarında döviz takibi yapan ve kapatma işleminin döviz tutarları bazında yapılmasını isteyen firmaların "Evet", TL tutarı bazında kapatma yapmak isteyen firmaların ise bu seçeneği "Hayır" olarak seçmesi gerekir. Dövizli parametresi "Hayır" olarak işaretlendiğinde, cari hesap kayıtlarında "Dövizli Cari" alanı işaretli olmayan cari hesapların TL tutarı bazında kapatma işlemi yapılır. |
| Sınır Tarihi | Yaşlandırmalı özel hesap kapatma işlemi, bu alana girilecek sınır tarihine kadar olan cari hareketler için yapılır. |
| Kapatma Tarih Seçimi | Kapatma işlemi için baz alınacak tarihin seçildiği alandır. Vade Tarihi ya da Hareket Tarihi seçenekleri arasından tercih yapılır. |
| Döviz | "Dövizli Kapama" alanı “Evet” olarak işaretlendiğinde aktif hale gelen alandır. Cari hareket kayıtlarında hangi döviz tipindeki hareketlerin kapatılması isteniyorsa, ilgili döviz tipinin girilmesi gerekir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, dövizler arasından seçim yapılır. Örneğin: Cari hareket kayıtlarında döviz tipi "1" olan hareketlerin kapatılması isteniyorsa, bu alana "1" rakamı girilir. Dövizli çalışıp, hareket kayıtlarında döviz tipleri olmayan hareketlerin kapatılması istendiğinde, "0" (sıfır) rakamı girilir. Dövizli özel hesap kapatma işlemi, sadece cari hesap kayıtlarında "Dövizli Cari" alanı işaretlenmiş olan cari kartlar için çalışır. Diğer cari kartlarda kapatma işlemi yapılmaz. |
| Döviz Tipi | "Döviz" alanında belirlenen döviz cinsinin, hangi döviz tipine göre yaşlandırmalı özel hesap kapatması yapılması isteniyorsa o döviz tipinin seçildiği alandır. Döviz Alış, Döviz Satış, Döviz Efektif Alış ve Döviz Efektif Satış olmak üzere dört seçenekten oluşur. |
| İçinde Bulunulan Şube Hareketleri Gösterilsin | Bu seçenek işaretlendiğinde, yaşlandırmalı özel hesap kapatma işlemi sadece içinde bulunulan şubenin hareketlerine bakılarak yapılır. |
| Proje Kodu Kırılımı | Proje kodu takibi yapıldığında aktif hale gelen alandır. Yaşlandırmalı özel hesap kapatma işleminde proje kodu kısıtı verilmek istendiğinde işaretlenmesi gerekir |
| Proje Kodu Aralığı | Yaşlandırmalı özel hesap kapatma işlemini yaparken, girilen proje kodu aralığındaki hareketler dikkate alınarak işlem yapılır. Başlangıç ve bitiş proje kodu kısıdı verilen alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, proje kodları arasından seçim yapılır. |
| ![](../../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Yaşlandırmalı özel hesap kapatma işlemi için verilen kısıtların kaydedilmesini sağlayan butondur. Butona basıldığında yaşlandırmalı özel hesap kapatma işlemi çalışır. Yaşlandırma işlemi yapıldığında aşağıdaki işlemler gerçekleşir: - "Dövizli Kapama" alanı "Hayır" olarak işaretlendiğinde, cari hesap kayıtlarındaki "Dövizli Cari" alanı işaretli olmayan hesapların hareketleri "TL" değer üzerinden kapatılır. Bu tür cari hesaplar için dövizli kapama işlemi yapılamaz.<br>- "Dövizli Kapama" alanı "Evet" olarak işaretlendiğinde, cari hesap kayıtlarındaki "Dövizli Cari" alanı işaretli olan ve döviz tipi girilmiş olan hesapların hareketleri dövizli olarak kapatılır. Verilen döviz tipi ile cari hesap kayıtlarında girilen döviz tipi aynı ise, dövizli kapatma işlemi yapılır. Eğer kapatma işleminde, cari karttaki döviz tipinin dışında bir döviz tipi verilmişse kapatma işlemi yapılamaz.<br>- "Dövizli Kapama" alanı "Evet" olarak işaretlenen ve cari hesap kayıtlarındaki "Dövizli" alanı işaretli fakat "Döviz Tipi" alanı 0 (sıfır) olarak bırakılmış cari hesaplardaki kapatma işleminin, hareketlerde bulunan döviz tipleri bazında yapılması gerekir. **Örneğin:** Bir cari hesabın hareket kayıtlarında, "Döviz Tipi" 0 (sıfır) yani TL, "Döviz Tipi" 1 ve "Döviz Tipi" 2 olan kayıtlar olduğu varsayıldığında, kapatma işlemi çalıştırılırken, "Dövizli Kapama" alanının "Evet" olarak işaretlenmesi ve 0 (sıfır) dahil tüm döviz tipleri için ayrı ayrı işlem çalıştırılması gerekir. İşlem her çalıştırıldığında, sadece verilen döviz tipine sahip hareketler kapatılır. Düzenli olarak özel kapatma işlemini kayıtlarında bulunduran firmaların, hiçbir problem yoksa bu işlemi çalıştırmalarına gerek yoktur. Çünkü, kayıtlar sırasında bir alacak/borç kaydı ile birden borç/alacak kaydı kapatılmış olabilir. Bu durumda işlem çalıştırılırsa, yapılan özel hesap kapatma kayıtları silinir ve yeniden yaşlandırma mantığı ile kapatma yapılır. Dolayısıyla, ilk yapılan özel hesap kapatma tutarlarına bir daha erişim sağlanamaz. Bu nedenle, işleme başlamadan önce yedek alınması önerilir. |
| ![](../../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Genel Kısıtlar ve Kısıt sekmelerinde verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Yaşlandırmalı özel hesap kapatma işlemi için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki yaşlandırmalı özel hesap kapatma işleminde kullanılmak üzere saklanır. |
| ![](../../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | Yaşlandırmalı özel hesap kapatma işlemi hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) İptal | Yaşlandırmalı özel hesap kapatma işlemi için verilen kısıtların iptal edildiği butondur. |

**Kısıt**

Yaşlandırmalı Özel Hesap Kapatma ekranı Kısıt sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Yaşlandırmalı Özel Hesap Kapatma Ekranı |  |
| --- | --- |
| Sahalar | Yaşlandırmalı özel hesap kapatmak için kısıt verilmesi istenen alanlar yer alır. Ekle ![](../../../../../_assets/b050fee00ab65632b16d.jpg) butonu ile istenen alanlar "kısıt verilecek sahalar" kısmına eklenir. |
| Kısıt Verilecek Sahalar | Yaşlandırmalı özel hesap kapatmak için kısıt verilen sahaların yer aldığı alandır. Çıkar ![](../../../../../_assets/a19640feaa753a52d048.jpg) butonu ile istenmeyen alanlar çıkarılır. |
| Eşit, Küçük, Küçük veya Eşit, Büyük, Büyük veya Eşit, Arasında, Benziyor, Eşit Boş, Eşit Değil, İçinde Eşit Değil | **Eşit:** İşaretlenen alanda belli bir sabit koşula göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "001" olan stok için liste alınacaksa "Eşit" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "001" girilir. Bu durumda, sadece "001" numaralı Stok Kodu için liste alınır. **Küçük:** İşaretlenen alanda belli bir değerden küçük olanlar koşuluna göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "100" olan stok için liste alınacaksa "Küçük" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" girilir. Bu durumda, "100'den küçük" numaralı Stok Kodu için liste alınır. **Küçük veya Eşit:** İşaretlenen alanda belli bir değere eşit veya küçük olanlar koşuluna göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "100" olan stok için liste alınacaksa "Küçük veya Eşit" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" girilir. Bu durumda, "100 ve 100'den küçük" numaralı Stok Kodu için liste alınır. **Büyük:** İşaretlenen alanda belli bir değerden büyük olanlar koşuluna göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "100" olan stok için liste alınacaksa "Büyük" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" girilir. Bu durumda, "100'den büyük" numaralı Stok Kodu için liste alınır. **Büyük veya Eşit:** İşaretlenen alanda belli bir değere eşit veya büyük olanlar koşuluna göre liste alınması istendiğinde kullanılan seçenektir. Örneğin; Stok Kodu "100" olan stok için liste alınacaksa "Büyük veya Eşit" seçilerek \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" girilir. Bu durumda, "100 ve 100'den büyük" numaralı Stok Kodu için liste alınır. **Arasında:** Seçilen alanla ilgili bir aralık tanımlanması istendiğinde kullanılması gereken seçenektir. Eğer belli bir başlangıç ve bitiş değeri arasında kalan değerlerle ilgili kısıt verilecekse kullanılması gereken seçenektir. Örneğin; Stok Kodu kıstasında, "Arasında" seçeneği seçilip \<tab\> tuşu ile ilerlendiğinde sağ tarafa "100" ve yine \<tab\> tuşu ile ilerlenerek altta bulunan alana "200" yazıldığı varsayılsın. Böylece stok kodu 100 ile 200 arasındaki stok kodları için liste alınır. **Benziyor:** Cari ile ilgili kayıt ararken cari hesabın ismi tam olarak bilinmiyorsa benziyor seçeneği kullanılır. Örneğin; cari hesabın isminin CANEL ya da CENEL olacağı düşünülüyorsa, bu seçeneği seçtikten sonra alanın sağ tarafındaki kayıt alanına "C_NEL" yazıldığında, raporda cari ismi "C" ile başlayan ikinci karakteri herhangi bir karakter olan fakat sonu "NEL" ile biten kayıtlar listelenir. **Eşit Boş:** Seçilen sahada hiçbir bilgi olmadığında kullanılan seçenektir. Bu seçenek alfanumerik sahalar için geçerlidir. Sıfırdan büyük veya sıfıra eşit bilgilerin aranması durumunda "Eşit", "Büyük Eşit", "Küçük Eşit" seçenekleri kullanılabilir. **Eşit Değil:** Raporda seçilen Eşit, Küçük ve Eşit, Büyük, Büyük ve Eşit, Arasında, Benziyor ve Eşit Boş seçeneklerindeki belirlemeler olumsuz (hariç) anlamını taşıyorsa "Eşit Değil" seçeneği işaretlenir. Örneğin; stok kodunda "Eşit" seçildiğinde ve "0101" kodu girildiği varsayıldığında, "Eşit Değil" seçeneği işaretlendiğinde, raporda stok kodu "0101" olanların haricindeki stokların listeleneceği anlaşılır. |
| İse/Değil ise | **İse:** Raporda seçilen Eşit, Küçük ve Eşit, Büyük, Büyük ve Eşit, Arasında ve Benziyor seçeneklerindeki belirlemeler olumlu (dahil) anlamını taşıyorsa "İse" seçeneği işaretlenir. Örneğin; stok kodunda "Eşit" seçildiğinde ve "0101" kodu girildiği varsayıldığında, "İse" seçeneği işaretlenirse, rapora stok kodu "0101" olan stokların dahil edileceği anlaşılır. **Değil İse:** Raporda seçilen Eşit, Küçük ve Eşit, Büyük, Büyük ve Eşit, Arasında ve Benziyor seçeneklerindeki belirlemeler olumsuz (hariç) anlamını taşıyorsa "Değil İse" seçeneği işaretlenir. Örneğin; stok kodunda "Eşit" seçildiğinde ve "0101" kodu girildiği varsayıldığında, "Değil İse" seçeneği işaretlendiğinde, raporda stok kodu "0101" olanların haricindeki stokların listeleneceği anlaşılır. |
| Ve/Veya | **Ve:** Seçilen sahalarda zorunlu bağlantı koşulu sağlar. **Örnek 1:** Karmaşık bir stok kodlaması olduğu varsayıldığında; Bu kodlardan iki tanesinin raporda çıkması isteniyor fakat bu iki stok kodunun ortak hiçbir özelliği yok. Bu durumda, "Stok Kodu" sahası iki kez kısıt verilecek sahalar bölümüne aktarılır. 1.Stok Kodu kıstasında eşit bağlantısı kurularak ilk stok kodu girilir ve "VE" bağlacı işaretlenir. Daha sonra 2. Stok Kodu seçilerek yine eşit bağlantısı ile diğer bir stok kodu yazılır. Böylece, raporda sadece bu iki stok koduna ait bilgi alınır. Bu seçenekte tanımlanan her koşulun olması zorunludur. Yani, tanımlanan iki stok kodundan biri bile mevcut değil ise, rapor bilgi vermez. **Örnek 2:** Grup kodu 1, Kod 1 alanı 2 ve Kod 2 alanı 3 olan stoklarla ilgili bir liste alınması istendiğinde verilen tanımlamalarda "VE" bağlacı kullanılırsa, mutlaka bu üç kısıta da sahip olan stoklar aranır ve bulunursa listelenir. Üç kısıttan herhangi birine sahip olmayan stoklar raporda listelenmez. **Veya:** Seçilen sahalarda olabilirlik koşulu sağlar. Yani, tanımlanan koşullardan biri bile sağlansa ilgili raporla ilgili bilgi alınabilir. **Örnek 1:** Grup kodu 1, Kod 1 alanı 2 ve Kod 2 alanı 3 olan stoklarla ilgili bir liste alınması istendiğinde, verilen tanımlamalarda "VEYA" bağlacı kullanılırsa, bu üç kısıttan birine bile sahip olan stoklar aranır ve bulunursa listelenir. |
| ![](../../../../../_assets/c7275efbddc154ea1579.jpg) Sakla | Yapılan tanımlamaların onaylanması için kullanılan butondur. |
| ![](../../../../../_assets/df428ea63894bc744f9a.jpg) İptal | Yapılan tanımlamaların iptal edilmesi için kullanılan butondur. |
| ![](../../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Yaşlandırmalı özel hesap kapatma işlemi için verilen kısıtların kaydedilmesini sağlayan butondur. |
| ![](../../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. > [!NOTE]<br>> **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Genel Kısıtlar ve Kısıt sekmelerinde verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. > [!NOTE]<br>> Yaşlandırmalı özel hesap kapatma işlemi için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki yaşlandırmalı özel hesap kapatma işleminde kullanılmak üzere saklanır. |
| ![](../../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | Yaşlandırmalı özel hesap kapatma işlemi hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) İptal | Yaşlandırmalı özel hesap kapatma işlemi için verilen kısıtların iptal edildiği butondur. |

Kısıt tanımlaması yapılırken açılan her parantez mutlaka kapatılması gerekir. Kapatılmadığı taktirde rapor butonu aktif olmaz.

**Sıralama**

Yaşlandırmalı Özel Hesap Kapatma ekranı Sıralama sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Yaşlandırmalı Özel Hesap Kapatma |  |
| --- | --- |
| Sahalar | Yaşlandırmalı özel hesap kapatmak için sıralanması istenen alanlar yer alır. Ekle ![](../../../../../_assets/b050fee00ab65632b16d.jpg) butonu ile istenen alanlar "sıralama sahaları" kısmına eklenir. |
| Sıralama Sahaları | Yaşlandırmalı özel hesap kapatmak için sıralama yapılacak sahaların yer aldığı alandır. Çıkar ![](../../../../../_assets/a19640feaa753a52d048.jpg) butonu ile istenmeyen alanlar çıkarılır. |
| Sıralama | Sıralamanın ne şekilde yapılacağının belirlendiği alandır. Artan ve Azalan olmak üzere iki seçenekten oluşur. **Artan:** Artan seçeneğin işaretlenmesi halinde, bilgiler küçükten büyüğe sıralı şekilde listelenir. **Azalan:** Azalan seçeneğinin işaretlenmesi halinde, bilgiler büyükten küçüğe sıralı şekilde listelenir. |
| Değişimde Toplam | Bu alan işaretlendiğinde, sıralanan bilgi her değiştiğinde ara toplam alınır. |
| Birinci Saha Değ. Baş. Saha | "Değişimde Toplam" seçeneği işaretlendiğinde, sıralanan bilgi her değiştiğinde ara toplam alınır. Bu durumda raporda, sıralı alanın içerdiği bilginin aynı kaldığı kayıt grubu için, sıralı alanın değeri başlık olarak yazılır. Başlıkların daha anlamlı olması açısından, başlık olarak sıralı alan bilgisinden daha farklı bir bilginin yazılması sağlanır. Örneğin; Sıralı Saha-1’de (grup koduna göre sıralatılan bir raporda), eğer grup kodlarının isimleri tanımlı ise (Grup Kodu Girişi bölümünden tanımlanmış ise) sıralama grup koduna göre yapılmasına rağmen, başlık olarak **grup kodu bilgisi** yerine, **grup ismi bilgisi** yazılır. Böylece grup kodlarına yabancı olan ya da bilmeyen bir kullanıcı için, raporun daha anlaşılır olması sağlanır. |
| ![](../../../../../_assets/c7275efbddc154ea1579.jpg) Sakla | Yapılan tanımlamaların onaylanması için kullanılan butondur. |
| ![](../../../../../_assets/df428ea63894bc744f9a.jpg) İptal | Yapılan tanımlamaların iptal edilmesi için kullanılan butondur. |
| Kırılımda Kayıt Sayısı | "Değişimde Toplam" alanının işaretlendiği durumlarda, her ara toplam için listelenen satır kayıt sayısının alınmasını sağlayan seçenektir. |
| Kümüle Döküm | Yaşlandırmalı özel hesap kapatmak için dökülecek bilgilerin toplam olarak tek kalemde görüntülenmesi istendiğinde işaretlenmesi gereken seçenektir. Sıralama alanlarında tanımlanan en son sahada kümülasyon yapılır. **Örneğin:** Stok hareket kayıtları ile ilgili bir rapor alındığında, "Kümüle Döküm" seçeneği işaretlenmezse o stoka ait kayıtlar hareket bazında satır satır listelenir. "Kümüle Döküm" seçeneği işaretlenirse, her bir stok koduna ait hareketler kümüle olarak tek satırda toplanır ve o şekilde listelenir. |
| ![](../../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Yaşlandırmalı özel hesap kapatma işlemi için verilen kısıtların kaydedilmesini sağlayan butondur. |
| ![](../../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Genel Kısıtlar ve Kısıt sekmelerinde verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Yaşlandırmalı özel hesap kapatma işlemi için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki yaşlandırmalı özel hesap kapatma işleminde kullanılmak üzere saklanır. |
| ![](../../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | Yaşlandırmalı özel hesap kapatma işlemi hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) İptal | Yaşlandırmalı özel hesap kapatma işlemi için verilen kısıtların iptal edildiği butondur. |

**Ölçekleme**

Standart raporlarda miktar, fiyat, tutar, kur, döviz tutarı, döviz fiyatı, firma döviz tutarı ve oran alanları için ölçekleme yapılmasını sağlayan sayfadır.

**Örneğin:** Fiyat ve tutar alanlarına 1.000 yazılması, fiyat ve tutara getirilecek verilerin 1.000'e bölüneceği anlamına gelir.

**Yazıcı Seçenekleri**

Yaşlandırmalı Özel Hesap Kapatma ekranı Yazıcı Seçenekleri sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Yaşlandırmalı Özel Hesap Kapatma Ekranı |  |
| --- | --- |
| Ekran | Raporun ekrandan alınması için işaretlenmesi gereken seçenektir. Hiçbir değişiklik yapılmaması durumunda, raporda ekran seçeneği işaretli olduğu için, rapor yine ekrandan alınır. |
| Yazıcı | Raporun yazıcıdan alınması için işaretlenmesi gereken seçenektir |
| Toplam Sayfa | Rapor yazıcıya döküldüğü zaman yazıcıdan kaç sayfa çıkarılacağının gösterildiği alandır. Kullanıcı, raporu yazıcıya göndermeden önce bu seçeneği işaretleyerek Rapor ![](../../../../../_assets/21c20c78203acae9cce6.jpg)butonuna basarsa, yazıcıya dökülecek sayfa adedi ekranda görüntülenir. ![](../../../../../_assets/b2e157c1e0713bfefb94.png) |
| Yazıcı Seçenekleri - Yönlendirme |  |
| Dikey | Raporun sadece yazıcı seçeneği ile bastırılması durumunda kullanılan seçenektir. Döküm yapılacak kağıdın genişliğine göre rapor dikey veya yatay olarak alınabilir. Bu seçenekte hiçbir değişiklik yapılmaması durumunda otomatik olarak "Dikey" işaretlenmiş olduğu için rapor dikey şekilde basılır. Ekran seçeneğinde bu parametrenin herhangi bir işlevi yoktur. |
| Yatay | Raporun sadece yazıcı seçeneği ile bastırılması durumunda kullanılan seçenektir. Döküm yapılacak kağıdın genişliğine göre rapor dikey veya yatay olarak alınabilir. Raporun kağıda yatay olarak basılması için işaretlenmesi gereken seçenektir. Ekran seçeneğinde bu parametrenin herhangi bir işlevi yoktur. |
| Yazıcı Seçenekleri |  |
| Şirket Adı | Basılsın, Basılmasın ve Detaylı Basılsın olmak üzere üç seçenekten oluşur. Yazıcıdan alınacak raporun her bir sayfasında şirket unvanının yazılması istendiğinde "Basılsın" seçeneğinin kullanılması gerekir. Şirket unvanı Yardımcı Programlar/Şirket/Şube Parametre Tanımları menüsünde tanımlandığı şekilde otomatik olarak ekrana gelir. |
| Başlık Yazılsın | Yazıcıdan alınacak raporun her bir sayfasında, tanımlanan liste başlığının yazılması istendiğinde işaretlenmesi gereken seçenektir. |
| Tarih / Saat Yazılsın | Yazıcıdan alınacak raporun her bir sayfasında sistem tarihi ve saatinin yazılması istendiğinde işaretlenmesi gereken seçenektir. |
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
| ![](../../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Yaşlandırmalı özel hesap kapatma işlemi için verilen kısıtların kaydedilmesini sağlayan butondur. |
| ![](../../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Genel Kısıtlar ve Kısıt sekmelerinde verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Yaşlandırmalı özel hesap kapatma işlemi için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki yaşlandırmalı özel hesap kapatma işleminde kullanılmak üzere saklanır. |
| ![](../../../../../_assets/4ad6cc61ca2c42a19c85.jpg) Yardım | Yaşlandırmalı özel hesap kapatma işlemi hakkında standart yardım bilgisi için kullanılan butondur. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) İptal | Yaşlandırmalı özel hesap kapatma işlemi için verilen kısıtların iptal edildiği butondur. |
