---
title: "9.0.28 Mayıs 2020"
page_id: "50664914"
product: "netsis-3-enterprise"
depth: 3
is_section: true
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Sürüm Dokümanları"
  - "2020 Netsis"
  - "9.0.28 Mayıs 2020"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Sürüm Dokümanları / 2020 Netsis / 9.0.28 Mayıs 2020"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTI2MWQ4MjY3LWQ4MGYtNDM0Zi05YTE3LTY5Y2VhNDZhN2M5NSZsaW5rPWQ4MTYxMjg3LTg2M2QtNGQzZS1iZjdlLWIzZGI3YmQxNmI1OSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=261d8267-d80f-434f-9a17-69cea46a7c95&link=d8161287-863d-4d3e-bf7e-b3db7bd16b59&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "9-0-28-mayis-2020_50664916_50664914.html"
source_version: "2022-07-05T11:57:42.713+03:00"
source_bytes: 46158
fetched_at: "2026-09-13T04:28:21+00:00"
generator: "netsis-scraper 1.0.0"
---
# 9.0.28 Mayıs 2020

Netsis 9.0.28 sürümünde yapılan yenilikler aşağıdaki şekildedir:

**1- Satış Tipli Hal Faturasında Mal Sahibi Alanının Zorunlu Olmamasının Sağlanması**

Satış tipli hal faturasında Mal sahibi VKN/TCKN ve Adı Soyadı/Unvan alanlarının zorunluluğu kaldırılmıştır.

**2- NetOpenX - Müstahsil Nesnesine Eksik Alanların Eklenmesi Talebi**

Müstahsil nesnesine GIB_FATIRS_NO, EMustahsil ve Kesinti_Dahil alanları eklenmiştir.

**3- Zamanlanmış Görevlerin Otomatik Oluşturulması Talebi**

Zamanlanmış Görevlerin yürütüldüğü Netsis.Notification.WinService ilk çalıştığı anda Netsis Yeni Sürüm ve Netsis ERP Youtube kanalında bulunan ürün videoları için otomatik sistem görevlerinin oluşması sağlanmıştır. Servis ilk çalıştığında her gün saat 10:00'da çalışması için görevler oluşturur ve kullanıcılara yeni sürüm ve yeni video içerikleri ile ilgili bilgilendirme maili gönderir. Kullanıcının, bu tipteki bildirim mesajlarını görmesi istenmiyorsa (“SYSTEMTASK”,”NOSHOW”) özel parametresinin kullanılması gerekir.

**4- Stok Kodu Değiştirme İşleminde Saha Tablo Eşleştirme Ekranında Girilen Kullanıcı Tanımlı Sahaların Aktarılması**

Stok Kodu Değiştirme işleminde Saha Tablo Eşleştirme ekranından girilen kullanıcı tanımlı bilgilerin aktarılması sağlanmıştır.

**5- 'CARI','OZELHESAPZORUNLU' Özel Parametresinin Cari Parametrelerindeki Özel Hesap Kapatma Sekmesine Taşınması Talebi**

'CARI','OZELHESAPZORUNLU' özel parametresi, "Özel hesap kapatma işlemi yapılmadan ekrandan çıkılamasın" ismiyle Cari Parametreleri ekranının "Özel Hesap Kapatma" sekmesine taşınmıştır.

**6- Kullanıcı e-Posta Tanımları Ekranının Yenilenmesi Talebi**

Kullanıcı e-Posta Tanımları ekranı görsel ve kullanım olarak yenilenmiştir.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=r8E5v8JZQ3M&ab_channel=LogoDestek).

**7- NetOpenX - e-İrsaliye Hal Desteğinin Sağlanması**

NetOpenX e-İrsaliye hal desteği sağlanmıştır.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=BfF6lgonyFQ&ab_channel=LogoDestek).

**8- Vardiya Bazında Kaynak Sayılarının Değiştiği Durumlarda Makine Doluluk Oranlarının Verimli Çıkmasının Sağlanması**

Vardiya bazında kaynak sayılarının değiştiği durumlarda ileri üretim planlama sonuçlarında kaynakların daha verimli kullanılması için gerekli iyileştirmeler yapılmıştır.

**9- GEKAP Uygulaması NetOpenX Düzenlemesinin Yapılması**

Geri Kazanım Katılım Payı Desteğinin Sağlanması ile ilgili ekranlara eklenen alanların NetOpenX desteği sağlanmıştır.

Stok Kartı ekranında "Stok Mevzuat" alanına veri atılması için TStokMevzuatTipi desteği getirilmiştir.

Kullanımı : StokTmlBlg.StokMevzuat = TStokMevzuatTipi.smGEKAPStok

Cari Kart ekranında "Geri Dönüşüm Katılım Payı Hesaplanmasın" alanına veri atılması için saha eklemesi yapılmıştır.

Kullanımı = GEKAPHESAPLANMASIN = false (Seçim yapılmadan kayıt atılacak anlamına gelir.)

Fatura ekranında "Kalem" nesnesine "Gekap Tutar" ve "Gekap Ambalaj Tutar" alanları eklenmiştir.

Kullanımı: fatKalem.GEKAPTutar = 10; fatKalem.GEKAPAmbTutar = 2

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=aKYzosBovt8&ab_channel=LogoDestek).

**10- Yeni Fiyat Tanımlama Ekranlarında Şubeli Fiyat Tanımlamasının Sağlanması**

Detaylı Fiyat Listesinden şube bazında tanımlanan fiyatların "Koşul Uygulaması" kullanıldığı zaman da ekrana gelmesi sağlanmıştır.

**11- NetOpenX - Hal Faturası Desteğinin Sağlanması**

NetOpenX ile "Hal Faturası Oluşturma" desteği sağlanmıştır.

**12- Gelen Kutusunda İken Farenin Sağ Tuşu ile Ekrana Gelen Seçeneklere Alış İrsaliyesi Oluşturma Seçeneğinin Eklenmesi Talebi**

"İrsaliye Bazında Gelen e-İrsaliye" ekranının sağ tuş seçenek menüsüne eklenen "E-İrsaliyeden Alış İrsaliyesi Oluşturma" işlemi ile, gelen e-İrsaliyelerden alış irsaliyesi oluşturulması desteklenmiştir. "e-Belge Eşleştirme İptali" işlemi ile de, oluşturulan alış irsaliyesinin e-Belge bağlantısının silinmesi sağlanmıştır. Ayrıca, "Alış İrsaliyesi" ekranının "Üst Bilgiler" sekmesindeki sağ tuş menüsüne de "e-Belge Görüntüle" ve "e-Belge Eşleştirme İptali" işlemleri eklenmiştir.

**13- e-İrsaliye Hal Faturası Desteğinin Getirilmesi Talebi**

e-İrsaliyede "Hal Faturası Senaryosu" desteklenmiştir.

**14- Özel Hesap Kapatma Ekranının Yenilenmesi ve Farklı Döviz Tipiyle Kapatma Desteğinin Getirilmesi Talebi**

"Özel Hesap Kapatma" ekranı yenilenerek, "Özel Hesap Kapatma" işleminde farklı döviz tiplerindeki hareketlerin birbirini kapatma desteği getirilmiştir.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=x18LI7qOF1Q&ab_channel=LogoDestek).

**15- Zamanlanmış Görev Tanımı Ekranındaki "Bilgilendirme Yöntemi" Parametresinin Çoklu Seçim Yapılabilir Hale Getirilmesi Talebi**

Zamanlanmış Görev Tanımı ekranında "Bilgilendirme Yöntemi" parametresinin çoklu seçim yapılabilir hale getirilmesi desteklenmiştir. Zamanlanmış görev sonucunda bildirim yöntemlerinin birden fazla seçilmesi sağlanmıştır.

**16- NetOpenX - Rapor Taslaklarının Çalıştırılması ve Sonuçlarının XLSX veya PDF Olarak Saklanması Talebi**

NetOpenX ile Taslak ve Sonuç Çıktı Tipi verilerek çalıştırılan raporun XLSX ve/veya PDF olarak belirtilen dizine kaydedilmesi ile ilgili destek sağlanmıştır.

**17- Zamanlanmış Görevler Eklentisine "Rapor Çalıştırma" İşleminin Eklenmesi Talebi**

Zamanlanmış Görevler eklentisine "Rapor Çalıştır" işlemi eklenmiştir.

**Örneğin;**

Netsis tarafından her gün bir rapor çalıştırılıp istenen kullanıcıya bu raporun e-Posta veya bildirim olarak gönderilmesi sağlanmıştır. "Zamanlanmış Rapor Oluşturma" işlemi "Zamanlanmış Görev" eklentisinden veya raporun ön sorgusundaki rapor butonunun yanında yer alan aşağı ok sembolü ile oluşturulabilir.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=eHoJoL9f1XY&ab_channel=LogoDestek).

**18- Yevmiye Kontrol İşleminin Zamanlanmış Görevlere Eklenmesi Talebi**

Zamanlanmış Görevler eklentisinde "Ön Tanımlı İşlem" olarak "Yevmiye Kontrol" işlemi desteklenmiştir.

**19- Cari Hareket Kontrol İşleminin Zamanlanmış Görevlere Eklenmesi Talebi**

"Zamanlanmış Görevler" eklentisinde Cari Hareket Kontrol işlemi desteklenmiştir.

**20- Yeni Tanıtım Videosu Kontrolü Desteğinin Zamanlanmış Görevler Eklentisine Eklenmesi**

Netsis ERP Sürüm Yenilikleri ile ilgili Youtube videolarının "Zamanlanmış Görevler" eklentisi ile kontrolünün yapılması desteklenmiştir. "Zamanlanmış Görevler" eklentisinde "Ön Tanımlı İşlemler" seçeneğinin altına eklenen bu yeni işlem ile, Netsis ERP Youtube kanalına yüklenen videoların takibi ve izlenmesi sağlanmıştır.

**21- Yeni Sürüm Kontrolü İşleminin Zamanlanmış Görevlere Eklenmesi Talebi**

"Zamanlanmış Görevler" eklentisinde "Ön Tanımlı" işlere "Yeni Sürüm Kontrol" seçeneği eklenmiştir. Bu görev ile güncel sürüm kontrol edilmesi sağlanarak, istendiğinde güncel sürüm indirilebilir. Böylece, "Netsis NetUpdate Uygulaması" ile güncellemeye hazır duruma getirilir.

**22- Veritabanı Bakım İşlemlerinin Zamanlanmış Görevler Eklentisine Eklenmesi**

Zamanlanmış Görevler Eklentisine “Veritabanı Bakım İşlemleri” ön tanımlı işlemi eklenmiştir. Parçalanma oranı %40'ın üzerindeki tabloların yeniden dizin oluşturma ve istatistiklerinin güncellenmesi sağlanmıştır. Görev, tablo bazında veya tüm tablolarda çalışacak şekilde tanımlanabilir.

**23- Rapor Taslak Kayıtlarının Desteklenmesi**

Raporlarda "Oku" - "Sakla" butonuna tıklandığında yetkilendirme yapılabilmesi sağlanmıştır. Rapor modülü raporlarının da veritabanında saklanması desteklenmiştir.

**24- Depolar Arası Transfer Kaydı Yapılan Mamulün Ambar Çıkış Fişinde Tekrar Sipariş Numarasına Bağlanması Talebi**

FATURA/SIPAMBARREHBER özel parametresi ile 'Sipariş bağlantılı Depolar Arası Transfer Kaydında Teslimat Ayrı Takip Edilsin" parametresi kullanıldığı durumlarda, "Ambar Çıkış Fişi" ekranının "Kalemler" sekmesindeki "Sipariş No" rehberinde, siparişe bağlı yapılan D.A.T. miktarlarını teslimat olarak göstermemesi sağlanmıştır.

**25- Cari Bazlı Döviz İyileştirmesinin Yapılması**

Genel Gider Cari Hesap Fatura Kaydı ve Serbest Meslek Makbuzu ekranlarında cari bazlı döviz uygulaması desteklenmiştir.

**26- Bağlantı Kopması Sonucu Tekrar Bağlantı Sağlanması**

Netsis bağlantısı koptuğunda, ekrana "Veritabanı Bağlantınız Koptuğu İçin Uygulama Tekrar Başlatılacaktır." uyarısının gelmesi sağlanmıştır. Uygulama tekrar başlatılırken yine bağlantı sağlanmazsa, "Bağlantı Kopması Sonucu Sunucuya Tekrar Bağlanılamadı. Uygulama kapatılacaktır." uyarısı ile uygulamanın kapatılması sağlanmıştır.

**27- Kullanıcı e-Posta Tanımları Ekranına Bildirim Servisi Desteğinin Getirilmesi**

"Kullanıcı e-Posta Tanımları" ekranına "Bildirim" seçeneği eklenmiştir. Seçili işlemlerde kullanıcı için bildirim seçeneği işaretlenirse, ilgili kullanıcıya işlem hakkında bildirim gönderilmesi sağlanır.

**28- Muhasebe - İşlemler - Yevmiye Kontrol İşleminin NetOpenX Tarafında Desteklenmesi Talebi**

Muhasebe - İşlemler - "Yevmiye Kontrol" işlemi NetOpenX tarafında desteklenmiştir.

**29- Fatura Belgesinin Klasöre Toplu Aktarımının Yapılması ve İlgili Dosyadan İçeri Alınmasının Sağlanması**

Alış ve satış faturalarının Json formatta istenen klasöre toplu olarak aktarılması ve ilgili dosyadan da içeri alınması için "Toplu Fatura Aktarımı" ekranı desteklenmiştir.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=Ok6BHIHzcFM&ab_channel=LogoDestek).

**30- Özel Tabloların Log Sistemine Dahil Edilmesinin Sağlanması**

Log Parametrelerine "Uyarlama Araçlarından Manuel Atılan Kayıtlar İçin Log Tutulsun" seçeneği eklenmiştir. Parametre işaretlendiğinde "Log Tutulacak Tablolar" ekranına, Kullanıcı Tablolar sekmesi gelir. Bu sekmeye, kullanıcıların kendi oluşturdukları özel tablolar gelir ve seçildiğinde; Dinamik Kodlama, NetOpenX, NetOpenX Rest veya NDI tarafından bu tablolarda değişiklik yapıldığında, Netsis Log Raporu ile rapor alınması sağlanmıştır.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=r8E5v8JZQ3M&ab_channel=LogoDestek).

**31- Cari Kodu Değişikliği İşleminde Saha-Tablo Eşleştirmesine Ait Kullanıcı Tanımlı Sahaların da Kopyalanmasının Sağlanması**

"Cari Kodu Değişikliği" işleminde saha-tablo eşleştirmelerine ait kullanıcı tanımlı sahaların da kopyalanması sağlanmıştır.

**32- SSO'da Domain Yapısı Olduğunda Organizasyonel Birimde Bir Alt Kırılım Olması Talebi**

SSO'da domain kullanıcı için tanım yapıldığında, "Organizasyonel Birim" altında bulunan bir grup için kısıt verilerek sadece o gruptaki kullanıcıların ekrana getirilmesi desteklenmiştir.

**33- "Faturalandırılan İrsaliyeler Saklansın" Parametresi Seçilmediğinde ve e-İrsaliye Oluşturulup Gönderildiğinde İrsaliyenin Faturaya Dönüştürülmesi ve Fatura Silindiğinde İrsaliye Kaydının da Silinmesi ile İlgili Durumun Düzeltilmesi Talebi**

e-İrsaliye kullanılması durumunda, Satış Parametreleri - "Faturalaştırılan İrsaliyeler Saklansın" seçiminin otomatik olarak seçilmesi sağlanmıştır. "e-İrsaliye Uygulamasından" bağımsız olarak, ilgili parametrenin kullanımı için FATURA\\EIRSALIYESAKLAKONTROL özel parametresinin kullanılması gerekir.

**34- e-İrsaliye Ekrana Getirilip Toplamlar Adımından Faturalandırma Yapılmasının Sağlanması**

e-İrsaliyesi oluşturulmuş irsaliyenin "Toplamlar" seçeneğinden faturalandırılması sağlanmıştır.

**35- Turizm Katkı Payı Beyannamesinin Desteklenmesi Talebi**

Turizm Katkı Payı Beyannamesi desteklenmiştir.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=mJ5FMA4U-Uc&ab_channel=LogoDestek).

**36- İş Emrine Bağlı Hammadde Dökümü Raporundaki "Sıralama" Alanlarının Daha Anlaşılır Hale Getirilmesi Talebi**

Üretim - Raporlar - "İş Emrine Bağlı Hammadde Dökümü" raporunda alan açıklama düzenlemeleri yapılmıştır.

- "Kod Sırası" ve "Giriş Sırası" seçeneklerinin bulunduğu grubun açıklaması "Hammadde Sıralama" olarak düzeltilmiştir.

- Alt bölümdeki "Sıralama" isimli büyük grubun açıklaması "İş Emri Sıralama" olarak düzeltilmiştir.

**37- Üretim - İşlemler - "Reçete Kopyalama" İşleminde İlgili Mamule Ait Alternatif Reçetelerin Kopyalanmasının Sağlanması**

Üretim -İşlemler - "Reçete Kopyalama" işleminde seçili mamule ait alternatif reçetelerin kopyalanması desteklenmiştir. Eklenen "Alternatif Reçeteler de Kopyalansın" seçeneği sayesinde, "Reçetesi Kopyalanacak Mamul Koduna" ait alternatif reçetelerin yeni mamul koduna kopyalanması sağlanmıştır.

**38- Teklif Aşamasında İken Çeki Listesi Girilmesinin Sağlanması**

Dış Ticaret Parametreleri ekranına "Tekliften Ön Çeki Listesi Oluşturulsun" parametresi eklenmiştir. Parametre işaretlendiğinde, siparişte olduğu gibi, teklif oluşturulurken çeki listesi de oluşturulur. İhracat Dosya İşlemleri - Tekliflerim sekmesindeki "Tanımlı Çeki Listesini Aktar" seçeneği işaretlendiğinde satış teklif girilirken oluşturulan çeki listesinin siparişe aktarılması sağlanmıştır.

**39- Yürüyen Bakiyeli Stok Raporu Ekranında Rapor Sekmesindeki Grid Üzerinde "Belge Detayı" Şeklinde Sağ Tuş Fonksiyonunun Desteklenmesi Talebi**

Üretim - Raporlar - Yürüyen Bakiyeli Stok Raporu ekranında "Rapor" sekmesinde "Belge Detayı" sağ tuş fonksiyonu olarak desteklenmiştir.

Belge Tipi :

-İş Emri veya IsemRzv ise "Açıklama" alanındaki iş emri numarası kullanılarak "İş Emri Girişi" ekranı açılır.

-Satsip ise "Açıklama" alanındaki satıcı siparişi numarası kullanılarak "Satıcı Siparişi" ekranı açılır.

-MusSip veya MussipRzv ise "Açıklama" alanındaki müşteri siparişi numarası kullanılarak "Müşteri Siparişi" ekranı açılır.

-Talep ise "Açıklama"alanındaki satın alma talep numarası kullanılarak "Satın Alma Talep" ekranı açılır.

-Stok ise "Stok Kodu" alanındaki değer kullanılarak "Stok Hareket Kayıtları" ekranı açılır.

Bu ekranları açarken kullanıcıların hak ve yetkileri kontrol ediliyor. Kullanıcının ilgili ekran için hakkı yoksa bu menü üzerinden ekranları açamaz.

**40- Yürüyen Bakiyeli Stok Raporu Ekranının Rapor Sekmesindeki Grid üzerinde "Cari Adı" ve "Depo Adı" Bilgilerinin Görünmesi Talebi**

Üretim - Raporlar - Yürüyen Bakiyeli Stok Raporu - "Rapor" sekmesindeki grid üzerine "Cari Kodu" alanından sonra "Cari Adı" ve "Depo Kodu" alanı ve "Depo Adı" alanları eklenmiştir.

**41- Merkezi Kimlik Yönetimi Kullanıcı Yetki Tanımlama Ekranında Şirket Seçimi İşleminde İyileştirme Yapılması Talebi**

Merkezi Kimlik Yönetimi - "Kullanıcı Yetki Tanımlama" ekranı "Şirket Seçimi" işleminde performans iyileştirmesi yapılmıştır.

**42- Zamanlanmış Görevler İçin REST Görev Tipinin Desteklenmesi Talebi**

Zamanlanmış Görevler için REST tipi eklenmiştir. Böylece, istenen REST servisine GET, PUT, POST veya DELETE çağrılar yapılması sağlanmıştır.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=RNtiFGA-53M&ab_channel=LogoDestek).

**43- Üretim Akış Kaydı Ekranından Üretim Sonu Kaydı Oluşturulurken Fire Miktarının Hesaba Katılmaması ile İlgili Durumun Düzeltilmesi Talebi**

"Üretim Akış Kaydı" ekranından "Üretim Sonu Kaydı" oluşturulurken fire miktarının hesaba katılmaması ile ilgili durum düzeltilmiştir.

**44- Rest - Stok Planlama Kayıtları Ekranının Desteklenmesi Talebi**

Stok Planlama Kayıtları, Müşteri/Satıcı Stok Kayıtları ve Cari Planlama Kayıtları ekranları Rest arayüzü için desteklenmiştir.

**45- Müşteri-Satıcı Stok Kayıtları Ekranı İçin Saha-Tablo Eşleştirmesi Desteğinin Sağlanması**

Müşteri-Satıcı Stok Kayıtları ekranında Saha Tablo Eşleştirmeleri desteklenmiştir.

**46- Cari Planlama Kayıtları Ekranı İçin Saha-Tablo Eşleştirmesi Desteğinin Getirilmesi Talebi**

Cari Planlama Kayıtları ekranına "Saha-Tablo Eşleştirme" desteği getirilmiştir.

**47- Toplu e-Arşiv Oluşturma Ekranının Taslaklar Sekmesinde Bulunan Faturaların Gönderim Yapılmadan Önce Toplu Olarak Basım Yapılmasının Sağlanması**

"Toplu e-Arşiv Oluşturma" ekranının "Taslaklar" sekmesinde bulunan faturaların gönderim yapılmadan önce toplu olarak basımının yapılması sağlanmıştır.

**48- Online e-İrsaliye Kullanan Firmalar İçin Gelen Kutusunda Kabul, Red ve Kısmi Red İşlemlerinin Desteklenmesi Talebi**

Online e-İrsaliye kullanan firmalar için gelen kutusunda Kabul, Red, Kısmi Kabul, Kısmi Red işlemleri desteklenmiştir.

**49- Mizan Raporunda Kapanış Fişleri Hariç Tutulsun ve Açılış Fişleri Hariç Tutulsun Seçenekleri ile Rapor Alınmasının Desteklenmesi**

Mizan raporunda "Kapanış Fişleri Hariç Tutulsun" ve "Açılış Fişleri Hariç Tutulsun" seçenekleri ile rapor alınması desteklenmiştir.

**50- NetOpenX - Muhasebe Hesap Kodu Aktarımı Talebi**

Muhasebe Hesap Kodu Aktarım ekranı NetOpenX tarafında desteklenmiştir.

**51- NetOpenX - Muhasebe Aydan Aya Fiş Aktarımı Desteğinin Sağlanması**

Aydan Aya Fiş Aktarımı işlemi NetOpenX tarafında desteklenmiştir.

**52- NetOpenX - Muhasebe Fiş Numarası Değişikliğinin Sağlanması Talebi**

Muhasebe - İşlemler - Hızlı Bilgi Değişikliği - "Fiş Numarası Değişikliği" işlemi NetOpenX tarafında desteklenmiştir.

**53- NetOpenX - TCMB Banka Kayıtları Online Güncellenme Desteğinin Sağlanması Talebi**

Banka - Kayıt - TCMB Kayıtları - TCMB Banka Kayıtları Online Güncellenme ekranının NetOpenX ile çalıştırılması desteklenmiştir.

**54- NetOpenX - Banka Hareket Kayıtları Desteğinin Sağlanması Talebi**

Banka hareket kaydının okunması ve yeni bir banka hareket kaydı oluşturulması desteklenmiştir.

**55- e-Mutabakat ekranında "Aynı VKN/TCKN'ye Sahip Kayıtlar Birleştirilsin" Parametresi ile Cari Kodları Şubeler Bazında Farklı da Olsa Aynı VKN/TCKN'ye Sahip Olan Carilerin Tutarlarının Kümüle Ediliğ Tek Bir Satırda Gösterilmesinin Sağlanması**

e-Mutabakat ekranında "Aynı VKN/TCKN'ye Sahip Kayıtlar Birleştirilsin" parametresiyle, cari kodları şubeler bazında farklı da olsa aynı VKN/TCKN'ye sahip olan cari hesapların tutarlarının kümüle edilip tek bir satırda gösterilmesi sağlanmıştır.

**56- İmleç Stok Kodu Alanına Odaklı İken Sağ Tuş ile Açılan Seçenekler Menüsüne Fiyat Listesinin Aktif Gelmesinin Sağlanması**

İmleç "Stok Kodu" alanına odaklı iken, sağ tuş seçeneklerine fiyat listesinin aktif gelmesi sağlanmıştır.

**57- Hava Durumu ve Döviz Eklentilerinin Bildirim Servisinde Olduğu Gibi Merkezi Kimlik Denetiminin Altına Taşınması Talebi**

Hava durumu ve Döviz eklentilerinin SSO servisi ile çalışması sağlanmıştır.

**58- Hesap Planına Göre Ters Bakiye Veren Hesapların Dönem Sonunda Yansıtma Hesabı ile Otomatik Kapama Yapılmasının Sağlanması**

120 ve 320 bilanço hesaplarının ters bakiye vermesi durumunda, dönem sonunda yansıtma hesapları ile otomatik kapama yapılması sağlanmıştır. "Ters Bakiyeli Hesap Kontrol Raporu" ekranından ters bakiye veren hesaplar raporlanarak yansıtma fişi oluşturulabilir. "Ters Bakiyeli Hesap Yansıtma Girişi" ekranından ilgili hesaplara, 340 ve 159 yansıtma hesaplarının da tanımlanması gerekir.

**59- Stok Kartı Ekranında "Sürükle Bırak" özelliğinde "İngilizce İsim" ve Ek Bilgiler Alanında "Türü" alanlarının Desteklenmesi Talebi**

Stok kartı Excel'den aktarımda "İngilizce İsim" ve "Ek Bilgiler" alanlarında "Türü" alanı desteklenmiştir.

**60- Yevmiye Fişi Listesine Kayıt Tarihi Kayıt Saati ve Kullanıcı Bilgilerinin Gelmesinin Sağlanması**

"Yevmiye Fişi" ve "Klasik Yevmiye Fişi" raporlarına "Fiş Kayıt Tarihi Basılsın" ve "Kayıt Yapan Kullanıcı Basılsın" seçenekleri eklenmiştir. Seçenekler işaretlenip rapor alındığında, raporda fişin kaydedildiği tarih ve saat bilgisi ile fişi kaydeden kullanıcı bilgilerinin de listelenmesi sağlanmıştır.

**61- Stok - İşlemler - Ürün Malzeme Maliyetleri Oluşturma İşlemi İçin Sistemde Log Kaydı Oluşmaması ile İlgili Durumun Düzeltilmesi Talebi**

Stok - İşlemler - "Ürün Malzeme Maliyetleri Oluşturma" işleminde, seçilen parametre bilgilerinin Log modülünde raporlanması desteklenmiştir.

**62- Demirbaş Paketinde Finansal Kiralama (Leasing) ile Alınan Faturaların İşleyişi ile İlgili İyileştirme Yapılması Talebi**

Demirbaş - Finansal Kiralama (Leasing) Uygulamasında; ödeme planının otomatik hesaplanması, Excel ile ödeme planının aktarılması, oluşturulan sözleşme, dekont, fatura ve ödeme kayıtlarının program ile entegre çalışması desteklenmiştir.

**İyileştirmeler**

**1- Bakım Sözleşmeleri Ekranında Başlık Bilgisi ve Etiket Uyarısı ile İlgili Durumun Düzeltilmesi Talebi**

Bakım Sözleşmeleri ekranın Başlık Bilgisi ve Ek Etiketi konumu düzeltilmiştir.

**2- İrsaliye Bazında Gelen Kutusu Açılırken Ekrana Gelen Uyarı ile İlgili Durumun Düzeltilmesi Talebi**

"İrsaliye Bazında Gelen e-İrsaliye" ekranında, iki farklı cari hesaptan gelen aynı e-İrsaliye numaralı belgelerin görünümü sağlanmıştır.

**3- Kalite Kontrol Ölçüm Kayıtları Ekranında Gelen Kalemlere Müdahale Edilememesi ile İlgili Durumun Düzeltilmesi Talebi**

Kalite Kontrol Kaydı ekranında girilen ölçüm kayıtlarının değiştirilmesine yönelik düzeltme yapılmıştır.

**4- Değerleme ve Amortisman Ayırma İşleminde Ekrana Gelen Uyarı Mesajı ile İlgili Durumun Düzeltilmesi Talebi**

Oracle veritabanında Değerleme ve Amortisman Ayırma işlemi sonucu ekrana gelen uyarı mesajı ile ilgili durum düzeltilmiştir.

**5- Çizelge Bazlı Kapasite Raporu Grid Başlıklarının Düzeltilmesi Talebi**

MRP - Raporlar - Çizelge Bazlı Kapasite Raporunun 'Makine Bazlı' raporlanması durumunda Makine Adı kolon ismi düzeltilmiştir.

**6- Demirbaş Dekont Kaydı Ekranında İşlemler Tamamlanamadı Uyarısı ile İlgili Durumun Düzeltilmesi Talebi**

Demirbaş Bilgi Kartı ekranından dekont kaydı oluşturulması sağlanmıştır.

**7- Genel Dekont Kaydı Ekranından Girilen Kayıtlar 10 Satırdan Fazla Olduğunda ve Mevcut Satırdaki Cari Kod Başka Bir Cari Kod ile Değiştirildiğinde Cari Hareket Tablosundan Eski Kaydın Silinmemesi ile İlgili Durumun Düzeltilmesi**

Genel Dekont Kaydı ekranında mevcut cari hareketin kodu değiştirildiğinde, iki cari kod için kayıt görünmesi ile ilgili durum düzeltilmiştir.

**8- Esnek Yapılandırmalı Stok Koduna Ait Reçete Kaydında Reçete Tablosuna Kayıt İşleminde Ekrana Gelen Uyarı ile İlgili Durumun Düzeltilmesi**

Esnek yapılandırmalı bir mamul kodu için Reçete Kaydı ekranında yeni kayıt işlemi için düzenleme yapılmıştır.

**9- Bildirim Merkezinde Başlıkta/Mesajda Bazı Türkçe Karakterlerin Gösterilmemesi ile İlgili Durumun Düzeltilmesi Talebi**

"Zamanlanmış Görev" ve "Bildirim Mesajlarındaki" Türkçe karakterlerin gösterilmemesi ile ilgili durum düzeltilmiştir.

**10- DAT Kaydında Cari Kodu Alanı Sıfır Değer ile Doldurulduğunda Kilitli Cari Uyarısının Alınması ile İlgili Durumunun Düzeltilmesi Talebi**

Depolar Arası Transfer kaydında "Cari Kodu" alanı sıfır değeri ile doldurulduğunda ekrana gelen uyarı ile ilgili durum düzeltilmiştir.

**11- CARI\\TESLIMCARIGOSTERME Özel Parametresi Tanımlı İken Fatura Girişinde Farklı Teslim Cari Bilgisi Girildiğinde Ekrana Gelen Uyarı ile İlgili Durumun Düzeltilmesi Talebi**

CARI\\TESLIMCARIGOSTERME özel parametresi tanımlı iken, fatura için farklı teslim cari bilgisi girildiğinde ekrana gelen 'GEKAPHESAPLANMASIN' uyarısı düzeltilmiştir.

**12- Satış Faturasında Serili Bir Stok Kaydı Girilirken Aynı Serinin Hem Küçük Hem Büyük Harften Oluşan Stok Girişine İzin Verilmesi ile İlgili Durumun Düzeltilmesi**

Serili stok için açılan "Seri Takibi" ekranından çıkış yaparken "Seri Rehberi" ekranında, küçük büyük harf duyarlılığı ile ilgili düzeltme yapılmıştır.

**13- Anlık Üretim Planlama Ekranında Yarı Mamul Bakiyeleri Dikkate Alınmadan Tekrar Yarı Mamul Üretilmesi İçin Hammadde Gereksiniminin Oluşması ile İlgili Durumun Düzeltilmesi**

Anlık Üretim Planlama ekranında mamul için 'Stok Seviyeleri Kontrolü' seçeneği seçili şekilde rapor alınırken ve hammadde gereksinim miktarı hesaplanırken, yarı mamul stok miktarlarının hesaba katılmasına yönelik düzenleme yapılmıştır.

**14- Zamanlanmış Görev Tanımı Ekranında Ön Tanım İşlemi Seçilmeyip Dinamik Tarih Aralığı Seçildiğinde Ekrana Gelen Uyarı ile İlgili Durumun Düzeltilmesi Talebi**

Zamanlanmış Görev Tanımı ekranında ön tanımlı işlem seçilmeden Dinamik Gün seçeneğinin seçilememesi sağlanmıştır.

**15- Üretim Akış Kaydından Birim Katsayı Güncelleme İşleminde Süre Tipine Göre Ayrım Yapmadan Hesaplama Yapıldığında Katsayı Hesaplarının Doğru Oluşmasının Sağlanması**

Birim Katsayı ekranı güncelleme işleminde birim katsayı verisi 'Üretim Akış Kontrolden Getirilsin' seçeneğinin seçili olması durumunda, katsayı hesabı yapılan üretim akış kaydı farklı süre tipleri ile ilgili hesaplamanın yapılmasına yönelik düzeltme yapılmıştır.

**16- Dinamik Depo Olan Bir Depodan Dinamik Depo Olmayan Bir Depoya DAT İşlemi Yapılırken Rehbere Tıklandığında Ekrana Gelen Uyarı ile İlgili Durumun Düzeltilmesi Talebi**

Dinamik Depo olan bir depodan, dinamik depo olmayan bir depoya DAT işlemi yapılırken - Hücre Toplama ekranında - hücre rehberine tıklandığında ekrana gelen uyarı ile ilgili durum düzeltilmiştir.

**17- Çizelgeleme Çalıştırıldığında Çizelgelenen İşler Raporundaki Bazı İş Emirlerinin Sipariş Termin Raporunda Çıkmaması ile İlgili Durumun Düzeltilmesi**

"İleri Üretim Planlama" ekranında "Çizelgeleme" çalıştırıldığında "Çizelgenen İşler" ve "Sipariş Termin Raporları" arasında oluşan farklılıklar giderilmiştir.

**18- Genel Dekont Kaydı Ekranında Banka Kaydı Bulunan Bir Dekont ile Düzeltme Yapıldığında Banka Hesap Hareketleri Tablosunda Tekrar Kayıt Oluşması ile İlgili Durumun Düzeltilmesi**

Genel Dekont Kaydı Ekranında banka kaydı bulunan bir dekont ile düzeltme yapıldığında Banka Hesap Hareketleri tablosunda tekrar kayıt oluşması ile ilgili durum düzeltilmiştir.

**19- Yükleme Emri Kalem Bilgilerinde Sağ Tuş Seçeneklerindeki Toplu Mal Ayırma Listesinde Rapora Yazılan Script Kodların Sadece Bu Raporda Çalışmasının Sağlanması**

Yükleme Emri - "Kalem Bilgileri" sekmesinde iken farenin sağ tuşu ile ekrana gelen 'Toplu Mal Ayırma Listesi' raporuna yazılan Script kodların sadece bu raporda çalışması sağlanmıştır.

**20- Stok Kartı Kayıtlarında Kullanıcı Tanımlı Sahalar Değiştirilip Klavyedeki F5 Tuşuna Basıldığında Değişikliğin Kaydedilmemesi ile İlgili Durumun Düzeltilmesi Talebi**

Cari Hesap Kayıtları ve Stok Kartı Kayıtlarında Kullanıcı Tanımlı Sahaların kaydedilmesi ile ilgili durum düzeltilmiştir.

**21- Stok Hareket Kayıtları Ekranında Herhangi Bir Stok Seçilmeden Farenin Sağ Tuşu ile Ekrana Gelen Hücre/Dinamik Depo Yerleştirme-Toplama İptali İşlemlerinde Alınan Uyarı ile İlgili Durumun Düzeltilmesi Talebi**

Stok Hareket Kayıtları ekranında herhangi bir stok seçilmeden farenin sağ tuşu ile ekrana gelen "Hücre veya Dinamik Depo Yerleştirme-Toplama İptali" işlemlerinde alınan uyarı ile ilgili durum düzeltilmiştir.

**22- Stok Planlama Kayıtlarında Kullanıcı Tanımlı Sahalardaki Kayıt Sorunlarının Çözülmesi Talebi**

Stok Planlama Kayıtlarında yer alan Kullanıcı Tanımlı Sahaların kaydedilmesi ile ilgili sorun çözülmüştür.

**23- Çizelgeleme - Kapasite Bazlı Doluluk Raporunda Kaynaklar İçin Rapor Alındığında Kaynak Doluluk Oranlarının Olması Gerekenden Düşük Çıkması ile İlgili Durumun Düzeltilmesi**

Çizelgeleme sonuçları için alınan "Çizelgele Bazlı Kapasite" raporunda kaynakların kapasite doluluk oranının olması gerekenden düşük çıkması ile ilgili durum düzeltilmiştir.

**24- Dış Ticaret Modülünden Satıl Teklif Kaydı Silindiğinde Aynı Satış Teklifi Kaydı Kaydedilirken Ekrana Gelen Uyarı ile İlgili Durumun Düzeltilmesi Talebi**

Dış Ticaret modülünde Satış Teklif Kaydı silindiğinde, aynı satış teklif kaydının tekrardan kullanılması sağlanmıştır.

**25- Kasa Kayıtları Dövizli Muhtelif İşlemlerinde Kur Bilgisinin Gelmesinin Sağlanması**

Kasa Kayıtları - Muhtelif ve Fatura sekmelerinde döviz bilgilerinin doğru gelmesi sağlanmıştır.

**26- Gereksinim Planlama Oluşturma İşlemi Sipariş Bazında Ayrım Parametresi Seçilmeden Yapıldığında İhtiyaçların Sipariş Detayı Olmadan Tarih Bazında Kümüle Edilerek Kaydedilmesi Talebi**

MRP Parametreleri ekranında "Sipariş Bazında Satıcı Siparişi ve Planlama" ve "Sipariş Bazında İş Emri ve Planlama" parametreleri seçilmediği zaman Gereksinim Planlama Oluşturma işleminde "Sipariş Bazında Ayrım" seçeneği seçilmeden çalıştırılabilir. Bu durumda ihtiyaçların, sipariş detayı olmadan tarih bazında kümüle edilerek kaydedilmesi sağlanmıştır.

**27- Tahminleme Sonucunun Kaydedilmesi Sırasında Ekrana Gelen Uyarı ile İlgili Durumun Düzeltilmesi Talebi**

Tahminleme sonucunun kaydedilmesi sağlanmıştır.

**28- "Ortalama Maliyetle Stok Hareketi" Raporunun Sıralama Sekmesinden "Stok Kodu" Seçilerek Rapor Alındığında Ekrana Gelen Uyarı ile İlgili Durumun Düzeltilmesi Talebi**

"Ortalama Maliyetle Stok Hareketi" raporunun "Sıralama" sekmesinde "Stok Kodu" seçilerek rapor alınması sağlanmıştır.

**29- Cari Kart Ekranı Sürükle Bırak İşleminde Excel İçinde Vade Günü Alanı Olmamasına Rağmen Aktarım Sonrasında Cari Hesapların Tanımlı Vade Günlerinin Sıfırlanması ile İlgili Durumun Düzeltilmesi Talebi**

"Excel'den Netsis'e Aktarım" işleminde sadece aktarım için seçili olan alanların güncellenmesi sağlanmıştır.

**30- Şubede Fatura Oluştururken Şubelerde Ortak Stok ve Cariler İçin Stok Hareket Tablosunda Şube Kodunun Doğru Oluşmasının Sağlanması**

Şubede fatura kaydedilirken, stok hareketlerine merkeze ait şube kodu değerinin atanması durumu düzeltilmiştir.

**31- Satınalma Teklifinin İçine ÖTV'li Bir Stok Girildiğinde KDV'nin Ara Toplam Üzerinden Hesaplanmasının Sağlanması**

Satınalma Talep ve Satınalma Teklif ekranında ÖTV'li bir stok girildiğinde KDV'nin ara toplam üzerinden hesaplanması sağlanmıştır.

**32- e-Fatura Gelen Kutusu Kısıtı Tanımlaması Olduğunda Zarf Bazında Gelen e-Fatura Listesinde T.C. Kimlik Numarası ile Gelen Zarfların Listeye Gelmemesi ile İlgili Durumun Düzeltilmesi Talebi**

"e-Fatura Gelen Kutusu Kısıtı" tanımlaması olduğunda, Zarf veya Fatura Bazında Gelen e-Fatura ekranlarında, şahıs firmalarından gelen (T.C. Kimlik Numarası dolu olan) zarfların listeye gelmesi sağlanmıştır.

**33- İş Emrinde Belge Bazında Etiket Tanımlaması Yapıldığında Arama Alanına Girilen Etiketin Belgeyi Açmaması ile İlgili Durumun Düzeltilmesi Talebi**

İş emri için etiket verildiğinde iş emrinin açılması sağlanmıştır.

**34- Dekont Üzerinde Düzeltme Yapıldığında Farklı Bir Dekonta Ait Hareket Kayıtlarının Silinmesi ile İlgili Durumun Düzeltilmesi Talebi**

"DEKONT","DEKONTNOON" özel parametresi tanımlandığında kayıtların doğru atılması sağlanmıştır.

**35- Reçete Kaydı Sırasında Seçilen Bileşen Kodunun Stok Kartında Ölçü Birimi Tanımlı Olmasına Rağmen İlk Bileşen Kaydı Yapılırken Ölçü Birimlerinin Ekrana Getirilmemesi ile İlgili Durumun Düzeltilmesi Talebi**

Reçete Kaydı sırasında ilk bileşen kaydı yapılırken, stok ölçü birimlerinin "İş Akış Uygulaması" açık olduğunda da ekrana getirilmesi sağlanmıştır.

**36- Proje Mizanı Raporunun Proje Hariç Aralığına Verilen Kısıta Göre Listelenmesi Talebi**

Proje Mizanı raporunun proje hariç aralığına verilen kısıta göre listelenmesi sağlanmıştır.

**37- Dövizli Hareket Dökümü Gelişmiş Rapor Seçeneği ile Alınıp PDF Olarak Kaydedildiğinde Sütunların Düzgün Görünmesinin Sağlanması**

"Gelişmiş Rapor" seçeneği ile alınan raporlar PDF olarak kaydedildiğinde, sütunların aynı sayfaya basımı sağlanmıştır.

**38- Mevcut Kaydı Olan Bir Stok Ekrana Getirtilip Ölçü Birimi veya Depo Gibi Bilgiler Girilip Güncellendiği Zaman Kaydedildikten Sonra Gridde Girilen Ölçü Birim veya Depo Kodu Bilgilerini Göstermemesi ile İlgili Durumun Düzeltilmesi Talebi**

Stok Kartı Kayıtlarında mevcut kayıt için Ölçü Birim 1, 2 ve 3 güncellendiğinde gridin de güncellenmesi sağlanmıştır.

**39- Açık İşlerin Kapatılması Ekranında Açıklama Girildiğinde Dekont İşlemleri Sekmesinde Onay Açıklamasının Görüntülenmemesi ile İlgili Durumun Düzeltilmesi Talebi**

İş Akış Yönetimi - Açık İşlerin Kapatılması - "Açık İşler" sekmesinde dekont kaydı için açıklama girildiğinde, "Dekont İşlemleri" sekmesinde bu açıklamanın gözükmemesi ile ilgili durum düzeltilmiştir.

**40- FIFO Metodu ile Stok Devrinde Bakiyelerin Her Şubeye Toplam Bakiye Olarak ve Çoğaltılarak Atılması ile İlgili Durumun Düzeltilmesi Talebi**

Stok Parametreleri - "Şubeler Dahil Maliyet Sistemi" parametresi seçili iken farklı şubelerde hareketleri olan bir stok için FIFO yöntemi ile, "Devir Hareketleri Detaylandırılsın" parametresi işaretlenerek devir yapıldığında bakiyelerin doğru oluşması sağlanmıştır.

**41- Fatura KDV İcmalinde İade Tipli Miktarsız Girilen Satış Faturalarında KDV Matrahı ve Tutarın Düşürülerek Hesaplanması ile İlgili Durumun Düzeltilmesi Talebi**

Fatura KDV İcmalinde iade tipli miktarsız satış faturaları için KDV matrahı ve tutar hesaplaması ile ilgili düzenleme yapılmıştır.
