---
title: "TFRS Fiş Girişi"
page_id: "39420276"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Muhasebe"
  - "Muhasebe Modülü"
  - "Kayıt / Muhasebe"
  - "TFRS Fiş Girişi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / Kayıt / Muhasebe / TFRS Fiş Girişi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWJkNDc4NzQxLWE4ZWYtNDY2MC05ZDQzLWY0ZmFkMDY0NmZhNiZsaW5rPTFmNGM5YjllLWViN2YtNDVhYi1iZTdmLTAyOWZmMzkxODQ3NSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=bd478741-a8ef-4660-9d43-f4fad0646fa6&link=1f4c9b9e-eb7f-45ab-be7f-029ff3918475&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "tfrs-fis-girisi_39420294_39420276.html"
source_version: "2022-09-28T17:44:00.023+03:00"
source_bytes: 133561
fetched_at: "2026-09-13T04:13:05+00:00"
generator: "netsis-scraper 1.0.0"
---
# TFRS Fiş Girişi

TFRS Fiş Girişi, Muhasebe Bölümü'nde, "Kayıt/Muhasebe Modülü" menüsünün altında yer alır.

TFRS Fiş Girişi, Muhasebe-Kayıt-[Muhasebe Parametreleri](<Muhasebe Parametreleri.md>)-Dövizli Muhasebe-"TFRS" parametresinin işaretlenmesi ile menüye eklenir.

TFRS Fiş Girişi, sistem tarafından oluşturulan TFRS fişlerinin görülmesini ve gerekli düzenlemelerin yapılmasını sağlayan bölümdür. " Fiş Girişi" ekranı ile birbirine benzer. Bu ekrandan sadece "TFRS" değerleri girilir. Aynı fiş içerisinde hem TL, hem TFRS değerleri girilecekse, " Fiş Girişi" ekranının kullanılması gerekir. TFRS değerleri, fişinde firma döviz alanından takip edilir. TFRS Fiş Girişi, Fiş Genel Bilgisi Ve Fiş Detay sekmelerinden oluşur.

**Fiş Genel Bilgisi**

![](../../../../_assets/9b01e4a93392b34c87dd.png)

TFRS Fiş Girişi ekranı Fiş Genel Bilgisi sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| TFRS Fiş Girişi Ekranı |  |
| --- | --- |
| Ay Kodu | TFRS fişi oluşturulacak veya önceden girilen TFRS fişinin düzenleneceği ay kodunun girildiği alandır. Son fiş numarası ve tarihi, kullanıcıya bilgi vermesi amacıyla ilgili ay içinde işlenen fişin numarası ve tarihi olarak ekrana getirilir. Bir aya ait sınırsız sayıda TFRS fişi kaydedilebilir. TFRS fişi içinde ve diğer bölümlerde ay kodunu düzeltme ve değiştirme imkanı yoktur. |
| Son Fiş Numarası | İlgili ay içinde kaydedilen son fiş numarasının izlendiği alandır. Kullanıcı tarafından değişiklik yapılamaz. |
| Son Fiş Tarihi | İlgili ay içinde kaydedilen son fiş tarihinin izlendiği alandır. Kullanıcı tarafından değişiklik yapılamaz. |
| Fiş Numarası | Kaydı yapılacak TFRS fiş numarasının girildiği alandır. Kayıtlı olan son belge numarasının bir büyüğü, program tarafından otomatik olarak ekrana getirilir. Önceden kaydedilen bir fişi izlemek için, fiş numarasının bu alana girilmesi gerekir. Fiş bilgileri ekrana program tarafından otomatik olarak aktarılır. Son kalan fişe numara aralığı verilip daha büyük bir numaradan devam edilmesi istendiğinde, istenilen aralık verilerek fiş numarası girilir. Geçmiş tarihlere ait belgelerin kayıtları, kalan numara takip edilerek oluşturulur. Daha sonra Muhasebe → İşlemler → "[Tarih Bazında Yeniden Numaralandırma](<../İşlemler - Muhasebe/Tarih Bazında Yeniden Numaralandırma.md>)" bölümü kullanılarak, fişler tarih sırasına göre numaralandırılabilir. Önceden hiç fiş kaydı yapılmamış ayın başlangıç numarasını belirlerken (bir önceki ayın son fiş numarası henüz belli değilse) 1 numarasından başlatılıp daha sonra yine “Tarih Bazında Yeniden Numaralandırma” bölümü kullanılarak, asıl başlangıç numarasından itibaren fişler numaralandırılabilir. Bu programın çalıştırılmasından sonra, program eski fiş numaralarını "Açıklama-2" alanına aktarır. Programda, şubeli muhasebe mantığına göre, şubelerden girilen fiş numaralarının başına şube numarası girilir. |
| Tarih | TFRS fişinin hangi tarihe ait olduğu ve ay kodu daha önceden belirlendiği için, sadece gün bilgisinin girildiği alandır. Daha önce kaydedilen bir TFRS fişinin tarihi bu ekrandan değiştirilemez. Kaydedilen fiş numarası yazıldıktan sonra, tarih bilgisi ekrana gelir. |
| Yevmiye Madde No | Yevmiye defter basımı yapıldıktan sonra, ilgili fişin madde numarasının program tarafından otomatik aktarıldığı alandır. |
| Düz. Yevmiye Madde No | Enflasyon muhasebesinin kullanıldığı durumlarda işlev kazanan bir alandır. Enflasyon muhasebesi ile ilgili detaylı bilgi; Muhasebe → Ekler → [Ek-1 Enflasyon Muhasebesi](<../Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/index.md>) bölümünde yer alır. |
| Fiş Tipi | TFRS fiş girişi sırasında, fiş tipinin “Kasa Tahsil”, “Kasa Tediye”, “Açılış Fişi”, “Kapanış Fişi” ya da “Mahsup” olarak belirlendiği alandır. Fiş listelerinden tipine göre seçimli döküm alınmasını sağlar. Programı muhasebe ile entegre kullanan kullanıcıların, entegrasyonda Kasa Tahsil/Tediye bölümündeki Fiş Tipi Tahsil/Tediye, Diğer Müşteri/Satıcı, Borç/Alacak ve Dekont kayıtlarının fiş tipi "Mahsup" olarak aktarılır. Ayrıca yıl sonu zamanı muhasebe hesaplarının kapatılması için "Kapanış Fişi" (hesaplar kapatıldıktan sonra Bilanço ve Gelir Tablosu almak için hesap kapatma kayıtlarının, "Kapanış" tipli fişlerde olması gerekir), kapatılan fişlerin sonraki yılda olması gereken bakiyelerinin oluşması için de "Açılış Fişi" kullanılır. |
| Açıklama-1 Açıklama-2 Açıklama-3 | İsteğe bağlı, TFRS fişine ait genel açıklamaların yazıldığı alanlardır. Muhasebe → İşlemler → "[Tarih Bazında Yeniden Numaralandırma](<../İşlemler - Muhasebe/Tarih Bazında Yeniden Numaralandırma.md>)" bölümünün çalıştırılmasından sonra, eski fiş numaraları (istenen durumlarda) "Açıklama-2" alanına aktarılır. |
| **![](../../../../_assets/fd1a13b1e1de342a0793.png)** Fiş İptal | TFRS fişinin iptal edilmesi için kullanılan butondur. "Fiş No" alanına iptal edilecek fiş numarası girildikten sonra "Fiş İptal" butonuna basılarak ilgili fiş iptal edilir. |

**Fiş Detay**

![](../../../../_assets/e853f9bf6743a2e442c6.png)

TFRS Fiş Girişi ekranı Fiş Detay sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| TFRS Fiş Girişi Ekranı |  |
| --- | --- |
| Fiş No | "Fiş Genel Bilgisi" sekmesinde girilen fiş numarasının izlendiği alandır. |
| Tarih | "Fiş Genel Bilgisi" sekmesinde girilen fiş tarihinin izlendiği alandır. |
| Fiş Tipi | "Fiş Genel Bilgisi" sekmesinde seçilen fiş tipinin izlendiği alandır. |
| Sıra No | Fiş içindeki kayıtların sıra numaralarının izlendiği alandır. Kayıtlar yapıldıkça program tarafından otomatik olarak arttırılır. Kullanıcı tarafından müdahale edilmez. TFRS fişinde 32.000 satır girişi yapılabilir. |
| Hesap Kodu | TFRS fiş satırının hesap planındaki hesaplardan hangisine ait olduğunun belirlenmesi için kullanılan alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılır. Sadece "Muavin" tipinde tanımlanan hesaplara kayıt yapılabilir. Boş bırakılmaz. Hesap planında şimdiye kadar hiç tanımlaması yapılmamış bir kod girildiğinde, alanın boş bırakılmasına izin verilmez. Hesap planında ilgili hesap tanımlandıktan sonra kayda devam edilir. |
| Borç/Alacak (B/A) | TFRS fiş kaydı oluşturulurken belirlenen hesap koduna, tutarın borç olarak mı yoksa alacak olarak mı işleneceği seçilir. |
| Açıklama 1, Açıklama 2 | TFRS fiş satırı için açıklama girilen alandır. Çok kullanılan bazı açıklama satırları "Fiş Açıklama Kayıtları" bölümünden tanımlandığında, her seferinde tekrar yazılması yerine rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) kullanılarak ekrana aktarılabilir. Aktarılan açıklama üzerinde değişiklik yapılabilir. |
| Evrak Tarihi | Evrakın kayıt tarihi ile evrak üzerindeki tarihin farklı olduğu durumlarda, evrak gerçek tarihinin girilerek izleme ve raporlama yapılmasını sağlar. Fişte girilen hareketin fiş tarihi bu alana aktarılır. Üzerinde değişiklik yapılabilir. Entegrasyondan aktarılan kayıtlarda da, evrak tarihi ilgili kaydın tarihi olarak bu alana aktarılır. |
| Referans Kodu | Referans kodu girilen bölümde, referans kodlarının girişi ve referans kodlarına isim açıklama tanımlaması yapılır. Bu bölümde girilen kayıtların, yevmiye fişlerinde ve entegre kayıtlarda kullanmak için Muhasebe → Kayıt → Muhasebe Parametreleri → “Fişlerde Referans Kodu Sorulsun” parametresinin işaretli olması gerekir. Yevmiye fiş girişi sırasında, entegrasyon işlemlerinde, dekont, kasa, ambar giriş/çıkış fişi işlemlerinde, alanının yanında yer alan rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile referans kodlarına ulaşılır. "Referans Kodu" alanını kullanan kullanıcılar, referans mizan listesi ve diğer raporlardaki referans aralığı tanımlamaları ile döküm alabilir. |
| Proje Kodu | Yardımcı Programlar → Kayıt → [Şirket/Şube Parametreleri](<../Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/Genel Tanımlar/Yardımcı Programlar-Şirket-Şube Parametreleri.md>) → “Proje Uygulaması Var” parametresinin işaretlenmesi ile aktif hale gelen alandır. Proje takibi yapılan hesaplarda kullanılır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, proje kodlarına ulaşılır. |
| Miktar | İlgili kayıt için, hesap kodunun ölçü birimi cinsi üzerinden miktar (varsa) girilen alandır. |
| KDV | İlgili kayda ait KDV oranının (varsa) girilmesini sağlamak için işaretlenen alandır. İşaretlendiğinde, KDV oranının girilmesini sağlayan alan aktif hale gelir. |
| Vade Günü | Vade günü değerinin bilgi amaçlı girildiği alandır. |
| TFRS Tutar | TFRS fiş satırının belirlenen hesap koduna Borç/Alacak olarak işlenecek tutarın girildiği alandır. "KDV" seçeneği işaretlenmiş ve KDV oranı girilmişse, tutar girildikten sonra “KDV kaydı oluşturmak istiyor musunuz?” şeklinde bir onay ekranı görüntülenir. “EVET” seçeneği ile onay verildiğinde, girilen tutardan KDV düşülerek KDV hariç rakam hesaplanır. Böylece, girilen diğer hesap kodunun KDV, Açıklama ve Tutar kısmına KDV tutarı otomatik olarak aktarılır. |
| Açıklama 3 | TFRS fiş satırı açıklamasının istenilen şekilde oluşturulabileceği bölümdür. Açıklama 1 ve 2 alanlarına ek olarak açıklama girilmek istendiğinde kullanılan alandır. Ekranın en altında yer alan Borç Tutarı, Alacak Tutarı, Borç/Alacak Bakiyesi, Borç Miktar, Alacak Miktar, Döviz Borç/Alacak ve Bakiye alanları, program tarafından otomatik olarak hesaplanır. Sağ alt kısımda ise, üzerinde bulunulan satıra ait hesap kodunun, hesap planı kayıtlarındaki hesap ismi ve miktar birimi ile kaydedilen son fiş numarası, bilgi amaçlı izlenir. |
| Belge Türü | E-Defter için belge türü bilgisinin girildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile belge türleri arasından seçim yapılır. |
| Belge No | E-Defter için belge numarası bilgisinin girildiği alandır. |
| Belge Tarihi | E-Defter için belge tarihinin girildiği alandır. |
| **![](../../../../_assets/99dd4001b3755b9521ab.png)**Yeni Fiş | İçinde bulunulan fişten çıkıp yeni fiş giriş ekranına geçilmesi için kullanılan butondur. Kapanmamış, bakiye veren fişlerden çıkılmasını sağlar. Muhasebe → Kayıt → [Muhasebe Parametreleri](<../Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/Muhasebe Modülü Tanımlamaları/Muhasebe Parametreleri - Muhasebe.md>) → Genel → “Fark Veren Fişlerden Çıkılmasın” parametresinin boş bırakılması durumunda, “Bakiyeli fişten çıkışı onaylıyor musunuz?” uyarısı ekrana gelir. Onaylanmadığında, tekrar fiş kaydı ekranına dönülerek işleme devam edilir. “Fark Veren Fişlerden Çıkılsın” parametresi işaretlendiğinde ise, “Bakiyeli fişten çıkamazsınız!” uyarısı ekrana gelir ve fiş kapatılmadan ekranın kapatılmasına izin verilmez. Fişlere ekleme, düzeltme ve iptal işlemi yapılacağı zaman aynı bölüme giriş yapılarak yine aynı fiş üzerinden gerekli değişiklikler yapılır. Fişlerin tarih ve numara değişiklikleri ise sadece Muhasebe → İşlemler → "[Hızlı Bilgi Değişikliği](<../İşlemler - Muhasebe/Hızlı Bilgi Değişikliği/index.md>)" bölümünden yapılır. |
| ![](../../../../_assets/f9a9808be94bfdaaa5f9.png) Muhasebe Tarihçe İzleme | Muhasebe hesap koduna ait tüm bilgilerin izlenmesi için kullanılan butondur. |
| ![](../../../../_assets/ebcd5e24044faae7268b.png) Araya Satır Ekleme | Butona tıklanması ile birlikte “Sıra Okuma” ekranı görüntülenir. Araya eklenmesi istenen satırın hangi sırada oluşması isteniyorsa, eklenecek sıra numarası girilir. ![](../../../../_assets/1d4d9356abb1b8b61bfd.png) |
| ![](../../../../_assets/7d94394aa880ccdd1068.png) Son Satır Kopyalama | "TFRS Fiş Girişi" ekranında listelenen kayıtların içinde, en altta bulunan satırı kopyalamak için kullanılan butondur. Butona tıklandığında, girilen son kayıt ekranın üst kısmına kopyalanır. \<tab\> tuşu ile ilerleyerek bu bilgilerin ayrı bir satırda kaydedilmesi sağlanır. |
| ![](../../../../_assets/9a12c3a43eff8c27cc29.png) Bakiye Kapatma | "TFRS Fiş Girişi" ekranında birden fazla borç hareketinin tek bir alacak hareketi ile kapatılması istendiğinde, “Alacak” hareketinin tutarına “Borç” toplamını hesaplayarak getirir. Bu butonun kullanılması, böyle bir durumda hata yapma olasılığını düşürür. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır. TFRS Fiş Girişi kaydının iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
