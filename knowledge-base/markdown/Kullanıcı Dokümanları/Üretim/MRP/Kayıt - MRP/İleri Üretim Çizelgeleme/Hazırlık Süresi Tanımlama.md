---
title: "Hazırlık Süresi Tanımlama"
page_id: "50673505"
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
  - "İleri Üretim Çizelgeleme"
  - "Hazırlık Süresi Tanımlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Üretim / MRP / Kayıt / MRP / İleri Üretim Çizelgeleme / Hazırlık Süresi Tanımlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTVkZTA1ZWZkLWE1NTMtNDNjNy04NmIzLThkMDljZjQwYjZiYSZsaW5rPWU0MTk3OGZmLTM3MzYtNGVkOS04ODViLWZhNzhhMDM0OGY2OSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=5de05efd-a553-43c7-86b3-8d09cf40b6ba&link=e41978ff-3736-4ed9-885b-fa78a0348f69&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "hazirlik-suresi-tanimlama_50673726_50673505.html"
source_version: "2022-10-18T15:15:46.677+03:00"
source_bytes: 9913
fetched_at: "2026-09-13T04:19:42+00:00"
generator: "netsis-scraper 1.0.0"
---
# Hazırlık Süresi Tanımlama

Hazırlık Süresi Tanımlama, Üretim Bölümü'nde Kayıt/MRP menüsünün altında yer alır. Beş farklı tipte hazırlık tanımlamasının yapıldığı bölümdür.

Hazırlık Süresi Tanımlama ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Hazırlık Süresi Tanımlama Ekranı |  |
| --- | --- |
| Operasyon | Hazırlık süresinin tanımlanacağı operasyonun seçildiği alandır. Operasyon Kodu, Operasyon Grubu veya Tümü seçenekleri arasından seçim yapılır. Operasyon Kodu ya da Operasyon Grubu seçilirse, “Operasyon Değer” alanı da hazırlık süresinin hangi operasyonlar veya operasyon grupları bazında geçerli olacağı bilgisine göre girilir. |
| Hazırlık Süresi Tipi | Hazırlık süresi tipinin seçildiği alandır. Kendisine Ait Hazırlık Süresi, Ürün Değişimi, Kaynak Değişimi, Operasyon Değişimi ve Script tipleri arasından seçim yapılır. **Kendisine Ait Hazırlık Süresi:** Operasyonun kendisine ait bir hazırlık süresi tanımlanacağı zaman seçilecek tiptir. **Ürün Değişimi:** Bir üründen diğerine geçilirken bir hazırlık söz konusu olduğunda seçilecek tiptir. Ürün değişimi seçildiği takdirde yeni alanlar ekrana gelir. Bu alanlara hangi üründen (Mevcut Ürün Seçimi) hangi ürüne (Sonraki Ürün Seçimi) geçiş için hazırlık süresi tanımlaması yapılacağı bilgisi girilir. Ürün Grubu, Ürün Kodu ya da Tümü seçeneklerinden uygun olanlar seçilip Ürün Kodu ya da Ürün Grubu seçildiyse, ayrıca “Ürün Değer” bilgisinin de girilmesi gerekir. **Kaynak Değişimi:** “Kaynak Değişimi” tipli hazırlık süresi seçildiğinde de yeni alanlar ekrana gelir. Burada da aynı şekilde hangi kaynaktan (Mevcut Kaynak Seçimi) hangi kaynağa (Sonraki Kaynak Seçimi) geçiş için hazırlık süresi tanımlaması yapılacağı bilgisi girilir. Kaynak Kodu ya da Kaynak Grubu için giriş yapılacaksa, “Kaynak Değer” bilgisinin de girilmesi gerekir. **Operasyon Değişimi:** “Operasyon Değişimi” tipli hazırlık süresi seçildiğinde ise yalnızca “Önceki Operasyon Seçimi” alanı görüntülenir. Bu alanda da Operasyon Kodu ya da Operasyon Grubu bazında seçim yapılabilir veya Tümü seçeneği seçilebilir. "Önceki Operasyon Seçimi" alanında ne tanımlandıysa, bu tanımdan mevcut operasyon alanında tanımlanan değere geçişte, girilen hazırlık süresi kullanılır. **Script:** İstenen bir script kodunun yazılması için alan oluşturulmasını sağlar. |
| Makine Bilgileri | Hazırlık süresi, seçilen hazırlık süresi tipi için makine bazında da değişkenlik gösteriyorsa ayrıca “Makine Bilgileri” alanına da tanımlama yapılması gerekir. Makine Kodu, Makine Grubu veya Tümü seçenekleri arasından seçim yapılır. Makine Kodu ya da Makine Grubu seçilirse, “Makine Değer” alanı da hazırlık süresinin hangi makineler veya makine grupları bazında geçerli olacağı bilgisine göre girilir. **Örneğin;** Ürün Değişimi tipli bir hazırlık süresi, A ürününden B ürününe geçiş için tanımlanmış olsun. Fakat bu geçiş, üretim Makine1’de yapıldığında 20 dakika, Makine2’de yapıldığında 30 dakika sürüyor olsun. Böyle bir durumda A’dan B’ye hazırlık süresi tanımlanırken makine bilgileri alanının da kullanılması ve her 2 makine için ayrı ayrı hazırlık süresi tanımlanması gerekir. |
| Hazırlık Süresi İşe Bağlı Değil | Hazırlık süresinin başlaması için, bir önceki operasyonun tamamlanıp, yarı mamullerin tanımlanmakta olan operasyona gelmesinin beklenmesi gerekmediğinde kullanılan seçenektir. |
| Kendisi Dahil | Tümü'nden Tümü'ne seçimli geçişler içi kullanılan seçenektir. Böyle bir seçim yapıldığı ve bu seçeneğin de işaretlendiği varsayıldığında, geçiş A ürününden A ürününe olsa bile, tanımlanan hazırlık süresi kullanılır. Seçeneğin işaretlenmediği durumda ise A ürününden A ürününe geçişte hazırlık süresi olmadığı varsayılır. |
| Hazırlık Süresi | Hazırlığın ne kadar sürdüğünü kaydetmek için kullanılan alandır. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır.

Kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
