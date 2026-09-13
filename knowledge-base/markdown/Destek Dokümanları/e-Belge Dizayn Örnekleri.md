---
title: "e-Belge Dizayn Örnekleri"
page_id: "66224396"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "e-Belge Dizayn Örnekleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / e-Belge Dizayn Örnekleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPThlYmM3YmNjLWY5YTctNGNjOC04OWNkLTZlNTc3MjlkOWI1NSZsaW5rPThiZDA4YTg4LTE4ZDEtNGJiYS1hNjdhLTFkM2M3YjE5MmJhYSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=8ebc7bcc-f9a7-4cc8-89cd-6e57729d9b55&link=8bd08a88-18d1-4bba-a67a-1d3c7b192baa&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "e-belge-dizayn-ornekleri_80090204_66224396.html"
source_version: "2022-11-02T16:06:26.843+03:00"
source_bytes: 9557638
fetched_at: "2026-09-13T04:25:15+00:00"
generator: "netsis-scraper 1.0.0"
---
# e-Belge Dizayn Örnekleri

e-Belge Dizayn Örnekleri ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

#### Satış Faturasının üst bilgilerinde Açıklama-1 ve Açıklama-2 alanlarına girilen bilgilerin e-Fatura belgesinde basılması (Invoice Notes)

Satış faturasının üst bilgilerinde Açıklama1 ve Açıklama2 alanlarına girilen bilgilerin e-Fatura belgesinin alt kısmında notlar bölümünde basılması istendiğinde, öncelikle e-Fatura dizaynı içerisinde İnvoice Notes tagi ile eşlenecek olan bilgiler; ister sql desteği, ister alan numarası seçilerek kaydedilir.
![](../_assets/9f6b894f25497831781c.png)
Örneğe göre, Açıklama-1 alanı için:

Yer: Üst

Tip: Program

Açıklama-1 için "1103" numaralı alan

e-Devlet Xml Tag: Invoice Notes seçilerek satır, sütun ve uzunluk bilgileri girilerek kaydedilir.

Benzer şekilde Açıklama-2 alanı için:

Yer: Üst,

Tip: Program

Açıklama-2 için "1104" numaralı alan

e-Devlet Xml Tag: Invoice Notes seçilerek satır, sütun ve uzunluk bilgileri girilerek kaydedilir.
![](../_assets/72917cc874b455c9c9cd.png)
![](../_assets/881d49b34828a0a0d291.png)

Basılmak istenen açıklama bilgileri e-Belgenin notlar kısmında basılacağı için Xslt dosyası içerisinde herhangi bir düzenleme yapmaya gerek yoktur. Bu tanımlamalardan sonra Toplu e-Fatura Oluşturma işlemiyle taslak oluşturulduğunda aşağıdaki e-Belge görüntüsünde notlar kısmında açıklamaların basıldığı görülmektedir.

![](../_assets/23289eb624170a33eaa9.png)

#### Fatura belgesinin üst bilgiler kısmına cari kodu bilgisinin basılması (Invoice Notes)

Satış faturasının cari kodu bilgisinin e-Fatura belgesinin üst kısmında basılması istendiğinde, öncelikle e-Fatura dizaynı içerisinde İnvoice Notes tagi ile eşlenecek olan cari kodu bilgisi için; ister sql desteği, ister alan numarası seçilerek kaydedilir.
![](../_assets/9f6b894f25497831781c.png)

Örneğe göre, Cari Kodu alanı için:

Yer: Üst

Tip: Sql, Sql cümlesi için **'X'+ VT_Karekter({1002})** ve e-Devlet Xml Tag: Invoice Notes seçilerek satır, sütun ve uzunluk bilgileri girilerek kaydedilir.

Bu sql cümlesinde "X" ifadesi + cari kodu alanı için "1002" numaralı alan numarası seçilmiştir.
Dizaynda gönderilen değerin başına X yazıldığı için xslt içinde de bunu belirterek gerekli düzenleme yapılmalıdır.
X, Y, Z, vb ifadeler kullanmadaki amaç, xslt içinde basılmak istenen yere, içinde bu ifade geçen Invoice Notes tagi ile getirilen bilginin basılabilmesi içindir.
![](../_assets/9b7cce76cdb23b23b8f1.png)

Xslt içerisinde cari kodunu SAYIN yazısının altına basılması istendiğinde, SAYIN yazısı seçilerek hızlıca kod bloğunun yazılacağı yere gelinir ve aşağıdaki kod bloğu yazılır. Bu kod bloğunda **\<xsl:text\>** tagleri arasına başlık bilgisi ve sonrasında "**X**" içeren Invoice Notes tagindeki bilginin basımı için "**contains**" ifadesi kullanılır. Bu basılacak bilgide 2. karakterden itibaren başlaması için (ilk karakter "X") "**substring**" komutu kullanılarak 2 den başlayıp, sonuna kadar basılması sağlanır.

**\<xsl:text\>Cari** **Kodu:**

\<xsl:for-each select="\*/cbc:Note"\>

**\<xsl:if\< strong=""\> **test="contains(.,'X')"\>****

\<xsl:value-of select="substring(.,2,string-length(.))"\>

![](../_assets/52b98aad39009f8d2073.png)

Cari kodu bilgisi Invoice Notes sahasına gönderilip, üst bilgilere cari kodunun basılması sağlandıktan sonra, aynı zamanda e-Belgenin notlar kısmında da çıkmaması için xsltde alt notların basıldığı yerde aşağıdaki gibi bir düzenleme yapılmalıdır.

\<xsl:for-each select="//n1:Invoice/cbc:Note"\>

\<xsl:if test="not(contains(.,'X'))"\>

```text
      Not: <xsl:value-of select=".">
```

Invoice Notes sahasında "X" ile başlayan bilgiyi fatura notları kısmında basmaması için **\<xsl:if\< strong=""\> **test="not(contains(.,'X'))"** ifadesi kullanılmalıdır. Basılması istenen yerde "contains" ifadesi, basılması istenmeyen yerde ise "not contains" ifadesi kullanılmalıdır.**

Bu tanımlamalardan sonra Toplu e-Fatura Oluşturma işlemiyle taslak oluşturulduğunda e- Belge görüntüsünde üst bilgilerde cari kodunun basıldığı görülmektedir.

![](../_assets/23289eb624170a33eaa9.png)

#### Migros, Amazon, Carrefour, Bim, vb firmalara kesilen e-Faturalar üzerinde olması gereken Malveren numarası, satıcı teslim noktası vb alıcı-satıcı bilgilerin basılması için kullanılan PartyIdentitication/ID elemanının ShemaID özelliği olan MUSTERINO ve BAYINO değerlerinin basılması (Customer.PartyIdentificationId, Customer.PartyIdentificationValue)

e-Fatura belgesinde müşteri tarafı için, MUSTERINO, BAYINO ve değerleri için e-Belge dizaynı içinde Customer-PartyIdentificatonId ve Customer-PartyIdentificatonValue taglerinin olması gerekmektedir.

e-Fatura dizaynı içerisinde Customer-PartyIdentificatonId tagi ile eşlenecek olan BAYINO değeri için:

Yer: Üst

Tip:Başlık seçilerek başlık olarak BAYINO yazılır ve e-Devlet Xml Tag: Customer- PartyIdentificatonId seçilerek kaydedilir. Customer- PartyIdentificatonId tagi ile eşlenecek kayıt tanımından sonra PartyIdentificatonValue tagi ile eşlenecek olan bilgi ister sql desteği ile ister alan numarası seçilerek kaydedilir. Örneğe göre sql seçilip sabit bir değer girilir.

![](../_assets/33a23f9467b57b8208df.png)![](../_assets/88d16575baec0ad5aa12.png)

Aynı dizayn içinde Customer-PartyIdentificatonId ve Customer-PartyIdentificationValue tagleri için yeni tanımlamalar yapılacaksa çakışma olmaması için Kayıt No alanına önceki tanımlarda kayıt no alanına girilen değerlerden farklı bir değer girilmelidir.

Buna göre Customer-PartyIdentificatonId tagi ile eşlenecek olan MUSTERINO değeri için, yer:Üst, tip:Başlık seçilerek başlık olarak MUSTERINO yazılır, e-Devlet Xml Tag: Customer- PartyIdentificatonId seçilir ve Kayıt no alanına "1" değeri girilerek kaydedilir.

PartyIdentificatonValue tagi ile eşlenecek olan bilgi ister sql desteği ile ister alan numarası seçilerek kaydedilir. Örneğe göre sql seçilip sabit bir değer girilir.

![](../_assets/10b4a46401d67cfff3d6.png)![](../_assets/7dcfa02b62db9b8e2d27.png)

Dizaynda seçilen xlst dosyasında herhangi bir düzenleme yapmaya gerek yoktur. Çünkü xslt içinde bu tag bilgileri tanımlıdır.

Bu tanımlamalardan sonra Toplu e-Fatura Oluşturma işlemiyle taslak oluşturulduğunda e- Belge görüntüsünde müşteri kısmında BAYINO ve MUSTERINO bilgilerinin basıldığı görülmektedir.

#### ![](../_assets/23289eb624170a33eaa9.png)
e-Fatura basımında sipariş numarasının istenilen karakter uzunluğunda basılabilmesi (Order- OrderRererenceId, Order-OrderIssueDate)

Aşağıda sipariş bağlantılı girilen satış faturasına bağlı sipariş numarası 000000000111296'dır.
![](../_assets/8bdef5a9a4fea9a812e7.png)

Bu sipariş numarasının sağdan 6 karakteri olan 111296 bilgisinin basılması için elge dizaynının içerisinde Order-OrderRererenceId ve Order-OrderIssueDate taglerinin olması gerekmektedir.

Örneğe göre, Sipariş numarasının sağdan 6 karakter olarak basımı için:

Yer: Üst,

Tip: Sql

Sql cümlesi için **RIGHT(** **VT_Karekter({4127}),6)** ve e-Devlet Xml Tag: Order-OrderreferenceId seçilerek satır, sütun ve uzunluk bilgileri girilerek kaydedilir. Bu sql cümlesinde RIGHT komutu kullanılarak sipariş numarasına karşılık gelen alan numarası seçilir ve sağdan 6 karakter olduğu için "6" yazılır.

Bu tag ile eşleşecek olan kayıt bu örnekte olduğu gibi sql desteği ile ya da alan numarası seçilerek farklı şekillerde de tanımlanabilir.

![](../_assets/f15c87d28e79af77395d.png)
Sipariş tarihi bilgisinin basımı için:

Yer: Üst

Tip: Program "1003" numaralı alan

e-Devlet Xml Tag: Order-OrderReferenceIssueId tagi seçilerek satır, sütun ve uzunluk bilgileri girilerek kaydedilir.

Dizaynda seçilen xslt dosyasında herhangi bir düzenleme yapmaya gerek yoktur. Mevcut tanımlı olan kod kullanılır. Bu tanımlamalardan sonra Toplu e-Fatura Oluşturma işlemiyle taslak oluşturulduğunda e- Belge görüntüsünde sipariş numarasının sağdan 6 karakteri olan 111296 olarak basıldığı görülür.

![](../_assets/061aafa01a7032c59097.png)

#### Satış faturasının üst bilgilerinde Açıklama 3 alanına girilen irsaliye numarasının e-Fatura belgesinde basılması (InvoiceLine-DespatchId, InvoiceLine-DespatchIssueDate)

Satış faturasına bağlı irsaliye numarasının basılması durumunda, dizayn içinde veya xslt dosyası üzerinde herhangi bir düzenleme yapmaya gerek yoktur. Faturanın bağlı olduğu irsaliye numarası taslak sonrası e-Belge üzerine basılacaktır.

Farklı bir alana girilen irsaliye bilgisinin basılabilmesi durumunda, aşağıda satış faturasının üst bilgilerinde Açıklama 3 alanına girilen irsaliye numarasının basılması için ve farklı bir alana girilen irsaliye bilgisinin basılabilmesi için gerekenler aşağıdaki şekildedir:

![](../_assets/9f6b894f25497831781c.png)

-
  -
    - Önceliklee-FaturadizaynındaiçerisindeInvoiceLine-DespatchIdveInvoiceLine-DespatchIssueDate taglerinin olması gerekmektedir.
    - Dizayn içerisinde InvoiceLine-DespatchId tagi ile eşlenecek olan tanım ister sql desteği ile ister alan numarası seçilerek farklı şekillerde tanımlanabilir.
    - Bu örnekte yer: Kalem, Tip: Program seçilip Açıklama3 alanı için "1105" numaralı alan seçilir ve e-Devlet XML Tag: InvoiceLine-DespatchId seçilerek kaydedilir.
    - InvoiceLine-DespatchIssueDate tagi ile eşlenecek irsaliye tarihi bilgisi ister sql desteği ile ister alan numarası seçilerek kaydedilir. Örneğe göre tip: Program seçilip "4143" numaralı alan seçilmiştir.

![](../_assets/c345058e549b9d827e72.png)
![](../_assets/b09d63465b2d7b63ba00.png)

- Dizaynda seçilen xslt dosyasında herhangi bir düzenleme yapmaya gerek yoktur.Mevcut tanımlı olan kod kullanılır.
- Bu tanımlamalardan sonra toplu e-fatura oluşturma ile taslak oluşturulduğunda e-Belge görüntüsünde Açıklama 3 alanına girilen irsaliye numarasının basıldığı görülür.

![](../_assets/061aafa01a7032c59097.png)

#### Satış faturasının kalem bilgilerinde girilen ek alan ve stok grup kodu bilgilerinin e-Fatura belgesinde basılması (InvoiceLine-BuyersItemIdentification, InvoiceLine- SellersItemIdentification)

e-Belge üzerinde stok kalemleri kısmında bir bilginin basılması için; InvoiceLine- BuyersItemIdentification, InvoiceLine- SellersItemIdentification, InvoiceLine- ManufacturerItemIdentification, InvoiceLine-Notes, InvoiceLine-Name, InvoiceLine-

ModelName, InvoiceLine- BrandName, InvoiceLine- Description, vb e-Devlet Xml tagleri kullanılarak basım yapılır. Stok kalemleri için hangi tag kullanılmıyorsa o tagler kullanılarak kalemlere istenilen bilgilerin basılması sağlanır.

Örneğe göre satış faturasında yer alan kalemler için, satırda girilen ek alan bilgisi InvoiceLine-BuyersItemIdentification tagi, stokların stok kartlarındaki grup kod bilgisinin de InvoiceLine- SellersItemIdentification tagleri kullanılarak basılacağı düşünüldüğünde, Ek Alan bilgisi için yer: Kalem, Tip: Sql seçilerek, sql cümlesi için **EKALAN FROM TBLSTHAR** **WHERE** **STHAR_FTIRSIP='1'** **AND** **FISNO=** **VT_Karekter({1001})** **AND** **STOK_KODU=** **VT_Karekter({4000})** **AND** **INCKEYNO=** **VT_Sayisal({4510})** ve e-Devlet XML Tag: InvoiceLine- BuyersItemIdentification seçilerek satır, sütun ve uzunluk bilgileri girilerek kaydedilir. Sql cümlesinde TBLSTHAR tablosundan EKALAN bilgisi seçilir ve kısıt olarak da satış faturası tipi, fisno, stok kodu ve belgede aynı stok kodu girişi olabileceği için inckeyno kısıtları verilir.

![](../_assets/6513fab897c54442bf04.png)![](../_assets/ca080768bc298619dcef.png)

![](../_assets/42ff550733aea3ce0258.png)

Stok Grup Kodu bilgisi için yer: Kalem, Tip: Program seçilerek stokların grup kodları için "4003" numaralı alan seçilir ve ve e-Devlet XML Tag: InvoiceLine- SellersItemIdentification seçilerek satır, sütun ve uzunluk bilgileri girilerek kaydedilir.

![](../_assets/a4dd0512bcbbc9fbeeb3.png)

Dizaynda tanımlanan bilgilerin stok kalemlerinde kolonlar halinde basılabilmesi için bazı düzenlemelerin yapılması gerekmektedir.

Xslt dosyasında ilk olarak ek alan ve stok grup kodu bilgilerinin basılacağı kolonların başlık bilgilerinin tanımlanması gerekir.

Mal Hizmet kolonunun sağ yanına "Ek Alan" ve "Grup Kodu" kolon başlıklarını eklemek için Mal Hizmet veya SıraNo yazısı seçilerek hızlı bir şekilde sağ taraftaki Kolon başlıklarının eklendiği kısıma gelinir ve aşağıdaki kod blokları eklenir.

****style="font-weight:bold;"\>****

\<xsl:text\>Ek Alan

****class="lineTableTd"** **style="width:20%"** **align="center"\>****

**\<xsl:text\>Grup** **Kodu**

Başlık bilgisi eklendikten sonra bu kolonlara bilginin hangi tagden geldiğini belirtmek gerekiyor. Bunun için xslt içinde kolonların hangi taglerden geldiğinin belirtildiği kısıma gelinir ve ekAlan bilgisinin InvoiceLine-BuyersItemIdentification taginden ve grup kodu bilgisinin de InvoiceLine-SellersItemIdentification taginden geldiği belirtilir.

Buna göre stok satırında ilgili kolonun hücresini belirtmek için belirteçleri yazıldıktan sonra sağ click\> **Xslt** **Tag** **Ekle** menüsü ile çıkan ekrandan fatura kalem bilgilerinde Ek Alan için BuyersItemIdentification, stok grup kodları için de SellersItemIdentification seçilip ekle denilerek xslt kod bloğu eklenmiş olur.
![](../_assets/8fa27b582d2efa4e1cb5.png)

**\<xsl:for-each\< strong=""\> **select="cac:Item/cac:BuyersItemIdentification/cbc:ID"\>****

\<xsl:value-of select="."\>

****class="lineTableTd"\>****

\<xsl:for-each select="cac:Item/cac:SellersItemIdentification/cbc:ID"\>

**\<xsl:value-of\< strong=""\> **select="."/\>****

Bu tanımlamalardan sonra toplu e-fatura oluşturma ile taslak oluşturulduğunda e-Belge görüntüsünde ekalan ve stok grup kodu bilgilerinin basıldığı görülür.![](../_assets/061aafa01a7032c59097.png)

#### Satış faturasının kalem bilgilerinde girilen satır iskontosu 1 ve satır iskontosu 2 bilgilerinin e- Fatura belgesinde basılması (InvoiceLine-Notes)

Satış faturasında yer alan kalemler için satırda girilen satır iskontosu1 ve satır iskontosu2 bilgilerinin basımı için InvoiceLine-Notes tagi kullanılarak basılmak istendiğinde, diğer bir deyişle dizayn içerisinde tek bir sql cümlesi ve tek bir e-Devlet Xml tagi kullanılarak e-Belge üzerinde stok kalemleri kısmında 2 farklı bilgi bastırılmak istendiğinde, Örnek için, yer: Kalem, tip: Sql seçilerek ekrandaki sql cümlesi olarak **'|\*1**|'\* **CAST(cast(STHAR_SATISK\*100000** **as** **decimal(15,2))** **AS** **VARCHAR(15))** **'|\*2**|'\* **CAST(cast(STHAR_SATISK2** **as** **decimal(15,2))** **AS** **VARCHAR(15))** **'|\*3**|'\* **FROM** **TBLSTHAR WHERE FISNO=VT_Karekter({1001}) AND STOK_KODU= VT_Karekter({4000})** **AND** **INCKEYNO=** **VT_Sayisal({4510})** ve e-Devlet Xml Tag: InvoiceLine- Note tagi seçilerek satır, sütun ve uzunluk bilgileri girilerek kaydedilir.

![](../_assets/5583d0a9a68313939b6f.png)
Cümleye baktığımızda bastırılmak istenen bilgilerin tabloda tutulduğu kolon bilgileri girilir ve bu kolonlar arasına \*|**rakam**|\* şeklinde ifadeler konarak sql cümlesi yazılır. Bu şekilde yazılmasının sebebi xslt dosyası üzerinde bu kolon bilgileri ilgili yerlere getirilirken Invoiceline-Note tagindeki **|3|** ile **|2|** arasındaki değeri al ilgili kolona bas, **|2|** ile **|1|** arasında kalan değeri al ilgili kolona bas diyebilmek içindir.

![](../_assets/523bee0f3b8feceb537d.png)
Bu eklenen bilgilerin stok kalemlerinde kolonlar halinde basılabilmesi için xslt dosyası üzerinde bazı düzenlemelerin yapılması gerekmektedir.

Xslt dosyasında ilk olarak satır iskontonsu1 ve satır iskontosu 2 bilgilerinin basılacağı kolon ve başlık bilgilerinin tanımlanması gerekir.

****style="font-weight:bold;"\>****

\<xsl:text\>Satır İsk1

****class="lineTableTd"** **style="width:9%"** **align="center"\>****

**\<xsl:text\>Satır** **İsk2**

Başlık bilgisi ve kolon eklendikten sonra bu kolonlara bilginin hangi tagden geldiğini belirtmek gerekiyor. Bunun için xslt içinde kolonların hangi tagden geldiğinin belirtildiği kısıma gelinir ve satır iskontosu1 ve 2 için InvoiceLine-Note tagi ve "**substring-before**" ve "**substring-after**" ifadeleri kullanılarak aşağıdaki kod blokları yazılır.

**\<xsl:text\>**

\<xsl:value-of select="substring-after(substring before(cbc:Note,'|&lt;strong&gt;2&lt;/strong&gt;|'),'|&lt;strong&gt;1&lt;/strong&gt;|')"\>

**\<xsl:text\>**

\<xsl:value-of select="substring-after(substring-before(cbc:Note,'|&lt;strong&gt;3&lt;/strong&gt;|'),'|&lt;strong&gt;2&lt;/strong&gt;|')"\>

'|**1**|' + CAST(cast(STHAR_SATISK\*100000 as decimal(15,2)) AS VARCHAR(15)) + '|**2**|' + CAST(cast(STHAR_SATISK2 as decimal(15,2)) AS VARCHAR(15)) + '|**3**|' FROM TBLSTHAR WHERE FISNO=VT_Karekter({1001}) AND STOK_KODU= VT_Karekter({4000}) AND INCKEYNO=**VT_Sayisal({4510})**

Satır iskontosu 1 basımı için şunlar yapılır:

- **Substring before(cbc:Note,'|\*2**|')\* komutu sql cümlesinde **'|\*2**|'\* ifadesinden öncesini belirtmektedir. Yani cümlede **'|\*1**|'\* + **CAST(cast(STHAR_SATISK\*100000** **as** **decimal(15,2))** **AS VARCHAR(15))** kısmı belirtilmektedir.
- **Substring-after(substring** **before(cbc:Note,'|\*2**|'),'|**1**|')\* komutu sql cümlesinde **'|\*1**|'\* ifadesindensonrasınıbelirtmektedir.Yani cümlede **CAST(cast(STHAR_SATISK\*100000** **as** **decimal(15,2))** **AS** **VARCHAR(15))** kısmı belirtilmektedir. Böylece satır iskontosu 1' in basımı sağlanmış olur.

Satır iskontosu 2 basımı için şunlar yapılır:

- **Substring before(cbc:Note,'|\*3**|')\* komutu sql cümlesinde **'|\*3**|'\* ifadesinden öncesini belirtmektedir. Yani cümlede **'|\*1**|'\* **CAST(cast(STHAR_SATISK\*100000** **as** **decimal(15,2)) AS VARCHAR(15))** **'|\*2**|'\* + **CAST (cast (STHAR_SATISK2 as decimal** **(15,2))** **AS** **VARCHAR(15))** kısmı belirtilmektedir.
- **Substring-after** **(substring** **before(cbc:Note,'|\*3**|'),'|**2**|')\* komutu sql cümlesinde **'|\*2**|'\* ifadesinden sonrasını belirtmektedir. Yani cümlede **CAST** **(cast** **(STHAR_SATISK2** **as** **decimal (15,2)) AS VARCHAR (15))** kısmı belirtilmektedir. Böylece satır iskontosu 2' nin basımı sağlanmış olur.
- Bu tanımlamalardan sonra toplu e-fatura oluşturma ile taslak oluşturulduğunda e-Belge görüntüsünde ekalan ve stok grup kodu bilgilerinin basıldığı görülür.

![](../_assets/061aafa01a7032c59097.png)

Fatura belgesine firma logosu eklenmesi aşağıdaki şekilde yapılır:

- Firma logosunun gelir idaresi logosu ve e-Fatura yazısının altına basılması istendiğinde, Xslt dosyasına firma logosunun basılması istenen yere gelindikten sonra sağ click \>Resim ekle diyerek ilgili jpeg uzantılı firma logosu eklenir. Sonrasında resmin genişliği ve sayfadaki hizalaması ayarlanır. Böylece firma logosu xslt dosyasına eklenmiş olur.
![](../_assets/90c4e5e7d6b1df781a61.png)
![](../_assets/e6f403270e40e23da7f5.png)

Fatura belgesine arka plan resmi ekleme aşağıdaki şekilde yapılır:

- e-Faturanın arka planında görünecek resmin internet üzerinden düzgün bir şekilde görüntülenebilmesi ve erişiminin olması gerekiyor.
- Xslt dosyası üzerinde body kısmına internetten erişiminin sağlandığı resmin adres bilgisi yazılır.

\<body background=[{+}](https://www.e-ptt.gov.tr/wp-content/uploads/2019/03/e-fatura-kutular-arkaplan.jpg)[https://www.e-ptt.gov.tr/wp-content/uploads/2019/03/e-+](https://www.e-ptt.gov.tr/wp-content/uploads/2019/03/e-+) [fatura-kutular-arkaplan.jpg](https://www.e-ptt.gov.tr/wp-content/uploads/2019/03/e-fatura-kutular-arkaplan.jpg)

- Dönüştür denildiğinde arka planın xslt dosyası üzerinde görünütülendiği görülmektedir.

![](../_assets/d8d405eded0485e114c2.png)
