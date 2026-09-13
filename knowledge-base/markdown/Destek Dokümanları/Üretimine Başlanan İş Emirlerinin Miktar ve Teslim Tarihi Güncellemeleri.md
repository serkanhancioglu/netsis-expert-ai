---
title: "Üretimine Başlanan İş Emirlerinin Miktar ve Teslim Tarihi Güncellemeleri"
page_id: "50669080"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Üretimine Başlanan İş Emirlerinin Miktar ve Teslim Tarihi Güncellemeleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Üretimine Başlanan İş Emirlerinin Miktar ve Teslim Tarihi Güncellemeleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWM5YTViODljLWY0YWEtNGY5My1iN2VjLTVlNTZhMTlhNDYzOCZsaW5rPWIzZDJhZDQ4LWVhNjMtNDkzMi05ZTg0LTRlOTAzZjkxNDU1YiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=c9a5b89c-f4aa-4f93-b7ec-5e56a19a4638&link=b3d2ad48-ea63-4932-9e84-4e903f91455b&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "uretimine-baslanan-is-emirlerinin-miktar-ve-teslim-tarihi-guncellemeleri_50669086_50669080.html"
source_version: "2022-11-03T09:04:32.223+03:00"
source_bytes: 44816
fetched_at: "2026-09-13T04:25:35+00:00"
generator: "netsis-scraper 1.0.0"
---
# Üretimine Başlanan İş Emirlerinin Miktar ve Teslim Tarihi Güncellemeleri

Üretimine Başlanan İş Emirlerinin Miktar ve Teslim Tarihi Güncellemeleri ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

MRP, bazı parametrelerle mevcut iş emirleri üzerinde miktar ve/veya tarih güncellemeleri önerebilir. Üretimine başlanan iş emirleri için MRP'nin güncelleme yapmaması sağlanabilir.![](../_assets/45b12f7668bf2c1429c8.png)

Üretim Parametreleri ekranına eklenen "Rezervasyon/UAK/USK Varsa İş Emri Teslim Tarihi Değiştirilemesin" parametresi ile; iş emrine ait herhangi bir rezervasyon yapılmışsa ve UAK ya da USK kaydı girilmişse, artık bu iş emrinin teslim tarihi MRP tarafından ya da kullanıcılar tarafından elle (Manuel) **değiştirilemez.**

İş Emri Miktar Güncelleme Politikası altında iki adet seçenek bulunur:

Rezervasyon/UAK/USK Varsa Miktar Değiştirilmesin: İş emrine ait herhangi bir rezervasyon yapılmışsa ve UAK ya da USK kaydı girilmişse, artık bu iş emrinin miktarı MRP tarafından ya da kullanıcılar tarafından elle (Manuel) değiştirilemez.
Rezervasyon/UAK/USK Miktarının Altına Düşülemesin: İş emrine ait herhangi bir rezervasyon yapılmışsa ve UAK ya da USK kaydı girilmişse, artık bu iş emrinin miktarı MRP tarafından ya da kullanıcılar tarafından, rezervasyon yapılan set miktarı, UAK miktarı ve USK miktarı arasında en büyük olanın altına düşürülemez.

MRP miktar değişikliği önerileri için yukarıdaki parametrelere göre davranır. Ancak, iş emri ihtiyacı tamamen ortadan kalkmışsa ilgili iş emrini kapatma önerisi getirir.

MRP'nin UAK kaydı olan iş emirlerine kapatma önerisi getirmemesi için aşağıdaki özel parametrenin tanımlanması gerekir:

Grup Kodu: MRP

Anahtar: ISEMRIUAKLIMIKTARKAPANMASIN

Değer: 1
