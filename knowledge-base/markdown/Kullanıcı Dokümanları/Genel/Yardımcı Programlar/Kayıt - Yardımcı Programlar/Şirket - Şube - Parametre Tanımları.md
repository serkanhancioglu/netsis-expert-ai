---
title: "Şirket / Şube / Parametre Tanımları"
page_id: "24752984"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Genel"
  - "Yardımcı Programlar"
  - "Kayıt / Yardımcı Programlar"
  - "Şirket / Şube / Parametre Tanımları"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Yardımcı Programlar / Kayıt / Yardımcı Programlar / Şirket / Şube / Parametre Tanımları"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWY3YmFhNjI4LTRiOWEtNDdjYi04ZjIyLTAzYWFiZGU3NmMxZSZsaW5rPThmOTFmNTc2LTI3ZTAtNGVlYS1hMGYxLTcxYmU3ZDc5YzM2NiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=f7baa628-4b9a-47cb-8f22-03aabde76c1e&link=8f91f576-27e0-4eea-a0f1-71be7d79c366&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "sirket-sube-parametre-tanimlari_41169973_24752984.html"
source_version: "2022-10-04T12:01:21.847+03:00"
source_bytes: 124202
fetched_at: "2026-09-13T04:17:05+00:00"
generator: "netsis-scraper 1.0.0"
---
# Şirket / Şube / Parametre Tanımları

Şirket/Şube/Parametre Tanımları; Genel Bölümü'nde, "Kayıt/Yardımcı Programlar" menüsünün altında yer alır. Şirket/Şube/Parametre Tanımları ekranı; İşletmeler, Şubeler ve Parametreler olmak üzere üç sekmeden oluşur. "İşletmeler" sekmesi, yeni işletmenin açılmasını sağlar.

"İşletmeler" sekmesi, sadece **"Enterprise"** paketinde ekrana gelir. Çünkü, sadece "Enterprise" Paketinde işletme tanımlaması yapılır. Diğer paketlerde, "Şubeler" ve "Parametreler" olmak üzere iki sekme görüntülenir.

"Şubeler" sekmesi, yeni şubenin açılmasını ve içinde çalışılan şirkete ait bazı tanımlamaların yapılmasını sağlayan sekmedir.

"Parametreler" sekmesi, şirkete ait genel uygulama parametrelerinin bulunduğu sekmedir.

**İşletme, Şirket, Şube Mantığı**

Yeni bir şirket, işletme ya da şube tanımlamadan önce ihtiyaca göre neyin tanımlamasının yapılacağına karar verilerek işlem adımlarına geçilmesi gerekir.

**Şirket,** içinde çalışılan veritabanıdır. Firmalar her mali yıl için şirket açar ve yıl sonunda devir yaparak, yeni şirket üzerinden işlemlerine devam eder. İşletme, holding kavramı olan yerlerde kullanılır.

**Örneğin**

SANGIDA firmasının bir holding olduğu düşünüldüğünde, holding bünyesinde yer alan SANSUT, SANET ve SANSU firmaları birer işletme olarak tanımlanabilir.

**Şube,** firmaların farklı bölgelerdeki şube kayıtlarının ayrı takip edilmesi istendiği durumlarda tanımlanır.

Çalışılan şirkete ya da işletmeye ait şube varsa, şirketten ayrı olarak şube tanımlaması yapılabilir. "İşletme" ve "Şube" tanımlamalarının yapılması ile, işletme veya şubeler bazında ortak raporlar alınması sağlanır. Bazı işlemlerin merkez şube ya da merkez işletmeden tek seferde ortak olarak yapılması sağlanır.

"Enterprise" paketinde; şirket içinde işletme, işletme içinde şube tanımlanabilir.

![](../../../../_assets/f61cda49c28aaee8b023.jpg)

**Mavi:** Şirket

**Yeşil:** İşletme

**Sarı:** Şube

"Enterprise" dışındaki paketlerde sadece şirket içinde şube açılabilir.

![](../../../../_assets/501eac336ef629e021a8.jpg)

**İşletmeler**

İşletmeler sekmesi, içinde çalışılan şirkete ait yeni işletmenin tanımlandığı sekmedir. Bir şirket içinde birden fazla işletme tanımlanabilir. İşletme tanımlamada; "İşletme Kodu" alanının sıfır (0) olması, ilgili işletmenin bu sistemde en yetkili şirket olduğu anlamına gelir. Bu işletmeye "Holding" de denilebilir.

Sıfır (0) işletme kodu ile açılan bir işletme; Tüm Kayıtları Görme, İşletme Tanımlama ve Şube Tanımlama yetkilerine sahiptir.

İşletme, sadece "Enterprise" Paketinde açılabilir. Yeni bir işletme tanımlamak için öncelikle, programa giriş yapılırken "Ortak30" işletmesinin seçilmesi gerekir. "Ortak30" işletmesi merkez işletmedir ve yeni bir işletme tanımlama işlemi "Ortak30" içinden yapılır.

Şirket/Şube/Parametre Tanımları ekranı İşletmeler sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Şirket/Şube/Parametre Tanımları Ekranı |  |
| --- | --- |
| İşletme Kodu | Yeni tanımlanacak işletme kodunun girildiği alandır. |
| İşletme Adı | Yeni tanımlanacak işletme adının girildiği alandır. |
| Aktif | Tanımlı olan işletmenin aktif olup olmadığının belirlendiği alandır. Aktif kutucuğu işaretlenmediği zaman, ilgili işletme şirket bağlantı ekranında diğer işletmeler arasında görülmez ve dolayısıyla o işletme içine girilemez. "Aktif" seçeneği, ilgili işletmenin geçici olarak kullanım dışı bırakılması durumunda kullanılabilir. İşaretlendiğinde, ilgili işletme şirket bağlantı ekranına gelerek işletme içindeki verilere ulaşılmasını sağlar. Yeni bir işletme tanımladıktan sonra ilgili işletme ve daha önce tanımlanan işletmeler grid ekranda görüntülenir. Tanımlanan yeni işletmeye girilmesi için ilgili işletmeye ait en az bir tane merkez özelliğine sahip şube açılması gerekir. |

**Şubeler**

Şubeler sekmesi, kullanılan pakete göre "İşletme" ya da "Şirket" içinden şube tanımlamasının yapılmasını sağlayan sekmedir. Bir işletme ya da şirketin içinde birden fazla şube açılabilir. "Merkez" seçeneğinin işaretli olması, açılan şubenin merkez olduğunu gösterir. Bir işletme ya da şirket içinde sadece bir merkez şube tanımlaması yapılır.

"Merkez" seçeneği işaretlendiğinde şube (merkez); kendi şubelerindeki tüm kayıtlara erişebilir ve şube tanımlaması yapabilir.

Merkez olmayan şube, program içinde sağlanan güvenlik nedeniyle yetkisiz hale getirilir. Yani, sadece kendi kayıtlarını ve ortak kullanıma açılmış kayıtları görebilir.

Şirket/Şube/Parametre Tanımları ekranı Şubeler sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

<table>

<tbody>
<tr>
<th>Şirket/Şube/Parametre Tanımları Ekranı</th>
<th> </th>
</tr>
<tr>
<td>
<p>Şube Kodu</p>
</td>
<td>

<p>Tanımlanacak şube kodunun girildiği alandır. Rehber butonu <img src="../../../../_assets/088477bb321d1b20c939.jpg"/> ile, şube kodlarına ulaşılır.</p>

</td>
</tr>
<tr>
<td colspan="1">Merkez</td>
<td colspan="1">Tanımlanan şubenin merkez olup olmayacağının belirtildiği alandır. </td>
</tr>
<tr>
<td>
<p>İşletme Kodu</p>
</td>
<td>
<p>İlgili şubenin hangi işletme koduna ait olduğu bilgisinin izlendiği alandır.</p>
</td>
</tr>
<tr>
<td>
<p>Unvan</p>
</td>
<td>
<p>İlgili şube unvanının girildiği alandır. Her şirket/işletme altında şube olması gerektiği için, şirket tanımlandığında bazı şubeler program tarafından oluşturulur. Bu şubeye kayıt girildikten sonra raporlanması istendiğinde, unvan bilgisinin basımı için şirket unvanının girilmesi gerekir. Programa giriş yapıldığında ana menü ve modül ana menülerinin başlık bilgisinde, giriş yapılan şubeye ait unvan bilgisi gösterilir.</p>
</td>
</tr>
<tr>
<td>
<p>Adres</p>
</td>
<td>
<p>Şubeye ait adres bilgisinin girildiği alandır.</p>
</td>
</tr>
<tr>
<td>
<p>İlçe</p>
</td>
<td>
<p>Şubeye ait ilçe bilgisinin girildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile daha önce girilen ilçeler görüntülenir.</p>
</td>
</tr>
<tr>
<td colspan="1">İl</td>
<td colspan="1">

<p>Şubeye ait il bilgisinin girildiği alandır. Rehber butonu <img src="../../../../_assets/088477bb321d1b20c939.jpg"/> ile, şehir rehberine ulaşılır.</p>

</td>
</tr>
<tr>
<td colspan="1">
<p>Ülke</p>
</td>
<td colspan="1">

<p>Şubeye ait ülke kodunun girildiği alandır. Rehber butonu <img src="../../../../_assets/088477bb321d1b20c939.jpg"/> ile, ülke kodlarına ulaşılır.</p>
			"Ülke Kodları Tanımlama" ile ilgili detay bilgi için Yardımcı Programlar → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253D9c0d489c-5006-4ef8-8bb4-04d72f6aca7e%2526link%253Dd592e0a3-4ec1-4f4b-9a9a-88b5fe07f3ab%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Ülke Kayıtları</a> dokümanına bakılabilir.
</td>
</tr>
<tr>
<td colspan="1">
<p>Vergi Dairesi</p>
</td>
<td colspan="1">
<p>Şubeye ait vergi dairesinin tanımlandığı alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile daha önce girilen vergi daireleri görüntülenir.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>Vergi No</p>
</td>
<td colspan="1">
<p>Şubeye ait vergi numarasının tanımlandığı alandır.</p>
</td>
</tr>
<tr>
<td colspan="1">TC Kimlik No</td>
<td colspan="1">Şahsa ait kimlik numarasının girildiği alandır. </td>
</tr>
<tr>
<td colspan="1">
<p>Web Adresi</p>
</td>
<td colspan="1">

<p>Web adresinin girildiği alandır. İnternet erişim butonu <img src="../../../../_assets/84ef9347ff052dddf803.png"/> ile, web adresine erişim sağlanır.</p>

</td>
</tr>
<tr>
<td colspan="1">Sermayesi</td>
<td colspan="1">Şube sermayesinin girildiği alandır.</td>
</tr>
<tr>
<td colspan="1">Ticaret Sicil Adresi</td>
<td colspan="1">Şubeye ait ticaret sicil adresinin girildiği alandır. </td>
</tr>
<tr>
<td colspan="1">Ticaret Sicil No</td>
<td colspan="1">Şubeye ait ticaret sicil numarasının girildiği alandır.</td>
</tr>
<tr>
<td colspan="1">Oda Kaydı/Üye No</td>
<td colspan="1">Şubeye ait oda kaydı veya üye numarasının girildiği alandır.</td>
</tr>
<tr>
<td colspan="1">
<p>Aktif</p>
</td>
<td colspan="1">
<p>Tanımlı olan şubenin aktif olup olmadığının belirlendiği alandır. Aktif kutucuğu işaretlenmediği zaman, ilgili şube şirket bağlantı ekranında diğer şubeler arasında görülmez ve dolayısıyla o şube içine girilemez. "Aktif" seçeneği, ilgili şubenin geçici olarak kullanım dışı bırakılması durumunda kullanılabilir. İşaretlendiğinde, ilgili şube şirket bağlantı ekranına gelerek şube içindeki verilere ulaşılmasını sağlar.</p>
</td>
</tr>
<tr>
<td colspan="1">Telefon No, Faks No, e-Posta</td>
<td colspan="1">Tanımlaması yapılan şubeye ait telefon numarası, faks numarası ve e-Posta bilgisinin girildiği alandır.</td>
</tr>
<tr>
<td colspan="1">

<p><img src="../../../../_assets/4d9d48639b4b1a99a51e.png"/> İşaret Butonları</p>

</td>
<td colspan="1">

<p>Şube ile ilgili resim/dosya eklenmesini sağlayan işaretlerdir. İşaretler kullanılarak, şube için birden fazla resmi eklenebilir, önceki ve sonraki resimler izlenebilir, dosya eklenebilir veya silinebilir.</p>

</td>
</tr>
<tr>
<td colspan="1">

<p><img src="../../../../_assets/53adc90948f52d52edc5.png"/> Şubeden Şubeye Bilgi Transferi</p>

</td>
<td colspan="1">

<p>Bir şubeden diğer şubeye "Kullanıcı Bilgileri" ve "Genel Parametre" bilgilerinin aktarılması için kullanılan butondur. Kaynak Şube ve Hedef Şube alanlarının sorgulanmasını sağlar. </p>
<p><img src="../../../../_assets/097166db9233d737c164.png"/></p>

<p>Şubeden Şubeye Bilgi Kopyalama ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:</p>

<table>
<tbody>
<tr>
<th>Şubeden Şubeye Bilgi Kopyalama Ekranı</th>
<th> </th>
</tr>
<tr>
<td>
<p>Kaynak Şube</p>
</td>
<td>

<p>Kopyalanması istenen şubenin girildiği alandır. Rehber butonu <img src="../../../../_assets/088477bb321d1b20c939.jpg"/> ile, şube kodları arasından seçim yapılır.</p>

</td>
</tr>
<tr>
<td>
<p>Hedef Şube</p>
</td>
<td>

<p>Kopyalanacak şubenin girildiği alandır.  Rehber butonu <img src="../../../../_assets/088477bb321d1b20c939.jpg"/> ile, şube kodları arasından seçim yapılır.</p>

</td>
</tr>
<tr>
<td>Kopyalanacak Bilgiler</td>
<td>Hedef şubeye kopyalanacak bilgilerin seçildiği alandır. </td>
</tr>
<tr>
<td>
<img src="../../../../_assets/d634a1c1e08cc2d392ed.png"/> Kopyala
</td>
<td>Şubeden şubeye bilgi kopyalama işleminin başlatılması için kullanılan butondur.</td>
</tr>
</tbody>
</table>

</td>
</tr>
</tbody>
</table>

**Parametreler**

Parametreler sekmesi, programda genel olarak hangi uygulamaların yapılacağının belirtildiği, genellikle bir defa düzenlenip daha sonra müdahale edilmeyen genel parametrelerin bulunduğu sekmedir.

Şirket/Şube/Parametre Tanımları ekranı Parametreler sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Şirket/Şube/Parametre Tanımları Ekranı |  |
| --- | --- |
| Şube Kodu | Yapılan tanımlamaların geçerli olacağı şube kodunun girildiği alandır. Seçilen şube için parametre tanımlamaları yapılır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, şube kodları arasından seçim yapılır. |
| Plasiyer Uygulaması Var | Firmaların satış organizasyonu, müşteri temsilcilikleri, bayi organizasyonu gibi durumları için, müşterilerine göre tanımladıkları ve cari kayıtlar bazında takip ettikleri satış elemanı, müşteri temsilcisi, pazarlamacı ve plasiyer gibi uygulamalarının hayata geçirilmesi için kullanılan parametredir. Plasiyer kodlarının, Cari → Kayıt → [Plasiyer Kodu Kayıtları](<../../../Finans/Cari/Kayıt - Cari/Plasiyer Kodu Kayıtları.md>) girişinden tek tek tanımlandıktan sonra, "Cari Sabit Kayıtları" ekranındaki "Plasiyer Kodu" alanından girilmesi gerekir. Bu parametrenin işaretlenmesi durumunda Kasa, Çek, Senet, Fatura, Dekont modüllerden girilen her kayıtta "Plasiyer Kodu" sorgulanır. Entegre kayıtlardan sorgulanarak girilen ya da elle yapılan kayıtlardan girilen "Plasiyer Kodları", cari hesaba ait hareketlere aktarılır ve "Plasiyer Kodu" alanında saklanır. Plasiyer uygulamasını seçerek kayıtlarını oluşturan firmalar, plasiyer koduna göre alacakları listeleri "Rapor" modülünden alabilir. |
| Proje Uygulaması Var | Proje uygulamasının başlatılması için kullanılan parametredir. Proje uygulaması; proje bazında iş yapan firmaların projenin başlangıcından sonuna kadar, ilgili proje için yapılan her türlü gider ve masrafı, projeye bağlı olarak gerçekleşen senet/çek hareketlerini, gerçekleştirilen üretim işlemlerini ve her türlü hareketi takip etmeleri için kullanılır. Böylece, projelerin her aşaması proje bazında ayrı ayrı raporlanarak projeler için aynı hesap kodları kullanılsa da tamamen birbirinden ayrılabilir. Proje uygulamasının kullanılması için, program genelinde tüm modül ve işlemlerde "Proje Kodu" sorgulaması bulunur. Bu parametrenin işaretlenmesiyle birlikte, her modülde ve her türlü hareket kayıtlarında "Proje Kodu" sorgulanır. "Proje Kodu" alanı boş bırakılmaz. Proje takibi ile ilgili detay bilgi için; Muhasebe → Kayıt → [Proje Kodu Girişi](<../../../Muhasebe/Muhasebe Modülü/Kayıt - Muhasebe/Proje Kodu Girişi/index.md>) dokümanına bakılabilir. |
| Otomatik İşlem Tipi | Her bir farklı menüden yapılan işlemlerin, program tarafından otomatik olarak belirlenen işlem tipleri ile entegrasyona aktarılması için kullanılan parametredir. Böylece, kullanıcıların işlem yaptıkları menülerde işlem tiplerini değiştirmemesi veya unutması gibi durumlardan kaynaklanacak hatalar ortadan kalkar. Bunun için farklı menülerden yapılan işlemlere, farklı işlem tipleri belirleyen bir işlem tipi rehberi hazırlandı. Firmalar işlem tipi rehberini kullanmadan işlemlerini yapabilir ve program yaptıkları işleme ait işlem tipini otomatik olarak entegrasyona aktarır. İşlem Tipi Tanımlama ile ilgili detay bilgi için; Entegrasyon → Kayıt → [İşlem Tipi Tanımlama](<../../../Muhasebe/Entegre/Kayıt - Entegre/İşlem Tipi Tanımlama.md>) dokümanına bakılabilir. |
| Muhasebe Entegre | Ön muhasebe kayıtlarının, genel muhasebeye entegre olarak çalışması için kullanılan parametredir. Ön muhasebe kayıtları kendi içinde entegre olarak çalışır. Bu durum parametrik olmayıp, kendi içindeki entegrasyonlar program tarafından sağlanır. Muhasebeye entegre çalışılması için, ön muhasebe sistemi ile muhasebe sistemi arasındaki entegrasyonun kurulması gerekir. Entegrasyon kurulması ile ilgili detay bilgi için; Entegrasyon → Kayıt → [Entegrasyon Kodları](<../../../Muhasebe/Entegre/Kayıt - Entegre/Entegrasyon Kodları.md>) dokümanına bakılabilir. |
| Para Birimi | Parametre tanımlamaları yapılan şube için para birimi girilen alandır. **Örneğin** TL KR |
| Doküman Yönetim Sistemi | Doküman yönetim sisteminin seçilmesi için kullanılan alandır. Netsis ve Kets DocPlace olmak üzere iki tür entegrasyon seçeneği vardır. Netsis doküman sisteminin haricinde, doküman eklenecek alanlar için Kets DocPlace yönetim sistemine bağlanılarak dosya eklenmesi için, alanın sağ tarafında yer alan Yükle/Sakla ![](../../../../_assets/f5494a9691693fdb71d7.png) butonu ile, “Kets DocPlace” kurulumunun yapılması gerekir. Kurulum işleminden sonra doküman eklenecek ekranlarda (Örneğin; "Stok Kartı Kayıtları" ekranı) standart dosya ekleme alanları pasif, “Kets DocPlace” butonu ise aktif hale gelir. “Doküman Yönetim Sistemi” parametresi “Netsis” olarak seçildiğinde, doküman eklenecek ekranlar eskisi gibi kullanılabilir. |
| Özel Hesap Penceresi Gösterilmesin | Cari kartlarda "Hesap Tipi" olarak "Özel Hesap Kapatma" seçildiği halde, program içinde "Özel Hesap Kapatma" sorgulama ekranının gelmemesi için kullanılan parametredir. Böylece, cari hesabın hesap tipi "Özel Hesap Kapatma" olduğu halde, işlem adımları sırasında "Özel Hesap Kapatma" sorgulaması ekrana gelmez. Kullanıcı, bu tür cari hesaplar için özel hesap kapatma işlemini Cari → Kayıt → Özel Hesap Kapatma bölümünden yapar. Özel Hesap Kapatma ile ilgili detay bilgi için; Cari → Kayıt → [Özel Hesap Kapatma](<../../../Finans/Cari/Kayıt - Cari/Özel Hesap Kapatma/index.md>) dokümanına bakılabilir. |
| Entegre Kullanıcı No. Sorulsun | Entegrasyon aktarımı sırasında "Kullanıcı Numarası" sorgulanması için kullanılan parametredir. Sadece, belirtilen kullanıcının kayıtları muhasebeye aktarılabilir. Böylece, "Entegrasyon" modülüne entegre edilen sadece belli bir kullanıcının girdiği kayıtların, tüm kayıtlar arasından ayıklanarak izlenmesi sağlanır. Burada, kayıt yapan kişinin kullanıcı kodu ne olursa olsun, diğer kullanıcıların kodlarını vererek, sadece onların yapmış olduğu kayıtları izleme olanağına sahiptir. Kullanıcı kodu 0 (sıfır) girildiğinde ise herhangi bir ayrım yapılmadan, o bölümdeki tüm kayıtlar ekranda listelenir. Kullanıcı numaralarıyla ilgili ayrımın yapılması için "Entegre Kullanıcı No. Sorulsun" parametresinin işaretlenmesi gerekir. Entegrasyon aktarımında kullanıcı numarasının sorgulanması ile ilgili detay bilgi için; Muhasebe → Entegre → İşlemler → [Seçenekli Aktarma](<../../../Muhasebe/Entegre/İşlemler - Entegre/Seçenekli Aktarma.md>)/[Toplu Aktarma](<../../../Muhasebe/Entegre/İşlemler - Entegre/Toplu Aktarma.md>) dokümanına bakılabilir. |
| Seri Takibi Var | Seri takibi uygulamasının kullanılmasını sağlayan parametredir. Seri takibi uygulaması, stok giriş/çıkışlarını ve üretim hareketlerini seri numaralarıyla birlikte takip etmek için program genelinde geliştirilmiş bir sistemdir. Parametrenin işaretlenmesi ile Stok, Fatura ve Üretim modüllerinde seri sorgulaması başlar. Seri takibi ile ilgili detay bilgi için; Stok → Kayıt → [Seri Parametreleri](<../../../Lojistik - Satış/Stok/Kayıt - Stok/Seri Takibi/Seri Parametreleri.md>) dokümanına bakılabilir. |
| İş Akışı Uygulaması Var | İş akış uygulamasının kullanılmasını sağlayan parametredir. Bu uygulama sadece "Enterprise" paketinde ve "Oracle" veritabanında kullanılır. Diğer paketlerde ve veritabanında aktif olarak gelmez. |
| İş Akış Online Onay Sistemi | Mail üzerinden iş akış onayının sağlanması için kullanılan seçenektir. Onaylanacak iş akışları mail olarak ilgili kişiye gönderilir. Mail üzerinden gelen "Bilgilendirme" ekranı ile onay işlemi gerçekleştirilir. |
| Güvenlik Uygulaması | Güvenlik uygulamasının kullanılmasını sağlayan parametredir. Alanın alt tarafında bulunan aşağı ok butonu ile; Satır Bazı Güvenlik Sistemi, Kolon Bazı Geçerlilik Sistemi, Hepsi, ve Hiçbiri seçenekleri arasından seçim yapılır. **Satır Bazı Güvenlik Sistemi:** Satır Bazı Güvenlik Sistemi uygulamasının aktif hale getirilmesi için kullanılan seçenektir. Satır Bazı Güvenlik Sistemi seçeneğinin seçilmesi ile Kullanıcı İşlemleri →Kayıt → "Satır Bazı Güvenlik" bölümü aktif hale gelir. Uygulama, sadece Oracle veritabanında desteklenir. **Kolon Bazı Geçerlilik Sistemi:** Kolon Bazı Geçerlilik Sistemi uygulamasının aktif hale getirilmesi için kullanılan seçenektir. Kolon Bazı Geçerlilik Sistemi seçeneğinin seçilmesi ile Kullanıcı İşlemleri → Kayıt → "Kolon Bazında Geçerlilik Değerleri" bölümü aktif hale gelir. **Hepsi:** Satır Bazı Güvenlik Sistemi ve Kolon Bazı Geçerlilik Sistemi uygulamasının aynı anda aktif hale getirilmesi için kullanılan seçenektir. Hepsi seçeneği sadece "Oracle" veritabanında görülür. **Hiçbiri:** Her iki güvenlik uygulamasının da (Satır Bazı Güvenlik Sistemi ve Kolon Bazı Geçerlilik Sistemi) kullanılması istenmediği zaman tercih edilen seçenektir. |
| Form Bazı Güvenlik Uygulaması Var | Form Bazı Güvenlik uygulamasının kullanılmasını sağlayan parametredir. "Form Bazı Güvenlik Uygulaması" ile açılan herhangi bir form üzerinde görülen alanların, kullanıcı/grup bazında kaydın değiştirilmemesi ya da alanın görüntülenmemesini sağlar. |
| Rehber Kullanım Şekli | Program genelinde rehberlerin farklı şekillerde kullanılmasını sağlayan parametredir. Alanın sağ tarafında yer alan aşağı ok butonu ile; Normal, Sırasız ve Hızlı seçenekleri arasından seçim yapılır. **Normal:** Rehberdeki sahalar otomatik olarak isim sıralı olarak gelir ve rehberdeki bilgilerin tamamı alttaki gridde görüntülenir. Kullanıcı isterse daha sonra rehberdeki kayıtları istediği alana göre sıralayabilir. **Sırasız:** Rehberdeki alanlar belli bir sahaya göre sıralanmadan gelir ve yine normal rehberde olduğu gibi alt gridde rehberdeki kayıtlar görüntülenir. Sırasız rehberde kayıtlar normal rehberde olduğu gibi sıralanmadan listelendiği için kayıtlar daha hızlı gelir. Kullanıcı isterse daha sonra rehberdeki kayıtları istediği alana göre sıralayabilir. **Hızlı:** Rehberin grid ekranında hiç bir kayıt gelmez. İstenen kod ya da isim yazılıp klavyede yer alan "Enter" tuşuna basıldığı zaman kayıtlar görüntülenir. Hızlı rehber şeklinde kayıtlar çağrılmadan önce grid ekrana hiçbir kayıt gelmediği için, veriler ekrana normal ve sırasız rehbere göre daha hızlı gelir. |
| NDI Uygulaması Var | NDI paketinin kullanıldığı durumlarda, NDI paketinde hazırlanan ekran ve rehberlerin ticari pakette kullanılmasını sağlamak için kullanılan parametredir. Bu durumda, içinde bulunulan şube ile NDI veritabanı bağlantısının kurulacağı ve NDI paketinde tanımlanan ekran ve rehberlerin ilgili şubede kullanılmasına yönelik tanımlamaların yapılacağı bölümler, Yardımcı Programlar → Kayıt → NDI bölümünün altında aktif hale gelir. |
| Dinamik Kodlama Sistemi | Kullanıcı ara birimlerinin her yerine eklenen dinamik kodlama özelliği ile; programın standart davranışını değiştirecek kod yazılması, ekranların istendiği şekilde değiştirilmesi ve yeni özellikler kazandırılması gibi programlama tekniği ile yapılabilecek fonksiyonların kodlanması için kullanılan parametredir. Dinamik kodlama özelliğinde kodlama, VBScript dili ile yapılır. Vbscript kodlarını sadece admin olan kullanıcılar tanımlar ve gerektiğinde geçersiz hale getirebilir. |
| Sabit Kart Yabancı Dil Girişi | Sabit kart yabancı dil girişinin aktif hale gelmesi için kullanılan parametredir. İşaretlendiğinde, "Cari Hesap Kayıtları" veya "Stok Kartı Kayıtları" gibi tanımlama yapılan ekranlarda, cari hesap isminin ya da stok kartı isminin girildiği alanların üzerinde iken, farenin sağ klik tuşu ile açılan seçeneklere "Sabit Kart Yabancı Dil Girişi" seçeneği eklenir. Böylece, programın yabancı dil desteği olmamasına rağmen istenen yabancı dilde bilgi girişinin yapılması sağlanır. |
| Online Onay Sistemi | Online Onay Sistemi'nin kullanılması için işaretlenen parametredir. Parametrenin işaretlenmesi ile "Online Onay Sistemi Ayarları" ekranı görüntülenir. İlgili ekran aracılığı ile "Servis Adresi" tanımlaması yapılarak kaydedilir. Online Onay Sistemi Ayarları ekranı üzerinden yapılacak parametre değişiklikleri şirket/işletme/şube bağımsız olarak tüm sunucuyu etkiler. |
| Döviz Uygulaması Var | Program kullanımında döviz uygulamasının aktif hale gelmesi için kullanılan parametredir. Modüllerin dövizli çalışmasını sağlar. Her modülün dövizli işlemlerle ilişkilendirilmesi için, parametreler veya sabit kayıtlardan sorgulanan döviz parametre ve sorgulamaların yanıtlanması gerekir. |
| Düzeltme Tipi | Programda yapılan tüm dövizli işlemlerde, döviz ekranlarından girilen değişik veya aynı döviz tip ve tutarları ilgili alanlarda saklanır. Firmaların, işlemler sırasında kullanacakları farklı döviz tiplerinin tek bir döviz tipine çevrilerek, döviz cinsi bazında rapor alması ve işlemlerini yapması için kullanılan parametredir. Yapılan tüm döviz çevrimlerinde, çevrilmesi istenen döviz tipi sorgulanır. "Düzeltme Tipi" alanına girilecek döviz tipinin, Döviz Takibi → Kayıt → "Döviz İsimleri Tanımlama" bölümünden tanımlanması gerekir. Firma, ilgili şirkette enflasyon muhasebesi kullandığında enflasyon için tanımlanan döviz tipinin girilmesi gerekir. Enflasyon Muhasebesi kullanımı ile ilgili detay bilgi için; Muhasebe → Ek → Ek-1 Enflasyon Muhasebesi dokümanına bakılabilir. |
| Döviz Çevrim Tipi | Döviz Alış, Döviz Satış, Efektif Alış, Efektif Satış olmak üzere dört seçenekten oluşur. Kayıtlarla ilgili döviz cinsinin hangi kurdan işlem göreceği firma prensiplerine göre seçilerek "Döviz Çevrim Tipi" alanında belirlenir. Tanımlanan döviz tipi, modüllerden yapılan dövizli kayıtlarda tekrar sorgulanır. Gerekli durumlarda kayıt sırasında döviz tipi değişikliği yapılabilir fakat, modüllerde bulunan "Dövize Çevrim" işlemlerinde "Döviz Çevrim Tipi" değiştirilemez. |
| Enter Tuş Desteği | Program genelindeki bölümlerde, bir alandan başka bir alana ilerlemek için klavyede bulunan \<tab\> tuşuna basılması gerekir. Fakat bu parametre işaretlendiğinde, \<tab\> tuşunun haricinde "Enter" tuşuna basarak da bir alandan başka bir alana ilerlenebilir. |
| Sesli Uyarı | Program genelindeki işlemler sırasında görüntülenen uyarı ekranlarında, uyarının sesli olarak gelmesi için kullanılan parametredir. |
| **![](../../../../_assets/68c5271d0b3fdf184ce6.png)**Aktif Alan Rengi | İşlemler sırasında aktif olan alan karakterlerini istenen renkte kullanmayı sağlayan butondur. Aktif Alan Rengi butonuna tıklanması ile ekrana gelen renk kartelası yardımı ile seçim yapılır. Tercih edilen renk, alanın sağ tarafında izlenir. |
| e-Posta Uygulaması Var | Şirket içinde yapılan işlemlerin bazılarının istenen kullanıcılara anında e-mail aracılığı ile gönderilmesi ve cari kartları tanımlı müşteri veya satıcılara, kendileriyle ilgili bir işlem yapıldığında e-mail yoluyla bilgi gönderilmesi için kullanılan parametredir. |
| Raporlarda e-Posta Gönderilmesin | Raporlarda e-Posta gönderilmemesi için kullanılan parametredir. |
| SMTP Server Adı | "e-posta Uygulaması Var" parametresinin işaretlenmesi ile aktif hale gelen alandır. İnternet sunucusunun adının girilmesini sağlar. |
| SMTP Kullanıcı Adı | "e-posta Uygulaması Var" parametresinin işaretlenmesi ile aktif hale gelen alandır. İnternet sunucusunun bulunduğu makinede geçerli olan bir kullanıcı adının girilmesini sağlar. İnternet sunucusunda, program uygulamaları için bir kullanıcı açılarak bu alana "Kullanıcı Adı" girilmesi gerekir. Logo Netsis uygulamaları sonucu, e-Posta gönderimi yapıldığında, gönderen kişi olarak bu alana girilen kullanıcı adı görüntülenir. |
| SMTP Şifre | "SMTP Kullanıcı Adı" alanına girilen kullanıcıya ait şifrenin girildiği alandır. Kullanılan bazı internet sunucuları için bu alana bilgi girilmesi zorunludur. Kullanıcı adı ve şifre alanlarına en fazla 100 karakterlik bilgi girilebilir. Kullanıcı adı ve şifre alanları, bilgi girişinin zorunlu olmadığı durumlarda boş bırakılabilir. |
| Rapor Sonuçları Saklansın | Modül raporları ve Rapor modülü altındaki Raporlar/Serbest Raporlar alındıktan sonra raporun saklanması için kullanılan parametredir. Raporların saklanacağı kayıt yolunun belirtilmesi ve son kaç tane sonucun saklanacağının belirtilmesi gerekir. En fazla ya son 50 sonuç otomatik olarak kaydedilir ya da bu alana 0 (Sıfır) değeri verilip rapor aldıktan sonra "Sonucu Kaydet" seçeneği ile elle (Manuel) kayıt yapılabilir. |
| İki Adımlı Doğrulama Yeri | Yüksek seviyeli güvenlik elde etmek için kullanılır. İki Adımlı Doğrulama sisteminde zaman bazlı tek seferli parola yöntemi kullanılır. Bu yöntemle kullanıcılar, telefon veya tablette tek seferli parola üretmek için, yükledikleri uygulamalar üzerinden zaman bazlı parolalar türeterek, bu parolalar ile uygulamaya giriş yapabilirler. Türetilen parolalar belli bir süre geçerlidir. Özellikle son dönemlerde kullanıcı şifrelerinin çalınması sonucu kötü niyetli kişilerin ciddi zararlar verdiği düşünüldüğünde, dünya genelinde İki Adımlı Doğrulama Sistemi sıklıkla önerilen bir yöntemdir. İki Adımlı Doğrulama Yeri; alanın sağ tarafında yer alan aşağı ok butonu ile Hiçbiri, Masaüstü, Web ve Türü seçenekleri arasından belirlenir. Hiçbiri seçildiğinde, İki Adımlı Doğrulama sisteminin pasif olması anlamına gelir. Masaüstü seçildiğinde, sadece Temelset üzerinden giriş yaparken aktif hale gelir. Web seçildiğinde, sadece Wings üzerinden yapılan girişler sırasında aktif hale gelir. Hepsi seçildiğinde, hem Masaüstü hem de Wings üzerinden yapılan girişler sırasında aktif hale gelir. |

Şirket/Şube/Parametre Tanımları ekranında ilgili kayıtlar girildikten sonra “Kaydet” ![](../../../../_assets/865524a70e225c89c107.jpg) butonu ile kayıt tamamlanır. Şirket/Şube/Parametre Tanımları ekranından açılan bir kayıt, kayıt sil ![](../../../../_assets/2df4b343310bcd16b01e.jpg)butonu ile iptal edilir veya üzerinde değişiklik yapılması için kaydet ![](../../../../_assets/865524a70e225c89c107.jpg) tuşu kullanılarak düzeltilir. Kaydedilen satır üzerinde değişiklik yapılması istendiğinde, ilgili satırının üzerinde çift tıklayarak seçim yapılması halinde, gerekli alan/alanların üzerinde değişiklik yapılabilir. Kaydedilen satır aynı şekilde seçildikten sonra araç çubuklarında bulunan ![](../../../../_assets/2df4b343310bcd16b01e.jpg) kayıt silme butonu ya da klavyedeki F7 tuşu yardımıyla ilgili satır silinir. Herhangi bir şubede kayıt olması halinde ilgili şube silinemez.
