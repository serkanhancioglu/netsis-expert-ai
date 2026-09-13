---
title: "Ek-3 (Maliyet Hesaplatma Öncesi Modüler Çalışmalar)"
page_id: "24752321"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Muhasebe"
  - "Maliyet Muhasebesi"
  - "Ekler / Maliyet Muhasebesi"
  - "Ek-3 (Maliyet Hesaplatma Öncesi Modüler Çalışmalar)"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Maliyet Muhasebesi / Ekler / Maliyet Muhasebesi / Ek-3 (Maliyet Hesaplatma Öncesi Modüler Çalışmalar)"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTI5Nzg1N2U1LTAxYmItNDU4Ni1hYTJmLWMyZTc2MDE4NDg3NCZsaW5rPTlkOGFlYTNkLTM5YWQtNGFjMi1hOTNhLTBmNjQxNjBjYjQzZCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=297857e5-01bb-4586-aa2f-c2e760184874&link=9d8aea3d-39ad-4ac2-a93a-0f64160cb43d&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ek-3-maliyet-hesaplatma-oncesi-moduler-calismalar_50678068_24752321.html"
source_version: "2022-12-02T15:12:50.960+03:00"
source_bytes: 295009
fetched_at: "2026-09-13T04:15:18+00:00"
generator: "netsis-scraper 1.0.0"
---
# Ek-3 (Maliyet Hesaplatma Öncesi Modüler Çalışmalar)

Maliyet hesaplatma öncesinde yapılması gereken işlemler şunlardır:

- Stok kodlarının tanımlanarak Maliyet Muhasebesi için Türü ve Maliyet Grup Kodları bilgisinin girilmesi gerekir.
- Maliyet Ana Mamul Kodları tanımlanarak ilgili hesap kodlarının maskeleme ve dağıtım anahtarları bilgisinin girilmesi gerekir.
- Maliyet Grup Kodları tanımlanarak, bu kodlara hesap planında açılan yansıtma kodlarının girilmesi gerekir.
- Üretim programından ürün bazında reçeteler hazırlanarak üretim aşaması durumuna gelinmesi gerekir.

**Üretim Sonu Kayıtları**

Bu bölüm, reçete kayıtları oluşturulmuş mamuller için üretim sonu kayıtlarını oluşturarak, günlük veya belli dönemler için stoklara işlenmesini sağlar. Bu işlemler; üretim yapıldıkça günlük, haftalık ya da aylık bazda şirket prensiplerine uygun zaman dilimleri için yapılır. Üretim sonu kayıtlarının raporunun alınması sonucu, mamullerle ilgili miktar ve tutar bazlı bilgilerin stoklara giriş hareketi, hammadde/yarı mamullerle ilgili miktar ve tutar bazlı bilgilerin stoklara çıkış hareketi olarak aktarıldığı görülür.

![](../../../../_assets/27bf319f5131548b278d.png)

Üretim Sonu Kaydı tamamlandıktan sonra, üretim sonu raporunun listelenmesinden önce ek sorgulama ekranı görüntülenir.

Raporun ekran/yazıcıdan alınacağını belirleyerek, “Kayıtlara Geçilsin” seçeneğinde, üretim sonu kaydının stok kayıtlarına işlenip işlenmemesi belirlenebilir. Deneme ve örnekleme için üretim sonu raporları düzenlenebilir. Bu kayıtların stoklara geçmemesi için bu seçeneğin işaretlenmemesi gerekir.

**Ambar Giriş/Çıkış Fişlerinden Sarfların Oluşturulması**

Fatura → Ambar Giriş ve Çıkış Fişi, maliyet muhasebesi işlemleriyle ilişkili olarak, üretim reçeteleri oluşturulamayan mamuller için hammadde, yarı mamul, sarf miktar ve tutarlarının kayıtlarının yapılacağı bölümdür. Hangi safha ile ilgili ise o safhanın üretim - yani, şube/depo koduna geçilerek - kayıtlarının yapılması gerekir. Kayıtlarda hareket türü olarak Üretim (C) seçilmesi gerekir.

**Örneğin;**

Maliyet Ana Grup Kodu olan 1.safha bölümünde H3’den YM2 üretilir. H3’ün üretim sonucunda ne kadar YM2 haline geleceğinin miktarsal oranları belirlenemediği ve bu yüzden üretim reçetesi tanımlanamadığı zaman, hammaddelerin sarf miktarları H3’den çıkıp YM1’e giriş olarak ambar giriş/çıkış fişi bölümünden, üretim seçeneği ile yapılması gerekir. H3’den çıkış yapılırken hareket türü maliyet ana grup kodu, maliyet grup kodu ya da stok kodu seçilebilir. H3’den çıkış yapılarak girişi yapılacak karşı hesap olarak stok kodu belirlenemiyosa, maliyet ana grup kodu ya da maliyet grup kodlarına giriş yapılması gerekir.

Bu bölümde önceden girilen fişleri tekrar çağırarak izleyebilir, düzenleyerek tekrar kaydedebilir ve kayıt sonlarında fiş basımları yapılabilir.

Fatura → Ambar Giriş/Çıkış Fişi ve Depolar Arası Transfer Fişi seçeneklerinde görüntülenecek olan ekranın Maliyet Muhasebesi kullananlar için açıklaması aşağıdaki şekildedir:

![](../../../../_assets/f535ae2b26d2472e8f47.png)

**Hareket Türü**

Maliyet muhasebesine bağlı sarf miktar ve tutarlarının aktarımı için hareket türü sorgulamasında, işlem sonucunda oluşturulacak stok hareket kayıtlarının, hareket tipinin (C)-Üretim olarak belirlenmesi gerekir. Stok → Maliyet Oluşturma işlemlerinde program, hareket tipleri üretim (C) olanları hesaplamaya alır.

Hareket tipleri hem raporlarda ayrı tipte hareketleri gruplandırmak açısından, hem de tiplerin ayrı ayrı icmallerinin alınması açısından önemlidir.

**Çıkış Yeri**

**Masraf Merkezi (M)**

Fatura → İşlemler bölümünden tanımlanan masraf merkezlerinde kayıt oluşturulması için tercih edilecek seçenektir. Fiş Numarası ve Masraf Merkezi Kodu girildikten sonra, ilgili mal kayıtlarının giriş/çıkış işlemlerine devam edilir. Stok kodunu kaydettikten sonra masraf merkezinin Muhasebe Kodu, açılan bir pencereden sizi bilgilendirir ve istenilirse buradan değiştirilebilir. Bu değişiklik sadece ilgili kayıt için geçerlidir. Masraf merkezinin Muhasebe Kodu değiştirilmez. Genel Muhasebe ve Maliyet Muhasebesi işlemlerinde Referans Kodu Uygulaması yapan firmalar Şube/Depo Sarf Çıkışlarını masraf merkezleri bazında kullanabilir.

**Stok Kodu (S)**

Sarf çıkışlarının üretimi yapılan stok kodundan çıkılması için kullanılacak seçenektir.

**Maliyet Ana Grubu (A)**

Maliyet Muhasebesi modülünü kullanan firmalar için, çıkış yeri belli olmayan - herhangi bir mamul koduna ait olmayan - fakat, maliyet ana grup koduna ait olan hammadde sarf miktarlarının çıkışları için kullanılacak seçenektir. Maliyet ana grup kayıtlarında “Hammadde sarfları ana grup bazında mı?” parametresi işaretlenmişse bu seçenek kullanılabilir. Maliyet Muhasebesi maliyet ana grubunda tanımlanan kodlar kullanılarak, hammadde sarf çıkışları için giriş/çıkış kayıtları oluşturulabilir. Ana Maliyet Grup karşılığında kayıtları oluşturulacak stok sabit kayıtlarının Ek Bilgiler sekmesi "Türü" alanı hammadde olarak tanımlanmamışsa, burada uyarı vererek giriş/çıkış işlemleri sistem tarafından engellenir.

**Maliyet Grubu (G)**

Maliyet Muhasebesi modülünü kullananlar için geçerli olan seçenektir. Maliyet Muhasebesi → Maliyet Grup Kodu bölümünden tanımlanan kodlar kullanılarak giriş/çıkış kayıtları oluşturulur.

**Serbest (F)**

Herhangi bir Giriş/Çıkış yeri belirtilmeden sadece "Tarih" alanına kayıt tarihi girilerek, stok kodlarına bu seçenek ile hareket kayıtları oluşturulur.

Bu ekrandan sonra ambar giriş/çıkış fişinin kaydedileceği ekrana ilerlenir.

Ambar Giriş/Çıkış Fişi Kaydı sırasında ekrana gelecek sahaların açıklamaları, Satış Faturaları bölümünde bahsedilen şekildedir. Bu sahalarla ilgili geniş açıklamalar Satış Faturası bölümünde yer alır.

Kaydedilmiş ambar giriş/çıkış fişleri, tekrar ekrana getirilip izlenebilir ve yanlış girilen bir fiş, ekrana fiş numarası verilerek getirilip iptal edilerek ya da üzerinde düzeltme yapılarak yeniden kaydedilebilir.

**Aylık Personel/ Demirbaş Entegrasyonu**

**Personel Bilgilerinin Entegrasyonu**

Personelle ilgili muhasebeleştirilecek bilgiler masraf merkezleri bazında toplanmıştır. Bu masraf merkezleri, Maliyet Muhasebesi'nde tanımlanan MALİYET GRUP KODLARI bazında düşünülerek oluşturulur.

Her bir muhasebe masraf merkezinin hangi hesap kodlarında muhasebeleştirileceği, Entegrasyon → Muhasebe Detay Kod Girişi bölümünden girilir. Personel Sabit Bilgilerinde de, her personel için hangi masraf merkezine dahil olduğu bilgisinin Detay Kodu alanında seçilmesi gerekir.

![](../../../../_assets/eb8f692349b341439d8d.png)

Tüm personel tek bir masraf merkezine işlenecekse, Detay Kodu sahalarına aynı kod yazılıp, bu kod için tanımlama yapılabilir. Bu bölümde ilk olarak, tanımlanacak masraf merkezi kodu girilir. Daha sonra bu masraf merkezine ait muhasebe hesap kodları tanımlanır. Kazanç ve yardımların brüt tutarları ile SSK işveren hissesi, tasarruf işveren katkısı, SGDP işveren hissesinin muhasebe hesap kodlarının girilmesi gerekir. Bu bölümde işlenen hesap kodları, maliyet hesapları olup, borçlandırılır. Netsis programı ile entegre çalışıldığı için Muhasebe Hesap Kodları girilirken muhasebe rehberinden faydalanılır.

**Personel Masraf Merkezi Tanımlama Örneği**

Aktarılacak olan bilgi sahasının karşısına aktarım yapılacak muhasebe hesap kodu, yevmiye fişine geçirilecek açıklama ve kümüle edilme gibi genel girişlerle birlikte bu bölümdeki kayıtlar tamamlanmış olmaktadır. Kümülasyon sahası ise bir masraf merkezi içinde tanımlanan hesap kodlarından aynı olanlarının tutarlarının kümüle edilmesiyle ilgilidir. Kümülasyonun işaretlenmediği durumda da aynı muhasebe hesap koduna ait olsa bile her girilen borç isminin mahsup fişinde ayrı satırlarda görülmesine yöneliktir. Aktarma işlemi Personel Programı/ Entegrasyon/ Muhasebe Aktar bölümünden yapılır.

Muhasebe Genel Kod girişi bölümde ise genel olarak, masraf merkezlerinden bağımsız, tek kalem muhasebeleştirilecek alacak hesaplarının tanımı yapılır. Parametrik olarak tanımlanabilen 24 adet kesinti tutarlarının ve bunlara ek olarak ödenecek SSK işçi, işveren, tasarruf işçi, işveren, gelir vergisi, damga vergisi, SGDP işçi, işveren tutarlarının muhasebe hesap kodları tanımlanabilir. Tanımlamalarda muhasebe hesap planı rehberi kullanılabilir. Bu bölümde işlenen hesap kodları , ödenecek toplam tutarları içerip, alacaklandırılır. Yuvarlama hesabı, diğerlerinden farklı olarak o ay borç/alacak bakiyesi vermesine göre işlem görür. Aktarılacak olan bilgi sahasının karşısına aktarım yapılacak muhasebe hesap kodu, yevmiye fişine geçirilecek açıklama ve kümüle edilme sorgusuna verilen yanıtla birlikte bu bölümdeki kayıtlar tamamlanır. Kümülasyon işaretlenirse, bir masraf merkezi içinde tanımlanan hesap kodlarından aynı olanlarının tutarlarının kümüle edilmesiyle ilgilidir. Kümülasyonun işaretlenmemesi durumunda aynı muhasebe hesap koduna ait olsa bile her girilen borç isminin mahsup fişinde ayrı satırlarda görülmesine yöneliktir.

**Personel Entegrasyon Mahsup Örneği**

Muhasebeye aktarma bölümü, istenen ayın personel mahsubunu oluşturur. Oluşan mahsup Entegrasyon Modülü/Dekont Mahsubu bölümünden izlenebilir. İlgili aktarım bilgileri kontrol edilerek Entegrasyon bölümünden de muhasebeye aktarım yapılması ve yevmiye fişi haline dönüştürülmesi gerekir.

**Amortisman Bilgilerinin Entegrasyonu**

Demirbaş entegrasyonu hazırlık çalışmaları ve aylık muhasebeleştirme işlemlerinin ayrıntılı açıklamaları Demirbaş paketinde yer alır.

**Demirbaş Sabit Kayıt Örneği**

Demirbaşlarla ilgili muhasebeleştirilecek bilgiler masraf merkezleri bazında toplanmıştır. Her bir demirbaş detay kodunun hangi muhasebe masraf merkezinde ve hangi hesap kodlarında muhasebeleştirileceği bilgisinin Demirbaş/Entegrasyon/Masraf Kodu Tanımlama bölümünden girilmesi gerekir. Masraf merkezlerinin MALİYET GRUP KODLARI'na göre belirlenmesi gerekir. Demirbaş paketinde Masraf Merkezleri oluşturulduktan sonra her demirbaş kaydı için Demirbaş Sabit Kayıtlarındaki detay kodlarına girilmesi gerekir.

**Örneğin;**

A firması için maliyet grup kodları; mamul-1 ve mamul-2 olarak tanımlanmış ve bu grup kodlarının ikinci ekranlarına maliyet masraf kodlarına göre amortisman hesaplarının maskelemeleri girilmişti. Bu durumda mamul-1 ve mamul-2 için masraf kodu tanımlaması oluşturularak, her birinin sabit kıymet, birikmiş amortisman ve masraf merkezleri tanımlamaları muhasebeye entegre olacak şekilde - hesap planı kodları - düzenlenmesi gerekir.

**Demirbaş Masraf Merkezi Tanımlama Örneği**

**![](../../../../_assets/561a6039cf73b40ed7d2.png)**

Detay kodunun masraf hesap kodları ve masraf dağıtım oranları yüzde bazında ilgili sahalarda belirlenir. Referans kodu mantığı ile çalışan firmalar aynı masraf merkezlerine ait oranlamaları aynı ya da değişik referans kodlarına entegre edebilirler. Detay kodu bazında kümüle olan toplam amortisman tutarı, tanımlı masraf hesap kodlarına ilgili oranlar bazında dağılarak aktarılır.

**Demirbaş Entegrasyonu Mahsup Örneği**

Aylık Hisse Muhasebeleştirme bölümü yardımıyla aylık bazda değerleme ile amortisman tutarları entegre edilebilir. Entegre edilecek ayın tarihi (gün/ay/yıl) girildiğinde, program otomatik olarak aylık amortisman tutarlarını Netsis programındaki Entegrasyon → Dekont Mahsubu bölümüne aktarır. Entegrasyon bölümünden de muhasebeye aktarım yapılması ve yevmiye fişi haline dönüştürülmesi gerekir.

**Genel Üretim/Yönetim Gider Dağılımları**

Yukarıda bahsedilen Personel ve Demirbaş Muhasebe Entegrasyonları sonucunda, direkt işçilik giderleri ve genel üretim giderlerinin işçilik ve amortisman payları dağıtıma hazır şekle getirilmiştir.

Yardımcı servis giderleri - yemekhane, atölye, kafeterya gibi - veya ay içinde dağıtılmayan genel üretim giderlerinin ürün merkezleri bazında dağılımı, anahtar sistemine göre Muhasebe → Yevmiye Fiş Girişi bölümünden mahsup fiş tipi ile oluşturularak tamamlanabilir. Ayrıca, Muhasebe → İşlemler → Yardımcı Servis Dağıtım İşlemleri bölümü kullanılarak da dağıtım gerçekleştirilebilir.

**Maliyet Bilgilerinin Dövizli Takibi**

Dövizli muhasebe uygulaması yapan firmalarda, maliyetlerin dövizli takibinin yapılabilmesi için bazı parametrelerin işaretlenmesi gerekir.

**Maliyet Hesaplatma Adımları**

**Stok Modülü/Döviz Fiyatları Oluşturma**

Dövizli Muhasebe uygulaması olan firmalar için, maliyet hesaplamalarından önce Stok Modülü/Döviz Fiyatları Oluşturma seçeneğinin çalıştırılması son derece önemlidir. Bunun nedeni, maliyet oluşturma adımında baz alınacak döviz tutarlarının, stok hareket kayıtlarındaki firma döviz tutarı sahasından alınmasıdır. Firma döviz tutarlarının oluşturulması da Stok Modülü/Döviz Fiyatları Oluşturma seçeneği ile yapılır.

**Stok Modülü/Maliyet Oluşturma**

Belli bir tarih aralığında, Aylık Ağırlıklı Ortalama/LIFO/FIFO maliyet yöntemi kullanılarak istenirse şubeler dahil tüm stok birim fiyatlarının hesaplanıp çıkış hareketlerinin güncellenmesini sağlar.

![](../../../../_assets/6d359b9cd1b60b87e6a7.png)

Bu bölümde, maliyet oluşturulacak tarih aralığının girilmesi gerekir. Bitiş tarihine maliyet çalıştırılan ayın son gününün girilmesi gerekir. Yıllık İşlem parametresi işaretlenmediğinde, başlangıç tarihine müdahale edilmez ve bu durumda program, seçilen maliyet tipine göre, bitiş tarihi sahasında belirtilen ayın, ilk gününden son gününe kadar aylık maliyet çalıştırır.

Yıllık İşlem seçeneği, yıl boyunca standart maliyet sistemini uygulayarak, yıl sonunda fiili maliyetleri hesaplatan ve standart-fiili farklarını bulan firmaların kullanacağı bir parametredir. Bu parametre ile bir yıllık hareketlerin tümü için tek bir maliyet fiyatı oluşur. Bu şekilde oluşan maliyet, aylık ağırlıklı ortalama yönteminde olduğu gibi hesaplanır. Yıllık standart maliyet sisteminin kullanılması için maliyet parametrelerinde “Yıllık Standart Maliyet” parametresinin işaretlenmesi gerekir.

Bu sorgulama ekranından sonra şubelerin de maliyet hesaplamalarına eklenmesi ile ilgili “Şubeler dahil edilecek mi” sorgu ekranı ile karşılaşılır. Maliyet ana grupları bazında üretim merkezleri olarak tanımlanan şube/depolar da buradaki maliyet hesaplamalarına mutlaka DAHİL edilmesi gerekir.

Örneğin;

Maliyet tipinin “Aylık Ağırlıklı Ortalama” seçilmesi durumunda, tarih aralığı olarak 01/08/2003 - 31/08/2003 verildiğinde; 01/08/2003 tarihine kadar devreden maliyet bulunup, 31/08/2003'e kadar aylık ağırlıklı ortalama yöntemi kullanılarak verilen tarih aralığındaki çıkış fiyatları düzenlenir.

Maliyet Oluşturma çalıştırılması sonucu, stok sabit kayıtlarındaki Ek Bilgiler sekmesinde yer alan Birim Maliyet ve Firma Döviz Maliyet - dövizli muhasebe kullananlarda - sahalarına burada seçilen maliyet yöntemi ile hesaplanan maliyet fiyatları aktarılır.

Buradaki işlemlerin bitiminde kontrol amacıyla, Stok → Ek Listeler → Ortalama Maliyet Stok Değerleri ve Merkez/Şube Envanter Raporları bölümünden listeleri alınabilir.

**Muhasebe Modülü /Döviz Tutarları Oluşturma**

Tüm işlemlerin tamamlanmasından sonra, dövizli muhasebe kullanan firmalarda, Maliyet Muhasebesi → Maliyet Oluşturma seçeneğinin çalıştırılmasından önce, Muhasebe → Döviz Tutarları Oluşturma bölümünin çalıştırılması gerekir. Böylece, masrafların birim maliyetlere yansıtılması sırasında firma döviz tutarlarının da bulunması sağlanır.

![](../../../../_assets/e9b2440175d915b067fc.png)

İlk olarak, Yardımcı Programlar → Şirket/Şube Parametre Tanımları bölümündeki “Döviz Uygulaması Var” parametresinin işaretlenmesi gerekir. Bu parametre, ilgili şirket/şube bazında döviz kullanımını sağlar. Yine bu bölümde, Döviz Çevrim Tipi ve Firma Döviz Tipi'nin belirlenmesi gerekir. Burada belirlenecek firma döviz tipi, maliyet hesaplamasında baz alınacak döviz tipidir.

İkinci olarak, Muhasebe Parametreleri → Döviz Muhasebe → FAS52 seçeneğinin işaretlenmesi gerekir.
