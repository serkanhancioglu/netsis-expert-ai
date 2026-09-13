---
title: "Netsis İleri Üretim Planlama"
page_id: "66237164"
product: "netsis-3-enterprise"
depth: 2
is_section: true
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis İleri Üretim Planlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis İleri Üretim Planlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTMzMWZiMWUyLTQ0MTEtNDBiYy05OGFhLTZhYjdhYjY3ZTU1ZiZsaW5rPTI2NTJjYWJlLTE3NDctNGE5YS05MTc0LWQ0YzMxY2IwY2Q2ZiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=331fb1e2-4411-40bc-98aa-6ab7ab67e55f&link=2652cabe-1747-4a9a-9174-d4c31cb0cd6f&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-ileri-uretim-planlama_80090065_66237164.html"
source_version: "2022-11-02T16:00:57.067+03:00"
source_bytes: 6311345
fetched_at: "2026-09-13T04:25:08+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis İleri Üretim Planlama

Netsis İleri Üretim Planlama ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

> [!NOTE]
> İlgili özelliğin anlatımını içeren webinar kaydına ulaşmak için [tıklayınız.](https://register.gotowebinar.com/recording/3264764878144964358)

İleri üretim planlama uygulaması, bir işletmede tamamlanması planlanan siparişlerin hangi istasyonlarda, hangi sırayla ve hangi kaynaklar kullanılarak üretilmesi gerektiğini hesaplamaya ve sonuçları bir Gantt şeması üzerinde çizelgelemeye yarar. Böylelikle doğru zamanda, doğru üretim, optimum kaynak kullanımıyla gerçekleştirilir ve işletme hedeflerine ulaşılması sağlanmış olur. Oluşturulan çizelgelere ait çok sayıda rapor seçeneği uygulamada desteklenmektedir. Bunlara ek olarak çizelge üzerindeki iş emri sabitleme, kural tanımları ve benzeri desteklerle kullanıcının üretim planlarına müdahale etmesi de mümkün kılınmıştır.

İleri üretim planlama uygulamasının Netsis üzerindeki hangi modüllerden veri aldığına dair bilgi akış diyagramı Ekran Görüntüsü 1'de görülmektedir.

![](../../_assets/4a83de4b60cf2b75cff9.png)**Ekran** **Görüntüsü** **1**

Uygulamanın hatasız şekilde çalışabilmesi için modül üzerindeki; vardiya, iş istasyonu, makine, operasyon, kaynak gibi sabit tanımlamaların adım adım ve doğru şekilde yapılması gereklidir. Bu dokümanda, bahsedilen adımlar sırasıyla ve ayrıntılı şekilde anlatılmıştır. İleri üretim planlama modülünün girdi ve çıktıları Ekran Görüntüsü 2'de özet halinde gösterilmiştir. Ekran görüntüsünde görülen tüm girdi ve çıktılara ait detay ve açıklamalara dokümanda sırasıyla yer verilmiştir.

![](../../_assets/43d4c06106219aa044eb.png)**Ekran** **Görüntüsü** **2**

İleri üretim planlama modülü kullanılmadan önce işletmeye ait üretim reçete yapısının iyi kurgulanmış ve program üzerinde oluşturulmuş olması gerekmektedir. Önerilen, her operasyon geçişi için yeni bir stok kodu (yarı mamul) oluşturulmasıdır. Bu şekilde tanımlama yapıldığı takdirde operasyonlar arasında mamul/yarı mamul stok bakiyesi takibi yapılabilir. Çok fazla sayıda operasyonu olan ve bu şekilde tanımlama yapmak istemeyen işletmelerde, birkaç operasyonu birleştirip, bu operasyonlar tek bir operasyonmuş gibi tanımlama yapmak da mümkündür. Ancak bu şekilde çalışacak işletmelerde operasyon tanımlamaları kritiktir. Eğer ara stok takibi yapılmak istenen operasyonlar varsa, birleştirilmesi düşünülen operasyonlar buna göre belirlenmelidir. İleri üretim planlama uygulamasının kullanılabilmesi için ileri üretim planlama ek lisansına sahip olmak gereklidir. Ayrıca lisans sahibi kullanıcıların Üretim-MRP-Kayıt-MRP Parametreleri yolunu izleyerek MRP II sekmesindeki "İleri Üretim Planlama" parametresini açarak uygulamayı aktifleştirmesi gerekmektedir. Bu işlemleri tamamlayan kullanıcılar Üretim-MRP-Kayıt-İleri Üretim Çizelgeleme menüsü altından "Vardiya Tanımlama" ekranına giriş yaparak uygulamayı kullanmaya başlayabilirler. (Bkz. Ekran Görüntüsü 3)

![](../../_assets/46db5c45017702d7461c.png)**Ekran** **Görüntüsü** **3**

#### Vardiya Tanımlama

İleri üretim planlama uygulamasının uyarlanmasına vardiya tanımlamaları ile başlamak gerekir. İşletmenin çalışma gün ve saatleri bu ekran üzerinden tanımlanabilir. (Bkz. Ekran Görüntüsü 4)

![](../../_assets/d105bc08f3228d15b641.png)**Ekran** **Görüntüsü** **4**

İşletmeye ait kaç farklı vardiya tipi varsa hepsi bu ekran üzerinden tanımlanmalıdır. Vardiya kodu, ismi ve açıklama alanları serbest şekilde doldurulabilir. Tanımlaması yapılan vardiyaya ait etkinlik tipleri ise tek tek seçilerek başlangıç-bitiş saatleri girilmeli ve ekranın altındaki grid alanına gönderilerek kaydedilmelidir. Çalışma, mola, yemek arası, duruş ve fazla mesai olmak üzere 5 çeşit etkinlik tipi bulunmaktadır. Bu etkinliklerden mola, yemek arası ve duruş tanımlanan saat aralıklarına uygulama tarafından iş planlanmaz. İleri üretim planlama modülünde fazla mesai etkinliğinin de varsayılan etkinlik tipi duruştur. Bu etkinlik tipinin gerçek anlamda fazla mesai gibi çalışması istendiği takdirde, kapasite planlama ekranından gerekli ayarlar yapılmış olmalıdır. Eğer tek tip ve tam gün süren vardiyalar mevcutsa, başlangıç-bitiş saatlerinin her ikisine de aynı değer yazılarak tam gün parametresi işaretlenmelidir.

Vardiya tanımlamaları yapılırken gün içinde başlayıp ertesi gün tamamlanan etkinlikler varsa başlangıç- bitiş saatine bu girişler yapıldığında ekrana bir onay mesajı gelecektir. Bu mesaj altındaki butonlardan "Evet" e tıklanması halinde "Sonraki Gün" parametresi otomatik işaretlenecektir. (Bkz. Ekran Görüntüsü 5)

![](../../_assets/a898ec12e33e7816f6cd.png)**Ekran** **Görüntüsü** **5**

#### Fabrika Vardiya Planı Tanımlama

İşletmede var olan tüm vardiyalar tanımlandıktan sonra bu vardiyalardan oluşan çalışma takvimi oluşturulmalıdır. Bu, zorunlu bir tanımlamadır. Üretim-MRP-Kayıt-İleri Üretim Çizelgeleme yolu takip edilerek "Fabrika Vardiya Planı Tanımlama" ekranı açılır. Fabrika Vardiya Planı Tanımlama ekranı üzerinde farklı vardiya planları oluşturulabilir. Farklı vardiya planlarıyla çizelgeleme çalıştırılarak farklı senaryoları karşılaştırmak mümkündür. Her bir plan için bir plan numarası verilmelidir. Ekran üzerindeki açıklama alanı serbestçe doldurulabilir. "Varsayılan" parametresini seçerek varsayılan vardiya planı belirlenebilir. Bu seçeneğin bir vardiya için işaretli olduğu durumlarda, vardiya plan numarası sorulan ekranlara otomatik olarak bu vardiya planı gelecektir. (Bkz. Ekran Görüntüsü 6)

![](../../_assets/98666fd8b4985fcee1eb.png)**Ekran** **Görüntüsü** **6**

Fabrika çalışma takvimi ekranında bulunan başlangıç-bitiş tarihleri oluşturulan vardiya planının geçerlilik tarihleridir. Bitiş tarihi boş bırakıldığı takdirde ilgili vardiya planı süresiz olarak geçerli kılınır.

Ekranın üst kısmında bulunan grid alanındaki seçim kutucuklarından vardiya planına alınmak istenenler çift tıklanmalıdır. Yapılan bu seçimlerin haftanın hangi günlerinde geçerli olacağı ise gridin solunda bulunan "Haftanın Günleri" alanından seçilmelidir. Vardiya planını oluştururken seçilen vardiyaların zaman bakımından çakışması halinde kullanıcıya bir hata mesajı gelecektir. Plan oluşturma sırasında buna dikkat edilmesi gereklidir. Ardından "Değişiklikleri Kaydet" butonuna tıklanarak vardiya planı alt gride atılmalıdır. Bu şekilde kaydedilmiş olur.

Vardiyalar için gün seçimi konusunda özelden genele bir hiyerarşik yapı vardır. Örneğin; haftanın tüm günleri için seçim yapılmış bir vardiya ile sadece pazar günü için seçim yapılmış bir vardiya birlikte bir vardiya planı oluşturursa, en özel geçerli olacak şekilde bir çalışma mantığı yürütülür. Yani bu örnekte pazar günleri için pazar seçimli vardiya, diğer günler için haftanın tüm günleri için seçilmiş vardiya geçerli olacaktır.

Vardiya planları için belirlenen başlangıç-bitiş tarihlerine göre dönemsel çakışma olması durumunda ise çizelgelemenin çalıştırıldığı tarihe en yakın başlangıç tarihine sahip vardiya planı geçerli olacaktır.

Yine aynı ekranda bulunan vardiya planı kopyala butonu ile istenilen bir vardiya, numarası o anda açılan pencere ile numarası belirlenecek başka bir vardiyaya kopyalanabilir.(Bkz. Ekran Görüntüsü 7) Yine benzer şekilde alt gridde bulunan satırlardan biri seçilerek "Başka Güne Kopyala" butonu ile kullanıcı tarafından belirlenecek gün ya da günlere kopyalanabilir. (Bkz. Ekran Görüntüsü 8) Ekrandaki "Plan İzleme" butonuna tıklanarak ise içinde bulunulan günden itibaren 1 haftanın vardiya planı görüntülenebilir.

![](../../_assets/235515d7cc1d365ad7f1.png)![](../../_assets/5b90857378684c10224b.png)**Ekran** **Görüntüsü** **7**

![](../../_assets/6fb6df06e29b9d8adffa.png)**Ekran** **Görüntüsü** **8**

#### İş İstasyonu Tanımlama

Vardiya ve fabrika çalışma takvimi tanımlamaları sonrasında iş istasyonlarının da tanımlanması gereklidir. Bunun için Üretim-MRP-Kayıt-İleri Üretim Çizelgeleme yolu takip edilerek "İş İstasyonu Tanımlama" ekranı açılmalıdır. (Bkz. Ekran Görüntüsü 9) İşletmedeki iş istasyonlarının doğru şekilde kurgulanarak bu ekranda doğru şekilde tanımlanması kritiktir. Her bir operasyon tek başına bir iş istasyonu olabileceği gibi aynı ya da benzer işleri yapan makine grupları da birer iş istasyonu olabilir.

![](../../_assets/bbca6aed39315347a6a7.png)**Ekran** **Görüntüsü** **9**

Ekran üzerindeki "İstasyon Kodu" , "İstasyon İsmi" ve "Departman Kodu" alanları serbestçe doldurulabilir. İsim ve departman kodu alanları zorunlu değildir. "Makine Seçim Önceliği" menüsü içinde 5 adet seçenek vardır. Buradan yapılacak seçim çizelgelemenin çalışma mantığını etkilemez, raporlama amaçlı kullanılır. Açıklama yazılmak isteniyorsa "Açıklama" alanı serbestçe kullanılabilir.

Akış tipli istasyona sahip işletmelerde böyle istasyonlar için "Akış Tipli İstasyon" parametresi seçilmelidir. Akış tipli istasyonlarda farklı operasyonlar arka arkaya kesintiye uğramadan yapılır ve araya iş girmesi söz konusu değildir. Bu parametre seçildiğinde altında bulunan "İlk Makine Kodu" alanı aktifleşecektir. Bu alana akışın başladığı makine tanımlanabilir. Eğer ilk makine kodu tanımlanmazsa akış ardışık çalışan makinelerin herhangi birinden başlayıp devam edebilir. Örneğin; akış tipli bir istasyonda sırasıyla 1-2-3-4 numaralı makineler varsa ve ilk makine kodu 1 seçildiyse hep 1. makineden başlayıp bu sırada üretim yapılacaktır. Ancak ilk makine kodu seçili değilse 3. makineden de akış başlayıp 34 sırasıyla üretim yapılabilir.

Ekranda bulunan vardiya planı sekmesi istasyon bazında vardiya planı oluşturmak için kullanılabilir. Bu sekme vardiya planı oluşturma bölümünde anlatılan ekranla aynıdır. (Bkz. Ekran Görüntüsü 10) Burada seçilen istasyon için bir vardiya planı oluşturulursa, hiyerarşik olarak fabrika vardiya planından daha özel bir tanımlama var olacağı için istasyon bazındaki vardiya planı kullanılacaktır.

Bu ekranda bulunan "Kapasite Planlama Bilgileri" alanının ise çizelgeleme açısından bir önemi yoktur.

![](../../_assets/f8f631a68515342dc73c.png)**Ekran** **Görüntüsü** **10**

#### Grup Tanımlamaları

Yukarıda bahsedilen adımların tamamlanmasının ardından grup tanımlamaları yapılmalıdır. Bunun için Üretim  MRP  Kayıt  İleri Üretim Çizelgeleme  Grup Kayıtları yolu izlenmelidir. Bu menünün altından operasyon, makine ya da kaynak grup tanımlamaları ekranlarına ulaşılabilir.

![](../../_assets/011d752c3dc2cc5776b6.png)

Operasyon grubu tanımlama ekranındaki "Grup Kodu" ve "Açıklama" alanları işletme faaliyetlerine uygun kurgu göz önünde bulundurularak serbestçe doldurulabilir. (Bkz. Ekran Görüntüsü 11) Burada tanımlanan operasyon grupları "Operasyon Tanımlama" ekranındaki "Grup Kodu" alanında kullanılabilir. Benzer şekilde ileriki bölümlerde detaylandırılacak olan operasyon-kaynak eşleştirme ekranlarında da operasyon grupları kullanımı kolaylık sağlayabilir.

Makine ve kaynak grubu tanımlama ekranları da operasyon grubu tanımlama ekranıyla aynıdır. Bu

ekranlarda da tanımlamalar aynı şekilde yapılabilir. (Bkz. Ekran Görüntüsü 12)

![](../../_assets/59fd15e7cef9a3d867ea.png)**Ekran** **Görüntüsü** **12**

Bunların haricinde Üretim-Üretim-Kayıt-Ürün Grubu Tanımla yolu izlenerek ürün grubu tanımlamalarının yapılabileceği ekrana ulaşılabilir. Bu ekran üzerinde 2 sekme bulunmakla birlikte "Ürün Grubu Tanımlama" sekmesi yine operasyon grubu tanımlama sekmesiyle aynıdır. Diğer sekmede ise ürün grupları ile mamul eşleştirme işlemi yapılmalıdır. Seçilen grup kodu için ürün kısıtı ya da detay kısıt verilerek "Kayıtları Getir" butonu tıklandığında ilişkili kayıtlar ekranın altında bulunan grid alana listelenecektir. Bu alandaki listenin seçim sütunundaki kutucuklar çift tıklanarak seçilebilir ve "Değişiklikleri Kaydet" butonu tıklanarak istenen eşleştirmeler kaydedilmiş olur. (Bkz. Ekran Görüntüsü 13)

![](../../_assets/35631bbf1e440949ac11.png)

Bu ekranda yapılacak eşleştirmeler sonraki adımlarda kolaylık sağlayacaktır. Bu sebeple üretim aşamaları aynı ya da benzer olan ürünleri gruplayarak sonrasında her ürün için tek tek işlem yapmaktansa gruplara işlem yapmak süreci hızlandıracaktır. Daha önce halihazırda yapılmış eşleştirmeler varsa ve yalnızca eşleştirmesi yapılmayan ürünler görüntülenmek istenirse "Henüz eşlenmeyen stoklar getirilsin" parametresi seçilebilir. Benzer şekilde ekranda desteklenenden daha farklı kısıtlar uygulanmak istenirse de "Listeye ileri kısıt uygulansın" parametresi kullanılabilir.

#### Makine Tanımlama

Bu adımlar sonrasında makine tanımlamaları yapılmalıdır. Bunun için Üretim-MRP-Kayıt-İleri Üretim Çizelgeleme-Makine Tanımlama yolu izlenmelidir. Makine tanımlama ekranı 2 sekmeden oluşmaktadır. (Bkz. Ekran Görüntüsü 14)

Programın "Üretim Akış Kontrol-Makine Tanımlama" ya da "MRP-Kayıt-Makine Tanımlama" yollarından makine tanımlamaları yapıldıysa da bu ekrana akmayacaktır. İleri üretim çizelgelemede kullanılacak tüm makine tanımlamaları bu ekran üzerinden yapılmalı ve güncellenmelidir.

Ekrandaki "Makine Kodu" ve "Makine İsmi" alanları serbestçe belirlenebilir. Bu ekranın aynı zamanda demirbaş modülü ile entegrasyonu bulunmaktadır. Bağlantı bilgileri tanımlı ve demirbaş paketi kullanımdaysa makine kodu rehberinden makine seçimi yapılabilir. Aksi halde ekran üzerinden yeni makine tanımlaması yapılmalıdır.

![](../../_assets/795d73476c602bbdf8dc.png)**Ekran** **Görüntüsü** **14**

Makineler gruplanmak istenirse ya da var olan bir gruba yeni tanımlanan bir makine eklenmek istenirse "Grup Kodu" alanı kullanılmalıdır. "İstasyon Kodu" alanı ise zorunludur. Makinenin bulunduğu istasyon kodunun mutlaka girilmesi gereklidir. "Alış Tarihi" ve "Birim Maliyet" alanları ileri üretim planlama içinde kullanılmamaktır, demirbaşı ilgilendiren alanlardır. "Öncelik Sırası" ise aynı işi yapan makinelerden hangisinin daha öncelikli kullanılacağını belirtmek için doldurulması gereken bir alandır. Bu alan doluysa çizelgelemede dikkate alınacaktır. Yine ekranda bulunan "Aktif-Pasif" alanları çizelgeleme açısından önemlidir. Pasife çekilmiş makineler çizelgelemede kullanılmayacaktır. "Açıklama" alanı ise gerek duyulduğu takdirde serbestçe kullanılabilir.

Ekranın üretim bilgileri bölümündeki "Makine Tipi" alanının doldurulması zorunlu ve doğru seçimin yapılması çizelgeleme sonuçları için önemlidir.

Makine Tipi alanında ayrıntıları aşağıda belirtilen 9 seçenek vardır:

- Normal (Single Processor) tipli makineler aynı anda yalnızca 1 ürün işleyebilir.
- Normal (Multi Processor) tipli makineler aynı anda birden fazla ürün işleyebilir. Ancak işlediği tüm ürünler aynıdır. Bu makine tipi seçildiğinde "İşlemci Sayısı" alanı oluşacaktır. Makine aynı anda kaç ürün işleyebiliyorsa buraya o sayı yazılmalıdır.
- Fason tipli seçim, dışarıda işlemeye gönderilen ürünler için kullanılmalıdır. Bu tip seçildiğinde "Cari Kodu" ve "Kapasite" alanlarıyla birlikte "Fason Lojistik Planı" sekmesi oluşacaktır. (Bkz. Ekran Görüntüsü 15) Hangi cari kodlu fason üreticisine ürün gönderiliyorsa o cari kodu ilgili alana girilmelidir. Eğer fason üretici tarafından günlük maksimum kaç birim üretim yapılabileceği bilgisi verildiyse "Kapasite" alanına bu veri girilerek çizelgelemenin bu bilgiyi hesaplamaya dahil etmesi sağlanabilir. Bahsi geçen kapasitenin ürün bazında tanımlanması da mümkündür. Bunun için operasyon-makine eşleştirme ekranı kullanılmalıdır. Bu konuda daha detaylı bilgi için "10.1 Operasyon-Makine Eşleştirme" bölümü okunabilir.

Fason lojistik planı ekranında ise fason üreticiye ait ürün gönderme ve teslim alış günleri ile saatleri tanımlanabilir. Gidiş bilgileri alanında birden fazla gün seçimi yapılabilir. Teslim etme tarihleri ise haftanın belli bir günü değil, işletme tarafından verilen günden itibaren 2 gün sonra ya da aynı gün gibi bir değerse, dönüş bilgileri alanının en altındaki seçenek tıklanarak açılan menüden uygun seçim yapılmalıdır. Fason tipli makinelerin üretim süresi, yalnızca kapasite tanımı yapılmadığında dikkate alınır ve kapasite tanımlı değilse makinenin sonsuz kapasite ile çalıştığı varsayılmaktadır. Bu durumlarda fason lojistik planına göre en yakın gidiş tarihi bulunur ve üretim süresine göre dönüş tarihi hesaplanır, yani girilmiş olan dönüş tarihi bilgisi dikkate alınmaz. Kapasite bilgisi tanımlanmış ise, bu kapasitenin 24 saatlik olduğu varsayılacak ve buna göre birim ürün için üretim süresi hesaplanacaktır. Ardından üretim başlangıç tarihi olarak lojistik planındaki en yakın gidiş tarihi seçilecek ve hesaplanan üretim süresine göre üretimin ne zaman tamamlanacağı bulunacaktır. Üretim bitiş tarihinden sonraki en yakın dönüş tarihi bilgisi kullanılarak ise planlama yapılacaktır.

![](../../_assets/481172813f96290da182.png)![](../../_assets/1135e72af67977111dbe.png)**Ekran** **Görüntüsü** **15**

- Fırın tipli makinelerde kapasite önemlidir. Boş kapasitesi olduğu sürece yeni ürün alabilir. Bu yönüyle gerçek ekmek fırınları gibi düşünülebilir ve yine bu özelliğiyle kazan tipli makinelerden ayrılmaktadır. Farklı ürünleri aynı anda işleme özelliği vardır. Her ürün fırında kendi proses süresi kadar işlenecektir. Ayrıca bu makine tipinde "İşe Başlayabilmek için Min. Kapasite Doluluk Oranı" alanı bulunmaktadır. 1 değeri %100 anlamına gelmektedir. Buraya girilen oran makinenin çalışmaya başlaması için, önünde kapasitesinin en az yüzde kaçı kadar iş birikmesini bekleyeceğini ifade eder. Örneğin bu değere 0,8 girilirse ve fırının kapasitesi 100 birimse, fırına girmeye hazır en az 80 birim ürün birikmeden fırın çalışmaya başlamayacaktır.
- Sürekli Fırın tipli makinelerde fırın içinde bir akış vardır. Ürünler fırına girip içinde ilerlerler ve fırından çıktıklarında işlenmeleri tamamlanmış olur. Bu makine tipi seçildiğinde "Çevrim Süresi" alanı oluşacaktır. Burada kavramların karıştırılmaması önemlidir. Örneğin; sürekli fırın tipli makine henüz boşken, giren ilk ürünün çıkana kadar makine içinde geçirdiği süre üretim süresine eşittir. İlk ürün çıktıktan sonra ise makine dolmuş olacağından, hemen arkasından seri olarak sıradaki ürünler çıkmaya devam edecektir. Dolayısıyla makineye giren ilk ürün makineden çıkana kadar geçen zamanla, makine dolduktan sonra bir ürün makineden çıkana kadar geçecek zamanlar eşit değildir. İşte bu ilk üründen sonra çıkan ürünler için, çevrim süresi kullanılması anlamlıdır. Örneğin; sürekli fırından her 30 saniyede, 1 adet ürün çıkıyorsa, bu makine için çevrim süresi 30 saniyedir.

- Montaj Hattı tipli makine mantık olarak sürekli fırın ile birebir aynıdır. Yine çevrim süresinin tanımlanabileceği alan burada da yer almaktadır. Bu tip makinelerde farklı olan nokta ise "Montaj Hattı Dengeleme" desteği bulunmasıdır. Montaj hattı dengeleme ekranına Üretim-MRP-Kayıt-İleri Üretim Çizelgeleme yolundan ulaşmak mümkündür.
- Manuel Montaj tipli makinelerde aynı anda farklı sayılarda kaynağın (operatör gibi) çalışması mümkündür. Bu sebeple bu tip makineler seçildiğinde "Min. Çalışabilecek Kaynak Seti Sayısı" ve "Maks. Çalışabilecek Kaynak Seti Sayısı" alanları oluşmaktadır. Buraya bu tipteki makinede çalışabilecek en az ve en fazla kaynak sayısı tanımlanmalıdır. Algoritma optimum seviyede kaynak kullanacak şekilde çizelgeleme yapacaktır. Bu tipteki makinelerde aynı anda farklı ürünlerin işlenebilmesi de mümkündür. Buna göre gerekli kaynak ataması algoritma tarafından yapılacaktır. Bu tip makinelere örnek olarak bir montaj masası etrafında operatörler tarafından paketleme operasyonu yapılması verilebilir. Bu operasyonu yapabilecek maksimum ve minimum operatör sayıları da kaynak seti sayıları olacaktır.
- Kazan tipli makinelerde de kapasite önemlidir. Kapasite tamamen dolmamış olsa dahi makine çalışmaya başladığında proses sonlanana kadar yeni ürün alamaz. Farklı ürünleri aynı anda işleme özelliği vardır fakat bu özelliğin kullanılabilmesi için "Farklı Ürünler Aynı Anda İşlem Görebilsin" parametresi seçili olmalıdır. Bu parametre açıldığında "Gruplama Seçeneği" listesi de aktifleşecektir. Bu listeden Üretim Süresi, Grup Kodu, Kod-1, Kod-2, Kod-3, Kod-4, Kod-5 ya da Ürün Grubu seçimi yapılabilir. (Bkz. Ekran Görüntüsü 16) Bu noktada kurgunun iyi yapılması önemlidir. Örneğin farklı üretim sürelerine sahip ürünlerden bir grup oluşturulduysa ve gruplama seçeneği listesinden bu grup seçildiyse, gruptaki tüm ürünler maksimum süreye sahip ürüne göre işlem görecektir. Ayrıca bu makine tipinde de "İşe Başlayabilmek için Min. Kapasite Doluluk Oranı" alanı bulunmaktadır. 1 değeri %100 anlamına gelmektedir. Buraya girilen oran makinenin çalışmaya başlaması için, önünde kapasitesinin en az yüzde kaçı kadar iş birikmesini bekleyeceğini ifade eder.

![](../../_assets/0afd6ec404e673dc9962.png)**Ekran** **Görüntüsü** **16**

- Robot tipli makineler farklı ürünleri eş zamanlı işleyebilme özelliğine sahip makinelerdir. Bu sebeple robot tipli bir makine tanımlandığında, "Eş Zamanlı İş Setleri Tanımlama" isimli yeni bir sekme oluşacaktır. Bu sekme üzerinden makinenin eş zamanlı işleyebileceği ürünler kaydedilebilir. (Bkz. Ekran Görüntüsü 17) Robot tipli bir makine tanımlandığında makinenin eş zamanlı işleyebileceği tüm set alternatiflerinin de tanımlanmış olması kritiktir. Eğer mevcut iş emirlerinden robot tipli makineye tanımlanmamış bir set alternatifi oluşursa bu iş emirleri robot tipli makineye planlanmayacaktır. Örneğin robot tipli bir makinenin aynı anda A, B ve C tipli ürünleri işleyebildiği varsayılsın. Bu aslında ilgili robotun A-B, A-C, B-C ve A-B-C ürünlerini eş zamanlı üretebileceği veya yalnızca A, B veya C ürününü üretebileceği anlamına gelecektir. Bu alternatiflerin bir veya birkaçının set olarak tanımlanmaması durumunda, iş emirlerinden tanımlanmamış bir kombinasyon oluştuğunda makineye atanamayacaktır.

Eş zamanlı iş setleri tanımlama sekmesindeki "Gruplama Seçeneği" alanından hangi tipte ürün tanımlaması yapılacağı seçilmelidir. Ürün kodu, grup kodu, Kod 1-2-3-4-5 ya da ürün grubu bazında giriş yapmak mümkündür. 17. ekran görüntüsünde kırımızı kutucuk içinde gösterilmiş aktif parametresi kullanılarak mevcut bir set aktif ya da pasife çekilebilir. Set numaraları sistem tarafından sırasıyla otomatik verilecektir. Gruplama seçeneği alanı doldurulduktan sonra "Ürün Detayları" alanındaki rehber kullanılarak oluşturulan sete eklenmek istenen ürünler seçilmelidir. "Üretim Miktarı" alanından ise ilgili ürünün, ilgili sette kaç adet üretilebileceği girilmelidir. Ekrandaki üst gridde o an oluşturulmakta olan setin içine eklenen ürünler görülecektir. Ekran görüntüsünde mor kutucuk içinde gösterilmiş olan "Kaydedilen Setler" alanının solundaki artı ve eksi butonlarıyla kaydedilen setler alanının açılıp kapanması mümkündür. Kaydedilen setler alanı açıldığında oluşan alt gridde ise kaydedilmiş setler görülebilir. Ekranın sol altında mor kutucuk içinde gösterilmiş "Yeni Set Ekle" butonuna basıldığında mevcut set kaydolarak alt gride geçecek ve ekran yeni bir set oluşturmaya hazır hale gelecektir. Yine bu butonlar yardımıyla mevcut bir seti silmek ya da kopyalamak da mümkündür.

![](../../_assets/44208a58505787212893.png)**Ekran** **Görüntüsü** **17**

Üretim bilgileri bölümünde bulunan "Verimlilik Katsayısı" alnına 1 değeri verilmesi makinenin %100 verimlilikle çalıştığı anlamına gelmektedir. Buraya girilen verimlilik değerine göre makine için tanımlanmış olan üretim süresi ters orantılı şekilde artacaktır. Yine bu bölümdeki "Parti Büyüklüğü" alanı ise bilgi amaçlı kullanılmaktadır.

Yine üretim bilgileri bölümünde yer alan "Üretim Süresi" ve "Üretim Miktarı" alanları makine tipine bağlı olarak değişkenlik göstermekle birlikte, aynı anda bulunması halinde (single processor tipli makinede olduğu gibi) bir arada kullanılmalıdır. Birim sürede yapılan üretim miktarı bu iki alana girilmelidir. Örneğin 70 saniyede 8 metre ürün işlenebiliyorsa, üretim süresi 70 saniye seçilmeli ve üretim miktarına 8 metre girilmelidir.

Makine tanımlama ekranında da vardiya planı sekmesi bulunmaktadır. (Bkz. Ekran Görüntüsü 14) Bu sekme makine bazında vardiya planı oluşturmak için kullanılabilir ve önceki bölümlerde detayları anlatılmış olan vardiya planı oluşturma ekranlarıyla aynıdır. Burada seçilen bir makine için oluşturulacak vardiya planı hiyerarşik olarak fabrika çalışma takvimi ve iş istasyonu bazındaki vardiya planından daha özel bir tanımlama olacağından, makine bazındaki vardiya planı kullanılacaktır.

Genel anlamda farklı makine tipleri için üretim süresi bilgilerinin de ürün bazında tanımlanması mümkündür. Bunun için operasyon-makine eşleştirme ekranı kullanılmalıdır. Bu konuda daha detaylı bilgi için "10.1 Operasyon-Makine Eşleştirme" bölümü okunabilir.

#### Operasyon Tanımlama

İleri üretim çizelgeleme uygulamasının doğru çalışabilmesi için yapılması gereken bir diğer tanım da operasyon tanımlarıdır. Üretim-MRP-Kayıt-İleri Üretim Çizelgeleme yolu izlenerek "Operasyon Tanımlama" ekranına ulaşılabilir. (Bkz. Ekran Görüntüsü 18)

Bu ekranda "Operasyon Kodu" ve "Operasyon İsmi" alanları istenilen şekilde doldurulabilir. "İstasyon Kodu" alanı ise zorunlu bir alan değildir. Aynı operasyon birden fazla istasyonda yapılıyorsa bu alana giriş yapmak mantıklı olmayacaktır. Tanımlanan operasyon bir gruba da tanımlanması isteniyorsa "Grup Kodu" alanı kullanılabilir. "Operasyon Açıklama" alanı ise gerekmesi halinde serbestçe kullanılabilmektedir.

Üretim bilgileri bölümünde ise "Üretim Süresi" ve "Üretim Miktarı" alanları bulunmaktadır. Bu alanlar bir arada kullanılarak anlamlı bir veri oluştururlar. Birim sürede yapılan üretim miktarı bahsedilen alanlara girilmelidir. Örneğin bir operasyonda 70 saniyede 8 metre ürün işlenebiliyorsa, üretim süresi 70 saniye seçilmeli ve üretim miktarına 8 metre girilmelidir. Burada belirtilmesi gereken önemli bir ayrıntı şudur ki; eğer bir operasyondaki üretim süresi ve miktarı o operasyon için tek ve sabit değilse, ürün ya da kaynak bazında farklılık gösteriyorsa, ileride detaylandırılacak olan eşleştirme ekranları üzerinde bu tanımlamalar yapılabilmektedir.

Ekranda ayrıca "Geçiş Süresi" alanı bulunmaktadır. Tanımlanmakta olan operasyon tamamlandıktan sonra, sıradaki operasyona geçilene kadar ürünlerin belli bir süre beklemesi gerekiyorsa bu süre bu alanda tanımlanmalıdır. Burada önemli olan geçiş süresi içinde herhangi bir kaynak kullanımı olup olmadığıdır. Eğer kaynak kullanımı olacaksa (bekleme alanının kısıtlı kapasitesi olması gibi) bu beklemeyi de farklı bir operasyon gibi tanımlayıp kısıtları tanımlamak gerekecektir.

![](../../_assets/ba159eb51d066723500a.png)**Ekran** **Görüntüsü** **18**

Operasyon tanımlama ekranında bulunan "Geçiş Miktarı" alanında 2 seçenek bulunmaktadır. Geçiş miktarı elle girilebilir ya da "Otomatik Hesaplansın" parametresi açılabilir. Buraya girilecek değer, tanımlanmakta olan operasyon tamamlandıktan sonra, ürünlerin sıradaki operasyona kaç birimlik yığınlar halinde geçeceğini belirlemektedir. Bu alanda geçiş miktarının hiç tanımlanmamış olması durumda ise, ilgili iş emrinin tamamının bitmesi beklenecek şekilde çizelgeleme yapılacaktır.

Yine bu ekrandaki "Parti Büyüklüğü" alanı ise şimdilik algoritmada desteklenmemektedir.

#### Kaynak Tanımlama

Bir diğer aşama olan kaynak tanımlama işlemini yapabilmek için Üretim-MRP-Kayıt-Kaynak Yönetimi-Kaynak Tanımlama yolu izlenmelidir. Bu ekran üzerinde 4 sekme bulunmaktadır. (Bkz. Ekran Görüntüsü 19) Kaynak bilgileri sekmesinde bulunan "Kaynak Tipi" alanından 3 farklı seçim yapılabilir. "Demirbaş" seçimi yapıldıktan sonra gerekli tanımlamalar manuel yapılabileceği gibi eğer demirbaş paketi kullanılıyorsa ve gerekli bağlantı tanımlamaları yapılmışsa paket üzerindeki tanımlamalar otomatik olarak gelecektir.

Doğrudan bu ekran üzerinde yeni tanımlama yaparken "Kaynak Kodu" ve "Kaynak İsmi" alanları serbestçe doldurulabilir. İlgili kaynak var olan bir gruba dahil edilmek istenirse ya da yeni bir grup yaratılmak istenirse "Kaynak Grup Kodu" alanı kullanılabilir. "İstasyon Kodu" alanı zorunlu bir alan olmamakla birlikte, tanımlanan kaynak yalnızca bir istasyonda kullanılacaksa bu alan doldurulabilir.

![](../../_assets/6bd994934705f9934bf9.png)**Ekran** **Görüntüsü** **19**

Ekran üzerinde bulunan "Birim Maliyet" alanı çizelgelemede kullanılmamaktadır. Demirbaş paketinde tanımı bulunması halinde bu ekrana da gelecektir. İlgili kaynağın kullanımda olup olmadığı bilgisi ise "Durum" alanındaki aktif-pasif seçiminden tanımlanmalıdır. "Toplam Miktar" alanına ise işletmede ilgili kaynaktan kaç adet bulunduğu girilmelidir. Bu ekrandaki "Öncelik Sırası" bilgi amaçlı kullanılmaktadır. Kaynak kullanımıyla ilgili bir öncelik belirlemesi yapılmak istendiğinde operasyon-kaynak eşleştirme veya makine-kaynak eşleştirme ekranlarındaki "Set Öncelik Sırası" alanları kullanılmalıdır. Bu ekranlarla ilgili detaylı bilgi edinmek için 10.3 ve 10.4 bölümleri okunabilir. Bu ekrandaki "Açıklama" alanı ise yine istenmesi halinde serbestçe kullanılabilir.

Aynı ekran üzerinde "Ömür Takibi Yapılsın" parametresi açılırsa programın sağlıklı çalışabilmesi "Ömür Takibi" sekmesindeki bilgilerin de doldurulması gerekmektedir. (Bkz. Ekran Görüntüsü 20) Bu ekranda bulunan "Son Kullanma Tarihi" ilgili kaynağın teknik talimatlarında (spesifikasyon) bulunan son kullanım tarihidir. Kaynak, ömrü dolmamış olsa bile bu tarihten sonra kullanılmayacaktır.

![](../../_assets/cd38de0d6b4fed3918f9.png)**Ekran** **Görüntüsü** **20**

Ekrandaki "Toplam Ömür" bilgisi ise kaynağın niteliğine uygun olarak girilmelidir. Buradaki birim serbestçe tanımlanabilir ya da daha önce tanımlanmış birimlerden seçim yapmak için alanın yanındaki ok kullanılabilir. "Kalıp Göz Sayısı" alanı aynı anda birden çok ürün işleyen kaynaklar için kullanılmaktadır. Örneğin 3 gözlü bir kalıp kaynak olarak tanımlanırsa ve 3 gözden birden ürün çıkarıyorsa bu alana 3 girilmelidir. Bu alanın doldurulması çizelgeleme için değil ömür takibi için gereklidir.

Ekrandaki "Tamir Edilebilir" parametresi açıldığında ise "Ort. Bakım Süresi", "Maksimum Bakım Sayısı" ve "Bakımda Yıpranma Payı" alanları aktifleşecektir. Tamiri mümkün olan kaynaklar için bu alanların tanımlanması ömür takibinin gerçeğe uygun şekilde yapılmasını sağlayacaktır. Örneğin ortalama bakım süresi 10 gün olarak girilen bir kaynak, toplam ömrü dolduğunda 10 gün boyunca çizelgelemede kullanım dışı tutulacaktır. Ayrıca bu kaynağa bakımdaki yıpranma payı girilmişse, tamirden döndükten toplam ömür alanı bu yıpranma payı kadar azalacaktır. Ömür takibi yapılan kaynaklar için çizelgeleme çalıştırıldıktan sonra kaynak bakım planı raporu alınabilir. Bu raporla ilgili detaylara 14. bölümden ulaşılabilir.

Kaynak tanımlama ekranı üzerinde kaynak tipinin "Stok" olarak seçildiği durumlarda ise kaynak kodu alanında seçim yapabilmek için öncesinde stok kartı tanımlanmış olmalıdır. Kaynak kodu rehberinden sistemde tanımlı olan stok kartları görüntülenebilmektedir. Buradan istenen seçim yapıldığında, stok kartından okunan kaynak ismi, grup kodu ve toplam miktar değerleri program tarafından ilgili alanlara otomatik olarak getirilecektir. Bu alanlara kaynak tanımlama ekranı üzerinden müdahale etmek mümkün değildir. Ek olarak stok tipli kaynak için ömür takibi de yine stok kartı üzerinden yapılmakta, tanımlanan toplam ömür verisine göre stok bakiyesi güncellenmektedir.

Kaynak tanımlama ekranı üzerinde seçim yapılabilecek son kaynak tipi "Personel'dir". Personel seçimi yapıldıktan sonra gerekli tanımlamalar manuel yapılabileceği gibi eğer personel paketi kullanılıyorsa ve gerekli bağlantı tanımlamaları yapılmışsa paket üzerindeki tanımlamalar otomatik olarak gelecektir. Personel tipli kaynak için doğrudan kaynak tanımlama ekranı üzerinde yeni tanımlama yaparken "Sicil Numarası" ve "Personel İsmi" alanları serbestçe doldurulabilir. İlgili kaynak var olan bir gruba dahil edilmek istenirse ya da yeni bir grup yaratılmak istenirse "Kaynak Grup Kodu" alanı kullanılabilir. "İstasyon Kodu" alanı zorunlu bir alan olmamakla birlikte, tanımlanan kaynak yalnızca bir istasyonda kullanılacaksa bu alan doldurulabilir.

Personel tipli kaynakta "Toplam Miktar" alanının kullanımı daha farklıdır. Eğer her sicil numarası için ilgili personelin adı-soyadı şeklinde tanımlama yapılmışsa bu alanı kullanmak anlamlı olmayacaktır. Ancak bir operasyon için, örneğin paketleme, paketleme personeli olarak tek bir kaynak tanımlanırsa, bu operasyonda çalışacak toplam personel sayısı bu alana girilebilir. Ayrıca personel tipli kaynak için ömür tanımlaması da desteklenmemektedir. Personel seçimi yapıldığında "Ömür Takibi Yapılsın" parametresi pasif olarak gelecektir.

Kaynak tanımlama ekranı üzerinde her 3 tipteki kaynak için de aktif olan "Vardiya Planı" sekmesi mevcuttur. Herhangi bir kaynak için buraya bir tanımlama yapıldığında, hiyerarşik olarak şimdiye kadar anlatılan tanımlamalardan daha özel bir tanımlama yapılmış olacağı için buradaki tanımlama baz alınarak çizelgeleme yapılacaktır.

Kaynak tanımlama ekranı üzerinde bulunan son sekme ise "Ürün Eşleştirme" sekmesidir. (Bkz. Ekran Görüntüsü 21) Bir kaynağın aynı anda birden fazla ürün işlemesi söz konusuysa bu sekme kullanılmalıdır. Örneğin kalıp göz sayısı tanımlaması yapılmış bir kaynak için bu sekmede aynı anda hangi ürünlerin ilgili kalıptan çıkabileceğinin tanımlaması yapılabilir. Bu ürünler kalıptan aynı anda çıkıyorsa "Eşleşen tüm ürünlerin eş zamanlı çıkma zorunluluğu var" seçeneği işaretlenmelidir. Bu

sekme üzerinde "set" mantığı vardır. Bir kalıp birden fazla şekilde kullanılabiliyorsa, bu ihtimaller ayrı setler olarak tanımlanmalıdır. Örneğin 3 gözlü bir kalıp 2 adet A ürünü ve 1 adet B ürünü çıkarabildiği gibi, 3 adet C ürünü de çıkarabiliyor olsun. Bu durumda bu 2 farklı senaryo bu kalıp özelinde 2 farklı set olarak tanımlanmalıdır. Bu tanımlamalar kaydedilen setler grid'inde görülebilecektir. Bu setlerden hangisine öncelik verileceği ise "Set Öncelik Sırası" alanından tanımlanabilir.

![](../../_assets/b6c14484b8883c1ba993.png)**Ekran** **Görüntüsü** **21**

Ekranın sol alt köşesindeki artı butonuyla kaydedilen setler ayrı bir gridde görüntülenebilmektedir. (Bkz. Ekran Görüntüsü 21) Set olarak kaydedilmek istenen ürünler ya da ürün gruplarından uygun seçim yapıldıktan sonra "Ürün Değer" alanındaki rehberden ilgili kaynakla üretilebilen ürünler tek tek seçilmeli ve her bir ürün için bu kaynaktan tek seferde bu üründen kaç birim çıktığı bilgisi "Tek seferde çıkan ürün miktarı" alanına girilmelidir. Bu girişler yapıldıkça ekranın altındaki grid alanda görüntülenecektir. İlgili kaynak için bir başka set tanımlanmak istenirse "Yeni Set Ekle" butonu kullanılmalıdır. Benzer şekilde mevcut setleri silmek ya da kopyalamak da mümkündür.

#### Hazırlık Süresi Tanımlama

İleri üretim çizelgeleme için yapılması gereken bir diğer kayıt da hazırlık süresi tanımlarıdır. Üretim-MRP-Kayıt-İleri Üretim Çizelgeleme yolu takip edilerek "Hazırlık Süresi Tanımlama" ekranına ulaşılabilir. (Bkz. Ekran Görüntüsü 22) Bu ekran üzerinde 5 farklı tipte hazırlık tanımlaması yapılabilmektedir. Hazırlık Süresi Tanımlama ekranında öncelikle neye ait hazırlık süresi tanımlanacağına karar verilmeli ve "Operasyon" alanından uygun seçim yapılmalıdır. Bu alanda "Tümü" haricinde bir seçim yapılırsa, "Operasyon Değer" alanından da tanımlama yapılmak istenen operasyon ya da operasyon grubu seçilmelidir. Ardından "Hazırlık Süresi Tipi" alanından uygun seçim yapılmalıdır. Operasyonun kendisine ait bir hazırlık süresi tanımlanacaksa "Kendisine Ait Hazırlık Süresi" seçilmelidir. Eğer bir üründen diğerine geçilirken bir hazırlık söz konusuysa "Ürün Değişimi" seçilmelidir. Ürün değişimi seçildiği takdirde sayfada yeni alanlar açılacaktır. (Bkz. Ekran Görüntüsü 23) Bu alanlara hangi üründen (mevcut ürün seçimi) hangi ürüne (sonraki ürün seçimi) geçiş için hazırlık süresi tanımlaması yapılacağı girilmelidir. Ürün grubu, ürün kodu ya da tümü seçeneklerinden uygun olanlar seçilip ürün kodu ya da ürün grubu seçildiyse ayrıca "Ürün Değer" alanı da doldurulmalıdır.

![](../../_assets/1d9092d51ed1ac908073.png)**Ekran** **Görüntüsü** **22**

Benzer şekilde "Kaynak Değişimi" tipli hazırlık süresi seçildiğinde de yeni alanlar açılacaktır. Burada da aynı şekilde hangi kaynaktan (mevcut kaynak seçimi) hangi kaynağa (sonraki kaynak seçimi) geçiş için hazırlık süresi tanımlaması yapılacağı girilmelidir. Kaynak kodu ya da kaynak grubu için giriş yapılacaksa "Kaynak Değer" alanı da doldurulmalıdır.

![](../../_assets/ac3210657476b8b57e54.png)**Ekran** **Görüntüsü** **23**

"Operasyon Değişimi" tipli hazırlık süresi seçildiğinde ise yalnızca "Önceki Operasyon Seçimi" alanı açılacaktır. Bu alanda da operasyon kodu ya da operasyon grubu bazında seçim yapılabilir veya tümü seçilebilir. Önceki operasyon seçimi alanında ne tanımlandıysa, bu tanımdan, halihazırda operasyon alanında tanımlanmış olan değere geçişte, girilen hazırlık süresi kullanılacaktır. Son hazırlık tipi süresi ise "Script"tir. Bu tip seçildiğinde oluşan alana istenilen bir script kodu yazılabilir.

Hazırlık süresi, seçilen hazırlık süresi tipi için makine bazında da değişkenlik gösteriyorsa ayrıca "Makine Bilgileri" alanına da tanımlama yapılmalıdır. Örneğin ürün değişimi tipli bir hazırlık süresi, A ürününden B ürününe geçiş için tanımlanmış olsun. Fakat bu geçiş, üretim Makine1'de yapıldığında 20 dakika, Makine2'de yapıldığında 30 dakika sürüyor olsun. Böyle bir durumda A'dan B'ye hazırlık süresi tanımlanırken makine bilgileri alanı da kullanılmalı ve her 2 makine için ayrı ayrı hazırlık süresi tanımlanmalıdır.

Ekran üzerinde bulunan "Hazırlık Süresi İşe Bağlı Değil" parametresi; hazırlık süresinin başlaması için, bir önceki operasyonun tamamlanıp yarı mamullerin tanımlanmakta olan operasyona gelmesinin beklenmek zorunda olmadığı durumlarda kullanılmalıdır.

Aynı yerde bulunan "Kendisi Dahil" parametresi ise Tümü'nden Tümü'ne seçimli geçişler için anlamlıdır. Böyle bir seçim yapıldığını ve bu parametrenin de açıldığı düşünelim. Bu durumda geçiş A ürününden A ürününe olsa bile tanımlanan hazırlık süresi kullanılacaktır. Parametrenin açık olmadığı durumda ise A ürününden A ürününe geçişte hazırlık süresi olmadığı varsayılacaktır.

Ekranın en sonunda bulunan "Hazırlık Süresi" alanı ise hazırlığın ne kadar sürdüğünü kaydetmek için kullanılmalıdır.

#### Rota Tanımlama

Çizelgelemenin doğru çalışabilmesi için en kritik tanımlamalardan biri de rota tanımlarıdır. İlgili ekrana ulaşabilmek için Üretim-MRP-Kayıt-İleri Üretim Çizelgeleme yolu izlenmelidir. Rota tanımlama, işletmede reçete sisteminin nasıl kurulduğuyla doğrudan ilişkilidir. Tüm operasyonların sonunda bir yarı mamul oluştuğu varsayımıyla her yarı mamul için bir stok tanımlamasının bulunduğu bir üretim ile, birkaç operasyonun arka arkaya yapılması sonucu bir yarı mamul oluştuğu varsayımıyla stok tanımlamasının yapıldığı bir üretimin rota tanımlama mantıkları da farklı olacaktır. Bu konuda doğru ya da yanlış yoktur. İşletmenin operasyon sayısı, ürün çeşitliliği, yarı mamul stok bakiyesinin takip edilme ihtiyacı gibi birçok parametreye bağlı olarak her işletmede farklı kurgular bulunması olasıdır.

Rota tanımlama ekranında normalde 2 sekme bulunmaktadır. (Bkz. Ekran Görüntüsü 24) Ancak "Rota Eşleştirme" sekmesinin oluşabilmesi için tanımlanmış bir rota bulunması gereklidir. "Rota Tanımlama" sekmesinde bulunan "Rota Kodu" alanı ve "Açıklama" alanı serbestçe doldurulabilir. Bu alanda tanımlanan rotayı detaylandırmak için ekranın sol tarafında bulunan alan kullanılır. Ekran Görüntüsü 24'te kırmızı kutucuk içine alınmış artı ve eksi butonları kullanılarak, tanımlanan rotaya operasyonlar eklenip çıkarılabilir. Artı butonuna tıklandıktan sonra ekranın sağında bulunan "Sıra No" Ve "Operasyon Kodu" alanlara giriş yapılması gerekmektedir. Tanımlanmakta olan rota sonucunda oluşacak mamul/yarı mamul göz önünde bulundurularak bu mamul/yarı mamulün oluşması için tamamlanması gereken operasyon ya da operasyonlar, operasyon kodu rehberinden seçilerek kaydedilmelidir. Rehberden tanımlı bir operasyon seçimi yapıldığında operasyon adı, operasyon kodu, istasyon ismi, operasyon açıklama alanları önceden kaydedilen tanımlamalara göre otomatik olarak dolacaktır. Bu alanlara bu ekran üzerinden müdahale etmek mümkün değildir. İstenilen rota oluşturulduktan sonra "Rota Kaydet" butonuna tıklanarak kayıt işlemi yapılmalıdır.

![](../../_assets/e2f4576f723610babedf.png)**Ekran** **Görüntüsü** **24**

Rota tanımlama işlemi tamamlandıktan sonra rota eşleştirme sekmesine geçilmelidir. (Bkz. Ekran Görüntüsü 25)

![](../../_assets/1733c327ce3722a502d2.png)**Ekran** **Görüntüsü** **25**

Tanımlanan rotaya ait eşleştirme işlemleri bu sekmeden yapılmaktadır. İlgili rotaya ait "Rota Kodu" ve "Açıklama" alanları tanımlama ekranındaki bilgilere istinaden otomatik olarak dolmaktadır. Bu alanlar bu sekme üzerinden değiştirilemez.

Tanımlanan rotadaki operasyonlar sırasıyla tamamlandıktan sonra hangi yarı mamul ya da mamullerin oluşacağı dikkate alınarak eşleştirme yapılmalıdır. Oluşacak yarı mamul/mamullerin eşleştirmesi için ürün kodu, ürün grubu ya da tüm ürünler bazında seçim yapılarak "Ürün Değer" alanına giriş yapılmalıdır. Buradan seçim yaparken rehberden yararlanılabilir. Tab tuşu ile ilerleyerek ilgili seçimin ekranın altında bulunan grid'e kaydedilmesi sağlanabilir. Ayrıca ürün kodu bazında eşleştirme yapıldığı ve farklı mamul/yarı mamullerin aynı rotayı izleyerek üretildiği durumlar için, tüm mamul/yarı mamulleri tek tek eşleştirmek gereklidir. Ekranın altındaki grid alanında her satır bir başka eşleşmeyi temsil edecektir.

Bir ürün birden çok rotayla eşleştirilebilmektedir. Bu durumda ilk eşletirme "varsayılan" olacaktır. Eğer birden çok rotayla eşleştirilen bir ürün için farklı bir rota varsayılan olarak kaydedilmek istenirse, rota eşleştirme sekmesi üzerinden "Yeni Varsayılan Rota Yapılsın" seçeneği işaretlenebilir. Burada dikkat edilmesi gereken nokta, bir ürün için yalnızca bir aktif rota olabileceğidir. Çizelgeleme yalnızca varsayılan rotayı dikkate alarak çalışacaktır.

Herhangi bir rotaya bağlı olmayan ürünler ise çizelgelemeye dahil edilmeyecektir. Bu yüzden tüm ürünlerin rota tanımlamaları ve eşleştirmeleri yapılmış olmalıdır.

#### Eşleştirme Bilgileri

İleri üretim çizelgeleme uygulamasının en doğru şekilde çalışabilmesi için şimdiye kadar yapılan tanımlamalara ek olarak yapılması gereken eşleştirmeler bulunmaktadır. Bunlardan "Operasyon-Makine" ya da "Makine-Operasyon" eşleştirmelerinin eksiksiz olarak tanımlanması zorunludur. Öte yandan kaynak (kalıp, takım vb.) tanımları bulunan kullanıcıların daha doğru sonuç alabilmek için "Operasyon-Kaynak" veya "Makine-Kaynak" eşleştirmelerini de yapması gerekmektedir, ancak bu tanımlamalar zorunlu değildir. Operasyon-makine ya da makine-operasyon eşleştirmeleri eksik olan ya da hiç olmayan ürünler için çizelgeleme yapılmayacaktır. Daha önceki bölümlerde de bahsedildiği gibi şimdiye kadar yapılan tanımlamaların; operasyon, kaynak, makine bazında detaylandırıldığı ve özelleştirildiği adım eşleştirme adımıdır. Operasyon-Makine ve Makine-Operasyon eşleştirmeleri uygulama üzerinden yapılabilmektedir.

Operasyon-Kaynak Makine-Kaynak Eşleştirme ekranlarına ulaşmak için birkaç farklı yol vardır. Bunlardan ilki rota tanımlama ekranıdır. Ekran Görüntüsü 24'te mor kutucuk içinde görülen 3 butondan ilki "Makine ile Eşleştir", ikincisi ise "Kaynak ile Eşleştir" butonudur. Rotaya tanımlanan bir operasyon seçili haldeyken bu 3 buton da aktif olacaktır. Benzer şekilde, operasyon tanımlama ekranı grid'indeki kayıtlı operasyonlardan herhangi biri üzerine çift tıklanarak operasyon seçilir ve ardından sağ tıkla açılan menüden "Operasyonu yapabilecek makineleri belirle" ya da "Operasyonda kullanılacak kaynakları belirle" seçimi yapılırsa da eşleştirme ekranlarına ulaşılabilmektedir. Makine-operasyon eşleşmesi yapılabilmesi için ise makine tanımlama ekranı kullanılmalıdır. Makine tanımlama ekranı altındaki grid'de bulunan kayıtlardan birine çift tıklayarak seçim yapılabilir, ardından sağ tık ile açılan menüden "Makinede yapılabilecek operasyonları belirle" seçeneğine tıklanarak eşleştirme ekranına gidilebilir. Bu sağ tık menüsü altından makine-kaynak eşleştirme ekranlarına girmek de mümkündür. Ek olarak operasyon grubu veya makine

grubu tanımlama ekranlarından da aynı sığ tık menüsüne ulaşılabilir ve operasyon/makine grubu bazında eşleştirme yapılabilir.

#### Operasyon-Makine Eşleştirme

Operasyon-makine eşleştirme ekranı seçilen operasyon için açılacaktır. Bu sebeple "Operasyon Kodu" alanına bu ekranda müdahale etmek mümkün değildir. (Bkz. Ekran Görüntüsü 26)

![](../../_assets/07261ffb700b03f5326d.png) **Ekran** **Görüntüsü** **26**

Ekranın ürün seçimi bölümü; ürün kodu, ürün grubu ya da tümü bazında eşleştirme yapmaya imkan vermektedir. Bu alanda yapılacak seçim, yapılacak eşleştirmenin, seçili operasyona gelen hangi ürünler için geçerli olacağını ifade etmektedir. Bu alanda ürün kodu ya da ürün grubu seçilirse "Ürün Değer" alanı da eşleştirmenin hangi ürünler veya ürün grupları bazında geçerli olacağı bilgisine göre doldurulmalıdır.

Ekran üzerindeki "İstasyon Kod" alanı ise daha önce operasyon tanımlama ekranı üzerinden yapılmış tanımlamalara istinaden otomatik olarak dolmaktadır. İstenmesi halinde bu kısıt kaldırılarak makinelerin tam listesi görüntülenebilir. Kısıtı kaldırmak için alandaki istasyon kodu silinip Tab tuşu ile ilerlenebilir. İlgili operasyonun hangi makinelerde yapılacağı, listede bulunan seçim hanesindeki kutucuklar çift tıklanarak belirlenebilir.

Eğer seçim kutucuğu tıklanmış bir makine için "Operasyon Tanımlama" veya "Makine Tanımlama" ekranlarında üretim süresi ve üretim miktarı bilgileri tanımlanmamışsa, program bu alanlara odaklanacak ve bu alanlar doldurulmadan seçimin kaydolmasına izin vermeyecektir.

Ekranın alt bölümünde bulunan grid alanda şimdiye kadar bahsi geçen tanımlama ekranlarındaki alanlar sütunlar halinde bulunmaktadır ve bu alanlarda tanımlama yapmak mümkündür. Operasyon- makine eşleştirme ekranı ürün bazında tanımlama yapmaya imkan verdiği için ve bu, şimdiye kadarki tanımlamalardan daha özel bir tanımlama türü olduğu için, hiyerarşik olarak buraya bir tanımlama yapıldıktan sonra bu ekrandaki tanımlamalar geçerli olacaktır. Yani daha önce yapılmış tanımlamalar olsa bile program bu ekrandaki tanımlamaları baz alacaktır.

Aynı hiyerarşik yapı ürün seçimi alanı için de geçerlidir. Örneğin bir operasyon-makine eşleştirmesi hem "Tümü" için yapılmış hem de "Ürün Kodu" için yapılmışsa, ürün kodu daha özel bir tanımlama olacağı için, geçerli olan bu özel tanım olacaktır.

Uygulamada tanımlanmış makine grupları olması durumunda, bahsedilen tanımlamalar aynı şekilde makine grubu bazında da yapılabilir. Bunun için "Makine Grubu ile Eşleştir" sekmesi kullanılmalıdır. İstenen tüm tanımlamaların yapılmasından sonra ise "Değişikleri Kaydet" butonuna tıklanarak kayıt tamamlanmalıdır.

#### Makine-Operasyon Eşleştirme

Makine-operasyon eşleştirme ekranı seçilen makine için açılacaktır. Bu sebeple "Makine Kodu" alanına bu ekranda müdahale etmek mümkün değildir. (Bkz. Ekran Görüntüsü 27)

![](../../_assets/68fc108d5b8c900e7338.png)**Ekran** **Görüntüsü** **27**

Ekranın ürün seçimi bölümü; ürün kodu, ürün grubu ya da tümü bazında eşleştirme yapmaya imkan vermektedir. Bu alanda yapılacak seçim, yapılacak eşleştirmenin, seçili makinede hangi ürünler üretilirken geçerli olacağını ifade etmektedir. Bu alanda ürün kodu ya da ürün grubu seçilirse "Ürün Değer" alanı da eşleştirmenin hangi ürünler veya ürün grupları bazında geçerli olacağı bilgisine göre doldurulmalıdır.

Ekran üzerindeki "İstasyon Kod" alanı ise daha önce operasyon tanımlama ekranı üzerinden yapılmış tanımlamalara istinaden otomatik olarak dolmaktadır. İstenmesi halinde bu kısıt kaldırılarak operasyonların tam listesi görüntülenebilir. Kısıtı kaldırmak için alandaki istasyon kodu silinip Tab tuşu ile ilerlenebilir. İlgili makinenin hangi operasyonlarda kullanılacağı, listede bulunan seçim hanesindeki kutucuklar çift tıklanarak belirlenebilir.

Eğer seçim kutucuğu tıklanmış bir operasyon için "Operasyon Tanımlama" veya "Makine Tanımlama" ekranlarında üretim süresi ve üretim miktarı bilgileri tanımlanmamışsa, program bu alanlara odaklanacak ve bu alanlar doldurulmadan seçimin kaydolmasına izin vermeyecektir.

Ekranın alt bölümünde bulunan grid alanda şimdiye kadar bahsi geçen tanımlama ekranlarındaki alanlar sütunlar halinde bulunmaktadır ve bu alanlarda tanımlama yapmak mümkündür. Makine- operasyon eşleştirme ekranı ürün bazında tanımlama yapmaya imkan verdiği için ve bu, şimdiye kadarki tanımlamalardan daha özel bir tanımlama türü olduğu için, hiyerarşik olarak buraya bir

tanımlama yapıldıktan sonra bu ekrandaki tanımlamalar geçerli olacaktır. Yani daha önce yapılmış tanımlamalar olsa bile program bu ekrandaki tanımlamaları baz alacaktır.

Aynı hiyerarşik yapı ürün seçimi alanı için de geçerlidir. Örneğin bir makine-operasyon eşleştirmesi hem "Tümü" için yapılmış hem de "Ürün Kodu" için yapılmışsa, ürün kodu daha özel bir tanımlama olacağı için, geçerli olan bu özel tanım olacaktır.

Uygulamada tanımlanmış operasyon grupları olması durumunda, bahsedilen tanımlamalar aynı şekilde operasyon grubu bazında da yapılabilir. Bunun için "Operasyon Grubu ile Eşleştir" sekmesi kullanılmalıdır. İstenen tüm tanımlamaların yapılmasından sonra ise "Değişikleri Kaydet" butonuna tıklanarak kayıt tamamlanmalıdır.

#### Operasyon-Kaynak Eşleştirme

Tanımlanmış kaynaklar için ürün bazında eşleştirmeler yapılmak istendiğinde operasyon-kaynak eşleştirme ekranı kullanılmalıdır. Bu ekrana önceki bölümde bahsedilen sağ tık menülerinden ulaşılabileceği gibi Üretim-MRP-Kayıt-Kaynak Yönetimi-Operasyon-Kaynak Eşleştirme yolu izlenerek de ulaşılabilir. (Bkz. Ekran Görüntüsü 28)

![](../../_assets/25298083d4cf16363890.png)**Ekran** **Görüntüsü** **28**

Bu ekranda, hangi operasyon sırasında hangi ürün için hangi kaynağın kullanılacağı tanımlanacaktır. Bunun için öncelikle "Operasyon Seçimi" alanından operasyon kodu, operasyon grubu ya da tümü için seçim yapılmalıdır. Operasyon-makine eşleştirme ekranında bahsedilen hiyerarşi bu ekranda da geçerlidir. Operasyon seçimi tümü olarak yapılıp ayrıca tekil operasyonlar için operasyon kodu/grubu bazında da eşleştirmeler yapılabilir. Bu durumda yine en özel tanımlama geçerli olacaktır.

İkinci olarak ekran üzerindeki "Ürün Seçimi" alanından aynı mantıkla seçim yapılmalıdır. Son olarak ise kaynak tanımlama ekranındaki gibi set yapısı kullanılarak eşleştirmeler yapılmalıdır. Bunun için "Set Bilgileri" bölümü kullanılmaktadır. "Set Öncelik Sırası" alanı istenildiği şekilde doldurulabilir. Buraya müdahale edilmezse her yeni set için set önceliği ardışık olarak ilerleyecektir. Seçilen operasyon ve

ürün bazında hangi kaynak ya da kaynakların kullanılacağının tanımlanması için kaynak kodu, kaynak grubu veya tümü seçimlerinin yapılması mümkündür. Ekranın altında bulunan "Yeni Set Ekle" butonuna basılmadığı sürece yapılan her ekleme aynı set içine yeni bir satır olarak yapılacaktır. Kaydedilen setler ise ekranın en altında bulunan grid üzerinden takip edilebilir. Burada her satır farklı bir sete karşılık gelmektedir. Set mantığı ile ilgili ek açıklamalar için 7. bölüme bakılabilir.

Eşleştirilen kaynaklardan yalnızca hazırlık süresi boyunca kullanılacak bir kaynak varsa, "Kaynak Kullanımı Sadece Hazırlık Aşamasında Yapılsın" parametresi açılmalıdır. Ömür takibi parametresi açılmış kaynaklar için "Ömür Tüketimi" girişi de bu ekran üzerinden yapılabilmektedir. Seçilen operasyonlar ve ürünler için ilgili kaynaktan kaç adet kullanılacağı bilgisi ise "Kaynak Sayısı" alanına girilmelidir.

#### Makine-Kaynak Eşleştirme

Tanımlanmış makineler için ürün bazında hangi kaynakların kullanılacağının tanımlanabileceği ekran makine-kaynak eşleştirme ekranıdır. Üretim-MRP-Kayıt-Kaynak Yönetimi-Makine-Kaynak Eşleştirme yolu izlenerek ilgili ekrana ulaşılabilir. (Bkz. Ekran Görüntüsü 29)

![](../../_assets/b4a2084b25fc04d68b49.png) **Ekran** **Görüntüsü** **29**

Bu ekran üzerinde öncelikle hangi makine için eşleştirme yapılacağı belirtilmelidir. Bunun için "Makine Seçimi" bölümü kullanılmalıdır. Bu alanda makine kodu, makine grubu ya da tümü için seçim yapılabilir. Özelden genele hiyerarşik yapı mantığı bu ekranda da geçerlidir. Tümü seçimi ile eşleştirmeler yapılsa dahi tekil makine kodu/grubu için de ayrı eşleştirmeler yapılabilir. Bu durumda en özel tanımlama geçerli olacak şekilde çizelgeleme yapılacaktır.

Makine seçim alanından sonra "Ürün Seçimi" bölümünden uygun seçim yapılmalıdır. Benzer şekilde burada da ürün kodu, ürün grubu ya da tümü seçimleri yapılabilir.

Son olarak hangi makinede hangi ürün üretilirken hangi kaynakların kullanılacağını tanımlamak için "Set Bilgileri" bölümü kullanılmalıdır. Kaynaklar kod/grup bazında ya da tüm kaynaklar eşleştirilecek şekilde seçilebilir. Kaynak set yapısı bu ekranda da bulunmaktadır. Seçilen makine ve ürünler bazında, farklı kaynak kod/grupları için farklı eşleştirmeler yapılabilir. Bunun için aynı set içinde yeni satırlar şeklinde kayıtlar oluşturmak mümkündür. Ekranın altında bulunan "Yeni Set Ekle" butonuna basılmadığı sürece yapılan her bir giriş aynı set içine yeni bir satır olarak kaydedilecektir. Setlerin hangisinin daha öncelikli kullanılacağı ise "Set Öncelik Sırası" alanı kullanılarak tanımlanabilir. Set mantığı ile ilgili ek açıklamalar için 7. bölüme bakılabilir.

Operasyon-kaynak eşleştirme ekranında da olduğu gibi eşleştirilen kaynaklardan yalnızca hazırlık süresi boyunca kullanılacak bir kaynak varsa, "Kaynak Kullanımı Sadece Hazırlık Aşamasında Yapılsın" parametresi açılmalıdır. Ömür takibi parametresi açılmış kaynaklar için "Ömür Tüketimi" girişi de bu ekran üzerinden yapılabilmektedir. Seçilen makineler ve ürünler için ilgili kaynaktan kaç adet kullanılacağı bilgisi ise "Kaynak Sayısı" alanına girilmelidir.

#### Kural Tanımlama

Operasyon, makine ve ürün bazında belli kurallara göre tanımlamaların yapılabileceği ekran ise "Kural Tanımlama" ekranıdır. Kural Tanımlama ekranına Üretim-MRP-Kayıt-İleri Üretim Çizelgeleme-Kural Tanımlama yolu izlenerek ulaşılabilir. (Bkz. Ekran Görüntüsü 30)

![](../../_assets/3451c16577ce558b14b2.png)**Ekran** **Görüntüsü** **30**

Bu ekranda 3 kural tipi desteklenmektedir; "Birlikte yapılamaz", "Birlikte yapılabilir" ve "Art arda yapılamaz". Bu kurallardan biri "Kural Seçimi" alanından seçildikten sonra "Kural Adı" serbestçe belirlenebilir. Ardından kural tanımlama ekranını sağ ve sol olmak üzere ikiye bölünmüş varsayarak kurallar oluşturulmalıdır. Ekranın sağ tarafı bir "operasyon-makine-ürün" kombinasyonuyken, sol tarafı bir başka "operasyon-makine-ürün" kombinasyonudur. Tanımlanan kural ise bu 2 kombinasyon gerçekleştiğinde geçerli olacaktır. Örneğin Ekran Görüntüsü 30'da; Mak1'de herhangi bir ürün için (Ürün Seçimi: Tümü) montaj operasyonu yapılırken, aynı anda Mak1'de hiçbir ürün için (Ürün Seçimi: Tümü) paketleme operasyonunun yapılamayacağı (birlikte yapılamaz kuralı) tanımlanmıştır.

Kural Tanımlama ekranı üzerinde hem operasyon hem makine hem de ürün seçimleri kod, grup ya da tümü olarak yapılabilmektedir. Ayrıca istenen adette kural tanımlanabilir. Oluşturulan kurallar Tab tuşuyla ilerlendiği takdirde yeni satırlar olarak kaydolacak ve ekranın altında bulunan grid alanında görülebilecektir.

#### Çizelge Modelleme Aracı

![](../../_assets/c6e8065a415d9497e665.png)**Ekran** **Görüntüsü** **31**

Çizelgelemenin hangi algoritmalar ve iş akışıyla çalışacağının tanımlanabileceği ekran "Çizelge Modelleme Aracı"dır. Bu ekrana Üretim-MRP-Kayıt-İleri Üretim Çizelgeleme-Çizelge Modelleme Aracı yolundan ulaşılabilir. (Bkz. Ekran Görüntüsü 31 Ekran üzerinde model oluşturmak için "Model Adı" alanı doldurmalıdır. Ardından tanımlanmakta olan modelin hangi vardiya plan numarası için geçerli olacağı seçilmelidir. Bu seçim "Vardiya Plan No." alanından yapılabilir. Alanın yanındaki göz simgesine tıklayarak fabrika çalışma takvimi sayfasına gitmek mümkündür.

Halihazırda kayıtlı modeller varsa ekranın üst kısmındaki grid'de görülebilir. Kayıtlı modelleri kopyalamak, başka bir isimle kaydedip üzerinde değişiklikler yapmak mümkündür. Bunun için "Model Kopyala" butonu kullanılmalıdır. Buton tıklandığında kopyalanacak modele verilmek istenen ismin yazılabileceği küçük bir pencere açılacaktır.

Ekranın üstündeki grid'den seçilen bir modeli silmek için "Kayıt Sil" butonu kullanılmalıdır. Yeni oluşturulan bir modele ait tasarımı yapabilmek için ise ekranın altında bulunan boş alan kullanılmalıdır. Bu boş alanın hemen yanında bulunan algoritma, script, if/else, bağlantı ve end blokları tasarım yaparken kullanılabilecek araçlardır.

Yeni oluşturulan bir modelin kaydedilebilmesi için en az 1 adet algoritma ya da script bloğu ve 1 adet end bloğu olmalıdır. Bir modelin kaydedilebilmesi için en basit haliyle "algoritmaend" ya da "scriptend" blokları oluşturulup bağlantı bloğu kullanılarak birbirine bağlanmış olmalıdır. Bu işlem yapıldıktan sonra "Kaydet" butonu kullanılarak yeni blok kaydı tamamlanabilir.

Bloklardan herhangi biri sol tuş ile tıklandığında seçilmiş olacaktır. Ardından boş alan üzerine gidip sol tuş basılı haldeyken sürükleme yapılabilir. Sol tuş bırakıldığı an ilgili blok model tasarım alanı üzerinde kaydolmuş olacaktır. Aynı yöntemle istenen bloklar tasarım ekranına eklenebilir. Son blok "end" olacak şekilde bağlantı blokları kullanılarak tüm bloklar birbirine bağlandığında model tasarımı bitmiş olacaktır. Burada asıl önemli olan işletmenin üretim yapısına uygun model tasarımının yapılabilmiş olmasıdır. Örneğin farklı istasyonlar için birden fazla algoritma bloğu kullanılarak her bir istasyon için farklı algoritma opsiyonları seçilebilir. Bu noktada modelleme sırasında tanımlanacak akışın bütün ürünler için geçerli olması ve istasyonlar arasında geri dönüşlerinin olmaması gerekmektedir. Öte yandan daha basit bir uyarlama yöntemi olarak tek bir algoritma bloğu kullanılarak, bu algoritmanın bütün operasyonlar/istasyonlar için çalışması da sağlanabilir.

Kullanılabilir bloklarının içinde bulunan If/Else bloğu koşul mantığıyla çalışmaktadır. Bu yüzden 2 çıkışı olmalı yani 2 bağlantısı bulunmalıdır. Bu bağlantıların ucunda da mutlaka birer blok bulunmalıdır. If bloğunu modelleme alanına sürükledikten sonra üzerine çift tıklanması halinde bir script alanı açılacaktır. Burada istenen koşul oluşturulmalıdır. If bloğuna bağlanacak diğer 2 blok ise, if bloğu içindeki koşulun "Doğru" olması ve "Yanlış" olması halinde çalışacaktır. If bloğunun "True" ucuna bağlanan algoritma, if bloğu içindeki koşul "Doğru" sonucu döndürdüğünde çalışacaktır. Bloğun "False" ucuna bağlanan algoritma ise, if bloğu içindeki koşuldan "Yanlış" sonucu döndüğünde çalışacaktır.

Kullanılabilir bloklarının içinde bulunan Script bloğu ise özel bir iş mantığının veya algoritmanın oluşturulması için kullanılabilir. Script bloğunun içi doldurulduktan sonra ihtiyaca uygun şekilde tasarlanan modelin içine yerleştirilmeli ve bağlantıları yapılmalıdır.

Algoritma bloğunu kullanabilmek için tasarım alanına sürüklenen algoritma bloğu üzerine çift tıklanmalı ve "Algoritma Özellikleri" penceresi açılmalıdır. Ardından bu pencerede "Genel Algoritma" klasörü içinde bulunan "EnjeksiyonAlgoritması" ya da "GenelAlgoritma" seçeneklerinden biri seçilmelidir. (Bkz. Ekran Görüntüsü 32) Enjeksiyon prosesi üretimine dahil olan işletmelerde enjeksiyon algoritması kullanılabilir. Diğer üretim tipleri için genel algoritma kullanılmalıdır.

![](../../_assets/79e528dd3d8d5142f7d0.png)**Ekran** **Görüntüsü** **32**

Algoritma özellikleri ekranının alt kısmında bulunan 2 sekmeden "Operasyon Seçimi" sekmesi, seçilen algoritmanın hangi operasyonlar için çalıştırılacağını belirleyecektir. Buradan operasyon kodu, operasyon grubu ya da tüm operasyonlar seçimleri yapılabileceği gibi istasyon kodu seçimi de yapılabilmektedir. Tüm operasyonlar dışında bir seçim yapılması halinde "Operasyon Kodu" alanı aktifleşecektir. Alanın bitimindeki "üç nokta" simgesi tıklandığında tanımlanmış operasyon kodlarının, operasyon gruplarının ya da istasyon kodlarının tamamının bulunduğu bir ekran açılacaktır. (Bkz. Ekran Görüntüsü 33) Bu ekran üzerinde her satırın önünde bir kutucuk bulunmaktadır. Bu kutucuklara tıklanarak ilgili satırlar seçilebilmektedir. Bu ekranda istenildiği kadar seçim yapılabilir. Ardından ekranın altında bulunan "Tamam" butonuna tıklanmalıdır. Bu işlemler tamamlandığında seçilen algoritma seçim yapılan satırlar için geçerli olacak ve çizelgeleme bu mantıkla çalışacaktır.

![](../../_assets/9d4c2858bf29bb433a0a.png)**Ekran** **Görüntüsü** **33**

Algoritma özellikleri ekranında bulunan bir diğer sekme de "Algoritma Opsiyonları" sekmesidir. Bu sekmede seçilen algoritmaya göre değişkenlik gösteren parametre ayarları bulunmaktadır. Genel algoritmaya ait opsiyonlar Ekran Görüntüsü 34'da görülebilir.

![](../../_assets/12e36f07ab4398f5ebb5.png)**Ekran** **Görüntüsü** **34**

Bu ekranda sırasıyla dikkate alınacak olan 5 adet "İşleri Sıralama Kriteri" bulunmaktadır. Her bir alan için listeden seçim yapmak gereklidir. Genel anlamda teslim tarihi, hazırlık süresi, işlem süresi, iş emri önceliği, kalan operasyon sayısı, stok kartı kod 1-2-3-4-5, stok kartı grup kodu, stok kartı kullanıcı tanımlı saha kriterlerine göre büyükten küçüğe ya da küçükten büyüğe seçim yapmak mümkündür.

Burada algoritmaya, boşta olup iş emri yerleştirmek için seçilen bir makineye, hangi kurala göre iş emri yerleştireceği bilgisi verilmektedir. Yerleştirilecek iş emirlerine ise daha önce tanımlama yapılan eşleştirme ekranlarındaki kısıtlar dikkate alınarak karar verilmektedir. Örneğin; Ekran Görüntüsü 34'te teslim tarihi en küçük olan iş emrini en önce yerleştir komutu görülmektedir. Diğer kriter alanlarına da listeden seçim yapılırsa teslim tarihi eşit olan iş emirlerini yerleştirmek için, algoritma sırasıyla diğer kriterleri kontrol edecek ve eşitlik olmayan ilk kriteri uygulayacak şekilde çalışacaktır.

Hazırlık süresi hesaplama politikası parametresi içinde mevcut olan 9 seçenekten istenen biri seçilip çizelgeleme bu doğrultuda çalıştırılabilir. İlk seçenek olan "Hazırlık süreleri dikkate alınmasın" seçilirse, program hiç hazırlık süresi yokmuş gibi çalışacaktır. Diğer bir seçenek olan "Hazırlık sürelerinin toplamı" seçildiğinde, ürün, operasyon, kaynak değişimi gibi değişimlerden kaynaklanan ve hazırlık süresi tanımlama ekranında tanımlanmış olan hazırlık sürelerinin tamamının toplamı dikkate alınacaktır. Yine bu seçeneklerden "Hazırlık sürelerinin en küçüğü" ya da "Hazırlık sürelerinin en büyüğü" seçimlerinden birinin yapılması halinde, hazırlık süresi tanımlama ekranında tanımlanmış olan hazırlık sürelerinin en büyüğü veya en küçüğüne göre çizelgeleme yapılacaktır. Alandaki diğer seçimler ise hazırlık süresi tanımla ekranı üzerindeki 5 farklı seçeneğe karşılık gelecek ayarları içerir. "Kendisine ait hazırlık süresi", "Ürün değişimi hazırlık süresi", "Kaynak değişimi hazırlık süresi", "Operasyon

değişimi hazırlık süresi" ya da "Script hazırlık süresi" seçeneklerinden biri seçilirse, yalnızca seçilen hazırlık süresi dikkate alınarak çizelgeleme yapılacaktır.

Kaynak kullanım politikası, hangi kaynak eşleşmelerinin dikkate alınacağını belirlemek için kullanılmaktadır. "Kaynaklar dikkate alınmasın" seçimi, çizelgelemede hiçbir kaynak eşleştirmesinin dikkate alınmamasını sağlamaktadır. "Operasyon-Kaynak eşleşmesi" ya da "Makine-Kaynak eşleşmesi" seçenekleri seçilirse yalnızca seçilen eşleşme dikkate alınarak çizelgeleme yapılacaktır. "Tüm eşleşmeler dikkate alınsın" seçeneği de ekranlarda tanımlanan tüm eşleştirmeleri dikkate alarak hesaplama yapılmasına yaramaktadır.

Geçiş miktarı politikası, tanımlanmış olan geçiş miktarlarının çizelgelemede dikkate alınıp alınmayacağını belirlemek için kullanılır. "Dikkate alınmasın" ya da "Dikkate alınsın" seçimleri bu sebeple bulunmaktadır. Eğer operasyon tanımlama ekranında geçiş miktarları tanımlanırken "Otomatik Hesaplansın" seçeneği işaretlendiyse, algoritma opsiyonlarında da "Dikkate alınsın ve miktar otomatik hesaplansın" seçeneği seçilmelidir.

İş emri bölme politikasında ise 3 seçenek vardır. "İş emirlerini bölme" seçeneği seçildiğinde bir iş emri bitene kadar aynı makinede üretim devam edecek şekilde çizelgeleme yapılacaktır. "Otomatik dağıt" seçeneği, iş emri zamanında tamamlanacak şekilde en az sayıda makineyle işi bitirecek şekilde parçalama yapabilmektedir. "Tamamına dağıt" seçeneği ise iş emrinin, üretilebileceği tüm alternatif makinelere eşit paylaştırılması metoduyla çalışmaktadır.

"Stok Bakiyeleri Dikkate Alınsın" parametresi sistemdeki yarı mamul ve mamul bakiyelerini dikkate alarak çizelgeleme yapılmasını sağlamaktadır. Örneğin bir mamulün oluşması için gereken yarı mamulün bakiyesinin olup olmadığı dikkate alınsın ve bakiyenin yetersiz olduğu durumda öncelikle bu yarı mamule ait iş emri planlansın istenirse bu parametre işaretlenebilir.

"Öncelik iş Emrinden Okunsun", "Öncelik Siparişten Okunsun", "Öncelik Plan Kayıtlarından Okunsun" parametrelerinin hepsi işleri sıralama kriterlerinden iş emri önceliği büyükten küçüğe ya da küçükten büyüğe seçiliyse kullanılmak üzere tasarlanmıştır. İş emri önceliği neye verilmek isteniyorsa, hangi kayıttan okunarak çalışılsın isteniyorsa ona göre bir parametre seçilmesi gerekmektedir.

Önceliklerin iş emrinden okunabilmesi için iş emri kayıt ekranındaki "Sıralama Önceliği" alanı doldurulmalıdır. İş emri ekranında "Sıralama Önceliği" sahasının aktif olması içinse 'URETIM',' ISEMRISIRAONCELIKGIRILSIN' özel parametresinin tanımlanması gerekmektedir. Önceliklerin siparişten okunabilmesi için siparişlerin öncelik bilgilerinin tutulduğu sahada öncelik bilgisi girilmiş olmalıdır. Önceliklerin plan kayıtlarından okunabilmesi için de üretilecek mamulün stok planlama kaydında öncelik bilgisi bulunmalıdır.

Eğer her 3 parametre de açılırsa, ilk parametre öncelikli olacak şekilde bir hiyerarşi izlenerek 3 parametre de dikkate alınacaktır.

"MRP Tedarik Planı Dikkate Alınsın" parametresi sipariş bazında rezervasyon sisteminin kullanıldığı ve iş emirlerinin MRP üzerinde açıldığı durumlarda kullanılmalıdır. MRP üzerinden hangi hammaddenin ne zaman geleceği bilgisi takip edilebildiğinden, malzemesi üretime hazır halde bulunmayan iş emirlerinin çizelgelemeye alınmaması bu parametre ile kontrol edilebilmektedir. Örneğin herhangi bir iş emri için MRP'nin önerdiği hammadde satın alma sipariş tarihi 15.09.2018 ise, bu hammaddeyi kullanacak iş emri 15.09.2018 tarihinden sonraya çizelgelenecektir.

"Ön İhtiyaç Miktar Kontrolü Yapılmasın" parametresi bir mamulün üretilmesi için ihtiyaç duyulan yarı mamul miktarının mevcut iş emirleri veya stok bakiyeleri tarafından karşılanıp karşılanamadığının kontrolüyle ilgilidir. Bu kontrolün yapılması istenmediğinde bu parametre işaretlenebilir. "Stok Bakiyeleri Dikkate Alınsın" parametresinin açıldığı durumlarda bu parametre açılmamalıdır. Aksi halde stok bakiyeleri dikkate alınmayacaktır.

"Ömrü Biten Kaynakların Bakımı Planlansın" parametresi kaynak tanımlarının, eşleştirmelerinin yapıldığı ve kaynak tanımlama sırasında "Ömür takibi yapılsın" parametresinin açıldığı durumlarda çalıştırılabilir. Ömrü biten kaynakların bakım zamanlarının takip edilmesi ve bakıma gidip geleceği sürelerin göz önünde bulundurularak çizelgeleme yapılabilmesi için bu parametre açılmış olmalıdır.

Enjeksiyon algoritmasına ait algoritma opsiyonları Ekran Görüntüsü 35'te görülebilir. Burada genel algoritmada açıklanan opsiyonlar haricinde yalnızca bir parametre bulunmaktadır. "Yürüyen Planlama Aralığı (Gün)" parametresi enjeksiyon algoritmasının ihtiyaçları kaçar günlük bloklar halinde ele alıp planlayacağını belirtmek için kullanılmalıdır.

![](../../_assets/8e73f43868d5803de85a.png)**Ekran** **Görüntüsü** **35**

Oluşturulan algoritma bloklarının içinden istenen tanımlama ve ayarlar yapıldıktan sonra modelleme alanı içinde bağlantısı yapılmamış blok kalmadığından ve algoritma sonuna bir end bloğu konulduğundan emin olunmalıdır.

Model oluşturulurken "Editör İşlemleri" butonu kullanılarak geri alma, kesme, kopyalama gibi komutlar yerine getirilebilir. "Görünüm Ayarları" butonundan ise modelleme alanının görünüme dair yakınlaştırma, uzaklaştırma, ekrana sığdırma gibi işlemler yapılabilmektedir. Yine ekranda bulunan "Model Dosya İşlemleri" butonu ile oluşturulan modelin kaydedilmesi, yeni bir model dosyası oluşturulması ya da var olan bir model dosyasının açılması işlemleri yapılabilmektedir.

#### İleri Üretim Planlama

Model oluşturulma ve kaydedilme aşamasının tamamlanmasının ardından sistem, üretim planlama için hazır hale gelecektir. Üretim planı oluşturmak için Üretim-MRP-Kayıt-İleri Üretim Çizelgeleme-İleri Üretim Planlama rotası izlenmelidir. (Bkz. Ekran Görüntüsü 36)

![](../../_assets/6daa72f4ac5f62b9e43a.png)**Ekran** **Görüntüsü** **36**

Bu ekranda 2 sekme bulunmaktadır. "Kısıt Girişi" sekmesi, planlama bilgisi bölümündeki "Başlangıç Tarihi" alanına iş emirlerinin yerleştirilmeye başlanmak istendiği tarih ve saat girilmelidir. "İş Emri Teslim Tarihi Aralığı" alanı ise filtreleme görevi yapmaktadır. Buraya bir tarih aralığı girildikten sonra "Kayıtları Getir" butonuna basılarak bu aralıkta teslim tarihi olan iş emirlerinin ekranın altındaki alanda listelenmesi sağlanabilir. Butonun hemen yanındaki küçük seçim butonuna tıklandığında iş emirlerinin getirilebileceği diğer yöntemler de görülebilmektedir. İş emirleri Excel'den yüklenebilir ya da MRP sonuçlarından da getirilebilir.

Excel'den yükleme yapılabilmesi için Excel dosyasının kolonlarının program tarafından istenen kolonlarla eşleşmesi gerekmektedir. Bunu yapabilmek için kayıtları getir butonu içinden "Excel'den Yükle" seçilmeli ve sonrasında açılan pencerenin "Dosya Seçimi" sekmesinden .xls formatındaki dosya seçilmelidir. "İleri" butonuna tıklandıktan sonra "Sayfa ve Kolon Seçimi" sekmesine gidilecektir. Bu sekmede programın kullanıcıdan beklediği kolonlarla, açılan Excel sayfası kolonları Ekran Görüntüsü 37'de işaretlenmiş menülerden seçilerek eşleştirilebilir. Ayrıca seçilen Excel sayfasının başlık satırının bulunup bulunmamasına göre "Başlık Satırı Mevcut Mu?" parametresini kullanmak gereklidir. Aktarılacak Excel kitapçığının birden fazla sayfası varsa, aktarılacak sayfanın hangisi olduğunu belirtmek için "Aktarılacak Excel Sayfasını Seçiniz" alanı kullanılmalıdır. "Hatalı Kayıtlar Politikası" alanı kullanılarak ise, aktarılan Excel sayfasında hatalı kayıtlar bulunursa aktarma işlemini tamamen durdurmaya ya da hatalı kayıtları aktarmayacak şekilde aktarımı yapmaya karar verilebilir.

![](../../_assets/754e3add48e882cd79cb.png)**Ekran** **Görüntüsü** **37**

İleri üretim planlama ekranındaki "Çizelgeleme Modeli" alanından ise çizelgelemenin hangi modeli kullanarak çalıştırılacağı seçilmelidir. Bu alanın yanındaki göz simgesine tıklanarak çizelgeleme modelleme aracı ekranına gidilebilir.

Ekranın altında listelenecek iş emirlerine ileri kısıt verilmek istenirse 36. ekran görüntüsünde mor kutucuk ile gösterilen + simgesine tıklanarak "İş Emri Kısıtları" alanı açılabilir ve bu alanda istenen kısıtların kaydı gerçekleştirilebilir.

Yine bu ekrandaki "Tamamı Transfer Edilmiş İş Emirleri Getirilsin" parametresi, iş emrinin ihtiyaç duyduğu malzemelerin depolar arası transfer yapılarak çalışıldığı durumlarda geçerlidir. Bu şekilde bir çalışma sistemi kurulduysa ve bu parametre açıldıysa, bir iş emrine ait tüm malzeme ihtiyaçlarının transferi tamamlanmadığı sürece o iş emri ekrandaki listeye gelmeyecektir.

"UAK Kaydı Bulunan İş Emirleri Getirilsin" parametresinin açılması durumunda ise verilen diğer filtrelere uygun iş emirleri gelecek ve bunlara ek olarak üretim akış kaydı olan tüm iş emirleri de listeye eklenecektir. Yani bu parametre işaretlenerek filtrelere uymayan fakat üretim akış kaydı bulunan iş emirlerinin de getirilmesi sağlanabilir. Ekranda bulunan "Tümünü Seç" ve "Tümünü Kaldır" butonları listelenen iş emirlerinin tamamının seçilmesini ya da tamamından seçimlerin kaldırılmasını sağlamaktadır.

"Hata Kontrolü" butonu iş emirleri aktarılırken tespit edilen hataların raporunu almak için kullanılmaktadır. Bu botunun hemen yanındaki küçük seçim butonundan, "Rapor Hazırla" ya da 'Gridde Göster" seçimleri yapılabilmektedir.

"İş Emri Sabitleme" butonu kullanılarak istenilen bir iş emri belirlenecek olan bir tarihe sabitlenebilir. Bunun için butona tıkladığında bir pencere açılacak ve çizelgelenecek iş emirleri listelenecektir. Sabitlenmek istenen iş emri bulunup ilk sütundaki ("Sabit" sütunu) kutucuk tıklanarak seçim yapılabilir. Ardından iş emrinin bulunduğu satıra ait "Sabitlenen Tarih" alanına, iş emrinin sabitlenmek istediği tarih ve saat yazılarak bu iş emrinin çizelgeleme üzerindeki yeri manuel olarak belirlenebilir. (Bkz. Ekran Görüntüsü 38) Sabitlenen iş emri için kullanılacak makine kodu ve kaynak kodu bilgisi de isteğe

bağlı olarak girilebilir. Bu bilgiler boş bırakılırsa çizelgeleme sırasında algoritma makine ve kaynak seçimlerini otomatik olarak yapacaktır, aksi durumda sabitlenen makine ve kaynak bilgisi kullanılacaktır.

Ekran üzerinden "Grupla" butonu tıklanarak gruplama seçeneklerinden uygun olan seçilebilir ve iş emirleri bu seçilen grup bazında görüntülenip sabitlenebilir. Ayrıca grup ekranı üzerinde sağ tık menüsü mevcuttur. Bu menüden grubu sabitleme, tüm kırılımları açma/kapama, gruba toplu sabitleme tarihi atama gibi işlemler de yapılabilmektedir. Sabitlenecek işlerin Excel üzerinden topluca aktarılması için "Excel'den Yükle" butonu kullanılabilir. İstenen tüm ayarlar yapıldıktan sonra da "Kaydet" butonu ile tanımlamalar kaydedilmelidir. İş emri sabitleme ekranında kaydedilen bilgiler geçici değildir, sistemde saklanarak daha sonra çalıştırılacak çizelgeleme işlemlerinde de dikkate alınacaktır.

![](../../_assets/0c0f035b929ab2b8748e.png)**Ekran** **Görüntüsü** **38**

Tüm bu tanımlamalar yapıldıktan sonra ise "Çizelgeyi Oluştur" butonu tıklanarak yeni bir çizelgeleme yapılabilir. Eğer öncesinde yapılıp taslak olarak kaydedilmiş çizelgelemelerden biri görüntülenmek istenirse ileri üretim planlama ekranındaki "Kaydedilen Taslaklar" sekmesinden işlem yapılmalıdır. (Bkz. Ekran Görüntüsü 39)

![](../../_assets/2733e10729f39b28279d.png)**Ekran** **Görüntüsü** **39**

Bu ekranın altındaki grid'de kaydedilmiş taslaklar görülebilir. "Taslağı Aç" butonu seçilen taslağı açıp görüntülemeye yaramaktadır. "Aktifleştir" butonu yardımıyla seçilen taslak aktifleştirilerek üretim planı olarak kullanılabilir. "Görünüm" butonuyla grid'de listelenmesi istenen taslaklara ait seçimler yapılabilir. "Yenile" butonuyla grid yeniden yüklenebilir. Aktifleştirilmiş bir taslak "Deaktifleştir" butonuyla deaktive edilebilir. "Taslağı Sil" butonu ile seçilen bir taslak silinebilir. "UAK Kayıt Yap"

butonu ise seçilen taslağa ait planlama bilgilerinin üretim akış kontrol modülüne aktarımını ve akışın bu modülden takibini sağlamaktadır.

#### Çizelge Gantt Ekranı

İleri üretim planlama ekranı üzerinden "Çizelgeyi Oluştur" butonu tıklandığında program arka planda iş emirlerinin yerleşimlerini belirleyip kullanıcı karşısına bir Gantt şeması çıkaracaktır. Bu şemada iş emirlerinin yerleşimleri görülebilmektedir. (Bkz. Ekran Görüntüsü 40) Ekranın sol tarafında istasyon ve makine bilgileri görülmektedir. İş emirleri makine kodlarının karşısına, ilgili operasyonlara göre yerleştirilmiştir.

![](../../_assets/eaff9830d7f29003d99a.png)**Ekran** **Görüntüsü** **40**

Gantt çizelgesi üzerinde varsayılan olarak makine görünümü görülecektir ancak istenmesi halinde "Görünüm" butonu kullanılarak kaynak ya da sipariş görünümüne geçilebilir. Ayrıca ekran görüntüsü 40 üzerinde mor kutu içinde gösterilen seçenekler kullanılarak saniye, dakika, saat, gün, hafta, ay ve yıl görünümlerini seçmek mümkündür. Çizelge üzerinde sağ tık menüsü bulunmaktadır. Sağ tık ile görünümü istenen şekilde yakınlaştırıp uzaklaştırmak mümkündür.

Çizelge alanında farklı iş emirleri farklı renkte çubuklar olarak bir zaman ekseni üzerinde görülmektedir. Ekranın altındaki kaydırma çubuğu kullanılarak zaman ekseninde gezilebilir. Renkli barlardan biri tıklandığında bağlantı okları görülecektir. Bu oklar ilgili iş emrinin izleyeceği yolu, öncül- ardıl operasyonlarını göstermektedir. Renkli barlardan biri çift tıklandığında ise yalnızca o iş emri ve o iş emrine bağlı bulunan öncül-ardıl iş emirleri görüntülenecek, diğer iş emirleri gizlenecektir. Görünümü önceki haline getirebilmek için boş bir alanı çift tıklamak yeterlidir. Çubuklar üzerinde durulduğunda ise iş emri, operasyon, makine, ürün, planlanan zaman ve varsa kaynak kullanım detayları görüntülenebilmektedir.

İş emirlerinin üzerindeki sarı ünlem işaretleri ilgili iş emrinde gecikme olduğunu temsilen bulunmaktadır. Üzerinde durulduğunda teslim tarihine göre ne kadar gecikme olduğu bilgisi görüntülenebilir. İş emirlerinin önünde görülen kırmızı çizgilerle taralı çubuklar ise hazırlık sürelerini temsil etmektedir.

Herhangi bir iş emri çubuğu tutulup sürüklenerek zaman ekseni üzerinde istenilen başka bir yere kaydırılabilir. Daha sonra bu çubuk üzerine sağ tıklayarak bırakılan yere sabitleme yapılabilir ya da aynı şekilde yapılan bir sabitleme kaldırılabilir. Bu işlem yapıldıktan sonra "Yeniden Çizelgele" butonuna tıklanmalıdır. Bu şekilde sabitlenen ya da sabitlemesi kaldırılan iş emirleri dikkate alınarak yeni bir çizelge oluşturulacaktır. Yine aynı sağ tık menüsünden "Taşı ve Sabitle" seçimi yapılırsa, taşınmak istenen tarihin kullanıcı tarafından girilebileceği bir ekran açılacaktır. İlgili iş emrinin taşınmak ve sabitlenmek istendiği tarih bu şekilde manuel girilebilir. Giriş yapılıp "Tamam" butonuna tıklandığında ilgili iş emrinin üretilebileceği makinelerin listesinin bulunduğu bir ekran daha açılacaktır. Bu ekrandan da iş emrinin üretilmesi istenen makine seçimi yapılmalıdır. Kullanıcı karşısına gelecek makine listesinde yalnızca ürünün eşleşmesi olan makineler bulunacaktır. Benzer şekilde çizelge ekranı üzerinde sürükle bırak yöntemiyle de makine değişimi yapılabilir. Yine yalnızca ürünün eşleşmesinin olduğu makinelere sürüklemeye izin verilecektir.

İş emri sabitleme işlemini tablo üzerinden yapabilmek için "İş Emri Sabitleme" butonu da kullanılabilir. Butona tıklandığında ileri üretim planlama ekranındaki iş emri sabitleme butonuyla aynı ekran açılacaktır. Ekranın kullanım detayları için 13. bölüme ve 38. ekran görüntüsüne bakılabilir. Sabitlemeler buradan yapılıp kaydedildiğinde otomatik olarak yeniden çizelgeleme yapılacaktır.

Oluşturulan bir çizelgeleme taslak olarak kaydedilebilir. Bunun için" Taslak Kaydet" butonu kullanılmalıdır. Butona tıklandığında "Çizelge Taslak Açıklaması" ekranı gelecektir. Bu ekranda taslak kaydının yapıldığı tarih, saat ve model adının bulunduğu varsayılan bir taslak ismi otomatik gelecektir ancak istenilmesi halinde taslağa serbestçe bir isim vermek de mümkündür. Kaydedilen taslaklar 13. bölümde anlatıldığı şekilde görüntülenebilir ya da yeniden aktifleştirilebilir. Özelliğin kullanım detayları için 13. bölüme ve 39. ekran görüntüsüne bakılabilir.

Ekrandaki "Arama" butonuna basıldığında ekranda 3 yeni alan açılacaktır. Bu alanlar kullanılarak sipariş numarası, iş emri numarası ve operasyon kodu bazında arama yapmak mümkündür. Alanların yanındaki rehber ikonları kullanılarak listeden seçim yapılmasına da olanak sağlanmaktadır. Sonrasında "Ara" butonuna tıklandığında çizelgeleme ekranında yalnızca arama sonucuna uygun işler görüntülenecektir. "Temizle" butonuna tıklanarak çizelgeleme ekranı önceki haline döndürülebilir.

Ekrandaki "Ayarlar" butonuna tıklandığında ise "Çalışılmayan Zamanları Göster" ve "İşlerin Çalışılmayan Zamana Gelen Kısımlarını Göster" parametrelerinin olduğu bir alan açılacaktır. Buradaki parametreleri kullanarak çizelge görüntüsünde ayarlama yapmak mümkündür.

"Dışa Aktar" butonu yardımıyla ise ilgili çizelgeleme sonuçları Excel dosyası ya da ekran resmi olarak bilgisayar ortamında saklanabilir. Ek olarak yazdırarak çıktı olarak arşivlemek de mümkündür.

"MRP Güncelle" butonunun aktif olması için ileri üretim planlama ekranının ilk sekmesinde "Kayıtları Getir" işlemi "MRP Sonuçlarından Getir" olarak seçilmiş olmalıdır. "MRP Güncelle" butonu tıklandığında, MRP sonuçları çizelgeleme sonuçlarına uygun olarak arka planda güncellenecektir. Güncellenen MRP sonuçlarını kullanarak gerekli satın alma ve iş emri belgelerini açmak için "Malzeme Gereksiniminden İş Emri Oluşturma" ve "Malzeme Gereksiniminden Sipariş/Talep Oluşturma" ekranları kullanılmalıdır.

Ekrandaki "Raporlar" butonu tıklandığında 11 farklı rapor seçeneği görüntülenecektir. Bunlardan uygun olan raporlar oluşturulup incelenebilir, istenirse kaydedilmesi de mümkündür. Raporlar üzerinde sağ tık menüsü çalışmaktadır. Sağ tıklanıp "Gönder" seçeneği üstüne geldiğinde HTML ya da Excel'e gönderme opsiyonları görülecektir. Buradan yapılacak seçime göre raporlar kaydedilebilmektedir. Yine sağ tık menüsü içinde "Gruplama" seçeneği aktifleştirilirse, ekranın en üstünde bir alan aktifleşecektir. Bu alana istenen bir sütun ya da sütunlar sürüklenerek bu sütunlar

bazında gruplama yapılabilecektir. Yukarıdaki alana sürüklenmiş olan sütunlar aynı şekilde grid alanına yeniden sürüklenerek gruplamalar iptal edilebilir. (Bkz. Ekran Görüntüsü 41) 41. ekran görüntüsünde kırmızı kutu içine alınmış alan gruplanmak istenen sütunların sürüklenebilmesi için oluşan alandır. Bu örnek görüntüde "Makine Kodu" sütununa göre gruplama yapılmış bir rapor görülmektedir.

![](../../_assets/8b69110452fa3280744b.png)**Ekran** **Görüntüsü** **41**

Raporlar içinde bulunabilecek ilk rapor "Çizelgelenen İşler Raporu" dur. Bu raporda çizelgeleme ekranı üzerinde görülen tüm iş emirleri ve bunlara ait planlama detayları liste halinde görülebilir. İkinci rapor ise "Çizelgelenemeyen İşler Raporu" dur. Bu raporda, varsa çizelgelemeye dahil edilemeyen iş emirleri liste halinde görülebilir. Aynı zamanda iş emirlerinin neden çizelgelenemediklerine dair açıklamalar da mevcuttur. Örneğin rota tanımı bulunmadığı için çizelgelenemeyen bir iş emrinde "Rota Tanımı Bulunmuyor" şeklinde bir açıklama görülecektir.

Bir diğer rapor ise "Geciken İşler Raporu" dur. Bu raporda geciken işler varsa listelenecektir. Gecikme süresi ve planlanan teslim tarihi bilgileri de raporda bulunmaktadır.

Bu raporların dışında listede "Çizelge Performans Raporu" (Bkz. Ekran Görüntüsü 42) ve "Performans Karşılaştırma Raporu" bulunmaktadır. Performans raporları çizelgelemeye ait çalışma süresi, çizelgelenen iş emri sayıları, hazırlık süreleri gibi birçok bilgi içermektedir. Performans karşılaştırma raporu ise çizelge modeli oluşturma sürecini destekleyici bir rapordur. Farklı modeller oluşturulup bu modeller için aynı iş emirlerine ait farklı çizelgeler oluşturulabilir ve bu sonuçlar taslak olarak kaydedilebilir, sonrasında bu taslaklara ait performans karşılaştırma raporu alınarak hangi modeli kullanmanın daha uygun olacağına karar verilebilir. Burada karşılaştırılabilecek taslak sayısı 3 ile sınırlıdır. Performans karşılaştırma raporuna tıklandığında kullanıcı karşısına çıkacak ilk ekrandan karşılaştırılmak istenen taslak kodlarına göre seçim kutucukları işaretlenerek seçim yapılmalı ve sonrasında "Tamam" butonuna basılarak rapor getirilmelidir. (Bkz. Ekran Görüntüsü 43)

![](../../_assets/17c8b019c712db249a89.png)**Ekran** **Görüntüsü** **42**

![](../../_assets/b63254ceceeab9a18a03.png)**Ekran** **Görüntüsü** **43**

"Sipariş Termin Raporu" çizelgelenen iş emirlerinin bağlı bulunduğu müşteri siparişlerinden geciken olup olmadığını özet halinde göstermeye yarayan bir rapordur. Aynı zamanda tahmini teslim tarihlerini de göstererek gecikme hakkında detay vermektedir.

"Çizelge Bazlı Kapasite Raporu" çizelgelemesi yapılan iş emirlerine göre makinelerin doluluk oranlarını göstermeye yarayan bir rapordur. Bu rapor tıklandığında açılan ilk ekrana, bu raporun hangi tarih aralığı için oluşturulacağı, hangi rapor tipi kullanılacağı ve bu aralıkta hangi periyodlar için gösterim yapılacağı girilmelidir. "Rapor Tipi" alanından "Genel" seçimi yapıldığında görsel rapor oluşacaktır. "İstasyon Bazında", "Makine Bazında" veya "Kaynak Bazında" seçimleri yapıldığında ise seçilen tipe göre tablo halinde grid ekranda raporlar oluşacaktır. Ayrıca kullanılmayan istasyonların gösterilip gösterilmeyeceğine ait bir parametre de bulunmaktadır. (Bkz. Ekran Görüntüsü 44) Bu alanlar doldurulduktan sonra "Raporu Göster" butonuna tıklanarak rapor görüntülenebilir. (Bkz. Ekran Görüntüsü 45) Bu rapordaki büyük daireler ilgili istasyonun ilgili periyodundaki makine doluluk oranını gösterirken, küçük daireler ise kaynak doluluk oranını göstermektedir.

![](../../_assets/d34e9d61ecc79e553151.png)**Ekran** **Görüntüsü** **44**

![](../../_assets/3a70aee811173364ffb6.png)![](../../_assets/cc1cc616b9d78ee6d1f3.png)**Ekran** **Görüntüsü** **45**

Çizelge bazlı kapasite raporunun en altında kaynak ve makinelerin fabrika genelindeki doluluk oranları çizgi grafik halinde görülmektedir. Ayrıca 45. ekran görüntüsünde kırmızı ile işaretlenmiş şekilde görülebileceği gibi, ekrandaki her bir karenin sol alt köşesinde bir + sembolü bulunmaktadır. Bu sembole tıklanarak ilgili istasyona ait detaylar görüntülenebilir. (Bkz. Ekran Görüntüsü 46) 46. ekran görüntüsünde mor kutucuklar içine alınmış sekmelerden kaynak ve makine bazında detay görüntülemek mümkündür. Kırmızı kutucuk içinde gösterilmiş "Geri" sembolü yardımıyla ise raporun özet haline geri dönülebilir.

![](../../_assets/4fc0280b2617ef80a5b0.png)**Ekran** **Görüntüsü** **46**

"Serbest Rapor" ise arka planda tutulan tüm veriyi içeren bir tablodur. Tıpkı çizelgelenen işler raporunda olduğu gibi bu raporda da istenen sütunlar gruplama alanına sürüklenerek çalışılabilir. Bu şekilde istenen herhangi bir raporun kullanıcı tarafından oluşturulabilmesi mümkün olmaktadır.

"İş Emri Kullanım Raporu" tüm iş emirlerinin kullanım bilgilerini öncül-ardıl şekilde göstermektedir. Çizelge Gantt ekranı üzerinde herhangi bir çubuğa tıklandığında, o iş emrinin öncül-ardıl operasyonlarına ait bağlantı bilgilerinin gösterimi, tablo olarak bu raporla alınabilir. Hangi iş emirlerinin hangi iş emirleri tarafından kullanıldığı bilgisi ve detaylar iş emri kullanım raporunda bulunmaktadır. (Bkz. Ekran Görüntüsü 47)

![](../../_assets/923441ae178015306507.png) **Ekran** **Görüntüsü** **47**

"Kaynak Bakım Planı Raporu" kaynaklar için ömür takibi yapılan işletmelerde kullanılabilecek bir rapordur. Ömür takibi yapılan kaynakların ne zaman bakıma gideceği ve ne zaman döneceği gibi bilgiler bu raporda görülebilmektedir.

"Personelin Aynı Anda Baktığı Makineler Raporu" enjeksiyon algoritması için geçerli bir rapordur. Tek bir personelin aynı anda yürüttüğü birden fazla makine varsa, bu makinelere ve operasyonlara ait bilgiler bu rapordan alınabilir.

Tüm bunların dışında Üretim-MRP-Raporlar-İleri Üretim Çizelgeleme yolu altında ileri üretim çizelgeleme kullanabilmek için yapılan tanımlamalara ait raporlar bulunmaktadır. İhtiyaç duyulması halinde buradan gerekli raporlar alınabilir. (Bkz. Ekran Görüntüsü 48)

![](../../_assets/abd6c02429b182c8ba3c.png)**Ekran** **Görüntüsü** **48**

#### UAK Aktarımı

İleri üretim planlama ekranının "Kaydedilen Taslaklar" sekmesinde, daha önce oluşturulmuş ve kaydedilmiş taslakların bulunduğu ve bu taslaklardan birinin aktifleştirildiği durumlarda "UAK Kayıt Yap" butonu aktifleşecektir. UAK kaydının sağlıklı şekilde yapılabilmesi için ise öncesinde UAK kayıt menüsünden aktivite tiplerinin tanımlanmış olması gerekmektedir.

UAK aktarım ekranında, "UAK Aktarım" ve "USK ve İş Emri Kapatma" olmak üzere 2 sekme bulunmaktadır. (Bkz. Ekran Görüntüsü 49) UAK Aktarım sekmesinde mevcut çizelge taslağına ait iş emirlerinin durumları ve varsa kullanılan kaynak bilgileri bulunmaktadır. Listelenen iş emirlerini satır bazında "Bitti", "Başladı Bitmedi" ya da "Başlamadı" durumlarıyla kaydetmek mümkündür. Bunun için ilgilenilen satırdaki "Bitti" sütununa çift tıklanmalıdır. Böylece ilgili satırın tıklanan sütununda 3 ikon belirecektir. İstenen durum bu ikonlara tıklanarak satır bazında seçilebilir. Yine satır bazında gerçekleşen miktar bilgisi de kullanıcı tarafından serbestçe girilebilmektedir. Burada dikkat edilmesi gereken şudur ki; gerçekleşen miktar bilgisi, iş emri miktarından büyük girilmek isteniyorsa üretim modülündeki "İş emrine bağlı üretimde fazla üretim yapılabilsin" parametresinin açılmış olması gerekmektedir. Ayrıca bu kayıtların hepsi, ekrandaki butonlar yardımıyla tüm satırlar için de yapılabilmektedir.

![](../../_assets/216096e4e85ed9a489a1.png)**Ekran** **Görüntüsü** **49**

USK ve İş Emri Kapatma sekmesinde ise UAK aktarımı yapılmış kalemler listelenmektedir. Bu ekranda toplu üretim sonu kaydı yapılabilmekte ve iş emirleri kapatılabilmektedir. Bunun için "USK Yap" ve "İE Kapat" sütunları kullanılmalıdır. Ancak herhangi bir stok koduna ait üretim sonu kaydının bu ekrandan yapılabilmesi için; stok planlama kayıtları ekranında ilgili stoka ait "Planlama-2" sekmesinde "Üretim sonu kaydı yeri" olarak UAK seçiminin yapılması gerekmektedir.
