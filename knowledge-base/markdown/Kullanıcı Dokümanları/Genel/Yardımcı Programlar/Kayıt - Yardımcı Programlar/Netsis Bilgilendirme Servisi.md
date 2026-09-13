---
title: "Netsis Bilgilendirme Servisi"
page_id: "24753249"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Genel"
  - "Yardımcı Programlar"
  - "Kayıt / Yardımcı Programlar"
  - "Netsis Bilgilendirme Servisi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Yardımcı Programlar / Kayıt / Yardımcı Programlar / Netsis Bilgilendirme Servisi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTE0NTY2Yzg5LTNkMWItNGU4Zi1hZmM4LWNjMjZiMjRhNDM3YSZsaW5rPTU3ODY5MmY4LWI4MmItNDY0ZS1iYjc3LTgzNDA1M2E4NjEyOCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=14566c89-3d1b-4e8f-afc8-cc26b24a437a&link=578692f8-b82b-464e-bb77-834053a86128&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-bilgilendirme-servisi_41170612_24753249.html"
source_version: "2022-10-05T09:43:58.350+03:00"
source_bytes: 192534
fetched_at: "2026-09-13T04:17:19+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis Bilgilendirme Servisi

Netsis Bilgilendirme Servisi, Genel Bölümü'nde, "Kayıt/Yardımcı Programlar" menüsünün altında yer alır. "Netsis Bilgilendirme Servisi" ile kullanıcıların zamana bağlı işlerinin takibi, şirketler bazında yapılması gereken işlemlerin makrolar yardımı ile istenen zamanda otomatik olarak yapılması, istenen kişilere şirketle ilgili bazı önemli bilgilerin istenen zaman aralıklarında listelenmesi, Logo Netsis’in haber ve yeniliklerinin otomatik olarak kullanıcılara duyurulması gibi işlemlerin yapıldığı bölümdür.

![](../../../../_assets/423216fd64a54752ef12.png)

Netsis Bilgilendirme Servisi ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Netsis Bilgilendirme Servisi Ekranı |  |
| --- | --- |
| Sıra No | Tanımlanacak iş tanımı için sıra numarası girilen alandır. Sıra numarası, sayısal bir değer olmalıdır. |
| Bilgisayar Adı | Hazırlanan bilginin veya işin belli bir bilgisayarda çalışması istendiği zaman, ilgili bilgisayar adının girildiği alandır. Bilgisayarı hangi kullanıcının kullandığı fark etmez. Boş bırakıldığında hazırlanan bilgi veya iş, bu uygulamayı kullanan tüm bilgisayarlarda çalışır. |
| PC Kullanıcısı | Hazırlanan bilginin veya işin sadece belli bir kullanıcı sisteme bağlandığında çalışması istendiği zaman, ilgili kullanıcı isminin girildiği alandır. Bilgisayar adı boşsa, kullanıcı hangi bilgisayardan sisteme bağlanırsa bağlansın fark etmez. Bilgisayar adı dolu olduğunda ise, sadece bu bilgisayara yazılan kullanıcı adı ile giriş yapıldığında çalışır. |
| Bilgi Tipi | Bilginin geldiği yerin sorgulandığı alandır. Bilgi Tipi alanı; Netsis Haber, Netsis Yenilik, Table, View, Stored Function, Makro seçeneklerinden oluşur. **Netsis Haber:** Belli zamanlarda, Netsis’in haber sayfasında yayınlanan bilgilerin, okunmak üzere hatırlatılması için kullanılan seçenektir. Netsis ile ilgili haberlerin gün içinde ulaştırılması için - çalışma şekli/dakika bazında ise - süre olarak en az 30 dakika tanımlanması gerekir. **Netsis Yenilik:** Belli zamanlarda, Netsis’in yenilik sayfasında yayınlanan bilgilerin, okunmak üzere hatırlatılması için kullanılan seçenektir. Netsis yeniliklerinin gün içinde ulaştırılması için - çalışma şekli/dakika bazında ise - süre olarak en az 30 dakika tanımlanması gerekir. Netsis Haber ve Yenilik ekranı görüntülendikten sonra, bu ekrandan Netsis’in web servisine bağlanarak konu ile ilgili daha detaylı bilgiye ulaşılabilir. Netsis Haber ve Netsis Yenilik bilgileri, Netsis tarafından oluşturuldukça kullanıcı bilgilendirilir. Gelen haber ve yenilikler bildirildikten sonra tekrar kullanıcının karşısına gelmez. Bilgisayar tarafından henüz hiç haber ve yenilik okunmamışsa, program yüklendiğinde sadece son yenilik veya haberler ekrana gelir. **Table:** Kullanıcı tarafından oluşturulan veya Netsis’in mevcut tablolarından bilgi alınacak bir işin tanımlanması için Table seçeneğinin kullanılması gerekir. **Örneğin,** içinde kullanıcı isimleri, yapılması gereken işler, işlerin tamamlanma süreleri ve işlerin son durumunun bulunduğu bir tablo oluşturulduğu varsayıldığında, tablodaki bilgilerin belli zaman aralıklarında kullanıcılara hatırlatılması için "Table" seçeneğinin kullanılması gerekir. **View:** Kullanıcı tarafından oluşturulan veya Netsis’in mevcut raporlarından bilgi - view - alınacak bir işin tanımlanması için kullanılan seçenektir. **Örneğin,** faturası kesilmemiş irsaliyeleri listeleyen bir rapor - view - hazırlandığında, belli sürelerde bu bilginin raporlanarak kullanıcılara hatırlatılması için kullanılabilir. **Stored Function:** Çok uzun süren ve çok sayıda SQL cümlelerinden oluşan işlemler için kullanılan seçenektir. Böylece, çok uzun süren işlemler daha hızlı ve zamana bağlanarak yapılabilir. **Makro:** Tanımlanmakta olan işin, tanımlı bir makroya bağlanması için kullanılan seçenektir. Böylece, özellikle çok uzun süren işlerin belli bir zamanda otomatik olarak başlatılması sağlanır. Bunun için makro tanımının önceden yapılması gerekir. Tanımlanan makronun otomatik olarak çalışmaya başlaması için şirket ana menüsünde bulunması gerekir. **Örneğin,** Maliyet Muhasebesi → "Maliyet Hesaplatma" seçeneği verilerin yoğunluğu doğrultusunda uzun süren bir işlemdir. Bu işlem için bir makro hazırlanıp mesai saatleri dışında çalışması sağlanabilir. Makro kullanımlarında işlerin çalışma şeklinin “Günlük” olması önerilir. |
| Paket | Bilgi tipinin Tablo, View ve Stored Function seçilmesi ile aktif hale gelen alandır. Seçilen veri tabanı ile ilgili bilginin alınacağı Logo Netsis paketinin belirlenmesini sağlar. **Örneğin;** bilgi, ticari pakete ait bir veri tabanından alınacaksa "Temelset", personel paketine ait bir veritabanından alınacaksa "Personel" seçeneğinin kullanılması gerekir. |
| Adı | Bilgi tipinin Tablo, View ve Stored Function seçilmesi ile aktif hale gelen alandır. Bilginin alınacağı veritabanı adının girilmesini sağlar. |
| Kullanıcı | Bilgi tipinin Tablo, View ve Stored Function seçilmesi ile aktif hale gelen alandır. Bilginin alınacağı veritabanına ait kullanıcı adının girilmesini sağlar. **Örneğin;** ticari pakete ait bir veritabanının kullanıcı adı standart olarak "TEMELSET", Demirbaş paketine ait bir veritabanının kullanıcı adı "DEMIRBAS", Personel paketine ait bir veritabanının kullanıcı adı "PERSONEL", İşletme paketine ait bir veritabanının kullanıcı adı ise "ISLETME'dir." |
| Şifre | Bilgi tipinin Tablo, View ve Stored Function seçilmesi ile aktif hale gelen alandır. Bilginin alınacağı veritabanına ait veritabanı kullanıcı şifresinin girilmesini sağlayan alandır. Veri tabanı kullanıcı şifresi yoksa bu alan boş bırakılabilir. |
| Nesne Adı | Bilgi tipinin Tablo, View ve Stored Function seçilmesi ile aktif hale gelen alandır. Özellikle yeni kullanıcılara kolaylık sağlar. Henüz bir SQL cümlesi tasarlayamayan kullanıcılar, bilgi almak istedikleri bir view veya tablo ismini "Nesne Adı" alanına girebilir. SQL alanında SQL cümlesi yazılmadan, "Nesne Adı" alanına bir view ya da tablo ismi girildiği zaman program, bu view ya da tablodaki bütün alanları listeler. |
| Alt Limit | Bilgi tipinin Tablo, View ve Stored Function seçilmesi ile aktif hale gelen alandır. Bir liste ekranının listelenmesi için ulaşacağı kayıt sayısının girilmesini sağlar. Yani, listelenecek kayıt sayısı, kullanıcının bu alana girdiği sayıya ulaştığında program bilgi verir. Bu sayının altına düşüldüğünde, bilgi listelenmez. **Örneğin;** faturalanmamış irsaliye sayıları ile ilgili bir rapor listelenmesi için "10" değerinin girildiği varsayıldığında, faturalanmamış irsaliye sayısı 10 ve üzeri olduğu zaman rapor listelenir. Kayıt sayısı 10 değerinin altına düştüğünde ise rapor listelenmez. |
| SQL | Bilgi tipinin Tablo, View ve Stored Function seçilmesi ile aktif hale gelen alandır. Tanımlanan iş için SQL cümlesinin girilmesi gerekir. **Örneğin;** SELECT \* FROM FATURALASMAMIS_IRSALIYELER ya da SELECT STOK_KODU,STOK_ADI,GRUP_KODU FROM TBLSTSABIT gibi. |
| Geçerlilik Başlangıç/Bitiş Tarihi | Netsis Bilgilendirme Sistemi ekranında girilen bilgilerin geçerlilik başlangıç ve bitiş tarih aralığının girildiği alanlardır. |
| Gösterme Şekli | Gösterilecek bilginin veriliş şeklinin belirlendiği alandır. Bilgi, Alarm ve İkaz olarak üç seçenekten oluşur. Her üç seçenekte de aynı bilgi verilir fakat veriliş şekli değişkenlik gösterir. "Gösterme Şekli" alanı kullanılarak, listenin daha kritik veya daha bilgi amaçlı olduğu gösterilebilir. Gösterme şekli "Bilgi" seçildiğinde, açılan ekranın sol üstünde “İ” harfi görünür. Gösterme şekli "Alarm" seçildiğinde, açılan ekranın sol üstünde “X” harfi görünür. Gösterme şekli "İkaz" seçildiğinde, açılan ekranın sol üstünde “!” ünlem işareti görünür. |
| Çalışma Şekli | Hazırlanan bilginin nasıl ve hangi sıklıkta çalışacağının belirlendiği alandır. Çalışma Şekli; Açılışta, Dakika Bazında ve Günlük olarak üç seçenekten oluşur. **Açılışta:** Hazırlanan bilgi, NetJob.EXE programı her açıldığında kullanıcının ekranına gelir. **Dakika Bazında:** Hazırlanan bilgi, NetJob.EXE programı her açıldığında belirtilen dakika aralığında kullanıcının ekranına gelir. **Günlük:** Hazırlanan bilgi, NetJob.EXE programı her açıldığında belirleyeceği günlerde, kullanıcının ekranına bir kez gelir. |
| Pencere Başlığı | Bilgilendirme ekranı kullanıcı ekranında görüntülendiği zaman istenen başlık görüntüsünün girildiği alandır. |
| Makro | Makroya bağlanacak bir iş tanımlanacağı zaman, çalışacak makro numarasının girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, tanımlı makro numaralarına ulaşılır. |
| Süre | "Çalışma Şekli" alanında "Dakika Bazında" seçeneği işaretlendiğinde aktif hale gelen alandır. Bilgilendirme ekranının kullanıcı karşısına çıkacağı dakika sayısının girilmesini sağlar. Netsis Haber veya Netsis Yenilik işaretlenmiş ise en az 30 dakika, diğer durumlarda ise en az 1 dakika verilebilir. Süre ayarlaması yapılırken, sistemi yormayacak veya çalışmaya engel olmayacak sürelerin girilmesi gerekir. |
| Saat | "Çalışma Şekli" alanında "Günlük" seçeneği işaretlendiğinde aktif hale gelen alandır. Bilgilendirme ekranının kullanıcı karşısına çıkacağı saat sayısının girilmesini sağlar. **Örneğin,** saat olarak 14:30 girildiğinde, bilgilendirme ekranı kullanıcının karşısına saat 14:30'da gelir. |

Netsis Bilgilendirme Servisi'ne ait tanımlamalar yapıldıktan sonra belirtilen sürede bilgilendirme ekranı kullanıcının karşısına gelir. Ekrana gelen "Hatırlatma Raporu" ekranında rapor ile ilgili düzenlemelerin yapılmasını sağlayan Yenile, Yenilemeyi Durdur, Listeden Çıkar ve Görünürlük Oranı alanları bulunur.

![](../../../../_assets/1d8ed7b774ce17d4a676.png)

Hatırlatma Raporu ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Hatırlatma Raporu Ekranı |  |
| --- | --- |
| **![](../../../../_assets/e0f0cbf500b875f18261.png)**Yenile | Ekrana gelen hatırlatma raporundaki bilgilerin güncellenmesi için kullanılan butondur. **Örneğin,** faturalanmamış irsaliyeler ile ilgili bir rapor görüntülendiğinde, o sırada yeni kaydedilen bir irsaliyenin de rapora eklenmesini sağlar. |
| ![](../../../../_assets/933d465b05106ef5b533.png) Yenilemeyi Durdur | Ekrana gelen hatırlatma raporundaki bilgilere yeni bir bilgi eklense bile ekrandaki raporun güncel hale getirilmeden sabit kalmasını sağlayan butondur. |
| ![](../../../../_assets/020a45e232ef1822e7a3.png) Listeden Çıkar | Ekrana gelen hatırlatma raporunun bir daha görüntülenmemesini sağlayan butondur. Rapor ekrana geldikten sonra butona tıklandığında, bir sonraki görüntülenme zamanı geldiğinde ekrana gelmez. Bu işlemden vazgeçilip raporun tekrar görüntülenmesi için Netjob.exe üzerinde farenin sağ tuşu ile açılan "İşleri Tekrar Oku" seçeneğine tıklanması gerekir. |
| Görünürlük Oranı | Ekrana gelen hatırlatma raporunun ekran üzerindeki görünürlük oranının sağa ve sola çekilerek ayarlanmasını sağlar. |

**Netjob.exe’(nin) Çalıştırılması:** Netsis Bilgilendirme Servisi ile ilgili tanımlamalar yapıldıktan sonra eğer uygulama ilk kez kullanılıyorsa, program dizininde servis dizini altındaki Netjob.exe’nin farenin sol tuşu ile çift tıklayarak çalıştırılması gerekir. Çalıştırıldıktan sonra ekranın sağ alt köşesinde netjob’ın simgesi görüntülenir.

Ekranın sağ alt köşesinde çalışan netjob.exe üzerinde iken farenin sağ tuşuna tıklandığı zaman netjob ile ilgili çeşitli düzenlemelerin yapılmasını sağlayan Durdur, İşleri Tekrar oku, Açılıştan kaldır, Son Haberi Getir, Son Yeniliği Getir, Ses ve Kapat seçenekleri ekrana gelir.

![](../../../../_assets/777f33839435a73a8994.png)

netjob.exe sağ fare tuşu seçenekleri şunlardır:

| netjob.exe Sağ Fare Tuşu Seçenekleri |  |
| --- | --- |
| Durdur | Çalışan Netsis Bilgilendirme Servisinin durdurulmasını sağlar. |
| İşleri Tekrar Oku | Netsis Bilgilendirme Servisinde geçici olarak durdurulan tanımlamaların aktif hale getirilmesi için kullanılan seçenektir. Tanımlamalarda bir değişiklik yapılmışsa, son değişikliğe göre işlerin tekrar okunup belirtilen sürede ekrana getirilmesini sağlar. |
| Açılıştan Kaldır | Netjob.exe bir defa çalıştırılıp aktif hale getirildikten sonra, bilgisayarın her açıldığında aktif hale gelir ve ekranın sağ alt köşesinde görüntülenir. Aktif olan netjob.exe’nin açılıştan tamamen kaldırılması, yani bilgisayarın kapatılıp tekrar açıldığında da görüntülenmemesi için kullanılan seçenektir. |
| Son Haberi Getir | Netsis ile ilgili tanımlı son haberin otomatik olarak ekrana gelmesini sağlayan seçenektir. |
| Son Yeniliği Getir | Netsis ile ilgili tanımlı son yeniliğin otomatik olarak ekrana gelmesini sağlayan seçenektir. |
| Ses | Netsis bilgilendirme servisi ile gelen uyarı mesajlarının sesli şekilde ekrana gelmesini sağlayan seçenektir. |
| Kapat | Çalışır durumda olan netjob.exe'nin kapatılmasını sağlayan seçenektir. Bilgisayar kapatılıp açıldığında tekrar aktif hale gelir. |
