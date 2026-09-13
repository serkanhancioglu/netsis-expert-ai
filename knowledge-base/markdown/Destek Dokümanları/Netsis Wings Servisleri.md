---
title: "Netsis Wings Servisleri"
page_id: "50679806"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis Wings Servisleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis Wings Servisleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPThmYTE5YTRlLWNhZWMtNGM0Yy04MTlmLTkyZDY2MTdhYzA0NyZsaW5rPWFjNDVkNmE0LTNkMzEtNDQ4YS05YjU5LTVhNzBlMTVhYTkyMiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=8fa19a4e-caec-4c4c-819f-92d6617ac047&link=ac45d6a4-3d31-448a-9b59-5a70e15aa922&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-wings-servisleri_82575792_50679806.html"
source_version: "2022-11-03T09:15:27.953+03:00"
source_bytes: 671799
fetched_at: "2026-09-13T04:25:50+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis Wings Servisleri

Netsis Wings Servisleri ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

#### SERVİSLER ve YÖNETİM PANELLERİ

##### Giriş

Bu doküman içerisinde Netsis Wings kurulumu ile gelen Servisler ve bu servislerin yönetim panelleri ile ilgili bilgilendirmeyi bulabilirsiniz.

##### Servisler

Netsis Wings Kurulumu ile aşağıdaki servislerin kurulumu gerçekleştirilmektedir:

- Logo Netsis Wings Servisi (Zorunlu).
- Logo Netsis Wings Broker Servisi (Seçimli).
- Logo Netsis Wings Gateway Servisi (Seçimli).
- Logo Services Agent (Light) (Zorunlu).
- Lisans Servisi (Zorunlu).

##### Logo Netsis Wings Servisi

Logo Netsis Wings Servisi web browser ile uygulama arasındaki iletişimi sağlayan bir HTTPS/Websocket sunucusudur. Windows servis olarak kurulur. Sisteme kaydı yapılan ve konfigüre edilen windows uygulamaların çalıştırılması için bu servisin kurulu ve çalışıyor olması gerekmektedir. Broker ve Gateway servislerinin kurulu olmadığı senaryolarda bütün bağlantıları bu servis karşılar ve cevaplar. Bu senaryo kapsamında gerekli konfigürasyon işlemlerini Ürün kurulum klasörünü altındaki ***VUI\\bin32\\Thinfinity.VirtualUI.Server.exe*** 'yi çalıştırarak ya da ***Netsis Wings Yönetim Paneli*** kısayoluna tıklayarak açabilirsiniz. (Bkz. Logo Netsis Wings Yönetim Paneli.)

##### Logo Netsis Wings Broker Servisi

Scaling ve Load balancing senaryolarında Logo Netsis Wings Gateway servisi ile birlikte çalışır. Uygulanmak istenen Load Balancing senaryosuna göre (Bkz: Scaling and Load Balancing) sunucu instance'larını yöneterek, sunucu instancelarının ayakta olup olmadığını kontrol eder. Aynı networkte bulunduğu ve kendisine tanımlanan gatewaylerden gelen istekleri karşılar ve cevaplar. Bu senaryo kapsamında gerekli konfigürasyon işlemlerini Ürün kurulum klasörünü altındaki
***VUI\\bin32\_*** ***\_Thinfinity.VirtualUI.Broker.exe*** 'yi çalıştırarak açabilirisiniz.

##### Logo Netsis Wings Gateway Servisi

Load balancing senaryolarında en az bir Logo Netsis Wings Gateway servisinin olması gerekmektedir. Logo Netsis Wings Broker servisi ile birlikte çalışır. Gelen bağlantıların ayakta olan sunuculara dağıtılması işlerini gerçekleştirir. Bu senaryo kapsamında gerekli konfigürasyon işlemlerini Ürün kurulum klasörünü altındaki ***VUI\\bin32\_*** ***\_Thinfinity.VirtualUI.Gateway.exe*** ' yi çalıştırarak açabilirisniz.

##### Logo Services Agent (Light)

Logo Services Agent (Light) bağlanan istemcilerin kayıt çağrılarını kaydeder ve ilk heartbeat çağrılarından itibaren ilgili haberleşme sürelerini kontrol eder, cevap göndermeyen istemci uygulamasını kapatır.
Windows servis olarak çalışır hale geldikten sonra NAMEDPIPE üzerinden haberleşme kanalını dinler ve kendisine bağlanan istemcinin timeout süresi ile kaydını yapar. İlgili istemcinin gönderdiği ilk heartbeat çağrısından itibaren geçen süreyi hesaplar ve beklenen sürede kendisine yeni bir heartbeat çağrısı gelmemesi durumunda, kayıt olan istemci uygulamasını kapatır.
Netsis Wings kurulumunda ürün exe sini dinleyerek (Örnek: "**wingsweb.exe**") ürün exe'sinden timeout süresi boyunca cevap gelmemesi durumunda ürün exe'sini kapatır. Timeout süresi "VUI\\bin32\\Logo.Web.Client.Registration.exe.Config" dosyasında "**WINGS_TIMEOUT**" parametresi ile set edilir ve varsayılan değeri 300 saniyedir. Log seviyesi .config dosyasında bulunur, varsayılan seviye error olarak tanımlanmıştır, loglarını Event Log tarafınada varsayılan olarak Servis İzleyisi EventLogSource adı ile loglarını kaydeder.

#### Yönetim Panelleri

##### Netsis Wings Yönetim Paneli

Netsis Wings Yönetim Paneli Logo Netsis Wings Servisinin kurulduğu durumlarda gerekli olan konfigürasyon ayarlarını düzenlemek için kullanılan arayüzdür. Kurulum ile birlikte uygulamanın açılması için gerekli olan konfigürasyon bilgileri ayarlanmış olmakla birlikte herhangi bir sorun durumunda bu arayüz kullanılarak düzenlemeler yapılabilir.
**Apply** : Bu buton ile yapılan değişiklikler kaydedilir.
**Close** : Bu buton ile Yönetim paneli ekranı kapatılır.
**Show** **Log** : Bu buton ile servis tarafından basılan loglar listelenir.

##### General Tabı

![](../_assets/9bfaca9017b07be9fc03.png)**Şekil** **1**: Netsis Wings Yönetim Paneli Genel Tabı
Şekil 1 ile gösterilen Yönetim Paneli Genel tabında windows servisin durumunu takip edebilirsiniz (Kırmızı kutu içerisine alınan alan). Servisin ayakta olmaması durumunda görüntü üzerindeki metnin "Windows service not running" ![](../_assets/99775e8741c166305c10.png) şekline dönüştüğünü göreceksiniz bu durumda Logo Netsis Wings Servisinin çalışır durumda olduğunu kontrol etmeniz gerekmektedir.
Communication Settings alanında aşağıdaki değerlerin girilmesi beklenmektedir:

| Tanım | Açıklama |
| --- | --- |
| Bind to IP | "All unassigned" seçeneği ile bütün mevcut IP adresleri ile gelen bağlantıların servis tarafından karşılanmasını sağlar. Özel bir IP adresi girilir ise sadece bu IP adresi üzerinden gelen istekler cevaplanır. |
| Protocol | Http ve Https protokolleri arasında yapılan tercih bu kısımda belirtilir. Varsayılan olarak Http portu üzerinden yayın yapılmaktadır. |
| ![](../_assets/5df21911d416ef888047.png) Uyarı | Protocol bilgisinin yanında yer alan bu buton ile Http varsayılan hatalarının yönlendirileceği hata sayfalarının değiştirilebileceği Hata Sayfası ekranına geçiş yapılır. (Bkz. Hata Sayfası Ekranı) |
| ![](../_assets/ba742ec3d43cdc7dfc97.png) SSL Sertifikası | Protocol olarak Https seçildiği durumda görünür. Https için kullanılacak olan SSL sertifikası tanımının yapıldığı SSL Sertifikası ekranını açar. (Bkz SSL Sertifikası Ekranı) |
| ![](../_assets/1f555439389baedf5e49.png) Güvenlik Ayarları | Protocol olarak Https seçili olduğu durumlarda ve Broker ve Gateway servislerinin kullanılmadığı senaryolarda kullanılır. Https Güvenlik Ayarları ekranını açar. (Bkz Https Güvenlik Ayarları Ekranı) |
| Port | Logo Netsis Wings Servisinin hangi porttan dinleme yaptığını gösterir. Varsayılan olarak 6580 portundan dinleme gerçekleştirir. |

##### Hata Sayfası Ekranı

General tabında yer alan Uyarı ![](../_assets/5df21911d416ef888047.png) butonuna basarak aşağıdaki ekrana ulaşabilirsiniz.
![](../_assets/feb1fe0f557ff98a5246.png)**Şekil** **2**: Hata Sayfaları Ekranı
Varsayılan olarak ürün kurulumunun altında yer alan "VUI\\web" altındaki hata sayaları kullanılmaktadır.
Listede yer alan alanlar ve tanımları aşağıdaki şekildedir:

| Tanım | Açıklama |
| --- | --- |
| Status Code | Http cevabının durumunu bildiren sayısal kod alanıdır. |
| Path | Hatalı Html cevabı için gösterilecek olan sayfa adresidir. |
| Type | Send file, fiziksel olarak sunucuda bulunan bir sayfanın disk üzerindeki adresi girilerek yapılmış bir tanım olduğunu belirtir.<br>Redirect, yönlendirme yapılacak olan sayfanın URL adresi girilerek yapılmış bir tanım olduğunu belirtir. |

**Edit** : Edit listede seçili olan kaydın güncellenmesi için Özel Hata Sayfası Düzenleme Ekranı açılır. Seçili olan Status Code için yeni sayfa tanımlamak için kullanılır. (Bkz Hata Sayfası Tanımlama Ekranı)
![](../_assets/ec5466a0c69ad56e945f.png)**Şekil** **3**: Hata Sayfası Güncelleme Ekranı
**Add**: Yeni bir hata sayfası tanımı girmek için kullanılır. Mevcut Status Code tanımları için ekleme yapılamaz. (Bkz Hata Sayfası Tanımlama Ekranı)
![](../_assets/89412eee2e0b7329425a.png)**Şekil** **4**: Hata Sayfası Ekleme Ekranı
Mevcut status code tanımları için ekleme yapılmaya çalışıldığında aşağıdaki hata ekranı ile karşılaşılacaktır:
![](../_assets/72ee3ebb30453ffcbba2.png)**Şekil** **5**: Mevcut Status Code Hatası
**Delete** : Seçili olan Hata sayfası tanımını siler.
**OK** : Yapılan değişiklikleri kayıt ederek ekranı kapatır.
**Cancel** : Yapılan değişiklikleri gözardı ederek ekranı kapatır.

##### Hata Sayfası Tanımlama Ekranı

Bu sayfada hata kodları için sayfa tanımlamaları ve güncellemeler yapılır.
![](../_assets/89412eee2e0b7329425a.png)**Şekil** **6**: Hata Sayfası Tanımlama Ekranı
**Status** **Code** : Http cevabının durumunu bildiren sayısal kod alanı.
**File** **Path** : Fiziksel bir sayfa tanımlanacağı zaman aktif hale gelir ve disk üzerinden fiziksel sayfanın seçilmesini sağlar. Hata sayfası tanımının tipi **send** **file** olur.
**Absolute** **URL** : Başka bir Url e yönlendirme yapılacağı zaman ilgili Url bilgisinin girilmesini sağlar. Hata sayfası tanımının tipi **Redirect** olur.
**OK** : Yapılan değişiklikleri kayıt ederek ekranı kapatır.
**Cancel** : Yapılan değişiklikleri gözardı ederek ekranı kapatır.

##### SSL Sertifikası Ekranı

General tabında Protocol olarak Https seçildiği durumda SSL Sertifkası ![](../_assets/ba742ec3d43cdc7dfc97.png) butonuna basarak bu ekrana ulaşabilirsiniz. Varsayılan olarak Thinfinitity VirtualUI sertifikası ürün kurulumu ile birlikte gelmektedir. Bu sertifikayı ürün kurulumunda **"VUI\\cert\\"** klasörü altında bulabilirsiniz. Bu sertifikayı kullanmak istediğiniz zaman aşağıdaki ekran görüntüsü gibi bilgileri doldurup kaydetmeniz yeterli olacaktır.
![](../_assets/01d92ec1bc91f9807b9c.png)**Şekil** **7**: SSL Sertifikası Ekranı
Kendi Sertifikanızı tanımlamak için bu ekranda aşağıdaki bilgileri girmeniz gerekmektedir:

| Manage SSL Certificate |  |
| --- | --- |
| Certificate File | Sertifika dosyasının adresi. |
| CA File | Tanımsız bir sertifika otoritesi tarafından yayımlanmış sertifikalar için CA sertifikasının<br>adresi girilmelidir. |
| Private Key | Sertifika Private Key adresi. |
| PassPhrase | Private Key oluşturulurken şifre kullanılmış ise bu şifre bilgisi bu alana girilmelidir. |

##### Create a self-signed certificate

Self Signed bir sertifika oluşturup bu sertifikayı kullanmak istiyorsanız Create a self-signed certificate butonuna tıklayarak açılan ekranda aşağıdaki bilgileri girmeniz gerekmektedir. Geçerli bir sertifika otoristesi olmayacağı için browser tarafından uyarı verilir.
![](../_assets/a8fc5d41e51c73f3d9c2.png)**Şekil** **8**: Create Self Signed Certificate Ekranı

| Create Self Signed Certificate |  |
| --- | --- |
| Country Code | ISO 3166 standartlarındaki iki karakterlik ülke kodu. |
| State | Organizasyonun bulunduğu İl adı (kısaltılmamış tam isim). |
| Locality | Organizasyonun bulunduğu semt (Kısaltılmamış tam isim). |
| Organization | Firmanın resmi unvanı. |
| Organizational Unit | Organizasyon içindeki farklı birimleri ayırmak için kullanılır. |
| Common Name | Sertifikayı kullanmayı düşündüğünüz sunucu ve domain adı<br>(wings.logo.com.tr) ya da Url bilgisi. |
| E-Mail Address | Firma eposta adresi. |
| Bits | 2048 büyüklüğünde anahtar kullanılması tavsiye edilir. |

Gerekli bilgiler tanımlandıktan sonra **Create** butonuna basılarak sertifikanın kaydedileği klasörü seçmemiz istenecek. Varsayılan klasör olarak "**VUI\\Cert"** klasörü açılır. Bu işlem başarılı bir şekilde yapıldıktan sonra artık bu sertifika kullanılıyor olacak. **Close** butonu ile işlemi kaydetmeden ekranı kapatabilirsiniz.

##### Create a Certificate Request

Create a Certificate Request, geçerli bir sertifika otoritesinden (VeriSign vs.) sertifika almak için kullanılır.
![](../_assets/7eee4857b83db4c9e5c6.png)**Şekil** **9**: Create a Certificate Request Ekranı

| Create a Certificate Request |  |
| --- | --- |
| **Country** **Code** | ISO 3166 standartlarındaki iki karakterlik ülke kodu. |
| **State** | Organizasyonun bulunduğu İl adı (kısaltılmamış tam isim). |
| **Locality** | Organizasyonun bulunduğu semt (Kısaltılmamış tam isim). |
| **Organization** | Firmanın resmi unvanı. |
| **Organizational** **Unit** | Organizasyon içindeki farklı birimleri ayırmak için kullanılır. |
| **Common** **Name** | Sertifikayı kullanmayı düşündüğünüz sunucu ve domain adı (wings.logo.com.tr) ya da Url bilgisi. |
| **E-Mail** **Address** | Firma eposta adresi. |
| **Bits** | 2048 büyüklüğünde anahtar kullanılması tavsiye edilir. |

Gerekli bilgiler tanımlandıktan sonra **Create** butonuna basılınca sistem iki dosya üretecektir. Öncelikle Private Key dosyasını bir klasöre kaydetmeniz istenecek, sonrasındada istek dosyasını bir klasöre kaydetmeniz istenecek. Oluşturulan istek dosyasını Sertifika otoritesine göndererek sertifika temini sağlanır. Bu dosyalar Sertifika tanımlama ekranından tanımlanarak bu sertifikaların kullanılması sağlanır.
**Close** butonu ile işlemi kaydetmeden ekranı kapatabilirsiniz.

##### Https Güvenlik Ayarları Ekranı

![](../_assets/7fac1ac4a5255573272c.png) General tabında Protocol olarak Https seçildiği ve Broker ve Gateway servislerinin kullanılmadığı senaryolarda Güvenlik Ayarları butonuna basarak aşağıdaki ekrana ulaşabilirsiniz:
![](../_assets/665b61d8263a1c090eba.png)**Şekil** **10**: Https Güvenlik Ayarları Ekranı

| HTTPS-Security Settings |  |
| --- | --- |
| Encryption Methods | Desteklenmesini istediğiniz Https encryption metodları seçebilirsiniz. |
| Default | Varsayılan Encryption metodu işaretlenir, varsayılan encryption metodunun desteklenmediği browserlarda diğer encryption metodlarına bakılır. |

##### RDS Tabı

Uygulamalar interactive kullanıcı heabı altında çalıştırılır, eğer kurulum yapılan sunucu üzerinde interactive kullanıcı yok ise uygulamalar açılmaz. Remote Desktop ile session açılan bir sunucuda uygulamaları çalıştırabilmek için RDS tabında bu alanın doldurulması gerekmektedir.
![](../_assets/c96212fad7055ddc2e89.png)**Şekil** **11**: RDS Tabı

| Tanım | Açıklama |
| --- | --- |
| Use this account for the Remote<br>Desktop Services session | Uygulamaların girilen Remote Desktop Service sessionı altında çalışması sağlanır. |
| Username | Remote Desktop Service sessionı kullanıcı adı. |
| Password | Remote Desktop Service sessionı kullanıcı şifresi. |
| Test | Girilen kullanıcı bilgilerini kontrol eder. |

##### Applications Tabı

Applications sekmesi, çalıştırılacak olan uygulama tanımlarının yapıldığı alandır. Bu tanımlama ile uygulama web sunucunda yayınlanmaya başlayacaktır. Yayımlanan uygulamaya erişmek için girmiş olduğunuz uygulama bilgilerine göre aşağıdaki URL formatını web browserında yazmak yeterli olacaktır. http:\\\\\\{local-ip}:{port} {virtualpath} Örnek : http:\\\\localhost:6580\\Wings
![](../_assets/a707779a16aa822a1d6d.png)**Şekil** **12**: Application Tabı

| Tanım | Açıklama |
| --- | --- |
| Application List | Tanımlanmış olan uygulamaların listesini gösterir. Sağ tarafta yer alan checkbox seçimi ile uygulama aktif pasif yapılabilir.<br>Name; Uygulamanın Adı, Target ise uygulamanın çalıştırılabilir dosyası (WebLink tipindeki uygulamalar için web adresi). |
| Add | Yeni uygulama ekleme ekranını açar. (bkz: Uygulama Detay Ekranı) |
| Edit | Seçili olan uygulama tanımının güncellenmesini sağlar. (bkz: Uygulama Detay Ekranı) |
| Allowed Users and Groups for selected profile | Seçili uygulama için yetkili olan kullanıcı ve grupları gösterir. |
| Database path | Uygulama için servis tarafından kullanılan veritabanı bilgilerinin tutulacağı klasör. |

##### Uygulama Detay Ekranı

Uygulama ekleme yada güncelleme işlemleri bu ekran üzerinden gerçekleştirilir.
![](../_assets/2d06ae38910a03b6cba9.png)**Şekil** **13**: Uygulama Detay Ekranı

| Tanım | Açıklama |
| --- | --- |
| Name | Uygulama Adı |
| Virtual Path | Her uygulama için tekil bir adres oluşturabilmek için bu değer kullanılır, daha önce kullanılmamış bir değer olması gerekir. Uygulama erişim adresine eklenir. Ör : [http://localhost/**Wings**](http://localhost/Wings) |
| Home Page | Karşılama Sayfa Adresi (Netsis Wings için ürün altında yer alan web klasöründeki index.html seçilmelidir.) |
| Access Key | Uygulama için yaratılan tekil değer (Id bilgisi) |
| Icon | Uygulama için icon seçme alanıdır, seçilen icon birden fazla uygulama olduğunda uygulama adresi girilmeden ([http://localhost:6580](http://localhost:6580)) açıldığında karşımıza çıkacak olan uygulama listesinde uygulama tanımın<br>göstermede kullanılcaktır. |
| Application/Web Link | Web Link seçildiğinde bu uygulama Web Hyperlink olarak davranacaktır, Netsis Wings için Application seçimi yapılmalıdır. |
| Default Application | Varsayılan uygulama olarak seçilen uygulama, uygulama adı URL'de girilmeden de ulaşılabilir olacaktır (http://localhost:6580 ile Netsis Wings uygulaması açılabilir olacaktır.) |

##### General Tabı

![](../_assets/fd84684d042354b390dd.png)

**Şekil** **14:** Uygulama Detay Ekranı-General Tabı

| Tanım | Açıklama |
| --- | --- |
| Program path and file name | Uygulamanın çalıştırılabilir(exe) dosyasının tam adresi. |
| Arguments | Uygulamaya gönderilecek olan parametre değeri/değerleri. |
| Start in the following folder | İçerik klasörü. |
| Resolution | Seçili olan listeden uygun çözünürlük ayarı seçilebilir. Netsis Wings için kullanılan varsayılan değer Fit To Browser window. |
| Browser rules file | Remote Desktop çözünürlük ayarlarını tanımlayan dosyanın adresi |
| Idle Timeout | Uygulama kapatıldıktan sonra exe dosyasının ne kadar sonra kill edileceğini gösterir. Bu süre zarfında uygulama session bilgisi açık kalır. 0 verilmesi durumunda uygulama kapatılır kapatılmaz exe<br>öldürülür. |

##### Credentials Tabı

Credentials sekmesi, uygulamanın hangi interaktif kullanıcı hesabı altında çalışacağını belirler.
![](../_assets/b7d33d1d4f1301b679a1.png)**Şekil** **15**: Uygulama Detay Ekranı-Credentials Tabı

| Tanım | Açıklama |
| --- | --- |
| Use the Authenticated Credentials | Permissions tabında tanımlanan kullanıcılar arasından browserda girilen kullanıcı bilgisini kullanmak için bu seçenek işaretlenir. Kullanıcı bağlı değilse bağlantı sağlanır. |
| Use these credentials | Bilgileri girilen kullanıcı hesabı ile bilgisayara bağlanılır ve uygulama çalıştırılır. |

##### Permissions Tabı

![](../_assets/5889a94c344f14b306e6.png)**Şekil** **16**: Uygulama Detay Ekranı-Permissions Tabı Bu uygulamaya erişebilecek olan kullanıcı listesi.

| Tanım | Açıklama |
| --- | --- |
| Allow ananymous access | Herhangi bir login işlemi olmadan uygulamanın çalışmasını sağlar. Yani herkese açık olur. |
| Add | Allow ananoymous access seçili değil ise uygulamaya login olup kullanabilecek olan yetkili kullanıcıları seçmemizi sağlar. |
| Remove | Daha önce eklenmiş olan bir hesabın yetkisin kaldırmamızı sağlar. |

##### Authentication Tabı

Authenticatication, Authentication yönteminin belirlendiği alandır.

![](../_assets/a505ea938fed708852df.png) **Şekil** **17**: Authentication Tabı-Methods Tabı

| Tanım | Açıklama |
| --- | --- |
| Authentication Methods | Tanımlı authentication yöntemlerinin listelendiği alandır. Sol taraftaki checkbox ile seçili authentication metodu aktif/pasif yapılabilir.<br>Name, Authentication yönteminin adı.<br>Type, Authentication yönteminin tipi. |
| Add | Yeni bir authentication yöntemi eklemek için kullanılır. Tıklandığında eklenebilecek authentication yöntemleri açılır. |
| Edit | Seçili authentication yöntemini güncellemek için kullanılır. |
| Remove | Seçili authentication yöntemini silmekte kullanılır. |
| Allow anonymous access | İşaretlendiğinde kullanıclar anonymous access olarak tanımlanmış olan uygulamalara erişebilirler. |
| Use standart browser authentication dialog | Seçili olduğunda browserın login dilogu kullanılır seçili değilse Virtual Uı ın web login ekranı kullanılır. |

##### Mappings Tab

Windows logon dışındaki diğer authentication yöntemlerindeki kullanıcıların Windows Acrtive Directory kullanıcıları ile eşleştirilmesini sağlar. Bu eşleştirme ile kullanıcıların uygulamalara erişimleri sağlanır.
![](../_assets/98f42aa20c419da4d765.png)**Şekil** **18**: Authentication Tabı-Methods Tabı

| Tanım | Açıklama |
| --- | --- |
| Switch Base | Authentication Id Mask ve Associated Permission listesinin görünüm sıralarını değiştirir. |
| Authentication Id Mask | Authentication Id Mask listesini gösterir. Authentication Id bilgisi yada bir maskeleme ile kayıt girişi sağlanır.Kullanıcı adının belli karakteri girilerek \* wildcardı kullanılarak maskeleme yapılabilir. |
| Associated Permissions | AuthenticationId mask ile ilişkilendirilen Active Directory Kullanıcı/gruplarını listeler. |
| Enabled | Authentication Id Mask sadece üst tarafta gösterilirken görünür. Seçili authentication Id Mask bilgisini aktif/pasif yapar. |
| Add | Yeni bir Authentication Id mask ya da Active Directory User/group ekleme işlemini yapar. |
| Remove | Üst tarafında yer alan listeden Authentication Id Mask yada Active Directory Kullanıcısı/Grubu silme işlemini gerçekleştirir. |

##### Radius Authentication Yöntemi

Authentication yöntemi olarak Radius seçildiğinde aşağıdaki ekranda bazı tanımlamaların girilmesi gerekmektedir.
![](../_assets/795e168389a708911108.png)**Şekil** **19**: Radius Authentication Method

| Tanım | Açıklama |
| --- | --- |
| Name | Authentication yönteminin adı. |
| Server IP | Radius Sunucu Ip'si. |
| Port | Radius Port. |
| Shared Secret | Radius Shared Secret. |
| Authentication Type | Authentication Tip seçimi yapılır. |
| Test Configuration | Radius sunucusuna bağlanıp test etmek için kullanılır. |

##### Oauth 2.0 Authentication Yöntemi

Oauth 2 Authentication Yöntemi tanımı yapmak için kullanılır.
![](../_assets/fd39db17cbc72cc1f38f.png)**Şekil** **20**: Oauth Authentication Method List
Önden tanımlı Oauth 2 sunucuları için (Google, Facebook, LinkedIn, Dropbox) aşağıdaki ekrandaki bilgileri girmek gerekmektedir.

##### General Tabı

![](../_assets/560b65a03033ccb5a65a.png)**Şekil** **21**: Oauth Authentication Method Tanımı

| Tanım | Açıklama |
| --- | --- |
| Name | Authentication yönteminin adı. |
| Virtual Path | Bu authentication yöntemini kullancak olan uygulamanın virtual path bilgisi. |
| Client ID | Authentication Provider Client Id bilgisi. |
| Client Secret | Authentication Provider Client Secret Bilgisi. |

##### Server Tabı

![](../_assets/7246f3f2f7a74b99abd6.png)**Şekil** **22**: Oauth Authentication Method Tanımı-Server Tabı

| Tanım | Açıklama |
| --- | --- |
| Authorization URL | Authorization isteğinin yapılacağı adres. |
| Authorization Parameters | Authorization Url için extra parametreler. |
| Token Validation Server URL | Token Validation Server URL. |
| Profile Information Server URL | Information Server URL. |
| Login username value in returned JSON | Username bilgisinin döneceği JSON alanının adı. |

##### External DLL Authentication Yöntemi

##### Sadece external dll bilgisinin ayarlanması yeterli olacaktır.
![](../_assets/800b09fa8180773543b1.png)Şekil 23: External Authentication Yöntemi Tanımlama Ekranı

Licenses Tabı

Lisans bilgisinin görüntülendiği ekrandır. Kullanıcın sahip olduğu lisansın durumu gösterilir.
![](../_assets/e7512b175db3a83419e6.png)**Şekil** **24**: Lisans Tabı
**Deactivate**: Mevcut kurulu olan lisans bilgisi sunucudan kaldırılır.
**Register**: Yeni lisans bilgisi tanımlama ekranını açar.
![](../_assets/d8aee3eb9e408ce201f2.png)**Şekil** **25**: Register License Ekranı
Bu ekranda E-Mail adresi alanı Müşteri Numarası Serial alanına üretilen serial key bilgisi girilerek Lisans kaydı gerçekleştirilir.

#### Netsis Wings Broker Yönetim Paneli

Scaling ve Load balancing senaryolarında yapılan kurulumlarda konfigürasyon yönetim işini Netsis Wings Yönetim panelinden devir alır. Ekranlarda Netsis Wings Yönetim Panelindeki tablar ve anlatılan bilgiler aynen geçerli olup RDS tabında çoklu RDS account girme farklılığı vardır. Netsis Wings Yönetim Panelinde olmayan ve scaling ve load balancing senaryolarında gerekli olan Gateways tabı bulunmaktadır.

![](../_assets/d54c73d57d8d332be2cf.png) **Şekil** **26**: Broker Yönetim Paneli- RDS Tabı
Bu alanda mevcut kullanıcı hesaplarını ekleyebileceğiniz gibi işletim sisteminde tanımlı olmayan kullanıcı hesaplarını da ekleyebilirsiniz. İşletim sisteminde olmayan hesaplar otomatik olarak işletim sistemi kullanıcı hesaplarına eklenecektir. Kullanıcı hesapları admin yetkilerine sahip olmalıdır. Bu özelliği kullanabilmek için Servis RD Session Host Role Servisinin yüklü olduğu bir Windows sunucuya kurulu olmalıdır. Tek bir bilgisayardan daha fazla bağlantıya cevap verebilmek için her RDS sessionı farklı uygulama instancelarını işler. (Bkz : Scaling ve Load Balancing)

##### Gateways Tabı

![](../_assets/429290ef8b2953d9e92d.png)**Şekil** **27**: Broker Yönetim Ekranı-Gateways Tabı
Network Id'si eşleşen ve gateway adresi bu alanda tanımlanmış olan gateway lerden gönderilecek olan istekler işlenip sadece bunlara cevap verilir.

##### Netsis Wings Gateway Yönetim Paneli

Netsis Wings Gateway Yönetim Paneli load balancing senaryolarında kullanılacak olan Logo Netsis Wings Gateway Servisinin yönetim panelidir. Gateway konfigürasyon ayarları bu panel üzerinden gerçekleştirilmektedir. Tasarlanan sistemde bir adet Gateway düşünülüyor ise bu kısımda girilecek olan IP ve port bilgileri bizim gateway bağlantı bilgilerimiz olacaktır. Eğer birden fazla gateway bulunduran bir mimari işletilecek ise DNS sunucusuna bu IP nin girilerek DNS sunucusunun bağlantıları bu gatewaylere yönlendirilmesi sağlanmalıdır. Aynı zamanda aynı mimari içerisinde yer alan bütün gateway ve broker sunucularının aynı network Id yi paylaşıyor olması gerekmektedir.
**Apply** : Bu buton ile yapılan değişiklikler kaydedilir.
**Close** : Bu buton ile Yönetim paneli ekranı kapatılır.

##### File Menüsü

![](../_assets/8fe5ad695735374c119d.png)**Şekil** **28**: File Menüsü

| Tanım | Açıklama |
| --- | --- |
| Save | Sistem ayarlarında yapılan değişiklikleri kaydeder. |
| Close | Netsis Wings Gateway yönetim panelini kapatır. |

##### Help Menüsü

![](../_assets/6ae7514e3605447263d5.png)**Şekil** **29**: Help Menüsü

##### General Tabı

![](../_assets/9880073e9e1d9af4cb3a.png)Şekil 30: Netsis Wings Gateway Yönetim Paneli
Şekil 1 ile gösterilen Yönetim Paneli Genel tabında windows servisin durumunu takip edebilirsiniz (Kırmızı kutu içerisine alınan alan). Servisin ayakta olmaması durumunda Logo Netsis Wings Gateway Servisinin çalışır durumda olduğunu kontrol etmeniz gerekmektedir.
Communication Settings alanında aşağıdaki değerlerin girilmesi beklenmektedir:

| Tanım | Açıklama |
| --- | --- |
| Bind to IP | "All unassigned" seçeneği ile bütün mevcut IP adresleri ile gelen bağlantıların servis tarafından karşılanmasını sağlar. Özel bir IP adresi girilir ise sadece bu IP adresi üzerinden gelen istekler cevaplanır. |
| Protocol | Http ve Https protokolleri arasında yapılan tercih bu kısımda belirtilir. Varsayılan olarak Http portu üzerinden yayın yapılmaktadır. |
| ![](../_assets/5df21911d416ef888047.png) Uyarı | Protocol bilgisinin yanında yer alan bu buton ile Http varsayılan hatalarının<br>yönlendirileceği hata sayfalarının değiştirilebileceği Hata Sayfası ekranına geçiş yapılır. (Bkz. Hata Sayfası Ekranı) |
| ![](../_assets/ba742ec3d43cdc7dfc97.png) SSL Sertifikası | Protocol olarak Https seçildiği durumda görünür. Https için kullanılacak olan SSL sertifikası tanımının yapıldığı SSL Sertifikası ekranını açar. (Bkz SSL Sertifikası Ekranı) |
| Port | Logo Netsis Wings Gateway Servisinin hangi porttan dinleme yaptığını gösterir. Varsayılan olarak 6580 portundan dinleme gerçekleştirir. |
| Network Id | İlgili Logo Netsis Wings Gateway kurulumunu tanımlar. (Id bilgisi). Kaynaklarını bu gateway ile paylaşmak isteyen Netsis Wings Broker kurulumları bu Network Id bilgisini tanımlamalıdırlar. Varsayılan olarak restgele bir string değer atanır, daha tanımlayıcı bir değerle değiştirilebilir.<br>![](../_assets/4543ed3c947cc6fc94cc.png) |

##### Scaling and Load Balancing

Tek Sunucu Çoklu Hesap: Tek bir sunucu üzerinde Çoklu RDS Hesapları ile farklı sunucu instanceları oluşturularak, farklı uygulama instancelarının ayrı ayrı sunucu instanceları tarafından ele alınması sağlanabilir.
Oluşturulan bu sunucu instanceları Logo Netsis Wings Broker Servis tarafından yönetilir, instanceın sağlıklı bir şekilde çalışır durumda olduğu kontrollerini yaparak, uygulama instancelarının sunucu instancelarına dağıtılması işini Logo Netsis Wings Gateway Servis ile birlikte çalışarak halleder.
![](../_assets/ebdac8e7d9282dfe845a.png)**Şekil** **31**: Tek Sunucu Çoklu Hesap Senaryosu

##### Çoklu Sunucu ile Load Balancing

Bu senaryoda tek bir Logo Netsis Wings Gateway Servisi bağlantıları farklı sunuculara dağıtır.
![](../_assets/db29b59766e1e619b5c4.png)**Şekil** **32**: Çoklu Sunucu ile Load Balancing Senaryosu

##### Çoklu Gateway ve Sunucu ile Load Balancing

Çoklu Gateway ve Sunucu il Load Balancing senaryosunda dış kaynaklı bir DNS sunucusu farklı Gateway servislerine load balancing yapar.

![](../_assets/a5bedce0f6837fe808c5.png)**Şekil** **33**: Çoklu Gateway ve Sunucu ile Load Balancing Senaryosu

##### Çoklu RDS Hesabı ve Çoklu Sunucu ile Load Balancing

Çoklu RDS Hesabı ve Çoklu Sunucu ile Load Balancing senaryosu Tek Sunucu Çoklu Hesap senaryosu ve Çoklu sunucu ile Load balancing senaryolarının birleştirilerek kullanılması ile gerçekleştirilir.
