---
title: "9.0.27 Mart 2020"
page_id: "50660445"
product: "netsis-3-enterprise"
depth: 3
is_section: true
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Sürüm Dokümanları"
  - "2020 Netsis"
  - "9.0.27 Mart 2020"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Sürüm Dokümanları / 2020 Netsis / 9.0.27 Mart 2020"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTQ4Mzc2ODQyLWM4ZGUtNDNjYS04YzU1LTQ4OGZkMWQ3YzBlYyZsaW5rPTc4YTQ4OTUzLTI3YmYtNDBiYi1hNTVjLTA0Nzk3MmZjZjM5YSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=48376842-c8de-43ca-8c55-488fd1d7c0ec&link=78a48953-27bf-40bb-a55c-047972fcf39a&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "9-0-27-mart-2020_50660447_50660445.html"
source_version: "2022-07-05T13:02:52.393+03:00"
source_bytes: 76848
fetched_at: "2026-09-13T04:28:21+00:00"
generator: "netsis-scraper 1.0.0"
---
# 9.0.27 Mart 2020

Netsis 9.0.27 sürümünde yapılan yenilikler aşağıdaki şekildedir:

**1- [Sipariş Bağlantılı İhracat Tipli İrsaliye Kaydı Ekranı Üst Bilgiler Sekmesinde e-İrsaliye Parametresinin Pasif Gelmesi İle İlgili Durumun Düzeltilmesi Talebi](https://jira.logo.com.tr/browse/NTERP-50613)**

İhracat Tipli İrsaliye Kaydı ekranından e-İrsaliye oluşturulması sağlanmıştır.

**2- [Çizelgeleme Genel Algoritma İçin Kaynakların İş Emrinin Operasyon Boyunca Rezerve Edilmesinin Sağlanması](https://jira.logo.com.tr/browse/NTERP-50268)**

Çizelgeleme sırasında, rotasında birden fazla operasyonu bulunan ürünler için ilk operasyonda kullanılan kaynağın sonraki operasyonlar için de ilgili iş emrine rezerve edilmesi desteklenmiştir. Bu sayede iş emrinin ilk operasyonda kullanmaya başladığı kaynak iş emrinin, bütün operasyonları bitmeden başka iş emirleri tarafından kullanılması engellenmiştir.
Bu özelliğin kaynak bazında aktif hale getirilmesi için "Kaynak Tanımlama" ekranındaki "İş Emrinin Operasyonları Boyunca Rezerve Edilsin" seçeneğinin işaretlenmesi gerekir.
İlgili parametrenin kullanılması için "İleri Üretim Planlama" lisansının bulunması ve "MRP Parametreleri" ekranından "İleri Üretim Planlama" seçeneğinin işaretlenmesi gerekir.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=PkhpIncKnpg&ab_channel=LogoDestek).

**3- [e-İrsaliye İhrac Kayıtlı ve İhracat Tipli e-İrsaliyelerin Toplu e-İrsaliye Ekranına Gelmesi İçin Belge Tipi Alanına İhraç Kayıtlı ve İhracat Tipli Seçeneklerinin Eklenmesi Talebi](https://jira.logo.com.tr/browse/NTERP-49953)**

e-İrsaliye belgeleriyle ihracat yapılması sağlanmıştır. "Toplu e-İrsaliye Oluşturma" ekranındaki belge tiplerine "İhraç Kayıtlı İrsaliyeler" ve "İhracat İrsaliyeleri" eklenmiştir.

**4- [Modül Dizaynlarının Altından e-Müstahsil Makbuzu İçin Atama Yapılmasının Sağlanması](https://jira.logo.com.tr/browse/NTERP-49876)**

Modül dizaynlarına e-İrsaliye ve e-Müstahsil eklenmiştir.

**5- [NetOpenX e-Belge Kaynak Tipi'ne Lokal Deponun Eklenmesi Talebi](https://jira.logo.com.tr/browse/NTERP-49872)**

Lokal depo tipli e-İrsaliye'den taslak oluşturulması ve gönderilmesi sağlanmıştır.

**6- [Dizayn Kayıtları Ekranındaki "e-Devlet XML Tag" Alanına "BillingReference-InvoiceDocumentReference-ID", "BillingReference-InvoiceDocumentReference-IssueDate" ve "BillingReference-InvoiceDocumentReference-DocumentTypeCode" Eklenmesi Talebi](https://jira.logo.com.tr/browse/NTERP-49520)**

Dizayn Kayıtları ekranındaki "e-Devlet XML Tag" alanına "BillingReference-InvoiceDocumentReference-ID", "BillingReference-InvoiceDocumentReference-IssueDate" ve "BillingReference-InvoiceDocumentReference-DocumentTypeCode" eklenmiştir.

**7- [Üretim Seri İzlenebilirlik Raporunda Stok Kodu Kısıtı Hammadde Olarak Verildiğinde Ekrana Gelen Uyarı ile İlgili Durumun Düzeltilmesi Talebi](https://jira.logo.com.tr/browse/NTERP-49450)**

"Üretim Seri İzlenebilirlik" raporundaki "Stok Kodu" rehberinde olmayan kodların, stok kodu kısıtı olarak verilmesi engellenmiştir.

**8- [Zamanlanmış Görevler Eklentisi Desteğinin Getirilmesi Talebi](https://jira.logo.com.tr/browse/NTERP-49414)**

Netsis eklentilere "Zamanlanmış Görevler" olarak yeni bir eklenti eklenmiştir. Zamanlanmış görevler ile bazı işlemlerin görev olarak tanımlanması ve bu görevlerin sunucu üzerinde çalıştırılması sağlanmıştır.
Zamanlanmış Görevler Eklentisi ile; Zamanlanmış görevlerin listeleneceği, yeni görev tanımının yapılacağı ve mevcut görevlerin düzenlenebilir (Görev Kopyalama, Görev Silme gibi).
Zamanlanmış Görev Tanımı Ekranı ile; "Görev Tipi" seçenekleri (VB Script, Ön Tanımlı İşlemler, Uygulama Çalıştır) seçilerek görev tanımları yapılabilir. Bu görevlerin Başlangıç, Bitiş Tarihi ve tekrarlanma sıklığı düzenlenebilir.Ekranlar Üzerinden Görev Oluşturma ile; aşağıdaki ekranlar üzerinde belirli butonlar ile "Zamanlanmış Görev Ekle" fonksiyonu desteklenmiştir.
Malzeme Gereksinim Planlama, Stok - Maliyet Oluşturma, İleri Üretim Planlama ekranlarında yer alan rapor butonunun altındaki:
Gereksinim Planlama Oluşturma - Gereksinim Plan Kısıt - "Tümünü Oluştur" butonu,
Maliyet Hesaplatma - "Tamam" butonu,
Döviz Kur Güncelleme - "Kur Bilgilerini Netsis'ten Getir" butonu,
Stok Hareket Kontrol - "Tamam" butonu,
e-Fatura Sorgulama - "Sorgula" butonu,

Bu ekranlarda işaretli olan parametreler alınarak aynı şekilde "Zamanlanmış Görev Tanımı" ekranına taşınacaktır.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=fNcIZGYB7UU&ab_channel=LogoDestek).

**9- [Netsis Wings Word Dizayn Basımı ile İlgili Durumun Düzeltilmesi Talebi](https://jira.logo.com.tr/browse/NTERP-49396)**

Netsis Wings ürününde Word Dizayn basımı yapıldığında, Word dosyasının tarayıcıdan indirilmesi sağlanmıştır. Dizayn'da "Basım" veya "Sakla" seçilmesi fark etmiyor.

**10- [Komisyoncu veya Tüccar Olarak Sebze-Meyve Ticareti Yapanlara e-Fatura, e-Arşiv, e-İrsaliye ve e-Müstahsil Makbuzu Zorunluluğu Durumunun İlgili Belge Ekranlarında Desteklenmesi Talebi](https://jira.logo.com.tr/browse/NTERP-49366)**

Komisyoncu veya tüccar olarak sebze ve meyve ticareti yapanlara getirilen “Hal Faturası” kesme zorunluluğu, e-Fatura ve e-Arşiv belgelerinde desteklenmiştir.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=U3TUDQ48BT8&ab_channel=LogoDestek).

**11- [İş Emri Ekranı İçin Belge Kilitleme Desteğinin Getirilmesi Talebi](https://jira.logo.com.tr/browse/NTERP-49362)**

"İş Emri" ekranı için "Belge Kilitleme" özelliği desteklenmiştir.

**12- [Reçete Kaydı Ekranı İçin Belge Kilitleme Desteğinin Sağlanması](https://jira.logo.com.tr/browse/NTERP-49360)**

"Reçete Kaydı" ekranında "Belge Kilitleme" özelliği desteklenmiştir.

**13- ["Stok Kodu Değiştirme" İşleminde TBLMALIYETDETAIL ve TBLMALISARFDETAIL Tabloların Desteklenmesi Talebi](https://jira.logo.com.tr/browse/NTERP-49350)**

"Stok Kodu Değiştirme" işleminin Maliyet Detay ve Mali Sarf Detay kayıtlarında çalışması sağlanmıştır.

**14- [Cari Bazında Döviz Kuru Tanımlama Desteğinin Sağlanması](https://jira.logo.com.tr/browse/NTERP-49340)**

Döviz Takibi modülüne eklenen "Cari Bazında Döviz Kurları Girişi" ekranı ile cariler için belirli tarih aralıklarında özel kur tanımı yapılması sağlanmıştır. Ayrıca, Cari Hesap Kayıtları ekranının Cari Kart 2 sekmesine eklenen "Döviz Çevrim Tipi" alanı ile cari bazlı döviz çevrim tanımının yapılması sağlanmıştır. Cariler için tanımlanan kur bilgisinin değiştirilmesinin engellenmesi için de "Cari Parametreleri" ekranına eklenen "Cari Bazında Tanımlanan Döviz Kurları Belgede Değiştirilemesin" seçeneğinin işaretlenmesi gerekir.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=5YZCxeRsA1Y&ab_channel=LogoDestek).

**15- [Dövizli Çalışan Cariler İçin Cari Bazında Döviz Çevrim Tipi Tanımlanmasının Sağlanması](https://jira.logo.com.tr/browse/NTERP-49339)**

Cari Hesap Kayıtları - Cari Kart 2 sekmesine "Döviz Çevrim Tipi" alanı eklenmiştir. Yapılan tanım ile, dövizli çalışılan cariler için cari bazında döviz çevrim tanımının yapılması sağlanmıştır.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=zEvaW-evlWQ&feature=youtu.be).

**16- [Excel Aktarım Altyapısı ile Hızlı Giriş Ekranları ve Kopyala Yapıştır Desteğinin Sağlanması](https://jira.logo.com.tr/browse/NTERP-49325)**

Veritabanı İşlemleri araç çubuğuna XLS (Excel'den Aktarım) butonu eklenmiştir. Aktarım ekranındaki "Excel Dosyası" seçeneğine ek olarak "Hızlı Veri Girişi" seçeneği eklenmiştir. "Hızlı Veri Girişi" seçeneği ile, desteklenen kolonlardan sadece aktarım yapılması istenen kolonların seçilmesi ve kolonlara varsayılan değerin ataması sağlanmıştır. Ayrıca, her iki seçenek için de "Şablon Sakla", "Şablon Yükle" işlemleri desteklenmiştir. Böylece, yapılan tanımlar için şablon oluşturma ve bir sonraki aktarımda tanımlanan şablonu yükleyerek işlem yapılması sağlanmıştır.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=5YFp16j990g&ab_channel=LogoDestek).

**17- [Yeni Eklenen “e-Defter Oluşturulan Aya Ait Belgelerde Değişiklik Yapılmasın” Parametresinin Yevmiye Fişini Oluşturan Kaynak Belgelerin Değiştirilmesini Engellenmesi Talebi](https://jira.logo.com.tr/browse/NTERP-49307)**

"Mükellef ve Düzenleyen Bilgileri" ekranında “e-Defter Oluşturulan Aya Ait Belgelerde Değişiklik Yapılmasın” seçeneği işaretlendiğinde, e-Defter oluşturulmuş ay için ön muhasebe işlemlerinin de yapılması engellenmiştir.

**18- [Malzeme Gereksiniminden İş Emri Oluşturma Ekranından Oturum Bilgisinin Silinmesinin Sağlanması](https://jira.logo.com.tr/browse/NTERP-49286)**

Malzeme Gereksiniminden İş Emri Oluşturma, Malzeme Gereksiniminden Sipariş Oluşturma ve Malzeme Gereksiniminden Talep Oluşturma ekranlarında oturum bilgisinin silinmesi sağlanmıştır.

**19- [Kapatması Yapılan İhracat Operasyonuna Ait Dosyadaki Kapalı Parametresinin Kapatma Sonrası Otomatik Olarak İşaretlenmesi Talebi](https://jira.logo.com.tr/browse/NTERP-49154)**

"Dış Ticaret Parametreleri" ekranının "İhracat Parametreleri" sekmesine "İhracat Kapatması Yapılan Dosyaların Durumu Kapalı Olsun" seçeneği eklenmiştir. İşaretlendiğinde, ihracat dosyasının içindeki tüm belgelerin kapatması yapıldığında, dosyanın durumu "Kapalı" olarak güncellenir.

**20- [Tanımlı Bir Detaylı Fiyat Listesine Girildiğinde Şubelere Ekle ve Çıkarma İşleminin Yapılmasının Sağlanması](https://jira.logo.com.tr/browse/NTERP-49133)**

Detaylı Fiyat Listesi uygulamasında, tanımlı bir fiyat listesine girildiği zaman, fiyat listesinin dahil olduğu şube kodlarının izlenmesi ve yeni şube kodunun dahil edilmesi desteklenmiştir.

**21- [Binek Otomobiller İçin Amortisman Hesap Değişikliği Talebi](https://jira.logo.com.tr/browse/NTERP-49132)**

Demirbaş paketinde Kıstelyum tipindeki demirbaş hesapları için KKEG hesaplaması desteklenmiştir.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=yPy7rkX4P34&ab_channel=LogoDestek).

**22- [NetOpenX Cari Hareket Kontrol İşlemi Desteğinin Sağlanması](https://jira.logo.com.tr/browse/NTERP-49085)**

NetOpenX şirket nesnesi altında "Cari Hareket Kontrol" işlemi desteklenmiştir.

**23- [NetOpenX MRP Nesnesinde "Satıcı Kodu Kontrol" Parametresinin Desteklenmesi Talebi](https://jira.logo.com.tr/browse/NTERP-49083)**

NetOpenX MRP nesnesinde "Satıcı Kodu Kontrol" parametresi - mrp.SaticiKoduKontrolu - desteklenmiştir.

**24- [NetOpenX e-Fatura ve e-İrsaliye Cari Güncelleme İşlemi Desteğinin Sağlanması](https://jira.logo.com.tr/browse/NTERP-49080)**

eBelge nesnesinin altına EBelgeCariGuncelle özelliği eklenerek, e-Fatura ve e-İrsaliye Cari Güncelleme işlemi desteklenmiştir.

**25- [Toplu Depo Kodu Rehberine İçinde Bulunulan Şubeye Ait Depo Kodlarının Getirilmesi Talebi](https://jira.logo.com.tr/browse/NTERP-48990)**

"Fatura/İrsaliyelerde Toplu Depo Kodu Kullanılsın" parametresi işaretlendiğinde kullanılan toplu depo kodu rehberine, içinde bulunulan şubeye ait depo kodlarının getirilmesi sağlanmıştır.

**26- [Çoklu Tevkifat Oranı Tanımlama Ekranına İşletme ve Şube Kodu Eklenmesi Talebi](https://jira.logo.com.tr/browse/NTERP-48989)**

"Çoklu Tevkifat Oranı Tanımlama" ekranına İşletme Kodu ve Şube Kodu eklenmiştir.

**27- [İleri Üretim Planlama Modülü Çizelgeleme Ekranında İş Emirleri Gridine Alan Eklenmesi Talebi](https://jira.logo.com.tr/browse/NTERP-48980)**

İleri Üretim Planlama ekranında "İleri Kısıt" altındaki iş emri kısıtlarına ve gride - "Sadece İş Emirlerini Getir" yapıldığında - Grup Kodu, Kod-1, Kod-2, Kod-3, Kod-4 ve Kod-5 alanları eklenmiştir.

**28- [Stok Planlama Kayıtları Ekranı İçin Saha-Tablo Eşleştirmesi Desteğinin Getirilmesi Talebi](https://jira.logo.com.tr/browse/NTERP-48974)**

Stok - Kayıt - ''Stok Planlama Kayıtları" ekranına "Saha-Tablo Eşleştirmeleri" özelliği eklenmiştir.

**29- [Rest İtemslips Nesnesinde IrsaliyeBagliFaturaSil Metodunun Desteklenmesi Talebi](https://jira.logo.com.tr/browse/NTERP-48903)**

ItemSlipsManager nesnesinin altına DeleteItemSlipLinkedWaybill(irsaliyebaglıfaturasil) metodu eklenmiştir.

**30- [Borç Çeki ve Müşteri Çeki İçin Yapılan Tanımlar Uygulamada Çalışırken NetOpenX ile Atılan Kayıtlarda Çalışmaması ile İlgili Durumun Düzeltilmesi Talebi](https://jira.logo.com.tr/browse/NTERP-48853)**

Borç çeki ve Müşteri Çeki için girilen açıklama bilgilerinin NetOpenX ile atıldığında kayıtlara geçmesi sağlanmıştır.

**31- [NetOpenX Stok Planlama Kayıtları Ekranı Desteğinin Sağlanması](https://jira.logo.com.tr/browse/NTERP-48817)**

Temelset tarafında bulunan Stok Planlama Kayıtları ekranı NetOpenX arayüzü için PlanlamaKayitlari nesnesi adı altında desteklenmiştir.

**32- [Binek Oto Masraflarının Kanunen Kabul Edilmeyen Gider Olarak Girilmesinin Sağlanması](https://jira.logo.com.tr/browse/NTERP-48720)**

Binek oto masraflarının "Kanunen Kabul Edilmeyen Gider" olarak girilmesi sağlanmıştır.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=_GXj-_qELtc&ab_channel=LogoDestek).

**33- [NetUpdate Yapılan Makine Üzerinde Netsis Sunucu Servisi Yüklü Olduğunda Güncelleme İşlemi Öncesinde Servisin Durdurulması ve Windows Dizini Altındaki Servis Dosyasının Güncellenmesi Talebi](https://jira.logo.com.tr/browse/NTERP-48402)**

NetUpdate.exe Windows dizini altındaki sunucu servisinin güncellenmesi sağlanmıştır.

**34- [Wings'de Eylemsiz Zaman Aşımı Süresi Dolduğunda EphesusWeb.exe'nin Sonlanması Fakat SSO'da Kullanıcı Oturumunun Sonlanmaması ile İlgili Durumun Düzeltilmesi Talebi](https://jira.logo.com.tr/browse/NTERP-48391)**

Kurulum sırasında Wings'e zaman aşımı süresi verildiğinde eylemsiz zaman aşımı süresi Wings zaman aşımı süresinden küçükse eylemsiz zaman aşımının Wings zaman aşımı+60 saniye olarak tanımlanması sağlanmıştır.

**35- [Tevkifatlı ve Tevkifatsız İrsaliye Seçilip “Tevkifat Hesaplansın” Parametresi ile Faturalandırıldığında Tevkifatsız Faturaya Tevkifat Uygulaması Parametre Kaldırıldığında ise Tevkifatlı Faturadaki Tevkifatı Taşımaması Durumunun Düzeltilmesi Talebi](https://jira.logo.com.tr/browse/NTERP-48354)**

"Alış\\Satış İrsaliyelerini Toplu Faturalama" ekranına "Tevkifat Hesaplama Şekli" seçeneği eklenmiştir. Bu alanda "Hesaplanmasın" seçeneği işaretlendiğinde irsaliyelerde tevkifat olsa bile faturada tevkifat hesaplanmayacak, "Tümü İçin Hesaplansın" seçeneği işaretlendiğinde irsaliyede tevkifat olmasa bile faturasında tevkifat hesaplanacak, "İrsaliyedeki Değerler ile Hesaplansın" seçeneği işaretlendiğinde ise irsaliyede tevkifat olup olmaması durumuna göre irsaliyedeki tevkifat bilgisi faturaya taşınacaktır.

**36- [Fatura Ekranından Sağ Tuş ile Açılan "Teslim Cari Tanımlama" Ekranı Üzerinden Atılan Log Kayıtlarının Program No ve Modül No Bilgilerinin "Cari Hesap Kayıtları" Şeklinde Ayarlanması Talebi](https://jira.logo.com.tr/browse/NTERP-48305)**

Faturada sağ tuş ile açılan "Teslim Cari Tanımlama" ekranında yapılan işlemlerin, Log raporlarında Program ve Modül bilgilerinin "Cari Hesap Kayıtları" şeklinde görüntülenmesi sağlanmıştır.

**37- [Giriş Tipli Seri Hareketleri İçin SKT Bilgisinin Raf Ömrüne Göre Otomatik Oluşturulması Talebi](https://jira.logo.com.tr/browse/NTERP-48267)**

"Seri Parametreleri" ekranına "Son Kullanma Tarihi Risk Süresine Göre Hesaplansın" ve "Hesaplanan Son Kullanma Tarihi Değiştirilemesin" seçenekleri eklenmiştir. "Son Kullanma Tarihi Risk Süresine Göre Hesaplansın" seçildiğinde giriş tipli seri hareketleri için son kullanma tarihi (SKT) bilgisi stok kartındaki risk süresi ve zaman birimine göre otomatik hesaplanması sağlanmıştır. Seri girişinde SKT'nin, belge tarihi+risk süresi kadar hesaplanıp otomatik doldurulması sağlanmıştır. "Hesaplanan Son Kullanma Tarihi Değiştirilemesin" işaretlendiğinde ise SKT'yi kullanıcının değiştirememesi sağlanmıştır.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=r_69aEesyHQ&ab_channel=LogoDestek).

**38- [SSO'dan Yapılan Kullanıcı/Grup Hak Kopyalama İşleminde TBKULLANHAKP ve TBLKULLANPROGP Tablolarına Eklenen Yeni Alanların da Kopyalanmasının Sağlanması](https://jira.logo.com.tr/browse/NTERP-47944)**

SSO'da " Kullanıcı/Grup Hak Kopyalama" ile TBKULLANHAKP ve TBLKULLANPROGP tablolarında, TRH_KILIT_GUNGECMIS ve TRH_KILIT_GUNGELECEK alanlarının da kopyalanması sağlanmıştır.

**39- [Modül Bazlı Tarih Kilidi Ekranında "Taksitli Kredi Açma" Ekranının Desteklenmesi ve Taksitli Kredi Açma Ekranının Modül Bazlı Tarih Kilidini Desteklemesi Talebi](https://jira.logo.com.tr/browse/NTERP-47807)**

"Modül Bazında Tarih Kilitleme" ekranında "Taksitli Kredi Açma" ekranı desteklenmiştir.

**40- [NetOpenX İçin e-Arşiv İptal Faturası Desteğinin Sağlanması](https://jira.logo.com.tr/browse/NTERP-47478)**

NetOpenX e-Arşiv iptal faturası oluşturulması için, Ebelge nesnesinin altına IptalFaturasiOlustur(); özelliği eklenmiştir.

**41- [NetOpenX İçin Dekont Stopaj Girişi Desteğinin Sağlanması](https://jira.logo.com.tr/browse/NTERP-47120)**

NetOpenX dekont nesnesinin altında Stopaj ve Savunma Sanayi Destekleme Fonu (SSDF) alanları desteklenmiştir.

**42- [NetopenX - Banka Havale/EFT Kayıtları Desteğinin Sağlanması](https://jira.logo.com.tr/browse/NTERP-47113)**

Netsis ERP Müşteri-Satıcı Havale/EFT Kayıtları, Banka Hesapları Arası Havale/EFT Kayıtları ve Banka Hesapları Arası Virman ekranlarındaki işlemler için NetopenX desteği sağlanmıştır.

**43- [Seri Takibi Kayıtları Ekranına Yeni Desteklenen Opsiyonel Sahaların Eklenmesi Talebi](https://jira.logo.com.tr/browse/NTERP-46917)**

"Seri Parametreleri" ekranından seçilen "Opsiyonel Sahaların Girişi" seri takibi kayıtlarında da desteklenmiştir.

**44- [Fatura - Çoklu Kalem Girişi Ekranında Esnek Yapılandırma Kodu Desteğinin Sağlanması](https://jira.logo.com.tr/browse/NTERP-46916)**

Fatura - "Çoklu Kalem Girişi" ekranına "Esnek Yapılandırma" desteği getirilmiştir. "Çoklu Kalem Girişi" ekranından yapılandırma kodu girişi yapılması sağlanmıştır.

**45- [Hatırlatıcı Üzerinden Gelen Bildirimlere Tıklandığında "Hatırlatıcı Düzenleme" Ekranının Açılması ve İlgili Hatırlatmaya Ait Bilgilerin Görünmesi Talebi](https://jira.logo.com.tr/browse/NTERP-46891)**

Hatırlatıcı eklentisi üzerinden gelen bildirimlere tıklandığında, "Hatırlatıcı Düzenleme" ekranının açılması ve ilgili hatırlatmaya ait bilgilerin gösterilmesi sağlanmıştır.

**46- [Excel ile Stok Kartı Aktarım İşlemine Zaman Birimi Alanının Eklenmesi Talebi](https://jira.logo.com.tr/browse/NTERP-46641)**

"Stok Kartı Kayıtları" ekranında Excel'den Netsis'e aktarım işlemine "Risk Süresi" ve "Zaman Birimi" alanları eklenmiştir.

**47- [Seri Girişi Sırasında Desteklenen Opsiyonel Sahaların SUSK ve Fatura Nesnelerinde REST İçin Desteklenmesi Talebi](https://jira.logo.com.tr/browse/NTERP-46456)**

Seri Girişi sırasında opsiyonel sahaların SUSK ve Fatura nesnelerinde REST için desteklenmesi sağlanmıştır.

**48- [Gelen Faturaların Onay Sürecinin Optimizasyonu İçin e-Fatura Dizaynının Kalem Bilgileri Kısmında Programın Tag Bilgisi İstemesi ile İlgili Durumun Çözülmesi Talebi](https://jira.logo.com.tr/browse/NTERP-45403)**

Dizayn Kayıtları ekranında "e-Devlet XML Tag" alanına "InvoiceLine-OrderLineReference-IssueDate" eklenmiştir. Sipariş bağlantılı belgede, bu alana yazılan tarih değerinin, e-Fatura XML'inde "Kalemler" bölümündeki "Sipariş Tarihi" alanına basılması sağlanmıştır.

**49- [Tarih Aralıklı Mizan Raporunda "Miktar Yazılsın" Seçeneği İşaretlendiğinde Mizan Raporundaki Gibi Rapora Ölçü Birimi Alanının Gelmesinin Sağlanması](https://jira.logo.com.tr/browse/NTERP-45398)**

"Tarih Aralıklı Mizan" raporunda "Miktar Yazılsın" seçeneği işaretlendiğinde mizan raporundaki gibi rapora ölçü birimi alanının gelmesi sağlanmıştır. "Dövizli Mizan" raporunda da "Ölçü Birimi" alanının "Miktar Yazılsın" seçeneğinin işaretlenmesine göre gelmesi sağlanmıştır.

**50- [Geçici Vergi Beyannamesi İçin "Sınai Mülkiyet Haklarında İstisna Tablosu Ekinin" Desteklenmesi Talebi](https://jira.logo.com.tr/browse/NTERP-45285)**

Geçici Vergi Beyannamesi'nde "Gelir Geçici Beyanname için Sınai Mülkiyet Haklarında İstisna Tablosu Eki" desteklenmiştir.

**51- [Geçici Vergi Beyannamesi İçin Eğitim Sağlık Harcamaları Ekinin Desteklenmesi Talebi](https://jira.logo.com.tr/browse/NTERP-45280)**

Geçici Vergi Beyannamesi'nde "Eğitim Sağlık Harcamaları Eki" desteklenmiştir.

**52- [Cariler İçin Belirli Tarih Aralığında Özel Kur Tanımının Yapılmasının Sağlanması](https://jira.logo.com.tr/browse/NTERP-44885)**

"Döviz Takibi" modülüne eklenen "Cari Bazında Döviz Kurları Girişi" ekranı ile cariler için belirli tarih aralıklarında özel kur tanımı yapılması sağlanmıştır. Ayrıca, "Cari Hesap Kayıtları" ekranının "Cari Kart-2" sekmesine eklenen "Döviz Çevrim Tipi" alanı ile cari bazlı döviz çevrim tanımının yapılması sağlanmıştır.

**53- [Regkontrol Çalıştırma İşleminin Set Güncelleme Sonrası Otomatik Olarak Çalıştırılması Talebi](https://jira.logo.com.tr/browse/NTERP-44811)**

Versiyon güncelleme işlemlerinden sonra RegKontrol.exe'nin Netsis açıldığında otomatik olarak çalıştırılması sağlanmıştır.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=lD6qdSOJMeo&ab_channel=LogoDestek).

**54- [DEKONT/DOVIZEKRAN Özel Parametresinin Portföydeki Çek/Senet Karşılıksız İşleminde de Çalışmasının Sağlanması](https://jira.logo.com.tr/browse/NTERP-44647)**

"Portföydeki Senet-Çek Karşılıksız İşlemi" için DEKONT/DOVIZEKRAN özel parametresinin çalışması desteklenmiştir.

**55- [Excel Dosyasından Sürükle Bırak Yöntemiyle Cari Kartlar Oluşturulurken Ödeme Tipi ve Kur Farkı Muhasebe Kod Alanlarının Şablona Eklenmesi Talebi](https://jira.logo.com.tr/browse/NTERP-44571)**

Excel dosyasından "Sürükle Bırak" yöntemiyle "Cari Kart Kayıtları" için "Ödeme Tipi" ve "Kur Farkı Borç-Alacak Muhasebe Kod" alanları desteklenmiştir.

**56- [Bakım Talep Kayıtları Ekranında Durumu "Bakım Emri Girildi" Olan Kayıtlar İçin Açılan "Bakım Emir No" Bilgisinin de Gösterilmesi Talebi](https://jira.logo.com.tr/browse/NTERP-44349)**

"Bakım Talep Kayıtları" ekranında, "Talebin Durumu" kolonunda "Bakım Emri Girildi" veya "Bakım Emri Kapandı" bilgisi olan kayıtlar için "Bakım Emri No" bilgisinin de gösterilmesi sağlanmıştır.

**57- [Cari Bazında Başlangıç ve Bitiş Tarihi Girilerek Kur Değerleri Tanımlanması Talebi](https://jira.logo.com.tr/browse/NTERP-43778)**

Döviz Takibi modülüne eklenen "Cari Bazında Döviz Kurları Girişi" ekranı ile cariler için belirli tarih aralıklarında özel kur tanımı yapılması sağlanmıştır. Ayrıca, "Cari Hesap Kayıtları" ekranının "Cari Kart-2" sekmesine eklenen "Döviz Çevrim Tipi" alanı ile de cari bazlı döviz çevrim tanımı yapılması sağlanmıştır.

**58- [Görsel Dizayn ile Basım Yapılması İçin Kasa Özel Parametre Talebi](https://jira.logo.com.tr/browse/NTERP-43529)**

KASA/KAYDETVEBASIMYAP özel parametresi ile kayıt sırasında görsel dizayn ile basım yapılması sağlanmıştır.

**59- [View Hak Kısıtları Ekranına Kopyalama ve Kullanıcı Bazında Tanımlama Sekmesinin Eklenmesi Talebi](https://jira.logo.com.tr/browse/NTERP-43518)**

"View Hak Kısıtları" ekranına "Kullanıcı Bazında" sekmesi eklenmiştir. Seçilen kullanıcı için, View kısıt tanımlarının yapılması sağlanmıştır.

**60- [B Formu Basımı Ekranında Kayıtlar Arasında Hızlı Geçiş Yapılamaması ile İlgili Durumunun Düzeltilmesi Talebi](https://jira.logo.com.tr/browse/NTERP-43230)**

"B Formu Basımı" ekranında gridden kayıt seçilememesi ile ilgili durum düzeltilmiştir.

**61- [NetOpenX Reçete Kaydı Bileşen Ölçü Birimi Atamasının Desteklenmesi Talebi](https://jira.logo.com.tr/browse/NTERP-42931)**

Reçete kaydı aktarımında, bileşenin "ölçübr2" ve "ölçübr3" alanlarına göre aktarım yapılması desteklenmiştir.

**62- [e-Arşiv Serileri İçin Yeni Fatura No Alanının Sağ Tuş ile Açılan Seçeneklerine e-Arşiv Birim Kodlarının Eklenmesi Talebi](https://jira.logo.com.tr/browse/NTERP-42786)**

"Yeni Fatura No" alanında sağ tuş ile ekrana gelen menüye "E-Arşiv Birim Kodları" seçeneği eklenmiştir.

**63- [MRP - Raporlar - "Çizelge-Taslak Sonuç Raporu" Ekranına Taslak Kodu Kısıtının Eklenmesi Talebi](https://jira.logo.com.tr/browse/NTERP-42089)**

MRP - Raporlar - İleri Üretim Çizelgeleme - "Çizelge-Taslak Sonuç Raporu" ekranına "Taslak Kodu" kısıdı eklenmiştir. Böylece, taslak koduna göre de rapor alınması sağlanmıştır.

**64- [Borcu Kapatılan Demirbaşlar Başka Demirbaş Şirketine Transfer Edildiğinde ve Eski Şirkette Değerleme ve Amortisman Raporu Alındığında Transfer Edilen Demirbaşların Ekrana Gelmesinin Engellenmesi Talebi](https://jira.logo.com.tr/browse/NTERP-41771)**

Değerleme Ve Amortisman Raporu - "Genel Kısıtlar" sekmesine "Transfer Edilen Demirbaşlar Gösterilmesin" seçeneği eklenmiştir.

**65- [Kalite Kontrol Kaydı İçin Rest Desteğinin Sağlanması](https://jira.logo.com.tr/browse/NTERP-40544)**

REST servis üzerinde "Kalite Kontrol Kaydı" ekranı QualityControl nesnesi olarak desteklenmiştir.

**66- [Yeni Fatura Kaydı Yapılırken Kalem Girişi Yapıldıktan Sonra Üst Bilgiler Sekmesine Gelinip Döviz Baz Tarihi Değiştirildiğinde Kurların da Güncellenmesinin Sağlanması](https://jira.logo.com.tr/browse/NTERP-40002)**

Yeni fatura kaydı yapılırken kalem girişi yapıldıktan sonra "Üst Bilgiler" sekmesine gelinip "Döviz Baz Tarihi" değiştirildiğinde kurların da güncellenmesi sağlanmıştır.

**67- [NDI'da Akıllı Grid Bileşeninin Desteklenmesi](https://jira.logo.com.tr/browse/NTERP-39301)**

NDI uygulamasında; Filtreleme, Sıralama, Grid Üzerinden Güncelleme Yapma gibi özellikleri bulunan akıllı grid bileşeni desteklenmiştir.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=PkhpIncKnpg&ab_channel=LogoDestek).

**68- [Müşteri/Satıcı ve Banka Hesapları Arası Havale/EFT Kayıtları Ekranlarında Kayıt Üzerinde Düzeltme Yapılmasının Sağlanması](https://jira.logo.com.tr/browse/NTERP-39213)**

Müşteri/Satıcı ve Banka Hesapları Arası Havale/EFT Kayıtları ekranlarında düzeltme yapılması sağlanmıştır.

**69- [Modül Bazında Tarih Kilitleme Özelliğinin Desteklenmesi](https://jira.logo.com.tr/browse/NTERP-38506)**

"Malzeme Gereksinim Planlama ve "MRP Raporu" ekranlarına "Modül Bazında Tarih Kilitleme" özelliği eklenmiştir.
"Malzeme Gereksinim Planı" için Kayıt, Silme ve Düzeltme işlemlerinden önce "Tarih" alanına göre sistem tarafından tarih kilidi kontrolü yapılıp uyarı vermesi sağlanmıştır.
"MRP raporu" ekranında "Gereksinim Planlama Çalıştır" seçeneği işaretlendiğinde, ekrandaki Tarih" alanına göre sistem tarafından tarih kilidi kontrolü yapılması sağlanmıştır.

**70- [e-Fatura Gelen Kutusu Ekranındaki Kullanıcı Bilgilendirme İşlemine Tüm Şube Kullanıcılarının Gelmesinin Sağlanması](https://jira.logo.com.tr/browse/NTERP-36631)**

"Fatura Bazında Gelen e-Fatura" ekranındaki "Kullanıcı Bilgilendirme" işlemine "Şubeler Dahil" seçeneği eklenmiştir. İşaretlendiğinde, diğer şube kullanıcılarının da bilgilendirilmesi sağlanmıştır.

**71- [Dekont Rehberinden Modül Seçilerek İlgili Modüle Ait Bir Kayıt Seçilip Ekran Kapatıldığında Modüle Ait Seçeneğin Kalmasının Sağlanması](https://jira.logo.com.tr/browse/NTERP-32108)**

"Genel Dekont Kaydı" ekranında rehberden ilgili modüle ait kayıt seçildikten sonra ekran kapatıldığında, seçilen modüle ait seçeneğin kalması sağlanmıştır.

**İyileştirmeler**

**1-** **İstatistiksel Proses Kontrol İçin P Chart Grafiğinin Düzgün Görünmesinin Sağlanması**

Proses kontrol girişi P Chart grafik gösteriminde ondalık 4 hane olacak şekilde değiştirilmiştir.

**2- Yardımcı Programlar Şirket-Şube Parametreleri Ekranında "Raporlarda e-Posta Gönderilmesin" Parametresi İşaretli İken e-Faturaların da e-Posta Olarak Gönderilmemesi Talebi**

Yardımcı Programlar - Şirket/Şube Parametreleri ekranında "Raporlarda e-Posta Gönderilmesin" parametresi işaretli iken e-Faturaların da e-Posta olarak gönderilmemesi ile ilgili durum düzeltilmiştir.

**3- İşlenen Müstahsil Stoklarının "tblsthar" Kayıtlarında "sthar_kdv" Sütunlarına Stok Kartındaki KDV Oranlarının Atanması ile İlgili Durumun Düzeltilmesi ve "sthar" Kayıtlarındaki KDV Oranlarının "0" Olması Talebi**

Müstahsil makbuzu kaydında, KDV oranının stok hareket kayıtlarına "0" olarak atılması sağlanmıştır.

**4-Taslak Faturaya Navlun Eklendiğinde Oluşan Yeni Dövizli Mal Bedeli ve Döviz Genel Toplamında Fark Oluşması Fakat Kalemler Toplandığında Bu Farkın Elde Edilmemesi İle İlgili Durumun Düzeltilmesi Talebi**

İhracat Dosya İşlemleri - Detay Gösterme ekranında Navlun veya Sigorta proformaya eklendiğinde, mal bedelinin kalem tutar toplamından farklı oluşması ile ilgili durum düzeltilmiştir.

**5- Üretim Parametreleri - "Fire Kodu Sorulsun" Parametresi İşaretlenmediğinde Ekrana Gelen Uyarı İle İlgili Durumun Düzeltilmesi Talebi**

"Üretim Akış Kaydı" ekranından üretim sonu kaydı oluşturulması sırasında ekrana gelen fire kodu ile ilgili uyarı düzeltilmiştir.

**6- Enflasyon Çevrim İşlemi 32767 Numaralı Şubede Çalıştırıldığında Fişin 32767 Numaralı Şubede Oluşmasının Sağlanması**

Enflasyon çevrim işlemi 32767 numaralı şubede çalıştırıldığında, yevmiye fişinin de 32767 numaralı şubede oluşması sağlanmıştır.

**7- Türk Telekom Faturaları için TBLEFATMASTAX Tablosu İsim Kolonuna 150 Karakterden Fazla Kayıt Atılmaya Çalışıldığında Ekrana Gelen Uyarı ile İlgili Durumun Düzeltilmesi Talebi**

e-Fatura içinde vergi dairesi numarası uzun olan kayıtlar olduğunda ekrana gelen uyarı ile ilgili durum düzeltilmiştir.

**8- B Formu Oluşturulması Sırasında Ekrana Gelen Uyarı ile İlgili Durumun Düzeltilmesi Talebi**

Limit altı faturaların sayısı 32767 rakamından fazla olduğunda, "B Formu Oluşturma" ekranına gelen uyarı ile ilgili durum düzeltilmiştir.

**9- Depolar Arası Transfer Kaydında e-İrsaliye Seçili Olduğunda Cari Seçimi Yapılmasının Engellenmesi Talebi**

"Depolar Arası Transfer Kaydı" ekranında "Cari Kodu" alanı için kilitli cari uyarısı verilmesi sağlanmıştır.

**10- Tarih Aralıklı Mizan Alınırken "Cari Detay Basılsın" Seçeneği Kullanıldığında Bakiyelerin Doğru Hesaplanması Talebi**

Tarih Aralıklı Mizan alınırken, içinde "42" geçen carilerin döviz kurunun, raporda dikkate alınmaması ile ilgili durum düzeltilmiştir.

**11- "Siparişleştirilen Talepler Kapatılsın" Parametresi ile "Satınalma Talep Siparişleştirme" İşlemi Yapıldığında Teklifin Kapanmaması İle İlgili Durumun Düzeltilmesi Talebi**

Satınalma Talep Siparişleştirme - "Siparişleştirilen Talepler Kapatılsın" seçeneği işaretlendiğinde, satınalma talebinin kapatılmaması ile ilgili durum düzeltilmiştir.

**12- Programın Ana Ekranındaki Arama Çubuğunda Modül İsmi İle Arama Yapılıp Etiket Sihirbazına Tıklandığında Ekrana Gelen Uyarı İle İlgili Durumun Düzeltilmesi Talebi**

Programın ana ekranındaki arama çubuğunda modül ismi ile arama yapılıp "Etiket Sihirbazı" seçildiğinde ekrana gelen uyarı ile ilgili durum düzeltilmiştir.

**13- Hizmet Prim Değerlendirme Ekranından Prim Belgesi Oluşturulduğunda Fiyat Tarihinin Belgeye 00.00.0000 Olarak Gelmesi İle İlgili Durumun Düzeltilmesi Talebi**

"Hizmet Prim Değerlendirme" ekranından "Prim Belgesi" oluşturulduğunda, fiyat tarihinin belgeye 00.00.0000 olarak gelmesi ile ilgili durum düzeltilmiştir.

**14- Stok Hareket Kayıtlarında Seri Bilgisi İzleme Ekranına Girildiğinde Miktar Ondalıklarının Görünmesinin Sağlanması**

Stok Hareket Kayıtları - "Seri Bilgisi İzleme" ekranına girildiğinde, miktar ondalıklarının görünmemesi ile ilgili durum düzeltilmiştir.

**15- Entegre Ürününde Yurtiçi e-Arşiv Faturası Kaydedilmesi İstendiğinde Ekrana Gelen "Bu Seri İhracat Tipli İrsaliye Belgelerinde Kullanılmaktadır." Uyarısı İle İlgili Durumun Düzeltilmesi Talebi**

Entegre ürününde yurtiçi e-Arşiv faturası kaydedilmesi istendiğinde "Toplamlar" sekmesinde ekrana gelen "Bu seri ihracat tipli irsaliye belgelerinde kullanılmaktadır" uyarısı ile ilgili durum düzeltilmiştir.

**16- Mrp Raporuna Fire Miktarının Eklenmesi Talebi**

MRP','FIREORANI_DIKKATE_ALINSIN' özel parametresi tanımlı iken - reçetede fire oran olarak tanımlıysa - MRP çalıştırıldığında, firenin doğru hesaplanması sağlanmıştır.

**17- Seri Takibi Yapılmayan Bir Stok İçin Daha Sonra Seri Uygulaması Açıldığında Ekrana Gelen Uyarı ile İlgili Durumun Düzeltilmesi Talebi**

Genel Dekont Kaydı ekranında seri takibi yapılmayan bir stok için daha sonra seri uygulaması açıldığında, kayıt sırasında ekrana gelen uyarı ile ilgili durum düzeltilmiştir.

**18- MRP Raporu Alınması Sırasında Ekrana Gelen Uyarı ile İlgili Durumun Düzeltilmesi Talebi**

"Kapasite Kullanımları Kontrol Edilsin" parametresi seçili şekilde "MRP Raporu" alındığında ekrana gelen "access violation" uyarısı ile ilgili durum düzeltilmiştir.

**19- Satınalma Talep Siparişleştirme - "Bilgi Gösterimi" Sekmesindeki "Ek Alan" Sütununun Ekrana Gelmesinin Sağlanması**

Satınalma Talep Siparişleştirme - "Bilgi Gösterim" sekmesindeki "Ek Alan" sütunun ekrana gelmesi sağlanmıştır.

**20- "İthalat Dosya İşlemleri" Ekranından Dosya Seçilip Başka Sekmeye Geçtikten Sonra İlk Sekmeye Geri Dönüldüğünde Griddeki Kayıtların İlk Satırdan İtibaren Gösterilmesi İle İlgili Durumun Düzeltilmesi Talebi**

"İthalat Dosya İşlemleri" ekranından dosya seçilip başka sekmeye geçtikten sonra ilk sekmeye geri dönüldüğünde, griddeki kayıtların ilk satırdan itibaren gösterilmesi ile ilgili durum düzeltilmiştir.

**21- "İthalat Dosya İşlemleri" Ekranından Bir Dosya Seçili İken "Yeni Dosya" Butonu ile Dosya Oluşturulup Seçili Dosyanın Carisinden Farklı Bir Cari Girildiğinde Ekrana Gelen "Cari Değiştirilemez" Uyarısı ile İlgili Durumun Düzeltilmesi Talebi**

"İthalat Dosya İşlemleri" ekranında bir dosya seçili iken "Yeni Dosya" butonu ile dosya oluşturulup seçili dosyanın carisinden farklı bir cari girildiğinde ekrana gelen "Cari Değiştirilemez" uyarısı ile ilgili durum düzeltilmiştir.

**22- Kalem Sıralama İşleminde Kalem Sıralarının Değişmemesi ile İlgili Durumun Düzeltilmesi Talebi**

Kalem sıralama işleminde, kalem sıralarının değişmemesi ile ilgili durum düzeltilmiştir.

**23- Birim Katsayı Güncelleme Ekranında Bitiş Tarihi ve Kayıt Tarihi Aynı Gün Olduğunda Girilen Tarihe Ait Verilerin Ekrana Gelmemesi ile İlgili Durumun Düzeltilmesi Talebi**

Maliyet Muhasebesi - İşlemler - "Birim Katsayı Güncelleme" ekranında "Bitiş Tarihi" ile "Kayıt Tarihi" aynı gün ise,girilen tarihteki veriler ekrana gelmiyor ve Bitiş Tarihi bir gün sonrası olarak tanımlanmak zorunda kalınıyordu. Düzeltilerek, veritabanı seviyesinde alanın Tarih-Saat olarak düzenlemesi yapılmıştır.

**24- Serili Bir Mamul İçin Serbest USK Yapılıp Miktar Değiştirildiğinde ve Seri Bilgisi Silindiğinde Eski Seriyi Göstermeye Devam Etmesi ile İlgili Durumun Düzeltilmesi Talebi**

"Serbest Üretim Sonu Kaydı" ekranında seri takibi yapılan mamul için fiş oluşturulduğunda, oluşturulan fişte mamulün miktarı değiştirilip sonrasında açılan Seri Bilgisi ekranından seri bilgileri silince, seri bilgisi girilmeden miktar değişiyordu. Düzeltilerek, serili stok için miktar değişikliği yapıldığında, seri bilgisi girilmeden kayıt yapılması engellenmiştir.

**25- Cari Hesap Çek Alındı Kaydında Mevcut Belge Üzerinde Değişiklik Yapıldıktan Sonra "Bordro Tamamlama" Yapılamaması ile İlgili Durumun Düzeltilmesi Talebi**

Cari Hesap Çek/Senet Alındı Kaydı ekranından "Bordro Tamamlama" yapılması sağlanmıştır.

**26- Müşteri Sipariş Girişinde Detaylı Fiyat Listesi Tanımlamasına Göre Girilen Döviz Tipi İçin İlgili Fiyatın Fiyat Listesinden Getirilmesinin Sağlanması**

Belgede döviz tipi değişikliği yapıldığında, ilgili fiyatın fiyat listesinden getirilmesi sağlanmıştır.

**27- Üretim Seri İzlenebilirlik Raporunda Reçetesi Olmayan Bir Stok İçin Kısıt Verildiğinde Ekrana Gelen Uyarı ile İlgili Durumun Düzeltilmesi Talebi**

"Üretim Seri İzlenebilirlik" raporunda reçetesi olmayan bir mamulün "Stok Kodu" kısıdı olarak verilmesi engellenmiştir.

**28- Dekont Modülünde Excel'den Kalem Bilgilerinin Aktarılması İşleminde B Form Kolonunun E ya da H Değerini Excel'den Okumaması ile İlgili Durumun Düzeltilmesi Talebi**

Dekont Modülünde kalem bilgilerinin Excel'den aktarılması işleminde, "B Formu" alanının doğru çalışması sağlanmıştır.

**29- Yayınlanmış İş Emirlerinin Teslim Tarihi Değişitirilmesin Parametresi İşaretli İken MRP Çalıştırılğında Hammade İçin Bildirim Süresinin Doğru Hesaplanmasının Sağlanması**

Üretim Parametreleri - "Rezervasyon Durumu Yayımlandı olan İş Emirlerinin Teslim Tarihi Değiştirilmesin" parametresi işaretli iken, mamulün hammadde bildirim tarihinin doğru hesaplanması sağlanmıştır.

**30- Modül Dizaynlarında Bulunan Bazı Dizayn Tiplerinin Dizayn Basım Log Raporunda Bulunması Talebi**

Basım Log Raporu ekranında yer alan "Dizayn Tipi" alanına eksik olan dizayn tipleri eklenmiştir.

**31- Firma Bazlı e-Fatura/e-İrsaliye Lisansları Olduğunda EfaturaAyarlar.exe Dosyası e-Fatura Ayarlarında Entegratör Bilgilerinin Pasif Görünmesi ile İlgili Durumun Düzeltilmesi Talebi**

Firma bazlı e-Fatura/e-İrsaliye lisansları olduğunda, EfaturaAyarlar.exe dosyası e-Fatura ayarlarında entegratör bilgilerinin pasif görünmesi ile ilgili durum düzeltilmiştir.

**32- Barkod Kayıtlarına Girildiğinde İlgili Stok Seçildikten Sonra Ölçü Birimlerinin Ekrana Gelmemesi ile İlgili Durumun Düzeltilmesi Talebi .**

Stok- Kayıt - "Barkod Kayıtları" ekranında ilgili Stok Kodu seçildikten sonra ölçü birimlerinin ekrana gelmemesi ile ilgili durum düzeltilmiştir.

**33- Stok Kartından Fiyat Oluşturma İşleminde Fiyat Listesi Seçildikten Sonra İlerleme Yapılamaması ile İlgili Durumun Düzeltilmesi Talebi**

"Stok Kartından Fiyat Oluşturma" ekranında "Fiyat Kodu" alanına son numaranın otomatik olarak atanması ve müdahale edilememesi sağlanmıştır.

**34- Dövizli Hareket Dökümü; Faturada Detay, Faturada Detay Aynı Satırda, TL Tutarlar Basılmasın, Verilen Tarih Aralığında Hareketi Olmayanlar Dökülsün Parametreleri Seçilerek Alındığında Rapordaki Satırların Düzgün Görünmesinin Sağlanması**

"Dövizli Hareket Dökümü" ekranının "Genel Kısıtlar" sekmesinde yer alan "Fatura Detay Aynı Satırda" ve "TL Tutarlar Basılmasın" parametreleri seçilerek rapor alındığında, rapor kolonlarında meydana gelen kayma giderilerek raporun düzgün şekilde alınması sağlanmıştır.

**35- Finansman Raporu Alınırken Taksitli Kredi İçin Sadece Anaparanın Dikkate Alınmayarak Faizlerin de Rapora Eklenmesi Talebi**

"Finansman Raporu" alırken, taksitli kredi için banka alacak tutarlarına faiz tutarları raporlanmıyordu. Düzeltilerek, "Banka Alacak" satırında "Anapara+Faiz" olarak raporlanması sağlanmıştır.

**36- Kalite Kontrol Kaydı Girilmeyen Alış İrsaliyelerinin Toplu Faturalama Ekranından Faturalandırılmasının Engellenmesi Talebi**

'FATURA','KALITE_ZORUNLU' özel parametresi ve "Kalite Kontrol Parametreleri" ekranındaki "Kalite Kontrol Kaydı Kapatılmayan Alış İrsaliyeleri Faturalandırılamasın" parametreleri seçili iken, Kalite Kontrol Kaydı yapılmamış alış irsaliyelerinin ''Alış İrsaliyelerini Toplu Faturalama" ekranı üzerinden de faturalandırılması engellenmiştir.

**37- Cari İhracat Bilgileri Ekranında Ödeme Açıklamaları Rehberine "Ödeme Tip ve Açıklamaları" Ekranında Tanımlanan Değerlerin Gelmesi Talebi**

"Cari İhracat Bilgileri" ekranındaki "Ödeme Açıklamaları" rehberine "Ödeme Tip ve Açıklamaları" ekranında tanımlanan değerlerin gelmesi sağlanmıştır.

**38- Oracle Veritabanında Seri Takibi Bakiye Listesinde Seri Takibi Kayıtlarından Girilen Kayıtların Dikkate Alınmasının Sağlanması**

Oracle veritabanında "Seri Takibi Kayıtları" ekranından girilen kayıtların "Seri Takibi Bakiye Listesi" raporunda görünmemesi ile ilgili durum düzeltilmiştir.

**39- Stok Kartı Kopyalama İşleminde Saha Tablo Eşleştirmesi Ekranından Tanımlanan Kullanıcı Tanımlı Sahalar Bilgilerinin de Kopyalanmasının Sağlanması**

"Stok Kartı Kopyalama" işleminde, "Saha Tablo Eşleştirmesi" ekranından tanımlanan "Kullanıcı Tanımlı Sahalar" bilgilerinin de kopyalanması desteklenmiştir.

**40- e-Defter Saklama Hizmeti ile Defter Rapor Beratlarının da Saklanmasının Sağlanması**

e-Defter rapor beratlarının saklanması sağlanmıştır.

**41- Rest Satış İrsaliyesi Açıklama Kaydının TBLFATUEK Tablosuna Eklenmemesi ile İlgili Durumun Düzeltilmesi Talebi**

Rest ile aktarılan satış irsaliyesi kayıtlarında, "Üst Bilgiler" sekmesinden girilen "Ek Açıklama" alanlarının TBLFATUEK tablosuna kaydedilmesi sağlanmıştır.

**42- Yevmiye Fiş Raporu Gelişmiş Rapor Olarak Alındığında Değişen Fiş Numarasında Sayfa Atlansın Seçeneğinin Desteklenmesi Talebi**

Gelişmiş raporlarda Excel'e kaydedilen durumlar hariç, "Değişen Fiş Numarasında Sayfa Atlansın" seçeneği desteklenmiştir.

**43- Cari Hesap Çek Alındı Ekranına Getirilen Kayıtlı Bir Çek Üzerinden İlerleme Yapıldığında Kayıtlı Cari Açıklamasının "Çekiniz" Olarak Değişmesi ile İlgili Durumun Düzeltilmesi Talebi**

"Cari Hesap Çek Alındı Kaydı" ekranından bir bordro içine birden fazla çek kaydedildiğinde cari hareket açıklamasının değişmesi ile ilgili durum düzeltilmiştir.

**44- Seri Takibi Açık Olan Bir Stok İçin Satış Faturası Kesilirken Ekrana Gelen Uyarı ile İlgili Durumun Düzeltilmesi Talebi**

"Çıkışlar İçin Seri Otomatik Hesaplansın" ve "Miktar Kadar Seri Sorulsun" parametreleri işaretli iken fatura seri giriş ekranında alınan uyarı ile ilgili durum düzeltilmiştir.
