---
title: "Ek-1 (Puan Uygulaması)"
page_id: "29993143"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Stok"
  - "Ekler (Stok)"
  - "Ek-1 (Puan Uygulaması)"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Stok / Ekler (Stok) / Ek-1 (Puan Uygulaması)"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTYzOTU0NDNiLTcxMjQtNDhiOC1hNjU4LWE2OWI2YjExNjU5ZiZsaW5rPTM4YzNhMDM4LTA3YTktNGI3Zi1iM2VhLTlkNDhmM2Q2ZWZhYSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=6395443b-7124-48b8-a658-a69b6b11659f&link=38c3a038-07a9-4b7f-b3ea-9d48f3d6efaa&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ek-1-puan-uygulamasi_30000565_29993143.html"
source_version: "2022-11-22T11:33:46.737+03:00"
source_bytes: 364030
fetched_at: "2026-09-13T04:05:26+00:00"
generator: "netsis-scraper 1.0.0"
---
# Ek-1 (Puan Uygulaması)

Puan Uygulaması ile ilgili detaylı bilgiye bu dokümandan ulaşılır.

Puan uygulaması, birçok sektörde yaygın olarak uygulanan puanlama kampanyalarının program tarafından otomatik takibine yönelik sistemdir.

Program, firmaların müşterilere alımları üzerinden puan hesaplaması ve puanlarına istinaden hediye vermesi gibi işlemlerin takibini yapar. Böyle bir sistemde, her bir ürün için ayrı puan belirlenir ve müşterilerin toplamda hak ettiği, kullandığı ve kalan puanlarının takibi yapılır. Toplanan puanların karşılığında verilecek hediye ürünler için bakiye puan dikkate alınır.

**Stok Kartı Kayıtlarında Yapılması Gerekenler**

Stok Kartı Kayıtlarında Yapılması Gerekenler aşağıdaki şekildedir:

![](../../../../_assets/587293f7dd0e7d94d9cf.png)

- Bu sistemin uygulanması için "Stok Kartı Kayıtları" bölümünde bulunan "Birim Puan" alanına stoka ait birim puan girilir. Böylece, "Fatura Modülünden" bu ürün için yapılan satış ve alışlarda (miktar \* puan değeri ile) puan toplamı hesaplanır.

**Örneğin:** Bir ürünün birim puanının 20 olduğu ve bu üründe 100 adet alındığı varsayıldığında, faturanın kesildiği müşterinin 2000 puanı olur.

- İlgili ürünün kaç puan karşılığında verileceği bilgisi "Puan Değeri" alanında belirlenir. Bu üründen bir adet hediye olarak verilmesi için, cari hesabın en az bu değer kadar puanının olması gerekir.

**Örneğin:** 8.000 puanı olan müşteri, puan değeri 10.000 olan bir üründen alamaz. Uygulamada, birim puanı dolu olan her stok kartının satışında otomatik olarak puan hesaplanır. Puan değeri dolu olan stok kartları da hediye ürün olarak verilir.

**Fatura Modülünde Yapılması Gerekenler**

Fatura Modülünde Yapılması Gerekenler aşağıdaki şekildedir:

- Fatura Modülünde, içindeki ürünler için birim puan girilen her faturada puan hesaplaması otomatik yapılır.

**Örneğin:** 00001 nolu stok kartında için birim puan olarak 20 değerinin girildiği, 06000 numaralı cariye bu üründen toplam 1100 adet satıldığı ve bunun 10 adedinin de iade edildiği varsayıldığında, "Cari Hareket Kayıtları" ekranında, örnek ekranda görüldüğü gibi cari hesabın satır bazında puanları ve toplam puanı izlenir. Puan kazandıran ürünlerden satın alındıkça puanlar toplanır ve bu üründen iade olduğunda da toplam puandan düşülür.

![](../../../../_assets/6d388754ebb1e939f6e8.png)

![](../../../../_assets/3185ce600988adebdaf7.png)

- İşlem yapılan carinin güncel biriken puanları, fatura kayıt ekranında iken fare ile sağ klik tuşu tıklandığında ekrana gelen özel tuşların içinden "Cari Kart İzleme" seçilerek izlenir.

![](../../../../_assets/7a5cddf17b5a506e7cff.png)

- Puan kazandıran ürünlerin bulunduğu fatura kayıtlarındaki "Toplamlar" sekmesinde ilgili faturaya ait **hediye puan** izlenir.

![](../../../../_assets/6b68563616d07a7ca1cb.png)

- Fatura Modülünde yapılan işlemlerde hangi tip faturalarda puan karşılığı hediye ürün verileceğinin anlaşılması için; "Özel Kod 2" kullanılır. Bunun için fatura parametrelerinde yer alan "Özel Kod ve Açıklama" sekmesindeki "Özel Kod 2", "Açıklama" bölümünde "Özel Kod2" ve "Özel Kod 2 Değeri Tablodan mı Kontrol Edilsin" parametrelerinin işaretlenmesi gerekir.

**Özel Kod 2 Tanımlama**

Faturaları kaydederken, puan karşılığı hediye ürün verilmesi için parametrelerde yapılan işaretleme gereği, "Özel Kod 2" değerinin tanımlanması gerekir. Bunun için; Fatura → İşlemler → "[Özel Kod 2 Tanımlama](<../../Fatura/İşlemler - Fatura/Özel Kod - 2 Tanımlama.md>)" bölümü kullanılır.

![](../../../../_assets/9d4384189648ed724ce9.png)

Özel Kod istenilen şekilde tanımlanabilir.

**Örneğin:** A, B, P, 1, 2, 3 gibi.

Açıklama bölümüne mutlaka **PUAN** kelimesinin girilmesi gerekir.

Puan kelimesinin başında veya sonunda başka bir açıklamanın yer almaması gerekir. (Puan Uygulaması, Puan Sistemi gibi).

Böylece, puan karşılığı hediye amaçlı kesilen fatura kayıtları sırasında aktif hale gelen Özel Kod 2 alanı kullanılır.

Yukarıda örnek ekranda bahsedilen carinin toplam 22.200 hediye puanı mevcut. Buna karşılık 00001 numaralı stoktan hediye almak istediğini ve 00001 stokun da 10.000 puan değeri olduğu varsayıldığında; hediye için fatura keserken bazı koşullara dikkate edilmesi gerekir.

Öncelikle bu tür faturaları keserken, "Özel Kod 2" alanına, uygulamada kullanılacak değerin girilmesi gerekir.

![](../../../../_assets/42a9ed0ce89ee9cac72a.png)

"Kalemler" sekmesinde puan değeri 10.000 olan stoktan 3 adet hediye verilmesi istendiğinde, aşağıdaki uyarı ekranı ile karşılaşılır. Bu üründen 3 adet verilmesi için müşterinin en az 30.000 puanının olması gerekir. Bu durumda, bu üründen bir veya iki adet hediye verilir.

Hediye ürün verilen faturalarda, fatura toplamı kadar (% 100) satır iskontosu yapılır ve genel toplam sıfırlanır.

Bu tür faturalarda, hediye ürünler dışındaki ürünler (puan değeri olmayan) satılmaz. Satılması istendiğinde, program tarafından "Bu ürün hediye faturasında kullanılamaz" uyarısını ekrana getirilir.

Hediye faturaları cari hareket kayıtlarına tutarsız olarak aktarılır ve kullanılan puan cari hesabın toplam puanından düşer.

**Puan Bilgilerinin Raporlanması**

Puan rakamlarının listelenmesi için Genel → Rapor → Raporlar → Cari Hareket Listesi → "Puan" alanı kullanılır.
