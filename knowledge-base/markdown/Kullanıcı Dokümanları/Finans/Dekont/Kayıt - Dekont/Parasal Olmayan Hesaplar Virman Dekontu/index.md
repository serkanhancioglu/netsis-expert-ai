---
title: "Parasal Olmayan Hesaplar Virman Dekontu"
page_id: "22805798"
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
  - "Parasal Olmayan Hesaplar Virman Dekontu"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Dekont / Kayıt / Dekont / Parasal Olmayan Hesaplar Virman Dekontu"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWVhY2Y1MTA0LWMyNTgtNDBjNy04MTM1LWE5OWEzMTFmZWExZCZsaW5rPWEzN2ZiNmYyLWEwMzktNGMxYi04Y2M4LWZjZmJlNTdiNTFiNCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=eacf5104-c258-40c7-8135-a99a311fea1d&link=a37fb6f2-a039-4c1b-8cc8-fcfbe57b51b4&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "parasal-olmayan-hesaplar-virman-dekontu_34226315_22805798.html"
source_version: "2022-03-30T11:27:30.507+03:00"
source_bytes: 214192
fetched_at: "2026-09-13T04:08:56+00:00"
generator: "netsis-scraper 1.0.0"
---
# Parasal Olmayan Hesaplar Virman Dekontu

Finans Bölümü'nde, "Kayıt/Dekont" menüsünün altında yer alır. Parasal olmayan hesaplar, dönem sonunda bir rapor yardımıyla maliyetlendirilir. Dönem içinde bu türden fazla hesap çalışıyorsa, dönem sonunda elle (manuel) düzenleme zor bir işlem haline gelebilir. Maliyetlendirmenin program tarafından yapılmasını sağlamak için, parasal olmayan hesaplarda yapılan çıkış/virman işlemleri, özel bir dekont ile yapılarak program tarafından otomatik olarak maliyet oluşturulması sağlanır.

**Örnek aşağıdaki şekildedir:**

| **Hesap** **Kodu** | **TL.** **Tutar** |
| --- | --- |
| 159-001 | \<150.000\> |
| 150-001 | 150.000 |

Şeklinde girilmesi gereken fiş için, programın otomatik maliyetlendirme yapması için aşağıdaki ekran kullanılır.

![](../../../../../_assets/2760ca4af5adfc648b70.png)

Parasal Olmayan Hesaplar Virman Dekontu ekranı alanları ve içerdiği bilgiler aşağıdaki şekildedir:

<table>

<tbody>
<tr>
<th>Parasal Olmayan Hesaplar Virman Dekontu Ekranı</th>
<th> </th>
</tr>
<tr>
<td colspan="1">Seri Kodu</td>
<td colspan="1">

<p>Çıkış/Virman yapılacak parasal olmayan hesap için seri kodu girilen alandır. Rehber butonu <img src="../../../../../_assets/088477bb321d1b20c939.jpg"/> ile, seri kodlarına ulaşılır.</p>

</td>
</tr>
<tr>
<td colspan="1">Dekont No</td>
<td colspan="1">

<p>Çıkış/Virman yapılacak parasal olmayan hesap için dekont numarası girilen alandır. Rehber butonu <img src="../../../../../_assets/088477bb321d1b20c939.jpg"/> ile, dekont numaralarına ulaşılır.</p>

</td>
</tr>
<tr>
<td colspan="1">İşlem Tarihi</td>
<td colspan="1">Virman dekont kaydının girildiği tarihtir.</td>
</tr>
<tr>
<td colspan="1">

<p>Yeni Dekont</p>

</td>
<td colspan="1">

<p>Dekont kaydının tamamlanması halinde, yeni bir dekonta geçmek için kullanılan butondur. Dekontun bakiye vermesi durumunda, butona basılması ile birlikte bakiyeyi kapatmadan işleme devam edilmesi ile ilgili onay ekranı görüntülenir. </p>
<p><img src="../../../../../_assets/62579336fbe3473d1c02.png"/></p>
<p>Onaylanması durumunda yeni dekont ile işleme devam edilir.</p>
			Dekont → Kayıt → Dekont Parametreleri → "Bakiye Veren Dekonttan Çıkılmasın" parametresinin işaretlenesi halinde, içinde bulunulan dekont bakiye veriyorsa, Yeni dekont butonuna basılsa bile, dekont kaydından çıkılmasına izin verilmez.
</td>
</tr>
<tr>
<td colspan="1">Fiş No</td>
<td colspan="1">Kaydı yapılan dekont için fiş numarası girilen alandır. Bu alana girilen numara, ilgili modüllerdeki "Fiş No" alanına otomatik olarak aktarılır.</td>
</tr>
<tr>
<td colspan="1">Muhasebe Kodu</td>
<td colspan="1">

<p>Çıkış/Virman yapılacak parasal olmayan hesap için kod bilgisi girilen alandır. Rehber butonu <img src="../../../../../_assets/088477bb321d1b20c939.jpg"/> ile, muhasebe kodlarına ulaşılır.</p>

</td>
</tr>
<tr>
<td colspan="1">Açıklama</td>
<td colspan="1">Virman dekontu için açıklama bilgisi girilen alandır.</td>
</tr>
<tr>
<td colspan="1">Borç/Alacak</td>
<td colspan="1">Seçilen hesabın işlem göreceği durumun borç olması istendiğinde "Borç", alacak olması istendiğinde ise "Alacak" seçeneği işaretlenerek klavyedeki &lt;tab&gt; tuşu ile ilerlenir.</td>
</tr>
<tr>
<td colspan="1">Döviz/TL</td>
<td colspan="1">Döviz bilgisi girilerek oluşturulacak kayıtlar için "Döviz", Türk Lirası girilerek oluşturulacak kayıtlar için "TL" seçeneğinin işaretlenmesi gerekir. Döviz seçeneği ile girilen kayıtlarda döviz sorgulama ekranı görüntülenir. Sorgulanan döviz kuru bilgisi ile "Tutar" alanına girilecek "Döviz Tutarı" çarpılarak TL değerine çevrilir. Hesaplanan değer "Tutar" alanına aktarılır</td>
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
<p>Miktar</p>
</td>
<td colspan="1">
<p>Çıkış/Virman yapılacak parasal olmayan hesap miktarının girildiği alandır. "Miktar" alanının boş bırakılmaması gerekir. Burada çıkış yapılan birimin, ilgili hesapta hangi birim baz alınarak giriş yapılmışsa ona göre toplam olarak girilmesi gerekir. </p>
<p>Yukarıdaki örneğe göre; 159-001 hesabından yapılan çıkış için miktar alanına 150 birim yazılması gerekir.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>Referans Kodu</p>
</td>
<td colspan="1">

<p>Muhasebe → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253Da59a9956-c477-449a-8ce1-21c150c7032e%2526link%253D5b8992bf-8e5b-4a0c-b969-08ded04f1569%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Muhasebe Parametreleri</a> → "Fişlerde Referans Kodu Sorulsun" parametresinin işaretlenmesi ile aktif hale gelen alandır. Rehber butonu <img src="../../../../../_assets/088477bb321d1b20c939.jpg"/> ile, referans kodlarına ulaşılır. Boş bırakılmaz.</p>

</td>
</tr>
<tr>
<td colspan="1">Proje Kodu</td>
<td colspan="1">

<p>Yardımcı Programlar → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253Dd1958e00-2586-4b57-8a40-dc9812c969ad%2526link%253D2b164138-dbcc-4825-8c16-0ea06ff6c7d8%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Şirket-Şube Parametreleri</a> → "Proje Uygulaması Var" parametresinin işaretlenmesi ile aktif hale gelen alandır. Dekont kaydı sırasında ilgili plasiyer kodunun girilmesi gerekir. Rehber butonu <img src="../../../../../_assets/088477bb321d1b20c939.jpg"/> ile, proje kodlarına ulaşılır. Boş bırakılmaz. Girilen proje kodları, cari hareketlere ve entegrasyona aktarılır.</p>

</td>
</tr>
<tr>
<td>
<p>Dağıtılacak Satır</p>
</td>
<td>
<p>Çıkış/Virman yapılacak satır(lar)ın <strong>dağıtılacak satırlar</strong> olarak işaretlenmesi gerekir.</p>
<p>Yukarıdaki örneğe göre; 159-001 hesabından 150 birim, 150.000 TL tutarındaki çıkış hareketine dağıtılacak işaretinin konması gerekir. Değer taşınma işlemi yapılacak diğer satırlarda, miktar alanının boş bırakılması ve dağıtılacak işaretinin konmaması gerekir.</p>

<table>
<tbody>
<tr>
<td>Hesap Kodu</td>
<td>TL Değer</td>
<td>Miktar</td>
<td>Dağıtılacak</td>
</tr>
<tr>
<td>159-001</td>
<td>&lt;150.000&gt;</td>
<td>150</td>
<td>
<p><img alt="(tick)" src="../../../../../_assets/72b3afd8b2fe319fbd82.svg"/></p>
</td>
</tr>
<tr>
<td>150-001</td>
<td>300.000</td>
<td>-</td>
<td>-</td>
</tr>
</tbody>
</table>

<p> </p>
</td>
</tr>
<tr>
<td colspan="1">Basım Yapılsın</td>
<td colspan="1">
<p>Kaydı yapılan dekontun standart basımının yapılması için kullanılan seçenektir. </p>
</td>
</tr>
</tbody>
</table>

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır.

Kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
