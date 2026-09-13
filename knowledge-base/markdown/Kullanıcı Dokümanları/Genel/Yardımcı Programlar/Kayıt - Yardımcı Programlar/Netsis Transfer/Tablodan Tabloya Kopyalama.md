---
title: "Tablodan Tabloya Kopyalama"
page_id: "24753095"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Genel"
  - "Yardımcı Programlar"
  - "Kayıt / Yardımcı Programlar"
  - "Netsis Transfer"
  - "Tablodan Tabloya Kopyalama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Yardımcı Programlar / Kayıt / Yardımcı Programlar / Netsis Transfer / Tablodan Tabloya Kopyalama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTY4Y2YyYmMyLTJkZTctNDAxOC1hOTRmLWExODIwMTA1MWU4MiZsaW5rPTNlM2UyNTJlLTY2NTUtNDY5OC1hMTRkLTdkNzQzNDc3ODQ1YSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=68cf2bc2-2de7-4018-a94f-a18201051e82&link=3e3e252e-6655-4698-a14d-7d743477845a&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "tablodan-tabloya-kopyalama_24753100_24753095.html"
source_version: "2022-10-04T15:03:05.143+03:00"
source_bytes: 199797
fetched_at: "2026-09-13T04:17:14+00:00"
generator: "netsis-scraper 1.0.0"
---
# Tablodan Tabloya Kopyalama

Tablodan Tabloya Kopyalama, Genel Bölümü'nde, "Kayıt/Yardımcı Programlar" menüsünün altında yer alır. Tablodan Tabloya Kopyalama, herhangi bir veri tabanına ait, bir tablodaki bilgilerin başka bir veri tabanındaki tabloya aktarılması için kullanılan bölümdür. Tablodan Tabloya Kopyalama ekranı; Kaynak/Hedef Tablo, Kaynak Sahalar ve Eşleme sekmesinden oluşur.

**Kaynak/Hedef Tablo**

Kaynak/Hedef Tablo, tablo aktarım işleminin yapılmasında kaynak/hedef veritabanı ve aktarılacak tabloların tanımlandığı sekmedir.

![](../../../../../_assets/1b04563420959e495b63.png)

Tablodan Tabloya ekranı Kaynak/Hedef Tablo sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Tablodan Tabloya Kopyalama Ekranı |  |
| --- | --- |
| Kaynak Tablo/Veri Tabanı Adı | Tablo bilgileri alınacak veri tabanı isminin girildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile veritabanı adları arasından seçim yapılır. |
| Kaynak Tablo/Tablo Adı | Tanımlaması yapılan veri tabanına ait tablonun listelenmesini sağlayan alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile, bilgi alınması istenen tablo seçilir. |
| **![](../../../../../_assets/c55cc4aed7ea3eaacbe7.png)** Kısıtlar | Kaynak tablodan alınacak bilgiler için kısıt verilmesini sağlayan butondur. **Örneğin** Aktarılacak tablo Tblstsabit - yani, stok sabit kartları - ve Grup Kodu 001 olan stok kartları aktarılacaksa bu bölümden grup kodu kısıtı verilebilir. |
| Farklı Kayıt | Kaynak tablodan alınan sahalar tekrarlı olması durumunda, bu kayıtların hedef tabloya tekrarsız olarak aktarılması için kullanılan seçenektir. **Örneğin** Kaynaktaki Tblsthar - stok hareket kayıtları - tablosundaki stok kodlarından, hedefte Tblstsabit - stok sabit kayıtları - tablosunun oluşturulması için kullanılabilir. Çünkü, Tblsthar tablosunda stokun birden fazla hareketi olacağı için stok kodları tekrarlı olarak oluşur. Fakat, Tblstsabit tablosunda tekrarsız oluşturulması gerekir. Çünkü, her stok için tek bir stok kartı kaydının olması gerekir. |
| Hedef Tablo/Veri Tabanı Adı | "Kaynak Tablo" bölümünde belirlenen tablo bilgilerinin alınacağı veritabanının girildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile veritabanı adları arasından seçim yapılır. |
| Hedef Tablo/Tablo Adı | "Kaynak tablo" bölümünde belirlenen tablo bilgilerinin alınacağı tablo adının girildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile, bilgi alınması istenen tablo seçilir. |

**Kaynak Sahalar**

Kaynak Sahalar sekmesi, "Kaynak Tablo" bölümünde seçilen tabloya ait sahaların listelendiği sekmedir. Aktarılacak sahaların bu sekmeden seçilmesi gerekir.

![](../../../../../_assets/a4638cd903573711c3ca.png)

Tablodan Tabloya ekranı Kaynak Sahalar sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Tablodan Tabloya Kopyalama Ekranı |  |
| --- | --- |
| Sahalar | Tablodan tabloya kopyalama işlemi için kısıt verilmesi istenen alanlar yer alır. Ekle ![](../../../../../_assets/6acbe5741cb2a7d733d8.jpg) butonu ile istenen alanlar "kısıt verilecek sahalar" kısmına eklenir. |
| Kısıt Verilecek Sahalar | Tablodan tabloya kopyalama işlemi için kısıt verilen sahaların yer aldığı alandır. Çıkar ![](../../../../../_assets/ac9ca28b6c03f3b2dbc0.jpg) butonu ile istenmeyen alanlar çıkarılır. |

**Eşleme**

Eşleme, aktarılması istenen kaynak sahaların, aktarılacağı hedef sahanın belirlendiği sekmedir. Kaynak sahalar hedef tabloda varsa otomatik eşleşerek ekrana gelir.

![](../../../../../_assets/7d3ebfe3bdc53623d186.png)

Tablodan Tabloya ekranı Eşleme sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Tablodan Tabloya Kopyalama Ekranı |  |
| --- | --- |
| Hedef Saha | Hedef için seçilen tabloya ait sahaların listelendiği alandır. |
| Kaynak Saha | Kaynak tabloya ait sahaların listelendiği alandır. Herhangi bir sahanın hedefe aktarılmaması için “Değiştirme” öndeğeri ile bırakılması gerekir. Kaynakta olup hedefte olmayan bir sahanın aktarılması için, "Kaynak Saha" kolon isminin altındaki listeden farenin sol tuşu ile tıklayarak saha seçimi yapılır. Kaynak sahalarda bulunan bir saha hedefte başka bir sahaya aktarılacak ise, aktarılması istenen sahanın seçilmesi gerekir. **Örneğin** Tblstsabit tablosundaki "Grup Kodu" sahasının, hedefte "Kod_1" sahasına aktarılacağı varsayıldığında "Hedef Saha" sütununda bulunan "Kod_1" sahası için "Kaynak Saha" kolon isminin altındaki sahaya farenin sol tuşu ile tıklayarak "Grup_kodu" seçiminin yapılması gerekir. Böylece "Grup Kodu" sahasındaki bilgiler, hedef tabloda "Kod_1" sahasına aktarılır. |
| Sabit Değer | Hedef tabloya aktarılması istenen sabit değerlerin tanımlandığı alandır. **Örneğin** Kaynak tabloda - Tblsthar - ölçü birimi olmadığı halde, hedefte - Tblstsabit - ölçü birimlerinin oluşturulması için, ölçü birimlerini sabit değer olarak söz konusu alana girilmesi gerekir. |
| Identity Insert | Veritabanı tablolarının bazı sahaları sistem tarafından otomatik oluşturulan auto incremental - otomatik artan - sahalardır. **Örneğin** Tblsthar - stok hareket kayıtları - tablosundaki INCKEYNO sahası bu tür özelliğe sahip bir sahadır. Bu sahalara sahip bir tabloya bilgi aktarılmak istendiğinde ve auto incremental saha bilgisinin değişmemesi isteniyorsa, "Identity Insert" seçeneğinin işaretlenmesi gerekir. Seçenek işaretlenmediği zaman; hedef tabloda böyle bir saha olduğunda ve bu sahaya bir bilgi aktarılmaya çalışıldığında program uyarı verir. Tüm ayarlamaların yapılmasından sonra Tamam tuşuna basıldığında, aktarma işlemi başlayacaktır. |
| ![](../../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Kopyalama işleminin başlatılmasını sağlayan butondur. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
