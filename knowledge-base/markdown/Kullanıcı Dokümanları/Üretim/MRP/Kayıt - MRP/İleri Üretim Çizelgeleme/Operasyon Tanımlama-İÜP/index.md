---
title: "Operasyon Tanımlama/İÜP"
page_id: "50672758"
product: "netsis-3-enterprise"
depth: 6
is_section: true
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Üretim"
  - "MRP"
  - "Kayıt / MRP"
  - "İleri Üretim Çizelgeleme"
  - "Operasyon Tanımlama/İÜP"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Üretim / MRP / Kayıt / MRP / İleri Üretim Çizelgeleme / Operasyon Tanımlama/İÜP"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWJiNTVlOTE2LTBlNjMtNDgzZC05N2UzLWUzZjM4YWE4ZGViYyZsaW5rPTUwN2ZiYWU0LTcwYzAtNDAwMy04ZjMwLWJhY2I1YTRiNDY3NiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=bb55e916-0e63-483d-97e3-e3f38aa8debc&link=507fbae4-70c0-4003-8f30-bacb5a4b4676&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "operasyon-tanimlama-iup_50672761_50672758.html"
source_version: "2022-10-18T16:30:04.307+03:00"
source_bytes: 14393
fetched_at: "2026-09-13T04:19:38+00:00"
generator: "netsis-scraper 1.0.0"
---
# Operasyon Tanımlama/İÜP

Operasyon Tanımlama İÜP, Üretim Bölümü'nde Kayıt/MRP menüsünün altında yer alır. İleri Üretim Çizelgeleme uygulamasının doğru çalışması için operasyon tanımlaması yapılan bölümdür.

Operasyon Tanımlama İÜP ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Operasyon Tanımlama Ekranı |  |
| --- | --- |
| Operasyon Kodu | Tanımlanan operasyon için takip edilmesi istenen kod numarasının girildiği alandır. İlgili operasyon, bu alanda tanımlanan kod numarası ile reçetelerde kullanılır. Rehber butonu ![](../../../../../../_assets/088477bb321d1b20c939.jpg) ile, operasyon kodlarına ulaşılır. |
| Operasyon İsmi | Tanımlanan operasyon kodu için isim bilgisi girilen alandır. |
| İstasyon Kodu | Tanımlanan operasyonun hangi iş istasyonunda yapıldığı bilgisi için kod tanımlaması yapılan alandır. Zorunlu bir alan değildir. Aynı operasyon birden fazla istasyonda yapılıyorsa bu alana<br>giriş yapılması mantıklı değildir. Rehber butonu ![](../../../../../../_assets/088477bb321d1b20c939.jpg) ile, istasyon kodlarına ulaşılır. |
| Grup Kodu | Tanımlanan operasyonun, belli bir gruba da tanımlanması için kullanılan alandır. Rehber butonu ![](../../../../../../_assets/088477bb321d1b20c939.jpg) ile, grup kodlarına ulaşılır. |
| Operasyon Açıklama | Tanımlanan operasyon için açıklama bilgisi girilen alandır. |
| Üretim Süresi Üretim Miktarı | Üretim Süresi ve Üretim Miktarı bir arada kullanılarak anlamlı bir veri oluşturur. Birim sürede yapılan üretim miktarının girildiği alanlardır. **Örneğin;** Bir operasyonda 70 saniyede 8 metre ürün işleniyorsa, Üretim Süresi alanına 70 saniye, Üretim Miktarı alanına 8 metre girilmesi gerekir. Burada belirtilmesi gereken önemli bir ayrıntı şudur ki; eğer bir operasyondaki üretim süresi ve miktarı o operasyon için tek ve sabit değilse, ürün ya da kaynak bazında farklılık gösteriyorsa, ileride detaylandırılacak olan eşleştirme ekranları üzerinde bu tanımlamalar yapılabilir. |
| Transfer Süresi | Tanımlanmakta olan operasyon tamamlandıktan sonra sıradaki operasyona geçilene kadar ürünlerin belli bir süre beklemesi gerektiğinde ilgili sürenin tanımlandığı alandır. Burada önemli olan transfer süresi içinde herhangi bir kaynak kullanımı olup olmadığıdır. Kaynak kullanımı olacaksa - bekleme alanının kısıtlı kapasitesi olması gibi - bu beklemeyi de farklı bir operasyon gibi tanımlayıp kısıtları tanımlamak gerekir. |
| Otomatik Hesaplansın | Geçiş Miktarı veya Geçiş Süresinin otomatik hesaplanması için kullanılan seçenektir. |
| Geçiş Tanım Tipi | Operasyon geçişinde kullanılacak tanım tipinin belirlendiği alandır. Alanın sağ tarafında bulunan aşağı ok butonu ile Geçiş Süresi veya Geçiş Miktarı seçenekleri arasından seçim yapılır. |
| Geçiş Süresi | Geçiş miktarının süre olarak tanımlandığı alandır. |
| Geçiş Miktarı | Geçiş Miktarı elle (Manuel) girilebilir ya da “Otomatik Hesaplansın” parametresi kullanılabilir. Geçiş Miktarı alanına girilecek değer, tanımlanmakta olan operasyon tamamlandıktan sonra, ürünlerin sıradaki operasyona kaç birimlik yığınlar halinde geçeceğini belirler. Bu alanda geçiş miktarının hiç tanımlanmaması durumunda ise, ilgili iş emrinin tamamının bitmesi beklenecek şekilde çizelgeleme yapılır. |
| Parti Büyüklüğü | Şimdilik algoritmada desteklenmeyen bir alandır. Bilgi amaçlı kullanılır. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır.

Kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
