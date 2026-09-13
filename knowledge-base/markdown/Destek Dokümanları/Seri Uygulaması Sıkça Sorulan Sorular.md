---
title: "Seri Uygulaması Sıkça Sorulan Sorular"
page_id: "108659249"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Seri Uygulaması Sıkça Sorulan Sorular"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Seri Uygulaması Sıkça Sorulan Sorular"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWJiZjA0NTkxLTE5OWQtNDFhMi1hOGNjLWU3YWJhYjM5YmIxNiZsaW5rPWQ5MDlkOTNiLTM3NmQtNDA0Yy04NjU4LWUwNjJjOGE0MGRjZSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=bbf04591-199d-41a2-a8cc-e7abab39bb16&link=d909d93b-376d-404c-8658-e062c8a40dce&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "seri-uygulamasi-sikca-sorulan-sorular_108659281_108659249.html"
source_version: "2023-03-31T09:36:53.383+03:00"
source_bytes: 4928871
fetched_at: "2026-09-13T04:23:35+00:00"
generator: "netsis-scraper 1.0.0"
---
# Seri Uygulaması Sıkça Sorulan Sorular

**Seri Lot/Parti Numarası Nedir?**

Lot ya da parti numarası aynı koşullarda ve zamanda üretilen, ambalaj, ambalaj büyüklüğü, sınıf, tip, çeşit ve boyu aynı olan bir ürün grubuna verilen sayısal/harflerin kombinasyonudur. Seri numarası her bir adet ürün için ayrı tanımlanır ve benzersizdir. Yani ürünün markası modeli üretim tarihi aynı bile olsa her bir ürün için ayrı bir seri numarası verilir. Örnek verecek olursak her bir cep telefonunun ayrı bir uluslararası mobil cihaz kodu vardır. Seri no takibi elektronik, bilgisayar, savunma sanayi sektörlerinde yoğun olarak kullanılmaktadır. Cihazların garanti takibi de bu şekilde yapılır. Parti numaraları ürün gruplarına uygulanırken, seri numaraları belirli bir ürün için ayrı tanımlayıcı numaralardır.

**Hangi paketlerde seri uygulaması kullanılabilir?**

Netsis Enterprise, Netsis Standard ve Netsis Entegre paketlerimizde seri uygulaması kullanılabilir.

**Seri uygulaması aktif hale** **nasıl getirilebilir?**

Yardımcı programlar modülü altından şirket şube parametreleri ekranından "Seri Takibi Var" parametresi işaretlenmelidir. Parametrenin aktif hale gelmesi için şirket değişikliği ya da programı kapatıp tekrar açmak gerekir.
![](../_assets/16bfab218849f86558f0.png)

**Seri takibi yapılmak istenilen stoklar için nasıl tanımlama yapılmalıdır?**

Seri takibi yapılmak istenilen stoklar için Stok Kartı Kayıtları Seri Takibi sekmesi üzerinden seri ile ilgili kullanılmak istenilen parametrelerin seçimi yapılabilir.

![](../_assets/7dbc4bebf040b305abf2.png)

**Seriler için bakiye takibi yapılabilir mi?**

Stok kartları üzerinden girişlerde ve çıkışlarda seri numarası takibi aktif olması durumunda bakiye kontrolü yapılsın parametresi de işaretlenir ise sistem girişlere uygun çıkış serilerinin bakiyelerini de kontrol etmektedir. Böylelikle sistemde olmayan bir seri/lot numarasından çıkış engellenir.

**Miktar kadar seri sorulsun parametresi nasıl çalışır?**

Miktar kadar seri sorulsun parametresi açık ise her miktar için tek bir seri numarası verileceği anlamına gelmektedir. Stok kartında bu parametre işaretli ise seri takibi, işaretli değil ise bu kartta lot numarası takibi yapılacağı anlaşılır.

**Her bir serinin stok bazında tek olması sağlanabilir mi?**

Seri parametreleri altında yer alan Seri Stok Bazında Tek Olsun parametresi kullanılabilir. Sadece stok giriş hareketlerinde baz alınır. Seri numaralarının her bir stok kartı bazında tek (tekrarsız) olması istendiği durumlarda işaretlenmesi gereken parametredir. Böylece, stok girişlerinde girilen seri numarasının daha önce girilip girilmediği kontrol edilir ve girilmişse aynı serinin girişine izin verilmez. Parametrenin işaretlenmemesi durumunda, aynı seriden birden fazla girişe izin verilir.
![](../_assets/b35cd7fdd1106402a993.png)

**Seri stok bazında tek olsun seçeneği işaretli iken iade tipli alış belgelerinde** **'SERİ TAKİBİ DOSYASINA KAYIT YAPILAMADI. ... NOLU SERİNİN GİRİŞİ DAHA ÖNCEDEN YAPILMIŞ" uyarısı alınmaması için ne yapılmalıdır?**

Grup kodu: STOK Anahtar: URUN_BAZINDA_SERI_DEGISKEN Değer: 0 özel parametresi tanımlanmalıdır.

**Miktarsız girilen kalemler için seri girişi nasıl yapılabilir?**

Seri parametreleri altında yer alan "Miktarsız Kalem İçin Seri Girişi Yapılsın" parametresi ile Fatura belgelerinde miktar "0" girildiğinde de "Seri Takibi" ekranının açılması sağlanabilir.

**Girişlerde seri takibi kullanılmayan stoklar için iade tipli alış faturası girişi nasıl sağlanır?**

Seri parametreleri altında yer alan "İade Tipli Girişlerde Seri Girişi Yapılsın" parametresi ile "Girişlerde Seri Takibi" parametresi işaretli değilken, iade tipli alış faturasında seri ekranının açılması sağlanabilir.

**FIFO serileri için sıralama değiştirilebilir mi?**

Seri parametreleri altında yer alan "FIFO Seri için Sıralama Kriteri" alanından seçili alana göre "Seri Takibi" ekranındaki sıralanarak getirilmesi sağlanabilir.

![](../_assets/14fe2f724f25b95d67a6.png)

**Seriler için sistem üzerinden otomatik seri numarası atanabilir mi?**

Seri parametreleri altında yer alan seri numarası girişler ve çıkışlar için otomatik hesaplansın parametresi aktif hale getirilerek hangi stoklarda otomatik hesaplanması isteniyor ise ilgili stok kartlarında seri takibi sekmesi üzerinden seri takibi giriş ve çıkışlar için otomatik hesaplansın seçenekleri kullanılabilir.

![](../_assets/b2e043f63521beffb44f.png)

**Seri takibi çıkışlar için otomatik hesaplansın seçeneği işaretli olduğu halde otomatik seri oluşturmamasının nedeni nedir?**

Stok Kartı Kayıtları → Seri Takibi → "Bakiye Kontrolü Yapılsın" parametresi işaretlendiğinde, çıkışlarda otomatik seri hesaplanmamaktadır.

**Seri ekranında seri girişi yöntemleri nelerdir?**

Belge üzerinde miktar çıkışından sonra açılan seri takibi için 5 yöntem ile giriş yapılabilmektedir.

1. Seriler satırlara manuel giriş yapılabilir.
2. Excel'den aktarım ile seriler aktarılabilir.
3. Serileri yapıştır seçeneği ile kopyalanan veriler yapıştırılabilir.
4. Hızlı seri girişi sekmesi üzerinden başlangıç bitiş seri ve miktar bilgileri girilerek seri girişleri yapılabilmektedir.
5. Giriş ve çıkışlar için otomatik seri oluşturulsun işaretli ise seri takibi ekranına otomatik seriler getirilmektedir.

**Belge girişi esnasında girilen seriler tekrar nasıl izlenebilir?**

Belge kalemleri üzerinde serili stoklar için sağ klik seri bilgisi izleme ile görüntülenebilir.

![](../_assets/c2c6f96eb5f83f329107.png)
![](../_assets/738204e1b7604fc81293.png)

**Girilen belgeler için seri numaraları tekrar nasıl izlenebilir?**

Stok hareket kayıtları üzerinde ilgili belge için sağ klik seri bilgisi izleme ekranı ile girilen seriler izlenebilir.

![](../_assets/d1eb4092d49c48eb4dc9.png)
![](../_assets/7323cf2f658cfb79fe0f.png)

**Seri takibi ekranında miktar uyumsuzluğu uyarısı alındığı durumda ne yapılmalıdır?**

Belgede girilen miktar ile seri miktarı uyumsuz olduğunda bu uyarı ile karşılaşılmaktadır. Alt bilgi ekranında hareket miktarı (belge miktarı), girilen seri miktarları ve kalan miktar bilgisi üzerinden kontrol sağlanabilir.

![](../_assets/89ff5d86567076b1595b.png)

**Belge içerisinde miktarın yanlış girilmesi durumunda seri takibi ekranı nasıl kapatılır?**

Seri takibi ekranında hiçbir seri girişi yapılmadı ise ekran kapatılabilmektedir ya da seri girişleri yapıldıktan sonra miktarın yanlış olduğu fark edildi ise tüm seri girişleri silinip ekran kapatılabilmektedir. Miktar düzeltmesi yapıldıktan sonra tekrar yeni açılan "Seri Takibi" ekranı üzerinden seri girişleri yapılabilir.

**Otomatik seri numarasının nasıl oluşacağına karar verilebilir mi?**

Otomatik seri no üretme tanımları ekranı ile sabit, değişken ve script ile serilerin nasıl oluşturulacağına karar verilebilir. Geçerli stoklar sekmesi üzerinden tanımlanan otomatik serinin hangi stok kodlarında çalışacağına karar verilebilir.

**Stok kartında giriş ve çıkışlar için seri otomatik hesaplansın seçeneği işaretli hem de otomatik seri no üretme ekranında eşleşmesi var ise sistem hangisini dikkate alır?**

Öncelik otomatik seri no üretme tanımları ekranındadır. Burada eşleşmesi bulunmaması durumunda sistem otomatik seri hesaplaması yapmaktadır.

**Son kullanma tarihinin seri ekranlarında kullanımı nasıldır?**

Seri parametreleri ekranında seri takibi için opsiyonel sahalarda "Son Kullanma Tarihi" seçeneğinin seçili olması gerekir. Girişi yapılan seriler içerisinde son kullanma tarihinin en küçük olanın ilk çıkış yapılmak istenir ise Seri Takibi ekranında FEFO Çıkış Seri butonuna basılarak son kullanma tarihi en yakın olan serinin çıkışının yapılabilmesi sağlanır.

![](../_assets/21e16ec7bc703984b1ec.png)

**Son kullanma tarihi yanlış girilmiş belgeler için son kullanma tarihi güncelle işlemi yapılabilir mi?**

Seri takibi ekranı üzerinde yer alana SKT Güncelle butonu ile seçili seri için son kullanma tarihi bilgisi değiştirilebilir. İlgili seri numarasının geçtiği tüm belgelerdeki son kullanma tarihleri güncellenir.

![](../_assets/1608fc936c0e01df46d7.png)
![](../_assets/8787092552193ef592c2.png)

**İlk giren serinin ilk çıkması için kullanım nasıl olmalıdır?**

Seri takibi ekranı üzerinde FIFO Çıkış Seri butonuna basıldığında ilk girilen serinin ilk çıkması sağlanabilir.

![](../_assets/ac824e0c32a7230d0075.png)

**Kullanılan seriler için barkod eşleştirilmesi yapılabilir mi?**

"Seri Parametreleri" ekranının "Seri Girişinde Kullanılacak Opsiyonel Sahalar" bölümüne "Barkod" alanı eklenmiştir. İşaretlendiğinde "Seri Takibi" ve "Seri Takibi Kayıtları" ekranlarında "Barkod" sahası görünür hale gelir. "Stok Kartı Kayıtları" ekranındaki "Seri Bilgileri" sekmesine "Girişlerde Barkod Tanımı Zorunludur" parametresi eklenmiştir. İşaretlendiğinde serili stok için yapılan "Giriş" tipli hareketlerde "Seri Takibi" ve "Seri Takibi Kayıtları" ekranlarında barkod girişi zorunlu olur. Fatura modülündeki "Alış/Satış Parametreleri" ekranlarına ve Talep/Teklif modülündeki "Talep/Teklif Parametreleri" ekranındaki sekmelere "Barkod Seriden Okunsun" parametresi ile, belgede "Stok Kodu" sahasına yazılan değer, Seri Kayıtları içerisinde aranacaktır, aramadan uygun bir kayıt bulunamaz ise de seri girişi sırasında yazılan Barkod kayıtlarına bakılacaktır. Uygun kayıt bulunduğunda "Seri Takibi" ekranı otomatik olarak "Stok Kodu" sahasına yazılan ilgili seri ile açılır.

Örnek; 12122022 barkod numaralı bir seri girişi yapılır.

![](../_assets/b2c0909c96891bd5874e.png)

Satış belgesinde bu barkod numarası yazılıp tab ile geçildiğinde stok ismi olarak otomatik değişir ve Seri Takibi ekranına da otomatik barkoda ait seri yansıtılır.

![](../_assets/49428ae59eb6e7522f85.png)
![](../_assets/7dfe57d138d7899edc61.png)
![](../_assets/bec5f510a80d1da2d47d.png)

**Seri numarası değişikliği yapılabilir mi?**

Stok\\Kayıt\\Seri Takibi\\ Seri Numarası Değişikliği ekranından seri numarası değişikliği yapılabilmektedir.

![](../_assets/33a5fcd2291b5cb4489c.png)

**Seri takibi kayıtları ekranı ne amaçla kullanılır?**

Bu bölümden girilen seri numaraları devir kabul edilir ve sadece raporlarda baz alınır.

"Stok Hareket Kayıtlarına" yansıtılmaz, kontrolü kullanıcılara bırakılır. Yani, stok giriş/çıkış hareketlerinde bu seriler için parametre kontrolü yapılmaz.

**Üretim belgelerinde seri giriş çıkışları hangi ekran üzerinden sağlanır?**

Üretim modülünde seri takibi yapılacaksa serbest üretim sonu kaydı ekranı kullanılmalıdır.

**Serbest üretim sonu kaydı ekranında seri bilgisi durumu nereden takip edilebilir?**

Fiş üretildikten sonra grid ekranda yer alan Seri Durumu alanından seri girişi yapılıp yapılmadığı kontrol edilebilir.

![](../_assets/362daa51f804beee81e2.png)

**İş emri reçetesindeki bileşenlere seri girişi yapılabilir mi?**

Seri parametreleri ekranında iş emri reçetesinde seri girişi yapılsın parametresi aktif ve üretim parametrelerinde iş emriyle reçete saklansın parametresi işaretli ise iş emri girişi ekranında yer alan iş emrine bağlı reçete kayıtları sekmesinde bileşenler için seri girişi yapılabilir ve serbest üretim sonu kaydı ekranına getirilmesi sağlanabilir.

**İş emrine bağlı depolar arası transferde girilen seri bilgisi serbest üretim sonu kaydı ekranına otomatik getirilebilir mi?**

İş emrine bağlı depolar arası transfer yapılıyorsa üretim parametrelerinde bulunan "Serbest üretim sonu kaydında malzeme serileri DAT belgesinden getirilsin" parametresi ile serilerin otomatik gelmesi sağlanabilir. Böylelikle seri numaraları tekrar seçilmek zorunda kalınmaz.

Örnek: Satış parametrelerinde üretim reçeteleri getirilsin seçeneği işaretli ve Dat belgesinde ilgili mamul ve iş emri numarası seçilip miktar çıkışında sonra sağ klik reçete getirme işlemi çalıştırılıp serili bileşeni için seri girilmesi durumunda SUSK ekranında ilgili iş emri üretildiğinde otomatik seri bilgisi DAT ekranından taşınmaktadır.

![](../_assets/28574aa73184a1875108.png)
![](../_assets/178ef86d273ee1e72905.png)
![](../_assets/3caa850fd4409905ac9f.png)
![](../_assets/4c0e34219f6d048371c2.png)

**Üretimde parti büyüklüğüne göre seri oluşturulması sağlanabilir mi?**

Seri parametreleri ekranında yer alan seri numarası girişler ve çıkışlar için otomatik hesaplansın altında yer alan "Üretim sonu kaydında girişler için Parti Büyüklüğü Kullanılsın" ve "Üretim sonu kaydında çıkışlar için Parti Büyüklüğü Kullanılsın" seçenekleri kullanılarak stok planlama kayıtlarında yer alan parti büyüklüğüne bağlı otomatik seri kayıtları oluşturulabilir. (10000 adet üretim parti büyüklüğü 1000 ise 10 satır olarak serileri oluşturur) İlgili stok kartları için miktar kadar seri sorulsun parametresinin işaretli olmaması gerekir.

**Üretimde çıkış serilerinin otomatik oluşması sağlanabilir mi?**

Üretim parametrelerinde yer alan Üretim Çıkışlarda FIFO ve FEFO seri oluşsun parametreleri ile İlk Giren İlk Çıkar ( FIFO) yöntemi ya da Son Kullanma Tarihi (FEFO) 'ni dikkate olarak otomatik serilerin getirilmesi sağlanabilir.

![](../_assets/0868460565978190f30d.png)

**Dinamik depo kullanımında hücre yerleştirme ve toplama işlemlerinde seri girişi nasıl yapılabilir?**

Dinamik depo parametrelerinde yer alan "Seri Bilgisi Depoda Sorulsun" parametresi işaretli ise serili stoklar için hücre yerleştirme ve toplama ekranlarında seri bilgisi girişi yapılabilir.
![](../_assets/8974bebcf95d51338938.png)![](../_assets/127e77acc23988f83ba0.png)

**Kalite kontrol belgeleri için seri girişi seçenekleri nelerdir?**

Kalite kontrol parametreleri altında yer alan Seri-Lot Girişi alanında serinin nereden girileceği seçimi yapılabilir. Alış irsaliyesinde seri girişi yapılacak ise alış irsaliyesi seçeneği, kalite kontrol kaydı esnasında seri girişi yapılacak ise kalite kontrolde seçeneği seçilmelidir.
![](../_assets/39dce600a90b846b3871.png)

**Sipariş ekranlarında seri desteklenmekte midir?**

Sipariş ekranlarında seri giriş ve çıkışları desteklenmemektedir.

**Seri bilgileri hangi tabloda tutulmaktadır?**

TBLSERITRA tablosunda tutulmaktadır.

**Karma koli stoğu için seri bilgisi girilebilir mi?**

Karma koli tanımında bilgi amaçlı seçeneği işaretli ise seri bilgisi girişi yapılabilir.

**Seri rehberinde ek açıklamalar kullanılması durumunda çıkış hareketlerinde açıkta kalan serilere ait açıklamalar nasıl görünür?**

"STOK", "SERIREHBAK_EKALANLAR" özel parametresiyle Seri Takibi ekranındaki Seri Rehberinde seri bilgilerinin ve bakiyelerin opsiyonel sahalara göre kırılımlı gelmesi sağlanmıştır.

**Çeki listesinden irsaliye oluşturulması durumunda seri girişi nasıl yapılabilir?**

Detay gösterme ekranı sevkiyatlar sekmesi üzerindeki kalemlere ait grid alanda sağ klik seri bilgisi girişi ile seriler girilebilir.

![](../_assets/3ff25cadb1598ffdb793.png)
