---
title: "Dinamik Depo Uygulaması"
page_id: "66238404"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Dinamik Depo Uygulaması"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Dinamik Depo Uygulaması"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWQxYjFiY2MyLTM5ZTYtNGE4YS1hZjdkLTM3YTlkZmZhMmM1NiZsaW5rPWY5ZjM0ZWVjLWI0Y2YtNDQxYy1hZjFiLTYxMjg5YTYxZjZhMyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=d1b1bcc2-39e6-4a8a-af7d-37a9dffa2c56&link=f9f34eec-b4cf-441c-af1b-61289a61f6a3&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "dinamik-depo-uygulamasi_82576708_66238404.html"
source_version: "2022-11-03T09:50:44.887+03:00"
source_bytes: 477705
fetched_at: "2026-09-13T04:26:15+00:00"
generator: "netsis-scraper 1.0.0"
---
# Dinamik Depo Uygulaması

Dinamik Depo Uygulaması ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Depo içinde malların, tanımlı parametrelerin yardımıyla, kolayca yerleştirilmesini ve çıkış işlemi sırasında kolayca toplanmasını sağlayan modüldür. Bu modülde, hammadde veya mamullerin depo içinde izlenebilirliği, satınalma, yerleştirme, toplama ve gönderme işlemlerinin kolayca yapılabilmesi ve seri takibi ile malın depoda izlediği tüm yollara erişilebilmesi sağlanmıştır.
Mallar hacimlerine göre raflarla eşleştirilebilir. Akıllı hücre kodlaması ile malların toplanmasında ve yerleştirilmesinde çok kullanılan FIFO, LIFO, Ağırlık önceliği veya Frekans gibi metodlar uygulanabilir. Parametreler yardımıyla depo içindeki kurallar katılaştırılıp, kolaylaştırılabilir. Audit raporları ile, varsa depo-stok uyumsuzluğu izlenebilir. Dinamik depo uygulamasının hayata geçirilebilmesi için mutlaka *Lokal* *Depo* uygulamasının kullanılması gerekmektedir. Bunun nedeni dinamik depo takibinin yapılacak olduğu ambar(lar)ın, bir lokal depo olarak tanımlanma zorunluluğu olmasıdır. Ayrıca, dinamik depoda kullanılacak olan lokal depo kodları açılırken, Depo Tanımlama bölümündeki "Lokasyon Takibi Yapılacak Mı" parametresi mutlaka işaretlenmelidir.
![](../_assets/84ec500b9179b0431e9e.png)

#### DİNAMİK DEPO PARAMETRE KAYITLARI

![](../_assets/0511b61d2b6cad005e2e.png)
**Seri Bilgisi Depoda Sorulsun mu:** Stokta seri/lot takibi yapılıyor ise, fatura modülündeki giriş ve çıkış belgelerinde, seri/lot numaraları sorgulanır. Stok seri bilgilerinin, bu belgeler üzerinde sorgulanmayıp, dinamik depo modülünde, yerleştirme veya toplama sırasında, sorgulanması isteniyor ise bu parametre işaretlenmelidir. Aksi halde stok serileri, dinamik depo modülünde değil fatura modülünde sorgulanacaktır.
**İrsaliyeler İle Kayıtlar Tutsun mu:** İrsaliye/ Faturalardaki miktarlar ile depoya yerleştirilen/ toplanan miktarların eşit olması kontrolünün yapılması için bu parametre işaretlenmelidir. Parametrenin işaretlenmemesi durumunda miktar kontrolü yapılmayacaktır.
**Ürün Hacim Grubu Kontrolü Yapılsın mı:** Dinamik depo modülünde mallar hacimlerine göre gruplanır ve raflara hangi hacim gruplarındaki malların yerleştirilebileceği tanımlanır. Bu parametre işaretlendiğinde, stok kartlarında girilen hacim kodları kontrol edilerek, stokların ait olmadığı bir raf grubuna yerleştirilmeleri engellenecektir. Parametre işaretlenmemiş ise stoklar, farklı hacim gruplarına yerleştirilebilecektir. Örneğin; A rafına küçük hacimli ürünlerin, B rafına büyük hacimdeki ürünlerin yerleştirilmesinin planlandığını düşünelim. Bu parametre işaretlenmiş ise küçük hacimli ürünler B rafına hiçbir zaman yerleştirilemez. Aksi halde, istenilen rafa yerleştirilebilir.
**Bir** **Hücreye** **Aynı** **Mal** **Grubu Ürün** **Yerleştirilsin** **mi:** Bir hücreye yeni bir mal yerleştirilirken, aynı hücreye daha önceden yerleştirilen ürünün mal grubuyla aynı olması isteniyor ise bu parametre işaretlenmelidir. Eğer bir hücreye farklı mal grubu ürünlerin yerleştirilebilmesi isteniyor ise işaretlenmemelidir. Örneğin; A rafının 1 numaralı hücresine makarna grubu bir ürün yerleştirilmiş olsun. Parametre işaretlenmiş ise 1 numaralı hücreye makarna grubu dışında bir ürün yerleştirilemez.
**Kapasite** **Kontrolü** **Yapılsın** **mı:** Bu parametre işaretlendiğinde, tanımlı raf hacmi kontrol edilecek ve kapasitenin üstünde yerleştirme yapılmasına izin verilmeyecektir. Parametre işaretlenmemiş ise kapasite kontrolü yapılmayacaktır.
**Bakiye** **Kontrolü** **Yapılsın** **mı:** Çıkış işlemlerinde, hücrede olmayan veya hücrede olan miktarlardan fazla çıkış yapılması istenmiyor ise bu parametre işaretlenmelidir. Parametre işaretlenmemiş ise bakiye kontrolü yapılmayacak ve hücrede olmayan ürünlerin çıkışına izin verilecektir.
**Brüt/Net Kg. Takibi Yapılacak mı:** Tartılı ürünlerde, ürünün birlikte tartıldığı darası düşülerek net miktarların hesaplanması ve bu net miktarların depo kayıtlarına işlenmesi istendiğinde işaretlenmesi gereken parametredir. Bu parametre işaretlendiğinde, depo hareketlerinde, miktar bilgisi girildikten sonra gelen ekranda netten brüte ya da brütten nete hesaplatma yapılabilmektedir.

#### GRUP KODU KAYITLARI

![](../_assets/3ebc937c67ec1722926f.png)
Hücre gruplarının tanımlandığı bölümdür. Hücreler, ebatlarına göre çeşitlilik gösterebilirler. Dolayısıyla, her grup ayrı ayrı tanımlanmalıdır.
**Grup** **Kodu:** Maksimum 15 karakter uzunluğunda, grup kodlarının girileceği sahadır.
**Açıklama:** İlgili grup kodunun açıklamasının/ adının girileceği sahadır.
**En/****Boy/****Yükseklik:** İlgili grubun bir hücresi için en, boy ve yükseklik bilgisinin rapor amaçlı girilebileceği sahadır.
**Hücre** **Adedi:** Aynı gruptan kaç hücre olduğu bu sahaya girilmektedir.

#### HÜCRE TANIMLAMA

![](../_assets/bc37157f873637f9afb6.png)
Malların depolandığı yerdeki, malların yerleştirildiği bölmelerin yani hücrelerin tanımlanacağı bölümdür. Hücre kodlamasının dikkatli yapılması gerekmektedir. Çünkü hücre kodlarının sıralanması sonucu malların yerleştirilmesi ve toplaması yapılmaktadır. Depo yerleşiminde şöyle düşüncelerle hareket edilebilir; örneğin: en hızlı şekilde mal toplanması ve yerleştirilmesi için en çok hareket gören mallar, en yakın raflara yerleştirilmeli, daha nadir hareket gören mallar uzak raflara yerleştirilmelidir. Bu düşünce ile hareket edilecekse en yakın raflar, en küçük kodlara sahip olmalı ve en sık kullanılan mallar bu raflara yerleşecek şekilde tanımlama yapılmalıdır. Aynı şekilde uzak raflar kod sırasında daha büyük kodlara sahip olmalıdır. Benzer bir örnek; ağır malların öncelikle toplanması, daha hafif malların daha üste gelmesi gerekliliğidir. Bu durumda, ağır malların depolandığı raflar, kod sırasında daha küçük koda sahip olmalı, hafif malların koyulduğu raflar ise daha büyük koda sahip olmalıdır. Hücre kodlarını tanımlarken depo içinde hangi tercihin öncelikli olduğuna karar vermek gerekiyor. Çünkü kodlamaya göre toplama ya da yerleştirme işlemlerinde hız kazanılabilir. Hücre kodları, tüm depolar ve şubeler bazında tektir. Bu nedenle, birden fazla depo kullanan veya şube kullanan yerlerde hücre kodlarının standardı buna göre belirlenmelidir. Örneğin; Depodaki her bir koridora A,B,C gibi isim verildiğini düşünelim. Koridorda sağda
bulunan hücreler için 1, soldakiler için 2 verilsin. Aynı zamanda, aynı koridordaki en alt raf için 0, 1. kat için 1, 2. kat için ise 2 tanımlansın. Hücrelerin yan sıra numaraları ise artan sayıda 1, 2, 3, 4 gibi verilsin. Bu durum A koridorundaki, sağdaki raf, 1. kattaki 2. sıradaki hücre için kodlama A11-2 olmalıdır.
**Hücre Kodu:** Maksimum 15 karakter uzunluğunda, hücre kodlaması yapılacak sahadır.
**Grup** **Kodu:** Tanımlanan hücrenin hangi hücre grubuna ait olduğu bu sahada girilmelidir.
**Depo** **Kodu:** Bu saha boş geçilemez. İlgili hücrenin tanımlı olduğu, yani içinde bulunduğu lokal depo kodu bu sahaya girilmelidir. Depo kodu sahasındaki rehberde, lokal depo tanımlamada "Lokasyon Takibi Yapılsın Mı" parametresi
işaretlenmiş depolar listelenecektir. Örneğin; Firmanın lokasyon takip ettiği 2 ayrı depo olabilir. Her depoda ayrı ayrı hücre tanımlaması yapmak gerektiği için, tanımlanan hücrenin lokal deposu belirtilmelidir.

#### HACİM KODU TANIMLAMA

![](../_assets/179adfde7e04df642a1f.png)

Yerleştirilecek/toplanacak ürünleri hacimleri bazında gruplayabilmek, aynı hacme sahip ürünlerin hepsini ayrı ayrı tanımlamaktansa bir grup kodu ile birleştirmek için hacim kodlarının tanımlanacağı bölümdür. Bu kodlar, stok kartı kayıtlarındaki hacim kodu sahasına girilmelidir.

#### HACİM-GRUP KOD TANIMLAMA

![](../_assets/ad521fbe0e77bb257fe7.png)
Yerleştirilecek ürünler için hangi hacim gruplarının hangi hücre grubuna yerleştirilebileceğinin tanımlandığı bölümdür.
**Hacim** **Kodu:** Maksimum 8 karakter uzunluğunda, hacim kodlarının girileceği sahadır.
**Grup Kodu:** Tanımlanan hacim koduna sahip ürünlerin, hangi hücre grubuna yerleştirileceği bu sahada belirlenmektedir.
**Kapasite:** Tanımlanan hacme sahip olan ürünlerin, ilgili gruptaki bir rafa en fazla ne kadar yerleştirilebileceği bu sahada girilmektedir. Örneğin; Bu sahaya 150 girilmiş ve hacmi 50 olan ürünler yerleştirilecek ise en fazla 3 adet ürün yerleştirilebilir.

#### HÜCRE YERLEŞTİRME BİLGİLERİ

![](../_assets/6532a3a32bb9436db91e.png)

Daha önceden kaydedilen/ girişi yapılan ürünlerin hücrelere yerleştirilmesi için kullanılacak bölümdür. Bu bölümde, Fatura Modülünde Alış İrsaliyesi, Alış Faturası, Ambar Giriş Fişi ve Depolar Arası Transfer, Üretim seçenekleri kullanılarak girilen stoklar hücrelere yerleştirilmektedir. Yerleştirme işlemi bu ekran üzerinden yapılabildiği gibi girilen belgeler üzerinde kalemler bölümünde sağ klik Dinamik Depo İşlemleri seçeneğinden de yapılabilmektedir.
**Tipi:** Hangi bölümden girilen stokların hücrelere yerleştirileceği bu sahada seçilecektir. Örneğin, Alış Faturası ile girilen bir faturadaki kalemler, hücrelere yerleştirilecek ise bu bölümde Alış Faturası seçilmelidir.
**Belge** **No:** Tipi sahasında seçilen belge tipine göre, ilgili belgelerin listesi bu sahadaki rehber tuşu ile çağrılabilir veya elle yerleştirme yapılacak belge numarası girilebilir.
**Cari** **Kodu:** Girilen belge numarasındaki cari kod bu sahaya otomatik getirilecektir.
**Kalemleri** **Getir:** Bu tuşa bastığınızda ilgili belgede, lokasyon takibi yapılan depo kodu ile kaydedilmiş stok kalemleri grid ekranında listelenecektir. Gelen kalemlerin hepsinin yerleştirileceği düşünüldüğünden, tüm kalemler seçili
gelecektir (kırmızı). Eğer listelenen stok kalemlerinden yerleştirme yapmak istemedikleriniz var ise, ilgili kalem üzerinde fareniz ile çift tıklamanız yeterlidir.
**Diğer** **Sayfa:** Kalemleri getir tuşu kullanıldıktan sonra bu tuş aktif olacaktır. Bu tuşa basarak yerleştirme sayfasına geçebilirsiniz.
![](../_assets/f79da415102765ff01ab.png)
Seçilen stok kalemleri, yukarıda görüldüğü gibi yerleştirme ekranına gelecektir. Ekranda listelenen ürünlerden yerleştirilmek istenilenler, fare ile çift tıklanarak seçilmelidir. Seçilen ürünün yerleştirileceği hücre kodu ve net miktar girilmelidir. Bu bölümde eğer, parametrelerde "İrsaliyeler ile Kayıtlar Tutsun mu" parametresi işaretlenmiş ise seçilen stokların belgedeki miktarı ile yerleştirilen miktarın eşit olması koşulu aranacaktır. Aksi halde yerleştirme ekranından çıkılamayacaktır.
![](../_assets/dd7521aefbff44c3c281.png)
Eğer, Dinamik Depo Parametre Kayıtlarında, "Brüt/Net Kg. Takibi Yapılacak Mı" parametresi işaretlenmiş ise kayıt tamamlanmadan yukarıda görülen ekran açılacaktır. Yerleştirilecek/toplanacak tartılı mallar, içinde taşındıkları kutu, palet, el arabası vb. ile birlikte tartılıyor, fakat içindeki net miktar kadar mal yerleştiriliyor/toplanıyor ise, bu ekranda net miktar veya brüt miktar otomatik hesaplanabilir. Öncelikle, malların taşındığı kutu, palet, el arabası vb. eşyalar için birer stok kartı açılmalıdır. Bu stokların grup kodu sahasına 'DARA' ifadesi girilmelidir. Her birinin birim ağırlık bilgisi stok kartında tanımlanmalıdır. Ekranda stok kodu sahasında, daranın stok kodu ve tartım miktarının içinde kaç adet bulunduğu yazılmalıdır. Daranın miktarı kadar birim ağırlık değeri, brüt miktardan düşülerek net miktar otomatik bulunacak ve yerleştirme bu miktarlar için yapılacaktır.
Bu bölümde, yapılan yerleştirme kayıtlarının silinmesine izin verilmemektedir. Bu işlemin, İşlemler seçeneğinin alındaki Yerleştirme/Toplama İptali bölümü kullanılarak yapılması gerekmektedir. İstenirse yerleştirme işlemi sırasında düzeltme kaydı yapılabilir. Düzeltme kaydı için grid alanda kayıt üzerinde sağ klikte yer alan Düzeltme Kaydı seçeneği kullanılmalıdır.
![](../_assets/219980920d7f60c3be8d.png)
Girilen bir yerleştirme bilgisi yanlış ise ve düzeltilecek ise bu tuş kullanılabilir. Bu tuş kullanıldığında, ekranda düzeltme miktar bilgisi ve düzeltmenin giriş mi yoksa çıkış mı olduğu sorgulanacaktır. Düzeltme kaydı yeni bir yerleştirme hareketi gibi kaydedilecektir. Örneğin yanlışlıkla yapılmış bir giriş hareketi, aynı miktarda çıkış hareketi ile düzeltilebilir.
**Seri** **Bilgisi** **İzleme:** Ticari pakette, Genel Parametre kayıtlarındaki, "Seri Takibi Var mı" parametresini işaretleyerek işlem yapan firmalarda kullanılabilecek tuştur. Yerleştirme ekranında bu tuşa basıldığında, seçilen stok kalemine ait, seri numaraları bazında bakiye izlenebilecektir.
**Basım:** Bu seçenek ile ilgili depo fiş basımı gerçekleştirilebilir.
**Gönder:** Bu seçenek ile grid alandaki yerleştirme kayıtları excele ya da akıllı gride gönderilebilir, grafik hazırlanabilir. Yerleştirme sayfasının üst bölümündeki seçilen kalemler bölgesinde farenin sağ tuşu, aşağıdaki menüyü karşınıza
getirir.
![](../_assets/645ab2cb1160c62d2eb3.png)
**Hücre** **Bakiye** **Listesi:** Bu liste ile hangi hücrede, hangi stoklardan, kaç adet bulunduğu görülebilir. Seri Bilgisi İzleme ve Gönder seçenekleri grid alanda çalıştığı şekli ile çalışmaktadır.

#### HÜCRE TOPLAMA BİLGİLERİ

Satış veya ambardan çıkış durumunda, hücrelerden toplanması işleminin yapıldığı bölümdür. Bu bölümde yapılan işlemler, Hücre Yerleştirme bölümüyle aynıdır.
![](../_assets/72920cbe4576b8a18426.png)

#### HÜCRELER ARASI TRANSFER

Herhangi bir hücredeki ürünün, bir başka hücreye transferi amacıyla kullanılacak bölümdür.

![](../_assets/834931841bb8d032822f.png)
**Stok** **Kodu:** Başka bir hücreye transfer edilecek stok kodunun girileceği sahadır.
**Kaynak** **Hücre** **Kodu:** Transferi yapılacak stokun, yerleştirilmiş olduğu hücre kodunun girileceği sahadır.
**Virman** **İşlemi** **Yapılsın:** Virman işleminin yapılması isteniyorsa işaretlenmesi gereken sahadır.
**Kaynak** **Belge:** Belirli bir belge kaydı için işlem gerçekleştirilecekse bu belge bilgisinin girileceği sahadır.
**Hedef** **Hücre** **Kodu:** Belirlenen stokun, transfer edileceği hücre kodunun girileceği sahadır.
**Miktar:** Belirlenen stokun, transfer edilecek miktarının girileceği sahadır.
**Tarih:** İşlemin gerçekleşeceği tarih bilgisinin girileceği sahadır.

#### HÜCRE SAYIM İŞLEMLERİ

Depolardaki hücrelere ait sayım işlemlerinin yapıldığı bölümdür. Stok parametrelerinde "Detaylı sayım sistemi kullanılsın" parametresi işaretli ise Stok modülü altındaki Sayım Girişi ekranından hücre sayım girişleri yapılabilir. Bu parametre kullanıldığında Dinamik Depo modülünde sadece Sayım Bağlantısız Bakiye Sıfırlama işlemi çalıştırılabilir.
![](../_assets/efeb88ab85b258a0d26a.png)
![](../_assets/d3bff5622853c6780771.png)
Detaylı stok sayım parametresi kullanılmıyorsa, hücre sayım işlemleri Dinamik Depo modülü altından gerçekleştirilecektir.

#### Sayım Girişi

Hücrelerdeki ürünlerin sayım sonuçlarının girileceği bölümdür.

![](../_assets/0f7d46433df9cf79008c.png)
**Tarih:** Sayımın yapıldığı tarihin girileceği sahadır. Sayımlar, tarih bazında saklandığı için farklı tarihli pek çok sayım
girilebilir.
**Hücre Kodu:** Sayım yapılan hücre kodunun girileceği sahadır.
**Stok** **Kodu:** Belirlenen hücre kodunda, sayımı yapılan stok kodunun girileceği sahadır.
**Sayım** **Miktarı:** İlgili stokun sayım sonucunun girileceği sahadır.

#### Sayım İptali

Belli bir tarihte girilmiş olan sayım bilgilerinin silinmesi amacıyla kullanılacak olan bölümdür.

![](../_assets/2da6d369736f1e63a966.png)
**Sayım** **Tarihi:** Sayım bilgileri silinecek olan sayımın, kaydedildiği tarihin girileceği sahadır.
**Hücre Kodu:** Sayım bilgisi silinecek olan hücreler için aralık tanımlaması yapılabilecek sahadır. Bu saha boş bırakılır ise hücre koduna bakılmaksızın girilen tarihteki tüm sayımlar silinecektir.

#### Sayım Farkını Hücre Hareketlerine İşleme

Hücrelerdeki stok bakiyelerinin, sayım sonuçlarına eşitlenmesi amacıyla kullanılacak olan bölümdür.

![](../_assets/771cd7c4a0f9752f376c.png)
**Sayım Tarihi:** Hücrelerdeki stok bakiyeleri, hangi tarihte girilen sayıma eşitlenecek ise ilgili tarih bu sahaya girilmelidir.
**Hücre Kodu:** Sayıma eşitleme işlemi belli hücre kodları için yapılacak ise ilgili hücre kodları bu sahaya girilebilir. Boş bırakılması durumunda, hücre kodu kısıtı olmaksızın işlem, bütün hücreler için yapılacaktır.
**Hücre** **Grup** **Kodu:** Belli grup koduna sahip hücreler için işlem yapılacak ise ilgili grup kodu aralığı bu sahalara
girilmelidir.
**Fiş No:** Oluşturulacak kayıtta kullanılacak fiş numarasıdır.
**Stok Hareketler İşlensin:** Hücrelere stok bakiyeleri işlenirken aynı zamanda stok hareketlere işlenmesi de istenirse bu parameter işaretlenmelidir. Bu durumda ekranda kapalı olan alan aktif hale gelecek ve stoklar için sayım kısıtları verilebilecektir.
**Hareket** **Tarihi:** Hücrelere yapılacak kayıt için kullanılacak olan tarihtir.
**Hareket** **Türü:** Hareket türü olarak, Sayım Farkı program tarafından otomatik getirilecek ve değiştirilemeyecektir.
**(-)Eksi'ler** **Giriş** **İşlensin:** Sayım bakiyesi, bilgisayardaki hücre stokundan az ise, hücre stokunu, sayım bakiyesine eşitlemek için otomatik çıkış hareketi işlenecektir. Sayım bakiyesi, bilgisayardaki hücre stokundan fazla ise, hücre stokunu sayım bakiyesine eşitlemek için giriş hareketi işlenmesi gereklidir. Bu hareketin işlem sırasında otomatik yapılmasını istiyorsanız bu seçeneği işaretleyebilirsiniz. Giriş hareketlerinin işlenmeyip, daha sonra birtakım kontroller yapıp manuel işlenmesini istiyorsanız, bu seçeneği işaretlemeyin.

#### Sayım Bağlantısız Bakiye Sıfırlama

Hücrelerdeki bakiyelerin girilen sayım bilgilerine bakılmaksızın giriş/çıkış hareketleri oluşturarak sıfır bakiyeye getirilmesi için kullanılan bölümdür. Bu işlem çalıştırıldığında, hücrelerin son bakiyelerine bakılır ve bu bakiyeler sıfıra eşitlenir.
![](../_assets/7c4db04adbc7c1df82df.png)
**Hücre** **Kodu:** Sıfırlama işleminin belirli bir hücre kodu aralığı için yapılması isteniyorsa kullanılan sahadır.
**Fiş** **No:** Sıfırlama işlemi işlenirken bir fiş numarasına bağlanması isteniyorsa kullanılan sahadır.
**Stok Hareketlere İşlensin:** Hücre sıfırlama işlemi stoklara işlensin istenirse kullanılan parametredir. Bu parametre işaretlendiğinde aşağıdaki bölüm aktif hale gelir ve burada stoklar için istenen kısıtlar girilebilir. Sayım bağlantısız stok sayım sıfırlama işlemi hücre ile birlikte gerçekleşmiş olur.
**Depo** **Kodu:** Belirli bir depo içindeki hücreler için sıfırlama işlemi yapılmak isteniyorsa kullanılan sahadır.

**Sayım** **Farkı** **Hareket** **İptali**
![](../_assets/e98392c59b80fd1a8942.png)
"Sayım Farkını Hücre Hareketlere İşleme" bölümünden hücrelerdeki stok bakiyelerinin, hücre kodu bazında silinmesi için kullanılan bölümdür. Sayım farkını hücre hareketlerine işlerken herhangi bir açıklama girildiyse, iptal sırasında da aynı açıklamanın girilmesi gerekir. Aksi takdirde hareketler iptal edilmez. İptal işlemi hücrelerde yapılırken stok hareketlere işlenen kayıtlarında silinmesi istendiği durumda "Stok Hareketler İptal Edilsin" parametresinin işaretlenmesi gereklidir.

#### HIZLI HÜCRE KODU TANIMLAMA

Hücre kodlarının belli bir format belirleyerek hızlıca açılması için kullanılan bölümdür.

![](../_assets/5b5c81f118939f750065.png)
Hücre kodlamasının malların yerleştirilmesinde ve toplanmasında çok önemli olduğundan bahsetmiştik. Bu bölüm kullanılarak, belirlenen kodlama formatında hızlı hücre kodları açılabilir.
**Hücre** **Maskesi:** Açılacak hücreler için formatın belirleneceği sahadır. Yatayda ve/veya dikeyde hücreleri otomatik açabilirsiniz. Yatayda hücrelerin açılmasını istiyorsanız, hücre kodlarının başına gelecek karakter(ler)i yazıp, buna bitişik olarak {1} karakter dizisini yazmalısınız.
Örneğin; HY{1} şeklinde bir hücre maskesi, HY ile başlayan ve numaralandırması yatay aralık bölümünde verilecek olan hücreler açılacağı anlamına gelir. HY60, HY61, HY62 HY69 gibi. Dikeyde hücrelerin açılmasını istiyorsanız,
hücre kodlarının başına gelecek karakter(ler)i yazıp, buna bitişik olarak {2} karakter dizisini yazmalısınız.
Örneğin; HD{2} şeklinde bir hücre maskesi, HD ile başlayan ve numaralandırması dikey aralık bölümünde verilecek olan hücreler açılacağı anlamına gelir. HD20, HD21, HD22 HD29 gibi. İstenirse hem yatayda hem de dikeyde
hücreler tanımlanabilir. Örneğin; HY{1}HD{2} şeklinde bir hücre maskesi, HY60HD20, HY61HD20, HY62HD20, HY69HD20, HY60HD21, HY61HD21, HY62HD21, .... , HY69HD21, HY60HD22, HY61HD22, HY62HD22,, HY69HD22,
.... , HY60HD29, HY61HD29, HY62HD29,, HY69HD29 şeklinde hücreler açılacağı anlamına gelir.
**Yatay:** Hücrelerin yatayda hangi sayıdan başlayıp hangi sayıda biteceği bu sahada belirlenecektir. Yukarıdaki örnekte yatay aralık 60-69 olmalıdır.
**Dikey:** Hücrelerin dikeyde hangi sayıdan başlayıp hangi sayıda biteceğinin belirlendiği sahadır. Yukarıdaki örnekte dikey aralık 20-29 olmalıdır.
**Hücre** **Grup** **Kodu:** Daha önceden tanımlı bir hücre grup kodu bu sahaya girilir ise açılacak hücre kodlarına bu grup kodu atanacaktır. Boş geçilebilir.
**Depo** **Kodu:** Açılacak hücreler için baz alınacak lokal depo kodunun girileceği sahadır. Açılan hücrelerin, lokasyon takibi yapılan depolardan hangisinde olduğunu belirtir.

#### YERLEŞTİRME/TOPLAMA İPTALİ

Hücre Yerleştirme veya Hücre Toplama adımlarıyla yapılan kayıtların iptali amacıyla kullanılan bölümdür. Yerleştirme/Toplama İptal işlemi bu ekrandan yapılabildiği gibi aynı zamanda belge işlemleri esnasında sağ klikte yer alan Dinamik Depo İşlemleri seçeneğinden de yapılabilir.
![](../_assets/1b2098aaad69e704b389.png)
**Yerleştirme/****Toplama:** Bu sahada, iptal edilecek kaydın, yerleştirme mi, toplama mı olduğu belirlenecektir.
**Kalemleri** **Getir:** Verdiğiniz kıstaslara uygun kalem bilgilerinin, grid ekranına getirilebilmesi için kullanılan tuştur.
**Hepsini Seç:** Grid ekranındaki kalemlerin işaretlenmesi için kullanılan tuştur. Herhangi bir kalem seçilmeden işlem yapılamayacağı için, öncelikle bu tuş kullanılarak veya satır seç tuşu ile tek tek seçerek ya da fareniz ile iptal edilecek satırı çift tıklayarak kalemleri seçmelisiniz.
**Hepsini** **Kapat:** Daha önceden seçilmiş olan satırların iptalinden vazgeçilmesi durumunda, kullanılacak tuştur. Seçilmiş olan bütün satırların işaretini kaldırır.
**Satır** **Seç;** Grid ekranında üzerinde bulunduğunuz bir satırın iptal edilmek üzere seçilmesi için kullanılan tuştur.
**Satır** **Kapat:** Daha önceden seçilmiş ve grid ekranında, üzerinde bulunduğunuz bir satırın iptalinden vazgeçilmesi durumunda kullanılacak tuştur.

#### HAREKET KONTROLÜ

![](../_assets/f97f07cbc95c61f20dc8.png)
Yerleştirme veya toplama bilgilerinden girilen kayıtlarla, hücrelerdeki kayıtlar arasında bir tutarsızlık olması durumunda kullanılacak olan bölümdür. İşlem çalıştırıldığında, yerleştirme ve toplama bilgileri baz alınarak hücrelerdeki stok bakiyeleri tekrar düzenlenir.

**DEPO DURUM RAPORU:** Raporunuz, stok kodu, stok adı, hücre kodu, hücre grup kodu, açıklama, hacim kodu, hacim açıklama, depo kodu, depo ismi, net bakiye ve brüt bakiye başlıkları altında listelenecektir.

**STOK HÜCRE BAKİYE RAPORU:** Depolarda bulunan stokların bakiyeleri ile stok modülünde görünen bakiyelerin karşılaştırmalı listesinin alınabileceği rapor seçeneğidir.
Raporunuz, stok kodu, stok adı, depo kodu, stok bakiye ve fark başlıkları altında listelenecektir.

**DEPO SAYIM FARK RAPORU:** Yapılan sayım sonuçları ile depodaki miktarların karşılaştırmalı listesinin alınabileceği rapor seçeneğidir.
Raporunuz, stok kodu, stok adı, giriş miktarı, çıkış miktarı, bilgisayar miktarı, sayım miktarı ve fark miktarı başlıkları altında listelenecektir.

**DEPO KONTROL RAPORU:** Yerleştirme veya Toplama işlemleri sırasında yapılan kayıtların, belge detayı ile listelerinin alınabileceği rapor seçeneğidir.
Raporunuz, belge numarası, cari kodu, stok kodu, stok adı, miktar, hücre kodu, hücre giriş miktarı ve hücre çıkış miktarı başlıkları ile listelenecektir.

#### DİNAMİK DEPO İŞLEMLERİNDE KULLANILAN ÖZEL PARAMETRELER

*DINDEPO\\HUCREBAKIYEGETIRME* özel parametresi kullanıldığında hücre yerleştirme ekranında fiş bakiyesi getirilmektedir.
*DINDEPO\\HAREKET_ZORUNLU* özel parametresi tanımlı olduğunda dinamik depo hücre yerleştirme işlemi zorunlu tutulmaktadır.
*DINDEPO\\OTOMATIKISLEM* özel parametresi kullanıldığında kalemler alanında dinamik depo hücre yerleştirme ekranı otomatik açılmaktadır.
*DINDEPO\\BELGE_TARIHI_KULLANILSIN* özel parametresi tanımlandığında hücre yerleştirme veya toplama yapılırken depo hareketine belgenin tarihi (yani stok hareketlerindeki) tarih atılmaktadır. Böylece tüm bakiyeler birbirini tutmaktadır.
