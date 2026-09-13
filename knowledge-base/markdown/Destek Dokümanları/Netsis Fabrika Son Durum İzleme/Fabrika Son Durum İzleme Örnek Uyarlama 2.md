---
title: "Fabrika Son Durum İzleme Örnek Uyarlama 2"
page_id: "140248189"
product: "netsis-3-enterprise"
depth: 3
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis Fabrika Son Durum İzleme"
  - "Fabrika Son Durum İzleme Örnek Uyarlama 2"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis Fabrika Son Durum İzleme / Fabrika Son Durum İzleme Örnek Uyarlama 2"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTQyYTc1NTU1LWJmNjktNDZiMy05Y2I1LThlZjg2MzBlYmQxMCZsaW5rPTRmMWFlN2ExLTczMDUtNGY4My1hNTg0LTdlMjBiNDRjNGI5NCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=42a75555-bf69-46b3-9cb5-8ef8630ebd10&link=4f1ae7a1-7305-4f83-a584-7e20b44c4b94&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "fabrika-son-durum-izleme-ornek-uyarlama-2_140248206_140248189.html"
source_version: "2024-12-08T14:08:20.930+03:00"
source_bytes: 1502736
fetched_at: "2026-09-13T04:24:57+00:00"
generator: "netsis-scraper 1.0.0"
---
# Fabrika Son Durum İzleme Örnek Uyarlama 2

Logo Netsis üzerindeki "Fabrika Son Durumu" ekranının hangi mantıkla çalıştığını ve ekranın kullanım detaylarını içeren "Fabrika Son Durum İzleme Tanıtım Dokümanı" sistemde halihazırda bulunmaktadır.

Bu dokümanda ise tanıtım dokümanında verilen detayların, örnek senaryolar üzerinden anlatılarak pekiştirilmesi amaçlanmıştır. Örnek uyarlama dokümanı incelenirken tanıtım dokümanından da yararlanılması önerilmektedir. Logo Netsis üzerindeki fabrika son durumu ekranının veri kaynağı kullanımı bakımından 3 farklı senaryo vardır:

- İleri üretim planlama (çizelgeleme) modülünün veri kaynağı olarak kullanıldığı senaryo.
- Kapasite planlama uygulamasının veri kaynağı olarak kullanıldığı senaryo.
- Reçete kaydı ekranının veri kaynağı olarak kullanıldığı senaryo.

Bu örnek uyarlama dokümanında, ileri üretim planlama (çizelgeleme) modülünün veri kaynağı olarak kullanıldığı senaryo ele alınacaktır.

#### İleri Üretim Planlama (Çizelgeleme) Ekranının Kullanıldığı Senaryo

Fabrika Son Durumu ekranının açıldığı ilk anda, çizelgeleme modülünün kullanılıp kullanılmadığı kontrol edilir. Çizelgeleme modülü kullanılıyorsa, vardiya planları Çizelgeleme modülünün "Fabrika Çalışma Takviminden" alınır.

![](../../_assets/2619ca288a5e2997d951.png)

Vardiya bilgileri aşağıdaki şekilde olup Fabrika Çalışma Takvimi'nde tüm günler için sabah, akşam, gece vardiyası seçilmiş olup pazar günü ise duruş vardiyası olup çalışma yapılmamaktadır.

![](../../_assets/35467cae0f2f4f8b4e90.png)

Bunun haricinde ileri üretim planlama uygulaması kullanıcıları için fabrika son durumu ekranı kullanımında kontrol edilmesi gereken bir parametre daha vardır. Bu parametre üretim akış kaydı ekranında makine bilgisinin de sorulmasını sağlamaktadır ki fabrika son durumu ekranının tam olarak çalışabilmesi için makine bilgisi gereklidir. İlgili parametre, üretim akış parametreleri altındaki "Makine Bilgisi Okunsun" parametresidir. Bu parametrenin açılmasıyla, üretim akış kaydı ekranına "Makine No" alanı eklenecektir.

![](../../_assets/8a33387003da30344731.png)

İleri üretim planlama uygulamasıyla fabrika son durumu ekranını kullanımına devam edilebilmesi için Üretim\\MRP\\Kayıt\\İleri Üretim Çizelgeleme\\Rota Tanımlama ekranı üzerinden yarı mamul ve mamullere ait rotaların tanımlı olması gerekir. Tanımlanan rotaya göre üretim akış kayıtlarında operasyon seçim yapılabilmektedir.

Örnek; YM_UST_BORU ve YM_ALT_BORU (aynı ürün grubuna bağlı) yarı mamullerine ait rota bilgileri aşağıdaki şekildedir ve iki operasyonda aynı istasyonda yapılmaktadır.

![](../../_assets/c4f81bc7fbc1343c2097.png)

Son olarak ilgili yarı mamul ve mamullere ait operasyon makine eşleştirme ekranı üzerinden ürünlerin birim zamanları tanımlı olmalıdır.

![](../../_assets/546c8e3f86dc440c896a.png)

Sistemde tanımlı aktivite kodları ve arıza kodları aşağıdaki şekildedir.

![](../../_assets/adc8f7b389063bdef8fb.png)

10.05.2024 tarihli YM_UST_BORU 200 adet ve YM_ALT_BORU 500 adetlik iş emrine ait üretim akış kayıtları aşağıdaki şekildedir. Üretim akış kaydı ekranında operasyon bilgilerini Rota Tanımlama ekranı üzerinden aldığından operasyon listesi alanı "Rota Kaydı" olarak görünmektedir.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| \1. operatör |  |  |  |  |  |  |  |
| **YM_UST_BORU** | Aktivite Kodu | Başlangıç Tarih/Saat | Bitiş Tarih /Saat | Üretim Miktarı | Fire Miktarı | Arıza Kodu | Makine Kodu |
| OP_BORU_KESIM | 02 | 10.05.2024 10:00 | 10.05.2024 12:00 | 200 | 15 |  | BORU_KESIM_01 |
| OP_KONIKLESTIRME | 01 | 10.05.2024 13:00 | 10.05.2024 13:20 |  |  |  | BORU_KONIK_MAK_02 |
| OP_KONIKLESTIRME | 02 | 10.05.2024 13:20 | 10.05.2024 14:00 | 30 | 10 |  | BORU_KONIK_MAK_02 |
| OP_KONIKLESTIRME | 03 | 10.05.2024 14:00 | 10.05.2024 15:00 |  |  | 02 | BORU_KONIK_MAK_02 |
| OP_KONIKLESTIRME | 01 | 10.05.2024 14:10 | 10.05.2024 14:30 |  |  |  | BORU_KONIK_MAK_03 |
| OP_KONIKLESTIRME | 02 | 10.05.2024 14:30 | 10.05.2024 17:00 | 150 | 5 |  | BORU_KONIK_MAK_03 |
| OP_KONIKLESTIRME | 02 | 10.05.2024 15:15 | 10.05.2024 16:00 | 5 |  |  | BORU_KONIK_MAK_02 |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| \2. operatör |  |  |  |  |  |  |  |  |
| **YM_ALT_BORU** | Aktivite Kodu | Başlangıç Tarih/Saat | Bitiş Tarih/Saat | Üretim Miktarı | Fire Miktarı | Arıza Kodu | Makine Kodu |  |
| OP_BORU_KESIM | 01 | 10.05.2024 09:00 | 10.05.2024 09:30 |  |  |  | BORU_KESIM_02 |  |
| OP_BORU_KESIM | 02 | 10.05.2024 09:30 | 10.05.2024 12:00 | 300 | 5 |  | BORU_KESIM_02 |  |
| OP_BORU_KESIM | 02 | 10.05.2024 13:00 | 10.05.2024 15:00 | 200 | 2 |  | BORU_KESIM_02 |  |
| OP_KONIKLESTIRME | 02 | 10.05.2024 10:00 | 10.05.2024 12:00 | 200 | 1 |  | BORU_KONIK_MAK_01 |  |
| OP_KONIKLESTIRME | 03 | 10.05.2024 13:00 | 10.05.2024 15:00 |  |  | 02 | BORU_KONIK_MAK_01 | Arıza devam ediyor. |
| OP_KONIKLESTIRME | 02 | 10.05.2024 16:00 | 10.05.2024 21:00 | 293 | 10 |  | BORU_KONIK_MAK_02 |  |

![](../../_assets/2139f9d95ef1c438c834.png)
![](../../_assets/72f8fe9f92c87a01be4c.png)

Yapılan üretim akış kayıtlarına ait fabrika son durumu aldığımızda aşağıdaki şekilde OEE değerleri hesaplanacaktır.

![](../../_assets/0a13ce6b0c0e8ad58f16.png)

BORU_KONIK_MAK_01 makinesinde en son bir makine arıza kaydı girildiği için Makine Arızası durumu ile Arızalı olarak görünmektedir. Diğer makineler ise çalışan makine olarak görünmektedir.

BORU_KONIK_MAK_02 makinesi için örnek OEE hesaplamasını inceleyelim.

![](../../_assets/aa0f7d915a4a72b65a50.png)

**OEE = AVA × PER × QUA**

Runtime= Planlanan Üretim Süresi- (Toplam Duruş Süresi + Toplam Hazırlık Süresi + Toplam Transfer Süresi)

|  |  |  |
| --- | --- | --- |
| AVA | = | Runtime |
|  |  | Planlanan Üretim Süresi |

Planlanan üretim süresi =24\*60 – (3\*60) - 45=1215 dk

Runtime = 1215 – 80 (20 ve 60 dk'lık duruşlar) =1135

**AVA** = 1135/1215=0,93415 (%93)

|  |  |  |
| --- | --- | --- |
| PER | = | ∑(Birim Ürün İçin Üretim Süresi X Birim Ürünün Üretim Miktarı |
|  |  | Runtime |

Ürünlerin standart üretim süreleri 65 sn., ilgili makinedeki üretim miktarları )30+5+293=328 adet.

Toplam standart üretim süresi=65\*328/60=355,33333 dk

**PER**= 355,333333/1135=0,313069 (%31)

|  |  |  |
| --- | --- | --- |
| QUA | = | ∑(Üretim Miktarı-Fire Miktarı) |
|  |  | ∑(Üretim Miktarı) |

QUA= 328-20/328 =0,9390 (%93)

**OEE**= AVA\*PER\*QUA =0,93\*0,31\*0,93=0,298119 (%27)

Son olarak ekranda görüntülenen tüm OEE değerlerinin hesaplanması sırasında kullanılan verilerin detaylarına "Grafik Verisi" seçeneğinden ulaşmak mümkündür. Fabrika Son Durumu ekranında fabrika, istasyon ve makine bazında görüntülenen OEE değeri ve bu değeri oluşturan tüm detaylar grafik verisi seçeneğine tıklandığında görüntülenebilir.

![](../../_assets/ce45eef802969fb3a5fb.png)
![](../../_assets/6f1c6be81cc479bfcaeb.png)
