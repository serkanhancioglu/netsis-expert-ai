---
title: "Satıcı Siparişleri"
page_id: "24754638"
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
  - "Satıcı Siparişleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Fatura / Kayıt / Fatura / Satıcı Siparişleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTc0NDA5MzkxLWE1OWMtNGU3Yy1hMGRjLWIwYzdlZTRlODdmYyZsaW5rPWVmMTdjMTZhLTZkYWUtNDk2Ni05YTk4LWNmZDU2NTczMTRkMyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=74409391-a59c-4e7c-a0dc-b0c7ee4e87fc&link=ef17c16a-6dae-4966-9a98-cfd5657314d3&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "satici-siparisleri_24754696_24754638.html"
source_version: "2022-10-24T18:25:22.290+03:00"
source_bytes: 96427
fetched_at: "2026-09-13T04:02:32+00:00"
generator: "netsis-scraper 1.0.0"
---
# Satıcı Siparişleri

Satıcı Siparişleri Bölümü'nde; satıcılarınıza verdiğiniz siparişler kaydedilir, düzenlenir ve izlenir.

Satıcı Siparişleri, Lojistik-Satış Bölümü’nde, fatura kayıt menüsünün altında yer alır. Üst Bilgiler, Koşul Bilgileri, Kalem Bilgileri, Toplamlar, Vadelere Bölme sekmelerinden oluşur.

"Satıcı Siparişleri" bölümünün menüde yer alması için; Fatura → Kayıt → [Alış Parametreleri](<Alış Parametreleri.md>) → Fatura Sipariş → "Sipariş Takibi Yapılsın" parametresinin işaretlenmesi gerekir.

**Üst Bilgiler**

Satıcı Siparişleri Üst Bilgiler sekmesi, satıcı siparişlerine ait sabit ve cari bilgi alanlarının yer aldığı ekrandır.

Satıcı Siparişleri ekranı Üst Bilgiler sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Satıcı Siparişleri Ekranı |  |
| --- | --- |
| Numara | Siparişin programdaki takip numarasıdır. Yeni oluşturulacak belgeye ait numara otomatik olarak ekrana gelir. Alış Fatura Parametrelerinde “İrsaliye/Faturalarda Seri No Takibi” parametresi işaretlenmiş ve "İşlemler/Seri Düzenleme" bölümünde gerekli tanımlamalar yapılmışsa, program otomatik olarak seri bilgisi olan bir numarayı ekrana getirir. Aksi takdirde, program tarafından herhangi bir değer ekrana getirilmez ve kullanıcı tarafından tek karakterlik alfabetik sıra numarasının girilmesi gerekir. \<tab\> tuşuna basıldığında, girilen seriye ait kalınan son numara ekrana gelir. Program, girilen seri numarasına göre oluşan sipariş numaralarını ayrı ayrı takip eder. "Seri Düzenleme İşlemi" ile ilgili detaylı bilgi için; Fatura → İşlemler → Seri Düzenleme dokümanına bakılabilir. Önceden girilmiş olan bir siparişi izlemek için, daha önceden kaydedilen sipariş numarasının girilip \<tab\> butonuna basılması yeterlidir. Bu durumda kayıtlı siparişe ait diğer bilgiler ekrana gelir. Daha Önceden kaydedilmiş müşteri siparişlerine ait numara bilgilerine, ![](../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu yardımı ile ulaşılır. |
| Cari Kodu | Sipariş verilen satıcıya ait cari hesap kodunun girildiği alandır. ![](../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu yardımı ile cari hesap kodları arasından seçim yapılır. |
| Tarih | Satıcı siparişine ait tarihin girileceği alandır. |
| Teslim Tarihi | Siparişin teslim edileceği tarihtir. Bu tarihin doğru olarak girilmesi, ileride belli tarih aralıklarında teslim edilmesi gereken siparişlerin veya teslimi gecikmiş siparişlerin raporlanabilmesi açısından önemlidir. |
| İstenilen Teslim Tarihi | Satıcının, siparişleri teslim etmek istediği tarihin rapor amaçlı girildiği alandır. |
| Döviz Baz Tarihi | Siparişlerde geçerli olacak kur bilgisinin, hangi tarihe göre baz alınacağının belirlendiği alandır. |
| Tipi | Siparişin yurtiçi mi yoksa yurtdışı mı olduğunun belirlendiği alandır. |
| İhracat/İthalat Tipi | Tipi alanında "yurtdışı" seçilmesi halinde aktif olan alandır. |
| Export Referans No | Export Referans Numarası, sadece yurtdışı tipli siparişlerde geçerli olacak alandır. Firmalar, yaptığı her ihracata bir numara vermesi gerekir. Programda İhracat faturası oluşturulması için öncelikle, ihracat tipli satış irsaliyesinin girilmesi gerekir. Finans Modülü→ Dekont→ Kayıt→ İthalat/İhracat İşlemleri → "İhracat Kapatma" bölümünden "Referans No" seçilerek ihracat faturası oluşturulur. İhracat işlemleri tamamlandığında program tarafından oluşturulan ihracat faturasına, irsaliyede girilen Export Referans Numarası aktarılır. |
| Özel Kod-1 | Tanımlanan Özel Kod-1 seçenekleri arasından,![](../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu ile seçim yapılarak, siparişlerin belli kodlar altında gruplanmasını sağlayan alandır. |
| Özel Kod-2 | Tanımlanan Özel Kod-2 seçenekleri arasından,![](../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu ile seçim yapılarak, sipariş kayıtlarının rapor bazında gruplama yapılmasını sağlayan alandır. |
| Açıklama | Satıcı siparişine ait açıklama bilgisinin girildiği alandır. |
| Plasiyer Kodu | Tanımlanan plasiyer kodları arasından,![](../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu ile seçim yapılarak, ilgili satıcıya ait plasiyer kodunun girildiği alandır. |
| KDV Dahil | KDV'nin nasıl uygulanacağının belirlendiği alandır. KDV dahil kutucuğu işaretlendiği takdirde, stoka ait birim fiyatı, KDV tutarını da içerir. |
| Bağlantı No | Girilen belgenin hangi bağlantıya ait olduğunun izlendiği alandır. |
| Sipariş Parçala | Bu uygulama, birden fazla işletme ya da şubeli çalışan firmalar tarafından kullanılır. Siparişler merkez tarafından alınıp işletmelere/şubelere dağıtılıyorsa, sipariş girişi sırasında “sipariş parçala” parametresi işaretlenir. Bu parametre, programa sadece merkezden girildiğinde kullanılır. Bu durumda kalem bilgilerindeki her stok için “şube kodu” sorgulanır. Şube koduna, ilgili stokun siparişinin kaydedileceği işletme/şube kodu girilir. Merkezden sipariş girişi tamamlandıktan sonra, her işletme/şube kendisi ile ilgili ürünlerin siparişlerini raporlayabilir fakat sipariş üzerinde düzeltme yapamaz. Şubelerde oluşan sipariş numarası, merkezdeki ile aynıdır. Merkezden girilen siparişlerin diğer işletme/şubelere dağıtılabilmesi için gerçekleştirilmesi gerekenler aşağıdaki şekildedir: - Siparişte girilen carinin, hem merkez hem de şubede işlem görmesi gerekir,<br>- Siparişte geçen stokun, hem merkez hem de ilgili şubede işlem görmesi gerekir.<br>- Bunun için cari ve stok kartlarında “işletmelerde ortak”, “şubelerde ortak” alanlarındaki ilgili işletme/şubenin kodu 1 ya da -1 (ortak) olmalıdır. |
| Toplu Depo | Tanımlanan depo kodları arasından, ![](../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu ile seçim yapılarak, ilgili depo kodunun girildiği alandır. Alış parametreleri kısmında bu parametre işaretlenmediği takdirde, her sipariş kalemi için ayrı ayrı lokal depo kodu girilmesi gerekir. |
| Nakliye Katsayısı | Tanımlanan nakliye katsayısı girişinin yapıldığı alandır. |
| Değişsin | Dövizli belgelerde bazen (yuvarlama kaynaklı) döviz fiyatının, kurun ya da TL fiyatının değişmesi gerekir. Böyle durumlarda hangi alandaki bilginin değişeceğinin belirlendiği alandır. |
| Farklı Teslimat | Stokların teslim edileceği cari hesap/adres ile, malların teslim edileceği cari hesap/adresin farklı olması halinde kullanılan bölümdür. |
| Bölge Farkı İskontosu | Satıcı ile daha önceden anlaşmaya varılan bir indirim tutarı varsa bu tutar "Cari Sabit Bilgilerinde" bulunan **Bölge Farkı İskontosu** alanına girilerek, belgelere otomatik olarak getirilmesi sağlanır. |
| Kod | Basıma yönelik adres bilgisi değişikliği için girilen alandır. Buradaki Cari Kod, siparişin girildiği kodun aynısı olmalıdır. |
| İsim | Kod alanına girilen cari kodun isim bilgisinin, program tarafından ekrana getirildiği alandır. |
| Adres | Teslimat yapılacak adres bilgisinin, cari hesabın koduna göre program tarafından ekrana getirildiği, kullanıcı tarafından da değişikliğinin yapılabildiği alandır. |
| İlçe | Teslimat yapılacak ilçe bilgisinin, cari hesabın koduna göre program tarafından ekrana getirildiği, kullanıcı tarafından da değişikliğinin yapılabildiği alandır. |
| İl | Teslimat yapılacak il bilgisinin, cari hesabın koduna göre program tarafından ekrana getirildiği, kullanıcı tarafından da değişikliğinin yapılabildiği alandır. |
| Cari Bilgiler/ İsim, Açıklama-1, Açıklama-2, Açıklama-3 | Kaydedilen siparişin satıcıya ait kod bilgisi girildiğinde, cari hesap kayıtlarında bulunan isim ve açıklama bilgilerinin program tarafından ekrana getirildiği alanlardır. Sipariş kaydı sırasında bu alanlara müdahale edilemez, sadece bilgi amaçlı olarak görüntülenir. |
| Ek Sahalar | Açıklama girişi için kullanılan alanlardır. |

Özel Kod-1, Özel Kod-2, Açıklama, Plasiyer Kodu, Proje Kodu, KDV Dahil, Toplu Depo, Nakliye Katsayısı, Farklı Teslimat (kod, isim, adres, ilçe, il), Cari Bilgiler/İsim, Açıklama-1 Açıklama-2 Açıklama 3 ve Ek Sahalardan oluşan alanlar, **Alış Parametreleri sayesinde** isteğe bağlı olarak ekranda yer alabilir/almayabilir.

**Koşul Bilgileri**

Satıcı Siparişleri Koşul Bilgileri sekmesi, satıcı siparişlerine ait geçerli koşul bilgileri alanlarının yer aldığı ekrandır.

Satıcı Siparişleri ekranı Koşul Bilgileri sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Satıcı Siparişleri Ekranı |  |
| --- | --- |
| Koşul Kodu | Tanımlaması yapılan koşulun, ![](../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu ile seçim yapılarak ekrana getirildiği koddur. |
| Vade Günü | Bir borcun ödenmesi için tanınan süredir. Bu alana vade günü girildiğinde, tanımlanan vade için belirlenen liste fiyatı, kalem bilgileri ekranındaki fiyat alanına otomatik olarak yansır. |
| Koşul Tarihi | Koşul tarihinin girildiği alandır. Bu alanda tarih, otomatik olarak ekrana gelir. Eğer koşul tarihi değiştirilirse, siparişin girildiği tarihte geçerli olan fiyata göre vade ve iskonto uygulaması yapılır. |
| Fiyat Tarihi | Sipariş fiyat liste tarihinin girildiği alandır. |
| Ödeme Kodu | Sipariş kaydı sırasında, koşula bağlı ödeme planının kodu girilmişse, ilgili ödeme kodunun ![](../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu ile seçim yapılarak ekrana getirildiği alandır. Cari/Koşul Kayıtları/ Genel Koşul Kayıtları/ Koşul Genel-2 sayfasında bulunan ödeme kodu alanına, o koşula bağlanacak ödeme planının kodu girilmiş ise, ilgili ödeme kodu bu alana program tarafından otomatik getirilir. Sipariş belgelerinde koşul uygulamasının olduğu, ancak koşula bağlı ödeme planının olmadığı durumlarda ödeme kodu alanı boş olur ve istenen ödeme planına ait kod girilebilir. Sipariş belgelerinde, cari ödeme planlarının koşul bağlantılı uygulanabilmesi için, **Koşul Sabit Kayıtları**nda bulunan “Cari Hesap Vadelere Bölünerek Atılsın” seçeneğinin işaretlenmesi gerekir. Koşul uygulamasının kullanılmadığı durumlarda bu alan, "Koşul Bilgileri" ekranı yerine "Üst Bilgiler " ekranında yer alır. |

Koşul bilgileri ekranındaki tüm alanlar**, Alış Fatura Parametreleri** sayesinde, isteğe bağlı olarak ekranda yer alabilir/almayabilir.

**Kalem Bilgileri**

Satıcı Siparişleri Kalem Girişi sekmesi, Açıklama ve Kalem Listesi alanlarının yer aldığı ekrandır.

Satıcı Siparişleri ekranı Kalem Girişi sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Satıcı Siparişleri Ekranı |  |
| --- | --- |
| Kod | Teslimatı yapılacak stok kaleminin, ![](../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu ile ile seçim yapılarak ekrana getirildiği koddur. |
| İsim | Stok sabit kayıtlarında kaydettiğiniz stok isminin, program tarafından ekrana getirildiği alandır. |
| Şube Kodu | Siparişe ait şube kodunun girildiği alandır. ![](../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu ile seçim yapılır. |
| D.Kd (Depo Kodu) | Tanımlaması yapılan depo kodunun, ![](../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu ile depo seçimi yapılarak, her siparişin ayrı ayrı depolarda takip ve raporlanmasını sağlamak amacıyla kullanılan alandır. |
| Yapılandırma Kodu | Esnek yapılandırma uygulamasının kullanıldığı durumlarda, stoka ait yapılandırma kodunun girildiği alandır. |
| Yapılandırma Kodu Açıklaması | Yapılandırma kodu alanına girilen değere ait açıklama bilgisinin, program tarafından ekrana getirildiği alandır. |
| Yapılandırma Kod Sihirbazı | Belirli bir özellik kombinasyonu içeren yapılandırma kodunun, sistemde tanımlı yapılandırma kodları arasında olup olmadığını saptamak ve tanımlı değilse de hızlı tanımlama yapmak amacıyla kullanılan alandır. |
| Yapılandırılabilir Ürün Girişi | Birden fazla yapılandırma koduna ait çıkış miktarlarının, tek seferde kaydedilmesi için kullanıldığı alandır. |
| Tes.Cari Kod (Teslim Cari Kodu) | Siparişin kaydedildiği cari hesap/adres ile, malların teslim edileceği cari hesap/adresin farklı olması halinde, teslimatın yapılacağı cari hesap/adresin girileceği alandır. |
| Satır Açıklama | Her kalem için, 10 ayrı ek açıklama girişinin yapıldığı alandır. |
| Ç.Değ (Çevrim Değeri) | Stok kodu alanına girilen stoka ait, birden fazla ölçü birimi tanımlanmışsa, hangi ölçü birimi üzerinden miktar girileceğinin belirlendiği alandır. Alanın sağ tarafında bulunan aşağı ok tuşuna basılarak, o stok için tanımlanmış olan ölçü birimi seçilir. Girilen miktar otomatik olarak ölçü birimi değerine çevrilir ve sistem tarafından ekrana getirilir. Alanın sağ tarafında bulunan rehber, stokun bir ölçü birimine ait birden fazla çevrim değeri olması halinde çevrimin hangi değere göre yapılacağını seçmek amacıyla kullanılır. |
| Seri Takibi | Siparişlerin seri numaralarına göre takibinin yapılması amacıyla kullanılan alandır. |
| Miktar 2 | Stok bazında takibin yapıldığı miktar alanıdır. Karma koli uygulamasının kullanıldığı durumlarda, koli stokuna ait miktar girişi için de kullanılır. |
| Fiyat Birim | Siparişteki stok kalemlerinin kaydı sırasında, fiyat girmeden önce, eğer ilgili mal için stoklarda birden fazla ölçü birimi tanımlanmışsa (adet, kg, koli gibi), girilen fiyatın hangi ölçü birimine ait olduğunun seçildiği alandır. |
| Vade Tarihi | Vade günü baz alınarak hesaplanan tarihin, program tarafından ekrana getirildiği alandır. |
| Ek Alan-1 | Sipariş basımına yönelik, anlık açıklamaların girildiği alandır. |
| Ek Alan-2 | Satıcı siparişleri girilirken stok kalemleri bazında ikinci bir açıklamanın gerekliliği halinde kullanılan alandır. Her bir kalem için 14 karakter uzunluğunda açıklama girilir. |
| Kesinleşmiş / Planlanan | Bu alanda, girilen sipariş kaleminin teslimat tarihinin kesinleşmiş olup olmadığı sorgulanır. Bu seçenek işaretlendiğinde planlanan sipariş, işaretlenmediğinde ise kesinleşen sipariş olarak kaydedilir. Burada yapılan seçim, MRP modülünde gereksinim planlanması aşamasında önem kazanır. Bu alanın MRP ile ilişkisi hakkında detaylı bilgi için bakınız MRP/Gereksinin Planlama Oluşturma. |
| Yükleme Tarihi | Siparişin ne zaman yükleneceğinin belirlendiği alandır. Bu alana herhangi bir tarih girmeden geçildiğinde, teslim tarihi alanındaki tarih, yükleme tarihi olarak otomatik olarak ekrana gelir. |
| Miktar | İlgili stok kaleminin sipariş üzerindeki miktarının yazıldığı alandır. |
| M. Faz ( Mal fazlası) | Sipariş edilen malın yanında alınan hediye malların, siparişte gösterilmesi için kullanıldığı alandır. Burada hediye verilen miktar girilmelidir. Eğer sipariş edilen malın yanında hediye verilen mal farklı ise, miktar hanesine gerekli değer yazılır, mal fazlası hanesi boş bırakılır. Bir sonraki satıra hediye olarak verilen malın kodu yazılır ve bu mal için de miktar hanesi boş bırakılarak, mal fazlası hanesine hediye miktarı girilmesi ile kayıt oluşturulur. |
| Dv. Tip (Döviz Tip) | Döviz takibinin yapıldığı alandır. Girilen stok kodu için, tanımlaması yapılan döviz satış tipi değeri, program tarafından ekrana getirilir. Bu alana getirilen değer, isteğe bağlı olarak farklı bir döviz tipi ile de değiştirilebilir. Döviz tipi olarak “0“ dan farklı bir değer seçilirse, ilgili kalemin dövizli olarak satıldığı, “0“ değeri seçilirse de TL olarak satıldığı anlaşılır. |
| Döviz Fiyat | Girilen stok kodu için, tanımlaması yapılan döviz fiyat değeri, otomatik olarak ekrana gelir. İsteğe bağlı olarak, bu alana getirilen fiyat değiştirilebilir. |
| Döviz Kur | "Üst bilgiler" sekmesinden girilen **Döviz Baz Tarihi** ile, **Döviz Takibi → Günlük Kur Girişi Bölümünden** girilen kur tutarı, **Döviz Kur** alanına aktarılır. İsteğe göre değişiklik yapılabilir. Kur tutarı ile döviz fiyatı alanındaki değerlerin çarpımı sonucu çıkan rakam, fiyat alanına aktarılır.Üst bilgiler ekranında girmiş olduğunuz **Döviz Baz Tarihi** ile, **Döviz Takibi/Günlük Kur Girişi Bölümü’nden** girmiş olduğunuz kur tutarı, **Döviz Kur** alanına yansır. İsteğe göre değişiklik yapılabilir. Kur tutarı ile döviz fiyatı alanındaki değerlerin çarpımı sonucu çıkan rakam, fiyat alanına yansır. |
| Fiyat | İlgili malın, sipariş üzerindeki birim fiyatıdır. |
| İsk.1-6 | İsteğe bağlı olarak 1’den 6’ya kadar kademeli şekilde ekranda yer alabilen, iskonto bilgisinin girildiği alandır. Sadece 1. İskonto için tutarsal iskonto girilebilir. Diğer kademeli iskontolarda, oran (%) bazında kayıt girilir. Hesaplamada malın brüt tutarından 1. iskonto düşüldükten sonra, kalan tutardan 2. iskonto düşülecektir. İkiden fazla iskonto kullanılması durumunda da, kalan tutar üzerinden diğer iskontolar düşülür. |
| İsk.1-6 Tip | İskontoların tiplerini muhasebe kodlarına bağlamak için kullanılan alandır. Örneğin, iskonto tip 1 için özel müşteriler iskontosu, iskonto tip 2 için mağaza iskontosu gibi kullanım amacına göre tanımlamalar yapıldıktan sonra belirlenen iskonto tipleri ile farklı muhasebe kodları çalıştırılabilir. |
| KDV | KDV oranının girildiği alandır. |
| Muhasebe Kodu | Hizmet faturası kesen firmaların, bu faturaları satır bazında ayrı hesaplarda muhasebeleştirebilmeleri için kullanılan alandır. Bu alan için tanımlanan muhasebe kodunun seçilmesi ile, ilgili satış faturasındaki hizmet kalemi için alacak hareketi oluşur. Hizmet faturası uygulaması, stok kartı kayıtlarında kodu "HIZ" ile başlayan stoklar için uygulanır. Dolayısıyla, hizmet uygulaması ile bu faturalardaki kalemleri ayrı hesaplarda muhasebeleştirmek isteyen firmaların, hizmet stoklarının kodunun ilk üç hanesini HIZ olarak açmaları gerekir. |
| Hesap İsmi | Muhasebe kodu alanına girilen hesap koduna ait isim bilgisinin program tarafından ekrana getirildiği alandır. |
| Proje Kodu | Verilen siparişin proje bazında izlenmesini sağlayan alandır. ![](../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu ile, ilgili proje seçimi yapılır. Örneğin, firmaya ait, farklı bir konumda yeni bir bina inşa edilmesi durumu bir projedir. Projeye ait bir kod tanımlar ve ilgili projeye ait alışlarda bu kod seçilerek kayıt yapılırsa, gerektiğinde **söz konusu projeye ait** siparişler bu kod sayesinde raporlanabilir. |
| Fiili Tarih | Üst Bilgiler sayfasında bulunan fiili tarih bilgisinin, kalem bilgilerine yansıtıldığı alandır. İsteğe bağlı olarak değiştirilebilir. |
| Tutar | Stok miktarı ile birim fiyatın program tarafından çarpılıp, brüt tutar olarak yazıldığı alandır. Bu alana müdahale edilemez. Sadece birim fiyat ve miktar hanelerinde yapılan değişiklikler tutarın değişmesine sebep olur. Siparişte girilen tüm stok tutarlarının toplamı, ekranın sağ alt köşesinde bulunan **Toplam Tutar** alanında görünür. |
| Top. Mik. (Toplam Miktar) | Siparişte girilen toplam miktarın izlendiği alandır. |
| Sip. Nolar (Sipariş Numaraları) | Müşteri siparişi kaydında herhangi bir kullanımı olmayıp, sipariş bağlantılı fatura oluşturulduğunda, ilgili sipariş numarasının izlendiği bölümdür. |
| Bakiye | Siparişte girilen her stok kodu için, ilgili malın stok hareket kayıtlarındaki bakiyesinin, bilgilendirme amacıyla program tarafından ekrana getirildiği alandır. |

Yapılandırma Kodu, Yapılandırma Kodu Açıklaması, Yapılandırma Kod Sihirbazı, Yapılandırılabilir Ürün Girişi, Teslim Cari Kodu, Sipariş No, Satır Açıklama, Depo Kodu, Çevrim Değeri, Ek Alan-1 ve 2, Seri Takibi, Miktar 2, Mal Fazlası, Fiyat Birim, Döviz Tip, İsk.1-6, KDV, Muhasebe Kodu, Hesap İsmi, Proje Kodu, Vade Tarihi alanları, **Alış Parametreleri** sayesinde, isteğe bağlı olarak ekranda yer alabilir/almayabilir.

#### Kalem Bilgilerinde Değişiklik/İptal

Yukarıda açıklanan alanlara bilgi girişi yapıldıktan sonra \<tab\> butonu ile ilerleyerek veya F5 butonuna basılarak, kalem bilgisi kaydedilir ve ekranda satır olarak görünür. Sipariş kaydedilmemiş olmasına rağmen, satıra aktarılan stok sipariş bilgileri, stok hareket kayıtlarına da işlenir. Dolayısıyla, bu aşamada iken, siparişin tamamı yerine sadece stok giriş hareketi kaydedilir.

Kaydedilen kalem üzerinde değişiklik yapılması istendiğinde, ilgili stok kalemi satırının üzerine çift tıklayarak seçim yapılması halinde, gerekli alan/alanların üzerinde değişiklik yapılabilir. Kaydedilen kalem aynı şekilde seçildikten sonra araç çubuklarında bulunan ![](../../../../_assets/2df4b343310bcd16b01e.jpg) kayıt silme butonu ya da klavyedeki F7 butonu yardımıyla ilgili kalem silinir.

**Toplamlar**

Satıcı Siparişleri Toplamlar sekmesi, İskonto ve Maliyet Toplamları, KDV'ler Toplamı ve Genel Toplam, Kayıt Sorgulamaları alanlarının yer aldığı ekrandır. Satıcı Siparişleri Toplamlar sekmesi, Kalem Bilgileri sayfasında tutar/fiyat bilgisi girilmesi halinde, toplam bilgilerinin izlenmesi, ek maliyet ve iskonto girişlerinin yapılması, siparişin kaydedilmesi ve basımının yapılmasını sağlar.

Satıcı Siparişleri ekranı Toplamlar sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Satıcı Siparişleri Ekranı | İskonto ve Maliyet Toplamları |
| --- | --- |
| Brüt Toplam | Siparişte kaydedilen mal tutarlarının, iskonto düşülmeden önceki brüt tutarını gösteren alandır. Kalem bilgileri ekranındaki bilgilere göre oluşturulan bir alan olduğu için, elle değiştirme yapılamaz. Buradaki tutarın yanlış olması durumunda, önceki ekrana (kalem bilgileri) geçilerek gerekli düzeltme işlemleri yapılmalıdır. |
| Mal Fazlası İsk. | Kalem bilgileri ekranında mal fazlası alanı kullanılmışsa, program öncelikle mal fazlası (hediye) tutarını brüt olarak hesaplar, daha sonra iskonto şeklinde brüt tutardan düşer. Bu alanda, sipariş kaydında mal fazlası olarak girilmiş bütün malların toplam tutarı ekranda görünür. Brüt tutardan ilk olarak düşecek iskonto, mal fazlası iskontosudur. Kalem bilgileri ekranındaki bilgilere göre oluşturulan bir alan olduğu için, elle değiştirme yapılamaz. Buradaki tutarın yanlış olması durumunda, önceki ekrana (kalem bilgileri) geçilerek gerekli düzeltme işlemleri yapılmalıdır. |
| Satır İskontosu | Sipariş kaydı sırasında, satır bazında girilen tüm iskonto oran/ tutar toplamlarının program tarafından hesaplanarak ekrana getirildiği alandır. Brüt tutar ve mal fazlası iskontosundan sonra düşülecek ikinci iskonto, satır iskontosudur. Kalem bilgileri ekranındaki bilgilere göre oluşturulan bir alan olduğu için, elle değiştirme yapılamaz. Buradaki tutarın yanlış olması durumunda, önceki ekrana (kalem bilgileri) geçilerek gerekli düzeltme işlemleri yapılmalıdır. |
| Fat.Alt. İsk 1, 2, 3 | Genel iskonto 1-2-3 tanımlamaları yapılmış ise ekrana gelen alanlardır. Fatura Altı İskonto-1 alanı; cari hesap için girilen iskonto oranı varsa, bu oran üzerinden hesaplanan tutarın program tarafından ekrana getirildiği alandır. Hem tutar hem de oran değeri üzerinde istenen düzenleme yapılabilir. Tutar üzerinde yapılan düzeltme oran sahasına, oran üzerinde yapılan düzeltme tutar sahasına otomatik olarak hesaplanarak yansır. Genel İskonto-1-2-3, mal fazlası ve satır iskontolarından sonra, brüt tutardan düşülecek fatura altı iskontolarıdır. Genel İskonto-3 ayrıca **Bölge Farkı İskontosu** için de kullanılır. |
| Fat.AltM-1, 2 | Ek Maliyet-1 veya 2 tanımlamaları yapılmış ise fatura altı ilave maliyetleri otomatik olarak ekrana gelir. Hesaplatılan bir değer yoksa elle tutar girilebilir. |
| Genel İskonto 1,2,3 | Mal fazlası ve satır iskontolarından sonra, brüt tutardan düşülen fatura altı iskonto alanlarıdır. Bu alanların ismi, satış parametreleri kısmında Genel İskonto veya Fatura Altı İskonto isimlerinden birinin işaretlenmesiyle belirlenen isim ile ekrana gelir. Genel İskonto-1, siparişin kesildiği müşterinin, cari hesap sabit kayıtlarında tanımlanan iskonto oranı üzerinden hesaplanan tutarın görüntülendiği alandır. Hem tutar hem de oran değeri üzerinde istenilen düzenleme yapılabilir. Tutar üzerinde yapacağınız düzeltme oran sahasına, oran üzerinde yapacağınız düzeltme tutar sahasına otomatik hesaplanarak yansır. Bölge farkı iskontosu için Genel İskonto-3 kullanılır. |
| Ek Maliyet 1,2 | İlave maliyetlerin girildiği alandır. Hesaplatılan bir değer yoksa, elle tutar girilebilir. |
| ÖTV | Hesaplanan ÖTV tutarının izlendiği alandır. |
| Yuvarlama | Sipariş genel toplamının yuvarlanması için kullanılan alandır. |
| Br. 1 Miktar, Br.2 Miktar, Br. 3 Miktar | Kalem Bilgilerinde girilen tüm stokların toplam miktar bilgilerinin, stok kartı kayıtlarında tanımlı birinci, ikinci ve üçüncü ölçü birimi cinsinden izlenen alandır. |
| **Satıcı Siparişleri Ekranı** | **KDV’ler Toplamı ve Genel Toplam** |
| Ara Toplam | Yukarıda anlatılan iskontolar toplamının brüt toplamdan düşülüp, ek maliyet toplamlarının eklenmesiyle oluşan toplamdır. Bu alana elle müdahale edilemez. Bilgilendirmek amacıyla görüntülenen alandır. |
| KDV 1,2,3,4,5 | Sipariş kaydında girilen stok kalemlerinin, stok sabit kayıtlarında yazılı KDV oranına göre, program tarafından otomatik hesaplanarak ekrana getirildiği alandır. |
| KDV % | KDV hesaplamalarında kullanılan oranların izlendiği alandır. |
| Toplam KDV | Farklı KDV oranları üzerinden hesaplanan tutarların toplamının yazıldığı alandır. Hesaplanan değer üzerinde çok küçük bir farklılık olması halinde düzenleme yapılmasını, aksi halde bu değerin değiştirilmemesi tavsiye edilir. Burada yapılacak düzeltme, yukarıda anlatıldığı şekilde hesaplanan KDV tutarları dağılımına yansımaz. Yapılan değişiklik, sadece aşağıdaki genel toplam alanına yansır. Fatura/ Kayıt/Alış Fatura Parametreleri Bölümü’nde “KDV Maliyete Eklensin” parametresi işaretlenmiş ise, bu alanda oluşan tutar muhasebeye entegre olmaz. Stok fiyatlarına KDV tutarları eklenerek stok hareket kayıtlarına aktarılır. |
| Genel Toplam | Yukarıda anlatılan işlemler sonucu oluşan son toplamın gösterildiği alandır. Bu tutar üzerinde değişiklik yapmak yerine "Karşı Toplam" alanı kullanılır. |
| Karşı Toplam | Satıcı siparişi genel toplam alanında değişiklik yapılması istendiğinde kullanılan alandır. |
| Resim Alanı | Siparişe resim yada doküman dosyası eklemek için kullanılan alandır. |
| Satıcı Siparişleri Ekranı | Kayıt Sorgulamaları |
| Toplam Mal Ağırlığı | Siparişte girilen stok kalemleri için, “Stok Kartı Kayıtlarında” birim ağırlık tanımlaması ile aktif olan alandır. Program bu ağırlıkları, faturadaki miktarlarla çarparak toplam mal ağırlığını hesaplar ve otomatik olarak ekrana getirir. |
| Vade Gün/Vade Tarihi | Sipariş kaydı oluştururken, cari hareket ve stok hareket kayıtlarına işlenecek vade gün/tarihinin belirlendiği alandır. Stok hareketlerine işlenen vade tarihi, stok hareket girişleri ekranından görüntülenmez fakat raporlardan izlenebilir. |
| Basım | Girilen siparişin basımı için işaretlenen alandır. Bu alan işaretlendikten sonra “Tamam” butonuna basıldığında, “Dizayn Sorgulama” ekranından dizayn tipi ve yazıcı seçilerek basım yapılır. |
| Sıralama Seçeneği | Basımı yapılacak olan sipariş kalemlerini, bu alanda bulunan seçeneklere göre sıralatmak amacıyla kullanılan alandır. |
| Vadelere Bölme | Sipariş tutarının cari hareket kayıtlarına işlenirken, vadelere bölünerek kaydedilmesi için kullanılan alandır. "Üst Bilgiler" veya "Koşul Bilgileri" ekranında ödeme kodu girilmişse, vadelere bölünen tutarlar program tarafından otomatik olarak bu alana gelir. |
| Tamam | Bilgileri girilen siparişin kaydı için kullanılan butondur. Tamam ![](../../../../_assets/23043a6798351fd813b5.png)düğmesine basıldığında, siparişe ilişkin kayıtlar ilgili entegre bölümlere aktarılır. Siparişin daha önce kaydedilmiş olması ve düzenlenip tekrar kaydedilmesi durumunda, entegre bölümlerden stok ve cari bölümlere işlenen hareketler program tarafından düzenlenir. Bu kayıtlar, Entegrasyon/Entegrasyon Kayıtlarında “ 2 [no.lu](http://no.lu/) " (Düzeltilmiş Kayıt) ya da “4 [no.lu](http://no.lu/) " (Düzeltilmiş Bulunamadı) tipte izlenebilir. |

Mal Fazlası İskontosu, Satır İskontosu, Genel İskonto, Ek Maliyet 1-2, Sıralama Seçeneği, Vadelere Bölme alanları **"Alış Parametreleri"** sayesinde, isteğe bağlı olarak ekranda yer alabilir/almayabilir.

**Vadelere Bölme**

Satıcı Siparişleri Vadelere Bölme sekmesi, sipariş tutarının "Cari Hareket Kayıtlarına" işlenirken vadeler bazında bölünerek işlenmesi için kullanılır. Sipariş "Üst Bilgiler "ya da "Koşul Bilgilerinde" ödeme kodu girilmiş olması halinde, vadeler bazındaki tutarlar otomatik olarak ekrana gelir.

Satıcı Siparişleri ekranı Vadelere Bölme sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Satıcı Siparişleri Ekranı |  |
| --- | --- |
| Vade Günü | Siparişin vadesinin kaç gün olacağını gösteren alandır. |
| Vade Tarihi | Siparişin vadesinin ne zaman dolacağını gösteren tarihtir. |
| Oran | Sipariş tutarının ne oranda bölüneceğini gösteren alandır. |
| Tutar | Vade günü tutarını gösteren alandır. |
| Rapor Kodu | Tanımlaması yapılmış olan rapor kodunun girildiği alandır. |
| Proje Kodu | Tanımlaması yapılmış olan proje kodunun girildiği alandır |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam Butonu | Sipariş tutarının "Cari Hareket Kayıtlarına" işlenirken vadeler bazında bölünerek kaydedilmesi için kullanılan butondur. |

**Satıcı Siparişleri Kaydı, Değişikliği, İptali aşağıdaki şekilde yapılır:**

- Sipariş kaydındaki alanlara bilgi girişi yapıldıktan sonra, siparişin kaydedilmesi için; "Toplamlar" sayfasındaki "Tamam" butonuna basılması gerekir. Sipariş kaydı sonrası, programın entegre bölümlerinden herhangi birine kayıt yapılmaz. Siparişlerin kaydedilmesi, teslimatlar yapıldıkça kalan teslimat ve siparişlerin raporlarını alabilmek açısından önemlidir.

- Daha önceden kaydedilmiş bir sipariş belgesi üzerinde değişiklik yapmak için; "Üst Bilgiler" sayfasından ilgili siparişin numarası girilir ve \<tab\> tuşuna basılarak ilerlenir. Böylece, kayıtlı siparişe ait daha önceden girilmiş bilgiler ekrana gelir. Burada değiştirilmek istenen alan üzerinde değişiklik yapılabilir. Belge üzerinde değişiklik yapıldıktan sonra, "Toplamlar" sayfasından belgenin tekrar kaydedilmesi gerekir.

- Kaydedilmiş bir müşteri siparişinin iptali için; sipariş "Üst Bilgiler" sayfasında iken araç çubuklarında bulunan ![](../../../../_assets/2df4b343310bcd16b01e.jpg) kayıt sil butonuna ya da klavyedeki F7 butonuna basılması yeterlidir. “Bu ekrana ait tüm bilgileriniz silinecektir. Emin misiniz?” şeklinde bir uyarı ekranı geldikten sonra "Evet" butonuna basılması halinde ilgili siparişe ait bilgiler silinir.

"Satıcı Siparişlerinde Kullanılan Özel Tuşlar" için detaylı bilgi; [Satış Faturasında Kullanılan Özel Tuşlar](<Satış Faturası/Satış Faturasında Kullanılan Özel Tuşlar.md>)
