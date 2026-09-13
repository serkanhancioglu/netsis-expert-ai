---
title: "Netsis İstatistiksel Proses Kontrol"
page_id: "66237142"
product: "netsis-3-enterprise"
depth: 2
is_section: true
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis İstatistiksel Proses Kontrol"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis İstatistiksel Proses Kontrol"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTAzNjQyYTNkLWM2MDgtNDdjMS05MWE0LWI2YzdmZThhZTc5NSZsaW5rPTAwNGU1NzgwLTQzMjItNDg1Ny1iYTNhLTZmYmIzMGNhYTJiMyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=03642a3d-c608-47c1-91a4-b6c7fe8ae795&link=004e5780-4322-4857-ba3a-6fbb30caa2b3&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-istatistiksel-proses-kontrol_80089253_66237142.html"
source_version: "2022-11-02T15:51:25.593+03:00"
source_bytes: 4158617
fetched_at: "2026-09-13T04:24:53+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis İstatistiksel Proses Kontrol

Netsis İstatistiksel Proses Kontrol ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

> [!TIP]
> İlgili özelliğin anlatımını içeren webinar kaydına ulaşmak için [tıklayınız.](https://register.gotowebinar.com/recording/5328699947232595467)

Günümüzün hızlı ve değişkenliği yüksek üretim şartlarında süreçlerin kontrol altında olduğundan emin olmak her zamankinden daha önemli olmuştur. Şirketlerin verimliliği, müşteri memnuniyeti ve fire oranları doğrudan süreçler üzerindeki kontrolle ilişkilidir. Standart kalite kontrol uygulamaları hataları oluştuktan sonra yakalayıp elemeye yönelikken, istatistiksel proses kontrol süreçleri henüz hatalar oluşmadan anomalileri tespit edip kontrol altına almaya ve dolayısıyla mali kayıpları ve verimsizlikleri daha oluşmadan engelleyebilmeye imkan yaratmaktadır. Bu noktada Logo Netsis'in kullanıcılarına sunduğu "İstatistiksel Proses Kontrol" uygulaması; görsel kontrol grafikleri, kolay uyarlanabilir altyapısı ve özelleştirilebilir parametreleriyle kullanıcılarına süreçlerini kontrol altına alma imkanı sağlamaktadır. Kritik süreçlerinin sağlıklı şekilde yürüdüğünü sürekli olarak takip etmek isteyen kullanıcılar için tasarlanmış olan "İstatistiksel Proses Kontrol" uygulaması; Netsis 3 Enterprise ve Netsis Wings Enterprise çözümleriyle kullanılabilmektedir.

#### Kontrol Grafiği Parametreleri

İstatistiksel proses kontrol uygulamasına ait ekranların tümü kalite kontrol modülünün altında bulunmaktadır. Uygulamaya ait parametre ekranı da kalite kontrol parametreleri içinde olup ulaşmak için Lojistik-Satış-Kalite Kontrol-Kayıt-Kalite Kontrol Parametreleri yolu izlenmelidir. (Bkz. Ekran Görüntüsü 1)

![](../../_assets/5f858caf1a7669038eab.png)**Ekran** **Görüntüsü** **1**

Kalite kontrol parametreleri ekranının "Kontrol Grafikleri" sekmesi, istatistiksel proses kontrol uygulamasına ait parametrelerin ve kuralların belirlenebileceği yerdir. Bu sekmedeki ilk parametre olan "Proses Kontrol dışına çıktığında Otomatik Olarak Bakım Talebi Açılsın" parametresi (Bkz. Ekran Görüntüsü 2), makine bakım modülüyle bağlantılı olarak çalışmaktadır. Bu parametre işaretlenirse ilgili proses kontrol dışına çıktığı an, makine bakım modülünde yapılmış olan tanımlara göre ilgili makine ya da kaynağa ait bakım talebi otomatik olarak açılacaktır. Bu işlemin doğru şekilde gerçekleşebilmesi içinse makine bakım modülünde en az 1 adet talimat şablonu tanımlanmış ve eşleştirilmiş olmalıdır. Tanımlı bakım talimat şablonunun birden fazla olması durumunda ise tanımlı ilk talimat şablonuna ait bakım talebi açılacaktır.

![](../../_assets/6ac41e4392f40afff6d3.png)**Ekran** **Görüntüsü** **2**

Kontrol grafikleri sekmesinde bulunan ikinci parametre ise "Kontrol Grafiği Gösterim Tarihi Limiti'dir. İstatistiksel proses kontrol uygulamasında istenen süreçler kontrol grafikleriyle izlenebilmektedir. Dolayısıyla grafiklere yansıtılacak verilerin hangi tarihten itibaren alınacağı da bu tarih limiti parametresiyle ayarlanmalıdır. Gün, hafta ya da ay bazında verilebilecek tarih limiti ile içinde bulunulan günden ne kadar geriye gidilip grafik verisi alınmaya başlanacağı belirtilmektedir. Örneğin bu limit "1 hafta" olarak belirlenirse son 1 haftaya ait veriler ile bir kontrol grafiği oluşturulacaktır.

Kontrol grafikleri sekmesinde bulunan "Kontrol Grafiği Kuralları" alanı ise, proseslerin hangi durumlarda kontrol dışına çıkmış sayılacağını belirlemek için kullanılmaktadır. Bu alanda 8 kural bulunmaktadır ve bu kurallar literatürde "Nelson Rules" olarak adlandırılmaktadır. Sistemdeki kurallar literatüre bağlı kalınarak desteklenmiştir. Kontrol grafiği kuralları alanında bulunan 8 kuraldan en az 1 seçim yapılması zorunlu olmak üzere istenilen şekilde seçim yapılabilmektedir.

Kontrol Grafiği Kuralları alanındaki kurallara ait detaylı açıklamalar aşağıda sıralanmıştır:

-
  - Bu alandaki ilk kural olan "Alt veya Üst Kontrol Limitlerinin Dışında Bir veya Daha Fazla Nokta Olması" kuralı seçilirse, ilgili süreçte kontrol limitlerinin altına ya da üstüne tek bir noktanın bile düşmesiyle proses kontrol dışına çıkmış sayılacaktır.
  - İkinci kural olan "Ardışık ve Aynı Yöndeki Üç Noktadan İkisinin Uyarı Limitlerinin Dışında Olması" seçilirse, grafik üzerinde arka arkaya gelen 3 değerden ikisi uyarı limitlerinin üstüne ya da altına düştüğünde proses kontrol dışına çıkmış sayılacaktır.
  - Üçüncü kural olan "Ardışık ve Aynı Yöndeki Beş Noktadan Dördünün Bir Sigmadan (***NOT***: *Kalite kontrol sistemleri sigma hesaplamalarıyla çalışmaktadır. Bu sistemlerde 1 sigma, 1* *standart sapmaya karşılık gelmektedir. Kontrol grafiklerinde sürekli olarak grafik verilerinin* *standart sapmaları hesaplanmakta ve bu değer 1 sigma olarak kullanılmaktadır.*) Grafik verilerinin 1 sigma Fazla Sapması" seçilirse, grafik üzerinde arka arkaya gelen her 5 noktaya bakılacak ve 4 noktanın 1 sigma kadar yukarı ya da aşağı yönde sapması durumunda proses kontrol dışına çıkmış sayılacaktır.
  - Dördüncü kural olan "Ardışık Sekiz Noktanın Ortalamanın Üstünde veya Altında Bulunması" seçilirse, grafik üzerinde arka arkaya gelen her 8 noktaya bakılacak ve bu noktalar ortalama değerle karşılaştırılacaktır. Arka arkaya gelen 8 nokta birden ortalamanın üstüne ya da altına düşerse proses kontrol dışına çıkmış sayılacaktır.
  - Beşinci kural olan "Ardışık Altı Noktanın Sürekli Artış ya da Azalış Göstermesi" seçilirse, arka arkaya gelen her 6 noktaya bakılacak ve trend takibi yapılacaktır. Arka arkaya gelen 6 nokta birden azalış ya da artış trendinde olursa proses kontrol dışına çıkmış sayılacaktır.
  - Altıncı kural olan "Ardışık On Beş Noktanın Ortalamanın Altında veya Üstünde Bir Sigmadan Az Sapması" seçilirse, arka arkaya gelen her 15 noktaya bakılacak ve ortalama ile kıyaslama yapılacaktır. Bu arka arkaya gelen 15 noktanın birden ortalama değerin altında ya da üstünde 1 sigmadan az sapması halinde ise proses kontrol dışına çıkmış sayılacaktır.
  - Yedinci kural olan "Ardışık On Dört Noktanın Dalgalı Hareket Göstermesi" seçilirse, arka arkaya gelen her 14 noktaya bakılacak ve trend takibi yapılacaktır. Eğer noktalar ortalamanın bir altına bir üstüne düşerek dalgalanma trendi gösterirse proses kontrol dışına çıkmış sayılacaktır.
  - Sekizinci ve son kural olan "Ardışık Sekiz Noktanın Bir Sigmadan Fazla Sapması" seçilirse, arka arkaya gelen her 8 noktaya bakılacak ve bu 8 noktanın birden ortalamaya göre sapmaları değerlendirilecektir. Bu sapmaların aşağı ya da yukarı yönde ve 1 sigmadan fazla olması durumunda proses kontrol dışına çıkmış sayılacaktır.

İstatistiksel proses kontrol uygulamasının çalışabilmesi için yukarıda bahsedilen 8 kuraldan en az birinin seçilmesi zorunludur. Ancak bunun dışında kuralların kullanımı tamamen kullanıcının çalışma şekline bağlıdır. Bu kurallar istenilen şekilde ve istenilen sayıda seçilebilmektedir.

#### Proses Kontrol Tanımları Ekranı

İstatistiksel proses kontrol uygulaması doğrudan kalite kontrol modülünden beslenmektedir. Kontrol grafiği çizilecek ölçümler, kalite kontrol modülünde tanımlanmış kalite grup tanımları içinden seçilmektedir. Bu noktada kalite kontrol modülünde tanımlanmış ölçüm gruplarından hangilerinin istatistiksel proses kontrol uygulamasıyla takip edileceğinin de sisteme en baştan tanımlanabilmesi mümkündür. Bu işlemin yapılacağı ekran ise Lojistik-Satış-Kalite Kontrol-Kayıt- Proses Kontrol Tanımları yolu izlenerek ulaşılan proses kontrol tanımları ekranıdır. (Bkz. Ekran Görüntüsü 3)

![](../../_assets/6ab517b831f7b21a1e49.png)**Ekran** **Görüntüsü** **3**

İlgili ekrandaki "Tanım Tipi" alanında istasyon, makine, kaynak ve genel seçenekleri bulunmaktadır. Seçilen tanım tipine göre istasyon kodu, makine kodu ya da kaynak kodu alanları aktifleşecektir. Sistem genelinde takibi yapılacak "Genel" tanım tipi seçilmesi durumunda ise bu kod alanı pasif olarak gelecektir.

Grup kodu alanı, seçilen tanım tipi ve kodu için hangi kalite ölçüm grubuna ait istatistiksel proses kontrolü yapılacağını belirtmekte kullanılır. Ekran Görüntüsü 3'teki örnekten, "KES1" istasyonunda "GORSEL_KONTROL" adlı kalite kontrol ölçüm grubunun uygulandığı ve bu ölçüm sonuçlarının da istatistiksel proses kontrol uygulaması ile takip edileceği anlaşılmaktadır. Bu şekilde bir tanımın

yapılması sonrasında ilgili tanım ve koda ait 3. bölümde detayları anlatılan şekilde bir proses kontrol

girişi yapılmak istendiğinde, kalite kontrol ölçüm grup kodu otomatik olarak getirilecektir.

Yine Ekran Görüntüsü 3'te mor daire içinde gösterilen "Proses Kontrol Ölçümleri Otomatik Getirilsin" parametresi seçildiğinde, ekran görüntüsünde kırmızı kutucuk içine alınmış tüm alanlar aktif hale gelecektir. Herhangi bir ölçüm grubuna ait yapılacak kontrol sıklıkları baştan belliyse ve 3. bölümde detayları anlatılan proses kontrol girişi ekranına bu kontrollerin otomatik gelmesi isteniyorsa "Proses Kontrol Ölçümleri Otomatik Getirilsin" parametresi işaretlenmelidir. Bu durumda hangi tarihten itibaren bu ölçümlere başlanacağı ve ilgili ölçümlerin ne sıklıkla tekrarlanacağını belirtmek için sırasıyla "Ölçüm Baş. Tar." ve "Ölçüm Sıklığı" alanları kullanılmalıdır. Ölçüm başlangıç tarihi alanına tarih ve saat cinsinden giriş yapılmalıdır. Ölçüm sıklığı alanı için ise birim üretim miktarı, saniye, dakika, saat, gün, hafta ve ay seçenekleri mevcuttur. Ekran Görüntüsü 3'teki örnekte her 25 birimlik üretimde kontrol gerçekleştirileceği ve bu kontrole ilişkin kontrol değeri girileceği anlaşılmaktadır. Burada yapılan "birim üretim" bilgisi ise üretim akış kayıtlarından alınmaktadır.

#### Proses Kontrol Girişi Ekranı

İstatistiksel proses kontrol uygulamasından beklenen kontrol grafiklerinin çizilebilmesi için ihtiyaç duyulan nokta değerlerinin girişi 2 şekilde yapılabilmektedir. İlk yöntem Lojistik-Satış-Kalite Kontrol-Kayıt-Proses Kontrol Girişi yolu izlenerek ulaşılan proses kontrol girişi ekranını kullanmaktır. (Bkz. Ekran Görüntüsü 4)

![](../../_assets/e08872f39c90fb05b673.png)**Ekran** **Görüntüsü** **4**

Proses kontrol girişi ekranından yapılacak ölçüm değeri girişlerine göre kontrol grafikleri oluşturulacaktır. Proses kontrol tanımları ekranından sıklığı belirli kontroller için kayıt yapıldıysa (Bkz. Ekran Görüntüsü 5), yapılan bu tanımlara göre ölçüm bekleyen kayıtlar proses kontrol girişi ekranına otomatik olarak gelecektir (Bkz. Ekran Görüntüsü 6). Sıklığı belli olmayıp yalnızca "Grup Kodu" tanımı yapılmış istasyon, makine ya da kaynaklar proses kontrol girişi ekranından seçildiğinde ise tanımlanan bu grup kodu otomatik olarak ekrana getirilecektir.

![](../../_assets/0e7817400cd8a1771756.png)**Ekran** **Görüntüsü** **5**

![](../../_assets/f9b186ccd3429a67bf96.png)**Ekran** **Görüntüsü** **6**

Proses kontrol girişi ekranının kullanılması için herhangi bir proses kontrol tanımı yapılmış olması zorunlu değildir. Hiçbir ön tanım yapmadan, proses kontrol girişi ekranı kullanılarak ölçüm kayıtları doğrudan oluşturulabilir. Bunun için ekranın tanım tipi alanındaki istasyon, makine, kaynak ya da genel seçeneklerinden biri seçilip ardından bu seçime ait kod bilgisi ("Genel" seçimi hariç) girilmelidir. Bu işlemin ardından sıradaki "Proses Kontrol No" otomatik olarak dolacaktır, bu alan istenirse manuel olarak değiştirilebilir. Ardından ölçüm sonucu kaydı yapılmak istenen tarih ve saat bilgisi kaydedilmelidir. "Grup Kodu" alanı rehberden seçim yapılarak doldurulmalıdır. "Personel Kodu" alanı zorunlu bir alan olmayıp isteğe bağlı olarak kullanılabilir. "Açıklama" alanı da benzer şekilde zorunlu bir alan değildir.

Bu tanımların ardından yapılan grup kodu kaydına ait ölçüm listesi, proses kontrol girişi ekranın alt kısmına grid görüntüsünde getirilecektir. Bu gridden seçilecek satırlar ekranın üst kısmına getirilecek ve buraya ölçüm değeri ve ölçüm açıklaması girilmesine izin verilecektir. İstenirse "Ölçüm Değeri" ve "Ölçüm Açıklama" alanları grid üzerinde de doldurulup kaydedilebilmektedir.

Proses kontrol girişi ekranına ilgili bir ölçüm için en az 2 değer girildikten sonra, kontrol grafikleri çizilebilecektir. Ekran Görüntüsü 7'de mor kutucuk içinde gösterilen butona tıklanarak kontrol grafiği alanı açılıp kapatılabilmektedir. Kontrol grafiklerine, ölçüm değeri girilen noktaların hangilerinin yansıtılacağı 1. bölümde detayları anlatılan "Kontrol Grafiği Gösterim Tarihi Limiti" ile ilişkilidir. Dolayısıyla bu parametre kontrol edilerek grafikler izlenmelidir.

Proses kontrol girişi ekranının grid bölümünde yer alan her bir satır altında ilgili kalite ölçüm grubuna ait alt satırlar yer alabilmektedir. Bu alt satırların her biri gruba ait farklı ölçümleri içermektedir. 2'den fazla ölçüm değeri girilmiş her alt satır için kontrol grafiği çizilebilmektedir. Hangi ölçüme ait kontrol grafiği görüntülenmek isteniyorsa, o alt satır çift tıklanarak seçilmelidir. Grafiği çizili verilerin detaylarını kontrol etmek için Ekran Görüntüsü 7'de kırmızı ile işaretlenmiş alana bakılabilir. Ayrıca kontrol grafiğinin hemen üstünde yer alan sekmeler içindeki "Grafik Verisi" alanında da ilgili grafiğe ait veriler tablo formatında görüntülenebilmektedir. Bu sekmede sağ tık menüsü bulunmaktadır ve tabloyu Excel'e gönderme seçeneği mevcuttur. Ayrıca grafik verisi sekmesinde satırların önündeki seçimler kaldırılarak yapılan yeni seçimlere göre grafikler eş zamanlı olarak güncellenebilmektedir.

![](../../_assets/1d4da0f4a8cf6d50f787.png)**Ekran** **Görüntüsü** **7**

Proses kontrol girişi ekranının grid alanında sağ tık menüsü bulunmaktadır. (Bkz. Ekran Görüntüsü 8) Menü üzerinden gruplama seçimi yapıldığında grid üzerinde gruplama alanı oluşacak ve istenen kolonların alana sürüklenerek gruplanması mümkün olacaktır. Menüdeki "Gönder" seçeneği ile gridin Excel dosyasına kopyalanması sağlanmaktadır. "Ölçüm Bilgisi Olan Kayıtlar", "Ölçüm Bilgisi Olmayan Kayıtlar" ve "Tüm Bekleyen Kayıtlar" seçenekleri ise yapılan seçimlere göre grid üzerinde filtreleme yapılmasını sağlamaktadır.

![](../../_assets/1251412ef8c72fab3c8f.png)**Ekran** **Görüntüsü** **8**

![](../../_assets/455e470245d716205b9b.png)

Kontrol grafiklerinin çizilebilmesi için ihtiyaç duyulan nokta değerlerinin girişi için kullanılabilecek ikinci yöntem ise Üretim Akış Kaydı ekranından giriş yapmaktır. Üretim akış kaydı ekranında proses kontrol girişi butonunu kullanarak istasyon, makine, kaynak ve genel seçimlerinden birini yapıp kısa yoldan proses kontrol girişi ekranına ulaşılabilmektedir. (Bkz. Ekran Görüntüsü 9)

**Ekran** **Görüntüsü** **9**

Bu anlatılanlara ek olarak operasyonel bazda ölçüm girişleri de üretim akış kaydı ekranı üzerinden yapılabilmektedir. Bunun için ekrandaki ölçüm bilgisi butonu kullanılmalı ve "Operasyon Ölçümleri" seçeneğine tıklanmalıdır. (Bkz. Ekran Görüntüsü 10) Operasyon ölçümleri seçiminin aktif olarak

gelebilmesi için ilgili stoka ait operasyon eşleştirmesinin "Stok-Grup Eşleştirme" ekranında tanımlı olması ve "Departman Tipi'nin "Üretim" olması gerekmektedir.

![](../../_assets/dc1132c2da83be63b93e.png)**Ekran** **Görüntüsü** **10**

Bu yolla operasyon ölçüm bilgileri girilmek için ilgili seçenek tıklandığında sayfadaki "Operasyon Ölçümleri" sekmesi kullanılabilir olacaktır ve operasyon ölçümlerine ait kontrol grafiği bu sekmede görüntülenebilecektir. (Bkz. Ekran Görüntüsü 11) Yine tıpkı proses kontrol girişi ekranında olduğu gibi seçimi yapılmış ölçüm koduna ait grafik çift tıklanarak çizilecektir.

![](../../_assets/b0b192d557a532e9f74d.png)**Ekran** **Görüntüsü** **11**

#### Kontrol Grafiği Türleri

İstatistiksel proses kontrol uygulamasında kullanılan kontrol grafikleri her türlü veri için çizilebilmektedir. Örneğin grafiği çizilecek veriler sayısal olabilir ya da olmayabilir. Ayrıca kontrol grafiği

çizilecek veri setinin büyüklüğü de değişken olacaktır. Konu bu yönüyle ele alındığında farklı tip veri setleri için farklı tip grafiklerin çizilmesi gerekecektir. Logo Netsis İstatistiksel Proses Kontrol uygulamasında da farklı veri setleri ve tipleri için literatüre uygun olarak farklı tür grafik destekleri sağlanmıştır. Uygulama içinde desteklenen tüm kontrol grafiği tipleri aşağıda açıklanmıştır.

#### X-Bar Chart

İstatistiksel proses kontrol uygulamasında sayısal değerli veri setleri için kullanılan grafik tipi X-Bar grafikleridir. Genel anlamda veri setlerinin büyüklüğüne göre X-Bar grafikleri ile birlikte R-Chart, S- Chart ya da I-Chart tiplerinde grafikler de çizilmektedir.

X-Bar grafikleri veri setlerindeki her bir noktanın tekil değerlerinin ve tüm veri setine ait ortalamanın izlenebildiği grafiklerdir. Böylece her bir tekil noktanın ortalamanın ne kadar uzağında olduğu görsel olarak takip edilebilmektedir. Örneğin Ekran Görüntüsü 12'deki X-Bar grafiğinde, veri setinde bulunan 6 noktanın her birine ait değerler noktalarla belirtilmiş şekilde zaman eğrisi üzerinde görülmektedir. Ayrıca bu 6 noktanın ortalaması olan 185,2 değeri de yeşil bir doğru olarak grafiğin ortasında gösterilmiştir.

İstatistiksel proses kontrol uygulamasında çizilen X-bar tipindeki grafiklere genel anlamda bakıldığında ise grafiklerde üst kontrol limiti, alt kontrol limiti, üst uyarı limiti ve alt uyarı limiti seviyelerinin de bulunduğu görülecektir. Bu seviyelerin hepsi literatürdeki kalite kontrol mantığına göre belirlenmiş ve sigma büyüklüğü ele alınarak hesaplanmıştır.

![](../../_assets/85f0a83ccb2f4f6049f8.png)

X-bar grafiklerindeki değerlerin ortalaması grafiğin ortasında yeşil bir doğru olarak gösterilirken grafiği oluşturan verilere ait standart sapma da hesaplanmaktadır. Ardından bu standart sapma değerine göre kontrol limitleri belirlenmektedir. Grafik verilerine göre hesaplanan standart sapma değeri 1 sigma değerine karşılık gelmektedir. X-bar grafiklerinin üst ve alt kontrol limitleri ise 6 sigma değerine göre oluşturulmaktadır. Buna göre grafiğin ortalama değerinin üzerine 3 sigma değeri eklenerek üst kontrol limiti hesaplanırken, ortalama değerden 3 sigma değeri çıkarılarak da alt kontrol limiti hesaplanmaktadır. Aynı mantıkla grafik verisi ortalamasının 2 sigma uzaklığında da üst uyarı ve alt uyarı limitleri konumlandırılmaktadır.

**Ekran** **Görüntüsü** **12**

#### I-Chart

İstatistiksel proses kontrol grafiklerinde X-Bar ile birlikte kullanılan grafik tiplerinden biri I-Chart'lardır. Grafiği çizilen veri için her bir ölçüm bilgisinin altında ilgili veriye ait yalnızca 1 ölçüm değeri olması durumunda I-Chart çizilmektedir.

Erkan Görüntüsü 13'teki örnekte 6 tane ölçüm bilgisi bulunmaktadır. Ölçümlerin her birinin altında 2 farklı alt ölçüm yer almaktadır. Örnekteki ilk ölçüm bilgisi kırmızı kutucuk içinde gösterilmiş ve alt ölçümlerden I grafiği çizilen veri (TRIM_OLCUM) mor kutucuk içinde gösterilmiştir. Burada her bir ölçüm satırına ait alt ölçümlerin sayısı 1 olduğu için I-Chart kullanılmıştır. TRIM-OLCUM kontrolü için her bir satırda yer alan ölçüm değerinin 1'den fazla olması durumunda ise farklı grafik tiplerine ihtiyaç duyulacaktır.

I-Chart tipindeki grafiklerde ölçümler arasındaki fark gösterilmektedir. Yani her bir ölçüm sonucu, bir sonraki ölçüm sonucuyla karşılaştırılır. Bir sonraki ölçüm sonucundan bir önceki ölçüm sonucu çıkarılarak ölçümler arasındaki fark bulunur ve bu değer grafiğe yansıtılır. 13. Ekran görüntüsündeki örnekte ilk TRIM_OLCUM değeri 4 ve ikinci ölçüm değeri 2'dir. Dolayısıyla I grafiğinde gösterilen ilk nokta değeri 2'dir (4-2=2).

![](../../_assets/7f3bd591c19f130de0b4.png)**Ekran** **Görüntüsü** **13**

#### R-Chart

İstatistiksel proses kontrol grafiklerinde X-Bar ile birlikte kullanılan grafik tiplerinden bir diğeri R- Chart'lardır. Grafiği çizilen veri için her bir ölçüm bilgisinin altında, ilgili veriye ait ölçüm değeri sayısı 1'den büyük ve 10'dan küçük ya da eşitse R-Chart çizilmektedir (1\<n&#8804; 10=""\>14. Ekran Görüntüsü'ndeki örnekte 4 ölçüm bulunmakta ve her ölçümün altında EN_OLCUM ve TRIM_OLCUM olmak üzere 2 farklı alt ölçüm bulunmaktadır. Bu alt ölçümlerden EN-OLCUM kontrolüne ait ise 2'şer adet ölçüm sonucu girilmiştir. Buradaki ölçüm sayısı (2), 1\<n&#8804; 10="" ait="" de="" grafi=""\>R grafiklerinde her bir proses kontrol numarası altında aynı ölçüm tipi için girilen ölçüm sonuçlarının tamamına bakılır. Bu sonuçların maksimum ve minimum değerleri dikkate alınıp maksimum ve minimum değerler arasındaki fark R grafiğine o veriye ait tek bir nokta olarak yansıtılır. 14. ve 15. Ekran Görüntüleri'ndeki örnekte 120 ve 123 olarak girilen EN_OLCUM sonuçlarına ait R grafiğine yansıtılan ilk nokta değeri 3 olmuştur (123-120=3). Eğer bu ölçüm altında 3 kontrol sonucu olsaydı ve bu 3 değer 115, 120 ve 123 olsaydı R grafiğindeki ilk nokta değeri 8 olacaktı. (Maksimum ve minimum değerler olan 115 ve 123'ün farklı 8'dir.)

Bir ölçüm tipine ait birden çok ölçüm sonucu bulunan durumlarda X-Bar grafiğinde de bu ölçümlerin ortalaması tek nokta olarak yer almaktadır. 15. Ekran Görüntüsü'ndeki örnekte ölçüm sonuçları 120 ve 123 olarak girilmiş 2 adet EN_OLCUM verisi bulunmaktadır. Bu verilere karşılık gelen X-Bar grafiğinde ise 121,5 (ortalama değer) değeri taşıyan tek bir nokta görülmektedir.

![](../../_assets/1e41a5b28cbadc555612.png)![](../../_assets/df3e4df8211947a896ed.png)**Ekran** **Görüntüsü** **14** **Ekran** **Görüntüsü** **15**

#### S-Chart

İstatistiksel proses kontrol grafiklerinde X-Bar ile birlikte kullanılan grafik tiplerinden sonuncusu S- Chart'lardır. Grafiği çizilen veri için her bir ölçüm bilgisinin altında ilgili veriye ait 10'dan fazla ölçüm değeri olması durumunda S-Chart çizilmektedir (n\>10).

16. Ekran Görüntüsü'ndeki örnekte 2 ölçüm bilgisi bulunmakta ve her ölçümün altında EN_OLCUM ve TRIM_OLCUM olmak üzere 2 farklı ölçüm kodu bulunmaktadır. Bu alt ölçümlerden EN-OLCUM kontrolüne ait ise 11'er adet ölçüm sonucu girilmiştir. Buradaki ölçüm sayısı (11), n\>10 kuralına uyduğu için de ilgili veriye ait S grafiği çizilmiştir.

S grafiklerinde her bir proses kontrol numarası altında aynı ölçüm tipi için girilen ölçüm sonuçlarının tamamına bakılır. Bu sonuçlara ait standart sapma değeri hesaplanır ve hesaplanan bu değer S grafiğine ilgili veriye ait tek bir nokta olarak yansıtılır. 16. Ekran Görüntüsü'nde ilk ölçüm bilgisi altında yer alan 11 adet EN_OLCUM veri değeri kırmızı kutucuk içinde gösterilmiştir. Her proses kontrol numarası altında EN_OLCUM verisine ait 11 adet ölçüm bulunduğundan kontrol grafiği S grafiğine dönüşmüştür. Kırmızı kutucuk içinde görülen 11 veriye ait standart sapma değeri 4,2 olduğu için S grafiğinin ilk noktasına bu değer yansıtılmıştır.

![](../../_assets/cd11fa874d01e117b11c.png)**Ekran** **Görüntüsü** **16**

Bir ölçüm tipine ait birden çok ölçüm sonucu bulunan durumlarda X-Bar grafiğinde de bu ölçümlerin ortalaması tek nokta olarak yer almaktadır. Örneğin 16. Ekran Görüntüsü'ndeki 11 ölçüm sonucuna ait ortalama değer hesaplanarak bu verilere karşılık gelen X-Bar grafiğinde bu ortalama değer tek bir nokta olarak görülmektedir.

İstatistiksel proses kontrol grafiklerinin tipleri belirlenirken ölçüm bilgisi altında maksimum sayıda kontrol sonucu girişi olan satırlar dikkate alınır. Örneğin tek kontrol sonucu için I-Chart ve 3 kontrol sonucu için R-Chart çizilmesi gerekmektedir. Toplam 8 ölçüm bilgisi olan bir giriş olduğunu ve bu girişlerden üçünün 3'er kontrol sonuç değeri, beşinin ise 1'er kontrol sonuç değeri bulundurduğunu varsayarsak maksimum kontrol sonucu sayısı 3 olduğundan, yalnızca bu 3 satır dikkate alınıp 3 noktalı bir R-Chart çizilecek diğer 5 satır ihmal edilecektir.

#### NP-Chart

Kalite kontrol ölçüm sonuçları her zaman sayısal olmak zorunda değildir. "Var-Yok", "OK-NOK" gibi sözel ölçüm sonucu olan kontroller de mevcuttur. Bu şekilde sözel ölçüm sonucu olan kontroller için çizilen grafiklerden biri NP-Chart'tır. (Bkz. Ekran Görüntüsü 17)

![](../../_assets/4130ebeffe4a9c1d9663.png)**Ekran** **Görüntüsü** **17**

NP grafiklerinde hata sayıları gösterilmektedir ve grafiklerin NP tipinde olması için kontrol sonucunun sözel olmasının yanı sıra her ölçüm bilgisinin altındaki kontrol sonucu sayısının da eşit olması gerekmektedir. 17. Ekran Görüntüsü'ndeki örnekte 4 ölçüm vardır ve her ölçümün altında 1 adet kontrol sonucu bulunmaktadır, bu yüzden NP grafiği çizilmiştir. Örnekteki kontrol sonuçlarından yalnızca kırmızı kutucuk içinde gösterilen 1 adeti "defect'tir". Dolayısıyla NP grafiğine bu hataya ait ölçüm sonucu 1 olarak yansıtılmıştır.

#### P-Chart

Logo Netsis İstatistiksel Proses Kontrol desteği kapsamında çizilen son tip kontrol grafiği P-Chart'tır. P grafikleri de sözel ölçüm sonucu olan kontroller için çizilmektedir. NP grafiklerinden farklı olarak her ölçüm altındaki kontrol adedinin birbirinden farklı olduğu durumlarda çizilir ve yine hata (defect) sayısı üzerinden ilerlemektedir. Ancak burada NP grafiğinden farklı olarak, hatalar adet cinsinden değil hata yüzdesi olarak gösterilmektedir. (Bkz. Ekran Görüntüsü 18)

18. Ekran Görüntüsü'ndeki örnekte kırmızı kutucuk içinde gösterilen 2 kontrol değerinden biri hata olduğu için hata oranı %50'dir ve grafiğe de bu şekilde yansıtılmıştır.

![](../../_assets/b81e821345c63ec5c467.png)**Ekran** **Görüntüsü** **18**

#### Kontrol Grafiği İzleme Ekranı

İstatistiksel proses kontrol uygulamasında çizilen grafiklerin tamamının sürekli olarak izlenebileceği ekran kontrol grafiği izleme ekranıdır. İlgili ekrana ulaşmak için Lojistik-Satış-Kalite Kontrol-Kayıt-Kontrol Grafiği İzleme yolu takip edilmelidir. (Bkz. Ekran Görüntüsü 19)

![](../../_assets/e1186b7bbebce38bd92b.png)**Ekran** **Görüntüsü** **19**

Bu ekran üzerindeki "Tanım Tipi" alanından, modülde yapılan istasyon, makine, kaynak ya da genel tanımlarından grafiği izlenmek istenen seçilmeli ve ardından yapılan seçime göre güncellenecek rehberden tanım tipinin kodu seçilmedir. (Bkz. Ekran Görüntüsü 20) Yapılan bu seçimlere göre "Ölçü Kodu" alanı rehberi de güncellenecektir. Bu alandan da istenen şekilde seçim yapılabilmektedir. Kontrol grafiği izleme ekranı "Güncelleme" alanından yapılacak seçime göre sürekli olarak güncellenecektir. Bu alanda saniye, dakika ve saat cinsinden seçim yapılabilmektedir. Yapılan tanıma göre ekranın altındaki zamanlayıcı doğrunun uzunluğu değişecek ve bir sonraki güncellemeye ne kadar kaldığı görsel olarak takip edilebilecektir.

![](../../_assets/651ca1f9f914dc197596.png)**Ekran** **Görüntüsü** **20**

İstatistiksel proses kontrol desteği kapsamında çizilen grafiklerin üzerinde gösterilen "Proses Kontrol Altında" ya da "Proses Kontrol Altında Değil" uyarıları, kalite kontrol parametreleri altındaki kontrol grafiği kurallarına göre belirlenmektedir. Bu kurallarda yapılacak değişikliklere göre verilecek uyarılar da değişecektir.

#### Kontrol Grafiği İzleme Eklentisi

Kontrol grafiklerinin sürekli olarak izlenebildiği son ekran kontrol grafiği izleme eklentisidir. Bu widget "Eklenti Ekle" komutu kullanılarak ve "Kalite kontrol için kontrol grafiği izleme" seçimi yapılıp kaydedilerek kullanılabilmektedir. Eklenti ayarlarına tıklayarak izlenmek istenen prosese ait parametre bilgileri kaydedildikten (Bkz. Ekran Görüntüsü 21) sonra, Logo Netsis masaüstündeki "Kontrol Grafiği İzleme" eklentisine ait butona tıklandığında kaydedilen eklenti parametrelerine uygun kontrol grafiği izlenebilecektir. (Bkz. Ekran Görüntüsü 22)

![](../../_assets/676302cc943898f3c663.png)**Ekran** **Görüntüsü** **21**

Eklenti üzerindeki veriler güncelleme süresi seçimine uygun şekilde otomatik olarak güncellenecek ve güncel veriler izlenebilecektir.

![](../../_assets/a2b02d63e67269bf3e79.png)**Ekran** **Görüntüsü** **22**

#### Raporlar

Sistemde istatistiksel proses kontrol uygulaması kapsamında desteklenen bir rapor bulunmaktadır. Lojistik-Satış-Kalite Kontrol-Raporlar-Proses Kontrol Raporu yolu izlenerek ulaşılabilecek raporda, uygulama üzerinde proses kontrole ilişkin yapılmış tüm kayıt ve tanımlar tablo formatında görüntülenebilmektedir. (Bkz. Ekran Görüntüsü 23)

![](../../_assets/b8ea59f4f57832b33a8f.png)**Ekran** **Görüntüsü** **23**
