---
title: "Cari Hesap Çek Alındı Kaydı"
page_id: "22806499"
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
  - "Cari Hesap Çek Alındı Kaydı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Müşteri Çekleri / Kayıt / Müşteri Çekleri / Cari Hesap Çek Alındı Kaydı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWJiNzZhZjg1LWI2ODgtNDRiYi04YmUwLWJmNmQxMDBmM2NlMSZsaW5rPTcxNDU3MTVkLTc1ZGItNDk0OC05MjM1LThmY2IzMjM3NTdmZSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=bb76af85-b688-44bb-8be0-bf6d100f3ce1&link=7145715d-75db-4948-9235-8fcb323757fe&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "cari-hesap-cek-alindi-kaydi_34210507_22806499.html"
source_version: "2022-11-15T14:27:35.057+03:00"
source_bytes: 113036
fetched_at: "2026-09-13T04:11:01+00:00"
generator: "netsis-scraper 1.0.0"
---
# Cari Hesap Çek Alındı Kaydı

Cari hesap çek alındı kaydı, Finans Bölümü'nde Kayıt/Müşteri Çekleri menüsünün altında yer alır. Müşterilerden alınan çek kayıtlarının yapıldığı bölümdür. Cari hesap çek alındı kaydı bölümünde girilen kayıtlar diğer modüllerle de entegre olduğu için, cari hesaplarda ve entegre havuzunda da kayıt oluşur.

Cari hesap çek alındı kaydı ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

<table>

<tbody>
<tr>
<th>Cari Hesap Çek Alındı Kaydı Ekranı</th>
<th> </th>
</tr>
<tr>
<td>
<p>Çek No<strong> </strong></p>
</td>
<td>

<p>Çek kaydı sırasında program tarafından sıradaki çek numarasının otomatik olarak ekrana getirildiği alandır. Daha önceden kaydedilmiş çeke ait numara girilerek, kayıtlı çekin ekrana getirilmesi sağlanır. Rehber butonu <img src="../../../../../_assets/088477bb321d1b20c939.jpg"/> ile kayıtlı çeklere ulaşılır.</p>

</td>
</tr>
<tr>
<td>
<p>Alındı Bordro No</p>
</td>
<td>

<p>Müşteriden aynı gün içinde alınan bir veya birden fazla adette, aynı makbuza ait çeklerin tek bir (aynı) numara altında toplanmasını sağlayan sisteme bordro denir. Çeklerin bordrolar altında takibi, raporlamada ve toplu çıkış gibi işlemlerde kolaylık sağlar. Bordro Numarası program tarafından otomatik olarak başlatılır. Program, bu numarayı her (yeni) giriş/çıkış makbuzunda bir sayı arttırarak sıra oluşturur.</p>
<p>Bordro numaralarının başlangıç numarası üzerinde herhangi bir değişiklik yapmak için; Müşteri Çekleri → İşlemler → Çek Numarası Değişikliği</p>
<p>Müşteriden yeni alınan çeklerin kaydı sırasında (portföye çek kaydı) program tarafından otomatik olarak ekrana getirilen Alındı Bordro Numarası ile kayıt yapma olanağı bulunur. Bu numarada yapılacak değişiklikler, programın işleyişinde bazı karışıklıklara neden olacağı için dikkatli olunması gerekir. Değişiklik yapılacak bordro numarasının, daha önceden kaydedilen çeklerin hiçbirinde yer almaması (bordro numaralarının boş olması) gerekir.</p>
<p>Bir makbuza (bordro) ait tek bir çek varsa bir adet çekin, birden fazla çek varsa (çekler arka arkaya girilerek) söz konusu çeklerin aynı alındı bordro numarasına aktarılması sağlanır. Alındı bordrosu tamamlanarak işlem ekranından çıkılıp tekrar girildiğinde, yeni bordro numarası program tarafından son kalınan numaradan bir sayı arttırılarak devam eder. Daha önceden kaydı yapılan herhangi bir bordroya yeni bir çek kaydının eklenmesi istendiğinde, bordro numarası ilgili alana tekrar girilerek çek kayıtlarına devam edilir. Bu işlemden sonra, Alındı Bordro Numarası ile kaydedilen çeklerin toplu izleme/iptal etme olanağı bulunur.</p>
<p>Bir veya birden fazla çeki tek alındı bordro numarası altında kaydettikten sonra, bu bordro numarasına ait çek kayıtlarının bittiğine dair sisteme bilgi vermek ve entegre bölümlere (cari, muhasebe) çeklerin işlenmesi açısından mutlaka <strong>Bordro Tamamlama</strong> işleminin yapılması gerekir.</p>
<p>Birden fazla çekin bulunduğu alındı bordrosunda tek bir çekin düzeltme/iptal işlemi söz konusu olduğunda, alındı bordro numarası girilerek daha önce kaydedilen bordroya erişilir ve ilgili çek grid alanı kullanılarak ekrana getirilir. Düzeltme/ iptal (F7) işlemi yapıldıktan sonra, sonucun diğer modüllere yansıması için <strong>Bordro Tamamlama</strong> işlemi yapılır.</p>
<p>Bir çek üzerinde düzeltme/iptal işlemi yapılması için, ilgili çekin portföyde bulunması gerekir. Ciro edilmiş çekler üzerinde düzeltme/iptal işlemi yapılmaz.</p>

</td>
</tr>
<tr>
<td>
<p>Giriş Tarihi</p>
</td>
<td>
<p>Kaydedilen çeklerin şirkete giriş tarihinin girildiği alandır. Giriş tarihi sistem tarihinden otomatik olarak aktarılır ve üzerinde istenen değişiklik yapılabilir. Cari Hesap Çek Alındı Kaydı bölümünden çek girişi yapıldıktan sonra değiştirilmesine izin verilmeyen tek alan çekin/çeklerin giriş tarihleridir. Giriş tarihinde bir hata yapılması durumunda, Müşteri Çekleri → İşlemler → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253D54e12603-4e64-4de0-a705-f91ceaf7d288%2526link%253D84365180-7cd6-438c-87a1-cf63ef61fbfb%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Toplu Giriş İptali</a> işlemi ile bordronun tamamen iptal edilerek tekrar girilmesi gerekir.</p>
</td>
</tr>
<tr>
<td>
<p>Verenin Kodu</p>
</td>
<td>

<p>Çeki veren müşterinin cari hesap kodunun girildiği alandır. Rehber butonu <img src="../../../../../_assets/088477bb321d1b20c939.jpg"/> ile, cari hesap kodlarına ulaşılır. Girilecek kodun, Cari → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253D42a33a34-474e-48d9-abe6-d840af3abda4%2526link%253Dc595a1fa-5e62-4e0c-ac6e-20f7004074f8%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Cari Hesap Kayıtları</a> bölümünde önceden tanımlanmış olması gerekir. </p>

</td>
</tr>
<tr>
<td>
<p>Asıl/Ciro</p>
</td>
<td>
<p>Kaydedilen çek müşterinin kendi çeki ise Asıl , veren kişiye ciro edilmiş ise (asıl borçlusu veren kişiden farklı bir kişi ise), Ciro seçeneğinin işaretlendiği alandır. Müşteriden gelen ciro çeklerin karşılıksız çıkma durumunda çekin asıl borçlusu kara liste kayıtlarına aktarılır. Diğer durumlarda asıl borçlusu çeki veren kişi ise, bu müşteri kara liste kaydına alınır.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>Asıl Borçlu<strong> </strong></p>
</td>
<td colspan="1">
<p>Kaydedilen çek Asıl ise, veren kişinin ismi bu alana program tarafından otomatik olarak aktarılır ve bu alana bilgi girilmesine izin verilmez. Çek Ciro ise (veren kişinin kendi çekleri değilse) asıl borçlusunun ismi yazılır. Asıl borçlusu da cari hesaplarda kayıtlı ise, asıl borçlunun cari kodu girilir. </p>
</td>
</tr>
<tr>
<td colspan="1">Asıl Borçlu T.C. Kimlik No</td>
<td colspan="1">Asıl borçlu T.C Kimlik Numarası'nın girildiği alandır. </td>
</tr>
<tr>
<td colspan="1">Asıl Borçlu Vergi Numarası</td>
<td colspan="1">Asıl Borçlu Vergi Numarası'nın girildiği alandır. </td>
</tr>
<tr>
<td colspan="1">
<p>Ciro Eden</p>
</td>
<td colspan="1">
<p>Kaydedilen çek Asıl ise (çeki veren kişinin kendi çekiyse), program otomatik olarak alanı boş bırakır. Çek Ciro ise (çeki veren kişinin kendi çekleri değilse) çeki verenin ismi program tarafından otomatik olarak aktarılır.</p>
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
<p>Cari → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253D6f1c0005-6726-405d-8ac7-b213b41d23c7%2526link%253Dd50e5347-1966-4bcb-87c7-1d4897ae336e%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Cari Parametreleri</a> → Hareketlerde Rapor Kodu Sorulsun parametresinin işaretli olması halinde, Rapor Kodu alanında olduğu gibi raporlama amacıyla en fazla 15 karakter uzunluğunda kod girilen alandır.</p>
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
<p>Vade tarihi itibariyle çekin opsiyonlu ödenme tarihinin girildiği alandır. Çek kaydı sırasında, ödeme tarihi vade tarihiyle aynı kaydedilir. Dekonttan ödendi işlemi yapıldığında, dekontun işlendiği tarih aktarılır ve değiştirilir.</p>
<p><strong>Örneğin;</strong></p>
<p>Firmanın, farklı şehirlerdeki (uzak iller için) çekinin gerçek tahsil günü ya da tatil günlerine denk gelen tarihlerdeki gerçek tahsil tarihi program tarafından (dekontlardan işlem yapıldığında) bu alana kaydedilerek, çeklerle ilgili raporların kaydedilen tarihe göre listelenmesi sağlanır.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>Yer Kodu</p>
</td>
<td colspan="1">
<p>Cari Hesap Çek Alındı Kaydı bölümünden girilen her çek için program tarafından otomatik olarak Portföy seçeneği işaretli olarak ekrana gelir<strong>. </strong> Üzerinde değişiklik yapılamaz.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>Çekin Bankası</p>
</td>
<td colspan="1">

<p>Çekin hangi bankanın çeki olduğu ile ilgili bilgi girişi yapılan alandır. Raporlamaya yöneliktir. İleride, erişim açısından banka isimlerini verirken kayıt standartlarına uyulması gerekir. Çeklerle ilgili işlem ve raporlamalarda, çeklerin listesi ekranda görüntülenir ve bu çeklerden istenen bir çek üzerine gelip fare ile tıklandığında, seçilen çek işlem görür. Böyle durumlarda, çekin bankası, çeklerin seçilmesinde önem kazanır. Alanın sağ tarafında yer alan aşağı ok butonu ile, kayıtlı banka isimlerine erişilir. Rehber butonu <img src="../../../../../_assets/088477bb321d1b20c939.jpg"/> ile, banka kodlarına ulaşılır.</p>

</td>
</tr>
<tr>
<td colspan="1">Çekin Şubesi</td>
<td colspan="1">Çekin Bankası alanına bilgi girişi yapıldıktan sonra, şube bilgisinin otomatik olarak ekrana geldiği alandır.</td>
</tr>
<tr>
<td colspan="1">İl/İlçe</td>
<td colspan="1">Çekin Bankası ve Çekin Şubesi alanlarına bilgi girişi yapıldıktan sonra bankanın bağlı olduğu il ve ilçe bilgisi otomatik olarak ekrana gelir.</td>
</tr>
<tr>
<td colspan="1">
<p>Hesap No</p>
</td>
<td colspan="1">
<p>İlgili çekin banka hesap numarasının girildiği alandır.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>Seri No</p>
</td>
<td colspan="1">

<p>Çekin üzerinde yazan çek numaralarıdır. Alındı/Verildi Bordro numaraları ve portföy dökümlerinde, bu alana girilen çek numaraları listelenir.</p>
<p>Yardımcı Programlar → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253Dd1958e00-2586-4b57-8a40-dc9812c969ad%2526link%253D2b164138-dbcc-4825-8c16-0ea06ff6c7d8%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Şirket-Şube Parametreleri</a> → Plasiyer Uygulaması Var parametresinin işaretlenmesi durumunda kullanılan alandır. Plasiyerlerin, müşterilerden tahsil etmiş olduğu çeklerin takibini yapması istendiğinde tanımlanması gerekir. İlgili müşterinin Cari Hesap Kayıtları bölümünde tanımlanan plasiyer kodu, bu alana program tarafından otomatik olarak aktarılır. Boş bırakılabilir fakat alan üzerinde değişiklik sadece, Cari → Kayıt → Plasiyer Kodu Kayıtları bölümünde tanımlı olan bir plasiyer kodu ile yapılır. Plasiyer kodu, daha önce Cari → Kayıt → Plasiyer Kodu Kayıtları bölümünden tanımlanmamış ise, bu alana giriş yapılamaz.</p>
<p>Plasiyer Kodlarının tanımlanması ile ilgili detaylı bilgi için Cari → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253De9ca791e-c557-4802-b5cf-b3cfb6b4b4c7%2526link%253Da57a736a-3545-49e1-a21c-82afc70bf99d%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Plasiyer Kodu Kayıtları</a>.</p>

</td>
</tr>
<tr>
<td colspan="1">
<p>Proje Kodu</p>
</td>
<td colspan="1">

<p>Yardımcı Programlar → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253Df7baa628-4b9a-47cb-8f22-03aabde76c1e%2526link%253D8f91f576-27e0-4eea-a0f1-71be7d79c366%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Şirket-Şube Parametre Tanımları</a> → Proje Uygulaması Var seçeneğinin işaretlenmesi ile aktif hale gelen alandır. Proje uygulamasında, çeklerdeki her türlü giriş/çıkış işlemlerinde proje kodu sorgulanır ve boş bırakılmaz. Cari hareketlerde ve entegre havuzunda ise, kayıtlar proje kodu bazında tek tek oluşur. Rehber butonu <img src="../../../../../_assets/088477bb321d1b20c939.jpg"/> ile proje kodlarına ulaşılır.</p>

</td>
</tr>
<tr>
<td colspan="1">
<p>Döviz Tipi/Kur/Döviz Tutarı</p>
</td>
<td colspan="1">

<p>Müşteri Çekleri → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253D80c77c17-6da1-4893-9694-5a72cec2e329%2526link%253D8e0a690f-a720-4f1c-8d6a-4f1498ee422f%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Müşteri Çekleri Parametreleri</a> → Döviz Uygulaması Var parametresinin işaretlendiği durumlarda çek tutarı bilgisi girilmeden önce, ilgili çekin döviz tipi, döviz tipinin işlem birimi ve kur tarihi sorgulanır.</p>
<img src="../../../../../_assets/1e8d6338e56da5432ff0.png"/>
<p>Girilen tarihe göre günlük kur (Döviz Tipi alanına bilgi girişi yapıldıktan sonra) ilgili alana otomatik olarak gelir. Ekrana gelen kur değeri üzerinde değişiklik yapılabilir. Aynı ekranda sorgulanan Tutar alanına çekin döviz tutarı girilir. Program, kur değeri ile döviz tutarını çarpıp TL değerini hesaplayarak Çek Tutarı alanına aktarır. Çeklerin girilen döviz bilgileri ve döviz tipi; kur ve döviz tutarı alanlarından izlenir. Döviz bilgileri, girilen her çek için ayrı ayrı sorgulanır. TL olan çekler için döviz bilgileri ekranı herhangi bir değer verilmeden boş bırakılır.</p>

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
<td colspan="1">Son İşlem Tipi</td>
<td colspan="1">Cariye ait çek ile ilgili durum bilgisinin izlendiği alandır.</td>
</tr>
<tr>
<td colspan="1">Son İşlem Tarihi</td>
<td colspan="1">Çek ile ilgili son yapılan işlem tarihinin izlendiği alandır.</td>
</tr>
<tr>
<td colspan="1">Ek Açıklama 1-2-3</td>
<td colspan="1">Girişi yapılan çeke ait açıklama bilgisinin girildiği alanlardır.</td>
</tr>
<tr>
<td colspan="1">

<p>Bordro Tamamlama</p>

</td>
<td colspan="1">

<p>Portföye alınacak olan çek/çekler bordroya eklendikten sonra, mutlaka bordro tamamlama işleminin yapılması gerekir. Bordro tamamlama işlemi yapılmadan ekrandan çıkılırsa, kayıtlar cari hesaba ve entegrasyon havuzuna aktırılmaz.</p>
<p><img src="../../../../../_assets/c67f632f990c944d9cb3.png"/></p>
<p>Bordro tamamlama ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:</p>

<table>
<tbody>
<tr>
<th>Bordro Tamamlama Ekranı</th>
<th> </th>
</tr>
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
<td>Bordro Basımı seçeneğinin işaretlenmesi ile işlev kazanan seçenektir. Çek girişinde yazılmış olan açıklamaların basılmasını sağlar. </td>
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
<p><strong>Örneğin; </strong>Çeklerin bankasına göre gruplar oluşturulduktan sonra, rapor koduna göre liste alınabilir.</p>
<p>Bordroya çek eklenirken de rapor kodu sorgulanır. Bordro tamamlama butonuna basıldığında, bu alanın tekrar sorgulanmasındaki amaç; çeklerin her biri için ayrı ayrı rapor kodu girilmesi yerine, burada belirlenen rapor kodunun tüm çeklere aktarılmasının sağlanması içindir.</p>

</td>
</tr>
<tr>
<td colspan="1">Cari R.K. (Cari Rapor Kodu)</td>
<td colspan="1">

<p>Rapor Kodu alanında olduğu gibi, raporlama amacıyla en fazla 15 karakter uzunluğunda kod bilgisi girilen alandır. Bilgi girişi yapılması için, Cari → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253D6f1c0005-6726-405d-8ac7-b213b41d23c7%2526link%253Dd50e5347-1966-4bcb-87c7-1d4897ae336e%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Cari Parametreleri</a> → Hareketlerde Rapor Kodu Sorulsun parametresinin işaretlenmesi gerekir.</p>
<p>Bordroya çek eklenirken de rapor kodu sorgulanır. Bordro tamamlama butonuna basıldığında, bu alanın tekrar sorgulanmasındaki amaç; çeklerin her biri için ayrı ayrı rapor kodu girilmesi yerine, burada belirlenen rapor kodunun tüm çeklere aktarılmasının sağlanması içindir.</p>
<p>Bordroya ait çeklerle ilgili kayıt/düzeltme işlemleri bittiğinde, kayıtların entegre bölümlere işlenmesi için mutlaka Bordro tamamlama butonu kullanılarak bordronun tamamlanması gerekir. Bordro tamamlama yapılmadan ekrandan çıkıldıktan sonra yeni bir çek alındı kaydı için tekrar giriş yapıldığında, tamamlanmamış bordrolarla ilgili bir pencere açılır. İptal butonuna tıklanarak işleme devam edilir ya da tamamlanmayan bordro seçilerek Bordro tamamlama butonuna basılır ve kayıt tamamlanır.</p>

</td>
</tr>
<tr>
<td colspan="1"><img src="../../../../../_assets/39d77b8716226638d9ce.jpg"/></td>
<td colspan="1">
<p>Bordro tamamlamak için girilen bilgilerin kaydedilmesini sağlayan butondur. Yardımcı Programlar → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253Dd1958e00-2586-4b57-8a40-dc9812c969ad%2526link%253D2b164138-dbcc-4825-8c16-0ea06ff6c7d8%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Şirket-Şube Parametreleri</a><br/>
						→ Döviz Uygulaması Var parametresinin işaretli olduğu ve cari hesapların döviz bilgileri ile takip edildiği durumlarda, Tamam butonuna basılmasıyla birlikte döviz bilgilerinin girileceği bir pencere ekrana gelir.</p>
<p><img src="../../../../../_assets/054e6fed03334e25aefc.png"/></p>
<p>Girilen çek dövizli ise, çek bilgilerinin toplam tutarının cari hesaplara döviz değerleri ile aktarılması için yukarıdaki ekranda yer alan sahaların doldurulması gerekir. Program, çeklerin toplam TL değerini, girilen kur tutarına bölerek hesapladığı döviz tutarını, cari hesap hareketlerindeki Döviz Tutarı alanına aktarır. Girilen döviz bilgileri, çeklerin tutar değerlerini oluşturmaz veya herhangi bir değişime neden olmaz. Sadece, ilgili carinin döviz raporları için Döviz Tutarı alanına aktarılır.</p>
</td>
</tr>
<tr>
<td colspan="1"><img src="../../../../../_assets/973111d004995dca0113.jpg"/></td>
<td colspan="1">Bordro tamamlama ekranında girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur.</td>
</tr>
</tbody>
</table>

</td>
</tr>
</tbody>
</table>

**Özel Hesap Kapatma**

Cari Hesapları özel hesap kapatma sistemine göre takip eden kullanıcılar için bordronun tamamlanmasından sonra hesap kapatma penceresi ekrana gelir. Müşteriye ait kapatılmamış olan borç ve alacak kayıtları hesap kapatma ekranında listelenir. İlgili borç ve alacak hareketleri işaretlendikten sonra **![](../../../../../_assets/fedfbf27471a0c9a288c.png) Seçilenleri Kapat** butonuna basılarak hesap kapatma işlemi gerçekleştirilir.

Herhangi bir durumda özel hesap kapatmayla ilgili yapılan bir yanlışın Cari → Kayıt → [Özel Hesap Kapatma](<../../../Cari/Kayıt - Cari/Özel Hesap Kapatma/index.md>) bölümünden düzeltme/değiştirme/izleme işlemi yapılabilir.

Özel Hesap Kapatma işlemi ile ilgili detay bilgi için; Cari → Kayıt → [Özel Hesap Kapatma](<../../../Cari/Kayıt - Cari/Özel Hesap Kapatma/index.md>).
