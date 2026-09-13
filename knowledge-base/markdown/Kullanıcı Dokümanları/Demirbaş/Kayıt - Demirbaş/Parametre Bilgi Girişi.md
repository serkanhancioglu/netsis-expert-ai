---
title: "Parametre Bilgi Girişi"
page_id: "50683709"
product: "netsis-3-enterprise"
depth: 4
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Demirbaş"
  - "Kayıt / Demirbaş"
  - "Parametre Bilgi Girişi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Demirbaş / Kayıt / Demirbaş / Parametre Bilgi Girişi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWZmNDQyZDE1LWE1MDMtNGZiMS05ZjdkLTQ1NTg1NDBlOGYwMSZsaW5rPWM1NmU3OTRhLTE4MzktNDg3Ni05MDQ5LThhNjM5YTM2ZWU5YiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=ff442d15-a503-4fb1-9f7d-4558540e8f01&link=c56e794a-1839-4876-9049-8a639a36ee9b&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "parametre-bilgi-girisi_50683722_50683709.html"
source_version: "2022-11-14T11:52:22.023+03:00"
source_bytes: 29386
fetched_at: "2026-09-13T04:21:18+00:00"
generator: "netsis-scraper 1.0.0"
---
# Parametre Bilgi Girişi

Parametre Bilgi Girişi, Demirbaş modülünde kullanılacak parametrelerin tanımlandığı bölümdür. Parametre Bilgi Girişi ekranı; Genel, Veritabanı Bilgileri, Dövizli Muhasebe, Kullanıcı Tanımlı Sahalar olmak üzere dört sekmeden oluşur.

**Genel**

Parametre Bilgi Girişi ekranı Genel sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Parametre Bilgi Girişi Ekranı |  |
| --- | --- |
| Dönem Sayısı | Devletin değerleme oranı açıkladığı dönem sayısının girildiği alandır. Mevcut uygulamaya göre bu sayı 4’tür. Eğer bu dönemler devlet tarafından değiştirilirse, yeni dönem sayısının mutlaka girilmesi gerekir. |
| Mali Başlangıç Ayı | Bilindiği gibi bazı sektörlerde mali başlangıç ayı 1. ayın dışında başka bir ay olabilir. Programın bir mali dönemi hesaplayabilmesi için mali başlangıç ayının girilmesi gerekir. **Örneğin,** Mali başlangıç ayı 7. ay olan bir firma için program, mali dönemin, içinde bulunulan cari yılın 7. ayından başlayıp bir sonraki yılın 6. ayında bittiğini düşünür. |
| Tutar İçin Ondalık Hane | Oluşan tüm değerleri kuruşlu olarak tutmak isteyen şirketlerin, raporda görüntülenmesini istediği ondalık hane sayısını girdiği alandır. |
| Hızlandırılmış Yöntem İçin Amortisman Tavan Oranı | Demirbaş Bilgi Kartı ekranında bulunan Amortisman Tipi bölümünden, "Hızlı" seçeneğinin işaretlenmesi halinde, Değerleme ve Amortisman Ayırma işleminde demirbaş kartında girilen amortisman oranının iki katı üzerinden amortisman ayrılır. Bu durumda, amortisman oranı yüksek olan demirbaşlarda - örneğin %30 - hızlı amortisman uygulandığında, hesaplamalar yüksek oranlar üzerinden - %30 için, hızlı amortisman ayrılıyorsa %60 olarak dikkate alınarak - yapılır. Bu parametre ile de, amortisman hesaplamasının en fazla hangi oran üzerinden yapılacağı belirlenir. **Örneğin,** 50 değer, girildiğinde, hesaplamalarda kullanılacak oranın %50’yi geçmesi halinde, program ilgili demirbaşların amortisman hesaplamalarını %50 üzerinden yapar. |
| Entegrasyon Yapılsın | Aylık ve yıl sonu hesaplarının Entegrasyon modülü ile bağlantılı kullanılması için işaretlenmesi gereken parametredir. Bu bölümün kullanılması için Temelset üzerinde Entegrasyon modülü ile ilgili tanımlamaların daha önceden yapılması gerekir. Entegre modülünü kullanmayanların bu parametreyi işaretlememesi gerekir. |
| Aylık Amortisman Uygulaması | Maliyet Muhasebesi kullanan ve dolayısıyla aylık amortisman hesaplamaları yapan firmalar için kullanılan parametredir. Aylık Amortisman Uygulaması olmayan firmalar için bu parametrenin işaretlenmemesi gerekir. Her ay amortisman tutarlarını hesaplayan firmalarda bu parametrenin mutlaka seçilmesi gerekir. Bu tür firmaların parametreyi işaretlemeleri, üçer aylık dönemler sonunda açıklanan değerleme oranları ile hesaplanan amortisman tutarları ile aylar bazında hesapladıkları üçer aylık amortisman tutarları arasında çıkacak tutar farkları için bir fark mahsubunun yapılmasını sağlar. Böylece, firmaların aylık olarak hesapladıkları ve muhasebeye aktardıkları amortisman tutarları, devletin açıkladığı değerleme oranına göre hesaplanan amortisman tutarları ile eşitlenir. |
| Eski Kıstalyum Uygulaması | Demirbaş Sabit Kartında bulunan Kıstalyum seçeneği işaretlenen demirbaşlar için demirbaşın alındığı aydan itibaren amortisman ayrılır. Bu parametrenin işaretlenmesi halinde, demirbaş alımından bir sonraki yıl amortisman ayrılırken, demirbaşın alındığı yılda, yıllık amortisman ayrılmış gibi işlem yapılır. |
| Check Digit Kontrolü | Barkodla işlem yapan firmalarda, kullanıcıların barkod olmayan demirbaşlarda girdikleri numaranın sonundaki Check Digit numarasının program tarafından otomatik olarak hesaplanmasını sağlayan parametredir. Bu parametre ile, oluşacak bir yanlışın önlenmesi sağlanır. |
| Entegrasyonda Demirbaş Devam Bilgilerine Bakılsın | Demirbaş paketinde, entegrasyonda devam bilgilerinin bakılması için kullanılan parametredir. |
| Satış Muhasebeleştirmede Miktarlar Muhasebeye Aktarılsın | Demirbaş modülünden yapılan işlemlerde, satış muhasebeleştirme yapılırken miktarların muhasebeye aktarılması için kullanılan seçenektir. |
| Demirbaş Faiz Tutarları Muhasebeye Aktarılsın | Demirbaş faiz tutarlarının muhasebeye aktarılması istendiğinde kullanılan parametredir. |
| Güvenlik Uygulaması | Bu parametrede Satır Bazı Güvenlik Sistemi ile Kolon Bazı Geçerlilik Sisteminin ya da “Hepsi” seçeneği ile her ikisinin de seçilmesi halinde, Kullanıcı İşlemleri modülünde ilgili alanlar aktif hale gelir. Satır Bazı Güvenlik Sistemi ile Tüm Kullanıcılar, Grup ya da Tek Bir Kullanıcı için satır bazında kısıtlama verilebilir. Ancak, Satır Bazı Güvenlik Sistemi sadece Oracle veritabanında desteklenir. Kolon Bazında Geçerlilik Sistemi ile, Tüm Kullanıcılar, Grup ya da Tek Bir Kullanıcı için kolon bazında geçerlilik tanımlaması yapılabilir ve tanımlamalarınızdan farklı kayıt giren kullanıcıların program tarafından uyarılması sağlanabilir. |
| İş Akışı Uygulaması | İş Akış Yönetimi (Workplace) uygulaması, bu parametrenin işaretlenmesi ile aktif hale gelir. Buna göre, yetki düzeylerine göre yapılan/yapılacak tüm işlerin tanımlanması, onay akışlarının ve süresinin belirlenmesi mümkün hale gelir. Bunun için yapılması gereken, İş Akış Kayıtları ekranında, hangi işler için onay akışı tanımlanacağının belirlenmesidir. |
| Dinamik Kodlama Sistemi | Kullanıcı arabirimlerinin her yerine eklenen "Dinamik Kodlama" özelliği ile, programın standart davranışını değiştirecek kod yazılması, ekranların istenen şekilde değiştirilmesi, yeni özellikler kazandırılması gibi programlama tekniği ile yapılacak fonksiyonlar kodlanabilir. Bu uygulamaların yapılması için, öncelikle "Dinamik Kodlama Sistemi" parametresinin seçilmesi gerekir. Dinamik Kodlama özelliğinde, VBScript dili ile kodlama yapılır. VBScript kodlarını sadece yetkili olan kullanıcılar tanımlayabilir ve gerektiğinde geçersiz hale getirebilir. |
| Enter Tuş Desteği | Normalde klavyedeki \<tab\> tuşu ile alanlar arasında ilerleme yapılır fakat bu parametrenin işaretlenmesi ile, \<enter\> tuşu ile de ilerlenmesi mümkün hale gelir. |
| Form Bazı Güvenlik Uygulaması | Form Bazı Güvenlik uygulamasının kullanılmasını sağlayan parametredir. "Form Bazı Güvenlik Uygulaması" ile açılan herhangi bir form üzerinde görülen alanların, kullanıcı/grup bazında kaydın değiştirilmemesi ya da alanın görüntülenmemesini sağlar. |
| Aktif Alan Rengi | Ekrandaki aktif olan alanın renginin belirlendiği alandır. |

**Veritabanı Bilgileri**

Veritabanı Bilgileri sekmesinde yer alan Entegrasyon Veritabanı Bilgileri, Amortisman Hisse Muhasebeleştirme ve Satış Muhasebeleştirme işlemleri için sorgulanır. Eğer Demirbaş programında tutulan bilgiler, ticari pakete entegre edilmeyecekse, bu bölüme giriş yapılmasına gerek yoktur.

Parametre Bilgi Girişi ekranı Veritabanı Bilgileri sekmesi Entegrasyon Veritabanı Bilgileri bölümünde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Parametre Bilgi Girişi Ekranı |  |
| --- | --- |
| Veritabanı İsmi | Ticari paket ile entegre çalışan firmalar için kullanılan alandır. Ticari pakette bağlanılacak şirketin, şirket kodu yazılır. |
| Veritabanı Kullanıcı İsmi | Bilgilerin entegre edileceği şirketin veritabanı kullanıcısının adının girildiği alandır. Standart kurulum özelliklerinin dışına çıkılmamışsa "Temelset" kullanıcısı ile bağlanılması gerekir. |
| Veritabanı Şifresi | Veritabanı Kullanıcı İsmi alanına girilen kullanıcıya ait şifrenin girilmesi gereken alandır. "Temelset" T kullanıcısı ile ilgili şifre program tarafından bağlantı sırasında otomatikman okunacak olup boş geçilmelidir. |
| Veritabanı Tipi | Kullanılan demirbaş programının hangi veritabanında yazıldığının belirlendiği alandır. Oracle veritabanı kullanılarak yazılan demirbaş programı için dtORACLE, msSQL veritabanı kullanılarak yazılan demirbaş programı için ise dtMsSQL seçilmesi gerekir. Alanın sağ tarafında yer alan aşağı ok butonu ile seçim yapılır. |
| Şube Kodu | Demirbaş bilgilerinin, "Veritabanı Tipi" alanında belirtilen veritabanında tutulan şirketin hangi şubesine aktarılması isteniyorsa, o şubenin kodunun girildiği alandır. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile, şube kodları arasından seçim yapılır. |

Veritabanı Bilgileri sekmesinde yer alan Personel Veritabanı Bilgileri, Personel Veritabanı Bilgileri'nin sorgulandığı bölümdür. Bu bilgiler daha sonra anlatılacak olan Zimmet Uygulaması için sorgulanır. Eğer Zimmet Uygulaması kullanılacaksa, Personel Veritabanı Bilgileri'nin mutlaka doğru bir şekilde kaydedilmesi gerekir. Aksi takdirde Demirbaş Zimmetleme işlemi kullanılamaz.

Parametre Bilgi Girişi ekranı Veritabanı Bilgileri sekmesi Personel Veritabanı Bilgileri bölümünde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Parametre Bilgi Girişi Ekranı |  |
| --- | --- |
| Veritabanı İsmi | Bağlanılacak personel veritabanı isminin girildiği alandır. |
| Veritabanı Kullanıcı İsmi | Bilgilerin entegre edileceği şirketin veritabanı kullanıcı adının girildiği alandır. Standart kurulum özelliklerinin dışına çıkılmamışsa "Personel" kullanıcısı ile bağlanılması gerekir. |
| Veritabanı Şifresi | Veritabanı Kullanıcı İsmi alanına girilen kullanıcıya ait şifrenin girildiği alandır. "Personel" kullanıcısı ile ilgili şifre, program tarafından bağlantı sırasında otomatik olarak okunur ve boş bırakılması gerekir. |
| Veritabanı Tipi | Kullanılan demirbaş programının hangi veritabanında yazıldığının belirlendiği alandır. Oracle veritabanı kullanılarak yazılan demirbaş programı için dtORACLE, msSQL veritabanı kullanılarak yazılan demirbaş programı için ise dtMsSQL seçilmesi gerekir. Alanın sağ tarafında yer alan aşağı ok butonu ile seçim yapılır. |

**Dövizli Muhasebe**

Parametre Bilgi Girişi ekranı Dövizli Muhasebe sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Parametre Bilgi Girişi Ekranı |  |
| --- | --- |
| TL Muhasebe/ IAS29/ FAS52 | TL Muhasebe seçeneği seçildiğinde, firmada amortisman tutarlarının sadece TL mevzuatına göre hesaplanarak yapılacağı anlaşılır ve diğer seçeneklerde aktif olan işlem ve raporlar kullanılamaz. IAS29 seçeneği seçildiğinde, enflasyon muhasebesinin de kullanılacağı amortisman hesaplamasında enflasyona göre ayrıca bir hesaplama yapılacağı anlaşılır. Bu durumda, İşlemler → Dövize/ Enflasyona Göre Çevrim seçeneğinde, firma döviz tutarları, enflasyon değerleri bazında oluşturulur. FAS52 seçeneği seçildiğinde, dövizli muhasebenin de kullanılacağı, amortisman hesaplamasında döviz bazında ayrıca bir hesaplama yapılacağı anlaşılır. Bu durumda, İşlemler → Dövize/ Enflasyona Göre Çevrim seçeneğinde, firma döviz tutarları, döviz bazında oluşturulur. IAS29 veya FAS52 işaretleyen firmaların, aynı zamanda “Aylık Amortisman Uygulaması” parametresini de işaretlemesi gerekir. Bunun nedeni, Dövizli/Enflasyonlu Amortisman uygulamasında aylık işlem yapılmasının zorunlu tutulmasıdır. Bu durumda, aylık yeniden değerleme oranlarının girilerek uygulama yapılması gerekir. |
| Firma Döviz Tipi | Demirbaşlarını dövizle takip etmek isteyen firmaların, oluşturulacak döviz değerleri için baz alınmasını istedikleri döviz tipinin belirlendiği alandır. Yeni bir demirbaş kaydedildiğinde, alış tarihindeki kur baz alınarak, burada girilen döviz tipine göre firma döviz tutarı otomatik olarak hesaplanır. |
| Döviz Çevrim | Firma Döviz Tipi'ni belirleyen firmaların, döviz tutarlarının hesaplanmasında, ilgili döviz tipinin hangi kurunun baz alınacağının belirlediği alandır. |
| Döviz Katsayı Dönemi | Hem amortismanlarda döviz uygulaması, hem de dövizlerin TL üzerinden hesaplanması işleminde döviz katsayı dönemi kullanılabilir. Eğer amortisman tutarlarının hesaplanmasında değişik dönemlerde farklı oranlar kullanılacaksa bu parametrenin işaretlenmesi gerekir. Şirketlerin, amortismanlarının itfa oluncaya kadar ayrılan amortisman tutarlarının aylar bazında eşit olarak yapılmasını istiyorlarsa bu parametreyi işaretlememesi gerekir. **Örneğin;** Bu parametrenin işaretlenmemesi durumunda, Döviz Katsayı Dönemi: 3, Alış Tutarı: 120.000.000 TL, Amortisman Bitiş Yılı: 2, Amortisman Bitiş Ayı: 24 ise, bu durumda 24 ay için amortisman tutarı aşağıdaki şekilde hesaplanır. 120.000.000/24 = 5.000.000 TL. Eğer yukarıdaki parametre işaretlenirse; girilecek dönemlerin, Demirbaş Döviz Bilgileri Girişi bölümünden her demirbaş için katsayı değerlerinin girilmesi gerekir. **Örneğin;** Alış Fiyatı: 120.000.000 TL, Amortisman Bitiş Yılı: 2, 1. Dönem Katsayı: 0,5 2. Dönem Katsayı: 1, 3. Dönem Katsayı: 1,5 olsun. Bu durumda, 120.000.000/24=5.000.000 TL'dir. Bu tutar, katsayılar göz önünde bulundurulmasaydı, aylık amortisman tutarı olacaktı. Katsayılar dikkate alınınca demirbaşın itfa olma süresine kadar 3 ayrı oran ortaya çıkar. Buna göre, itfa süresi olan 24 ayın ilk 8 ayında 0.5 katsayısına, 2. 8 ayda 1 katsayısına ve 3. 8 ayda 1.5 katsayısına göre amortismanlar hesaplanır. Yani: 5.000.000 \* 0.5 = 2.500.000 TL. demirbaşın ilk 8 ayında ayrılacak olan amortisman tutarıdır. 2.500.000 \* 8 = 20.000.000 5.000.000 \* 1 = 5.000.000 TL. demirbaşın ikinci 8 ayında ayrılacak amortisman tutarıdır. 5.000.000 \* 8 = 40.000.000 5.000.000 \* 1.5 = 7.500.000 TL. demirbaşın üçüncü 8 ayında ayrılacak amortisman tutarıdır. 7.500.000 \* 8 = 60.000.000 Toplamda 20.000.000 + 40.000.000 + 60.000.000 = 120.000.000 TL tutarında amortisman ayrılır ve sabit kıymet değeri ile birikmiş amortisman tutarı birbirine eşitlenince demirbaş itfa olur. |
| Amortisman Başlangıç Ayı (Alınan Ay/Sonraki Ay) | Yeni alınan bir demirbaşın amortisman başlangıç ayının, amortismanlarda döviz uygulaması sisteminde hangi ay olacağının belirlendiği parametredir. Alınan ay işaretlendiğinde, amortisman ayırma işlemi demirbaşın alındığı aydan itibaren yapılır. Sonraki ay işaretlendiğinde ise, amortisman ayırma işlemi, demirbaşın alındığı bir sonraki aydan itibaren başlar. |
| Amortisman Hesaplama Günlük Değerler Üzerinden Yapılsın | Amortisman hesaplamasının günlük değerler üzerinden yapılması için kullanılan parametredir. |
| Demirbaş Ömrü Günlük Değer Olarak Sorulsun | Demirbaş ömrünün günlük değer olarak sorulması için kullanılan parametredir. |
| Sıfır Araç KDV+ÖTV Üst Sınır Bedeli (Gider) | Araç alımlarında KDV ve ÖTV üzerinden yapılacak gider bedeli üst sınırın girildiği alandır. |
| Sıfır Araç KDV+ÖTV Üst Sınır Bedeli (Maliyet) | Araç alımlarında KDV ve ÖTV üzerinden yapılacak maliyet bedeli üst sınırın girildiği alandır. |
| İkinci El Araç Üst Sınır Bedeli | İkinci el araç alımlarında kullanılacak üst sınır bedelinin girildiği alandır. |

**Kullanıcı Tanımlı Sahalar**

Parametre Bilgi Girişi ekranı Kullanıcı Tanımlı Sahalar sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Parametre Bilgi Girişi Ekranı |  |
| --- | --- |
| Sayısal Saha Başlıkları (1,2,3,4) | Demirbaş Bilgi Kartları'nda bulunan sahaların dışında tutulması istenen diğer bilgiler için 4 adet 25 karakter uzunluğunda sayısal başlık tanımlanacak sahalardır. Bu bölümde tanımlayacağınız başlıklar Demirbaş Bilgi Kartları'nda Ek Bilgiler bölümüne eklenir ve başlıkların karşılığına bilgi girişi yapılır. Girilen bu bilgilere ait raporlar alınabilir. |
| Alfa Sayısal Saha Başlıkları (1,2,3,4) | Demirbaş Bilgi Kartları'nda bulunan sahaların dışında tutulması istenen diğer bilgiler için 4 adet 25 karakter uzunluğunda alfa nümerik başlık tanımlanacak sahalardır. Bu bölümde tanımlayacağınız başlıklar Demirbaş Bilgi Kartları'nda Ek Bilgiler bölümüne eklenir ve başlıkların karşılığına bilgi girişi yapılır. Girilen bu bilgilere ait raporlar alınabilecektir. |
