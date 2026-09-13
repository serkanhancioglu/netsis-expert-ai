---
title: "MRP - Satıcı Siparişleri İçin Dış Ticaret Uygulamasıyla Entegre Yoldaki Miktar Desteği"
page_id: "50684704"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "MRP - Satıcı Siparişleri İçin Dış Ticaret Uygulamasıyla Entegre Yoldaki Miktar Desteği"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / MRP - Satıcı Siparişleri İçin Dış Ticaret Uygulamasıyla Entegre Yoldaki Miktar Desteği"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTI2YTljZTE2LTQ1Y2ItNDkxYi04ZjA4LTYxNzFmNTlmMjQxYyZsaW5rPWJhOWUzNzk0LWRhOTEtNDQ1My04YWQzLWMzOTcwYWRjZjk5NiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=26a9ce16-45cb-491b-8f08-6171f59f241c&link=ba9e3794-da91-4453-8ad3-c3970adcf996&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "mrp-satici-siparisleri-icin-dis-ticaret-uygulamasiyla-entegre-yoldaki-miktar-destegi_90669785_50684704.html"
source_version: "2022-11-03T09:57:38.890+03:00"
source_bytes: 465409
fetched_at: "2026-09-13T04:26:32+00:00"
generator: "netsis-scraper 1.0.0"
---
# MRP - Satıcı Siparişleri İçin Dış Ticaret Uygulamasıyla Entegre Yoldaki Miktar Desteği

MRP-Satıcı Siparişleri İçin Dış Ticaret Uygulamasıyla Entegre Yoldaki Miktar ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

MRP modülünde yola çıkmış olan satıcı siparişlerine ait yoldaki miktarın dikkate alınabilmesi için dış ticaret/ithalat uygulamasıyla entegre çalışabilen bir yapı bulunur. Bu yapı sayesinde MRP sonucunda satıcı siparişi önerileri aşamasında yoldaki miktarı sıfırdan büyük olan satıcı siparişleri için gerekli kontroller yapılır ve sistem aşağıdaki şekilde davranır:

- Satıcı sipariş kaleminin miktarı yoldaki miktarın altına düşürülmemektedir.
- Satıcı sipariş kalemi için teslim tarihi bilgisi sabitlenmektedir.

Herhangi bir satıcı siparişinin yola çıktığını göstermek için dış ticaret modülünde ithalat uygulaması üzerinden satıcı sipariş kalemi için sevk belgesi hazırlanmalı ve ithalat faturalarının oluşturulması gerekmektedir. Bu durumda ilgili satıcı sipariş kalemi stoklara giriş yapmamakta ancak yoldaki miktar olarak tanımlanmaktadır.

![](../_assets/52593ed242146089a3b0.png)

![](../_assets/3f0c1171da1366b9fc1d.png)

Dış ticaret/ithalat uygulamasının haricinde yurtdışı tipli satıcı siparişlerinin yola çıktığını belirtebilmek amacıyla Fatura/Alış parametreleri/İthalat sekmesindeki "Yurt dışı tipli alış irsaliyelerinde miktarlar stoklara geçsin" parametresi de kullanılabilmektedir. Bu parametrenin işaretli olmadığı durumda yurtdışı tipli bir satıcı siparişine alış irsaliyesi girildiğinde miktarlar stok hareketlerine geçmemekte fakat satıcı sipariş kaleminin yola çıktığı anlaşılmaktadır.

MRP'de yoldaki miktar desteği yukarıda bahsedilen iki kullanım şekli için de desteklenmektedir. MRP'de yoldaki miktar uygulamasının kullanılabilmesi için MRP modül parametrelerinden "sipariş bazında rezervasyon sistemi" parametresinin seçili olması gerekmektedir.

![](../_assets/6d6f1853fbc577af81d6.png)

Yoldaki miktar uygulamasının kullanılabilmesi için Dış Ticaret ve Fatura parametrelerinde Yurt Dışı Tipli Alış irsaliyelerinde Miktarlar Stoklara Geçsin parametresi işaretli olmamalıdır.

![](../_assets/7a5c5dca9dd896f15a9e.png)
