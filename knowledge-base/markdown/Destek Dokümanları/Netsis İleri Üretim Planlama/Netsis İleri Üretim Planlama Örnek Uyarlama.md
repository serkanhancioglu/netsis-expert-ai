---
title: "Netsis İleri Üretim Planlama Örnek Uyarlama"
page_id: "80090127"
product: "netsis-3-enterprise"
depth: 3
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis İleri Üretim Planlama"
  - "Netsis İleri Üretim Planlama Örnek Uyarlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis İleri Üretim Planlama / Netsis İleri Üretim Planlama Örnek Uyarlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWE5MDgzYTNhLTA2MmMtNDQ5My04NjViLTU3NjMyOWI3OTM1NyZsaW5rPWM3YzIwZDgwLTQwZWItNDYxMi1hZmZhLTIzZmQ2YTE1OWQ4YSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=a9083a3a-062c-4493-865b-576329b79357&link=c7c20d80-40eb-4612-affa-23fd6a159d8a&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-ileri-uretim-planlama-ornek-uyarlama_80090192_80090127.html"
source_version: "2022-11-02T16:04:12.953+03:00"
source_bytes: 4006010
fetched_at: "2026-09-13T04:25:07+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis İleri Üretim Planlama Örnek Uyarlama

Netsis İleri Üretim Planlama Örnek Uyarlama ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

![](../../_assets/edc5ebdf4771ceeea3b6.png)**Ekran** **Görüntüsü** **1**
İleri üretim planlama modülünün kullanım ve ekran detaylarına ait "İleri Üretim Planlama Modül Tanıtım Dokümanı" daha önce paylaşılmıştı. Bu dokümanda ise ileri üretim planlama modülü kullanılarak uyarlaması yapılan örnek bir senaryoya ait uyarlama aşamaları anlatılacaktır. Örnek uyarlama dokümanı incelenirken modül tanıtım dokümanından da yararlanılması önerilmektedir. Uyarlama aşamalarını özet olarak sırasıyla görebilmek için modül tanıtım dokümanının "İçindekiler" sayfasına bakılabilir.
İleri üretim planlama modülü üzerindeki tanımlamalara başlamadan önce aşağıdaki gibi üretim akışı olan bir işletmemiz olduğunu varsayalım. (Bkz. Ekran Görüntüsü 1) Makine ve operasyon isimlerine ilişkin tablo ise ekran görüntüsü 2'de görülebilir.
Ekran görüntüsü 1'deki üretim sisteminde 2 noktadan ham madde girişi olmakta ve bu 2 noktadan paralel şekilde ilerleyen yarı mamuller bulunmaktadır. Sistem içindeki malzeme akışı oklarla gösterilmiştir. Ayrıca sistemdeki stok kodları da ilgili akış okları üzerinde belirtilmiştir. Örneğin; YM1_001_03 numaralı stok kodu KESME_003 kodlu makinenin operasyonu sonucunda oluşmaktadır ve sıradaki işlem için KESME_004 kodlu makineye gitmektedir. Kesme istasyonundan giren ham maddeler Kesme 1-Kesme 2-Kesme 3-Kesme 4-Pres-Torna 1-Montaj operasyonlarını takip eden yolu izlerken, torna istasyonundan giren ham maddeler ise Torna 2-Delik Delme-Montaj operasyonlarını takip eden bir yol izlemektedir. Ardından bu 2 yolu izleyerek oluşan yarı mamuller montaj operasyonunda birleştirilerek mamule dönüştürülmektedir.
![](../../_assets/365973ba9719ea174e91.png)**Ekran** **Görüntüsü** **2**
Yukarıdaki ekran görüntülerinde ayrıntılarına yer verilen örnek üretim tesisine ait reçeteleri oluşturmak için "Ürün Konfigüratörü" kullanılmıştır. Ürün Konfigüratörü ekranına ulaşabilmek için Üretim-Üretim-Kayıt yolu izlenmelidir. (Bkz. Ekran Görüntüsü 3)
İlgili üretim örneğinde akış sonunda mamul 11, 12 ve 13 olmak üzere 3 farklı mamul oluşmaktadır. Bu 3 farklı mamul de aynı ham maddelerden üretilmektedir ancak ham maddelerden üretilen yarı mamuller farklılık göstermektedir. Bu sebeple bu 3 mamulün oluşması sırasında üretilen yarı mamulleri içeren 3 farklı malzeme akışı vardır. Her 3 mamul için ürün konfigüratöründe oluşturulmuş 3 malzeme akışına ait görseller ekran görüntüsü 4'te görülebilir.
![](../../_assets/a30ed86c998419c8a09f.png)**Ekran** **Görüntüsü** **3**
![](../../_assets/0187d8b5b307166e6855.png)![](../../_assets/08c92066998ba45634c2.png)![](../../_assets/70a89b76263287794220.png)**Ekran** **Görüntüsü** **4**
Ürün konfigüratöründe baz mamule ilişkin bileşen ve operasyon ilişkileri girilirken stok kartı, operasyon ve reçete kayıtları da otomatik olarak yapılacaktır. Fakat bu kayıtları yapmak için konfigüratör ekranı kullanılmak istenmezse öncesinde ileri üretim çizelgeleme modülünden operasyon tanımlamaları ve stok modülünden stok kartı kayıtları yapılabilir. Önceden kayıtların yapılmış olduğu durumda konfigüratör ekranındaki rehber menüleri kullanarak operasyon ve stok kodu seçimleri yapılabilir. Ardından üretim modülü altındaki "Reçete Kaydı" veya "Ürün Konfigüratörü" ekranları üzerinden reçeteler tanımlanabilir. Reçete kaydı sırasında operasyon bilgilerinin girilmesi zorunlu değildir, çünkü rota bilgileri ileri üretim çizelgeleme menüsü altındaki "Rota Tanımlama" ekranı üzerinden yapılacaktır. Bu örnekte reçetenin daha anlaşılır olması için reçete tanımlarına operasyonlar da eklenmiştir.
Ürün konfigüratörü yardımıyla reçete yapısının oluşturulmasının ardından vardiya tanımlarının yapılması gerekmektedir. Örnek üretime ait vardiya yapısı bilgileri ekran görüntüsü 5'teki tabloda gösterilmiştir.
![](../../_assets/b6ff1ed4e0822ae6965a.png)**Ekran** **Görüntüsü** **5**
Yukarıdaki tabloda verilen bilgilere göre ileri üretim çizelgeleme modülündeki vardiya tanımlama ekranından oluşturulan vardiyalara ilişkin görüntüler için ekran görüntüsü 6'ya bakılabilir.
![](../../_assets/10714609ab9b528a40c0.png)![](../../_assets/f62362ea1c26255c4754.png)![](../../_assets/f883ca4f9d408cbb267d.png)**Ekran** **Görüntüsü** **6**
Ekran görüntüsü 5'te verilen bilgilere istinaden 4 farklı vardiya tanımlaması yapılmıştır. Bu vardiyalar kullanılarak oluşturulan "Fabrika Çalışma Takvimi" ise ekran görüntüsü 7'de görülmektedir.
![](../../_assets/3bfcafdce5e4343886e3.png)İleri üretim planlama uygulamasının bir sonraki adımı olan "İş İstasyonu Tanımlama" adımı için aşağıdaki bilgi verilmiştir. (Bkz. Ekran Görüntüsü 8)
![](../../_assets/a1b184d9128a9c44eaa3.png)**Ekran** **Görüntüsü** **8**
Verilen bilgilere istinaden yapılan istasyon tanımlamaları için ekran görüntüsü 9'a, montaj istasyonu özelindeki vardiya planı tanımı için ise ekran görüntüsü 10'a bakılabilir.
![](../../_assets/292c7b86a13988500517.png)**Ekran** **Görüntüsü** **9**
![](../../_assets/c1581d2a9517ae74b52f.png)**Ekran Görüntüsü 10**
Uyarlaması yapılmakta olan bu örnek üretim sistemi için herhangi bir grup tanımı yapılmasına ihtiyaç duyulmamıştır. Bu yüzden grup tanımlama adımı atlanarak makine tanımlama adımına geçilmiştir. Makine detayında aşağıdaki bilgi verilmiştir. (Bkz. Ekran Görüntüsü 11)
![](../../_assets/f7f49680a7f0c42ed59c.png)**Ekran** **Görüntüsü** **11**
![](../../_assets/dc8cd0c79562d71c5341.png)**Ekran** **Görüntüsü** **12**

Bu bilgi gereği vardiya tanımlama ekranında 24 saat çalışma tanımlanarak yeni bir vardiya oluşturulmuştur. (Bkz. Ekran Görüntüsü 12)
![](../../_assets/02436dc7d6bcaf1145aa.png) **Ekran** **Görüntüsü** **13**

Verilen bilgilere istinaden yapılan makine tanımlamaları için ekran görüntüsü 13'e, TORNA_001 makinesi özelindeki vardiya planı tanımı için ise ekran görüntüsü 14'e bakılabilir.
![](../../_assets/828b7126123818f01014.png)**Ekran** **Görüntüsü** **14**
İleri üretim planlama için sıradaki adım olan "Operasyon Tanımlama" adımına ilişkin detaylar için 15. ekran görüntüsüne bakılabilir.
![](../../_assets/f939b68b901a46347b62.png)**Ekran** **Görüntüsü** **15**
Bu örnek uyarlamada pres operasyonunda kullanılan 2 farklı kalıp olduğu varsayılmaktadır. Bu 2 kalıba ait tanımlamalar için ekran görüntüsü 16'ya bakılabilir.
![](../../_assets/409a22cb457eab75da3a.png)**Ekran** **Görüntüsü** **16**
Kalıp tanımlamaları yapıldıktan sonra ekran görüntüsü 17'deki bilgilere göre hazırlık süresi tanımları yapılarak uyarlamaya devam edilecektir.
![](../../_assets/58531a4b0945e9afe593.png)**Ekran** **Görüntüsü** **17**
Yukarıdaki 3 bilgiye göre yapılan hazırlık süresi tanımlamaları için sırasıyla ekran görüntüsü 18, 19 ve 20'ye bakılabilir.
![](../../_assets/0c6b2598cfef706b51d7.png)**Ekran** **Görüntüsü** **18**
![](../../_assets/8b6b73debeb04b2411b1.png)**Ekran** **Görüntüsü** **19**
![](../../_assets/70443f1863752969ec17.png)**Ekran** **Görüntüsü** **20**
İleri üretim planlama modülü içindeki hazırlık tanımlamalarından sonra "Rota Tanımları" yapılmalıdır. Sistem üzerinde şimdiye kadar halihazırda mamul, yarı mamul, operasyon tanımlamaları yapılmış ve ürün konfigüratörü yardımıyla reçeteler oluşturulmuştu. Rota tanımlama aşamasında ise bu mamul ve yarı mamullerin sırasıyla hangi işlemlerden geçtiği tanımlanacaktır.
İleri üretim planlama uygulamasına ait dokümanda da bahsedildiği gibi, bu aşamaya kadar tüm operasyonlar ve her tekil operasyon sonucu ortaya çıkan mamul/yarı mamuller tek tek tanımlanmış olmayabilirdi. Örneğin bu uyarlamada Kesme 1-Kesme 2-Kesme 3-Kesme 4 operasyonları ve bu operasyonların ardından oluşan yarı mamuller tek tek tanımlandı. Ancak tüm kesme operasyonları tek bir operasyonmuş varsayımı yapılarak tek bir kesme operasyonu tanımlanabilir ve yalnızca tüm kesme işlemleri sonrasında ortaya çıkan yarı mamul tanımlanmış olabilirdi. Bu durumda bu yarı mamulün rotasında sırasıyla Kesme 1-Kesme 2-Kesme 3-Kesme 4 şeklinde dört operasyon bulunacaktı ve diğer 3 kesme operasyonunun sonucunda oluşan ara stokların takibi mümkün olmayacaktı. Burada verilecek karar tamamıyla stratejiktir ve üretim sisteminin ne detayda takip edilmek istendiğine bağlıdır.
Örnek uyarlama için oluşturulan rotaların tanımları ve eşleştirme ekranları aşağıda görülmektedir. (Bkz. Ekran Görüntüsü 21,22,23,24,25,26,27,28 ve 29)
![](../../_assets/0b7c48578564a76b7846.png)![](../../_assets/5fe2965aa37d350dd3a1.png)**Ekran** **Görüntüsü** **21**
![](../../_assets/809cda98ae1f1d0828f3.png)![](../../_assets/afe5d1ba8e58d0d766b0.png)**Ekran** **Görüntüsü** **22**
![](../../_assets/42bb6694db31124130c1.png)![](../../_assets/13f89b83443e85e90e50.png)**Ekran Görüntüsü 23**
![](../../_assets/008ca6949e5ed5f84840.png)![](../../_assets/87d5df6546b0c0e72b2b.png)**Ekran** **Görüntüsü** **24**
![](../../_assets/5aa77b2e9c663162268e.png)![](../../_assets/46a6b5cf302612324bb6.png)**Ekran** **Görüntüsü** **25**
![](../../_assets/39acc21a361582a48bce.png)![](../../_assets/912fb1f4e6f8c6e9591f.png)**Ekran Görüntüsü 26**
![](../../_assets/9e366fe9896632268344.png)![](../../_assets/100c22b3ff890d8a53c7.png)**Ekran** **Görüntüsü** **27**
![](../../_assets/4d277542e2e13827f3db.png)![](../../_assets/dcb8df22e1111451a4e3.png)**Ekran** **Görüntüsü** **28**![](../../_assets/a9ad99be08d5e58466d4.png)![](../../_assets/089388dda9f0d21a8eb7.png)**Ekran Görüntüsü 29**
![](../../_assets/d67fd39064ad2cfca955.png) **Ekran** **Görüntüsü** **30**

Tüm operasyon rotalarının tanımlanmasının ardından zorunlu olarak yapılması gereken bir diğer tanım ise operasyon-makine eşleştirmeleridir. Hangi operasyonların hangi makinelerde yapılabildiği ekran görüntüsü 2'de belirtilmişti. Bu bilgilere ek olarak üretim sürelerine ilişkin tablo da paylaşılmıştır. (Bkz. Ekran Görüntüsü 30)
30. ekran görüntüsüne istinaden yapılan operasyon-makine eşleştirmelerine ait örnekler için ekran görüntüsü 31,32,33,34,35,36 ve 37'ye bakılabilir.
![](../../_assets/73c4b37aee52d59f6d60.png)**Ekran** **Görüntüsü** **31**
![](../../_assets/a17e998c94e8818aaa76.png)**Ekran** **Görüntüsü** **32**
![](../../_assets/b68a0e4297cdbb1c0ff3.png)**Ekran** **Görüntüsü** **33**
![](../../_assets/1d301b808a4d086a7b46.png)**Ekran** **Görüntüsü** **34**
![](../../_assets/ff29d187337186f53e03.png)**Ekran** **Görüntüsü** **35**
![](../../_assets/e25ec8f9a219644fa0b8.png)**Ekran** **Görüntüsü** **36**
![](../../_assets/8d4e633ac0a5fcd97221.png)**Ekran** **Görüntüsü** **37**
Bu örnek uyarlamada tanımlanan 2 adet kaynaktan kalıp 1'in birinci öncelikle, kalıp 2'nin ise ikinci öncelikle pres operasyonu sonucunda oluşan YM1_001_05 yarı mamulünün üretimi sırasında kullanıldığı varsayımıyla ekran görüntüsü 38'deki operasyon-kaynak eşleştirmeleri yapılmıştır.
![](../../_assets/5ac0400842007f069166.png)**Ekran** **Görüntüsü** **38**
Bu örnek uyarlamada bir kural bilgisi verilmediğinden kural tanımlama adımı atlanmıştır. Ekran görüntüsü 39'da verilen bilgiler ise sisteme girilmesi gereken müşteri siparişlerini göstermektedir.
![](../../_assets/9aa7669cad9839cecced.png)**Ekran** **Görüntüsü** **39**
![](../../_assets/c2f8868217155207eebe.png)**Ekran** **Görüntüsü** **40**

İlgili siparişlerin girişi tamamlandıktan sonra çizelge modelleme aracı yardımıyla bir algoritma tanımlama adımına geçilmiştir. Örnekte enjeksiyon operasyonu bulunmadığı için yalnızca genel algoritmayı içeren bir model yapılmıştır. Ekran görüntüsü 40 ve 41'de örnek model ve modele ait algoritma opsiyonları görülebilir.
![](../../_assets/e2042ce5b0806a20a85b.png)**Ekran** **Görüntüsü** **41**
Modelleme adımının da tamamlanmasından sonra oluşturulan müşteri siparişlerine ait "Gereksinim Planlama Oluşturma" işlemi yapılmış ve ardından "Malzeme Gereksinim Planlama" çalıştırılmıştır. (Bkz. Ekran Görüntüsü 42 ve 43)
![](../../_assets/222240389e41ee8b1c64.png)**Ekran** **Görüntüsü** **42**
![](../../_assets/1a2073c2f44f6dc4e842.png) **Ekran** **Görüntüsü** **43**
Tüm bu işlemlerden sonra çizelgeyi oluşturmak için "İleri Üretim Planlama" ekranına gidilmiştir. Burada kayıtlar "MRP Sonuçlarından Getir" seçeneğiyle getirilmiş ve model olarak 40. ekran görüntüsünde nasıl oluşturulduğu gösterilen MODEL\_ÖRNEK kullanılmıştır. (Bkz. Ekran Görüntüsü 44)
![](../../_assets/14dfaf2b7afd866ad654.png)**Ekran** **Görüntüsü** **44**
MRP sonuçlarından kayıtları getirdikten sonra "Çizelgeyi Oluştur" butonu tıklanarak çizelge oluşturulabilir. (Bkz. Ekran Görüntüsü 45) Böylece MRP sonuçlarının önerdiği iş emri miktarları ve teslim tarihleri üzerinden çizelgeleme sonuçları alınmış olacaktır. Ancak çizelgelemeyi MRP sonuçları üzerinden yapmak zorunlu değildir. "Kayıtları Getir" butonu altındaki "İş Emirlerini Getir" seçeneği ile sistemde bulunan açık iş emirlerinin çizelgelenmesi ya da "Excel'den Yükle" seçeneği ile Excel üzerinden serbest şekilde aktarılan ihtiyaçların çizelgelenmesi de mümkündür.
![](../../_assets/28293fa9c47aacd9e389.png)**Ekran** **Görüntüsü** **45**
![](../../_assets/4135fc5937e4c8a986f1.png)**Ekran** **Görüntüsü** **46**

Çizelge oluşturulduktan sonra istenen raporlar alınabilir, mevcut çizelge taslak olarak kaydedilebilir, iş emri sabitleme yapılabilir ya da MRP kayıtlarından seçimler filtrelenerek yeni bir çizelge oluşturulabilir. (Bkz. Ekran Görüntüsü 46 ve 47)
![](../../_assets/9e29d07d78eb952af03b.png)**Ekran** **Görüntüsü** **47**
Bu ekranla ilgili diğer tüm detaylar için "İleri Üretim Planlama Modül Tanıtım Dokümanı" incelenebilir. Malzeme gereksinim planlama konusu bu dokümanın kapsamına girmediği için bu konudaki detaylara burada yer verilmemiştir. MRP ile ilgili detaylar için MRP dokümanlarına ayrıca bakılması gerekmektedir.
