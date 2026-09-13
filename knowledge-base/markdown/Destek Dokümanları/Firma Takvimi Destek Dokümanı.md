---
title: "Firma Takvimi Destek Dokümanı"
page_id: "104104661"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Firma Takvimi Destek Dokümanı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Firma Takvimi Destek Dokümanı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWY5OWYyOGY5LThiMTMtNDBkOS1hZTE0LThhODE4ZjI5NWE2NiZsaW5rPWI2YmU1NDZmLTAwMTItNDQ4Yy05ZDMyLTY0ODZiNjFkNmFiMSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=f99f28f9-8b13-40d9-ae14-8a818f295a66&link=b6be546f-0012-448c-9d32-6486b61d6ab1&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "firma-takvimi-destek-dokumani_104104671_104104661.html"
source_version: "2023-02-08T14:19:56.193+03:00"
source_bytes: 3811325
fetched_at: "2026-09-13T04:23:42+00:00"
generator: "netsis-scraper 1.0.0"
---
# Firma Takvimi Destek Dokümanı

Firma Takvimi, Kayıt/Yardımcı Programlar modülü altında yer alır. Firma takvimi uygulaması hakkında ayrıntılı bilgiye bu dokümandan ulaşılır. Firma Takvimiyle, firma için genel veya özel takvimler hazırlanarak takvim kontrollerinin program tarafından otomatik olarak yapılması sağlanır. Böylece hafta tatillerinin, dini veya resmi tatillere denk gelen tarihlerin kullanıcı tarafından değil program tarafından takip edilmesi sağlanır. Ayrıca her cari için, farklı takvim ve çalışma günleri tanımlanarak, tek bir takvim yerine birçok takvime göre gün takibi de yapılabilir.

![](../_assets/85f036356cc3e23b180a.png)

Firma Takvimi, Sabit ve Detay olmak üzere iki sekmeden oluşur.

![](../_assets/8bb6c2e282dbf9fd014a.png)

**Kod** Tanımlanacak takvim için kod numarası girilen alandır. En fazla 10 sayısal karaktere sahip kod tanımlaması yapılabilir. Takvim, bu alanda verilen kod ile program genelinde ekrana getirilebilir.

**Açıklama** Kod bilgisine ait açıklamanın girildiği alandır.

**Sorgula** Takvim tanımlanırken, hafta tatilleri, dini veya resmi tatillerin belirlenmesi gerekir. Program genelindeki modüllerde kayıt oluştururken, vade tarihi olarak çalışılmayan bir gün tespit edildiğinde, programın uyarı vermesi için kullanılan seçenektir. İşaretlendiğinde, çalışılmayan bir gün vade tarihi olarak girildiğinde, girilen günün tatil gününe denk geldiğini gösteren bir uyarı ekranı görüntülenir. Vadenin alınması istenen tarih sorgulanır. Yapılan seçime göre ileri veya geri bir çalışılan gün hesaplanır. İşaretlenmediği zaman uyarı ekranı ile karşılaşılmaz. Yapılan takvim tanımlaması baz alınarak, çalışılan vade tarihi program tarafından otomatik olarak değiştirilir.

**Genel Rehber** Firma için geçerli olan genel bir rehber tanımlanması için kullanılan seçenektir. Tanımlanan bir rehberden sonra, başka bir rehber için "Genel Rehber" sorgulaması işaretlenmez. Her cari hesap için istenirse, ayrı bir takvim tanımlanabilir ve tanımlanan takvim kodu Cari Hesap Kayıtlarında "**Firma Takvimi**" alanında belirtilir. Cari Hesap Kayıtları ekranında Firma Takvimi boş bırakılırsa, takvim hesaplaması için Genel Takvim baz alınır.

![](../_assets/be9026947db2bf7cd317.png)

**Hafta** **Göster** parametresi işaretlenirse, "**Detay**" sekmesinde her haftanın hafta numarası görüntülenir. İşaretlenmediği zaman, takvimde sadece günler görüntülenir.

**Bugünü** **Göster** parametresi işaretlenirse, "**Detay**" sekmesinde içinde bulunulan günün tarihi görüntülenir. İşaretlenmediği zaman, takvimde sadece günler görüntülenir.

![](../_assets/9a0cf81dc32f9af7c955.png)

**İşlem** **Türü** İşlemler sırasında hesaplanan vade tarihinin kullanılan takvimde tanımlanan çalışılmayan bir güne denk gelmesi halinde, programın vade tarihinin ileri bir güne alınması için "**İleriye** **Git**", geri bir güne alınması için "**Geriye** **Git**" seçeneğinin kullanılması gerekir.

Örneğin, 01.01.2023 tarihi Yılbaşı' na denk geldiği için, "**İleriye Git**" seçeneği işaretlendiğinde, program vade tarihine ilerideki ilk çalışma günü olan 02.01.2023 tarihini getirir.

**Hafta** **Başlangıcı** Takvimde görülmesi istenen haftanın başlangıç günü belirlenir. Buradaki belirlemeye göre "**Detay**" sekmesindeki haftanın başlangıç günü değişir.

Örneğin, Hafta başlangıcı olarak "Salı" gününün seçildiğinde, takvimde haftanın ilk günü olarak "Salı" günü gelir.

Detay sekmesinde; tanımlanan takvime, istenen tatil günleri (standart olan tatil günleri, resmi tatiller, dini tatiller ve hafta sonu tatilleri gibi) eklenir veya çıkartılır. Bir tatil gününün tek bir türü olabilir. Belli bir tarih, hem resmi hem de dini tatil olarak tanımlanamaz.

![](../_assets/28171e9ab331becb00f3.png)

**Örnek**

Cari için tanımlanan firma takvimi tanımında aşağıdaki ekranda da görüleceği üzere hafta başlangıcı Salı olarak, işlem türü ileriye git olarak tanımlanmış ve hafta tatilleri, resmi ve dini bayramlar takvimde belirtilmiştir. Bu firma takvim bilgisi de cari hesap kayıtlarında firma takvimi alanında seçilmiştir.

![](../_assets/8d38bbe2d3213958c506.png)

Bu tanımlamalardan sonra girilen faturada vade tarihi 01.01.2023 girildiğinde (girilen vade tarihi yılbaşı günü yani bir tatil gününe denk geldiği için) "**Sorgula**" seçeneği işaretlenerek hazırlanan bir takvim olduğu için, vade tarihi tatil gününe geldiğinden aşağıdaki gibi bir uyarı ekranı gelir.

Vade tarihi Yılbaşına denk geldiği için, vade tarihinin Yılbaşı' na gelmesi ve seçilecek işlem türü sorgulanır. Yapılan seçime uygun çalışma günü bulunarak "Vade Tarihi" alanına uygun tarih getirilir.

Tanımlanan takvimde "Sorgula" alanı işaretlenmediği zaman bu uyarı ekrana gelmez ve uygun çalışma günü otomatik olarak "Vade Tarihi" alanına gelir.

![](../_assets/b49a99f659b3cdaa44d5.png)

![](../_assets/f710f493beadb27a11ca.png)
