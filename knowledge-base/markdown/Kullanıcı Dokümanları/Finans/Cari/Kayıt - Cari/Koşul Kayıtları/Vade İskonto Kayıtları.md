---
title: "Vade İskonto Kayıtları"
page_id: "22805138"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Cari"
  - "Kayıt / Cari"
  - "Koşul Kayıtları"
  - "Vade İskonto Kayıtları"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Cari / Kayıt / Cari / Koşul Kayıtları / Vade İskonto Kayıtları"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTZmZjc0MzFiLTQ3ZGQtNDM4Ni04ZmUyLTYxMjIxOTVlOGMzMSZsaW5rPWE5NGQwNzMyLWM2YTMtNDNmMS1hZjVjLTdiOWRkZWM4YjAzMyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=6ff7431b-47dd-4386-8fe2-6122195e8c31&link=a94d0732-c6a3-43f1-af5c-7b9ddec8b033&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "vade-iskonto-kayitlari_22805141_22805138.html"
source_version: "2022-10-27T11:27:11.213+03:00"
source_bytes: 53268
fetched_at: "2026-09-13T04:07:44+00:00"
generator: "netsis-scraper 1.0.0"
---
# Vade İskonto Kayıtları

Vade İskonto Kayıtları, Finans Bölümü'nde, "Kayıt/Cari " menüsünün altında yer alır. Vade İskonto Kayıtları; "Detay Koşul Kayıtları" bölümündeki Vade İskontosu/Faiz Uygulaması ile, faturaya ilgili koşul kodu girildiğinde, vadesinden önce yapılacak ödemeler için vade iskontosu, geç ödemeler için de faiz uygulamasının yapılmasını sağlar. Ancak bu uygulamada program, koşul genel kayıtlarında verilen sabit bir iskonto/faiz oranını baz alarak, belgedeki vade gününe göre iskonto/faiz oranını hesaplar. Farklı vade günleri için girilecek iskonto oranları, hesaplama yöntemi yerine kullanıcı tarafından manuel girilmesi istendiğinde bu bölüm kullanılır. Böylece, Fatura/İrsaliye/Sipariş kayıtlarında satır bazında girilen vade günlerine göre hesaplanacak satır iskontosu, program tarafından ekrana getirilir.

Vade İskonto Kayıtları; Vade Kodları ve Vade İskonto Değerleri olmak üzere iki sekmeden oluşur.

**Vade** **Kodları**

Vade İskonto Kayıtları ekranı Vade Kodları sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Vade İskonto Kodları Ekranı |  |
| --- | --- |
| Vade Kodu | Vade bazında iskonto uygulaması için tanımlanacak vade kodunun girildiği alandır. Bu kod daha sonra "Detay Koşul Kayıtları" bölümünde kullanılır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, vade kodları arasından seçim yapılır. |
| Vade Açıklama | Tanımlanan vade koduna ait açıklamanın girildiği alandır. Vade kodu bu sekmede tanımlanarak kaydedildikten sonra, "Vade İskonto Değerleri" sekmesine geçilerek, satır bazında girilen vade günü için uygulanacak satır iskontosu oranı belirlenir. |

**Vade İskonto Değerleri**

Vade İskonto Değeri, Vade Kodları sekmesinde tanımlanan kodlardan biri seçildikten sonra, vade bazında kullanılacak iskonto oranın tanımlandığı bölümdür.

Satır bazında girilen vade gününe göre, satır iskontosunun alacağı oranlar bu bölümde tanımlanır. "Detay Koşul Kayıtları" bölümünde, detay koşul bazında kullanılmak istenen vade iskonto kodu ilgili alana girilmelidir. Tanımlanan vade kodlarının kullanılması için, "Detay Koşul Tanımlamaları" bölümünden ilgili kodların girilmesi gerekir.

Detay koşul kayıtlarında tanımlanması gereken alanlar hakkında detaylı bilgi için; Finans → Cari → Koşul Kayıtları → Detay Koşul Kayıtları

Tanımlamalar yapıldıktan sonra fatura modülündeki kullanım örneği aşağıdaki gibidir:

![](../../../../../_assets/cb67d7bd709a5a327034.png)

Faturada satır bazında girilen vade günü için belirlenen iskonto oranı program tarafından ekrana getirilir. Yukarıdaki örneğe göre, vade iskonto tanımlamalarında 15 vade günü için %20 satır iskontosu tanımlanmış. Ayrıca "Detay Koşul Kayıtları" bölümünde vade iskontosunun 1. satır iskontosuna yazılacağı belirlenmiş.

Bu durumda, fatura kaydı sırasında 1. satır iskontosu boş bırakılarak "Vade Günü" alanına uygulanacak vade günü girilir. Satır iskontosu, vade günü girildikten sonra program tarafından otomatik olarak ekrana getirilir.

Program, sadece "Vade İskonto Kayıtları" bölümünde girilen vade günlerine ait iskontoları ekrana getirir.

**Örneğin:** 15 gün için %20, 30 gün için %10 iskonto tanımlandığında ve fatura kaydında vade günü olarak 17 girildiğinde iskonto getirilmez. Bunun sebebi, "Vade İskonto Kayıtları" bölümünde 17 gün için iskonto oranının verilmemiş olmasıdır.

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır. Yapılan kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
