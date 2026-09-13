---
title: "Yeni Yıl Kopyalama"
page_id: "47073661"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Genel"
  - "Sene Sonu Devir"
  - "Kayıt / Sene Sonu Devir"
  - "Yeni Yıl Kopyalama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Sene Sonu Devir / Kayıt / Sene Sonu Devir / Yeni Yıl Kopyalama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTBhOTliZTZkLTg3ODAtNDFjMy1hNTYzLThkMmRkNmI1MDlkZSZsaW5rPTliMmU3Y2NkLTRmZjQtNGE5MC05NzJkLTAzYzhjNWViMGNmNyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=0a99be6d-8780-41c3-a563-8d2dd6b509de&link=9b2e7ccd-4ff4-4a90-972d-03c8c5eb0cf7&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "yeni-yil-kopyalama_47073948_47073661.html"
source_version: "2022-10-19T10:27:58.653+03:00"
source_bytes: 98922
fetched_at: "2026-09-13T04:18:03+00:00"
generator: "netsis-scraper 1.0.0"
---
# Yeni Yıl Kopyalama

Yeni Yıl Kopyalama, modül devirleri yapılmadan yeni yıl şirketinin hazırlanmasında kullanılan bölümdür. Yeni Yıl Kopyalama, yeni yılda çalışılacak şirket bilgisinin oluşturulmasını ve eski yıl şirketinde bulunan sabit bilgilerin bu şirkete geçmesini sağlar. Yeni Yıl Kopyalama işlemi, Enterprise ürünlerini kullanan ve birden fazla işletme tanımlanan firmalarda işletmelerin merkezinde, Standard ve Entegre ürünleri ile Enterprise ürünlerinde işletme tanımlanmayan firmalarda ise merkez şubede çalıştırılması gerekir.

Yeni Yıl Kopyalama ekranı; Giriş, İşlem ve İşlem Sonucu olmak üzere üç sekmeden oluşur.

**Giriş**

**![](../../../../_assets/0a0d99631b47d2010d6f.png)**

**İşlem**

**![](../../../../_assets/9b5ad7be9cd2d2485c50.png)**

Yeni Yıl Kopyalama ekranı İşlem sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Yeni Yıl Kopyalama Ekranı |  |
| --- | --- |
| Devir Şirketi | Yeni yılda kullanılacak şirket isminin girildiği alandır. Girilen şirketin önceden açılmaması gerekir. Girilen şirket program tarafından açılır. "Yeni Yıl Kopyalama" işlemi aynı yeni yıl şirketinin ismi kullanılarak birden fazla tekrarlanıyorsa, "Yeni Yıl Kopyalama" işlemi öncesinde devir şirketinin "Şirket Silme işlemiyle silinmesi gerekir. |
| Devir Yılı | Devredilecek eski yıl bilgisinin girildiği alandır. |
| Mali Başlangıç Ayı Dikkate Alınsın | "Muhasebe" modülünde yer alan parametrelerde mali başlangıç ayı 1’den farklı olan şirketler için kullanılan seçenektir. İşaretlendiğinde, "Yeni Yıl Kopyalama" ve modül bazında devirler özel döneme göre yapılır. |
| Veritabanı Yedeği İçin Başka Dizin Kullan | "Yeni Yıl Kopyalama" işleminde backup/restore işlemi yapıldığı için SQL server yüklü makinenin diskinde yeterli yer olması gerekir. Yeterli yer olmaması halinde, istendiği zaman "Veritabanı Yedeği İçin Başka Dizin Kullan seçeneği" işaretlenerek yedeğin alınması için boş alana sahip olan diğer diskteki bir dizin verilebilir. İşlem sonunda geçici dosyalar silinir. |
| Önceki Yıl Fiyat Listeleri Yeni Yıla Aktarılsın | Devir yapılan yıla ait fiyat listelerinin yeni yıl şirketine aktarılması için kullanılan seçenektir. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilgilerin onaylanmasını sağlayan butondur. |
| ![](../../../../_assets/249197106fa4d90d9fe9.png) Çıkış | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |

Yeni Yıl Kopyalama işlemi sırasında program tarafından yapılan işlemler aşağıdaki gibidir:

- Eski senenin tüm bilgilerinin - table, view gibi - yedeği alınır.
- Yedeklenen bu bilgiler, devir şirketine yüklenir.
- Yeni yıl şirketindeki hareketler iptal edilir, sabitler ise kalır.

Bazı tablolarda ise, birtakım koşullara bağlı iptaller yapılır.

**Örneğin;** Koşul tablolarında, kapatılmış koşullar iptal edilip aktif koşullar yeni senede kullanılması için bırakılır.

Bu türden işlem gören tablolar; TBLKOSULEK,TBLKOSDETAY,TBLKOSGENEL,TBLDEPSAYIM,TBLMUHAGEC, TBLNAKLIYEBELGELINK,TBLNAKLIYE,TBLTAHSILAT,TBLFIYFARKMAS,TBLFATUIRS, TBLFARKLITESLIM,TBLTARTIMBLG,TBLTAHSILAT,TBLKASA,TBLMUSTAHSI,TBLREPLANIS, TBLSAYIM,TBLSTOKFIAT,TBLREVERRORLOG,TBLSTOKURS,TBLBNKTEMTRA, TBLBNKTEMSABIT,TBLDAMGAVERGISI,TBLKDVBEYAN,TBLMUHTASAR,TBLFATUVADE, TBLFATUEK,TBLKOSULMAS,TBLDEKOTRA,TBLDEKOMAS,TBLCEKSENDEK, TBLDAGAKTARIMLOG,TBLCRMFIRSATURUN,TBLCRMFIRSAT,TBLCRMADAYURUN, TBLCRMADAY,TBLCRMSATAKT,TBLCRMPAZALTAKT,TBLCRMPAZAKT,TBLBEYANBASIM, TBLCRMSKYAKT,TBLCRMSKYSABIT,TBLCRMANK,TBLCRMANKCEVAPMAS, TBLCRMAN tablolarıdır.

Eski yıla ait hareket kayıtlarının tamamı silinen tablolar ise; TBLCRMANKICERIK,TBLCRMANKSABIT,TBLSMSTRA,TBLSMSMAS,TBLMAKMALIYET, TBLMAKSARF,TBLBKMBIS,TBLBKMSBPER,TBLBKMSBSTOK,TBLBKMTRA,TBLBKMTALEP, TBLBKMPLAN,TBLBKMSOZDET,TBLMAKBKM,TBLBKMSOZMAS,TBLKRTSOZKST,
TBLKRTSOZTRA,TBLKRTSOZMAS,TBLFORECAST,TBLMPS,TBLNPMLOG,TBLSSATIRAC, TBLKKMAS,TBLHIZMETMALIYETMAS,TBLHIZMETPRIMTANIM, TBLHESTEMP,TBLIMALAT,TBLKAMBBCEK,TBLBCEK,TBLKAMBBSEN,TBLBSEN, TBLKAMBMSEN,TBLMSEN,TBLKAMBMCEK,TBLMCEK,TBLODEEMIR,TBLCAHAR, TBLOZELHESAP,TBLCEKSENLOG,TBLDEPDURUM,TBLSIPAMAS,TBLSIPATRA, TBLNETSISLOG,TBLMALISARF,TBLMALIYET,TBLMUHARES,TBLMUHMAS,TBLMUHFIS, TBLMUPLANSUBE,TBLSTHAR,TBLDEPHAR,TBLSTOKPH,TBLISEMRI,TBLISEMRIREC, TBLUAKMAS,TBLBAGLANTI,LOGQUERYINFO,TBLAL12,TBLAL12DUMY,
TBLBNKHESTRA,TBLBNKLOGTRA,TBLBORDROMAS,TBLDAGDISPATCH,TBLDAGKMTAKIP, TBLDAGPENETRASYON,TBLDAGPLASZIYARET,TBLDAGZIYRAPORDETAY,TBLSEVKMAS, TBLSEVKTRA,TBLTEKLIFMAS,TBLTEKLIFTRA,TBLBCK_MRP,TBLBCK_MRP_DETAIL, TBLBCK_MRPPLAN,TBLBCK_MRPSIP,TBLMRPSIP,TBLKAPASITE,TBLMRP,TBLMRP_DETAIL, TBLSERITRA,TBLACIKREC,TBLDAGFUNCHIST,TBLDAGFUNCHISTXML,TBLDZNBASIMLOG, TBLBFORMU,TBLCRMFORECAST,TBLCRMHEDEF,TBLFATKALEMILISKI,TBLKUMGENEL,
TBLFORECASTHAZIRLIK,TBLIMZALOG,TBLBNKMSRF,TBLMPSKAPASITE, TBLPOSAKTARILANLAR, TEMP_MUHAGEC,TBLKRTTHSLT,TBLISEMRIEK, TBLMSENPARCA,TBLBSENPARCA,TBLMCEKPARCA,TBLBCEKPARCA, TBLHIZMETMALIYETFISTRA,TBLHIZMETMALIYETSTHARFISTRA,TBLMRPSIPBELGELOG, TBLMRPSIPEKRMAS,TBLMRPSIPEKRTRA,TBLMRPSIPBAGLANTI,TBLBCK_MGPMAS, TBLISEMRIREZERVESTOK,TBLMUHFISEK,TBLEFATMAS,TBLEFATURA,TBLEFATYANIT,TBLE
FATZARF, TBLEDEFTER, TBLEFATKALEMTAX, TBLEFATMASTAX,TBLEARSIV tablolarıdır.

Yeni sene şirketinde, her bölüme ait sabit kayıtlarda - Stok kartı kayıtları, Cari hesap kayıtları, Hesap planı, Banka Hesap Kayıtları - eski seneden oluşan toplam giriş, çıkış ve bakiye bilgileri sıfırlanır.

Devir şirketi ve Devir Yılı sorgulamaları geçildikten sonra, "Devir işlemleri için yeni bir şirket açılacak. Emin Misiniz?" şeklinde bir onay ekranı görüntülenir. "Evet" butonu ile onaylandığında, uzun zaman alacak bir takım işlemler program tarafından yapılmaya başlar. Bu aşamada kullanıcı müdahalesine gerek yoktur.

CRM Uygulaması Var İse; CRM Uygulamasının kullanıldığı durumlarda, CRM’de girilen sabit kayıtlar ile açık olan aday, fırsat, aktivite, anket ve şikayet kayıtları "Yeni Yıl Kopyalama" işlemi ile yeni yıl şirketine aktarılır. CRM kayıtlarının devri için modül devri yapılmasına gerek yoktur. "Yeni Yıl Kopyalama" işlemi sonrası CRM Uygulamasına mutlaka yeni yıl şirketinde devam edilmesi gerekir. Diğer modüllerin kayıtları, geçmiş yıl şirketinde yapılıyorsa CRM Uygulaması tarafından oluşturulan yeni cari hesap kayıtları, talep/teklif, sipariş ve faturaların kod ve numaralarına dikkat edilmesi gerekir. Çünkü, bu numaraların eski yıl şirketinde girilen yeni yıla ait kayıtlarda kullanılmamış olması gerekir. Aksi taktirde, modül devirleri sırasında numara ve kod çakışması olabilir.

#### Yeni Yıl Kopyalama Sırasında Yedekleme/Yükleme İşlemi

**MS SQL Server:** Yeni yıl kopyalama işleminde yedekleme/yükleme işlemi yapıldığı için, SQL server yüklü makinenin diskinde yeterli yer olması gerekir. Yer olmaması halinde yeni yıl kopyalama işlemi uyarı verir. Bu durumda, disk üzerinde boş alan ayarlanarak işleme devam edilebilir.

İstendiği zaman - aynı sunucuda bulunan farklı bir diskte boş alan olması halinde - tanımlanan özel bir parametre ile yedeğin boş alana sahip olan diğer diskteki bir dizinde oluşturulması sağlanabilir. Bunun için Yardımcı Programlar → Özel Parametre Kayıtları menüsünde tanımlama yapılması gerekir.

Özel parametre tanımlamasının, Grup Kodu: DEVIR, Anahtar: MSSQLBACKUPDIZINI, Değer: “SQL Sunucu üzerinde bir dizin” şeklinde yapılması gerekir. "Sene Sonu Devir "işleminde yedeğin alınacağı dizin sorgulanmaz ve yedek, parametrede belirlenen dizinde oluşturulur.

**Oracle:** Eğer **kullanılan veri tabanı Oracle ise,** "Yeni Yıl Kopyalama" ekranında Tamam ![](../../../../_assets/39d77b8716226638d9ce.jpg) butonuna tıklandığında Yeni Yıl Kopyalama işleminin yapılması için dizin sorgulanan bir ekran görüntülenir. Kopyalanacak şirketin tüm bilgilerinin, geçici bir klasörde yedeğinin alınması için işlemin yapılacağı istemcide yeterli boş alanın ve ilgili kullanıcı haklarının yeterli olması gerekir. İşlem sonunda geçici dosyalar silinir.

**İşlem Sonucu**

İşlem sırasında oluşan hatalar "İşlem Sonucu" sekmesinde görüntülenerek farenin sağ tuşuna tıklanarak dosyaya kaydedilir. Gelen hataların incelenmesi gerekir.

"Yeni Yıl Kopyalama" işlemi, devir şirketi oluşturulduktan sonra, herhangi bir hatadan dolayı yarım kalabilir. İşlemin kesilmesine sebep olan problem çözüldükten sonra; yeni sene için açılan şirketi sıfırlayarak ya da, yeni sene hazırlık işlemine kalınan yerden devam etmek mümkündür.

Açılan şirketi sıfırlayarak yeni yıl kopyalama işlemine baştan başlamak için, "Şirket Silme" işlemi ile yeni şirketin silinmesi gerekir.

Kalınan yerden "Yeni Yıl Kopyalama" işlemine devam etmek için, işlem tekrar çalıştırılarak, sorgulanan sahalara daha önceden girilen bilgilerin girilmesi ve "Evet" butonuna tıklanması gerekir.

Bu durumda, kalınan yerden işleme devam etmek istenip istenmediğinin sorgulandığı bir ekran görüntülenir. “Evet” butonuna tıklanması ile yeni yıl şirketinin tekrar kopyalanmasına gerek kalmadan devir işlemine devam edilir.

İşlemler bittiğinde, modül devirleri öncesi, yeni sene kayıtlarına başlama ortamının hazırlanması işlemi tamamlanır. İstendiğinde eski senenin kayıtları bitene kadar, hiç bir modülün devri yapılmadan eski sene şirketinde ve yeni sene şirketinde ayrı ayrı çalışılarak kayıtlara devam edilebilir. Eski senenin devir kayıtları, eski sene kapatılıp devir yapıldığında yeni sene bilgilerine aktarılır. İstendiğinde modül devirleri programın içinden yapılmayıp, açılan yeni sene şirketinde elle kaydedilebilir. Bu işlemlerden biri yapılmadan yeni sene bakiyelerini doğru olarak izlemek mümkün değildir.

"Yeni Yıl Kopyalama" işlemi ile devri oluşturulan eski şirkete girerken, “Şirket devri yapılmıştır. Devir Şirketi: DEVIR. Bu şirketin sadece rapor amaçlı kullanılması tavsiye edilmektedir. Yeni yıla ait kayıtlarınızı veya düzeltme işlemlerinizi DEVIR şirketine yapabilirsiniz!” şeklinde bir uyarı mesajı görüntülenir.

Dosyaya bağlanan ve dosyası kapatılan dış ticaret belgelerinin yeni yıl şirketine aktarılmaması sağlanır.
