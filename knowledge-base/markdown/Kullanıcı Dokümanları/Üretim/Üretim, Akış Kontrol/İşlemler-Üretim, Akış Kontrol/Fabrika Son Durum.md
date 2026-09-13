---
title: "Fabrika Son Durum"
page_id: "50665435"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Üretim"
  - "Üretim, Akış Kontrol"
  - "İşlemler/Üretim, Akış Kontrol"
  - "Fabrika Son Durum"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Üretim / Üretim, Akış Kontrol / İşlemler/Üretim, Akış Kontrol / Fabrika Son Durum"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTcyODU3Y2ZlLTgyMmEtNDUzMC1iNDliLTRmYzM3OThiYTZmYiZsaW5rPTdhOTZlYWEzLWU3MDYtNDk4Mi1hNGY0LTIxMDEyZDA2M2Y1OSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=72857cfe-822a-4530-b49b-4fc3798ba6fb&link=7a96eaa3-e706-4982-a4f4-21012d063f59&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "fabrika-son-durum_50665459_50665435.html"
source_version: "2022-11-08T09:44:34.423+03:00"
source_bytes: 6279536
fetched_at: "2026-09-13T04:20:48+00:00"
generator: "netsis-scraper 1.0.0"
---
# Fabrika Son Durum

Fabrika Son Durum, Üretim Bölümü'nde, "İşlemler/Üretim-Akış Kontrol" menüsünün altında yer alır. Her iş kolunda olduğu gibi üretim sektöründe de yönetilmesi gereken birçok süreç vardır. Son derece karmaşık ve dinamik olan üretim süreçlerini doğru yönetmek ise zor olduğu kadar şirketlerin verimliliği ve başarısı için önemlidir. Üretim sahasında bulunan makinelerin ve istasyonların durumlarını anlık olarak görmek, üretimi devam eden ve üretime girecek olan siparişlerle ilgili kritik kararları doğru vermek, varsa verimsiz kullanılan makineleri tespit etmek, kalite standartlarında iyileştirme gereken noktaları belirlemek gibi birçok konu bakımından büyük önem taşır. Bu noktada Logo Netsis'in kullanıcılarına sunduğu "Fabrika Son Durumu" ekranı, üretim sahası yöneticileri için bir nevi "büyük resim" görevi görür. Böylece, üretimin detaylarında boğulup, asıl ilgilenilmesi gereken kritik noktaların gözden kaçması engellenir.

**1. Toplam Ekipman Etkinliği (OEE)**

![](../../../../_assets/5f0bf545b8fc757f2081.png) ![](../../../../_assets/b12d7f0fa9b58e56bba2.png)

**Ekran Görüntüsü** **1**

Fabrika son durumu ekranında kullanıcının seçimine göre, sistemde kayıtlı makineler, istasyonlar veya tüm fabrika için toplam ekipman etkinliği değerleri (OEE – Overall Equipment Effectiveness) gösterilir. Toplam ekipman etkinliği değerinin hesaplanması için üç farklı veri gerekir. Bunlar; Kullanılabilirlik (AVA – Availability), Performans (PER – Performance) ve Kalite (QUA – Quality) olarak sıralanır. Bu üç verinin hesaplanıp çarpılması yoluyla Toplam Ekipman Etkinliği değeri bulunur. (Bkz. Ekran Görüntüsü 2)

**OEE = AVA × PER × QUA**
![](../../../../_assets/b12d7f0fa9b58e56bba2.png)

![](../../../../_assets/9f6b48f7787e2a3df612.png)

**Ekran Görüntüsü** **2**

Toplam Ekipman Etkinliği değerinin üç farklı bileşen kullanılarak hesaplanması, üretime ait kayıpların oluşma sebeplerinin detaylarıyla ortaya konulması bakımından önemlidir. Toplam ekipman etkinliğini oluşturan her bir bileşen, üretimde yaşanması muhtemel farklı bir problemi işaret eder ve üretim yöneticilerine hangi noktalara odaklanılması gerektiği konusunda yol gösterir. OEE'yi oluşturan ilk bileşen olan kullanılabilirlik, her bir makinenin vardiya sürelerini dikkate alarak hesaplanır. Genel anlamıyla her bir makinenin vardiya boyunca çalıştığı gerçek sürenin, planlanan çalışma süresine oranlanmasıyla bulunur. Bu bakımdan kullanılabilirlik değeri, makinelerin duruşlarından - arıza, kalıp değişimi gibi - kaynaklanan kayıpları işaret eder.

Planlanan Üretim Süresi - (Toplam Duruş Süresi+Toplam Hazırlık Süresi+Toplam Transfer Süresi)

AVA = Planlanan Üretim Süresi

OEE'yi oluşturan ikinci unsur olan performans ise, planlanan üretim zamanı içinde gerçekleşen üretim adedinin, üretilmesi mümkün olan maksimum üretim adedine oranlanmasıyla hesaplanır. Bu anlamda OEE'nin içinde barındırdığı performans bileşeninin, en temelde hız kayıplarına işaret ettiğini söylemek mümkündür.

∑(Birim Ürün İçin Üretim Süresi X Birim Ürünün Üretim Miktarı

PER = Planlanan Üretim Süresi - (Toplam Duruş Süresi+Toplam Hazırlık Süresi+Toplam Transfer Süresi)

OEE'nin son bileşeni olan kalite ise, üretilen toplam ürün miktarı içinde kalite standartları bakımından "geçer" ürün miktarının payıdır. Bu hesaplama yöntemi değerlendirildiğinde, kalitesizlikten kaynaklanan kayıpların OEE'nin içindeki kalite bileşeniyle temsil edildiği söylenebilir.

∑(Üretim Miktarı-Fire Miktarı)

QUA = ∑(Üretim Miktarı)

Tüm bu bilgiler göz önünde bulundurulduğunda, toplam ekipman etkinliği (OEE) değerinin üretim tesislerinin sağlık göstergesi olduğu söylenebilir. Fabrika Son Durum ekranı üzerinden ulaşılan verilerin doğru şekilde yorumlanmasıyla, üretim tesislerindeki sorunların doğru tespiti mümkündür.

**2- Fabrika Son Durumu Ekranı**

Fabrika son durumu ekranının kullanımı oldukça basittir. Tamamen görsellik ön planda olacak şekilde tasarlanan bu ekran üzerinde görünüm değişikliklerinin yapılması son derece kolaydır. Ekran kullanımına ait bilinmesi gereken en temel şey, bu ekran üzerinde hesaplanan tüm verilerin üretim akış kayıtları kullanılarak elde edildiğidir. Yani, ekranda görülen toplam ekipman etkinliği, kullanılabilirlik, performans ve kalite değerlerinin tümü sistemde kayıtlı üretim akış kayıtları taranarak hesaplanır.
Ekranın en üst kısmında bulunan Başlangıç ve Bitiş Zamanları tarih ve saat cinsinden manuel (elle) olarak seçilebilir. Manuel (elle) olarak giriş yapıldıktan sonra ekrandaki "Rapor" butonuna tıklanarak, girilen zaman aralığının veriye yansıması sağlanır. Ekranda gösterilecek değerler ise, bu alanlarda yapılan seçime uyan üretim akış kayıtları kullanılarak hesaplanır. (Bkz. Ekran Görüntüsü 3)

![](../../../../_assets/d8b94a3ff1c78b64e66b.png)

**Ekran Görüntüsü** **3**

Burada manuel (elle) bir seçim yapılmasa da, ekran açıldığında kullanıcı karşısına varsayılan değerler getirilir. Bitiş Zamanı için varsayılan değer, içinde bulunulan günden bir sonraki gün saat 00:00:00'dır. Varsayılan Başlangıç Zamanı ise "Üretim Akış Parametreleri" ekranının "Fabrika Son Durumu" alanında bulunan, "OEE Hesabı için Tarih Limiti" parametresinden gelir. Varsayılan Bitiş Zamanından, OEE hesabı için tarih limiti parametresinde belirtilen kadar gün çıkarılarak Başlangıç Zamanı bulunur. (Bkz. Ekran Görüntüsü 4)

![](../../../../_assets/3143d9a10e80ee69250d.png)

**Ekran Görüntüsü** **4**

Yine 4. ekran görüntüsünde görülen "Grafik Güncelleme Sıklığı" parametresi de Fabrika Son Durumu ekranının çalışma prensibiyle ilişkilidir. Fabrika Son Durumu ekranında gösterilen verilerin hangi sıklıkla güncellenmesi isteniyorsa, grafik güncelleme sıklığı parametresinde buna uygun seçim yapılır. Birinci bölümde bahsedilen ekran görünümünün makine, istasyon ya da fabrika türünden ayarlanması ise yine ekran üzerinden basit bir şekilde yapılır. 3. ekran görüntüsünde yeşil kutucuk içinde gösterilen ayar menüsünden Makine Görünümü, İstasyon Görünümü ya da Fabrika Görünümü seçeneklerinden biri seçildiğinde, ekrandaki veriler otomatik olarak bu seçime göre güncellenir. Görünüm değişikliği, kullanılan üretim akış kayıtları bakımından bir değişikliğe sebep olmaz. Görünüm değiştirilse de ekranda girilen Başlangıç ve Bitiş Zamanları arasındaki üretim akış kayıtları dikkate alınır ve hesaplamalar buna göre yapılır.

![](../../../../_assets/9846d549d6962c6dcc3c.png)

**Ekran Görüntüsü** **5**

Fabrika Son Durumu ekranının bir başka özelliği ise ekrandan arama yapılmasıdır. 5. ekran görüntüsünde kırmızı kutucuk içinde gösterilen arama çubuğu kullanılarak, ekrandaki makineler ya da istasyonlar içinde arama yapılabilir. Ayrıca, ekranda OEE'leri listelenen makine ya da istasyonların mevcut durumlarına göre filtrelenmesi de mümkündür. Bunun için, arama çubuğunun yanındaki filtre sahasından seçim yapılarak, isteğe göre yalnızca boşta, arızalı ya da çalışan makine/istasyonların gösterilmesi sağlanır. (Bkz. Ekran Görüntüsü 5)

Fabrika Son Durumu ekranında bu alan varsayılan olarak "Tümünü Göster" seçimiyle gelir. Makinelerin yukarıda bahsedilen olası mevcut durumları, ekranın sağ üst köşesinde sembolik olarak gösterilir. (Bkz. Ekran Görüntüsü 6)
![](../../../../_assets/b12d7f0fa9b58e56bba2.png)

![](../../../../_assets/8abd3bcab33cc1604ff8.png)

**Ekran Görüntüsü** **6**

Her bir makineye ait mevcut durum ise, ilgili makineye ait OEE kutucuğunun sol alt köşesinde gösterilir. (Bkz. Ekran Görüntüsü 7)
![](../../../../_assets/b12d7f0fa9b58e56bba2.png)

![](../../../../_assets/277bf29fbcdd6e91f42b.png)

**Ekran Görüntüsü** **7**

Makinelerin mevcut durumları yine üretim akış kayıtlarından gelir. İlgili makineye ait en son üretim akış kaydının aktivite tipi, o makinenin mevcut fabrika son durumunu belirler.

**Örneğin;**

Son üretim akış kaydı aktivite tipi "Durma/Arıza" olan bir makine, fabrika son durumu ekranında "Arızalı" olarak gösterilir.

Fabrika Son Durumu ekranından kontrol edilen bir diğer özellik ise, ekran üzerindeki makine/istasyonların sıralamasıdır. 8. ekran görüntüsünde yeşil kutucuk içinde gösterilen sıralama alanından, ekrandaki değerlerin neye göre sıralanacağı kontrol edilir. İstasyon Kodu, Makine Kodu, Makine Durumu ya da OEE değerlerine göre otomatik sıralama yapılacağı gibi kullanıcının sıralamaya tamamen kendisinin karar vermesi de mümkündür. "Kullanıcı Tanımlı" bu sıralama için Fabrika Son Durumu ekranı üzerinde her bir makineye ait olan kutucuklar farenin sol tuşu ile tutulup "Sürükle-Bırak" yöntemiyle istenen sıralamaya getirilmelidir. İstenen sıralamaya getirilen Fabrika Son Durumu ekranı kapatıldığında, en son yapılan manuel (elle) sıralama saklanır. Ekran tekrar açıldığında ise saklanan bu sıralama "Kullanıcı Tanımlı" seçimi yapıldığında otomatik olarak ekrana getirilir.

![](../../../../_assets/09f5c84de5ed04da877b.png)

**Ekran Görüntüsü** **8**

Fabrika Son Durumu ekranında bulunan son buton ise ekranın sağ üst köşesindeki mavi butondur (Bkz. Ekran Görüntüsü 9). Ekranda manuel (elle) olarak yapılan sıralama, ekran kapatılırken otomatik olarak saklanıp, "Kullanıcı Tanımlı" seçeneğiyle getirileceği gibi, mavi butona tıklandığında açılan menüde bulunan "Görünümü Kaydet" seçeneğiyle de "Kullanıcı Tanımlı" seçimine kaydedilebilir.

![](../../../../_assets/f9ea0db41147a84b51f2.png)

**Ekran Görüntüsü** **9**

Yine sıralama anlamında ekranda yapılan tüm değişikliklerin iptal edilmesi ve varsayılan haline döndürülmesi için "Görünümü Sıfırla" seçeneği kullanılabilir. Son olarak ekranda görüntülenen tüm OEE değerlerinin hesaplanması sırasında kullanılan verilerin detaylarına "Grafik Verisi" seçeneğinden ulaşmak mümkündür. Fabrika Son Durumu ekranında fabrika, istasyon ve makine bazında görüntülenen OEE değeri ve bu değeri oluşturan tüm detaylar grafik verisi seçeneğine tıklandığında görüntülenir. (Bkz. Ekran Görüntüsü 10)
![](../../../../_assets/b12d7f0fa9b58e56bba2.png)

![](../../../../_assets/c34e014435572dbd0928.png)

**Ekran Görüntüsü** **10**

Grafik verisi ekranı üzerinde filtreleme yapılması mümkündür. Filtreleme yapılması istenen kolonlar sol fare tuşu ile tutulup "Sürükle-Bırak" yöntemiyle 10. ekran görüntüsünde yeşil kutucuk ile gösterilen alana sürüklenebilir ve istenen filtreleme uygulanabilir.
Tüm bunların dışında, Fabrika Son Durum ekranı açıldığında varsayılan olarak kullanıcı karşısına gelen "Grafiksel Gösterim"in haricinde, 11. ekran görüntüsünde yeşil kutucuklar içinde gösterilen "Gantt Gösterimi" ve "Detay Bilgi" görünümleri de bulunur. İlgili sekmelere tıklanarak ekrandaki görünüm değiştirilebilir.
![](../../../../_assets/b12d7f0fa9b58e56bba2.png)

![](../../../../_assets/b11e26517813c1c85f0b.png)

**Ekran Görüntüsü** **11**

![](../../../../_assets/b88bd9918022385adc3f.png)

**Ekran Görüntüsü** **12**

"Gantt Gösterimi"sekmesi, her bir makinede üretilen iş emirlerini üretim zamanları bazında gösterirken (Bkz. Ekran Görüntüsü 12) "Detay Bilgi" sekmesinde, "Fabrika Son Durumu" ekranının çalıştırıldığı zaman aralığındaki tüm iş emirleri ve bu iş emirlerine ait Aktivite Tipi, Belge Tipi, Üretim Miktarı, Personel gibi tüm detaylar tablo formunda gösterilir. (Bkz. Ekran Görüntüsü 13)
![](../../../../_assets/b12d7f0fa9b58e56bba2.png)

![](../../../../_assets/31557e755e4f1ffba733.png)

**Ekran Görüntüsü** **1****3**

Son olarak, "Detay Bilgi" sekmesinden de filtreleme yapılabilir. Ekrandaki kolonların başlık satırlarının üzerine gelindiğinde çıkan filtre ikonuna tıklayarak ilgili kolona istenen kısıtların verilmesi mümkündür. Ayrıca kolonlar, farenin sol tuşuyla tutulup "Sürükle-Bırak" yöntemiyle istendiği gibi sıralanabilir.

**3- Fabrika Son Durumu Ekranı Veri Kaynakları**

Fabrika Son Durumu ekranındaki veriler, kullanıcının sisteminde bulunan birkaç farklı kaynaktan gelebilir. Bu, kullanıcının kullandığı modüllerle ilişkilidir.

**Örneğin;**

Üretime ait planlanan zamanlar OEE hesabında kullanılır ve bu bilginin hesaplanması için vardiya planlarına ihtiyaç vardır. Kullanıcının sisteminde tanımlı vardiya planlarının kaynakları ise Çizelgeleme modülünün kullanıp kullanılmamasına göre değişiklik gösterir.

Fabrika Son Durumu ekranının açıldığı ilk anda, çizelgeleme modülünün kullanılıp kullanılmadığı kontrol edilir. Çizelgeleme modülü kullanılıyorsa, vardiya planları Çizelgeleme modülünün "Fabrika Çalışma Takviminden" alınır. (Bkz. Ekran Görüntüsü 14)

![](../../../../_assets/a55a7d0feedfccc5ee78.png)

**Ekran Görüntüsü** **14**

Çizelgeleme modülü kullanılmıyorsa, MRP modülünün altında bulunan Fabrika Çalışma Takvimi ve İstasyon Çalışma Takvimi verileri kullanılır. Fabrika çalışma takviminin kullanıldığı senaryoda, MRP parametreleri altındaki "MRP II" sekmesinde vardiya sürelerinin tanımlarının yapılması ve "Vardiyada Çalışan Kişi Sayısı" bilgilerinin doldurulması gerekir. (Bkz. Ekran Görüntüsü 15)

![](../../../../_assets/837368d8764c45fe17a9.png) ![](../../../../_assets/b12d7f0fa9b58e56bba2.png)

**Ekran Görüntüsü** **1****5**

İstasyon çalışma takviminin kullanıldığı senaryoda ise benzer şekilde, istasyon çalışma takvimi tanımlarına ek olarak, İş İstasyonu Tanımlama ekranındaki vardiya süresi tanımlarının da yapılması gerekir. (Bkz. Ekran Görüntüsü 16)

![](../../../../_assets/f5b9c4bfdb7e03d2ec8a.png) ![](../../../../_assets/f13fbd27ada00aa46241.png)

**Ekran Görün****tüsü** **1****6**

Benzer şekilde ürünlerin birim zamanları için öncellikle çizelgeleme parametresinin açık olup olmadığı kontrol edilir. Eğer Çizelgeleme modülü kullanılıyorsa, ürünlerin birim zamanları Çizelgeleme modülünün altında bulunan eşleştirme ekranlarından getirilir. (Bkz. Ekran Görüntüsü 17)

![](../../../../_assets/f273e6c9d5f60f353e63.png)

**Ekran Görüntüsü** **17**

Çizelgeleme modülü kullanılmıyorsa, ikinci olarak kullanıcının kapasite planlama uygulaması kullanıp kullanmadığı kontrol edilir. Bunun için MRP parametrelerinin altında bulunan kapasite planlama parametreleri içindeki "Planlama Verisi" alanı kontrol edilir. Kontrol sonucunda, kapasite planlama uygulamasının kullanıldığı tespit edilirse, birim zamanlar MRP modülünün altındaki rota tanımlarından getirilir. (Bkz. Ekran Görüntüsü 18)

![](../../../../_assets/df77ec17feb9a49c2083.png)

**Ekran Görüntüsü** **18**

Kapasite planlama uygulamasının da kullanılmadığı tespit edilirse, üçüncü ve son kontrol reçete kayıtlarından yapılır. Kontrol sonucunda ise reçetede tanımlı operasyonların birim süreleri kullanılır ve Fabrika Son Durumu ekranındaki hesaplamalar yapılır (Bkz. Ekran Görüntüsü 19)

![](../../../../_assets/ff820a8f7d805b0073f7.png)

**Ekran Görüntüsü** **19**
