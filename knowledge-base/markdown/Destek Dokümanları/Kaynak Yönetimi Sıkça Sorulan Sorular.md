---
title: "Kaynak Yönetimi Sıkça Sorulan Sorular"
page_id: "88900824"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Kaynak Yönetimi Sıkça Sorulan Sorular"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Kaynak Yönetimi Sıkça Sorulan Sorular"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWQzOGY0ZjkzLTEwMTMtNDNiMC05ODc0LWVmMDNkOTEwZjk5YSZsaW5rPWFkNzFjZjg4LWNkMzktNDZhNy04NDkzLWZjMTVhN2U2NDFhZiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=d38f4f93-1013-43b0-9874-ef03d910f99a&link=ad71cf88-cd39-46a7-8493-fc15a7e641af&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "kaynak-yonetimi-sikca-sorulan-sorular_90670184_88900824.html"
source_version: "2022-12-07T15:57:03.297+03:00"
source_bytes: 17247
fetched_at: "2026-09-13T04:23:59+00:00"
generator: "netsis-scraper 1.0.0"
---
# Kaynak Yönetimi Sıkça Sorulan Sorular

**Kaynak yönetiminin amaçları nelerdir?**

Üretim sırasında ihtiyaç duyulan ve bu sebeple kullanımı gerekli olan takım, teçhizat gibi aletlere kaynak denmektedir. Üretim sektöründen örnek vermek gerekirse, torna makinesine takılan kesici uç veya enjeksiyon makinesine takılan kalıp vs. gibi kaynaklar sıklıkla kullanılmaktadır. Kaynak yönetimi sayesinde üretimde kullanılan kaynakların tanımları yapılmakta ve üretim kayıtları sırasında kaynak kullanımları girilerek kaynakların ömür takibi yapılabilmekte, geçmişe yönelik kaynak hareketleri izlenebilmektedir. Ayrıca ileri üretim planlama uygulamasında kaynakların ömür bilgileri dikkate alınmaktadır ve çizelgeleme sonucu bu bilgiye göre oluşmaktadır. Tamir edilebilen kaynaklar için çizelgeleme sonucuna göre bakım planı çıkarılmaktadır.

**Kaynak yönetiminin için ek modül lisansına ihtiyaç var mıdır?**

MRP modül lisansına sahip olunmalıdır.

**Kaynak uygulamasının etkin bir şekilde kullanılabilmesi için ne gibi tanımlamalar yapılmalıdır?**

Üretimde kullanılan kaynakların tanımı "MRP \> Kaynak Yönetimi \> Kaynak Tanımlama" ekranı üzerinden yapılmalıdır. Operasyon ve makine bazında kaynak eşleştirmeleri yapılmak isteniyor ise “MRP \> Kaynak Yönetimi \> Operasyon – Kaynak Eşleştirme “ ve “MRP \> Kaynak Yönetimi \> Makine – Kaynak Eşleştirme “ ekranları üzerinden de tanımlamalar yapılmalıdır.

**Program içerisinde desteklenen kaynak tipleri nelerdir?**

Kaynak tanımında kullanılabilecek stok, demirbaş ve personel olmak üzere 3 farklı kaynak tipi bulunmaktadır.

**Stok:** Bu tip seçildiğinde kaynak kodu olarak sistem üzerinde tanımlı olan stok kodlarından biri kullanılmaktadır. Stok tipli kaynakların hareketleri, stok hareketleriyle bütünleşik çalışmaktadır. Örneğin stok için alış faturası girildiğinde kaynak hareketlerine de ömür artışı olarak yansımaktadır. Üretim kayıtları sırasında girilen kaynak kullanımları da stok hareketlerine sarf miktarı olarak yansımaktadır.

**Demirbaş:** Bu tip seçildiğinde demirbaş paketiyle bağlantılı olarak kaynak tanımı yapılabilmektedir, bu durumda kaynak kodu olarak demirbaş paketindeki demirbaş kodlarından biri kullanılmaktadır ve demirbaş paketindeki kart tanımı dikkate alınmaktadır. Ayrıca demirbaş paketinden yapılacak satış ve transfer hareketleri, kaynak hareketlerine otomatik olarak yansımaktadır. "Demirbaş Bağlantılı" seçeneği işaretli olmaması durumunda kullanıcı tarafından yeni bir kaynak kodu verilmektedir.

**Personel:** Bu tip seçildiğinde personel paketiyle bağlantılı kaynak tanımı yapılabilmektedir. Personel tipli kaynaklar için ömür takibi yapılamaz ve kaynak hareketleri izlenemez. "Personel Bağlantılı" seçeneği işaretli olmaması durumunda kullanıcı tarafından yeni bir kaynak kodu verilmektedir.

**Kaynaklar için ömür takibi yapılabilir mi?**

Ömür takibi yapılacak kaynaklar için kaynak tanımlama ekranında ömür takibi yapılsın seçeneği işaretlenmelidir. Böylece “Ömür Takibi “sekmesindeki "Toplam Ömür" alanına tahmini ömür bilgisi girişi yapılabilmektedir.

**Kaynağımızın ömrü bitti ya da kaynak artık kullanılmak istenilmiyorsa ne yapılmalıdır?**

Kaynak tanımlama ekranında durum alanı pasife çekilmesi durumunda bu kaynak artık kullanılamayacak ve ileri üretim planlamada da dikkate alınmayacaktır. Aynı zamanda ömür takibi yapılsın işaretli ve ilgili kaynak için son kullanma tarihi belirtilmiş ise bu tarihten sonrası için ileri üretim planlama bu kaynağı dikkate almayacaktır.

**Kullanılan kaynak iş emrinin tüm operasyonları boyunca kullanılmak isteniyor ise nasıl tanımlama yapılmalıdır?**

Kaynak tanımlama ekranı üzerinden “İş Emrinin Operasyonları Boyunca Rezerve Edilsin” seçeneğinin işaretlenmesi durumunda ilgili kaynak o iş emrine ait tüm operasyonlar için rezerve edilecektir.

**İleri üretim çizelgeleme uygulamasını kullanan firmalar için kaynak bazında vardiya planı tanımlanabilir mi?**

Kaynak tanımlama ekranı üzerindeki “Vardiya Planı” sekmesi üzerinden kaynak bazında vardiya tanımlaması yapılabilmektedir.

**Bir kaynak için aynı anda birden fazla ürün işlemesi söz konusu ise nasıl bir tanımlama yapılmalıdır?**

Kaynak tanımlama ekranı üzerindeki “Ürün Eşleştirme” sekmesi üzerinden aynı anda hangi ürünlerin ilgili kalıptan çıkabileceğinin tanımlaması yapılabilir. Bu ürünler kalıptan aynı anda çıkıyorsa "Eşleşen tüm ürünlerin eş zamanlı çıkma zorunluluğu var" seçeneği işaretlenmelidir.

**Aynı kalıptan A ve B ürünü aynı anda çıkabilmekte bunun yanı sıra C ve D ürünü de çıkabilmektedir. Programa bu tanımlamayı nasıl yapabiliriz?**

Bir kalıp birden fazla şekilde kullanılabiliyorsa, bu ihtimaller ürün eşleştirme sekmesi üzerinde ayrı setler olarak tanımlanmalıdır. Örneğin 3 gözlü bir kalıp 2 adet A ürünü ve 1 adet B ürünü çıkarabildiği gibi, 3 adet C ürünü de çıkarabiliyor olsun. Bu durumda bu 2 farklı senaryo bu kalıp özelinde 2 farklı set olarak tanımlanmalıdır. Bu setlerden hangisine öncelik verileceği "Set Öncelik Sırası" alanından tanımlanabilir.

**Toplam ömür nasıl hesaplanmaktadır?**

Kaynak miktarı ile ömür sayısının çarpımı toplam ömrü vermektedir.

**Kaynak tipi stok seçildiğinde miktar alanı neden pasif gelmektedir?**

Stok tipli kaynaklar, stok hareketleriyle bütünleşik çalışmaktadır. Bu yüzden miktar sahası ilgili stokun bakiyesi olarak getirilmektedir. Örneğin stok için alış faturası girildiğinde kaynak hareketlerine de ömür artışı olarak yansımaktadır.

**Kaynak hareketlerini hangi ekranlar üzerinden girebiliriz?**

Üretim sonu kaydı, serbest üretim sonu kaydı ve üretim akış kaydı ekranları üzerinde kaynak kullanım girişleri yapılabilir. Ayrıca kaynak hareketleri ekranı üzerinden de manuel girişler yapılabilir.

**Makine bakım modülünde kaynaklar sekmesi gelmemektedir ne yapabilirim?**

İleri üretim planlama parametresi açık ve ilgili kaynak için kaynak tanımlama ekranında tamir edilebilir seçeneğinin işaretli olması gerekmektedir.

**Üretim sonu kaydı ekranında sağ menüde “Kullanılan Kaynak Girişi” yapamıyorum, neden?**

Üretim sonu kaydının fiş üret butonu ile kayıtlara geçilsin denildikten sonra kaynak girişi yapılabilir.

**Kalıp tanımlama ekranında göz sayısı tanımladım fakat bazen gözlerin bir kısmını kapatıp üretim yapabiliyoruz bu durumda ne yapılmalıdır?**

Kaynak girişi sırasında kalıp göz sayısı alanında anlık değişiklik yapılabilir. Ömür tüketimi bilgisi ise yeni göz sayısı üzerinden hesaplanacaktır.

**Kalıp için göz sayısı tanımlandı ise ömür tüketimi nasıl hesaplanmaktadır?**

Ömür tüketimi= Üretim miktarı/ kalıp göz sayısı

**Stok tipli kaynaklar için kullanımlar stok hareketlerine nasıl yansımaktadır?**

Kaynak kullanım girişinde girilen ömür miktarı/ Kaynak tanımı ekranındaki toplam ömür değeri ile bulunan miktar stok hareketlerine çıkış hareketi olarak yansımaktadır.

**Girilen ömür kullanımlarını nereden takip edebilirim?**

Üretim\\MRP\\Kayıt\\Kaynak Yönetimi\\ Kaynak Hareketleri menüsü üzerinden detaylı ve görsel olarak kaynak ömür takipleri yapılabilir, aynı zamanda Üretim\\MRP\\Raporlar\\Kaynak Hareketleri Raporu ile de tüm kaynaklara ait kaynak hareketleri raporu alınabilmektedir.

**Hangi operasyonda hangi kaynakların kullanılacağını nasıl tanımlayabilirim?**

Operasyon-Kaynak Eşleştirme Ekranı üzerinden ürün ve ürün grupları bazında operasyon kaynak eşleştirmeleri yapılabilmekte ve kullanılan kaynak girişi ekranına getirilmesi sağlanabilmektedir.

**Tamirdeki kaynakların girişi nereden yapılmalıdır?**

Üretim\\MRP\\Kayıt\\Kaynak Yönetimi\\ Kaynak Hareketleri menüsü üzerinden ilgili kaynak için kaynak hareketleri sekmesi üzerinden tamir hareket tipli giriş ve çıkış hareketleri yapılabilmektedir.

**Kaynak modülünün makine bakım modülü ile entegrasyonu mevcut mudur?**

Kaynakların ömür takibi sırasında bakım işlemlerini takip edebilmek için şu anda "Kaynak Hareketleri" ekranı üzerinden "Tamir" tipli hareket girilerek yönetim yapılabilir, hali hazırda "Makine Bakım \> Bakım Emri" üzerinden yapılan girişlerin ömür takibi üzerine etkisi yoktur, bunun desteği önümüzdeki versiyonlarda planlanmaktadır.

**Kaynak yönetimi için netopenx desteği mevcut mudur?**

Netopenx desteğimiz mevcuttur.

**Üretim kayıtlarında kullanılan kaynak bilgilerinin otomatik gelmesi sağlanabilir mi?**

Üretim parametreleri- Üretim 2 sekmesi altında “Üretim Kayıtlarında Kaynak Kullanımları Otomatik Atılsın” parametresi işaretli olması durumunda otomatik olarak kaynak girişleri ilgili belgelere yansımaktadır.

**Kullanılan kaynak girişi yapıyorum fakat veri tabanına kaydetmiyor, ne yapabilirim?**

Kullanılan kaynak giriş ekranında kaynaklar eklendikten sonra onayla butonuna basılması gerekir. Eğer tanımlı olan kaynakların ilgili belgelere doğrudan yansıtılıp onaylı getirilmesi istenir ise “Üretim Kayıtlarında Kaynak Kullanımları Otomatik Atılsın” parametresi işaretli olmalıdır.

**Operasyon- Kaynak eşleştirme ekranında birden fazla set tanımım mevcut ise bu setleri nasıl kullanabilirim?**

İlgili belgelerde kullanılan kaynak girişi yapılmak istenildiğinde set seçimi ile ilgili karşınıza bir ekran çıkacaktır ve istenilen setin seçimi yapılabilecektir. İstenir ise set seçimi yapmadan manuel kaynak girişi de mümkündür.

**Kaynak hareketleri ekranında hareket tipi tamir seçeneği neden gelmez?**

Kaynak tanımlama ekranında ömür takibi yapılsın parametresi ve tamir edilebilir seçeneğinin işaretli olması gerekmektedir.

**İleri üretim çizelgeleme uygulamasında kaynaklar nasıl dikkate alınabilir?**

Çizelgeleme modelleme aracı üzerindeki algoritma içerisinde yer alan “Kaynak Kullanım Politikası” seçimine göre kaynaklar dikkate alınmaktadır.

**İleri üretim çizelgelemede ömür takibi nasıl yapılmaktadır?**

Çizelgeleme tarafında kaynak ömrünü ve tahmini bakım işlemlerini dikkate alabilmek için "Algoritma Opsiyonları" kısmındaki "Ömrü Biten Kaynakların Bakımı Plansın" parametresi işaretlenebilir. Böylece “Kaynak Bakım Planı Raporu” üzerinden ömür takibi yapılabilmektedir. İlgili kaynağın kalan ömrü zaman ekseni boyunca kümülatif olarak yürütülmekte ve ömrü bittiğinde bakım süresi kadar bakıma gönderilmektedir.

**Personel tipli kaynaklarının personel paketi bağlantılı ise personelin izinli olması durumunda temelset paketi ile entegre çalışıyor mu?**

Personellerin izinli olması durumu ile entegre çalışmamaktadır. Durum alanı pasife çekilebilir.

**Kaynaklar için bakım talimatları tanımlanabilir mi?**

Kaynaklar için periyodik ya da durum bazlı bakım talimatları oluşturulabilir. Periyodik tanımlamalarla bakım planları oluşturulabileceği gibi durum bazlı bakım talimatları ile otomatik bakım talepleri oluşturulabilmektedir.

Bakım talimat şablonları ekranı üzerinden kaynaklar için durum bazlı bakım talimatı tanımlanabilir. Toplam üretim miktarı, toplam üretim süresi, son bakımdan itibaren geçen süre ve son bakımdan itibaren üretilen miktar olmak üzere 4 farklı durum bulunmaktadır. Ekranda ikinci bir durumun daha tanımlanmasına izin verilmektedir. Bir durum daha girilmesi gereken durumlarda, ilk durum satırının hemen altındaki alandan "ve" ya da "veya" operatörlerinden biri seçilerek ikinci duruma ait alanın aktifleşmesi sağlanmaktadır. Ardından aktifleşen ikinci durum alanı da ilk durum alanı gibi doldurulabilmektedir.
