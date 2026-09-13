---
title: "e-Defter Uygulamasında Dikkat Edilecek Hususlar"
page_id: "50684698"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "e-Defter Uygulamasında Dikkat Edilecek Hususlar"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / e-Defter Uygulamasında Dikkat Edilecek Hususlar"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTIzOGZkMmE0LTQ3Y2EtNGQ5NC05NmIyLWFiZWMzMDNjNzc5MSZsaW5rPWNjMjE0NmI4LTJjZDgtNDBmZS1hOGViLTVhYTBmYjk1OWQ3MCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=238fd2a4-47ca-4d94-96b2-abec303c7791&link=cc2146b8-2cd8-40fe-a8eb-5aa0fb959d70&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "e-defter-uygulamasinda-dikkat-edilecek-hususlar_90669850_50684698.html"
source_version: "2022-11-03T09:56:02.020+03:00"
source_bytes: 2048605
fetched_at: "2026-09-13T04:26:31+00:00"
generator: "netsis-scraper 1.0.0"
---
# e-Defter Uygulamasında Dikkat Edilecek Hususlar

e-Defter Uygulamasında Dikkat Edilecek Hususlar ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

e-Defter uygulamasında dikkat edilmesi gereken bazı hususlar vardır. Bunlarında başında mükellef ve düzenleyen bilgilerinin eksiksiz ve doğru doldurulması gelir. Bu bölümde nasıl doldurulacağı konusunda yoğun soru gelen sahalar açıklanmaktadır.

**Mükellef ve Düzenleyen Bilgileri:** e-Defter için oluşturulacak olan XML dosyasında gerekli olan, mükellef bilgileri, düzenleyen bilgileri ve YMM bilgilerinin girişi için Muhasebe / Kayıt / Mükellef ve Düzenleyen Bilgileri ekranı kullanılmalıdır.

**İdari Ve Mükellef Bilgileri** ekranından işletmenin detay bilgileri girilmelidir.

![](../_assets/5a382a98d31ec71e825f.png)

**Unvan:** Firmaların unvan bilgisi, ticaret sicil gazetesinde yer aldığı biçimde kısaltma yapılmaksızın eksiksiz biçimde girilmelidir.

**Faaliyet Kodu** alanına işletmenin faaliyet konusunu gösteren "NACE" kodu yazılmalıdır. [http://tuikapp.tuik.gov.tr/DIESS/SiniflamaSurumListeAction.do?turId=1](http://tuikapp.tuik.gov.tr/DIESS/SiniflamaSurumListeAction.do?turId=1)linkinden faaliyet koduna ilişkin detaylı bilgi edinilebilir.

**Vergi** **Kimlik** **No** – **T.C.** **Kimlik** **No:** Kurum tipi tüzel ise vergi kimlik numarası 10 karakter olarak, kurum tipi gerçek ise TC kimlik numarası 11 karakter olarak tanımlanmış olmalıdır. Bu sahalardan sadece biri dolu olmalıdır. Girilen kimlik numarası e- Defter sipariş aşamasında belirtilen kimlik numarası ile aynı olmalıdır.

**Defter Bilgileri** ekranından deftere ait dönem, şubeli defter oluşturulacaksa şube bilgileri gibi oluşacak deftere ait detaylar girilmelidir.

![](../_assets/3908e9126d39686d8e07.png)

**Dönem Başlangıç – Bitiş:** Mali hesap dönemi başlangıç ve bitiş tarihi yazılmalıdır.

**Şube No / Şube Adı:** Şube bazında defterlerin ayrı tutulması halinde, defter isimlerinin şube bilgisini içerecek şekilde oluşabilmesi için defter şube bilgileri doldurulmalıdır. e-Defterde "0" şube kodu olarak kullanılamadığı için Netsis'te takip edilen şube kodundan farklı olarak bu ekranda e-Defter için ayrıca şube kodu/ünvanı bilgisi girilmelidir.

Her şube kendi içerisinde e-Defter standardına uygun oluşturulmalıdır. Şube bazlı defter tutulması durumunda bir şube için oluşturulan defterlerde kullanılan "şube no" hesap dönemi (Özel hesap dönemi dahil) boyunca aynı olmalı ve aylık dönemlere ait defterlerde değiştirilmemelidir.

Şube'nin hesap dönemi içinde kapanmış olması durumunda, kapanan şubeye ait kapanış tarihinden sonraki dönemler için GİB'e herhangi bir berat gönderilmeyecektir.

Ticaret Sicilde şube adı değişikliği olursa defter tanımlarında da bu değişiklik yapılabilir. e-Defter kullanıcılarının dikkat etmesi gereken şube'nin adının değiştirilmesi durumunda, bu şubeye ait berat GİB'e iletilmeden önce Ticaret Sicil gazetesinin ekinde olduğu bir dilekçe ile durum GİB'e bildirilmelidir.

**Mali** **dönem** **başlangıcı** **farklı** **olduğunda** **e-Defter** **periyot** **başlangıç** **günü** **ay** **başı** **yapılsın:** Defter kayıtlarının ay ortasından başladığı tasfiye gibi durumlarda verilen defterin periyot başlangıcının ay başı olması için işaretlenmesi gereken parametredir.

**e-Defter oluşturulan aya ait belgelerde değişiklik yapılmasın:** Defter verilen ayda veri bütünlüğünün korunabilmesi için muhasebe kayıtlarında ve kaynak belgelerde değişiklik yapılmaması gerekmektedir. Bu parametre ile defteri verilen kayıtlar üzerinde değişiklik engellenmektedir.

**HSV Bilgileri:** Defterin hangi sıfatla verildiğinin belirlendiği ekrandır. Defteri mükellef veriyorsa HSV tipi mükellef seçilip mükellef bilgileri, kanuni temsilci veriyorsa kanuni temsilciye ait bilgiler girilmelidir.

![](../_assets/50b62fee55c08ddacc4a.png)

**Sözleşme Açıklaması:** SM/SMMM veya YMM bir işletme için defter oluşturuyorsa, bu durumda SM/SMMM veya YMM ile yapılan sözleşmeye ait Sözleşme açıklaması, Sözleşme çeşidi, Sözleşme tarihi ve numarası yazılmalıdır. Eğer defterler işletme bünyesinde tutuluyorsa bu alana tire işareti yazılarak geçilebilir. Çünkü Sözleşme Tipi Açıklaması, şematron kontrollerine göre boş geçilmemesi gereken bir alandır.

**Düzenleyen Bilgileri:** Düzenleyen tipinin belirlendiği ekrandır. Serbest Muhasebeci, Serbest Muhasebeci Mali Müşavir, Yeminli Mali Müşavir, Mükellef ve Kanuni Temsilci seçenekleri arasından defteri düzenleyene göre seçim yapılır ve yapılan seçime ait detay tanımlamalar girilir.

![](../_assets/726e30fe565074c079e1.png)

Tam Tasdik Düzenleyen Bilgileri linki ile Tam Tasdik Düzenleyen Bilgileri ekranına ulaşılıp raporu düzenleyen SM, SMMM ve YMM bilgilerinin kaydedilmesi sağlanır.

![](../_assets/c2293baddc4889b130b3.png)

**Gönderen ve YMM Bilgileri:** Defteri düzenleyenin dışında gönderen ve YMM bilgilerinin girilebildiği ekrandır.

![](../_assets/5435b2480a63219415d8.png)

**Belge Tipi:** Muhasebe kaydına esas teşkil eden işlem bir belgeye dayanıyorsa, mutlaka **belge** **tipi** alanının kullanılması gerekmektedir. Ancak muhasebe kaydına esas teşkil eden işlem bir belgeye dayanmıyorsa belge tipi alanı kullanılmamalıdır. Dolayısıyla muhasebe kaydına esas teşkil eden işlem bir belgeye dayanmıyorsa, belge türü, tarihi veya numarası gibi bilgiler verilemez. Örneğin, açılış-kapanış işlemleri belgeye dayalı olmayabilir.

Gelir İdaresi Başkanlığının yayımlandığı Yevmiye Defteri kılavuzunda aşağıdaki sekiz belge tipi tanımlanmıştır. Tabloda sayılan yedi belge tipinin dışında ki belgeler için "Diğer" belge türü kullanılır.

|  | **Belge** **Tipi** | **Esas** **Belge** |
| --- | --- | --- |
| **1** | Invoice | Fatura |
| **2** | Check | Çek |
| **3** | Voucher | Senet |
| **4** | Receipt | Makbuz |
| **5** | Other | Diğer |
| **6** | Shipment | Navlun |
| **7** | Order-vendor | Satıcı Siparişi Belgesi |
| **8** | Order-customer | Müşteri Siparişi Belgesi |

Muhasebe kaydına esas teşkil eden işlem tabloda sayılan belge tiplerinden birine dayanıyorsa, bu durumda belge tipi tanımlaması bu tablo da belirtildiği şekilde yapılmaktadır. Örneğin fatura girişlerinde kullanılması gereken belge tipi "invoice" olacaktır. Ancak Fatura yerine geçen belgeler için "invoice" belge tipi kullanılamaz. Örneğin Serbest meslek makbuzu, fatura yerine geçen bir belge olmasına rağmen, elektronik defterde "invoice" olarak değil; "other" belge tipinde gösterilmelidir. Açıklama kısmında ise "serbest meslek makbuzu" olarak tanımlanmalıdır.

Tabloda sayılan ilk yedi belge tipinin dışındaki muhasebe kaydına esas teşkil eden belgeler için Netsis'te e- defter oluşturulurken, bu belgeler için "other" belge tipi otomatik olarak doldurulur ve fişlerin girilmiş olan belge türleri açıklama olarak getirilir. Örneğin, dekont ekranında girilen bir virman işleminde belge türüne "Dekont" girilmiş olsun, bu durumda e-defter oluştuğunda belge tipi "other", açıklama alanı ise "Dekont" olarak gelecektir. Böylece kullanıcıların fazladan giriş yapmamalarını sağlayarak kayıt girişinin hızlanması hedeflenmiştir.

Belge açıklama alanı, e-Defter xml alanlarında "documenttypedescription" alanına karşılık gelmektedir. Bu alan serbest metin olarak giriş yapılan bir alandır. Ancak belge açıklama alanına yapılan işlemin adı değil, doğrudan kayda esas belgenin adı yazılmalıdır. Örneğin, ücret bordrosu, teminat mektubu, sigorta poliçesi, dekont vb. bilgiler girilebilir. Ancak havale, eft, ödeme vb. işlem adları kayda esas belge olarak belge tipi alanına yazılmamalıdır.

Belge numarası ve Belge tarihi, elektronik defter xml'inde sırasıyla documentnumber ve documentdate alanlarına karşılık gelmektedir. Bu elemanlar yevmiye maddesine kaynak teşkil eden belgenin numarasını ve tarihini gösteren elemanlardır. Dolayısıyla yevmiye kaydına ait tarih ve numara ile belgeye ait numara ve tarih farklı olabilir. Kayda esas belgenin üzerinde kendine ait numara ve tarih var ise, belge numarası ve belge tarihi alanlarına belge üzerindeki bilgiler yazılmalı, bu bilgiler yerine muhasebe fişinin tarihi ve numarası yazılmamalıdır.

**Banka İşlemleri:** Bilindiği üzere bankaya ait işlemlerde muhasebe kaydına esas belge bankadan verilen **dekont** olmaktadır. Netsis'te yapılan havale, eft vb. banka modülünden oluşan muhasebe fişleri için e- defter oluştuğunda, belge tipi "other" ve belge açıklaması "dekont" olarak görülecektir. Eğer banka modülü kullanılmadan dekont/muhasebe modülünden kayıtlar yapılıyorsa bu durumda ekrandaki belge tipi açıklamasına "dekont" girilmelidir. Ayrıca dekont üzerinde belge numarası-tarihi ise, belge numarası ve tarihi olarak yazılmalıdır.

Eğer bankaya ait işlemler dekont bazında tek tek muhasebeleştirilemiyorsa, bu banka işlemleri günlük olarak, banka banka ayrıştırmak koşuluyla, her bir bankadan yapılan işlemler birer muhasebe fişinde işlenebilir. e-Defterde bu kayda esas belge olarak muhasebe fişi gösterilebilir. Netsis'e kaydedilen bu durumdaki muhasebe fişinin belge tipi açıklaması "**Muhasebe** **Fişi**" olarak kaydı yapılabilir ve fişin numarası ve tarihi girilir.

**Masraf listeleri**: Gün içinde işletmenin ya da personelin yapmış olduğu giderlere ilişkin alınmış belgeler teknik kılavuzlarda sayılan belgelerden biriyse mutlaka belge tipi kılavuzda belirtildiği gibi olmalıdır. Örneğin, personelin yapmış olduğu giderler arasında belge olarak fatura varsa, bu fatura mutlaka fatura olarak kayıt yapılabilen Netsis ekranlarından girilmelidir.

Eğer yapılan giderle ilgili belge tipi, yukarıdaki tabloda sayılan ilk yedi belge tipinden biri değil ise bir masraf formu oluşturulup, dekont modülünden belge tipi açıklaması "**masraf formu**" olarak kaydı yapılabilir. Ayrıca bu masraf formunun numarası ve tarihinin de girilmesi zorunludur. Bu masraf formlarında matbu bir numara ve tarih olmadığı için, oluşturulacak her bir form için tekil bir numara ve formun oluşturulduğu günün tarihi üzerine yazılmalıdır. Bu durumun uygulamada kolay takip edilebilmesi için ayrı dekont serileri açılabilir. Bu masraf formunda yapılan giderlere ait belgelerin detayları yer almak zorundadır. Ayrıca bu masraf formu firma kaşesi ve imzasıyla matbu olarak ya da elektronik imza/mali mühür ile elektronik ortamda muhafaza edilmek zorundadır.

**Z raporu:** Gün sonunda her bir yazar kasadan alınan Z raporunun Netsis'e aktarılan muhasebe kaydında belge tipi açıklaması "**Z Raporu**" olarak yapılmalıdır. Ayrıca bu Z Raporu'nun numarası ve tarihinin de girilmesi zorunludur. Ancak gün içinde yapılan satışlarda Z Raporunun üzerinde yer alan ödeme yöntemlerine (nakit, kredi kartı, vb.) göre ayrıştırılmalıdır. Ödeme yöntemine isabet edecek KDV tutarlarının da ayrıştırılması ve her bir ödeme yönteminin farklı yevmiye maddelerinde gösterilmesi gerekmektedir.

**Çek bordrosu:** e-Defter uygulamasında kılavuzda sayılan tüm belge tiplerinde olduğu gibi, her bir çek belgesinin de ayrı yevmiye maddelerine kaydedilmesi esastır. Ancak çek bordrosuyla da kaydı mümkün olduğundan e-Defter uygulamasında da bu bordolar üzerinden, aynı alıcı veya satıcıya ait olmak şartıyla, birden fazla çek aynı yevmiye maddesinde kaydedilebilir. Ayrıca muhasebe kaydında belge tipi açıklaması "**Çek bordrosu**" olarak kaydı yapılır ve bu çek bordrosunun numarası ve tarihinin girilir. Her bir çek bordrosunda, çeklerin detayları yer almak zorundadır. Bu çek bordrosu firma kaşesi ve imzasıyla matbu olarak ya da elektronik imza/mali mühür ile elektronik ortamda muhafaza edilmek zorundadır.

**Senet bordrosu**: e-Defter uygulamasında kılavuzda sayılan tüm belge türlerinde olduğu gibi, her bir senet belgesinin de ayrı yevmiye maddelerine kaydedilmesi esastır. Ancak senet bordrosuyla da kaydı mümkün olduğundan e-Defter uygulamasında da bu bordolar üzerinden, aynı alıcı veya satıcıya ait olmak şartıyla, birden fazla senet aynı yevmiye maddesinde kaydedilebilir. Ayrıca muhasebe kaydında belge tipi açıklaması "**Senet** **bordrosu**" olarak kaydı yapılır ve bu senet bordrosunun numarası ve tarihinin girilmesi zorunludur. Senet bordrolarında, senetlerin detayları yer almak zorundadır. Bu senet bordrosu firma kaşesi ve imzasıyla matbu olarak ya da elektronik imza/mali mühür ile elektronik ortamda muhafaza edilmek zorundadır.

**Ücret** **Bordrosu**: Firmalar çalışanları için aylık olarak oluşturacakları ücret bordrolarını muhasebe aktardıktan sonra oluşan fişte, tüm personel için oluşan bordroları bir listeye bağlayıp, belge tipi açıklaması "**Ücret Bordrosu** **İcmali**" olarak kaydedebilir. Ücret bordrosu icmalinin numara ve tarihinin girilmesi zorunludur. Ancak ücret bordrosu icmalinde matbu bir numara ve tarih olmadığı için, oluşturulacak her bir icmal listesi için tekil bir numara verilmeli ve icmalin oluşturulduğu günün tarihi muhasebe fişinin belge tarihine yazılmalıdır.

**Serbest Meslek Makbuzu**: Serbest meslek erbabının, mesleki faaliyetlerine ilişkin her türlü tahsilatı için düzenlediği belge serbest meslek makbuzudur. Bu makbuz e-Defter kılavuzunda sayılan belgeler arasında yer alan makbuz (receipt) ile karıştırılmamalıdır. Serbest meslek makbuzu sayılan belgeler arasında yer almadığı için belge tipi açıklaması "**serbest** **meslek** **makbuzu**" olarak kaydı yapılır. Ayrıca belgenin numarası ve tarihinin de girilmesi zorunludur.

| **Kayıt Edilen**<br>**Belge** | **Document** **Type** | **Document**<br>**TypeDescription** | **Document**<br>**Number** | **Document**<br>**Date** | **Payment** **Method** |
| --- | --- | --- | --- | --- | --- |
| **Fatura** | Invoice |  | Fatura<br>Numarası | Fatura tarihi | Nakit/Kredi Kartı |
| **CariÖdeme**<br>**Emri** | Other | Ödeme Emri | Dekont<br>Numarası | Tarih | Nakit |
| **Kasa** **Tahsil** | Receipt |  | Fiş no | Tarih | Kredi Kartı/Nakit |
| **Kasa** **Tediye** | Other | Tediye | Fiş no | Tarih | Nakit |
| **Senet** | Voucher(M.Senet/S.Ciro/B.Senet) |  | Senet No | Tarih | Senet |
| **Çek** | Check (M.Çek / Ç.Ciro / B.Çek) Tek tek muhasebeleştirme<br>Other(Bordro bazında muhasebeleştirme) | Çek Bordrosu | Çek No<br>Bordro No |  | Çek |
| **Dekont** | Seri FT ise "**Invoice**", değilse "**Other**" | FT ise boş,<br>Elle girilmiş ise girilen<br>bilgi<br>Boşsa "**Dekont**" | Fiş No | Valör Tarihi | Genek Dekont kaydında seçilen ödeme türü<br>Senet tahsilat işlemlerinde Nakit |
| **Müstahsil** | Receipt |  | Fiş No | Tarih |  |
| **Banka** | Other | Dekont | Belge No | Tarih | Nakit |
| **Bordro** | Other | Ücret Bordrosu İcmali | Fiş No | Tarih |  |

**Belge Kayıtlarındaki Düzenlemeler:** Genel dekont kaydı ekranında kaynak belge bilgileri girişi:

![](../_assets/6c728e30e017afac90b2.png)

Yevmiye fiş girişinde kaynak belge bilgileri girişi alanları manuel fiş girişinde aktif, ön muhasebeden akan kayıtlarda pasif gelecektir.

![](../_assets/6ca039179143bb428148.png)

Kasa modülünden girilen kayıtlarda kaynak belge bilgileri girişi:

![](../_assets/c603193952e93c7c6308.png)

Ödeme emri ekranında kaynak belge bilgileri girişi:

![](../_assets/c6fb6067a6e410b9951a.png)

**Yevmiye Detay Değişikliği:** e-Defter'de yer alacak kayıtlarda şematron kontrolü gereği dolu olması zorunlu olan alanlar vardır. Bu alanların herhangi bir nedenle boş olması halinde defter oluşturma öncesinde hızlıca düzenlenebilmesi için Gezgin\\Muhasebe\\Muhasebe\\İşlemler\\Hızlı Bilgi Değişikliği\\Yevmiye Detay Değişikliği ekranı kullanılabilir.

![](../_assets/faf0ae87cb464f0c20d7.png)

![](../_assets/d68aad4f4a43bfcf8b00.png)

Düzenlenen bilgiler Değişen Bilgileri Sakla butonu ile saklandıktan sonra tekrar hazırlık çalıştırılmamalıdır. Çalıştırılması halinde yevmiye detay değişikliği ekranından yapılan düzenlemeler silinecektir.
