---
title: "Veri Tabanı Kontrol Paneli Sıkça Sorulan Sorular"
page_id: ""
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Veri Tabanı Kontrol Paneli Sıkça Sorulan Sorular"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Veri Tabanı Kontrol Paneli Sıkça Sorulan Sorular"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTM5MWU5ZmVkLTNhZTctNGViOS04ZjE2LWQwZDQ5ODU4YWRhMCZsaW5rPTBlM2NiZTE0LTI4YWUtNDAyNi1hZWM5LTUyOGM3ZjBhODRkYSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=391e9fed-3ae7-4eb9-8f16-d0d49858ada0&link=0e3cbe14-28ae-4026-aec9-528c7f0a84da&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "veri-tabani-kontrol-paneli-sikca-sorulan-sorular.html"
source_version: ""
source_bytes: 10726
fetched_at: "2026-09-13T04:21:53+00:00"
generator: "netsis-scraper 1.0.0"
---
# Veri Tabanı Kontrol Paneli Sıkça Sorulan Sorular

- **Veri Tabanı Kontrol Paneli hangi amaçla kullanılır ve ne tür raporlamaları sağlar?**

Veri Tabanı Kontrol Paneli üzerinden, veri tabanına ait genel bilgiler, tablo ve index bilgileri, şema/nesne farkları ve performans testi gibi konularda raporlama yapılabilmektedir.
- **Veri Tabanı Kontrol Paneli hangi Netsis sürüm ve paketlerinde kullanılabilir?**

Netsis 9.0.51 ve üzeri sürümlerde tüm Netsis paketlerinde kullanılabilir.
- **Veri Tabanı Kontrol Paneli hangi veri tabanı türlerinde çalışır?**

Sadece Microsoft SQL Server için desteklenmektedir.
- **“Genel Bilgiler” sekmesinde hangi bilgiler listelenir?**

Veri tabanı sunucusu bilgileri altında, sunucu ve istemci bilgileri yer alır. Veri Tabanı Bilgileri altında MDF Dosya Adı, MDF Dosya Yolu, MDF Dosya Boyutu, LDF Dosya Adı, LDF Dosya Yolu, LDF Dosya Boyutu, Toplam Index Boyutu, Toplam Veri Boyutu, Toplam Boş Alan, Oluşturma Zamanı, Son Yedekleme Zamanı, Collation ve Uyumluluk Seviyesi gibi bilgiler görüntülenir.
- **“Tablo Bilgileri" sekmesinde hangi bilgiler listelenir?**

Raporun alındığı aktif şirkete ait veri tabanında bulunan tüm tablolar listelenir. Her bir tablo için; tablo adı, kayıt sayısı, veri boyutu, index boyutu, SQL Server tarafından ayrılmış ancak henüz kullanılmayan alan boyutu ile toplam disk alanı görüntülenebilir.
- **Tablo Bilgileri sekmesindeki "Kullanılmayan Alan" ve "Disk Boyutu" ne anlama gelir?**

"Kullanılmayan Alan" SQL Server'da ayrılmış fakat kullanılmayan alanı, "Disk Boyutu" ise toplam alan boyutunu MB olarak gösterir.
- **"Index Bilgileri" sekmesinde hangi bilgiler listelenir?**

Tablo adı, tablodaki index adı, index tipi, index’in içerdiği kolon listesi, index boyutu ve fragmentation (parçalanma) seviyesi yüzde olarak gösterilir.
- **Index Bilgileri sekmesinde bulunan fragmentation seviyesi nedir ve neden önemlidir?**

Fragmentation, index’lerin parçalanma seviyesidir. Yüksek fragmentation değeri sorgu performansını olumsuz etkiler. Veri tabanı Kontrol Paneli üzerinden fragmentation oranlarına göre sıralama yapılarak index bakım işlemleri başlatılabilir.
- **Index bakımı nasıl yapılır?**

Index’ler seçildikten sonra “Index Bakım” butonuna tıklanır.

Seçilenler İçin Çalıştır: Seçilen index’ler için bakım yapılır.

Tümü İçin Zamanlanmış Görev: Zamanlanmış Görevler eklentisi üzerinden index bakım işleminin çalıştırılması periyodik olarak zamanlanabilir.

Bakım sırasında %40’tan yüksek fragmentation oranı için rebuild (yeniden oluşturma), %40’tan düşük fragmentation oranı için reorganize (yeniden düzenleme) işlemi yapılır. Ayrıca, istatistiklerin güncellenmesi seçeneği de bulunmaktadır.
- **Indeks bakımı sırasında fragmentation sınır oranı değiştirilebilir mi?**

Evet, indeks bakımı sırasında “Fragmentation Sınır Değeri (%)” alanına istenilen yüzde değeri girilerek fragmentation oranı değiştirilebilir.
- **Index bakımında “İstatistikler Güncellensin” seçeneği ne işe yarar?**

Bu seçenek işaretlendiğinde, bakım sonunda SP_UPDATESTATS komutu çalıştırılır. Bu işlem veri tabanı performansını artırmak için SQL Server’ın istatistiklerini günceller. İstatistikler Güncellenesin seçeneği varsayılan olarak işaretlidir.
- **Şema/Nesne Farkları raporu ne işe yarar?**

Aktif şirket ile kaynak şirket arasındaki veritabanı nesnelerindeki farkları göstererek, veritabanı yapılarının tutarlılığının kontrol edilmesini sağlar.
- **Kaynak Test Şirketi nedir ve nasıl oluşturulur?**

Aktif şirketin seçilen bir veritabanı ile karşılaştırılması amacıyla kullanılan test veri tabanıdır. “Kaynak Test Şirketi Oluştur” seçeneği ile sıfırdan bir test şirketi oluşturulabilir.
- **Kaynak Test Şirketi Oluştur seçeneği ile oluşturulan test şirketi işlem sonrasında otomatik silinir mi?**

Evet, “Kaynak Test Şirketi Oluştur” seçeneğiyle oluşturulan şirket rapor tamamlandıktan sonra silinir. Mevcut şirketlerden seçilen kaynak şirket için ise herhangi bir işlem yapılmaz.
- **Nesne Detayları Karşılaştırma ekranı ne işe yarar?**

Fark tespit edilen nesnelerin (örn; Procedure, Function, Trigger) SQL CREATE cümlelerini yan yana karşılaştırmak için kullanılır. "Detay" kolonundaki üç noktaya tıklayarak cümleler arasındaki farkların detayı görülebilir. "Detay" kolonuna tıklandığında açılan ekranda, sol tarafta nesneye ait kaynak şirket üzerindeki sql cümlesi gösterilirken, sağ tarafta ise aktif şirket için sql cümlesi gösterilmektedir. Ekranın üst bölümündeki "Önceki Fark" ve "Sonraki Fark" butonlarına tıklayarak iki cümle arasında fark veren satırlara hızlıca odaklanılması sağlanabilir.
- **Şema/Nesne Farkları ve Performans Testi raporların çalıştırılması ne kadar sürer?**

Şema/Nesne Farkları ve Performans Testi işlemleri yüksek veri hacmi ve dummy veri oluşturma-silme gibi işlemler içerdiğinden zaman alabilir. İşlem sırasında ekranda “Test Şirketi Oluşturuluyor, Rapor Hazırlanıyor, Test Şirketi Siliniyor” gibi açıklamalarla mevcut durum gösterilir.
- **Nesne farklılıkları tespit edildiğinde bu farkları otomatik düzeltme seçeneği var mı?**

Hayır, sistem yalnızca nesne farklılıklarını raporlar ve otomatik düzeltme yapmaz. Tespit edilen farklar manuel incelenmeli ve düzeltme için karar verilmelidir.
- **Şema/Nesne farklılıkları test şirketi oluşturulmadan raporlanabilir mi?**

Evet. “Kaynak Şirket Seç” seçeneği ile daha önce oluşturulmuş mevcut şirket veri tabanları karşılaştırma için kullanılabilir. Bu işlemde test şirketi oluşturulmaz.
- **Performans testi neyi ölçer ve nasıl çalışır?**

Performans testi, veri tabanında Select, Insert, Update ve Delete işlemlerinin ne kadar sürede yapıldığını ölçer. Sonuç raporu, her işlem için maksimum, minimum, ortalama süre ve standart sapma değerlerini içerir.
- **Performans testleri hangi tablolar üzerinde gerçekleştirilir?**

Test sırasında STHAR, CAHAR, MUHFIS, DEKOTRA, FATUIRS, ISEMRI tablolarında rastgele seçilen kayıtlarla SELECT, INSERT, UPDATE, DELETE işlemleri yapılır.
- **Performans testindeki varsayılan kayıt sayıları değiştirilebilir mi?**

Evet. Aşağıdaki özel parametreler ile ölçüm sayısı değiştirilebilir.

"YARDIMCI","PERFTEST_DUMMY_OLCUMSAYI" → Varsayılan 10000

"YARDIMCI","PERFTEST_SELECT_OLCUMSAYI" → Varsayılan 1000
- **Performans testi sırasında hangi işlemler ölçülür?**

Insert (tek tek ve toplu – farklı yöntemlerle)

Select (sonuç getirme ve okuma)

Update (tek tek ve toplu)

Delete (tek tek ve toplu)

STHAR, CAHAR, MUHFIS vb. tablolardan rastgele SELECT işlemleri

Her işlem için maksimum, minimum, ortalama süre ve standart sapma hesaplanır.
- **Performans testi sırasında sistem performansı etkilenir mi?**

Test sırasında oluşturulan dummy veri ve işlemler, kısa süreli olarak veri tabanı kaynaklarını kullanır. Yoğun kullanılan sistemlerde performans test işleminin mesai saatleri dışında çalıştırılması önerilir. Test sonrasında tüm dummy veriler otomatik olarak temizlenir.
- **Performans testi sonuçları nasıl yorumlanmalıdır?**

Her test için ortalama süre ve standart sapma değerleri dikkate alınmalıdır. Ortalama sürelerin yüksek çıkması durumunda donanım, sunucu kaynakları, SQL Server yapılandırması ve ağ bağlantıları gibi sistem bileşenleri gözden geçirilebilir.
- **Performans testi sonuç raporları dışarı aktarılabilir mi?**

Grid alanda Sağ Klik\>Gönder\>Excel seçeneği ile Excel ortamına aktarılabilir.
- **Panelde gösterilen rapor sonuçları hangi tabloda saklanır?**

Veri tabanı kontrol paneli işlemleri sırasında oluşturulan raporlar ve işlemler aşağıdaki tablolarda saklanır.

Şema farkları: TBLDBOBJCONTROLMAS, TBLDBOBJCONTROLDETAIL

Performans testleri: TBLDBPERFCONTROLMAS, TBLDBPERFCONTROLDETAIL

Not: Bu kayıtlar yeni rapor çalıştırıldığında silinir ve güncel verilerle yeniden oluşturulur.
- **Veri Tabanı Kontrol Paneline tüm kullanıcılar erişebilir mi, yoksa admin yetkisi mi gereklidir?**

Ekrana erişim SSO’da tanımlanan yetkilendirme ile belirlenir. Yardımcı Programlar \> “Veri Tabanı Kontrol Paneli” menüsüne yetki tanımlanmalıdır.
