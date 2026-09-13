---
title: "Netsis Yüklenilen KDV Listesi"
page_id: "66237071"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis Yüklenilen KDV Listesi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis Yüklenilen KDV Listesi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTYyZWIwMzE1LTg2NTktNDJmYy1hNjVlLTc2OWM2YTViZmQ4ZCZsaW5rPTg5ZGU2MWIyLWRjY2ItNDdlNi04NjA0LWQ4M2JiYThlMDA0OSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=62eb0315-8659-42fc-a65e-769c6a5bfd8d&link=89de61b2-dccb-47e6-8604-d83bba8e0049&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-yuklenilen-kdv-listesi_66237072_66237071.html"
source_version: "2022-11-02T15:09:53.213+03:00"
source_bytes: 172539
fetched_at: "2026-09-13T04:24:35+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis Yüklenilen KDV Listesi

Netsis Yüklenilen KDV Listesi ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

> [!TIP]
> İlgili özelliğin anlatımını içeren webinar kaydına ulaşmak için [tıklayınız.](https://register.gotowebinar.com/recording/924689692649935371)

##### Yüklenilen KDV Listesi

Yüklenilen KDV listesi raporu, özellikle ihracat yapan firmaların ihracat faturalarında KDV tutarı bulunmadığı için, ihracat yaptığı ürünlerin üretiminde kullandıkları ve satın aldıkları hammaddelere ait alış faturalarındaki KDV tutarlarını dikkate alarak Gelir İdaresi Başkanlığından vergi iadesi alabilmek için hazırlamaları gereken bir rapordur. Yüklenilen KDV listesi raporunun desteklendiği ilk versiyonda sadece reçete kaydı bulunan ürünlere ait satış faturaları için destek verilmektedir, ilerleyen versiyonlarda al-sat yapılan ticari mallar için de bu raporun desteklenmesi planlanmaktadır.

Yüklenilen KDV listesi raporunun çalışma mantığı özetle şu şekilde olmaktadır; raporun hazırlanmak istendiği dönemdeki satış faturaları dikkate alınarak, öncelikle bu satışlardaki ürünlerin reçeteleri üzerinden toplamda gereksinim duyulan ve satın alınması gereken hammadde ihtiyacı hesaplanmakta ve bu hammadde ihtiyaçları için FIFO (İlk Giren İlk Çıkar) mantığına uygun olacak şekilde alış faturalarıyla otomatik eşleşme yapılarak alış faturalarındaki KDV tutarları rapora getirilmektedir. Bu eşleşme sırasında alış faturaları tarihe göre küçükten büyüğe sıralanmakta ve bu şekilde tarihi daha küçük olan alış faturalarıyla ilk olarak eşleşme sağlanmaktadır. Ayrıca alış faturasının kalem miktarları sadece hesaplanan ihtiyaç miktarı kadar kullanılmakta ve geri kalan miktarların ilerleyen aylardaki rapor sırasında kullanılabilmesi sağlanmaktadır. Öte yandan alış faturalarıyla yapılan eşleşme bilgileri NETSIS veri tabanı altında saklandığı için şirket devri yapılsa bile bir önceki senelerden gelen eşleşme bilgileri dikkate alınmakta ve önceki senelerde kullanılmamış alış faturaları için doğru şekilde eşleştirme yapılabilmektedir. Aynı zamanda "Stok \> Kod Değiştirme" işlemi üzerinden stok kodu değişikliği yapılmış olsa bile geçmiş sene şirketlerindeki eski stok kodlarına ait alış faturalarıyla eşleştirme yapılabilmektedir.

Yüklenilen KDV Listesinin kullanımı için aşağıdaki bölümlerde açıklanan 4 yeni ekran desteklenmiştir:

#### Yüklenilen KDV Devir Girişi

"Muhasebe-Kayıt-Yüklenilen KDV Devir Girişi" ekranını üzerinden uygulamaya ilk geçiş sırasında daha önceden Gelir İdaresi Başkanlığına beyan edilmiş alış faturalarının beyan edilmemiş (kalan) miktarları için devir girişi yapılabilmektedir. Bu ekran üzerinden yapılacak tanımlamalar şu anlama gelmektedir: Daha önceden Netsis üzerinden takip edilmeyen ve Gelir İdaresi Başkanlığına vergi iadesi için beyan edilen alış fatura kalemlerinin beyan edilmeyen kalan miktarları girilebilmekte ve uygulama kullanılmaya geçildikten sonra alış fatura kalemleri devir girişi yapılan miktarlar üzerinden değerlendirilip bu şekilde kullanılmaktadır.

Örneğin; A00000000000001 numaralı alış faturasının 1 numaralı kaleminin 50 Adet miktarı olduğunu düşünelim, bu kalemin 40 adetlik miktarı için daha önceden Netsis üzerinden rapor kullanımı yapılmıyorken "Yüklenilen KDV Listesi" hazırlanmış ve vergi iadesi alınmış olabilir. Bu durumda ilgili alış faturası kaleminin "Kalan Miktar" bilgisi 10 adet girilerek devir girişi yapılırsa, Yüklenilen KDV Listesinde bu alış faturasının sadece geriye kalan 10 adetlik miktarı için kullanım yapılacaktır.

"Yüklenilen KDV Devir Girişi" ekranı aşağıdaki gibidir.

![](../_assets/d96d5f9adf1d812914d2.png)

"Yüklenilen KDV Devir Girişi" ekranında serbest giriş yapılabileceği gibi herhangi bir şirket üzerinde yer alan alış faturası seçilerek de giriş yapılabilir. Serbest giriş seçeneği özellikle Netsis kullanımına yeni geçiş yapılan ve Netsis üzerinde önceki dönemlere ait alış fatura kayıtlarının bulunmadığı müşterilerimizde serbest şekilde giriş yapılması amacıyla desteklenmiştir, aksi durumda Netsis şirketleri üzerinde tanımlı olan alış faturaları seçilerek devir girişi yapılabilir.

Yüklenilen KDV Devir Girişi ekranı üzerindeki alanlar ve açıklamaları aşağıdaki gibidir:

- Serbest Giriş seçeneği, Netsis üzerinde tanımlı bulunmayan alış faturaları için işaretlenebilir. Serbest Giriş seçeneği işaretlendiğinde tanımlanan alış faturalarına ait serbest girilen alış fatura bilgileri Yüklenilen KDV Listesinde kullanılacaktır. Serbest Giriş seçeneği işaretlediğinde "Şirket İsmi" alanı pasif hale gelir ve aşağıdaki açıklanacak birçok saha kullanıcı tarafından manuel olarak doldurulmalıdır. (Alış Fatura No, Tarih, Resmi Belge No, Kalem Miktar vs.) Seçenek işaretlenmez ise Netsis şirketleri altındaki herhangi bir alış faturası seçilebilir ve sadece o alış faturası içim "Kalan Miktar" sahası doldurulabilir.
- Şirket İsmi alanı, "Serbest Giriş" seçeneği işaretli değilse Netsis şirketleri üzerinden alış faturası seçebilmek için öncelikle doldurulmalıdır. Devir girişi yapılacak alış faturası önceki sene şirketlerinde olsa bile bu saha sayesinde önceki senelerdeki alış faturaları için devir girişi yapılabilir.
- Alış Fatura No alanına, devir girişi yapılacak alış fatura numarası girilmelidir. Eğer serbest giriş yapılıyorsa istenen bir numara girilebilir, aksi halde seçilen şirket altında var olan bir alış faturası girilmelidir.
- Tarih alanına, alış faturasına ait tarih bilgisi girilebilir. Serbest giriş yapılmıyorsa seçilen alış faturasını tarihi otomatik olarak gelmektedir.
- Cari Kodu alanına, alış faturasına ait cari kodu bilgisi girilmelidir. Serbest giriş yapılsa bile Netsis üzerinde tanımlı olan bir cari kodu girilmelidir.
- Resmi Belge No alanına, alış faturasına ait resmi belge numarası bu sahaya girilebilir. Serbest giriş yapılıyorsa manuel olarak doldurulmalıdır, aksi halde seçilen alış faturası üzerinden getirilmekte ve alan pasif olmaktadır.
- GGB No alanına, ithalat tipi alış faturaları için GBB (Gümrük Giriş Belge) No bilgisi girilebilir. Serbest giriş yapılıyorsa manuel olarak doldurulmalıdır, aksi halde seçilen alış faturası üzerinden getirilmekte ve alan pasif olmaktadır.
- Kalem Sıra No alanına, seçilen alış faturasının kalem sıra bilgisi girilmelidir. Serbest giriş yapılıyorsa bu sahaya manuel giriş yapılabilir, aksi halde seçilen alış faturasının kalemlerinden biri seçilmelidir.
- Stok Kodu alanına, seçilen alış faturası kalemine ait stok kodu girilmelidir. Serbest giriş yapılıyorsa Netsis üzerinde tanımlı olan stok kodlarından biri manuel olarak seçilebilir, aksi durumda seçilen alış fatura kalemine ait stok kodu getirilmekte de alan pasif olmaktadır.
- Kalem Miktar alanına, seçilen alış faturası kalemine ait miktar bilgisi girilmelidir. Serbest giriş yapılıyorsa manuel olarak miktar bilgisi girilebilir, aksi durumda seçilen alış fatura kalemine ait miktar bilgisi getirilmekte ve alan pasif olmaktadır.
- KDV Oranı alanına, seçilen alış faturası kalemine ait KDV oranı girilmelidir. Serbest giriş yapılıyorsa manuel olarak oran bilgisi girilebilir, aksi durumda seçilen alış fatura kalemine ait KDV oranı getirilmekte ve alan pasif olmaktadır.
- Kalan Miktar alanına devir giriş sırasında asıl olarak girilmek istenen veri denk gelmektedir. Seçilen alış faturası kaleminin ne kadarlık miktarının beyan edilmediği, yani daha sonraki Yüklenilen KDV Listesi raporlarında ne kadarlık miktarın kullanılabileceği bu sahaya girilen devir miktarı üzerinden belirlenmektedir. "Kalem Miktarı" sahasına girilen değerden daha büyük olmamalıdır.
- Kullanılan Miktar alanı, (Kalem Miktar-Kalan Miktar) formülüyle otomatik olarak hesaplanmaktadır ve pasif bir alandır.
- Net Fiyat alanına, seçilen alış faturası kalemine ait KDV hariç birim fiyat bilgisi girilmelidir. Serbest giriş yapılıyorsa manuel olarak girilebilir, aksi durumda seçilen alış fatura kaleminden getirilmekte ve alan pasif olmaktadır.
- Net Tutar alanı, (Kalem Miktar\*Net Fiyat) formülüyle otomatik olarak hesaplanmaktadır ve pasif bir alandır.
- Fason Faturası seçeneği, devir girişi yapılan alış faturası fason işlemler için kullanılan bir belge ise işaretlenebilir ve alt bölümdeki "Fason Ürün Kodu" sahasına bu alış faturasının hangi ürüne ait bir fason işlem olduğu bilgisi girilebilir. (Fason uygulamasıyla ilgili detaylı bilgi için "Yüklenilen KDV Parametreleri" başlığı incelenebilir.)

#### Yüklenilen KDV Parametreleri

"Muhasebe-Kayıt-Yüklenilen KDV Parametreleri" ekranında Yüklenilen KDV Listesi için kullanılacak genel parametreler ayarlanmaktadır.

![](../_assets/1d6412fc5f0a4bfca845.png)

Yüklenilen KDV Parametreleri ekranında "Genel" ve "Belge Kısıtları" ismiyle iki sekme bulunmaktadır.

Yüklenilen KDV Parametreleri ekranı "Genel" sekmesi üzerinde yer alan parametreler ve açıklamaları aşağıdaki gibidir:

- Alış Faturaları için Devir Baz Tarihi alanında, Yüklenilen KDV Listesi için Netsis üzerinden kullanıma ilk geçiş sırasında bu parametrenin belirlenmesi ve girişi zorunludur. Girilen tarihten önceki alış faturaları rapora dahil edilmeyecek ve kullanılmayacaktır. Bu parametre "Yüklenilen KDV Devir Girişi" ekranında girilen alış faturalarını etkilemeyecektir, devir girişi haricindeki faturalar için kısıt oluşturmaktadır. Normal şartlarda Yüklenilen KDV Listesi uygulamasına ilk geçiş sırasında tek seferlik belirlenmesi yeterledir, yani şirket devir yapıldığında değiştirilmesine gerek yoktur.
- Yüklenilen KDV Listesinde Kullanılan Alış Faturaları Değiştirilemesin parametresi, Yüklenilen KDV Listesi raporunda kullanılan alış faturalarının daha sonradan değiştirilmesini engellemek için işaretlenebilir. Çünkü bu rapor FIFO mantığına uygun olarak alış faturaları ve miktarları ile eşleştirme yaptığı için daha önceki ayların raporunda kullanılan alış faturalarındaki değişiklik sonraki aylar için tekrar raporun alınması anlamına gelmektedir. Bu tarz durumların önüne geçip kontrol sağlamak amacıyla bu parametre işaretlenebilir.
- Fason Uygulaması Kullanılsın parametresi, Üretim aşamasında fason işlem yaptıran firmalar için bu parametre işaretlenebilir.

Fason uygulaması Yüklenilen KDV uygulamasında aşağıdaki iki farklı fason yöntemi için desteklenmektedir:

- "Fason İşçilik Faturaları için" yönteminde fason işlem yapan firmaya hammaddeler gönderilmekte ve sonrasında fason operasyonlar sonucunda ortaya çıkan yarı mamul/mamul geri alınmakta, fakat bu aşamada sadece işçilik alış faturası

kesilmektedir. Yani fason işlem sonucu firmaya geri gelen yarı mamul/mamul için ayrıca bir alış faturası bulunmamaktadır. Bu şekilde gelen fason işçilik faturalarına ait KDV tutarlarının da Yüklenilen KDV Listesinde dahil edilmesi ve FIFO mantığıyla eşleştirilmesi desteklenmektedir. Bu tarz alış faturalarında kullanılan stok kodunun "Stok Kartı Kayıtları\>Ek Bilgiler Sekmesi\>Maliye Türü" sahasının "Fason" olması gerekmektedir.
- "Fason Alış Faturaları için" yönteminde fason işlem sonucunda alınan yarı mamul/mamuller için direkt olarak alış faturası kesilmektedir ve ürünler bu şekilde giriş yapılmaktadır. Bu şekilde girişi yapılan alış faturaları için de reçeteler üzerinden yapılan hammadde gereksinim ihtiyacı hesabında, ilgili fason satın alımlarına ait yarı mamul/mamul miktarları düşülerek hesaplama yapılmaktadır. Çünkü bu ürünler dışardan geldiği için bunlara ait bir hammadde ihtiyacı olmamalı ve aynı şekilde bu hammadde gereksinimlerine ait alış faturalarıyla yapılacak eşleşmeler de fason üretim oranında azalmalıdır.

"Fason Uygulaması Kullanılsın" parametresi işaretlendiğinde girilen fason alış faturalarının hangi yarı mamul/mamul kodlarına ait olduğunu belirleyebilmek/eşleştirebilmek için aşağıdaki iki alan aktif gelmektedir, alış faturası veya stok kartı üzerinde belirlenen bu alanlar sayesinde fason alışın hangi yarı mamul/mamul için yapılabildiğini belirlemek mümkün olmaktadır:

- Fason Bilgisinin Tutulacağı Yer alanı, fason alış faturalarında eşleştirme yapılacak yarı mamul/mamul kodu bilgisinin yerini belirler, "Stok Kartı" ve "Alış Faturası" şeklinde iki seçenek bulunmaktadır.
- Fason Bilgisinin Tutulacağı Saha, "Fason Bilgisinin Tutulacağı Yer" parametresine göre otomatik olarak stok kartı veya alış fatura kalemlerinde girilebilecek ek sahaları listeler (Satır açıklama, kullanıcı tanımlı sahalar, saha-tablo eşleştirmeleri gibi). Seçilecek sahaya alış faturasında fason işlem sonucunda geri dönen ürün kodu yazılacak ve bu şekilde Yüklenilen KDV Listesinde fason işlem dikkate alınacaktır.

Yukarıdaki iki parametrenin kullanımını daha kolay anlayabilmek için aşağıdaki örneği verebiliriz:

Fason işlemlerin işçilik faturası üzerinden yürütüldüğünü düşünelim ve gelen fason işçilik faturalarının Satır Açıklama-1 sahasına hangi yarı mamul için fason işlem yapıldığını giriyor olalım. Bu durumda "Fason Bilgisinin Tutulacağı Yer" parametresinde "Alış Faturası" seçeneğini seçilmeli ve "Fason Bilgisinin Tutulacağı Saha" parametresinde ise "Satır Açıklama-1" seçeneği seçilmelidir. Böylece fason işçilik faturasını girerken "Satır Açıklama-1" sahasına YM1 gibi bir değer girersek, bu fason faturanın YM1 ürünü için yapılmış olacağı anlaşılacaktır. Benzer şekilde "Fason Bilgisinin Tutulacağı Yer" parametresini "Stok Kartı" seçilerek "Stok Kartı Kayıtları" ekranındaki seçilen ek sahaya ilgili YM1 değeri girilebilir ve alış faturasında kalem bazında giriş yapmadan direkt olarak stok kartından eşleşme sağlanabilir.

- Mal ve Hizmet Adının Getirileceği Sahaya, Yüklenilen KDV Listesi raporunda "Alınan Mal ve/veya Hizmetin Cinsi" kolonunda yazacak satın alınan stok bilgisi bu parametreye getirilmektedir. Varsayılan olarak "Stok Adı" getirilmekte, ancak istenirse stok kartındaki kullanıcı tanımlı sahalar veya saha-tablo eşleştirmeleri üzerinden biri seçilerek bu alanda yazan değerlerin rapora getirilmesi sağlanmaktadır.

Yüklenilen KDV Parametreleri ekranında "Belge Kısıtları" sekmesi üzerinden rapora dahil edilecek Alış Faturaları, Satış Faturaları ve Dekont belge tipleri için ayrı ayrı filtre verilebilir.![](../_assets/75544e27779529e257a2.png)

#### Yüklenilen KDV Listesi

"Muhasebe-Rapor-Yüklenilen KDV Listesi" ekranından raporun alınmak istendiği ay/yıl bilgileri girilerek işlem yapılabilir.

![](../_assets/e2da7a422121d758761c.png)

Rapor ekranı üzerinde "Son Çalıştırılan Dönem" sahası bilgi amaçlı olarak son çalıştırılan rapor tarihini göstermekte ve pasif şekilde gelmektedir. Bu tarihten önceki dönemler için rapor çalıştırılmak istenirse "Son Çalıştırılan Dönem" sahasındaki tarihe kadar olan kayıtlar silinecek ve rapor bu şekilde çalıştırılacaktır.

"Yıl" ve "Ay" sahasında raporun çalıştırılmak istendiği tarihler çoklu seçim şeklinde birden fazla ay olacak şekilde seçilebilir, ancak ayların birbirini takip edecek şekilde seçilmesi gerekmektedir. Bu noktada örneğin Haziran ayı için rapor alınmadıysa Temmuz ayı için rapor alınmasına izin verilmemektedir, çünkü alış faturaları ile FIFO mantığına göre eşleşme sağlandığı için çalıştırılan rapor dönemlerinin de ay atlamadan alınması gerekmektedir.

"Şubeler Dahil" seçeneği sadece merkez şubelerde aktif olarak gelmektedir, bu seçenek işaretlendiğinde ilgili işletmenin bütün şubeleri için rapor çalıştırılmaktadır.

"Rapor Sonucu İhracat Faturaları İçin Filtrelensin" seçeneği işaretlendiğinde sadece ihracat satışları için yapılan faturalara ait rapor dökülmekte ve Gelir İdaresi Başkanlığına bu rapor sonuçları iletilebilmektedir. Bu şekilde bir parametrenin olmasının sebebi şu şekildedir: Normal şartlarda Yüklenilen KDV Listesi seçilen ay/yıl içindeki bütün satış faturalar için çalışmaktadır, çünkü satın alımı yapılan herhangi bir hammadde birden fazla farklı mamul reçetesinde yer alıyor olabilir ve bu mamullerden bazıları ihraç edilirken bazıları yurt dışına satılıyor olabilir. Bu sebeple hammadde alış faturalarını FIFO mantığına göre doğru şekilde eşleştirme için bütün satış faturaları dikkate alınmaktadır, ancak Gelir İdaresi Başkanlığına verilecek raporu için ilgili parametre işaretlenerek filtre verilebilir.

Rapor butonuna tıklandıktan sonra gelen sonuçlar aşağıdaki gibi olmaktadır.

![](../_assets/60dcc6267e8b4618d38c.png)

Rapor üzerinde çalıştırılan her ay/yıl için "Vergi Dairesi Rapor" ve "Rapor Detay" şeklinde iki sayfa basılmaktadır.

"Vergi Dairesi Rapor" sayfasında Gelir İdaresi Başkanlığına verilecek formata uygun olacak şekilde rapor gösterilmektedir, "Rapor Detay" sayfasında ise alış fatura kalemleri ve bu kalemlerin satışı yapılan mamul kodları bazında detayları gösterilmektedir.

"Vergi Dairesi Rapor" sayfasında yer alan kolonlar ve açıklamaları aşağıdaki gibidir:

- Sıra No kolonunda 1'den başlayarak artan sırada otomatik olarak bir değer gösterilmektedir.
- Alış Faturasının Tarihi kolonunda rapora dahil olan, yani satış faturalarından doğan ihtiyaca göre FIFO mantığıyla eşleştirilen alış faturasının tarih bilgisi gösterilmektedir.
- Alış Faturasının Serisi kolonunda, ilgili alış faturası e-belge ise bu alan boş bırakılmakta, aksi durumda alış faturasının seri bilgisi gösterilmektedir.
- Alış Faturasının Sıra Nosu kolonunda, ilgili alış faturası e-belge ise bu alana resmi belge numarası basılmakta, aksi durumda alış faturasının serisi haricindeki numara sıfırlar çıkartılarak gösterilmektedir.
- Satıcının Adı-Soyadı/Unvanı kolonunda, alış faturasındaki cari isim bilgisi gösterilmektedir.
- Satıcının Vergi Kimlik Numarası/TC Kimlik Numarası kolonunda, alış faturasındaki carinin vergi kimlik numarası veya TC Kimlik numarası gösterilmektedir.
- Alınan Mal veya Hizmetin Cinsi kolonunda, alış faturasındaki stok bilgisi (Bu saha "Yüklenilen KDV Parametreleri" ekranındaki "Mal ve Hizmet Adının Getirileceği Saha" üzerinden ayarlanabilir) Tek bir fatura üzerinde birden fazla kalem varsa ve raporda bu kalemler için kullanım bulunuyorsa virgül ile ayrılarak gösterilir.
- Alınan Mal veya Hizmetin Miktarı kolonunda, alış faturasındaki kalemlerin kullanılan/eşleştirilen miktarları gösterilmektedir. Birden fazla kalem gösteriliyorsa virgül ile ayrılarak raporlanmaktadır.
- Alış Faturasının KDV Hariç Tutarı kolonunda, alış faturasının "Toplamlar" sekmesindeki KDV hariç tutarı gösterilmektedir.
- Alış Faturasının KDV'si kolonunda Alış faturasının "Toplamlar" sekmesindeki KDV tutarı gösterilmektedir.
- Bünyeye Giren Mal ve/veya Hizmetin KDV'si kolonunda alış faturasında kullanılan/eşleştirilen kalemlere ait toplam KDV tutarı bu alanda gösterilmektedir.
- GGB Tescil No'su (Alış İthalat İse) kolonunda Alış faturası ithalat tipinde ise GGB (Gümrük Giriş Belge) numarası gösterilmektedir.

**Not:** İthalat faturalarında KDV tutarı bulunmamasına rağmen "İthalat Masraf Dekont Kayıtları" veya "Dekont Kayıtları" ekranlarından girilen masraf kayıtları Export Referans No üzerinden alış faturalarıyla eşleştirilmekte ve bu masraflara ait KDV tutarları rapora dahil edilmektedir. Eğer "İthalat Masraf Dekont Kayıtları" ekranından "Masraf Dağıtımı" butonuyla stok bazında masraf dağıtımı yapılmış ise bu tutarlar kullanıcının belirlediği şekilde alınmakta, aksi durumda alış faturalarındaki kalemlerin tutarları oranında doğru orantılı olacak şekilde masraf tutarı otomatik olarak dağıtılmakta ve bu şekilde rapora dahil edilmektedir.

- Belgeye İlişkin İade Hakkı Doğuran İşlem Türü alanında, satış faturasında girilen istisna kodu bu alanda gösterilmektedir, eğer kullanılan/eşleştirilen alış faturası birden fazla farklı satış faturasına denk geliyorsa ve satış faturalarının istisna kodları birbirinden farklı ise virgül ile ayrılarak gösterilir.
- Yüklenim Türü alanında, varsayılan olarak "Doğrudan Yüklenim" şeklinde gösterilmektedir, diğer türlerin şu anda desteği bulunmamaktadır.
- Belgenin İndirime Konu Edildiği KDV Dönemi alanında, alış faturasının tarih bilgisine göre gösterilmektedir. Örneğin alış faturasının tarihi 12.02.2020 ise bu alanda "202002" değeri gösterilecektir.
- Belgenin Yüklenildiği KDV Dönemi alanında, yüklenilen KDV Listesinin çalıştırıldığı dönem bilgisi gösterilmektedir. Örneğin rapor 05/2020 için çalıştırılıyor ise bu alanda "202005" değeri gösterilecektir.

#### Yüklenilen KDV Listesi Silme

"Muhasebe-İşlemler-Yüklenilen KDV Listesi Silme" ekranı üzerinden daha önceden çalıştırılmış olan rapor sonuçlarının toplu şekilde silinebilmesi sağlanmaktadır.

![](../_assets/6f386325fd856f10ef54.png)

Ekran üzerinde "Bitiş Dönemi" sahasında otomatik olarak son çalıştırılan Yüklenilen KDV Listesi raporuna ait tarih bilgisi pasif saha olarak bilgi amaçlı gösterilmektedir. "Başlangıç Dönemi" sahasında girilen ay/yıl bilgisinden itibaren bitiş dönemine kadarki bütün sonuçlar toplu halde silinmektedir.
