---
title: "Netsis SSO WebSocket Kurulumu"
page_id: "50679894"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis SSO WebSocket Kurulumu"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis SSO WebSocket Kurulumu"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTdjMDMyMWU0LTc1ZDQtNGIzZi1iMzIyLTM4YTllZjVlZTUwMyZsaW5rPTYzMjYxNzI2LTMzM2ItNGZmYy04MWIwLTViNmIzMGIyNWU5MSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=7c0321e4-75d4-4b3f-b322-38a9ef5ee503&link=63261726-333b-4ffc-81b0-5b6b30b25e91&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-sso-websocket-kurulumu_82576003_50679894.html"
source_version: "2022-11-03T09:27:00.343+03:00"
source_bytes: 1142638
fetched_at: "2026-09-13T04:25:53+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis SSO WebSocket Kurulumu

Netsis SSO WebSocket Kurulumu ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Bilindiği gibi Netsis Web ürünleri (Net HR, Netsis B2B, Netsis CRM vb.), kullanıcı oturum açılışında Netsis SSO sistemini kullanmaktadır. Netsis SSO web üzerinde oturum açabilmek için Java uygulaması gerektirmektedir. Başta Google Chrome olmak üzere gezgin üreticileri güvenlik açığı oluşturduğundan dolayı Java desteğini kaldırmak yönünde çalışmalar yapmaktadır. Bu nedenle Netsis SSO sistemi, Java olmaksızın çalışacak şekilde güncellendi.

Java olmaksızın çalışabilmek için sunucudaki SSO kurulumu yanı sıra, istemcilerde de **WebSocket** kurulumu yapılması gerekecektir.

#### Netsis Merkezi Kimlik Yönetimi (SSO) Kurulumu

Merkezi Kimlik Yönetimi Servisinin Kurulumu için set içerisindeki kurulum klasörü altındaki NetsisSSOSetup.exe "Yönetici olarak çalıştır (Run As Administrator)" denilerek çalıştırılmalıdır.

![](../_assets/33cda54514a93b9dff3b.png)

![](../_assets/0a93256c61032f539dae.png)

WebSocket kurulabilmesi için bu adımda Netsis Web uygulamasının mutlaka yüklenmesi gerekmektedir.

! Netsis Web uygulamasının kurulacağı sunucunun Windows Server 2003 ve üzeri olması gereklidir, ancak Windows Server 2008 ve üzeri olması önerilir.

! Netsis Web uygulaması ile SSO uygulamasının aynı sunucuda olması zorunlu değildir. SSO farklı bir sunucuya kurulup, Netsis Web uygulaması IIS sunucusu olarak kullanılacak diğer bir sunucuya kurulabilir.

![](../_assets/178805af7bd603f1a50c.png)

#### Web Uygulamalarına Giriş

Kullanıcılar kendi bilgisayarlarından Chrome, Yandex gibi Java desteğini kesen tarayıcılar ile web uygulamalarına giriş yaptığı zaman giriş ekranında aşağıdaki şekilde bir bilgilendirme görürler:

![](../_assets/312914f95ffe7f7973d3.png)

Kullanıcının linkte yazısını tıklayarak "Sso.WebSocket.Setup.exe" dosyasını indirmesi ve kurması gerekmektedir.

Kurulum ile ilgili bilgilere "WebSocket Kurulum Adımları" başlığı altında bulabilirsiniz.

Not: https:// ile başlayan SSL güvenlikli domain girişi kullanan yapılarda kullanıcı, giriş yapılan tarayıcı (Chrome-Yandex) adres çubuğunda aşağıdaki işareti tıklamalı; sağ üstteki işaret tıkladıktan sonra, "Güvenli olmayan komut dosyalarını yükle" yazısını tıklayarak "Sso.WebSocket.Setup.exe" dosyasını indirmelidir.

![](../_assets/4fc5495ce12a4b924617.png)

Web Socket Kurulum Adımları aşağıdaki şekildedir:

- İlgili kullanıcı bilgisayarında Microsoft .NET Framework 4.0 kurulu olmalıdır.
- İndirilen Sso.WebSocket.Setup.exe, "Yönetici olarak çalıştır (Run As Administrator)" denilerek çalıştırılmalıdır.

![](../_assets/1a26ba2d66145669869f.png)

.NET Framework 4.0 kurulu değilse aşağıdaki şekilde bir hata alınır:

![](../_assets/7799800d6b7269688111.png)

Bu durumda dil paketi size uygun olan .net paketini, aşağıdaki linklerden birini de kullanıp indirebilirsiniz.

[{+}](http://www.microsoft.com/tr-tr/download/details.aspx?id=17851)[http://www.microsoft.com/tr-tr/download/details.aspx?id=17851+](http://www.microsoft.com/tr-tr/download/details.aspx?id=17851+) [{+}](http://www.microsoft.com/en-US/download/details.aspx?id=17851)[http://www.microsoft.com/en-US/download/details.aspx?id=17851+](http://www.microsoft.com/en-US/download/details.aspx?id=17851+)

İndirdikten sonra, "dotNetFx40_Full_setup.exe" nizi çaıştırın ve .NET Framework 4.0 kurulumunuzu tamamlayın. Bu aşamadan sonra Sso.WebSocket.Setup.exe, "Yönetici olarak çalıştırıp (Run As

Administrator)" kuruluma başlayabilirsiniz.

![](../_assets/71da6c506fc3d56716ed.png)
- Dil seçimi yapıldıktan sonra, "İleri" tuşu ile sonraki adıma geçilir,
- Ön koşul için Microsoft .NET Framework 4.0 kontrolü tekrar yapılır, yüklü ise İleri ile sonraki adıma geçilir.

![](../_assets/c36db193c7c2b7ad1a86.png)

![](../_assets/7243d35e18c7b58b91bb.png)
- Kurulum yapılacak dizin seçilir, İleri tuşu ile kurulum tamamlanır.

![](../_assets/ede61c58087f4840a894.png)
- Ardından web uygulama için sayfa açılıp tekrar kapatılarak ya da giriş linkine tıklanarak tekrar giriş yapılır ve kullanıcı adı-şifre ekranı görünür durumu gelir.
