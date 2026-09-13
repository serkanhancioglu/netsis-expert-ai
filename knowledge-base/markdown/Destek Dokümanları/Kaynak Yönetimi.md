---
title: "Kaynak Yönetimi"
page_id: "50679870"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Kaynak Yönetimi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Kaynak Yönetimi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWJiNGJhMmM2LTRkNGYtNDQyNy05MTU3LWM0MjI0OGU3ZGQ4MSZsaW5rPTc0ZWI4OGU4LTVjMjgtNDY5ZS05OWQwLWZjN2Q5NmU0Yzg3YSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=bb4ba2c6-4d4f-4427-9157-c42248e7dd81&link=74eb88e8-5c28-469e-99d0-fc7d96e4c87a&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "kaynak-yonetimi_82575986_50679870.html"
source_version: "2022-12-19T11:53:56.937+03:00"
source_bytes: 931939
fetched_at: "2026-09-13T04:25:53+00:00"
generator: "netsis-scraper 1.0.0"
---
# Kaynak Yönetimi

Kaynak Yönetimi ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

**Genel**

|  |  |
| --- | --- |
| **Ürün** **Grubu** | \[X\] Netsis 3 Enterprise \[X\] Netsis 3 Standard |
| **Kategori** | \[X\] Yeni Fonksiyon |
| **Modül** | MRP, Üretim, Üretim Akış Kontrol |
| **Versiyon** **Önkoşulu** | 9.0.6 Onaylı Versiyon |
| **Gerekli** **Dosyalar** | 9.0.6 Seti Dosyaları |

#### Kaynak Yönetimi Genel Uygulama ve Amaç

Üretim sırasında ihtiyaç duyulan ve bu sebeple kullanımı gerekli olan takım, teçhizat gibi aletlere kaynak denmektedir. Üretim sektöründen örnek vermek gerekirse, torna makinesine takılan kesici uç veya enjeksiyon makinesine takılan kalıp vs. gibi kaynaklar sıklıkla kullanılmaktadır. Kaynak yönetimi sayesinde üretimde kullanılan kaynakların tanımları yapılmakta ve üretim kayıtları sırasında kaynak kullanımları girilerek kaynakların ömür takibi yapılabilmekte, geçmişe yönelik kaynak hareketleri izlenebilmektedir. Ayrıca ileri üretim planlama uygulamasında kaynakların ömür bilgileri dikkate alınmaktadır ve çizelgeleme sonucu bu bilgiye göre oluşmaktadır. Tamir edilebilen kaynaklar için çizelgeleme sonucuna göre bakım planı çıkarılmaktadır. Kaynak tanımlama sırasında mevcut stok kodları veya demirbaş modülünde tanımlanan demirbaş kartları kullanılabileceği gibi, kullanıcı tarafından verilecek yeni kodlar ile serbest tanımlama imkanı da bulunmaktadır.
Kaynak yönetimi kapsamında kullanılacak ekranlar "MRP \> Kayıt \> Kaynak Yönetimi" menüsü altına eklenmiştir. Ayrıca "MRP \> Raporlar" menüsü altına "Kaynak Hareketleri Raporu" eklenmiştir.

#### Kaynak Tanımlama

Üretimde kullanılan kaynakların tanımı "MRP-Kaynak Yönetimi-Kaynak Tanımlama" ekranı üzerinden yapılmaktadır.
![](../_assets/01f510d356b2550325bf.png)

Kaynak tanımlama ekranında "**Kaynak Bilgileri**" sekmesinde bulunan alanlar ve açıklamaları aşağıdaki gibidir.

**Kaynak** **Tipi:** Kaynak tanımında kullanılabilecek Stok, Demirbaş ve Personel olmak üzere 3 farklı kaynak tipi bulunmaktadır.

**Stok:** Bu tip seçildiğinde kaynak kodu olarak sistem üzerinde tanımlı olan stok kodlarından biri kullanılmaktadır. Stok tipli kaynakların hareketleri, stok hareketleriyle bütünleşik çalışmaktadır. Örneğin stok için alış faturası girildiğinde kaynak hareketlerine de ömür artışı olarak yansımaktadır. Üretim kayıtları sırasında girilen kaynak kullanımları da stok hareketlerine sarf miktarı olarak yansımaktadır.

**Demirbaş:** Bu tip seçildiğinde demirbaş paketiyle bağlantılı olarak kaynak tanımı yapılabilmektedir, bu durumda kaynak kodu olarak demirbaş paketindeki demirbaş kodlarından biri kullanılmaktadır ve demirbaş paketindeki kart tanımı dikkate alınmaktadır. Ayrıca demirbaş paketinden yapılacak satış ve transfer hareketleri, kaynak hareketlerine otomatik olarak yansımaktadır.

**Personel:** Bu tip seçildiğinde personel paketiyle bağlantılı kaynak tanımı yapılabilmektedir. Personel tipli kaynaklar için ömür takibi yapılamaz ve kaynak hareketleri izlenemez.

**Demirbaş Bağlantılı, Personel Bağlantılı:** "Demirbaş Bağlantılı" seçeneği demirbaş tipli kaynaklarda aktif hale gelirken, "Personel Bağlantılı" seçeneği de personel tipli kaynaklarda aktif hale gelmektedir. Bu seçenek işaretlenmezse, personel veya demirbaş paket bağlantısı olmadan serbest tanım yapılabilmektedir, bu durumda kullanıcı tarafından yeni bir kaynak kodu verilmektedir.

**Şirket Kodu:** Demirbaş veya personel paketleriyle bağlantısı bulunan kaynaklar için kullanılmaktadır ve ilgili uygulamada kullanılan şirket kodu seçilmelidir. Paket bağlantısı yoksa bu alana değer girilemez.

**Kaynak Kodu:** Bu alanda stok tipli kaynaklar için stok kodu, demirbaş paketiyle bağlantılı kaynaklar için demirbaş kodu, personel paketiyle bağlantılı kaynaklar için personel kodu seçilmektedir. Paket bağlantısı olmadan tanımlanan personel veya demirbaş tipli kaynaklar için kullanıcı tarafından yeni bir kaynak kodu verilmelidir.

**Kaynak İsmi:** Paket bağlantısı olmayan demirbaş veya personel tipli kaynak tanımlarında doldurulabilir, aksi durumda bu alana giriş yapılamaz ve kaynak ismi ilgili kart tanımından (stok kartı, demirbaş kartı vs.) otomatik olarak getirilir.

**Kaynak** **Grup** **Kodu:** Kaynak tanımlarını gruplayabilmek için kullanılacak alandır.

**İstasyon Kodu:** Kaynağın kullanıldığı istasyon bilgisi bu alana girilebilir. Girişi zorunlu değildir, boş geçilebilir.

**Birim** **Maliyet:** Kaynağın birim maliyet bilgisi bu alana girilebilir, rapor amaçlıdır.

**Durum:** Bu alanda "Aktif" veya "Pasif" seçeneklerinden biri seçilebilir. Durumu pasif olarak seçilen kaynaklar için hareket girişi yapılamaz ve bu kaynaklar ileri üretim planlama sırasında kullanılamaz.

**Toplam Miktar:** Paket bağlantısı olmayan demirbaş veya personel tipli kaynak tanımlarında doldurulabilir, aksi durumda bu alana giriş yapılamaz ve kaynak miktarı ilgili kartın hareketlerinden (stok kartı, demirbaş kartı vs.) otomatik olarak getirilir. Örneğin stok tipli bir kaynağın toplam miktar bilgisi, stok hareketlerindeki bakiyeden getirilir. Demirbaş tipli bir kaynağın toplam miktar bilgisi ise, demirbaş kartındaki miktar değeri ve demirbaş satış hareketlerine bakılarak hesaplanır.

**Öncelik Sırası:** Kaynak tanımına ait öncelik bilgisi bu alana girilebilir. Bu alana girilen öncelik değeri ileri üretim planlama uygulamasında kullanılmaktadır, öncelik değeri daha küçük olan kaynaklar planlamada daha öncelikli olarak kullanılmaktadır.

**Ömür Takibi Yapılsın:** Ömür takibi yapılacak kaynaklar için bu seçenek işaretlenmelidir. Bu seçenek işaretlenirse "Ömür Takibi" sekmesindeki "Toplam Ömür" alanının doldurulması zorunludur.

Kaynak tanımlama ekranında "**Ömür Takibi**" sekmesinde bulunan alanlar ve açıklamaları aşağıdaki gibidir:
![](../_assets/a79597f9a3dabbac138e.png)

**Son** **Kullanma** **Tarihi:** Kaynak için son kullanma tarihinin girilebileceği alandır. İleri üretim planlama sırasında bu tarihten daha sonrası için kaynağa iş planlanmayacaktır.

**Toplam Ömür:** Kaynağın bir birimi için toplam ömür bilgisi bu alana girilebilir. Kaynakla ilgili tahmini ömür bilgisidir, kesinlik içermez. Herhangi bir anda kaynağın kalan ömür bakiyesi ve ömür yüzdesi hesaplanırken, toplam ömür bilgisi kullanılmaktadır. Toplam ömür bilgisinin birimi, kullanıcı tarafından serbest olarak belirlenmektedir. Örneğin vuruş, kesim vs. gibi birimler tanımlanabilir. Kaynak kullanımları ve hareketleri de bu tanımlama sırasında girilen birim üzerinden gösterilecektir.

**Kalıp** **Göz** **Sayısı:** Tanımlanan kaynak kalıp ise ve birden fazla gözü bulunuyorsa, bu alan doldurulabilir. Kaynak kullanımları girilirken tanımlamada verilen göz sayısı otomatik olarak getirilecektir, ancak kullanıcı tarafından değiştirilebilir. Göz sayısına bağlı olarak kaynağın ömür tüketimi değişecektir. Örneğin 2 gözlü bir kaynakla 100 adetlik üretim 50 vuruş ömür tüketirken, 1 gözlü bir kaynakla aynı üretim 100 vuruşluk ömür tüketimine sebep olmaktadır. Not: Kaynak kullanımlarının girişi sırasında göz sayısının girilebilmesi için kaynak tanımlarında göz sayısının 1'den büyük olduğu en az bir tanım bulunmalıdır.

**Tamir** **Edilebilir:** Tanımlanan kaynak için tamir yapılabiliyorsa bu seçenek işaretlenmelidir ve tamirle ilgili genel bilgiler girilmelidir.

**Ortalama Bakım Süresi:** Kaynak için tahmini bakım süresi bu alana girilebilir. İleri üretim planlama sırasında tamir edilebilir kaynakların ortalama bakım süresi dikkate alınmaktadır ve tamir dönüşünde kaynağa tekrardan iş planı yapılabilmektedir.

**Max. Bakım Sayısı:** Kaynak için yapılabilecek maksimum tamir sayısı bu alana girilebilir. İleri üretim planlama sırasında bakım planı çıkarılırken maksimum bakım sayısı dikkate alınmaktadır ve maksimum bakım sayısına ulaşan kaynaklara iş planlanmayacaktır. Sıfır olarak tanımlanırsa maksimum bakım sayısı sınırsız olarak kabul edilmektedir.

**Bakımda Yıpranma Payı (%):** Bakım sonrasında kaynağın toplam ömründe beklenen yıpranma payı yüzde olarak bu alana girilebilir. Bu bilgi ileri üretim planlama sırasında dikkate alınmaktadır ve bakımdan dönen kaynakların toplam ömür bilgisi bu değere göre belirlenmektedir. Örneğin toplam ömrü 1000 vuruş olan bir kaynağın bakımda yıpranma payı %10 olarak tanımlanmış ise, bu kaynağın ilk bakımdan dönüşünde toplam ömrünün 900 vuruş olacağı varsayılacaktır.

#### Operasyon-Kaynak Eşleştirme

Ürün ve ürünün operasyonları bazında kullanılabilecek kaynakların tanımlandığı ve varsayılan ömür tüketimlerinin girilebildiği ekrandır. Bu ekranda yapılan tanımlamalar kaynak kullanımı sırasında otomatik olarak tüketimlerin getirilmesini sağlamaktadır, kullanıcı otomatik gelen bu bilgiler üzerinden istediği değişiklikleri ve ekleme-çıkarma yapabilir. Aynı zamanda ileri üretim planlama uygulaması da bu ekrandan yapılan tanımlara göre planlama yapmaktadır, "hangi ürünün üretiminde hangi kaynaktan kaç adet kullanılacağı" bu ekrandan yapılan eşleştirmeler sayesinde bilinmektedir.
Operasyon-Kaynak Eşleştirme tanımlaması için aşağıdaki işlem adımları sırasıyla izlenmelidir:

- Operasyon seçimi yapılır. Kaynağın kullanıldığı operasyon bilgisi seçilmelidir. Operasyon kodu bazında tanım yapılabileceği gibi, operasyon grubu veya tüm operasyonlar için de tanım yapılabilir. Örneğin OP_GRUP1 operasyon grubundaki bütün operasyonlar aynı kaynağı kullanıyorsa, operasyon grubu üzerinden tanımlama yapmak kolaylık sağlayacaktır.
- Ürün seçimi yapılır. Operasyon kodu belirlendikten sonra ürün detayında kaynak eşleştirmesi yapabilmek için ürün detayı verilebilir. Ürün kodu bazında tanım yapılabileceği gibi, ürün grubu veya tüm ürünler için de tanım yapılabilir. Örneğin kaynak kullanımı için ürün detayı vermeye gerek yoksa, ilgili operasyonda bütün ürünler aynı kaynağı kullanıyorsa, tüm ürünler üzerinden tanımlama yapmak kolaylık sağlayacaktır.
- Kullanılacak kaynak bilgilerinin set yapısında tanımı yapılır. Set kavramı, bir arada kullanılacak birden fazla kaynağı küme haline getirmek için kullanılmaktadır. Bir setin içine bir veya daha fazla kaynak eklenebilir, bu kaynaklar üretim sırasında bir arada kullanılmaktadır. Aynı şekilde bir operasyon ve ürün kodu için birden fazla set tanımı yapılabilir, bu durumda her set tanımı birbirinin alternatifi gibi düşünülebilir. Örneğin OP1 için MAMUL1 üretimi sırasında kullanılan kaynakların SET1 ve SET2 gibi iki set şeklinde tanımlandığını düşünelim. Bu tanımlama şu anlama gelmektedir: MAMUL1 üretimi sırasında OP1 operasyonu yapılırken SET1 **veya** SET2 içindeki kaynaklar kullanılacaktır.
- "Set Öncelik Sırası" ekran tarafından otomatik olarak verilir. Kullanıcı isterse set önceliğini değiştirebilir. Set önceliği, ileri üretim planlama sırasında seçilecek kaynakları etkilemektedir. Set önceliği küçük olan tanımlar daha önceliklidir.
- Setin içine eklenecek kaynak bilgileri girilir. Kaynak kodu bazında tanım yapılabileceği gibi, kaynak grubu veya tüm kaynaklar için de tanım yapılabilir. Kaynak bilgisi seçildikten sonra "Kaynak Sayısı" alanına üretim sırasında ilgili kaynaktan kaç adet kullanılacağının bilgisi girilir. Bir birimlik üretim sırasında ilgili kaynağın ömründen yapılacak tüketim miktarı "Ömür Tüketimi" alanına girilir.
- Yeni bir set eklemek için ekranı sağ alt köşesindeki "Yeni Set Ekle" butonu kullanılarak işlemlere devam edilir. Başka bir operasyonun tanımlarına geçmek için ekranın ilk bölümündeki operasyon bilgisi değiştirilir.

![](../_assets/55703b0bf9fdc6e967de.png)
Örneğin yukarıdaki ekran görüntüsünde OP021 operasyonu için MAMUL1 üretimi sırasında kullanılacak kaynaklar SET1 veya SET2 şeklinde tanımlanmıştır. Üretim sırasında bu setlerden bir tanesi seçilerek kullanılacaktır. SET1 kümesi içinde KALIP1 ve TESTERE_01 kaynakları bir arada kullanılırken, SET2 kümesi içinde KALIP2 ve TESTERE_01 kaynakları bir arada kullanılmaktadır.

#### Kullanılan Kaynak Girişi

Üretim kayıtlarının girildiği aşağıdaki ekranlarda kullanılan kaynak girişi desteklenmiştir:

**Üretim akış kaydı:** Ekran üzerindeki "Kullanılan Kaynaklar" butonuyla kaynak girişi yapılabilir.

**Üretim sonu kaydı:** Grid üzerindeki üretim satırı seçilerek sağ tık menüsünden kaynak girişi yapılabilir.

**Serbest üretim sonu kaydı:** Grid üzerinde sağ tık menüsünden kaynak girişi yapılabilir.

Kaynak girişi yapılacak ürün için operasyon-kaynak eşleştirmesi bulunuyorsa, bu eşleşmedeki bilgiler otomatik olarak getirilecektir. Eğer operasyon-kanyak eşleşmesinde birden fazla alternatif set tanımlanmış ise, ekran aşağıdaki gibi "set seçimi" sekmesiyle açılacaktır, aksi durumda bu sekme ekrana gelmeyecektir. Set seçimi sekmesinde operasyon bazında tanımlanmış olan alternatif kaynak setleri gösterilecektir, tanımlı setlerden biri seçilerek işleme devam edilebilir ya da direkt olarak ikinci sekme üzerinden serbest giriş yapılabilir.
![](../_assets/d26e5722d23e09e0c593.png)
Kullanılan kaynaklar sekmesinde kaynak kodu seçilerek, üretimde kullanılan kaynak miktarı ve ömür tüketimi girilebilir. Operasyon-kaynak eşleşmesine göre kullanılan kaynaklar otomatik olarak getirilmektedir, ancak kullanıcı bu bilgiler üzerinde değişiklik yapabilir veya yeni kaynak kullanımı girebilir.
Üretim akış kaydı sırasında girilen kaynak bilgileri, iş emrine bağlı yapılan üretim sonu kayıtlarında otomatik olarak getirilir, bu kayıtlar üzerinde düzenleme yapılamaz, ancak yeni kaynak kullanımları girilebilir. Kaynak kullanımlarını girmek için üretim akış kaydının kullanılması zorunlu değildir, üretim sonu kaydı atılırken de kaynak kullanımlarını girmek mümkündür.
![](../_assets/47cd6f85b8ae020749ee.png)

#### Kaynak Hareketleri

Kaynak hareketleri ekranı sayesinde kaynak kullanımlarını, ömür tüketimlerini ve kaynakların şu anki durumunu detaylı olarak incelemek mümkündür. Aynı zamanda bu ekran üzerinden demirbaş tipli kaynaklar için tamire gidiş ve tamirden dönüş hareketleri girilebilir. Kaynak Hareketleri ekranı, Özet Bilgiler ve Kaynak Hareketleri olmak üzere iki sekmeden oluşmaktadır. "Özet Bilgiler" sekmesinde bütün kaynakların toplu listesi ve bazı özet raporlar gösterilmektedir. "Kaynak hareketleri" sekmesinde ise kaynak kodu bazında hareket kayıtlarını detaylı olarak incelemek mümkündür.
![](../_assets/85fca7cdc930716a4588.png)
Özet bilgiler sekmesinde ekranın sol üst bölümünde "Ömrü Azalan Kaynaklar" listelenmektedir, bu bölümde ömür yüzdesi en küçük olan ilk 5 kaynak gösterilmektedir. Ekranın sağ üst bölümünde "Bakımdaki Kaynaklar" listelenmektedir, bu bölümde tamire gitmiş ancak henüz tamirden dönmemiş kaynak kodları gösterilmektedir, ayrıca bu kaynakların bakımda geçen süreleri ve kaynak kartlarında tanımlanmış olan ortalama bakım süreleri izlenmektedir. Ekranın alt bölümde ömür takibi yapılan kaynakların bir listesi ve bu kaynaklara ait özet bilgiler bulunmaktadır (ömür bakiyesi, ömür yüzdesi vs.). Kaynak listesindeki herhangi bir kayda çift tıklayarak veya üst bölümdeki grafiklerde ilgili kaynak koduna tıklayarak kaynağın hareket kayıtlarına ulaşılabilir.
![](../_assets/6b13a50a876fe3d7f268.png)
Kaynak hareketleri sekmesinde kaynak kodu girilerek geçmişe yönelik hareketler raporlanmakta ve kaynağın yürüyen ömür bakiyesi izlenmektedir. Demirbaş tipli kaynakların tamire gidiş ve tamirden dönüş hareketleri bu ekrandan girilebilir. Üretim sırasında girilen kaynak kullanımları ekranda gösterilmektedir, fakat bu kayıtlar üzerinde düzenleme yapılamaz. Aynı şekilde stok tipli kaynakların fatura vs. gibi hareketleri de bu ekranda gösterilmektedir, fakat bu kayıtlar üzerinden düzenleme yapılamaz.
Kaynak hareketleri sekmesinin sağ üst köşesindeki ikona tıklayarak grafik için görünüm seçeneği değiştirilebilir. Varsayılan olarak grafikte bütün kayıtlar gösterilmektedir, ancak haftalık, günlük vs. gibi seçenekler sayesinde gösterilen kayıt sayısı kısıtlanabilir, daha detaylı kısıt verebilmek için tarih aralığı girmek de mümkündür. Örneğin haftalık görünüm seçildiğinde, grid üzerinden seçilen kaydın bulunduğu haftadaki bütün hareketler gösterilir.
![](../_assets/deaa5fa71828446084bd.png)
Kaynak hareketleri grafiğindeki noktalara tıklandığında, grid üzerindeki hareket satırı otomatik olarak seçilmektedir. Bu satır üzerinden hareketin detayı (hangi üretim fişinde kullanılmış, tarih ve ömür tüketim bilgileri vs.) görülebilir.
Stok tipli kaynaklar için üretim sırasında girilen kullanım bilgileri, stok hareketlerine de yansımaktadır. Ancak kaynak hareketleri ekranında ömür birimi üzerinden raporlama yapılmaktadır. Örneğin TESTERE_01 kaynağı stok tipli bir kaynaktır ve kaynak hareketleri aşağıdaki gibi görünmektedir:
![](../_assets/853823185b2407e9f1fb.png)
Kaynak hareketleri ekranındaki miktarlar, "kesim" birimi üzerinden raporlanmaktadır, aynı şekilde üretim belgelerinde kullanılan kaynak girişi yapılırken de miktarlar "kesim" birimi üzerinden girilmiştir. Oluşan ömür tüketimleri stok kartının birinci ölçü birimine çevrilerek stok hareketlerine aşağıdaki şekilde işlenmiştir.

Birinci ölçü birimine çevrim sırasında şu formül kullanılmaktadır: Hareket satırındaki ömür miktarı/Kaynak tanımındaki toplam ömür değeri
![](../_assets/acb45a63736b1c65807b.png)

#### İleri Üretim Planlama ve Kaynak Ömür Takibi

İleri üretim planlama uygulamasında kullanılacak kaynaklar için ömür takibi yapılıyorsa, ömür bakiyeleri dikkate alınmaktadır ve tamir edilebilir kaynakların bakım planı otomatik olarak çıkarılmaktadır, bu raporda tahmini olarak bakıma gidiş ve bakımdan dönüş bilgileri görülmektedir. Bakım süresi olarak kaynak tanımlama ekranında girilen ortalama bakım süresi kullanılmaktadır.
Örneğin kaynak ömür bakiyesi 900 vuruş olan KALIP1 için en fazla 900 vuruşluk iş planlanacaktır, ardından tamir edilebilir bir kaynak ise bakıma gidiş ve bakımdan dönüş planı çıkarılacaktır, bakımdan döndükten sonra "bakımda yıpranma payı" da dikkate alınarak kaynak ömrü yenilecek ve tekrardan yeni işler planlanacaktır.
![](../_assets/230e41550d2960642bca.png)
![](../_assets/a3fc3ddf569bb59ccfe7.png)
Çizelgeleme sonuçlarının gösterildiği gantt ekranda planlanan işlerin üzerine gelindiğinde kullanılan kaynak bilgileri ve tahmini ömür tüketimleri de gösterilmektedir.
![](../_assets/7fa4bec5a555535dcf8f.png)
