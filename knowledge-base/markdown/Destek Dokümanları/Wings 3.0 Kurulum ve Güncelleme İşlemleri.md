---
title: "Wings 3.0 Kurulum ve Güncelleme İşlemleri"
page_id: "66239171"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Wings 3.0 Kurulum ve Güncelleme İşlemleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Wings 3.0 Kurulum ve Güncelleme İşlemleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWJkMTc4M2Q1LTcxZGMtNGMzNS04MzY1LTA1NTE1NTAyZTQ5NyZsaW5rPWYwNzdjYzA5LTk3OTktNDAyOS1iZjliLTQ3YjkwNjVkZjIyZCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=bd1783d5-71dc-4c35-8365-05515502e497&link=f077cc09-9799-4029-bf9b-47b9065df22d&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "wings-3-0-kurulum-ve-guncelleme-islemleri_66239174_66239171.html"
source_version: "2022-11-02T15:00:22.427+03:00"
source_bytes: 6685008
fetched_at: "2026-09-13T04:24:38+00:00"
generator: "netsis-scraper 1.0.0"
---
# Wings 3.0 Kurulum ve Güncelleme İşlemleri

Wings 3.0 Kurulum ve Güncelleme İşlemleri ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

#### Wings-Thinfinity VirtualUI 3.0

Logo Netsis Wings ürününün alt yapısında kullanılan Thinfinity VirtualUI'ın versiyon geçiş süreçleri tamamlanıp 3.0 versiyonuna güncelleme yapılmış, 9.0.37.0 sürümü ve üzeri tüm Logo Netsis Wings çözümleriyle birlikte kullanıma sunulmuştur.

Kurulum ve Güncelleme Öncesi Hazırlık

Kurulum ve güncelleme işlemleri öncesi Wings uygulamasında kullanılacak "Kullanıcı" için yapılması gereken tanımlar, ayarlar ve yetki düzenlemeleri ile ilgili adımlar aşağıdaki gibidir:

- Wings uygulaması için kullanılacak ayrı bir "Local Admin" kullanıcısı tanımlanmalıdır.

![](../_assets/acc8c5d0740a072ac12b.png)
- Wings kullanıcısı ileride ünün kullanımını olumsuz etkileyip kesintilere neden olmaması için şifre değiştirme ayarı "Password Never Expires" şeklinde tanımlanmalıdır.
- Tanımlanan Wings kullanıcısı eğer yeni oluşturulan bir kullanıcı ise gerekli klasörlerin oluşması ve politikaların işletilebilmesi için bu işlem sonrasında en az bir defa sisteme giriş yapması gerekmektedir.

![](../_assets/a207b1744373cbb84665.png)

- Sunucu üzerinde tanımlanan wings kullanıcısı üzerinden uygulamayı kullanabilmek için "Control Panel (Denetim Masası)-System (Sistem) özelliklerinde bulunan "Allow users to connect remotely to this computer" (Bu bilgisayara uzaktan bağlantıya izin ver) seçeneğini işaretlenip Remote Desktop (Uzak Masaüstü) özelliğinin devreye alınması gerekmektedir.

![](../_assets/21dc633f0f99085fc3cc.png)
- Tanımlanan Wings kullanıcısı "Administrators" ve "Remote Desktop Users" grubuna dahil edilmelidir.

![](../_assets/3546a8cbcaccd56a717e.png)

![](../_assets/ffa9a03f775cbfe3abb3.png)

Kullanıcı tanımlama işlemleri sonrası terminal server üzerinden oluşturduğumuz wings kullanıcısıyla aynı anda birden çok oturum açabilmek için izlenen adımlar şunlardır; Run (Çalıştır)\>gpedit.msc\>Edit Group Policy (Grup ilkesini düzenle)\>"Computer Configuration ( Bilgisayar yapılandırması)\>Administrative Templates (Yönetim Şablonları)\>Windows Components (Windows bileşenleri)\>Remote Desktop Services (Uzak Masaüstü Hizmetleri)\>Remote Desktop Session Host (Uzak Masaüstü Oturumu Ana Bilgisayarı)\>Connections (Bağlantılar)\>"Restrict Remote Desktop Services users to a single Remote Desktop Services session" (Uzak masaüstü hizmetleri kullanıcılarını bir uzak masaüstü hizmetleri oturumuyla sınırla) özelliğinin "Disable" (Kapalı) edilmesi gerekmektedir.

![](../_assets/c359f8704c37c45851cb.png)

![](../_assets/0e41416dd4750abda2be.png)

![](../_assets/76095f5b5c51488329eb.png)

Kurulum ve güncelleme işlemlerinin yapılacağı server işletim sisteminde "ESET" antivirüs programı kullanılıyorsa antivirüs ayalarından ilgili EXE'ler için istisnalar eklenmeli ve 127.0.0.1 adresi de istisna olarak eklenmelidir.

"Advanced Setup (Gelişmiş Ayarlar)" \> Web and Email \> Excluded Applications (Dışarıda Bekleyen Uygulamalar); "C:\\Netsis\\ENTERPRISE9\\VUI\\bin64\\Thinfinity.VirtualUI.Broker.exe" "C:\\Netsis\\ENTERPRISE9\\VUI\\bin64\\Thinfinity.VirtualUI.Gateway.exe" "C:\\Netsis\\ENTERPRISE9\\VUI\\bin64\\Thinfinity.VirtualUI.Server.exe" "C:\\Netsis\\ENTERPRISE9\\VUI\\bin64\\Thinfinity.VirtualUI.SvcMgr.exe"

Setup\>Network\>Network attack protection (IDS)'in sağındaki ayarlar\>Web and Email\>"Excluded

IP Address"\>127.0.0.1

![](../_assets/94e52f7c86166a5eb026.png)

![](../_assets/8a90f7f07c1bf288b3a6.png)

Sunucu üzerinde yapılması gereken bir diğer Group Policy (Grup İlkesi) ayarı da, Wings açıldıktan sonra giriş ekranı açıkken veya kullanıcı işlem yaparken oturumunun düşmesinin engellenmesi için yapılan oturum süresi ayarıdır. Oturum Süresi ayarı ile ilgili düzenleme için izlenen adımlar şunlardır; Run (Çalıştır)\>gpedit.msc\>Edit Group Policy (Grup İlkesini düzenle)\>"User Configuration ( Kullanıcı yapılandırması)\>Administrative Templates (Yönetim Şablonları)\>Windows Components (Windows bileşenleri)\>Remote Desktop Services (Uzak Masaüstü Hizmetleri)\>Remote Desktop Session Host (Uzak Masaüstü Oturumu Ana Bilgisayarı)\>Session Time Limits (Oturum Süresi Limitleri) "Set time limit for disconnected sessions özelliğinin "Enable" edilip süreyi "Never" (Hiçbir Zaman) olarak düzenlemek gerekmektedir. Bu düzenlemenin aktif olabilmesi için işlem sonrası sunucunun yeniden başlatılması gerekmektedir.

![](../_assets/c359f8704c37c45851cb.png)

![](../_assets/010670d8490b0193c518.png)

![](../_assets/b8f31b2e8c015d9dba34.png)

**Not**: HTML içeriklerin olduğu beyanname parametreleri gibi ekranlarda gelen güvenlik uyarıları için Start\>Server Manager\>Local Server\>IE Enhanced Security Configuration\>Off şeklinde düzenlenmelidir. Eğer halihazırda bu ayar off durumda ise Internet Explorer'ı açıp gelen ekran üzerinden varsayılan ayarlar uygulansın uyarısı kabul ederek kapatmak gerekmektedir. Bu düzenlemelerden sonra "Administrators" ve "Remote Desktop Users" grubuna dahil edilen bu kullanıcı için "C:\\ProgramData\\Logo\\NetsisWings" dizinine "yazma" yetkisi verilmelidir.

![](../_assets/a30b9f5c4cea00714d2d.png)

![](../_assets/735b21543372f1e565a8.png)

"C:\\Users\\Administrator\\AppData\\Roaming\\Logo\\NetsisWings" dizinine Wings kulanıcısı için "yazma" yetkisi verilmelidir. (Administrator yerine kurulum yapılacak olan sunucuya giriş yapan kullanıcı ismi yazılacaktır.)

![](../_assets/251a46e238f57524e170.png)

![](../_assets/7de2bc1af2a009f659d3.png)

"C:\\Users\\wings\\AppData\\Local\\Temp" dizinine Wings kullanıcısı için "yazma" yetkisi verilmelidir.

![](../_assets/b468958e0727a6492307.png)

![](../_assets/e7d9a2344cbfe6ac98fc.png)

Son olarak "C:\\Netsis\\ENTERPRISE9" dizinine "Wings" kullanıcıs için "yazma" yetkisi verilmelidir. (Bkz. Ekran Görüntüsü-20,21) (Netsis kurulum dizini farklılık gösterilebilir, bu dizin Netsis'in kurulu olduğu dizin olarak belirlenecektir)

![](../_assets/7f8523b6e4287d99674f.png)

![](../_assets/54aeb97b2f7a787f91c2.png)

#### Wings 3.0 Kurulum ve Ayarlar

Wing 3.0 kurulum ve ayarlarının yapılması için yapılması gerekenler aşağıdaki şekildedir:

- Logo Netsis Wings sistem ihtiyaçları dokümanında belirtilen minimum sistem ihtiyaçları ve kurulum yapılacak sunucu konfigürasyonları kontrol edildikten sonra 9.0.37.0 seti indirilmelidir.
- 9.0.37.0 set güncelleme işlemleri sonrası "SSO Merkezi Kimlik Uygulaması" güncellenmelidir.

![](../_assets/429d4170db867f42eb88.png)
- SSO Merkezi Kimlik Uygulaması güncelleme işlemi tamamlandıktan sonra "Ephesus.exe" ile bir kez Temelset uygulamasına giriş yapılıp sonrasında SSO Merkezi Kimlik Uygulaması üzerinden "OnayIı Sürüm Güncelleme" işlemi çalıştırılacaktır. Bu şekilde Wings 3.0 kurulumu için gerekli olan Thinfinity lisansı güncellenmiş olacaktır.

![](../_assets/a7c1727446a8b7e40f4e.png)

![](../_assets/cb0e06af000a8509812f.png)

![](../_assets/c464ba93a3f731448651.png)
- "Onaylı Sürüm Güncelleme" işlemi "Başarılı" bir şekilde tamamlandıktan sonra 9.0.37.0 versiyonlu güncel Netsis90.exe üzerinden "Sunucu Kurulumu" işlemi başlatılmalıdır.

![](../_assets/b2185b66f0241fc1f711.png)

![](../_assets/c8f933a745ba8d4a008c.png)
- Sunucu kurulumu adımları izlenip "Wings Kurulum Ayarları" ekranına gelindiğinde "Wings Kurulumu Yapılsın" seçeneği işaretlenerek "Kullanıcı Ayarları" bölümünden sadece Wings için tanımlanan "Local Admin" kullanıcısının Kullanıcı Adı ve Şifre bilgileri girilmelidir.

![](../_assets/44a094d6c3058452d330.png)
- Kullanıcı adı ve Şifre bilgileri başarılı şekilde doldurulduktan sonra ekrana çıkan "Bilgi" penceresinde Tanımlanan Wings kullanıcısı için belirtilen tanımlama ve yetkilendirme adımları tamamlanmalıdır.

![](../_assets/cd1cf7f478ef1fc4a4c7.png)
- Önceki Wings sürümünde manuel olarak yapılan tüm "Load Balancing" işlemleri Wings 3.0 sürümüyle birlikte varsayılan olarak işaretli "Load Balancing" parametresinin seçilmesiyle otomatik olarak yapılacaktır.

Wings uygulamasının "Load Balancing" modunda kullanılabilmesi için kurulum ve güncelleme işlemlerinin Sunucu/Server İşletim Sistemleri üzerinde yapılıyor olması gerekmektedir. Windows 10 sunucu üzerinde kurulum yapılıyor ve wings kullanıcı sayısı "4" ve altında ise "load balancing" modunda kurulum yapmadan da wings uygulaması kullanılabilmektedir. Thinfinity.VirtualUI.Server üzerinde "Sessions" ayarları bölümünde yer alan "Shared Windows Session" modu ve "Use the current interactive session or console" login seçenekleriyle birlikte çalıştırılabilmekte ancak bu yöntem kullanıcı sayısının fazla olduğu durumlarda önerilmemektedir.

![](../_assets/5d5448b7ea614b5cbfd4.png)

![](../_assets/e710cff98af67a391179.png)

Netsis90.exe üzerindeki kurulum "Kurulum uygulaması sadece güvenlik ve lisans dosyasını güncellenmesin mi? Sorusuna "Evet" seçeneği işaretlenerek tamamlanır.

![](../_assets/6e13d8e78c26a4943d3c.png)

Kurulum tamamlandıktan sonra gelen log bilgisi ekranında İşlem Tipi "Wings" için sonuçların başarılı olarak tamamlandığından emin olunmalıdır.

![](../_assets/b595ed502f62a319e03e.png)

Netsis90.exe Sunucu Kurulumu işlemi tamamlandıktan sonra lisans aktive işleminin başarılı bir şekilde tamamlandığından emin olmak için "C:\\Netsis\\ENTERPRISE9\\VUI\\bin64" dizini altındaki "Log.txt" dosyasının en alt bölümünde "**Lisans Aktive edildi**." Bilgisi kontrol edilmelidir.

![](../_assets/5e0bf44d8772a8fc78f0.png)

![](../_assets/704c723a475087ce183d.png)

"Log.txt" dosyası incelenip "Lisans Aktive edildi." bilgisi doğrulandıktan sonra "C:\\Netsis\\ENTERPRISE9\\VUI\\bin64" dizini altında "Thinfinity.VirtualUI.Server.exe" Wings3.0 konfigürasyonları ve bağlantı bilgileri test edilip düzenlenmelidir.

![](../_assets/94f434505ed516b6c561.png)

Thinfinity.VirtualUI.Server ilk açılışta Lisans seçim ekranı gelecektir. Wings 3.0 için kullanılacak lisans anahtarı işaretlenerek "Select" butonu yardımıyla seçimi yapıldıktan sonra "Close" butonu ile ekran kapatılacaktır.

![](../_assets/c3cb29132448f6e26d52.png)

Thinfinity.VirtualUI.Server üzerinde "Sessions" sekmesinde Wings için tanımlanan "Local Admin" Username ve Password bilgileri Netsis90 "Wings Kurulum Ayarları" bölümünde tanımlanan kullanıcı bilgileri ile otomatik olarak doldurulmaktadır. Kurulum adımlarında "Bilgi" ekranında gösterilen dizinler için yetki kontrol bu ekranındaki "Test" butonu tıklanmalıdır. Bu işlem sonrası yetki hatası mesajı alınması durumunda "Bilgi" ekranındaki yetki ile ilgili maddeler tekrar kontrol edilmelidir.

![](../_assets/cfd5e78fbe973f5a1989.png)

Thinfinity.VirtualUI.Server üzerinde "Applications" ayarları bölümünde yer alan "Credentials" ekranındaki kullanıcı bilgileri ilk kez Wings kurulumu yapılıyor ise boş olarak gelecektir. Bu durumda uygulamaya giriş bilgileri "Session" sekmesindeki kullanıcı bilgilerinden alınacak ve bu ekranda bilgileri doldurmaya gerek kalmayacaktır. Wings güncelleme işlemi yapılıyor ise bu ekranda kullanıcı bilgileri "Sessions" sekmesindeki bilgiler ile aynı gelecektir. Wings güncellemesi yapılıyorsa "Credentials" sekmesindeki bilgiler kontrol edilip "Ok" tuşuna basılarak ayarların kaydedilmesi gerekmektedir.

![](../_assets/b2ca2cd4fa133c473679.png)

![](../_assets/7a06dae22c3e8032f5a2.png)

Wings 3.0 kurulumu işlemi sonrası eski versiyonlardaki "Netsis Wings" ve "Load Balancing" uygulamasının kullanılması durumunda "Broker" ve "Gateway" servisleri otomatik olarak kaldırılıp bu servisler yerine "**Thinfinity VirtualUI Service Manager**" servisi kurulacaktır. Son olarak "Thinfinity VirtualUI Service Manager" servis yeniden başlatılıp uygulamaya giriş yapılabilir.

![](../_assets/6706b2232e55d3f49cf1.png)

Kurulum ve güncelleme adımları tamamlanmıştır. "Wings 3.0" uygulaması bu işlemlerden sonra güncel versiyonuyla çalıştırılabilmektedir.

![](../_assets/545758441ed30d2a2302.png)
