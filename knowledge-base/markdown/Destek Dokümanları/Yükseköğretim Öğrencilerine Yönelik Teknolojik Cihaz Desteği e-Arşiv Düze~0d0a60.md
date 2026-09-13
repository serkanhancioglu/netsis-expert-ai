---
title: "Yükseköğretim Öğrencilerine Yönelik Teknolojik Cihaz Desteği e-Arşiv Düzenlemeleri"
page_id: ""
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Yükseköğretim Öğrencilerine Yönelik Teknolojik Cihaz Desteği e-Arşiv Düzenlemeleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Yükseköğretim Öğrencilerine Yönelik Teknolojik Cihaz Desteği e-Arşiv Düzenlemeleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTNjZmJmZjUxLTdlMmItNDNiOC1iN2U1LWMzYzY2YTU1YzdiNCZsaW5rPTIyNmRhNDQ3LWNiNmEtNDY4MC05NjM5LTQzYTZkMWRkMTZjOSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=3cfbff51-7e2b-43b8-b7e5-c3c66a55c7b4&link=226da447-cb6a-4680-9639-43a6d1dd16c9&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "yusekogretim-ogrencilerine-yonelik-teknolojik-cihaz-destegi-e-arsiv-duzenlemeleri.html"
source_version: ""
source_bytes: 11145
fetched_at: "2026-09-13T04:22:01+00:00"
generator: "netsis-scraper 1.0.0"
---
# Yükseköğretim Öğrencilerine Yönelik Teknolojik Cihaz Desteği e-Arşiv Düzenlemeleri

24.10.2023 tarihli ve 7734 sayılı Cumhurbaşkanı Kararı ile yürürlüğe konulan Yükseköğretim Öğrencilerine Teknolojik Cihaz ve İnternet Desteği Verilmesine ilişkin usul ve esaslar 14.11.2023 tarihli ve 32369 sayılı Resmi Gazete’ de yayımlanan “**Yükseköğretim Öğrencilerine Teknolojik Cihaz ve İnternet Desteği Verilmesine İlişkin Usul ve Esaslar Hakkında Tebliğ**” ile düzenlenmiştir.

Bu destek kapsamındaki e-Arşiv faturalarında UBL standartlarında yeni alanlar zorunlu hale getirilmiştir. Tebliğ 02.05.2025 tarihinde yürürlüğe girecektir. Gelir İdaresi’ nin yayınladığı klavuza ulaşmak için [tıklayınız](https://ebelge.gib.gov.tr/dosyalar/kilavuzlar/Teknoloji_Destek_e-Arsiv_Fatura_Teknik_Kilavuzu_V.1.0.pdf).

• Teknoloji Destek fatura tipi sadece e-Arşiv Faturaları için geçerlidir. e-Fatura belgelerinde bu fatura tipi kullanılmamaktadır .9.0.62.4 ve 9.0.63.1 versiyonlarıyla birlikte, Teknoloji Destek Fatura tipli e-Arşiv faturalarının düzenlenebilmesi sağlanmıştır.

• Teknolojik cihaz desteği kapsamında telefon veya bilgisayar/tablet satışlarında düzenlenecek e-Arşiv Faturalarında “**TEKNOLOJIDESTEK**” fatura tipi kullanılmaktadır.

• Teknolojik cihaz desteği olan e-Arşiv faturaları şahıslara düzenlenmektedir. Bu sebeple Cari Hesap Kartlarında, cariye ait TC Kimlik Numarasının girilmesi gerekmektedir.

Bu kapsamda, Toplu E-Arşiv Oluşturma ekranında İşlem Tipi Seçimi sekmesine "**Oluşacak Belge Teknoloji Destek Tipli Olsun**" adında bir parametre eklenmiştir. Bu parametre işaretlendiğinde ekranda “**TEKNOLOJIDESTEK tipli bir fatura oluşturabilmek için Netsis’ de zorunlu alanların yer aldığı bir dizayn oluşturduğunuzdan emin olunuz ve taslak oluştururken bu dizaynı kullanınız**” yazılı bir açıklama mesajı ekrana gelmektedir. Teknolojik cihaz desteği kapsamında e-Arşiv faturası düzenlenmesi durumunda bu parametre işaretlenerek taslak oluşturma işlemi yapılması gerekmektedir.

Ayrıca Teknoloji Destek tipli e-Arşiv faturası, kağıt veya e-Posta tipli e-Arşiv faturası olarak kesilebilir ya da İnternet e-Arşiv faturası olarak da düzenlenebilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/235559c4-bc48-43f0-9792-96a6dbe2adcc/yuksekogrenimresim1.png)

• Teknolojik destek kapsamında düzenlenecek e-Arşiv Faturalarının “InvoiceLine” alanı altında “Item/ AdditionalItemIdentification alanlarının telefon veya tablet/PC satışlarına göre e-Arşiv dizaynları içinde tanımlanması gerekmektedir.

**Telefon satışında;**

Telefona ait IMEI numaralarının basılması için aşağıdaki tanımlamaların dizayn içinde yapılması gerekemektedir.

Dizayn içinde Yer:“**Kalem**”, Tip:"**Başlık"**, e-Devlet XML Tag:“**InvoiceLine-AdditionalItemIdentification-schemeID**” seçilir. Başlık: “**TELEFON**” yazılarak, satır, sütun ve uzunluk bilgisi girilerek kaydedilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/0dee44bf-fc90-4449-b390-498c2af40ea2/yuksekogrenimresim2.png)

Diğer bir zorunlu tanımlama ise, telefona ait IMEI Numara bilgilerinin hangi alandan getirileceğinin belirtilmesidir. Telefon stoklarına ait IMEI bilgileri farklı alanlarda takip ediliyor olabilir.

Örneğin Seri Uygulaması kullanımı varsa, IMEI bilgileri seri bilgilerinden getirilebilir. IMEI bilgileri, Fatura kalemlerinde Satır Açıklama alanlarına girilmesi durumunda bu alanlardan bu bilgiler getirilebilir veya stok kartlarında herhangi bir alana IMEI numaraları tanımlanıyorsa bu alanlardan bu bilgiler getirilebilir.

Dizaynda IMEI numaralarının hangi alandan çekileceği, dizayn alan numaraları kullanılarak veya sql desteği ile getirilebilir. Bu örnekte sql desteği kullanılarak getirilmiştir.

Dizayn içinde Yer:“**Kalem**”, Tip:"**Sql**", e-Devlet XML Tag:“**InvoiceLine-AdditionalItemIdentification**” seçilir. Satır, sütun ve uzunluk bilgisi girilerek kaydedilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/7cb22d1f-0400-4915-99fc-02af7d6a16bc/d3.png)

Aşağıda IMEI numaralarının seri ekranındaki seri1 ve seri2 alanlarından getirildiği durumda örnek bir sql cümlesi bulunmaktadır. Bu sql cümlesine göre telefon stoğuna ait girilen IMEI bilgileri TBLSERITRA tablosundan getirilmektedir.

Bir telefona ait birden fazla IMEI bilgisi olması durumunda, bu IMEI bilgilerinin yan yana basılması ve **(IMEI)1. IMEI Numarası;(IMEI2)2. IMEI Numarası…** formatında olması gerekmektedir.

**'(IMEI)'+SERI_NO+(CASE WHEN LEN(ISNULL(ACIK1 ,''))\>0 THEN ';(IMEI2)'+ ISNULL(ACIK1,'') ELSE '' END),\* FROM TBLSERITRA WHERE STRA_INC= VT_Sayisal({4510})**

Telefonlara ait IMEI bilgilerinin XML dışında, e-Arşiv görüntüsünde de kalemler kısmında çıkması için, XSLT içerine kalemler kısmına aşağıdaki kod bloklarının eklenmesi gerekir. Ancak bu bir zorunluluk değildir.

**\<td class="lineTableTd" style="width:7.4%" align="center"\>

\<span style="font-weight:bold;"\>

\<xsl:text\>IMEI NO\</xsl:text\>

\</span\>

\</td\>**

**\<td class="lineTableTd"\>

\<xsl:text\>&#160;\</xsl:text\>

\<xsl:value-of select="./cac:Item/cac:AdditionalItemIdentification"/\>

\<xsl:value-of select="cbc:ID"/\>

\</td\>**

**Tablet/PC satışında;**

AdditionalItemIdentification/ID altındaki schemeID alanına “TABLET_PC” yazılmalıdır.

Dizayn içinde Yer:“**Kalem**”, Tip:"**Başlık**", e-Devlet XML Tag:“**InvoiceLine-AdditionalItemIdentification-schemeID**” seçilir. Başlık: “**TABLET_PC**” yazılır. Satır, sütun ve uzunluk bilgisi girilerek kaydedilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/50ce4554-1dfd-42dd-92f7-0cfb67e4441d/d4.png)

Tüm bu tanımlamalar sonrasında e-Arşiv Faturası için taslak oluşturulduğunda e-Arşiv fatura tipinin TEKNOLOJIDESTEK olarak geldiği görülmektedir. Ayrıca xslt içerisine yukarıda belirtilen kodun tanımlanması durumunda da kalemler kısmında IMEI numaralarının basımı sağlanmaktadır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/c8e9280e-6152-47d5-a681-576ba29b27f3/d55.png)

Taslak sonrası oluşan XML’ e baktğımızda ise,InvoiceTypeCode taginin “TEKNOLOJIDESTEK” destek olarak geldiği görülmektedir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/b835a060-ea7e-436e-9a4a-60032c4c6ace/d6.png)

XML’ de telefon stoğuna ait IMEI bilgilerinin AdditionalItemIdentification taginde yer aldığı görülmektedir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/6fd5baee-7793-4b06-aca8-37a1598d225c/d7.png)

Tablet/PC satışı ile ilgili kesilen e-Arşiv faturası örneği ve xml’ i aşağıdaki gibidir. Tablet/pc stoklarına ait bir IMEI Numara bilgisi olmadığı için AdditionalItemIdentification taginin schemeID kısmı sadece TABLET_PC olacak şekilde düzenlenmektedir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/b4740970-34f0-4406-b627-90f56c212d7d/d8.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/9d313576-9326-45c9-849b-27cbb1c29cac/d9.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/e50c373e-50c5-4d56-82a8-60fc27eac87d/d10.png)
