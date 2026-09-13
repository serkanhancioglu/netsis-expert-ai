---
title: "Maliyet Muhasebesi Uyarlama Örneği"
page_id: "147554909"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Maliyet Muhasebesi Uyarlama Örneği"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Maliyet Muhasebesi Uyarlama Örneği"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWFlMTFhY2QwLTg2MjEtNGNmNS04NjMwLTk3YTYxZjhhZDYyMiZsaW5rPTdkYTgwZmUxLTk2MDQtNDE5NC05NTllLWVlYTViNDAzNDI4YSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=ae11acd0-8621-4cf5-8630-97a61f8ad622&link=7da80fe1-9604-4194-959e-eea5b403428a&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "maliyet-muhasebesi-uyarlama-ornegi_147554925_147554909.html"
source_version: "2024-08-26T11:23:50.547+03:00"
source_bytes: 673180
fetched_at: "2026-09-13T04:22:44+00:00"
generator: "netsis-scraper 1.0.0"
---
# Maliyet Muhasebesi Uyarlama Örneği

Bu dokümanda maliyet muhasebesi uyarlamasına ait bir örneğe yer verilmiştir. Netsis maliyet muhasebesi modülü Standard, Enterprise ve Wings Enterprise ürünlerimizde opsiyonel olarak kullanılabilmektedir.

Maliyet muhasebesi modülü, stok, üretim, fatura, muhasebe ve entegrasyon modülleri ile entegre, Personel ve Demirbaş ile bağlantılı çalışır.

Maliyet Muhasebesi modülünde kayıt ve işlem yapılabilmesi için stok modülü parametre kayıtlarında maliyet sistemi işaretlenmeli ve sabit kayıtlar ayrı ayrı tanımlanmalı, muhasebe modülünde hesap kodları girilmeli, üretim modülünde üretim reçeteleri girilmelidir.

Sabit Tanımlamalar

1-Stok parametrelerinden "Maliyet Sistemi" parametresi açılır ve çalıştırılmak istenen maliyet tipi seçilir; örneğin aylık ağırlıklı ortalama yöntemi seçilebilir.

2-Reçete tanımı yapılır.

Maliyeti hesaplanacak örnek ürün reçetesi aşağıdaki gibidir, reçetedeki bileşen kullanımları bire bir olarak tanımlanmıştır, yani her ürünün 1 adet üretilmesi için altındaki bileşenden bir adet sarf edilmektedir.
![](../_assets/dd3124764b5f92c97dd6.png)
Yapılan operasyonlara göre iki farklı üretim safhası bulunmaktadır: Preshane ve Montaj

3-Muhasebe hesap planı oluşturulur. Bu aşamada önemli olan nokta, gider hesaplarının üretim safhaları bazında kırılımlı olmasıdır.

Önemli hesap kodları aşağıdaki gibidir:

-
  - 100 : Kasa
  - 102 : Banka
  - 150 : Hammadde alış
  - 151 : Yarı mamul alış
  - 152 : Mamuller
  - 153 : Ticari Mallar
  - 120 : Alıcılar
  - 320 : Satıcılar
  - 600 : Yurtiçi Satış Hesabı
  - 601 : Yurtdışı Satış Hesabı
  - 620 : Satılan malın maliyeti hesabı
  - 710 : Sarfedilen hammadde hesabı
  - 720 : Direkt işçilik giderleri
  - 730 : Genel üretim giderleri
    - Elektrik
    - Yakıt
    - Amortisman
    - Alet-Edevat
    - Ulaşım Giderleri
    - Bakım Onarım
    - Kalite Kontrol
  - 740 : Hizmet üretim maliyeti
  - 750 : Arge Giderleri
  - 760 : Pazarlama – Satış ve Dtığım giderleri
  - 770 : Genel yönetim giderleri
  - 780 : Finansman Giderleri

![](../_assets/668edb5c9240cfbdbf58.png)
Muhasebe hesap planı oluşturulurken sıkça kullanılan iki farklı yaklaşım bulunmaktadır:

-
  - Gider yerine göre gider çeşidi : 710-01-001 01 KESME SAFHASI \\\\ 001 ELEKTRIK
  - Gider çeşidine göre gider yeri : 710-01-001 01 ELEKTRIK \\\\ 001 KESME SAFHASI

Örnek üretim sistemi için muhasebe hesap planı aşağıdaki gibi oluşturulmuştur:

| Hesap Kodu | Hesap Adı | Tür | Grup Kodu | Tip |
| --- | --- | --- | --- | --- |
| 150-001-001 | HAMMADDE1 | M | 15 | AKTİF |
| 150-001-002 | HAMMADDE2 | M | 15 | AKTİF |
| 150-001-003 | HAMMADDE3 | M | 15 | AKTİF |
| 150-001-004 | BOYA | M | 15 | AKTİF |
| 151-001-001 | YARIMAMUL1 | M | 15 | AKTİF |
| 151-001-002 | YARIMAMUL2 | M | 15 | AKTİF |
| 151-001-003 | YARIMAMUL3 | M | 15 | AKTİF |
| 151-001-004 | YARIMAMULLER GECICI YANSITMA HESABI | M | 15 | AKTİF |
| 152-001-001 | MAMUL1 | M | 15 | AKTİF |
| 600-001-001 | PRESHANE YURTICI SATISLAR | M | 60 | GELİR |
| 600-001-002 | MONTAJ YURTICI SATISLAR | M | 60 | GELİR |
| 600-001-003 | YURTICI HAMMADDE SATIŞLARI | M | 60 | GELİR |
| 620-001-001 | PRESHANE- SATILAN MAMUL MALIYETI | M | 62 | GİDER |
| 620-001-002 | MONTAJ- SATILAN MAMUL MALIYETI | M | 62 | GİDER |
| 710-001-001 | PRESHANE HAMMADDE SARFLARI | M | 71 | GİDER |
| 710-001-002 | MONTAJ HAMMADDE SARFLARI | M | 71 | GİDER |
| 710-001-003 | PRESHANE AMBALAJ SARFLARI | M | 71 | GİDER |
| 710-001-004 | MONTAJ AMBALAJ SARFLARI | M | 71 | GİDER |
| 711-001-001 | PRESHANE HAMMADDE SARFLARI | M | 71 | GİDER |
| 711-001-002 | MONTAJ HAMMADDE SARFLARI | M | 71 | GİDER |
| 711-001-003 | PRESHANE AMBALAJ SARFLARI | M | 71 | GİDER |
| 711-001-004 | MONTAJ AMBALAJ SARFLARI | M | 71 | GİDER |
| 720-001-001 | PRESHANE DIREKT ISCILIK GIDERI | M | 72 | GİDER |
| 720-001-002 | MONTAJ DIREKT ISCILIK GIDERLERI | M | 72 | GİDER |
| 721-001-001 | PRESHANE ISCILIK GIDERLERI | M | 72 | GİDER |
| 721-001-002 | MONTAJ ISCILIK GIDERLERI | M | 72 | GİDER |
| 730-001-001 | PRESHANE ELEKTRIK GIDERI | M | 73 | GİDER |
| 730-001-002 | MONTAJ ELEKTRIK GIDERI | M | 73 | GİDER |
| 730-001-003 | PRESHANE YAKIT GIDERI | M | 73 | GİDER |
| 730-001-004 | MONTAJ YAKIT GIDERI | M | 73 | GİDER |
| 730-002-001 | PRESHANE ALET EDEVAT GİDERLERİ | M | 73 | GİDER |
| 730-002-002 | MONTAJ ALET EDEVAT GIDERLERI | M | 73 | GİDER |
| 730-003-001 | PERSONEL ULAŞIM GİDERLERİ | M | 73 | GİDER |
| 730-003-002 | PRESHANE ULAŞIM GİDERLERİ | M | 73 | GİDER |
| 730-003-003 | MONTAJ ULAŞIM GİDERLERİ | M | 73 | GİDER |
| 730-004-001 | PRESHANE AMORTISMAN GIDERLERI | M | 73 | GİDER |
| 730-004-002 | MONTAJ AMORTISMAN GIDERLERI | M | 73 | GİDER |
| 731-001-001 | PRESHANE ELEKTRIK GIDERI | M | 73 | GİDER |
| 731-001-002 | MONTAJ ELEKTRIK GIDERI | M | 73 | GİDER |
| 731-001-003 | PRESHANE YAKIT GIDERI | M | 73 | GİDER |
| 731-001-004 | MONTAJ YAKIT GIDERI | M | 73 | GİDER |
|  |  |  |  |  |
| 731-002-001 | PRESHANE ALET EDEVAT GİDERLERİ | M | 73 | GİDER |
| 731-002-002 | MONTAJ ALET EDEVAT GİDERLERİ | M | 73 | GİDER |
| 731-004-001 | PRESHANE AMORTISMAN GIDERLERI | M | 73 | GİDER |
| 731-004-002 | MONTAJ AMORTISMAN GIDERLERI | M | 73 | GİDER |
| 731-003-002 | PRESHANE ULASIM GIDERLERI | M | 73 | GİDER |
| 731-003-003 | MONTAJ ULASIM GIDERLERI | M | 73 | GİDER |

4-Stok kartları için muhasebe detay kodları tanımlanır. Muhasebe detay kodunda ilgili detay kodu için alış\\satış ve iade hesapları tanımlanmaktadır, tanımlanan muhasebe detay kodu stok kartında seçilmelidir.

![](../_assets/16d347d0c4c43a8bb217.png)

5-Maliyet muhasebesi modülünden "**mamul ana grup kayıtları**" tanımlanır. Mamul ana grup kaydı üretim sahasındaki aşamaları ifade etmektedir, üretim safhası olarak da tanımlanabilir.

Örnek reçete incelendiğinde progresif, boy kesme ve bükme operasyonları preshane istasyonunda yapılırken, braket çakma operasyonu montaj istasyonunda yapılmaktadır. Ayrıca bu örnekte 72\\73 gider hesapları da preshane ve montaj olarak ayrılabilmektedir, daha detaylı şekilde muhasebe hesap planında takip edilememektedir. Bu yüzden üretim safhaları "preshane" ve "montaj" olarak tanımlanmıştır.

![](../_assets/0504e054f097ed6b398a.png)

Mamul ana grubuna ait gider hesapları tanımlanır ve dağıtım anahtarları sekmesinden ilgili giderlerin dağıtım yöntemi seçilir (üretim miktarları oranı, birim katsayılar oranı, hammadde sarfları oranı) Özetle bu ekranda tanımlanan gider hesapları, üretim safhasına ait toplam gider tutarlarının biriktirildiği hesaplardır. Bu hesaplarda biriken bakiyelerin ilgili safhada üretilen ürünlere (ilgili safhadaki mamul grup kodlarına) dağıtılması gerekmektedir.

Muhasebe modülünden **referans kodu** tanımı yapıldıktan sonra, mamul ana grup kaydını bir referans koduyla eşleştirerek gider hesaplarının referans kodu bazında çekilmesi\\gruplanması sağlanabilir.

Maliyet muhasebesi parametreleri ikinci sekmede yer alan "**mamul iadeleri otomatik hesaplansın**" işaretliyse mamul ana grup kodu kayıtlarındaki "**iade işlemde geri dönülecek ay sayısı**" bilgisine göre iade edilen tutarlar hesaplanmaktadır. İade tutarını hesaplarken iade edilen mamulün ne zaman ve hangi maliyetle üretildiği bilinmediğinden, geri dönülecek ay sayısında belirtilen değer kadar geriye gidilerek o tarihteki maliyet üzerinden hesaplama yapılmaktadır. Uyarlama aşamasında mamul ana grup kodu bazında üretilen ürünlerin ortalama iade süresi öğrenilir ve geri dönülecek ay sayısı olarak tanımlanır. İade işleminde geri dönülecek ay sayısı **"En Yakın Ay"** seçeneği işaretli olduğu durumlarda iade maliyetinde ortalama maliyet bulunan ilk değer dikkate alınacaktır. Mamul iadeleri otomatik hesaplansın işaretli değilse iade faturası girilirken "iade maliyet tutarı" sorulur.

Program bu şekilde girilen tutarları dikkate alır, otomatik maliyet tutarı bulmaya çalışmaz.

Dağıtım anahtarları sekmesinde bulunan "**hammadde sarfları ana-grup bazında**" parametresi işaretlenirse ambar çıkış fişiyle mamul ana grubuna hammadde sarfiyatı yapılabilir ve bu sarf edilen toplam tutar mamul ana grubuna bağlı bulunan mamul grup kodlarına dağıtılacaktır. Örneğin üretimde paçal şekilde tüketilen ve reçetelerde bulunmayan boya, gaz, çivi vs. gibi hammaddelerde bu yöntem kullanılabilir.

Mamul ana grup kayıtları TBLMALIANAG tablosunda tutulmaktadır.

6-Maliyet muhasebesi modülünden **mamul grup kodları** tanımlanır.

Mamul grup kodları genelde stok kodu bazında tanımlanır, yani her bir yarı mamul{color} mamul için bir adet mamul grup kodu tanımlanabilir. Genel anlamda birim katsayıların ve mamul grupları için çalışacak muhasebe hesaplarının tanımlandığı bölümdür.

![](../_assets/5914acd7b7b97b3b258e.png)

Mamul grup kodu tanımlanırken ilgili ürünlerin hangi üretim safhasına dahil olduğu "**ana grup kodu**" bölümüne girilmelidir.

Tanımlanan mamul kodu için "**mamul\\yarı mamul\\yan ürün**" tiplerinden biri seçilir.

Eğer tanımlanan mamul grup kodu birden fazla ürünü temsil edecekse ortak bir ölçü birimi seçilmelidir.

Mamul grup kodunun üretim safhası için (mamul ana grup kaydı) dağıtım anahtarı olarak birim katsayılar oranı seçilmiş ise, mamul grup kodu tanımlama ekranında birim katsayılar bölümü aktif hale gelecektir ve tanımlanması gerekir.

![](../_assets/c4361eba252a024981ad.png)

Mamul\\Hammadde hesap kodları sekmesinde mamul grup koduna ait **yarı mamul \\ mamul hesapları (151-152), hammadde\\ambalaj sarf hesapları (710) ve satılan malın maliyeti hesabı (620)** tanımlanmalıdır.

Mamuller için kullanılan grup kodu kayıtlarında yar mamul ve mamul hesaplarının ikisinin de tanımlanması gerekir. Çünkü direkt olarak 150 hesaptan 152 hesaba geçiş olmaz. Muhasebe kurallarına göre öncelikle 150 hesaptan 151 hesaba aktarılmalıdır, daha sonrasında 151'den 152 hesaba geçiş yapmalıdır. O yüzden her türlü yar mamul üretimi olmasa bile maliyet fişinde 151 hesaplar çalışır. Borç çalışan 151 hesabı yarı mamul hesabına denk gelirken, alacak çalışan 151 hesap yarı mamul transfer hesabına denk gelmektedir.

Yansıtma hesapları sekmesinde gider hesaplarına (7_0) karşılık gelen yansıtma hesapları (7_1) seçilir. 7_0 hesaplarda hep borç çalışılır, bu hesapların alacak karşılıkları 7_1 yansıtma hesaplarına yazılır. Böylece herhangi bir anda mizan çekildiğinde 7_0 hesaplardaki gider bakiyesi görülebilir.

7-Üretimde kullanılacak bütün stok kodları için stok kartı – ek bilgiler sekmesindeki **maliyet bilgileri** seçilmelidir. Maliyet bilgileri türü olarak "yarı mamul" veya "mamul" tiplerinden biri seçildiğinde mamul grup kodunun girilmesi zorunludur. Bu şekilde mamul grup koduyla stok kartı eşleştirilmiş olur.

Hammadde ve ambalaj tipli stok kodları için maliyet bilgileri türü olarak "**ilk madde**" veya "**ambalaj**" seçilir ve mamul grup kodu boş bırakılır.

![](../_assets/5deae8662dcaebeaa145.png)

8-Maliyet muhasebesi modülünden "**işlem sırası tanımlama**" yapılır. Mamullerin üretimi sırasında gerçekleştirilen üretim safhaları (mamul ana grup kodları) en baştan en sona doğru sıralanır. Örneğin üretilen ilk yarı mamul birinci işlem sırasında yer alırken, satılacak olan mamulün üretim safhası en sonuncu işlem sırasında yer almalıdır.

![](../_assets/5f6094900470318d60fa.png)

Eğer herhangi bir işlem sırasında\\üretim safhasında yukarıdaki örnekte olduğu gibi birden çok üretim seviyesi varsa (örneğin YM2 altında YM3 üretimi var ve bu iki üretim aynı mamul ana grup koduna denk gelmektedir), seviye sayısını safha adedi bölümüne girmek gerekmektedir.

Maliyet Muhasebesi Çalıştırma Adımları

1-Stok - İşlemler - Maliyet Oluşturma\* menüsünden "hammadde-ambalaj-ticari mallar" için maliyet oluşturma işlemi yapılır. Bitiş tarihi olarak maliyet çalıştırılacak dönemin son günü girilir. Stok modülündeki maliyet tipi parametresine göre ilk malzemeler için maliyetler hesaplanmış olur.

![](../_assets/954e60d2227a5b4143cb.png)

2-Fatura - İşlemler - Ambar Fişi Muhasebeleştirme\* işlemi ile ilgili ay boyunca Hammadde/Sarf Malzemesi/Ticari Mal (I/D/T) dan masraf merkezine yapılan sarf hareketlerini ilgili maliyet fiyatından muhasebeleştirecektir.

Masraf merkezine yapılan sarf hareketleri, reçetede yer almayan ve paçal şekilde sarf hareketi girilen hammaddeler için uygulanmaktadır. Bu tür hammaddeler için **tipi "üretim" ve çıkış yeri "masraf merkezi"** olan ambar çıkış fişi girilmektedir, ambar çıkış fişinde "masraf kodu" bölümünde fatura modülünde tanımlanmış olan masraf merkezlerinden biri seçilir. Masraf merkezi tanımlanırken muhasebe hesap planında ilgili masrafa denk gelen gider hesap kodu seçilir. Masraf merkezi tanımında seçilen gider kodunun, ilgili mamul ana grup kayıtlarında gider olarak seçilmiş olması gerekmektedir. Böylece bu masraf merkezine yapılan sarfiyatlar ilgili mamul ana grup kayıtlarına gider olarak dağıtılacaktır.
![](../_assets/01a7351d089d0e9e2fb9.png)

Öte yandan üretim tipli ambar çıkış fişinde çıkış yeri olarak **"mamul ana grup kodu"** veya "**mamul grup kodu**" seçilebilir, bu durumda ambar fişi muhasebeleştirme yapmaya gerek yoktur. Ambar çıkış fişinin mamul ana grup koduna bağlı olarak kaydedildiği durumlarda mamul ana grup kodu kayıtlarında dağıtım anahtarları sekmesindeki "**hammadde sarfları ana grup kodu bazında"** parametresi işaretlenmelidir.

![](../_assets/5be9144d7f895031038e.png)

3-Üretim merkezleri dışında gerçekleşen veya üretim safhaları bazında girişi yapılamayan giderler, farklı hesaplarda takip edildiğinden bu hesaplardaki biriken tutarlar belirlenen oranlarla üretim merkezlerine ait muhasebe hesaplarına aktarılmalıdır. Bunun için öncelikle Muhasebe - İşlemler - Yardımcı Servis Dağıtım İşlemleri - Dağıtım tablosu\* ekranından dağıtımı yapılacak hesaplar ve oranlar girilmelidir.

![](../_assets/9478b67fea24c867f3b4.png)
Örneğin tanımı yapılan üretim sisteminde ulaşım giderleri terk bir kalem olarak ödenmektedir. Fakat bu giderlerin mamul ana grup bazında farklı hesaplara dağıtılması istenmektedir. Yukarıdaki tanımlamada 730-003-001 hesabına genel bir ulaşım gideri ödenmiştir. Bu ulaşım giderini üretim safhaları bazında tanımlanmış olan 730-001-002 ve 730-001-003 hesaplarına dağıtmak için **Muhasebe** **İşlemler** **Yardımcı Servis Dağıtım İşlemleri** **Dağıtım Fişi Oluşturma** işlemi yapılmalıdır. Bu işlem dağıtım tablosundaki oranlara göre yevmiye fişi oluşturacaktır.

![](../_assets/95eb1db14e31aed47927.png)

4-Son olarak \*Maliyet Muhasebesi  Kayıt  Maliyet Hesaplatma\* menüsünden maliyet muhasebesi çalıştırılır.

![](../_assets/65a36bf1c649923cd02c.png)

**Tarih** bilgisi olarak maliyet hesabı yapılacak ay\\yıl girilir.

**"Hazırlık yapılacak"** parametresi maliyet hesaplama işleminin tekrardan yapılmasını sağlayacaktır.

**"Mahsup oluşturulacak"** parametresi hesaplanan maliyet mahsubunun yevmiye fişi olarak muhasebeye aktarımını sağlar.

**Ana grup paylaştırma hassasiyeti,** mamul ana grup kayıtları \\ dağıtım anahtarları sekmesinde "hammadde sarfları mamul ana grup bazında" parametresi işaretli olduğunda anlam kazanmaktadır. Ambar çıkış fişiyle mamul ana grubuna bağlı olarak sarf edilen hammaddelerin dağıtımında bu parametrede yazılan hassasiyet değeri kullanılır. Örneğin bu değer 0.0001 olarak tanımlandığında bu değerden daha küçük (örneğin 0.0000001) bir değer, maliyet hesabına dahil edilmemektedir.

**Genel safha sayısına** üretim safhaları arasında meydana geri dönüşlerin bir fazlası girilir. Örneğin son ürünün üretimi sırasında PRES  MONTAJ  PRES şeklinde bir işlem sırası varsa; ki bir böyle bir durum bir kere geri dönüş olduğunu göstermektedir; bu durumda genel safha sayısına 1+1 = 2 değeri girilmelidir.

**Örnek Senaryo**

Yukarıdaki sabit bilgiler bölümünde yapılan tanımlamalar kullanılarak sistemde aşağıdaki hareketler yapılıyor.

1-11 TL fiyat ile 05.07.2016 tarihinde 100 adet Hammadde1 kapalı faturayla satın alınıyor.

2-12 TL fiyat ile 10.07.2016 tarihinde 100 adet Hammadde1 açık faturayla satın alınıyor.

3-15 TL fiyat ile 01.07.2016 tarihinde 50 adet Hammadde2 açık faturayla satın alınıyor.

4-20 TL fiyat ile 10.07.2016 tarihinde 100 adet Hammadde2 açık faturayla satın alınıyor.

5-5 TL fiyat ile 10.07.2016 tarihinde 150 adet Hammadde3 açık faturayla satın alınıyor.

6-1 TL fiyat ile 18.07.2016 tarihinde 100 kg BOYA açık faturayla satın alınıyor.

Hammadde satın alımları sonrasında oluşan yevmiye fişi ve hareket gören muhasebe hesapları aşağıdaki gibi olmaktadır:

| Hesap Kodu | Hesap Adı | Borç Tut. | Alacak Tut. |
| --- | --- | --- | --- |
| 150-001-001 | HAMMADDE1 | 1,200.00 | 0 |
| 100-001-001 | KASA- TL | 0 | 1,200.00 |
| 150-001-001 | HAMMADDE1 | 1,100.00 | 0 |
| 320-001-001 | SATICI1 | 0 | 1,100.00 |
| 150-001-002 | HAMMADDE2 | 750 | 0 |
| 320-001-001 | SATICI1 | 0 | 750 |
| 150-001-002 | HAMMADDE2 | 2,000.00 | 0 |
| 320-001-001 | SATICI1 | 0 | 2,000.00 |
| 150-001-003 | HAMMADDE3 | 750 | 0 |
| 320-001-001 | SATICI1 | 0 | 750 |
| 150-001-004 | BOYA | 100 | 0 |
| 320-001-001 | SATICI1 | 0 | 100 |

7-Satın alımlar sonrasında üretim sonu kayıtları atılıyor.

1. 100 adet YARIMAMUL1 üretiliyor.
2. 60 adet YARIMAMUL1 üretiliyor, 10 adet mamul firesi meydana geliyor.
3. 150 adet YARIMAMUL3 üretiliyor.
4. 150 adet YARIMAMUL2 üretiliyor.
5. 150 adet MAMUL1 üretiliyor.

8-Aşağıdaki gider hesaplarına kasadan ödeme yapılıyor.

1. 720-001-001  Preshane işçilik gideri: 1000 TL
2. 720-001-002  Montaj işçilik gideri: 1000 TL
3. 730-004-001  Preshane amortisman: 400 TL
4. 730-004-002  Montaj amortisman: 600 TL
5. 730-001-002  Montaj elektrik gideri: 1500 TL
6. 730-001-001  Preshane elektrik gideri: 800 TL

9-730-003-001 ulaşım giderleri hesabına kasadan 1500 TL ödeme yapılıyor. Bu hesaba yapılan gider "MuhasebeİşlemlerYardımcı Servis Dağıtım İşlemleriDağıtım Fişi Oluşturma" işlemiyle 730-003-002 (preshane ulaşım giderleri) ve 730-003-003 (montaj ulaşım giderleri) hesaplarına dağıtılacaktır.

Bu hesaplar için tanımlanan dağıtım tablosu aşağıdaki gibidir:

| İşlem Sıra No | Kaynak Kodu | Dağıtım Kodu | Oran |
| --- | --- | --- | --- |
| 1 | 730-003-001 | 730-003-002 | 40 |
| 2 | 730-003-001 | 730-003-003 | 60 |

Dağıtım işlemi sonucunda oluşan yevmiye fişi aşağıdaki gibi olmaktadır:

| Hesap Kodu | Hesap Adı | Borç Tut. | Alacak Tut. |
| --- | --- | --- | --- |
| 730-003-002 | PRESHANE ULAŞIM GIDERLERI | 600.00 | 0.00 |
| 730-003-001 | PERSONEL ULAŞIM GİDERLERİ | 0.00 | 600.00 |
| 730-003-003 | MONTAJ ULAŞIM GIDERLERİ | 900.00 | 0.00 |
| 730-003-001 | PERSONEL ULAŞIM GİDERLERİ | 0.00 | 900.00 |

10-Üretim tipli ambar çıkış fişiyle BOYAMA masraf merkezine 5 TL değerinde BOYA malzemesi sarf ediliyor. Bu işlemi muhasebe modülüne yansıtmak için "FaturaİşlemlerAmbar Fişi Muhasebeleştirme" işlemi yapılıyor. İşlem sonucunda oluşan yevmiye fişi aşağıdaki gibi olmaktadır:

| Hesap Kodu | Hesap Adı | Borç Tut. | Alacak Tut. |
| --- | --- | --- | --- |
| 730-002-002 | MONTAJ ALET EDEVAT GIDERLERI | 5 | 0 |
| 150-001-004 | BOYA | 0 | 5 |

Bu işlemler sonrasında maliyet çalıştırma işlem adımları izlenerek aşağıdaki sonuçlar elde edilmiştir:

**1-Stok - İşlemler - Maliyet Oluşturma**

İlk malzemeler ve ambalajlar için maliyet oluşturma işlemi çalıştırıldığında elde edilen maliyetler aşağıdaki gibidir.
Not: Stok modülünde maliyet tipi olarak "aylık ağırlıklı ortalama" yöntemi seçilmiştir.

| Stok Kodu | BIRIM MALIYET |
| --- | --- |
| HAMMADDE1 | 11.50 |
| HAMMADDE2 | 18.33 ( \* ) |
| HAMMADDE3 | 5 |
| BOYA | 1 |

Aylık ağırlıklı ortalama yöntemiyle maliyet hesaplanırken ilgili ay içindeki alış hareketlerine bakılarak aşağıdaki şekilde hesaplama yapılır:

![](../_assets/5b7f0e9587d9a4b4d906.png)

Örneğin; HAMMADDE2 için temmuz ayındaki birim maliyet aşağıdaki şekilde hesaplanmaktadır:

![](../_assets/4c7de93bbd79b00620b2.png)

**2-Fatura - İşlemler - Ambar Fişi Muhasebeleştirme**

Bu işlem sonucunda BOYAMA masraf merkezi için yapılan sarfiyat aşağıdaki şekilde yevmiye fişi haline getirilmiştir:

| Hesap Kodu | Hesap Adı | Borç Tut. | Alacak Tut. |
| --- | --- | --- | --- |
| 730-002-002 | MONTAJ ALET EDEVAT GIDERLERI | 5 | 0 |
| 150-001-004 | BOYA | 0 | 5 |

**3-Muhasebe - İşlemler - Yardımcı Servis Dağıtım İşlemleri - Dağıtım Fişi Oluşturma**

Bu işlem sonucunda 730-003-001 hesabındaki giderler üretim safhaları bazında dağıtılmıştır ve aşağıdaki yevmiye fişi oluşturulmuştur:

| Hesap Kodu | Hesap Adı | Borç Tut. | Alacak Tut. |
| --- | --- | --- | --- |
| 730-003-002 | PRESHANE ULAŞIM GIDERLERI | 600.00 | 0.00 |
| 730-003-001 | PERSONEL ULAŞIM GİDERLERİ | 0.00 | 600.00 |
| 730-003-003 | MONTAJ ULAŞIM GIDERLERİ | 900.00 | 0.00 |
| 730-003-001 | PERSONEL ULAŞIM GİDERLERİ | 0.00 | 900.00 |

**4-Maliyet Muhasebesi - Kayıt - Maliyet Hesaplatma**

Maliyet hesaplatma sonucunda aşağıdaki sonuçlar bulunmuştur:

| Stok Kodu | Üretim Miktarı | Hammadde Miktarı | Hammadde Sarf Tutarı | İşçilik | Enerji | Amortisman | Yardımcı Servis | Yedek Parça | Ambalaj | Yarı Mamul Sarfı | Aylık Maliyet Fiyatı | Ortalama Maliyet |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MAMUL1 | 150 | 0 | 0.00 | 1,000.00 | 1,500.00 | 600 | 5 | 900 | 750 | 7,390.07 | 80.97 | 80.97 |
| YARIMAMUL1 | 150 | 160 | 1,840.00 | 262.30 | 278.26 | 90.01 | 0 | 208.7 | 0 | 0 | 17.86 | 17.86 |
| YARIMAMUL2 | 150 | 0 | 0.00 | 491.80 | 260.87 | 175.47 | 0 | 195.65 | 0 | 3,587.01 | 31.41 | 31.41 |
| YARIMAMUL3 | 150 | 150 | 2,750.00 | 245.90 | 260.87 | 134.52 | 0 | 195.65 | 0 | 0 | 23.91 | 23.91 |

Gider hesaplarının dağıtımı için mamul ana grup kodlarındaki aşağıdaki dağıtım anahtarları dikkate alınmıştır:

<table><tbody><tr><th><p><strong>Mamul Ana Grup Kodu</strong></p></th><th colspan="5"><p><strong>Dağıtım Anahtarları</strong></p></th></tr><tr><td><p><br/></p></td><td><p><strong>Hammadde</strong></p></td><td><p><strong>Ambalaj</strong></p></td><td><p><strong>İşçilik</strong></p></td><td><p><strong>Amortisman</strong></p></td><td><p><strong>Enerji</strong></p></td></tr><tr><td><p>PRESHANE</p></td><td><p>Üretim miktarları oranı</p></td><td><p>Üretim miktarları oranı</p></td><td><p>Birim katsayılar oranı</p></td><td><p>Hammadde sarfları oranı</p></td><td><p>Üretim miktarları oranı</p></td></tr><tr><td><p>MONTAJ</p></td><td><p>Üretim miktarları oranı</p></td><td><p>Üretim miktarları oranı</p></td><td><p>Üretim miktarları oranı</p></td><td><p>Üretim miktarları oranı</p></td><td><p>Üretim miktarları oranı</p></td></tr></tbody></table>

Preshane ana grubuna bağlı bulunan mamul grup kodları için işçilik-birim katsayıları aşağıdaki gibidir:

| Mamul Grup Kodu | İşçilik - Birim katsayısı |
| --- | --- |
| YARIMAMUL1 | 1 |
| YARIMAMUL2 | 2 |
| YARIMAMUL3 | 1 |

Gider hesaplamalarına ait ayrıntılar aşağıdaki gibidir:

a-Preshane safhası için enerji giderinin üretim miktarları oranına göre dağıtımı aşağıdaki gibi hesaplanacaktır:

Mamul grup kodu için gider tutarı : (İlgili mamul grubu için giriş yapan brüt üretim miktarı / İlgili aydaki toplam üretim miktarı) \* Toplam gider tutarı

| Mamul Grup Kodu | Üretim Miktarı | Fire miktarı | Brüt üretim miktarı |
| --- | --- | --- | --- |
| YARIMAMUL1 | 150 | 10 | 160 |
| YARIMAMUL2 | 150 | 0 | 150 |
| YARIMAMUL3 | 150 | 0 | 150 |

- Preshane için toplam enerji gideri  730-001-001 (elektrik gideri) : 800 TL
- İlgili aydaki toplam üretim miktarı = 160+150+150 = 460
- Yarımamul1 için enerji gideri = (160 / 460) \* 800 = 278.26
- Yarımamul2 için enerji gideri = (150 / 460) \* 800 = 260.87
- Yarımamul3 için enerji gideri = (150 / 460) \* 800 = 260.87

b-Preshane safhası için işçilik giderinin birim katsayılar oranına göre dağıtımı aşağıdaki gibi hesaplanacaktır:

Mamul grup kodu için gider tutarı : (mamul ana grubunun birim katsayısı \* mamul ana grubuna ait üretim miktarı) / SUM (birim katsayı \* üretim miktarı) \* Toplam gider tutarı

| Mamul Grup Kodu | Üretim Miktarı | Fire miktarı | Brüt üretim miktarı | Birim katsayı | Birim katsayı \* üretim miktarı |
| --- | --- | --- | --- | --- | --- |
| YARIMAMUL1 | 150 | 10 | 160 | 1 | 160 |
| YARIMAMUL2 | 150 | 0 | 150 | 2 | 300 |
| YARIMAMUL3 | 150 | 0 | 150 | 1 | 150 |

- Preshane için toplam işçilik gideri : 720-001-001 (işçilik gideri) : 1000 TL
- İlgili aydaki bütün mamul grupları için SUM \[birim katsayı \* üretim miktarı\] =160 + 300 + 150=610
- Yarımamul1 için enerji gideri = (160 / 610) \* 1000 = 262.30
- Yarımamul2 için enerji gideri = (300 / 610) \* 1000 = 491.80
- Yarımamul3 için enerji gideri = (150 / 610) \* 1000 = 245.90

c-Preshane safhası için amortisman giderinin hammadde sarfları oranına göre dağıtımı aşağıdaki gibi hesaplanacaktır:

Mamul grup kodu için gider tutarı: (üretim için kullanılan hammadde+ yarı mamul tutarı / toplam hammadde+ yarı mamul tutarı) \* Toplam gider tutarı

| Mamul Grup Kodu | Üretim Miktarı | Hammadde Tutarı | Yarı mamul Tutarı |
| --- | --- | --- | --- |
| YARIMAMUL1 | 150 | 1,840.00 | 0 |
| YARIMAMUL2 | 150 | 0 | 3,587.01 |
| YARIMAMUL3 | 150 | 2,750.00 | 0 |

- Preshane için toplam amortisman gideri  730-004-001 (amortisman gideri) : 400 TL
- İlgili aydaki bütün mamul grupları için SUM \[hammadde+ yarımamul tutarı\] = 1840 + 2750 + 3587.01 = 8177.01
- Yarımamul1 için amortisman gideri = (1840 / 8177.01) \* 400 = 90.01
- Yarımamul2 için amortisman gideri = (2750 / 8177.01) \* 400 = 175.47
- Yarımamul3 için amortisman gideri = (3587.01 / 8177.01) \* 400 = 134.52

Maliyet muhasebesi hesaplamaları sonrasında oluşan maliyet fişi aşağıdaki gibi olmaktadır:

| Hesap Kodu | Hesap Adı | Açıklama | Borç Tut. | Alacak Tut. |
| --- | --- | --- | --- | --- |
| **151** | **YARI MAMULLER - URETIM** |  | **23,135.98** | **0** |
| 151-001-001 | YARIMAMUL1 | YARIMAMUL1: GRUBU MALİYET | 2,646.53 | 0 |
| 151-001-002 | YARIMAMUL2 | PRESHANE: A.GR.SARF | 3,600.96 | 0 |
| 151-001-002 | YARIMAMUL2 | YARIMAMUL2: GRUBU MALİYET | 1,142.52 | 0 |
| 151-001-003 | YARIMAMUL3 | YARIMAMUL3: GRUBU MALİYET | 3,600.96 | 0 |
| 151-001-004 | YARIMAMULLER GECICI YANSITMA HESABI | MONTAJ: A.GR.SARF | 7,390.01 | 0 |
| 151-001-004 | YARIMAMULLER GECICI YANSITMA HESABI | MAMUL1: GRUBU MALİYET | 4,755.00 | 0 |
| **152** | **MAMULLER** |  | **12,145.01** | **0** |
| 152-001-001 | MAMUL1 | MAMUL1: GRUBU MALİYET | 12,145.01 | 0 |
| **620** | **SATILAN MAMULLER MALIYETI** |  | **8,096.67** | **0** |
| 620-001-002 | MONTAJ - SATILAN MAMUL MALIYETI | MAMUL1: GRUBU SAT.MAM.MAL. | 8,096.67 | 0 |
| **710** | **DIREKT ILK MADDE VE MAL.GIDERL** |  | **5,340.00** | **0** |
| 710-001-001 | PRESHANE HAMMADDE SARFLARI | PRESHANE: A.GR.SARF | 4,590.00 | 0 |
| 710-001-004 | MONTAJ AMBALAJ SARFLARI | MONTAJ: A.GR.SARF | 750.00 | 0 |
| **150** | **ILK MADDE VE MALZEME** |  | **0** | **5,340.00** |
| 150-001-001 | HAMMADDE1 | PRESHANE: A.GR.SARF | 0 | 1,840.00 |
| 150-001-002 | HAMMADDE2 | PRESHANE: A.GR.SARF | 0 | 2,750.00 |
| 150-001-003 | HAMMADDE3 | MONTAJ: A.GR.SARF | 0 | 750.00 |
| **151** | **YARI MAMULLER - URETIM** |  | **0** | **23,135.98** |
| 151-001-001 | YARIMAMUL1 | MONTAJ: A.GR.SARF | 0 | 2,646.53 |
| 151-001-002 | YARIMAMUL2 | MONTAJ: A.GR.SARF | 0 | 4,743.48 |
| 151-001-003 | YARIMAMUL3 | PRESHANE: A.GR.SARF | 0 | 3,600.96 |
| 151-001-004 | YARIMAMULLER GECICI YANSITMA HESABI | MAMUL1: GRUBU MALİYET | 0 | 12,145.01 |
| **152** | **MAMULLER** |  | **0** | **8,096.67** |
| 152-001-001 | MAMUL1 | MAMUL1: GRUBU SAT.MAM.MAL. | 0 | 8,096.67 |
| **711** | **DIREKT ILK MAD.VE MAL.YAN.FARK** |  | **0** | **5,340.00** |
| 711-001-001 | PRESHANE HAMMADDE SARFLARI | PRESHANE: ANA GRUP MALİYET YANS. | 0 | 4,590.00 |
| 711-001-004 | MONTAJ AMBALAJ SARFLARI | MONTAJ: ANA GRUP MALİYET YANS. | 0 | 750.00 |
| **721** | **DIREKT ISCI.GIDERLERI YANSITMA** |  | **0** | **2,000.00** |
| 721-001-001 | PRESHANE ISCILIK GIDERLERI | PRESHANE: ANA GRUP MALİYET YANS. | 0 | 1,000.00 |
| 721-001-002 | MONTAJ ISCILIK GIDERLERI | MONTAJ: ANA GRUP MALİYET YANS. | 0 | 1,000.00 |
| **731** | **GENEL URETIM GIDER. YANSITMA** |  | **0** | **4,805.01** |
| 731-001-001 | PRESHANE ELEKTRIK GIDERI | PRESHANE: ANA GRUP MALİYET YANS. | 0 | 800.01 |
| 731-001-002 | MONTAJ ELEKTRIK GIDERI | MONTAJ: ANA GRUP MALİYET YANS. | 0 | 1,500.00 |
| 731-002-002 | MONTAJ ALET EDEVAT GİDERLERİ | MONTAJ: ANA GRUP MALİYET YANS. | 0 | 5.00 |
| 731-003-002 | PRESHANE ULASIM GIDERLERI | PRESHANE: ANA GRUP MALİYET YANS. | 0 | 600.00 |
| 731-003-003 | MONTAJ ULASIM GIDERLERI | MONTAJ: ANA GRUP MALİYET YANS. | 0 | 900.00 |
| 731-004-001 | PRESHANE AMORTISMAN GIDERLERI | PRESHANE: ANA GRUP MALİYET YANS. | 0 | 400.00 |
| 731-004-002 | MONTAJ AMORTISMAN GIDERLERI | MONTAJ: ANA GRUP MALİYET YANS. | 0 | 600.00 |
|  |  | **Toplam** | **48,717.66** | **48,717.66** |
