---
title: "Netsis Temel Mükellef Bilgileri Sorgulama (TÜRMOB)"
page_id: "87032121"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis Temel Mükellef Bilgileri Sorgulama (TÜRMOB)"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis Temel Mükellef Bilgileri Sorgulama (TÜRMOB)"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTg2ZDdkN2Q3LTkxMjAtNGM4Yy1iOTg0LWU3MmYzMzM0YmEzZSZsaW5rPThiOGI2YjYwLWJkZGMtNDc4Zi1iMTFmLTRhZmQ2YTJhYWMwMCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=86d7d7d7-9120-4c8c-b984-e72f3334ba3e&link=8b8b6b60-bddc-478f-b11f-4afd6a2aac00&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-temel-mukellef-bilgileri-sorgulama-turmob_90670164_87032121.html"
source_version: "2022-12-13T14:16:44.010+03:00"
source_bytes: 1297623
fetched_at: "2026-09-13T04:24:02+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis Temel Mükellef Bilgileri Sorgulama (TÜRMOB)

Netsis Temel Mükellef Bilgileri Sorgulama (TÜRMOB) ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

**9.0.39** setiyle birlikte Türkiye Mali Müşavirler Odaları Birliği'nin (TÜRMOB) desteklediği temel mükellef bilgileri sorgulama servisi ile yapılan entegrasyon desteği sağlanmıştır ve entegrasyon daha önceki sürümlerde aynı işlevi göre Noterler Birliği Servisi ile yapılan entegrasyonun yerini almaktadır.

Cari Parametreleri ekranında **Cari** **İsim** **Sorgulama** **Kaynağı** kısmına Noterler Birliği seçeneği yerine **TÜRMOB** seçeneği eklenmiştir. Bu seçenek sadece **Standard** ve **Enterprise** paketlerde aktif olmakta ancak 9.0.44 setinden itibaren Entegre paketinde de desteklenmiştir.

![](../_assets/acff769836b0e3ca7df3.png)

TÜRMOB seçeneği seçildikten sonra **TÜRMOB** **Bağlantı** **Bilgileri** kısmı doldurulmalıdır. Bu bölümde TÜRMOB tarafından kullanıcılara verilen Anahtar bilgisi **Token** alanına yazılmalıdır.

TÜRMOB bağlantı bilgileri kaydedildikten sonra Cari Hesap Kayıtları ekranında, temel mükellefi bilgileri sorgulanmak istenen cari seçildikten sonra cari rehber butonunun yanında olan TÜRMOB Servisinden Sorgula butonu tıklanır. Butona tıklandığında "**Cari bilgileri güncellenecektir, devam** **etmek** **istiyor** **musunuz?**" uyarı mesajı çıkmaktadır. Bu uyarıya "**Evet**" denilerek geçilir.

![](../_assets/21e4617ab4a6846eb977.png)

Bu buton yardımıyla cariye ait vergi kimlik numarası veya tc kimlik numarası üzerinden TÜRMOB servisi üzerinden temel mükellef bilgileri sorgulanmakta ve ekrana cari isim, adres, il, ilçe, vergi dairesi, vb bilgiler getirilmektedir. Böylece cariye ait bilgiler güncellenmiş olmaktadır.

![](../_assets/850a9a7d28970cb2d2ed.png)

![](../_assets/bb2f42a698d181116026.png)

Cari hesap kayıtlarında Türmob servis sorgulaması sırasında en çok alınan "Error connecting with SSL. Error 140770FC: SSL routines: SSL23_GET_SERVER_HELLO: unknown protocol" uyarısı alındığında aşağıdaki işlem adımları kontrol edilebilir.

![](../_assets/6e5d1a6acb7bbebf03e4.png)

Mükellef bilgileri sorgulama entegrasyonunda erişim olması gereken adresler şunlardır:

- [https://ebirlik.turmob.org.tr/](https://ebirlik.turmob.org.tr/+)[https://service1.turmob.org.tr/?ReturnUrl=https://ebirlik.turmob.or](https://service1.turmob.org.tr/?ReturnUrl=https://ebirlik.turmob.or) [g.tr/AccountManager](http://g.tr/AccountManager)
- [https://service2.turmob.org.tr/?ReturnUrl=https://ebirlik.turmob.org.tr/AccountManager?Retur](https://service2.turmob.org.tr/?ReturnUrl=https://ebirlik.turmob.org.tr/AccountManager?Retur) nUrl=/External/Credentials

TLS 1.2'nin hem client makinada hem de sunucuda aktif olması gerekmektedir. Sunucu ve istemci makinalarda TLS 1.2 aktif edilebilmesi için aşağıdaki linklerdeki işlem adımları takip edilebilir.

[https://docs.microsoft.com/tr-tr/mem/configmgr/core/plan-design/security/enable-tls-1-2-server](https://docs.microsoft.com/tr-tr/mem/configmgr/core/plan-design/security/enable-tls-1-2-server+)

[https://docs.microsoft.com/tr-tr/mem/configmgr/core/plan-design/security/enable-tls-1-2-client](https://docs.microsoft.com/tr-tr/mem/configmgr/core/plan-design/security/enable-tls-1-2-client+)

Bu servisin çalışabilmesi için işletim sistemi Windows 8 ve üstü olmalıdır.

Netsis versiyonunu için minimum 9.0.38 seti olmalıdır.

Temelset klasörü altındaki ssleay32.dll ve libeay32.dll dosyalarının tarihlerinin 2018 tarihli güncel dosyalar olması gerekiyor.
