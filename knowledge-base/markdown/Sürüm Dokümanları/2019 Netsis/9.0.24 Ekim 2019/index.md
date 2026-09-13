---
title: "9.0.24 Ekim 2019"
page_id: "41165095"
product: "netsis-3-enterprise"
depth: 3
is_section: true
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Sürüm Dokümanları"
  - "2019 Netsis"
  - "9.0.24 Ekim 2019"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Sürüm Dokümanları / 2019 Netsis / 9.0.24 Ekim 2019"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTJkZjBkOTFmLWI4OGYtNGVlMi04MTgwLTk5MjJjOWVhMjNhYiZsaW5rPTM4YTA1YzM3LWQ3MTctNGU1Yy05MTkyLTA2MWU1NzFlNmJiNyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=2df0d91f-b88f-4ee2-8180-9922c9ea23ab&link=38a05c37-d717-4e5c-9192-061e571e6bb7&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "9-0-24-ekim-2019_41165103_41165095.html"
source_version: "2022-07-05T13:25:04.787+03:00"
source_bytes: 92159
fetched_at: "2026-09-13T04:28:27+00:00"
generator: "netsis-scraper 1.0.0"
---
# 9.0.24 Ekim 2019

**CARİ**

**Yenilikler**

**1- Cari Risk Girişi" Ekranında Yer Alan; Sipariş Riski, Sevk Riski, Yükleme Riski, İrsaliye Riski Alanlarına 0-100 Dışında Bir Rakam Yazılması**

"Cari Risk Girişi" ekranında yer alan Sipariş Riski, Sevk Riski, Yükleme Riski ve İrsaliye Riski alanlarına 0-100 aralığı dışında da değer verilerek, risk hesaplamalarının girilen değere göre yapılması desteklendi.

**2-** **Cari Sabit Kayıtlarının Döviz Bilgileri Sekmesinde Bakiye Kolonu Yerine, Borç Bakiye ve Alacak Bakiye Alanlarının Yer Alması**

Cari - Kayıt - Cari Hesap Kayıtları - Döviz Hareketleri sekmesinde bulunan "Bakiye" alanına, "Borç Bakiye" ve "Alacak Bakiye" alanları eklendi.

**3-** **"Cari Hesap Kayıtları" Ekranında, Performans Ölçme ve İyileştirme Çalışmalarının Yapılması**

"Cari Hesap Kayıtları" ekranında, performans ölçme ve iyileştirme çalışmaları yapıldı.

**4-** **e-Posta Gönderiminde, Gönderilmiş Öğeler Mantığında Bir Liste ve Hangi Tarihte Hangi Modülden Kime Mail Gönderildiğine Dair Bir Rapor Alınması**

Gönderilen e-Postaların log raporunun alınması için, Yardımcı Programlar - Raporlar - "e-Posta Log Raporu" eklendi. Bu rapor ile, gönderilen tüm e-Postaların gönderim durumu ve kim tarafından gönderildiği bilgisinin alınması sağlanır.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=dmq2oiW0xeA&ab_channel=LogoDestek).

**5-** **Sürükle Bırak Yöntemiyle Excel'den Veri Aktarımında, Cari Hesap Kartı Daha Önce Açılmışsa Uyarı Vermesi. Bu İşlemin Muhasebe Hesap Planı - Stok Kartları ve Diğer Kartların Açılmasında da Uygulanması**

Excel'den Netsis'e aktarım işleminde, "Cari Hesap Kayıtları" ekranı için "Veri Aktarımında Mevcut Kayıtlar İçin İşlem Yapılmasın" seçeneği desteklendi. İşaretlendiğinde, önceden tanımlı olan cari kartlar için aktarım işlemi yapılmaz.

**6- Cari Kart açarken, e-Fatura Carilerinin Ek Bilgiler Cari Alias Kısmında, Carinin Vergi Numarasına ya da TC Kimlik Numarasına Göre Rehber Şeklinde Sadece Cari Etiket Bilgilerinin Seçileceği Bir Rehber Olması**

Cari - Kayıt - Cari Hesap Kayıtları - Ek Bilgiler sekmesinde bulunan "Cari Alias Bilgisi" alanına, cariye ait alias bilgilerini listeleyen rehber butonu eklendi. "Cari Parametreleri" ekranına eklenen "Sadece Eşleşen Cari Alias Bilgisi Kaydedilebilsin" parametresi ile de, carinin VKN ya da TCKN bilgisine ait alias bilgisi dışında bir alias kaydedilememesi sağlandı.

**İyileştirmeler**

**1 - Gridde Herhangi Bir Kısıt Verilmeden Kullanıcı Tanımlı Sahalarda Ekrana Gelen Uyarının Kaldırılması Talebi**

"Cari Hesap Kayıtları" ve "Stok Kartı Kayıtları" ekranlarında, gridde filtreleme varken kartta düzeltme yapıldığında ekrana gelen uyarı kaldırıldı.

**FATURA**

**Yenilikler**

**1- Silinen Fatura Bilgisinin Restore Edilmesi**

Yardımcı Programlar - Kayıt - "Silinen Belge Parametreleri" menüsü eklendi. Silinen Belge Parametreleri - "Silinen Kayıtlar Geri Alınabilsin" parametresi işaretlendiğinde, Fatura - İşlemler - "Silinen Fatura Belgeleri" menüsü aktif hale gelir. İlgili ekranlar aracılığı ile, satış/alış faturalarında silinen belgelerin izlenmesi ve istendiği zaman silinen belgenin geri alınması sağlandı.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=sR0EVLGJfCc&ab_channel=LogoDestek).

**2- Kalem Bazında Doküman Eklenmesinin Sağlanması**

Fatura ve teklif belgelerine, kalem bazında doküman ekleme desteği getirildi. "Kalem Bilgileri" sekmesinde iken farenin sağ tuşu ile ekrana gelen menüye eklenen "Belge Ekleme" seçeneği ile kalemlere belge eklenmesi sağlandı.

**3- Hızlı Tahsilat Kaydında Kalan Tutarın Görünmesi Talebi**

"Fatura" modülünden açılan "Hızlı Tahsilat Kayıtları" ekranına "Kalan Tutar" alanı eklendi. Böylece, fatura tutarı ile tahsilat tutarı arasındaki farkın "Kalan Tutar" alanından izlenmesi sağlandı.

**4- Fatura Ek Açıklamalarının Sonunda Boşluk Olduğunda veya Enter Tuşuna Basıldığında, e-Arşiv Taslak Oluşturma İşlemi Yapılırken Uyarı Alınması**

e-Arşiv Faturası - "Ek Açıklama" alanlarının sonunda boşluk bırakıldığı zaman, "Taslak Oluşturma" işleminde uyarı alınmaması sağlandı.

**5**- **Negatif İskontonun Fiyat Artıran Şekilde Çalışması Talebi**

Faturada, satır iskontosu 2-3-4-5-6 için negatif değer girildiğinde de hesaplama yapılması sağlandı.

**6- Satış İrsaliyesi ya da Satış Faturası Ekranında, Seri Bilgisi Düzgün Şekilde Geliyor Fakat, Satış İrsaliyesi Faturalandırıldığında Ekrana Gelen Yeni Fatura Bilgileri Sekmesinde, Yeni Fatura Numarasının B0000.01 (irsaliye serisi : B) Olarak Gelmesi**

FATURA/FATSERIDEGER özel parametresi ile irsaliye faturalandırma işleminde, yeni fatura bilgileri ekranına faturanın varsayılan seri değerinin getirilmesi sağlandı. Varsayılan bir seri değeri tanımlı değilse, irsaliyenin serisi getirilir.

**7-** **Toplu Faturalama İşlemi Yapıldığında Sistem, Kalem Bazında Girilen Teslim Carilerini Kontrol Etmeden Kalemleri Birleştiriyor. Kalem Bazında Farklı Teslim Carileri Varsa, Faturada Kalemlerin İki Ayrı Satırda Görülmesi Talebi**

Satış Faturası - Kayıt - Satış Parametreleri - "Satır Bazında Teslim Cari Kodu Sorulsun" parametresinin işaretlendiği durumlarda, irsaliye kalem bazında teslim carisi seçilebilir. İrsaliyede aynı stok kodu, depo kodu ve fiyat bilgileri içeren kalemlerin teslim carilerinin farklı olması ve "Satış İrsaliyelerini Toplu Faturalandırma" ekranında "Mallar Birleştirilsin" seçeneğinin işaretlenmesi durumunda, kalemlerin teslim cari bilgisine göre kümüle edip faturalandırılması sağlandı.

**8- Dövizli Carilerde Belge Oluşturulurken, Fiyat ve Tutarların Dövizli Oluşturulması İle İlgili Sorgulamanın Kaldırılması ya da Özel Parametreye Bağlanması Talebi**

Dövizli e-Belgelerin taslak oluşturulması sırasında ekrana gelen "Fiyat ve Tutarlar Dövizli Oluşturulsun mu?" sorusunun özel parametre ile ekrana gelmemesi sağlandı. Bunun için, belge tipine göre EARSIV/DOVIZLIOLUSTUR, EFATURA/DOVIZLIOLUSTUR, EIRSALIYE/DOVIZLIOLUSTUR özel parametrelerinin tanımlanması gerekir. Özel parametrelerin "Değer" alanına; dövizli belgelerden dövizli taslak oluşması için E, TL taslak oluşması için H yazılması gerekir.

**9- Fatura Formunda Seri Girişi Yapıldıktan Sonra Tekrar Seri Girişi Açıldığında, Daha Önce Girilen Değerlerin Kaybolmamasının Sağlanması**

Fatura ekranlarında seri girişi tamamlandıktan sonra tekrar seri girişi ekranı açıldığında, mevcut kayıtların korunması sağlandı.

**10- Toplu E-Fatura ve e-Arşiv Basım Ekranlarında Belge No Rehberine, Sadece e-Fatura veya e-Arşivi Oluşan Belgelerin Getirilmesi Talebi**

Toplu e-Fatura ve e-Arşiv basım ekranlarında yer alan "Belge No" rehberine, sadece e-Faturası veya e-Arşivi olan belgelerin gelmesi sağlandı.

**11- Alış Parametrelerinde "İade Faturada Tahsilat Ekranı Çıksın" Parametresi Kullanıldığında, İade Tipli Alış Fatura Kaydında Çıkan Hızlı Tahsilat Kaydı Ekranının, Tahsilat Bilgisi Girilmeden Kapatılmasının Sağlanması**

FATURA/ALISIADETAHSILSEC özel parametresi ile alış parametrelerinde "İade Faturada Tahsilat Ekranı Çıksın" parametresinin kullanılması durumunda; İade tipli alış fatura kaydında ekrana gelen "Hızlı Tahsilat Kaydı" ekranının, tahsilat bilgisi girilmeden de kapatılması sağlandı.

**12- Netsis Dışından API Desteği İle e-Arşiv Oluşturulmasının Sağlanması**

e-Arşiv için API ara tablo desteklendi.

**13- Talep, Teklif, Sipariş, İrsaliye, Fatura, Depolar Arası Transfer ve Ambar Giriş-Çıkış Fişi Ekranlarında, Kalemler Kısmına Araya Satır Ekleme Özelliği Talebi**

Sipariş, İrsaliye, Fatura ve Ambar Giriş-Çıkış Fişi belgelerinde, "Kalemleri Sırala" özelliği desteklendi. Fatura Satış/Alış Parametreleri ekranında "İrsaliye/Sipariş Sıralama" seçeneğinin "Manuel Sıralama" olarak ayarlanması gerekir. Böylece, belgelerin "Toplamlar" sekmesinde iken farenin sağ tuşu ile ekrana gelen "Kalemleri Sırala" menüsü görülecek ve bu menü aracılığı ile açılan "Kalem Sıralama" ekranından kalemlerin sıralaması değiştirilmesi sağlanacak. İlgili özellik, Depolar Arası Transfer belgesinde ve Karma Koli Uygulamasının kullanıldığı durumlarda desteklenmemektedir.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=9qxX4NW0k94&ab_channel=LogoDestek).

**İyileştirmeler**

**1- Faturalaştırma Kırılımı "Cari Kod" ve "Proje Kodu" Seçildikten Sonra, İrsaliye Listesi Sekmesine Geçildiğinde SQL Syntax Uyarısının Alınması**

"Satış İrsaliyelerini Toplu Faturalama" ekranında, faturalaştırma kırılımı "Cari Kod" ve "Proje Kodu" seçildikten sonra "İrsaliye Listesi" sekmesine geçildiğinde ekrana gelen uyarı kaldırıldı.

**2-** **Ambar Fişi - "D.A.T İzleme Raporu" Alınırken Uygun Kısıtlar Girilmesine Rağmen Kaydın Ekrana Gelmemesi**

Ambar Fişi - "D.A.T İzleme Raporu" alınırken uygun kısıtların girilmesine rağmen kayıt ekrana gelmiyordu, düzeltildi.

**3- Tahsilat Kaydı Girilmiş "Açık" tipli Satış Faturasının Tahsilat Kaydının Silinmesi Durumunda, Kaydın Cari Hareketlerden de Silinmesi Talebi**

Satış Parametreleri - Genel 4 - “Fatura Düzeltme İşleminde Cariden Silme” parametresi işaretlendiğinde; tahsilat kaydı girilmiş "Açık" tipli satış faturasının tahsilat kaydının silinmesi durumunda, kaydın cari hareketlerden de silinmesi sağlandı.

**4- Fatura Sonunda Çıkan Sipariş Açma/Kapama İşleminde Kalem Bazında Sipariş Kapatıldığında, Siparişin Kilitlenmemesinin Sağlanması**

Fatura - Toplamlar sekmesinde açılan Sipariş Açma/Kapama ekranından, kalem bazında sipariş kapatıldığında, tüm siparişin kilitlenmesi ile ilgili durum düzeltildi.

**5- e-Logo Entegratör Fark Raporunda "Sorgulama İşleminden Sonra Netsis'te Bulunmayan Faturalar İndirilsin Mi?" Sorgusuna Hayır Denilmesine Rağmen Faturayı İndirmesi İle İlgili Durumun Düzeltilmesi Talebi**

e-Logo Entegratör Fark Raporunda "Sorgulama işleminden sonra Netsis'te bulunmayan faturalar indirilsin mi?" sorgusuna "Hayır" denilmesine rağmen faturanın indirilmesi ile ilgili durum düzeltildi.

**6- Gümüş Tevkifat Uygulamasında Risk Kontrolünün Yapılmasının Sağlanması**

Gümüş Tevkifat Uygulamasında risk kontrolü yapılamıyordu, düzeltildi.

**7- İhraç Kayıtlı Satış Faturalarında, Plasiyer Kodu Değiştirme İşleminin Çalışmasının Sağlanması**

İhraç kayıtlı satış faturalarında, plasiyer kodu değiştirme işleminin çalışması sağlandı.

**8- İptal Butonlarının, İşlevini Yerine Getirmesi Talebi**

"e-Belge Görüntüleme" ekranında "Basım" butonu ile açılan "Basım Ayarları" ekranına ve "Gelen e-Fatura" için "Uygulama Yanıt" seçeneği ile açılan Kabul/Ret ekranlarına "Vazgeç" butonu eklendi. Bu buton ile, ilgili ekranların işlem yapmadan kapatılması sağlandı.

**STOK**

**Yenilikler**

**1- Seri Sisteminde Son Kullanım Tarihi (SKT) ve FEFO Desteğinin Sağlanması**

"Seri Takibi Kayıtları" ekranına "SKT Güncelle" ve "FEFO Çıkış Seri" butonları eklendi. "Seri Parametreleri" ekranında opsiyonel saha olarak "Son Kullanma Tarihi" seçeneğinin işaretlenmesi durumunda aktif olan bu butonlar ile, "Son Kullanma Tarihi" (SKT) alanının fonksiyonel anlamda kullanılmasını sağlayacak geliştirmeler yapıldı. Bir stokun aynı serileri için tek bir SKT girişi yapılabilir ve "SKT Güncelle" işlemi o stoka ait serinin son kullanma tarihini değiştirmeyi sağlar. Bu işlem, ilgili serinin tüm hareket kayıtlarındaki son kullanma tarihi bilgisini günceller. "FEFO Çıkış Seri" butonu ile de, seri çıkışlarının son kullanma tarihine göre yapılması desteklendi. Çıkış hareketlerinde aktif olan bu buton yardımıyla, son kullanma tarihi en yakın olan serinin ilk çıkması sağlandı.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=noPAfBpP4yY&ab_channel=LogoDestek).

**2- Otomatik Seri Kodu Üretme Ekranında SQL Sorgusu Yazılırken "Stok Kodu" Bilgisinin Parametre Olarak Kullanılması Talebi**

"Otomatik Seri No Üretme Tanımlamaları" ve "Esnek Kodu Üretim Parametreleri" ekranında "Başlangıç Karakteri" alanında iken, farenin sağ tuşu ile ekrana gelen menüye "Stok Kodu Değişkeni" eklendi.
"Stok Kodu Değişkeni" üzerine tıklandığında, imlecin bulunduğu yere "($StokKodu)" ifadesi eklenir. Bu şekilde başlangıç karakteri verildiğinde, seri numarası üretileceği sırada içinde bulunulan stok kodu bilgisinin, üretilecek seri numarasının başlangıç karakteri olarak yazılması sağlandı.

**3- SQL 2005 Kullanan Müşteride DBO.NSF_MIKTARSIZMALIYET Fonksiyonunun Oluşturulamamasından Dolayı SMA Raporunda Ekrana Uyarı Gelmesi**

SQL 2005 sunucusunda DBO.NSF_MIKTARSIZMALIYET fonksiyonunun oluşamamasından dolayı, Serbest Maliyet Ambar Raporu alırken ekrana gelen uyarı kaldırıldı.

**İyileştirmeler**

**1- "Stok Kartı Kayıtları" Ekranındaki "Evrak Ekleme" Alanı Genişliğinin Düzeltilmesi**

"Stok Kartı Kayıtları" ekranındaki "Evrak Ekleme" alanı genişliği ile ilgili düzeltme yapıldı.

**2- Stok Parametrelerinde “Tarihsel Planlama Kayıtları Yapılsın” ve “Şubeler Dahil Maliyet Sistemi” Parametreleri Aynı Anda Kullanıldığında "Şubeler Dahil Maliyet Sistemi" Parametresinin İşaretli Görünmesinin Sağlanması**

Stok - Kayıt - Stok Parametreleri - “Tarihsel Planlama Kayıtları Yapılsın” ve “Şubeler Dahil Maliyet Sistemi” parametreleri aynı anda kullanıldığında, "Şubeler Dahil Maliyet Sistemi" parametresinin işaretli görünmemesi ile ilgili durum düzeltildi.

**3- Ürün Malzeme Maliyeti Oluşturma Çalıştırılırken, "Şubeler Dahil" Seçeneği İşaretlendiğinde, Maliyet Oluşturmanın Sadece Aktif Olan Şubeler İçin Çalışmasının Sağlanması**

Ürün malzeme maliyeti oluşturma çalıştırılırken, "Şubeler Dahil" seçeneği işaretlendiğinde, maliyet oluşturmanın sadece aktif olan şubeler için çalışması sağlandı.

**4- Seri Girişi Ekranında, Opsiyonel Sahalarda Son Kullanım Tarihinde Gelen Uyarının Düzeltilmesi Talebi**

"Seri Girişi" ekranında "Son Kullanma Tarihi" alanı ile ilgili durum düzeltildi.

**YARDIMCI PROGRAMLAR**

**Yenilikler**

**1- Şirket Kopyalama İşlemi Yapıldığında, TBLEDEFTER'e Yeni Şirket Koduyla Birlikte Eski Yıl Satırlarının Aktarılması Talebi**

Yardımcı Programlar - Kayıt - Şirket İşlemleri - "Şirket Kopyalama" işlemi ile; kaynak şirketteki e-Defter kayıtlarının, yeni oluşturulan şirkete aktarılması sağlandı.

**2-** **Etiketlerle İlgili Toplu Yönetim Ekranı Talebi**

Genel - Yardımcı Programlar - İşlemler menüsüne, "Etiket Yönetimi" eklendi.
"Etiket Yönetimi" işlemi ile;
- Etiket Ekle: Mevcut etiket kaydı seçilerek yeni bir etiket ekleme ve birden fazla etiket tipi seçilerek yeni etiket kayıtlarının yapılması,
- Etiket Sil: Seçilen etiket kayıtların silinmesi,
- Etiket Değiştir (Seçili Etiketi Değiştir): Seçili etiket kayıtlarının değiştirilmesi,
- Etiket Değiştir (Tüm Etiketlerini Değiştir): Seçilen etiket kayıtlarının silinerek yeni etiket kaydı eklenmesi sağlandı.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=kkUsIhbKJOA&feature=youtu.be).

**3- Makine Bakım - "Bakım Emirleri" Ekranına, Kullanıcı Tanımlı Saha Desteğinin Getirilmesi Talebi**

Yardımcı Programlar - Kayıt - "Saha Tablo Eşleştirmesi" ekranına, Makine Bakım/Bakım Emirleri tanımlaması eklendi.

**İyileştirmeler**

**1- Oracle'da Saha Tablo Eşleştirmesi Silindiğinde İşlemin Veritabanından da Silinmesi Talebi**

Oracle'da saha tablo eşleştirmesi silindiğinde veritabanından silinmiyordu, düzeltildi.

**MRP**

**Yenilikler**

**1- Kaynak Tanımlama Ekranına Kullanıcı Tanımlı Saha Desteğinin Getirilmesi**

MRP - Kayıt - Kaynak Yönetimi - "Kaynak Tanımlama" ekranına "Saha-Tablo Eşleştirmesi" özelliği eklendi.

**2- Makine Tanımlama Ekranına Kullanıcı Tanımlı Saha Desteği Getirilmesi**

MRP - "Makine Tanımlama" ekranlarına "Ek Saha" alanları eklendi.

**3- Çizelgeleme Sonuç Ekranında, Gantt üzerinde Çizelgelenen İş Emrinin Üzerine Gelindiğinde, İş Emri Teslim Tarihinin Yanında Sipariş Teslim Tarihinin de Olması Talebi**

Gantt ekranında iken fare ile "İş Emri" üzerine gelindiğinde açılan bilgi penceresinde, iş emrinin sipariş ile bağlantılı olması durumunda, "Müşteri Sipariş No", "Sipariş Sıra No", "Sipariş Miktarı" ve "Sipariş Teslim Tarihi" bilgilerinin gösterilmesi sağlandı.

**4- "Sipariş İşlemlerini Gerçekleştir " Buton İsminin, "Talep İşlemlerini Gerçekleştir" Şeklinde Düzenlenmesi ve Teslim Tarihini Düzelt, Miktar Düzelt Gibi Butonların Belge Düzeltme Önerisi Olmadığında Pasif Hale Getirilmesi Talebi**

"Malzeme Gereksiniminden Talep/Sipariş/İş Emri Oluşturma" ekranlarının "Dengeleme Sonuç Sayfası" sekmesinde farenin sağ tuşu ile ekrana gelen menüye; "Grubu Seç", "Grubun Seçimini Kaldır", "Tüm Kırılımları Aç" ve "Tüm Kırılımları Topla" seçenekleri eklendi.
"Belge Düzeltme" önerisi olmadığında, "Teslim Tarihini Düzelt", "Miktar Düzelt" ve "Hepsi" butonlarının pasif hale getirilmesi sağlandı.

**5- Kazan Tipli Makine İçin Hazırlık Süresi Desteği**

"Makine Tanımlama" ekranlarında kazan tipli makineler için hazırlık süreleri dikkate alınarak "Çizelgeleme" yapılması sağlandı.

**İyileştirmeler**

**1- Oluşan Sipariş ya da Talep Belgelerinde, Satırdaki Depo Kodunun Stok Kartındaki Depo Kodundan Alınması Gerekirken, Ekranda Girilen Depo Kodundan Alması**

MRP - İşlemler - "Malzeme Gereksinimden Sipariş Oluşturma" işleminde, satıcı siparişi dengelerken "Yeni Sipariş Bilgileri" sekmesinde yer alan "Stok Depo Kullan" parametresinin işaretlendiği ve "Depo Kodunun" seçildiği durumlarda, "Satıcı Siparişi" oluşturulurken "Stok Depo Kodu" dikkate alınmıyordu. "Stok Depo Kullan" parametresinin işaretlenmesi durumunda, stok kartındaki depo kodunun getirilmesi sağlandı.

**2-** **"Gereksinim Planlama Çalıştır" ve "Kapasite Kullanımları Kontrol Edilsin" Parametreleri İşaretlenerek MRP Raporu Alındığında "Duplicates not allowed" Uyarısının Gelmesi**

"Gereksinim Planlama Çalıştır" ve "Kapasite Kullanımları Kontrol Edilsin" parametrelerinin işaretlendiği durumlarda, "Malzeme Gereksinim Planlama" çalıştırıldığında ekrana gelen "Duplicates not allowed" uyarısı kaldırıldı.

**3- Makine Tanımlama - "Grup Kodu" Rehberine Gelen Kayıtlar, Grup Kodu Tanımlı Makine Sayısı Kadar Çoklu Değer Olarak Gelmemesinin Sağlanması**

MRP - Kayıt - Makine Tanımlama - "Grup Kodu" rehberine gelen kayıtlar, grup kodu tanımlı makine sayısı kadar çoklu değer olarak geliyordu, düzeltildi.

**4- Minimum Sipariş Miktarı Olan Bir Hammadde İçin Mrp Raporu Alındığında, Satınalma Sipariş Miktarınının Doğru Hesaplanmasının Sağlanması**

"Satıcı Sipariş Kontrol" Parametresinin işaretli ve "Malzeme Gereksinim Planlama" çalıştırıldığı durumlarda; Stok-Planlama Kayıtlarında Minimum Sipariş Miktarı tanımlı bir stok kodunun satınalma net gereksinim miktarının doğru hesaplanması sağlandı.

**5- Çizelgeleme Sırasında, Makine-Kaynak Eşleştirmesi Ekranında Belirtilen Kaynak Sayısı Kadar Kullanılmasının Sağlanması**

Kaynak Grubu ile Makine-Kaynak Eşleştirmesi yapıldığında, bir kaynak grubuna bağlı birden fazla kaynak tanımlanıyor ve bu kaynaklar Makine-Kaynak Eşleştirmesine, kaynak grubuna göre birden fazla kaynağın kullanılması şeklinde belirtiliyordu. Çizelgeleme çalıştırıldığında ise sistem, kaynak grubuna bağlı tek bir kaynaktan çizelgeleme yapıyordu. İlgili durum düzeltilerek, Makine-Kaynak Eşleştirmesi ekranında belirtilen kaynak sayısı kadar kullanılması sağlandı.

**ÜRETİM**

**Yenilikler**

**1- İş Emirleri MRP'den Açıldığında ve Referans İş Emri Sahaları Dolu Olduğunda, Tepe Mamulün İş Emrinde Tarih ve Teslim Tarihleri Değiştirilince, Bağlı İş Emirlerinin de Tarih ve Teslim Tarihlerinin Değişmesi Talebi**

İş emirlerinde ''Tarih" ve "Teslim Tarihi" güncellendiği zaman, ilgili iş emirlerine bağlı alt iş emirlerinin de ''Tarih" ve "Teslim Tarihi" alanlarının güncellenmesi sağlandı.

**2- Üretim - Kayıt - Planlanan Bileşen Değişiklikleri - Yeni Bileşen Bilgi - "Miktar" Alanının Her Zaman "Sabit" Olacak Şekilde İşaretli Gelmesi Talebi**

Üretim - Kayıt - Planlanan Bileşen Değişiklikleri - Yeni Bileşen Bilgi - "Miktar" alanının her zaman "Sabit" olarak işaretli şekilde gelmesi sağlandı.

**3- Üretim Sonu Kaydı Ekranındaki Sipariş/İş Emri Rehberinde Stok Kodu Filtresi Verilerek Birden fazla Belge Seçildiğinde, Her Filtre Değişiminde Bir Önceki Seçilen Belgenin Kaybolmaması Talebi**

Üretim Sonu Kaydı - İş Emri/Sipariş No rehberinde birden fazla kayıt için filtre verilip seçim yapıldığında, tüm kayıt seçimlerinin gelmesi sağlandı.

**4-** **Kazan Tipli Makine İçin Hazırlık Süresi Desteği**

"Makine Tanımlama" ekranlarında kazan tipli makineler için hazırlık süreleri dikkate alınarak "Çizelgeleme" yapılması sağlandı.

**5-** **Üretim Sonu Kaydı Girildiğinde Parti Büyüklüğüne Göre Serilerin Otomatik Oluşturulması Talebi**

"Seri Parametreleri" ekranında yer alan "Seri Kodu Girişler İçin Otomatik Hesaplansın" parametresinin altına "Üretim Sonu Kaydında Girişler İçin Parti Büyüklüğü Kullanılsın" parametresi,
"Seri Kodu Çıkışlar İçin Otomatik Hesaplansın" parametresinin altına da "Üretim Sonu Kaydında Çıkışlar İçin Parti Büyüklüğü Kullanılsın" parametresi eklendi.
Yeni eklenen parametreler ile birlikte, Stok Kartı Kayıtları - Seri Takibi - "Seri Kodu Girişler İçin Otomatik Hesaplansın" veya "Seri Kodu Çıkışlar İçin Otomatik Hesaplansın" parametrelerinin de işaretlenmesi ile, serili bir stok için "Serbest Üretim Sonu Kaydı" oluşturulur.
Giriş ve Çıkış hareketleri için üretim sonu miktarı, stok planlama kayıtlarında parti büyüklüğü, bağlı otomatik seri kayıtları oluşturur.

**6- Makine Tanımlama Ekranına, Alış Tarihi Bilgisi Alanının Eklenmesi Talebi**

MRP - Kayıt - "Makine Tanımlama" ekranına, "Alış Tarihi" alanı eklendi.

**7- Üretimde Yan Ürün Desteğiyle İlgili İyileştirme Talebi**

Üretim ekranlarında yan ürün desteği sağlandı.

1- Üretim - Kayıt - "Reçete Kaydı" Ekranında Yan Ürün Desteği: Yan ürün şeklinde bir bileşen tipi seçeneği eklendi. Reçete kaydı oluştururken yan ürün tipli bileşenin de eklenmesi sağlandı.
2- Üretim - Kayıt - "Ürün Konfigüratörü" Ekranında Yan Ürün Desteği: Yan ürün şeklinde bir bileşen tipi seçeneği eklendi. Ürün ağacı oluştururken, yan ürün tipli bileşenin de eklenmesi sağlandı.
3- Üretim - Kayıt - "İş Emri" Ekranında Yan Ürün Desteği: İş emri kaydı sırasında "Reçeteyi Kaydet" seçeneği işaretli ise, yan ürün tipli bileşen için de kaydedilmesi sağlandı.
4- Üretim - Kayıt - "İş Emri Malzeme Rezervasyonu" Ekranında Yan Ürün Desteği: İş emrinden reçete getirilirken, yan ürün tipli bileşenin getirilmemesi sağlandı.
5- Üretim - Kayıt - "Üretim Sonu Kaydı" Ekranları Yan Ürün Desteği:
5.1. Üretim - Kayıt - "Serbest Üretim Sonu Kaydı" ekranlarında yan ürün tipli bileşen hareketi için giriş hareketi atılması yapılması sağlandı. Yan ürün tipi için atılan giriş hareketinin, Miktar Depo Kodu bilgisinin değiştirilmesi fakat, Stok Kodu ve Yapılandırma Kodu bilgilerinin değiştirilmemesi sağlandı.
5.2. Üretim - Kayıt - "Üretim Sonu Kaydı" ekranında, yan ürün tipli bileşen hareketi için giriş hareketi atılması sağlandı.
5.3. Üretim - Kayıt - "Ters Üretim Sonu Kaydı" ekranında, yan ürün tipli bileşenler için giriş hareketi atılmaması sağlandı.
5.4. Üretim - Kayıt - "Mamul Parçalama" ekranında, yan ürün tipli bileşenler için giriş hareketi atılmaması sağlandı.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=viGsx1UHQ4I&ab_channel=LogoDestek).

**İyileştirmeler**

**1- Reçete Listesi Raporunda, Stok Kodu Sütununun Üzerinde İken "Kayıt Detayı İçin Çift Tıklayınız" Özelliğine Tıklandığında Stok Kartlarının Açılmaması**

Üretim - Raporlar - "Reçete Listesi" raporu alındıktan sonra "Stok Kodu" sütununun üzerinde iken "Kayıt Detayı İçin Çift Tıklayınız" özelliğine tıklandığında, "Stok Kartı Kayıtları" ekranından seçilen stok verilerinin gelmesi sağlandı.

**2- Fabrika Son Durum Ekranında Bitiş Tarihi Girilen Alanın Çalışmaması**

Üretim Akış Kontrol - İşlemler - "Fabrika Son Durumu" ekranında bulunan "Bitiş Tarihi' alanının dikkate alınmaması ile ilgili durum düzeltildi.

**3- Gelişmiş Rapor Alırken "Object Doesn't Support This Property or Method: 'RaporBook.GetCellFormat' EOleException" Uyarısının Gelmesi**

"Tek Seviyeli Reçete Listesi" ekranına yazılan script kodun, "Gelişmiş Rapor" alındığında verdiği uyarı kaldırıldı.

**4- İstasyon Tanımlama Ekranında, Departman Kodu Rehberinin Açılması Talebi**

MRP - Kayıt - "İş İstasyonu Tanımlama" ekranında yer alan "Departman Kodu" rehberinde kayıtlar ekrana gelmiyordu, gelmesi sağlandı.

**5- SBOM Çalıştırıldığında, Güncel Sette Kaydetme İşleminin Yapılmasının Sağlanması**

"Süper Reçete" kullanılması durumunda, "SBOM" butonu altında "Esnek Yapılandırma Sihirbazı" ekranında yer alan "SBOM" butonu (SBOM Reçete Ekranı) ekrana gelmiyordu, düzeltildi.

**ÜRETİM, AKIŞ KONTROL**

**Yenilikler**

**1- Standart Pakette Script Desteğinin Pasif Gelmesi Talebi**

Script desteği sadece "Enterprise" paketinde bulunduğu için, "Standart" paketin iş akış kayıtlarında "Koşul Tanımlama" çalışmıyordu. "Koşul Tanımlamanın" sadece "Enterprise" paketini kullanan müşterilerde görünmesi sağlandı.

**2- Makine Tanımlama Ekranına, Alış Tarihi Bilgisi Alanının Eklenmesi Talebi**

Üretim, Akış Kontrol - Kayıt - "Makine Tanımlama" ekranına, "Alış Tarihi" alanı eklendi.

**3- UakToUsk İşleminin Rest Tarafında da Desteklenmesi Talebi**

Üretim, Akış Kontrol - İşlemler - "Üretim Sonu Kaydı" işlemi Rest tarafında da desteklendi.

**GENEL**

**Yenilikler**

**1- Bakım Emrini Geriye Dönük Bir Kullanıcının Kilitlemesi ve Diğer Kullanıcıların Kilitlenen Bakım Emrini Değiştirememesi Talebi**

Ekranların üstündeki navigatör üzerine "Belge Kilitle" ismiyle yeni bir buton eklendi. Bu butona tıklandığında, seçili olan kaydın kilitlenmesi sağlandı. Kilitli belgeyi herkes görebilir fakat, sadece admin veya kilitleyen kullanıcı değiştirebilir. Bu özellik şimdilik, "Bakım Emirleri" ekranında desteklendi.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=5f2WCW73kh8&ab_channel=LogoDestek).

**2- Gezgin, Menü Ağacı ve Pencere Başlık Sağ Tık Menüsüne "Etiketleme Sihirbazı" Seçeneğinin Eklenmesi Talebi**

Gezgin, menü ağacı ve pencere başlık sağ tık menüsüne "Etiketleme Sihirbazı" seçeneği eklendi.

**3- "Genel Arama Yapılsın" Özelliği İçin Arama Yapılacak Dataların Arasında Çoklu Seçim Yapılması Talebi**

Ekstra menüsünün altındaki "Genel Arama Yapılsın" seçeneğine tıklandığında, arama yapılacak yerlerin seçilmesi sağlandı. Genel aramada Fatura, Sipariş ve İrsaliye belgelerinin aranması desteklendi. Aramaya "Cari Adı" yazıldığında, siparişler arasında arama yapılması sağlandı.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=uL-teFqtpNI&ab_channel=LogoDestek).

**4- Program Genelindeki Yetki Uyarılarının Düzenlenmesi Talebi**

Belge araması yapıldığında, sonuç olarak girilen son 20 belge ekrana gelir. İşlem yapılan modül ve program için gerekli kullanıcı yetkisi bulunmadığında alınan uyarı mesajına, modül ve program numarası ile birlikte modül ve program adı da eklenerek, uyarı mesajının daha anlaşılır olması sağlandı.

**5-** **Log'un Şirket Veri Tabanından Çıkartılması (Oracle Desteği)**

"Log Veri Tabanı Oluşturma" işleminin, Oracle kullanan Netsis ürünlerinde de çalışması sağlandı.

**6- Wings'in Timeout Süresi dolup Prgram Kapandığında, Sunucuda EphesusWeb Çalışmayı Durdurdu Uyarısının Gelmesi**

Kullanıcı "timeout" süresini doldurduğunda, sunucuda EphesusWeb.exe'nin uyarı vererek sonlanması ile ilgili durum düzeltildi.

**7- Bedelsiz Olarak Kapatılan İhracat İşlemlerinin, Fatura Raporlarında Bedelli Olarak Görünmemesinin Sağlanması**

Fatura-İrsaliye İzleme ve Fatura-İrsaliye İcmali ekranlarının "Ön Sorgu" sekmelerine, "Bedelsiz İhracat Faturaları Hariç Tutulsun" seçeneği eklendi. Böylece, raporlarda bedelsiz olarak kapatılan İhracat faturalarının listelenmemesi sağlandı.

**8- e-Fatura Dizaynlarından Oluşturulan XML Belgesinde, Fatura KDV Tutarının 0 (Sıfır) Olması Durumunda, Kesilen Faturaların Firmalar Tarafından Reddedilmesi**

e-Fatura dizaynlarından oluşturulan XML belgesinde, KDV tutarının sıfır olması durumunda, XML belgesindeki percent etiketinin yazılmaması ile ilgili durum düzeltildi.

**İyileştirmeler**

**1- NetUpdate İle Güncelleme Yapılacağı Zaman, Agent Servisi Çalışır Halde İken Güncelleme Yapılması Talebi**

NetUpdate.exe ile güncelleme yapılacağı zaman, agent servisi çalışır halde iken güncelleme yapılamıyordu, düzeltildi.

**2-** **Standart Raporlarda Sıralama Sekmesinde Sıralama Yapıldığında, Kümüle Döküm Seçeneği Evet Olarak İşaretlenerek Saklanması İstendiğinde ve Rapor Oku Butonu Kullanıldığında Sakla Butonunun Görevini Yerine Getirmesi Talebi**

Rapor ekranlarında yer alan "Sakla" butonu "Kırılımda Kayıt Sayısı" ve "Kümüle Döküm" alanlarını saklamıyordu, düzeltildi.

**3-** **SMARTCODE.DivCount'un Yatay Görünümde 0 Değerini Döndürmesi**

Akıllı kodda SMARTCODE.DivCount fonksiyonu yatay görünümde çalışmıyordu, düzeltildi.

**4- Mizan Alınırken Yazıcı Seçeneklerinde PDF Dosya Yolu yazılarak Rapor Alındığında, PDF Dosyasının Verilen Dizinde Oluşarak Dosyanın Açılmasının Sağlanması**

Gelişmiş rapor alındığında PDF basımının çalıştığına dair uyarı eklendi ve klasik raporlarda PDF oluşmaması sağlandı.

**5- Satılan Demirbaşların, Demirbaş Raporunda Doğru Görünmesinin Sağlanması**

Özel dönem kullanılan durumlarda, satılan demirbaşların demirbaş raporunda doğru görünmemesi ile ilgili durum düzeltildi.

**MAKİNE BAKIM**

**Yenilikler**

**1- Makine Bakım Modülünde Toplu Basımın Desteklenmesi Talebi**

Üretim - Makine Bakım - İşlemler menüsüne, "Toplu Bakım Emri Basımı" eklendi. Bu ekran ile, toplu bakım emri basımının yapılması sağlandı.

**DIŞ TİCARET**

**Yenilikler**

**1- Satırlara DIIB Girişi Yapılırken, Her Satır İçin Birden Fazla DIIB Eşleştirmesi Yapılması Talebi**

Dış Ticaret Parametreleri - İhracat Parametreleri sekmesine "Çoklu Diib Uygulaması" seçeneği eklendi. Parametre işaretlendiğinde, Dış Ticaret - İşlemler - İhracat İşlemleri - Dosya İşlemleri ekranındaki "Detay Gösterme" ekranı üzerinde iken farenin sağ tuşu ile ekrana gelen menüden "DİİB Bilgi Girişi" ve "Kalem Detay Bilgileri" seçenekleri kullanılarak, bir kaleme birden fazla diib no atanması desteklendi. Parametre işaretli olduğunda, ilgili ekranlarda diib no rehberi yerine "Çoklu Diib Girişi" ekranı açılarak birden fazla diib no seçimi yapılması sağlandı.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=LK7EfC9hFJ0&ab_channel=LogoDestek).

**2-****Çeki Listesi Kontrol Raporunun, Çeki Listesi Ekranında Farenin Sağ Tuşu İle Açılmasının Sağlanması**

Dış Ticaret - Raporlar - "Çeki Listesi Kontrol Raporu" ekranının, Dış Ticaret - İşlemler - İhracat İşlemleri - Dosya İşlemleri - Detay Gösterme - "Çeki Listesi" sekmesinde farenin sağ tuşu ile açılması sağlandı.

**3- İthalat/İhracat Masraf Dekont Girişinde, İlgili Masrafın Dağıtım Detayının Belirlenmesinin Sağlanması**

Dış Ticaret - İşlemler - İthalat İşlemleri - "İthalat Masraf Dekont Kayıtları" ekranına "Masraf Dağıtım" butonu eklendi. Masraf dağıtımı ile, stok bazında masraf dağıtımının yapılması sağlandı.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=PUTMD61cxc8&ab_channel=LogoDestek).

**İyileştirmeler**

**1- Dış Ticaret Modülünde İthalat Kapatma Yapılırken, Masraf Birim Ağırlığa Göre Hesaplandığında TL Tutarın Doğru Hesaplanmasının Sağlanması**

"Dış Ticaret" modülünden ithalat kapatma yapılırken, "İthalat Masraflarının Dağıtılması Birim Ağırlığa Göre Yapılsın" seçeneği işaretlendiğinde, TL tutarların hesaplanması düzeltildi.

**2- İthalat Mal Kabul İşleminde Cari İsmin Gridde Doğru Yazılmasının Sağlanması**

Dış Ticaret - İşlemler - İthalat İşlemleri - "İthalat Mal Kabul" ekranındaki gride "Cari İsim" kolonu eklendi.

**3- İthalat Dosya İşlemlerinin "Genel" Sekmesindeki Gride, Gümrük Beyanname Bilgileri Kadar Mükerrer Gelen Kayıtların Düzeltilmesi**

İthalat Dosya İşlemlerinde, gridde bazı dosyalar mükerrer görünüyordu, düzeltildi.

**İTHALAT**

**Yenilikler**

**1- İthalatta Dövizli İskonto Desteği**

'IHRACAT','PROFORMAUSERGENELISKONTO' özel parametresinin ithalat işlemleri için de çalışması sağlandı. İthalat - İşlemler - İthalat İşlemleri - Dosya İşlemleri - "Faturalarım" sekmesindeki gride, dış ticaretteki gibi "Düzenle" seçeneği eklendi. Toplamlar sekmesinden genel iskonto yapılması sağlandı. "İthalat Kapatma" irsaliye tutarları üzerinden yapıldığı için, irsaliye oluşturmadan önce proformada iskonto yapılması gerekir.

**KALİTE KONTROL**

**Yenilikler**

**1- Departman Tanım Ekranında Kabul-Red-Şartlı Kabul ve Hurda DAT İşlemleri İçin Fiş No Seri Tanımlama Desteğinin Sağlanması**

Departman bazında tanımlanacak belge seri bilgilerinin DAT veya USK işlemi sırasında kullanılması sağlandı.
Kalite Kontrol - Kayıt - "Kalite Kontrol Departman Girişi" ekranına "Kabul Seri", "Red Seri", "Hurda Seri", "Şartlı Kabul Seri’" alanları eklendi.
Kalite Kontrol - İşlemler - "DAT Kayıtları" ve Kalite Kontrol - İşlemler - "Üretim Sonu Kayıtları" ekranlarına “Fiş No Serisi Departmandan Getirilsin” seçeneği eklendi. Böylece, oluşacak belge serisinin departman bazında tanımlanan seri koduna göre oluşturulması sağlandı.

**2- Kalite Kontrol Kaydı İşleminde Belge Numarası Rehberinin, Seçilen Departmana Uygun Olan Stoklar İçin Listelenmesi Talebi**

Kalite Kontrol Parametreleri ekranına, "Kalite Kontrol Kaydında Grup Eşleştirme Bilgileri Kontrol Edilsin" seçeneği eklendi. Bu parametre işaretlendiğinde, kalite kontrol kaydında belge numarası rehberine belgelerin "Stok-Cari Grup Eşleştirme" ile eşleştirilen kayıtlara göre getirilmesi sağlandı.

**3- Kalite Kontrol Kaydı Ölçüm Bilgileri Ekranında, Seri Takibi Olan Bir Ürüne Serisiz Bilgi Girişinin Yapılmaması Talebi**

"Kalite Kontrol Parametreleri" ekranına, "Kalite Kontrol Kayıt Kapamada Seri-Lot Girişleri Kontrol Edilsin" parametresi eklendi. Parametre işaretlendikten sonra "Kalite Kontrol Kaydı" ekranından "Kayıt Kapama" butonuna tıklandığında, seri takibi yapılan stok kodları için ölçüm hareketlerinde yer alan "Seri No" alanının kontrol edilerek, seri bilgisi girilmeyen kayıt işlemlerinin durdurulması sağlandı.
"Kalite Kontrol Hareketleri Otomatik Oluşsun" parametresinin işaretlendiği durumlarda, ölçüm hareketleri otomatik aktarıldığı için, bu aşamada seri kontrolü yapılmaz.

**MUHASEBE**

**Yenilikler**

**1- Fatura Modülünden Gelen Faturalarda Tarih Sorgusunun Fiili Tarih Üzerinden Yapılmasının Sağlanması**

MUHASEBE,BFORMFIILITARIH özel parametresiyle BA-BS raporları oluşturulurken, faturaların fiili tarihe göre raporlanması desteklendi.

**2- "Yansıtma Girişi" Ekranında Olmayan Diğer Gider Hesaplarının Yansıtılması Talebi**

Muhasebe - İşlemler - Dönem Sonu İşlemleri - "Yansıtma Girişi (Diğer Hesaplar)" ve "Yansıtma Fişi Oluşturma (Diğer Hesaplar)" menüleri eklendi. Böylece, "Yansıtma Girişi" ekranında olmayan diğer gider hesaplarının da yansıtılması sağlandı.

**3- RES_YEVM_NO Alanı 0 Olan Kayıtların E-Defter Kontrolünün Sağlanması**

e-Defter oluşturulan aya ait yevmiye fişlerinde (resmi yevmiye madde numarasının bulunmaması durumunda) e-defter oluşturma aşamasında, "Belirtilen dönem için yevmiye madde numarası oluşturulmamış kayıtlar tespit edildi. e-Defter hazırlık işlemini çalıştırınız." bilgi mesajının getirilerek, işleme devam edilmemesi sağlandı.

**4- Dönemi Biten Defterlerde e-Defter Onaylama İşleminde Ekrana Gelen Uyarının "Mükellef ve Düzenleyen Bilgilerinde Dönem Başlangıç\\Bitiş Tarihlerini Güncelleyiniz" Olarak Verilmesi Talebi**

"e-Defter Oluşturma" ekranında "Yıl" bilgisinin yanına, alan ile ilgili açıklama yazıldı.

**5- 2019 Ocak Ayı İçin Vergi Detaysız e-Defter Oluşturulması İstendiğinde, Defter Raporu İçin "Vergi Detayını Temsil Edecek gl-cor:entryheader elemaı Sayısı 1 Olmalıdır" Uyarısının Alınmamasının Sağlanması**

"Vergi Detaysız e-Defter" işleminde "Defter Raporu" oluşturulması desteklendi.

**6- Muhtasar Beyannamesi - Kültür Yatırımları ve Girişimlerine İlişkin Bildirim Eki Desteğinin Sağlanması**

Muhtasar Parametreleri - Beyanname ekranına, "Kültür Yatırımları Ve Girişimlerine İlişkin Bildirim Eki" eklendi.

**İyileştirmeler**

**1- Muhtasar Beyanname Parametrelerinde Vergi Sorumlusunun Vergi Kimlik No Alanına Değer Girilmesinin Sağlanması**

Muhtasar Parametreleri - Beyanname sekmesinde yer alan "Vergi Sorumlusunun Vergi Kimlik No" alanına değer girilemiyordu, düzeltildi.

**2- Tarih Bazında Kilitli Kullanıcının Eski Aylara Ait Yevmiye Fişlerini F7 ile Silmesinin Engellenmesi**

Tüm kullanıcılara "Tarih Kilidi" yapılmasına rağmen, yönetici olmayan kullanıcının yevmiye fişini F7 tuşu ile silmesi ile ilgili durum düzeltildi.

**3- Defteri Kebir ve Yevmiye Defterinde Toplam Sayfayı Gösteren Ekranın Bazen Açılmaması İle İlgili Durumun Düzeltilmesi Talebi**

Defteri Kebir ve Yevmiye Defterinde toplam sayfayı gösteren ekranın bazen açılmaması ile ilgili durum düzeltildi.

**4- Şubeli Muhasebe Kapalı İken; İlgili Aya İlk Kayıt Atıldığında, Şubeli Muhasebe Açıkmış Gibi Fiş Numarası Vermesinin Düzeltilmesi**

Şubeli muhasebe kapalı iken; ilgili aya ilk kayıt atıldığında, şubeli muhasebe açıkmış gibi fiş numarası veriyordu, düzeltildi.

**TALEP TEKLİF**

**Yenilikler**

**1- Satın Alma Talep Teklifleştirme Bilgi Gösterimi Sekmesinde Filtreleme Yapılması Talebi**

Satın Alma Talep Teklifleştirme - "Bilgi Gösterim" sekmesinde akıllı grid desteklendi.

**2- Talep ve Teklif Ekranlarında Excel Desteğinin Sağlanması**

Excel dosyasından "Sürükle Bırak" özelliği ile hızlı veri aktarımı ve güncellemesi işlemi, Talep-Teklif Modülü kayıt ekranlarında (Satış Talep, Satış Teklif, Satın Alma Talep, Satın Alma Teklif) da desteklendi.

**DEKONT**

**Yenilikler**

**1- Genel Dekont Kaydında Stok Seçilip Referans Kodu Girildiğinde, Seçilen Referans Bilgisinin Stok Hareket Kayıtlarına Gitmesinin Sağlanması**

"Genel Dekont Kaydı" ekranında Stok Kodu seçilip Referans Kodu girildiğinde, TBLSTHAR tablosu S_YEDEK1 alanına, girilen referans kodunun eklenmesi sağlandı.

**2-** **Genel Dekont Kaydı ve Çek/Senet Bordro İşlemlerinde, Sadece Kayıt Yetkisi Olan Bir Kullanıcı Dekont Kaydı Oluşturduğunda, Dekontu Tamamlamadan Satırlara Müdahale Edilmesinin Sağlanması**

Genel Dekont Kaydı sırasında sadece kayıt yetkisi olan bir kullanıcı "Tamamla" butonunu kullanmamasına rağmen girilen kayıtta değişiklik yapamıyordu, düzeltildi.

**İyileştirmeler**

**1- "Genel Dekont Kaydı" Ekranında, Seri Takibi Yapılan Stok Kaleminin Miktar ve Serisinde Düzenleme Yapıldığında Ekrana Gelen Uyarının Kaldırılmasının Sağlanması**

"Genel Dekont Kaydı" ekranında, seri takibi yapılan stok kaleminin miktar ve serisinde düzenleme yapıldığında ekrana gelen uyarı kaldırıldı.

**ENTEGRASYON**

**Yenilikler**

**1- Entegrasyon Kodları Fatura Ek Maliyet Sekmesinde İade ÖTV Hesabına Yazılan Kodun Otomatik Olarak Formatlanmasının Sağlanması**

Muhasebe - Kayıt - Muhasebe Parametreleri - "Seviye Takibi Yapılsın" parametresi, hesap kodlarını belirtilen seviyelere göre kodlar. Entegre - Kayıt - Entegrasyon Kodları - Fatura Ek Maliyet - "İade ÖTV Hesabı" alanında da, hesap kodlarının seviye takibine göre kodlanması sağlandı.

**BANKA**

**Yenilikler**

**1- Gridde CTRL+HOME VEYA CTRL+END Tuşlarına Basıldığında, Farenin Sağ Tuşu İle Ekrana Gelen Gönder Seçeneğinin Kaybolmamasının Sağlanması**

"Banka Hesap Hareketleri" ekranında grid üzerinde CTRL+HOME veya CTRL+END kombinasyonları kullanıldıktan sonra, kayıtlar üzerine farenin sağ tuşu ile tıklandığında, "Gönder" seçeneğinin pasif gelmesi ile ilgili durum düzeltildi.

**2-** **Dekont İşlem Tipindeki Kayıtları Aktarırken Referans Kodunun Sorulması ve Aktarılan Dekonta Girildiği Zaman Referans Kodunun Boş Gelmemesinin Sağlanması**

Banka - Kayıt - MT940 Kayıtları - "MT940 Entegrasyonu" ekranında belge tipi "Genel Dekont" olan kayıtlar için kalem bazlı proje kodu ve referans kodu girişi yapılması sağlandı. Aktarım sırasında açılan "Gerekli Belge Bilgileri" ekranı üzerinden de referans kodu girişinin yapılması desteklendi.

**İyileştirmeler**

**1- MT940 Entegrasyonu Transfer Bilgileri Sekmesinde Ek Bilgi Panelinin Düzgün Görünmesinin Sağlanması**

Banka - Kayıt - MT940 Kayıtları - MT940 Entegrasyonu - "Transfer Bilgileri" sekmesinde yer alan "Ek Bilgi" panelinin düzgün görünmesi sağlandı.

**2-** **MT940 Entegrasyonu Ekranında Dosya Seç Butonuna Tıklandığında Açılan Windows Dosya Seçme Penceresinin Başka Pencerelerin Arkasında Kalmamasının Sağlanması**

Banka - Kayıt - MT940 Kayıtları - "MT940 Entegrasyonu" ekranında "Dosya Seç" butonuna tıklanması ile açılan ekranın, başka pencerelerin arkasında kalmaması sağlandı.

**3-** **Uzun ve Orta Vadeli Kredinin İlk Taksit Ödemesinde, Banka Hareketine Faiz Oranının Aktarılmasının Sağlanması**

Uzun vadeli kredilerin ilk taksit ödemesinde, banka hareketine faiz oranı atılamıyordu, düzeltildi.

**4-** **Uzun ve Orta Vadeli Kredilerde, İlk Taksitin Banka Hareketinde Yer Alan "Türü", "Vade Tarihi" ve "Efektif Tarihi" Alanlarına Doğru Değerlerin Gelmesinin Sağlanması**

Uzun ve orta vadeli kredilerde, ilk taksitin banka hareketinde yer alan "Türü", "Vade Tarihi" ve "Efektif Tarihi" alanlarına doğru değerlerin gelmesi sağlandı.

**5- MT940 İle Programda Çek Tahsil Oluşturulduğunda Çek İşlemi Silinirken, Banka Hareketlerinin de Silinmesinin Sağlanması**

MT940 entegrasyonu ile oluşan çek tahsil kaydı silindiğinde, banka hareketi silinmiyordu, düzeltildi.

**KASA**

**Yenilikler**

**1- Kasa Kayıtları - Transfer İşleminde Referans Kodunun Girilmesinin Sağlanması**

Kasa - Kayıt - Kasa Kayıtları - Transfer sekmesine, "Referans Kodu" alanı eklendi. "Referans Kodu" alanı, "Referans Uygulaması" açık olduğunda ve aktif hesaplar için referans takibi yapıldığında aktif hale gelir.

**MALİYET MUHASEBESİ**

**İyileştirmeler**

**1- Maliyet Hesaplatma Çalıştırıldıktan Sonra Oluşan Yevmiye Fişi Kontrol Edildiğinde, İki Ayrı Yarı Mamule Ait Borç Kaydına Bağlı Miktarın Doğru Aktarılmasının Sağlanması**

Aynı ana gruba bağlı farklı iki yarı mamule, mamul grubu tanımlamasında aynı yarı mamul hesabı tanımlandığında, "Maliyet Hesaplatma" sonucu oluşan yevmiye fişinde oluşan miktar farkı ile ilgili durum düzeltildi.

**2- Üretimde Yan Ürün Desteği İle İlgili İyileştirme Talebi**

Muhasebe - Maliyet Muhasebesi Desteği: Maliyet hesaplatma işleminde, yan ürün tipli bileşenler için maliyet hesabının yapılması sağlandı.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=l01vljZn1Aw&feature=youtu.be).

**LOG**

**İyileştirmeler**

**1- Oracle'da Log Raporuna Düzeltme Kayıtlarının Eski Halinin Aktarılmasının Sağlanması**

Oracle'da log raporuna eski değerin aktarılması sağlandı. (Seti güncelledikten sonra log triggerlarının tekrar oluşturulması gerekiyor).

**RAPOR**

**İyileştirmeler**

**1- Oracle'da "Satıcı 12 aylık Alış Raporunda" Dosya Sahalarının Doğru Gelmesinin Sağlanması**

Oracle'da "Satıcı 12 aylık Alış Raporunda" dosya alanları yanlış geliyordu, düzeltildi.

**MÜŞTERİ ÇEKLERİ**

**İyileştirmeler**

**1- "Banka Bilgisi Basılsın" ve "Vade Tarihi (Sıralama)" Parametrelerinin İşaretlendiği Durumlarda, "Ay Toplamının" Doğru Sütunda Listelenmesinin Sağlanması**

Müşteri Çekleri - Raporlar - Tahsildeki Çekler Listesi - Genel Kısıtlar - "Banka Bilgisi Basılsın" ve "Vade Tarihi (Sıralama)" parametrelerinin işaretlendiği durumlarda, "Ay Toplamının" yanlış sütunda listelenmesi ile ilgili durum düzeltildi.

**DİNAMİK DEPO**
**İyileştirmeler**

**1- DAT Kaydı Girildikten Sonra Serili Bir Stok İçin "Hücre Toplama" İşlemi Yapılırken, "Hücre Kodu" Rehberine DAT Kaydının Çıkış Deposunda Bulunan Hücre-Stok Miktarlarının Getirilmesinin Sağlanması**

Dinamik Depo - Kayıt - Dinamik Depo Parametreleri - "Seri Bilgisi Depoda Sorulsun" parametresinin işaretlendiği ve serili bir stok için "Depolar Arası Transfer" kaydının girildiği durumlarda, DAT kaydı girildikten sonra "Hücre Toplama" işlemi yapılırken "Hücre Kodu" rehberi boş geliyordu. "Hücre Kodu" rehberine, DAT kaydının çıkış deposunda bulunan hücre-stok miktarlarının getirilmesi sağlandı.

**2- Bakiyesi Sıfır Olan Stoklar İçin, Dinamik Depo Sayım Farkını Hücre Hareketlerine İşleme Sırasında Ekrana Gelen Uyarının Kaldırılmasının Sağlanması**

Bakiyesi sıfır olan stoklar için, dinamik depo sayım farkını hücre hareketlerine işleme sırasında ekrana gelen uyarı kaldırıldı.

**KULLANICI İŞLEMLERİ**
**İyileştirmeler**

**1- "Stok Kartı Kopyalama" İşlemi Seçildiğinde; İşlem Tarihi, Kullanıcı İçin Tanımlanan Açık Tarih Aralığında Olmasına Rağmen Ekrana Gelen "Tarih Kilidi" Uyarısının Kaldırılması Talebi**

"Stok Kartı Kayıtları" ekranında iken farenin sağ tuşu ile ekrana gelen "Stok Kartı Kopyalama" işlemi seçildiğinde; işlem tarihi, kullanıcı için tanımlanan açık tarih aralığında olmasına rağmen alınan "Tarih Kilidi" uyarısı kaldırıldı.

**NDI**

**İyileştirmeler**

**1- CheckListBox’da İşaretlenen Kayıtların Bulunmasının Sağlanması**

NDICheckListBox bileşeninde "CheckedList" özelliği desteklendi.
