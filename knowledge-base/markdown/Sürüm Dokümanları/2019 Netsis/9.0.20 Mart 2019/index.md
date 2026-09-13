---
title: "9.0.20 Mart 2019"
page_id: "34220755"
product: "netsis-3-enterprise"
depth: 3
is_section: true
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Sürüm Dokümanları"
  - "2019 Netsis"
  - "9.0.20 Mart 2019"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Sürüm Dokümanları / 2019 Netsis / 9.0.20 Mart 2019"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTMzNDY5ZTEzLTQ4MTAtNDNiNy1hMTQwLTQ2MTJmNTJiNzVlZSZsaW5rPWI4MTcwNjcxLWFkNDgtNGFhNC05YjVjLWViNjY0NTYxNmE1NyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=33469e13-4810-43b7-a140-4612f52b75ee&link=b8170671-ad48-4aa4-9b5c-eb6645616a57&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "9-0-20-mart-2019_47073073_34220755.html"
source_version: "2019-12-04T08:51:37.953+03:00"
source_bytes: 29086
fetched_at: "2026-09-13T04:28:33+00:00"
generator: "netsis-scraper 1.0.0"
---
# 9.0.20 Mart 2019

**Genel**

- Demirbaş uygulaması için Akıllı Kod desteklendi. Temelset'teki gibi Ekstra menüsünün altından istenilen tasarım yapılabilir.

- Yardımcı Programlar\\Kayıt altına “View Hak Kısıtları” ekranı eklendi. Bu ekrana yapılacak tanımlamalar ile, serbest rapor menüsünden alınan raporlarda kullanılması istenmeyen viewler; şirket, şube ve kullanıcı bazında kısıtlanabilir. Saklanmış bir NRP uzantılı rapor dosyasının kullandığı bir view için kısıtlama yapılırsa, kullanıcı ilgili view'den rapor çekemeyeceği için, kayıtlı NRP raporunu da alamayacaktır.

- Merkezi Kimlik Yönetimi - Döviz İşlemleri menüsü altına "Kur Kopyalama" yetkisi eklendi.

- Netsis'e 1 kullanıcı ile 2 farklı bilgisayardan giriş yapılamıyordu. Netsis'e 2. bilgisayardan giriş yapılması durumunda kullanıcının diğer bilgisayardaki oturumu sonlandırabilmesi sağlandı.

- Şirket kopyalama ekranında veritabanı yedeği için başka dizin kullan' parametresi seçili olduğunda yedeklemenin yapılacağı path alanı eklendi.

- NDI ekranları için de özel yardım dosya desteği getirildi.

- Excel dosyasından sürükle bırak özelliği ile hızlı veri aktarımı ve güncellemesi işlemi desteklendi. Bu özelliğin desteklendiği ekranlar; Stok Kartı Kayıtları, Cari Kartı Kayıtları, Muhasebe Hesap Planı, Müşteri ve Satıcı siparişi için kalem bilgileri aktarımı. Bu özelliğin kullanılabilmesi için ilgili bilgisayara “AccessDatabaseEngine.exe” yüklenmelidir.(Utilities klasörü altından bu dosyaya erişilebilir)

- Log modülüne “SSO Log Raporu” eklendi. Raporda SSO (Merkezi Kimlik Yönetimi) kullanıcısı ekleme, silme, SSO’ya giriş ve çıkış yapan kullanıcılar listelenebilmektedir. Ayrıca Log Parametreleri’ne eklenen “Kullanıcı Oturum İşlemleri Log Kayıtları Tutulsun” seçeneği işaretlendiğinde, Netsis programına giriş ve çıkış yapan kullanıcıların da logunun tutulması ve Log Raporu’nda listelenmesi desteklendi.

**Fatura Modülü**

- E-Fatura ve e-irsaliye fatura bazında giden kutusunda şahıs firmaları için T.C. kimlik numarasının gösterilmesi sağlandı.

- Satış parametreleri, fatura ek 1 sekmesine "Ambalaj Uygulaması" seçeneği eklendi. Uygulamayı kullanılırken stok kodunun stok kartında istenilen alfa sayısal kullanıcı tanımlı sahasına "P" yazılır. Satış parametrelerinde ambalaj uygulaması seçeneği işaretlendikten sonra kullanılacak stok kodu sahası alanında stok kartında tanımladığımız sahası seçilir. Satış faturasında bu stoğu kullandığımız zaman bu stok için artık iskontodan muaf tutulacaktır.

- Toplu e-fatura oluşturmada ihracat e-fatura oluşturulurken çeki listesi uyarısının hangi sıra numaralı çeki listesi veya kalemi için geldiğinin yazılması sağlandı.

- E-fatura parametrelerine eklenen "Cari etiket bilgisi seçilebilsin" seçeneği ile cariye ait birden fazla etiket varsa e-fatura zarf gönderme aşamasında "Cari Etiket Seçimi" ekranının açılması ve faturanın bu ekrandan seçilen etiket bilgisi ile gönderilmesi sağlandı.

- Kamu idarelerine e-fatura gönderimi desteklendi. 6110368859 nolu VKN'ye sahip olan Maliye Bakanlığı Muhasebat Genel Müdürlüğü'ne e-fatura gönderimi yapılırken Sınıflandırma Kodu, Menşei ve Banka Bilgisi belirtilmesi zorunludur. Bu bilgilerin e-faturaya ilave olarak eklenmesi, e-fatura dizaynı aracılığı ile desteklenmiştir. Dizaynda, Sınıflandırma Kodu için "InvoiceLine-CommondityClassification, InvoiceLine-CommondityClassification-ListName, InvoiceLine-CommondityClassification-ListVersionId" ; Menşei için "InvoiceLine-OriginCountry-IdentificationCode, InvoiceLine-OriginCountry-Name" ve Banka Bilgisi için de "PaymentMeans-PaymentMeansCode, PaymentMeans-PayeeFinancialAccount-ID, PaymentMeans-PayeeFinancialAccount-CurrencyCode, PaymentMeans-PayeeFinancialAccount-PaymentNote" etiketleri kullanılmalıdır. Detaylı bilgi için: [http://www.efatura.gov.tr/dosyalar/kilavuzlar/Kamu_e-Fatura_Teknik_Kilavuzu.pdf](http://www.efatura.gov.tr/dosyalar/kilavuzlar/Kamu_e-Fatura_Teknik_Kilavuzu.pdf)

- Satış ve alış parametreleri fatura sipariş sekmesine "Sipariş Bağlantılı İrsaliye/Faturada Sipariş Kapama Açılsın" seçeneği eklendi. Bu seçenek işaretlendiğinde girilen irsaliye veya fatura belgesi sipariş bağlantılıysa, belge tamamlanırken "Sipariş Açma/Kapama" ekranının açılması sağlandı. Bu ekranda kullanıcı gridde kalan miktar alanına filtre vererek siparişin kapandığını kontrol edip siparişi kapatabilir.

- Alış Fatura Parametreleri / Ek Maliyet sekmesine "KDV Hesabı Tevkifata Göre Detaylandırılsın" seçeneği eklendi. İşaretlendiğinde, tevkifatlı alış faturalarındaki KDV tutarı içerisindeki tevkifat tutarının Tevkifat KDV Hesabı'na; KDV ve tevkifat tutarları arasındaki farkın da İndirilecek KDV Hesabı'na atılması sağlandı. Tevkifat KDV Hesap Kodu tanımı için bu seçenek işaretlendiğinde aktif olan "KDV Hesap Kodlarınızı Buradan Girebilirsiniz" alanı ile açılan "Tevkifat KDV Hesap Kodu Girişi" ekranı kullanılmalıdır. Ayrıca mal bazında KDV uygulamasının kullanıldığı durumda, bu özelliğin aktif olabilmesi için satır bazı tevkifat uygulaması da açılmalıdır.

- Depolar arası transfer, alış irsaliyesi, satış irsaliyesi, ambar giriş fişi ve ambar çıkış fişi için belge bazında log atılması sağlandı. Netsis güncellemesi yapıldıktan sonra log triggerlarının tekrardan yaratılması gerekiyor.

- İhracat tipli irsaliye cari harekete işlenmediği için risk toplamı etkilenmiyordu. 'FATURA','IRS_IHR_CARI_ISLE' özel parametresi tanımlandığında cari harekete işlendiği için risk toplamı oluşuyor, fakat bu sefer de ihracat irsaliye birleştirme işlemi irsaliyeler saklanarak yapıldığında eski irsaliye ve birleşimden oluşan irsaliye de cari harekette gösterildiği için risk yanlış hesaplanıyor. İrsaliye birleştikten sonra eski irsaliye hareketlerinin silinmesi için 'DEKONT','BIRIRSCAHARSIL' özel parametresi tanımlandı. 'FATURA','IRS_IHR_CARI_ISLE' ve 'DEKONT','BIRIRSCAHARSIL' özel parametreleri beraber tanımlandığında hem cari risk hem irsaliye birleştirme doğru çalışıyor.

- Taslak oluşturulmuş veya gönderilmiş e-irsaliye belgelerinde değişiklik yapılamaması sağlandı. Bu irsaliyeler "Satış İrsaliyelerini Toplu Faturalama" menüsünden faturalaştırılabilir.

- Sipariş rezervasyon ekranında ‘Kapalı Siparişler Revize Siparişe aktarılsın’ parametresi eklendi. Rezervasyonu yapılan sipariş kaleminin kapalı olması durumunda, bu kalemler kapalı olarak revize siparişe aktarılacaktır.

- E- Fatura birim eşleştirme ekranında Uluslararası Birim Ölçü Birim Kodları alanına CS(Koli-Kasa) birim kodu eklendi.

- E- Fatura birim eşleştirme ekranında Uluslararası Para Birim Kodu alanına QAR(Katar Riyali) para birimi eklendi.

**Muhasebe Modülü**

- Hesap Kodu Aktarımı işleminde Başlangıç/Bitiş Tarihi alanlarına Gün/Ay/Yıl olarak kısıt verilebilmesi desteklendi.

- Proje Mizanı raporuna "Proje Kodu Kırılımı" seçeneği eklendi. İşaretlendiğinde, bakiyeler proje kodu kırılımı ile gösterilmektedir.

**Cari Modülü**

- Cari irtibat bilgilerinde aynı cari için 2 farklı kayıt girilip her kayıt için farklı özel dizayn tanımlandığında her cari kaydı için ilgili özel dizayn ile e-posta gönderilmesi sağlandı.

- Alınan Teminat Mektupları Raporu'na "Proje Kodu Kırılımı" ve "Proje Kodu Aralığı" eklendi. Böylece proje koduna göre kısıt verilerek ya da proje kodu kırılımlı olarak rapor alınabilmesi desteklendi.

- Cari hesap kayıtlarına "Cari Banka Bilgileri" sekmesi eklendi. Bu sekmede carinin cari - banka kayıtları gösterilmesi sağlandı.

- Yaşlandırmalı Özel Hesap Kapatma Genel Kısıtlar ekranına "Kapatma Tarih Seçimi" alanı eklendi. Böylece kapatma işlemi yaparken yaşlandırma bu alandan seçilen Vade Tarihi ya da Hareket Tarihine göre yapılacaktır.

- E-Mutabakat Yönetimi ekranında e-mutabakat oluşturulurken verilen kısıtların Seçenekler sekmesine "Bakiye Sadece TL Hareketlerden Oluşturulsun" seçeneği eklendi. İşaretlendiğinde, TL bakiye içerisine dövizli hareketlerin TL karşılıkları dahil edilmeden, sadece TL hareketlerin bakiyeleri gösterilmektedir.

- Cari Hareketler Dökümü rapor ekranında, TC No olan carilerin rapor alınırken vergi dairesi üst bilgisi eklendi.

**MRP Modülü**

- İş istasyonu tanımlamada makine seçim önceliği alanında seçilen değere göre çizelgeleme yapılması sağlandı. Yeni/Eski seçildiğinde makine tanımlama ekranındaki alış tarihine göre makinelerin yaşı hesaplanacaktır. Yaşı daha küçük olan (yeni) makineler daha öncelikli olacaktır. Hızlı/Yavaş seçildiğinde ilgili ürünün eşleştiği makinelerdeki üretim sürelerine bakılarak, üretim süresi düşük (hızlı) olan makineler daha öncelikli olacaktır. Maliyet seçildiğinde Makine tanımlama ekranındaki birim maliyet bilgisine bakılarak, birim maliyeti daha düşük olan makineler daha öncelikli olacaktır. Makinede Tanımlı Öncelik Sırası seçildiğinde ise makine tanımında verilen önceliğe göre çizelgeleme yapılacaktır.

- Çizelgeleme Gantt Gösterimi ekranına "Sabitlenen Tarihte Planlanamayan İş Emirleri" raporu eklendi. İş Emri Sabitleme yapılmasına rağmen sabitlenen tarihe planlanamayan işlerle ilgili sebepleri ile birlikte bilgi verilmesi sağlandı.

- Hazırlık süresi tanımlama ekranında "Kendisine ait hazırlık süresi" tipine "Sadece Makinedeki İlk Operasyon İçin" seçeneği eklendi. Sadece makinedeki ilk operasyon için seçeneği işaretlendiğinde ilgili operasyon için sadece makinedeki ilk işlem sırasında hazırlık süresi işletilecektir. Yani bu operasyon her yapıldığında hazırlık süresi ortaya çıkmayacaktır. Sadece ilgili makinenin ilk işlemi ise hazırlık yapılacaktır.

- Makine Tanımlama\\Fason Lojistik Planı tanımlama ekranında giden gün seçildikten sonra Dönüş süresinin 30 güne kadar verilebilmesi sağlandı.

- Malzeme Gereksiniminden İş Emri oluşturma ekranına iş emri gruplama seçeneği getirildi. Bu ekranda "Yeni İş Emri Bilgileri" sekmesine en son satıra "İş Emri Kalemleri için Gruplama Seçeneği" eklendi. Bu koşul üretim parametreleri iş emri kalem uygulaması ve mrp parametreleri sipariş bazında rezevasyon aktif olduğunda desteklenecektir. Bu parametre seçeneklerine göre iş emirleri gruplandırılma desteklendi.

- Sipariş Termin Raporunda sipariş bazında takip edilmeyen kümüle edilen iş emirlerinin sipariş bağlantısı getirilerek iş emirlerini kümüle göstermektedir.

- MRP işlemlerin altında Müşteri Siparişleri Önceliklendirme ekranına "Sipariş Satırları Getirilsin" parametresi eklendi. Bu parametreinin aktif olabilmesi için MRP parametrelerinden "sipariş bazında rezervasyon sistemi" parametresinin işaretli olması gerekiyor. Bu parametre işaretlenerek "Kayıtları Getir" butonuna tıklandığında müşteri siparişleri satırlarıyla beraber detaylı getirilecektir. Ayrıca bu durumda alt bölümdeki grid üzerinde "Sipariş Numarası" alanından sonra "Sipariş Sıra No" alanı görünür olacaktır. Bu durumda siparişin satırları bazında ayrı öncelik bilgisi girilerek kayıt yapılabilecektir.

- MRP Parametreleri ve Malzeme Gereksinim Planlama\\Kapasite Planlama sekmesine "İhtiyaçlar sadece ardışık periyotlara bölünebilsin" parametresi eklendi. Bu parametre; Farklı periyot ve makinelere bölünebilsin ve Farklı periyotlara bölünebilsin seçenekleri seçili olduğunda aktif gelmektedir. Bu parametre seçili oldupğunda ihtiyaç kalemi ardışık periyotlara dağıtılacak. Ardışık sırada bir periyodun atlanması gereken durumda ise ihtiyacın geri kalan kısmı ilk ihtiyaç tarihine yerleştirilecek ve bu periyotta kapasite aşımı olacaktır.

- MRP Kayıt modülü altındaki Tahminleme İşlemleri ekranına Excel’den veri aktarımı desteği getirildi. Tahminleme işlemleri ilk sekmesinde "Satış Verisi" alanına "Excel'den Aktarım" şeklinde yeni bir seçenek eklendi. Eğer satış verisi olarak "Excel'den Aktarım" seçeneği seçilirse "Satış Verisi Oluşturma" sekmesindeki sol tarafta yer alan "Şirketler" bölümü seçilmemektedir. Yüklenecek olan excelde sırasyıla şu alanlar istenecektir. Grup Kodu(Gruplama seçeneği "Stok Kodu"ndan farklı ise bu alan sorulacaktı), Stok Kodu, YapKodu(Yapılandırma uygulaması açık ise) Periyot, Yıl, Miktar

- MRP\\Raporlar\\İleri Üretim Çizelegeleme menüsü altına Çizelgeleme-Gantt ekranındaki raporlar eklendi. (Çizelge-Taslak Sonuç Raporu, İş Emri Kullanım Raporu, Geciken İşler Raporu, Sipariş Termin Raporu, Çizelge Performans Raporu, Çizelge Bazlı Kapasite Raporu, Kaynak Bakım Planı Raporu )

- Çizelgeleme Gantt Gösterimi ekranı üzerinden ‘İş emri Sabitleme’ ekranı açılındığında; "Sabitlenecek Periyot" ismiyle yeni bir buton eklenmiştir. Bu butona tıklandığında Periyot Tipi ve Sabitlenecek Periyot Sayısı alanları sorulacaktır. Bu periyoda göre planlanan tarihe göre ilgili iş emirleri planlanan tarihe ve makinelere sabitlenecektir.

- Müşteri Siparişinin Kesinleşen veya Plananlanan durumu İleri Üretim Planlama ekranına Sipariş Plan\\Kesin kolonuna eklendi.

- Çizelgeleme Gantt Gösterimi ekranının Çizelgelenen İşler ve Dışa aktarım Excel raporlarına "Operasyon Kodu" sahasından sonra "Operasyon Adı" kolonu, "Makine Kodu" sahasından sonra sırasıyla "Makine İsmi", "İstasyon Kodu" ve "İstasyon Adı" kolonu eklenmiştir.

- Bir rotada bir operasyonun birden fazla geçmesi durumunda operasyon-makine eşleştirme ekranına operasyon sıra no alanı eklenmiştir. Bu alan sadece operasyonun birden fazla geçmesi durumunda aktif oalcaktır. Operasyon sıra numarası bazında makine üretim verileri kaydedilebilir bu doğrultuda çizelgeleme çalıştırılabilir.
- Satıcı siparişlerinin teslim tarihi değiştiğinde MRP tekrar çalıştırılıp çizelgelendiğinde iş emirleninin satıcı siparişinin teslim tarihine göre güncellenmesi desteklendi. Bu özelliğin çalışabilmesi için algoritma opsiyonlarında "MRP Tedarik Planı Dikkate Alınsın" parametresi işaretli olması gerekmektedir.

- Operasyon tanımlama ekranında Üretim Bilgileri grubu içindeki geçiş süresi alanı transfer süresi olarak değiştirilmiştir. Geçiş Miktarı\\Süresi grubunda yer alan geçiş miktarı alanı sadece miktar olarak tutuluyordu. Süre olarakta tutulabilmesi sağlandı.

- İleri Üretim Planlama Genel Algoritmalarında öncelik siparişten okunsun parametresinin aktif olduğu durumda müşteri siparişlerinde önceliklere göre işe emri planlaması sağlandı. MRP parametrelerinde ‘Müşteri Siparişi Sıralama Kriterinin Tutulacağı Saha’ alanını müşteri siparişlerinden kalem öncelikleri belirtilebilir. Bu öncelik değerlerine göre işe emirleri planlanabilir.

**Çek\\Senet Modülü**

- Devir çek / senet ekranında sağ tık menüsünde bulunan "Tarihsel Çek / Senet İzleme" ekranına "İşlem Yapan Kullanıcı" alanı eklendi. Bu başlık altında o işlemi hangi kullanıcı yapmış görülmesi sağlandı.

- Verene göre senet listesi raporuna "Ödeme Detay Bilgisi Basılsın" seçeneği eklendi. Bu seçenek işaretlendiğinde rapora "Ödenen TL Tutar", "Kalan TL Tutar", "Ödenen Döviz Tutar" ve "Kalan Döviz Tutar" alanlarının gelmesi sağlandı.

- Çek ve senet ekranlarında 14 haneli çek ve senet numaralarının ilk ve son kodları girilip tab tuşuna basıldığında aradaki sıfır (0) rakamlarının eklenmesi sağlandı.

**Müstahsil Faturası Modülü**

- E-Müstahsil işlemleri altına "Birim Eşleştirme" eklendi.

- E-Müstahsil işlemleri menüsü altında "Toplu E-Müstahsil Basımı" eklendi.

**Dış Ticaret Modülü**

- "Konteyner Tanımları", "Gümrük Ofis Tanımları" ve "Ödeme Açıklamaları" ekranlarına işletme ve şube kodu bilgisinin tanımlanabilmesi sağlandı.

**Makine Bakım Modülü**

- Bakım Emirleri - Dizayn Basımı işlemine görsel dizayn desteği getirildi. Dizayn data olarak DZNBAKIMEMRI seçilmelidir.

**Banka Modülü**

- MT940 işlem kodlarına "OKL - Okul ödemeleri" eklendi. Bu işlem tipi ile sadece genel dekont kaydı girilebiliyor.

- MT940 parametrelerine "MT940 kural tespitinde sadece metin alanı eşleştirilsin" seçeneği eklendi. Bu seçenek işaretlendiğinde sadece işlem kodu ve borç/alacak durumuna bağlı olarak bulunan kurallar içerisinde metin alanı, hesap hareket açıklamasında bulunan kayıtlar eşlenecektir. Diğer kural tespit adımları çalıştırılmayacaktır.

- Banka\\Kayıt\\TCMB kayıtları\\TCMB Banka Kayıtları Online Güncellenme ekranında TCMB web servis üzerinden banka şube kayıtlarının güncellenmesi sağlanmıştır.

**Üretim Modülü**

- Reçete kaydında mamul için de fire bilgisi girilebilmesi sağlandı. Reçetede mamul için girilen fire oranı üretim sonu kaydı, serbest üretim sonu kaydı, ters üretim sonu kaydı ve mamul parçalama ekranlarında girilen miktar üzerinden hesaplanıp oluşan firenin 2. miktar alanına yazılması sağlandı.

- Üretim modülü kayıt menüsü altına "Aralık Bazında Fire Oranı Tanımlama" ekranı eklendi. Bu ekranda bileşen ve mamul bazında, istenilen aralıklarda istenilen fire oranı tanımlanabilmesi sağlandı. Buradaki fire oranları tanımlandıktan sonra USK/Serbest USK/Ters USK/Mamul Parçalama ekranlarında girilen miktar hangi aralığa denk geliyorsa o fire miktarları 2. miktar alanına yazılır. "Aralık Bazında Fire Oranı Tanımlama" ekranına reçete kaydındaki fire tanımlama alanının yanındaki göz ikonu ile de ulaşılabilir. "Aralık Bazında Fire Oranı Tanımlama" ekranında tanımlanan oranların çalışması için üretim parametrelerinde "Üretim Kayıtlarında Aralık Bazında Fire Oranları Dikkate Alınsın" parametresi işaretlenmesi gerekir.

- Bir mamulün reçetesi düzenlenip iş akışına girdiğinde, bu mamul iş emri girişinde kullanılamaması sağlandı. Eğer mamul iş akışı sürecindeyse bu mamul sadece akışı onaylayacak kullanıcıda görünüyor.

**Dekont Modülü**

- TL tutarlı çek veya senet tahsil dekontu ekranında kayıt tarihi çıkışında döviz bilgisinin sorulması sağlandı.

**Kasa Modülü**

- Kasa modülü Kasa Raporuna Plasiyer Kodu ve Plasiyer Adı alanları eklendi.

**Demirbaş**

- Detaylı değerleme ve amortisman ve değerleme ve amortisman raporlarına "İtfa Olan Demirbaşlar Basılsın" seçeneği eklendi.

- Demirbaş işlemler menüsü altına "Toplu Dekont Oluşturma" eklendi. Bu ekran ile istenilen aralıktaki demirbaşların toplu dekont oluşturulması sağlandı.

- Taşınmazlara 30.09.2018 tarihine kadar bir defaya mahsus getirilen yeniden değerleme imkânı hakkında yayınlanan VUK tebliğine göre programda düzenleme yapılmıştır. Demirbaş Bilgi Kartı ekranına "Değerleme Oranı" alanı eklendi. "Yeniden Değerlemeye Tabi" seçeneği işaretli ise Yeniden Değerleme ve Amortisman Ayırma işlemi ile demirbaş bazında girilen değerleme oranı varsa bu orana göre, yoksa Değerleme Oran Girişi ekranında belirtilen orana göre yeniden değerleme yapılmaktadır. Yeniden değerleme işlemi sonrasında demirbaş kartlarından "Yeniden Değerlemeye Tabi" seçeneğinin işareti otomatik kaldırılmaktadır.

- Değerleme ve Amortisman Raporu'nun Genel Kısıtlar sekmesine "Miktar Bilgisi Basılsın" seçeneği eklendi. İşaretlendiğinde raporda demirbaşlara ait "Alış Miktarı", "Toplam Satış Miktarı", "Miktar(Bakiye)" bilgileri gösterilmektedir.

**Stok Modülü**

- Stok hareket kayıtları ekranında üretim tipli bir belge seçilip üst bölümden "Fiş No" alanına çift tıkladığımıza üretim kaydı hangi ekran üzerinden (Üretim Sonu Kaydı Ekranı, Serbest Üretim Sonu Kaydı Ekranı, UAK üzerinden USK, Kalite Kontrol üzerinden USK, Ters Üretim Sonu Kaydı, Mamul Parçalama) yapıldıysa o ekrana gitmesi sağlandı.
