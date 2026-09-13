---
title: "Ambar Giriş Fişi"
page_id: "24754932"
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
  - "Ambar Giriş Fişi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Fatura / Kayıt / Fatura / Ambar Giriş Fişi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTc4NmViODVjLWMyMDEtNGJjZC05MWQ4LWIxNGQ2MjIxNWM4NiZsaW5rPWIwOGJjM2RkLTczOGEtNGI2MS05MDE3LWQ0NDI0ODIzNTM0YSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=786eb85c-c201-4bcd-91d8-b14d62215c86&link=b08bc3dd-738a-4b61-9017-d4424823534a&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ambar-giris-fisi_24755127_24754932.html"
source_version: "2022-10-24T20:55:20.587+03:00"
source_bytes: 182302
fetched_at: "2026-09-13T04:02:35+00:00"
generator: "netsis-scraper 1.0.0"
---
# Ambar Giriş Fişi

Ambar Giriş Fişi bölümünde; cari hesaplarla ilgisi olmayan, muhasebeye faturasız genel gider/gelir kayıtlarının yapılması, stoklarla bağlantılı ambar giriş fişlerinin kaydedilmesi, önceden girilmiş fişlerin izlenmesi, düzenlenmesi ve kayıt sonunda fiş basımının yapılmasını sağlar.

Ambar Giriş Fişi, Lojistik-Alış Bölümü’nde, fatura kayıt menüsünün altında yer alır. Ambar Giriş Fişi; Sipariş Bilgileri, Üst Bilgiler, Kalem Bilgileri ve Toplamlar sekmelerinden oluşur.

Bu sekmelerden bazıları, belirli parametrelerin işaretlenmesi sonucu ekranda yer alır.

Ambar Giriş Fişlerinin kullanılması için öncelikle bazı tanımlamaların yapılması gerekir. Bu fişin kaydı sonucu, stoklara ve istenirse muhasebe hesaplarına hareket kayıtları işleneceği için, bu muhasebe hesaplarının hangileri olduğu, Fatura → İşlemler → [Masraf Merkezi Tanımlama](<../İşlemler - Fatura/Masraf Merkezi Tanımlama.md>) bölümünde belirlenir.

Masraf merkezi ile ilgili detaylı bilgi için; Fatura → İşlemler → [Masraf Merkezi Tanımlama](<../İşlemler - Fatura/Masraf Merkezi Tanımlama.md>) dokümanına bakılabilir.

Fiş kaydı sırasında giriş hareketleri muhasebede hangi hesaba işlenecekse, söz konusu hesap için tanımlanan masraf merkezinin girilmesi gerekir.

**Sipariş Bilgileri**

Ambar Giriş Fişi ekranı Sipariş Bilgileri sekmesi, siparişe ait ambar giriş fişi oluşturmak için tüm bilgilerin en baştan tekrar girilmesi yerine, daha önceden girilen müşteri siparişlerinden giriş fişi oluşturulmasını sağlar.

Ambar Giriş Fişi ekranı Sipariş Bilgileri sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Ambar Giriş Fişi Ekranı |  |
| --- | --- |
| Belge Tipi | Sipariş ve İrsaliye seçeneklerinden oluşur. |
| Belge Numarası | Ambar giriş fişi oluşturulacak belge numarasının seçildiği alandır. ![](../../../../_assets/088477bb321d1b20c939.jpg) Rehber butonu ile seçim yapılabilir. |
| Teslim Cari Kodu | Sipariş veya irsaliyenin teslim edildiği yerin, ![](../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu ile seçim yapılarak girildiği cari kod alanıdır. Ambar girişı yapılan cari hesap/adres ile, stokların teslim edileceği cari hesap/adresin farklı olması halinde kullanılır. |
| ![](../../../../_assets/6cc8efad4b6180353095.jpg) Ambar Giriş Fişi | Ambar giriş fişi butonuna basıldığında "Sipariş teslimatınız yapılsın mı?" sorulu ekran gelir. ![](../../../../_assets/b777d29a1acb695d6b41.png) Siparişe ait belgelerin yer aldığı listeye yeni numara, tarih, giriş yeri türü ve masraf kodu bilgisi girilerek giriş fişi oluşturulur. |
| Detaylı Sipariş / İrsaliye Rehberi Cari Kodu | Ambar giriş fişi oluşturulacak sipariş veya irsaliye belgelerine kısıt vermek için kullanılan alandır. giriş fişinin oluşturulması aşamasında, sipariş bilgilerinin detaylandırılarak girildiği müşterinin kodudur. ![](../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu ile cari kod seçimi yapılır. |
| Detaylı Sipariş / İrsaliye Rehberi Belge Numarası | Ambar giriş fişinin oluşturulacağı sipariş numarasının girildiği alandır. Tek bir siparişe ait ambar giriş işlemi yapılacaksa bu bölüm kullanılabilir. Cari kodun girilip bu alanın boş geçilmesi halinde, ilgili cariye ait tüm siparişler listelenir. |
| Mal Detaylı Mı? | “Mal detaylı mı?” sorusu işaretlendiğinde, müşterinin kalan siparişleri mal bazında detaylı listelenir. İşaretlenmediğinde, belirlenen cari koda ait, teslimi yapılmamış (kalan) sipariş numaralarının yer aldığı liste üzerinden, istenilen siparişler farenin sol tuşu çift tıklanarak işaretlenebilir. Böylece ambar giriş işlemlerinde siparişler birleştirilerek fiş oluşturulabilir fakat mal detayları izlenemez. |
| Stok Kısıdı Verilebilsin | Ekranın altında listelenecek sipariş kalemleri için kısıt verilmesi amacıyla kullanılan seçenektir. Bu seçeneğin aktif olması için “Mal Detaylı Mı?” sorusunun işaretlenmesi gerekir. “Stok Kısıdı Verilebilsin” seçeneği işaretlendikten sonra Belgekeri Getir ![](../../../../_assets/f4340e22c274b630f96a.jpg) butonuna basıldığında, listelenecek sipariş kalemlerinin belirlenmesi için “Stok Kısıt Ekranı” gelir. Bu ekranda bulunan **Saha** **Adı** sütunundaki hücreye tıklandığında, stok ilişkili alanlar listelenir. Bu listede, kısıt verilecek alan seçildikten sonra, “Operatör” ve “Değer” alanları kullanılarak istenen kısıt verilir. |
| Sıralama | Belge no, teslim tarihi, koşul kodu, belge tarihi, stok kodu, stok adı seçeneklerini içerir. Listelenecek sipariş/irsaliye belgelerinin seçilecek alanlara göre sıralanmasını sağlar. |
| ![](../../../../_assets/f4340e22c274b630f96a.jpg) Belgeleri Getir | Cari kod ve mal detayı bilgileri baz alınarak, sipariş belgelerinin listelenmesini sağlayan butondur. |

**Üst Bilgiler**

Ambar Giriş Fişi ekranı Üst Bilgiler sekmesi, ambar giriş fişine ait sabit ve cari bilgi alanlarının yer aldığı ekrandır.

Ambar Giriş Fişi ekranı Üst Bilgiler sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Ambar Giriş Fişi Ekranı |  |
| --- | --- |
| Fiş No | Ambar giriş fişinin programdaki takip numarasıdır. ![](../../../../_assets/088477bb321d1b20c939.jpg) Rehber tuşu kullanılarak numaralar arasından seçim yapılabilir. |
| Hareket Türü | Fiş kaydı sonucunda oluşturulacak stok hareket kayıtlarındaki hareket tipinin ne olacağının (B-Depolar arası transfer, C-Üretim, D-Muhtelif, F-Konsinye tiplerinden biri) belirlendiği alandır. Stok hareketlerindeki hareket tipleri, hem raporlarda ayrı tipteki hareketleri gruplandırabilmek açısından, hem de tiplerin ayrı ayrı icmallerinin alınabilmesi açısından önemlidir. Örneğin, Üretim modülü kullanılıyorsa ve yapılacak giriş, üretim işleminde sarf edilen malzeme dışı bir gider ise burada **C-Üretim** hareket tipi seçilir. Burada **B-Depolar arası transfer** tipi seçilse bile, işlem bir depodan diğerine transfer şeklinde çalışmaz, sadece bir ambardan giriş yapılır ve stok hareketlerine hareket tipi olarak işlenir. |
| Giriş Yeri | Ambar girişi yapılan malların gideceği yeri belirlemek için kullanılır. Alanın sağ tarafında yer alan aşağı ok tuşu yardımı ile çıkış yeri seçimi yapılır. Çıkış yerleri şunlardır; **A** Devir, **B** Depolar, **C** Üretim, **D** Muhtelif, **F** Konsinyedir. Örneğin; "Maliyet Muhasebesi" modülünü kullananlar için bu bölümden yapılan hammadde sarflarının, hangi maliyet grubuna ait olduğu bu alanda belirlenir. |
| Masraf Kodu | Bu bölümden yapılan kayıtlar, stok ve muhasebe hesaplarına işleneceği için müşteri/satıcı kodu sorgulaması yapılmaz. Bunun yerine giriş yeri sorgulanır. Burada "Fatura/Masraf Merkezi Tanımlama" bölümünden tanımlanmış olan masraf kodlarından biri veya "Maliyet Muhasebesi" bölümünden tanımlanmış maliyet ana veya grup kodu girilmelidir. Masraf kodu girildiğinde, tanımlanmış olan karşılık muhasebe hesap kodu ve açıklaması ekranın sağ tarafında bulunan "GİRİŞ" bölümünde görüntülenir. Ambar giriş fişinin "Kalem Bilgileri" sayfasında yer alan "Masraf Kodu" alanından sonra satır bazında muhasebe kodu sorgulanır ve "Üst Bilgiler" sayfasında girilen masraf kodunun karşılık muhasebe kodu otomatik olarak bu alana aktarılır. Fakat mal bazında gider yazılacak hesap kodu değişkenlik gösteriyorsa, bu kod üzerinde gerekli düzenleme yapılıp, o malla ilgili muhasebe kaydının girildiği hesap kodunda oluşması sağlanabilir. Maliyet ana ve grup kodlarında da bu pencereden değişiklik yapılabilir. |
| Stok Kodu | Ambar giriş fişi kayıtları, stok hareket kayıtları arasında da işlem görebildiği için, "Üretim" ya da "Maliyet Muhasebesi" modülünü kullananların değişik düzeydeki stok kodlarının hareket kayıtları için kullanılır.![](../../../../_assets/088477bb321d1b20c939.jpg) Rehber butonu ile stok kodu seçimi yapılabilir. |
| Tarih | Ambar giriş fişinin üzerinde yazan tarihin girildiği alandır. |
| Toplu Depo | Tanımlanan depo kodları arasından,![](../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu ile seçim yapılarak, ilgili depo kodunun girildiği alandır. alış parametreleri kısmında bu parametre işaretlenmediği takdirde, her stok kalemi için ayrı ayrı lokal depo kodu girilmesi gerekir. |
| Fiili Tarih | Ambar girişinin gerçekleştiği tarihin girildiği alandır. |
| Döviz Bazında Tarih | Ambar çıkış fişlerinde geçerli olacak kur bilgisinin hangi tarihe göre baz alınacağının belirlendiği alandır. |
| Özel Kod-1 | Tanımlanan Özel Kod-1 seçenekleri arasından,![](../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu ile seçim yapılarak, ambar giriş fişlerinin belli kodlar altında gruplanmasını sağlayan alandır. |
| Özel Kod-2 | Tanımlanan Özel Kod-2 seçenekleri arasından,![](../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu ile seçim yapılarak, ambar giriş kayıtlarının rapor bazında gruplama yapılmasını sağlayan alandır. |
| Açıklama | Ambar giriş fişine ait açıklama bilgisinin girildiği alandır. |
| Nakliye Katsayısı | Tanımlanan nakliye katsayısı girişinin yapıldığı alandır. |
| Proje Kodu | Tanımlanan proje kodları arasından,![](../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu ile seçim yapılarak, istenildiğinde proje bazında rapor alınabilmesi için girilen koddur. |
| Plasiyer Kodu | Tanımlanan plasiyer kodları arasından,![](../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu ile seçim yapılarak, ilgili müşteriye ait plasiyer kodunun girildiği alandır. |
| KDV Dahil | KDV'nin nasıl uygulanacağının belirlendiği alandır. KDV dahil kutucuğu işaretlendiği takdirde, stoka ait birim fiyatı, KDV tutarını da içerir. |
| Değişsin | Dövizli belgelerde bazen (yuvarlama kaynaklı) döviz fiyatının, kurun ya da TL fiyatının değişmesi gerekebilir. Bu gibi durumlarda hangi sahadaki bilginin değişeceğinin belirlendiği alandır. |
| Farklı Teslimat | Ambar giriş fişinin kesildiği cari hesap/adres ile, stokların teslim edileceği cari hesap/adresin farklı olması halinde kullanılan bölümdür. |
| Giriş | Ambar girişi yapılacak malzeme isminin yer aldığı alandır. |
| Ek Sahalar | Açıklama girişi için kullanılan alanlardır. |

Özel Kod-1, Özel Kod-2, Masraf Kodu, Serbest, Maliyet Grubu, Ana Maliyet Grubu, Açıklama, Plasiyer Kodu, Proje Kodu, KDV Dahil, Toplu Depo, Nakliye Katsayısı, Farklı Teslimat, Ek Sahalardan oluşan alanlar, **A****lış Parametreleri sayesinde** isteğe bağlı olarak ekranda yer alabilir/almayabilir.

**Kalem Bilgileri**

Ambar Giriş Fişi ekranı Kalem Bilgileri sekmesi; Kalem Girişi, Açıklama ve Kalem Listesi alanlarının yer aldığı ekrandır.

Ambar Giriş Fişi ekranı Kalem Bilgileri sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Ambar Giriş Fişi Ekranı |  |
| --- | --- |
| Kod | Tanımlaması yapılan stok kaleminin, ![](../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu ile seçim yapılarak ekrana getirildiği koddur. |
| İsim | Stok sabit kayıtlarında kaydettiğiniz stok isminin, program tarafından ekrana getirildiği alandır. |
| Sipariş No | Her malın ayrı ayrı sipariş numarasının girilmesini sağlamak için kullanılan alandır. ![](../../../../_assets/088477bb321d1b20c939.jpg)rehber butonu ile stoklar için girilmiş tüm siparişlere ulaşılarak seçim yapılır. Ambar giriş fişi, sipariş bağlantılı kesilmeyecek ise, bu alan boş bırakılarak \<tab\> tuşu ile ilerlenir. Sipariş numarası olmadığı ya da yanlış girildiği durumlarda, program “**Sipariş Bulunamadı**” şeklinde bir uyarı verir. Sipariş bulunduğu zaman, o siparişle ilgili teslimi bekleyen mallar, kalan miktarları ve sipariş tutarlarıyla birlikte otomatik olarak ambar giriş ekranına gelir. |
| D.Kd (Depo Kodu) | Tanımlaması yapılan depo kodunun, ![](../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu ile depo seçimi yapılarak, her malın ayrı ayrı depolarda takip ve raporlanmasını sağlamak amacıyla kullanılan alandır. |
| Yapılandırma Kodu | Esnek yapılandırma uygulamasının kullanıldığı durumlarda, stoka ait yapılandırma kodunun girildiği alandır. |
| Yapılandırma Kodu Açıklaması | Yapılandırma kodu alanına girilen değere ait açıklama bilgisinin, program tarafından getirildiği alandır. |
| Yapılandırma Kod Sihirbazı | Belirli bir özellik kombinasyonu içeren yapılandırma kodunun, sistemde tanımlı yapılandırma kodları arasında olup olmadığını saptamak ve tanımlı değilse de hızlı tanımlama yapmak amacıyla kullanılan alandır. |
| Yapılandırılabilir Ürün Girişi | Birden fazla yapılandırma koduna ait giriş miktarlarının, tek seferde kaydedilmesi için kullanıldığı alandır. |
| Tes.Cari Kod (Teslim Cari Kodu) | Ambar giriş fişinin kesildiği cari hesap/adres ile, stokların teslim edileceği cari hesap/adresin farklı olması halinde, teslimatın yapılacağı cari hesap/adresin girileceği alandır. |
| Satır Açıklama | Her kalem için, 10 ayrı ek açıklama girişinin yapılabileceği alandır. |
| Ç.Değ (Çevrim Değeri) | Stok kodu alanına girilen stoka ait, birden fazla ölçü birimi tanımlanmışsa, hangi ölçü birimi üzerinden miktar girileceğinin belirlendiği alandır. Alanın sağ tarafında bulunan aşağı ok tuşuna basılarak, o stok için tanımlanmış olan ölçü birimi seçilir. Girilen miktar otomatik olarak ölçü birimi değerine çevrilir ve sistem tarafından ekrana getirilir. Alanın sağ tarafında bulunan rehber, stokun bir ölçü birimine ait birden fazla çevrim değeri olması halinde çevrimin hangi değere göre yapılacağını seçmek amacıyla kullanılır. |
| Seri Takibi | Ambar girişlerinin, seri numaralarına göre takibinin yapılması amacıyla kullanılan alandır. |
| Miktar 2 | Stok bazında takibin yapıldığı miktar alanıdır. Karma koli uygulamasının kullanıldığı durumlarda, koli stokuna ait miktar girişi için de kullanılır. |
| Fiyat Birim | Ambar giriş fişindeki stok kalemlerinin kaydı sırasında, fiyat girmeden önce, eğer ilgili mal için stoklarda birden fazla ölçü birimi tanımlanmışsa (adet, kg, koli v.s), gireceğiniz fiyatın hangi ölçü birimine ait olduğunun seçildiği alandır. |
| Muhasebe Kodu | Hizmet faturası kesen firmaların, bu faturaları satır bazında ayrı hesaplarda muhasebeleştirebilmeleri için kullanılan alandır. Bu alan için tanımlanan muhasebe kodunun seçilmesi ile, ilgili ambar giriş fişindeki hizmet kalemi için borç hareketi oluşur. "Üst bilgiler" sekmesinde giriş yeri "Masraf Merkezi" seçildiğinde, girilen masraf koduna karşılık gelen "Muhasebe Kodu" bu alana otomatik olarak aktarılır ve değiştirilmez. Hizmet faturası uygulaması, stok kartı kayıtlarında kodu "HIZ" ile başlayan stoklar için uygulanır. Dolayısıyla, hizmet uygulaması ile bu faturalardaki kalemleri ayrı hesaplarda muhasebeleştirmek isteyen firmaların, hizmet stoklarının kodunun ilk üç hanesini HIZ olarak açmaları gerekir. |
| Hesap İsmi | Muhasebe kodu alanına girilen hesap koduna ait isim bilgisinin program tarafından ekrana getirildiği alandır. |
| Ek Alan-1 | Ambar giriş fişi basımına yönelik, anlık açıklamaların girildiği alandır. |
| Ek Alan-2 | Ambar giriş fişleri girilirken stok kalemleri bazında ikinci bir açıklamanın gerekliliği halinde kullanılan alandır. Her bir kalem için 14 karakter uzunluğunda açıklama girilir. |
| Miktar | İlgili stok kaleminin ambar giriş fişi üzerindeki miktarının yazıldığı alandır. |
| M. Faz ( Mal fazlası) | Satılan malın yanında verilen hediye malların, ambar giriş fişlerinde gösterilmesi için kullanıldığı alandır. Burada hediye verilen miktar girilmelidir. Eğer satılan malın yanında hediye verilen mal farklı ise, miktar hanesine gerekli değer yazılır, mal fazlası hanesi boş bırakılır. Bir sonraki satıra hediye olarak verilen malın kodu yazılır ve bu mal için de miktar hanesi boş bırakılarak, mal fazlası hanesine hediye miktarı girilmesi ile kayıt oluşturulur. |
| Dv. Tip (Döviz Tip) | Döviz takibinin yapıldığı alandır. Girilen stok kodu için, tanımlaması yapılan döviz alış tipi değeri, program tarafından ekrana getirilir. Bu alana getirilen değer, isteğe bağlı olarak farklı bir döviz tipi ile de değiştirilebilir. Döviz tipi olarak “0“ dan farklı bir değer seçilirse, ilgili kalemin dövizli olarak satıldığı, “0“ değeri seçilirse de TL olarak satıldığı anlaşılır. |
| Döviz Fiyat | Girilen stok kodu için, tanımlaması yapılan döviz fiyat değeri, otomatik olarak ekrana gelir. İsteğe bağlı olarak, bu alana getirilen fiyat değiştirilebilir. |
| Döv.Kur | Üst bilgiler ekranında girmiş olduğunuz **Döviz Baz Tarihi** ile, **Döviz Takibi/Günlük Kur Girişi Bölümü’nden** girmiş olduğunuz kur tutarı, **Döviz Kur** alanına yansır. İsteğe göre değişiklik yapılabilir. Kur tutarı ile döviz fiyatı alanındaki değerlerin çarpımı sonucu çıkan rakam, fiyat alanına yansır. |
| Fiyat | İlgili malın, ambar giriş fişi üzerindeki birim fiyatıdır. |
| İsk.1-6 | İsteğe bağlı olarak 1’den 6’ya kadar kademeli şekilde ekranda yer alabilen, iskonto bilgisinin girildiği alandır. Sadece 1. İskonto için tutarsal iskonto girilebilir. Diğer kademeli iskontolarda, oran (%) bazında kayıt girilir. Hesaplamada malın brüt tutarından 1. iskonto düşüldükten sonra, kalan tutardan 2. iskonto düşülecektir. İkiden fazla iskonto kullanılması durumunda da, kalan tutar üzerinden diğer iskontolar düşülür. |
| İsk.1-6 Tip | İskontoların tiplerini muhasebe kodlarına bağlamak için kullanılan alandır. Örneğin, iskonto tip 1 için özel müşteriler iskontosu, iskonto tip 2 için mağaza iskontosu gibi kullanım amacına göre tanımlamalar yapıldıktan sonra belirlenen iskonto tipleri ile farklı muhasebe kodları çalıştırılabilir. |
| KDV | KDV oranının girildiği alandır. |
| Proje Kodu | Yapılan ambar girişinin proje bazında izlenmesini sağlayan alandır. ![](../../../../_assets/088477bb321d1b20c939.jpg)rehber butonu ile, ilgili proje seçimi yapılır. Örneğin, firmaya ait, farklı bir konumda yeni bir bina inşa edilmesi durumu bir projedir. Projeye ait bir kod tanımlar ve ilgili projeye ait alışlarda bu kodu seçerek kayıt yaparsanız, gerektiğinde **söz konusu projeye ait** ambar girişlerini bu kod sayesinde raporlayabilirsiniz. |
| Fiili Tarih | Üst Bilgiler sayfasında bulunan fiili tarih bilgisinin, kalem bilgilerine yansıtıldığı alandır. İsteğe bağlı olarak değiştirilebilir. |
| Tutar | Stok miktarı ile birim fiyatın program tarafından çarpılıp, brüt tutar olarak yazıldığı alandır. Bu alana müdahale edilemez. Sadece birim fiyat ve miktar hanelerinde yapılan değişiklikler tutarın değişmesine sebep olur. Ambar girişinde girilen tüm stok tutarlarının toplamı, ekranın sağ alt köşesinde bulunan **Toplam Tutar** alanında görünür. |
| Top. Mik. (Toplam Miktar) | Sipariş/irsaliye bağlantılı ambar giriş fişi oluşturulduğunda, ilgili stok kalemi için seçilen sipariş/irsaliye kalemindeki miktar bilgisinin program tarafından ekrana getirildiği alandır. |
| Sip. No.lar (Sipariş Numaraları) | Sipariş bağlantılı ambar giriş fişi oluşturulduğunda, ilgili sipariş numarasının izlendiği alandır. |
| İrs. Nolar (İrsaliye Numaraları) | İrsaliye bağlantılı ambar giriş fişi oluşturulduğunda, ilgili irsaliye numarasının izlendiği alandır. |
| Bakiye | Ambar giriş fişinde girilen her stok kodu için, ilgili malın stok hareket kayıtlarındaki bakiyesinin, bilgilendirme amacıyla program tarafından ekrana getirildiği alandır. |

Yapılandırma Kodu, Yapılandırma Kodu Açıklaması, Yapılandırma Kod Sihirbazı, Yapılandırılabilir Ürün Girişi, Teslim Cari Kodu, Sipariş No, Satır Açıklama, Depo Kodu, Çevrim Değeri, Ek Alan-1 ve 2, Seri Takibi, Miktar 2, Mal Fazlası, Fiyat Birim, Döviz Tip, İsk.1-6, KDV, Muhasebe Kodu, Hesap İsmi, Proje Kodu alanları, "**alış Parametreleri"** sayesinde isteğe bağlı olarak ekranda yer alabilir/almayabilir.

Kalem Bilgilerinde Değişiklik/İptal aşağıdaki şekilde yapılır:

- Yukarıda açıklanan alanlara bilgi girişi yapıldıktan sonra \<tab\> butonu ile ilerleyerek veya F5 butonuna basılarak, kalem bilgisi kaydedilir ve ekranda satır olarak görünür. Ambar giriş fişi kaydedilmemiş olmasına rağmen, satıra aktarılan stok alış bilgileri, stok hareket kayıtlarına da işlenir. Dolayısıyla, bu aşamada iken, ambar giriş fişinin tamamı yerine sadece stok giriş hareketi kaydedilir.
- Kaydedilen kalem üzerinde değişiklik yapılması istendiğinde, ilgili stok kalemi satırının üzerine çift tıklayarak seçim yapılması halinde, gerekli alan/alanların üzerinde değişiklik yapılabilir. Kaydedilen kalem aynı şekilde seçildikten sonra araç çubuklarında bulunan ![](../../../../_assets/2df4b343310bcd16b01e.jpg) kayıt silme butonu ya da klavyedeki F7 butonu yardımıyla ilgili kalem silinir.

**Toplamlar**

Ambar Giriş Fişi ekranı Toplamlar sekmesi; İskonto ve Maliyet Toplamları, KDV'ler Toplamı ve Genel Toplam, Kayıt Sorgulamaları alanlarının yer aldığı ekrandır.

Ambar Giriş Fişi ekranı Toplamlar sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Toplamlar Ekranı | İskonto ve Maliyet Toplamları |
| --- | --- |
| Brüt Toplam | Ambar giriş fişinde kaydedilen mal tutarlarının, iskonto düşülmeden önceki brüt tutarını gösteren alandır. Kalem bilgileri ekranındaki bilgilere göre oluşturulan bir alan olduğu için, elle değiştirme yapılamaz. Buradaki tutarın yanlış olması durumunda, önceki ekrana (kalem bilgileri) geçilerek gerekli düzeltme işlemleri yapılmalıdır. |
| Mal Fazlası İsk. | Kalem bilgileri ekranında mal fazlası alanı kullanılmışsa, program öncelikle mal fazlası (hediye) tutarını brüt olarak hesaplar, daha sonra iskonto şeklinde brüt tutardan düşer. Bu alanda, ambar giriş fişi kaydında mal fazlası olarak girilmiş bütün malların toplam tutarı ekranda görünür. Brüt tutardan ilk olarak düşecek iskonto, mal fazlası iskontosudur. Kalem bilgileri ekranındaki bilgilere göre oluşturulan bir alan olduğu için, elle değiştirme yapılamaz. Buradaki tutarın yanlış olması durumunda, önceki ekrana (kalem bilgileri) geçilerek gerekli düzeltme işlemleri yapılmalıdır. |
| Satır İskontosu | Ambar giriş kaydı sırasında, satır bazında girilen tüm iskonto oran/ tutar toplamlarının program tarafından hesaplanarak ekrana getirildiği alandır. Brüt tutar ve mal fazlası iskontosundan sonra düşülecek ikinci iskonto, satır iskontosudur. Kalem bilgileri ekranındaki bilgilere göre oluşturulan bir alan olduğu için, elle değiştirme yapılamaz. Buradaki tutarın yanlış olması durumunda, önceki ekrana (kalem bilgileri) geçilerek gerekli düzeltme işlemleri yapılmalıdır. |
| Ek Maliyet 1,2 | İlave maliyetlerin girildiği alandır. Hesaplatılan bir değer yoksa, elle tutar girilebilir. |
| Yuvarlama | Ambar giriş fişi genel toplamının yuvarlanması için kullanılan alandır. |
| Br. 1 Miktar, Br.2 Miktar, Br. 3 Miktar | Kalem Bilgilerinde girilen tüm stokların toplam miktar bilgilerinin, stok kartı kayıtlarında tanımlı birinci, ikinci ve üçüncü ölçü birimi cinsinden izlenen alandır. |
| Hediye Puan | Müşterilere, aldıkları malın üzerinden puan hesaplaması yapılması ve puanlarına istinaden hediye verilmesi işlemlerinin takibinin yapılması amacıyla kullanılan alandır. Bu sistemde, her bir ürün için ayrı ayrı puanlar belirlenerek, hak edilen, kullanılan ve kalan bakiye puanları takip edilebilir. Puan karşılığı verilen hediye ürünlerde, bakiye puan dikkate alınır. |
| Toplamlar Ekranı | **KDV’ler Toplamı ve Genel Toplam** |
| Ara Toplam | Yukarıda anlatılan iskontolar toplamının brüt toplamdan düşülüp, ek maliyet toplamlarının eklenmesiyle oluşan toplamdır. Bu alana elle müdahale edilemez. Bilgilendirmek amacıyla görüntülenen alandır. |
| KDV 1,2,3,4,5 | Ambar giriş fişinde girilen stok kalemlerinin, stok sabit kayıtlarında yazılı KDV oranına göre, program tarafından otomatik hesaplanarak ekrana getirildiği alandır. |
| KDV % | KDV hesaplamalarında kullanılan oranların izlendiği alandır. |
| Toplam KDV | Farklı KDV oranları üzerinden hesaplanan tutarların toplamının yazıldığı alandır. Hesaplanan değer üzerinde çok küçük bir farklılık olması halinde düzenleme yapılmasını, aksi halde bu değerin değiştirilmemesi tavsiye edilir. Burada yapılacak düzeltme, yukarıda anlatıldığı şekilde hesaplanan KDV tutarları dağılımına yansımaz. Yapılan değişiklik, sadece aşağıdaki genel toplam alanına yansır. Fatura/ Kayıt/alış Fatura Parametreleri Bölümü’nde “KDV Maliyete Eklensin” parametresi işaretlenmiş ise, bu alanda oluşan tutar muhasebeye entegre olmaz. Stok fiyatlarına KDV tutarları eklenerek stok hareket kayıtlarına aktarılır. |
| Genel Toplam | Yukarıda anlatılan işlemler sonucu oluşan son toplamın gösterildiği alandır. Bu tutar üzerinde değişiklik yapmak yerine Karşı Toplam alanı kullanılır. |
| Resim Alanı | Faturaya resim yada doküman dosyası eklemek için kullanılan alandır. |
| Toplamlar Ekranı | Kayıt Sorgulamaları |
| Toplam Mal Ağırlığı | Ambar giriş fişinde girilen stok kalemleri için, “Stok Kartı Kayıtlarında” birim ağırlık tanımlaması ile aktif olan alandır. Program bu ağırlıkları, ambar giriş fişindeki miktarlarla çarparak toplam mal ağırlığını hesaplar ve otomatik olarak ekrana getirir. |
| Vade Gün/Vade Tarihi | Ambar giriş kaydı oluştururken, cari hareket ve stok hareket kayıtlarına işlenecek vade gün/tarihinin belirlendiği alandır. Stok hareketlerine işlenen vade tarihi, stok hareket girişleri ekranından görüntülenmez fakat raporlardan izlenebilir. |
| Basım | Girilen ambar giriş fişinin basımı yapılacak ise işaretlenen alandır. Bu alan işaretlendikten sonra “Tamam” butonuna basıldığında, “Dizayn Sorgulama” ekranından dizayn tipi ve yazıcı seçilerek basım yapılır. |
| Sıralama Seçeneği | Basımı yapılacak olan ambar giriş fişi kalemlerini, bu alanda bulunan seçeneklere göre sıralatmak amacıyla kullanılan alandır. |
| Tamam | Bilgileri girilen ambar giriş fişinin kaydı için kullanılan butondur. Tamam ![](../../../../_assets/23043a6798351fd813b5.png) butonuna basıldığında, ambar giriş fişine ilişkin kayıtlar ilgili entegre bölümlere aktarılır. Ambar giriş fişinin daha önce kaydedilmiş olması ve düzenlenip tekrar kaydedilmesi durumunda, entegre bölümlerden stok ve cari bölümlere işlenen hareketler program tarafından düzenlenir. Bu kayıtlar, Entegrasyon/Entegrasyon Kayıtlarında “ 2 <u>no.lu</u> " (Düzeltilmiş Kayıt) ya da “4 <u>no.lu</u> " (Düzeltilmiş Bulunamadı) tipte izlenebilir. |

Mal Fazlası İskontosu, Satır İskontosu, Sıralama Seçeneği alanları **"Alış Parametreleri"** sayesinde, isteğe bağlı olarak ekranda yer alabilir/almayabilir.

Ambar Giriş Fişi Kaydı, Değişikliği, İptali aşağıdaki şekilde yapılır:

- Ambar giriş fişinin kaydı için, ilgili ekrandaki alanlara bilgi girişi yapıldıktan sonra, "Toplamlar" ekranında "**tamam"** butonuna basılır. Böylece, "Üst Bilgiler" ekranında seçilen tipe göre, gerekli bölümlerde entegre kayıtlar oluşur.

- Daha önceden kaydedilmiş bir ambar giriş fişi üzerinde değişiklik yapmak için, "Üst Bilgiler" ekranından ilgili faturanın numarası girilerek \<tab\> tuşuna basılır. Böylece, kayıtlı faturaya ait daha önceden girilmiş bilgiler ekrana gelir. Mevcut ekranda değiştirilmek istenen alana gelip düzenleme yapılır. Burada dikkat edilmesi gereken nokta, belge üzerinde değişiklik yapıldıktan sonra, ambar girişi ile ilgili bağlantılı bölümlerde de gerekli değişikliklerin program tarafından yapılabilmesi için, "**Toplamlar"** ekranından belgenin tekrar kaydedilmesi gerekir.
- Kaydedilmiş bir ambar giriş fişinin iptali için, "Üst Bilgiler" ekranında iken araç çubuklarında bulunan ![](../../../../_assets/2df4b343310bcd16b01e.jpg) (Kayıt Sil) butonuna ya da klavyedeki F7 butonuna basılır. Bu aşamada program, “Bu ekrana ait tüm bilgileriniz silinecektir. Emin misiniz?” şeklinde bir uyarı ekrana getirir. “Evet” butonuna basılması halinde, ilgili faturaya ait bilgiler, bağlı olduğu tüm bölümler dahil olmak üzere sistemden silinir.

Ambar Giriş Fişinde Kullanılan Özel Tuşlar için; [Alış Faturasında Kullanılan Özel Tuşlar](<Alış Faturası/Alış Faturasında Kullanılan Özel Tuşlar.md>)
