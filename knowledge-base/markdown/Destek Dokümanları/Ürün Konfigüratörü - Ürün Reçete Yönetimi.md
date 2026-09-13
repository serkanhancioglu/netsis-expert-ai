---
title: "Ürün Konfigüratörü - Ürün Reçete Yönetimi"
page_id: "50680146"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Ürün Konfigüratörü - Ürün Reçete Yönetimi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Ürün Konfigüratörü - Ürün Reçete Yönetimi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTVlZjNjNTk3LTBiYTYtNDJkNi04YmNiLTM0NjliNzk1ODNhYyZsaW5rPTk4YmIzMWM2LTg5ZWItNDVmOS05NWViLTBiNTQ0OTY3NjNlZiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=5ef3c597-0ba6-42d6-8bcb-3469b79583ac&link=98bb31c6-89eb-45f9-95eb-0b54496763ef&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "urun-konfiguratoru-urun-recete-yonetimi_82576590_50680146.html"
source_version: "2022-11-03T09:49:45.047+03:00"
source_bytes: 876642
fetched_at: "2026-09-13T04:26:14+00:00"
generator: "netsis-scraper 1.0.0"
---
# Ürün Konfigüratörü - Ürün Reçete Yönetimi

Ürün Konfigüratörü-Ürün Reçete Yönetimi ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

|  |  |
| --- | --- |
| **Amaç ve** **Fayda** | Yeni Ürün Konfigüratörü ekranları ile sıfırdan bir ürün ağacı oluşturmak veya mevcut bir ürün ağacını değiştirerek yeni ürünler türetmek, görsel işlemler kullanılarak pratik ve hızlı bir şekilde yapılabilir. Bu işlemler mevcut Reçete Kaydı ekranı ile paralel yürütülür. Ayrıca satış sürecinde müşteriden teklif alınırken henüz kaydedilmemiş yani taslak halindeki yeni ürünler de kullanılabilir. Taslak ürünler bir onay sürecinden geçirilerek onaylanabilir. Ürün ağacında yapılacak tüm işlemlerin kontrollü olması için konfigürasyon kuralları tanımlanır ve ürün ağacında yapılan bileşen değişikliklerin bu kurallara uygun olup olmadığı kontrol edilerek ürün reçete yönetim sürecinin denetlenmesi sağlanır. |
| **Ürün** **Grubu** | \[X\] Redcode Enterprise<br>\[X\] Redcode Standart |
| **Modül** | \[X\] Teklif<br>\[X\] Üretim |
| **Yükleme** **Sonrası** **İşlemler** | \[X\] DBUPDATE Programının Çalıştırılması |
| **Modül** | \[X\] Yeni Fonksiyon |
| **Versiyon** **Önkoşulu** | 5.0.10 |

Yeni Ürün Konfigüratörü ekranları ile sıfırdan bir ürün ağacı tasarlamak veya mevcut bir ürün ağacı üzerinde değişiklikler yaparak yeni ürünler türetmek, ekranda yer alan görsel işlemler kullanılarak pratik ve hızlı bir şekilde yapılabilir. Bu işlemler mevcut Reçete Kaydı ekranı ile paralel yürütülür, yani her iki yerden de ürün ağacını güncellemek ve görüntülemek mümkündür.
Ayrıca satış sürecinde müşteriden teklif alınırken henüz kaydedilmemiş yani taslak halindeki yeni ürünler de kullanılabilir hale getirilmiştir. Taslak ürünler bir onay sürecinden geçirilerek onaylanabilir.
Ürün ağacında yapılacak tüm bileşen değişiklik işlemlerinin kontrollü olması için konfigürasyon kuralları tanımlanır ve ürün ağacında yapılan değişikliklerin bu kurallara uygun olup olmadığı kontrol edilerek ürün reçete yönetim sürecinin denetlenmesi sağlanır.

#### Ürün Konfigüratörü

Ürün konfigüratörü ekranı kullanıcıların sıfırdan yeni bir ürünü yaratabildikleri veya var olan bir ürün üzerinde değişiklik yapabildikleri, taslak ürünler oluşturup onaya gönderdikleri ve taslakları onaylayabildikleri veya reddettikleri yerdir. Mevcut durumda ürün tanımının yapıldığı reçete uygulamasına göre daha fazla görsel unsurların kullanılması nedeniyle daha hızlı ve pratik şekilde ürün reçete değişikliği yapmak, ayrıca ürün değişikliklerindeki kontrol sürecini yürütmek mümkündür.

Bu ekran Reçete Kaydı ekranı ile paralel çalışmaktadır, yani iki tarafta da ürün ağacı üzerinde değişiklik yapılabilmektedir. Bir diğer yenilik de ürün konfigüratörünün satış süreci ile bağlantılı çalıştırılabilmesidir. Ürün konfigüratörü uygulamasından önce satış teklifi sadece tanımlı bir stok kodu seçilerek oluşturulabilmekteydi. Bu düzenleme ile stok kodu olmayan mamullerin kullanıcı tarafından taslak halinde iken de teklife eklenebilmesi sağlanmıştır. Bu işlem için **Talep/Teklif** modülünde **Satış Teklif** ekranında teklif kaydı oluşturulurken, **Kalem Bilgileri** sekmesinde **Kod** alanına Stok Kodu girmek yerine, bu alandayken sağ tıkla açılan menüden **Ürün** **Konfigüratörü** penceresine ulaşılabilir.
Bu ekrana doğrudan **Üretim** modülündeki **Kayıt** menüsünden de ulaşılabilir. Ürün konfigüratörü ekranının açılışında, ekranın kullanılma yöntemi için iki seçenek mevcuttur; ya "Baz Mamul Aç" işlemi ile bir mamul seçilerek üzerinde değişiklik
yapılacaktır, ya da "Yeni Konfigürasyon" denerek boş bir ürün ağacı üzerinde yeni bir ürün yaratılacaktır. Her iki durumda da yapılacak değişiklikler için sistem tarafından sıra numarası verilir ve bu numara Taslak Kodu olarak kaydedilir. Daha önceden kaydedilmiş bir taslak, kodu girilerek çağrılabilir veya taslak rehberinden kayıt seçilebilir.

![](../_assets/ca4c253b6593560b6b48.png)**Şekil** **6** Ürün Konfigüratörü Ekranı

#### Ürün Ağacı (Sol Panel)

Ürün Konfigüratörü ekranında üzerinde çalışılan ürün ağacı sol panelde gösterilecektir. Bu kısmın üzerinde ürün ağacı üzerinde yapılabilecek işlemlere ait ikonların sıralandığı görsel bir menü yer alır. Bu menüdeki ikonlar ve temsil ettikleri işlemler şöyledir:

![](../_assets/8696c06bda528cc68b2f.png)Baz Mamul Aç: Konfigürasyon işleminde baz olarak bir mamul veya yarımamul kullanılmak isteniyorsa bu işlem ile mamul ve yarımamul rehberi açılabilir. Açılan mamul rehberi ürün grubu detayı ile listeleme yapmaktadır.

![](../_assets/f8e855ae59202d732eff.png)Yeni Konfigürasyon: Sıfırdan ürün tasarımı yapılmak isteniyor ise bu işlem ile yeni ürün tasarlama moduna geçilebilir. Ürün Konfigürasyon Onaylama yetkisine sahip kullanıcılara açık bir işlemdir. Ürün Konfigüratörü ekranı ilk "Yeni Konfigürasyon" modunda açılmaktadır.
Not: Ürün konfigüratörü onaylama yetkisi olmayan kullanıcılar, sadece baz mamulden yola çıkarak ve sadece değişebileceği tanımlanan bileşenler üzerinde değişiklik yaparak yeni bir ürün elde edebileceklerdir. (Konfigüratör Yetkileri bölümüne bakınız).

![](../_assets/55296c045dd5af3e0762.png)Tüm Seviyeleri Göster: Ürün ağacının tüm seviyeleri açılarak görülmek isteniyorsa bu işlem kullanılabilir.

![](../_assets/b7762659eadae80b0365.png)Tüm Seviyeleri Sakla: Ürün ağacının sadece ilk seviyesi görmek isteniyor ise bu işlem kullanılabilir.

![](../_assets/90e04a278c69650d733b.png) Seçili Mamul/Yarımamul Altına Bileşen Ekle: Ürün ağacındaki ilk seviyeye ya da alt seviyelerdeki yarı mamullere bileşen eklemek için kullanılabilir. F8 tuş yardımı ile hızlı bileşen ekleme işlemi yapılabilir.

![](../_assets/d65689ec2ff8a746fec5.png) Seçili Bileşeni Sil: Ürün ağacındaki herhangi bir bileşenin silinmesi isteniyor ise kullanılabilir. Yarımamul silme durumunda, yarımamul altındaki tüm bileşenler de ürün ağacından silinir. F7 tuş yardımı ile hızlı silme işlemi yapılabilir.

![](../_assets/cd1ffa5d4f81b34ab684.png) Seçili Bileşeni Kopyala: "Bilgi Amaçlı" olarak işaretlenen bileşenlerde aktif duruma gelen işlemdir. Seçili bilgi amaçlı bileşenden bir tane daha ürün ağacına eklemeyi sağlar.

Not: Bileşen ekleme ve silme gibi işlemler, ürün ağacında yeni bir mamul/yarı mamul oluşmasına sebep olacaktır.

Oluşan yarı mamul/mamul için aşağıdakiler yapılabilir:

- Yeni bir kod verilerek yeni bir stok kartı açılabilir
- Daha önceden tanımlı böyle bir yarı mamul/mamul var olup olmadığına bakılarak, varsa mevcut tanımlı yarı mamul/mamul kullanılabilir. (Reçete kontrol işlemine bakınız).
- Tanımlı bir yarı mamul/mamul altında yapılan değişiklikler ile, ilgili reçete güncellenebilir.

![](../_assets/4f8df1a3588a6ed1db57.png) Seçili Bileşeni Güncelle: Bileşen ekleme, silme gibi işlemler sonucunda Ürün Konfigüratörünün yarattığı "yeni mamul/yarı mamul" yerine, yapılan düzenlemelerin mamul/yarı mamul reçetesini güncelleyecek şekilde
davranılması isteniyor ise, bu davranışın uygulanması istenilen mamullerde "Seçili Bileşeni Güncelle" işlemi çalıştırılmalıdır.

![](../_assets/d61f0751570d41d962ba.png) Değiştirilebilir/Değiştirilemez: Konfigürasyonda değiştirilmemesi istenen bileşenleri işaretlemek için kullanılır. Satış ekibinin, ürün tasarım ekibine, müşterinin önemle üzerinde durduğu ve değiştirilmemesini istediği parça olduğunu iletmesi olarak düşünülebilir.

![](../_assets/c6805c728b7125993c6e.png)Yeni Malzeme Talebi: Seçili bileşenin içinde bulunduğu malzeme grubunda, ihtiyacı karşılayan nitelikte bir ikame bulunmuyorsa, mevcut malzemelerden daha farklı bir malzeme talebinde bulunulabilir. (Tüm onaylardan sonra yeni bir stok kodu olarak yaratılacaktır). Ancak yeni malzeme talebinin yapılabilmesi için, öncelikle mevcut bir malzeme ürün ağacında bulunmalı ya da eklenmiş olmalıdır. Ve ancak bu malzemenin içinde bulunduğu gruba ait yeni bir malzeme talep edilebilmektedir. (Malzeme grup tanımlama bölümüne bakınız).

![](../_assets/d88e9a4b75729108e247.png)Bileşenlerden Yarımamul Yap: Aynı seviyedeki bileşenlerin bir bölümü ya da tümü kullanılarak yeni bir yarımamul oluşturmak isteniyor ise kullanılabilir.

![](../_assets/9914c698e0a5014d47cb.png)Bileşenleri Dışarı Çıkart: Yarımamul altındaki bileşenlerin yarımamul altında kalmayıp bir üst seviyeye çıkarılması isteniyor ise bu işlem kullanılabilir.

Yarımamule bağlı tüm bileşenler bir üst seviyeye eklenecektir.

![](../_assets/0b3db3396f5e78c29f3b.png) Açıklamalar: Ürün Konfigüratörü uygulaması taslağa ait sınırsız sayıda açıklama girilmesini mümkün kılmaktadır. Bu sayede, satış ve ürün tasarım

ekipleri arasındaki mesaj trafiği de yönetilebilir olmaktadır. Taslağa ait açıklama girmek ya da mevcut açıklamaları listelemek için bu işlem kullanılabilir.

![](../_assets/5cb772b2127f02dc65a4.png) Bağlantılı Belgeler: Satış ekipleri, satış teklifi aşamasında Ürün Konfigüratörü ile taslak oluşturup, bu taslağı ürün tasarım ekibine onay için gönderebilirler. Ürün tasarım ekibinde benzer taslaklardan çok sayıda
oluşmasını engellemek için, çok sayıda satış teklif belgesini aynı taslağa bağlamak mümkündür. Taslağa bağlı bağlantılı belgeleri listelemek için bu işlem kullanılabilir.

![](../_assets/e934da0879823e7446cf.png) Otomatik Reçete Kontrol Ayarları: Ürün ağacındaki mamullerde herhangi bir düzenleme (bileşen ekleme, silme gibi) yapıldığında, Ürün Konfigüratör uygulaması, yeni bir yarı mamul/mamul oluşturacak şekilde davranır. Reçete Kontrol işlemi ile, ürün ağacının güncel haliyle sistemde kayıtlı ürün ağaçlarında arama yapılıp, benzer ürün ağaçları bulunuyor ise tekrar yeni bir mamul kaydı veya kayıtları atılmaması sağlanır. Reçete kontrol işleminin belirli noktalarda otomatik çalıştırılması isteniyor ise bu işlem kullanılabilir. Ürün ağacının görüntülendiği panelin sağ alt köşesinde, üzerine imleç geldiği zaman görünen bilgilendirme paneli yer alır. Ürün ağacının rahat okunabilmesini ve
izlenmesini sağlamak için, bileşenlerin durumunu özetlemekte olan ikonların ve renklerin bilgilendirmesini yapması için tasarlanmıştır. Farenin imleci ile bilgilendirme kutucuğu ikonu üstüne gelindiğinde panel içeriği görüntülenmektedir, fare kutucuk üzerinden alındığında bilgilendirme paneli gizlenmektedir.
![](../_assets/7ebc293ff1d046b2ff93.png)**Şekil** **7** Bilgilendirme Paneli

#### Sekmeler (Sağ Panel)

Ekranın sağ kısmında ise, ürün ağacında seçili bileşenin özelliğine göre farklı sekmeler yer alır:

**Malzeme** **Seçimi:** Mevcut bileşen için tanımlanmış bir Malzeme Grubu var ise bu sekme görünecektir. Burada seçili bileşen yerine, aynı ikame malzeme grubunda yer alan diğer bileşenler, özellik ve değer bilgileri ile birlikte gösterilir. Böylece kullanıcı ürün ağacındaki bileşenin alternatiflerini hızlıca görüntüleyecek ve isterse farklı bir bileşeni seçebilecektir. (İkame malzeme grupları tanımlama bölümüne bakınız). Alternatif olarak kullanılacak bileşen bulunamadıysa "Yeni Malzeme Ekle" denerek yeni bir bileşen de tanımlanabilir. Malzeme Seçimi sekmesinde "Filtreyi Kaldır" tuşunun sağında yer alan kısımda stok kodu veya stok adına göre arama yapılarak ikame malzemelerin buna göre listelenmesi sağlanabilir.

**Bileşen** **Bilgileri:** Ürün ağacındaki tüm bileşenler için reçete bilgileri bu sekmede gösterilir. Burada tüm alanlar ve bilgiler Reçete Kaydı ekranındaki "Reçete Bilgileri 1" ve "Reçete Bilgileri 2" sekmelerinde yer alan bilgilerle aynıdır.

**Reçete Üst Bilgileri:** Reçete kaydı ekranında en üst kısımda yer alan bilgiler de bu sekmede gösterilir.

**Yeni Malzeme/Yarı** **Mamul** **Bilgileri**: Reçeteye yeni kaydedilecek malzeme ve yarı mamuller için oluşturulan sekmedir. Kullanıcı burada stok kodu, ismi vb. bilgileri belirleyebilir.

#### Taslak Onay Süreci

Yeni bir ürün için veya bir ürün değişikliği için oluşturulan taslak kaydı üzerinde gerçekleştirilen onay işlemleri şöyledir:

**Ön Onaya Gönder:** Konfigüratör Parametrelerinde "Ön Onay Sistemi" "Evet" olarak işaretli ise görünecektir. Eğer oluşturulan taslak, kayıtlarda mevcut bir ürün ağacı ile eşleşiyorsa bu kayıt ön onaya gönder denildiğinde, onaya gönderilmeyecek ve bulunan stok kodu teklif kaydına eklenecektir. Onaya gönderme işlemi sırasında parametrelerde tanımlı kullanıcılara e-posta gönderilecektir. Kullanıcı ön onaya gönderdiği bir taslak üzerinde değişiklik yapamaz.

**Onaya Gönder:** Eğer oluşturulan taslak, kayıtlarda mevcut bir ürün ağacı ile eşleşiyorsa bu kayıt için onaya gönder denildiğinde, onaya gönderilmeyecek ve bulunan stok kodu teklif kaydına eklenecektir. Onaya gönderme işlemi sırasında parametrelerde tanımlı kullanıcılara e-posta gönderilecektir. Ön Onay sistemi

çalışsın diye işaretlenmişse, sadece "Ön Onay Kabul" durumundaki taslaklar onaya gönderilebilecektir. Kullanıcı onaya gönderdiği bir taslak üzerinde değişiklik yapamaz.

**Onayla:** Yetkisi olan kullanıcı kendisine ön onaya veya onaya gönderilmiş taslakları (durumları Ön Onayda veya Onay Bekleniyor olanlar) açtığında

Onayla ve Reddet tuşları aktif olacaktır. Ön Onayda durumunda iken kullanıcı taslak üzerinde herhangi bir değişiklik yapamayacaktır. Onay bekleniyor durumunda yeni bileşenler için stok kaydı oluşturulabilir ve ürün ağacı
güncellenebilir.

**Reddet:** Onaya veya ön onaya gönderilen taslaklar kullanıcı tarafından reddedilebilir.

Onay sürecindeki aşamalara göre taslağın görüntülenecek onay durumları aşağıdaki gibidir:

**Beklemede:** Henüz bir işlem yapılmamış ve taslak kodu almamış taslak kaydını ifade eder.

**Hazırlandı:** Taslak sadece kaydedildi ise taslak kodu verilerek bu statüde saklanacaktır. Bu durumdaki taslak tekrar güncellenip kaydedilebilir, onaya gönderilebilir veya silinebilir.

**Ön Onayda:** Yetkili kullanıcı bu durumdaki bir taslağı onaylayabilir (Durum: Ön Onay Kabul) veya reddedebilir (Durum: Ön Onay Red). Ön Onayda durumundaki taslaklar üzerinde değişiklik, silme işlemleri yapılamaz. Bunlar sadece "Belgede Kullan" denerek teklife eklenebilir veya Reçete Kontrol ile ekran üzerinde yapılacak değişikliklerin reçeteye etkisi izlenebilir.

**Ön Onay Kabul:** Kullanıcı bu taslağı isterse onaya gönderir (Durum: Onay Bekleniyor) veya gerek kalmadıysa silebilir.

**Ön Onay Red:** Kullanıcı bu taslakla ilgili işlem yapamayacaktır, kayıt temizliği açısından silmesi uygundur.

**Onay Bekleniyor:** Yetkili kullanıcı bu durumdaki bir taslağı onaylayabilir (Durum: Onaylandı) veya reddedebilir (Durum: Reddedildi)

**Onaylandı:** Onaylanmış taslaklar için yeni stok kodu verilmiştir. Artık taslak kodu yerine bu stok kodunun kullanılması yeterlidir. Teklif kayıtlarını güncellemek için, ilgili teklif satırında "Konfigürasyon Kodu Değiştirme" işlemi yapılarak taslak kodu yerine stok kodunun yazılarak kaydedilmesi sağlanmalıdır.

**Reddedildi:** Reddedilmiş taslak kayıtları üzerinde herhangi bir işlem yapılamaz.

#### Diğer Konfigüratör İşlemleri

Onaylama sürecinin dışında da taslak kayıtları üzerinde bir takım işlemler yapılabilir. Bu işlemler ekranın sağ alt köşesindeki tuşlar aracılığı ile gerçekleştirilebilmektedir.

**Reçete** **Kontrol:** Kullanıcının reçete yani ürün ağacı üzerinde yaptığı değişiklikleri dikkate alarak mevcut kayıtlarda bununla eşleşen bir ürün ağacı var mı diye kontrol edilir, bulunursa sol alt satırda bulunan baz mamül stok kodu gösterilir, bulunamazsa "Konfigürasyona ait baz mamul bulunamadı" mesajı gösterilir.

Ürün ağacı işlemleri menüsündeki "Otomatik Reçete Kontrol Ayarları" seçeneği ile reçete kontrol işleminin çalışması istenen durumlar aşağıdaki seçenekler arasından tanımlanabilmektedir:

**Belgede Kullan:** Ürün Konfigüratöründe seçilen taslak bu tuş ile teklife eklenir. Stok kaydı üzerinde değişiklik yapıldı ve reçete kontrol sonucunda yeni ürün için bir stok kaydı ile eşleştirme yapılamadı ise bu tuş aktif olmayacaktır, kayıt

onaya gönderilince teklif kaydına dönülür ve taslak teklife eklenmiş olur. Tanımlı bir stok kaydı bulundu ise bu kayıt Belgede Kullan tuşu ile teklife eklenebilecektir.

**Taslak Kaydet:** Ürün konfigüratöründe, baz mamul çağrılarak kayıt üzerinde değişiklik yapıldıktan sonra, taslak hemen onaya gönderilmeyecekse Taslak Kaydet tuşu ile kaydedilebilir ve sonra kullanıcı bu taslağı seçerek çalışmasına devam edebilir.

**Taslak** **Sil:** Kullanıcının kaydettiği ama onaya göndermediği, veya onaya gönderdiği ancak onayı reddedilen taslaklar silinebilir.

#### Ürün Konfigüratörü Tanımları

Konfigüratör tanım ekranları aşağıdaki gibidir:

- Ürün Grubu Tanımlama.
- Konfigüratör Tanımlamaları.
- İkame Malzeme Grubu Tanımlama.
- Özellik-Değer Tanımlama.
- Yarımamul ve Hammadde Stok Bağlantı Tanımlama.
- Kural Tanımlama.
- Konfigüratör Parametreleri.

Yeni ürün ağacı oluşturma veya ürün ağacı görüntüleme işlemleri ile ürün taslaklarının onay işlemleri ise yine **Üretim** modülündeki **Kayıt** menüsünde "Ürün Konfigüratörü" ekranında yapılmaktadır.
Ürün Konfigüratörü ile ilgili önemli notlar:

- Ürün Konfigüratörü uygulaması güncel sürümünde, içinde operasyon geçen ürün ağaçlarının konfigürasyonu desteklenmemektedir. Operasyon desteği gelecek iş planlarımız içinde bulunmaktadır.
- Ürün Konfigüratörü uygulaması yapısı gereği esnek yapılandırmalı sistemler ile entegre çalışmamaktadır. Esnek yapılandırmalı ürünlerin konfigürasyonu Ürün Konfigüratörü uygulamasında ileri sürümlerde desteklenecektir.

#### Ürün Grubu Tanımlama Ekranı

Ürün Grupları, konfigürasyon aşamasında, mevcut bir üründen yola çıkarak yeni bir ürünün konfigüre edilmesi istendiği durumda, baz alınacak mamulleri sınıflandırmak ve üzerinde değişiklik yapılabilecek bileşen gruplarını kontrol etmek amacı ile kullanılır. Böylece ürün ağacı değişiklikleri daha az sayıda veri üzerinden kontrollü bir şekilde yapılmış olur. Ürün Grubu Tanımlama ekranına **Üretim** modülü **Kayıt** menüsünden ulaşılır. Grup Kodu ve Grup Açıklaması girilerek tanımlama yapılır. Bu ekrandan bir ürün grubu seçilerek "Ürün Grubu Mamul Eşleştirme" sekmesine geçilerek istenen stok kodları seçili ürün grubuna atanır. Örneğin bir Beyaz Eşya üreticisi için Ürün Grupları; "Buzdolabı", "Çamaşır Makinesi", "Bulaşık Makinesi" ve "Kurutma Makinesi" olacaktır. Bu ürün grupları ilgili mamullerin stok kodları ile eşleştirildiğinde, kullanıcılar "Buzdolabı" grubunda kaç mamul olduğunu (Örneğin şu stoklar "BZD001-2 Kapılı No-Frost", "BZD002-Tek Kapılı No-Frost", "BZD003-3 Kapılı No-Frost" gibi) görebilecek, yeni bir Buzdolabı konfigürasyonu hazırlanacaksa bu stok kodlarından birini seçerek devam edecektir. Yeni ürün "Tek Kapılı Derin Donduruculu" Buzdolabı ise "BZD002-Tek Kapılı No-Frost" stok kaydını baz mamul olarak seçerek konfigürasyona başlandığında en az sayıda değişiklik yapılarak yeni ürün tasarımına ulaşılabilir. Seçilen ürün grubuna atanacak stok kodlarını listelerken, erkanın üst kısmında yer alan çeşitli filtreler uygulanabileceği gibi, "Listeye İleri Kısıt Uygulansın" denerek daha detaylı sorgulamalar da yapılabilmektedir. Listelenen stok kodları daha sonra topluca veya satır bazında işaretlenerek eşleştirme yapılabilir. Değişiklikler kaydedildiğinde yapılan eşleştirmeler veya iptal edilen eşleştirmeler saklanacaktır.
![](../_assets/f1459a389ed7583ce176.png)Ürün Grubu Mamul Eşleştirme Ekranı

#### İkame Malzeme Grubu Tanımlama Ekranı

Konfigürasyon sırasında güncellenecek üründe mevcut bir bileşen yerine ihtiyaç doğrultusunda farklı olarak kullanılabilecek bileşenlerin gruplanması amacı ile "İkame Malzeme Grubu" tanımlaması yapılabilmektedir. Böylelikle, değişiklik yapacak kişinin, sadece tanımlı malzemeler içinden seçim yapması sağlanabilir.
Örneğin, Beyaz Eşya üreticisi Buzdolabı ürünlerinde 3 farklı elektrik motoru kullanıyor olsun. Konfigürasyon sırasında bu farklı stok kodlarından birinin buzdolabı için elektrik üretme amacıyla kullanılabileceğini tanımlamak için öncelikle bu ekranda "Elektrikli Motor" diye bir ikame malzeme grubu tanımlanmalıdır.
İlgili ekrana **Üretim** modülünde **Kayıt** menüsünde **Konfigüratör Tanımlamaları** alt menüsünden ulaşılır. Grup Kodu ve Grup Açıklaması girilerek tanımlama yapılır.

**"Bilgi** **Amaçlı":** Bu şekilde işaretlenen ikame malzeme grubundaki stok kayıtları ürün ağacında yer almaz ancak konfigürasyon taslağında görünecektir. Bu kayıtların stok takibi yapılmaz, işemrine bağlı reçetelere de kaydedilmez,
sadece iş emri basınlarında bilgi amaçlı yer alır.

**"Bağlantılı Ürün Seçimi": "**Bilgi Amaçlı" işaretlendi ise hangi ürün grupları için bu şekilde çalışacağı seçilmelidir.
![](../_assets/61a84604d514c877321b.png)**Şekil** **2** İkame Malzeme Grubu Tanımlama Ekranı

#### Özellik - Değer Tanımlama Ekranı

Bir ikame malzeme grubunda benzer özellikte stok kayıtları gruplanır. Bu stok kayıtlarının hangi yönlerinin ayırıcı olduğunu Özellik ve Değer atayarak tanımlayabiliriz. Öncelikle özellikler, "Özellik Kodu" ve "Özellik Açıklaması" ile tanımlanır. Sonra bu özelliğin alabileceği değerler diğer sekmede, "Değer Kodu" ve "Değer Açıklaması" girilerek tanımlanır. Örneğin, bir kullanım kılavuzu için ayırıcı özellik "Lisan" olacaktır. Hangi lisanlarda kılavuzların olacağı (Türkçe, İngilizce gibi) değer olarak tanımlanır. Yetkili kullanıcılar, konfigürasyon esnasında yeni bir stok kaydı açarken, gerekiyorsa mevcut bir özelliğe yeni bir değer atayabilirler.
Not: Buradaki özellik ve özellik değerleri tanımları, esnek yapılandırma uygulaması ile benzeşmektedir. Esnek yapılandırma uygulaması destekleneceği zaman ve bu uygulamamızı kullanan müşterilerimizde, buradaki özellik tanımlamaları yerine esnek yapılandırma uygulamasındakiler kullanılacaktır.
Buradaki tanımlar ise, esnek yapılandırma kullanılmadığı durumda geçerlidir. Bu uygulamada, esnek yapılandırmadan farklı olarak, farklı özellik değeri taşıyan malzemeler, ayrı birer stok kodu olarak tanımlanmaktadır. Dolayısıyla farklı özellikler içeren ürünler de ayrı birer ürün kodu olacak ve ayrı ürün ağaçları olacaktır. Buradaki konfigüratör yapısı, mevcut bir ürün baz alınarak ve üründe kullanılan özellikler ihtiyaç doğrultusunda değiştirilerek (dolayısıyla baz üründen farklı
malzemelerin kullandırılması sağlanarak), yeni bir ürün ağacı elde etmeye yarar.
![](../_assets/24bbf4f5d285b09096ab.png)**Şekil** **3.** Özellik – Değer Tanımlama Ekranı

#### Yarı Mamul ve Hammade Stok Bağlantı Tanımlama

Bu ekranda daha önce yapılmış olan konfigürasyon tanımları bir arada kullanılır. Burada yapılacak tanım ve eşleştirmelerin nihai amacı, mamul üzerinde gerçekleştirilecek konfigürasyon değişikliklerinin doğrulamasının ve kontrolünün yapılabilmesidir. Stok kayıtlarının hangi ikame malzeme gruplarında yer aldığı burada tanımlanır. Yine stok kayıtlarının ilgili özellik ve değer bilgileri de burada atanabilecektir. Ekranın en üst kısmı filtreleme yapabilmek için tasarlanmıştır, filtreleme yapılarak üzerinde çalışılacak stok kodlarının listede görüntülenmesi sağlanabilir. Burada Stok Kodu, Grup Kodu ve diğer kodlara göre filtreleme yapılabildiği gibi, Detay Kısıtlar bölümünde "Listeye İleri Kısıt Uygulansın" seçeneği ile daha gelişmiş bir filtreleme de tarif edilebilir. "Filtrele" tuşuna basıldığında verilen kısıtlara uyan stok kayıtları listelenecektir. Seçilen stok kaydı için satırdaki "İkame Malzeme Grup Kodu" alanına kod girilebilir veya rehberden eklenebilir. Tüm satırlardaki ikame malzeme grup kodunun değiştirilebilmesi için en üstteki mavi renkli satıra bileşen kodu girilir, alandan çıkıldığında doğrulama amaçlı "Girmiş olduğunuz değerler tüm satırlara yansıtılacak. Devam etmek istiyor musunuz?" mesajı çıkacaktır. Evet dendiğinde listedeki tüm kayıtların ikame malzeme grupları güncellenir. Özellik ve değer atama işlemi ekranın alt bölümünde yapılır. Stok kaydı listesinden ilgili kayıt üzerine gelinir, Özellik Kodu ve Değer Kodu girilir. Kaydedilen bilgiler en alt kısımda listelenecektir. Özellik ve değer girebilmek için ikame malzeme grubu tanımlamış olmak gerekir. Bir malzemenin birden fazla özelliği olabileceğinden, burada aynı satır için birden çok özellik ve değer tanımlaması yapılabilmektedir.
![](../_assets/8aaceba49de6c27bf6c2.png)**Şekil** **4.** Yarı Mamul ve Hammade Stok Bağlantı Tanımlama

#### Kural Tanımlama Ekranı

Bir ürüne ait konfigürasyonda değişiklik yapılacağı zaman bu değişiklik ürün ağacını da etkileyecektir. Bir mamulün ürün ağacında değişim yönetiminin kapsamında olacak ve ne tür değişiklikler yapılabileceği veya yapılamayacağı kurallarla tarif edilmesi istenen her bileşenin öncelikle bir ikame malzeme grubu ile ifade edildiği varsayımını yapıyoruz. Böylece kullanıcı ürün konfigüre ederken sadece önceden belirlenmiş kurallar çerçevesinde değişiklikler yapacağından ürün konfigürasyonu kontrol altında tutulmuş olur. Kural tanımlama ekranında bu tür konfigürasyon kontrol kuralları tanımlanabilecektir. Kural tanımı ürün grupları ve ikame malzeme grupları bazında yapılmaktadır. Ekranın üst kısmında kuralların uygulanacağı ürünler ve bileşenleri (ikame malzeme grubu veya stok kodu bazında) seçilir, kural listesinden ilgili kayıt seçilerek eşleştirilir.

Kural listesinde tanımlı olan kayıtlar:

**Ürün Ağacını Değiştirmez:** Bu kuralda tarif edilen ikame malzeme grubu veya stokla ilgili bir değişiklik yapıldığında ilgili kaydın ürün ağacının değişmeyeceği varsayılmaktadır. Bu bileşen ürün ağacında değiştirilse bile nihai ürünün stok kodu aynı kalacaktır.

**Ürün Konfigürasyon Hazırlarken Silme Yapılabilir:** Ürün ağacından belirtilen ikame malzeme grupları veya stoklar kullanıcı tarafından silinebilir anlamına gelmektedir. Ürün ağacı onaylama yetkisi olmayan kullanıcılar için geçerlidir.

**Ürün Konfigürasyon Hazırlarken Ekleme Yapılabilir:** Ürün ağacına belirtilen ikame malzeme grupları veya stoklar kullanıcı tarafından eklenebilir anlamına gelmektedir. Ürün ağacı onaylama yetkisi olmayan kullanıcılar için geçerlidir.

**Ürün Konfigürasyon Hazırlarken Değiştirme Yapılabilir**: Ürün ağacında belirtilen ikame malzeme grupları veya stoklar kullanıcı tarafından değiştirilebilir anlamına gelmektedir. Ürün ağacı onaylama yetkisi olmayan kullanıcılar için geçerlidir.
Kurallar bir kere tanımlandıktan sonra bu kurala özel istisnai durumlar yani kuralın uygulanmamasının istendiği durumlar da tanımlanabilir. Kural seçildikten sonra "Kural İstisna Tanımlama" tanımlama tuşu ile yine ürün ve bileşen grubu bazında kurala dahil edilmemesi istenen kayıtlar diğer sekmede tanımlanabilmektedir.

![](../_assets/8aaceba49de6c27bf6c2.png)**Şekil** **5.** Kural Tanımlama Ekranı

#### Konfigüratör Parametreleri Ekranı

Ürün Konfigüratörü ekranında bir taslak onaya gönderildiğinde ilgili kişilere mail gönderilecektir. Kime mail gönderileceği "Yönetici Mail" alanında tanımlanır. Birden fazla kişiye mail gönderilmesi için mail adreslerinin arasına ";" girilmelidir.
"Ön Onay Sistemi" parametresi işaretlendiğinde satış teklifi aşamasında konfigürasyon taslakları Ön Onay'a gönderilir. Ürün geliştirme birimi tarafından ürün taslakları kontrol edilir ancak bir değişiklik yapılamaz. Ön Onayda kabul edilen bir taslak daha sonraki aşamada tekrar onaya gönderilebilecektir. "Ön Onay Sistemi" işaretlenmediğinde ürün taslakları direk onaya gönderilir.

#### Yetkilendirme İşlemleri

Yeni Konfigürasyon ekranları için tanımlanmış kullanıcı program yetkileri aşağıdaki gibidir:

**Program**

**NoProgram** **Adı**:

Ürün Grubu Tanımlama

İkame Malzeme Grubu Tanımlama

Özellik Tanımlama

Değer Tanımlama

Kural Tanımlama

Yarımamul ve Hammadde Stok Bağlantı Tanımlama

Ürün Konfigürasyon Onaylama

Ürün Konfigürasyon Hazırlama

Konfigüratör Parametreleri

Burada dikkat edilmesi gereken nokta Ürün Konfigürasyon Hazırlama ve Ürün Konfigürasyon Onaylama yetkilerinin verilmesiyle ilgilidir. Hazırlama yetkisi olan kullanıcı ürün reçeteleri üzerinde değişiklik yapsa da bunları ancak taslak olarak
kaydedebilecektir. Değişiklikler Onaylama yetkisine sahip kullanıcının onayı sonucu reçeteye yansıtılacaktır. Sıfırdan ürün tasarlama işlemi için kullanıcıda yine Ürün Konfigürasyon Onaylama yetkisinin olması gerekmektedir.

#### Satış Teklifi Ekranındaki Değişiklikler

**Talep/Teklif** modülünde **Satış Teklif** ekranında teklif kaydı oluşturulurken farenin sağ tuşuyla açılan pencereden Ürün Konfigüratörü ekranı açılarak bir taslak oluşturulduğunda ve teklif kaydına dönüldüğünde kalem bilgilerinde stok kodu olarak **KONFIG** görünecektir.
Taslağın onaylanması sonrasında teklif ve sipariş sürecine devam edilebilmesi için, yeni verilen stok kodunun satış teklifindeki "Konfig" değeri yerine yazılması gerekir. Bunu teklif kaydı üzerinde iken sağ tıkla açılan menüden "Konfigürasyon Kodu Değiştirme" seçerek yapabilirsiniz. Onay aşamasında verilen stok kodu "Yeni Stok Kodu" alanında görülecektir, "Tamam" dendiğinde teklif kaydı yeni stok kodu ile kaydedilir. Taslak hala onay sürecinde ise "Yeni stok kodu bulunamadı" yazacaktır.

![](../_assets/bbb9987d46a41100b863.png)**Şekil** **8** Konfigürasyon Kodu Değiştirme Ekranı

#### İş Emri Girişi

İş Emri Girişi ekranının görünümünde bir değişiklik olmamıştır, ancak iş emrine bağlı ürün ağacının getirilmesinde bir değişiklik yapılmıştır. Eğer iş emri girişinde sipariş numarası belirtilir ve "Reçete Saklansın" seçilir ise, bu siparişle ilgili tekliften
konfigürasyon kayıtlarına ulaşılır. Bu kayıtlardaki "Stok Takibi Yapılmayacak" olarak tanımlı bileşenler dikkate alınmaz. "Ürün Ağacını Değiştirmez" olarak işaretli bileşenler taslaktaki haliyle dikkate alınır, yani ürün ağacındaki karşılıkları yerine bu bileşenler iş emrinin reçetesine kaydedilir. Bu şekilde mevcut bir baz mamul üzerinde sadece "Ürün Ağacını Değiştirmez" bileşenler değiştirildiğinde, teklif isteğe göre konfigüre edilmiş olur ve ürün ağacında değişiklik yapılmasına gerek kalmadan iş emri reçetesine yansıtılmış olur.
