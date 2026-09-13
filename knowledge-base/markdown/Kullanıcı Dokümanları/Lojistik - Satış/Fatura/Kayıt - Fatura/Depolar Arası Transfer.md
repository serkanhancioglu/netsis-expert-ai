---
title: "Depolar Arası Transfer"
page_id: "24754705"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Fatura"
  - "Kayıt / Fatura"
  - "Depolar Arası Transfer"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Fatura / Kayıt / Fatura / Depolar Arası Transfer"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWYzNmE1MDFiLWRlY2YtNGQzOS1hZWVlLTg0YWQ4N2IzMDI1YiZsaW5rPTJhMzU5NzNkLTU3MWItNDk5NC05NzE5LWFlMTdmNzZjYWJiMiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=f36a501b-decf-4d39-aeee-84ad87b3025b&link=2a35973d-571b-4994-9719-ae17f76cabb2&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "depolar-arasi-transfer_24754712_24754705.html"
source_version: "2022-10-24T20:43:05.200+03:00"
source_bytes: 79563
fetched_at: "2026-09-13T04:02:33+00:00"
generator: "netsis-scraper 1.0.0"
---
# Depolar Arası Transfer

Depolar arası transfer bölümünde; merkez ve/veya birden fazla şube ile çalışılan durumlarda, depolar arası transfer fişlerinin kaydedilmesi, düzenlenmesi ve izlenmesi işlemlerinin gerçekleşmesi sağlanır.

Depolar Arası Transfer, Lojistik-Satış Bölümü’nde, fatura kayıt menüsünün altında yer alır. Sipariş Bilgileri, Üst Bilgiler, Kalem Bilgileri, Toplamlar sekmelerinden oluşur.

Bu sekmelerden bazıları, belirli parametrelerin işaretlenmesi sonucu ekranda yer alır.

**Sipariş Bilgileri**

Depolar Arası Transfer Sipariş Bilgileri sekmesi, sipariş takibi yapan firmalarda, müşteri siparişlerinden depolar arası transfer kaydı oluşturulması için kullanılan bölümdür. "Depolar Arası Transfer" menüsüne girildiğinde bu sekmenin ekranda yer alması için; "[Satış Parametreleri](<Satış Parametreleri.md>)" bölümünde bulunan “Depolar Arası Transferde Sipariş No Sorulsun” parametresinin işaretlenmesi gerekir. Bu bölümün kullanımı ile sipariş bağlantılı depolar arası transfer oluşturulması sağlanır.

Depolar Arası Transfer ekranı Sipariş Bilgileri sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Depolar Arası Transfer Ekranı |  |
| --- | --- |
| Belge Tipi | Sipariş ve İrsaliye seçeneklerinden oluşur. |
| Belge Numarası | Transfer yapılacak siparişin belge numarasının seçildiği alandır. ![](../../../../_assets/088477bb321d1b20c939.jpg) Rehber butonu ile seçim yapılabilir. |
| ![](../../../../_assets/2636d38991826c806649.jpg) Depolar Arası Transfer Butonu | Sipariş belge numarası ile depolar arası transfer işlemini gerçekleştirmek için kullanılan butondur. Butona basılması ile birlikte "Sipariş teslimatınız yapılsın mı?" sorulu ekran görüntülenir. Bu ekranda "Yeni Numara" ve "Giden Depo" alanları doldurulduktan sonra "Tamam" butonuna basılması ile birlikte "Üst Bilgiler" sayfasına geçilir. |
| Detaylı Sipariş/İrsaliye Rehberi Cari Kodu | Transferi yapılacak sipariş belgesine kısıt vermek için kullanılan alandır. Transferin oluşturulması aşamasında, sipariş bilgilerinin detaylandırılarak girildiği müşterinin kodudur. ![](../../../../_assets/088477bb321d1b20c939.jpg) Rehber butonu ile cari kod seçimi yapılır. |
| Detaylı Sipariş / İrsaliye Rehberi Belge Numarası | Transferin oluşturulacağı sipariş numarasının girildiği alandır. Tek bir siparişe ait transfer işlemi yapılacaksa bu bölüm kullanılabilir. Cari kodun girilip bu alanın boş geçilmesi halinde, ilgili cariye ait tüm siparişler listelenir. |
| Mal Detaylı Mı? | “Mal detaylı mı?” sorusu işaretlendiğinde, müşterinin kalan siparişleri mal bazında detaylı listelenir. İşaretlenmediğinde, belirlenen cari koda ait, teslimi yapılmamış (kalan) sipariş numaralarının yer aldığı liste üzerinden, istenilen siparişler farenin sol tuşu çift tıklanarak işaretlenebilir. Böylece faturalama işlemlerinde siparişler birleştirilerek faturalandırılabilir fakat mal detayları izlenemez. |
| Stok Kısıdı Verilebilsin | Ekranın altında listelenecek sipariş kalemleri için kısıt verilmesi amacıyla kullanılan seçenektir. Bu seçeneğin aktif olması için “Mal Detaylı Mı?” sorusunun işaretlenmesi gerekir. “Stok Kısıdı Verilebilsin” seçeneği işaretlendikten sonra “Belgeleri Getir” butonuna basıldığında, listelenecek sipariş kalemlerinin belirlenmesi için “Stok Kısıt Ekranı” gelir. Bu ekranda bulunan **Saha** **Adı** sütunundaki hücreye tıklandığında, stok ilişkili alanlar listelenir. Bu listede, kısıt verilecek alan seçildikten sonra, “Operatör” ve “Değer” alanları kullanılarak istenen kısıt verilir. |
| Sıralama | Belge no, teslim tarihi, koşul kodu, belge tarihi, stok kodu, stok adı seçeneklerini içerir. Listelenecek sipariş belgelerinin seçilecek alanlara göre sıralanmasını sağlar. |
| Belgeleri Getir | Cari kod ve mal detayı bilgileri baz alınarak, sipariş belgelerinin listelenmesini sağlayan butondur. |

**Üst Bilgiler Ekranı**

Depolar Arası Transfer ekranı Üst Bilgiler sekmesi, transfere ait sabit ve cari bilgi alanlarının yer aldığı ekrandır.

Depolar Arası Transfer ekranı Üst Bilgiler sekmesinde yer alan alanlar ve içerdiği bilgiler şunladır:

| Depolar Arası Transfer Ekranı |  |
| --- | --- |
| İrsaliye No | Depolar Arası Transfer fişine ait numaranın girildiği alandır. ![](../../../../_assets/088477bb321d1b20c939.jpg) Rehber butonu ile irsaliye numaraları arasından seçim yapılabilir. |
| Hareket Türü | İşlem sonunda oluşacak stok hareket kayıtlarının hareket tipinin belirlendiği alandır. Bu alanda A- Devir, B- Depolar, C- Üretim, D- Muhtelif F- Konsinye tiplerinden biri seçilir. Seçilen tipe göre, stok hareket kayıtlarında bulunan "Tip Sahası" değişir. Stok hareketlerindeki hareket tipleri, hem raporlarda ayrı tipteki hareketleri gruplandırabilmek açısından, hem de tiplerin ayrı ayrı icmallerini alabilmek açısından önemlidir. |
| Lokal Depo | Yapılacak transfer işlemi lokal depolar arası ise işaretlenecek alandır. Bu durumda "Gideceği Depo, Ambar ve Cari Kod" alanları pasif olur. Eğer şubeler arası bir transfer işlemi yapılacak ise bu seçenek işaretlenmemelidir. |
| Gideceği Depo | Şubeler arası transfer işlemlerinde kullanılan alandır. Bu alanda transferin nereye yapılacağı belirlenir. Alanın sağ tarafında bulunan aşağı ok işaretine basıldığında, şube kodları listelenir. Transferin yapılacağı şube kodu bu alandan seçilir. Şube kodu 0 (sıfır) merkez anlamındadır. Yani, herhangi bir şubeden merkeze transfer işlemi yapılacak ise bu alanda 0 (sıfır) seçilmesi gerekir. |
| Ambar | Transferin yapılacağı şube için açılan cari kod bilgisinin girildiği alandır. Yani "şube 1’e" transfer yapılıyor ise bu alana "şube 1" için açılan cari kod girilmelidir. Bu cari kod, işlemin yapıldığı merkez veya şubenin stok hareket kayıtlarındaki açıklama alanına aktarılır. ![](../../../../_assets/088477bb321d1b20c939.jpg) Rehber butonu ile cari kodlar arasından seçim yapılabilir. |
| Cari Kodu | Transferin yapıldığı (işlemin yapıldığı) yer için açılan cari kod bilgisinin girildiği alandır. Yani transfer işlemi merkezden yapılıyor ise bu alana merkez için açılan cari kod girilir. Bu cari kod, transferin yapıldığı merkez veya şubenin stok hareket kayıtlarındaki açıklama alanına aktarılır. ![](../../../../_assets/088477bb321d1b20c939.jpg) Rehber butonu ile cari kodlar arasından seçim yapılabilir. |
| Tarih | Depolar arası transfere ait tarihin girildiği alandır. Günün tarihi, otomatik olarak bu ekrana gelir. Bu tarih aynı zamanda stok hareketlerine işlenecek olan kayıt tarihidir. |
| Fiili Tarih | Depolar arası transferlerin gerçekleştiği tarihin girildiği alandır. Rapor amaçlı bir alandır. |
| Döviz Baz Tarihi | Oluşturulacak irsaliyede geçerli olacak kur bilgisinin belirlendiği alandır. Bu alana Döviz Takibi/Döviz Kurları Girişi bölümünden girilen kur tutarı, Kalem Bilgileri sayfasındaki stok bazında sorgulanan kur tutarı alanına yansır. |
| Özel Kod 1 | Tanımlanan Özel Kod 1 seçenekleri arasından, ![](../../../../_assets/088477bb321d1b20c939.jpg) Rehber butonu ile seçim yapılarak transferlerin belli kodlar altında gruplanmasını sağlayan alandır. |
| Özel Kod 2 | Tanımlanan Özel Kod 2 seçenekleri arasından, ![](../../../../_assets/088477bb321d1b20c939.jpg) Rehber butonu ile seçim yapılarak transfer kayıtlarının rapor bazında gruplanmasını sağlayan alandır. |
| Açıklama | Transfere ait açıklama bilgisinin girildiği alandır. |
| Proje Kodu | Tanımlanan proje kodları arasından,![](../../../../_assets/088477bb321d1b20c939.jpg) tuşu ile seçim yapılarak, istenildiğinde proje bazında rapor alınabilmesi için girilen koddur. Bu alana girilen proje kodu kalem bilgilerine aktarılır. Boş geçilemez. |
| Plasiyer Kodu | Tanımlanan plasiyer kodları arasından,![](../../../../_assets/088477bb321d1b20c939.jpg) tuşu ile seçim yapılarak, ilgili müşteriye ait plasiyer kodunun girildiği alandır. |
| KDV Dahil | KDV'nin nasıl uygulanacağının belirlendiği alandır. KDV dahil kutucuğu işaretlendiği takdirde, stoka ait birim fiyatı, KDV tutarını da içerir. |
| Toplu Çıkış Depo | Toplu depo kodu tanımlamasının yapıldığı durumlarda kullanılan alandır. Bu alana girilen depo kodu, "Kalem Bilgileri" sayfasındaki her stok kalemi için "Çıkış Depo" alanına otomatik olarak gelir. |
| Toplu Giriş Depo | Toplu depo kodu tanımlamasının yapıldığı durumlarda kullanılan alandır. Bu alana girilen depo kodu, "Kalem Bilgileri" sayfasındaki her stok kalemi için "Giriş Depo" alanına otomatik olarak gelir. |
| Nakliye Katsayısı | Tanımlanan nakliye katsayısı girişinin yapıldığı alandır. |
| Değişsin | Dövizli belgelerde bazen (yuvarlama kaynaklı) döviz fiyatının, kurun ya da TL fiyatının değişmesi gerekebilir. Bu gibi durumlarda hangi alandaki bilginin değişeceğinin belirlendiği alandır. |
| Giriş Depo | Ambar alanına girilen şubenin, cari koduna ait isim bilgisinin otomatik olarak ekrana geldiği alandır. |
| Çıkış Depo | "Cari Kod" alanına girilen şubenin, cari koduna ait isim bilgisinin otomatik olarak ekrana geldiği alandır. |
| Ek Saha Açıklamaları | Cari kod girildikten sonra açıklama alanlarının başlığı olarak parametrede girilen başlıklar ekrana gelir. İstenilen ya da gerekli olanlar kaydedilir. İsteğe bağlı olarak boş bırakılabilir. Bu ekrandaki satırlara yapılan açıklamalar saklanarak daha sonra izlenebilir ve Rapor Modülü/Fatura Raporları bölümünden listelenebilir. |

Özel Kod-1, Özel Kod-2, Açıklama, Plasiyer Kodu, Proje Kodu, KDV Dahil, Toplu Depo, Nakliye Katsayısı, Açıklama-1 Açıklama-2 Açıklama 3 ve Ek Sahalardan oluşan alanlar, **Satış Parametreleri sayesinde** isteğe bağlı olarak ekranda yer alabilir/almayabilir.

**Kalem Bilgileri**

Depolar Arası Transfer ekranı Kalem Bilgileri sekmesi; Kalem Girişi, Açıklama ve Kalem Listesi alanlarının yer aldığı ekrandır.

Depolar Arası Transfer ekranı Kalem Bilgileri sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Depolar Arası Transfer Ekranı |  |
| --- | --- |
| Kod | Tanımlaması yapılan stok kaleminin, ![](../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu ile seçim yapılarak ekrana getirildiği koddur. |
| İsim | Stok sabit kayıtlarında kaydedilen stok isminin, program tarafından ekrana getirildiği alandır. |
| İş Emri No | Depolar Arası Transfer kaydının, Üretim/İş Emri Girişi bölümünden oluşturulan mamul/yarı mamul iş emirleri için yapılması halinde, ilgili iş emrine ait numaranın girileceği alandır. Buraya girilen iş emrindeki miktar bilgisi , otomatik olarak miktar alanına aktarılır. |
| Sipariş No | Her malın ayrı ayrı sipariş numarasının girilmesini sağlamak için kullanılan alandır. ![](../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu ile stoklar için girilmiş tüm siparişlere ulaşılarak seçim yapılır. Transfer, sipariş bağlantılı yapılmayacak ise, bu alan boş bırakılarak \<tab\> tuşu ile ilerlenir. Sipariş numarası olmadığı ya da yanlış girildiği durumlarda, program “**Sipariş Bulunamadı**” şeklinde bir uyarı verir. Sipariş bulunduğu zaman, o siparişle ilgili teslimi bekleyen mallar, kalan miktarları ve sipariş tutarlarıyla birlikte otomatik olarak ekrana gelir. |
| D.Kd (Depo Kodu) | Çıkış yapılacak depo kodunun, ![](../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu ile depo seçimi yapılarak, her malın ayrı ayrı depolarda takip ve raporlanmasını sağlamak amacıyla kullanılan alandır. |
| G.KD (Giriş Depo Kodu) | Depolar Arası Transfer kaydının lokal depolar arasında yapılması halinde, hangi depoya transfer (depoya giriş) yapılacağının belirlendiği alandır. Depolar Arası Transfer kaydı şubeler arasında yapılıyor ise, transfer yapılan şubede bulunan depolardan hangisine transfer yapılacağı bu alanda belirlenir. Depo kodu sahasında bulunan ![](../../../../_assets/088477bb321d1b20c939.jpg) rehber butonuna basılarak tanımlı lokal depolardan biri seçilir ve bu alan boş bırakılamaz. |
| Yapılandırma Kodu | Esnek yapılandırma uygulamasının kullanıldığı durumlarda, stoka ait yapılandırma kodunun girildiği alandır. |
| Yapılandırma Kodu Açıklaması | Yapılandırma kodu alanına girilen değere ait açıklama bilgisinin, program tarafından getirildiği alandır. |
| Yapılandırma Kod Sihirbazı | Belirli bir özellik kombinasyonu içeren yapılandırma kodunun, sistemde tanımlı yapılandırma kodları arasında olup olmadığını saptamak ve tanımlı değilse de hızlı tanımlama yapmak amacıyla kullanılan alandır. |
| Yapılandırılabilir Ürün Girişi | Birden fazla yapılandırma koduna ait çıkış miktarlarının, tek seferde kaydedilmesi için kullanıldığı alandır. |
| Tes.Cari Kod (Teslim Cari Kodu) | Transferin yapıldığı cari hesap/adres ile, stokların teslim edileceği cari hesap/adresin farklı olması halinde, teslimatın yapılacağı cari hesap/adresin girileceği alandır. |
| Satır Açıklama | Her kalem için, 10 ayrı ek açıklama girişinin yapılabileceği alandır. |
| Ç.Değ (Çevrim Değeri) | Stok kodu alanına girilen stoka ait, birden fazla ölçü birimi tanımlanmışsa, hangi ölçü birimi üzerinden miktar girileceğinin belirlendiği alandır. Alanın sağ tarafında bulunan aşağı ok tuşuna basılarak, o stok için tanımlanmış olan ölçü birimi seçilir. Girilen miktar otomatik olarak ölçü birimi değerine çevrilir ve sistem tarafından ekrana getirilir. Alanın sağ tarafında bulunan rehber, stokun bir ölçü birimine ait birden fazla çevrim değeri olması halinde çevrimin hangi değere göre yapılacağını seçmek amacıyla kullanılır. |
| Seri Takibi | Transferlerin, seri numaralarına göre takibinin yapılması amacıyla kullanılan alandır. |
| Miktar 2 | Stok bazında takibin yapıldığı miktar alanıdır. Karma koli uygulamasının kullanıldığı durumlarda, koli stokuna ait miktar girişi için de kullanılır. |
| Fiyat Birim | Transferdeki stok kalemlerinin kaydı sırasında, fiyat girmeden önce, eğer ilgili mal için stoklarda birden fazla ölçü birimi tanımlanmışsa (adet, kg, koli v.s), gireceğiniz fiyatın hangi ölçü birimine ait olduğunun seçildiği alandır. |
| Ek Alan-1 | Transfer basımına yönelik, anlık açıklamaların girildiği alandır. |
| Ek Alan-2 | Transfer kaydı girilirken stok kalemleri bazında ikinci bir açıklamanın gerekliliği halinde kullanılan alandır. Her bir kalem için en fazla 14 karakter uzunluğunda açıklama girilir. |
| Miktar | İlgili stok kaleminin transfer miktar girişinin yapıldığı alandır. |
| M. Faz ( Mal fazlası) | Transferi olacak malın yanında verilen hediye malların gösterilmesi için kullanılan alandır. Burada hediye verilen miktar girilmelidir. Eğer transfer edilecel malın yanında hediye verilen mal farklı ise, miktar hanesine gerekli değer yazılır, mal fazlası hanesi boş bırakılır. Bir sonraki satıra hediye olarak verilen malın kodu yazılır ve bu mal için de miktar hanesi boş bırakılarak, mal fazlası hanesine hediye miktarı girilmesi ile kayıt oluşturulur. |
| Dv. Tip (Döviz Tip) | Döviz takibinin yapıldığı alandır. Girilen stok kodu için, tanımlaması yapılan döviz satış tipi değeri, program tarafından ekrana getirilir. Bu alana getirilen değer, isteğe bağlı olarak farklı bir döviz tipi ile de değiştirilebilir. Döviz tipi olarak “0“ dan farklı bir değer seçilirse, ilgili kalemin dövizli olarak satıldığı, “0“ değeri seçilirse de TL olarak satıldığı anlaşılır. |
| Döviz Fiyat | Girilen stok kodu için, tanımlaması yapılan döviz fiyat değeri, otomatik olarak ekrana gelir. İsteğe bağlı olarak, bu alana getirilen fiyat değiştirilebilir. |
| Döv.Kur | Üst bilgiler ekranında girmiş olduğunuz **Döviz Baz Tarihi** ile, **Döviz Takibi/Günlük Kur Girişi Bölümü’nden** girmiş olduğunuz kur tutarı, **Döviz Kur** alanına yansır. İsteğe göre değişiklik yapılabilir. Kur tutarı ile döviz fiyatı alanındaki değerlerin çarpımı sonucu çıkan rakam, fiyat alanına yansır. |
| Fiyat | İlgili malın birim fiyatıdır. |
| KDV | Kdv oranının girildiği alandır. |
| Proje Kodu | Yapılan transferin proje bazında izlenmesini sağlayan alandır. ![](../../../../_assets/088477bb321d1b20c939.jpg) Rehber butonu ile ilgili proje seçimi yapılır. Örneğin, firmaya ait, farklı bir konumda yeni bir bina inşa edilmesi durumu bir projedir. Projeye ait bir kod tanımlar ve ilgili projeye ait transferlerde bu kod seçilerek kayıt yapılırsa, gerekli olduğunda **söz konusu projeye ait** transferleri bu kod sayesinde raporlayabilirsiniz. |
| Fiili Tarih | Üst Bilgiler sayfasında bulunan fiili tarih bilgisinin, kalem bilgilerine yansıtıldığı alandır. İsteğe bağlı olarak değiştirilebilir. |
| Tutar | Stok miktarı ile birim fiyatın program tarafından çarpılıp, brüt tutar olarak yazıldığı alandır. Bu alana müdahale edilemez. Sadece birim fiyat ve miktar hanelerinde yapılan değişiklikler tutarın değişmesine sebep olur. Faturada girilen tüm stok tutarlarının toplamı, ekranın sağ alt köşesinde bulunan **Toplam Tutar** alanında görünür. |
| Top. Mik. (Toplam Miktar) | Sipariş/irsaliye bağlantılı transfer oluşturulduğunda, ilgili stok kalemi için seçilen sipariş/irsaliye kalemindeki miktar bilgisinin program tarafından ekrana getirildiği alandır. |
| Sip. Nolar (Sipariş Numaraları) | Sipariş bağlantılı transfer oluşturulduğunda, ilgili sipariş numarasının izlendiği alandır. |
| İrs. Nolar (İrsaliye Numaraları) | İrsaliye bağlantılı transfer oluşturulduğunda, ilgili irsaliye numarasının izlendiği alandır. |
| Bakiye | Transfer kaydında girilen her stok kodu için, ilgili malın stok hareket kayıtlarındaki bakiyesinin, bilgilendirme amacıyla program tarafından ekrana getirildiği alandır. |

**Toplamlar**

Depolar Arası Transfer ekranı Toplamlar sekmesi; İskonto ve Maliyet Toplamları, KDV'ler Toplamı ve Genel Toplam, Kayıt Sorgulamaları alanlarının yer aldığı ekrandır.

Depolar Arası Transfer ekranı Toplamlar sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Toplamlar Ekranı | İskonto ve Maliyet Toplamları |
| --- | --- |
| Brüt Toplam | Transferde kaydedilen mal tutarlarının, iskonto düşülmeden önceki brüt tutarını gösteren alandır. Kalem bilgileri ekranındaki bilgilere göre oluşturulan bir alan olduğu için, elle değiştirme yapılamaz. Buradaki tutarın yanlış olması durumunda, önceki ekrana (kalem bilgileri) geçilerek gerekli düzeltme işlemleri yapılmalıdır. |
| Ek Maliyet 1,2 | İlave maliyetlerin girildiği alandır. Hesaplatılan bir değer yoksa, elle tutar girilebilir. |
| Yuvarlama | Transferi yapılacak malların genel toplamının yuvarlanması için kullanılan alandır. |
| Br. 1 Miktar, Br.2 Miktar, Br. 3 Miktar | Kalem Bilgilerinde girilen tüm stokların toplam miktar bilgilerinin, stok kartı kayıtlarında tanımlı birinci, ikinci ve üçüncü ölçü birimi cinsinden izlenen alandır. |
| Toplamlar Ekranı | KDV’ler Toplamı ve Genel Toplam |
| Ara Toplam | Yukarıda anlatılan iskontolar toplamının brüt toplamdan düşülüp, ek maliyet toplamlarının eklenmesiyle oluşan toplamdır. Bu alana elle müdahale edilemez. Bilgilendirmek amacıyla görüntülenen alandır. |
| KDV 1,2,3,4,5 | Sipariş kaydında girilen stok kalemlerinin, stok sabit kayıtlarında yazılı KDV oranına göre, program tarafından otomatik hesaplanarak ekrana getirildiği alandır. |
| KDV % | KDV hesaplamalarında kullanılan oranların izlendiği alandır. |
| Toplam KDV | Farklı KDV oranları üzerinden hesaplanan tutarların toplamının yazıldığı alandır. Hesaplanan değer üzerinde çok küçük bir farklılık olması halinde düzenleme yapılmasını, aksi halde bu değerin değiştirilmemesi tavsiye edilir. Burada yapılacak düzeltme, yukarıda anlatıldığı şekilde hesaplanan KDV tutarları dağılımına yansımaz. Yapılan değişiklik, sadece aşağıdaki genel toplam alanına yansır. Fatura/ Kayıt/Satış Fatura Parametreleri Bölümü’nde “KDV Maliyete Eklensin” parametresi işaretlenmiş ise, bu alanda oluşan tutar muhasebeye entegre olmaz. Stok fiyatlarına KDV tutarları eklenerek stok hareket kayıtlarına aktarılır. |
| Genel Toplam | Yukarıda anlatılan işlemler sonucu oluşan son toplamın gösterildiği alandır. Bu tutar üzerinde değişiklik yapmak yerine "Karşı Toplam" alanı kullanılır. |
| Karşı Toplam | Transfer kaydı genel toplam alanında değişiklik yapılması istendiğinde kullanılan alandır. |
| Resim Alanı | Transfere resim yada doküman dosyası eklemek için kullanılan alandır. |
| Toplamlar Ekranı | Kayıt Sorgulamaları |
| Toplam Mal Ağırlığı | Transfer kaydında girilen stok kalemleri için, “Stok Kartı Kayıtlarında” birim ağırlık tanımlaması ile aktif olan alandır. Program bu ağırlıkları, faturadaki miktarlarla çarparak toplam mal ağırlığını hesaplar ve otomatik olarak ekrana getirir. |
| Basım | Girilen siparişin basımı için işaretlenen alandır. Bu alan işaretlendikten sonra “Tamam” butonuna basıldığında, “Dizayn Sorgulama” ekranından dizayn tipi ve yazıcı seçilerek basım yapılır. |
| Sıralama Seçeneği | Basımı yapılacak olan sipariş kalemlerini, bu alanda bulunan seçeneklere göre sıralatmak amacıyla kullanılan alandır. |
| Tamam | Bilgileri girilen transferin kaydı için kullanılan butondur. Tamam ![](../../../../_assets/23043a6798351fd813b5.png)butonuna basıldığında, siparişe ilişkin kayıtlar ilgili entegre bölümlere aktarılır. Transferin daha önce kaydedilmiş olması ve düzenlenip tekrar kaydedilmesi durumunda, entegre bölümlerden stok ve cari bölümlere işlenen hareketler program tarafından düzenlenir. Bu kayıtlar, Entegrasyon/Entegrasyon Kayıtlarında “ 2 no.lu " (Düzeltilmiş Kayıt) ya da “4 no.lu " (Düzeltilmiş Bulunamadı) tipte izlenebilir. |

**Depolar Arası Transfer Kaydı, Değişikliği, İptali**

Depolar Arası Transfer kaydındaki alanlara bilgi girişi yapıldıktan sonra belgenin kaydedilmesi için; "Toplamlar" sayfasındaki "Tamam" butonuna basılması gerekir. Lokal depolar arası transfer işlemi yapıldığında "Stok Hareket Kayıtlarında" bir çıkış bir de giriş hareketi oluşur. Şubeler arası transfer işlemi yapabilmek için hem merkez hem de şubeler için birer cari kod açmak gerekir.

Daha önceden kaydedilmiş belge üzerinde değişiklik yapmak için; "Üst Bilgiler" sayfasında ilgili depolar arası transfer belgesinin numarası girilmesi ve \<tab\> butonuna basılması gerekir. Böylece kayıtlı belgeye ait daha önceden girilmiş bilgiler ekrana gelir. Bundan sonra değiştirilmek istenen alan üzerinde değişiklik yapılabilir. Belge üzerinde değişiklik yapıldıktan sonra, belge ile ilgili entegre bölümlerde de gerekli değişikliklerin otomatik olarak yapılabilmesi için "Toplamlar" sayfasından tekrar kaydedilmesi gerekir.

Kaydedilmiş bir depolar arası transfer fişinin iptali için; "Üst Bilgiler" sayfasında iken araç çubuklarında bulunan ![](../../../../_assets/2df4b343310bcd16b01e.jpg)Kayıt Sil butonuna ya da klavyedeki F7 butonuna basıldığında, “Bu ekrana ait tüm bilgileriniz silinecektir. Emin misiniz?” şeklinde bir uyarı ekrana gelir. Bu ekranda "Evet" butonuna basılması halinde, ilgili fişe ait bilgiler silinir.

Depolar Arası Özel Tuşların Kullanımı İçin; [Satış Faturasında Kullanılan Özel Tuşlar](<Satış Faturası/Satış Faturasında Kullanılan Özel Tuşlar.md>).
