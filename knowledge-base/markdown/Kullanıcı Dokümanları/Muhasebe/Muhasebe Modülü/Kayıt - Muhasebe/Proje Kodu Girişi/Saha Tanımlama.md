---
title: "Saha Tanımlama"
page_id: "24740495"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Muhasebe"
  - "Muhasebe Modülü"
  - "Kayıt / Muhasebe"
  - "Proje Kodu Girişi"
  - "Saha Tanımlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / Kayıt / Muhasebe / Proje Kodu Girişi / Saha Tanımlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTdjMjU4NGViLTU0MGEtNGVhMi04Yjk4LTYxNTUyNmM2MzdiNiZsaW5rPWQ1NTE0MDY1LTQwYTktNDNmNC04N2ZkLTdmZDlmNDc1OTk0ZSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=7c2584eb-540a-4ea2-8b98-615526c637b6&link=d5514065-40a9-43f4-87fd-7fd9f475994e&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "saha-tanimlama_39419989_24740495.html"
source_version: "2022-09-27T14:48:18.493+03:00"
source_bytes: 52326
fetched_at: "2026-09-13T04:12:56+00:00"
generator: "netsis-scraper 1.0.0"
---
# Saha Tanımlama

Saha Tanımlama, Muhasebe Bölümü'nde, "Kayıt/Muhasebe Modülü" menüsünün altında yer alır. Saha Tanımlama, eklenecek olan saha ile ilgili genel tanımlamaların yapıldığı bölümdür. Saha Tanımlama, Saha Tanımlama ve Ön Değer Tanımlama olmak üzere iki sekmeden oluşur.

**Saha Tanımlama**

![](../../../../../_assets/f2ea0ed01dce9ae2d2c5.png)

Saha Tanımlama ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Kullanıcı Saha Tanımlamaları Ekranı |  |
| --- | --- |
| Alan Adı | Tanımlanan yeni alanlar, eklendiği tabloda yeni bir saha olarak yer alır. Burada verilen isim, tablodaki sahanın ismidir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile tanımlı alan adlarına ulaşılır. Buraya girilen alan adının başına program tarafından “KT\_” ön değeri aktarılır. Bunun sebebi, alanının kullanıcı tarafından tanımlandığının belirlenmesidir. Tanımlanan ön değer değiştirilmez/kaldırılmaz. Bu sahalar “Saha Tablo Eşleştirme” bölümünde "Alan Adı" sahasında görüntülenir. "Alan Adı" verilirken boşluk ve Türkçe karakterin kullanılmaması gerekir. |
| Alan Tipi | Tanımlanan alana uygun tipin girildiği alandır. Karakter, Karakter Dizesi, Tam Sayı, Ondalık Sayı, Bayt ve Tarih seçeneklerinden oluşur. Alanın sağ tarafında yer alan aşağı ok butonu ile seçim yapılır. **Örneğin,** tanımlanan saha, tarih bilgisi için kullanılacaksa “Tarih” seçeneğinin seçilmesi gerekir. |
| Başlık | Tanımlanan sahanın ekranda görüntülenmesi istenen başlığının girildiği alandır. Belirlenen başlık daha sonra değiştirilebilir. |
| Bileşen Tipi | Ekranda sahaların görüntülenmesi sırasında bazı bileşenler kullanılır. Görünen her bir saha, kendi tipinin gerektirdiği özellikleri taşıyan bir bileşenle eşleştirilir. Burada da, tanımlanan sahanın ekran bileşenleri arasından eşleştirilmesi istenen tip belirlenir. Alanın sağ tarafında yer alan aşağı ok butonu ile; Kombo Seçim Alanı, Yazı Alanı, Onay Kutusu, Çoklu Onay Grubu ve Metin Alanı seçenekleri arasından tercih yapılır. |
| Ön Değer | Tanımlanan saha için, yeni kayıtta ön değer aktarılası istendiğinde kullanılan alandır. |
| Uzunluk | Tanımlanan sahaya bilgi girişi yapılması istenen karakter sayısının girildiği alandır. |

**Ön Değer Tanımlama**

Ön Değer Tanımalama, "Bileşen Tipi" alanında "Kombo Seçim Alanı" ya da "Çoklu Onay Grubu seçilmesi halinde, kullanıcının içinden seçim yapacağı seçeneklerin combo ya da radio içine program tarafından yerleştirilmesi için tanımlama yapılmasını sağlayan sekmedir.

![](../../../../../_assets/0539bdaf5cf06baa787c.png)

Kullanıcı Saha Tanımlamaları ekranı Öndeğer Tanımlama sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Kullanıcı Saha Tanımlamaları Ekranı |  |
| --- | --- |
| Gösterim Sırası | Tanımlanan ön değerin ekrana getirileceği gösterim sırasının girildiği alandır. |
| Değer | Tanımlanan sahanın alacağı değerin girildiği alandır. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır. Kullanıcı Saha Tanımlamaları kaydının iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
