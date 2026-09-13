---
title: "Hücre Tanımlama"
page_id: "22803915"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Dinamik Depo"
  - "Kayıt / Dinamik Depo"
  - "Hücre Tanımlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Dinamik Depo / Kayıt / Dinamik Depo / Hücre Tanımlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTY3NWVjOTU4LTQ4ZGMtNDc1Zi05MThhLWQ4NjM4MTE2ODAzYSZsaW5rPTc1ZWNhMDlmLWI2M2UtNDc0Ni04MWI0LWFmNjYzNjE4ZGU0MyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=675ec958-48dc-475f-918a-d8638116803a&link=75eca09f-b63e-4746-81b4-af663618de43&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "hucre-tanimlama_74716170_22803915.html"
source_version: "2022-10-31T08:51:35.980+03:00"
source_bytes: 29237
fetched_at: "2026-09-13T04:06:05+00:00"
generator: "netsis-scraper 1.0.0"
---
# Hücre Tanımlama

Hücre Tanımlama; Dinamik Depo-Kayıt menüsünün altında yer alır. Hücre Tanımlama bölümü ile; malların depolandığı yerdeki, malların yerleştirildiği bölmeleri yani hücreleri tanımlanır.

Hücre kodlamasının dikkatli yapılması gerekir. Çünkü, hücre kodlarının sıralanması sonucu malların yerleştirilmesi ve toplaması yapılır.

Depo yerleşiminde şu düşüncelerle hareket edilebilir:

- Örneğin; en hızlı şekilde mal toplanması ve yerleştirilmesi için en çok hareket gören malların en yakın raflara yerleştirilmesi, daha nadir hareket gören malların uzak raflara yerleştirilmesi gerekir. Bu düşünce ile hareket edilecekse en yakın raflar, en küçük kodlara sahip olmalı ve en sık kullanılan mallar bu raflara yerleşecek şekilde tanımlama yapılmalıdır. Aynı şekilde uzak raflar kod sırasında daha büyük kodlara sahip olmalıdır.
- Benzer bir örnek; ağır malların öncelikli toplanması, daha hafif malların daha üste gelmesi gerektiğidir. Bu durumda, ağır malların depolandığı raflar, kod sırasında daha küçük koda sahip olmalı, hafif malların koyulduğu raflar ise daha büyük koda sahip olmalıdır. Hücre kodlarını tanımlarken depo içinde hangi tercihin öncelikli olduğuna karar vermek gerekiyor. Çünkü kodlamaya göre toplama ya da yerleştirme işlemlerinde hız kazanılabilir. Hücre kodları, tüm depolar ve şubeler bazında tektir. Bu nedenle, birden fazla depo kullanan veya şube kullanan yerlerde hücre kodlarının standardının buna göre belirlenmesi gerekir.

Örneğin; Depodaki her bir koridora A,B,C gibi isim verildiğini düşünelim. Koridorda sağda bulunan hücreler için 1, soldakiler için 2 verilsin. Aynı zamanda, aynı koridordaki en alt raf için 0, 1. kat için 1, 2. kat için ise 2 tanımlansın. Hücrelerin yan sıra numaraları ise artan sayıda 1, 2, 3, 4 gibi verilsin.

Bu durumda; A koridorunda sağdaki raf, 1. kat 2. sıradaki hücre için kodlama A11-2 olur.

![](../../../../_assets/c93f5dd197cf5da30194.png)

Hücre Tanımlama ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Hücre Tanımlama Ekranı |  |
| --- | --- |
| Hücre Kodu | Maksimum 15 karakter uzunluğunda, hücre kodlamasının yapıldığı alandır. Rehber butonu ile Hücre Kodları rehberine ulaşılabilir. |
| Grup Kodu | Tanımlanan hücrenin hangi hücre grubuna ait olduğu Grup Kodu alanına girilir. Rehber butonu ile Grup Kodları rehberine ulaşılabilir. |
| Depo Kodu | Depo Kodu alanı boş bırakılamaz. İlgili hücrenin tanımlı olduğu, yani içinde bulunduğu lokal depo kodunun Depo Kodu alanına girilmesi gerekir. Depo kodu alanında yer alan Rehber butonuna tıklandığında, Lokal Depo Tanımlama ekranında “Lokasyon Takibi Yapılsın Mı” parametresi işaretlenmiş depolar listelenir. Örneğin; Firmanın lokasyon takip ettiği 2 ayrı depo olabilir. Her depoda ayrı ayrı hücre tanımlaması yapılması gerektiği için, tanımlanan hücrenin lokal deposunun belirtilmesi gerekir. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır. Yapılan kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../_assets/604869e96ca2f8104a00.png) butonuna tıklanması gerekir.
