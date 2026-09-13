---
title: "NetUpdate Uygulaması"
page_id: "50679943"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "NetUpdate Uygulaması"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / NetUpdate Uygulaması"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTcyZTQ0ZWUzLWQ2MzktNDQ2ZS04NWQ5LTBiOTcxNjgxMzYyOCZsaW5rPWZjODRiMDAyLWFmZmMtNDBlOC05ZWI5LTc3MDE5NjQ5MzgyOSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=72e44ee3-d639-446e-85d9-0b9716813628&link=fc84b002-affc-40e8-9eb9-770196493829&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netupdate-uygulamasi_82576135_50679943.html"
source_version: "2022-11-03T09:28:59.217+03:00"
source_bytes: 6116594
fetched_at: "2026-09-13T04:26:02+00:00"
generator: "netsis-scraper 1.0.0"
---
# NetUpdate Uygulaması

NetUpdate Uygulaması ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

NetUpdate Uygulaması kullanım dokümanı bilgileri aşağıdaki şekildedir:

- Mevcut setlere (9.0.3, 9.0.4 ve sonrası) ilave olarak çıkarılan ara setlerde (9.0.4.1, 9.0.4.2, ) yapılan düzeltme ve geliştirmelerin aktif olabilmesi için Netsis klasörü Servis dizinine ***"NetUpdate.exe"*** uygulaması eklenmiştir. Ara set dosyalarını manuel kopyalamak yerine, bu uygulama ile eski dosyalar otomatik olarak yeni ara set dosyalarıyla güncellenecektir.
- Uygulamanın kullanılabilmesi için; ilgili set klasörü içerisinde .rar dosya olarak bulunan ara set dosyasının, Netsis dizini ana set klasörüne indirilmesi gerekir.

![](../_assets/d35a0f349abca2765e11.png)

Uygulama Adımları aşağıdaki şekildedir:

- Servis dizini NetUpdate.exe, sağ click "Run as Administrator" ile admin olarak çalıştırılır. Açılan pencere, Merkezi Kimlik Yönetimi uygulamasının girişinde gelen ekrandır. Merkezi Kimlik Yönetimi uygulamasını kullanırken girdiğiniz Kullanıcı Adı ve Şifre bilgilerini giriniz.

![](../_assets/a198de33e0be6457173f.png)

- Giriş yapıldıktan sonra resimdeki ekran açılır. Mevcutta kurulu olan sete ek olarak çıkarılmış patch dosyaları listelenmiş olarak gelir.

![](../_assets/cebefb8a6b5acc15d2fd.png)

- Üst panelde bulunan Ürün Fark Bilgileri menüsüne tıklanarak; yapılan geliştirmeler, düzeltmeler ve nedenleri görülebilir.

![](../_assets/c12b5ed4392bbdb87a43.png)

- " ? " bulunan satırlarda soru işaretine tıklanarak, ilgili dosya güncellenmesine istinaden yapılan geliştirmeler, düzeltmeler ve nedenleri görülebilir.

![](../_assets/1376bb8e4d1347636d94.png)

![](../_assets/526ec2276b2346ab7c2c.png)

- Üst panelde bulunan Aktif Kullanıcılar menüsü ile aktif oturumlar listelenecek ve halihazırda aktif kullanıcı/kullanıcılar varsa güncellemeye izin verilmeyecektir.

![](../_assets/30470fde6aad0246ac13.png)

- Üst panelde bulunan Güncelleme sonrası menüsü ile "Güncelle" işlemi tıklandığında yapılacak işlemler listelenir. Bu işlemler Sso kurulumu, Dbupdate veya .tlb dosyalarında değişiklik varsa RegKontrol olabilir. Burada listelenen işlemler, dosya değişimleri sonrası bu uygulama tarafından otomatik olarak tetiklenecektir.

![](../_assets/db9cb071e7cddd0b64ab.png)

- Güncelleme menüsü tıklandığında, Güncelleme işlemi alt panelden takip edilebilir.

![](../_assets/fb7b91c3d66031d1831e.png)

- Güncelleme sonrası, gelen bilgi kutucuğundan işlem sonucu görülür.

![](../_assets/beeff14c753e983bbeb5.png)

- Açılan bilgi kutucuğu kapatılınca, Dbupdate ekranı gelir. Dbupdate işlemi çalıştırılır.

![](../_assets/cb74891c40b513fd5293.png)

- Dbupdate işleminin tamamlanmasının ardından, Merkezi Kimlik Yönetimi kurulum uygulaması ekrana gelir. Güncelleme işlemi yapılır.

![](../_assets/5ffe90a5033ed5eb5ebb.png)

- Merkezi Kimlik Yönetimi güncellenmesinin tamamlanmasının ardından, üst panelde bulunan Yenile menüsü tıklandığında Durum bilgisinin "Güncellenebilir" statüsünden "Güncel" statüsüne geçtiği görülür.

![](../_assets/8b44e38c75f3731a125f.png)

- Ek olarak, .tlb dosyası değişikliği varsa RegKontrol işlemi tetiklenecektir.
