---
title: "Stok Kartı Kayıtları"
page_id: "22803581"
product: "netsis-3-enterprise"
depth: 5
is_section: true
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Stok"
  - "Kayıt / Stok"
  - "Stok Kartı Kayıtları"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Stok / Kayıt / Stok / Stok Kartı Kayıtları"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTk1NzMxMmUwLTUxY2EtNDMwMi05YjViLTYxYTVlODZhM2Q4MCZsaW5rPTM3ZDNjYmJmLWQ4OTQtNDE2Mi1hOGE3LWE1ODFlMzQ5MjIxNyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=957312e0-51ca-4302-9b5b-61a5e86a3d80&link=37d3cbbf-d894-4162-a8a7-a581e3492217&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "stok-karti-kayitlari_22804423_22803581.html"
source_version: "2022-10-25T14:54:48.300+03:00"
source_bytes: 203856
fetched_at: "2026-09-13T04:03:53+00:00"
generator: "netsis-scraper 1.0.0"
---
# Stok Kartı Kayıtları

Stok Kartı Kayıtları, Lojistik - Satış Bölümü'nde, "Kayıt/Stok" menüsünün altında yer alır. Programın genelinde, stoklarla ilgili bir işlem yapılması için (giriş, çıkış, sayım, üretim vb.) stok kartlarının öncelikle "Stok Kartı Kayıtları" bölümünden tanımlanması gerekir. Tanımlanan stok kart bilgileri Fatura, Üretim ve Müstahsil Modüllerinde kullanılarak kayıt oluşturulur. Oluşan kayıtlar sonucu, giriş/çıkış hareketleri de entegre bağlantısı nedeniyle "Stok Hareket Kayıtları" bölümünde toplanır.

Stok Kartı Kayıtları; [Stok Kartı-1](#stokkarti1), [Ölçü Birimleri](#olcubirimleri), [Stok Kartı-2](#stokkarti2), [Fiyatlar](#fiyatlar), [Ek Bilgiler](#ekbilgiler), [Kullanıcı Tanımlı Sahalar](#kullanicitanimlisahalar), [Tutar/Miktar Bilgileri](#tutarmiktarbilgileri), [Stok Bilgisi](#stokbilgisi), [Lokal Depo Bakiye Listesi](#lokaldepobakiye), [Seri Takibi Fiyat Bilgileri](#seritakibi), [Reçete Bilgileri](#recetebilgileri) ve [Döviz Bilgileri](#dovizbilgileri) sekmelerinden oluşur. "Stok Kartı Kayıtları" bölümüne girilerek yeni bir kart tanımlandığında veya var olan bir stok kartı rehber butonu yardımı ile ![](../../../../../_assets/088477bb321d1b20c939.jpg) ekrana getirildiğinde, stokla ilgili tüm sekmelere ulaşılır.

Firmalar, döviz kullanımı, üretim ve maliyet muhasebesi uygulamaları, üretimde seri takibi uygulamaları veya belirli fiyat listeleri oluşturarak, bunlar üzerinden satış yapma durumlarına göre kendileriyle ilgili olan alanları kullanabilirler. Bu uygulamalar ile ilgili alanların hangileri olduğu ile ilgili açıklamalar aşağıda yer alır.

**Stok Kartı-1**

Stok Kartı Kayıtları ekranı Stok Kartı-1 sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Stok Kartı Kayıtları Ekranı |  |
| --- | --- |
| Stok Kodu | Stoklara ait kod bilgisinin tanımlandığı alandır. belirlenmektedir. Herhangi bir stok kodu, sadece tek bir stok için geçerlidir ve diğer stoklar için kullanılmaz. Stok kodları, en fazla 35 karakter uzunluğunda olmak üzere, sayısal ya da alfa sayısal karakterler kullanılarak oluşturulur. Stok kodu vermeden stok kartı açılmaz. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile tanımlanmış stok kodlarına ulaşılır. |
| Stok Adı | Stoklara ait isim bilgisinin girildiği alandır. Stok adı en fazla 50 karakter uzunluğunda olabilir. |
| İngilizce İsim | Stoka ait İngilizce isim bilgisinin girildiği alandır. İngilizce isim en fazla 50 karakter uzunluğunda olabilir. |
| Check Digit | Stok → Kayıt → [Stok Parametreleri](<../Stok Parametreleri.md>) → "Check Digit Kontrolü" parametresinin işaretlendiği durumlarda, "Stok Kartı Kayıtları" ekranına "C.D" seçenek alanı eklenir. Stok kodunda sorgulanan "C.D" seçeneği, stok kodunu barkod numarası olarak tanımlayan firmalar tarafından kullanılır. Barkod numaraları belirli bir düzen içinde tanımlanır. Barkodun en sonunda yer alan numara bir tür hesaplamayla bulunur ve bu hesaplama tüm barkodlar için aynı şekilde yapılır. **Örneğin:** 7 karakterlik bir stok kodu girilip "C.D" seçeneğinin işaretlendiğinde, girilen karakterler için hesaplama yapılır ve bulunan rakam 8. karakter olarak stok koduna eklenir. |
| Satış/Alış KDV Oranı | Stoklara ait alış ve satış KDV oranlarının girildiği alandır. Fatura belgelerinde KDV hesaplaması yapılırken ilk olarak bu alan kontrol edilir. Dolayısıyla, bu alanlara KDV oranlarının girilmemesi halinde KDV tutarı hesaplanmaz. |
| Risk Süresi | Tanımlanan stokun (zaman birimi belirtmeden) dayanma süresinin (bozulmadan) girildiği alandır. Stok kaydının ambarda en fazla ne kadar süre kalacağı belirtilerek (Örneğin, 30 gün dayanma süresi olan bir ürün için bu alana 30 yazılır), rapor alınmasını sağlar. İlgili süre Gün, Hafta veya Ay bazında olabilir. Girilen süreye ait zaman birimi, "Stok Kartı Kayıtları" ekranında yer alan "Zaman Birimi" alanından belirlenir. |
| Zaman Birimi | "Risk Süresi" alanında girilen süre bilgisine ait birimin belirlendiği alandır. Risk süresi hangi zaman birimi bazında (Gün, Hafta, Ay vb.) girildiyse, bu alana zaman birimi ile ilgili iki karakterlik kısaltma (GN, HF, AY, vb.) girilebilir. |
| Muhasebe Detay Kodu | Stok veya stok grupları bazında muhasebe hesap takibi yapan firmaların mutlaka bilgi girişi yapmaları gereken alandır. Hesap planının stok detaylı olarak takip edildiği durumlarda, çalışacak hesaplar öncelikle Stok → Kayıt → "[Muhasebe Detay Kod Girişi](<../Muhasebe Detay Kod Girişi.md>)" bölümünde tanımlanır. Daha sonra tanımlanan muhasebe detay kodları stoklar ile eşleştirilir. Stok hesaplarının stok veya stok grupları bazında detay olmadan takip edildiği durumlarda ise bu alan 0 (sıfır) olarak ekrana gelir ve değiştirilmesine gerek yoktur. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile tanımlanmış muhasebe detay kodlarına ulaşılır. |
| Depo kodu | Stok → Kayıt → [Stok Parametreleri](<../Stok Parametreleri.md>) → "Lokal Depo Uygulaması" parametresinin işaretlendiği durumlarda, ilgili malın işlem gördüğü lokal depo kodunun girildiği alandır. Stoka ait yerel depo kodunun bu alana girilmesi için öncelikle Stok → Kayıt → [Lokal Depo İşlemleri](<../Lokal Depo İşlemleri/index.md>) → "Depo Tanımlama" bölümünden tanımlanması gerekir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile tanımlanmış depo kodlarına ulaşılır. |
| Resim Alanı | Tanımlanan stoka ait resim ya da doküman dosyasının eklenmesi için kullanılan alandır. Buraya eklenen resim dosyası ile stok ilişkilendirilir ve böylece stokla ilgili basım yapıldığında, karta eklenen resim de bastırılabilir. |

**Ölçü Birimleri**

Stok Kartı Kayıtları Ölçü Birimleri, stok bazında ölçü birimlerinin tanımlanması için kullanılan sekmedir. Tek bir stok için sınırsız sayıda ölçü birimi tanımlanabilir. Ölçü birimi tanımlamaları "Sabit Tanımlamalar" ve "Çoklu Ölçü Birimi" olmak üzere iki bölümden yapılır.

| Stok Kartı Kayıtları Ekranı | Sabit Tanımlamalar |
| --- | --- |
| Br-1/Br-2/Br-3 | Satış/alış ya da üretim kayıtlarında en fazla hangi ölçü birimiyle işlem yapılıyorsa, ilgili ölçü biriminin girildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile ölçü birimi seçeneklerinden biri seçilir. "Sabit Tanımlamalar" bölümünde 3 adet ölçü birimi tanımlanabilir. Kullanılacak temel ölçü birimi, Br-1'dir. Faturalama sırasında (parametrelerde yapılacak bir düzenleme ile) diğer ölçü birimlerinden de giriş/çıkış yapılabilir. Ancak program, stok hareketlerini her zaman ölçü birimi 1, yani temel ölçü birimine göre çevirerek hareket kayıtlarına aktarır. Stoklar ile ilgili hareket kayıtlar (giriş/çıkış) oluşturulduktan sonra, temel ölçü birimi değiştirilmemeli. Aksi takdirde, raporlarda ve "Stok Hareket Kayıtlarında" hatalar meydana gelir. Stok Hareket Kayıtları ile ilgili detaylı bilgi için; Stok → Kayıt → [Stok Hareket Kayıtları](<../Stok Hareket Kayıtları/index.md>) dokümanına bakılabilir. Birinci ölçü birimi tanımlandıktan sonra diğer ölçü birimleri tanımlanırken, birinci ölçü birimine göre çevrim değerleri belirlenir. ![](../../../../../_assets/a8d1260d229f694bf1b9.png) Çevrim değerleri pay/payda değerleri ile oluşturulur. **Örneğin:** Birinci ölçü birimi AD (Adet) olan bir stoka ait diğer ölçü birimlerinin KG (Kilogram) ve PK (Paket) olduğu varsayıldığında, Ölçü birimlerine ait pay payda değerleri de sırasıyla ½ ve ¼ olarak tanımlandığında, 1 kilo stokun 2 adet, 1 paket stokun da 4 adet olduğu anlaşılır. Dolayısıyla, fatura belgesinde 2 PK (paket) stok çıkışı yapıldığında stok hareketlerinden 8 adet çıkış gerçekleşir. |
| Çoklu Girişleri Güncelle ![](../../../../../_assets/975d8b87e19407bdc6a7.png) | "Sabit Tanımlamalar" bölümünde yapılan ölçü birimi tanımlamalarının "Çoklu Ölçü Birimi" bölümüne aktarılması için kullanılan butondur. Girilen ölçü birimleri, "Çoklu Ölçü Birimleri" bölümüne aktarıldıktan sonra, "Sabit Tanımlamalar" bölümünde değişiklik yapılması halinde, yapılan değişiklikler "Çoklu Ölçü Birimi" bölümüne aktarılmaz. Ancak, Çoklu Girişleri Güncelle ![](../../../../../_assets/f603e711aedaad1817ba.png) butonu kullanılarak, "Çoklu Ölçü Birimi" alanının güncellenmesi sağlanabilir. |
| Stok Kartı Kayıtları Ekranı | Çoklu Ölçü Birimi |
| Ölçü Birimi | Üçten fazla ölçü biriminin bulunması halinde kullanılan alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile tanımlanmış ölçü birimlerine ulaşılır. Ölçü birimlerinin her birine, çevrimde kullanılacak pay, payda, en, boy, yükseklik gibi ebat bilgileri girilir. "Sabit Tanımlamalar" bölümünde yer almayan ve bu alana ayrıca girilen ölçü birimlerinden en fazla iki tanesi fatura ve stok raporlarında kullanılabilir. Bu iki ölçü biriminin hangileri olduğu "Birim Seçimi" alanında belirlenir. |
| Birim Seçimi | Stoklarda farklı sayıda farklı ölçü birimleri tanımlanabildiği için, fatura kaydı ve stok raporlarında (ölçü birimi 1,2,3 haricinde) "Birim Seçimi-1" ve "Birim Seçimi-2" alanlarında belirlenen ölçü birimleri dahil olmak üzere toplam beş ölçü birimi ile raporlama ve çevrim işlemleri yapılabilir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile tanımlanmış birim seçimi kodlarına ulaşılır. "Çoklu Ölçü Birimi" bölümünde girilen, "Sabit Tanımlamalar" ve "Birim Seçimi" alanlarında bulunmayan ölçü birimleri sadece bilgi amaçlıdır. Fatura işlemleri ve stok raporlarında bu ölçü birimleri için çevrim işlemi yapılmaz. "Çoklu Ölçü Birimi" kullanımı ile ilgili detaylı bilgi için; Stok → [Ek-2 (Ölçü Birimi Uygulamaları)](<../../Ekler (Stok)/Ek-2 (Ölçü Birimi Uygulamaları).md>) dokümanına bakılabilir. |
| Fiyat Birimi | Stokların alış ve satış faturalarının fiyatlandırılmasında işlem göreceği temel ölçü biriminin belirlendiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu yardımı ile fiyat birimleri arasından seçim yapılır. |

**Stok Kartı-2**

Stok Kartı Kayıtları ekranı Stok Kartı-2 sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Stok Kartı Kayıtları Ekranı |  |
| --- | --- |
| Stok Kodu | Stok kodu ve isim bilgisinin program tarafından otomatik olarak aktarıldığı alandır. |
| Birim Ağırlık | Stokun birim ağırlığının girildiği alandır. Birim ağırlık bilgisi, cari sabit kartlarındaki nakliye katsayısı ve fatura modülündeki birim ağırlık iskontosu uygulamalarıyla bağlantılı olarak çalışır. Uygulamaların aktif hale gelmesi için ilgili modüllerden düzenleme yapılması gerekir. Bunun haricinde irsaliye veya faturada toplam mal ağırlığının görülmesi veya dizayn üzerinde basılması için bu alana birim ağırlığın girilmesi gerekir. Nakliye uygulaması ile ilgili detaylı bilgi için; Fatura → Kayıt → [Alış Parametreleri](<../../../Fatura/Kayıt - Fatura/Alış Parametreleri.md>)/[Satış Parametreleri](<../../../Fatura/Kayıt - Fatura/Satış Parametreleri.md>) → Ek Maliyet dokümanına bakılabilir. |
| Nakliye Tutar | Cari kartta yer alan "Nakliye Katsayısı" alanıyla bağlantılı olarak çalışır. Birim ağırlık başına hesaplanan nakliye tutarının girilmesi gerekir. Nakliye uygulaması ile ilgili detaylı bilgi için; Fatura → Kayıt → [Alış Parametreleri](<../../../Fatura/Kayıt - Fatura/Alış Parametreleri.md>)/[Satış Parametreleri](<../../../Fatura/Kayıt - Fatura/Satış Parametreleri.md>) → Ek Maliyet dokümanına bakılabilir. |
| Önceki Kodu | Stoklarda kod değişikliği yapılması halinde, eski kodun program tarafından aktarıldığı alandır. Stok → İşlemler → [Kod Değiştirme](<../../İşlemler - Stok/Kod Değiştirme.md>) bölümünden değiştirilen yeni kod stok kodu alanına, eski kod ise bu alana aktarılır. Alanın sağ tarafında yer alan görüntüle butonu ![](../../../../../_assets/58de576353e14f2b2ed8.png) ile, "Stok Kodu Tarihçesi" ekranına ulaşılır. Bu ekran "Kod Değiştirme" işlemiyle yapılan stok kodu değişikliklerinin raporlanmasını sağlar. Kod üzerinden birden çok değişiklik yapıldığında, değişikliklerin tamamı geçmiş senelerdeki şirketler de dikkate alınarak raporlanır. Kullanıcı tarafından, geçmiş yıllardaki şirketlere ait stok kodu tarihçesi tanımlanabilir fakat kod değiştirme işlemi ile oluşan kayıtlar üzerinde değişiklik yapılamaz. ![](../../../../../_assets/6c80e053558c2ef25053.png)<br>Stok kod değişikliği ile ilgili detaylı bilgi için; Stok → İşlemler → [Kod Değiştirme](<../../İşlemler - Stok/Kod Değiştirme.md>) dokümanına bakılabilir. |
| Sonraki Kodu | Stok kartlarında değiştirilen kodun yenisinin girildiği alandır. Firmalar bu alana bakarak ilgili stok hareketlerinin hangi stok koduna aktarıldığını görebilir. Stok kod değişikliği ile ilgili detaylı bilgi için; Stok → İşlemler → [Kod Değiştirme](<../../İşlemler - Stok/Kod Değiştirme.md>) dokümanına bakılabilir. |
| Son Stok Kodu | Stok kartlarında kodu birden fazla değiştirilmiş stok için verilen yeni kodlardan sonuncusunun girildiği alandır. Firmalar bu alana bakarak ilgili stok hareketlerinin en son hangi stok koduna aktarıldığını görebilirler. Stok kod değişikliği ile ilgili detaylı bilgi için; Stok → İşlemler → [Kod Değiştirme](<../../İşlemler - Stok/Kod Değiştirme.md>) dokümanına bakılabilir. |
| Barkod 1, 2, 3 | Barkod cihazları ile çalışma yapan (örneğin; süpermarket vb.) firmalarda, stokların barkod numaralarının girildiği alandır. Birden fazla satıcıdan alım yapan firmalar, aynı mallar için değişik barkod kodu kullanmak zorunda kalabilirler. Böyle durumlarda en çok kullanılandan en az kullanılana doğru malların 2.ve 3. barkod kodları da ilgili alanlara girilir. Bir stok kartına ait aynı barkod numarası birden fazla girilemez. Stoka ait barkod bilgisinin bu alanlara girilmesi ile, fatura belgelerinde kalem girişi sırasında stok kodu yerine barkod bilgisi de kullanılabilir. |
| C.D | Stok → Kayıt → [Stok Parametreleri](<../Stok Parametreleri.md>) → "Check Digit Kontrolü" parametresinin işaretlendiği durumlarda, "Stok Kartı Kayıtları" ekranında barkod alanlarının yanına "C.D" seçenek alanı eklenir. Stok kodunda sorgulanan "C.D" seçeneği, stok kodunu barkod numarası olarak tanımlayan firmalar tarafından kullanılır. Barkod numaraları belirli bir düzen içinde tanımlanır. Barkodun en sonunda yer alan numara bir tür hesaplamayla bulunur ve bu hesaplama tüm barkodlar için aynı şekilde yapılır. **Örneğin:** 7 karakterlik bir stok kodu girilip "C.D" seçeneğinin işaretlendiğinde, girilen karakterler için hesaplama yapılır ve bulunan rakam 8. karakter olarak stok koduna eklenir. |
| Stok Kartı Kayıtları Ekranı | Rapor Kodları |
| Cari/S Kodu | Tanımlanan stokun hangi satıcıdan alındığı bilgisinin stok kartında görülmesi ve buna göre diğer uygulamalarda kullanılması için, ilgili satıcının cari hesap kayıtlarındaki kodunun girildiği alandır. Bu durumda, Üretim → MRP → İşlemler → "Malzeme Gereksiniminden Sipariş Oluşturma" ve Stok → İşlemler → "Netsis Sipariş Önerisi" bölümleri ile oluşturulan siparişlerde, bu alana girilen satıcı kodları kullanılır. Cari/S kodunun sipariş oluşturma işlemlerinde kullanımı ile ilgili detaylı bilgi için; Üretim → MRP → İşlemler → "Malzeme Gereksiniminden Sipariş Oluşturma" ve Stok → İşlemler → "[Netsis Sipariş Önerisi](<../../İşlemler - Stok/Netsis Sipariş Önerisi/index.md>)" dokümanına bakılabilir. |
| Üretici Kodu | Tanımlanan stoka ait alış faturalarındaki kodların girildiği alandır. Böylece, satıcının/alıcının ilgili stok için kullandığı kod bilgisi kayıt altında olur ve fatura belgelerinde de satıcının/alıcının stoka vermiş olduğu kod kullanılabilir. Stok, birden fazla satıcıdan alındığında ya da birden fazla alıcıya satıldığında, içlerinde en fazla kullanılan kodlama sisteminin tercih edilmesi gerekir. Cari hesap bazında kullanılan stok kodları, Stok → Kayıt → [Müşteri/Satıcı Stok Kayıtları](<../Müşteri - Satıcı Stok Kayıtları.md>) bölümünden tanımlanır. |
| Grup Kodu | Stoklarla ilgili gerçekleştirilen bazı işlemlerin daha hızlı ve kolay, alınan raporların da daha hızlı ve ayrıntılı olması için kullanılan alandır. Grup kodu alanı, stokların sahip oldukları özellikler bazında gruplanarak sadece belli bir mal grubu için işlem yapılmasını ya da rapor alınmasını sağlar. Bunun için ilgili mal grubuna en fazla 8 karakter uzunluğunda bir kod tanımlayarak, gruba ait malların kodu bu alana girilir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, tanımlanmış grup kodlarına ulaşılır. **Örneğin:** Malların alındığı yere göre grup kodlaması yapılabilir. Grup kodu, Stok → Stok Kod Kayıtları → [Grup Kodu Kayıtları](<../Stok Kod Kayıtları/Grup Kodu Kayıtları.md>) bölümünden kaydedilmediyse, "Stok Parametreleri" bölümünde yer alan "Grup Açıklama" parametresi işaretlenerek, stok kartından grup kodlarına ait açıklama girişi yapılabilir. Kaydederken açılan ekrana grup kodunun ismi girildiğinde, "Grup Kodu Kayıtları" bölümüne bu bilgi otomatik olarak aktarılır. "Grup Kodlarının Tanımlanması" ile ilgili detaylı bilgi için; Stok → Stok Kod Kayıtları → [Grup Kodu Kayıtları](<../Stok Kod Kayıtları/Grup Kodu Kayıtları.md>) dokümanına bakılabilir. "Grup Açıklama" parametresinin kullanımı ile ilgili detaylı bilgi için; Stok → Kayıt → [Stok Parametreleri](<../Stok Parametreleri.md>) dokümanına bakılabilir. |
| Kod-1/Kod-2/Kod-3/Kod-4/Kod-5 | Stok işlemleri ve raporlamalarda kullanılmak üzere, gruplama mantığı ile 8 karakter uzunluğunda kod bilgisinin girildiği alanlardır. Bu alanların kullanım amaçları "Grup Kodu" alanı ile aynıdır. "Stok Kod Kayıtları" bölümünde bulunan Kod-1, Kod-2, Kod-3, Kod-4, ve Kod-5 kayıtlarının alt menülerinde tanımlanan kod bilgilerine, rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) yardımı ile ulaşılır. Daha önce "Stok Kod Kayıtları" bölümünde bulunan menülerden tanımlaması yapılmayan kod , bu alana girilebilir. Fakat bu şekilde yapılan girişlerde koda ait açıklama tanımlanamaz. |
| Ebat Bilgileri | Stoka ait en, boy ve genişlik gibi ebat bilgilerinin girildiği alanlardır. |
| İşletmelerde Ortak | Tanımlaması yapılan kodların hangi işletmede kullanılacağının belirlendiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile işletme kodları arasından seçim yapılır. Bu alana -1 değerinin girilmesi halinde, stokun tüm işletmelerde kullanılacağı anlaşılır. İşletme ile ilgili detaylı bilgi için; Yardımcı Programlar → Kayıt → Şirket - [Şube Parametre Tanımları](<../../../../Genel/Yardımcı Programlar/Kayıt - Yardımcı Programlar/Şirket - Şube - Parametre Tanımları.md>) → İşletmeler dokümanına bakılabilir. |
| Şubelerde Ortak | Tanımlaması yapılan kodların hangi şubede kullanılacağının belirlendiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile şube kodları arasından seçim yapılır. Bu alana -1 değerinin girilmesi halinde, stokun tüm şubelerde kullanılacağı anlaşılır. "Şubelerde Ortak" alanı, sadece içinde bulunulan şubenin merkez şube olması halinde aktif hale gelir. İşletme ile ilgili detaylı bilgi için; Yardımcı Programlar → Kayıt → [Şirket - Şube Parametre Tanımları](<../../../../Genel/Yardımcı Programlar/Kayıt - Yardımcı Programlar/Şirket - Şube - Parametre Tanımları.md>) → İşletmelerBir stok kartı tüm işletmelerde ortak kullanılacaksa, İşletme Kodu alanı -1 değerini alır. Bir stok kartı X işletmesinin tüm şubelerinde ortak olacaksa, İşletme Kodu alanı X’ işletmesinin değeri, Şube Kodu alanı da -1 değerini alır. Eğer X işletmesinin kodu 2, X merkezinin şube kodu 200 ise, X işletmesinin merkezine özel bir stok kartı açıldığında, İşletme Kodu=2 ve Şube Kodu=200 değerini alır. |
| Hariç Tutulacak Şube Tanımlamaları | "Hariç Tutulacak Şube Tanımlamaları" yazısının üzerine tıklandığında, mevcut şubeler içinde, hariç tutulması istenen şubeler için sol fare tuşu ile çift tıklanarak seçim yapılan alandır. |

**Fiyatlar**

Stok Kartı Kayıtları ekranı Fiyatlar sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Stok Kartı Kayıtları Ekranı |  |
| --- | --- |
| Stok Kodu | Stok kodu ve isim bilgisinin program tarafından otomatik olarak aktarıldığı alandır. |
| Satış fiyatı 1, 2, 3, 4 | Stok satış fiyatlarının girildiği alanlardır. Özellikle vadelere göre farklı fiyat uygulaması olan firmalar, tek stok için birden fazla fiyat tanımlayarak istedikleri fiyatın fatura kaydı sırasında ekrana gelmesini sağlayarak işlem yapabilirler. |
| Alış fiyatı 1, 2, 3, 4 | Stok alış fiyatlarının girildiği alanlardır. |
| Stok Kartı Kayıtları Ekranı | **Özel Fiyat** **Stok → Kayıt → [Stok Parametreleri](<../Stok Parametreleri.md>) → "Özel Fiyat Sistemi" parametresinin işaretlenmesiyle aktif hale gelen alandır. Stok → Kayıt → "Stok Fiyat İşlemleri" bölümünün kullanılması halinde, bu bölümden oluşturulan fiyat listesinin stok kartıyla bağlantısının yapılması sağlanır.** **"Stok Fiyat İşlemleri" menüsündeki bölümler (stok kartlarında tanımlı olan fiyatlar kullanılmadan), farklı amaçlı tarihsel fiyat listelerinin oluşturulması ve oluşturulan fiyat listelerindeki alış/satış fiyatlarının grup tanımlanarak değiştirilmesini sağlar. Girilen fiyatlar "Fatura" modülünde de kullanılabilir. Oluşan fiyat listeleri, "Cari" modülde bulunan “Koşul Kayıtları” bölümüyle bağlantılı kullanılabilir.** |
| Fiyat Kodu | Tanımlanan stokun bağlı olacağı fiyat kodunun, Stok → Kayıt → Stok Fiyat İşlemleri → "Fiyat Kodu Tanımlamaları" bölümünden kaydedildikten sonra girildiği alandır. Alış ve/veya satış fiyat değişikliği yapılırken, belirlenen fiyat koduna ait stokların fiyatları değiştirilebilir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile tanımlanmış fiyat kodlarına ulaşılır. |
| Fiyat Sırası | "Stok Fiyat İşlemleri" bölümünden toplu ürün fiyat değişikliği yapılırken girilen fiyat koduna ait stokların listede kaçıncı sırada listelenmesi isteniyorsa, ilgili sıra numarasının girildiği alandır. **Örneğin:** Aynı fiyat koduna ait 100 adet stok kodu olduğu varsayıldığında; A malını kaydederken fiyat sırasına 5 girildiğinde, fiyat değişikliği listesinde A malı 5.sırada listelenir. |
| Stok Kartı Kayıtları Ekranı | Döviz Bilgileri Tanımlanan stokun farklı döviz birimleri ile alış/satış yapılmasını sağlayan alandır. |
| Alış Tipi | Dövizle takip edilecek stok kartlarında "Alış Tipi" alanına, "Döviz Takibi" modülünde yer alan "[Döviz İsimleri Tanımlama](<../../../../Genel/Döviz Takibi/Kayıt - Döviz Takibi/Döviz İsimleri Tanımlama.md>)" bölümündeki "Döviz Sıra Numarası" girilir. Döviz tiplerinin tanımlanması ile ilgili detaylı bilgi için; Genel → Döviz Takibi → Kayıt → Döviz İsimleri Tanımlama dokümanına bakılabilir. Özellikle dövizli alım yapan firmaların bu alanı boş bırakmaması gerekir. Döviz tipi girilmediğinde, fatura işlemleri yapılırken stokun dövizli çalışıp çalışmadığı, program tarafından bu alan üzerinden kontrol edilir. Boş bırakılırsa, stokla ilgili döviz fiyatı girilemez. Belirlenen döviz tipi, fatura kaydı sırasında kullanıcı tarafından değiştirilerek farklı bir döviz tipi ile alım yapılabilir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile tanımlanmış alış tipi kodlarına ulaşılır. |
| Alış Fiyatı | Kaydı oluşturulan stokun, döviz biriminden alış fiyatının girildiği alandır. Bu alana girilen döviz fiyatı fatura işlemi yapılırken anlık değiştirilebilir. Kullanıcı işlem sırasında döviz bilgisini silmek amacıyla TL kaydı da girebilir. |
| Maliyet | Kaydı oluşturulan stokun dövizli alışlarında, döviz birim fiyatına yansıyan (nakliye vb.) ve maliyetini etkileyen tutarı, döviz alış tipinde belirlenen para biriminden girilmesini sağlayan alandır. |
| Satış Tipi | Dövizle takip edilecek stok kartlarında "Satış Tipi" alanına, "Döviz Takibi" modülünde yer alan "Döviz İsimleri Tanımlama" bölümündeki "Döviz Sıra Numarası" girilir. Döviz tiplerinin tanımlanması ile ilgili detaylı bilgi için; Genel → Döviz Takibi → Kayıt → [Döviz İsimleri Tanımlama](<../../../../Genel/Döviz Takibi/Kayıt - Döviz Takibi/Döviz İsimleri Tanımlama.md>) Özellikle dövizli alım yapan firmaların bu alanı boş bırakmaması gerekir. Döviz tipi girilmediğinde, fatura işlemleri yapılırken stokun dövizli çalışıp çalışmadığı, program tarafından bu alan üzerinden kontrol edilir. Boş bırakılırsa, stokla ilgili döviz fiyatı girilemez. Belirlenen döviz tipi, fatura kaydı sırasında kullanıcı tarafından değiştirilerek farklı bir döviz tipi ile alım yapılabilir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile tanımlanmış satış tipi kodlarına ulaşılır. |
| Satış Fiyatı | Kaydı oluşturulan stokun, döviz biriminden satış fiyatının girildiği alandır. Bu alana girilen döviz fiyatı fatura işlemi yapılırken anlık değiştirilebilir. Kullanıcı işlem sırasında döviz bilgisini silmek amacıyla TL kaydı da girebilir. |

**Ek Bilgiler**

Stok Kartı Kayıtları ekranında Ek Bilgiler sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Stok Kartı Kayıtları Ekranı |  |
| --- | --- |
| Stok Kodu | Stok kodu ve isim bilgisinin program tarafından otomatik olarak aktarıldığı alandır. |
| Yok/Satış/Alış | İlgili stok için ÖTV (Özel Tüketim Vergisi) durumunun sorgulandığı alandır. İlgili stok için ÖTV uygulanmayacaksa "Yok", ÖTV uygulanacak stoklar satışta uygulanıyorsa "Satış", alışta uygulanıyorsa "Alış" seçeneği işaretlenir. |
| Oran/Tutar | ÖTV'nin oran/tutar üzerinden hesaplanması ile ilgili seçim yapılan alandır. |
| Tutar/Oran | Oran/Tutar alanında yapılan seçime göre, ÖTV hesaplanırken kullanılacak tutar ya da oranın girilmesi için kullanılır. Bir önceki alanda "Oran" seçildiğinde bu alana ÖTV oranı, "Tutar" seçildiğinde ise ÖTV tutarı girilir. |
| ÖTV Tevkifatına Tabi | ÖTV tevkifatı uygulanacak stoklar için kullanılan seçenektir. |
| Ek Bilgiler Ekranı | Puan Bilgileri Satıcı firmaların, müşterilere alım üzerinden puan hesaplatması ve puanlarına istinaden hediye vermesi ile ilgili işlemlerin takibinin yapıldığı bölümdür. |
| Birim Puan | Ürünün bir birimi için belirlenen puandır. Eğer bir ürünün satışı veya alımı sonucu puan verilecekse bu alan mutlaka doldurulur. Böylece, Fatura Modülünden bu ürün için yapılan satış ve alışlarda miktar \* puan değeri ile puan toplamı hesaplanır. |
| Puan Değeri | Hediye ürünler için kullanılan alandır. İlgili ürünün kaç puan karşılığında verileceği belirlenir. Bu üründen bir adet hediye verilmesi için, carinin en az bu değer kadar puanının olması gerekir. Puan uygulamasının işleyişi ve programda yapılması gereken tanımlarla ilgili bilgi için; Stok → [Ek-1 (Puan Uygulaması)](<../../Ekler (Stok)/Ek-1 (Puan Uygulaması).md>) dokümanına bakılabilir. |
| Hacim Kodu | "Dinamik Depo" uygulamasında yerleştirilecek ve toplanacak ürünleri, hacim bazında gruplamak ve aynı hacme sahip ürünlerin hepsini ayrı ayrı tanımlamaktansa bir grup kodu ile birleştirmek için hacim kodları tanımlanır. "Dinamik Depo" uygulaması kullanılıyorsa, hacim kodları stok kartlarındaki hacim kodu alanına girilir. Alanın sağ tarafında yer alan aşağı ok veya rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, hacim kodları arasından seçim yapılır. |
| Tartı ürünü | Özellikle marketlerde kullanılan elektronik terazilere Logo Netsis ile stok bilgilerinin gönderildiği durumlarda, teraziye gönderilecek stoklar için işaretlenmesi gereken seçenektir. Aksi halde ürünler Text dosyaya gönderilmez. |
| Fiktif Mamul | Üretim Modülünü kullanan firmaların, uygulamalarına yönelik işaretlemeleri gereken seçenektir. Fiktif mamul olarak kaydedilen stok, sadece reçete kayıtları için kullanılır. Bu stok, reçete kayıtları sırasında reçetesi tanımlanan mamul olarak girilir. Üretim sonucu, fiktif mamul için herhangi bir giriş veya çıkış hareketi oluşmaz. Fiktif Mamul Uygulaması ile ilgili detaylı bilgi için; Üretim → Ek-1 (Fiktif Mamul Uygulaması) |
| Gümrük Tarife Kodu | Özellikle serbest bölgede faaliyet veren firmaların, rapor amaçlı kullandıkları alandır. Her stoka ait "Gümrük Tarife Kodu" ilgili alana kaydedildikten sonra, "Serbest Raporlar" kullanılarak listelenebilir. Serbest raporların kullanımı ile ilgili detaylı bilgi için bakınız Genel → Rapor → Raporlar → Serbest Rapor dokümanına bakılabilir. |
| Dağıtıcı Kodu | Rapor amaçlı kullanılan alandır. |
| Ek Bilgiler Ekranı | Maliyet Bilgileri |
| Türü | Maliyet Muhasebesi Modülünde kullanılmak üzere, maliyet hesaplamaları için belirleyici olarak kullanılan alandır. Mamul, yarı mamul ve yan ürün seçeneği girilen stok kodları için "Mamul Grup Kodunun" mutlaka tanımlanması gerekir. Maliyet raporlarında stok kodunun türüne göre rapor alınacağı için bu alanın tanımlanmış olması gerekir. |
| Mamul Grup | Maliyet Muhasebesi Modülü kullananlar için, bu bölümde tanımlanan maliyet grup kodunun girildiği alandır. Maliyet gruplarının maliyet hesaplamalarında bu alanlar program tarafından kontrol edilir. Alanın boş bırakılması halinde bu stok kodu herhangi bir maliyet grubuna eklenmeyeceği için maliyet hesaplamalarına dahil edilmez. Maliyet Muhasebesi Modülünde tanımlanan maliyet grup kodları, rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile seçilir. Maliyet grup kodlarının tanımlanması ile ilgili detaylı bilgi için; Muhasebe → Maliyet Muhasebesi → Kayıt → [Mamul Grup Kodu Kayıtları](<../../../../Muhasebe/Maliyet Muhasebesi/Kayıt - Maliyet Muhasebesi/Mamul Grup Kodu Kayıtları.md>) dokümanına bakılabilir. |
| Ek Bilgiler Ekranı | **Reçete Bilgileri** |
| Mamul | Üretim Modülünde reçetesi olan mamullerde işaretli olarak gelen alandır. |
| Eski Reçete | Üretim Modülünde daha önceden reçetesi bulunan stoklarda işaretli olarak gelen alandır. |
| Bileşen | Üretim Modülünden kaydedilen bir reçetede bileşen olarak kullanılan stoklarda işaretli olarak gelen alandır. |
| Ek Bilgiler Ekranı | **Ambar Giriş/Çıkış** |
| Çıkış Yeri/Masraf Merkezi | Ambar Giriş/Çıkış işlemlerinde kullanılmak üzere Çıkış Yeri ve Masraf Merkezi bilgilerinin girildiği alandır. Stok kartında girilen bu bilgiler, Ambar Giriş/Çıkış fişlerinin "Kalem Bilgileri" sekmesinde yer alan "Ek Açıklama" alanına otomatik olarak gelir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile çıkış yeri ve masraf merkezi seçilir. |
| Ek Bilgiler Ekranı | **Esnek Yapılandırma Bilgileri** |
| Esnek Yapılandır | Tanımlanan stokun birden fazla özelliği bulunduğunda, bu özellikler bazında takibinin sağlanması için işaretlenmesi gereken seçenektir. Alanın stok kartında sorgulanması için "Esnek Yapılandırma Uygulamasının" yüklü olması ve "[Stok Parametreleri](<../Stok Parametreleri.md>)" bölümünde bulunan "Esnek Yapılandırma" parametresinin işaretli olması gerekir. |
| Süper Reçete Kullanılsın | Esnek yapılandırma uygulamasının kullanıldığı durumlarda, farklı özelliklere sahip ürün için tek bir reçete tanımlanır ve daha sonra ürün özelliği bazında reçetelerin program tarafından oluşturulması sağlanır. Tanımlanan ürünün farklı özellikleri için gerekli reçetelerin program tarafından oluşturulması istendiğinde "Süper Reçete Kullanılsın" seçeneğinin işaretlenmesi gerekir. Bu seçenek "Esnek Yapılandır" seçeneği işaretlendiği zaman aktif hale gelir. Özellik bazındaki reçetelerin program tarafından oluşturulması ile ilgili detaylı bilgi için; Üretim → Kayıt → Süper Reçete Kayıtları dokümanına bakılabilir. |
| Bağlı Stok Kodu | Esnek yapılandırma uygulamasının kullanıldığı durumlarda bağlı stok kodunun girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile stok kodları arasından seçim yapılır. |
| Yapılandırma Kodu | Esnek yapılandırma uygulamasının kullanıldığı durumlarda yapılandırma kodunun girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile kodlar arasından seçim yapılabilir veya "Yapılandırma Kodu" yazısının üzerine çift tıklandığında açılan ekran sayesinde "Ürün Yapılandırma" tanımlaması yapılabilir. ![](../../../../../_assets/a949e0b3f3325e7ac771.png) |
| Stok Mevzuat Tipi | İlgili stok kartının kullanılacağı binek oto senaryosu tipinin seçildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile tipler arasından seçim yapılır. |

**Tutar/Miktar Bilgileri**

Stok Kartı Kayıtları ekranında Tutar/Miktar Bilgileri sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Tutar/Miktar Bilgileri Ekranı |  |
| --- | --- |
| Stok Kodu | Stok kodu ve isim bilgisinin program tarafından otomatik olarak aktarıldığı alandır. |
| **![](../../../../../_assets/7dde24912d3c19496de5.png)**Stok Aylık İcmal | "Raporlar" menüsünde bulunan "Stok Aylık İcmal" raporuna ait kısa yol butonudur. İlgili stoka ait aylık giriş/çıkış bilgilerine ait rapor alınmasını sağlar. "Stok Aylık İcmal" raporu ile ilgili detaylı bilgi için; Stok → Raporlar → [Stok Aylık İcmal](<../../Raporlar - Stok/Stok Aylık İcmal.md>) dokümanına bakılabilir. |
| **![](../../../../../_assets/1cd2cc7a64c87d7f40a2.png)**Stok Hareket İcmali | "Raporlar" menüsünde bulunan "Stok Hareket İcmali" raporuna ait kısa yol butonudur. İlgili stoka ait aylık giriş/çıkış bilgilerine ait rapor alınmasını sağlar. "Stok Hareket İcmal" raporu ile ilgili detaylı bilgi için; Stok → Raporlar → [Stok Hareket İcmali](<../../Raporlar - Stok/Stok Hareket İcmali.md>) dokümanına bakılabilir. |
| Giriş Miktarı | İlgili stok kartının tüm giriş hareketlerine ait toplam miktarın izlendiği alandır. |
| Çıkış Miktarı | İlgili stok kartının tüm çıkış hareketlerine ait toplam miktarın izlendiği alandır. |
| Bakiye | İlgili stok kartının anlık bakiye miktarının izlendiği alandır. |
| Giriş Tutarı | İlgili stok kartının tüm giriş hareketlerine ait toplam tutarın izlendiği alandır. |
| Çıkış Tutarı | İlgili stok kartının tüm çıkış hareketlerine ait toplam tutarın izlendiği alandır. |
| Son Net Fiyat | Alış faturasında son girilen net fiyat bilgisinin izlendiği alandır. |
| Son Brüt Fiyat | Alış faturasında son girilen brüt fiyat bilgisinin izlendiği alandır. |
| Yoldaki Miktar | İthalat/İhracat tipli alış ve satış irsaliyesi ile giriş/çıkış yapılan stokun, bu tip irsaliyelerde işlem gören miktarının ("İthalat/İhracat Kapatma işlemi" yapılmadan önce) izlendiği alandır. |
| Birim Maliyet | Stok → İşlemler → "[Ürün Malzeme Maliyetleri Oluşturma](<../../İşlemler - Stok/Ürün Malzeme Maliyetleri Oluşturma.md>)" bölümünden maliyet oluşturulduktan sonra, stok için hesaplanan birim maliyet tutarının izlendiği alandır. Bu alan, Maliyet Muhasebesi Modülünün kullanıldığı durumlarda maliyet oluşturma işleminden sonra atanır. Kullanıcının kayıt ve değişiklik yapma hakkı yoktur. |
| Dövizli Birim Maliyet | Muhasebe → Kayıt → [Muhasebe Parametreleri](<../../../../Muhasebe/Muhasebe Modülü/Kayıt - Muhasebe/Muhasebe Parametreleri.md>) → Dövizli Muhasebe → "FAS52" seçeneğinin işaretlendiği durumlarda dövizli birim maliyet bilgisinin aktarıldığı alandır. Öncelikle Stok → İşlemler → "[Stok Döviz Çevrim](<../../İşlemler - Stok/Stok Döviz Çevrim.md>)" işleminin çalıştırılarak firma döviz tutarlarının oluşturulması gerekir. Daha sonra Stok → İşlemler → "[Ürün Malzeme Maliyetleri Oluşturma](<../../İşlemler - Stok/Ürün Malzeme Maliyetleri Oluşturma.md>)" işlemi çalıştırıldığında, stok kaydı için döviz cinsinden birim maliyet tutarı hesaplanır. Kullanıcının kayıt ve değişiklik yapma hakkı yoktur. |
| Tutar/Miktar Bilgileri Ekranı | Müşteri |
| Ayrılmış Stok | Fatura → Kayıt → Satış Parametreleri → “Siparişte Stoktan Ayırma Yapılsın” parametresinin işaretlendiği durumlarda ayrılmış stok bilgisinin aktarıldığı alandır. Parametre işaretlendiğinde, girilen müşteri siparişleri direkt stoktan ayrılır. |
| Toplam Sipariş | Bugüne kadar alınan toplam müşteri siparişlerinin izlendiği alandır. |
| Toplam Teslim | Bugüne kadar teslim edilen toplam sipariş miktarlarının izlendiği alandır. |
| Sipariş Bakiyesi | Kalan müşteri sipariş miktarlarının izlendiği alandır. |
| Tutar/Miktar Bilgileri Ekranı | Satıcı |
| Toplam Sipariş | Bugüne kadar verilen toplam satıcı siparişlerinin izlendiği alandır. |
| Toplam Teslim | Bugüne kadar teslim alınan toplam sipariş miktarlarının izlendiği alandır. |
| Bakiye | Kalan satıcı sipariş miktarlarının izlendiği alandır. |

**Kullanıcı Tanımlı Sahalar**

Kullanıcı Tanımlı Sahalar sekmesi, rapor amaçlı bilgi girişi yapılması için kullanılan sekmedir.

Kullanıcı Tanımlı Sahalar sekmesinin ekranda yer alması için; Stok → Kayıt → Stok Parametreleri → Kullanıcı Tanımlı Sahalar sekmesinde saha başlık tanımlamalarının yapılması gerekir.

Stok Kartı Kayıtları ekranında Kullanıcı Tanımlı Sahalar sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Kullanıcı Tanımlı Sahalar Ekranı |  |
| --- | --- |
| Stok Kodu | Stok kodu ve isim bilgisinin program tarafından otomatik olarak aktarıldığı alandır. |
| Alfa Sayısal Sahalar | Stok sabit kayıtlar için, ek bilgi alanı olarak rapor amaçlı kullanılmak üzere 8 adet, 25 karakter uzunluğunda alfa sayısal değer girilen alandır. Bu alanlara bilgi girişi yapılması için öncelikle, Stok → Kayıt → [Stok Parametreleri](<../Stok Parametreleri.md>) → Kullanıcı Tanımlı Sahalar sekmesinden başlık bilgisi girilir. Aksi takdirde alanlar pasif hale gelir. Girilen bilgiler, Stok → Raporlar → Stok Raporları bölümündeki Stok Sabit, Bakiye ve Hareket listelerinden raporlanır. |
| Sayısal Sahalar | Stok sabit kayıtlar için, ek bilgi alanı olarak rapor amaçlı kullanılmak üzere 8 adet, 25 karakter uzunluğunda sayısal değer girilen alandır. Bu alanlara bilgi girişi yapılması için öncelikle, Stok → Kayıt → [Stok Parametreleri](<../Stok Parametreleri.md>) → Kullanıcı Tanımlı Sahalar sekmesinden başlık bilgisi girilir. Aksi takdirde alanlar pasif hale gelir. Girilen bilgiler, Stok → Raporlar → Stok Raporları bölümündeki Stok Sabit, Bakiye ve Hareket listelerinden raporlanır. |

**Stok Bilgisi**

Stok Bilgisi sekmesi, ilgili stok kartına ait serbest bilgi girişi yapılması için kullanılan sekmedir.

**Lokal Depo Bakiye Bilgisi**

Lokal Depo Bakiye Bilgisi sekmesi, lokal depo uygulaması yapan firmaların, lokal depo bazında toplam giriş/çıkış miktar ve bakiyelerinin izlendiği sekmedir.

**Seri Takibi**

Seri Takibi sekmesi, Yardımcı Programlar → Kayıt → [Şirket - Şube Parametre Tanımları](<../../../../Genel/Yardımcı Programlar/Kayıt - Yardımcı Programlar/Şirket - Şube - Parametre Tanımları.md>) →“Seri Takibi Var" parametresinin işaretlenmesi ile ekrana gelir.

Stok Kartı Kayıtları ekranı Seri Takibi sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Seri Takibi Ekranı |  |
| --- | --- |
| Stok Kodu | Stok kodu ve isim bilgisinin program tarafından otomatik olarak aktarıldığı alandır. |
| Girişlerde Seri No Takibi Yapılacak Mı? | Stok Hareket Kayıtlarına manuel (elle) "Üretim" veya "Fatura" modülünden yapılacak girişlerde, seri numarası takibinin yapılıp yapılmayacağını sorgulayan seçenektir. İşaretlenmesi durumunda, stok hareketlerine yapılacak giriş hareketlerinde seri ekranı açılır ve seri numarası sorgulanır. |
| Çıkışlarda Seri No Takibi Yapılacak Mı? | Stok Hareket Kayıtlarına manuel (elle) "Üretim" veya "Fatura" modülünden yapılacak girişlerde, seri numarası takibinin yapılıp yapılmayacağını sorgulayan seçenektir. İşaretlenmesi durumunda, stok hareketlerine yapılacak çıkış hareketlerinde seri ekranı açılır ve seri numarası sorgulanır. |
| Bakiye Kontrolü Yapılacak Mı? | Çıkış işlemleri için kullanılan seçenektir. İşaretlenmesi durumunda, çıkılan seri numarasının girişinin olup olmadığı ve bakiyesi kontrol edilir. Girilmemiş bir seri veya ilgili serinin bakiyesinden fazla çıkış yapılıyorsa program uyarı vererek çıkış işlemine izin vermez. İşaretlenmemesi durumunda, çıkılan seri numarasının girişinin olup olmadığı ve bakiyesi kontrol edilmediği için, daha önce girilmemiş bir seri veya bakiye miktarından fazla çıkış yapılabilir. Bu seçenek işaretlendiğinde, “Seri Kodu Çıkışlar İçin Otomatik Hesaplansın” seçeneği pasif hale gelir. |
| Miktar Kadar Seri Sorulsun Mu? | Giriş ve çıkış işlemlerinde yazılan miktar kadar seri numarası sorgulanmasını sağlayan seçenektir. Bu parametrenin işaretli olduğu durumlarda, bir stok için 5 adet çıkış yapılacaksa, seri ekranında 5 adet seri satırı açılır ve 5 seri numarası girildikten sonra, seri ekranı otomatik olarak kapanır. Giriş veya çıkışlarda otomatik seri hesaplatılıyorsa, girilen miktar kadar seri otomatik hesaplanır. “Miktar Kadar Seri Sorulsun Mu” seçeneği kullanıldığında, giriş ve çıkış işlemleri sırasında seri ekranındaki "Miktar" alanına müdahale edilmez. Toplam girilen miktar kadar seri girişi yapılacağı düşünülerek, her bir birim için bir seri numarası girilmesi beklenir. Genel miktar girişi tamamlandığında seri ekranı otomatik olarak kapanır. Seçeneğin işaretli olduğu durumlarda, miktar için 5 girilip seri ekranındaki miktara 3, bir diğer seri numarası miktarına da 2 girilemez. Tek tek 5 adet seri numarası girilmesi gerekir. Bu nedenle tartılan, kg ile alınıp satılan ve her seri için ağırlığı o anda belli olmayan ürünlerde bu seçeneğin işaretlenmemesi gerekir. |
| Seri Kodu Girişler İçin Otomatik Hesaplansın | Stok → Kayıt → Seri Takibi → [Seri Parametreleri](<../Seri Takibi/Seri Parametreleri.md>) → "Seri Kodu Girişleri İçin Otomatik Hesaplansın" parametresi işaretli değilse, stok kartlarında sorgulanan bu seçeneğin işlevi yoktur. Seri Parametrelerinde bu parametre işaretli ise, bazı kartlarda otomatik hesaplama yapılacağı gibi, bazılarında da bu parametre işaretlenmeyerek manuel (elle) seri girişi yapılır. Her iki parametrenin de işaretlenmesi durumunda, “Miktar Kadar Seri Sorulsun” seçeneğine bağlı olarak seri numaraları otomatik hesaplanır. “Miktar Kadar Seri Sorulsun” seçeneği işaretlenmişse, girilen miktar kadar farklı seri otomatik hesaplanır. İşaretli değilse, girilen toplam miktar için 1adet seri numarası otomatik hesaplanır. |
| Seri Kodu Çıkışlar İçin Otomatik Hesaplansın | Stok → Kayıt → Seri Takibi → [Seri Parametreleri](<../Seri Takibi/Seri Parametreleri.md>) → "Seri Kodu Girişleri İçin Otomatik Hesaplansın" parametresi işaretli değilse, stok kartlarında sorgulanan bu seçeneğin işlevi yoktur. Seri Parametrelerinde bu parametre işaretli ise, bazı kartlarda otomatik hesaplama yapılacağı gibi, bazılarında da bu parametre işaretlenmeyerek manuel (elle) seri çıkışı yapılır. Her iki parametrenin de işaretlenmesi durumunda, “Miktar Kadar Seri Sorulsun” seçeneğine bağlı olarak seri numaraları otomatik hesaplanır. “Miktar Kadar Seri Sorulsun” seçeneği işaretlenmişse, girilen miktar kadar farklı seri otomatik hesaplanır. İşaretli değilse, girilen toplam miktar için 1adet seri numarası otomatik hesaplanır. |
| Farklı Serilerden İşlem Yapılsın | Bir mal kalemi için birden fazla farklı seri takibi yapılacağı durumlarda işaretlenmesi gereken seçenektir. Bu durumda, giriş ve çıkış işlemlerinde seri numarasının başına eklenecek 2 karakterlik seri kodu başlangıcı sorgulanır. Bir mal için hem "Farklı Serilerden İşlem" yapılır hem de "Çıkışlarda Seri Kodu Otomatik Hesaplatılır" ise, giriş ve çıkış işlemlerinde seri kodu başlangıcı olarak, son seri numarasından bir fazlası otomatik olarak ekrana getirilir. |
| Seri Kodu İçin Başlangıç Değer | Stok giriş ve/veya çıkış işlemlerinde seri numarası otomatik hesaplandığında kullanılan seçenektir. Seri numaralarının başında, baz alınması istenen değerin girilmesi gerekir. **Örnek** "A" değerinin girildiği varsayıldığında aşağıdaki durumlar gerçekleşir: - İlgili stok kartı için seri numarası "A" ile başlar. Seri Parametrelerinde "Stok Kodu Başlangıç Değer Kabul Edilsin” parametresinin işaretlendiği durumlarda, stok kodu seri numarasının başlangıcı kabul edilir ve hemen yanına bu alana girilen değer aktarılır.<br>- Stok kodu "CEPTEL" olan bir ürün için bu alana "A" değeri girilmiş ve ilgili parametre işaretlenmişse, seri numarası başlangıcı "CEPTELA" olarak kaydolur ve diğer seri parametreleri göz önüne alınarak seri numarası tamamlanır.<br>- Hem “Farklı Serilerden İşlem Yapılsın” parametresi işaretli hem de seri kodu başlangıç değeri girilmişse, başlangıç değeri otomatik olarak ekrana getirilir fakat kullanıcı istediğinde farklı bir seri de girebilir. |

**Fiyat Bilgileri**

Fiyat Bilgileri, fiyat listesi takibi yapan firmaların, ilgili stok kartına ait güncel fiyat listelerini izlemelerini sağlayan sekmedir. Fiyat Bilgileri sekmesinde, sadece içinde bulunan tarihi kapsayacak şekilde tanımlanan fiyat listeleri izlenir.

Fiyat listelerinin tanımlanması ile ilgili detaylı bilgi için; Stok → Kayıt → [Stok Fiyat İşlemleri](<../Stok Fiyat İşlemleri/index.md>) dokümanına bakılabilir.

Stok Kartı Kayıtları ekranı Fiyat Bilgileri sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Stok Kartı Kayıtları Ekranı |  |
| --- | --- |
| Stok Kodu | Fiyat bilgisi izlenecek stok kodunun izlendiği alandır. |
| Yapılandırmalı Fiyatları Göster | Esnek yapılandırmalı stoklarda aktif ve görünür hale gelen seçenektir. İşaretlendiğinde - stok koduna ait esnek yapılandırmada özel fiyat tanımlandıysa - belge girerken gelecek fiyatların listelenmesi sağlanır. |

**Reçete Bilgileri**

Reçete Bilgileri sekmede bulunan bilgiler sayesinde, ilgili stokun (üretim reçetelerinde) mamul, yarı mamul, bileşen çeşitlerinden hangisi için kullanıldığı izlenir. "MAMULMÜ" alanında "E" yazması stoka ait bir reçetenin bulunduğu, "BİLEŞENMİ" alanında "E" yazması ise stokun reçetede bileşen olarak kullanıldığı anlamına gelir. Her iki alanda da "E" yazıyor ise, ilgili stokun yarı mamul olduğu anlaşılır. Reçete toplamı, stokun bulunduğu reçetenin toplamını gösterir.

"Reçete Toplamı" ile ilgili detaylı bilgi için; Üretim → Kayıt → Reçete Kaydı dokümanına bakılabilir.

Esnek yapılandırma uygulamasının kullanıldığı durumlarda, stokların sahip olduğu farklı özellikler bazında reçete bilgileri olacağı için, bu sekmedeki reçete bilgileri yapılandırma kodu bazında gösterilir.

**Döviz Bilgileri**

Döviz Bilgileri, stokların döviz tipleri bazında hareket gördüğü net fiyatlar üzerinden, toplam giriş/çıkış tutarları ve döviz bakiyesinin izlendiği sekmedir.

**Stok Kartının Kaydedilmesi ve İptali**

Bilgileri girilen stoklara ait kartların kaydedilmesi için, ekranın sol üst köşesinde bulunan kaydet butonu ![](../../../../../_assets/865524a70e225c89c107.jpg), ya da klavyedeki F5 tuşu kullanılır. Tanımlı stok kartını iptal etmek için de, ekranın sol üst köşesinde bulunan kayıt sil butonu ![](../../../../../_assets/2df4b343310bcd16b01e.jpg), ya da klavyedeki F7 tuşu kullanılır. Ancak, tanımlı stok kodunun daha önce herhangi bir kayıt işleminde kullanılması halinde, stok kartının iptali için öncelikle kullanıldığı kayıt bilgisinin iptal edilmesi gerekir.

**Örneğin:** Tanımlanan stok için satış faturası kaydedildiğinde, stok kartının silinmesi için öncelikle stokun kullanıldığı satış faturasının silinmesi gerekir.
