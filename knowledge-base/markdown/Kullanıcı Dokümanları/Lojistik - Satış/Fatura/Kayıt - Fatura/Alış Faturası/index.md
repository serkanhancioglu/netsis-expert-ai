---
title: "Alış Faturası"
page_id: "22804223"
product: "netsis-3-enterprise"
depth: 5
is_section: true
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Fatura"
  - "Kayıt / Fatura"
  - "Alış Faturası"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Fatura / Kayıt / Fatura / Alış Faturası"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWY1YTg1Nzc3LTU0ZTQtNGI5NS1hYThhLTBjMzljNmFjY2NhOCZsaW5rPTAzNWM4MjRlLTcxMzctNDViMS05N2RkLWY4MGFmMDk4MjU5MiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=f5a85777-54e4-4b95-aa8a-0c39c6accca8&link=035c824e-7137-45b1-97dd-f80af0982592&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "alis-faturasi_22804731_22804223.html"
source_version: "2022-10-24T10:39:28.630+03:00"
source_bytes: 952423
fetched_at: "2026-09-13T04:01:40+00:00"
generator: "netsis-scraper 1.0.0"
---
# Alış Faturası

Alış Faturası Bölümü'nde aşağıdaki işlemler kaydedilir, düzenlenir ve izlenir:

- Satıcılardan gelen alış faturalarının ve satıştan iade faturalarının işlemleri.
- Sipariş/irsaliye bağlantılı fatura işlemleri.

Alış faturası, Lojistik-Satış Bölümü’nde, fatura kayıt menüsünün altında yer alır. Sipariş Bilgileri, Üst Bilgiler, Koşul Bilgileri, Kalem Bilgileri, Toplamlar, Vadelere Bölme bilgilerinin girilmesi ile alış faturası kaydı oluşturulur.

Bu bölümlerden bazıları, belirli parametrelerin işaretlenmesi sonucu ekranda görülür.

**Sipariş Bilgileri**

Sipariş Bilgileri, sipariş takibi yapan firmalarda, sipariş bağlantılı fatura oluşturulması için ya da alış irsaliyelerinin faturalandırılması için kullanılan bölümdür.

Sipariş Bilgileri sekmesi, siparişe ait fatura oluşturmak için tüm bilgilerin en baştan tekrar girilmesi yerine, daha önceden girilen müşteri siparişlerinden fatura oluşturulmasını sağlar.

Alış Faturası modülüne girildiğinde, Sipariş Bilgileri sekmesinin ekrana gelmesi için mutlaka, "[Alış Parametrelerinde](index.md)" bulunan “Sipariş Takibi Yapılsın” parametresinin işaretlenmiş olması gerekir.

Alış Faturası ekranı Sipariş Bilgileri sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Alış Faturası Ekranı |  |
| --- | --- |
| Belge Tipi | Sipariş ve İrsaliye seçeneklerinden oluşur. Alış faturası sipariş bağlantılı ise sipariş, irsaliye bağlantılı ise irsaliye seçeneği seçilir. Bu alan irsaliye bağlantılı fatura oluşturulmadığında pasif olur ve sipariş seçeneği program tarafından seçilir. |
| Belge Numarası | Faturalandırılması istenen sipariş veya irsaliyenin belge numarasının, rehber ![](../../../../../_assets/088477bb321d1b20c939.jpg) tuşu ile seçim yapılarak girildiği alandır. Siparişlerin teslim edilen/kalan bazında takibinin sağlıklı olarak yapılabilmesi için faturanın bağlantılı olduğu sipariş numarasının doğru olarak girilmesi gerekir. |
| Teslim Cari Kodu | Sipariş veya irsaliyenin teslim edildiği yerin, rehber ![](../../../../../_assets/088477bb321d1b20c939.jpg) tuşu ile seçim yapılarak girildiği cari kod alanıdır. Faturanın kesildiği cari hesap/adres ile, stokların teslim edileceği cari hesap/adresin farklı olması halinde kullanılır. |
| Fatura Oluştur | “Belge Numarası” alanı ve/veya “Detaylı Sipariş/İrsaliye Rehberi” alanı seçilerek fatura oluşturmayı sağlar. Butona tıklandığında, oluşturulacak faturaya ilişkin numara ve tarih bilgilerinin yer aldığı **“Sipariş Teslimatınız Yapılsın Mı?”** başlıklı ekran gelir. Burada **“Tamam”** butonuna basıldığında, seçilen siparişte bulunan bilgiler faturaya aktarılır ve istenirse aktarılan bilgiler üzerinde değişiklik yapılabilir. |
| Detaylı Sipariş/İrsaliye Rehberi Cari Kodu | Faturalandırılacak sipariş veya irsaliye belgelerine kısıt vermek için kullanılan alandır. Faturanın oluşturulması aşamasında, sipariş bilgilerinin detaylandırılarak girildiği müşterinin kodudur. Rehber tuşu ile cari kod seçimi yapılır. |
| Detaylı Sipariş / İrsaliye Rehberi Belge Numarası | Faturanın oluşturulacağı sipariş numarasının girildiği alandır. Tek bir siparişe ait faturalandırma işlemi yapılacaksa bu bölüm kullanılabilir. Cari kodun girilip bu alanın boş geçilmesi halinde, ilgili cariye ait tüm siparişler listelenir. |
| Mal Detaylı Mı? | “Mal detaylı mı?” sorusu işaretlendiğinde, müşterinin kalan siparişleri mal bazında detaylı listelenir. İşaretlenmediğinde, belirlenen cari koda ait, teslimi yapılmamış (kalan) sipariş numaralarının yer aldığı liste üzerinden, istenilen siparişler farenin sol tuşu çift tıklanarak işaretlenebilir. Böylece faturalama işlemlerinde siparişler birleştirilerek faturalandırılabilir fakat mal detayları izlenemez. |
| Stok Kısıdı Verilebilsin | Ekranın altında listelenecek sipariş kalemleri için kısıt verilmesi amacıyla kullanılan seçenektir. Bu seçeneğin aktif olması için “Mal Detaylı Mı?” sorusunun işaretlenmesi gerekir. “Stok Kısıdı Verilebilsin” seçeneği işaretlendikten sonra “Belgeleri Getir” butonuna basıldığında, listelenecek sipariş kalemlerinin belirlenmesi için “Stok Kısıt Ekranı” gelecektir. Bu ekranda bulunan **Saha** **Adı** sütunundaki hücreye tıklandığında, stok ilişkili alanlar listelenir. Bu listede, kısıt verilecek alan seçildikten sonra, “Operatör” ve “Değer” alanları kullanılarak istenen kısıt verilir. |
| Sıralama | Belge no, teslim tarihi, koşul kodu, belge tarihi, stok kodu, stok adı seçeneklerini içerir. Listelenecek sipariş/irsaliye belgelerinin seçilecek alanlara göre sıralanmasını sağlar. |
| Belgeleri Getir | Cari kod ve mal detayı bilgileri baz alınarak, sipariş belgelerinin listelenmesini sağlayan butondur. |

**İrsaliye Bağlantılı Fatura İşlemleri**

Alış Faturası modülünden irsaliye bağlantılı fatura oluştururken, aynı cariye ait birden fazla irsaliye birleştirilerek tek bir fatura halinde kaydedilebilir. Bunun için, “Sipariş/İrsaliye Bilgileri” ekranında faturalandırılması istenen irsaliye yada irsaliye kalemleri seçilir. İrsaliyelerin parçalı olarak faturalandırılması için, “Kalem Bilgileri” ekranından irsaliye seçimi yapılır (Bu durumda her stok için satır bazında irsaliye numarası sorulacaktır.)

İrsaliye rehberinde, ilgili faturadaki cariye ait faturalanmamış irsaliyelerin listesi yer alır. Rehber ![](../../../../../_assets/088477bb321d1b20c939.jpg) tuşu ile ilgili faturaya ait faturalanması istenen irsaliye seçilir. Seçilen irsaliyede, bir stokun birden fazla tekrar edildiği satırlarda, hangi satırdaki kaydın seçileceğini, irsaliye kontrol alanı belirler. Satır bazında irsaliye numarası seçilerek yapılan faturalandırma işlemlerinde, irsaliyelerin miktarlarında değişiklik yapılması isteniyorsa, irsaliyenin tamamı faturalandırılmadan önce, irsaliye miktarından faturalanan miktar düşülerek, faturalanmayan satırlar üzerinde değişiklik yapılabilir. Bu şekilde, tamamı faturalandırılmamış irsaliyelerde, bakiye ve miktar kısmı daha sonra faturalandırılır. İrsaliyenin tamamı faturalandırıldığı zaman, satış/alış irsaliyeleri bölümünden irsaliye kaydı çağrıldığında “faturalanmış irsaliye” uyarısı gelir ve bir daha faturalandırılmasına izin verilmez. İrsaliye numarasının olmadığı ya da yanlış girildiği durumlarda, program “Bu müşteriye ait irsaliye bulunamadı” şeklinde bir uyarı verir. Fatura, irsaliye bağlantılı değilse, irsaliye numarası alanı boş bırakılarak, \<tab\> butonu ile devam edilir.

İrsaliyelerin saklanması ve parçalı faturalandırma için [Alış Parametrelerinde](index.md) bulunan “**Faturalandırılan İrsaliyeler Saklansın**” ve “**İrsaliye Bilgilerinin Parçalı Faturalandırılması**” parametrelerinin işaretlenmesi gerekir. Uygulamaya dönem ortasında geçmek isteyen firmaların, bu sisteme geçmeden önce tüm irsaliyelerini faturalandırmaları gerekir.

**Üst Bilgiler**

Alış Faturası Üst Bilgiler sekmesi, alış faturasına ait sabit ve cari bilgi alanlarının yer aldığı ekrandır.

Alış Faturası ekranı Üst Bilgiler sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Alış Faturası Ekranı |  |
| --- | --- |
| Numara | Faturanın programdaki takip numarasıdır. |
| Cari Kodu | Faturanın ait olduğu cari hesabın kodudur. |
| Tarih | Faturanın üzerinde yazan tarihin girileceği alandır. |
| Entegre Tarih | Faturanın muhasebeye işlenme tarihidir. |
| Fiili Tarih | Faturanın gerçekleştiği tarihin girileceği alandır. |
| Döviz Bazında Tarih | Faturalarda geçerli olacak kur bilgisinin, hangi tarihe göre baz alınacağının belirlendiği alandır. Ekrana Döviz Bazında Tarih alanının eklenmesi için, "[Alış Parametreleri](index.md)" Genel 2 ekranında yer alan "Döviz Takibi Yapılsın" parametresi ve Yardımcı Programlar→ Şirket→ Şube→ Parametre kayıtlarında bulunan "Döviz Uygulaması" parametresinin işaretli olması gerekir. |
| Tipi | Faturanın hangi tipte kesileceğinin sorgulandığı bölümdür. Tipi alanı; Kapalı, açık, muhtelif, iade, zayi iade, ithalat/ihracat seçeneklerini içerir. **Kapalı Fatura:** Peşin faturalar için kullanılan fatura tipidir. Kapalı kesilen fatura ile stoklara giriş hareketi, kasa kayıtlarına da çıkış (ödeme) hareketi işlenir. Fatura ile ilgili kayıtlar muhasebe ile entegre çalışılması halinde, Entegrasyon Kayıtları/Kasa Tediye bölümüne işlenir. Kapalı fatura tipi seçildiğinde, cari hareket kayıtlarında kayıt oluşmaz. **Açık Fatura:** Vadeli faturalar için kullanılan fatura tipidir. Açık kesilen fatura ile stoklara giriş hareketi, cari hesap kayıtlarına da fatura toplamı kadar alacak hareketi işlenir. Fatura ile ilgili kayıtlar muhasebe ile entegre çalışılması halinde, Entegrasyon Kayıtları/Satıcı Alacak bölümüne işlenir. **Muhtelif Fatura:** Müşteri kodu sahasında herhangi bir kod girilmediğinde, yani muhtelif müşteriye fatura kesilmesi halinde, program bu fatura tipini otomatik olarak ekrana getirir (Herhangi bir cari kod belirlenmiş ise bu fatura tipi seçilemez). Muhtelif fatura, hareketlere işleyiş açısından kapalı fatura gibi işlem görür. **İade Fatura:** Satılan malların iade edileceği durumlarda kesilen fatura tipidir. Satıştan iade işlemi söz konusu ise mutlaka iade fatura tipi seçilmelidir (Birçok satış raporu, bu tiplere bakılarak satışların durumunu yansıtır). İade kesilen fatura ile stoklara giriş hareketi, alıcı cari hesaba da alacak hareketi işlenir. Fatura ile ilgili kayıtlar muhasebe ile entegre çalışılması halinde, Entegrasyon Kayıtları/Müşteri Alacak bölümüne işlenir. **Zayi İade Fatura:** Satılan malların zarar görmesi sebebiyle iade edilmesi halinde kesilen fatura tipidir. İade fatura gibi işlem görür, rapor amaçlıdır. **İthalat/İhracat:** Bu seçenek işaretlenerek kaydedilen bir alış/satış irsaliyesinin **Dekont Modülünden** ithalat/ihracat kapatması yapıldığında, alış/satış faturasının tipi otomatik olarak İthalat/İhracat olur. Kullanıcıların elle kestikleri faturalarda bu seçeneği kullanmamaları gerekir. |
| İhracat/İthalat Tipi | Bu alanda bulunan tipler, sadece ihracat faturaları için geçerlidir. Bir ihracata ait, dekont modülünden yapılan işlemler sonucu oluşan faturada, kesilen irsaliyede belirtilen ihracatın tipi bu alana yansır. Kullanıcıların elle, ithalat/ihracat ve tipi alanlarını kullanarak fatura kesmemeleri gerekir. |
| Export Referans No | Export Referans Numarası, sadece ithalat/ihracat tipli faturalarda dolu olacaktır. Firmaların yaptıkları her ithalata bir numara vermesi gerekmektedir. Programda İthalat faturası oluşturulması için öncelikle, ithalat tipli alış irsaliyesi girilmelidir. Finans Modülü → Dekont → Kayıt → İthalat/İhracat İşlemleri → "İthalat Kapatma" bölümünden girildiğinde, referans no seçilerek ithalat faturası oluşturulur. İthalat işlemleri tamamlandığında program tarafından oluşturulan ithalat faturasına, irsaliyede girilen export referans numarası aktarılacaktır. |
| Hal Fatura Tipi | Hal Faturası Uygulaması parametresinin işaretlenmesi ile aktif hale gelen alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile Hiçbiri, Komisyoncu veya Satış seçenekleri arasından seçim yapılır. **Örneğin;** Kesilecek fatura bir hal faturası ise ve "Komisyoncu" tipine sahipse, "Komisyoncu" tipinin seçilmesi gerekir. |
| Özel Kod-1 | Tanımlanan Özel Kod-1 seçenekleri arasından,![](../../../../../_assets/088477bb321d1b20c939.jpg) tuşu ile seçim yapılarak, faturaların belli kodlar altında gruplanmasını sağlayan alandır. **Örneğin;** Peşin alışlar ayrı, vadeli alışlar ayrı bir alış hesabında gruplanabilir. Ekrana Özel Kod-1 alanının eklenmesi için, "[Alış Parametreleri](index.md)" Özel Kod ve Açıklama sekmesinde yer alan "Özel Kod-1" parametresinin işaretli olması gerekir. |
| Özel Kod-2 | Tanımlanan Özel Kod-2 seçenekleri arasından, Rehber ![](../../../../../_assets/088477bb321d1b20c939.jpg) tuşu ile seçim yapılarak, fatura kayıtlarının rapor bazında gruplama yapılmasını sağlayan alandır. Ekrana Özel Kod-2 alanının eklenmesi için, "[Alış Parametreleri](index.md)" Özel Kod ve Açıklama sekmesinde yer alan "Özel Kod-2" parametresinin işaretli olması gerekir. |
| Açıklama | Alış faturasına ait açıklama bilgisinin girildiği alandır. Ekrana Açıklama alanının eklenmesi için, "[Alış Parametreleri](index.md)" Özel Kod ve Açıklama sekmesinde yer alan "Açıklama" parametresinin işaretli olması gerekir. |
| Proje Kodu | Tanımlanan proje kodları arasından, Rehber ![](../../../../../_assets/088477bb321d1b20c939.jpg) tuşu ile seçim yapılarak, istenildiğinde proje bazında rapor alınabilmesi için girilen koddur. |
| Plasiyer Kodu | Tanımlanan plasiyer kodları arasından, Rehber ![](../../../../../_assets/088477bb321d1b20c939.jpg) tuşu ile seçim yapılarak, ilgili satıcıya ait plasiyer kodunun girildiği alandır. |
| Resmi Fatura No | Resmi elektronik fatura numarasının girildiği alandır. |
| KDV Dahil mi? | KDV'nin nasıl uygulanacağının belirlendiği alandır. KDV dahil kutucuğu işaretlendiği takdirde, stoka ait birim fiyatı, KDV tutarını da içerir. Ekrana KDV Dahil mi? alanının eklenmesi için, "[Alış Parametreleri](index.md)" Fatura KDV sekmesinde yer alan "KDV Dahil/Hariç Sorusu Her Faturada Sorulsun" parametresinin işaretli olması gerekir. |
| Bağlantı No | Girilen belgenin hangi bağlantıya ait olduğunun izlendiği alandır. |
| Toplu Depo | Tanımlanan depo kodları arasından, Rehber ![](../../../../../_assets/088477bb321d1b20c939.jpg) tuşu ile seçim yapılarak, ilgili depo kodunun girildiği alandır. Alış parametreleri kısmında bu parametre işaretlenmediği takdirde, her stok kalemi için ayrı ayrı lokal depo kodu girilmesi gerekir. Ekrana Toplu Depo alanının eklenmesi için, "[Alış Parametreleri](index.md)" Genel 2 sekmesinde yer alan "Fatura/İrsaliyelerde Toplu Depo Kodu Kullanılsın" parametresinin işaretli olması gerekir. |
| Nakliye Katsayısı | Tanımlanan nakliye katsayısı girişinin yapıldığı alandır. Ekrana Nakliye Katsayısı alanının eklenmesi için, "[Alış Parametreleri](index.md)" Genel 3 sekmesinde yer alan "Fatura/İrsaliyelerde Nakliye Katsayısı Girişi Yapılsın" parametresinin işaretli olması gerekir. |
| Değişsin | Dövizli belgelerde bazen (yuvarlama kaynaklı) döviz fiyatının, kurun ya da TL fiyatının değişmesi gerekebilmektedir. Bu gibi durumlarda hangi sahadaki bilginin değişeceğinin belirlendiği alandır. |
| Farklı Teslimat | Faturanın kesildiği cari hesap/adres ile, stokların teslim edileceği cari hesap/adresin farklı olması halinde kullanılan bölümdür. Ekrana Farklı Teslimat alanın eklenmesi için, "[Alış Parametreleri](index.md)" Genel 3 sekmesinde yer alan "Sipariş/İrsaliye/Faturada Farklı Teslim Yeri Kullanılsın" parametresinin işaretli olması gerekir. |
| Kod | Basıma yönelik adres bilgisi değişikliği için girilen alandır. Buradaki cari Kod, faturanın kesildiği kodun aynısı olmalıdır. |
| İsim | Kod alanına girilen cari kodun isim bilgisinin, program tarafından ekrana getirildiği alandır. |
| Adres | Teslimat yapılacak adres bilgisinin, cari hesabın koduna göre program tarafından ekrana getirildiği, kullanıcı tarafından da değişikliğinin yapılabileceği alandır. |
| İlçe | Teslimat yapılacak ilçe bilgisinin, cari hesabın koduna göre program tarafından ekrana getirildiği, kullanıcı tarafından da değişikliğinin yapılabileceği alandır. |
| İl | Teslimat yapılacak il bilgisinin, cari hesabın koduna göre program tarafından ekrana getirildiği, kullanıcı tarafından da değişikliğinin yapılabileceği alandır. |
| Cari Bilgiler/İsim Açıklama-1 Açıklama-2 Açıklama-3 | Kesilen faturanın satıcıya ait kod bilgisi girildiğinde, cari hesap kayıtlarında bulunan isim ve açıklama bilgilerinin program tarafından ekrana getirildiği alanlardır. Fatura kaydı sırasında bu alanlara müdahale edilemez, sadece bilgi amaçlı görüntülenir. |
| Ek Sahalar | Açıklama girişi için kullanılan alanlardır. Ekrana Ek Sahalar alanının eklenmesi için, "[Alış Parametreleri](index.md)" Genel 4 sekmesinde yer alan "Sipariş/İrsaliye/Faturada Ek Sahalar Kullanılsın " parametresinin işaretli olması gerekir. |

Özel Kod-1, Özel Kod-2, Açıklama, Plasiyer Kodu, Proje Kodu, KDV Dahil, Toplu Depo, Nakliye Katsayısı, Farklı Teslimat (kod, isim, adres, ilçe, il) ve Ek Sahalardan oluşan alanlar, "[Alış Parametreleri](index.md)" sayesinde isteğe bağlı olarak ekranda yer alabilir veya almayabilir.

**Koşul Bilgileri**

Alış Faturası Koşul Bilgileri sekmesi, alış faturasına ait geçerli koşul bilgileri alanlarının yer aldığı ekrandır.

Alış Faturası ekranı Koşul Bilgileri sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Alış Faturası Ekranı |  |
| --- | --- |
| Koşul Kodu | Tanımlaması yapılan koşulun, Rehber ![](../../../../../_assets/088477bb321d1b20c939.jpg) tuşu ile seçim yapılarak ekrana getirildiği koddur. |
| Vade Günü | Bir borcun ödenmesi için tanınan süredir. Bu alana vade günü girildiğinde, tanımlanan vade için belirlenen liste fiyatı, kalem bilgileri ekranındaki fiyat sahasına otomatik olarak yansır. |
| Koşul Tarihi | Alış koşul tarihinin girildiği alandır. Bu alanda tarih, otomatik olarak ekrana gelecektir. Eğer koşul tarihi değiştirilirse, alışın girildiği tarihte geçerli olan fiyata göre vade ve iskonto uygulaması yapılır. |
| Fiyat Tarihi | Alış fiyat listesi tarihinin girildiği alandır. |
| Ödeme Kodu | Fatura kaydı sırasında, koşula bağlı ödeme planının kodu girilmişse, ilgili ödeme kodunun Rehber ![](../../../../../_assets/088477bb321d1b20c939.jpg) tuşu ile seçim yapılarak ekrana getirildiği alandır. Cari/Koşul Kayıtları/ Genel Koşul Kayıtları/ Koşul Genel-2 sayfasında bulunan ödeme kodu alanına, o koşula bağlanacak ödeme planının kodu girilmiş ise, ilgili ödeme kodu bu alana program tarafından otomatik getirilir. Fatura belgelerinde koşul uygulamasının olduğu, ancak koşula bağlı ödeme planının olmadığı durumlarda ödeme kodu alanı boş olur ve istenen ödeme planına ait kod girilebilir. Fatura belgelerinde, cari ödeme planlarının koşul bağlantılı uygulanabilmesi için, **Koşul Sabit Kayıtları**nda bulunan “Cari Hesap Vadelere Bölünerek Atılsın” seçeneğinin işaretlenmesi gerekmektedir. Koşul uygulamasının kullanılmadığı durumlarda bu alan, "Koşul Bilgileri" ekranı yerine "Üst Bilgiler " ekranında yer alır. |

Koşul bilgilerindeki tüm alanların ekranda yer alabilmesi için**, "[Alış Parametreleri](index.md)" Koşul ekranında yer alan "Sipariş**/İrsaliye/Faturada Koşul Uygulaması Kullanılsın" parametresinin işaretli olması gerekir.

**Kalem Bilgileri**

Kalem Girişi sekmesi, Açıklama ve Kalem Listesi alanlarının yer aldığı ekrandır.

Alış Faturası ekranı Kalem Bilgileri sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Alış Faturası Ekranı |  |
| --- | --- |
| Kod | Tanımlaması yapılan stok kaleminin, Rehber ![](../../../../../_assets/088477bb321d1b20c939.jpg) tuşu ile seçim yapılarak ekrana getirildiği koddur. |
| İsim | Stok sabit kayıtlarında kaydettiğiniz stok isminin, program tarafından ekrana getirildiği alandır. |
| Sipariş No | Her malın ayrı ayrı sipariş numarasının girilmesini sağlamak için kullanılan alandır. Rehber ![](../../../../../_assets/088477bb321d1b20c939.jpg) tuşu ile stoklar için girilmiş tüm siparişlere ulaşılarak seçim yapılır. Fatura, sipariş bağlantılı kesilmeyecek ise, bu alan boş bırakılarak \<tab\> tuşu ile ilerlenir. Sipariş numarası olmadığı ya da yanlış girildiği durumlarda, program “**Sipariş Bulunamadı**” şeklinde bir uyarı verir. Sipariş bulunduğu zaman, o siparişle ilgili teslimi bekleyen mallar, kalan miktarları ve sipariş tutarlarıyla birlikte otomatik olarak fatura ekranına gelir. Ekrana Sipariş No alanının eklenmesi için, "[Alış Parametreleri](index.md)" Fatura Sipariş sekmesinde yer alan "İrsaliye/Faturada Sipariş No. Mal Bazında Sorulsun" parametresinin işaretli olması gerekir. |
| D.Kd (Depo Kodu) | Tanımlaması yapılan depo kodunun, Rehber ![](../../../../../_assets/088477bb321d1b20c939.jpg) tuşu ile depo seçimi yapılarak, her malın ayrı ayrı depolarda takip ve raporlanmasını sağlamak amacıyla kullanılan alandır. |
| Yapılandırma Kodu | Esnek yapılandırma uygulamasının kullanıldığı durumlarda, stoka ait yapılandırma kodunun girildiği alandır. |
| Yapılandırma Kodu Açıklaması | Yapılandırma kodu alanına girilen değere ait açıklama bilgisinin, program tarafından getirildiği alandır. |
| Yapılandırma Kod Sihirbazı | Belirli bir özellik kombinasyonu içeren yapılandırma kodunun, sistemde tanımlı yapılandırma kodları arasında olup olmadığını saptamak ve tanımlı değilse de hızlı tanımlama yapmak amacıyla kullanılan alandır. |
| Yapılandırılabilir Ürün Girişi | Birden fazla yapılandırma koduna ait çıkış miktarlarının, tek seferde kaydedilmesi için kullanıldığı alandır. |
| Tes.Cari Kod (Teslim Cari Kodu) | Faturanın kesildiği cari hesap/adres ile, stokların teslim edileceği cari hesap/adresin farklı olması halinde, teslimatın yapılacağı cari hesap/adresin girileceği alandır. Ekrana Tes.Cari Kod alanının eklenmesi için, "[Alış Parametreleri](index.md)" Genel 3 sekmesinde yer alan "Satır Bazında Teslim Cari Kodu Sorulsun" parametresinin işaretli olması gerekir. |
| Satır Açıklama | Her kalem için, 10 ayrı ek açıklama girişinin yapılabileceği alandır. Ekrana Satır Açıklama alanının eklenmesi için, "[Alış Parametreleri](index.md)" Genel 6 sekmesinde yer alan "Satır Bazında Ek Açıklama Sorulsun" parametresinin işaretli olması gerekir. |
| Ç.Değ (Çevrim Değeri) | Stok kodu alanına girilen stoka ait, birden fazla ölçü birimi tanımlanmışsa, hangi ölçü birimi üzerinden miktar girileceğinin belirlendiği alandır. Alanın sağ tarafında bulunan aşağı ok tuşuna basılarak, o stok için tanımlanmış olan ölçü birimi seçilir. Girilen miktar otomatik olarak ölçü birimi değerine çevrilir ve sistem tarafından ekrana getirilir. Alanın sağ tarafında bulunan rehber, stokun bir ölçü birimine ait birden fazla çevrim değeri olması halinde çevrimin hangi değere göre yapılacağını seçmek amacıyla kullanılır. Ekrana Ç.Değ alanının eklenmesi için, "[Alış Parametreleri](index.md)" Genel 1 sekmesinde yer alan "Farklı Birimlerden Mal Girişi Yapılsın" parametresinin işaretli olması gerekir. |
| Seri Takibi | Alışların, seri numaralarına göre takibinin yapılması amacıyla kullanılan alandır. |
| Miktar 2 | Stok bazında takibin yapıldığı miktar alanıdır. Karma koli uygulamasının kullanıldığı durumlarda, koli stokuna ait miktar girişi için de kullanılır. Ekrana Miktar 2 alanın eklenmesi için, "[Alış Parametreleri](index.md)" Genel 2 sekmesinde yer alan "İkinci Miktar Sorulsun" parametresinin işaretli olması gerekir. |
| Fiyat Birim | Faturadaki stok kalemlerinin kaydı sırasında, fiyat girmeden önce, eğer ilgili mal için stoklarda birden fazla ölçü birimi tanımlanmışsa (adet, kg, koli v.s), gireceğiniz fiyatın hangi ölçü birimine ait olduğunun seçildiği alandır. Ekrana Fiyat Birim alanının eklenmesi için, "[Alış Parametreleri](index.md)" Genel 1 sekmesinde yer alan "Fiyat Birimi Sorulsun" parametresinin işaretli olması gerekir. |
| Muhasebe Kodu | Hizmet faturası kesen firmaların, bu faturaları satır bazında ayrı hesaplarda muhasebeleştirebilmeleri için kullanılan alandır. Bu alan için tanımlanan muhasebe kodunun seçilmesi ile, ilgili alış faturasındaki hizmet kalemi için borç hareketi oluşur. Hizmet faturası uygulaması, stok kartı kayıtlarında kodu "HIZ" ile başlayan stoklar için uygulanır. Dolayısıyla, hizmet uygulaması ile bu faturalardaki kalemleri ayrı hesaplarda muhasebeleştirmek isteyen firmaların, hizmet stoklarının kodunun ilk üç hanesini HIZ olarak açmaları gerekir.Ekrana Muhasebe Kodu alanının eklenmesi için, "[Alış Parametreleri](index.md)" Genel 1 sekmesinde yer alan "Hizmet Uygulaması" parametresinin işaretli olması gerekir. |
| Hesap İsmi | Muhasebe kodu alanına girilen hesap koduna ait isim bilgisinin program tarafından ekrana getirildiği alandır. |
| Vade Tarihi | Vade günü baz alınarak hesaplanan tarihin, program tarafından ekrana getirildiği alandır. Ekrana Vade Tarihi alanının eklenmesi için, "[Alış Parametreleri](index.md)" Genel 3 sekmesinde yer alan "Kayıtlarda Her Satırda Vade Tarihi Sorulsun" parametresinin işaretli olması gerekir. |
| Ek Alan-1 | Fatura basımına yönelik, anlık açıklamaların girildiği alandır. Ekrana Ek Alan-1 alanının eklenmesi için, "[Alış Parametreleri](index.md)" Genel 1 sekmesinde yer alan "Ek Alan Kullanılsın" parametresinin işaretli olması gerekir. |
| Ek Alan-2 | Alış Faturaları girilirken stok kalemleri bazında ikinci bir açıklamanın gerekliliği halinde kullanılan alandır. Her bir kalem için 14 karakter uzunluğunda açıklama girilir. Ekrana Ek Alan-2 alanının eklenmesi için, "[Alış Parametreleri](index.md)" Genel 2 sekmesinde yer alan "Ek Alan 2 Kullanılsın" parametresinin işaretli olması gerekir. |
| Miktar | İlgili stok kaleminin fatura üzerindeki miktarının yazıldığı alandır. |
| M. Faz ( Mal fazlası) | Alınan malın yanında gelen hediye malların, faturada gösterilmesi için kullanıldığı alandır. Burada hediye gelen miktar girilmelidir. Eğer alınan malın yanında hediye gelen mal farklı ise, miktar hanesine gerekli değer yazılır, mal fazlası hanesi boş bırakılır. Bir sonraki satıra hediye olarak gelen malın kodu yazılır ve bu mal için de miktar hanesi boş bırakılarak, mal fazlası hanesine hediye miktarı girilmesi ile kayıt oluşturulur. Ekrana M. Faz alanının eklenmesi için, "[Alış Parametreleri](index.md)" İskonto ekranında yer alan "Mal Fazlası İskontosu Uygulansın" parametresinin işaretli olması gerekir. |
| Fiyat Tipi | "Stok Sabit Kayıtlarında girilmiş" olan altı fiyattan birinin, fiyat hanesine aktarılması için kullanılan alandır.Alanın sağ tarafında bulunan aşağı ok işaretine basılarak hangi alana girilen fiyatın kullanılacağı belirlenir Ekrana Fiyat Tipi alanın eklenmesi için, "[Alış Parametreleri](index.md)" Genel 3 sekmesinde yer alan "Sipariş/İrsaliye/Faturada Satır Bazında Fiyat Sorulsun" parametresinin işaretli olması gerekir. |
| Dv. Tip (Döviz Tip) | Döviz takibinin yapıldığı alandır. Girilen stok kodu için, tanımlaması yapılan döviz alış tipi değeri, program tarafından ekrana getirilir. Bu alana getirilen değer, isteğe bağlı olarak farklı bir döviz tipi ile de değiştirilebilir. Döviz tipi olarak “0“ dan farklı bir değer seçilirse, ilgili kalemin dövizli olarak alındığı, “0“ değeri seçilirse de TL olarak alındığı anlaşılır. Ekrana Dv. Tip alanının eklenmesi için, "[Alış Parametreleri](index.md)" Genel 2 sekmesinde yer alan "Döviz Takibi Yapılsın" parametresinin işaretli olması gerekir. |
| Döviz Fiyat | Girilen stok kodu için, tanımlaması yapılan döviz fiyat değeri, program tarafından ekrana getirilir. İsteğe bağlı olarak, bu alana getirilen fiyat değiştirilebilir. Ekrana Döviz Fiyat alanının eklenmesi için, "[Alış Parametreleri](index.md)" Genel 2 sekmesinde yer alan "Döviz Takibi Yapılsın" parametresinin işaretli olması gerekir. |
| Döv.Kur | Üst bilgiler ekranında girmiş olduğunuz **Döviz Baz Tarihi** ile, **Döviz Takibi/Günlük Kur Girişi Bölümü’nden** girmiş olduğunuz kur tutarı, **Döviz Kur** alanına yansır. İsteğe göre değişiklik yapılabilir. Kur tutarı ile döviz fiyatı alanındaki değerlerin çarpımı sonucu çıkan rakam, fiyat alanına yansır. |
| Fiyat | İlgili malın, fatura üzerindeki birim fiyatıdır. |
| İsk.1-6 | İsteğe bağlı olarak 1’den 6’ya kadar kademeli şekilde ekranda yer alabilen, iskonto bilgisinin girildiği alandır. Sadece 1. İskonto için tutarsal iskonto girilebilir. Diğer kademeli iskontolarda, oran (%) bazında kayıt girilir. Hesaplamada malın brüt tutarından 1. iskonto düşüldükten sonra, kalan tutardan 2. iskonto düşülür. İkiden fazla iskonto kullanılması durumunda da, kalan tutar üzerinden diğer iskontolar düşülür. Ekrana bu alanın eklenmesi için, "[Alış Parametreleri](index.md)" İskonto sekmesinde yer alan "Kademeli Kaç İskonto Sorulsun" parametresinin işaretli olması gerekir. |
| İsk.1-6 Tip | İskontoları tiplerini muhasebe kodlarına bağlamak için kullanılan alandır. Örneğin, iskonto tip 1 için özel müşteriler iskontosu, iskonto tip 2 için mağaza iskontosu gibi kullanım amacına göre tanımlamalar yapıldıktan sonra belirlenen iskonto tipleri ile farklı muhasebe kodları çalıştırılabilir. |
| KDV | Kdv oranının girildiği alandır. Ekrana bu alanın eklenmesi için, "[Alış Parametreleri](index.md)" Fatura KDV sekmesinde yer alan "Her Satırda KDV Sorulsun" parametresinin işaretli olması gerekir. |
| Proje Kodu | Yapılan alışın proje bazında izlenmesini sağlayan alandır. Rehber ![](../../../../../_assets/088477bb321d1b20c939.jpg) tuşu ile, ilgili proje seçimi yapılır. Örneğin, firmaya ait, farklı bir konumda yeni bir bina inşa edilmesi durumu bir projedir. Projeye ait bir kod tanımlar ve ilgili projeye ait alışlarda bu kod seçilerek kayıt yapılırsa, gerektiğinde **söz konusu projeye ait** alışlar bu kod sayesinde raporlanabilir. |
| Fiili Tarih | Üst Bilgiler sayfasında bulunan fiili tarih bilgisinin, kalem bilgilerine yansıtıldığı alandır. İsteğe bağlı değiştirilebilir. |
| Künye No | Hal Faturası Uygulaması kullanıldığında aktif hale gelen alandır. İlgili ürün için 19 haneli "Künye No" bilgisinin girildiği alandır. |
| Mal Sahibi | Hal Faturası Uygulaması kullanıldığında aktif hale gelen alandır. Hal Faturası Tipi alanında Satış tipinin seçilmesi ile görüntülenir. Mal sahibi bilgisinin girilmesi için kullanılır. |
| Mal Sahibi TCKN/VKN | Hal Faturası Uygulaması kullanıldığında aktif hale gelen alandır. Hal Faturası Tipi alanında Satış tipinin seçilmesi ile görüntülenir. Mal sahibine ait kimlik veya vergi kimlik numarasının girilmesi için kullanılır. |
| GEKAP Tutarı | İlgili alış faturası için GEKAP tutarının girildiği alandır. |
| GEKAP Ambalaj Tutarı | İlgili alış faturası için GEKAP ambalaj tutarının girildiği alandır. |
| Tutar | Stok miktarı ile birim fiyatın program tarafından çarpılıp, brüt tutar olarak yazıldığı alandır. Bu alana müdahale edilemez. Sadece birim fiyat ve miktar hanelerinde yapılan değişiklikler tutarın değişmesine sebep olur. Faturada girilen tüm stok tutarlarının toplamı, ekranın sağ alt köşesinde bulunan **Toplam Tutar** alanında görünür. |
| Top. Mik. (Toplam Miktar) | Sipariş/irsaliye bağlantılı fatura oluşturulduğunda, ilgili stok kalemi için seçilen sipariş/irsaliye kalemindeki miktar bilgisinin program tarafından ekrana getirildiği alandır. |
| Sip. Nolar (Sipariş Numaraları) | Sipariş bağlantılı fatura oluşturulduğunda, ilgili sipariş numarasının izlendiği alandır. |
| İrs. Nolar (İrsaliye Numaraları) | İrsaliye bağlantılı fatura oluşturulduğunda, ilgili irsaliye numarasının izlendiği alandır. |
| Bakiye | Faturada girilen her stok kodu için, ilgili malın stok hareket kayıtlarındaki bakiyesinin, bilgilendirme amacıyla program tarafından ekrana getirildiği alandır. |

Yapılandırma Kodu, Yapılandırma Kodu Açıklaması, Yapılandırma Kod Sihirbazı, Yapılandırılabilir Ürün Girişi, Teslim Cari Kodu, Sipariş No, Satır Açıklama, Depo Kodu, Çevrim Değeri, Ek Alan-1 ve 2, Seri Takibi, Miktar 2, Mal Fazlası, Fiyat Birim, Döviz Tip, İsk.1-6, KDV, Muhasebe Kodu, Hesap İsmi, Proje Kodu, Vade Tarihi alanları, "[Alış Parametreleri](index.md)" sayesinde, isteğe bağlı olarak ekranda yer alabilir/almayabilir.

**Kalem Bilgilerinde Değişiklik/İptal**

Yukarıda açıklanan alanlara bilgi girişi yapıldıktan sonra \<tab\> butonu ile ilerleyerek veya F5 butonuna basılarak, kalem bilgisi kaydedilir ve ekranda satır olarak görünür. Fatura kaydedilmemiş olmasına rağmen, satıra aktarılan stok alış bilgileri, stok hareket kayıtlarına da işlenir. Dolayısıyla, bu aşamada iken, faturanın tamamı yerine sadece stok giriş hareketi kaydedilir.

Kaydedilen kalem üzerinde değişiklik yapılması istendiğinde, ilgili stok kalemi satırının üzerine çift tıklayarak seçim yapılması halinde, gerekli alan/alanların üzerinde değişiklik yapılabilir. Kaydedilen kalem aynı şekilde seçildikten sonra araç çubuklarında bulunan Kayıt Silme ![](../../../../../_assets/2df4b343310bcd16b01e.jpg) tuşu ya da klavyedeki F7 tuşu yardımıyla ilgili kalem silinir.

**Toplamlar**

Toplamlar sekmesi; İskonto ve Maliyet Toplamları, KDV'ler Toplamı ve Genel Toplam, Kayıt Sorgulamaları alanlarının yer aldığı ekrandır.

Alış Faturası ekranı Toplamlar sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Alış Faturası Ekranı | İskonto ve Maliyet Toplamları |
| --- | --- |
| Brüt Toplam | Faturada kaydedilen mal tutarlarının, iskonto düşülmeden önceki brüt tutarını gösteren alandır. Kalem bilgileri ekranındaki bilgilere göre oluşturulan bir alan olduğu için, elle değiştirme yapılamaz. Buradaki tutarın yanlış olması durumunda, önceki ekrana (kalem bilgileri) geçilerek gerekli düzeltme işlemleri yapılmalıdır. |
| Mal Fazlası İsk. | Kalem bilgileri ekranında mal fazlası alanı kullanılmışsa, program öncelikle mal fazlası (hediye) tutarını brüt olarak hesaplayacak, daha sonra iskonto şeklinde brüt tutardan düşecek. Bu alanda, fatura kaydında mal fazlası olarak girilmiş bütün malların toplam tutarı ekranda görünür. Brüt tutardan ilk olarak düşecek iskonto, mal fazlası iskontosudur. Kalem bilgileri ekranındaki bilgilere göre oluşturulan bir alan olduğu için, elle değiştirme yapılamaz. Buradaki tutarın yanlış olması durumunda, önceki ekrana (kalem bilgileri) geçilerek gerekli düzeltme işlemleri yapılmalıdır. |
| Satır İskontosu | Fatura kaydı sırasında, satır bazında girilen tüm iskonto oran/ tutar toplamlarının program tarafından hesaplanarak ekrana getirildiği alandır. Brüt tutar ve mal fazlası iskontosundan sonra düşülecek ikinci iskonto, satır iskontosudur. Kalem bilgileri ekranındaki bilgilere göre oluşturulan bir alan olduğu için, elle değiştirme yapılamaz. Buradaki tutarın yanlış olması durumunda, önceki ekrana (kalem bilgileri) geçilerek gerekli düzeltme işlemleri yapılmalıdır. |
| Fat.Alt. İsk 1, 2, 3 | Genel iskonto 1-2-3 tanımlamaları yapılmış ise ekrana gelen alanlardır. Fatura Altı İskonto-1 alanı; cari hesap için girilen iskonto oranı varsa, bu oran üzerinden hesaplanan tutarın program tarafından ekrana getirildiği alandır. Hem tutar hem de oran değeri üzerinde istenen düzenleme yapılabilir. Tutar üzerinde yapılan düzeltme oran sahasına, oran üzerinde yapılan düzeltme tutar sahasına otomatik olarak hesaplanarak yansır. Genel İskonto-1-2-3, mal fazlası ve satır iskontolarından sonra, brüt tutardan düşülecek fatura altı iskontolarıdır. Genel İskonto-3 ayrıca **Bölge Farkı İskontosu** için de kullanılır. Ekrana Fat.Alt. İsk 1, 2, 3 alanının eklenmesi için, "[Alış Parametreleri](index.md)" İskonto sekmesinde yer alan "Genel İskonto 1-2-3" parametrelerinin işaretli olması gerekir. |
| Fat.AltM-1, 2 | Ek Maliyet-1 veya 2 tanımlamaları yapılmış ise fatura altı ilave maliyetleri program tarafından otomatik olarak ekrana gelir. Hesaplatılan bir değer yoksa elle tutar girilebilir. Ekrana Fat.AltM-1, 2 alanının eklenmesi için, "[Alış Parametreleri](index.md)" Ek Maliyet sekmesinde yer alan "Ek Maliyet 1-2" parametrelerinin işaretli olması gerekir. |
| Genel İskonto 1,2,3 | Mal fazlası ve satır iskontolarından sonra, brüt tutardan düşülen fatura altı iskonto alanlarıdır. Bu alanların ismi, alış parametreleri kısmında Genel İskonto veya Fatura Altı İskonto isimlerinden birinin işaretlenmesiyle belirlenen isim ile ekrana gelir. Genel İskonto-1, faturanın kesildiği müşterinin, cari hesap sabit kayıtlarında tanımlanan iskonto oranı üzerinden hesaplanan tutarın görüntülendiği alandır. Hem tutar hem de oran değeri üzerinde istenilen düzenleme yapılabilir. Tutar üzerinde yapacağınız düzeltme oran sahasına, oran üzerinde yapacağınız düzeltme tutar sahasına otomatik hesaplanarak yansır. Bölge farkı iskontosu için Genel İskonto-3 kullanılır. |
| Ek Maliyet 1,2 | İlave maliyetlerin girildiği alandır. Hesaplatılan bir değer yoksa, elle tutar girilebilir. |
| ÖTV | Hesaplanan ÖTV tutarının izlendiği alandır. |
| ÖTV Tevkifatı | Belge için ÖTV tevkifatının hesaplanarak getirildiği alandır. ÖTV tevkifatının hesaplanması veya sıfırlanması için, ekran üzerinde farenin sağ tuşuna tıklandığında görüntülenen seçenekler arasından "ÖTV Tevkifatı Hesapla" veya "ÖTV Tevkifatı Sıfırla" seçeneğine tıklanır. |
| Yuvarlama | Fatura genel toplamının yuvarlanması için kullanılan alandır. |
| Br. 1 Miktar, Br.2 Miktar, Br. 3 Miktar | Kalem Bilgilerinde girilen tüm stokların toplam miktar bilgilerinin, stok kartı kayıtlarında tanımlı birinci, ikinci ve üçüncü ölçü birimi cinsinden izlenen alandır. |
| Hediye Puan | Müşterilere, aldıkları malın üzerinden puan hesaplaması yapılması ve puanlarına istinaden hediye verilmesi işlemlerinin takibinin yapılması amacıyla kullanılan alandır. Bu sistemde, her bir ürün için ayrı ayrı puanlar belirlenerek, hak edilen, kullanılan ve kalan bakiye puanları takip edilebilir. Puan karşılığı verilen hediye ürünlerde, bakiye puan dikkate alınır. |
| Alış Faturası Ekranı | KDV’ler Toplamı ve Genel Toplam |
| Ara Toplam | Yukarıda anlatılan iskontolar toplamının brüt toplamdan düşülüp, ek maliyet toplamlarının eklenmesiyle oluşan toplamdır. Bu alana elle müdahale edilemez. Bilgilendirmek amacıyla görüntülenen alandır. |
| KDV 1,2,3,4,5 | Fatura kaydında girilen stok kalemlerinin, stok sabit kayıtlarında yazılı KDV oranına göre, program tarafından otomatik hesaplanarak ekrana getirildiği alandır. |
| KDV % | KDV hesaplamalarında kullanılan oranların izlendiği alandır. |
| Toplam KDV | Farklı KDV oranları üzerinden hesaplanan tutarların toplamının yazıldığı alandır. Hesaplanan değer üzerinde çok küçük bir farklılık olması halinde düzenleme yapılmasını, aksi halde bu değerin değiştirilmemesi tavsiye edilir. Burada yapılacak düzeltme, yukarıda anlatıldığı şekilde hesaplanan KDV tutarları dağılımına yansımaz. Yapılan değişiklik, sadece aşağıdaki genel toplam alanına yansır. Fatura/ Kayıt/Satış Fatura Parametreleri Bölümü’nde “KDV Maliyete Eklensin” parametresi işaretlenmiş ise, bu alanda oluşan tutar muhasebeye entegre olmaz. Stok fiyatlarına KDV tutarları eklenerek stok hareket kayıtlarına aktarılır. |
| Genel Toplam | Yukarıda anlatılan işlemler sonucu oluşan son toplamın gösterildiği alandır. Bu tutar üzerinde değişiklik yapmak yerine Karşı Toplam alanı kullanılmalıdır. |
| Karşı Toplam | Satış faturası genel toplam alanında değişiklik yapılması istendiğinde kullanılan alandır. Yardımcı Programlar/Özel Parametre Kayıtları Bölümü’nde, Grup Kodu sahası “FATURA”, Anahtar sahası “SATFATKARSITOPLAM” ve Değer sahası ‘0’ olarak tanımlama yapılması halinde bilgi girişi yapılır. Bu alana girilecek tutar "Genel Toplam" alanına aktarılır. "Genel Toplam" ile "Karşı Toplam" arasındaki fark, yuvarlama alanından takip edilir. |
| Resim Alanı | Faturaya resim yada doküman dosyası eklemek için kullanılan alandır. |
| e-Fatura Senaryosu Hal Faturası | Hal Faturası Uygulaması kullanıldığında görüntülenen alandır. Üzerine tıklandığında farenin sağ tuşu ile ekrana gelen "Hal Faturası Masraf Girişi" ekranından ilgili fatura için mevcut olan komisyon/satış oranları ve bu oranlara ait varsa KDV oranları girilir. İlgili masraf oranları girildikten sonra Tamam ![](../../../../../_assets/39d77b8716226638d9ce.jpg) butonuna tıklanarak fatura kaydedilir. |
| Alış Faturası Ekranı | Kayıt Sorgulamaları |
| Kasa Kodu | "Fatura Üst Bilgiler" sayfasında bulunan fatura tipleri arasından, kapalı ve muhtelif fatura tipleri seçildiğinde aktif olan alandır. Bu iki tip fatura, peşin fatura olarak kabul edilir ve kasa modülünde kayıt oluşur. Bu alanda çoklu kasa kullanılıyor ise, fatura toplamının hangi kasaya aktarılacağı sorgulanır. Tek kasa kullanımında ‘00’ kasa kodu, program tarafından ekrana getirilir. Kasa kodu seçmek için, sahanın sağ tarafında bulunan aşağı ok işaretine, sağ klik tuşuyla basılması yeterlidir. |
| Kasa Adı | Kasa kodu seçilmesi halinde, ilgili kasaya ait ismin, program tarafından ekrana getirildiği alandır. |
| Toplam Mal Ağırlığı | Faturada girilen stok kalemleri için, “Stok Kartı Kayıtlarında” birim ağırlık tanımlaması ile aktif olan alandır. Program bu ağırlıkları, faturadaki miktarlarla çarparak toplam mal ağırlığını hesaplar ve otomatik olarak ekrana getirir. |
| Vade Gün/Vade Tarihi | Fatura kaydı oluştururken, cari hareket ve stok hareket kayıtlarına işlenecek vade gün/tarihinin belirlendiği alandır. Stok hareketlerine işlenen vade tarihi, stok hareket girişleri ekranından görüntülenmez fakat raporlardan izlenebilir. Ekrana Vade Gün/Vade Tarihi alanının eklenmesi için, "[Alış Parametreleri](index.md)" Genel 3 sekmesinde yer alan "Kayıtlarda Her Satırda Vade Tarihi ve Vade Günü Sorulsun" parametrelerinin işaretli olması gerekir. |
| Basım | Girilen faturanın basımı yapılacak ise işaretlenen alandır. Bu alan işaretlendikten sonra “Tamam” butonuna basıldığında, “Dizayn Sorgulama” ekranından dizayn tipi ve yazıcı seçilerek basım yapılır. |
| Sıralama Seçeneği | Basımı yapılacak olan fatura kalemlerini, bu alanda bulunan seçeneklere göre sıralatmak amacıyla kullanılan alandır Ekrana Sıralama Seçeneği alanının eklenmesi için, "[Alış Parametreleri](index.md)" Genel 5 sekmesinde yer alan "Sıralama Seçeneği Faturada Sorulsun" parametresinin işaretli olması gerekir. |
| Vadelere Bölme | Alış Faturası tutarının cari hareket kayıtlarına işlenirken, vadelere bölünerek kaydedilmesi için kullanılan alandır. "Üst Bilgiler" veya "Koşul Bilgileri" ekranında ödeme kodu girilmişse, vadelere bölünen tutarlar program tarafından otomatik olarak bu alana gelir. Ekrana Vadelere Bölme alanının eklenmesi için, "[Alış Parametreleri](index.md)" Genel 2 sekmesinde yer alan "C/H Vadelere Bölünerek Geçsin" parametresinin işaretli olması gerekir. |
| Maliyet Dağıtımı | Sistemde yer alan alış ya da satış tipli fatura belgelerinin “Maliyet Dağıtım” işlemleri için kullanılan alandır. Mevcut bir fatura belgesinin “Kalem Bilgileri” sayfasında, sağ fare tuşu tıklandığında çıkan menüde, “Maliyet Dağıtım“ tıklandığında, otomatik olarak “Maliyet Dağıtım” ekranı açılır. Bu ekranda, fatura belgesinin dağıtımı yapılacak şekilde otomatik ayarlamalar yapılır. Aynı durum, “Toplamlar” sekmesinde yer alan “Maliyet Dağıtım” alanının işaretlenmesi durumunda da geçerlidir. **"Tamam"** tuşuna basıldığında “Maliyet Dağıtımı” ekrana gelir Bu kolaylık ile birlikte, “Maliyet Dağıtım” ekranına manuel girmeye gerek kalmadan, fatura girişi esnasında otomatik olarak maliyet dağıtımı yapılması sağlanmıştır. Dağıtılacak fatura belgesinin “Hizmet Prim Belgesi” olması durumunda, “Maliyet Dağıtım” ekranında yer alan dağıtım anahtarı değeri, “Hizmet Prim Belgesi” olacak şekilde otomatik ayarlanır. Diğer fatura belgelerinin dağıtımı işleminde ise, dağıtım anahtarı değeri manuel seçilmelidir. |
| Tamam | Bilgileri girilen faturanın kaydı için kullanılan butondur. Tamam ![](../../../../../_assets/23043a6798351fd813b5.png)butonuna basıldığında, faturaya ilişkin kayıtlar ilgili entegre bölümlere aktarılır. Faturanın daha önce kaydedilmiş olması ve düzenlenip tekrar kaydedilmesi durumunda, entegre bölümlerden stok ve cari bölümlere işlenen hareketler program tarafından düzenlenir. Bu kayıtlar, Entegrasyon/Entegrasyon Kayıtlarında “2 no.lu" (Düzeltilmiş Kayıt) ya da “4 no.lu" (Düzeltilmiş Bulunamadı) tipte izlenir. |

Maliyet Dağıtımı Ekranı Dağıtım Genel Bilgileri alanları ve içerdiği bilgiler şunlardır:

| Maliyet Dağıtımı Ekranı | Dağıtım Genel Bilgileri |
| --- | --- |
| Fiş No | Maliyet dağıtım fişine ait sıra numarasının gösterildiği alandır. Prim hesaplaması yapılan ürünlere ait prim dağıtımları bu alana girilen fiş numaraları ile takip edilir. Ancak buradaki fiş numarası, programdaki diğer fatura numaraları ile karıştırılmamalıdır. Perakende uygulamasına özel bir fiş numarasıdır. Yanlış dağıtım yapıldığında, geriye dönük belgeleme için önemlidir. |
| Maliyet Dağıtım Anahtarı | Fatura belgesine ait, maliyet dağıtım şeklinin seçildiği alandır. Aşağı ok tuşuna tıklayarak seçim yapılır. “Hizmet Prim Belgeleri” isimli anahtar, programda daha önceden oluşturulmuş bir anahtardır. Dolayısıyla, “Hizmet Prim Belgeleri” sisteme tanıtılmış durumdadır. Program, sistemdeki fatura belgelerinin hizmet prim faturası olup olmadığını ayırır. “Maliyet Dağıtım Anahtarı” yazısının üzerine çift tıklandığında, Maliyet Dağıtım Anahtarı ekranına otomatik olarak geçiş yapılabilir. Bu alanda, “Hizmet Prim Belgeleri” başlıklı anahtar dışında nakliye, montaj, vb. diğer fatura belgeleri için “Maliyet Dağıtım Anahtarı” ekranında önceden oluşturulan şablonlar da listelenir. |
| Fiş Tarihi | Maliyet dağıtımının hangi tarihte yapılacağının girildiği alandır. |
| Maliyet Dağıtımı Ekranı | Dağıtılacak Kaynak Belge Kısıtları-Genel Kısıtlar |
| Belge Tipi | Alış Faturası ve Satış Faturası olarak iki seçenek içeren alandır. Aşağı ok ile ilgili fatura seçimi yapılır. |
| Tipi | Kapalı, Açık, Muhtelif, İade ve Zayi İade seçeneklerini içeren alandır. İlgili tip aşağı ok tuşu ile seçilerek ilerlenir. |
| Belge No Aralığı | Dağıtımı yapılacak veya kısmi dağıtımı yapılmış olan fatura belgelerinin ekrana gelmesini sağlayan alandır. ![](../../../../../_assets/088477bb321d1b20c939.jpg) tuşu ile belge numaraları arasından seçim yapılır. |
| Kod 1 | Alış faturasında girilmiş olan Kod 1 alanındaki değere göre kısıt verilmesini sağlayan alandır. |
| Kod 2 | Alış faturasında girilmiş olan Kod 2 alanındaki değere göre kısıt verilmesini sağlayan alandır. |
| Tarih Aralığı | Dağıtımı yapılacak belgelerin ekrana gelebilmesi için girilen tarih aralığıdır. |

Dağıtılacak kaynak belge kısıtları verildikten sonra Kayıt Getir ![](../../../../../_assets/5e13c4e6a56c1c670520.png) butonuna basılarak, ekranın sağ bölümünde o satış faturasına ait kayıtlar listelenir. Listedeki kayıt üzerine sağ fare tuşu ile tıklandığında, seçili satırda maliyet dağıtımı yapılır. Satır üzerinde sağ ok ![](../../../../../_assets/e4bfda3a4ab1d3d44663.jpg) ve üç nokta ![](../../../../../_assets/e577cf0766513395a6ad.jpg) tuşlarına çift tıklanarak fatura detayı görüntülenir.

![](../../../../../_assets/cafbf8e6a4522bee3cea.jpg)

Maliyet Dağıtımı Ekranı Dağıtılacak Kaynak Belge Kısıtları-Stok Kısıtları alanları ve içerdiği bilgiler şunlardır:

| Maliyet Dağıtımı Ekranı | Dağıtılacak Kaynak Belge Kısıtları-Stok Kısıtları |
| --- | --- |
| Stok Kodu | Stoka ait kod numarasıdır. ![](../../../../../_assets/088477bb321d1b20c939.jpg) tuşu ile stok kodları arasından seçim yapılır. |
| Grup Kodu | Gruba ait kod numarasıdır. ![](../../../../../_assets/088477bb321d1b20c939.jpg) tuşu ile grup kodları arasından seçim yapılır. |
| Stok Kod 1/2/3/4/5 | Aynı tür ve özelliklere sahip olan stok kayıtlarının gruplanarak bir arada raporlarının alınabilmesine yönelik stok kodlarının seçildiği alandır. Üç nokta ![](../../../../../_assets/e577cf0766513395a6ad.jpg)tuşu ile stok kodları arasından seçim yapılır. |
| Cari/Satıcı Kodu | Cariye ait kod numarasıdır. ![](../../../../../_assets/088477bb321d1b20c939.jpg) tuşu ile cari kodlar arasından seçim yapılır. |

Dağıtılacak Kaynak Belge Kısıtları-Stok Kısıtları alanlarına verilen kısıt sayesinde, dağıtılacak belgelerin kayıtlarının gelmesi sağlanır. Kayıt Getir ![](../../../../../_assets/5e13c4e6a56c1c670520.png) butonuna basıldığında, ekranın sağ bölümünde, satış faturasına ait kayıtlar listelenir. Listedeki kayıdın üzerine sağ fare tuşu ile tıklandığında, seçili satırda maliyet dağıtımı yapılır. Satır üzerinde sağ ok![](../../../../../_assets/e4bfda3a4ab1d3d44663.jpg) ve üç nokta ![](../../../../../_assets/e577cf0766513395a6ad.jpg) butonlarına çift tıklandığında fatura detayı görüntülenir.

![](../../../../../_assets/3077088a5630624462cd.jpg)

Maliyet Dağıtımı ekranı Dağıtılacak Kaynak Belge Kısıtları-Cari Kısıtları sekmesi alanları ve içerdiği bilgiler şunlardır:

| Maliyet Dağıtımı Ekranı | Dağıtılacak Kaynak Belge Kısıtları-Cari Kısıtları |
| --- | --- |
| Cari Kod Aralığı | Maliyet dağıtımı yapılacak faturaya, kısıt vermek için cari kod seçiminin kullanıldığı alandır. ![](../../../../../_assets/088477bb321d1b20c939.jpg) tuşu ile cari kodlar arasından seçim yapılır. |
| Cari Grup Kodu | Cari gruba ait kod bilgisinin girildiği alandır. ![](../../../../../_assets/088477bb321d1b20c939.jpg) tuşu ile grup kodları arasından seçim yapılır. |
| Bağlı Cari Kodu | Farklı teslim adresleri için cari kartların birbirleri ile ilişkilendirilmesini sağlayan alandır. ![](../../../../../_assets/088477bb321d1b20c939.jpg) tuşu ile bağlı cari kodlar arasından seçim yapılır. |
| Kullanıcı Tanımlı Saha Kısıtları | Cari hesap kartlarında girilmiş olan kullanıcı tanımlı saha değerlerine göre kısıtlama yapılmasını sağlayan alandır. |

Dağıtılacak Kaynak Belge Kısıtlarındaki “Dağıtılacak Tutar” kolonundaki prim tutarı değerinin, Dağıtımı Yapılacak Hedef Belge Kısıtlarındaki “Dağıtılacak Tutar” kolonundaki tutarların toplamıyla aynı olması gerekir. Prim tutarının tamamı dağıtılabileceği gibi, kısmi olarak da dağıtım yapılabilir. Kısmi olarak dağıtılan prim tutarı “Dağıtılmış Tutar” kolonunda görüntülenir.

**Dağıtımı Yapılacak Hedef Belge Kısıtları**

Dağıtımı yapılacak hedef belgelere kısıt vermek için kullanılır. Genel Kısıtlar, Stok Kısıtları ve Cari Kısıtlar olmak üzere üç bölümden oluşur. **Dağıtılacak Kaynak Belge Kısıtları** kısmında verilen kısıtların aynısı bu kısımda da verilir.

Dağıtılacak kaynak belge kısıtları verildikten sonra Kayıt Getir ![](../../../../../_assets/5e13c4e6a56c1c670520.png) butonuna basıldığında, “Prime Esas Hareketler Otomatik Getirilsin Mi?” sorusunun yazılı olduğu uyarı ekranında “evet” butonu seçilerek, prim tutarlarının hesaplandığı belge/belgeler ve ilgili ürün kodları program tarafından otomatik olarak ekranın sağ tarafında listelenir. “hayır” butonunun seçilmesi halinde, seçim kullanıcıya bırakılır. Kısıtları Temizle ![](../../../../../_assets/064db28106431a884c09.jpg) butonu ile girilen kısıtlar silinir.

Listedeki kayıt üzerine sağ fare tuşu ile tıklanarak, seçili satırda maliyet dağıtımı yapılır. Satır üzerinde sağ ok ![](../../../../../_assets/e4bfda3a4ab1d3d44663.jpg) ve üç nokta ![](../../../../../_assets/e577cf0766513395a6ad.jpg) butonlarına çift tıklanarak fatura detayı görüntülenir.

Dağıtım işlemini sonlandırmak için “Kaydet” butonuna basılır. Ardından ekrana “Eşleştirme işleminiz kaydedilecektir. Emin misiniz?” yazılı onaylama ekranı gelir. Bu onay ekranında “Evet” butonuna basılması halinde dağıtım işlemi yapılmış olur. “Maliyet Dağıtım İşleminiz Başarı ile Gerçekleştirilmiştir.” yazılı uyarı ekranının gelmesiyle de işlem son bulur.

Önceden oluşturulmuş maliyet dağıtım fişleri üzerinde herhangi bir değişiklik yapılamaz fakat “Fiş İptali” yapılabilir. Fiş no rehberinden, önceden kayıtlı fiş seçildiğinde, “Fiş İptal” butonu ile işlem gerçekleşir.

![](../../../../../_assets/a06058b45b966594ce57.jpg)

"Maliyet Dağıtımı" ekranında iken, ilgili kayıt üzerinde çift tıklanarak, klavyeden “Delete” tuşuna basıldığında seçili satır silinir. Sağ klik tuşu ile de, ilgili satır maliyetine göre dağıtılabilir, fatura belgesi görüntülenebilir ve satır/satırların silme işlemleri yapılabilir.

![](../../../../../_assets/1fde67651d28434c7aeb.jpg)

Mal Fazlası İskontosu, Satır İskontosu, Genel İskonto, Ek Maliyet 1-2, Sıralama Seçeneği, Vadelere Bölme alanları **"[Alış Parametreleri](index.md)"** sayesinde, isteğe bağlı olarak ekranda yer alabilir/almayabilir.

Alış Faturası Kaydı, Değişikliği, İptali aşağıdaki şekilde yapılır:

- Alış faturasının kaydı için, fatura ekranındaki alanlara bilgi girişi yapıldıktan sonra, "Toplamlar" ekranında "**tamam"** tuşuna basılır. Böylece, Üst Bilgiler ekranında seçilen tipe göre, gerekli bölümlerde entegre kayıtlar oluşur.
- Daha önceden kaydedilmiş bir fatura üzerinde değişiklik yapmak için, "Üst Bilgiler" ekranından ilgili faturanın numarası girilerek \<tab\> butonuna basılır. Böylece, kayıtlı faturaya ait daha önceden girilmiş bilgiler ekrana gelir. Mevcut ekranda değiştirilmek istenen alana gelip düzenleme yapılır. Burada dikkat edilmesi gereken nokta, belge üzerinde değişiklik yapıldıktan sonra, fatura ile ilgili bağlantılı bölümlerde de gerekli değişikliklerin program tarafından yapılabilmesi için, "**Toplamlar"** ekranından belgenin tekrar kaydedilmesi gerekir.
- Kaydedilmiş bir alış faturasının iptali için, "Üst Bilgiler" ekranında iken araç çubuklarında bulunan Kayır Sil ![](../../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna ya da klavyedeki F7 butonuna basılır. Bu aşamada program, “Bu ekrana ait tüm bilgileriniz silinir. Emin misiniz?” şeklinde bir uyarı ekrana getirir. “Evet” butonuna basılması halinde, ilgili faturaya ait bilgiler, bağlı olduğu tüm bölümler dahil olmak üzere sistemden silinir.
