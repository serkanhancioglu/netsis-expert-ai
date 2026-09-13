---
title: "Toplu Şifre Değişikliği"
page_id: "134054755"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Toplu Şifre Değişikliği"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Toplu Şifre Değişikliği"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTM3ZDVmYzkzLWMxZGUtNGM2YS1iNzFjLTFkYjQ2ZjZiMmVlNSZsaW5rPTgxZTliZjMyLTMxODgtNDI1ZC05NzkzLThiNjhjNWY4YzE3NiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=37d5fc93-c1de-4c6a-b71c-1db46f6b2ee5&link=81e9bf32-3188-425d-9793-8b68c5f8c176&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "toplu-sifre-degisikligi_134054755_134054755.html"
source_version: "2024-02-16T16:19:03.103+03:00"
source_bytes: 369868
fetched_at: "2026-09-13T04:23:09+00:00"
generator: "netsis-scraper 1.0.0"
---
# Toplu Şifre Değişikliği

9.0.46 sürümü ile entegratör üzerinde yapılan şifre değişikliğinin "e-Fatura Ayarlar" ekranında ilgili vergi numarasına ait şifre değişikliğinin tüm makineler için topluca yapılabilmesi desteklenmiştir. İlgili menüye Netsis'in kurulu olduğu dizindeki Servis klasörü içerisinde yer alan EFaturaAyarlar.exe çalıştırılıp İşlemler menüsü altında "Toplu Şifre Değişikliği" seçilerek ulaşılabilir.

![](../_assets/2309cbf08f9bc12aa621.png)

Açılan ekranda girilen vergi numarasına ait şifrenin tüm makinelerde topluca değiştirilmesini sağlayan bu işlem ayrıca şube bazında detaylandır seçeneği ile aynı vergi numarası ile başlayan diğer şube tanımlamaları için de toplu olarak şifrelerinin güncellenmesini sağlamaktadır. Yapılan şifre değişiklikleri NETSIS veri tabanı altında yer alan TBLEIMZAREG tablosundaki INTEGRATOR_PASSWORD ve S_YEDEK1 alanlarında güncellenir.

![](../_assets/78c07bb3c72318853204.png)
![](../_assets/8bd35dce1dd6edf31575.png)
