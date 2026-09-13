---
title: "9.0.26 Ocak 2020"
page_id: "47081687"
product: "netsis-3-enterprise"
depth: 3
is_section: true
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Sürüm Dokümanları"
  - "2020 Netsis"
  - "9.0.26 Ocak 2020"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Sürüm Dokümanları / 2020 Netsis / 9.0.26 Ocak 2020"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTg4ZTI5ZTFlLWZhYzgtNDcxYy1hYmFjLTEyOGIyOWQxMjZmZCZsaW5rPTI5MGY2OTlkLWEzYmUtNDQ2Zi05NmYxLTg5NGVhNGE5YTEzYyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=88e29e1e-fac8-471c-abac-128b29d126fd&link=290f699d-a3be-446f-96f1-894ea4a9a13c&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "9-0-26-ocak-2020_47081689_47081687.html"
source_version: "2022-07-05T13:10:07.610+03:00"
source_bytes: 65131
fetched_at: "2026-09-13T04:28:23+00:00"
generator: "netsis-scraper 1.0.0"
---
# 9.0.26 Ocak 2020

Netsis 9.0.26 sürümünde yapılan yenilikler aşağıdaki şekildedir:

**1- e-Müstahsil Dizaynında "InvoiceNotes" Alanına Açıklama Girilmesinin Sağlanması**

e-Müstahsil dizaynı e-Devlet XML etiketlerinde "InvoiceNotes" alanının çalışması sağlanmıştır.

**2- e-Müstahsil Fatura Dizaynında Bağkur ve Borsa Kesintilerinin Görünmesi Talebi**

E-Müstahsil fatura dizaynında Bağkur ve Borsa kesintilerinin görünmesi sağlanmıştır.

**3- Amortisman Ayrılmadığı Halde, Rapora Yıllık Amortisman Tutarının Gelmesi İle İlgili Durumun Düzeltilmesi Talebi**

Bazı demirbaşlarda itfa olmasına rağmen, "Değerleme ve Amortisman Raporu" alındığında yıllık amortismanın 0 (sıfır) gösterilmemesi ile ilgili durum düzeltilmiştir.

**4- Kdv Hariç Faturada, İskontodan Önce KDV Hesaplanmasının Sağlanması**

Alış/Satış Parametreleri ve Talep-Teklif Parametreleri ekranlarına "KDV Hariç Faturada İskontodan Önce KDV Düşülsün" parametresi eklenmiştir. Böylece; KDV hariç belge girildiğinde, kalemin KDV'sinin iskonto düşülmeden önceki tutar üzerinden hesaplanması sağlanmıştır.

**5- "AccessDatabaseEngine" Kurulu Olmadığı Zaman Excel Aktarımı Yapıldığında Ekrana Uyarı Gelmesi Talebi**

"AccessDatabaseEngine" kurulu olmadığı durumlarda Excel aktarımının desteklendiği ekranlara "Sürükle Bırak" yöntemi ile XLSX uzantılı dosyalar eklendiğinde, işlemin devam etmeyip uyarı vermesi sağlanmıştır.

**6- Netsis Simge Durumunda İken Bildirimlerin Gösterilmesinin Sağlanması**

Netsis simge durumunda iken, bildirimlerin (Hatırlatıcı, Anlık Mesaj gibi) ana monitörün sağ üstünde gösterilmesi sağlanmıştır.

**7- NetUpdate.exe İle Güncelleme Yapılırken "Logo.Web.Client.Registration.exe.config" Dosyasının Dosya Listesine Gelmemesinin Sağlanması**

NetUpdate.exe ile güncelleme yapılırken "Logo.Web.Client.Registration.exe.config" dosyasının dosya listesine gelmemesi sağlanmıştır.

**8- İthalat İşlemlerinde Masraf Dağıtımı İşleminin Parçalı İthalat İçin Desteklenmesi Talebi**

Dış Ticaret - "Parçalı İthalat Kapatma" işleminde "Stok Bazında Masraf Dağıtım" desteklenmiştir.

**9- Rapordan Grafik Hazırlarken Ekrana Gelen Uyarı İle İlgili Durumun Düzeltilmesi Talebi**

Eski tip raporlarda grafik hazırlarken ekrana gelen uyarı ile ilgili durum düzeltilmiştir.

**10- Serbest Üretim Sonu Kaydı İçin "Kayıtlara Geçilsin" Desteğinin Rest Tarafında Desteklenmesi Talebi**

SERBESTUSK nesnesi altında "Kayıtlara Geçilsin" parametresi desteklenmiştir.

**11- Serbest Üretim Sonu Kaydı İçin NetOpenx Tarafında Fiş Üretildiğinde Stok Hareketleri Aktarılmadan, Liste Şeklinde Kalemleri Dolduracak Bir Özelliğin Desteklenmesi Talebi**

"Serbest Üretim Sonu Kaydı" ekranında bulunan "Kayıtlara Geçilsin" parametresi NetOpenx arayüzünde de desteklenmiştir.

**12- "Tahminleme İşlemleri" Ekranında "Satış Verisi Oluşturma" Sekmesine Geçiş Yaparken, Çevrimdışı Veritabanı Bulunduğunda Ekrana Gelen Uyarı İle İlgili Durumun Düzeltilmesi Talebi**

"Tahminleme İşlemleri" ekranında "Satış Verisi Oluşturma" sekmesine geçiş yaparken, çevrimdışı veritabanı bulunduğunda ekrana gelen uyarı ile ilgili durum düzeltilerek, çevrimdışı veritabanının işleme alınmayıp listelemesi sağlanmıştır.

**13- Serbest Üretim Sonu Kaydı Excel Aktarım Desteği Talebi**

Excel dosyası ile Serbest Üretim Sonu Kaydı yapılması sağlanmıştır. Oluşturulan şablon, Excel dosyası Serbest Üretim Sonu Kaydı penceresine "sürükle-Bırak" yöntemi ile bırakıldığında Excel aktarım adımları başlatılıyor.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=4MiV1uLiuuI&ab_channel=LogoDestek).

**14- Toplu Kalem Ekleme Ekranında Sadece Seçilen Stokların Filtrelenmesi Talebi**

Fatura belgelerindeki "Çoklu Kalem Girişi" ekranında "Seçim" kolon başlığına eklenen filtre özelliği ile, seçilen stokların filtrelenmesi sağlanmıştır.

**15- Netsis Wings ile Netsis'e Giriş Yapılamaması ve Kopyala-Yapıştır İle Türkçe Karakterlerin Bozulması İle İlgili Durumun Düzeltilmesi Talebi**

Windows 1803 versiyonu sonrası Netsis Wings ile Netsis'e giriş yapamama ve CTRL+C CTRL+V ile kopyala-yapıştır yapıldığında Türkçe karakterlerin bozulması ile ilgili durum düzeltilmiştir.

**16- Detaylı Maliyet Analiz Raporunda Mali Grup Kodu ve Ana Grup Kodu Bilgisinin Yanında Mali Grup Kodu İsmi ve Ana Grup Kodu İsimlerinin De Listelenmesi Talebi**

Maliyet Muhasebesi - Raporlar - "Detaylı Maliyet Analiz Raporu" ekranında, "Mali Grup Kodu" ve "Ana Grup Kodu" yanında "Mali Grup İsmi" ve "Ana Grup İsmi" bilgilerinin de listelenmesi sağlanmıştır.

**17- Finansman Raporu Alındığında Kasa ve Banka Borç Tipindeki Toplam Tutarların Ocak Ayında Görünmesi İle İlgili Durumun Düzeltilmesi Talebi**

Cari - Raporlar - Finansman Raporu alındığında "Kasa" ve "Banka Borç kayıtları" Ocak ayı içine kümüle edilip raporlanıyordu. Düzeltilerek, bulunan ay içinde tutarların gösterilmesi sağlanmıştır.

**18- Lokal Depolar Arası Transfer Belgeleri İçin e-İrsaliye Oluşturulmasının Sağlanması**

"Lokal Depolar Arası Transfer" belgeleri için e-İrsaliye Oluşturulması sağlanmıştır. "e-İrsaliye Kullanılsın" parametresi işaretlendiğinde, lokal depo belgelerinde "Cari Kodu" alanı aktif hale gelir.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=j4WTnfBfwJk&ab_channel=LogoDestek).

**19- Depolar Arası Transfer Giden Depoda Onaylanmadığı Halde Aynı Depodaki Serbest Üretim Sonu Kaydında Kontrol Edilmediği İçin Bakiye Uyarısı Vermeden Kaydın Devam Etmesi Durumu İle İlgili İyileştirme Talebi**

Üretim Parametreleri - Üretim-2 - "Üretim Sonu Kaydında Depolar Arası Transfer Onayı Kontrol Edilsin" parametresi eklenmiştir. Bu parametre, 'URETIM','BAKIYEDE_DAT_ONAYINA_BAK' özel parametresi ile aynı şekilde çalışır. Parametrenin aktif hale gelmesi için "Satış Parametreleri" ekranındaki "Şubeler Arası Transfer Fişi Karşı Ambarda Onaylasın" veya "Lokal Depolar Arası Transfer Fişi Onaylasın" parametrelerinin seçilmesi gerekir. Böylece, "Depolar Arası Transfer Onayı" olmayan kayıtların "Serbest Üretim Sonu Kaydı" fişi oluşturulurken miktar kontrolünün yapılması sağlanmıştır.

**20- Hücre Yerleştirme/Toplama Yapılırken, Depo Hareketine Belge Tarihinin (Stok Hareketlerindeki Tarihin) Aktarılması Talebi**

'DINDEPO','BELGE_TARIHI_KULLANILSIN' özel parametresi tanımlandığında hücre yerleştirme veya toplama yapılırken, depo hareketine belge tarihinin (stok hareketlerindeki tarihin) aktarılması sağlanmıştır. Böylece, tüm bakiyeler birbirini tutuyor.

**21- SSO e-Posta Tanımı Yapılırken @xxx.local Şeklinde Olan e-Posta Tanımlaması Yapılmasına İzin Verilmemesi İle İlgili Durumun Çözülmesi Talebi**

Merkezi Kimlik Yönetimi'nin (SSO) "Kullanıcı İşlemleri" ekranından yapılan e-Posta tanımlamalarında, sadece "@" ve "." karakterlerinin kontrol edilmesi sağlanmıştır.

**22- Genel - Log Modülü - İşlemler menüsüne "Log Veritabanı Oluştur" Modülünün Gelmemesi ile İlgili Durumun Düzeltilmesi Talebi**

"Log Veritabanı Oluştur" ekranının - SQL versiyonu 2008 R2 olduğunda - menüye gelmemesi ile ilgili durum düzeltilmiştir.

**23- Aynı Faturaya Bağlı İrsaliyelerin Alt Alta Gelecek Şekilde Listelenmesinin Sağlanması**

Faturalanmış İrsaliye Listesi - Genel Kısıtlar 2 - "Fatura Numarasına Göre Gruplansın" parametresi eklenmiştir. İşaretlendiğinde, aynı faturaya bağlı irsaliyelerin alt alta gelecek şekilde listelenmesi sağlanmıştır.

**24- "e-Faturadan Alış Faturası Oluşturma" Ekranında Fatura Numarası Arama ve Bulma İle İlgili İyileştirme Yapılması Talebi**

"e-Faturadan Alış Faturası Oluşturma" ekranına eklenen Fatura Tarihi, GİB Belge No, Vergi/T.C. Kimlik No ve Cari Unvan alanları ile faturalara kısıt verilmesi desteklenmiştir.

**25- Kalite Hareket Rapor Ekranında Ölçüm Kodlarının Yanında Ölçüm Açıklama Bilgilerinin De Listelenmesi Talebi**

Kalite Kontrol - Raporlar - Kalite Hareket Raporu ekranından alınan raporda, ölçüm kodlarının yanında ölçüm açıklama bilgilerinin de listelenmesi sağlanmıştır.

**26- Bir Stokun Sadece Bir Tedarikçi İçin Kilitlenmesi ve "Genel Kilit" İşaretlendiğinde İlgili Cari İçin İlgili Stokun Kullanılmasının Engellenmesi Talebi**

"Müşteri-Satıcı Stok Kayıtları" ekranındaki "Genel Kilit" seçeneği işaretlendiğinde, ilgili cariler için oluşturulan belgelerde, stokun kullanılması engellenerek, "Stok Kodu Kilitli" uyarısının getirilmesi sağlanmıştır.

**27- Vergi Numarası Girildiğinde e-Defter Gönderiminde Programın Uyarı Vermesi İle İlgili Durumun Düzeltilmesi Talebi**

Şahıs şirketleri için, "B Formu" tanımlamalarında T.C. kimlik bilgisi doldurulup, XML olarak "B Formu" raporunun oluşturulması sağlanmıştır.

**28- Merkezi Kimlik Yönetimi (SSO) Ekranına, "e-Arşiv İptal Faturası Oluşturma" Yetkisinin Eklenmesi Talebi**

Merkezi Kimlik Yönetimi (SSO) ekranına, "e-Arşiv İptal Faturası Oluşturma" yetkisi eklenmiştir. Yetkisi olmayan kullanıcılara, işlem sırasında yetki tanımı yapılması gerektiğine dair uyarı verilmesi sağlanmıştır.

**29- NetUpdate Güncelleme Sonrası Kopyalanmayan Dosyaların Ayrı Bir Açılır Pencerede Gösterilmesi Talebi**

NetUpdate.exe ile yapılan güncelleme işleminde, güncellenmeyen dosyaların ayrı bir ekranda gösterilmesi sağlanmıştır.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=l8jxc4YB8hs&ab_channel=LogoDestek).

**30- NetUpdate Uygulamasında Ekrandaki Dosyaları Yükleme Aşamasında Yapılan "Kullanımda" Kontrolünün Kaldırılması Talebi**

NetUpdate ile güncellenecek dosyalar listelenirken "Kullanımda" kontrolünün yapılması kaldırılmıştır.

**31- Modül Bazında Tarih Kilitleme Ekranında Seçili Satır Değerlerinin Tüm Satırlara Kopyalanmasının Sağlanması**

"Modül Bazında Tarih Kilitleme" ekranına "Satırlara Kopyala" butonu eklenmiştir. Butona tıklandığında, gridde seçili satır değerlerinin diğer satırlara kopyalanması sağlanmıştır.

**32- Cari Hareket Kayıtları Ekranında Dekont Hareketleri İçin "e-Belge Görüntüleme" İşleminin Yapılması Talebi**

"Cari Hareket Kayıtları" ekranında, dekont hareketleri için de "e-Belge Görüntüleme" işleminin yapılması sağlanmıştır.

**33- MT940 Entegrasyonunda Kurala Bağlı Gelen Cari ve Muhasebe Kod Açıklamalarının Gridde Görülmesinin Sağlanması**

MT940 entegrasyonunda kurala bağlı gelen cari ve muhasebe kod açıklamalarının gridde görülmesi sağlanmıştır.

**34- e-İrsaliye Mükellefine Belge Girilirken, E-İrsaliye Carisi Olduğuna Dair Uyarı Mesajının Gelmesi Talebi**

e-İrsaliye mükellefine belge girilirken, "E-İrsaliye" kutucuğunun program tarafından otomatik olarak işaretli gelmesi sağlanmıştır. "e-İrsaliye" kutucuğu kaldırılarak belge oluşturulması istendiğinde ise e-İrsaliye carisi olduğuna dair ekrana uyarı mesajının gelmesi sağlanmıştır.

**35- Cari İrtibat Bilgileri Ekranında e-Posta Alanının 255 Karakterden Fazla Olması Talebi**

"Cari İrtibat Bilgileri" ekranında e-Posta alanının karakter sayısı 1000'e yükseltilmiştir.

**36- Dekont Modülünde Excel'den Kalem Bilgilerinin Aktarılması Talebi**

Genel dekont kaydı kalemlerinin kaydedilmesi için Excel'den aktarım desteklenmiştir. Dekont üst bilgileri girildikten sonra Excel dosyası "Sürükle-Bırak" yöntemi ile aktarılabilir.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=4MiV1uLiuuI&ab_channel=LogoDestek).

**37- Log Raporu Alırken Farklı Şubelerde Aynı Kullanıcı Numarası İle Tanımlı Kullanıcıların Kullanıcı Adı Bilgisinin Doğru Gelmesinin Sağlanması**

Log raporu alırken farklı şubelerde aynı kullanıcı numarası ile tanımlı kullanıcıların, kullanıcı adı bilgisi yanlış geliyordu. Düzeltilerek, "Kullanıcı No" bilgisi aynı olan farklı şubelerdeki kullanıcılara göre kayıtların raporlanması sağlanmıştır.

**38- İş Emri Ekranında Sağ Tuş İle Ekrana gelen Reçeteden İş Emri Oluşturma Ekranında Stok Adının Görünmesi Talebi**

İş emri ekranında sağ tuş ile ekrana gelen "Reçeteden İş Emri Oluşturma" seçeneği ile açılan "Açılacak İş Emirleri" ekranına "Stok Adı" alanı eklenmiştir.

**39- Diyalogoda Olan Faturaların Bazı Zamanlarda Netsis'e Düşmemesi İle İlgili Durumun Düzeltilmesi Talebi**

e-Logo Entegratör Fark Raporu'nun varsayılan olarak "Netsis'e Fatura İndirilmemiş" durumundaki kayıtları listelemesi sağlanmıştır. İstendiği zaman, ekranın "Kısıt" alanına eklenen "Tüm Faturalar Listelensin" seçeneği ile tüm faturaların görüntülenmesi sağlanır.

**40- Gelir Tablosuna Dönem ve Tarih Seçeneğinin Eklenmesi Talebi**

İşletme Gelir Tablosu'na "Dönem ve Tarih Bilgisi Basılsın" seçeneği eklenmiştir. İşaretlendiğinde, raporun alındığı dönem ve tarih bilgisi rapor başlığına yazılır.

**41- Çizelgelenen İş Emirleri Taslak Olarak Kaydedildikten Sonra Kaydedilen Taslak Tekrar Açıldığında Çizelgelenmeyen İşler Raporunun Çalışmaması İle İlgili Durumun Düzeltilmesi Talebi**

"İleri üretim Planlama" ekranında çizelgeleme işlemi sonucu "Çizelgelenmeyen İşler Raporu" bilgilerinin taslak numarası bazında kaydedilmesi sağlanmıştır. Bu geliştirme ile kaydedilmiş taslağı, Gantt ekranındaki "Çizelgelenemeyen İşler Raporunun" getirmesi sağlanmıştır. Aynı rapor, MRP - Raporlar - "İleri Üretim Çizelgeleme" bölümü altında da taslak numarasına göre raporlanabilir.

**42- Taksitli Kredilerde Ödeme Planının Elle (Manuel) Girilmeden Banka Entegrasyonu İle Sisteme Aktarılması Talebi**

"Taksitli Kredi Açma" ve "Uzun - Orta Vadeli Kredi Açma" ekranlarının "Ödeme Planı" sekmesinde Excel'den aktarım desteklenmiştir.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=4MiV1uLiuuI&ab_channel=LogoDestek).

**43- Talep Siparişleştirme Ya Da Teklif Siparişleştirme Ekranlarının Bilgi Gösterim Ekranında İstenen Sahalar İle İstenmeyen Sahaların Göründüğü Yerlerin Değiştirilmesinin Sağlanması**

"Satış Talep Siparişleştirme", "Satış Teklif Siparişleştirme", "Satınalma Talep Siparişleştirme" ve "Satınalma Teklif Siparişleştirme" ekranlarının "Bilgi Gösterim" sekmesindeki grid, akıllı grid olarak değiştirilmiştir. Böylece, gridde filtreleme veya sıralama gibi özellikler kullanılabilir. Eski gridin kullanılması için 'GRID','PERFORMANS','Modulno_Programno' olarak özel tanımlama yapılması gerekir. "Değer" alanında değerler arasına ";" eklenerek 1'den fazla program eklenebilir.

Örneğin;

40_6;40_7 gibi.

**44- Reçetelerde Brüt Miktar Girişi Yapıldığında Maliyetlendirme Veya Üretim Sonu Kaydı Sonucu Olması Gerekenden Daha Az Malzeme Kullanıldığı Görünmesi Üzerine Yanlış Yorumlamaya Sebep Olmaması İçin Gereginin Yapılması Talebi**

"Reçete Kaydı" ekranında herhangi bir bileşenin 'Fire Miktarı' oranının "Malzeme Gereksinim Planlama" sonucu hesaba katılmasını sağlamak amacıyla 'MRP','FIREORANI_DIKKATE_ALINSIN' özel parametresi desteklenmiştir. Böylece, MRP çalıştırma sonucu gereksinim miktarına fire oranı da eklenecektir.

**45-** **"Kullanıcı e-Posta Tanımları" Ekranında Bakım Talepleri ve Bakım Emirleri için SMS Gönderilmesi Desteği**

"Bakım Emri" ve "Bakım Talep" ekranları için "SMS Uygulaması" desteklenmiştir. SMS uygulamasını açtıktan sonra "Kullanıcı e-Posta Tanımları" ekranından SMS gönderilmesi istenen durumlarda, işlemlerden istenen bakım emir veya talep işlemleri seçildikten sonra "Cep Tel." alanındaki rehberden kullanıcı seçilerek SMS gönderilmesi istenilen kullanıcılar seçilebilir.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=YGGSjqB8slU&ab_channel=LogoDestek).

**46- Ambar Çıkış Fişi Oluşturulduğunda, Oluşan Yevmiye Kaydının Stokun Detay Kodundaki Alış Hesabını Çalıştırması Talebi**

FATURA/AMBARHESKODGETIR özel parametresi ile, Entegrasyon Kodları - "Fatura Genel" sekmesindeki "Depolar Arası Transfer Entegre" seçeneği kullanıldığı zaman, ambar giriş/çıkış belgelerinde çalışacak olan muhasebe hesabının belirlenmesi sağlanmıştır. "Depolar Arası Transfer Entegre" seçeneği ile Satış Diğer-3 hesabı çalışırken, özel parametrenin "Değer" alanına yazılan değere göre stokun muhasebe detay kodundaki diğer hesapların da çalıştırılması desteklenmiştir. Satış Diğer 1, 2, ..., 8 hesapları için parametrenin "Değer" alanına 1, 2, ..., 8 , Alış Hesabı için 9, Alıştan İade için 10, Satış Hesabı için 11 ve Satıştan İade Hesabı için de 12 değerinin yazılması gerekir.

**47- İthalat İşlemlerinde Masraf Dağıtımı İçin Ek Geliştirme Talebi**

"Stok Bazında Masraf Dağıtım" ekranının, dosya işlemleri "Masraf" sekmesinde de açılması sağlanmıştır. Masraf dağıtımı bulunan satırda farenin sağ tuşu ile bu ekrana ulaşılabilir. "Masraf Dağıtım" ekranında iken farenin sağ tuşu ile ekrana Tümünü Seç/Kaldır butonları, Oran ve Tutarları Temizleme eklenmiştir. "Masraf Dağıtım" ekranının açılmadığı durumlarda kullanıcının program tarafından uyarılması sağlanmıştır.

**48- Döviz Kuru Eklentisinde Görüntülenecek Kurun Seçilmesinin Sağlanması**

Döviz Kuru Eklentisinde Görüntülenecek Kurun Seçilmesinin Sağlanması"Döviz Kuru" eklentisi ayarlarına, "Döviz Çevrim Tipi" seçeneği eklenmiştir. Eklentideki kur değeri, bu alandaki "Şirket-Şube Parametrelerinden Getir", "Alış", "Satış", "Efektif Alış" ve "Efektif Satış" seçeneklerine göre görüntülenecektir.

**49- MT940 Kayıtlarından İşlem Kodlarına HGS ve OGS Eklenmesi Talebi**

MT940 kayıtlarından işlem kodlarına HGS ve OGS eklenmiştir. Eklenen işlem kodlarının genel dekont kural bilgileri ile eşleştirilmesi sağlanmıştır.

**50- Müşteri Puan Bakiyesi Raporunun Alınmasını Sağlayacak Bir Rapor Seçeneğinin Eklenmesi Talebi**

"Cari Sabit Listesi" raporunda dosya sahalarına "Puan" alanı eklenmiştir. İlgili rapor ile, carilerin puan durumunun raporlanması sağlanmıştır.

**51- Stok Planlama Kayıtlarına Eklenen "Üretim Transfer Süresi" Alanının Müşteri Satıcı Stok Kayıtları Ekranına da Eklenmesi Talebi**

"Stok Planlama Kayıtları" ekranına eklenen "Üretim Transfer Süresi" alanı, "Müşteri-Satıcı Stok Kayıtları" ve "Cari Planlama Kayıtları" ekranlarına da eklenmiştir. Üretim transfer süresine ait girilen bu kayıtların önceliği, "Müşteri-Satıcı Stok Kayıtları", "Cari Planlama Kayıtları" ve "Stok Planlama Kayıtları" ekranlarında belirtilen sıralamaya bağlıdır.

**52- Hatırlarıcı Bildirimlerinin Kullanıcı Tarafından Kapatılana Kadar Ekranda Kalmasının Sağlanması**

Hatırlatıcı bildirimlerinin kullanıcı tarafından kapatılana kadar ekranda kalması sağlanmıştır.

**53- e-Posta Log Raporunda e-Posta İçeriğinin Görüntülenmesi Talebi**

"e-Posta Log Raporu" ekranının başlık hücresine fare ile çift tıklandığında e-posta içeriğinin - içerik yoksa fare ile çift tıklama yapılamaz- görüntülenmesi sağlanmıştır.

**54- Kalem Bazında Doküman Ekleme Desteğinin Proforma Faturada Da Desteklenmesi Talebi**

"Dış Ticaret" modülünde kalem bazında "Belge Ekleme" işlemi desteklenmiştir. İhracat Dosya İşlemleri için "Detay Gösterme" ekranının "Kalem Bilgileri" sekmesinden, İthalat Dosya İşlemleri için ise "Dosya Siparişleri" ve "Faturalarım" sekmesinden işlem yapılır.

**55- Ekranlardaki Araç Çubuğundan "Bağlantıyı Kopyala" Butonu İle Aktif Kaydın "Bildirim Girişi", "Anlık Mesajlaşma" ve "Hatırlatıcı" Ekranlarında Kolayca Eklenmesi Talebi**

"Veritabanı İşlemleri" menüsünde bulunan "Bağlantı Kopyala" işlemi ile kopyalanan kayıtların, "Bildirim Girişi" ve "Anlık Mesajlaşma" ekranlarına eklenen "Bağlantı Yapıştır" seçeneği ile kolayca paylaşılması sağlanmıştır.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=ZBLtiMFxwBY&ab_channel=LogoDestek).

**56- Hatırlatıcı Eklentisindeki "Belge Bağlantısı" Bölümünün Bildirim Servisindeki Belge Bağlantısıyla Aynı Olacak Şekilde Desteklenmesi Talebi**

"Hatırlatıcı" eklentisi ekranına "Dosya Ekleme" seçeneğiyle birlikte "Netsis Link" ve "Bağlantı Yapıştır" özellikleri de eklenmiştir.

**57- Seri Girişi Sırasında Desteklenen Opsiyonel Alanların NetOpenX Fatura Nesnesinde Desteklenmesi Talebi**

"Seri Parametreleri" ekranında bulunan opsiyonel sahalar, NetOpenx Seri Giriş ekranında da desteklenmiştir. Bu sahalar, Temelset tarafı seri parametrelerinde opsiyonel sahaların aktif olması durumunda, aktarım yapılırken dikkate alınacaktır.

**58- Netsis Profiler Üzerinde Yığın İzleme'nin Varsayılan Olarak Açık Gelmesi ve "Modül Adı" Kolonunda Sürüm Bilgisinin Görünmesinin Sağlanması**

"Netsis Profiler" uygulamasına, çalışan modül dosyalarının versiyon bilgilerini gösteren kolon eklenmiştir.

**59- Makine, Bakım Emri veya Makine Grubu Bazında Bakım Maliyet Raporunun Eklenmesi Talebi**

Makine Bakım - Raporlar menüsünün altına "Bakım Emri Masraf Raporu" ismiyle yeni bir rapor eklenmiştir. Eklenen rapor, "Bakım Emirleri" ekranında eklenen masraf faturalarını raporlar. "Fatura Detayları Gösterilsin" parametresi ile de, eşleşen bakım emri ve alış faturalarının raporda detaylı olarak gösterilmesi desteklenmiştir.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=Vgjy5l1cpS4&ab_channel=LogoDestek).

**60- Bakım Emri Ekranına Dışarıdan Hizmet Tipli Bakım Şablonları İçin Alış Faturası Eşleştirme Desteğinin Sağlanması Talebi**

Makine Bakım - Kayıt - "Bakım Emirleri" ekranına sağ tuş özelliği olarak "Masraf Faturası Seç" seçeneği eklenmiştir. Seçildiğinde, Grid üzerinde çoklu seçim yapılacak şekilde alış fatura kalemlerinin listelenmesi sağlanır. Eklenen seçenek ile alış faturalarının listelenmesi için Bakım Talimat Şablonunun ''Dışarıdan Hizmet" olarak tanımlanması gerekir.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://youtu.be/k0z3ZwDnnJs).

**61- Seri İzleme Ekranında Opsiyonel Sahaların Gösterilmesi Talebi**

Stok Hareket Kayıtları ekranında iken farenin sağ tuşu ile ekrana gelen "Seri İzleme" seçeneğinde, serinin opsiyonel sahalarının gösterilmesi sağlanmıştır.

**62- Çoklu Kalem Girişi Desteği Gibi Toplu Kalem Güncelleme İşlem Desteğinin Sağlanması**

Fatura, irsaliye, ambar işleri, depolar arası transfer, sipariş ve talep teklif ekranlarında grid üzerinde iken farenin sağ tuşu ile açılan menüye "Toplu Kalem Güncelleme" seçeneği eklenmiştir. Seçeneğin menüde görünmesi için, kalem bilgilerine en az 2 stokun girilmesi gerekir. Bu ekran ile Miktar, Miktar 2, Fiyat, Döviz Fiyat, Muhasebe Referans Kod, Depo Kodu, Proje Kodu, Vade Günü, Vade Tarihi, Koşul Kodu, KDV Oranı, Teslim Cari, Fiili Tarih, Yükleme Tarih ve Sipariş Teslim Tarihi alanları - alanlar, ekranlara göre değişebilir - güncellenebilir. Güncelleme gridde seçilen stoklar, güncellenecek alan, yöntem ve değere göre kalemlere yansıtılır ve "Kaydet" butonuna tıklandıktan sonra güncelleme işlemi yapılır.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=4PtoZXZBy_g&ab_channel=LogoDestek).

**63- Vakıfbank MT940 Gelen Ekstrede COL İşlem Kodu Olduğu Halde İşlem Kodları Girişinden COL İşlem Kodunun Eklenememesi İle İlgili Durumun Düzeltilmesi Talebi**

"MT940 İşlem Kodları" ekranına "COL-Otomatik Ödemeler" tipi eklenmiştir. Bu işlem tipi ile genel dekont kaydı oluşturulması sağlanmıştır.

**64- Geçici Beyanname'de "Yurtdışı Mukimi Kişi ve/veya Kurumlara Verilen Eğitim Hizmetlerine İlişkin Form" Eki Desteği Talebi**

Geçici Beyanname'de "Yurtdışı Mukimi Kişi ve/veya Kurumlara Verilen Eğitim Hizmetlerine İlişkin Form" eki desteklenmiştir.

**65- Geçici Vergi Beyannamesi Ekranında "Yurtdışı Mukimi Kişi ve/veya Kurumlara Verilen Sağlık Hizmetlerine İlişkin Form" Eki Talebi**

Geçici Vergi Beyannamesi ekranında "Yurtdışı Mukimi Kişi ve/veya Kurumlara verilen Sağlık Hizmetlerine İlişkin Form" eki desteklenmiştir.

**66- Reçete Kopyalama İşleminde Reçetedeki Ek Bilgilerin Kopyalanması Talebi**

"Reçete Kopyalama" işlemi sırasında reçete içindeki ek sahaların da kopyalanması desteklenmiştir.

**67- Kantar Tartım Fişlerini Oluştururken Otomatik Olarak İrsaliye Oluşturulmasının Engellenmesi Talebi**

"Kantar-Tartım" modülüne "Tartım Bilgilerinden Belge Oluşturma" ekranı eklenmiştir. "Hareket Girişi" ekranından irsaliye oluşturulmadan çıkılması ve işlemlere "Tartım Bilgilerinden Belge Oluşturma" ekranından devam edilmesi sağlanmıştır.

**68- Damga Vergisi Muhasebeleştirme İşleminin Şubelerden De Yapılması Talebi**

"Damga Vergisi Muhasebeleştirme" işleminin şubelerden de yapılması sağlanmıştır.

**69- Excel Dosyasından "Sürükle-Bırak" Yöntemi İle Mamul Grup Kodu Kayıtlarının Oluşturulmasının Sağlanması**

"Mamul Grup Kodu Kayıtları" ekranında, Excel'den Netsis'e aktarım işlemi desteklenmiştir.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=4MiV1uLiuuI&ab_channel=LogoDestek).

**70- Bakım Emirleri Ekranında Kayıt Yeri "Bakım Talebi" Olan Belgeler İçin "Bakım Talep No" Bilgisinin Gösterilmesi Talebi**

Makine Bakım - Kayıt - "Bakım Emirleri" ekranındaki listeye "Bakım Talep No" alanı eklenmiştir. Bakım emirleri listesinde "Kayıt Yeri" bilgisi "Bakım Talebi" ise "Bakım Talep No" bilgisi de listelenecektir.

**71- Cari Muhasebe Açıklama Kayıtlarında Hızlı Tahsilat Kaydının Desteklenmesi**

Cari Muhasebe Açıklama Kayıtları - Hızlı Tahsilat Kaydı desteklenmiştir. "Entegrasyon Çalışılan Kasa Açıklaması" seçeneği ile kasanın muhasebe hesabına giden açıklama, "Entegrasyon Cari Genel Açıklama" seçeneği ile carinin muhasebe hesabına giden açıklama, "Cari Genel Açıklama" seçeneği ile de cari hareket kayıtlarına giden açıklama bilgisi değiştirilmesi sağlanmıştır.

**72- İleri Üretim Planlama Lisansı Varsa ve MRP Parametrelerinde "İleri Üretim Planlama" Parametresi Seçilmişse, İş Emri Ekranındaki "Sıralama Önceliği" Alanının Aktif Halde Görünmesi Talebi**

"İleri Üretim Planlama" lisansı varsa ve MRP parametrelerinde "İleri Üretim Planlama" parametresi seçili ise, "İş Emri Girişi" ekranındaki "Sıralama Önceliği" alanının aktif halde görünmesi sağlanmıştır.

**73- Kalite Süreci Tamamlanmayan Belgenin Faturalandırılmasının Engellenmesi Talebi**

Alış irsaliyesinden fatura oluştururken kalite kontrol kaydı kontrolü yapan 'FATURA','KALITE_ZORUNLU' özel parametresiyle beraber "Kalite Kontrol Parametreleri" ekranına "Kalite Kontrol Kaydı Kapatılmayan Alış İrsaliyeleri Faturalaştırılamasın" ismiyle yeni bir parametre eklenmiştir. İlgili parametre ile, kalite kontrol kaydı olmayan alış irsaliyelerinin faturalandırılması engellenmiştir.

**74- Toplu Yazıcı Atama Talebi**

Dizayn - İşlemler menüsüne "Toplu Yazıcı Atama" bölümü eklenmiştir. Bu ekran ile, dizaynlara atanan yazıcıların görülüp, toplu olarak değiştirilmesi sağlanmıştır.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=ZCLOSmafLlI&ab_channel=LogoDestek).

**75- MRP Parametrelerine Tamamlanmamış Taleplerin Dikkate Alınmasını Sağlayacak Parametre Eklenmesi Talebi**

MRP Parametreleri - Genel-2 sekmesine "Tamamlanmamış Satınalma Belgeleri MGP'ye Dahil Edilsin" parametresi eklenmiştir. Bu parametrenin aktif olması durumda MRP çalıştırırken, tamamlanmamış durumda olan satınalma talep ve satıcı siparişleri hesaba katılacaktır. Aksi durumda ise sadece tamamlanmış belgeler hesaba katılacaktır.

**76- Gelişmiş Rapor Fonksiyonlarının Çalışmasının Sağlanması**

Gelişmiş raporun desteklediği araçların çalışması sağlanmıştır. Desteklenmeyen araçlar gelişmiş rapordan kaldırılmıştır.

**77- "Fire Muhasebe Kodu Detaylı" Parametresi İşaretlenmediğinde Ekrana Gelen "İşlem Başarısız" Uyarısı İle İlgili Durumun Düzeltilerek Seçim Yapılmadan "Tamam" Butonuna Tıklanmasının Engellenmesi**

Üretim - İşlemler - Üretim Sonu Kayıtları Entegrasyonu - "Fire Muhasebe Kodu Detaylı" parametresi işaretli değilse "Tamam" butonuna tıklandığında, ilgili "Fire Muhasebe Kodu" seçeneklerinden biri seçili değilse "İşleme devam edebilmek için fire muhasebe kodu alanı doldurulmalıdır." uyarısın gelmesi sağlanmıştır.

**78- Cari Hesap Bazında Cari Muhasebe Fark Listesinin Alınması Talebi**

"Cari Muhasebe Fark Listesi" raporu alındığında "Muhasebe Koduna Göre Kümülasyon Yapılmasın" seçeneği işaretlenmesine ve Cari Borç/Cari Alacak değerlerinin cari koda göre detay göstermesine rağmen Muhasebe Borç ya da Muhasebe Alacak değerlerini kümüle gösteriyordu. Düzeltilerek, "Muhasebe Koduna Göre Kümülasyon Yapılmasın" seçeneğinin işaretlenmesi durumunda muhasebe borç ve alacak değerlerinin detay olarak gösterilmesi sağlanmıştır.

**79- Hizmet Prim Uygulamasında Döviz Desteğinin Sağlanması**

"Hizmet Prim Uygulaması" için döviz desteği getirilmiştir. Böylece, dövizli hizmet prim tanımının yapılması ve döviz değerleri üzerinden hizmet prim faturası oluşturulması sağlanmıştır.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=xrwRqm2WYoE&ab_channel=LogoDestek).

**80- Kullanıcı Tanımlı Sahalara Form Bazında Güvenlik Tanımlaması Yapılarak Bazı Alanlara Kontrol ve Güvenlik Eklenmesinin Sağlanması**

"Saha Tablo Eşleştirmesi" ekranından tanımlaması yapılan "Kullanıcı Tanımlı Sahalar" için "Form Bazı Güvenlik" tanımlamasının yapılması desteklenmiştir.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=EcOEkVbYUK4&ab_channel=LogoDestek).

**81- Entegrasyon Kodlarında Borç Kısmında Oluşacak Yuvarlamalar İçin Ayrı, Alacak Kısmında Oluşacak Hesaplar İçin Ayrı Muhasebe Hesabının Girilmesi Talebi**

Yuvarlama farklarının muhasebede borç ve alacak olarak iki ayrı hesaba atılması sağlanmıştır. Kullanılması istenen muhasebe hesap kodları, entegrasyon kodları genel sekmesinden seçilebilir. Bu özellik, 9.0.26 onaylı sürüm ve sonrası olan kullanıcılarda kullanılabilir.

**82- e-Faturası Oluşturulan Sigara Faturasında KDV Tutarının Görünmemesi Talebi**

"Toplu e-Fatura Oluşturma" işleminde, sigara faturaları için otomatik olarak "806 - Özel Matrah" kodunun atanması ve KDV'nin sıfırlanması desteklenmiştir.

**83- İstatistiksel Proses Kontrol Uygulamasının Desteklenmesi**

İstatistiksel proses kontrol kayıtlarının girişi ve kontrol grafiklerinin raporlanması için gerekli geliştirmeler yapılmıştır. İstatistiksel proses kontrol kayıtları makine, kaynak, istasyon veya fabrika geneli için girilebilir. Benzer şekilde "Üretim Akış Kaydı" ekranında iş emri ve operasyon kodu bazında ölçüm kayıtları girilerek istatistiksel kontrol grafikleri raporlanabilir.

> [!NOTE]
> Madde ile ilgili ilk video için [tıklayınız](https://www.youtube.com/watch?v=z_FJreEb_q0&ab_channel=LogoDestek).
>
> Madde ile ilgili ikinci video için [tıklayınız](https://www.youtube.com/watch?v=0hhUOHZl4ns&ab_channel=LogoDestek).

**84- Aynı Ağ Üzerindeki Mevcut SSO Kurulumlarının Kontrolü İle İlgili Düzenleme Talebi**

Aynı ağ üzerinde farklı lisans ve farklı SQL Server Instance olması durumunda, birden fazla SSO kurulumunun gerçekleştirilmesi desteklenmiştir.

**85- Kayıtlı Olmayan Alıcıya e-İrsaliye Düzenlenmesi Talebi**

e-İrsaliye mükellefi olmayan cari hesaplar için de e-İrsaliye kaydedilmesi sağlanmıştır.

> [!NOTE]
> Madde ile ilgili video için [tıklayınız](https://www.youtube.com/watch?v=1zOnWcmQaoQ&ab_channel=LogoDestek).

**86- NetOpenx'de Kayıtlı Olmayan Alıcıya e-İrsaliye Düzenlenmesi Talebi**

e-İrsaliye mükellefi olmayan cari hesaplar için NetOpenx tarafında da e-İrsaliye oluşturulması desteklenmiştir.

**İyileştirmeler**

**1- Sevk Emrinden Yükleme Emri Oluşturulması İstendiğinde Ekrana Gelen "incorrect syntax" Uyarısı İle İlgili Durumun Düzeltilmesi Talebi**

Sevk emrinden yükleme emri oluşturulması istendiğinde ekrana gelen uyarı ile ilgili durum düzeltilmiştir.

**2- Tarih Aralıklı Mizanda Bazı Muhasebe Hesap Planlarında Cari Hesap Kayıtlarının Açılması İle İlgili Durumun Düzeltilmesi Talebi**

Tarih aralıklı mizanda bazı muhasebe hesap planlarında cari hesap kayıtlarının açılması ile ilgili durum düzeltilmiştir.

**3- SQL Server 2019 Kurulu Sunucuda "Log Veritabanı Oluştur" Bölümünün Ekrana Gelmesinin Sağlanması**

MS SQL Server 2019 kurulu sunucuda "Log Veritabanı Oluştur" bölümünün ekrana gelmesi sağlanmıştır.

**4- Müşteri Siparişi Kalemler Sekmesinde Yapılandırma Kodu Alanından İlerlenmesi İstendiğinde Ekrana Gelen Uyarı İle İlgili Durumun Düzeltilmesi Talebi**

Fatura veya sipariş kalemlerinde, "Esnek Yapılandırma Kodu" oluşturduktan sonra, "Esnek Yapılandırma Kodu" alanından ilerlenmesi istendiğinde ekrana gelen uyarı ile ilgili durum düzeltilmiştir.

**5- Oluşan Dekontta Cari ve KDV Satırı İçin Kur Bilgisinin, Demirbaş Kartında Kullanılan Kur Bilgisinden Alınmasının Sağlanması**

Demirbaş kartından dekont kaydı oluşturulurken, dövizli demirbaşlar için kur bilgisinin, demirbaş kartında kullanılan kur bilgisinden alınması sağlanmıştır.

**6- Genel Dekont Kaydında Girilen Stok Kodunun Cari Kod İle Aynı Olması Durumunda, Stok Kodu Girerken e-Posta Gönderimi Yapılması İle İlgili Durumun Düzeltilmesi Talebi**

"Genel Dekont Kaydı" ekranında, e-Posta gönderim kontrolü her kalem tipi için yapılıyordu. Düzeltilerek, sadece cari için yapılması sağlanmıştır.

**7- Yan Ürün İçeren Serbest Üretim Sonu Kaydı ve Üretim Sonu Kaydı Fişlerinde Depo Önceliği Tanımlarında Belirtilen Depo Kodlarının Dikkate Alınmaması İle ilgili Durumun Düzeltilmesi Talebi**

Yan ürün içeren ürün reçeteleri için "Üretim Sonu Kaydı" ve "Serbest Üretim Sonu Kaydı" ekranlarında depo önceliği seçenekleri (Stok Depo Kullan, İş Emri Depo Kullan, Üretim Depo Kullan) kullanılarak yapılan kayıtlarda, ilgili seçeneklere bağlı depo hareketi oluşturulması sağlanmıştır.

**8- Cari Devir Ekranının Cari Kısıtları Sekmesinde "Plasiyer Kısıtı" Verilirken Rehberin Görüntülenmemesi İle İlgili Durumun Düzeltilmesi Talebi**

Sene Sonu Devir - Cari Devir - "Cari Kısıtları" sekmesinde "Saha Adı" olarak PLASIYER_KODU seçildikten sonra "Operatör" seçildiğinde rehberin görüntülenmemesi ile ilgili durum düzeltilmiştir.

**9- Satış Faturası Ekranında Sipariş Kayıtlarının Mal Bazında Ekrana Getirtilip Fatura Oluşturulması İstendiğinde Fatura Numarası Sonrası Fatura Tarihi Değiştirildiğinde Resmi Evrak Numarasının Değişmemesi İle İlgili Durumun Düzeltilmesi Talebi**

Faturadan sipariş teslim edilirken fatura tarihi değiştirildiğinde "Resmi Numara" alanının güncellenmemesi ile ilgili durum düzeltilmiştir.

**10- Onayda Bekleyen Siparişin Yeni Yıl Şirketine Devredilmemesinin Sağlanması**

"İş Akış Uygulaması" açık olduğunda, Sene Sonu Devir - "Yeni Yıl Kopyalama" işlemi sırasında iş akış onay süreci tamamlanmayan kayıtların yeni sene şirketine aktarılmayacağına dair uyarı mesajının ekrana gelmesi sağlanmıştır.

**11- Detaylı Fiyat Listesi Parametresi Kullanımda İken, Fiyat Listesi Tanımlama Ekranında Görüntülenen Uyarı İle İlgili Durumun Düzeltilmesi Talebi**

"Stok Fiyat Listesi Tanımlama" ekranında "Sıralama" kısıdı sekmesinde ekrana gelen uyarı ile ilgili durum düzeltildi.

**12- Hizmet Prim Uygulamasında Prim Belgesi Oluşacak Stok Kartında Depo Kodu Tanımlı Değilse, Prim Belgesi Oluşurken Ekrana Gelen Uyarının Düzeltilmesi Talebi**

Hizmet prim uygulaması prim belgesi oluşturma ekranında, "Depo Kodu" girilmesi sağlanarak uyarı ile ilgili durum düzeltilmiştir.

**13- Planlı Bakım İş Emirleri Mevcut Bakım İş Emri Serisinin Devam Etmemesi İle İlgili Durumun Düzeltilmesi Talebi**

"Bakım Planlama" ekranı üzerinden bakım emri oluşturulduğunda, iş emri serisinin bakım emirlerinde tanımlı olan seri kodu üzerinden devam etmemesi ile ilgili durum düzeltilmiştir.

**14- Oracle Veritabanı Personel Paketinde Log Raporu Alırken Ekrana Gelen Uyarı İle İlgili Durumun Düzeltilmesi Talebi**

Oracle veritabanı "Log Raporu" alırken ekrana gelen uyarı ile ilgili durum düzeltilmiştir.

**15- NetOpenx FisAna Nesnesi Tarih Kilidi Uyarısı İle İlgili Durumun Düzeltilmesi Talebi**

FisAna nesnesinin altına "Entegre Tarihi" alanı eklenmiştir. Açık tarih aralığı için ilgili tarih bilgisi girilerek işlem yapılması gerekir.

**16- "e-Fatura'dan Alış Faturası Oluşturma" İşleminde Kilitli Carilere İşlem Yapılmasının Engellenmesi Talebi**

"e-Fatura'dan Alış Faturası Oluşturma" işleminde kilitli carilere işlem yapılması engellenmiştir.

**17- USK ve Serbest USK Ekranlarında Depo Önceliği Olarak "İş Emri" Seçildiğinde, Bileşenler İçin Eksi Bakiye Kontrolünün İş Emrindeki Depo Kodu Üzerinden Yapılmasının Sağlanması**

"Üretim Sonu Kaydı" ve "Serbest Üretim Sonu Kaydı" ekranlarında, depo önceliği olarak "İş Emri Depo Kullan" seçeneği seçildiğinde yapılan üretim sonu kaydı fişlerinde bakiye kontrolü iş emrindeki depo kodu üzerinden yapılmıyordu. Düzeltilerek, iş emrinde belirtilen depo üzerinden bakiye kontrolü yapılması sağlanmıştır.

**18- İletişim İzinlerinde İlgili Cari İçin Bitiş Tarihi Geçmesine Rağmen Yeni Belge Girildiğinde Mail Gönderilmesi İle İlgili Durumun Düzeltilmesi Talebi**

"İletişim İzin Kayıtları" ekranında iletişim izin tarihi geçmiş bir kayıt için KVKK\\ILETISIM_IZNI_ZORUNLU\\0 özel parametresinin tanımlı olmadığı durumlarda mail gönderilmesi ile ilgili durum düzeltilmiştir.

**19- Netsis Wings Toplu e-Arşiv Basım Ekranında Fatura İçine Girilmeden Basım Yapılması İstendiğinde, Belge İçinin Ekrana Boş Gelmesi İle İlgili Durumun Düzeltilmesi Talebi**

Netsis Wings "Toplu e-Arşiv Basımı" ekranındaki basım ile ilgili durum düzeltilmiştir.

**20- Tarih Kırılım Parametresi İle Alınan Raporun Gün Bazında Toplam Vermesi Talebi**

"Cari Hareket Dökümü" Raporu "Tarih Kırılımlı" seçeneği seçilerek alındığında, tarih bazında alt toplamlar gelmiyordu. Düzeltilerek, gün bazı toplamında listelenmesi sağlanmıştır.

**21- Genel Dekont Kaydı Tamamlanırken e-Fatura Uygulaması Kullanılmadığında "e-Fatura Cari Eşleştirme" Ekranının Görüntülenmemesi Talebi**

"e-Fatura Uygulaması" kullanılmadığında, "Genel Dekont Kaydı" ekranında "e-Fatura Cari Eşleştirme" ekranının görüntülenmemesi sağlanmıştır.

**22- NetUpdate.exe İle Dosyalar Güncellendikten Sonra Servisler Güncellenirken, İlgili Servis Durduğunda Ekrana Gelen Uyarı İle İlgili Durumun Düzeltilmesi Talebi**

NetUpdate.exe ile güncelleme yapılırken güncellenecek servis duruyorsa, servisin güncellenerek tekrardan başlatılması sağlanmıştır.

**23- Reçete İzleme Seçeneğinde Yan Ürün Tipli Bileşen Adlarının Listelenmesi Talebi**

"Reçete Kaydı" ekranında iken farenin sağ tuşu ile görüntülenen "Reçete İzleme" seçeneğine tıklandığında, yan ürün tipli bileşen adlarının listelenmesi sağlanmıştır.

**24- Oracle Veritabanında Muhtasar Parametrelerinde e-Beyanname Oluşturulması Sırasında Ekrana Gelen Uyarı İle İlgili Durumun Düzeltilmesi Talebi**

Oracle veritabanında muhtasar basımı XML dosyası oluşturulması sırasında ekrana gelen uyarı ile ilgili durum düzeltilmiştir.

**25- Mamul Rezervasyon Oluşturma Ekranında Depo Kodlarının Ekrana Gelmemesi İle İlgili Durumun Düzeltilmesi Talebi**

"Fabrika Uygulaması" kullanıldığında "Mamul Rezervasyon Oluşturma" ekranında depo kodlarının ekrana gelmemesi ile ilgili durum düzeltilmiştir.

**26- "Satıştan Üretim Sonu Kaydı" İşlemi İle Aynı Tarihli Faturaların Tek Fişte Oluşturulmasının Sağlanması**

"Satıştan Üretim Sonu Kaydı" ekranında "Farklı Tarihli Hareketler İçin Farklı Fişler Oluşturulsun" seçeneği işaretlendiğinde, aynı tarihteki farklı faturalar için tek bir üretim sonu kaydı oluşturulmuyordu. Düzeltilerek, aynı tarihli faturalar için tek bir "Üretim Sonu Kaydı" oluşturulması sağlanmıştır.

**27- Form Bazının Tanımlı Olduğu Durumlarda Farenin Sağ Tuşu İle Ekrana Gelen Seçeneklerin Pasif Olması İle İlgili Durumun Düzeltilmesi Talebi**

Admin olmayan kullanıcı için fatura ekranlarında form bazı güvenlik ile numara alanları "Görülebilir" ve "Değiştirilemez" olarak tanımlandığında, rehberden herhangi bir fatura seçilmesi durumunda farenin sağ tuşu ile ekrana gelen seçenekler pasif şekilde görünüyordu. Düzeltilerek, sağ tuş seçeneklerinin aktif ve çalışır durumda olması sağlanmıştır.

**28- Kurulum Yapılırken Ekrana Gelen "Lisans/Güvenlik Bilgileri Oluşturluyor" Cümlesindeki "Oluşturluyor" Kelimesinin Doğru Yazılmasının Sağlanması**

Kurulum dosyasında yer alan "Lisans/güvenlik bilgileri oluşturuluyor" cümlesi "Lisans/güvenlik bilgileri oluşturuluyor" olarak düzeltilmiştir.

**29- Sigara Faturası Kesildikten Sonra Muhasebe Tarafında Oluşan Kayıtlarda Fazladan KDV Satırının Oluşması İle İlgili Durumun Düzeltilmesi Talebi**

'EFATURA','SIGARAKDV' özel parametresi eklenmiştir. İlgili özel parametre tanımlandığında Toplu e-Fatura Oluşturma ekranına "Sigara Faturası Oluşturulsun" seçeneği eklenir. Seçenek işaretlendiğinde, "Sigara Uygulaması" kullanılmayan durumlarda da e-Fatura oluştururken, sigara faturası gibi oluşturulması sağlanmıştır.

**30- MT940 Aktarımı Yapılırken Ekrana Gelen "Kayıt Yapma Hakkınız Yok" Uyarısı İle İlgili Durumun Düzeltilmesi Talebi**

MT940 entegrasyonu ile çek tahsil işlemi yapılması istendiğinde, yetki olduğu halde yetki olmadığına dair ekrana uyarı gelmesi ile ilgili durum düzeltilmiştir.

**31- Dövizli Çeklerin Ondalık Bölümlerinin Raporda Görünmemesi İle İlgili Durumun Düzeltilmesi Talebi**

"Geçmiş Portföy Çek Listesi" ve "Geçmiş Portföy Senet Listesi" raporlarının "Döviz Tutarı" sütununda rakamların ondalık değerlerinin görünmemesi ile ilgili durum düzeltilmiştir.

**32- Netsis Wings Programında Türkçe Karakter İçeren Açıklamalar Başka Bir Alana Kopyalandığında Harflerin Bozuk Gözükmesi İle İlgili Durumun Düzeltilmesi Talebi**

Netsis Wings Programında, Türkçe karakter içeren metin kopyalama işleminde harflerin düzgün görünmesi sağlanmıştır.

**33- Müşteri Siparişlerinde Yurtiçi Olarak Açılan Belgeyi Yurtdışı Tipine Çevirdikten Sonra Log Kayıtlarına Kayıt Atmaması İle İlgili Durumun Düzeltilmesi Talebi**

Müşteri siparişlerinde sağ tuş fonksiyonu ile yurtiçi/yurtdışı yapıldığında log kayıtlarına kayıt atmaması ile ilgili durum düzeltilmiştir.

**34- Depolar Arası Transfer Fişinin İçinde İken Kalem Seçilip Hücre Yerleştirme İptali Yapılması İstendiğinde "Belge No" Alanının Dolu Olarak Gelmesi Fakat Fiş İçinde Yapılan Hücre Yerleştirmelerinin Grid Ekrana Getirilmemesi İle İlgili Durumun Düzeltilmesi**

"Hücre Yerleştirme/Toplama İptali" işlemlerinde, ekrana getirilen cari kod bilgisi ile ilgili düzeltme sağlanmıştır.

**35- Stok Karlılık Raporu Alırken Maliyet Hesaplamalarına Ambar Çıkış Fişlerinin Dahil Edilmemesi Talebi**

Stok Karlılık Raporu ekranına "Ambar Çıkış Fişi Hareketleri Dahil Edilmesin" seçeneği eklenmiştir. Seçenek işaretlendiğinde, maliyet hesaplamalarına ambar çıkış fişlerinin dahil edilmemesi sağlanmıştır.

**36- Kur Farkı Kapatma İşleminde Farklı Şubeden Girilen Hareketin Rapora Gelmesi Fakat Cari Hareket Kayıtlarına Yansımaması İle İlgili Durumun Düzeltilmesi Talebi**

"Cari Kur Farkı Çalıştırma" ekranında döviz tipi olan fakat döviz tutarı olmayan kayıtların rapora gelmemesi sağlanmıştır.

**37- Demirbaştan Dekont Oluşturma İşlemi Yapıldığında Tarih Kilidi Dikkate Alınmadan Dekont Oluşturulması İle İlgili Durumun Düzeltilmesi Talebi**

Demirbaş - "Toplu Dekont Oluşturma Kaydı" ekranının, demirbaşın tarih kilit aralığına ve ekranda girilen dekont tarihine göre çalışması sağlanmıştır. "Her Demirbaş İçin Ayrı Oluşsun" seçeneği işaretlendiğinde, demirbaşın alış tarihine göre kontrol yapılması sağlanmıştır. Ayrıca, "Toplu Dekont Oluşturma Kaydı" ekranında hak kontrolü yapılması ile ilgili durum da düzeltilmiştir.

**38- MT940 Kural Bilgileri Ekranında Rehberden Banka Seçiminin Yapılamaması İle İlgili Durumun Düzeltilmesi Talebi**

Banka - Kayıt - MT940 - "Kural Bilgileri" ekranında, "İşlem Tipi" alanında "Banka" seçildikten sonra rehberden banka seçiminin yapılamaması ile ilgili durum düzeltilmiştir.

**39- İşlem Yapılırken Sistemin Seçilen Dizaynı Görmemesi ve Varsayılan e-Posta Biçiminde Mail Gönderimi Yapması İle İlgili Durumun Düzeltilmesi Talebi**

"Havale-EFT Kayıtları" için dizayn ile e-Posta gönderiminin çalışması sağlanmıştır.

**40- Fiş Değişiminde Her Fiş İçin Ayrı Sayfa Oluşturulması Fakat Excel'e Aktarıldığında Her Fişi Sayfa Başı Yapmaması İle İlgili Durumun Düzeltilmesi Talebi**

Muhasebe - Raporlar - Fiş Listeleri - Yevmiye Fişi - "Değişen Fiş Numarasında Sayfa Atlansın" seçeneği işaretlendiğinde, Excel aktarımında sayfa atlanmaması ile ilgili durum düzeltilmiştir.

**41- Bilgisayar-Sayım Fark Raporu Ekranında Gelen Uyarılar İle İlgili Durumun Düzeltilmesi Talebi**

Sayım/Bilgisayar Fark Raporu - Esnek Yapılandırma Kullanılıyorsa - "Sıralama" sekmesinde uyarı gelen alanlar kaldırılmıştır ve maliyet tipi değiştirildiğinde ekrana gelen uyarı ile ilgili durum düzeltilmiştir.

**42- Borç-Alacak Yaşlandırma Listesi Tutar Alanında Kuruş Farkı Oluşması İle İlgili Durumun Düzeltilmesi Talebi**

"Borç-Alacak Yaşlandırma Listesi" raporunda döviz tipli tutarın ondalık değeri, cari hareketler döviz tutarı ile kıyaslandığında oluşan küsurat farkı ile ilgili durum düzeltilmiştir.

**43- Dövizli Çek Tahsilinde Döviz Tutarının Doğru Hesaplanmasının Sağlanması**

"Dekont/Senet/Çek modüllerinde Kur Farkı Kaydı Yapılsın mı?" parametresi işaretlenmediği zaman, döviz tutarının doğru hesaplanması sağlanmıştır. Oluşması gereken kur farkının, daha sonra "Banka" modülündeki "Döviz Farklarını Kapatma" ile oluşturulması gerekiyor.

**44- Stok Hareket Kayıtlarında Filtre Verildikten Sonra Bir Sonraki Stoka Geçildiğinde Filtrenin Kalkması İle İlgili Durumun Düzeltilmesi Talebi**

Stok ve Cari Hareket Kayıtları ekranında gride filtre verildiğinde ve sonraki kayda geçildiğinde filtrelerin bazen temizlenmemesi ile ilgili durum düzeltilmiştir.

**45- Bilanço Esasına Göre Defter Veren Bir Şahıs Şirketi İçin B Formu Parametrelerinde T.C. Kimlik Bilgisi Doldurulup B Formu Alınması İstendiğinde Ekrana Gelen Uyarı ile İlgili Durumun Düzeltilmesi Talebi**

Şahıs şirketleri için B Formu tanımlamalarında T.C. kimlik bilgisi doldurulup, XML olarak B Formu raporu oluşturulması sağlanmıştır.

**46- Merkezi Kimlik Denetimi (SSO) NDI'da Açık Olan Kullanıcının Askıda Kalma Durumu İle İlgili Durumun Düzeltilmesi Talebi**

"NDI Uygulaması" kullanıldıktan sonra Temelset kapatıldığında, kullanıcının askıda kalma durumu ile ilgili düzeltme yapılmıştır.

**47- "e-Faturadan Alış Faturası Oluşturma" İşleminde, Döviz Tipi ve Döviz Fiyatının Ekrana Gelmesinin Sağlanması**

"e-Faturadan Alış Faturası Oluşturma" işleminde, alış faturasına "Döviz Tipi" bilgisinin gelmesi sağlanmıştır.
