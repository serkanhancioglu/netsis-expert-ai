---
title: "Demirbaş Parçalama Destek Dokümanı"
page_id: "160040311"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Demirbaş Parçalama Destek Dokümanı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Demirbaş Parçalama Destek Dokümanı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTk5ZmJkOWI2LWU4M2ItNGI3Ni05ZjY3LWZmYWM0OTM0N2Q4ZiZsaW5rPTEwY2EyMDNjLWIzYWUtNGZkNy1iNDBjLWE5MzdjNWU0OWVkNyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=99fbd9b6-e83b-4b76-9f67-ffac49347d8f&link=10ca203c-b3ae-4fd7-b40c-a937c5e49ed7&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "demirbas-parcalama-destek-dokumani_160040311_160040311.html"
source_version: "2024-12-23T09:19:50.816+03:00"
source_bytes: 7440776
fetched_at: "2026-09-13T04:22:29+00:00"
generator: "netsis-scraper 1.0.0"
---
# Demirbaş Parçalama Destek Dokümanı

Demirbaş Parçalama, "Demirbaş Yönetimi\\Demirbaş\\İşlemler menüsü altında yer alır.

Demirbaş modülünde birden fazla miktarlı demirbaşlar için tek bir demirbaş kartı tanımlandığı durumlarda, bu demirbaşların miktarsal ya da tutarsal olarak farklı demirbaş kartlarına bölünebilmesi işlemidir.

## Miktara göre parçalama

![](../_assets/653d529b2ceba7a36f2c.png)

Örnekteki M1 kodlu demirbaşın;

Alış Miktarı: 100

**Alış** **Fiyatı:** 250.000

![](../_assets/3151578ec9c128761586.png)

**Toplam** **Amortisman:** 41.666,6670

![](../_assets/083a2e229e0e930ca23b.png)

İlgili demirbaş için miktarsal olarak parçalama işlemi yapılırken, Demirbaş Parçalama ekranında Demirbaş Kodu seçilmeli ve "Miktara Göre Otomatik Parçalansın" parametresi **işaretlenmelidir.**

İşlem tamamlandığında, baz demirbaşın alış bilgileri doğrultusunda, toplamda **100** adet demirbaş kartı program tarafından otomatik olarak oluşturulacak ve her bir kartın alış fiyatı ise; 250.000/100=**2500** olacaktır.

![](../_assets/c7cbe7b0689dc606ff2c.png)

Ayrıca, ilgili demirbaşın "Amortisman Bilgileri" sekmesinde bulunan "Toplam Amortisman" rakamı, yeni oluşan her bir karta eşit olarak paylaştırılacaktır.

## ![](../_assets/68f49da3600c6dd0776c.png)

## Tutara göre parçalama

## ![](../_assets/e65a5f04977d5bda9e0d.png)

Örnekteki T1 kodlu demirbaşın;

Alış Miktarı: 100

**Alış** **Fiyatı:** 250.000

![](../_assets/0537cdb95715169a6a31.png)

**Toplam** **Amortisman:** 43.779,1667

Tutarsal olarak demirbaş parçalanacağı durumda, Demirbaş Yönetimi\\Demirbaş\\Kayıt menüsü altında yer alan "Demirbaş Parçalama Bilgileri" ekranından, demirbaşın hangi kod ve tutarlara göre parçalanacağı bilgilerinin mutlaka tanımlanması gerekmektedir. Burada önemli olan nokta, tanımlama bilgilerindeki alış miktar toplamının baz alınacak demirbaşın alış miktarına denk olmasıdır.

![](../_assets/90042c0c3308193c0fba.png)

![](../_assets/f00d14e881f4e5ffdcec.png)

İlgili demirbaş için tutarsal olarak parçalama işlemi yapılırken, Demirbaş Parçalama ekranında Demirbaş Kodu seçilmeli ve "Miktara Göre Otomatik Parçalansın" parametresi **işaretlenmemelidir.**

İşlem tamamlandığında, demirbaş parçalama bilgilerindeki tanımlama doğrultusunda, toplamda **2** adet demirbaş kartı program tarafından otomatik olarak oluşturulacak ve her bir kartın alış fiyatı ve alış fiyatına göre hesaplanan alış miktarı program tarafından otomatik olarak yeni kartlara getirilecektir.

![](../_assets/9833e99fe0a0b520307a.png)

Ayrıca, ilgili demirbaşın "Amortisman Bilgileri" sekmesinde bulunan "Toplam Amortisman" rakamı, yeni oluşan her bir kartın miktar ve tutar bilgilerine göre otomatik olarak paylaştırılacaktır.
![](../_assets/499abb7faa0c10395253.png)

![](../_assets/bc3880d9e3023ad9d815.png)
