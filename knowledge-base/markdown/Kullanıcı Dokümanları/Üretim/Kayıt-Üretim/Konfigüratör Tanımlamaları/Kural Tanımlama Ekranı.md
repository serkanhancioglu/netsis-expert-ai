---
title: "Kural Tanımlama Ekranı"
page_id: "50663117"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Üretim"
  - "Kayıt/Üretim"
  - "Konfigüratör Tanımlamaları"
  - "Kural Tanımlama Ekranı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Üretim / Kayıt/Üretim / Konfigüratör Tanımlamaları / Kural Tanımlama Ekranı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWMzM2Q1NjliLTJmY2UtNDFjMy1hMDRkLTExYTFkNTdmOTA1MyZsaW5rPTRjZDhiYjBjLTk1MjctNGYwOC05NGY2LWRmMmZiY2Q5ZjYxZiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=c33d569b-2fce-41c3-a04d-11a1d57f9053&link=4cd8bb0c-9527-4f08-94f6-df2fbcd9f61f&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "kural-tanimlama-ekrani_50663119_50663117.html"
source_version: "2022-10-13T11:54:49.710+03:00"
source_bytes: 19988
fetched_at: "2026-09-13T04:18:49+00:00"
generator: "netsis-scraper 1.0.0"
---
# Kural Tanımlama Ekranı

Kural Tanımlama Ekranı, Üretim modülünde Kayıt/Üretim menüsünün altında yer alır. Bir ürüne ait konfigürasyonda değişiklik yapılacağı zaman bu değişiklik ürün ağacını da etkiler. Bir mamulün ürün ağacında değişim yönetiminin kapsamında olacak ve ne tür değişiklikler yapılacağı veya yapılamayacağı kurallarla tarif edilmesi istenen her bileşenin, öncelikle bir ikame malzeme grubu ile ifade edildiği varsayımı yapılır. Böylece, kullanıcı ürün konfigüre ederken sadece önceden belirlenen kurallar çerçevesinde değişiklik yapacağı için ürün konfigürasyonu kontrol altında tutulmuş olur. Kural Tanımlama ekranı, bu tür konfigürasyon kontrol kurallarının tanımlanmasını sağlar. Kural tanımı ürün grupları ve ikame malzeme grupları bazında yapılır. Ekranın üst kısmında kuralların uygulanacağı ürünler ve bileşenleri -ikame malzeme grubu veya stok kodu bazında- seçilir, kural listesinden ilgili kayıt seçilerek eşleştirilir.

Kurallar ve İstisnalar olmak üzere iki sekmeden oluşur.

**Kurallar**

Kural Tanımlama Ekranı Kural sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Kural Tanımlama Ekranı |  |
| --- | --- |
| Kural Kodu | Tanımlaması yapılacak kural kodunun girildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile seçim yapılır. **Ürün Ağacını Değiştirmez:** Tarif edilen ikame malzeme grubu veya stokla ilgili bir değişiklik yapıldığında ilgili kaydın ürün ağacının değişmemesi için kullanılan seçenektir. Bu bileşen ürün ağacında değiştirilse bile nihai ürünün stok kodu aynı kalır. **Kullanıcı Değiştirme Yapılabilir:** Ürün ağacında belirtilen ikame malzeme grupları veya stokların kullanıcı tarafından değiştirilmesini sağlayan seçenektir. Ürün ağacı onaylama yetkisi olmayan kullanıcılar için geçerlidir. **Kullanıcı Ekleme Yapılabilir:** Ürün ağacına belirtilen ikame malzeme grupları veya stokların kullanıcı tarafından eklenmesini sağlayan seçenektir. Ürün ağacı onaylama yetkisi olmayan kullanıcılar için<br>geçerlidir. **Kullanıcı Silme Yapılabilir:** Ürün ağacından belirtilen ikame malzeme grupları veya stokların kullanıcı tarafından silinmesini sağlayan seçenektir. Ürün ağacı onaylama yetkisi olmayan kullanıcılar için<br>geçerlidir. **Birliktelik Kuralı:** Ürün ağacı üzerinde yapılan konfigürasyonlarda hangi özellik ve değerin hangileriyle kullanılacağını veya kullanılmayacağını belirleyen seçenektir. Öncelikle bir “Birliktelik Kuralı” tanımlanır, ardından aynı ekranda “Birliktelik Setleri” sekmesi aktif hale gelir. Birliktelik kuralına bağlı birliktelik setleri tanımlandıktan sonra, “Birliktelik Kalemleri” sekmesi aktif hale gelir ve asıl burada hangi özellik ve değerlerin birbirleriyle kullanılacağı veya kullanılmayacağı belirlenir. Birliktelik kuralı tanımlamasında ürün seçimi bölümünde tüm ürünler haricinde daha spesifik bir tanımlama yapıldıysa yukarıda “Kural Kopyala” bölümü aktif hale gelir. Buradaki kural kopyalama işlemi, önceden tanımlanan bir birliktelik kuralını diğer stok kodları veya ürün grupları için kopyalamayı sağlar. |
| Kural Adı | Tanımlanacak kural adının girildiği alandır. |
| Ürün Seçimi | Tanımlanacak kural için ürün seçiminin yapıldığı alandır. Ürün Kodu, Ürün Grubu ve Tüm Ürünler arasından seçim yapılır. |
| Ürün Değer | Ürün Kodu veya Ürün Grubu seçeneğinin seçilmesi ile aktif hale gelen alandır. Ürün değeri için stok kodunun seçilmesini sağlar. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, stok kodları arasından seçim yapılır. |
| Asorti Kodu | Ürün Değer alanında girilen stok koduna ait asorti kodunun girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, tanımlanan özellik kodlarına ulaşılır. |
| Asorti Kodu Açıklaması | Asorti koduna ait açıklama bilgisinin otomatik olarak ekrana getirildiği alandır. |
| Bileşen Tipi | Tanımlanacak kural için bileşen tipi seçilen alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile bileşen tipleri arasından seçim yapılır. |
| Tümü | Tüm bileşenler için kural tanımlama yapılmasını sağlayan seçenektir. |
| Bileşen Değer | Bileşen Tipi alanında seçilen tipe göre bileşen değerinin girildiği alandır. Bileşen değeri için stok kodunun seçilmesini sağlar. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, stok kodları arasından seçim yapılır. |
| Asorti Kodu | Bileşen Değer alanında girilen stok koduna ait asorti kodunun girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, tanımlanan özellik kodlarına ulaşılır. |
| Asorti Kodu Açıklaması | Asorti koduna ait açıklama bilgisinin otomatik olarak ekrana getirildiği alandır. |

Kurallar bir kere tanımlandıktan sonra bu kurala özel istisnai - kuralın uygulanmamasının gereken - durumlar da tanımlanabilir. Grid üzerinden kural fare ile çift tıklanarak seçildikten sonra "İstisna" sekmesi ekrana gelir.

**İstisnalar**

Kural Tanımlama Ekranı İstisnalar sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Kural Tanımlama Ekranı |  |
| --- | --- |
| Ürün Kodu | "Kurallar" sekmesinde tanımlanan ürünün izlendiği alandır. |
| Stok Kodu | "Kurallar" sekmesinde tanımlanan stokun izlendiği alandır. |
| Ürün Seçimi/Bileşen Seçimi Alanları | Ürün ve bileşen grubu bazında kurala dahil edilmemesi istenen kayıtların tanımlanması sağlayan alanlardır. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır.

Kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
