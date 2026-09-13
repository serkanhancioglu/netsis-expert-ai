---
title: "Özel Kod - 1 Tanımlama"
page_id: "24763165"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Fatura"
  - "İşlemler / Fatura"
  - "Özel Kod - 1 Tanımlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Fatura / İşlemler / Fatura / Özel Kod - 1 Tanımlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTUzZWQ2ZWM0LTRmNGEtNDBlOC1iZGFlLWZmNzdhYzM3Y2VhZSZsaW5rPTZhMzQ4ZDIzLTk0OWItNDdlMS1hNzBhLTYwZDk1ZTY4ZDg1NCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=53ed6ec4-4f4a-40e8-bdae-ff77ac37ceae&link=6a348d23-949b-47e1-a70a-60d95e68d854&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ozel-kod-1-tanimlama_24763186_24763165.html"
source_version: "2022-10-24T09:26:58.307+03:00"
source_bytes: 5467
fetched_at: "2026-09-13T04:02:37+00:00"
generator: "netsis-scraper 1.0.0"
---
# Özel Kod - 1 Tanımlama

Özel Kod-1 Tanımlama, Lojistik-Satış Bölümü'nde, "İşlemler/Fatura" menüsünün altında yer alır.

Özel Kod-1 Tanımlama, Satış parametrelerinde Özel Kod-1 parametresini işaretleyerek işlem yapan firmaların, Kod-1 tanımlamalarını kaydedecekleri bölümdür. Özel Kod-1 bölümünden kaydedilen Kod-1 tanımlamalarının fatura modülü işlemlerinde kullanılabilmesi için, [Satış Fatura parametrelerindeki](<../Kayıt - Fatura/Satış Parametreleri.md>) “Özel Kod1 değeri tablodan kontrol edilsin “ parametresinin işaretlenmiş olması gerekir. Böylece, girilen Kod-1 değerinin bu bölümde kayıtlı olup olmadığı program tarafından kontrol edilir ve kayıtlı olmayan Kod-1 değeri kullanılmaz. Girilen Kod-1 değerine göre belirlenmiş olan fiyat satış fiyatı olarak getirilir.

Özel Kod-1 Tanımlama ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Özel Kod-1 Tanımlama Ekranı |  |
| --- | --- |
| Kod | Kullanılacak Kod-1 değerinin girildiği alandır. En fazla bir karakterlik Kod-1 değeri girilir. |
| Açıklama | Girilen Kod-1 değerinin açıklamasının kaydedildiği alandır. |
| Fiyat Tipi 1,2,3,4 | İlgili Kod-1 değeri için girilmesi gereken fiyat tipidir. Satış işlemlerinde girilen Kod-1 değerine göre burada belirlenen satış fiyatı, stok kartlarından aktarılır. |
| Hesap Kodu | Özel Kod-1 kullanılarak kesilen faturalarda, satış hesaplarının istenilen muhasebe hesabına aktarılması için “muhasebe kodu” alanı kullanılır. Girilen muhasebe hesabının dikkate alınması için , Entegrasyon Modülü → Entegrasyon Kodlarında yer alan “Özel Kod-1 ile satış hesapları değişsin” parametresinin işaretlenmesi gerekir. Böylece, Özel Kod-1 girilerek kesilen faturalardaki satış hesabı, bu alana girilen muhasebe hesabı ile çalışır. ![](../../../../_assets/088477bb321d1b20c939.jpg) Rehber butonu yardımı ile hesap kodları arasından seçim yapılır. |
