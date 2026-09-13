---
title: "Havale/Eft İşlemlerinde Kullanılan Özel Tuşlar"
page_id: "22806135"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Banka"
  - "Kayıt / Banka"
  - "Havale - EFT Kayıtları"
  - "Havale/Eft İşlemlerinde Kullanılan Özel Tuşlar"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Banka / Kayıt / Banka / Havale - EFT Kayıtları / Havale/Eft İşlemlerinde Kullanılan Özel Tuşlar"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWMyNjdmMmRlLTM5ODYtNDdhZi1iMzU4LWVmMTE0NTBmNmE1YSZsaW5rPTExOGQyZjBmLTQzZjYtNGVkZS1iMDFiLWY3ZTVmNTJjNzAzYyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=c267f2de-3986-47af-b358-ef11450f6a5a&link=118d2f0f-43f6-4ede-b01b-f7e5f52c703c&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "havale-eft-islemlerinde-kullanilan-ozel-tuslar_34220678_22806135.html"
source_version: "2022-04-04T09:27:44.470+03:00"
source_bytes: 591413
fetched_at: "2026-09-13T04:09:50+00:00"
generator: "netsis-scraper 1.0.0"
---
# Havale/Eft İşlemlerinde Kullanılan Özel Tuşlar

Havale/EFT işlemleri ile ilgili bölümlerin "Virman Bilgileri" sekmesinde kullanılan yardımcı tuşlar, ekran üzerinde iken farenin sağ tuşu ile ekrana gelir.

![](../../../../../_assets/662c9bc87a9ac1aad967.png)

Havale/Eft İşlemlerinde Kullanılan Özel Tuşlar ekranındaki menü seçenekleri aşağıdaki şekildedir:

<table>

<tbody>
<tr>
<th>Havale/EFT İşlemlerinde Kullanılan Özel Tuşlar</th>
<th> </th>
</tr>
<tr>
<td>Kaydı İptal Et</td>
<td>Yapılan Havale/EFT işleminin direkt olarak iptal edilmesini ve kaydın tamamen silinmesini sağlayan seçenektir.</td>
</tr>
<tr>
<td>Havale/EFT Basımı</td>
<td>

<p>Yapılan Havale/EFT kayıtlarına ait "Dizayn Modülü" bölümünden hazırlanan dizaynın basılmasını sağlayan seçenektir. İlgili basımın seçilmesi ile birlikte "Dizayn Sorgulama" ekranı görüntülenir.</p>
<p><img src="../../../../../_assets/a04283e1ad8f8a0754bd.png"/></p>

</td>
</tr>
<tr>
<td>Toplu Havale/EFT Basım Sorgulama</td>
<td>

<p>Yapılan Havale/EFT kayıtlarına ait "Dizayn Modülü" bölümünden hazırlanan dekontun basılmasını sağlayan seçenektir. Toplu Havale/EFT Basım Sorgulama ekranında yer alan "Dekont No" ve "İşlem Tarihi" alanlarına bilgi girişi yapıldıktan sonra ilgili basımın seçileceği "Dizayn Sorgulama" ekranı görüntülenir.</p>
<p><img src="../../../../../_assets/b45d6bff9e45fdf402f7.png"/><img src="../../../../../_assets/649c6b3177566671c1c6.png"/></p>

</td>
</tr>
<tr>
<td colspan="1">
<p>Havale/EFT Talimat Basımı</p>
<p>Toplu Havale/EFT Basımı</p>
</td>
<td colspan="1">

<p>Yapılan Havale/EFT kayıtları için bankaya bildirilecek talimat basımlarının yapılmasını sağlayan seçenektir.</p>
<p><img src="../../../../../_assets/23d4238727375e73c769.png"/></p>
<p>"Microsoft Word" programının desteklediği "Merge" kavramı kullanılarak talimat basımının yapılması sağlanır. İlgili basımı gerçekleştirmek için "Word" programında bir şablon hazırlanarak .doc uzantısı ile hazırlanan şablonun saklanması gerekir. Şablon, "Merge" alanları kullanılarak hazırlanır. Merge Field eklemek için, "Word" ekranındaki "Insert" menüsünün altında yer alan "Field" seçeneğinin seçilmesi ve gelen ekrandan Field ismi olarak "Merge Field" isminin seçilmesi gerekir. Merge Field için Logo Netsis programı tarafından desteklenen standart alan isimleri verilir. Bu alan isimlerinin ve anlamlarının aşağıdaki gibi olması gerekir.</p>

<table>
<tbody>
<tr>
<th><strong>Merge </strong><strong>Alan Adı</strong></th>
<th><strong>Açıklama</strong></th>
</tr>
<tr>
<td><strong>nmfsirketismi</strong></td>
<td> Genel Parametre kayıtlarında girilen şirket unvanıdır.</td>
</tr>
<tr>
<td><strong>nmftarih</strong></td>
<td> Havale/EFT için verilen efektif tarihidir.</td>
</tr>
<tr>
<td>
<p><strong>nmfbankaismi</strong></p>
</td>
<td> Havale/EFT için seçilen banka hesabına ait ana hesap tanımı sırasında girilen isimdir.</td>
</tr>
<tr>
<td>
<p><strong>nmfbankasubeismi</strong></p>
</td>
<td> Havale/EFT için seçilen banka hesabına ait şube hesap tanımı sırasında girilen isimdir.</td>
</tr>
<tr>
<td><strong>nmftcmbbankaismi</strong></td>
<td> Havale/EFT için seçilen hesabın Merkez Bankası rehberindeki ismidir.</td>
</tr>
<tr>
<td><strong>nmftcmbbankasubeismi</strong></td>
<td> Havale/EFT için seçilen hesabın Merkez Bankası rehberindeki şube ismidir.</td>
</tr>
<tr>
<td><strong>nmfmusterino</strong></td>
<td> Havale/EFT için seçilen hesabın ana hesap tanımında girilen müşteri numarasıdır.</td>
</tr>
<tr>
<td><strong>nmfcarivergidairesi</strong></td>
<td> Havale/EFT yapılan müşteri/satıcı vergi dairesidir.</td>
</tr>
<tr>
<td><strong>nmfcarivergino</strong></td>
<td> Havale/EFT yapılan müşteri/satıcı vergi numarasıdır.</td>
</tr>
<tr>
<td><strong>nmfbankahesno</strong></td>
<td> Havale/EFT için seçilen hesabın banka hesap tanımı sırasında girilen hesap numarasıdır.</td>
</tr>
<tr>
<td><strong>nmfswiftkodu</strong></td>
<td> Havale/EFT için seçilen hesabın ana hesap tanımında girilen ülkeler arası için gerekli olan swift kodudur.</td>
</tr>
<tr>
<td><strong>nmfulkeismi</strong></td>
<td> Havale/EFT için seçilen hesabın banka şube tanımları sırasında girilen ülke ismidir.</td>
</tr>
<tr>
<td><strong>nmfsehirismi</strong></td>
<td> Havale/EFT için seçilen hesabın banka şube tanımları sırasında girilen şehir ismidir.</td>
</tr>
<tr>
<td><strong>nmfislemtarih</strong></td>
<td> Havale/EFT işlemi için girilen tarihtir.</td>
</tr>
<tr>
<td><strong>nmfkarsicariismi</strong></td>
<td> Havale/EFT yapılan carinin ismidir.</td>
</tr>
<tr>
<td><strong>nmfkarsibankaismi</strong></td>
<td> Havale/EFT yapılan cari için girilen bankanın ismidir.</td>
</tr>
<tr>
<td><strong>nmfkarsibankasubeismi</strong></td>
<td> Havale/EFT yapılan cari için girilen banka şubesinin ismidir.</td>
</tr>
<tr>
<td><strong>nmfkarsibankahesno</strong></td>
<td> Havale/EFT yapılan carinin banka hesap numarasıdır.</td>
</tr>
<tr>
<td><strong>nmfkarsiswiftkodu</strong></td>
<td> Havale/EFT yapılan cari için girilen hesabın ülkeler arası işlem için gerekli olan swift kodudur. Kodlar, T.C.M.B. kayıtlarından alınır.</td>
</tr>
<tr>
<td><strong>nmfkarsiulkeismi</strong></td>
<td> Havale/EFT yapılan cari için girilen hesabın ülke ismidir. T.C.M.B. kayıtlarından alınır.</td>
</tr>
<tr>
<td><strong>nmfkarsisehirismi</strong></td>
<td> Havale/EFT yapılan cari için girilen hesabın şehir ismidir. T.C.M.B. kayıtlarından alınır.</td>
</tr>
<tr>
<td><strong>nmfdovizismi</strong></td>
<td> Yapılan Havale/EFT işlemi sırasında girilen döviz tipinin ismidir.</td>
</tr>
<tr>
<td><strong>nmfdoviztutar</strong></td>
<td> Yapılan Havale/EFT işlemi sırasında girilen döviz tutarıdır.</td>
</tr>
<tr>
<td><strong>nmftutar</strong></td>
<td> Yapılan Havale/EFT işlemi sırasında girilen tutardır.</td>
</tr>
<tr>
<td><strong>nmftoplamtutar</strong><br/>
						 </td>
<td>Toplu talimat basımı için kullanılan alandır. Birden fazla yapılan Havale/EFT işleminin toplam tutarının basılması için gerekli olan alandır. </td>
</tr>
<tr>
<td><strong>nmftoplamdoviztutar</strong><br/>
						 </td>
<td>Toplu talimat basımı için kullanılan alandır. Birden fazla yapılan Havale/EFT işleminin toplam döviz tutarının basılması için gerekli olan alandır. </td>
</tr>
</tbody>
</table>

			Toplu talimat basımının yapılması için "Word" programında hazırlanan şablonda "Merge Field" mutlaka bir tablo içinde girilir.
</td>
</tr>
<tr>
<td colspan="1">Cari Hareket İzleme</td>
<td colspan="1">Havale/EFT işlemi ile ilgili cari hareketlerin izlenmesini sağlayan seçenektir.</td>
</tr>
<tr>
<td colspan="1">Gruplama</td>
<td colspan="1">

<p>Grid ekran üzerinde yer alan kolon başlıklarının ilgili yere sürüklenerek gruplama yapılmasını sağlayan seçenektir.</p>
<p><strong>Örneğin: </strong>Aşağıdaki ekranda "Tutar" kolon başlığının ilgili alana sürüklenmesi ile tutarların gruplanması sağlanabilir.</p>
<p><img src="../../../../../_assets/adec4ab2ad3db1563001.png"/></p>
<p>Veya, kolon başlığının yanında yer alan aşağı ok butonu ile "filtreleme" işlemi yapılabilir.</p>
<p><img src="../../../../../_assets/6085eee1d1a4880abb52.png"/></p>

</td>
</tr>
<tr>
<td colspan="1">Gönder</td>
<td colspan="1">
<p>İlgili Havale/EFT kaydının "Excel" tablosuna gönderilmesini sağlayan seçenektir.</p>
<p>Detaylı bilgi için; Giriş → Kayıt Ekranları Kullanımı → Grid → <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253D659755e5-df2b-4d12-a4bb-1174d578eeeb%2526link%253Dce7addd9-fed2-4a99-b46c-9e2a90a75c36%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Bilgi Gönderimi</a>.</p>
</td>
</tr>
<tr>
<td colspan="1">Görünüm Ayarları</td>
<td colspan="1">Grid ekrandan seçilen harekete ait sağ fare tuşu ile ekrana gelen "Görünüm Ayarları" seçeneği sayesinde, grid ekranında yer alan herhangi bir kolonun manuel şekilde ayarlanan görünümünün saklanmasını veya standart görünümüne dönmesi sağlanır.</td>
</tr>
<tr>
<td>Kolonları Sığdır</td>
<td>Grid ekrandan seçilen harekete ait sağ fare tuşu ile ekrana gelen "Kolonları Sığdır" seçeneği sayesinde, grid ekranında yer alan kolonların boyutu, sütunda yazan bilgilerin uzunluk boyutuna göre ayarlanır.</td>
</tr>
<tr>
<td colspan="1">Karşılıksız Çek/Senet Ödemesi</td>
<td colspan="1">"Karşılıksız" duruma geçen çekler ve senetler için tahsilat işlemlerinin yapılmasını sağlayan seçenektir.  Bu ekran ile karşılıksız kaydı yapılmış çekler ile yapılan tahsilatların TL ve döviz cinsinden eşleştirilmesi de sağlanır. </td>
</tr>
</tbody>
</table>
