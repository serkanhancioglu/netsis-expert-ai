---
title: "Operasyon Tanımlama/MRP"
page_id: "50666624"
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
  - "Operasyon Tanımlama/MRP"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Üretim / MRP / Kayıt / MRP / Operasyon Tanımlama/MRP"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTlkMzExYzgyLWYwMGYtNGY3OS05ZDFkLTVhY2YzNDc2YzE0MCZsaW5rPTQ0Y2JlYmNhLTczMDgtNGEwNS05YzJlLTNmZDM3NDkxZmZkNSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=9d311c82-f00f-4f79-9d1d-5acf3476c140&link=44cbebca-7308-4a05-9c2e-3fd37491ffd5&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "operasyon-tanimlama-mrp_50666625_50666624.html"
source_version: "2022-10-18T16:31:51.850+03:00"
source_bytes: 11305
fetched_at: "2026-09-13T04:19:47+00:00"
generator: "netsis-scraper 1.0.0"
---
# Operasyon Tanımlama/MRP

Operasyon Tanımlama MRP, Üretim Bölümü'nde Kayıt/MRP menüsünün altında yer alır. Ürünün üretilmesi sırasında, sırayla yapılan işlemlerin her biridir. Programda bir operasyon kataloğu bulunur. Bu kataloğa fabrikada yapılan her türlü işlem kaydedilebilir. Ürünün işlemleri (Rotası) reçetelerde tanımlanırken bu katalogdan operasyonlar seçilerek eklenir. Operasyonların her birinin, fabrikadaki bir iş istasyonunda yapılması gerekir. Operasyonlar için iş istasyonu, kullanılacak simültane işlem birimi (Tezgah Sayısı), üretim süresi, hazırlık süresi, bir sonraki operasyona geçiş için lot miktarı ve süresi tanımlanır.

Operasyon Tanımlama MRP ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Operasyon Tanımlama Ekranı |  |
| --- | --- |
| Operasyon Kodu | Tanımlanan operasyon için takip edilmesi istenen kod numarasının girildiği alandır. İlgili operasyon, bu alanda tanımlanan kod numarası ile reçetelerde kullanılır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, operasyon kodlarına ulaşılır. |
| Operasyon İsmi | Tanımlanan operasyon kodu için isim bilgisi girilen alandır. |
| İstasyon Kodu | Tanımlanan operasyonun hangi iş istasyonunda yapıldığı bilgisi için kod tanımlaması yapılan alandır. Boş bırakılmaz. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, istasyon kodlarına ulaşılır. |
| Simültane Tezgah Miktarı | Operasyonun bir anda yapılacağı tezgah sayısının tanımlandığı alandır. Aynı işlem birden fazla makinede yapılabilir. Mevcut makineler aynı anda aynı mamul için bir işi yapabiliyorsa, toplam makine sayısının girilmesi gerekir. Makinelerin kalıp, aparat gibi malzeme gereksinimlerinden dolayı sadece 1 makinede işlem yapılabiliyorsa 1 değerinin girilmesi gerekir. |
| Operasyon Açıklama | Tanımlanan operasyon için açıklama bilgisinin girildiği alandır. |
| Geçiş Miktarı | Bir sonraki operasyona geçiş miktarının tanımlandığı alandır. |
| Hazırlık Süresi | Operasyona başlanması için gereken sürenin tanımlandığı alandır. **Örneğin;** Operasyonda kullanılan makinenin ısınması için 30 dk. gerekmesi gibi. |
| Üretim Süresi | Operasyonda üretime başlanması ile, bir birim üretimin tamamlanması arasında geçen sürenin tanımlandığı alandır. |
| Geçiş Süresi | Tanımlanmakta olan operasyon tamamlandıktan sonra, sıradaki operasyona geçilene kadar ürünlerin belli bir süre beklemesi gerekiyorsa ilgili sürenin tanımlandığı alandır. Burada önemli olan geçiş süresi içinde herhangi bir kaynak kullanımı olup olmadığıdır. Eğer kaynak kullanımı olacaksa (bekleme alanının kısıtlı kapasitesi olması gibi) bu beklemeyi de farklı bir operasyon gibi tanımlayıp kısıtları tanımlamak gerekir. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır.

Kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
