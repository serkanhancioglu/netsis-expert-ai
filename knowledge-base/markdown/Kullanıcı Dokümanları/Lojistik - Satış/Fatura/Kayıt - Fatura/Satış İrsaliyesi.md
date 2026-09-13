---
title: "Satış İrsaliyesi"
page_id: "22803525"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Fatura"
  - "Kayıt / Fatura"
  - "Satış İrsaliyesi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Fatura / Kayıt / Fatura / Satış İrsaliyesi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTIyM2JkYjQ4LTc2YWYtNDMwOC1iMzRhLThkMDFkZDE2YWY0MCZsaW5rPTFiYjVlNGQyLWRjODUtNDE1Zi05MmYwLWIyNjk3MTJhZjUwYiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=223bdb48-76af-4308-b34a-8d01dd16af40&link=1bb5e4d2-dc85-415f-92f0-b269712af50b&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "satis-irsaliyesi_22804783_22803525.html"
source_version: "2022-10-24T10:50:41.553+03:00"
source_bytes: 123208
fetched_at: "2026-09-13T04:01:43+00:00"
generator: "netsis-scraper 1.0.0"
---
# Satış İrsaliyesi

Satış irsaliyesi bölümü, satışların mal sevkiyatı sırasında (fatura aşamasından önce sevk irsaliyesi düzenlendiği durumlarda) sevk irsaliyesi kayıtlarının girildiği, düzenlendiği ve izlendiği bölümdür.

Satış irsaliyesi, Lojistik-Satış Bölümü’nde, fatura kayıt menüsünün altında yer alır. Sipariş Bilgileri, Üst Bilgiler, Koşul Bilgileri, Kalem Bilgileri, Toplamlar sekmelerinden oluşur.

Bu bölümlerden bazıları, belirli parametrelerin işaretlenmesi sonucu ekranda görünür.

**Sipariş Bilgileri**

Sipariş Bilgileri, sipariş takibi yapan firmalarda, müşteri siparişlerinden satış irsaliyesi oluşturulması için kullanılan bölümdür.

Sipariş Bilgileri sekmesi, sipariş takibi yapıldığı durumlarda, girilen müşteri siparişlerinin teslimatının yapılabilmesi amacıyla kesilen irsaliyeler için, tüm bilgilerin en baştan tekrar girilmesi yerine, daha önceden girilen müşteri siparişlerinden irsaliye oluşturulmasını sağlar.

Satış İrsaliyesi modülüne girildiğinde, Sipariş Bilgileri sekmesinin ekrana gelmesi için mutlaka, [Satış Fatura Parametrelerinde](<Satış Faturası/index.md>) bulunan “Sipariş Takibi Yapılsın” parametresinin işaretlenmiş olması gerekir.

Satış İrsaliyesi ekranı Sipariş Bilgileri sekmesinde yer alanlar ve içerdiği bilgiler şunlardır:

| Satış İrsaliyesi Ekranı |  |
| --- | --- |
| Belge Tipi | Sipariş ve İrsaliye seçeneklerinden oluşur. Satış irsaliyesi sipariş bağlantılı ise sipariş seçeneği işaretlenir. |
| Belge Numarası | Satış irsaliyesi sipariş belge numarasının, rehber ![](../../../../_assets/088477bb321d1b20c939.jpg) tuşu ile seçim yapılarak girildiği alandır. Siparişlerin teslim edilen/kalan bazında takibinin sağlıklı olarak yapılabilmesi için faturanın bağlantılı olduğu sipariş numarasının doğru olarak girilmesi gerekir. |
| Teslim Cari Kodu | Siparişin teslim edildiği yerin, rehber ![](../../../../_assets/088477bb321d1b20c939.jpg) tuşu ile seçim yapılarak girildiği cari kod alanıdır. İrsaliyenin kesildiği cari hesap/adres ile, stokların teslim edileceği cari hesap/adresin farklı olması halinde kullanılır. |
| İrsaliye Oluştur | Belge Numarası” alanı ve/veya “Detaylı Sipariş/İrsaliye Rehberi” alanı seçilerek irsaliye oluşturmayı sağlar. Butona tıklandığında, oluşturulacak irsaliyeye ilişkin numara ve tarih bilgilerinin yer aldığı **“Sipariş Teslimatınız Yapılsın Mı?”** başlıklı ekran gelir. Burada **“Tamam”** butonuna basıldığında, seçilen siparişte bulunan bilgiler irsaliyeye aktarılır ve istenirse aktarılan bilgiler üzerinde değişiklik yapılabilir. |
| Detaylı Sipariş/İrsaliye Rehberi Cari Kodu | İrsaliyesi oluşturulacak sipariş belgelerine kısıt vermek için kullanılan alandır. İrsaliyenin oluşturulması aşamasında, sipariş bilgilerinin detaylandırılarak girildiği müşterinin kodudur. Rehber ![](../../../../_assets/088477bb321d1b20c939.jpg)tuşu ile cari kod seçimi yapılır. |
| Detaylı Sipariş/İrsaliye Rehberi Belge Numarası | İrsaliyesi oluşturulacak sipariş numarasının girildiği alandır. Tek bir siparişe ait irsaliye işlemi yapılacaksa bu bölüm kullanılabilir. Cari kodun girilip bu alanın boş geçilmesi halinde, ilgili cariye ait tüm siparişler listelenir. |
| Mal Detaylı Mı? | “Mal detaylı mı?” sorusu işaretlendiğinde, müşterinin kalan siparişleri mal bazında detaylı listelenir. İşaretlenmediğinde, belirlenen cari koda ait, teslimi yapılmamış (kalan) sipariş numaralarının yer aldığı liste üzerinden, istenilen siparişler farenin sol tuşu çift tıklanarak işaretlenebilir. Böylece faturalama işlemlerinde siparişler birleştirilerek faturalandırılır fakat mal detayları izlenemez. |
| Stok Kısıdı Verilebilsin | Ekranın altında listelenecek sipariş kalemleri için kısıt verilmesi amacıyla kullanılan seçenektir. Bu seçeneğin aktif olması için “Mal Detaylı Mı?” sorusunun işaretlenmesi gerekir. “Stok Kısıdı Verilebilsin” seçeneği işaretlendikten sonra “Belgeleri Getir” butonuna basıldığında, listelenecek sipariş kalemlerinin belirlenmesi için “Stok Kısıt Ekranı” gelecektir. Bu ekranda bulunan **Saha** **Adı** sütunundaki hücreye tıklandığında, stok ilişkili alanlar listelenir. Bu listede, kısıt verilecek alan seçildikten sonra, “Operatör” ve “Değer” alanları kullanılarak istenen kısıt verilir. |
| Sıralama | Belge no, teslim tarihi, koşul kodu, belge tarihi, stok kodu, stok adı seçeneklerini içerir. Listelenecek sipariş belgelerinin seçilecek alanlara göre sıralanmasını sağlar. |
| Belgeleri Getir | Cari kod ve mal detayı bilgileri baz alınarak, sipariş belgelerinin listelenmesini sağlayan butondur. |

**Sipariş Bağlantılı Satış İrsaliyesi Kaydı**

Müşteri siparişlerinin irsaliye kaydı iki yöntemle yapılır:

- "Satış İrsaliyesi" modülüne girildiğinde gelen Sipariş Bilgileri sayfasında, irsaliyesi oluşturulacak sipariş kalemlerinin seçilmesi gerekir.
- "Kalem Bilgileri" ekranında bulunan "Sipariş Numarası" alanının kullanılmasıdır.

**Üst Bilgiler**

Satış İrsaliyesi ekranı Üst Bilgiler sekmesi alanları ve içerdiği bilgiler şunlardır:

| Satış İrsaliyesi Ekranı |  |
| --- | --- |
| Numara | İrsaliyenin programdaki takip numarasıdır. |
| Cari Kodu | İrsaliyenin ait olduğu cari hesabın kodudur. |
| Tarih | İrsaliyenin üzerinde yazan tarihin girileceği alandır. |
| Entegre Tarih | İrsaliyenin muhasebeye işlenme tarihidir. |
| Fiili Tarih | İrsaliyenin gerçekleştiği tarihin girileceği alandır. |
| Döviz Bazında Tarih | İrsaliyelerde geçerli olacak kur bilgisinin, hangi tarihe göre baz alınacağının belirlendiği alandır Ekrana Döviz Bazında Tarih alanının eklenmesi için, "[Satış Fatura Parametreleri](<Satış Faturası/index.md>)" Genel 4 sekmesinde yer alan "Döviz Takibi Yapılsın" parametresi ve Yardımcı Programlar→ Şirket→ Şube→ Parametre kayıtlarında bulunan "Döviz Uygulaması" parametresinin işaretli olması gerekir. |
| Tipi | Faturanın hangi tipte kesileceğinin sorgulandığı bölümdür. Kapalı, açık, muhtelif, iade, zayi iade, ithalat/ihracat tiplerinden biri seçildiğinde, seçilen tipe göre irsaliyeler faturalandırılarak entegre bölümlere işlenir. |
| İhracat/İthalat | Bu seçenek işaretlenerek kaydedilen bir satış irsaliyesi, ihracat kaydı sayılır. Bilindiği üzere ihracat işlemlerinde ilk olarak proforma fatura kullanılır. Bu fatura toplamı da cari hareketlere yansır. İhracat tipi işaretlenerek kesilen satış irsaliyesindeki stokların hareket kayıtlarında, miktarsal bir değişim söz konusu olmaz. Miktar bilgisi stok hareketlerinde başka bir alanda tutulur. İlgili ihracat kaydına ait kapatma kaydı, Dekont Modülünden "İhracat Kapatma" seçeneği kullanılarak yapılır. |
| İhracat/İthalat Tipi | Tipi alanında "İthalat/İhracat" seçilmesi halinde aktif olan alandır. Bir ihracata ait, dekont modülünden yapılan işlemler sonucu oluşan faturada, kesilen irsaliyede belirtilen ihracatın tipi bu alana yansır. Kullanıcıların elle ithalat/ihracat ve tipi sahalarını kullanarak fatura kesmemeleri gerekir. Bu alandaki tipler sadece ihracat amacıyla kaydedilen satış irsaliyeleri için kullanılır. İhracat tipinin doğru şekilde seçilmesi önemlidir. **Fob (Free On Board-Gemi Bordasında Teslim):** Yükleme limanına kadar yanaşan vapurun vinç ya da bordasına kadar masraflarının satıcıya (firmaya), geri kalanının da alıcıya (müşteriye) ait olduğu ihracat şeklidir. **CIF (Cost, Insurance and Freight- Mal Bedeli, Sigorta ve Navlun):** Mal bedeli, sigorta primi ve nakliye bedelinin satıcıya (firmaya) ait olduğu ihracat şeklidir. **Cf (Cost and Freight-Mal Bedeli ve Navlun):** Mal bedeli ve nakliye bedelinin satıcıya (firmaya) ait olduğu ihracat şeklidir **Fot (Free On Train-Trende Teslim):** Hareket istasyonunda trenin vinç ya da vagonuna kadar olan masrafların satıcıya (firmaya) geri kalanının da alıcıya (müşteriye) ait olduğu ihracat şeklidir. **İhr. Kayıt:** Malların yurtdışına satılması şartı ile yurtiçine satışının yapılması halinde kullanılan tiptir **Daf (Delivered At Frontier-Sınırda Teslim):** Sınırda belirlenen yere kadar olan masrafların satıcıya (firmaya) geri kalanların da alıcıya (müşteriye) ait olduğu ihracat şeklidir. **Exw (Ticari İşletmede Teslim):** "Ex works", satıcının (firmanın) malları kendi işletmesinde (fabrika, depo v.b), alıcının (müşteri) emrine hazır halde bulundurmasıyla yükümlü olduğu anlamına gelir. Satıcı (firma), aksi kararlaştırılmadıkça malın alıcı tarafından sağlanan bir araca yüklenmesinden ya da ihraç gümrüğünden geçirilmesinden sorumlu değildir. Alıcı bu noktadan itibaren varış yerine kadar, malın taşınması ile ilgili tüm gider ve risklerin yükümlülüğünü taşır. Bu teslim şeklinde sözleşmede belirtilen satış bedeline yalnızca ambalajlanmış mal bedeli dahildir. Yani teslim tarihinden itibaren her türlü nakliye, yükleme, boşaltma ve sigorta masrafları alıcı tarafından ödenir. |
| İhr. Kur Farkı | İhracat işlemlerine ait kur farkı faturalarının girişi için kullanılan alandır. |
| Export Referans No | Export Referans Numarası, sadece ihracat tipli faturalarda dolu olacaktır. Firmalar, yaptığı her ihracata bir numara vermesi gerekir. Programda İhracat faturası oluşturulması için öncelikle, ihracat tipli satış irsaliyesinin girilmesi gerekir. Finans Modülü→ Dekont→ Kayıt→ İthalat/İhracat İşlemleri → "İhracat Kapatma" bölümünden "Referans No" seçilerek ihracat faturası oluşturulur. İhracat işlemleri tamamlandığında program tarafından oluşturulan ihracat faturasına, irsaliyede girilen Export Referans Numarası aktarılır. |
| Özel Kod-1 | Tanımlanan Özel Kod-1 seçenekleri arasından, rehber ![](../../../../_assets/088477bb321d1b20c939.jpg) tuşu ile seçim yapılarak, irsaliyelerin belli kodlar altında gruplanmasını sağlayan alandır. Örneğin, Peşin satışlar ayrı, vadeli satışlar ayrı bir satış hesabında gruplanabilir Ekrana Özel Kod-1 alanının eklenmesi için, [Satış Parametreleri](<Satış Faturası/index.md>) Özel Kod ve Açıklama sekmesinde yer alan "Özel Kod - 1" parametresinin işaretli olması gerekir. |
| Özel Kod-2 | Tanımlanan Özel Kod-2 seçenekleri arasından,![](../../../../_assets/088477bb321d1b20c939.jpg) tuşu ile seçim yapılarak, irsaliye kayıtlarının rapor bazında gruplama yapılmasını sağlayan alandır. Ekrana Özel Kod-2 alanının eklenmesi için, [Satış Parametreleri](<Satış Faturası/index.md>) Özel Kod ve Açıklama sekmesinde yer alan "Özel Kod - 2" parametresinin işaretli olması gerekir. |
| Açıklama | Satış irsaliyesine ait açıklama bilgisinin girildiği alandır Ekrana Açıklama alanının eklenmesi için, [Satış Parametreleri](<Satış Faturası/index.md>) Özel Kod ve Açıklama sekmesinde yer alan "Açıklama" parametresinin işaretli olması gerekir. |
| Proje Kodu | Tanımlanan proje kodları arasından, rehber ![](../../../../_assets/088477bb321d1b20c939.jpg) tuşu ile seçim yapılarak, istenildiğinde proje bazında rapor alınabilmesi için girilen koddur. |
| Plasiyer Kodu | Tanımlanan plasiyer kodları arasından, rehber ![](../../../../_assets/088477bb321d1b20c939.jpg) tuşu ile seçim yapılarak, ilgili müşteriye ait plasiyer kodunun girildiği alandır. |
| Kdv Dahil mi? | KDV'nin nasıl uygulanacağının belirlendiği alandır. KDV dahil kutucuğu işaretlendiği takdirde, stoka ait birim fiyatı, KDV tutarını da içerir. Ekrana Kdv Dahil mi? alanının eklenmesi için, [Satış Parametreleri](<Satış Faturası/index.md>) Fatura KDV sekmesinde yer alan "KDV Dahil/Hariç Sorusu Her Faturada Sorulsun" parametresinin işaretli olması gerekir. |
| Bağlantı No | Girilen belgenin hangi bağlantıya ait olduğunun izlendiği alandır. |
| Toplu Depo | Tanımlanan depo kodları arasından, rehber ![](../../../../_assets/088477bb321d1b20c939.jpg) tuşu ile seçim yapılarak, ilgili depo kodunun girildiği alandır. Satış parametreleri kısmında bu parametre işaretlenmediği takdirde, her stok kalemi için ayrı ayrı lokal depo kodu girilmesi gerekir. Ekrana Toplu Depo alanın eklenmesi için, [Satış Parametreleri](<Satış Faturası/index.md>) Genel 2 sekmesinde yer alan "Fatura/İrsaliyelerde Toplu Depo Kodu Kullanılsın" parametresinin işaretli olması gerekir. |
| Nakliye Katsayısı | Tanımlanan nakliye katsayısı girişinin yapıldığı alandır Ekrana Nakliye Katsayısı alanın eklenmesi için, [Satış Parametreleri](<Satış Faturası/index.md>) Fatura Ek 1 sekmesinde yer alan "Fatura/İrsaliyelerde Nakliye Katsayısı Girişi Yapılsın" parametresinin işaretli olması gerekir. |
| Değişsin | Dövizli belgelerde bazen (yuvarlama kaynaklı) döviz fiyatının, kurun ya da TL fiyatının değişmesi gerekir. Böyle durumlarda, hangi alandaki bilginin değişeceği "Değişsin" alanı kullanılarak belirlenir. Alanın sağ tarafında yer alan aşağı ok butonu ile Döviz Fiyatı, Kur ve Fiyat seçenekleri arasından seçim yapılır. |
| Farklı Teslimat | İrsaliyenin kesildiği cari hesap/adres ile, stokların teslim edileceği cari hesap/adresin farklı olması halinde kullanılan bölümdür Ekrana Farklı Teslimat alanın eklenmesi için, "Alış Parametreleri" Genel 3 sekmesinde yer alan "Sipariş/İrsaliye/Faturada Farklı Teslim Yeri Kullanılsın" parametresinin işaretli olması gerekir. |
| Kod | Basıma yönelik adres bilgisi değişikliği için girilen alandır. Buradaki Cari Kod, irsaliyenin kesildiği kodun aynısı olmalı. |
| İsim | Kod alanına girilen cari kodun isim bilgisinin, program tarafından ekrana getirildiği alandır. |
| Adres | Teslimat yapılacak adres bilgisinin, cari hesabın koduna göre program tarafından ekrana getirildiği, kullanıcı tarafından da değişikliğinin yapılabileceği alandır. |
| İlçe | Teslimat yapılacak ilçe bilgisinin, cari hesabın koduna göre program tarafından ekrana getirildiği, kullanıcı tarafından da değişikliğinin yapılabileceği alandır. |
| İl | Teslimat yapılacak il bilgisinin, cari hesabın koduna göre program tarafından ekrana getirildiği, kullanıcı tarafından da değişikliğinin yapılabileceği alandır. |
| Cari Bilgiler/İsim, Açıklama-1, Açıklama-2, Açıklama-3 | Kesilen irsaliyenin müşteriye ait kod bilgisi girildiğinde, cari hesap kayıtlarında bulunan isim ve açıklama bilgilerinin program tarafından ekrana getirildiği alanlardır. İrsaliye kaydı sırasında bu alanlara müdahale edilemez, sadece bilgi amaçlı olarak görüntülenir. |
| Ek Sahalar | Açıklama girişi için kullanılan alanlardır. Ekrana Ek Sahalar alanının eklenmesi için, [Satış Parametreleri](<Satış Faturası/index.md>) Genel 5 sekmesinde yer alan "Sipariş/İrsaliye/Faturada Ek Sahalar Kullanılsın " parametresinin işaretli olması gerekir. |

Özel Kod-1, Özel Kod-2, Açıklama, Plasiyer Kodu, Proje Kodu, KDV Dahil, Toplu Depo, Nakliye Katsayısı, Farklı Teslimat (kod, isim, adres, ilçe, il), Cari Bilgiler/İsim, Açıklama-1 Açıklama-2 Açıklama 3 ve Ek Sahalardan oluşan alanlar, [Satış Fatura Parametreleri](<Satış Faturası/index.md>) sayesinde isteğe bağlı olarak ekranda yer alabilir/almayabilir.

**Koşul Bilgileri**

Satış İrsaliyesi Koşul Bilgileri, satış irsaliyesine ait geçerli koşul bilgileri alanlarının yer aldığı ekrandır.

Satış İrsaliyesi ekranı Koşul Bilgileri sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Satış İrsaliyesi Ekranı |  |
| --- | --- |
| Koşul Kodu | Tanımlaması yapılan koşulun, rehber ![](../../../../_assets/088477bb321d1b20c939.jpg) tuşu ile seçim yapılarak ekrana getirildiği koddur. |
| Vade Günü | Bir borcun ödenmesi için tanınan süredir. Bu alana vade günü girildiğinde, tanımlanan vade için belirlenen liste fiyatı, kalem bilgileri ekranındaki fiyat sahasına otomatik olarak yansır. |
| Koşul Tarihi | Koşul tarihinin girildiği alandır. Bu alanda tarih, otomatik olarak ekrana gelir. Eğer koşul tarihi değiştirilirse, satışın girildiği tarihte geçerli olan fiyata göre vade ve iskonto uygulaması yapılır. |
| Fiyat Tarihi | Satış fiyat liste tarihinin girildiği alandır. |
| Ödeme Kodu | İrsaliye kaydı sırasında, koşula bağlı ödeme planının kodu girilmişse, ilgili ödeme kodunun rehber ![](../../../../_assets/088477bb321d1b20c939.jpg) tuşu ile seçim yapılarak ekrana getirildiği alandır. Cari/Koşul Kayıtları/ Genel Koşul Kayıtları/ Koşul Genel-2 sayfasında bulunan ödeme kodu alanına, o koşula bağlanacak ödeme planının kodu girilmiş ise, ilgili ödeme kodu bu alana program tarafından otomatik getirilir. İrsaliye belgelerinde koşul uygulamasının olduğu, ancak koşula bağlı ödeme planının olmadığı durumlarda ödeme kodu alanı boş olur ve istenen ödeme planına ait kod girilebilir. İrsaliye belgelerinde, cari ödeme planlarının koşul bağlantılı uygulanabilmesi için, **Koşul Sabit Kayıtları**nda bulunan “Cari Hesap Vadelere Bölünerek Atılsın” seçeneğinin işaretlenmesi gerekir. Koşul uygulamasının kullanılmadığı durumlarda bu alan, "Koşul Bilgileri" ekranı yerine "Üst Bilgiler " ekranında yer alır. |

Koşul bilgilerindeki tüm alanların ekranda yer alabilmesi için**, [Satış Parametreleri](<Satış Faturası/index.md>) Koşul ekranında yer alan "Sipariş****/İrsaliye/Faturada Koşul Uygulaması Kullanılsın"** parametresinin işaretli olması gerekir.

**Kalem Bilgileri aşağıdaki şekildedir:**

Satış İrsaliyesi Kalem Girişi, Açıklama ve Kalem Listesi alanlarının yer aldığı ekrandır.

Satış irsaliyesi sekmesi Kalem Bilgileri ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Satış İrsaliyesi Ekranı |  |
| --- | --- |
| Kod | Teslimatı yapılan stok kaleminin, rehber ![](../../../../_assets/088477bb321d1b20c939.jpg) tuşu ile seçim yapılarak ekrana getirildiği koddur. |
| İsim | Stok sabit kayıtlarında kaydedilen stok isminin, program tarafından ekrana getirildiği alandır. |
| Sipariş No | Her malın ayrı ayrı sipariş numarasının girilmesini sağlamak için kullanılan alandır. Rehber ![](../../../../_assets/088477bb321d1b20c939.jpg) tuşu ile stoklar için girilmiş tüm siparişlere ulaşılarak seçim yapılır. İrsaliye, sipariş bağlantılı kesilmeyecek ise, bu alan boş bırakılarak \<tab\> butonu ile ilerlenir. Sipariş numarası olmadığı ya da yanlış girildiği durumlarda, program “**Sipariş Bulunamadı**” şeklinde bir uyarı verir. Sipariş bulunduğu zaman, o siparişle ilgili teslimi bekleyen mallar, kalan miktarları ve sipariş tutarlarıyla birlikte otomatik olarak irsaliye ekranına gelir. Ekrana Sipariş No alanının eklenmesi için, [Satış Parametreleri](<Satış Faturası/index.md>) Fatura Sipariş sekmesinde yer alan "İrsaliye/Faturada Sipariş No. Mal Bazında Sorulsun" parametresinin işaretli olması gerekir. |
| D.Kd (Depo Kodu) | Tanımlaması yapılan depo kodunun, rehber ![](../../../../_assets/088477bb321d1b20c939.jpg) tuşu ile depo seçimi yapılarak, her malın ayrı ayrı depolarda takip ve raporlanmasını sağlamak amacıyla kullanılan alandır. |
| Yapılandırma Kodu | Esnek yapılandırma uygulamasının kullanıldığı durumlarda, stoka ait yapılandırma kodunun girildiği alandır. |
| Yapılandırma Kodu Açıklaması | Yapılandırma kodu alanına girilen değere ait açıklama bilgisinin, program tarafından getirildiği alandır. |
| Yapılandırma Kod Sihirbazı | Belirli bir özellik kombinasyonu içeren yapılandırma kodunun, sistemde tanımlı yapılandırma kodları arasında olup olmadığını saptamak ve tanımlı değilse de hızlı tanımlama yapmak amacıyla kullanılan alandır. |
| Yapılandırılabilir Ürün Girişi | Birden fazla yapılandırma koduna ait çıkış miktarlarının, tek seferde kaydedilmesi için kullanıldığı alandır. |
| Tes.Cari Kod (Teslim Cari Kodu) | İrsaliyenin kesildiği cari hesap/adres ile, stokların teslim edileceği cari hesap/adresin farklı olması halinde, teslimatın yapılacağı cari hesap/adresin stok bazında belirlenmesi için kullanılan alandır. Ekrana Tes.Cari Kod alanının eklenmesi için, [Satış Parametreleri](<Satış Faturası/index.md>) Genel 3 sekmesinde yer alan "Satır Bazında Teslim Cari Kodu Sorulsun" parametresinin işaretli olması gerekir. |
| Satır Açıklama | Her kalem için, 10 ayrı ek açıklama girişinin yapılabileceği alandır. Ekrana Satır Açıklama alanının eklenmesi için, [Satış Parametreleri](<Satış Faturası/index.md>) Genel 6 sekmesinde yer alan "Satır Bazında Ek Açıklama Sorulsun" parametresinin işaretli olması gerekir. |
| Ç.Değ (Çevrim Değeri) | Stok kodu alanına girilen stoka ait, birden fazla ölçü birimi tanımlanmışsa, hangi ölçü birimi üzerinden miktar girileceğinin belirlendiği alandır. Alanın sağ tarafında bulunan aşağı ok tuşuna basılarak, o stok için tanımlanmış olan ölçü birimi seçilir. Girilen miktar otomatik olarak ölçü birimi değerine çevrilir ve sistem tarafından ekrana getirilir. Alanın sağ tarafında bulunan rehber, stokun bir ölçü birimine ait birden fazla çevrim değeri olması halinde çevrimin hangi değere göre yapılacağını seçmek amacıyla kullanılır. Ekrana Ç.Değ alanının eklenmesi için, [Satış Parametreleri](<Satış Faturası/index.md>) Genel 1 sekmesinde yer alan "Farklı Birimlerden Mal Çıkışı Yapılsın" parametresinin işaretli olması gerekir. |
| Seri Takibi | Satış irsaliyelerinin, seri numaralarına göre takibinin yapılması amacıyla kullanılan alandır. |
| Miktar 2 | Stok bazında takibin yapıldığı miktar alanıdır. Karma koli uygulamasının kullanıldığı durumlarda, koli stokuna ait miktar girişi için de kullanılır. Ekrana Miktar 2 alanın eklenmesi için, [Satış Parametreleri](<Satış Faturası/index.md>) Genel 2 sekmesinde yer alan "İkinci Miktar Sorulsun" parametresinin işaretli olması gerekir. |
| Fiyat Birim | İrsaliyedeki stok kalemlerinin kaydı sırasında, fiyat girmeden önce, eğer ilgili mal için stoklarda birden fazla ölçü birimi tanımlanmışsa (adet, kg, koli vb.), gireceğiniz fiyatın hangi ölçü birimine ait olduğunun seçildiği alandır. Ekrana Fiyat Birim alanının eklenmesi için, [Satış Parametreleri](<Satış Faturası/index.md>) Genel 1 sekmesinde yer alan "Fiyat Birimi Sorulsun" parametresinin işaretli olması gerekir. |
| Muhasebe Kodu | Hizmet faturası kesen firmaların, bu faturaları satır bazında ayrı hesaplarda muhasebeleştirebilmeleri için kullanılan alandır. Bu alan için tanımlanan muhasebe kodunun seçilmesi ile, ilgili satış faturasındaki hizmet kalemi için alacak hareketi oluşur. Hizmet faturası uygulaması, stok kartı kayıtlarında kodu "HIZ" ile başlayan stoklar için uygulanır. Dolayısıyla, hizmet uygulaması ile bu faturalardaki kalemleri ayrı hesaplarda muhasebeleştirmek isteyen firmaların, hizmet stoklarının kodunun ilk üç hanesini HIZ olarak açmaları gerekir.Ekrana Muhasebe Kodu alanının eklenmesi için, [Satış Parametreleri](<Satış Faturası/index.md>) Genel 1 sekmesinde yer alan "Hizmet Uygulaması" parametresinin işaretli olması gerekir. |
| Hesap İsmi | Muhasebe kodu alanına girilen hesap koduna ait isim bilgisinin program tarafından ekrana getirildiği alandır. |
| Vade Tarihi | Vade günü baz alınarak hesaplanan tarihin, program tarafından ekrana getirildiği alandır. Ekrana Vade Tarihi alanının eklenmesi için, [Satış Parametreleri](<Satış Faturası/index.md>) Genel 4 sekmesinde yer alan "Kayıtlarda Her Satırda Vade Tarihi Sorulsun" parametresinin işaretli olması gerekir. |
| Ek Alan-1 | İrsaliye basımına yönelik, anlık açıklamaların girildiği alandır Ekrana Ek Alan-1 alanının eklenmesi için, [Satış Parametreleri](<Satış Faturası/index.md>) Genel 2 sekmesinde yer alan "Ek Alan Kullanılsın" parametresinin işaretli olması gerekir. |
| Ek Alan-2 | Satış irsaliyeleri girilirken stok kalemleri bazında ikinci bir açıklamanın gerekliliği halinde kullanılan alandır. Her bir kalem için en fazla 14 karakter uzunluğunda açıklama girilir. Ekrana Ek Alan-2 alanının eklenmesi için, [Satış Parametreleri](<Satış Faturası/index.md>) Genel 2 sekmesinde yer alan "Ek Alan 2 Kullanılsın" parametresinin işaretli olması gerekir. |
| Miktar | İlgili stok kaleminin irsaliye üzerindeki teslimat miktarının yazıldığı alandır. Satış irsaliyesinde girilen stok kayıtları, irsaliye kaydı tamamlanmadan stok hareket kayıtlarına aktarılır. Bu sayede diğer terminallerden stok kontrolleri, irsaliye kaydının bitirilmesi işlemi beklemeden yapılabilir ve bakiyeleri izlenebilir. |
| M. Faz ( Mal fazlası) | Satılan malın yanında verilen hediye malların, irsaliyede gösterilmesi için kullanıldığı alandır. Burada hediye verilen miktar girilmelidir. Eğer satılan malın yanında hediye verilen mal farklı ise, miktar hanesine gerekli değer yazılır, mal fazlası hanesi boş bırakılır. Bir sonraki satıra hediye olarak verilen malın kodu yazılır ve bu mal için de miktar hanesi boş bırakılarak, mal fazlası hanesine hediye miktarı girilmesi ile kayıt oluşturulur. Ekrana M. Faz alanının eklenmesi için, [Satış Parametreleri](<Satış Faturası/index.md>) İskonto sekmesinde yer alan "Mal Fazlası İskontosu Uygulansın" parametresinin işaretli olması gerekir. |
| Dv. Tip (Döviz Tip) | Döviz takibinin yapıldığı alandır. Girilen stok kodu için, tanımlaması yapılan döviz satış tipi değeri, program tarafından ekrana getirilir. Bu alana getirilen değer, isteğe bağlı olarak farklı bir döviz tipi ile de değiştirilebilir. Döviz tipi olarak “0“ dan farklı bir değer seçilirse, ilgili kalemin dövizli olarak satıldığı, “0“ değeri seçilirse de TL olarak satıldığı anlaşılır. Ekrana Dv. Tip alanının eklenmesi için, [Satış Parametreleri](<Satış Faturası/index.md>) Genel 4 sekmesinde yer alan "Döviz Takibi Yapılsın" parametresinin işaretli olması gerekir. |
| Döviz Fiyat | Girilen stok kodu için, tanımlaması yapılan döviz fiyat değeri, otomatik ekrana gelir. İsteğe bağlı olarak, bu alana getirilen fiyat değiştirilebilir. Ekrana Döviz Fiyat alanının eklenmesi için, [Satış Parametreleri](<Satış Faturası/index.md>) Genel 4 sekmesinde yer alan "Döviz Takibi Yapılsın" parametresinin işaretli olması gerekir. |
| Döv.Kur | Üst bilgiler ekranında girmiş olduğunuz **Döviz Baz Tarihi** ile, **Döviz Takibi/Günlük Kur Girişi Bölümü’nden** girmiş olduğunuz kur tutarı, **Döviz Kur** alanına yansır. İsteğe göre değişiklik yapılabilir. Kur tutarı ile döviz fiyatı alanındaki değerlerin çarpımı sonucu çıkan rakam, fiyat alanına yansır. |
| Fiyat | İlgili malın, irsaliye üzerindeki birim fiyatıdır. |
| İsk.1-6 | İsteğe bağlı olarak 1’den 6’ya kadar kademeli şekilde ekranda yer alabilen, iskonto bilgisinin girildiği alandır. Sadece 1. İskonto için tutarsal iskonto girilebilir. Diğer kademeli iskontolarda, oran (%) bazında kayıt girilir. Hesaplamada malın brüt tutarından 1. iskonto düşüldükten sonra, kalan tutardan 2. iskonto düşülecektir. İkiden fazla iskonto kullanılması durumunda da, kalan tutar üzerinden diğer iskontolar düşülür. Ekrana İsk.1-6 alanının eklenmesi için, [Satış Parametreleri](<Satış Faturası/index.md>) İskonto sekmesinde yer alan "Kademeli Kaç İskonto Sorulsun" parametresinin işaretli olması gerekir. |
| İsk.1-6 Tip | İskontoları tiplerini muhasebe kodlarına bağlamak için kullanılan alandır. **Örneğin;** İskonto tip 1 için özel müşteriler iskontosu, iskonto tip 2 için mağaza iskontosu gibi kullanım amacına göre tanımlamalar yapıldıktan sonra belirlenen iskonto tipleri ile farklı muhasebe kodları çalıştırılabilir. |
| KDV | KDV oranının girildiği alandır. Ekrana KDV alanının eklenmesi için, [Satış Parametreleri](<Satış Faturası/index.md>) Fatura KDV sekmesinde yer alan "Her Satırda KDV Sorulsun" parametresinin işaretli olması gerekir. |
| Proje Kodu | Yapılan satışın proje bazında izlenmesini sağlayan alandır. Rehber ![](../../../../_assets/088477bb321d1b20c939.jpg) tuşu ile, ilgili proje seçimi yapılır. **Örneğin;** Firmaya ait, farklı bir konumda yeni bir bina inşa edilmesi durumu bir projedir. Projeye ait bir kod tanımlar ve ilgili projeye ait satışlarda bu kod seçilerek kayıt yapılırsa, gerektiğinde **söz konusu projeye ait** satışları bu kod sayesinde raporlanabilir. |
| Fiili Tarih | Üst Bilgiler sayfasında bulunan fiili tarih bilgisinin, kalem bilgilerine yansıtıldığı alandır. İsteğe bağlı olarak değiştirilebilir. |
| Tutar | Stok miktarı ile birim fiyatın program tarafından çarpılıp, brüt tutar olarak yazıldığı alandır. Bu alana müdahale edilemez. Sadece birim fiyat ve miktar hanelerinde yapılan değişiklikler tutarın değişmesine sebep olur. İrsaliyede girilen tüm stok tutarlarının toplamı, ekranın sağ alt köşesinde bulunan **Toplam Tutar** alanında görünür. |
| Top. Mik. (Toplam Miktar) | Sipariş bağlantılı fatura oluşturulduğunda, ilgili stok kalemi için seçilen sipariş/irsaliye kalemindeki miktar bilgisinin program tarafından ekrana getirildiği alandır. |
| Sip. Nolar (Sipariş Numaraları) | Sipariş bağlantılı irsaliye oluşturulduğunda, ilgili sipariş numarasının izlendiği alandır. |
| Bakiye | İrsaliyede girilen her stok kodu için, ilgili malın stok hareket kayıtlarındaki bakiyesinin, bilgilendirme amacıyla program tarafından ekrana getirildiği alandır. |

Yapılandırma Kodu, Yapılandırma Kodu Açıklaması, Yapılandırma Kod Sihirbazı, Yapılandırılabilir Ürün Girişi, Teslim Cari Kodu, Sipariş No, Satır Açıklama, Depo Kodu, Çevrim Değeri, Ek Alan-1 ve 2, Seri Takibi, Miktar 2, Mal Fazlası, Fiyat Birim, Döviz Tip, İsk.1-6, KDV, Muhasebe Kodu, Hesap İsmi, Proje Kodu, Vade Tarihi alanları, [Satış Parametreleri](<Satış Faturası/index.md>) sayesinde, isteğe bağlı olarak ekranda yer alabilir/almayabilir.

**Kalem Bilgilerinde Değişiklik/İptal**

Yukarıda açıklanan alanlara bilgi girişi yapıldıktan sonra \<tab\> butonu ile ilerleyerek veya F5 tuşuna basılarak, kalem bilgisi kaydedilir ve ekranda satır olarak görünür. İrsaliye kaydedilmemiş olmasına rağmen, satıra aktarılan stok satış bilgileri, stok hareket kayıtlarına da işlenir. Dolayısıyla, bu aşamada iken, faturanın tamamı yerine sadece stok çıkış hareketi kaydedilir.

Kaydedilen kalem üzerinde değişiklik yapılması istendiğinde, ilgili stok kalemi satırının üzerine çift tıklayarak seçim yapılması halinde, gerekli alan/alanların üzerinde değişiklik yapılabilir. Kaydedilen kalem aynı şekilde seçildikten sonra araç çubuklarında bulunan ![](../../../../_assets/2df4b343310bcd16b01e.jpg) kayıt silme butonu ya da klavyedeki F7 butonu yardımıyla ilgili kalem silinir.

**Toplamlar Sekmesi**

Toplamlar sekmesi; İskonto ve Maliyet Toplamları, KDV'ler Toplamı ve Genel Toplam, Kayıt Sorgulamaları alanlarının yer aldığı ekrandır.

Satış İrsaliyesi ekranı Toplamlar sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Satış İrsaliyesi Ekranı | İskonto ve Maliyet Toplamları |
| --- | --- |
| Brüt Toplam | İrsaliyede kaydedilen mal tutarlarının, iskonto düşülmeden önceki brüt tutarını gösteren alandır. Kalem bilgileri ekranındaki bilgilere göre oluşturulan bir alan olduğu için, elle değiştirme yapılamaz. Buradaki tutarın yanlış olması durumunda, önceki ekrana (kalem bilgileri) geçilerek gerekli düzeltme işlemleri yapılır. |
| Mal Fazlası İsk. | Kalem bilgileri ekranında mal fazlası alanı kullanılmışsa, program öncelikle mal fazlası (hediye) tutarını brüt olarak hesaplayacak, daha sonra iskonto şeklinde brüt tutardan düşecek. Bu alanda, irsailye kaydında mal fazlası olarak girilmiş bütün malların toplam tutarı ekranda görünür. Brüt tutardan ilk olarak düşecek iskonto, mal fazlası iskontosudur. Kalem bilgileri ekranındaki bilgilere göre oluşturulan bir alan olduğu için, elle değiştirme yapılamaz. Buradaki tutarın yanlış olması durumunda, önceki ekrana (kalem bilgileri) geçilerek gerekli düzeltme işlemleri yapılır. |
| Satır İskontosu | İrsaliye kaydı sırasında, satır bazında girilen tüm iskonto oran/ tutar toplamlarının program tarafından hesaplanarak ekrana getirildiği alandır. Brüt tutar ve mal fazlası iskontosundan sonra düşülecek ikinci iskonto, satır iskontosudur. Kalem bilgileri ekranındaki bilgilere göre oluşturulan bir alan olduğu için, elle değiştirme yapılamaz. Buradaki tutarın yanlış olması durumunda, önceki ekrana (kalem bilgileri) geçilerek gerekli düzeltme işlemleri yapılır. |
| Fat.Alt. İsk 1, 2, 3 | Genel iskonto 1-2-3 tanımlamaları yapılmış ise ekrana gelen alanlardır. Fatura Altı İskonto-1 alanı; cari hesap için girilen iskonto oranı varsa, bu oran üzerinden hesaplanan tutarın program tarafından ekrana getirildiği alandır. Hem tutar hem de oran değeri üzerinde istenen düzenleme yapılabilir. Tutar üzerinde yapılan düzeltme oran sahasına, oran üzerinde yapılan düzeltme tutar sahasına otomatik olarak hesaplanarak yansır. Genel İskonto-1-2-3, mal fazlası ve satır iskontolarından sonra, brüt tutardan düşülecek fatura altı iskontolarıdır. Genel İskonto-3 ayrıca **Bölge Farkı İskontosu** için de kullanılır. Ekrana Fat.Alt. İsk 1, 2, 3 alanının eklenmesi için, [Satış Parametreleri](<Satış Faturası/index.md>) İskonto sekmesinde yer alan "Genel İskonto 1-2-3" parametrelerinin işaretli olması gerekir. |
| Fat.AltM-1, 2 | Ek Maliyet-1 veya 2 tanımlamaları yapılmış ise fatura altı ilave maliyetleri program tarafından otomatik olarak ekrana gelir. Hesaplatılan bir değer yoksa elle tutar girilebilir. Ekrana Fat.AltM-1, 2 alanının eklenmesi için, [Satış Parametreleri](<Satış Faturası/index.md>) Ek Maliyet sekmesinde yer alan "Ek Maliyet 1-2" parametrelerinin işaretli olması gerekir. |
| Genel İskonto 1,2,3 | Mal fazlası ve satır iskontolarından sonra, brüt tutardan düşülen fatura altı iskonto alanlarıdır. Bu alanların ismi, [satış parametreleri](<Satış Faturası/index.md>) kısmında Genel İskonto veya Fatura Altı İskonto isimlerinden birinin işaretlenmesiyle belirlenen isim ile ekrana gelir. Genel İskonto-1, faturanın kesildiği müşterinin, cari hesap sabit kayıtlarında tanımlanan iskonto oranı üzerinden hesaplanan tutarın görüntülendiği alandır. Hem tutar hem de oran değeri üzerinde istenilen düzenleme yapılabilir. Tutar üzerinde yapacağınız düzeltme oran sahasına, oran üzerinde yapacağınız düzeltme tutar sahasına otomatik hesaplanarak yansır. Bölge farkı iskontosu için Genel İskonto-3 kullanılır. |
| Ek Maliyet 1,2 | İlave maliyetlerin girildiği alandır. Hesaplatılan bir değer yoksa, elle tutar girilebilir. |
| ÖTV | Hesaplanan ÖTV tutarının izlendiği alandır. |
| Yuvarlama | İrsaliye genel toplamının yuvarlanması için kullanılan alandır. |
| Br. 1 Miktar, Br.2 Miktar, Br. 3 Miktar | Kalem Bilgilerinde girilen tüm stokların toplam miktar bilgilerinin, stok kartı kayıtlarında tanımlı birinci, ikinci ve üçüncü ölçü birimi cinsinden izlenen alandır. |
| Hediye Puan | Müşterilere, aldıkları malın üzerinden puan hesaplaması yapılması ve puanlarına istinaden hediye verilmesi işlemlerinin takibinin yapılması amacıyla kullanılan alandır. Bu sistemde, her bir ürün için ayrı ayrı puanlar belirlenerek, hak edilen, kullanılan ve kalan bakiye puanları takip edilebilir. Puan karşılığı verilen hediye ürünlerde, bakiye puan dikkate alınır. |
| Satış İrsaliyesi Ekranı | KDV’ler Toplamı ve Genel Toplam |
| Ara Toplam | Yukarıda anlatılan iskontolar toplamının brüt toplamdan düşülüp, ek maliyet toplamlarının eklenmesiyle oluşan toplamdır. Bu alana elle müdahale edilemez. Bilgilendirmek amacıyla görüntülenen alandır. |
| KDV 1,2,3,4,5 | İrsaliye kaydında girilen stok kalemlerinin, stok sabit kayıtlarında yazılı KDV oranına göre, program tarafından otomatik hesaplanarak ekrana getirildiği alandır. |
| KDV % | KDV hesaplamalarında kullanılan oranların izlendiği alandır. |
| Toplam KDV | Farklı KDV oranları üzerinden hesaplanan tutarların toplamının yazıldığı alandır. Hesaplanan değer üzerinde çok küçük bir farklılık olması halinde düzenleme yapılmasını, aksi halde bu değerin değiştirilmemesi tavsiye edilir. Burada yapılacak düzeltme, yukarıda anlatıldığı şekilde hesaplanan KDV tutarları dağılımına yansımaz. Yapılan değişiklik, sadece aşağıdaki genel toplam alanına yansır. Fatura/ Kayıt/[Satış Fatura Parametreleri](<Satış Faturası/index.md>) Bölümü’nde “KDV Maliyete Eklensin” parametresi işaretlenmiş ise, bu alanda oluşan tutar muhasebeye entegre olmaz. Stok fiyatlarına KDV tutarları eklenerek stok hareket kayıtlarına aktarılır. |
| Genel Toplam | Yukarıda anlatılan işlemler sonucu oluşan son toplamın gösterildiği alandır. Bu tutar üzerinde değişiklik yapmak yerine Karşı Toplam alanı kullanılır. |
| Karşı Toplam | Satış İrsaliyesi genel toplam alanında değişiklik yapılması istendiğinde kullanılan alandır. Yardımcı Programlar/Özel Parametre Kayıtları Bölümü’nde, Grup Kodu sahası “FATURA”, Anahtar sahası “SATFATKARSITOPLAM” ve Değer sahası ‘0’ olarak tanımlama yapılması halinde bilgi girişi yapılır. Bu alana girilecek tutar "Genel Toplam" alanına aktarılır. "Genel Toplam" ile "Karşı Toplam" arasındaki fark, yuvarlama alanından takip edilir. |
| Resim Alanı | Faturaya resim yada doküman dosyası eklemek için kullanılan alandır. |
| Satış İrsaliyesi Ekranı | Kayıt Sorgulamaları |
| Kasa Kodu | "Fatura Üst Bilgiler" sayfasında bulunan fatura tipleri arasından, kapalı ve muhtelif fatura tipleri seçildiğinde aktif olan alandır. Bu iki tip fatura, peşin fatura olarak kabul edilir ve kasa modülünde kayıt oluşur. Bu alanda çoklu kasa kullanılıyor ise, fatura toplamının hangi kasaya aktarılacağı sorgulanır. Tek kasa kullanımında ‘00’ kasa kodu, otomatik olarak ekrana gelir. Kasa kodu seçmek için, sahanın sağ tarafında bulunan aşağı ok işaretine, sağ klik tuşuyla basılması yeterlidir. |
| Kasa Adı | Kasa kodu seçilmesi halinde, ilgili kasaya ait ismin, program tarafından ekrana getirildiği alandır. |
| Toplam Mal Ağırlığı | İrsaliyede girilen stok kalemleri için, “Stok Kartı Kayıtlarında” birim ağırlık tanımlaması ile aktif olan alandır. Program bu ağırlıkları, irsaliyedeki miktarlarla çarparak toplam mal ağırlığını hesaplar ve otomatik olarak ekrana getirir. |
| Vade Gün/Vade Tarihi | İrsaliye kaydı oluştururken, cari hareket ve stok hareket kayıtlarına işlenecek vade gün/tarihinin belirlendiği alandır. Stok hareketlerine işlenen vade tarihi, stok hareket girişleri ekranından görüntülenmez fakat raporlardan izlenebilir. Ekrana Vade Gün/Vade Tarihi alanının eklenmesi için, [Satış Parametreleri](<Satış Faturası/index.md>)Genel 4 sekmesinde yer alan "Kayıtlarda Her Satırda Vade Tarihi ve Vade Günü Sorulsun" parametrelerinin işaretli olması gerekir. |
| Basım | Girilen irsaliyenin basımı yapılacak ise işaretlenen alandır. Bu alan işaretlendikten sonra “Tamam” butonuna basıldığında, “Dizayn Sorgulama” ekranından dizayn tipi ve yazıcı seçilerek basım yapılır. |
| Sıralama Seçeneği | Basımı yapılacak olan irsaliye kalemlerini, bu alanda bulunan seçeneklere göre sıralatmak amacıyla kullanılan alandır. Ekrana Sıralama Seçeneği alanın eklenmesi için, [Satış Parametreleri](<Satış Faturası/index.md>) Genel 1 sekmesinde yer alan "Sıralama Seçeneği Faturada Sorulsun" parametresinin işaretli olması gerekir. |
| Vadelere Bölme | Satış irsaliyesi tutarının cari hareket kayıtlarına işlenirken, vadelere bölünerek kaydedilmesi için kullanılan alandır. "Üst Bilgiler" veya "Koşul Bilgileri" ekranında ödeme kodu girilmişse, vadelere bölünen tutarlar program tarafından otomatik olarak bu alana gelir. Ekrana Vadelere Bölme alanının eklenmesi için, [Satış Parametreleri](<Satış Faturası/index.md>) Genel 4 sekmesinde yer alan "C/H Vadelere Bölünerek Geçsin" parametresinin işaretli olması gerekir. |
| Tamam | Bilgileri girilen irsaliyenin kaydı için kullanılan butondur. Tamam ![](../../../../_assets/23043a6798351fd813b5.png)butonuna basıldığında, irsaliyeye ilişkin kayıtlar ilgili entegre bölümlere aktarılır. İrsaliyenin daha önce kaydedilmiş olması ve düzenlenip tekrar kaydedilmesi durumunda, entegre bölümlerden stok ve cari bölümlere işlenen hareketler program tarafından düzenlenir. Bu kayıtlar, Entegrasyon/Entegrasyon Kayıtlarında “ 2 no.lu " (Düzeltilmiş Kayıt) ya da “4 no.lu " (Düzeltilmiş Bulunamadı) tipte izlenir. |

Mal Fazlası İskontosu, Satır İskontosu, Genel İskonto, Ek Maliyet 1-2, Sıralama Seçeneği, Vadelere Bölme alanları [Satış Parametreleri](<Satış Faturası/index.md>) sayesinde, isteğe bağlı olarak ekranda yer alabilir/almayabilir.

Satış İrsaliyesi Kaydı, Değişikliği, İptali için yapılması gerekenler aşağıdaki şekildedir:

- Satış irsaliyesinin kaydı için, irsaliye ekranındaki alanlara bilgi girişi yapıldıktan sonra, "Toplamlar" ekranında "**tamam"** tuşuna basılır. Böylece, Üst Bilgiler ekranında seçilen tipe göre, gerekli bölümlerde entegre kayıtlar oluşur.
- Daha önceden kaydedilmiş bir irsaliye üzerinde değişiklik yapmak için, "Üst Bilgiler" ekranından ilgili irsaliyenin numarası girilerek \<tab\> butonuna basılır. Böylece, kayıtlı irsaliyeye ait daha önceden girilmiş bilgiler ekrana gelir. Mevcut ekranda değiştirilmek istenen alana gelip düzenleme yapılır. Burada dikkat edilmesi gereken nokta, belge üzerinde değişiklik yapıldıktan sonra, irsaliye ile ilgili bağlantılı bölümlerde de gerekli değişikliklerin program tarafından yapılabilmesi için, "**Toplamlar"** ekranından belgenin tekrar kaydedilmesi gerekir.
- Kaydedilmiş bir irsaliye faturasının iptali için, "Üst Bilgiler" ekranında iken araç çubuklarında bulunan ![](../../../../_assets/2df4b343310bcd16b01e.jpg) (Kayıt Sil) butonuna ya da klavyedeki F7 butonuna basılır. Bu aşamada program, “Bu ekrana ait tüm bilgileriniz silinecektir. Emin misiniz?” şeklinde bir uyarı ekrana getirir. “Evet” butonuna basılması halinde, ilgili irsaliyeye ait bilgiler, bağlı olduğu tüm bölümler dahil olmak üzere sistemden silinir.

"Satış İrsaliyesinde Kullanılan Özel Tuşlar" için bkz. [Satış Faturasında Kullanılan Özel Tuşlar](<Satış Faturası/Satış Faturasında Kullanılan Özel Tuşlar.md>)
