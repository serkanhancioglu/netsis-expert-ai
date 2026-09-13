---
title: "Yevmiye Fişi Aktarımı"
page_id: "24740649"
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
  - "Yevmiye Fişi Aktarımı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / İşlemler / Muhasebe / Sisteme Veri Aktarımı / Yevmiye Fişi Aktarımı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTZlYTM3Y2RmLTRjYTgtNDk4My04ZjBlLTM4YmQyNzBiMzQ2YSZsaW5rPWJlOTAzYTkwLTUwZmQtNDlhNy1hNmMzLTBkOTcwZmRjODZiNiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=6ea37cdf-4ca8-4983-8f0e-38bd270b346a&link=be903a90-50fd-49a7-a6c3-0d970fdc86b6&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "yevmiye-fisi-aktarimi_41157751_24740649.html"
source_version: "2022-10-06T12:58:45.163+03:00"
source_bytes: 20912
fetched_at: "2026-09-13T04:13:35+00:00"
generator: "netsis-scraper 1.0.0"
---
# Yevmiye Fişi Aktarımı

Yevmiye Fişi Aktarımı, Muhasebe Bölümünde, "İşlemler/Muhasebe Modülü" menüsünün altında yer alır. Yevmiye Fişi Aktarımı, daha önce kullanıcı tarafından oluşturulan TXT dosyasından, yevmiye fiş kayıtlarına aktarım yapılmasını sağlayan bölümdür.

![](../../../../../_assets/688a687cbe8ecf3ad808.png)

Yevmiye Fişi Aktarımı ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Yevmiye Fişi Aktarımı Ekranı |  |
| --- | --- |
| **Dosya İsmi** | Aktarılacak dosyanın bulunduğu dizin ve ismin tanımlandığı alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, dosyalar arasından seçim yapılır. Aktarım yapılacak TXT dosya yapısının belli bir düzene göre hazırlanması gerekir. İlk 3 satır başlık bilgisi olarak aşağıdaki gibi olmalıdır: ```text<br>1.satır str(5) DETAY<br>``` ```text<br>2.satır str(35) Aktarımı yapılacak TXT dosyaya özel olmalı. Ayrıca her aktarım için tekil olmalı.<br>``` ```text<br>3.satır number(5,0) Kaç adet kayıt olduğu gönderilmeli (kontrol açısından gerekli). Burada bilgiler tek fişe yazılacağı için, kayıt sayısı 32.767 rakamından küçük olmalı.<br>``` Diğer bilgi satırı yapısı: ```text<br>Ay Kodu Number(2)<br>``` ```text<br>Fiş No str(15)<br>``` Hesap Kodu str(35) ```text<br>Tarih str(8)<br>``` BA (B Borç A Alacak) char(1) ```text<br>Açıklama str(50)<br>``` ```text<br>Tutar number(28,x)<br>``` Buradaki x (ondalık) en fazla 8 olmalı ve toplam 28 karakter olmalı (ondalık ayıracı ile birlikte 28 olmalı) ```text<br>Miktar number(28,x) bknz.tutar açıklamasına<br>``` ```text<br>RefKod str(15)<br>``` ```text<br>DovTip number(3)<br>``` ```text<br>DovTut number(28,x) bknz.tutar açıklamasına<br>``` ```text<br>Firma.Döv.Tip number(3)<br>``` ```text<br>Firma.Döv.Tut. number(28,x) bknz.tutar açıklamasına<br>``` Yevmiye kaydı yapılırken: Evrak Tarihi: Günün tarihi girilir. Entegrefkey: ModulNo str(2)+ProgramNo str(2)+2.satırda verilen Text id Kayıt Yapan ve Kayıt Tarihi alanları doldurulur. Fiş Tipi: Mahsup seçilir. Hesap Planı ve Yevmiye Fişi Aktarımı işlemlerinin sonucunda, program tablolarına direkt kayıt aktarıldığı için işleme başlamadan önce yedek alınması önerilir. |
| ![](../../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilginin onaylanmasını sağlayan butondur. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgiden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
