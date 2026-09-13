---
title: "Ürün Yapılandırma Tanımlamaları"
page_id: "29993480"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Stok"
  - "Kayıt / Stok"
  - "Esnek Yapılandırma"
  - "Ürün Yapılandırma Tanımlamaları"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Stok / Kayıt / Stok / Esnek Yapılandırma / Ürün Yapılandırma Tanımlamaları"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWI4YzVjMjhhLWViMDMtNGZjMi05MzM4LWU5ZGY2OGIwOGE4NCZsaW5rPTU1ZTUyNGJlLTM2YjYtNDk2Yy04NGI5LTc1NTcwNzUyOTQyMiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=b8c5c28a-eb03-4fc2-9338-e9df68b08a84&link=55e524be-36b6-496c-84b9-755707529422&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "urun-yapilandirma-tanimlamalari_29993484_29993480.html"
source_version: "2022-10-25T15:23:21.280+03:00"
source_bytes: 18453
fetched_at: "2026-09-13T04:03:58+00:00"
generator: "netsis-scraper 1.0.0"
---
# Ürün Yapılandırma Tanımlamaları

Ürün Yapılandırma Tanımlamaları, Lojistik - Satış Bölümü'nde, "Kayıt/Stok" menüsünün altında yer alır. Ürün Yapılandırma Tanımlamaları, "Ürün Yapılandırma Profili" bölümünde tanımlanan özelliklerin (yapılandırma kodu bazında) hangi değerleri alacağı ile ilgili tanımlamaların yapıldığı bölümdür. Kullanılacak olan her farklı özellik kombinasyonu için yapılandırma kodu ve bu koda ait özellik değerlerinin tanımlanması gerekir. Yapılandırma tanımları farklı kombinasyonlar gerektikçe, programın her yerinde kullanım kolaylığı sağlayan **Yapılandırma Sihirbazları** ile yapılır. Ürün Yapılandırma Tanımları, Sabit Kayıtlar ve Detay Kayıtlar olmak üzere iki sekmeden oluşur.

Yapılandırma Sihirbazı kullanımı ile ilgili detaylı bilgi için; Stok → Ekler → [Ek-3 (Esnek Yapılandırma Uygulaması)](<../../Ekler (Stok)/Ek-3 (Esnek Yapılandırma Uygulaması).md>) dokümanına bakılabilir.

**Sabit Kayıtlar**

Ürün Yapılandırma Tanımlamaları ekranı Sabit Kayırlar sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Ürün Yapılandırma Tanımlamaları Ekranı |  |
| --- | --- |
| Kodu | Yapılandırma kodunun girildiği alandır. En fazla 15 karakterden oluşan alfa nümerik kod girilir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, tanımlanmış kodlar arasından seçim yapılabilir. |
| Açıklama | Tanımlanan yapılandırma koduna ait açıklamanın girildiği alandır. |
| Geçerlilik Başlangıç Tarihi/Geçerlilik Bitiş Tarihi | Tanımlanan yapılandırma koduna ait geçerlilik süresinin, başlangıç/bitiş tarihinin belirlendiği alandır. İçinde bulunulan günün tarihi bu alana program tarafından otomatik olarak getirilir. İstendiğinde kullanıcı tarafından değişiklik yapılabilir. |
| Yapılandırılacak Stok | Tanımlanan yapılandırma kodunun hangi stok için kullanılacağı ile ilgili bilginin girildiği alandır. Bilgi amaçlı bir alan olduğu için boş bırakılabilir. Her bir yapılandırma kodu tek bir ürün için kullanılacağı gibi, aynı özelliklere sahip birden fazla ürün için de kullanılabilir. "Esnek Yapılandırma Uygulaması" ile ilgili dosyaların güncellenmesi sonucu, "Ürün Yapılandırma Tanımlamaları" bölümünde **999999999999999** kodlu "Genel Yapılandırma Kodu" program tarafından otomatik olarak tanımlanır. "Genel Yapılandırma Kodu" Üretim ve MRP Modülleri dışında hiç bir yerde kullanılmaz ve bu kod silinmez. |
| İşletmelerde Ortak | Tanımlaması yapılan yapılandırma kodunun hangi işletmede kullanılacağının belirlendiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile işletme kodları arasından seçim yapılır. |
| Şubelerde Ortak | Tanımlaması yapılan yapılandırma kodunun hangi şubede kullanılacağının belirlendiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile şube kodları arasından seçim yapılır. |
| Hariç Tutulacak Şube Tanımlamaları | "Hariç Tutulacak Şube Tanımlamaları" yazısının üzerine tıklandığında, mevcut şubeler içinde, hariç tutulması istenen şubeler için sol fare tuşu ile çift tıklanarak seçim yapılan alandır. |

**Detay Kayıtlar**

Detay Kayıtlar, tanımlanan yapılandırma kodunun hangi özelliklere sahip olduğu ve bu özelliklere bağlı olarak alacağı değerlerin belirlendiği sekmedir.

Ürün Yapılandırma Tanımlamaları ekranı Detay Kayıtlar sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Ürün Yapılandırma Tanımları Ekranı |  |
| --- | --- |
| Özellik Kodu | Yapılandırma kodunun sahip olduğu özelliğe ait kod bilgisinin girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, tanımlanmış kodlar arasından seçim yapılabilir. |
| Değer Kodu | Yapılandırma kodunun sahip olduğu özellikler için hangi değerleri alacağı ile ilgili kod bilgisinin girildiği alandır. Yapılandırma kodu, aynı özelliğin birden fazla değerini alamaz. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır. Yapılan kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
