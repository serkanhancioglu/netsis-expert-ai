---
title: "Detaylı Maliyet Analizi"
page_id: "50679803"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Detaylı Maliyet Analizi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Detaylı Maliyet Analizi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWJmODVjNmNhLTVkMTMtNGI1ZS05ODNmLTNlMmJlMjRjYjViOCZsaW5rPTRjOGZiZmY2LTNlMzgtNGJiMy1hNzUyLTk4MGYyOTU0M2VlYyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=bf85c6ca-5d13-4b5e-983f-3e2be24cb5b8&link=4c8fbff6-3e38-4bb3-a752-980f29543eec&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "detayli-maliyet-analizi_82575773_50679803.html"
source_version: "2022-12-19T11:32:34.410+03:00"
source_bytes: 1025794
fetched_at: "2026-09-13T04:25:49+00:00"
generator: "netsis-scraper 1.0.0"
---
# Detaylı Maliyet Analizi

Detaylı Maliyet Analizi ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

**Detaylı Maliyet** **Analizi** **(Malzeme** **Akışı** **Maliyet** **Muhasebesi)**
Güncelleme Tarihi: 30.01.2018

#### Genel

|  |  |
| --- | --- |
| **Ürün** **Grubu** | \[X\] Netsis 3 Enterprise \[X\] Netsis 3 Standard |
| **Kategori** | \[X\] Yeni Fonksiyon |
| **Modül** | Maliyet Muhasebesi |
| **Versiyon** **Önkoşulu** | 9.0.12 Onaylı Versiyon |
| **Gerekli** **Dosyalar** | 9.0.12 Seti Dosyaları |

Detaylı Maliyet Analizi Genel Uygulama ve Amaç aşağıdaki şekildedir:

- Detaylı maliyet analizi işleminin maliyet hesaplatmaya dahil edilmesi ve ekstra bir işlem olmaktan çıkarılması: Detaylı maliyet analizi işleminin önceki sürümlerde "Maliyet Muhasebesi-İşlemler" menüsü altından ekstra olarak çalıştırılması gerekmekteydi, yeni versiyonla birlikte "Maliyet muhasebesi-Kayıt-Maliyet Hesaplatma" işlemi yapıldığında detaylı maliyet analizine ilişkin sonuçlar da hesaplanmış olacaktır.
- Detaylı maliyet analizi için performans iyileştirmesi
- Detaylı maliyet analizi sonucunda ortaya çıkan gider bilgilerinin reçete seviyeleri bazında raporlanabilmesi. Bir ürünle ilgili rapor alındığında ürünün en alt seviyesine kadar hangi yarı mamullerden kullanım yapıldığı ve hangi seviyelerden ne kadarlık gider taşındığının görülebilmesi.
- Detaylı maliyet analizi sonucunda ortaya çıkan gider bilgilerinin safha bazında görsel olarak gösterimi (MFCA-Material Flow Cost Accounting-Malzeme Akışı Maliyet Muhasebesi).

**Detaylı Maliyet Analizi**

Detaylı maliyet analizi için Maliyet Muhasebesi modülü altından "Maliyet Hesaplatma" işlemi çalıştırılmalıdır. Ortaya çıkan sonuçları inceleyebilmek için "Maliyet Muhasebesi-Kayıt-Maliyet Bilgi Girişi" ekranındaki "Detaylı Maliyet Analizi" sekmesi kullanılabilir. Ayrıca sonuçları rapor formatında alabilmek için "Maliyet Muhasebesi \> Rapor \> Detaylı Maliyet Analiz Raporu" kullanılabilir.
![](../_assets/5ed53aafdb44ca13d055.png)
Maliyet girişi sekmesinden herhangi bir kayıt seçilerek "Detaylı Maliyet Analizi" sekmesine geçildiğinde ilgili mamul grup kodu ve ay için detaylı maliyet analizi raporlanmaktadır.

Ekranın sol üst bölümündeki akış diyagramında mamul ana grupları (üretim safhaları) arasındaki aylık toplam gider akışları görülebilir. Bu diyagramdaki okların yönü ve üzerinde yazan tutarlar, safhalar arasında gerçekleşen gider akışını ve toplam tutarları göstermektedir. Okların üzerindeki tutar bilgisine mouse ile gelindiğinde tutarın detayı görülmektedir. Gider tutarlarının büyüklüğüne orantılı olarak ok kalınlıkları da büyümektedir. Öte yandan diyagram üzerindeki dikdörtgen kutular da mamul ana gruplarını (üretim safhalarını) göstermektedir. Bu görsel sayesinde incelenen mamul grubunun en alt seviyelerinden itibaren hangi maul ana gruplarından (safhalardan) geçtiği ve bu geçişler sırasında ne kadarlık bir toplam gider tutarı taşıdığı raporlanabilmektedir. Rapor ilk açıldığında gösterilen tutarlar, bütün gider çeşitlerinin toplamını göstermektedir. (işçilik+enerji+amortisman gibi)

Ekranın sağ üst bölümünde seçilen mamul grup kodu için toplam gider yüzdeleri gösterilmektedir. Bu gider yüzdeleri mamul grubuna alt safhalardan nakil olarak gelen giderleri de içermektedir. Pasta grafiği üzerinde herhangi bir gider kodunun üzerine gelerek, bu gider koduyla ilgili ayrıntıya ulaşılabilir. Ayrıntı bilgi olarak "mamülün kendi safhasında harcadığı gider tutarını" ve "alt safhalardan nakil olan toplam gider tutarını" görmek mümkündür.

Ekranın alt bölümünde Gider Akış Detayı ve Ana Grup Detayı olmak üzere iki sekmeden oluşan bir grid bulunmaktadır:

**Gider Akış Detayı:** Gider akış diyagramındaki akış tutarlarının ayrıntısı bu sekme üzerinden görülebilir. Örneğin hangi ana safhalar arasında işçilik giderinin ne şekilde aktarıldığını görebilmek için "Gider Kodu" kolonuna "Toplam İşçilik" kısıtı verilebilir.

**Ana Grup Detayı:** Akış diyagramında yer alan mamul ana gruplarında üretilen mamul grup kodlarının detayı bu sekme üzerinden raporlanabilir.

Gider yüzdelerini gösteren pasta grafiğindeki giderlerden biri üzerine tıklandığında ilgili giderin toplam akış tutarları diyagram üzerinde gösterilir. Ayrıca alt bölümdeki grid üzerinde "Gider Akış Detayı" sekmesi aktif hale gelir ve seçilen gider kodu için filtre verilir.
![](../_assets/fb8e646ee73d4e3c32b1.png)
Gider akış diyagramında gösterilen mamul ana gruplarından birine tıklandığında, alt bölümdeki grid üzerinde 'Ana Grup Detayı' sekmesi aktif hale gelir ve ilgili ana grupta işlem göre mamul grup kodları filtrelenir. Bu grid üzerinde mamul grup koduna ait detaylı maliyet bilgileri raporlanabilir. Bu bilgilerin açıklamasını işçilik gideri üzerinden örneklemeye çalışırsak aşağıdaki gibi açıklanabilir:
![](../_assets/1f6c1e808b6a6f75e7e8.png)
**İşçilik:** Mamul grup kodunun üretildiği mamul ana grubundaki işçilik giderinden aldığı toplam tutardır. Örneğin yukarıdaki ekran görüntüsünde MAMUL1 ürünü için, MAMUL1'in üretildiği ana gruptaki toplam işçilik giderinin 4000 TL'lik kısmı harcanmıştır.
**Nakil Gelen İşçilik:** Mamul grup koduna sarf ettiği bileşenlerden dolayı nakil olarak gelen toplam işçilik tutarıdır. Örneğin MAMUL1'in YARIMAMUL1 sarf ettiği, YARIMAMUL1'in de YARIMAMUL2'yi sarf ettiğini düşünelim. Aynı zamanda bütün bu ürünlerin farklı mamul ana gruplarında üretildiğini düşünelim. Öncelikle YARIMAMUL1 üretilecektir ve YARIMAMUL1 kendi üretim safhasındaki işçilik giderinin belli oranını üzerine alacaktır. YARIMAMUL2 üretiminde YARIMAMUL1 sarf edildiği için, YARIMAMUL1'in taşıdığı işçilik gideri YARIMAMUL2'ye nakil olacaktır.
YARIMAMUL2 de kendi mamul ana grubundaki toplam işçilik tutarının belli bir miktarını üzerine alacaktır. Böylece YARIMAMUL1'den gelen nakil işçilik tutarı ve YARIMAMUL2'nin kendi ana grubundaki işçilik gideri toplanarak, MAMUL1 üzerine nakil olacaktır. Bu tutar grid üzerinde "Nakil Gelen İşçilik" olarak gösterilecektir.
**Nakil Giden İşçilik:** Mamul grup kodunun, sarf edildiği mamul gruplarına aktarmış olduğu ve sadece kendi ana grubundan pay aldığı toplam işçilik tutarıdır. Yukarıdaki örnekten yola çıkarsak YARIMAMUL2'nin kendi safhasındaki işçilik giderinden pay aldığı ve MAMUL1 üzerine nakil ettiği tutarı "Nakil Giden İşçilik" olarak tanımlayabiliriz. YARIMAMUL2'ye bir alt seviyedeki YARIMAMUL1 üzerinden nakil olan işçilik tutarı, nakil giden işçiliğe dahil değildir.
**Toplam Nakil Giden İşçilik:** Mamul grup kodunun, sarf edildiği mamul gruplarına aktarmış olduğu toplam işçilik tutarıdır. Mamul grup kodunun kendi ana grubunda pay almış olduğu
işçilik tutarına ek olarak, sarf ettiği alt seviyedeki bileşenlerden nakil gelen işçilik tutarları da dahil edilir. Yukarıdaki örnekten yola çıkarsak YARIMAMUL2'nin kendi safhasındaki işçilik giderinden pay aldığı tutar ve alt seviyelerden YARIMAMUL2'ye nakil gelen işçilik giderlerinin toplamı, daha üst seviyedeki ürün gruplarına sarf olarak aktarıldığında "Toplam Nakil Giden İşçilik" olarak adlandırılmaktadır.
Gider Akış Diyagramının sağ alt köşesinde yer alan butonlar yardımıyla aşağıdaki fonksiyonlar kullanılabilir.

| Buton | Fonksiyon |
| --- | --- |
| Kaydet ![](../_assets/77e24bd095bfc72f8b35.png) | Ekrandaki akış diyagramını jpeg formatıyla resim olarak kaydeder. |
| Uzaklaştır ![](../_assets/de3ed9ada4a9646d3ac9.png) | Ekrandaki akış diyagramından uzaklaşıp görüntüyü küçültmek için kullanılır. |
| Yakınlaştır ![](../_assets/0d9db83139be2ce18568.png) | Ekrandaki akış diyagramına yaklaşıp görüntüyü büyütmek için kullanılır. |
| ![](../_assets/9a7b41728312277b2a27.png) Yenile | Ekrandaki akış diyagramını yenileyip raporun ilk haline dönülmesini sağlar. |
| ![](../_assets/7c48b480af9ecbe77874.png) Renklendir | Akış diyagramında görünen gider türlerinin ve mamul ana gruplarının renklerinin özel olarak seçilebilmesini sağlar. |

"Renk Ayarları" butonuna tıklandığı zaman aşağıdaki gibi bir ekran açılmaktadır. Bu ekran üzerinden giderler veya mamul ana grupları için renk seçimi yapılabilmektedir ve bu seçimler saklanarak daha sonra alınacak raporlarda kullanılmaktadır.
![](../_assets/3057220c784ccdc98bea.png)

#### Örnek Uygulama

Aşağıdaki gibi bir reçeteye sahip olan mamulün ve altındaki yarı mamullerin ana grup kodları ve mamul grup kodları aşağıdaki gibidir:
![](../_assets/d514dbf2143af519b8dd.png)

| **Stok** **Kodu** | **Mamul** **Grup** **Kodu** | **Mamul** **Ana** **Grup** **Kodu** |
| --- | --- | --- |
| MAMUL40 | MAMUL40 | MONTAJ |
| YARIMAMUL20 | YARIMAMUL20 | CNC |
| YARIMAMUL30 | YARIMAMUL30 | PRESHANE |
| YARIMAMUL40 | YARIMAMUL40 | BOYAHANE |

Bu ürünler için Şubat/2018 ayında aşağıdaki üretimler yapılmıştır. Sırasıyla "Stok modülü-Maliyet oluşturma" ve "Maliyet muhasebesi modülü-Maliyet oluşturma" çalıştırılmıştır. Bu örnek üzerinde işçilik giderleri üzerinden gidilirse, maliyet hesaplatma sonrasında mamul gruplarına ait işçilik gider bilgileri aşağıdaki gibi oluşmaktadır:

| **Stok** **Kodu** | **Üretim** **Miktarı** | **Aylık** **Toplam** **İşçilik** **Tutarı** |
| --- | --- | --- |
| MAMUL40 | 100 | 4000 |
| YARIMAMUL20 | 200 | 3000 |
| YARIMAMUL30 | 200 | 3000 |
| YARIMAMUL40 | 100 | 3000 |

Bu şartlar altında maliyet bilgi girişi ekranında "detaylı maliyet analizi" sekmesine geçildiğinde aşağıdaki sonuçlar görülmektedir:
![](../_assets/b976425f6eafb63db599.png)
En alt seviyedeki YARIMAMUL30'a ait detay satırı işçilik gideri için incelendiğinde şu bilgiler görülmektedir:

- İşçilik : 3000 TL-YARIMAMUL30 Şubat ayında kendi ana grubundaki toplam işçilik tutarının 3000 TL'lik kısmını harcamıştır. Bu sonuç maliyet muhasebesi tarafından hesaplanmaktadır.

- Nakil Gelen İşçilik: 0 TL-YARIMAMUL30 sadece hammadde sarf ettiği için üzerine alt seviyelerden nakil gelen bir işçilik tutarı yoktur.
- Nakil Giden İşçilik: 3000 TL-YARIMAMUL30 Şubat ayında 200 adet üretilmiştir ve bu üretimin tamamı bir üst seviyedeki YARIMAMUL20 tarafından sarf edilmiştir, çünkü YARIMAMUL20'nin Şubat ayındaki üretim miktarı da 200 adettir. Bu durumda YARIMAMUL30'un kendi safhasında harcadığı işçilik giderinin tamamı (3000TL) nakil giden işçilik olarak hesaplanmıştır.
- Toplam Nakil Giden İşçilik: 3000 TL-YARIMAMUL30 üzerine alt seviyelerden nakil gelen işçilik olmadığı için toplam nakil giden işçilik tutarı, nakil giden işçilik tutarına eşittir.

YARIMAMUL30'un bir üst seviyesindeki YARIMAMUL20 incelendiğinde aşağıdaki sonuçlar görülmektedir:

- İşçilik : 3000 TL-YARIMAMUL20 Şubat ayında kendi ana grubundaki toplam işçilik tutarının 3000 TL'lik kısmını harcamıştır. Bu sonuç maliyet muhasebesi tarafından hesaplanmaktadır.

- Nakil Gelen İşçilik: 3000 TL-YARIMAMUL20 Şubat ayında 200 adet üretilmiştir ve bu aşamada 200 adetlik YARIMAMUL30 sarfı yapmıştır. YARIMAMUL30 üzerinden 3000 TL'lik işçilik gideri nakil gelmektedir.
- Nakil Giden İşçilik: 3000 TL-YARIMAMUL20 Şubat ayında 200 adet üretilmiştir ve fakat bu üretimin sadece 100 adetlik kısmı bir üst seviyedeki MAMUL40 tarafından sarf edilmiştir, çünkü MAMUL40'ın Şubat ayındaki üretim miktarı 100 adettir. Bu durumda YARIMAMUL20'un kendi safhasında harcadığı işçilik giderinin sadece yarısı (1500TL) nakil giden işçilik olarak hesaplanmıştır.

- Toplam Nakil Giden İşçilik:1500 TL-YARIMAMUL20 kendi safhasında harcadığı 1500 TL'lik işçilik tutarını nakil giden işçilik olarak aktarırken, aynı zamanda YARIMAMUL30 üzerinden gelen 3000TL'lik nakil gelen işçiliğin de 1500 TL'sini MAMUL40 üzerine aktarmaktadır. Bu yüzden toplam nakil giden işçilik 3000TL (1500+1500) olarak hesaplanmaktadır

#### Detaylı Maliyet Analiz Raporu

"Maliyet muhasebesi-Kayıt-Maliyet Hesaplatma" işlemi sonrasında detaylı maliyet analizine ilişkin sonuçlar da kaydedilmektedir. Bu sonuçları üretim seviyelerini de gösterecek şekilde raporlayabilmek için "Maliyet Muhasebesi-Raporlar-Detaylı Maliyet Analiz Raporu" kullanılabilir.
![](../_assets/ff68a83f21b0c7ee65a3.png)
Bu rapordaki başlıkların açıklamaları ve formülasyonları aşağıdaki gibidir:

- **Nakil Gider Tutarı:** Mamul grubunun ilgili ayda alt seviyelerden yaptığı yarı mamul sarflarından nakil gelen toplam gider tutarıdır. (Örneğin Nakil İşçilik Tutarı)

- **Gider** **Tutarı:** Mamul grubunun ilgili ayda kendi safhasından pay aldığı toplam gider tutarıdır. (Örneğin İşçilik Tutarı)
- **Gider** **Ortalaması:** Mamulün kendi safhasında yaptığı giderin ortalama birim tutarıdır. Bu hesaplama sırasında bir önceki aydan gelen devir bakiye ve mamulün bir önceki ayda hesaplanmış olan gider ortalaması da dikkate alınır. (Örneğin İşçilik Ortalaması)
- **Formülasyon:** (Maliyetin hesaplandığı aydaki mamulün kendi seviyesindeki toplam işçilik tutarı + bir önceki aydan gelen mamulün kendi seviyesindeki toplam işçilik tutarı)/(Maliyetin hesaplandığı aydaki üretim miktarı+Bir önceki aydan gelen devir bakiye)
- **Nakil Gider Ortalaması:** Alt seviyelerden sarf edilen bütün yarı mamullerden gelen ortalama birim nakil gider tutarıdır. Bu hesaplama sırasında bir önceki ayda hesaplanmış olan nakil gider ortalaması da dikkate alınır. (Örneğin Nakil İşçilik Ortalaması)
- **Formülasyon:** ((Bir önceki ayın devir bakiyesi\*bir önceki ayın nakil gider ortalaması)+Bu aydaki nakil gider tutarı)/(Bir önceki aydan gelen devir bakiye+bu aydaki üretim miktarı)
