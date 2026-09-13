---
title: "Asorti Uygulaması"
page_id: "50677835"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Asorti Uygulaması"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Asorti Uygulaması"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWM4ODk5YzcxLTI2Y2MtNDE0Zi1hNjkzLTRhN2VkZjE0ZjQwMyZsaW5rPWFiMDI5NDJkLTFhZTEtNDg1OS1hYjc1LWEwMTlmNTZhYjM3ZSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=c8899c71-26cc-414f-a693-4a7edf14f403&link=ab02942d-1ae1-4859-ab75-a019f56ab37e&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "asorti-uygulamasi_50677861_50677835.html"
source_version: "2022-11-03T09:11:23.137+03:00"
source_bytes: 1851479
fetched_at: "2026-09-13T04:25:45+00:00"
generator: "netsis-scraper 1.0.0"
---
# Asorti Uygulaması

Asorti Uygulaması ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Asorti uygulaması, "Esnek Yapılandırma" uygulamasına ek olarak getirilmiş bir özelliktir. Esnek yapılandırma uygulamasıyla, stokların sahip oldukları özellikler bazında tek bir stok kartı üzerinden takibi sağlanır. Asorti uygulamasında ise, stokların sahip olduğu özellikler arasında, bir özelliğin sabit tutularak, diğer özeliklerin farklı değerleri için gruplama yapılması ile asorti grupları elde edilmesi ve tanımlanan asorti gruplarının, belgelerde seçilerek hızlıca girilmesi sağlanmıştır. Asorti grubu belgede seçildiğinde, asorti grubunda yer alan farklı özelliklere sahip stoklar ve miktarları otomatik olarak belgeye eklenmiş olur.

**Asorti Parametreleri**

Asorti Parametreleri'nde izlenmesi gereken adımlar aşağıdaki şekildedir:

![](../_assets/0c3eb8469bc7517b9c0a.png)

- Stok parametreleri ekranında "Esnek Yapılandırma" parametresi işaretlenmiş, tüm özellik ve değerleri esnek yapılandırma ekranlarından tanımlanmış olmalıdır.
- Yardımcı Programlar-Özel Parametre Tanımlamaları ekranında "ESNEKYAP", "ASORTI" özel parametresi tanımlanmış olmalıdır.
- Belgedeki stok kalemleri için asorti kodunun saklanacağı alanın fatura parametrelerinden seçimi yapılmış olmalıdır.

**Asorti Tanımlamaları**

Asorti Tanımlamaları, Stok Modülü-Esnek Yapılandırma-Asorti Tanımlamaları ekranından yapılır.

![](../_assets/1b2fc0c1a66998ef5a7a.png)

Asorti Tanımlama ekranı "Asorti Tanım" ve "Stok-Asorti Eşleme" sekmelerinden oluşur.

Asorti Tanım ekranındaki alanlar aşağıdaki gibidir:

**Asorti Kodu:** Kullanıcı tarafından belirlenen ve programda belge girişinde kullanılacak olan Asorti grup kodlarının girileceği alandır.

**Açıklama:** Asorti grubuna ait açıklama bilgisinin girildiği alandır.

**Ana Özellik (Satır):** Sabit tutulan özelliğin, özellik kodunun girildiği alandır. Örnekte, stokun Renk özelliği (Siyah renk) sabit tutulan özelliktir.

**Ana Değer (Satır):** Sabit tutulan özellik değerinin girildiği alandır. Bu alan boş geçildiğinde, sabit tutulan özelliğin tüm değerlerinin "Miktar Bilgileri" alanına getirileceği anlamına gelir. Örnekte Renk özelliğinin, Siyah değeri seçilmiştir. Değer seçilmediği durumda tüm renkler matris ekrana gelir.

**Asorti Özellik (Sütun):** Sabit tutulan özelliğe göre, değişken olan özellik kodunun girildiği alandır.

Örnekte, stokun Numara özelliği değişen özelliktir.

![](../_assets/a60e5f7735305875c749.png) Matrise girilen değişken özellik bazında miktar bilgilerini saklar.
![](../_assets/f698c2ad73655308acdb.png)

Örnekte Ayakkabı stokunun renk özelliği (Siyah renk) sabit tutulmuş, numara özelliği değişkenlik göstermiştir. Siyah Renk için, numara özelliğine göre miktar ataması yapılmıştır.
Stok-Asorti Eşleme ekranında, esnek yapılandırılabilir stoklar için asorti grup eşleştirmesi yapılır.

![](../_assets/44014d213c47c8457c27.png)

Asorti grup-stok eşleştirmesi girildikten sonra kaydet butonu ile kaydedilir. Bir stok için birden fazla asorti grubu tanımlaması yapılmışsa, belgede varsayılan olarak gelecek asorti grubu için, varsayılan kolonu işaretlenir.

**Hızlı Asorti Atama:** Asorti gruplarının verilen kısıtlara göre ürün gruplarına atanmasını sağlar. Butona basıldığında Asorti Kodu Toplu Atama ekranı açılır, verilen ürün kısıtlamasına göre atanacak asorti kodu alanında girilen asorti kodu kısıtlara uyan ürünlere atanır.

![](../_assets/0ae228f6d2d39f5b8441.png)

**Fatura Modülünde Asorti**
Fatura modülünde girilen belgede, kalem bilgileri sekmesinde stok kodu girildikten sonra asorti kodu alanına Asorti Tanımlama ekranında varsayılan olarak atanan asorti kodu gelir. Kullanıcı isterse asorti kodu rehberinden ilgili stok için tanımlanmış diğer asorti grup kodlarından seçim yapabilir.

![](../_assets/73a452152329fec0ae12.png)

Yapılandırma Kodları ![](../_assets/4ff5f4c2e070ff904bfa.png) butonu ile, belgede asorti grup kodlarının seçimi yerine, yapılandırma kodlarının seçilmesi sağlanır.
Arama ![](../_assets/08430e457c827d527645.png) butonu ile, asorti grup kodlarına geçilerek, asorti grup kodlarının seçimi sağlanır.

Asorti Kodu alanının çıkışında Asortili Ürün Girişi ekranı açılır. Bu ekranda kalemlerde girilen stokun asorti grubuna ait yapılandırma özellikleri bazında miktarları ve toplam miktarı gösterilir.

![](../_assets/43c82de8f64931d3c155.png)

Set miktarı arttırıldığında, değer miktarları set miktarı ile çarpılır. Örneğin set miktarını 2 yaparak tanımlı tüm miktarların 2 katı olarak belgeye yansıması sağlanabildiği gibi buradaki miktarlara elle müdahale edilip yine belgeye bu düzenleme ile yansıması sağlanabilir.

![](../_assets/e927b85144e57553d87e.png)

Asorti grubu seçilip set miktarı ayarlandıktan sonra miktar alanı 0 olarak geçilebilir. Ürüne ait asorti grubunda yer alan tüm özellikler ve miktarları otomatik olarak gride atılır.
"Kalem görünümünü değiştir'e" basıldığında asorti grubunda yer alan ürünleri yapılandırma özellikleri bazında detaylı ve kırılımlı olarak gösterir.

![](../_assets/e972ab78c35b89a8b7df.png)
Esnek yapılandırma ile aynı fatura 5 satır kalem girişi ile sağlanabilirken, asorti uygulamasında tek satırda aynı özelliğin farklı değerleri için tek seferde sağlanır.

"Asorti Bakiye Raporu" ile asorti grubunda bulunan ürünlerin, yapılandırma özellikleri bazında bakiyeleri ve asorti grubunda yer alan yapılandırma kodlarına ait tüketilen miktar bilgileri raporlanabilir.
