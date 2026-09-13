---
title: "e-Arşiv Servis Uygulaması"
page_id: "34213372"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "e-Arşiv Servis Uygulaması"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / e-Arşiv Servis Uygulaması"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTBiZmIxNjQyLTdhNjktNDRlMi1iOTQ0LTlkNGQ1MjBmNWI5NiZsaW5rPWI5YjVmZWNjLTkwODktNDI4NC1iYTc5LWYyMmYxNDgyMzY2MiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=0bfb1642-7a69-44e2-b944-9d4d520f5b96&link=b9b5fecc-9089-4284-ba79-f22f14823662&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "e-arsiv-servis-uygulamasi_82575546_34213372.html"
source_version: "2022-11-03T09:08:58.263+03:00"
source_bytes: 1583481
fetched_at: "2026-09-13T04:25:43+00:00"
generator: "netsis-scraper 1.0.0"
---
# e-Arşiv Servis Uygulaması

e-Arşiv Servis Uygulaması ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Netsis e-Arşiv uygulamasında, faturaların entegratöre gönderilme süresi, imzalanmış e-arşiv faturalarının entegratörden indirilmesi ve entegratörden dönen durum bilgisinin alınması sürecinin kullanıcılar herhangi bir işlem yapmalarına gerek kalmadan çalışan bir servis aracılığıyla yapılabilmesi amacıyla uygulamada düzenleme yapılmıştır.

e-Arşiv uygulamasının desteklendiği ürün grubu; Netsis Enterprise, Netsis Standard ve Netsis Entegre'dir.

e-Arşiv uygulamasının desteklendiği Modül Fatura'dır.
e-Arşiv uygulamasının desteklendiği Kategori Yeni Fonksiyon'dur.

e-Arşiv uygulamasının Versiyon Önkoşulu9.0'dır.

**Uygulama**
Netsis E-Arşiv Servis Uygulaması, entegratöre gönderilen E-Arşiv faturalarının gönderme, arşivleme ve sorgulama işleminin bekleme olmadan yapılmasını sağlayan yardımcı servis uygulamasıdır. Netsis 9.0.0 ve üzeri versiyonlarda ve tüm paketlerde (Entegre/Standard/Enterprise) desteklenmiştir.

Fatura-Kayıt-E-Arşiv İşlemleri-E-Arşiv Parametreleri altına "Netsis E-Arşiv Gönderim Servisi" parametresi gelmiştir.
![](../_assets/47753333b5e608987048.png)

E-Arşiv Servis Uygulaması, her 10 saniyede bir sorgulama yaparak arşivlenecek belge varsa bulur ve arşivleme işlemi yapar.

E-Arşiv taslak oluşturulduktan sonra "Arşivle" butonuna basıldığında devrede olan servis, arşivlenecek kayıtları tespit ederek gönderilmeyi bekleyen e-arsiv faturalarını entegratöre iletir, daha önce entegratöre iletilmiş olup imzalanmış olanları sisteme indirir ve son olarakta e-arşiv faturalarının entegratördeki durum kodu ve açıklamalarını alarak işlemi gerçekleştirir. Dolayısıyla bu işlemler mevcut e-arşiv ekranlarında yapıldığında oluşan performans sorunları ve kullanıcıların bekleme süresi böylece en az seviyeye iner.

![](../_assets/2b0bca5ba3f8cafa8451.png)

Arşivleme işlemi sırasında entegratörden dönen hata cevapları servis tarafından loglanır. Bu kayıtlara Fatura-Kayıt-E-Arşiv İşlemleri-E-Arşiv Log Kayıt İnceleme ekranından ulaşılabilir.

![](../_assets/dff84dd302c4ebfe63bc.png)

Servis; işletme ve şube bazlı olarak e-arşiv log kayıtlarını oluşturur.

İlgili işletmede, merkez şube altında kontrol yapılıyorsa 'Şubeler Dahil Edilsin' parametresi açılarak diğer şubelerde oluşan log kayıtları da görüntülenebilir.
Log kayıtları veritabanında TBLEARSIVLOG tablosuna kaydedilir.

**E-Arşiv Servisinin NetOpenX ile Kullanımı**
NetOpenX ile E-Arşiv kullanımı için Ebelge nesnesi eklenmiş ve ilgili özellikler desteklenmiştir.

{+}http://wikidocs.logo.com.tr/display/NUA/Ebelge+

{+}http://wikidocs.logo.com.tr/pages/viewpage.action?pageId=16023908+ (E-Arşiv Taslak Oluşturma Desteği)

**E-Arşiv Servis Kurulumu**
e-Arşiv Servis Kurulumu için yapılacaklar aşağıdaki şekildedir:

- Kurulum klasörü altında bulunan EArsivServisSetup.exe yönetici olarak çalıştırılır.
![](../_assets/600d940732f7fa8e17fa.png)
- Veritabanı bağlantısı "NETSIS" olacak şekilde seçilir. "Veritabanı Bağlantı Bilgileri Şifrelensin" işaretli ise 'Kurulum Lokasyonu' adresinde oluşturulacak olan Netsis.EarchiveSrv.exe.config dosyasında tanımlanan bağlantı bilgileri şifreli olarak oluşturulur.
![](../_assets/4bb63026a2e7775867d8.png)
- Daha sonra gelen ekrandan "kurulum başla" işlemi ile servis kurulumu tamamlanır. Servis, kurulum sonrası çalışır haldedir.

![](../_assets/8df3557166b8a4354e7b.png)
