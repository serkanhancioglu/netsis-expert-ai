---
title: "Netsis 3 Wings Thinfinity v3.0 Yönetim Paneli"
page_id: "79167739"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis 3 Wings Thinfinity v3.0 Yönetim Paneli"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis 3 Wings Thinfinity v3.0 Yönetim Paneli"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTEzNmViZDAyLWM4MDEtNDhiZi1hMWE0LWUxZTA5MzY1MGI1NSZsaW5rPTFmYTYzMDY2LTE5OWYtNGVlMi05NWJiLWZjNzJmZmU0MGJiNCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=136ebd02-c801-48bf-a1a4-e1e093650b55&link=1fa63066-199f-4ee2-95bb-fc72ffe40bb4&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-3-wings-thinfinity-v3-0-yonetim-paneli_80087369_79167739.html"
source_version: "2022-11-02T14:39:49.160+03:00"
source_bytes: 590474
fetched_at: "2026-09-13T04:24:09+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis 3 Wings Thinfinity v3.0 Yönetim Paneli

Netsis 3 Wings Thinfinity v3.0 Yönetim Paneli ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

**General** Sekmesinde bulunan Bindings alanında, istemcilerin Wings adresine erişim sağlamak için kullanacağı bağlantı noktaları listelenmektedir. Netsis 3 Wings, Wings kurulumu aşamasında belirlenen port (varsayılan 6580) üzerinden çalışmaktadır. Eğer uygulamanın farklı bir port üzerinden çalışması istenirse, Edit modu ile açılan ekrandan port numarası değişikliği yapılarak istenilen port üzerinden çalıştırılması sağlanabilir ve aynı ekran üzerinden SSL sertifikası ile ilgili ayarlar yapılabilir.

**Enable** **External Access In Windows Firewall:** Server üzerindeki güvenlik duvarı kısıtlamalarında Wings ürününü kapsam dışı bırakmak için kullanılan ayardır.

Wings loglarına erişmek için **Show Log** butonu kullanılabilir.

![](../_assets/ee6d56ad3545709e0037.png)

**Sessions** Sekmesinde bulunan **Mode** alanında, Shared Windows Session ve One Browser per Windows Session olmak üzere iki farklı seçenek bulunmaktadır.

**Shared Windows Session:** Shared Windows Session alanından, Wings için tanımlanan kullanıcının aktif oturumunda istemcilerden gelen tüm taleplere karşılık yeni bir ephesusweb.exe başlatılır.

**One** **Browser** **per** **Windows** **Session:** One Browser per Windows Session alanından, Her istemci için disconnect mod ile açılan Wings kullanıcı oturumu altında yük dengeleme (load balance) yapılarak ephesusweb.exe başlatılır. Bu sayede Wings uygulamasında yüksek performans elde edilir.

Shared Windows Session modunda tüm isteklere karışık sunucuda tek bir kullanıcı oturumu başlatılırken, One Browser per Windows Session modunda kullanıcı oturumu her istek için disconnect mod ile çalışmaktadır.

![](../_assets/d868ae2cd5c8285ae2ed.png)

**Applications** Sekmesi; uygulama konumu, uygulama ayarları ve erişim için kullanıcı izinlerinin yapılandırıldığı bölümdür. Temelset, NDI ve Sabit Kıymet uygulamaları için ayrı uygulama tanımları mevcuttur.

![](../_assets/d9a8dd640bef6abb8ba8.png)

**Application/General** sekmesi, uygulama profili ayarlarının düzenlendiği bölümdür. Ekran görüntüsünde üst kısımda bulunan ayarlar, Netsis Wings kurulumu ile birlikte ön tanımlı olarak gelmektedir.

**Name:** Name alanı, uygulama adının belirtildiği alandır.

**Virtual Path:** Virtual Path alanı**, u**ygulama için benzersiz bir URL adresinin tanımlandığı alandır.

**Home Page:** Home Page alanı, uygulama açılışı için kullanılan HTML sayfanın seçildiği alandır.

**Icon:** Icon alanı, Web arayüzünde gösterilecek uygulama simgesinin seçildiği alandır.

**Default Application:** Default Application alanı, mevcut profillerden birini varsayılan yapmak için seçilebilecek alandır.

![](../_assets/4e203aa2c01f310d1cb3.png)

**Application/General** Sekmesinde bulunan **Resolution** ayarları ile, Wings ürününün tarayıcı içerisindeki çözünürlük bilgisi ayarlanabilir. **Resolution** ayarı varsayılan olarak web tarayıcıya yayılmış (Fit to browser windows) olarak gelir.

**Reconnection** **Timeout:** Reconnection Timeout alanına girilen değer baz alınarak Wings ürünü kapatılmadan tarayıcı sekmesi kapatıldıktan sonra tekrar yeni sekme ile ürün açılmak üstendiğinde oturumun ne kadar süre açık kalacağı belirlenir. Bu süre zarfında ürün yeniden açılırsa kullanıcı direkt olarak ürüne erişebilecek ve tekrar giriş yapmasına ihtiyaç duyulmayacaktır.

**Default** **Quality:** Default Quality alanından, Wings ekranının görüntü kalitesi ile ilgili ayarlar yapılabilir.

![](../_assets/424be9c775ff3e579817.png)

**Application/Credentials** sekmesinde sunucuya erişim için, Use these credentials seçeneği ile kullanıcı bilgileri tanımlanmalıdır. Wings kurulumu esnasında belirtilen kullanıcı hesabı bu bölüme kaydedilmektedir.

Not: Kullanıcı hesabında değişiklik yapılması durumunda **Sessions** ve **Credentials** sekmelerinde bulunan kullanıcı hesap bilgileri yeniden doğrulanmalıdır.

![](../_assets/42aa9023fb0d08c3fd7f.png)

**Application/Permissions** sekmesi, uygulamaya erişim sağlayabilecek kullanıcıların seçildiği bölümdür.

**Allow** **anonymous Access:** Allow anonymous Access seçeneği, herhangi bir kimlik doğrulama olmadan uygulamayı kullanılabilir hale getirmek için işaretlenmesi gereken seçenektir. Bu, Thinfinty VirtualUI'a erişen herkesin uygulamaya erişebileceği anlamına gelir. Allow anonymous Access seçeneği işaretlendiğinde Add/Remove butonları devre dışı bırakılmaktadır.

Not: Wings uygulamalarının çalışması için allow anonymous access seçeneği işaretli olmalıdır.

![](../_assets/7704177c4342b0427dda.png)

**Application/Restrictions** sekmesinde IP adresi bazında güvenlik ayarları yapılabilmektedir. Uygulamaya bağlanmasına izin verilmek istenen IP adreslerinin erişimine izin verilebilir veya erişim engellenebilir.

**No restrictions** alanında, hangi IP adreslerinin uygulamaya bağlanabileceği konusunda herhangi bir kısıtlama bulunmamaktadır.

**Allow** **only** **from** **these** **Ips** alanında, listelenen tüm IP adreslerinin bağlantılarına izin verilir.

**Block** **connections** **from** **these** **Ips** alanında, listelenen tüm IP adreslerinin bağlantıları engellenir.

**Add** alanı listeye yeni bir IP adresi eklemek için kullanılır.

**Remove** alanı, listede mevcut bir IP Adresini silmek için kullanılır.

![](../_assets/2e3b5756a0e4a6b8ee8a.png)

**Application/Access Hours** sekmesinde kullanıcıların belirlenen tarih aralığında ve saatlerde uygulamaya erişimi engellenebilir veya izin verilebilir.

**Access Permitted** alanında, uygulamanın hangi gün ve saatte müsait olacağı tanımlanır.

**Access Denied** alanında, uygulamaya hangi gün ve saatte devre dışı bırakılacağı tanımlanır.

Not: Bu bölümde herhangi bir tanımlama yapılmaması durumunda uygulamaya sürekli erişim sağlanabilecektir.

![](../_assets/2f074569a839299b7571.png)

**Services** Sekmesinde Wings ürününün load balancing senaryosunda çalışması için **Broker Service** ve **Gateway Service** işaretli olmalıdır.

![](../_assets/5bc14db0a4c5c7773276.png)

**Licence** Sekmesinde mevcut Wings lisansına ait bilgiler görüntülenebilir.

![](../_assets/37a85d20e3f507e8ff02.png)
