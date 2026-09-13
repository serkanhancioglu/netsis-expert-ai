---
title: "Serili Stok Devri"
page_id: "24753435"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Genel"
  - "Sene Sonu Devir"
  - "Kayıt / Sene Sonu Devir"
  - "Lojistik Satış"
  - "Serili Stok Devri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Sene Sonu Devir / Kayıt / Sene Sonu Devir / Lojistik Satış / Serili Stok Devri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTIwMGYzYjMyLWNlZDEtNDE0ZS1hM2VkLWQ1MmMzNWRhYTBiMCZsaW5rPTA1NTAzOTNjLWU1ZTUtNDBmZC1hNWRhLTY3Mzk4NmUyMWY4NCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=200f3b32-ced1-414e-a3ed-d52c35daa0b0&link=0550393c-e5e5-40fd-a5da-673986e21f84&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "serili-stok-devri_47073512_24753435.html"
source_version: "2022-10-19T13:54:39.580+03:00"
source_bytes: 149569
fetched_at: "2026-09-13T04:18:08+00:00"
generator: "netsis-scraper 1.0.0"
---
# Serili Stok Devri

Serili Stok Devri, Genel Bölümü'nde, "Kayıt/Sene Sonu Devir" menüsünün altında yer alır. Serili Stok Devri, "Genel Parametre Kayıtları" bölümünde “Seri Uygulaması” parametresini kullanan ve stok kartlarında giriş ve çıkışlarda seri uygulaması işaretli olan stok devirlerinin yapıldığı bölümdür. "Serili Stok Devir" işleminin, tüm versiyonlarda her işletme ve şube için ayrı ayrı çalıştırılması gerekir. Serili Stok Devri; Giriş, İşlem ve İşlem Sonucu sekmesinden oluşur.

Serili stok devri yapılacağı zaman, seriler ya da stokların eksi bakiye vermemesi gerekir. Stokların bir kısmının serili, bir kısmının da serisiz kullanıldığı durumlarda, Serili ve Serisiz Stok Devri işlemlerinin her ikisinin de çalıştırılması gerekir. Böylece, hangi işlemde hangi stokların devredileceği stok kartındaki seri parametrelerine göre belirlenir. Stok sabit bilgilerinin yeni sene şirketine aktarılması işleminin önceden "Yeni Yıl Kopyalama" bölümünden yapılması gerekir. Sabit işleme bağlı hareketlerin devri yapılarak, sonuç devir hareketi yeni sene şirketindeki hareketlere işlenir. Sipariş ve talep/teklif takibi kullanıldığında ve sipariş ile talep/teklif devirleri henüz yapılmadığında, stok devrini yapmadan önce sipariş ve talep/teklif kayıtlarının devredilmesi gerekir. Ayrıca; "Esnek Yapılandırma" uygulamasının kullanıldığı firmalarda, stok hareketleri yapılandırma kodları bazında kırılımlı olarak program tarafından olusturulur. "Lokal Depo Uygulaması" olan firmalarda, lokal depolara göre devir işlemi, stok devri sırasında program tarafından otomatik olarak yapılacağı için lokal depolardaki tüm çalışmaların bitirilmesi gerekir. Serili stok devri yapılırken öncelikle, verilecek kısıtlar doğrultusunda stok bakiyeleri bulunur ve bakiye devirler aktarılır. Devir hareketleri ile bağlantılı seriler ilk giren ilk çıkar metoduna göre bulunur ve stok hareketleri ile ilişkilendirilir. Aktarılan seriler, yeni yıl şirketinde, stok hareketlerinde farenin sağ tuşu ile tıklandığında görüntülenen “Seri Bilgisi İzleme” adımından ya da "Seri Takibi Bakiye Listesinden" izlenebilir. Rapor Modülü → Stok Raporları → "[Seri Kayıt Listesi](<../../../Rapor/Stok Raporları/Seri Kayıt Listesi.md>)" bölümünden hazırlanacak bir rapor ile, eski yıl şirketinde bu serilerin hangi belgeden aktarıldığına dair detay bilgiler de görülebilir.

**Giriş**

**![](../../../../../_assets/1274490fef44a42064f1.png)**

**İşlem**

![](../../../../../_assets/a2dba5d513730cca5b01.png)

Serili Stok Devri ekranı İşlem sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Serili Stok Devri Ekranı |  |
| --- | --- |
| Devir Şirketi | Yeni yılda kullanılacak şirket isminin girildiği alandır. Girilen şirketin önceden açılmaması gerekir. Girilen şirket program tarafından açılır. "Yeni Yıl Kopyalama" işlemi aynı yeni yıl şirketinin ismi kullanılarak birden fazla tekrarlanıyorsa, "Yeni Yıl Kopyalama" işlemi öncesinde devir şirketinin "Şirket Silme işlemiyle silinmesi gerekir. |
| Devir Baz Tarihi | Stok devri için baz alınacak tarihin girildiği alandır. Yılın son günü otomatik olarak gelir. Devir baz tarihinden önceki stok hareketleri, seçilen maliyet türüne göre devredilir. Bu tarihten sonraki hareketler aynen yeni şirkete aktarılır. |
| Devir Tarihi | Yeni şirkete aktarılacak stok devirleri için kullanılması istenen tarihin girildiği alandır. |
| Maliyet Türü | FIFO (ilk giren ilk çıkar), LIFO (son giren ilk çıkar), Ağırlıklı Ortalama, Hareketli Ortalama, Aylık Ağırlıklı Ortalama, Maliyet Muhasebesi Fiyatı ve Alış Fiyatı maliyet türlerinden oluşan alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile maliyet türleri arasından seçim yapılarak kısıt verilir. Maliyet Muhasebesi kullanan firmaların maliyet türü olarak "Maliyet Muhasebesi Fiyatını" seçmeleri gerekir. Böyle bir durumda stok devrinde, stok kartlarındaki maliyet fiyatları baz alınır. |
| İthalat/İhracat Hareketleri Aktarılmasın | Serili stok devri yapılırken ithalat/ihracat hareketlerinin aktarılmaması için kullanılan seçenektir. |
| Dinamik Depo İçin Devir Yapılsın | "Dinamik Depo" modülü kullanan firmalarda merkez isletme ya da şubede işaretli olarak gelir ve değiştirilemez. Devir için verilen tarih itibari ile hücre bakiyeleri, yeni seneye devir olarak işlenir. |
| Devirde Hücre Kodu Dikkate Alınsın | "Bakiye Verenler" seçeneği işaretlendiğinde aktif hale gelen alandır. "Dinamik Depo" modülünün kullanıldığı durumlarda, bakiye veren seri kayıtları aktarılırken, bakiye kontrolünün hem seri hem de seri kayıtlarında bulunan hücre koduna göre yapılması İçin kullanılan seçenektir. Bu seçeneğin işaretlenmesi halinde, "Seri" ve "Hücre Kodu" kırılımında aktarım gerçekleşir. |
| Devirde Seri-2 Dikkate Alınsın | Bakiye veren seri kayıtları aktarılırken, bakiye kontrolünün hem seri hem de seri-2’ye göre yapılmasını sağlayan seçenektir. Aktarım, Seri ve Seri-2 kırılımlı olarak yapılır. |
| Dövizli Stok Devri İçin | Dövizli stok devri, FAS52, IAS29 veya Enflasyon Muhasebesi seçeneklerinden birinin kullanılması durumunda mutlaka gereklidir. Dövizli stok devri yapılması için öncelikle maliyet türü olarak "Aylık Ağırlıklı Ortalama", "FIFO", "LIFO" veya "Maliyet Muhasebesi Fiyatı" seçeneklerinden birinin işaretlenmesi gerekir. Bu durumda program, seçilen maliyet türüne göre her stokun dövizli birim maliyet fiyatını bularak, yeni yıl şirketinde döviz tutarına aktarır. Döviz tipi olarak "Genel Parametre Kayıtları" bölümündeki firma döviz tipi kullanılır. |
| Eksi Bakiyeliler Devredilsin | Bakiyesi eksiye düşen stokların da yeni yıl şirketine aktarılması için kullanılan seçenektir. Kullanılmadığı zaman, eksi bakiyeli olan stokların devri yeni yıl şirketine aktarılmaz. |
| Seri Kadar Stok Hareket Atılmasın | Serili stok devri yapılırken, seri kadar stok hareketi aktarılmaması için kullanılan seçenektir. |
| Sadece Girişte Seri Takibi Yapılan Stoklar Da Devredilsin | Serili stok devri yapılırken, sadece girişte seri takibi yapılan stokların da devredilmesi için kullanılan seçenektir. |
| Stok ve Seri Bakiyesi Ayrı Bağlantısız Olarak Aktarılsın | Serili stok devri yapılırken stok ve seri bakiyesinin bağlantısız olarak ayrı aktarılması için kullanılan seçenektir. "Hepsi" ve "Bakiyeli" seçenekleri arasından seçim yapılır. İşaretlendiğinde, "Bu seçeneği işaretlemeniz serisiz stokların da devredilmesi anlamına gelmektedir. Daha önce serisiz stok devri yaptıysanız tekrarlı kayıt oluşmaması için kayıtları sildiğinizden emin olunuz." uyarısı ekrana gelir. İşleme devam edilmesi için "Tamam" butonu ile onay verilerek ilerlenir. |
| Devirden Sonra Stok Hareket Kontrol İşlemi Çalıştırılsın | Devir sonrası stok hareket kontrolünün çalıştırılması için kullanılan seçenektir. |
| Sabit Kayıt Kontrolü Yapılsın | Serisiz stok devri işleminde sabit kayıt kontrolünün yapılması için kullanılan seçenektir. |
| Proje Kırılımlı Devir | Devrin, proje kırılımlı yapılması için kullanılan seçenektir. İşaretlenmediği zaman, alanın sağ tarafında yer alan rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, proje kodları arasından seçim yapılır. İşaretlendiğinde, rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg)pasif olarak görünür. |
| Serili Stok Devri Ekranı | Stok Kısıtları **Stok Kısıtları sekmesi, devri yapılması istenen stoklarla ilgili kısıtlamaların yapıldığı sekmedir. Ekranda, stok sabit kayıtlarında girilen bilgiler listelenir. Stokların bölüm bölüm devrinin yapılmasını sağlamak için kullanılır.** |
| Saha Adı | "Stok Kısıtları" sekmesine tıklanması ile görüntülenir. Serili Stok işleminde baz alınacak saha adı için kısıt verilen alandır. İlgili hücre üzerinde iken klavyede yer alan **Boşluk Çubuğuna** basılarak aktif hale gelen aşağı ok butonu, kısıt verilmesi istenen sahalara ulaşılmasını sağlar. Satırın silinmesi için klavyedeki "Delete" tuşuna basılması gerekir. ![](../../../../../_assets/8fb117a714a706c1351f.png) |
| ![](../../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilgilerin onaylanmasını sağlayan butondur. |
| ![](../../../../../_assets/249197106fa4d90d9fe9.png) Çıkış | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |

**İşlem Sonucu**

İşlem sırasında oluşan hatalar "İşlem Sonucu" sekmesinde görüntülenerek farenin sağ tuşuna tıklanarak dosyaya kaydedilir. Gelen hataların incelenmesi gerekir.

"Yeni Yıl Kopyalama" işlemi, devir şirketi oluşturulduktan sonra, herhangi bir hatadan dolayı yarım kalabilir. İşlemin kesilmesine sebep olan problem çözüldükten sonra; yeni sene için açılan şirketi sıfırlayarak ya da, yeni sene hazırlık işlemine kalınan yerden devam etmek mümkündür.

Açılan şirketi sıfırlayarak yeni yıl kopyalama işlemine baştan başlamak için, "Şirket Silme" işlemi ile yeni şirketin silinmesi gerekir.

Kalınan yerden "Yeni Yıl Kopyalama" işlemine devam etmek için, işlem tekrar çalıştırılarak, sorgulanan sahalara daha önceden girilen bilgilerin girilmesi ve "Evet" butonuna tıklanması gerekir.

Bu durumda, kalınan yerden işleme devam etmek istenip istenmediğinin sorgulandığı bir ekran görüntülenir. “Evet” butonuna tıklanması ile yeni yıl şirketinin tekrar kopyalanmasına gerek kalmadan devir işlemine devam edilir.

İşlemler bittiğinde, modül devirleri öncesi, yeni sene kayıtlarına başlama ortamının hazırlanması işlemi tamamlanır. İstendiğinde eski senenin kayıtları bitene kadar, hiç bir modülün devri yapılmadan eski sene şirketinde ve yeni sene şirketinde ayrı ayrı çalışılarak kayıtlara devam edilebilir. Eski senenin devir kayıtları, eski sene kapatılıp devir yapıldığında yeni sene bilgilerine aktarılır. İstendiğinde modül devirleri programın içinden yapılmayıp, açılan yeni sene şirketinde elle kaydedilebilir. Bu işlemlerden biri yapılmadan yeni sene bakiyelerini doğru olarak izlemek mümkün değildir.

"Yeni Yıl Kopyalama" işlemi ile devri oluşturulan eski şirkete girerken, “Şirket devri yapılmıştır. Devir Şirketi: DEVIR. Bu şirketin sadece rapor amaçlı kullanılması tavsiye edilmektedir. Yeni yıla ait kayıtlarınızı veya düzeltme işlemlerinizi DEVIR şirketine yapabilirsiniz!” şeklinde bir uyarı mesajı görüntülenir.

Dosyaya bağlanan ve dosyası kapatılan dış ticaret belgelerinin yeni yıl şirketine aktarılmaması sağlanır.
