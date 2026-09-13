---
title: "Koşul Uygulamasında Yapılan Yenilikler"
page_id: "50684695"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Koşul Uygulamasında Yapılan Yenilikler"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Koşul Uygulamasında Yapılan Yenilikler"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTQ0ZTFiMjcyLWJmN2YtNDhmNy04MDAyLTgzMjM0MGE2MGUzMyZsaW5rPTE3ZTNkMjVkLTU4ZGYtNDkzNy1hZGIyLTU5ODcxMTI3NTk2ZCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=44e1b272-bf7f-48f7-8002-832340a60e33&link=17e3d25d-58df-4937-adb2-59871127596d&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "kosul-uygulamasinda-yapilan-yenilikler_90669874_50684695.html"
source_version: "2022-11-03T09:55:36.877+03:00"
source_bytes: 1312194
fetched_at: "2026-09-13T04:26:30+00:00"
generator: "netsis-scraper 1.0.0"
---
# Koşul Uygulamasında Yapılan Yenilikler

Koşul Uygulamasında Yapılan Yenilikler ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Bu doküman ile koşul uygulamasında yapılan değişikliklerin anlatılması amaçlanmıştır. Koşul uygulamasında yapılan yenilikler şunlardır:

- Koşul Sabit Kayıtları ve Detay Koşul Kayıtları ekranlarının daha düzenli hale getirilmesi.
- Koşul tanımlamalarının birden fazla stok rapor kodu için tanımlanabilmesi.
- Mal fazlası iskontolarının stok rapor kodlarına göre tanımlanabilmesi.
- Fire iskontosunun desteklenmesi.
- Satır bazında belirlenen vade gününe göre satır iskontosunun program tarafından getirilmesi.
- Cari için birden fazla koşul tanımlaması yapılarak, fatura işlemlerinde birden fazla koşulun geçerli olması ya da verilen önceliklere göre geçerli olacak koşulun belirlenmesi için Ek Koşul Kayıtlarında bulunan politikalardan farklı politikaların tanımlanabilmesi sağlanmıştır.

Modül: Cari

Gerekli Dosyalar: Cari.dll, Cartrk.dll, Fatura.dll, Fattrk.dll

Yükleme Sonrası: DbUpdate çalıştırılmalıdır.

**Koşul uygulaması ile ilgili yapılan yenilikler şu başlıklar altında incelenecektir;**

1-Koşul tanımlamalarında yapılan değişiklikler

1.1- Koşul Sabit Kayıtları 1.2- Koşul Detay Kayıtları 1.3- Ek Koşul Kayıtları

2-Vade bazında iskonto belirleme

2.1- Vade İskonto Kayıtları
2.2- Vade Kodunun Koşul Kaydında Kullanımı
2.3- Fatura modülünde kullanımı 3- İleri Koşul Uygulaması
3.1- Koşul Tip Kayıtları
3.2- Koşul Politika Kayıtları

**1- Koşul Tanımlamalarında Yapılan Değişiklikler**

Koşul Sabit Kayıtları, Detay Koşul Kayıtları ve Ek Koşul Kayıtlarının tanımlamalarının daha kullanışlı hale gelmesi için hem ekranlar üzerinde değişiklik yapılmış hem de tanımlamalara yeni sahalar eklenmiştir. Bu dokümanda yeni eklenen sahalar hakkında bilgi verilecektir. Daha önceden kullanılan sahalar hakkında detaylı bilgiyi ilgili modülün yardım dokümanlarında bulabilirsiniz.

Koşul Sabit Kayıtları

![](../_assets/ebe4800c6a47fc709b29.png)
Koşul Sabit Kayıtlarına eklenen sahalar şunlardır;

**Koşul Tipi:** Koşul Politika Tanımlamaları için kullanılacak sahadır. Bu sahanın kullanımı hakkında detaylı bilgi, dokümanın sonunda bulunan Koşul Tip Kayıtları bölümünde verildiğinden burada tekrar anlatılmayacaktır.

**Çoklu Seçim:** Bilindiği gibi Detay Koşul Kayıtları, Koşul Sabit Kayıtlarında belirlenen Koşul Rapor Koduna göre yapılmaktadır.

Örneğin, Detay Koşul Kayıtları stokların sahip olduğu grup koduna göre yapılacaksa, ilgili koşul kodu için Koşul Sabit Kayıtlarında Koşul Rapor Kodu olarak Stok Grup Kodu seçilmektedir. Böylece koşulun, sadece belirtilen grup koduna sahip stoklar için geçerli olacağı belirlenmektedir.

Ancak bazı durumlarda koşulun geçerli olacağı stokların tek bir sahaya göre (örneğin grup kodu) belirlenmesi mümkün olmamaktadır. Bu yüzden, Detay Koşul Kayıtlarının geçerli olacağı stokların, birden fazla koşul rapor kodu ya da stok kartında bulunan diğer sahalara göre belirlenebilmesi için **Çoklu Seçim** seçeneği işaretlenmelidir.

Bu seçenek işaretlenerek tanımlanan koşul kodları için Detay Koşul tanımlanırken, Geçerli Stoklar başlıklı sayfada koşulun hangi stoklar için geçerli olduğunun belirlenmesi gerekecektir. Geçerli stokların nasıl belirlendiği dokümanın Detay Koşul Kayıtları bölümünde anlatılmaktadır.

![](../_assets/a7b88f9e9f2be5ea856e.png)

Koşul Sabit Kayıtlarında yapılan değişiklikler sonucunda ekran daha düzenli hale getirilmiştir. Koşul Kartı sayfasında bulunan seçeneklerden bir kısmı yeni eklenen Koşul Kartı-2 sayfasına taşınmıştır.

**Detay Koşul Kayıtları**

**Detay Koşul Bilgileri**

![](../_assets/6ad70865a951bbc23e25.png)

**Vade** **Kodu:** Vade bazında iskonto uygulaması için eklenen sahadır. Bu sahanın kullanımı hakkında detaylı bilgiyi dokümanın Vade İskonto Kayıtları bölümünde bulabilirsiniz.

**Fiyat** **Miktar** **Aralığı:** Sipariş, irsaliye ve fatura kayıtlarında girilen stok miktarına göre fiyat listesindeki kaçıncı fiyatın kullanılacağının önceden belirlenmesi ve bu fiyatın program tarafından getirilmesi için kullanılan bölümdür.

Detay Koşul Kayıtlarında yukarıdaki ekrandaki gibi bir aralık tanımlandığında, detay koşulun geçerli olduğu stok için faturada girilen miktar 10' dan küçük ise 1. liste fiyatı, 10 - 20 arasında ise 2. liste fiyatı, 20 – 30 arasında ise 3. liste fiyatı, 30' dan büyük ise de 4. liste fiyatı program tarafından getirilecektir.

Detay Koşul kaydı sırasında Fiyat Miktar Aralığı girilmesi halinde, Liste Fiyatı sahası pasif olacaktir. Bunun sebebi, faturaya getirilecek olan fiyatın, Liste Fiyatı sahası yerine girilen miktar aralığına göre belirlenecek olmasıdır.

**Fiyat Grubu:** Özel Fiyat Sisteminin kullanıldığı durumlarda, cari için geçerli fiyat grubu Cari Hesap Kayıtlarındaki Cari Kart 2 sayfasında bulunan Fiyat Grubu sahasında belirtilmektedir. Fiyat Grubu sahası Detay Koşul Kayıtlarına da eklenmiştir. Bu durumda, carilerin hangi fiyat listesi ile çalışacağı belirlenirken ilk önce fatura kaydında girilen koşula ait Detay Koşul Kayıtlarındaki tanımlamaya bakılacaktır. Ancak burada herhangi bir bilgi bulunmuyorsa, Cari Hesap Kayıtlarında girilen Fiyat Grubu bilgisine göre işlem yapılacaktır.

**Ölçü Birimi:** Satış Fatura Parametrelerinde bulunan "Farklı birimlerden mal çıkışı yapılsın mı" parametresinin işaretli olması halinde, fatura kaydı sırasında stoka ait farklı ölçü birimlerinden çıkış yapılabilmektedir. Detay koşulun geçerli olduğu stokların kartlarında girilmiş farklı ölçü birimleri olması halinde, fatura kaydı sırasında, detay koşulda seçilen ölçü birimi program tarafından getirilecektir. Bu sahada 5 adet ölçü birimi desteklenmektedir. Bunlar Stok Kartı Kayıtları/ Ölçü Birimi sayfasında Sabit Tanımlamalar bölümünde bulunan 3 ölçü birimi ile Çoklu Ölçü Birimi bölümünde tanımlanarak Birim Seçimi sahalarına girilmiş 2 ölçü birimidir.

**Detay Koşul Bilgileri-2**

![](../_assets/fb7a13622e0a81ac5651.png)

**Fire Hangi İsk.:** Bazı sektörlerde, malların nakliyesi sırasında ağırlıklarında azalma olmaktadır. Örneğin, tavuk veya et gibi ürünlerin nakliyesi sonrasında, nakliye süresinde yaşanan su kaybından dolayı ağırlıkları azalmaktadır. Bu gibi durumlarda oluşan firenin, faturada iskonto olarak gösterilmesi için kullanılan sahadır. Oluşan firenin faturada kaçıncı satır iskontosuna yazılacağı bu sahada belirlenmektedir.

**Fire İsk. Tipi:** Fire iskontosunun takip edileceği iskonto tipinin girileceği alandır. Buraya girilecek iskonto tipinin daha önceden İskonto Tip Kayıtlarından tanımlanması gerekmektedir.
Fire İskontosunun uygulanabilmesi için burada yapılan tanımlamalar dışında başka tanımlamaların da yapılması gerekmektedir. İlk olarak Yardımcı Programlar/ Özel Parametre Tanımları menüsünde aşağıdaki 2 tanımlamanın yapılması gerekmektedir. Bu tanımlama ile fire iskontosunun cari ve stok kartlarındaki hangi sahadan kontrol edileceği belirtilmektedir.

**Grup Kodu: FATURA Anahtar: FIRECARISAHA Değer: KULL1N**

**Grup Kodu: FATURA Anahtar: FIRESTOKSAHA Değer: KULL1N**

Özel parametrelerde değer sahalarında KULL1N girilmiştir. Bu, fire iskontosun kullanıcı tanımlı sahalardaki 1. sayısal sahaya girileceği anlamına gelmektedir. Ancak istenirse kullanıcı tanımlı sahalardaki farklı bir sayısal saha da belirlenebilir.

Daha sonra stok ve cari kartta bulunan Kullanıcı Tanımlı Sahalar sayfasında, Özel Parametrede belirtilen sahaya, stok ve cari için fire iskonto oranları girilmelidir. Şöyle ki, fire uygulamasında stoka ait fire oranı sabit iken carilere göre değişiklik gösterebilir. Bunun sebebide fire oranının carilerin uzaklıklarına göre değişkenlik göstermesidir. Yakın mesafedeki cariye mal gönderilirken fire daha az olmakla birlikte, daha uzak cariye gönderilen malda daha fazla fire olacaktır. Dolayısıyla stok kartlarına girilen fire oranı ve cari karta girilen fire oranı beraber dikkate alınacak ve fatura kaydında, detay koşulda belirlenen iskonto sahasına, bu iki oranın çarpımı getirilecektir. Örneğin, nakliyesi sırasında fire oluşan stoka ait fire iskontosu oranı 2 olsun. Bu oran özel parametrede belirtilen kullanıcı tanımlı sahaya girilecektir. Ayrıca mesafe olarak biri yakın biri uzak 2 müşteri olsun. Fire iskontosunun, yakın olan müşteri için 3, uzak olan müşteri için de 5 olması halinde, bu oranların cari karttaki kullanıcı tanımlı sahalara girilmesi gerekecektir. Böylece, mesafesi yakın olan cariye ilgili stok için fatura kaydı girildiğinde fire için detay koşulda belirtilen iskonto sahasına 6(2\*3) getirilecektir. Ancak uzak olan müşteriye aynı stok için getirilecek iskonto oranı 10 (2X5) olacaktır.

**Geçerli Stoklar**

Geçerli Stoklar ekranı, Koşul Sabit Bilgilerinde, ilgili stok için yapılan tanımlamada Çoklu Seçim işaretlenmesi halinde gelmektedir. Burada, tanımlanan detay koşul bilgilerinin hangi stoklar için geçerli olduğu belirlenmektedir.
Örneğin, tanımladığınız koşulun, sadece Grup Kodu 6 olan stoklar için geçerli olmasını istemeniz halinde, Koşul Sabit Kaydı sırasında Koşul Rapor Kodu olarak Stok Grup Kodu seçmeniz ve ilgili grup kodunu Detay Koşul Bilgileri sahasında belirtmeniz yeterli olacaktır.

Ancak koşulun geçerli olacağı stokları belirlerken birden fazla sahaya ihtiyaç duyuluyorsa Koşul Sabit Kayıtlarında Çoklu Seçim işaretlenerek Geçerli Stokalar sayfasında birden fazla saha için kısıt verilebilir.

![](../_assets/24082d7994cd2794685e.png)

Örneğin, tanımlanan koşulun, Grup Kodu 6 ve Kod-1'i K1 olan stoklar için geçerli olması isteniyorsa yukarıdaki ekrandaki gibi bir tanımlama yapılması gerekmektedir.

Bu ekranda, Saha Adı üzerinde iken klavyede **boşluk çubuğu**' na basıldığında bilgi girişi yapılması mümkün olacaktır. Örneğin Grup Kodu için kısıt verilmesi isteniyorsa, Saha Adı sütununda boşluk çubuğuna basılması ve aşağı ok tuşuna basarak Grup Kodu sahasının seçilmesi gerekmektedir. Daha sonra **Enter** tuşuna bastığınızda girilen bilgi saklanacak ve sağdaki hücreye geçilecektir. Bu bölümde birden fazla saha için kısıt verilecek ise klavyede bulunan **Insert** tuşuna basarak yeni satır ekleyebilirsiniz. Eklenmiş bir satırın silinmesi için de, ilgili satırı seçtikten sonra yine klavyedeki **Delete** tuşuna basmanız gerekmektedir.

Klavye tuşları yerine ilgili satır üzerinde farenin sağ tuşu ile açılan menü yardımıyla Satır Ekleme, Satır Silme, Araya Satır Ekle, Temizle, Aşağı Kaydır ve ekranın aşağısında verilen kısıtı gösteren cümlenin gösterilmesi için Cümleyi Göster seçenekleri yer almaktadır.

![](../_assets/17d8942a6741f397645f.png)

Detay koşul kayıtlarındaki, çoklu seçim uygulaması ile, bir stok için, aynı koşul koduna ait birden fazla detay koşul kaydı geçerli olabilmektedir. Örneğin bir detay koşul kaydında, grup kodu 'A' olan stoklar, diğer detay koşul kaydında ise, kod-1'i '001' olan stoklar dahil edildiğinde, grup kodu 'A' olup da kod-1'i '001' olan bir stok, bu durumda her iki detay koşul kaydı için geçerli olacaktır. Ancak faturalama belgelerinde, program ilk sıradaki detay koşul kaydına göre işlem yapacaktır.

**Mal Fazlası**

Yapılan detay koşul tanımlamasının geçerli olduğu stoklar için mal fazlası verilecek ise kullanılacak bölümdür.

Mal Fazlası Stok Kodu belirlenirken, Mal Fazlası Stok Kodu sahasına mal fazlası olarak verilecek stok kodunun girilebilir. Bu durumda koşulun geçerli olduğu stokların satışında, bu sahaya girilen stok mal fazlası olarak verilecektir.
Mal fazlası için verilen stoklar belli bir grup ürün ise bu durumda, **Mal Fazlası Grup Mu** seçeğini işaretlenip Geçerli Mal Fazlası Stoklarının belirlenmesi gerekir. Bunun kullanım amacını bir örnek ile açıklayalım. Mesela makarna ve salça satan bir firma, makarna grubundan alım yapan müşterilerine salça grubuna ait ürünlerden mal fazlası veriyor olsun. Bu durumda koşul tanımlamasını makarna grubunu kapsayacak şekilde yapmalıdır. Daha sonra da Mal Fazlası Grup Mu seçeneğini işaretleyerek **Geçerli Stoklar** sahasında Salça grubuna ait stokları için kullanılan rapor kodlarına göre kısıt vermelidir.

![](../_assets/1010219171e95a9b5933.png)

Ek Koşul Kayıtları

Ek koşul kayıtları, belli bir koşul kodunun kullanımında, ayrıcalıklı davranılması gereken durumlar için kullanılır. Ek koşul kayıtları, daha önce verilen Cari Kod, Cari Tip, Koşul Kodu ve cari rapor kodları için geçerli olabiliyordu. Ancak bu bölümde yapılan değişiklikler sonucunda ek koşulun geçerli olduğu durumların belirlenmesinde Proje Kodu, Plasiyer Kodu, Faturalama belgesi Özel Kod-1/2, Faturalama belgesi Açıklama ve Teslim Cari kodlarının da kullanılabilmesi sağlanmıştır. Ayrıca kod türlerinde bulunan Çoklu Seçimin işaretlenmesi halinde, burada bulunan sahalardan farklı sahalar için de tanımlama yapılabilmektedir.

Kod Türü sahasında Çoklu Seçim seçeneğinin işaretlenerek tanımlanan ek koşul bilgisinin hangi durumlar için geçerli olacağı, Geçerli Cariler sayfasında belirlenmelidir. Saha adı bölümünde gelen sahalar üzerinden kısıt tanımlanarak, ek koşulun geçerli olduğu durumlar belirlenebilir. Bu sayfanın kullanımı Detay Koşul Kayıtlarındaki Geçerli Stoklar ile aynı olduğundan burada tekrar edilmeyecektir.

Kod Türü olarak Çoklu Seçimin işaretlenmesi halinde bu sayfada gerekli tanımlamalar mutlaka yapılmalıdır. Aksi takdirde ek koşul tanımlaması yapılamayacaktır.

Cari Parametre Kayıtlarına eklenen "Koşul Politika Tanımlaması Yapılacak" parametresinin işaretlenmiş olduğu durumlarda, ek koşulun ne şekilde çalışacağı, İlave Şekli ve İskonto Toplam Şekli sahaları aracılığıyla belirlenmeyeceğinden dolayı, Ek Koşul Kayıtlarındaki bu sahalar pasif olacaktır.

![](../_assets/db1872fa80b9900332c6.png)

![](../_assets/d764344385748fcdd43d.png)

**Vade Bazında İskonto Belirleme**

Koşul uygulamasında, önceden mevcut olan Vade İskontosu veya Faiz Uygulaması ile, fatura modülünde, ilgili koşula kodu verildiğinde, vadesinden önce yapılacak ödemeler için vade iskontosu, geç ödemeler için de faiz uygulaması desteklenmekteydi. Ancak bu uygulamada, program koşul genel kayıtlarında verilen sabit bir iskonto/faiz oranını baz alarak, belgedeki vade gününe göre, iskonto/faiz oranı hesaplamaktaydı. Oysa, uygulamada, farklı vade günleri için iskonto oranları, hesaplama yöntemiyle değil, kullanıcı tarafından verilmek istenmektedir. Fatura/ İrsaliye/ Sipariş kayıtlarında satır bazında girilen vade günlerine göre, satır iskontosunun program tarafından getirilmesi amacıyla kullanılabilecek uygulamadır.

Bu uygulamanın desteklenmesi için Cari modülde Koşul Kayıtları altına **Vade** **İskonto** **Kayıtları** eklenmiştir. Burada bulunan sahaların açıklamaları ve kullanımı aşağıdadır.

Vade İskonto Kayıtları

Vade İskonto Kaytıları iki bölümden oluşmaktadır.

**Vade İskonto Kodları**

![](../_assets/5f95cb64d4ccd3136feb.png)

**Vade** **Kodu:** Vade bazında iskonto uygulaması için tanımlanacak vade kodunun girileceği alandır. Bu kod daha sonra Detay Koşul Kayıtlarında kullanılacaktır.

**Vade** **Açıklama:** Tanımlanan Vade Koduna ait açıklamanın girileceği alandır.

Vade kodu bu sayfada tanımlanarak kaydedildikten sonra, Vade İskonto Değerleri sayfasına geçilerek, satır bazında girilen vade günü için uygulanacak satır iskontosu oranı belirlenecektir.

**Vade İskonto Değerleri**

Vade Kodları sayfasında tanımlanan kodlardan biri seçildikten sonra, vade bazında kullanılacak iskonto oranın tanımlanacağı alandır.

![](../_assets/cf2635d3fed025b58201.png)
Satır bazında girilen vade gününe göre, satır iskontosunun alacağı oranlar bu bölümde tanımlanmalıdır.
Detay koşul kayıtlarında, detay koşul bazında kullanılmak istenen vade iskonto kodu ilgili sahaya girilmelidir.

Vade Kodunun Koşul Kaydında Kullanımı

Tanımlanan vade kodlarının kullanılabilmesi için Detay Koşul Tanımlamalarında girilmesi gerekmektedir.

Bunun için Detay Koşul Kayıtlarına eklenen sahaların açıklamaları şöyledir;

![](../_assets/a6ae6638942a3b2de641.png)

**Vade** **Kodu:** İlgili detay koşul kullanıldığında geçerli olacak vade kodudur. Buraya girilecek kodun daha önceden Vade İskonto Kayıtlarında tanımlanmış olması gerekmektedir.

**Vade Hangi İsk.:** Faturada satır bazında girilecek vade gününe göre getirilecek satır iskontosunun kaçıncı iskontoya yazılacağının belirlendiği alandır. Yukarıdaki ekranda bu sahaya 1 girilmiştir. Yani vade iskontosu için 1. satır iskontosu kullanılacaktır. Bu bölümde dikkat edilmesi gereken nokta, burada belirtilen iskonto sahasının farklı bir uygulama için kullanılmaması gerektiğidir. Örneğin, yukarıdaki tanımlamada 1. satır iskonto oranı 0 (sıfır) geçilmiştir.

**Vade** **İsk.** **Tipi:** Vade iskontosu için hangi iskonto tipinin kullanılacağının belirlendiği sahadır. Bu sahaya İskonto Tip Kayıtlarında tanımlanan iskonto tiplerinden biri girilebilir.

Fatura modülündeki kullanım

![](../_assets/7a204f02dc02833d1846.png)

Bu tanımlamaları yaptıktan sonra satır bazında girilen vade günü için belirlenen iskonto oranı program tarafından getirilecektir. Yukarıdaki örneğe göre, vade iskonto tanımlamalarında 15 vade günü için %10 satır iskontosu tanımlanmıştır. Ayrıca Detay Koşul Kayıtlarında da vade iskontosunun 1. satır iskontosuna yazılacağı belirlenmiştir.

Bu durumda fatura kaydı sırasında 1. satır iskontosu boş geçilerek Vade Günü sahasına uygulanacak vade günü girilmelidir. Satır iskontosu vade günü girildikten sonra program tarafından getirilecektir.

Dikkat! Program sadece Vade İskonto Kayıtlarında girilen vade günlerine ait iskontoları getirecektir. Mesela 15 gün için %10, 30 gün için %8 iskonto tanımlandığında, fatura kaydında vade günü olarak 17 girildiğinde iskonto getirilmeyecektir. Bunun sebebi Vade İskonto Kayıtlarında 17 gün için iskonto oranı verilmemiş olmasıdır.

**İleri Koşul Uygulaması**

Bilindiği gibi, Ek Koşul Kayıtlarında yapılan tanımlamalar sonucunda, fatura belgeleri kayıtları sırasında, birden fazla detay koşul kaydı, işleme alınabilmektedir. Bu detay koşulların nasıl işlem göreceği ise, ilave şekli ve iskonto toplam şekli (Sıfır değerler dahil üstüne yaz, Normal toplam al gibi) seçeneklerinde belirlenmekteydi. Ancak koşul tanımlamalarında yapılan yenilikler ile mevcut politikalardan farklı politikaların tanımlanabilmesi sağlanmıştır.

**Koşul Tip Kayıtları**

Koşul Sabit Kayıtları üstünde bir gruplama oluşturulması ve Koşul Politika Tanımlamasında burada belirlenen önceliklere göre politika tanımlanabilmesi amacıyla kullanılmaktadır.

![](../_assets/4b7ae821ce77c7a50391.png)

**Koşul** **Tipi:** Tanımlanan tipe ait kodun girileceği alandır.

**Açıklama:** Tanımlanan koşul tipine ait açıklamanın girileceği sahadır.

**Önceliği:** Tanımlanan koşul tipinin önceliğinin girildiği alandır. Bu bölümde tanımlanan koşul tiplerinin Koşul Sabit Kayıtlarında sorgulanan Koşul Tipi sahasına girilmesi ile, hangi koşulun hangi önceliğe sahip olduğu belirlenmektedir.

**Birden fazla koşul olduğunda sorulsun:** Koşul politika Kayıtlarında belirlenen politikaya göre, önceliği aynı olan birden fazla koşul geçerli olduğunda, hangisinin kullanılacağının fatura kayıtları sırasında sorgulanması için kullanılacak sorgulamadır. Bu uygulama şu an için desteklenmemektedir.

Koşul Tip Kayıtları şube ve işletme bazında tanımlanabilmektedir.

Ek Koşul Kayıtlarında bulunan politikalardan farklı olarak belirlenen önceliklere göre tanımlama yapılabilmesi için Cari Parametre Kayıtlarına eklenen "**Koşul Politika Tanımlaması Yapılacak**" parametresinin işaretlenmesi gerekmektedir.

Böylece Koşul Kayıtları altında Koşul Politika Kayıtları ekranı gelecektir.

![](../_assets/6c8ee745a9151a975277.png)

**Koşul Politika Tanımlaması**

Bu bölümde yazılacak Visual Basic script' i ile, Ek Koşul Kayıtlarında İlave Şekli ile uygulanabilecek politikalardan daha geniş kapsamlı politika tanımlaması yapılabilir.

Belgelerde, Koşul Politika Tanımlamasında belirlenen vade günü, iskonto ve fiyat gibi bilgilerin getirilmesi isteniyorsa, bu bilgilerin bulunduğu detay koşulların mutlaka Ek Koşul Kayıtları yapılmalı ve bu ek koşulların belge üzerindeki cari kod için geçerli olması gerekmektedir.

Bunu bir örnek ile açıklayalım. Bir firmanın tanımlı olan detay koşulları aşağıdaki gibi olsun:

|  |  |  |
| --- | --- | --- |
| Koşul Kodu | Koşul Kapsamı | Satır İsk 1 |
| K10 | Türkiye Geneli Kampanya | 10 |
| K20 | Ege Bölgesi Kampanyası | 12 |
| K30 | Yaz Kampanyası | 5 |

Ayrıca bu koşul kayıtlarının tamamı, Ek Koşul Kayıtları bölümünden İzmir'de bulunan bir müşterisi için tanımlanmış olsun. İzmir'de bulunan bu müşteriye Haziran ayında mal satışı yapıldığında her üç koşul da geçerli olacaktır. Koşul politika tanımlamaları ile bu koşullardan hangilerinin ne şekilde kullanılacağı belirlenecektir.

Aşağıdaki ekranda yapılan politika tanımlaması sonucunda, geçerli koşulların 1. satır iskontolarının ortalaması hesaplanarak belgeye yine 1. satır iskontosu olarak getirilmesi sağlanmıştır. Buna göre, yukarıda verilen örnekteki müşteriye ait belgelerde 1. satır iskontosu oranı 9 ((10+12+5)/3) gelecektir.

![](../_assets/355cfebe46b97c8e0248.png)

Yukarıda tanımlanan script, fatura belgesinin her satırında, bir program parçacığı gibi, baştan sona çalışacaktır. Scrit içerisinde kullanılan "DetSayısı" ile, Detay Koşul Kayıtlarında tanımlanmış ve ilgili cari için ek koşul olarak girilmiş koşul sayısı ifade edilmektedir. Ek koşullarla belirlenmiş olan bu detay koşullar tümü, program parçacığı içerisinde aktiftir ve "KosulDetaylar" dizisinin içinde bulunmaktadır. Script içinde kurulan döngü ile, bu ek detay koşullar ("KosulDetaylar" dizisi), baştan sona kontrol edilmektedir. Bu döngü içinde, KosulDetaylar dizisinin her bir elemanı, "AktifDetay" değişkenine atanmaktadır. Aktif detay olarak atanan detay koşulun, 1. iskonto oranı "Isk" değişkenine eklenmiştir. Böylece tüm ek detay koşulların 1. iskonto oranları toplamı alınmış oldu. Döngü sonunda, belgede girilen koşulun da 1. iskonto oranı, bu toplama eklenmiştir. Bunun sebebi belgede girilmiş olan koşulun, ek koşul olarak tanımlanmış olsa dahi, KosulDetaylar dizisinin içinde bulunmamasıdır.

Yazılan script ile, belgede girilen koşul kodu için belirlenen 1. satır iskontosu ve bu belgede girilen cariye Ek Koşul Kayıtlarından bağlanmış koşullar için detay koşulda belirlenen 1. satır iskontoları toplanmıştır. Sonuçta da, bulunan değer, toplam geçerli koşul sayısına bölünerek ortalama 1. satır iskontosu oranı bulunmuştur.

Koşul Politika Tanımlamalarında kullanılabilecek araç çubukları şunlardır:

![](../_assets/103dbc3e0c2030906f8b.png) **NesneTarayıcısı:** Koşul politika tanımlaması esnasında kullanılabilecek nesnelerin izlenebilmesini sağlayan butondur.

Bu butona basıldığında Nesne Tarayıcısı başlıklı bir ekran gelecektir. Burada politika tanımlarken kullanabileceğiniz sahaları bulabilirsiniz. Koşul Politika Tanımlamasında, Detay Koşul ve Ek koşul Kayıtlarında bulunan sahaların bir çoğu kullanılarak politika tanımlaması yapılabilir.

![](../_assets/c53398176cfaaee5ed2a.png)

**![](../_assets/e65add2604194132d858.png) Kod İçeriği (Ctrl-Space):**

Script editor içerisinde kullanılabilen nesnelerin yardım pencerelerini getirir. Şöyle ki, script editorde nesne ismi yazılıp yanına "." Nokta işareti konup, ctrl-space tuşlarına basıldığında, ya da araç çubuğundan bu fonksiyon çağrıldığında, nesnenin içerdiği sahalar, bir pencerede gösterilecek ve sahaların içinden seçim yapılabilecektir.

![](../_assets/9287ace174f29169a502.png)

**![](../_assets/6182cf8d0617cc0a2797.png) Kod Tamamla (Kod içeriği aktif ise Enter):**

Script editor içerisinde, nesne ismi yazılıp, kod içeriği penceresi aktif iken, kullanılmak istenen saha isminin başlangıç harf(ler)i yazıldığında, kod içeriği imleci ilgili sahanın üzerine gidecek ve Enter'a basıldığında ya da bu fonksiyon çalıştırıldığında, kullanılmak istenen sahanın tam adının otomatik getirilmesi sağlanacaktır.

**![](../_assets/808d06c089ccf602d842.png) Satıra Git:**

Koşul Politika ekranı üzerinde istenilen satıra gitmek için kullanılan butondur. Bu butona basıldığında açılan ekranda, imlecin hangi satıra gitmesi istendiği sorgulanacaktır.
Bul/ Sonraki Arama/ Önceki Arama/ Değiştir: Bu butonlar yardımıyla ekranda girilen script içinde istenilen karakter dizisi aratılması (Bul), birden fazla yerde geçmesi halinde sırayla her birinin üzerine gidilmesi (Sonraki Arama/ Önceki Arama) ya da script içinde geçen herhangi bir değerin farklı bir değerle değiştirilmesi (Değitir) mümkündür.

**![](../_assets/f0418f8cfb03a1ddb302.png) Yükle/ Kaydet:**

Bu fonksiyonlar, koşul politika tanımı editoründe aktif değildir.
