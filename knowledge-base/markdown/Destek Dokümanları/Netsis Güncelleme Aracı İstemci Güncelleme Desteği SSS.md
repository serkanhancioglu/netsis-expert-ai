---
title: "Netsis Güncelleme Aracı İstemci Güncelleme Desteği SSS"
page_id: "153158840"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis Güncelleme Aracı İstemci Güncelleme Desteği SSS"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis Güncelleme Aracı İstemci Güncelleme Desteği SSS"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTZhYWUwMmQyLTlhMjgtNDQyZC04YzE3LWE2NzU3YWNjNTk0ZSZsaW5rPWY3Y2VmMGRhLTVhY2ItNDZmYS1iY2RhLTRlZjgwMmJmYzE3MyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=6aae02d2-9a28-442d-8c17-a6757acc594e&link=f7cef0da-5acb-46fa-bcda-4ef802bfc173&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-guncelleme-araci-istemci-guncelleme-destegi-sss_153158840_153158840.html"
source_version: "2024-10-14T10:28:26.230+03:00"
source_bytes: 6015
fetched_at: "2026-09-13T04:22:31+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis Güncelleme Aracı İstemci Güncelleme Desteği SSS

**İstemci güncellemelerinin yapılması zorunlu mudur? Hangi durumda yapılması tavsiye edilir?**

Zorunlu bir işlem değildir. Ağ bağlantı hızından kaynaklanan uygulamadaki performans sorunlarını minimize etmek için yapılması tavsiye edilir.

**NetUpdate istemci güncelleme desteği için hangi sürüm gereklidir?**

İstemcilerde güncelleme desteği için Netsis sürümünün en az 9.0.57 olması gerekmektedir.

**Güncelleme paketleri nasıl oluşturulur?**

Güncelleme paketlerinin oluşması için sürüm geçişinin NetUpdate üzerinden gerçekleştirilmesi gerekmektedir.

**NetUpdateService nasıl yüklenir?**

NetUpdateService 9.0.57 sürümünden itibaren RegKontrol işlemiyle yüklenmektedir.

**NetUpdateService hangi portu kullanır?**

NetUpdate Service, varsayılan olarak 2027 portunu kullanmaktadır. Eğer 2027 portu kullanımda ise, 2027 portundan itibaren boştaki 20 port bilgisi aranır. Boşta olan port bilgisi kullanılarak servis kaydedilir.

**Windows Firewall üzerinde yapılması gereken işlemler nelerdir?**

Gelişmiş Güvenlik Özellikli Windows Güvenlik Duvarı menüsünden, NetUpdateService tarafından kullanılan port için (varsayılan 2027) gelen ve giden kurallar tanımlanmalı ve bağlantılarına izin verilmelidir.

**İstemci güncelleme paketleri nereye kaydedilir?**

Güncelleme paketleri, "…\\Netsis\\ENTERPRISE9\\Servis\\NetUpdateService" dizinindeki "NetUpdatePackage" klasöründe \*.zip dosyası olarak kaydedilmektedir.

**İstemci güncellemesi için dikkat edilmesi gerekenler nelerdir?**

- NetUpdate Service'in sunucu ve istemcilerde aktif durumda olup olmadığı kontrol edilmelidir.
- Sunucu güncelleme işlemi NetUpdate üzerinden yapılmalıdır.
- Güncelleme paketlerinin "NetUpdatePackage" klasöründe bulunduğundan emin olunmalıdır.
- İstemcilerin online/offline durumu kontrol edilmelidir.
- Windows güvenlik duvarı ayarlarında servis portuna erişim izinleri verilmelidir.

**İstemci güncellemesi sırasında kullanıcıda Ephesus.exe açık durumdayken güncelleme başlatılabilir mi?**

Ephesus.exe açık durumdayken güncelleme başlatıldığında, kullanıcıya oturumun sonlandırılacağına dair bir bildirim gönderilmektedir. Kullanıcı oturumunu kapatmazsa, sistem tarafından otomatik olarak oturumu sonlandırılır.

**İstemci Güncelleme sekmesinde gösterilen ClientLocal ve ClientNetwork tipleri arasındaki fark nedir?**

ClientLocal, istemci makinenin uygulama dosyalarını yerel kaynaklardan kullandığını belirtirken, ClientNetwork sunucu üzerinden kullandığını ifade eder.

**"Netsis Update Servisine Erişilemedi" uyarısı hangi durumda alınır?**

Bu uyarı sunucuda NetUpdateService çalışmadığında, istemci güncellemesi başlatılırsa alınır. Windows Hizmetler menüsünden servisin durumu kontrol edilmelidir.

**İstemci güncelleme paketleri ne zaman oluşur?**

Güncelleme paketleri, Netsis Güncelleme Aracı kullanılarak gerçekleştirilen güncelleme işleminde, sunucu güncellemesi tamamlandıktan sonra oluşur. Bu işlem gerçekleşirken ekranın alt bölümünde "Güncelleme dosyalarının istemci güncellemesi için yedekleniyor" uyarısı gösterilmektedir.

**İstemci güncelleme paketleri manuel oluşturulabilir mi?**

Paket dosyaları, NetUpdateService tarafından otomatik olarak oluşturulmaktadır. Bu işlem sırasında veritabanı düzeyinde işlemler gerçekleşerek ilgili tablolara paket bilgileri kaydedilmektedir.

**Ağ üzerinden çalışan istemcilerde masaüstü ekranının sağ üst bölümünde yer alan "Uygulama dosyaları ağ üzerinden okunduğu için performans sorunu yaşanabilir" uyarısı gizlenebilir mi?**

Hayır. Bu uyarı, ağ üzerinden dosyaların okunduğu tüm istemcilerde gösterilen standart bir mesajdır.

**İstemci güncellemesi ile uygulama dosyaları istemciye iletilirken bir klasör oluşturulması gerekir mi?**

Hayır. ClientNetwork tipindeki bir istemci için güncelleme yapıldığında, uygulama dosyaları istemcinin sistem diskine Netsis dizini açılarak kopyalanmaktadır.
