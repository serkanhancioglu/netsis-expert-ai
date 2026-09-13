---
title: "Enflasyon Muhasebesi Sıkça Sorulan Sorular"
page_id: "135823534"
product: "netsis-3-enterprise"
depth: 3
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Enflasyon Muhasebesi Düzenlemeleri (555 Sayılı VUK Genel Tebliği)"
  - "Enflasyon Muhasebesi Sıkça Sorulan Sorular"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Enflasyon Muhasebesi Düzenlemeleri (555 Sayılı VUK Genel Tebliği) / Enflasyon Muhasebesi Sıkça Sorulan Sorular"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWY4OTg3Y2M4LWEzMDMtNDYyNi04NjFiLTEzYWI5ZjYxMzcyNiZsaW5rPTY0ZDQwMDQxLWVlN2YtNDQxOS05OWRlLTg0Mjk5OTViZWY1NyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=f8987cc8-a303-4626-861b-13ab9f613726&link=64d40041-ee7f-4419-99de-8429995bef57&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "enflasyon-muhasebesi-sikca-sorulan-sorular_135823770_135823534.html"
source_version: "2024-10-04T14:17:54.183+03:00"
source_bytes: 243464
fetched_at: "2026-09-13T04:22:43+00:00"
generator: "netsis-scraper 1.0.0"
---
# Enflasyon Muhasebesi Sıkça Sorulan Sorular

**Enflasyon düzeltmesi nedir?**

VUK 298/A maddesinde enflasyon düzeltmesi, "mali tablonun ait olduğu tarihteki satın alma gücü cinsinden hesaplanması" şeklinde tanımlanmıştır. Buna göre enflasyon düzeltmesi, mali tablolarda yer alan parasal olmayan kıymetlerin Türk Lirası değerlerinin, tablonun ait olduğu tarihteki değerine yükseltilmesi işlemidir.

**Düzeltme işlemine tabi olacak bilanço hangi tarihli bilançodur?**

Hesap dönemi takvim yılı olanlar için 31/12/2023 tarihli bilanço, kendisine özel hesap dönemi tayin edilen mükellefler için 2024 yılı içinde biten hesap dönemi sonunda düzenleyecekleri bilanço düzeltme işlemine tabidir.

**2023 yılı bilançosu düzeltilmiş değerler üzerinden mi düzenlenir?**

2023 hesap dönemi sonuna ait bilanço, enflasyon düzeltmesine ilişkin hükümler göz önünde bulundurulmaksızın düzenlenir.

**2024 yılında her geçici vergi döneminde enflasyon düzeltmesi yapılacak mı?**

Düzeltme şartlarının devam etmesi halinde izleyen geçici vergi dönem sonu bilançoları da düzeltme işlemine tabi tutulur. Netsis ERP tarafında düzeltmeler ay ay yürütülerek yapılır.

**Enflasyon düzeltmesi sürecinde temelde yapılması gereken işlemler sırası ile nelerdir?**

- Mali tabloda yer alan kıymetlerden hangilerinin parasal olmayan kıymet olduğu tespit edilir.
- Tespit edilmiş parasal olmayan kıymetlerin enflasyon düzeltmesinde dikkate alınacak tutarları (düzeltmeye esas tutarları) bulunur.
- Tespit edilmiş parasal olmayan kıymetlerin enflasyon düzeltmesinde düzeltmeye esas tarihleri ve buna bağlı düzeltme/taşıma katsayıları belirlenir.
- Tespit edilmiş düzeltmeye esas tutarlar ait oldukları düzeltme/taşıma katsayılarıyla çarpılarak düzeltilmiş tutarları hesaplanır.
- Parasal olmayan kıymetlerin, düzeltilmiş değerler ile düzeltme öncesi değerler arasındaki enflasyon farkları kayıtlara alınır.
- Parasal olmayan kıymetler düzeltilmiş değerleriyle, parasal kıymetler ise düzeltmeye tabi tutulmaksızın mali tabloda gösterilir.

**Enflasyon düzeltmesi için Netsis Erp'de yapılması gereken tanımlamalar nelerdir?**

- Netsis Sıra Numarası "Aylık Enflasyon Oranları" olan bir döviz tipi tanımlanır ve bu döviz tipi Şirket - Şube - Parametre Tanımları ekranından "Döviz Tipi" alanına bağlanır.
- Döviz Kurları Girişi ekranından "Tüm Enflasyon Oranlarını Güncelle" işlemi çalıştırılır ya da her ayın son gününe ait Yİ-ÜFE endeks bilgisi elle girilir.
- Muhasebe Parametreleri/Dövizli Muhasebe ekranından "Enf. Muh." seçilir ve "Toplulaştırılmış Yöntem Uygulaması" belirlenir.
- Düzeltme işlemlerinde kullanılacak enflasyon fark hesapları, enflasyon düzeltme hesapları, parasal kar zarar hesapları tanımlanır.
- Hesap Planı ekranından düzeltilecek hesaplar için "Düzeltilecek Hesap" seçeneği işaretlenir ve düzeltilmiş tutarın aktarılacağı "Enflasyon Fark Hesap Kodu" seçilir.
- Muhasebe Parametreleri/Dövizli Muhasebe ekranından "Enf.Düz.Hesap Alacak/Borç" ve "Parasal Kar/Zarar" hesapları seçilir.

**Enflasyon düzeltmesinde kullanılacak fark hesapları nasıl tanımlanır?**

Hesap Planı ekranından "Enflasyon Fark Hesabı" seçeneği işaretlenerek tanımlanır.

**Düzeltilecek hesabın düzeltme tutarının hangi hesaba kayıt atacağı nasıl belirlenir?**

Hesap Planı ekranında "Düzeltilecek Hesap" seçildikten sonra Döviz Bilgileri sekmesinden "Enflasyon Fark Hesap Kodu" seçilir.

**Enflasyon fark hesap kodu rehberi neden boş gelir?**

Fark işlemlerinde kullanılacak hesaplar açılırken Hesap Planı ekranında "Enflasyon Fark Hesabı" seçeneği işaretlenerek tanımlanmalıdır. Rehbere sadece bu şekilde tanımlanan hesaplar gelir.

**Enflasyon fark hesap kodu alanı neden pasif gelir?**

Hesap planı ilk sayfasında "Enflasyon Fark Hesabı" seçilen hesapların Dövizli sekmesinde "Enflasyon Fark Hesap Kodu" pasif gelir.

**Muhasebe Parametrelerinde bulunan Toplulaştırılmış Yöntem Uygulamalarından Enf.Muh. Ve Hiçbiri arasındaki fark nedir?**

Toplulaştırılmış Yöntem "Enf.Muh." seçimi stok hesapları için düzeltme işlemlerinin muhasebe tarafında basit ortalama ve stok devir hızı yöntemleri kullanılarak toplulaştırılmış yöntemlerle yapılacağı anlamına gelir. "Hiçbiri" seçimi ise stokların gerçek yöntem ile stok bazında Stok modülü üzerinden yapılacak enflasyon düzeltme işlemleri ile düzeltileceği anlamına gelir.

**Enflasyon düzeltmesi nasıl yapılacak?**

Düzeltme, parasal olmayan kıymetlerin enflasyon düzeltmesinde dikkate alınacak tutarlarının, düzeltme katsayısı ile çarpılması suretiyle gerçekleşir.

**Düzeltme katsayısı nedir?**

Bilanço günündeki fiyat endeksi rakamının, düzeltmeye konu işlemin gerçekleştiği tarihteki fiyat endeksi rakamına bölünmesi suretiyle elde edilen katsayıdır.

**Düzeltmeye esas tutar nedir?**

Parasal olmayan kıymetin düzeltmeye esas tarih itibari ile sahip olduğu değerdir

**Enflasyon düzeltmesinde hangi endeks kullanılır?**

Mükelleflerce düzeltme katsayısı belirlenirken Yİ-ÜFE oranları dikkate alınır.

**Yİ-ÜFE nedir?**

Yİ-ÜFE Türkiye İstatistik Kurumunca her ay için belirlenen; 2004 yılı Aralık ayı bakımından toptan eşya fiyat endeksi (TEFE) değeri,1/1/2005 tarihinden itibaren üretici fiyatları endeksi (ÜFE) değerleri, 1/1/2014 tarihinden itibaren yurt içi üretici fiyat endeksi (Yİ-ÜFE) değeridir.

**Toplulaştırılmış yöntemlerle katsayı belirleme olanağı hangi kıymetler için geçerlidir?**

Toplulaştırılmış yöntemler kullanılarak düzeltilebilecek parasal olmayan kıymetler sadece stoklarla sınırlıdır.

**Toplulaştırılmış yöntemler nelerdir?**

Enflasyon düzeltmesi işleminde kullanılabilecek toplulaştırılmış yöntemler "Basit Ortalama" ve "Stok Devir Hızı" yöntemidir.

**Basit ortalama yöntemi nedir?**

Dönem ortalama düzeltme katsayısı bulunarak stok hesapları TL değerlerinin bu katsayıyla çarpılması suretiyle düzeltilmesidir.

Dönem Sonu Endeksi / ((Bir önceki dönem sonu endeksi+Dönem sonu endeksi)/2) şeklinde hesaplanır.

**Stok devir hızı yöntemi nedir?**

Stok hesapları bazında, ortalama stokta durma günü hesaplanarak kalan stoğun bu tarihte alındığı varsayılır. Kalan stoğun dönem sonu TL değeri, dönem sonu endeksinin stoğa giriş tarihindeki (dönem sonu - durma günü tarihindeki) endekse oranlanması ile elde edilen katsayı ile düzeltilir.Bu yöntem seçildiğinde stok hesapları için Düzeltilecek Stok Hesapları ekranında yer alan "Durma Günü" değerleri ve "Oran" bilgileri girilmelidir.

**Stok hesapları bazında farklı toplulaştırılmış yöntemler belirlenebilir mi?**

Toplulaştırılmış Yöntem Uygulaması "Enf.Muh." seçilmesi durumunda stok hesapları için Muhasebe/ Düzeltilecek Stok Hesapları Tanımları ekranından hesap bazında yöntem seçilir.

**Enflasyon düzeltmesi ile enflasyon taşıma işlemi arasındaki fark nedir?**

Teknik olarak ikisi de aynı amaca hizmet eder. 2023-12 bilançosu üzerinde yapılacak olan düzeltme işlemi toplu yapılacak bir işlemdir ve enflasyon düzeltmesi olarak adlandırılır. 2024-1 ile başlayacak ve her vergi döneminde yapılacak işlem ise enflasyon taşıma olarak adlandırılır.

**2023 Sonu enflasyon düzeltmesi İçin Netsis ERP'de nasıl bir yol izlenmelidir?**

2023 yılı düzeltmesi 2023 ve öncesini kapsayan bir düzenleme olduğu için düzeltme farklarının elle yevmiye kaydı olarak girilmesi ya da excelde düzenlenip Netsis içerisine aktarılması beklenmektedir.

**Enflasyon taşıma işlemlerinin adımları nelerdir?**
Toplulaştırılmış Yöntem Uygulaması "Enf.Muh." seçili olduğu durumda;

- Muhasebe/ Stok Hesapları Düzeltme
- Muhasebe/ Enflasyon Düzeltme
- Muhasebe/ Enflasyon Düzeltmeleri Parasal K-Z Virmanı

Toplulaştırılmış Yöntem Uygulaması "Hiçbiri" seçili olduğu durumda;

- Stok Döviz Çevrim
- Stok Enflasyon Düzeltme
- Maliyet Oluşturma
- Kullanılıyor ise Satılan Malın Maliyeti Mahsubu / Maliyet Muhasebesi-Maliyet Hesaplatma
- Muhasebe/ Enflasyon Düzeltme
- Muhasebe/ Enflasyon Düzeltmeleri Parasal K-Z Virmanı Virmanı

**Stok Hesapları Düzeltme işlemi ne işe yarar?**

Toplulaştırılmış Yöntem Uygulaması "Enf.Muh." seçildiğinde yani toplulaştırılmış yöntemler kullanıldığında Muhasebe/Düzeltilecek Stok Hesapları ekranından stok hesapları bazında yöntem belirlenir. Bu tanımlamamalara istinaden farkların hesaplanması ve muhasebe fişinin oluşması Stok Hesapları Düzeltme işlemi ile sağlanır. İşlem aylık olarak çalıştırılmalıdır.

**Stok Hesapları Düzeltme ekranında bulunan "Dönem Son Ay İçin Düzeltme" işlemi ne işe yarar?**

Düzeltilecek Stok Hesapları ekranında bulunan Yöntem seçiminde "Basit Ortalama" ve "Stok Devir Hızı" olarak iki seçim bulunur. Basit ortalama dönemsel bir taşıma yaparken, stok devir hızı tanımlarda bulunan durma gününe göre geriye dönük endeks bularak taşıma yapar. Bu aşamada doğru endekse ulaşmak için işlem aylık çalıştırılmalıdır(Ocak-Şubat, Ocak-Mart, Ocak-Nisan…). Aylık çalıştırmalarda sadece "Stok Devir Hızı" seçimli hesaplar taşınırken, "Dönem Son Ay İçin Düzeltme" parametresi işaretlendiğinde "Basit Ortalama" seçili hesaplarda taşıma işlemine dahil edilir. Buda geçici vergi dönemlerinde yapılacak taşıma işleminde seçilmesi gerektiği anlamına gelir.

**Stok Hesapları Düzeltme, Enflasyon Düzeltme işlemleri geri alınabilir mi?**

İki işleminde iptali Düzeltme Fişleri Toplu İptali adımından yapılır.

**Enflasyon Düzeltme işlemi ne işe yarar?**

Muhasebede bulunan bu işlem hesap planında düzeltilecek hesap olarak belirlenmiş Düzeltilecek Stok Hesapları ekranında tanımlı olmayan tüm hesaplar için verilen ay aralığına uygun endeksleri alarak taşıma işlemi yapar. İlk olarak kontrol edilen hesabın bakiyesinin olup olmadığıdır. Eğer hesabın düzeltme ayında bakiyesi sıfır ise düzeltmeye tabii tutulmaz. Hesabın bakiyesi varsa her ayın işlemi ilgili ayın endeksi kullanılarak düzeltilir. Örneğin hesabın Şubat bakiyesi için taşıma katsayısı (Taşıma işleminin Haziran ayında yapılacağını varsayarsak) Haziran / Şubat endeksinden bulunur. Kaydın ilk ve düzeltme sonrası değerleri arasındaki farka istinaden düzeltme fişi oluşur.

**Stok Döviz Çevrim işlemi ne işe yarar?**

Stok Döviz Çevrim sadece Toplulaştırılmış Yöntem Uygulaması "Hiçbiri" seçildiğinde yani gerçek yöntem tercih edildiğinde stok düzeltmelerinde kullanılan ilk adımdır. Bu işlem ile ilgili aydaki stok hareketlerinin firma döviz tipi enflasyon endeksleri için açılmış döviz tipi ve firma döviz tutarı stok hareketlerinde yazan fiyat olacak şekilde güncellenir. Bu işlem enflasyon düzeltmesinde kullanılacak değerleri bu sahalara taşıyan işlemdir.

**Stok Enflasyon Düzeltme işlemi ne işe yarar?**

Stok döviz çevrim ile dolan firma döviz fiyatları katsayılar yardımı ile düzeltilir ve düzeltilme sonucu oluşan giriş – çıkış tutar farkları stok hareketlerine E- Miktarsız Maliyet hareket tipi ile firma döviz tipi ve tutarı dolu olacak şekilde işlenir. Böylece gerçek tutarları bozmadan enflasyondan doğan farklar stok hareketlerinde ve raporlarında izlenebilir hale gelir.

**Stok Enflasyon Düzeltme işlemi geri alınabilir mi?**

Evet. Yapılan işlem sonrasında oluşan E tipli hareketlerin iptal edilmesi ve yeniden çalıştırma işleminin yapılması isteniyor ise Stok Enflasyon Düzeltme İptali çalıştırılır.

**Enflasyon Düzeltmeleri Parasal K-Z Virmanı işlemi ne işe yarar?**

Enflasyon düzeltme işlemleri sonucuna enflasyon fark ve enflasyon düzeltme hesaplarının çalıştığı yevmiye fişleri oluşur. Bu fişlerle oluşan enflasyon düzeltme tutarlarının 698 hesaptan 648 hesaba taşınması gerekir. Bu işlem Enflasyon Düzeltmeleri Parasal K-Z Virmanı ile sağlanır.

**Stok hareketlerinde enflasyonun etkisindeki birim maliyet izlenebilir mi?**

Stok enflasyon düzeltme sonrası oluşan E tipli hareketler maliyet oluşturma işleminde dikkate alınır. Enflasyonsuz değerler birim maliyete(STHAR_IAF) yazılırken, düzeltilmiş maliyetler firma döviz maliyet(FIRMA_DOVMAL) sahasına yazılır. Serbest Maliyet Ambar Raporu "Dövizli Maliyet" seçeneği ile Stok Hareket Dökümü "Tutarlar Firma Döviz Tipine Göre Basılsın" ve "Maliyet Fiyatı Baz Alınsın" seçenekleri ile alınarak giriş-çıkış tutarları, birim maliyet ve kalan tutarın düzeltilmiş maliyetle raporlanabilmesi sağlanır.

**2023 sonu stok maliyetlerinde ve bakiye tutarlarında oluşan enflasyon farkının 2024 yılına etki etmesi için nasıl bir yol izlenmeli?**

Bunun için iki yöntem bulunur.

Yöntem 1: Devir ile gelen kaydın fiyat bilgisini düzeltilmiş fiyat olarak düzeltmektir. Aşağıdaki örnek için 100 olarak gelen fiyat 147,5 olarak değiştirilebilir.

Yöntem 2: 2023/12 düzeltmesi sonucu oluşmuş enflasyon farkı 2024 Ocak ayına <u>E tipli, Fiş No bilgisi dolu, Açıklama alanı DEV ile başlayan, Döviz tipi ve Döviz tutarı 0 ve TL fiyatı fark tutarı</u> olacak şekilde elle girilir.

Örn: 2024 Ocak itibari ile 2023 bakiyesi olarak 100 TL den 50 adet ürün var. Bunun 31.12.2023 düzeltmeleri sonucunda oluşan birim maliyeti ise 145,7 olduğunu varsayalım;

![](../../_assets/afa408d43934ff45d103.png)

Birim maliyetteki artış bakiye miktar ile çarpılarak Ocak ayına girilir.

Yani;

(145,7 \* 50 ) – (100\*50) =2285,18

![](../../_assets/58a64e7b72a9038665c4.png)

**Maliyet Muhasebesinin kullanıldığı durumlarda 2023 sonu stok maliyetlerinde oluşan farkın 2024 yılına etki etmesi için nasıl bir yol izlenmeli?**

Maliyet muhasebesinin kullanıldığı durumda Mamuller ve Yarı Mamuller için “Maliyet Bilgi Girişi” ekranındaki devir kaydı düzeltilmiş fiyat ile oluşturulur.

“Muhasebe Parametreleri” ekranında “Toplulaştırılmış Yöntem” parametresi “Hiçbiri” olarak seçilmiş ise (detaylı takip yapılıyorsa) “Döv. Maliyet Girişi” sekmesindeki “Döv.Ort.Maliyet” sahasına da düzeltilmiş birim fiyatın aynısı yazılır.

Aşağıdaki örnekte M10 mamulü için düzeltilmiş birim maliyet olan 20 TL için devir kaydı oluşturulmuştur. Bu mamul için devir kayıtları ile gelen birim maliyet 10 TL olmasına rağmen, enflasyon düzeltmesi yapılmış birim maliyet (20 TL) manuel olarak hesaplanarak ilgili ekran üzerinden girilmelidir.

![](../../_assets/97b1ed63e5283f10b0de.png)

**Yeniden değerleme ile enflasyon düzeltmesi aynı işlem midir?**

Değildir. Yeniden değerleme enflasyon şartları sağlanmasa da firmalara tanınabilen tek seferlik ya da sürekli değerleme hakkıdır. Enflasyon düzeltmesi ise seçimli değildir. Firmalar her vergi döneminde enflasyon düzeltmesi çalıştırır.

**Demirbaş uygulamasında enflasyon düzeltmesi için yapılması gereken tanımlar nelerdir?**

- Netsis Sıra Numarası "Aylık Enflasyon Oranları" olan bir döviz tipi tanımlanır ve bu döviz tipi Parametre Girişi / Dövizli Muhasebe sekmesindeki "Enf.Muh.Düz. Tipi" alanına bağlanır.
- Döviz Kurları Girişi ekranından "Tüm Enflasyon Oranlarını Güncelle" işlemi çalıştırılır ya da her ayın son gününe ait Yİ-ÜFE endeks bilgisi elle girilir.
- Parametre Girişi/ Dövizli Muhasebe ekranında "TL Muhasebe" seçilir.

**Demirbaş uygulamasında enflasyon düzeltmesi nasıl yapılır?**

2023/12 Değerleme ve Amortisman Ayırma işlemi yapıldıktan sonra bir defaya mahsus "Enflasyona Başlama" işlemi çalıştırılmalıdır. İşlem, seçilen tarih ile yeni dönemde dikkate alınacak düzeltilmiş değerlerin oluşmasını sağlar. Bundan sonraki ilk taşımada dikkate alınacak tutarlar bu işlem ile hesaplanır ve TBLAMORTISMANDEV tablosuna yazılır ve "Enflasyon Muhasebesi Devir Bilgileri" ekranından izlenir.

**Enflasyona Başlama işlemi iptal edilebilir mi?**

Enflasyon Muhasebesi Devir İptali işlemi ile iptal edilebilir.

**Enflasyona başlama işlemi düzeltilmiş değerleri bulurken hangi endeksi baz alır?**

Düzeltme işleminde baz alınacak endeks varlığın alış tarihidir. Ancak demirbaşlar için yeniden değerleme işlemleri söz konusu olduğu için burada öncelik varsa yeniden değerleme yapıldığı tarihtir. Özetle yeniden değerlemeye tabi bir demirbaş için düzeltme katsayısı 2023/12 endeksi, son değerleme tarihindeki endekse bölünerek bulunur. Değerleme görmemiş bir demirbaşta ise baz endeks alış tarihidir. Eğer demirbaş 2005 yılı öncesinde alınmış ve hiç değerleme görmemişse 2004 sonu enflasyon düzeltmesine tabi olduğu varsayılır ve enflasyon düzeltmesi baz alınarak 2005/1 endeksi kullanılır.

**Değerleme ve Amortisman Ayırma işleminde "Değerleme Durumu" sahasının Enflasyon Düzeltme olarak pasif seçili gelmesinin nedeni nedir?**

Enflasyona başlama çalıştırdıktan sonra VUK kapsamında yeniden değerleme yapılamayacağı için Enflasyon Düzeltme pasif seçili olarak gelmektedir. Enflasyon devir iptali ile alan aktif hale getirilir.

**2023.12 sonu demirbaş düzeltilmiş değerleri elle hesaplayıp excelden içeriye almak için nasıl bir yol izlemeliyiz?**

2023.12 Değerleme ve Amortisman Ayırma işlemi çalıştırdıktan sonra Enflasyona Başlama çalıştırılmalıdır. Bu işlem ile TBLAMORTISMANDEV tablosu dolacaktır. Dışarıda hazırlanmış excel dosyası bu tablo yapısına göre düzenlenip bu tablo içine güncelleme olarak alınır.

**İtfa olan demirbaş için enflasyon düzeltme yapılabilir mi?**

VUK itfa demirbaşlarla ilgili düzeltmeyi mükellefin seçimine bırakmıştır. Eğer itfa demirbaş için düzeltme yapılacaksa DEMIRBAS/ITFASONRASIAMORTISMAN özel parametresi tanımlandıktan sonra 12. Ay için Değerleme ve Amortisman Ayırma işleminin yapılmalıdır. Bu durumda itfa demirbaş için amortisman tablosuna kayıt atılacak ve Enflasyon Başlama çalıştırıldığında bu demirbaş içinde düzeltilmiş değerler oluşacaktır.

**Enflasyona Başlama çalıştırdıktan sonra demirbaşın düzeltileceği endeksi yeniden değerleme olmasına rağmen alış tarihinden alıyorsa nedendir?**

TBLAMORTISMAN.DEGERLEMEDURUMU boş olan yeniden değerleme satırları düzeltme işleminde izlenemediği için bu kolon 298/Ç değerlemeleri için "3", Madde32 değerlemeleri için "2" olarak update edilmelidir.

**Enflasyona Başlama işlemi ile oluşan yeni değerler ile eski değerler arasındaki fark nasıl muhasebeleştirilir?**

2023 düzeltmesi olarak adlandırdığımız geçmişe yönelik bu düzeltmeye ait fark tutarının muhasebe kaydı, Temelset tarafında olduğu gibi düzeltme fişi içerisine elle girilir.

**2023 için muhasebeye işlenecek fark tutarını raporlayabilir miyiz?**

Enflasyona Başlama işlemi sonrasında oluşan eski-yeni değerler ve fark tutarları Rapor/Enflasyon Muhasebesi Devir Bilgileri raporu yardımı ile izlenebilir.

**2024 yılında demirbaşlar için enflasyon taşıma işlemleri nasıl yapılacak?**

2023 yılı için Enflasyon Başlatma çalıştırdıktan sonra enflasyon taşıma yapılacak aylarda Değerleme ve Amortisman Ayırma işlemi Değerleme Durumu “Enflasyon Düzeltmesi” seçeneği ile çalıştırılır. Bu işlemin doğru değerlere ulaşması için Döviz Kurları Girişi ekranından ilgili ayın endeksi indirilmiş ve Değerleme Oran Girişi ekranından ilgili yıl ve ay bilgisi girilerek "Enf.Göre Oran Getir" işleminin çalıştırılmış ve gelen oranın kaydedilmiş olması gerekir. Gelen oran (oran/100 )-1 formülü ile katsayıya çevrilir ve sabit kıymet ile birikmiş amortismana uygulanır.

**2024 yılında Değerleme ve Amortisman Ayırma işleminde otomatik olarak oluşacak olan enflasyon farkları nasıl muhasebeleştirilir?**

Demirbaş Detay Kodu Tanımlama ekranında bulunan "Enf.Düz.Sabit Kıymet" ve "Enf.Düz.Amortisman" sahalarına enflasyon artışlarında kullanılacak hesapların tanımlanması halinde Amortisman Hisse Muhasebeleştirme işleminde fark tutarlarının bu hesap kodlarına atılması sağlanır.
