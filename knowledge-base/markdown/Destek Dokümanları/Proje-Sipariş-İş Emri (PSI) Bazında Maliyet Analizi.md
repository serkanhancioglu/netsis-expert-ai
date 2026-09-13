---
title: "Proje-Sipariş-İş Emri (PSI) Bazında Maliyet Analizi"
page_id: "50680104"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Proje-Sipariş-İş Emri (PSI) Bazında Maliyet Analizi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Proje-Sipariş-İş Emri (PSI) Bazında Maliyet Analizi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTM2YzQ0NmM4LTE2ZGYtNGNlYi05ZjM1LWQxOWZiMDEwZDFmYiZsaW5rPTE4MjdiMDNmLWYzOWQtNDAzMC05MWQ2LWFmYjEyOTc4ZWIwOCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=36c446c8-16df-4ceb-9f35-d19fb010d1fb&link=1827b03f-f39d-4030-91d6-afb12978eb08&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "proje-siparis-is-emri-psi-bazinda-maliyet-analizi_82576546_50680104.html"
source_version: "2022-11-03T09:48:09.370+03:00"
source_bytes: 1890705
fetched_at: "2026-09-13T04:26:12+00:00"
generator: "netsis-scraper 1.0.0"
---
# Proje-Sipariş-İş Emri (PSI) Bazında Maliyet Analizi

Proje-Sipariş-İş Emri (PSI) Bazında Maliyet Analizi ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

|  |  |
| --- | --- |
| **Amaç ve** **Fayda** | Bilindiği gibi mamul maliyetleri direkt hammadde (direkt ilk madde ve ambalaj), direkt işçilik ve genel üretim giderlerinden oluşmaktadır. Proje/Sipariş/İş Emri (PSI) bazında maliyet analizi kapsamında; proje, sipariş veya iş emri bazında maliyetler yeni geliştirilen yaklaşım metoduyla mevcut maliyet değerleri üzerinden izlenebilmesi sağlanmıştır.<br>PSI bazında maliyet analizinin müşterilerimizin ihtiyaçları olan maliyet bilgilerinin proje, sipariş veya iş emri bazında da temin edilebilmesi konusunda önemli bir araç olması hedeflenmiştir. PSI bazında maliyet analizi, mevcut maliyet muhasebesi sisteminin bir parçası olarak, tüm maliyet merkezlerini kapsayacak şekilde proje, sipariş veya iş emri maliyetlerini tespit etmenize, karlılık hesaplamalarının daha doğru yapılmasına ve ileriye dönük stratejik kararların daha güvenli alınabilmesine yardımcı olur.<br>Bu noktada müşterilerimizin hassasiyetleri göz önünde bulundurularak mümkün olduğu kadar hızlı çalışan bir yapı tasarlandı. Netsis kullanıcıları oluşturdukları analizleri dışarı veri aktarımı ile Excel entegrasyonu veya e-posta yoluyla birbirleriyle paylaşma imkânına da sahip olacaklar. |
| **Ürün** **Grubu** | \[X\] Netsis Enterprise<br>\[X\] Netsis Standard |
| **Modül** | \[X\] Maliyet Muhasebesi |
| **Kategori** | \[X\] Yeni Fonksiyon |
| **Kısaltmalar** | PSI: Proje Sipariş İş Emri |
| **Versiyon** **Önkoşulu** | 7.0.0 |

Proje, sipariş ve iş emri (PSI) bazında maliyet analizi, mevcut maliyet oluşturma ve detaylı maliyet analizi sonucunda oluşan değerler üzerinden yeni bir yaklaşım yöntemiyle oluşturulması sağlanmıştır. PSI bazında maliyet analizi sonucunda yarı mamul ve mamul maliyetleri izlenebilip; sarf detayları da bu perspektifte incelenebilmektedir.

PSI bazında maliyet analizi; satılan malın maliyeti göz önünde bulundurularak oluşmaktadır. Yapılan analiz sonucunda üretim aşamasında, ilk madde ve ambalajlar (sarflar) yaklaşımıyla; satış aşamasında ise PSI için mamul ürünler (yan ürün-yarı mamul-mamul) detaylarıyla ele alınmaktadır.

Netsis Maliyet Muhasebesinde, bilindiği gibi mamul maliyetleri, hammadde, işçilik, amortisman, enerji, yarı mamul gibi yaklaşık 12 unsurdan meydana gelen detaylar bazında hesaplanır. Mamulün maliyetinin içinde ne kadar işçilik olduğu bilgisi detaylı maliyet analizi ile tespit edilebilmektedir. Detaylı Maliyet Oluşturma çalıştırıldığında, program tarafından mamul/yarı mamul maliyet kartlarında oluşan yarı mamul sarflarının detayları ve aynı zamanda ortalama maliyet değerleri, maliyet kalemi bazında takip edilebilmektedir. Yani, eldeki değeri 100 birim olan bir mamulün ne kadarlık kısmının işçilik, hammadde, enerji ve amortisman olduğu gibi sorulara cevap bulunabilmektedir.
PSI analizinde detaylı maliyet oluşturma sonucunda oluşan bilgileri kullanarak aşağıda anlatılan yaklaşım metodu ile proje, sipariş veya iş emrinin maliyetlerini tespit etmeye çalışmaktadır.
Analiz çalışmasında öncelikle PSI için verilen aralıktaki mamul grupları tespit edilip bunlar için kullanılan hammaddeler, mamul veya yarı mamullerin birbirlerine olan sarfları tespit edilip bunların PSI bazında bakiye bilgilerine ulaşılmaktadır. Yaklaşım metodu da tespit edilen bu bakiyeler üzerinden çalışmaktadır.
PSI maliyeti hesaplanırken tespit edilen mamullerin öncelikle hammaddeleri bazında stok maliyet oluşturma sonucunda oluşan maliyetleri hesaplanır.
Daha sonrada bakiye tablosundaki miktarlarla, mamulün veya yarı mamulün detaylı maliyet oluşturma sonucunda oluşan kendi seviyesindeki hammadde giderleri ortalaması (HAMORT) ile ilgili dönemin yarı mamul ortalama fiyatlarının maliyet cinslerinden değeri (o ayki nakil hammadde giderleri ortalaması -OAYNAKHAMORT) toplamı çarpılarak bakiyenin + veya – olmasına göre düşülür veya eklenir. Bu yöntem ile proje, sipariş veya iş emrinin yaklaşık maliyetine ulaşılır.
Bu yaklaşım metodunda ön koşul olarak kısıt olarak verilen PSI bazındaki mamullerin satış miktarlarının olması beklenmektedir. Eğer satış miktarı yok ise yaklaşım metodumuz PSI bazında hammadde maliyetleri ile detaylı maliyetten gelecek olan ortalama maliyet değerleri birbirini karşılayacağı için sıfır hesaplanacaktır.
Ambalaj maliyetlerinin hesaplama işleyişi de hammadde maliyet hesabına paralel olarak yürütülmektedir.
Diğer maliyet değerlerinin hesaplama sürecinde de mamul grupların satış miktarları kullanılacaktır. Maliyet türlerine ait ortalama maliyet değerleri de detaylı maliyet analizi sonucunda oluşan veriler kullanılarak tespit edilecektir.
Sonuç olarak rapor incelendiğinde maliyet kalemi bazında bakiye ve satış miktarları ele alınarak proje, iş emri veya sipariş bazında oluşan hammadde, işçilik, enerji, amortisman, yardımcı servis gider ve yedek parça gider maliyet değerlerinin ne olduğu gibi sorulara cevap bulunabilecektir.
Bu bölümde proje bazında maliyet analizine yönelik örnek bir senaryo üzerinden işleyiş anlatılacaktır. Üretim sürecindeki hammadde, yarı mamul ve mamullerin işlem akışı aşağıdaki gibidir:

M1 (Mamul1)

```text
          Y1 (Yarı Mamul1)
```

```text
                      H1 (Hammadde1) H2 (Hammadde2)
```

H3 (Hammadde3)

Üretim süresince oluşan sarf durumu aşağıda özetlenmiştir. Yukarıda belirtilen tabloda yarı mamul üretimi için kullanılan hammaddeler, üretilen yarı mamulün ana mamullerin üretiminde kullanılması durumu ele alınmıştır. Analiz süreci çalıştırıldığında sarf, üretim, satış miktarları göz önünde bulundurularak verilen PSI bazında mamul gruplar incelenip; bakiye durumları tespit edilecektir.
Örnek senaryomuzda ön kontrol sonrasında oluşması beklenen bakiye tablosu aşağıdaki şekilde oluşacaktır:

| **STOK**<br>**KODU** | **PROJE** **KODU** | **GİRİŞ** **MİK.** | **SATIŞ** **MİK.** | **ÇIKIŞ** **MİK.** | BAKİYE | **HAMORT +**<br>**OAYNAKHAMORT** |
| --- | --- | --- | --- | --- | --- | --- |
| **Y1** | **01** | **10** | **0** | **5** | **5** | **2** |
| **M1** | **01** | **5** | **1** | **0** | **4** | **3** |

Sonrasındaki süreçte hammadde maliyetlerinin hesaplama yöntemini incelersek:

- Ham maddelerin stok hareket birim fiyatlarının 1 TL olduğu varsayıldığında Y1 için ham madde maliyeti ( 1 × 20 ) 20 TL dir. Benzer hesaplama ile M1 in hammadde maliyetide 20 + (1 x 5) 25 TL dir.
- Üretim sonucunda oluşan yarı mamul, yan ve mamul ürünlerin bakiyesi **pozitif olduğunda** tespit edilen maliyet değeri üzerinden (son hesaplanan tarih itibariyle detaylı maliyet analiz verileri kullanılarak) azalma gerçekleştirilecektir. Diğer bir durum olan bakiyenin eksi olması halinde ise ekleme işlemi gerçekleşecektir.

Örneğimizde **(HAMORT+OAYNAKHAMORT)** toplamının 3 TL olması beklenmektedir. Bu durumda hammadde maliyeti satılan malın maliyeti bakış açısı ile, 25 TL – ( 5 × 2 ) – ( 4 × 3 ) = 3 TL şeklinde hesaplanacaktır.

**Kısıtlar**
Kısıtlar bölümünde kısıt kodu aralığı ve eski yıl şirket kayıtlarının analiz kapsamına dâhili seçimleri yapılabilecektir. Çalıştır işlemi ile analiz yeniden çalıştırılacaktır. Daha önce oluşturulan rapor var ise mevcut rapor seçeneği ile izlenebilecektir. Görüntüle işlemi ile mevcut maliyet analiz dosya içeriği incelenebilecektir.

| **SARF** **STOK** **KODU** | **SARF** **MİKTAR** | **ÜRETİM STOK** **KODU** | **ÜRETİM** **MİKTAR** | **PROJE** **KODU** |
| --- | --- | --- | --- | --- |
| **H1** | **10** | **Y1** | **10** | **01** |
| **H2** | **10** |  |  |  |
| **Y1** | **5** | **M1** | **5** | **01** |
| **H3** | **5** |  |  |  |

![](../_assets/7f98538b059d037c5367.png)![](../_assets/92abb0dd9738d37dded3.png)![](../_assets/a204c59d785463d2fe68.png)
Kısıtlar bölümünde yapılan seçimler, kullanıcı bazında saklanmaktadır. Bu sayede sonraki kullanımlarda daha önce yapılan seçimler, sistem tarafından kullanıcıya sunulabilecektir.

#### Rapor

Raporun hazırlanması sürecindeki adımlar, işleyişin hangi aşamada olduğu ve ne kadar sürede tamamlandığına dair bilgiler, yardımcı ekran vasıtasıyla takip edilebilecektir.
Rapor ekranında öncelikle genel hatları ile PSI bilgileri yer almaktadır. Sütun bölümünde görüntülenen ikonlar yardımı ile ilgili sütun üzerinde sıralama yapılabilmektedir. Sağ bölümde yer alan Microsoft Excel dışarı veri aktarım grafik ikonu ile bulunduğu satır itibariyle bağlı olduğu bölüm için aktarım sağlanabilecektir.
![](../_assets/c1f1fae5a3436a37a519.png)![](../_assets/34af2292a2015c451d82.png)

Detay bölümünde ise projenin alt maliyet analiz bilgileri bulunmaktadır.
PSI detayında hammadde sarf özeti ve maliyet özeti başlıkları yer almaktadır. Hammadde sarf özeti, mamul grupların PSI bazında giriş, çıkış, satış miktarları ve bakiye takibinin izlenebileceği bir bölüm olmak ile birlikte istenen mamul grupların hammadde sarf detaylarının da gözlemlenebileceği bir bölüm olarak kullanılabilecektir.
PSI bazında maliyet özeti ise analiz karakterinin genel olarak maliyet türlerine uygun şekilde dağılımı görüntülenmektedir. Bu bölümde PSI bazında tespit edilen maliyetler, mamul gruplar detayında izlenebilecektir.

#### E-Posta Gönderimi-Görüntüleme

PSI bazında maliyet bilgileri e-posta yardımı ile Netsis kullanıcıları arasında paylaşılabilmektedir. E-posta gönderim seçeneği ile PSI maliyet analiz bilgileri ek dosya olarak seçilen kullanıcılara iletilecektir. Bize ulaşan ek dosya, PSI maliyet analiz bölümünde görüntüleme işlemi ile izlenebilecektir. Dosya boyutu, 10 MB'ı aştığında sistem tarafından NETZIP uzantısı ile sıkıştırılarak kullanıcılara iletilmektedir. Bu şekilde gelen dosya açılmak istendiğinde aşağıdaki şekilde olduğu gibi sürükle-bırak veya dosya seçim yöntemleriyle görüntüleme işlemi gerçekleştirilebilecektir.
![](../_assets/88e3d12be74fb9931f7c.png)![](../_assets/f421e387558e3025d826.png)![](../_assets/b9fdf09b21752a69a6c2.png)
Dosya ekran üzerine bırakıldığında içeriği sistem tarafından kullanıcıya görüntülenecektir. 10 MB dosya büyüklüğünü aşmayan maliyet analiz dosyaları, HTML uzantısı ile kullanıcılara iletilecektir. Bu şekilde alınan ek dosyalar, mevcut bir tarayıcı (browser) yardımı ile izlenebilecektir.

#### Dışarı Veri Aktarımı

PSI bazında maliyet özeti aktarımı yapılmak istendiğinde mevcut örnekte aşağıdaki şekilde aktarım gerçekleştirilebilecektir. PSI bazında mamul grup bakiye ve hammadde sarf özeti bilgileri bir arada aktarım yapılabilecektir.
![](../_assets/34682f30c1aa845b9eee.png)![](../_assets/f140f50016ae5dfc834f.png)![](../_assets/d428f52270040fdfe0de.png)![](../_assets/86475616f29b33266662.png)![](../_assets/5eb335ad85595f6b5d0f.png)

Bununla birlikte PSI bazında bütün detay analiz rapor bilgileri aktarımı da yapılabilecektir.
