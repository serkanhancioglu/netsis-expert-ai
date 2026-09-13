---
title: "Genel Dekont Kaydı"
page_id: "22805784"
product: "netsis-3-enterprise"
depth: 5
is_section: true
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Dekont"
  - "Kayıt / Dekont"
  - "Genel Dekont Kaydı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Dekont / Kayıt / Dekont / Genel Dekont Kaydı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTFlYzRiNWVkLTMyOWMtNDc4Yi1iZjUzLTM2YTY3ZTFiMDU3NSZsaW5rPWM2ODMzYzFmLWVhNGMtNDI4OS04OTQxLWVhN2U2OTE3ZjYyOSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=1ec4b5ed-329c-478b-bf53-36a67e1b0575&link=c6833c1f-ea4c-4289-8941-ea7e6917f629&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "genel-dekont-kaydi_22805795_22805784.html"
source_version: "2022-11-29T13:52:02.943+03:00"
source_bytes: 821544
fetched_at: "2026-09-13T04:08:56+00:00"
generator: "netsis-scraper 1.0.0"
---
# Genel Dekont Kaydı

Genel Dekont Kaydı; Finans Bölümü'nde, "Kayıt/Dekont" menüsünün altında yer alır. Genel Dekont Kaydı; masraf faturalarının kayıtları, hesaplar arası virman işlemleri veya ithalat/ihracat işlemleri ile ilgili mal bedel ve masraflarının kaydedildiği bölümdür. Genel Dekont Kaydı, bir veya birden fazla cari, muhasebe, banka ve stok hesaplarını ilgilendiren tutar transferlerinde kullanılır. Ön muhasebenin mahsup fişine benzer. Sınırsız kayıt girilebilir. Genel Dekont Kaydı; Dekont Saha-1 ve Dekont Saha-2 olmak üzere iki sekmeden oluşur.

**Dekont Saha-1**

![](../../../../../_assets/ad95b20d32b6cb34d55e.png)

Dekont Saha-1 alanları ve içerdiği bilgiler aşağıdaki şekildedir:

<table>

<tbody>
<tr>
<th>Genel Dekont Kaydı Ekranı</th>
<th> </th>
</tr>
<tr>
<td>
<p>Seri Kodu</p>
</td>
<td>

<p>Girilen dekontun seri numarasının kaydedildiği alandır. Dekont modülünden yapılan kayıtları birbirinden ayırmayı sağlar. Rehber butonu <img src="../../../../../_assets/088477bb321d1b20c939.jpg"/> ile, kayıtlı seri kodlarına ulaşılır. "Seri Kodu" alanı boş bırakılmaz.</p>
<p><strong>Örneğin: </strong>Çek tahsilatları için CT, senet tahsilatları için ST, banka masrafları için BK gibi farklı seriler girilebilir. Seri numaralarının daha önce Dekont<strong> → </strong>İşlemler → "<a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253D80295780-5f10-4258-bd3d-8838ecbf1830%2526link%253D366b4e3d-3587-4656-b315-ae2f8db29777%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Seri Kodu Tanımlama</a>" bölümünden kaydedilmesi gerekir.</p>
			İthalat ve İhracat işlemleri ile ilgili dekont kayıtlarında IT ve IH serisinin kullanımı zorunludur.
</td>
</tr>
<tr>
<td>
<p>Dekont No</p>
</td>
<td>

<p>Program tarafından otomatik olarak her bir dekont serisi için 1 rakamından başlar. Kaydedilen her dekont için bir sayı arttırılarak devam eder. Farklı bir numaradan başlaması istendiğinde ise; Dekont → İşlemler → "<a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253Da390a40a-f4e6-42ee-a601-d03e99b93ac9%2526link%253D6a039680-30e4-49ed-a9c2-1ec883feb8f8%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Dekont Numarası Düzenleme</a>" bölümü kullanılarak serilere başlangıç numarası verilir. Rehber butonu <img src="../../../../../_assets/088477bb321d1b20c939.jpg"/> ile, kayıtlı dekont numaralarına ulaşılır.</p>

</td>
</tr>
<tr>
<td>
<p>İşlem Tarihi</p>
</td>
<td>
<p>Dekont kaydının girildiği tarihtir.</p>
</td>
</tr>
<tr>
<td>
<p>Fiş No</p>
</td>
<td>
<p>Kaydı yapılan dekont için fiş numarası girilen alandır. Bu alana girilen numara, ilgili modüllerdeki "Fiş No" alanına otomatik olarak aktarılır.</p>
</td>
</tr>
<tr>
<td>
<p>Hesap Kodu</p>
</td>
<td>

<p>Muhasebe Hesap Kodu, Cari Kodu, Stok Kodu ya da Banka Hesap Kodunun girildiği alandır. Rehber butonu <img src="../../../../../_assets/088477bb321d1b20c939.jpg"/> ile; cari, stok ve muhasebe kodlarına ulaşılır. Rehber butonunun yanında yer alan "Cari, Stok, Muhasebe veya Banka" seçenekleri ile ilgili kısım seçilir. Seçilen hesabın işlem göreceği durumun borç olması istendiğinde "Borç", alacak olması istendiğinde ise "Alacak" seçeneği işaretlenerek klavyedeki &lt;tab&gt; tuşu ile ilerlenir.</p>
			Banka Hesap Kodlarının rehberde yer alması istendiğinde; Banka → Kayıt → Banka Genel Parametreleri → "Banka Entegre" seçeneğinin işaretlenmesi gerekir.

			<p><img src="../../../../../_assets/d36751a701bf182d9d4a.png"/></p>

</td>
</tr>
<tr>
<td colspan="1">Açıklama</td>
<td colspan="1">İlgili modüle kaydedilmesi istenen dekont açıklama bilgisinin girildiği alandır.</td>
</tr>
<tr>
<td colspan="1">Kayıt Sayısı</td>
<td colspan="1">

<p>Satırda girilecek olan tutarın Referans/Proje bazında dağılımını sağlayan alandır. Kayıt sayısı standart şekilde "1" olarak ekrana gelir. Girilecek olan tutarın farklı bir projeye veya masraf merkezine dağıtılması durumunda, tutarın kaça bölüneceği ile ilgili rakam girilir. </p>
<p>Aşağıda yer alan örnekte girilecek olan tutar 2 farklı projeye ve masraf merkezine bölünmüştür.</p>
<p><img src="../../../../../_assets/8e78148c61130f6926ea.png"/></p>
<p>Proje/Referans Bazında Dağılım ekranının alanları ve içerdiği bilgiler aşağıdaki şekildedir:</p>

<table>
<tbody>
<tr>
<th>Proje/Referans Bazında Dağılım Ekranı</th>
<th> </th>
</tr>
<tr>
<td>Girilen Kayıt Sayısı</td>
<td>Proje/referans bazında dağılım için girilen kayıt sayısının izlendiği alandır.</td>
</tr>
<tr>
<td>Toplam Kayıt Sayısı</td>
<td>Proje/referans bazında dağılım için toplam kayıt sayısının izlendiği alandır.</td>
</tr>
<tr>
<td>Proje Kodu/Referans Kodu</td>
<td>
"Proje Kodu" veya "Referans Kodu" uygulamasının kullanıldığı durumlarda aktif hale gelen alanlardır. İlgili proje seçildikten sonra varsa referans kodu seçilir. Rehber butonu <img src="../../../../../_assets/088477bb321d1b20c939.jpg"/> ile, proje/referans kodlarına ulaşılır.
</td>
</tr>
<tr>
<td>Tutar</td>
<td>
İlgili proje/referans bazında dağılım için tutar girilen alandır. Aynı işlem tekrarlanarak ikinci veya daha sonraki satırlar oluşturulup Tamam <img src="../../../../../_assets/39d77b8716226638d9ce.jpg"/> butonuna basılır. Burada girilen rakamlar, "Genel Dekont Kaydı" ekranında girilen satır sayısı kadar oluşur.
</td>
</tr>
<tr>
<td>
<img src="../../../../../_assets/39d77b8716226638d9ce.jpg"/> Tamam
</td>
<td>Girilen bilgilerin onaylanmasını sağlayan butondur.</td>
</tr>
<tr>
<td><img src="../../../../../_assets/973111d004995dca0113.jpg"/> İptal</td>
<td>Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur.</td>
</tr>
</tbody>
</table>

<p> </p>

</td>
</tr>
<tr>
<td>
<p>Değişsin</p>
</td>
<td>
<p>Bu alanda ön değer olarak "Döviz tutarı" seçeneği otomatik şekilde ekrana gelir. Bu şekilde ilerlenirse, klasik döviz uygulaması yapılır. Yani, girilen kur ve döviz tutarına göre TL tutar hesaplanır. "Alanın sağ tarafında yer alan aşağı ok butonu ile seçim yapılır. Kur" seçeneği seçildiğinde, döviz tutarı sabit kalır ve girilen TL tutara göre kur hesaplanır. "Tutar" seçeneği seçildiğinde ise; kur sabit tutulup, girilen TL tutara göre döviz tutarı hesaplanır.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>Döviz/Türk Lirası</p>
</td>
<td colspan="1">
<p>Döviz bilgisi girilerek oluşturulacak kayıtlar için "Döviz", Türk Lirası girilerek oluşturulacak kayıtlar için "TL" seçeneğinin işaretlenmesi gerekir. Döviz seçeneği ile girilen kayıtlarda döviz sorgulama ekranı görüntülenir. Sorgulanan döviz kuru bilgisi ile "Tutar" alanına girilecek "Döviz Tutarı" çarpılarak TL değerine çevrilir. Hesaplanan değer "Tutar" alanına aktarılır. Bu uygulama, "Değişsin" alanında yapılan seçime göre farklılık gösterir. Döviz tutarı, "Cari Hareket Kayıtları" bölümüne (Döviz uygulaması olan firmalar için) aktarılır.</p>
<p>Döviz-TL seçenekli para birimi alanındaki TL seçeneği, <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253Df7baa628-4b9a-47cb-8f22-03aabde76c1e%2526link%253D8f91f576-27e0-4eea-a0f1-71be7d79c366%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Şirket/Şube Parametre Tanımları</a> ekranındaki "Para Birimi" alanına göre program tarafından otomatik olarak işaretli şekilde gelir.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>Döviz Tutarı</p>
</td>
<td colspan="1">
<p>Kur bilgisi girildikten sonra ilgili hareketin döviz tutarının girildiği alandır.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>Tutar</p>
</td>
<td colspan="1">
<p>Girilen dekont kaydına ait tutar bilgisinin girildiği alandır. "Döviz Tipi" seçilerek girilen kayıtlarda, "Döviz Tutarı" ve "Kur" çarpılarak hesaplanan tutar bu alana aktarılır.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>KDV Dahil/Hariç</p>
</td>
<td colspan="1">
<p>Girilmiş olan rakama KDV rakamının dahil edilmesi istendiğinde "Dahil", dahil edilmesi istenmediğinde ise "Hariç" seçeneğinin işaretlenmesi gerekir. KDV oranı girildikten sonra, yapılan seçime göre tutar alanı tekrar güncellenir.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>KDV Oranı</p>
</td>
<td colspan="1">
<p>KDV oranının girildiği alandır.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>KDV Tutarı</p>
</td>
<td colspan="1">
<p>Oran girildikten sonra,  KDV tutarının program tarafından hesaplanarak otomatik şekilde ekrana getirdiği alandır. Üzerinde değişiklik yapılabilir.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>Miktar</p>
</td>
<td colspan="1">
<p>Dekont → Kayıt <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253Dd69f4164-212a-4596-8715-74903c23d163%2526link%253D74c0c526-a87b-48db-8b3b-4f5d7894b970%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Dekont Parametreleri</a>→ → "Miktar Girişi Yapılsın" parametresinin işaretlenmesi halinde aktif hale gelen alandır. Girilen miktar bilgisi, cari hareket kayıtlarının ve yevmiye fiş kayıtlarının miktar alanına aktarılır.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>Valör Başlangıç Tarihi</p>
</td>
<td colspan="1">Dekont → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253Dd69f4164-212a-4596-8715-74903c23d163%2526link%253D74c0c526-a87b-48db-8b3b-4f5d7894b970%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Dekont Parametreleri</a> → "Valör Bilgisi Girişi Yapılsın” parametresinin işaretlenmesi halinde aktif hale gelen alandır. Günün tarihi otomatik olarak ekrana gelir. Elle (manuel) değiştirilmesine izin verilen bu tarih başlangıç kabul edilip, valör gününün bu tarihe eklenmesi ile yeni bir tarih hesaplanır.</td>
</tr>
<tr>
<td colspan="1">
<p>Vadelere Bölünsün</p>
</td>
<td colspan="1">

<p>Kaydedilen dekont tutarının, cari hareket kayıtlarına, kullanıcı tarafından belirlenen vade sayısı kadar bölünerek birden fazla kayıt halinde işlenmesi için işaretlenen seçenektir. Dekont kaydı sırasında açılan ekranda "Vade Günü" ve "Oran (Yüzde)" alanları sorgulanır. </p>
			"Vadelere Bölünsün" seçeneği, "Hesap Kodu" alanına "Muhasebe Kodu" girildiği zaman aktif hale gelmez.
<p><img src="../../../../../_assets/32b5efab4b1348777c04.png"/></p>
<p>Cari Hesap Vade Oranları ekranının alanları ve içerdiği bilgiler aşağıdaki şekildedir:</p>

<table>
<tbody>
<tr>
<th>Cari Hesap Vade Oranları Ekranı</th>
<th> </th>
</tr>
<tr>
<td>Peşinat Tutarı</td>
<td>Taksitli satış bilgileri için peşinat tutarı girilen alandır.</td>
</tr>
<tr>
<td>Taksit Sayısı</td>
<td>Taksitli satış bilgileri için taksit sayısı girilen alandır.</td>
</tr>
<tr>
<td colspan="1"><img src="../../../../../_assets/d17849675b68554265fa.png"/> Taksitleri Oluştur</td>
<td colspan="1">
<p>"Peşinat Tutarı" ve "Taksit Sayısı" girildikten sonra taksitlerin oluşturulması için kullanılan butondur.</p>
<p><strong>Örneğin: </strong>50 TL tutarındaki bir dekontun peşinat tutarının 20 TL, taksit sayısının ise 2 olarak girildiği varsayıldığında, oluşturulan taksit grid ekrana aşağıdaki şekilde yansır.</p>
<p><img src="../../../../../_assets/1f2c5ea5b2860f1a7829.png"/></p>
<p>Girilen peşinat tutarına göre oranlama, program tarafından otomatik olarak hesaplanır. 50 TL tutarındaki dekontun 20 TL tutarındaki peşinatı, dekont tutarının %40'ını oluşturur. Kalan 30 TL tutarındaki miktar 2 eşit taksite bölünür. Hesaplanan 15 TL tutarındaki taksitler, 50 TL tutarındaki dekontun %15'ini oluşturur.</p>
</td>
</tr>
<tr>
<td>Vade Günü</td>
<td>Taksitli satış bilgileri için vade günü girilen alandır.</td>
</tr>
<tr>
<td>Vade Tarihi</td>
<td>
<p>"Vade Günü" girildikten sonra, "İşlem Tarihi" alanındaki tarihe vade günü eklenerek hesaplanan tarihin otomatik olarak aktarıldığı alandır.</p>
</td>
</tr>
<tr>
<td>Oran (Yüzde)/Tutar</td>
<td>
<p>Taksitli satış bilgileri için oran bilgisi girilen alandır. Girilen orana göre tutar bilgisi program tarafından otomatik olarak hesaplanır.</p>
<p><strong>Örneğin: </strong>50 TL tutarındaki bir dekontun oranı %40 olarak girildiğinde, program "Tutar" alanına 20 rakamını otomatik olarak getirir.</p>
<p><img src="../../../../../_assets/f0f666e74e37ee309ee4.png"/></p>
</td>
</tr>
<tr>
<td><img src="../../../../../_assets/4f2c70e38891c33ca4ba.png"/> Tamam</td>
<td>Girilen bilgilerin kaydedilmesi için kullanılan butondur.</td>
</tr>
<tr>
<td><img src="../../../../../_assets/5d28b2685d1d5f39a70f.png"/> Satır Azalt</td>
<td>Grid ekranda oluşan taksit satırının silinmesi için kullanılan butondur. Satır Azalt <img src="../../../../../_assets/5d28b2685d1d5f39a70f.png"/> butonu, ekrandaki alanlara bilgi girişi yapıldıktan sonra Tamam <img src="../../../../../_assets/4f2c70e38891c33ca4ba.png"/> butonu ile girilen bilgiler kaydedilip dekont ekranındaki "Vadelere Bölünsün" seçeneğine tıklandığında aktif hale gelir.</td>
</tr>
</tbody>
</table>

<p> </p>

</td>
</tr>
<tr>
<td colspan="1">
<p>Valör Günü</p>
</td>
<td colspan="1">
<p>Valör gününün girildiği alandır. Bu alana girilen gün değeri valör başlangıç tarihine eklendiğinde hesaplanan yeni tarih, valör tarihine aktarılır.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>Efektif Tarih</p>
</td>
<td colspan="1">
<p>Valör başlangıç tarihine valör gününün eklenmesi ile bulunan tarihin aktarıldığı alandır. Valör tarihi, ilgili cari hesabın hareket kayıtlarındaki vade tarihi alanına aktarılır.</p>
</td>
</tr>
<tr>
<td colspan="1">Basım Yapılsın</td>
<td colspan="1">
<p>Kaydı yapılan dekontun standart basımının yapılması için kullanılan seçenektir. </p>
</td>
</tr>
<tr>
<td colspan="1">

<p><img src="../../../../../_assets/11c219723b32599f0785.png"/> Stopaj Girişi</p>

</td>
<td colspan="1">

<p>İlgili dekont tutarı üzerinden, belirlenecek oranlarda Stopaj ve SSDF kesilmesi için kullanılan butondur. İlk olarak girilen tutar üzerinden stopaj, daha sonra stopaj kesilmiş tutar üzerinden SSDF kesilir.</p>
<p><img src="../../../../../_assets/1b7a739f53810d62f2fa.png"/></p>
<p>Stopaj Girişi ekranı alanları ve içerdiği bilgiler aşağıdaki şekildedir:</p>

<table>
<tbody>
<tr>
<th>Stopaj Girişi Ekranı</th>
<th> </th>
</tr>
<tr>
<td>
<p>Stopaj Oranı</p>
</td>
<td>
<p>Stopaj oranının girildiği alandır. Bu alana girilen değer, diğer kayıtlara program tarafından otomatik olarak aktarılır. İstendiğinde kullanıcı tarafından değişiklik yapılabilir.</p>
</td>
</tr>
<tr>
<td>Stopaj Tutarı</td>
<td>KDV öncesi tutar alanındaki değerin, stopaj oranına göre yüzde tutarının program tarafından hesaplanarak aktarıldığı alandır. İstendiğinde kullanıcı tarafından değişiklik yapılabilir.</td>
</tr>
<tr>
<td>Stopaj Kodu</td>
<td>
Stopaj tutarının muhasebede takip edileceği hesap kodunun girildiği alandır. <img src="../../../../../_assets/088477bb321d1b20c939.jpg"/> Rehber butonu yardımıyla stopaj kodları arasından seçim yapılır.
</td>
</tr>
<tr>
<td>SSDF Oranı</td>
<td>Savunma Sanayi Destekleme Fonu oranının girildiği alandır. Bu alana girilen değer, diğer kayıtlara program tarafından otomatik olarak aktarılır. İstendiğinde kullanıcı tarafından değişiklik yapılabilir.</td>
</tr>
<tr>
<td>SSDF Tutarı</td>
<td>Stopaj tutarının, girilen SSDF oranına göre yüzde değerinin program tarafından hesaplanarak aktarıldığı alandır. İstendiğinde kullanıcı tarafından değişiklik yapılabilir.</td>
</tr>
<tr>
<td>SSDF Kodu</td>
<td>Savunma Sanayi Destekleme Fonu tutarının muhasebede takip edileceği hesap kodunun girildiği alandır. </td>
</tr>
<tr>
<td>
<img src="../../../../../_assets/39d77b8716226638d9ce.jpg"/> Tamam
</td>
<td>
Stopaj girişi ekranına girilen bilgilerin onaylanması için kullanılan butondur.
</td>
</tr>
<tr>
<td>
<img src="../../../../../_assets/973111d004995dca0113.jpg"/> İptal
</td>
<td>Stopaj girişi ekranına girilen bilgilerin iptal edilmesi için kullanılan butondur.</td>
</tr>
</tbody>
</table>

</td>
</tr>
<tr>
<td colspan="1">B Formu</td>
<td colspan="1">

<p>Dekont tutarının BA/BS bildirimine uygunluğu durumunda işaretlenmesi gereken seçenektir. </p>
			Bilanço esasına göre defter tutan mükelleflerin bir kişi veya kurumdan (KDV hariç) 5.000 TL ve üzerindeki; mal ve/veya hizmet alımlarını Mal ve Hizmet Alımlarına İlişkin Bildirim Formu (Form Ba), mal ve/veya hizmet satışlarını ise Mal ve Hizmet Satışlarına İlişkin Bildirim Formu (Form Bs) ile (KDV hariç tutarlar dikkate alınarak) bildirme yükümlülüğü bulunur.
</td>
</tr>
<tr>
<td colspan="1">Cari kodu</td>
<td colspan="1">

<p>"B Formu" seçeneğinin işaretlenmesi ile aktif hale gelen alandır. B Formu işaretlenen dekontların takip edileceği cari kodun seçilmesini sağlar. Rehber butonu <img src="../../../../../_assets/088477bb321d1b20c939.jpg"/> ile, kodlar arasından seçim yapılır.</p>

</td>
</tr>
<tr>
<td colspan="1">Belge Türü</td>
<td colspan="1">Dekont belge türünün seçildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile, belge türleri arasından seçim yapılır.</td>
</tr>
<tr>
<td colspan="1">Ödeme Türü</td>
<td colspan="1">Ödeme türünün girildiği alandır. Seçilen belge türünün ne şekilde ödeneceği belirlenir.</td>
</tr>
<tr>
<td colspan="1">

<p><img src="../../../../../_assets/729df1abaad494a8bc70.png"/> Yeni Dekont</p>

</td>
<td colspan="1">

<p>Dekont kaydının tamamlanması halinde, yeni bir dekonta geçmek için kullanılan butondur. Dekontun bakiye vermesi durumunda, butona basılması ile birlikte bakiyeyi kapatmadan işleme devam edilmesi ile ilgili onay ekranı görüntülenir. </p>
<p><img src="../../../../../_assets/62579336fbe3473d1c02.png"/></p>
<p>Onaylanması durumunda yeni dekont ile işleme devam edilir. </p>
			Dekont → Kayıt → Dekont Parametreleri → "Bakiye Veren Dekonttan Çıkılmasın" parametresinin işaretlenesi halinde, içinde bulunulan dekont bakiye veriyorsa, Yeni Dekont <img src="../../../../../_assets/729df1abaad494a8bc70.png"/> butonuna basılsa bile, dekont kaydından çıkılmasına izin verilmez.
</td>
</tr>
<tr>
<td colspan="1">

<p><img src="../../../../../_assets/c9c84236b8200318e2fd.png"/> Tamamla</p>

</td>
<td colspan="1">

<p>Dekont kaydının tamamlanması için kullanılan butondur. İndirilecek KDV bilgi girişi yapıldıktan sonra dekont kaydı tamamlanır.</p>
<p><img src="../../../../../_assets/474b06f401569e8495b9.png"/></p>
<p>İndirilecek KDV Bilgi Girişi ekranı alanları ve içerdiği bilgiler aşağıdaki şekildedir:</p>

<table>
<tbody>
<tr>
<th>İndirilecek KDV Bilgi Girişi Ekranı</th>
<th> </th>
</tr>
<tr>
<td>Alış Faturasının Tarihi</td>
<td>Dekont işlem tarihinin program tarafından otomatik olarak aktarıldığı alandır.</td>
</tr>
<tr>
<td>Alış Faturasının Serisi</td>
<td>Alış faturasına ait seri numarasının girildiği alandır.</td>
</tr>
<tr>
<td>Alış Faturasının Sıra Numarası</td>
<td>Alış faturasına ait sıra numarasının girildiği alandır.</td>
</tr>
<tr>
<td>Satıcı Adı Soyadı Unvanı</td>
<td>Dekont ekranında girilen hesaba ait isim bilgisinin otomatik olarak aktarıldığı alandır. İstendiğinde kullanıcı tarafından değişiklik yapılabilir.</td>
</tr>
<tr>
<td>Satıcının Vergi Dairesi</td>
<td>Satıcının bağlı olduğu vergi dairesinin girildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile, daha önce girilen vergi dairesi seçeneklerine ulaşılır.</td>
</tr>
<tr>
<td>Satıcının Vergi Kimlik Numarası/TC Kimlik Numarası</td>
<td>Satıcının kimlik numarası bilgilerinin girildiği alandır.</td>
</tr>
<tr>
<td>Alınan Mal ve/veya Hizmetin Cinsi</td>
<td>Alınan mal ve/veya hizmetin girildiği alandır.</td>
</tr>
<tr>
<td>Alınan Mal ve/veya Hizmetin Miktarı</td>
<td>Alınan mal ve/veya hizmetin miktar bilgisinin girildiği alandır. </td>
</tr>
<tr>
<td colspan="1">Gümrük Giriş Beyannamesi Tescil Numarası</td>
<td colspan="1">Gümrük giriş beyannamesine ait tescil numarasının girildiği alandır.</td>
</tr>
<tr>
<td colspan="1">Belgenin İndirim Hakkının Kullanıldığı Beyanname Dönemi</td>
<td colspan="1">Belgenin indirim hakkının kullanıldığı beyanname döneminin girildiği alandır.</td>
</tr>
<tr>
<td colspan="1">İhracatına Aracılık Edilen Firmanın Vergi Kimlik Numarası/TC Kimlik Numarası</td>
<td colspan="1">İhracatı için aracılık edilen firmaya ait kimlik numarası bilgisinin girildiği alandır.</td>
</tr>
<tr>
<td colspan="1"><img src="../../../../../_assets/0fd06cd30fbc696fcf68.png"/> Değişikliği Kaydet</td>
<td colspan="1">İndirilecek KDV bilgi girişi ekranında girilen bilgilerin kaydedilmesini sağlayan butondur.</td>
</tr>
<tr>
<td colspan="1"><img src="../../../../../_assets/249197106fa4d90d9fe9.png"/> Çıkış</td>
<td colspan="1">İndirilecek KDV bilgi girişi ekranında girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur.</td>
</tr>
</tbody>
</table>

</td>
</tr>
</tbody>
</table>

**Dekont Saha-2**

![](../../../../../_assets/128e3e4718cdb697d159.png)

Dekont Saha-2 alanları ve içerdiği bilgiler aşağıdaki şekildedir:

| Genel Dekont Kaydı Ekranı |  |
| --- | --- |
| Export Referans Numarası | İthalat/ihracat işlemleri için oluşturulan masraflar ve mal bedelleri ile ilgili kayıtlar için ithalat/ihracat dosya numarasının girildiği alandır. Bu alan boş bırakıldığında ithalat için yapılan masraflar, ithalat kapatma ekranında dikkate alınmaz. Alanın sağ tarafında yer alan aşağı ok butonu ile, daha önce girilen referans numaralarına ulaşılır. |
| Export Tipi | "İthalat Kapatma" için işlem yapılacak dekont için masraf tipinin seçildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile, tipler arasından seçim yapılır (Mal Bedeli, Gümrük Vergisi, Komisyon gibi). |
| Referans Kodu | Muhasebe → Kayıt → [Muhasebe Parametreleri](<../Dekont Parametreleri.md>) → "Fişlerde Referans Kodu Sorulsun" parametresinin işaretlenmesi ile aktif hale gelen alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, referans kodlarına ulaşılır. Boş bırakılmaz. |
| Plasiyer Kodu | Yardımcı Programlar → Kayıt → [Şirket-Şube Parametreleri](<../../../../Muhasebe/Muhasebe Modülü/Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/Genel Tanımlar/Yardımcı Programlar-Şirket-Şube Parametreleri.md>) → "Plasiyer Uygulaması Var" parametresinin işaretlenmesi ile aktif hale gelen alandır. Dekont kaydı sırasında ilgili plasiyer kodunun girilmesi gerekir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, plasiyer kodlarına ulaşılır. Boş bırakılmaz. |
| Proje Kodu | Yardımcı Programlar → Kayıt → [Şirket-Şube Parametreleri](<../../../../Muhasebe/Muhasebe Modülü/Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/Genel Tanımlar/Yardımcı Programlar-Şirket-Şube Parametreleri.md>) → "Proje Uygulaması Var" parametresinin işaretlenmesi ile aktif hale gelen alandır. Dekont kaydı sırasında ilgili plasiyer kodunun girilmesi gerekir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, proje kodlarına ulaşılır. Boş bırakılmaz. Girilen proje kodları, cari hareketlere ve entegrasyona aktarılır. |
| Cari Rapor Kodu | Cari → Kayıt → Cari Parametreleri → "Hareketlerde Rapor Kodu Girilsin" parametresinin işaretlenmesi ile aktif hale gelen alandır. Hareketlere aktarılması ve raporlanması amacıyla 1 karakterden oluşan rapor kodu girişi yapılır. |
| Şube Girilecek | Şubeli çalışıldığında ve şube merkezinde dekont kaydı yapıldığında aktif hale gelen alandır. Seçenek işaretlendiği zaman dekont kaydının yapıldığı satırdaki hareket kaydı, şube kodu alanında tanımlanan şubeye aktarılır. Aktarma işleminde, ilgili dekonta ait bilgilerin tamamı, içinde bulunulan şirketin entegrasyon kayıtlarına aktarılır. Muhasebeye aktarım işleminde sadece, "Şube Girilecek" seçeneği işaretli olan hareketler ilgili şubenin muhasebe fişine aktarılır. |
| Şube Kodu | Dekont hareketlerinin aktarılacağı şube kodunun girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, şube kodları arasından seçim yapılır. |
| Cari Rapor Kodu-2 | Cari → Kayıt → [Cari Parametreleri](<../../../Cari/Kayıt - Cari/Cari Parametreleri.md>) → "Hareketlerde Rapor Kodu Girilsin" parametresinin işaretlenmesi ile aktif hale gelen alandır. Hareketlere aktarılması ve raporlanması amacıyla 15 karakterden oluşan rapor kodu girişi yapılır. |
| Ek Açıklama | Dekont → Kayıt → [Dekont Parametreleri](<../Dekont Parametreleri.md>) → "Ek Açıklama Girişi Yapılsın" parametresinin işaretlenmesi ile aktif hale gelen alandır. Bu parametre ile açılan üç açıklama satırına istenen açıklama bilgisi girilir. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır.

Kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
