---
title: "Ödeme Emri Entegrasyonu"
page_id: "22805246"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Cari"
  - "İşlemler / Cari"
  - "Ödeme Emirleri"
  - "Ödeme Emri Entegrasyonu"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Cari / İşlemler / Cari / Ödeme Emirleri / Ödeme Emri Entegrasyonu"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWUzOGYzMGEzLWM4NmQtNGUxNy1iOWNmLTRmZGMzZDNiY2FlNCZsaW5rPTEzMWYxNzMxLWMwZmYtNDkxOS05MmU1LWE1MDAwMWVkZmNkYiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=e38f30a3-c86d-4e17-b9cf-4fdc3d3bcae4&link=131f1731-c0ff-4919-92e5-a50001edfcdb&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "odeme-emri-entegrasyonu_29985462_22805246.html"
source_version: "2022-10-31T11:32:05.560+03:00"
source_bytes: 11094
fetched_at: "2026-09-13T04:08:06+00:00"
generator: "netsis-scraper 1.0.0"
---
# Ödeme Emri Entegrasyonu

Ödeme Emri Entegrasyonu işlemi, Finans Bölümü'nde İşlemler/Cari menüsünün altında yer alır. Ödeme Emri Entegrasyonu, oluşturulan ödeme emirlerinin listelerinin alınması ve kontrolünden sonra muhasebe entegrasyonunun yapılmasını sağlayan bölümdür. Ödeme Emri Entegrasyonu ile Entegre edilen kayıtlar, Entegrasyon Modülü - Kayıt - Entegrasyon Kayıtları - Dekont sekmesine aktarılır. Ödeme emirlerinin mahsup kayıtları, satıcılar ve bankaların cari sabit bilgilerindeki muhasebe kodu alanlarından okunarak oluşturulur.

Ödeme Emri Entegrasyonu ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Ödeme Emri Entegrasyonu Ekranı |  |
| --- | --- |
| Tarih | Ödeme emri entegrasyonu için tarih girilen alandır. Programdaki tarih, otomatik olarak ekrana gelir. |
| Havale/Çek/Hepsi | Bu bölümde, havale ve borç çeki ödemeleri tek tek yapılabileceği gibi "Hepsi" seçeneği ile her iki ödemede de gerçekleşebilir. Ödeme emirlerinin entegrasyonunda, bankanın ve borç çeklerinin cari hareket kayıtlarına alacak, satıcının cari hareket kayıtlarına ise borç kaydı işlenir. Bunun dışında, borç çeki ödemeleri için satıcılara ciro edilen borç çekleri, "Borç Çekleri" modülünde oluşturulur. Ödeme emirleri entegrasyonu tamamlandığında herhangi bir sorun çıkarsa, program ODEMEENT.ERR dosyası oluşturur. Bu dosya incelenerek hatanın nereden kaynaklandığı bulunabilir. |
| Satıcı Hareketlerine Detaylı İşlensin | Bu alan işaretlenerek "Ödeme Emirleri Entegrasyonu" yapıldığında, satıcının cari hareket kayıtlarında oluşacak borç hareketi, her bir alacak kaydına karşılık ayrı bir satır olarak işlenir. işaretlenmeden işlem yapıldığında, cari hesaba ait tüm alacakların toplamı kadar tek bir satır borç hareketi işlenir. |
| Şubeler Dahil Edilsin | "Ödeme Emri Entegrasyon" işlemine tüm şubelerin dahil edilmesi istendiğinde işaretlenmesi gereken seçenektir. |
| Havale Banka Kodu | Entegrasyona aktarılacak ödeme emirleri için havale banka kodu kısıdı verilen alandır. Burada girilen havale banka koduna ait ödeme emirleri entegrasyona aktarılır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, kodlar arasından seçim yapılır. |
| ![](../../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Ödeme emri entegrasyonu için verilen kısıtların onaylanması için kullanılan butondur. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) İptal | Ödeme emri entegrasyonu için verilen kısıtlardan vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
