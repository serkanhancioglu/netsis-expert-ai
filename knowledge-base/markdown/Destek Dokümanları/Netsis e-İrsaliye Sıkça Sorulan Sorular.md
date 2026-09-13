---
title: "Netsis e-İrsaliye Sıkça Sorulan Sorular"
page_id: "50686939"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis e-İrsaliye Sıkça Sorulan Sorular"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis e-İrsaliye Sıkça Sorulan Sorular"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWE2Mjg0YWExLThiYzctNDdiYy05MjMzLTg0NWY5NzBlMGUzZiZsaW5rPTFlOGNiMjU0LWU2NjAtNGM0Ni1iOWY2LWE1NmE5Yjg0Y2FmMCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=a6284aa1-8bc7-47bc-9233-845f970e0e3f&link=1e8cb254-e660-4c46-b9f6-a56a9b84caf0&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-e-irsaliye-sikca-sorulan-sorular_80090615_50686939.html"
source_version: "2022-12-09T15:36:55.560+03:00"
source_bytes: 29540
fetched_at: "2026-09-13T04:25:20+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis e-İrsaliye Sıkça Sorulan Sorular

**Online e-İrsaliye için test süreçleri nasıl olmalıdır?**

Detaylı bilgi için [tıklayınız.](<Netsis e-İrsaliye Entegrasyon Test Süreçleri.md>)

**e-Fatura ve e-İrsaliye uygulaması için aynı yöntem mi kullanılmalıdır?**

GİB tarafında e-Fatura ve e-İrsaliye uygulaması için kullanılan yöntemlerin aynı olma zorunluluğu yoktur. 9.0.29 seti ile birlikte Logo Netsis' te e-Fatura ve e-İrsaliye uygulaması için kullanılan yöntemlerin aynı olma zorunluluğu kalkmıştır.

Netsis içerisinde e-Fatura ve e-İrsaliye uygulaması aynı sertifika tanımını kullanmaktadır. Bu sebeple e-Fatura ve e-İrsaliye uygulamasında farklı yöntem kullanımı söz konusu ise, aynı makine için entegratör yöntemi kullanımında da mühürlü sertifika tanımı kullanılmalıdır. Ayrıca Netsis'in entegre çalıştığı logo dışındaki diğer özel enetgratörler (akbank,e-finans, veriban, isis) içinde e-İrsaliye uygulaması için çalışma yapılmaktadır.

**e-İrsaliye ve e-Fatura uygulaması için her ikisinde aynı entegratör mü** **kullanılmalıdır?**

e-İrsaliye uygulamasında Netsis'in entegre çalıştığı logo dışındaki diğer özel entegratörler (Akbank, e-Finans, veriban, isis, vb.) şu an için desteklenmemektedir.

**e-İrsaliye** **mükellefi** **olmayan** **firmaya e-İrsaliye** **belgesi** **(sanal** **irsaliye)** **nasıl** **kesilir?**

Netsis içerisinde firma için açılmış cari hesaba e-İrsaliye serisinden satış irsaliyesi kesilip, toplu e-İrsaliye Oluşturma işlemi ile taslak oluşturulup gönderme işlemi yapılır. Entegratör kullanımında, entegratöre gönderilen e-İrsaliye carisine ait alias bilgisi boş gider. Gib sanal irsaliye hesabına ait VKN, alias bilgisi entegratör tarafından doldurularak irsaliye zarfı GİB' e iletilir. Online e-İrsaliye kullanımında ise, taslak oluşturulup gönderim aşamasında programın arka planında GİB' in sanal irsaliye hesabına ait VKN ve alias bilgisi doldurularak irsaliye zarfı GİB'e iletilir.

**Müşteriye e-İrsaliye kesiliyor. Ancak sevkiyat daha yola çıkmamışken, herhangi** **bir** **hatalı** **durumdan** **dolayı** **e-İrsaliye** **iptal** **edilmek** **istendiğinde** **ne** **yapılmalıdır?**

e-İrsaliyede iptal işlemi yoktur. Sevkiyat yola çıkmamışsa, müşteri e-İrsaliye mükellefi değilse, e-İrsaliye sadece GİB' in sanal irsaliye kullanıcı hesabına gider. Netsis içerisinden sevk edilen malların depolara geri alınması ve işlenmesi gerekmektedir. Bu durumda karşı tarafın herhangi bir şey yapmasına gerek yoktur. İster manuel, ister alış irsaliyesi, depolar arası transfer fişi veya ambar giriş fişi ile stoklara giriş yapılmalıdır. Sevkiyat yola çıkmamışsa, müşteri e-İrsaliye mükellefi ise, e-İrsaliye müşteri hesabına ulaşır. Bu durumda karşı tarafın herhangi bir şey yapmasına gerek yoktur çünkü kendisine gelen bir mal yoktur. Netsis içerisinden sevk edilen malların depolara geri alınması ve işlenmesi gerekmektedir. İster manuel, ister alış irsaliyesi, depolar arası transfer fişi veya ambar giriş fişi ile stoklara giriş yapılmalıdır.

**Müşteriye e-İrsaliye kesiliyor. Ürünler araca yüklenip yola çıkıyor. Ancak adresin** **yanlış** **çıkması,** **adreste** **müşterinin** **olmaması,** **firmadaki** **muhasebeci/yetkili** **kişinin** **o** **esnada olmaması, yolda müşteri ürünleri almaktan vazgeçmesi, bir sebeple karşı taraf** **malı almak istememesi veya irsaliyenin hatalı oluşarak gönderilmesi, vb. durumlarda e-İrsaliye iptal** **edilmek** **istendiğinde ne** **yapılmalıdır?**

Eğer müşteri e-İrsaliye mükellefi ise, mallar karşı tarafa ulaştıktan sonra, karşı taraf öncelike kabul etmeyeceği mallar için isteğe bağlı olarak irsaliye yanıtı verebilir. (red/kısmi red bilgi amaçlı olarak). Sonrasında malları sanki kabul ediyormuş gibi depolarına işlemeli ve akabinde geri göndereceği kısım için tekrar satış irsaliyesi keserek malı gönderen tarafa e-İrsaliye olarak göndermelidir. Sonrasında malı gönderen firmanın gelen kutusuna ilgili e- İrsaliye düşer ve bu gelen e İrsaliyeye karşılık alış irsaliyesi oluşturulur. Eğer müşteri e-İrsaliye mükellefi değil ise, mallar karşı tarafa ulaştıktan sonra malları sanki kabul ediyormuş gibi depolarına işlemeli ve akabinde geri göndereceği kısım için tekrar matbu satış irsaliyesi keserek malı gönderen tarafa iletmelidir. Sonrasında malı gönderen firma kendisine gelen matbu irsaliyeyi manuel olarak sistemine işlemelidir. Eğer müşteri, kendisine gelen malların tamamını istemezse ve kendisi irsaliye kesmek istemezse, bu durumda malı gönderen taraf kendi kendine e-İrsaliye keserek kamyonun geri dönmesini sağlar. Kendi kendine kestiği bu e-İrsaliyesini kendi sistemine işler. Sonrasında netsis içinde ambar giriş fişi, sarf fişi veya manuel olarak ilk çıkışa karşılık giriş kaydı atarak bakiyenin dengelenmesi sağlanır.

**GİB'** **in** **sisteminde** **sorun** **olması** **durumunda,** **kuyrukta** **bekleyen** **belgelerin** **olması** **durumunda** **veya** **internetin** **olmadığı** **durumda** **nasıl** **e-İrsaliye** **gönderilir?**

Aslında matbu irsaliye ile e-İrsaliye aynı anda kesilmelidir. Her iki belge üzerinde birbirlerinin bilgisini içeren açıklamalar olmalıdır. Matbu irsaliye girişi sırasında e-İrsaliye kesilemese bile e-İrsaliye numarası netsiste ayrılıp ilgili numara matbu üzerine girilmelidir. (matbu irsaliye üzerine, "OMR…1 nolu e-İrsaliyeye istinaden oluşturulmuş matbu irsaliyedir" ibaresi olmalıdır.) Sonrasında e-İrsaliye için ayrılan numaraya irsaliye girildiğinde matbu numarası da e-İrsaliye üzerine girilmelidir.

("ABC…1 matbu irsaliyeye istinaden oluşturulmuş e-İrsaliyedir" ibaresi olmalıdır.) 9.0.30 seti ile birlikte, e-İrsaliye'de "Matbudan" senaryosu desteklenmiştir. "İrsaliye Ek Bilgi Girişi" ekranına "Matbu Bilgileri" seçeneği eklenmiştir. "Matbudan" tipli e-İrsaliye oluşturulması için ilgili seçeneğin işaretlenip, gerekli bilgilerin doldurulması gerekmektedir.

**e-İrsaliye** **geçişinden** **sonra,** **geçişten** **sonraki** **1** **ay** **için** **basılı** **irsaliye** **kesilebilir** **mi** **ya** **da** **ne** **zaman** **matbu** **irsaliye** **kesebilirim?**

Geçiş sonrası 1 ay içinde matbu irsaliye kesilebilir. 509 nolu tebliğ v7 maddesine göre GİB sistemi çalışmadığı durumda (GİB' e e-İrsaliye gönderilip alınamıyorsa, kuyrukta bekleyen e-İrsaliyeler varsa, vb..) kullanılabilir denmektedir. Bu durum temmuza kadar olan geçişler için geçerliydi temmuzdan sonra bu durum yok.

**Sevkiyat** **için** **kamyon** **ne** **zaman** **yola** **çıkmalıdır?**

Sevkiyat için kamyon e-İrsaliye gönderildikten sonra, irsaliye zarfının durumu 1200 olduğu anda yola çıkabilir. 1200' lü durum kodlarının alınması demek e-İrsaliyenin GİB portalına ulaştığı anlamına gelir. 1200 lü durum kodları için alınan hatalar zaten alıcı kaynaklı hatalardır.

Entegratör kullanımı durumunda sevkiyat için kamyon, e-İrsaliye gönderilip entegratöre ulaştığı andan itibaren yola çıkabilir. Entegratör yöntem kullanımında 1200' lü durum kodlarını beklemeye gerek yoktur.

**Gönderilen** **e-İrsaliyenin** **1300'** **e** **ulaşmama** **durumunda** **ne** **yapılmalıdır?**

e-İrsaliye zarfının hata alması durumunda, hatalı zarf silinerek hata düzeltildikten sonra tekrar gönderilmelidir. Hatalı durum kodları dışında 1200 lü kodların alınması durumunda sevkiyat çıkarılmalı sonrasında ise, ettn değiştirilmeden "zarf tekrar gönder" işlemi yapılmalıdır. Ancak şu an konu ile ilgili maddemiz mevcuttur.

**Ticari İrsaliye senaryosu var mıdır? İrsaliye tipi SEVK ve MATBU dışında başka irsaliye tipi var mıdır?**

Uygulama yanıtı sadece bilgilendirme amaçlı gönderildiği için tek tip senaryo var o da temel İrsaliye senaryosudur. GİB tarafında Iade, taşıma, konsinye, vb tipte irsaliye tipleri yoktur. Sadece SEVk ve MATBU irsaliye tipleri vardır.

**Kime,** **neyi,** **ne** **kadar** **verileceği** **bilinmediği** **durumlarda** **nasıl** **e-İrsaliye** **kesilmelidir?**

Muhtelif müşteri tipinde e-İrsaliye düzenlenmelidir. Netsis içerisinde ise, depolar arası transfer kaydı girilmeli ve cari olarak muhtelif cari (VKN:555555555 cari isim: MUHTELİF MÜŞTERİLER) seçilmelidir. Malların kamyona yüklenebilmesi için, kamyon için kamyon deposu açılmalıdır. Mallar kamyon deposuna DAT kaydı ile alınmalı ve kamyon yola çıkmalıdır. Satış gerçekleştikte gerçek carilere e-İrsaliye, efatura, earşiv veya irsaliyeli fatura kesilmelidir.

**Yarım** **mamul,** **mamul** **malların** **bazı** **işlemler** **yapılmak** **üzere** **farklı** **lokasyona** **gönderilmesinde** **e-İrsaliye** **kesilmeli** **midir?**

Örneğin İzmir' de tekstil sektöründe faaliyet gösteren bir firma olup kıyafet dikimi yapılıyor. Dikim sonrası bu kıyafetler Karşıyaka' dan Alsancak' a boyaya gidiyor. Kıyafetlerin satışı gibi bir durum yok, boyayı yapacak yere fatura kesme durumu yok. Bu durumda e-İrsaliye kesilmelidir. Faturanın genel notlar kısmına "fatura edilmeyecektir", "fason işçilik kapsamında", "boyama kapsamında", taşıma amaçlı düzenlenmiştir", vb. notlar yazılabilir.

**Satışa** **konu** **olmayan,** **tamir,** **bakım** **amaçlı** **gönderilen** **malzemelerin,** **ekipman,** **demirbaş sevkiyatlarında taşıyan-taşıtan her kimse sevk sırasında e-İrsaliye kesmeli** **midir?**

Örneğin bozulan şirket telefonlarını Apple firmasına tamire götürürken, İstanbul ofisten İzmir ofise monitörleri gönderirken, sevk aşamasında e-İrsaliye (ister irsaliye kaydı, ister dat kaydı) kesilmelidir.

**Soru** **15:** **"Sevk** **irsaliyesi** **yerine** **geçer"** **ibareli** **belgelerin** **düzenlendiği** **durumlar** **nelerdir?**

GİB, eğer firma e-İrsaliye mükellefi ise, satışın yapıldığı anda ürün teslimatı yapılıyorsa ve kesilen faturanın (e- fatura veya e-Arşiv) üzerinde "irsaliye yerine geçer" ibaresi varsa ve düzenleme saat bilgisi (düzenleme tarihi değil) varsa tekrardan e-İrsaliye kesmeye gerek yoktur. Bu faturanın çıktısı üzerine kaşe ve imza atılarak irsaliye düzenlemeden alıcıya malı taşıtabilir veya ürünler alıcıya teslim edilebilir.

Sıcak satış sırasında kamyon içinde veya satış esnasında fatura kesilip çıktı alınma durumu varsa, fatura üzerinde "irsaliye yerine geçer" ibaresi varsa ve düzenleme saat bilgisi varsa e-İrsaliye kesilmeye gerek yok. Örnek olarak Trendyol'dan yapılan alışveriş sonrası kesilen faturalar gibi, English home' dan havlu alındığında kesilen faturalar gibi.

**İrsaliye** **yanıtı** **oluşturulmadan** **mallar** **iade** **edilebilir** **mi?**

İrsaliyeye uygulama yanıtı verilmesi zorunlu değildir. İrsaliye yanıtı verilmeden iade edilecek miktar kadar e-İrsaliye kesilip gönderilmelidir.

**Kabul** **edilmeyen** **malların** **faturalandırılması** **nasıl** **olmalıdır?**

A firması B firmasına 50 kg elma gönderdi. B firması 30 kg sunu kabul edip 20 kg sunu reddetti. Kabul etmediği miktar kadar tekrar irsaliye düzenleyerek A firmasına geri gönderdi. A firması da B den gelen irsaliyeyi kendi sistemine işledi.

Bu örnekte faturalandırma durumu firmaların işleyişlerine göre değişebilir. A firması 50 kg gönderilen elma için satış faturası keser. 20 kg elma iadesi için B firmasından iade faturası isteyebilir. B firması 20 kg elma iadesi için kendi irsaliyesini gönderir ve A firması kendi sistemine işler. A firması sadece 30 kg elma için satış faturası kesebilir. E-belgelerin saklanma özelliğinden dolayı, ilerde olacak denetimde irsaliye ile fatura arasındaki miktarsal fark e- belgelerle kanıtlanabileceğinden irsaliye ile fatura miktarlarının aynı olmasına gerek yoktur. Kabul edilmeyen mallar için kesilen irsaliyeler sevk amaçlı kesildiği için faturalandırılmaya gerek yoktur.

**Şubelerarası transfer fişinde 300 adet kalem olup tek kağıda sığmama** **durumunda,** **her** **kağıtta** **ayrı** **bir** **e-İrsaliye** **numarası** **ve** **karekod** **olmalı** **mıdır?**

300 adet kalem için tek bir belge numarası, tek bir barkod ve tek bir çıkış olmalıdır.

**Fatura** **üzerinde** **"İrsaliye** **yerine** **geçer"** **ibareli** **ve** **düzenleme** **saati** **olan** **faturalarda** **barkod,** **karekod** **zorunlu** **mudur?**

Zorunlu değildir.

**Fatura** **kesilen** **ürünler** **için** **irsaliye** **ayrıca** **kesilmeli** **midir?**

Mallar bugün faturanın çıktısıyla teslim edildiyse ve fatura üzerinde "irsaliye yerine geçer" ibaresi ve düzenleme saati varsa e-İrsaliyeye gerek yoktur. Mal sevkiyatı fatura kesilmeden önce veya sonra olursa e-İrsaliye kesilmelidir.

**Müşteriye** **kesilen** **e-İrsaliyeler** **müşterinin** **mailine** **düşer** **mi?**

eLogo üzerinde e-İrsaliye mailing hizmeti vardır. Netsis içerisinden müşteriye ait mail bilgisi Customer.ElectronicMail tag iyle gönderildikten sonra eLogo tarafından mail gönderilmektedir.

**Örneğin,** **firma** **dökme** **ürünü** **olan** **1000kg** **X** **ürününü** **e-İrsaliye** **ile** **gönderdi.** **Ürünü** **alan** **müşteride** **yapılan** **kantar** **ölçümünde** **1000 kg** **olarak** **gelen** **ürün** **950 kg** **olarak** **tartıldı.** **Bu** **durumda** **müşterinin** **kantarı** **kabul** **ediliyor** **ve** **müşteri** **kendi** **sistemine 950kg ürün geldi diyerek işliyor. Bu durumda geriye bir mal sevki olmayacağı** **için** **ne yapılmalıdır?**

Malı gönderen taraf 1000 kg için e-İrsaliye oluşturup gönderdi. Müşteri gelen ürünü tartıp 950 kg geldiğini ve irsaliye yanıtını bilgi amaçlı olarak karşı tarafa 950 kg sunu kısmi kabul ettiğini göndermelidir. Müşteri önce 1000

kg'lık ürünü stoklarına işlemelidir. Sonrasında mal sevki olmasa bile 50 kg'lık kayıp için kendi irsaliyesini kesip göndermelidir. Ürünü satan kişi bu e-İrsaliyeyi alıp sistemine işlemelidir.

**İrsaliye** **düzenleme** **tarihinden** **önceki** **bir** **zaman** **için** **sevk** **tarihi** **girilebilir** **mi?**

05.06.2020 de irsaliye oluştu. İrsaliyenin sevk tarihine 04.06.2020 girilemez. Geçmişe yönelik sevk tarihi girilemez. İleriye yönelik sevk tarihi belirtilebilir. Yanlışlıkla girilme durumunda e-İrsaliye gönderildiğinde "Sevk tarihi irsaliye tarihinden küçük olamaz." uyarı mesajı entegratör tarafından gelmektedir.

**05.06.2020'de 10 adet telefon satıldı. Faturası ve irsaliyesi bugün kesildi.** **Faturası bugün e-fatura olarak gönderildi ama telefonlar 3 gün sonra geleceği için** **sevkiyat 3** **gün** **sonra** **yapılacak.** **Bu** **noktada** **işleyiş** **nasıl** **olmalıdır?**

e-İrsaliye oluşturma sırasında düzenlenme tarihi 05.06.2020 olmalı ama sevk tarihi olarak 08.06.2020 yazılarak kaydedilmelidir. Sonrasında irsaliye bu şekilde faturalaştırılmalıdır.

Netsis içerisinde 05.06.2020 tarihinde satış irsaliyesi oluşturulur. Satış irsaliyesi girişi sırasında "e-İrsaliye Bilgi Girişi" ekranında sevk tarihi olarak 08.06.2020 tarihi girilir. e-İrsaliye faturaya dönüştürülüp e-Fatura olarak gönderilir. Sonrasında Toplu e-İrsaliye Oluşturma ekranından "Faturalandırılmış İrsaliyeler Getirilsin" parametresi işaretlenerek taslak oluşturularak e-İrsaliye gönderilir.

**Kamyona** **1000** **adet** **ürün** **yüklendi.** **Sırayla** **firmalara** **dağıtımları** **yaptı** **kamyonda** **200** **adetlik** **ürün** **kaldı. Bu** **200** **adetlik** **ürünle** **geri** **gelmesi** **durumunda** **ne** **yapılmalıdır?**

Depolar arası transfer kaydı ile kamyon deposundan ürünlerin kendi deposuna taşınması sağlanır. Bu belge de cari olarak firma kendisi için açılan cariyi seçebilir.

**Mal** **ihracatında** **da** **e-İrsaliye** **oluşturulmalı** **mıdır?**

Hollanda'daki bir müşteriye bir ihracat işlemi yapılıyorsa (Hollanda'daki müşteri e-İrsaliye mükellefi değil) e- İrsaliye kesilip GİB' in sanal irsaliye kullanıcı hesabına gönderilecek. Çıktısı alınıp sevkiyat için kamyona verilecek. Gümrüğe veya serbest bölgeye gidecek. Bir süre sonra gümrüğe gidecek e-İrsaliyeler Gümrük tarafında açılacak hesaba gidecek.

**A** **firması** **B firmasına** **10** **kg** **elma** **gönderdi. B** **firması** **2** **kg**'**sini** **çürük** **olduğu** **için geri göndermek istedi. B firması, A firmasının kamyonu geri dönmeden 2 kg'lik** **elma** **için** **kestiği** **irsaliyede taşıyıcı** **bilgileri** **kısmında ne** **yazmalıdır?**

A firmasına ait bilgileri girmelidir.

**Ürünlerin kargo firması tarafından taşındığı durumda e-İrsaliye girişinde şoför** **ve** **plaka** **bilgisi** **girişi** **zorunlu** **mudur?**

9.0.29 setiyle beraber bu zorunluluk kaldırılmıştır. Taşıyıcı bilgilerinin girilmesi yeterlidir.

**e-İrsaliye Belgesi olarak Ambar Çıkış Fişi belgesi kullanımda e-İrsaliye** **kutucuğunun** **aktif gelmesi** **koşulu** **nedir?**

Belge üzerinde çıkış yeri: Serbest Masraf Kod alanında cari kod seçilmesi durumunda "e-İrsaliye" kutucuğu işaretli gelir.

**e-İrsaliye** **oluşacak** **hal** **senaryosunda** **satış** **irsaliyesinde** **girilen** **künye** **bilgisi** **e-faturaya** **taşınabilir mi?**

9.0.29 setiyle birlikte künye bilgisi faturaya taşınmıştır.

**Fiyatsız** **gönderilen** **e-İrsaliye** **belgesi** **fiyatlandırılarak** **faturalandırılarak** **gönderilmek** **isteniyor.** **Bu işlem** **nasıl yapılır?**

Fiyatlar sonradan belli oluyorsa, fiyatsız oluşturulan satış irsaliye belgesi e-İrsaliye oluşturulup gönderildikten sonra tekrar satış irsaliyesi içerisine girilip toplamlar sekmesindeki "Fat" butonu yardımıyla faturası oluşturulur. Fiyatlar fatura içinde girilir. Fiyatlar önceden belli ama irsaliye fiyatsız gidecekse, satış irsaliye belgesi içerisinde ürünlerin fiyatları girilip kaydedilir. Toplu e-İrsaliye oluşturma ekranında "fiyatlar basılsın" parametresi işaretlenmeden taslak oluşursa ürünler fiyatsız oluşur.

**A** **firması** **elektrik** **ürünleri** **satıyor** **ve** **malı** **deposunda** **tutuyor** **yani** **B firması** **A** **firmasından** **mal** **aldığında** **mallar** **A** **firmasının** **deposunda** **kalıyor** **sevk** **işlemi** **C** **firmasına** **A** **firmasının** **deposundan** **yapılıyor** **ama** **A** **firmasının** **irsaliyesi** **ile** **değil** **B** **firmasının** **irsaliyesi** **ile** **sevki** **isteniyor.** **Bu** **durumda** **A** **firması** **ne** **yapmalıdır?**

A B' ye çıkacak malları ama sevk adresi olarak C firmasını beyan edecek. Yani irsaliye B ye gidecek mallar C ye.
