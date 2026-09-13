---
title: "XSLT Editörde Kümülasyon Nasıl Yapılır?"
page_id: "50688878"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "XSLT Editörde Kümülasyon Nasıl Yapılır?"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / XSLT Editörde Kümülasyon Nasıl Yapılır?"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTc0YzA0MmZlLWFkYjktNGM1NS05YmY1LTQ1NWVmMjc0N2E2NCZsaW5rPWFlNDAzNTJlLWNkZWUtNDk0ZC05OTQ1LTA4ZTZiYTdmMzEwOSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=74c042fe-adb9-4c55-9bf5-455ef2747a64&link=ae40352e-cdee-494d-9945-08e6ba7f3109&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "xslt-editorde-kumulasyon-nasil-yapilir_80090318_50688878.html"
source_version: "2022-11-03T08:52:57.330+03:00"
source_bytes: 1649557
fetched_at: "2026-09-13T04:25:14+00:00"
generator: "netsis-scraper 1.0.0"
---
# XSLT Editörde Kümülasyon Nasıl Yapılır?

XSLT Editörde Kümülasyon Nasıl Yapılır? ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Stok kalemlerinin belirli alanlara göre kümüle edilip kümüle edilmiş şekilde e-Belgeler üzerinde görüntülenmesi ve basılabilmesi için XSLT editör üzerinde gruplama özelliği kullanılır. Belgedeki stok kalemlerinin; stok kodlarına, stok isimlerine, stokların grup kodlarına, diğer kod 1/2/3/4/5 kodlarına, stokların GTIP' lerine (Gümrük Tarife Kodu), belgede kalem bazında girilen ekalanlara veya farklı alanlara göre kümüle edilerek e-Belge üzerinde görüntülenmesi ve basılabilmesi sağlanır.
!! XSLT editör üzerinde yapılan kümülasyon sonrasında e-Belge görüntüsünde yapılan kümülasyon görüntülenirken, XML içerisine yapılan kümülasyon yansımaz. Belge kalemleri kümüle edilmeden XML içinde gösterilir.

Örneğin, belgede girilen stok kalemlerinin stok grup kodlarına göre kümüle edildiğinde gerekli tanımlamalar yapılır.

Dizayn içerisinde kümülasyon yapılacak olan alan tanımlaması ve e-Devlet XML tagiyle eşleştirilmesi aşağıdaki şekildedir:

- Dizayn içerisinde kümülasyon yapılacak alan, dizayn alan numarası seçilerek veya sql desteği kullanılarak tanımlanır.
- Tanımlanan bu dizayn satırı, e-Devlet XML Tag alanında XSLT dosyasında stok kalemleri kısmında kullanılmamış ve boşta olan InvoiceLine taglerinden biri ile eşleştirilir.
- Gruplamada kullanılabilecek e-Devlet XML tagleri, InvoiceLine-Brandname, InvoiceLine- BuyersItemIdentification, InvoiceLine-SellersItemIdentification, InvoiceLine-Description, InvoiceLine-ModelName,InvoiceLine-Name,InvoiceLine-Note, InvoiceLine- ManufacturersItemIdentification, InvoiceLine-ItemClassificationCode tagleridir.
- Örnekte Yer olarak "Kalem", Tip olarak "Program", stok grup kodu için alan numarası "4003" ve E-Devlet XML Tag olarak "InvoiceLine-ModelName" seçilir.

![](../_assets/0c372a5424a290818576.png)

- XSLT editörde stok kalemleri kısmında dizayn içinde kümülasyon için tanımlanan alan için kolon eklemesi yapılır.
- XSLT dosyasında kolon başlığı eklemek için aşağıdaki kod bloğu eklenir. Örneğe göre eklenen kolonun başlığı, "Grup Kodu" 'dur.
**width="100"\>*

*\<xsl:text\>Grup* *Kodu*

XSLT dosyasında eklenen kolonun değerini getirmek için dizaynda tanımlanan satırın eşlendiği e- Devlet XML Tag' inin yer aldığı aşağıdaki kod bloğu eklenir. Örneğe göre "ModelName" e-Devlet tagi kullanılır.
**align="left"* *style="white-space:* *nowrap"\>*
*\<xsl:text\>*
*\<xsl:value-of\< em=""\> *select="cac:Item/cbc:ModelName"* /\>

![](../_assets/72aee313b8ea4ab73a59.png)
![](../_assets/4f35ca3782affc325250.png)***
- XSLT editörde kümülasyon için, XSLT Grup Oluşturma ekranında Özellikler listesinden ilgili e-Devlet XML Tag seçilip artı butonu ile eklenir ve sonraki butonu ile gruplama XSLT' ye eklenir.

![](../_assets/c1c00c413c46f98ae623.png)![](../_assets/660a62f2382b4d83272a.png)![](../_assets/530f8ec0c5087cbfc049.png)

- XSLT dosyasında gruplama yapıldıktan sonra, gruplama ile ilgili bazı XSLT kodları dosyaya eklenir ve dosya kaydedilir.
- Belge girilir ve Toplu e-Fatura/e-Arşiv Oluşturma ekranında ilgili dizayn seçilerek taslak oluşturulur.

Girilen belgede 2 ürün bulunmaktadır. Her 2 ürünün Stok Kartı Kayıtları ekranında Grup Kodu "12- Meyve'dir. Taslak oluşturma sonrasında e-Belge Görüntüsünde 2 stok kaleminin kümüle edildiği görülür.
![](../_assets/4a1158b2591148a38beb.png)
![](../_assets/4a4babe3290fdc48788b.png)
