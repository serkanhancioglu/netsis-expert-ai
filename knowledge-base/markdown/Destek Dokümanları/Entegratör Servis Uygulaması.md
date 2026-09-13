---
title: "Entegratör Servis Uygulaması"
page_id: "128585833"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Entegratör Servis Uygulaması"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Entegratör Servis Uygulaması"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWU4MjY1OGQwLWE3NDItNGNlMS1hNzZkLTQ4ZTI5ZWY5ODUwZCZsaW5rPWU5MWRlODc3LTIwYWQtNDNkNS05ZmI3LWM5ODM3ODgxNzYyNCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=e82658d0-a742-4ce1-a76d-48e29ef9850d&link=e91de877-20ad-43d5-9fb7-c98378817624&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "entegrator-servis-uygulamasi_128585833_128585833.html"
source_version: "2024-01-18T11:10:48.763+03:00"
source_bytes: 810957
fetched_at: "2026-09-13T04:22:57+00:00"
generator: "netsis-scraper 1.0.0"
---
# Entegratör Servis Uygulaması

**Entegratör Servis Uygulaması nedir?**

Entegratöre gönderilen e-Arşiv faturalarının gönderme, arşivleme ve sorgulama işleminde bekleme olmadan yapılmasını sağlayan, e-Mutabakat işlemlerinde Netsis ve eLogo Mutabakat Portalı arasındaki entegrasyonu sağlayan ve aynı zamanda Netsis' ten oluşturulan e-Defter dosyalarının otomatik olarak Logo Özel Entegratör Portalında saklanmasını sağlayan bir yardımcı servis uygulamasıdır.
Netsis 9.0 ve üzeri versiyonlarda ve tüm paketlerde desteklenmektedir.

**Entegratör Servis Kurulumu**

Netsisin kurulu olduğu dizinde Kurulum klasörü altında EntegratorServisSetup.exe dosyası yönetici olarak çalıştırılır.

![](../_assets/55c8320756a26dd17363.png)

Kullanılacak Uygulamalar kısmında e-Arşiv, e-Mutabakat ve e-Defter Yedekleme seçenekleri bulunmaktadır.

**e-Arşiv** seçilerek kurulum yapıldığında, servis kurulduğunda entegratöre gönderilen e-Arşiv faturalarının; gönderme, arşivleme ve sorgulama işleminin bekleme olmadan yapılması sağlanır. Bu servis, her 10 saniyede bir sorgulama yaparak, arşivlenecek belge varsa bulur ve arşivleme işlemi yapar.

e-Arşiv taslağı oluşturulduktan sonra "**Arşivle**" butonuna tıklandığında devrede olan servis, arşivlenecek kayıtları tespit ederek gönderilmeyi bekleyen e-Arşiv faturalarını entegratöre iletir. Daha önce entegratöre iletilen ve imzalanan belgeleri sisteme indirir ve son olarak e-Arşiv faturalarının entegratördeki durum kodu ve açıklamalarını alarak işlemi gerçekleştirir.

**e-Mutabakat** seçilerek kurulum yapıldığında, servis Netsis içerisinde oluşturulan e- Mutabakatların eLogo Mutabakat portalına gönderilmesini sağlar. Karşı tarafa gönderim de eLogo tarafından yapılır. Mutabakat süreçlerinin hangi aşamada oldukları, tamamlanan veya onaylanmayan mutabakatların takibi, giden mutabakatlar ve ilgili mutabakata yönelik cevaplar (Mutabıkız, Mutabık değiliz gibi.) servis aracılığı ile Netsise iletilir ve e-Mutabakat kayıtları ekranından takip edilir.

**e-Defter** seçilip kurulum yapıldığında, Gelir İdaresi ve Netsis' te onaylı görünen e-Defterler, e- Defter Onaylama ekranında "**Defter Dosyalarını Yedekle**" menüsü seçildiğinde entegratör servisi aracılığı ile eLogo Defter Saklama Portalına yüklenmektedir.

**Kurulum Lokasyonu:** Servisin kurulacağı dizin bilgisi (C:\\Program Files (x86)\\Netsis\\Entegrator Servis) otomatik olarak gelmektedir.

**Servis Port Numaraları**: Entegratör Servisinin çalışacağı port numarası: 2026 ve Netsis İletişim Servisinin çalışacağı port numarası: 9008 numaralı port numaraları kullanılmaktadır.

**Veritabanı** **Bağlantısı:** Veritabanı bağlantı bilgileri girilir. Server adı, veritabanı kullanıcı adı ve şifre bilgileri girilir. Bağlantı yapılacak veritabanı olarak NETSIS veritabanı seçilir ve bağlantı testi yapılır. Bağlantıda sorun yoksa Ok butonuna basılarak erkandan çıkılır.

**Veritabanı** **Bağlantı** **Bilgileri** **Şifrelensin** parametresi otomatik olarak işaretli geliyor. Bu parametre işaretli olduğunda, "Kurulum Lokasyonu" adresinde oluşturulacak olan Netsis.IntegratorSrv.exe.config dosyasında tanımlanan bağlantı bilgileri şifreli olarak oluşturulur.
![](../_assets/e26a2203d809b2f14cc4.png)

**Proxy** **Kullan:** Proxy bilgileri varsa bu alan doldurulmalıdır.

![](../_assets/0a258cb949a466cd011a.png)

![](../_assets/be85dec6324e632db78c.png)
![](../_assets/e00d26972bfdedbeefd3.png)

![](../_assets/b5e74e93a75f235760e2.png)

Ayarların kontrolünden sonra "**Kuruluma** **Başla**" işlemi ile servis kurulumu başlar. Servis kurulum sonrası çalışır haldedir.

![](../_assets/dd8acc4460df6ba260e6.png)

![](../_assets/d70e769b0b6fe0ea27f8.png)

Kurulum sonrasında servisler kısmında Netsis Entegratör Servisi satırı görünür ve çalışır durumunda olması gerekir.

![](../_assets/25178cfa4d9c1698c35f.png)
