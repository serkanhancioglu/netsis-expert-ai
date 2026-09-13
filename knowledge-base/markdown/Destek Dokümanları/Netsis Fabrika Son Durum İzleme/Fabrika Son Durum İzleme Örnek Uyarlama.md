---
title: "Fabrika Son Durum İzleme Örnek Uyarlama"
page_id: "80089827"
product: "netsis-3-enterprise"
depth: 3
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis Fabrika Son Durum İzleme"
  - "Fabrika Son Durum İzleme Örnek Uyarlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis Fabrika Son Durum İzleme / Fabrika Son Durum İzleme Örnek Uyarlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTk4OWZkNzU3LTUxOTItNDI5Yi1iZjcyLWU0YTgyYTFlY2Q2NSZsaW5rPWM2YjcxY2Y2LTMyN2ItNDZiYS05MTdjLWI3YzYzMjI4NDhkZiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=989fd757-5192-429b-bf72-e4a82a1ecd65&link=c6b71cf6-327b-46ba-917c-b7c6322848df&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "fabrika-son-durum-izleme-ornek-uyarlama_80089849_80089827.html"
source_version: "2022-11-02T15:57:14.097+03:00"
source_bytes: 1447063
fetched_at: "2026-09-13T04:24:56+00:00"
generator: "netsis-scraper 1.0.0"
---
# Fabrika Son Durum İzleme Örnek Uyarlama

Fabrika Son Durum İzleme Örnek Uyarlama ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Logo Netsis üzerindeki "Fabrika Son Durumu" ekranının hangi mantıkla çalıştığını ve ekranın kullanım detaylarını içeren "Fabrika Son Durum İzleme Tanıtım Dokümanı" sistemde halihazırda bulunmaktadır. Bu dokümanda ise tanıtım dokümanında verilen detayların, örnek senaryolar üzerinden anlatılarak pekiştirilmesi amaçlanmıştır. Örnek uyarlama dokümanı incelenirken tanıtım dokümanından da yararlanılması önerilmektedir. Logo Netsis üzerindeki fabrika son durumu ekranının veri kaynağı kullanımı bakımından 3 farklı senaryosu vardır:

- İleri üretim planlama (çizelgeleme) modülünün veri kaynağı olarak kullanıldığı senaryo.
- Kapasite planlama uygulamasının veri kaynağı olarak kullanıldığı senaryo.
- Reçete kaydı ekranının veri kaynağı olarak kullanıldığı senaryo.

Bu örnek uyarlama dokümanında, kapasite planlama uygulamasının ve reçete kaydı ekranının kullanıldığı senaryolar ele alınacaktır.

#### Reçete Kaydı Ekranının Kullanıldığı Senaryo

Çizelgeleme ve kapasite planlama uygulaması kullanmayan bir kullanıcının fabrika son durumu ekranını kullanabilmesi için gerekli olan vardiya planlarına ve ürün birim sürelerine sırasıyla; MRP modülü altındaki fabrika çalışma takvimi ve reçete kayıtlarındaki operasyon sürelerinden ulaşılmaktadır. Bu bağlamda fabrika çalışma planının tanımlanabilmesi için Üretim-MRP-Kayıt-Takvim Tanımlamaları-Fabrika Çalışma Takvimi yolu izlenmelidir. Fabrika çalışma planı yerine aynı yol izlenerek ulaşılabilen "İstasyon Çalışma Takvimi" de kullanıcının ihtiyacı doğrultusunda kullanılabilmektedir ancak bu uyarlamada fabrika çalışma takvimi üzerinden gidilecektir.
![](../../_assets/7ea61a83c58a80b71b34.png)**Ekran** **Görüntüsü** **1**

Örnek uyarlamamız sırasında kullanılmak üzere şöyle bir vardiya planıyla çalıştığımız varsayımıyla başlayalım; her biri 8 saatlik 3 vardiyayla çalışıyoruz ve ilk vardiya 00:00'da çalışmaya başlıyor. Bu durumda fabrika çalışma takvimi tanımından da önce, ilk olarak MRP parametreleri içindeki MRP II parametre ayarlarının yapılması gerekmektedir. (Bkz. Ekran Görüntüsü 1)
1. ekran görüntüsünde görülebileceği gibi, vardiyaların başlangıç saatleri ve toplam süreleri MRP parametreleri içinden girilmiştir. Fabrika son durumu ekranı tarafından bu bilgiler kullanılacaktır. Ayrıca vardiyada çalışan kişi sayıları ve reçete kaydı ekranındaki operasyon sürelerinin birimi de (dakika ya da saat) ilgili ekran üzerinden yapılmıştır. MRP parametre ayarlarının yapılmasının ardından fabrika çalışma takvimi tanımlamaları yapılmalıdır.
3 vardiyayla çalışmaya uygun olacak şekilde yapılan tanımlamalar 2. ekran görüntüsünde gösterilmiştir.
![](../../_assets/ab5c229aeb945bf1367b.png)**Ekran** **Görüntüsü** **2**
Vardiya düzeni ve fabrika çalışma takvimi belirlendikten sonra operasyonlar ve ürünlerin birim süreleri ile ilgili tanımların yapılması gerekmektedir. Bu nokta asıl amacımızın fabrika son durumu ekranının kullanımının pekiştirilmesi olması sebebiyle, son derece basit bir sistem kurgulayacağız. Öncelikle bir adet istasyon tanımı yaparak başlayalım. (Bkz. Ekran Görüntüsü 3)
![](../../_assets/0d59ca18efe7bbcb7864.png)**Ekran** **Görüntüsü** **3**
İleri üretim planlama modülü kullanılmadığından, istasyon tanımı MRP modülünün altından yapılmalıdır. Üretim-MRP-Kayıt  İş İstasyonu Tanımlama yolu izlenerek ilgili ekrandan "IST10" kodlu bir istasyon tanımı yapılmıştır. İş istasyonu tanımı yapılırken kayıtlı tüm vardiyalar için "Standart Eşzamanlı Operasyon Sayısı/X. Vardiya" bilgilerinin doldurulmasının zorunlu olduğu unutulmamalıdır. Bu kaydın ardından bir de makine tanımı yapılmalıdır. (Bkz. Ekran Görüntüsü 4)
![](../../_assets/7037ff7e6c7d25cb5481.png)**Ekran** **Görüntüsü** **4**
Yine MRP modülünün altından yapılan makine tanımlaması için Üretim-MRP-Kayıt-Makine Tanımlama yolu izlenmiştir. Ekran üzerinden "MAK10" kodlu bir makine tanımlanmıştır. Bu işlemin ardından bir de operasyon tanımlaması yapılması gerekmektedir. Operasyon tanımları da aynı şekilde MRP modülünün altından yapılmalıdır. (Bkz. Ekran Görüntüsü 5)
![](../../_assets/e85f7116b34a680b54d2.png)**Ekran** **Görüntüsü** **5**
"OP10" kodu operasyon tanımı da Üretim-MRP-Kayıt-Operasyon Tanımlama yolu kullanılarak tanımlanmıştır. Böylece içinde "Makine 10"u barındıran bir "İstasyon 10" ve bu makinede gerçekleşecek bir "Operasyon 10" tanımlamış olduk.
Son olarak da bu sistemde üretilecek bir son ürüne ihtiyacımız var. Bu noktada sisteme "Yarı Mamul 10" ve "Mamul 10" olmak üzere 2 adet stok kartı kaydı yapılmıştır. Bu örnekte YM10'un (yarı mamul 10) Operasyon 10'a girdiği ve sonuçta bir MAMUL10 üretimi gerçekleştiği varsayılmaktadır. Bu bilgiler dahilinde fabrika son durumu ekranının kullanımından önceki son aşama olarak bir reçete tanımlamasının da yapılması gerekmektedir. Bu senaryoda hem ileri üretim planlama modülü hem de kapasite planlama uygulaması kullanılmadığı varsayıldığından, örnekteki MAMUL10'un üretimi için gereken birim süre reçete kaydı ekranından alınacaktır. (Bkz. Ekran Görüntüsü 6)
![](../../_assets/d92c908326205f0aaf3b.png)**Ekran** **Görüntüsü** **6**

![](../../_assets/aee488ffdc4b3eb148e3.png)

\6. ekran görüntüsünde görüldüğü gibi, bir MAMUL10 reçetemiz var ve bu reçete altında 1 adet YM10 bileşeni ve OP10 operasyonu var. Bu noktada operasyon için yapılan Reçete Bilgileri-2 tanımları önem taşımaktadır. Çünkü fabrika son durumu ekranı, mamule ait operasyonel süre bilgisini buradan almaktadır. (Bkz. Ekran Görüntüsü 7)

![](../../_assets/48808e274db451a41e31.png)![](../../_assets/32d64bb1e28e239c27f9.png)**Ekran Görüntüsü 7 ve 8**

\7. ekran görüntüsünde görüldüğü gibi OP10'un süresi 2 dakikadır. Üretim süresinin birim tanımı ise MRP Parametreleri-MRP II sekmesinin "Süre Tipi" alanında "dakika" olarak belirlenmişti. (Bkz. Ekran Görüntüsü 1)

![](../../_assets/ec1c1efad13066df5be1.png)**Ekran Görüntüsü 9**

Tüm bu tanımlamaların ardından fabrika son durumu ekranında veri görebilmek için 3 adet iş emri oluşturalım. 100,150 ve 200 adetlik, 3 adet MAMUL10 iş emri 8. ekran görüntüsünde gösterilmiştir.
İş emirlerinin de oluşturulmasından sonra, son aşama olan üretim akış kaydı oluşturma işlemini de tamamlayalım. (Bkz. Ekran Görüntüsü 9) Yaptığımız üretim akış kayıtlarının ilkinde üretilen ürün adedi 95 olmuş, bu ürünlerin 5'i fireye dönüşmüş ve toplam üretim süresi 208 dakika olmuştur. İkinci üretim akış kaydında ise iş emri adedi 150 olan MAMUL10'un üretim adedi 144 olmuş, 6 tane ürün fireye dönüşmüş ve üretim toplamda 323 dakika sürmüştür. Son üretim akış kaydında ise 198 adet MAMUL10'un üretimi 430 dakika sürmüştür ve 2 ürün fire olmuştur. Üretim akış kayıtlarını da tamamladıktan sonra fabrika son durumu ekranını açıp, OEE (toplam ekipman etkinliği) değerimizin ne olduğunu görebiliriz. (Bkz. Ekran Görüntüsü 10)
![](../../_assets/46231f5303b1f4c0c24c.png)**Ekran** **Görüntüsü** **10**
Örnek uyarlamamız için girdiğimiz az sayıdaki veriye ve rapor tarih aralığına istinaden hesaplanan OEE değeri 10. ekran görüntüsünde görüldüğü gibi %58'dir. Kullanılabilirlik, performans ve kalite değerleri de sırasıyla %100, %60 ve %97 olarak gerçekleşmiştir.

İlgili değerler şu şekilde hesaplanmıştır:

**OEE** = AVA × PER × QUA → **0,58** = 1,0 × 0,6 × 0,97

AVA = 𝑷𝒍𝒂𝒏𝒍𝒂𝒏𝒂𝒏 Ü𝒓𝒆𝒕𝒊𝒎 𝑺ü𝒓𝒆𝒔𝒊 − (𝑻𝒐𝒑𝒍𝒂𝒎 𝑫𝒖𝒓𝒖ş 𝑺ü𝒓𝒆𝒔𝒊+𝑻𝒐𝒑𝒍𝒂𝒎 𝑯𝒂𝒛𝚤𝒓𝒍𝚤𝒌 𝑺ü𝒓𝒆𝒔𝒊+𝑻𝒐𝒑𝒍𝒂𝒎 𝑻𝒓𝒂𝒏𝒔𝒇𝒆𝒓 𝑺ü𝒓𝒆𝒔𝒊)

𝑷𝒍𝒂𝒏𝒍𝒂𝒏𝒂𝒏 Ü𝒓𝒆𝒕𝒊𝒎 𝑺ü𝒓𝒆𝒔𝒊
1,0 = ((8+8+8) ×60 )−0
(8+8+8) ×60 → 8 saatlik 3 vardiyamız var. Duruş ve hazırlık gibi bekleme süreleri olmadığından kullanılabilirlik değeri %100.

PER = ∑(𝑩𝒊𝒓𝒊𝒎 Ü𝒓ü𝒏 𝒊ç𝒊𝒏 Ü𝒓𝒆𝒕𝒊𝒎 𝑺ü𝒓𝒆𝒔𝒊 × 𝑩𝒊𝒓𝒊𝒎 Ü𝒓ü𝒏ü𝒏 Ü𝒓𝒆𝒕𝒊𝒎 𝑴𝒊𝒌𝒕𝒂𝒓𝚤)

𝑷𝒍𝒂𝒏𝒍𝒂𝒏𝒂𝒏 Ü𝒓𝒆𝒕𝒊𝒎 𝑺ü𝒓𝒆𝒔𝒊 − (𝑻𝒐𝒑𝒍𝒂𝒎 𝑫𝒖𝒓𝒖ş 𝑺ü𝒓𝒆𝒔𝒊+𝑻𝒐𝒑𝒍𝒂𝒎 𝑯𝒂𝒛𝚤𝒓𝒍𝚤𝒌 𝑺ü𝒓𝒆𝒔𝒊+𝑻𝒐𝒑𝒍𝒂𝒎 𝑻𝒓𝒂𝒏𝒔𝒇𝒆𝒓 𝑺ü𝒓𝒆𝒔𝒊)

0,6 = (𝟗𝟓 𝒂𝒅𝒆𝒕 × 𝟐𝒅𝒌)(𝟏𝟒𝟒 𝒂𝒅𝒆𝒕 × 𝟐𝒅𝒌)(𝟏𝟗𝟖 𝒂𝒅𝒆𝒕 × 𝟐𝒅𝒌) ((8+8+8) ×60 )−0 → Sistemimizde üretim süreleri 2 dakika ve üretim adetleri sırasıyla 95,144 ve 198 olan 3 farklı üretim akış kaydımız vardı.
QUA = ∑(Ü𝒓𝒆𝒕𝒊𝒎 𝑴𝒊𝒌𝒕𝒂𝒓𝚤−𝑭𝒊𝒓𝒆 𝑴𝒊𝒌𝒕𝒂𝒓𝚤) ∑(Ü𝒓𝒆𝒕𝒊𝒎 𝑴𝒊𝒌𝒕𝒂𝒓𝚤)
0,97 = (𝟗𝟓+𝟏𝟒𝟒+𝟏𝟗𝟖)−(𝟓+𝟔+𝟐) → İş emirlerine girilen üretim ve fire adetlerini formüle yerleştirdik. (𝟗𝟓+𝟏𝟒𝟒+𝟏𝟗𝟖)
Bu verilere ilişkin detayları görebilmek için "Detay Bilgi" sekmesi ve mavi buton altındaki "Grafik Verisi" seçeneği kullanılabilir. Ayrıca iş emirlerine ilişkin Gantt tablosuna da "Gantt Gösterimi" sekmesinden ulaşmak mümkündür.

#### Kapasite Planlama Uygulamasının Kullanıldığı Senaryo

Çizelgeleme modülünü kullanmayıp kapasite planlama uygulaması kullanan bir kullanıcının fabrika son durumu ekranını kullanabilmesi için gerekli olan vardiya planlarına ve ürün birim sürelerine sırasıyla; MRP modülü altındaki fabrika çalışma takvimi ve rota tanımlama ekranlarından ulaşılmaktadır. Fakat burada bilinmesi gereken şudur ki; kapasite planlama uygulaması kullanıcıları için fabrika son durumu ekranı desteği 9.0.22 setiyle birlikte gelmiştir. Bundan önceki setlerde bu senaryoda anlatılan uyarlama gerçekleştirilemeyecektir.
Fabrika çalışma takvimi tarafı, kapasite planlama uygulamasının kullanılmadığı senaryo ile aynı olduğundan bu senaryoda yeniden gösterilmeyecektir. Aynı vardiya planı ve fabrika çalışma takvimiyle bu senaryoya ait örnek uyarlama da yapılacaktır.
İkinci aşama olan birim zaman tanımlamalarına geçmeden önce ise kapasite planlarıyla ilgili kontrol edilmesi gereken bir parametre vardır. Kapasite planlama verilerinin fabrika son durumu ekranında kullanılabilmesi için, MRP Parametreleri  MRP II yolundaki "Kapasite Planlama Parametreleri" alanında "Planlama Verisi" parametresinin "Kapasite planlama verisi kullanılsın" olarak ayarlanmış olması gerekmektedir. (Bkz. Ekran Görüntüsü 11)
![](../../_assets/030361b62777d0bbc7be.png)**Ekran** **Görüntüsü** **11**
Bunun haricinde kapasite planlama uygulaması kullanıcıları için fabrika son durumu ekranı kullanımında kontrol edilmesi gereken bir parametre daha vardır. Bu parametre üretim akış kaydı ekranında makine bilgisinin de sorulmasını sağlamaktadır ki fabrika son durumu ekranının tam olarak çalışabilmesi için makine bilgisi gereklidir. İlgili parametre, üretim akış parametreleri altındaki "Makine Bilgisi Okunsun" parametresidir. (Bkz. Ekran Görüntüsü 12) Bu parametrenin açılmasıyla, üretim akış kaydı ekranına "Makine No" alanı eklenecektir.
![](../../_assets/d1506beba2611d5b55c2.png)**Ekran** **Görüntüsü** **12**
Vardiya planları ve kapasite planlama uygulamasıyla fabrika son durumu ekranını kullanmak için önemli olan parametrelerden bahsettikten sonra ürünlerin birim zamanlarının belirlenmesiyle devam edebiliriz. Elimizde ilk senaryoda tanımladığımız MAMUL10, OP10, MAK10 ve IST10 vardı. Bu tanımlamaları yeni senaryoda da kullanmaya devam edeceğiz.
![](../../_assets/589505750b2d96664927.png)

Öncelikle Üretim-MRP-Kayıt-Rota Tanımlama yolunu izleyerek rota tanımlama işlemini tamamlayalım. Bunun için rota tanımlama ekranının "Stok Seçim" sekmesinden MAMUL10'u seçelim ve ardından "Rota" sekmesine geçelim.
**Ekran** **Görüntüsü** **14**
![](../../_assets/5699c31029111e6be8a0.png)![](../../_assets/15f729a4361e36989a6d.png)**Ekran** **Görüntüsü** **13 ve 14**

Rota sekmesi üzerinden MAMUL10 için operasyon seçimini OP10 ve makine seçimini MAK10 olarak yapalım. Üretim süremiz ise bu senaryo için 1 adet üründe 3 dakika olsun. (Bkz. Ekran Görüntüsü 13)
Son ürünümüze ait birim zaman tanımlamasını da yaptıktan sonra iş emri girişleri ve bu iş emirlerine istinaden üretim akış kaydı girişleri yapılması kalmaktadır. Bir önceki senaryoda girdiğimiz 3 adet iş emrini bu senaryo için de kullanalım. Bir önceki senaryodan farklı olarak bu 3 iş emri için 3 adet yeni üretim akış kaydı oluşturalım çünkü bu senaryoda makine numarası alanlarını da doldurmamız gerekmektedir. (Bkz. Ekran Görüntüsü 14)
Bütün bu işlemler sonrasında fabrika son durumu ekranını da aynı tarih aralığı için çalıştıralım. Kapasite planlama uygulaması kullanılan senaryomuz için ilk senaryodakiyle aynı iş emirlerini ve üretim akış kayıtlarını kullandık, yalnızca farklı görebilmek açısından ürünümüzün birim zamanını 2 dakika yerine 3 dakika olarak girdik. Bu koşullar altında aynı tarih aralığında çalıştırdığımız fabrika son durumu ekranının, OEE verisinin ilk senaryodakinden farklı olmasını beklemeliyiz. (Bkz. Ekran Görüntüsü 15)
![](../../_assets/f0e377a644dc4c811852.png)**Ekran** **Görüntüsü** **15**
Fabrika son durumu ekranında görüldüğü üzere, farklı birim zamanlar için hesaplanan OEE ve PER değerleri beklediğimiz gibi farklı hesaplandı. Son olarak aynı veriye ait Gantt şeması ise 16. ekran görüntüsünde paylaşılmıştır.
![](../../_assets/f45021bf449b4c0be992.png)**Ekran** **Görüntüsü** **16**
Tüm bu işlemler sonunda kapasite planlama uygulaması kullanılmayan ve kullanılan 2 farklı senaryo için fabrika son durumu ekranının hangi adımlar izlenerek kullanılabileceği gösterilmiş oldu. Bu örnek uyarlama dokümanında değinilmeyen detaylara ulaşmak için ise, fabrika son durumu izleme tanıtım dokümanından ya da fabrika son durumu izleme Webinar'ından faydalanılması gerekmektedir.
