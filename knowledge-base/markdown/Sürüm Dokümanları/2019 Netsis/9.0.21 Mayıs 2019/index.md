---
title: "9.0.21 Mayıs 2019"
page_id: "34226609"
product: "netsis-3-enterprise"
depth: 3
is_section: true
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Sürüm Dokümanları"
  - "2019 Netsis"
  - "9.0.21 Mayıs 2019"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Sürüm Dokümanları / 2019 Netsis / 9.0.21 Mayıs 2019"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWRmNTdlNDUwLWUzZjItNDJkNi1hOTEyLTNkNjcxMTFkMjYzMCZsaW5rPWUxMjg3MmFlLTMxYWMtNGUyNy1hN2FjLWFmZGRjOGJkMGUxNSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=df57e450-e3f2-42d6-a912-3d67111d2630&link=e12872ae-31ac-4e27-a7ac-afddc8bd0e15&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "9-0-21-mayis-2019_34226611_34226609.html"
source_version: "2019-05-14T15:59:13.277+03:00"
source_bytes: 18328
fetched_at: "2026-09-13T04:28:32+00:00"
generator: "netsis-scraper 1.0.0"
---
# 9.0.21 Mayıs 2019

- Merkezi Netsis sunucusundaki web servisinden yapılan yayını alacak ve clientlarda gösterecek bir eklenti tasarlandı.

- "Banka Hesap Hareketleri Dökümü" raporunda performans iyileştirmesi yapıldı.

- Modül ekran açılışı performans değerlerinin sorgulanmasını sağlamak için geliştirme yapıldı.

- İş emirlerinde kullanılan hammadde ve/veya yarımamulleri stoktan, satıcı siparişinden ve satıcı talebinden karşılanıyorsa, bu bilgilerin "Çizelgeleme Gantt Gösterimi" ekranında "İş Emri Kullanım Raporu" ile gösterilmesi sağlandı. Böylece; çizelgelenen işler raporuna, iş emrine başlamak için gerekli olan hammadde ve/veya yarımamulün stoktan hazır mı karşılandığı, yoksa satıcı siparişi, talebi ve/veya yarımamul iş emrinin üretimi ile mi karşılanacağı ile ilgili bilginin alınması sağlandı.

- "Fabrika Son Durum" ekranına "Bitiş Tarihi" alanı eklendi. Eklenen alan sayesinde, fabrikanın makine istasyon ve kaynak kullanımı ile ilgili rapor alırken bitiş tarihi kısıdı verilmesi sağlanır.

- Tepe mamul için hesaplamaya giren ara bileşen maliyetlerinin de aynı anda hesaplanması ve kaydedilmesi için, "Reçete Listesi" ekranında, mamul hesabının ara bileşenler için de hesaplanması sağlandı. Hesaplanan bu maliyetlerin TBLRECMALIYET tablosuna kaydedilmesi sağlandı.

- "Bakım Talep Kayıtları" ekranında en son açılan (yeni) talebin grid alanda en üstte olması sağlandı. Açılan son kaydın sürekli üstte olması, gereksiz tekrar kayıt açılması ile ilgili tedbir oluşturdu.

- "Log Raporu" ekranındaki "Ön Sorgulama" sekmesinde yer alan "Rapor Gösterim Tipi" alanına "Grid (Tarihler Sütunda)" seçeneği eklendi. Bu seçeneğin aktif hale gelmesi için, "Anahtar Saha 1" alanının boş bırakılmaması ve "Detay Bilgi Basılsın" seçeneğinin işaretlenmesi gerekir. Rapor gösterim tipi olarak "Grid (Tarihler Sütunda)" seçeneğinin seçilmesi, değişim olan her tablo için değişiklik tarihinin sütunda gösterilmesini sağlar. Hangi tarihte ne değişiklik yapıldığı, kırmızı ile işaretlenerek kullanıcıya gösterilir.

- Makine Bakım - Kayıt - "Talimat Şablonları" ekranına "Açıklama" alanı eklendi. Eklenen açıklama alanı ile, "Bakım Planlama" ekranından toplu bakım ile oluşturulan bakım emirlerinin "Açıklama" alanına aktarılması sağlandı. "Bakım Talep Kayıtları" ekranındaki "Talep Açıklaması" alanının, talep onaylandıktan sonra "Bakım Emirleri" ekranındaki "Emir Açıklama" alanına aktarılması sağlandı.

- "E-İrsaliye işlemleri" menüsünün altına "E-İrsaliye Ek Bilgiler Şablon Oluşturma" bölümü eklendi. Bu ekranda ön tanımlama olarak e-irsaliye ek bilgi girişi tanımlanır. Tanımlanan bilgiler, e-irsaliye oluşturulurken "Toplamlar" sekmesinde yer alan "Ek Bilgi Girişi" yardımı ile ilgili şablon seçildikten sonra "Bilgileri Şablondan Getir" tuşuna tıklandığında ekrana gelir.

- "Üretim Sonu Kaydı" oluştururken, ilk ve son operasyon şeklinde birden fazla operasyon varsa, öncelikle bu operasyonlara üretim akış kaydı girilir ve ardından üretim sonu kaydı yapılır. İlk operasyonda daha fazla ürün üretildiği varsayılarak, bu miktarı kapatacak maksimum bir "Üretim Akış Kaydı" girildiğinde, "Üretim Sonu Kaydı" oluştururken ortaya çıkan hata ile ilgili düzeltme yapıldı.

- Cari - Raporlar bölümündeki tüm raporlar için performans iyileştirmesi yapıldı.

- Tarih Aralıklı Mizan raporu ile ilgili performans iyileştirmesi yapıldı.

- Netsis HR entegresiz kullanım için, merkezi kimlik yönetiminde kullanıcı hakları ile ilgili tanımlamalar desteklendi.

- "Üretim Akış Kaydı" için belge bazında log desteği sağlandı.

- "İthalat Masraf Dekont Kayıtları" ekranına belge bazında "Log Raporu" desteği getirildi.

- "Muhasebe Detay Kod Girişi" ekranına belge bazında log desteği getirildi.

- "Stok Kartı Kayıtları" ekranına, belge bazında log desteği getirildi.

- "İhracat Masraf Dekont Kayıtları" ekranına, belge bazında "Log Raporu" desteği getirildi.

- "Satın Alma Talep" ekranına, belge bazında log desteği getirildi.

- "Yükleme Emri" ekranında, belge bazında "Log Raporu" desteklendi.

- "Satın Alma Teklif" ekranına, belge bazında log desteği getirildi.

- "Satış Talep" ekranına, belge bazında log desteği getirildi.

- "Müstahsil Faturası" ekranına belge bazında log desteği getirildi.

- "Serbest Üretim Sonu Kaydı" ekranına, belge bazında log desteği getirildi.

- Çizelgeleme için "MRP Sonuçlarından Getir" seçeneği ile yeni açılacak iş emirleri için sıradan iş emri numaraları türetildikten sonra MRP'den iş emirleri açıldığında, ilgili çizelgeleme raporlarındaki bilgilerin kaybolması ile ilgili durum düzeltildi.

- "Reçete Sıra No Düzenleme" ekranına "Tüm Mamuller İçin Çalıştırılsın" parametresi eklendi. Parametrenin seçilmesi ile, reçetesi olan tüm stok kodları için toplu şekilde işlem yapılması sağlanır.

- KDV-1 beyannamesinde, "KDV Kanununun 13/f Maddesi Kapsamında Yüklenici Firmalara Yapılan Teslim ve Hizmetlere Ait Liste" eki desteklendi.

- "Kalite Kontrol Kaydı" ekranına belge bazında log desteği getirildi.

- "Mamul Ana Grup Kayıtları" ekranına belge bazında log desteği eklendi.

- "Mamul Grup Kodu Kayıtları" ekranına belge bazında log desteği eklendi.

- "Üretim Akış Kaydı" ekranına belge bazında log desteği eklendi.

- "Bakım Talep Kayıtları" ekranına belge bazında log desteği eklendi.

- "Bakım Emirleri" ekranına belge bazında log desteği getirildi.

- "Reçete Kaydı" ekranına belge bazında log desteği getirildi.

- "İş Emri Girişi" ekranına belge bazında log desteği getirildi.

- "Satış Teklif" ekranına belge bazında log desteği getirildi.

- Esnek yapılandırma sihirbaz ekranı yenilendi. Esnek yapılandırmalı stokun özellik ve değer kodlarına göre yapılandırma kodu arama ve tanımlama işlemlerinde kullanım kolaylığı sağlandı.

- NetOpenX ile, "Fatura Modülü" üzerinden yürütülen e-ihracat aşamasında, sağ klik tuşu ile ekrana gelen özel tuşlar sayesinde ek alanlar desteklendi.

- "Stok Kartı Kayıtları" ekranından herhangi bir stok ile ilgili işlem yapılması istendiğinde; işlemin yapılacağı günün tarihi, "Tarih Kilitleme" ekranında belirlenen tarih kilidi aralığının içinde ise, programın stok ile ilgili işlem yapılmasına izin vermemesi durumu düzeltildi.

- "Dövizli Borç-Alacak Dökümü" ekranına "Döviz Bakiyesi Sıfır Olanlar Dahil Edilsin" seçeneği eklendi. Bu seçenek işaretlenmediğinde, döviz borç veya alacak bakiyesi sıfır olan kayıtlar raporda yer almaz.

- 'EFATURA','KALEMOTVBAS' özel parametresi tanımlanarak oluşturulan e-faturada; ÖTV'li stok varsa, e-faturanın XML ve kalem bilgilerinde ÖTV bilgisinin yazması sağlandı. Bu özel parametrenin 'EFATURA','NET_FIYAT' ile birlikte kullanılmaması gerekiyor.

- "Satış İrsaliyelerini Toplu Faturalama" ekranından oluşacak KDV'siz e-faturalar için, "KDV'siz Belge İstisna Kodu" alanı eklendi. Bu seçenek, "E-Fatura Cari Getirilsin" seçeneği işaretlendiğinde aktif hale gelerek e-fatura oluşturulurken belirtilen istisna kodu ile e-fatura oluşturulmasını sağlar. Fatura oluşturma adımında kullanıcıya sorulmaz.

- "Yevmiye Fiş Girişi" ekranında belge bazında log desteği sağlandı.

- "Dekont Modülü" menüsünde yer alan "Genel Dekont Kaydı", "Genel Gider Cari Hesap Fatura Kaydı" ve "Serbest Meslek Makbuzu Kaydı" ekranlarına, belge bazında log raporu desteği getirildi.

- "Mamul Parçalama" ekranına belge bazında log desteği getirildi.

- "Ters Üretim Sonu Kaydı" ekranında belge bazında log raporu desteklendi.

- "Cari Hesap Kayıtları" ve "Cari Risk Girişi" ekranlarına belge bazında log desteği getirildi.

- "Banka Hesap Kayıtları" ekranına belge bazında log desteği getirildi. TBLBNKHESSABIT tablosu için log tutulması ile aktif hale gelir.

- "Ürün Konfigüratörü" ekranına "Ortak Özellikler Otomatik Değişsin" seçeneği eklendi.

- KDV 1 Beyannamesine "3065 Sayılı Kanunun 13/i Maddesindeki İstisna Kapsamında Yapılan Teslimlere İlişkin Bildirim" eki eklendi.

- Ürün konfigüratörünün, "Üretim Modülü" güncelleme durumunda açılması sağlandı.

- KDV-1 Beyannamesine "Teknoloji Geliştirme Bölgeleri" eki eklendi.

- KDV-1 Beyannamesine "Türk Hava Kuvvetlerinin Güçlendirilmesine Katılma Payı Bildirimi" eki eklendi.

- MRP - Kayıt - İleri Üretim Çizelgeleme - "Makine Tanımlama" sekmesinde yer alan "Makine Tipi" alanının "Fason" olarak seçilmesinden sonra açılan "Fason Lojistik Planı" sekmesinde, "Gidiş Günü" seçildikten sonra dönüş süresinin 30 güne kadar girilmesi sağlandı.

- NetOpenX ile e-irsaliye ek bilgi girişi EIrsaliyeEkYeni ve EIrsUstBilgileriOku fonksiyonları ile desteklendi.

- NetOpenX ile, taslakta bekleyen e-fatura belgelerinin gönderimi için "EBelgeGonderme" fonksiyonu eklendi.

- NetopenX ile, e-irsaliye belgeleri için sıradaki numarayı getiren fatura.YeniEIrsaliyeNumara("EIR"); fonksiyonu eklendi.

- e-arşiv belgelerinin "İmzalandı" durumundan önce basımının alınması sağlandı. İmzalanmadan önce basım alınırken, belge üzerinde "TASLAK" ibaresinin bulunması ve iptal edilen e-arşiv belgelerinin üzerinde de "IPTAL" ibaresinin olması sağlandı. Taslak oluşturma işleminden sonra, tüm e-belgelerin (e-arşiv, e-fatura, e-irsaliye, e-müstahsil) görüntüsüne "TASLAK" ibaresi eklendi. E-fatura, e-irsaliye ve e-müstahsil belgeleri için "TASLAK" ibaresinin olması istenmediğinde, EFATURA/TASLAKBASIM özel parametresinin tanımlanması gerekir.

- Fatura/İrsaliye/Sipariş ekranlarının "Kalem Bilgileri" sekmesinde iken sağ klik ile ekrana gelen özel tuşlar menüsüne "FIFO Raporu" eklendi. "Stok Kodu" seçildikten sonra menüye tıklandığında "FIFO Raporu" açılır ve seçili stok kodu, raporun "Ön Sorgulama" sekmesine kısıt olarak getirilir.

- "Alternatif Reçete Kaydı" ekranı üzerinde iken sağ klik tuşu ile ekrana gelen "Varsayılan Reçete Yap" işlemi ile, mevcut reçetenin silinmeyerek alternatif reçete olarak kaydedilmesi sağlandı.

- Carinin e-fatura mükellefi olmasından itibaren verilen 7 günlük süre dolduğunda; "Carinin e-fatura mükellefi olmasından itibaren verilen 7 günlük süre dolmuştur. Efatura mükellefiyetini pasifleştirmek istediğinize emin misiniz?" uyarısı ile kullanıcıya bilgi verilmesi sağlandı.

- İptal edilen e-arşiv belgelerinin üzerine "IPTAL" ibaresinin yazılması sağlandı.

- Rapor Modülü kullanılarak alınan raporlar için 'Gelişmiş Rapor' seçeneği desteklendi.

- Üretim - İşlemler - Toplu Rezervasyon İptali - "Rezervasyon İptal Bilgileri" sekmesine "Tüm Depolar" seçeneği eklendi. Seçenek işaretlendiğinde; tüm depolar için toplu rezervasyon iptali yapılması sağlandı. Ayrıca "Rezervasyon İptal İşlemi" sekmesine "Çıkış Depo" kolonu getirildi.

- KDV 2 beyannamesinde yer alan "TABLO-1 TAM TEVKİFAT UYGULANAN İŞLEMLERE AİT BİLDİRİM" kısmındaki satırlar çoğaltıldı.

- Teslim carisinin "TC Kimlik No" yada "Vergi No" alanları boş olduğunda, "Toplu E-Arşiv Oluşturma" ekranından taslak oluşturma sırasında uyarı verilmesi sağlandı.

- Üretim - Üretim Akış Kontrol - Üretim Akış Kaydı ekranına iş emri çağrıldığında, sağ klik tuşu ile ekrana gelen özel tuşlara "Reçete İzleme" özelliği eklendi.

- "İleri Üretim Çizelgeleme" modülünün kullanılmadığı durumda; İstasyon, Operasyon, Rota vb. kayıtların MRP modülü kayıt işlemlerinin altında tutularak istasyon ve operasyon eşleştirmelerinin "Üretim Akış Kaydı" ekranına getirilmesi sağlandı.

- Üretim - MRP - Kayıt - "Malzeme Gereksinim Planlama" ekranında yer alan "MGP Çalıştır/Rapor" butonuna basıldıktan sonra, açılan ekranda yer alan "Stok Bakiye Kontrol" seçeneği işaretlenerek alınan rapor ekranındaki tabloya "Depodan Kullanım" kolonu eklendi.

- Reçete kaydında bir operasyon bileşene çevrildiğinde "Reçete Bilgileri-2" sekmesinde son operasyon parametre alanının sıfırlanması ile ilgili durum düzeltildi.

- "Stok Planlama Kayıtları" ekranına "Üretim Transfer Süresi" alanı eklendi. Bu süre MRP modülündeki üretim süresine eklenerek MRP bildirim tarihlerinin miktardan bağımsız hesaplanması sağlandı.

- Döviz kurlarının takip edilmesini sağlamak için Döviz Kuru eklenti tasarımı yapıldı.

- Kullanıcı bazında not girişi yapılmasını sağlayacak bir eklenti tasarlandı.
