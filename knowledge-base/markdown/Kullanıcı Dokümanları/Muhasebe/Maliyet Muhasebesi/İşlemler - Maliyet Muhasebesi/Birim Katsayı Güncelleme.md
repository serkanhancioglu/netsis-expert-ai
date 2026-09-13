---
title: "Birim Katsayı Güncelleme"
page_id: "24752263"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Muhasebe"
  - "Maliyet Muhasebesi"
  - "İşlemler / Maliyet Muhasebesi"
  - "Birim Katsayı Güncelleme"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Maliyet Muhasebesi / İşlemler / Maliyet Muhasebesi / Birim Katsayı Güncelleme"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTM0NDliNWQ2LWUzODctNDIyNC1hM2Q4LWJmYjM0MTU0NGI4MiZsaW5rPTFjMzM3YWRlLWUxZWMtNDFmZS05MTk4LTU1ODQxMDM2M2YzMCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=3449b5d6-e387-4224-a3d8-bfb341544b82&link=1c337ade-e1ec-41fe-9198-558410363f30&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "birim-katsayi-guncelleme_50677340_24752263.html"
source_version: "2022-10-18T10:36:51.050+03:00"
source_bytes: 13694
fetched_at: "2026-09-13T04:15:05+00:00"
generator: "netsis-scraper 1.0.0"
---
# Birim Katsayı Güncelleme

Birim Katsayı Güncelleme, Muhasebe Bölümü'nde, "İşlemler/Maliyet Muhasebesi Modülü" menüsünün altında yer alır. Birim Katsayı Güncelleme, Birim Katsayı Hesaplama İşlem Verisi alanından seçilecek işlem tipine göre, mamul grupları ve gider tipleri için otomatik olarak birim katsayılarının toplu şekilde hesaplanmasını sağlayan bölümdür. Böylece, Mamul Grup Kayıtları ekranındaki birim katsayıların güncellenmesi sağlanır.

Üretim Akış Kontrol modülünden elde edilen üretim süreleri, reçetelerdeki üretim süreleri veya çizelgeleme tanımlarındaki üretim süreleri kullanılarak birim katsayı hesaplaması yapılabilir. Bu ekranın ana amacı, mamul grupları bazında birim üretim sürelerini hesaplamak ve bu süreleri, verilen tarih aralığında mamul ana grubu altında üretilmiş ürünlerin toplam üretim süresine oranlayarak 0-1 arasında birim katsayısı hesaplamaktır.

Birim Katsayı Güncelleme ekranı; Hesaplama ve Hesaplama Sonuçları olmak üzere iki sekmeden oluşur.

**Hesaplama**

Birim Katsayı Güncelleme ekranı Hesaplama sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Birim Katsayı Güncelleme Ekranı |  |
| --- | --- |
| Birim Katsayı Hesaplama Verisi | Birim katsayılarının güncelleneceği hesaplama verisinin seçildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile seçim yapılır. **Üretim Akış Kontrol** seçilirse; Üretim Akış Kontrol modülünden girilen kayıtlar kullanılarak mamul grupları için birim üretim süreleri hesaplanır. **Reçete** seçilirse; mamul grupları için reçetelerdeki operasyonların üretim süreleri kullanılarak birim üretim süreleri hesaplanır. **Çizelgeleme** seçilirse; mamul grupları için çizelgeleme uygulamasında yapılan operasyon-makine eşleşmelerindeki üretim süreleri kullanılarak birim üretim süreleri hesaplanır. |
| UAK Tarih Aralığı | Hesaplama verisi olarak “Üretim Akış Kontrolden Getirilsin” seçildiğinde aktif hale gelen alandır. Hesaplama sırasında kullanılacak üretim akış kontrol kayıtlarının tarih aralığını filtrelemek için kullanılır. |
| Mamul Ana Grup Kodu Aralığı | Birim katsayı hesabının yapılacağı mamul ana grubu için kısıt verilen alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, grup kodları arasından seçim yapılır. |
| Güncellenecek Gider Hesapları | Birim katsayılarının güncelleneceği gider hesaplarının seçildiği alandır. Hammadde, İşçilik, Enerji, Amortisman, Yardımcı Servis, Yedek Parça, Ambalaj, 5. Gider Tanımı ve belirlenen gider tipleri arasından seçim yapılır. |
| ![](../../../../_assets/033e3e50bbe25f98d5da.png) Hesapla | Girilen kısıtlamalar doğrultusunda hesaplama yapılması için kullanılan butondur. |

**Hesaplama Sonuçları**

Hesaplama sonuçlarının yer aldığı sekmedir. Sonuçlar Excel'e Gönder ![](../../../../_assets/b4b759f688e3cd4bf447.png) butonu ile Excel'e gönderilebilir, Excel'den Netsis'e aktarım için- Excel'den Yükle ![](../../../../_assets/bc1d3aed39ece0978cdd.png)butonu kullanılır. Birim katsayılarının güncellenmesi için de, Kaydet ![](../../../../_assets/7c1ed84f54082c570a92.png)butonuna tıklanması gerekir.

Mamul grupları için hesaplanan yeni birim katsayılar “Yeni Değer” kolonunda görülür. Mamul grubu için giderler bazında daha önce tanımlı olan birim katsayılar da ayrı kolonlarda - işçilik, enerji gibi - raporlanır. "Yeni Değer" kolonundaki birim katsayılar grid üzerinden değiştirilebilir. Eğer ilgili mamul ana grubunun gider hesabının dağıtım anahtarı “Birim Katsayılar Oranı” değilse, bu satırlar için birim katsayılar güncellenmez ve ekranda pasif olarak görünür.

**Örnek Uygulama**

Preshane mamul ana grubu altında aşağıdaki mamul gruplarına ait üretim akış kontrol kayıtlarından elde edilen birim üretim süreleri görülür:

```text
Mamul Grup Kodu                       Birim Üretim SüresiYARIMAMUL1                                15 snYARIMAMUL2                                25 snYARIMAMUL3                                30 sn
```

Mamul grubuna ait birim katsayı hesabında aşağıdaki formül kullanılır:

Birim Katsayı = Mamul Grubunun Birim Üretim Süresi ÷ Mamul Ana Grubunda Üretilen Bütün Ürünlerin Toplam Üretim Süresi

Bu örnek için mamul gruplarının birim katsayı hesapları aşağıdaki şekildedir:

```text
Mamul Grup Kodu                      Birim Üretim SüresiYARIMAMUL1                               15/(15+25+30) = 15/70 = 0.2143YARIMAMUL2                               25/(15+25+30) = 25/70 = 0.3571YARIMAMUL3                               30/(15+25+30) = 30/70 = 0.4286
```
