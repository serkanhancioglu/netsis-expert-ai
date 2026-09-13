---
title: "Envanter Defterinin e-Defter Olarak Gönderilmesi"
page_id: ""
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Envanter Defterinin e-Defter Olarak Gönderilmesi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Envanter Defterinin e-Defter Olarak Gönderilmesi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTAyMTViODA4LWIwZjctNGU1ZS04ZTdmLTM3MjY2MDc1YTNhYSZsaW5rPWZkYzE2Y2ZjLTNkZWMtNDYwYi1hZTZhLWNhNzE4ZmIxMTYyYyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=0215b808-b0f7-4e5e-8e7f-37266075a3aa&link=fdc16cfc-3dec-460b-ae6a-ca718fb1162c&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "envanter-defterinin-e-defter-olarak-gonderilmesi.html"
source_version: ""
source_bytes: 5033
fetched_at: "2026-09-13T04:21:45+00:00"
generator: "netsis-scraper 1.0.0"
---
# Envanter Defterinin e-Defter Olarak Gönderilmesi

Dijital dönüşüm ve e-Dönüşüm süreçlerinin bir parçası olarak, Gelir İdaresi Başkanlığı (GİB) tarafından yayımlanan Vergi Usul Kanunu (VUK) Genel Tebliğleri doğrultusunda, e-Defter uygulamasına dahil olan mükelleflerin yevmiye ve defter-i kebir dışındaki diğer yasal defterlerinin de elektronik ortamda tutulması, beratlarının alınması süreçleri kademeli olarak zorunlu hale getirilmektedir.

Bu kapsamda, işletmelerin dönem başı ve dönem sonu finansal durumlarını, varlıklarını ve borçlarını detaylı olarak gösteren Envanter Defteri, artık e-Defter standartlarına uygun olarak elektronik ortamda oluşturulabilmektedir. Yasal mevzuata göre Envanter Defteri;

• Dönem Başı Açılış Bilgileri (Ocak ayı veya özel hesap döneminin ilk ayı) ve

• Dönem Sonu Kapanış/Envanter Bilgileri (Aralık ayı veya özel hesap döneminin son ayı)

esas alınarak yılda iki kez GİB platformuna e-defter formatında iletilmelidir.

Bu yasal düzenlemelere uyum çalışmaları kapsamında, **9.0.70.5** ve **9.0.71.2** sürümleri ile birlikte; **Envanter Defteri** gönderimi desteklenmiştir. Kullanıcı tarafında iş yükü yaratmayacak şekilde tasarlanan bu yenilikle birlikte, süreç mevcut e-Defter hazırlama adımlarına bağlanmıştır.

Sistemde yapılan geliştirmeler ve operasyonel akış şu şekildedir:

##### Mükellef ve Düzenleyen Bilgileri

Sürecin aktif hale getirilebilmesi için Muhasebe modülünde yer alan Mükellef ve Düzenleyen Bilgileri Defter Bilgileri ekranında bulunan Envanter Defteri Oluşturulsun parametresi işaretlenir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/d4d11d0a-6d4d-4b61-b9d7-2f93a1682502/es_envanter_mukellefduzenleyen.jpg)

##### Otomatik Envanter Defteri Oluşturma Mantığı

Parametre işaretlendikten sonra, sistem arka planda yasal takvimi otomatik olarak yönetir. Kullanıcının her ay ekstra bir işlem yapmasına gerek kalmaz.

**• Ocak Ayı:** Kullanıcı rutin e-Defter oluşturma işlemini başlattığında, sistem yasal gereksinim sebebi ile Yevmiye ve Kebir defterlerinin yanı sıra Envanter Defterini de otomatik olarak paketler.

**• Aralık Ayı:** Dönem sonu kapanış işlemlerinin bir parçası olarak Aralık ayı defterleri oluşturulurken, sistem yine otomatik olarak Envanter Defterini sürece dahil eder.

**• Diğer Aylar (Şubat - Kasım):** Bu aylarda envanter defteri oluşturulması yasal olarak gerekmediğinden, sistem mevcut standart akışında (Yevmiye ve Kebir) çalışmaya devam eder.

Ocak ve Aralık ayında yapılan E-Defter Oluştur işleminde, E-Defter Listesinde Envanter Defteri oluşur. Envanter defteri Ocak ayı için Açılış Fişi, Aralık ayı için Kapanış Fişi baz alınarak oluşur. İlgili ayda girilen diğer kayıtlar envanter defterindeki tutarları etkilemez.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/286d7517-3564-4e1a-a13e-e2a5f555877b/es_envanter_defterlist (2).jpg)

E-Defter Zip Dosyası İndir işleminde, defter dizininde envanter defterine ait VKN/TCKN-Dönem-EB-Parça numarası formatında zip klasörü oluşur. Bu dosyanın içerisinde hem envanter beratı hem de envanter defteri yer alır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/2561643b-12b8-482c-8cc9-51c943cb6923/es_envanter_dosyadizin.jpg)

E-Defter Görüntüle işleminde, HTML formatta envanter beratı ve envanter defteri görüntülenir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/1c76c2f7-bf72-48a4-b6a5-bce96b40b636/es_envanter_berathtml.jpg)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/a493d824-aecd-4259-8520-866b8d05d0e6/es_envanter_envanterhtml.jpg)
