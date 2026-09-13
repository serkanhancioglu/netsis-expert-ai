---
title: "Görsel Dizayn ve Görsel Rapor Tasarımlarımda Cross-Tab Kullanımı"
page_id: "128583298"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Görsel Dizayn ve Görsel Rapor Tasarımlarımda Cross-Tab Kullanımı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Görsel Dizayn ve Görsel Rapor Tasarımlarımda Cross-Tab Kullanımı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTFkMzI3MzU0LWU4ODYtNDRkYy05OWY4LWUyYzk1OTQxODMxNCZsaW5rPWFlMmJjNTU1LWNjOGItNDZhOC1hYTM0LTNiYThlNmM4MTUyMiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=1d327354-e886-44dc-99f8-e2c959418314&link=ae2bc555-cc8b-46a8-aa34-3ba8e6c81522&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "gorsel-dizayn-ve-gorsel-rapor-tasarimlarimda-cross-tab-kullanimi_128583299_128583298.html"
source_version: "2023-12-25T11:07:22.407+03:00"
source_bytes: 821385
fetched_at: "2026-09-13T04:23:02+00:00"
generator: "netsis-scraper 1.0.0"
---
# Görsel Dizayn ve Görsel Rapor Tasarımlarımda Cross-Tab Kullanımı

Görsel Dizayn ve Görsel Rapor Tasarımlarımda Cross-Tab Kullanımı hakkında ayrıntılı bilgiye bu dokümandan ulaşılır.

Cross-Tab (Çapraz Tablo), verilerin daha özet ve anlamlı olarak gösterilmesini sağlayan bir raporlama aracıdır. Büyük veri setlerinin sadeleştirilerek analiz edilmesi ve yorumlanmasını kolaylaştırır.

Cross-Tab özelliği kullanılarak oluşturulan raporlarda veriler satır ve sütunlar halinde gruplanarak, grup bazında toplam değerlerin gösterimi gerçekleştirilebilir. Bu sayede, karmaşık veri setlerinin daha anlaşılır hale getirilmesi sağlanır.

Bu doküman; esnek yapılandırma uygulaması kullanılarak müşteri siparişinde girilen stok kalemlerine ait varyasyonların, sipariş dizaynında Cross-tab ile gösteriminin sağlanmasına yönelik işlem adımlarını içermektedir.

Müşteri siparişine eklenen sipariş kalem bilgileri aşağıdaki gibidir.

![](../_assets/c58145abaf08db379468.png)

Sipariş formunda ürün özellik ve miktar bilgilerinin aşağıdaki gibi gösterilmesi amaçlanmaktadır.

![](../_assets/5e6fd1247e70bc3b4416.png)

Dizayn ön izlemesinde üst, kalem ve toplam bilgilerini içerecek veri tabanı nesnesinin yanı sıra yapılandırma kodu bazında miktar ve özellik bilgilerinin gösterimi için ayrı bir veri tabanı nesnesi oluşturularak "Dizayn Kayıtları" ekranından Dizayn Data nesnesi olarak eklenmelidir.
![](../_assets/315779fdfc6fc5f658f8.png)
Cross-tab ile gösterilecek ürün özellik ve miktar verilerinin, "SIPARISDZNURUN" isimli view ile dizayna getirilmesi sağlanmıştır.

Veri tabanı nesnesinde kullanılan SQL sorgusu aşağıdaki gibidir.

SELECT YAPKOD,FTIRSIP,CARI_KODU,FATIRS_NO,
MAX(CASE WHEN RN = 1 THEN OZELLIK END) AS BEDEN,
MAX(CASE WHEN RN = 2 THEN OZELLIK END) AS RENK,
MAX(CASE WHEN RN = 1 THEN MIKTAR END) AS MIKTAR
FROM (
SELECT \*,
ROW_NUMBER() OVER (PARTITION BY YAPKOD ORDER BY OZELLIK) AS RN
FROM (
SELECT
S.YAPKOD,
T.DEGERKOD AS OZELLIK,
S.STHAR_GCMIK AS MIKTAR,
S.FISNO AS FATIRS_NO,
S.STHAR_ACIKLAMA AS CARI_KODU,
S.STHAR_FTIRSIP AS FTIRSIP
FROM TBLSIPATRA AS S
CROSS APPLY (
SELECT \*
FROM TBLESNYAPTRA AS T
WHERE S.YAPKOD = T.YAPKOD
) AS T
) AS Y
) AS T
GROUP BY YAPKOD,FTIRSIP,CARI_KODU,FATIRS_NO
Cross-Tab içinde kullanılacak veri kümesi aşağıdaki gibidir.
![](../_assets/5f5efb5df58a05394ad4.png)
Dizayn tasarım ekranı açılarak *"Object Toolbar"* bölümünden ![](../_assets/994626f5a72b751f3248.png) **(DB Cross-tab object)** bileşeni form tasarımına eklenir. Bileşen üzerinde çift tıklanarak **"Cross-tab Editor"** ekranı açılır ve **"source data"** alanından veri seti için kullanılacak data nesnesinin seçimi yapılır. Ardından, sütun, satır ve değer olarak gösterilmek istenen alanlar *sürükle-bırak* yöntemi ile ilgili alanlara taşınır.
![](../_assets/90fcef61f0454c424b12.png)
Satır ve sütun sonlarında toplam değerinin otomatik hesaplanması için **"column grand total"** ve **"row grand total"** seçenekleri işaretlenir. Oluşturulan tablo, dizaynda istenen bölüme konumlandırılır.
![](../_assets/448b7766798611edbff6.png)
Oluşturulan dizaynın baskı ön izlemesi aşağıdaki gibidir.
![](../_assets/e27f2eece12c1b6ee1f9.png)
