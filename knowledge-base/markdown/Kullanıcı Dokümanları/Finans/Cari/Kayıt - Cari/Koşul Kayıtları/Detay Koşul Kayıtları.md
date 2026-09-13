---
title: "Detay Koşul Kayıtları"
page_id: "22803661"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Cari"
  - "Kayıt / Cari"
  - "Koşul Kayıtları"
  - "Detay Koşul Kayıtları"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Cari / Kayıt / Cari / Koşul Kayıtları / Detay Koşul Kayıtları"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTJmNzUwYzBkLTVkMTItNGFmYy1iMWZlLWJkNzk5ZDY3NGQyYyZsaW5rPWQxOTUxMWMwLWI4NjktNDk1Ni04NjA3LWVhYWZiODQyZDg0NSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=2f750c0d-5d12-4afc-b1fe-bd799d674d2c&link=d19511c0-b869-4956-8607-eaafb842d845&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "detay-kosul-kayitlari_28154784_22803661.html"
source_version: "2022-10-27T11:18:39.697+03:00"
source_bytes: 89899
fetched_at: "2026-09-13T04:07:42+00:00"
generator: "netsis-scraper 1.0.0"
---
# Detay Koşul Kayıtları

Detay Koşul Kayıtları, Finans Bölümü'nde Kayıt/Cari menüsünün altında yer alır. "Genel Koşul Kayıtları" bölümündeki tanımlamalar dışında, bir takım detay tanımlamalara ihtiyaç duyulduğunda kullanılması gereken bölümdür. Bir stok veya bir grup stok için satır bazında farklı iskonto oranları tanımlamak, mal fazlası miktarları tanımlamak veya satır bazında iskonto aralıkları tanımlamak, detay tanımlamalar içinde sayılabilir. Detay Koşul Kayıtları; Detay Koşul Bilgileri, Detay Koşul Bilgileri-2, Geçerli Stoklar ve Mal Fazlası olmak üzere dört sekmeden oluşur.

**D****etay Koşul Bilgileri**

Detay Koşul Kayıtları ekranı Detay Koşul Bilgileri sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Detay Koşul Kayıtları Ekranı |  |
| --- | --- |
| Koşul Kodu | "Koşul Sabit Kayıtları" bölümünden kaydedilen ve detay koşulları tanımlanan koşul kodunun girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, koşul kodları arasından seçim yapılır. |
| Kayıt Tarihi | Detay koşulunun tanımlandığı tarihtir. Günün tarihi, program tarafından otomatik olarak ekrana getirilir. |
| Başlangıç Tarihi | İlgili detay koşulun başlama tarihidir. Program tarafından günün tarihi otomatik olarak ekrana getirilir fakat istendiğinde kullanıcı tarafından değiştirilebilir. Boş bırakılamaz. |
| Stok Kodu | Bazı stokların satılmasında veya alınmasında, "Genel Koşul Kayıtları" bölümünde girilen standartların dışında bir uygulama yapıldığı durumlarda kullanılan alandır. Boş bırakılabilir. Yani, birçok stok için "Genel Koşul Kayıtları" bölümünde girilen özellikler (iskonto oranı, vade günü, iskonto aralıkları vs.) kullanılacak, fakat bazı stoklarda farklı koşulların uygulanması istendiğinde kullanılması gereken alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, stok kodları arasından seçim yapılır. **Örneğin:** Stokta A, B ve C mallarının olduğu varsayıldığında, "Genel Koşul Kayıtları" bölümünde bu malların satışı sırasında vade günü "30", İskonto oranı %10 olarak belirlenmişse, C ürünü için satır bazında farklı iskonto oranları veya mal fazlası tanımlanacaksa mutlaka detay koşul tanımlamasının yapılması gerekir. |
| Koşul Rapor Kodu | "Koşul Sabit Kayıtları" bölümünde belirlenen rapor kodudur. "Koşul Sabit Kayıtları" bölümünde rapor kodu olarak "Stok Grup Kodu" seçilmişse, grup kodlarının yer aldığı listeye rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg)ile ulaşılır. Bu durumda ilgili alana, stok grup kodları dışında bir bilgi girilmesine izin verilmez. Bu alanın boş bırakılmasına, sadece "Stok Kodu" alanı doluysa izin verilir. Hem "Stok Kodu" hem de "Koşul Rapor Kodu" alanlarının aynı anda hem dolu hem de boş olmasına izin verilmez. Herhangi birinin dolu olması gerekir. |
| Bitiş Tarihi | Detay koşulun bitiş tarihidir. Boş bırakılabilir. Kullanıcı tarafından girilecek tarih, bu tarihin başlangıç tarihine eşit veya büyük olması gerekir. |
| Tutar/Oran | İlgili detay koşulunda tanımlı stok kodu veya koşul rapor kodundaki stoklar için, uygulanacak satır iskontosunun tutar bazında mı yoksa oran bazında mı olacağının belirlendiği alandır. **Örneğin:** Yapılması istenen iskonto %10 değerinde ise: Oran, 1.000.000 TL tutarında bir iskonto ise: Tutar seçeneğinin işaretlenmesi gerekir. |
| Değer | Yukarıdaki seçime göre tutar veya oran olarak iskonto değerinin girildiği alandır. **Örneğin:** %10’luk bir iskonto yapıldığında, "Tutar/Oran" alanında "Oran" seçilir ve bu alana "10" değeri girilir. Eğer, 1.000.000.TL tutarında bir iskonto uygulanacaksa, "Tutar/Oran" alanında "Tutar" seçilir ve bu alana "1.000.000" değeri girilir. |
| İsk 2,3,4,5,6 | İlgili koşulla işlem gören cari hesaplar için satır bazı 2,3,4,5,6 iskontolarına verilen oranın girildiği alanlardır. |
| Vade Gün | Fatura parametrelerindeki "Her Satırda Vade Günü Sorulsun" parametresi aktif olduğunda, bu alana girilen vade günü fatura ekranında yer alan "Kalemler" sekmesindeki "Vade Günü" alanına aktarılır. |
| Sabit Vade Tarihi | Fatura parametrelerindeki "Her Satırda Vade Günü Sorulsun" parametresi aktif olduğunda, bu alana girilen vade günü fatura ekranında yer alan "Kalemler" sekmesindeki "Vade Günü" alanına aktarılır. |
| Vade Kodu | Vade bazında iskonto belirleme uygulamasıyla bağlantılı olarak ilgili detay koşul kullanıldığında geçerli olacak vade kodudur. Buraya girilecek kodun daha önceden "Vade İskonto Kayıtları" bölümünde tanımlanmış olması gerekir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, vade kodları arasından seçim yapılır. Vade İskonto Kayıtları ile ilgili detaylı bilgi için; Cari → Kayıt → Koşul Kayıtları → Vade İskonto Kayıtları. |
| Vade Hangi İsk. | Vade bazında iskonto belirleme uygulaması ile bağlantılı olarak faturada satır bazında girilecek vade gününe göre, getirilecek satır iskontosunun kaçıncı iskontoya yazılacağının belirlendiği alandır. Bu sahaya "1" değerinin girilmesi, vade iskontosu için 1. satır iskontosunun kullanılacağı anlamına gelir. Burada belirtilen iskonto alanı farklı bir uygulama için kullanılmamalıdır. Vade İskonto Kayıtları ile ilgili detaylı bilgi için; Cari → Kayıt → Koşul Kayıtları → Vade İskonto Kayıtları. |
| Vade İsk. Tipi | Vade iskontosu için hangi iskonto tipinin kullanılacağının belirlendiği alandır. Bu alana "İskonto Tip Kayıtları" bölümünden tanımlanan iskonto tiplerinden biri girilir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, vade iskonto tipleri arasından seçim yapılır. Vade İskonto Kayıtları ile ilgili detaylı bilgi için; Cari → Kayıt → Koşul Kayıtları → Vade İskonto Kayıtları. |
| Miktar | Sipariş, irsaliye ve fatura kayıtlarında girilen stok miktarına göre, fiyat listesindeki kaçıncı fiyatın kullanılacağının önceden belirlenmesi ve bu fiyatın da program tarafından otomatik olarak ekrana getirilmesi için kullanılan alandır. **Örneğin:** "Detay Koşul Kayıtları" ekranında yer alan "Fiyat Miktar Aralığı" bölümündeki "Miktar" alanına 10\<20\<30 gibi bir aralık tanımlandığında, detay koşulun geçerli olduğu stok için faturada girilen miktar; 10’dan küçük ise 1. liste fiyatı, 10-20 arasında ise 2. liste fiyatı, 20-30 arasında ise 3. liste fiyatı, 30’dan büyük ise de 4. liste fiyatı program tarafından otomatik olarak ekrana getirilir. "Detay Koşul Kaydı "sırasında "Fiyat Miktar Aralığı" girilmesi halinde, "Liste Fiyatı" alanı pasif hale gelir. Bunun sebebi, faturaya getirilecek olan fiyatın, "Liste Fiyatı" alanı yerine girilen miktar aralığına göre belirlenmesinden kaynaklanır. |
| Liste Fiyatı | Fiyatların, hangi liste fiyatından alınarak hesaplanacağının belirlendiği alandır. 1 ile 4 arası bir değer girilmesi gerekir. Stok Modülü parametrelerinde yer alan “Özel Fiyat Sistemi” parametresi işaretli ise, tanımlanan listelerdeki fiyat dikkate alınır. İlgili parametre işaretlenmemişse, stok kartlarındaki fiyatlar baz alınarak alış/satış fiyatları otomatik olarak ekrana gelir. **Örneğin:** Özel fiyat sistemi kullanılmadığı zamanlarda bu alana "2" değeri girilmişse, satış ve alış işlemlerinde stok kartlarındaki satış fiyatı–2 veya alış fiyatı–2 alanı ekrana getirilir. |
| Fiyat Tarihi | Stok Modülü parametrelerinde yer alan “Özel Fiyat Sistemi” parametresi işaretli ise bu alana girilen tarih, liste fiyatlarında geçerli olacak tarih olarak kabul edilir. Yani ilgili tarih için belirlenmiş fiyat baz alınarak hesaplama yapılır. Özel fiyat sisteminin kullanılmadığı durumlarda boş bırakılabilir. |
| Fiyat Grubu | Özel fiyat sisteminin kullanıldığı durumlarda, cari hesap için geçerli fiyat grubu "Cari Hesap Kayıtları" bölümünde yer alan "Cari Kart 2" sekmesindeki "Fiyat Grubu" alanında belirtilir. Cari hesapların hangi fiyat listesi ile çalışacağı belirlenirken, ilk önce fatura kaydında girilen koşula ait "Detay Koşul Kayıtları" bölümündeki tanımlamaya bakılır. Burada herhangi bir bilgi bulunmuyorsa, "Cari Hesap Kayıtları" bölümünden girilen "Fiyat Grubu" bilgisine göre işlem yapılır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, fiyat grupları arasından seçim yapılır. |
| Ölçü Birim | "Satış Fatura Parametreleri" bölümünde bulunan “Farklı birimlerden mal çıkışı yapılsın” parametresinin işaretli olması halinde, fatura kaydı sırasında stoka ait farklı ölçü birimlerinden çıkış yapılabilir. Detay koşulun geçerli olduğu stok kartlarında girilmiş farklı ölçü birimleri olması halinde, fatura kaydı sırasında, detay koşulda seçilen ölçü birimi program tarafından ekrana getirilir. Bu alanda 5 adet ölçü birimi desteklenir. Bunlar "Stok Kartı Kayıtları" bölümünün "Ölçü Birimleri" sekmesindeki "Sabit Tanımlamalar" bölümünde bulunan üç ölçü birimi ile, "Çoklu Ölçü Birimi" bölümünde tanımlanarak "Birim Seçimi" alanlarına girilmiş iki ölçü birimidir. Alanın sağ tarafında yer alan aşağı ok butonu yardımı ile ölçü birimleri arasından seçim yapılır. |
| Koşul Kapatılsın Mı? | Tanımlanan koşul detay bilgilerinin geçerli olmasının istenmediği durumlarda kullanılan seçenektir. |
| Grup Koşul | Fatura belgelerinde girilen tüm kalemlerin toplamı üzerinden iskonto ve/veya mal fazlası hesaplaması yapılması istendiğinde işaretlenmesi gereken alandır. Bu alan "Grup Koşul Uygulaması" ile ilgili bir alandır. Grup Koşul Uygulaması ile ilgili detaylı bilgi için; Cari → Ek–5 (Koşul Uygulamalarında Grup Desteği). |

**Detay Koşul Bilgileri-2**

Detay Koşul Kayıtları ekranı Detay Koşul Bilgileri-2 sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Detay Koşul Kayıtları Ekranı |  |
| --- | --- |
| Grup Koşul | Fatura belgelerinde girilen tüm kalemlerin toplamı üzerinden iskonto ve/veya mal fazlası hesaplaması yapılması istendiğinde işaretlenmesi gereken seçenektir. Grup Koşul Uygulaması ile ilgili detay bilgi için; Finans → Cari → Ek 5 (Koşul Uygulamalarında Grup Desteği) |
| İsk.Aralığı Var mı? | İskonto aralığı kullanılması gerektiğinde işaretlenmesi gereken seçenektir. Belli miktar veya tutar limitleri kontrol edilerek satır iskontosu yapılacağı zaman işaretlenir. **Örneğin:** A malından bir siparişteki alış miktarı 1000’in üzerinde olanlara, satır bazında %10 iskonto yapılması istendiğinde veya A malından 50 TL ve üzerinde alışveriş yapanlara %10 satır iskontosu yapılması istendiğinde bu seçenek kullanılabilir. |
| Tutar/Miktar | “İskonto Aralığı Var Mı” seçeneği işaretlendiğinde aktif olan alanlardır. İskonto yapılırken, tutar/miktar kontrolü için tercih yapılması gereken alandır. Miktar seçeneği tercih edildiğinde, kullanılacak stok kodlarının birim ağırlık alanlarına bir değer girilmesi gerekir. Program, faturalarda girilen "miktar" ile "birim ağırlık" alanında girilen değeri çarparak, bulunan yeni miktara göre iskonto oranını otomatik olarak hesaplar. |
| Değer 1, 2, 3 | Tutar/ Miktar alanında yapılan seçime göre değerlerin girildiği alandır. **Örneğin:** A malından 1000 ile 2000 tane alanlara %10 satır iskontosu yapılmak istendiğinde, "Değer-1" alanına 1000, "Değer-2" alanına 2000 değeri girilir. |
| İskonto 1, 2, 3 | Yapılacak iskonto değerinin girildiği alandır. **Örneğin:** "Değer-1" alanına 100 "Değer-2" alanına 200 "Değer-3" alanına 300 "İskonto 1" alanına 10 "İskonto 2" alanına 20 "İskonto 3" alanına 30 ve işlem yapılacak stok kodunun birim ağırlık alanına da 2 değerinin girildiği varsayıldığında, faturada "miktar" alanına "100" değeri girildiğinde bu değer, "birim ağırlık" alanındaki değer ile çarpılarak program tarafından otomatik olarak hesaplanır. Bulunan "200" değerindeki miktara karşılık gelen iskonto oranı da 20 olarak hesaplanır. |
| Hangi Satır İskontosu | Yapılacak iskontonun faturada hangi satır iskontosuna aktarılacağının belirlendiği alandır. Boş bırakılamaz. |
| 30 Gün İçin Peşin İskonto Oranı | "Koşul Sabit Kayıtları" bölümünde yer alan, “Vade İskontosu Veya Faiz Uygulaması" parametresinin işaretli olduğu durumlarda aktif hale gelen alandır. Bu bölüme, 30 gün erken ödemelerde baz alınacak iskonto oranının girilmesi gerekir. 30 günden erken yapılacak ödemelerde, girilen değer oranlanarak iskonto oranı hesaplanır. |
| 30 Gün İçin Fiyata Ekleme Katsayısı | "Koşul Sabit Kayıtları" bölümünde yer alan, “Vade İskontosu Veya Faiz Uygulaması" parametresinin işaretli olduğu durumlarda aktif hale gelen alandır. Bu bölüme, 30 gün geç ödemelerde fiyata eklenecek faiz oranının girilmesi gerekir. |
| Dönem Sonu Ciro/Miktar Hesaplamasına Dahil Edilsin | Ciro primi uygulaması ile ilgili bir alandır. "Dönem Sonu Ciro ve Hakediş Hesaplama" işleminin yapılması için işaretlenmesi gerekir. |
| Ciro İskontosuna Dahil Edilsin | Ciro primi uygulaması ile ilgili bir alandır. İlgili cari hesaplar için ciro iskontosu hesaplaması yapılması istendiğinde işaretlenmesi gerekir. Ciro Primi Uygulaması ile ilgili detay bilgi için; Finans → Cari → Ek 4 /Ciro Primi Uygulaması. |
| Fire Hangi İskonto | Bazı sektörlerde, malların nakliyesi sırasında ağırlıklarında azalma meydana gelir. **Örneğin:** Tavuk veya et gibi ürünlerin nakliyesi sonrası, nakliye süresinde yaşanan su kaybından dolayı ağırlıkları azalır. Böyle durumlarda oluşan firenin, faturada iskonto olarak gösterilmesi için bu alanın kullanılması gerekir. Oluşan firenin, faturada kaçıncı satır iskontosuna yazılacağı da bu alanda belirlenir. |
| Fire İskonto Tipi | Fire iskontosunun takip edileceği iskonto tipinin girildiği alandır. Buraya girilecek iskonto tipinin daha önceden "İskonto Tip Kayıtları" bölümünde tanımlanması gerekir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) yardımı ile iskonto tipleri arasından seçim yapılabilir. Fire İskontosunun uygulanması için burada yapılan tanımlamalar dışında başka tanımlamaların da yapılması gerekir. Yardımcı Programlar → Özel Parametre Tanımları bölümünde, aşağıdaki yer alan iki tanımlamanın yapılması gerekir. Bu tanımlama ile fire iskontosunun cari ve stok kartlarında hangi alandan kontrol edileceği belirlenir. ![](../../../../../_assets/789004393edd8b292dcf.png) Ekrandaki değer alanına "KULL1N" tanımı girilmiş. Bu, fire iskontosunun kullanıcı tanımlı sahalardaki 1. sayısal alana girileceği anlamına gelir. İstendiğinde, kullanıcı tanımlı alanlardaki farklı bir sayısal alan da belirlenebilir. Stok ve cari kartta bulunan "Kullanıcı Tanımlı Sahalar" sekmesinde, özel parametrede belirtilen alana, stok ve cari hesap için fire iskonto oranları girilir. **Örneğin:** Fire uygulamasında stoka ait fire oranı sabitken cari hesaplara göre değişiklik gösterebilir. Bu durum, fire oranının cari hesapların uzaklıklarına göre değişkenlik göstermesinden kaynaklanır. Yakın mesafedeki cari hesaba mal gönderilirken fire daha az olmakla birlikte, uzak mesafedeki cari hesaba gönderilen malda daha fazla fire meydana gelir. Dolayısıyla, stok kartlarına girilen fire oranı ve cari karta girilen fire oranı birlikte dikkate alınır ve fatura kaydında, detay koşulda belirlenen iskonto alanına bu iki oranın çarpımı aktarılır. Nakliye sırasında fire oluşan stoka ait iskonto oranı: 2 (Bu oran özel parametrede belirtilen kullanıcı tanımlı sahaya girilir). Yakın mesafeli müşteri için fire sayısı: 3 Uzak mesafeli müşteri için fire sayısı: 5 (bu oranların cari karttaki kullanıcı tanımlı sahalara girilmesi gerekir) olarak girildiğinde; Mesafesi yakın olan cari hesaba ilgili stok için fatura kaydı girildiğinde, fire için detay koşulda belirtilen iskonto alanına 6(2\*3) aktarılır. Mesafesi uzak olan müşteriye aynı stok için aktarılacak iskonto oranı ise, 10(2\*5)'dur. |

**Geçerli Stoklar**

Detay Koşul Kayıtları ekranı Geçerli Stoklar sekmesi, Koşul Sabit Bilgileri bölümünde, ilgili stok için yapılan tanımlamada "Çoklu Seçim" seçeneğinin işaretlenmesi halinde ekrana gelir. Burada, tanımlanan detay koşul bilgilerinin, hangi stoklar için geçerli olduğu belirlenir.

**Örneğin:**

Tanımlanan koşulun, sadece "Grup Kodu 6" olan stoklar için geçerli olması istendiğinde, "Koşul Sabit Kaydı" sırasında "Koşul Rapor Kodu" olarak "Stok Grup Kodu" seçilmesi ve ilgili grup kodunun "Detay Koşul Bilgileri" alanında belirtilmesi yeterlidir.
Koşulun geçerli olacağı stoklar belirlenirken, birden fazla alana ihtiyaç duyulması halinde, "Koşul Sabit Kayıtları" bölümünde "Çoklu Seçim" işaretlenerek "Geçerli Stoklar" sekmesinde birden fazla alan için kısıt verilebilir.

**![](../../../../../_assets/a979e34348dfadd39311.png)**

Tanımlanan koşulun, Grup Kodu 6 ve Kod-1'i K1 olan stoklar için geçerli olması istendiğinde, ekrandaki gibi bir tanımlama yapılması gerekir.
Bu ekranda, "Saha Adı" sütununun üzerinde iken klavyede "Ara Çubuğuna" basıldığında, bilgi girişi yapılması için alan aktif hale gelir.

**Örneğin;**

"Grup Kodu" için kısıt verilmesi istendiğinde, "Saha Adı "sütununda iken klavyedeki "Ara Çubuğuna" basılması ve aşağı ok tuşuna basılarak "Grup Kodu" alanının seçilmesi gerekir. Daha sonra "Enter" tuşuna basıldığında girilen bilgi saklanır ve sağdaki hücreye ilerlenir.

Bu bölümde birden fazla alan için kısıt verilecekse, klavyede bulunan "Insert" tuşuna basılarak yeni satır eklenebilir. Eklenmiş bir satırın silinmesi için de, ilgili satır seçildikten sonra yine klavyedeki "Delete" tuşuna basılması gerekir.

Operatör, Değer 1 ve Değer 2 alanlarında, kısıtın hangi alanlara ve koşullara göre verileceği seçilir.

"Ve" seçeneği seçildiğinde, iki kısıtı da aynı anda sağlayan kayıtlar dikkate alınır.

"Veya" seçeneği seçildiğinde, iki kısıttan biri bile koşulu sağlıyorsa o kayıt dikkate alınır.

"Detay Koşul Kayıtları" bölümündeki "Çoklu Seçim Uygulaması" ile, bir stok için aynı koşul koduna ait birden fazla detay koşul kaydı geçerli olabilir.

**Örneğin:** Bir detay koşul kaydında, grup kodu 'A' olan stoklar, diğer detay koşul kaydında ise kod-1'i '001' olan stoklar koşula dahil edildiğinde, grup kodu 'A' olup da kod-1'i '001' olan bir stok her iki detay koşul kaydı için de geçerli olur. Ancak faturalama belgelerinde, program ilk sıradaki detay koşul kaydına göre işlem yapar.

**Mal Fazlası**

Detay Koşul Kayıtları ekranı Mal Fazlası sekmesi yapılan detay koşul tanımlamasının geçerli olacağı stoklar için mal fazlası verileceği durumlarda kullanılan bölümdür.

| Detay Koşul Kayıtları Ekranı | Mal Fazlası |
| --- | --- |
| Mal Fazlası Grup | Geçerli mal fazlası stoklarının belirlenmesi için işaretlenmesi gereken seçenektir. **Örneğin:** Makarna ve salça satan bir firmanın, makarna grubundan alım yapan müşterilerine salça grubuna ait ürünlerden mal fazlası verdiği varsayıldığında, koşul tanımlaması makarna grubunu kapsayacak şekilde yapılır. Daha sonra "Mal Fazlası Grup" seçeneği işaretlenerek "Geçerli Stoklar" alanında salça grubuna ait stoklar için kullanılan rapor kodlarına göre kısıt verilir. |
| Mal Fazlası Stok Kodu | "Mal Fazlası Stok Kodu" alanına mal fazlası olarak verilecek stok kodu girilir. Böylece koşulun geçerli olduğu stokların satışında bu alana girilen stok, mal fazlası olarak verilir. Faturada girilen stok kodu ile mal fazlası stok kodu aynı olursa, stok kodu ile mal fazlası aynı satırda gösterilir. Eğer faturada kullanılan stok kodu ile mal fazlası stok kodu farklı olursa, bu durumda mal fazlası ayrı bir satırda gösterilir. |
| Miktar-1 | Hangi miktardaki mal için mal fazlası iskontosu verilecekse, ilgili miktarın girildiği alandır. **Örneğin:** 100 adet mal için mal fazlası verilecekse, 100 değerinin girilmesi gerekir. |
| Mal Fazlası-1 | "Miktar-1" alanına girilen miktar için, hangi miktarda mal fazlası verileceği ile ilgili değer girilen alandır. **Örneğin:** 10 değeri girildiğinde, 100 adet mal için 10 adet mal fazlası verileceği anlaşılır. |
| Miktar-2 | Yukarıda girilen oranların dışında, farklı bir mal fazlası uygulaması yapılacağı zaman kullanılması gereken alandır. **Örneğin:** 200 adet mal için 25 adet mal fazlası girilecekse, 200 değerinin girilmesi gerekir. |
| Mal fazlası-2 | "Miktar-2" alanına girilen değer için, verilecek mal fazlası miktarının girildiği alandır. **Örneğin:** 25 adet mal fazlası girilecekse, 25 değerinin girilmesi gerekir. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır. Yapılan kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
