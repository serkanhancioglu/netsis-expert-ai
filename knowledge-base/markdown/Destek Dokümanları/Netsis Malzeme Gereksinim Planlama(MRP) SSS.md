---
title: "Netsis Malzeme Gereksinim Planlama(MRP) SSS"
page_id: "66248567"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis Malzeme Gereksinim Planlama(MRP) SSS"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis Malzeme Gereksinim Planlama(MRP) SSS"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTJiZWE3NWFlLTNiNmItNGRkMC1iMGYwLTViNDZiNjU0ZDkyMCZsaW5rPWVmZTAwYTM3LTE2OWItNDJkOS1hYTE4LTQyZjRlNmFmODY0YyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=2bea75ae-3b6b-4dd0-b0f0-5b46b654d920&link=efe00a37-169b-42d9-aa18-42f4e6af864c&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-malzeme-gereksinim-planlama-mrp-sss_80088524_66248567.html"
source_version: "2022-12-09T13:17:53.733+03:00"
source_bytes: 375930
fetched_at: "2026-09-13T04:24:26+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis Malzeme Gereksinim Planlama(MRP) SSS

**MRP** **nedir?**

Belli dönemler için üretim planının girilmesine ve/veya otomatik oluşturulmasını, üretim planının gerçekleşmesi için miktar ve tarih bazında malzeme ve yarı mamul gereksinimlerinin çıkarılmasını, çeşitli şekillerde listelenmesine ve ilgili dönemler için otomatik sipariş ve iş emri takiplerinin yapılmasını sağlayan modüldür. Bunun dışında, eldeki kaynaklar ile, gerekli olan kaynakların tespit edilerek kapasite planlamanın yapılabilmesi bu modül sayesinde mümkündür.

**MRP** **programda** **kaç** **farklı** **şekilde** **kullanılabilir?**

MRP sipariş bazında rezervasyon sistemi ve kümülasyona göre iki farklı şekilde kullanılabilir. Sipariş bazında rezervasyon sisteminde her sipariş için çıkarılan ihtiyaçların başka siparişler tarafından kullanılması engellenirken, rezervasyon sistemi kullanılmadığında ihtiyaçlar kümüle hesaplanmaktadır. MRP'de yapılan yenilikler sipariş bazında rezervasyon sistemi üzerinden gerçekleştirilmektedir. (Uygulama detay dokümanı için [tıklayınız](<Sipariş Bazında Rezervasyon Sistemi.md>).)

**Sipariş bazında rezervasyon sistemi kullanıldığında dengeleme ekranları nasıl** **çalışacaktır?**

Bu sistem kullanıldığında MRP parametrelerinde iş emri ve satıcı sipariş dengeleme parametreleri otomatik işaretlenecektir. Böylece dengeleme ekranlarından açılan iş emri ve satıcı siparişlerinin ilgili müşteri siparişine rezervasyonu otomatik gerçekleşecektir.

**MRP** **kaç** **adımda** **çalıştırılır?**

MRP iki adımda çalıştırılır:

- Gereksinim Planlama işlemi çalıştırılarak, belirtilen teslim tarihi aralığında teslimatı yapılmamış açık durumdaki müşteri siparişleri listelenir.
- Malzeme Gereksinim Planlama işlemi ile bir önceki ekranda belirlenmiş müşteri siparişleri için ihtiyaçların belirlenmesi sağlanır. Bu ekranda Gereksinim Planlama butonu ile MRP tekrar tekrar çalıştırılabilir. Bu parametre işaretlenmeden rapor alınırsa en son çalıştırılan MRP sonuçları gelecektir.

**Malzeme** **gereksinim** **planlamayı** **çalıştırdım** **neden** **stokum** **listeye** **gelmiyor?**

Stok Planlama Kayıtları ekranında ilgili stok için "Planlanacak" parametresi işaretli olmalıdır.

**MRP** **çalıştığında** **hangi** **depoları** **dikkate** **almaktadır?**

Üretim/Kayıt/Şube-Lokal depo tanımlamaları ekranından MRP'ye dahil edilmek istenen daha önceden sistemde tanımlanmış olan lokal depoların eleştirilmesi gereklidir. Bu eşleştirme olmadığı takdirde stokun ilgili depoda bakiyesi olsa bile MRP bu bakiyeyi dikkate almayacaktır.

**MRP** **çalıştığında** **çıkan** **ihtiyaç** **listesindeki** **yükleme** **tarihi,** **teslim** **tarihi,** **bildirim** **tarihi** **gibi** **bilgiler** **nasıl** **hesaplanmaktadır?**

MRP müşteri sipariş kalemlerini dikkate alarak çalışmaktadır. Belirtilen tarihlerde siparişteki mamul kaleminin teslim tarihine göre hesaplanmaktadır. Bu mamul ve mamul reçetesinde yer alan bileşenlerin stok planlama kayıtlarında nakliye günü, bildirim süresi, yükleme günü bilgileri dolu ise bu alanlardaki bilgiye göre tarih alanları mamulün teslim tarihi gecikmeyecek şekilde hesaplanmaktadır.

**Bir sipariş içerisinde aynı kaleme ait birden fazla farklı teslim tarihi olan satır** **var** **ise** **MRP çalıştığında** **iş** **emirlerini kümüle** **etmesi** **nasıl** **sağlanabilir**?

MRP parametrelerinden, Sipariş satırı bazında iş emri ve planlama parametresi kaldırılıp siparişlerin yükleme tarihleri aynı girildiği takdirde, sistemde rezervasyon sistemi açık olsa bile iş emirleri için kümülasyon gerçekleşecektir. Bu işlemin program genelinde değil belirli stoklar için olması isteniyorsa, ilgili parametre kaldırılmadan stok planlama kayıtları ekranından iş emri planlama yöntemi "Sipariş Bazında Değil" olarak seçilerek de kümülasyon sadece ilgili stok için sağlanabilir.

**MRP sonuç raporunda depodan kullanım, siparişten kullanım, talepten kullanım,** **iş emrinden kullanım ne anlama** **gelmektedir?**

Bu alanlar sistemde ilgili yerdeki bakiyelerini göstermektedir. Bakiye kontrolleri yapılarak MRP çalıştırıldıysa ve bu bakiyeler serbest durumda ise MRP yeni öneriler sunmadan önce bu bakiyelerden kullanım gerçekleştirecektir.

**MRP** **sonuç** **raporunda** \*\*\* **işareti** **ne** **anlama** **geliyor?**

Bu işaret hangi kolonun yanında ise onun geciktiği anlamına gelmektedir.

**MRP çalıştırılırken satıcı** **sipariş** **kontrol,** **iş** **emri** **kontrol,** **satın** **alma** **talep** **kontrol** **gibi** **parametreler** **neden** **pasif** **gelir?**

Sipariş bazında rezervasyon, sipariş bazında iş emri ve satıcı siparişi planlama parametreleri kullanılmadığında bu alanlar pasif gelmektedir. Bu durumda MRP buralardaki bakiye kontrolünü yapmadan sadece stok ve mamul bakiye kontrolünü yapabilmektedir.

**MRP ekranında MGP sekmesindeki Min. Stok Kontrol butonu ile MRP çalıştırma** **ekranındaki** **minimum** **stoka** **bakılacak** **parametresi** **arasındaki** **fark** **nedir?**

*Min.stok kontrol* butonu ile gereksinim planlama çalıştığında listeye dahil olmayan, minimum stok kontrolü yapılan mamullerin MRP listesine dahil olması sağlanır. *Minimum* *stoka* *bakılacak* parametresi ile MRP'nin çıkaracağı ihtiyaçlar arasında stok planlama kayıtlarında asgari stok bilgisi girilmiş olan bileşenler için bu ihtiyacın dikkate alınması sağlanır.

**MRP çalıştırma ekranındaki "Belge Detayları Gösterilsin" ve "Kümüle** **Belgelerde** **Siparişler** **Raporlansın"** **parametreleri** **ne** **işe** **yaramaktadır?**

"*Belge* *Detayları Gösterilsin*" parametresi MRP sonuçlarının gösterildiği "Sipariş" sekmesinde, eğer mevcut belgeler (iş emri/talep/satıcı siparişi) ile eşleşme sağlandıysa (yani mevcut belgeler ihtiyacı karşılamak için kullanıldıysa) bu belgelerin FISNO, TESLIM_MIKTARI vs. gibi detaylarını göstermek için kullanılmaktadır. "*Kümüle* *Belgelerde* *Siparişler* *Raporlansın*" parametresi ise sipariş bazında takip edilmeyen ve günlük/haftalık/aylık vs. kümüle edilen belgelerin (iş emri/talep/satıcı siparişi) hangi siparişler için oluşturulduğu detayını MRP sonuçları "Sipariş" sekmesinde göstermek için kullanılabilir.

**MRP'de** **iş** **emri** **reçetesi** **kullanılsın** **parametresinin** **çalışma** **koşulları** **nelerdir?**

MRP'de iş emri reçetesi kullanılsın parametresinin çalışma koşulları şunlardır:

- Sipariş bazında rezervasyon parametresi açık olmalıdır.
- İş emrinde sipariş numarası ve sip. kont seçilmiş ise saklanan reçeteye göre MRP çalışmaktadır.
- Eğer iş emrinde seçilmemiş ise stok planlama kayıtlarında iş emri ve planlama yöntemi sipariş bazında değil seçilmiş olmalıdır.( Sipariş bazında işaretli ise saklanan reçeteyi görmemektedir).
- MRP çalıştırılırken "İş emri reçetesi kontrol edilsin" parametresi işaretlenmelidir.

**MRP, mamülün reçetesinde bulunan bir yarı mamüle ait alternatif reçete** **varsa** **bunu** **dikkate** **alır** **mı?**

Mamul reçetesinde ilgili yarı mamül için alt.kodu bilgisi girilmişse MRP bu bilgiyi dikkate alarak çalışacaktır. MRP çalıştırılırken iş emri reçetesi kontrolü yapılırsa, sistem alternatif reçeteyi değil iş emri reçetesini dikkate alacaktır.

![](../_assets/648bbcf40d5bb0f05ecb.png)

**"MRP Sonuçlarından İş Emri/Talep/Sipariş Oluşturma" ekranlarında üst bölümdeki araç çubuğunda yer alan "Teslimat Tarihini Düzelt" ve "Miktar Düzelt" butonları ne işe yaramaktadır?**

MRP sonuçlarında "Güncellenecek Belgeler" olarak önerilen belgeler için Teslim Tarihi ve Miktar değişiklikleri önerilmektedir. Teslim Tarihi ve Miktar butonlar yardımıyla güncellenecek belgelere ait satırların sadece teslim tarihini veya miktarını düzeltebilmek için topluca komut verilebilir. Örneğin bu butonlar arasından Teslimat Tarihini Düzelt tıklanırsa güncellenecek satırlar içinde sadece teslim tarihi değişiklikleri yapılacaktır ve miktar değişiklikleri yapılmayacaktır. Ya da "Hepsi" butonuna tıklanarak bütün güncelleme önerileri kabul edilebilir. Teslim Tarihi ve Miktar Düzelt butonlarının MRP sonuçlarından farklı olarak kullanıcının manuel olarak tarih veya miktar vermesini sağlayacak bir fonksiyonu yoktur, sadece hangi alandaki değişiklikleri sonuca yansıtmak istediğimizi seçmemizi sağlar.

**Sipariş bazında rezervasyon sistemi kullanılıyor, stok planlama kayıtlarında iş emri ve satıcı siparişi planlama yöntemi olarak "Sipariş Bazında" seçili, ayrıca MRP parametrelerindeki planlama yöntemleri de "Sipariş Bazında" olarak seçiliyor. Ancak yine de MRP sonuçlarında bazı stok kodları için sipariş bazında sonuç alamıyorum, neden olabilir?**

İlgili stok kodları için stok planlama kayıtları ekranında parti büyüklüğü ve minimum sipariş miktarı tanımlanmış olabilir, bu durumda sipariş bazında takip edilmeyecektir. Çünkü parti büyüklüğü veya minimum sipariş miktarı bulunan bir stoğu sipariş bazında takip ettiğimiz durumlarda, fazladan iş emri/satıcı siparişi açılmasına sebep olmaktadır.

**Programda fabrika bazında MRP çalıştırılması destekleniyor mu?**

Evet, desteklenmektedir. Bunun için Şube/Lokal Depo tanımlama ekranından şube ya da depo bazında fabrika gruplaması yapılabilir. İşlem detaylarına doküman [linkinden](<Fabrika Bazında MRP.md>) erişilebilir.)

**MRP çalıştığında farklı şubedeki bir depoyu dikkate alması nasıl sağlanabilir?**

Şube/Lokal depo tanımlama ekranından ilgili depo şube olarak eklenebilir. Bu işlem esnasında default gelen 0000 fabrika kodu değiştirilmemelidir.

**MRP çalıştırma işleminde TBLMRPSIP kayıtlarının veritabanına aktarımı işleminde SqlDateTime taşması uyarısı alındığında neler kontrol edilmeli?**

TBLCARISTOK tablosunda olması gereken öndeğer tanımlamalar kontrol edilip, mevcut kayıtlarda sorun var ise düzeltilmelidir. Ayrıca alınan uyarıya bağlı olarak tedarik süresi/tedarik miktarının fazla ve ihtiyaç miktarının yüksek olup olmadığı kontrol edilmelidir.

**MRP çalıştırılırken kapasite planlama uygulaması kullanılıyor. Çıkan kapasite planlama raporunda "Kapasite Detay Sonuçları" sekmesinde "İş Emri No" alanı boş geliyor. Neden olabilir?**

"Kapasite Detay Sonuçları" sekmesindeki "İş Emri No" alanının dolu olması için MRP'nin mevcut bir iş emrini kullanması ve bu iş emrini planlaması gerekmektedir. Eğer MRP yeni bir iş emri öneriyorsa, bu iş emrinin numarası belli olmadığı için "İş Emri No" sahası boş gelecektir.

**MRP çalıştırılırken Insert Into MRP_DETAIL (…) uyarısı alınıyorsa ne yapılmalıdır?**

TBLMRP_DETAIL tablosu altında yer alan Fkeyler kontrol edilmeli ve bu tablo altında tanımlı bir Pkey varsa silinmelidir. (Lokalde yer alan tablo ile kıyaslanarak işlemler yapılabilir)

**MRP raporu alındığında istenen özellikler desteklenmiyor (The requested properties cannot be supported) uyarısı alınıyorsa ne yapılmalıdır?**

SQL üzerinden ilgili datanın sağ klik özellikler options kısmından compatibility level değeri artırılmalıdır.

**MRP sonuç raporuna kapasite planı yapılmayan işler sekmesinde vardiya planı bulunamadı mesajı alındığında ne yapılmalıdır?**

İş istasyonunda vardiya tanımı yapılmalıdır.

**Operasyon tanımlama ekranında Sim. Tez. Miktarı alanı MRP de dikkate alınıyor mu? MRP, kapasite planlamada operasyon sürelerini nereden okuyor?**

Operasyon tanımlama ve reçete kaydı ekranında bulunan "Sim. Tez. Miktarı" mevcut sürümlerde desteklenen bir özellik değildir, yapılan tanımın üretim süresi/miktarına bir etkisi yoktur.

Reçetelerden getirilsin işaretlendiğinde reçetelerdeki operasyonları ve sürelerini dikkate alır aynı zamanda program rota bilgilerini de reçetede tanımlı operasyonlardan alır. Eğer ileri üretim çizelgeleme kullanılıyor ise çizelgeleme üzerinden getirilsin işaretlendiğinde ileri üretim çizelgeleme altında bulunan rota tanımlarını ve ileri üretim planlamadaki operasyon sürelerini dikkate alır.

Reçetede operasyonların tanımlı olmadığı ve ileri üretim planlamanın kullanılmadığı durumda kapasite planlama yapabilmek için kapasite planlama verisi kullanılsın işaretlenebilir. Bu durumda MRP kayıt menüsünün altında rota tanımlama adıyla yeni bir ekran gelecektir. Rota tanımlama ekranından ürünün rotasındaki operasyonlar makineler ile eşleştirilerek üretim süreleri tanımlanır ve kapasite sonuçları buna göre raporlanır.

**MRP’nin önerdiği ihtiyaçların otomatik açılması sağlanabilir mi?**

MRP çalışması sonrası ortaya çıkan ihtiyaçlar için gerekli olan iş emirleri, satın alma talepleri, satıcı siparişleri dengeleme ekranlarından otomatik olarak açılabilmektedir. Malzeme gereksinimden talep oluşturma /sipariş oluşturma/iş emri oluşturma ekranlarından, MRP'nin çıkardığı ihtiyaçlar mevcut belgelerle eşlenebildiği gibi, yeni kayıtlar açılabilmekte, mevcut belgeler miktar ya da teslim tarihine göre düzenlenebilmekte ya da iptal edilebilmektedir.

Sipariş bazında rezervasyon sistemi ile MRP çalıştırıldığında ise dengeleme işlemleri müşteri siparişi bazında gerçekleşmektedir.

**MRP'den iş emri oluşturmada ihtiyaç kümülasyon seçenekleri neden gelmiyor?**

Sipariş bazında rezervasyon parametresi açık olduğunda bu seçenek gelmeyecektir.

**MRP çalıştırıldığında belli bir hammadde kodu için mevcut satıcı siparişleri kullanılmıyor ve yeni belge öneriliyor. Diğer hammadde kodları için böyle bir sorun olmuyor. Neden olabilir?**

Eğer satıcı siparişlerinin teslim tarihi ihtiyaç tarihinden büyük ise, satıcı siparişlerinin kullanılabilmesi için MRP çalıştırılırken ""İleri Tarihli Belgelerle Eşleştirme Yapılsın" parametresi işaretlenmelidir.

Ayrıca ilgili hammadde kodu ve satıcı siparişlerindeki cari kodu için müşteri-satıcı stok kaydı tanımı bulunuyorsa, bu tanımın sipariş oranı 0'dan büyük olmalıdır. Aksi halde mevcut satıcı siparişleri kullanılmayacaktır.
