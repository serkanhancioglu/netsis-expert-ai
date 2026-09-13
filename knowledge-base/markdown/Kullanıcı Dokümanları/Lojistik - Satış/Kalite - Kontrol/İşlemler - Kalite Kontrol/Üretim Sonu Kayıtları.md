---
title: "Üretim Sonu Kayıtları"
page_id: "22804191"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Kalite - Kontrol"
  - "İşlemler / Kalite Kontrol"
  - "Üretim Sonu Kayıtları"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Kalite - Kontrol / İşlemler / Kalite Kontrol / Üretim Sonu Kayıtları"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWZmNzQ4NzM3LTk0ZTgtNGYzNy1hNzc5LWE3NDM1YmY2YTRkNSZsaW5rPTNiOTNhNzM0LThkNzEtNDU3Yy1iNjU4LWQzMTNiMmQxNGQ2YyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=ff748737-94e8-4f37-a779-a7435bf6a4d5&link=3b93a734-8d71-457c-b658-d313b2d14d6c&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "uretim-sonu-kayitlari_28148733_22804191.html"
source_version: "2022-10-25T10:06:41.573+03:00"
source_bytes: 43321
fetched_at: "2026-09-13T04:06:43+00:00"
generator: "netsis-scraper 1.0.0"
---
# Üretim Sonu Kayıtları

Üretim Sonu Kayıtlarını Oluşturma, Lojistik - Satış Bölümü'nde, "İşlemler/Kalite Kontrol" menüsünün altında yer alır. Üretim menüsünden yapılan kalite kontrol kayıtları sonunda, kabul ve red edilen malların üretim sonu kayıtlarının oluşturulması ve istendiğinde, üretimlerin stok hareketlerine yansıtılması için kullanılan bölümdür. Fire uygulamasının kullanıldığı durumlarda reddedilen mamuller, üretim sonu kayıtlarında fire olarak değerlendirilir. Üretim sonu kayıtları, "Kalite Kontrol Kayıtları" bölümünde girilen iş emirleri bazında ayrı ayrı oluşturulur.

Üretim sonu kayıtlarının oluşturabilmesi için Kalite Kontrol Kaydı kapatılmalı ve Kalite Kontrol Kaydında yer alan stoka ait "Stok Planlama Kayıtları" bölümünün Planlama-2 sekmesindeki “Üretim Sonu Kaydı Yeri” alanı "Kalite Kontrol" olmalıdır.

![](../../../../_assets/51c3757631c55745b2ec.png)

Üretim Sonu Kayıtlarını Oluşturma ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Üretim Sonu Kayıtlarını Oluşturma Ekranı |  |
| --- | --- |
| Fişler İş Emri Bazında Tek Tek Oluşturulsun | Üretim sonu kayıt fişlerinin iş emri bazında tek tek oluşturulması istendiğinde işaretlenmesi gereken seçenektir. |
| İş Emri No Aralığı | Üretim sonu kaydını oluşturacak iş emirlerinin seçildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile iş emri numaraları arasından seçim yapılarak numara aralığı verilir. |
| Kalite Kontrol Kayıtları İçin Son Tarih | Girilen tarihe kadar, kaydedilen kalite kontrol kayıtları kontrol edilir. Bu kayıtlardan, üretim sonu kaydı oluşturulmamış olan iş emirleri için üretim sonu kayıtları oluşturulur. |
| Oluşturulan Fişler İçin Kayıt Tarihi | Oluşan üretim sonu fişlerinin için kabul edilecek tarih bilgisinin girildiği alandır. Günün tarihi ve sistem saati program tarafından otomatik olarak ekrana getirilir. |
| Fiş No Serisi | Oluşturulan üretim sonu fiş kayıtlarının hangi seri ile oluşturulacağının belirlendiği alandır. |
| USK Depo Kodu | Üretim sonu kayıtları için depo kodunun girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile depo kodları arasından seçim yapılabilir. |
| Oluşturulan Fişler Otomatik Üretilsin | Oluşturulan üretim sonu kayıtlarının stok hareketlerine işlenmesini sağlayan seçenektir. İşaretlenmediğinde, oluşan üretim sonu kayıtlarının üretilmesi için, Üretim Modülü → "Üretim Sonu Kayıtları" bölümünde bu fişlerin çağrılarak kayıtlara geçmesi gerekir. |
| Bakiye (Bulunulan Depo/Tüm Depolar) | "Oluşturulan Fişler Otomatik Üretilsin" seçeneği işaretlendiğinde aktif hale gelen seçenektir. Üretim safhalarının lokal depolar bazında tanımlandığı ve hangi lokal depoların üretimle ilgili olduğunun, "Üretim Modülü Parametrelerinde" belirlendiği durumlarda, bakiye kontrolünün üretimin yapıldığı **tek depodan mı**, yoksa üretimi ilgilendiren **tüm depolardan mı** yapılacağını belirler. Tüm depolar seçeneğinde; malzeme miktarı olarak, üretim parametrelerinde tanımlanan bütün depolardaki bakiyeler baz alınır. Bulunulan depo seçeneğinde ise; üretimin yapıldığı USK Depo Kodu alanında yer alan lokal depodaki bakiyeler baz alınır. |
| Otomatik Yarı Mamullerde Stoktan Kullan | "Üretim Reçete Kayıtlarında", yarı mamuller için tanımlanan reçetelerde, bu yarı mamullerin kullanıldığı mamullerin üretimi sırasında otomatik olarak üretilmesi için “Otomatik Reçete” parametresinin işaretlenmesi gerekir. Bu üretimlerde, üretilen mamul için yarı mamul bakiyesinin yeterli olup olmadığına bakılmaz ve mamulün üretimi için gerekli olan miktarda yarı mamul, stokta yok kabul edilerek üretilir. Bu şekilde yapılan üretimlerde, yarı mamulün stokta bulunup bulunmadığına bakılmadığı için, yarı mamul stoklarında mamulün üretiminden kaynaklanan gereksiz bir çoğalma meydana gelir. Üretim sonu kayıtlarında bu seçenek kullanılırsa, bu tür yarı mamullerin bakiyelerine bakılır ve mamulün üretimi için gerekli olan miktar varsa yarı mamul üretilmez. Sadece yarı mamul bakiyesi mamulün üretimi için yeterli değilse, yarı mamul üretimi gerçekleşir. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Üretim sonu kaydı oluşturmak için girilen tüm bilgilerin kaydedilmesini sağlayan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Üretim sonu kaydı oluşturmak için girilen tüm bilgilerden vazgeçilmesi halinde kullanılan butondur. |
