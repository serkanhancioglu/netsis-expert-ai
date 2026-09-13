---
title: "Netsis Fabrika Son Durum İzleme"
page_id: "66237150"
product: "netsis-3-enterprise"
depth: 2
is_section: true
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis Fabrika Son Durum İzleme"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis Fabrika Son Durum İzleme"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTRiMzg4YjkwLTg2NTMtNDIyYi04MzNlLWJmMDVmY2FiMmRjYSZsaW5rPTNjODZmOTJjLWJhMmUtNGM1NC04NDBkLTRhMmMyNDliMDUwNiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=4b388b90-8653-422b-833e-bf05fcab2dca&link=3c86f92c-ba2e-4c54-840d-4a2c249b0506&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-fabrika-son-durum-izleme_66237151_66237150.html"
source_version: "2022-11-02T15:56:49.510+03:00"
source_bytes: 3939417
fetched_at: "2026-09-13T04:24:58+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis Fabrika Son Durum İzleme

Netsis Fabrika Son Durum İzleme ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

> [!NOTE]
> İlgili özelliğin anlatımını içeren webinar kaydına ulaşmak için [tıklayınız.](https://register.gotowebinar.com/recording/3432174324255827457)

Her iş kolunda olduğu gibi üretim sektöründe de yönetilmesi gereken birçok süreç vardır. Son derece karmaşık ve dinamik olan üretim süreçlerini doğru yönetebilmek ise zor olduğu kadar şirketlerin verimliliği ve başarısı için önemlidir. Üretim sahasında bulunan makinelerin ve istasyonların durumlarını anlık olarak görebilmek, üretimi devam eden ve üretime girecek olan siparişlerle ilgili kritik kararları doğru verebilmek, varsa verimsiz kullanılan makineleri tespit edebilmek, kalite standartlarında iyileştirme gereken noktaları belirleyebilmek gibi birçok konu bakımından büyük önem taşımaktadır. Bu noktada Logo Netsis'in kullanıcılarına sunduğu "Fabrika Son Durumu" ekranı, üretim sahası yöneticileri için bir nevi "büyük resim" görevi görmektedir. Böylece üretimin detaylarında boğulup, asıl ilgilenilmesi gereken kritik noktaların gözden kaçması engellenmektedir. Tüm üretim yöneticileri için sağ kol görevi görecek "Fabrika Son Durumu" ekranı; Netsis 3 Standard, Netsis Wings, Netsis 3 Enterprise ve Netsis Wings Enterprise çözümleriyle kullanılabilmektedir.

#### Toplam Ekipman Etkinliği (OEE)

Fabrika son durumu ekranına ulaşmak için Üretim-Üretim Akış Kontrol-İşlemler yolu izlenmelidir. (Bkz. Ekran Görüntüsü 1)

![](../../_assets/04dfe4f379cbdf050364.png)**Ekran** **Görüntüsü** **1**

Fabrika son durumu ekranında kullanıcının seçimine göre, sistemde kayıtlı makineler, istasyonlar veya tüm fabrika için toplam ekipman etkinliği değerleri (OEE – Overall Equipment Effectiveness) gösterilmektedir. Toplam ekipman etkinliği değerinin hesaplanabilmesi için 3 farklı veri gerekmektedir; kullanılabilirlik (AVA – Availability), performans (PER – Performance) ve kalite (QUA – Quality). Bu 3 verinin hesaplanıp çarpılması yoluyla ise toplam ekipman etkinliği değeri bulunmaktadır. (Bkz. Ekran Görüntüsü 2)

OEE = AVA × PER × QUA

![](../../_assets/a7b01086db649247725e.png)![](../../_assets/57b9ba9c3628a8ef9a66.png)**Ekran** **Görüntüsü** **2**

Toplam ekipman etkinliği değerinin 3 farklı bileşen kullanılarak hesaplanması, üretime ait kayıpların oluşma sebeplerinin detaylarıyla ortaya konulabilmesi bakımından önemlidir. Toplam ekipman etkinliğini oluşturan her bir bileşen, üretimde yaşanması muhtemel farklı bir problemi işaret etmekte ve üretim yöneticilerine hangi noktalara odaklanılması gerektiği konusunda yol göstermektedir. OEE'yi oluşturan ilk bileşen olan kullanılabilirlik, her bir makinenin vardiya sürelerini dikkate alarak hesaplanmaktadır. Genel anlamıyla her bir makinenin vardiya boyunca çalıştığı gerçek sürenin, planlanan çalışma süresine oranlanmasıyla bulunmaktadır. Bu bakımdan kullanılabilirlik değeri, makinelerin duruşlarından (arıza, kalıp değişimi vb.) kaynaklanan kayıpları işaret etmektedir.

AVA = Planlanan Üretim Süresi − (Toplam Duruş Süresi + Toplam Hazırlık Süresi + Toplam Transfer Süresi)

#### Planlanan Üretim Süresi

OEE'yi oluşturan ikinci unsur olan performans ise, planlanan üretim zamanı içinde gerçekleşen üretim adedinin, üretilmesi mümkün olan maksimum üretim adedine oranlanmasıyla hesaplanmaktadır. Bu anlamda OEE'nin içinde barındırdığı performans bileşeninin, en temelde hız kayıplarına işaret ettiğini söylemek mümkündür.

PER = ∑(Birim Ürün İçin Üretim Süresi × Birim Ürünün Üretim Miktarı) Planlanan Üretim Süresi − (Toplam Duruş Süresi + Toplam Hazırlık Süresi + Toplam Transfer Süresi)

OEE'nin son bileşeni olan kalite ise, üretilen toplam ürün miktarı içinde kalite standartları bakımından "geçer" ürün miktarının payıdır. Bu hesaplama yöntemi değerlendirildiğinde, kalitesizlikten kaynaklanan kayıpların OEE'nin içindeki kalite bileşeniyle temsil edildiği söylenebilmektedir.

QUA = ∑(Üretim Miktarı−Fire Miktarı) ∑ (Üretim Miktarı)

Tüm bu bilgiler göz önünde bulundurulduğunda, toplam ekipman etkinliği (OEE) değerinin üretim tesislerinin sağlık göstergesi olduğunu söylemek yanlış olmayacaktır. Fabrika son durum ekranı üzerinden ulaşılabilen verilerin doğru şekilde yorumlanmasıyla, üretim tesislerindeki sorunların doğru tespiti mümkün olmaktadır.

#### Fabrika Son Durumu Ekranı

Fabrika son durumu ekranının kullanımı oldukça basittir. Tamamen görsellik ön planda olacak şekilde tasarlanmış olan bu ekran üzerinde görünüm değişikliklerinin yapılması da mümkün ve son derece kolaydır.

Fabrika Son Durum ekranının kullanımına ait bilinmesi gereken en temel şey, bu ekran üzerinde hesaplanan tüm verilerin üretim akış kayıtları kullanılarak elde edildiğidir. Yani ekranda görülen toplam ekipman etkinliği, kullanılabilirlik, performans ve kalite değerlerinin tümü sistemde kayıtlı üretim akış kayıtları taranarak hesaplanmaktadır. Ekranın en üst kısmında bulunan başlangıç ve bitiş zamanları tarih ve saat cinsinden manuel olarak istenildiği gibi seçilebilmektedir. Manuel olarak giriş yapıldıktan sonra ekrandaki "Rapor" butonuna tıklanarak, girilen zaman aralığının veriye yansıması sağlanmaktadır. Ekranda gösterilecek değerler ise bu alanlarda yapılan yapılan seçime uyan üretim akış kayıtları kullanılarak hesaplanacaktır. (Bkz. Ekran Görüntüsü 3)

![](../../_assets/dcd1cf59182aefbcc04a.png)**Ekran** **Görüntüsü** **3**

Ancak burada manuel bir seçim yapılmasa da ekran açıldığında kullanıcı karşısına varsayılan değerler getirilecektir. Bitiş zamanı için varsayılan değer, içinde bulunulan günden bir sonraki gün saat 00:00:00'dır. Varsayılan başlangıç zamanı ise "Üretim Akış Parametreleri" ekranının "Fabrika Son Durumu" alanında bulunan, "OEE Hesabı için Tarih Limiti" parametresinden gelmektedir. Varsayılan bitiş zamanından, OEE hesabı için tarih limiti parametresindeki kadar gün çıkarılarak başlangıç zamanı bulunmaktadır. (Bkz. Ekran Görüntüsü 4)

![](../../_assets/cf590ddc6f550e82d1e6.png)**Ekran** **Görüntüsü** **4**

Yine 4. Ekran görüntüsünde görülen "Grafik Güncelleme Sıklığı" parametresi de fabrika son durumu ekranının çalışma prensibiyle ilişkilidir. Fabrika son durumu ekranında gösterilen verilerin hangi sıklıkla güncellenmesi isteniyorsa, grafik güncelleme sıklığı parametresinden buna uygun seçim yapılabilmektedir.

Dokümanın birinci bölümünde bahsedilen, ekran görünümünün makine, istasyon ya da fabrika türünden ayarlanması ise yine ekran üzerinden basitçe yapılabilmektedir. 3. Ekran görüntüsünde yeşil kutucuk içinde gösterilen ayar menüsünden makine görünümü, istasyon görünümü ya da fabrika görünümü seçeneklerinden biri seçildiğinde, ekrandaki veriler otomatik olarak bu seçime göre güncellenecektir. Görünüm değişikliği, kullanılan üretim akış kayıtları bakımından ise bir değişikliği sebep olmamaktadır. Görünüm değiştirilse de ekranda girilmiş olan başlangıç ve bitiş zamanları arasındaki üretim akış kayıtları dikkate alınacak ve hesaplamalar buna göre yapılacaktır.

![](../../_assets/3f609b4427816c584658.png)**Ekran** **Görüntüsü** **5**

Fabrika son durumu ekranının bir başka özelliği ise ekranda arama yapılabilmesidir. 5. ekran görüntüsünde kırmızı kutucuk içinde gösterilen arama çubuğu kullanılarak, ekrandaki makineler ya da istasyonlar içinde arama yapılabilmektedir. Ayrıca ekranda OEE'leri listelenen makine ya da istasyonların mevcut durumlarına göre filtrelenebilmeleri de mümkündür. Bunun için arama çubuğunun yanındaki filtre sahasından seçim yapılarak, isteğe göre yalnızca boşta, arızalı ya da çalışan

makine/istasyonların gösterilmesi sağlanmaktadır. (Bkz. Ekran Görüntüsü 5) Fabrika son durumu ekranında bu alan varsayılan olarak "Tümünü Göster" seçimiyle gelecektir. Makinelerin yukarıda bahsedilen olası tüm mevcut durumları, ekranın sağ üst köşesinde sembolik olarak gösterilmektedir. (Bkz. Ekran Görüntüsü 6)

![](../../_assets/b6b025a0e8c19d7418f6.png) **Ekran** **Görüntüsü** **6**

Her bir makineye ait mevcut durum ise, ilgili makineye ait OEE kutucuğunun sol alt köşesinde vurgulanmaktadır. (Bkz. Ekran Görüntüsü 7)

![](../../_assets/a294a0558bab3f8efa31.png)![](../../_assets/8cad01bc2854f19ccb26.png)**Ekran** **Görüntüsü** **7**

Makinelerin mevcut durumları yine üretim akış kayıtlarından gelmektedir. İlgili makineye ait en son üretim akış kaydının aktivite tipi, o makinenin mevcut fabrika son durumunu belirleyecektir. Örneğin son üretim akış kaydı aktivite tipi "Durma/Arıza" olan bir makine, fabrika son durumu ekranında "Arızalı" olarak gösterilecektir.

Fabrika son durumu ekranından kontrol edilebilen bir diğer özellik ise ekran üzerindeki makine/istasyonların sıralamasıdır. 8. ekran görüntüsünde yeşil kutucuk içinde gösterilen sıralama alanından, ekrandaki değerlerin neye göre sıralanacağı kontrol edilebilmektedir. İstasyon kodu, makine kodu, makine durumu ya da OEE değerlerine göre otomatik sıralama yapılabileceği gibi kullanıcının sıralamaya tamamen kendisinin karar vermesi de mümkündür. "Kullanıcı Tanımlı" bu sıralama için fabrika son durumu ekranı üzerinde her bir makineye ait olan kutucuklar farenin sol tuşu ile tutulup sürükle-bırak yöntemiyle istenilen sıralamaya getirilmedir. İstenilen sıralamaya getirilen fabrika son durumu ekranı kapatıldığında, en son yapılan manuel sıralama saklanacaktır. Ekran tekrar açıldığında ise saklanan bu sıralama "Kullanıcı Tanımlı" seçimi yapıldığında otomatik olarak getirilecektir.

![](../../_assets/365565be7db7b41903e1.png)**Ekran** **Görüntüsü** **8**

Fabrika son durumu ekranında bulunan son buton ise ekranın sağ üst köşesindeki mavi butondur. (Bkz. Ekran Görüntüsü 9) Ekranda manuel olarak yapılan sıralama ekran kapatılırken otomatik olarak saklanıp, "Kullanıcı Tanımlı" seçeneğiyle getirilebileceği gibi, mavi butona tıklandığında açılan menüde bulunan "Görünümü Kaydet" seçeneğiyle de "Kullanıcı Tanımlı" seçimine kaydedilebilmektedir.

![](../../_assets/bdd61cfbab8c9d0f8408.png)**Ekran** **Görüntüsü** **9**

Yine sıralama anlamında ekranda yapılan tüm değişikliklerin iptal edilebilmesi ve varsayılan haline döndürülebilmesi için "Görünümü Sıfırla" seçeneği kullanılabilmektedir. Son olarak ekranda görüntülenen tüm OEE değerlerinin hesaplanması sırasında kullanılan verilerin detaylarına "Grafik Verisi" seçeneğinden ulaşmak mümkündür. Fabrika son durumu ekranında fabrika, istasyon ve makine bazında görüntülenebilen OEE değeri ve bu değeri oluşturan tüm detaylar grafik verisi seçeneği tıklandığında görüntülenebilmektedir. (Bkz. Ekran Görüntüsü 10)

![](../../_assets/c220068a5dbc7abdfdb3.png)**Ekran** **Görüntüsü** **10**

Grafik verisi ekranı üzerinde filtreleme yapmak mümkündür. Filtreleme yapılmak istenen kolonlar sol fare tuşu ile tutulup sürükle-bırak yöntemiyle 10. ekran görüntüsünde yeşil kutucuk ile gösterilen alana sürüklenebilir ve istenen filtrelemeler uygulanabilir.

Tüm bunların dışında, fabrika son durum ekranı açıldığında varsayılan olarak kullanıcı karşısına gelen "Grafiksel Gösterim"in haricinde, 11. ekran görüntüsünde yeşil kutucuklar içinde gösterilen "Gantt Gösterimi" ve "Detay Bilgi" görünümleri de bulunmaktadır. İlgili sekmeler tıklanarak ekrandaki görünüm değiştirilebilmektedir.

![](../../_assets/2433ef5bcba65a02dbe9.png)**Ekran** **Görüntüsü** **11**

![](../../_assets/b7a69c5cec7f99bf269c.png)**Ekran** **Görüntüsü** **12**

Gantt gösterimi, her bir makinede üretilen iş emirlerini üretim zamanları bazında gösterirken (Bkz. Ekran Görüntüsü 12) detay bilgi sekmesinde fabrika son durumu ekranının çalıştırıldığı zaman aralığındaki tüm iş emirleri ve bu iş emirlerine ait aktivite tipi, belge tipi, üretim miktarı, personel gibi tüm detaylar tablo formunda gösterilmektedir. (Bkz. Ekran Görüntüsü 13)

![](../../_assets/1d0952fdaf20bb9c2d70.png)**Ekran** **Görüntüsü** **13**

Son olarak, detay bilgi ekranında da filtreleme yapılabilmektedir. Ekrandaki kolonların başlık satırları üzerine gelindiğinde çıkan filtre ikonuna tıklayarak ilgili kolona istenen kısıtların verilmesi mümkündür. Ayrıca kolonlar, farenin sol tuşuyla tutulup sürükle-bırak yöntemiyle istenildiği gibi sıralanabilmektedir.

#### Fabrika Son Durumu Ekranı Veri Kaynakları

Fabrika son durumu ekranındaki veriler, kullanıcının sisteminde bulunan birkaç farklı kaynaktan gelebilmektedir. Bu, kullanıcının kullandığı modüllerle ilişkilidir. Örneğin üretime ait planlanan zamanlar OEE hesabında kullanılmaktadır ve bu bilginin hesaplanabilmesi için vardiya planlarına ihtiyaç vardır. Kullanıcının sisteminde tanımlı vardiya planlarının kaynakları ise çizelgeleme modülü kullanıp kullanmamasına göre değişiklik göstermektedir.

Bu noktada, fabrika son durumu ekranının açıldığı ilk anda, çizelgeleme modülünün kullanılıp kullanılmadığı kontrol edilmektedir. Eğer çizelgeleme modülü kullanılıyorsa, vardiya planları çizelgeleme modülünün "Fabrika Çalışma Takvimi'nden alınmaktadır. (Bkz. Ekran Görüntüsü 14)

![](../../_assets/4ae0aa96728d7ada565b.png)**Ekran** **Görüntüsü** **14**

Eğer çizelgeleme modülü kullanılmıyorsa, MRP modülünün altında bulunan fabrika çalışma takvimi ve istasyon çalışma takvimi verileri kullanılmaktadır. Fabrika çalışma takviminin kullanıldığı senaryoda, MRP parametreleri altındaki MRPII sekmesinde vardiya sürelerinin de tanımlarının yapılmış olması ve "Vardiyada Çalışan Kişi Sayısı" bilgilerinin doldurulmuş olması gerekmektedir. (Bkz. Ekran Görüntüsü 15)

![](../../_assets/cbc9f32d07c08af3e788.png)**Ekran** **Görüntüsü** **15**

İstasyon çalışma takviminin kullanıldığı senaryoda ise benzer şekilde, istasyon çalışma takvimi tanımlarına ek olarak, iş istasyonu tanımlama ekranındaki vardiya süresi tanımlarının da yapılmış olması gerekmektedir. (Bkz. Ekran Görüntüsü 16)

![](../../_assets/6b932e24848e1971ee63.png)**Ekran** **Görüntüsü** **16**

Benzer şekilde ürünlerin birim zamanları için de öncellikle çizelgeleme parametresinin açık olup olmadığı kontrol edilmektedir. Eğer çizelgeleme modülü kullanılıyorsa, ürünlerin birim zamanları çizelgeleme modülünün altında bulunan eşleştirme ekranlarından getirilmektedir. (Bkz. Ekran Görüntüsü 17)

![](../../_assets/6b6e15956c5fba519db5.png)**Ekran** **Görüntüsü** **17**

Eğer çizelgeleme modülü kullanılmıyorsa, ikinci olarak kullanıcının kapasite planlama uygulaması kullanıp kullanmadığı kontrol edilmektedir. Bunun için MRP parametrelerinin altında bulunan kapasite planlama parametreleri içindeki "Planlama Verisi" alanı kontrol edilmektedir. Bu kontrol sonucunda kapasite planlama uygulamasının kullanıldığı tespit edilirse, birim zamanlar MRP modülünün altındaki rota tanımlarından getirilmektedir. (Bkz. Ekran Görüntüsü 18)

![](../../_assets/92c7c307c23d8046982e.png)**Ekran** **Görüntüsü** **18**

Ancak eğer kapasite planlama uygulamasının da kullanılmadığı tespit edilirse, üçüncü ve son kontrol reçete kayıtlarından yapılmaktadır. Bu kontrol sonucunda ise reçetede tanımlı operasyonların birim süreleri kullanılmakta ve fabrika son durumu ekranındaki hesaplamalar yapılmaktadır. (Bkz. Ekran Görüntüsü 19)

![](../../_assets/05e14260c224afa4061f.png)**Ekran** **Görüntüsü** **19**
