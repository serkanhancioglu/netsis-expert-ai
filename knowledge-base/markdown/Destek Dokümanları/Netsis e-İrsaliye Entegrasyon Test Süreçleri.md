---
title: "Netsis e-İrsaliye Entegrasyon Test Süreçleri"
page_id: "50671945"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis e-İrsaliye Entegrasyon Test Süreçleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis e-İrsaliye Entegrasyon Test Süreçleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWQ3NjQ2NTM1LTMyZDktNDlkZS1iMGU3LTgyOGMzZDIxNjI5NyZsaW5rPWEwNjkwZjgxLTA3YWYtNGRmNi1hMjkzLTQ1YmU4NTAzYThjNyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=d7646535-32d9-49de-b0e7-828c3d216297&link=a0690f81-07af-4df6-a293-45be8503a8c7&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-e-irsaliye-entegrasyon-test-surecleri_50672083_50671945.html"
source_version: "2022-11-03T08:58:39.293+03:00"
source_bytes: 8369332
fetched_at: "2026-09-13T04:25:33+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis e-İrsaliye Entegrasyon Test Süreçleri

Netsis e-İrsaliye Entegrasyon Test Süreçleri ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Netsis e-İrsaliye Entegrasyon test Süreçleri dokümanı; Entegrasyon lisansına (Online e-İrsaliye) sahip, Entegrasyon çalışmalarına başlayacağı Başkanlık tarafından kendisine bildirilen ve hali hazırda e-Fatura uygulamasını kullanan, mali mühürleri kendilerine ulaşan mükelleflerin, e-İrsaliye test çalışmalarını açıklamak amacıyla hazırlanmıştır.

Gerekli ön hazırlıklar ve entegrasyon testleri için aşağıdaki sıranın takip edilmesi gerekir:

- e-İrsaliye uygulamasından yararlanmak isteyen mükelleflerin öncelikle e-Fatura kullanıcısı olması gerekir.
- Netsis programının e-İrsaliye uygulamasında kullanılan yöntem, e-Fatura uygulamasında kullanılan yöntemle aynı olmak zorundadır.

Gelir İdaresi'nin yayınladığı e-İrsaliye başvuru dokümanı, kullanılan yönteme göre başvuru süreçleri hakkında kısa bilgiler içerir.

> [!NOTE]
> Detaylı bilgi için [tıklayınız](https://ebelge.gib.gov.tr/dosyalar/kilavuzlar/E-irsaliyeUygulamasiBasvuruRehberiveKilavuzu_V1.pdf).

#### Başkanlığa e-İrsaliye Entegrasyon Yöntemi Başvurusu

e-Fatura uygulamasında hali hazırda entegrasyon yöntemini kullanan mükelleflerin, e-İrsaliye uygulamasına dahil olmak için Başkanlığa hitaben bir dilekçe ve ekinde yer alan test tanım formu ile başvurması gerekir.

> [!NOTE]
> Test Tanım Formu için [tıklayınız](https://test.efatura.gov.tr/entegrasyonbasvuru/BasvuruWS_SSL.jsp).

Test Tanım Formu, uygulamanın test ortamına bağlantı kuracağı sunucu ve istemci IP adresleri ile web servis uç noktalarının belirtildiği formdur. Test tanım formunda yer alan IP numaraları ile canlı ortamda kullanılan IP numaralarının farklı olması gerekir.

![](../_assets/698319ecfd21e0047535.png)

Entegrasyon çalışmalarına başlayacağı bilgisi Başkanlık tarafından kendisine bildirilen kullanıcılar, kendi bilgi işlem sistemleri aracılığı ile e-İrsaliye gönderip almaları için öncelikle sistemlerinde gerekli altyapıyı oluşturmaları gerekir. Bu nedenle kullanıcıların, [www.ebelge.gov.tr](http://www.ebelge.gov.tr/) adresinde yer alan teknik kılavuzlarda, açıklanan servislere ve altyapıya yönelik hazırlıklarını tamamladıktan sonra entegrasyon çalışmalarına başlaması gerekir. Başvurusu uygun bulunan mükelleflerin entegrasyon testlerinde kullanacakları test hesapları Başkanlık tarafından tanımlanır ve mükellefe e-Posta ile bildirilir. Gelir idaresinin açıkladığı test adımlarının detaylı açıklaması için [tıklayınız](https://ebelge.gib.gov.tr/dosyalar/kilavuzlar/e-FaturaTestPlani.pdf). Dokümanın ilk 4 bölümü, ön hazırlık ve erişim testleri hakkında bilgi verir. 8'inci bölümde ise, Netsis uygulamasında yapılması gereken e-İrsaliye test adımları ile ilgili bilgiler bulunur.

> [!WARNING]
> Test adımlarına geçilmeden önce hem Netsis Web servisinin kurulu olduğu makinede, hem de faturaları mühürleyip gönderme işlemini yapan Netsis istemci makinesinde, aşağıdaki adrese girilip sayfanın açılıp açılmadığı kontrol edilmesi gerekir. Kontrol edilecek adres için [tıklayınız](https://merkeztest.efatura.gov.tr/EFaturaMerkez/services/EFatura?wsdl). Bu link, her iki makineden de açıldığında aşağıdaki gibi bir sayfa ekrana gelmiyorsa, bu durumda test tanım formlarında belirtilen IP ve servis uç noktası adresleri için GİB tarafında gerekli kontrollerin yapılması ve gerekli düzeltmelerin sağlanması gerekir. Sayfa her iki makineden de düzgün bir şekilde açılıyorsa test adımlarına başlanabilir.

![](../_assets/d7ece78902d2c32a0171.png)

#### Gönderici Birim, Merkez ve Posta Kutusu Rolleri

e-Fatura ve e-İrsaliye Uygulamasında **Gönderici Birim**, **Merkez ve Posta Kutusu** olmak üzere 3 temel rol bulunur. Bu rollerden **Gönderici Birim;** e-Fatura ve e-İrsaliye'yi göndermeyi**, Posta Kutusu;** e-Fatura ve e-İrsaliye'yi almayı, **Merkez** ise; Posta Kutusu ile Gönderici Birim arasındaki iletişimi sağlar. Bu amaçla e-Fatura ve e-İrsaliye Uygulamasına entegre olmak isteyen kurumlar için, Gelir İdaresi Başkanlığı tarafından iki adet kullanıcı açılır. Birisi Başkanlık bünyesinde bulunan **Portal Kullanıcısı**, diğeri ise firmanın bilgi işlem sistemi ile entegre çalışan (Firmanın kendisini ifade eden) **Entegrasyon Kullanıcısı**'dır. Entegrasyon testleri kontrol edilirken bu iki kullanıcı arasındaki irsaliyeler dikkate alınır. Entegrasyon çalışmalarına başlanacağı bilgisi kendisine bildirilen kuruma, bu iki kullanıcıya ait bilgiler Gelir İdaresi Başkanlığı tarafından iletilir. Bu aşamadan sonra e-İrsaliye testlerine başlanır.

#### Gelir İdaresi Başkanlığı Test Portalı'na Giriş

Entegrasyon başvurusu onaylandığında Gelir İdaresi Başkanlığı ilgili mükellef için, test amaçlı bir kullanıcı yaratır. Aşağıdaki örnekte görüldüğü gibi Gelir İdaresi Başkanlığı tarafından test kullanıcı bilgileri ve portal şifre bilgileri iletilir.![](../_assets/b934e3e73e065356e716.png)

Bu kullanıcı ile, [Gelir İdaresi Test Portalı'na](https://gbpktest.efatura.gov.tr/efatura/) giriş yapılır.

![](../_assets/841eb78b96361c22ee6a.png)

Gelir İdaresi Başkanlığı Test Portalı'na giriş yapıldıktan sonra portal üzerinden irsaliye göndermek ve almak için, Test Araçları → Araçlar → Kullanıcı Bilgileri →"**e-İrsaliye Kullanmak İstiyorum**" seçeneğinin seçilmesi gerekir. ![](../_assets/41a4dcba591de13c5d39.png)

Netsis İçinde e-İrsaliye Test Adımları şunlardır:

- Kullanıcı bilgisinin Netsis veritabanı altında TBLEIRSCARI Tablosu'na ve e-İrsaliye Mükellefleri Listesi'ne manuel (elle) eklenmesi gerekir.

Örnek SQL cümlesi aşağıdadır:

INSERT INTO NETSIS..TBLEFIRSCARI(IDENTIFIER,ALIAS,TITLE,EFATTYPE,TARIH,PROFILEID,AKTIF) VALUES ('1111111000','urn:mail:defaultpk@logo.com.tr','LOGO TEST IRSALIYE','OZEL','2020-01-01','0','E')

- Bu işlemden sonra test kullanıcısının vergi numarasıyla Netsis Fatura modülünden Satış İrsaliyesi oluşturmak için, Cari Hesap, Unvan, Adres ve Vergi Numarası bilgilerinin tanımlanması gerekir.

![](../_assets/4ad973f4d6b4592b65ad.png)

- e-Fatura Parametreleri ekranından "e-İrsaliye Kullanılsın" parametresinin seçilmesi ve e-İrsaliye belgesi için üç karakterden oluşan Belge Birim Kodu bilgisinin girilmesi gerekir.

![](../_assets/1c06f26bcdc161257296.png)

#### Gönderici Birim Çalışma Testleri

Fatura Modülü'nden yukarıda tanımlanan test cari hesabına satış irsaliyesi kesilip, "Toplu e-İrsaliye Oluşturma" ekranında taslak oluşturulup, "Gönder" butonu ile şema ve schematron kontrolünden geçirilen, onaylı e-İrsaliye içeren ve GİB Test Portalı'nda giriş yapılan test, kullanıcı hesabına gönderilir.

![](../_assets/8726c81dd6d6e3905290.png)![](../_assets/c7af97ec3ac5b227c081.png)

Bu işlem sonucunda, Netsis Fatura Modülü'nde e-İrsaliye İşlemleri → e-İrsaliye Giden Kutusu → Zarf Bazında Giden/İrsaliye Bazında Giden ekranlarında, gönderilen e-İrsaliye ve Zarf izlenir. Giden Kutusu'nda "Sorgula" işleminin mutlaka yapılması gerekir. e-İrsaliye Belgesi'ni ve Zarf'ını aldıklarına dair Gelir İdaresi ve Test Kullanıcı Hesabı'ndan gönderilen sistem yanıtlarının, Netsis programı içinden başarılı bir şekilde alınması gerekir. "Sistem Yanıtları" bölümünde iki adet sistem yanıtının görülmesi gerekir. Giden Kutusu Zarf Listesi kısmında gönderilen zarfın, Durum kolonunda "1300", Açıklama kolonunda ise, "BAŞARIYLA TAMAMLANDI" bilgisinin görülmesi gerekir.![](../_assets/2f89c2cbc4a7dce2c570.png)

Firmanın, Gelir İdaresi Test Portalı'ndaki Posta Kutusu hesabına göndermiş olduğu zarfı, Gelen Kutusu → Zarf Bazında Listeleme ekranından sorgulaması ve Belge Bazında Listeleme ekranından e-İrsaliye'yi görüntülemesi gerekir.

![](../_assets/5a2a1909f2309dcdc494.png) ![](../_assets/e7567da5378f8ea4d3b4.png)

Posta Kutusu Birim Çalışma Testleri aşağıdaki şekildedir:

- Posta Kutusu Testi ile, alış irsaliyesinin uygun bir şekilde alınıp alınmadığı kontrol edilir. Dolayısı ile bu işlemlerin Gelir İdaresi Test Portalı'ndan yapılması gerekir. Bu işleme, Portal'ın "İrsaliye Oluştur" menüsünden irsaliye oluşturularak başlanması gerekir.
- Ekrandan irsaliye kaydedilirken VKN/TCKN alanına mükellefin gerçek vergi numarasının (Netsis → Şirket/Şube Parametre Tanımları → Vergi Kimlik Numarası/T.C. Kimlik Numarası) girilmesi gerekir. Ekrandaki diğer zorunlu alanlar girilerek e-İrsaliye oluşturulur ve gönderilir.

![](../_assets/dc1ff7a7adb530522db5.png)

- Portal'dan gönderilen e-İrsaliye ve Zarf, Netsis Fatura → e-İrsaliye İşlemleri → e-İrsaliye Gelen Kutusu → Zarf Bazında Gelen/İrsaliye Bazında Gelen ekranlarından izlenir. Gelen Kutusu'nda sorgulama işleminin mutlaka yapılması gerekir.
- Gelir İdaresi Test Portalı'ından gönderilen e-İrsaliye ve Zarf; şema, schematron ve mühür kontrolünden geçirilerek, Netsis içine başarılı bir şekilde alınır. Gelen e-İrsaliyenin zarfının Durum kolonunda "**1300**" ve Açıklama kolonunda "**BAŞARI İLE İŞLENDİ**" ifadesinin görülmesi gerekir. Gelen e-İrsaliye ve Zarf'ın mükellef tarafından başarılı bir şekilde alındığına dair sistem yanıtı gönderilir.

![](../_assets/53031311bc3bcf9634f7.png)

- Firma, Gelir İdaresi Test Portal'ının Gönderici Birim Hesabı'ndan, gönderilmiş zarfın durumunu Gelen Kutusu → Posta Kutusu Yanıtları menüsünden ilgili kayda tıklayarak görüntüleyebilir.

![](../_assets/1b229a5756e894a1be67.png)

ISS İçin Eklenmesi Gereken Roles ve Features Listesi, ISS sunucusuna e-Fatura Web Servis Kurulumu İçin İşlem Adımları, SSL Sertifika Yükleme/Binding İşlemi ve e-İrsaliye Sertifika Tanımlama e-Fatura Web Servis Kurulumu Öncesi ISS İçin Eklenmesi Gereken Roles ve Features Listesi Denetim Masası → Program Ekle/Kaldır, Windows Özelliklerini Aç/Kapat kısmından yapılır.

![](../_assets/190a6eddcebad332deb8.png)![](../_assets/cdd62febffbe7a822d7a.png)

![](../_assets/03281d90635230429a10.png) ![](../_assets/a3a371378c30186644db.png)

ISS Sunucusuna e-Fatura Web Servis Kurulumu İçin İşlem Adımları şunlardır:

> [!NOTE]
> Örnek Web Servis uç noktası için [tıklayınız](https://efatura.besice.com.tr/Marti/NetsisEFatura/EfaturaService.asmx?WSDL).

- ISS sunucusunda EfaturaSetup.exe çalıştırılır. Bu işlem sırasında Mali Mühür'ün takılmasına gerek yoktur. İşlem sonrasında varsayılan kurulum gerçekleşir. Kurulum sonrası C:\\inetpub\\wwwroot altında NetsisEFatura klasörü oluşur. ISS üzerinde Default Web Site altında **NetsisEFatura** satırı ve **ApplicationPool** için **NetsisEFatura** adında uygulama havuzu oluşur.

![](../_assets/914f034db557ef521a80.png)
- C:\\inetpub\\wwwroot altında Marti adında bir klasör oluşturulur. Web Servis Kurulumu ile gelen NetsisEFatura klasörü bu dizinin altına taşınır.

![](../_assets/96637348dad9f25b65dd.png)

- NetsisEfatura klasörünün altında bununan Web.config dosyasının içinden ilgili database ayarları yapılır.
- ISS tarafına geçilir. ISS durdurulur. Default Web Site altında oluşan NetsisEFatura üzerinde Advanced Settings ekranında Application Pool olarak **DefaultAppPool** seçilir.
- Physical Path kısmında ise, C:\\inetpub\\wwwroot\\Marti\\NetsisEFatura seçilip kaydedilir.

![](../_assets/16ae01bbe410d88cd1d9.png)

- ApplicationPools'a tıklanır. **NetsisEFaturaPool** ismi değiştirilerek edilerek **MartiPool** yapılır.

![](../_assets/2fc891d8a5d2372c6e5a.png) ![](../_assets/0d1ee74d7ab987acd88a.png)

- Cmd.exe yönetici olarak çalıştırılır. C:\\Windows\\System32\\İnetsrv\> altında aşağıdaki komut çalıştırılarak mevcut NetsisEFatura poolu Marti/NetsisEFatura altında oluşturulur. appcmd set app "Default Web Site/NetsisEFatura" -path:/Marti/NetsisEfatura

![](../_assets/51cd975802395ec91566.png)

- ISS restart edilir.
- Default Web Site altında oluşan Marti klasörü altındaki NetsisEFatura üzerinde, Advanced Settings ekranında Application Pool olarak oluşan **MartiPool** seçilir.

![](../_assets/d951ad4ad7637fe56dc2.png)

- Ardından Marti altındaki NetsisEFatura için Browse denilerek ve Browser'da gelen adresin sonuna EfaturaService.asmx yazılarak erişimin sağlanıp sağlanmadığı kontrol edilir.

![](../_assets/c5868d5f9292efa7bdc2.png)

SSL sertifika yükleme ve Binding İşlemi adımları aşağıdaki şekildedir:

- ISS üzerinde **Server Certificates \> Complete Certificate Request** işlem adımından ilgili sertifika yüklenir.
- **Friendly name** kısmına SSL'in bağlanacağı adres bilgisi yazılır.

![](../_assets/84b46afc5d08751fabbb.png)

- Default Web Site üstünde **Bindings** işlemi ile eklenen SSL sertifikası bağlanır.

![](../_assets/2ee016a25786d1a312b5.png)

- Web Servis uç noktalarına test zarfı gönderilerek kontrol edilir.

**e-İrsaliye Gönderimi İçin Sertifika Tanımlama**

e-İrsaliye Uygulaması, e-Fatura Uygulaması için tanımlanan sertifika ayarlarını kullanır. e-İrsaliye gönderimi için, Netsis'in kurulu olduğu dizinde Servis Klasörü altında EFaturaAyarlar.exe dosyası yönetici olarak çalıştırılıp, Yeni Sertifika Tanımlama ekranı açılır.

> [!NOTE]
> Tanımlama sırasında Mali Mühür'ün makineye takılı olması gerekir.

> [!NOTE]
> e-İrsaliye Test Süresi boyunca "Test Kullanımı" parametresinin işaretli olması gerekir.
>
> ![](../_assets/033efb79d362b716c441.png)
