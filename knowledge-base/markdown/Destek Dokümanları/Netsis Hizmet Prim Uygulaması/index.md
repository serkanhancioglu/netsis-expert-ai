---
title: "Netsis Hizmet Prim Uygulaması"
page_id: "66237115"
product: "netsis-3-enterprise"
depth: 2
is_section: true
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis Hizmet Prim Uygulaması"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis Hizmet Prim Uygulaması"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTgyNDk1MDI2LWE1ZWMtNDY1MS05YjBlLWM1YWU5Y2I5OTllMiZsaW5rPThiOTZmYWZlLTNiODYtNDZjOS04ODgwLTFjM2E2N2IzZGQ5NyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=82495026-a5ec-4651-9b0e-c5ae9cb999e2&link=8b96fafe-3b86-46c9-8880-1c3a67b3dd97&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-hizmet-prim-uygulamasi_80088981_66237115.html"
source_version: "2022-11-02T15:38:06.680+03:00"
source_bytes: 1939449
fetched_at: "2026-09-13T04:24:42+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis Hizmet Prim Uygulaması

Netsis Hizmet Prim Uygulaması ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

> [!TIP]
> İlgili özelliğin anlatımını içeren webinar kaydına ulaşmak için [tıklayınız.](https://register.gotowebinar.com/recording/3505738259995921671)

Günümüz çalışma şekillerine bakıldığında prim bazlı sözleşmelerin hemen her sektörde karşımıza çıktığını görüyoruz. Prim alan ya da veren tarafta olmak fark etmeksizin, prim sistemiyle çalışmakta olan herkes sözleşmelerinin takibini detaylı şekilde yapma ihtiyacı duymaktadır. Satın almalar ya da satışlar karşılığı hesaplanması gereken primlerin; alış/satış miktarlarına, fatura tutarlarına, prim sözleşme tarihlerine bağlı birçok detayı bulunabilmektedir.

Bu noktada Logo Netsis Hizmet Prim Uygulaması, bir prim sözleşmesinin içerebileceği tüm detayları kaydedebilme imkânı sunarak kullanıcılarının alış ve satış faturaları üzerinden primlerini hesaplayabilmesini sağlamaktadır. Oransal ya da tutarsal primlerle çalışma desteği sağladığı gibi sabit prim sistemleri için de kullanım olanağı sunan Logo Netsis Hizmet Prim Uygulaması, Logo Netsis 3 Standard, Logo Netsis 3 Enterprise, Logo Netsis Wings ve Logo Netsis Wings Enterprise çözümleriyle birlikte kullanılabilmektedir.

Bu dokümanda Hizmet Prim Uygulaması kapsamındaki ekranların detayları anlatılmaktadır. Burada anlatılan detaylara ilişkin örneklerin incelenebilmesi için "Hizmet Prim Uygulaması Örnek Uyarlama Dokümanı"ndan da yararlanılması önerilmektedir.

#### Hizmet Prim Tanımlama

Hizmet prim uygulamasının kullanılabilmesi için gerekli ilk tanımların yapılabileceği "Hizmet Prim Tanımlama" ekranına Finans-Cari-Kayıt-Hizmet Bilgileri Girişi yolu izlenerek ulaşılabilmektedir.

![](../../_assets/3e66be6a408db2b56da4.png)

Takip edilmek istenen primlerle ilgili tanımların yapıldığı hizmet prim tanımlama ekranı 2 sekmeden oluşmaktadır. İlk sekme olan "Prim Tanım Bilgileri" sekmesindeki ilk alan "Hizmet Prim Kodu" alanıdır. Bu alana takibi yapılacak prim için serbest şekilde alfa-numerik bir kod girişi yapılmalıdır. Ardından isteğe bağlı olarak ilgili hizmet prim koduna ait bir açıklama bilgisi "Açıklama" alanına girilebilmektedir. Sekmedeki üçüncü alan olan "Grup Kodu" alanı ise tanımlanan hizmet primlerinin gruplar halinde raporlanmak istendiği durumlarda kullanılan opsiyonel bir alandır. Sekmedeki "Cari Seçimi" alanı, birden çok seçeneği barındırmakta ve tanımlanmakta olan hizmet prim kodunun hangi cariler için geçerli olacağını belirtmekte kullanılmaktadır. Her bir hizmet prim kodu gerçek hayatta yapılmış bir hizmet prim sözleşmesiyle eşlenik olarak düşünülebilir. Bu anlamda yapılan prim sözleşmesine dahil olan carilerin "Cari Seçimi" alanı kullanılarak kaydedilmesi gerektiği söylenebilmektedir. Kaydedilmekte olan hizmet prim sözleşmesine dahil olan yalnızca 1 cari bulunması durumunda "Cari Kısıt Tipi" bölümünden "Cari Kodu" seçimi yapılmalı ve alanın hemen yanındaki "Cari Kısıt" sahasına ilgili cari kodu girilmelidir. Eğer ilgili primi hak ediş noktasında bir cari grubunun varlığından söz ediliyorsa cari kısıt tipi alanından "Grup Kodu" seçimi yapılmalı ve cari kısıt sahasına da ilgili cari grubu girilmelidir. Benzer şekilde cari kısıt tipi olarak Kod-1, Kod-2, Kod-3, Kod-4 ya da Kod-5 seçimleri yapmak da mümkündür. Cari kısıt tipi alanında yapılacak seçime göre "Cari Kısıt" alanı rehberi de otomatik olarak değiştirilecektir. Şu ana kadar bahsedilen cari kısıt tiplerinin yeterli olmaması durumunda ise son seçenek olan "SQL" tipli cari kısıtı seçilebilmektedir. Böylece alanın hemen yanında ileri kısıt bileşeni görüntülenecek ve istenen ileri kısıtların buradan verilerek prim hak edişe konu olan carilerin kaydedilmesi mümkün olacaktır.

![](../../_assets/82034cfec180205bf7c8.png)

Sekmedeki "Tip" alanından, Alış ya da Satış seçimlerinden biri hizmet prim sözleşmesine uygun olarak yapılabilmektedir. Alış seçimi yapıldığında prim hesaplamaları üst bölümde seçilen carilerin alış faturaları üzerinden, satış seçimi yapıldığında ise satış faturaları üzerinden yapılacaktır. Hizmet primlerinin belirli bir döviz cinsinden olan faturalar üzerinden takip edilmek istendiği durumlarda ise ekrandaki "Dövizli İşlem Yapılsın" parametresi işaretlenmeli ve ardından prim hesaplaması yapılacak döviz cinsi, "Döviz Tipi" alanına kaydedilmelidir.

"Başlangıç Tarihi" ve "Bitiş Tarihi" alanları ilgili primin hangi tarih aralığındaki faturalar kullanılarak hesaplanacağını belirtmek için kullanılmaktadır. "Prim Değerlendirme Sayısı" sahası ise belirlenen bu tarih aralığında kaç kez prim hesaplanacağını belirlemek için kullanılmaktadır. Başlangıç ve bitiş tarihleri arasında kalan süre, prim değerlendirme sayısına göre eşit şekilde bölünecek ve bu eşit zaman aralıklarından her biri için bir prim hesaplaması yapılacaktır.

![](../../_assets/69daaba4b119860d0f2c.png)

Ekrandaki "Matrah Türü" alanı ise ilgili primin hangi tutar baz alınarak hesaplanacağına ilişkin seçimleri içermektedir. Buradan "Net Ciro" seçimi yapılırsa prim, KDV tutarı hariç ve iskonto uygulanmış bedel üzerinden hesaplanacaktır. "Brüt Ciro" seçimi primin, KDV tutarı hariç ve iskonto uygulanmamış bedel üzerinden hesaplanmasını sağlamaktadır. "İskonto Ciro" seçimi ise "İskonto Kademe" alanını aktifleştirmektedir. İskonto ciro seçimi yapıldığında prim hesaplaması, brüt tutar üzerinden iskonto kademe sahasına girilen değere göre satır iskontosu uygulanmış tutar üzerinden hesaplanır. Örneğin iskonto kademe sahası 3 olarak girilmişse brüt değerden 3 satır iskonto tutarı düşülerek elde edilen tutar üzerinden prim hesaplanacaktır. Ekrandaki bir diğer alan olan "Prim Belge Stok Kodu" alanı, prim hesaplaması sonrasında oluşturulacak sipariş ya da fatura belgesine girilecek stok kodunu belirtmek için kullanılmaktadır.

Prim tanım bilgileri sekmesinde 3 adet parametre bulunmaktadır. Bunlardan ilki olan "Prim belgeleri için kısıt uygulaması olacak mı" parametresi, aynı alış/satış faturasının birden çok hizmet prim sözleşmesinin kapsamına girdiği durumlarda anlamlıdır. Bu gibi senaryolar bulunması halinde ilgili sözleşmelerde bahsi geçen parametre işaretlenirse, aynı fatura için birden çok kez prim hesaplanması engellenecektir. Bu durumda farklı sözleşmelerin kapsamına giren ortak fatura, öncelikle prim hesaplaması yapılan sözleşmede kullanılacak ve diğer sözleşme/sözleşmelerin prim hesabına dahil edilmeyecektir.

Sekmedeki bir diğer parametre olan "Kota Miktar/Ciro Hesaplanırken Kısıtlarda Girilen Farklı Kısıt Tiplerinin Toplamı Uygulansın" parametresi ise aynı sözleşme altında birden çok stok için kota tanımlaması (Kota kavramı bu bölümün devamında detaylı olarak anlatılmıştır.) yapıldığında anlamlıdır. Tek bir sözleşmede birden çok stokun olduğu bir senaryoda, ilgili parametre işaretlenmeden prim hesaplaması yapılırsa; sözleşmedeki her bir stok için kota bilgileri ayrı ayrı kontrol edilecek ve her bir stoka ait toplam miktar/ciroya bakılarak ayrı ayrı prim hesaplaması yapılacaktır. Aynı senaryoda "Kota Miktar/Ciro Hesaplanırken Kısıtlarda Girilen Farklı Kısıt Tiplerinin Toplamı Uygulansın" parametresi işaretlendiğinde ise yine her bir stok için kendi kotasına göre ayrı ayrı prim hesaplanacaktır ancak bu kez hesaplama, sözleşme altındaki tüm stokların toplam miktar/cirosuna bakılarak yapılacaktır.

Sekmedeki son parametre ise "Prim Değerlendirme İşleminde Grup Hesaplamada Tüm Grup Sınır Değerleri Dikkate Alınsın" parametresidir. Bu parametre de yine aynı sözleşme altında birden çok stok için kota tanımlaması yapıldığında anlamlıdır. İlgili parametre işaretlendiğinde "Kota Girişi" sekmesindeki "Grup Hesaplaması Sıfırlansın" parametresi de aktif hale gelecektir. "Prim Değerlendirme İşleminde Grup Hesaplamada Tüm Grup Sınır Değerleri Dikkate Alınsın" parametresi, prim değerlendirmesine dahil edilen fatura tutar/miktarlarının belirli bir kota sınırı içine girdiğinde sıfırlanmasını sağlayan ve çok özel senaryolarda kullanılabilecek bir parametredir. Bu parametre kullanılırken, hangi özel kota aralığında hesaplanan primin sıfırlanması isteniyorsa, o aralıktaki kota için "Grup Hesaplaması Sıfırlansın" parametresi de işaretlenmelidir. Bu durumda sözleşmedeki stoklardan "Grup Hesaplaması Sıfırlansın" seçeneği işaretli olan stok, ilgili kota aralığına girerse, bu stokla birlikte sözleşmedeki diğer tüm stoklar için de hesaplanan prim sıfırlanacaktır. Dolayısıyla toplam prim hak edişi 0 olacaktır.

![](../../_assets/dfe7302478b46bf0148b.png)

Prim tanım bilgileri ekranındaki girişler tamamlandıktan sonra "Kota Girişi" sekmesine geçilmelidir. (Bkz. Ekran Görüntüsü 5) Kota girişi sekmesi, prim hesaplamalarının hangi limitlere göre ve hangi stokların alış/satışlarına göre yapılacağının kaydedilmesini sağlamaktadır.

Sekmedeki ilk alan olan "Hizmet Primine Esas Stok Seçimi" alanı, hangi stokların alış ya da satışları üzerinden prim hesaplanacağını belirtmekte kullanılmaktadır. Bu anlamda prim sözleşmesine bağlı olarak tek bir stok üzerinden prim hesaplanıyor olabileceği gibi farklı stok grupları için de hesaplama yapılması gerekebilir. Eğer sözleşmeye konu olan primi hak ediş noktasında yalnızca bir stokun alış/satışı baz alınıyorsa "Hizmet Primine Esas Stok Seçimi" sahasından "Stok Kodu" seçimi yapılmalı ve alanın hemen yanındaki "Kod" alanına ilgili stok kodu girilmelidir. Eğer prim hesaplaması bir stok üzerinden değil de bir stok grubu üzerinden yapılacaksa hizmet primine esas stok seçimi alanından

"Grup Kodu" seçimi yapılmalı ve kod sahasına da ilgili stok grubu girilmelidir. Benzer şekilde hizmet primine esas stok seçimi olarak Cari/S Kodu, Üretici Kodu, Kod-1, Kod-2, Kod-3, Kod-4, Kod-5 ya da Hepsi seçimleri yapmak da mümkündür. Hizmet primine esas stok seçimi alanında yapılacak seçime göre "Kod" alanı rehberi de otomatik olarak güncellenecektir. Şu ana kadar bahsedilen hizmet primine esas stok seçimlerinin yeterli olmaması durumunda ise "SQL" seçimine başvurulabilmektedir. Böylece alanın hemen yanında ileri kısıt bileşeni görüntülenecek ve istenen ileri kısıtların buradan verilerek prim hak edişe konu olan stokların kaydedilmesi mümkün olacaktır.

![](../../_assets/3283e923996ba6048111.png)

Bu noktada bir detay olarak "Kısıt Tipi" alanındaki hiyerarşiden bahsetmek gerekmektedir. Aynı prim sözleşmesi içinde birden çok kısıt tipi ile tanımlamalar yapılmasına izin verilmektedir. Örneğin hem bir "Stok Kodu" için hem de bir "Grup Kodu" için aynı sözleşme içinde tanımlar bulunabilmektedir. Bu durumlarda farklı kısıt tiplerinin 2 ya da daha fazlasına birden dahil olan stokların bulunma ihtimali de karşımıza çıkmaktadır. Bu tip bir senaryo gerçekleştiğinde prim hesaplaması yapılırken dikkate alınacak hiyerarşi, kısıt tipi alanındaki sıralamayla aynı şekilde; yani Stok Kodu-Cari/S Kodu-Üretici Kodu-Grup Kodu-Kod-1,Kod-2,Kod-3,Kod-4,Kod-5,SQL ve Hepsi şeklindedir. Aynı sözleşmede, birden çok kısıt tipine uyan bir stok için prim hesaplanırken bahsedilen hiyerarşi takip edilecek ve öncelikli olan kısıt tipine göre prim hesaplaması yapılacaktır.

Prime esas stok seçimlerinin yapılmasının ardından "Kota Özellikleri" kısmına geçilmelidir. Bu bölümde prim hesaplaması yapılırken dikkate alınacak kotaların tanımlanması mümkündür. Öncelikle "Kota Tipi" alanından ciro ya da miktar seçimi yapılmalıdır. Prim hesaplaması yapılırken bu bölümde yapılacak seçime göre alış/satışı yapılan stokların ciroları ya da alış/satış miktarları baz alınacaktır. Burada bir detay olarak kota tipinin "Miktar" olarak seçilmesi durumunda prim tanım bilgileri sekmesindeki matrah türü seçiminin geçersiz kalacağından bahsedilmelidir. Ekrandaki "Kota Yok" parametresi ise alış/satışlardan bağımsız sabit prim sisteminin uygulandığı durumlarda kullanılması gereken bir parametredir.

Sekmedeki "Ölçü Birimi" alanı ise prim hesaplanırken kullanılacak miktar bilgilerinin hangi ölçü birimi cinsinden değerlendirileceğini belirtmekte kullanılmaktadır.

Ekrandaki bir diğer bölüm olan "Hak Ediş Özellikleri" kısmında yapılacak "Oran" ya da "Tutar" seçimlerine göre, hak edilen prim oransal ya da tutarsal olarak hesaplanacaktır. Bir diğer deyişle burada yapılacak seçimle, hak edilecek primin fatura tutar/miktarının % X' i olarak mı, yoksa fatura tutar/miktarına göre sabit XXX TL (döviz seçimi yapılmamışsa) olarak mı hesaplanacağına karar verilmektedir.

Yine bu bölümdeki "Hak Ediş Adet Bazında" parametresi ise hak ediş olarak "Tutar" seçimi yapıldığında anlamlıdır. Bu seçim yapıldığında satışı/alışı gerçekleşen her 1 adet ürün için prim hesaplaması yapılacaktır.

Hizmet primi hesaplanırken karşılaşılabilecek bir istisna senaryo olarak, alış/satışlardan bağımsız şekilde sabit prim sisteminin bulunduğu durumlardan bahsedilmelidir. Böyle bir senaryo için hizmet prim tanımlama ekranında şu tanımlar yapılmalıdır; hizmet primine esas stok seçimi "Hepsi", kota özellikleri "Kota Yok" ve hak ediş özellikleri "Tutar". Bahsedilen tanımlar bu şekilde yapıldığında, verilen tarih aralığında alış/satış olmasa bile "Değer" alanında yazılan tutar kadar prim hak edişi hesaplanacaktır.

Hak ediş özellikleri altındaki bir diğer parametre ise "Kademeli" parametresidir. Bu parametre hak ediş özelliği "Oran" olarak seçildiğinde kullanılabilmektedir. Kademeli parametresi seçildiğinde, prim hak edişe konu olan alış/satışların toplam miktar/tutarları üzerinden bir kota değerlendirmesi yapılmaz. Bunun yerine alış/satış faturalarının toplam tutar/miktarına bakılır ve sırayla her bir kota aralığına denk gelen prim hesaplanarak ilerlenir. Primi hesaplanan her kota aralığının ardından, toplam tutar/miktardan, hesaplanan kotaya dahil olan tutar/miktar çıkarılır ve kalan bakiye üzerinden sıradaki kotaya düşen prim hesaplanır.

Örneğin 100 TL ile 500 TL arası satış faturaları için %10, 500 TL ile 1000 TL arası satış faturaları için %20 kota değerleri olan bir hizmet prim sözleşmesi olduğunu varsayalım. Sözleşmeye konu olan stok için 2 satış faturamız olduğunu ve bunlardan ilkinin tutarının 300 TL, ikincisinin tutarının ise 400 TL olduğunu düşünelim. Böyle bir senaryoda "Kademeli" parametresi işaretliyse hesaplama şu şekilde olacaktır; toplam 700 TL olan hak edişe konu satış faturalarının ilk kota aralığına denk gelen 500 TL'si için %10 prim hesaplanacaktır ve karşılığı 50 TL olacaktır. Toplam 700 TL olan faturaların 500 TL'lik kısmı değerlendirilmiş ve geriye 200 TL'lik kısım kalmıştır. Bu kısım da ikinci kota aralığına yani %20'lik prim hak edişine denk gelmektedir. Kalan 200 TL fatura bedeli için de %20 prim hesaplanacaktır ve karşılığı 40 TL olacaktır. Dolayısıyla bu örnekte toplam 90 TL'lik bir prim hak edilmiş olacaktır.

Aynı örnekte "Kademeli" parametresi işaretlenmeden bir hesaplama yapılırsa toplam 700 TL olan fatura bedelinin tamamı ikinci kota aralığına dahil edilecek ve %20 prim hesaplanacaktır. Hesaplanan primin değeri ise 140 TL olacaktır.

Sekmedeki son bölüm olan "Kota Girişi" bölümü ise hak edişe konu olan primin hangi aralıklardaki alım/satımlar için, hangi değerde verileceğini belirtmekte kullanılmaktadır. Burada verilecek alt-üst sınır değerleri, "Kota Tipi" alanındaki seçime göre belirlenmektedir. Benzer şekilde burada verilecek "Değer" de, hak ediş özellikleri alanındaki seçime göre oransal ya da tutarsal olarak değerlendirilecektir. Sahadaki "Alt Sınır" alanı pasif bir alandır ve 0'dan başlayarak kullanıcının verdiği her bir üst sınır değerine göre otomatik güncellenmektedir. Örneğin Ekran Görüntüsü 5'teki kayıtta, kota tipi "Ciro" ve hak ediş özellikleri "Oran" olarak seçildiğinden, 100 TL ile 300 TL arası cirosu olan satışlar için (Bu örnekte "Tip" olarak satış seçimi yapılmıştı.) %10'luk bir prim hesaplanacağı anlaşılmaktadır.

#### Hizmet Prim Değerlendirme

Logo Netsis hizmet prim uygulamasının kullanılabilmesi için tamamlanması gereken ilk adım olan hizmet prim tanımlamaları yapıldıktan sonra, yapılan tanımlara uygun primlerin hesaplanabilmesi için "Hizmet Prim Değerlendirme" ekranı kullanılmalıdır. Finans-Cari-Kayıt-Hizmet Bilgileri Girişi yolu izlenerek ulaşılan ekran üzerinden gerekli girişler yapıldığında hesaplanan hizmet primi görüntülenebilecektir.

![](../../_assets/c18e448ef46632b6094e.png)

Hizmet prim değerlendirme ekranının ilk sahası olan "Hizmet Prim Kodu" alanına, hizmet prim tanımlama ekranı üzerinden kaydedilmiş olan ve prim değerlendirmesi yapılmak istenen hizmet prim kodu girilmelidir. Ekrandaki "Cari Kısıt" ve "Tip" alanları ise ilgili hizmet prim koduna ait cari ve tip detayları hakkında kullanıcıya bilgi vermek amacıyla pasif olarak gösterilen, üzerinde değişiklik yapılamayan alanlardır. Bahsi geçen alanların hemen altındaki "Cari kısıtta verilen tüm carilerin belgeleri listelenebilsin" parametresi ise ilgili hizmet prim sözleşmesine dahil olan birden çok carinin bulunduğu durumlarda anlamlıdır. Böyle bir senaryoda "Cari kısıtta verilen tüm carilerin belgeleri listelenebilsin" parametresi işaretlendiğinde sözleşmeye konu olan tüm carilerin hareketleri grid alanda listelenecektir. Eğer parametre işaretlenmezse, hemen altındaki "Cari Kodu" alanının doldurulması zorunlu olacaktır ve sözleşmeye konu carilerden yalnızca bir tanesinin cari kodu alanına girilmesi beklenecektir. Bu durumda ekranın grid alanında, ilgili sözleşmeye dahil olan carilerden yalnızca "Cari Kodu" alanına girilmiş olanının belgeleri görüntülenecektir. Ekrandaki "Dönem Aralığı" alanı ise, hizmet prim tanımlama ekranında girilen başlangıç ve bitiş tarihleri ile değerlendirme sayısına göre otomatik olarak doldurulacaktır. İlgili dönem aralığındaki değerlendirme sayısı 1'den çoksa, sistem tarafından son değerlendirme kontrol edilecek ve tarih aralığı, sıradaki değerlendirme dönemine uygun olarak getirilecektir. İstenirse bu alanların manuel olarak değiştirilmesi mümkündür. Ekranın üst kısmındaki gerekli bilgilerin doldurulmasının ardından kısıtlara uygun belgelerin listelenebilmesi için ekranın sağ alt bölümündeki "Prime Esas Hareketleri Listele" butonuna basılmalıdır. Butona tıklandığında ekranın alt kısmında verilen kısıtlara uygun tüm belgeler listelenecektir. Listelenen belgelerin tümünün prim değerlendirmesine dahil edilmesi ise zorunlu değildir. Belgelerin hemen solundaki kutucuklardan istenenlerin seçimleri kaldırılarak prim değerlendirmesinin dışında bırakılabilir.

![](../../_assets/aaa6bad5b032efbd683e.png)

İstenen belge seçimleri tamamlandıktan sonra ekran görüntüsünde eşil kutucuk içinde gösterilen "Prim Değerlendir" butonuna tıklandığında ise hizmet prim değerlendirme ekranının grid alanında listelenen ve seçili olan belgelere ait prim değerlendirmesinin görüntülendiği yeni bir pencere görüntülenecektir.

![](../../_assets/89997f568786563ef644.png)

Prim değerlendirmesinin görüntülendiği pencerede ilgili hizmet prim sözleşmesine ait özet bilgiler yer almaktadır. Ayrıca kota bilgilerinin özet olarak gösterildiği bölümde, yapılmakta olan değerlendirmenin dahil olduğu kota değerleri koyu renkli şekilde gösterilmektedir. Değerlendirmenin en altında kırmızı renkle gösterilen satır ise hak edilen primi belirtmektedir. Ekrandaki bilgiler kontrol edildikten sonra ilgili değerlendirmenin kayıtlara geçmesi ve prim ödemesinin sistem üzerinde belgelendirilebilmesi için Ekran Görüntüsü 8'de yeşil kutucuk içinde gösterilen "Prim Belgesi Oluştur" butonuna tıklanmalıdır.

![](../../_assets/83fcde26fc8bb0d43f79.png)

Prim belgesi oluştur butonuna tıklandıktan sonra açılacak yeni pencerede belgeye ait seçimlerin yapılabileceği alanlar bulunmaktadır. Bunlardan ilki olan "Belge Numarası" alanı sıradaki belge numarasıyla otomatik olarak doldurulacaktır ancak isteğe bağlı olarak değişiklik yapmak mümkündür. Alış tipli prim sözleşmeleri için oluşturulacak belge müşteri siparişiyken, satış tipli prim sözleşmeleri için satıcı siparişidir. Eğer sipariş belgesi oluşturulmadan doğrudan fatura oluşturulmak istenirse ("HIZMETPRIM", "FATURA") özel parametresi kullanılabilmektedir.

"Belge Tarihi" bilgisi ise günün tarihiyle otomatik olarak doldurulacaktır ancak manuel değişiklik yapılabilmektedir. "Prim Fatura Carisi" alanı, tek bir carinin dahil olduğu sözleşmelerde otomatik olarak ilgili cari bilgisi ile dolu olarak getirilecektir ve değişiklik yapılamayacaktır ancak birden çok carinin dahil olduğu sözleşmelerde alan rehberi kullanılarak sözleşmeye dahil carilerden birinin fatura carisi olarak seçilmesi gerekmektedir.

Ekrandaki gerekli alanlar doldurulduktan sonra Ekran Görüntüsü 9'da yeşil kutucuk içinde gösterilen "Prim Belgesi Görüntüle" butonuna tıklanmalıdır. Ardından ekranın alt bölümünde belgeye ait özet bilgiler görüntülenecektir ve gerekli kontroller yapılıp "Prim Belgesi Oluştur" butonuna tıklandığında ilgili belge yaratılacaktır. Tüm bu işlemler yapılırken bir önceki ekrana dönmek için ekranın sağ alt köşesindeki butonlar kullanılabilmektedir. Örneğin prim belgesi oluşturma ekranında "Prim Değerlendirme" butonu görüntülenmektedir ve butona tıklandığında bir önceki ekrana dönülmektedir.

Bir prim sözleşmesinin değerlendirme sayısı 1'den büyükse ve ilk değerlendirme yapıldıysa ikinci kez prim değerlendirme yapılacağı sırada ekrandaki "Önceki Dönem Hesaplamaları Göster" seçeneği aktif olacaktır. (Bkz. Ekran Görüntüsü 7) Bu seçeneğe tıklandığında önceki dönemlerde değerlendirmesi yapılıp belgeleri oluşturulmuş tüm prim kayıtları yeni bir pencerede görüntülenecektir. Eğer herhangi bir prim kaydı iptal edilmek istenirse öncelikle ilgili belge silinmeli ardından "Önceki Dönem Prim Hesaplamaları" ekranındaki iptal butonuna tıklanmalıdır.

![](../../_assets/475563816b39f3333817.png)

Bir prim dönemindeki tüm değerlendirmeler tamamlandığında ise ilgili prim için hizmet prim değerlendirme ekranında yalnızca "Önceki Dönem Hesaplamaları Göster" butonu çalışacaktır ve bu butona tıklandığında açılan pencerede belgeleri oluşturulan prim detaylarıyla birlikte "Prim hesaplama limitini tamamladınız." uyarısı görüntülenecektir.

![](../../_assets/833447a8d6339b99719c.png)

#### Maliyet Dağıtımı

Hizmet prim uygulaması kapsamında kullanılabilecek sonuncu fonksiyon ise maliyet dağıtımıdır. Bu işlem, alış ya da satış tipli bir hizmet prim sözleşmesinin değerlendirme ve fatura oluşturma işlemlerinin tamamlanmasından sonra geçilebilecek bir aşamadır. Değerlendirmesi tamamlanmış ve primine dair faturası oluşturulmuş bir hizmet prim sözleşmesi için maliyet dağıtımı yapılması, primin, prim hesaplanan stoklara dağıtılması anlamına gelecektir. Faturaya dönüştürülmesi tamamlanan primlerin ilgili stoklara dağıtılması, maliyetlerin de değişmesini sağlayacaktır. Bahsedilen maliyet dağıtım işleminin yapılabilmesi için kullanılacak "Maliyet Dağıtımı" ekranına Lojistik-Satış-Fatura-İşlemler-Hizmet- Maliyet İşlemleri yolu izlenerek ulaşılabilmektedir.

![](../../_assets/2e2e1a6fedee64e1fd23.png)

Maliyet Dağıtımı ekranı, yalnızca hizmet prim belgelerinin maliyet dağıtımı için kullanılabilecek bir ekran değildir. İlgili ekran, dağıtımı yapılacak kaynak belge ve dağıtma yapılacak hedef belge seçimlerinin yapılabileceği 2 bölümden oluşmaktadır ve her türlü belgenin kaynak ya da hedef olarak seçilerek maliyet dağıtımının yapılması mümkündür. Hizmet prim belgeleri içinse, bu dağıtımın daha pratik şekilde yapılabilmesi için sistemde varsayılan olarak bulunan ve ekran görüntüsünde yeşil kutucuk içinde gösterilen "Hizmet Prim Belgeleri" tipli maliyet dağıtım anahtarı desteği bulunmaktadır. Bu anahtar seçildikten sonra ekran görüntüsündeki mor kutucuk içinde gösterilen "Kayıt Getir" butonuna basıldığında sistemde faturaya dönüştürülme işlemi tamamlanmış tüm hizmet prim belgeleri ekranın üst kısmındaki kaynak belgeler bölümünde otomatik olarak listelenecektir. Ayrıca "Hizmet Prim Belgeleri" tipli maliyet dağıtım anahtarı seçiliyken "Kayıt Getir" butonuna tıklandığında Ekran Görüntüsü 13'teki seçim mesajı görüntülenecektir.

![](../../_assets/94ad4d4019ce39134662.png)![](../../_assets/d3147d002148d0572524.png)

Bu mesaja "Evet" olarak yanıt verildiğinde, maliyet dağıtımı ekranının üst kısmında kaynak belge olarak listelenen prim faturalarının hesaplanması sırasında kullanılan tüm alış/satış faturaları da ekranın alt kısmındaki hedef belge alanında otomatik olarak listelenecektir. Bu mesaja "Evet" yanıtı verilmesi aynı zamanda ekran görüntüsünde yeşil kutucuk içinde gösterilen "Prime Esas Hareketler Dikkate Alınsın" parametresinin seçilmesini de sağlamaktadır. Hedef belgeler listesinde yalnızca prime esas, yani ilgili prim faturalarının hesaplanmasına dahil edilen alış/satış faturalarının listelenmesi değil, sistemdeki tüm faturaların listelenmesi istenirse, "Prime Esas Hareketler Dikkate Alınsın" parametresinin seçimi kaldırılmalı ve ardından hedef belge kısıtları bölümündeki "Kayıt Getir" butonuna tıklanmalıdır.

![](../../_assets/32e80ac472fa36bae905.png)

Yukarıda bahsedilen adımlar gerçekleştirildiğinde hedef belgeler bölümüne, ekran görüntüsünde görüldüğü gibi sistemdeki tüm faturalar listelenecektir. Benzer şekilde dağıtılacak kaynak belge bölümünde de sadece prim faturalarının listelenmesi değil, sistemdeki tüm faturaların listelenmesi istenirse maliyet dağıtım anahtarı alanındaki "Hizmet Prim Belgeleri" seçimi temizlenmeli ve ardından kaynak belge kısıtları bölümündeki "Kayıt Getir" butonuna tıklanmalıdır.

Maliyet dağıtım ekranının hedef belge bölümünde listelenen tüm faturalara dağıtım işlemi yapılması zorunlu değildir. Ekran görüntüsünde mor kutucuk içinde gösterildiği gibi, "Dağıtım Yapılacak" sütununda istenen satırda çift tıklama yapılarak, ilgili satıra dağıtım yapılıp yapılmayacağı fatura bazında seçilebilmektedir. Maliyet dağıtımı ekranı kapsamında hem kaynak hem de hedef belge kısıtları bölümlerinde, ilgili belge listeleri manuel kısıtlar verilerek de oluşturulabilmektedir. Bunun için her bir bölümdeki Genel Kısıtlar, Ek Kısıtlar, Stok Kısıtları ve Cari Kısıtları alanları kullanılabilmektedir. Bahsedilen "Ek Kısıtlar" alanı parametrik bir sahadır ve alış fatura parametreleri ekranındaki "Sipariş/İrsaliye/Faturada Ek Sahalar Kullanılsın" parametresinin seçili olduğu durumlarda görüntülenebilmektedir.

![](../../_assets/60c86920a60004e8fea8.png)![](../../_assets/6d0c97c790c6edc58713.png)![](../../_assets/41b64928280cfcb9835d.png)![](../../_assets/13e735eed3126ccb5a31.png)![](../../_assets/a8b62ad309f49e9b2b53.png)![](../../_assets/fde60b0fa835a6f8fcf2.png)

![](../../_assets/6da917d61cfc4a83045f.png)

Maliyet dağıtımı ekranı üzerindeki hedef ve kaynak belge listeleri istenen şekilde oluşturulduktan ve gerekli seçimler yapıldıktan sonra, kaynak belge bölümündeki "Dağıtım Tipi" sütunundan "Miktar" ya da "Tutar" seçimi yapılmalıdır. Buradan yapılacak seçime göre kaynak belgelerin "Dağıtılacak Tutar" bedelleri ya hedef belgelerin miktarlarıyla ya da tutarlarıyla orantılı şekilde, kaynak belgeler üzerinden hedef belgelere dağıtıma hazır hale gelecektir. Ardından kaynak belge bölümündeki "Dağıt" sütunu, dağıtımı yapılmak istenen kaynak belgeler için çift tıklanmalıdır. Bu işlem sonrasında kaynak belgelerin "Dağıtılacak Tutar" sütununda gösterilen bedel, hedef belgelere dağıtılacaktır.

Tüm bu işlemler sonunda ekran görüntüsünde kırmızı kutucuk içinde gösterilen "Kaydet" butonuna basılmalıdır. Butona tıklandığında ilgili dağıtım işlemi sistemsel olarak gerçekleştirilecek ve dağıtma işlemine ait fiş oluşturulacaktır.

![](../../_assets/b124ff68ed21d51ed376.png)![](../../_assets/dd821c9e5d06c63de938.png)![](../../_assets/ae9a244359590640431f.png)![](../../_assets/af6027cee896d22778df.png)

Yapılan dağıtım iptal edilmek istendiğinde ise maliyet dağıtımı ekranının "Fiş No" kısmından ilgili belge seçilmeli ve "Fiş İptal" butonuna tıklanmalıdır. Maliyet dağıtımı ekranında "Dağıtılacak Tutar" alanı otomatik olarak getirilmektedir ancak istenirse bu alanın manuel olarak güncellenmesi mümkündür. Bu şekilde bir güncelleme yapılarak maliyet dağıtımı gerçekleştirilirse, aynı belge için yeniden bir dağıtım yapılmak istendiğinde "Dağıtılmış Tutar" sütununda daha önce yapılan kısmi dağıtıma ait bedel görüntülenecek ve kalan tutar da yine "Dağıtılacak Tutar" sütununda gösterilecektir.

![](../../_assets/089c337bb4baf4840dae.png)

Hizmet Prim Uygulaması kapsamında hesaplanan primin, ilgili belgelere dağıtımı tamamlandıktan ve dağıtım fişi oluşturulduktan sonra, yapılan maliyet dağıtımının birim fiyatlara etkisi; serbest maliyet ambar raporu, lokal depo maliyet raporu, LIFO, FIFO, fatura karlılık raporu, mal detaylı karlılık raporu ve stok karlılık raporlarında izlenebilmektedir. Bunun için bahsedilen raporların "Genel Kısıtlar" sekmelerindeki "Ek Maliyet Dağıtım Uygulaması Kullanılsın" parametresi işaretlenmiş olmalıdır.

![](../../_assets/07ba136c7726b8d5550a.png)
