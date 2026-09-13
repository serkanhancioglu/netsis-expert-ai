---
title: "Netsis Gümüş Uygulaması Desteği"
page_id: "50690632"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis Gümüş Uygulaması Desteği"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis Gümüş Uygulaması Desteği"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTdjMTIyZTUyLTgwNTktNGM4OC04NjBjLTEwYmJhMjI2NTM3NSZsaW5rPWZlNzY4YzI5LTdjYTgtNDdkZi1hYWFlLTBlYTcxMDJlOGFhNiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=7c122e52-8059-4c88-860c-10bba2265375&link=fe768c29-7ca8-47df-aaae-0ea7102e8aa6&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-gumus-uygulamasi-destegi_80090288_50690632.html"
source_version: "2022-11-02T16:09:30.127+03:00"
source_bytes: 506055
fetched_at: "2026-09-13T04:25:10+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis Gümüş Uygulaması Desteği

Netsis Gümüş Uygulaması ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Gümüş uygulaması ile satılan ürünün kullanım oranı kadar KDV'den muaf olması sağlanır. Bu uygulamanın kullanılabilmesi için; Yardımcı Programlar/Özel parametreler bölümünden tanım yapılmalıdır.

Grup kodu = FATURA

Anahtar= GUMUSTEVKIFATUYGULAMASI

Değer= 0

![](../_assets/a7369048cb583d0d11f5.png)

Bu özel parametre tanımlandıktan sonra stok kartı kayıtlarında "Kullanım Oranı" sahası görünecektir ve kullanım oranı mutlaka ilgili ürün için tanımlanmalıdır.

![](../_assets/12332b6eaae0b812d348.png)

Ayrıca özel parametrenin tanımlanması ile birlikte belge girişi yaparken (Sipariş/İrsaliye/Fatura) kalem bilgileri alanında "Özel Fiyat" alanı açılmaktadır.

*Gümüş uygulaması için belgenin "KDV Hariç" kesilmesi gerekmektedir.*
Aşağıdaki gibi bir örnek üzerinden KDV hesaplaması şu şekilde yapılmaktadır: Kdv oranı = %18
Kullanım oranı=%20
Birim Fiyat=842
Özel fiyat= 1095 (işçilik dahil fiyatı)
Miktar= 5 Kg

![](../_assets/616bf5053bc49117331d.png)

1095X 0,20= 219
842-219= 623
623X5X0,18=560,7 olarak kdv hesabı yapılmaktadır.

![](../_assets/6a64b30c6b58dec69d85.png)

Belgeyi kaydettikten sonra oluşan muhasebe kaydı ise aşağıdaki gibidir;

![](../_assets/50d3287963068ed7a57a.png)
