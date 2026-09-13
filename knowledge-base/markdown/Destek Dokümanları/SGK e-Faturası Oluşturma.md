---
title: "SGK e-Faturası Oluşturma"
page_id: ""
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "SGK e-Faturası Oluşturma"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / SGK e-Faturası Oluşturma"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWIyZWY0NWUwLTMwZmUtNDI1Mi1hN2QyLTZiOGYzYzdmOWZmNCZsaW5rPThiNmUxOGI1LWM4ODMtNGExYy1iZTNmLTRjN2Y3MjZhYWYyMyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=b2ef45e0-30fe-4252-a7d2-6b8f3c7f9ff4&link=8b6e18b5-c883-4a1c-be3f-4c7f726aaf23&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "sgk-e-faturasi-olusturma.html"
source_version: ""
source_bytes: 42729
fetched_at: "2026-09-13T04:22:14+00:00"
generator: "netsis-scraper 1.0.0"
---
# SGK e-Faturası Oluşturma

Sosyal Güvenlik Kurumu 01 Ekim 2017 tarihinden itibaren elektronik fatura (e-Fatura) uygulamasına dahil olmuştur. Elektronik fatura uygulamasına kayıtlı sağlık hizmet sunucuları ve diğer mükelleflerin söz konusu tarihten itibaren Kuruma düzenleyecekleri faturaları, e-Fatura olarak göndermeleri gerekmektedir. Sağlık sunucuların, mükelleflerin gönderdiği e-Faturaları GİB üzerinden alır, kontrol eder, işler ve kayıt altına alınır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/a5643f80-19fd-4c89-b82c-a6282c30cbd3/sgk1.png)

SGK e-Faturalarında **Mükellef Kodu, Mükellef Adı, Dosya Numarası, Fatura Dönemi ve İlave Fatura Tipi** bilgilerinin bulunması zorunludur.

**Mükellef Kodu (MUKELLEF_KODU)**

Sağlık Hizmeti Sunucusunun kurumda tanımlı kodudur.

Mükellef Kodu bilgisinin XML ve e-Fatura görüntüsünde çıkması için, aşağıdaki 4 e-Devlet XML taglerinin tanımlı olması ve değerleri ile eşleştirilmiş olması gerekmektedir.

AdditionalDocumentReference.ID

AdditionalDocumentReference.IssueDate

AdditionalDocumentReference.DocumentTypeCode

AdditionalDocumentReference. DocumentType

Mükellef Kodunun basılması için aşağıdaki gibi tanımlamaların yapılması gerekmektedir.

Bu 4 AdditionaDocumentReference tagleri Mükellef Adı ve Dosya Numarası alanlarının basımında da kullanılacağı için, her alanın basımını birbirinden ayırmak için dizaynda **Kayıt No** alanı kullanılır. Bu örnekte Mükellef Kodunun basımı için Kayıt No alanlarına 1 girilmiştir.

AdditionalDocumentReference.ID ve AdditionalDocumentReference.DocumentTypeCode taglerine karşılık gelen değerler için Tip olarak Başlık seçilip değer alanına MUKELLEF_KODU yazılmıştır.

AdditionalDocumentReference.IssueDate tagine karşılık gelen tarih bilgisi, bu örnekte olduğu gibi ister sabit bir değer girilebilir, ister sql desteği ile tarih bilgisi getirilebilir, ister dizayn alanlarından tarih bilgisi basan bir alan seçilebilir.

Mükellef Kodunun hangi alandan getirileceği ise, dizayn alan numaraları kullanılarak ya da dizaynda sql desteği ile yapılabilir. Bu örnekte Mükellef Kodu Fatura Üst Bilgileri Açıklama 1 alanından (dizayn alan no: 1103) getirilmiştir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/4d9c5ab4-87a8-49d9-b63b-7d1ed68900e8/MK1.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/69faa1b6-bdde-4a08-8054-0ee3e33b5f1a/MK2.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/2acd3daa-a882-48b4-851e-30574692e541/MK3.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/0d31b497-d3ad-45c3-b342-a1ee14ca956a/MK4.png)

**Mükellef Adı (MUKELLEF_ADI)**

Sağlık Hizmeti Sunucusunun kurumda tanımlı adıdır.

Mükellef Adı bilgisinin XML ve e-Fatura görüntüsünde çıkması için, Mükellef Kodu alanında olduğu gibi aşağıdaki 4 e-Devlet XML taglerinin tanımlı olması ve değerleri ile eşleştirilmiş olması gerekmektedir.

AdditionalDocumentReference.ID

AdditionalDocumentReference.IssueDate

AdditionalDocumentReference.DocumentTypeCode

AdditionalDocumentReference. DocumentType

Mükellef Adının basılması için aşağıdaki gibi tanımlamaların yapılması gerekmektedir.

Bu 4 AdditionalDocumentReference tagleri Mükellef Kodu ve Dosya Numarası alanlarının basımında da kullanılacağı için, her alanın basımını birbirinden ayırmak için dizaynda **Kayıt No** alanı kullanılır. Bu örnekte Mükellef Adının basımı için Kayıt No alanlarına 2 girilmiştir.

AdditionalDocumentReference.ID ve AdditionalDocumentReference.DocumentTypeCode taglerine karşılık gelen değerler için Tip olarak Başlık seçilip değer alanına MUKELLEF_ADI yazılmıştır.

AdditionalDocumentReference.IssueDate tagine karşılık gelen tarih bilgisi, bu örnekte olduğu gibi ister sabit bir değer girilebilir, ister sql desteği ile tarih bilgisi getirilebilir, ister dizayn alanlarından tarih bilgisi basan bir alan seçilebilir.

Mükellef Adının hangi alandan getirileceği ise, dizayn alan numaraları kullanılarak ya da dizaynda sql desteği ile yapılabilir. Bu örnekte Mükellef Adı Fatura Üst Bilgileri Açıklama 2 alanından (dizayn alan no: 1104) getirilmiştir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/763eb7af-8137-4818-b431-7877cfb78c6a/MA1.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/f0a9315c-1e7f-4c1a-a98c-6d4c76c15ce6/MA2.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/3040ee5f-cb8c-42fd-81b7-146147e64d38/MA3.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/fd52a36a-0104-4dcb-b6a7-c5dea08bd1e8/MA4.png)

**Dosya Numarası (DOSYA_NO)**

Dosya No bilgisi girilir.

Dosya No bilgisinin XML ve e-Fatura görüntüsünde çıkması için, Mükellef Kodu alanında olduğu gibi aşağıdaki 4 e-Devlet XML taglerinin tanımlı olması ve değerleri ile eşleştirilmiş olması gerekmektedir.

AdditionalDocumentReference.ID

AdditionalDocumentReference.IssueDate

AdditionalDocumentReference.DocumentTypeCode

AdditionalDocumentReference. DocumentType

Dosya No bilgisinin basılması için aşağıdaki gibi tanımlamaların yapılması gerekmektedir.

Bu 4 AdditionalDocumentReference tagleri Mükellef Kodu ve Mükellef Adı alanlarının basımında da kullanılacağı için, her alanın basımını birbirinden ayırmak için dizaynda **Kayıt No** alanı kullanılır. Bu örnekte Dosya No bilgisinin basımı için Kayıt No alanlarına 3 girilmiştir.

AdditionalDocumentReference.ID ve AdditionalDocumentReference.DocumentTypeCode taglerine karşılık gelen değerler için Tip olarak Başlık seçilip değer alanına DOSYA_NO yazılmıştır.

AdditionalDocumentReference.IssueDate tagine karşılık gelen Tarih bilgisi, bu örnekte olduğu gibi ister sabit bir değer girilebilir, ister sql desteği ile tarih Bilgisi getirilebilir, ister dizayn alanlarından Tarih Bilgisi basan bir alan seçilebilir.

Dosya No bilgisinin hangi alandan getirileceği ise, dizayn alan numaraları kullanılarak ya da dizaynda sql desteği ile yapılabilir. Bu örnekte mükellef kodu Fatura Üst Bilgileri Açıklama 3 alanından (dizayn alan no: 1105) getirilmiştir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/770ea2fd-de42-45d4-8b31-ddf31dcf056b/DN1.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/97fb81e0-975c-4686-b6f7-5f6436607888/DN2.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/bfdc59fb-4db8-4cd9-af38-fc01e52a9814/DN3.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/0a751908-4be6-40f5-9464-007fe073a80b/DN4.png)

**Fatura Dönemi**

Fatura Dönem Bilgisi oluşan faturanın hangi döneme ait olduğu bilgisini içerir.

Fatura Dönemi bilgisinin XML ve e-Fatura görüntüsünde çıkması için, InvoicePeriod-StartDate ve InvoicePeriod-EndDate tagleri kullanılır.

Örnekte Fatura Dönem Başlangıç Tarihi, Fatura Üst Bilgileri Açıklama 4 (dizayn alan no: 1106) alanından, Fatura Dönem Bitiş Tarihi, Fatura Üst Bilgileri Açıklama 5 (dizayn alan no: 1107) alanından getirilmiştir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/d9314926-7aed-414b-bcd4-7d72e87b2d32/FT1.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/b83a058d-791b-465b-b8d5-673103eaa37c/FT2.png)

**İlave Fatura Tipi**

Faturanın hangi sağlık hizmet sunucusundan geldiğini belirtir. **SAGLIK_ECZ, SAGLIK_HAS, SAGLIK_OPT, SAGLIK_MED, ABONELIK, MAL_HIZMET** ve **DIGER** değerlerinden birini alır.

**1-Sağlık Hizmeti Sunucusu Faturaları:** Sosyal Güvenlik Kurumu ile Sağlık Hizmet Sunucusu kapsamında sözleşme imzalayan mükelleflerden gelecek faturalar; Eczane, Hastane, Optik ve Medikal’ dir.

**2-Abonelik İşletmelerine Ait Faturalar:** Kurumun tanımlı bulunan ve kullandığı abonelik işletmelerine ait faturalar; elektrik, doğalgaz, telefon, internet, su, tv, vb dir.

**3-Mal/Hizmet Alımı Kapsamında Gelen Faturalar:** Kurum ihale/doğrudan temin sonucunda mal hizmet alımı yaptığı firmalardan gelen faturalar; SGK ile ihale kapsamında verdikleri mal/hizmete ait mükelleflerin faturalarıdır.

**4-Diğer Gelen Faturalar**: Kurum ile sözleşmesi olmayan, mal hizmet alımı yapmadığı tek seferlik faturalar diğer grubunda yer alacaktır. Yukardaki kapsamlar dışında kalan diğer faturalar

İlave Fatura Tipi bilgisinin XML ve e-Fatura görüntüsünde çıkması için, AccountingCost tagi kullanılır. Örnekte İlave Fatura Tipi bilgisi, Fatura Üst Bilgileri Açıklama 6 (dizayn alan no: 1108) alanından getirilmiştir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/44d42256-fd41-4adb-99d3-7f35bf022015/IF1.png)

Xslt içerisinde aşağıdaki kod bloğunun da olması gerekir.

\<xsl:for-each select="//n1:Invoice/cac:AdditionalDocumentReference"\>

```text
        <tr >
```

```text
            <xsl:if test="cbc:ID = 'MUKELLEF_KODU'">
```

```text
            <td> <b>MUKELLEF KODU: </b></td>
```

```text
            <td> <xsl:value-of select="cbc:DocumentType"/> </td>
```

```text
            </xsl:if>
```

```text
            <xsl:if test="cbc:ID = 'MUKELLEF_ADI'">
```

```text
              <td> <b>MUKELLEF ADI: </b></td>
```

```text
              <td> <xsl:value-of select="cbc:DocumentType"/><br/></td>
```

```text
            </xsl:if>
```

```text
            <xsl:if test="cbc:ID = 'DOSYA_NO'">
```

```text
              <td> <b>DOSYA NO: </b></td>
```

```text
              <td> <xsl:value-of select="cbc:DocumentType"/><br/></td>
```

```text
            </xsl:if>
```

```text
        </tr>
```

```text
      </xsl:for-each>
```

```text
      <tr>
```

```text
          <td class="invoiceDetailColor"><b>Fatura Dönemi:</b></td>
```

```text
      <td>
```

```text
      <xsl:for-each select="//n1:Invoice/cac:InvoicePeriod/cbc:StartDate">
```

```text
       <xsl:value-of select="substring(.,9,2)"/>.<xsl:value-of select="substring(.,6,2)"/>.<xsl:value-of select="substring(.,1,4)"/>
```

```text
       </xsl:for-each>
```

```text
       <xsl:text>-</xsl:text>
```

```text
       <xsl:for-each select="//n1:Invoice/cac:InvoicePeriod/cbc:EndDate">
```

```text
       <xsl:value-of select="substring(.,9,2)"/>.<xsl:value-of select="substring(.,6,2)"/>.<xsl:value-of select="substring(.,1,4)"/>
```

```text
       </xsl:for-each>
```

```text
       </td>
```

```text
        </tr>
```

```text
       <tr>
```

```text
           <td><b>Sağlık Fatura Tipi:</b></td>
```

```text
      <td>
```

```text
      <xsl:for-each select="n1:Invoice//cbc:AccountingCost">
```

```text
       <xsl:apply-templates/>
```

\</xsl:for-each\>

```text
       </td>
```

```text
        </tr>
```

Ilave fatura tiplerine göre doldurulması zorunlu alan bilgileri aşağıdaki tabloda yer almaktadır.

Örneğin, ilave fatura tipi: SAGLIK_ECZ ise; mükellef kodu, mükellef adı, dosya no alanları dolu olmalıdır. İlave fatura tipi: MAL_HIZMET ise; sadece dosya no alanının dolu olması yeterlidir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/eb78365a-4ff2-4d10-b582-bfc30ef99fde/SGK2.png)

Fatura girişinde aşağıdaki gibi dizaynda belirtilen alanlar, girilmesi zorunlu bilgilerle doldurulur.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/4d2c7266-ce21-436b-9949-d40f5bc8ec1b/FAT1.png)

Taslak sonrası oluşan SGK e-Faturasının görüntüsü aşağıdaki gibidir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/6c5e4fef-cd8f-43b2-9760-d63d7323a440/taslak.png)

SGK e-Faturası örnek dizayn için [tıklayınız](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/5e248479-4522-4871-9ecb-3c7b5d4871ae/SGKGENEL.rar)
