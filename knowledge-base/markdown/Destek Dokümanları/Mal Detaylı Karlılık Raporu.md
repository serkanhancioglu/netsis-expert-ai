---
title: "Mal Detaylı Karlılık Raporu"
page_id: ""
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Mal Detaylı Karlılık Raporu"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Mal Detaylı Karlılık Raporu"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTA2NGZiNjBkLTE0NjUtNGRhOS05MDlhLTc5NmU4OTMyNzlkZSZsaW5rPTZjMzZjYmM4LTkzYmMtNDQ3ZS1iZjAwLTAxMmFlM2FlZWNkOSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=064fb60d-1465-4da9-909a-796e893279de&link=6c36cbc8-93bc-447e-bf00-012ae3aeecd9&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "mal-bazinda-karlilik-raporu.html"
source_version: ""
source_bytes: 17868
fetched_at: "2026-09-13T04:22:12+00:00"
generator: "netsis-scraper 1.0.0"
---
# Mal Detaylı Karlılık Raporu

**Mal Detaylı Karlılık Raporu Hesaplama Örnekleri**

Bu dokümanda aşağıdaki gibi hareketleri olan bir stok üzerinden mal detaylı karlılık raporundaki hesaplamalarına değinilecektir. Bilindiği gibi mal detaylı karlılık raporu, ilgili hareketlerin alış maliyetinin bulunması sonucunda satış tutarından bu rakam düşülerek kâr rakamına ulaşılabilmesini sağlamaktır.

Fatura karlılık raporunda maliyet hesabı aşağıdaki iş akışıyla yapılmaktadır.1) Öncelikle ekrandan seçilen maliyet tipine göre maliyet hesabı yapılır.2) Eğer maliyet hesabı sonucunda bulunan değer sıfır ise stok kartındaki Alış Fiyat-1 üzerinden maliyet getirilir.3) Alış Fiyat-1 bilgisi de sıfır ise ilgili stoğa ait son net giriş fiyatı ile maliyet hesabı yapılır.

Stok parametreleri **maliyet sistemi** parametresi **kapalı** iken mal detaylı karlılık raporu seçilen maliyet tiplerine göre şu şekilde çalışmaktadır.

Aşağıdaki gibi hareketleri olan bir stok üzerinden detaylı olarak maliyet hesaplamaları aşağıdaki şekildedir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/76a6c9bd-1ff0-4812-98d2-c94c0aa1233a/malbazı1.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/511e12c5-9825-4122-9dba-7f403c51216a/malbazı2.png)

**Son Giriş Net Fiyatı** seçili iken rapor alınması durumda ay bazındaki son giriş net fiyatlarının miktar ile çarpımı alış maliyeti olarak hesaplanır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/067bdaab-cbc8-4c80-a7f1-af9802049cbe/malbazı3.png)

1.ay sonundaki son giriş net fiyat 20 TL,2. ay sonundaki son giriş net fiyat 30 TL üzerinden alış maliyeti bulunmuş ve kar hesaplanmıştır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/84a8878b-0d01-4ff0-89a6-51f87d20b546/malbazı4.png)

**Son Giriş Brüt Fiyatı** seçili iken rapor alınması durumda ay bazındaki son giriş brüt fiyatlarının miktar ile çarpımı alış maliyeti olarak hesaplanır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/91cb78a4-958e-4987-9336-a7397907c88f/malbazı5.png)

1.ay sonundaki son giriş brüt fiyat 20 TL, 2. ay sonundaki son giriş brüt fiyat 33 TL üzerinden alış maliyeti bulunmuş ve kar hesaplanmıştır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/03c37fef-1b6f-42a1-96d1-3195b9844ecb/malbazı6.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/adbc15db-8189-4d85-b221-5353390687e7/malbazı7.png)

**Ağırlıklı ortalama** seçili iken rapor alınması durumda ay bazındaki ağırlıklı ortalama maliyetlerinin miktar ile çarpımı alış maliyeti olarak hesaplanır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/e0e02f71-04d3-4c9e-a3b0-5ba151c5ca73/malbazı8.png)

1.ay sonundaki ağırlıklı ortalama fiyatı;

(Toplam giriş tutarı + İade tipli giriş tutarı-İade tipli çıkış tutarı +E tipli giriş tutarı) /(Toplam giriş miktarı -İade tipli çıkış miktarı)

10\*100 +20\*100 / 100+100 =15

2. ay sonundaki ağırlıklı ortalama fiyatı;

10\*100 +20\*100+30\*50 /100+100+50 =4500/250 =18

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/d9225de9-384d-4286-a625-43b179c996f1/malbazı9.png)

**Hareketli ortalama** seçili iken rapor alınması durumda ay bazındaki ağırlıklı ortalama maliyetlerinin miktar ile çarpımı alış maliyeti olarak hesaplanır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/d6d4cc80-d3e8-400e-9412-a04a874a7a98/malbazı10.png)

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tarih | Fiş No | Tip | Fiyat | Giriş Miktarı | Çıkış Miktarı | Bakiye | **(Bir önceki** **hareketin** **ToplamTutarBakiyesi / Bir önceki** **hareketin** **ToplamMiktarBakiye)** | Toplam Tutar Bakiyesi | Toplam Miktar Bakiyesi |
| 01.01.2025 | S00000000001717 | J | 10,000000 | 100,00 | 0,00 | 100,00 |  | 1.000,00 | 100,00 |
| 10.01.2025 | S00000000001718 | J | 20,000000 | 100,00 | 0,00 | 200,00 |  | 3.000,00 | 200,00 |
| 22.01.2025 | S00000000019473 | J | 60,000000 | 0,00 | 1,00 | 199,00 | **3000/200 =15** | 2.985,00 | 199,00 |
| 24.02.2025 | S00000000001724 | J | 30,000000 | 50,00 | 0,00 | 249,00 |  | 4.485,00 | 249,00 |
| 26.02.2025 | S00000000019491 | J | 70,000000 | 0,00 | 2,00 | 247,00 | **4485/249=18,012** | 4.448,98 | 247,00 |

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/62296812-e16a-42eb-85aa-25f4f0f40dd7/malbazı11.png)

**Alış Fiyatı** seçili iken rapor alınması durumda stok kartında tanımlı olan alış fiyatı 1 tutarı ile miktar çarpımı alış maliyeti olarak hesaplanır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/fcc7f2ed-3b1f-4976-bfff-c08f226c7eed/malbazı12.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/5663b967-2cb6-464e-8555-da895f03caa7/malbazı13.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/ea24bf4c-947b-40e9-88fc-1209e163196f/malbazı14.png)

**LIFO** seçili iken rapor alınması durumda Son Giren İlk Çıkar yöntemine göre hesaplanan tutar ile miktar çarpımı alış maliyeti olarak hesaplanır. Buradaki hesaplama yöntemi kalem bazında maliyeti hesaplama yöntemine göre değil elde kalan giriş hareketlerinin ortalamasına göre yapılmaktadır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/d6730821-8979-4822-8224-e529bbe766fa/malbazı15.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/11e17627-08db-4bef-aeb4-dc3e099f2cbb/malbazı16.png)

Son giren ilk çıkar yöntemine göre ay bazında birim maliyetler hesaplanır.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Fiyat | Miktar | Tutar | Birim Maliyet |
| 01.01.2025 | 10 | 100 | 1000 |  |
| 10.01.2025 | 20 | 99 | 1980 |  |
| \1. ay LIFO maliyet |  | 199 | 2980 | 14,97487437 |
| 24.02.2025 | 30 | 48 | 1440 |  |
| \2. ay LIFO maliyet |  | 247 | 4420 | 17,89473684 |

1.ay içerisinde 1 adetlik çıkış son giriş hareketi olan 10.01.2025 tarihindeki 20 TL'den 100 adetlik girişten düşülmektedir. Böylece birim maliyet 2980/199=14,97 olarak hesaplanmaktadır.

\2. ay içerisindeki 2 adetlik çıkış ise 24.02.2025 tarihinde 30 TL'den 50 adetlik girişten düşülmektedir. Böylece birim maliyet bir önceki ay maliyeti ve ilgili ay maliyetleri dikkate alınarak 2980+(30\*48)/(199+48)=17,89 olarak hesaplanmaktadır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/b1af8edd-f7d2-47d5-a80b-3795bc41f920/malbazı17.png)

**FIFO** seçili iken rapor alınması durumda İlk Giren İlk Çıkar yöntemine göre hesaplanan tutar ile miktar çarpımı alış maliyeti olarak hesaplanır. Buradaki hesaplama yöntemi kalem bazında maliyeti hesaplama yöntemine göre değil elde kalan giriş hareketlerinin ortalamasına göre yapılmaktadır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/3aba5f74-c626-494e-b737-434e735e8c5f/malbazı18.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/9770fcf4-5bf3-40cc-9c54-c803728bdfa6/malbazı19.png)

İlk giren ilk çıkar yöntemine göre ay bazında birim maliyetler hesaplanır.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Fiyat | Miktar | Tutar | Birim Maliyet |
| 01.01.2025 | 10 | 99 | 990 |  |
| 10.01.2025 | 20 | 100 | 2000 |  |
| \1. ay FIFO maliyet |  | 199 | 2990 | 15,02512563 |
|  |  |  |  |  |
| 01.01.2025 | 10 | 97 | 970 |  |
| 10.01.2025 | 20 | 100 | 2000 |  |
| 24.02.2025 | 30 | 50 | 1500 |  |
| \2. ay FIFO maliyet |  | 247 | 4470 | 18,09716599 |

1.ay içerisinde 1 adetlik çıkış ilk giriş hareketi olan 01.01.2025 tarihindeki 10 TL'den 100 adetlik girişten düşülmektedir. Böylece birim maliyet 2990/199=15,025 olarak hesaplanmaktadır.

\2. ay içerisindeki 2 adetlik çıkış ise yine 01.01.2025 tarihinde 10 TL'den 100 adetlik girişten düşülmektedir. Böylece birim maliyet bir önceki ay maliyeti ve ilgili ay maliyetleri dikkate alınarak (10\*97)(20\*100)(30\*50)/(97+100+50)=18,097 olarak hesaplanmaktadır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/dc530386-6665-49f2-be66-fde03bebbb6b/malbazı20.png)

**Aylık Ağırlıklı Ortalama** seçili iken rapor alınması durumda aylık ağırlıklı ortalama yöntemine göre hesaplanan tutar ile miktar çarpımı alış maliyeti olarak hesaplanır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/089228ad-c4e1-4a47-8635-7cf8ca011fb5/malbazı21.png)

1.ay sonundaki aylık ağırlıklı ortalama fiyatı;

(Toplam giriş tutarı + İade tipli giriş tutarı-İade tipli çıkış tutarı +E tipli giriş tutarı) /(Toplam giriş miktarı -İade tipli çıkış miktarı)

10\*100 +20\*100 / 100+100 =15

2. ay sonundaki ağırlıklı ortalama fiyatı;

(Devir giriş miktarı\*devir maliyet tutarı) + Toplam giriş tutarı + İade tipli giriş tutarı-İade tipli çıkış tutarı +E tipli giriş tutarı) /(Devir giriş miktarı +Toplam giriş miktarı -İade tipli çıkış miktarı)

(100+100-1)\*15 + 30\*50 /199+50=18,01205

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/40e5f59e-1278-4c04-9bf3-356498cd6e22/malbazı22.png)

Stok parametreleri **Maliyet Sistemi** parametresi **açık** ya da **maliyet fiyatı baz alınsın seçeneği işaretli** iken mal detaylı karlılık raporu stok parametrelerinde seçili olan maliyet tipine göre maliyet oluşturma işlemi çalıştırılması sonucu oluşan hesaplanan maliyet değeri ile alış maliyeti hesaplanmaktadır. Seçilen maliyet tipine göre hesaplama **yapılmamaktadır**.

Örneğimizde stok parametrelerinde FIFO seçili olup maliyet oluşturma işlemi çalıştırılmış olup mal detaylı karlılık raporu alınması durumunda hangi maliyet tipi seçili olursa olsun alış maliyeti çalıştırılmış olan maliyet fiyatından gelmektedir (TBLSTHAR-STHAR_IAF değeri)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/35491143-5ebf-4a8b-80d3-a673ff8a6c4f/malbazı23.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/a6171528-b03c-435e-bace-8b2bcc4f6b22/malbazı24.png)

Stok parametreleri **Maliyet Sistemi** parametresi **açık** ve **FATURA\\SONGIRISFIAT\\0** özel parametresi tanımlı iken mal detaylı karlılık raporu alındığında ise mal detaylı karlılık raporunda seçilen maliyet tipine göre hesaplama **yapılmaktadır**.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/b8dbe193-1199-4c60-9690-10d74835959a/malbazı25.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/84e06408-6122-46cd-bfa1-cdade3d4a601/malbazı26.png)

Seçilen maliyet tiplerine göre yapılan hesaplamalar maliyet sistemi kapalı iken yapılan hesaplamalar ile aynı sonucu vermektedir.![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/d3b9f16e-15ee-458b-abba-d73bc51810f7/malbazı27.png)
