---
title: "İthalat Dosya İşlemleri"
page_id: "50679531"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Dış Ticaret"
  - "İşlemler / Dış Ticaret"
  - "İthalat İşlemleri"
  - "İthalat Dosya İşlemleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Dış Ticaret / İşlemler / Dış Ticaret / İthalat İşlemleri / İthalat Dosya İşlemleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTg4NTY2NjM0LWRlODQtNGNhMS04NGIzLWM0Y2M5NjUwN2M2YiZsaW5rPTA4NzM0MTM0LTQwMzQtNGQwZS1hNjFiLTMzZTNmNjY3N2ZlOSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=88566634-de84-4ca1-84b3-c4cc96507c6b&link=08734134-4034-4d0e-a61b-33e3f6677fe9&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ithalat-dosya-islemleri_50679600_50679531.html"
source_version: "2022-11-02T12:57:14.493+03:00"
source_bytes: 49627
fetched_at: "2026-09-13T04:05:51+00:00"
generator: "netsis-scraper 1.0.0"
---
# İthalat Dosya İşlemleri

İthalat Dosya İşlemleri, Lojistik/Satış Bölümü'nde İşlemler/Dış Ticaret Modülü menüsünün altında yer alır. İthalat işlemlerinde kullanılacak belgenin oluşturulacağı bölümdür.

İthalat Dosya İşlemleri bölümü; Genel, Satınalma Teklif, Satıcı Siparişleri, Dosya Siparişleri, Faturalarım, İthalat Ödeme Bilgileri, Nakliye, Nakliye Detayları ve Konşimento Bilgileri, Gümrük Beyanname Bilgileri, Debit/Credit Note Bilgileri, Masraflar sekmesinden oluşur.

**Genel**

İthalat Dosya İşlemleri ekranı Genel sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| İthalat Dosya İşlemleri Ekranı |  |
| --- | --- |
| İthalat Dosya No | Tüm ithalat işlemleri birer dosya numarası altında gruplanarak takip edilir. Her ithalat işlemi için bir dosya numarası verilir. Bir dosya numarasının altında birden fazla<br>fatura kaydı yapılabilir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, daha önce kaydedilen dosya numaralarına ulaşılır. Artı ![(plus)](../../../../../_assets/8bc1079dc378a6219e99.svg) butonuna tıklandığında; Dosya Numarası alanına, yeni bir dosya numarası getirilir. Dosya Numarası, Dış Ticaret Parametreleri → İthalat Parametreleri → Dosya No-Prefix değerine göre artırılarak getirilir. |
| Dosya No | Yeni oluşturulacak ya da daha önceden kaydedilen ithalat işlemine ait dosya numarasının girildiği alandır. |
| ![](../../../../../_assets/60b46c97470edcf767e5.png) İthalat Dosyasını Kapat | İthalat Kapatma İşlemi ekranına bağlanarak ilgili ithalat dosyasının kapatılması için kullanılır. |
| Cari Kodu | İthalat işleminin yapılacağı tedarikçinin, Cari → Kayıt → Cari Hesap Kayıtları bölümünde tanımlanan kodunun girildiği alandır. |
| Teslim Cari | İthalat işleminin yapılacağı cari hesap ile, stokların fiilen teslim edileceği cari adresin farklı olması durumunda, stokların teslim edileceği cari kodun girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, cari kodlar arasından seçim yapılır. |
| Tarih | Kaydedilen ithalat dosyası tarihinin girildiği alandır. |
| Teslim Şekli | İthalata ilişkin teslimat şeklinin girildiği alandır. Teslim şeklinin belirlenmesi halinde Satın Alma Teklif, Satıcı Siparişleri, Kontrat Bilgilerim ve Faturalarım sekmelerinde, sadece burada girilen teslimat şekli ile kaydedilmiş bilgiler listelenir. Boş bırakılması halinde ise, dosya ile ilişkilendirilecek belgelerde teslim şekli kontrol edilmez. Alanın sağ tarafında yer alan aşağı ok butonu ile teslim şekilleri arasından seçim yapılır. |
| Açıklama | Dosya kaydı hakkında açıklama bilgisinin girildiği alandır. |
| Parçalı İthalat | Tanımlanan ithalat dosya işleminin parçalı ithalat olması durumunda seçilmesi gereken seçenektir. |
| Toplam Fatura Detayları Gösterilsin | Grid ekranda toplam fatura detaylarının gösterilmesi için kullanılan seçenektir. |

**Satınalma Teklif**

İthalat Dosya İşlemleri ekranı Satınalma Teklif sekmesi, Genel sekmesinde girilen Cari Kod'a ait satınalma teklif belgelerinin seçilerek, satıcı siparişi oluşturulmasını sağlayan sekmedir. Ekrana ilk olarak "Kısıt" penceresi gelir. Ekrandaki alanlar üzerinden kısıt verilerek, tekliflerin girilen kısıtlara göre listelenmesi sağlanır.

Satınalma Teklif sekmesi, Dış Ticaret Parametreleri → "İthalat Uygulaması Tekliften Başlasın" parametresinin işaretlenmesi ile ekrana gelir.

Ekranda sıralanan tekliflerden, sipariş oluşturulması istenenler için, satır başındaki kutucuğun işaretlenmesi gerekir. Satınalma teklifinin içindeki kalem bilgileri artı “+” tuşuna tıklanarak görüntülenir.
Belge Numarası'nın üzerine tıklandığında ise, satınalma teklif ekranı açılır ve teklif üzerinde izleme, düzeltme ya da iptal yapılabilir. Ekranın alt kısmındaki "Sipariş Numarası" alanına, oluşturulacak satıcı siparişinin numarası yazılıp "Sipariş Oluştur" butonuna tıklandığında, satınalma teklifinin sipariş haline getirilmesi işlemi gerçekleşir.

**Satıcı Siparişleri**

İthalat Dosya İşlemleri ekranı Satıcı Siparişleri sekmesi, satınalma teklifinden oluşturulan satıcı siparişleri arasından, sevk belgesinin (Kontrat) oluşturulduğu sekmedir. Ekrana ilk olarak "Kısıt" penceresi gelir. Ekrandaki alanlar üzerinden kısıt verilerek, siparişlerin girilen kısıtlara göre listelenmesi sağlanır. Kontrat oluşturulduğunda, stok hareketlerine ve cari hareketlerine herhangi bir kayıt atılmaz.
Ekranda sıralanan siparişlerden, kontrat oluşturulması istenenler için, satır başındaki kutucuğun işaretlenmesi gerekir. Satıcı siparişi içindeki kalem bilgileri “+” tuşuna tıklanarak görüntülenir. Belge Numarası'nın üzerine tıklandığında ise, satıcı siparişi ekranı açılır ve sipariş üzerinde izleme, düzeltme ya da iptal yapılabilir. Kontratı oluşturulacak sipariş kalemleri seçildikten sonra, sipariş miktarının ne kadarının kontrata taşınacağı "Kalan Miktar" alanından belirlenir. "Kalan Miktar" alanında değişiklik yapılmazsa, sipariş miktarının tamamı için kontrat oluşturulur. Sipariş kalemlerinde yer alan "Toplam Sevk Miktarı" kolonunda, sevk belgesi (Kontratı) oluşmuş miktar değil, fiilen sevk edilmiş - ithalat faturası oluşmuş - miktar gösterilir.

**Dosya Siparişleri**

Satıcı siparişlerinden oluşturulan kontrat bilgilerinin görüntülendiği sekmedir. Bu sekmede, henüz ithalat faturası oluşmamış kontratlar listelenir.

İthalat Dosya İşlemleri ekranı Dosya Siparişleri sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| İthalat Dosya İşlemleri Ekranı |  |
| --- | --- |
| Seçili Kalemler İçin İthalat Faturası Oluştur![](../../../../../_assets/ac9e3cb591de074ac521.png) | Seçilen kalemler için kontrat bilgilerinin iptal edilmesi için kullanılan butondur. Satıcı Siparişleri sekmesinden, ilgili kalemler için yeniden kontrat oluşturulabilir. |
| Seçili Kalemleri Sil ![](../../../../../_assets/f63de215c7060a2fcb1e.png) | Grid üzerinde listelenen kalemlerin çift tıklanarak seçildikten sonra silinmesi için kullanılan butondur. |
| Ek Maliyetler ![](../../../../../_assets/474d425daaff0648b6e1.png) | İlgili kalem için ek maliyet girişinin yapılmasını sağlayan butondur. Butona tıklandığında "Ek Maliyet" ekranı görüntülenir. |
| Basım ![](../../../../../_assets/177aec8184221dc858e8.png) | Dizayn tipi "Alış Faturası" olan dizaynlar ile kontrat basımının yapılması için kullanılan butondur. |
| İptal ![](../../../../../_assets/9b138cc40c9ef66cd81b.png) | Seçili olsun ya da olmasın, listelenen tüm kalemlere ilişkin kontrat bilgilerini iptal etmek için kullanılan butondur. İthalat faturası oluşmuş kontratların iptali için, öncelikle ilişkili fatura belgesinin iptal edilmesi gerekir. |
| Yenile ![](../../../../../_assets/8c87b0aa5865119d638e.png) | Kalem listesini güncellemek için kullanılan butondur. |

**Faturalarım**

İthalat Dosya İşlemleri ekranı Faturalarım sekmesi, Tedarikçi firmadan gelen ve "Genel" sekmesinde seçilen ithalat dosya numarası ile ilişkili faturalar, kontratlardan oluşturulduktan sonra bu sayfada gösterilir. Ekranın üst bölümünden, faturaların üst bilgileri izlenebilir. Kontrat bilgilerinden kaydedilen faturalar, sistemde "Alış İrsaliyesi" olarak saklanır. Üst kısımda listelenen "Fatura" satırlarında iken, "Düzenle" butonuna tıklandığında, ilgili alış irsaliyesi ekranı açılır ve bu belge üzerinden değişiklik yapılabilir. "Yazdır" butonuna tıklandığında, "Dizayn" modülünde Dizayn Tipi "Alış İrsaliyesi" olan dizaynların basımı yapılır. "İptal" butonuna tıklandığında ise, belgeler silinir. "Ek Maliyet" butonuna tıklandığında, fatura genel toplamına ilave edilmesi istenen maliyetlerin girileceği "Ek Maliyet" bilgi girişi ekranı açılır. Girilen ek maliyet tutarlarının toplamı, belgenin "Toplamlar" alanındaki "Ek Maliyet-1" alanında yazılır. Birim stok fiyatı etkileyecek masraflar, İthalat Masraf Dekont Kayıtları bölümünden girilir. Herhangi bir satır üzerinde iken fare ile çift tıklandığında, ilgili faturadaki kalem bilgilerinin detayları ekranın alt kısmında listelenir. Kalem listesindeki satırlar üzerinde iken fare ile çift tıklandığında ise, seçilen satır için Kalem Ön İzleme/Ek Bilgiler ekranı açılır. Bu ekranda, stoka ait Gümrük Tarife Kodu, DIIB Numarası, Menşei, Rejim Bilgisi, faturadaki Stok Adı ve diğer Ek Bilgiler girilir. İthalat dosyası kapatıldığında oluşan faturanın kalemleri için, bu ekrandan girilen Gümrük Tarife Kodu, DIIB No, Menşei, Rejim ve Fatura Stok İsim alanları bazında kümülasyon yapılarak Gümrük Beyanname Bilgileri/Beyanname Kalem Bilgileri oluşur.

**İthalat Ödeme Bilgileri**

İthalat Dosya İşlemleri ekranı İthalat Ödeme Bilgileri sekmesi İthalat dosyalarına ilişkin planlanan ödemelerin takibi için kullanılır.

| İthalat Dosya İşlemleri Ekranı |  |
| --- | --- |
| Ödeme Tip | Ödeme Açıklamaları bölümünde tanımlanan ödeme tipinin girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, ödeme tipleri arasından seçim yapılır. |
| Ödeme Tarihi | Ödemenin planlandığı tarihin girildiği alandır. |
| Tahmini | Tahmini planlanan ödemeler kesinleşen veya tahmini olabilir. Tahmini ödemeler için kullanılan seçenektir. |
| Ödeme Türü | Bilgi amaçlı olarak ödeme türü girilen alandır. |
| Döviz Tipi | Planlanan ödemenin yapılacağı döviz tipinin girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, döviz tipleri arasından seçim yapılır. |
| Tutar | Seçilen döviz cinsi üzerinden tutarın girildiği alandır. |
| Banka Kodu | Ödemenin yapılacağı bankanın girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, banka kodları arasından seçim yapılır. |
| Referans No | Referans numarasının girildiği alandır. |
| Ödeme Açıklama | Ödemeye ait açıklama bilgisinin girildiği alandır. |
| Açıklama-1,2,3 | Ödemeye ait ek açıklama bilgilerinin girildiği alanlardır. |
| Akreditif Bilgileri | Seçilen ödeme tipi tanımlanırken "Akreditif" seçeneği işaretlenmişse, Akreditif bilgileri girilir. İthalat Ödeme Bilgileri'nden girilen bilgiler bilgi amaçlı olup, entegre modüllerde herhangi bir kayıt oluşturmaz. |

**Nakliye**

İthalat Dosya İşlemleri ekranı Nakliye sekmesi, ithal edilen stokun nakliyesine ilişkin bilgilerin takip edilmesi için kullanılır. Nakliyeci-Acenta-Komisyoncu Bilgileri, Transfer-Yükleme-Sevkiyat Bilgileri, Navlun Tutarı Bilgileri ve Gözetim Bilgileri ile ilgili tanımlamaların yapılmasını sağlar.

**Nakliye Detayları ve Konşimento**

Konşimento bilgilerinin takip edilmesi için kullanılan sekmedir.

**Gümrük Beyanname Bilgileri**

Beyanname Genel, Beyanname Kalem Bilgileri ve Beyanname Masrafları olmak üzere üç sekmeden oluşur. Oluşturulan ithalat dosyası için Gümrük Beyannamesi ile ilgili bilgilerin girildiği ekrandır.

**Beyanname Genel**

Gümrük Beyanname Bilgileri ekranı Beyanname Genel sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Gümrük Beyanname Bilgileri Ekranı |  |
| --- | --- |
| GGB Fiili Tarih | GGB fiili tarihin girildiği alandır. |
| İthalat Tipi | İlgili ithalat tipinin girildiği alandır. |
| Beyanname Kur | Beyannamenin tescil edildiği günün ithalat beyannameleri için Döviz Satış, ihracat için Döviz Alış kurunun girildiği alandır. |
| Beyanname Teslim Şekli | İthalatçı/İhracatçının belirlediği teslim şeklinin seçildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile seçim yapılır. |
| Beyanname Ödeme Şekli | İthalatçının ihracatçı ile anlaştığı ödeme şeklinin, sistemden tanımlanan ödeme tiplerine göre seçildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, ödeme tipleri arasından seçim yapılır. |
| Geldiği Ülke | Malzemenin geldiği ülkenin girildiği alandır. |
| Gümrük Kodu | Gümrük beyannamesine ait gümrük kodunun girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, gümrük kodları arasından seçim yapılır. |
| Gümrükçü Kodu | Gümrük beyannamesine ait gümrükçü kodunun girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, cari kodlar arasından seçim yapılır. |
| GGB No | Gümrük Giriş Beyanname numarasının girildiği alandır. |
| GGB Tarihi | Gümrük Giriş Beyanname tarihinin girildiği alandır. |
| GGB Tescil Tarihi | Gümrük Giriş Beyannamesinin tescil tarihinin girildiği alandır. |
| GGB İntaç Tarihi | Gümrük Çıkış Beyannamesinin kapatıldığı tarihin girildiği alandır. |
| GGB Geliş Tarihi | Gümrük Giriş Beyannamesinin geliş tarihinin girildiği alandır. |
| Kati GGB Tescil No | Gümrük Giriş Beyannamesinin kesin tescil tarihinin girildiği alandır. |
| Kati GB Tarihi | Giriş Beyannamesinin kesin tarihinin girildiği alandır. |
| Antrepo Beyanname No | Antrepo beyanname numarasının girildiği alandır. |
| Antrepo Beyanname Tarihi | Antrepo beyanname tarihinin girildiği alandır. |
| A.TR (ATR) | ATR dolaşım sertifikası bilgilerinin girildiği alandır. |
| EUR.1 | EUR.1 dolaşım sertifikası bilgilerinin girildiği alandır. |
| FORM A | Form A belgesinin bilgilerinin girildiği alandır. |
| Menşei Sert. | Menşei sertifikası bilgilerinin girildiği alandır. |
| Ek Açıklama-1, Ek Açıklama-2, Ek Açıklama-3 ve Ek Açıklama-4 | Gümrük beyannamesine ait ek açıklamaların girildiği alanlardır. |

**Beyanname Kalem Bilgileri**

Gümrük Beyanname Bilgileri ekranı Beyanname Kalem Bilgileri sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Gümrük Beyanname Bilgileri Ekranı |  |
| --- | --- |
| Gümrük Tarife Kodu | Kalemin gümrük tarife kodunun girildiği alandır. |
| Menşei | Kalemin menşei bilgisinin girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, ülke kodları arasından seçim yapılır. |
| Net Kg | Kalemin net kilosunun girildiği alandır. |
| Rejim | Kalemin statüsünün girildiği alandır. |
| Brüt Kg | Kalemin brüt kilosunun girildiği alandır. |
| Açıklama-1 ve Açıklama-2 | Kaleme ait açıklama bilgisinin girildiği alanlardır. |

**Beyanname Masrafları**

Beyanname masraflarının listelendiği sekmedir.

**Debit/Credit Note Bilgileri**

Dış Ticaret yapan firmalar, ticarette çeşitli şekillerde ortaya çıkan maliyete ilişkin tutarları karşılıklı olarak dengelemek amacıyla Debit/Credit (Alacak/Borç) Notu Belgesi düzenleyebilir. Bu notlar; satıcının, satış faturasında yaptığı hataları veya öngörülmeyen durumları düzeltmek için kullanılan bir araç olup, Ticari, Lojistik, Teknik Talepler, Fiyat Düzeltmeleri, Komisyon ve İndirim gibi nedenlerle satıcı tarafından alıcıya yönelik düzenlenir.
İthalat dosyası ile ilgili oluşan bu notların bilgi amaçlı takibi "Debit/Credit Note Bilgileri" sekmesinden yapılır.**Masraf Bilgileri**

Masraf dekont kayıtları üzerinden girilen bilgilerin listelendiği sekmedir.
