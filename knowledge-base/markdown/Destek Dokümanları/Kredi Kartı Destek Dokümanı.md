---
title: "Kredi Kartı Destek Dokümanı"
page_id: "50680377"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Kredi Kartı Destek Dokümanı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Kredi Kartı Destek Dokümanı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTYxMDA3N2NmLTk5YTEtNGIwMi1iNDMxLTE0NzU0MzJhZjhmMyZsaW5rPWE4MmFkMDc4LTkyNGQtNDYzMi04MTE5LTIzNjEzYWRkMjUxMSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=610077cf-99a1-4b02-b431-1475432af8f3&link=a82ad078-924d-4632-8119-23613add2511&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "kredi-karti-destek-dokumani_50681012_50680377.html"
source_version: "2022-11-03T09:53:33.367+03:00"
source_bytes: 5672744
fetched_at: "2026-09-13T04:26:27+00:00"
generator: "netsis-scraper 1.0.0"
---
# Kredi Kartı Destek Dokümanı

Kredi Kartı ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Kredi kartı uygulaması, mağazalar ile bankalar arası kart sözleşmelerinin ve bu sözleşmelere ait detayların tanımlanabilmesini, kart ile yapılan tahsilatların takip edilebilmesini sağlar.

**Kredi Kartı Tip Tanımları:** Banka kart tiplerinin tanımlandığı ekrandır. Bu ekrandan tanımlanan tipler kredi kartı tanımlarına bağlanacaktır.

![](../_assets/f81ac8e99e2376b7d038.png)

**Kredi Kartı Tanımlamaları:** Farklı bankalara ait kredi kart kodlarının tanımlandığı ekrandır. Bu ekrandan tanımlanan kart kodları daha sonra sözleşmeler ile bağlanacaktır.

![](../_assets/87c8212d673c1093a8f7.png)

**Kart Kodu:** Kullanıcı tarafından tanımlanan, kart sabitine verilecek olan koddur.

**Banka Kodu:** Tanımlanan kredi kartının bağlı olduğu banka ana kodunun girildiği sahadır.

**Tip Kodu:** Tanımlanan kredi kartının, kart tipi ile eşleştirildiği sahadır.

**Banka Kesinti Tip Tanımlamaları:** Bankalar mağazalar ile olan sözleşmeleri kapsamında farklılık gösterebilen kesintiler uygularlar. Bu kesinti tipleri "Banka Kesinti Tip Tanımları" ekranından açılmaktadır.

![](../_assets/d5ad20030aaf5e556d1d.png)

**Banka Kesinti Tanımları:** "Banka Kesinti Tip Tanımları" ekranından açılan kesinti tiplerinin detaylandırıldığı ekrandır. Burada detaylandırılan kesintiler daha sonra "Banka Sözleşme Tanımlamaları" ekranından, sözleşmeler ile bağlanacaktır.

![](../_assets/00ef1edc9ae5d710aabc.png)

**Kesinti Kodu:** Kullanıcı tarafından belirlenen kesinti kodunun girileceği sahadır.

**Tip Kodu:** Tanımlanan kesinti tiplerinin, kesintiler ile eşleştirildiği sahadır.

**Banka Kodu.** Yapılan kesinti tanımlamasının bağlı olduğu banka ana kodunun girildiği sahadır.

**Kesinti Zamanı:** Kesintinin tamamının ilk tahsilattan yapılması gerektiğinde "İlk Tahsilat", kesintinin taksit tutarı üzerinden, taksitlere uygulanması gerektiğinde ise "Vadeli" seçeneğinin işaretlenmesi gerekir.

**Kesinti Kullanımı:** Kesintinin kullanımı "Brüt" veya "Net" olarak iki seçenekten oluşur. Tanımlanan kesinti tipi "Net" ise satış anında taksit tutarı içerisinden kesinti ayrılarak banka hareketlerine atılır. Tanımlanan kesinti tipi "Brüt" ise satış anında taksit tutarı matrah dahil tek satır şeklinde atılır.

**Kesinti Oranı:** Matraha uygulanacak olan kesinti oranının girildiği sahadır.

**Masraf Muhasebe Kodu:** Banka Şube Bazında Parametreler ekranında "Kart Masrafları Satış Anında Entegrasyona Atılsın" parametresinin işaretli olduğu durumda, masraf muhasebe koduna yazılan hesaba, brüt tipli kesintiler için borç hareketleri atılacaktır. Net tipli kesintiler için 108 hesap çalışacaktır. Parametrenin işaretli olmaması durumunda kesintiler "Kredi Kartı Tahsilat Kayıtları" yapıldığı sırada bu hesaba borç olarak yansıyacaktır.

**Tahakkuk Muhasebe Kodu:** Banka Şube Bazında Parametreler ekranında "Kart Masrafları Satış Anında Entegrasyona Atılsın" parametresinin işaretli olduğu durumda tahakkuk muhasebe koduna yazılan hesapta, brüt tipli kesintiler için masraf muhasebe kodu borç çalışırken tahakkuk muhasebe kodunda alacak hareketleri oluşacaktır.

Örneğin %3 net tipli ve %1 brüt tipli kesinti bağlanmış olan bir sözleşme ile yapılan 1000 liralık alışveriş sonrası %3 net kesinti tutarı olan 30 YTL matrahtan ayrı, %1 brüt kesinti tutarı olan 10 YTL ise matrahın içinde olacak şekilde banka hareketlerine aktarılacaktır.

![](../_assets/9fc98dd1ebffddf06fb0.png)

1000 YTL üzerinden; %3 30 YTL net kesinti, %1 10 YTL brüt kesinti 960 YTL hesaba geçecek olan matrahtır. Ancak %1 brüt bir kesinti olduğu için satış anında matrah ile aynı satırda oluşur. (970 virman,30 masraf)

Bu satışın muhasebe kaydı ise aşağıdaki şekilde olacaktır.

\*\*Banka Şube Bazında Parametreler "Kart Masrafları Satış Anında Entegrasyona Atılsın" parametresinin işaretli olduğu durumda kayıtlar oluşturulmuştur.

![](../_assets/21c1d0f35955379d2992.png)

Satış anında net tipli kesinti için(30 YTL) sadece 108 hesap borç olarak çalışırken, brüt tipli kesinti matrah içinde 108 hesaba borç olarak yansımış(10 YTL) aynı zamanda masraf hesabına(780) borç, kesinti tahakkuk hesabına(381) hesabına alacak işlemiştir . Brüt kesinti satış anında tahakkuk hesabına alacak yazarken, net kesinti tahsilat kayıtları anında 381 hesaba direk aktarılacaktır.

![](../_assets/64632c4393e6201441cf.png)

Bu satışa ait "Kredi Kartı Tahsilat Kayıtları" işlemi çalıştırıdığında vadesiz hesaba aktarılacak hareket ve oluşacak yevmiye fişleri aşağıdaki gibi olacaktır.

![](../_assets/ebd31c9c8a431f95bd1f.png)

Brüt kesinti olan 10 YTL "Kredi Kartı Tahsilat Kayıtları" işleminde matrah ile birlikte vadesiz mevduat hesabına girmiş ve daha sonra tahakkuk hesabına aktarılmak üzere hesaptan çıkış yapmıştır. Bu durumda vadesiz mevduat hesabında kesintiler düşülmüş tutar olan 960 YTL kalmıştır.

**Banka Sözleşme Tanımlamaları**

Bankalar ile yapılan sözleşmenin hangi kredi kartına ait olduğu, geçerli tarih aralığı, taksit sayısı ve kesintileri ile ilgili tanımlamaların yapıldığı bölümdür. Sözleşme tanımı banka hatta bankalar ile yapılan farklı sözleşmeler ya da bankalara ait farklı özellikteki kartlar bazında çoğaltılabilir.

![](../_assets/fbfa056139ec1abefb4b.png)

**Sözleşme Kodu**: Bankalar ile yapılan sözleşmelere kullanıcı tarafından programda kullanılmak üzere verilen koddur. Sözleşme kodu en fazla 15 karakter olabilir.

**Açıklama:** Sözleşme koduna ait açıklamanın girilebileceği sahadır.

**Kart Kodu:** "Kredi Kartı Kayıtları" ekranından girilen kart sabitlerinin sözleşme ile eşleştirildiği sahadır.

**Bnk. Hes. Kod:** Kapalı faturanın ya da hızlı tahsilat kaydı sırasında çalışacak banka kodunun seçileceği sahadır. Rehbere basıldığında "Banka Hesap Kayıtları"' ekranından Hesap Tipi "Kredi Kartı Hesabı" seçilerek tanımlanmış bankalar listelenecektir.

**Başlangıç Tarihi/ Bitiş Tarihi**: Sözleşmenin başlangıç/bitiş tarihinin girilmesi gereken sahadır. Başlangıç tarihi öncesinde ya da bitiş tarihi sonrasında sözleşmeler satış anında kullanılamayacaktır.

**Kilit:** Kilit parametresi işaretlendiği durumda kaydedilen sözleşme tahsilat işlemlerinde kullanılamaz.

**Sözleşme Detay Bilgileri:** Yapılacak tanımın hangi taksit aralıklarını kapsayacağı ve koşullarının belirleneceği bölümdür. Örneğin 1 ila 5 taksit arasında %5 kesinti ve 20 gün vade / 5 ila 10 taksit arasına %7 kesinti 30 gün vade olacak şekilde detay tanımlamalar bu ekran aracılığı ile sağlanabilir.

![](../_assets/4d3b795bdd764601f4d3.png)

**Taksit Aralığı:** Uygulanacak vade, kesinti ve blokajın hangi taksit aralıklarında geçerli olacağının belirlendiği sahadır. Başlangıç taksit 0, bitiş taksit 0 olarak tanımlanan taksitler puan kullanımını ifade etmektedir. Taksit aralıkları bir öncekini kapsamayacak şekilde tanımlanmalıdır.

**Tahsilat şekli:** Bankadan yapılan tahsilatlar tek seferde yapılacağı gibi vadeli olarak da yapılabilirler. Tahsilat şekli "Vadeli" seçildiğinde, toplam tahsil edilmesi gereken tutar, taksitlere bölünecektir. Bankadan tek seferde ödeme alınması durumunda tahsilat "Tek Seferde" seçilir ve böylece müşteri ödemeleri taksitli olarak yapmasına rağmen mağaza paranın tamamını bankadan peşin olarak tahsil eder.

**Vade Atlama:** Taksit atlatma uygulaması yapılacak ise, kaç taksitin atlanması gerektiği bu sahada belirtilmelidir. Örneğin: Vade atlatma 1 ise ve satış işlemi 20/06/2020 tarihinde yapıldıysa taksit atlatılacağı için ilk ödeme için baz tarihi 20/07/2020 olarak belirlenecektir ve bu tarihe göre taksitler ayarlanacaktır.

**Blokaj Şekli**: Satış işleminden sonra, bankanın parayı belirli bir süre elinde bulundurması, ödemeyi daha sonra gerçekleştirmesi işlemidir.

Sabit Gün seçilir ise blokaj değerine girilen değer bir ayın günlerini ifade eder. Buraya 10 girildiyse ayın 10. günü anlamına gelir.
İlave Gün seçilir ise blokaj değerine girilen gün, alışveriş tarihine eklenerek ilk ödemenin yapılacağı gün bulunur. Taksit uygulamasının olduğu durumlarda ilk ödemenin yapaılcağı gün baz alınarak diğer ödemelerin vadeleri oluşacaktır.

Örneğin;

Alışveriş 20/06/2020 tarihinde yapılmış ve ilave güne 30 girilmiş ise blokaj 20/07/2020 tarihinde bitecek ve banka bu tarihte ilk ödemeyi gerçekleştirecektir. Bir sonraki ödemenin de 30 gün sonra yapılacağı varsayılırsa ödeme tarihi 19/08/2020 olacaktır.

**Blokaj Değeri:** Blokaj uygulamasının kaç gün süreceğinin belirlendiği sahadır. Blokaj Şekli bölümünde yapılan seçime göre, buraya sabit gün ya da ilave gün değeri girilmektedir.

**Vade Şekli:** Bankanın yapacağı ödemelerin hangi vadelere göre oluşacağının belirlendiği bölümdür.

Sabit gün seçilir ise; alışveriş tarihine bakılmaksızın vade değerine girilen değer bir ayın günlerini ifade eder.

İlave gün seçilir ise; vade değeri sahası pasif hale geçecektir. İlave gün seçildiğinde 30 günlük periyotlarda vadeler oluşacaktır.

Dinamik değer seçildiğinde ise; normalde ilk bulunan tarihin günü, dinamik değer alanına girdiğimiz değerden (günden) küçükse o zaman tarih, vade gün alanında girdiğimiz gün olarak tespit edilir(İlk taksit olursa 1 ay sonrasındaki gün).

Sonrasında tespit edilen tarihin günü, dinamik değerden büyük eşitse ve dinamik değerin 2 katından küçükse o zaman tarih, vade günü ile dinamik değer toplamı olan gün olarak tespit edilir (İlk taksit olursa 1 ay sonrasındaki gün).

Sonrasında tespit edilen tarihin günü, dinamik değerin 2 katından büyük eşitse ve 31 den küçükse o zaman tarih, vade günü ile (dinamik değer \* 2) toplamı olan gün olarak tespit edilir (İlk taksit olursa 1 ay sonrasındaki gün).

**Vade Değeri:** Vadenin kaç gün olacağının belirlendiği sahadır. "Vade Şekli" bölümünde yapılan seçime göre sabit gün için değerin belirlendiği sahadır.

**Sözleşme Kesinti Bilgileri**

Sözleşme detay bilgilerinde seçili olan taksit aralığında banka tarafından hangi kesintilerin uygulanacağının belirlendiği ekrandır. Burada dikkat edilmesi gereken "Sözleşme Detay Bilgileri" ekranından hangi taksit aralığı tanımı seçildi ise kesintiler o aralıktaki işlemlere uygulanacaktır.

![](../_assets/b600f2aa5c42a9471c6a.png)

**Kesinti Kodu**

Tanımlanan taksit aralıklarından kesintinin uygulanacağı aralık seçildikten sonra bu sayfaya ulaşılabilecektir. Rehber yardımı ile "Banka Kesinti Kayıtları" bölümünde tanımlanan kesintilere ulaşılabilir.

**Kredi Kartı Banka Hesabının Tanımlanması**

Kredi kartları için "Banka Hesap Kayıtları" ekranından "Hesap Tipi" sahası "Kredi Kartı Hesabı" olan ayrı hesap tanımlamaları yapılmalıdır.

![](../_assets/8325870f3bfff9c856b9.png)![](../_assets/b833b7af20a0dd09f1c8.png)

Tipi kredi kartı hesabı olarak seçildiğinde "Bağ. Hes. Kod." sahası aktif hale gelecektir. Bağlı hesap kodu, kredi kartı tahsilat işlemi sonucunda banka tarafından ödenen tutarın aktarılacağı vadesiz mevduat hesabıdır.

"Banka Hesap Kayıtları" "Banka Hesap Bilgi-2" ekranından çalışacak muhasebe hesap kodları belirlenmelidir. Kartın kullanımı durumunda çalışacak hesap "Banka" alanına girilmelidir. Gerçekte banka tarafından yapılan ödeme programda hesaplanan ödemeden farklı olursa, elle müdahaleye izin verilmekte ve hesaplanan değer ile düzenlenen değer arasındaki fark, Fark A.M.K. ve Fark B.M.K. muhasebe hesaplarına aktarılmaktadır.

**Fatura Modülünde Kredi Kartı Uygulamaları**

Kredi kartı ile yapılan bir alışverişin kapalı tipteki faturası kaydedilirken açılan "Hızlı Tahsilat Kayıtları" ekranından tahsilat bilgileri girilip, aynı anda banka, kasa, entegrasyon/muhasebe ve cari modüllerine kayıtların yapılması sağlanabilir.
Kapalı tipli kesilen faturada Hızlı Tahsilat Kayıtları ekranının açılabilmesi için Satış Fatura Parametreleri Genel-3 sekmesindeki "Kapalı Faturada Tahsilat Ekranı Çıksın" parametresi işaretlenmelidir. "Banka Şube Bazında Parametreler" "Kredi Kartı Tahsilatları Nakit Kasaya İşlensin" parametresi ile kredi kartı ile alınan tahsilatlarında banka yerine kasaya işlemesi sağlanabilir.

**Hızlı Tahsilat Kayıtları**

Kapalı kesilen satış faturasında, toplamlar sayfasında Tamam butonuna basıldıktan sonra Hızlı Tahsilat Kayıtları ekranı çıkacaktır. Bu ekran, bir kısmı nakit, bir kısmı kredi kartı ile, tamamı kredi kartı ya da tamamı nakit olarak, farklı banka kartları ile ödeme almaya olanak sunmaktadır.

![](../_assets/fa8c2c790ae42d94af73.png)

**Cari Kodu:** Tahsilatın alındığı cari kodunun girildiği sahadır.

**Belge No:** Tahsilat belge numarasının girildiği sahadır.

**Tahsilat Şekli:** Yapılan alışverişte hangi sözleşmenin kullanılacağının belirlendiği sahadır. Tahsilat Şekli rehberinde, "Banka Sözleşme Tanımlamaları" ekranından girilen kayıtlar listelenecektir. Tahsilat şekli boş geçilirse, tahsilatın nakit olarak yapılacağı anlaşılacak ve Tahsil Şekli sahasına "Nakit" değeri atanacaktır.

**Taksit Sayısı:** Tahsilat şekli nakit dışında ise taksit sayısının belirlendiği sahadır.

**Kart Numarası:** Müşterinin alışverişte kullandığı kredi kartının 16 haneli kart numarasının girileceği sahadır. Kart bilgisi takip edilmek istenmiyorsa BANKA/KREDIKARTIKONTROLETME özel parametresi kullanılabilir.

**Tutar:** Tahsilat şekline ait tutarının girileceği sahadır. Ödemenin bir kısmı nakit, bir kısmı puanla yapılıyor bir kısmı da taksitlendiriliyor ise her üç ödeme için ayrı ayrı kayıtlar girilmelidir. Girilen tutarların toplamı faturanın toplamına eşit olmalıdır.

**Hızlı Tahsilat Kaydı Sonucunda Kasa Modülünde Oluşan Kayıtlar**

"Banka Şube Bazında Parametreler" ekranında "Kredi Kartı Tahsilatları Nakit Kasaya İşlensin" parametresinin işaretli olmadığı durumlarda nakit tahsilatlar kasaya işlenirken, sözleşme seçilerek yapılan tüm işlemler direk banka hesaplarına işlenecektir.

Hızlı Tahsilat Kaydı sonucunda kasanın fatura sekmesinde işlemin yapıldığı tarihte nakit seçilen tutar kadar
gelir kaydı oluşacaktır.

Örneğin, 194,70 YTL olan borcun 100 YTL'lik kısmı kredi kartı ile 2 taksit, kalan 94,70 YTL'lik kısmı nakit işlendi ise; kasada sadece 94,70 YTL görünecek ve 100 YTL 2 taksite bölünmüş olarak banka hesabına geçecektir.

![](../_assets/d1a20e5f1afc6f889f78.png)

**Hızlı Tahsilat Kaydı Sonucunda Cari Modülünde Oluşan Kayıtlar**

Kapalı tipli faturanın cari hareketlerde izlenmesi isteniyor ise "Satış Fatura Parametreleri/Genel3 " sekmesindeki "Kapalı Fatura Cari Harekete İşlensin" parametresi işaretlenmelidir. Fatura kaydı sonrasında, cari hareketlere fatura toplamı kadar borç ve alacak kaydı atılacaktır.

![](../_assets/b6ec220f8a939c0bd8cd.png)

**Hızlı Tahsilat Kaydı Sonucunda Banka Modülünde Oluşan Kayıtlar**

Kesilen kapalı tipli fatura sonrasında, sözleşmede belirtilen banka hesap kodunda taksit tutarları için borç hareketi oluşur. Hareket ya da hareketlerin vadeleri, sözleşmede belirlenen koşullara göre belirlenir.
Örneğin,

- Alışveriş tarihi 07/09/2020
- Blokaj ilave 10 gün
- Vade ilave gün
- Ödemeler bankadan taksitli olarak tahsil edilecek
- Kesintilerden bir tanesi ilk tahsilatta diğeri de vadeli ve net olarak yapılacaktır.

Bu durumda iki taksitli olarak kesilen 3599 YTL tutarındaki fatura için kayıtlar kredi kartının hesabında aşağıdaki gibi oluşacaktır.

![](../_assets/69233f6df738a0e736a4.png)

Oluşan hareketlerin açıklamalarında cari adı, belge numarası, sözleşme kodu, taksit sayısı ve kesinti kodu görülmektedir. Borç kısmında taksit tutarları ve kesintiler için ayrı(NET kesinti tanımlandığı için) kayıtlar oluşmuştur.

İlk vade 07/09/2020+10 gün = 17/09/2020 olarak bulunur. Sonraki vade 17/09/2020+30 gün = 10/10/2020 olarak bulunur.

Kesintilerden biri ilk tahsilatta olduğu için sadece ilk taksitte izlenirken, diğeri vadeli olduğu için iki taksitte de izlenmektedir.

Not: Aynı örnek için Kesinti tipi "BRÜT" olan bir sözleşme kullanılsaydı kayıtlar aşağıdaki gibi oluşacaktı.

![](../_assets/ad668478cc26df1fbb9c.png)

Oluşan iki taksit içinde kesintiler izlenemeyecek, ancak tahsilat işlemlerinde içerisinden kesintiler ayrılıp ilgili hesaplara aktarılacaktır.

**Hızlı Tahsilat Kaydı Sonucunda Entegrasyon Modülünde Oluşan Kayıtlar**

Banka Şube Bazında Parametreler ekranında "Kart Masrafları Satış Anında Entegrasyona Atılsın" parametresinin işaretli olması durumda brüt kesintiler için banka kesinti tanımlamalarında belirtilen "Masraf Muhasebe Kodu" borç, "Tahakkuk Muhasebe Kodu" alacak olacak şekilde faturanın kaydedildiği sırada çalışacaktır. Yani kesintiler satış anında giderleşecektir. Net kesintiler için 108 hesap borç çalışacak ve giderleştirme işlemi "Kredi Kartı Tahsilat Kayıtları" işleminde gerçekleşecektir.

Masraf ve tahakkuk hesapları sözleşmede belirtilen koşullara göre taksit sayısı kadar ya da tek seferde çalışacak, kesintileri NET/BRÜT seçimine göre oluşacaktır.
Aşağıdaki örnekte 3599 YTL'lik iki taksitle yapılan bir satış kaydına ait muhasebe kaydı görülmektedir. "Kart Masrafları Satış Anında Entegrasyona Atılsın" parametresi işaretli olduğu durumda işlem yapılmıştır.
Banka ile yapılan sözleşmeye göre, iki taksitli satış için iki ayrı brüt kesinti yapılmıştır. Biri ilk tahsilatta diğeri
ise vadeli olarak kesilecek şekilde tanımlanmıştır.

![](../_assets/559da24de11ca1c60e19.png)

108 ile başlayan kredi kartının banka hesap kodunda taksit sayısı kadar hareket oluşmuştur. Tahakkuk ve masraf kodları da iki defa vadeli kesinti için ve bir defa ilk taksitte olacak şekilde ilk tahsilatta alınan kesinti için olmak üzere üç ayrı satırda çalışmıştır.

**Örnek1**

İş bankası ile yapılan sözleşmenin koşulları aşağıdaki gibidir;

- Banka tarafından ödemeler tek seferde yapılacaktır.
- Puan ile yapılan ödemelerde komisyon oranı %1
- Puan kazandırma komisyon oranı %1,5
- 1-10 taksitli ödemelerde komisyon oranı %3
- Genel hizmet komisyon oranı %2 olarak uygulanacaktır.
- Blokaj süresi ilave 20 gündür.
- Kesintiler ilk tahsilatta yapılacaktır.

Öncelikle banka kesinti tanımlamalarında kesintiler ve komisyon oranları tanımlanmalıdır.

![](../_assets/589c601ce4b9fdc6f0cb.png)

Sözleşme tanımı aşağıdaki gibi yapılmalıdır.

![](../_assets/1ea249e23dcc3c574906.png)

Puan(taksit aralığı 0-0) ve 1-10 taksitli alışveriş seçeneği için sözleşme detay tanımlamaları aşağıdaki şekilde yapılmalıdır.

![](../_assets/c00bcf7a6a6a357041df.png)

Puan ile alışveriş için sözleşme kesinti tanımalamaları aşağıdaki gibi olacaktır.

![](../_assets/ce366b3d3663ed2a36a0.png)

1-10 taksitli alışveriş için sözleşme kesinti tanımlamaları aşağıdaki gibi olacaktır.

![](../_assets/44842c5dda8e7b87f435.png)

Bu sözleşme çerçevesinde 22/06/20 tarihinde 1.000 YTL tutarında kapalı bir fatura kesiliyor. Faturanın 200 YTL'lik kısmı puan ile kalan 800 YTL'lik kısmı da 2 taksitli olarak ödeniyor.

![](../_assets/3d36fcaf8c75fbb641e5.png)

Tamam butonuna basıldıktan sonra sırayla banka ve entegrasyonda oluşan kayıtlar aşağıdaki şekilde olacaktır.

**Banka**

![](../_assets/1438755f6c67931f15af.png)
Banka hesap hareketlerinde oluşan kayıtların vade tarihleri banka tarafından ödemenin yapılacağı tarihi ifade etmektedir. Sözleşmeye göre ilave 20 gün blokaj uygulandığı için kayıtların vade tarihleri "alışveriş tarihi + 20 gün" olarak bulunur. Banka ödemeleri 12/07/2020 tarihinde gerçekleştirecektir. Banka, puanlı alışveriş için 200 YTL üzerinden %2(2YTL) kesintiyi,alışverişin taksitli kısmı için de 800 YTL üzerinden kesintiler kademesiz tanımlandığı için %3-24 YTL, %2-16 YTL ve %1,5-12 YTL masrafı ayırıp kalan rakamı virmanlayacaktır.

![](../_assets/835c3592d8f88d0d4ea3.png)

Muhasebe kayıtlarında, 200 YTL'lik puan ile ödeme ve iki taksit ile ödeme için toplam 800 YTL'lik alacak hareketi görülmektedir.

**Kredi Kartı Tahsilat Kayıtları**

Bankaların yaptığı ya da yapacağı ödemelerin tespit edilmesini, banka ve entegrasyon modüllerinde ödeme kayıtlarının oluşmasını sağlayan işlemdir.

![](../_assets/feb672e12bd74a7fc251.png)

**Vade Başlangıç Tarihi/ Vade Bitiş Tarihi:** Bankalar tarafından ödemesi gelen taksitlerin vade aralığının girildiği sahalardır.

**Hareket Tarihi**: İşlem sonucunda oluşacak olan tahsilatların, banka ve entegrasyon modüllerinde hangi tarihte oluşacağının belirlendiği sahadır.

**Şube Kodu:** Merkez şubeden girildiğinde aktif olan sahadır. Hangi şube için işlem yapılacağı bu sahadan seçilebilir.

**Banka Hesap Kodu:** Tahsilat işleminin çalıştırılmak istendiği kredi kartı hesap kodunun seçildiği sahadır. Boş geçilerek tüm hesaplar için aynı anda çalıştırılabilir.

**Kayıtlar Şube Kırılımlı Oluşturulsun:** Birden fazla şube için aynı anda tahsilat kaydı yapıldığında bu parametre işaretlenerek kayıtların şube bazında oluşması sağlanabilir. Bu parametre sadece merkez şubeden giriş yapıldığında aktif olarak gelecektir.

**Kayıtlar Belge No Kırılımlı Oluşturulsun:** Kayıtlar belge no kırılımlı oluşturulsun parametresi işaretli olmadığı durumlarda ilgili banka kodunda vadeye uyan tüm hareketler kümüle olarak izlenecektir.

![](../_assets/3277f569659e3eb9fc43.png)

!worddav9f3acd9f0f7368b9c9253aaf9359756e.png|height=53,width=628!Parametre işaretlendiğinde ise ilgili banka kodu her tahsilat evrakı için ayrı ayrı "Belge No" detayı ile oluşacaktır.

**Kayıtlar Proje Kırılımlı Oluşturulsun**: Proje uygulamasının açık olması durumunda aktif olan parametredir. Oluşacak tahsilat kayıtlarının proje bazında kırılımlı olarak oluşmasını sağlar.

**Kayıtlar Plasiyer Kırılımlı Oluşturulsun:** Plasiyer uygulamasının açık olması durumunda aktif olan parametredir. Oluşacak tahsilat kayıtlarının plasiyer bazında kırılımlı olarak oluşmasını sağlar.

Kayıtlar Detaylı Oluşturulsun: Kayıtlar detaylı oluşturulsun parametesi kullanıdığında tahsilata ait bilgilerde detaylandırılacaktır. Örneğin 198 YTL puan tahsilatı, 748 YTL taksit ile yapılan tahsilat gibi.

![](../_assets/fcd0c14a255fcfc32b01.png)
Detaylı yapılan tahsilat işlemleri daha sonra belge bazında virman dekontu silinerek iptal edilebilir. Detaysız yapılan işlemlerde ise belge bazında işlemi geri alma mümkün olmayacaktır.

**Tutar:** Hazırlık işleminden sonra grid ekranda listelen kayıtlardan seçilen kayda ait tutarın izlenebildiği ve düzeltilebildiği sahadır.

**Kayıt Onay:** Hazırlık işleminden sonra grid ekranda listelen kayıtlardan seçilen kaydın tutarının onaylanıp onaylanmadığının sorgulandığı sahadır. Rakam değiştilip onaylı hale getirilebilir.

**Detay Kısıt**: Ekrandaki kısıtlar dışında başka kısıtların da verilebileceği bölümdür. Detay kısıt butonun basıldığında aşağıdaki İleri Kısıt Tanımlama ekranı açılacaktır.

**Hazırlık**: Kayıtlar yapılmadan önce verilen kısıtlar doğrultusunda bir hazırlık işleminin çalışması gerekmektedir. Hazırlık butonun basıldığında aşağıdaki gibi bir onay ekranı açılır.

![](../_assets/6a32bc37c58547652e1c.png)

Evet butonuna basılarak işleme devam edildiğinde aşağıdaki şekilde bir uyarı mesajı alınacaktır.

![](../_assets/b1cd92e273e0fe16169c.png)

İşlem tamamlandıktan sonra grid ekranda aşağıdaki gibi kayıtlar listelenecektir

![](../_assets/feb672e12bd74a7fc251.png)

Grid ekranda listelenen bütün kayıtlar onaylı olarak gelecektir. İstenirse onayı kaldırılıp, oluştur işlemi sırasında banka ve entegrasyona kayıt atılmaması sağlanabilir.

**Oluştur:** Hazırlık sonucunda listelenen kayıtların banka ve entegrasyon modüllerine işlenmesi oluştur butonu yardımı ile yapılmaktadır. İşlem sonucunda aşağıdaki şekilde bir uyarı alınacaktır.

![](../_assets/7ed57d3bc4c99507b6c5.png)

!worddav9e6d8f45a44a58d20b4df067172389c5.png|height=163,width=628!Kredi Kartı Tahsilat Kayıtları Sonucu Banka Modülünde Oluşan Kayıtlar Kredi kartının bağlı olduğu banka

Tahsilat işlemi tamamlandığında kredi kartının banka hesap kodunda tahsilat anında oluşmuş olan tüm satırlar için karşı ayak oluşacatır. Yukarıdaki ekran görüntüsünde 22.06 da 200 YTL puan,800 YTL iki taksitli alışveriş için 31.07 tarihinde hem vadesiz hesaba geçecek olan ana para hemde kesintiler için alacak hareketi atılmış ve hesap bu işlem için sıfırlanmıştır.

**Kredi kartı hesabının bağlı olduğu vadesiz mevduat hesabı**

Bu hesap matrahtan kesintiler düşüldükten sonra hesaba geçecek ana parayı barındırır. Yani banka tarafından işletme hesabına yatacak olan ana para bu hesaba işlenir.

Yukarıdaki örneğe istinaden bu para 1000-54 den 946 YTL olacaktır.

![](../_assets/0da7c733c1945b861437.png)

**Kredi Kartı Tahsilat Kayıtları Sonucu Entegrasyon Modülünde Oluşan Kayıtlar**

Kredi kartı tahsilat işlemi sonucunda, online muhasebe kapalı ise kayıtlar dekont mahsubunda oluşacaktır. Açık ise işlemlere ait oluşan yevmiye fişleri muhasebe modülünden kontrol edilebilir.

![](../_assets/d4d923f7787f05b14358.png)

Yukarıdaki örnekte de görüldüğü gibi ilk fişte kredi kartı hesabı(108) net tutar kadar alacak çalışmıştır. Bağlı hesap kodu (102), banka tarafından yatırılan net tutar kadar borç çalışmıştır. "Kart Masrafları Satış Anında Entegrasyona Atılsın" parametresinin işaretli olması nedeni ile her bir kesinti için tanımlanan tahakkuk hesabında borç hareketleri oluşmuştur. "Kart masrafları satış anında entegrasyona atılsın" parametresi işaretli olmasaydı 381 tahakkuk hesabı yerine 780 gider hesabı çalışacaktı. Masraflar fatura kesildiği anda gidere atıldığı için tahakkuk hesabı borçlandırılmıştır.
