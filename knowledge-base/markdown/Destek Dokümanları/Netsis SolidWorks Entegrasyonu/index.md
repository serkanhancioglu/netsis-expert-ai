---
title: "Netsis SolidWorks Entegrasyonu"
page_id: "66237155"
product: "netsis-3-enterprise"
depth: 2
is_section: true
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis SolidWorks Entegrasyonu"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis SolidWorks Entegrasyonu"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWVmMWM5OGZjLWQzMjYtNGQyYi1hYjU3LWU1NmRmNTk3NzhmNyZsaW5rPThlM2NjNzVmLTk5ZTMtNDE2MS1iOTg1LTdkYzM1ZmJiZDcwNSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=ef1c98fc-d326-4d2b-ab57-e56df59778f7&link=8e3cc75f-99e3-4161-b985-7dc35fbbd705&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-solidworks-entegrasyonu_80089852_66237155.html"
source_version: "2022-11-02T15:59:19.957+03:00"
source_bytes: 4123343
fetched_at: "2026-09-13T04:25:01+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis SolidWorks Entegrasyonu

Netsis SolidWorks Entegrasyonu ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

> [!TIP]
> İlgili özelliğin anlatımını içeren webinar kaydına ulaşmak için [tıklayınız.](https://register.gotowebinar.com/recording/5004405582567795979)

Üretim yapan tesislerin belirli bir son ürünü üretebilmeleri için tüketmeleri gereken bileşenler ile bu bileşenlerin tüketim miktarlarını içeren ürün reçeteleri, Logo Netsis ERP çözümleri üzerinde çeşitli şekillerde yönetilebilmektedir. Sistem üzerinde reçete yönetimi konusu her ne kadar esnek ve kolay şekilde ele alınabiliyor olsa da işletmelerin yeni ürünler tasarlamak için kullandıkları sistem dışı farklı programlar da bulunmaktadır. Üretim sektöründe yeni ürün tasarım süreçlerinin özellikle Solidworks programı kullanılarak yürütülüyor olması, Solidworks ile Logo Netsis arasında bir entegrasyon kurarak kullanıcıların iş yüklerini azaltma fikrini doğurmuştur. Bu fikirden yola çıkarak desteklenen Logo Netsis ERP & Solidworks entegrasyonu sayesinde, Solidworks üzerinde tasarlanan ürün reçetelerinin erp çözümüne kolay ve hızlı bir şekilde aktarımı mümkün olmaktadır.

Logo Netsis ERP & Solidworks entegrasyonu, ürün konfigüratörünün desteklendiği Logo Netsis 3 Standard, Logo Netsis Wings, Logo Netsis 3 Enterprise ve Logo Netsis Wings Enterprise çözümleriyle kullanılabilmektedir. Bu dokümanda, bahsedilen entegrasyonun kullanım detayları anlatılmaktadır.

#### Logo Netsis ERP & Solidworks Entegrasyon Kurulumu

![](../../_assets/5af7db37ca2e90ada69d.png)**Ekran** **Görüntüsü** **1**

Logo Netsis ERP & Solidworks entegrasyonunun kullanılabilmesi için öncelikle bir kurulum işlemi yapılması gerekmektedir. Oldukça kolay yapılabilen bu kurulum için Logo Netsis ERP Servis klasörünün altında bulunan RegKontrol.exe programı, sağ tık menüsü içindeki "Yönetici olarak çalıştır" komutuyla çalıştırılmalıdır. (Bkz. Ekran Görüntüsü 1)

Bu şekilde çalıştırılan RegKontrol.exe, gerekli tüm kayıt işlemlerini gerçekleştirecektir. RegKontrol.exe çalışmayı tamamladığında açılacak olan "Kurulum Log Kayıtlarını İzleme Ekranı"nın detay sütununda LogoBOMExtractor.dll görülmelidir. Ardından Solidworks açıldığında, bu eklentinin de yüklendiği görülecektir. (Bkz. Ekran Görüntüsü 2)

![](../../_assets/7e142a299218387a75ed.png)**Ekran** **Görüntüsü** **2**

Eklentinin yüklü ve çalışır durumda olduğunu kontrol etmek için Solidworks içindeki "Eklentiler" menüsü kullanılmalıdır. Menü içinde yer alan "Diğer Eklentiler" alanında "Logo BOM Extractor" görülecektir. İdeal koşullarda RegKontrol.exe tarafından bu eklenti seçili duruma getirilecektir ancak aksi bir durum olması halinde, seçim manuel olarak da yapılabilmektedir. (Bkz. Ekran Görüntüsü 3)

Bu işlemlerin sonunda Solidworks açılırken hata mesajı alınması durumunda, Solidworks.exe de yönetici olarak çalıştırılarak başlatılmalıdır.

![](../../_assets/04c83199f8a488f82331.png)![](../../_assets/ff640585f63dcc86fd32.png)**Ekran** **Görüntüsü** **3 ve 4**

Kurulum işleminin tamamlanması sonrasında ise hangi bağlantı tipi kullanılacağı seçilmeli ve bağlantı ayarları yapılmalıdır. Solidworks entegrasyonu kapsamında NetOpenX ve REST olmak üzere 2 farklı bağlantı tipi desteklenmektedir.

NetOpenX ile bağlantı yapılmak istendiğinde bağlantı "Logo Netsis ERP (NetOpenX)" olarak seçilmelidir. Bağlantı portu varsayılan olarak "9090"dır. Ancak bu port bir sebeple kullanılamıyorsa, belirlenecek farklı bir port da kullanılabilir. Veri tabanı tipi de kullanıma uygun olarak seçildikten sonra entegrasyonun kullanılacağı veri tabanı adı, şube kodu, Netsis kullanıcı adı ve şifresi de girilmelidir.

![](../../_assets/e361f50578ba33a0cf33.png)**Ekran** **Görüntüsü** **5**

Bağlantı tipinin REST seçildiği durumda ise genel ayarlar altında bulunan "REST Servisi URL" alanına REST servisinin yayın yaptığı sunucunun adresi girilmelidir. Ayrıca veri tabanı kullanıcı adı ile şifresi de girilmelidir. Geri kalan veri tabanı tipi ve adı, şube kodu, Logo Netsis ERP kullanıcı adı ve şifresi gibi bilgiler entegrasyonun kullanımına uygun şekilde girilmelidir. (Bkz. Ekran Görüntüsü 5)

Gerekli bilgi girişleri ve seçimler yapıldıktan sonra ilgili alanın sağ alt köşesindeki "Kaydet" tuşuna basılmalıdır. Bu şekilde bilgilerin kaydı yapıldıktan sonra açılacak ekrandaki bilgiler kontrol edilmeli ve şifre girilerek "Giriş" butonuna basılmalıdır.

#### Ürün Reçetesi Aktarımı

Birinci bölümde anlatılan kurulum ayarlarının tamamlanmasından sonra, Solidworks ve Logo Netsis ERP arasındaki entegrasyon sağlanmış olacaktır ve Solidworks üzerinde tasarlanan bir ürünün reçetesi Netsis'e aktarılabilecektir. Bunun için tasarım ekranında ilgili ürün son haline getirildikten sonra 6. ekran görüntüsünde yeşil kutucuk içinde gösterilen "Reçete Getir" butonuna tıklanmalıdır. Bu işlem yapıldığında yine 6. ekran görüntüsünde kırmızı kutucuk içinde görüntülenebileceği gibi tasarıma ait reçete, tüm seviyeleriyle Logo BOM Extractor eklentisinin reçete alanında görüntülenecektir.

![](../../_assets/b9ac49daef8e94530425.png)**Ekran** **Görüntüsü** **6**

Reçetenin kontrolü ve doğruluğundan emin olunması sonrasında, Logo Netsis ERP ürün konfigüratörü aktarımını sağlamak için 6. ekran görüntüsünde mavi kutucuk içinde gösterilen "Kaydet" butonuna basılmalıdır. Butona basıldığında reçeteyi aktarmak için bir onay bildirimi görüntülenecektir. Bu ekranda "Evet"e basılması durumunda reçete ürün konfigüratörüne aktarılacak ve hangi taslak numarasıyla kaydın gerçekleştiğine dair bir uyarı görüntülenecektir. (Bkz. Ekran Görüntüsü 7)

![](../../_assets/0e3c0b49d6adfe5d2fae.png)**Ekran** **Görüntüsü** **7**

Ekran görüntüsü 7'deki örnekte belirtilen 17 numaralı taslak reçete, ürün konfigüratöründe açıldığında reçetenin aynen kullanılan ERP çözümüne aktarılmış olduğu görülecektir. (Bkz. Ekran Görüntüsü 8)

![](../../_assets/76bb4ddc0be482cfedbf.png)**Ekran** **Görüntüsü** **8**

Ürün konfigüratörü üzerinde kayıtlı olan bu taslak üzerinde değişiklikler yapmak mümkündür. ERP çözümüne Solidworks'ten aktarılan bir ürün reçetesi ile, konfigüratör üzerinde sıfırdan oluşturulmuş bir ürün reçetesi arasında, ürün konfigüratörünün kullanımı açısından bir farklılık yoktur. Ürün konfigüratörünün tüm özellikleri entegrasyon ile aktarılmış reçeteler için de kullanılabilir durumdadır. Ürüne ait reçetenin Logo Netsis ERP'de geçerli olabilmesi için ise varsa gerekli tüm değişiklikler taslak üzerinde yapıldıktan sonra, ilgili taslak onaylanmalıdır. Böylece sistemde bulunmayan stok kartları açılacak ve reçete sisteme alınmış olacaktır.

Solidworks'te tasarımı yapılan ürüne ait stok kartları halihazırda ERP üzerinde varsa ve yeni ürünün bileşenleri bu stok kartlarıyla eşleştirilmek istenirse, Logo BOM Extractor eklentisinin stok kodu alanının hemen yanında bulunan "…" butonu kullanılmalıdır. Bu butona tıklandığında Netsis stok rehberi açılacak ve rehberden seçim yapılmasına izin verilecektir. (Bkz. Ekran Görüntüsü 9) Stok rehberinden bir seçim yapıldığı takdirde artık ilgili bileşen ile Netsis'teki ilgili stok kartı eşleşmiş olacaktır.

Yukarıda anlatıldığı gibi bir eşleştirme yapıldıktan sonra, ilgili ürün reçetesi ERP çözümüne aktarılırsa stok kodları otomatik olarak kontrol edilecektir. Eşleştirmesi yapılan bir stok kodunun halihazırda kullanılan ERP çözümü üzerinde bir reçetesi varsa, aktarılan taslak onaylandığı anda bu stok koduna ait reçete de güncellenecektir. Bu yüzden reçete aktarımları sırasında stok kartı eşleştirmeleri yapılırken, mevcut ürün reçetelerinin değiştirilmemesi için dikkatli olunmalıdır.

![](../../_assets/f23ad16c2438f4eb005a.png)**Ekran** **Görüntüsü** **9**

Ayrıca Logo BOM Extractor eklentisinin reçete alanında sağ tık desteği bulunmaktadır. Sağ tık menüsü içinde reçete görünümünü düzenlemek üzere kullanılan "Tüm Kırılımları Aç" ve "Tüm Kırılımları Kapat" seçenekleri bulunmaktadır. Bunun dışında yarı mamuller üzerinde sağ tık menüsü açıldığında görüntülenecek olan "Bileşenin Altındakileri Gönderme" seçimi yapılması durumunda, ilgili yarı mamul tekil bir bileşen gibi işlem görecektir. Ek olarak ilgili yarı mamulün altındaki bileşenler pasifleşecek ve aktarılmayacaktır. (Bkz. Ekran Görüntüsü 10)

![](../../_assets/6202abb6395f4d2089bb.png)![](../../_assets/0b7bfe6fb2ca8c6e6171.png)**Ekran** **Görüntüsü** **10**

#### Özel Özellik Ayarları

Logo Netsis ERP ile Solidworks arasında kurulan entegrasyon fonksiyonlarının belirli özellikleri kontrol edilebilmektedir. Genel anlamıyla bu kontrol edilebilir özelliklere, "Özel Özellik" denilmektedir. Dokümanın 2. bölümünde anlatılan Solidworks bileşeni ile stok kartı eşleştirmesi de kontrol edilebilen özelliklerdendir. İstenilmesi halinde bu eşleştirme engellenebilir. Logo BOM Extractor eklentisinin "Özel Özellik Ekleme" fonksiyonunun "Alan" bölümüne bakıldığında hangi bileşen özelliklerinin ERP çözümü ile entegrasyonunun yapılabildiği ve dolayısıyla hangi özelliklerin Solidworks üzerinden kontrol edilebildiği görülecektir. (Bkz. Ekran Görüntüsü 11)

![](../../_assets/d2c484ae74e79d7baa05.png)![](../../_assets/acffd91948642a80cb61.png)**Ekran** **Görüntüsü 11**

Ekran görüntüsünde görüldüğü gibi "Stok Kodu" alanı, kontrol edilebilir bir özelliktir. Ekran görüntüsünde yeşil kutucuk içinde gösterilen "Değiştirilebilsin" parametresi işaretlenip "Güncelle" butonuna tıklanır ve ardından mavi kutucuk içinde gösterilen "Kaydet" butonuna basılırsa, stok kodu alanı dokümanın 2. bölümünde bahsedildiği şekilde değiştirilebilecek ve Netsis stok kartlarıyla eşleştirilebilecektir. Aynı işlem "Alan" menüsünde gösterilen tüm veriler için yapılabilmektedir.

Ayrıca yapılan eşleştirmeler yalnızca içinde bulunulan tasarıma ait olmayacaktır. Eşleştirmesi yapılan Solidworks bileşeni, farklı tasarımlar içinde de kullanılıyorsa "Reçete Getir" butonuna tıklandığında tüm değiştirilmiş stok kodları kontrol edilecek ve tasarım içindeki bileşenler kayıtlı eşleştirmelere göre güncellenecektir.

Yapılan stok kodu eşleşmesini eski haline getirebilmek de mümkündür. Bunun için eşleştirme yapılan bileşen üzerinde sağ tık menüsü açılmalı ve "Değiştirilmiş Stok Kodları Listesi" seçeneği seçilmelidir. (Bkz. Ekran Görüntüsü 12)

![](../../_assets/1c16ca98d72ee800b2ea.png)![](../../_assets/c5be674a69774b411437.png)**Ekran** **Görüntüsü** **12**

İlgili seçim yapıldığında o ana kadar uygulanan stok kodu değişiklikleri bir liste halinde görüntülenecek ve istenen değişiklik, ilgili satırın sonundaki "Sil" butonu kullanılarak değişiklik öncesi haline getirilebilecektir.

1. ekran görüntüsünde stok kodu alanının hemen altında görülen "Solidworks Ölçü Birim" alanı ise yine değiştirilebilir bir alandır. Solidworks ölçü birimi değiştirildikçe "Logo Netsis ERP'ye Aktarılacak Miktar" verisi de otomatik olarak değişecektir. Bu alanlar Solidworks üzerinde yapılan tasarımda kullanılan malzemenin cinsine göre Solidworks tarafından otomatik olarak hesaplanmaktadır. Örneğin bu dokümanda gösterilen vidanın malzemesi çelik olarak atandığındaki kütlesi ile bakır olarak atandığındaki kütlesi farklı olacaktır. Solidworks'un kendi içinde yaptığı bu hesaplama kullanılarak, aktarım yapılmaktadır. (Bkz. Ekran Görüntüsü 13)

![](../../_assets/8494700603e10715ee69.png)![](../../_assets/ea99fbb99ccf7048d92f.png)![](../../_assets/1407a786babff6d64bfd.png)**Ekran** **Görüntüsü** **13**

Logo BOM Extractor eklentisinin ayarlar menüsü altında bulunan "Parametreler" bölümü içinde bazı seçenekler bulunmaktadır. (Bkz. Ekran Görüntüsü 14)

![](../../_assets/4cf63cfcc005bc0d83fb.png)**Ekran** **Görüntüsü** **14**

Bu bölümdeki ilk parametre olan "Gizli bileşenler ürün ağacına getirilsin" seçimi, Solidworks içinde gizlenen bileşenlerin ürün ağacında gösterilip gösterilmeyeceğini kontrol edebilmek amacıyla kullanılmaktadır.

![](../../_assets/172d5d0d0a5433d14296.png)![](../../_assets/767ea6cbd92c7a7a20fb.png)**Ekran** **Görüntüsü 15**

İkinci parametre olan "Ham maddeler yarı mamul olarak aktarılsın" seçimi yapıldığında, ilgili bileşen yarı mamul yapılacak ve bu bileşenin ham maddesi de yarı mamul altında bir bileşen olacak şekilde düzenlenecektir. (Bkz. Ekran Görüntüsü 15)

Bir diğer parametre olan "Gösterilecek Bilgi" parametresi içinde "Stok Adı", "Stok Kodu" ve "Stok Kodu-Stok Adı" seçimleri mevcuttur. Bu alandan yapılacak seçime göre Logo BOM Extractor eklentisinin ürün ağacı bölümünde yer alan bileşenlerin hangi bilgilerinin görüntüleneceği belirlenmektedir. (Bkz. Ekran Görüntüsü 16)

![](../../_assets/04059429a0ac138aa3eb.png)![](../../_assets/a7dc77088c76c5cfe2da.png)![](../../_assets/a4fb1f2138ce7d8876a0.png)![](../../_assets/4ae159f281541f7bd6a8.png)**Ekran** **Görüntüsü** **16**

"Log kaydı tutulsun" parametresi işaretlendiğinde ise eklentinin sol alt köşesinde "Log Kayıtları" butonu oluşacaktır. Bu butona tıklandığında eklenti kullanılarak yapılan işlemlerin log kayıtları, tarih ve saat bilgisiyle gösterilecektir.

Son parametre olan "Mamul resmi aktarılsın" seçimi yapıldığında ise, Solidworks üzerinde oluşturulup ERP'ye aktarılan ürünün stok kartı içine ürün görseli de aktarılacaktır. (Bkz. Ekran Görüntüsü 17)

![](../../_assets/2c6de3d85f99bcc87b13.png)**Ekran** **Görüntüsü** **17**

Bahsi geçen bu parametre ayarlarının haricinde istenen özel özelliklerin oluşturularak ürün tasarımlarına eklenmesi de mümkündür. Bunun için Property Tab Builder kullanılması gerekmektedir. İlgili ekranın açılabilmesi için Solidworks kurulum klasörlerinin altında bulunan PropertyTabBuilder.exe programı çalıştırılabilir ya da "Solidworks Kaynaklar" menüsünün altında bulunan "Özellik Sekmesi Oluşturucu" yolu kullanılabilir. (Bkz. Ekran Görüntüsü 18)

![](../../_assets/16a85fd35ff3f99f6ad7.png)**Ekran** **Görüntüsü 18**

Solidworks'ün kendi fonksiyonu olan bu özellik sekmesi oluşturucu kullanılarak, tasarlanan ürünün tamamına ya da sadece seçilen bileşenlerine istenen özellikler eklenebilmektedir. Özellik sekmesi oluşturucu 3 alandan oluşmaktadır, ekran 3 sütuna bölünmüş gibi düşünülebilir. İlk sütun, desteklenen özel özellikleri içermektedir ve bu sütundan seçilecek özellikler ikinci sütun olan "Custom Properties" alanına sürükle-bırak yöntemiyle taşınabilmektedir. Özellik sekmesi oluşturucu tarafından Groupbox, Textbox, List, Number, Checkbox, Radio ve Listgroup özellikleri desteklenmektedir. Bu özelliklerden istenenler farenin sol tuşu ile tutulup sürüklenerek ikinci sütuna bırakılabilir. "Custom Properties" sütununda da aynı sürükle-bırak fonksiyonu kullanılarak, eklenen özelliklerin yerlerinin değiştirilmesi, ilgili sütunun istenen şekilde tasarlanması mümkündür. (Bkz. Ekran Görüntüsü 19)

![](../../_assets/7b017f5fd68dfafb08a3.png)**Ekran** **Görüntüsü** **19**

Ekranın "Custom Properties" alanına sürüklenen her özelliğe ait detaylar ise "Control Attributes" sütununda tanımlanmaktadır. Örneğin bir groupbox, bir checkbox ve bir textbox'tan oluşan bir örnek özellik kümesi 20. ekran görüntüsünde görülmektedir. Eklenen özelliklere ait bazı ayarların yapıldığı örnekte, groupbox başlığının "Ürün Bilgileri" olarak değiştirildiği görülmektedir.

![](../../_assets/474fe3d0d4515a844680.png)**Ekran** **Görüntüsü** **20**

Özellik sekmesi üzerinden oluşturulan bu taslaklar istenilmesi halinde kaydedilerek kullanılabilir duruma getirilmektedir. Kaydetme işlemi yapılırken dosya uzantısı ".asmprp" olarak seçilirse, özel özellik kümesi "assembly" tipli bileşenler için kullanılabilir olacaktır. Benzer şekilde dosya uzantısı ".prtprp" olarak seçilirse "part" tipli bileşenler için kullanılabilir olacaktır. Aynı uzantıda birden fazla özel özellik dosyası kaydedilmesi halinde, bileşenlere özel özelliklerin tanımlanırken "Özel Özellikler" sekmesinden bir liste görüntülenecek ve buradan istenen dosya seçilerek açılabilecektir.

Solidworks'ün kendi desteği olan özel özellik yaratma fonksiyonu, Logo Netsis ERP tarafında kısmen desteklenmiştir. Daha önce anlatılan "Özel Özellik Ekleme" fonksiyonunun "Alan" bölümünde yer alan sıra numarası, stok kodu, stok adı, yapılandırma kodu ve bileşen açıklama bilgileri, Solidworks entegrasyonu kapsamında desteklenen verilerdir. Bunların dışındaki bilgiler ERP çözümüne aktarılamamaktadır.

![](../../_assets/94f2eb3a7a005c8d559f.png)**Ekran** **Görüntüsü** **21**

Bahsedilenlere örnek olarak "Alan" bölümünde yer alan stok adı özelliği için, entegrasyon kurulmak istenirse öncelikle stok adının girişinin yapılabileceği bir textbox içeren özel özellik dosyası oluşturulmalıdır.

21. ekran görüntüsünde detayları gösterilen "Stok Adı" textbox'ı, "Stok Özellikleri" groupbox'ı içine yerleştirilmiş ve "StokAdi" ismi verilmiştir. Bu dosya reçetedeki bileşenler için kullanılmak üzere "template2.prtprp" uzantısıyla kaydedilmiştir.

Bu kayıt işleminden sonra dosyayı açabilmek için örnek olarak "bolt" bileşeni seçilip, özel özellikler sekmesi açılmıştır. Sistemde parça tipli bileşenler için birden çok dosya kayıtlı olduğundan seçim yapabilmek üzere bir liste görüntülenmiştir ve buradan istenen dosya seçilerek "Uygula" butonuna basılmıştır. (Bkz. Ekran Görüntüsü 22)

![](../../_assets/882c73762ad8cb58f0eb.png)**Ekran** **Görüntüsü** **22**

Bu işlemler sonrasında, Logo BOM Extractor eklentisinin ayarlar menüsü içindeki "Özel Özellik Ekleme" bölümünden "Alan" seçimi yapılıp "Ekle" butonuna basılmalıdır. Bu işlem yapıldığında "Özel Özellik Eşleştirme" bölümüne yapılan seçim gelecektir. Ardından özellik sekmesi oluşturucu uygulamasında ilgili özel özelliğin "Name" alanına girilen değer, "Özel Özellik Eşleştirme" bölümünde ilgili alana yazılmalıdır ve "Kaydet" butonuna basılmalıdır. (Bkz. Ekran Görüntüsü 23)

![](../../_assets/c72ca764710e7bb954f7.png)![](../../_assets/64cf107e54bddab9d6a4.png)**Ekran Görüntüsü 23**

Bu işlemler sonrasında, işlem yapılan "Alan'a ait değerler "Özel Özellikler" sekmesi üzerinden elle girilebilecektir ve Logo BOM Extractor eklentisinde "Reçete Getir" butonuna tıklandığında, ilgili alan manuel girilen bu değere güncellenecektir. Solidworks'ten Netsis'e gönderilen reçetelerle aktarılan değerler de manuel girilen bu değerler olacaktır. (Bkz. Ekran Görüntüsü 24)

![](../../_assets/778f0a51808002807617.png)![](../../_assets/cfce657f2a34a77928e2.png) ![](../../_assets/5c2d7ae7473b2bf5a0bd.png)**Ekran Görüntüsü 24**

Özel özellik eşleştirmesi her bileşen için yapılmak zorunda değildir. Eşleştirmesi yapılan bileşen ve alanlar için, yapılan eşleştirmeye göre değerler getirilirken, eşleştirme yapılmayan bileşenlere ait değerler Solidworks'ten direkt gelen değerler olacaktır.

Ayrıca özel özellik ekleme bölümünde yer alan "Ekranda görünsün" ve "Değiştirilebilsin" parametreleri kullanılarak, seçilen "Alan'ın Logo BOM Extractor eklentisinde görülüp görülmeyeceği ve görülüyorsa ilgili alanın eklenti üzerinden değiştirilebilip değiştirilemeyeceği kontrol edilebilmektedir.
