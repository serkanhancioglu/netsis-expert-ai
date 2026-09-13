---
title: "Netsis 3 Enterprise ile E-İrsaliye Gönderimi"
page_id: "24772495"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Fatura"
  - "Kayıt / Fatura"
  - "E-İrsaliye İşlemleri"
  - "Netsis 3 Enterprise ile E-İrsaliye Gönderimi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Fatura / Kayıt / Fatura / E-İrsaliye İşlemleri / Netsis 3 Enterprise ile E-İrsaliye Gönderimi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTUzYzM5YzQ1LTkzNzgtNDQ5NS1iMGExLWMzY2IyMTRkOTgwNCZsaW5rPWE0N2Y0MWJhLTM0NmEtNGYzNS04YjRjLWQ0YmJhZGJkNDM2MiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=53c39c45-9378-4495-b0a1-c3cb214d9804&link=a47f41ba-346a-4f35-8b4c-d4bbadbd4362&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-3-enterprise-ile-e-irsaliye-gonderimi_28147754_24772495.html"
source_version: "2022-10-24T18:02:22.867+03:00"
source_bytes: 768819
fetched_at: "2026-09-13T04:02:33+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis 3 Enterprise ile E-İrsaliye Gönderimi

e-İrsaliye, Lojistik-Satış Bölümünde, Kayıt/Fatura menüsünün altında yer alır.

e-İrsaliye uygulamasının fatura kayıt menüsünün altında yer alması için öncelikle, Lojistik -Satış → Fatura → E-Fatura İşlemleri → [E-Fatura Parametreleri](<../E-Fatura İşlemleri/e-Fatura Parametreleri.md>) → "E-İrsaliye Kullanılsın" parametresinin işaretlenmesi gerekir.

![](../../../../../_assets/4b806cc75c432c8eba90.png)

e-Fatura uygulamasında olduğu gibi, e-İrsaliye de belge birim kodlarına bağlanır. Yukarıdaki ekranda yer alan "E-İrsaliye belge birim kodlarınızı buradan girebilirsiniz" yazısının üzerine çift tıklandığında ekrana gelen "Çoklu Seri Giriş Ekranı" ile birim kodları girilir.

![](../../../../../_assets/a2706bc946365e93da24.png)

Gelir İdaresinin zorunlu tuttuğu ve aynı zamanda faturalarda da kullanılan üç haneli kodlar, E-İrsaliye uygulamasında da kullanılır. Burada offline olanlar "FYS" ve "GIB" kodlarını kullanırken, online olanlar üç haneli belirledikleri diğer kodları kullanır.

**Örneğin:** E-Fatura için belge birim kodu olarak **"FYS"** kullanan bir mükellef, **"FYS"** dışındaki bir seriden E-Fatura mükellefine satış faturası kesemez. E-İrsaliye için de aynı durum geçerlidir.

"Çoklu Seri Giriş Ekranında" belge birim kodları tanımlandıktan sonra "E-İrsaliye Yanıt Serisi" seçeneği tercih edilen birim kod ile birlikte işaretlenir.

Kontrol sistemi, tek bir birim kod için "E-İrsaliye Yanıt Serisi" seçeneğinin işaretlenmesine izin verir.

**![](../../../../../_assets/8bbea01de60a31b707ae.png)**

E-İrsaliye serisi (EIR) birden fazla tanımlanabilir fakat, E-İrsaliye Yanıt Serisi (EYS) bir tane tanımlanır.

E-İrsaliye uygulaması, program tarafından üç tür işlem için desteklenir. e-İrsaliye uygulamasının desteklendiği işlemler; Satış İrsaliyesi, DAT (Depolar Arası Transfer) ve Ambar Çıkış Fişi.

**Satış İrsaliyesi**

![](../../../../../_assets/7739b241f23dafcd3c63.png)

Satış irsaliyesini E-İrsaliye olarak oluşturmak için, "Üst Bilgiler" ekranında yer alan E-İrsaliye seçeneğinin işaretlenmesi gerekir. E-İrsaliye seçeneği, işlem yapılan carinin E-Fatura mükellefi olması durumunda işaretlenir.

Carinin E-Fatura mükellefi olup olmadığı; Lojistik - Satış → Fatura → Kayıt → E-Fatura İşlemleri → [E-Fatura Cari Güncelleme](<../E-Fatura İşlemleri/E-Fatura Cari Güncelleme.md>) ekranındaki kayıtlı kullanıcılar listesinden veya, Finans → Cari → Kayıt → [Cari Hesap Kayıtları](<../../../../Finans/Cari/Kayıt - Cari/Cari Hesap Kayıtları/index.md>) bölümündeki "Cari Kart 1" sekmesi ekranında yer alan "E-Fatura Mükellefi" bilgisi ile anlaşılır.

![](../../../../../_assets/5ee3aa82c5734e8f2573.png)

![](../../../../../_assets/9c14848c6266bb8e179d.png)

**E-İrsaliye Ek Bilgi Girişi**

Satış İrsaliyesi kaydedilirken "Toplamlar" ekranına sağ klik tuşu ile gelen "E-İrsaliye Ek Bilgi Girişi" seçeneği sayesinde, taşıyıcı bilgileri tanımlanır. "Matbu Bilgileri" seçeneği ile "Matbudan" tipli e-İrsaliye oluşturulması için ilgili seçeneğin işaretlenip, gerekli bilgilerin doldurulması gerekir.

Bu seçenekteki bilgi alanlarına giriş yapılmadan Tamam ![](../../../../../_assets/39d77b8716226638d9ce.jpg) butonuna basılırsa, "Toplu E-İrsaliye Oluşturma" bölümündeki belge için Taslak Oluştur ![](../../../../../_assets/0a7b217912e33a3e059a.jpg) butonuna basıldığında, sistem tarafından "Taşıyıcı bilgileri boş bırakılamaz" uyarısı ekrana gelir ve taslak oluşturulamaz.

**Toplu E-İrsaliye Oluşturma**

Taslaklar E-İrsaliye haline geldikten sonra, "Toplu E-İrsaliye Oluşturma" ekranına kısıt verilerek "E-İrsaliye Belgeleri (Taslak)" sekmesinde listelenir. Belge üzerine çift tıklandığında E-İrsaliye belgesi görüntülenir.

![](../../../../../_assets/b0f713cc65531fba1e9f.png)![](../../../../../_assets/5a563f0dc91d9f36c896.png)

E-İrsaliye belgesinde "ETTN" numarasının yer alması mevzuat gereği zorunlu tutulur. Bu numara program tarafından otomatik olarak oluşturulur. Belge takibinin yapılması aşamasında önem taşır. E-İrsaliye belgesinde yer alan "QR Kodu" ile "ETTN Numarası" devletin sisteminde eşleşir.

Taslak haline gelen belgede düzenleme yapılması istendiğinde ilk olarak Taslak Sil ![](../../../../../_assets/8ffc46090e943510415c.png) butonu ile belge iptal edilir. Daha sonra, belge tekrar düzenlenip taslak haline getirilir (Bu aşama belge düzeltme ile ilgili son aşamadır.) Taslak halindeki belgelerde hiçbir sorun yoksa Gönder ![](../../../../../_assets/204830f023c407035dec.png) butonuna basılır. Böylece doküman, "GIB" e iletilir. Bu aşamadan sonra, belge ile ilgili hiçbir düzeltme işlemi yapılamaz.

Her E-İrsaliye tek zarfta "GIB" e gider.

**Örneğin:** Taslaklar (E-İrsaliye) sekmesinde 10 tane belge varsa, Gönder ![](../../../../../_assets/204830f023c407035dec.png) butonuna basıldığında 10 tane zarf "GIB" e gönderilir.

Hatırlayınız; E-Faturada 10 adet belge için 1 adet zarf "GIB" e gönderiliyordu.

**Zarf olarak "GIB" e gönderilen irsaliyeler:** Zarf olarak "GIB" e gönderilen irsaliyeler, Lojistik - Satış → Fatura → Kayıt → E-İrsaliye İşlemleri → [Giden Kutusu](<Giden Kutusu (E-İrsaliye)/index.md>) bölümünden takip edilir. Zarf bazında ve İrsaliye bazında görüntülenir.

![](../../../../../_assets/cb3d9f87f4f93310bf71.png)![](../../../../../_assets/bef8f9a54baf8d3ce334.png)

Zarf bazında görüntülendiğinde, sistem yanıtları hakkında bilgi alınır. (Şuan için programda yanıt sistemi bulunmamaktadır.) İrsaliye bazında görüntülendiğinde ise, kalem bilgileri hakkında bilgi alınır.

**Zarf olarak "GIB" den gelen irsaliyeler:** Zarf olarak "GIB" den gelen irsaliyeler, Lojistik - Satış → Fatura → Kayıt → E-İrsaliye İşlemleri → [Gelen Kutusu (E-İrsaliye İşlemleri)](<Gelen Kutusu (E-İrsaliye İşlemleri)/index.md>) bölümünden takip edilir. Zarf bazında ve İrsaliye bazında görüntülenir.

![](../../../../../_assets/b0e8c8051d618fcd510a.png)![](../../../../../_assets/e594aa40c30ec1f9fc23.png)

Zarf bazında gelen E-İrsaliye ekranında tarih aralığı kısıtı verilerek, gelen irsaliyeler zarf bazında sorgulanır ve görüntülenir. Yanıt vermek için, irsaliye bazında gelen E-irsaliye ekranı kullanılır. Buradaki listede yer alan E-İrsaliye, üzerinde çift tıklanarak seçildiğinde, sağ klik tuşu ile ekrana gelen uygulama yanıt seçeneklerinden (kabul/red, kalem bazında) biri seçilir. "Kabul/Red" seçeneği tüm ürünleri kabul/reddetmek için, "Kalem Bazında" seçeneği ise, irsaliyedeki kalemlerden bir/birkaç tanesinin kabul/red durumu halinde kullanılır.

![](../../../../../_assets/b24d2d2dfa43b9ff4615.png)

**Kabul/Red yanıt seçeneği işaretlendiğinde**, açıklama bilgisi girilen bir ekran görüntülenir.

![](../../../../../_assets/9b730ded7f799ac57c1b.png)![](../../../../../_assets/9d829b83875997c3c4b9.png)

Buradaki yanıt numarası ve açıklama alanı, program tarafından otomatik olarak ekrana gelir. Tamam ![](../../../../../_assets/39d77b8716226638d9ce.jpg) butonuna basıldığında, karşı tarafa yanıt gider. (Şuan için programda yanıt görüntüleme sistemi bulunmamaktadır.)

**Kalem bazında yanıt seçeneği işaretlendiğinde,** irsaliye yanıt ekranı görüntülenir.

**![](../../../../../_assets/670604854c1d509a5c91.png)**

Bu ekrana, kabul edilmeyen/hasarlı miktar girişi ve teslim alınan miktar bilgisi girişi yapılır ve ![](../../../../../_assets/39d77b8716226638d9ce.jpg) butonu ile işlem sona erer.

İrsaliye için daha önce yanıt verilmişse, sistem yeni bir yanıta izin vermez.

**Dizayn**

Genel → Dizayn Modülü → Kayıt → [Dizayn](<../../../../Genel/Dizayn Modülü/Kayıt - Dizayn/Dizayn.md>) Bölümü girişi ile ekrana gelen "Dizayn Kayıtları" ekranında dizayn tipi "E-İrsaliye Basım" olarak belirlenir.

**![](../../../../../_assets/10d8bbbd2354f6cb6b4e.png)**

Dizayn adı ve açıklama bilgisi de girildikten sonra çift ok ![](../../../../../_assets/839ad027b7dbeba6ec69.png) butonuna basılarak dizayn oluşturulur.
