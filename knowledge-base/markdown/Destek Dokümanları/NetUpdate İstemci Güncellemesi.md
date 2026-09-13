---
title: "NetUpdate İstemci Güncellemesi"
page_id: "153158815"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "NetUpdate İstemci Güncellemesi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / NetUpdate İstemci Güncellemesi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWYwMDJjZGMyLTNhMGQtNDQyMy1iOWNjLTA4ZDlkYjAwZGE0MCZsaW5rPTBkNDdmNzNmLTc5ZGEtNDlmYy04NTRlLTlkNGZkZjczZmIxYiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=f002cdc2-3a0d-4423-b9cc-08d9db00da40&link=0d47f73f-79da-49fc-854e-9d4fdf73fb1b&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netupdate-istemci-guncellemesi_153158815_153158815.html"
source_version: "2024-10-14T10:21:45.770+03:00"
source_bytes: 926881
fetched_at: "2026-09-13T04:22:33+00:00"
generator: "netsis-scraper 1.0.0"
---
# NetUpdate İstemci Güncellemesi

Netsis 9.0.57 sürümünde, NetUpdate uygulaması aracılığıyla istemci güncelleme desteği sağlanmıştır. Daha önce yalnızca sunucu güncellemelerinde kullanılan NetUpdate, artık istemcilerdeki dosyaların da güncellenmesine olanak tanımaktadır. Özellikle ağ bağlantı hızından kaynaklanan sorunlar, dosyaların sunucu üzerinden okunması durumunda performans sorunlarına yol açabilmektedir. NetUpdate v.2.0 geliştirmeleri kapsamında istemcilerin yerel dosyaları üzerinden çalışabilmesi ve dosyaların toplu şekilde güncellenmesi sağlanmıştır. Bu sayede, Netsis sunucusunda yapılan son güncellemeler tüm istemcilere iletilebilmektedir.

İstemci güncelleme desteğinin kullanılabilmesi için Netsis sürümünün 9.0.57 veya üzeri olması gerekmektedir.

Güncelleme paketlerinin oluşması için sürüm geçişi NetUpdate üzerinden gerçekleştirilmelidir.

Ayrıca, istemcilerde uygulama dosyaları ağ üzerinden çalışıyorsa, ekranın sağ üst bölümünde bir uyarı görüntülenmektedir.

![](../_assets/74caf85c3ca49f0cd0ad.png)

Ağ üzerinden çalışan istemcilerde Registry Editor'de "Netsis\\9.0\\KokDizin" yolunda ağ adresi tanımlıdır.

Diğer bir koşul ise, istemcilerde NetUpdate Service'in yüklenebilmesi için minimum 9.0.57 sürümünde RegKontrol işleminin en az bir kez çalıştırılmış olması gerekmektedir.

![](../_assets/51aeedae5b2af63902d9.png)

Güncelleme işlemi için NetUpdate Service, sunucu ve istemcilerde aktif durumda olmalıdır.

RegKontrol işlemine ait loglarda NetUpdate Service'in kurulu olup olmadığı bilgisi görüntülenebilmektedir.

![](../_assets/34152ea69e73ce3a29a7.png)

Windows Firewall açık olduğunda, gelişmiş güvenlik duvarı ayarlarında 2027 portu için gelen ve giden kurallar tanımlanmalı, bağlantı noktası TCP seçilerek 2027 portuna bağlantılara izin verilmelidir.

![](../_assets/09e95db2730ab2a75e56.png)

Sunucu güncellemesi NetUpdate ile gerçekleştirildiğinde, istemcilere gönderilecek paket dosyaları "…\\Netsis\\ENTERPRISE9\\Servis\\NetUpdateService" dizinindeki "NetUpdatePackage" klasöründe \*.zip dosyası olarak kaydedilmektedir. Bu işlem, ana sürüm ve patch güncellemeleri için güncelleme tamamlandıktan sonra gerçekleşir.

Paket dosyaları oluşturulurken, ekranın alt bölümünde *"Güncelleme dosyalarının istemci güncellemesi için yedekleniyor"* uyarısı gösterilmektedir.

![](../_assets/46b07344c38909fc1849.png)

Güncelleme paketlerinin oluşturulması tamamlandığında ekran görüntüsünde görüldüğü gibi ZIP arşiv dosyalarının belirtilen dizinde mevcut olması gerekmektedir.

![](../_assets/bb23e56fec4566926aee.png)

Eğer güncelleme paketleri oluşmadan istemci güncellemesi başlatılırsa, aşağıdaki ekran görüntüsünde yer alan uyarı mesajı alınacaktır.

![](../_assets/b5dcf5ae02bc0797a31e.png)

NetUpdate.exe sunucuda açıldığında, Yükleme Seçenekleri ekranında **"İstemci Güncelleme Yapılsın"** seçeneği görüntülenmektedir.

![](../_assets/2b6f50de406b5a518e74.png)

Bir sonraki sekmede, güncelleme işlemlerinin yönetildiği bir ekran açılmaktadır. Bu ekranda, istemcilere ve sunucuya ait makine adı, IP adresi, mevcut sürüm, online/offline durumu, son güncelleme tarihi ve güncelleme durumu gibi önemli bilgiler yer almaktadır.

**Tip** alanında istemcilere dair iki seçenek bulunmaktadır:

- ClientLocal: İstemci makinenin uygulama dosyalarını yerel kaynaklarından kullandığını belirtir.
- ClientNetwork: İstemci makinenin uygulama dosyalarını sunucu üzerinden kullandığını ifade eder.

**Online** seçeneğinde, istemci makinenin aktif olup olmadığı bilgisi gösterilmektedir. Makine bilgileri listelenirken istemcilere eşzamanlı olarak ping isteği gönderilir ve bu sayede makinenin online veya offline durumu belirlenir.

![](../_assets/ce8c2dff34bd286ea54c.png)

Eğer sunucuda NetUpdateService çalışmıyorsa, istemci güncellemesi başlatılmaya çalışıldığında "Net Update Servisine erişilemedi." uyarısı görüntülenecektir.

![](../_assets/c2de1f35863958d25d9e.png)

İstemcide NetUpdateService çalışmadığında ise, grid alanda o istemciye ait makine bilgileri listede görünmeyecektir.

**Son Güncelleme Durumu:** Güncelleme işlemi istemci için hatalı sonuçlandığında, ilgili alanda hata detaylarına erişim sağlanabilmektedir.

Grid üzerindeki sağ tık menüsünde bulunan **"Güncelleme Geçmişi"** seçeneği ile istemci bazında önceki tüm güncelleme geçmişine ait paket gönderim tarihi, güncelleme başlangıç ve bitiş zamanı, eski sürüm ve mevcut sürüm bilgilerine ulaşılabilmektedir.

![](../_assets/49e9170531822279d5d1.png)

Güncelleme işlemi, *ClientNetwork* tipindeki bir istemci için gerçekleştirildiğinde uygulama dosyaları istemcinin sistem diskine kopyalanmaktadır.

*ClientLocal* tipindeki istemcilerde ise uygulama dosyalarının güncellenmesi, istemcinin yerel dizinindeki dosyalar üzerinden gerçekleştirilmektedir.

Güncelleme işlemini başlatmak için, istemciler sol taraftaki seçim kutucuğundan veya "Tümünü Seç" menüsünden seçim yapılarak ***"Güncelle"*** butonuna tıklanmalıdır.

Güncelleme başlatıldığında, eğer istemcide Ephesus.exe açık durumdaysa kullanıcıya oturumun sonlandırılacağına dair bir bildirim gönderilir. Kullanıcı, belirtilen süre içinde oturumu kapatmadığında sistem otomatik olarak oturumu sonlandırarak güncelleme işlemi başlatılır.

![](../_assets/770a01cafbc823988fc2.png)
