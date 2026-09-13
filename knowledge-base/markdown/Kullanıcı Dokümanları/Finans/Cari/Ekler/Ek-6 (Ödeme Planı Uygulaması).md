---
title: "Ek-6 (Ödeme Planı Uygulaması)"
page_id: "22805765"
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
  - "Ek-6 (Ödeme Planı Uygulaması)"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Cari / Ekler / Ek-6 (Ödeme Planı Uygulaması)"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWEwOTU5NmNmLWI2YWItNGQ0NC04ODExLTExZWUyM2I4OTNmYiZsaW5rPTIzMTczZDVhLTJiYTItNGM0Yy04OTQzLTUwNWU1NWQwMjUyYiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=a09596cf-b6ab-4d44-8811-11ee23b893fb&link=23173d5a-2ba2-4c4c-8943-505e55d0252b&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ek-6-odeme-plani-uygulamasi_29992205_22805765.html"
source_version: "2022-11-21T15:15:14.870+03:00"
source_bytes: 173173
fetched_at: "2026-09-13T04:08:52+00:00"
generator: "netsis-scraper 1.0.0"
---
# Ek-6 (Ödeme Planı Uygulaması)

Ödeme planı uygulaması hakkında ayrıntılı bilgiye bu dokümandan ulaşılır.

**Koşul Bağlantılı Cari Ödeme Planı**

Koşul uygulamasını kullanan firmaların, Cari → Kayıt → Koşul Kayıtları → [Genel Koşul Kayıtları](<../Kayıt - Cari/Koşul Kayıtları/Genel Koşul Kayıtları.md>) → "Koşul Genel-2" sekmesinde bulunan "Ödeme Kodu" alanına, o koşula bağlanacak ödeme planına ait kod bilgisini girmeleri gerekir.

![](../../../../_assets/44196d61532467506b0d.png)

Böylece sipariş, irsaliye ve fatura kayıtları sırasında sorgulanan koşul kodu girildiğinde, bu koşula bağlanan ödeme kodu "Koşul Bilgileri" sekmesindeki ilgili alana otomatik olarak gelir. Cari ödeme planlarının koşul bağlantılı uygulanması için, "Koşul Sabit Kayıtları" ekranında yer alan “Cari Hesap Vadelere Bölünerek Atılsın” seçeneğinin işaretlenmesi gerekir. Ayrıca, Fatura → Kayıt → Satış Parametreleri → Genel 4 → "Koşul C/H Vadelere Bölünerek Geçsin Parametresi Dikkate Alınsın” parametresinin de işaretli olması gerekir. Aksi halde, "Koşul Sabit Kayıtları" bölümünde yapılan seçim dikkate alınmaz.

![](../../../../_assets/c55ab579f7f7f792c404.png)

Yukarıdaki örnekte girilen ödeme planının, 15/06/2006 tarihli bir faturaya aktarılmasıyla oluşan vadeler şu şekildedir; "Vadelere Bölme" sekmesinde, vade günleri listesi üzerinde herhangi bir değişiklik yapılamaz. Koşul uygulamasının olduğu fakat koşula bağlı ödeme planının olmadığı durumlarda, "Koşul Bilgileri" sekmesinde bulunan "Ödeme Kodu" alanına istenilen ödeme planının kodunun girilmesi mümkündür.

![](../../../../_assets/bce70150f9d8717e7d9d.png)

**Koşul Bağlantısız Cari Ödeme Planı**

Eğer koşul uygulaması kullanılmıyorsa ödeme kodu bu kez sipariş, irsaliye ve fatura kayıtlarının "Üst Bilgiler" sekmesinde sorgulanır.

![](../../../../_assets/6993a2b6b682c56be5a8.png)

Eğer cari hesabın sabit kartında bulunan "Ödeme Kodu" alanına herhangi bir ödeme planının kodu girilirse, faturada cari kod girildiğinde cari hesabın sabit kartındaki ödeme kodu program tarafından faturaya otomatik olarak aktarılır. Faturanın "Üst Bilgiler" sekmesine getirilen "Ödeme Kodu" kullanıcı tarafından değiştirilebilir. Ayrıca, cari sabit kartta "Ödeme Kodu" girilmeden, faturada ilgili cari için "Ödeme Kodu" girişi yapılması mümkündür.

![](../../../../_assets/f6fb01b0fab921ac4b78.png)

Koşul bağlantılı ödeme planında olduğu gibi, faturanın "Üst Bilgiler" sekmesinde girilen ödeme koduna göre oluşan genel toplam, vadelere bölünerek cari hareketlere ayrı bir kayıt olarak aktarılır.

Müşteri siparişi girilirken "Ödeme Kodu" belirtildiyse, sipariş irsaliye veya fatura olarak kaydedilirken siparişte girilen "Ödeme Kodu" yeni yapılan kayda aktarılır. "Ödeme Kodu" kullanıcı tarafından değiştirilebilir.

Eğer faturada ödeme planı bağlantısı olan bir koşul girildiyse, ayrıca cari hesabın sabit kartında da koşuldaki koddan farklı bir ödeme kodu varsa, koşul ile bağlanmış ödeme koduna göre vade hesaplaması program tarafından otomatik olarak yapılır.
