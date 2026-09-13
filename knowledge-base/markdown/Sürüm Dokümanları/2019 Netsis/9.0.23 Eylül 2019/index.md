---
title: "9.0.23 Eylül 2019"
page_id: "41161966"
product: "netsis-3-enterprise"
depth: 3
is_section: true
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Sürüm Dokümanları"
  - "2019 Netsis"
  - "9.0.23 Eylül 2019"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Sürüm Dokümanları / 2019 Netsis / 9.0.23 Eylül 2019"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTVmOTNlNDFjLTJlYjgtNDU0MS05YjNhLTFkODQ0OTYwNDYzMCZsaW5rPTQxZDgzN2ZkLTZiMzktNDI4Ni05MDA5LTNmZDI3NmU0Nzc2YSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=5f93e41c-2eb8-4541-9b3a-1d8449604630&link=41d837fd-6b39-4286-9009-3fd276e4776a&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "9-0-23-eylul-2019_41161968_41161966.html"
source_version: "2022-07-05T13:26:26.173+03:00"
source_bytes: 17099
fetched_at: "2026-09-13T04:28:29+00:00"
generator: "netsis-scraper 1.0.0"
---
# 9.0.23 Eylül 2019

- Merkezi Kimlik Yönetimi (SSO) üzerinden, kullanıcının Temelset oturum bilgisi silindiğinde, kullanıcıya "Sistem yöneticisi tarafından oturumunuz kapatılmıştır. Uygulamanız 30 sn içerisinde kapanacaktır." bildiriminin gönderilmesi ve 30 sn sonunda Temelset uygulamasının otomatik olarak kapatılması desteklendi.

- Cari - İşlemler - "Cari Kodu Değişikliği" ekranındaki alanların hizaları düzeltildi.

- Modüller üzerinden ilgili kayıt için "Bağlantı Kopyala" butonu eklendi. Bu butona tıklandığında seçili kayıt için bağlantı adresi oluşturulur. Oluşturulan adres, anlık mesajlaşma eklentisine veya Netsis dışından Outlook, Word, Excel gibi uygulamalara yapıştırılarak adresteki kaydın açılması sağlanır.

- - Ülke kod tanımlarına, ''ZZ" kodlu "Bilinmeyen Ülke ve Topraklar" ve ''XZ" kodlu "Uluslararası Sular" tanımlamaları eklendi.

```text
          - Uluslararası ölçü birim tablosuna, "PTN" kodu ile "Parça, Kısım" ölçü kodu eklendi.
```

```text
          - Döviz tipi ve döviz birim eşleştirmeleri alanlarına “BYN” kodlu "Beyaz Rusya Rublesi" para birimi eklendi.
```

```text
          - Tam istisna muafiyet kodlarına, "336" kodu ile "Geçici 40 UEFA Müsabakaları Kapsamında Yapılacak Teslim ve Hizmetler" eklendi.
```

```text
          İlgili geliştirmeler e-arşiv ve e-fatura tarafında desteklendi.
```

- Netsis güncelleme aracı çalışırken ..\\Servis\\Log klasörü altına yapılan işlemlerin log atılması sağlandı. Programda hata meydana gelirse, ilgili log dosyası ile detayı incelenebilir.

- "Çek Alındı Kaydı" ekranının dinamik kodlama ile açılması desteklendi.

- KDV İstisna Kanunu ile ilgili tebliğe göre 335 nolu "KDV 13/n Basılı Kitap ve Süreli Yayınların Teslimleri" istisna kodu tanımlamaları earşiv tarafında desteklendi.

- Aktivasyon süresi yaklaştığında veya dolduğunda gelen uyarı mesajında, onaylı sürüm güncelleme çalıştırılmasının yapılması gerektiği belirtildi.

- "Noterler Birliği Servisinin" E-Fatura lisansından bağımsız olarak kullanılması sağlandı.

- EARSIV/TASLAKBASIM özel parametresi ile e-arşiv belgelerinde 'TASLAK' ibaresinin gösterilmemesi sağlandı.

- Güncelleme işlemi başlarken daha güncel bir NetUpdate.exe varsa tespit edilmesi ve daha sonra güncellenerek programın yeniden çalıştırılması sağlandı.

- Kullanıcıların program içerisinde mesajlaşması için "Anlık Mesajlaşma" eklentisi eklendi. Bu eklenti sayesinde, kullanıcıların birbirine dosya (Örneğin; Excel dosyası) göndermesi, programda olan bir kaydın gönderilmesi ve bağlantı göndermesi sağlandı.

- Kullanıcı bazında hatırlatmaların girilmesini sağlayan 'Hatırlatıcı' eklentisi eklendi. Bu eklenti ile kullanıcılar hatırlatma ekleyebilir. Ayrıca, "Enterprise" paketi ile hatırlatmalar, belge bağlantısı ile desteklenebilir.

- Üretim - Kayıt - "Saha-Tablo Eşleştirmesi" ve Muhasebe - Kayıt - Proje Kodu Girişi - "Kullanıcı Tanımlı Sahalar" sekmesinde yer alan "Saha Tanımlama", "Saha Tablo Eşleştirme" ekranları, Yardımcı Programlar - Kayıt menüsünün altına "Saha-Tablo Eşleştirmesi" olarak eklendi.

- Cari - Kayıt - "Cari Hesap Kayıtları" ekranına "Ek Saha" özelliği eklendi.

- Stok - Kayıt - "Stok Kartı Kayıtları" ekranına "Saha-Tablo Eşleştirmeleri" özelliği eklendi.

- Seri girişi sırasında, klavyede yer alan \<tab\> tuşu ile alanlar arasında geçiş yapılması sağlandı.

- Stok - Kayıt - "Seri Takibi" menüsünün altına "Seri Numarası Değişikliği" ekranı eklendi. Bu ekran sayesinde, "Eski Seri No" ve "Yeni Seri No" alanları kullanılarak seri numaralarında değişiklik yapılması sağlandı.

- Stok - Kayıt - Seri Takibi - "Seri Parametreleri" ekranına "Seri Rehberinden Miktar Bilgisi 1 Olarak Alınsın" parametresi eklendi. Bu parametre işaretli olduğunda, seri rehberinden seçilen serili stokların miktarı seri ekranına 1 olarak aktarılır. Böylece, seri miktarının birden fazla ayrı seriden kullanılması durumunda, seri miktarlarını "0" olarak düzeltip miktar girilmesi sürecinde kolaylık sağlandı.

- Stok - Kayıt - Seri Takibi - "Seri Takibi Kayıtları" ekranına "Açıklama-1" ve "Açıklama-2" alanları eklendi.

- "Seri Giriş" ekranı ve "Seri Takibi Kayıtları" ekranında Excel'den aktarım desteklendi. "Seri Giriş" ekranında yer alan "Excel'den Aktar" butonu ile gride Excel'den aktarım yapılması sağlandı. "Seri Takibi Kayıtları" ekranında iken farenin sağ tuşuile ekrana gelen "Excel'den Aktar" seçeneğine tıklanarak da Excel'den aktarım yapılabilir.

- Stok - Kayıt - Seri Takibi - "Seri Parametreleri" ekranına "Seri Girişinde Kullanılacak Opsiyonel Sahalar" eklendi. Burada seçilen sahaların "Seri Girişi" ekranında kullanılması sağlandı.

- "Seri Uygulaması" ile ilgili özel parametreler, "Seri Parametreleri" ekranına alındı. İlgili parametreler;\- "Seri Takibi" ekranında Seri Girişi Zorunlu Olsun (STOK/SERISIZKAYITYAPMA): "Seri Takibi" ekranında, girilen seri miktarı "0" olduğunda ekranın kapanmasını engelleyerek, seri girişini zorunlu tutar.\- Miktarsız Kalem İçin Seri Girişi Yapılsın (FATURA/MIKTARSIZSERI): Fatura belgelerinde miktar "0" girildiğinde de "Seri Takibi" ekranının açılmasını sağlar.\- FIFO Seri İçin Sıralama Kriteri (FATURA/SERISIRALA): "Seri Takibi" ekranındaki FIFO çıkış seri işleminde seriler, bu parametrede seçili değere göre sıralanarak ekrana getirilir.\- Miktar Girişinden Sonra Seri Ekranı Otomatik Kapanmasın (FATURA/SERIOTOKAPATMA): Seri miktarı ile hareket miktarı eşit olduğunda, "Seri Girişi" ekranının otomatik olarak kapanmasını engeller.\- FIFO Seri İçin Proje Kodu Kontrol Edilsin (GENEL/FIFOSERIPROJE): FIFO çıkış seri işleminde, hareketteki proje kodu kontrol edilerek ekrana ilgili proje koduna ait seriler sıralanarak getirilir.\- İade Tipli Girişlerde Seri Girişi Yapılsın (FATURA/IADESERI): "Girişlerde Seri Takibi" parametresi işaretli değilken iade tipli alış faturasında seri ekranının açılmasını sağlar.\- İş Emri Reçetesinde Seri Girişi Yapılsın (URETIM/ISEMRIRECSERISORULSUNMU): İş emri reçetesinde sarf edilecek bileşenler için seri girişinin yapılmasını sağlar.

- "Toplu Fatura Basımı" ekranında, fatura basımı yapılırken birden fazla faturanın tek bir PDF olarak raporlanması sağlandı.

- NetOpenx tarafına eklenen e-irsaliye oluşturma ve e-irsaliye ek bilgi girişi ile birlikte; e-fatura, e-arşiv, e-irsaliye taslak oluşturma, e-fatura, e-arşiv, e-irsaliye görüntüleme, e-fatura, e-arşiv, e-irsaliye gönderme işlemleri Rest tarafında da desteklendi.

- Varsayılan "Wings Timeout" süresi 1800 saniye olarak değiştirildi.

- Şirket değişikliği ya da şirkete ilk girişte, app ve eklentilerin programı kapatmadan önceki hali ile kalması sağlandı.

- "Cari Risk Girişi" ekranında yer alan "Toplam Risk" alanının yazı rengi turuncu ve mavi olarak değiştirildi.

- E-Faturadan "Alış Faturası Oluşturma" ya da "Dekont E-Fatura Eşleştirme" işlemlerinde; gelen e-faturanın vergi numarasına ait birden fazla cari kart varsa, açılan "E-Fatura Cari Eşleştirme" ekranında cari kodun yanında cari isim bilgisinin de gösterilmesi sağlandı.

- "Otomatik Seri Kodu Üretme Tanımları - "Geçerli Stoklar" sekmesinde "Çoklu Stok Seçimi" yöntemi desteklendi. Giriş yöntemi olarak "Kısıt Girişi" kullanıldığında, önceden olduğu gibi kısıt verilen stoklarda ilgili otomatik üretim kodu çalışır. Giriş yöntemi olarak "Çoklu Stok Seçimi" seçildiğinde ekrana grid gelir ve "Kayıtları Getir" butonuna tıklandığında serili stoklar aktarılır. Otomatik seri kodu üretilmesi için, istenen stoklar seçildikten sonra "Kaydet" butonuna tıklanır. Diğer modüllerde "Seri Girişi" ekranı açıldığında, burada girilen kayıtlara göre seri kodları getirilir. "Çoklu Stok Seçimi" yöntemi ekranında, "İleri Kısıt" ve "Kayıt Getir" ile gride getirilecek stoklar filtrelenebilir.

- "Dosya Sürümleri" ekranının sol üst kısmında bulunan "Netsis Yazılım" logosu kaldırıldı.

- Muhasebe - Kayıt - KDV Beyannamesi Parametreleri - Tablo-3 Diğer İşlemler bölümüne "VUK 322 Kapsamına Giren Borçlara Ait KDV" alanı eklendi.

- KDV1 Beyannamesinin versiyonu 31 olarak güncellendi. Muhasebe - Kayıt - KDV Parametreleri - "Beyanname" sekmesine "107 ve 111 Kodlu İndirim Türleri İçin Bildirimler" eki eklendi.

- "Seri Parametreleri" ekranına "Tarihsel Seri Bakiye Kontrolü Yapılsın" seçeneği eklendi. İşaretlendiğinde, "Seri Takibi" ekranındaki seri rehberinde, seri bakiye bilgilerinin belge tarihine göre hesaplanması ve "FIFO Çıkış Seri" butonunun girilen belge tarihine göre tarihsel bakiye kontrolü yaparak çalışması sağlandı.

- "Muhtasar Beyanname" ekranına "Serbest Bölgelerde Gelir Vergisi İstisnasına İlişkin Bildirim" eki eklendi.

- 'FATURA', 'EPOSTA_KONU_DETAYLANDIRILSIN' özel parametresi tanımlandığında; fatura, irsaliye, sipariş, DAT ve ambar fiş girişlerinde gönderilen e-postanın "Yeni Kayıt" veya "Düzeltme Kaydı" başlığı ile gönderilmesi sağlandı.

- Ödeme Emri Online Banka Transferi - "Ödeme Emri Sorgulama" sekmesinde yer alan "Entegre Edilmiş Ödemeleri Sil", "Onaylanmamış Ödemeleri Sil" butonlarının çalışmaması ile ilgili durum düzeltildi.

- "Aktivasyon Tarihi" ile ilgili uyarı mesajı için SSO'ya yetki eklendi. Modül olarak "Bildirim Servisi" altından yetki verilebilir.

- "Online e-irsaliye Carilerini Güncelle" butonu kullanılarak, e-irsaliye mükellef listesi indirilir. "Cari Hesap Kayıtları" ekranına "e-irsaliye Mükellefi Bilgisi" eklendi. "Satış İrsaliyesi" ekranının girişinde bulunan "e-irsaliye" seçeneğinin işaretlenmesi, carinin e-irsaliye mükellefi olması şartına bağlandı. "Satış İrsaliyesi" ekranındaki "Cari Kodu" alanının yanında yer alan rehber butonunun sağ tık ile açılan menüsüne, "e-irsaliye Cari Seçimi' rehberi eklenerek e-irsaliye carilerinin rehberde görüntülenmesi sağlandı.

- Fatura ekranındaki çoklu kalem girişinde; Miktar, Fiyat, Depo Kodu ve Proje Kodu alanlarının kullanıcı tarafından girilmesi sağlandı.

- "Farklı Şube" seçeneği ile girilen siparişlerin, "İş Emri Girişi" ekranından kaydının yapılması sağlandı.

- "Sipariş Açma-Kapama" ekranına, gridde sağ tuşa filtre görünümünün saklanmasını sağlayan "Görünüm Ayarları" seçeneği eklendi.

- Dış ticaret - İşlemler - İthalat İşlemleri - Dosya İşlemleri - "Gümrük Beyanname Bilgileri" sekmesinde "Geldiği Ülke" kısmının ilk girişte ekrana dolu gelmesi ile ilgili sorun düzeltildi.

- Detaylı Sipariş Raporu - "Genel Kısıtlar" sekmesine "D.A.T-Ambar Fişi Kayıtları Teslimat Kabul Edilsin" seçeneği eklendi. Seçenek işaretlendiğinde; siparişe bağlı olarak girilen DAT veya Ambar Çıkış Fişleri teslimat olarak kabul edilerek, siparişin teslim edilen miktarına dahil edilir. Parametrenin işaretli olup olmamasına bağlı olarak raporda gösterilen "Teslim Miktarı" ve "Kalan Miktar" kolonlarındaki değerler farklılık gösterir.

- "e-defter Onaylama" ekranına "E-Logo Yedekleme Listesi" sekmesi eklendi. İşlemler menüsü altından "Defter Dosyalarını Yedekle" seçeneği ile, ilgili defterlerin e-Logo e-defter saklama hizmetine yedeklenmesi sağlandı. Yedeklemenin yapılacağı eLogo kullanıcı bilgilerinin "EFaturaAyarlar.exe" uygulamasında, var olan ayarların altındaki "Entegratör Kullanıcı Bilgileri" sekmesine girilmesi gerekir.
