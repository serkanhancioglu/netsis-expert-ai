---
title: "9.0.19 Ocak 2019"
page_id: "34213102"
product: "netsis-3-enterprise"
depth: 3
is_section: true
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Sürüm Dokümanları"
  - "2019 Netsis"
  - "9.0.19 Ocak 2019"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Sürüm Dokümanları / 2019 Netsis / 9.0.19 Ocak 2019"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTAwMWNmZmM5LWQ1MTUtNDhhOC1hMDU5LTFjYTY5MWZjNTM2NiZsaW5rPWZiZDBhOGNkLTEzMGEtNDUxMS04MTQzLTg3YjIyNTAzNzlmZiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=001cffc9-d515-48a8-a059-1ca691fc5366&link=fbd0a8cd-130a-4511-8143-87b2250379ff&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "9-0-19-ocak-2019_34213102_34213102.html"
source_version: "2019-02-13T15:33:16.617+03:00"
source_bytes: 15618
fetched_at: "2026-09-13T04:28:35+00:00"
generator: "netsis-scraper 1.0.0"
---
# 9.0.19 Ocak 2019

**Genel**

- Netsis Ana Menü / Ekstra sekmesine "Açık Pencereleri Yerleştir" menüsü eklendi. Yatay Döşe ya da Dikey Döşe seçenekleri ile açık pencerelerin Netsis Masaüstü boyutuna göre yatay ya da dikey olarak yerleştirilmesi sağlandı. Pencere yerleşimi en fazla üç ekran ile yapılmakta olup, üçten fazla açık ekran olması durumunda ilk açılmış üç ekran yerleştirilip diğer ekranlar simge durumuna küçültülmektedir.
- Modül ve modül gruplarının da masaüstüne kısa yol olarak eklenebilmesi sağlandı.
- Akıllı kod üretimi yapılırken ilgili alan için 1'den fazla eşleşme varsa "Akıllı Kod Listesi" penceresi açılması sağlandı. Bu pencerede kullanıcı istediği tasarıma çift tıklayarak bu akıllı kod tasarımını çalıştırabilir.
- Netsis Ana Menü / Diğer sekmesine "Logo Fırsatlar Dünyası" menüsü eklendi. Bu menüye tıklantığında <u>[https://www.logofirsatlardunyasi.com.tr](https://www.logofirsatlardunyasi.com.tr/)</u>adresinin açılması sağlandı.
- Resim eklenen ekranlarda PNG, GIF, TIFF dosya türlerinin de eklenmesi ve önizleme yapılabilmesi desteklendi.

**Fatura Modülü**

- Toplu E-Arşiv Oluşturma ekranının Ön Sorgulama sekmesine "Satırda İskonto Dikkate Alınmasın" seçeneği eklendi. İşaretlendiğinde, oluşan e-arşiv belgelerinin kalem bilgilerindeki mal ve hizmet tutarı alanına brüt fiyat yazılması sağlandı.
- Fatura / İrsaliye İcmali raporuna genel kısıtlara "T.C. Kimlik No Aralığı", "Vergi No Aralığı" ve "Vergi Dairesi" alanları eklendi. Rapora da vergi no/TCKN ve vergi dairesi alanları eklendi.
- Kalem bilgileri sekmesinde sağ tıkta "Stok Hareket İzleme" ve "Cari Bazında Stok Hareket" ekranlarındaki Fiyat alanına çift tıklandığında, kalem fiyatının tıklanan fiyat olacak şekilde güncellenmesi sağlandı.
- Gümüş uygulaması hesaplamasının cari risk için de hesaplanması sağlandı.
- Alış Parametreleri/Genel 3 sekmesine "Alış Faturasından Satış Belgesi Oluşturulsun" parametresi eklendi. İşaretlendiğinde, Alış faturası üst bilgiler sağ tık menüsünde aktif hale gelen "İşlemler" menüsü ile alış faturasından satış faturası ya da satış irsaliyesi oluşturulabilmesi sağlandı.
- Fatura modülünde fatura, irsaliye, sipariş ve ambar fişi programlarında kalemler sekmesinde sağ tık menüsüne "Çoklu Kalem Girişi" eklendi. Bu ekran ile grid’de seçilen stokların topluca fatura kalemi olarak eklenmesi sağlandı. Kalem eklenirken miktarı 1 olarak atılıyor, fiyat veya depo kodu gibi bilgiler sistemde bulunursa atıyor, bulamazsa boş bırakıyor, zorunluysa stok eklenirken uyarı vermesi sağlanıyor. Ambar fişi özelinde girilen masraf merkezine ait muhasebe kodu tanımlanmamışsa her kaleme muhasebe kodu girilmesi zorunlu olduğu için çoklu kalem girişi yapılamıyor.
- E-Fatura işlemleri altına "e-Logo Entegratör Fark Raporu" eklendi. Bu rapor Logo entegratör kullanan kullanıcılar için aktif oluyor. Bu rapor ile kullanıcıların e-Logo sisteminde bulunan faturaları görmesi, indirilebilir durumdaysa ve Netsis'te bulunmuyorsa indirilebilmesi sağlanıyor. "GİB Belge Numarası" alanında "Netsis'e Fatura İndirilmemiş" yazan faturalar e-Logo'da bulunan ama Netsis'te bulunmayan faturaları gösteriyor.

**Muhasebe Modülü**

- Oluşturulacak hesaba yazılan kod mevcutta varsa işlem yapılamıyordu, mevcutta bulunan kod varsa baz alınacak koddaki grup ve muavin kodlarının bu koda kopyalanması sağlandı. Eğer mevcut kodda grup ve muavinler varsa bunlara dokunulmayıp eksik olan hesaplar açılıyor.
- Muhtasar ve KDV ekranlarında yıl/ay bilgisinin girildiği ön ekrana 'Beyanname Temizleme' butonu eklendi. Böylece parametre ekranlarında ilgili ay için saklanmış parametreler, basım ekranlarında ise ilgili ay için saklanmış tüm kayıtların silinmesi sağlanacaktır. Ayrıca parametre ve basım ekranlarına eklenen 'Tüm alanlar için parametre oku' butonu ile ekrandaki tüm bilgilerin daha önce saklanmış son değerleri ile değiştirilmesi desteklendi.
- Kullanılan e-Defter dosyasının, yayınlanmış olan en güncel dosya olup olmadığına dair versiyon kontrolü yapılması desteklendi. Eğer kullanılan dosya en günceli değil ise, "Defter oluşturmak için gerekli olan dosyalarınız güncel durumda değildir. İşleminize devam etmek istediğinize emin misiniz?" uyarısı ile bilgi verilmesi sağlandı.
- Muhtasar Beyannamesi için "Yeraltı Maden İşletmeleri Bildirimi" ve "İstihdamın Teşvikine İlişkin Bildirim" ekleri desteklendi.
- E-Defter mükelleflerinin Ocak / 2019 döneminden itibaren GİB’e göndermeleri gereken Defter Raporu Beratı dosyasının program üzerinden oluşturulması desteklendi.

**Cari Modülü**

- Özel Hesap Kapatma ekranlarına şube kodu kolonu eklendi.

**MRP Modülü**

- İleri üretim planlama MRP planından oluşturulduğunda çizelgeleme opsiyonlarındaki “MRP Tedarik Planı Dikkate Alınsın” seçeneği işaretli değilmiş gibi çalışması sağlandı.
- Çizelgeleme algoritma opsiyonlarına "En Erken Planlama Tarihi ile Teslim Tarihi Farkı(Gün)" seçeneği eklendi. İleri üretim planlamada çizelgeleme yapılırken teslim tarihini yani işin bitiş tarihini burada verilen gün kadar öne çekerek hesaplama yapılması sağlandı.
- İleri üretim planlama uygulamasında sadece hazırlık aşamasında kullanılan kaynakların gantt sonuç ekranındaki hazırlık süresi kısmında raporlanması sağlandı.
- Dengeleme ekranlarında sonuçlar yüklenirken bilgilendirme penceresi gelmesi sağlandı.
- Gereksinim planlama çalıştırmada, "Kapasite kullanımları kontrol edilsin" parametresi seçiliyken, kapasite planlamaya dahil edilemeyen işler var ise bu işlerin plana dahil edilememe sebepleri ile birlikte, MRP sonuç raporunun "Kapasite Planı Yapılamayan İşler" sekmesinde raporlanması sağlandı.
- İleri üretim planlama gantt sonuç raporunda "Vardiya Bazında Üretim Planı Raporu" eklendi. Bu rapor sayesinde üretilmesi planlanan ürünlerin vardiya ve tarih bazında miktarları raporlanabilir.

**Çek\\Senet Modülü**

- Dövizli Çekler/Senetler Yeniden Değerleme Listesi raporuna "Yeniden Değerleme Tarihi" ve "Döviz Kuru" bilgisi eklendi.
- Müşteri Senetleri\\Kayıt\\Taksitli Satış\\Senet Tahsil ekranına "Ödenen TL Tutar" kolonu eklendi. Bu alan üzerinden ödeme tutarı izlenebilecektir

**Müstahsil Faturası Modülü**

- E-Müstahsil uygulaması desteklendi.

**Dış Ticaret Modülü**

- Çeki Listesinden İrsaliye Oluşturma ekranında gride "Depo Kodu" alanı eklendi. Depo Kodu alanına siparişte girilen depo kodu otomatik gelecek istenirse depo kodu üzerinde değişiklik yapılabilecektir.
- Paket Tanımları ekranına "Hacim" alanı eklendi. Çeki listesi oluşturulurken seçilen paket tipine göre hacim bilgisinin otomatik getirilmesi ve istenirse grid üzerinden değiştirilebilmesi sağlandı.
- Proforma birleştirme ekranında birleştirme yapıldıktan sonra proformaların silinmesi sağlandı. Eğer proformalar saklanmak isteniyorsa buraya yeni eklenen "Birleştirilen Proformalar Saklansın" seçeneği kullanılabilir.
- Dış ticaret modülü ihracat dosya işlemlerinde çeki listesi sekmesinde kalem listesi grid’i akıllı grid olarak güncellendi.
- Dış ticaret modülü raporlarına "Çeki Listesi Kontrol Raporu" eklendi. Bu rapor ile ihracat dosyalarındaki çeki listesinin stokları, kalem miktarı ve kalan miktar yani çeki listesi oluşturulan miktarı görülebilir.
- Mal bedeli ile sevk bedeli farklıysa ihracat kapatma sırasında gelen uyarıda mal bedeli değeri, toplam sevk bedeli (yani irsaliyelerin toplamı) ve aradaki farkın eklenmesi sağlandı.
- Dış ticarette parçalı ithalat için kapatma yapılırken DAT kaydı atıldığında belgenin tarihi fiili ithalat tarihi ile oluşması sağlandı.
- Dış Ticaret modülü İhracat Dosya işlemleri\\Navlun ve Sigorta sekmelerine eklenen "Kur" alanı ile navlun ve sigorta için farklı kur girişi yapılabilmesi desteklendi.

**Makine Bakım Modülü**

- Devir Bakım talep kayıtları ekranına "Talepte Bulunan" alanı eklendi.

**Log Modülü**

- Dış ticaret işlemleri için log tutulması log modülünde desteklendi.

**Talep\\Teklif Modülü**

- Talep/Teklif modülünde muhtelif cari ile belge girişi desteklendi.

**Üretim Modülü**

- Alternatif reçete kaydında grid'in sağ tık menüsüne "Varsayılan Reçete Yap" seçeneği eklendi. Bu seçeneğe tıklandığında ana reçeteyi silip seçili olan alternatif reçetenin ana reçete yapılması sağlandı.
- Üretim Parametreleri / Üretim 2 sekmesine eklenen "Fire Girişinde Fire Kodu Sorulsun" parametresi ile fire uygulamasında fire sebeplerinin girilebilmesi desteklendi. Üretim Sonu Kaydı, Serbest Üretim Sonu Kaydı, Ters Üretim Sonu Kaydı, Mamul Parçalama ve Üretim Akış Kaydı ekranlarında fire girişinden sonra açılan "Fire Detay Girişi" ekranından fire detayları girilebilecektir. Öncelikle Üretim/Kayıt menüsüne eklenen "Fire Tanımlama" ekranından fire kodlarının tanımlanması gerekmektedir. "Fire Girişinde Fire Kodu Sorulsun" parametresinin kullanılabilmesi için üretim parametrelerindeki "Fire Uygulaması" ve "2. Miktar Girilecek" parametreleri işaretli olmalıdır. Girilen fire detay bilgilerinin raporlanabilmesi için de Üretim/Raporlar menüsüne eklenen "Fire Analiz Raporu" kullanılabilir.

**Kasa Modülü**
- Programda Kasa Kayıtları - Banka sekmesine referans kodu alanı eklendi. Muhasebe parametrelerindeki referans kodu seçeneklerine göre aktif ya da pasif gelmektedir.

**Devir Modülü**
- Devir\\Yeni Yıl Kopyalama ekranında” Önceki Yıl Fiyat Listeleri Yeni Yıla Aktarılsın” seçeneği eklendi. Bu seçenek işaretlendiğinde devir yapılan yıla ait fiyat listelerinin de yeni yıl şirketine aktarılması sağlandı.

**Bordro**
- Personel Sabit Bilgileri, Yatay bordro ve Detay Kod girişi ekranına “Kanun 4447 Geçici Madde 19 SGK İşsizlik Terkin” sahası eklenmiştir. Buna göre 17103 ve 27103 terkinleri için işsizlik kısmının ayrı gösterilmesi ve ayrı hesaba entegre edilmesi sağlanmıştır.
- Personel Puantaj Bilgileri ekranında sağ tık’a eklenen “Kişiselleştirilmiş Görünüm” seçeneği ile kullanıcıların ekranda yaptıkları hizalamaların kaydedilmesi ve aynı ekranı tekrar açtıklarında aynı şekilde gelmesi sağlanmıştır.
