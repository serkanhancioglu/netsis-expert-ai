---
title: "Kalite Kontrol Kaydı"
page_id: "22804208"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Kalite - Kontrol"
  - "Kayıt / Kalite Kontrol"
  - "Kalite Kontrol Kaydı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Kalite - Kontrol / Kayıt / Kalite Kontrol / Kalite Kontrol Kaydı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWUxZDNlMWRjLTUxYzctNGIzNS04OTYxLTUzZTY4NmFiY2Y2NCZsaW5rPTBhNjU1ZjkxLTBjZTItNDlkZC05NDQ3LTYyNWFmMjAxY2FjNyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=e1d3e1dc-51c7-4b35-8961-53e686abcf64&link=0a655f91-0ce2-49dd-9447-625af201cac7&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "kalite-kontrol-kaydi_28148430_22804208.html"
source_version: "2022-10-25T09:19:49.923+03:00"
source_bytes: 217802
fetched_at: "2026-09-13T04:06:37+00:00"
generator: "netsis-scraper 1.0.0"
---
# Kalite Kontrol Kaydı

Kalite Kontrol Kaydı, Lojistik - Satış Bölümü'nde, "Kayıt/Kalite Kontrol" menüsünün altında yer alır. Kalite kontrol belgesi oluşturmak için kullanılır.

Kalite kontrol kaydı sırasında "Genel Bilgiler" sekmesindeki alanların üzerinden \<tab\> tuşu ile değer girişi yapılmadan geçilebilir. Kalite kontrol kayıtlarının tamamlanmasının ardından kabul edilen, reddedilen ve hurdaya ayrılan stokların miktarları program tarafından burada bulunan ilgili alanlara otomatik olarak aktarılır.

[Kalite Kontrol Parametreleri](<Kalite Kontrol Parametreleri.md>)nde bulunan "Kalite Kontrol Numune Aralıkları Tanımlama" parametresinin işaretli olması halinde, "Muayene Kodu" alanı ekrana eklenir ve bu alan boş bırakılamaz. Kalite kontrol kaydının hangi muayene kodu için grup aralıkları bazında oluşturulacağının belirlenmesini sağlar.

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır.

Kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.

![](../../../../_assets/47b1078e15424749888f.png)

Kalite Kontrol Kaydı ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

<table>

<tbody>
<tr>
<th>Kalite Kontrol Kaydı Ekranı</th>
<th> </th>
</tr>
<tr>
<td colspan="1">Personel Kodu</td>
<td colspan="1">

<p>Kalite kontrol yapan personel kodunun girildiği alandır. Rehber butonu <img src="../../../../_assets/088477bb321d1b20c939.jpg"/> ile personel kodları arasından seçim yapılabilir.</p>

</td>
</tr>
<tr>
<td colspan="1">Departman Kodu</td>
<td colspan="1">

<p>Kalite kontrol yapan departman kodunun girildiği alandır. Rehber butonu <img src="../../../../_assets/088477bb321d1b20c939.jpg"/> ile departman kodları arasından seçim yapılabilir.</p>

</td>
</tr>
<tr>
<td colspan="1">Belge Tipi</td>
<td colspan="1">Kalite kontrol yapılan belge tipinin belirlendiği alandır. Alanın sağ tarafında bulunan aşağı ok tuşu yardımıyla belge tipleri arasından seçim yapılır. Alış İrsaliyesi, Müstahsil Faturası, Depolar Arası Transfer ve Ambar Giriş Fişi olmak üzere dört adet belge tipi seçeneği bulunur.</td>
</tr>
<tr>
<td colspan="1">Belge Numarası</td>
<td colspan="1">

<p>Kalite kontrol kaydı yapılacak belge numarasının girildiği alandır. Rehber butonu <img src="../../../../_assets/088477bb321d1b20c939.jpg"/> ile belge numaraları arasından seçim yapılabilir.</p>

</td>
</tr>
<tr>
<td colspan="1">Sıra No</td>
<td colspan="1">Sıra numarasının girildiği alandır.</td>
</tr>
<tr>
<td>Kalite Kontrol Numarası</td>
<td>
<p>Kalite kontrol kaydına ait, programın oluşturduğu kalite kontrol numarasıdır. Kalite kontrol numaraları; "Genel Bilgiler" sekmesindeki ekranında girilen departmana ait,  “Kalite Kontrol Departman Girişi” bölümünde tanımlanan seri karakter ile başlar ve sırası ile arttırılır. Kullanıcıların, bu numaralara müdahale etme hakkı yoktur. S0000001, S00000002..gibi.</p>
<p>Kalite Kontrol Parametreleri bölümünde bulunan “Kalite Kontrol Hareketleri Otomatik Oluşsun” parametresinin işaretlenmiş olması halinde, örnekler program tarafından oluşturulur. Örneklerin miktarlarının ne kadar olacağı <a href="https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/external%253Fcid%253Dac515097-c668-48b3-8302-ba840a90cb76%2526link%253D4124d7ba-f59d-4381-b150-6b00265dd0aa%2526tenantId%253Dcdd87e13-3009-4dd1-a5b8-2a005c0e58da%2526hideName%253DTrue">Kalite Grup Tanımlamaları</a> bölümünde belirlenir.</p>
</td>
</tr>
<tr>
<td colspan="1">Bitiş Tarihi</td>
<td colspan="1">Kalite kontrol işlemine ait bitiş tarihi bilgisinin girildiği alandır. Tarih ve saat bilgisi kullanıcı tarafından istenilen şekilde ayarlanabilir.</td>
</tr>
<tr>
<td colspan="1">Muayene Kodu</td>
<td colspan="1">

<p>Kalite kontrol kayıt işlemi için muayene kodu bilgisinin girildiği alandır. Rehber butonu <img src="../../../../_assets/088477bb321d1b20c939.jpg"/> ile muayene kodları arasından seçim yapılabilir.</p>

</td>
</tr>
<tr>
<td colspan="1">Grup Kodu</td>
<td colspan="1">

<p>Kalite kontrol kayıt işlemi için grup kodu bilgisinin girildiği alandır. Rehber butonu <img src="../../../../_assets/088477bb321d1b20c939.jpg"/> ile grup kodları arasından seçim yapılabilir.</p>

</td>
</tr>
<tr>
<td colspan="1">Kabul Miktarı/Önerilen</td>
<td colspan="1">Kalite kontrol kaydı yapılan işleme ait kabul edilen/önerilen miktarın girildiği alandır.</td>
</tr>
<tr>
<td colspan="1">Red Miktarı/Önerilen</td>
<td colspan="1">Kalite kontrol kaydı yapılan işleme ait reddedilen/önerilen miktarın girildiği alandır.</td>
</tr>
<tr>
<td colspan="1">Hurda Miktarı/Önerilen</td>
<td colspan="1">Kalite kontrol kaydı yapılan işleme ait hurdaya ayrılan/önerilen miktarın girildiği alandır.</td>
</tr>
<tr>
<td colspan="1">Şartlı Kabul Miktarı/Önerilen</td>
<td colspan="1">Kalite kontrol kaydı yapılan işleme ait şartlı kabul edilen/önerilen miktarın girildiği alandır.</td>
</tr>
<tr>
<td colspan="1">

<p>Kayıt Kapama</p>

</td>
<td colspan="1">

<p>Butona basıldığında "Kayıt Kapama" penceresi ekrana gelir.</p>
<p><img src="../../../../_assets/c1f0ee67635c37ddc6ce.png"/></p>
<p>Kalite kontrol kaydı yapılan belgeye ait Hepsi Kabul, Hepsi Red, Hepsi Şartlı Kabul, Girilen Miktarlar, Önerilen Miktarlar seçeneklerinden biri işaretlenerek Tamam butonuna basıldığında, "Kalite Kontrol Depolar Arası Transfer" penceresi ekrana gelir.</p>

</td>
</tr>
<tr>
<td colspan="1">

<p>Depolar Arası Transfer</p>

</td>
<td colspan="1">

<p>Kalite kontrol kaydı oluşturulan belgeye ait depolar arası transfer işlemi gerçekleştirmek için ekrandaki "D.A.T Fişleri İçin Seri" alanına bilgi girişi yapıldıktan sonra Tamam butonuna basılarak işlem tamamlanır.</p>
<p><img src="../../../../_assets/806a98dd255244bb9102.png"/></p>

</td>
</tr>
<tr>
<td colspan="1">

<p>Ölçüm Kayıtları</p>

</td>
<td colspan="1">

<p>Butona basıldığında Kalite Kontrol Kaydı ekranına "Ölçüm Kayıtları" sekmesi eklenir. Kontrolü yapan, kontrol edilen miktar, ölçü birimi, kabul/red miktarı gibi bilgileri içerir. Numunelerin her birine ait ölçüm bilgilerinin girilebileceği ekrandır.  Hareket kayıtları, kalite kontrol genel bilgiler kaydı yapıldıktan sonra kullanıcı tarafından grid üzerindeki kaydı seçtikten sonra sağ klik tuşu ile ekrana gelen <strong>"Kalite Kontrol Hareketlerini Oluştur"</strong> işleminin başlatılması ile oluşturulur. </p>
<p><img src="../../../../_assets/d5b2092b11e172398c4d.png"/></p>
<p>Kalite Kontrol Kaydı ekranı Ölçüm Kayıtları sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:</p>

<table>
<tbody>
<tr>
<th>Kalite Kontrol Kaydı Ekranı</th>
<th>Ölçüm Kayıtları</th>
</tr>
<tr>
<td>Hareket Bilgileri</td>
<td>Alanın sol tarafında bulunan <img alt="(plus)" src="../../../../_assets/8bc1079dc378a6219e99.svg"/> artı butonuna tıklanarak yeni hareket bilgileri girilmesi için alanların açılması sağlanır.</td>
</tr>
<tr>
<td>Sıra</td>
<td>Hareket sıra numarasının izlendiği alandır.</td>
</tr>
<tr>
<td>KK Tarihi</td>
<td>Seçilen numuneye ait kalite kontrol tarihinin girildiği alandır.</td>
</tr>
<tr>
<td colspan="1">Kontrol Edilen Miktar</td>
<td colspan="1">Seçilen numuneye ait kontrol edilen miktarın girildiği alandır.</td>
</tr>
<tr>
<td colspan="1">Ölçü Birimi</td>
<td colspan="1">Seçilen numuneye ait ölçü biriminin girildiği alandır.</td>
</tr>
<tr>
<td colspan="1">Kabul/Red/Şartlı Kabul Miktarı</td>
<td colspan="1">Seçilen numuneye ait Kabul/Red/Şartlı Kabul Miktarının girildiği alandır.</td>
</tr>
<tr>
<td colspan="1">Hurda Miktarı</td>
<td colspan="1">Seçilen numuneye ait hurda miktarının girildiği alandır.</td>
</tr>
<tr>
<td colspan="1">Durumu</td>
<td colspan="1">Numunenin durumunun girildiği alandır. Hiçbiri, Kabul, Red, Şartlı Kabul seçeneklerinden biri seçilebilir.</td>
</tr>
<tr>
<td colspan="1">Açıklama</td>
<td colspan="1">Seçilen numuneye ait kalite kontrol açıklamasının girildiği alandır.</td>
</tr>
</tbody>
</table>

<p><strong>Ölçüm Hareketlerini Yansıt Özel Tuşu</strong></p>
<p>Ölçüm hareketlerini yansıt tuşu, hareket kayıtları, kalite kontrol genel bilgiler kaydı yapıldıktan sonra kullanıcı tarafından grid üzerindeki kaydı seçtikten sonra sağ klik tuşu ile ekrana gelir.</p>
<p><strong><img src="../../../../_assets/e205bd010f5b9ccd2673.png"/></strong></p>
<p><strong><img src="../../../../_assets/5203de8299c05c808f18.png"/></strong></p>
<p>Mevcut ölçüm bilgileri diğer hareket ölçümlerine yansıtılacaktır sorusu onaylandığında, ölçüm bilgileri diğer hareket ölçümlerinin tümüne aktarılır.</p>

</td>
</tr>
<tr>
<td colspan="1">

<p>Fiş Basımı</p>

</td>
<td colspan="1">Kalite kontrol kayıt fişi basımı için kullanılan butondur.</td>
</tr>
</tbody>
</table>
