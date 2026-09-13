---
title: "Genel Gider Cari Hesap Fatura Kaydı"
page_id: "22805933"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Dekont"
  - "Kayıt / Dekont"
  - "Genel Gider Cari Hesap Fatura Kaydı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Dekont / Kayıt / Dekont / Genel Gider Cari Hesap Fatura Kaydı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTFlNjkxZjNjLTUyYTEtNDA4MC1hMzA2LWU2YjJhNGE4NzM4MiZsaW5rPTgyNjVhNmY5LWM4YzYtNDU0NC04YWM3LTE0ZDI3MTIyNGQ4NyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=1e691f3c-52a1-4080-a306-e6b2a4a87382&link=8265a6f9-c8c6-4544-8ac7-14d271224d87&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "genel-gider-cari-hesap-fatura-kaydi_34231090_22805933.html"
source_version: "2022-12-01T09:36:12.330+03:00"
source_bytes: 843415
fetched_at: "2026-09-13T04:09:22+00:00"
generator: "netsis-scraper 1.0.0"
---
# Genel Gider Cari Hesap Fatura Kaydı

Genel Gider Cari Hesap Fatura Kaydı, Finans Bölümü'nde, "Kayıt/Dekont" menüsünün altında yer alır. Genel Gider Cari Hesap Fatura Kaydı, stoklarla bağlantısı olmayan cari, banka ve muhasebe genel gider hesaplarına işlenecek faturaların kaydedildiği bölümdür.

"Genel Gider Cari Hesap Fatura Kaydı" bölümüne girildiğinde Yardımcı Programlar → Kayıt → [Şirket-Şube Parametreleri](<../../../Muhasebe/Muhasebe Modülü/Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/Genel Tanımlar/Yardımcı Programlar-Şirket-Şube Parametreleri.md>) → “Döviz Uygulaması Var” parametresi işaretlenmişse, ilk olarak döviz bilgilerini sorgulayan bir ekran görüntülenir. Dekont bilgilerinin döviz değerleri ile girilmesi istendiğinde, "Döviz Tipi" ve "Kur" bilgilerinin girilmesi gerekir.

![](../../../../_assets/b7a2e47d44ee184bc2c2.png)

Tamam ![](../../../../_assets/39d77b8716226638d9ce.jpg) butonuna tıklanarak "Genel Gider Cari Hesap Fatura Kaydı" ekranına geçilir.

![](../../../../_assets/9ab60677e50ba7bccf4f.png)

Genel Gider Cari Hesap Fatura Kaydı ekranının alanları ve içerdiği bilgiler aşağıdaki şekildedir:

<table>

<tbody>
<tr>
<th>Genel Gider Cari Hesap Fatura Kaydı Ekranı</th>
<th> </th>
</tr>
<tr>
<td>
<p>Seri Kodu</p>
</td>
<td>
<p>Fatura Serisi (FT) kodunun otomatik olarak aktarıldığı alandır. Kullanıcı tarafından müdahale edilemez.</p>
</td>
</tr>
<tr>
<td>
<p>Dekont No</p>
</td>
<td>

<p>Program tarafından otomatik olarak her bir dekont serisi için 1 rakamından başlar. Kaydedilen her dekont için bir sayı arttırılarak devam eder. Farklı bir numaradan başlaması istendiğinde ise; Dekont → İşlemler → "<a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253Da390a40a-f4e6-42ee-a601-d03e99b93ac9%2526link%253D6a039680-30e4-49ed-a9c2-1ec883feb8f8%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Dekont Numarası Düzenleme</a>" bölümü kullanılarak serilere başlangıç numarası verilir. Rehber butonu <img src="../../../../_assets/088477bb321d1b20c939.jpg"/> ile, kayıtlı dekont numaralarına ulaşılır.</p>

</td>
</tr>
<tr>
<td>
<p>İşlem Tarihi</p>
</td>
<td>
<p>Kaydın girildiği tarihtir. Yapılan kayıtlar, bu alana girilen tarih bazında ilgili modüllere aktarılır.</p>
</td>
</tr>
<tr>
<td>
<p>Fiş Numarası</p>
</td>
<td>
<p>Genel gider cari hesap fatura kaydı için fiş numarası girilen alandır. Bu alana girilen numara, ilgili modüllerdeki "Fiş No" alanına otomatik olarak aktarılır.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>Karşılık Hesap<strong> </strong></p>
</td>
<td colspan="1">
<p>İşlenen evraktaki giderin tek satır olması durumunda <strong>Tek</strong>, birden fazla olması durumunda <strong>Çok</strong> seçeneğinin seçildiği alandır.</p>
</td>
</tr>
<tr>
<td colspan="1">

<p><img src="../../../../_assets/b3a3ada752086d02dc6e.png"/> Gider Kalemleri</p>

</td>
<td colspan="1">

<p>"Karşılık Hesap" sorgulamasından sonra klavye üzerinde yer alan &lt;tab&gt; tuşu ile ilerlendiğinde veya Gider Kalemleri <img src="../../../../_assets/b3a3ada752086d02dc6e.png"/> butonuna tıklandığında "Gider Kalemleri" ekranına geçilir. </p>
<p><img src="../../../../_assets/ca7c68a56c1986582aa4.png"/></p>
<p>Gider Kalemleri ekranının alanları ve içerdiği bilgiler aşağıdaki şekildedir:</p>

<table>
<tbody>
<tr>
<th>Gider Kalemleri Ekranı</th>
<th> </th>
</tr>
<tr>
<td>Girilen Kayıt Sayısı</td>
<td>Gider kalemleri için girilen kayıt sayısının izlendiği alandır.</td>
</tr>
<tr>
<td>Gider Hesap Kodu ve Adı</td>
<td>
Gider kalemlerinin işleneceği hesap kodunun girildiği alandır. Rehber butonu <img src="../../../../_assets/088477bb321d1b20c939.jpg"/> ile, muhasebe hesap kodları arasından seçim yapılır.
</td>
</tr>
<tr>
<td>Referans Kodu</td>
<td>
Muhasebe → Kayıt → Muhasebe Parametreleri → "Fişlerde Referans Kodu Sorulsun" parametresinin işaretlenmesi ile aktif hale gelen alandır. Rehber butonu <img src="../../../../_assets/088477bb321d1b20c939.jpg"/> ile, referans kodları arasından seçim yapılır. Boş bırakılmaz.
</td>
</tr>
<tr>
<td>
<p>Proje Kodu</p>
</td>
<td>

<p>Yardımcı Programlar → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253Dd1958e00-2586-4b57-8a40-dc9812c969ad%2526link%253D2b164138-dbcc-4825-8c16-0ea06ff6c7d8%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Şirket-Şube Parametreleri</a> → "Proje Uygulaması Var" parametresinin işaretlenmesi ile aktif hale gelen alandır. İlgili masrafın yapıldığı proje kodunun girilmesini sağlar. Rehber butonu <img src="../../../../_assets/088477bb321d1b20c939.jpg"/> ile, proje kodları arasından seçim yapılır. Boş bırakılmaz. Girilen proje kodları, cari hareketlere ve entegrasyona aktarılır.</p>

</td>
</tr>
<tr>
<td>Miktar</td>
<td>Dekont → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253Dd69f4164-212a-4596-8715-74903c23d163%2526link%253D74c0c526-a87b-48db-8b3b-4f5d7894b970%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Dekont Parametreleri</a> → "Miktar Girişi Yapılsın" parametresinin işaretlenmesi ile aktif hale gelen alandır. Masraflarla ilgili miktar bilgisi, bu alana girilen miktarla takip edilir.</td>
</tr>
<tr>
<td>Döviz Tutarı</td>
<td>Dekont kaydının döviz değerleri ile yapılması durumunda, "Gider Hesap Kodu" alanına kaydedilecek tutarın döviz cinsinden kaydedildiği alandır. Girilen değer kur ile çarpılarak "Tutar" alanına aktarılır.</td>
</tr>
<tr>
<td colspan="1">KDV Oran</td>
<td colspan="1">Gider kalemi için KDV oranı girilen alandır.</td>
</tr>
<tr>
<td colspan="1">KDV Tutar</td>
<td colspan="1">Döviz bilgisi girilmeden dekont kaydının yapıldığı durumlarda, program tarafından otomatik hesaplanarak aktarılan alandır. Kullanıcı müdahale edemez. </td>
</tr>
<tr>
<td colspan="1">KDV'li Döviz Tutarı</td>
<td colspan="1">Dekont kaydının döviz değerleri ile yapılması durumunda, "Gider Hesap Kodu" alanına kaydedilecek KDV'li tutarın döviz cinsinden kaydedildiği alandır.</td>
</tr>
<tr>
<td colspan="1">KDV Hesap Kodu</td>
<td colspan="1">Gider kalemleri için girilen KDV tutarının aktarılacağı hesap kodunun girildiği alandır. Rehber butonu <img src="../../../../_assets/088477bb321d1b20c939.jpg"/> ile, hesap kodları arasından seçim yapılır.</td>
</tr>
<tr>
<td colspan="1">KDV'siz Tutar</td>
<td colspan="1">Gider kalemleri için KDV'siz tutarın girildiği alandır.</td>
</tr>
<tr>
<td colspan="1">KDV'li Tutar</td>
<td colspan="1">
<p>Gider kalemleri için KDV'li tutarın girildiği alandır.</p>
</td>
</tr>
<tr>
<td colspan="1">KDV'siz Dövizli Tutar</td>
<td colspan="1">Gider kalemleri için KDV'siz dövizli tutarın girildiği alandır.</td>
</tr>
<tr>
<td colspan="1">KDV'li Dövizli Tutar</td>
<td colspan="1">Gider kalemleri için KDV'li dövizli tutarın girildiği alandır.</td>
</tr>
<tr>
<td colspan="1">Açıklama</td>
<td colspan="1">Gider kalemleri için açıklama bilgisi girilen alandır.</td>
</tr>
<tr>
<td colspan="1">Plasiyer Kodu</td>
<td colspan="1">Gider kalemi için plasiyer kodu seçilen alandır. Yardımcı Programlar → Kayıt → Şirket-Şube Parametreleri → "Plasiyer Uygulaması Var" parametresinin seçilmesi ile aktif hale gelen alandır.</td>
</tr>
<tr>
<td colspan="1">B Formu</td>
<td colspan="1">

<p>Dekont tutarının BA/BS bildirimine uygunluğu durumunda işaretlenmesi gereken seçenektir. </p>
						Bilanço esasına göre defter tutan mükelleflerin bir kişi veya kurumdan (KDV hariç) 5.000 TL ve üzerindeki mal ve/veya hizmet alımlarını Mal ve Hizmet Alımlarına İlişkin Bildirim Formu (Form Ba), mal ve/veya hizmet satışlarını ise Mal ve Hizmet Satışlarına İlişkin Bildirim Formu (Form BS) ile (KDV hariç tutarlar dikkate alınarak) bildirme yükümlülüğü bulunur.
</td>
</tr>
<tr>
<td colspan="1"><img src="../../../../_assets/e6ea31e79b2f1cbdcaaf.png"/> Kayıt Sil</td>
<td colspan="1">Grid ekranda oluşan kaydın silinmesi için kullanılan butondur.</td>
</tr>
<tr>
<td colspan="1"><img src="../../../../_assets/39d77b8716226638d9ce.jpg"/> Tamam</td>
<td colspan="1">Girilen bilgilerin kaydedilmesini sağlayan butondur. Butona basıldığında, "Genel Gider Cari Hesap Fatura Kaydı" ekranına geçilerek işlemlere devam edilir.</td>
</tr>
<tr>
<td colspan="1"><img src="../../../../_assets/973111d004995dca0113.jpg"/> İptal</td>
<td colspan="1">Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur.</td>
</tr>
</tbody>
</table>

<p> </p>

</td>
</tr>
<tr>
<td colspan="1">
<p>Cari/Banka</p>
</td>
<td colspan="1">
<p>İşlenen gider karşılığında, alacak çalışacak modülün seçildiği alandır. Cari veya Banka seçeneklerinden biri seçilir.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>Cari/Banka Kodu</p>
</td>
<td colspan="1">
<p>İşlenen gider karşılığı için seçilen cari/banka hesap kodunun girildiği alandır.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>KDV Dahil/Hariç</p>
</td>
<td colspan="1">
<p>"Gider Kalemleri" bölümündeki tutara, KDV rakamının dahil edilmesi istendiğinde "Dahil", KDV rakamının dahil edilmesi istenmediğinde "Hariç" seçeneğinin işaretlendiği alandır. </p>
</td>
</tr>
<tr>
<td colspan="1">
<p>KDV’li Tutar</p>
</td>
<td colspan="1">
<p>KDV oranının girilmesi ile, "Gider Kalemleri" bölümünden kaydedilen tutara KDV eklenerek otomatik aktarılan alandır. Kullanıcı müdahale edemez.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>KDV’li Döviz Tutarı</p>
</td>
<td colspan="1">
<p>KDV oranının girilmesi ile, "Gider Kalemleri" bölümünden kaydedilen döviz tutarına KDV eklenerek otomatik aktarılan alandır. Kullanıcı müdahale edemez.</p>
</td>
</tr>
<tr>
<td colspan="1">KDV Oranı</td>
<td colspan="1">İlgili kayıt için KDV oranı girilen alandır.</td>
</tr>
<tr>
<td colspan="1">
<p>KDV Tutarı</p>
</td>
<td colspan="1">
<p>"KDV Oranı" alanına girilen değerin otomatik olarak aktarıldığı alandır.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>KDV’siz Tutar</p>
</td>
<td colspan="1">
<p>"Gider Kalemleri" bölümünde girilen KDV hariç tutarın otomatik olarak aktarıldığı alandır. Kullanıcı müdahale edemez. </p>
</td>
</tr>
<tr>
<td colspan="1">
<p>KDV’siz Döviz Tutarı</p>
</td>
<td colspan="1">
<p>"Gider Kalemleri" bölümünde girilen KDV hariç döviz tutarının otomatik olarak aktarıldığı alandır. Kullanıcı müdahale edemez. </p>
</td>
</tr>
<tr>
<td colspan="1">
<p>KDV Hesap Kodu</p>
</td>
<td colspan="1">

<p>KDV tutarının muhasebeleşeceği hesap kodunun girildiği alandır. Rehber butonu <img src="../../../../_assets/088477bb321d1b20c939.jpg"/> ile, hesap kodları arasından seçim yapılır.</p>

</td>
</tr>
<tr>
<td colspan="1">
<p>Cari Açıklama/Yevmiye Açıklama</p>
</td>
<td colspan="1">
<p>"Cari Hesap Hareket Kaydı" bölümüne ve yevmiye fişine işlenecek açıklamaların kaydedildiği alandır.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>Ek Açıklama-2/Ek Açıklama-3</p>
</td>
<td colspan="1">
<p>Dekont → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253Dd69f4164-212a-4596-8715-74903c23d163%2526link%253D74c0c526-a87b-48db-8b3b-4f5d7894b970%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Dekont Parametreleri</a> → “Ek Açıklama Bilgi Girişi Yapılsın” parametresinin işaretlenmesi ile aktif hale gelen alanlardır. </p>
</td>
</tr>
<tr>
<td colspan="1">
<p>Cari Rapor Kodu</p>
</td>
<td colspan="1">
<p>Cari → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253D6f1c0005-6726-405d-8ac7-b213b41d23c7%2526link%253Dd50e5347-1966-4bcb-87c7-1d4897ae336e%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Cari Parametreleri</a> → "Hareketlerde Rapor Kodu Girilsin" parametresinin işaretlenmesi ile aktif hale gelen alandır. Hareketlere aktarılması ve raporlanması amacıyla 1 karakterden oluşan rapor kodu girişi yapılır.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>Cari Rapor Kodu-2</p>
</td>
<td colspan="1">
<p>Cari → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253D6f1c0005-6726-405d-8ac7-b213b41d23c7%2526link%253Dd50e5347-1966-4bcb-87c7-1d4897ae336e%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Cari Parametreleri</a> → "Hareketlerde Rapor Kodu Girilsin" parametresinin işaretlenmesi ile aktif hale gelen alandır. Hareketlere aktarılması ve raporlanması amacıyla 15 karakterden oluşan rapor kodu girişi yapılır.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>Plasiyer Kodu</p>
</td>
<td colspan="1">

<p>Yardımcı Programlar → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253Dd1958e00-2586-4b57-8a40-dc9812c969ad%2526link%253D2b164138-dbcc-4825-8c16-0ea06ff6c7d8%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Şirket-Şube Parametreleri</a> → "Plasiyer Uygulaması Var" parametresinin işaretlenmesi ile aktif hale gelen alandır. Dekont kaydı sırasında ilgili plasiyer kodunun girilmesi gerekir. Rehber butonu <img src="../../../../_assets/088477bb321d1b20c939.jpg"/> ile, plasiyer kodlarına ulaşılır. Boş bırakılmaz. </p>

</td>
</tr>
<tr>
<td colspan="1">Miktar</td>
<td colspan="1">Genel gider cari hesap faturası için miktar girilen alandır.</td>
</tr>
<tr>
<td colspan="1">
<p>Valör Başlangıç Tarihi</p>
</td>
<td colspan="1">Dekont → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253Dd69f4164-212a-4596-8715-74903c23d163%2526link%253D74c0c526-a87b-48db-8b3b-4f5d7894b970%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Dekont Parametreleri</a> → "Valör Bilgisi Girişi Yapılsın” parametresinin işaretlenmesi halinde aktif hale gelen alandır. Günün tarihi otomatik olarak ekrana gelir. Elle (manuel) değiştirilmesine izin verilen bu tarih başlangıç kabul edilip, valör gününün bu tarihe eklenmesi ile yeni bir tarih hesaplanır.</td>
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
<p>Vadelere Bölünsün</p>
</td>
<td colspan="1">

<p>Kaydedilen dekont tutarının, cari hareket kayıtlarına, kullanıcı tarafından belirlenen vade sayısı kadar bölünerek birden fazla kayıt halinde işlenmesi için işaretlenen seçenektir. Dekont kaydı sırasında açılan ekranda "Vade Günü" ve "Oran (Yüzde)" alanları sorgulanır. </p>
<p>"Vadelere Bölünsün" seçeneği, "Hesap Kodu" alanına "Muhasebe Kodu" girildiği zaman aktif hale gelmez.</p>
<p><img src="../../../../_assets/32b5efab4b1348777c04.png"/></p>
<p>Cari Hesap Vade Oranları ekranının alanları ve içerdiği bilgiler aşağıdaki şekildedir:</p>

<table>
<thead>
<tr>
<th>
<p>Cari Hesap Vade Oranları Ekranı</p>
</th>
<th> </th>
</tr>
</thead>
<tbody>
<tr>
<td>Peşinat Tutarı</td>
<td>Taksitli satış bilgileri için peşinat tutarı girilen alandır.</td>
</tr>
<tr>
<td>Taksit Sayısı</td>
<td>Taksitli satış bilgileri için taksit sayısı girilen alandır.</td>
</tr>
<tr>
<td colspan="1">
<img src="../../../../_assets/d17849675b68554265fa.png"/> Taksitleri Oluştur
</td>
<td colspan="1">

<p>"Peşinat Tutarı" ve "Taksit Sayısı" girildikten sonra taksitlerin oluşturulması için kullanılan butondur.</p>
<p><strong>Örneğin: </strong>50 TL tutarındaki bir dekontun peşinat tutarının 20 TL, taksit sayısının ise 2 olarak girildiği varsayıldığında, oluşturulan taksit grid ekrana aşağıdaki şekilde yansır.</p>
<p><img src="../../../../_assets/1f2c5ea5b2860f1a7829.png"/></p>
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
<p><img src="../../../../_assets/f0f666e74e37ee309ee4.png"/></p>

</td>
</tr>
<tr>
<td>
<img src="../../../../_assets/4f2c70e38891c33ca4ba.png"/> Tamam
</td>
<td>Girilen bilgilerin kaydedilmesi için kullanılan butondur.</td>
</tr>
<tr>
<td>
<img src="../../../../_assets/5d28b2685d1d5f39a70f.png"/> Satır Sil
</td>
<td>
Grid ekranda oluşan taksit satırının silinmesi için kullanılan butondur. Satır Sil <img src="../../../../_assets/5d28b2685d1d5f39a70f.png"/> butonu, ekrandaki alanlara bilgi girişi yapıldıktan sonra Tamam <img src="../../../../_assets/4f2c70e38891c33ca4ba.png"/> butonu ile girilen bilgiler kaydedilip dekont ekranındaki "Vadelere Bölünsün" seçeneğine tıklandığında aktif hale gelir.
</td>
</tr>
</tbody>
</table>

</td>
</tr>
<tr>
<td colspan="1">
<p>Vade Tarihi</p>
</td>
<td colspan="1">
<p>Valör başlangıç tarihine valör gününün eklenmesi ile bulunan tarihin otomatik olarak aktarıldığı alandır. Girilen tarih, ilgili cari hesabın hareket kayıtlarındaki "Vade Tarihi" alanına aktarılır.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>Proje Kodu</p>
</td>
<td colspan="1">

<p>Yardımcı Programlar → Kayıt → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253Dd1958e00-2586-4b57-8a40-dc9812c969ad%2526link%253D2b164138-dbcc-4825-8c16-0ea06ff6c7d8%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Şirket-Şube Parametreleri</a> → "Proje Uygulaması Var" parametresinin işaretlenmesi ile aktif hale gelen alandır. Dekont kaydı sırasında ilgili plasiyer kodunun girilmesi gerekir. Rehber butonu <img src="../../../../_assets/088477bb321d1b20c939.jpg"/> ile, proje kodlarına ulaşılır. Boş bırakılmaz. Girilen proje kodları, cari hareketlere ve entegrasyona aktarılır.</p>

</td>
</tr>
<tr>
<td colspan="1">
<p>Muhasebeleştirme</p>
</td>
<td colspan="1">
<p>Muhasebe ile entegre çalışıldığı durumlarda, dekont kaydına ait mahsubun, Entegrasyon Modülünde hangi mahsuba aktarılacağını sorgulayan alandır. Yapılacak seçime göre, ilgili muhasebe kaydı "<strong>Dekont Mahsubuna</strong> "veya "<strong>Satıcı/Müşteri Alacak Mahsubuna</strong>" aktarılır.</p>
</td>
</tr>
<tr>
<td colspan="1">
<p>Basım</p>
</td>
<td colspan="1">
<p>Kaydı yapılan dekontun standart basımının yapılması için kullanılan seçenektir. </p>
</td>
</tr>
</tbody>
</table>

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır. Kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
