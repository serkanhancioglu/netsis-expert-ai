---
title: "Sayımdan Devir İşleme"
page_id: "22803758"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Stok"
  - "İşlemler / Stok"
  - "Stok Sayım İşlemleri"
  - "Sayımdan Devir İşleme"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Stok / İşlemler / Stok / Stok Sayım İşlemleri / Sayımdan Devir İşleme"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWYxODFjMmNhLWZhNWMtNDIyYS1hMTdlLTA3OTNjNjdlMDVlNiZsaW5rPTc1M2YzNWEwLWIzNDgtNDcwOS1hNGUwLTU1ODA5MDI0YzFhMCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=f181c2ca-fa5c-422a-a17e-0793c67e05e6&link=753f35a0-b348-4709-a4e0-55809024c1a0&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "sayimdan-devir-isleme_29996913_22803758.html"
source_version: "2022-10-26T10:01:03.397+03:00"
source_bytes: 20394
fetched_at: "2026-09-13T04:04:42+00:00"
generator: "netsis-scraper 1.0.0"
---
# Sayımdan Devir İşleme

Sayımdan Devir İşleme, Lojistik - Satış Bölümü'nde, "İşlemler/Stok " menüsünün altında yer alır. Sayımdan Devir İşleme, "Sayım Girişi" bölümünden oluşturulan kayıtların, oluşacak ya da var olan farklı bir şirketin stok hareketlerine, istenen tarih ve istenen maliyet türü ile "DEVİR" olarak aktarılmasını sağlayan bölümdür.

Sayımdan Devir İşleme bölümü, özellikle sene sonlarında girilen sayım miktarlarının bir sonraki sene için oluşturulan şirket koduna devir girişi olarak aktarılması için kullanılır. Program, Dövizli muhasebe kullanıldığında, bakiye kapatma satırlarını işlerken birim döviz maliyetini de bulur ve operasyon döviz tutarına aktarır. Bu işlem sırasında, döviz tipi olarak tanımlanan firma döviz tipini kullanır. Birim döviz maliyetini hesaplarken, girilen tarih aralığında stok hareket kayıtlarındaki firma döviz tutarlarından faydalanır. Dolayısıyla, Sayımdan Devir İşleme işleminden önce firma döviz tutarlarının oluşması için önceden Stok → İşlemler → [Stok Döviz Çevrim](<../Stok Döviz Çevrim.md>) bölümünün çalıştırılması gerekir.

Sayımdan Devir İşleme ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Sayımdan Devir İşleme Ekranı |  |
| --- | --- |
| Sayım Tarihi | Sayım Girişi/ Lokal Depo Sayım Girişi bölümünden girilen stokların sayım tarihinin girildiği alandır. Bu alana sayım bilgisi olmayan herhangi bir tarihin girilmemesi gerekir. |
| Depo Kodu Aralığı | Sayım bilgisinin lokal depo bazında girilmesi halinde kullanılan alandır. Lokal depo kodu aralığı verilmesi halinde, sadece o lokal depoya/depolara ait devir aktarılır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, depo kodları arasından seçim yapılır. |
| Cari Kodu | Lokal depoları cari koda bağlantılı olarak (örneğin; satış noktaları bazında) tanımlayan firmaların kullandığı alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, cari kodlar arasından seçim yapılır. |
| Devir Tarihi | Sayımdan devir işlenmesi amacıyla devir tarihi girilen alandır. |
| Maliyet İçin Sınır Tarihi | Sayım miktar devri yapılırken, birim fiyat ve maliyet tutarlarının hesaplanacağı sınır tarihin girildiği alandır. |
| Maliyet Muhasebesi Devri | Maliyet muhasebesi devri yapılması istendiğinde işaretlenmesi gereken seçenektir. |
| Maliyet Türü | Sayım miktar devri yapılırken, birim fiyatı ve maliyet tutarlarının hesaplanacağı maliyet tipinin seçildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile, maliyet tipleri arasından seçim yapılır. "Maliyet Muhasebesi Devri" seçeneği işaretli olduğunda, "Maliyet Türü" alanı pasif hale gelir. |
| Devrin Oluşturulacağı Şirket | Devrin oluşturulacağı şirket isminin girildiği alandır. |
| Sıfır Maliyetle Hangi Fiyat | Sıfır maliyetle son giriş fiyatı veya alış fiyatı seçenekleri arasından seçim yapılan alandır. |
| Proje Kodu (Başlangıç) | Sayımdan devir işlenmesi amacıyla, başlangıç proje kodunun girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, proje kodları arasından seçim yapılır. |
| Proje Kodu (Bitiş) | Sayımdan devir işlenmesi, bitiş proje kodunun girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, proje kodları arasından seçim yapılır. |
| ![](../../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilginin onaylanmasını sağlayan butondur. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgiden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
