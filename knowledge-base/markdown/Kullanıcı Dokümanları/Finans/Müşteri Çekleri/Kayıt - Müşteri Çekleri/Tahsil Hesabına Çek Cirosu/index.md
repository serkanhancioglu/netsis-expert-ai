---
title: "Tahsil Hesabına Çek Cirosu"
page_id: "22806514"
product: "netsis-3-enterprise"
depth: 5
is_section: true
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Müşteri Çekleri"
  - "Kayıt / Müşteri Çekleri"
  - "Tahsil Hesabına Çek Cirosu"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Müşteri Çekleri / Kayıt / Müşteri Çekleri / Tahsil Hesabına Çek Cirosu"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTk1MTQ2YTJlLTliOTUtNDFlMi1iZmFhLWM4ODI4NjliMDgxZiZsaW5rPTEzMmE5M2QwLTJhYTctNDM0NS1iMWU1LTA3MzhkZWYxMTY2ZSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=95146a2e-9b95-41e2-bfaa-c882869b081f&link=132a93d0-2aa7-4345-b1e5-0738def1166e&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "tahsil-hesabina-cek-cirosu_34210638_22806514.html"
source_version: "2022-09-19T14:49:49.067+03:00"
source_bytes: 167239
fetched_at: "2026-09-13T04:11:03+00:00"
generator: "netsis-scraper 1.0.0"
---
# Tahsil Hesabına Çek Cirosu

Tahsil hesabına çek cirosu, Finans Bölümü'nde, Kayıt/Müşteri Çekleri menüsünün altında yer alır. Tanımlanan tahsil hesabına çeklerin ciro edilmesi için kullanılan bölümdür.

![](../../../../../_assets/fcea3d0c99759540d288.png)

Tahsil hesabına çek cirosu ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

<table>

<tbody>
<tr>
<th>Tahsil Hesabına Çek Cirosu Ekranı</th>
<th> </th>
</tr>
<tr>
<td>
<p>Verildi Bordro No</p>
</td>
<td>
<p>Satıcıya aynı gün içinde verilen, tahsil ve teminata çıkılan bir veya birden fazla çekin tek bir numara altında toplanmasını sağlar.  "Verildi Bordro Numaraları" da, "Alındı Bordro Numaraları" alanında olduğu gibi program tarafından başlatılır ve bir sayı artarak sıra oluşturur. Rehber butonu <img src="../../../../../_assets/088477bb321d1b20c939.jpg"/> ile bordro numaralarına ulaşılır.</p>

<p>Verildi Bordro numarasının başlangıç numarası değişikliği, Müşteri Çekleri → İşlemler → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253De3efecc9-cb95-4597-94f0-27d35227fdb7%2526link%253Dad80d8a6-8a85-4d6d-bc42-e831b5bac740%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Çek Numarası Değişikliği</a> bölümünden yapılır. Program diğer modüllerle entegre kullanılmaya başlandığında (cari hesaplarda kayıtlı müşterilere çek ciro edildiğinde ve bankaya tahsilata/teminata çıkışlarda)" Verildi Bordro Numarası" otomatik olarak aktarılır ve çeklerin ilgili alanlarına kaydedilir. </p>

<p>Bir veya birden fazla çek, tek bir verildi bordro numarası altında kaydedildikten sonra, bu bordro numarasına ait çeklerin kayıtlarının bittiğine dair bilgisayara bilgi vermek ve entegre bölümlere (Cari, Muhasebe) çeklerin işlenmesi açısından Bordro Tamamlama işleminin yapılması gerekir. Bir "Verildi Bordrosuna" ait çekler, işlem ekranından çıkmadan arka arkaya kaydedilebilir.</p>
<p>Tamamlanmayan herhangi bir bordroya yeni bir çek kaydının eklenmesi istendiğinde, bordro numarası değiştirilerek (istenen numara ekrana getirtilerek) çek kayıtlarına devam edilir. Verildi bordro numarası ile kaydedilen çeklerin, bu işlemden sonra toplu izleme/iptal etme  (Müşteri Çekleri → İşlemler → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253D2e84e0af-237f-4a65-9249-42f18242882f%2526link%253D0f37b144-47d2-48ae-933a-c67fdb1b1f8a%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Toplu Çıkış İptali</a>) olanağı bulunur.</p>
</td>
</tr>
<tr>
<td>
<p>Çıkış Tarihi<strong> </strong></p>
</td>
<td>

<p>Satıcıya ciro edilen çeklerin (portföydeki çeklerin) şirket tarafından satıcıya ciro edildiği tarihtir. Çıkış tarihi sistem tarihi üzerinden otomatik olarak ekrana gelir ve üzerinde değişiklik yapılabilir. Çıkış tarihi, giriş tarihinden küçük bir tarih olamaz.</p>

</td>
</tr>
<tr>
<td>
<p>Verilen Kodu</p>
</td>
<td>

<p>Çeklerin tahsil hesabına çıkması için kullanılan üç farklı yöntem şunlardır:</p>
<ul>
<li>Banka Hesapları; Cari Modülde tüm tahsil hesapları cari kart gibi açılabilir.</li>
<li>Muhasebe hesap planındaki hesaplar kullanılabilir.</li>
<li>Banka Modülünde tüm tahsil hesaplarına kart açılabilir.</li>
</ul>
<p>Bu işlemler parametre tanımlarına göre değişkenlik gösterir.</p>
<p>Banka → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253De6722a7d-ee45-435b-842e-3be02ba0940e%2526link%253D4addcde3-ed2c-4e1e-baf1-93c5b5ebbd2e%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Banka Genel Parametreleri</a> → "Banka Entegre" parametresinin işaretlendiği durumlarda, "Verilen Kodu" alanının yanında yer alan rehber butonuna <img src="../../../../../_assets/088477bb321d1b20c939.jpg"/> basıldığında, "Banka Hesap Kodu Rehberi" ekrana gelir. Rehberde, Banka Modülünde hesap tipi olarak "Tahsil Çekleri Hesabı" seçilerek tanımlanan banka kodları ter alır.</p>
<p>Parametre işaretlenmediğinde, "Verilen Kodu" alanının yanında yer alan rehber butonuna <img src="../../../../../_assets/088477bb321d1b20c939.jpg"/> basıldığında, "Cari Hesap Rehberi" ekrana gelir. Böyle bir durumda, banka tahsil hesaplarının cari kart olarak açılması gerekir.</p>
<p>Müşteri Çekleri → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253D80c77c17-6da1-4893-9694-5a72cec2e329%2526link%253D8e0a690f-a720-4f1c-8d6a-4f1498ee422f%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Müşteri Çekleri Parametreleri</a> → "Tahsil/Teminata Çıkış Cariden" parametresi işaretli değilse, "Verilen Kodu" alanının yanında yer alan rehber butonuna <img src="../../../../../_assets/088477bb321d1b20c939.jpg"/> basıldığında, "Muhasebe Hesap Rehberi" ekrana gelir.</p>

</td>
</tr>
<tr>
<td>
<p>Çek No</p>
</td>
<td>

<p>Tahsil hesabına gönderilmek üzere, verildi bordrosuna eklenecek çek numarasının girildiği alandır. Rehber butonu <img src="../../../../../_assets/088477bb321d1b20c939.jpg"/> ile, kayıtlı çek numaralarına ulaşılır.</p>
<p>Çek rehberi kullanımı ile ilgili detaylı bilgi için; Finans → Müşteri Çekleri → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253D284b2d90-e40f-4bd5-8c6f-b03b4cf23dae%2526link%253De96ad9e4-d0ed-46a9-b54b-478e56686403%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Ek-1 (Çek/Senet No Rehberi Kullanımı)</a>.</p>
<p>Alan üzerinde iken, çek numarası girildiğinde ya da rehberden bir çek seçildiğinde, "Portföyde olan bu kayıt, otomatik olarak bu bordroya eklenecektir." şeklinde bir uyarı ekrana gelir. Seçilen çekin, verildi bordrosuna eklenerek ciro edilmesi istendiğinde bu uyarının onaylanması gerekir.</p>
<p>Seçilen çek, verildi bordrosuna eklendiğinde, çek için "Cari Hesap Çek Alındı Kaydı" bölümünden girilen Rapor Kodu, Rapor Kodu, Cari Rapor Kodu, Proje Kodu, Alındı Bordro No, Giriş Tarihi, Verenin Kodu, Vade Tarihi, Ödeme Tarihi, Ciro Eden, Asıl Borçlu, Plasiyer Kodu, Çekin Bankası, Tutar gibi bilgiler, program tarafından otomatik olarak verildi bordrosuna aktarılır. Bu bilgiler üzerinde değişiklik yapılması istendiğinde, Dekont → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253D20de7d77-d83d-45aa-9d57-f987d5049b71%2526link%253D8388c1e5-7b1a-4a58-91ef-9290e3bf92dd%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Çek/Senet Düzeltme Dekontu</a> bölümünün kullanılması gerekir. İlgili çek, verildi bordrosundan çıkarılarak ve "Cari Hesap Çek Alındı Kaydı" bölümünde ekrana getirilerek de değişiklik yapılabilir.</p>

</td>
</tr>
<tr>
<td colspan="1">
<p>Rapor Kodu</p>
</td>
<td colspan="1">
<p>Kaydedilen çeklerin, raporlamaya yönelik bir kod altında toplanması için, 1 karakter uzunluğunda isteğe göre kayıt oluşturulmasını sağlayan alandır.</p>
<p><strong>Örneğin; </strong>Çeklerin bankasına göre gruplar oluşturulduktan sonra, rapor koduna göre liste alınabilir.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>Cari Rapor Kodu</p>
</td>
<td colspan="1">
<p>Cari → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253D6f1c0005-6726-405d-8ac7-b213b41d23c7%2526link%253Dd50e5347-1966-4bcb-87c7-1d4897ae336e%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Cari Parametreleri</a> → “Hareketlerde Rapor Kodu Sorulsun” parametresinin işaretli olması halinde, "Rapor Kodu" alanında olduğu gibi raporlama amacıyla en fazla 15 karakter uzunluğunda kod girilen alandır.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>Proje Kodu</p>
</td>
<td colspan="1">

<p>Yardımcı Programlar → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253Df7baa628-4b9a-47cb-8f22-03aabde76c1e%2526link%253D8f91f576-27e0-4eea-a0f1-71be7d79c366%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Şirket-Şube Parametre Tanımları</a> → “Proje Uygulaması Var" seçeneğinin işaretlenmesi ile aktif hale gelen alandır. Proje uygulamasında, çeklerdeki her türlü giriş/çıkış işlemlerinde proje kodu sorgulanır ve boş bırakılmaz. Cari hareketlerde ve entegre havuzunda ise, kayıtlar proje kodu bazında tek tek oluşur. Rehber butonu <img src="../../../../../_assets/088477bb321d1b20c939.jpg"/> ile proje kodlarına ulaşılır.</p>

</td>
</tr>
<tr>
<td colspan="1">
<p>Alındı Bordro No</p>
</td>
<td colspan="1">

<p>Müşteriden aynı gün içinde alınan bir veya birden fazla adette, aynı makbuza ait çeklerin tek bir (aynı) numara altında toplanmasını sağlayan sisteme bordro denir. Çeklerin bordrolar altında takibi, raporlamada ve toplu çıkış gibi işlemlerde kolaylık sağlar. "Bordro Numarası" program tarafından otomatik olarak başlatılır. Program, bu numarayı her (yeni) giriş/çıkış makbuzunda bir sayı arttırarak sıra oluşturur.</p>
<p>Bordro numaralarının başlangıç numarası üzerinde herhangi bir değişiklik yapmak için; Müşteri Çekleri → İşlemler → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253De3efecc9-cb95-4597-94f0-27d35227fdb7%2526link%253Dad80d8a6-8a85-4d6d-bc42-e831b5bac740%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Çek Numarası Değişikliği</a> Müşteriden yeni alınan çeklerin kaydı sırasında (portföye çek kaydı) program tarafından otomatik olarak ekrana getirilen "Alındı Bordro Numarası" ile kayıt yapma olanağı bulunur. Bu numarada yapılacak değişiklikler, programın işleyişinde bazı karışıklıklara neden olacağı için dikkatli olunması gerekir. Değişiklik yapılacak bordro numarasının, daha önceden kaydedilen çeklerin hiçbirinde yer almaması (bordro numaralarının boş olması) gerekir.</p>
<p>Bir makbuza (bordro) ait tek bir çek varsa bir adet çekin, birden fazla çek varsa (çekler arka arkaya girilerek) söz konusu çeklerin aynı alındı bordro numarasına aktarılması sağlanır. Alındı bordrosu tamamlanarak işlem ekranından çıkılıp tekrar girildiğinde, yeni bordro numarası program tarafından son kalınan numaradan bir sayı arttırılarak devam eder. Daha önceden kaydı yapılan herhangi bir bordroya yeni bir çek kaydının eklenmesi istendiğinde, bordro numarası ilgili alana tekrar girilerek çek kayıtlarına devam edilir. Bu işlemden sonra, "Alındı Bordro Numarası" ile kaydedilen çeklerin toplu izleme/iptal etme olanağı bulunur.</p>
<p>Bir veya birden fazla çeki tek alındı bordro numarası altında kaydettikten sonra, bu bordro numarasına ait çek kayıtlarının bittiğine dair sisteme bilgi vermek ve entegre bölümlere (cari, muhasebe) çeklerin işlenmesi açısından mutlaka <strong>Bordro Tamamlama</strong> işleminin yapılması gerekir.</p>
<p>Birden fazla çekin bulunduğu alındı bordrosunda tek bir çekin düzeltme/iptal işlemi söz konusu olduğunda, alındı bordro numarası girilerek daha önce kaydedilen bordroya erişilir ve ilgili çek grid alanı kullanılarak ekrana getirilir. Düzeltme/ iptal (F7) işlemi yapıldıktan sonra, sonucun diğer modüllere yansıması için <strong>Bordro Tamamlama</strong> işlemi yapılır.</p>
<p>Bir çek üzerinde düzeltme/iptal işlemi yapılması için, ilgili çekin portföyde bulunması gerekir. Ciro edilmiş çekler üzerinde düzeltme/iptal işlemi yapılmaz.</p>

</td>
</tr>
<tr>
<td colspan="1">
<p>Giriş Tarihi</p>
</td>
<td colspan="1">
<p>Kaydedilen çeklerin şirkete giriş tarihinin girildiği alandır. Giriş tarihi sistem tarihinden otomatik olarak aktarılır ve üzerinde istenen değişiklik yapılabilir. "<a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253Dbb76af85-b688-44bb-8be0-bf6d100f3ce1%2526link%253D7145715d-75db-4948-9235-8fcb323757fe%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Cari Hesap Çek Alındı Kaydı</a>" bölümünden çek girişi yapıldıktan sonra değiştirilmesine izin verilmeyen tek alan çekin/çeklerin giriş tarihleridir. Giriş tarihinde bir hata yapılması durumunda, Müşteri Çekleri → İşlemler → Toplu Giriş İptali işlemi ile bordronun tamamen iptal edilerek tekrar girilmesi gerekir.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>Verenin Kodu</p>
</td>
<td colspan="1">

<p>Çeki veren müşterinin cari hesap kodunun girildiği alandır. Rehber butonu <img src="../../../../../_assets/088477bb321d1b20c939.jpg"/> ile cari hesap kodlarına ulaşılır. Girilecek kodun, Cari → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253D42a33a34-474e-48d9-abe6-d840af3abda4%2526link%253Dc595a1fa-5e62-4e0c-ac6e-20f7004074f8%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Cari Hesap Kayıtları</a> bölümünde önceden tanımlanmış olması gerekir. </p>

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
<p>Vade tarihi itibariyle çekin opsiyonlu ödenme tarihinin girildiği alandır. Çekin kaydı sırasında, ödeme tarihi vade tarihiyle aynı kaydedilir. Dekonttan ödendi işlemi yapıldığında, dekontun işlendiği tarih aktarılır ve değiştirilir.</p>
<p><strong>Örneğin; </strong>Firmanın, farklı şehirlerdeki (uzak iller için) çekinin gerçek tahsil günü ya da tatil günlerine denk gelen tarihlerdeki gerçek tahsil tarihi program tarafından (dekontlardan işlem yapıldığında) bu alana kaydedilerek, çeklerle ilgili raporların kaydedilen tarihe göre listelenmesi sağlanır.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>Ciro Eden</p>
</td>
<td colspan="1">
<p>Kaydedilen çek "Asıl" ise (çeki veren kişinin kendi çekiyse), program otomatik olarak alanı boş bırakır. Çek "Ciro" ise (çeki veren kişinin kendi çekleri değilse) çeki verenin ismi program tarafından otomatik olarak aktarılır.</p>
</td>
</tr>
<tr>
<td>
<p>Asıl/Ciro</p>
</td>
<td>
<p>Kaydedilen çek müşterinin kendi çeki ise "Asıl", veren kişiye ciro edilmiş ise (asıl borçlusu veren kişiden farklı bir kişi ise), "Ciro" seçeneğinin işaretlendiği alandır. Müşteriden gelen ciro çeklerin karşılıksız çıkma durumunda çekin asıl borçlusu kara liste kayıtlarına aktarılır. Diğer durumlarda asıl borçlusu çeki veren kişi ise, bu müşteri kara liste kaydına alınır.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>Asıl Borçlu </p>
</td>
<td colspan="1">
<p>Kaydedilen çek "Asıl" ise, veren kişinin ismi bu alana program tarafından otomatik olarak aktarılır ve bu alana bilgi girilmesine izin verilmez. Çek "Ciro" ise (veren kişinin kendi çekleri değilse) asıl borçlusunun ismi yazılır. Asıl borçlusu da cari hesaplarda kayıtlı ise, asıl borçlunun cari kodu girilir.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>Çekin Bankası</p>
</td>
<td colspan="1">

<p>Çekin hangi bankanın çeki olduğu ile ilgili bilgi girişi yapılan alandır. Raporlamaya yöneliktir. İleride, erişim açısından banka isimlerini verirken kayıt standartlarına uyulması gerekir. Çeklerle ilgili işlem ve raporlamalarda, çeklerin listesi ekranda görüntülenir ve bu çeklerden istenen bir çek üzerine gelip fare ile tıklandığında, seçilen çek işlem görür. Böyle durumlarda, çekin bankası, çeklerin seçilmesinde önem kazanır. Alanın sağ tarafında yer alan aşağı ok butonu ile, kayıtlı banka isimlerine erişilir. Rehber butonu <img src="../../../../../_assets/088477bb321d1b20c939.jpg"/> ile banka kodlarına ulaşılır.</p>

</td>
</tr>
<tr>
<td colspan="1">
<p>Tutar</p>
</td>
<td colspan="1">
<p>Kaydedilen çeklerin Türk Lirası olarak tutarıdır. Bir bordrodaki toplam çek adedi ve tutarı, ekranın alt bölümünde yer alan gri renkli alanda bilgi olarak verilir.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>Döviz Tipi/Kur/Döviz Tutarı</p>
</td>
<td colspan="1">

<p>Müşteri Çekleri → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253D80c77c17-6da1-4893-9694-5a72cec2e329%2526link%253D8e0a690f-a720-4f1c-8d6a-4f1498ee422f%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Müşteri Çekleri Parametreleri</a> → “Döviz Uygulaması Var” parametresinin işaretlendiği durumlarda çek tutarı bilgisi girilmeden önce, ilgili çekin döviz tipi, döviz tipinin işlem birimi ve kur tarihi sorgulanır.</p>
<img src="../../../../../_assets/1e8d6338e56da5432ff0.png"/>
<p>Girilen tarihe göre günlük kur (Döviz Tipi alanına bilgi girişi yapıldıktan sonra) ilgili alana otomatik olarak gelir. Ekrana gelen kur değeri üzerinde değişiklik yapılabilir. Aynı ekranda sorgulanan "Tutar" alanına çekin döviz tutarı girilir. Program, kur değeri ile döviz tutarını çarpıp TL değerini hesaplayarak "Çek Tutarı" alanına aktarır. Çeklerin girilen döviz bilgileri ve döviz tipi; kur ve döviz tutarı alanlarından izlenir. Döviz bilgileri, girilen her çek için ayrı ayrı sorgulanır. TL olan çekler için döviz bilgileri ekranı herhangi bir değer verilmeden boş bırakılır.</p>

</td>
</tr>
<tr>
<td colspan="1">Son İşlem Tipi</td>
<td colspan="1">Cariye ait çek ile ilgili durum bilgisinin izlendiği alandır.</td>
</tr>
<tr>
<td colspan="1">Son İşlem Tarihi</td>
<td colspan="1">Çek ile ilgili son yapılan işlem tarihinin izlendiği alandır.</td>
</tr>
<tr>
<td colspan="1">

<p>Bordro Tamamlama</p>

</td>
<td colspan="1">

<p>Portföye alınacak olan çek/çekler bordroya eklendikten sonra, mutlaka bordro tamamlama işleminin yapılması gerekir. Bordro tamamlama işlemi yapılmadan ekrandan çıkışırsa, kayıtlar cari hesaba ve entegrasyon havuzuna aktırılmaz.</p>
<p><img src="../../../../../_assets/c67f632f990c944d9cb3.png"/></p>

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
<td>Çek Toplamı</td>
<td>Bordro içinde bulunan çeklerin toplam tutarının izlendiği alandır.</td>
</tr>
<tr>
<td>Adat Baz Tarihi</td>
<td>Adat hesaplaması için baz alınacak tarihin girildiği alandır. Bordro basımında yer alacak ortalama gün cari hesaplara bordro bazında toplu kayıt geçiliyorsa, cari hareket efektif tarihi bu tarih baz alınarak hesaplanır. Adat baz tarihi, günün tarihi olarak ekranda görüntülenir.</td>
</tr>
<tr>
<td>Bordro Basımı</td>
<td>Bordrodaki tamamlanan çeklerin yazıcıdan dökümünün almak için işaretlenmesi gereken seçenektir.</td>
</tr>
<tr>
<td>Özel Bordro Basımı</td>
<td>Bordro basımı için özel bir dizayn belirlenmişse, bordro dökümü almak için işaretlenmesi gereken seçenektir.</td>
</tr>
<tr>
<td>Açıklama Basılsın</td>
<td>"Bordro Basımı" seçeneğinin işaretlenmesi ile işlev kazanan seçenektir. Çek girişinde yazılmış olan açıklamaların basılmasını sağlar. </td>
</tr>
<tr>
<td>
<p>Cari/Muhasebeye Kayıt Yapılacak Mı<strong> </strong></p>
</td>
<td>
<p>Tamamlanan bordro ile ilgili cari hesap hareket ve entegrasyon kayıtlarının oluşturulması istendiğinde işaretlenmesi gereken seçenektir. Böylece, bordro içinde geriye dönük gerekli düzenlemeler yapılarak tekrar bordro tamamlama ile entegre kayıtların gerçekleşmesi sağlanır.</p>
</td>
</tr>
<tr>
<td>Parçalama Yapılsın</td>
<td>Firmada cari kaydı bulunan bünyeye bağlı kuruluşların birinden alınan çek/çeklerin, bünye içindeki diğer firmaların borçlarına mahsuben dağıtılmasını sağlayan seçenektir.</td>
</tr>
<tr>
<td colspan="1">R.K. (Rapor Kodu)</td>
<td colspan="1">

<p>Kaydedilen çeklerin, raporlara yönelik olarak tek kod altında toplanması için en fazla 1 karakter uzunluğunda, isteğe göre kayıt oluşturulan alandır.</p>
<p><strong>Örneğin;</strong></p>
<p>Çeklerin bankasına göre gruplar oluşturulduktan sonra, rapor koduna göre liste alınabilir.</p>
<p>Bordroya çek eklenirken de rapor kodu sorgulanır. Bordro Tamamlama butonuna basıldığında, bu alanın tekrar sorgulanmasındaki amaç; çeklerin her biri için ayrı ayrı rapor kodu girilmesi yerine, burada belirlenen rapor kodunun tüm çeklere aktarılmasının sağlanması içindir.</p>

</td>
</tr>
<tr>
<td colspan="1">Cari R.K. (Cari Rapor Kodu)</td>
<td colspan="1">

<p>"Rapor Kodu" alanında olduğu gibi, raporlama amacıyla en fazla 15 karakter uzunluğunda kod bilgisi girilen alandır. Bilgi girişi yapılması için, Cari → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253D6f1c0005-6726-405d-8ac7-b213b41d23c7%2526link%253Dd50e5347-1966-4bcb-87c7-1d4897ae336e%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Cari Parametreleri</a> → “Hareketlerde Rapor Kodu Sorulsun” parametresinin işaretlenmesi gerekir.</p>
<p>Bordroya çek eklenirken de rapor kodu sorgulanır. Bordro Tamamlama butonuna basıldığında, bu alanın tekrar sorgulanmasındaki amaç; çeklerin her biri için ayrı ayrı rapor kodu girilmesi yerine, burada belirlenen rapor kodunun tüm çeklere aktarılmasının sağlanması içindir.</p>
<p>Bordroya ait çeklerle ilgili kayıt/düzeltme işlemleri bittiğinde, kayıtların entegre bölümlere işlenmesi için mutlaka Bordro Tamamlama butonu kullanılarak bordronun tamamlanması gerekir. Bordro tamamlama yapılmadan ekrandan çıkıldıktan sonra yeni bir çek alındı kaydı için tekrar giriş yapıldığında, tamamlanmamış bordrolarla ilgili bir pencere açılır. İptal butonuna tıklanarak işleme devam edilir ya da tamamlanmayan bordro seçilerek Bordro Tamamlama butonuna basılır ve kayıt tamamlanır.</p>

</td>
</tr>
<tr>
<td colspan="1">
Tamam
</td>
<td colspan="1">

<p>Bordro tamamlamak için girilen bilgilerin kaydedilmesini sağlayan butondur. Yardımcı Programlar → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253Dd1958e00-2586-4b57-8a40-dc9812c969ad%2526link%253D2b164138-dbcc-4825-8c16-0ea06ff6c7d8%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Şirket-Şube Parametreleri</a> → "Döviz Uygulaması Var" parametresinin işaretli olduğu ve cari hesapların döviz bilgileri ile takip edildiği durumlarda, Tamam butonuna basılmasıyla birlikte döviz bilgilerinin girileceği bir pencere ekrana gelir.</p>
<p><img src="../../../../../_assets/054e6fed03334e25aefc.png"/></p>
<p>Girilen çek dövizli ise, çek bilgilerinin toplam tutarının cari hesaplara döviz değerleri ile aktarılması için yukarıdaki ekranda yer alan sahaların doldurulması gerekir. Program, çeklerin toplam TL değerini, girilen kur tutarına bölerek hesapladığı döviz tutarını, cari hesap hareketlerindeki "Döviz Tutarı" alanına aktarır. Girilen döviz bilgileri, çeklerin tutar değerlerini oluşturmaz veya herhangi bir değişime neden olmaz. Sadece, ilgili carinin döviz raporları için "Döviz Tutarı" alanına aktarılır.</p>

</td>
</tr>
<tr>
<td colspan="1">
İptal
</td>
<td colspan="1">Bordro tamamlama ekranında girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur.</td>
</tr>
</tbody>
</table>

</td>
</tr>
</tbody>
</table>
