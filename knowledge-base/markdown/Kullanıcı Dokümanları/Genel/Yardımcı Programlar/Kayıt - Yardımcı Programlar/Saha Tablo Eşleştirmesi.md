---
title: "Saha Tablo Eşleştirmesi"
page_id: "41170622"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Genel"
  - "Yardımcı Programlar"
  - "Kayıt / Yardımcı Programlar"
  - "Saha Tablo Eşleştirmesi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Yardımcı Programlar / Kayıt / Yardımcı Programlar / Saha Tablo Eşleştirmesi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWUyY2U3ODE0LTNiYmEtNDA3Zi04NDI3LTY0YTI0OThhZmYxMyZsaW5rPTAwZjc5MTVjLTViM2EtNDJiZi1iZGY0LWQxNTU2OTlmMWUyZCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=e2ce7814-3bba-407f-8427-64a2498aff13&link=00f7915c-5b3a-42bf-bdf4-d155699f1e2d&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "saha-tablo-eslestirmesi_47073086_41170622.html"
source_version: "2022-10-05T10:55:37.733+03:00"
source_bytes: 17566
fetched_at: "2026-09-13T04:17:28+00:00"
generator: "netsis-scraper 1.0.0"
---
# Saha Tablo Eşleştirmesi

Saha Tablo Eşleştirmesi, Genel Bölümü'nde, "Kayıt/Yardımcı Programlar" menüsünün altında yer alır. Saha Tablo Eşleştirmesi; Muhasebe (Proje Sabit Tanımları), Üretim (İş Emri, Üretim Sonu Kaydı, Reçete), Finans (Cari Hesap Kayıtları, Cari Planlama Kayıtları), Lojistik/Satış (Stok Kartı Kayıtları, Stok Planlama Kayıtları, Müşteri/Satıcı Stok Kayıtları), MRP (Kaynak Tanımlama, Makine Tanımlama), Makine Bakım ( Bakım Emirleri) ve Üretim Akış Kontrol (Üretim Akış Kaydı) kayıtlarında kullanılması için ekstra saha tanımlamalarının yapıldığı bölümdür. İlk olarak "Saha Tanımlamaları" sekmesinden sahaların tanımlanması, daha sonra da tanımlı sahaların hangi ekranlarda kullanılacağının belirlenmesi amacıyla saha ve tablo eşleştirmesinin yapılması gerekir.

**Saha Tanımlamaları**

Saha Tablo Eşleştirmesi ekranı Saha Tanımlamaları sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Saha Tablo Eşleştirmesi Ekranı |  |
| --- | --- |
| Alan Adı | Tanımlanan yeni alanlar, eklendiği tabloda yeni bir saha olarak yer alır. Burada verilen isim, tablodaki sahanın ismidir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile tanımlı alan adlarına ulaşılır. Buraya girilen alan adının başına program tarafından “KT\_” ön değeri aktarılır. Bunun sebebi, alanının kullanıcı tarafından tanımlandığının belirlenmesidir. Tanımlanan ön değer değiştirilmez/kaldırılmaz. Bu sahalar “Saha Tablo Eşleştirme” bölümünde "Alan Adı" sahasında görüntülenir. "Alan Adı" verilirken boşluk ve Türkçe karakterin kullanılmaması gerekir. |
| Alan Tipi | Tanımlanan alana uygun tipin girildiği alandır. Karakter, Karakter Dizesi, Tam Sayı, Ondalık Sayı, Bayt ve Tarih seçeneklerinden oluşur. Alanın sağ tarafında yer alan aşağı ok butonu ile seçim yapılır. **Örneğin,** tanımlanan saha, tarih bilgisi için kullanılacaksa “Tarih” seçeneğinin seçilmesi gerekir. |
| Başlık | Tanımlanan sahanın ekranda görüntülenmesi istenen başlığının girildiği alandır. Belirlenen başlık daha sonra değiştirilebilir. |
| Bileşen Tipi | Ekranda sahaların görüntülenmesi sırasında bazı bileşenler kullanılır. Görünen her bir saha, kendi tipinin gerektirdiği özellikleri taşıyan bir bileşenle eşleştirilir. Burada da, tanımlanan sahanın ekran bileşenleri arasından eşleştirilmesi istenen tip belirlenir. Alanın sağ tarafında yer alan aşağı ok butonu ile; Kombo Seçim Alanı, Yazı Alanı, Onay Kutusu, Çoklu Onay Grubu ve Metin Alanı seçenekleri arasından tercih yapılır. |
| Ön Değer | Tanımlanan saha için, yeni kayıtta ön değer aktarılası istendiğinde kullanılan alandır. |
| Uzunluk | Tanımlanan sahaya bilgi girişi yapılması istenen karakter sayısının girildiği alandır. |

**Öndeğer Tanımlama**

Öndeğer Tanımlama sekmesi, "Bileşen Tipi" alanında "Kombo Seçim Alanı" ya da "Çoklu Onay Grubu seçilmesi halinde, kullanıcının içinden seçim yapacağı seçeneklerin combo ya da radio içine program tarafından yerleştirilmesi için tanımlama yapılmasını sağlayan sekmedir.

Saha Tablo Eşleştirmesi ekranı Öndeğer Tanımlama sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Saha Tablo Eşleştirmesi Ekranı |  |
| --- | --- |
| Gösterim Sırası | Tanımlanan ön değerin ekrana getirileceği gösterim sırasının girildiği alandır. |
| Değer | Tanımlanan sahanın alacağı değerin girildiği alandır. |

**Saha Tablo Eşleştirmeleri**

Saha Tablo Eşleştirmeleri sekmesi, "Saha Tanımlama" bölümünden eklenen alanların "Proje Sabit Tanımları" ekranında görüntülenmesini sağlar.

Saha Tablo Eşleştirmesi ekranı Saha Tablo Eşleştirmeleri sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Saha Tablo Eşleştirmesi Ekranı |  |
| --- | --- |
| Alan Adı | "Saha Tanımlama" bölümünde tanımlanan ve tabloya eklenmesi istenen sahanın seçildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, tanımlı alanlara ulaşılır. |
| Aktif | Eklenen sahanın ekranda görüntülenmesi için işaretlenmesi gereken seçenektir.<br>İşaretlenmediğinde, saha tabloya eklense bile giriş ekranlarında kullanılamaz. Bu alan, daha önceden eklenen fakat artık kullanılması istenmeyen sahaların silinememesinden dolayı, sadece pasif hale getirmek için kullanılabilir. |
| Zorunlu | Tabloya eklenen sahanın, kayıt girişi sırasında boş bırakılmaması için işaretlenmesi için kullanılan seçenektir. |
| Altına Çizgi Çekilsin | Eklenen sahanın ekranda görüntülenirken, saha adı altına çizgi eklenmesi için kullanılan seçenektir. |
| Gösterim Sırası | Eklenen sahanın "Proje Sabit Tanımları" ekranında "Kullanıcı Tanımlı Sahalarının" içinde gösterilmesi istenen sıranın belirlendiği alandır. Tanımlı saha, tabloya eklendikten sonra silinmez. Eşleştirme kaydı yapılırken ilgili sahanın tabloya eklenip eklenmeyeceği sorgulanır.<br>Onaylama ekranında “Evet” seçilmesi durumunda, saha eşleştirildiği tabloya eklenir. Onaylama ekranında “Hayır” seçilmesi halinde ilgili saha tabloya eklenmez. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır. Saha Tablo Eşleştirmesi kaydının iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
