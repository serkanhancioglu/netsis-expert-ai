---
title: "Netsis Wings Enterprise ve Netsis Wings Kurulum Dokümanı"
page_id: "50679740"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis Wings Enterprise ve Netsis Wings Kurulum Dokümanı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis Wings Enterprise ve Netsis Wings Kurulum Dokümanı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTE4ZGM2MTk0LTBkYzMtNDUzNS05NDU1LWY0NTcwMTZkNDVlNCZsaW5rPTM4ZGU3ZTU4LTQ5NTktNDBjOC04ZGZjLTBhMGM4ODRkNzA5NiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=18dc6194-0dc3-4535-9455-f457016d45e4&link=38de7e58-4959-40c8-8dfc-0a0c884d7096&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-wings-enterprise-ve-netsis-wings-kurulum-dokumani_82575608_50679740.html"
source_version: "2022-11-03T09:12:24.997+03:00"
source_bytes: 820949
fetched_at: "2026-09-13T04:25:46+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis Wings Enterprise ve Netsis Wings Kurulum Dokümanı

Netsis Wings Enterprise ve Netsis Wings Kurulumu ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

**Kurulum** **ve** **Ayarlar**
Netsis Wings Enterprise ve Netsis Wings Kurulum ve Ayarları için izlenen adımlar aşağıdaki şekildedir:

- LOGO Netsis Wings ve LOGO Netsis Wings Enterprise, Web platformunda çalışmaktadır ve Netsis 3 ürününün özellik setine sahiptir.
- Masaüstü, Web veya hem masaüstü hem Web ortamından çalıştırılabilir.
- Fiziksel bir sunucuda veya bulut ortamında kurulum yapılabilir.
- E-devlet uygulamaları için uzak bağlantı yapılması gerekmektedir.
- Ürün için herhangi bir IIS kurulumuna gerek yoktur.
- İstemci tarafında herhangi bir kurulum yapmadan HTML5 destekli bir tarayıcı ile çalışmaktadır.
- LOGO Netsis Wings ve LOGO Netsis Wings Enterprise uygulaması, server tarafında bulunan bir Windows servis ile çalışmaktadır.

Netsis Wings ve Logo Netsis Wings Enterprise Kurulumu için izlenen adımlar aşağıdaki şekildedir:

- Netsis Wings sistem ihtiyaçları dokümanında belirtilen minimum sistem ihtiyaçları ve kurulum yapılacak server konfigürasyonları kontrol edilir.

![](../_assets/2663963948d541280cb6.png)

- Netsis kurulum dosyaları +[ftp://download.logo.com.tr+](ftp://download.logo.com.tr+) adresinden temin edilir.

- SSO Merkezi Kimlik Uygulaması üzerinden Netsis Wings lisansı indirilir.

![](../_assets/370a3b0be12f7aacc505.png)

- Ftp' den indirilen kurulum dosyası (Netsis90.exe) çalıştırılır.

![](../_assets/e8318b3c04c0c9051e24.png)

Kurulum sırasında "Wings Kurulum Ayarları" bölümündeki gerekli alanlar aşağıdaki şekildedir:

**Kullanıcı** **Adı:** Oluşturulacak Wings servislerinin ve sunucuda çalıştırılacak Wings uygulamasının hangi kullanıcı yetkisi ile yönetileceği belirtilir. Belirtilen bu kullanıcı ilgili bilgisayarda local admin ya da domain admin yetkisine sahip olmalıdır ve Wings uygulaması için ayrı bir kullanıcı açılması tavsiye edilmektedir.

**Şifre:** İlgili kullanıcının şifresi belirtilir.

**Port:** Uygulamaya hangi port üzerinden ulaşılacağı belirtilir. İhtiyaç durumunda windows firewall üzerinden bu port'un açılması gerekmektedir.

**Idle** **Timeout:** Uygulama açıkken boş durumda (işlem yapmadan) bekleme süresini belirtilir. Kullanıcı bu süreden daha fazla boşta beklediğinde Wings uygulaması kapatılacaktır.

**Wings Timeout:** Uygulamanın time out süresi belirtilir. Uygulama kapatıldıktan sonra exe'nin sistemden kapatılma süresi olup saniye olarak giriş yapılır.

Scaling ve Load Balancing senaryosu söz konusu değilse kurulum sırasında Broker ve Gateway servisleri seçilmemelidir. Bu durumda servisleri de oluşmayacaktır.

Kurulum sonrasında seçilen hizmetlere göre aşağıdaki Windows servisleri oluşturulacaktır:

Logo Services Agent (Light): Idle Timeout ve Wings Timeout parametrelerini kontrol eden servistir.

Netsis Sunucu Servisi 9.0

Netsis Wings Service

Netsis Wings Broker Service: Aynı networkte bulunan ve kendisine tanımlanan gateway'lerden gelen istekleri karşılayıp cevaplayan servistir.

Netsis Wings Gateway Service: Gelen bağlantıların ayakta olan sunuculara dağıtılması işlemini gerçekleştirir.

#### ![](../_assets/b2ac53d56b744c155e0a.png)

Netsis Wings Yönetim Paneli

Netsis Wings Yönetim Paneli için izlenen adımlar aşağıdaki şekildedir:

- Programın kurulumu esnasında yanlış kullanıcı şifresi girişi yapıldığında, kullanıcının şifresi değiştiğinde ya da Netsis Wings Web penceresinin açılışında sorun ile karşılaşıldığında yönetim panelinde tanımlı bilgiler kontrol edilmelidir.
- Netsis Wings Yönetim Paneline Netsis kurulumunun bulunduğu dizin üzerinde "VUI\\bin32{color} Thinfinity.VirtualUI.Server.exe" yolundan erişilebilir
![](../_assets/07d4ae6172c879cfbe7e.png)
- RDS sekmesinde yer alan Username ve Password bilgileri kontrol edilmelidir.

![](../_assets/50d8b1bc43b6e43d79c7.png)

- Yönetim panelindeki Applications sekmesinde NetsisWingsWeb.exe yolu seçilerek Edit ile açılır. Ardından bu bölümdeki Credentials sekmesinde bulunan Username ve Password alanları kontrol edilmelidir.

![](../_assets/6ecbc7a754c8f05483f9.png)
![](../_assets/2197b9408f96ee9e5ddc.png)

- Yönetim panelindeki Applications sekmesinde NetsisWingsWeb.exe yolu seçilerek Edit ile açılır. Ardından bu bölümdeki Permissions sekmesinde bulunan "Allow anonymous access" seçeneğinin işaretli olduğundan emin olunmalıdır.

![](../_assets/4d710987519563c7c53f.png)

- Yönetim panelindeki Authentication sekmesindeki "Allow anonymous access" işaretli olmalıdır.

![](../_assets/9857c7645cb25ff16dcf.png)

- Yönetim panelindeki General sekmesinde "Server started." ifadesinin yazdığından emin olunmalıdır.

![](../_assets/96c67061e61d24f5704f.png)

- Yönetim panelinde yapılan değişikliklerin geçerli olması için server üzerindeki LogoNetsisWings servisi yeniden başlatılmalıdır.
