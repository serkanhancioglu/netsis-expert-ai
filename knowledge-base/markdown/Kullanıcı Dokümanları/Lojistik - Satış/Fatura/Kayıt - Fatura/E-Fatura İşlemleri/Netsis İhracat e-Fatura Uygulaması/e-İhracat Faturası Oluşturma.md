---
title: "e-İhracat Faturası Oluşturma"
page_id: "47084861"
product: "netsis-3-enterprise"
depth: 7
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Fatura"
  - "Kayıt / Fatura"
  - "E-Fatura İşlemleri"
  - "Netsis İhracat e-Fatura Uygulaması"
  - "e-İhracat Faturası Oluşturma"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Fatura / Kayıt / Fatura / E-Fatura İşlemleri / Netsis İhracat e-Fatura Uygulaması / e-İhracat Faturası Oluşturma"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTgyYmMyYjdhLTdlNjItNGNlMC1hNTZkLWI3NDllMmUxZGQ1MSZsaW5rPWFiYTVhYWE0LTdhZGItNDY1Yi05MmNjLTUxNmMyMjMyMzE0NyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=82bc2b7a-7e62-4ce0-a56d-b749e2e1dd51&link=aba5aaa4-7adb-465b-92cc-516c22323147&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "e-ihracat-faturasi-olusturma_74714198_47084861.html"
source_version: "2022-10-24T14:29:10.670+03:00"
source_bytes: 3837
fetched_at: "2026-09-13T04:02:14+00:00"
generator: "netsis-scraper 1.0.0"
---
# e-İhracat Faturası Oluşturma

Satış irsaliyesi oluşturulduktan sonra, "Toplu e-Fatura Oluşturma" işlemi ile ihracat e-Fatura taslağı oluşturulur. e-İhracat faturası oluşturmak için, ekrandaki belge tipinin “İhracat Faturaları” olarak seçilmesi gerekir.

"Dış Ticaret" modülü kullanılıyorsa, "Toplu e-Fatura Oluşturma" işlemi ile ihracat e-Fatura taslağının oluşturulması gerekir. Belge tipi “İhracat Faturaları” olarak seçildikten sonra “Dış Ticaret Modülünden Oluşsun (Proforma)” parametresinin işaretlenmesi gerekir. Böylece proforma faturaların listelenmesi sağlanır.

Taslağı oluşturulan faturalara; Gümrük ve Ticaret Bakanlığı’nın bilgileride otomatik olarak eklenir. Girişi yapılan “Ödeme Şekli”, “Nakliye Tipi”, “Gümrük Tarife Kodu (GTİP)” “Paket Tipi” bilgileri de oluşan XML içeriğinde gönderilir.

GİB’e gönderilen e-Fatura senaryosu otomatik olarak ‘İhracat Faturası’ tipinde olacaktır.

GİB'e fatura gönderildiğinde öncelikle teknik kontrolleri yapılarak, bu kontrollerde herhangi bir sorun tespit edilmezse, GİB'den gelecek “Sistem Yanıtı” zarfında, aynı zamanda takip numarası olarak kullanılacak olan "Referans Numarası" bilgisi de gelir. Bu bilgi, "Netsis Zarf (Giden Kutusu)" ekranında "Yanıt Zarfı" bölümünden takip edilir. Aynı bilgi, GTB'nin e-Fatura portalından da kontrol edilebilir.

Eğer ihracat işlemlerinde herhangi bir sorun tespit edilmezse, GTB'ye gönderilen zarfı onaylandığında “Uygulama Yanıtı” gelir. Uygulama yanıtının içinde Netsis ihracat faturasının kapatmasında kullanılacak Gümrük Çıkış Beyanname numarası ile birlikte Fiili İhracat Tarihi bilgisi gelir.

**GTB Ref No:** Gümrük Bakanlığı’ndan gelen 23 haneli referans numarasıdır.

**GTB GÇB Tecil No:** Gümrük Çıkış Beyannamesi'nin tescil numarasıdır. Kabul tipi uygulama yanıtlarında zorunludur.

**GTB Fiili İhracat Tarihi:** İhraç mallarının gümrük çıkış kapısından çıktığı tarihtir. Kabul tipi uygulama yanıtlarında zorunludur.

Uygulama yanıtı sadece "Kabul" olarak geldiğinde, İhracat Kapatma işlemi yapılır. Uygulama yanıtı "Ret" olarak geldiğinde, yeni bir satış irsaliyesi ile ihracat e-Faturasının yeniden oluşturulması gerekir.

İhracat firmasının gönderdiği zarfları Gümrük Bakanlığı yetkilileri reddedebildiği gibi, süreci hızlandırmak için ihracat firmasının yetkilileri de sorun tespit edilecek faturaları, GTB'nin portalından reddedebilir.
