---
title: "Netsis Data Inspector (NDI)"
page_id: "66237083"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis Data Inspector (NDI)"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis Data Inspector (NDI)"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWQ4N2EzM2YyLTg1OGItNDQ1Mi04MDVkLWQ3OTBiZDFlMjA0OSZsaW5rPTNkNTVhNTk5LTVmMjYtNDgxZC1hNGI1LTdjODk0MDdkNTZiNiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=d87a33f2-858b-4452-805d-d790bd1e2049&link=3d55a599-5f26-481d-a4b5-7c89407d56b6&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-data-inspector-ndi_80088866_66237083.html"
source_version: "2022-11-02T15:36:33.803+03:00"
source_bytes: 3022351
fetched_at: "2026-09-13T04:24:39+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis Data Inspector (NDI)

Netsis Data Inspector (NDI) ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

> [!NOTE]
> İlgili özelliğin anlatımını içeren webinar kaydına ulaşmak için [tıklayınız.](https://register.gotowebinar.com/recording/3096728733633956367)

NDI (Netsis Data Inspector) paketi ile, Netsis'in standart ekranları dışında ihtiyaç duyulabilecek uygulamaların tasarlanarak kullanılması ve raporlanması sağlanmaktadır. NDI paketi; Netsis 3 Standart, Netsis 3 Enterprise, Netsis Wings ve Netsis Wings Enterprise ürünü ile kullanılabilmektedir.

Giriş

NDI uygulamasında kullanılacak ekran, rehber ve raporların tasarımları NDI ortamından yapılmakta, kullanımı ise ister NDI ortamından ister Netsis Temelset veya Netsis Bordro içerisindeki herhangi bir modülden yapılabilmektedir. NDI uygulaması çalıştırıldığında, bağlanılacak şirket, kullanıcı isim ve şifre bilgileri sorgulanacaktır. Eğer ilgili kullanıcı SSO'da bir domain kullanıcısına bağlanmış ise giriş ekranında diğer Netsis paketlerindeki olduğu gibi otomatik olarak getirilecektir.

![](../_assets/b6d47ba185a3311af0e6.png)

NDI kurulumu sırasında, NDI uygulamalarının tasarımı ile ilgili verilerin saklanacağı bir şirket varsayılan olarak açılacaktır. NDI uygulamasında farklı tasarım bilgilerini saklamak amacıyla birden fazla NDI şirketleri açılabilir.

NDI'da kullanılacak olan verilerin mutlaka NDI şirketinde bulunması zorunlu değildir, farklı bir veritabanına bağlanılarak veriler buradan da kullanılabilmektedir. NDI uygulamasını kullanacak olan kullanıcıları Merkezi Kimlik Yönetimi ekranında, yetkili uygulamalar bölümünden NDI satırında Yetki Ver butonu ile belirleyebiliriz.

![](../_assets/401ec202099598270caf.png)

Kullanıcı bu şekilde yetkilendirildikten sonra Kullanıcı Hakları menüsü kullanılarak NDI'da ilgili kullanıcının hakkı olan ekranlar belirlenebilir.

![](../_assets/77150dfd1083add15108.png)

NDI aracılığıyla veri giriş ekranlarının tasarlanabilmesi için öncelikle çalışılacak tabloların veritabanı üzerinde yaratılmış olması gerekir. Tablolar kullanım amaçlarına göre istenilen bir veri tabanı içinde yaratılabilir; örneğin bu tablolar Temelset için açılan şirketlerin veritabanlarında olabileceği gibi, NDI için yaratılan veritabanında ya da tamamen farklı bir veritabanında bulunabilirler.

#### NDI Modülü

NDI uygulamasının ana ekranının menü çubuğundaki Genel seçeneği altında bulunan NDI seçeneği, NDI modülüne girişi sağlar.

#### Dizayn Hazırlama

![](../_assets/9f128cacd5e65cf7693d.png)

Dizayn Hazırlama seçeneği ile, NDI aracılığıyla hazırlanan tüm ekran dizaynlarının topluca izlenebileceği pencere açılacaktır. Burada dizaynların ana bilgilerini yönetebilir ve seçili dizaynla ilgili olarak dizayn ortamına geçebilirsiniz.

Dizayn hazırlama ekranında yer alan alanlar aşağıda detaylandırılmıştır:

- Kod alanında, NDI aracılığıyla yapılan her dizayn için tekrarsız bir kod verme zorunluluğu bulunmaktadır. Kendi sistematiğinize göre burada kodlamanızı yapabilirsiniz.
- Başlık alanı, dizayn başlığı bilgisidir. Bu bilgi tasarlanan ekranın kullanımı sırasında açılan ekranın başlığı olacaktır.
- Veritabanı İlişkili alanı, tasarlanacak olan NDI ekranı eğer veritabanı ile ilişkilendirilerek veritabanı bağlantısının otomatik oluşturulması ve tasarım aşamasında veritabanı bağlantılı alanların görünmesi isteniyorsa işaretlenmesi gereken bir alandır.
- Tarih alanı, dizaynın yapıldığı ilk tarih bilgisi olarak saklanabilecek alandır. Kullanıcı bu alana istediği bir tarih bilgisi girebilir.
- Tablo Adı alanı, veritabanı ilişkili seçeneği işaretlendiğinde aktif olan bir alandır. Dizayn ekranında veritabanı bağlantılı olarak kullanılan bileşenlerin verileri kaynak olarak getireceği tablo bilgisidir. Tablonun dizayn öncesinde, veritabanında SQL komutları yardımıyla yaratılmış olması gerekmektedir. NDI, tablo yaratma işlevini içermez.
- Veritabanı Kodu alanı, veritabanı ilişkili seçeneği işaretlendiğinde aktif olan bir alandır. Dizayn ekranında veritabanı bağlantılı olarak kullanılan bileşenlerin, verileri hangi veritabanından getireceği bilgisidir. Bu bağlantı tanımlamaları Veritabanı Bağlantı Tanımlama ekranında yapılacaktır. Bu sahada Veritabanı Bağlantı Tanımlama ekranında yapılmış olan ve bu NDI dizaynında kullanılacak olan veritabanı kodu girilecektir.
- Grup Kodu alanında, hazırlanan dizaynların gruplanması isteniyorsa ilgili dizaynın içinde yer alacağı grubu belirtebilirsiniz. Kendi sistematiğinize göre gruplandırmayı yapabilirsiniz. Herhangi bir grup kodu verilmezse, ilgili dizayn GENELDIZAYN grubu altına alacaktır.
- Ortam alanında, sabit olarak D-Win32 değeri gelmektedir. Bu seçenek dizaynın windows ortamında çalışacağını belirtmektedir.
- Form Tipi seçeneği, tasarlanan formun N-Normal ya da C-Child olduğunun belirleneceği seçenektir. Normal formlar açıldıkları pencereden bağımsız olup yeni bir ekran şeklinde düşünülebilir. Child formlar ise açıldıkları pencere içinde çalışırlar.
- Sıra No alanında, dizaynın menüde kaçıncı sırada yer alacağı bilgisi tanımlanacaktır.
- Aktif alanında, dizaynın aktif veya pasif olduğu bilgisi belirlenecektir.
- Dizayn Görüntüleme seçeneği, seçilmiş olan dizaynın görüntülenmesini sağlayan bir seçenektir.
- Dizayn Ortamı butonu, dizaynı hazırlamak için dizayn ortamına geçmemizi sağlayan butondur.

#### Dizayn Ortamı

![](../_assets/a9f187368f3b96b43851.png)

NDI Dizayn Ortamı; Netsis Araç Çubuğu, Netsis Object Inspector, Tasarım Ekranı ve VCL Palette bölümlerinden oluşmaktadır. NDI Dizayn Ortamında, tasarımın kendisi (form, ekranın ortasında) ve yardımcı araçlar olarak VCL (Visual Component Library – Görsel Bileşen Kütüphanesi, ekranın sağ tarafında) ve Object Inspector (Nesne Denetçisi, ekranın sol tarafında) bulunmaktadır. Form üzerine yerleştirilecek bileşenler, görsel bileşen kütüphanesinden seçilir ve formun istenilen yerine yerleştirilir. Bileşenin seçimi için, VCL penceresine geçip istenen bileşen tıklanmalıdır. İstenen bileşen seçili iken form üzerine gelip tıklandığında, bileşenin bir kopyası form üzerinde belirecektir. Form üzerinde beliren bileşen fare ile sürükle bırak işlemi ile yerleştirilebilir. Bileşen boyutları istenen şekilde fare ile ayarlanabilir. Bileşen form üzerine yerleştirildikten sonra ve seçili iken, nesne denetçisi penceresine geçip, özellikleri belirlenebilir.

#### Dizayn Ortamı Araç Çubukları

![](../_assets/6f90b7584071962d290e.png)

NDI dizayn ortamında yer alan araç çubukları sırasıyla aşağıdaki gibidir:

- Kes, Kopyala, Yapıştır, Geri Al butonları, Windows uygulamalarındaki standart kullanım şekli ile aynıdır.
- Object Inspector butonu, Object Inspector penceresine geçişi ve seçili olmasını sağlar.
- Tasarım butonu, Tasarım penceresine geçişi ve seçili olmasını sağlar.
- VCL Palette butonu, VCL (Visual Component Library) penceresine geçişi ve seçili olmasını sağlar.
- Master Field Göster butonu, anahtar alan seçimi penceresini açar. Anahtar alan seçimi işlemi tasarım işleminde anlatılacaktır.
- Ön Değer Göster butonu, varsayılan (Ön değer) Değer tanımlama penceresini açar. Varsayılan Değer tanımları tasarım işleminde anlatılacaktır.
- Dizayn Kaydet butonu, yapılan değişiklikleri kaydetmeye yarar. F2 kısayol tuşu da aynı işleve sahiptir.

#### VCL (Visual Component Library – Görsel Bileşen Kütüphanesi)

![](../_assets/2292183a17d1023490ae.png)

NDI uygulamasında, bir form üzerine yerleştirilebilecek mevcut bileşenleri içeren araçtır. Form üzerindeyken VCL'e geçiş fare yardımıyla ya da F10 kısa yol tuşuyla yapılabilir. VCL Palette üzerinde Standart, İleri, Veritabanı Kontrol ve Web grupları bulunmaktadır. Kullanılabilecek bileşenler bu grupların altında yer almaktadır.

#### Standart Bileşenler

Standart bölümünde yer alan bileşenler, veritabanından bağımsızdır ve temel bileşenleri içermektedir.

TLabel bileşenini ekranda bilgi amacıyla yazmak istediğiniz her şey için kullanabilirsiniz. Çoğunlukla saha başlıkları için kullanılır. Bunun dışında herhangi bir yerde bilgi vermek amacıyla da kullanılabilir. Bilgi girişi amacıyla kullanılmaz

TButton bileşeni ekrana buton koyabilmek amacıyla kullanılır. Buton tıklandığında uygulamanın bir işlem yapılması beklenmektedir aksi halde buton koymanın bir anlamı olmayacaktır. Buton basıldığında yapılması istenen işlemler script girişi aracılığıyla yapılabilir.

TNetEdit bileşeni, uzunluğu belli olan sayısal ya da alfabetik bilgilerin ekrandan sorgulanabilmesi için kullanılır.

TMemo bileşeni, TNetEdit'e benzemektedir. TNetEdit'den farkı, bu alan uzun metin girişi için kullanılabilecek bileşendir.

TPanel bileşeni, panel içerisinde başka bileşenleri de barındırabilen bir bileşendir. Form üzerine bir veya birden fazla panel, bileşenlerin gruplanması amacıyla yerleştirilebilir.

TNDIRehberBtn bileşeni, rehber bileşenini form üzerine yerleştirmek için kullanılır. Rehber tuşuna bağlanacak rehber için tanım ayrıca yapılmalıdır.

TGroupBox bileşeni, Form'da alt bileşenleri belirli bir gruba yerleştirmek için bir kapsayıcı olarak kullanılır. Kullanım amacı bileşenleri bir grup altında toplayarak kategorilere ayırmaktır.

TCombobox bileşeni, Combobox kontrolü açılır listeler hazırlamak için kullanılmaktadır.

TCheckBox bileşeni, Checkbox bileşeni kullanıcıya seçenekler sunarak bunlardan birini, birkaçını ya da tamamını seçebilmesi istenen durumlar için kullanılır.

TRadioGroup bileşeni, RadioGroup bileşeni kullanıcıya seçenekler sunarak bunlardan sadece birinin seçebilmesi için kullanılır. Items özelliği altına eklenen her bir satır, radiogroup içerisinde bir seçenek ekleyecektir.

TListBox bileşeni, metin türündeki verilerin alt alta liste şeklinde sıralanmasını sağlayan bileşendir.

#### İleri Bileşenler

TPageControl bileşeni, form üzerindeki bilgilerin tek pencereye sığmaması halinde, gruplanarak birden fazla sayfa üzerinde dizayn edilebilmesi için kullanılır. İçerisinde en az bir sayfa olması gerekmektedir, her eklenen sayfaya farklı farklı bileşenler eklenebilir. Sayfa ekleme işlemi, bileşen üzerinde sağ tık menüsü ile gelen menüde Özel İşlemler/Yeni Sayfa seçilerek yapılmaktadır. Benzer şekilde önceki veya sonraki sayfaya geçme işlemi de bileşen üzerinde sağ tık menüsü ile gelen menüde Özel İşlemler/Önceki Sayfa veya Sonraki Sayfa menüsü ile yapılmaktadır.

TScrollBox bileşeni, panel ile aynı işlevi görmek üzere ekrana yerleştirilebilir. Panelin içine sığmayacak kadar çok bilgi yerleştirilecek ise, scrollbox tercih edilebilir. Bu kutucuğun içinde yukarı, aşağı, sola, sağa scroll (kaydırma) edilerek daha fazla bilgi yerleştirilebilir.

TBevel bileşeni, formun üzerinde çizgi çekmek, kutu benzeri görüntüleri oluşturabilmek için kullanılır. Bevel, boyutları değiştirilerek istenilen şekle getirilerek formun istenen yerlerine yerleştirilebilir.

TNDIPicture bileşeni, form üzerine bir resim koyabilmek için kullanılır.

TAnimate bileşeni, video klip vb. bir animasyonun form üzerinde gösterilmesi için kullanılır.

TNDIRecStatMonitor bileşeni, kullanımda son yapılan veri tabanı işlemi sonucu kalınan durum ve ekrandaki kayıt kümesi bilgisinin detaylı olarak izlenebilmesine yarayan bileşendir.

TNDIBitBtn bileşeni, ekran üzerine eklenecek bileşenin ResimDosya özelliğine değer atanarak bileşenin üzerinde seçilen BMP dosyasının görüntülenmesi sağlanabilir. Ayrıca bileşen üzerinde görüntülenen resme ek olarak Caption özelliğine atanan değer de metin olarak bileşen üzerinde görüntülenebilmektedir. Bileşenin Layout özelliğine atanacak blGlyphRight, blGlyphBottom, blGlyphLeft ve blGlyphRight özelliklerine göre resmin yazının neresinde gösterileceği seçilecektir. Örneğin blGlyphLeft seçildiğinde resim yazının solunda görüntülenecektir.

TNDIPaintBox bileşeni, Dinamik Kodlama özelliği ile TNDIPaintBox nesneleri üzerinde grafiksel değişiklikler yapmak için "Canvas" özelliği kullanılabilir.

TGauge bileşeninde bu kontrol sayesinde gerçekleşen işleminizi yüzdelik olarak kullanıcıya gösterebilirsiniz. MinValue ve MaxValue değerleri ayarlanarak bileşende kullanılacak alt ve üst sınır değerleri belirlenebilir. Ayrıca bileşenin Kind özelliği sayesinde gösterimin şekli de kullanıcı tarafından belirlenebilmektedir. gkHorizontalBar (Yatay Bar Şeklinde), gkVerticalBar (Düşey Bar Şeklinde), gkNeedle (Yarım Elips Şeklinde), gkPie (Daire Şeklinde) ve gkText (Sadece Yazı Şeklinde) değerlerinden biri seçilebilir. Atanacak Progress özelliği ile bileşene bir başlangıç değeri atanabilir, bu değer MinValue ve MaxValue değerleri arasında olmalıdır. Bileşenin bir progress bar gibi çalışmasını sağlamak için form üzerine bir Timer nesnesi ekleyip Progress özelliğinin belirli zaman aralıklarıda değiştirilmesi sağlanabilir.

TNDITimer bileşeni ile bir kod bloğunun belli bir zaman aralığında tekrar tekrar çalıştırılması sağlanabilir. Bunun için bileşenin OnTimer olayına dinamik kodlama ile kodlama yapılması gerekmektedir. OnTimer olayına yazılan kodun birden çok kez işletilmesi için beklemesi gereken süre bu değerde tutulur. Bileşenin Interval özelliğine girilen değer milisaniye cinsindendir. Yani buraya "1000" girilmesi bir saniye beklemesi gerektiği anlamını taşımaktadır.

TNDIXGrid bileşeni ile belirlenen bir sorgu sonucunda dönen verilerin grid ekran üzerinde gösterilmesi sağlanabilir. Gridin GridSql özelliğine kullanılmak istenen sorgu yazılmalı ve DbConnection özelliğine de bağlantı sağlanacak veritabanına ait daha önceden tanımlanmış olan bağlantı kodu seçilmelidir. Sonrasında StrColumns özelliği ile sorgu sonucunda gelen alanların hangilerinin grid üzerinde gösterileceği tek tek belirlenmelidir.

![](../_assets/6e8a9ac4b39526148569.png)

StrColumns ile gösterilecek kolonlar belirlenirken çıkan ekranda sorgulanan alanların detayarı şöyledir;

Alan bölümünde, tablodaki hangi alanın görüntülenmesini istediğiniz. Sağındaki ok tuşu ile sahaların listesini açabilir ve içinden bir tanesini seçebilirsiniz.

Başlık alanından seçilen alanın grid üzerinde görüntülenecek olan başlık bilgisidir.

Giriş Maske alanında sütunda yer alacak bilgilerin belli bir maske ile görüntülenmesi isteniyorsa, maske bilgisi girilebilir.

Genişlik alanı sütun genişliğinin pixel cinsinden değeridir.

Hizalama seçeneği; bilgilerin sola dayalı, sağa dayalı ya da ortalanmış görüntüleneceğine dair seçenektir.

NDS Tip alanı, Netsis'in diğer paketlerinden birinin içinden çalıştırıldığı durumda geçerli özellik olup, paket içindeki NDS (Netsis Decimal System) tanımlarından hangisinin sütun için geçerli olduğunun belirlendiği sahadır.

Kolon Max Genişlik seçeneği, sütunun içerdiği bilgilerin en genişi kadar dinamik genişlik alması için işaretlenmeli, işaretlenmediği durumda, genişlik olarak belirlenen değer geçerli olacaktır.

Yazı Renk butonu sütunun görünecek renginin belirlenebileceği butondur.

Yazı Tipi butonu sütundaki bilgilerin yazı tipi (font) ayarının yapılabileceği butondur.

Seçilen kolonların sayısına göre ColCount özelliğinin de ayarlanması gerekecektir, grid üzerinde burada belirlenen sayıda kolon gösterilecektir.

TDateTimePicker bileşeni, görüntüsel olarak ComboBox kontrolüne benzeyen, çalışma zamanında içerisinden gerekli tarihi seçmenize imkan sağlayan kullanışlı bir bileşendir. Kind özelliği ile bileşende tarih mi yoksa saat bilgisinin mi gösterileceği seçilebilir. dtkTime değeri seçildiğinde zamanı, dtkDate değeri seçildiğinde ise tarihi gösterecektir.

TNDICheckListBox bileşeni, Listbox bileşenine benzemektedir fakat burada listeye eklenen her satırda bir checkbox bulunmaktadır ve istenen satırların böylelikle işaretlenmesi sağlanmaktadır. Listede bulunacak satırlar Items özelliği altında tanımlanabilir. Dİnamik kodlama kullanarak işaretli olan satır bilgileri elde edilebileceği gibi, yine dinamik kodlama ile istenen satırların işaretlenmesi, yeni satır eklenmesi veya satırdaki işeretin kaldırılması da sağlanabilmektedir.

TNDITreeView bileşeni, ağaç yapısı işlemleri için kullanılan bileşendir. Windows içerisinde bir çok yerde bu bileşene rastlayabiliriz. Dİnamik kodlama kullanarak bileşen üzerindeki ağaç yapısı gezilebilir.

#### Veritabanı Kontrol Bileşenler

TDBNedit: Tablodaki uzunluğu belli olan alfa nümerik tüm sahaların ekrandan sorgulanması ve gösterilmesi için kullanılır.

TDBNumber: Tablodaki nümerik sahaların ekrandan sorgulanması ve gösterilmesi için kullanılır.

TDBDateTime: Tablodaki tarih alanlarını, kullanıcıya takvim yardımıyla seçtirtebilmek için kullanılan bileşendir.

TNetCombobox: Birden fazla seçenekten birinin seçilebileceği saha tiplerinde tercih edilmesi gereken bileşendir. Örneğin cari hareket tipleri, A-Devir, B-Fatura, C-İade fatura, D-Kasa vb. Değerler alabilmektedir. Sahanın alabileceği değerler listede gösterilerek kullanıcının bu değerlerden birini seçmesi sağlanır.

TDBMemo: Tabloda uzun metin olarak tanımlanan sahaların sorgulanması için kullanılabilecek ekran bileşenidir. Tabloda Text ve Blob tanımlı alanlar için geçerlidir.

TDBCheckBox: Tablodaki ilgili saha evet/hayır gibi iki değerden birini alabiliyorsa, tercih edilecek bileşendir.

TDbOpButton: Tablodaki kayıtlara erişimin (ilk kayıt, son kayıt, önceki, sonraki vb.) görsel butonlar aracılığıyla yapılması isteniyorsa, her bir veri tabanı işlemi için forma bir buton konabilir. Her biri bir butona bağlanmak kaydıyla, ilk/son kayıt, önceki/sonraki kayıt, yeni kayıt, kayıt sil, kayıt sakla, benzer arama ve kesin arama fonksiyonlarını içeren bir veri tabanı gezgini tasarlanabilir. Butonlar, ekranın

bağlantılı olduğu tablodaki kayıtlar arasında dolaşabilmek, yeni kayıt girme ortamına geçmek, ekranda

bulunan kaydı silmek amacıyla kullanılır.

TNetsisGrid: Ekrandaki kayıt kümesinin, belli sahalarının içeriklerinin satır satır grid (ızgara) içinde gösterilmesi için kullanılabilir. Grid bileşeni eklendikten sonra, tablodaki hangi sahaların, gridin hangi sütunlarında gösterilmesi istendiği strcolumns özelliği kullanılarak belirlenecektir.

TNDIBlob: Uzun metin, doküman, resim, clip, müzik vb. blob (binary large objects) saklamak için kullanılır. Tablodaki Image, Blob sahalarına karşılık kullanılan bileşendir. Bileşen, tablodaki tek blob sahaya eşlenmesine rağmen, kullanıcının birden fazla nesnenin saklayabilmesine olanak tanır.

TDBRadioGroup: CheckBox kontrolü ile aynı mantıkta işlem yapar. Tek farkı RadioGroup içerisinden sadece bir seçenek işaretlenebilmektedir. Bu bileşenin DataField özelliğine hangi alandaki değerlerin kullanılacağı seçilecektir. Items özelliğinde ise seçilen alanda yer alan değerlerin kullanıcıya hangi isimlerde gösterileceği tüm olası seçenekler için satır satır girilecektir. Values özelliğinde ise Items altında tanımlanan ve kullanıcıya gösterilen değerlerin veritabanındaki ilgili alanda hangi değerler ile tutulduğu bilgisi satır satır girilecektir. Burada Items özelliğinde yazılan değerler ile Values alanındaki değerlerin eşit sırada girilmesi önem taşımaktadır. Örneğin DataField olarak CARI_TIP seçilmiş ise Items olarak Alıcı, Satıcı değerleri satırlara girilebilir, Values olarak da sırasıyla A ve S satırlarının girilmesi gerekmektedir.

TNDINetsisCxGrid: TNetsisGrid ile aynı amaca hizmet eden bir bileşendir. Fakat bazı farklı özellikleri bulunmaktadır. Bu gridin de ColCount özelliği ile gösterilecek kolon sayısı belirlenebilir. GridSql özelliği ile verileri getireceği sorgu atanabilir, DbConnection ile bağlantı kuracağı veritabanı seçilebilir. NetColumns özelliği ile kullanılacak olan kolonların tek tek tanımlanması gerekmektedir.

![](../_assets/c4da9621b623bca46613.png)

Burada diğer grid bileşeninden farklı olarak Kontrol Bileşeni ve Değiştirilebilir alanları bulunmaktadır. Kontrol Bileşeni olarak form üzerinde yer alan TDBNEdit tipindeki alanlar getirilmektedir, yani gridin bu alanında seçilen değer form üzerindeki ilgili alana bağlanmış olmaktadır. Grid üzerinden bir satır seçildiğinde ilgili satır ve kolondaki değer bu seçilen alanda gösterilmektedir.

Ayrıca bu grid üzerinden istendiğinde veri girişi de yapılabilmektedir, bu özelliğin kullanılabilmesi için grid üzerinde kullanılacak olan kolonlar belirlenirken "Değiştirilebilir" seçeneğinin ilgili kolon için işaretlenmesi gerekmektedir.

Bu gridin diğer gridlerden en büyük farkı ise kolonlar üzerinde sıralama ve filtreleme işlemlerinin kullancı tarafından anlık olarak yapılabilmesidir.

Son olarak bu gridin özelikleri arasında yer alan UseSelectionCol özelliği ile istendiğinde satırların en soluna otomatik olarak seçim kolonu eklenebilmektedir.

Ayrıca dinamik kodlama kullanılarak seçimi gerçekleştirilen satır değerleri; grid üzerinde yapılan çoklu seçimler, değiştirilen hücrenin kolon ve satır indeksleri alınabileceği gibi istendiğinde istenen bir satırın seçilmesi veya seçili bir satırın kaldırılması da sağlanabilir.

#### Web Bileşenler

TNetWebBrowser: NDI dizaynı üzerine bir web tarayıcı eklenmek isteniyorsa bu bileşen kullanılmaktadır.

THTMLEditor: Bu bileşen ile temel HTML biçimlendirme işlemlerini NDI formu üzerinden gerçekleştirebilirsiniz. HTML veya tasarım modları arasında geçiş yapılabilir. Bu bileşenin kullanılabilmesi için Microsoft'un DHTML Editing Control uygulamasının [{+}](https://www.microsoft.com/en-us/download/details.aspx?id=8956)[https://www.microsoft.com/en-us/download/details.aspx?id=8956+](https://www.microsoft.com/en-us/download/details.aspx?id=8956+) linki üzerinden kurulması gerekmektedir.

![](../_assets/8869793cb728e3d509f0.png)

#### Object Inspector (Nesne Denetçisi)

![](../_assets/facc3423b75ecd255874.png)

VCL'den seçilerek form üzerine yerleştirilmiş olan nesnelerin birtakım özelliklerini belirlemek için kullanılan araçtır. Form üzerinde nesne (bileşen) seçili olduğu durumda, fare yardımıyla ya da F11 kısa yol tuşuyla object inspector'a geçilebilir.

Object Inspector üst bölümünde, seçili nesnenin ismi görülmektedir. Bu kutucukta sağdaki ok tuşuna basıldığında, tüm nesne isimleri görülebilir. Açılan listeden başka bir nesne seçip, seçilen yeni nesne ile ilgili düzenleme yapmak mümkündür. Nesne listesinin altında ise, seçili nesneye ait özellikler yer almaktadır. Sol tarafta özelliğin ismi, sağ tarafta ise, özelliğin mevcut değerleri görünür. Her bir özelliğin sağındaki bu kutucuklara fare ile gelinip, özellik değeri değiştirilebilir. Birçok özellik kendine göre belli değerler alabilmektedir. Bu tür özelliklerde fare ile üzerinde gelindiğinde ya aşağı doğru ok ya da üç nokta işareti belirmektedir. Forma VCL'den seçilerek eklenen her bileşen belli varsayılan özellikleriyle birlikte eklenmektedir.

![](../_assets/a4d88fc3af2ff43a7c8c.png) ![](../_assets/355ad0f7d4180d5adfe9.png)

Object Inspector bölümünde nesnelere ait olan ve kullanıcılar tarafından değiştirilebilen bazı önemli özellikleri aşağıda yer almaktadır.

Name: Form üzerine VCL'den seçilerek eklenen bileşenlerin (nesne), varsayılan bir özelliği de isimleridir. NDI, eklenen her bileşenin ismini, VCL'deki isminin yanına artan sıra numarası vererek oluşturur ve bileşene atar. Sonradan kullanıcı tarafından bu atanan isimler kendi isimlendirme mantığına göre değiştirilebilir. Burada önemli nokta, form içerisinde aynı isimli sadece bir tane bileşenin bulunabileceğidir. İsimlendirme yapılırken boşluk karakteri ve Türkçe karakter kullanılmaması gerekmektedir. Sadece form bileşeni için Name özelliği değiştirilememektedir.

Active: TNDIXGrid, TNetsisGrid ve TAnimate bileşenlerinde geçerlidir. Animasyon bileşeninde, animasyona ait dosya ismi belirtildikten sonra, kullanım anında animasyonun çalışması için True yapılmalıdır, False kaldığı durumda animasyon bileşeni kullanım anında hareket etmeyecektir.

Align: Panel, grid, page control gibi form içinde belli bir bölgeye yerleşen bileşenler için geçerli olup, alBottom, alClient, alCustom, alLeft, alNone, alRight, alTop seçenekleri vardır. Seçenekler, formdaki yerleşim yerini ve şeklini belirler.

Alignment: Bilgi giriş sahası, etiket gibi bileşenlerin içindeki metnin sağa, sola yanaşık ya da ortalanmış görünmesini sağlar. taCenter, taRightJustify, taLeftJustify seçenekleri vardır.

Autosize: Bileşenin uzunluğunun içerdiği bilgi kadar olmasını sağlar. Sadece etiket bileşeninde, yazılan başlık uzunluğunda olması için True olması önerilir. Diğer bileşenlerde ise tasarım sırasında belirlenen uzunluğun korunması için False olmalıdır.

BevelEdges, BevelInner, BevelKind, BevelOuter, BevelWidth, BorderStyle: Bileşeni çevreleyen kutucuğun görünümü ile ilgili tanımlardır.

Caption: Bileşenin form üzerinde görünen başlığıdır. Kullanıcıya görünmesini istendiği şekliyle başlık bilgisi yazılmalıdır. Bu özellik name (isim) özelliği ile karıştırılmamalıdır. Başlık özelliğinde Türkçe vb. istenen karakterler kullanılabilir.

CharCase: Bileşenin veri girişi sırasında büyük, küçük harfle ya da girildiği şekliyle alınmasını sağlayan özelliktir. ecLowerCase, ecUpperCase, ecNormal seçenekleri mevcuttur.

Color: Bileşenin görünen rengini değiştirmek için kullanılır. İstenen renk, açılan color palette vasıtasıyla

belirlenebilir.

ColCount: Grid bileşeninin toplam kolon sayısıdır.

ColMaxWidth: Grid bileşeninin kolonları tanımlanırken, ilgili kolonun genişliğinin, içerdiği bilginin en uzun olanına göre dinamik olarak ayarlanmasını sağlayan özelliktir. Bu özelliğin seçilmemiş olma durumunda grid kolonu genişliği tasarım sırasında belirtilen değerde sabitlenecektir.

Cursor: Kullanım sırasında bileşenin üzerine gelindiğinde cursor tipinin değişmesini sağlar. Standart tip için sıfır bırakılmalıdır.

DataField: Veri tabanı bileşenleri için geçerli olup, tablodaki ilişkili sahanın belirleneceği özelliktir. Özelliğin yanındaki üç nokta ile, bağlantılı tablodaki alanlar listelenerek içinden istenen saha seçilebilir.

DbOperation: DBOperasyon buton bileşeninin veri tabanı gezgini işlevlerini içeren özelliğidir. doFirst, doLast, doPrior, doNext, doPost, doDelete, doInsert, doLikeSearch, doExactSearch değerlerini alabilir. Veri tabanı bileşenleri bölümünde anlatıldığı gibi her bir işlev için forma birer buton eklenirse tam bir gezgin elde edilebilir. Seçeneklerin işlevleri de detaylı olarak Veri Tabanı Bileşenleri/ Db Operasyon bölümünde anlatılmıştır.

Decimal: Nümerik sahalar için ondalık bölümünün basamak sayısı belirlenmelidir.

EditMask: Kullanım sırasında sahaya girilebilecek bilginin belli bir formatta girilmesini zorlamak için

verilebilecek maskesidir.

Enabled: Ekran üzerinde genelde bilgi amaçlı olup veri girişi amacıyla kullanılmayan sahalar, kullanıcının müdahale etmemesi için Enabled özelliği False olur. Kullanıcının müdahale edebileceği sahaların ise Enabled özellikleri True olmak zorundadır. Enabled özelliği False olan bileşenlerin renkleri de değiştirilerek ekranda farklı görünmeleri sağlanabilir. Örneğin stok kodu yazıldığında, stok sabit bilgilerinden isim bulunup ekranda görüntülenecekse, stok ismi bileşeninin Enabled False olacaktır.

FileName: Animasyon bileşeni için eklenecek video dosya isminin belirlenmesine yarar.

Font: Bileşenin içerdiği bilginin yazı karakterini belirlemeye yarar.

Height: Bileşenin piksel cinsinden yüksekliğini belirlemek içindir.

ItemIndex: Combobox bileşeni için varsayılan olarak hangi değerin seçili olarak gelmesi istendiğinin belirlenebileceği özelliktir. Varsayılan değerin listedeki sıra numarası belirtilmelidir. Listedeki ilk değer sıfırdan başlayarak numaralandırılır.

Items: Combobox bileşeni için listedeki seçeneklerin belirleneceği özelliktir. Bu özelliğin sağındaki üç noktaya tıklanarak açılan pencerede, Combobox listesinde yer alması istenen seçenekler girilebilir. Açılan pencerede her seçenek bir satır halinde girilmelidir. Örneğin cari hareket tipi seçenekleri her biri bir satıra olmak üzere, "A-Devir", "B-Fatura", "C-İade Fatura" ... şeklinde girilmelidir.

Left: Bileşenin, form üzerinde, panel ya da page control içindeki yerleşiminin sol kenardan piksel

cinsinden uzaklığıdır.

LUCustEditAck: Rehber bileşeni için, döndürülmek istenen ikinci bilgi sahasının belirleneceği özelliktir. Örneğin kod ve isim sahalarından oluşan bir rehberimiz bulunduğunu ve form üzerine yerleştirdiğimiz kod ve isim sahalarına rehberden bilgi döndürmek istediğimizi düşünelim. Bu özelliğin sağ tarafındaki üç nokta tıklandığında, form üzerine yerleştirilmiş olan ve bilgi döndürülebilecek tüm sahalar görüntülenecektir. Sahaların içinden isim döndürmek istediğimiz sahayı belirleyebiliriz.

LUCustomEdit: Rehber bileşeni için, döndürülmek istenen ana bilgi sahasının belirleneceği özelliktir. Örneğin kod ve isim sahalarından oluşan bir rehberimiz bulunduğunu ve form üzerine yerleştirdiğimiz kod sahasına rehberden seçilen kodun döndürülmesini istediğimizi düşünelim. Bu özelliğin sağ tarafındaki üç nokta tıklandığında, form üzerine yerleştirilmiş olan ve bilgi döndürülebilecek tüm sahalar görüntülenecektir. Sahaların içinden kod döndürmek istediğimiz sahayı belirleyebiliriz.

MaxLength: Bileşene kullanım sırasında girilecek bilginin maksimum uzunluğunu belirlemek içindir. Kullanıcı belirlenen uzunluktan fazla sayıda karakter giremeyecektir.

NDSType: Tasarlanan formun, Netsis'in diğer paketlerinden birinin içinden çalıştırıldığı durumda geçerli özellik olup, paket içindeki NDS (Netsis Decimal System) tanımlarından hangisinin bileşen için geçerli olduğunun belirlendiği özelliktir.

OddRowColor: Grid üzerinde satırların ayrı renklerde gösterilerek kullanıcıya görsel ayrıştırma kolaylığı sağlanmak isteniyorsa, satırların biri beyaz zeminde gösterilmek üzere diğerinin zemin rengi bu özellikle belirlenebilmektedir. Kullanımda grid, bir satırı beyaz, bir satırı belirlenen renkte olmak üzere görünecektir.

PageIndex: Page Control bileşeninin seçili sayfasının sıra numarasıdır. İlk sayfa 0, ikinci sayfa 1 ...

şeklinde numaralandırılmıştır. Sayfalar arasında kaydırma yapmak için, örneğin ikinci sayfayı ilk sayfa

olarak değiştirmek için, bu özellik sıra numarası değiştirilebilir. Özellik için değer tanımlandığında, seçili sayfa belirlenen yere taşınacak, diğer sayfalar ise kaydırılarak yer değiştirecektir.

ReadOnly: Bileşenin salt okunur özellikte olmasını sağlar.

RehberKodu: Rehber bileşeni için, kullanılacak olan rehberin kodunun girileceği özelliktir. Rehberler, NDI Modülünde Rehber Tanımlama bölümünde hazırlanmakta ve tasarımda kodu belirlenerek kullanılabilmektedir. (Bkz: Rehber Tanımlama)

ResimDosya: Resim bileşeni için kullanılacak resmin bulunduğu dosyanın belirleneceği özelliktir. Özelliğin sağındaki üç nokta ile diyalog açılarak dosya yeri belirlenebilir.

RtrnFldIndex: Rehber bileşeni için, döndürülmek istenen ikinci bilgi sahasının, rehberdeki kaçıncı saha olduğunun belirleneceği özelliktir. Rehber tanımlamada rehberde yer alması istenen sahalar tanımlanabilmektedir. Rehber kullanım sırasında, kullanıcı kaydı bulabilmek için bu sahaların içerdiği bilgilerden arama yapabilmekte, kaydı bulduğunda ise, bir bilgi sahasını, örneğin kodu, geri döndürebilmektedir. Rehberin içinde bulunan ikinci bir bilgi sahasının, örneğin isim bilgisinin, form üzerinde bir bileşene döndürülmesi isteniyorsa, bu özellikte, isim sahasının rehberdeki sıra numarası belirtilmelidir. İsim sahasında yer alan bilginin, form üzerindeki hangi bileşene döndürüleceği ise, LUCustEditAck özelliğinde belirtilir.

ScrollBars: Uzun metin girişi yapılabilen Memo ve DBMemo bileşenlerinde, yukarı/aşağı ve soldan sağa kaydırma çubuklarının bileşenin içinde yer alıp almaması ile ilgili özelliktir. ssNone (kaydırma çubuğu yok), ssBoth (hem yukarı/aşağı hem de sol/sağ kaydırma çubukları var), ssHorizontal (sadece sol/sağ kaydırma çubuğu var), ssVertical (sadece yukarı/aşağı kaydırma çubuğu var) seçenekleri bulunmaktadır.

StrColumns: Grid içinde yer almasını istediğiniz bilgilerin, yani grid sütun tanımlarının yapıldığı özelliktir. Özelliği sağındaki üç nokta tıklandığında karşınıza aşağıdaki ekran gelecektir. Bu ekranda grid sütunlarını arka arkaya tanımlayabilirsiniz.

Alan; Tablodaki hangi alanın görüntülenmesini istediğiniz. Sağındaki ok tuşu ile sahaların listesini açabilir ve içinden bir tanesini seçebilirsiniz.

Başlık; Sütunun grid üzerinde görüntülenecek olan başlığıdır.

Giriş Maske; Sütunda yer alacak bilgilerin belli bir maske ile görüntülenmesi isteniyorsa, maske bilgisi girilmelidir.

Genişlik; Sütun genişliğini piksel cinsinden belirleyebilirsiniz.

Hizalama; Bilgilerin sola dayalı, sağa dayalı ya da ortalanmış görüntüleneceğine dair seçenektir.

NDS Tip; Netsis'in diğer paketlerinden birinin içinden çalıştırıldığı durumda geçerli özellik olup, paket içindeki NDS (Netsis Decimal System) tanımlarından hangisinin sütun için geçerli olduğunun belirlendiği sahadır.

Kolon Max Genişlik; Sütunun içerdiği bilgilerin en genişi kadar dinamik genişlik alması için işaretlenmeli, işaretlenmediği durumda, genişlik olarak belirlenen değer geçerli olacaktır.

Renk butonu; Sütunun görünecek renginin belirlenebileceği seçenektir.

Yazı Yüzü; Sütundaki bilgilerin yazı tipi (font) ayarının yapılabileceği seçenektir.

Stretch: Resim bileşenin görünme şeklidir. Resim bileşeni için belirlenen resmin bileşenin boyutunda ayarlanması için True, resmin kendi boyutunda bileşenin içine yerleştirilmesi içinse False seçilmelidir.

Style: Combobox bileşeninin liste şeklinin belirlenmesi içindir. csDropDown (listeden seçilebilir, kullanıcı giriş yapabilir, liste kapalı gelir, kullanıcı isterse açar), csDropDownList (sadece listeden seçilebilir, liste kapalı gelir kullanıcı isterse açar), csOwnerDrawFixed, csOwnerDrawVariable, csSimple (liste açık gelir, kapatılamaz) değerleri alabilir.

TabIndex: Page Control içindeki sayfalardan birinin seçili hale getirilmesi için kullanılır. Sayfa numarası yazılmalıdır. Sayfalar ilk sayfa 0, ikinci sayfa 1 ... olmak üzere numaralandırılmıştır.

TabOrder: Kullanım sırasında, bileşenin içinde bulunduğu form, panel, page control vb. üzerinde kaçıncı sırada üzerine gelineceğidir. Giriş sırasını belirlemek açısından Taborder sıralamasına dikkat etmek gerekir. NDI, bileşenleri forma eklediğiniz sırada numaralandıracaktır. Ancak araya bir bileşen eklerseniz, bu bileşenin üzerine geliş sırası, en son sırada olacaktır. Ekrandaki yerleşim sırasına göre giriş sırasını, Taborder özelliğini kullanarak düzenleyebilirsiniz. Tek tek bileşenler için Taborder belirlemek yerine sağ tık pop-up menüde gelen Sekme Sırası Düzenleme seçeneği kullanılabilir. Bkz: Sağ tık/ Sekme Sırası

TabStop: Kullanımda giriş sırasında bileşenin üzerinde durulup durulmayacağı ile ilgilidir. Örneğin giriş sırasında, herhangi bir zamanda grid bileşeninin üzerine gelip durmaya gerek yoktur, çünkü grid bilgi amaçlıdır. Grid bileşeni için Tabstop False yapılabilir. Ancak bilgi girişi yapılacak bir okuma alanı (NetEdit ya da dbNetEdit) için Tabstop True olmalıdır. Bilgi girişi yapılmayacak olan, sadece bilginin gösterilmesi için konmuş olan alanlar, örneğin rehberden dönen kodun isminin gösterildiği saha, için ise False yapılabilir.

TabVisible: Page Control bileşeninin içine yerleştirilen sayfaların görünüp görünmeyeceği bilgisidir.

Tag: Programcının özel kullanımı içindir.

Text: Bileşenin içinde yer almasını istediğiniz varsayılan bilgidir. Kullanımda form açıldığında bileşen bu değeri alacaktır. Bileşenin içinde herhangi bir bilgi yer alması istenmediği durumda özellik değeri boşaltılmalıdır.

Top: Bileşenin, form üzerinde, panel ya da page control içindeki yerleşiminin üst kenardan piksel

cinsinden uzaklığıdır.

ValueChecked: DBCheckBox bileşeni için, kullanımda işaretlendiği ve işaretlenmediği durumda veri

tabanına saklanacak değerleri belirlemek içindir. Bu özellikte işaretli durum değeri verilmelidir.

Values: DBComboBox bileşeni için, Items özelliğiyle listeye eklenen her bir seçeneğin veri tabanına saklanacak değeridir. Açılan pencerede her satıra bir değer olmak üzere alt alta sıralanmalıdır.

ValueUnchecked: DBCheckBox bileşeni için, kullanımda işaretlendiği ve işaretlenmediği durumda veri

tabanına saklanacak değerleri belirlemek içindir. Bu özellikte işaretsiz durum değeri verilmelidir.

Visible: Bileşenin görünüp görünmeyeceği bilgisidir.

Width: Bileşenin piksel cinsinden genişliğidir.

#### Tasarım Ekranı Sağ Tık Menü Kullanımı

![](../_assets/2fa6efe85ed7bec08ace.png)

Tasarım üzerindeyken sağ tık ile açılan pop-up menüde. (Bkz. Ekran Görüntüsü 13) aşağıda detayı açıklanan işlemler yapılabilmektedir.

Özel İşlemler: Sadece TPageControl bileşeni seçiliyken sağ tık yapıldığında gelen seçenek olup, page control içinde, yeni bir sayfa yaratmaya, sayfalar arasında geçiş yapmaya, mevcut bir sayfayı silmeye yarar.

Tasarımı Kaydet (F2): Tasarımı mevcut son haliyle kaydetmeye yarar. F2 kısa yol tuşu da aynı işleve sahiptir.

Düzenle (Kopyala, Kes, Yapıştır, Sil): Seçili bileşen için Windows standart kullanımında yapılabilen kopyala, kes, yapıştır ve sil işlemlerini yapar. Bu işlemlerin standart Windows kullanımındaki kısa yol tuşları da geçerlidir.

Nesneyi Öne Getir: Tasarımda üst üste binmiş nesneler varsa, seçili olanı öne getirmeye yarar.

Nesneyi Arkaya Gönder: Tasarımda üst üste binmiş nesneler varsa, seçili olanı arkaya göndermeye yarar.

Sekme Sırası: Bu seçenekle, kullanım sırasında, bileşenlerin üzerine hangi sırada gelineceği yani giriş sırası listelenmektedir. Sıralama, içinde bulunulan form, panel, page control vb. birden fazla bileşen içeren kontrol ile ilgili olarak listelenir. Farklı bir bölümün sıralaması için, ilgili bölüm seçilerek sağ tık yapılmalıdır. Giriş sırası fare ile bileşenler kaydırılarak düzenlenebilir. Bu liste bileşenlerin forma eklenme zamanına göre sıralanır. Araya bir bileşen eklenirse, bu bileşenin üzerine geliş sırası, en son sırada olacaktır. Ekrandaki yerleşim sırasına göre giriş sırasını, bu listeden düzenleyebilirsiniz. Bu liste onaylandığında mevcut sıralama aynı zamanda bileşenlerin Tab order özelliğine yansıtılmaktadır.

![](../_assets/b9ab6b817def2ad9db60.png)

Object Inspector Göster (F11): Tasarımdan Object Inspector penceresine geçişi sağlar. Object Inspector'da seçili bileşen için özellik tanımları gelir. F11 kısa yol tuşu da aynı işleve sahiptir.

VCL Liste Göster (F11): Tasarımdan VCL (Visual Component Library) penceresine geçişi sağlar. F10 kısa yol tuşu da aynı işleve sahiptir.

Varsayılan Değer Göster: İstenen bileşenlere kullanım sırasında varsayılan değerler atamak mümkündür. Form açıldığında, ya da veri tabanı bağlantılı formda, yeni kayıt durumuna geçildiğinde, burada tanımlanan varsayılan değerler gelecektir.

![](../_assets/c10526d833638ae9196a.png)

Alanlar: Hangi alan için varsayılan değer tanımı yapılacağı belirlenir.

Ön değer Tipi: Sabit bir ön değer belirtilebileceği gibi, dinamik anlık oluşan bir ön değer de

belirlenebilmektedir.

Ön değer: Sabit ön değer ya da dinamik oluşturulmak istenen ön değer için SQL cümlesi yazılarak belirlenir. Örnek Select Getdate() cümlesi ile tarih sahasına günün tarihi ön değer olarak getirilebilir.

Ön Değer Sil: Tanımlanan ön değerler pencerenin alt bölümündeki grid üzerinde görülebilmektedir. İstenmeyen kayıtlar seçilerek sağ tık menüsü ile gelen Ön Değer Sil seçeneği ile silinebilir.

Anahtar Alan Göster: Veri tabanı bağlantılı ekranlarda, tablodaki hangi sahaların tekrarsız anahtar oluşturduğunun belirlenmesi gerekmektedir. (Bkz. Ekran Görüntüsü 16).

![](../_assets/ddadb64d17b6f8debaa2.png)

Tüm veritabanı üzerinde yapılacak işlemler (ilk/son kayıt, önceki/sonraki kayıt, yeni kayıt, silme vb.) bu anahtar alanlar baz alınarak yapılacaktır. Ekranla bağlantılı olan tabloda bir Primary Key (tekrarsız anahtar alan) yoksa, geri dönüp öncelikle böyle bir alan tespit edip SQL yardımıyla tablonuzda bunu belirtmelisiniz. Böyle bir alanınız mevcut ise, ekranda Anahtar Alan Göster işlemiyle mutlaka anahtar alanınızı forma tanıtmalısınız. Anahtar Alan Göster işleminde açılan pencerede, sol tarafta tablonuzdaki alanlar sıralanacak. Anahtar alanınızı belirleyip ekle butonu ile sağ taraftaki anahtar alanlar bölümüne ekleyebilirsiniz. Birden fazla alanın birleşmesiyle oluşan bir anahtarınız varsa (segmented key) bu durumda alanları sırasıyla seçip ekleyiniz. Yanlışlıkla eklenmiş bir anahtar alanı seçiliyken çıkar butonuna basarak listeden çıkarabilirsiniz. Pencerenin alt tarafındaki tamam butonu ile değişiklikleri saklayarak, iptal butonu ile değişiklikleri saklamadan pencereyi kapatabilirsiniz.

Dinamik Kod Girişi: Bileşenler ve özellikleri kullanılarak yapılan uygulama tasarımında ayrıca programlama yapılmasını gerektiren durumlarda Script girişi kullanılabilir.

![](../_assets/72d77668d5c42c22a212.png)

Script girişinde Visual Basic dili tam anlamıyla desteklenmekte olup bu dil kullanılarak istenildiği şekilde programlama yapılabilir. NDI formunun mevcut bileşenleri, özellikleri ile NDI'a özel geçerli değişkenler, Script ortamında kullanılabilmektedir. Script ile yapılabileceklere birkaç basit örnek verecek olursak, bir veri giriş bileşenine kullanıcının yazdığı değerin, bileşenin çıkışında (OnExit) kontrol ederek geçerli bir değer olup olmadığını saptamak, geçersiz değer ise uyarı vermek ve işlemi durdurmak; Bir butona basıldığında ya da yine bir bileşenin çıkışında birtakım hesaplamalar yapmak ve sonucu form üzerinde göstermek, bir butona basıldığında başka bir pencere açılmasını sağlamak içindir. Dinamik Kodlama kullanımı ile ilgili detay bilgi için ilgili dokümanımızı inceleyebilirsiniz.

#### Rehber Tanımlama

Rehber Tanımlama seçeneği ile, NDI tasarımlarında kullanılacak olan her çeşit rehber tanımlanabilir, topluca izlenebilir ve yönetilebilir. Bu bölümde tanımlanan bir rehber, aynı amaca hizmet eden birçok tasarımda ve bir tasarım içinde birden fazla kez kullanılabilir.

![](../_assets/3c2b9bbee1b3287eb8cc.png)

Rehber Tanımlama sekmesinde yer alan bilgilerin detayları aşağıdaki gibidir.

Rehber Kodu: Tanımlanan her rehber için serbest ve tekrarsız bir kod belirlenmelidir. Kendi sistematiğinize göre burada kodlamanızı yapabilirsiniz. Belirlenen kod dizayn ortamında tasarıma eklenen rehber tuşunun rehber kodu özelliğinde belirtilecektir.

Açıklama: Tanımlanan rehbere ait açıklama bilgisi girilecek alandır. Hatırlatma amacıyla, rehberin içeriği ve kullanım amacı ile ilgili bilgi yazılmasında fayda var.

Veritabanı Bağlantı Kodu: NDI ile birden fazla veri tabanında bulunan tablolar için rehber tanımlanabilmektedir. Örneğin hem Temelset hem de Personel veri tabanlarına ait rehber tanımlanabilir. Veri tabanı bağlantıları dokümanın ilerleyen bölümlerinde anlatılacak olan başka bir menü seçeneğinden yapılmaktadır. (Bkz: Veri tabanı Bağlantı Tanımlama). Her bir veri tabanı bağlantısı tanımına bir kod verilecektir. Bu sahada ise, tanımlanan veri tabanı bağlantılarından hangisinin kullanılacağı, veri tabanı bağlantı kodu verilerek belirlenecektir. Tanımlı veri tabanı bağlantıları, sahanın rehberi aracılığıyla da belirlenebilir.

Tablo Adı: Rehber ile ilişkili olan, arama yapılacak ve görüntülenecek tablo ya da View'ın veri tabanındaki adıdır. Tablo ya da View'ın dizayn öncesinde, veri tabanında SQL komutları yardımıyla yaratılmış olması gerekmektedir.

Grup Kodu: Hazırlanan rehberlerin gruplanması isteniyorsa bu sahada, ilgili rehberin içinde yer alacağı grubu belirtebilirsiniz. Kendi sistematiğinize göre gruplandırmayı yapabilirisiniz. Herhangi bir grup kodu verilmezse, NDI, rehberi GENELREHBER grubu altına alacaktır.

Kısıt: Rehberin düzenlendiği tablodaki herhangi bir sahaya kısıt verilerek, rehberde gelen kayıt kümesinin daraltılması sağlanabilir. Kısıt cümlesi, SQL cümlelerinin WHERE ile başlayan kısıt bölümünde yazılan formatta olmalıdır.

Tuş: Rehber kısa yol tuşudur. Kullanımda, Ctrl tuşu ile birlikte bu tuşa basıldığında, rehber aktif hale gelir.

Rehber Detay sekmesine geçildiğinde, kullanılacak olan rehber alanları ön sekmede yazılmış olan tablodaki alanlardan tek tek seçilmektedir.

![](../_assets/3118355d87fe0f4b1ac5.png)

Bu sekmede yer alan alanların detayları aşağıda verilmiştir.

Gösterim Sırası: Tanımlanacak sahanın rehberde kaçıncı sırada getirileceğinin bilgisidir.

Alan Adı: Rehbere getirilecek olan sahanın tablodaki saha ismi karşılığıdır.

Açıklama: Rehbere getirilecek olan sahanın kullanıcıya gösterilecek başlık bilgisidir.

Odakla: Rehber açıldığında arama amaçlı üzerinde durulacak olan sahanın hangisi olacağının belirlendiği bilgidir. Rehberde bulunan alanlardan sadece bir tanesi için bu değer işaretlenebilir.

Dönüş: Rehberden uygulamaya döndürülmesi istenen sahanın hangisi olduğunun belirlendiği alandır. Rehberde bulunan alanlardan sadece bir tanesi için bu değer işaretlenebilir.

#### Grup Kodu Tanımlama

Dizayn ve rehberlerin gruplandırılması için grup tanımlamalarının bu ekran ile yapılmış olması gerekmektedir. Burada yapılan grup tanımlamaları rehber ve dizayn kayıt ekranlarındaki Grup Kodu rehberinden seçilebilecektir.

![](../_assets/cfc76cb17f713a9e348f.png)

#### Veritabanı Bağlantı Tanımlama

NDI aracılığıyla yapılan dizaynlarda kullanılan veri, istenen herhangi bir veritabanında saklanabilmektedir. İstenirse, veriler birden fazla veritabanında da bulunabilir. Bu ekran, NDI uygulamasında kullanılacak verilerin getirileceği veritabanı bağlantılarını tanımlamak amacıyla kullanılır.

Bağlantı Kodu: Tanımlanan her veritabanı bağlantısı için kullanıcı tarafından tekrarsız bir kod belirlenmelidir. Kendi sistematiğinize göre burada kodlamanızı yapabilirsiniz. Burada vereceğiniz kod, tasarlanmış olan veritabanı ilişkili ekran ve rehber tanımlamalarında Veritabanı Kodu alanında seçilebilecektir.

Bağlantı Açıklama: Veritabanı bağlantısının kullanıcı tarafından belirlenen açıklama bilgisidir.

Hatırlatma amacıyla ilgili bağlantıyı açıklayabilecek bir bilgi yazılmalıdır.

Paket: Netsis paketlerinden birine bağlantı yapılıyorsa, program otomatik olarak ilgili paketin hangi veritabanı sunucusunda çalıştığını algılar. Bu alanda Ticari, Personel, Demirbaş, İşletme ve Diğer seçeneklerinden birinin seçilmesi gerekmektedir. Burada Diğer seçeneğinin seçilmesi demek, verilerin Netsis paketinin kurulu olmadığı farklı bir veritabanından geleceği anlamına gelmektedir.

Hesaplansın: Veri tabanı bağlantısı, Netsis'in diğer paketleri içinden kullanılacak nesneler için tanımlanıyorsa, mutlaka hesaplanacak seçeneği işaretlenmelidir. Bu durumda, nesne paketin içinden çalışırken, veri tabanı bağlantısını kendi içinde çalıştığı paketinkiyle aynı şekilde yapabilecektir.

Veritabanı Sunucu: Netsis paketleri dışında bir paket ile bağlantı yapılacak ise, veritabanı sunucusunun ismi yazılmalıdır. Netsis paketleri ile bağlantıda, bağlanılacak veritabanı sunucusu bilgileri, pakete ait kurulum bilgilerinden otomatik alınır ve sorgulanmaz.

Veritabanı Adı: Tanımlanan bağlantı kodu ile bağlanılacak veritabanı adının yazıldığı alandır.

Veritabanı Kullanıcı: Yukarıda detayları verilen veritabanı sunucusu ve veritabanına bağlantı gerçekleştirirken kullanılacak kullanıcı adı bilgisidir. Buraya yazılacak kullanıcı, veritabanı seviyesinde tanımlı bir kullanıcıdır, Netsis içerisinde mevcut tanımlanan kullanıcılar değildir. Paket bilgisi olarak Diğer dışında bir seçenek seçilmiş ise bu alana bir değer yazılması istenmeyecektir. Bu durumda veritabanı kullanıcısı olarak pakete ait kurulum bilgilerinden otomatik olarak getirilir.

Şifre: Veritabanı kullanıcısının veri tabanına bağlanmak için kullandığı şifredir. Paket bilgisinde Diğer dışında bir seçenek seçilmiş ise bu alana bir değer yazılması istenmeyecektir.

Veritabanı Tip: Paket bilgisi olarak Diğer seçildiğinde aktif olan bir alandır ve Diğer seçeneği dışında biri seçildiğinde bu bilgi paketin kurulum bilgilerinden otomatik olarak alınacaktır. Diğer seçeneği ile bağlantı kurulmak istenen veri tabanının tipi seçilebilmektedir. Bu alanda MSSQL, Oracle seçeneklerinden birinin seçilmesi gerekmektedir.

![](../_assets/217138cdb7b006788d89.png)

#### Şirket Tanımlama

NDI uygulaması ilk kurulduğunda varsayılan olarak NDI32 adı ile otomatik olarak oluşturulmuş bir şirket tanımı olacaktır. İstenirse Şirket Tanımlama işlemi ile farklı şirketler de oluşturulabilir. Bu şirketlerde farklı tasarımlar ve farklı kullanıcılar yer alabilir. NDI'a giriş sırasında birden fazla şirket bulunması halinde giriş yapılacak şirketin seçilmesi gerekecektir.

![](../_assets/0c00f6b92662949c4521.png)

#### Şirket Parametreleri

İçinde bulunulan NDI şirketine ait ana parametrelerin bulunduğu bölümdür.

![](../_assets/e6311072e3135bde536a.png)

Şirket Parametreleri ekranı üzerinden ayarlanabilecek olan parametreler aşağıdaki gibidir:

Seviye: Bu parametre ile İleri/Kolay olmak üzere iki seviyede belirlenebilmektedir. İleri seçeneği seçildiğinde dizayn ortamı ekranında yer alan VCL Palette kısmında "İleri" grubu altında yer alan bileşenler kullanılabilir. Bu seçenekte Kolay seçilmesi durumunda buradaki bileşenler kullanılamayacaktır.

Rehber Kullanım Şekli: Rehberlerin farklı şekillerde kullanılması mümkündür. Buradaki Combobox alanından istenilen rehber şekli seçilmelidir. Rehberler Normal, Sırasız ve Hızlı olmak üzere 3 çeşittir. Kullanım şekli Temelset paketindeki ile aynıdır.

Ekran Açılış Modu: Veri tabanı ilişkili olan NDI dizaynlarında ilgili ekran açıldığında veritabanı bağlantılı olan alanların nasıl dolacağı seçilmektedir. Burada İlk Kayıt, Yeni Kayıt ve Son Kayıt seçeneklerinden biri seçilebilecektir. İlk Kayıt seçili ise form açıldığında ilk kayda odaklanacak, Son Kayıt seçili ise form açıldığında son kayda veya Yeni Kayıt seçili ise form yeni kayıt girişine hazır şekilde hiçbir kayda odaklanmadan acıkacaktır.

Ekranlarda Silme Uyarısı: Veritabanı bağlantılı olan NDI dizaynlarında mevcut bir kayıt silinmek istendiğinde kullanıcıya "Kayıt silinecektir. Emin misiniz?" gibi bir uyarı mesajı çıkması isteniyorsa bu seçenek işaretlenmelidir.

Sesli Uyarı: İşlemler sırasında çıkan uyarı ekranlarında sesli olarak da uyarı gelmesi isteniyorsa işaretlenmesi gereken parametredir.

E-Posta Uygulaması: Formlar aracılığı ile e-posta gönderimi desteklenmesi isteniyorsa işaretlenmesi gereken parametredir. Bu parametre işaretlendiğinde, e-posta uygulaması için gerekli olan aşağıdaki iki saha sorgulanacaktır.

SMTP Server Adı: E-posta uygulaması işaretlendiği zaman aktif olan parametredir. Bu sahaya internet

sunucusunun adı girilmelidir.

SMTP Kullanıcı Adı: E-posta uygulaması işaretlenmiş ise aktif olan parametredir. Internet sunucusunun bulunduğu makinede geçerli olan bir kullanıcının adının girileceği sahadır. NDI üzerinden e-posta gönderimi yapıldığında, gönderen kişi olarak bu sahaya girilen kullanıcı adı görüntülenecektir.

SMTP Şifre: SMTP Kullanıcı Adı sahasına girilen kullanıcıya ait şifrenin girilebileceği sahadır. Kullanılan bazı internet sunucuları için bu sahaya bilgi girilmesi zorunludur. Kullanıcı adı ve şifre sahaları, bilgi girişinin zorunlu olmadığı durumlarda boş geçilebilir.

#### Ekran Hakları Tanımlama

NDI ile tasarlanan nesnelerin, NDI uygulamasından kullanımı ile ilgili kullanıcı hakları belirlemeye yarayan bölümdür. NDI ile tasarlanan ekranlar Temelset vb. diğer paketlerden kullanılacaksa burada herhangi bir tanımlama yapmaya gerek yoktur.

![](../_assets/643ae5aea1cb2923ae02.png)

Nesne Tipi: Kullanıcı hakları belirlenecek olan nesne tipinin seçileceği alandır. Tasarlanan ekranlar, raporlar ve rehberler için kullanıcı hakları tanımlanabilmektedir.

Nesne Kodu: Dizayn Hazırlama ile hazırlanmış olan dizaynın, Rehber Tanımlama ile hazırlanmış olan rehberin ya da rapor modülünde hazırlanmış raporun kodudur.

Kısıt Kapsam: Kullanıcı haklarının, tek bir kullanıcı, kullanıcı grubu ya da tüm kullanıcılar bazında tanımlanacağının bilgisidir.

Kullanıcı No, Kullanıcı Grup No: Bir tek kullanıcı ya da kullanıcı grubu için hak tanımlanması isteniyorsa, kısıt kapsam sahasında belirlenen seçeneğe göre kullanıcı kodunun ya da grup kodunun girileceği sahalardır. Rehberden yararlanarak tanımlı kullanıcılardan ya da gruplardan seçim yapılabilir.

İzleme, Kayıt, Düzeltme, Silme: Belirlenen kullanıcı, kullanıcı grubu ya da tüm kullanıcıların, bu nesne üzerinde yapabileceği işlemlerin belirlenebileceği sahalardır. Yapılması istenen işlemler işaretlenmeli, engellenmesi istenen işlemler ise işaretlenmemelidir.

Tüm Yetkileri Ver: İzleme, Kayıt, Düzeltme, Silme işlemlerinin tamamının tek tuşla işaretlenmesini sağlar.

Tüm Yetkileri Kaldır: İzleme, Kayıt, Düzeltme, Silme işlemlerinin tamamının tek tuşla işaretlerinin kaldırılmasını sağlar.

#### XML Dışarı Aktar-İçeri Yükle

Dizayn XML Dışarı Aktar ve Rehber XML Dışarı Aktar seçenekleri NDI'da tanımlanmış olan bir dizayn veya rehberin dış ortama XML dosya formatında kaydedilmesi için kullanılır. Dizayn XML İçeri Yükle ve Rehber XML İçeri Yükle seçenekleri ise öncesinde XML dosya olarak dışarı aktarılmış dizayn veya rehberlerin tekrar NDI'a kaydedilebilmesi için sağlanmaktadır.

![](../_assets/bc6fbca6753275b81897.png)![](../_assets/8921013dc7112ef8dc45.png)

Dışarı aktar işleminde yer alan alanlar şunlardır:

Dizayn Kodu: Aktarılmak istenen dizaynın, dizayn tanımlamada belirlenen kodudur.

Dosya Adı: Aktarılmak istenen fiziksel dosya ismi olup, ekrandaki yardım butonu aracılığıyla klasör ve

dosya ismi belirlenebilir.

Kullanıcı Tanım: Kullanıcı Tanımlarının aktarılması, aktarılan bu nesnenin, yüklenmesi sırasında, karşı taraftaki NDI uygulamasında bulunan tüm kullanıcılara bu nesne ile ilgili tüm hakların verileceği anlamına gelir. Kullanıcı Tanımları aktarılmamış ise, nesnenin yüklenmesi sırasında karşı taraftaki NDI uygulamasında herhangi bir kullanıcı hakkı tanımlanmayacak, kullanıcılar yüklenen bu nesneyi göremeyecekler, kullanıcı haklarının yükleme sonrasında ayrıca yapılması gerekecektir.

Veri Tabanı Bağlantı Bilgisi: Veri tabanı bağlantı bilgisinin de nesneyle birlikte transfer edilip edilmeyeceğini belirlemek içindir. Veri tabanı bağlantısı transfer edilmediği durumda, başka NDI paketine bu XML yüklendiğinde, dizayn tanımında veri tabanı bağlantısı oluşturulması gerekecektir.

İçeri yükle işleminde yer alan alanlar;

Dosya Adı: Yüklenmesi istenen fiziksel dosya ismi olup, ekrandaki yardım butonu aracılığıyla klasör ve dosya ismi belirlenebilir.

Nesne Adı: Yüklenecek nesnenin kodu, XML dosyadan bulunarak getirilmektedir. İstenirse değiştirilerek farklı bir kodla yüklenebilir.

Veritabanı Bağlantı Kodu: Yüklenecek nesnenin XML dosyaya aktarımı sırasında veritabanı bağlantı kodu aktarılmış ise bu bilgi otomatik getirilecektir. İstenirse değiştirilip mevcut veri tabanı

bağlantılarından biri kullanılabilir. Eğer veri tabanı bağlantı bilgisi aktarılmamışsa bu saha okutulmayacaktır ve nesnenin veritabanı bağlantı bilgisi oluşmayacaktır. Bu durumda nesnenin tasarlandığı bölümden bu bilgi düzenlenmelidir.

#### Kullanıcı Grup Kayıtları

Gezgin\\Genel\\Kullanıcı İşlemleri\\Kayıt menüsü altında yer alan Kullanıcı Grup Kayıtları ekranı ile NDI'da yetkisi olacak kullanıcıların belirli gruplar altında yer alması isteniyorsa öncelikle bu ekrandan tanımlanması gerekmektedir.

![](../_assets/14069f6cbaad01882d4b.png)

Ayrıca bu ekran üzerinden seçilmiş olan gruba bağlı olan kullanıcılar Gruba Bağlı Kullanıcılar butonu ile listelenebilir, Grup Yetkileri butonu ile seçilmiş olan gruba atanmış olan haklar izlenebilir veya Grup Kopyalama butonu ile mevcut bir grup tanımı kopyalanabilir.

#### NDI ile Netsis Paketleri Entegrasyonu

NDI paketinde hazırlanan ekranların Temelset ve Netsis Bordro paketinde bulunan modüllerdeki menülere eklenebilmesi ve bu modüllerden çalıştırılabilmesi ve NDI paketinde hazırlanan rehberlerin, Temelset ve Bordro paketlerinde hazırlanan ek rehberler mantığıyla kullanılabilmesi mümkündür. Ayrıca, NDI paketinde hazırlanarak Temelset ve Bordro paketine eklenen ekranlar için Kolon Bazı Geçerlilik, Satır Bazı Güvenlik ve Log uygulamaları kullanılabilir.

NDI'da hazırlanan ekran veya rehberlerin Netsis Temelset veya Netsis Bordro içerisinden kullanılabilmesi için bazı tanımlamaların yapılması gerekmektedir.

#### NDI ile Netsis Temelset Bağlantısı

NDI paketinde hazırlanan ekran ve rehberlerin kullanılacağı şubeler için öncelikle Netsis Temelset paketinde bulunan Yardımcı Programlar/Şirket/Şube/Parametre Tanımları ekranında bulunan "NDI Uygulaması Var" parametresinin işaretlenmesi gerekmektedir.

![](../_assets/e59d9c4073348ab34715.png)

"NDI Uygulaması Var" parametresinin işaretlenmesi halinde Genel\\Yardımcı Programlar\\Kayıt\\NDI menüsü altındaki "NDI Bağlantı Tanımları" ve "NDI Nesneleri" ekranları aktif olacaktır.

#### NDI Bağlantı Tanımları

NDI Bağlantı Tanımları ekranındaki tanımlamalar ile, Temelset paketindeki şubelerden hangi NDI şirketine bağlanılacağı bilgisi belirlenmektedir.

![](../_assets/6db8f5a7121eca399af3.png)

İşletmelerde Ortak: Tanımlanan bağlantının hangi işletmeler için geçerli olduğunun belirlendiği alandır. Temelset-NDI bağlantısının tüm işletmelerde geçerli olması isteniyorsa bu sahaya -1, sadece belirli bir işletmede geçerli olması isteniyor ise de ilgili işletmenin kodu girilmelidir. Bu saha merkez işletmede aktif olacaktır. Bağlantı tanımlaması, merkez işletmede yapılmıyor ise, işletme kodu sahası pasif olacak ve içinde bulunulan işletme kodu program tarafından getirilecektir.

Şubelerde Ortak: Tanımlanan bağlantının hangi şubeler için geçerli olduğunun belirlendiği alandır. Temelset-NDI bağlantısının tüm şubelerde geçerli olması isteniyorsa bu sahaya -1, sadece belirli bir şubede geçerli olması isteniyor ise de ilgili şubenin kodu girilmelidir. Bu saha sadece merkez şubede iken aktif olacaktır. Bağlantı tanımlaması, merkez şubede yapılmıyor ise, şube kodu sahası pasif olacak ve içinde bulunulan şube kodu, program tarafından getirilecektir.

NDI Şirket Adı: Bağlantı kurulacak NDI şirketinin belirlendiği sahadır. Sahanın sağ tarafında bulunan aşağı ok işaretine basıldığında NDI paketinde tanımlı şirketlerin isimleri listelenecektir. Yukarıda açıklanan İşletmelerde Ortak ve Şubelerde Ortak sahaları kullanılarak, birden fazla işletme ve şubenin tek bir NDI şirketi ile bağlantısını sağlamak mümkündür.

#### NDI Nesneleri

NDI paketinde hazırlanan ekran ve rehberlerin listelendiği ve bu nesnelerin Temelset modüllerine eklenmesi için kullanılan menüdür. Temelset içerisinden kullanılacak olan her bir ekran ve rehberin bu ekrandan tanımlanmış olması gerekmektedir.

![](../_assets/b2b91a7ea558d75eabb7.png)

Program Numarası: Temelset'e eklenen her bir NDI nesnesine tekrarsız serbest bir numara verilmelidir. Verilen bu program numaraları daha sonra Merkezi Kimlik Yönetimi üzerinden kullanıcılara nesne ile ilgili hakların belirlenmesi sırasında kullanılacaktır. NDI paketinde tanımlanan nesne ve rehberler, Temelset paketine eklendikten sonra, yönetici (Admin) yetkisine sahip olmayan kullanıcılar için, bu nesnelere ait hak tanımlaması yapılacaktır.

![](../_assets/8789f89027bd9536aec0.png)

Kullanılacak Modül Numarası: NDI paketinde tanımlanan ekranların, hangi Temelset modülünde kullanılacağının belirlendiği sahadır. İlgili ekranın bütün modüllerde kullanılması isteniyorsa Tüm Modüller, sadece belirli bir modülde kullanılması isteniyorsa, ilgili modül seçilmelidir. NDI'da tanımlanan rehberlerin Temelset paketine eklenmesi aşamasında, burada seçilen Kullanılacak Modül Numarası bilgisinin herhangi bir geçerliliği yoktur. Rehberler, Temelset paketi içinden hazırlanan diğer ek rehberler gibi tüm modüllerde kullanılabilecektir.

Başlık: Eklenen ekran ve rehberlerin başlık bilgisi olup, Merkezi Kimlik Yönetiminde kullanıcı hakları tanımlama ekranında ilgili rehber veya ekranlar için bu sahada belirlenen isimler listeleneceklerdir. Ayrıca, tanımlı ekranların Temelset modüllerine eklenmesi halinde, ekranlar için bu sahada girilen başlık bilgileri, modül ana menüsüne gelecek olan NDI Uygulamaları menü başlığı altında listelenecektir. Örneğin NDI paketinde hazırlanan "929-3" nesne kodlu ekranın, tüm modüllerdeki NDI menüsü altına eklenmesi aşamasında, başlık bilgisi olarak "Vardiya Çalışan Kayıtları" girildiğinde, her modülde yer alan NDI Uygulamaları menüsü aşağıdaki gibi olacaktır.

![](../_assets/6415b2f21f6bd255a21d.png)

Grup Başlığı: Modül ana menüsüne eklenen ekranın, menüde bir alt başlık altında listelenmesi isteniyorsa kullanılacak sahadır. Nesne, ilgili modüldeki NDI Uygulamaları menüsünde, tanımlamada verilen grup başlığı altında listelenecektir. Örneğin "Vardiya Çalışanları" nesnesinin Cari modülüne eklenmesi aşamasında Grup Başlığı sahasına "Vardiya Bilgileri" girilmesi halinde, menü aşağıdaki gibi olacaktır.

![](../_assets/577cd6ef86165d16ae03.png)

NDI paketinde ekran tanımlaması yapılırken form tipi olarak Normal seçilmesi gerekmektedir. Child olarak tanımlanan ekranlar Temelset paketine eklenemeyecektir.

Birden fazla NDI şirketinin olması ve bunlardan birisi için, içinde bulunulan şube ile bağlantı tanımlanmış olması halinde, bu listede, bağlantı tanımlaması yapılmış olsun ya da olmasın, tüm NDI şirketlerinde tanımlanan nesneler görüntülenecektir. Ancak, bağlantı tanımlanmamış NDI şirketinde oluşturulan nesneler, bu bölümden Temelset menüsüne eklenebilmesine rağmen, menüde görülemeyecektir. Bu yüzden, nesnelerin tanımlı olduğu NDI şirketi için mutlaka NDI-Temelset bağlantı tanımlamasının yapılmış olması gerekmektedir.

#### NDI ile Netsis Bordro Bağlantısı

NDI paketinde hazırlanan ekran ve rehberlerin kullanılacağı şirketler için öncelikle personel paketinde bulunan Ek Modüller\\Yardımcı Programlar\\Kayıt\\İşletme-İşyeri Tanımları ekranında yer alan "NDI Uygulaması Var" parametresinin işaretlenmesi gerekmektedir.

![](../_assets/640fb31779deb6a41dc0.png)

Bu durumda, içinde bulunulan şube ile NDI veri tabanı bağlantısının kurulacağı ve NDI paketinde tanımlanan ekran ve rehberlerin ilgili şubede kullanılmasına yönelik tanımlamaların yapılacağı menüler Netsis Bordo paketindeki Yardımcı Programlar/Kayıt/NDI menüsü altında aktif hale gelecektir.

![](../_assets/8c73d70903c83c5102ea.png)

#### NDI Bağlantı Tanımları

NDI Bağlantı Tanımları ekranındaki tanımlamalar ile, Netsis Bordro paketinden hangi NDI şirketine bağlanılacağı bilgisi belirlenmektedir.

![](../_assets/2a0b13f57dfcbc3ced42.png)

İşyeri Kodu: İlgili Netsis Bordro şirketinde yer alan işyeri kodları bu alanda listelenecektir. Burada seçilen işyeri ilgili NDI şirketi ile bağlanmış olacaktır.

NDI Şirket Adı: Bağlantı kurulacak NDI şirketinin belirlendiği sahadır. Sahanın sağ tarafında bulunan aşağı ok işaretine basıldığında NDI paketinde tanımlı şirketlerin isimleri listelenecektir.

Ortak Bağlantı: Tanımlamada belirlenen NDI şirketine bağlanarak NDI ile tasarım yapabilme ve tasarlanmış uygulamaların kullanımının, genel bir kullanıcı ile gerçekleşmesi isteniyorsa işaretlenmesi gereken seçenektir. Ortak Bağlantı seçeneğinin işaretlenmesi halinde (Anonymous Access), NDI paketine bağlantı, Bordro paketine bağlanan kullanıcılar yerine, bu bölümde verilecek olan kullanıcı ve şifre ile yapılacaktır. Bu durumda NDI tarafında, burada belirlenen kullanıcı isim ve şifresinin tanımlı olması yeterli olacaktır. Ortak Bağlantı seçeneğinin işaretlenmediği durumlarda ise (Integrated Netsis Authentication), kullanıcının NDI şirketinde tasarım yapabilmesi ve tasarımları kullanabilmesi için, Bordro şirketine giriş yaptığı kullanıcı adı ve şifresi geçerlidir. Dolayısıyla, Ortak Bağlantının işaretli olmadığı durumlarda, NDI şirketine bağlanacak tüm kullanıcıların ve şifrelerinin, NDI şirketinde tanımlanmış olması gerekmektedir.

NDI Kullanıcı Adı: Ortak Bağlantı seçeneğinin işaretlenmesi halinde sorgulanan sahadır. Bu sahada, seçilen NDI şirketine bağlantı için geçerli genel kullanıcı adı girilmelidir. Netsis Bordro-NDI entegrasyonunu kullanacak tüm kullanıcılar için burada girilen kullanıcı adı ile bağlantı sağlanacaktır. Girilen kullanıcı adının, mutlaka NDI şirketinde de tanımlanmış olması gerekmektedir.

NDI Kullanıcı Şifresi: Ortak Bağlantı seçeneğinin işaretlenerek, NDI Kullanıcı Adı sahasında belirlenen kullanıcıya ait şifre bilgisinin girileceği sahadır.

NDI Nesneleri menüsünün kullanımı yukarıda açıklanan Temelset paketindeki tanımlamalar ile aynıdır, bu sebeple bu bölümde tekrar detaylandırılmamıştır. NDI Dizayn Ortamı ekranı ile NDI uygulamasının açılması sağlanabilmektedir.

#### NDI Nesnelerinde İş Akış Desteği

NDI paketinde hazırlanarak Temelset paketine eklenen veritabanı ilişkili ekranlar iş akışa dahil edilebilmektedir. Bunun için öncelikle, NDI paketinde ekranların hazırlanması aşamasında, bu ekranların iş akışa dahil edileceği belirtilmektedir. NDI paketinde ekranların hazırlanması aşamasında, iş akışa dahil edilmek istenen ekranlarda farenin sağ tuşuna tıkladığında gelen menüden "İş Akış Dahil Et" seçeneği işaretlenmelidir.

![](../_assets/33bbe677f4746997a5ce.png)

İş Akış Dahil Et seçeneği işaretlenmediğinde, Temelset paketinde iş akışı uygulamasının kullanılıyor olmasına rağmen, NDI paketinde hazırlanan ekranlar, iş akışa dahil edilemeyecektir.

Sonraki adımda İş Akış Kayıtları ekranından NDI Uygulamaları modülü için iş akışa dahil etmek istediğimiz ekranlar için tanımlamalar yapmamız gerekmektedir. Program No alanında iş akışa dahil edilen ve NDI Nesneleri ekranında Temelset üzerinde bir modüle eklenmiş olan NDI tasarımları gelecektir.

![](../_assets/59ffbc8bbde1a6e43dca.png)

İş Tanımlamaları sekmesinde bu tanımlamayı yaptıktan sonra ikinci sekme olan İş Akış Yolu Kayıtları ekranından ilgili NDI formu üzerinde Path Tipi alanında belirtilen türde bir işlem yapıldığında hangi kullanıcılara onaya gitmesi isteniyorsa bu tanımlamalar yapılacaktır, bu sekmedeki tanımlamalar klasik Temelset ekranlarındaki iş akış yolu kayıtları için yapılan tanımlamalar ile aynıdır.

#### NDI Rehberleri için Ek Rehber Tanımlamaları

NDI paketinde hazırlanan rehberlerin de diğer ek rehberlerde olduğu gibi, Temelset paketinde hangi tuş ile kullanılacakları Yardımcı Programlar\\ Kayıt\\ Ek Rehber Oluşturma bölümünde belirlenmektedir.

![](../_assets/659d18165de6628a6bd9.png)

Geçerli olması istenen tuş bilgisi girildikten sonra, Tablo Adı sahasında ilgili rehber seçilmelidir. NDI paketinde hazırlanan rehberler, Tablo Adı sahasında bulunan aşağı ok tuşuna basıldığında çıkan listenin en altında bulunmaktadır. Bu rehberlerin listede gösterim formatı "NDI; Rehber Başlığı; Program Numarası" şeklide olacaktır. Rehber başlığı ve program bilgisi, NDI Nesneleri menüsünde tanımlanmaktadır.

NDI paketinde hazırlanan rehberler için Ek Rehber Oluşturma bölümünde başka herhangi bir tanımlama yapılması gerekmemektedir. Tanımlama kaydedildikten sonraki kullanımı, doğrudan Ek Rehber Oluşturma bölümünden tanımlanan rehberlerde olduğu gibidir.

#### Rapor Modülü

Gezgin\\Genel\\Rapor\\Raporlar menüsü altından tanımlı olan rapor ekranları kullanılabilir. Bu raporların kullanımı Temelset paketinde yer alan rapor modülü ile aynıdır.

![](../_assets/9b6869968b30187aa01f.png)

Kullanıcı Ekranları raporu ile ekran olarak tasarlanan NDI nesneleri raporlanabilmektedir, benzer şekilde Kullanıcı Rehberleri raporu ile rehber olarak tasarlanan NDI nesneleri raporlanabilmektedir.

#### Log Modülü

NDI ekranları üzerinde yapılan çalışmaların log kayıtlarının tutulması isteniyorsa log modülü kullanılabilir. Uygulama Temelset'deki mantıkta çalışmaktadır, öncelikle Log parametreleri ekranından "Log Uygulaması Kullanılsın" seçeneğinin işaretlenmesi gerekmektedir.

![](../_assets/651e4bc5ce269e2bbfdc.png)

Bu ekranda eğer alınan raporların da log kayıtlarında yer alması isteniyorsa "Raporlar Loga Yazılsın" seçeneğinin işaretlenmesi ve değişiklik yapılan kayıtların eski halinin saklanması isteniyorsa "Düzeltme İşlemlerinde Kaydın Eski Hali Tutulsun" parametresinin işaretli olması gerekmektedir. Bu tanımlamalardan sonra Log Tutulacak tablolar ekranı ile log tutulması istenen tabloların seçimi yapılmalıdır.

#### Örnek NDI Ekranı

Örnek olarak ZIYARETCI ve ZIYARETCI_KART ismi ile iki tablo oluşturalım ve firmamıza giriş yapan çalışan personel haricindeki kişileri burada kayıt altına alacağımızı varsayalım.

![](../_assets/5c8dd312a3c5e04a8233.png)![](../_assets/a24e0fcdeb432f4cbfb5.png)

Bu tasarım için NDI formunu oluştururken "Veritabanı İlişkili" seçeneğini işaretliyorum, böylece tasarım ekranında VCL Palette bölümünde Veritabanı Kontrol bölümünde yer alan bileşenleri kullanabileceğim.

![](../_assets/f586276acf68a8c0446e.png)

Dizayn ortamına geçtiğimizde öncelikle form üzerindeki anahtar alan/alanların belirlenmesinde fayda var, bu tablo yapısında ben SIRA alanını anahtar alan olarak belirliyorum. Böylece SIRA alanı değiştiğinde ilgili SIRA numaralı kaydı forma otomatik taşıyacak veya TDbOpButton ile önceki/sonraki kayıt butonları tıklandığında bir sonraki sıra numaralı kaydı forma getiriyor olacaktır.

![](../_assets/d7e126f5bcec6e98073a.png)

![](../_assets/42bfb40f6286eb69b841.png)

Formumuz üzerine üst kısımda kayıtlar arasında gezmemizi sağlayacak TDbOpButtonların yer alacağı bir panel ekleyelim. Ve panelin formun en üstünde yer alması için *Align* özelliğini alTop olarak ayarlayalım. Ayrıca panel üzerinde bir metin yazmaması için *Caption* bilgisini temizliyoruz ve dışında çerçeve eklenmesi için *BorderStyle* özelliğine bsSingle değerini seçip, *BorderWidth* yani çerçeve kalınlığını da 2 olarak ayarlıyoruz. Bu panelin içine ekleyeceğimiz TDbOpButtonları ekliyoruz. Örneğin ilk butona tıklandığında ilk kayda gidilmesi isteniyorsa *DbOperation* özelliğini doFirst olarak ayarlamamız gerekecektir. Ayrıca butonun üzerinde \<\< yazması için de *Caption* özelliğini değiştiriyoruz.

![](../_assets/5098018ced1235c868c3.png)![](../_assets/80351022caecb6c03b77.png)

Benzer şekilde buradaki tüm butonların tıklandığında yapması istenen işlemlerin *DbOperation* özelliği ile ayarlanması gerekmektedir.

![](../_assets/2aebce1bfb27514f6cf2.png)

Sonrasında tablomuzda bulunan alanlar için form üzerine gerekli bileşenleri ekleyeceğiz. Sıra, Firma Kodu, Firma Unvan, Görüşeceği Kişi, Ziyaretçi Ad, Ziyaretçi Soyad, Kart No alanları için TDBNEdit tipinde bileşenler eklenecektir. TDBNEdit bileşeninde *DataField* özelliğine tabloda bu alanın karşılık geldiği alan seçilecektir.

![](../_assets/ce9e750a03fa0bf5080f.png)

Tip alanı için TDBRadioGroup bileşeni kullanabiliriz, bu alanda ziyaretçinin tipini seçiyor olacağız bu alan veritabanında Kişi-0, Özel Araç-1, Kamyon-2, Tır-3 şeklinde sayısal olarak tutulmaktadır.

Bu eşleştirmeyi yapabilmek için öncelikle TDBNEdit bileşeninde olduğu gibi *DataField* özelliğinde verinin tutulduğu tablo sahasını seçiyor olacağız. Ardından *Items* özelliğinde ekran üzerinde görünecek Kişi, Özel Araç, Kamyon ve Tır değerlerini satır satır tanımlayacağız.

*Values* özelliğinde ise *Items* özelliğinde yazılan değerlerle aynı sırada bu seçeneklere karşılık gelen ve veritabanında kullanılacak olan değerler girilecektir. Bu örnekte 0,1,2,3 olacak şekilde satırlar giriliyor olacaktır.

Firma Kodu ve Kart No alanlarının yanında bu değerlerin getirileceği birer rehber butonu eklenmiştir. Öncelikle rehber tanımlarının Genel\\NDI\\Kayıt\\Rehber Tanımlama ekranından yapılması gerekmektedir.

![](../_assets/3a43d76540b909e7c350.png)

Kart No rehberi için RHB00002 kodu ile yeni bir tanımlama gerçekleştiriyoruz. Açıklama alanında bu rehber için görülecek açıklama bilgisi verilecektir. Veritabanı bağlantı kodu alanında rehberde kullanılacak alanların getirileceği tablonun bulunduğu veritabanına yapılacak bağlantı kodu yazılacaktır. Tablo adı alanında rehberde kullanılacak olan tablo bilgisi verilecektir. Grup Kodu alanında Genel\\NDI\\Kayıt\\Grup Kodu Tanımlama ekranında tanımlanan grup kodlarından birisi yazılabilir, zorunu bir bilgi değildir. Kısıt alanında verilecek kısıt ile tablodan tüm satırlar yerine sadece istenen satırların gelmesi sağlanabilir. Tuş alanında da atanacak olan tuş bilgisi yazılabilir, zorunlu bir bilgi değildir.

![](../_assets/23e59eca5841f8a36092.png)

Temel rehber tanımlarını tamamladıktan soran Rehber Detay sekmesinden rehberde yer alacak, rehber açıldığında odaklanılacak ve rehberden seçim yapıldığında NDI formuna geri döndürülecek alanların tanımlaması yapılacaktır.

Rehber üzerinde seçilen alanlar Gösterim Sırası alanında belirtildiği sırada gösterilecektir. Alan Adı seçim kutusunda Rehber Tanımlama sekmesindeki Tablo Adı alanında yazılan tablonun alanları yer alacaktır, kullanıcı rehberde görünmesini istediği alanı buradan seçecektir. Odakla seçeneği işaretlendiğinde, rehber ekranda getirildiğinde otomatik olarak imlecin odaklanacağı alan seçimi yapılmış olacaktır. Her rehberde sadece bir saha için Odakla seçeneği işaretlenebilmektedir. Dönüş seçeneği işaretlendiğinde ise dönüş olarak işaretlenen alanın değeri rehberden seçim yapıldığında NDI formu üzerine döndürülecektir. Açıklama alanına yazılan bilgi rehberin başlığında gösterilecektir. Yapılmış olan rehber tanımlamaları Rehber Test butonu tıklanarak izlenebilmektedir.

![](../_assets/a869b407f5eb71f76716.png)

Rehber tanımlamaları yapıldıktan sonra NDI formu üzerine yerleştirilen TNDIRehberBtn bileşeninin *RehberKodu* özelliği tanımlanan rehberler arasından seçilebilir.

*LUCustEditAck* özelliği ile rehberden seçilen satırdaki değerin NDI formu üzerindeki hangi alana döndürüleceği seçilecektir. *LUCustomEdit* özelliği ise rehberden form üzerine bir değer döndürüldükten sonra imlecin hangi alana odaklanacağını belirlemektedir.

![](../_assets/757930ad7c246dd115cc.png)

\*51\*Giriş ve Çıkış Tarihi alanlarında yer alan tarih ve saat bilgileri için TDBDateTime bileşeni kullanılmıştır. Giriş Tarihi için eklenen iki adet TDBDateTime bileşeni kullanılmıştır, bu alanların birinde GIRISTAR alanındaki bilgide yer alan tarih bilgisi, diğer bileşende ise yine aynı GIRISTAR alanındaki bilgide yer alan saat bilgisi gösterilmektedir. Bu tanımlamaları yapabilmek için her iki TDBDateTime bileşeninin de DataField özelliğini GIRISTAR olarak seçmek gerekmektedir. Bu alanların birinde tarih, birinde saat bilgisini gösterebilmek için ise tarih olarak gösterilecek bileşenin *Kind* özelliğinde dtkDate ve saat olarak gösterilecek bileşenin *Kind* özelliğinde ise dtkTime değeri seçilmelidir.

Mevcut kayıtları NDI formu üzerinde gösterebilmek için bir TNDINetsisCxGrid bileşeni ekliyor olacağız. Burada bahsedilen grid yerine NDI'da desteklediğimiz diğer gridler de kullanılabilir.

![](../_assets/31fa49a0311b2ef2c745.png)

TNDINetsisCxGrid bileşeninin kullanılabilmesi için öncelikle *ColCount, DbConnectionCo, GridSql ve NetColumns* özelliklerinin ayarlanmış olması gerekmektedir. Gridde gösterilmesi istenen saha sayısı *ColCount* özelliğinde belirtilmelidir. *DbConnectionCo* özelliğinde ise rehber ve form alanlarının belirlenmesinde olduğu gibi verilerin grid üzerine getirileceği veritabanı bağlantı kodu yazılacaktır. *GridSql* özelliğine yazılacak olan sorgu sonucunda gelen değerler grid üzerinde gösterilecektir. Bu örneğimizde "SELECT \* FROM ZIYARETCI " sorgusunu kullanıyor olacağız. Sorgu sonucunda dönen sahalar arasında hangilerinin grid üzerinde gösterileceği ve alan bazlı detaylar ise *NetColumns* özelliğinde tek tek kolon kolon tanımlanacaktır. Alan bölümünde sorgu sonucunda dönen alanlar yer alacaktır, kullanıcı grid üzerinde görünmesini istediği alanları görünmesini istediği sırada bu alanda tanımlaması gerekecektir.

Başlık bilgisinde grid üzerinde en üstte birinci sırada yer alan başlık satırında bu alan için görüntülenecek açıklayıcı bilginin yazılması gerekmektedir.

\*52\*Kontrol bileşeni özelliğinde bu alanın form üzerinde hangi DBNEdit tipli alana karşılık geldiği seçilecektir, bu seçim yapıldığında kullanıcı grid üzerinden çift tıklayarak bir satır seçimi yaptığında, ilgili satırdaki değerleri form üzerinde de eşleştirilen alanlara otomatik olarak atanacaktır.

![](../_assets/fb69a584e0c88ae7a98f.png)

Değiştirilebilir özelliği ise bu alanın kullanıcı tarafından grid üzerinden değiştirilip değiştirilemeyeceğini belirlemektedir. Değiştirilebilir olarak işaretlenen alanları kullanıcılar grid üzerinden değiştirebilecektir.

Son olarak NDI formları üzerinde dinamik kodlamalar ile de geliştirmeler yapılabilmektedir, dinamik kodlama ile ilgili detayları {+}https://docs.logo.com.tr/pages/viewpage.action?pageId=50680277+ kullanıcı destek dokümanında da inceleyebilirsiniz.

NDI formumuz üzerinde dinamik kodlama girişi yapılmak isteniyorsa ilgili ekrana dizayn ortamında, form üzerinde sağ tık menüsünden "Dinamik Kod Girişi" menüsü ile veya formun sol üstüne tıklayarak "Netsis Script Kod Desteği" menüsünden erişebiliriz.

![](../_assets/0dbb7c0f79d305827d11.png)![](../_assets/2a14befb2294d8a78fe0.png)

Örneğin form üzerindeki firma kodu alanına elle bir cari kodu yazılıp sekme tuşu (Tab) ile alandan çıkıldığında eğer cari kod Netsis'de kayıtlı bir cari kodu ise carinin ismini kullanıcıya mesaj olarak çıkartıp ardından Firma Ünvan alanına cari ismin getirilmesini, cari kayıtlı değilse cari kodu alanına odaklanarak kullanıcının bu alandan çıkamamasını sağlayabiliriz.

![](../_assets/6e631c88b58e1be985af.png)

NDI'da yazılacak dinamik kodlamalar içerisinde NetopenX nesnesi kullanılarak da sorgular geliştirilebilir.
