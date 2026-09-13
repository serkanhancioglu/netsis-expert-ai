---
title: "Netsis DDMRP-Talebe Dayalı Malzeme İhtiyaç Planlama"
page_id: "66237063"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis DDMRP-Talebe Dayalı Malzeme İhtiyaç Planlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis DDMRP-Talebe Dayalı Malzeme İhtiyaç Planlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWFlNjk5MzVlLTllOGItNGI2ZS1hMjUzLThmYTAyMzNmNTE1NCZsaW5rPTFhZWFkYzI2LWZlMzctNGU2MC1hNWIzLThlNmM3OGJmYTAxZSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=ae69935e-9e8b-4b6e-a253-8fa0233f5154&link=1aeadc26-fe37-4e60-a5b3-8e6c78bfa01e&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-ddmrp-talebe-dayali-malzeme-ihtiyac-planlama_66237066_66237063.html"
source_version: "2022-11-02T15:09:30.467+03:00"
source_bytes: 1614525
fetched_at: "2026-09-13T04:24:36+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis DDMRP-Talebe Dayalı Malzeme İhtiyaç Planlama

Netsis DDMRP-Talebe Dayalı Malzeme İhtiyaç Planlama ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

> [!TIP]
> İlgili özelliğin anlatımını içeren webinar kaydına ulaşmak için [tıklayınız.](https://register.gotowebinar.com/recording/5168481320198735361)

Tedarik zincirleri çok sayıda operasyon ve paydaş içeren karmaşık sistemlerdir. Dolayısıyla bu kompleks yapıların yönetimi her zaman kritik ve zorlayıcı olmuştur. Zincirin sorunsuz işlemesini sağlamak için tutarlı ve ayrıntılı planlar yapma ihtiyacı her dönem önemini korumuştur. Üstelik zamanla tüketim hacminin ve hızının artması tedarik zinciri içinde yapılacak planların her zamankinden daha dinamik ve daha güvenilir olması ihtiyacını da doğurmuştur. Bu noktada Malzeme İhtiyaç Planlama (MRP-Material Requirements Planning) doğmuş ve ilk günden beri sistemin tüm paydaşları için vazgeçilmez bir planlama aracı olmuştur.

MRP 1950'li yıllarda geliştirilmiş bir metodoloji olmasına rağmen yıllardır önemini kaybetmemiştir. MRP'nin önemini koruyor olması, çözüm ürettiği sistemlerin de hala var olmasıyla ve hatta daha da karmaşıklaşmasıyla açıklanabilse de metodolojinin yaklaşık 70 yıldır pek de değişmemiş olması birtakım soru işaretlerini beraberinde getirmektedir. Çünkü MRP metodolojisi oluşturulduğunda var olan hemen hemen tüm koşullar değişmiş ancak MRP aynı kalmıştır. MRP'nin geliştirildiği günden bu yana müşteri tolerans limitlerinin azalması, ürün yaşam döngülerinin ve tedarik sürelerinin kısalması, ürün çeşitliliğinin ve karmaşıklığının artması gibi onlarca değişim sayılabilmektedir. Elbette tedarik zincirindeki ürünlerin hepsi bu değişimlerden aynı düzeyde etkilenmemiştir ancak yine de tüm işletmeler için bu değişimleri şiddetli yaşayan en az bir ürünün varlığından söz edilebilmektedir.

Bu bilgilere ek olarak MRP metodolojisinin katı yapısından ve pratikle tam olarak örtüşmeyen varsayımlar üzerine inşa edilmiş olmasından da bahsedilmelidir. Örneğin MRP; ürün ağaçlarının %100 doğru olduğunu, her malzemenin stok giriş çıkışının mutlaka kaydedildiğini, tüm siparişlerin bağımsız olduğunu ve hiçbir siparişin tüm bileşenleri hazır olmadan başlamadığını varsayar. Ancak uygulamada bunların eksiksiz gerçekleşmesi mümkün olamamaktadır. Ayrıca MRP'nin tahminlemelerden yararlanması ve tahminlerin doğası gereği sapmalar içeriyor oluşu da MRP ile ilgili soru işaretlerini güçlendirmiş ve bazı çevreler tarafından yeni bir tedarik zinciri yönetim aracı arayışına sebep olmuştur.

MRP hakkında değinilen tüm bu itirazlar ve burada bahsedilmeyen daha da fazlası sebebiyle yeni bir planlama aracı olarak *Talebe* *Dayalı* *Malzeme* *İhtiyaç* *Planlama* metodolojisi geliştirilmiş ve tüm metodoloji bir kitapta ortaya konmuştur<sup>\*</sup>. Talebe Dayalı Malzeme İhtiyaç Planlama yani bir diğer ifadeyle DDMRP (Demand Driven Material Requirements Planning), en temelde kamçı etkisine (Bullwhip effect) çözüm bulmayı hedeflemektedir. Tedarik zinciri problemlerinden biri olarak literatüre geçen kamçı etkisi, müşteri talebindeki yukarı ya da aşağı yönlü küçük dalgalanmaların bile tedarik zinciri boyunca ilerlendiğinde, zincirin her bir halkasında daha da şiddetlendiğini ifade etmektedir. Bu etki kamçıların salınımına benzetilerek tarif edilmiş ve bir kamçı için hareketin kaynağında dalga büyüklüğü ve gerilim minimumken hareket kaynağından uzaklaştıkça kamçıdaki gerilim ve dalga şiddetinin katlanarak artması vurgulanmıştır.

DDMRP'nin kamçı etkisine önerdiğin çözümse aslında metodolojinin de temelini oluşturmaktadır. DDMRP, kamçı etkisinin tedarik zinciri halkaları boyunca şiddetlenerek artmasını engellemek için zincirin stratejik olarak belirlenecek bölgelerinde tampon stoklar tutmayı ve böylece zincir üzerinde *ayrıştırılmış* bölgeler yaratmayı önermektedir. Tampon stok bulundurarak *ayrıştırılan* bölgeler, zincirin bağımlı parçalarını bağımsız duruma getirmekte ve bağımsız planlama ve uygulama alanları yaratmaktadır. Bahsedilen ayrıştırma noktalarında, olası arz ve talep değişkenliklerinin birikimi engellenmekte ve kamçı etkisini çift yönde kesecek duvarlar oluşturulmaktadır.

DDMRP stratejik olarak yerleri belirlenecek ayrıştırma noktalarında tutulacak tampon stoklar (buffer) için genel kullanımda 3 seviye önermektedir. Bu seviyeler kırmızı, sarı ve yeşil renklerle belirtilmekte ve her bir buffer noktası için ayrı ayrı hesaplanmaktadır. Ayrıca DDMRP tampon stoklar için farklı profiller belirlemeyi, stokların profillerine göre yönetilmesini önermektedir. Stokların tampon profilleri; tedarik şekillerine (üretim ya da satın alma), talep değişkenlik seviyelerine ve tedarik sürelerine (lead time) göre belirlenmektedir. Stokların tampon miktarları belirlenirken de bu tampon profilleri dikkate alınmaktadır. Son olarak DDMRP'nin planlama sisteminin temelinde stokların ortalama günlük tüketimleri çok önemli bir rol oynamakta ve tüm hesaplamalara dahil olan bu parametre sık sık yeniden hesaplanmaktadır.

DDMRP metodolojisiyle ilgili bahsedilen özet bilgilere ek olarak, bu malzeme yönetim şeklinin MRP yerine geçecek bir sistem olmadığını vurgulamak gerekmektedir. Geleneksel MRP'nin hantal kaldığı ve dinamizm yönünden yetersiz bulunduğu değişkenlikteki stokların yönetimi için DDMRP'nin değerlendirilmesi yerinde olacaktır. DDMRP ile stok yönetimi yapmak, tüm stokları bu metotla yönetmeyi gerektirmemektedir. Stratejik olarak ihtiyaç duyulan stokların yönetimi DDMRP ile yapılırken, MRP ile verimli şekilde yönetilen stoklar için değişiklik yapılması gerekmemekte, hibrit bir yaklaşımla malzeme ihtiyaç planlaması yapılabilmektedir.

Malzeme ihtiyaç planlamaları için alternatif yöntemler arayan Logo Netsis kullanıcıları için desteklenen Talebe Dayalı MRP (DDMPR) uygulamasından yaralanmak için Netsis 3 Enterprise ve Netsis Wings Enterprise çözümlerinden birine sahip olma şartı aranmaktadır.

#### Parametreler

DDMRP metodolojisinin mantığı ve çözüm ürettiği sorunlar anlaşıldıktan sonra yapılması gereken ilk şey hangi stokların *Talebe* *Dayalı* *MRP* ile takip edileceğinin belirlenmesidir. Bu karar stratejik bir karar olup her işletme için farklılık gösterecektir. Dolayısıyla hangi stokların DDMRP ile takip edilmesi gerektiğiyle ilgili bir kural, bir formül bulunmamaktadır. Bununla birlikte klasik MRP ile malzeme planlaması yapılırken yaşanabilecek şu durumların, ilgili stoklar için DDMRP seçeneğini değerlendirme anlamında kritik sinyaller olduğu söylenebilir; klasik MRP ile yönetilirken sık sık eksik ya da fazla malzeme bulundurulması sorunuyla karşılaşılması, tedarik süreçleri kaynaklı müşteri memnuniyetsizliğinin yüksek olması, talep tahminlerinin sürekli olarak yüksek sapma içermesi, müşteri taleplerinin değişkenliğinin çok yüksek olması.

Stratejik gerekçeleri saptanarak DDMRP ile yönetilmesine karar verilen stoklar için Logo Netsis'te yapılması gereken ilk işlem Lojistik-Satış  Stok  Kayıt yolu izlenerek ulaşılan Stok Planlama Kayıtları ekranının Planlama-2 sekmesinde bulunan "Talebe Dayalı MRP Parametreleri" alanına uygun girişlerin yapılmasıdır. Bu bölümdeki "MRP Politikası" parametresinin "Talebe Dayalı" olarak ayarlanması, ilgili stokun DDMRP ile yönetileceği anlamına gelmektedir. (Bkz. Ekran Görüntüsü 1) DDMRP'nin şu anda desteklenmiş versiyonu yalnızca ham maddelerin ve satın alma yoluyla tedarik edilen ticari malların bu yöntemle yönetilmesini desteklemektedir. Yarı mamullerin DDMRP ile takibi mevcut versiyonda desteklenmemektedir.

DDMRP hakkında dokümanın sonraki bölümlerinde detayları anlatılacak konulardan biri de tedarik süresidir. DDMRP ile yönetilen stokların tedarik süreleri, *ayrıştırma noktalarında* tutulacak tampon stok seviyelerinin belirlenmesinde kullanılmaktadır. Dolayısıyla son derece önemli verilerdir. DDMRP metodolojisiyle planlaması yapılan stoklar için tedarik süresi yeniden hesaplanmakta ve bu yeniden hesaplanan tedarik süresine *ayrıştırılmış tedarik süresi (decoupled lead time)* denilmektedir.

Programda klasik tedarik süresi hesaplama işlemlerinde de Stok Planlama Kayıtları ekranındaki verilerden yararlanılmaktadır. Tedarik süresi hesaplamasına katılan Bildirim/Üretim Süresi, Nakliye Süresi ve Üretim Transfer Süresi verileri, Stok Planlama Kayıtları ekranının Planlama-1 sekmesinde yer almaktadır.

![](../_assets/15c5bd0f6d9b4f04659b.png)

![](../_assets/98fe74db9c5592ae51e6.png)

Ayrıca DDMRP metodolojisi kapsamında, malzeme planlama aşamasında ihtiyaç duyulan Ani Yükseliş Ufku Katsayısı, Ani Yükseliş Ufku Sabit Değeri ve Ani Yükseliş Eşiği Katsayısı olmak üzere 3 farklı parametre daha bulunmaktadır. Bu parametreler varsayılan değerleriyle birlikte "MRP Parametreleri" ekranının "Genel-2" sekmesine eklenmiştir. İstenmesi halinde varsayılan değerlerin kullanıcı tarafından değiştirilmesine izin verilmektedir. İlgili parametrelerin kullanım detayları hakkında detaylı bilgi için Bölüm 5 incelenmelidir.

#### Talebe Dayalı MRP Veri Yönetimi Ekranı

DDMRP ile planlama yapılırken kullanılacak ekranlardan ilki olan Talebe Dayalı MRP Veri Yönetimi ekranına ulaşmak için, Üretim-MRP-Kayıt-Talebe Dayalı MRP yolu izlenmelidir.

Talebe Dayalı MRP'nin (DDMRP), klasik MRP'ye göre üstünlük sağladığı en önemli konu dinamik oluşudur. Bu dinamizm, değişkenliği yüksek stokların planlamasında özellikle öne çıkmaktadır. DDMRP'nin dinamik oluşu ise metodolojinin planlama hesaplarında kullandığı verilerin güncelleme sıklığını kullanıcı ihtiyacına bırakmasından kaynaklanmaktadır. Bu yaklaşım sayesinde sezonsallık ya da önemli bir tedarik sıkıntısı gibi arz ve/veya talepte dalgalanma yaratacak değişiklikler için verilerin güncellenmesi ve tampon stoklarının bu yeni verilere göre yeniden belirlenmesi sağlanabilmektedir. Talebe Dayalı MRP Veri Yönetimi ekranı ise bahsedilen bu verilerin güncelleme işleminin yapılabileceği ekrandır.

![](../_assets/59dc47aca2f723cbc278.png)

Talebe Dayalı MRP Veri Yönetimi ekranı 2 sekmeden oluşmaktadır. Bunlardan ilki olan *Kısıtlar* sekmesi, hangi stoklar için DDMRP tampon seviyelerinin hesaplanmasında yararlanılan dinamik verilerin yeniden hesaplanmasının istendiğine dair stok seçimi yapılabilecek alandır. İlgili sekmede Stok Kodu, Grup Kodu, Kod 1-2-3-4-5 alanları için filtre verilebildiği gibi ileri kısıt girişi yapılması da mümkündür. DDMRP uygulaması kapsamında esnek yapılandırma desteği sağlanmıştır. Esnek yapılandırma kullanımında, stok kodu ve yapılandırma kodu bazında seçim yapılabilmektedir.

Bunlara ek olarak, *Kısıtlar* sekmesi üzerinden stokların MRP politikalarına göre filtrelenmesi sağlanabilmektedir. Bunun için ekran görüntüsünde yeşil kutucuk içinde gösterilen *MRP Politikası* alanından seçim yapılabilir. Bu alanda "Klasik" seçimi yapıldığında geleneksel MRP ile planlanan stoklar, "Talebe Dayalı MRP" seçildiğinde DDMRP ile planlanan stoklar listelenecektir. Gerekli filtreler ilgili sekmede verildikten sonra seçime uygun stokların listelenmesi için ekranın sağ alt köşesindeki "Kayıtları Getir" butonuna tıklanmalıdır.

*Kayıtları Getir* butonuna tıklandıktan sonra otomatik olarak "Stok Listesi" sekmesine geçilecek ve seçilen stoklara ait dinamik verilerin de izlenebildiği bir grid alan görüntülenecektir.

![](../_assets/85ff3de8ae2901a4ca5e.png)

*Stok* *Listesi* sekmesinde listelenen tüm stoklar için bu bölümün devamında detayları anlatılan dinamik veriler hesaplanmış olmayabilir. Eğer verilerin hesaplanması isteniyorsa ekrandaki "Hesapla" butonuna tıklanmalıdır. Daha önce "Hesapla" butonuna tıklanarak verileri hesaplanan stoklar için *Stok* *Listesi* sekmesinde son hesaplama sonuçları gösterilirken, daha önce hiç hesaplama yapılmamış stoklar için de ilgili alanlar boş görünecektir. Sekmedeki listeden hesaplama yapılmak istenen stoklar seçildikten sonra *Hesapla* butonuna tıklandığında ise ekranda hangi verilerin hesaplanmak istediğinin seçilebileceği "Parametreler" ara ekranı görüntülenecek ve burada yapılacak tercihlere göre seçili stokların ilgili verileri yeniden hesaplanacaktır. Bu veriler bazı stoklar için ilk kez hesaplanırken bazı stoklar için güncel bilgiler kullanılarak yeniden hesaplanacak olabilir.

![](../_assets/17dff4066d0dd6adaff1.png)

Talebe Dayalı MRP Veri Yönetimi ekranının *Stok* *Listesi* sekmesinden seçilip *Hesapla* butonuna tıklanan stoklar için hesaplanabilecek veriler, Ekran Görüntüsü 5'te görülen *Parametreler* ekranında gösterilmiştir. Bu veriler Ortalama Günlük Tüketim, Değişkenlik Sınıflandırması, Değer Sınıflandırması, Reçete Kullanım Sınıflandırması, Tedarik Süresi Sınıflandırması ve Ayrıştırılmış Tedarik Süresi'dir. Bu verilerden hangilerinin yeniden (Bazı stoklar için ilk kez olabilir.) hesaplanmak istendiği, 5. Ekran Görüntüsü'nde yeşil alanlar içinde gösterilen seçim kutucukları kullanılarak belirlenebilmektedir.

Talebe Dayalı MRP Veri Yönetimi ekranının kullanımıyla ilgili diğer ayrıntılar anlatılmadan önce, *Parametreler* ara ekranında yer alan dinamik verilerden ve bu verilerin DDMRP metodolojisindeki işlevlerinden bahsedilecektir.

#### Ortalama Günlük Tüketim (OGT)

Ortalama günlük tüketim (OGT) bilgisi, DDMRP'nin en önemli bileşeni olan ayrıştırma noktalarında tutulacak tampon stok seviyesi hesabına doğrudan dahil olan bir çarpandır. DDMRP'nin klasik MRP'ye göre üstünlüğü de tutulacak tampon stokların ihtiyaç oldukça yeniden belirlenmesine imkan vermesinden ileri gelmektedir. Yeniden tampon stok seviyesi hesaplarken ortalama günlük tüketim (average daily usage) bilgisi de hesaplamaya doğrudan dahil olduğundan, OGT verisinde kayda değer bir dalgalanmanın varlığı durumunda OGT'nin de yeniden hesaplanması anlamlı olacaktır. OGT hesabı yapılabilmesi için Geçmiş Hafta Sayısı, Gelecek Hafta Sayısı ve Gelecek Dönem Veri Kaynağı bilgileri kullanılmaktadır. Bu bilgiler *Parametreler* ara ekranının OGT hesaplaması ile ilgili alanında görülmektedir. (Bkz. Ekran Görüntüsü 6) Burada yapılacak OGT hesabı için ilgili alanların kullanım durumuna göre 3 alternatif vardır; yalnızca geçmiş veriye göre, yalnızca gelecek veriye göre ya da her iki veri tipini de dikkate alarak OGT hesaplanabilmektedir.

![](../_assets/99c1f03124609b2f1376.png)

Ekrandaki "Geçmiş Hafta Sayısı" alanına girilecek değer, geçmiş kaç haftanın verileri kullanılarak OGT hesaplanmak istendiğini ifade etmektedir. Geri gidilecek hafta sayısına göre devir şirketleri için de kontrol sağlanmaktadır. Benzer şekilde "Gelecek Hafta Sayısı" alanına girilecek değer de gelecek kaç haftanın verileri kullanılarak OGT hesaplanmak istendiğini belirtmektedir. Hesaplamaya dahil edilmek istenmeyen bir veri tipi için ilgili alan 0 bırakılabilir ancak hem gelecek hem de geçmiş hafta sayısı alanlarının 0 olarak bırakılmasına izin verilmemektedir. Bu alanlardan biri mutlaka sıfırdan büyük bir değerle doldurulmalıdır.

OGT hesaplamasında gelecek verileri kullanılmak istendiğinde ve buna karşılık "Gelecek Hafta Sayısı" alanına sıfırdan büyük bir değer girildiğinde ilgili alanın hemen altındaki "Gelecek Dönem Veri Kaynağı" alanı aktifleşecektir. Bu alandan gelecek dönem verileri için Müşteri Siparişleri, Tahminleme Kayıtları, Tahminleme Kayıtları&Müşteri Siparişleri ya da Son Çalışan MRP Sonucu veri kaynaklarından biri seçilmelidir. İlgili alandan *Tahminleme Kayıtları'nı* içeren bir veri kaynağı seçilmesi halinde, alanın hemen altındaki "Tahmin No" alanı aktifleşecek ve alan rehberinden veri olarak kullanılmak istenen tahminleme numarası seçilebilecektir.

Geçmiş ve gelecek hafta sayısı alanları için hiyerarşik olarak öncelikli veri, Stok Planlama Kayıtları ekranının Planlama-2 sekmesinde yer alan Talebe Dayalı MRP Parametreleri bölümünün "Geçmiş Hafta Sayısı" ve "Gelecek Hafta Sayısı" sahalarıdır. Eğer bu alanlarda stok bazında bir geçmiş ya da gelecek hafta sayısı bilgisi mevcutsa, *Parametreler* ekranındaki geçmiş ve/veya gelecek hafta sayısı alanlarına girilen değerler ezilecektir.

#### Değişkenlik Sınıflandırması (XYZ)

#### ![](../_assets/c04e83defdca4126fdf4.png)

DDMRP metodolojisi kapsamında hesaplamaları etkileyen farklı stok sınıflandırma tipleri bulunmaktadır. Bunlardan biri stokların değişkenlik sınıflandırması olarak adlandırılan XYZ sınıflandırmasıdır. Bu sınıflandırma stokların çıkış hareketleri üzerinden yapılır ve dolayısıyla talepteki değişkenliğin seviyesini ölçmeye çalışır. Yapılan sınıflandırmaya göre stoklar X, Y ya da Z olarak kategorilendirilir.

XYZ sınıflandırması sırasında seçilen periyot için stok bazında çıkış hareketlerinin standart sapmaları ve ortalamaları hesaplanıp oranlanır. Bu oran üzerinden stokların sınıfları belirlenir. X sınıfı düşük talep değişkenliğini temsil ederken Y orta, Z ise yüksek değişkenlik anlamına gelmektedir. Seçilen hesaplama dönemi için hiç çıkış hareketi olmayan stoklar doğrudan X olarak değerlendirilecektir.

XYZ sınıflandırmasının hesaplanacağı dönem ekran görüntüsünde yeşil kutucuk içinde gösterilen "Başlangıç Tarihi" alanı kullanılarak yapılır. Ayrıca "Periyot Tipi" alanından *Hafta* ya da *Ay* seçimi yapılarak ilgili hesaplamanın hangi periyot tipi için yapılacağı seçilebilmektedir.

#### Değer Sınıflandırması (ABC)

#### ![](../_assets/7c5a60df0964e19cabe0.png)

DDMRP desteği kapsamında analizi yapılan stok sınıflandırmalarından bir diğeri, değer sınıflandırması olarak adlandırılan ABC sınıflandırmasıdır. ABC sınıflandırması yine stokların çıkış hareketleri üzerinden yapılır ancak bu kez çıkış hareketleriyle birlikte stokların fiyatları da hesaplamaya dahil edilir.

ABC analizi yapılırken seçilen dönem için çıkış hareketi bulunan stokların, aynı dönemdeki tüm çıkış hareketleri içindeki paylarına bakılır. Bu pay Ekran Görüntüsü 8'de gösterilen "Fiyat Kriteri" alanından seçilecek *Net* *Fiyat* ya da *Birim* *Maliyet* cinsinden hesaplanır. Hesap yapılacak dönem, kullanıcı tarafından verilen *Başlangıç Tarihi* baz alınarak belirlenir. Ayrıca stokların hesaplanan maddi değer açısından payları kümüle edilerek, toplam yaratılan değerin içinde hangi stokların hangi seviyede pay sahibi olduğu değerlendirilir ve bunun sonucunda stoklara A, B ya da C sınıfları atanır.

Özetle ABC sınıflandırması, stokların yarattığı mali değere göre yapılan bir sınıflandırmadır. Değeri en yüksek stoklar A, orta seviye değer yaratan stoklar B ve en az değeri yaratan stoklar C sınıfı olarak değerlendirilir. Seçilen dönem için hiçbir çıkış hareketi bulanmayan stoklar da C grubu olarak işlem görecektir. Stokların yarattığı değerin analiz edilmesi, hangi stokların malzeme planlamada hangi seviyede önem taşıdığına dair önemli bir bilgidir. Bu nedenle DDMRP kapsamında ABC analizi desteklenmiştir ancak bu sınıflandırma DDMRP içindeki hesaplamalara doğrudan etki etmemektedir. ABC analizi, sistemin bütünsel anlamda bir değerlendirmesinin yapılmasına yardımcı olması amacıyla bulunmaktadır.

#### Reçete Kullanım Sınıflandırması (PQR)

DDMRP ile çalışırken analiz aracı olarak kullanılan bir diğer sınıflandırma ise PQR sınıflandırmasıdır. Bu sınıflandırma üretim reçeteleri (BOM) seviyelerinin kontrolüyle yapılır. PQR sınıflandırması için üretim reçeteleri en tepeden en alt seviyeye kadar tüm dallarıyla taranır. Stok bazında bir materyalin reçete içinde kaç kez tekrar ettiğine bakılır ve buna göre ilgili stoklar P, Q ya da R olarak kategorilendirilir.

![](../_assets/d7ca72b0047ce0c2cc63.png)

PQR sınıflandırması, DDMRP'nin kilit bilgisi olan ayrıştırma noktalarının reçetelerdeki hangi stok seviyelerine koyulabileceği konusunda yol gösterici olma konusunda önemlidir. Ayrıca PQR sınıflandırması, bir stokun ayrıştırma noktası olarak belirlenmesi halinde planlamaya ne seviyede etki edeceğine dair çıkarım yapılabilmesine de yardımcı olmaktadır. Bu sebeplerle PQR sınıflandırması DDMRP kapsamında desteklenmiştir ancak bu bilgi yapılan hesaplamalarda doğrudan kullanılmamaktadır. Analiz amaçlı kullanılabilecek bir veridir.

#### Tedarik Süresi Sınıflandırması (EFG)

DDMRP kapsamında yapılan son stok sınıflandırması ise EFG sınıflandırmasıdır. EFG sınıflandırması stokların tedarik sürelerine göre yapılmaktadır. Ancak buradaki tedarik süresi, DDMRP tarafından kullanılan *Ayrıştırılmış Tedarik Süresi'dir (ATS).* Programda genel kullanımda tedarik süresi (lead time) hesaplanırken üretim, nakliye ve transfer sürelerinin toplamına bakılmaktadır. Aynı durum DDMRP ile yönetilen ancak reçetesi bulunmayan, yani üretimi yapılmadan alınıp satılan ticari mallar için de geçerlidir. DDMRP'nin *ayrıştırılmış* *tedarik* *süresi* *(ATS)* kavramı, sistemde reçetesi bulunan tepe mamuller için anlamlıdır. Dolayısıyla DDMRP ile planlanan, sistemde reçetesi bulunan ve reçetede son ürün olan (Mevcut versiyonda yarı mamuller için DDMRP desteklenmemiştir.) stoklar için ayrıştırılmış tedarik süresi hesaplanmaktadır ve bu hesaplamaya göre ilgili stoklar E, F ya da G gruplarından birine atanmaktadır. Bu bilgiden de anlaşılacağı üzere EFG sınıflandırmasının yapılabilmesi için öncesinde ayrıştırılmış tedarik süresinin hesaplanmış olması gerekmektedir. Bu yüzden Ekran Görüntüsü 10'da gösterilen "Tedarik Süresi Sınıflandırması (EFG) Yapılsın" parametresi işaretlendiğinde, "Ayrıştırılmış Tedarik Süresi Hesaplansın" parametresi de otomatik olarak işaretlenmektedir.

![](../_assets/b4225c5ba22156b75bbd.png)

Ayrıştırılmış tedarik sürelerine göre sınıflandırılan mamullerden; E grubu ATS'si düşük (3 gün ya da daha kısa), F grubu ATS'si orta uzunlukta (3 ila 5 gün) ve G grubu ATS'si yüksek (5 günden büyük) stokları temsil etmektedir.

#### Ayrıştırılmış Tedarik Süresi (ATS) Hesaplaması

Bir önceki bölümde bahsedildiği gibi ayrıştırılmış tedarik süresi, sistemde reçetesi olan tepe mamuller için anlamlı bir kavramdır. Ayrıştırılmış tedarik süresi hesaplanırken bir ürün reçetesinin (BOM) tüm dalları ve basamakları ele alınır. Bu dallar içinden tedarik süresi cinsinden en uzun dal seçilir ve ilgili dal üzerindeki tüm bileşenlerin tedarik süreleri toplanarak tepe mamulün tedarik süresine ulaşılır.

Ekran Görüntüsü 11'deki örnekte tepe mamul X ve bileşenlerini içeren ürün reçetesi görülmektedir. Bu gösterimde bileşenlerin yanlarında parantez içinde gösterilen sayılar ilgili bileşenin tedarik süresini gün cinsinden belirtmektedir. Renklendirilmiş hücreler ise o bileşenler için ayrıştırma noktası belirlendiği anlamına gelmektedir.

![](../_assets/aebdd04ecc30091cb1b0.png)

Bu örnekte hiçbir ayrıştırma noktasının olmadığı senaryoda; X-210-310-410 (ya da 420) dalındaki tedarik süresi toplamı en uzun olduğundan, X'in tedarik süresinin 45+4+2+1=52 gün olduğu bulunacaktır.

Eğer 410 ve 420 bileşenleri için Stok Planlama Kayıtları ekranındaki MRP politikası "Talebe Dayalı" olarak işaretlenirse, bu stokların ayrıştırma noktası olarak belirlendiği ve bu bileşenler için tampon stok tutulduğu anlaşılacaktır. Böyle bir durumda 410 ve 420 bileşenleri için elde tampon stok bulunduruluyor olduğundan, X mamulü için *ayrıştırılmış* *tedarik* *süresi* *(ATS)* hesaplanması gerekecektir. Bu süre hesaplanırken ayrıştırma noktaları ve varsa bu noktaların altında kalan BOM seviyeleri ihmal edilecektir. Yani 410 ve 420'nin ayrıştırma noktası olarak belirlendiği senaryoda X-210-310 dalındaki tedarik süresi, X mamulü için ayrıştırılmış tedarik süresi olacak ve 4+2+1=7 gün olarak hesaplanacaktır.

Benzer mantıkla X mamulünün diğer BOM dalından da ayrıştırılmış tedarik süresi hesaplanabilir. X-210-310 dalındaki tedarik süresi ayrıştırılarak 7 güne düştüğünden diğer dallara bakmak anlamlı olacaktır. Eğer diğer dallarda da hiç ayrıştırma noktası bulunmadığı varsayılırsa en uzun tedarik süresini içeren dal, X-220-320-430 yolu olacak ve bu yolda X mamulünün tedarik süresi 10+4+5+1=20 gün olarak hesaplanacaktır.

Aynı dalda 430 bileşeninin Stok Planlama Kayıtları ekranındaki MRP politikası "Talebe Dayalı" olarak işaretlenirse, bu noktada tampon stok tutulduğundan ayrıştırılmış tedarik süresi hesaplamasına dahil edilmeyecek ve X'in ayrıştırılmış tedarik süresi bu dalda 4+5+1=10 gün olacaktır. Ancak bu durumda da X-220-330 yolu yeni en uzun yol olacağından bu dalda tedarik süresi hesaplanacak ve 12+5+1=18 gün olarak bulunacaktır. Bu senaryoda 330 bileşeninin de ayrıştırma noktası olmasına karar verilirse yeni ayrıştırılmış tedarik süresi 5+1=6 gün olarak hesaplanacaktır.

Örnekten anlaşılacağı gibi bir BOM üzerinde ayrıştırma noktalarının olması ayrıştırılmış tedarik süresi hesaplanmasını gerektirmektedir ve ayrıştırma noktaları tepe mamullerin tedarik sürelerini düşürebilmeyi sağlamaktadır. Tepe mamulün ayrıştırılmış tedarik süresi ise her zaman en uzun tedarik süresi toplamına sahip BOM dalının ayrıştırılmış tedarik süreleri toplamına eşit olacaktır.

*Parametreler* ekranın detayları üzerinden anlaşılabilir ki, herhangi bir zamanda herhangi bir stok için parametreler ekranındaki dinamik analizlerden istenenler çalıştırılarak yeniden hesaplama yapılabilir. DDMRP'nin geleneksel MRP'ye göre esneklik yakaladığı noktalardan biri budur. Parametreler ekranında istenen seçimler yapıldıktan sonra ekranın sağ alt köşesindeki "Çalıştır" butonuna basmak ilgili analizlerin çalışmasını ve hesaplanan güncel verilerin Talebe Dayalı MRP Veri Yönetimi ekranının Stok Listesi sekmesinde görüntülenmesini sağlamaktadır.

Talebe Dayalı MRP Veri Yönetimi ekranının grid alanında bulunup *Parametreler* ara ekranında görülmeyen 2 adet bilgi vardır. Bunlar *Değişkenlik Faktörü* ve *Tedarik Süresi Faktörü'dür.* Bu verilerin kaynağı ve işlevi ile ilgili detaylı bilgi için Bölüm 3 incelenmelidir. Talebe Dayalı MRP Veri Yönetimi ekranında bulunan son buton ise "Talep Düzeltme Faktörü" butonudur.

![](../_assets/3ec185ddea841cfc9746.png)

Ekranın Stok Listesi sekmesinden talep düzeltme faktörü atanmak istenen stoklar seçildikten sonra ilgili butona tıklanıldığında, düzeltme faktörü girişinin yapılabileceği yeni bir ekran açılacaktır. (Bkz. Ekran Görüntüsü 13) DDMRP'nin malzeme yönetiminde esneklik sağladığı önemli noktalardan biri olan Talep Düzeltme Faktörü'nün kullanım amacı, talep değişkenliğinin önceden bilindiği belirli stoklar için, DDMRP tarafından hesaplanan OGT (ortalama günlük tüketim) verisini manipüle etmektir. İlgili ekran üzerinden atanacak talep düzeltme faktörleri, DDMRP tarafından hesaplanan OGT değeri ile çarpılacak ve böylece yeni bir OGT değeri hesaplanacaktır. OGT'nin manipüle edilmesini gerektirecek durumlara örnek olarak sezonsallık ya da kampanya dönemleri gibi, müşteri taleplerinin olağan seyrinden farklı bir trend yakaladığı senaryolar verilebilir.

![](../_assets/a2f3988872fa66f9cc83.png)

Talep Düzeltme Faktörü ekranında, DDMRP tarafından hesaplanan OGT ile çarpılacak düzeltme faktör değerleri hafta bazında girilebilir. Ekranın *Hafta/Yıl* alanına, hangi yılın hangi haftası için talep faktörü kullanılmak istendiği girilmeli ve *Düzeltme* *Faktörü* alanına da ilgili dönem için OGT ile çarpılacak faktör bilgisi girilmelidir. İstenilen sayıda hafta için bu bilgiler stok bazında girilebilmektedir.

Talep değişkenliğini böyle bir düzeltme faktörüyle yönetmenin avantajı ise hem OGT'ye stok bazında müdahale etmenin kolaylaşması hem de DDMRP'nin OGT hesaplamak için kullandığı parametreleri değiştirmeye gerek kalmadan, talep dalgalanması olacağının bilindiği belirli dönemlerin kolayca yönetilebilmesidir.

#### Tampon Profil Tanımları Ekranı

DDMRP desteği kapsamında desteklenen ekranlardan bir diğeri Üretim-MRP-Kayıt-Talebe Dayalı MRP yolu izlenerek ulaşılan Tampon Profil Tanımları ekranıdır. Bu ekranda DDMRP ile yönetilen stokların tedarik türü, değişkenlik ve tedarik süresi sınıfı ile minimum sipariş miktarı bilgilerine göre alacakları *Değişkenlik Faktörü* ve *Tedarik Süresi Faktörü* verileri yer almaktadır.

![](../_assets/a48eff34da375030d8aa.png)

Tampon Profil Tanımları ekranında yer alan değişkenlik ve tedarik süresi faktörü bilgileri DDMRP'nin en önemli noktalarından biri olan tampon seviyelerinin hesaplanmasında doğrudan kullanılmaktadır. Ekranın üst kısmında yer alan stok kriterlerine uygun faktör tanımlamaları, literatüre uygun olarak program tarafından varsayılan olarak atanmıştır ancak kullanıcılar tarafından bu alanların değiştirilmesine izin verilmektedir.

#### Tampon Seviyeleri Yönetimi Ekranı

DDMRP desteği kapsamında Üretim-MRP-Kayıt-Talebe Dayalı MRP yolu izlenerek ulaşılabilen "Tampon Seviyeleri Yönetimi" ekranı, DDMRP metodolojisinin en can alıcı noktası olan tampon seviyelerinin belirlenmesinde kullanılmaktadır.

Dokümanın bu bölümüne kadar anlatılan ekranlarda; hangi stokların DDMRP ile takip edilmek istendiğinin belirlenmesi, DDMRP ile yönetilecek materyallerin *ayrıştırma noktası* olarak atandığı ve bu noktalarda tampon stoklar tutulacağı anlatılmıştır. Ayrıca tampon stok seviyelerinin belirlenmesi için kritik olan ATS, OGT, düzeltme faktörleri ve stok sınıflandırmaları gibi önemli verilerin nasıl dinamik şekilde yönetilebildiği açıklanmıştır. *Tampon* *Seviyeleri* *Yönetimi* ekranında ise şimdiye kadar tanımlanan ve hesaplanan bu veriler kullanılarak, ayrıştırma noktalarında tutulacak tampon stok miktarlarının nasıl belirlendiği açıklanacaktır.

![](../_assets/8b2197a0630b6eafa9ba.png)

DDMRP metodolojisi her bir ayrıştırma noktasında tampon stokları 3 kademe olarak ele alıp hesaplama yapar ve bu kademeleri kırmızı, sarı ve yeşil renkle belirtir. Bir ayrıştırma noktasında tutulan tampon stok miktarı için kırmızı renkle belirtilen kısım en düşük seviyeyi, sarı ile belirtilen kısım ise kırmızı bölgenin bir üst seviyesini ve yeniden sipariş bölgesini temsil eder. Yeşil bölge ise sarı bölgenin üstünü ve güvenli stok seviyesini göstermektedir. Tampon stok seviyeleriyle ilgili tüm hesaplamalarda her bir stok için kırmızı, sarı ve yeşil bölgeler stok miktarıyla birlikte ilgili renklerle gösterilir. Böylece stok seviyeleriyle ilgili verilere bakıldığında görsel olarak da yönetim kolaylığı sağlanmaktadır.

Tampon Seviyeleri Yönetimi ekranı açıldığında yalnızca Stok Planlama Kayıtları ekranındaki MRP Politikası parametresi "Talebe Dayalı" olarak seçili stoklar, yani ayrıştırma noktası olarak belirlenmiş ve DDMRP ile yönetilen stoklar, listelenecektir. Listelenen stoklardan tampon stok seviyeleri hesaplanmak istenenler seçim kutucukları işaretlenerek seçili hale getirilmelidir ve ardından ekranın sağ üst köşesindeki "Hesapla" butonuna basılmalıdır. Tampon stok seviyelerinin hesaplanabilmesi için Talebe Dayalı MRP Veri Yönetimi ekranı kullanılarak gerekli parametreler hesaplanmış ve dolayısıyla stokların tampon profilleri belirlenmiş olmalıdır.

Tampon stoklar için kırmızı bölgeler; kırmızı baz ve kırmızı emniyet bölümleri olmak üzere 2 bölümden oluşmaktadır. Kırmızı bölgenin kendisi, bu 2 alt bölge hesaplamasının toplamıdır. Yeşil bölge içinse 2 değer hesaplaması yapılır ve bunlardan büyük olan yeşil bölge tampon seviyesini oluşturur. DDMRP stratejisiyle malzeme yönetimi yapılırken amaç stok seviyesini yeşil bölgede tutmaktır. Bunun için de tampon seviyesi stoklar bazında kontrol edilir ve seviye sarı ya da kırmızı bölgeye her düştüğünde DDMRP yeniden sipariş vermeyi önerir. Tampon seviyelerin bölgeler bazında hesaplaması Ekran Görüntüsü 16'da gösterilmiştir.

![](../_assets/b16357b4aecab063a0ca.png)

*Tampon* *Seviyeleri* *Yönetimi* ekranında kırmızı, sarı ve yeşil bölgeler için yazan stok miktarları, bölgelerin büyüklüklerini değil, her bir renge ait bölgenin en üst seviyesini gösterir. Yani tampon stok seviyeleri kümüle edilerek bir üst renk grubunun miktarı bulunmaktadır. Örneğin kırmızı bölge hesaplandıktan sonra *Tampon Seviyeleri Yönetimi* ekranının "Kırmızı Bölge" alanına yazılır. Ardından sarı bölge hesaplanır ve sarı bölge ile kırmızı bölge hesaplamalarından gelen toplam miktar "Sarı Bölge" alanına yazılır. "Yeşil Bölge" alanında yazan değer ise tüm bölgelerin hesaplamalarının toplamıdır.

*Tampon* *Seviyeleri* *Yönetimi* ekranında desteklenen bir diğer özellik de hesaplanan tampon seviyelerin detaylarının görüntülenebilmesidir. Bunun için detayları görüntülenmek istenen stok Tampon Seviyeleri Yönetimi ekranının grid alanından seçilmeli ve ardından ekranın üst bölümünde yer alan "Tampon Seviye Detayı" butonuna basılmalıdır. Bu işlem yapıldığında seçili stok için detayları gösteren yeni bir ekran görüntülenecektir.

![](../_assets/b1bb47ff74fc130fb848.png)

*Tampon* *Seviye* *Detayı* butonuna tıklandığında açılan ekranda görüntülenecek ilk bilgi "Güncel Tampon Seviyesi" detayıdır. Buradaki gösterim yine kırmızı bölgeden yeşile gidildikçe tampon miktarının kümüle edilmesiyle bulunan değerleri içermektedir.

Ekrandaki ikinci sekme olan "Tampon Seviyeleri Geçmişi" sekmesine geçildiğinde ise ilgili stok için geçmişte hesaplanan tampon seviyeleri zaman çizelgesi üzerinde görülebilecektir. Bu ekrandaki grafik üzerinde bulunan çubukların renkli bölgeleri yine tampon seviyelerini göstermektedir ve renklerin üzerine gelindiğinde ilgili renge karşılık gelen tampon stok miktarı görüntülenebilmektedir.

![](../_assets/77af2fd51ac784140a67.png)

Ekrandaki son sekme olan "Stok Seviyesi Performansı" sekmesine geçildiğinde ise zaman ekseni üzerinde DDMRP tarafından hesaplanan stok seviyelerini renklerle temsil ederek gösteren çubuk grafikler görüntülenmektedir.

![](../_assets/0b288e62f53502106b52.png)

Bu ekranda *Tampon* *Seviyeleri* *Geçmişi* ekranından farklı olarak çubuklar 5 bölümden oluşmaktadır. Bu bölümler yukarıdan aşağıya sırasıyla Kırmızı-Sarı-Yeşil-Sarı-Kırmızı şeklindedir. Ayrıca bu bölgeler yine yukarıdan aşağıya sırayla belirlenen tampon seviyelerindeki; sarı bölgenin yarısı, sarı bölgenin yarısı, yeşil bölgenin tamamı, kırmızı bölgenin yarısı ve kırmızı bölgenin yarısı şeklinde değer almaktadır. Ek olarak bu grafik üzerinde mavi noktalarla, tampon seviyelerinden farklı olarak ilgili stokun bakiyesi de gösterilir. Böylece DDMRP'nin önerdiği tampon stoklarla eldeki stok bakiyesi arasında nasıl bir ilişki olduğunun anlaşılmasına yardımcı olunur. Hatta bu ilişki zaman çizelgesi üzerinde görülebildiğinden trend hakkında yorum yapılabilmesine de olanak sağlanır.

#### Talebe Dayalı Planlama Ekranı

DDMRP desteği kapsamında kullanılan son ekran ise "Talebe Dayalı Planlama" ekranıdır. İlgili ekrana ulaşabilmek için Üretim-MRP-Kayıt-Talebe Dayalı MRP yolu izlenmelidir. *Talebe Dayalı Planlama* ekranı, DDMRP ile malzeme yönetiminin son basamağıdır. DDMRP ile planlanan malzemeler için çıkan ihtiyaçlar ve bu ihtiyaçlar doğrultusunda önerilen satın almalar bu ekranda gösterilmektedir.

![](../_assets/b36568c2746422532c1e.png)

*Talebe Dayalı Planlama* ekranında yalnızca DDMRP ile yönetilen stoklar listelenmekte ve bu stoklar için ekran ilk açıldığında, yapılan en son hesaplamalara ait veriler gösterilmektedir. DDMRP metodolojisinin son kritik ayağı olan "Net Akış" değeri de bu ekran üzerinden takip edilmektedir. DDMRP metodolojisinde elde bulunan stok miktarı, güncel stok bakiyesine eşit değildir. DDMRP, eldeki stok seviyesini *Net* *Akış* değeri olarak adlandırır ve tampon stok seviyeleriyle net akış değerini karşılaştırarak ihtiyaca karar verip sipariş önerisinde bulunur. Net akış değeri ise şu formülle hesaplanmaktadır; **Net** **Akış**=**Stok** **Bakiyesi** **Planlanan** **Tedarik** **Miktarı** - **(Geciken** **Talep** **Miktarı** **Ani** **Yükseliş** **Talep** **Miktarı).**

Talebe Dayalı Planlama ekranında belirli stoklar için *Net Akış* ve tampon seviyelerinin karşılaştırılması ve buna istinaden satın alma belgesi önerilerinin getirilebilmesi için, planlanması istenen stoklar grid ekran üzerindeki seçim kutucukları kullanılarak seçilmeli ve ardından ekranın üst bölümündeki "Hesapla" butonuna basılmalıdır. Bu işlem ekranda listelenen tüm stoklar için yapılmak isteniyorsa seçim için ekranın üst bölümündeki "Tümünü Seç" butonu kullanılabilir.

Talebe Dayalı Planlama ekranında hesaplanan *Ani Yükseliş Talep Miktarı,* planlama ekranında yapılan son hesaplama tarihinden sonra, *Ani* *Yükseliş* *Ufku* boyunca *Ani* *Yükseliş* *Eşiği'*ni geçen ihtiyaç miktarlarının toplamıdır. Bu değer hesaplanırken kullanılan *Ani* *Yükseliş* *Ufku* değeri ise MRP Parametreleri ekranının Genel-2 sekmesine eklenen *Ani Yükseliş Ufku Katsayısı* ile ATS'nin çarpım değerine *Ani* *Yükseliş* *Ufku* *Sabit* *Değeri'*nin eklenmesiyle bulunmaktadır. *Ani* *Yükseliş* *Eşiği* hesaplanırkense *Ani* *Yükseliş* *Eşiği* *Katsayısı* ile emniyet seviyesi çarpılmaktadır. Ani yükseliş ufku ve ani yükseliş eşiği kavramları DDMRP'ye özel kavramlar olup DDMRP'de malzeme ihtiyaç planlaması yaparken klasik MRP'den ayrılan önemli bir noktadır. DDMRP metodolojisinde ihtiyaç çıkarılırken gelecekteki tüm siparişler dikkate alınmamaktadır. Bunun yerine ani yükseliş ufku kadar uzaklıktaki müşteri siparişleri dikkate alınmakta ve bu ufukta da ani yükseliş eşiğini aşan talepler kritik kabul edilerek dikkate alınmaktadır.

Talebe Dayalı Planlama ekranında karşılaşılan bazı başka kavramlar da bulunmaktadır. Bunlardan *Planlanan* *Tedarik* *Miktarı,* satın alma siparişleri ve satın alma taleplerini içeren bir veridir. Bu veri ATS kadarlık bir gelecek periyodu için hesaplanmaktadır. *Geciken Talep Miktarı* verisi ise Talebe Dayalı Planlama ekranında yapılan son hesaplama tarihinden itibaren gecikmeye düşmüş müşteri siparişlerini göstermektedir. Ekrandaki *Planlama Önceliği* verisi ise net akış değeri ile maksimum stok seviyesi değerinin oranlanmasıyla hesaplanmaktadır. Burada hesaplanan yüzdelik değer küçüldükçe o stok için satın alma yapılması gerektiği ve hatta yapılacak satın almanın kritik seviyeye geldiği anlaşılmaktadır.

Talebe Dayalı Planlama ekranının grid alanında yer alan Planlanan Tedarik Miktarı, Geciken Talep Miktarı ve Ani Yükseliş Talep Miktarı verileri için hesaplanmış bir değer olduğunda, değer üzerine tıklayarak ilgili sonuca hangi veriler / belgeler kullanılarak ulaşıldığına dair detay ekranlara ulaşılabilmektedir.

![](../_assets/90093d4bb8cc40659811.png)

Bu bilgilere ek olarak, Talebe Dayalı Planlama ekranında listelenen stoklardan biri seçilip ekranın üst kısmındaki "Hesaplama Geçmişi" butonuna tıklanabilmektedir. Bu işlem yapıldığında ilgili stoka ait hesaplama geçmişi detaylarıyla ve tarih bilgisiyle birlikte izlenebilecektir.

![](../_assets/04ead7e60538bc616079.png)

Talebe Dayalı Planlama ekranının son fonksiyonu ise listelenen stoklar için önerilen belgelerin açılabilmesidir. Bunun için, ekranın grid alanından önerilen belgeleri açılmak istenen stoklar seçilmeli ve ardından ekranın sağ üst köşesindeki "Belgeleri Aç" butonuna tıklanmalıdır. Bu işlem yalnızca "Önerilen Belge Miktarı" bilgisi sıfırdan büyük stoklar için gerçekleştirilecektir. Burada vurgulanması gereken detay şudur ki; DDMRP, net akış değeri yeşil bölgenin altına düşen stoklar için belge açma önerisinde bulunmaktadır ve önerilen belge miktarı her stok için kendi yeşil seviyesinin en üst noktasına ulaşacak kadar olacaktır. Örneğin Ekran Görüntüsü 20'de grid alandaki ilk stok için net akış değeri 210 olarak hesaplanmış ve maksimum stok seviyesi (kümülasyon yöntemiyle yeşil bölgenin üst sınırına kadar yapılan hesaplama) 288,82 olduğundan DDMRP tarafında 78,82 adetlik bir öneride bulunulmuştur.

*Belgeleri Aç* butonuna tıklandıktan sonra MRP Parametreleri ekranı Genel-1 sekmesindeki "MRP için satıcı siparişi yerine satın alma talebi oluşturulsun" parametresi kontrol edilir ve bu parametredeki seçime göre Satıcı Siparişi ya da Satın Alma Talebi belgeleri oluşturulmak üzere bir ara ekran görüntülenir.

![](../_assets/113b30c52a1677eb8316.png)

İlgili ekranın ilk alanı "Başlangıç Sipariş Numarası" sahasıdır. Bu sahaya DDMRP tarafından önerilen belgelerin hangi numaradan başlanarak sırayla açılması istendiği girilmelidir. Ardından açılacak belgelerin tarih bilgileri "Sipariş Kayıt Tarihi" alanına ve belgelerin satıcı bilgileri de "Satıcı Kodu" alanına girilmelidir. Açılacak her bir belge için "Satıcı Kodu" atanırken öncelikle "Müşteri-Satıcı Stok Kayıtları" ekranı kontrol edilecektir. Eğer stok özelinde Müşteri-Satıcı Stok Kayıtları ekranında cari eşleşmeleri varsa ilgili belgeler, ilgili carilere ekrandaki sipariş oranına göre açılacaktır. Eşleşme olmaması halinde *Satıcı* *Siparişi* *Parametreleri* ekranına girilen Satıcı Kodu bilgisi kullanılacaktır. Ekrandaki "Stok Depo Kullan" parametresi ise açılacak belgelerin Giriş Depo Kodu bilgisinin stok kartından getirilmesi istendiğinde kullanılmalıdır. Açılacak belgelere girilmesi istenen depo kodu bilgisi ise "Mal Kabul Depo Kodu" alanına girilmelidir.

*Satıcı Siparişi Parametreleri* ekranında gerekli bilgiler doldurulup "Tamam" butonuna tıklandığında kullanıcı tarafında seçilen ve DDMRP'nin satın alma önerisi getirdiği stoklar için belgeler açılacaktır. Belgesi açılan stoklar için Talebe Dayalı Planlama ekranının "Belge Oluşturuldu" sütunu "Evet" olarak güncellenecektir. Belgesi oluşturulduğuna dair bilgisi "Evet" olan stoklar için, Talebe Dayalı Planlama ekranı üzerinden yeni bir hesaplama yapılmadığı sürece yeniden belge oluşturulmasına izin verilmeyecektir.
