---
title: "Satış Faturası"
page_id: "22804107"
product: "netsis-3-enterprise"
depth: 5
is_section: true
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Fatura"
  - "Kayıt / Fatura"
  - "Satış Faturası"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Fatura / Kayıt / Fatura / Satış Faturası"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTk5ODk5NjAxLTUwOTgtNDM2NS05YTY2LTJhNGM2NmNhMGVjMiZsaW5rPWI5ZjM1N2U0LTJkNjYtNDJiZS04ODZmLWY5NGNlMmIyYzgwZCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=99899601-5098-4365-9a66-2a4c66ca0ec2&link=b9f357e4-2d66-42be-886f-f94ce2b2c80d&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "satis-faturasi_22804670_22804107.html"
source_version: "2022-11-03T11:35:20.473+03:00"
source_bytes: 1405257
fetched_at: "2026-09-13T04:01:42+00:00"
generator: "netsis-scraper 1.0.0"
---
# Satış Faturası

Satış Faturası Bölümü’nde aşağıdaki işlemler kaydedilir, düzenlenir ve izlenir:

- Müşterilere kesilen satış ve alıştan iade fatura işlemleri.
- Sipariş-İrsaliye bağlantılı fatura işlemleri.

Satış faturası, Lojistik-Satış Bölümü’nde, fatura kayıt menüsünün altında yer alır. Sipariş Bilgileri, Üst Bilgiler, Koşul Bilgileri, Kalem Bilgileri, Toplamlar, Vadelere Bölme bilgilerinin girilmesi ile satış faturası kaydı oluşturulur.

Bu bölümlerden bazıları, belirli parametrelerin işaretlenmesi sonucu ekranda gözükür.

**Sipariş Bilgileri**

Sipariş Bilgileri, sipariş takibi yapan firmalarda, sipariş bağlantılı fatura oluşturulması için ya da satış irsaliyelerinin faturalandırılması için kullanılan sekmedir.

Sipariş Bilgileri sekmesi, siparişe ait fatura oluşturmak için tüm bilgilerin en baştan tekrar girilmesi yerine, daha önceden girilen müşteri siparişlerinden fatura oluşturulmasını sağlar.

Satış Faturası modülüne girildiğinde, Sipariş Bilgileri sekmesinin ekrana gelmesi için mutlaka, [Satış Fatura Parametreleri](<../Satış Parametreleri.md>)nde bulunan “Sipariş Takibi Yapılsın” parametresinin işaretlenmiş olması gerekir.

Satış Faturası ekranı Sipariş Bilgileri sekmesi alanları ve içerdiği bilgiler şunlardır:

| Satış Faturası Ekranı |  |
| --- | --- |
| Belge Tipi | Sipariş ve İrsaliye seçeneklerinden oluşur. Satış faturası sipariş bağlantılı ise sipariş, irsaliye bağlantılı ise irsaliye seçeneği seçilir. Bu alan irsaliye bağlantılı fatura oluşturulmadığında pasif olur ve sipariş seçeneği program tarafından seçilir. |
| Belge Numarası | Faturalandırılması istenen sipariş veya irsaliyenin belge numarasının, ![](../../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu ile seçim yapılarak girildiği alandır. Siparişlerin teslim edilen/kalan bazında takibinin sağlıklı olarak yapılabilmesi için faturanın bağlantılı olduğu sipariş numarasının doğru olarak girilmesi gerekir. |
| Teslim Cari Kodu | Sipariş veya irsaliyenin teslim edildiği yerin, ![](../../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu ile seçim yapılarak girildiği cari kod alanıdır. Faturanın kesildiği cari hesap/adres ile, stokların teslim edileceği cari hesap/adresin farklı olması halinde kullanılır. |
| Fatura Oluştur | “Belge Numarası” alanı ve/veya “Detaylı Sipariş/İrsaliye Rehberi” alanı seçilerek fatura oluşturmayı sağlar. Butona tıklandığında, oluşturulacak faturaya ilişkin numara ve tarih bilgilerinin yer aldığı **“Sipariş Teslimatınız Yapılsın Mı?”** başlıklı ekran gelir. Burada **“Tamam”** butonuna basıldığında, seçilen siparişte bulunan bilgiler faturaya aktarılır ve istenirse aktarılan bilgiler üzerinde değişiklik yapılabilir. |
| Detaylı Sipariş/İrsaliye Rehberi Cari Kodu | Faturalandırılacak sipariş veya irsaliye belgelerine kısıt vermek için kullanılan alandır. Faturanın oluşturulması aşamasında, sipariş bilgilerinin detaylandırılarak girildiği müşterinin kodudur. ![](../../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu ile cari kod seçimi yapılır. |
| Detaylı Sipariş/İrsaliye Rehberi Belge Numarası | Faturanın oluşturulacağı sipariş numarasının girildiği alandır. Tek bir siparişe ait faturalandırma işlemi yapılacaksa bu bölüm kullanılabilir. Cari kodun girilip bu alanın boş geçilmesi halinde, ilgili cariye ait tüm siparişler listelenir. |
| Mal Detaylı mı? | “Mal detaylı mı?” sorusu işaretlendiğinde, müşterinin kalan siparişleri mal bazında detaylı listelenir. İşaretlenmediğinde, belirlenen cari koda ait, teslimi yapılmamış (kalan) sipariş numaralarının yer aldığı liste üzerinden, istenilen siparişler farenin sol tuşu çift tıklanarak işaretlenebilir. Böylece faturalama işlemlerinde siparişler birleştirilerek faturalandırılabilir fakat mal detayları izlenemez. |
| Stok Kısıdı Verilebilsin | Ekranın altında listelenecek sipariş kalemleri için kısıt verilmesi amacıyla kullanılan seçenektir. Bu seçeneğin aktif olması için “Mal Detaylı Mı?” sorusunun işaretlenmesi gerekir. “Stok Kısıdı Verilebilsin” seçeneği işaretlendikten sonra “Belgeleri Getir” butonuna basıldığında, listelenecek sipariş kalemlerinin belirlenmesi için “Stok Kısıt Ekranı” gelir. Bu ekranda bulunan **Saha** **Adı** sütunundaki hücreye tıklandığında, stok ilişkili alanlar listelenir. Bu listede, kısıt verilecek alan seçildikten sonra, “Operatör” ve “Değer” alanları kullanılarak istenen kısıt verilir. |
| Sıralama | Belge no, teslim tarihi, koşul kodu, belge tarihi, stok kodu, stok adı seçeneklerini içerir. Listelenecek sipariş/irsaliye belgelerinin seçilecek alanlara göre sıralanmasını sağlar. |
| Belgeleri Getir | Cari kod ve mal detayı bilgileri baz alınarak, sipariş belgelerinin listelenmesini sağlayan butondur. |

**İrsaliye Bağlantılı Fatura İşlemleri**

Satış Faturası modülünden irsaliye bağlantılı fatura oluştururken, aynı cariye ait birden fazla irsaliye birleştirilerek tek bir fatura halinde kaydedilebilir. Bunun için, “Sipariş/İrsaliye Bilgileri” ekranında faturalandırılması istenen irsaliye yada irsaliye kalemleri seçilir. İrsaliyelerin parçalı olarak faturalandırılması için, “Kalem Bilgileri” ekranından irsaliye seçimi yapılır (Bu durumda her stok için satır bazında irsaliye numarası sorulur.) İrsaliye rehberinde, ilgili faturadaki cariye ait faturalanmamış irsaliyelerin listesi yer alır. ![](../../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu ile ilgili faturaya ait faturalanması istenen irsaliye seçilir. Seçilen irsaliyede, bir stokun birden fazla tekrar edildiği satırlarda, hangi satırdaki kaydın seçileceğini, irsaliye kontrol alanı belirler. Satır bazında irsaliye numarası seçilerek yapılan faturalandırma işlemlerinde, irsaliyelerin miktarlarında değişiklik yapılması isteniyorsa, irsaliyenin tamamı faturalandırılmadan önce, irsaliye miktarından faturalanan miktar düşülerek, faturalanmayan satırlar üzerinde değişiklik yapılabilir. Bu şekilde, tamamı faturalandırılmamış irsaliyelerde, bakiye ve miktar kısmı daha sonra faturalandırılır. İrsaliyenin tamamı faturalandırıldığı zaman, satış/alış irsaliyeleri bölümünden irsaliye kaydı çağrıldığında “faturalanmış irsaliye” uyarısı gelir ve bir daha faturalandırılmasına izin verilmez. İrsaliye numarasının olmadığı ya da yanlış girildiği durumlarda, program “Bu müşteriye ait irsaliye bulunamadı” şeklinde bir uyarı verir. Fatura, irsaliye bağlantılı değilse, irsaliye numarası alanı boş bırakılarak, \<tab\> tuşu ile devam edilir.

İrsaliyelerin saklanması ve parçalı faturalandırmanın yapılması için [Satış Fatura Parametreleri](<../Satış Parametreleri.md>)nde bulunan “**Faturalandırılan İrsaliyeler Saklansın**” ve “**İrsaliye Bilgilerinin Parçalı Faturalandırılması**” parametreleri işaretlenir. Uygulamaya dönem ortasında geçmek isteyen firmaların, bu sisteme geçmeden önce tüm irsaliyelerini faturalandırmaları gerekir.

**Üst Bilgiler**

Üst Bilgiler, satış faturasına ait sabit ve cari bilgi alanlarının yer aldığı sekmedir.

Satış Faturası ekranı Üst Bilgiler sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

<table>

<tbody>
<tr>
<th colspan="2">Satış Faturası Ekranı</th>
</tr>
<tr>
<td> Numara</td>
<td>Faturanın programdaki takip numarasıdır. </td>
</tr>
<tr>
<td> Cari Kodu</td>
<td>Faturanın ait olduğu cari hesabın kodudur.</td>
</tr>
<tr>
<td> Tarih</td>
<td>Faturanın üzerinde yazan tarihin girileceği alandır.</td>
</tr>
<tr>
<td> Entegre Tarih</td>
<td>Faturanın muhasebeye işlenme tarihidir.</td>
</tr>
<tr>
<td> Fiili Tarih</td>
<td>Faturanın gerçekleştiği tarihin girileceği alandır.</td>
</tr>
<tr>
<td> Döviz Bazında Tarih</td>
<td>

<p>Faturalarda geçerli olacak kur bilgisinin, hangi tarihe göre baz alınacağının belirlendiği alandır.</p>
Ekrana Döviz Bazında Tarih alanının eklenmesi için, "<a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253Dc72fffc7-4901-4a8f-8ad0-33010d064c95%2526link%253D3669d28a-a827-4a6a-819b-15c02cd1a185%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Satış Fatura Parametreleri</a>" Genel 4 ekranında yer alan "Döviz Takibi Yapılsın" parametresi ve Yardımcı Programlar→ <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253Dd1958e00-2586-4b57-8a40-dc9812c969ad%2526link%253D2b164138-dbcc-4825-8c16-0ea06ff6c7d8%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Şirket-Şube Parametreleri</a>→ "Döviz Uygulaması" parametresinin işaretli olması gerekir.
</td>
</tr>
<tr>
<td> Tipi</td>
<td>
<p>Faturanın hangi tipte kesileceğinin sorgulandığı bölümdür. Tipi alanı; Kapalı, açık, muhtelif, iade, zayi iade, ithalat/ihracat seçeneklerini içerir. </p>
<p><strong>Kapalı Fatura:</strong> Peşin faturalar için kullanılan fatura tipidir. Kapalı kesilen fatura ile stoklara çıkış hareketi, kasa kayıtlarına da giriş (tahsilat) hareketi işlenir. Fatura ile ilgili kayıtlar muhasebe ile entegre çalışılması halinde, Entegrasyon Kayıtları/Kasa Tahsil bölümüne işlenir. Kapalı fatura tipi seçildiğinde, cari hareket kayıtlarında kayıt oluşmaz.</p>
<p><strong>Açık Fatura: </strong>Vadeli faturalar için kullanılan fatura tipidir. Açık kesilen fatura ile stoklara çıkış hareketi, cari hesap kayıtlarına da fatura toplamı kadar borç hareketi işlenir. Fatura ile ilgili kayıtlar muhasebe ile entegre çalışılması halinde, Entegrasyon Kayıtları/Müşteri Borç bölümüne işlenir.</p>
<p><strong>Muhtelif Fatura: </strong>Müşteri kodu sahasında herhangi bir kod girilmediğinde, yani muhtelif müşteriye fatura kesilmesi halinde, program bu fatura tipini otomatik olarak ekrana getirir (Herhangi bir cari kod belirlenmiş ise bu fatura tipi seçilemez). Muhtelif fatura, hareketlere işleyiş açısından kapalı fatura gibi işlem görür.</p>
<p><strong>İade Fatura: </strong>Alınan malların iade edileceği durumlarda kesilen fatura tipidir. Alıştan iade işlemi söz konusu ise mutlaka iade fatura tipi seçilmelidir (Birçok satış raporu, bu tiplere bakılarak satışların durumunu yansıtır). İade kesilen fatura ile stoklara çıkış hareketi, satıcı cari hesaba da borç hareketi işlenir. Fatura ile ilgili kayıtlar muhasebe ile entegre çalışılması halinde, Entegrasyon Kayıtları/Satıcı Borç bölümüne işlenir.</p>
<p><strong>Zayi İade Fatura: </strong>Alınan malların zarar görmesi sebebiyle iade edilmesi halinde kesilen fatura tipidir. İade fatura gibi işlem görür, rapor amaçlıdır.</p>
<p><strong>İthalat/İhracat: </strong>Bu seçenek işaretlenerek kaydedilen bir alış/satış irsaliyesinin <strong>Dekont Modülünden</strong> ithalat/ihracat kapatması yapıldığında, alış/satış faturasının tipi otomatik olarak İthalat/İhracat olur. Kullanıcıların elle kestikleri faturalarda bu seçeneği kullanmamaları gerekir.</p>
</td>
</tr>
<tr>
<td> İhracat/İthalat Tipi</td>
<td>Bu alanda bulunan tipler, sadece ihracat faturaları için geçerlidir. Bir ihracata ait, dekont modülünden yapılan işlemler sonucu oluşan faturada, kesilen irsaliyede belirtilen ihracatın tipi bu alana yansır. Kullanıcıların elle, ithalat/ihracat ve tipi alanlarını kullanarak fatura kesmemeleri gerekir.</td>
</tr>
<tr>
<td>Export Referans No</td>
<td>
<p>Export Referans Numarası, sadece ithalat/ihracat tipli faturalarda dolu olacaktır. Firmaların yaptıkları her ihracata bir numara vermesi gerekir. Programda İhracat faturası oluşturulması için öncelikle, ihracat tipli satış irsaliyesi girilmelidir. </p>
Finans → Dekont→ Kayıt→ İthalat/İhracat İşlemleri → İhracat Kapatma bölümünden girildiğinde, referans no seçilerek ihracat faturası oluşturulur. İhracat işlemleri tamamlandığında program tarafından oluşturulan ihracat faturasına, irsaliyede girilen export referans numarası aktarılır.</td>
</tr>
<tr>
<td colspan="1">Hal Fatura Tipi</td>
<td colspan="1">
<p>Hal Faturası Uygulaması parametresinin işaretlenmesi ile aktif hale gelen alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile Hiçbiri, Komisyoncu veya Satış seçenekleri arasından seçim yapılır.</p>
<p><strong>Örneğin: </strong>Kesilecek fatura bir hal faturası ise ve "Komisyoncu" tipine sahipse, "Komisyoncu" tipinin seçilmesi gerekir. </p>
</td>
</tr>
<tr>
<td colspan="1">Özel Kod-1</td>
<td colspan="1">

<p>Tanımlanan Özel Kod-1 seçenekleri arasından,<img src="../../../../../_assets/088477bb321d1b20c939.jpg"/> rehber butonu ile seçim yapılarak, faturaların belli kodlar altında gruplanmasını sağlayan alandır. </p>
<p>Örneğin, Peşin satışlar ayrı, vadeli satışlar ayrı bir satış hesabında gruplanabilir.</p>
Ekrana Özel Kod-1 alanın eklenmesi için, <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253Dc72fffc7-4901-4a8f-8ad0-33010d064c95%2526link%253D3669d28a-a827-4a6a-819b-15c02cd1a185%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Satış Parametreleri</a> Özel Kod ve Açıklama sekmesinde yer alan "Özel Kod - 1" parametresinin işaretli olması gerekir.
</td>
</tr>
<tr>
<td>Özel Kod-2</td>
<td>

<p>Tanımlanan Özel Kod-2 seçenekleri arasından,<img src="../../../../../_assets/088477bb321d1b20c939.jpg"/> rehber butonu ile seçim yapılarak, fatura kayıtlarının rapor bazında gruplama yapılmasını sağlayan alandır.</p>
Ekrana Özel Kod-2 alanın eklenmesi için, <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253Dc72fffc7-4901-4a8f-8ad0-33010d064c95%2526link%253D3669d28a-a827-4a6a-819b-15c02cd1a185%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Satış Parametreleri</a> Özel Kod ve Açıklama sekmesinde yer alan "Özel Kod - 2" parametresinin işaretli olması gerekir.
</td>
</tr>
<tr>
<td colspan="1">Açıklama</td>
<td colspan="1">

<p>Satış faturasına ait açıklama bilgisinin girildiği alandır.</p>
Ekrana Açıklama alanın eklenmesi için, Satış Parametreleri Özel Kod ve Açıklama sekmesinde yer alan "Açıklama" parametresinin işaretli olması gerekir.
</td>
</tr>
<tr>
<td>Proje Kodu</td>
<td>

<p>Tanımlanan proje kodları arasından,<img src="../../../../../_assets/088477bb321d1b20c939.jpg"/> rehber butonu ile seçim yapılarak, istenildiğinde proje bazında rapor alınabilmesi için girilen koddur.</p>

</td>
</tr>
<tr>
<td>Plasiyer Kodu</td>
<td>

<p>Tanımlanan plasiyer kodları arasından,<img src="../../../../../_assets/088477bb321d1b20c939.jpg"/> rehber butonu ile seçim yapılarak, ilgili müşteriye ait plasiyer kodunun girildiği alandır.</p>

</td>
</tr>
<tr>
<td>Resmi Fatura No</td>
<td>Resmi elektronik fatura numarasının girildiği alandır.</td>
</tr>
<tr>
<td>Kdv Dahil mi?</td>
<td>

<p>KDV'nin nasıl uygulanacağının belirlendiği alandır. KDV dahil kutucuğu işaretlendiği takdirde, stoka ait birim fiyatı, KDV tutarını da içerir.</p>
Ekrana Kdv Dahil mi? alanının eklenmesi için,  <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253Dc72fffc7-4901-4a8f-8ad0-33010d064c95%2526link%253D3669d28a-a827-4a6a-819b-15c02cd1a185%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Satış Parametreleri</a> Fatura KDV sekmesinde yer alan "KDV Dahil/Hariç Sorusu Her Faturada Sorulsun" parametresinin işaretli olması gerekir.
</td>
</tr>
<tr>
<td>Bağlantı No</td>
<td>
<p>Girilen belgenin hangi bağlantıya ait olduğunun izlendiği alandır.</p>
</td>
</tr>
<tr>
<td>Toplu Depo</td>
<td>

<p>Tanımlanan depo kodları arasından,<img src="../../../../../_assets/088477bb321d1b20c939.jpg"/> rehber butonu ile seçim yapılarak, ilgili depo kodunun girildiği alandır. Satış parametreleri kısmında bu parametre işaretlenmediği takdirde, her stok kalemi için ayrı ayrı lokal depo kodu girilmesi gerekir.</p>
Ekrana Toplu Depo alanının eklenmesi için,  <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253Dc72fffc7-4901-4a8f-8ad0-33010d064c95%2526link%253D3669d28a-a827-4a6a-819b-15c02cd1a185%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Satış Parametreleri</a> Genel 2 sekmesinde yer alan "Fatura/İrsaliyelerde Toplu Depo Kodu Kullanılsın" parametresinin işaretli olması gerekir.
</td>
</tr>
<tr>
<td>Nakliye Katsayısı</td>
<td>

<p>Tanımlanan nakliye katsayısı girişinin yapıldığı alandır.</p>
Ekrana Nakliye Katsayısı alanının eklenmesi için, <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253Dc72fffc7-4901-4a8f-8ad0-33010d064c95%2526link%253D3669d28a-a827-4a6a-819b-15c02cd1a185%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Satış Parametreleri</a> Fatura Ek 1 sekmesinde yer alan "Fatura/İrsaliyelerde Nakliye Katsayısı Girişi Yapılsın" parametresinin işaretli olması gerekir.
</td>
</tr>
<tr>
<td>
<p>Değişsin</p>
</td>
<td>
<p>Dövizli belgelerde bazen (yuvarlama kaynaklı) döviz fiyatının, kurun ya da TL fiyatının değişmesi gerekebilir. Bu gibi durumlarda hangi sahadaki bilginin değişeceğinin belirlendiği alandır.</p>
</td>
</tr>
<tr>
<td colspan="1">Farklı Teslimat</td>
<td colspan="1">

<p>Faturanın kesildiği cari hesap/adres ile, stokların teslim edileceği cari hesap/adresin farklı olması halinde kullanılan alandır.</p>
Ekrana Farklı Teslimat alanının eklenmesi için,  <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253Dc72fffc7-4901-4a8f-8ad0-33010d064c95%2526link%253D3669d28a-a827-4a6a-819b-15c02cd1a185%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Satış Parametreleri</a> Genel 3 sekmesinde yer alan "Sipariş/İrsaliye/Faturada Farklı Teslim Yeri Kullanılsın" parametresinin işaretli olması gerekir.
</td>
</tr>
<tr>
<td colspan="1">Kod</td>
<td colspan="1">Basıma yönelik adres bilgisi değişikliği için girilen alandır. Buradaki cari Kod, faturanın kesildiği kodun aynısı olması gerekir.</td>
</tr>
<tr>
<td colspan="1">İsim</td>
<td colspan="1">
<p>Kod alanına girilen cari kodun isim bilgisinin, program tarafından ekrana getirildiği alandır.</p>
</td>
</tr>
<tr>
<td colspan="1">Adres</td>
<td colspan="1">Teslimat yapılacak adres bilgisinin, cari hesabın koduna göre program tarafından ekrana getirildiği, kullanıcı tarafından da değişikliğinin yapılabileceği alandır.</td>
</tr>
<tr>
<td colspan="1">İlçe</td>
<td colspan="1">Teslimat yapılacak ilçe bilgisinin, cari hesabın koduna göre program tarafından ekrana getirildiği, kullanıcı tarafından da değişikliğinin yapılabileceği alandır.</td>
</tr>
<tr>
<td colspan="1">İl</td>
<td colspan="1">Teslimat yapılacak il bilgisinin, cari hesabın koduna göre program tarafından ekrana getirildiği, kullanıcı tarafından da değişikliğinin yapılabileceği alandır.</td>
</tr>
<tr>
<td colspan="1">
<p>Cari Bilgiler/İsim, Açıklama-1, Açıklama-2, Açıklama-3</p>
</td>
<td colspan="1">
<p>Kesilen faturanın müşteriye ait kod bilgisi girildiğinde, cari hesap kayıtlarında bulunan isim ve açıklama bilgilerinin program tarafından ekrana getirildiği alanlardır. Fatura kaydı sırasında bu alanlara müdahale edilemez, sadece bilgi amaçlı olarak görüntülenir.</p>
</td>
</tr>
<tr>
<td colspan="1">Ek Sahalar</td>
<td colspan="1">

<p>Açıklama girişi için kullanılan alanlardır.</p>
Ekrana Ek Sahalar alanın eklenmesi için, <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253Dc72fffc7-4901-4a8f-8ad0-33010d064c95%2526link%253D3669d28a-a827-4a6a-819b-15c02cd1a185%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue"> Satış Parametreleri</a> Genel 5 sekmesinde yer alan "Sipariş/İrsaliye/Faturada Ek Sahalar Kullanılsın " parametresinin işaretli olması gerekir.
</td>
</tr>
</tbody>
</table>

Özel Kod-1, Özel Kod-2, Açıklama, Plasiyer Kodu, Proje Kodu, KDV Dahil, Toplu Depo, Nakliye Katsayısı, Farklı Teslimat (kod, isim, adres, ilçe, il), Cari Bilgiler/İsim, Açıklama-1 Açıklama-2 Açıklama 3 ve Ek Sahalardan oluşan alanlar, [Satış Parametreleri](<../Satış Parametreleri.md>) sayesinde isteğe bağlı olarak ekranda yer alabilir/almayabilir.

**Koşul Bilgileri**

Koşul Bilgileri, satış faturasına ait geçerli koşul bilgileri alanlarının yer aldığı sekmedir.

Satış Faturası ekranı Koşul Bilgileri sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Satış Faturası Ekranı |  |
| --- | --- |
| Koşul Kodu | Tanımlaması yapılan koşulun, ![](../../../../../_assets/088477bb321d1b20c939.jpg)rehber butonu ile seçim yapılarak ekrana getirildiği koddur. |
| Vade Günü | Bir borcun ödenmesi için tanınan süredir. Bu alana vade günü girildiğinde, tanımlanan vade için belirlenen liste fiyatı, kalem bilgileri ekranındaki fiyat sahasına otomatik olarak yansıyacaktır. |
| Koşul Tarihi | Satış koşul tarihinin girildiği alandır. Bu alanda tarih, otomatik olarak ekrana gelecektir. Eğer koşul tarihi değiştirilirse, satışın girildiği tarihte geçerli olan fiyata göre vade ve iskonto uygulaması yapılacaktır. |
| Fiyat Tarihi | Satış fiyat liste tarihinin girildiği alandır. |
| Ödeme Kodu | Fatura kaydı sırasında, koşula bağlı ödeme planının kodu girilmişse, ilgili ödeme kodunun ![](../../../../../_assets/088477bb321d1b20c939.jpg)rehber butonu ile seçim yapılarak ekrana getirildiği alandır. Cari/Koşul Kayıtları/Genel Koşul Kayıtları/Koşul Genel-2 sayfasında bulunan ödeme kodu alanına, o koşula bağlanacak ödeme planının kodu girilmiş ise, ilgili ödeme kodu bu alana program tarafından otomatik olarak ekrana gelir. Fatura belgelerinde koşul uygulamasının olduğu, ancak koşula bağlı ödeme planının olmadığı durumlarda ödeme kodu alanı boş olur ve istenen ödeme planına ait kod girilir. Fatura belgelerinde, cari ödeme planlarının koşul bağlantılı uygulanabilmesi için, **Koşul Sabit Kayıtları**nda bulunan “Cari Hesap Vadelere Bölünerek Atılsın” seçeneğinin işaretlenmesi gerekir. Koşul uygulamasının kullanılmadığı durumlarda bu alan, "Koşul Bilgileri" ekranı yerine "Üst Bilgiler " ekranında yer alır. |

Koşul bilgilerindeki tüm alanların ekranda yer alabilmesi için**, [Satış Parametreler](<../Satış Parametreleri.md>)i** Koşul sekmesinde yer alan "Sipariş/İrsaliye/Faturada Koşul Uygulaması Kullanılsın" parametresinin işaretli olması gerekir.

**Kalem Bilgileri**

Kalem Bilgileri, Kalem Girişi, Açıklama ve Kalem Listesi alanlarının yer aldığı sekmedir.

Satış Faturası ekranı Kalem Bilgileri sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Satış Faturası Ekranı |  |
| --- | --- |
| Kod | Tanımlaması yapılan stok kaleminin, ![](../../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu ile seçim yapılarak ekrana getirildiği koddur. |
| İsim | Stok sabit kayıtlarında kaydettiğiniz stok isminin, program tarafından ekrana getirildiği alandır. |
| Sipariş No | Her malın ayrı ayrı sipariş numarasının girilmesini sağlamak için kullanılan alandır. ![](../../../../../_assets/088477bb321d1b20c939.jpg)rehber butonu ile stoklar için girilmiş tüm siparişlere ulaşılarak seçim yapılır. Fatura, sipariş bağlantılı kesilmeyecek ise, bu alan boş bırakılarak \<tab\> tuşu ile ilerlenir. Sipariş numarası olmadığı ya da yanlış girildiği durumlarda, program “**Sipariş Bulunamadı**” şeklinde bir uyarı verir. Sipariş bulunduğu zaman, o siparişle ilgili teslimi bekleyen mallar, kalan miktarları ve sipariş tutarlarıyla birlikte otomatik olarak fatura ekranına gelir. Ekrana Sipariş No alanının eklenmesi için, Satış Parametreleri Fatura Sipariş sekmesinde yer alan "İrsaliye/Faturada Sipariş No. Mal Bazında Sorulsun" parametresinin işaretli olması gerekir. |
| D.Kd (Depo Kodu) | Tanımlaması yapılan depo kodunun, ![](../../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu ile depo seçimi yapılarak, her malın ayrı ayrı depolarda takip ve raporlanmasını sağlamak amacıyla kullanılan alandır. |
| Yapılandırma Kodu | Esnek yapılandırma uygulamasının kullanıldığı durumlarda, stoka ait yapılandırma kodunun girildiği alandır. |
| Yapılandırma Kodu Açıklaması | Yapılandırma kodu alanına girilen değere ait açıklama bilgisinin, program tarafından getirildiği alandır. Alanın sağ tarafında yer alan yapılandırma kod sihirbazı butonu ![](../../../../../_assets/4d5937e5d0ca7cc09b74.png) ile, yapılandırma kodu tanımlamasının yapılmasını sağlayan ekrana ulaşılır. ![](../../../../../_assets/d6a976b7e9ad5129db10.png) Yeni esnek yapılandırma kodu tanımlamaları butonu ![](../../../../../_assets/b7912af1d26fd81f7ea4.png) ile, yapılandırılabilir ürün girişi ekranına ulaşılır. ![](../../../../../_assets/eb89a3e92ccfc2a92f1c.png) |
| Yapılandırma Kod Sihirbazı | Belirli bir özellik kombinasyonu içeren yapılandırma kodunun, sistemde tanımlı yapılandırma kodları arasında olup olmadığını saptamak ve tanımlı değilse de hızlı tanımlama yapmak amacıyla kullanılan alandır. ![](../../../../../_assets/d6a976b7e9ad5129db10.png) |
| Yapılandırılabilir Ürün Girişi | Birden fazla yapılandırma koduna ait çıkış miktarlarının, tek seferde kaydedilmesi için kullanıldığı alandır. |
| Tes. Cari Kod (Teslim Cari Kodu) | Faturanın kesildiği cari hesap/adres ile, stokların teslim edileceği cari hesap/adresin farklı olması halinde, teslimatın yapılacağı cari hesap/adresin girileceği alandır. Ekrana Tes.Cari Kod alanının eklenmesi için, [Satış Parametreleri](<../Satış Parametreleri.md>) Genel 3 sekmesinde yer alan "Satır Bazında Teslim Cari Kodu Sorulsun" parametresinin işaretli olması gerekir. |
| Satır Açıklama | Her kalem için, 10 ayrı ek açıklama girişinin yapılabileceği alandır. Ekrana Satır Açıklama alanının eklenmesi için, [Satış Parametreleri](<../Satış Parametreleri.md>) Genel 6 sekmesinde yer alan "Satır Bazında Ek Açıklama Sorulsun" parametresinin işaretli olması gerekir. |
| Ç.Değ (Çevrim Değeri) | Stok kodu alanına girilen stoka ait, birden fazla ölçü birimi tanımlanmışsa, hangi ölçü birimi üzerinden miktar girileceğinin belirlendiği alandır. Alanın sağ tarafında bulunan aşağı ok tuşuna basılarak, o stok için tanımlanmış olan ölçü birimi seçilir. Girilen miktar otomatik olarak ölçü birimi değerine çevrilir ve sistem tarafından ekrana getirilir. Alanın sağ tarafında bulunan rehber, stokun bir ölçü birimine ait birden fazla çevrim değeri olması halinde çevrimin hangi değere göre yapılacağını seçmek amacıyla kullanılır. Ekrana Ç.Değ alanının eklenmesi için, [Satış Parametreleri](<../Satış Parametreleri.md>) Genel 1 sekmesinde yer alan "Farklı Birimlerden Mal Çıkışı Yapılsın" parametresinin işaretli olması gerekir. |
| Seri Takibi | Satışların, seri numaralarına göre takibinin yapılması amacıyla kullanılan alandır. |
| Miktar 2 | Stok bazında takibin yapıldığı miktar alanıdır. Karma koli uygulamasının kullanıldığı durumlarda, koli stokuna ait miktar girişi için de kullanılır. Ekrana Miktar 2 alanının eklenmesi için, [Satış Parametreleri](<../Satış Parametreleri.md>) Genel 2 sekmesinde yer alan "İkinci Miktar Sorulsun" parametresinin işaretli olması gerekir. |
| Fiyat Birim | Faturadaki stok kalemlerinin kaydı sırasında, fiyat girmeden önce, eğer ilgili mal için stoklarda birden fazla ölçü birimi tanımlanmışsa (adet, kg, koli v.s) gireceğiniz fiyatın hangi ölçü birimine ait olduğunun seçildiği alandır. Ekrana Fiyat Birim alanının eklenmesi için, [Satış Parametreleri](<../Satış Parametreleri.md>) Genel 1 sekmesinde yer alan "Fiyat Birimi Sorulsun" parametresinin işaretli olması gerekir. |
| Muhasebe Kodu | Hizmet faturası kesen firmaların, bu faturaları satır bazında ayrı hesaplarda muhasebeleştirebilmeleri için kullanılan alandır. Bu alan için tanımlanan muhasebe kodunun seçilmesi ile, ilgili satış faturasındaki hizmet kalemi için alacak hareketi oluşur. Hizmet faturası uygulaması, stok kartı kayıtlarında kodu "HIZ" ile başlayan stoklar için uygulanır. Dolayısıyla, hizmet uygulaması ile bu faturalardaki kalemleri ayrı hesaplarda muhasebeleştirmek isteyen firmaların, hizmet stoklarının kodunun ilk üç hanesini HIZ olarak açmaları gerekir. Ekrana Muhasebe Kodu alanının eklenmesi için, [Satış Parametreleri](<../Satış Parametreleri.md>) Genel 1 sekmesinde yer alan "Hizmet Uygulaması" parametresinin işaretli olması gerekir. |
| Hesap İsmi | Muhasebe kodu alanına girilen hesap koduna ait isim bilgisinin program tarafından ekrana getirildiği alandır. |
| Vade Tarihi | Vade günü baz alınarak hesaplanan tarihin, program tarafından ekrana getirildiği alandır. Ekrana Vade Tarihi alanının eklenmesi için, [Satış Parametreleri](<../Satış Parametreleri.md>) Genel 4 sekmesinde yer alan "Kayıtlarda Her Satırda Vade Tarihi Sorulsun" parametresinin işaretli olması gerekir. |
| Ek Alan-1 | Fatura basımına yönelik, anlık açıklamaların girildiği alandır. Ekrana Ek Alan-1 alanının eklenmesi için, [Satış Parametreleri](<../Satış Parametreleri.md>) Genel 2 sekmesinde yer alan "Ek Alan Kullanılsın" parametresinin işaretli olması gerekir. |
| Ek Alan-2 | Satış Faturaları girilirken stok kalemleri bazında ikinci bir açıklamanın gerekliliği halinde kullanılan alandır. Her bir kalem için 14 karakter uzunluğunda açıklama girilir. Ekrana Ek Alan-2 alanının eklenmesi için, [Satış Parametreleri](<../Satış Parametreleri.md>) Genel 2 sekmesinde yer alan "Ek Alan 2 Kullanılsın" parametresinin işaretli olması gerekir. |
| Miktar | İlgili stok kaleminin fatura üzerindeki miktarının yazıldığı alandır. |
| M. Faz (Mal fazlası) | Satılan malın yanında verilen hediye malların, faturada gösterilmesi için kullanıldığı alandır. Burada hediye verilen miktar girilmelidir. Eğer satılan malın yanında hediye verilen mal farklı ise, miktar hanesine gerekli değer yazılır, mal fazlası hanesi boş bırakılır. Bir sonraki satıra hediye olarak verilen malın kodu yazılır ve bu mal için de miktar hanesi boş bırakılarak, mal fazlası hanesine hediye miktarı girilmesi ile kayıt oluşturulur. Ekrana M. Faz alanının eklenmesi için, [Satış Parametreleri](<../Satış Parametreleri.md>) İskonto sekmesinde yer alan "Mal Fazlası İskontosu Uygulansın" parametresinin işaretli olması gerekir. |
| Dv. Tip (Döviz Tip) | Döviz takibinin yapıldığı alandır. Girilen stok kodu için, tanımlaması yapılan döviz satış tipi değeri, program tarafından ekrana getirilir. Bu alana getirilen değer, isteğe bağlı olarak farklı bir döviz tipi ile de değiştirilebilir. Döviz tipi olarak “0“ dan farklı bir değer seçilirse, ilgili kalemin dövizli olarak satıldığı, “0“ değeri seçilirse de TL olarak satıldığı anlaşılır. Ekrana Dv. Tip alanının eklenmesi için, [Satış Parametreleri](<../Satış Parametreleri.md>) Genel 4 sekmesinde yer alan "Döviz Takibi Yapılsın" parametresinin işaretli olması gerekir. |
| Döviz Fiyat | Girilen stok kodu için, tanımlaması yapılan döviz fiyat değeri, otomatik olarak ekrana gelir. İsteğe bağlı olarak, bu alana getirilen fiyat değiştirilebilir. Ekrana Döviz Fiyat alanının eklenmesi için, [Satış Parametreleri](<../Satış Parametreleri.md>) Genel 4 sekmesinde yer alan "Döviz Takibi Yapılsın" parametresinin işaretli olması gerekir. |
| Döviz Kur | Üst bilgiler ekranında girilen **Döviz Baz Tarihi** ile, **Döviz Takibi/Günlük Kur Girişi Bölümü’nden** girilen kur tutarı, **Döviz Kur** alanına yansır. İsteğe göre değişiklik yapılabilir. Kur tutarı ile döviz fiyatı alanındaki değerlerin çarpımı sonucu çıkan rakam, fiyat alanına yansır. |
| Fiyat | İlgili malın, fatura üzerindeki birim fiyatıdır. |
| İsk.1-6 | İsteğe bağlı olarak 1’den 6’ya kadar kademeli şekilde ekranda yer alan iskonto bilgisinin girildiği alandır. Sadece 1. İskonto için tutar bazında iskonto girilir. Diğer kademeli iskontolarda, oran (%) bazında kayıt girilir. Hesaplamada malın brüt tutarından 1. iskonto düşüldükten sonra, kalan tutardan 2. iskonto düşülür. İkiden fazla iskonto kullanılması durumunda da, kalan tutar üzerinden diğer iskontolar düşülür. Ekrana İsk.1-6 alanının eklenmesi için, [Satış Parametreleri](<../Satış Parametreleri.md>) İskonto sekmesinde yer alan "Kademeli Kaç İskonto Sorulsun" parametresinin işaretli olması gerekir. |
| İsk.1-6 Tip | İskontoların tiplerini muhasebe kodlarına bağlamak için kullanılan alandır. Örneğin, iskonto tip 1 için özel müşteriler iskontosu, iskonto tip 2 için mağaza iskontosu gibi kullanım amacına göre tanımlamalar yapıldıktan sonra belirlenen iskonto tipleri ile farklı muhasebe kodları çalıştırılabilir. |
| KDV | KDV oranının girildiği alandır. Ekrana KDV alanının eklenmesi için, [Satış Parametreleri](<../Satış Parametreleri.md>) Fatura KDV sekmesinde yer alan "Her Satırda KDV Sorulsun" parametresinin işaretli olması gerekir. |
| Proje Kodu | Yapılan satışın proje bazında izlenmesini sağlayan alandır. ![](../../../../../_assets/088477bb321d1b20c939.jpg)rehber butonu ile, ilgili proje seçimi yapılır. Örneğin, firmaya ait, farklı bir konumda yeni bir bina inşa edilmesi durumu bir projedir. Projeye ait bir kod tanımlar ve ilgili projeye ait satışlarda bu kodu seçerek kayıt yaparsanız, gerektiğinde **söz konusu projeye ait** satışlar bu kod sayesinde raporlanabilir. |
| Fiili Tarih | Üst Bilgiler sayfasında bulunan fiili tarih bilgisinin, kalem bilgilerine yansıtıldığı alandır. İsteğe bağlı olarak değiştirilebilir. |
| Künye No | Hal Faturası Uygulaması kullanıldığında aktif hale gelen alandır. İlgili ürün için 19 haneli "Künye No" bilgisinin girildiği alandır. |
| Mal Sahibi | Hal Faturası Uygulaması kullanıldığında aktif hale gelen alandır. Hal Faturası Tipi alanında Satış tipinin seçilmesi ile görüntülenir. Mal sahibi bilgisinin girilmesi için kullanılır. |
| Mal Sahibi TCKN/VKN | Hal Faturası Uygulaması kullanıldığında aktif hale gelen alandır. Hal Faturası Tipi alanında Satış tipinin seçilmesi ile görüntülenir. Mal sahibine ait kimlik veya vergi kimlik numarasının girilmesi için kullanılır. |
| GEKAP Tutarı | İlgili satış faturası için GEKAP tutarının girildiği alandır. |
| GEKAP Ambalaj Tutarı | İlgili satış faturası için GEKAP ambalaj tutarının girildiği alandır. |
| Tutar | Stok miktarı ile birim fiyatın program tarafından çarpılıp, brüt tutar olarak yazıldığı alandır. Bu alana müdahale edilemez. Sadece birim fiyat ve miktar hanelerinde yapılan değişiklikler tutarın değişmesine sebep olur. Faturada girilen tüm stok tutarlarının toplamı, ekranın sağ alt köşesinde bulunan **Toplam Tutar** alanında görüntülenir. |
| Top. Mik. (Toplam Miktar) | Sipariş/irsaliye bağlantılı fatura oluşturulduğunda, ilgili stok kalemi için seçilen sipariş/irsaliye kalemindeki miktar bilgisinin program tarafından ekrana getirildiği alandır. |
| Sip. Nolar (Sipariş Numaraları) | Sipariş bağlantılı fatura oluşturulduğunda, ilgili sipariş numarasının izlendiği alandır. |
| İrs. Nolar (İrsaliye Numaraları) | İrsaliye bağlantılı fatura oluşturulduğunda, ilgili irsaliye numarasının izlendiği alandır. |
| Bakiye | Faturada girilen her stok kodu için, ilgili malın stok hareket kayıtlarındaki bakiyesinin, bilgilendirme amacıyla program tarafından ekrana getirildiği alandır. |
| Özel Fiyat | FATURA\\KDVOZELMATRAH özel parametresi tanımlandığında sorgulanan alandır. Böylece KDV tutarı - Fiyat, Özel Fiyat - üzerinden hesaplanır. "Özel Fiyat" alanına malın alış bedeli, "Fiyat" alanına da satış bedelinin girilmesi gerekir. Toplamlar sekmesindeki diğer hesaplamalarda, yine kalemlerde girilen "Fiyat" alanı baz alınır. Bu şekilde kaydedilen faturalarda iskonto, ek maliyet gibi tanımlamaların olmaması gerekir. |

Yapılandırma Kodu, Yapılandırma Kodu Açıklaması, Yapılandırma Kod Sihirbazı, Yapılandırılabilir Ürün Girişi, Teslim Cari Kodu, Sipariş No, Satır Açıklama, Depo Kodu, Çevrim Değeri, Ek Alan-1 ve 2, Seri Takibi, Miktar 2, Mal Fazlası, Fiyat Birim, Döviz Tip, İsk.1-6, KDV, Muhasebe Kodu, Hesap İsmi, Proje Kodu, Vade Tarihi alanları, Satış Parametreleri sayesinde, isteğe bağlı olarak ekranda yer alabilir/almayabilir.

**Kalem Bilgilerinde Değişiklik/İptal**

Yukarıda açıklanan alanlara bilgi girişi yapıldıktan sonra \<tab\> butonu ile ilerleyerek veya F5 butonuna basılarak, kalem bilgisi kaydedilir ve ekranda satır olarak görünür. Fatura kaydedilmemiş olmasına rağmen, satıra aktarılan stok satış bilgileri, stok hareket kayıtlarına da işlenir. Dolayısıyla, bu aşamada iken, faturanın tamamı yerine sadece stok çıkış hareketi kaydedilir.

Kaydedilen kalem üzerinde değişiklik yapılması istendiğinde, ilgili stok kalemi satırının üzerine çift tıklayarak seçim yapılması halinde, gerekli alan/alanların üzerinde değişiklik yapılabilir. Kaydedilen kalem aynı şekilde seçildikten sonra araç çubuklarında bulunan ![](../../../../../_assets/2df4b343310bcd16b01e.jpg) kayıt silme butonu ya da klavyedeki F7 butonu yardımıyla ilgili kalem silinir.

**Toplamlar**

Toplamlar; İskonto ve Maliyet Toplamları, KDV'ler Toplamı ve Genel Toplam, Kayıt Sorgulamaları alanlarının yer aldığı sekmedir.

Satış Faturası ekranı Toplamlar sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Satış Faturası Ekranı | İskonto ve Maliyet Toplamları |
| --- | --- |
| Brüt Toplam | Faturada kaydedilen mal tutarlarının, iskonto düşülmeden önceki brüt tutarını gösteren alandır. Kalem bilgileri ekranındaki bilgilere göre oluşturulan bir alan olduğu için, elle değiştirme yapılamaz. Buradaki tutarın yanlış olması durumunda, önceki ekrana (kalem bilgileri) geçilerek gerekli düzeltme işlemlerinin yapılması gerekir. |
| Mal Fazlası İsk. | Kalem bilgileri ekranında mal fazlası alanı kullanılmışsa, program öncelikle mal fazlası (hediye) tutarını brüt olarak hesaplar, daha sonra iskonto şeklinde brüt tutardan düşer. Bu alanda, fatura kaydında mal fazlası olarak girilmiş bütün malların toplam tutarı ekranda görünür. Brüt tutardan ilk olarak düşecek iskonto, mal fazlası iskontosudur. Kalem bilgileri ekranındaki bilgilere göre oluşturulan bir alan olduğu için, elle değiştirme yapılamaz. Buradaki tutarın yanlış olması durumunda, önceki ekrana (kalem bilgileri) geçilerek gerekli düzeltme işlemlerinin yapılması gerekir: |
| Satır İskontosu | Fatura kaydı sırasında, satır bazında girilen tüm iskonto oran/ tutar toplamlarının program tarafından hesaplanarak ekrana getirildiği alandır. Brüt tutar ve mal fazlası iskontosundan sonra düşülecek ikinci iskonto, satır iskontosudur. "Kalem Bilgileri" sekmesindeki bilgilere göre oluşturulan bir alan olduğu için, program elle (manuel) değiştirme yapılmasına izin vermez. Buradaki tutarın yanlış olması durumunda, önceki ekrana (kalem bilgileri) geçilerek gerekli düzeltme işlemlerinin yapılması gerekir. |
| Fat.Alt. İsk 1, 2, 3 | Genel iskonto 1-2-3 tanımlamaları yapılmış ise ekrana gelen alanlardır. Fatura Altı İskonto-1 alanı; cari hesap için girilen iskonto oranı varsa, bu oran üzerinden hesaplanan tutarın program tarafından ekrana getirildiği alandır. Hem tutar hem de oran değeri üzerinde istenen düzenleme yapılabilir. Tutar üzerinde yapılan düzeltme oran sahasına, oran üzerinde yapılan düzeltme tutar sahasına otomatik olarak hesaplanarak yansır. Genel İskonto-1-2-3, mal fazlası ve satır iskontolarından sonra, brüt tutardan düşülecek fatura altı iskontolarıdır. Genel İskonto-3 ayrıca **Bölge Farkı İskontosu** için de kullanılır. Ekrana Fat.Alt. İsk 1, 2, 3 alanının eklenmesi için, [Satış Parametreleri](<../Satış Parametreleri.md>) İskonto sekmesinde yer alan "Genel İskonto 1-2-3" parametrelerinin işaretli olması gerekir. |
| Fat.AltM-1, 2 | Ek Maliyet-1 veya 2 tanımlamaları yapılmış ise fatura altı ilave maliyetleri otomatik olarak ekrana gelir. Hesaplatılan bir değer yoksa elle tutar girilir. Ekrana Fat.AltM-1, 2 alanının eklenmesi için, [Satış Parametreleri](<../Satış Parametreleri.md>) Ek Maliyet sekmesinde yer alan "Ek Maliyet 1-2" parametrelerinin işaretli olması gerekir. |
| Genel İskonto 1,2,3 | Mal fazlası ve satır iskontolarından sonra, brüt tutardan düşülen fatura altı iskonto alanlarıdır. Bu alanların ismi, satış parametreleri kısmında Genel İskonto veya Fatura Altı İskonto isimlerinden birinin işaretlenmesiyle belirlenen isim ile ekrana gelir. Genel İskonto-1, faturanın kesildiği müşterinin, cari hesap sabit kayıtlarında tanımlanan iskonto oranı üzerinden hesaplanan tutarın görüntülendiği alandır. Hem tutar hem de oran değeri üzerinde istenilen düzenleme yapılabilir. Tutar üzerinde yapacağınız düzeltme oran sahasına, oran üzerinde yapacağınız düzeltme tutar sahasına otomatik hesaplanarak yansır. Bölge farkı iskontosu için Genel İskonto-3 kullanılır. |
| Ek Maliyet 1,2 | İlave maliyetlerin girildiği alandır. Hesaplatılan bir değer yoksa, elle tutar girilir. |
| ÖTV | Hesaplanan ÖTV tutarının izlendiği alandır. |
| ÖTV Tevkifatı | Belge için ÖTV tevkifatının hesaplanarak getirildiği alandır. ÖTV tevkifatının hesaplanması veya sıfırlanması için, ekran üzerinde farenin sağ tuşuna tıklandığında görüntülenen seçenekler arasından "ÖTV Tevkifatı Hesapla" veya "ÖTV Tevkifatı Sıfırla" seçeneğine tıklanır. |
| Yuvarlama | Fatura genel toplamının yuvarlanması için kullanılan alandır. |
| Br. 1 Miktar, Br.2 Miktar, Br. 3 Miktar | Kalem Bilgilerinde girilen tüm stokların toplam miktar bilgilerinin, stok kartı kayıtlarında tanımlı birinci, ikinci ve üçüncü ölçü birimi cinsinden izlenen alandır. |
| Hediye Puan | Müşterilere, aldıkları malın üzerinden puan hesaplaması yapılması ve puanlarına istinaden hediye verilmesi işlemlerinin takibinin yapılması amacıyla kullanılan alandır. Bu sistemde, her bir ürün için ayrı ayrı puanlar belirlenerek, hak edilen, kullanılan ve kalan bakiye puanları takip edilebilir. Puan karşılığı verilen hediye ürünlerde, bakiye puan dikkate alınır. |
| Satış Faturası Ekranı | **KDV’ler Toplamı ve Genel Toplam** |
| Ara Toplam | Yukarıda anlatılan iskontolar toplamının brüt toplamdan düşülüp, ek maliyet toplamlarının eklenmesiyle oluşan toplamdır. Bu alana elle müdahale edilmez. Bilgilendirmek amacıyla görüntülenen alandır. |
| KDV 1,2,3,4,5 | Fatura kaydında girilen stok kalemlerinin, stok sabit kayıtlarında yazılı KDV oranına göre, program tarafından otomatik hesaplanarak ekrana getirildiği alandır. |
| KDV % | KDV hesaplamalarında kullanılan oranların izlendiği alandır. |
| Toplam KDV | Farklı KDV oranları üzerinden hesaplanan tutarların toplamının yazıldığı alandır. Hesaplanan değer üzerinde çok küçük bir farklılık olması halinde düzenleme yapılmasını, aksi halde bu değerin değiştirilmemesi tavsiye edilir. Burada yapılacak düzeltme, yukarıda anlatıldığı şekilde hesaplanan KDV tutarları dağılımına yansımaz. Yapılan değişiklik, sadece aşağıdaki genel toplam alanına yansır. Fatura → Kayıt → [Satış Parametreleri](<../Satış Parametreleri.md>) → “KDV Maliyete Eklensin” parametresi işaretlenmiş ise, bu alanda oluşan tutar muhasebeye entegre olmaz. Stok fiyatlarına KDV tutarları eklenerek stok hareket kayıtlarına aktarılır. |
| Genel Toplam | Yukarıda anlatılan işlemler sonucu oluşan son toplamın gösterildiği alandır. Bu tutar üzerinde değişiklik yapmak yerine Karşı Toplam alanı kullanılır. |
| Karşı Toplam | Satış faturası genel toplam alanında değişiklik yapılması istendiğinde kullanılan alandır. Yardımcı Programlar/Özel Parametre Kayıtları Bölümü’nde, Grup Kodu sahası “FATURA”, Anahtar sahası “SATFATKARSITOPLAM” ve Değer sahası ‘0’ olarak tanımlama yapılması halinde bilgi girişi yapılır. Bu alana girilecek tutar "Genel Toplam" alanına aktarılır. "Genel Toplam" ile "Karşı Toplam" arasındaki fark, yuvarlama alanından takip edilir. |
| Resim Alanı | Faturaya resim yada doküman dosyası eklemek için kullanılan alandır. |
| e-Fatura Senaryosu Hal Faturası | Hal Faturası Uygulaması kullanıldığında görüntülenen alandır. Üzerine tıklandığında farenin sağ tuşu ile ekrana gelen "Hal Faturası Masraf Girişi" ekranından ilgili fatura için mevcut olan komisyon/satış oranları ve bu oranlara ait varsa KDV oranları girilir. İlgili masraf oranları girildikten sonra ![](../../../../../_assets/39d77b8716226638d9ce.jpg) Tamam butonuna tıklanarak fatura kaydedilir. |
| Satış Faturası Ekranı | Kayıt Sorgulamaları |
| Kasa Kodu | "Üst Bilgiler" sekmesinde bulunan fatura tipleri arasından, kapalı ve muhtelif fatura tipleri seçildiğinde aktif olan alandır. Bu iki tip fatura, peşin fatura olarak kabul edilir ve kasa modülünde kayıt oluşur. Bu alanda çoklu kasa kullanılıyor ise, fatura toplamının hangi kasaya aktarılacağı sorgulanır. Tek kasa kullanımında ‘00’ kasa kodu, program tarafından ekrana getirilir. Kasa kodu seçmek için, sahanın sağ tarafında bulunan aşağı ok işaretine, sağ klik tuşuyla basılması yeterlidir. |
| Kasa Adı | Kasa kodu seçilmesi halinde, ilgili kasaya ait ismin, program tarafından ekrana getirildiği alandır. |
| Toplam Mal Ağırlığı | Faturada girilen stok kalemleri için, “Stok Kartı Kayıtlarında” birim ağırlık tanımlaması ile aktif olan alandır. Program bu ağırlıkları, faturadaki miktarlarla çarparak toplam mal ağırlığını hesaplar ve otomatik olarak ekrana getirir. |
| Vade Gün/Vade Tarihi | Fatura kaydı oluştururken, cari hareket ve stok hareket kayıtlarına işlenecek vade gün/tarihinin belirlendiği alandır. Stok hareketlerine işlenen vade tarihi, stok hareket girişleri ekranından görüntülenmez fakat raporlardan izlenebilir. Ekrana Vade Gün/Vade Tarihi alanının eklenmesi için, [Satış Parametrelerid](<../Satış Parametreleri.md>) Genel 4 sekmesinde yer alan "Kayıtlarda Her Satırda Vade Tarihi ve Vade Günü Sorulsun" parametrelerinin işaretli olması gerekir. |
| Basım | Girilen faturanın basımı yapılacak ise işaretlenen alandır. Bu alan işaretlendikten sonra “Tamam” butonuna basıldığında, “Dizayn Sorgulama” ekranından dizayn tipi ve yazıcı seçilerek basım yapılır. |
| Sıralama Seçeneği | Basımı yapılacak olan fatura kalemlerini, bu alanda bulunan seçeneklere göre sıralatmak amacıyla kullanılan alandır. Ekrana Sıralama Seçeneği alanının eklenmesi için, [Satış Parametreleri](<../Satış Parametreleri.md>)Genel 1 sekmesinde yer alan "Sıralama Seçeneği Faturada Sorulsun" parametresinin işaretli olması gerekir. |
| Vadelere Bölme | Satış Faturası tutarının cari hareket kayıtlarına işlenirken, vadelere bölünerek kaydedilmesi için kullanılan alandır. "Üst Bilgiler" veya "Koşul Bilgileri" ekranında ödeme kodu girilmişse, vadelere bölünen tutarlar program tarafından otomatik olarak bu alana gelir. Ekrana Vadelere Bölme alanının eklenmesi için, [Satış Parametreleri](<../Satış Parametreleri.md>) Genel 4 ekranında yer alan "C/H Vadelere Bölünerek Geçsin" parametresinin işaretli olması gerekir. |
| Maliyet Dağıtımı | Sistemde yer alan alış/satış tipli fatura belgelerinin “Maliyet Dağıtım” işlemleri için kullanılan alandır. Mevcut bir fatura belgesinin “Kalem Bilgileri” sayfasında, sağ fare tuşu tıklandığında çıkan menüde, “Maliyet Dağıtım“ tıklandığında, otomatik olarak “Maliyet Dağıtım” ekranı açılır. Bu ekranda, fatura belgesinin dağıtımı yapılacak şekilde otomatik ayarlamalar yapılır. Aynı durum, “Toplamlar” sekmesinde yer alan “Maliyet Dağıtım” alanının işaretlenmesi durumunda da geçerlidir. **"Tamam"** tuşuna basıldığında “Maliyet Dağıtımı” ekrana gelir Bu kolaylık ile birlikte, “Maliyet Dağıtım” ekranına manuel girmeye gerek kalmadan, fatura girişi esnasında otomatik olarak maliyet dağıtımı yapılması sağlanmıştır. Dağıtılacak fatura belgesinin “Hizmet Prim Belgesi” olması durumunda, “Maliyet Dağıtım” ekranında yer alan dağıtım anahtarı değeri, “Hizmet Prim Belgesi” olacak şekilde otomatik ayarlanır. Diğer fatura belgelerinin dağıtımı işleminde ise, dağıtım anahtarı değerinin manuel seçilmesi gerekir. |
| Tamam | Bilgileri girilen faturanın kaydı için kullanılan butondur. ![](../../../../../_assets/23043a6798351fd813b5.png) Tamam butonuna basıldığında, faturaya ilişkin kayıtlar ilgili entegre bölümlere aktarılır. Faturanın daha önce kaydedilmiş olması ve düzenlenip tekrar kaydedilmesi durumunda, entegre bölümlerden stok ve cari bölümlere işlenen hareketler program tarafından düzenlenir. Bu kayıtlar, Entegrasyon/Entegrasyon Kayıtlarında “2 no.lu" (Düzeltilmiş Kayıt) ya da “4 no.lu" (Düzeltilmiş Bulunamadı) tipte izlenir. |

Maliyet Dağıtımı Ekranı Dağıtım Genel Bilgileri aşağıdaki şekildedir:

| Maliyet Dağıtımı Ekranı | Dağıtım Genel Bilgileri |
| --- | --- |
| Fiş No | Maliyet dağıtım fişine ait sıra numarasının gösterildiği alandır. Prim hesaplaması yapılan ürünlere ait prim dağıtımları bu alana girilen fiş numaraları ile takip edilir. Ancak buradaki fiş numarası, programdaki diğer fatura numaraları ile karıştırılmamalıdır. Perakende uygulamasına özel bir fiş numarasıdır. Yanlış dağıtım yapıldığında, geriye dönük belgeleme için önemlidir. |
| Maliyet Dağıtım Anahtarı | Fatura belgesine ait, maliyet dağıtım şeklinin seçildiği alandır. Aşağı ok tuşuna tıklayarak seçim yapılır. “Hizmet Prim Belgeleri” isimli anahtar, programda daha önceden oluşturulmuş bir anahtardır. Dolayısıyla, “Hizmet Prim Belgeleri” sisteme tanıtılmış durumdadır. Program, sistemdeki fatura belgelerinin hizmet prim faturası olup olmadığını ayırır. “Maliyet Dağıtım Anahtarı” yazısının üzerine çift tıklandığında, Maliyet Dağıtım Anahtarı ekranına otomatik olarak geçiş yapılabilir. Bu alanda, “Hizmet Prim Belgeleri” başlıklı anahtar dışında nakliye, montaj, vb. diğer fatura belgeleri için “Maliyet Dağıtım Anahtarı” ekranında önceden oluşturulan şablonlar da listelenir. |
| Fiş Tarihi | Maliyet dağıtımının hangi tarihte yapılacağının girildiği alandır. |
| Maliyet Dağıtımı | Dağıtılacak Kaynak Belge Kısıtları - Genel Kısıtlar |
| Belge Tipi | Alış Faturası ve Satış Faturası olarak iki seçenek içeren alandır. Aşağı ok ile ilgili fatura seçimi yapılır. |
| Tipi | Kapalı, Açık, Muhtelif, İade ve Zayi İade seçeneklerini içeren alandır. İlgili tip aşağı ok tuşu ile seçilerek ilerlenir. |
| Belge No Aralığı | Dağıtımı yapılacak veya kısmi dağıtımı yapılmış olan fatura belgelerinin ekrana gelmesini sağlayan alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, belge numaraları arasından seçim yapılır. |
| Kod 1 | Satış faturasında girilmiş olan Kod 1 alanındaki değere göre kısıt verilmesini sağlayan alandır. |
| Kod 2 | Satış faturasında girilmiş olan Kod 2 alanındaki değere göre kısıt verilmesini sağlayan alandır. |
| Tarih Aralığı | Dağıtımı yapılacak belgelerin ekrana gelebilmesi için girilen tarih aralığıdır. |

Dağıtılacak kaynak belge kısıtları verildikten sonra ![](../../../../../_assets/5e13c4e6a56c1c670520.png) Kayıt Getir butonuna basıldığında, ekranın sağ bölümünde o satış faturasına ait kayıtlar listelenir. Listedeki kayıt üzerine sağ fare tuşu ile tıklanarak, seçili satırda maliyet dağıtımı yapılır. Satır üzerinde sağ ok ![](../../../../../_assets/e4bfda3a4ab1d3d44663.jpg) ve üç nokta ![](../../../../../_assets/e577cf0766513395a6ad.jpg) tuşlarına çift tıklanarak fatura detayı görüntülenir.

![](../../../../../_assets/fd8983b2ef9edc5b362f.jpg)

Maliyet Dağıtımı Ekranı Dağıtılacak Kaynak Belge Kısıtları-Stok Kısıtları alanlar ve içerdiği bilgiler şunlardır:

| Maliyet Dağıtımı Ekranı | Dağıtılacak Kaynak Belge Kısıtları - Stok Kısıtları |
| --- | --- |
| Stok Kodu | Stoka ait kod numarasıdır. ![](../../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu ile stok kodları arasından seçim yapılır. |
| Grup Kodu | Gruba ait kod numarasıdır. ![](../../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu ile grup kodları arasından seçim yapılır. |
| Stok Kod 1/2/3/4/5 | Aynı tür ve özelliklere sahip olan stok kayıtlarının gruplanarak bir arada raporlarının alınabilmesine yönelik stok kodlarının seçildiği alandır. Üç nokta ![](../../../../../_assets/e577cf0766513395a6ad.jpg)butonu ile stok kodları arasından seçim yapılır. |
| Cari/Satıcı Kodu | Cariye ait kod numarasıdır. ![](../../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu ile cari kodlar arasından seçim yapılır. |

Dağıtılacak Kaynak Belge Kısıtları-Stok Kısıtları alanlarına verilen kısıt sayesinde, dağıtılacak belgelerin kayıtlarının gelmesi sağlanır. Kayıt Getir ![](../../../../../_assets/5e13c4e6a56c1c670520.png) butonuna basıldığında, ekranın sağ bölümünde, satış faturasına ait kayıtlar listelenir. Listedeki kaydın üzerine sağ fare tuşu ile tıklandığında, seçili satırda maliyet dağıtımı yapılır. Satır üzerinde sağ ok![](../../../../../_assets/e4bfda3a4ab1d3d44663.jpg) ve üç nokta ![](../../../../../_assets/e577cf0766513395a6ad.jpg) butonlarına çift tıklandığında fatura detayı görüntülenir.

![](../../../../../_assets/42b920091ef197de3f77.jpg)

Maliyet Dağıtımı ekranı Dağıtılacak Kaynak Belge Kısıtları-Cari Kısıtları sekmesi alanlar ve içerdiği bilgiler şunlardır:

| Maliyet Dağıtımı | Dağıtılacak Kaynak Belge Kısıtları - Cari Kısıtları |
| --- | --- |
| Cari Kod Aralığı | Maliyet dağıtımı yapılacak faturaya, kısıt vermek için cari kod seçiminin kullanıldığı alandır. ![](../../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu ile cari kodlar arasından seçim yapılır. |
| Cari Grup Kodu | Cari gruba ait kod bilgisinin girildiği alandır. ![](../../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu ile grup kodları arasından seçim yapılır. |
| Bağlı Cari Kodu | Farklı teslim adresleri için cari kartların birbirleri ile ilişkilendirilmesini sağlayan alandır. ![](../../../../../_assets/088477bb321d1b20c939.jpg) rehber butonu ile bağlı cari kodlar arasından seçim yapılır. |
| Kullanıcı Tanımlı Saha Kısıtları | Cari hesap kartlarında girilmiş olan kullanıcı tanımlı saha değerlerine göre kısıtlama yapılmasını sağlayan alandır. |

Dağıtılacak Kaynak Belge Kısıtlarındaki “Dağıtılacak Tutar” kolonundaki prim tutarı değerinin, Dağıtımı Yapılacak Hedef Belge Kısıtlarındaki “Dağıtılacak Tutar” kolonundaki tutarların toplamıyla aynı olması gerekir. Prim tutarının tamamı dağıtılabileceği gibi, kısmi olarak da dağıtım yapılabilir. Kısmi olarak dağıtılan prim tutarı “Dağıtılmış Tutar” kolonunda görüntülenir.

**Dağıtımı Yapılacak Hedef Belge Kısıtları**

Dağıtımı yapılacak hedef belgelere kısıt vermek için kullanılır. Genel Kısıtlar, Stok Kısıtları ve Cari Kısıtlar olmak üzere üç bölümden oluşur. **Dağıtılacak Kaynak Belge Kısıtları** kısmında verilen kısıtların aynısı bu kısımda da verilir.

Dağıtılacak kaynak belge kısıtları verildikten sonra Kayıt Getir ![](../../../../../_assets/5e13c4e6a56c1c670520.png) butonuna basıldığında, “Prime Esas Hareketler Otomatik Getirilsin Mi?” sorusunun yazılı olduğu uyarı ekranında “evet” butonu seçilerek, prim tutarlarının hesaplandığı belge/belgeler ve ilgili ürün kodları program tarafından otomatik olarak ekranın sağ tarafında listelenir. “hayır” butonunun seçilmesi halinde, seçim kullanıcıya bırakılır. Kısıtları Temizle ![](../../../../../_assets/064db28106431a884c09.jpg) butonu ile girilen kısıtlar silinir.

Listedeki kayıt üzerine sağ fare tuşu ile tıklanarak, seçili satırda maliyet dağıtımı yapılır. Satır üzerinde sağ ok ![](../../../../../_assets/e4bfda3a4ab1d3d44663.jpg) ve üç nokta ![](../../../../../_assets/e577cf0766513395a6ad.jpg) butonlarına çift tıklanarak fatura detayı görüntülenir.

Dağıtım işlemini sonlandırmak için “Kaydet” butonuna basılır. Ardından ekrana “Eşleştirme işleminiz kaydedilecektir. Emin misiniz?” yazılı onaylama ekranı gelir. Bu onay ekranında “Evet” butonuna basılması halinde dağıtım işlemi yapılmış olur. “Maliyet Dağıtım İşleminiz Başarı ile Gerçekleştirilmiştir.” yazılı uyarı ekranının gelmesiyle de işlem son bulur.

Önceden oluşturulmuş maliyet dağıtım fişleri üzerinde herhangi bir değişiklik yapılamaz fakat “Fiş İptali” yapılabilir. Fiş no rehberinden, önceden kayıtlı fiş seçildiğinde, “Fiş İptal” butonu ile işlem gerçekleşir.

![](../../../../../_assets/53bf222232561ce48b2b.jpg)

"Maliyet Dağıtımı" ekranında iken, ilgili kayıt üzerine çift tıklanarak, klavyeden “Delete” butonuna basıldığında seçili satır silinir. Sağ klik tuşu ile de, ilgili satır maliyetine göre dağıtılır, fatura belgesi görüntülenir ve satır/satırların silme işlemleri yapılır.

![](../../../../../_assets/1fde67651d28434c7aeb.jpg)

Mal Fazlası İskontosu, Satır İskontosu, Genel İskonto, Ek Maliyet 1-2, Sıralama Seçeneği, Vadelere Bölme alanları Satış Parametreleri sayesinde, isteğe bağlı olarak ekranda yer alabilir/almayabilir.

Satış Faturası Kaydı, Değişikliği, İptali aşağıdaki şekilde yapılır:

- Satış faturasının kaydı için, fatura ekranındaki alanlara bilgi girişi yapıldıktan sonra, "Toplamlar" ekranında "**tamam"** butonuna basılır. Böylece, Üst Bilgiler ekranında seçilen tipe göre, gerekli bölümlerde entegre kayıtlar oluşur.
- Daha önceden kaydedilmiş bir fatura üzerinde değişiklik yapmak için, "Üst Bilgiler" ekranından ilgili faturanın numarası girilerek \<tab\> tuşuna basılır. Böylece, kayıtlı faturaya ait daha önceden girilmiş bilgiler ekrana gelir. Mevcut ekranda değiştirilmek istenen alana gelip düzenleme yapılır. Burada dikkat edilmesi gereken nokta, belge üzerinde değişiklik yapıldıktan sonra, fatura ile ilgili bağlantılı bölümlerde de gerekli değişikliklerin program tarafından yapılabilmesi için, "**Toplamlar"** ekranından belgenin tekrar kaydedilmesi gerekir.
- Kaydedilmiş bir satış faturasının iptali için, "Üst Bilgiler" ekranında iken araç çubuklarında bulunan Kayıt Sil ![](../../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna ya da klavyedeki F7 butonuna basılır. Bu aşamada program, “Bu ekrana ait tüm bilgileriniz silinecektir. Emin misiniz?” şeklinde bir uyarı ekrana getirir. “Evet” butonuna basılması halinde, ilgili faturaya ait bilgiler, bağlı olduğu tüm bölümler dahil olmak üzere sistemden silinir.
