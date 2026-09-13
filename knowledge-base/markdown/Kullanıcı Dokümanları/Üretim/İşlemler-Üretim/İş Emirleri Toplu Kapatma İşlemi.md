---
title: "İş Emirleri Toplu Kapatma İşlemi"
page_id: "50664003"
product: "netsis-3-enterprise"
depth: 4
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Üretim"
  - "İşlemler/Üretim"
  - "İş Emirleri Toplu Kapatma İşlemi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Üretim / İşlemler/Üretim / İş Emirleri Toplu Kapatma İşlemi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTYyZDViNDE3LTgzZmItNDYzMS04OGRiLWVmZTFlOTM5MGQwNCZsaW5rPTVkYWViYTNiLWVhNjQtNDgwNC05ODNjLWJiYjgxOGZkYzQ5NSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=62d5b417-83fb-4631-88db-efe1e9390d04&link=5daeba3b-ea64-4804-983c-bbb818fdc495&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "is-emirleri-toplu-kapatma-islemi_50664006_50664003.html"
source_version: "2022-10-12T15:32:12.210+03:00"
source_bytes: 21802
fetched_at: "2026-09-13T04:19:08+00:00"
generator: "netsis-scraper 1.0.0"
---
# İş Emirleri Toplu Kapatma İşlemi

İş Emirleri Toplu Kapatma işlemi, Üretim Bölümü'nde İşlemler/Üretim menüsünün altında yer alır. İş emirlerinin tek tek değil toplu şekilde silinmesi için kullanılan bölümdür.

İş Emirleri Toplu Kapatma işlemi ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| İş Emirlerini Toplu Kapatma İşlemi Ekranı |  |
| --- | --- |
| Üretimi Kapananları Otomatik Kapatma İşlemi | Seçenek işaretlendiğinde, ekrandaki diğer alt seçeneklere müdahale edilemeyerek, ![](../../../_assets/39d77b8716226638d9ce.jpg) Tamam butonu ile işleme devam edilir. İşlemin yapılmasından vazgeçilmesi halinde ![](../../../_assets/973111d004995dca0113.jpg) İptal butonu ile işlemden çıkılabilir. |
| Kriterlere Göre Otomatik Kapatma İşlemi | Programın; Stok Kodu, İş Emri No ve Tarih aralığı verilerek silme işlemi yapmasını sağlayan seçenektir. Sadece istenen ortak özelliklere sahip iş emirlerinin silinmesini sağlar. |
| Üretim Planında Kaydı Olmayan Stoklar İçin Açılmış Olan İş Emirlerini Kapatma İşlemi | İlgili işletmede MRP çalıştırılıyorsa son çalışan MRP sonuçlarında bulunmayan stok kodlarına ait iş emirlerinin kapatılmasını sağlayan seçenektir. |
| Stok Kodu Aralığı | Kriterlere Göre Otomatik Kapatma İşlemi seçeneğinin işaretlenmesi ile aktif hale gelen alandır. İş emirlerinin silinmesi için stok kodu kısıdının verilmesini sağlar. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile stok kodları arasından seçim yapılır. |
| İş Emri No Aralığı | Kriterlere Göre Otomatik Kapatma İşlemi seçeneğinin işaretlenmesi ile aktif hale gelen alandır. İş emirlerinin silinmesi için iş emri numarası kısıdının verilmesini sağlar. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile iş emri numaraları arasından seçim yapılır. |
| Referans İş Emri No Aralığı | Kriterlere Göre Otomatik Kapatma İşlemi seçeneğinin işaretlenmesi ile aktif hale gelen alandır. İş emirlerinin silinmesi için referans iş emri numarası kısıdının verilmesini sağlar. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile referans iş emri numaraları arasından seçim yapılır. |
| Tarih Aralığı | Kriterlere Göre Otomatik Kapatma İşlemi seçeneğinin işaretlenmesi ile aktif hale gelen alandır. İş emirlerinin silinmesi için tarih kısıdının verilmesini sağlar. |
| Teslim Tarihi Aralığı | Kriterlere Göre Otomatik Kapatma İşlemi seçeneğinin işaretlenmesi ile aktif hale gelen alandır. İş emirlerinin silinmesi için teslim tarihi kısıdının verilmesini sağlar. |
| Fireler Dikkate Alınsın | Fireler Dikkate Alınsın seçeneği, Üretimi Tamamlananları Otomatik Kapatma İşlemi seçildiğinde kullanılabilir. Üretim Parametreleri - Fire Uygulaması Var ve İkinci Miktar Girilecek parametreleri işaretli olduğunda aktif hale gelir. Seçeneğin işaretlenmesi ile birlikte, iş emrine bağlı üretim sonu kayıtlarındaki Net Üretim Miktarı (Fire miktarı düşmüş) ile Fire Miktarı toplanarak, iş emrindeki miktar ile karşılaştırılır. Bu rakamın iş emri miktarına eşit ya da iş emri miktarından büyük olması durumunda ilgili iş emri kapatılır. Seçenek işaretlenmediği zaman, fire miktarı düşmüş Net Üretim Miktarı ile, iş emrindeki miktar karşılaştırılır. Net Üretim Miktarının iş emri miktarına eşit ya da iş emri miktarından büyük olması durumunda iş emri kapatılır. **Örneğin;** M1 mamulü için 100 adet iş emri verildiği varsayıldığında; Üretim Sonu Kayıtlarında 100 birim üretilmiş, bunun da 10 birimi fire olmuştur. Net Üretim Miktarı 90’dır. Fireler Dikkate Alınsın seçeneği işaretlenirse, iş emri ve üretim sonu kayıtlarındaki toplam üretim miktarı eşit olduğundan iş emri kapatılır. Seçenek işaretlenmediği zaman, 90 adet üretim sonu kaydı ile 100 adet iş emri karşılaştırıldığı için iş emri kapatılmaz. |
| ![](../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilginin onaylanmasını sağlayan butondur. |
| ![](../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgiden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
