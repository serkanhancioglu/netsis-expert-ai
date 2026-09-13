---
title: "Zamanlanmış Görevler Sıkça Sorulan Sorular"
page_id: "50687671"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Zamanlanmış Görevler Sıkça Sorulan Sorular"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Zamanlanmış Görevler Sıkça Sorulan Sorular"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTkxODE1MTJlLWY4YzItNDMyYS04ZDhkLTBlYTZmNzJjY2FhYiZsaW5rPTZmNmYwMDQ5LWEzNWMtNGExNS1hYjM0LTAwYjNiNWU5N2E1ZCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=9181512e-f8c2-432a-8d8d-0ea6f72ccaab&link=6f6f0049-a35c-4a15-ab34-00b3b5e97a5d&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "zamanlanmis-gorevler-sikca-sorulan-sorular_80090447_50687671.html"
source_version: "2022-12-09T14:08:41.670+03:00"
source_bytes: 11280
fetched_at: "2026-09-13T04:25:17+00:00"
generator: "netsis-scraper 1.0.0"
---
# Zamanlanmış Görevler Sıkça Sorulan Sorular

**Zamanlanmış görevler eklentisi ne amaçla kullanılır?**

Zamanlanmış görevler eklentisi ile istenilen uygulama, ön tanımlı işlem veya raporların sunucu arka planında 7x24 çalışması sağlanmaktadır. Böylece, bilgisayar başında olunmayan zamanlarda belirli işlemlerin periyodik olan veya istenilen bir zaman diliminde çalıştırılması sağlanabilir.

**Zamanlanmış görevler eklentisi Netsis Standard veya Entegre çözümleri ile kullanılabilir mi?**

Zamanlanmış görevler desteği için bir paket kısıtlaması yoktur. Tüm paketlerde kullanılabilmektedir.

**Zamanlanmış görevler eklentisi Hangi netsis sürümleri ile** **çalışmaktadır?**

Netsis 3 9.0.27 ve üzeri tüm sürümlerde desteklenmektedir.

**Zamanlanmış görevler eklentisi ile ne gibi işlemler gerçekleştirebilir?**

Ön tanımlı işlemler seçeneğinde gelen tüm işlemlerin istenilen zamanlarda çalıştırılması sağlanabilir. Bu işlemler Netsis 3 9.0.31 sürümü itibari ile; Gereksinim Planı Oluşturma, Malzeme Gereksinim Planlama, Maliyet Oluşturma, Maliyet Muhasebesi, Döviz Kurları Güncelleme, Stok Hareket Kontrol, İleri Üretim Çizelgeleme, e-Fatura Sorgulama, Cari Hareket Kontrolü, Yevmiye Kontrol, Veritabanı Bakım İşlemleri, Yeni Tanıtım Videosu Kontrolü, Yeni Sürüm Kontrolü, TCMB Nanka Kodları Online Güncelleme, Kuyruktaki e- Postaları Gönderme, Kişisel Verileri Anonimleştirme, Stok Döviz Çevrim, Muhasebe Döviz Çevrim, e-Belge Cari Güncelleme, Açık Reçete Analizi işlemleridir. Ayrıca sunucu üzerindeki exe veya bat uzantılı belirli bir uygulamanın çalıştırılması için uygulama çalıştır desteği bulunmaktadır. Rapor çalıştır seçeneği ile daha önce kaydedilen bir raporun taslak no rehberinden seçimi yapılarak istenilen zamanlarda otomatik çalıştırılması sağlanabilir. Script seçeneği ile; dinamik kodlama ile script dili kullanılarak istenilen scriptlerin belirli zamanlarda çalıştırılması sağlanabilir. Rest seçeneği ile; rest tipinde zamanlanmış görev tanımlaması yapılabilir.

**Serbest rapor menüsünden oluşturulan bir raporun zamanlanmış görev eklentisi ile çalıştırılması mümkün mü?**

Modül raporlarında olduğu gibi serbest raporlarda taslak olarak kaydedilerek zamanlanmış görevlere eklenebilir.

**Zamanlarmış görevlerde çalıştırılan bir rapor içeriği e-posta olarak gönderilebilir mi?**

Tanımlanan görev için görev tanımı ekranından mail seçiminin yapılması halinde belirtilen kullanıcılara e-posta gönderimi sağlanmaktadır. Aynı zamanda diğer işlemler içinde mail alanı işaretlenerek istenilen kullanıcılara mail gönderimleri sağlanabilir.

**Ön tanımlı işlemlerde yer alan veritabanı bakım işlemi ne amaçla kullanılmaktadır?**

Veritabanı bakım işlemi istenilen bir tablo bazında (opsiyonel) veya tüm veritabanında index fragmantasyon oranları tespit ederek fragmantasyon oranı yüksek indexler için rebuild ve reorganize işlemlerini gerçekleştirmektedir. Aynı zamanda opsiyonel olarak index defragmantasyonu ile birlikte istatistiklerin güncellenmesi mümkündür.

**Eklenti açılışında A host is a required uyarısı neden alınmaktadır?**

Sunucu üzerinde Netsis.Notification.WinService.exe çalışmadığında belirtilen uyarı alınmaktadır. Görev yöneticisi işlemler menüsünden exe'nin çalışır durumda olduğundan emin olunmalıdır.

**Eklentiyi kullanabilmek için sistem ve uygulama gereksinimleri nelerdir?**

SSO kurulu sunucuda minimum .Net Framework 4.6 sürümü kurulu olmalıdır. Firewall'de Notification servisin kullandığı iletişim portuna bir engelleme olmamalıdır. SSO sürümü Temelset sürümü ile uyumlu olmalı ve minimum Netsis 9.0.27 sürümü kullanılıyor olmalıdır.

**Eklenti hangi portu kullanmaktadır?**

Zamanlanmış görevler eklentisi 2024 portu ile çalışmaktadır. Bu port ile ilgili bir kısıtlama olmaması önerilir.

**Zamanlanmış görevlerde alınan hata ile ilgili uygulama logları nasıl görüntülenir?**

Eklenti ile ilgili tüm loglar …:\\Program Files (x86)\\Logo\\Merkezi Yönetim\\SsoService\\Notification\\log dizinine text dosyası olarak kaydedilir.

**Tanımlanan bir görevin çalışma zamanları ile ilgili geçmiş bilgiler görüntülebilir mi?**

Zamanlanmış görevler widget ekranında istenilen görevin üzerinde sağ klik yapılarak geçmişi göster seçeneği ile görevin ne zaman çalıştığı ile ilgili tüm bilgiler görüntülenebilir.

**Zamanlanmış görevler ile gönderilen e-postaların loglarının takibi mümkün müdür?**

Bunun için yardımcı programlardan e-posta log rapor kullanılmalıdır. Rapor parametrelerinde modül no rehberinde 1000-Netsis Widget seçeneği işaretlenerek eklenti tarafından gönderilen e- postaların log kayıtlarının raporlanması sağlanabilir.

**Öncül görev tanımı nedir?**

Kayıtlı birden çok zamanlanmış görev bulunması durumunda bazı görevlerin çalışması, başka görevlerin çalışıp tamamlanmasına bağlı olabilir. Örneğin sistemde hem malzeme gereksinim planlama hem de gereksinim planlama oluşturma görevleri tanımlı olabilir. Standart kullanımda Malzeme Gereksinim Planlama görevi çalıştırılmadan önce, Gereksinim Planlama Oluşturma görevinin çalıştırılması gerekecektir. Bu durumda Malzeme Gereksinim Planlama görevinin "Öncül Görev" alanına Gereksinim Planlama Oluşturma görevi rehber alan kullanılarak tanımlanmalıdır. Ya da benzer şekilde zamanlanmış görev olarak alınan bir rapor olabilir ancak bu rapor alınmadan önce Döviz Kurları Güncelleme görevinin tamamlanması gerekebilir. Bu durumda da ilgili rapor görevinin öncül görevi Döviz Kurları Güncelleme olacaktır. Zamanlanmış görevler uygulaması her bir görev için "Öncül Görev" kontrolü yaparak çalışmaktadır.

**Netsis.Notification.WinService.exe'nin SSO servisinden bağımsız olarak yeniden başlatılması mümkün mü?**

Şu an için desteklenmemektedir. Netsis.Notification.WinService.exe SSO servisine bağlı bir uygulamadır. Ancak uygulamanın SSO servisinden bağımsız olarak yeniden başlatılmasını içeren yenilik mevcut planlarımızda bulunmakta olup ilerleyen dönemde yeniliğin desteklenmesi sağlanacaktır.

**Birden fazla şirket için zamanlanmış görevler kullanılabilir mi?**

Tanımlanan görevler şirket bazında tanımlanmakta olup her bir şirket için farklı görevlerin tanımlanarak çalıştırılması mümkündür.

**Script desteği nasıl kullanılır?**

Script özelliği için Netsiscore nesnesine ulaşılarak yazılan script kodun çalıştırılması sağlanabilir. Örneğin SQL üzerinde tanımlı bir prosedürün belirli periyodlarda çalıştırılması isteniyor. Bunun için görev tipinden script seçilerek script girişi alanına istenen kod bloğu yazılmalıdır. Örnek olarak aşağıda belirtilen kod örneği ile SP_CALISTIR adındaki prosedürün zamanlanmış görev ile çalıştırılması sağlanabilir.
SET QRY = NETSISCORE.NetLibDB.GetNewQuery QRY.RECSQL(("EXEC SP_CALISTIR"))
