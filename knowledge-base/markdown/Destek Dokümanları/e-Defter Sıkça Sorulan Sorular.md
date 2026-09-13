---
title: "e-Defter Sıkça Sorulan Sorular"
page_id: "50684975"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "e-Defter Sıkça Sorulan Sorular"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / e-Defter Sıkça Sorulan Sorular"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWMxYWE2ZWRiLTgyZTMtNDllZC1iYzAyLTFmZjU0ZWRjZTYyNiZsaW5rPTEzM2VhMThhLWRkOWEtNGQzYy1hZGE2LWQzYzM4NGRjMmY1ZiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=c1aa6edb-82e3-49ed-bc02-1ff54edce626&link=133ea18a-dd9a-4d3c-ada6-d3c384dc2f5f&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "e-defter-sikca-sorulan-sorular_50690003_50684975.html"
source_version: "2022-12-13T13:10:27.360+03:00"
source_bytes: 2619240
fetched_at: "2026-09-13T04:25:24+00:00"
generator: "netsis-scraper 1.0.0"
---
# e-Defter Sıkça Sorulan Sorular

**e-Defter nedir?**

Şekil hükümlerinden bağımsız olarak Vergi Usul Kanununa ve/veya Türk Ticaret Kanununa göre tutulması zorunlu olan defterde yer alması gereken bilgileri kapsayan elektronik kayıtlar bütünüdür.

Standartlara uygun olarak hazırlanan elektronik defterlerin değişmezliğinin, kaynağının ve bütünlüğünün sağlanmasında gerçek kişiler için elektronik imza veya tüzel kişiler için mali mühür kullanılacaktır.

Böylece defterlerin kağıt ortamına basılması ve saklanması gibi zahmetli ve maliyetli işlemler artık elektronik ortamda kolayca ve maliyetsiz olarak yapılabilmekte, defterlerin kaynağının doğruluğu, sonradan değiştirilmediği, belgelerin bütünlüğü e-imza/mali mühür ve başkanlık beratı ile garanti altına alınmaktadır.

**Netsis** **e-Defter** uygulaması ile "Yevmiye Defteri"' , "Defter-i Kebir (Büyük Defter)" ve "Defter Raporu " belgeleri, GİB tarafından belirlenen standartlarda hazırlanabilmekte ve elektronik olarak GİB'e kolayca gönderebilmektedir.

Netsis e-Defter uygulaması ile aşağıdaki işlemler yapılır:

- e-Defter dosyaları aylık olarak xml formatında oluşturulur.
- e-Defter oluşturulurken eksik ve hatalı kayıtlar otomatik olarak tespit edilir ve uyarı verilerek işlem kesilir.
- e-Defter dosyaları ile birlikte, imzalanmış/mühürlenmiş berat dosyası oluşturulur.
- Oluşan XML dosyaların içeriği kontrol amaçlı görüntülenebilir.
- Oluşturulan e-Defter berat dosyaları GİB sistemine otomatik gönderilir.
- Yedekleme hizmeti satın alınması durumunda e-Defter dosyaları otomatik olarak Logo Özel Entegratör servislerinde saklanır.

![](../_assets/7823cf17b656f443736b.png)

![](../_assets/747f79c0786177626493.png)

**Zaman Damgası nedir, neden kullanılır?**

Zaman damgası, 5070 sayılı Elektronik İmza Kanunu'nda tanımlandığı üzere; elektronik bir verinin, üretildiği, değiştirildiği, gönderildiği, alındığı veya kaydedildiği zamanın tespit edilmesi amacıyla, hizmet sağlayıcısı tarafından elektronik imzayla doğrulanan kayıtların resmi olarak kanıtlanmasıdır. Zaman damgaları, verinin belirtilen tarihte oluşturulduğu, değiştirildiği veyahut gönderilip alındığını bilgisini doğrulamada kullanılmaktadır.

![](../_assets/33c63873840400b209d7.png)

Örneğin, bir elektrik kesintisi veya sistem arızası nedeni ile beratların Başkanlık tarafından onaylanması işleminin gerçekleştirilememesi durumunda söz konusu beratlar, güvenli elektronik imza (gerçek kişiler için) veya mali mühür (tüzel kişiler için) ile zaman damgalı olarak imzalanacak veya onaylanacaktır. Bu kapsamda kullanılacak olan zaman damgaları TÜBİTAK-UEKAE 'den temin edilecektir.

**e-Defter uygulamasını hangi Logo Netsis çözümleri ile kullanabilirim?**

e-Defter uygulaması tüm Logo Netsis çözümleri ile birlikte kullanılabilmektedir.

**e-Defter uygulamasından faydalanmak için Logo Netsis tarafında neler yapılmalı?**

Öncelikle e-Defter lisansının mevcut olması gerekmektedir. Lisans işlemleri sonrasında mükellef ve düzenleyen bilgileri doğru ve eksiksiz bir şekilde tanımlanmalı ve girilen TCKN/Vergi numarası lisans bilgilerindeki ile aynı olmalıdır. Defter gönderimi yapacak olan makinede EFaturaAyarlar üzerinden NetsisEdefter.dll sakla işlemi çalıştırılmalı ve sertifikasız ayar tanımlama işlemi yapılmalıdır.

**Dönem ortasında Logo Netsis e-Defter uygulamasına geçebilir miyim?**

Evet geçebilirsiniz. Ancak defterlerin tekil numaralarının doğru takibi için eski aylara ait defterlerin Netsis'e yüklenmiş olması gerekmektedir. Bu işlem e-Defter Onaylama/İşlemler/Defter Yükle adımı ile yapılabilir.

**Gönderilen defterler GIB sisteminde başarısız olursa ne yapmalıyız?**

Eğer defterlerin yüklenme süresi geçmedi ise neden başarısıza düştüğü tespit edilip Netsis'ten silinmeli ve sorun giderildikten sonra tekrar oluşturulup gönderilmelidir. Ancak yükleme süresi geçmiş bir defter hataya düştü ise hata sebebi incelenmeli iptal ve tekrar gönderimi için GIB'e başvurulmalıdır.

**GIB sisteminde defterlerim onaylı ancak rapor dosyası hatalı görünüyor. Sadece rapor dosyasını** **tekrar** **göndermenin** **bir** **yolu** **var** **mıdır?**

Hatalı aya ait defterlerin fiziki dizinde bulunan AY klasöründen rapor dosyası alınıp, GIB sistemine sırası ile manuel yüklenebilir.

**TBLEDEFTER tablosu silindi ama defterlerin fiziki dosyaları mevcut ne yapabilirim?**

e-Defter Onaylama/İşlemler/Defter Yükle ile tüm defterler yüklenebilir.

#### ![](../_assets/cfd574a25f5817788e45.png)

**Defter yükleme işlemi nasıl yapılmalıdır?**

Defterlerin hatasız yüklenebilmesi için tüm defterler ağaç yapısı mantığında saklanmış olmalıdır. Çünkü defter yükleme işleminde sadece defter(ayrı ayrı Y,K,EDR dosyası) seçilmekte program deftere bağlı berat ve GIB onaylı berat dosyasını ağaç yapısı sayesinde otomatik olarak yüklemektedir.

#### ![](../_assets/53ae22f6988d3b83df06.png)

**Defter dizinin ağaç yapısında olması neden önemlidir?**

Ağaç yapısı GIB'in belirlediği ve uyumluluk onayı alan yazılım firmalarını sorumlu tuttuğu bir yapıdır. "Yevmiye/kebir dosyalarının, yevmiye/kebir beratlarının, defter raporunun ve GIB onaylı yevmiye/kebir beratlarının içinde tutulduğu dizin ilgili ayın paketleri bir klasörde, tüm ayların toplamı hesap dönemi klasöründe ve hesap dönemi klasörlerin hepsi de aynı klasörde olacak şekilde saklanmalıdır. XML dosyalarını mükellefin/denetim elemanının düzgün görüntüleyebilmesi için XSLT dosyaları da ilgili ay dizinlerinin içerisine konulmalıdır. Bunun için Defter Onaylama ekranında bir dizin vermeniz yeterlidir. Dizin altına ağaç yapısı manuel oluşturulmamalıdır. Uygulama dizin altındaki yapıyı oluşturmaktadır.

**GIB sistemine defterleri yükledikten sonra aynı dönemin defterini tekrar gönderebilir miyim?**

GİB sistemine yüklenmiş, onaylı beratları alınmış bir tarih aralığı için bir daha defter oluşturulamaz. Eğer yükleme zamanı geçmedi ise GIB sisteminden defter silinebilir ve tekrar oluşturup gönderilebilir. Ancak yükleme zamanı geçti ise iptali için GİB'e başvuru yapılmalıdır.

**Defteri gönderilmiş aya ait kayıtlar üzerinde düzeltme yapılmasını engelleyebilir miyiz?**

Mükellef ve düzenleyen bilgilerindeki "e-Defter oluşturulan aya ait belgelerde değişiklik yapılmasın" parametresi ile değişiklik, iptal ve yeni kayıt işlemlerinin önüne geçilebilmektedir.

**Boş e-Defter gönderimi yapılabilir mi?**

![](../_assets/1aa0ae5c2afa8d2c8bbb.png)

Faaliyet halinde bir firmanın e-Defter dosyasının oluşması için ilgili döneme ait sistemde en az bir adet yevmiye kaydının bulunması gerekir. e-Defter oluşturacak döneme ait hiçbir mahsup fişi bulunmuyor ise dosya oluşturma işlemi sırasında «**Tüm** **ayı** **kapsayan** **bir** **defterde** **en** **az** **1** **gl-cor:entryHeader** **elemanı** **olmalıdır»** uyarısı alınmaktadır.

**e-Defter Saklama Hizmeti Nedir? Hangi Yönetmelerle Saklama Yapılabilir?**

19/10/2019 tarih ve 30923 sayılı Resmi Gazetede yayınlanan Tebliğ'de belirtildiği gibi; "e-Defter dosyaları ile bunlara ilişkin berat dosyalarının ikincil kopyalarının, gizliliği ve güvenliği sağlanacak şekilde e-Defter saklama hizmeti yönünden teknik yeterliliğe sahip ve Başkanlıktan bu hususta izin alan özel entegratörlerin bilgi işlem sistemlerinde ya da Başkanlığın bilgi işlem sistemlerinde 1/1/2020 tarihinden itibaren asgari 10 yıl süre ile muhafaza edilmesi zorunludur. "

Bu zorunluluğa istinaden, firmalar internet ortamında gönderilmiş olan e-Defter kayıtlarını kendileri saklayabilir ya da özel entegratörler aracılığı ile bu hizmeti daha güvenli olarak alabilirler.

Mükellefler, kendi bilgi işlem sistemlerinde muhafaza edilen elektronik defter ve beratların silinmesi, zarar görmesi, virüs bulaşması vb. nedenlerle elektronik defter ve beratların ibrazında sorun yaşayabilmektedir. Özellikle son dönemlerde artan siber saldırılar nedeniyle birçok mükellefimizin elektronik defter dosyalarının zarar gördüğü görülmekte ve bu nedenle Özel Entegratör üzerinden saklama hizmeti alınmasının önemi giderek artmaktadır.

![](../_assets/0663a176c8d39d12e1b0.png)![](../_assets/82a4abfaa980b2827cc2.png)![](../_assets/d470bc82719cc2a54ad7.png)

#### e-Defter Dosyaları Otomatik Olarak Saklanabilir Mi?

LOGO Özel Entegratörlük hizmeti satın alınmış ise mevcut kontörler saklama hizmetinde kullanılabilir. Bunun için Netsis Entegratör Servisi kurulumunun E-Defter Yedekleme seçeneği ile çalıştırılmış olması, ve servisin kurulduğu makinede sertifikasız ayar tanımlama yapılmış olması gerekmektedir.

#### ![](../_assets/3c90a704bba6a7d8b201.png)![](../_assets/078cd20c63be3ee80976.png)

**Gelir İdaresinde ve Netsis'te onaylı görünen defter e-Logo defter saklama portalına yüklendiğinde "Yüklenecek dosyalar sistemdeki mevcut dosyalar ile uyumluluk sağlamıyor" uyarısını neden alır?**

Bu uyarı yüklenen defter dosyalarının, beratlar ve GIB onaylı beratlarındaki imza değerleri ile uyumsuz olduğunda alınmaktadır. Bunun teyidi için öncelikle ilgili dönem e-Defterleri [edefter.gov.tr](http://edefter.gov.tr) internet adresinde yayınlanan "e-Defter Görüntüleyici Programı" ile kontrol edilmeli ve program tarafından üretilen "Durum Raporu'nda" e-Defterler ile ilişkili berat dosyalarında imza uyumsuzluğundan dolayı sorun oluştuğu netleştirilmelidir.

e-Defter görüntüleyici programında «defterin imza değeri ile GIB onaylı beratındaki uyuşmamaktadır» uyarısı alınıyor ise yapılabilecek tek işlem GIB ile görüşüp defter iptali talep etmek ve iptal sonrasında Netsis tarafında defteri tekrar oluşturup göndermektir.

![](../_assets/e2ad9d71733ac30e42e6.png)

**GİB Tarafından Yayınlanan e-Defter Bildirim Programı ile e-Defter Dosyalarının Saklanması Zorunlu Mudur?**

e-Defter dosyaları ile bunlara ilişkin berat dosyalarının ikincil kopyalarının Gelir İdaresi Başkanlığı'nın bilgi işlem sistemlerinde saklanması zorunludur.

Bu saklama işlemi için [https://deftersaklama.gib.gov.tr/download/](https://deftersaklama.gib.gov.tr/download/) adresinden GİB tarafından yayınlanan e-DefterBildirim programı indirilmeli ve bu program aracılığı ile e-Defter dosyaları GIB sunucularında saklanmalıdır.

Logo Özel Entegratörlük servisi ile saklama yapılıyor ise Entegratör portalında parametreler kısmında "e-Defter dosyalarım saklanmak üzere GİB ile paylaşılsın" parametresinin "Evet" yapılması durumunda e-Defter dosyaları GİB sunucularına saklanmak üzere otomatik olarak gönderilecektir.

**e-Defter saklama programında "Çapraz Doğrulama Kontrolü Hatalıdır" uyarısı neden alınmaktadır?**

e-Defter Saklama Programında "Çapraz Doğrulama Kontrolü Hatalıdır" uyarısı alan mükellefler (ilgili dönem e-Defterlerini [edefter.gov.tr](http://edefter.gov.tr) internet adresimizde yayınlanan "e-Defter Görüntüleyici Programı" ile kontrol etmeleri ve program tarafından üretilen "Durum Raporu'nda e-Defterler ile ilişkili berat dosyalarında imza hatası almadıkları durumda) ile "Counter Signature Doğrulama Kontrolü Hatalıdır" uyarısı alan mükelleflerin e-Defter Saklama Programının [https://deftersaklama.gib.gov.tr/download/](https://deftersaklama.gib.gov.tr/download/) adresinde yayınlanan e-DefterBildirimV2.4_Prod.exe versiyonunu indirerek eski versiyonu kaldırdıktan sonra yeni versiyon ile kurulum işlemini tamamlamaları ve söz konusu hataları alan paketlerini tekrar yüklemeleri gerekmektedir.

e-Defter Görüntüleyici Programı ile kontrol etmeleri ve program tarafından üretilen "Durum Raporu'nda e-Defterler ile ilişkili berat dosyalarından imza hatası aldıkları durumda ise oluşan hatanın kaynağının tespiti için xml içerisindeki imza değerleri kontrol edilmelidir.

**e-Defter Yükleme Takviminde Tercihli Dönem Nedir?**

Geçici vergi dönemleri bazında berat yükleme tercihinde bulunmak isteyen mükelleflerin, mali mühür veya elektronik imza ile e-Defter uygulamasına giriş yapıp "Bilgi Güncelle" kısmından "Berat Yükleme Tercihi" bölümünden; Aylık yükleme / Geçici vergi dönemleri bazında yükleme şeklinde seçimlerini yapmaları mümkün bulunmaktadır. 31.01.2020 tarihine kadar yapılan bu seçim göre e-Defter berat dosyalarının GİB sistemine yüklenme süreleri değişiklik göstermiştir. Bu konuyla ilgili program tarafında bir geliştirme yapılmasına gerek olmayıp sadece belirtilen tarihlerde ilgili dönemlere ait e-Defter dosyalarının oluşturulup belirtilen tarihlere kadar beyan edilmesi gerekmektedir.

![](../_assets/2123717cfae8e0daaf2c.png)

**Defter isimleri neye göre oluşur?**

Gönderilecek paketlerde aşağıdaki belirtilen isimlendirme şekillerinden birisi kullanılacaktır.

1234567808-201901-YB-000000-*0001*.zip

1234567808-201901-YB-000000.zip

**1234567808**: Defterin ait olduğu tüzel kişiler için vergi kimlik numarası (VKN), gerçek kişiler için vatandaşlık numarası (TCKN)

**201901**: e-Defter'in dönemi

**Y, K, YB, KB,DR** : Belge türü kodu. Yevmiye defteri için Y, büyük defter için K, yevmiye defter beratı için YB, kebir (büyük defter) beratı için KB, Defter raporu için DR kullanılacaktır.

**000000**: Parça numarası. Aylık oluşturulan defterin kaç parçadan oluştuğunu gösteren sayaçtır. Parça numarası 6 hanelidir. Defter bölünmeden tek bir parça şeklinde oluşturuluyorsa "000000" değerini almalıdır. Aylık oluşturulan defterin boyutu nedeniyle bölünme olması halinde aylık bölünen defter parçalarına "000001" den başlayarak numara verilmektedir.

**0001**: Şube numarası.

"000000" ve "000001" parça numaraları aynı anda bulunmamaktadır. Bir arada oldukları takdirde hata alınmaktadır. Şube numarası **''0000'' olamaz**, "0001"den başlamalıdır. Bu nedenle şubeli defter kullanımı varsa Mükellef ve Düzenleyen bilgilerinde Şube Kodu sahasında 0 kodu kullanılmamalıdır.

Parça numarası Defter raporu için sadece 000000 olabilir. Çünkü defter raporu tüm ayı içerir. Parçalı defterde defter raporu son parça oluşturulduğunda oluşacaktır.

**Manuel defter bölmede nelere dikkat etmeliyim?**

Oluşturulacak defterlerin (Y ve K dosyalarının) boyutunun **200 MB**'i geçmesi halinde bölünmesi gerekmektedir. Uygulama defter oluşturma anında bu boyut kontrolünü gerçekleştirip defteri otomatik olarak böler. Eğer bu işlemin herhangi bir sebeple manuel yapılması isteniyor ise dikkat edilmesi gereken bazı noktalar vardır.

| Parça No | İlk Yevmiye Tarihi | Son Yevmiye Tarihi | periodCoveredStart | periodCoveredEnd |
| --- | --- | --- | --- | --- |
| 000001 | 2019-01-02 | 2019-01-10 | 2019-01-01 | 2019-01-10 |
| 000002 | 2019-01-15 | 2019-01-20 | 2019-01-11 | 2019-01-20 |
| 000003 | 2019-01-20 | 2019-01-31 | 2019-01-20 | 2019-01-31 |

Defter belgesinde bulunan ilk yevmiye tarihi Ocak ayının 2'si olduğu halde "periodCoveredStart" elemanına Ocak ayının 1'i yazılmıştır. **İlk** **parçaya** **ait** "periodCoveredStart" elemanına her zaman ilgili ayın ilk günü yazılmalıdır. 000002 numaralı parçada ilk yevmiye tarihi Ocak ayının 15'i olduğu halde "periodCoveredStart" elemanına Ocak ayının 11'i yazılmıştır. Parçalar arasında gün boşluğu (bazı günler için yevmiye kaydı olmayabilir) olsa bile dokümanın kapsadığı günleri ifade eden "periodCoveredStart" ve "periodCoveredEnd" elemanları arasında gün boşluğu olmamalıdır. Sonuç olarak bir döneme ait bir parçanın "periodCoveredStart" elemanı ile bir önceki parçasına ait "periodCoveredEnd" elemanı arasında gün boşluğu olmamalıdır.

![](../_assets/9c4feb0777199f0066c0.png)

**Şubeli** **defter** **vermek** **için** **yapılması** **gereken** **işlemler** **nedir?**

Defterler hesap dönemi başında ne şekilde verildi ise dönem sonuna kadar o şekilde devam edilmelidir. Yani dönem başında defterler şubeler dahil verildi ise dönem ortasında şubeli defter verilemez. Gelir idaresi bu kontrolü sağlamaktadır. Bu bilgi eşliğinde Netsis içerisinde defterlerin şube bilgisi ile oluşabilmesi için Mükellef ve Düzenleyen Bilgileri/Defter Bilgileri ekranında e-Defter Şube Uygulaması Kullanılsın parametresi işaretlenip şube kodu doldurulmuş olmalıdır.

Şubeli defter verilecekse «0» şube kodu kullanılmamalıdır. Ve defter her şubenin kendi içerisinden oluşturulmalıdır. Defter isimleri "VKN-Yıl/Ay-Parça No-Şube Kodu" formatında oluşacaktır.

Şubeli defter isimlendirme : 1234567808-201901-YB-000000-*0001*.zip Son 4 karakter şube kodunu belirtmektedir. Bazı durumlarda ( her şubenin ayrı bir veritabanında tutulması gibi) şubesiz datada şubeli defter oluşturmak istenebilir. Bu durumda aşağıdaki özel parametre tanımlanıp yine şube bilgileri doldurulmalıdır. EDEFTER/SUBELERDE_ORTAK_SUBELI_EDEFTER

**e-Defter kapsamında tasfiye ve nevi değişikliği halinde neler yapılmalıdır?**

Tasfiye veya nevi değişikliğine giden firmaların e-Defter dosyalarını sorunsuz oluşturabilmesi için, işlem tarihinden önceki ve sonraki kayıtların 2 ayrı şirkette izlenmesi gerekmektedir.

• Tasfiye/Nevi Değişikliği Tarihinde İseniz: Yeni yıl kopyalama işlemi yapılarak işlem tarihinden sonraki kayıtlar bu yeni açılan şirkete girilmelidir.

• Tasfiye/Nevi Değişikliği Tarihi Geçti İse: Şirket kopyalama işlemi yapılmalı; işlem tarihinden önceki kayıtlar kaynak şirkette tutulurken, sonraki kayıtlar hedef şirkette yer alacak şekilde düzenlenmelidir.

Tasfiye öncesi şirkette ilgili aya ait defter eski mühürle oluşturulup gönderildikten sonra GIB tarafında onaylanması beklenmelidir. Onay alındıktan sonra tasfiye sonrası şirkette Mali Yıl Başlangıç Ayı, Dönem Başlangıç ve Bitiş tarihleri tasfiye tarihine göre düzenlenmeli, “Mali dönem başlangıcı farklı olduğunda e-defter periyot başlangıç günü ay başı yapılsın” parametresi işaretlenmeli, Yardımcı Programlar/Şirket-Şube Parametre Tanımları ekranından unvan TASFİYE HALİNDE bilgisini içerecek şekilde düzenlenmeli ve hazırlık çalıştırılmalıdır. Bu şirkette defter tekil numarası ve madde numarası 1’ den başlamalıdır.

Not: Sürecin hatasız yürütülmesi için GIB tarafında tasfiye ile ilgili yürütülen operasyon tamamlanmış ve GIB tarafından defter gönderimi yapılabileceğine dair mail alınmış olmaldır.

**Kontrol Numarası (uniqueID) (Tekil No)**

Kontrol numarası, **ilgili** **hesap** **dönemi** **içerisinde** birbirinden ayrı olarak oluşturulan defter dosyalarının müteselsilliğini ve birbirleri ile bağlanabilmelerini sağlamaya yönelik bir numaradır.

YEV201101000001 (Ocak ayına ait tek parça defterin uniqueid örneği)

YEV201102000002

YEV201102000003 (Şubat ayına ait iki parça deftere ait uniqueid örneği)

YEV201103000004 (Mart ayına ait tek parça deftere ait uniqueid örneği)

Her firma **kendi** **hesap** **dönemi** **içerisinde** birbirinden ayrı olarak oluşturulan defter dosyalarının müteselsilliğini hem ay hem de parça numarası bazında sağlayacaktır.

![](../_assets/926ece6b723074bc33b9.png)

**e-Defter dosyasının şematron kontrolü sırasında "gl-cor:enteredBy elemanı en az iki karakter olmamalıdır" uyarısı neden alınır?**

e-Defter dosyasında bulunan her bir yevmiye kaydının, oluşturan kullanıcı bilgisinin e-Defter dosyasında bulunması gerekir. Bu bilgi TBLMUHFIS tablosunun KAYITYAPANKUL sahasından alınır ve TBLKULLANP ile eşleştirilir. Eğer bu kullanıcının TBLKULLANP tablosunda ISIM_SOYAD bilgisi boş ise bu uyarı alınır.

![](../_assets/01b1131ed7cd27117eea.png)

**e-Defter oluşturma sırasında "N'EDefterRepository-GetUserInfo çalıştırımında hata oluştu Unclosed quotation mark after the character string '','')''. " uyarısı neden alınır?**

e-Defter dosyasında bulunan her bir yevmiye kaydının oluşturan kullanıcı bilgisinin e-Defter dosyasında bulunması gerekir. Bu bilgi TBLMUHFIS tablosunun KAYITYAPANKUL sahasından alınır ve TBLKULLANP ile eşleştirilir. Eğer bu kullanıcının TBLKULLANP tablosunda KULLANICI_ISIM sahasında ','',- değerleri yani Kullanıcı Adı tanımında türkçe karakter varsa bu uyarı alınmaktadır.

![](../_assets/4c9ca73f931557e0b134.png)

**e-Defter dosyasının şematron kontrolü sırasında "gl-bus:totalDebit elemanının değeri gl-bus:totalCredit elemanının değerine eşit olmalıdır" uyarısı neden alınır?**

e-Defter dosyasında bulunan her bir yevmiye fişinin genel borç / alacak toplamı ile bu yevmiye satırlarının toplamları eşit olmalıdır. Bu toplamlarda bir uyuşmazlık olması durumunda bu şematron uyarısı alınabilir. Bunun hızlıca kontrolü Kapatılmamış Fişler raporu ile yapılabilir.

Fiş satır ve toplam borç/alacak bilgisi alınırken çalışan cümle TBLMUPLAN, TBLMUPLANSUBE,TBLMUHMAS ve TBLMUHFIS tablolarının bağlandığı bir cümledir. Tabloların birindeki veri bütünlüğü bozulduğunda cümleden dönen borç / alacak toplamı da hatalı olacaktır. Örneğin TBLMUPLAN tablosunda 120 hesabın AGM sahasının boş olması yada şubesinin 32767 görünmesi bu hesabın geçtiği fişler için **"gl-bus:totalDebit** **elemanının** **değeri** **gl-bus:totalCredit** **elemanının** **değerine** **eşit** **olmalıdır"** uyarısı alınmasına neden olur.

**e-Defter** **dosyasının** **şematron** **kontrolü** **sırasında** **"entryNumberCounter** **müteselsil** **bir** **değere** **sahip** **olmalıdır"** **uyarısı** **neden** **alınır?**

e-Defter dosyasında bulunan her bir yevmiye satırı için satır numarası atanmış olmalı ve bu numaralar sıralı gitmelidir. Aynı zamanda her bir yevmiye fişine madde numarası atanmış olmalı ve bu madde numaraları da tarih bazında sıralı olarak artmış olmalıdır. Aksi durumda **"entryNumberCounter** **müteselsil** **bir** **değere** **sahip** **olmalıdır"** şematron uyarısı alınmaktadır.

TBLMUHFIS tablosunda **SIRA** alanında tutulan satır numaraları, fiş bazında sıralı olarak gitmelidir.

Bu şematron hatası alındığında ilgili dönem için klasik fiş sıralama işlemi tekrar yapılmalıdır.

![](../_assets/dcb5d1cf9c93a1b1e3f4.png)

Müteselsil hatası sıralılık kuralının ihlalinden alınır. Bu nedenle sadece bu kondüsyon değil buna sebep olabilecek birçok kondüsyon vardır.

TBLMUHFIS tablosunda olup TBLMUHFISEK tablosunda olmayan kayıtlar, hata alınan fiş içerisinde, ya da resmi yevmiye madde numarasına göre öncesi veya sonrasındaki yevmiye madde numarasına karşılık gelen fişlerin içerisinde, fiş numarasından farklı evrak tarihli kayıtlar, TBLMUHMAS resmi yevmiye numaralarının tarih bazında sıralı gitmemesi, TBLMUHAS tablosunda TBLMUHFIS tablosunda olmayan kayıtlar.

![](../_assets/8c17366e7303583503ed.png)

**eDefter oluşturma sırasında "gl-cor:postingDate elemanının değeri bir üst düzeydeki gl-cor:enteredDate elemanının değerine eşit olmalıdır." şematron uyarısı neden alınır?**

Fiş tarihi, fiş içerisinde bulunan ilk satırdan alınır. Eğer ilk satırın tarihi diğer satırlardan farklı ise fiş tarihi (enteredDate), kayıt satırlarının tarihi(postingDate) ile farklı oluşur. Buda «gl-cor:postingDate elemanının değeri bir üst düzeydeki gl-cor:enteredDate elemanının değerine eşit olmalıdır.» şematron uyarısına neden olur. Aynı fiş içerisindeki tarihler aynı olmalıdır.

![](../_assets/5886299803ce8c49235e.png)

#### ![](../_assets/99d9808148c55e3680f9.png)

**Kontrol Numarası (uniqueID) (Tekil No)**

Hesap dönemi içerisinde tekil numarası 1 ile başlar ve sıralı olarak devam eder. Ekim defteri oluşturma işleminde alınan uyarıda dönemin(01.09.2020/31.12.2020) ilk defter tekil parça numarasının 1 olmadığı tespit edilip Ekim ayı defterinde uyarı verilmiştir. Eğer hesap dönemi 9. ayda başlıyor ise 9. ayın ilk defterinin tekil parça numarası da 1 olmalıdır.

Bu uyarıda yine tekil numarasından kaynaklanan bir uyarıdır. Defterler gönderildikten sonra GIB tarafından dönen bir durum bilgisidir. Bu uyarıdan defterin dönemi 01.01.2019/31.12.2019 olmasına rağmen parça numarasından ilk defter olduğu görülen defterinin döneminin 10 olmaması gerektiği anlaşılmaktadır. Ya dönem 10 dan başlamalı ya da varsa geçmiş aya ait defterler Netsis'e yükledikten sonra tekil numarasının 10 olarak oluşması sağlanmalıdır.

![](../_assets/0d2b63de8b0d32e492d5.png)

**e-Defter** **işlemlerini** **izleyebileceğimiz,** **hataları** **görebileceğimiz** **bir** **rapor** **var** **mıdır?**

Log Bilgilerini Görüntüle işlemi ile defter uygulaması üzerinde oluşturulmuş, hata alınmış, silinmiş tüm defter bilgileri kullanıcı, bilgisayar ve işlem zamanı bilgileri görüntüler.

![](../_assets/c0fbcf60654b0ba3699d.png)

![](../_assets/46d1ebd9e4004977d994.png)

Defter dönemi içerisinde madde numarası boş olan yevmiye fişlerinin olması durumunda alınan uyarıdır. Madde numaraları fiş bazında TBLMUHMAS tablosunun RESM_YEVMNO sahasında tutulur.

Defter raporu, defter içerisinde işlem görmüş tüm ana hesapları işlem sayısı ve tutarsal olarak özetleyen bir rapordur. Uyarı bu rapordaki tutarların defter içerisinde yer alan muavin hesapların toplamı ile uyumsuz olduğu bilgisini veriyor.

TBLMUPLAN tablosunda ana-grup-muavin tanımlarında var olan sorunlar nedeni ile bu uyarı alınabilir( AGM kolonu null ya da hesap ile uyumsuz AGM verisi, şube kodu 32767 olması, hesabın TBLMUPLANEK tablosunda olmaması vb.)

Farklı bir kondüsyon olarak da TBLMUHFIS tablosunda TARIH defter dönemine uygunken EVRAKTARIHI defter döneminden farklı oluşmuş kayıtlar olabilir. Tam tersi durumlarda geçerlidir. Yani defter dönemine uygun tarihteki bir fiş satırının TARIH kolonun farklı bir ay olması gibi( Dışarıdan alınan kayıtlar, fiş kopyalamalar)

**e-Defter Teknik Rapor Hazırlama Süreci Hakkında Bilgi Alabilir Miyiz?**

Mükellefler tarafından Gelirler İdaresi Başkanlığı'na iletilen iptal talepleri ile ilgili ya da yapılan denetlemelerde ortaya çıkan bazı sorunlarla ilgili olarak uyumlu yazılım firmasının teknik inceleme yapması ve bunu bir rapor halinde kendilerine sunması GİB tarafından talep edilebilir.

Örneğin; e-Defter dosyalarında yaşanan imza uyuşmazlıkları, e-Defter dosyalarının bazı sebeplerden dolayı makinadan silinmesi, zayi olması ve bu dosyaların yedeklerinin bulunmaması, şubeli defter gönderimi yapılması gerekirken şubeler dahil defter gönderilmesi, e-Defter dosyasına eklenmesi gereken kayıtların bulunması, tekil numarasının doğru olmayan bir değer alması. Bu ve benzeri durumlarda GIB tarafından, Logo Yazılım'a teknik inceleme talebi yazılı olarak gönderildikten sonra teknik inceleme raporu tarafımızca oluşturup ıslak imzalı olarak mükelleflere kargo ile gönderilmektedir.
