---
title: "Rapordan Grafik Hazırlama"
page_id: "47084406"
product: "netsis-3-enterprise"
depth: 3
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Giriş"
  - "Rapordan Grafik Hazırlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Giriş / Rapordan Grafik Hazırlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTc5OGVhY2FkLWZjMjEtNDBhMS05Njc4LTYyYmMxMTU2ZTI2ZCZsaW5rPWE5ZTFhMjkzLWNkM2UtNGQ4OC1hNTY4LWI3OTk4ZTkxY2YzMSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=798eacad-fc21-40a1-9678-62bc1156e26d&link=a9e1a293-cd3e-4d88-a568-b7998e91cf31&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "rapordan-grafik-hazirlama_94634043_47084406.html"
source_version: "2022-10-21T14:10:01.633+03:00"
source_bytes: 16518
fetched_at: "2026-09-13T04:01:26+00:00"
generator: "netsis-scraper 1.0.0"
---
# Rapordan Grafik Hazırlama

Herhangi bir rapor, ekranda listelendikten sonra, grafiği oluşturulacak bölüm fare ile seçilir ve araç çubuğunda bulunan "Grafik Hazırlama" ikonu kullanılarak "Netsis Grafik Hazırlama Aracı'na" ulaşılır. Raporlardan grafik oluşturulması için, raporda gösterilmesi istenen bilgilerin ekrandan seçilmesi gerekir. Grafikte, seçilen kolonlardan sadece ikisi yer alır. Tüm kolonların seçilerek, raporlanacak kolonların daha sonra belirlenmesi mümkündür. Sadece grafiği oluşturulacak kolonların seçilmesi de sağlanabilir.

**Gridden Grafik Hazırlama**

Ekranda açık bulunan herhangi bir grid ekran üzerinde iken, farenin sağ klik tuşu ile ekrana gelen "Grafik Hazırlama" seçeneği ile "Netsis Grafik Hazırlama Aracı’na" ulaşılır. Böylece, gridde bulunan kolonlardan istenen iki tanesi grafikle gösterilir. Gridden grafik oluştururken başlangıçta kolon seçimi yapılmayarak grafik haline getirilecek kolonlar, "Grafik Hazırla" seçeneğinden sonra gelen "Tablo Parametreleri" ekranından belirlenir.

**Diğer Ortamlardan Kopyalanan Verilerden Grafik Hazırlama**

Excel, Word, Notepad gibi başka ortamlarda bulunan veriler seçildikten sonra klavyede bulunan CTRL+C tuşlarına basılarak veya farenin sağ klik tuşu ile açılan "Kopyala" seçeneği ile kopyalandıktan sonra, Netsis paketlerinin herhangi bir modülüne geçip Araçlar → Fonksiyonlar → Grafik Hazırlama seçeneği ile "Netsis Grafik Hazırlama Aracı'na" ulaşılır. Bu durumda, kopyalanan verinin grafikte gösterilecek kolonlarının belirleneceği "Tablo Parametreleri" ekranı görüntülenir.

Notepad ve Word gibi uygulamalarda tutulan verilerin grafik ile gösterilmesi için belirli bir biçime göre düzenlenmesi gerekir. Bu dosyalarda bulunan kolonların birbirinden farklı değerler olarak algılanması için, dosya içine yazılan veriler arasındaki boşluğun “tab” tuşu kullanılarak verilmesi gerekir. Aksi takdirde “Gridde sayısal değere sahip sütun bulunamadı” şeklinde bir uyarı mesajı görüntülenir ve verilerin grafik çizimine uygun olmadığı anlaşılır.

Tüm kolonlar seçildikten sonra grafik haline getirilecek kolonlar daha sonra belirlenebilir. Sadece grafik haline getirilecek kolonların seçilmesi ve bunların grafikte gösterilmesi de sağlanabilir.

**Grafik Hazırlama Aracı**

Grafik hazırlama yöntemlerinden (raporlardan, gridden ya da dış ortamdan grafik hazırlama) herhangi biri kullanılarak "Netsis Grafik Hazırlama Aracı'na" ulaşılabilir. Bu araç ile, grafiksel olarak gösterilecek bilgiler belirlenir ve grafik detayları tanımlanır. "Grafik Hazırlama Aracı'na" tıklandığında ilk olarak “Tablo Parametreleri” ekranı açılır.

**Tablo Parametreleri**

Tablo Parametreleri, Grafiğin X ve Y eksenlerinde, gösterilecek bilgilerin seçildiği ve bu bilgilerin hangi başlık altında gösterileceğinin belirlendiği ekrandır.

Tablo Parametreleri ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Tablo Parametreleri Ekranı |  |
| --- | --- |
| Rapor Başlığı | Grafiksel olarak gösterilen raporu başlığının girildiği alandır. |
| X Sütunu Seçenekleri | Grafik gridden hazırlanıyorsa, gridde bulunan tüm kolonlar X sütunu seçeneklerinde listelenir. Rapordan ya da diğer ortamlardan kopyalanan verilerden oluşturulduğu zaman, seçili olan kolonların tamamı listelenir. Grafiğin X ekseninde gösterilecek kolonun, listelenen kolonlar arasından seçilmesi gerekir. |
| Y Sütunu Seçenekleri | Gridden grafik hazırlandığında, griddeki tüm sayısal kolonların, rapordan ya da diğer ortamlardan hazırlanan grafiklerde seçilen kolonlardan sayısal verilere sahip olanlarının listelendiği bölümdür. Listedeki kolonlardan birisi seçilerek raporun Y sütununda gösterilmesi sağlanır. |
| X Ekseni Başlığı | X ekseni için seçilen sütunun, grafikte gösterilecek başlığının izlendiği ve değiştirildiği alandır. |
| Y Ekseni Başlığı | Y ekseni için seçilen sütunun, raporda gösterilecek başlığının izlendiği ve değiştirildiği alandır. |

**Satır Aralığı**

Grafik hazırlanan ekran raporsa, “Tablo Parametreleri” adımından sonra “Satır Aralığı” ekranı görüntülenir. Kullanıcı, ilgili ekran yardımıyla raporda hangi satır aralığındaki bilgileri incelemek istediğine karar verir. Griddeki veya diğer ortamlardaki bilgilerden grafik hazırlarken satır aralığı belirlenmez. Gridde; tüm satırlar, dış ortamdaki verilerde; fare yardımıyla seçilmiş olanlar grafiğe dahil edilir.

Kullanılacak Satır Aralığı: Raporda bulunan verilerin başlangıç ve bitiş satırlarının izlendiği bölümdür.

İlk Satır: Rapor ekranında listelenen bilgilerden, grafik çiziminde hangi satırın başlangıç kabul edileceğinin gösterildiği alandır. Rapor ekranında iken rapor alınması istenen bölüm fare ile işaretlendiği için, bu bilgi otomatik olarak ekrana getirilir. Gelen satır bilgisi, "Kullanılacak Satır Aralığı" bölümünde, verilen aralıktaki başka bir satırla değiştirilebilir.

Son Satır: Rapor ekranında listelenen bilgilerden, grafik çiziminde hangi satırın bitiş kabul edileceğinin gösterildiği alandır. Rapor ekranında iken grafik halinde alınması istenen bölüm fare ile işaretlendiği için, bu bilgi otomatik olarak ekrana getirilir. İstendiğinde, "Satır Aralığı" bölümünde görülen aralıktaki başka bir değer ile değiştirilebilir.

Grafik (Chart) tipini seçiniz: Oluşturulacak grafik görünümünün seçildiği bölümdür. Ekranda örneği bulunan grafik tiplerinde grafik oluşturulması sağlanır.

**Genel Ayarlar**

Grafikler 3D Şeklinde Gösterilsin: Grafiğin üç boyutlu gösterimi için kullanılan parametredir. İşaretlenmediği zaman, görünüm iki boyutlu olarak ekrana gelir.

Seçim Aşamasında Animasyon Kullanılsın: Grafik tipi seçimi sırasında, grafiklerin hareketli olarak gösterilmesini sağlayan seçenektir.

Grafik Tipi: Grafik tipinin seçildiği bölümdür. Ekranda örnekleri görülen tiplerden biri fare ile seçildiğinde, seçilen tipe uygun olarak grafik oluşur.

**Grafik Gösterim Özellikleri**

"Grafik Tipi" seçildikten sonra ekrana gelen bu sayfada, seçilen veriler grafiksel olarak gösterilir. Ekranın sağ tarafında "Grafik Gösterimi" bulunur. Solda ise, grafiğin gösterimine ait bazı seçenekler yer alır. Bu seçeneklere göre, grafik üzerinde değişiklikler yapılabilir.

Eksenlere Ait Parametreler: Eksenlerin görünümü ile ilgili bazı değişikliklerin yapılmasını sağlayan bölümdür. Burada bulunan parametreler, her grafik tipi için kullanılamayıp, grafik tipleri bazında değişkenlik gösterir. Eksenlere ait parametreler ile X ve Y ekseninde bulunan bilgilerin grafikten taşması engellenebilir ya da bu eksenlerde bulunan verilerin test olarak gösterilmesi sağlanabilir.

**Örneğin;** X ekseninde bölgeler; Ege, Marmara ve İç Anadolu sırasına göre gösterilirken, sıralamanın İç Anadolu, Marmara ve Ege olacak şeklinde gösterilmesi sağlanabilir.

Üst Başlık: Grafiğin üst bölümünde bulunan başlık ile ilgili düzenlemelerin yapıldığı bölümdür. "Başlık Gösterilsin" seçeneği işaretlendiğinde, "Tablo Parametreleri" bölümünde belirlenen grafik başlık gösterilir. Başlık; grafiğin sağında, solunda ya da ortasında gösterilebilir. Başlığın gösterileceği yer ise, parametrenin altında bulunan seçenek kutucuğundan seçilebilir. Başlığın yazı karakteri, rengi, boyutu gibi ayarların yapılması için "Font" seçeneği kullanılır. Yapılan "Font" seçimleri sonucu, başlık gösteriminin nasıl olacağı "Font" başlığı altındaki metinden izlenir.

Alt Başlık: Grafik olarak gösterilecek raporda alt başlık olması halinde, alt başlığın gösterilip gösterilmeyeceği ya da ekranın neresinde ve ne şekilde gösterileceği ile ilgili tanımlamaların yapıldığı bölümdür.

**Grafik Etiketleri**

Grafikte gelen verilere ait etiketlerin gösterim şeklinin düzenlendiği bölümdür.

**Örneğin;** Grafik tipi olarak "BarSeries" seçildiğinde, her bar üzerinde, hangi veriye ait olduğunun gösterilmesi amacıyla etiket eklenebilir. Bunun için “Gösterilsin” seçeneğinin işaretlenmesi gerekir.

Legend: Grafikle gösterilen bilgilerin, grafiğin üst kısmında özet olarak gösterildiği bölümün, ekrandaki yerinin ve görünümle ilgili özelliklerinin ayarlanmasını sağlayan bölümdür.

**Örneğin;** Sol % ve Sağ % seçenekleri ile, grafikte gösterilen değerlerin toplam içindeki yüzdelerinin göstergede izlenmesi sağlanabilir. Alınan raporun bölgeler bazında satış tutarları olduğu varsayıldığında; X ekseninde bölgeler, Y eksininde bölge bazında satış tutarları gösterilsin.

Bu durumda, herhangi bir bölgenin satış tutarının toplam satış tutarına oranı asıl grafikte gösterilmeyerek, göstergeden izlenir.

Sayfalama: Grafiğin kaç sayfadan oluşacağı ve bir sayfada kaç nokta gösterileceği gibi düzenlemelerin yapıldığı bölümdür. Sayfalar arasında geçiş işlemi de yine bu bölümden yapılabilir.

Yazıcı İşlemleri: Oluşturulan grafiğin yazıcıya gönderilmesi ile ilgili işlemlerin yapıldığı bölümdür. Burada bulunan seçenekler ile, grafiğin basılacağı yazıcının seçimi, yazıcı ile ilgili diğer ayarların yapılması, grafiğin yazdırılması ve basımda geçerli olacak çözünürlüğün seçimi mümkündür.

Zoom İşlemleri: Grafikle ilgili yakınlaştırma ve uzaklaştırma işlemlerinin yapıldığı bölümdür.

Dosya Saklama: Grafiğin "Bitmap" ya da "Metafile" olarak saklanması işleminin yapıldığı bölümdür. Bitmap/Metafile (\*.bmp / \*.wmf) seçeneği ile grafiğin hangi dizine, hangi isimle saklanacağının sorgulandığı ekran görüntülenir.

Arka Alan İçin Resim: Grafik alanının arka planına resim dosyası eklenmesi ve daha sonra bu dosyanın kaldırılması mümkündür. Resim eklemek için "Dosyadan Resim Okuma" seçeneği kullanılır. Bu seçenek ile, eklenecek resim dosyası seçilebilir. Grafiğe eklenecek resim dosyalarının mutlaka Bitmap ya da Metafile (\*.bmp / \*.wmf) formatında olması gerekir. Eklenen resimlerin ortalanması, dağıtılması ya da genişletilmesi mümkündür.

Gradient Renk Kullanımı: Renk ölçeğinden seçilen başlangıç renginden bitiş rengine geçilerek arka plan renginin oluşturulması için kullanılan bölümdür. “Gradient renk kullanımı aktif” seçeneğinin işaretlenmemesi ile, seçilen başlangıç ve bitiş renklerinin dikkate alınmayarak arka fonun beyaz renkte gösterilmesi sağlanır. “Gradient Renk Dağılım Şekli” seçeneğinde bulunan tipler ile, başlangıç ve bitiş renkleri arasındaki geçişin nasıl yapılacağının belirlenmesi mümkündür.
