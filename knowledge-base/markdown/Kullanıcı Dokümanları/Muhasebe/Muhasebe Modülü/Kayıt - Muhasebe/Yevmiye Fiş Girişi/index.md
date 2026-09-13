---
title: "Yevmiye Fiş Girişi"
page_id: "24740387"
product: "netsis-3-enterprise"
depth: 5
is_section: true
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Muhasebe"
  - "Muhasebe Modülü"
  - "Kayıt / Muhasebe"
  - "Yevmiye Fiş Girişi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / Kayıt / Muhasebe / Yevmiye Fiş Girişi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTgwNDc3NmY0LWRkZjItNGFlNS1iZWJhLTQyYjMwNWY5ZDg5YiZsaW5rPTkzMTY2ZDBhLTFlN2EtNDQzZS04Yzc0LTBjNWUyMzk1NmRlYSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=804776f4-ddf2-4ae5-beba-42b305f9d89b&link=93166d0a-1e7a-443e-8c74-0c5e23956dea&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "yevmiye-fis-girisi_34232031_24740387.html"
source_version: "2022-09-27T10:34:56.830+03:00"
source_bytes: 178535
fetched_at: "2026-09-13T04:12:48+00:00"
generator: "netsis-scraper 1.0.0"
---
# Yevmiye Fiş Girişi

Yevmiye Fiş Girişi; Muhasebe Bölümü'nde, "Kayıt/Muhasebe Modülü" menüsünün altında yer alır. Yevmiye Fiş Girişi, günlük işlemlerin muhasebe fiş kayıtları olarak girildiği, önceden girilen fişlerin izlendiği ve fiş düzenlemesi yapıldığı bölümdür. Yevmiye Fiş Girişi bölümündeki kayıtlar muavin, mizan ve kanuni defter dökümlerine aktarılacağı için, girişlerin düzenli ve doğru bilgilerden oluşmasına dikkat edilmesi gerekir.

"Yevmiye Fiş Girişi" ekranı; Fiş Genel Bilgisi ve Fiş Detay sekmelerinden oluşur.

**Fiş Genel Bilgisi**

![](../../../../../_assets/80bf3cba5110eb0a11c6.png)

Yevmiye Fiş Girişi ekranı Fiş Genel Bilgileri sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Yevmiye Fiş Girişi Ekranı |  |
| --- | --- |
| Ay Kodu | Yevmiye fişi oluşturulacak veya önceden girilen yevmiye fişinin düzenleneceği ay kodunun girildiği alandır. Son fiş numarası ve tarihi, kullanıcıya bilgi vermesi amacıyla ilgili ay içinde işlenen fişin numarası ve tarihi olarak ekrana getirilir. Bir aya ait sınırsız sayıda yevmiye fişi kaydedilebilir. Yevmiye fişi içinde ve diğer bölümlerde ay kodunu düzeltme ve değiştirme imkanı yoktur. |
| Son Fiş Numarası | İlgili ay içinde kaydedilen son fiş numarasının izlendiği alandır. Kullanıcı tarafından değişiklik yapılamaz. |
| Son Fiş Tarihi | İlgili ay içinde kaydedilen son fiş tarihinin izlendiği alandır. Kullanıcı tarafından değişiklik yapılamaz. |
| Fiş Numarası | Kaydı yapılacak yevmiye fiş numarasının girildiği alandır. Kayıtlı olan son belge numarasının bir büyüğü, program tarafından otomatik olarak ekrana getirilir. Önceden kaydedilen bir fişi izlemek için, fiş numarasının bu alana girilmesi gerekir. Fiş bilgileri ekrana program tarafından otomatik olarak aktarılır. Son kalan fişe numara aralığı verilip daha büyük bir numaradan devam edilmesi istendiğinde, istenilen aralık verilerek fiş numarası girilir. Geçmiş tarihlere ait belgelerin kayıtları, kalan numara takip edilerek oluşturulur. Daha sonra Muhasebe → İşlemler → "[Tarih Bazında Yeniden Numaralandırma](<http://Tarih Bazında Yeniden Numaralandırma>)" bölümü kullanılarak, fişler tarih sırasına göre numaralandırılabilir. Önceden hiç fiş kaydı yapılmamış ayın başlangıç numarasını belirlerken (bir önceki ayın son fiş numarası henüz belli değilse) 1 numarasından başlatılıp daha sonra yine “Tarih Bazında Yeniden Numaralandırma” bölümü kullanılarak, asıl başlangıç numarasından itibaren fişler numaralandırılabilir. Bu programın çalıştırılmasından sonra, program eski fiş numaralarını "Açıklama-2" alanına aktarır. Programda, şubeli muhasebe mantığına göre, şubelerden girilen fiş numaralarının başına şube numarası girilir. |
| Tarih | Yevmiye fişinin hangi tarihe ait olduğu ve ay kodu daha önceden belirlendiği için, sadece gün bilgisinin girildiği alandır. Daha önce kaydedilen bir yevmiye fişinin tarihi bu ekrandan değiştirilemez. Kaydedilen fiş numarası yazıldıktan sonra, tarih bilgisi ekrana gelir. |
| Yevmiye Madde No | Yevmiye defter basımı yapıldıktan sonra, ilgili fişin madde numarasının program tarafından otomatik aktarıldığı alandır. |
| Düz. Yevmiye Madde No | Enflasyon muhasebesinin kullanıldığı durumlarda işlev kazanan bir alandır. Enflasyon muhasebesi ile ilgili detaylı bilgi; Muhasebe → Ekler → [Ek-1 Enflasyon Muhasebesi](<../../Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/index.md>) bölümünde yer alır. |
| Fiş Tipi | Yevmiye fiş girişi sırasında, fiş tipinin “Kasa Tahsil”, “Kasa Tediye”, “Açılış Fişi”, “Kapanış Fişi” ya da “Mahsup” olarak belirlendiği alandır. Fiş listelerinden tipine göre seçimli döküm alınmasını sağlar. Programı muhasebe ile entegre kullanan kullanıcıların, entegrasyonda Kasa Tahsil/Tediye bölümündeki Fiş Tipi Tahsil/Tediye, Diğer Müşteri/Satıcı, Borç/Alacak ve Dekont kayıtlarının fiş tipi "Mahsup" olarak aktarılır. Ayrıca yıl sonu zamanı muhasebe hesaplarının kapatılması için "Kapanış Fişi" (hesaplar kapatıldıktan sonra Bilanço ve Gelir Tablosu almak için hesap kapatma kayıtlarının, "Kapanış" tipli fişlerde olması gerekir), kapatılan fişlerin sonraki yılda olması gereken bakiyelerinin oluşması için de "Açılış Fişi" kullanılır. |
| Açıklama-1, Açıklama-2, Açıklama-3 | İsteğe bağlı, yevmiye fişine ait genel açıklamaların yazıldığı alanlardır. Muhasebe → İşlemler → "[Tarih Bazında Yeniden Numaralandırma](<../../İşlemler - Muhasebe/Tarih Bazında Yeniden Numaralandırma.md>)" bölümünün çalıştırılmasından sonra, eski fiş numaraları (istenen durumlarda) "Açıklama-2" alanına aktarılır. |
| **![](../../../../../_assets/fd1a13b1e1de342a0793.png)** Fiş İptal | Yevmiye fişinin iptal edilmesi için kullanılan butondur. "Fiş No" alanına iptal edilecek fiş numarası girildikten sonra "Fiş İptal" butonuna basılarak ilgili fiş iptal edilir. |

**Fiş Detay**

![](../../../../../_assets/27053993c41cc049c5c5.png)

Yevmiye Fiş Girişi ekranı Fiş Detay sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Yevmiye Fiş Girişi Ekranı |  |
| --- | --- |
| Fiş No | "Fiş Genel Bilgisi" sekmesinde girilen fiş numarasının izlendiği alandır. |
| Tarih | "Fiş Genel Bilgisi" sekmesinde girilen fiş tarihinin izlendiği alandır. |
| Fiş Tipi | "Fiş Genel Bilgisi" sekmesinde seçilen fiş tipinin izlendiği alandır. |
| Sıra No | Fiş içindeki kayıtların sıra numaralarının izlendiği alandır. Kayıtlar yapıldıkça program tarafından otomatik olarak arttırılır. Kullanıcı tarafından müdahale edilmez. Yevmiye fişinde 32.000 satır girişi yapılabilir. |
| Hesap Kodu | Yevmiye fiş satırının hesap planındaki hesaplardan hangisine ait olduğunun belirlenmesi için kullanılan alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılır. Sadece "Muavin" tipinde tanımlanan hesaplara kayıt yapılabilir. Boş bırakılmaz. Hesap planında şimdiye kadar hiç tanımlaması yapılmamış bir kod girildiğinde, alanın boş bırakılmasına izin verilmez. Hesap planında ilgili hesap tanımlandıktan sonra kayda devam edilir. |
| Borç/Alacak (B/A) | Yevmiye fiş kaydı oluşturulurken belirlenen hesap koduna, tutarın borç olarak mı yoksa alacak olarak mı işleneceği seçilir. |
| Açıklama 1, Açıklama 2 | Yevmiye fiş satırı için açıklama girilen alandır. Çok kullanılan bazı açıklama satırları "Fiş Açıklama Kayıtları" bölümünden tanımlandığında, her seferinde tekrar yazılması yerine rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) kullanılarak ekrana aktarılabilir. Aktarılan açıklama üzerinde değişiklik yapılabilir. |
| Evrak Tarihi | Evrakın kayıt tarihi ile evrak üzerindeki tarihin farklı olduğu durumlarda, evrak gerçek tarihinin girilerek izleme ve raporlama yapılmasını sağlar. Fişte girilen hareketin fiş tarihi bu alana aktarılır. Üzerinde değişiklik yapılabilir. Entegrasyondan aktarılan kayıtlarda da, evrak tarihi ilgili kaydın tarihi olarak bu alana aktarılır. |
| Referans Kodu | Referans kodu girilen bölümde, referans kodlarının girişi ve referans kodlarına isim açıklama tanımlaması yapılır. Bu bölümde girilen kayıtların, yevmiye fişlerinde ve entegre kayıtlarda kullanmak için Muhasebe → Kayıt → Muhasebe Parametreleri → “Fişlerde Referans Kodu Sorulsun” parametresinin işaretli olması gerekir. Yevmiye fiş girişi sırasında, entegrasyon işlemlerinde, dekont, kasa, ambar giriş/çıkış fişi işlemlerinde, alanının yanında yer alan rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile referans kodlarına ulaşılır. "Referans Kodu" alanını kullanan kullanıcılar, referans mizan listesi ve diğer raporlardaki referans aralığı tanımlamaları ile döküm alabilir. |
| Proje Kodu | Yardımcı Programlar → Kayıt → [Şirket/Şube Parametreleri](<../../Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/Genel Tanımlar/Yardımcı Programlar-Şirket-Şube Parametreleri.md>) → “Proje Uygulaması Var” parametresinin işaretlenmesi ile aktif hale gelen alandır. Proje takibi yapılan hesaplarda kullanılır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, proje kodlarına ulaşılır. |
| Miktar | İlgili kayıt için, hesap kodunun ölçü birimi cinsi üzerinden miktar (varsa) girilen alandır. |
| KDV | İlgili kayda ait KDV oranının (varsa) girilmesini sağlamak için işaretlenen alandır. İşaretlendiğinde, KDV oranının girilmesini sağlayan alan aktif hale gelir. |
| Vade Günü | Vade günü değerinin bilgi amaçlı girildiği alandır. |
| Dövizli Mi | Döviz uygulamasını kullanan firmaların kullandığı alandır. Muhasebe → Kayıt → [Muhasebe Parametreleri](<../Muhasebe Parametreleri.md>) → Dövizli Muhasebe → "FAS52" parametresini işaretleyen firmaların hesap planı kayıtlarında döviz bilgileri ekranı görüntülenir. Bu bölümde, her zaman döviz bilgisi girilmesi istenen hesaplar için döviz tipi girilmesi gerekir. Bu durumda, ilgili hesap yevmiye fiş kayıtlarında kullanılırsa mutlaka döviz ekranı görüntülenir ve döviz bilgileri girilir. Bazı muavin hesaplarda ise, yevmiye fiş girişinde her zaman döviz bilgisi girilmesi istenmez fakat bazı durumlarda döviz ekranlarının açılması istenir. Bu durumda, ilgili muavin hesapların hesap planındaki döviz tipi 0 (sıfır) olarak bırakılır ve döviz bilgisi girilecek ise bu seçeneğe tıklandıktan sonra \<tab\> tuşu ile ilerlendiğinde döviz bilgileri ekranı görüntülenir. ![](../../../../../_assets/0512b955ccbffb1652ed.png) |
| Tutar | Yevmiye fiş satırının belirlenen hesap koduna Borç/Alacak olarak işlenecek tutarın girildiği alandır. "KDV" seçeneği işaretlenmiş ve KDV oranı girilmişse, tutar girildikten sonra “KDV kaydı oluşturmak istiyor musunuz?” şeklinde bir onay ekranı görüntülenir. “EVET” seçeneği ile onay verildiğinde, girilen tutardan KDV düşülerek KDV hariç rakam hesaplanır. Böylece, girilen diğer hesap kodunun KDV, Açıklama ve Tutar kısmına KDV tutarı otomatik olarak aktarılır. |
| Firma Döviz Tipi, Firma Döviz Tutarı | Muhasebe → Kayıt → Muhasebe Parametreleri → Dövizli Muhasebe → "FAS52" parametresi işaretlenir ve "Hesap Planı" Kayıtlarında "Döviz Tipi" alanının 0 (sıfır)’dan farklı bir değer alırsa, yevmiye fişine yapılan kayıtlarda döviz bilgileri sorgulanır. Muhasebe → Kayıt → Muhasebe Parametreleri → Dövizli Muhasebe → "FAS52" parametresinin işaretlenir ve "Hesap Planı" kayıtlarında "Döviz Tipi" alanı 0 (sıfır) boş bırakıldığında ise, yine döviz bilgilerinin sorgulandığı bir ekran görüntülenir. Entegrasyondan aktarılan fiş kayıtlarında, kayıt girişi sırasında sorgulanan döviz kuru ve döviz tutarı bu alanlara program tarafından otomatik olarak aktarılır. "Döviz Takibi" bölümünden "Günlük Kur" girilmemişse, ilgili hesabın döviz kuru sorgulanır. Kur bilgisi girilmişse, hesabın hesap planında tanımlanan döviz tipine göre ilgili alana aktarılır. "Döviz Tutarı" alanına tutar girildikten sonra, fişin "Tutar" alanına, hesaplanan Türk Lirası değeri otomatik olarak aktarılır. Program, "Hesap Planı" kayıtlarında, ilgili hesabın döviz bilgilerinin girişinde "Döviz Tipi" alanına 0 (sıfır)’dan farklı bir değer girildiğinde, "Kur" veya "Döviz Tutarı" alanlarından birinin dolu olup-olmadığını kontrol eder. "Döviz Tutarı" boş bırakılırsa, fişin "Tutar" alanına girilen değer "Döviz Tutarı" olarak kabul edilir ve yine döviz kuru ile çarpılarak Türk Lirasına çevrildikten sonra "Tutar" alanına aktarılır. "Hesap Planı" kayıtlarındaki "Döviz Tipi" alanının boş bırakıldığı durumlarda ise, Döviz Bilgileri" ekranının açılması isteğe bağlı olarak döviz tuşu yardımı ile yapılır. "Döviz Bilgileri" ekranında "Kur" alanı boş bırakılarak, sadece döviz bilgileriyle kayıt yapılmasına izin verilir. |
| Düzeltme Tipi, Düzeltilmiş Tutarı | Muhasebe → İşlemler → "[Döviz Çevrim](<../../İşlemler - Muhasebe/Döviz Çevrim.md>)" işlemi çalıştırıldığında, yevmiye fişlerine dövizli olarak girilen kayıtların firma döviz tutarları oluşur. "Yevmiye Fiş Girişi" ekranında bu kayıtların üzerine gelip iki kez tıklandığında, ilgili kaydın firma döviz tipine göre firma döviz tutarı izlenir. |
| Açıklama 3 | Yevmiye fiş satırı açıklamasının istenilen şekilde oluşturulabileceği bölümdür. Açıklama 1 ve 2 alanlarına ek olarak açıklama girilmek istendiğinde kullanılan alandır. Ekranın en altında yer alan Borç Tutarı, Alacak Tutarı, Borç/Alacak Bakiyesi, Borç Miktar, Alacak Miktar, Döviz Borç/Alacak ve Bakiye alanları, program tarafından otomatik olarak hesaplanır. Sağ alt kısımda ise, üzerinde bulunulan satıra ait hesap kodunun, hesap planı kayıtlarındaki hesap ismi ve miktar birimi ile kaydedilen son fiş numarası, bilgi amaçlı izlenir. |
| Belge Türü | E-Defter için belge türü bilgisinin girildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile belge türleri arasından seçim yapılır. |
| Belge No | E-Defter için belge numarası bilgisinin girildiği alandır. |
| Kur | E-Defter için kur bilgisinin girildiği alandır. |
| Döviz Kur Tarihi | E-Defter için döviz kur tarihinin girildiği alandır. |
| Belge Tarihi | E-Defter için belge tarihinin girildiği alandır. |
| Döviz Kuru Bilgisi | E-Defter için döviz kuru bilgisinin girildiği alandır. |
| Uluslararası Para Birimi | Yevmiye fişinin dövizli olması halinde, döviz eşleştirmede tanımlanan para biriminin otomatik aktarıldığı alandır. Üzerinde değişiklik yapılamaz. |
| Döviz Kuru Açıklama Bilgisi | E-Defter için girilen kur tarihi ve kur bilgisi bilgilerinden oluşan açıklama bilgisinin otomatik olarak getirildiği alandır. Üzerinde değişiklik yapılamaz. |
| Ödeme Türü | E-Defter için ödeme türü bilgisi girilen alandır. |
| **![](../../../../../_assets/99dd4001b3755b9521ab.png)**Yeni Fiş | İçinde bulunulan fişten çıkıp yeni fiş giriş ekranına geçilmesi için kullanılan butondur. Yeni Fiş butonu, kapanmamış, bakiye veren fişlerden çıkılmasını sağlar. Muhasebe → Kayıt → Muhasebe Parametreleri → Genel → “Fark Veren Fişlerden Çıkılmasın” parametresinin boş bırakılması durumunda, “Bakiyeli fişten çıkışı onaylıyor musunuz?” uyarısı ekrana gelir. Onaylanmadığında, tekrar fiş kaydı ekranına dönülerek işleme devam edilir. “Fark Veren Fişlerden Çıkılsın” parametresi işaretlendiğinde ise, “Bakiyeli fişten çıkamazsınız!” uyarısı ekrana gelir ve fiş kapatılmadan ekranın kapatılmasına izin verilmez. Fişlere ekleme, düzeltme ve iptal işlemi yapılacağı zaman aynı bölüme giriş yapılarak yine aynı fiş üzerinden gerekli değişiklikler yapılır. Fişlerin tarih ve numara değişiklikleri ise sadece Muhasebe → İşlemler → "[Hızlı Bilgi Değişikliği](<../../İşlemler - Muhasebe/Hızlı Bilgi Değişikliği/index.md>)" bölümünden yapılır. |
| ![](../../../../../_assets/f9a9808be94bfdaaa5f9.png) Muhasebe Tarihçe İzleme | Muhasebe hesap koduna ait tüm bilgilerin izlenmesi için kullanılan butondur. |
| ![](../../../../../_assets/ebcd5e24044faae7268b.png) Araya Satır Ekleme | Araya Satır Ekleme butonuna tıklanması ile birlikte “Sıra Okuma” ekranı görüntülenir. Araya eklenmesi istenen satırın hangi sırada oluşması isteniyorsa, eklenecek sıra numarası girilir. ![](../../../../../_assets/1d4d9356abb1b8b61bfd.png) |
| ![](../../../../../_assets/7d94394aa880ccdd1068.png) Son Satır Kopyalama | "Yevmiye Fiş Girişi" ekranında listelenen kayıtların içinde, en altta bulunan satırı kopyalamak için kullanılan butondur. Son Satır Kopyalama butonuna tıklandığında, girilen son kayıt ekranın üst kısmına kopyalanır. \<tab\> tuşu ile ilerleyerek bu bilgilerin ayrı bir satırda kaydedilmesi sağlanır. |
| ![](../../../../../_assets/9a12c3a43eff8c27cc29.png) Bakiye Kapatma | "Yevmiye Fiş Girişi" ekranında birden fazla borç hareketinin tek bir alacak hareketi ile kapatılması istendiğinde, “Alacak” hareketinin tutarına “Borç” toplamını hesaplayarak getirir. Bu butonun kullanılması, böyle bir durumda hata yapma olasılığını düşürür. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır. Yevmiye Fiş Girişi kaydının iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
