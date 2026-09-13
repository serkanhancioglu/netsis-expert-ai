---
title: "Lokal Depo Bazında Maliyet Mahsubu"
page_id: "22803730"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Stok"
  - "Kayıt / Stok"
  - "Lokal Depo İşlemleri"
  - "Lokal Depo Bazında Maliyet Mahsubu"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Stok / Kayıt / Stok / Lokal Depo İşlemleri / Lokal Depo Bazında Maliyet Mahsubu"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWJjNGY1ZTIyLTk5NjYtNDYzNi05N2I1LTIzM2Y2OTM5YTdlNSZsaW5rPWQzMmIyOGRiLTkzMjctNDM3YS1iOGMwLWQ4MDFkMTU1MjIxNyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=bc4f5e22-9966-4636-97b5-233f6939a7e5&link=d32b28db-9327-437a-b8c0-d801d1552217&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "lokal-depo-bazinda-maliyet-mahsubu_29994395_22803730.html"
source_version: "2022-10-25T20:31:27.380+03:00"
source_bytes: 11669
fetched_at: "2026-09-13T04:04:14+00:00"
generator: "netsis-scraper 1.0.0"
---
# Lokal Depo Bazında Maliyet Mahsubu

Lokal Depo Bazında Maliyet Mahsubu, Lojistik - Satış Bölümü'nde, "Kayıt/Stok" menüsünün altında yer alır. Lokal Depo Bazında Maliyet Mahsubu, "Maliyet Muhasebesi Modülü" kullanılıp, stoklarını lokal depo bazında takip eden firmaların mal miktarlarının muhasebede takip edilmesi ve görülmesi için kullanılan bölümdür. Lokal Depo Bazında Maliyet Mahsubu bölümünün kullanılması ile muhasebede 150 hesaplarda toplam olarak izlenen mal miktarları, lokal depo bazında ayrı ayrı izlenebilir.

Lokal depolarda bulunan mal miktarlarının muhasebeye entegre edilmesi için bazı ön hazırlıkların yapılması gerekir. Öncelikle, lokal depolar bazında açılacak olan muhasebe kodları için "Cari Modülde" kod açılması gerekir. Açılan cari kodların "Muhasebe Kodu" alanlarına, muhasebede ilgili lokal depo için tanımlanan kod girilir. Daha sonra, "Lokal Depo Tanımlama" bölümünde lokal depo için açılan cari kod, "Cari Kodu" alanına girilir.

Lokal depo bazında maliyet mahsubunu çalıştırmadan önce, Stok → İşlemler → “Maliyet Oluşturma” bölümünün çalıştırılması gerekir. Maliyet oluşturma ile, stok kartlarının ağırlıklı ortalamaya göre toplam maliyetlerinin bulunması sağlanır. Daha sonra lokal depo bazında maliyet mahsubu bölümü çalıştırılır.

Lokal depo bazında maliyet mahsubunun oluşturulması için; Yardımcı Programlar → Kayıt → [Şirket-Şube Parametreleri](<../../../../Muhasebe/Muhasebe Modülü/Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/Genel Tanımlar/Yardımcı Programlar-Şirket-Şube Parametreleri.md>) → "Proje Uygulaması" parametresinin işaretlenmesi gerekir.

Proje Uygulaması ile ilgili detaylı bilgi için; Muhasebe → Kayıt → [Proje Sabit Tanımları](<../../../../Muhasebe/Muhasebe Modülü/Kayıt - Muhasebe/Proje Kodu Girişi/Proje Sabit Tanımları.md>) dokümanına bakılabilir.

Lokal Depo Bazında Maliyet Mahsubu ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Lokal Depo Bazında Maliyet Mahsubu Ekranı |  |
| --- | --- |
| Sınır Tarihi | İşlemler için sınır tarihinin belirlendiği alandır. Girilen sınır tarihine kadar her lokal deponun bakiyesi bulunarak, stok kartlarındaki maliyet fiyatıyla çarpılır ve toplam depo maliyeti bulunur. İşlem sonucunda, stok detay kodlarında yazılı olan alış hesaplarına alacak, "Lokal Depo Tanımlama" bölümünde girilen cari kodda yazılan muhasebe koduna ise borç hareketi işlenir. |
| Stok Grup Kodu | Lokal depo bazında maliyet mahsubu için stok grup kodunun girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, kodlar arasından seçim yapılır. |
| ![](../../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilgilerin kaydedilmesi için kullanılan butondur. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerden vazgeçilmesi halinde, ekrandan çıkmak için kullanılan butondur. |
