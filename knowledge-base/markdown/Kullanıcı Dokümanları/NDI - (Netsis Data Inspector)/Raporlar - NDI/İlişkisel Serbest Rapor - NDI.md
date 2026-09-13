---
title: "İlişkisel Serbest Rapor / NDI"
page_id: "50682928"
product: "netsis-3-enterprise"
depth: 4
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "NDI - (Netsis Data Inspector)"
  - "Raporlar / NDI"
  - "İlişkisel Serbest Rapor / NDI"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / NDI - (Netsis Data Inspector) / Raporlar / NDI / İlişkisel Serbest Rapor / NDI"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTdkMzAwNGFhLTUxNGQtNDg5NS1iZjcxLTAxMTlmMDliZTRjNSZsaW5rPTA4ODJkMzI2LWFhOWMtNDUzMi1hM2ZmLWZkZjFhODMxZjcxMSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=7d3004aa-514d-4895-bf71-0119f09be4c5&link=0882d326-aa9c-4532-a3ff-fdf1a831f711&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "iliskisel-serbest-rapor-ndi_90669262_50682928.html"
source_version: "2022-09-16T15:05:23.637+03:00"
source_bytes: 421040
fetched_at: "2026-09-13T04:20:58+00:00"
generator: "netsis-scraper 1.0.0"
---
# İlişkisel Serbest Rapor / NDI

İlişkisel Serbest Rapor, NDI Bölümünde, "Raporlar" menüsünün altında yer alır. "İlişkisel Rapor" bölümünde, birden fazla tablo veya görüntü birbiriyle ilişkilendirilerek kapsanan kayıtların raporlanması sağlanır. İlişkisel Rapor, bir ana tablo/görüntü (Stok Sabit Kayıtları, Cari Sabit Kayıtları, Personel Sabit Bilgileri gibi) ve bu ana görüntüye bağlı tablo/görüntüler (Stok Hareketleri, Cari Hesap Hareketleri, Personel Kartoteks Kayıtları gibi) şeklinde bağlantılarla oluşturulur. Rapor listelenirken de ana kayıtlar (Stok Sabit Bilgisi gibi) ve her bir ana kayda bağlı alt kayıtlar (ilgili stok kaydının hareketleri gibi) listelenir.

"İlişkisel Rapor" hazırlamak için, programın araç çubuğunda yer alan "Rapor" modülünün işaretlenmesi gerekir.

![](../../../_assets/58385ed94d3d063e81d9.png)

**İlişkisel Serbest Rapor Sihirbazı**

İlişkisel Serbest Raporlar, "İlişkisel Serbest Rapor Sihirbazı" aracılığıyla hazırlanır. Sihirbaz, raporun hazırlanması aşamasında kullanıcıyı yönlendirir.

**Rapor Dosyası Belirleme**

Hazırlanan raporla ilgili rapor sihirbazında yapılan tanımlamalar bir dosyada saklanır. İlişkisel Serbest Rapor Sihirbazının ilk sekmesi, dosya ismini belirlemek için kullanılır.

![](../../../_assets/3c5557f94f5ef024dab9.png)

İlişkisel Serbest Rapor Sihirbazı ekranında yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| İlişkisel Serbest Rapor Sihirbazı Ekranı |  |
| --- | --- |
| Yeni Rapor Dosyası | Sihirbaz içinde, yeni ve sıfırdan bir rapor hazırlanacağı zaman kullanılan seçenektir. |
| Rapor Dosyasını Düzenle | Önceden hazırlanan ve saklanan bir raporun tekrar düzenlenmesi ya da düzenlenmeden tekrar rapor alınması için işaretlenmesi gereken seçenektir. |
| Dosya İsmi | Sihirbazda tanımlamalara başlamadan önce, önceden tanımlanan rapor dosyası ya da yeni rapor dosyası üzerinde çalışmak için mutlaka bir dosya isminin belirtilmesi gerekir. Dosya ismi ve yeri, alanın sağ tarafında yer alan üç nokta ![](../../../_assets/e577cf0766513395a6ad.jpg) butonu ile belirlenir. |
| ![](../../../_assets/f5e31757087faaeac54b.png) Çalıştır | Önceden tanımlı bir rapor dosyası açıldığında aktif hale gelen butondur. Sihirbazda herhangi bir düzenleme yapılmayacaksa, bu buton yardımı ile doğrudan rapor çalıştırılabilir. |
| ![](../../../_assets/3d436647c2cd6ab8842d.png) Geri | Geçerli bir dosya ismi belirlendiğinde aktif hale gelen butondur. Geri butonu ile, sihirbazın geri sekmelerine geçilir. |
| ![](../../../_assets/ccd70a9b860d515ff68c.png) İleri | Geçerli bir dosya ismi belirlendiğinde aktif hale gelen butondur. İleri butonu yardımı ile, sihirbazın sonraki sekmelerine geçilir. |
| ![](../../../_assets/e1e7e4f9572282e2ff15.png) İptal | İşlemin iptal edilmesini sağlayan butondur. |

**İlişkilendirilecek Görüntülerin Seçimi**

İlişkisel Serbest Rapor Sihirbazının ikinci sekmesinde, ilişkilendirilecek görüntüler seçilir.

![](../../../_assets/27c1548a8678081eb074.png)

İlişkilendirilecek Görüntülerin Seçimi sekmesinde yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| İlişkisel Serbest Rapor Sihirbazı Ekranı |  |
| --- | --- |
| Kayıtlı Görüntüler | Üzerinde çalışılan veri tabanında kayıtlı tüm görüntüler, ekranın sol tarafında yer alan pencerede listelenir. Görüntüler, farenin sol tuşu ile çift tıklayarak ya da "sürükle bırak" yöntemiyle, sağ taraftaki seçilen görüntüler penceresine aktarılır. |
| Rapor Adı | Kayıtlı görüntüler içinden seçilen ilk görüntü adı, rapor adı olarak aktarılır. Rapor başlığı olarak kullanılacak bu bilgi, istenen şekilde değiştirilebilir. |
| Seçilen Görüntüler | Kayıtlı görüntülerden aktarılan görüntü isimleri, ekranın sağ tarafındaki alanda yer alır. İlk eklenen görüntü, ana görüntüdür. Sonradan eklenen görüntüler ise, ana görüntüye bağlı olarak düşünülür. Ek görüntülerin, ana görüntüye değil, alt görüntülerden birine bağlı olması için, ek görüntü, bağlanması istenen görüntünün içine sürüklenip bırakıldığında, görüntü bağlantısı otomatik düzeltilir. Seçilen Görüntüler penceresinde, yanlış tanımlanan bir görüntüyü çıkarmak için, görüntünün "Sürükle Bırak" yöntemiyle "Kayıtlı Görüntüler" penceresine bırakılması gerekir. Çıkarılan görüntüye bağlı görüntüler ve bu görüntülerle ilgili, sihirbazın ilerleyen bölümlerinde yapılmış tanımlamalar varsa, bunlar da otomatik olarak çıkarılır. Bu yüzden, raporla ilgili diğer tanımlamalara geçmeden önce, görüntülerin ve ilişkilerin doğru olarak belirlenmesi önemlidir. **Örnek 1** İlk eklenen görüntü STGRUP (Stok Grup Kodları), sonrasında eklenen görüntüler STSABIT (Stok Kartları) ve STHAR (Stok Hareketleri) olduğunda; ilk aşamada eklenen her iki görüntü de, STGRUP'a bağlı görünür. Ancak, STHAR görüntüsü, STGRUP'a bağlı olamaz. "Stok Kodu" alanı üzerinden sadece STSABIT ile ilişkilendirilebilir. Bu durumda, STHAR görüntüsü fare ile tıklanarak sürüklendikten sonra STSABIT görüntüsünün içine bırakıldığında, otomatik olarak STGRUP → STHAR ilişkisi iptal edilir ve STSABIT → STHAR ilişkisi oluşturulur. **Örnek 2** STGRUP → STSABIT → STHAR şeklinde oluşturulan ilişkisel raporda, stok grup kodları, ana kayıtlar olarak listelenir. Her grup kaydı açıldığında, bu gruba ait stok kartları listelenir ve grup içindeki her bir stok kartı kaydı açıldığında, bu karta ait hareketler listelenir. STGRUP → STSABIT ilişkisini sağlayan saha, her iki görüntüde bulunan grup kodu sahasıdır. STSABIT → STHAR ilişkisini sağlayan saha ise stok kodu sahasıdır ve bu görüntülerin ilgili sahalar üzerinden ilişkilendirilmesi bir sonraki sekmeden yapılır.<br>Bu ilişkiyi, STSABIT → STGRUP → STHAR şeklinde yapmak yanlış olurdu. Çünkü, her bir STSABIT ana kaydı için sadece bir tane geçerli STGRUP kaydı vardır (Bir stok kartının sadece bir grup kodu olabilir). Bu şekilde tanımlanan ilişkisel raporda, stok kartları ana kayıtları listelenir ve her bir ana kayıt açıldığında grup kaydı izlenebilir. Aslında buna gerek yoktur. STSABIT görüntüsünde hazırda mevcut olan grup kodu sahası, STSABIT ana kayıtlarında bir saha olarak görüntülenebilir. İstendiği zaman, grup açıklaması da bir saha olarak görüntü ve listeye eklenebilir. Bu durumda, STGRUP için ayrı bir ilişki yaratmaya gerek kalmaz. |
| Dikkat, Raporun Performans Maliyeti | Raporda tanımlanan ana görüntü için bir rapor, ana görüntüye ait bir ilişki için her bir ana kayıt altında listelenecek alt kayıtlar için yeni bir rapor oluşturulur. Örneğin, raporda listelenen ana kayıt sayısı 10 ise ve bir ilişkili görüntü olup, her bir ana kayıt için de alt kayıtların mevcut ve listeleneceği düşünüldüğünde; ana kayıtlar için 1 + her bir ana kayıt için 10\*1 = toplam 11 tane rapor oluşturulur. Listelenecek ana ve alt ilişki sayısı, açılacak rapor sayısını belirler. Bu sayılar arttıkça, rapor performansı etkilenebilir. Bu sebeple, doğru ilişki tanımları ve kayıt filtresi *ile* sonuç kümesi daraltması, optimum raporun elde edilmesini sağlar. |
| Kayıtlı Görüntüler Aç/Kapa | "Kayıtlı Görüntüler" penceresi ile "Seçilen Görüntüler" penceresi arasında bulunan bu ekran bileşeni sayesinde, "Kayıtlı Görüntüler" penceresinin kapatılarak, "Seçili Görüntüler" penceresinin genişletilmesi sağlanır. Kayıtlı görüntüler penceresi kapalı iken, tekrar aynı bileşen farenin sol tuşu ile tıklanarak açılabilir. |
| ![](../../../_assets/3d436647c2cd6ab8842d.png) Geri | İlişkilendirilecek görüntüler belirlendikten sonra bir önceki sekmeye geçilmesini sağlayan butondur. |
| ![](../../../_assets/ccd70a9b860d515ff68c.png) İleri | İlişkilendirilecek görüntüler belirlendikten sonra bir sonraki sekmeye geçilmesini sağlayan butondur. |

**Görüntüler Arası Bağlantılar**

Görüntüler Arası Bağlantılar sekmesinde, görüntü seçimi ve görüntü ilişkileri belirlendikten sonra, ilişkileri sağlayacak olan bağlantılar belirlenir. Görüntüler Arası Bağlantılar sekmesinde, tüm görüntüler için bağlantıların tanımlanması gerekir.

![](../../../_assets/fe1b25fce814aabc9c94.png)

Görüntüler Arası Bağlantılar sekmesinde yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| İlişkisel Serbest Rapor Sihirbazı Ekranı |  |
| --- | --- |
| Seçili Görüntü | Bir önceki sekmede seçilen ve ilişkilendirilen görüntülerin yer aldığı penceredir. Bu görüntüler içinden, bağlantısı tanımlanacak görüntü farenin sol tuşu ile bir kez tıklanarak seçilir. Ana görüntü için herhangi bir bağlantı tanımlanmaz. Eklenen görüntülerin bağlantıları tanımlanır. Eklenen görüntü seçildiğinde, eklendiği görüntüyle arasındaki bağlantının yapılacağı anlamına gelir. **Örneğin** STSABIT → STHAR görüntüleri arasındaki bağlantının tanımlanması için STHAR görüntüsünün seçilmesi gerekir. Seçilen görüntü ismi, pencere başlığında görünür. Tablo ve Bağlantı Tablosu Sahaları; bağlanacak görüntü belirlendiğinde, bu görüntü "Tablo" bölümünde ve bağlantısı yapılacak ana görüntü, "Bağlantı Tablosu" bölümünde yer alır. Her iki bölümde yer alan seçim kutularındaki görüntülerde mevcut sahalar listelenir. Seçim kutularının sağ tarafında yer alan aşağı ok butonu yardımıyla açılan saha listesinden, ilişkilendirilecek olan sahanın/sahaların seçilmesi gerekir. |
| ![](../../../_assets/2289ec10ee63fca1f7e9.png) Ekle veya Çıkar Butonu | Oluşturulan bir ilişkinin eklenmesi ya da yanlış oluşturulan bir ilişkinin çıkarılması için kullanılan butonlardır. **Örnek 1** STGRUP → STSABIT arasındaki bağlantı, STSABIT görüntüsündeki GRUP_KODU ile, STGRUP görüntüsündeki GRUP_KODU sahaları üzerinden yapılır. Bunun anlamı, raporda her bir grup ana kaydı için listelenecek kayıtlar, STSABIT.GRUP_KODU=STGRUP.GRUP_KODU eşitliğini sağlayan kayıtlardır (ilgili grupta yer alan stoklar). **Örnek 2** STSABIT → STHAR arasındaki bağlantı, STHAR görüntüsündeki STOK_KODU ile, STHAR görüntüsündeki STOK_KODU sahaları üzerinden yapılır. Bunun anlamı, raporda, her bir grup ana kaydı için listelenecek kayıtlar, STHAR.STOK_KODU=STSABIT.STOK_KODU eşitliğini sağlayan kayıtlardır (ilgili stokun hareketleri). ![](../../../_assets/2d422a3a42c71d62d93c.png) **Örnek 3** Görüntüler arasındaki bağlantının birden fazla saha gerektirdiği durumlarda, bağlantıyı sağlayan tüm sahaların görüntüler arasından karşılıklı olarak seçilerek eklenmesi gerekir. **Örnek 4** SICIL (Personel Sabit Bilgileri) → KARTX (Personel Kartoteks Bilgileri) arasında bağlantı, (SICIL.ISYERI=KARTX.ISYERI AND SICIL.SICILNO=KARTX.SICILNO) eşitliği üzerinden kurulabilir. Bu durumda, önce her iki görüntünün ISYERI sahaları seçilerek eklenmesi, daha sonra da SICILNO sahaları seçilerek eklenmesi gerekir. |
| ![](../../../_assets/3d436647c2cd6ab8842d.png) Geri | Bağlantılar belirlendikten sonra bir önceki sekmeye geçilmesini sağlayan butondur. |
| ![](../../../_assets/ccd70a9b860d515ff68c.png) İleri | Bağlantılar görüntüler belirlendikten sonra bir sonraki sekmeye geçilmesini sağlayan butondur. |

**Filtreleme**

Görüntülerdeki kayıtlar içinden filtreleme yapılarak sonuç kümesinin istenen kapsamda daraltılmasını sağlayan sekmedir. Herhangi bir kısıtlama yapılmayacaksa, boş bırakılarak bir sonraki sekmeye geçilebilir.

Filtrelemenin amacı, bir saha için veri tabanına kaydedilmiş bilgileri, verilen bir değerle karşılaştırıp, uygun kayıtları belirleyerek sonuç kümesini oluşturmaktır. Karşılaştırmanın yapılması için öncelikle, hangi sahadaki bilgilerin filtreleneceği, daha sonra hangi operatör kullanılarak karşılaştırma yapılacağı ve hangi değerle karşılaştırılacağı belirlenir.

![](../../../_assets/43af2857363f098b4f25.png)

Filtreleme sekmesinde yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| İlişkisel Serbest Rapor Sihirbazı Ekranı |  |
| --- | --- |
| Seçili Görüntü | Önceki sekmelerde seçilen, ilişkilendirilen ve bağlantıları belirlenen görüntülerin yer aldığı penceredir. Bu görüntülerin içinden, kayıtları filtrelenmesi istenen görüntünün farenin sol tuşu ile tıklanarak seçilmesi gerekir. |
| Saha Adı | İlişkisel serbest rapor alınırken baz alınacak saha adı için kısıt verilen alandır. İlgili hücre üzerinde iken klavyede yer alan **Boşluk Çubuğuna** basılarak aktif hale gelen aşağı ok butonu, kısıt verilmesi istenen sahalara ulaşılmasını sağlar. Saha adı olarak "(" parantez de belirlenebilir. Parantez olarak belirlenen satırda başka bir tanımlama yapılmaz. "(" Parantez açma belirlendiğinde, otomatik olarak bir tane de ")" parantez kapatma satırı oluşur. Bu durumda, (",") satırları arasına satır ekleyerek, filtrenin iki parantez satırı arasındaki satırda tanımlanması gerekir. ![](../../../_assets/9b033d0be6ab77c29d7a.png) ![](../../../_assets/42f802df2d371bec466f.png)![](../../../_assets/16444022f71052261bce.png) |
| Operatör | "Saha Adı" alanında belirlenen sahanın içerdiği bilgilerin, karşılaştırılacağı operatörün seçildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile seçenekler arasından tercih yapılır. **Eşittir:** İçeriği, sonraki adımda belirlenecek değere eşit olan kayıtlar anlamına gelir. **Küçük:** İçeriği, sonraki adımda belirlenecek değerden küçük olan kayıtlar anlamına gelir. **Küçük Eşit:** İçeriği, sonraki adımda belirlenecek değere eşit ya da bu değerden küçük kayıtlar anlamına gelir. **Büyük:** İçeriği, sonraki adımda belirlenecek değerden büyük olan kayıtlar anlamına gelir. **Büyük Eşit:** İçeriği, sonraki adımda belirlenecek değere eşit ya da bu değerden büyük kayıtlar anlamına gelir. **Benzer:** İçeriği, sonraki adımda belirlenecek değere benzer kayıtlar anlamına gelir. SQL standartlarında kullanılan yüzde "%'" ve alt çizgi "\_" arama karakterleri, SQL cümlelerinde kullanıldıkları şekliyle geçerlidir. **Arasında:** İçeriği, sonraki adımlarda belirlenecek olan Değer 1 ile Değer 2 arasında olan kayıtlar anlamına gelir. **İçinde:** İçeriği, sonraki adımda belirlenecek olan değerlerin birine eşit olan kayıtlar anlamına gelir. Değerlerin, "Değer 1" sahasında virgülle ayrılmış olarak, alfanümerik değerler tırnak içinde olacak şekilde verilmesi gerekir. **Farklıdır:** İçeriği, sonraki adımda belirlenecek değerden farklı olan (eşit olmayan) kayıtlar anlamına gelir. **Boş:** İçeriği boş olan kayıtlar anlamına gelir. **Dolu:** İçeriği dolu olan kayıtlar anlamına gelir. |
| Değer 1, Değer 2 | Belirlenen sahanın veri tabanında içerdiği bilgiler, bu sahalarda belirlenecek olan değerin/değerlerin, belirlenen operatörle kıyaslanıp sonuç kümesi oluşturulmasını sağlar. |
| Ve/Veya | Üzerinde bulunulan satırda tanımlanacak olan filtrenin, bir önceki satırda tanımlanan filtreye ne şekilde bağlanacağı belirlenir. Ve/Veya olmak üzere iki çeşit bağlantı şekli vardır. İki filtre birbirine "Ve" ile bağlantı yapıldığında, kaydın sonuç kümesinde yer alması için her iki filtredeki koşulu sağlaması gerekir. "Veya" ile bağlantıda ise, kaydın sonuç kümesinde yer alması için iki filtredeki koşullardan birini sağlaması yeterlidir. Çok fazla sayıda filtre tanımlanıyorsa, parantezler yardımıyla koşulların doğru sıralanmasının sağlaması gerekir. |
| Değil | Parantez olarak belirlenen satırda aktif olan sahadır. Parantez içinde tanımlanacak olan filtreye uyan değil, uymayan kayıtların sonuç kümesinde yer alması için kullanılır. |
| ![](../../../_assets/3d436647c2cd6ab8842d.png) Geri | Filtreler tamamlandıktan sonra bir önceki sekmeye geçilmesini sağlayan butondur. |
| ![](../../../_assets/ccd70a9b860d515ff68c.png) İleri | Filtreler tamamlandıktan sonra bir sonraki sekmeye geçilmesini sağlayan butondur. |

İlişkisel Serbest Rapor ekranı üzerinde iken, farenin sağ tuşu ile ekrana gelen seçeneklerin kullanımı aşağıdaki şekildedir:

![](../../../_assets/b1d60ff9ef3dff2a4316.png)

| İlişkisel Serbest Rapor Ekranı |  |
| --- | --- |
| Satır Ekle | Gridin sonuna yeni bir satır eklemek için kullanılır. Klavyede yer alan "Insert" tuşu aynı işlev için kullanılabilir. |
| Araya Satır Ekle | Grid üzerinde, içinde bulunulan (seçili) satır ile önceki satır arasına boş bir satır açmak için kullanılır. Klavyede yer alan "Alt+Insert" tuşları aynı işlev için kullanılabilir. |
| Satır Sil | Grid üzerinde, içinde bulunulan satırın silinmesi için kullanılır. Klavyede yer alan "Delete" tuşu aynı işlev için kullanılabilir. |
| Temizle | Grid üzerinde, içinde bulunulan hücredeki değerin silinmesi, hücrenin boşaltılması için kullanılır. Klavyede yer alan "Backspace" tuşu aynı işlev için kullanılabilir. |
| Yukarı Kaydır/Aşağı Kaydır | Grid üzerinde, içinde bulunulan satırın yukarı/aşağı kaydırılması ile, üstündeki/altındaki satırla yer değiştirmesi için kullanılır. Bu seçenekler kaydırmanın mümkün olduğu satırlarda aktif hale gelir. Gridin alt kısmında bulunan yukarı/aşağı butonları da aynı işlev için kullanılabilir. Klavyede yer alan Ctrl+Yukarı Ok veya Ctrl+Aşağı Ok tuşları aynı işlev için kullanılabilir. |
| Cümleyi Göster | Oluşan filtrelerin, gridin altındaki bilgi sahasında cümle olarak gösterilmesini sağlar. ![](../../../_assets/477dd646b71817432be9.png) |
| Gönder | Grid içeriğinin dışa (Excel, Word, Calculator, Writer, Grafik Hazırla, Akıllı Gride Gönder) aktarılmasını sağlar. |

**Raporda Gösterilecek Alanlar**

Raporda Gösterilecek Alanlar bölümünde, raporda görüntülenmesi istenen sahalar seçilir.

**![](../../../_assets/813a3c5d58b5ed820203.png)**

Raporda Gösterilecek Alanlar sekmesinde yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| İlişkisel Serbest Rapor Sihirbazı Ekranı |  |
| --- | --- |
| Seçili Görüntü | Önceki sekmelerde seçilen, ilişkilendirilen ve bağlantıları belirlenen görüntülerin yer aldığı penceredir. Bu görüntüler içinden, rapor alanları belirlenecek olan görüntünün, farenin sol tuşu ile bir kez tıklanarak seçilmesi gerekir. "Seçili Görüntüler" penceresindeki her bir görüntü için raporda en az bir sahanın tanımlanması gerekir. |
| Görüntü Başlığı | Sahaları belirlemek üzere seçilen görüntü için, raporda yer alacak olan başlıktır. Görüntü seçildiğinde, görüntü ismi ön değer olarak otomatik şekilde ekrana gelir. İstenen şekilde değiştirilerek oluşturulabilir. |
| Tekrarları Gösterme | Görüntü için raporlanan kayıtlarda, seçilecek sahaların içerikleri birebir aynı olan kayıtların, tek seferde gösterilmesini sağlayan seçenektir. |
| Satır Limit | Görüntü için raporlanan kayıtların ilk "n" tanesini rapora dahil etmek için kullanılan seçenektir. Belirlenen sayıda kayıt, rapora dahil edilir. Çok uzun olan raporlarda, rapor hazırlama aşamasındaki denemelerde, az sayıda kayıt ile deneme yapmak için kullanışlı olabilir. |
| Saha Tipi | Raporda iki tip saha yer alır. "Normal" tipli sahalar, görüntü sahalarından herhangi biridir ve sonuç kümesindeki kayıtlarda sahanın içerdiği bilgi olduğu gibi gösterilir. "Hesaplanan" tipli sahalar ise, tanımlanacak hesaplamalar sonucu oluşan bilgiyi gösterir. Hesaplanan sahalar, öncelikle boş bir saha olarak eklenir ve daha sonra hesaplanma şekli bir sonraki sekmede "Script Girişi" bölümünden tanımlanır. |
| Saha Adı | "Normal" tipli sahalar için, alanın sağ tarafında yer alan aşağı ok butonu ile görüntü sahaları içinden seçim yapılır. Hesaplanan tipli sahalar için, CALC1, CALC2 ... şeklinde otomatik verilen isimler geçerlidir ve değiştirilemez. |
| Operatör | Bu alan kullanılmıyor. |
| Değer Tipi | "Hesaplanan" tipli sahalarda aktif hale gelen alandır. Hesaplama sonucu oluşacak bilginin, tipini belirlemek için kullanılır. Alanın sağ tarafında yer alan aşağı ok butonu ile String (Metin), Smallint (Tamsayı, -32768..32767), Integer (Tamsayı, -2147483648..2147483647), Word (Tamsayı, 0..65535), Boolean (doğru ya da yanlış değer alabilen), Float (Gerçek sayı), Currency (Para birimi), DateTime (Tarih, saat), Memo (Uzun metin) ve Graphic tipleri arasından seçim yapılır. Sonuç bilgilerinin doğru gösterilmesi için uygun saha tipinin seçilmesi önemlidir. |
| Kolon Adı | Raporda saha için görünen başlığın girildiği alandır. |
| Sırala | Seçilen saha bilgilerinin sıralanması için işaretlenen seçenektir. Alanın sağ tarafındaki kısımda, sıralamanın yapılacağı şeklin (Artan/Azalan) belirlenmesi gerekir. Aynı görüntü için birden fazla sahada sıralama işaretlenirse, sahalar bir biri içinde ve verildikleri sırada, sıralama işlemine tabi tutulur. **Örneğin;** Order by GRUP_KODU, STOK_KODU gibi bir cümle oluşturulabilir. Bu örnekte GRUP_KODU sahasının, STOK_KODU sahasından önce eklenen bir saha olması gerekir. Ancak, Order by STOK_KODU, GRUP_KODU gibi bir cümle oluşması anlamlı değildir. Stok kodu içinde grup kodu sıralamasının anlamı yoktur. |
| Ön Biçim | Bu alan kullanılmıyor. |
| Biçim | Nümerik ve Tarih tipli alanlar için görüntü biçiminin belirlendiği alandır. #### Nümerik Alan Örnekleri Kullanılan karakterler; 0 (basamak değeridir, yoksa sıfır görünür), \# (basamak değeridir, yoksa görünmez), . (ondalık ayırıcıdır), , (binlik ayırıcıdır). Değer: 0.008; Biçim: #.00 ise, 0.01 Değer: 12.2; Biçim: #.00 ise, 12.20; Biçim: #.## ise, 12.2 Değer: 8756.35; Biçim: #,###.00 ise, 8,756.35 Değer: 8756987; Biçim: #,###.00 ise, 8,756,987.00 #### Tarih Alan Örnekleri Kullanılan karakterler; d (gün değeri), m (ay değeri), y (yıl değeri) Biçim: dd/mm/yyyy ise, 13/07/2005, Biçim: dd/mm/yy ise, 13/07/05 |
| Ondalık Sistemi | Bu alan kullanılmıyor. |
| Ondalık | Bu alan kullanılmıyor. |
| Gizli | Hesaplanan sahalarda kullanılacak görüntü sahalarının mutlaka rapora eklenmesi gerekir. Bu sahaların, raporda görüntülenmesi istenmediğinde, sadece hesaplamalarda kullanılması isteniyorsa, "Gizli" seçeneğinin işaretlenmesi gerekir. |
| ![](../../../_assets/a6730ebc851851d9f3bc.png) Ekle | Tanımlanan sahanın rapora eklenmesi için, tanımlamalar yapıldıktan sonra kullanılan butondur. Eklenen saha, sağ alt köşede yer alan saha listesi penceresinden izlenir.<br>Sağ alt köşede yer alan "Saha Listesi" penceresinden farenin sol tuşu ile çift tıklayarak seçilen bir saha için, tanımlamalarda değişiklik yapıldıktan sonra "Ekle" butonuna basıldığında, seçili sahanın tanımı güncel hale gelir. |
| ![](../../../_assets/f34da78b935259703da9.png) Çıkar | Tanımlanan sahanın rapordan çıkarılması için kullanılan butondur. Raporda görünmesi istenmeyen saha, pencere içinden seçilerek "Çıkar" butonu yardımı ile çıkarılır. |
| ![](../../../_assets/ea48e3e26785e0694a67.png) Tamamını Ekle | Seçili görüntünün tüm sahalarını tek seferde rapora eklemek için kullanılan rapordur. |
| ![](../../../_assets/80f28eeefabf8346c378.png) Tamamını Çıkar | Rapora eklenen ve sağ alt pencerede yer alan tüm sahaların rapordan çıkarılması için kullanılan butondur. |

**Saha Yeri Değiştirme**

Ekranda yer alan "Saha Listesi" penceresine eklenen sahaların raporda görünüm sırasının değiştirilmesi için, ilgili saha, farenin sol tuşu ile bir kez tıklayarak seçilir. Klavyede yer alan Ctrl+Yukarı Ok ve Ctrl+Aşağı Ok tuşları yardımıyla yukarı/aşağı kaydırma yapılması gerekir.

**Hesaplama Sahaları Ekleme**

Raporun istenen sütunlarında, hesaplama sonucu değer gösterilebilir. Hesaplanan kolon ekleneceği zaman, öncelikle bu bölümde boş bir kolon oluşturulması gerekir. Hesaplama için tanımlanan saha tipinin "Hesaplanan" olması gerekir. Saha tipi "Hesaplanan" olarak belirlendiğinde, "Saha Adı" CALC1, CALC2, .... CALCn olarak, birden fazla hesaplanan saha olması durumunda ardışık olarak numaralandırılmış şekilde otomatik olarak ekrana gelir ve değiştirilemez. Hesaplanan saha için, hesaplama sonucu oluşacak değerin tipinin, "Değer Tipi" seçeneğinde belirlenmesi gerekir. "Kolon Adı" ve "Biçim", istenen şekilde belirlendikten sonra, sahanın rapora eklenmesi gerekir.
Bu aşamada, hesaplama yapılması için boş bir kolon oluşturulmuştur. Bundan sonraki bölümde, hesaplama şeklini tanımlayacak olan VBScript kodunun yazılması gerekir. VBScript kodu, bir sonraki sekmede yazılır.
Rapora eklenen sahaların tanımlamaları yapıldıktan sonra, ekranın alt kısmında aktif olan, Geri *![](../../../_assets/3d436647c2cd6ab8842d.png)* butonu ile bir önceki sekmeye, İleri *![](../../../_assets/ccd70a9b860d515ff68c.png)* butonu ile de bir sonraki sekmeye ilerlenir.

**Script Bölümü**

Script bölümünde, rapora sorgu cümleleri ile müdahale edilebilir. En önemli kullanım alanı ise, hesaplama sahalarındaki hesaplamaların ne şekilde yapılacağının tanımlanmasıdır. Script sekmesinde, herhangi bir tanımlama yapılması zorunlu değildir. Bir hesaplama sahası ya da raporun kendi normal algoritması içinde yapılması istenen farklı bir işlem yoksa, boş bırakılarak ilerlenir.

**Olay Bazlı Programlama**

Raporun tanımlamaları bittikten sonra, istenen rapor program tarafından oluşturulur. Raporun oluşturulması sırasında henüz kullanıcı ekranına gelmeden önce, yazılan sorgu cümlelerinin çalıştırılarak raporun şekillendirilmesi sağlanır. Yazılacak sorgu cümlesi, rapor oluşturulması sırasında meydana gelen olaylar sırasında çalışır.

Örneğin; raporun bir satırı tamamlandığında, o satırla ilgili bir hesaplama işlemi yaptırılabilir. Dolayısıyla, rapor oluşturma sırasında her bir satır tamamlanması, sorgu cümlesinin yazılması gereken bir olay olarak düşünülebilir.

**Geçerli Olaylar**

Rapor oluşturma sırasında meydana gelen tüm olaylar kullanıcıya açık değildir. Kullanıcı, sadece bu ortamda kendisine açılan olaylar için kod geliştirebilir. Script düzenleme bölümünde yazılan sorgu cümlesinin öncelikle mevcut olaylardan hangisi için yazılacağı belirlenir. Seçilen olay her meydana geldiğinde, yazılan kod bir kez çalışır.

Örneğin; satır tamamlanması olayı için yazılan sorgu cümlesi, raporun her bir satırı tamamlandığında bir kez çalışır.

**Rapor Olayları**

İlk olarak, ekranın sol üst köşesinde yer alan ve kullanıcıya açılan olaylardan hangisi için script yazılacağı belirlenir. Script yazılması istenen olay bu pencereden seçildikten sonra, olayla ilgili script yazılması için ekranın sağ tarafında yer alan Script bölümüne geçilir.

|  |  |
| --- | --- |
| OnReportInit | Ana rapor başlangıcı öncesidir. |
| OnReportEnd | Ana rapor bitişi sonrasıdır. |

**Mevcut Görüntüler**
İlişkisel Serbest Rapor'da seçilerek ilişkilendirilen her bir görüntü için bir rapor (grid-ızgara) açılır. Bu sebeple, her bir görüntü raporu için ayrı ayrı olay belirlenmesi gerekir. "Mevcut Görüntüler" bölümünde, hangi görüntünün raporuna ait olay/olaylar için script yazılacağı belirlenir.

| Olaylar |  |
| --- | --- |
| OnGridInit | Seçilen görüntü raporunda, her bir grid (ızgara) oluşturmadan öncesidir. |
| OnRowInit | Seçilen görüntü raporunda, grid içindeki her bir satırın oluşturulmadan öncesidir. Grid satırı oluşturulmadan önce, satırdaki değerler henüz oluşmaz. Satırdaki değerler kullanılarak yapılacak işlemler için bu olayın tercih edilmemesi gerekir. |
| OnRowEnd | Seçilen görüntü raporunda, grid içindeki her bir satırın oluşturulması bitişidir. Satırdaki veri tabanından okunan değerler oluşmuş olacağından, bu değerler kullanılarak yazılacak olan hesaplama işlemleri için en uygun olaydır. |
| OnGridEnd | Seçilen görüntü raporunda, her bir grid (ızgara) bitişidir. Hangi olay için script yazılacağı seçildikten sonra, sağ tarafta yer alan kod penceresine geçilebilir.<br>Sekme ilk açıldığında, OnReportInit olayı seçili şekilde ekrana gelir. Başka bir olay seçilmeden yazılan kod, OnReportInit olayı için geçerlidir. |

**Sahalar**
Ekranın sol tarafında bulunan penceredeki "Sahalar" sekmesi, yardım amaçlı olarak, rapor için tanımlanan sahaları gösterir.

**Scripting (Kodlama)**

Scripting bölümünde, VBScript söz dizimi (sentaks) kullanılarak kod yazılması gerekir. Yazılan sorgu cümlesi, sadece rapor oluşturulması sırasında algılanarak çalıştırılır. Hatalı yazım varsa, raporda hata oluşur.

**Programlama Elemanları**
VBScript ile kullanılabilen, If Then Else, Sub, Function, Select Case, For Next, Do Loop gibi programlama elemanları geçerlidir. Dokümanda VBScript ile program yazımı ve söz dizimi (sentaks) standartları açıklanmaz. Kullanıcıların bu bilgiye sahip olduğu varsayılır.

**Geçerli Nesneler**

Bu ortamda, "İlişkisel Serbest Rapor" için script yazılması sağlanır. İlişkisel serbest raporda mevcut bazı nesneler ile, sahip oldukları özellik ve metotlar kullanıma açık şekildedir. Bu nesneler, raporu oluşturan nesneler olup raporun gridine, satırına, hücresine gibi değer atanması için ya da bir değer alınması için kullanılır. Nesneler ile çalışmak için, nesne tabanlı programlama prensiplerine aşina olunması gerekir. Dokümanda, nesne tabanlı programlama ile ilgili detay bilgi verilmez. Kullanıcıların bu bilgiye sahip olduğu varsayılır.

**Netsis Code Insight**
Bu pencerede, klavyede yer alan Ctrl+Boşluk tuşları ile, ortamda kullanılacak nesneler görüntülenir. Kullanılacak nesne, pencereden seçildikten sonra kodlama bölümüne aktarılır. Nesnenin içerdiği özellikler ve metotlar, klavyede yer alan ctrl+boşluk tuşları ile ekrana getirilmeye devam edilir. Bu özellik kullanılarak, nesne ve özellikler kolayca belirlenir. Elle teker teker yazılmasına gerek kalmaz.

**NNRREPORT Nesnesi**
İlişkisel serbest raporda, açılan her bir raporun (ana görüntü ve ilişkili tüm görüntüler için açılan raporlar), rapor gridi (ızgara), grid içindeki satırlar, satırlardaki hücreler ve hücrelerin değerlerini barındıran nesnedir. NNRReport.ActiveGrid nesnesi, üzerinde bulunulan gridin özelliklerini, NNRReport.ActiveGrid.ActiveRow nesnesi ise, üzerinde bulunulan satırın özelliklerini kapsar.

**Query Nesnesi**
Seçilen olay anında rapora bir SQL cümlesi yazılarak, sonuç döndüren kod parçacığı hazırlamak için kullanılır. Query. SQL özelliği kullanılarak farklı bir SQL cümleciği çalıştırılabilir. Dönen sonuç, raporun bir hücresine ya da başka bir bölümüne aktarılabilir.

SQL cümlecikleri, seçilen olay her gerçekleştiğinde çalışır.

Örneğin; satır sonu için bir SQL cümlesi yazılmışsa, her satırda çalışır. Bu işlem raporun performansını büyük ölçüde düşürür.

**Geçerli Nesnelerin Özellikleri ve Metotları Kullanımı**

Scripting bölümünde kullanıma sunulan nesnelerin içerdiği özelliklerin ve metotların ne şekilde kullanılması gerektiği "Nesne Tarayıcısı" yardımı ile izlenir.

**Nesne Tarayıcısı**
Scripting bölümünün araç çubuğunda yer alan "Nesne Tarayıcısı" butonu yardımı ile, kullanıma açık nesnelerle ilgili bilgi alınması sağlanır.

Nesne Tarayıcısı ekranı alanında yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| Nesne Tarayıcısı Ekranı |  |
| --- | --- |
| Kullanılan Kütüphaneler | Ortamda kullanımına izin verilen nesneler, farklı kütüphanelerden gelir. Programın hazırladığı nesne kütüphaneleri, kurulum sırasında ...\\NETTLB adlı klasöre aktarılır ve işletim sistemine register edilir. Sadece bu şekilde yüklenen ve register edien kütüphanelerin nesneleri kullanılabilir. İlk olarak, bilgi alınması istenen nesne kütüphaneden seçilir.<br>Örneğin;"İlişkisel Serbest Rapor" için Scripting ortamında iki tane nesne mevcuttur. Bu iki nesne iki farklı kütüphaneden gelir. NNRReport nesnesi NNRRPT.TLB isimli kütüphaneden, Query nesnesi ise NETSISVCL_3_0.TLB kütüphanesinden gelir.<br>Ortamda kullanıma açılan başka nesneler olsaydı, "Kütüphane Listesi" bölümünde, nesnelerin içinde bulunduğu kütüphaneler de izlenebilirdi. |
| Kayıtlı Sınıflar | Nesne tabanlı yapıda, nesneler (object) sınıflardan (class) türetilir. Yani sınıflar, nesnenin tanımıdır. Nesne ise, ilgili tanımın kullanımıdır. Seçilen kütüphanenin içerdiği ve ortamda kullanıma açık nesnelerin türedikleri sınıflar, ekranın "Kayıtlı Sınıflar" bölümünde listelenir. **Örnek 1** NNRReport nesnesi, INNRReport sınıfından türer. INNRReport sınıfı seçilerek, NNRReport nesnesinin sınıfında tanımlı özellikler ve metotlar izlenebilir. **Örnek 2** NNRReport nesnesinin içerdiği, ActiveGrid (üzerinde bulunulan grid) nesnesi, IGrid sınıfından türer. ActiveGrid ile kullanılacak, sınıfında tanımlı özellik ve metotlara, IGrid sınıfı seçilerek ulaşılabilir. **Örnek 3** NNRReport.ActiveGrid nesnesinin içerdiği, ActiveRow (üzerinde bulunulan satır) nesnesi IGridRow sınıfından türer. ActiveRow ile kullanılacak, sınıfında tanımlı özellik ve metotlara, IGridRow sınıfı seçilerek ulaşılabilir. |
| Sınıf Üyeleri | Kullanılan kütüphane ve özellikleri izlenecek sınıf seçildiğinde, sınıfın içerdiği tüm özellik ve metotlar, "..... Sınıfı Üyeleri" başlıklı, sağ üst bölümdeki pencereden izlenir. Dokümanda geçerli nesnelerin tüm özellik (property) ve metotları (procedure, function) hakkında detaylı bilgi verilmez. Özellik ve metotlar, İngilizce isimlendirilir. İsimleri ve işlevleri hakkında bilgi verilmez. |
| Parametreler | Kullanılan kütüphane ve özellikleri izlenecek sınıfın herhangi bir özellik ya da metodu işaretlenerek seçildiğinde, sağ alt pencerede, özellik ya da metot kullanıldığında dönen ve istenen parametreler izlenir. |
| Dönüş Parametresi | Seçilen sınıf üyesi kullanıldığında, ne tip bilgi döneceğini belirtir. **Örnek 1** IGridRow sınıfının Index özelliği, isminden de anlaşılacağı gibi üzerinde bulunulan satır numarası bilgisini, dönüş parametresi olarak Long (tamsayı) cinsinden döndürür. **Örnek 2** IntXQuery (Query nesnesinin türediği sınıf) sınıfının, Open metodu, isminden de anlaşılacağı gibi yazılan SQL cümlesinin çalıştırılması sonucu oluşacak sonuç kümesinin açılmasını sağlar ve dönüş parametresi Void, yani yoktur. İşlemi yapar ve herhangi bir sonuç döndürmez. |
| Yardım | "Parametreler" penceresinde bulunan bu bölümde ise, seçilen sınıf üyesi kullanılırken temin edilmesi gereken değişkenler izlenir. Örneğin; IGridRow sınıfının ColByName özelliği, isminden de anlaşılacağı gibi, satırdaki belli bir kolonun (hücrenin) içeriğini döndürür. Ancak kullanımda hangi hücrenin bilgisinin döndürüleceği, parametre olarak kolon ismi gönderilmesi şartıyla belirtilmesi gerekir. Bu özellik kullanıldığında, nesneden programa dönecek olan içerik, "Dönüş Parametresi" kısmında Variant (değişken) tipli olarak izlenebilir. Bunun sebebi, kolon içeriğinin ne tip bilgi içerdiğinin bilinmemesi ve herhangi bir tipe sahip olmasından kaynaklanır. Yardım kısmında ise, kullanım sırasında temin edilmesi gereken parametre (ColName - kolon ismi) bilgileri izlenebilir. |
| Parametre Adı | Sınıf üyesi kullanılırken gönderilmesi gereken parametrenin adıdır. |
| Tipi | Sınıf üyesi kullanılırken gönderilmesi gereken parametrenin veri tipidir. |
| Varsayılan | Sınıf üyesi kullanılırken gönderilecek parametrenin, nesne tanımında varsayılan değeri olup olmadığı belirlenir. |
| Seçmeli | Sınıf üyesi kullanılırken gönderilecek parametrenin, gönderiminin seçmeli olup olmadığı belirlenir. |

**Script Örnekleri**

**Örnek 1**

Stok hareketlerini gösteren raporda, "Miktar" isimli, hesaplanan bir kolon tanımlandığı ve bu kolonda giriş hareketleri için stok hareketindeki miktarı olduğu gibi, çıkış hareketleri için de miktarın eksi değeriyle gösterilmesi istendiğinde aşağıdaki durum gerçekleşir:

Seçilen Görüntü: STHAR

Seçilen Olay: OnRowEnd

Kod : if NNRREPORT.ActiveGrid.ActiveRow.ColByName("STHAR_GCKOD")="C" then NNRREPORT.ActiveGrid.ActiveRow.ColByName("CALC1")= -1\*NNRREPORT.ActiveGrid.ActiveRow.ColByName("STHAR_GCMIK") else NNRREPORT.ActiveGrid.ActiveRow.ColByName("CALC1")=NNRREPORT.ActiveGrid.ActiveRow.ColByName("STHAR_GCMIK") end if

Kodun anlamı: İlişkisel Serbest Raporun aktif gridindeki aktif satırın, STHAR_GCKOD (stok hareketinin giriş/çıkış olduğunu belirleyen sahası olup G/C değerlerini alır) isimli sahası değeri "C" ise, İlişkisel Serbest Raporun aktif gridindeki aktif satırın, CALC1 (Miktar için tanımlanmış, hesaplanan sahanın program tarafından atanan ismi) isimli sahasının değerini, İlişkisel Serbest Raporun aktif gridindeki aktif satırın, STHAR_GCMIK (stok hareketinin miktarının saklandığı saha) isimli sahasının değerini -1 ile çarparak oluştur.
STHAR_GCKOD sahası değeri "C" değilse ki "C" dışında sadece "G" olabilir. STHAR_GCMIK sahasının değerini olduğu gibi, CALC1 isimli sahaya aktar.

Not : Raporda görüntülenmek istenen sahalar tanımlanırken, STHAR görüntüsünden STHAR_GCKOD ve STHAR_GCMIK isimli sahalar seçilmeli, ancak sadece hesaplamada kullanılacakları için Gizli olarak işaretlenmelidir.

**Örnek 2**

Birinci örnekteki "Miktar" sahası dışında, yürüyen bakiye sahası tanımlanması istendiği zaman, bu saha her satırda kalan stok bakiyesini gösterir. Gridin ilk satırında, miktar olduğu gibi yazılır ve takip eden satırlarda ise toplanarak ilerletilir.

Bakiye isimli hesaplanan saha tanımlandığında aşağıdaki işlem gerçekleşir:

Seçilen Görüntü: STHAR

Seçilen Olay: OnRowEnd

Kod: NNRREPORT.ActiveGrid.ActiveRow.ColByName("CALC2")=NNRREPORT.ActiveGrid.ActiveRow.ColByName("CALC1") if NNRREPORT.ActiveGrid.ActiveRow.Index\>0 then NNRREPORT.ActiveGrid.ActiveRow.ColByName("CALC2")= CDbl(NNRREPORT.ActiveGrid.ActiveRow.ColByName("CALC2"))+ CDbl(NNRREPORT.ActiveGrid.Cell(5,NNRReport.ActiveGrid.ActiveRow.Index-1)) end if

Kodun Anlamı : İlişkisel Serbest Raporun aktif gridindeki aktif satırın, CALC2 (Bakiye için tanımlanmış hesaplanan sahanın program tarafından atanan ismi) isimli sahasına, birinci örnekte tanımı verilen CALC1 sahasının değerini olduğu gibi taşı. Eğer, İlişkisel Serbest Raporun aktif gridindeki aktif satırın, satır numarası sıfırdan büyük ise, yani raporda yer alan ilk satır değilde sonraki satırlar için, CALC2 sahası değerine, bir önceki satırda yer alan CALC2 sahasının değerini ekle.

Not: Cell (hücre) özelliği, gridin herhangi bir hücresindeki değeri döndürür. Cell özelliği, parametre olarak kolon numarası ve satır numarası bilgilerini alır. Kolon numarası, CALC2 sahasının grid üzerinde bulunduğu kolonun sıfır tabanlı numarasıdır. Satır numarası ise, aktif satırın numarası (index) -1, yani aktif satırdan önceki satırdır.
CDbl, ColByName ya da Cell özelliklerinden dönen variant (değişken) tipli bilgiyi, double (nümerik) olarak ifade etmek için kullanılır. Bu tip çevrim yapılmazsa, dönen değer metin olarak düşünülüp, toplama işlemi olarak iki metin yan yana birbirine eklenir.

**Araç Çubuğu ve Diğer Yardımcı Butonlar**

Araç Çubuğu ve Diğer Yardımcı Butonlar ve açıklamaları aşağıdaki şekildedir:

| Buton İsmi | Açıklama |
| --- | --- |
| Pencere Kapat/Aç | Pencerelerin etrafında yer alan bu butonlar ile, ilgili pencere kapatılarak, görüntüde diğer pencerelere daha çok yer açılması sağlanır. Aynı buton yardımıyla pencere geriye açılabilir. |
| Nesne Tarayıcısı | Scripting bölümünün araç çubuğunda yer alan "Nesne Tarayıcısı" butonu yardımı ile, kullanıma açık nesnelerle ilgili bilgi alınması sağlanır. |
| Kod Tamamla | Kullanılmıyor. |
| Kod İçeriği | Script editör ortamındaki ctrl+boşluk tuşları (klavyede yer alan) ile aynı işlevi yapar. |
| Satıra Git | Uzun kodlar içinde istene bir satıra hızlı gidiş sağlar. Açılacak pencerede satır numarası verildiğinde hızlı gidiş sağlanır. |
| Bul, Sonrakini Ara, Öncekini Ara, Değiştir | Kod içinde istenen metni arama, bulunduktan sonra, sonrakini/öncekini arama, bulunan metni istenen başka bir metinle değiştirme işlemlerini yapar. Arama, büyük-küçük harf duyarlı, verilen metin kelime olarak imleçten itibaren ve sadece seçili metin içerisinde, imleçten ileriye ve geriye olmak üzere yönlendirilerek yapılır. Değiştirme işleminde de, aynı şekilde aranarak bulunan metin parçacığı değiştirilebilir. Arama ve değiştirme işlemi, bir defa yapıldıktan sonra, sonrakini/öncekini ara butonları ile tüm kod geneli devam ettirilir. |
| ![](../../../_assets/3d436647c2cd6ab8842d.png) Geri | Scripting bölümü tamamlandıktan sonra bir önceki sekmeye geçilmesini sağlayan butondur. |
| ![](../../../_assets/ccd70a9b860d515ff68c.png) İleri | Scripting bölümü tamamlandıktan sonra bir sonraki sekmeye geçilmesini sağlayan butondur. |

**Üst Bilgi/Alt Bilgi Düzenleme**

Üst Bilgi ve Alt Bilgi, rapor sonunda veya kırılımlarda, sütunlardaki değerlerin toplamını ve ortalamasını aldırmak için kullanılır.

| İlişkisel Serbest Rapor Sihirbazı Ekranı |  |
| --- | --- |
| Seçili Görüntü | Önceki sekmelerde seçilen, ilişkilendirilen ve bağlantıları belirlenen görüntülerin yer aldığı penceredir. Görüntülerin içinden, üst/alt bilgisi tanımlanacak olan görüntü, farenin sol tuşu ile tıklanarak seçilir. |
| Tanımlı Sahalar | Seçilen görüntü için, "Raporda Gösterilecek Alanlar" bölümünde tanımlanan kolon bilgileri, sağ alt bölümdeki pencerede listelenir. Ancak, önceden eklenen bu sahalar için alt/üst bilgi tanımlanabilir. Başka bir saha için tanımlama yapılması istendiği zaman, ilgili sahanın da "Raporda Gösterilecek Alanlar" bölümünden eklenmesi gerekir. Üst/Alt bilgisi tanımlanacak olan saha, "Tanımlı Sahalar" penceresindeki listeden farenin sol tuşu çift tıklanarak seçilir. |

**Alt Bilgi Kullanımı**

Rapor alınması sırasında, açılan her rapor gridinin alt kısmında, belli bir sahanın gridde dökülen tüm değerlerinin toplamının veya ortalamasının alınması için kullanılır.

Örneğin; STSABIT görüntüsü ana görüntü olmak üzere, STOKCARIANALIZ görüntüsü bağlandığında ve alt görüntüdeki Tarih, Net Fiyat, Giriş Miktar ve Tutarı, Çıkış Miktar ve Tutarı sahaları rapora eklendiğinde, Giriş Tutarı ve Çıkış Tutarı sahaları alt bilgisinde sahaların toplamının alınması için rapor dökümü sırasında, her bir stok kartına açılan stokcarianaliz kayıtları gridinin alt kısmında, "Giriş Tutarı" ve "Çıkış Tutarı" sahalarının toplamı izlenebilir.

**Üst Bilgi Kullanımı**

Rapor alındıktan sonra gruplama/kırılım işlemi yapıldığında, kırılımda, istenen bir sahanın içerdiği değerlerin toplamının veya ortalamasının alınması için kullanılır.

Örneğin; STSABIT görüntüsü ana görüntü olmak üzere, STOKCARIANALIZ görüntüsü bağlandığında ve alt görüntüdeki Tarih, Net Fiyat, Çıkış Miktar ve Tutarı sahaları rapora eklendiğinde, Çıkış Tutarı sahası alt bilgisinde sahaların toplamı alınır. Bu toplam ilgili stoka ait dökülen tüm çıkış tutarlarının toplamını verir. "Tarih" sahası için bu kez, üst bilgide ve çıkış tutarı toplamı aldırılır. Bunun anlamı, rapor alındıktan sonra tarih gruplama/kırılımı yapılırsa, her bir tarih için "Çıkış Tutarı" toplamı izlenebilir.

**Tanımlamalar**

İlişkisel Rapor ekranı Tanımlama alanları ve içerdiği bilgiler aşağıdaki şekildedir:

| Tanımlama Alanları |  |
| --- | --- |
| Kolon Adı | Seçilen sahanın, "Raporda Gösterilecek Alanlar" bölümünde tanımlanan kolon adıdır. Bilgi amaçlı gösterilmektedir. |
| İşlem Sahası | Üst/Alt bilgide hesaplamaya tabi tutulacak alan bilgisidir. Üst bilgi örneğinde belirtildiği gibi; toplam ve ortalama işlemi yapılacak olan saha, işaretli bilgi sahasından farklı olabilir (Tarih sahasında, çıkış tutarı toplamlarının alınması gibi). |
| Ön Biçim | Kullanılmıyor. |
| Biçim | Nümerik alanlar için üst/alt bilgi görüntü biçiminin belirlendiği sahadır. |
| Tip | Üst/alt bilgide yer alacak işlem tipidir. Toplam; işlem sahasında belirtilen sahanın, gridde dökülen tüm değerlerinin alt ya da kırılım toplamlarını verir. Ortalama, işlem sahasında belirtilen sahanın, gridde dökülen tüm değerlerinin toplam ya da kırılım ortalamasını verir. Sayı; işlem sahasında belirtilen sahanın, gridde dökülen kayıt sayısını altta ya da kırılımda verir. En düşük/En yüksek; işlem sahasında belirtilen sahanın gridde dökülen değerlerinin en düşüğünü/en yükseğini, altta ya da kırılımda gösterir. |
| Yeri | Alt bilgide/üst bilgide olmak üzere, işlemin yerini belirlemek için kullanılır. **Örnek 1** Çıkış tutarı alt toplamı için, sağ alt penceredeki tanımlı sahalardan "Çıkış Tutarı" alanı seçilir. İşlem sahası olarak yine "Çıkış Tutarı" sahası seçilerek, "Tip" alanının Toplam, "Yeri" alanın da Alt Bilgi olarak seçilmesi gerekir. **Örnek 2** Tarih kırılımında, çıkış tutarları toplamı alınması için, sağ alt penceredeki tanımlı sahalardan, "Tarih" sahasının seçilmesi ve "İşlem Sahası" olarak "Çıkış Tutarı" sahası seçilerek, "Tip" alanının Toplam, "Yeri" alanın da Üst Bilgi olarak seçilmesi gerekir. |

**Baskı Ayarları**

Rapor ekrana alındıktan sonra yazıcıya gönderilir. Yazıcıdan çıktı alınırken, baskı ön ayarlarının yapılması gerekir. "Baskı Ayarları" sekmesi, "İlişkisel Serbest Rapor" sihirbazının son sekmesi olup, tanımlamalar bu sekmeden sonra biter. Rapor ekrana alındıktan sonra, yazıcıya gönderilmeden önce bazı baskı ayarları yapılabilir.

Baskı Ayarları sekmesi alanları ve içerdiği bilgiler aşağıdaki şekildedir:

| İlişkisel Serbest Rapor Sihirbazı Ekranı |  |
| --- | --- |
| Yönlendirme | Raporun sayfa üzerinde basılacağı şeklin belirlendiği alandır. Yatay/dikey seçenekleri arasından seçim yapılır. |
| Her Sayfada Şirket Adı | Raporun her sayfasında şirket adının basılması için kullanılır. |
| Her Sayfada Başlık | Rapor başlığının (İlişkilendirilecek Görüntülerin Seçimi" sekmesinde yer alan "Rapor Adı" seçeneğinde belirlenen), raporun her sayfasında basılması için kullanılır. |
| Her Sayfada Tarih/Saat | Raporun her sayfasında tarih ve saat bilgisinin basılması için kullanılır. |
| Sayfa No/Toplam Sayfa | Raporun her sayfasında sayfa numarası ve toplam sayfa bilgisinin basılması için kullanılır. |
| Yatayda/Düşeyde Hizalama | Raporun, yatayda/düşeyde sayfanın ortasına basılması için kullanılır. |
| Ölçekleme, Ayarla | Raporun sayfaya sığdırılması için, tüm karakterlerin verilen ölçekte küçültülmesi/büyütülmesi için kullanılır. |
| Ölçekleme, Sığdır | Raporun sayfaya tam sığacağı şekilde, karakterlerin büyütme/küçültme oranlarının otomatik ayarlanması için kullanılır. |
| Sıfırlar Basılsın | Raporda, değerleri sıfır olan hücrelerin basılması ya da boş bırakılması için kullanılır. |
| Nüsha Sayısı | Raporun birden fazla kopyalanarak basılması için kullanılır. |
| Firma Logosu, Basım Yeri | Raporda firma logosu basım yeri belirlemek içindir. Üst Bilgi/Alt Bilgi ya da her ikisinde de, sol köşe, sağ köşe, her iki köşe gibi bölümlerinde basılmasını sağlar. |
| Firma Logosu Referans Ekle | Firma logosu olarak basılması istenen resmin eklenmesi içindir. Seçenek işaretlendiğinde aktif hale gelen "Ekleme" butonu yardımı ile, açılan pencereden logonun bulunduğu klasöre geçilip resim dosyası seçilerek eklenebilir. Eklenen resim dosyası, "Silme" butonu yardımı ile silinir. |
| Geri | Önceki sekmeye dönülmesi için kullanılan butondur. |
| Çalıştır | Tanımlanan raporun çalıştırılması için kullanılan butondur. Yapılan tanımlamalar, bu butonla saklanmaz. Sadece rapor alındıktan sonra saklanabilir. |
| Kaydet ve Çık | Yapılan tanımlamaların saklanarak, sihirbazın rapor çalıştırılmadan kapatılmasını sağlar. |
| İptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |

**İlişkisel Serbest Rapor İçeriği:** İlişkisel Serbest Rapor sihirbazında tanımlamalar yapıldıktan sonra "Çalıştı" butonu ile raporun ekrana gelmesi sağlanır.

**Bilgi Çubuğu:** Raporun tamamının ekrana getirilmesi, içerdiği kayıt sayısı doğrultusunda biraz zaman alabilir. Geçen sürede, rapor penceresinin alt bilgi çubuğunda, getirilen kayıt sayısı ve süre bilgisi görünür. Tüm kayıtlar bittiğinde, yine alt bilgi çubuğunda "Rapor Hatasız Tamamlandı" bilgisi ekrana gelir.

**Grid (Izgara) Kullanımı:** Raporun ilk aşamada görünen tek gridi ve ana görüntü kayıtlarını içeren griddir.

**Grid Sütunları:** Her görüntü için, "Raporda Gösterilecek Alanlar" bölümünde belirlenen sahalar, gridin sütununu oluşturur.

Örneğin; ana görüntü olarak STGRUP görüntüsü belirlenen bir raporda, GRUP_KOD ve GRUP_ISIM sahaları, raporda görüntülenmesi için eklenmişse, ana grid "Grup Kodu" ve "Grup İsmi" olmak üzere iki sütundan oluşur.

**Grid Satırları:** Grid içindeki satırlar, ilgili görüntünün "Filtreleme" bölümündeki kriterler ile, kısıtlanmış sonuç kümesine düşen kayıtlardır.

**İlişkili Gridlerin Açılması/Kapanması**

Grid satırının sol tarafında artı ![(plus)](../../../_assets/8bc1079dc378a6219e99.svg) işareti bulunan satırların, ilişkilendirilmiş alt görüntüden gelen kayıtları mevcuttur. Bu butona tıklandığında, ilişkili kayıtlara ait grid açılır.

Örneğin; STGRUP ana görüntüsüne bağlı STSABIT alt görüntüsü mevcut ise, grupları listeleyen ana gridin sol tarafında ![(plus)](../../../_assets/8bc1079dc378a6219e99.svg) işareti bulunan satırlarından biri bu buton ile tıklandığında, grubun içerdiği stok kayıtları izlenebilir.

İlişkiden dolayı, her grup kaydının altında açılan gridde, kendi grubunun içerdiği stoklar izlenebilir. Diğer bir grubun içerdiği stokları izlemek için, ilgili grup kaydının satırında grid açma işleminin tekrarlanması gerekir.
Alt gridi açılan kaydın sol tarafında eksi ![(minus)](../../../_assets/1b0d15e570bf80d3a5bb.svg) işareti görülür. Bu buton yardımı ile alt grid kapatılabilir.

Örneğin; Yukarıdaki örnekte STGRUP görüntüsüne STSABIT ve STSABIT görüntüsüne de STOKCARIANALIZ görüntüsünün eklendiği varsayıldığında; STSABIT alt görüntüsü için açılan her bir gridde, ilişkili STOKCARIANALIZ kayıtları için de alt gridler oluşur. Bu gridleri de aynı şekilde açıp kapatmak mümkündür.

**Raporun Performans Maliyeti**
Örnekte anlatıldığı gibi, her bir alt görüntü için raporda bir grid oluşturulur. Artı ![(plus)](../../../_assets/8bc1079dc378a6219e99.svg) işareti ile açılabilen her grid, bellekte belli bir yer kaplar. Grid sayısı arttıkça, rapor performansı etkilenebilir. Bu sebeple, doğru ilişki tanımları ve kayıt filtrelemeleri ile sonuç kümesi daraltması, optimum raporun elde edilmesini sağlar.

**Gridde Sıralama**

Griddeki bir kolonun başlığına farenin sol tuşu ile bir kez tıklandığında, griddeki tüm kayıtlar bu kolonun içerdiği bilgilere göre küçükten büyüğe sıralanır. Sıralanan kolon başlığında, "yukarı ok" şeklinde küçükten büyüğe sıralandığına dair bilgi ikonu görünür. Kolon başlığına tekrar farenin sol tuşu ile tıklandığında, bu kez grid kayıtları kolonun içerdiği bilgilere göre büyükten küçüğe sıralanır. Kolon başlığında, "aşağı ok" şeklinde büyükten küçüğe sıralandığına dair bilgi ikonu görünür. Kolon başlığına tekrar farenin sol tuşu ile tıklandığında ise, ilgili kolondaki sıralama kaldırılarak, ilk döküm sıralamasına geri döndürülür ve kolonun sıralandığına dair görünen bilgi ikonları yok olur.

**Gridde Arama**

Grid kolonu bilgilerinden ilk olanın üzerine fare ile gelinip, aranması istenen bilginin baş harfleri yazılarak, her bir harf yazıldığında oluşan, başlangıç değerine uyan ilk bilginin üzerine otomatik gelinir.

**Grid Kayıtlarının Filtrelenmesi-****Kayıtlar Listesinden Filtreleme**

Grid kolonunun sağ köşesinde yer alan "aşağı ok" işaretine farenin sol tuşu ile tıklandığında, kolonda yer alan bilgilerin tekrarsız listesi açılır. Bu listeden bir tanesi seçildiğinde, tüm gridde sadece ilgili kolonda seçilen değere eşit olan kayıtlar listelenip diğerleri kapatılır.

**Kişisel Filtreleme**
Listeden bir değer belirlenmesi dışında, yine listede yer alan (Kişisel) seçeneği ile, farklı filtreleme de yapılabilir. Kişisel filtrelemede, filtrelenecek kolon için operatör ve değer tanımlanabilir.

Örneğin; Stok ismi kolonunda, benzer operatörü ile "ORANGE%" değeri kullanıldığında, "ORANGE" ile başlayan stok isimlerine ait kayıtlar gridde görünür ve diğerleri kapatılır. Yine aynı tanım içinde, ikinci bir koşul tanımlayıp, ilk koşula ve/veya operatörü ile birleştirilmesi şartıyla ikili filtre tanımlanması da mümkündür.

Kişisel filtrelemede kullanılan değerler ve bilgileri aşağıdaki şekildedir:

| Kişisel Filtreleme |  |
| --- | --- |
| Benzer, Benzemez | Yazılan karakterleri içeren/içermeyen kayıtlar anlamına gelir. SQL standartlarında olduğu gibi % ve \_ maskeleme işaretlerinin kullanılması gerekir. |
| Eşittir, Eşit Değildir | Yazılan karakterlere tamamen eşit olan/eşit olmayan kayıtlar anlamına gelir. |
| Küçük, Eşit Küçük, Büyük, Eşit Büyük | Yazılan değerden küçük/eşit ve küçük/büyük/eşit ve büyük olan kayıtlar anlamına gelir. |
| Boşluktur, Boşluk Değildir | Değeri boş olan/boş olmayan kayıtlar anlamına gelir. İster listeden değer seçilerek, ister "kişisel" seçeneği ile filtreleme sonucu, grid kayıt kümesi daraltılarak sadece filtrelenen kayıtlar görünür diğerleri kapatılır. Gridin alt bölümünde ise, gridin filtrelenmiş olduğuna dair bilgi verilerek filtre koşulları gösterilir. |

Bilgi çubuğunda yer alan "Çarpı" butonu ile, filtreleme ve tanımlı koşullar kaldırılarak grid eski haline döndürülür. "Onay" butonu ile, filtre uygula/uygulama işlemi yapılır. Seçenek işaretli iken filtre uygulanarak grid kayıtları kısıtlanır. Seçenek işaretli değilken, filtre bilgisi ekranda kalır fakat grid tüm kayıtları listeler. Bilgi çubuğunda seçeneğin işaretlenerek filtrelenmiş hale dönülmesi mümkündür.

**Filtreleyici**
"Customize" butonu ile açılan pencerede daha ileri filtre tanımları yapmak mümkündür.

Filtreleyici penceresinde, koşulun yanında bulunan kutucuklara tıklandığında, yapılabilen işlemler şöyledir:

| Filtreleyici Penceresi |  |
| --- | --- |
| Durum Ekle | Mevcut koşula yeni bir koşul eklemeye yarar. |
| Grup Ekle | Mevcut koşula parantez içinde koşul grubu eklemeye yarar. |
| Satırı Sil | Yanlış tanımlanan koşul satırını silmeye yarar. |
| Bağlantı | Bir grup içinde yer alan koşulların birbirlerine bağlantı şeklini belirlemeye yarar. "Ve/Veya", "Ve Değil/Veya Değil" şeklinde bağlantı şekilleri vardır. |
| Saha İsmi | Koşul satırının ilk bölümünde saha ismi belirlenir. Yeşil renkle gösterilen saha ismi üzerinde farenin sol tuşu ile tıklandığında, gridin aktif saha isimleri listelenir ve içinden seçim yapılabilir. |
| Operatör | Koşul satırının orta bölümde, operatör belirlenir. Bordro renkle gösterilen operatör üzerine farenin sol tuşu ile tıklandığında, kullanılacak operatörler listelenir ve içlerinden seçim yapılabilir. |
| Değer | Koşulun sağlanması için istenen değer yazılır. "Uygula" butonu ile, koşulun gridde uygulanması sağlanır. |

![](../../../_assets/fbbe2f81e2f67f20dae2.png)

Şekilde tanımlanan filtre uygulandığında, oluşan koşul aşağıdaki şekildedir:

![](../../../_assets/544c09fb10aafd20f19a.png)

**Gridde Gruplama/Kırılım**

![](../../../_assets/195d84141f98ef88f49a.png)

Gridlerin üzerinde, herhangi bir kolon başlığı, "sürükle bırak" yöntemiyle grid üzerindeki boşluğa taşındığında, bu kolondaki bilgilere göre grid gruplanır. Gridde, bir stoka ait belli tarih aralığındaki hareket kayıtları, STOKCARIANALIZ görüntüsünden getirilerek görülür. Aynı tarihe (güne) ait birden fazla hareket vardır. Tarih kolonu, "sürükle bırak" yöntemi ile grid üzerindeki boşluğa bırakıldığında, kayıtlar tarih bazında gruplanır. Her bir tarih için sol tarafta bulunan artı ![(plus)](../../../_assets/8bc1079dc378a6219e99.svg) işareti ile, ilgili tarihe ait kayıtlar açılır.
Bu görüntü için "Tarih" alanında, çıkış tutarları toplamları üst bilgisi tanımlanarak kırılımda toplam gösterilir. Saha için herhangi bir üst bilgi tanımlanmadığı zaman, satırlardaki tarihlerin yanında toplam bilgisi görünmez.

**Araç Çubuğu ve Farenin Sağ Tuşu**

Rapor araç çubuğunda ve grid üzerinde farenin sağ tuşu ile ekrana gelen menü seçenekleri aşağıdaki şekildedir:

**Export All To XLS:** Raporun tüm içeriğinin Excel dosyasına aktarılmasını sağlar. Buton kullanıldığında açılan pencerede, Excel dosya klasör ve isminin belirtilmesi gerekir.

**Export All To Text:** Raporun tüm içeriğinin bir Text dosyasına aktarılmasını sağlar. Buton kullanıldığında açılan pencerede Text dosya klasör ve isminin belirtilmesi gerekir.

**Export Selected/All To XML:** Raporun seçili/tüm içeriğinin bir XML dosyasına aktarılmasını sağlar. Buton kullanıldığında açılan pencerede XML dosya klasör ve isminin belirtilmesi gerekir. Oluşan XML dosya, raporun sınıflamasında yer alır.

**Export Selected/All To XML:** Raporun seçili/tüm içeriğinin bir HTML dosyasına aktarılmasını sağlar. Buton kullanıldığında açılan pencerede HTML dosya klasör ve isminin belirtilmesi gerekir. Oluşan dosya ile rapor, tarayıcı tarafından izlenebilir.

**Print Preview, Print:** Raporun baskı ön izlemesini ve yazıcıdan çıktısının alınmasını sağlar.

**Tümünü Aç/Kapa:** Rapordaki tüm alt gridlerin tek hareketle açılmasını/kapatılmasını sağlar.

**Sihirbaz:** Rapor sihirbazına dönerek, tanımlamaların düzenlenmesini ve tekrar aynı raporun alınmasını sağlar.

**Rapor Kapatılması ve Saklama**

Rapor üzerindeki çalışma tamamlandıktan sonra, rapor penceresi bilinen yöntemlerle (klavyede yer alan Esc tuşu ya da ekranın sağ üst köşesinde yer alan X tuşu ile) kapatılır. Rapor kapatma sırasında, "Rapor Kaydedilsin mi?" şeklinde ekrana gelen onay sorusundan sonra, isteğe bağlı bir isim verilir ya da mevcut bir rapor üzerine kaydedilir.
