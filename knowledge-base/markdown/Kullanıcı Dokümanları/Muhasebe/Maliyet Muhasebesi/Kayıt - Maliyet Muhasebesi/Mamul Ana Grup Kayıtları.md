---
title: "Mamul Ana Grup Kayıtları"
page_id: "24741099"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Muhasebe"
  - "Maliyet Muhasebesi"
  - "Kayıt / Maliyet Muhasebesi"
  - "Mamul Ana Grup Kayıtları"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Maliyet Muhasebesi / Kayıt / Maliyet Muhasebesi / Mamul Ana Grup Kayıtları"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTAyNGYxODg4LTJkNzItNDU2MC05OTI3LTQ3NWM5NjcxZDJiMyZsaW5rPTQ2NDEyNzRiLWUzMTMtNDNhOC05MmFmLTI2ZDgwZjM5MmRjNSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=024f1888-2d72-4560-9927-475c9671d2b3&link=4641274b-e313-43a8-92af-26d80f392dc5&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "mamul-ana-grup-kayitlari_50675130_24741099.html"
source_version: "2022-10-17T13:15:38.630+03:00"
source_bytes: 66252
fetched_at: "2026-09-13T04:14:54+00:00"
generator: "netsis-scraper 1.0.0"
---
# Mamul Ana Grup Kayıtları

Mamul Ana Grup Kayıtları, Muhasebe Bölümü'nde, "Kayıt/Maliyet Muhasebesi Modülü" menüsünün altında yer alır. Ana Gruplar üretimin safhaları olup, maliyet safhalarının ayrı ayrı ve sırasıyla hesaplanması gereken bölümler olarak düşünülmesi gerekir.

**Örneğin;** Bir firmada Döküm, Karıştırma ve Montaj safhalarının olması halinde, bu safhaların Mamul Ana Grup Kodu Kayıtları bölümünden tanımlanması gerekir.

Mamul Ana Grup Kayıtları ekranı; Maliyet Gider Hesapları-1, Maliyet Gider Hesapları-2, Dağıtım Anahtarları sekmelerinden oluşur.

**Maliyet Gider Hesapları-1**

Mamul Ana Grup Kayıtları ekranı Maliyet Gider Hesapları-1 sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Mamul Ana Grup Kayıtları Ekranı |  |
| --- | --- |
| Ana Grup Kodu | Maliyet ana grubuna verilen koddur. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, ana grup kodları arasından seçim yapılır. Uygunluk taşıması açısından Muhasebe Hesap Planı ekranında girilen sarf yerleri hesap kodu ile aynı olabilir. |
| Ana Grup İsmi | Maliyet ana grup isminin girildiği alandır. Rapor amaçlı kullanılır. |
| Referans Kodu | [Muhasebe Parametreleri](<../../Muhasebe Modülü/Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/Muhasebe Modülü Tanımlamaları/Muhasebe Parametreleri - Muhasebe.md>) bölümünde Referans Kodu kullanımını işaretleyen kullanıcıların kullandığı alandır. Muhasebe Hesap Planı detayı olmadan sarf merkezleri referans kodları bazında tanımlanmışsa, maliyet ana grup koduna ait referans kodunun girilmesi gerekir. Referans kodu kullanımında da aşağıda açıklamaları bulunan hesap kod maskelemesi kullanılır. Fakat program maliyet hesaplarında, sarf tutarlarını yevmiye fişlerindeki referans kodlarını tarayarak oluşturur. |
| Standart Maliyet | Mamul ana grubu için standart maliyet bilgisinin girildiği alandır. |
| İade Hesaplamalarında Geri Dönülecek Ay Sayısı | Mamul ve yarı mamullerin satıştan iade işlemlerinde, maliyet fiyatlarının geçmiş bir aydaki ortalama maliyet fiyatı üzerinden değerlendirilmesi için kullanılacak alandır. Kaç ay geriye dönüleceği “İade Hesaplamalarında Geri Dönülecek Ay Sayısı” alanına girilen rakama göre belirlenir. **Örneğin;** 11. ayda maliyet oluşturuluyorsa, geri dönülecek ay sayısının 2 olarak belirtilmesi durumunda, iade alınan mamul ve yarı mamullerin maliyetleri, 9 ayda maliyet girişinde oluşan ortalama maliyet fiyatı üzerinden değerlendirilir. |
| Yan Ürünün Ortalama Satış Tutarı Mamul Maliyetinden Düşülecek | Yan ürün, üretimin nihai amacı olmayan, üretim aşamalarında yan ürün olarak çıkan ve satışı da yapılan üründür. Kuruluşun üretim safhalarında yan ürün olarak oluşan ürünler olduğunda ve bu yan ürünlerin mamul ürünleri gibi satışı yapıldığında kullanılması gereken seçenektir. Maliyet hesaplamalarında yan ürünlerin satış tutarlarının bağlı oldukları yarı mamul/mamulün, maliyet toplamlarından düşülmesini sağlar. İşaretlendiği durumda, hesaplanan yarı mamul/mamul maliyeti toplam tutarından, yan ürünlerin satış tutarları çıkarılır. Bu tercih ile, yarı mamul/mamulün maliyet değerleri düşürülür. Ayrıca, seçeneğin işaretlenmesi ile o yan ürünün maliyeti, ortalama satış fiyatı olarak kabul edilir. **Örneğin;** Buğdaydan irmik üretimi sırasında yan ürün olarak kepek çıkıyor. İrmik oluşturma safhasının bir maliyet ana kodu olarak tanımlandığı düşünüldüğünde, seçeneğin işaretlenmesi ile birlikte, irmiğin maliyetinden kepeğin ortalama satış fiyatı olarak kabul edilen maliyeti düşülür. |
| İşçilik | İşçilik giderlerinin getirileceği muhasebe hesap kodunun tanımlandığı alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, muhasebe hesap kodlarına ulaşılır. |
| Enerji | Enerji giderlerinin getirileceği muhasebe hesap kodunun tanımlandığı alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, muhasebe hesap kodlarına ulaşılır. |
| Amortisman | Amortisman giderlerinin getirileceği muhasebe hesap kodunun tanımlandığı alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, muhasebe hesap kodlarına ulaşılır. |
| Yardımcı Servis | Yardımcı Servis giderlerinin getirileceği muhasebe hesap kodunun tanımlandığı alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, muhasebe hesap kodlarına ulaşılır. |
| Yedek Parça | Yedek Parça giderlerinin getirileceği muhasebe hesap kodunun tanımlandığı alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, muhasebe hesap kodlarına ulaşılır. |

**Muhasebe Hesap Kodlarının Maskelenmesi**

720 ve 730 hesapların maskelenerek, maliyet ana grubu bazında girildiği alanlardır. 720 ve 730 hesapların maskelenerek maliyet ana grubu bazında girilirken dikkat edilecek konu; maskeleme işlemlerinin tam hesap kodu düzeninde yapılmasıdır.

**Örneğin;** 3-3-4 seviye ve kod uzunluklarında oluşturulan 730 hesaplardan, 6 grubu ile başlayan amortisman giderleri için Ana Grup Kodu tanımlama bölümündeki maskelemenin 730-6??-???? şeklinde olması gerekir.

Maliyet kalemlerinde girilen bu maskeleme filtrelenerek yine muavin hesaplara dağıtılır. Referans kodu sistemi ile çalışılsa dahi, bu filtreleme işlemi yapılır. Gider yerleri olarak 2. sahalar, detaylandırması çok ayrıntılı olan hesap planları için kullanılacak yedek sahalardır. Özellikle tek bir muavin kullanan firmaların bu yedek sahaları mutlaka boş bırakması gerekir.

**Örneğin;** Özellikle işçilik gideri hem 720 Ana Hesap hem de Genel Yönetim Giderleri (730) bazında sarf nevilerinde dağıtılır. Bu dağılımların, 720 ve 730 ana hesap bazında ayrı ayrı entegre edilmesi gerekir. Bu durumda işçilik hesap kodlarının her iki sahaya da ayrı ayrı girilmesi gerekir.

Maliyet Gider Hesapları-2

Maliyet Gider Hesapları-2 sekmesi, Maliyet Ana Grup Kayıtları ekranında standart olarak gelen beş gider alanı dışında, kullanılması istenen başka gider kalemlerinin olması halinde, kullanılacak olan saha başlıklarının izlendiği sekmedir. Saha başlıkları [Maliyet Muhasebesi Parametreleri](<Maliyet Muhasebesi Parametreleri.md>) bölümünden tanımlanır.

Mamul Ana Grup Kayıtları ekranı Maliyet Gider Hesapları-2 sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Maliyet Gider Hesapları-2 Ekranı |  |
| --- | --- |
| Ana Grup Kodu | Maliyet Gider Hesapları-1 sekmesinde girilen Ana Grup Kodu bilgisinin izlendiği alandır. |
| Ana Grup İsmi | Maliyet Gider Hesapları-1 sekmesinde girilen Ana Grup İsmi bilgisinin izlendiği alandır. |
| Referans Kodu | Maliyet Gider Hesapları-1 sekmesinde girilen Referans Kodu bilgisinin izlendiği alandır. |
| Standart Maliyet | Maliyet Gider Hesapları-1 sekmesinde girilen Standart Maliyet bilgisinin izlendiği alandır. |

**Dağıtım Anahtarları**

![](../../../../_assets/1599b9155d00cc6d390b.png)

Mamul Ana Grup Kayıtları ekranı Dağıtım Anahtarları sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Mamul Ana Grup Kayıtları Ekranı |  |
| --- | --- |
| Hammadde Sarfları Ana Grup Bazında | Çıkış yeri detayı belli olmayan hammadde sarf tutarlarının, doğrudan maliyet ana grubuna çıkış kaydı yapılmasına olanak sağlayan seçenektir. Seçenek işaretlenmemişse, hammadde sarf tutarları ya stok koduna ya da maliyet grup koduna yapılabilir. |
| Dağıtım Anahtarları | Hesaplanan sarf tutarlarının maliyet ana grubu bazında dağıtım anahtarlarıdır. Maliyet hesaplamalarında sarf ve maliyet mahsupları oluşturulurken, hesaplanan sarf tutarlarının dağıtım çalışmaları Üretim Miktarları Oranı, Birim Katsayılar Oranı ve Hammadde Sarfları Oranı olmak üzere üç tip anahtara göre yapılır. **Üretim Miktarları Oranı:** Üretilen miktarlar baz alınarak program tarafından hesaplanacak katsayılara göre sarf tutarları dağıtımının yapılacağı anahtar tipidir. **Örneğin;** 1.safhada YY1 ve YY2’yi üretiliyor ve üretim miktarları ilgili ayda; YY1 **1.000** adet, YY2 **500** adet, İşçilik Gideri **3.000.000** ise, dağıtım işlemi aşağıdaki şekilde gerçekleşir: Toplam Üretim Miktarı = 1.000 + 500 = 1500 Birim İşçilik Değeri = 3.000.000 / 1.500 = 2.000 **YY1** için oluşan işçilik tutarı = 1.000 x 2.000 = **2.000.000** **YY2** için oluşan işçilik tutarı = 500 x 2.000 = **1.000.000** olarak oluşur. **Birim Katsayılar Oranı:** Yukarıda anlatılan üretim miktarları oranı hesaplamasından oluşan değerin, Maliyet Grup Kodu bölümünde girilen birim katsayılarla çarpılarak dağıtılması yöntemidir. **Örneğin,** 1.safhada YY1 ve YY2’yi üretiliyor ve üretim miktarları ilgili ayda; YY1 **1.000** adet ve Birim katsayı **2,** YY2 **500** adet ve Birim katsayı **3,** İşçilik Gideri 3.000.000 ise, dağıtım işlemi aşağıdaki şekilde gerçekleşir: Toplam (üretim x birim katsayı) = (1.000 x 2) + (500 x 3) = 3.500 Birim İşçilik Değeri = 3.000.000 / 3500 = 857.142,8571 **YY1** için oluşan işçilik tutarı = 2.000 x 857.142,8571 = **1.714.285.714** **YY2** için oluşan işçilik tutarı = 1.500 x 857.142,8571 = **1.285.714.286** olarak oluşur. |
| Hammadde Sarfları Oranı | Hammadde Sarfları Oranı dağıtım anahtarı ile; maliyet mamul grubuna ait hammadde sarf tutarları, program tarafından ilgili hesaplardan okunup, varsa yarı mamul sarf tutarları da eklenerek, toplam sarf tutarı her gruba oranlanarak hesaplanır. |

İlgili kayıtlar girildikten sonra “Kaydet” ![](../../../../_assets/865524a70e225c89c107.jpg) butonu ile kayıt tamamlanır. Açılan bir kayıt, kayıt sil ![](../../../../_assets/2df4b343310bcd16b01e.jpg)butonu ile iptal edilir veya üzerinde değişiklik yapılması için kaydet ![](../../../../_assets/865524a70e225c89c107.jpg) tuşu kullanılarak düzeltilir.
