---
title: "Netsis Services Health Checker Manager"
page_id: "111247760"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis Services Health Checker Manager"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis Services Health Checker Manager"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTA3MjhlZGMyLTJkMmItNDRiYi1iMjZmLWFlNWMwNDQ3N2UxOSZsaW5rPTM2NGZmN2U4LWRlYjQtNDA0OC05YmM1LTk2OGI1ZDlmM2VkMiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=0728edc2-2d2b-44bb-b26f-ae5c04477e19&link=364ff7e8-deb4-4048-9bc5-968b5d9f3ed2&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-services-health-checker-manager_111247760_111247760.html"
source_version: "2023-05-05T14:22:19.430+03:00"
source_bytes: 151930
fetched_at: "2026-09-13T04:23:26+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis Services Health Checker Manager

Netsis Health Checker Servisi ile ilgili ayrıntılı bilgiye bu dokümandan ulaşılır.

Netsis Health Checker, Netsis tarafından kullanılan yardımcı servislerin çalışır durumda olup olmadığını ve çalışan servislerin sağlıklı bir şekilde cevap dönüp dönmediği gibi durumları belirli aralıklar ile denetleyen bir altyapı servisidir.

Netsis Health Checker ile **Netsis NetOpenX Rest Servisi**, **Netsis Sso Servisi** ve **Notification.WinService**'in kontrolleri yapılır.

Netsis Rest, Sso ve Notification servislerinin herhangi bir nedenden dolayı "Stopped" durumda olması veya "Running" durumda gözükmesine rağmen gelen istekleri işleyemeyecek duruma gelmesi halinde ilgili servislerin sağlıklı bir durumda tekrar çalışması Health Checker tarafından sağlanır.

Healt Checker servisinin kurulumu için "Kurulum" dizini içerisinde bulunan **"NetsisServicesHealthCheckerSetup"** uygulaması yüklenmelidir. Uygulamanın kurulumu tamamlandıktan sonra services.msc'de "Netsis Services HealthChecker" isimli servis oluşur ve başlangıçta çalışacak bir servis olarak ayarlanır.

Health Checker yönetim paneline, "Netsis Services HealthChecker Manager" kısayolu ile erişim sağlanabilir.

![](../_assets/1a42fdc3d87914908b61.png)

Uygulama arayüzündeki "HealthCheck Servisi" bölümünde Health Check servisinin çalışma durumu gösterilir ve "Stopped" durumda ise Çalıştır butonu ile servisin çalıştırılması sağlanabilir.

**Health Check Yapılacak Servisler** bölümünde, tablodan seçilen satırdaki servis ile ilgili tanımlamalar yapılır. Heath Checker kurulumu gerçekleştirildiğinde tüm servisler için kontrolün yapılacağı "Aktif" seçeneği işaretli olarak ayarlanır. Kontrol yapılması istenmeyen servislerin Aktif kutucuğu kaldırılabilir.

**Makine İsmi** alanına Rest, Sso ve Notification servislerinin kurulu olduğu makine adı bilgisi girilmelidir. Bu bölüm kurulum ile birlikte otomatik olarak doldurulur.

**Kontrol Sıklık Periyodu** ve **Kontrol Sıklığı** tanımlarında seçili olan servisin kontrol başlangıç tarihinden itibaren ne sıklıkla kontrol edileceği belirlenir.

Health Checker ile iki tür servis kontrolü sağlanır;

1. **Servis Çalışmıyorsa Yeniden Başlatılsın** seçeneği ile kontrol edilen periyotta "Stopped" durumda olan servisin yeniden başlatılması sağlanır.
2. **Servis HealthCheck'i Başarısızsa Yeniden Başlatılsın** seçeneğinde ise ilgili servisin kontrol edilen periyotta "Running" durumda olmasına rağmen sağlıklı bir sonuç dönmemesi durumunda servisi yeniden başlatılması sağlanır.

**HealthCheck Adresi (Http)** alanında NetOpenX Rest servis adresi yazılarak adresin sonunda Health Check methodunun belirtilmesi gerekir.

**Process Olarak Çalışan Servis** seçeneği sadece Notification.WinService için işaretlidir. Process Path alanında "Netsis.Notification.WinService.exe" uygulama yolu ve adı belirtilmelidir.

**Log Seçenekleri** bölümünde Health Checker loglarına ne tür log bilgilerinin *(Error, Info, Trace)* kaydedileceği belirlenir. Oluşan log kayıtları **"C:\\Program Files (x86)\\Logo\\Netsis Services HealthChecker\\Log"** dizini içerisinden görüntülenebilir.
