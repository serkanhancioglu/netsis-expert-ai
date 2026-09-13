---
title: "Banka Sözleşme Tanımlamaları"
page_id: "22806217"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Banka"
  - "Kayıt / Banka"
  - "Kredi Kartı Tanımlamaları"
  - "Banka Sözleşme Tanımlamaları"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Banka / Kayıt / Banka / Kredi Kartı Tanımlamaları / Banka Sözleşme Tanımlamaları"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWZhYmFmMzI1LWI2NDEtNDY2Zi04MWM5LWUxNzE1ZGI0YzUyYyZsaW5rPWMyNDZmODc1LTNiOTctNDY3Zi1iZGI3LTQzNjZmMTVkZmVmYiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=fabaf325-b641-466f-81c9-e1715db4c52c&link=c246f875-3b97-467f-bdb7-4366f15dfefb&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "banka-sozlesme-tanimlamalari_22806224_22806217.html"
source_version: "2022-04-04T10:57:59.737+03:00"
source_bytes: 263175
fetched_at: "2026-09-13T04:10:00+00:00"
generator: "netsis-scraper 1.0.0"
---
# Banka Sözleşme Tanımlamaları

Finans Bölümü'nde, "Kayıt/Banka" menüsünün altında yer alır. Banka Sözleşme Tanımlamaları, bankalar ile yapılan sözleşmenin hangi kredi kartına ait olduğu ve geçerli olduğu tarih aralığı ile ilgili tanımlamaların yapıldığı bölümdür. Bankalar ile yapılan sözleşmelerde, diğer banka kredi kartlarının kullanımı durumunda uygulanan kesintiler farklı olacağı için, bu kesintiler için ayrı sözleşme tanımlanır. "Banka Sözleşme Tanımlamaları" ekranı; Banka Sözleşme Tanımlamaları, Sözleşme Detay Bilgileri ve "Sözleşme Kesinti Bilgileri" sekmelerinden oluşur.

**Banka Sözleşme Tanımlamaları**

![](../../../../../_assets/580d0cfcbc07f27d1232.png)

Banka Sözleşme Tanımlamaları ekranında yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| Banka Sözleşme Tanımlamaları Ekranı |  |
| --- | --- |
| Sözleşme Kodu | Bankalar ile yapılan sözleşmeler için kod tanımlaması yapılan alandır. Sözleşme kodu en fazla 15 karakterden oluşur. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, sözleşme kodlarına ulaşılır. |
| Açıklama | Sözleşme koduna ait açıklama bilgisinin girildiği alandır. |
| Kart Kodu | Yapılan sözleşmenin hangi kredi kartına ait olduğunun belirlenmesi için ilgili kart kodunun girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, kredi kartı tiplerine ulaşılır. |
| Banka Hesap Kodu | Kapalı fatura kaydı sırasında çalışacak banka kodunun girildiği alandır. Seçilen banka kodunda, kesintiler ve taksitlerin her biri için sözleşmede belirtilen koşullara göre, ayrı ayrı alacak kayıtları oluşur. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, banka hesap kodlarına ulaşılır. |
| Başlangıç Tarihi | Sözleşme başlangıç tarihinin girildiği alandır. |
| Bitiş Tarihi | Sözleşme bitiş tarihinin girildiği alandır. |
| Kilit | Kaydedilen sözleşmenin tahsilat işlemlerinde kullanıma kapatılmasını sağlayan seçenektir. |

**Sözleşme Detay Bilgileri**

Sözleşmenin taksit aralığı ve koşulları ile ilgili tanımlama yapılmasını sağlayan sekmedir.

![](../../../../../_assets/79d8da3191de6526ef61.png)

Sözleşme Detay Bilgileri sekmesinin alanları ve içerdiği bilgiler aşağıdaki şekildedir:

| Bankaya Sözleşme Tanımlamaları Ekranı |  |
| --- | --- |
| Sözleşme Kodu | "Banka Sözleşme Tanımlamaları" sekmesinde tanımlanan sözleşme kodunun otomatik olarak aktarıldığı alandır. |
| Taksit Aralığı | Başlangıç ve bitiş taksit aralıklarının belirlendiği alandır. Başlangıç taksit 0 (sıfır), bitiş taksit 0 (sıfır) olarak tanımlanan taksitler puan kullanımını ifade eder. Taksit aralıklarının bir öncekini kapsamayacak şekilde tanımlanması gerekir. |
| Tahsilat şekli | Bankadan yapılan tahsilatlar "Tek Seferde" veya "Vadeli" olarak yapılır. Tahsilat şekli olarak "Vadeli" seçildiğinde; toplam tahsil edilmesi gereken tutar, taksitlere bölünür. "Tek Seferde" seçildiğinde ise; müşteri, ödemeleri taksitli olarak yapmasına rağmen satışı yapan şirket paranın tamamını bankadan peşin olarak tahsil eder. |
| Vade Atlama | Taksit atlama sayısının girildiği alandır. **Örneğin:** Vade atlatma sayısının 1 olduğu varsayıldığında, 20/06/2019 tarihinde yapılan satışın taksit atlatma sayısına göre ilk ödemesi 20/07/2019 tarihine denk gelir. |
| Blokaj Şekli | Bankanın, satış işleminden sonra parayı belli bir süre elinde tutması ve ödemeyi daha sonra gerçekleştirmesine "Blokaj" denir. Blokaj şekli; "Sabit Gün" ve "İlave Gün" olmak üzere iki seçenekte belirlenir. "Sabit Gün" seçildiğinde; blokaj değerine girilen değer, ayın gününü ifade eder. **Örneğin:** "Blokaj Değeri" alanına 10 değeri girildiğinde, ayın 10.günü anlamına gelir. "İlave Gün" seçildiğinde ise; blokaj değerine girilen gün, alışveriş tarihine eklenerek ilk ödemenin yapılacağı günü ifade eder. Taksit uygulamasının olduğu durumlarda ilk ödemenin yapılacağı gün baz alınarak diğer ödemelerin vadeleri oluşur. **Örneğin:** Alışverişin 20/06/2019 tarihinde yapıldığı ve "İlave Gün" seçilerek "Blokaj Değeri" alanına 30 değerinin girildiği varsayıldığında, Blokaj 20/07/2019 tarihinde biter ve banka bu tarihte ilk ödemeyi gerçekleştirir. |
| Blokaj Değeri | Blokaj uygulamasının kaç gün süreceğini belirlemek için değer girilen alandır. "Blokaj Şekli" alanında yapılan seçime göre, sabit gün ya da ilave gün değeri girilir. |
| Vade Şekli | Bankanın yapacağı ödemelerin hangi vadelere göre oluşacağının belirlendiği alandır. Vade Şekli alanı; Sabit Gün, İlave Gün, Dinamik Değer ve İlave Gün (+1) olmak üzere dört seçenekten oluşur. |
| Vade Değeri | Vadenin kaç gün olacağının belirlendiği alandır. "Vade Şekli" alanında yapılan seçime göre, sabit gün için değer belirlenmesini sağlar. |
| Dinamik Değer | Vade tarihi tespiti için kullanılan seçenektir. Dinamik değer kullanımında belirlenen vade tarihi; İlk taksit olması, vade tarihi gününün dinamik değer ve belirlenen aralıklara göre büyük/küçük olması gibi durumlar baz alınarak oluşturulur. |
| Açıklama | Sözleşme açıklama bilgisinin girildiği alandır. |

**Sözleşme Kesinti Bilgileri**

"Sözleşme Detay Bilgileri" sekmesinde girilen taksit aralığı doğrultusunda, banka tarafından hangi kesintilerin yapılacağının belirlendiği sekmedir.

![](../../../../../_assets/f9e6fc656ef94feb7018.png)

Sözleşme Kesinti Bilgileri sekmesinin alanları ve içerdiği bilgiler aşağıdaki şekildedir:

| Bankaya Sözleşme Tanımlamaları Ekranı |  |
| --- | --- |
| Sözleşme Kodu | "Banka Sözleşme Tanımlamaları" sekmesinde tanımlanan sözleşme kodunun otomatik olarak aktarıldığı alandır. |
| Kesinti Kodu | Tanımlanan sözleşme için, taksit aralığı bazında uygulanacağı kesinti kodunun girildiği alandır. Kesinti kodu seçilmesi için, öncelikle "Sözleşme Detay Bilgileri" sekmesinde taksit aralığının tanımlanması gerekir. Tanımlanan taksit aralıklarından biri seçildikten sonra bu sekme aktif hale gelir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, "Banka Kesinti Kayıtları" sekmesinde tanımlanan kesinti kodlarına ulaşılır. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır. Yapılan kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
