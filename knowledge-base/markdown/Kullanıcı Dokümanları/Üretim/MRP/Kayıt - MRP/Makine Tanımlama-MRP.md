---
title: "Makine Tanımlama/MRP"
page_id: "50666632"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Üretim"
  - "MRP"
  - "Kayıt / MRP"
  - "Makine Tanımlama/MRP"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Üretim / MRP / Kayıt / MRP / Makine Tanımlama/MRP"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTNjMDhkM2RjLTA5NjktNDdmOC05YzdhLWNjYmU1M2U4ZTQ1YyZsaW5rPTA4ZWI3NTQwLWM5MzctNDkwOS1hY2Q5LTlhNDViNjRlZTk2NCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=3c08d3dc-0969-47f8-9c7a-ccbe53e8e45c&link=08eb7540-c937-4909-acd9-9a45b64ee964&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "makine-tanimlama-mrp_50666636_50666632.html"
source_version: "2022-10-18T16:34:24.820+03:00"
source_bytes: 16209
fetched_at: "2026-09-13T04:19:48+00:00"
generator: "netsis-scraper 1.0.0"
---
# Makine Tanımlama/MRP

Makine Tanımlama MRP, Üretim Bölümü'nde Kayıt/MRP menüsünün altında yer alır. İstendiği zaman "Netsis Demirbaş" programı ile bağlantılı olarak, istendiği zaman da serbest kodlama ile, makinelerin hangi operasyonda çalıştığını, saat maliyetini, üretim ve hazırlık sürelerini, öncelik kodu, grup kodu ve durumunun tanımlanacağı bölümdür. "Netsis Demirbaş Paketi" ile bağlantı kurmak için Yardımcı Programlar modülünde yer alan “Diğer Paketlerle Bağlantı” bölümü ile gerekli düzenlemelerin yapılması gereklidir. Düzenlemeler yapıldıktan sonra, "Rehber Paketi" alanından “Rehber” seçeneği seçilmesi gerekir.

Makine tanımlama MRP ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Makine Tanımlama Ekranı |  |
| --- | --- |
| Rehber Paketi | Makine tanımlamak için rehber paketin seçildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile seçim yapılır. Rehber paketi alanının aktif hale gelmesi için "Yardımcı Programlar" modülünde yer alan “Diğer Paketlerle Bağlantı” bölümü ile gerekli düzenlemelerin yapılması gerekir. Düzenleme yapılmadığında program otomatik olarak "Serbest" seçimini ekrana getirir. |
| Şirket Kodu | Makinenin çalıştığı şirket kodunun tanımlandığı alandır. |
| Demirbaş Kodu | Makine için demirbaş kodu tanımlanan alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, demirbaş kodlarına ulaşılır. |
| Demirbaş İsmi | Tanımlanan demirbaş için isim bilgisi girilen alandır. |
| Grup Kodu | Tanımlanan makineler için grup oluşturmak amacıyla grup kodu tanımlaması yapılan alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, grup kodlarına ulaşılır. |
| İstasyon Kodu | Tanımlaması yapılan makinenin çalışacağı istasyonun belirlendiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, istasyon kodlarına ulaşılır. |
| Üretim Süresi | Makinenin üretim süresinin tanımlandığı alandır. |
| Hazırlık Süresi | Makinenin hazırlık süresinin tanımlandığı alandır. |
| Birim Maliyet | Makine için birim maliyet tanımlaması yapılan alandır. |
| Durum | Makine aktif/pasif çalıştığını belirlemek için kullanılan alandır. Pasif seçilen makineler Üretim Akıl Kaydı yapılırken kullanılmaz. |
| Önem Derecesi | Aynı işi yapan makinelerden hangisinin daha önce kullanılacağını belirtmek için kullanılan alandır. |
| Makine Seri No | Tanımlanan makine için seri numarası girilen alandır. |
| Masraf Kodu | Tanımlanan makine ile ilgili yapılan masrafların kontrol edileceği hesabın girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılır. |
| Verimlilik Katsayı | “Verimlilik Katsayısı” alnına 1 değerinin verilmesi makinenin %100 verimlilikle çalıştığı anlamına gelir. Buraya girilen verimlilik değerine göre makine için tanımlanan üretim süresi ters orantılı şekilde artar. |
| Alış Tarihi | Makinenin alış tarihinin girildiği alandır. Demirbaş bakımından önemlidir. |
| Makine Sayısı | Tanımlanan makineden kaç adet olduğunun belirlendiği alandır. |
| Açıklama | Tanımlanan makine için açıklama bilgisinin girildiği alandır. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır.

Kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
