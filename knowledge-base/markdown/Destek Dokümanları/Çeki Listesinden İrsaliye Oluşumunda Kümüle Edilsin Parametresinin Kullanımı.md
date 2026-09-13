---
title: "Çeki Listesinden İrsaliye Oluşumunda Kümüle Edilsin Parametresinin Kullanımı"
page_id: "163414879"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Çeki Listesinden İrsaliye Oluşumunda Kümüle Edilsin Parametresinin Kullanımı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Çeki Listesinden İrsaliye Oluşumunda Kümüle Edilsin Parametresinin Kullanımı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTc3NDJjMWZkLWFiZWUtNDdhMy04OWM5LTNjZTkxYTg4YjI4YyZsaW5rPTc0ODIyNzBiLTk1MDktNDgyYy05M2I3LThjZjU2YmI5NzczYiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=7742c1fd-abee-47a3-89c9-3ce91a88b28c&link=7482270b-9509-482c-93b7-8cf56bb9773b&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ceki-listesinden-irsaliye-olusumunda-kumule-edilsin-parametresinin-kullanimi_163414879_163414879.html"
source_version: "2025-01-21T08:39:16.250+03:00"
source_bytes: 2066872
fetched_at: "2026-09-13T04:22:19+00:00"
generator: "netsis-scraper 1.0.0"
---
# Çeki Listesinden İrsaliye Oluşumunda Kümüle Edilsin Parametresinin Kullanımı

Dış Ticaret Parametreleri ekranına "**Çeki Listesinden İrsaliye Oluşumunda Kümüle Edilsin**" parametresi 804 setinden itibaren eklenmiştir. İhracat Dosyası içinde Çeki Listesi sekmesinde, teklif ya da sipariş belgelerinden oluşan proforma faturadaki kalemleri miktarsal olarak parçalayarak çeki listesi oluşturulabilir. Çeki listesinden irsaliye oluşturulduğunda bu parametre işaretli ise, oluşan irsaliyede miktarsal parçalama yapılan kalemler kümüle edilerek oluşur. Parametre işaretli değilse, çeki listesinde oluşturulduğu gibi kümüle edilmeden irsaliye oluşur.

![](../_assets/017d0391dbfea4121de1.png)

Bir örnek yardımıyla parametrenin işleyişine bakalım.

5 birimlik 01 kodlu bir stok kalemi için bir müşteri siparişi girilir. Bu girilen müşteri siparişi İhracat Dosya İşlemleri ekranında ihracat dosyasına bağlanarak proforma fatura oluşturulur.

![](../_assets/e4f9cbabb8e2c215c4f4.png)

![](../_assets/e941bdea2d4cbb7c7b4f.png)

Oluşan proforma fatura detayına girildiğinde, Çeki Listesi sekmesinde Kalem Listesi kısmında proforma faturada yer alan stok kalemleri listelenir.

![](../_assets/9ce450a3ed440db26644.png)

Bu bölümden ilgili stok kalemi seçilerek 2,2,1 miktar olacak şekilde parçalanarak çeki listesi oluşturulur ve kaydedilir. Ardından Çeki Listesinden irsaliye oluşturulur.

![](../_assets/dfc2fd59a5c895f04e24.png)
![](../_assets/83e8b4301dc24126b01e.png)

"**Çeki** **Listesinden** **İrsaliye** **Oluşumunda** **Kümüle** **Edilsin**" parametresi işaretli olduğunda, oluşan irsaliyede miktarsal olarak parçalanarak girilen stok kalemi kümüle olarak oluşur.

![](../_assets/49a37f6b4485dc5317d3.png)

Parametre işaretli olmadığında oluşan irsaliyede çeki listesinde miktarsal olarak parçalanarak oluşan stok kalemleri kümüle edilmeden oluşmaktadır.

![](../_assets/8af500cf34bae8b7469d.png)
