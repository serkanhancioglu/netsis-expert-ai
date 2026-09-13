---
title: "Cari Hesaba Çek Cirosu / Borç Çekleri"
page_id: "24740201"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Borç Çekleri"
  - "Kayıt / Borç Çekleri"
  - "Cari Hesaba Çek Cirosu / Borç Çekleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Borç Çekleri / Kayıt / Borç Çekleri / Cari Hesaba Çek Cirosu / Borç Çekleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWNmMmQ2ODAyLWVjMmEtNGFkNy1hOGE0LTdkYmJhNWI4ZTkzYiZsaW5rPWEyODAxNDI5LWJmMGUtNGM3ZS05MzhlLWVlZWJjZWJmYjFlZiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=cf2d6802-ec2a-4ad7-a8a4-7dbba5b8e93b&link=a2801429-bf0e-4c7e-938e-eeebcebfb1ef&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "cari-hesaba-cek-cirosu-borc-cekleri_34218772_24740201.html"
source_version: "2022-12-13T13:50:16.870+03:00"
source_bytes: 237337
fetched_at: "2026-09-13T04:12:31+00:00"
generator: "netsis-scraper 1.0.0"
---
# Cari Hesaba Çek Cirosu / Borç Çekleri

Borç Çekleri modülü Cari Hesaba Çek Cirosu bölümü, Finans Bölümü'nde, "Kayıt/Borç Çekleri" menüsünün altında yer alır. Cari hesaplara ya da satıcılara verilen (ciro edilen) borç çeki kayıtlarının girildiği bölümdür.

![](../../../../_assets/ffcae73afe3d50c9f439.png)

Borç Çekleri modülü Cari Hesaba Çek Cirosu ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

<table>

<tbody>
<tr>
<th>Cari Hesaba Çek Cirosu Ekranı</th>
<th> </th>
</tr>
<tr>
<td>
<p>Çek No</p>
</td>
<td>
<p>Kaydedilen borç çekinin takibinin yapılması için kullanılan numaradır. Yeni çek girişi sırasında program tarafından sıradaki çek numarasının otomatik olarak ekrana getirilir. Çek numaraları, programın başlattığı numaradan takip edilerek ya da <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253De3efecc9-cb95-4597-94f0-27d35227fdb7%2526link%253Dad80d8a6-8a85-4d6d-bc42-e831b5bac740%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Çek Numarası Değişikliği</a> bölümünden de belirlenebilir.</p>
</td>
</tr>
<tr>
<td>
<p>Verildi Bordro No</p>
</td>
<td>

<p>Satıcıya aynı gün içinde verilen, tahsil ve teminata çıkılan bir veya birden fazla çekin tek bir numara altında toplanmasını sağlar.  "Verildi Bordro Numaraları" da, "Alındı Bordro Numaraları" alanında olduğu gibi program tarafından başlatılır ve bir sayı artarak sıra oluşturur. Rehber butonu <img src="../../../../_assets/088477bb321d1b20c939.jpg"/> ile, bordro numaralarına ulaşılır.</p>
Verildi Bordro numarasının başlangıç numarası değişikliği, Borç Çekleri → İşlemler → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253De3efecc9-cb95-4597-94f0-27d35227fdb7%2526link%253Dad80d8a6-8a85-4d6d-bc42-e831b5bac740%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Çek Numarası Değişikliği</a> bölümünden yapılır. Program diğer modüllerle entegre kullanılmaya başlandığında (cari hesaplarda kayıtlı müşterilere çek ciro edildiğinde ve bankaya tahsilata/teminata çıkışlarda)" Verildi Bordro Numarası" otomatik olarak aktarılır ve çeklerin ilgili alanlarına kaydedilir. 
<p>Bir veya birden fazla çek, tek bir verildi bordro numarası altında kaydedildikten sonra, bu bordro numarasına ait çek kayıtlarının bittiğine dair bilgisayara bilgi vermek ve entegre bölümlere (Cari, Muhasebe) çeklerin işlenmesi açısından Bordro Tamamlama işleminin yapılması gerekir. Bir "Verildi Bordrosuna" ait çekler, işlem ekranından çıkmadan arka arkaya kaydedilebilir.</p>
<p>Tamamlanmayan herhangi bir bordroya yeni bir çek kaydının eklenmesi istendiğinde, bordro numarası değiştirilerek (istenen numara ekrana getirtilerek) çek kayıtlarına devam edilir. Verildi bordro numarası ile kaydedilen çeklerin, bu işlemden sonra toplu izleme/iptal etme (Borç Çekleri → İşlemler → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253D2e84e0af-237f-4a65-9249-42f18242882f%2526link%253D0f37b144-47d2-48ae-933a-c67fdb1b1f8a%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Toplu Çıkış İptali</a>) olanağı bulunur.</p>

</td>
</tr>
<tr>
<td>
<p>R.Kod (Rapor Kodu)</p>
</td>
<td>
<p>Kaydedilen çeklerin, raporlamaya yönelik bir kod altında toplanması için, 1 karakter uzunluğunda isteğe göre kayıt oluşturulmasını sağlayan alandır.</p>
<p><strong>Örneğin;</strong> </p>
<p>Normal belirlenen çeklerin rapor kodu için (N), devir çeklerinin rapor kodu için (D) karakterleri kullanılabilir,</p>
<p>Çeklerin bankasına göre gruplamalar yaparak daha sonra toplu çıkış bölümünden rapor koduna göre hızlı ciro edilebilir ya da, </p>
<p>Rapor koduna göre listeler alınabilir.</p>
</td>
</tr>
<tr>
<td>
<p>Cari Rapor Kodu</p>
</td>
<td>
<p>Cari → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253D6f1c0005-6726-405d-8ac7-b213b41d23c7%2526link%253Dd50e5347-1966-4bcb-87c7-1d4897ae336e%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Cari Parametreleri</a> → “Hareketlerde Rapor Kodu Sorulsun” parametresinin işaretli olması halinde, "Rapor Kodu" alanında olduğu gibi raporlama amacıyla en fazla 15 karakter uzunluğunda kod girilen alandır.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>Asıl Borçlu<strong> </strong></p>
</td>
<td colspan="1">
<p>Kaydedilen çek "Asıl" ise, veren kişinin ismi bu alana program tarafından otomatik olarak aktarılır ve alana bilgi girilmesine izin verilmez. Çek "Ciro" ise (veren kişinin kendi çekleri değilse) asıl borçlusunun ismi yazılır. Asıl borçlusu da cari hesaplarda kayıtlı ise, asıl borçlunun cari kodu girilir. </p>
</td>
</tr>
<tr>
<td colspan="1">
<p>Vade Tarihi</p>
</td>
<td colspan="1">
<p>Çekin ödenme (vade) tarihinin girildiği alandır.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>Ödeme Tarihi</p>
</td>
<td colspan="1">

<p>Vade tarihi itibariyle çekin opsiyonlu ödenme tarihinin girildiği alandır. çek kaydı sırasında, ödeme tarihi vade tarihiyle aynı kaydedilir. Çek için girilen "Ödendi" ve "Karşılıksız Çek Kaydı" sonucu, gerçek ödeme tarihi program tarafından otomatik olarak düzeltilir.</p>

Çek için ödendi kaydının oluşturulması ile ilgili detaylı bilgi için; Dekont → Kayıt → Borç Senedi-Çeki Ödentisi, Dekont → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253D9f5b42e4-9363-40cd-85f6-2dc3e63973b7%2526link%253D3148d35d-9e92-424b-97cc-49879eef701f%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Toplu Borç Çeki Ödentisi</a>.<strong> </strong>

</td>
</tr>
<tr>
<td colspan="1">
<p>Yeri</p>
</td>
<td colspan="1">
<p>Çekin düzenlendiği il/ilçe bilgisinin girildiği alandır.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>Yer Kodu</p>
</td>
<td colspan="1">
<p>Çeklerin ciro edildiğini gösteren alandır. Çekler kaydedilirken, bu alanda bulunan "Ciro" seçeneği işaretli olarak ekrana gelir.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>Çıkış Tarihi</p>
</td>
<td colspan="1">

<p>Kaydedilen çeklerin (portföydeki çeklerin) satıcılara veya bankalara ciro edilme tarihinin girildiği alandır. Eski tarihlerde alınmış ve ileri vadeli olan çekler için devir kaydı girişi yapılırken, çeklerin ciro edildiği tarih olarak (bu tarih belli değil ise) programa kayıt yapıldığı günün tarihi kullanılabilir. Program entegre kullanılmaya başlandığında, çıkış tarihi sistem tarihi olarak otomatik şekilde ekrana getirilir ve üzerinde değişiklik yapılabilir. Çekler, programda bulunan ciro işleminden (Cari Hesaba Çek Cirosu, Tahsil Hesabına Çek Cirosu ve Teminat Hesabına Çek Cirosu) ciro edildiğinde veya "Devir Çek Girişi" bölümünden girilen devir çeklerinde "Yer Kodu" olarak "Ciro" seçildiğinde, bu alanın boş bırakılmaması gerekir. </p>

Çıkış tarihi, giriş tarihinden küçük bir tarih olamaz.

</td>
</tr>
<tr>
<td colspan="1">
<p>Verilen Kodu</p>
</td>
<td colspan="1">

<p>Çeklerin ciro edileceği satıcıya ait cari kodun girildiği alandır. Bu alanda yeni bir satıcı tanımlaması yapılmaz. Bu nedenle çeklerin ciro işlemlerine başlamadan önce, ilgili satıcıya ait cari kodun mutlaka tanımlanmış olması gerekir. Rehber butonu <img src="../../../../_assets/088477bb321d1b20c939.jpg"/> ile, cari kodlara ulaşılır.</p>

</td>
</tr>
<tr>
<td colspan="1">
<p>Plasiyer Kodu</p>
</td>
<td colspan="1">

<p>Yardımcı Programlar → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253Df7baa628-4b9a-47cb-8f22-03aabde76c1e%2526link%253D8f91f576-27e0-4eea-a0f1-71be7d79c366%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Şirket-Şube Parametre Tanımları</a> → "Plasiyer Uygulaması Var" parametresinin işaretlenmesi ile aktif hale gelen alandır. Plasiyerlerin, müşterilerden tahsil etmiş olduğu çeklerin takibinin yapılması istendiğinde kullanılır. Rehber butonu <img src="../../../../_assets/088477bb321d1b20c939.jpg"/> ile, plasiyer kodlarına ulaşılır. "<a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253D42a33a34-474e-48d9-abe6-d840af3abda4%2526link%253Dc595a1fa-5e62-4e0c-ac6e-20f7004074f8%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Cari Hesap Kayıtları</a>" bölümünde girilen ilgili müşterinin plasiyer kodu, program tarafından otomatik olarak bu alana aktarılır. Boş bırakılabilir fakat alan üzerinde değişiklik sadece, Cari → Kayıt → "Plasiyer Kodu Kayıtları" bölümünden tanımlı olan bir "Plasiyer Kodu" ile yapılır. Plasiyer kodu daha önce Cari → Kayıt → "Plasiyer Kodu Kayıtları" bölümünde tanımlanmamış ise bu alana giriş yapılamaz.</p>

Plasiyer Kodlarının tanımlanması ile ilgili detaylı bilgi için; Cari → Kayıt → "Plasiyer Kodu Kayıtları"<strong> </strong>

</td>
</tr>
<tr>
<td colspan="1">
<p>Proje Kodu</p>
</td>
<td colspan="1">

<p>Yardımcı Programlar → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253Df7baa628-4b9a-47cb-8f22-03aabde76c1e%2526link%253D8f91f576-27e0-4eea-a0f1-71be7d79c366%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Şirket-Şube Parametre Tanımları</a> → “Proje Uygulaması Var" seçeneğinin işaretlenmesi ile aktif hale gelen alandır. Proje uygulamasında, çeklerdeki her türlü giriş/çıkış işlemlerinde proje kodu sorgulanır ve boş bırakılmaz. Cari hareketlerde ve entegre havuzunda ise, kayıtlar proje kodu bazında tek tek oluşur. Rehber butonu <img src="../../../../_assets/088477bb321d1b20c939.jpg"/> ile, proje kodlarına ulaşılır.</p>

</td>
</tr>
<tr>
<td colspan="1">Tutar</td>
<td colspan="1">Kaydedilen çeklerin Türk Lirası tutarının girildiği alandır.</td>
</tr>
<tr>
<td colspan="1">
<p>Döviz Tipi</p>
</td>
<td colspan="1">

<p>Borç Çekleri → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253D52504cd7-729d-4e6a-b399-9dad6b8f6b86%2526link%253D597534ca-8916-4a9a-8508-156a1645e93b%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Borç Çekleri Parametreleri</a> → “Döviz Uygulaması Var" parametresinin işaretlenmesi ile aktif hale gelen alandır. "Döviz Tipi" ekranı ile, girilen çekin dövizli bilgileri tanımlanır. Çek kaydı sırasında döviz tipi ile ilgili ilk sorgulama, girilen çekin hangi döviz tipinden olduğu ile ilgili belirleme yapılması için kullanılır. "Döviz Tipi, Döviz Takibi → Kayıt → "Döviz İsimleri Tanımlama" bölümünden yapılır.</p>

Döviz tiplerinin tanımlanması ile ilgili detaylı bilgi için; Döviz Takibi → Kayıt → "<a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253D8120d06c-c829-4862-b199-07cfbac28149%2526link%253D667f1cda-7eac-4a96-a9da-18791e58f2a7%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Döviz İsimleri Tanımlama</a>"

<p>"Döviz Tipi" alanı 0 (sıfır) olarak bırakıldığında "dövizsiz" (TL çek girişi) yapılacağı anlamına gelir. Bu ekrandan girilen döviz cinsi, ilgili çekin "Döviz Tipi" alanına aktarılır.</p>

</td>
</tr>
<tr>
<td colspan="1">Döviz Tutarı</td>
<td colspan="1">Çek girişlerinde sorgulanan "Döviz Tipi" bazında, ilgili çek için döviz tutarının girildiği alandır. Girilen döviz tutarı, klavyede yer alan &lt;tab&gt; tuşu ile boş bırakıldığında, "Kur" ile "Döviz Tutarı" çarpılarak "Tutar" alanına aktarılır.</td>
</tr>
<tr>
<td colspan="1">Kur Farkı</td>
<td colspan="1">
<p>Dövizli işlem gören çeklerde, oluşacak kur farkı tutarlarının izlendiği alandır. Borç Çekleri → İşlemler → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253D24a919c4-6363-43c4-9bb7-5185eaf1797c%2526link%253D5f5e5880-142a-4a4d-8f93-1a78a1c58757%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Dövizli Çekler Kur Farkı Kaydı</a> bölümünün çalıştırılmasından sonra oluşan kur farkı tutarları, ilgili çeklerin "Kur Farkı" alanlarına otomatik olarak aktarılır. </p>
<p>Girilen tüm çek kayıtları, ekranın alt kısmında yer alan grid alandan izlenir. İzlenmesi istenen çekin üzerinde iken, farenin sol klik tuşu ile çift tıklandığında çek bilgilerinin ekranda görüntülenmesi sağlanır.</p>
</td>
</tr>
<tr>
<td>
<p>Kur</p>
</td>
<td>

<p>Girilen tarihteki kur kaydedilmişse, program tarafından otomatik olarak ekrana getirilir. İlgili tarihte kur bulunamaz ise, kur bilgisinin elle (manuel) girilmesi gerekir.</p>

Kur bilgilerinin girişi ile ilgili detaylı bilgi için; Döviz Takibi → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253D43d935ab-b337-49ad-a395-c2763747f27c%2526link%253D0ef5d6d8-458a-4e85-86f1-9cfe54fa7e3c%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Döviz Kurları Girişi</a>.

</td>
</tr>
<tr>
<td>Son İşlem Tipi</td>
<td>Cariye ait çek ile ilgili durum bilgisinin izlendiği alandır.</td>
</tr>
<tr>
<td>Son İşlem Tarihi</td>
<td>Çek ile ilgili son yapılan işlem tarihinin izlendiği alandır.</td>
</tr>
<tr>
<td>Ek Açıklama 1-2-3</td>
<td>Girişi yapılan çeke ait açıklama bilgisinin girildiği alanlardır.</td>
</tr>
<tr>
<td>

<p>Bordro Tamamlama</p>

</td>
<td>

<p>Portföye alınacak olan çek/çekler bordroya eklendikten sonra, mutlaka bordro tamamlama işleminin yapılması gerekir. Bordro tamamlama işlemi yapılmadan ekrandan çıkılırsa, kayıtlar cari hesaba ve entegrasyon havuzuna aktırılmaz.</p>
<p><img src="../../../../_assets/1742cad3b01a0d59a6fb.png"/></p>

<table>
<thead>
<tr>
<th>
<p>Bordro Tamamlama Ekranı</p>
</th>
<th> </th>
</tr>
</thead>
<tbody>
<tr>
<td>Açıklama Basılsın</td>
<td>"Bordro Basımı" seçeneğinin işaretlenmesi ile işlev kazanan seçenektir. çek girişinde yazılmış olan açıklamaların basılmasını sağlar. </td>
</tr>
<tr>
<td>Cari R.K. (Cari Rapor Kodu)</td>
<td>

<p>"Rapor Kodu" alanında olduğu gibi, raporlama amacıyla en fazla 15 karakter uzunluğunda kod bilgisi girilen alandır. Bilgi girişi yapılması için, Cari → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253D6f1c0005-6726-405d-8ac7-b213b41d23c7%2526link%253Dd50e5347-1966-4bcb-87c7-1d4897ae336e%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Cari Parametreleri</a> → “Hareketlerde Rapor Kodu Sorulsun” parametresinin işaretlenmesi gerekir.</p>
<p>Bordroya çek eklenirken de rapor kodu sorgulanır. <img src="../../../../_assets/c96e2b0d2c19eb0d52cc.png"/> butonuna basıldığında, bu alanın tekrar sorgulanmasındaki amaç; çeklerin her biri için ayrı ayrı rapor kodu girilmesi yerine, burada belirlenen rapor kodunun tüm çeklere aktarılmasının sağlanması içindir.</p>
<p>Bordroya ait çeklerle ilgili kayıt/düzeltme işlemleri bittiğinde, kayıtların entegre bölümlere işlenmesi için mutlaka<img src="../../../../_assets/c96e2b0d2c19eb0d52cc.png"/> butonu kullanılarak bordronun tamamlanması gerekir. Bordro tamamlama yapılmadan ekrandan çıkıldıktan sonra yeni bir çek alındı kaydı için tekrar giriş yapıldığında, tamamlanmamış bordrolarla ilgili bir pencere açılır. <img src="../../../../_assets/973111d004995dca0113.jpg"/>  butonuna tıklanarak işleme devam edilir ya da tamamlanmayan bordro seçilerek <img src="../../../../_assets/09045048d4760e152eff.png"/> butonuna basılır ve kayıt tamamlanır.</p>

</td>
</tr>
<tr>
<td>Adat Baz Tarihi</td>
<td>Adat hesaplaması için baz alınacak tarihin girildiği alandır. Bordro basımında yer alacak ortalama gün cari hesaplara bordro bazında toplu kayıt geçiliyorsa, cari hareket efektif tarihi bu tarih baz alınarak hesaplanır. Adat baz tarihi, günün tarihi olarak ekranda görüntülenir.</td>
</tr>
<tr>
<td>Özel Bordro Basımı</td>
<td>Bordro basımı için özel bir dizayn belirlenmişse, bordro dökümü almak için işaretlenmesi gereken seçenektir.</td>
</tr>
<tr>
<td>Çek Toplamı</td>
<td>Bordro içinde bulunan çeklerin toplam tutarının izlendiği alandır.</td>
</tr>
<tr>
<td>
<img src="../../../../_assets/973111d004995dca0113.jpg"/>
</td>
<td>Bordro tamamlama ekranında girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur.</td>
</tr>
<tr>
<td>
<img src="../../../../_assets/39d77b8716226638d9ce.jpg"/>
</td>
<td>

<p>Bordro tamamlamak için girilen bilgilerin kaydedilmesini sağlayan butondur. Yardımcı Programlar → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253Dd1958e00-2586-4b57-8a40-dc9812c969ad%2526link%253D2b164138-dbcc-4825-8c16-0ea06ff6c7d8%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Şirket-Şube Parametreleri</a><br/>
						→ "Döviz Uygulaması Var" parametresinin işaretli olduğu ve cari hesapların döviz bilgileri ile takip edildiği durumlarda, <img src="../../../../_assets/39d77b8716226638d9ce.jpg"/> butonuna basılmasıyla birlikte döviz bilgilerinin girileceği bir pencere ekrana gelir.</p>
<p><img src="../../../../_assets/054e6fed03334e25aefc.png"/></p>
<p>Girilen çek dövizli ise, çek bilgilerinin toplam tutarının cari hesaplara döviz değerleri ile aktarılması için yukarıdaki ekranda yer alan sahaların doldurulması gerekir. Program, çeklerin toplam TL değerini, girilen kur tutarına bölerek hesapladığı döviz tutarını, cari hesap hareketlerindeki "Döviz Tutarı" alanına aktarır. Girilen döviz bilgileri, çeklerin tutar değerlerini oluşturmaz veya herhangi bir değişime neden olmaz. Sadece, ilgili carinin döviz raporları için "Döviz Tutarı" alanına aktarılır.</p>

</td>
</tr>
<tr>
<td>Bordro Basımı</td>
<td>Bordrodaki tamamlanan çeklerim yazıcıdan dökümünün almak için işaretlenmesi gereken seçenektir.</td>
</tr>
<tr>
<td>Parçalama Yapılsın</td>
<td>

<p>Firmada cari kaydı bulunan bünyeye bağlı kuruluşların birinden alınan çek/çeklerin, bünye içindeki diğer firmaların borçlarına mahsuben dağıtılmasını sağlayan seçenektir.</p>
<p><img src="../../../../_assets/09d5c8a578dcf7282233.png"/></p>
<p><strong>Örneğin;</strong></p>
<p>A, B ve C firması adı altında üç ayrı firmayla çalışıldığı varsayıldığında:</p>
<p>A firmasına verilen 2.200 TL tutarındaki çeklerin, 1.000 TL kadarı B firmasının alacağına mahsuben, 1.200 TL kadarı ise C firmasının alacağına mahsuben verildiği zaman</p>
<p>A firması için: 0</p>
<p>B firması için: 1.000 TL</p>
<p>C firması için: 1.200 TL dağıtım yapılması gerekir.</p>
						Parçalama işleminin yapılması için bordroda bulunan tüm çeklerin döviz tiplerinin aynı olması gerekir.
</td>
</tr>
<tr>
<td>R.K. (Rapor Kodu)</td>
<td>

<p>Kaydedilen çeklerin, raporlara yönelik olarak tek kod altında toplanması için en fazla 1 karakter uzunluğunda, isteğe göre kayıt oluşturulan alandır.</p>
<p><strong>Örneğin;</strong></p>
<p>Çekin düzenlendiği yere göre gruplar oluşturulduktan sonra, rapor koduna göre liste alınabilir.</p>
<p>Bordroya çek eklenirken de rapor kodu sorgulanır. <img src="../../../../_assets/c96e2b0d2c19eb0d52cc.png"/> butonuna basıldığında, bu alanın tekrar sorgulanmasındaki amaç; çeklerin her biri için ayrı ayrı rapor kodu girilmesi yerine, burada belirlenen rapor kodunun tüm çeklere aktarılmasının sağlanması içindir.</p>

</td>
</tr>
<tr>
<td>
<p>Cari/Muhasebeye Kayıt Yapılacak Mı<strong> </strong></p>
</td>
<td>
<p>Tamamlanan bordro ile ilgili cari hesap hareket ve entegrasyon kayıtlarının oluşturulması istendiğinde işaretlenmesi gereken seçenektir. Böylece, bordro içinde geriye dönük gerekli düzenlemeler yapılarak tekrar bordro tamamlama ile entegre kayıtların gerçekleşmesi sağlanır.</p>
</td>
</tr>
</tbody>
</table>

</td>
</tr>
</tbody>
</table>

**Özel Hesap Kapatma**

Cari Hesapları özel hesap kapatma sistemine göre takip eden kullanıcılar için bordronun tamamlanmasından sonra hesap kapatma penceresi ekrana gelir. Müşteriye ait kapatılmamış olan borç ve alacak kayıtları hesap kapatma ekranında listelenir. İlgili borç ve alacak hareketleri işaretlendikten sonra **![](../../../../_assets/fedfbf27471a0c9a288c.png)** butonuna basılarak hesap kapatma işlemi gerçekleştirilir.

Herhangi bir durumda özel hesap kapatmayla ilgili yapılan bir yanlışın Cari → Kayıt → Özel Hesap Kapatma bölümünden düzeltme/değiştirme/izleme işlemi yapılabilir.

> [!NOTE]
> Özel Hesap Kapatma işlemi ile ilgili detay bilgi için; Cari → Kayıt → [Özel Hesap Kapatma](<../../Cari/Kayıt - Cari/Özel Hesap Kapatma/index.md>)

İlgili alanlara bilgi girişi yapıldıktan sonra "Kaydet" ![](../../../../_assets/865524a70e225c89c107.jpg) butonuna basılarak kayıt oluşturulur.

Kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.

> [!NOTE]
> Cari Hesaba Senet Girişinde Kullanılan Özel Tuşların kullanımı, "Müşteri Çekleri" modülünde yer alan "Devir Çek Girişi Özel Tuşları" ile aynı işleve sahiptir. Detaylı bilgi için; Müşteri Çekleri → Kayıt → [Devir Çek Girişinde Kullanılan Özel Tuşlar](<../../Müşteri Çekleri/Kayıt - Müşteri Çekleri/Devir Çek Girişi/Devir Çek Girişinde Kullanılan Özel Tuşlar.md>)
