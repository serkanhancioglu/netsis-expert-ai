---
title: "Ürün Konfigüratörü – Yapılandırma Kodu Desteği"
page_id: "50669071"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Ürün Konfigüratörü – Yapılandırma Kodu Desteği"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Ürün Konfigüratörü – Yapılandırma Kodu Desteği"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWFmZWU2YmE1LWQzOGQtNDRjYS04MDM2LTIzNTUxNGRiMTZiMSZsaW5rPWNiNWVmYzVlLWI0ZTktNDQ3OC05MDNlLWY4Y2JjZGUxZjFlZCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=afee6ba5-d38d-44ca-8036-235514db16b1&link=cb5efc5e-b4e9-4478-903e-f8cbcde1f1ed&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "urun-konfiguratoru-yapilandirma-kodu-destegi_50669078_50669071.html"
source_version: "2022-11-03T09:06:06.587+03:00"
source_bytes: 668977
fetched_at: "2026-09-13T04:25:37+00:00"
generator: "netsis-scraper 1.0.0"
---
# Ürün Konfigüratörü – Yapılandırma Kodu Desteği

Ürün Konfigüratörü-Yapılandırma Kodu Desteği ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Ürün konfigüratörü "Esnek Yapılandırma Kodu" desteği sayesinde, ürün konfigürasyonu sırasında, yapılandırmalı stok kodlarının kullanılmasını ve bu stok kodlarına ait reçete düzenlemelerinin yapılmasını sağlar.

Ürün Konfigüratörü Yapılandırma Kodu ile yapılabilecekler aşağıdaki şekildedir:

- Daha önce yapılandırma kodu kapsamında tanımlanan özellik ve özellik değerleri, otomatik olarak ürün konfigüratöründe özellik kodu olarak kullanılabilir. Böylece, ürün konfigüratörünün özellik-değer filtresi kısmında "Esnek Yapılandırma" özellikleri kullanılabilir. Bir stokun farklı yapılandırma kodlarına sahip yönleri, aynı ikame malzeme grubuna dahil ve birbirlerinin alternatifi gibi davranır.
- Ürün konfigüratöründe yeni bir stok kodunun tanımlanması sırasında bu stok kodu için yapılandırma kodu türetme özelliği mümkündür.
- Esnek yapılandırma ve özellikleri, ürün konfigüratöründeki birliktelik kontrolü için de desteklenir. Böylece, birliktelik kontrolü kuralları tanımlanırken esnek yapılandırma kapsamında tanımlanan özellik ve özellik değerleri kullanılabilir. Esnek yapılandırma özelliği aktif ise, Kural Tanımlama ve Ürün Grubu Oluşturma ekranlarında yapılan tanımlamalar yapılandırma kodu detayında olabilir.

#### Yeni Malzeme Ekleme Aşaması Kullanım Durumu

![](../_assets/e4ccc2b7b8c830a44e71.png)

Esnek yapılandırmalı baz mamul reçetesi açıldıktan sonra, yine yapılandırılmış bileşen seçildiğinde, "Mamul Seçimi" sekmesinde bulunan diğer yapılandırma kodları (Alternatifleri) görünür. Seçilmesi istenen özellikteki bileşen bu alternatifler arasında yoksa, "Yeni Malzeme Ekle" butonu ile yeni malzemenin tanımlaması yapılır. Burada yeni "Yapılandırma Kodu" program tarafından otomatik olarak oluşturulur. Bu yapılandırma kodu bileşen stok için için henüz var olmayan bir yapılandırma kodudur. Özelllik değer gridine bu bileşen için istenen özellik değeri yazılır.

![](../_assets/9d1fbc8bb4fd1679faf4.png)

![](../_assets/396771c0965f0be60a7b.png)

Bu aşamadan sonra oluşan yeni mamul ile ilgili tanımlamaların yapılması ve reçetenin onaylanması ile; bileşen için otomatik oluşturulan Yapılandırma Kodunda, yeni tanımlanan özellik değerinde ve Stok modülündeki esnek yapılandırma tanımlamalarında da gerekli eşleşmeler gerçekleşir.

![](../_assets/a4deb5bcfaea9ef7692c.png)

Bileşenlerden biri, mevcut alternatiflerden biri ile değiştirildiğinde, oluşan yeni konfigürasyon mevcut bir ürün reçetesine karşılık gelmiyor - reçete kontrol ile bir baz mamul bulunamıyor - ise Mamul Kodu YENI olur.![](../_assets/6222c795fc344166c7ca.png)

Yeni mamul için Yeni Mamul Tanımlama sekmesinde gerekli tanımlamalar yapılır. Bu reçete, mevcut stok ve mevcut yapılandırma kodu için tanımlanacaksa "Yeni Stok Kodu" alanına mevcut yapılandırılabilir bir ürün kodu girildikten sonra "Yeni Yapılandırma Kodu" alanı için mevcut yapılandırma kodlarından birinin yazılması gerekir. Bunlar için alanın sağ tarafında yer alan rehber butonundan yararlanılabilir.![](../_assets/b1e38fa3ee63399e5891.png)

Mevcut bir yapılandırma kodu seçildiğinden dolayı bu konfigürasyon onaylandığında, başka herhangi bir tanımlama yapmaya gerek kalmadan anlamlı bir reçete tanımlanır. Seçilen yapılandırma kodu için daha önceden reçete tanımlaması yapılmışsa, onaylama sonrası oluşturulan yeni konfigürasyonla ilgili reçete değiştirilir.
Yeni bir konfigürasyon oluşturarak veya mevcut bir baz mamulü konfigüre ederek yeni bir mamul reçetesi oluşturulup, "Yeni Mamul Tanımlama" sekmesinden mamul bilgileri girilip, "Yeni Stok Kodu" olarak mevcut bir mamul seçilirse, yeni bir yapılandırma kodunun türetilmesi sağlanır.
Reçete onaylandığında, yeni oluşturulan fakat özellik ve değer bilgileri tanımlanmamış yapılandırma kodu için reçete tanımlanır. Bu yapılandırma kodunun anlam kazanması için, Stok-"Esnek Yapılandırma Tanımlamaları" bölümünden, ilgili yapılandırma kodunun özellik ve değer bilgilerinin tanımlanması gerekir.
