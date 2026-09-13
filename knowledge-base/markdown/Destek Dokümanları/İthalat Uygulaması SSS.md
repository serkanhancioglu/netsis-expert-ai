---
title: "İthalat Uygulaması SSS"
page_id: "98960217"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "İthalat Uygulaması SSS"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / İthalat Uygulaması SSS"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTZiZDFjZWJkLWMzNmItNDA2My1hMDY2LWE0Y2YwZjA4MzRmNyZsaW5rPTlhNmVlNzMyLTJhMGMtNGIzMy05MmFmLTFlYjVkOTVjYzNmNSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=6bd1cebd-c36b-4063-a066-a4cf0f0834f7&link=9a6ee732-2a0c-4b33-92af-1eb5d95cc3f5&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ithalat-uygulamasi-sss_98960222_98960217.html"
source_version: "2022-12-02T16:41:28.257+03:00"
source_bytes: 915242
fetched_at: "2026-09-13T04:23:47+00:00"
generator: "netsis-scraper 1.0.0"
---
# İthalat Uygulaması SSS

**Soru 1: İthalat/İhracat dosya işlemlerinde seçilen belgelerin yeni grid görünümü yerine, eski html görünümle görüntülenmesi için ne yapılmalıdır?**

**DISTICARET/HTMLGORUNUM/0** özel parametresinin tanımlanması gerekmektedir. Bu özel parametre tanımlanınca aşağıdaki html görünümü gelmektedir.

![](../_assets/5664495fe7faeff2c666.png)

**Soru 2: Dış ticaret modülünde DISTICARET/SAYFAYENILENMESIN özel parametresi ne işe yarar?**

**DISTICARET/SAYFAYENILENMESIN** özel parametresiyle, dış ticaret modülünde ithalat dosyasında gride veri getirmede dosyaya her belge bağlama işlemi sonrası güncel belgeleri getirmek için çıkan popup ekranın kullanıcı istediğinde görüntülenmesi sağlanmıştır. **Yenile** butonu eklenmiş olup, Yenile butonuna basılarak kullanıcının isteğine göre kısıt ekranı getirilmektedir.

![](../_assets/b5d6268337f53068f03d.png)

**Soru 3: İthalat sürecinde oluşan alış irsaliyesi sonrasında stok hareketlerinde irsaliye** **miktarının takip edilebilmesi için ne yapılmalıdır?**

Dış ticaret modülü kullanımında, Dış Ticaret Parametreleri ekranında "**İthalat Miktarları Stoklara** **Geçsin**" parametresinin, fatura-dekont modülleri kullanımında Alış Fatura Parametreleri\>İthalat sekmesinde "**Yurt** **Dışı** **Tipli** **Alış** **İrsaliyelerinde** **Miktarlar** **Stoklara** **Geçsin**" parametresinin işaretlenmesi gerekir.

**Soru 4: Parçalı İthalat kapatma adımında, ithalat kapatma sonrası Depolar Arası Transfer belgesi oluşturulması için ne yapılmalıdır?**

İthalat kapatma ekranında **Depo** **Kodu** alanına, Alış irsaliyesi belgesinde girilen depo kodundan farklı bir depo kodu girildiğinde parçalı ithalat kapatma sonrasında alış irsaliyesindeki depodan, ithalat kapatma ekranında girilen depoya Depolar Arası Transfer kaydı yapılmaktadır. Depo kodu boş geçildiğinde, parçalı ithalat kapatma sonrası transfer işlemi yapılmamaktadır.

![](../_assets/28004fa566aef894cfc9.png)

**Soru 5: İthalat sürecinde, alış irsaliyesinin tarihi ve kur bilgisi, mal bedeli dekontunun tarihi ve kur bilgisinden farklı olduğu durumda oluşan kur farkının tüm kalemlere dağıtılması için ne yapılır?**

**ITHALAT\* \*YUVARLAMAFARKINISONKALEMEDAGITILMASIN** özel parametresi tanımlıyken, İthalat Kapatma sonrası alış faturasındaki kalemlere kur farkı tutarı eşit olarak dağıtılmaktadır.

**Soru 6: İthalat kapatma sırasında kullanılan dağıtım yöntemleri nelerdir?**

**Miktarlara göre** ve **Birim Ağırlıklara** göre yapılan dağıtım yöntemleri ithalat kapatma sırasında tüm kalemlere aynı dağıtım yöntemi uygulanmaktadır.

İthalat Masraf Dekon Kayıtları ekranında yer alan **Eşit** **Dağıtılsın,** **Serbest** **Yüzde,** **Serbest** **Tutar** **ve Birim** **Ağırlık\*Fiyat** dağıtım yöntemleri ise, stok kalemi bazında istenilen dağıtım yöntemi uygulanmaktadır.

**Soru 7: Alış irsaliyesi ithalat faturasına dönüştürüldüğünde oluşan alış faturası cariye yansır mı?**

Dış ticaret modül kullanımında dosya içinden ithalat kapatma yapıldığında oluşan alış faturası cari hareket kayıtlarına yansımaz. İthalat kapatma öncesi oluşturulan mal bedeli dekontu cari hareket kayıtlarına yansır. Benzer şekilde fatura-dekont modülü kullanımında alış irsaliyesi girişi sonrasında genel dekont kaydından oluşturulan mal bedeli dekontu cari hareket kayıtlarına yansır.
Fatura modülünden girilen alış irsaliyesi sonrası, alış irsaliyesi toplamlar sekmesinde **İth** butonuna basılarak oluşturulan ithalat faturası sonrası cari hareket kayıtlarına ithalat faturası yansır.

**Soru 8: İthalat Masraf Dekont kayıtlarından girilen masraf tutarları muhasebeye kümüle olarak atılabilir mi?**

İthalat parametrelerinde, "**Masraf Dekont Kayıtları** **Kümüle** **Edilsin**" parametresinin işaretlenmesi gereklidir. Bu parametre ithalata ait girilen masraflar için, aynı dosya içine girilen masraf kayıtlarının muhasebeye atılırken kümüle olarak atılabilmesi için gerekli bir parametredir. Ancak bu kümülasyon belli kriterlere göre olur. Dosya numarası (Export Ref. No), Masraf Kodu, Vade Tarihi, Proje Kodu, Referans Kodu, Belge Tipi ve Döviz Tipi bilgisi aynı olan masraf satırları kümüle edilerek muhasebeye kümüle olarak aktarılır.

**Soru 9: İthalat sürecine ait gümrük, komisyon, sigorta, ardiye, vb masraf tutarlarının ürünlerin birim fiyatlarına yansıması için ne yapılmalıdır?**

İthalat sürecine ait gümrük, komisyon, sigorta, ardiye, vb masraf tutarlarının ürünlerin birim fiyatlarına yansıması için, masraf dekontlarında, masraf tutarlarının159 veya 259 lu muhasebe hesaplarına girilmesi gerekir.

**Soru 10: İthalat sürecinde bedelsiz kalemlere masraf tutarları dağıtılabilir mi?**

İthalat kapatma ekranında "**İthalat** **masrafları** **bedelsiz** **kalemlere** **dağıtılsın**" parametresi işaretlenmeden kapatma yapıldığında bedelsiz kaleme masraf dağıtımı yapılmamaktadır. Ancak parametre işaretlenerek kapatma yapıldığında bedelsiz kaleme de masraf dağıtımı yapılacaktır.
