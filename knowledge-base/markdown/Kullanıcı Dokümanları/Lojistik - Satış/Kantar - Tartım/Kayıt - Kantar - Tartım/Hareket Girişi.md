---
title: "Hareket Girişi"
page_id: "22804234"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Kantar - Tartım"
  - "Kayıt / Kantar - Tartım"
  - "Hareket Girişi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Kantar - Tartım / Kayıt / Kantar - Tartım / Hareket Girişi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTM4YWE5NzgxLTJjNjYtNDdkMS1iOTVhLThhYmU2NjczZGEyNCZsaW5rPWVmMTA1MTJhLWY4ZDMtNDdiOS1iNDBiLWU0ZjgwMDg1NmY5MSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=38aa9781-2c66-47d1-b95a-8abe6673da24&link=ef10512a-f8d3-47b9-b40b-e4f800856f91&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "hareket-girisi_28149349_22804234.html"
source_version: "2022-10-25T13:14:50.633+03:00"
source_bytes: 84539
fetched_at: "2026-09-13T04:06:52+00:00"
generator: "netsis-scraper 1.0.0"
---
# Hareket Girişi

Kantar Tartımı Hareket Girişi, Lojistik - Satış Bölümü'nde Kayıt/Kantar-Tartım menüsünün altında yer alır. Programa girilen parametreler doğrultusunda tartım kayıtlarının oluşturularak programa entegre edilmesini sağlar.

Bu bölüme ilk girişte, tartım kayıtlarını oluşturan operatörün adı ve kantar kodunun sorgulandığı "Operatör Girişi" ekranı açılır. Operatör adı boş geçilemez, ad girilmeden kantar modülüne geçiş yapılamaz. Sorgulanan alanlara bilgi girişi yapıldıktan sonra, "Hareket Tartım Girişi" sekmesi ile devam edilir.

Kantar Tartımı Hareket Girişi ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Hareket Girişi Ekranı |  |
| --- | --- |
| Kantar Kodu | "Operatör Girişi" ekranında tanımlanan kantar kodunun girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, kantar kodları arasından seçim yapılır. |
| Kamyon Plakası | "Kamyon Sabit Bilgileri" bölümünden kaydedilen kamyon plakasının girildiği alandır. Bu alana daha önce tanımlanmamış olan kamyon plakası girilemez. Kamyon plakası tartım fişi kayıtlarına ve basımlarına aktarılır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, kamyon plakaları arasından seçim yapılır. Kamyon plakası girildikten sonra (ilk tartım olduğu durumlarda) parametrelerde “Dara Aktarım” parametresi işaretlenmişse, “Dara İlk Tartıma Aktarılsın Mı” şeklinde bir uyarı ekranı açılır. Bu ekranda, "Evet" butonuna tıklandığında, "Kamyon Sabit Bilgileri" bölümünden kaydedilen kamyonun darası, "İlk Tartım Değeri" alanına aktarılır. |
| Farklı Mal/Cari Hesap Kodu | "Farklı Mal/Cari Teslim Sorgulansın" seçeneğinin işaretlenmesi halinde teslimatla ilgili tercihin yapıldığı alandır. Tartımın carilere göre dağıtımı ve stok koduna göre seçilmesi istendiğinde (özellikle, aynı kamyonla farklı carilere sevk veya aynı kamyonla farklı malların sevki işlemlerinde kullanılır) bu alan işaretlenir ve tartım sonrası irsaliye oluşturma ekranından dağıtımlar yapılır. |
| ![](../../../../_assets/83945eabafe577916cb0.png) Son Tartımı Aktar | Son tartımın ilk tartıma aktarılması istendiğinde kullanılan butondur. |
| Cari Kodu | "Farklı Mali/Cari Teslim Sorgulansın" seçeneğinin işaretlenmemesi durumunda aktif olan alandır. Tartım kaydının aktarılacağı irsaliye için, müşteri ya da satıcı kodunun girildiği alandır. Carinin ismi sağ bölümdeki "Cari İsim" alanından izlenir. "Kamyon Sabit Bilgileri" bölümünde plaka bilgisi ile birlikte tanımlanan cari kod, "Kamyon Plakası" alanına bilgi girişi yapıldıktan sonra \<tab\> tuşu ile ilerlendiğinde otomatik olarak ekrana getirilir. Üzerinde değişiklik yapılabilir. |
| Stok Kodu | "Farklı Mali/Cari Teslim Sorgulansın" seçeneğinin işaretlenmemesi durumunda aktif olan alandır. Tartım kaydının aktarılacağı irsaliye için stok kodunun girildiği alandır. Stokun ismi sağ bölümdeki "Stok İsmi" alanından izlenir. |
| Kamyon Modeli | "Kamyon Sabit Bilgileri" bölümünde plaka bilgisi ile birlikte tanımlanan kamyon modeli, "Kamyon Plakası" alanına bilgi girişi yapıldıktan sonra \<tab\> tuşu ile ilerlendiğinde otomatik olarak ekrana getirilir. Üzerinde tartım girişi için değişiklik yapılması istendiğinde, kullanıcı tarafından düzenleme yapılabilir. |
| Açıklama 1-2-3 | Kantar-Tartım Parametrelerinde bulunan “Ek Açıklama Sorulsun” parametresinin işaretlenmesi halinde aktif hale gelen alanlardır. En fazla 50 karakterlik açıklama girilebilir. |
| Şoförün Adı | "Kamyon Sabit Bilgileri" bölümünden, kamyon plakasına göre girilen şoför adının otomatik olarak aktarıldığı alandır. Üzerinde tartım girişi için değişiklik yapılması istendiğinde, kullanıcı tarafından düzenleme yapılabilir. |
| İlk/Son Operatör Adı | İlk/Son operatör adının izlendiği alandır. Program tarafından otomatik aktarılır. Üzerinde değişiklik yapılamaz. |
| İlk/Son Kantar Kodu | İlk/Son kantar kodunun izlendiği alandır. Program tarafından otomatik aktarılır. Üzerinde değişiklik yapılamaz. |
| Tartım Numarası | Tartım numarasının izlendiği alandır. Program tarafından otomatik aktarılır. Üzerinde değişiklik yapılamaz. |
| Geliş Tarihi | Kamyonun tartıma geliş tarihidir. Program tarafından otomatik aktarılır. Üzerinde değişiklik yapılamaz. |
| Geliş Saati | Kamyonun tartıma geliş saatidir. Program tarafından otomatik aktarılır. Üzerinde değişiklik yapılamaz. |
| Gidiş Tarihi | Kamyonun tartımdan çıkış tarihidir. Otomatik olarak sistemden atanacaktır. Kullanıcılar bu sahaya ulaşamaz. |
| Gidiş Saati | Kamyonun tartımdan çıkış saatidir. Program tarafından otomatik aktarılır. Üzerinde değişiklik yapılamaz. |
| İlk Tartım Değeri | Kantardan aktarılan ya da tartım girişinde kullanıcıların kaydettiği ilk tartım miktarının aktarıldığı alandır. Kamyonun darası bu alana aktarılmışsa üzerinde değişiklik yapılamaz. Eğer [Kantar-Tartım Parametreleri](<Kantar - Tartım Parametreleri.md>)nde bulunan “Kantardan Miktar Okunsun” parametresi işaretlenmişse, ilk tartım miktarı kantardan okunarak, ilk tartım miktarı alanına aktarılır. |
| Son Tartım Değeri | Kantardan aktarılan ya da tartım girişinde kullanıcıların kaydettiği son tartım miktarının aktarıldığı alandır. Kamyonun ilk tartımında bu alana ulaşılamaz. |
| Fire Oranı | Fire verilen oranın girildiği alandır. |
| İrsaliye Kesilmiş | İrsaliyesi oluşturulmuş tartımlarda bu alan program tarafından işaretlenmiş olarak ekrana gelir. |
| Kantardaki Sayı | Son tartım miktarı ile ilk tartım miktarının farkının izlendiği alandır. Program ilk tartım kayıtlarını kamyon plakalarına göre kayda alır. Arka arkaya tartıma giren kamyonların, ilk tartım bilgileri ayrı plakalara göre oluşturulabilir. İlk tartım bilgilerinin düzeltme yada iptalleri "Hareket Düzeltme" bölümünden gerçekleştirilir. Kamyonların boşaltım yada yüklemeleri yapıldıktan sonra yapılan ikinci tartım işlemi ile irsaliye kayıtlarının oluşturulması aşamasına geçilir. |
| ![](../../../../_assets/da77c3cd37ae9a57f11d.png) Tartım Tamamla | Son Tartım, gidiş tarihi ve saatinin manuel olarak düzenlenmesini sağlayan butondur. ![](../../../../_assets/3096809437cd75b3454d.png) |

Kamyonun yüklenmesi/boşaltımı yapıldıktan sonra tekrar kantardan yapılan kayıtlar ikinci tartım olarak işlenir. İlk tartım kaydı olan bir kamyon plakası tekrar ekrana çağrıldığında, program bunu ikinci tartım kaydı olarak algılar ve ilk tartım bilgileri ekrana yansır. "Kamyon Plakası" alanındaki rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, ilgili kamyon plakası girildiğinde, bu kamyona daha önce girilen ilk tartım değeri, ilk tartım tarihi ve saati ekrana yansır. Program tekrar farklı mal/cari teslimat alanına bilgi girişi yapılmasını ister. Bu alanlara ikinci tartım için gereken bilgiler girildikten sonra, ekrana son tartım kayıtlarına geçileceğinin uyarısı gelir.

Kantar-Tartım Parametrelerinde bulunan "Kantardan Miktar Okunsun" alanı işaretlenmişse, kantardaki makineden ikinci tartım değeri, ilgili alana aktarılır. Eğer bu parametre işaretlenmemişse tartım bilgilerinin girileceği yeni bir ekrana geçilir. Daha önce girilen ilk tartım değeri, "İlk Tartım" alanına aktarılmış olarak izlenebilir. İlk tartım değeri üzerinde herhangi bir değişiklik yapılamaz. Bu bölümde İkinci tartım değerleri girilir. Girilen tartım bilgilerinin arasındaki farkın değerine göre, stoklara giriş/çıkış kaydı program tarafından otomatik olarak oluşturulur. Eğer son tartım ilk tartım değerinden daha büyükse, aradaki fark (-) olur ve program bu kaydı çıkış olarak değerlendirerek satış irsaliyesi oluşturur. Eğer son tartım ilk tartım değerinden daha küçükse, aradaki fark (+) olur ve program bu kaydı giriş olarak değerlendirerek alış irsaliyesi oluşturur.

İkinci tartım değerleri girildikten sonra program tekrar “Miktardan Emin misiniz” uyarısı ile işleme devam edebilmek için onay bekler. Yanıt olarak "Hayır" butonuna tıklandığında, tekrar tartım değerlerinin girildiği ekrana dönülür. "Evet" butonuna tıklandığında ise, dağıtım ve irsaliye oluşturma işlemlerine devam edilir. Kantar-Tartım Parametrelerinde bulunan "İkinci Tartım Basılsın" alanı işaretlenmişse, ikinci tartımın basımı yapılabilir.

Program tartım değerleri arasındaki fark eksi (-) ise irsaliye oluşturma ekranından "satış irsaliyesi" oluşturmak üzere sorgulama yapacağı alanları ekrana getirir.

Kantar Tartımı Hareket Girişi İrsaliye ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Hareket Girişi Ekranı | İrsaliye |
| --- | --- |
| Plaka No | Tartım bilgilerinin girişinde kullanılan plaka numarasının otomatik olarak aktarıldığı alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile plaka numaraları arasından seçim yapılır. |
| Belge Tipi | Tartım bilgilerinin girişinde kullanılan belge tipinin otomatik olarak aktarıldığı alandır. |
| Numara | Program tarafından satış irsaliyesi numarasının bir fazlasının aktarıldığı alandır. Kullanıcı istediğinde üzerinde değişiklik/düzeltme yapabilir. "Alış İrsaliyesi" oluşturma işlemlerinde ise bu alana alış irsaliyesinin numarası girilir. Değişiklik veya düzeltme işleminin yapılabilmesi için [Kantar-Tartım Parametreleri](<Kantar - Tartım Parametreleri.md>)nde bulunan "İrsaliye No Düzeltme" parametresinin işaretlenmiş olması gerekir. |
| İrsaliye Tarihi | Satış irsaliyeleri için sistem tarihinin otomatik olarak aktarıldığı alandır. Alış irsaliyelerinde ise gelen irsaliyenin tarihinin girilmesi gerekir. |
| Tartım No | İçinde bulunulan tartımın numarasının aktarıldığı alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile tartım numaraları arasından seçim yapılabilir. |
| Cari Kodu | İrsaliyenin oluşturulduğu müşteri/satıcının kod bilgisinin girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile cari kodlar arasından seçim yapılır. Cari isim alanına, cari kodun ismi program tarafından otomatik olarak aktarılır. |
| Stok Kodu | Tartım kaydının oluşturulacağı stok kodu bilgisinin girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile stok kodları arasından seçim yapılır. Stok adı alanına, koda ait isim bilgisi program tarafından otomatik olarak aktarılır. |
| Ek Alan | Anlık açıklama bilgisinin girildiği alandır. [Kantar-Tartım Parametreleri](<Kantar - Tartım Parametreleri.md>)nde bulunan "Ek Açıklama Sorulsun" parametresinin işaretlenmesi ile ekrana gelir. |
| Sipariş No | [Kantar-Tartım Parametreleri](<Kantar - Tartım Parametreleri.md>)nde bulunan "Sipariş Entegre Yapılsın" parametresi işaretlendiğinde, ekrana gelen alandır. Sipariş numarasının girilmesini sağlar. Bu işlemlerden önce sipariş bilgilerinin, Fatura → Kayıt → [Müşteri](<../../Fatura/Kayıt - Fatura/Müşteri Siparişleri.md>)/[Satıcı Siparişleri](<../../Fatura/Kayıt - Fatura/Satıcı Siparişleri.md>) bölümünden girilmiş olması gerekir. Sipariş bağlantı kayıtlarının oluşturulmasında, sipariş kaydında girilen miktar ile tartım miktarı arasında bir farkın olmaması gerekir. Eğer arasında (-) bir fark çıkarsa (sipariş miktarından fazla tartım yapıldı ise) program, aradaki farkın kapatılması yapılmadan işleme devam edilmesine izin vermez. Sipariş kaydına tartımdan aktarılan bilgi ise teslimat olarak işlenir ve sipariş kapatılmış olur. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile sipariş numaraları arasından seçim yapılabilir. Alanın boş bırakılması istendiğinde [Kantar-Tartım Parametreleri](<Kantar - Tartım Parametreleri.md>)nde bulunan "Sipariş No Boş Bırakılsın" parametresinin işaretlenmesi gerekir. |
| ![](../../../../_assets/9fa7184e6bce531ef983.png) Sipariş Detay | Siparişe ait detay bilgilere ulaşmak için kullanılan butondur. İlgili irsaliyeye ait "Üst Bilgiler" sekmesinde yer alan bilgilerin ekranda görüntülenmesini sağlar. |
| Depo Kodu | Siparişe ait depo kodu bilgisinin program tarafından otomatik olarak aktarıldığı alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile depo kodları arasından seçim yapılabilir. |
| Referans Kodu | Referans kodunun girildiği alandır. |
| ![](../../../../_assets/8d6ceb4b12f29f521409.png) Tartım Miktarını Getir | Tartım miktarlarının otomatik olarak "Miktar" alanına aktarılmasını sağlayan butondur. Üzerine çift tıklandığında işlem gerçekleşir. Tek tıklama yapıldığında, Miktarı Siparişten Getir ![](../../../../_assets/10ed6325207a223ce854.png) butonuna çevrilir. |
| ![](../../../../_assets/22ee89c00bc10af410f7.png) Miktarı Siparişten Getir | Miktar bilgisinin siparişten okunarak "Miktar" alanına aktarılması istendiğinde kullanılan butondur. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilgilerin kaydedilmesini sağlayan butondur. İrsaliye tamamlama ekranına geçilerek işleme devam edilir. Oluşturulan irsaliyenin içinde kayıtlı olan stok kartlarına fiyat bilgisi girilirse, tutar hesaplanarak aktarılan irsaliye dosyasına tutar bilgisi aktarılır. Kayıt sonunda, program tarafından irsaliyenin basımı ile ilgili onay sorusuna "Evet" yanıtı verildiğinde, "[Dizayn Modülü](<../../../Genel/Dizayn Modülü/index.md>)" ile oluşturulan dizayna göre basım yapılır. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır.

Kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.

Burada tartım bilgilerinin oluşturulması sırasında girilen farklı yanıtlara göre kayıtlar farklı türlerde kaydedilebilir.

Farklı Mali/Cari Teslimatı işaretlenmediği ve tartım kayıt ekranından cari kodu ve stok kodunun girildiği durumlarda; tartım numarasının üzerinden \<tab\> tuşu ile ilerlendiğinde, ön ekrandan girilen bilgiler otomatik olarak ilgili alanlara aktarılır.

Farklı Mali/Cari Teslimatı parametresi işaretlenmiş ve tartım girişi ekranında cari kodu-stok kodu alanları boş geçilmişse; İrsaliye Oluşturma ekranında cari kodu, stok kodu ve miktar alanları boş olarak izlenebilir ve kullanıcılar tartım kaydını istenen cari, stok kodu ve miktara göre dağıtabilir. Dağıtım işleminde tartım miktarı ile dağıtım miktarı arasında fark varsa, program “ Lütfen Fark Miktarını Kapatın” şeklinde bir uyarı ile irsaliye kayıtlarına ulaşılmasına izin vermez. [Kantar-Tartım Parametreleri](<Kantar - Tartım Parametreleri.md>)nde bulunan “İrsaliyede Miktar Düzeltilsin” parametresi işaretlenmişse, tartım miktarı ile dağıtım miktarı arasındaki fark kontrol edilmez ve işleme devam edilir.
