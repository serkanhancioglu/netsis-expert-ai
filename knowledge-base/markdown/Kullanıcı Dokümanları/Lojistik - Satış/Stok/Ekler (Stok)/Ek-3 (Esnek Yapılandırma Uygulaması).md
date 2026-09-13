---
title: "Ek-3 (Esnek Yapılandırma Uygulaması)"
page_id: "29993147"
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
  - "Ek-3 (Esnek Yapılandırma Uygulaması)"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Stok / Ekler (Stok) / Ek-3 (Esnek Yapılandırma Uygulaması)"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTUzYzkzOTE1LTRjZTItNGIxYi1hYWY3LWZhNzMzNzZhMWZjNyZsaW5rPTk3MjNkODU2LTIwYzMtNDVjNy05MDMxLTU2YzBhOTYxOGZkMSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=53c93915-4ce2-4b1b-aaf7-fa73376a1fc7&link=9723d856-20c3-45c7-9031-56c0a9618fd1&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ek-3-esnek-yapilandirma-uygulamasi_30000747_29993147.html"
source_version: "2022-11-22T11:34:50.017+03:00"
source_bytes: 2750215
fetched_at: "2026-09-13T04:05:30+00:00"
generator: "netsis-scraper 1.0.0"
---
# Ek-3 (Esnek Yapılandırma Uygulaması)

Esnek Yapılandırma Uygulaması ile ilgili detaylı bilgiye bu dokümandan ulaşılır.

**Kullanım Amacı:** Bu uygulama ile, stokların sahip oldukları özellikler bazında, ayrı kartlar yerine tek bir kartta takip yapılması sağlanır. Böylece, hareket girişlerindeki reçetelerde tek bir kart üzerinden işlem yapılmasını ve stokun sahip olduğu özellikler bazında bakiye takibi yapılmasını sağlar.
Bazı sektörlerdeki ürünler, sahip oldukları özelliklere göre farklılaşır. Üretilen ürün tek olmasına rağmen, üretilen mamulün her bir özelliğine göre farklı stok kartı ve reçete tanımlanması gerekir.

**Örneğin:** Gömlek üreten bir firma, aynı gömleği farklı renk ve bedenlerde ürettiğinde, her bir renk ve beden ayrı stok kartı ve reçete anlamına geliyordu. Uygulamayı kolaylaştırmak amacıyla, stok kartlarına bu tipteki mamullerin farklı özelliklere sahip olduklarının belirlenmesi için olanak sağlandı. Ayrıca, bu mamuller için programa eklenen ayrı bir bölümden reçete oluşturulması sağlandı.

Sipariş, satın alma, satış vb. bölümlerde (mamul özellikli ise) hangi özellikte mamulün işlem gördüğü sorgulanır.

**Örneğin:** Gömlek üreten bir firmanın değişik renk (beyaz ve mavi) ve bedenlerde (medium, small ve large) gömlek ürettiği varsayıldığında ve esnek yapılandırmanın kullanılmadığı durumlarda açılması gereken stok kartları aşağıdaki gibidir:

Gömlek1: Beyaz, Small (S)

Gömlek2: Beyaz, Medium (M)

Gömlek3: Beyaz, Large (L)

Gömlek4: Mavi, Small (S)

Gömlek5: Mavi, Medium (M)

Gömlek6: Mavi, Large (L)

Sonuç olarak aynı gömlek için açılması gereken stok kartı sayısı altı olacak iken, esnek yapılandırma uygulaması ile sadece tek bir kart açmak yeterli hale gelir. Firmanın, gömlek için G001 kodunu kullandığı varsayıldığında;

G001 stok kartı açılırken Stok → Kayıt → Stok Kartı Kayıtları → Ek Bilgiler → "Esnek Yapılandır" seçeneğinin işaretlenmesi gerekir. Böylece, stokun sahip olduğu özelliklere göre farklılaşacağı anlaşılır. Daha sonra, stokların sahip oldukları özelliklerin tanımlanarak işleme devam edilir.

**Kullanıma Yönelik Bilgiler**

Yapılandırma başlangıç numaraları kullanımı bir örnekle açıklanacak olursa, aşağıdaki ekranlarda değişken parametresi seçilerek oluşturulan kodun başlangıç karakteri, içinde bulunulan tarihteki yıl ve ay rakamlarından oluşur.

Otomatik oluşan yapılandırma kodları ile yapılandırma koduna ait konfigürasyonun detayı aşağıda görüldüğü şekildedir.

![](../../../../_assets/1967c98f84a1c9ceb96b.png)![](../../../../_assets/f078a9ec99a479de2455.png)

**Yapılandırma Tanımları Kullanımı**

Stok Hareket Kayıtları, Sipariş, İrsaliye, Fatura Kayıtları, İş Emri Kayıtları, Ürün Ağacı (reçete) Kayıtları, MRP için Üretim Planı Girişleri gibi sistem geneli stok kodu sorgulanan her yerde, "Stok Kartı Kayıtları" bölümündeki "Esnek Yapılandır" seçeneği işaretli olan stoklardan birinin seçilmesi halinde, "Yapılandırma Kodu" sorgulanır. Sorgulanan alana işlem gören stokun hangi yapılandırma koduna sahip olduğunun girilmesi gerekir. "Yapılandırma Kodu" alanı boş bırakılmaz.

"Stok Hareket Kayıtları" bölümünde diğer modüllerden entegre olarak gelen hareketlerin yapılandırma kodu söz konusu alana aktarılır. Aktarılan yapılandırma kodunun değiştirilmesi işlemi, "Stok Hareket Kayıtları" bölümünden değil, kaydın girildiği modülden yapılır.

**Yapılandırma Kodu:** İşlem gören stokun hangi yapılandırma koduna sahip olduğunun belirlendiği alandır.

Aşağıdaki örnekte 10 adet gömlek girişi yapıldığı görüntülenir. Gömleğin stok kartında "Esnek Yapılandırma" seçeneği işaretli olduğu için "Yapılandırma Kodu" aktif haldedir. Girişi yapılan gömleğin rengi **beyaz**, bedeni de **large** olduğu için **"BL"** olarak tanımlı olan yapılandırma kodu seçilmiş.

Stok Kartı Kayıtları bölümünde "Esnek Yapılandır" seçeneği işaretli stoklarda "Yapılandırma Kodu" sorgulanır. Sorgulanması halinde bu alan boş bırakılmaz.

![](../../../../_assets/6bfb7095f6f88a61f066.png)

**Yapılandırma Sihirbazı Kullanımı**

**Yapılandırma Sihirbazı:** Yapılandırma özelliği olan ürünler için (stok kartında yapılandırılabilir tanımı olan), sistem geneli hangi işlemde olursa olsun stok koduyla birlikte yapılandırma kodu da verilir. Kullanılması istenen ve özellik kombinasyonu içeren yapılandırma kodunun, sistemde tanımlı yapılandırma kodları içinde mevcut olup olmadığını saptamak ve tanımlı değilse hızlı bir şekilde tanımlamak için kullanılan işlemdir.

**Yapılandırma Bilgilerinden Arama:** Belirtilmesi istenen kombinasyonda bir yapılandırmanın mevcut olup-olmadığını saptamak için, herhangi bir kısıt verilmeden Özellikleri Ara ![](../../../../_assets/5c96ed431410ef20681b.png) butonu tıklandığında, "Arama Sonuçları" alanında "Ürün Yapılandırma Tanımlamaları" bölümünde belirlenen yapılandırma kodları listelenir. Yapılandırma kodlarının sağ tarafında, ilgili stoka ait bakiyeler yapılandırma kodu bazında görüntülenir.

![](../../../../_assets/1a859e18de8f77d850e6.png)

Kısıt vermek için grid ekran kullanılır. Özellik kataloğundaki herhangi bir özellik kodu için, aranılan değer ve alternatif olabilecek değerler kısıt olarak verilir. Grid üzerindeki hücrelere veri girişinin sağlanması için, ilgili hücrenin üzerindeyken klavye üzerindeki "Boşluk" tuşuna basılır. Bu tuş ile, üzerinde bulunulan hücreye girilecek geçerli bilgiler, liste halinde ekranda görüntülenir. Listeden seçim yapıldıktan sonra "Enter" tuşu ile hücre düzenleme işlemi sonlandırılır. Kısıt Sil![](../../../../_assets/79eb132596df8983e6d8.png)ya da klavyedeki F7 tuşu kullanılarak, üzerinde bulunulan kısıt satırı silinir. Verilen kısıtların tamamının silinmesi istendiğinde ise, Hepsini Sil ![](../../../../_assets/28c5b1a32323bd1ce1c9.png) butonu kullanılır.
Kısıt girildikten sonra Özellikleri Ara ![](../../../../_assets/5c96ed431410ef20681b.png) butonuna tıklandığında, verilen kısıtlara uygun yapılandırma kodları "Arama Sonuçları" alanında listelenir. Kısıt verilirken "Arama Tipi" olarak **Tam Arama** ya da **Opsiyonel Arama** seçeneklerinden biri tercih edilebilir. **Tam Arama** seçeneği kullanıldığında, "Arama Sonuçları" alanında sadece girilen kısıta uyan yapılandırma kodları listelenir. **Opsiyonel Arama** seçildiğinde ise, "Arama Sonuçları" alanında, verilen kısıtlara uyan yapılandırma kodları öncelikli olarak listelenir. Özellik Kopyala ![](../../../../_assets/d82433767bf56df50f98.png)butonuna basıldığında "Yeni Yapılandırma İçin Bilgi Girişi" sekmesine geçilir.

SBOM ![](../../../../_assets/34fa6d6f15130ec4b811.png) butonunun kullanımı ile ilgili detaylı bilgi için, Üretim → Kayıt → Süper Reçete Kaydı

![](../../../../_assets/cf8279e2ee155422b79b.png)

**Yeni Yapılandırma İçin Bilgi Girişi**

Kullanılması istenen özellikleri içeren bir yapılandırma kodu saptanamadığında, yapılandırma oluşturulması için kullanılan bölümdür. Üretilen farklı mamuller benzer yapılandırma konfigürasyonlarına sahip olabilir. Dolayısı ile tüm yapılandırma kodlarının teker teker tanımlanması zaman alacağı için, tanımlanan yapılandırma kodu üzerinde değişiklik yapılarak saklanması için de bu bölüm kullanılır.

**Yeni Yapılandırma Kodu Tanımlanması**

Yeni Yapılandırma Kodu Tanımlanması bilgileri aşağıdaki şekildedir:

![](../../../../_assets/7b16b72c482c83c18405.png)

| Yapılandırma Kod Sihirbazı Ekranı |  |
| --- | --- |
| Yapılandırma Kodu | Tanımlanacak yapılandırma kodunun girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, kodlar arasından seçim yapılabilir. |
| Yapılandırma Adı | Tanımlanan yapılandırma koduna ait ismin girildiği alandır. |
| Geçerlilik Başlangıç ve Bitiş Tarihi | Yeni tanımlanan yapılandırma koduna ait başlangıç ve bitiş tarihinin girildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile, takvim yardımıyla da seçim yapılabilir. |
| Farklı Kaydet | Tanımlı yapılandırma kodu üzerinde değişiklik yapılarak kaydedilmesini sağlayan parametredir. İşaretlendiğinde, "Yeni Yapılandırma Kodu" alanı sorgulanır. Yeni yapılandırma kodu girildikten sonra Konf. Sakla ve Geriye Dön ![](../../../../_assets/4467d5f0e2451cb2b612.png) butonuna tıklanarak kaydedilir. Tanımlı yapılandırma kodlarından bağımsız, yeni bir yapılandırma kodu tanımlanıyorsa bu seçeneğin işaretlenmemesi gerekir. |
| ![](../../../../_assets/30100fd58c110027b974.png) Özellik Sil | Grid ekranındaki özelliklerin silinmesi için kullanılan butondur. Grid üzerinde silinmesi istenen özelliğin üzerine fare ile bir kez tıkladıktan sonra butona basıldığında silme işlemi gerçekleşir. |
| ![](../../../../_assets/28c5b1a32323bd1ce1c9.png) Hepsini Sil | Grid ekranında görülen özelliklerin hepsinin silinmesi istendiğinde kullanılan butondur. |

Tanımlı yapılandırma kodu kopyalanacak ise:

![](../../../../_assets/13ccb12239b196f75010.png)

| Yapılandırma Kod Sihirbazı Ekranı |  |
| --- | --- |
| Yapılandırma Kodu | Daha önceden tanımlanmış ve üzerinde değişiklik yapılarak farklı isimle saklanması istenen yapılandırma kodunun seçildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, kodlar arasından seçim yapılabilir. |
| Yapılandırma Adı | Yapılandırma kodu seçildikten sonra "Ürün Yapılandırma Kayıtları" bölümünden aktarılan ismin program tarafından ekrana getirildiği alandır. Yeni tanımlanacak yapılandırma kodu için buraya yeni bir isim girilir. |
| Geçerlilik Başlangıç ve Bitiş Tarihi | Kopyalanacak yapılandırma koduna ait başlangıç ve bitiş tarihinin girildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile, takvim yardımıyla da seçim yapılabilir. |
| Farklı Kaydet | Seçeneğin işaretlenmesi ile, "Yapılandırma Kodu" alanına girilen kodun, farklı bir kod kullanılarak kopyalanacağı anlaşılır ve "Yeni Yapılandırma Kodu" alanı sorgulanır. |
| ![](../../../../_assets/30100fd58c110027b974.png) Özellik Sil | Grid ekranındaki özelliklerin silinmesi için kullanılan butondur. Grid üzerinde silinmesi istenen özelliğin üzerine fare ile bir kez tıkladıktan sonra butona basıldığında silme işlemi gerçekleşir. |
| ![](../../../../_assets/28c5b1a32323bd1ce1c9.png) Hepsini Sil | Grid ekranında görülen özelliklerin hepsinin silinmesi istendiğinde kullanılan butondur. |
| Yeni Yapılandırma Kodu | "Yapılandırma Kodu" alanında seçilen kodun üzerinde değişiklik yapılıp kaydedilmesi sırasında yeni oluşacak yapılandırma koduna ait bilginin girildiği alandır. Yapılandırma kodunun alınması istenen özellik değerleri grid alanda belirledikten sonra, "Yeni Yapılandırma Kodu" alanının sağ tarafında yer alan Konf. Sakla ve Geriye Dön ![](../../../../_assets/4467d5f0e2451cb2b612.png) butonuna tıklanarak kayıt işlemi tamamlanır. |

Kaydedilen yapılandırma kodları, "Ürün Yapılandırma Tanımlamaları" bölümünden izlenebilir ya da sahip olduğu değerler değiştirilebilir. Kayıtların silme işlemi, "Ürün Yapılandırma Kayıtları" bölümünden ilgili kod seçilerek yapılır.

Yapılandırma kodunun silinmesi için, kodun stok hareketlerinde kullanılmamış olması gerekir.

#### Yapılandırılabilir Ürün Girişi

Özellikle sipariş girişi gibi belgelerin üzerinde, yapılandırılabilir olan ürünlerin (stok kartında yapılandırılabilir tanımı olan), birden fazla yapılandırma koduna ait giriş/çıkış miktarlarının tek seferde kaydedilmesi için kullanılır.![](../../../../_assets/a8eb35a961a67bb8e52e.png)

Ekrana, "Ürün Yapılandırma Profili" bölümünde tanımlanana tüm özellik kodları ve alacağı değerleri içeren kombinasyonlar, matris halinde görüntülenir. Kaydedilmesi istenen miktarın girilmesi için, yapılandırma satırındaki "Stok Miktarı" alanının üzerine bir kez tıklanması yeterlidir.

Yukarıdaki ekranda; Beyaz renk için 5, Mavi renk için 10, Sarı renk için de 5 adet miktar girişi yer alır. Tamam ![](../../../../_assets/39d77b8716226638d9ce.jpg) butonuna basıldığında, "Stok Hareket Kayıtları" aşağıdaki şekilde oluşur.

![](../../../../_assets/bc56d8c15dc4e2c83f78.png)

"Yapılandırılabilir Ürün Girişi" ekranında 3 farklı yapılandırma koduna giriş yapıldığı için, bu girişler stok hareketlerine yapılandırma kodları bazında ayrı kayıtlar halinde aktarılır.
"Stok Hareket Kaydı" sırasında miktar girilse bile, "Yapılandırılabilir Ürün Girişi" ekranında belirlenen miktar dikkate alınır ve hareketler burada girilen miktara göre oluşur.
"Stok Hareket Kayıtları" bölümünde sorgulanan yapılandırma kodları ve bu kodların girişinde kullanılan sihirbazlar, stok kodu girişi yapılan diğer modüllerde de sorgulanır. Eğer, seçilen stok kodunun kartında "Esnek Yapılandır" seçeneği işaretli ise yapılandırma kodu bu bölümlerde de boş bırakılmaz.

![](../../../../_assets/aeb0bb7c8719f9d8ed03.png)

**Örneğin:** Satış Faturası kaydı sırasında yapılandırılacak stok kodu girildiğinde, ilgili stokun yapılandırma kodu sorgulanır ve faturadaki kalem bilgileri, aynı stok için farklı yapılandırma kodları seçilerek girilen miktarlar bazında oluşur.

Stok kodu için girilen yapılandırma kodu grid ekrandan izlenebilir.

**Dinamik Değerler Kullanımı**

"Özellik Tanımlamaları" ekranında "Değerler Dinamik" seçeneği işaretlenerek tanımlanan özellikler için "Yapılandırılabilir Ürün Girişi" bölümünden yeni değerler girilir.

![](../../../../_assets/ad7b18c0253388ed519e.png)

**Örneğin:** Renk özelliği için "Özellik Tanımlamaları" ekranında yapılan tanımlamanın yukarıdaki şekilde olduğu varsayıldığında; Renk özelliği, "Değerler Dinamik" seçeneği işaretlenerek kaydedildiği için, bu özelliğe hareket girişi esnasında yeni özellik değerleri verileceği anlaşılır. Ancak, renk özelliğinin alacağı değerler standart olduğundan, bu değerlerin "Özellik Tanımlamaları" bölümünde belirlenmesi daha sonraki kullanımda kolaylık sağlar.
"Değerler Dinamik" seçeneği işaretlenerek kaydedilen özellikler için, "Özellik Tanımlama" bölümünde bilgi amaçlı olarak değer tanımlaması yapılır. Tanımlanan değerlerin bilgi amaçlı olmasının sebebi, "Yapılandırılabilir Ürün Girişi" ekranında bu değerlerin kullanıcı tarafından görülmemesinden kaynaklanır.
"Özellik Tanımlamaları" bu şekilde yapıldıktan sonra, esnek yapılandırılacak ürüne ait hareket girişi sırasında, Yapılandırılabilir Ürün Girişi butonu ![](../../../../_assets/4d5937e5d0ca7cc09b74.png) kullanılarak, değerleri dinamik olmayan özellikler için daha önceden tanımlanmış değerler seçilir.

Sadece dinamik değere sahip özellikler için yeni değer girişi yapılır.

![](../../../../_assets/a8eb35a961a67bb8e52e.png)

Ürünün dinamik değere sahip özelliği olmadığında, özelliklerine ait değerlerin tümü matrise gelir ve bu değerlere ait mevcut stok bakiyeleri izlenir. Ancak, ürünün sahip olduğu özelliklerden herhangi biri için "Değerler Dinamik" seçeneği işaretlendiyse, "Yapılandırma Ürün Girişi" matrisine girildiğinde ekran boş olarak görüntülenir. Bu aşamada, dinamik değere sahip olmayan özellikler için önceden tanımlanmış değerler arasından seçim yapılır. Ancak, değerleri dinamik olan özelliklere ait değerler ilgili sütuna elle (manuel) girilir. Girilen değerler program tarafından saklanır ve "Özellik Tanımlamaları" bölümüne aktarılır. Ekranın sol üstünde bulunan Ekle ![](../../../../_assets/b050fee00ab65632b16d.jpg) butonunu ya da klavyede yer alan "boşluk" tuşu kullanılarak matrise yeni satır/satırlar eklenir. Sil ![](../../../../_assets/3b7f9a10b6b12eb5cbcb.png) butonu ya da klavyede yer alan "Delete" tuşu kullanarak da seçili satır silinir.
Bu bölümde belirlenen konfigürasyonlara ait daha önceden tanımlanmış bir yapılandırma kodu yoksa, kayıt esnasında program tarafından oluşturulur.

**Yapılandırılabilir Ürün Girişi Matrisinde Sıralama Özelliği**

Özellik değerlerinin çok fazla çeşitlilik gösterdiği durumlarda, istenen değerin "Yapılandırılabilir Ürün Girişi" matrisinde bulunması zaman alabilir. Ancak, matriste yapılan değişiklikler sonrasında, yapılandırma kodu ve özellik değerlerine göre sıralama yapılarak istenen kayda daha kolay ulaşılması sağlanır.

![](../../../../_assets/271abdc4193f07e5b83a.png)

Matriste bulunan sütunlardan hangisine göre sıralama yapılması isteniyorsa, ilgili sütun üzerinde iken klavyede yer alan "Alt+Aşağı Ok" ya da "Alt+Yukarı Ok" tuşları ile istenen yönde sıralama yapılması sağlanır.

Yukarıda yer alan ekranda, bilgilerin "Alt+Aşağı Ok" tuşları kullanılarak, yapılandırma kodu bazında artan şekilde sıralanması yer alır.

Aşağıda ise, aynı bilgilerin "Alt+Yukarı Ok" tuşları kullanılarak, renk özelliği bazında azalan şekilde sıralanması yer alır.

![](../../../../_assets/0156f48fb60536b9456c.png)

Sıralama fonksiyonu "miktar" alanları için kullanılmaz.

#### Yapılandırma Kodu Bilgileri

Fatura, irsaliye ,sipariş, iş emri gibi, stokla ilişkili işlem yapılan ekranlarda Yapılandırma Kodu Bilgileri butonu ![](../../../../_assets/4d5937e5d0ca7cc09b74.png) aktif hale gelir. Bu buton, seçilen yapılandırma koduna ait özelliklerin ve özellik değerlerinin görüntülenmesini sağlar.

**Örneğin:** Özellik kodları renk ve beden olan gömlek stokuna ait bir yapılandırma kodu seçildiğinde, detayları aşağıdaki şekilde görüntülenir.

![](../../../../_assets/9d5e6ab2ad0c434ad2e3.png)

#### Yapılandırma Açıklaması Kullanım Şekli Örnekleri

Stok → Kayıt → Stok Parametreleri → "Yapılandırma Açıklaması Kullanım Şekli" alanında yapılan seçime göre oluşacak görüntüler aşağıdaki şekilde oluşur.

**Örneğin:** Gömlek stokuna ait bir yapılandırma kodunun özellik kod ve değerinin aşağıdaki gibi olduğu varsayıldığında:

```text
Özellik Kodu         Özellik DeğeriM Beden               MR Renk                  B Beyaz
```

Stok → Kayıt → Stok Parametreleri → Yapılandırma Açıklaması Kullanım Şekli → "Özellik ve Değer Kodlarından Oluşsun" parametresinin işaretlenmesi durumunda; Fatura, İrsaliye, Sipariş, İş Emri gibi yapılandırma kodunun seçildiği ekranlarda, yapılandırma koduna ait açıklama aşağıdaki şekilde oluşur.

![](../../../../_assets/100636fa3d080a5f988c.png)

Stok → Kayıt → Stok Parametreleri → Yapılandırma Açıklaması Kullanım Şekli → "Özellik ve Değer Açıklamalarından Oluşsun" parametresinin işaretlenmesi durumunda; Fatura, İrsaliye, Sipariş, İş Emri gibi yapılandırma kodunun seçildiği ekranlarda, yapılandırma koduna ait açıklama aşağıdaki şekilde oluşur.

![](../../../../_assets/820e7c7e2a7b0b153111.png)

Stok → Kayıt → Stok Parametreleri → Yapılandırma Açıklaması Kullanım Şekli → "Girilmiş Yapılandırma Açıklamalarından Oluşsun" parametresinin işaretlenmesi durumunda; Fatura, İrsaliye, Sipariş, İş Emri gibi yapılandırma kodunun seçildiği ekranlarda, yapılandırma koduna ait açıklama aşağıdaki şekilde oluşur. Açıklama alanında yapılandırma kodu tanımlanırken elle (manuel) veya otomatik oluşturulan kayıtlar da "Otomatik" gösterilir.

![](../../../../_assets/8c86a66658876b44a09a.png)
