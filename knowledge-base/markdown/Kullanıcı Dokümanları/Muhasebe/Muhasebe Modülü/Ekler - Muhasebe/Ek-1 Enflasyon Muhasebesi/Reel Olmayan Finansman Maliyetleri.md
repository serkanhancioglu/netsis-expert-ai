---
title: "Reel Olmayan Finansman Maliyetleri"
page_id: "24740924"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Muhasebe"
  - "Muhasebe Modülü"
  - "Ekler / Muhasebe"
  - "Ek-1 Enflasyon Muhasebesi"
  - "Reel Olmayan Finansman Maliyetleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / Ekler / Muhasebe / Ek-1 Enflasyon Muhasebesi / Reel Olmayan Finansman Maliyetleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWZhMzJiMThhLTQ4MGYtNDcyMy1hYWZhLWM1MTM2M2Q4YzZlNyZsaW5rPTg5MjdkZDQ1LTU5NDgtNDFkYS1hZTViLTFhNTYyNWExNDIwMSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=fa32b18a-480f-4723-aafa-c51363d8c6e7&link=8927dd45-5948-41da-ae5b-1a5625a14201&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "reel-olmayan-finansman-maliyetleri_41162295_24740924.html"
source_version: "2022-12-12T16:27:38.010+03:00"
source_bytes: 31521
fetched_at: "2026-09-13T04:14:31+00:00"
generator: "netsis-scraper 1.0.0"
---
# Reel Olmayan Finansman Maliyetleri

Reel Olmayan Finansman Maliyetleri ile ilgili ayrıntılı bilgiye bu dokümandan ulaşılabilir.

Stokların, satılan malın ve maddi duran varlıkların maliyet bedeline ve mali duran varlıkların alış bedeline intikal ettirilen finansman maliyeti, faiz ve kur farkı gibi maliyetler olup, içerdikleri enflasyon payından arındırıldıktan sonra kalan değerler üzerinden düzeltmeye tabi tutulması gerekir. Alış ve maliyet bedellerine intikal ettirilen finansman maliyetlerinin içerdiği enflasyon payı, **Reel Olmayan Finansman Maliyeti** olarak adlandırılır.

**Örneğin;**

3.000.000 TL tutarında alınan bir maddi duran varlık için, bir sonraki dönemde %30 kredi faizi karşılığı olan 900.000 TL tutarında finansman maliyeti olarak aktif hale getirilir. Maddi duran varlığın değeri; 3.900.000 TL tutarına yükselir. Ancak, bu dönemde enflasyon %10 oranında gerçekleştiğinde, söz konusu finansman maliyetinin %10 enflasyon payını içeren kısmı, reel olmayan finansman maliyetidir.

Reel olmayan finansman maliyeti = 0.1/0.3 \* 900,000 = 300.000

Finansman maliyeti reel kısmı = 900.000 – 300.000 = 600.000

Maddi duran varlık reel değeri = 3.000.000 + 600.000 = 3.600.000.

Dönem sonrası düzeltmeye tabi tutulacak maddi duran varlık bedelinin 3.600.000 olması gerekir.

Vergi Usul Kanununa göre reel olmayan finansman maliyeti ihtiva eden iktisadi kıymetler; Stoklar, Maddi Duran Varlıklar, Mali Duran Varlıklar ve Özel Tükenmeye Tabi Varlıklardır. Bu kalemlerde aktif hale gelen finansman maliyeti bulunuyorsa, düzeltme işlemlerinden önce reel olmayan kısımların arındırılmasına dikkat edilmesi gerekir.

Örnekte, aktif hale gelen finansman maliyetinin kredi faiz oranı (%30) biliniyordu. Ancak, farklı faiz oranları ile birden fazla kredi kullanılmış ve bunlar zaman içinde birden fazla farklı kalem üzerinde aktif hale gelmişse, finansman maliyetlerinin reel olmayan kısımlarını arındırma işlemi için faiz oranı belirlemek güçleşir. Bu durumda mükellefler; reel olmayan finansman maliyetini toplam finansman maliyetlerine, ilgili döneme ait TEFE artış oranının dönem ortalama ticari kredi faiz oranına bölünmesi suretiyle belirlenen oranı uygulayarak tespit edebilirler. Söz konusu "Ortalama Tcari Kredi Faiz Oranları" Maliye Bakanlığı tarafından açıklanır (328 Seri No’lu VUK Genel Tebiliği’nin 4 numaralı ekinde oranlar yer almaktadır).

Bu açıklama dikkate alınarak,

Reel olmayan finansman maliyeti = Enflasyon Oranı/Ortalama Ticari Kredi Faiz Oranı \* Finansman Maliyeti şeklinde hesaplanır.

> [!NOTE]
> Logo Netsis Enflasyon Muhasebesinde, reel olmayan finansman maliyeti arındırması için otomatik bir yöntem yoktur. Aktif hale getirme işlemi sırasında, yukarıda verilen oranlamanın yapılarak finansman maliyetinin reel olan kısmı ayrıştırılır ve ilgili hesaba (stok, sabit kıymet gibi) aktarılır. Reel olmayan kısmı ise muhasebede finansman giderine aktarılır. Stok ve Sabit Kıymet gibi modüllerde de aynı mantıkla reel finansman maliyeti girilir. Reel ve reel olmayan finansman maliyetlerinin tüm modüllerde TL tutarlara kaydedilmesi gerekir.

**Parasal Kıymetler (1)**

|  |  |
| --- | --- |
| 100 | İşletmenin elinde bulunan ulusal paralar |
| 101 | Gerçek ve tüzel kişiler tarafından işletmeye verilen ve henüz tahsil için bankaya verilmemiş veya ciro edilmemiş olan çekler |
| 102 | İşletme tarafından yurt içi ve yurt dışı banka ve benzeri finans kurumlarına yatırılan ve çekilen mevduat |
| 103 | Bankalar ve özel finans kurumları üzerinden gerçekleştirilen çekler ve ödeme emirleri |
| 108 | İşletmenin ihtiyacı için satın alınan posta, damga ve harç pulları ile vadesi gelmiş kuponlar ve yoldaki paralar |
| 111 | Özel sektör tarafından çıkarılan tahvil, senet ve bonolar **(2)** |
| 112 | Kamu kesimince çıkarılan tahvil, senet ve bonolar **(3)** |
| 120 | İşletmenin faaliyet konusunu oluşturan mal ve hizmet satışlarından kaynaklanan senetsiz alacaklar |
| 121 | İşletmenin faaliyet konusunu oluşturan mal ve hizmet satışlarından kaynaklanan senede bağlanmış alacaklar |
| 122 | Alacak senetleri için ayrılan reeskont işlemleri |
| 124 | Finansal kiralamanın yapıldığı tarihte, kiralama işlemlerinden doğan alacaklar ile kira ödemelerinin bugünkü değeri arasındaki fark |
| 126 | İşletme tarafından üçüncü kişilere karşı bir işin yapılmasının üstlenilmesi veya bir sözleşmenin ya da diğer işlemlerin karşılığı olarak geri alınmak üzere verilen depozito ve teminatlar **(4)** |
| 128 | Ödeme süresi geçmiş bu nedenle vadesi bir kaç defa uzatılmış veya protesto edilmiş, yazı ile birden fazla istenmiş ya da dava veya icra safhasına aktarılmış senetli ve senetsiz şüpheli ticari alacaklar |
| 131 | İşletmenin esas faaliyet konusu dışındaki işlemler dolayısı ile (ödünç verme ve benzer nedenlerle ortaya çıkan) ortaklarından olan alacakları |
| 132 | İşletmenin esas faaliyet konusu dışındaki işlemler dolayısı ile (ödünç verme ve benzer nedenlerle ortaya çıkan) iştiraklerinden olan alacakları |
| 133 | İşletmenin esas faaliyet konusu dışındaki işlemler dolayısı ile (ödünç verme ve benzer nedenlerle ortaya çıkan) bağlı ortaklıklarından olan alacakları |
| 135 | İşletmeye dahil olan personel ve işçilerden olan alacaklar |
| 137 | Alacak senetleri için ayrılan reeskont işlemleri |
| 138 | Ödeme süresi geçmiş bu nedenle vadesi bir kaç defa uzatılmış veya protesto edilmiş, yazı ile birden fazla istenmiş ya da dava veya icra safhasına aktarılmış senetli ve senetsiz şüpheli diğer alacaklar |
| 179 | Taşeronlara verilen avanslar **(5)** |
| 181 | Üçüncü kişilerden tahsili ya da bunlar hesabına kesin borç kaydı hesap döneminden sonra yapılacak gelirlerin, içinde bulunan dönemde tahakkuk eden kısımları |
| 190 | Devreden katma değer vergisi |
| 191 | İndirilecek katma değer vergisi |
| 192 | Teşvikli yatırım mallarının ithalinde ödenmesi gerektiği halde ödenmeyip, fiilen indirilmesinin mümkün olacağı tarihe kadar ertelenen katma değer vergisi |
| 193 | Mevzuat gereğince peşin ödenen gelir, kurumlar ve diğer vergiler ile fonlar |
| 195 | İşletme adına mal ve hizmet satın alacak, işletme adına bir kısım gider ve ödemeleri yapacak personel ve personel dışındaki kişilere verilen avanslar |
| 196 | Personele maaş, ücret ve yolluklarına mahsuben önceden ödenen diğer avanslar |
| 197 | Tesellüm sırasında veya sayımlar sonucunda tespit edilen noksanlar |
| 220 | İşletmenin faaliyet konusunu oluşturan mal ve hizmet satışlarından kaynaklanan senetsiz alacaklar |
| 221 | Her türlü senetli alacaklar |
| 222 | Senetli alacakların tasarruf değeriyle değerlenmesini sağlamak amacı ile alacak senetleri için ayrılan reeskont işlemleri |
| 224 | Finansal kiralamanın yapıldığı tarihte kiralama işlemlerinden doğan alacaklar ile kira ödemelerinin bugünkü değeri arasındaki fark |
| 226 | Üçüncü kişilere karşı bir işin yapılmasının üstlenilmesi ve bir akdin karşılığı olarak, geri alınmak üzere verilen, bir yıldan uzun süreli depozito ve teminatlar **(6)** |
| 231 | Esas faaliyet konusu dışındaki işlemler dolayısı ile (ödünç verme ve benzer nedenlerle ortaya çıkan) ortaklardan olan alacaklar |
| 232 | Esas faaliyet konusu dışındaki işlemler dolayısı ile (ödünç verme ve benzer nedenlerle ortaya çıkan) iştiraklerden olan alacaklar |
| 233 | Esas faaliyet konusu dışındaki işlemler dolayısı ile (ödünç verme ve benzer nedenlerle ortaya çıkan) bağlı ortaklıklardan olan alacaklar |
| 235 | İşletme topluluğuna dahil olan personelden alacaklar |
| 237 | Diğer alacaklar grubundaki senetli alacakların değerlenmesini sağlamak amacı ile alacak senetleri için ayrılan reeskont işlemleri |
| 269 | Maddi olmayan duran varlıklarla ilgili olarak gerek yurt içi, gerekse yurt dışındaki kişi ve kuruluşlara verilen avanslar **(7)** |
| 279 | Özel tükenmeye tabi varlıklar için verilen avanslar **(8)** |
| 281 | Üçüncü kişilerden tahsili ya da bunlar hesabına kesin borç kaydı bir yıl veya daha sonraki yıllarda yapılacak gelirlerin içinde bulunulan dönemde tahakkuk eden kısımları |
| 291 | Satın alınan veya imal edilen, amortismana tabi iktisadi kıymetlerle ilgili bir yıldan daha uzun sürede indirilebilecek nitelikteki katma değer vergisi |
| 292 | Ertelenen, iadesi gereken, tahsil edilen ve çeşitli şekillerde ortaya çıkan diğer katma değer vergisi |
| 295 | Peşin ödenen vergiler ve fonlar |
| 300 | Banka ve diğer finans kuruluşlarından sağlanan krediler |
| 301 | Kiracıların finansal kiralama yapanlara olan ve vadesi 1 yılı geçmeyen borçları **(9)** |
| 302 | Finansal kiralamanın yapıldığı tarihte kiralama işlemlerinden doğan borçlar ile kiralanan varlığa ilişkin kira ödemelerinin bugünkü değeri arasındaki fark |
| 303 | Vadelerine bir yıldan fazla süre bulunmakla birlikte uzun vadeli kredilerin, bilanço tarihinden itibaren bir yıl içinde ödenecek anapara taksitleri ile bunların tahakkuk ettiği halde henüz ödenmeyen faizleri |
| 304 | Bilanço tarihinden itibaren bir yıl içinde ödenecek tahvil anapara taksitleri ile tahakkuk edip de henüz ödenmeyen faizleri |
| 305 | Tedavüldeki finansman bonoları ve banka bonoları gibi kısa vadeli para ve sermaye piyasası araçları karşılığında sağlanan fonlar |
| 308 | Nominal değerinin altında ihraç edilen tahvil, senet gibi diğer menkul kıymetlerin nominal değeri ile satış fiyatı arasındaki farkın gelecek döneme ait olan kısmı |
| 320 | İşletmenin faaliyet konusu ile ilgili her türlü mal ve hizmet alımlarından kaynaklanan senetsiz borçları |
| 321 | İşletmenin faaliyet konusu ile ilgili her türlü mal ve hizmet alımlarından kaynaklanan senede bağlanmış ticari borçları |
| 322 | Bilanço gününde, senetli borçların tasarruf değeri ile değerlemesini sağlamak üzere borç senetleri için ayrılan reeskont işlemleri |
| 326 | Üçüncü kişilerin belli bir işi yapmalarını, aldıkları bir değeri geri vermelerini sağlamak amacıyla ve belli sözleşmeler nedeniyle gerçekleşecek bir alacağın karşılığı olarak alınan depozito ve teminatlar **(10)** |
| 331 | İşletmenin esas faaliyet konusu dışındaki işlemleri dolayısıyla ortaklarına olan borçları |
| 332 | İşletmenin esas faaliyet konusu dışındaki işlemleri dolayısıyla iştiraklerine olan borçları |
| 333 | İşletmenin sermaye taahhüdünden borçları hariç olmak üzere faaliyet konusu dışındaki işlemleri dolayısıyla bağlı ortaklıklarına olan borçlar |
| 335 | İşletmenin personeline olan çeşitli borçları |
| 337 | Bilanço gününde, diğer borçlar grubundaki senetli borçların değerlemesini sağlamak amacı ile borç senetleri için ayrılan reeskont işlemleri |
| 360 | İşletmenin ekonomik faaliyetlerde bulunmasının sonucu ilgili mali mevzuat uyarınca mükellef veya sorumlu sıfatıyla işletmenin kendisine, personeline ve üçüncü kişilere ilişkin olarak ödenmesi gereken vergi, resim, harç ve fonlar |
| 361 | İşletmenin, personelin hak edişlerinden sosyal güvenlik mevzuatı hükümlerine göre kesintiye tabi tutmakla yükümlü bulunduğu, personele ait emeklilik keseneği ve sigorta primleri ile bunlara ilişkin işveren katılma payları gibi işverence sosyal güvenlik kuruluşlarına ödenecek kesintiler |
| 368 | Kanuni süresi içerisinde ödenmeyen vergi ve yükümlülükler |
| 371 | Mevzuat gereğince peşin ödenen gelir ve kurumlar vergisi ile diğer yükümlülükler |
| 381 | Gelecek aylarda ödemesi yapılacak belgeye dayalı gider tahakkukları |
| 391 | Teslim edilen mal veya ifa edilen hizmetler üzerinden hesaplanan katma değer vergisi ile işlemi gerçekleşmeyen ya da işlemden vazgeçilen mal ve hizmetlere ilişkin katma değer vergisi |
| 392 | Teşvikli yatırım mallarının ithalinden doğan ve ertelenen katma değer vergisi ve ihraç kaydıyla satış nedeniyle ertelenen ve terkin edilecek katma değer vergisi |
| 393 | Merkez ve şubeler cari hesabı |
| 397 | Sayımlar sonunda tespit edilen kasa, stok ve maddi duran varlıklardaki fazlalar |
| 400 | Banka ve diğer finans kuruluşlarından alınan uzun vadeli krediler |
| 401 | Kiracıların finansal kiralama yapanlara olan ve vadesi 1 yılı aşan borçları **(11)** |
| 402 | Finansal kiralamanın yapıldığı tarihte kiralama işlemlerinden doğan ve vadesi bir yılı aşan borçlar ile kiralanan varlığa ilişkin kira ödemelerinin bugünkü değeri arasındaki fark |
| 405 | İşletme tarafından çıkarılmış bulunan ve vadesi bir yılı aşan tahviller |
| 407 | İşletme tarafından çıkarılmış katılma intifa senedi dışındaki vadeleri bir yıldan uzun olan diğer menkul değerler |
| 408 | Nominal değerinin altında ihraç edilen tahvil, senet ve diğer menkul kıymetlerin nominal değerleri ile satış fiyatı arasındaki farkın gelecek yıllara ait olan kısmı |
| 420 | İşletmenin faaliyet konusu ile ilgili her türlü mal ve hizmet alımlarından kaynaklanan vadelerine bir yıldan fazla süre bulunan senetsiz borçlar |
| 421 | İşletmenin faaliyet konusu ile ilgili her türlü mal ve hizmet alımlarından kaynaklanan vadelerine bir yıldan fazla süre bulunan senetli borçlar |
| 422 | Bilanço gününde, senetli borçların tasarruf değeriyle değerlenmesini sağlamak üzere, borç senetleri için ayrılan reeskont işlemleri |
| 426 | Alınan Depozito ve Teminatlar hesabında alış amaçları belirtilen depozito ve teminatların vadeleri bir yıldan fazla olan kısımları **(12)** |
| 431 | İşletmenin esas faaliyet konusu dışındaki işlemleri dolayısıyla ortaklarına olan vadeleri bir yıldan fazla süreli borçları |
| 432 | İşletmenin esas faaliyet konusu dışındaki işlemleri dolayısıyla iştiraklerine olan vadeleri bir yıldan fazla süreli borçları |
| 433 | İşletmenin sermaye taahhüdünden borçları hariç olmak üzere faaliyet konusu dışındaki işlemleri dolayısıyla bağlı ortaklıklarına vadeleri bir yıldan fazla süreli olan borçları |
| 437 | Bilanço gününde, uzun vadeli diğer borçlar grubunda yer alan senetli borçların değerlemesini sağlamak amacı ile borç senetleri için ayrılan reeskont işlemleri |
| 438 | Kamuya olan vergi ve benzeri borçlardan vadesinde ödenmeyip ertelenmiş veya taksite bağlanmış olup bir yıldan daha uzun bir sürede ödenecek olan borçlar |
| 481 | Gelecek yıllarda ödenmesi yapılacak ve kesinlikle belgeye dayalı gider tahakkukları |
| 492 | Teşvikli yatırım mallarının ithalinde ödenmesi gerektiği halde ödenmeyip, fiilen indirilmesinin mümkün olacağı tarihe kadar ertelenen katma değer vergisi ile imalatçı teşebbüsler tarafından imal ettikleri mallardan ihraç edilmek kaydı ile ihracatçılara yapılan teslimler nedeniyle hesaplanan ve düzenlenen fatura ve fatura yerine geçen belgelerde mevzuat gereği ihracatçılardan tahsil edilmeyen ve tamamının indirim konusu yapılmaması nedeniyle gelecek bilanço devrelerine kadar tecil olunan katma değer vergisi |
| 493 | İşletmeye ait tesislerden yararlanmak amacıyla üçüncü kişilerin, tesis bedellerine katılma payları |

**(1)** Listede yer alan iktisadi kıymetler, uygulayıcılar için kolaylık sağlamak üzere, “Tek Düzen Hesap Planı” bölümünden izlenen hesap kodları ile gösterilir.

**(2)** Bu kıymetler, Vergi Usul Kanununun 279. maddesi kapsamında alış bedeli ile değerlenmesi halinde, değerlendiği tarihten itibaren “parasal olmayan kıymet” olarak addolunur.

**(3)** Bu kıymetler, Vergi Usul Kanununun 279. maddesi kapsamında alış bedeli ile değerlenmesi halinde, değerlendiği tarihten itibaren “parasal olmayan kıymet” olarak addolunur.

**(4)** Geri alınması şartıyla verilen depozito ve teminatların parasal olmayan bir mahiyet taşıması durumunda, söz konusu verilen depozito ve teminatlar “parasal olmayan kıymet” olarak addolunur.

**(5)** Verilen avans, parasal olmayan bir mahiyet taşıyor ise “parasal olmayan kıymet” olarak addolunur.

**(6)** Geri alınması şartıyla verilen depozito ve teminatların parasal olmayan bir mahiyet taşıması durumunda, söz konusu verilen depozito ve teminatlar “parasal olmayan kıymet” olarak addolunur.

**(7)** Verilen avans, parasal olmayan bir mahiyet taşıyor ise “parasal olmayan kıymet” olarak addolunur.

**(8)** Verilen avans, parasal olmayan bir mahiyet taşıyor ise “parasal olmayan kıymet” olarak addolunur.

**(9)** Vergi Usul Kanununun Mükerrer 290. maddesine göre finansal kiralama yoluyla temin edilen iktisadi kıymetler “parasal kıymet” addolunur.

**(10)** Geri verilmesi şartıyla alınan depozito ve teminatların parasal olmayan bir mahiyet taşıması durumunda, söz konusu alınan depozito ve teminatlar “parasal olmayan kıymet” olarak addolunur.

**(11)** Vergi usul Kanununun Mükerrer 290. maddesine göre finansal kiralama yoluyla temin edilen iktisadi kıymetler “parasal kıymet” addolunur.

**(12)** Geri verilmesi şartıyla alınan depozito ve teminatların parasal olmayan bir mahiyet taşıması durumunda, söz konusu alınan depozito ve teminatlar “parasal olmayan kıymet” olarak addolunur.

**Parasal Olmayan Kıymetler (1)**

**(1)** Listede yer alan iktisadi kıymetler, uygulayıcılar için kolaylık sağlamak üzere, “Tek Düzen Hesap Planı” bölümünden izlenen hesap kodları ile gösterilir.

**(2)** İşletmenin ortaklık hakkı elde etmek için yaptığı ödeme karşılığında, hisse senedi almaması halinde, bu kıymetler “parasal kıymet” addolunur.

**(3)** Sermaye taahhüdünün ortaklık hakkı elde etmek için yapılan ödeme karşılığında hisse senedi alınmamış bir iştirak için yapılmış olması halinde bu kıymetler “parasal kıymet” addolunur.

**(4)** İşletmenin ortaklık hakkı elde etmek için yaptığı ödeme karşılığında, hisse senedi almaması halinde, bu kıymetler “parasal kıymet” addolunur.

**(5)** Sermaye taahhüdünün ortaklık hakkı elde etmek için yapılan ödeme karşılığında hisse senedi alınmamış bir iştirak için yapılmış olması halinde bu kıymetler “parasal kıymet” addolunur.

**(6)** Verilen avans, parasal olmayan bir mahiyet taşıyor ise “parasal olmayan kıymet” olarak addolunur.
