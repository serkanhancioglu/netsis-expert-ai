---
title: "Faturada Satır Bazında Dövizli İskonto Desteği"
page_id: "147554776"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Faturada Satır Bazında Dövizli İskonto Desteği"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Faturada Satır Bazında Dövizli İskonto Desteği"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTVhZjI0ZGFkLTFkYTgtNDQ4MS1iYzUyLWViYmEwNDFiNzIzNiZsaW5rPTY2ODk3MDlmLTQ0NTctNGM0NS05ZDE2LWMwMWQ4ZDIwM2IwNCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=5af24dad-1da8-4481-bc52-ebba041b7236&link=6689709f-4457-4c45-9d16-c01d8d203b04&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "faturada-satir-bazinda-dovizli-iskonto-destegi_147554776_147554776.html"
source_version: "2024-08-07T08:51:20.030+03:00"
source_bytes: 1174056
fetched_at: "2026-09-13T04:22:46+00:00"
generator: "netsis-scraper 1.0.0"
---
# Faturada Satır Bazında Dövizli İskonto Desteği

9057 sürümüyle birlikte, Alış/Satış Fatura/İrsaliye ve Müşteri/Satıcı Siparişi belgelerinde satır bazında girilen iskonto tutarının dövizli olarak girilebilmesi desteklenmiştir.

Bunun için, Alış/Satış Parametreleri ekranında İskonto sekmesinde yer alan "**Yüzde/Tutar** **Sorulsun**" parametresi işaretlenmelidir.

Bu parametrenin işaretlenmesiyle, belge kaydı esnasında satır bazında dövizli iskonto girilebilmesi için, kalem bilgilerine "**İsk.Döv.Tip**" isminde yeni bir alan eklenmiştir.

Bir örnekle dövizli iskonto hesaplamasına bakalım. Aşağıda kalem detayları yer alan bir satış faturası girildiğini düşünelim. Buna göre,

| **Stok** **Kodu** | Miktar | **Döviz** **Tipi** | **Birim** **Fiyat** | **Satır İskonto**<br>**Döviz** **Tipi** | **Satır İskonto**<br>**Tutarı** |
| --- | --- | --- | --- | --- | --- |
| 01 | 1 | 1 (dolar) | 2000 $ | 1 (dolar) | 200 $ |
| 001 | 1 | 1 (dolar) | 3000 $ | 1 (TL) | 300 TL |

Belgedeki ilk kalem için 200 $ iskonto tutarı girilebilmesi için, kalem girişi sırasında **"Y/T"** parametresi işaretlenir sonrasında **"İsk.** **Döv.** **Tip"** kısmına satırda girilecek iskonto tutarının döviz tipi girilir. Sonrasında **İsk.1** alanına girilen döviz tipine göre iskonto tutarı girilir.

![](../_assets/577da8618658a7bfa30c.png)

İskonto döviz tipi, belgedeki kalemin döviz tipinde veya TL olabilir. TL veya kalem döviz tipinden farklı bir döviz tipi girişi yapılamaz.

Girilmek istendiğinde **"İskonto** **döviz** **tipi** **Fatura** **kalemindeki** **döviz** **tipiyle** **uyumlu** **değildir"** uyarısı alınarak, TL veya kalem döviz tipinden farklı bir döviz tipi girişi engellenmiş olur.

![](../_assets/6d00ccb096a2846745ee.png)

Bu örnekte 200 $ satır iskontosu girileceği için, "**Y/T**" parametresi işaretlenir. **İsk.** **Döv.** **Tip** alanına dolar döviz tipi ve **İsk.1** alanına da 200 girilerek kalem gride atılır.

Belgedeki ikinci kalem için 300 TL iskonto tutarı girilebilmesi için, kalem girişi sırasında **"Y/T"** parametresi işaretlenir. **"İsk. Döv. Tip"** alanına TL iskonto tutarı girileceği için döviz tipi 0 (TL) girilir. Sonrasında **İsk.1** alanına girilen döviz tipine göre iskonto tutarı girilerek kalem gride atılır.

![](../_assets/bcd18f54391a07be03c1.png)
![](../_assets/996cf9d2316df3cc637c.png)

Toplamlar sekmesinde Satır İskontosu kısmında hem TL hem de dövizli girilen iskonto tutarları görünmektedir.

İlk satırdaki 200$ iskonto tutarının tl karşılığı 200\*33,1378=6.627,56 TL

İkinci satırdaki 300 TL iskonto tutarının dolar karşılığı 300/33,1378=9,05 $

TL satır iskontosu toplamı=300+6627,56=6927,56TL Dolar satır iskontosu toplamı=200+9,05=209,05$

![](../_assets/0f9b178b1cb0ec2251ae.png)
