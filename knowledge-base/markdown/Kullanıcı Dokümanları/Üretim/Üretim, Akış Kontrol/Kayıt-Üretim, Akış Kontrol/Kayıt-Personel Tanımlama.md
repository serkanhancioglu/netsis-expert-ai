---
title: "Kayıt/Personel Tanımlama"
page_id: "50665080"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Üretim"
  - "Üretim, Akış Kontrol"
  - "Kayıt/Üretim, Akış Kontrol"
  - "Kayıt/Personel Tanımlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Üretim / Üretim, Akış Kontrol / Kayıt/Üretim, Akış Kontrol / Kayıt/Personel Tanımlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTkxY2NiYWUwLTNhNjYtNDNiNi04YzdiLTI5MjQ3MzkxOTRhMSZsaW5rPWE3Y2RkYzAzLTYxMzEtNDc3MC1hOWJjLTUyNDEyYjE4MmM0YiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=91ccbae0-3a66-43b6-8c7b-2924739194a1&link=a7cddc03-6131-4770-a9bc-52412b182c4b&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "kayit-personel-tanimlama_50665226_50665080.html"
source_version: "2022-09-19T10:29:06.080+03:00"
source_bytes: 14740
fetched_at: "2026-09-13T04:20:38+00:00"
generator: "netsis-scraper 1.0.0"
---
# Kayıt/Personel Tanımlama

Personel Tanımlama, Üretim Bölümü'nde, "Kayıt/Üretim,Akış Kontrol" menüsünün altında yer alır. Personel Tanımlama bölümü; istendiği zaman Netsis Personel programıyla bağlantılı olarak, istendiği zaman ise, serbest kodlama ile personellerin hangi iş istasyonlarında ve hangi görevde çalıştığı, saat maliyeti, grup kodu ve durumunu tanımlamak için kullanılan bölümdür.

"Netsis Personel Paketi" ile bağlantı kurmak için, "Yardımcı Programlar" modülünde yer alan “[Diğer Paketlerle Bağlantı](<../../../Genel/Yardımcı Programlar/Kayıt - Yardımcı Programlar/Diğer Paketlerle Bağlantı.md>)” bölümü ile gerekli düzenlemelerin yapılması gerekir. Düzenlemeler yapıldıktan sonra, "Rehber Paketi" alanından “Rehber” seçeneği seçilerek “İşyeri” alanına "Personel" paketinde oluşturulmuş, veri alınacak personel şirketinin isminin girilmesi gerekir.

Personel Tanımlama ekranında yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| Personel Tanımlama Ekranı |  |
| --- | --- |
| Rehber Paketi | Personel tanımlamak için rehber paketin seçildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile seçim yapılır. Alanın aktif hale gelmesi için "Yardımcı Programlar" modülünde yer alan “[Diğer Paketlerle Bağlantı](<../../../Genel/Yardımcı Programlar/Kayıt - Yardımcı Programlar/Diğer Paketlerle Bağlantı.md>)” bölümü ile gerekli düzenlemelerin yapılması gerekir. Düzenleme yapılmadığında program otomatik olarak "Serbest" seçimini ekrana getirir. |
| İşyeri | "Personel" paketinde oluşturulmuş, veri alınacak personel şirketinin isminin girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, şirket kodlarına ulaşılır. |
| Sicil Numarası | Personel sicil numarasının tanımlandığı alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, personel isimlerine ulaşılır. |
| Personel İsmi | Personel isminin tanımlandığı alandır. |
| Grup Kodu | Personelleri gruplamak için grup kodu tanımlanan alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile grup kodlarına ulaşılır. |
| Görev Kodu | Tanımlanan personel için görev kodu girilen alandır. |
| İstasyon Kodu | Personelin çalışacağı istasyonun tanımlandığı alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile istasyon kodlarına ulaşılır. |
| Durum | Personelin aktif/pasif çalıştığını belirleyen alandır. |
| Birim Maliyet | Tanımlanan personel için birim maliyet girilen alandır. |
| Personel Bağlantılı | "Rehber Paketi" alanından "Personel" seçildiğinde ve personel paketindeki SICILNO bilgisi girilerek kayıt yapıldığında program tarafından otomatik olarak işaretli halde ekrana gelir. Bu alanın işaretli olduğu durumlarda, "Personel İsmi" alanı pasif olur. İsim bilgisi personel paketinden getirilir. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır. Personel Tanımlama ekranı kaydının iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
