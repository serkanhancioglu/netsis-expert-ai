---
title: "İş Akış Online Onay Sistemi SSS"
page_id: "66250673"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "İş Akış Online Onay Sistemi SSS"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / İş Akış Online Onay Sistemi SSS"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTEzZDQ3MDIxLTk4NzEtNGNlYi1iNDU3LWQ5YzA3MGJmNmY5ZSZsaW5rPWZkMWY3MWRiLWI4N2ItNGE3Zi1hNGJkLTI2YzY4ZDJjZTMyZCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=13d47021-9871-4ceb-b457-d9c070bf6f9e&link=fd1f71db-b87b-4a7f-a4bd-26c68d2ce32d&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "is-akis-online-onay-sistemi-sss_80088466_66250673.html"
source_version: "2022-12-07T16:23:08.710+03:00"
source_bytes: 1868639
fetched_at: "2026-09-13T04:24:25+00:00"
generator: "netsis-scraper 1.0.0"
---
# İş Akış Online Onay Sistemi SSS

**İş akış yönetiminde online onay sisteminin aktif olması için tanımlama nasıl** **olmalıdır?**

"Şirket Şube Parametre Tanımları" ekranındaki "İş Akışı Uygulaması Var" ve "İş Akış Online Onay Sistemi" parametreleri işaretli olmalıdır.

![](../_assets/98d52bc9dd8f9811d2f0.png)
![](../_assets/58e1e3321727ced8800d.png)

**Online** **Onay** **sistemi** **hangi** **servisi** **kullanmaktadır?**

İş akış kayıtları ekranında yapılan tanımlamalarda e-posta seçeneği "Evet" olarak seçili olmalıdır. Online onay sistemini Netsis Notification servisi yönetmektedir.

**İş** **akış** **online** **onay** **sistemi** **hangi** **paketlerde** **desteklenmektedir?**

İş akış online onay sistemi özelliği Enterprise pakette desteklenmektedir.

**İş akış için online onay sistemini kullanımında gönderilen maillerde onay veya** **red** **linki** **oluşmamaktadır.** **Neden olabilir?**

"Online Onay Sistemi Ayarları" ekranından ilgili sistem aktif hale getirilmelidir ve erişim sorunu olmayacak şekilde doğru bir servis adresi yazılmalıdır. Bu adrese erişim sağlanıp sağlanmadığı kontrol edilmelidir. "Şirket Şube Parametre Tanımları" ekranındaki "Online Onay Sistemi" ve "İş Akış Online Onay Sistemi" parametreleri işaretli olmalıdır.

![](../_assets/cca4b353c924d8b3b7e5.png)
![](../_assets/eb887b3926e22f99c271.png)

Yukarıdaki parametre tanımları yapılmasına rağmen gönderilen mail üzerinde onay/red linkleri oluşmuyor ise görev yöneticisi üzerinden Netsis.Notification.WinService.exe uygulamasının çalışıyor olduğundan emin olunmalıdır.

![](../_assets/3820ad5bf937a1b56932.png)
![](../_assets/2cbe81138846f865b5c3.png)

**Online** **onay** **sistemi** **ayarlarında port** **bilgisi** **2025'den** **farklı** **bir** **değer** **verilebilir** **mi?**

2025 nolu portu notification servis portu + 1 değerine karşılık gelmektedir.

"C:\\ProgramFiles(x86)\\Logo\\MerkeziYönetim\\SsoService\\Notification" klasörü içerisindeki Netsis.Notification.Settings.json dosyası edit mod ile açılarak aşağıda görünen 2024 nolu port yerine verilmek istenen port değerinin bir eksiği yazılmalı ve online onay sistemi ayarlarında da verilmek istenen port değeri yazılmalıdır.

Bu değişikliği yaptıktan sonra sso servisini restart etmek gerekmektedir. Örnek olarak verilmek istenen port değeri 1999 olsun.

O zaman Netsis.Notification.Settings.json dosyasında aşağıda belirtilen alana 1998 yazılmalıdır.

![](../_assets/2f2374c69cdafbcb4620.png)

Online onay sistemi ayarlarına ise tanımlama aşağıdaki gibi olmalıdır.

![](../_assets/ae28a179971babc63588.png)

Bu işlemlerden sonra bu port üzerinden gönderim sağlanmaktadır.

**Online** **iş** **akış** **onay** **sistemi kullanımında** **mail** **üzerinden** **onaylanarak** **tamamlanan** **iş** **akış** **kayıtlarında** **cari** **irtibat** **bilgilerindeki** **mail** **adresine** **mail** **gönderimi** **sağlanmakta** **mıdır?**

Online iş akış onay sistemi kullanımında mail üzerinden onaylanarak tamamlanan iş akış kayıtlarında cari irtibat bilgilerindeki mail adresine mail gönderimi yapılmaktadır.
