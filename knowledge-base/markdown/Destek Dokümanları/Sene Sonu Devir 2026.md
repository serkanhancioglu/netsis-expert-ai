---
title: "Sene Sonu Devir 2026"
page_id: ""
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Sene Sonu Devir 2026"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Sene Sonu Devir 2026"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTUwMzQ0MjRjLTg4MjQtNGU3My1iZGFmLWU3ZGY2MGVkYzU2NSZsaW5rPTJjOGFjMjU3LWM2ZTctNDk4NS1hZWVhLTcxYjRjZTA2ODUwOSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=5034424c-8824-4e73-bdaf-e7df60edc565&link=2c8ac257-c6e7-4985-aeea-71b4ce068509&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "sene-sonu-devir-2026.html"
source_version: ""
source_bytes: 1250298
fetched_at: "2026-09-13T04:21:58+00:00"
generator: "netsis-scraper 1.0.0"
---
# Sene Sonu Devir 2026

## 1-Sene Sonu Devir Modülü

Netsis Wings Entegre, Netsis Wings Entegre Pro, Netsis 3 Standard, Netsis Wings Standard, Netsis 3 Enterprise ve Netsis Wings Enterprise ürünlerinde her şirket bir cari yılı temsil eder ve her yeni cari yıl için yeni bir şirket yaratılır. Program, yeni sene kayıtlarının eski sene kayıtlarının devamı olarak aynı şirkette oluşturulmasına izin vermektedir.

Ancak "**Muhasebeye Doğrudan Aktarım**" özelliğinin kullanıldığı şirketlerde, modüllerin yeni yıl kayıtlarının mutlaka devir ile oluşturulan yeni yıl şirketine girilmesi gerekmektedir (Fatura, çek, banka, dekont vb).

Örneğin, fatura modülünde muhasebeye doğrudan aktarım özelliği kullanılıyorsa, yeni yıla (2025) ilişkin fatura belgeleri yeni yıl şirketine girilmelidir. Aksi durumda geçmiş yıla giriş yapılan yeni yıl belgeleri, modül devirlerinde dikkate alınmayacaktır ve yeni yıla aktarılmayacaktır. Eski şirketteki yeni yıl kayıtları, doğrudan muhasebeye işlenmiş olacak ve eski yıl şirketinde muhasebe kayıtları, yeni yıl muhasebe kayıtlarını da içerecektir. Bu durumun oluşmaması için muhasebeye doğrudan aktarım özelliğinin kullanıldığı modüllerin yeni yıl kayıtları, mutlaka yeni yıl şirketine girilmelidir.

Yıl sonunda yeni sene işlemlerine başlamadan önce aşağıdaki iki yöntemden birini belirleyip buna göre devir işlemleri planlanmalıdır.

- Yeni senenin başında, yeni sene şirketi hazırlanıp tüm modüller için yeni seneye ait kayıtlar yeni sene, eski seneye ait kayıtlar eski sene şirketine girilerek devam edilebilir. Modül bazında devirler (stok devri, cari devir, vb.) ise, daha ileri bir tarihte yapılıp devir kayıtlarının otomatik olarak yeni sene şirketine aktarılması sağlanabilir.
- Muhasebeye doğrudan aktarım özelliği kullanılmıyor ise, eski sene şirketinde, yeni sene kayıtları girilmeye devam edilebilir ve modül bazında devirlerin (stok devri, cari devir, vb.) yapılacağı tarihe kadar bu şekilde devam edilebilir. Bu tarihte yeni sene şirketi yaratılıp modül devirleri yapılabilir. Ancak bu çalışma şeklinde, devir yapılma tarihine kadar eski sene şirketinde muhasebe entegrasyonu ve muhasebede fiş girişi yapılmamalıdır ve yeni sene şirketinin hazırlanması ile modül devirleri aynı tarihte yapılmalıdır.

Yeni sene şirketinin hazırlanması, Yeni Yıl Kopyalama bölümünde anlatılmaktadır.

- Modül devirleri istenirse, eski seneden yeni seneye program tarafından otomatik olarak değil, her modülün kendi devir hareketlerinin kullanıcı tarafından elle işlenmesiyle de yapılabilir.

Modül devirleri ister program tarafından ister kullanıcı tarafından yapılıyor olsun yeni sene şirketinin hazırlanması için devir öncesi hazırlık (yeni yıl kopyalama) işlemi mutlaka yapılmalıdır.

- Yeni sene şirketi hazırlık ve modül bazında devir işlemlerinin hepsi **eski** **sene**

**şirketinden** yapılmalıdır.

- Yeni sene şirketinde devir yapılmadan muhasebe kayıtlarına başlanacaksa, sonradan oluşturulacak açılış fişi için bir yevmiye fiş numarası ayrılmalıdır.
- Denetim Listeleriyle, modül bazında devirler sonrasında ilgili modülün devir tutarları ile muhasebe açılış fişindeki bağlantılı hesapların devir tutarları kıyaslanarak, farklılıklar tespit edilebilir.

**ÖNEMLİ** **UYARI** !!

Netsis Online E-fatura veya Entegratör kullanan firmaların yeni yıla ve eski yıla ait gelen e-faturalarının doğru şirketlere aktarımının sağlanabilmesi için **en geç 31.12.2025** tarihinde yeni yıl şirketlerini açması gerekmektedir.

- Yeni yıl kopyalama işlemi ile TBLEIMZAREG tablosuna yeni yıl şirketine ait kayıt otomatik olarak atılmaktadır. Efaturaayarlar.exe'den yeni yıl şirketi için sertifika tanımlamasına gerek yoktur. Entegratör kullanan firmalar için, önceki yıl data bilgisi alanına program tarafından eski yıl şirket ismi getirilmektedir.
- Online E-Fatura kullanan firmaların Yeni Yıl Kopyalama işlemi haricinde, yeni yıla ve eski yıla ait gelen faturalarının doğru şirketlere aktarımının sağlanabilmesi için web.config dosyasının düzenlemesi gerekmektedir. 31.12.2025 tarihi öncesinde devir yapılması durumunda web.config dosyası 01.01.2026 tarihine kadar geçen süre için değiştirilmemelidir.

Bunu yapmanın iki yöntemi var:

1. Netsis' in kurulu olduğu dizinde bulunan Servis klasöründeki Efaturaayarlar.exe dosyası çalıştırılır ve işlemler menüsünden Web Servis Ayarları seçilir. Açılan ekranda sol tarafta görünen Default Web Site' ın altında değişiklik yapılacak olan kayıt seçilir. Veritabanı bilgilerinin olduğu satırdaki ... işaretine basılır, açılan ekranda **VT Adı (Şirket)** bölümüne yeni yıl şirketinin (**2026)** adı yazılır. **Önceki Yıl Datası** yazan bölüme de eski yıl şirketinin **(2025)** ismi yazılır ve kaydet butonuna basılır. Böylece web.config dosyası düzenlenmiş olur.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/04731a1e-b485-409c-b0a2-501509ad4a80/ssd2026resim1.png)

\2. Efatura web servisinin kurulduğu sunucu bilgisayarın C:\\inetpub\\wwwroot\\NetsisEFatura dizininde bulunan Web.config dosyası, notepad ile açılıp manuel düzenlenebilir. Buna göre **OldSchema** bölümüne **2025** şirketi, **Schema** ve **initial catalog** bölümlerine **2026** şirketinin adı yazılmalı ve kaydedilmelidir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/12ba8070-71b9-48d4-92b7-818c849cf070/ssd2026resim2.png)

- 31.12.2025 tarihine kadar yeni yıl şirketi açılmamışsa, program içerisinde **fatura tarihinin yılı \<sistem strong="" tarihinin="" y=""\> kontrolü yapılır ve 2025 faturalarını almaya devam eden firmaların faturaları 2024 yılı şirketine gitmiş olur. Bu durumda eski yıl şirketine düşen faturalar tespit edilip yeni yıl şirketine aktarılması gerekmektedir.**
- Entegratör kullanımında E-fatura kayıtlarının yeni yıl kopyalama sonrasında, faturanın ilgili olduğu yıl şirketine kaydedilmesi sağlanır. Bu çalışmada özel dönem kullanımı da desteklenmektedir.

### 1.1 Yeni Yıl Kopyalama

Yeni yıl kopyalama, yeni yılda çalışılacak şirket bilgisinin oluşturulmasını ve eski yıl şirketinde bulunan sabit bilgilerin bu şirkete aktarılmasını sağlar.

Yeni Yıl Kopyalama işlemi Netsis 3 Enterprise, Netsis Wings Enterprise ürünlerini kullanan ve birden fazla işletme tanımlanmış olan firmalarda merkez işletmenin merkez şubesinde, Netsis Wings Entegre, Netsis Wings Entegre Pro, Netsis 3 Standard, Netsis Wings Standard ürünleri ile işletme tanımlanmamış Netsis 3 Enterprise, Netsis Wings Enterprise ürünlerinde, merkez şubede çalıştırılmalıdır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/f3c7aede-18a0-4a3e-b739-a28fc8d74f99/ssd2026resim3.png)

#### Devir Şirketi

Yeni yılda kullanılacak şirketin isminin girileceği sahadır. Bu sahaya girilen şirketin daha önceden açılmamış olması gerekmektedir.

#### Devir Yılı

Bu sahaya devredilecek eski yıl bilgisi girilmelidir.

#### Mali Başlangıç Ayı Dikkate Alınsın

Muhasebe modülünde parametrelerde mali başlangıç ayı 1' den farklı olan şirketler için işaretlenmesi gereken parametredir. Bu parametre işaretlendiğinde Yeni Yıl Kopyalama ve modül bazında devirler özel döneme göre yapılacaktır.

#### Önceki yıl fiyat listeleri yeni yıla aktarılsın

Geçmiş yıl fiyat listelerinin, yeni yıl şirketinde izlenebilmesi istenildiğinde işaretlenmesi

gerekmektedir.

#### Sadece Sınır Tarihinden Sonraki e-Mutabakat Kayıtları Yeni Yıla Aktarılsın

Tüm e-Mutabakat kayıtları yerine, verilen sınır tarihinden sonraki e-Mutabakaların yeni yıl şirketine aktarıması isteniyorsa ilgili parametre işaretlenmeli ve sınır tarihi girilmelidir.

#### Veritabanı yedeği için başka dizin kullan

Yeni yıl kopyalama işleminde backup/restore işlemi yapıldığı için SQL server yüklü makinenin diskinde yeterli yer olmalıdır. Yeterince yer olmaması halinde, istenirse veritabanı yedeği için başka dizin kullan seçeneği işaretlenerek yedeğin alınması için boş alana sahip olan diğer diskteki bir dizin verilebilir.

#### Veritabanı Yedeği Sıkıştırılsın

Yeni yıl kopyalama işleminde backup/restore işlemi sırasında, alınan backup dosyasının sıkıştırılarak diskte yerden tarsarruf edilmesi sağlanmaktadır.

#### Taslak İşlemleri

Devir işlemlerinde verilen kısıtların kaydedilmesi ve daha sonraki senelerde tekrar aynı kısıtların kullanılabilmesi için kısıtlar verildikten sonra Taslak İşlemleri menüsündan Sakla ve tekrar kullanılabilmesi için Oku adımları kullanılmaktadır.

#### Yeni Yıl Kopyalama işlemi sırasında program tarafından yapılan işlemler;

- Eski senenin tüm bilgilerinin (table, view, vb.) yedeği alınacaktır (BACKUP).
- Yedeklenen bu bilgiler, devir şirketine yüklenecektir (RESTORE).
- Yeni yıl şirketindeki hareket kayıtları iptal edilecek, sabit kayıtlar ise kalacaktır.
- Bazı tablolarda ise, birtakım koşullara bağlı iptaller yapılacaktır. Örneğin koşul tablolarında, kapatılmış koşullar iptal edilip, aktif koşullar yeni senede kullanılmak üzere bırakılacaktır.
- Örneğin, ihracat ve ithalat dosyaları ile ilgili tablolarda, dosyası kapatılmış olan kayıtlar yeni sene şirketine aktarılmayacaktır.

Bu türden işlem gören tablolar aşağıdaki gibidir:

TBLKOSULEK,TBLKOSDETAY,TBLKOSGENEL,TBLDEPSAYIM,TBLMUHAGEC, TBLNAKLIYEBELGELINK,TBLNAKLIYE,TBLTAHSILAT,TBLFIYFARKMAS,TBLFATUIRS, TBLFARKLITESLIM,TBLTARTIMBLG,TBLTAHSILAT,TBLKASA,TBLMUSTAHSI,TBLREPLANIS, TBLSAYIM,TBLSTOKFIAT,TBLREVERRORLOG,TBLSTOKURS,TBLBNKTEMTRA, TBLBNKTEMSABIT,TBLDAMGAVERGISI,TBLKDVBEYAN,TBLMUHTASAR,TBLFATUVADE, TBLFATUEK,TBLKOSULMAS,TBLDEKOTRA,TBLDEKOMAS,TBLCEKSENDEK, TBLDAGAKTARIMLOG, TBLIHRDOSYAMAS, TBLITHDOSYAMAS

- Eski yıla ait hareket kayıtlarının tamamı silinen tablolar ise:

TBLSMSTRA,TBLSMSMAS,TBLMAKMALIYET,TBLMAKSARF,TBLBKMBIS,TBLBKMSBPER,TBL BKMSBSTOK,TBLBKMTRA,TBLBKMTALEP, TBLBKMPLAN,TBLBKMSOZDET,TBLMAKBKM,TBLBKMSOZMAS,TBLKRTSOZKST, TBLKRTSOZTRA,TBLKRTSOZMAS,TBLFORECAST,TBLMPS,TBLNPMLOG,TBLSSATIRAC, TBLKKMAS,TBLHIZMETMALIYETMAS,TBLHIZMETPRIMTANIM,TBLHESTEMP,TBLIMALAT,TB LKAMBBCEK,TBLBCEK,TBLKAMBBSEN,TBLBSEN, TBLKAMBMSEN,TBLMSEN,TBLKAMBMCEK,TBLMCEK,TBLODEEMIR,TBLCAHAR, TBLOZELHESAP,TBLCEKSENLOG,TBLDEPDURUM,TBLSIPAMAS,TBLSIPATRA, TBLNETSISLOG,TBLMALISARF,TBLMALIYET,TBLMUHARES,TBLMUHMAS,TBLMUHFIS, TBLMUPLANSUBE,TBLSTHAR,TBLDEPHAR,TBLSTOKPH,TBLISEMRI,TBLISEMRIREC, TBLUAKMAS,TBLBAGLANTI,LOGQUERYINFO,TBLAL12,TBLAL12DUMY, TBLBNKHESTRA,TBLBNKLOGTRA,TBLBORDROMAS,TBLDAGDISPATCH,TBLDAGKMTAKIP, TBLDAGPENETRASYON,TBLDAGPLASZIYARET,TBLDAGZIYRAPORDETAY,TBLSEVKMAS, TBLSEVKTRA,TBLTEKLIFMAS,TBLTEKLIFTRA,TBLBCK_MRP,TBLBCK_MRP_DETAIL, TBLBCK_MRPPLAN,TBLBCK_MRPSIP,TBLMRPSIP,TBLKAPASITE,TBLMRP,TBLMRP_DETAIL, TBLSERITRA,TBLACIKREC,TBLDAGFUNCHIST,TBLDAGFUNCHISTXML,TBLDZNBASIMLOG, TBLBFORMU,TBLCRMFORECAST,TBLCRMHEDEF,TBLFATKALEMILISKI,TBLKUMGENEL, TBLFORECASTHAZIRLIK,TBLIMZALOG,TBLBNKMSRF,TBLMPSKAPASITE, TBLPOSAKTARILANLAR, TEMP_MUHAGEC,TBLKRTTHSLT,TBLISEMRIEK, TBLMSENPARCA,TBLBSENPARCA,TBLMCEKPARCA,TBLBCEKPARCA, TBLHIZMETMALIYETFISTRA,TBLHIZMETMALIYETSTHARFISTRA,TBLMRPSIPBELGELOG, TBLMRPSIPEKRMAS,TBLMRPSIPEKRTRA,TBLMRPSIPBAGLANTI,TBLBCK_MGPMAS,

TBLISEMRIREZERVESTOK,TBLMUHFISEK,TBLEFATMAS,TBLEFATURA,TBLEFATYANIT,TBLE FATZARF, TBLEDEFTER, TBLEFATKALEMTAX, TBLEFATMASTAX,TBLEARSIV..

- Yeni sene şirketinde, her bölüme ait sabit kayıtlarda (Stok kartı kayıtları, Cari hesap kayıtları, Hesap planı, Banka Hesap Kayıtları), eski seneden oluşmuş toplam giriş, çıkış ve bakiye bilgileri sıfırlanacaktır.

Devir şirketi ve devir yılı sorgulamaları geçildikten sonra, ekrana aşağıdaki gibi bir onaylama ekranı gelecektir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/d6c2c269-026c-436c-8a99-9adce4f63d3c/ssd2026resim4.png)

"Evet" tuşuna basıldığında, uzun sürebilecek birtakım işlemler program tarafından yapılmaya başlanacaktır.

#### Yeni Yıl Kopyalama Sırasında Oluşabilecek Hatalar

İşlem sırasında çıkabilecek hatalar İşlem Sonucu sayfasında görüntülenecek ve farenin sağ tuşuna basılarak dosyaya kaydedilebilecektir. Yeni Yıl Kopyalama işlemi, devir şirketi yaratıldıktan sonra, herhangi bir hatadan dolayı yarım kalabilir. İşlemin kesilmesine sebep olan problem çözüldükten sonra,

- Yeni sene için açılmış olan şirketi sıfırlayarak ya da yeni yıl kopyalama işlemine kaldığı yerden devam etmek mümkündür.

Açılmış olan şirketi sıfırlayarak yeni yıl kopyalama işlemine yeni baştan başlamak için,

*şirket* *silme* işlemi ile yeni şirket silinmelidir.

Kalınan yerden yeni yıl kopyalama işlemine devam etmek için, işlem tekrar çalıştırılarak,

sorgulanan sahalara daha önceden girilen bilgiler girilmeli ve "Evet" butonuna basılmalıdır.

Bu durumda, işleme kalınan yerden devam etmek istenip istenmediğini sorgulayan bir ekran gelecektir. "Evet" butonuna basılması durumunda, yeni yıl şirketi tekrar kopyalanmadan devir işlemine devam edilecek.

![](../_assets/3642be27cb1142f8ecc3.png)

İşlemler bittiğinde, modül devirleri öncesi, yeni sene kayıtlarına başlama ortamının hazırlanması işlemi tamamlanmış olur. İstenirse eski senenin kayıtları bitene kadar, hiçbir modülün devri yapılmadan eski sene şirketinde ve yeni sene şirketinde ayrı ayrı çalışılarak kayıtlara devam edilebilir. Eski senenin devir kayıtları, yeni sene bilgilerine, eski sene kapatılıp devir yapıldığında aktarılabilir. İstenirse modül devirleri programın içinden yapılmayıp, açılan yeni sene şirketinde elle işlenebilir.

Yeni yıl kopyalama işlemi ile devri oluşturulan eski şirkete girerken "Şirket devri yapılmıştır." şeklinde uyarı mesajı verilmektedir. Bu sadece bilgilendirme amaçlıdır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/0ca66e78-f9e8-4155-840d-b639d9b6d1f2/ssd2026resim5.png)

***Not:*** Önceki setlerde Yeni Yıl Kopyalama ekranından ulaşılan Dinamik Kodlama ekranında ThazırlıkFrm nesnesine OnDevirStart/OnDevirEnd eventları ve veritabanı seviyesinde kullanılmak üzere NSP_BEFOREDEVIR/NSP_AFTERDEVIR prosedürleri eklenmiştir.

#### Sabit Kayıt Kontrolü

Sabit Kayıt Kontrolü, Netsis 3 Enterprise, Netsis Wings Enterprise ürünlerini kullanan ve birden fazla işletme tanımlanmış olan firmalarda merkez işletmenin merkez şubesinde, Netsis Wings Entegre, Netsis Wings Entegre Pro, Netsis 3 Standard, Netsis Wings Standard ürünleri ile işletme tanımlanmamış Netsis 3 Enterprise, Netsis Wings Enterprise ürünlerinde, merkez şubede çalıştırılmalıdır.

Yeni yıl kopyalama sonrasında eski yıl şirketinde açılmış sabit kartların, yeni yıl şirketinde hızlıca oluşturulmasını sağlar. Çalıştırılmadığı durumlarda, eğer yeni açılan kartlara hareket girildiyse modül devirlerinde hata verecek ve devir yapılamayacaktır.

Cari, Stok ve Muhasebe devir işlemleri ekranlarında da "Sabit Kayıt Kontrolü" desteği bulunmaktadır. Böylece kontrolün, modül devri esnasında yapılması sağlanabilir.

Ayrıca fiyat güncellemesi yapılsın seçeneği ile daha önce aktarılan stok sabit kartlarında fiyatı değişen stokların fiyatı, yeni sene şirketinde güncellenebilir.

Ayrıca reçete bilgileri, barkod bilgileri, proje, plasiyer bilgileri, referans kodları, kullanıcı ve kullanıcı grupları, maliyet muhasebesi mamul ana ve grup hesapları, dinamik depo hücre tanımları ve fon tanımları için de sabit kayıt kontrolü yapılmaktadır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/8f7e39b7-a65e-471b-a75d-d15056f41fbf/ssd2026resim6.png)

Eski sene şirketinde bulunup, yeni sene şirketinde de tanımlanmasını istediğiniz sabit bilgi türü işaretlenerek yeni sene şirketinde oluşturulmaktadır.

#### Taslak İşlemleri

Devir işlemlerinde verilen kısıtların kaydedilmesi ve daha sonraki senelerde tekrar aynı kısıtların kullanılabilmesi için kısıtlar verildikten sonra Taslak İşlemleri menüsündan Sakla ve tekrar kullanılabilmesi için Oku adımları kullanılmaktadır.

### 1.2 Lojistik/Satış

### 1.2.1 Talep/Teklif Devir

Talep/ Teklif Devir işlemi her işletme ve şube için ayrı ayrı çalıştırılmalıdır.

Talep/ Teklif uygulamasını kullanılması halinde, stok devrinden önce mutlaka Talep/ Teklif devri yapılmalıdır.

Eski sene şirketindeki teslimatı yapılmamış talep ve tekliflerin takibine, yeni senede devam edebilmeniz için talep ve tekliflerin yeni sene şirketine aktarılması sağlanır.

#### Devir Baz Tarihi

Talep/ Teklif devri için baz alınacak tarihtir. Devir baz tarihi olarak verilen tarihten önceki talep ve teklifler (talep/ teklif kayıt tarihi baz alınır) sadece teslimatı tamamlanmamış olanları ile bu tarihten sonraki tüm talep/ teklif kayıtları yeni sene şirketine aktarılır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/bcb1331d-2b10-49e7-9ede-8eb6d2aa6a35/ssd2026resim7.png)

#### Taslak İşlemleri

Devir işlemlerinde verilen kısıtların kaydedilmesi ve daha sonraki senelerde tekrar aynı kısıtların kullanılabilmesi için kısıtlar verildikten sonra Taslak İşlemleri menüsündan Sakla ve tekrar kullanılabilmesi için Oku adımları kullanılmaktadır.

### 1.2.2 Sipariş Devir

Sipariş Devir işlemi, her işletme ve şube için ayrı ayrı çalıştırılmalıdır. Sipariş uygulamasının kullanılması halinde, stok devrinden önce mutlaka sipariş devri yapılmalıdır.

Eski sene şirketindeki teslimatı yapılmamış siparişlerin takibine, yeni senede devam edebilmek için siparişlerin yeni sene şirketine aktarılması gerekir.

#### Devir Baz Tarihi

Sipariş devri için baz alınacak tarihtir. Devir baz tarihi olarak verilen tarihten önceki siparişlerin (sipariş kayıt tarihi baz alınır) sadece teslimatı tamamlanmamış olanları ile bu tarihten sonraki tüm sipariş kayıtları yeni sene şirketine aktarılır.

#### Sipariş Tipi

Sipariş devrinin müşteri siparişleri, satıcı siparişleri şeklinde ayrı ayrı ya da tümünün aynı anda yapılabilmesi için kullanılır.

#### Parçalanmış Siparişler Devredilsin

Bu parametre ile, merkezden girilen ve şube kodları verilerek şubeler bazında parçalanmış siparişlerden teslimatı tamamlanmamış olanlarının, devir şirketine aktarılması sağlanır. Merkez işletme veya şubenin siparişleri devrediliyorsa, bu saha işaretlenmiş olarak gelecektir ve değişiklik yapılamayacaktır. Ancak merkez olmayan bir işletme veya şubenin siparişleri devrediliyorsa bu alan işaretlenemeyecektir. Bunun sebebi ise, parçalı siparişlerin sadece merkezden girilebilir olmasıdır.

Sipariş devri yapıldıktan sonra, devir işlemi tekrar çalıştırılabilir. Bu durumda önceden devredilen kayıtlar tekrar devredilmeyecek, yeni kayıtlar yeni yıl şirketine aktarılacaktır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/336686ea-9532-4d6f-8eb3-44191c8decfe/ssd2026resim8.png)

#### Taslak İşlemleri

Devir işlemlerinde verilen kısıtların kaydedilmesi ve daha sonraki senelerde tekrar aynı kısıtların kullanılabilmesi için kısıtlar verildikten sonra Taslak İşlemleri menüsündan Sakla ve tekrar kullanılabilmesi için Oku adımları kullanılmaktadır.

### 1.2.3 Stok Hareket Devri

Netsis Wings Entegre, Netsis Wings Entegre Pro, Netsis 3 Standard, Netsis 3 Enterprise, Netsis Wings Standard ve Netsis Wings Enterprise ürünlerimizde eski versiyonlarımızda farklı ekranlar altında bulunan serili ve serisiz stok devri ekranları Stok Hareket Devri adı ile tek bir ekranda farklı iki sekme altında birleştirilmiştir. Eski ekranlarımızın kullanılmak istenildiği durumda DEVIR/ STOK_DEVIR_ESKI_EKRAN özel parametresi kullanılabilir.![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/b85cd3a1-5af5-423e-82fd-63cccdf23ff6/ssd2026resim9.png)

#### Devirden Sonra Stok Hareket Kontrol İşlemi Çalıştırılsın

Yeni yıl şirketine stok devir hareketleri aktarıldıktan sonra, yeni yıl şirketinde stok hareket kontrolün otomatik olarak çalıştırılması için bu seçenek işaretlenmelidir.

#### Sabit Kayıt Kontrolü Yapılsın

Bu seçenek işaretlendiğinde eski sene şirketinde olup yeni sene şirketinde olmayan stok kayıtları devir öncesinde yeni sene şirketinde tanımlanacaktır. Sabit Kayıt Kontrolü işlemi ayrıca ortak işletmeden daha detaylı olarak da yapılabilmektedir.

#### İrsaliyeler Devredilsin

Bu seçenek işaretlendiğinde stok bakiyesi irsaliye hareketleri hariç olarak hesaplanıp yeni yıl şirketine aktarılmaktadır. Ardından irsaliye belgeleri, irsaliye stok hareket ile birlikte yeni yıl şirketine aktarılacak ve eski – yeni sene bakiye tutarlılığı sağlanacaktır.

![](../_assets/60cb4c4e97aecec63114.png)

### 1.2.3.1 Serisiz Devir Parametreleri

Serisiz stok devri, seri uygulaması kullanmayan firmalar tarafından uygulanacaktır. Sadece Çıkışta seri takibi yapılıyor ise devir, Serisiz Stok Devri adımından yapılmalıdır. Ancak seri bilgileri aktarılmayacaktır.

Serisiz Stok Devir işlemi, her işletme ve şube için ayrı ayrı çalıştırılmalıdır.

Burada stok sabitlere bağlı hareketlerin devri yapılacak, sonuç devir hareketi/hareketleri yeni sene şirketindeki stok hareketlerine işlenecektir. Sipariş ve talep/teklif takibi kullanılıyor ise ve sipariş ile talep/teklif devirleri henüz yapmadı ise, stok devrini yapmadan önce sipariş ve talep/teklif kayıtları devredilmelidir.

Ayrıca; Esnek Yapılandırma uygulamasının kullanıldığı firmalarda, stok hareketleri yapılandırma kodları bazında kırılımlı olarak program tarafından oluşturulacaktır. Lokal Depo Uygulaması olan firmalarda, lokal depolara göre devir işlemi, stok devri sırasında program tarafından yapılacağı için lokal depolardaki tüm çalışmaların bitirilmiş olması gereklidir. Maliyet türü FIFO/LIFO seçilmiş olan firmalarda lokal depo uygulaması kullanılıyor ise, aynı maliyet fiyatı ile lokal depo kırılımlı olarak devir hareket/hareketleri yeni sene şirketine işlenecektir.

#### Genel Parametreler Devir Baz Tarihi

Stok devri için baz alınacak tarihtir. Bu sahaya yılın son günü otomatik olarak program tarafından getirilecektir. Devir baz tarihinden önceki stok hareketleri, seçilen maliyet türüne göre devredilir. Bu tarihten sonraki hareketler aynen yeni şirkete aktarılır.

#### Devir Tarihi

Yeni şirkete aktarılacak stok devirleri için, kullanılması istenen tarihin girileceği sahadır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/d7665248-1309-40bf-8e09-553c961eddfc/ssd2026resim10.png)

#### Maliyet Türü

Devir, FIFO (ilk giren ilk çıkar), LIFO (son giren ilk çıkar), Ağırlıklı ortalama, Hareketli ortalama, Aylık ağırlıklı ortalama, Maliyet Muhasebesi ve Alış fiyatı maliyet türlerinden biriyle yapılabilmektedir.

***Dikkat!*** Maliyet Muhasebesini kullanan firmaların maliyet türü olarak Maliyet Muhasebesi Fiyatı' nı seçmeleri gerekmektedir. Bu durumda stok devrinde stok kartlarındaki maliyet fiyatları baz alınacaktır.

#### İthalat/İhracat Hareketleri Aktarılmasın

Fatura modülünde bulunan "İhracat/ İthalat miktarları stoklara geçsin" parametresinin kullanıldığı durumlarda, bu parametre işaretlenerek devir yapıldığında kapatılmamış ithalat/ihracat kayıtları yeni sene şirketine aktarılmayacaktır.

"İhracat/ İthalat miktarları stoklara geçsin" parametresi kullanılmıyorsa bu seçenek işaretlenmeyip, sadece İhracat/ İthalat Devri işlemi çalıştırılacaktır.

#### Dinamik Depo İçin Devir Yapılsın

Dinamik depo modülü kullanan firmalarda merkez işletme ya da şubede işaretli olarak gelecek ve müdahale edilemeyecektir. Devir için verilen tarih itibarı ile hücre bakiyeleri yeni seneye devir olarak işlenecektir.

#### Eksi Bakiyeliler Devredilsin

Bakiyesi eksiye düşmüş olan stokların da yeni yıl şirketine aktarılması isteniyorsa işaretlenmesi gereken seçenektir. İşaretlenmediği durumda eksi bakiyede olan stokların devri yeni yıl şirketine aktarılmayacaktır.

#### Proje Kırılımlı Devir

Bu seçenek işaretlenerek devir yapıldığında, stok bakiyeleri yeni yıl şirketine proje kırılımlı olarak aktarılmaktadır. Eğer işaretlenmeyip rehberden bir proje kodu seçilip devredilirse, yeni yıl şirketinde oluşan tüm stok hareketlerine bu proje kodu yazılacaktır. Seçenek işaretlenmez ve rehberden bir proje kodu seçimi yapılmaz ise de yeni yıl şirketindeki stok hareketlerin proje kodu sahaları boş olacaktır.

#### Dövizli Stok Devri İçin

Dövizli stok devri, FAS52, IAS29 veya Enf.Muh. Seçeneklerinden birinin kullanılması durumunda mutlaka gereklidir. Dövizli stok devri yapabilmek için öncelikle maliyet türü olarak Aylık Ağırlıklı Ortalama, FIFO, LIFO veya Maliyet Muhasebesi Fiyatı seçeneklerinden birinin işaretlenmiş olması gereklidir.

Bu durumda program, seçilen maliyet türüne göre her stoğun dövizli birim maliyet fiyatını bulacak, yeni yıl şirketinde döviz tutarına aktaracaktır. Döviz tipi olarak Genel Parametre Kayıtlarındaki firma döviz tipi kullanılacaktır.

#### Stok Kısıtları

Devri yapılmak istenen stoklarla ilgili kısıtlamaların yapılabileceği bölümdür. Verilecek kısıtlarla stok devrinin parça parça yapılması sağlanabilr. Ekrana yeni bir satır eklemek için klavyeden insert, seçili olan satırı silmek için de delete tuşuna basılmalıdır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/c1def746-a73a-429b-85e2-311301428c8d/ssd2026resim11.png)

#### Taslak İşlemleri

Devir işlemlerinde verilen kısıtların kaydedilmesi ve daha sonraki senelerde tekrar aynı kısıtların kullanılabilmesi için kısıtlar verildikten sonra Taslak İşlemleri menüsündan Sakla ve tekrar kullanılabilmesi için Oku adımları kullanılmaktadır.

### 1.2.3.2 Serili Devir Parametreleri

Serili Stok Devir işlemi, her işletme ve şube için ayrı ayrı çalıştırılmalıdır.

Genel Parametre Kayıtları bölümünde "Seri Uygulaması" parametresini kullanan ve stok kartlarında Giriş ve Çıkışlarda seri uygulaması işaretli olan stokların devirlerinin yapılacağı bölümdür. Sadece Girişte seri takibi işaretli olan stoklar için ise Serili Stok Devri bölümünden parametrik olarak devir yapılacaktır.

Serili stok devri yapılırken öncelikle, verilecek kısıtlar doğrultusunda stok bakiyeleri bulunur ve bakiye devirler aktarılır. Devir hareketleri ile bağlantılı seriler ilk giren ilk çıkar metoduna göre bulunur ve stok hareketleri ile ilişkilendirilir.

Aktarılan seriler, yeni yıl şirketinde, stok hareketlerinde sağ klikte bulunan "Seri Bilgisi İzleme" adımından ya da Seri Takibi Bakiye Listesinden izlenebilir.

Rapor Modülü/Stok Raporları/Seri Kayıt Listesi bölümünden hazırlanacak bir rapor ile eski yıl şirketinde bu serilerin hangi belgeden aktarıldığına dair detay bilgiler de görülebilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/e7b80d0e-eb35-4ffa-b40e-44b5597acf2a/ssd2026resim12.png)

#### Devir Baz Tarihi

Stok devri için baz alınacak tarihtir. Bu sahaya yılın son günü otomatik olarak getirilecektir. Devir baz tarihinden önceki stok hareketleri, seçilen maliyet türüne göre devredilir. Bu tarihten sonraki hareketler aynen yeni şirkete aktarılır.

#### Devir Tarihi

Yeni şirkete aktarılacak stok devirleri için, kullanılması istenen tarihin girileceği sahadır.

#### Maliyet Türü

Devir, FIFO (ilk giren ilk cıkar), LIFO (son giren ilk cıkar), Ağırlıklı ortalama, Hareketli ortalama, Aylık ağırlıklı ortalama, Alıs fiyatı ve Maliyet Muhasebesi maliyet türlerinden biriyle yapılabilmektedir.

***Dikkat!*** Maliyet Muhasebesini kullanan firmaların maliyet türü olarak Maliyet Muhasebesi Fiyatı seçmeleri gerekmektedir. Bu durumda stok devrinde stok kartlarındaki maliyet fiyatları baz alınacaktır.

#### İthalat/İhracat Hareketleri Aktarılmasın

Fatura modülünde bulunan "İhracat/ İthalat miktarları stoklara geçsin" parametresinin kullanıldığı durumlarda, bu parametre işaretlenerek devir yapıldığında kapatılmamış ithalat/ihracat kayıtları yeni sene şirketine aktarılmayacaktır.

"İhracat/ İthalat miktarları stoklara geçsin" parametresi kullanılmıyorsa bu seçenek işaretlenmeyip, sadece İhracat/ İthalat Devri işlemi çalıştırılacaktır.

#### Dinamik Depo İçin Devir Yapılsın

Dinamik depo modülü kullanan firmalarda merkez işletme ya da şubede işaretli olarak gelecek ve müdahale edilemeyecektir. Devir için verilen tarih itibarı ile hücre bakiyeleri yeni seneye devir olarak işlenecektir.

#### Devirde Hücre Kodu Dikkate Alınsın

Dinamik depo modülünün kullanıldığı durumlarda, bakiye veren seri kayıtları aktarılırken bakiye kontrolünün hem seri hem de seri kayıtlarında bulunan hücre koduna göre yapılması için kullanılan seçenektir. Bu seçeneğin işaretlenmesi halinde aktarım, Seri ve Hücre Kodu kırılımında olacaktır.

#### Devirde Seri-2 Dikkate Alınsın

Bu seçeneğin işaretlenmesi halinde, bakiye veren seri kayıtları aktarılırken bakiye kontrolü hem seri hem de seri-2' ye göre yapılacaktır. Aktarım, Seri ve Seri-2 kırılımlı olarak yapılacaktır. Seri ve seri-2' nin açıklamaları da yeni sene şirketine aktarılacaktır.

#### Eksi Bakiyeliler Devredilsin

Bakiyesi eksiye düşmüş olan stokların da yeni yıl şirketine aktarılması isteniyorsa işaretlenmesi gereken seçenektir. İşaretlenmediği durumda eksi bakiyede olan stokların devri yeni yıl şirketine aktarılmayacaktır.

#### Seri Kadar Stok Hareket Atılmasın

Bu seçeneğin işaretlenmesi halinde, bakiye veren seri kayıtları kırılım yapılmadan stok hareket kayıtlarına işlenecektir. Aktarılan seriler, yeni yıl şirketinde, stok hareketlerinde sağ klikte bulunan "Seri Bilgisi İzleme" adımından ya da Seri Takibi Bakiye Listesinden izlenebilecektir.

#### Sadece Girişte Seri Takibi Yapılan Stoklar da Devredilsin

Serili Stok Devri bölümünden stok kartlarında Giriş ve Çıkışlarda seri uygulaması işaretli olan stokların devirleri yapılmaktadır. Bu seçeneğin işaretlenmesi halinde ise, sadece girişte seri takibi işaretli olan stoklar için de serili stok devri yapılacaktır.

***Önemli***

- Stokların bir kısmının serili bir kısmının serisiz kullanıldığı durumda, Serili ve Serisiz Stok Devri işlemlerinin her ikisi de çalıştırılmalıdır. Bu durumda hangi işlemde hangi stokların devredileceği stok kartındaki seri parametrelerine göre belirlenir. Stok kartında girişlerde ve çıkışlarda seri takibi olan stoklar serili devir işlemi ile devredilecektir. Seri parametreleri işaretli olmayan veya sadece çıkışlarda seri takibi açık olan stoklar ise serisiz stok devriyle devredilecektir.
- Sadece girişlerde seri takibi açık olan stoklar ise hem serili devir ekranında hem de serisiz devir ekranından devredilebilir. Eğer serisiz devir ekranından devredilirse sadece stok hareketleri oluşacaktır, seri tablosundaki kayıtları oluşmayacaktır; serili devir ekranından ancak "Sadece Girişte seri takibi yapılan stoklarda devredilsin" parametresi işaretlenirse devredilebilecektir ve seri hareketleri de aktarılabilecektir. Bu yüzden stok devirlerinde işlem sırası olarak, önce serisiz stok devri ve ardından serili stok devrinin yapılması tavsiye edilmektedir.
- Merkezde seri takibi uygulamasının kullanılıp, şubede seri takibi uygulamasının kullanılmadığı durumda, merkezden serili stok devri, şubeden ise serisiz stok devri yapılabilir.

#### Stok ve Seri Bakiyesi Ayrı Bağlantısız Olarak Aktarılsın

Seri hareketleri ile stok hareketleri arasında bağlantının kullanılmadığı, birbirinden bağımsız olarak seri ve stok hareketlerinin takip edildiği firmalar için sorgulanan sahadır. *Hepsi* seçildiğinde girilmiş olan bütün seri hareketleri yeni yıl şirketine aktarılacaktır. *Bakiyeli* işaretlenir ise; sadece bakiye veren seri kayıtları yeni sene şirketine aktarılacaktır.

#### Taslak İşlemleri

Devir işlemlerinde verilen kısıtların kaydedilmesi ve daha sonraki senelerde tekrar aynı kısıtların kullanılabilmesi için kısıtlar verildikten sonra Taslak İşlemleri menüsünden Sakla ve tekrar kullanılabilmesi için Oku adımları kullanılmaktadır.

### 1.2.4 İthalat/İhracat Devir

İthalat/ İhracat Devir işlemi, her işletme ve şube için ayrı ayrı çalıştırılmalıdır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/1d469932-9d13-44c3-b41b-db8636ee9b4f/ssd2026resim13.png)

İthalat ve ihracat uygulaması olan firmaların, henüz kapatılmamış kayıtlarının devir şirketine aktarılması için kullanılan bölümdür.

Bu işlem ile ithalat kapatması henüz tamamlanmamış ithalat/ ihracat irsaliyeleri (miktar sahaları boş, export miktarı sahaları dolu olan hareketler) devir şirketindeki stok hareket kayıtlarına aktarılmaktadır. Ayrıca Dekont Modülü/Genel Dekont Kaydı bölümünden IT ve IH seri numarasıyla kaydedilmiş tüm dekontlar devir şirketine aktarılacaktır.

Fatura modülünde bulunan "İhracat/ İthalat miktarları stoklara geçsin" parametresi işaretli ise, tüm ithalat/ ihracat kayıtları eski senede kapatılmalıdır. Bu parametreyi kullanan firmalar, stok devirlerini yapmadan önce, gerekirse yeni senede olabilecek masraflar için de karşılık ayırarak, eski sene şirketinde bütün ithalat/ihracat kapatmalarını yapmalıdır.

#### Kapatılmış Kayıtlar Devredilmesin

Eski yılda ithalat kapatması yapılmış kayıtların İthalat/ihracat devri yapıldığında yeni yıl şirketine gelmemesi isteniyorsa işaretlenmelidir.

İthalat/İhracat devri ile dış ticaret modülündeki hareketler yeni sene şirketine aktarılmaz. Yeni yıl kopyalama işlemiyle dış ticaret modülünde oluşturulmuş olan ithalat/ ihracat dosyaları (kapalı parametresi işaretsiz olan) ve proforma fatura belgeleri yeni sene şirketine aktarılır.

#### Taslak İşlemleri

Devir işlemlerinde verilen kısıtların kaydedilmesi ve daha sonraki senelerde tekrar aynı kısıtların kullanılabilmesi için kısıtlar verildikten sonra Taslak İşlemleri menüsündan Sakla ve tekrar kullanılabilmesi için Oku adımları kullanılmaktadır.

### 1.3 Finans

### Cari Devir

Cari Devir işlemi, Netsis 3 Enterprise, Netsis Wings Enterprise ürünlerini kullanan ve birden fazla işletme tanımlanmış olan firmalarda merkez işletmenin merkez şubesinde, Netsis Wings Entegre, Netsis Wings Entegre Pro, Netsis Wings Standard, Netsis 3 Standard ürünleri ile işletme tanımlanmamış Netsis 3 Enterprise, Netsis Wings Enterprise ürünlerinde, merkez şubede çalıştırılmalıdır.

Cari hareketlerin her çeşit devri şube bazında ayrı ayrı otomatik olarak oluşturulacaktır. Bu işlemden önce, cari hesap sabit bilgilerinin yeni sene şirketine aktarılma işleminin yukarıda anlatılan Yeni Yıl Kopyalama bölümünden yapılmış olması gerekmektedir. Yeni Yıl Kopyalama işleminden sonra eski yıl şirketinde oluşturulan cari hesap sabit bilgisi var ise, bu bilgiler, yukarıda anlatılan Sabit Kayıt Kontrolü ile yeni yıl şirketine aktarılabilir. Burada, sabitlere bağlı hareketlerin devri yapılacak, sonuç devir hareketi yeni sene şirketindeki hareketlere işlenecektir.

Yeni yıla ait kayıtları yeni yıl şirketine girmeyi tercih eden firmalar, modül devirleri yapılana kadar, eski yıla ait devir bilgilerini yeni yıl şirketinde göremeyeceklerdir. Dolayısıyla bu firmalar, modül devri yapılıncaya kadar, yaşlandırmalı ödeme emri hazırlayamayacak, cari risk takibi ve özel hesap kapatma yapamayacaklardır. Bu tür uygulamaları olan firmalar, cari hesap mutabakatları yapılana kadar, yeni yıla ait kayıtları eski yıl şirketine girmek suretiyle, işlemlerini gerçekleştirebilirler. Ancak muhasebeye doğrudan aktarım özelliğinin kullanıldığı modüller için yeni yıl kayıtları, mutlaka yeni yıl şirketine girilmelidir.

![](../_assets/eedc9e68f887de96aa19.png)

Cari Devir adımı girişinde, ilk olarak yukarıdaki uyarı ekranı gelecektir. Bu uyarı, dövizli çalışma varsa devir yapılmadan öncelikle cari modülde kur farklarının kapatılma işleminin yapılması içindir. Bu işlemin gerekliliği ilerideki bölümlerde anlatılacaktır.

Bu onaylama ekranında Evet butonuna basıldığında Cari hesap devirlerinin ne şekilde gerçekleşeceğini sorgulayan ekran gelecektir.

#### Devir Tipi

Cari devirlerinizi yapmadan önce hangi tip devir yapacağınıza karar vermelisiniz. Seçilebilecek devir tipleri şöyledir;

1. BAKİYELİ DEVİR

1.1- SON BAKİYE

1.2- TARİH ARALIKLI

1. CARİ HESAP TİPİNE GÖRE (YAŞLANDIRMALI DEVİR)

#### Bakiyeli Devir

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/ad8f8bf1-832f-4ff2-ae86-edde34768dad/ssd2026resim14.png)

**Devir** **Baz** **Tarihi**

Tarih aralıklı devir seçeneği için, en son hangi tarihe kadar olan hareketlerin devrinin yapılacağını belirleyeceğiniz sınır tarihi sorusudur. (Cari hareket kayıt tarihleri baz alınır) Bu tarihten sonraki kayıtlar aynen aktarılır.

#### Devir Tarihi

Devir tarihi, devir hareketlerinin yeni sene şirketine işleneceği kayıt tarihidir. Büyük çoğunlukla yeni yılın ilk iş günü girilir.

#### Sabit Kayıt Kontrolü Yapılsın

Bu seçenek işaretlendiğinde eski sene şirketinde olup yeni sene şirketinde olmayan cari kayıtları devir öncesinde yeni sene şirketinde tanımlanacaktır. Sabit Kayıt Kontrolü işlemi ayrıca ortak işletmeden daha detaylı olarak da yapılabilmektedir.

#### Proje Kırılımlı Devir

Genel Parametre Kayıtları bölümünde "Proje Uygulaması Var" parametresinin kullanıldığı durumda bu seçenek işaretli olarak devir yapıldığında, yeni sene şirketine proje kodu kırılımlı olarak devir hareketleri işlenecektir. Proje Kodu Kırılımlı devir parametresi işaretli olmadığında, yanındaki rehber alanı aktif hale gelecek, aktarılan devir hareketine bu rehberden seçilen proje kodu işlenecektir.

#### Bakiyeli Devir Parametreleri Bakiyeli Devir Tipi

*Tarih* *Aralıklı*

Tarih aralıklı devir seçeneği, devir yapılacak tarihten sonrasına kaydedilmiş hareketler varsa işaretlenmelidir. Yeni sene şirketinde örneğin eski senenin 12. aya kadar devir bilgisi ve 1. ayın bilgilerini olduğu gibi görebilmek için kullanılır.

*Son* *Bakiye*

Bu seçenek ile, cari hesabın son borç/ alacak bakiyesi, tek devir hareketi olarak yeni sene şirketine işlenir. Proje kodu ve/veya döviz kullanımı varsa, proje/döviz kırılımında bakiyeler ayrı ayrı işlenir. Eğer eski sene şirketinde hiç yeni sene kaydı girilmemiş ise ve cari kayıtlarında özel hesap kapatma kullanılmamışsa, hız açısından tavsiye edilen devir yöntemidir. Eski yıl şirketine yeni yıl kaydı girilmesi halinde ise, yeni yıla ait kayıtlar olduğu gibi yeni sene şirketine aktarılacaktır.

#### Devir Kayıtlarında Ortalama Vade Tarihi Hesaplansın

Geçmiş yıl şirketindeki cari hareketlerinin, devir tarihine göre ortalama vade gününün bulunmasını sağlayan seçenektir. Bulunan gün değeri devir tarihine eklenerek, devredilen hareketlerin vade tarihi sahasına yazılmaktadır.

Cari hesaplarda Puan uygulamasının kullanıldığı durumda, puan bakiyelerinin de cari hareketlere taşınması sağlanmıştır. Sadece Bakiyeli Devir seçeneği için desteklenmektedir.

#### Plasiyerlere Göre Kırılım

Plasiyer uygulaması olan firmalarda, bu seçenek işaretlenir ise, devir olarak aktarılan cari hareketler için plasiyer koduna göre kırılım yapılacaktır. Kullanılmamışsa, hız açısından tavsiye edilen devir yöntemidir.

#### Bakiyesi 0 Olan Carinin Puan Bilgisi Aktarılsın

Carinin bakiyesi olmasa bile kalan puanı var ise puanın aktarılmasını sağlar.

#### Taslak İşlemleri

Devir işlemlerinde verilen kısıtların kaydedilmesi ve daha sonraki senelerde tekrar aynı kısıtların kullanılabilmesi için kısıtlar verildikten sonra Taslak İşlemleri menüsündan Sakla ve tekrar kullanılabilmesi için Oku adımları kullanılmaktadır.

#### Cari Hesap Tipine Göre Devir Devir Baz Tarihi

Yaşlandırmalı devir için, en son hangi tarihe kadar olan hareketlerin devrinin yapılacağının gösterildiği sınır tarihi sahasıdır. (Cari hareket kayıt tarihleri baz alınır) Bu tarihten sonraki kayıtlar aynen aktarılır. Bu devir seçeneği, cari sabit kayıtlarında, her cari için ayrı ayrı belirlenebilen Cari Hesap Tipine (Yaşlandırma / Özel Hesap Kapatma) göre Borç/Alacak yaşlandırması yapılarak, kalan açık hareketler yeni yıla ayrı ayrı devir kaydı olarak devredilecektir.

***Not:*** Bu seçeneğe göre yaşlandırma, borçlu çalışan cari hesaplarda, borç hareketlerini alacak hareketleriyle, alacaklı çalışan cari hesaplarda alacak hareketlerini borç hareketleriyle otomatik kapatacak, açıkta kalan (ödenmemiş) hareketleri devir olarak yeni seneye işleyecektir.

***Not:*** Özel hesap kapatma ile çalışan firmalar, cari devirden önce, Cari Modül/ Ek Listeler/ Denetim Listeleri/ Özel Hesap Kapatma Denetimi listesinden, eksik kapatmaları ve yapılan kapatmaların doğruluğunu kontrol etmelidir.

Plasiyer Uygulamasının kullanıldığı durumda, yaşlandırma sonucunda bulunan ve yeni yıl şirketine aktarılan hareketlere plasiyer kodları da taşınmaktadır.

***Önemli;*** plasiyer bazında yaşlandırma yapılmamaktadır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/35aed770-3673-40c2-98b9-e000b958e466/ssd2026resim15.png)

#### Cari Hesap Tipine Göre Devir Parametreleri

**Eski** **kayıtlara** **devir** **tarihi** **atılsın**

Bu seçeneğin işaretlenmesi halinde, eski sene şirketindeki cari hareketlerden kapanmamış olanları yeni sene şirketine aktarırken, kayıt tarihi sahasına işlem sırasında belirlenen devir tarihi yazılacaktır. Bu şekilde yapılan devirde kayıt tarihleri düzenlenecek, vade tarihlerinde değişiklik yapılmayacaktır. Bu seçenek işaretlenmeden devir yapılması halinde ise, kayıt tarihleri olduğu gibi aktarılacaktır.

#### Devir Döviz Tarihi

Dövizli devir yapıldığı durumda ve yaşlandırma kur türü bölümünde anlatılacak olan "Devir Döviz Tarihi Kuru" seçildiğinde, bu sahada girilen tarih baz alınarak işlem yapılacaktır.

#### Yaşlandırma Parametreleri

**Yaşlandırma** **Tarihi**

Cari hesap tipine göre (Yaşlandırmalı) devir seçeneği için yaşlandırmanın kayıt ya da vade tarihine göre yapılacağının seçileceği bölümdür. Yaşlandırma sırasında otomatik yapılacak olan borç/alacak kapatmalarının hareketlerin hangi tarih sırasında yapılacağıdır.

#### Dövizli Yaşlandırma

Bu seçenek, cari hesaplarda döviz kullanımı varsa, yani "Dövizli" seçeneği işaretlenmiş cari kartlar için geçerlidir.

![](../_assets/a26738a26d15d59e2c9c.png)

#### Yapılmasın

Dövizli yaşlandırma yapılması istenmiyorsa seçilmelidir. Bu durumda dövizli cariler için yaşlandırma yapılmaz, döviz tipi bazında bakiyeli devir yapılır.

#### Firma Döviz Tipine Göre

Yardımcı Programlar/Şirket Şube Parametre Tanımlamaları bölümünde Düzeltme Tipi sahasında seçilen döviz tipine göre yaşlandırma yapılması için kullanılan seçenektir. Öncelikle Cari Modülü / İşlemler / Döviz tutarlarını oluşturma işleminin çalışmış ve cari hareketlerde Firma Döviz tutarlarının oluşmuş olması gerekir. Yaşlandırma sadece firma döviz tipinde ve bulunan döviz tutarlarına göre yapılır. Yeni yıl şirketinde aktarılan cari hareketlerde, firma dövizi cinsinden bulunan döviz bakiyeleri "Döviz Tutarı" sahasına, "Yaşlandırma Kur turu" bölümünde anlatılacak olan kur bilgisine göre hesaplanan TL değerleri ise borç/alacak sahalarına aktarılır. (Özel Hesap Kapatmalı cari hesaplar için firma dövizine göre işlem yapılmaz).

Yeni yıl şirketine firma dövizine göre devir yapılmadan önce, eski yıl şirketinde Cari Modülü

/ Raporlar / Ek Listeler / Tarih Aralıklı Yaşlandırma Listesinden gerekli kısıtlamalar yapılarak ve "Firma Döviz Tipine Göre Dökülsün" seçeneği işaretlenerek, oluşacak hareketler kontrol edilebilir.

#### Cari Hareket Döviz Tiplerine Göre

Dövizli cari hesaplar için, hareket girişi esnasında girilmiş olan operasyon dövizlerine göre yaşlandırmalı devir yapılması isteniyorsa bu seçenek işaretlenmelidir. Bu durumda her bir döviz tipi, kendi içinde yaşlandırma yapılacak ve yeni yıl şirketinde devir hareketleri bu kırılımda oluşacaktır. Cari kartında Özel hesap kapatma işaretli olan dövizli cariler için, açıkta kalan döviz hareketleri aktarılacaktır.

Yeni yıl şirketinde oluşacak hareketler, eski yıl şirketinden Cari Modülü / Raporlar / Ek Listeler / Tarih Aralıklı Yaşlandırma Listesinden gerekli kısıtlamalar yapılarak ve "Döviz Tipine Göre Kırılım" seçeneği işaretlenerek kontrol edilebilir.

Yurtiçi Dövizli cariler için de yaşlandırmalı devir desteği getirilmiştir. Eğer cari kartında Yurtiçi Döviz tipi seçilmiş ise ve Dövizli yaşlandırma bölümünde "Cari Hareket Döviz Tiplerine Göre" seçeneği işaretlenmişse, yurtiçi döviz tipine göre yaşlandırmalı devir yapılmaktadır. Firma Döviz Tipine göre seçeneği Yurtiçi Dövizli cariler için kullanılamamaktadır.

#### Yaşlandırma Kur Türü

Firma ya da Cari Hareket Döviz Tipine göre devir seçildiğinde yaşlandırma sonucunda bulunan döviz bakiyelerinin, TL tutarlarının hangi kur bilgisi ile oluşacağının seçildiği bölümdür.

Hareket Kuru: Yaşlandırma sonucunda bulunan hareketlerin, hareketin girildiği tarihteki kur ile yeni yıl şirketine aktarılması istendiği durumda işaretlenmesi gereken seçenektir.

Devir Döviz Tarihi Kuru: Yaşlandırma sonucunda bulunan hareketlerin, Devir Döviz Tarihi sahasında yazılan tarihteki kur bilgisi ile aktarılması istendiği durumda işaretlenmesi gereken seçenektir. Eğer geçmiş yıl şirketinde, yılsonunda kur farkı hesaplama çalıştırılmış ise "Devir Döviz Tarihi Kuru" seçilerek işlem yapılmalıdır.

#### Proje Bazında Yaşlandırma Yapılsın

Bu seçenek, proje uygulaması kullanılıyor ise aktif olarak ekranda görülecektir. Proje kodu bazında yaşlandırma yaparak devirlerin oluşması isteniyorsa işaretlenmelidir. Proje bazında yaşlandırma işaretli olmadığı durumda, yaşlandırma sırasında proje kodları dikkate alınmayacaktır. Fakat yaşlandırma sonucunda bulunan kalan rakamlara, hangi hareketten kaldıysa o hareketin proje kodu yazılacaktır.

#### Cari Alt Kodlarıyla Beraber

Cari Bağlantı kayıtları kullanıldığı durumda, ilgili cari hesabın Cari Alt Kodlarına ait hareket kayıtları için de Borç/Alacak yaşlandırması yapılarak, kalan açık hareketlerin yeni yıla ana cari hesaba devir kaydı olarak devredilmesi için bu seçenek işaretlenmelidir. Alt cari hesaplar, hareketsiz olarak devredilecektir.

#### Özel Hesap Kapatmalı Carilerde Kur Farkı Atmasın

Eski sene şirketinde kur farkı çalıştırılmış olmasına rağmen program yeni sene şirketinde tekrar kur farkı çalıştırıyordu. Bunu istemeyen firmalar için bu parametre kullanılabilir. Bu şekilde devir döviz tarihindeki kura göre hareketlerin TL rakamlarını bulup kur farkı kayıtlarını oluşturmamaktadır.

#### Kapatılmamış Hareketlerin Kalan Tutarları Aktarılsın

Bu seçenek işaretli olduğunda eski yıl şirketinde özel hesap kapatması yapılmamış ve açıkta kalan hareketler yeni yıl şirketine aktarılırken eski yıl şirketindeki (tutar-kapatılmış tutar) değeri ile aktarılacaktır.

#### Taslak İşlemleri

Devir işlemlerinde verilen kısıtların kaydedilmesi ve daha sonraki senelerde tekrar aynı kısıtların kullanılabilmesi için kısıtlar verildikten sonra Taslak İşlemleri menüsündan Sakla ve tekrar kullanılabilmesi için Oku adımları kullanılmaktadır.

Cari Hesap Tipine Göre Devir, bir özel parametre tanımlaması ile her şube için ayrı ayrı yapılabilir. Bunun için Yardımcı Programlar/Özel Parametre Tanımları menüsünde tanımlama yapılması gerekmektedir.

![](../_assets/47befb3c19b0e7fd8f3c.png)

Bu özel parametre tanımlı olduğunda, cari devir, her işletme ve şube için ayrı ayrı yapılacaktır.

#### Cari Kısıtları

Devri yapılmak istenen cari hesaplarla ilgili kısıtlamaların yapılabileceği bölümdür. Ekranda, cari sabit kayıtlarında girilen bilgiler listelenmektedir. Carilerin bölüm bölüm devrinin yapılabilmesi için kullanılır. Ekrana yeni bir satır eklemek için klavyeden insert, seçili olan satırı silmek içinde delete tuşuna basılmalıdır. Cari Devri'nde oluşacak kayıtları birkaç örnek ile açıklayalım.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/ff01e6ce-5288-4971-ac3c-f975c37dc883/ssd2026resim16.png)

#### Örnekler;

(Aşağıdaki örneklerde, cari hesap tipine göre devir tipi belirlenmiş olduğu kabul edilmiştir.)

**1-Cari** **Hesap** **Tipi** = **Yaşlandırma, Cari Hesap Dövizli,**

**Döviz** **Tipi** = **0,**

**Dövizli** **Yaşlandırma** **seçeneğinde** **"Yapılmasın"** **işaretli**

Döviz Yaşlandırma seçilmediğinden döviz kırılımlı tarih aralıklı bakiye devri yapılır.

Döviz tipi bazında ve kullanılıyorsa proje kodu bazında borç/alacak bakiyeleri bulunur, her bir kırılım için ayrı bir devir hareketi yeni senede oluşturulur.

TL dışındaki döviz tipleri için oluşturulan satırlardaki TL değerler, döviz bakiyesine ve verilen kur tarihine göre yeniden hesaplanır.

**2-Cari** **Hesap** **Tipi** = **Yaşlandırma, Cari Hesap Dövizli,**

**Döviz** **Tipi** = **0,**

**Dövizli** **Yaşlandırma** **bölümünde** **"Cari** **Hareket** **Döviz** **Tiplerine** **Göre"** **seçeneği işaretlenmiş;**

Döviz tipine göre yaşlandırma yapılarak her döviz tipi için açıkta kalan hareketler, kendi döviz tipleriyle yeni senede oluşturulur.

Proje kodu kullanımı varsa, her bir devir satırının eski senedeki kendi proje kodu yeni senedeki devir hareketine taşınır. TL dışındaki döviz tipleri için oluşturulan satırlardaki TL değerler, döviz bakiyesine ve verilen kur tarihine göre yeniden hesaplanır. Yaşlandırma işleminde, yaşlandırma sahasında belirtilen kayıt/vade tarihi seçeneği geçerlidir.

**3-Cari** **Hesap** **Tipi** = **Yaşlandırma, Cari Hesap Dövizli,**

**Döviz** **Tipi** = **0** **(sıfır)'dan** **farklı;**

**Dövizli** **Yaşlandırma** **seçeneğinde** **"Yapılmasın"** **işaretli;**

Döviz Yaşlandırma seçilmediğinden cari karttaki döviz tipi için tarih aralıklı bakiye devri yapılır. Cari karttaki döviz tipi için ve kullanılıyorsa proje kodu bazında borç/alacak bakiyeleri bulunur, her bir kırılım için ayrı bir devir hareketi yeni senede oluşturulur.

Sene içinde, cari karttaki döviz tipi değiştirilmiş ve birden fazla farklı döviz tipine ait hareket mevcutsa, **sadece cari karttaki döviz cinsinden kayıtlı hareketler dikkate alınacaktır.** Oluşturulan satırlardaki TL değerler, döviz bakiyesine ve verilen kur tarihine göre yeniden hesaplanır.

**4-Cari** **Hesap** **Tipi** = **Yaşlandırma, Cari Hesap Dövizli,**

**Döviz** **Tipi** = **0** **(sıfır)'dan** **farklı,**

**Dövizli** **Yaşlandırma** **bölümünde** **"Cari** **Hareket** **Döviz** **Tiplerine** **Göre"** **seçeneği işaretlenmiş;**

Cari karttaki döviz tipine göre yaşlandırma yapılarak açıkta kalan hareketler, ilgili döviz tipiyle yeni senede oluşturulur.Proje kodu kullanımı varsa, her bir devir satırının eski senedeki kendi proje kodu yeni senedeki devir hareketine taşınır. Sene içinde, cari karttaki döviz tipi değiştirilmiş ve birden fazla farklı döviz tipine ait hareket mevcutsa, **sadece** **cari karttaki** **döviz** **cinsinden** **kayıtlı** **hareketler** **dikkate** **alınacaktır.** Oluşturulan satırlardaki TL değerler, döviz bakiyesine ve verilen kur tarihine göre yeniden hesaplanır. Yaşlandırma işleminde, yaşlandırma sahasında belirtilen kayıt/vade tarihi seçeneği geçerlidir.

**5-Cari Hesap Tipi= Yaşlandırma, Cari Hesap Dövizli,**

**Dövizli** **Yaşlandırma** **bölümünde** **"Firma** **Döviz** **Tipine** **Göre"** **seçeneği işaretlenmiş;**

Cari hareketler için firma dövizine göre yaşlandırma yapılarak açıkta kalan hareketler, firma döviz tipiyle yeni senede oluşturulur. Proje kodu kullanımı varsa, yaşlandırma sonucunda bulunan her bir devir satırının eski senedeki kendi proje kodu yeni senedeki devir hareketine taşınır. Oluşturulan satırlardaki TL değerler, döviz bakiyesine ve seçilen kur türüne göre, Kayıt Tarihi ise hareket tarihindeki kurdan, Devir Döviz tarihi ise Devir Döviz Tarihindeki kurdan hesaplanır.

**6-Cari Hesap Tipi = Özel Hesap Kapatma, Cari Hesap Dövizli,**

Döviz bazında kapatılmış tutarların farkları, her bir döviz tipi için ayrı ayrı, yeni senede oluşturulur. TL dışındaki döviz tipleri için oluşturulan satırlardaki TL değerler, hareket tarihindeki kur ile bakiye döviz tutarı çarpımı olarak hesaplanıp oluşturulur. TL dışındaki her bir döviz tipinin, devir tarihindeki kur üzerinden TL bakiyesi ile önceki maddede hesaplanan TL bakiyesi arasındaki fark, ayrı bir kur farkı kaydı olarak TL değeri hesaplanarak yeni senede oluşturulur. TL dışındaki bu döviz tipleri için eski senede kaydedilmiş kur farkı hareketleri dikkate alınmaz.

Özel Hesap Kapatmalı carilerde, dövizli yaşlandırma seçeneğinin işaretlenmiş olup olmaması, cari kartta döviz tipinin sıfır ya da sıfırdan farklı olması, yaşlandırma işleminin kayıt/vade sırasında yapılıyor olması etkilemez. Devir yukarıda anlatıldığı sekliyle yapılır. Ayrıca, Firma Döviz Tipine Göre devir yapılamaz.

### 1.3.2 Senet/Çek Devir

Senet/ Çek Devir işlemi her işletme ve şube için ayrı ayrı çalıştırılmalıdır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/209f8979-0938-42d5-827a-8ac4e5b4b729/ssd2026resim17.png)

Müşteri Çekleri/Senetleri ile Borç Çekleri/Senetlerini devredebileceğiniz bölümdür.

#### Modül

Devri yapılacak senet/çek modüllerinin listelendiği sahadır. Bu sahadaki modülleri sırasıyla seçerek senet/çek devri tamamlanır. Devir işlemi çalıştırılmadan önce Çek/Senet Modülü/İşlemler/Toplu Ödeme Bildirimi bölümünün çalıştırılmış olmasına dikkat edilmelidir. Senet ya da çekin ödeme tarihi, devir baz tarihinden büyükse yeni yıl şirketine aynen aktarılmaktadır.

#### Devir Baz Tarihi

Vade tarihleri devir baz tarihinden büyük olan çek ve senetlerin tamamı yeni sene şirketine işlenecektir. Ancak vade tarihleri devir baz tarihinden büyük olan çek ve senetlerin durumu ödenmiş ise yeni yıl şirketine aktarılmayacaktır.

-Vade tarihleri devir baz tarihinden önceki tarihli çek ve senetler yeni sene şirketine aktarılmayacaktır.

#### Bekleyenleri Aktar

Vade tarihleri devir baz tarihinden önce ve durumu Beklemede olan senet/çeklerin de yeni sene şirketine aktarılması için işaretlenmesi gereken sahadır. Senet çeklerin Beklemede olanlarının takiplerine yeni sene şirketinde devam etmek için bu sahayı kullanabilirsiniz. Bu saha işaretlenmediğinde senedin/ çekin durumuna bakılmaksızın baz tarihinden önceki senetler/ çekler yeni sene şirketine aktarılmayacaktır.

Bu bölümdeki önemli nokta, yeni yıl için oluşturulan şirkette çek/ senet ve alındı/ verildi numaralarının, eski sene bilgilerinin kaldığı son numaradan takip edilerek kullanılmaya devam edilmesi gerektiğinin unutulmamasıdır.

#### Daha Önce Devredilenler Silinsin

Senet/Çek devri yapıldıktan sonra, bir hata yapıldığı tespit edilirse, devir işlemi tekrar çalıştırılabilir. Daha önce devredilenler silinsin parametresi işaretli ise önceden devredilen kayıtlar silinecek, çek ve senet devri yeniden yapılacaktır. Bu parametrenin işaretlenmediği durumda, sadece devirden sonra yeni girilmiş olan kayıtlar yeni sene şirketine aktarılacaktır.

#### Taslak İşlemleri

Devir işlemlerinde verilen kısıtların kaydedilmesi ve daha sonraki senelerde tekrar aynı kısıtların kullanılabilmesi için kısıtlar verildikten sonra Taslak İşlemleri menüsünden Sakla ve tekrar kullanılabilmesi için Oku adımları kullanılmaktadır.

Yeni sene şirketinde oluşacak çek veya senetlerin yeni numaralarının başına yıl kodu atama işlemi yeni yıl kopyalama sonucunda program tarafından gerçekleştirilmektedir.

### 1.3.3 Bağlantı Devir

Bağlantı Devir işlemi, Netsis 3 Enterprise, Netsis Wings Enterprise ürünlerini kullanan ve birden fazla işletme tanımlanmış olan firmalarda merkez işletmenin merkez şubesinde, Netsis Wings Entegre, Netsis Wings Entegre Pro, Netsis 3 Standard, Netsis Wings Standard ürünleri ile işletme tanımlanmamış Netsis 3 Enterprise, Netsis Wings Enterprise ürünlerinde, merkez şubede çalıştırılmalıdır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/1284ecac-2b70-413c-a9db-1a517862515c/ssd2026resim18.png)

Bağlantı takibi yapan firmalarda, bağlantı kayıtlarının ve devir şirketine kopyalanması için kullanılan devir seçeneğidir.

#### Taslak İşlemleri

Devir işlemlerinde verilen kısıtların kaydedilmesi ve daha sonraki senelerde tekrar aynı kısıtların kullanılabilmesi için kısıtlar verildikten sonra Taslak İşlemleri menüsündan Sakla ve tekrar kullanılabilmesi için Oku adımları kullanılmaktadır.

### 1.3.4 Banka Devir

Banka modülü devri, Netsis 3 Enterprise, Netsis Wings Enterprise ürünlerini kullanan ve birden fazla işletme tanımlanmış olan firmalarda merkez işletmenin merkez şubesinde, Netsis Wings Entegre, Netsis Wings Entegre Pro, Netsis 3 Standard, Netsis Wings Standard ürünleri ile işletme tanımlanmamış Netsis 3 Enterprise, Netsis Wings Enterprise ürünlerinde, merkez şubede çalıştırılmalıdır.

Bu işlemden önce Banka hesap sabit bilgilerinin yeni sene şirketine yukarıda anlatılan Yeni Yıl Kopyalama bölümünden aktarılmış olması gerekmektedir. Burada sabitlere bağlı hareketlerin devri yapılacak, sonuç devir hareketi yeni sene şirketindeki hareketlere işlenecektir.

Devir işlemine başlamadan önce;

- Tüm banka hesapları için döviz farkları kapatma işleminin,
- Vadesiz ve Rotatif hesaplar için faiz kapatma işleminin ve fon takibi yapılıyorsa devir öncesi Fon Kar-Zarar Hesaplama işlemlerinin çalıştırılmış olması gerekir. Program bunu bir ekranla uyaracaktır.

![](../_assets/1263a60b31332ae4784b.png)

Eğer Banka/ İşlemler bölümünde bulunan Döviz Farklarını Kapatma ve Faiz Kapatma işlemleri çalıştırıldıysa bu sorgulama "Evet", henüz çalıştırılmadıysa, programın kesilerek devir işleminden çıkılması için "Hayır" olarak yanıtlanmalıdır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/eb764169-a439-41af-92f3-be1193ad9f81/ssd2026resim19.png)

Banka hesapları devrinde, Vadeli, Spot, Taksitli Kredi, Uzun/Orta Vadeli Kredi ve Repo hesap hareketleri için, hesabın bakiye verip vermediğine bakılmaktadır. Eğer hesabın bakiyesi varsa, son hesap açma işleminde girilen tutar, devir baz tarihine bakılmaksızın yeni sene şirketine devredilmektedir.

Rotatif, Vadesiz ve Kredi Kartı hesaplarının devirleri vade tarihine göre yapılmaktadır. Vade tarihi, devir tarihinden büyük olan kayıtlar yeni yıl şirketine aynen aktarılmaktadır. Bunun dışındaki tüm hesap hareketleri, Cari Tarih Aralıklı Devir mantığına göre yeni sene şirketine aktarılacaktır. Yani, belirlediğiniz Devir Baz Tarihine kadar olan hareketlerin sadece bakiyesi devredilecek, bu tarihten sonraki hareketler aynen yeni sene şirketine aktarılacaktır.

Şirket/ Şube Parametre Tanımlamalarında "Proje Uygulaması" işaretlenmiş ise hareketler proje kodu kırılımlı olarak yapılacaktır.

#### Devir Baz Tarihi

Cari Tarih Aralıklı Devir mantığına göre devredilecek banka hesapları için, en son hangi tarihe kadar olan hareketlerin devrinin yapılacağını belirleyeceğiniz sınır tarihi sorusudur.

#### Devir Tarihi

Devir hareketlerinin yeni sene şirketine işleneceği kayıt tarihidir. Büyük çoğunlukla yeni yılın ilk günü girilir.

#### Döviz Tarihi

Banka hareketlerinde dövizli kayıt bulunan firmaların sene sonu devirlerinde kullanılacak

olan kur tarihidir.

***Not:*** Dövizli banka hesapları devredilirken, program döviz tiplerine göre ayrı ayrı devir alacak ve döviz bazında bakiyeleri ayrı ayrı yeni sene devri olarak oluşturacaktır. Döviz bazında yapılan bu devir hareketlerinin TL tutarları ise, her döviz tipi için burada girilen tarihteki kurdan yeniden hesaplanacaktır. Eğer eski sene şirketinde, devir yapılan tarih itibariyle kur farkı kapatma işlemi yapılmadıysa, bu yeniden hesaplama sonucu, bakiyeler, eski sene şirketiyle yeni sene şirketi arasında fark verebilir. Bu nedenle devir programı, banka devir seçeneğine giriş sırasında kur farkı kapatma yapılması gerektiğine dair uyarı verir.

#### Banka Hes. Kod Aralığı

Belirli bir aralıktaki banka hesaplarına ait hareketlerin yeni yıl şirketine aktarılması için kullanılan sahadır. Sadece devredilmesini istediğiniz banka hesap kodları için kısıt verebilirsiniz. Buraya girilen banka hesap kodları için daha önce devir yapılmışsa, bu banka hesapları için daha önceki devirde oluşturulan hareketler silinecek ve tekrar oluşturulacaktır.

#### Proje Kırılımlı Devir

Genel Parametre Kayıtları bölümünde "Proje Uygulaması Var" parametresinin kullanıldığı durumda bu seçenek işaretli olarak devir yapıldığında, bulunan bakiyeler yeni sene şirketine proje kodu kırılımlı olarak işlenecektir. Proje Kodu Kırılımlı devir parametresi işaretli olmadığında, yanındaki rehber alanı aktif hale gelecek, aktarılan devir hareketine bu rehberden seçilen proje kodu işlenecektir.

#### Eski Kayıtlara Devir Tarihi Atılsın

Banka devri yapılırken eski kayıtlara devir tarihinin atılması için kullanılan seçenektir.

#### Devir Sonunda Kur Farkı Kapatma Yapılsın

Banka devri sonrasında kur farkı kapatmalarının yapılması için kullanılan seçenektir.

#### Firma Kredi Kartlarında Ödenmeyen Kayıtlar Aktarılsın

Firma Kredi Kartı uygulamasında vade tarihi eski yıla ait ödenmemiş kayıtların yeni sene şirketine devir olarak atılması sağlanmaktadır.

#### Taslak İşlemleri

Devir işlemlerinde verilen kısıtların kaydedilmesi ve daha sonraki senelerde tekrar aynı kısıtların kullanılabilmesi için kısıtlar verildikten sonra Taslak İşlemleri menüsündan Sakla ve tekrar kullanılabilmesi için Oku adımları kullanılmaktadır.

Yeni sene şirketinde oluşacak yeni numaralarının başına yıl kodu atama işlemi program tarafından gerçekleştirilmektedir.

### 1.3.5 Poliçe Devir

Poliçe devri kapsamında Sene Sonu Devir Finans bölümü altına Poliçe Devri isminde yeni bir ekran eklenmiştir. Poliçe Devri ekranı 3 sekmeden oluşmaktadır. İlk sekmede Poliçe Devri yapılacağına dair kullanıcıya bir bilgilendirme mesajı gelmektedir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/d704c144-29ef-440c-a90b-5eafa4995bed/ssd2026resim20.png)

İşlem sekmesinde ise bu poliçe devrinin hangi şirkete yapılacağı program tarafından getirilir.

**Devir Baz Tarihi** kısmında, Poliçe Devri’ nin hangi baz tarihine göre yapılacağı girilir.

Poliçe Devri sonucu İşlem Sonucu sekmesinde izlenebilmektedir. Alınan herhangi bir uyarı varsa işlem sonucu ekranında görüntülenmektedir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/83b80b93-4c6c-4b97-8885-55373bcca720/ssd2026resim21.png)

Tahakkuk/Ödeme Kaydı Tamamlanmamış ve Bitiş Tarihi Geçen Devir Baz Tarihinden Önceki Poliçeler Aktarılsın Parametresi

Bu parametre işaretlenmeden Poliçe Devri gerçekleştirildiğinde program devir baz tarihine göre bu tarihten daha büyük bitiş tarihine sahip olan poliçe kayıtlarını yeni sene şirketine aktarmaktadır. Eski sene şirketinde ödemesi ve tahakkuk işlemi tamamlanmamış ancak bitiş tarihi devir baz tarihinden küçük kayıtlar varsa ve yeni sene şirketine aktarılması isteniyorsa ilgili parametrenin işaretlenmesi gerekmektedir.

Poliçe Kısıtları bölümünde, kullanıcı istediği kısıtları verebilir. Poliçe Devri burada verilen kısıtlara göre yapılacaktır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/11d4c758-864e-4735-96ea-617948537bdd/ssd2026resim22.png)

## 1.4 Muhasebe Devir

### 1.4.1 Muhasebe Kapanış Fişi

Muhasebe Kapanış Fişi, her işletme ve şube için ayrı ayrı oluşturulmalıdır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/c62ef9ea-aa21-4de3-90cc-863d7ce19448/ssd2026resim23.png)

Eski sene muhasebe kayıtları tamamlandığında, muhasebe bölümünün devri iki aşamalı olarak yapılır. Bunlardan ilki dönem sonu kapanış fişidir. Muhasebe fiş kayıtlarının bittiğinden, mizanların tuttuğundan emin olmadan bu işlemi çalıştırmayınız. Aksi halde yapacağınız herhangi bir düzenlemeyi kapanış ve açılış fişlerinde elle yapılmalıdır.

Yeni yıl kopyalama ile yeni sene şirketi açılmadan, muhasebe kapanış fişi oluşturulabilmektedir.

#### Kapanış Tarihi

İçinde bulunduğunuz şirket için otomatik oluşturulacak kapanış fişi için verilecek tarihtir. Verilen tarihe, yılın son ayının son fiş numarasının bir sonrasına, kapanış fişini otomatikman oluşturacaktır.

#### Proje Kodu Bazında Devir

Proje Kodu uygulaması olan firmalarda bu seçenek işaretlenir ise kapanış fişi proje kodu kırılımı ile yapılacaktır. Yani her bir muavin hesap kapanışı, proje kodu bazında bakiyeleri dikkate alınarak yapılacaktır.

#### Dövizli Devir

Muhasebe kayıtlarını döviz bazında takip eden firmaların, kapanış fişinin döviz değerleri ile oluşması için kullanacağı seçenektir. IAS29, FAS52 seçeneklerinden biriyle çalışan firmalar bu seçeneği işaretlemeyip bir sonraki seçeneği işaretlemelidir.

İşlem sırasında, kapanış fişi, döviz tipi kırılımı ile oluşturulmakta ve kayıtlara, her bir döviz tipine göre hesaplanan döviz tutarları ve varsa firma döviz tutarları aktarılmaktadır.

#### IAS29 / FAS52/ Enf.Muh.

Bu seçenekle kapanış fişini oluşturacak firmaların, Muhasebe/ Parametre Kayıtları bölümünde IAS29, FAS52 veya Enf.Muh seçeneklerinden birinin mutlaka işaretlenmiş olması gereklidir.

Bu seçenek ile kapanış fişi oluşturulmadan önce, devir öncesi son dönem için enflasyon muhasebesi işlemleri mutlaka çalıştırılmalıdır. IAS29 ya da FAS52 için kapanış fişi ile firma döviz tutarlarının hesap kodu bazında bakiyeleri, TL' si sıfır (0), firma döviz tipi ve tutarı dolu olan kayıtlar oluşturulur.

IAS29' a göre muhasebe yapılması halinde ve muavin hesabın kapanış fişine atılacak TL ve Firma Döviz tutarları ayrı yönde ise (TL bakiyesi borç, Firma Döviz bakiyesi alacak ya da tam tersi), kapanış fişinde TL için ayrı Firma Dövizi için ayrı satırlar oluşturulur.

#### Referans Kodu Bazında Devir

Referans Kodu uygulaması olan firmalarda bu seçenek işaretlenir ise kapanış fişi referans kodu kırılımı ile yapılacaktır. Yani her bir muavin hesap kapanışı, referans kodu bazında bakiyeleri dikkate alınarak yapılacaktır.

#### 0 Tutar Kontrolünde Firma Döviz Tutarı Dikkate Alınsın

Kapanış fişi oluşturulurken tutar = 0, döviz tutarı = 0 ve firma döviz tutarı ǂ 0 değerinden farklı olan hesap kodlarının fişe eklenmesi için kullanılan seçenektir. Hesabın bakiyesi yok (0 tutarlı) ve kapanış fişinde de 0 tutarlı olarak görünüyorken, döviz uygulaması kullanılıyor ve o hesabın firma döviz tutarı varsa bu parametrenin işaretlenerek fiş oluşturulması daha kontrollü devir yapmaya yarar. Bu kondisyona uyan hesap kodlarının fişe eklenmesi için kullanılan seçenektir.

#### Şubeler İçin Kapanış Fişi Oluşturulabilsin

9.0.25 setiyle birlikte şubeli muhasebe kullanan firmalarda kapanış fişinin merkezden şubeler adına oluşturulması desteklenmiştir. Parametrenin işaretlenmesi halinde şube seçim ekranı aktif olacaktır.

#### Hesap Planı Kısıtları

Devri yapılmak istenen hesap planı ile ilgili kısıtlamaların yapılabileceği bölümdür. Ekranda, muhasebe hesap planı kayıtlarında girilen bilgiler listelenmektedir. Hesap planının bölüm bölüm devrinin yapılabilmesi için kullanılır. Ekrana yeni bir satır eklemek için klavyeden insert, seçili olan satırı silmek içinde delete tuşuna basılmalıdır.

![](../_assets/d1cdb275a82bc159e330.png)

#### Şubeler

9.0.25 seti ile birlikte gelen bir destektir. Şubeler İçin Kapanış Fişi Oluşturulabilsin parametresi işaretlendiğinde aktif olmaktadır. Şubeli muhasebe kullanan firmaların kullanımına uygundur.

![](../_assets/978a666da2a5b33443db.png)

Merkez şube içerisindeyken seçilecek şubelerinde kapanış fişlerinin oluşması sağlanacak ve böylece her şube için ayrıca kapanış fişi oluşturmaya gerek kalmayacaktır.

### 1.4.2 Muhasebe Açılış Fişi

Muhasebe Açılış Fişi, her işletme ve şube için ayrı ayrı oluşturulmalıdır.

Yeni sene şirketine aktarılması gereken açılış fişinin oluşturulduğu ve otomatikman aktarıldığı bölümdür. Bu işlemi çalıştırmadan önce dönem sonu kapanış fişi işleminin çalıştırılmış olması gerekmektedir. Bu kapanış fişi baz alınarak yeni senedeki açılış fişi oluşturulacaktır. Devir yapılmadan yeni sene şirketinde muhasebe kayıtlarına başlandığında, ilk ayın yevmiye fiş numaralandırması açılış fişi için bir numara ayıracak şekilde yapılmalıdır. (Örn: 1 numaralı fişi açılış fişi için ayırıp, kayıtlara 2 numaradan başlanmalıdır.)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/855366ed-4816-4f4a-9b68-f131e91d8b88/ssd2026resim24.png)

#### Kapanış Yılı

Devir yapılan şirkette, kapanış fişinin oluşturulduğu yıl kodunun girileceği sahadır.

#### Kapanış Ayı

Devir yapılan şirkette, kapanış fişinin oluşturulduğu ay kodunun girileceği sahadır.

#### Kapanış Fiş No

Devir yapılan şirkette, oluşturulan kapanış fiş numarasının girileceği sahadır. Program tarafından, kapanış ayı sahasında girilen aya ait son fiş numarası otomatik olarak getirilecektir.

#### Açılış Tarihi

Yeni yıl için açılan şirkette oluşturulacak açılış fişi için girilecek ay kodudur. Program tarafından bu sahaya yılın ilk ayı otomatik olarak getirilecektir.

#### İlk Fiş No.

Yeni yıl şirketinde oluşturulacak açılış fişi için verilecek fiş numarasıdır. Yeni yıl şirketinin muhasebe modülünde, işlemler yapılsa bile ilk ayın ilk fiş numarasının açılış kaydı için boş bırakılması gereklidir. Böyle olacağı düşünülerek 01. Ay için bu sahaya 000000000000001 nolu fiş otomatik olarak getirilecektir.

#### Sabit Kayıt Kontrolü Yapılsın

Bu seçenek işaretlendiğinde eski sene şirketinde olup yeni sene şirketinde olmayan muhasebe kodları devir öncesinde yeni sene şirketinde tanımlanacaktır. Sabit Kayıt Kontrolü işlemi ayrıca ortak işletmeden daha detaylı olarak da yapılabilmektedir.

### 1.4.3 Maliyet Muhasebesi Devir

Maliyet Muhasebesi Devir işlemi, her işletme ve şube için ayrı ayrı çalıştırılmalıdır.

Maliyet muhasebesi Modülü kullanan firmalarda, eski sene şirketinde oluşturulan sarf dosyasının son aya ait bilgilerinin, yeni sene şirketine kopyalanması için kullanılacak bölümdür. Maliyet Muhasebesi Devri, maliyet muhasebesi modülü kullanan firmalarda çalıştırılmalıdır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/2a75e82e-e752-45de-bdef-b5c48bc07569/ssd2026resim25.png)

#### Taslak İşlemleri

Devir işlemlerinde verilen kısıtların kaydedilmesi ve daha sonraki senelerde tekrar aynı kısıtların kullanılabilmesi için kısıtlar verildikten sonra Taslak İşlemleri menüsündan Sakla ve tekrar kullanılabilmesi için Oku adımları kullanılmaktadır.

### 1.5 Üretim

### 1.5.1 İş Emri Devir

İş Emri Devir işlemi, her işletme ve şube için ayrı ayrı çalıştırılmalıdır.

Üretim modülünden girilmiş fakat henüz üretimi tamamlanmamış iş emirlerinin, yeni yıl şirketine aktarılmasını sağlayan bölümdür.

#### Taslak İşlemleri

Devir işlemlerinde verilen kısıtların kaydedilmesi ve daha sonraki senelerde tekrar aynı kısıtların kullanılabilmesi için kısıtlar verildikten sonra Taslak İşlemleri menüsündan Sakla ve tekrar kullanılabilmesi için Oku adımları kullanılmaktadır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/d2eecd49-ce03-4833-93e0-8480f56d23b7/ssd2026resim26.png)

### 1.5.2 Mamul Rezervasyonu Devir

Mamul rezervasyonu devir işlemi, tüm işletme ve şube için ayrı ayrı çalıştırılmalıdır.

Bu işlem, MRP parametrelerinde "sipariş bazında rezervasyon sistemi" işaretliyse aktif hale gelmektedir. Müşteri siparişine rezerve edilmiş mamul bakiyelerinin yeni yıl şirketine aktarılmasını sağlayan bölümdür. Mamul rezervasyon devri yapılmadan önce mutlaka stok devri ve sipariş devrinin yapılmış olması gerekmektedir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/e44ea628-cb4d-437e-8f05-a879083227e7/ssd2026resim27.png)

#### Taslak İşlemleri

Devir işlemlerinde verilen kısıtların kaydedilmesi ve daha sonraki senelerde tekrar aynı kısıtların kullanılabilmesi için kısıtlar verildikten sonra Taslak İşlemleri menüsündan Sakla ve tekrar kullanılabilmesi için Oku adımları kullanılmaktadır.

## 1.6 Denetim Listeleri

Modül bazında devirler sonucunda yeni sene şirketinde cari hesap, stok, çek/senet ve banka hareketlerinde oluşan devir kayıtları ile yine yeni sene şirketinde oluşan muhasebe açılış fişi arasındaki farkları, modüllerdeki denetim listeleri mantığında raporlayan bölümdür. Burada bulunan raporlar, devir işlemleri sırasında oluşabilecek farkların program tarafından kapatılabilmesine yönelik olarak kullanılabilir.

### 1.6.1 Cari-Muhasebe Fark Listesi

Cari-Muhasebe Fark İşlemi, Netsis 3 Enterprise, Netsis Wings Enterprise ürünlerini kullanan ve birden fazla işletme tanımlanmış olan firmalarda merkez işletmenin merkez şubesinde, Netsis Wings Entegre, Netsis Wings Entegre Pro, Netsis 3 Standard, Netsis Wings Standard ürünleri ile işletme tanımlanmamış Netsis 3 Enterprise, Netsis Wings Enterprise ürünlerinde, merkez şubede çalıştırılmalıdır.

Bu işlem, Cari Hesap Kayıtlarındaki Muhasebe Hesap Koduna göre, yeni sene şirketinde devirden kaynaklanan cari hareketlerdeki bakiyeler ile carilerin muhasebe hesap kodlarının yeni sene şirketindeki açılış fişinde yer alan bakiyesi arasındaki farkın belirlenmesini sağlar. Bulunan fark isteğe bağlı olarak muhasebe kayıtlarına işlenebilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/58806dac-dadc-4677-8d31-f1cf911e5445/ssd2026resim28.png)

#### Devir Şirketi

Cari hesap ve muhasebe hesaplarının bakiyelerinin kontrol edileceği yeni sene şirketinin girileceği alandır. Yeni Yıl Kopyalama işlemi ile açılan yeni sene şirketi, buraya program tarafından getirilecektir.

#### Cari Kodu

Belirli cari hesaplar için fark kontrolü yapılması isteniyorsa, cari kod aralığının verileceği alandır. Boş geçilmesi halinde tüm cari kodlar için fark kontrolü yapılacaktır.

#### Cari Muhasebe Kodu

Sadece belirli cari muhasebe hesap kodları için fark kontrolü yapılması isteniyorsa, muhasebe hesap kodu aralığı verilebilecek alandır. Boş geçilmesi halinde işlem, cari hesap kayıtlarında girilen tüm muhasebe hesap kodları için çalıştırılacaktır.

#### Yuvarlama Borç/ Alacak Hesap Kodu

Bulunan farkın muhasebe fişi olarak işlenmesi isteniyorsa, cari muhasebe hesap kodlarıyla karşılıklı çalışacak muavin hesapların girilmesi gerekmektedir. Cari Hesap modülündeki devir değeri ile muhasebe açılış fişindeki devir değerini eşitlemek için gerekli fark ilgili muhasebe hesap koduna işlenecek, karşılığında da borç ya da alacak olarak yuvarlama hesapları çalışacaktır.

#### Kayıtlara Geçsin

İşlemin, bu seçenek işaretlenerek çalıştırılması halinde, bulunan fark tutarları, yeni sene şirketinde yevmiye fişi haline getirilecektir. Oluşturulan fişin tarihi 01/01/2024, açıklaması ise "Cari-Muhasebe Fark İşlemi" olacaktır. İşlem, bu seçenek işaretlenmeden çalıştırılır ise, bulunan fark tutarları işlem tamamlandıktan sonra, sadece listelenecek ancak muhasebe kayıtlarına geçmeyecektir.

### 1.6.2 Stok-Muhasebe Fark İşlemi

Stok-Muhasebe Fark İşlemi, Netsis 3 Enterprise, Netsis Wings Enterprise ürünlerini kullanan ve birden fazla işletme tanımlanmış olan firmalarda merkez işletmenin merkez şubesinde, Netsis Wings Entegre, Netsis Wings Entegre Pro, Netsis 3 Standard, Netsis Wings Standard ürünleri ile işletme tanımlanmamış Netsis 3 Enterprise, Netsis Wings Enterprise ürünlerinde, merkez şubede çalıştırılmalıdır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/82097045-95d4-40d6-8ba0-7fdd8eae6f2d/ssd2026resim29.png)

Bu işlem, Stok Kartı Muhasebe Detay Koduna ait Alış Hesap Koduna göre, yeni sene şirketinde devirden kaynaklanan stok hareketlerdeki bakiyeler ile stok alış hesap kodlarının yeni sene şirketindeki açılış fişinde yer alan bakiyesi arasındaki farkın belirlenmesini sağlar. Bulunan fark tutarları, isteğe bağlı olarak muhasebe kayıtlarına işlenebilir.

#### Devir Şirketi

Stok devirleri ile muhasebe hesaplarının bakiyelerinin kontrol edileceği yeni sene şirketinin girileceği alandır. Yeni Yıl Kopyalama işlemi ile açılan yeni sene şirketi, buraya program tarafından getirilecektir.

#### Stok Kodu

Belirli stok için fark kontrolü yapılması isteniyorsa, stok kodu aralığının verileceği alandır. Boş geçilmesi halinde işlem tüm stok kodları için çalıştırılacaktır.

#### Muhasebe Detay Kodu

Sadece belirli muhasebe detay kodlarında bulunan alış hesap kodları için fark kontrolü yapılması isteniyorsa, muhasebe detay kodu aralığı verilebilecek alandır. Boş geçilmesi halinde işlem, muhasebe hesap kayıtlarında girilen tüm muhasebe hesap kodları için çalıştırılacaktır.

#### Mali Grup Kodu

Maliyet Muhasebesi kullanan firmalarda Mali Grup Kodu Kayıtlarında girilen Mamul ve Yarı Mamul hesabına göre fark kontrolü yapılacaktır. Stok Kartı Kayıtlarında, tipi mamul ya da yarı mamul işaretlenmiş stokların, Mamul Grup Kodları için aralık verilebilecek sahadır.

#### Yuvarlama Borç/ Alacak Hesap Kodu

Bulunan farkın muhasebe fişi olarak işlenmesi isteniyorsa, stok alış hesap kodlarıyla karşılıklı çalışacak muavin hesapların girilmesi gerekmektedir. Stok modülündeki devir değeri ile muhasebe açılış fişindeki devir değerini eşitlemek için gerekli fark, ilgili muhasebe hesap koduna işlenecek, karşılığında da borç ya da alacak olarak yuvarlama hesapları çalışacaktır.

#### Kayıtlara Geçsin

İşlemin, bu seçenek işaretlenerek çalıştırılması halinde, bulunan fark tutarları, yeni sene şirketinde yevmiye fişi haline getirilecektir. Oluşturulan fişin tarihi 01/01/2023, açıklaması ise "Stok-Muhasebe Fark İşlemi" olacaktır. İşlem, bu seçenek işaretlenmeden çalıştırılır ise, bulunan fark tutarları işlem tamamlandıktan sonra, sadece listelenecek ancak muhasebe kayıtlarına geçmeyecektir.

### 1.6.3 Çek/Senet-Muhasebe Fark Listesi

Çek/Senet-Muhasebe Fark İşlemi, Netsis 3 Enterprise, Netsis Wings Enterprise ürünlerini kullanan ve birden fazla işletme tanımlanmış olan firmalarda merkez işletmenin merkez şubesinde, Netsis Wings Entegre, Netsis Wings Entegre Pro, Netsis 3 Standard, Netsis Wings Standard ürünleri ile işletme tanımlanmamış Netsis 3 Enterprise, Netsis Wings Enterprise ürünlerinde, merkez şubede çalıştırılmalıdır.

Bu işlem, Entegrasyon Modülünde tanımlanan çek/senet hesap kodlarına göre, yeni sene şirketinde devirden kaynaklanan çek/senet bakiyeleri ile çek/senet kodlarının yeni sene şirketindeki açılış fişinde yer alan bakiyesi arasındaki farkın belirlenmesini sağlar. Bulunan fark tutarları, isteğe bağlı olarak muhasebe kayıtlarına işlenebilir. Entegrasyon modülünde "Dövizli Senet/Çek İçin Özel Hesap Kodu Uygulaması Var mı?" parametresi işaretli ise, Entegrasyon kodlarında çek ve senetler için girilen muhasebe hesap kodları değil, çek ve senetlerin girişlerinde kullanılan döviz tipleri için kullanılan hesap kodları kontrol edilecektir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/7893d69c-ca06-4368-851e-c140d1b2ec94/ssd2026resim30.png)

#### Devir Şirketi

Devredilen çek/senet tutarları ile muhasebe hesaplarının bakiyelerinin kontrol edileceği yeni sene şirketinin girileceği alandır. Yeni Yıl Kopyalama işlemi ile açılan yeni sene şirketi, buraya program tarafından getirilecektir.

#### Modül

Hangi modül için fark kontrolünün yapılacağı bu sahada belirlenmektedir. İşlemi, Müşteri Çekleri, Müşteri Senetleri, Borç Çekleri ya da Borç Senetleri modüllerinden biri için çalıştırabilirsiniz.

#### Yuvarlama Borç/ Alacak Hesap Kodu

Bulunan farkın muhasebe fişi olarak işlenmesi isteniyorsa, çek/senet hesap kodlarıyla karşılıklı çalışacak muavin hesapların girilmesi gerekmektedir. Çek/Senet modüllerindeki devir değeri ile muhasebe açılış fişindeki devir değerini eşitlemek için gerekli fark, ilgili muhasebe hesap koduna işlenecek, karşılığında da borç ya da alacak olarak yuvarlama hesapları çalışacaktır.

#### Kayıtlara Geçsin

İşlemin, bu seçenek işaretlenerek çalıştırılması halinde, bulunan fark tutarları, yeni sene şirketinde yevmiye fişi haline getirilecektir. Oluşturulan fişin tarihi 01/01/2023, açıklaması ise "Çek/Senet-Muhasebe Fark İşlemi" olacaktır. İşlem, bu seçenek işaretlenmeden çalıştırılır ise, bulunan fark tutarları işlem tamamlandıktan sonra, sadece listelenecek ancak muhasebe kayıtlarına geçmeyecektir.

### 1.6.4 Banka-Muhasebe Fark Listesi

Banka-Muhasebe Fark İşlemi, Netsis 3 Enterprise, Netsis Wings Enterprise ürünlerini kullanan ve birden fazla işletme tanımlanmış olan firmalarda merkez işletmenin merkez şubesinde, Netsis Wings Entegre, Netsis Wings Entegre Pro, Netsis 3 Standard, Netsis Wings Standard ürünleri ile işletme tanımlanmamış Netsis 3 Enterprise, Netsis Wings Enterprise ürünlerinde, merkez şubede çalıştırılmalıdır.

Bu işlem, Banka Hesap Kayıtlarındaki Muhasebe Hesap Koduna göre, yeni sene şirketinde devirden kaynaklanan banka hareketlerindeki bakiyeler ile banka muhasebe hesap kodlarının yeni sene şirketindeki açılış fişinde yer alan bakiyesi arasındaki farkın belirlenmesini sağlar. Bulunan fark tutarları, isteğe bağlı olarak muhasebe kayıtlarına işlenebilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/402f3457-2332-4caf-8217-c51a7cb9a1cb/ssd2026resim31.png)

#### Devir Şirketi

Devredilen banka hesap tutarları ile muhasebe hesaplarının bakiyelerinin kontrol edileceği yeni sene şirketinin girileceği alandır. Yeni Yıl Kopyalama işlemi ile açılan yeni sene şirketi, buraya program tarafından getirilecektir.

#### Banka Hesap Kodu

Sadece belirli banka hesap kodları için fark kontrolü yapılması istendiği zaman banka hesap kodu aralığı girilen alandır. Rehber butonu ile, banka hesap kodları arasından seçim yapılır.

#### Hesap Muhasebe Kodu

Sadece belirli banka muhasebe hesap kodları için fark kontrolü yapılması isteniyorsa, muhasebe hesap kodu aralığı verilebilecek alandır. Boş geçilmesi halinde işlem, Banka Hesap Kayıtlarında girilen tüm muhasebe hesap kodları için çalıştırılacaktır.

#### Yuvarlama Borç/ Alacak Hesap Kodu

Bulunan farkın muhasebe fişi olarak işlenmesi isteniyorsa, banka muhasebe hesap kodlarıyla karşılıklı çalışacak muavin hesapların girilmesi gerekmektedir. Banka modülündeki devir değeri ile muhasebe açılış fişindeki devir değerini eşitlemek için gerekli fark ilgili muhasebe hesap koduna işlenecek, karşılığında da borç ya da alacak olarak yuvarlama hesapları çalışacaktır.

#### Kayıtlara Geçsin

İşlemin, bu seçenek işaretlenerek çalıştırılması halinde, bulunan fark tutarları, yeni sene şirketinde yevmiye fişi haline getirilecektir. Oluşturulan fişin tarihi 01/01/2023, açıklaması ise "Banka-Muhasebe Fark İşlemi" olacaktır. İşlem, bu seçenek işaretlenmeden çalıştırılır ise, bulunan fark tutarları işlem tamamlandıktan sonra, sadece listelenecek ancak muhasebe kayıtlarına geçmeyecektir.

### 1.6.5 Parametre Kayıtları

Devir işlemlerine yeni eklenen VBscript özelliği ile firmalara özel devir uygulamalarının yazılması mümkündür. Bunun için ekrandaki "Dinamik Kodlama ile Firmaya Özel Devir Yapılsın" parametresinin işaretli olması gerekmektedir.

![](../_assets/b8f0ea09293775a25fa9.png)

Bu parametre işaretlendikten sonra bu ekrana yazılan Vbscript kodu, Yeni Yıl Kopyalama işleminde çalışacaktır. Parametre işaretli ise, Yeni Yıl Kopyalama işleminin standardında olan ve program tarafından yapılan yedekleme, yedekten dönme ve tabloların içeriklerinin silinmesi işlemlerinin tamamı script içine istenildiği şekilde baştan yazılmalıdır. Yeni Yıl Kopyalama işlemi, script ile çalıştıktan sonra, modül devirleri ilgili menü seçeneklerinden yapılabilir. İstenirse herhangi bir modül devrine ait işlemler de script'e eklenebilir. Bu durumda ilgili bölümün devri, menü seçeneğinden çalıştırılmayıp, script sırasında çalışması sağlanabilir.

***Not:*** 9.0.44 sürümünde devir ile ilgili yapılan yenilikler aşağıdaki şekildedir:

*(https://*[*www.youtube.com/watch?v=kD1_VPcaWIg)*](<http://www.youtube.com/watch?v=kD1_VPcaWIg)>)

- Yeni yıla devirden sonra vadesi eski yıl olan ancak henüz ödenmemiş olan taksitlerin de yeni yıl şirketine getirilmesi sağlanmıştır.
- Cari devirde "Cari Hareket Döviz Tiplerine Göre" devir yapılıyor iken eski sene şirketinde yıl sonunda hesaplatılan kur farkı kayıtlarının yeni sene şirketine aktarılması sağlanmıştır. DEVIR/YASLANDIRMALICARI_KURFARKI_DEVREDILSIN özel parametresinin tanımlı olması gerekmektedir.
- Banka devri ekranında ileri kısıt bileşeni desteklenmiştir.
- Cari devir ekranında Devir Tipi "Cari Hesap Tipine Göre" seçildiğinde aktif olacak şekilde "Kapatılmamış Hareketlerin Kalan Tutarları Aktarılsın" parametresi desteklenmiştir. Bu seçenek işaretli olduğunda eski yıl şirketinde özel hesap kapatması yapılmamış ve açıkta kalan hareketler yeni yıl şirketine aktarılırken eski yıl şirketindeki (tutar-kapatılmış tutar) değeri ile aktarılacaktır.
- "Faturadaki "İthalat\\İhracat miktarları stoklara geçsin" parametresini işaretli ve devir yaparken "ithalat\\ihracat belgeleri aktarılmasın" işaretli olma durumuna göre stok bakiyesinin devredilen şirkette hesaplanmasına yönelik çalışma yapılmıştır.

### 1.6.6 Sıkça Karşılaşılan Hatalar ve Çözümleri

Sene sonu devir ile ilgili sıkça sorulan soru ve çözümleri için burayı [tıklayınız.](<Sene Sonu Devir Sıkça Sorulan Sorular.md>)
