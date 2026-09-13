---
title: "NDI Bağlantı Tanımlamaları"
page_id: "41170616"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Genel"
  - "Yardımcı Programlar"
  - "Kayıt / Yardımcı Programlar"
  - "NDI"
  - "NDI Bağlantı Tanımlamaları"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Yardımcı Programlar / Kayıt / Yardımcı Programlar / NDI / NDI Bağlantı Tanımlamaları"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWJiZjcyZmU3LWEwZmUtNDk0Yi05NTQ2LTExZDM5Y2IxMDJiYiZsaW5rPWRmOGRlZWI4LWZkNzEtNDkzOS1iZDYzLTQ1OTYzZWRkMjgyZCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=bbf72fe7-a0fe-494b-9546-11d39cb102bb&link=df8deeb8-fd71-4939-bd63-45963edd282d&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ndi-baglanti-tanimlamalari_47072928_41170616.html"
source_version: "2022-10-05T09:55:07.377+03:00"
source_bytes: 44625
fetched_at: "2026-09-13T04:17:22+00:00"
generator: "netsis-scraper 1.0.0"
---
# NDI Bağlantı Tanımlamaları

NDI Bağlantı Tanımlamaları, Yardımcı Programlar → Kayıt → [İşletme/Şube/Parametre Tanımlamaları](<../Şirket - Şube - Parametre Tanımları.md>) → “NDI Uygulaması Var” parametresinin işaretlenmesi ile aktif hale gelen NDI menüsünün altında yer alır. NDI Bağlantı Tanımlamaları ekranından yapılan tanımlamalar ile, Temelset paketindeki şubelerden hangi NDI şirketine, hangi kullanıcı ile bağlanılacağı belirlenir.

![](../../../../../_assets/dfcb57133183be464b88.png)

NDI Bağlantı Tanımlamaları ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| NDI Bağlantı Tanımlamaları Ekranı |  |
| --- | --- |
| İşletmelerde Ortak | Tanımlanan bağlantı için geçerli olacak işletmenin/işletmelerin belirlendiği alandır. Temelset-NDI bağlantısının tüm işletmelerde geçerli olması için -1, sadece belirli bir işletmede geçerli olması için de ilgili işletme kodunun girilmesi gerekir. Bu alan sadece Enterprise paketinde merkez işletmede iken aktif hale gelir. Bağlantı tanımlaması, merkez işletmede yapılmıyorsa, "İşletme Kodu" alanı pasif olarak görünür ve içinde bulunulan işletme kodu program tarafından ekrana getirilir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, işletme kodlarına ulaşılır. |
| Şubelerde Ortak | Tanımlanan bağlantı için geçerli olacak şubenin/şubelerin belirlendiği alandır. Temelset-NDI bağlantısının tüm şubelerde geçerli olması için -1, sadece belirli bir şubede geçerli olması için de ilgili şube kodunun girilmesi gerekir. Bu alan sadece merkez şubede iken aktif hale gelir. Bağlantı tanımlaması, merkez şubede yapılmıyorsa, "Şube Kodu" alanı pasif olarak görünür ve içinde bulunulan şube kodu, program tarafından ekrana getirilir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, şube kodlarına ulaşılır. |
| NDI Şirket Adı | Bağlantı kurulacak NDI şirketinin belirlendiği alandır. Alanın sağ tarafında bulunan aşağı ok tuşu ile, NDI paketinde tanımlı şirket isimleri listelenir. "İşletmelerde Ortak" ve "Şubelerde Ortak" alanları kullanılarak, birden fazla işletme ve şubenin tek bir NDI şirketi ile bağlantısı sağlanır. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır. NDI Bağlantı Tanımlamaları ekranından yapılan kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
