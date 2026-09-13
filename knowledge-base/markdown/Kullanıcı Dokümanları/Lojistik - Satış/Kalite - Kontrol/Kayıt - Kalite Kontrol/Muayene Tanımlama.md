---
title: "Muayene Tanımlama"
page_id: "22804172"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Kalite - Kontrol"
  - "Kayıt / Kalite Kontrol"
  - "Muayene Tanımlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Kalite - Kontrol / Kayıt / Kalite Kontrol / Muayene Tanımlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWJhMzAwZmZjLTFmZGUtNDllYS04ZjVmLTRmM2I3YmI2ZDE3MyZsaW5rPWZmYmUyNTEzLTEwZWItNDk1ZC05MDM4LWRjNTgyOGQ0M2ViNSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=ba300ffc-1fde-49ea-8f5f-4f3b7bb6d173&link=ffbe2513-10eb-495d-9038-dc5828d43eb5&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "muayene-tanimlama_28148084_22804172.html"
source_version: "2022-11-28T08:59:20.240+03:00"
source_bytes: 266825
fetched_at: "2026-09-13T04:06:33+00:00"
generator: "netsis-scraper 1.0.0"
---
# Muayene Tanımlama

Muayene Tanımlama, Lojistik - Satış Bölümü'nde, "Kayıt/Kalite Kontrol" menüsünün altında yer alır. Muayene Kayıtları ve Muayene Aralık Tanımlama olmak üzere iki sekmeden oluşur. Muayene Tanımlama bölümü, Kalite Kontrol Parametreleri bölümünde bulunan "Kalite Kontrol Numune Aralıkları Tanımlama" parametresinin işaretlenmesi ile aktif hale gelir. Bu bölüm kullanılarak tanımlanan muayene kodları, Kalite Grup Tanımlarında sorgulanır ve aynı miktar aralığı için birden fazla örnekleme miktarının tanımlanmasını sağlar.

Örnekleme miktarlarının miktar aralığı bazında verilmesi için mutlaka muayene kodunun tanımlanmış olması gerekir.

![](../../../../_assets/6f3bcdfa5c14fef8cb22.png)

Standart, seviye bazında yukarıdaki gibi kontrol planları önerir. Örnek tabloda, Normal Seviye (Level-2) için parti büyüklüklerine (sample size code letter) göre numune miktarları (sample size) belirtilmiş. Kontrol planında ise, tercihe göre % 0,01 hata payından % 1000 hata payına kadar (sütun başlıkları), numunelerde çıkacak hatalı miktar üzerinden kabul edilebilir (Ac–Accept) ve red edilmesi gereken (Re–Reject) miktarlar verilir. Daha hassas hata payları için (örneğin insan hayatını ilgilendiren bir ürün/parça) sıfır ya da sıfıra yakın hatalı miktar, daha önemsiz parça/ürünler için daha yüksek sayıda hatalı miktar kabul edilir.

**Örneğin:** Tabloya göre, %6,5 hata payı ile çalışıldığında, parti miktarı 51 ile 90 arasında ise (E), 13 adet numunenin muayene edilmesi gerekir. Muayene sonucu 2 adet hatalı ürün varsa partinin kabul edilmesi, 3 adet ve üzeri hatalı ürün varsa partinin reddedilmesi gerekir.

Red miktarı, normal kontrol seviyesinde kabul edilebilir hatalı miktarın bir fazlasıdır. Ancak gevşek (indirgenmiş) seviyede, kabul/red miktarları arasında fark vardır. Bu durumda hatalı miktar kabul miktarının altındaysa parti kabul, red miktarı üzerindeyse parti red, ikisinin arasındaysa "bir sonraki partide kontrol seviyesinin değiştirilmesi" şartıyla kabul anlamına gelir.

Muayene tanımı, bir seviye ve bir hassasiyet derecesi için yapılır. Örnek: Normal seviyenin %0,01-%25 arası hata paylarına ait muayene kodları, MN00.010, MN00.015, MN00.025, MN00.040, MN00.065, MN00.100, MN00.150, MN00.250, MN00.400, MN00.650, MN01.000, MN01.500, MN02.500, MN04.000, MN06.500, MN10.000, MN15.000, MN25.000 şeklinde tanımlanabilir.

Aşağıdaki ekranda muayene kodları tanımlandıktan sonra, parti büyüklüklerine göre farklı miktarda numune ile standarttaki şekliyle kontrol planı oluşturulacaksa, başka bir tanımlama yapmaya gerek yoktur. "Muayene Aralık Tanımlama" bölümüne geçerek kayıt işlemlerine devam edilir.

**Muayene Kayıtları**

![](../../../../_assets/32ff46983543153cbc80.png)

Muayene Tanımlama Muayene Kayıtları sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Muayene Tanımlama Ekranı | Muayene Kayıtları |
| --- | --- |
| Muayene Kodu | Muayene kod bilgisinin girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, muayene kodları arasından seçim yapılabilir. Muayene kodu, malzemenin ne olduğundan ve yapılan ölçümlerden bağımsız, sadece parti büyüklükleri, numune miktarları, kabul/red miktar planlarına yönelik tanımlara yönelik oluşturulur. |
| Muayene Adı | Muayene kod bilgisi girildiğinde, koda ait açıklama isminin program tarafından otomatik olarak ekrana getirildiği alandır. |
| Örnekler Hurda | Örnekler hurda ise işaretlenmesi gereken seçenektir. |
| Sıfır Hata Politikası Uygulansın | Sıfır hata politikası uygulanması istendiğinde işaretlenmesi gereken seçenektir. |
| Metot Açıklama | Muayene kaydına ait metot açıklamasının girildiği alandır. |

**Muayene Aralık Tanımlama**

Tanımlanan muayene koduna ait parti büyüklüklerine göre kontrol edilecek örneklem miktarı (numune sayısı) ile kabul edilebilir ve red edilmesi gereken hatalı parça miktarları tanımlanır.

![](../../../../_assets/beec88227e1e0acf707b.png)

Muayene Tanımlama Muayene Aralık Tanımlama sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Muayene Tanımlama Ekranı | Muayene Aralık Tanımlama |
| --- | --- |
| Muayene Kodu | Tanımlanan muayene kodunun seçildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, muayene kodları arasından seçim yapılır. |
| Serbest Veri Girişi | Muayene aralık tanımlamasının ISO Standardına göre yapılmadığı durumlarda işaretlenmesi gereken seçenektir. İşaretlendiğinde, Standart, Seviye kodu ve Hata Payı alanları pasif hale gelir. Standardın dışındaki verilerin girilmesi için diğer alanlara bilgi girişi yapılır. |
| ISO Standardı | Muayene aralık tanımlamasının ISO Standardına göre yapılmasının istendiği durumlarda işaretlenmesi gereken seçenektir. |
| Miktar Kodu | Muayene aralık tanımlaması için miktar kodunun girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, miktar kodları arasından seçim yapılır. |
| Seviye Kodu | Muayene aralık tanımlaması için seviye kodunun girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, seviye kodları arasından seçim yapılır. |
| Başlangıç Miktarı | Girilen miktar ve seviye kodlarına göre başlangıç miktarının belirlendiği alandır. |
| Bitiş Miktarı | Girilen miktar ve seviye kodlarına göre bitiş miktarının belirlendiği alandır. |
| Oran (%) | Oran girilen alandır. |
| Örneklem Miktarı | Muayene için ayrılacak numune miktarın girildiği alandır. |
| Sabit Miktar | Sabit miktarın girildiği alandır. |
| Kabul Miktarı | Kabul edilebilir miktarın girildiği alandır. |
| Red Miktarı | Red edilmesi gereken veya hatalı parça miktarının girildiği alandır. |
| Kalite Kontrol Ölçümleri Örnekleme Göre Oluşsun | Ölçümlerin numuneye göre oluşturulması istendiğinde işaretlenmesi gereken seçenektir. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır.

Kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
