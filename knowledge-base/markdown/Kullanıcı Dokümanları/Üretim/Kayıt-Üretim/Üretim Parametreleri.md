---
title: "Üretim Parametreleri"
page_id: "50663922"
product: "netsis-3-enterprise"
depth: 4
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Üretim"
  - "Kayıt/Üretim"
  - "Üretim Parametreleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Üretim / Kayıt/Üretim / Üretim Parametreleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTEwMmE4YmE4LWI4MTgtNDE0YS1hNTcyLTFiZDY2MTZjZTM3NyZsaW5rPTZmMzA0YTE0LWRlY2QtNGZiYS1iM2Y4LTRiZThhZTUyOTlmMCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=102a8ba8-b818-414a-a572-1bd6616ce377&link=6f304a14-decd-4fba-b3f8-4be8ae5299f0&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "uretim-parametreleri_50663931_50663922.html"
source_version: "2022-10-13T12:27:13.073+03:00"
source_bytes: 47883
fetched_at: "2026-09-13T04:19:02+00:00"
generator: "netsis-scraper 1.0.0"
---
# Üretim Parametreleri

Üretim Parametreleri, Üretim modülünde Kayıt/Üretim menüsünün altında yer alır. Üretim Modülü ile ilgili parametre tanımlarının yapıldığı bölümdür. Üretim, Üretim-2 ve Muhasebe olmak üzere üç sekmeden oluşur.

**Üretim**

Üretim Parametreleri ekranı Üretim sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Üretim Parametreleri Ekranı |  |
| --- | --- |
| Maliyet Tipi | Tüm modül dahilinde, herhangi bir kayıt veya listelemede, hammadde maliyetlerinin hesaplanacağı maliyet türünün belirlendiği parametredir. Yarı mamul ve mamul maliyetleri de hammaddelerin maliyetleri baz alınarak, ürün ağacında belirtilen miktarlara göre hesaplanır. Üretimde hesaplanan maliyetler anlık olup dönem içinde yanlış maliyettir. Üretim maliyet hesaplaması için stoktaki tüm maliyet metotlarını destekler. |
| İkame Maliyet Tipi | Hammaddenin herhangi bir zamanda, yukarıda belirtilen maliyet türü üzerinden maliyetinin sıfır olduğu durumlarda, programın hesaplama yapacağı maliyet türünün belirlendiği parametredir. Program, hammadde maliyetini önce maliyet türü üzerinden, 0 (Sıfır) olması durumunda ise ikame maliyet türü üzerinden, bu da 0 (Sıfır) ise alış fiyatı üzerinden otomatik olarak hesaplar. |
| İş Emriyle Reçete Sakla | İş emri ile üretim takibi yapan işletmeler için, iş emrinin açıldığı sırada, mamul reçetesini anlık hali ile saklamak ve daha sonra ilgili iş emri üretiminin, saklanan reçete üzerinden yapılmasını sağlamak için kullanılan parametredir. Özellikle ürün reçetelerinin sıklıkla değiştiği işletmelerde, iş emrinin verildiği ve üretim ambarına çıkışların yapıldığı gün itibariyle reçetenin saklanıp, üretimin tamamlandığı gün, Üretim Sonu Kaydını, ilgili reçete ile yapmak için kullanılır. |
| Eksi Bakiye Kontrolü | Üretimi yapılan mamulün reçetesinde kullanılan yarı mamul ya da hammadde stok seviyelerinin kontrol edilerek kullanıcının uyarılmasını sağlayan parametredir. Eksi Bakiye Kontrolü ile, istendiği zaman işleme son verilerek, üretim kayıtlarının stok hareketlerine aktarılmaması sağlanır. Eksi bakiyelerin kontrolünden sonra bu bölüm tekrar çalıştırılarak Üretim Sonu Kaydı yapılabilir. Parametrenin işaretlenmemesi durumunda ise, reçeteye tabi bileşenlerin stok seviyeleri kontrol edilmez ve program tarafından herhangi bir uyarı verilmez. |
| Eksi Bakiyede İşlemi Durdur | Üretim Sonu Kaydı yapıldığında eksi bakiyeye düşüldüğü zaman işlemin durdurulmasını ve kayıt yapılmasını önleyen parametredir. |
| Üretim Fişlerinde Seri Takibi | Üretim yapan firmalarda, farklı serilere sahip bir hammaddede hangi serinin hangi mamuller için kullanıldığı, hangi mamul serisinin hangi serilere sahip hammaddelerden oluştuğu gibi bilgilere, Üretim Modülünde yapılacak Seri Uygulaması ile ulaşılır. Üretim Modülünde, Seri Uygulamasının yapılması için, Serbest Üretim Sonu Kaydı bölümünün kullanılması gerekir. Üretim Modülündeki Üretim Sonu Kaydı işlemi otomatik olarak yapılır ve kullanıcıların müdahalesi söz konusu değildir. Lakin, Seri Uygulamasında seri numaralarının elle (Manuel) girilmesi de gerekeceği için, kullanıcıların müdahale edebileceği bir bölümden üretim kayıtlarının gerçekleştirilmesi gerekir. Bu nedenle Seri Uygulaması yapan firmalar, üretim kayıtlarını "Serbest Üretim Sonu Kaydı" bölümünü kullanarak yapması gerekir. Seri ekranında, seri parametre kayıtları ve stok kartlarında verilen seri kısıtları doğrultusunda, seri numaraları ya otomatik oluşturulur ya da kullanıcılar tarafından elle (Manuel) girilir. Seri numaraları otomatik oluşturuluyorsa, üretilen mamul kodu için - üretim miktarı 1 - 1 adet yeni seri numarası oluşturulur. "Fiş Üret" butonuna tıklandığında, ilgili mamul için kullanılacak hammadde veya yarı mamuller miktarlarıyla beraber grid ekranda görünür. İstenirse hammadde ve yarı mamuller grid ekrandan seçilerek/grid ekrana getirilerek seri numaraları elle değiştirilebilir. Bu işlem sonunda üretilen mamul kodunun seri numarası, bu mamulün reçetesindeki bileşen kodlarının seri hareket dosyasında tutulan Karşılık Kodu alanına aktarılır. Böylece, mamul seri kodunun hangi hammadde ve yarı mamullerde kullanıldığı, hangi hammadde veya yarı mamulün hangi mamul seri kodu için kullanıldığı raporlanır. > [!NOTE]<br>> Üretim Sonu Kaydında mamulün 1 birim üretilmesi gerekir. Çünkü, hammadde veya yarı mamuller için karşılık koduna 1 adet seri numarası işlenebilir. Eğer mamul üretim miktarı birden fazla ise, bu durumda oluşan mamul seri numaraları bileşen kodlarına aktarılmaz. Dolayısıyla, üretilen mamul miktarı kadar seri numarası oluşturuluyorsa sistemin doğru olarak işlemesi mümkün değildir. Bu nedenle mamullerin birer birer üretilmesi gerekir.<br>><br>> Ancak, üretilen mamul - boya gibi - miktarı - 100 kg. gibi - ne olursa olsun, mamule 1 adet seri numarası veriliyorsa sistem yine doğru olarak işler.<br>><br>> **Örneğin;**<br>><br>> 100 kg. boya için hesaplanan seri numarası bileşen kodlarının karşılık kodlarına aktarılır. |
| 2.Miktar Girilecek | Üretim Sonu Kayıtlarında, mal kalemleri bazında, üretime esas miktar dışında ikinci bir miktar kaydı yapılması ve izlenmesi için kullanılan parametredir. Genellikle, malların iki ölçü birimi olup, aralarındaki çevrimin belli olmaması, üretim bazında değişmesi durumunda kullanılır. **Örneğin;** Üretimin adet bazında yapıldığı ve üretim kaydı sonunda gerçekleşen mamullerin koli olarak paketlendiği varsayıldığında, mal kalemleri bazında adet olarak üretilen mamulün kaç koli yaptığı "2. Miktar" alanında girilebilir ve takip edilebilir. Bunun dışında, eğer Fire Uygulaması parametresi işaretlenmiş ise malların fire miktarları 2. miktar sahasına girilecektir. Bu durumda, 2. miktar sahası başka bir amaçla kullanılamayacaktır. |
| Üretimde İş Emri Kontrolü | İş emrine bağlı üretim yapan firmalarda, Üretim Sonu Kayıtlarının iş emri numarası girilmeden yapılmasının engellenmesi için kullanılan parametredir. Bu durumda, Üretim Sonu Kayıtları yapılırken program, iş emri numarasının girilip girilmediğini kontrol eder. Girilmediğinde, Üretim Sonu Kaydının yapılmasına izin verilmez. Parametre işaretlenmediği zaman, iş numarası kontrolü yapılmaz. İş emri girilmeden de Üretim Sonu Kayıtları yapılabilir. |
| Katı Madde Uygulaması | Katı Madde Uygulaması, üretim sırasında kullanılan hammaddelerin uçma (Havaya karışma) özelliği olduğunda kullanılan parametredir. Bazı mamullerin üretiminde kullanılan hammaddeler (Aseton, eter, tiner gibi), reçetede tanımlanan miktarları ne olursa olsun, belli oranlarda üretim sırasında havaya karışır. Dolayısıyla, reçetede tanımlanan miktarlarından daha azı mamule karışır. Katı Madde Uygulamasında, bu tür uçucu hammaddelerin stok kartlarında ayrılması ve uçma oranlarının stok kartlarına girilmesi gerekir. Bunun için, Stok → Stok Parametreleri → Kullanıcı Tanımlı Sahalar bölümündeki "Sayısal Saha Başlıklarından" herhangi birine "KATI MADDE" başlığının yazılması gerekir. Ayrıca, stok kartlarında bu başlığın karşısına uçma ya da kayıp oranının kaydedilmesi gerekir. Bu tanımlamaların yapılmasından sonra, Üretim Sonu Kaydı gerçekleştirildiğinde, hammaddeler için bu oranlar göz önünde bulundurularak uçma veya kayıp oranı bulunur. Reçeteler için hesaplanan bu oranlar, "Reçete Kaydı" ekranında iken farenin sağ tuşu ile ekrana gelen "Hammadde Toplam Bilgisi" raporundan izlenir. Böyle bir uygulama yoksa, bu parametrenin işaretlenmemesi gerekir. |
| Fire Uygulaması | Üretim sırasında kullanılan mamul, hammadde veya yarı mamullerin kırılması, dökülmesi veya bozulması durumunda, fireye giden bu miktarların takip edilmesi ve raporlanması için kullanılan parametredir. Fire Uygulaması, sadece "Serbest Üretim Sonu Kaydı" bölümünden yapılır. Nedeni ise, reçete miktarlarına ve bileşenlere sadece bu seçenekten müdahale edilmesidir. Fire miktarları Serbest Üretim Sonu Kaydında, "2. Miktar" alanına girilir. Hammadde ve yarı mamul bileşenlerinin, satır bazında "2. Miktar" alanına fire miktarı girildiğinde, fire miktarı da kullanım miktarına ilave edilir ve stok hareket kayıtlarına bu şekilde işlenir. Mamul üretim miktarında "2. Miktar" alanına fire miktarı girildiğinde ise, fire miktarı üretim miktarından düşülerek stoklara işlenir. |
| Ek Alan Kullanımı | Üretim Sonu Kaydı ekranlarına Ek Alan-1 ve Ek Alan-2 alanlarının eklenmesi için kullanılan parametredir. Serbest Üretim Sonu Kaydında, mamul ve bileşenler için girilen ek alan bilgileri, Üretim Sonu Kaydında yalnızca mamuller için girilebilir. Bu bilgiler, Stok Hareket Kayıtlarında iken farenin sağ tuşu ile ekrana gelen “Stok Diğer Bilgiler” ekranının "Diğer 2" sekmesinden izlenir. Böylece, "Ek Alan" sahaları kullanılarak raporlanır. Üretim Sonu Kayıtları sipariş bağlantılı yapıldığında ise, siparişte girilen ek alanlar aynen bu sahalara getirilir ve stok hareket kayıtlarına aktarılır. |
| Reçete Formül Toplamına Tamamlansın | Reçete kayıtlarında sorgulanan ve izlenebilen Reçete Toplamı ve Anlık Reçete Toplamı kavramları aşağıdaki şekilde açıklanabilir: "Reçete Toplamı", ürün ağacı girilen mamulün, bileşen miktarlarının kaç birim için tanımlandığı anlamındadır. Yani, "Reçete Toplamı" alanına 1 girildiği takdirde, 1 birim mamul için katsayılar şeklinde hammadde/yarı mamul miktarlarının işleneceği varsayılır. 1 dışında herhangi bir rakam girildiğinde hammadde/yarı mamul miktarlarının toplanarak reçete toplamını oluşturacağı düşünülür. "Anlık Reçete Toplamı" ise, Reçete Toplamı 1'den farklıysa - bileşen miktarlarının toplamı mamulün birim toplamını oluşturuyorsa - bu durumda reçeteye bileşen (Hammadde/yarı mamul) eklendikçe o anlık reçete toplamının ne olduğuna dair bilgi veren alandır. Kullanıcı elle müdahale edemez. Bu alan izlenerek girilen bileşen kayıtlarına göre, reçete toplamında tanımlanan rakamla, o anda erişilen toplam rakam kıyaslanabilir. "Reçete Formül Toplamı Tamamlansın" parametresi, Reçete Toplamı" ile "Anlık Reçete Toplamının" birbirinden farklı olması ve "Anlık Reçete Toplamının" "Reçete Toplamı" olarak kabul edilmesi durumunda kullanılması gerekir. Bu parametre işaretlendiğinde, program "Anlık Reçete Toplamı" ile "Reçete Toplamı" eşitlenmediği sürece kayıt yapmaz. Parametre işaretlenmediği zaman, her iki reçete toplamı eşit değil ise program uyarı verir ve kayıt yapılmasını sağlar. |
| Üretim Yapılan Depo Kodu (Öndeğer) | Lokal Depo Uygulamasını kullanarak, Üretim bölümünü depo olarak tanımlayan firmaların kullandığı parametredir. Bu alanda belirtilen Depo Kodu, Üretim Sonu Kayıtları sırasında öndeğer olarak getirilir. Kullanıcı isterse değiştirebilir. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile, depo kodları arasından seçim yapılır. |
| Üretim Sonu Kayıtlarında Barkodlu İşlem | Barkod cihazları ile çalışma yapan firmaların kullandığı parametredir. Bu uygulamada, stoklara ait barkod kodları, Stok Kartı Kayıtlarındaki "Barkod" alanına ya da "Barkod Kayıtları" bölümüne kaydedilir. Parametrenin işaretlenmesi ile birlikte Üretim Sonu Kaydı ve Serbest Üretim Sonu Kaydında, Stok Kodu yerine Barkod Kodu girilebilir. Program, barkod koduna ait stok kodunu bularak üretim sonu kayıtlarını yapar. |
| Rezervasyon Bakiyelerinin Takibi Yapılsın | Rezervasyon bakiyelerinin İş Emri, İş Emri Dengeleme ve Üretim Sonu Kaydı ekranlarında kontrol edilmesini sağlamak için kullanılan parametredir. Alanın sağ tarafında yer alan aşağı ok butonu ile seçim yapılır. |
| Üretim Çıkışlarda Fifo Seri Oluşsun | Üretim Sonu Kaydı sırasında sarf edilecek bileşenler için otomatik olarak FIFO seri kaydı oluşturulması için kullanılan parametredir. |
| İş Emrine Bağlı Üretimde Fazla Üretim Yapılabilsin | İş emrine bağlı üretimde fazla üretim yapılmasını sağlamak için kullanılan parametredir. Alanın sağ tarafında yer alan Fazla Üretim Oranı alanı, yapılacak fazla üretim oranının girilmesini sağlar. |
| Depolar Arası Transfer ve Ambar Çıkış Fişinde İş Emrine Ait Malzemelerin Bakiye Takibi Yapılsın | Depolar Arası Transfer ve Ambar Çıkış Fişinde iş emrine ait malzemelerin bakiye takibinin yapılması için kullanılan parametredir. |
| Reçete Kaydında Miktarın Otomatik Geleceği Alan | Reçete kaydında miktarın otomatik geleceği alanın seçildiği parametredir. Alanın sağ tarafında yer alan aşağı ok butonu ile alanlar arasından seçim yapılır. |
| Üretim Sonu Kayıtları Raporlarında Bakiye ve Maliyet Gösterilsin | ÜSK raporlarında bakiye ve maliyetlerin gösterilmesi için kullanılan parametredir. |
| İş Emri Reçetesi Saklanırken Reçeteyi Tek Seviye Sakla | İş emri reçetesi saklanırken reçetenin tek seviye olarak saklanması için kullanılan parametredir. |
| ÜSK'da Tek Seviyeli Reçete Kullan | Üretim Sonu Kayıtlarında tek seviyeli reçete kullanılmasını sağlayan parametredir. |
| Maliyet Sıfır Olduğunda Alış Fiyatı-1'e Göre Maliyet Hesapla | Maliyet sıfır olduğunda "Alış Fiyatı-1" alanına göre maliyetin hesaplanmasını sağlayan parametredir. |
| ÜSK'da Tarihsel Bakiyeye Bakılsın | Üretim Sonu Kayıtlarında tarihsel bakiyeye bakılması için kullanılan parametredir. |
| ![](../../../_assets/39d77b8716226638d9ce.jpg) Tamam | İşaretlenen parametrelerle ilgili işlemlerin gerçekleşmesini sağlayan butondur. > [!NOTE]<br>> Parametrelerle ilgili işlemlerin programa yansıması için programın kapatılıp tekrar açılması gerekir. |
| ![](../../../_assets/973111d004995dca0113.jpg) İptal | İşaretlenen parametrelerden vazgeçilmesi halinde kullanılan butondur. |

**Üretim-2**

Üretim Parametreleri ekranı Üretim 2 sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Üretim Parametreleri Ekranı |  |
| --- | --- |
| İş Emrine Bağlı ÜSK Girilmişse İlgili İş Emri İptal Edilemesin | İş emrine bağlı Üretim Sonu Kaydı girilmişse, ilgili iş emrinin iptal edilmesinin engellenmesi için kullanılan parametredir. |
| Rezervasyon/UAK/USK Varsa İş Emri Teslim Tarihi Değiştirilemesin | Rezervasyon, Üretim Akış Kontrol veya Üretim Sonu Kaydı varsa, iş emri teslim tarihinin değiştirilmesinin engellenmesi için kullanılan parametredir. |
| İş Emri Miktar Güncelleme Politikası | İş emri miktar güncelleme politikasının seçildiği parametredir. Parametrenin sağ tarafında yer alan aşağı ok butonu ile politikalar arasından seçim yapılır. |
| Kilitli Mamul Kodu Kontrolü Yapılsın | Üretim kayıtlarında kilitli mamul kodu kontrolünün yapılması için kullanılan parametredir. |
| Kilitli Bileşen Kodu Kontrolü Yapılsın | Üretim kayıtlarında kilitli bileşen kodu kontrolünün yapılması için kullanılan parametredir. |
| İş Emri Kalem Uygulaması | İş emri kayıtlarında kalem uygulamasının yapılması için kullanılan parametredir. |
| Alternatif Reçete Bilgisinin Müşteri Siparişinde Tutulacağı Saha | Alternatif reçete bilgisinin müşteri siparişinde tutulacağı sahanın belirlendiği parametredir. Parametrenin sağında bulunan alanın yanında yer alan aşağı ok butonu ile istenen saha seçilir. |
| Siparişe Bağlı İş Emri ve Üretimde Fazla Miktar Girilebilsin | Siparişe bağlı iş emri ve üretimde fazla miktar girilmesini sağlayan parametredir. |
| Rezervasyon Durumu Yayımlandı Olan İş Emirlerinin Miktarı Değiştirilmesin | Rezervasyon durumu "Yayımlandı" olan iş emirlerinin miktarının değiştirilmesinin engellenmesi için kullanılan parametredir. |
| Rezervasyon Durumu Yayımlandı Olan İş Emirlerinin Teslim Tarihi Değiştirilmesin | Rezervasyon durumu "Yayımlandı" olan iş emirlerinin teslim tarihinin değiştirilmesinin engellenmesi için kullanılan parametredir. |
| ÜSK'da Asgari Limit Kontrolü | Üretim Sonu Kaydında asgari limit kontrolünün yapılması için kullanılan parametredir. |
| İş Emirleri Kapatılırken Bağlantılı İş Emirleri de Kapatılsın | İş emirleri kapatılırken bağlantılı iş emirlerinin de kapatılması için kullanılan parametredir. |
| ÜSK'da Stok-Depo Kodu Kontrol Edilsin | Üretim Sonu Kaydında Stok ve Depo Kodunun kontrol edilmesi için kullanılan parametredir. |
| Serbest Üretim Sonu Kaydında Malzeme Serileri D.A.T Belgesinden Getirilsin | Serbest Üretim Sonu Kaydında malzeme serilerinin Depolar Arası Transfer belgesinden getirilmesi için kullanılan parametredir. |
| İş Emri Malzeme Rezervasyonu İşleminde FIFO Seri Oluştur | İş emri malzeme rezervasyonu işleminde FIFO serisinin oluşturulması için kullanılan parametredir. |
| Fire Girişinde Fire Kodu Sorulsun | Fire girişlerinde fire kodu sorgulamasının yapılması için kullanılan parametredir. |
| Üretim Kayıtlarında Aralık Bazında Fire Oranları Dikkate Alınsın | Üretim kayıtlarında aralık bazında fire oranlarının dikkate alınması için kullanılan parametredir. |
| ÜSK'da D.A.T Onayı Kontrol Edilsin | Üretim Sonu Kayıtlarında "Depolar Arası Transfer" onayının kontrol edilmesi için kullanılan parametredir. |
| ![](../../../_assets/39d77b8716226638d9ce.jpg) Tamam | İşaretlenen parametrelerle ilgili işlemlerin gerçekleşmesini sağlayan butondur. > [!NOTE]<br>> Parametrelerle ilgili işlemlerin programa yansıması için programın kapatılıp tekrar açılması gerekir. |
| ![](../../../_assets/973111d004995dca0113.jpg) İptal | İşaretlenen parametrelerden vazgeçilmesi halinde kullanılan butondur. |

**Muhasebe**

Üretim Sonu Kayıtları ile oluşacak stok hareketleri, “Üretim Sonu Kayıtları Entegrasyonu” işlemi ile muhasebeleştirilir. Bu işlem sırasında mamul ve hammadeler için hangi hesaplarının çalışacağı, "Muhasebe" sekmesinde seçilen parametrelere göre belirlenir. Bunun için mamul, yarı mamul ve hammaddelerin stok kartlarındaki "Muhasebe Detay Kodu" alanlarına kod girilmesi gerekir.

Üretim Parametreleri ekranı Muhasebe sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Üretim Parametreleri Ekranı |  |
| --- | --- |
| Mamul Hesabı | Muhasebeleştirilecek mamul hesabının seçildiği alandır. |
| Hammadde Hesabı | Muhasebeleştirilecek hammadde hesabının seçildiği alandır. |
| Miktarlar Muhasebeye Geçsin | Miktarların muhasebeye geçmesi için kullanılan parametredir. |
| ![](../../../_assets/39d77b8716226638d9ce.jpg) Tamam | İşaretlenen parametrelerle ilgili işlemlerin gerçekleşmesini sağlayan butondur. > [!NOTE]<br>> Parametrelerle ilgili işlemlerin programa yansıması için programın kapatılıp tekrar açılması gerekir. |
| ![](../../../_assets/973111d004995dca0113.jpg) İptal | İşaretlenen parametrelerden vazgeçilmesi halinde kullanılan butondur. |
