---
title: "Hesap Planı Aktarımı"
page_id: "24740646"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Muhasebe"
  - "Muhasebe Modülü"
  - "İşlemler / Muhasebe"
  - "Sisteme Veri Aktarımı"
  - "Hesap Planı Aktarımı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / İşlemler / Muhasebe / Sisteme Veri Aktarımı / Hesap Planı Aktarımı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTQ4OGNkMTE0LWEzNGMtNDkzZi05OWZmLTkyMjk5NDBhNDA5MSZsaW5rPTFlNjNjNWY3LWNlNDQtNGFjNS1iODA5LTNjMzYxMDM4Nzc2ZCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=488cd114-a34c-493f-99ff-9229940a4091&link=1e63c5f7-ce44-4ac5-b809-3c361038776d&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "hesap-plani-aktarimi_41157749_24740646.html"
source_version: "2022-10-06T12:56:45.313+03:00"
source_bytes: 29658
fetched_at: "2026-09-13T04:13:34+00:00"
generator: "netsis-scraper 1.0.0"
---
# Hesap Planı Aktarımı

Hesap Planı Aktarımı, Muhasebe Bölümünde, "İşlemler/Muhasebe Modülü" menüsünün altında yer alır. Hesap Planı Aktarımı, daha önce kullanıcı tarafından oluşturulan TXT dosyasından, hesap planı kayıtlarına aktarım yapılmasını sağlayan bölümdür.

![](../../../../../_assets/b947a3abd328b9861b87.png)

Hesap Planı Aktarımı ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Hesap Planı Aktarımı Ekranı |  |
| --- | --- |
| Dosya İsmi | Aktarılacak dosyanın bulunduğu dizin ve ismin tanımlandığı alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, dosyalar arasından seçim yapılır. |
| İşletmelerde Ortak | Aktarımın yapılacağı işletmenin belirlendiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, işletmeler arasından seçim yapılır. |
| Şubelerde Ortak | Aktarımın yapılacağı şubenin belirlendiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, şubeler arasından seçim yapılır. Aktarım yapılacak TXT dosya yapısının belli bir düzene göre hazırlanması gerekir. İlk 3 satır başlık bilgisi olarak aşağıdaki gibi olmalıdır: 1.satır str(4) PLAN 2.satır str(35) Aktarımı yapılacak TXT dosyaya özel olmalı. Ayrıca her aktarım için tekil olmalı. (Text id) 3.satır number(5,0) Kaç adet kayıt olduğu gönderilmeli (kontrol açısından gerekli). Diğer bilgi satırı yapısı: ```text<br>Hesap Kodu str(35)<br>``` ```text<br>Hesap Türü (A Ana G Grup M Muavin) char(1)<br>``` ```text<br>Hesap İsmi str(50)<br>``` ```text<br>Yabancı Hesap İsmi str(50)<br>``` ```text<br>Hesap Grup Kodu str(8)<br>``` Hesap Tipi (A Aktif P Pasif) ```text<br>G Gelir I Gider N Nazım char(1)<br>``` ```text<br>Çalışma Tipi (B Borç A Alacak) char(1)<br>``` ```text<br>Düzeltilecek Hesap (E Evet H Hayır) char(1)<br>``` ```text<br>Parasal Hesap (E Evet H Hayır) char(1)<br>``` Hesaplama Türü (K Kayıt Tarihi) O (Ortalama Kur) ```text<br>V (Verilen Tarih) char(1)<br>``` |
| ![](../../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilginin onaylanmasını sağlayan butondur. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgiden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
