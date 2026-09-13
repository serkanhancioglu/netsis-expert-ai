---
title: "Ek-5 (Koşul Uygulamalarında Grup Desteği)"
page_id: "22805763"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Cari"
  - "Ekler"
  - "Ek-5 (Koşul Uygulamalarında Grup Desteği)"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Cari / Ekler / Ek-5 (Koşul Uygulamalarında Grup Desteği)"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWRjNGEwNjgxLTQzYTYtNDMzZC1iNWFiLTRjYmJkMmY1MGI4OCZsaW5rPWQ0MzQyZjlkLTdhZDEtNDJkZS04M2RiLWY0NTJiYWM3MGJkNCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=dc4a0681-43a6-433d-b5ab-4cbbd2f50b88&link=d4342f9d-7ad1-42de-83db-f452bac70bd4&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ek-5-kosul-uygulamalarinda-grup-destegi_29991943_22805763.html"
source_version: "2022-11-21T15:14:00.227+03:00"
source_bytes: 271445
fetched_at: "2026-09-13T04:08:52+00:00"
generator: "netsis-scraper 1.0.0"
---
# Ek-5 (Koşul Uygulamalarında Grup Desteği)

Koşul uygulamaları hakkında ayrıntılı bilgiye bu dokümandan ulaşılır.

Stoka ya da stok gruplarına verilecek mal fazlasının stok grubu olarak belirlenmesi ve hak edilen mal fazlası miktarının tespiti için belgede girilen tüm kalemlere bakılması mümkündür.

**Örneğin:** Makarna grubunda bulunan stoklardan 10 adet alana, sos grubundaki stoklardan 1 tane mal fazlası olarak verilmesi gibi.

Böylece mal fazlası miktarı tespit edilirken, belgede girilen makarna grubuna dahil stokların toplam miktarına bakılır. Ayrıca koşul tanımlamalarında tutar ya da miktar aralığına göre satır iskonto oranı tanımlandığında, belgede girilen kalemlerden koşulun geçerli olduğu kalemlerin toplam tutarı ya da miktarı kontrol edilir ve satır iskontosu buna göre getirilir.

Grup Koşul uygulamasının kullanılması için programın bazı bölümlerindeki alan ve seçeneklerin açıklamaları aşağıdadır;

**Koşul Kayıtları “Grup Koşul” Alanları**

Detay koşul kayıtlarında bu uygulama için, "Detay Koşul Bilgileri" ve "Mal Fazlası" sekmelerinde sorgulama yapılır.

![](../../../../_assets/53bf7ea16fff99378358.png)

"Grup Koşul" alanının işaretlenmesi, fatura belgelerinde girilen tüm kalemlerin toplamı üzerinden iskonto ve/veya mal fazlası hesaplaması yapılacağı anlamına gelir.

![](../../../../_assets/cc24329eff273ff9e8a1.png)

“Mal Mazlası Grup” sorgusu, stok için verilecek mal fazlasının bir gruptaki stoklardan herhangi birinin olması durumunda bu seçeneğinin mutlaka işaretlenmesi gerekir. Aksi takdirde, mal fazlası olarak ya stokun kendisi ya da farklı tek bir stok belirlenir. "Mal Fazlası Grup" seçeneği işaretlendikten sonra, tanımlanan koşul için hangi stok grubundan mal fazlası verileceği, "Geçerli Mal Fazlası Stokları" bölümünde belirlenir Yukarıdaki örneğe göre mal fazlası olarak “G02” grubuna dahil stoklardan biri girilir. Grup mal fazlası belirlenirken, grup kodu dışında diğer rapor kodları da kullanılabilir.

**Satış Fatura Parametrelerinde “Grup Koşul” Parametreleri**

Satış Fatura Parametrelerinde “Grup Koşul” Parametreleri aşağıdaki şekildedir:

![](../../../../_assets/000ce4bae0176d83fbb4.png)

**“Grup Koşul Uygulama Yeri”** parametresi ile, grup koşul uygulamasının hangi belgede uygulanacağı belirlenir. Detay koşul kaydında, grup koşul tanımlamaları yapıldıktan sonra, grup iskontoların hangi belgede verileceği bu bölüm kullanılarak önceden belirlenir.

**Örneğin:** Mal fazlası iskontolarının, sipariş kaydında iken belgeye yansıtılması istendiğinde, “Sipariş” seçeneğinin işaretlenmesi gerekir. Sipariş ya da belirtilen belgede yapılan iskontolar, sonraki bağlantılı belgelere aynen aktarılır ve tekrar sorgulanmaz.

Bu bölümde “Yok” seçeneğinin işaretlenmesi halinde, hiçbir belgede grup koşulu uygulanması yapılmaz.

**“Mal Fazlası Koşulu Sağlamalı”** parametresi işaretlendiğinde, program tarafından belirlenen mal fazlası miktarından faklı bir mal fazlası girilmesine izin verilmez. Parametrenin işaretli olmadığı durumlarda ise, belgede hesaplanan mal fazlası miktarından farklı bir mal fazlası miktarı girilebilir.

**“Çakışan Grup Koşullarda Aralık İskonto Politikası”** parametresi ise kalem bilgilerinde girilen stok için, detay koşul kayıtlarında birden fazla grup koşulun geçerli olduğu durumlarda, miktar/tutar aralığı iskontosu oranı olarak ne getirileceğinin belirlendiği parametredir. Grup koşulun uygulanmadığı durumlarda (belgede girilen kalem birden fazla koşul için geçerli olduğunda) program, detay kayıtlarından bulunan ilk koşula göre oran getirir. Ancak grup koşul kullanıldığında miktar ya da tutar aralığı kalemlerin toplamına göre tespit edildiği için, birden fazla koşul kontrol edilir.

**Örneğin:** Aşağıda bazı stokların rapor kodları yer alır.

| Stok Kodu | Grup Kodu | Kod-1 |
| --- | --- | --- |
| 001 | G01 | K1 |
| 002 | G01 |  |
| 003 | G01 | K1 |
| 004 | G02 | K1 |
| 005 | G02 |  |

Detay koşul kayıtlarında çoklu seçime göre tanımlama yapıldığında bir stok birden fazla detay koşula dahil olabilir. Detay koşul kayıtlarında "Grup Koşul" seçeneği işaretlenerek yapılan tanımlamaların aşağıdaki gibi olduğu varsayıldığında aşağıdaki şekildedir:

| Koşul Kodu | Geçerli Stoklar | Miktar Aralığı | İskonto Aralığı |
| --- | --- | --- | --- |
| K01 | G01 | 10-20-30 | 1% - 2% - 3% |
| K01 | G02 veya K1 | 10-20-30 | 3% - 4% - 6% |

K01 koşul kodu ile oluşturulan fatura belgesinde miktarlar aşağıdaki şekildedir:

| Stok Kodu | Miktar |
| --- | --- |
| 001 | 3 |
| 002 | 2 |
| 003 | 5 |
| 004 | 6 |
| 005 | 8 |

Bu durumda program, girilen kalemler için hangi koşulların geçerli olduğunu kontrol eder. Kontrol sırasında öncelikle, detay koşul kayıtlarında yer alan ilgili kalem için geçerli olan ilk satır dikkate alınır.

001,002 ve 003 stoklarının grup kodu "G01" olduğu için, detay koşul kayıtlarındaki ilk tanımlama geçerlidir ve bu kalemlerin toplam miktarı 10 olduğu için, iskonto oranı 1'dir. 004 stokunun Grup Kodu "G02" Kod-1 değeri "K1", 005 stokunun da Grup Kodu "G02" olduğu için bu iki stok detay koşul kayıtlarındaki ikinci tanımlamaya girer. Ancak, bu iki kalemin toplamı alınmadan önce bu koşulu sağlayan stokların fatura kalemlerinde olup olmadığı kontrol edilir. Bu durumda 001 ve 003 kodlu stoklarının da Kod-1 bilgileri "K1" olduğu için toplama dahil edilir. Böylece 001,003,004 ve 005 kodlu stoklar detay koşul kayıtlarındaki ikinci satır için geçerlidir ve toplam miktarları 24 olarak hesaplanır. Bu miktar için yapılması gereken iskonto %4’tür. Sonuç olarak 001 ve 003 stokları için iki detay koşul kaydı geçerlidir ve bu kayıtlar sonucu farklı iskonto oranları bulunur.

Bu aşamada bulunan iskonto oranlarından hangisinin faturaya yansıtılacağı bu parametrede belirlenir. Eğer politika olarak, **“İskonto değeri büyük olan koşulu dikkate al”** seçilirse, 001 ve 003 kodlu stokların iskonto oranları ikinci koşul detay kaydından aktarılır.

| Stok Kodu | **İskonto** **Oranı** |
| --- | --- |
| 001 | 4 |
| 002 | 1 |
| 003 | 4 |
| 004 | 4 |
| 005 | 4 |

002 stokunun belgede girilen miktarı tek başına aralık iskontosu almaya yetmemesine rağmen, 001 ve 003 kodlu stokların miktarları da toplama dahil edildiği için 002 stokuna iskonto yapılmıştır. Eğer politika olarak parametrelerde, **“İskonto değeri küçük olan koşulu dikkate al”** seçilirse, 001 ve 003 kodlu stokların iskonto oranları ilk koşul detay kaydından aktarılır.

| Stok Kodu | **İskonto** **Oranı** |
| --- | --- |
| 001 | 1 |
| 002 | 1 |
| 003 | 1 |
| 004 | 4 |
| 005 | 4 |

Yukarıda da belirtildiği gibi 001 ve 003 kodlu stoklar için geçerli olan ikinci detay koşulu çalışsaydı daha yüksek iskonto oranı geleceği için, bu stoklar için ilk koşul detay dikkate alınır. Ancak 004 ve 005 için iskonto oranının bulunmasında kullanılan toplam bilgisine 001 ve 003 stokları da dahil edilir.

**Fatura Belgelerinde “Grup Koşul” Seçenekleri**

Grup mal fazlası miktarlarının izlenmesi için fatura belgelerinin "Kalem Bilgileri" sekmesinde farenin sağ tuşu ile ekrana gelen [Satış Faturasında Kullanılan Özel Tuş](/pages/createpage.action?spaceKey=N3ENTKD&title=Kullan%C4%B1lan+%C3%96zel+Tu%C5%9Flar&linkCreation=true&fromPageId=22805763)seçeneklerinde “Grup Koşullarını Çalıştır” bulunur.

![](../../../../_assets/dbc8ec6a33459c74a2fc.png)

Bu seçenekle kalem bilgilerinde girilen stok miktarlarına göre hangi gruptan ne kadar mal fazlası verileceği, açılan "Koşul Grup İşlemleri" ekranından izlenir.

![](../../../../_assets/e971c2ea51384ce6f961.png)

Yukarıdaki örnekte **001, 002 ve 003** stokları makarna grubuna (G01) dahildir. Ve grup kodları G01’dir. "Detay Koşul Kayıtları" bölümünde bu gruptan 10 tane alana 1, 20 tane alana da 2 adet G02 (makarna sosları) grubuna dahil stoklardan mal fazlası verileceği tanımlanır. Bu üç stok için faturada girilen toplam miktar 80’dir. Dolayısıyla mal fazlası olarak G02 grubundaki stoklardan 8 adet verilir.

**007** stoku ise, 2.5 litrelik içecekler grubundadır (G03). Bu gruptan da 4 tane alana 1, 8 tane alana 2 adet G04 grubundan (330 cL’lik içecek) mal fazlası verilmesi şeklinde tanımlama yapılır. Böylece 007 stoku için G04 grubundaki stoklardan 2 adet mal fazlası verilir.

Mal fazlası olarak girilecek stoklar "Koşul Grup İşlemleri" bölümünde listelendikten sonra, ilgili gruptan hangi stok verilecekse o stok kodu üzerinde çift tıklandığında, "Stok Kodu" alanına seçilen stok aktarılır. Kullanıcı bu aşamadan sonra mal fazlası miktarını elle (Manuel) girmesi gerekir. "Koşul Grup İşlemleri" şeffaf bir ekran olduğu için, mal fazlası miktar girişi esnasında kapatılmasına gerek yoktur.

Mal fazlası kalemleri girildikten sonra, "Koşul Grup İşlemleri" ekranının "Mal Fazlası Detay Bilgileri" sekmesinde, belgede girilen mal fazlası stoklarının neler olduğu, girilen mal fazlası miktarları ve hangi koşul koduna bağlı olarak girildiği izlenebilir.

**Aralıklı İskonto Hesaplamasında “Grup Koşul” Desteği**

"Detay Koşul Kayıtları" ekranının "Detay Koşul Bilgileri-2" sekmesinde aralıklı iskonto tanımlaması yapıldığı durumlarda aynı koşulun geçerli olduğu birden fazla kalemin toplam tutar ya da miktar bazında iskonto yapılması grup koşul desteği ile mümkündür.

**Örneğin:**

G01 (makarna) grubu için tanımlanan iskonto aralığının aşağıdaki gibi olduğu varsayıldığında "Miktar" alanına 10-20 arasında bir değer girildiğinde %5, 20-30 arasında bir değer girildiğinde %6, 30 ve üzeri bir değer girildiğinde ise %30 satır iskontosu yapılır.

![](../../../../_assets/7b139ec623613ec6f8f3.png)

"Miktar" alanına 10-20 arasında bir değer girildiğinde %5, 20-30 arasında bir değer girildiğinde %6, 30 ve üzeri bir değer girildiğinde ise %30 satır iskontosu yapılır.

Fatura belgelerinde girilen toplam miktarın kontrol edilmesi için, "Detay Koşul Kaydı" ekranındaki “Grup Koşul” seçeneğinin mutlaka işaretli olması gerekir.

Yukarıdaki örnek kalem bazında incelendiğinde; 001 stoku için %5, 002 stoku için %6 ve 003 stoku için de %0 iskonto yapılması gerekirdi. Ancak bu belgede grup koşul kullanıldığı için ve bu stokların hepsi de makarna grubuna dahil olduğu için, satır iskontosu oranı bulunurken tüm stokların toplam miktarına bakılmış ve bu miktara karşılık gelen satır iskontosu uygulanmıştır. Girilen kalemlerin toplam miktarı 32 olduğu için, iskonto oranı olarak 7 değeri ekrana getirilir.

İskonto oranın hesaplanarak iskonto alanına getirilmesi için, "Koşul Grup İşlemleri" ekranının Mal Fazlası/İskonto sekmesinde bulunan "**İskontoları Getir"** butonu kullanılır. Belgede bulunması gereken tüm kalemler girildikten sonra "İskontoları Getir" butonuna basıldığında, uygun satır iskonto oranları, koşulda belirtilen iskonto oranı alanına program tarafından otomatik olarak getirilir. Bu işlem sırasında stoklar için geçerli birden fazla koşul detay kaydı olduğunda getirilecek iskonto oranlarının ne şekilde belirleneceği, yukarıda anlatılan “**Çakışan Grup Koşullarda Aralık İskonto Politikası**” parametresinde belirlenir.
