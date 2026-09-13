---
title: "İş Emri Malzeme Rezervasyonu"
page_id: "50664093"
product: "netsis-3-enterprise"
depth: 4
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Üretim"
  - "İşlemler/Üretim"
  - "İş Emri Malzeme Rezervasyonu"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Üretim / İşlemler/Üretim / İş Emri Malzeme Rezervasyonu"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPThkZWE0NjI3LTBjNzYtNGE4MC1iZTczLTkzYTRlNGRkOWE3ZCZsaW5rPWY4MDE0NzA5LWY5NDEtNGQ1NS05YTEzLTEwZjI4NTg1Y2EyMyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=8dea4627-0c76-4a80-be73-93a4e4dd9a7d&link=f8014709-f941-4d55-9a13-10f28585ca23&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "is-emri-malzeme-rezervasyonu_50664095_50664093.html"
source_version: "2022-10-12T16:06:03.217+03:00"
source_bytes: 50529
fetched_at: "2026-09-13T04:19:13+00:00"
generator: "netsis-scraper 1.0.0"
---
# İş Emri Malzeme Rezervasyonu

İş Emri Malzeme Rezervasyonu işlemi, Üretim Bölümü'nde İşlemler/Üretim menüsünün altında yer alır. İş emirleri için depolardan malzeme çekilmesini kolaylaştırmak için kullanılan bölümdür. Planlama personelinin, üretim depolarından malzeme talep ve önem sırasını kontrol etmesini sağlar.

Üretim personeli İş Emri Malzeme Rezervasyonu ekranının İş Emri Seçimi sekmesinde, depo transferi için kullanılacak fiş numarası ve tarih bilgilerini girer. Talep ekranı yardımıyla, seçilen üretim depoları için giriş/çıkış hareketlerini oluşturacak depolararası transfer fişleri oluşturulur.

İş Emri Malzeme Rezervasyonu ekranı; İş Emri Seçimi, İş Emri Kısıt Girişi ve İş Emri Malzeme Rezervasyonu olmak üzere üç sekmeden oluşur.

**İş Emri Seçimi**

İş Emri Malzeme Rezervasyonu işlemi İş Emri Seçimi sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| İş Emri Malzeme Rezervasyonu Ekranı |  |
| --- | --- |
| Rezervasyon Tipi Seçimi | İş emri malzeme rezervasyonu için rezervasyon tipinin seçildiği alandır. Rezervasyon Yap veya Rezervasyon Taşı seçenekleri arasından seçim yapılır. |
| Fiş No | Depolar arası transfer için kullanılacak fiş numarasının girildiği alandır. |
| Tarih | Depolar arası transfer için kullanılacak tarih bilgisinin girildiği alandır. |
| Fiili Tarih | Depolar arası transfer için kullanılacak fiili tarih bilgisinin girildiği alandır. |
| Çıkış Yapılacak Depolar | Çıkış yapılacak depoların seçildiği bölümdür. ![](../../../_assets/38b31798a0012cc13233.jpg) Hepsini Seç butonu ile çıkış depo kodlarının hepsinin seçilmesi sağlanır. ![](../../../_assets/12b82ca53fc4aa5346fd.png) Seçimi İptal Et butonu ile de, seçimi yapılan çıkış depo kodlarının seçiminin iptal edilmesi sağlanır. |
| Giriş Yapılacak Depolar | Giriş yapılacak depoların seçildiği bölümdür. Giriş depo kodlarının seçilmesini sağlar. |
| Malzemeler Bulundukları Depoya Rezerve Edilsin | Giriş depo kodu seçimi kapatılıp bunun yerine çıkış deposunda bakiyesi bulunan ürünlerin, yine çıkış yaptıkları depoya otomatik olarak rezerve edilmesi için kullanılan seçenektir.<br>**Örneğin;** Normalde, Çıkış Depo bölümünden 1 ve 2 No'lu depoların seçildiği ve Giriş Depo bölümünden de 3 No'lu deponun seçildiği varsayıldığında, seçilen iş emri malzeme olarak 100 adet HM1 tükettiği zaman HM1 bakiyesi çıkış depolarda sırasıyla aranır. 50 adet Depo 1'de, 50 adet Depo 2'de olsun. Depo 1'den Giriş Depo olan Depo 3'e 50 adet taşınır (DAT Kaydı), Depo 2'den Giriş Depo olan Depo 3'e 50 adet taşınır (DAT Kaydı). Malzemeler Bulundukları Depoya Rezerve Edilsin seçeneği işaretlendiğinde; Depo 1'den Depo 1'e 50 adet rezervasyon, Depo 2'den Depo 2'ye 50 adet rezervasyon için DAT Kaydı yapılmaz. Çünkü, depo değişmez. |
| ![](../../../_assets/e1aa2732c9793caadbb8.jpg) İleri | İş Emri Kısıt Girişi sekmesine ilerlemek için kullanılan butondur. İş emri, mamul ve hammadde bazında kısıtlar girilerek, alttaki gridde sadece istenen iş emirlerinin listelenmesi sağlanır. Malzeme çıkışı başlatılması istenen iş emirleri listeden seçilir. Bu seçim ve kısıt girişlerinden sonra, malzeme çekilmesi için detaylı bilgilerin listelendiği İş Emri Malzeme Rezervasyonu sekmesi hazır hale gelir. |

**İş Emri Kısıt Girişi**

İş Emri Malzeme Rezervasyonu işlemi İş Emri Kısıt Girişi sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| İş Emri Malzeme Rezervasyonu Ekranı |  |
| --- | --- |
| İş Emri No Maskesi | İş emri malzeme rezervasyonu yapılacak iş emri numarasının girildiği alandır. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile, iş emri numaraları arasından seçim yapılır. Açık bir iş emri numarasının girilmesi gerekir. |
| Referans İş Emri No Maskesi | İş emri malzeme rezervasyonu yapılacak referans iş emri numarasının girildiği alandır. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile, iş emri numaraları arasından seçim yapılır. Açık bir iş emri numarasının girilmesi gerekir. |
| Teslim Tarihi | İş emri numaraları için teslim tarihi kısıdı verilen alandır. Başlangıç ve bitiş teslim tarihinin girilmesini sağlar. |
| İş Emri | İş emri için kısıt verilen alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile; Hepsi, Tamamı Transfer Edilmiş İş Emirleri Getirilsin, Tamamı Transfer Edilmiş İş Emirleri Getirilmesin ve Tamamı Transfer Edilebilir İş Emirleri Getirilsin seçenekleri arasından seçim yapılır. |
| Set Miktarlarını Getir | İş emri malzeme rezervasyonu ekranına, girilen kısıtlara uygun set miktarlarının getirilmesi için kullanılan seçenektir. Set Miktarı: Set miktarı, üretime başlanması için gerekli olan tüm bileşenlerin mevcut depo bakiyeleri kontrol edilerek, üretilebilecek mamul miktarını belirtir. Bu hesaplama için bileşenlerin bakiyesi en küçük olan baz alınarak diğer bileşenlerden ne kadar talep edilmesi gerektiği tespit edilir. **Örneğin;** Ürün C için reçete A ve B bileşenlerinden oluşsun. A’nın bakiyesi 70, B’nin bakiyesi 100 ise, en fazla 70 adet C üretileceğinden, 100 adet C üretmek için girilmiş bir iş emrine, B’den de 70 tane çekilmesi gerektiği kolaylıkla anlaşılabilir.<br>Bazı reçetelerde üretim yapılmasını etkilemeyecek - vida, kapak gibi - bazı bileşenler bulunabilir. Bu tür bileşenlerin set miktarı uygulamasında takip edilmesi istenmediği zaman, mamulün reçetesinde bu durumdaki bileşenler için Set Miktarı Hesaplamasında Kontrol Edilmesin seçeneğinin işaretlenmesi gerekir. |
| Toplam Rezerve Miktarı Getir | İş emri malzeme rezervasyonu ekranına toplam rezerve miktarının getirilmesi için kullanılan seçenektir. |
| Toplu Rezervasyon Politikası | Toplu rezervasyon politikası için kullanılan alandır. Bileşen İhtiyacının Tamamı Rezerve Edilebilen İş Emirleri Rezerve Edilsin ve Bileşen İhtiyacının Kısmi Rezerve Edilebilen İş Emirleri Rezerve Edilsin olmak üzere iki seçenekten oluşur. |
| DAT Belgeleri İçin Miktarlar Stok Bazında Kümüle Edilsin | Depolar Arası Transfer belgeleri için miktarların stok bazında kümüle edilmesi için kullanılan seçenektir. |
| Mamul Kodu Maskesi | İş emri malzeme rezervasyonu için mamul kodu maskesi kısıdı verilen alandır. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile, stok kodları arasından seçim yapılır. |
| İleri Kısıt Ver | Mamul için ileri kısıt verilmesi istendiğinde kullanılan seçenektir. Klavyede bulunan \<tab\> tuşu ile ilerlendiğinde Stok İleri Kısıt Ekranı görüntülenir. |
| Bağlantılı İş Emirleri Getirilsin | İş emri malzeme rezervasyonu ekranına, girilen mamul kodu ile bağlantılı olan iş emirlerinin getirilmesi için kullanılan seçenektir. |
| Hammadde Kodu Maskesi | İş emri malzeme rezervasyonu için hammadde kodu maskesi kısıdı verilen alandır. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile, hammadde kodları arasından seçim yapılır. |
| ![](../../../_assets/e790827aa88a0ab2e051.png) İş Emirlerini Listele | Girilen kısıtlara uygun iş emirlerinin grid ekranda listelenmesi için kullanılan butondur. |
| ![](../../../_assets/38b31798a0012cc13233.jpg) Hepsini Seç | Grid ekrana listelenen iş emirlerinin hepsinin seçilmesi için kullanılan butondur. |
| ![](../../../_assets/9f77dcdb92897fa07bf9.png) Seçimleri Kaldır | Grid ekranda seçilen iş emirlerinin seçimlerinin kaldırılması için kullanılan butondur. |
| ![](../../../_assets/d0d615df44d602f6775d.png) Excel'e Aktar | Grid ekrana listelenen iş emirlerini Excel'e aktarmak için kullanılan butondur. |
| ![](../../../_assets/d22a7d7b5ee5869d7e59.png) Geri | İş Emri Girişi sekmesine geri dönmek için kullanılan butondur. |
| ![](../../../_assets/509ca33f831549923dcb.png) İleri | İş Emri Malzeme Rezervasyonu sekmesine ilerlemek için kullanılan butondur. |
| ![](../../../_assets/166bfaec92738b059bf1.png) Toplu Rezervasyon | Toplu rezervasyon yapmak için kullanılan butondur. |

**İş Emri Malzeme Rezervasyonu**

İş Emri Malzeme Rezervasyonu işlemi İş Emri Malzeme rezervasyonu sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| İş Emri Malzeme Rezervasyonu Ekranı |  |
| --- | --- |
| ![](../../../_assets/4044b9742267919feafe.png) Yazdır | İş emri için malzeme rezervasyon formunun yazdırılmasını sağlayan butondur. |
| ![](../../../_assets/c75839bf5e8bed8cdbe8.png) Sakla | İş emri için malzeme rezervasyon formunun saklanmasını sağlayan butondur. |
| ![](../../../_assets/3bc481e2dca87318c0a8.png) İş Emirlerini Listele | Girilen kısıtlara uygun iş emirlerinin listelenmesini sağlayan butondur. |
| ![](../../../_assets/ef90cde5377ba601829d.png) Önceki İş Emri | Bir önceki iş emrinin görüntülenmesi için kullanılan butondur. |
| ![](../../../_assets/b3adc680fdf0348e34e9.png) Sonraki İş Emri | Bir sonraki iş emrinin görüntülenmesi için kullanılan butondur. |
| ![](../../../_assets/051549e489ee4ea47813.png) Oluşan Belgeleri Listele | Mevcut oturumda oluşturulan belgelerin listelenmesi için kullanılan butondur. |
| ![](../../../_assets/30e10e07eaa1eb2fa841.png) Eksik Malzemeleri Tamamla | Eksik malzemelerin tamamlanması için kullanılan butondur. Butona tıklandığında ekrana gelen Rezervasyon işlemlerini gerçekleştirecek belgeler oluşturulsun mu? uyarısına Evet butonuna tıklanarak yanıt verildiğinde, rezervasyon için eksik belgeler oluşturulur. |
| ![](../../../_assets/f3ba29a11a085b4b427b.png) Giriş Ekranına Dön | İş Emri Seçimi sekmesine dönmek için kullanılan butondur. |
| ![](../../../_assets/b1ac5b4ee874768f200e.png) Çıkış | Rezervasyon işlemleri gerçekleştirildikten sonra ekrandan çıkmak için kullanılan butondur. Butona tıklandığında Seçilen iş emirleri arasında rezervasyon işlemi gerçekleştirilmemiş olanlar var. Çıkmak istediğinizden emin misiniz? uyarısı ekrana gelir. Tüm iş emirleri için rezervasyon işlemi gerçekleştirilmişse Evet butonuna tıklanarak yanıt verilir. |
| Set Miktarı | Reçetede bulunan hammaddelerden - otomatik reçeteler dahil - üretim sonu kaydına kadar gerek duyulmayanlar (Reçetede set miktarın hesaplanmasına dahil edilmeyenler) hariç dikkate alınarak iş emrinde yer alan üründen kaç tane üretilebileceğini ifade eder. Mamul reçetesindeki tüm hammaddeler göz önüne alındığında üretimi tamamlanacak mamul sayısını gösterir. Set miktarı alanının yanındaki bar kullanılarak, iş emri için istenen set miktarı seçilir ve ![](../../../_assets/595019dcd33846604329.png) Güncelle butonu ile, aşağıdaki hammadde listesine yansıtılır. |
| DİE Bakiye | Listedeki hammaddeler için DİE Bakiye (Diğer İş Emri Bakiye) sütununda toplamlar gösterilir. Bunun yanı sıra, satır bazında detaylı olarak hangi iş emirlerinde ne miktarlarda ihtiyaç bulunduğunu görmek de mümkündür. |
| ![](../../../_assets/488dfb24e0c91830ca52.png) Bileşen Bul | Listelenen bileşenler içinde arama yapmak için kullanılan butondur. |
| ![](../../../_assets/1e79dc74b6cfbbcf442c.png) Belgeleri Oluştur | Depolar Arası Transfer fişlerinin oluşturularak ekranda listelenmesi için kullanılan butondur. |

İş Emri Malzeme Rezervasyonu ekranında yapılan iş emirlerine stok ayırma işlemleri sonucunda oluşan verilerle, iş emirlerinin malzeme durumunu gösteren rapor alınabilir.

**Örneğin;**

İş Emri Malzeme Rezervasyonu ekranında rezerve edilmemiş (Reçetede set miktar hesaplamasına dahil edilmemiş) hammaddeleri göstermek üzere hazırlanan standart raporun çıktısı alınabilir.

Bunun dışında da, serbest raporlar kullanılarak, ihtiyaca uygun şekilde iş emri malzeme durumu raporları üretmek mümkündür.
