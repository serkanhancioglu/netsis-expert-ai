---
title: "PSI Bazında Maliyet Analizi"
page_id: "24752292"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Muhasebe"
  - "Maliyet Muhasebesi"
  - "Raporlar / Maliyet Muhasebesi"
  - "PSI Bazında Maliyet Analizi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Maliyet Muhasebesi / Raporlar / Maliyet Muhasebesi / PSI Bazında Maliyet Analizi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWM4Nzk1OTk1LTY1ZDgtNDhjNi1iZTExLTNkY2E2N2FkMzEyMyZsaW5rPWMyYzE1OWY0LTlkYTMtNDAyMS04NjY1LWQ0ZjM4MzQ5YjU1YSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=c8795995-65d8-48c6-be11-3dca67ad3123&link=c2c159f4-9da3-4021-8665-d4f38349b55a&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "psi-bazinda-maliyet-analizi_50677519_24752292.html"
source_version: "2022-10-18T13:43:36.747+03:00"
source_bytes: 13202
fetched_at: "2026-09-13T04:15:11+00:00"
generator: "netsis-scraper 1.0.0"
---
# PSI Bazında Maliyet Analizi

PSI Bazında Maliyet Analizi, Muhasebe Bölümünde, "Raporlar/Maliyet Muhasebesi Modülü" menüsünün altında yer alır. Proje, sipariş ve iş emri (PSI) bazında maliyet analizinin, mevcut maliyet oluşturma ve detaylı maliyet analizi sonucunda oluşan değerler üzerinden yeni bir yaklaşım yöntemiyle oluşturulması sağlandı. PSI Bazında Maliyet Analizi sonucu, yarı mamul ve mamul maliyetleri izlenip, sarf detaylarının da incelenmesi sağlanır.

PSI Bazında Maliyet Analizi, satılan malın maliyeti göz önünde bulundurularak oluşur. Yapılan analiz sonucu Üretim aşamasında ilk madde ve ambalajlar (Sarflar) yaklaşımıyla, Satış aşamasında ise PSI için mamul ürünler (Yan ürün-yarı mamul-mamul) detaylarıyla ele alınır.

Maliyet Muhasebesi'nde mamul maliyetleri; hammadde, işçilik, amortisman, enerji, yarı mamul gibi yaklaşık 12 unsurdan meydana gelen detaylar bazında hesaplanır. Mamul maliyetinin içinde ne kadar işçilik olduğu bilgisi detaylı maliyet analizi ile tespit edilir.

Detaylı Maliyet Oluşturma çalıştırıldığında, program tarafından mamul/yarı mamul maliyet kartlarında oluşan yarı mamul sarflarının detayları ve aynı zamanda ortalama maliyet değerleri, maliyet kalemi bazında takip edilir. Yani, eldeki değeri 100 birim olan bir mamulün ne kadarlık kısmının işçilik, hammadde, enerji ve amortisman olduğu gibi sorulara yanıt olur.

PSI analizi, Detaylı Maliyet Oluşturma sonucunda oluşan bilgileri kullanarak aşağıda yer alan yaklaşım metodu ile; proje, sipariş veya iş emrinin maliyetlerini tespit etmeye çalışır.

Analiz çalışmasında öncelikle PSI için verilen aralıktaki mamul grupları tespit edilip daha sonra bunlar için kullanılan hammaddeler, mamul veya yarı mamullerin birbirlerine olan sarfları tespit edilip, bunların PSI bazında bakiye bilgilerine ulaşılır. Yaklaşım metodu da tespit edilen bu bakiyeler üzerinden çalışır. PSI maliyeti hesaplanırken tespit edilen mamullerin öncelikle hammaddeler bazında stok maliyet oluşturma sonucunda oluşan maliyetleri hesaplanır. Daha sonra da Bakiye tablosundaki miktarlarla, mamulün veya yarı mamulün Detaylı Maliyet Oluşturma sonucu oluşan kendi seviyesindeki Hammadde Giderleri Ortalaması (HAMORT) ile ilgili dönemin yarı mamul ortalama fiyatlarının maliyet cinsinden değeri - ilgili aya ait nakil hammadde giderleri ortalaması (OAYNAKHAMORT) - toplamı çarpılarak bakiyenin + veya – olmasına göre düşülür veya eklenir. Bu yöntem ile proje, sipariş veya iş emrinin yaklaşık maliyetine ulaşılır. Bu yaklaşım metodunda ön koşul olarak, kısıt verilen PSI bazındaki mamullerin satış miktarlarının olması beklenir. Eğer satış miktarı yoksa, yaklaşım metodu PSI bazında hammadde maliyetleri ile detaylı maliyetten gelecek ortalama maliyet değerleri birbirini karşılayacağı için sıfır olarak hesaplanır.

Ambalaj maliyetlerinin hesaplama işleyişi de hammadde maliyet hesabına paralel olarak yürütülür. Diğer maliyet değerlerinin hesaplama sürecinde de mamul grupların satış miktarları kullanılır. Maliyet türlerine ait ortalama maliyet değerleri de Detaylı Maliyet Analizi sonucu oluşan veriler kullanılarak tespit edilir. Sonuç olarak rapor incelendiğinde, maliyet kalemi bazında bakiye ve satış miktarları ele alınarak proje, iş emri veya sipariş bazında oluşan hammadde, işçilik, enerji, amortisman, yardımcı servis gider ve yedek parça gider maliyet değerlerinin ne olduğu gibi sorulara cevap bulunur.

Proje bazında maliyet analizine yönelik örnek bir senaryo üzerinden işleyişten bahsedilecek olunursa, Üretim sürecindeki hammadde, yarı mamul ve mamullerin işlem akışı aşağıdaki gibidir:

M1 ( Mamul1 )
Y1 ( Yarı Mamul1 )
H1 ( Hammadde1 )
H2 ( Hammadde2 )
H3 ( Hammadde3 )

Üretim süresince oluşan sarf durumu aşağıda özetlenmiştir:

| Sarf Stok Kodu | Sarf Miktar | Üretim Stok Kodu | Üretim Miktar | Proje Kodu |
| --- | --- | --- | --- | --- |
| H1 H2 | 10 10 | Y1 | 10 | 01 |
| Y1 H3 | 5 5 | M1 | 5 | 01 |

Yukarıda belirtilen tabloda yarı mamul üretimi için kullanılan hammaddeler; üretilen yarı mamulün ana mamullerin üretimde kullanılması durumu ele alınmıştır. Analiz süreci çalıştırıldığında çalıştırıldığında sarf, üretim, satış miktarları göz önünde bulundurularak verilen PSI bazında mamul grupları incelenip, bakiye durumları tespit edilir.

Örnek senaryoda ön kontrol sonrası oluşması beklenen bakiye tablosu aşağıdaki şekilde oluşur:

| Stok Kodu | Proje Kodu | Giriş Miktarı | Satış Miktarı | Çıkış Miktarı | Bakiye | HAMORT + OAYNAKHAMORT |
| --- | --- | --- | --- | --- | --- | --- |
| Y1 | 01 | 10 | 0 | 5 | 5 | 2 |
| M1 | 01 | 5 | 1 | 0 | 4 | 3 |

Sonraki süreçte hammadde maliyetlerinin hesaplama yöntemi incelendiğinde hesaplama aşağıdaki şekildedir:

- Ham maddelerin stok hareket birim fiyatlarının 1 TL olduğu varsayıldığında, Y1 için hammadde maliyeti ( 1 × 20 ) 20 TL'dir. Benzer hesaplama ile M1'in hammadde maliyeti de 20 + (1 x 5) 25 TL'dir.
- Üretim sonucu oluşan yarı mamul, yan ve mamul ürünlerin bakiyesi pozitif olduğunda tespit edilen maliyet değeri üzerinden - son hesaplanan tarih itibariyle detaylı maliyet analiz verileri kullanılarak - azalma gerçekleştirilir. Diğer bir durum olan bakiyenin eksi olması halinde ise, ekleme işlemi gerçekleşir.
- Örnekte HAMORT+OAYNAKHAMORT toplamının 3 TL olması beklenir. Bu durumda hammadde maliyeti satılan malın maliyeti bakış açısı ile:
25 TL – ( 5 × 2 ) – ( 4 × 3 ) = 3 TL şeklinde hesaplanır.

**Kısıtlar**

Kısıtlar sekmesinde Kısıt Kodu Aralığı ve eski yıl şirket kayıtlarının analiz kapsamına dahil seçimler yapılır. "Çalıştır" butonu ile analiz yeniden çalıştırılır. Daha önce oluşturulan rapor varsa, "Mevcut Rapor" butonu ile izlenir. "Görüntüle" butonu ile de, mevcut maliyet analiz dosya içeriği incelenir.

Kısıtlar sekmesinde yapılan seçimler, kullanıcı bazında saklanır. Bu sayede, sonraki kullanımlarda daha önce yapılan seçimler sistem tarafından kullanıcıya sunulur.

**Rapor**

Raporun hazırlanması sürecindeki adımlar, işleyişin hangi aşamada olduğu ve ne kadar sürede tamamlandığına dair bilgiler, yardımcı ekran aracılığı ile takip edilir. Rapor ekranında öncelikle genel hatları ile PSI bilgileri yer alır. Sütun bölümünde görüntülenen ikonlar yardımı ile, ilgili sütun üzerinde sıralama yapılması sağlanır. Sağ bölümde yer alan Microsoft Excel dışarı veri aktarım grafik ikonu ile, bulunduğu satır itibariyle bağlı olan bölüm için aktarım sağlanır.

"Detaylar" bölümünde ise, projenin alt maliyet analiz bilgileri bulunur. PSI detayında Hammadde Sarf Özeti ve Maliyet Özeti başlıkları yer alır. Hammadde Sarf Özeti; mamul grupların PSI bazında giriş, çıkış, satış miktarları ve bakiye takibinin izleneceği bir bölüm olmakla birlikte, istenen mamul gruplarının hammadde sarf detaylarının gözlemleneceği bir bölüm olarak da kullanılabilir.

PSI Bazında Maliyet Özeti'nde, analiz karakterinin genel olarak maliyet türlerine uygun şekilde dağılımı görüntülenir. Bu bölümde PSI bazında tespit edilen maliyetler, mamul gruplar detayından izlenir.

**e-Posta Gönderimi ve Görüntüleme**

PSI bazında maliyet bilgileri e-Posta yardımı ile kullanıcılar arasında paylaşılabilir. e-Posta Gönderim seçeneği ile, PSI maliyet analiz bilgileri "Ek Dosya" olarak seçilen kullanıcılara iletilir. Ulaşan ek dosya, PSI Maliyet Analiz bölümünde "Görüntüleme" işlemi ile izlenir. Dosya boyutu 10 MB’yi aştığında, sistem tarafından NETZIP uzantısı ile sıkıştırılarak kullanıcılara iletilir. Bu şekilde gelen dosyanın açılması istendiğinde Sürükle-Bırak veya dosya seçim yöntemleriyle görüntüleme işlemi gerçekleştirilir. Dosya ekran üzerine bırakıldığında, içerik sistem tarafından kullanıcıya gösterilir. 10 MB dosya büyüklüğünü aşmayan maliyet analiz dosyaları, HTML uzantısı ile kullanıcılara iletilir. Bu şekilde alınan ek dosyalar, mevcut bir tarayıcı (Browser) yardımı ile izlenir.

**Dışarı Veri Aktarımı**

PSI bazında Mamul Grup Bakiye ve Hammadde Sarf Özeti bilgilerinin bir arada aktarılmasını sağlar.
