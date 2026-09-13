---
title: "Stokta Durma Maliyeti"
page_id: ""
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Stokta Durma Maliyeti"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Stokta Durma Maliyeti"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTY0NTllMzIxLWIyNDItNDY0Mi04NzMxLTVhOTk3MTcxMjMyMyZsaW5rPWRlMWFiOTY5LTdhOGItNDNiMC1iNDg1LTgzNTEyYzM1ZDY1NiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=6459e321-b242-4642-8731-5a9971712323&link=de1ab969-7a8b-43b0-b485-83512c35d656&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "stokta-durma-maliyeti.html"
source_version: ""
source_bytes: 8062
fetched_at: "2026-09-13T04:21:45+00:00"
generator: "netsis-scraper 1.0.0"
---
# Stokta Durma Maliyeti

Stokta durma maliyeti (stok bulundurma veya elde tutma maliyeti), satılmamış ürünlerin depolanması, sigortalanması ve yönetilmesi sebebiyle işletmenin katlandığı tüm görünür ve görünmez masraflardır. Bu dokümanda ilgili ay içerisinde üretimi olmamasına rağmen stokta durma maliyetlerinin stoklar üzerine dağıtılmasına değinilecektir. Uygulamaya başlayabilmek için Maliyet Muhasebesi Parametreleri ekranı Maliyet Parametleri-2 sekmesinde yer alan “Stokta Durma Maliyeti Toplam Maliyete Eklensin” parametresi aktif hale getirilmelidir.

Lokal Depo Kodu alanı maliyet hesaplatma sonucu stok hareketlerinde oluşan E tipli hareketin hangi depo kodu ile sisteme aktarılacağını gösterir.

Muhasebe Kodu Maskesi alanı ise stokta durma maliyetinin kullanıldığı gider hesap kodunun ya da hesap kodu maskesinin girildiği alandır.

5. gider tanımı alanında ise özel bir ifade gerek olmaksızın herhangi bir gider tanımı girişi yapılmalıdır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/57d7de10-66cf-43bb-82b5-c75f019f1f24/STM-1.jpg)

İlgili mamul grup kodları için yansıtma hesapları sekmesinde ilgili gidere karşılık gelen yansıtma hesabı doldurulmalıdır.

## ![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/d41f5ad5-f565-4bc6-af8e-74d52d0602a7/STM-2.jpg)

Stokta durma maliyet giderinin dağıtım yöntemi olarak üretim miktarları oranı ya da birim katsayılar yöntemi kullanılabilir.

**Üretim Miktarları Oranı Yöntemi**

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/cfd3163b-6bdb-43d3-886c-e842c074d21c/STM-3.jpg)

Bu yöntemde stok hareketlerinde hangi depoların bakiyesinin dikkate alınacağı aşağıdaki özel parametre tanımı ile belirlenmelidir.

Grup Kodu: MALIYET

Anahtar: STOK_DURMA_DEPOKODLARI

Değer: Bu alana dikkate alınacak depo kodları girilmelidir. Birden fazla depo kodu dikkate alınması istenir ise depo kodları arasına virgül konularak (Ör: 1,3,20) tanımlama yapılmalıdır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/fdfbee54-9259-4173-81db-3d2a14da4aed/STM-4.jpg)

Örnek stok hareketleri aşağıdaki şekilde olan aynı mamul ana grubuna bağlı 2 stok için 4. Ayda üretimler yapılmış ve maliyetler oluşturulmuştur. 5. Ayda ise herhangi bir üretim gerçekleşmemiş olup ilgili stoklara gider hesabına ait borç bakiyesi dağıtılacaktır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/bd1285fb-e0ff-4b0f-9d46-82c4533d5258/STM--51.jpg)

YMAL1 stoğunun 4. Ay maliyeti 60 lira, YMAL2 stoğunun ise 70 liradır. 5. Ay için maliyet oluşturma ve maliyet hesaplatma işlemleri çalıştırıldığında E tipli hareketler ilgili stoklara aşağıdaki şekilde yansımaktadır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/5de29fb6-b24f-48d8-a398-8addf7a6ed38/tSTM-61.jpg)

Stokta durma için tanımlanan gider hesabının ilgili aydaki borç bakiyesi aşağıdaki şekildedir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/d64a01c7-bc55-4a3e-b7d3-c7631bc08b14/stm-71.jpg)

2000 lira olan bakiye YMAL1 ve YMAL2 stokları için özel parametrelerde 20 nolu depo tanımı yapıldığından ilgili depodaki bakiyeleri kontrol ederek gider hesabını dağıtım oranı aşağıdaki şekilde hesaplanır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/abb0abcc-702f-4f3f-84ed-83549b714362/STM-8.jpg)

Ay başı stok: Bir önceki aydan ilgili depo için kalan bakiye

Ay sonu stok: İlgili ay sonundaki ilgili depodaki kalan bakiye

Ortalama stok miktarı YMAL1: (Ay başı stok+ Ay sonu stok) /2 = (20+20) /2=20

Ortalama stok miktarı YMAL2: (Ay başı stok+ Ay sonu stok) /2 = (3+17) /2=10

Dağıtım oranı YMAL1 = 20/ (((20+20) +(3+17)) / 2) =20/30

Dağıtım oranı YMAL2 = 10/ (((20+20) +(3+17)) / 2) =10/30

YMAL1 gider dağıtım tutarı: 2000\*(20/30) =1333,3333

YMAL2 gider dağıtım tutarı: 2000\*(10/30) =666,6667

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/5ecf898a-6d52-4e4a-807c-bcb976c4a52f/STM-91.jpg)

5. ayda üretim olmamasına rağmen ortalama maliyet değerleri stokta durma maliyeti eklenerek artış göstermiştir.

YMAL1: 60\*20 (4. Ay bakiye maliyeti) +1333,33 /20 =126,6667

YMAL2: 70\*80 (4. Ay bakiye maliyeti) +666,67 /80 =78,3333

Not: Ay başı stok ve ay sonu stok miktarları ay bazında TBLMALIGRUP tablosunda tutulmaktadır. Her ay maliyet hesaplatma işlemi ile bu değerler güncellenmektedir.

**Birim Katsayılar Yöntemi**

Birim katsayı yönteminde ise stok bakiyeleri ile ilgili herhangi bir kontrol bulunmayıp doğrudan ilgili stoklar için belirlenen katsayılar üzerinden oran dağıtımı hesaplanıp giderler dağıtılır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/64f84d32-9cab-4034-a63f-d5b23186f02f/STM-10.jpg)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/1696db6f-6025-4729-ab20-7582c0fcc467/stm-11-1.jpg)

Toplam birim katsayı =3+8=11

YMAL1 için dağıtım oranı: 3/11

YMAL2 için dağıtım oranı : 8/11

YMAL1 için gider tutarı = 2000\* 3/11=545,45

YMAL2 için gider tutarı 2000\* 8/11= 1454,55

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/384342cf-3a35-4ab0-bb04-b4eeb82efbef/stm-12-1.jpg)

Hesaplanan gider tutarları stok hareketlerine E tipli hareket olarak yansımış olup ortalama maliyeti de arttırmıştır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/47c728cc-5c90-40f9-9187-0c74204a7a9f/stm-13-1.jpg)

Her iki yöntemde de parametrelerde tanımlanan hesap kodundaki bakiye tutar ürünlere dağıtılır. İlgili hesap kodunun proje / referans kırılımına göre dağıtım yapılmamaktadır.
