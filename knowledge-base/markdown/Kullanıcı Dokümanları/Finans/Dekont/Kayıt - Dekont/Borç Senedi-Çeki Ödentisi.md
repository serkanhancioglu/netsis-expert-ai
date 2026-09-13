---
title: "Borç Senedi/Çeki Ödentisi"
page_id: "22805858"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Dekont"
  - "Kayıt / Dekont"
  - "Borç Senedi/Çeki Ödentisi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Dekont / Kayıt / Dekont / Borç Senedi/Çeki Ödentisi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTdkMDJlZWY0LWExYjMtNDE4Ny04MzBiLWI2Y2QwNjE0N2Q5NCZsaW5rPTQzZDhjNDg4LWFlN2UtNDc4Mi04ZDg0LWJhOWI3Y2M1NzVmOSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=7d02eef4-a1b3-4187-830b-b6cd06147d94&link=43d8c488-ae7e-4782-8d84-ba9b7cc575f9&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "borc-senedi-ceki-odentisi_34229012_22805858.html"
source_version: "2022-11-30T10:42:52.317+03:00"
source_bytes: 291100
fetched_at: "2026-09-13T04:09:10+00:00"
generator: "netsis-scraper 1.0.0"
---
# Borç Senedi/Çeki Ödentisi

Borç Senedi/Çeki Ödentisi, Finans Bölümü'nde, "Kayıt/Dekont" menüsünün altında yer alır. Borç Senedi/Çeki Ödentisi, tedarikçi firmalara verilen borç çeklerinin/senetlerinin ödeme işleminin yapılması için kullanılan bölümdür. Borç Senedi/Çeki Ödentisi; Borç Senetleri ve Borç Çekleri olmak üzere iki sekmeden oluşur.

**Borç Senetleri**

![](../../../../_assets/d1c89b50d447347fb241.png)

Borç Senetleri alanları ve içerdiği bilgiler aşağıdaki şekildedir:

| Borç Senedi/Çeki Ödentisi Ekranı |  |
| --- | --- |
| Senet No | Ödeme işleminin yapılacağı senet numarasının girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, senet numaralarına ulaşılır. |
| Seri Kodu | Girilen senedin seri numarasının kaydedildiği alandır. Boş bırakılmaz. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, seri kodlarına ulaşılır. |
| Dekont No | Program tarafından otomatik olarak her bir dekont serisi 1 rakamından başlar. Kaydedilen her dekont için bir sayı arttırılarak devam eder. Farklı bir numaradan başlaması istendiğinde ise; Dekont → İşlemler → "[Dekont Numarası Düzenleme](<../İşlemler - Dekont/Dekont Numarası Düzenleme.md>)" bölümü kullanılarak serilere başlangıç numarası verilir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, kayıtlı dekont numaralarına ulaşılır. |
| Fiş No | Borç senedi ödendi kaydı için fiş numarası girilen alandır. Bu alana girilen numara Muhasebe Entegrasyonu ve Cari Hareket Kayıtları bölümlerinde yer alan "Fiş No" alanına aktarılır. |
| İşlem Tarihi | Borç senedi/çeki ödenti kaydının girildiği tarihtir. Yapılacak işlem sonucu oluşacak kayıtlar ,diğer modüllere (Banka-Entegrasyon-Senet) bu tarih ile kaydedilir. |
| Tutar | Girilen senet numarasına göre tutar bilgisinin otomatik olarak aktarıldığı alandır. "Döviz Tipi" seçilerek girilen kayıtlarda, "Döviz Tutarı" ve "Kur" çarpılarak hesaplanan tutar bu alana aktarılır. |
| Döviz/Türk Lirası | Döviz bilgisi girilerek oluşturulacak kayıtlar için "Döviz", Türk Lirası girilerek oluşturulacak kayıtlar için "TL" seçeneğinin işaretlenmesi gerekir. Döviz seçeneği ile girilen kayıtlarda döviz sorgulama ekranı görüntülenir. Sorgulanan döviz kuru bilgisi ile "Tutar" alanına girilecek "Döviz Tutarı" çarpılarak TL değerine çevrilir. Hesaplanan değer "Tutar" alanına aktarılır. Bu uygulama, "Değişsin" alanında yapılan seçime göre farklılık gösterir. Döviz tutarı, "Cari Hareket Kayıtları" bölümüne (Döviz uygulaması olan firmalar için) aktarılır. |
| Döviz Tutarı | Kur bilgisi girildikten sonra ilgili hareketin döviz tutarının girildiği alandır. |
| Döviz Bilgileri | Program, (Girilen borç senedi/borç çeki dövizle kaydedilmiş ise) dekont tarihinde kur değişikliği dolayısı ile oluşacak farkın hesaplanması için kur bilgisini sorgular. Döviz bilgileriyle kaydedilmeyen çek ya da senetler için bu sorgulama yapılmaz. |
| Kur Farkı | Döviz bilgileriyle kaydedilen senet ve çekler için, verildiği tarih ile ödendiği tarih arasında kur değişikliğinden kaynaklanan farkın aktarıldığı alandır. Boş bırakılır ve kullanıcı müdahale edemez. |
| Cari/Muhasebe/Banka | Senet ya da çek tutarının alacak olarak kaydedileceği hesabın seçildiği alandır. Cari, Muhasebe ve Banka olmak üzere üç seçenekten oluşur. Muhasebe seçildiğinde, program muhasebe kodu sorgular ve senet tutarını, girilen muhasebe koduna alacak olarak kaydeder. Banka seçildiğinde, program banka kodu sorgular ve senet tutarını, girilen banka koduna alacak olarak kaydeder. Cari seçildiğinde ise, program cari kod sorgular ve senet tutarını, girilen cari koda alacak olarak kaydeder. |
| Banka Kodu | Borç senetleri yada çekleri için takip edilen banka hesabının cari hesapta takip edilmesi durumunda ilgili banka cari kodunun, banka modülünde olması durumunda ise banka kodunun girildiği alandır. |
| Cari Rapor Kodu | Cari → Kayıt → [Cari Parametreleri](<../../Cari/Kayıt - Cari/Cari Parametreleri.md>) → "Hareketlerde Rapor Kodu Girilsin" parametresinin işaretlenmesi ile aktif hale gelen alandır. Hareketlere aktarılması ve raporlanması amacıyla 1 karakterden oluşan rapor kodu girişi yapılır. |
| Plasiyer Kodu | Yardımcı Programlar → Kayıt → [Şirket-Şube Parametreleri](<../../../Muhasebe/Muhasebe Modülü/Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/Genel Tanımlar/Yardımcı Programlar-Şirket-Şube Parametreleri.md>) → "Plasiyer Uygulaması Var" parametresinin işaretlenmesi ile aktif hale gelen alandır. Dekont kaydı sırasında ilgili plasiyer kodunun girilmesi gerekir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, plasiyer kodlarına ulaşılır. Boş bırakılmaz. |
| Proje Kodu | Yardımcı Programlar → Kayıt → [Şirket-Şube Parametreleri](<../../../Muhasebe/Muhasebe Modülü/Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/Genel Tanımlar/Yardımcı Programlar-Şirket-Şube Parametreleri.md>) → "Proje Uygulaması Var" parametresinin işaretlenmesi ile aktif hale gelen alandır. Dekont kaydı sırasında ilgili plasiyer kodunun girilmesi gerekir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, proje kodlarına ulaşılır. Boş bırakılmaz. Girilen proje kodları, cari hareketlere ve entegrasyona aktarılır. |
| Banka Kayıtları Detaylı Oluşturulsun | Senet/çek muhasebe hesap kayıtları kümüle edilmeden detaylı olarak oluşturulması için kullanılan seçenektir. |
| Açıklama | Bu alana açıklama olarak “?? NOLU SENET/ÇEK ÖDENTİSİ” program tarafından otomatik olarak aktarılır. Kullanıcı tarafından değişiklik yapılabilir. |
| Özel Basım | Dekont kaydının basımı için "Dizayn Modülü" ile hazırlanan özel bir basımın kullanılması istendiğinde işaretlenen seçenektir. Özel bir basım değil, standart bir basım yapılması istendiğinde bu seçenek işaretlenmemesi, sadece "Basım "alanındaki "Evet" seçeneğinin işaretlenmesi gerekir. |
| Basım | Dekont kaydının basımı için kullanılan seçenektir. İşlemler bittikten sonra Tamam ![](../../../../_assets/39d77b8716226638d9ce.jpg) butonuna basıldığında, "Müşteri Senetleri Modülünde" ilgili senedin durumu program tarafından “Ödendi” olarak değiştirilir. İlgili yevmiye maddeleri oluşturularak Entegre → Kayıt → [Entegrasyon Kayıtları](<../../../Muhasebe/Entegre/Kayıt - Entegre/Entegrasyon Kayıtları.md>) → Dekont sekmesinden izlenir. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilginin onaylanmasını sağlayan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgiden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |

**Borç Çekleri**

![](../../../../_assets/a95bf4b34e8f3852efb5.png)

Borç Çekleri alanları ve içerdiği bilgiler aşağıdaki şekildedir:

| Borç Senedi/Çeki Ödentisi Ekranı |  |
| --- | --- |
| Çek No | Ödeme işleminin yapılacağı çek numarasının girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, çek numaralarına ulaşılır. |
| Seri Kodu | Girilen senedin seri numarasının kaydedildiği alandır. Boş bırakılmaz. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, seri kodlarına ulaşılır. |
| Dekont No | Program tarafından otomatik olarak her bir dekont serisi 1 rakamından başlar. Kaydedilen her dekont için bir sayı arttırılarak devam eder. Farklı bir numaradan başlaması istendiğinde ise; Dekont → İşlemler → "Dekont Numarası Düzenleme" bölümü kullanılarak serilere başlangıç numarası verilir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, kayıtlı dekont numaralarına ulaşılır. |
| Fiş No | Borç çeki ödendi kaydı için fiş numarası girilen alandır. Bu alana girilen numara Muhasebe Entegrasyonu ve Cari Hareket Kayıtları bölümlerinde yer alan "Fiş No" alanına aktarılır. |
| İşlem Tarihi | Borç senedi/çeki ödenti kaydının girildiği tarihtir. Yapılacak işlem sonucu oluşacak kayıtlar ,diğer modüllere (Banka-Entegrasyon-Senet) bu tarih ile kaydedilir. |
| Tutar | Girilen çek numarasına göre tutar bilgisinin otomatik olarak aktarıldığı alandır. "Döviz Tipi" seçilerek girilen kayıtlarda, "Döviz Tutarı" ve "Kur" çarpılarak hesaplanan tutar bu alana aktarılır. |
| Döviz/Türk Lirası | Döviz bilgisi girilerek oluşturulacak kayıtlar için "Döviz", Türk Lirası girilerek oluşturulacak kayıtlar için "TL" seçeneğinin işaretlenmesi gerekir. Döviz seçeneği ile girilen kayıtlarda döviz sorgulama ekranı görüntülenir. Sorgulanan döviz kuru bilgisi ile "Tutar" alanına girilecek "Döviz Tutarı" çarpılarak TL değerine çevrilir. Hesaplanan değer "Tutar" alanına aktarılır. Bu uygulama, "Değişsin" alanında yapılan seçime göre farklılık gösterir. Döviz tutarı, "Cari Hareket Kayıtları" bölümüne (Döviz uygulaması olan firmalar için) aktarılır. |
| Döviz Tutarı | Kur bilgisi girildikten sonra ilgili hareketin döviz tutarının girildiği alandır. |
| Döviz Bilgileri | Program, (Girilen borç senedi/borç çeki dövizle kaydedilmiş ise) dekont tarihinde kur değişikliği dolayısı ile oluşacak farkın hesaplanması için kur bilgisini sorgular. Döviz bilgileriyle kaydedilmeyen çek ya da senetler için bu sorgulama yapılmaz. |
| Kur Farkı | Döviz bilgileriyle kaydedilen senet ve çekler için, verildiği tarih ile ödendiği tarih arasında kur değişikliğinden kaynaklanan farkın aktarıldığı alandır. Boş bırakılır ve kullanıcı müdahale edemez. |
| Cari/Muhasebe/Banka | Senet ya da çek tutarının alacak olarak kaydedileceği hesabın seçildiği alandır. Cari, Muhasebe ve Banka olmak üzere üç seçenekten oluşur. Muhasebe seçildiğinde; program muhasebe kodu sorgular ve çek tutarını, girilen muhasebe koduna alacak olarak kaydeder. Banka seçildiğinde; program banka kodu sorgular ve çek tutarını, girilen banka koduna alacak olarak kaydeder. Cari seçildiğinde ise; program cari kod sorgular ve çek tutarını, girilen cari koda alacak olarak kaydeder. |
| Banka Kodu | Borç senetleri yada çekleri için takip edilen banka hesabının cari hesapta takip edilmesi durumunda ilgili banka cari kodunun, banka modülünde olması durumunda ise banka kodunun girildiği alandır. |
| Cari Rapor Kodu | Cari → Kayıt → Cari Parametreleri → "Hareketlerde Rapor Kodu Girilsin" parametresinin işaretlenmesi ile aktif hale gelen alandır. Hareketlere aktarılması ve raporlanması amacıyla 1 karakterden oluşan rapor kodu girişi yapılır. |
| Plasiyer Kodu | Yardımcı Programlar → Kayıt → Şirket-Şube Parametreleri → "Plasiyer Uygulaması Var" parametresinin işaretlenmesi ile aktif hale gelen alandır. Dekont kaydı sırasında ilgili plasiyer kodunun girilmesi gerekir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, plasiyer kodlarına ulaşılır. Boş bırakılmaz. |
| Proje Kodu | Yardımcı Programlar → Kayıt → Şirket-Şube Parametreleri → "Proje Uygulaması Var" parametresinin işaretlenmesi ile aktif hale gelen alandır. Dekont kaydı sırasında ilgili plasiyer kodunun girilmesi gerekir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, proje kodlarına ulaşılır. Boş bırakılmaz. Girilen proje kodları, cari hareketlere ve entegrasyona aktarılır. |
| Banka Kayıtları Detaylı Oluşturulsun | Senet/çek muhasebe hesap kayıtları kümüle edilmeden detaylı olarak oluşturulması için kullanılan seçenektir. |
| Açıklama | Bu alana açıklama olarak “?? NOLU SENET/ÇEK ÖDENTİSİ” program tarafından otomatik olarak aktarılır. Kullanıcı tarafından değişiklik yapılabilir. |
| Özel Basım | Dekont kaydının basımı için "Dizayn Modülü" ile hazırlanan özel bir basımın kullanılması istendiğinde işaretlenen seçenektir. Özel bir basım değil, standart bir basım yapılması istendiğinde bu seçenek işaretlenmemesi, sadece "Basım "alanındaki "Evet" seçeneğinin işaretlenmesi gerekir. |
| Basım | Dekont kaydının basımı için kullanılan seçenektir. İşlemler bittikten sonra Tamam ![](../../../../_assets/39d77b8716226638d9ce.jpg) butonuna basıldığında, "Müşteri Çekleri Modülünde" ilgili çekin durumu program tarafından “Ödendi” olarak değiştirilir. İlgili yevmiye maddeleri oluşturularak Entegre → Kayıt → Entegrasyon Kayıtları → Dekont sekmesinden izlenir. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilginin onaylanmasını sağlayan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgiden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |

**Borç Senedi/Çeki Ödeme Dekont İptali**

Borç Senedi/Çeki Ödeme Dekontunun iptali yerine ters kayıt oluşturulur. Bu dekont kaydına ait ters kayıtların nasıl oluşturulacağı ile ilgili detaylı bilgi; [Çek Tahsil Dekontu](<Tahsil-Teminat-Ciro Çekleri Ödeme Dekontu/Çek Tahsil Dekontu/index.md>) bölümünde yer alır.
