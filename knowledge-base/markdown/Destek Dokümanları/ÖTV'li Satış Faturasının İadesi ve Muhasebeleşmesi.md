---
title: "ÖTV'li Satış Faturasının İadesi ve Muhasebeleşmesi"
page_id: "108659178"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "ÖTV'li Satış Faturasının İadesi ve Muhasebeleşmesi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / ÖTV'li Satış Faturasının İadesi ve Muhasebeleşmesi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTA0YmVjMWYyLTg2ZjEtNDgzZi05YWZmLWVhYmZkYWMxODkzOSZsaW5rPWYyMTdkMjFmLTEwNzUtNGE5ZS1hZWZjLWY1NWYzOTU4MzBmZCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=04bec1f2-86f1-483f-9aff-eabfdac18939&link=f217d21f-1075-4a9e-aefc-f55f395830fd&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "otv-li-satis-faturasinin-iadesi-ve-muhasebelesmesi_108659186_108659178.html"
source_version: "2023-03-31T09:02:12.643+03:00"
source_bytes: 3074210
fetched_at: "2026-09-13T04:23:35+00:00"
generator: "netsis-scraper 1.0.0"
---
# ÖTV'li Satış Faturasının İadesi ve Muhasebeleşmesi

Logo Netsis içerisinde ÖTV'li girilen satış faturasının iadesi "İADE" tipli alış faturası girilerek yapılmaktadır. ÖTV'li satış faturasının iadesi ve muhasebeleşmesi hakkında ayrıntılı bilgiye bu dokümandan ulaşılır. İade tipli girilen alış faturasında toplamlar sekmesinde ÖTV tutarı yazmakta ve ilgili iade ÖTV hesabında takip edilmektedir. Uygulama ve işlem adımlarını bir örnekle açıklayalım.

ÖTV' li bir satış faturası giriliyor. Birim fiyatı 500 tl %8 kdv ve %10 ÖTV miktar:1

Stok Kartı kayıtları Ek Bilgiler sekmesinde ÖTV Satış için işaretlenir ve Oran seçilip, Tutar/Oran alanına 10 girilir.

![](../_assets/742fe7ae18088e2dcca6.png)

Satış faturası Toplamlar sekmesinde ÖTV tutarı 50 olarak hesaplanmıştır. Brüt toplam üzerinden %10 ÖTV (500/100\*10) =50 tl

![](../_assets/d1b71e3169a56c19d8a9.png)

Satışta hesaplanan ÖTV tutarı, Entegrasyon Kodları/Fatura Ek maliyet sekmesinde Satış kısmında ÖTV Hesabı alanına girilen muhasebe hesabına atılır. ÖTV Satış Kodu boş bırakılmalıdır. Boş bırakılmadığı durumda ÖTV hesabı dolu olsa bile, ÖTV tutarı stoklar için tanımlanan muhasebe detay kod girişinde girilen muhasebe hesaplarına atılmaktadır.

![](../_assets/1e8a605f31b3f70eabc9.png)![](../_assets/b6e905e4537ccb306fdc.png)

Girilen ÖTV' li satış faturasının iadesi, iade tipli alış faturası girilerek sağlanır. Alış faturası üst bilgilerde Tipi: İade seçilir. Sonrasında iade edilecek ÖTVli stok kodu girilir. Toplamlar sekmesinde iade tipli alış faturasında da ÖTV tutarı hesaplanmaktadır.

![](../_assets/68431218fe4372581d88.png)![](../_assets/83f1d08f302c2185006b.png)

Satılan ÖTV' li ürünün iadesinde hesaplanan ÖTV tutarı Entegrasyon Kodları/Fatura Ek maliyet sekmesinde Alış kısmında İade ÖTV Hesabı alanına girilen muhasebe hesabına atılır. ÖTV Satış Kodu boş bırakılmalıdır.

![](../_assets/1e8a605f31b3f70eabc9.png)

![](../_assets/7cf0567e312dc9d2fd53.png)
