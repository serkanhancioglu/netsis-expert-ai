---
title: "Operasyon Tanımlama"
page_id: "50663019"
product: "netsis-3-enterprise"
depth: 4
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Üretim"
  - "Kayıt/Üretim"
  - "Operasyon Tanımlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Üretim / Kayıt/Üretim / Operasyon Tanımlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTZmYjFiYjQ2LWUyOWMtNDgxOC04MTQ4LTk5N2IxNzRmYmM1ZCZsaW5rPTQ0ZmY1ODU2LWEwOWYtNDRlNS05ZmZiLTNkNGM1ZjY2NjViZSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=6fb1bb46-e29c-4818-8148-997b174fbc5d&link=44ff5856-a09f-44e5-9ffb-3d4c5f6665be&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "operasyon-tanimlama_50663022_50663019.html"
source_version: "2022-10-13T11:42:39.537+03:00"
source_bytes: 10369
fetched_at: "2026-09-13T04:18:46+00:00"
generator: "netsis-scraper 1.0.0"
---
# Operasyon Tanımlama

Operasyon Tanımlama, Üretim modülünde Kayıt/Üretim menüsünün altında yer alır. Operasyon için ilgili alanların tanımlanmasını sağlar.

Operasyon Tanımlama ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Operasyon Tanımlama Ekranı |  |
| --- | --- |
| Operasyon Kodu | Tanımlanacak operasyon için kod bilgisi girilen alandır. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile tanımlı operasyon kodlarına ulaşılır. |
| Operasyon İsmi | Tanımlanan operasyon kodu için isim bilgisi girilen alandır. |
| İstasyon Kodu | İstasyon kodu tanımlanması için kullanılan alandır. Zorunlu bir alan değildir. Aynı operasyon birden fazla istasyonda yapılıyorsa bu alana kod girilmesine gerek yoktur. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile istasyon kodlarına ulaşılır. |
| Simültane Tezgah Miktarı | Operasyonun bir anda yapılacağı tezgah sayısının tanımlandığı alandır. Aynı işlem birden fazla makinede yapılabilir. Mevcut makineler aynı anda aynı mamul için bir işi yapabiliyorsa, toplam makine sayısının girilmesi gerekir. Makinelerin kalıp, aparat gibi malzeme gereksinimlerinden dolayı sadece 1 makinede işlem yapılabiliyorsa 1 değerinin girilmesi gerekir. |
| Geçiş Miktarı | Bir sonraki operasyona geçiş miktarının tanımlandığı alandır. |
| Hazırlık Süresi | Operasyona başlanması için gereken sürenin tanımlandığı alandır. **Örneğin;** Operasyonda kullanılan makinenin ısınması için 30 dk. gerekmesi gibi. |
| Üretim Süresi | Operasyonda üretime başlanması ile, bir birim üretimin tamamlanması arasında geçen sürenin tanımlandığı alandır. |
| Geçiş Süresi | Tanımlanmakta olan operasyon tamamlandıktan sonra, sıradaki operasyona geçilene kadar ürünlerin belli bir süre beklemesi gerekiyorsa ilgili sürenin tanımlandığı alandır. Burada önemli olan geçiş süresi içinde herhangi bir kaynak kullanımı olup olmadığıdır. Eğer kaynak kullanımı olacaksa (bekleme alanının kısıtlı kapasitesi olması gibi) bu beklemeyi de farklı bir operasyon gibi tanımlayıp kısıtları tanımlamak gerekir. |
| Operasyon Açıklama | Tanımlanan operasyon için açıklama bilgisinin girildiği alandır. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır.

Kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
