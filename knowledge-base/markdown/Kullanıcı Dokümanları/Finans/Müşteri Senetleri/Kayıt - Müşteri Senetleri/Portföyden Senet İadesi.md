---
title: "Portföyden Senet İadesi"
page_id: "24740059"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Müşteri Senetleri"
  - "Kayıt / Müşteri Senetleri"
  - "Portföyden Senet İadesi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Müşteri Senetleri / Kayıt / Müşteri Senetleri / Portföyden Senet İadesi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTMwNDIzN2NiLTk1MjUtNGFjMy05MmI5LTFjZjRmYzllY2QxZCZsaW5rPTBmZGI3MmNjLWJhNmMtNDZmNi04NjI1LTRkMjE1MDFhNzZlNyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=304237cb-9525-4ac3-92b9-1cf4fc9ecd1d&link=0fdb72cc-ba6c-46f6-8625-4d21501a76e7&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "portfoyden-senet-iadesi_34217375_24740059.html"
source_version: "2022-09-20T11:10:11.907+03:00"
source_bytes: 187609
fetched_at: "2026-09-13T04:11:45+00:00"
generator: "netsis-scraper 1.0.0"
---
# Portföyden Senet İadesi

Portföyden Senet İadesi, Finans Bölümü'nde, "Kayıt/Müşteri Senetleri " menüsünün altında yer alır. Portföyden Senet İadesi, portföyde bulunan senet/senetlerin müşteriye iadesi için kullanılan bölümdür.

![](../../../../_assets/6169eaa9deea07d90111.png)

Portföyden Senet İadesi ekranında yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

<table>

<tbody>
<tr>
<th>Portföyden Senet İadesi Ekranı</th>
<th> </th>
</tr>
<tr>
<td>
<p>Verildi Bordro No</p>
</td>
<td>
<p>Aynı gün içinde portföyde bulunan ve senedi veren kişiye iade edilecek bir veya birden fazla senedin tek bir numara altında toplanmasını sağlar.  "Verildi Bordro Numaraları" da, "Alındı Bordro Numaraları" alanında olduğu gibi program tarafından başlatılır ve bir sayı artarak sıra oluşturur. Rehber butonu <img src="../../../../_assets/088477bb321d1b20c939.jpg"/> ile, bordro numaralarına ulaşılır.</p>

<p>Verildi Bordro numarasının başlangıç numarası değişikliği, Müşteri Senetleri → İşlemler → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253D59aad9ad-b336-4aa4-847a-8d066eae349f%2526link%253D01c75897-d151-4079-b612-dc7c7cbb9d27%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Senet Numarası Değişikliği</a> bölümünden yapılır. Program diğer modüllerle entegre kullanılmaya başlandığında (cari hesaplarda kayıtlı müşterilere çek ciro edildiğinde ve bankaya tahsilata/teminata çıkışlarda)" Verildi Bordro Numarası" otomatik olarak aktarılır ve senetlerin ilgili alanlarına kaydedilir. </p>

<p>Bir veya birden fazla senet, tek bir verildi bordro numarası altında kaydedildikten sonra, bu bordro numarasına ait senet kayıtlarının bittiğine dair bilgisayara bilgi vermek ve entegre bölümlere (Cari, Muhasebe) çeklerin işlenmesi açısından Bordro Tamamlama işleminin yapılması gerekir. Bir "Verildi Bordrosuna" ait senetler, işlem ekranından çıkmadan arka arkaya kaydedilebilir.</p>
<p>Tamamlanmayan herhangi bir bordroya yeni bir senet kaydının eklenmesi istendiğinde, bordro numarası değiştirilerek (istenen numara ekrana getirtilerek) senet kayıtlarına devam edilir. Verildi bordro numarası ile kaydedilen senetlerin, bu işlemden sonra toplu izleme/iptal etme  (Müşteri Senetleri → İşlemler → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253D2e84e0af-237f-4a65-9249-42f18242882f%2526link%253D0f37b144-47d2-48ae-933a-c67fdb1b1f8a%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Toplu Çıkış İptali</a>) olanağı bulunur.</p>
</td>
</tr>
<tr>
<td>
<p>Çıkış Tarihi<strong> </strong></p>
</td>
<td>

<p>Müşterilerden alınan senetlerin (portföydeki senetlerin) müşteriye iade edildiği tarihin girildiği alandır.</p>
<p>Çıkış tarihi sistem tarihi üzerinden otomatik olarak ekrana gelir ve üzerinde değişiklik yapılabilir. Çıkış tarihi, giriş tarihinden küçük bir tarih olamaz.</p>

</td>
</tr>
<tr>
<td>Verilen Kodu</td>
<td>
<p>"Portföyden Senet İadesi" işleminde, daha önce portföye giren müşteri senedinin tekrar veren kişiye iadesi söz konusu olduğu için, "Verilen Kodu" alanı pasif halde ekrana gelir. İade edilecek senet seçildikten sonra, senedi veren cari hesaba ait kod bilgisi program tarafından otomatik olarak aktarılır.</p>
</td>
</tr>
<tr>
<td>
<p>Senet No</p>
</td>
<td>

<p>Veren kişiye iade edilmek üzere, verildi bordrosuna eklenecek senet numarasının girildiği alandır. Rehber butonu <img src="../../../../_assets/088477bb321d1b20c939.jpg"/> ile, kayıtlı senet numaralarına ulaşılır.</p>
<p>Senet rehberi kullanımı ile ilgili detaylı bilgi için; <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253D284b2d90-e40f-4bd5-8c6f-b03b4cf23dae%2526link%253De96ad9e4-d0ed-46a9-b54b-478e56686403%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Ek-1 (Çek/Senet No Rehberi Kullanımı)</a> dokümanına bakılabilir.</p>
<p>Alan üzerinde iken, Senet numarası girildiğinde ya da rehberden bir senet seçildiğinde, "Portföyde olan bu kayıt, otomatik olarak bu bordroya eklenecektir." şeklinde bir uyarı ekrana gelir. Seçilen senedin, verildi bordrosuna eklenerek ciro edilmesi istendiğinde bu uyarının onaylanması gerekir.</p>
<p>Seçilen senet, verildi bordrosuna eklendiğinde, senet için "Cari Hesap Senet Alındı Kaydı" bölümünden girilen Rapor Kodu, Rapor Kodu, Cari Rapor Kodu, Proje Kodu, Alındı Bordro No, Giriş Tarihi, Verenin Kodu, Vade Tarihi, Ödeme Tarihi, Ciro Eden, Asıl Borçlu, Plasiyer Kodu, Çekin Bankası, Tutar gibi bilgiler, program tarafından otomatik olarak verildi bordrosuna aktarılır. Bu bilgiler üzerinde değişiklik yapılması istendiğinde, Dekont → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253D20de7d77-d83d-45aa-9d57-f987d5049b71%2526link%253D8388c1e5-7b1a-4a58-91ef-9290e3bf92dd%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Çek/Senet Düzeltme Dekontu</a> bölümünün kullanılması gerekir. İlgili senet, verildi bordrosundan çıkarılarak ve "Cari Hesap Senet Alındı Kaydı" bölümünde ekrana getirilerek de değişiklik yapılabilir.</p>

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
<p>Proje Kodu</p>
</td>
<td colspan="1">

<p>Yardımcı Programlar → Kayıt → <a href="http://Şirket-Şube Parametre Tanımları">Şirket-Şube Parametre Tanımları</a> → “Proje Uygulaması Var" seçeneğinin işaretlenmesi ile aktif hale gelen alandır. Proje uygulamasında, senetlerdeki her türlü giriş/çıkış işlemlerinde proje kodu sorgulanır ve boş bırakılmaz. Cari hareketlerde ve entegre havuzunda ise, kayıtlar proje kodu bazında tek tek oluşur. Rehber butonu <img src="../../../../_assets/088477bb321d1b20c939.jpg"/> ile, proje kodlarına ulaşılır.</p>

</td>
</tr>
<tr>
<td colspan="1">
<p>Alındı Bordro No</p>
</td>
<td colspan="1">

<p>Müşteriden aynı gün içinde iade alınan bir veya birden fazla adette, aynı makbuza ait senetlerin tek bir (aynı) numara altında toplanmasını sağlayan sisteme bordro denir. Senetlerin bordrolar altında takibi, raporlama ve toplu çıkış gibi işlemlerde kolaylık sağlar. "Bordro Numarası" program tarafından otomatik olarak başlatılır. Program, bu numarayı her (yeni) giriş/çıkış makbuzunda bir sayı arttırarak sıra oluşturur.</p>
Bordro numaralarının başlangıç numarası üzerinde herhangi bir değişiklik yapmak için; Müşteri Senetleri → İşlemler → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253D59aad9ad-b336-4aa4-847a-8d066eae349f%2526link%253D01c75897-d151-4079-b612-dc7c7cbb9d27%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Senet Numarası Değişikliği</a> bölümü kullanılır.
Müşteriden yeni alınan senetlerin kaydı sırasında (portföye senet kaydı) program tarafından otomatik olarak ekrana getirilen "Alındı Bordro Numarası" ile kayıt yapma olanağı bulunur. Bu numarada yapılacak değişiklikler, programın işleyişinde bazı karışıklıklara neden olacağı için dikkatli olunması gerekir. Değişiklik yapılacak bordro numarasının, daha önceden kaydedilen senetlerin hiçbirinde yer almaması (bordro numaralarının boş olması) gerekir.
<p>Bir makbuza (bordro) ait tek bir senet varsa bir adet senedin, birden fazla senet varsa (senetler arka arkaya girilerek) söz konusu senetlerin aynı alındı bordro numarasına aktarılması sağlanır. Alındı bordrosu tamamlanarak işlem ekranından çıkılıp tekrar girildiğinde, yeni bordro numarası program tarafından son kalınan numaradan bir sayı arttırılarak devam eder. Daha önceden kaydı yapılan herhangi bir bordroya yeni bir senet kaydının eklenmesi istendiğinde, bordro numarası ilgili alana tekrar girilerek senet kayıtlarına devam edilir. Bu işlemden sonra, "Alındı Bordro Numarası" ile kaydedilen senetlerin toplu izleme/iptal etme olanağı bulunur.</p>
<p>Bir veya birden fazla senedi tek alındı bordro numarası altında kaydettikten sonra, bu bordro numarasına ait senet kayıtlarının bittiğine dair sisteme bilgi vermek ve entegre bölümlere (cari, muhasebe) senetlerin işlenmesi açısından mutlaka <strong>Bordro Tamamlama</strong> işleminin yapılması gerekir.</p>
<p>Birden fazla senedin bulunduğu alındı bordrosunda tek bir senedin düzeltme/iptal işlemi söz konusu olduğunda, alındı bordro numarası girilerek daha önce kaydedilen bordroya erişilir ve ilgili senet grid alanı kullanılarak ekrana getirilir. Düzeltme/iptal (F7) işlemi yapıldıktan sonra, sonucun diğer modüllere yansıması için <strong>Bordro Tamamlama</strong> işlemi yapılır.</p>
 <br/>
			Bir senet üzerinde düzeltme/iptal işlemi yapılması için, ilgili senedin portföyde bulunması gerekir. Ciro edilmiş senetler üzerinde düzeltme/iptal işlemi yapılmaz.
</td>
</tr>
<tr>
<td colspan="1">
<p>Giriş Tarihi</p>
</td>
<td colspan="1">
<p>Kaydedilen senetlerin şirkete giriş tarihinin girildiği alandır. Giriş tarihi sistem tarihinden otomatik olarak aktarılır ve üzerinde istenen değişiklik yapılabilir. "Cari Hesap Senet Alındı Kaydı" bölümünden çek girişi yapıldıktan sonra değiştirilmesine izin verilmeyen tek alan çekin/çeklerin giriş tarihleridir. Giriş tarihinde bir hata yapılması durumunda, Müşteri Senetleri → İşlemler → Toplu Giriş İptali işlemi ile bordronun tamamen iptal edilerek tekrar girilmesi gerekir.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>Verenin Kodu</p>
</td>
<td colspan="1">

<p>Senedi iade veren müşterinin cari hesap kodunun girildiği alandır. Rehber butonu <img src="../../../../_assets/088477bb321d1b20c939.jpg"/> ile, cari hesap kodlarına ulaşılır. Girilecek kodun, Cari → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253D42a33a34-474e-48d9-abe6-d840af3abda4%2526link%253Dc595a1fa-5e62-4e0c-ac6e-20f7004074f8%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Cari Hesap Kayıtları</a> bölümünde önceden tanımlanmış olması gerekir. </p>

</td>
</tr>
<tr>
<td colspan="1">
<p>Vade Tarihi</p>
</td>
<td colspan="1">
<p>Senedin ödenme (vade) tarihinin girildiği alandır.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>Ödeme Tarihi</p>
</td>
<td colspan="1">
<p>Vade tarihi itibariyle senedin opsiyonlu ödenme tarihinin girildiği alandır. Senet kaydı sırasında, ödeme tarihi vade tarihiyle aynı kaydedilir. Dekonttan ödendi işlemi yapıldığında, dekontun işlendiği tarih aktarılır ve değiştirilir.</p>
<p><strong>Örneğin; </strong>firmanın, farklı şehirlerdeki (uzak iller için) senedinin gerçek tahsil günü ya da tatil günlerine denk gelen tarihlerdeki gerçek tahsil tarihi program tarafından (dekontlardan işlem yapıldığında) bu alana kaydedilerek, senetlerle ilgili raporların kaydedilen tarihe göre listelenmesi sağlanır.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>Ciro Eden</p>
</td>
<td colspan="1">
<p>Kaydedilen senet "Asıl" ise (senedi veren kişinin kendi çekiyse), program otomatik olarak alanı boş bırakır. Senet "Ciro" ise (senedi veren kişinin kendi senetleri değilse) senedi verenin ismi program tarafından otomatik olarak aktarılır.</p>
</td>
</tr>
<tr>
<td>
<p>Plasiyer Kodu</p>
</td>
<td>

<p>Yardımcı Programlar → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253Df7baa628-4b9a-47cb-8f22-03aabde76c1e%2526link%253D8f91f576-27e0-4eea-a0f1-71be7d79c366%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Şirket-Şube Parametre Tanımları</a> → "Plasiyer Uygulaması Var" parametresinin işaretlenmesi ile aktif hale gelen alandır. Plasiyerlerin, müşterilerden tahsil etmiş olduğu senetlerin takibinin yapılması istendiğinde kullanılır. Rehber butonu <img src="../../../../_assets/088477bb321d1b20c939.jpg"/> ile, plasiyer kodlarına ulaşılır. "Cari Hesap Kayıtları" bölümünde girilen ilgili müşterinin plasiyer kodu, program tarafından otomatik olarak bu alana aktarılır. Boş bırakılabilir fakat alan üzerinde değişiklik sadece, Cari → Kayıt → "<a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253De9ca791e-c557-4802-b5cf-b3cfb6b4b4c7%2526link%253Da57a736a-3545-49e1-a21c-82afc70bf99d%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Plasiyer Kodu Kayıtları</a>" bölümünden tanımlı olan bir "Plasiyer Kodu" ile yapılır. Plasiyer kodu daha önce Cari → Kayıt → "Plasiyer Kodu Kayıtları" bölümünde tanımlanmamış ise bu alana giriş yapılamaz.</p>
Plasiyer Kodlarının tanımlanması ile ilgili detaylı bilgi için; Cari → Kayıt → "Plasiyer Kodu Kayıtları" bölümüne bakılabilir.
</td>
</tr>
<tr>
<td>
<p>Asıl Borçlu </p>
</td>
<td>
<p>Kaydedilen senet "Asıl" ise, veren kişinin ismi bu alana program tarafından otomatik olarak aktarılır ve bu alana bilgi girilmesine izin verilmez. Senet "Ciro" ise (veren kişinin kendi senetleri değilse) asıl borçlusunun ismi yazılır. Asıl borçlusu da cari hesaplarda kayıtlı ise, asıl borçlunun cari kodu girilir.</p>
</td>
</tr>
<tr>
<td>
<p>Çekin Bankası</p>
</td>
<td>

<p>Kaydedilen senedin tanzim edildiği şehir bilgisin girildiği alandır. Asıl borçlusu veren kişi ise, tanzim yeri de veren kişinin bulunduğu ildir. Asıl borçlusu veren kişiden farklı bir kişi ise, ilgili şehir veya ilçe kaydedilir. Girilen bilgiler raporlamaya yöneliktir.</p>

</td>
</tr>
<tr>
<td>
<p>Tutar</p>
</td>
<td>
<p>Kaydedilen senetlerin Türk Lirası olarak tutarıdır. Bir bordrodaki toplam senet adedi ve tutarı, ekranın alt bölümünde yer alan gri renkli alanda bilgi olarak verilir.</p>
</td>
</tr>
<tr>
<td>
<p>Döviz Tipi/Kur/Döviz Tutarı</p>
</td>
<td>

<p>Müşteri Senetleri → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253D7d6ba288-08f0-4543-a617-25f7a0419417%2526link%253Da7b93cc5-1c94-451e-a076-1a38f6f9adee%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Müşteri Senetleri Parametreleri</a> → “Döviz Uygulaması Var” parametresinin işaretlendiği durumlarda senet tutarı bilgisi girilmeden önce, ilgili senedin döviz tipi, döviz tipinin işlem birimi ve kur tarihi sorgulanır.</p>
<img src="../../../../_assets/1e8d6338e56da5432ff0.png"/>
<p>Girilen tarihe göre günlük kur (Döviz Tipi alanına bilgi girişi yapıldıktan sonra) ilgili alana otomatik olarak gelir. Ekrana gelen kur değeri üzerinde değişiklik yapılabilir. Aynı ekranda sorgulanan "Tutar" alanına senedin döviz tutarı girilir. Program, kur değeri ile döviz tutarını çarpıp TL değerini hesaplayarak "Senet Tutarı" alanına aktarır. Senetlerin girilen döviz bilgileri ve döviz tipi; kur ve döviz tutarı alanlarından izlenir. Döviz bilgileri, girilen her senet için ayrı ayrı sorgulanır. TL olan senetler için döviz bilgileri ekranı herhangi bir değer verilmeden boş bırakılır.</p>

</td>
</tr>
<tr>
<td>Son İşlem Tipi</td>
<td>Cariye ait senet ile ilgili durum bilgisinin izlendiği alandır.</td>
</tr>
<tr>
<td>Son İşlem Tarihi</td>
<td>Senet ile ilgili son yapılan işlem tarihinin izlendiği alandır.</td>
</tr>
<tr>
<td colspan="1">Ek Açıklama 1-2-3</td>
<td colspan="1">Girişi yapılan senede ait açıklama bilgisinin girildiği alanlardır.</td>
</tr>
<tr>
<td>

<p><img src="../../../../_assets/09045048d4760e152eff.png"/> Bordro Tamamlama</p>

</td>
<td>

<p>Portföye alınacak olan senet/senetler bordroya eklendikten sonra, mutlaka bordro tamamlama işleminin yapılması gerekir. Bordro tamamlama işlemi yapılmadan ekrandan çıkılırsa, kayıtlar cari hesaba ve entegrasyon havuzuna aktırılmaz.</p>
<p><img src="../../../../_assets/1742cad3b01a0d59a6fb.png"/></p>
<p>Bordro Tamamlama ekranında yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:</p>

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
<td>"Bordro Basımı" seçeneğinin işaretlenmesi ile işlev kazanan seçenektir. Senet girişinde yazılmış olan açıklamaların basılmasını sağlar. </td>
</tr>
<tr>
<td>Cari R.K. (Cari Rapor Kodu)</td>
<td>

<p>"Rapor Kodu" alanında olduğu gibi, raporlama amacıyla en fazla 15 karakter uzunluğunda kod bilgisi girilen alandır. Bilgi girişi yapılması için, Cari → Kayıt → Cari Parametreleri → “Hareketlerde Rapor Kodu Sorulsun” parametresinin işaretlenmesi gerekir.</p>
<p>Bordroya senet eklenirken de rapor kodu sorgulanır. Bordro Tamamlama <img src="../../../../_assets/c96e2b0d2c19eb0d52cc.png"/> butonuna basıldığında, bu alanın tekrar sorgulanmasındaki amaç; senetlerin her biri için ayrı ayrı rapor kodu girilmesi yerine, burada belirlenen rapor kodunun tüm senetlere aktarılmasının sağlanması içindir.</p>
<p>Bordroya ait senetlerle ilgili kayıt/düzeltme işlemleri bittiğinde, kayıtların entegre bölümlere işlenmesi için mutlaka Bordro Tamamlama <img src="../../../../_assets/c96e2b0d2c19eb0d52cc.png"/> butonu kullanılarak bordronun tamamlanması gerekir. Bordro tamamlama yapılmadan ekrandan çıkıldıktan sonra yeni bir senet alındı kaydı için tekrar giriş yapıldığında, tamamlanmamış bordrolarla ilgili bir pencere açılır. İptal <img src="../../../../_assets/973111d004995dca0113.jpg"/>  butonuna tıklanarak işleme devam edilir ya da tamamlanmayan bordro seçilerek Bordro Tamamlama <img src="../../../../_assets/09045048d4760e152eff.png"/> butonuna basılır ve kayıt tamamlanır.</p>

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
<td>Senet Toplamı</td>
<td>Bordro içinde bulunan senetlerin toplam tutarının izlendiği alandır.</td>
</tr>
<tr>
<td>
<img src="../../../../_assets/973111d004995dca0113.jpg"/> İptal
</td>
<td>Bordro tamamlama ekranında girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur.</td>
</tr>
<tr>
<td>
<img src="../../../../_assets/39d77b8716226638d9ce.jpg"/> Tamam
</td>
<td>

<p>Bordro tamamlamak için girilen bilgilerin kaydedilmesini sağlayan butondur. Yardımcı Programlar → Kayıt → Şirket-Şube Parametreleri → "Döviz Uygulaması Var" parametresinin işaretli olduğu ve cari hesapların döviz bilgileri ile takip edildiği  durumlarda, Tamam <img src="../../../../_assets/39d77b8716226638d9ce.jpg"/> butonuna basılmasıyla birlikte döviz bilgilerinin girileceği bir pencere ekrana gelir.</p>
<p><img src="../../../../_assets/054e6fed03334e25aefc.png"/></p>
<p>Girilen senet dövizli ise, senet bilgilerinin toplam tutarının cari hesaplara döviz değerleri ile aktarılması için yukarıdaki ekranda yer alan sahaların doldurulması gerekir. Program, senetlerin toplam TL değerini, girilen kur tutarına bölerek hesapladığı döviz tutarını, cari hesap hareketlerindeki "Döviz Tutarı" alanına aktarır. Girilen döviz bilgileri, senetlerin tutar değerlerini oluşturmaz veya herhangi bir değişime neden olmaz. Sadece, ilgili carinin döviz raporları için "Döviz Tutarı" alanına aktarılır.</p>

</td>
</tr>
<tr>
<td>Bordro Basımı</td>
<td>Bordrodaki tamamlanan senetlerim yazıcıdan dökümünün almak için işaretlenmesi gereken seçenektir.</td>
</tr>
<tr>
<td>Parçalama Yapılsın</td>
<td>Firmada cari kaydı bulunan bünyeye bağlı kuruluşların birinden alınan senet/senetlerin, bünye içindeki diğer firmaların borçlarına mahsuben dağıtılmasını sağlayan seçenektir.</td>
</tr>
<tr>
<td>R.K. (Rapor Kodu)</td>
<td>

<p>Kaydedilen senetlerin, raporlara yönelik olarak tek kod altında toplanması için en fazla 1 karakter uzunluğunda, isteğe göre kayıt oluşturulan alandır.</p>
<p><strong>Örneğin; </strong>senedin düzenlendiği yere göre gruplar oluşturulduktan sonra, rapor koduna göre liste alınabilir.</p>
<p>Bordroya senet eklenirken de rapor kodu sorgulanır. Bordro Tamamlama <img src="../../../../_assets/c96e2b0d2c19eb0d52cc.png"/> butonuna basıldığında, bu alanın tekrar sorgulanmasındaki amaç; senetlerin her biri için ayrı ayrı rapor kodu girilmesi yerine, burada belirlenen rapor kodunun tüm senetlere aktarılmasının sağlanması içindir.</p>

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

Portföyden Senet İadesinde Kullanılan Özel Tuşlar [Tahsil Hesabına Senet Cirosunda Kullanılan Özel Tuşlar](<Tahsil Hesabına Senet Cirosu/Tahsil Hesabına Senet Cirosunda Kullanılan Özel Tuşlar.md>); bölümü ile aynıdır.
