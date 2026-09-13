---
title: "Yürüyen Bakiyeli Stok Raporu Desteği"
page_id: "50667421"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Yürüyen Bakiyeli Stok Raporu Desteği"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Yürüyen Bakiyeli Stok Raporu Desteği"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWJhNTQ2OTM3LWQxMTEtNDVjZS1iZTVhLTczNzkzYTk0NmJjYiZsaW5rPWM5MjM0ZDM1LTliNmMtNGVkMC1hYWM1LTUxNGNlYTYxYWZlYiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=ba546937-d111-45ce-be5a-73793a946bcb&link=c9234d35-9b6c-4ed0-aac5-514cea61afeb&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "yuruyen-bakiyeli-stok-raporu-destegi_50667422_50667421.html"
source_version: "2022-11-03T09:08:31.853+03:00"
source_bytes: 323267
fetched_at: "2026-09-13T04:25:41+00:00"
generator: "netsis-scraper 1.0.0"
---
# Yürüyen Bakiyeli Stok Raporu Desteği

Yürüyen Bakiyeli Stok Raporu Desteği ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Yürüyen Bakiyeli Stok Raporu sayesinde belirlenen tarih aralığı içindeki stok bakiyesi değişimi izlenir. İleri tarihe yönelik yapılan planların, stok bakiyesini ne şekilde etkileyeceği raporlanır. Bu uygulama sayesinde, üretim planlama sürecinin daha etkin takibi amaçlanır. Rapor ekranına Üretim modülü altındaki Raporlar menüsünden ulaşılır.

**Kısıt** **Girişi:** Rapor ekranı açıldığında ilk olarak Kısıt Girişi sekmesi ekrana gelir. Kısıt Girişi sekmesi, Stok Kodu Kısıt Girişi, İleri Kısıt Girişi ve Rapor Parametre Girişi olmak üzere üç bölümden oluşur.

**Stok Kodu Kısıt** **Girişi:** Stok Kodu Kısıt Girişi bölümünde Stok Kodu için, stok kartlarında tanımlı Kod-1, Kod-2, Kod-3, Kod-4, Kod-5, Grup Kodu gibi değerlere göre rapor kısıtlaması yapılır. Bu bölümde "Sadece Mamuller/Yarı Mamuller Getirilsin", "Sadece Bileşenler Getirilsin", "Hepsi Getirilsin" gibi seçenekler yardımıyla kısıt girişi daha ayrıntılı bir şekilde yapılabilir.

**İleri** **Kısıt** **Girişi:** İleri Kısıt Girişi bölümünde stok ile ilgili tüm değerlere göre ayrıntılı şekilde kısıtlama yapılması mümkündür.

![](../_assets/40cf25b5623dc97f71aa.png)

**Rapor** **Parametre** **Girişi:** Rapor Parametre Girişi bölümündeki Hareket Tipi seçenekleri aşağıdaki gibidir:

**Başlangıç** **Tarihi:** Raporun alınacağı başlangıç tarihinin belirlendiği alandır.

**Bitiş** **Tarihi:** Raporun bitiş tarihinin belirtildiği alandır.

**İş** **Emirleri** **Kontrol** **Edilsin:** Mamuller için açılan iş emri bilgileri dikkate alınır ve bu iş emirlerinin teslim tarihi dikkate alınarak mamul bakiyesine giriş hareketi raporlanır.

**Talepler** **Kontrol** **Edilsin:** Talep bilgileri dikkate alınarak bu belgelerin teslim tarihinde stok giriş ve çıkış hareketleri raporlanır.

**Serbest** **Stoklar** **Kontrol** **Edilsin:** Rapor için verilen başlangıç tarihinde tüm depoları dikkate alarak stok bakiye bilgisini raporlar.

**Rezerve** **Stoklar** **Kontrol** **Edilsin:** İş emrine rezerve edilen hammadde stokları ve müşteri siparişine rezerve edilen mamul stoklarının dikkate alınarak rapor alınmasını sağlar.

**MRP Sonuçları** **Kontrol** **Edilsin:** MRP sonucuna göre açılacak iş emirleri ve satıcı siparişleri dikkate alınarak raporlanır.

**Siparişler** **Kontrol** **Edilsin:** Satıcı Siparişi ve Müşteri Siparişi dikkate alınarak bu belgelerin teslim tarihinde stok giriş ve çıkış hareketleri raporlanır. Planlanan ve Kesinleşen parametreleri ile rapor sonuçları kısıtlanabilir.![](../_assets/5b0f4d842827bc9bc5f8.png)

**Rapor**

Rapor sekmesinde "Grafik Gösterimi" ve Rapor bölümü bulunur. Grafik Gösterimi bölümü açılır-kapanır özelliğe sahiptir. Rapor kısmına yer kazandırmak amacıyla kapatılabilir. Rapor görünümü otomatik olarak Stok Kodu ve onun altında tarih bazında kırılımlı olarak gelir. Birden fazla stok kodu için rapor alınmışsa, stok kodu kırılımına tıklanarak grafik gösterimi ilgili stok için güncellenir. Grafik gösteriminde mavi renkle taralı alan, stok bakiyesinin zaman eksenindeki değişimini ifade eder. Grafik gösterimindeki kırmızı çizgi, Stok Planlama Kayıtlarında tanımlanan asgari stok miktarını, yeşil çizgi ise azami stok miktarını gösterir. Grafikte istenen alan üzerinde seçim yapılarak yakınlaştırma yapılabilir.
Rapor bölümünde stok kodu için, ilk satırda verilen başlangıç tarihinde, tüm depolar dikkate alınarak stok bakiyesi verilir. Ardından ileri tarihlerdeki planlara göre stok bakiyesindeki değişimler tarih bazında yürüyen bakiye usulüne göre raporlanır. Rapor kısmındaki alan başlıklarına tıklayarak, çoklu seçim ve akıllı filtreleme yapmak mümkündür. Bu bölümde stok ile ilgili giriş çıkış hareketlerine yönelik oluşturulan belgelerin belge tipi, cari kodu, cari adı, depo kodu, depo adı, hareket miktarı ve tarih bazında bakiyesi gösterilir.
Rapor kısmında "Belge Tipi" alanı sayesinde ilgili hareketin hangi belgeye karşılık geldiği anlaşılır.

Raporda hareketlere geçecek belge tipleri aşağıdaki şekilde listelenir:

**Stok:** Başlangıç tarihi için tüm depoları dikkate alarak stok bakiyesini gösterir.

**SatSip :** İlgili tarihte satıcı siparişinden depoya girecek miktarı gösterir.

**MusSip :** İlgili tarihte teslim edilecek müşteri siparişi miktarını gösterir.

**İşemri :** İlgili tarihte iş emrinden tamamlanarak depoya girecek mamul/yarı mamul miktarını gösterir.

**Talep :** Açık teklif bilgisini sipariş haline gelen miktarları düşerek gösterir.

**IsemRzv :** İş emrine rezerve edilmiş malzemelerin, ilgili tarihte ilgili iş emri için tüketileceği miktarını gösterir. Rezervasyonlar, depolar arası transferle veya iş emri malzeme talep ekranı ile yapılır.

**MusSipRzv :** Müşteri siparişine rezerve edilmiş mamullerin ilgili tarihte teslim edileceği miktarı gösterir. Müşteri siparişine rezervasyon, üretim sonu kaydı sırasında iş emri numarası ya da müşteri siparişi numarası belirtilerek yapılır. Aynı zamanda Fatura modülünden yapılan sipariş bağlantılı DAT işlemleri de ilgili siparişe mamul rezervasyonu olarak dikkate alınır.

Rapor sekmesinde sağ tuş özelliklerinde yer alan "Belge Detayı" özelliği ile aşağıda belirtilen belge tipleri bazında, ilgili ekranlara seçilen belge için erişim sağlanır.

**İş** **Emri** veya **IsemRzv** ise "Açıklama" alanındaki iş emri numarası kullanılarak "İş Emri Girişi" ekranı açılır.

**Satsip** ise "Açıklama" alanındaki satıcı siparişi numarası kullanılarak "Satıcı Siparişi" ekranı açılır.

**MusSip** veya **MussipRzv** ise "Açıklama" alanındaki müşteri siparişi numarası kullanılarak "Müşteri Siparişi" ekranı açılır.

**Talep** ise "Açıklama" alanındaki satın alma talep numarası kullanılarak "Satın Alma Talep" ekranı açılır.

**Stok** ise "Stok Kodu" alanındaki değer kullanılarak "Stok Hareket Kayıtları" ekranı açılır.
Bu ekranlar açılırken kullanıcıların hak ve yetkileri kontrol edilir. Kullanıcının ilgili ekran için hakkı yoksa bu menü üzerinden ekranlara erişilemez.
