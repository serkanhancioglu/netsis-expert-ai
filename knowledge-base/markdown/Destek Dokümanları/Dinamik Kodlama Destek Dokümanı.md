---
title: "Dinamik Kodlama Destek Dokümanı"
page_id: "50680277"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Dinamik Kodlama Destek Dokümanı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Dinamik Kodlama Destek Dokümanı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTA4OTBiYzA5LTA4MzQtNDAyMy1iOWJkLWMwZTE2YzM0MDBkZSZsaW5rPThjOWJiNmFjLWVkN2QtNDgxOS1iMzA2LWFjODFhNmIyMzcyOCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=0890bc09-0834-4023-b9bd-c0e16c3400de&link=8c9bb6ac-ed7d-4819-b306-ac81a6b23728&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "dinamik-kodlama-destek-dokumani_82576787_50680277.html"
source_version: "2022-11-03T09:52:06.863+03:00"
source_bytes: 1327776
fetched_at: "2026-09-13T04:26:20+00:00"
generator: "netsis-scraper 1.0.0"
---
# Dinamik Kodlama Destek Dokümanı

Dinamik Kodlama ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

|  |  |
| --- | --- |
| Ürün Grubu | \[X\] Fusion@6 |
| Kategori | \[X\] Yeni Fonksiyon |
| Versiyon Önkoşulu | @6 |

@6 Serisi ürünlerde, kullanıcı arabirimlerinin her yerine eklenen dinamik kodlama özelliği ile, programın standart davranışını değiştirecek kod yazılması, ekranların istendiği şekilde değiştirilebilmesi, yeni özellikler kazandırılması gibi programlama tekniği ile yapılabilecek fonksiyonlar, kodlanabilmektedir. Dinamik kodlama özelliğinde, kodlama VBScript dili ile yapılmaktadır. Vbscript kodlarını sadece admin olan kullanıcılar tanımlayabilmekte ve gerektiğinde geçersiz hale getirebilmektedirler.

#### Dinamik Kod Desteği Parametresi

Dinamik kod desteğinin programda aktif hale getirilmesi için Yardımcı Programlar-Kayıt-Şirket Şube Parametre Tanımları menüsünde Parametreler sekmesinde bulunan Dinamik Kod Desteği parametresinin işaretlenmesi gerekmektedir. Bu parametrenin işaretli olduğu durumlarda, formların sol üst köşesinde bulunan N Harfine tıklandığında, Netsis script kod desteği seçeneği gelecektir. Netsis script kod desteği tıklandığında kod geliştirme ortamı açılacaktır.

#### Dinamik Kodun Yazılma ve Çalışma Yeri

Dinamik kodlama, Netsis programlarının herhangi bir ekranında ya da NDI uygulamasında hazırlanan bir ekranda çalışması için, o ekrana ait script kod girişi bölümünde yazılır. Kod, hangi ekran için yazıldıysa o ekran için çalışır. Yazılan kod, içinde bulunduğu ekranda, programın doğal davranışı dışında başka bir işlemin yapılabilmesini sağlar. Örneğin stok kartı kayıtları ekranında çalışması istenen dinamik kod, "stok kartı kayıtları" menü seçeneği ile açılan pencerenin sol üst köşesindeki menüsünden "*Netsis* *Script* *Kod* *Desteği*" seçeneği ile açılan bölümde yazılmalıdır.

![](../_assets/5a42728d60c11915a4d7.png)![](../_assets/15273ce951a4e094796d.png)
Stok modülü ana menüsünün sol üst köşesinden açılan script kod bölümünde yazılan kod, sadece modül menüsünde çalışacaktır. NDI uygulamasında hazırlanan bir ekran (form) için, programlama, yine formun sol üst köşesinden açılan menüden ya da form içindeki herhangi bir bileşen üzerinde sağ click menüsünden Script / Dinamik Kod Desteği seçeneği ile gelen ortamda yapılabilir. Script kodun içinde çalıştığı ekrana "*form*" adı verilmektedir ve dokumanın sonrasında bu şekilde adlandırılacaktır. Netsis script kod geliştirme ortamı üç bölümden oluşmaktadır. Bunlardan ilki, kod geliştirme ortamına girildiğinde gelen Özel Menü başlıklı bölüdür.

#### NETSĐS SCRIPT KOD DESTEĞİ

##### Özel Menü Sekmesi

Dinamik kodlama uygulaması ile kullanıcılar tarafından programdaki sağ kliklerdeki menülere eklemeler yapılabilir. Özel Menü bölümünde de farenin sağ tuşunda gelecek menünün adı belirlenmektedir. Kullanıcılar tarafından eklenen bu menülere vbscript kodu yazılabilir.
Örneğin SCRIPT isimli bir menü eklemek isteniyorsa Menü adı kısmına kodlama sırasında görülecek açıklama yazıldığında, bu adın başına program tarafından mnCustomItem\_ ibaresi ekleyecektir. Açıklama kısmına yazılan değer ise tanımlanan menünün ekranda görülecek ismidir.
**Satır Ekle:** Yeni bir menü eklemek için boş bir satır açar.
![](../_assets/7c541005f556fde53ae2.png)

**Çizgi Ekle:** Menüler arasına yatay çizgi eklenmesini sağlar.
**Satır Sil:** Üzerinde bulunulan satırı silecektir.
**Hepsini Sil:** Bu ekranda bulunan tüm tanımlamaları silecektir.
**Menü Test:** Menünün görünümünün test edilmesini sağlar.
**Kısıtlamaya Geç:** Özel menü bölümünden çıkarak, Script nesneleri kısıtlama bölümüne geçmek üzere kullanılan butondur.

Bu bölümde yapılan tanımlamalar sonucunda, tanımlamanın yapıldığı ekranda farenin sağ tuşuna basıldığında "Kullanıcı İşlemleri" kısayol seçeneği gelecektir. Bu seçenek altında da tanımlanan özel menüye, belirlenen açıklama bilgisi ile erişilebilir.

##### Script Nesnelerini Kısıtlama Sekmesi

Özel Menü bölümündeki "Kısıtlamaya Geç" butonuna basıldığında script girişi esnasında hangi nesnelerin kullanılacağının belirlendiği Script Nesnelerini Kısıtlama bölümü gelecektir. Eğer vbscript kodu, sadece yeni eklenen sağ klik menüsü için yazılacaksa, gelen listeden sadece TMenuItem'ın seçilmesi yeterli olacaktır. Burada bulunan nesnelerin tümü seçilerek de kodlamaya geçiş yapılabilir. Bu durumda, formdaki tüm nesneler için istenirse kodlama yapılabilir. Ancak, tüm nesnelerin eklenmesi, formun açılma hızını etkileyecektir. Bunun sebebi formun her açılışta buradaki nesneleri yükleyerek açmasıdır. Listede yer alan nesneler, scriptin içinde yazıldığı formda bulunan nesnelerdir. *Bknz:* *Nesne* *(Object,* *Instance)*.
**Listedeki tüm nesneleri seç:** Listelenen nesnelerin tamamını birden seçmek için kullanılan butondur. Seçilen nesnelerin solundaki kutu işaretlenecektir.
**Seçimi iptal et:** Listelenen nesnelerden seçilmiş olaların seçimini kaldırmak için kullanılan butondur.
**Script kodlamaya geçiş:** Seçilen nesneler kullanılarak script kodu yazmak için Script Tanımlama bölümüne geçmek için kullanılan butondur.

##### Script Kodlama Sekmesi - Olay (Event)

Script kodu, formdaki herhangi bir görsel bileşene ait olay (event) gerçekleşmesinde çalışabilir.
![](../_assets/1c20690f815ab7234079.png)

Daha doğrusu script kodu, formdaki herhangi bir görsel bileşenin, herhangi bir olayında çalışması için yazılır. Örneğin "kod" isimli alfabetik bilgi giriş sahası (TEdit) görsel bileşeninin çıkışında (onexit), kullanıcının "kod" sahasına girmiş olduğu bilginin kontrolü script içinde yapılarak, buna göre farklı bir davranışta bulunulabilir, mesela girilen kodun kabul edilmemesi, uyarı verilmesi ve tekrar kod okunmak üzere aynı sahaya dönülmesi gibi. *Bknz:* *Olay* *Sürmeli* *(Event* *Driven)* *Programlama*

#### Nesne İzleme Bölümü

Script kodu yazılmadan önce mutlaka hangi bileşenin hangi olayı için yazılacağı belirlenmelidir. Script kodlama ekranına geçildiğinde, sol bölümdeki "*Nesne Đzleme*" penceresinde, scriptin yazıldığı formda bulunan görsel bileşenler listelenir. Listede her bir görsel bileşen, bir nesne olup, kendi türediği sınıf başlığının altında yer alır. *Bknz:* *Sınıf(Class);* *Nesne (Object,* *Instance)*.
Örneğin, TEdit sınıfının altında, script yazılan formda bulunan alfabetik okuma sahalarının isimleri yer alır. TButton sınıfı altında, formdaki butonların isimleri yer alır. Listeden, herhangi bir olayı için script kod
yazılmak istenen bileşen, fare ile tek tıklanarak belirlenmelidir. Burada listelenen bileşenlerden herhangi biri için daha önceden script girişi yapılmış ise, ilgili bileşenin solunda, sağa doğru yeşil bir ok işareti olacaktır. Bu bileşen seçildiğinde ise, girilmiş script, Kod geliştirme bölümüne gelecektir.

#### Nesne Olayı (Event) Bölümü

"*Nesne İzleme*" penceresinin altındaki bölümde yer alan "*Nesne Olayı (Event)*" bölümünde ise, seçilen bileşen için geçerli olaylar listelenir. Script kodunun, hangi olay gerçekleştiğinde çalışması isteniyorsa, bu olay fare ile tıklanarak belirlenmelidir. Örneğin TButton sınıfından OkBtn isimli bileşen ve bu bileşene ait olaylardan onclick seçilirse, kullanıcı ekrandaki OkBtn isimli butona bastığında çalışması istenen kod yazılabilir. Örnekte, Stok Kartındaki stok kodu (STOK_KODUDB) sahasının çıkışında (onexit) çalışacak kodun yazılacağı belirtilmiştir. *Bknz: Olay Sürmeli (Event* *Driven)* *Programlama*. Kodlama bölümünde yazılan kod, seçilen nesnenin, seçilen olayı gerçekleştiğinde çalışacaktır. Kod yazılırken sol tarafta seçili nesne ve olayın, doğruluğuna dikkat edilmelidir.

#### Kodlama Bölümü

##### VBScript Syntax

Ekranın ortasındaki boş alan script girişi için editor olarak tasarlanmıştır. Kodlama, işletim sisteminin doğrudan yorumlayabildiği VBScript komutları ve sentaksı kullanılarak yapılmalıdır. "IF ... THEN ... ELSE ... END IF", "SELECT CASE ... ELSE ... END SELECT", "FOR ... NEXT", "DO WHILE ... LOOP", "MSGBOX", "INPUTBOX" gibi vbscript komutları, temel program mantığının oluşturulmasında kullanılır.

#### Araç Çubuğu – 1 (Sol Üst)

![](../_assets/0eb77bdf762b88188057.png) **Kaydet:** Script'in saklanmasını sağlar. Yazılan script'ler bu butonla saklandıktan sonra, değişikliklerin geçerli olması için ekranın en alt bölümündeki Tamam butonuna basarak ekranın kapatılması gerekmektedir. Script ekranı Tamam butonu dışında bir şekilde kapatılırsa, değişiklikler saklanmadan çıkılacaktır.

![](../_assets/8fd2464f53815a642dad.png) **Yenile:** Kod geliştirilme ortamının güncellenmesi için kullanılan butondur. Bu butona basıldığında, script girişi en son kaydedilen haline dönecektir.

![](../_assets/0433739526f5bfb4e47f.png) **Temizle:** Kod içeriğinin temizlenmesi için kullanılan butondur. Yani butona basıldığında, ekranda görülen scriptler silinecektir.

![](../_assets/9095e8dcf9f40b3b9a42.png) **Kod Şablonları:** Daha önceden saklanmış kod şablonları arasından seçim yapmak için kullanılan butondur. Bu butona basıldığında, Netsis Script Kod Şablon Tanımlamaları rehberi gelecektir.

![](../_assets/415bedfcf5fd9b608671.png) **Form Global:**

![](../_assets/8d18430c6208b78a3f3c.png) **Session Global:**

![](../_assets/2feb4df8c0bbe7e2d2ca.png) **Uygulama Global:** Tüm formlarda, tüm şirketlerde ortak kullanılmak istenilen tanımlamaların girilmesi için kullanılan butondur. Yani eğer yazılan bir fonksiyon veya sub her yerde ortak olarak kullanılmak isteniyorsa bu tanımlamayı uygulama global kısmında yaparak tüm modüllerde ve şirketlerde bu fonksiyona erişerek çalıştırılabilir. Bu özellik ile ortak olan bir fonksiyon tanımlamasının, kullanılacak olan her ekranda tekrar tekrar yazılması önlenmiştir.
Örneğin; sub mail(kime,cc,subject,ek,body) call NETSISCORE.NetLibEMail.EPostaGonder(kime,cc,subject,ek,body) end sub şeklinde Uygulama Global'de yapılan bir tanımlamayı bizim hazırladığımız menüde kullanabilmek için; call appglobal.mail(MAIL,"","MEKTUP","",ICERIK) şeklinde çağırılması gerekmektedir.
Yukarıdaki sub tanımlamasında NETSISCORE.NetLibEMail.EpostaGonder şeklinde bir tanımlama yapılmıştır. Bu tanımlama ile Netsis'in nesnelerinin kullanıldığı belirtilmiştir. Bu nesneler hakkında bilgi almak için Nesne Tarayıcısı Kullanılabilir. *Bknz: Nesne* *Tarayıcısı*.

#### Nesneye Yönelik Programlama Kavramları

**Sınıf** **(Class):** Nesneye yönelik programlamada temel öğelerdir. Gerçek dünyadaki ya da akıldaki mantıksal nesnelerin programlamda ifade edilmesi için Class yapısı kullanılır. Sınıfların özellik (property) ve yöntemleri (method) vardır. Özellikler, sınıfı tanımlayan verileri olup, yöntemler ise sınıfın yapabileceği işlemler, yani yetenekleridir. Sınıf tanımı içinde sınıfa ait özellik ve yöntemler belirtilir. Programda sınıf tanımlarından nesneler türetilir. O nedenle sınıf tanımı, aynı zamanda nesne şablonu olarak da düşünülebilir.

**Nesne (Object,** **Instance):** Tanımlı bir sınıfın programda kullanılan bir örneğidir ya da olumudur. Sınıfların amacı, bir yapıyı bir kez tanımlamak, isimlendirmek ve tekrar tekrar kullanılmasını sağlamaktır. *Bknz: Sınıf (Class)*. Program yazılırken, bir sınıf tanımına ait gerektiği sayıda nesne yaratılıp kullanılabilir. Bu nesneler, sınıf tanımındaki özelliklere sahiptir ve yöntemleri gerçekleştirebilir. Aynı program parçası içinde, sınıflardan türemiş her bir nesnenin tekrarsız bir adı olmak zorundadır ve nesne bu isimle kullanılır.

**Olay Sürmeli (Event Driven)** **Programlama:** Bir program, bir başlangıç noktasından başlayıp, sırayla devam edip bir yerde bitmiyorsa, kod parçacıklarının çalışması olaylara bağlanmışsa buna olay sürmeli programlama diyoruz. Win32 görsel formlarının olay sürmeli programlanması zorunludur. Çünkü kullanıcı form üzerinde işlem yaparken bir sıra takip etmek zorunda değildir ve birbiri arkasından çok farklı olaylar meydana gelebilir. Örneğin bir bilgi giriş sahasına giriş, bilgi giriş sahasından çıkış, başka bir bilgi giriş sahasına uğramadan bir butona basılması gibi. O nedenle, form, üzerinde oluşabilecek her olay için bir kod parçacığı yazılarak yönetilmelidir.
Form ve formun üzerindeki görsel bileşenlerin her biri kendi sınıf tanımının özellik ve yeteneklerini içeren birer nesnedir. *Bknz: Nesne (Object, Instance)*. Her nesnenin olmamakla birlikte çoğunun nesne girişi, çıkışı, tıklanması gibi olayları mevcuttur.
Nesneler, sınıflarından gelen yeteneklerinden dolayı bazı işlemleri doğal olarak her seferinde aynı şekilde yapabilir. Örneğin, nümerik veri girişi alanı sınıfından türemiş ve form üzerine konmuş tüm nesneler, nümerik karakterleri alacak, alfabetik karakterleri kabul etmeyecek, belki basamak gruplaması ve ondalık gösterim gibi yetenekleri sergileyecek tir. Ancak bu nesne, Örneğin, iki tane nümerik sahadaki değerlerin çarpılarak başka bir sahada gösterilmesi gibi bir yeteneğe sahip değildir. İstenen bu işlem, nesne çıkışlarına ya da bir buton tıklanması olayı için ayrıca yazılmalıdır.
Dinamik kodlamada, bir form üzerinde mevcut görsel bileşen nesnelerinin olayları gerçekleşmesi sırasında çalışacak kod parçacıkları yazılabilmektedir. O nedenle kod yazımız öncesinde, hangi nesnenin hangi olayı için kod yazıldığı belirlenir. *Bknz:* *Nesne* *Đzleme* *Bölümü,* *Nesne* *Olayı* *(Event)* *Bölümü*.

![](../_assets/493c5d5b9ae84e2f9a59.png)![](../_assets/fa019829756e20b6b14c.png)![](../_assets/8cf003ce94cf6bd4a8ac.png)
**Kalıtım (Inheritance) ve Sınıf** **Hiyerarşisi:** Mevcut bir sınıfın yapısının, yetersiz kaldığı ve sınıftan yaratılacak nesnenin ek özellikler ve yetenekler içermesi gerektiği durumda, mevcut sınıfın yapısını ve mevcut yaratılmış nesnelerdeki kullanımını bozmadan, bu sınıfın yöntem ve özelliklerini miras alan yeni bir sınıf yapısı tanımlanabilmektedir. Yaratılan sınıf, türediği üst sahibinin (owner), özellik ve yöntemlerini miras alır. Yeni sınıfa yeni özellik ve yöntemler ilave edilebilir, sahip sınıf tanımında izin verilen özellik ve yöntemlerde değişiklik yapılabilir. Görsel programlama araçlarında, program yazımında kullanılabilecek sınıf kütüphaneleri mevcuttur ve içinde birçok sınıf barındırır. Bu kütüphanelerde sınıf hiyerarşisi de mevcuttur.

**Netsis** **Kütüphanesi:** Netsis, dinamik kodlama içinden, içinde bulunulan formda ya da uygulama genelinde mevcut nesnelerin özellik ve yöntemlerine (görsel bileşenlerin içerikleri, global değişkenler, Netsis uygulamasında yapılabilen e-mail, sms gönderme gibi birtakım işlemler) erişimi mümkün kılmak için, ortamda geçerli kütüphaneler sağlar.
Netsis kütüphaneleri, paketin kurulumu sırasında sisteme yüklenir ve kayıt edilir. Ancak kütüphanelerin yenilenmesi ya da tümüne erişim sağlanamaması durumunda, kurulum sırasında yaratılan SERVIS klasöründeki (NETSIS/FUSION06/SERVIS), RegKontrol.Exe çalıştırılarak kütüphanelerin tekrar kayıt edilmesi sağlanabilir.

#### Nesne Tarayıcısı ()

**Kullanılan** **Kütüphaneler:** Kodlama ortamında hangi kütüphanelerin kullanılabileceği, kodlama bölümünün araç çubuğundaki "*Nesne Tarayıcısı*" butonu yardımıyla izlenebilir. Nesne Tarayıcısının sol üst köşesinden açılan listede, kullanılabilecek kütüphaneler görülebillir.
**Kayıtlı Sınıflar:** Netsis kütüphaneleri ile kayıt edilen ve script kod içinde kullanılabilecek sınıfların isimleri listede yer alır. Herhangi bir sınıfla ilgili bilgi alabilmek için sınıf üzerine tıklanmalıdır. Seçilen sınıfın özellik (property) ve yöntemleri (function, procedure) sağ taraftaki bölümde listelenir. Herhangi bir özellik ya da yöntemin de tek tıklanmasıyla seçimi sonrasında, aynı pencerenin alt kısmında, yöntemin geriye döndürdüğü parametrenin tipi, yöntemin kısa tanımı ve varsa yöntemi kullanırken gönderilmesi gereken parametrelerin listesi yer alır.

**Kütüphanelerdeki** **Sınıflar:** Kodlama sırasında kullanılabilecek nesnelerin kısayol yardımı için *bknz: Araç Çubuğu-**2* *(Sağ* *Üst)*/*Kod* *Đçeriği* *(Code* *Insight).*
![](../_assets/77a098c178e5e92980ae.png)

**NetsisCore (ICore):** Netsis'in uygulama çalışma sırasında bellekte bulunan aktif kullanıcı, aktif modül, aktif menü seçeneği, entegrasyon tarihi vb. kor (çekirdek) bilgilerine ve Netsis paketinin altyapısında kullanılan E-posta, SMS gönderme fonksiyonları, kredi
kartı doğrulama, seslendirme, onaylı sürüm kontrolü, veri tabanı sorgulama nesneleri yaratılması vb. yöntemleri barındıran ana sınıftır. Sınıf ismi "ICore", kodlama ortamında kullanılbilecek nesne ismi ise, "NetsisCore" dur.
Nesne Tarayıcısında "ICore" ile başlayan alt sınıfları içerir. Kodlama ortamında kullanılabilecek nesneleri ise, "ICore" yerine "NetLib" ile başlar, geri kalan bölümü ise aynıdır. Örnek: Sınıf = "IcoreDB", Nesne = "NetLibDB". Her bir alt sınıfın kendi yöntemleri vardır. Yöntemler, NetsisCore.AltSınıf.Yöntem şeklinde kullanılmalıdır. Örnek:"NetsisCore.NetLibDB.GetNewQuery", kor (çekirdek) kütüphanenin veritabanı ile ilgili alt nesnesinin sorgu nesnesi yaratma yöntemini çalıştırır.
**NetsisVCL:** Birçok görsel bileşen sınıfı içeren Netsis Görsel Bileşen Kütüphanesidir (Visual Component Library). Nesne tarayıcısında, NetsisVCL içindeki görsel bileşen sınıfları "INetT" ile başlar. Kodlama ortamında görsel bileşen nesnesinin kullanılması için doğrudan ilgili nesnenin adı yazılabilir.
**CommonQuery:** Netsis kor (çekirdek) kütüphanesinin (NetsisCore), veritabanı altnesnesinin (NetlibDB), sorgu yaratma yöntemiyle (GetNewQuery) yaratılan sorgu nesnesidir. Sorgu nesnesinin, SQL cümlesi, kayıt sayısı, aktif olup olmadığı, kayıt kümesinin sonuna gelip gelmediği, saha bilgileri vb. özellikleri ile, sonuç kümesi dödürülmesi, ilk kayıt, sonraki, önceki, son kayıt vb. yöntemleri mevcuttur.
**Self:** Kodun çalışması sırasında aktif olan nesne için standart kullanımdır. Özellikle, kod yazımı sırasında, kodun hangi nesne için çalıştığı bilinmeyen durumda kullanılabilir. Dinamik kodlama için self, kodlama öncesinde sol bölümdeki "nesne izleme" listesinden seçilmiş olan ve sonrasında, kodun hangi olayı (event) için yazıldığının belirlendiği nesnedir. Self.özellikadı ya da self.yöntemadı formatında yazılarak aktif nesnenin bilgilerine erişmek ya da yöntemini çalıştırmak mümkündür.

#### Araç Çubuğu-2 (Sağ Üst)

![](../_assets/f2434c8939e3fe5be42b.png) **Kod Tamamlama (Code Complete):** Belli kalıplarda kod bloklarının otomatik olarak tamamlanması için kullanılabilir. Örneğin "if" ibaresi yazılarak bu tuşa basıldığında, bir if-then-else bloğunun düzgün syntax ile tamamlanması sağlanabilir.

![](../_assets/3a82edaf4189fc40aef7.png) **Kod İçeriği (Code Insight):** Script içinde kullanılabilecek hazır nesneleri ile nesnelere ait özellik (property) ve yöntemlerin (method) listesinin getirilebileceği tuş. Script giriş editöründe, Ctrl-boşluk tuşu ile aynı işleve sahiptir. Editörde Ctrl-Boşluk tuş takımı ya da araç çubuğundaki bu buton ile, kullanıma açılmış olan nesneler getirilebilmektedir. Ctrl-Boşluk ile açılan "Netsis Code Insight" listesinden bir nesne seçilip tekrar ctrl-boşluk ile seçilen nesnenin özelliklerini getiren yeni bir Code Insight penceresi açılabilir. Buradan da nesnenin istenen kullanılacak özelliği seçilebilir.

![](../_assets/60e43a78fb9578ba6a07.png) **Git (Go To):** Bu butona basıldığında gitmek istediğiniz satır numarası sorgulanacak ve cursor kod içerisinde verilen satır numarasına gidecektir.

![](../_assets/b603f6c487b56ccdcc31.png) **Ara:** Kod içerisinde belli bir karakter dizisiniz aramak amacıyla kullanılır. Aranması istenen karakter dizisi, büyük/küçük harf duyarlı, sadece kelime, imleçten itibaren ara, sadece seçili metinde ara seçenekleri ile ileri/geri yönde aranabilmektedir.

![](../_assets/e9564ceb3fb169c9ede0.png) **Ara Sonraki, Önceki:** Kod içerisinde arama yapılıp verilen karakter dizisi bulunduktan sonra, aynı karakter dizisinin, verilen arama kriterleri ile, sonrakini/öncekini bulmaya yarayan butonlardır.

![](../_assets/b5db36522d3116cfef46.png) **Bul/Değiştir:** Arama işlevinin, bulunan karakter dizisi yerine başka bir karakter dizisini otomatik olarak yerleştirme amacıyla kullanılması içindir. Aranacak karakter dizisi ile yerine yerleştirilecek karakter dizisi belirtilmelidir.
![](../_assets/61af0fa5f670a740fb96.png)

Büyük/küçük harf duyarlı, sadece kelime, imleçten itibaren ara, sadece seçili metinde ara seçenekleri ile ileri/geri yönde arama geçerlidir. Đlk bul/değiştir işleminden sonra, sonraki/önceki için yukarıda belirtilen butonlar kullanılabilir.

![](../_assets/5be1098aea68dee13368.png) **Script Sakla/Yükle:** Yazılan scriptin dış ortama text dosya olarak aktarımı ya da dış ortamdaki bir script'in text dosyadan editöre yüklenmesi.

#### NETSİS SCRIPT KOD ÖRNEKLERİ

##### Örnek-1: Cari Hesap Kayıtları Sağ Click menüsünden anında cari hesaba e-posta gönderimi

Cari Hesap Kayıtlarında, Cari Kod kısmında bulunan cari koduna ait o andaki borç ve alacak bakiyesini carinin mail adresine yollayan bir uygulama.

![](../_assets/61af0fa5f670a740fb96.png)
Burada öncelikle cari hesap kayıtlarında cari kodu editbox'ında bulunan değeri CARI isimli bir değişkene atılıyor ve Netsis'in nesnelerinden NETSISCORE.NetLibDb.GetNewQuery ile QUERY isimli yeni bir sorgu nesnesi yaratılıyor. SORGU değişkenine çalıştırmak istenilen sorgu yazılıyor. Burada TBLCAHAR tablosundan borç ve alacak toplamı ile günün tarihini çeken bir sorgu yazılmıştır. Ardından QUERY nesnesi ile bu sorguyu çalıştırıyoruz.
Đkinci olarak carinin ismi ve mail adresi gerektiğinden bu bilgilerde QUERY1 ile çekiliyor. Ve içerik isminde mailin içeriğini saklayan bir değişken tanımlanıyor. Bu değişkene veritabanından çekilen verilerin de eklenmesi gerekmektedir. QUERY1 ile çekilen değerlerden CARI_ISIM sahasını içeriğe eklemek için QUERY1.fields(1).assstring tanımlaması kullanılabilir. Carinin EMAIL adresini eklemek için ise QUERY1.fields(0).assstring tanımlaması kullanılabilir yani sorgudaki ilk saha için 0 indeks'ten başlanarak veriler alınabiliyor.
ICERIK değişkeni tamamlandıktan sonra uygulama global'de tanımlanan mail sub'ı kullanılarak cariye mail atılması sağlanabiliyor.

##### Örnek-2: Girilen Stok Koduna göre Depo Kodunun Oluşturulması

Stok kodu girildiğinde girilen kod'a göre oluşan değerin depo kodu sahasına atılması istenebilir. Stok koduna IZM001,IZM002 gibi kodlar yazıldığında stokun depo koduna 1 yazılması; IST001,IST002 şeklinde kodlar yazıldığında depo koduna 2 yazılması aksi durumda 3 yazılması isteniyorsa;
![](../_assets/a7a4d1ac4eada8296367.png)
Burada stok kodu bilgisi edit olduğu için TDBNEdit altında bulunabilir. Yukarıdaki tanımlamaya bakıldığında Stok_kodudb'nin OnExit olayında script yazılmıştır ve stok koduna yazılan değerin ilk 3 hanesini alarak IZM olup olmadığı kontrol ediliyor eğer IZM ise depo koduna 1 yazılıyor. Depo kodu bilgisi de edit olduğu için Depo_Kodu.TEXT olarak atama yapılmıştır. Eğer IZM değilse kontrole devam ederek IST olup olmadığına bakılıyor doğru ise 2 aksi durumda 3 olarak depo kodu belirleniyor.

##### Örnek-3: INetStrGrid (Netsis grid nesnesi)

Aşağıdaki sıralama, StrGrid nesnesinin hangi sınıf hiyerarşisinin parçası olduğunu göstermektedir. Bu yapıya göre, StrGrid nesnesi, hiyerarşide kendinden önce gelen( atası olan ) tüm sınıfların özelliklerini, otomatik olarak desteklemektedir.
![](../_assets/9b8114a2c44567fa74b9.png)
Sınıf Hiyerarşisi

INetTObject-INetTComponent-INetTControl-INetTWinControl-INetStrGrid
StrGrid Nesnesi, tüm Netsis paketlerinde kullanılan *grid* nesnesidir .
*StrGrid* nesnesine ait örnek görünüm
'\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* *'StringGrid* *nesnelerine* *ait test* *kodları*

*'sgTest : String Grid nesnesidir* '\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

*'Đlk* *kolon* *uzunlugunu* *100* *pixel* *yap*

SGTEST.StrColumn(0).Width = 100
*'Đlk* *kolonda* *gösterilen* *bilgileri* *bold* *göster*

SGTEST.StrColumn(0).Font.Bold = true SGTEST.StrColumn(0).Title = "Stok Adı"
*'Đlk* *kolonun* *1..5 satırlarına* *değer* *1..5* *yaz*
for I=1 to 5 sgtest.cells(1,I) = "değer " & i next
*'Grid* *üzerindeki* *boyama* *işlerini* *gözden* *geçir*
sgtest.Invalidate
*'Grid* *nesnesine* *ait* *önemli* *bilgiler* *gösteriliyor*
GridBilgi = "aktif kolon " & sgtest.Col & chr(13) & chr(10) &\_ "aktif satır " & sgtest.Row & chr(13) & chr(10) &\_ "sabit satır sayısı " & sgtest.FixedRows & chr(13) & chr(10) &\_ "sabit kolon sayısı " & sgtest.FixedCols & chr(13) & chr(10) &\_
"Solda görünen kolonun numarası " & sgtest.LeftCol & chr(13) & chr(10) &\_

<table><tbody><tr><td><p><em>'Graphic</em> <em>nesnesi</em> <em>hazırlanıyor</em> <br/>Set GraphLib = NETSISCORE.NetLibGraph <br/><br/><em>'Ekran</em> <em>nesnesindeki</em> <em>TEdit</em> <em>sınıfına</em> <em>ait</em> <em>örnekler</em> <em>listeye</em> <em>alınıyor</em> <br/>Set EditListesi = Self.ComponentList("TEdit") <br/><br/><em>'Listede</em> <em>kayıt</em> <em>var</em> <em>mı?</em> <br/>if EditListesi.Count &gt; 0 then <em>'Listedeki tüm kayıtları</em> <em>dön</em> For i=1 To EditListesi.Count <br/><em>'Listedeki</em> <em>aktif</em> <em>nesneye</em> <em>erişim</em> <br/>Set edObj = EditListesi.Items(I - 1) <br/><em>'erişim</em> <em>yapılan</em> <em>nesnenin</em> <em>renk</em> <em>özelliği</em> <em>"domates"</em> <em>rengine</em> <em>atanıyor...</em> <br/>edObj.PropertyValue("Color") = GraphLib.WEBColorToColor ("clwebTomato") Next End If</p></td><td><br/></td></tr><tr><td><p><strong>Örnek-8: INetTWEBBrowser</strong> <br/>WEB sayfaları ve HTML düzeninde hazırlanan bilgilerin gösterilmesi için tasarlanmıştır. NDI paketinde Win32 ortamında, WEB sekmesinde TNetWEBBrowser nesnesi için <br/>kullanılabilir.</p></td><td><br/></td></tr><tr><td><p><em>'WEB</em> <em>nesnesini</em> <em>ilk</em> <em>kullanım</em> <em>için</em> <em>hazırla</em> <br/>call NETWB.Navigate("about:blank") <br/><br/><em>'Basit</em> <em>HTML</em> <em>rapor</em> <em>hazırla</em> htmlcode = "</p>"&amp;_ "<table>"&amp;_ "<tr><th>Adı</th><th>yasi"&amp;_ "</th></tr><tr><td>Cemal</td><td>50"&amp;_ "</td></tr><tr><td>Kemal</td><td>18"&amp;_ "</td></tr><tr><td>Đnes</td><td>20"&amp;_ "</td></tr></table>"<p><em>'Hazırlanan</em> <em>HTML</em> <em>bilgisinin</em> <em>ekranda</em> <em>görünmesi</em> <em>için</em> <em>güncelle</em> <br/>call NETWB.SetDisplayHTML(htmlcode) msgBox "Hazırlanan raporu izle"</p></td><td><br/></td></tr><tr><td><p><em>'NetWB</em> <em>nesnesini</em> <em>Netsis</em> <em>ana</em> <em>sayfasına</em> <em>yönlendir</em></p><p>call NETWB.Navigate("<a href="http://www.netsis.com.tr/">http://www.netsis.com.tr</a>")</p></td><td><br/></td></tr><tr><td><p><br/><img src="../_assets/d756a3a10b3bb84e7fc9.png"/> <br/>Yukarıdaki örnek koda ait ekran görüntüsü <br/><strong>Örnek-9: INetControl</strong> <br/>"Perform" ve "ClientRect" özellikleri eklendi. <br/>Perform komutuna ait bir örnek</p></td><td><br/></td></tr><tr><td><p><em>'*************************************************************************</em> <em>'CB_GETITEMHEIGHT windows mesajı nedir?</em> <em>'*************************************************************************</em> <em>'</em> <br/><em>'ComboBox</em> <em>nesnelerinde</em> <em>yer</em> <em>alan</em> <em>satırların</em> <em>yükselik</em> <em>'değerini</em> <em>geriye dönmektedir.</em> <br/><em>'Bu</em> <em>örnek,</em> <em>perform</em> <em>komutunun</em> <em>kullanımı</em> <em>için</em> <em>kullanılmıştır.</em> <br/><em>'Windows</em> <em>API</em> <em>seviyesinde</em> <em>dinamik</em> <em>kodlama</em> <em>için</em> <em>Windows</em> <em>SDK</em> <em>veya</em> <em>benzeri</em> <em>'kaynaklardan</em> <em>yardım alınması gerekmektedir...</em> <br/><em>'</em> <br/><em>'*************************************************************************</em> <br/><br/><em>'Windows</em> <em>mesaj</em> <em>listesindeki</em> <em>özel</em> <em>değer</em> <em>tanımlanıyor...</em> <br/>Const CB_GETITEMHEIGHT = 340 <br/><em>'Bu</em> <em>tür</em> <em>mesajlar</em> <em>için</em> <em>Windows</em> <em>SDK</em> <em>yardımları</em> <em>kullanılabilir</em> <br/><br/><em>'Ekrana</em> <em>Windows</em> <em>mesajının</em> <em>cevabını</em> <em>yazdır!</em> <br/>msgbox COMBOBOX1.Perform( CB_GETITEMHEIGHT, 0, 0 )</p></td><td><br/></td></tr><tr><td><p><strong>Örnek-10: INetObject</strong> <br/>InvokeEvent yöntemi eklendi. <br/>InvokeEvent komutuna ait örnek</p></td><td><br/></td></tr><tr><td><p><em>'Button</em> <em>nesnesindeki</em> <em>"OnClick"</em> <em>olayının</em> <em>(event)</em> <em>tetiklenmesi</em> <br/><br/><em>'OnClick</em> <em>gibi</em> <em>olay</em> <em>isimlerini</em> <em>öğrenmek</em> <em>için</em> <em>Dinamik</em> <em>kodlama</em> <em>'tasarım</em> <em>ekranından</em> <em>yardım alınabilir.</em> <br/><br/>BTNSAKLA.InvokeEvent("OnClick")</p></td><td><br/></td></tr><tr><td><p><img src="../_assets/f642d8852f57a99799ba.png"/>OnClick olayının Dinamik Kodlama Ekranından izlenmesi <br/><strong>Not:</strong> InvokeEvent yöntemi sadece tek parametreli olaylar için kullanılmalıdır. (Sender: Tobject) parametre deseninde olmayan olaylarda çalıştırılması sonucunda hata alınacaktır.</p><p>Örnek – 11: ICoreSession <br/>"EntegrasyonTarihi" özelliği eklendi.</p><p>Örnek – 12: ICoreLocalizationConvert <br/>Genelde Iran kültüründe ihtiyaç duyulan fonksiyonlar için kullanılabilir. Normal takvim sistemindeki bir değer Farsi sisteme, Farsi tarih sistemdeki tarih değeri de normal <br/>takvime çevrilebilir.</p></td><td><br/></td></tr><tr><td><p><em>'Localization</em> <em>servis</em> <em>nesnesine</em> <em>erişim</em> <em>yap</em> <br/>Set NetLocalizationService = NETSISCORE.NetLibLocalizationConvert <br/><br/><em>'Normal</em> <em>takvim</em> <em>bilgisi</em> <em>Iran</em> <em>takvim</em> <em>sistemine</em> <em>çevriliyor</em> <em>'***<strong>NOT:</strong>****</em> <br/><em>'Iran</em> <em>takvim</em> <em>sistemi,</em> <em>Netsis</em> <em>Çalışma</em> <em>Kültür</em> <em>değerinin</em> <em>Iran'a</em> <em>göre</em> <em>'ayarlanması</em> <em>durumunda çalışacaktır...</em> <br/>MsgBox NETSISCORE.NetLibLocalizationConvert.StrDateToStrFarsi("01/01/2007")</p></td><td><br/></td></tr><tr><td><p>Örnek-13: ICoreWin32 <br/>KrediKartNoDogrula, OzelParamVarMi , OzelParamDegerOku, YaziIlePara, YaziIleParaIng, WinPostMessage, WinSendMessage yöntemleri eklendi. <br/>Özel Parametre Kontrolü</p></td><td><br/></td></tr><tr><td><p>Dim BasimParamAcik <br/>BasimParamAcik = NETSISCORE.NetLibWin32. OzelParamVarMi("FATURA", "BASIM")</p></td><td><br/></td></tr><tr><td><p>WinPostMessage Kullanımı</p></td><td><br/></td></tr><tr><td><p><em>'Windows</em> <em>form</em> <em>kapanış</em> <em>özel</em> <em>mesaj</em> <em>değeri</em> <em>tanımlanıyor...</em> <br/>Const WINDOWS_MESSAGE_FORM_CLOSE = 16 <br/><br/><em>'Windows</em> <em>mesaj</em> <em>kuyruğuna</em> <em>zamanuyumsuz</em> <em>(asynch)</em> <em>mesaj</em> <em>gönderimi</em> <em>için</em> <em>kullanılır</em> <br/><br/><em>'Zamanuyumlu</em> <em>mesaj</em> <em>gönderimlerinde</em> <em>(synch)</em> <em>WinPostMessage</em> <em>yerine</em> <em>'WinSendMessage</em> <em>yöntemi kullanılmalıdır.</em> <br/><br/><em>'************************************************************************</em> <em>'Windows mesaj yönetimi için Windows-SDK yardımı kullanılabilir..</em> <em>'***********************************************************************</em> <br/><br/>CALL NETSISCORE.NetLibWin32.WinPostMessage(SELF.HANDLE, WINDOWS_MESSAGE_FORM_CLOSE, 0, 0)</p></td><td><br/></td></tr><tr><td><p>Örnek-14: ICoreSMS <br/>ICore. NetLibSMS yöntemi ile yaratılan nesne, tek ya da toplu olarak SMS gönderimi için kullanılmaktadır. Desteklediği yöntemler: AddMessage, SendMessage ve</p></td><td><br/></td></tr><tr><td><p>SendMessages yöntemleridir. Toplu mesaj gönderimlerinde, mesajlar AddMessage yöntemi ile eklenmeli ve tüm mesajlar eklendikten sonra SendMessages yöntemi çağırılmalıdır. Sadece bir mesaj gönderimi durumunda ise; SendMessage yöntemi çağırılmalıdır.</p></td><td><p><br/></p></td></tr><tr><td><p><em>'ICoreSMS</em> <em>nesnesi</em> <em>yaratılıyor</em> <br/>Set SMSObj = ICore. NetLibSMS( "Netsis", now, now+2 ) <br/><br/><em>'Mesaj</em> <em>gönderiliyor</em> <br/>Call SMSObj.SendMessage("Netsis",now,now+2,"Deneme","00905333333333","01","Netsis")</p></td><td><p><br/></p></td></tr><tr><td><p>Gainsboro</p></td><td><p>MistyRose</p></td></tr><tr><td><p>GhostWhite</p></td><td><p>Moccasin</p></td></tr><tr><td><p>Gold</p></td><td><p>NavajoWhite</p></td></tr><tr><td><p>GoldenRod</p></td><td><p>Navy</p></td></tr><tr><td><p>Gray</p></td><td><p>OldLace</p></td></tr><tr><td><p>Grey</p></td><td><p>Olive</p></td></tr><tr><td><p>Green</p></td><td><p>OliveDrab</p></td></tr><tr><td><p>GreenYellow</p></td><td><p>Orange</p></td></tr><tr><td><p>HoneyDew</p></td><td><p>OrangeRed</p></td></tr><tr><td><p>HotPink</p></td><td><p>Orchid</p></td></tr><tr><td><p>IndianRed</p></td><td><p>PaleGoldenRod</p></td></tr><tr><td><p>Indigo</p></td><td><p>PaleGreen</p></td></tr><tr><td><p>Ivory</p></td><td><p>PaleTurquoise</p></td></tr><tr><td><p>Khaki</p></td><td><p>PaleVioletRed</p></td></tr><tr><td><p>Lavender</p></td><td><p>PapayaWhip</p></td></tr><tr><td><p>LavenderBlush</p></td><td><p>PeachPuff</p></td></tr><tr><td><p>LawnGreen</p></td><td><p>Peru</p></td></tr></tbody></table>

|  |  |  |
| --- | --- | --- |
| CornflowerBlue | LemonChiffon | Pink |
| Cornsilk | LightBlue | Plum |
| Crimson | LightCoral | PowderBlue |
| Cyan | LightCyan | Purple |
| DarkBlue | LightGoldenRodYellow | Red |
| DarkCyan | LightGray | RosyBrown |
| DarkGoldenRod | LightGrey | RoyalBlue |
| DarkGray | LightGreen | SaddleBrown |
| DarkGrey | LightPink | Salmon |
| DarkGreen | LightSalmon | SandyBrown |
| DarkKhaki | LightSeaGreen | SeaGreen |
| DarkMagenta | LightSkyBlue | SeaShell |
| DarkOliveGreen | LightSlateGray | Sienna |
| Darkorange | LightSlateGrey | Silver |
| DarkOrchid | LightSteelBlue | SkyBlue |
| DarkRed | LightYellow | SlateBlue |
| DarkSalmon | Lime | SlateGray |
| DarkSeaGreen | LimeGreen | SlateGrey |
| DarkSlateBlue | Linen | Snow |
| DarkSlateGray | Magenta | SpringGreen |
| DarkSlateGrey | Maroon | SteelBlue |
| DarkTurquoise | MediumAquaMarine | Tan |
| DarkViolet | MediumBlue | Teal |
| DeepPink | MediumOrchid | Thistle |
| DeepSkyBlue | MediumPurple | Tomato |
| DimGray | MediumSeaGreen | Turquoise |
| DimGrey | MediumSlateBlue | Violet |
| DodgerBlue | MediumSpringGreen | Wheat |
| FireBrick | MediumTurquoise | White |
| FloralWhite | MediumVioletRed | WhiteSmoke |
| ForestGreen | MidnightBlue | Yellow |
| Fuchsia | MintCream | YellowGreen |

|  |
| --- |
| **Windows mesajlaşma sistemi (Windows Messaging)**<br>Windows işletim sisteminde kullanılan mesajlar için +[http://msdn.microsoft.com/library/default.asp?url=/library/en-+](http://msdn.microsoft.com/library/default.asp?url=/library/en-+) us/winui/winui/windowsuserinterface/windowing/messagesandmessagequeues.asp adresi kullanılabilir. **GDI (Graphics Device Interface)**<br>*Windows* GDI (grafik aygıt arabirimi), grafik çıktıyı görüntülemede kullanılan bir takım API lerden (Application Programming Interface) oluşur. **CANVAS**<br>*Canvas* nesnesi, nesnelerin resimlerini şekillendirmek için kullanılan bir çizim yüzeyi olarak ifade edilmektedir. *Canvas* nesnesi, özellikleri, olayları ve yöntemleri ile, nesnelerin, grafiksel olarak, çizim, boyama ve yazı yüzü özelliklerini belirlemek için kullanılmaktadır **BRUSH**<br>*Brush*, kapalı şekilleri doldurmak için kullanılan bir araçtır. *Brush* nesnesinin taşıdığı renk (brush.color), boyanacak alanın doldurulması için kullanılacaktır ve doldurma işlemi ile(fill), seçilen alan(clientrect, cliprect, vb.) bu renk ile boyanmış olacaktır. *Brush* nesnesi, taşıdığı renk(color), resim(bitmap) ve desen(style) ile tanımlanmaktadır. |

#### ![](../_assets/250fd1445b08a5289154.png)![](../_assets/cd7446d6677c9ab6c7c9.png)

#### PEN

*Canvas* nesnesi aracılığı ile kullanılabilecek olan *Pen* nesnesi, nesneye atanan renk ile(pen.color) çizgi çizmek için kullanılmaktadır.

**RECT**

*Rect* tipi, bir dikdörtgenin ölçülerini ifade etmektedir. Koordinatlar, sol, üst, sağ ve alt kenarları ifade eden 4 ayrı sayısal değer olarak ya da sol üst köşe ve sağ alt köşe noktaları olarak ifade edilirler.

#### POINT

*Point* tipi, ekran üzerindeki bir *pixel'* in yerini ifade eder. X, *Point* tipinin yatay koordinatını ifade eder.
