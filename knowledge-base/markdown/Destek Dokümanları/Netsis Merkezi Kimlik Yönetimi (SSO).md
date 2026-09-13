---
title: "Netsis Merkezi Kimlik Yönetimi (SSO)"
page_id: "50680080"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis Merkezi Kimlik Yönetimi (SSO)"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis Merkezi Kimlik Yönetimi (SSO)"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTE1ZjYwMDE4LWMxYmItNDZlYy1hMzcyLWY1ZmU0NWQ0ODZjNiZsaW5rPWNmZmVkODcyLWU2ZGUtNDM3MS05NTU1LTJiZDBiNTZhZTAyMSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=15f60018-c1bb-46ec-a372-f5fe45d486c6&link=cffed872-e6de-4371-9555-2bd0b56ae021&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-merkezi-kimlik-yonetimi-sso_80085323_50680080.html"
source_version: "2022-12-19T14:37:59.620+03:00"
source_bytes: 1047174
fetched_at: "2026-09-13T04:26:25+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis Merkezi Kimlik Yönetimi (SSO)

Netsis Merkezi Kimlik Yönetimi (SSO) ile ilgili detaylı bilgiye bu dokümandan ulaşabilirsiniz.

Üzerine inşa edildiği platform ve kullandığı teknolojiden bağımsız olarak Web/Windows tüm Netsis uygulamalarının tek bir merkezi kimlik denetimi ve oturum yönetimi ile çalışmasını sağlayan altyapı hizmetidir. Netsis Merkezi Kimlik Yönetimi ile birlikte programda yapılanlar şunlardır:

- Windows/Web ayrımı olmaksızın tüm Netsis uygulamalarına erişecek kullanıcılar için "sadece bir kullanıcı adı/şifre" (SSO kullanıcısı) oluşturulacak ve tüm uygulamalara bu kullanıcı ile erişilecektir.
- Kullanıcı herhangi bir pakete girip oturum açtıktan sonra ve en az bir uygulamada oturumu açık olduğu sürece, diğer paket, şirket, şube bağlantılarında tekrar kullanıcı adı/şifre sorgulanmayacaktır.
- SSO kullanıcılarının Netsis paketlerine şirket-şube ya da geçmiş yıl şirketlerine erişimleri ise, yetki sistemi üzerinden gerçekleştirilecektir.

SSO sisteminin uluslararası standartlardaki kimlik denetim mekanizmalarına bağlı ya da yarı bağlı (hibrid) şekilde kullanım imkanı da bulunmaktadır. Örneğin istenirse, Active Directory kullanan bir işletmede, kullanıcıların domain'deki hesapları ile Netsis uygulamalarına erişimi sağlanabilir. Böylelikle Active Directory'nin sağlayacağı güvenlik politikalarından doğrudan faydalanılabilir. Kullanıcılar Netsis uygulamalarına kullanıcı adı/şifre sorulmaksızın açmış oldukları Windows oturumu üzerinden bağlanabilir.
Bunun yanı sıra Active Directory bağlantısız kullanıcılar için şifre ve oturum yönetimi, windows oturumlarından bağımsız olarak yürütülebilmektedir. Bu kullanıcılar için de istenirse, asgari şifre uzunluğu, karmaşık şifre zorlama, şifre tekrarlama sayısı oturum koruma/kilitleme, giriş sınırlandırma ve benzeri kurumsal güvenlik politikaları uygulanabilmektedir.

**YÖNETİM KONSOLU**

Birçok farklı yönetsel işlevi bünyesinde barındıran Merkezi Kimlik Yönetimi Yönetim Konsolu ile SSO servisine ilişkin kullanıcı yaratma, paket / şirket / şube eşleme, hak belirleme, devre dışı bırakma, şifre sıfırlama gibi yönetsel işlemler yapılabildiği gibi uygulamalara ait lisansların takibi, güncellenmesi, lisans haklarının kullanım durumları gibi yine kullanıcı tabanı ile ilişkilerin yönetimi de aynı ortam içerisinden gerçekleştirilebilmektedir.
Oturum yönetimi kapsamında tüm Netsis uygulamalarına ilişkin açık oturumların istemci makineleri, kullanım yoğunluğu ve kaynak tüketimlerinin merkezi şekilde takip edilmesi ve gerektiğinde istenen oturumun düşürülebilmesi sağlanan fonksiyonellikler arasındadır. Lisans ve Oturum Yönetimi dışındaki diğer Netsis hizmet programlarının çalışma durumlarının izlenmesi ve kapatma-açma gibi işlemler bu konsol üzerinden gerçekleştirilebilir.
Merkezi Kimlik Yönetimi kurulumu tamamlandığında Windows Hizmetler (services) listesinde "Netsis SSO Service" ve web uygulamaları için kurulumu yapıldı ise "Netsis NTF Service" adında iki yeni hizmet programı otomatik çalışacak şekilde hazır bulunur. SSO servisi "Netsis SSO Service" çalışır halde olmadığında hiçbir Netsis uygulamasında kullanıcı girişine izin verilmeyeceğinden bu servisin kapatılmaması gerekmektedir.

Netsis SSO Servisi hem kullanıcı oturum denetimlerini hem de lisans sistemini yönettiği için tüm uygulamalar bu servis ile iletişim kurarak çalışırlar. NetOpenX üzerinden yapılan çağrılar ile NDI ve NDF ile geliştirilen özel uygulamalar da aynı sistem içerisinde çalışacaktır. Benzer şekilde tamamen bağımsız olarak geliştirilen üçüncü parti uygulamaları da bu sisteme entegre olarak aynı yapı içerisinde çalışabilirler.
Merkezi Kimlik Yönetimi uygulaması "İşlemler" menüsünde aşağıdaki seçenekler bulunmaktadır:

- Uygulama Bilgileri.
- Sipariş Bilgileri.
- Kullanıcı Sayıları.
- Kullanıcı
  - Kullanıcı Yaratma.
  - Kullanıcı Eşleme.
  - Kullanıcı Hakları.
  - Grup Tanımları.
  - Kullanıcı / Grup Hak Kopyalama.
  - Kullanıcı Giriş Sınırlandırma.
- Log Bilgileri.
- Bildirim Servisini Yeniden Başlat.
- Ayarlar.
- Hakkında.

### UYGULAMA BİLGİLERİ

![](../_assets/66c0345e73d762a6aa3d.png)

Netsis masaüstü ve web uygulamalarındaki aktif ve kalan kullanıcı sayılarının uygulama bazında grafiksel olarak izlenebileceği ekrandır. Ekran üzerinde paketi belirten grafiklere tıklandığında veya menüdeki "Kullanıcı Sayıları (Detay)" sayfası açıldığında, paketteki aktif kullanıcıların kullandıkları şirket ve sunucu üzerindeki kullandıkları kaynakların kullanım yüzdeleri, aktif kullanıcıların son aktivite tarih/saati, uygulamayı çalıştırdığı bilgisayar adı ve IP adresi hakkında detaylı bilgi alınabilir. Ayrıca aktif kullanıcıların Netsis oturumları da ![](../_assets/1c78466ddf9d7285a247.png) çarpı butonu ile ekran üzerinden sonlandırılabilir.

![](../_assets/39d34fb7e884f0120bab.png)

![](../_assets/dee68ed6b2ff3969569f.png)

### SİPARİŞ BİLGİLERİ

![](../_assets/168ce08431afa35e1806.png)

Uygulamaların kurulumu için gereken lisans bilgilerinin kaydedildiği ve daha önce kaydedilen mevcut lisanslara ait bilgilerin (sürüm, kullanıcı sayıları) izlenebildiği bölümdür.

![](../_assets/477002b53b18489b5640.png)

### LOG BİLGİLERİ

![](../_assets/d05e717d768421740fc7.png)

SSO (Single Sign On) uygulama loglarını görüntülendiği sayfadır. SSO yönetim konsoluna giriş/çıkış hareketleri, başarısız giriş denemeleri, yeni kullanıcı açılması veya mevcut bir kullanıcının silinmesi, kullanıcı eşleştirmeleri ve benzeri işlemler log ekranından işlemin yapıldığı tarih ve saati bilgisi ile görüntülenebilir.

### BİLDİRİM SERVİSİNİ YENİDEN BAŞLAT

Bildirim servisi olan Netsis.Notification.WinService.exe uygulamasının SSO servisinden bağımsız olarak yeniden başlatılmasını sağlayan seçenektir. SSO servisi yeniden başlatıldığında bildirim servisi yeniden başlatılmaktadır fakat bildirim servisini yeniden başlat seçeneği sso servisini etkilememektedir.

*Not: Netsis.Notification.WinService.exe uygulamasının çalışmadığı durumlarda Zamanlanmış Görevler eklentisinin açılışında "Bildirim servisine erişilemiyor. Bildirim servisinin (Netsis.Notification.WinService.exe) çalışır durumda olduğundan emin olunuz." uyarısı alınacaktır. Bu durumda "Bildirim Servisini Yeniden Başlat" işlemi ile servisin çalışması sağlanarak belirtilen uyarının alınmaması sağlanabilir.*

### HAKKINDA

Kurulu SSO uygulamasının versiyon ve yayınlanma tarihi bilgilerinin görüntülenebileceği seçenektedir.

### KULLANICI / KULLANICI YARATMA

![](../_assets/eb0899f18e942df342e3.png)

Yeni kullanıcı tanımlama ve mevcut kullanıcıların bilgilerinde değişiklerinin sağlandığı sayfadır. Yeni kullanıcı oluşturmak için Kullanıcı Adı, şifre ve kullanıcı tipi alanlarının doldurulması zorunludur.

**SSO Admin mi?** Tanımlanan kullanıcının Merkezi Kimlik Yönetimi uygulamasına giriş yapabilmesi için işaretlenmesi gereken seçenektedir.

**Kullanıcı Tipi:** Tanımlanan kullanıcının Standart veya Web uygulamalarına girişi için belirlenmesi gereken seçenektedir. Kullanıcının Wings uygulamalarına girişi için "Web" seçeneği işaretlenmelidir. Aynı kullanıcının Netsis masaüstü ve Wings uygulamasına girişi için "Standart&Web" seçeneği işaretlenmelidir.

**Domain Kullanıcı Adı:** Ayarlar bölümünde "Active Directory Sorgu Ayarları" tanımlı ise, oluşturulan SSO kullanıcısının domain kullanıcısı ile eşleştirilmesi için listeden domain kullanıcı seçiminin yapıldığı alandır.

**e-Posta:** Uygulama içerisinden gönderilecek e-postalar için kullanıcı e-posta bilgisinin tanımlandığı alandır.

**Aktif:** Mevcut bir kullanıcı hesabı silinmeden oturum açmasının engellenmesi için "Aktif" seçeneğinin işareti kaldırılabilir.

Oluşturulan kullanıcı hesabına ait yetki düzenlemeleri yapılmadan önce, kullanıcının giriş yapabileceği Netsis uygulamalarının/şirket-şubelerin belirlenmesi için **Yetkili Uygulamalar** bölümünden tanımlamalar gerçekleştirilmelidir.

**"Yetkili Uygulamalar" s**eçeneği ile ekranda yüklü olan uygulamaların paketleri listelenecek, uygulama seçimi sonrasında şirket ve şubelerin listelendiği ekran açılacaktır. Bu ekran üzerinden yetki tanımı yapılmak istenen şirket/şube veya şirketler/şubeler çoklu seçim yapılarak kaydedilebilir.

### KULLANICI / KULLANICI HAKLARI

![](../_assets/13b009695072f6d6e1b4.png)

Kullanıcı ve gruplara ait hak tanımlarının sağlandığı sayfadır. Kullanıcı hakları tanımlanmak istenen kullanıcı "Sso Kullanıcıları" alanından seçilmelidir. Seçilen kullanıcının haklarının hangi uygulama/şirket/şube için tanımlanacağı belirlenmelidir. Kullancının hangi haklara sahip olacağı ekrandaki modül ve program listesi üzerinden seçim yapılarak belirlenebilir. Kullanıcının admin olarak tanımlanması için "Şirket Admin mi?" parametresi işaretlenmelidir.

*Not: Admin yetkisine sahip kullanıcı uygulama içerisindeki tüm işlemlere tam denetim sahibidir.*

Ekranda seçilen kullanıcının, bir kullanıcı grubına dahil edilmesi için "Grup Kodu" listesinden tanımlanan kullanıcı grubu seçim yapılabilir.

*Not:* *Gruba* *dahil* *edilen* *kullanıcılarda* *hak tanımları* *grup* *haklarından* *alınmaktadır.* *Gruba* *dahil* *edilen* *bir* *kullanıcı için* *kullanıcı* *özelinde* *belirli* *işlem/işlemler* *için* *hak* *tanımı* *yapılmak* *istenirse* *sadece* *ilgili* *işlem* *kullanıcı* *bazında* *hak tanımı* *yapılması* *yeterlidir.* Örn; Şafak kullanıcısı "Muhasebe" grubuna dahildir. Muhasebe grubunun grup haklarında yevmiye kayıtları ekranında silme yetkisi bulunmamaktadır. Gruba bağlı diğer kullanıcılar yevmiye ekranında silme işlemini gerçekleştiremiyor iken Şafak kullanıcısı için kullanıcı haklarında yevmiye kayıtları ekranı için silme yetkisi tanımlanır ise ilgili ekranda silme işlemini gerçekleştirebilecektir.

### KULLANICI / GRUP TANIMLARI

![](../_assets/3c67096ebe5b9c079978.png)

Uygulama/Şirket/Şube bazında yeni kullanıcı grubu oluşturma, mevcut bir kullanıcı grubu için düzenleme ve silme işlemlerinin sağlandığı bölümdür.

Grup tanımı yapıldıktan sonra grup yetkilerinin belirlenmesi için "Kullanıcı Hakları" menüsünden "Grup Hakları" seçilmelidir.

### KULLANICI / KULLANICI / GRUP HAKLARI KOPYALAMA

Seçilen kullanıcı veya grup haklarının, farklı bir kullanıcı veya gruba kopyalanması için kullanılan sayfadır. Hakları kopyalanacak kullanıcı, "Baz Alınacak Kullanıcı/Grup" alanından alanından seçilmeli ve sonrasında tablodan hakların kopyalanacağı kullanıcı/grup seçilmelidir. Hakların kopyalanması için "Seçili Kullanıcılar İçin Baz Alınan Hakları Kopyala" butonu kullanılmalıdır.

![](../_assets/b18bc85b10f8bfba535e.png)

### KULLANICI / KULLANICI GİRİŞ SINIRLANDIRMA

Kullanıcıların programa giriş yapacakları gün ve saatin kısıtlanabileceği bölümdür. Kısıtlama işlemi; kullanıcı, grup veya tüm kullanıcılar için şube bazında yapılabilir.

![](../_assets/7c56e9c1f522cbc96a6e.png)

### KULLANICI / KULLANICI EŞLEŞME

Şirket içerisinde bulunan kullanıcıların eşleşmesinin görüntülendiği, mevcut eşleşme bilgilerinin kaldırılabildiği ve yeni kullanıcı eşleşmelerinin yapılabildiği sayfadır. Ekranın üst bölümünde Netsis uygulamaları ayrı sekmelerde gösterilmektedir.

![](../_assets/f28114f05d651b67ec0d.png)

Ekrandaki tabloda, daha önce şirket/şube için tanımlanmış ancak henüz eşleşmesi bulunmayan veya eşleşmesi kaldırılan kullanıcılar listelenmektedir. Listelenen kayıtlar içerisinde, başlık bilgilerinde bulunan arama ve gruplandırma özellikleri ile filtreleme yapılabilmektedir.

Eşleşmesi yapılmak istenen kullanıcı, listeden seçim yapıldıktan sonra aşağıda bulunan "Sso Kullanıcıları" alanından eşleşmesi yapılacak SSO kullanıcı adı seçilmeli ve "Kullanıcı Eşle" butonu tıklanmalıdır.

Kullanıcı Yaratma ekranından tanımlanan ve Yetkili Uygulamalar bölümünden şirket/şube yetkisi tanımlanan kullanıcılar için eşleşme otomatik sağlanacağından bu ekran üzerinden eşleşmenin yapılmasına gerek bulunmamaktadır.

*Not: Mevcut bir SSO kullanıcısının eşleşmesi var ise silinmesine izin verilmemektedir. Bunun için önce "Kullanıcı Eşleşme" ekranından kullanıcının tüm eşleşmeleri kaldırılmalıdır ve daha sonra silme işlemi yapılmalıdır.*

### LİSANS KOPYALAMA

![](../_assets/cda2fd8e62dfeddf5509.png)
Netsis veri tabanında bulunan lisans bilgilerinin SQL Server'a restore edilen farklı bir Netsis veri tabanına aktarımı için kullanılan işlemdir. Lisans kopyalama işlem adımları aşağıdaki gibidir;

- Mevcut "NETSIS" veri tabanı rename edilmelidir. Örn; "NETSISBACKUP"
- Kontrol edilmek istenen "NETSIS" veri tabanı "NETSIS" adıyla SQL Server'a restore edilir,
- Lisans Kopyalama ekranı açılarak Kaynak Veritabanı alanından "NETSISBACKUP" veri tabanı seçilir ve "Kopyala" butonu ile test edilmek istenen "NETSIS" veritabanına mevcut lisans bilgilerinin aktarımı tamamlanır.

### PENCELER

Merkezi Kimlik Yönetimi uygulamasında açık ekranlara hızlı erişim imkanı sağlayan menüdür.

### AYARLAR

![](../_assets/c15eef2a87126516c273.png)

**Active Directory Sorgu Ayarları**

![](../_assets/c1ebead9d8d2688477c5.png)

Windows Active Directory yapısını kullanan işletmelerde, SSO kullanıcılarının Active Directory kullanıcıları ile eşleştirilmesi için gerekli ayarların sağlandığı bölümdür. Active Directory bağlantısının sağlanması için domain adı, kullanıcı adı ve şifre bilgilerinin girilmesi zorunludur. Tanımlanan kullanıcının Active Directory kullanıcı listesini görüntüleme yetkisine sahip olması yeterlidir. Active Directory yapısında grup ve organizasyonel birim nesneleri sorgu ayarları kullanılabilmektedir.

Örn; Active Directory yapısında Izmir OU (Organizational Unit) altında bulunan Urla organizasyonel birimine ait kullanıcıların getirilmesi için organizasyonel birim sorgu tanımı aşağıdaki gibi kullanılmalıdır.

(ou=Urla,ou=Izmir,dc=abc,dc=com,dc=tr)

### Dil

Merkezi Kimlik Yönetimi (SSO) yönetim konsolunun dil seçeneği Türkçe veya İngilizce olarak belirlenebilir.

### ![](../_assets/ee58031eb762904f5457.png)

### e-Posta

SSO Uygulamasında herhangi bir kullanıcının şifre değişikliğinin kullanıcıya e-posta ile bildirilmesi için kullanılan bölümdür. SMTP kullanıcı adı ve şifre bilgilerinin doldurulması gerekir.

### e-Posta SMTP

Merkezi Kimlik Yönetiminde e-Posta desteğinin kullanılabilmesi için SMTP ayarlarının belirlendiği bölümdür. SMTP sunucu adı, port numarası ve SSL kullanımı bilgileri doldurulmalıdır.

### Netsis Güncelleme Bilgileri

Versiyon güncelleme sonrasında istemci makinelerde otomatik olarak RegKontrol işleminin çalıştırılması için kullanılan bölümdür. Özelliğin kullanılabilmesi için domain admin yetkisine sahip kullanıcı bilgileri tanımlanmalıdır. Versiyon güncelleme sonrasında istemci bilgisayardan uygulamaya giriş sırasında "Sürüm güncellemesi sebebiyle regkontrol işlemi çalıştırılacaktır." alınan uyarı mesajında tamam butonuna tıklandığında otomatik RegKontrol işlemi başlatılacaktır.

### Otomatik Oturum Düşürme

Web uygulamalarında oturum açan kullanıcı, zaman aşımı süresi (dakika) alanında belirlenen süre içerisinde herhangi bir işlem yapmaz ise oturumu düşürülmektedir. Özellik yalnızca web uygulamaları için geçerlidir.

### Şifre Ayarları

SSO Kullanıcılarının şifre politikalarının belirlenmesini sağlayan ayarların bulunduğu bölümdür.
Harf-rakam-özel karakter içerme zorunluluğu, büyük/küçük harf duyarlılığı, minimum şifre uzunluğu, şifre değiştirme gün aralığı, şifre tekrarlanma sayısı politikaları uygulanabilir.

### Veritabanı

Veritabanı sunucusuna erişim için gerekli bilgilerinin bulunduğu bölümdür. SSO kurulumu aşamasında bu bilgiler zorunlu olarak doldurulmaktadır.
