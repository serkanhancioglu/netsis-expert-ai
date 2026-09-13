---
title: "Fiyat Kodu Tanımlamaları"
page_id: "29994575"
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
  - "Stok Fiyat İşlemleri"
  - "Fiyat Kodu Tanımlamaları"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Stok / Kayıt / Stok / Stok Fiyat İşlemleri / Fiyat Kodu Tanımlamaları"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWQzOWZjMTJkLWQyYjQtNGQ5Yi1hZDNlLWUwYTNiNjFkNTE0YyZsaW5rPThmYWJkOTgzLWM0MDItNGIwZS05MjI5LTNjZjg1Y2FmN2NkZiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=d39fc12d-d2b4-4d9b-ad3e-e0a3b61d514c&link=8fabd983-c402-4b0e-9229-3cf85caf7cdf&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "fiyat-kodu-tanimlamalari_29994581_29994575.html"
source_version: "2022-10-25T20:44:02.397+03:00"
source_bytes: 11850
fetched_at: "2026-09-13T04:04:18+00:00"
generator: "netsis-scraper 1.0.0"
---
# Fiyat Kodu Tanımlamaları

Fiyat Kodu Tanımlamaları, Lojistik - Satış Bölümü'nde, "Kayıt/Stok" menüsünün altında yer alır. Fiyat Kodu Tanımlamaları, stok kartlarına girilen fiyat kodu ve sorumlu grup bazında yapılacak fiyat değişiklikleri için fiyat hesaplama kıstaslarının tanımlandığı bölümdür.

Fiyat Kodu Tanımlamaları ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Fiyat Kodu Tanımlamaları Ekranı |  |
| --- | --- |
| Fiyat Kodu | Fiyat Kodu alanı kullanılırsa, ilgili fiyat koduna sahip (stok kartı kayıtlarında fiyat kodu girilen) stok fiyat hesaplamaları, sorumlu grup kısıtlamaları kullanılarak (güvenlik açısından), alt/üst limitler ve kar marjı belirlenerek yapılır. "Fiyat Kodu" kullanılmazsa, kar marjı kullanılarak fiyat değişiklikleri yapılır. Ancak, sorumlu grup kontrolü yapılmaz. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, daha önce tanımlaması yapılan fiyat kodlarına ulaşılır. |
| Açıklama | İlgili fiyat koduna ait açıklama bilgisinin girildiği alandır. |
| Sorumlu Grup | İlgili fiyat grubu için sorumlu olacak grubun girildiği alandır. Tanımlanan fiyat koduna sorumlu bir grup girildiğinde ve ilgili fiyat koduna sahip stokların fiyat değişikliğinde, işlemi yapan kişinin kullanıcı numarası kontrol edilir. Fiyat değişikliği yapan kişi, sorumlu grupta tanımlanmamışsa değişikliğe izin verilmez. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, daha önce tanımlaması yapılan sorumlu grup kodlarına ulaşılır. |
| Alt/Üst | Bu sorgulama, alış fiyatı üzerinden satış fiyatı belirlerken matematiksel bir yöntem olarak kullanılır. **Örneğin:** Alış Fiyatı = 100 Alt/ Üst = A Marj = 20 ise<br>Satış Fiyatı = 100 x 1.20 =120 olarak,<br>Aynı örnekte Alt/Üst = U ise<br>Satış Fiyatı = 100 / (1-0.20) = 125 olarak hesaplanır. |
| Satış Fiyatına KDV Dahil | Seçenek işaretlendiğinde; "Alt/Üst" alanında yer alan örnekteki satış fiyatına, stok kartlarında bulunan KDV oranı kadar KDV eklenmesi sağlanır. İşaretlenmediğinde ise, bulunan satış fiyatına KDV oranı eklenmez. |
| Kar Marjı | Satış fiyatı hesaplamasında baz alınacak % (yüzde ) değerin girildiği alandır. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır. Kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
