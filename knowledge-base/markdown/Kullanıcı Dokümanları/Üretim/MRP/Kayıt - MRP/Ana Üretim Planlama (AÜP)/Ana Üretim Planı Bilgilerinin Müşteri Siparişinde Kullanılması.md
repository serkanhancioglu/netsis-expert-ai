---
title: "Ana Üretim Planı Bilgilerinin Müşteri Siparişinde Kullanılması"
page_id: "50668363"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Üretim"
  - "MRP"
  - "Kayıt / MRP"
  - "Ana Üretim Planlama (AÜP)"
  - "Ana Üretim Planı Bilgilerinin Müşteri Siparişinde Kullanılması"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Üretim / MRP / Kayıt / MRP / Ana Üretim Planlama (AÜP) / Ana Üretim Planı Bilgilerinin Müşteri Siparişinde Kullanılması"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTQ0OWJkNTk4LTgwYzUtNGZlYS1hZjYzLWUzZWFlMmEyOGI1NiZsaW5rPTAyNTNkMGEzLWQ0OTgtNDJmMC05MmM3LWM5ZWNjOTM2Yjk2YiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=449bd598-80c5-4fea-af63-e3eae2a28b56&link=0253d0a3-d498-42f0-92c7-c9ecc936b96b&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ana-uretim-plani-bilgilerinin-musteri-siparisinde-kullanilmasi_91719370_50668363.html"
source_version: "2022-10-19T15:01:21.290+03:00"
source_bytes: 2928
fetched_at: "2026-09-13T04:19:58+00:00"
generator: "netsis-scraper 1.0.0"
---
# Ana Üretim Planı Bilgilerinin Müşteri Siparişinde Kullanılması

Ana Üretim Planlama sonucu hesaplanan teslim edilebilir miktar değerleri, Fatura modülünden girilecek müşteri siparişleri sırasında kullanılabilir. Bu şekilde satış ekibi ile planlama ekibi arasında ortak bir değer üzerinden iletişim kurulması amaçlanır ve satış ekibinin gireceği sipariş sırasında plana uygunluk kontrolünün yapılması sağlanır. Böylece, müşteri siparişi girilirken hangi teslim tarihine ne kadarlık teslimat yapılacağı raporlanabilir.

Ana Üretim Planlama işlemlerinin müşteri siparişi ekranında kullanılabilmesi için gerekli olan bilgiler şunlardır:

- AÜP ek lisansının bulunması gerekir.
- Satış Parametreleri-“Sipariş Kaydında Her Satırda Teslim Tarihi Sorulsun” seçeneğinin işaretlenmesi gerekir.

İlgili fonksiyona Müşteri Siparişi ekranında yer alan "Kalemler" sekmesine stok kodunu girdikten sonra farenin sağ tuşuna tıklayarak ulaşılır.

"Ana Üretim Planlama Bilgileri" seçeneğine tıklayarak ulaşılan ekran üzerinde, girilen miktar ve teslim tarihine göre ana üretim planına uygun teslimat önerileri sunulur. İlgili miktarın bulunduğu periyotta yeterli teslim edilebilir miktar varsa, siparişin teslim tarihinde sorun yoktur ve farklı bir öneri sunulmaz. Ancak, istenilen teslim tarihinde girilen miktarı karşılayacak teslim edilebilir miktar yoksa sipariş düzleme yöntemleri kullanılarak yeni teslimat önerileri sunulur. Kullanıcı bu önerileri kabul ederse ilgili öneriler sipariş kalemlerine otomatik olarak aktarılır. Kullanıcı bu önerileri kabul etmezse, girilen teslim tarihine tek bir satır olarak kayıt atılır. Önerileri kabul etmeyerek kaydedilen müşteri sipariş kalemleri sonrası, ana üretim planına uygun olmayan durumlar oluşabilir ve bu durumu düzeltmek için planlama ekibinin tekrar ana üretim planını çalıştırması gerekir.
