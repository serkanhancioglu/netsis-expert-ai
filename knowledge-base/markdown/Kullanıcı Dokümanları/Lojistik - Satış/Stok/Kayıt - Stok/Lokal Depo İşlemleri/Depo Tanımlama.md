---
title: "Depo Tanımlama"
page_id: ""
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Stok"
  - "Kayıt / Stok"
  - "Lokal Depo İşlemleri"
  - "Depo Tanımlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Stok / Kayıt / Stok / Lokal Depo İşlemleri / Depo Tanımlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTc4NzhkMDg3LTE0MzAtNDk3NC05YzA1LWY0MGFlMTIzODM2ZiZsaW5rPTc5ZDRjOTUxLTUwNWYtNDBlZC1iNzY0LWRmMTc4YmIyYmIzNyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=7878d087-1430-4974-9c05-f40ae123836f&link=79d4c951-505f-40ed-b764-df178bb2bb37&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "depo-tanimlama.html"
source_version: ""
source_bytes: 13645
fetched_at: "2026-09-13T04:04:13+00:00"
generator: "netsis-scraper 1.0.0"
---
# Depo Tanımlama

Depo Tanımlama, Lojistik - Satış Bölümü'nde, "Kayıt/Stok" menüsünün altında yer alır. Birden fazla depo mantığıyla çalışan firmalar için, lokal depo tanımlamalarının yapıldığı bölümdür.

Depo Tanımlama ekranından tanımlanan lokal depoların program genelinde kullanılması için, Stok → Kayıt → [Stok Parametreleri](<../Stok Parametreleri.md>) → “Lokal Depo Uygulaması” parametresinin işaretlenmesi gerekir.

Firmalar, genel depolarını bölümlere ayırarak ayrı Giriş/Çıkış işlemleri yapmak, stok bakiyelerini ayrı ayrı takip etmek ya da listelerini ayrı ayrı oluşturmak ister. Kullanıcılar, lokal depo kodlarını firma ve sektör özelliklerine göre istedikleri gibi belirleyebilir.

**Lokal depo kullanımı sanayi sektöründe;** Raf sistemine göre ayrı depo tanımlama ve farklı ambarları olan firmalar için ambarlara göre stok takibi yapmayı olanaklı hale getirir. Lokal depo tanımlamaları, depo mantığında kullanılmasının yanı sıra, sarf yerlerine (masraf merkezlerine) göre ayarlanarak giriş/çıkış ve stok takiplerinin yapılmasını da sağlar.

**Lokal depo kullanımı gıda sektöründe;** Raf, ambar ya da reyon sistemine göre lokal depo tanımlamaları yapılarak kullanılır.

Lokal depo sistemi, frenchise sistemi (satış noktaları) ile çalışan firmalar için satış noktalarını lokal depo olarak tanımlayıp, müşteri bazında (cari kodlarına göre) takip imkanı sağlar.

Lokal depo tanımlamaları şube tanımlamaları için engel oluşturmaz. Firmanın, lokal depolarının dışında diğer semtlerde de şubeleri varsa, bunları ayrı ayrı şube kodu tanımlaması ile oluşturarak her şubesinin stok giriş/çıkış işlemlerini ayrı şube bölümlerinde tutması ve stok bakiyelerini şubeler bazında listelemesi mümkün.

En fazla 32.767 adet lokal depo tanımlaması yapılır.

Depo Tanımlama ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Depo Tanımlama Ekranı |  |
| --- | --- |
| Depo Kodu | Sadece sayısal olarak kayıt girilen lokal deponun kodunun tanımlandığı alandır. Stok giriş ve çıkışları ile ilgili kayıtlarda (Örneğin satış faturası, üretim sonu kaydı vb.) sorgulanan depo kodu, bu alanda tanımlanan koddur. Rehber butonu ![](https://docs.logo.com.tr/download/thumbnails/22803727/se%C3%A7enek%20tu%C5%9Fu.jpg?version=1&modificationDate=1542196737167&api=v2) ile, depo kodlarına ulaşılır. |
| Depo İsmi | Tanımlanan lokal deponun isminin girildiği alandır. |
| Fiyat Tipi | İlgili lokal depodan yapılan giriş ve çıkışlarda baz alınacak fiyatın belirlendiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile, fiyat tipleri arasından seçim yapılır. |
| Cari Kodu | Lokal depo kodu ve ismi, kullanıcılar tarafından isteğe göre tanımlandıktan sonra satış noktaları mantığıyla (her müşterinin deposunu, lokal depo olarak tanımlayarak) takip etmek için kullanılan alandır. "Cari Hesap Kayıtları" bölümünde, müşteriler için tanımlanan cari kodun girilmesi gerekir. Satış noktaları mantığıyla çalışmayan firmaların cari kod girmesine gerek yoktur. |
| Referans Kodu | Fatura → Kayıt → [Alış Parametreleri](<../../../Fatura/Kayıt - Fatura/Alış Parametreleri.md>) → Genel 5 → "Sipariş/İrsaliye/Faturada Referans Kodu Sorulsun" parametresi işaretlenmişse, bu alana girilen "Referans Kodu", "Depo Kodu" seçildiği zaman Sipariş/İrsaliye/Faturada otomatik olarak ekrana gelir. Referans uygulaması ile ilgili detaylı bilgi için; Muhasebe → Kayıt → [Referans Kodu Kayıtları](<../../../../Muhasebe/Muhasebe Modülü/Kayıt - Muhasebe/Referans Kodu Kayıtları.md>) dokümanına bakılabilir. |
| Genel Kilit | Depo hareketlerinin işlemlere kapatılmasını sağlayan parametredir. İşaretlendiğinde (örneğin, sayım dönemlerinde vb.), depo hareketleri tüm modüllerden entegre ve elle (manuel) yapılan kayıtlara kapatılır. |
| Mal Çıkışlarında Eski Bakiye Göstersin | Tanımlaması yapılan deponun mal çıkışlarında eski bakiye gösterilmesi için kullanılan seçenektir. |
| Eksi Bakiye Kontrol | "Lokal Depo" kullanan firmalarda, lokal depo bazında ayrı ayrı eksi bakiye kontrolü için kullanılan seçenektir. Fatura → Kayıt → Alış/Satış Parametreleri → "Eksi Bakiye Kontrolü" ve "Eksi Bakiyede İşlem Durdurulsun" parametresi işaretlense bile, eksi bakiye kontrolü işaretlenmemiş bir lokal depodan, kontrol yapılmadan çıkış işlemleri yapılabilir. Fatura kayıtlarında eksi bakiye takibi ile ilgili detaylı bilgi için; Fatura → Kayıt → [Satış Parametreleri](<../../../Fatura/Kayıt - Fatura/Satış Parametreleri.md>) dokümanına bakılabilir. |
| Antrepo Depo | Tanımlanacak deponun antrepo depo olması halinde işaretlenmesi gereken seçenektir. |
| Lokasyon Takibi Yapılsın Mı? | "Dinamik Depo Uygulaması" kullanıldığı zaman işaretlenmesi gereken bir seçenektir. "Dinamik Depo Uygulamasının" kullanılması için mutlaka "Lokal Depo Uygulamasının" kullanılması gerekir. Bu durum, dinamik depo takibinin yapılacağı durumlarda, ambarların lokal depo olarak tanımlanma zorunluluğu olmasından kaynaklanır. Dinamik depoda kullanılacak olan lokal depo kodları açılırken, ekranda yer alan “Lokasyon Takibi Yapılsın Mı” parametresinin mutlaka işaretlenmesi gerekir. Dinamik Depo uygulaması ile ilgili detaylı bilgi için; Lojistik - Satış → [Dinamik Depo](<../../../Dinamik Depo/index.md>) dokümanına bakılabilir. |
| Ortak Bakiye Kodu | Stok hareketlerini "Lokal Depo" bazında takip eden firmaların kullandığı alandır. "Lokal Depo Uygulaması" kullanıldığında, Fatura Modülündeki çıkışlarda, lokal deponun bakiyesine bakılarak eksi bakiye kontrolü yapılır. Bu uygulama ile stokun hareket gördüğü birden fazla deponun bakiyesi kümüle edilerek, toplam değer üzerinden bakiye kontrolü gerçekleştirilir. Bunun için, bakiyesi kümüle edilecek depoların "Ortak Bakiye Kodu" alanına aynı değerin yazılması gerekir. **Örneğin:** 001 kodlu stokun hareket gördüğü lokal depolar ve bu depolardaki bakiyelerin aşağıdaki gibi olduğu varsayıldığında: ```text<br>Depo Kodu Bakiye Ortak Bakiye Kodu<br>``` ```text<br>1 100 01<br>``` ```text<br>2 50 01<br>``` ```text<br>3 50 --<br>``` Lokal depo bazında stok bakiyeleri bu şekilde iken, satış faturası ile 1 numaralı depodan 130 adet çıkış yapıldığında, 1 ve 2 numaralı depoların bakiyeleri kümüle edilir ve buna göre eksi bakiye kontrolü yapılır. Yani stokun 1 numaralı depodaki bakiyesinin 150 olduğu varsayılır. 3 numaralı lokal deponun "Ortak Depo Kodu" alanına diğer depolar için tanımlanan kod yazılmadığı için, bu deponun bakiyesi herhangi bir kümülasyona dahil edilmez. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<Tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır. Yapılan kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](https://docs.logo.com.tr/download/thumbnails/22803727/kay%C4%B1t%20sil%203.png?version=1&modificationDate=1582272377397&api=v2) butonuna tıklanması gerekir.
