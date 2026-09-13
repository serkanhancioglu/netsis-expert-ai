---
title: "Hizmet Prim Tanımlama"
page_id: "22805123"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Cari"
  - "Kayıt / Cari"
  - "Hizmet Bilgileri Girişi"
  - "Hizmet Prim Tanımlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Cari / Kayıt / Cari / Hizmet Bilgileri Girişi / Hizmet Prim Tanımlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWIyNTkwNDA4LWQwYTgtNGRmOS05NjBiLTM4Mjc3MzFkYjc5NiZsaW5rPTE2Yjc3ZDk0LWU5ZGQtNDEyYy04ZjIzLTg2NGI3ODdjMzNlYyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=b2590408-d0a8-4df9-960b-3827731db796&link=16b77d94-e9dd-412c-8f23-864b787c33ec&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "hizmet-prim-tanimlama_29982775_22805123.html"
source_version: "2022-10-31T09:04:26.703+03:00"
source_bytes: 28392
fetched_at: "2026-09-13T04:07:49+00:00"
generator: "netsis-scraper 1.0.0"
---
# Hizmet Prim Tanımlama

Hizmet Prim Tanımlama, Finans Bölümü'nde Kayıt/Cari menüsünün altında yer alır. Hizmet Prim Tanımlama, hizmet prim sözleşmelerinin tanımlandığı bölümdür. Prim Tanım Bilgileri ve Kota Girişi olmak üzere iki sekmeden oluşur.

**Prim Tanım Bilgileri**

Prim Tanım Bilgileri sekmesi alanları ve içerdiği bilgiler aşağıdaki şekildedir:

| Hizmet Prim Tanımlama Ekranı |  |
| --- | --- |
| Hizmet Prim Kodu | Program içinde tanımlanan prim sözleşmeleri, hizmet prim kodları üzerinden takip edilir. Kullanıcı tarafından girilen tekrarlanmayan koddur. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, hizmet prim kodları arasından seçim yapılabilir. |
| Açıklama | Hizmet prim kodlarına ait açıklama bilgisinin girildiği alandır. |
| Grup Kodu | Prim hizmet sözleşmelerini kendi içinde gruplamayı sağlayan alandır. Raporlama amaçlı kullanılır. Alanın sağ tarafında bulunan aşağı ok butonu yardımı ile, kodlar arasından seçim yapılabilir. |
| Cari Seçimi |  |
| Cari Kısıt Tipi | Tanımlanan sözleşmeye hangi carilerin dahil olduğunu belirtmek için Cari Kodu, Grup Kodu, Kod 1/2/3/4/5 ve SQL desteği kısıdının verildiği alandır. |
| Cari Kısıt | Tanımlanan sözleşmeye cari kısıdının verildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, cariler arasından seçim yapılabilir. |
| Prim Bilgileri Girişi |  |
| Tip | Alış seçeneği seçilmişse alış faturalarının, satış seçeneği seçilmişse satış faturalarının dikkate alınarak prim hesaplamalarının yapılmasını sağlayan alandır. |
| Dövizli İşlem Yapılsın | Dövizli hizmet prim tanımının yapılması ve döviz değerleri üzerinden hizmet prim faturası oluşturulması için kullanılan seçenektir. |
| Döviz Tipi | "Dövizli İşlem Yapılsın" seçeneğinin işaretlenmesi ile aktif hale gelir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, döviz tipleri arasından seçim yapılır. |
| Başlangıç/Bitiş Tarihi | Tanımlanan sözleşmenin hangi tarihler arasında geçerli olacağı ve primin hangi tarihler arasında hesaplanacağının belirlendiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile, takvim yardımı alarak tarih girilebilir. |
| Prim Değerlendirme Sayısı | Girilen tarih aralığında kaç kere prim hesaplaması yapılacağını belirleyen alandır. **Örneğin:** 01/01/2010-31/12/2010 tarih aralığı için prim değerlendirme sayısı 12 ise, bir yıl boyunca 12 kez prim hesaplaması yapılacağı anlamına gelir. Bu durum, aylık dönemlerde prim hesaplaması yapılacağını gösterir. (Ocak, Şubat, Mart .... Aralık) 01/01/2010-31/12/2010 tarih aralığı için prim değerlendirme sayısı 4 ise, bir yıl boyunca 4 kez prim hesaplaması yapılacağı anlamına gelir. Bu durum, üç aylık dönemlerde prim hesaplaması yapılacağını gösterir. (Ocak-Mart, Nisan-Haziran, Temmuz-Eylül, Ekim-Aralık) |
| Matrah Türü | Girilen primin hangi tutar üzerinden hesaplanacağının belirlendiği alandır. Üç çeşit matrah vardır; Net Ciro, Brüt Ciro ve İskonto Ciro. **Net Ciro:** İskonto tutarı düşülmüş ve KDV tutarı eklenmemiş tutardır. Faturadaki ara toplamı ifade eder. **Brüt Ciro:** İskonto tutarı düşülmemiş ve KDV tutarı eklenmemiş tutardır. Faturada brüt toplamı ifare eder. **İskonto Ciro:** Brüt tutar üzerinden hangi kademeye kadar olan iskonto tutarlarının düşüleceği belirlenir. **Örneğin:** 6 adet satır iskontosu varken, iskonto kademesi 2 seçildiğinde, prim hesaplamasının kademeli olarak 2 satır iskonto tutarı düşülerek yapılacağı anlamına gelir. |
| İskonto Kademe | İskonto kademesinin girildiği alandır. İskonto ciro seçeneğinin seçilmesi ile aktif hale gelir. Alanın sağ tarafında yer alan aşağı ok butonu ile iskonto kademeleri arasından seçim yapılır. |
| Prim Belge Stok Kodu | Prim hesaplaması için kullanılan ürün kodudur. İstenilen ürün kodu girilir. Prim hesaplama işlemi sonunda sipariş ya da fatura belgesi oluşturulurken, bu alanda girilen stok kodu kullanılır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, stok kodları arasından seçim yapılır. |
| Prim Belgeleri İçin Kısıt Uygulaması Olacak Mı? | Birbirini kapsayan diğer bir deyişle tarih aralıkları çakışan sözleşmelerde, parametrenin işaretlenmediği durumda, aynı tarihler için birden fazla prim hesaplaması söz konusu haline gelir. **Örneğin:** 07/08/2010-07/09/2010 tarihleri arasında yapılan P1 kodlu sözleşme doğrultusunda, kota girişinde X stoku için, 0-990 adet arası 50 TL prim, 991-2000 adet arası 60 TL prim 07/08/2010-07/09/2010 tarihleri arasında yapılan P2 kodlu sözleşme doğrultusunda, kota girişinde X stoku için, 0-50 adet arası 20 TL prim, 51-100 adet arası 30 TL prim tanımlamaları yapıldığı varsayıldığında, öncelikle P2 kodlu prim sözleşmesi için prim değerlemesi yapılır. Ardından P2’yi kapsayan daha geniş tarih aralığında geçerli olan P1 kodlu sözleşme için prim değerlemesi yapılır. P2 için değerleme yapıldıktan sonra P1 kodlu sözleşme için prim değerlemesi yapıldığında prim değerlenecek kayıt ekrana gelmez. Bu durum aynı belgelerin P2 kodlu sözleşme için değerlemeye dahil edilmesinden kaynaklanır. Dolayısı ile “Hariç Tutulacak Prim Belge Listesinde" P2 hizmet prim koduna göre oluşan belge ve bilgileri ekrana gelir. |

**Kota Girişi**

Kota Girişi sekmesi alanları ve içerdiği bilgiler aşağıdaki şekildedir:

| Hizmet Prim Tanımlama Ekranı | Hizmet Primine Esas Stok Seçimi |
| --- | --- |
| Kısıt Tipi | Hangi ürünlere istinaden prim hesaplaması yapılacağının belirlendiği alandır. Ürün kodlarına ve belirli rapor kodlarına göre, SQL desteği yardımıyla veya hepsine göre kısıtlama verilebilir. Hepsi seçeneği seçildiğinde, ürün kısıtlaması yapılmadan tüm ürünlerin alım yada satımlarında prim hesaplanacağı anlamına gelir. Aynı sözleşme altında birden fazla ürün kısıtına göre tanımlamalar yapılmışsa, prim hesaplama işleminde bir stokun birden fazla ürün kısıtına uyması durumunda, prim hesaplamadaki öncelik sırası kısıt tipi alanında belirtilen şekildedir (Stok kodu, Cari/S kodu, Üretici kodu, Grup kodu, Kod1/2/3/4/5, SQL ve hepsi sırasındadır). |
| Kod | "Kısıt Tipi" alanında belirlenen kısıta göre kod seçiminin yapıldığı alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, kodlar arasından seçim yapılır. |
| Kota Özellikleri |  |
| Kota Tipi | Prim hesaplamasının satılan/alınan ürünlerin ciroları üzerinden mi yoksa miktarları üzerinden mi hesaplanacağının belirlendiği alandır. **Ciro** seçilmesi durumunda, "Prim Tanım Bilgileri" sekmesindeki "Matrah Türü" alanında belirlenen ciro tipine göre hesaplama yapılır. |
| Kota Yok | Prim hesaplamasında herhangi bir miktar ya da tutar bazında kota konulmayacaksa işaretlenen seçenektir. |
| Ölçü Birim | Prim hesaplama işleminde, satılan ya da alınan ürünlerin miktarları, burada seçilen ölçü birimi dikkate alınarak getirilir. Alanın sağ tarafında yer alan aşağı ok butonu ile ölçü birimleri arasından seçim yapılır. |
| Hak Ediş Özellikleri | Kota Girişi bölümünde, ilgili kota aralıkları için girilen değer bilgilerinin oran olarak mı yoksa tutar olarak mı yorumlanacağının belirlendiği alandır. **Örneğin:** Oran seçilmesi durumunda; prim hesaplama işleminde satılan ya da alınan ürünlerin toplam cirosu, ilgili kota aralığındaki değer bilgisinin 100’e oranı ile çarpılarak hesaplanır. |
| Hak Ediş Adet Bazında | Bu seçeneğin işaretlenmesi durumunda her adet ürün için prim hesaplaması söz konusudur. Hak ediş olarak "Tutar" seçildiğinde anlamlıdır. Bu durumda ilgili kota aralığındaki değer bilgisi ile satılan ya da alınan ürünün toplam miktarı çarpılarak prim hesaplanır. |
| Kademeli | Prim hesaplamasının kademeli yapılması için kullanılan seçenektir. |
| Kota Girişi |  |
| Alt Sınır | Kota ve hak ediş tanımlamalarına göre alt sınırın tanımlandığı alandır. "Kota Yok" seçeneği işaretlendiğinde, program tarafından pasif hale getirilir. Kota olmadığı için değerin ne olduğunun da önemi yoktur. |
| Üst Sınır | Kota ve hak ediş tanımlamalarına göre üst sınırın tanımlandığı alandır. "Kota Yok" seçeneği işaretlendiğinde, program tarafından pasif hale getirilir. Kota olmadığı için değerin ne olduğunun da önemi yoktur. |
| Değer | Kota ve hak ediş tanımlamalarına göre üst sınırın tanımlandığı alandır. |
| Sabit Bedel Kavramı | Hizmet primine esas stok seçiminde **"Hepsi"**, kota özelliklerinde **"Kota Yok"** ve hak ediş özelliği olarak "Tutar" seçilmesi ile ekrana gelen alandır. Prim Sözleşmesinin tanımlı tarihleri arasında alım ya da satım olmasa bile, prim değerlendirme ekranına ilgili kayıt gelir ve hak ediş özelliklerinde belirlenen tutar kadar prim tutarı elde edilip prim belgesi oluşturulur. |
| Grup Hesaplaması Sıfırlansın | Grup hesaplamasının sıfırlanması için kullanılan seçenektir. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır. Yapılan kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
