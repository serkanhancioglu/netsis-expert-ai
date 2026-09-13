---
title: "Ürün Profil ve Yapılandırma Kodu Tanımlamaları"
page_id: "29993452"
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
  - "Ürün Profil ve Yapılandırma Kodu Tanımlamaları"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Stok / Kayıt / Stok / Esnek Yapılandırma / Ürün Profil ve Yapılandırma Kodu Tanımlamaları"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWY5Mzg4ZDI0LWNiODMtNDc1NS04ZWRiLTUxY2ViODY0MDU4OCZsaW5rPTVhZGQ5N2JiLWI4ZGYtNDliNi04YjdjLTQ3MWU1MjczOWU3YyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=f9388d24-cb83-4755-8edb-51ceb8640588&link=5add97bb-b8df-49b6-8b7c-471e52739e7c&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "urun-profil-ve-yapilandirma-kodu-tanimlamalari_29993454_29993452.html"
source_version: "2022-10-25T15:14:35.420+03:00"
source_bytes: 15444
fetched_at: "2026-09-13T04:03:56+00:00"
generator: "netsis-scraper 1.0.0"
---
# Ürün Profil ve Yapılandırma Kodu Tanımlamaları

Ürün Profil ve Yapılandırma Kodu Tanımlamaları, Lojistik - Satış Bölümü'nde, "Kayıt/Stok" menüsünün altında yer alır. Ürün Profil ve Yapılandırma Kodu Tanımlamaları, Esnek Yapılandırma sisteminde, yapılandırma yapılacak stok kartına ait ürün profillerinin tanımlanması ve ürünün çeşitli konfigürasyonlarını belirten yapılandırma kodlarının tanımlanması için kullanılan bölümdür. Ürün Profil ve Yapılandırma Kodu Tanımlamaları; Ürün Profil Tanımlamaları, Özellik Değer Kısıtları ve Yapılandırma Kodu Tanımlamaları olmak üzere üç sekmeden oluşur.

Ürün Profil ve Yapılandırma Kodu Tanımlamaları bölümünün kullanılması için; "[Özel Parametre Tanımlamaları](<../../../../Genel/Yardımcı Programlar/Kayıt - Yardımcı Programlar/Özel Parametre Tanımları.md>)" ekranında aşağıdaki tanımlamaların yapılması gerekir:

| Özel Parametre Tanımlamaları Ekranı |  |
| --- | --- |
| Grup Kodu | STOK |
| Anahtar | URUN_PROFIL_ESKI |

**Ürün Profil Tanımlamaları**

Ürün Profil Tanımlamaları sekmesinde yer alan bilgileri aşağıdaki şekildedir:

| Ürün Profil ve Yapılandırma Kodu Tanımlamaları Ekranı |  |
| --- | --- |
| Stok Kodu | Yapılandırması yapılacak ürünün kodunun girildiği alandır. Alanın sağ tarafında bulunan rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile "Stok Kartı Kayıtları" bölümünde "Esnek Yapılandır" seçeneği işaretli olan stoklar listelenir ve sadece bu stoklar için yapılandırma yapılır. |
| Sıra No | Ürüne tanımlanacak özelliğin sırasının belirlendiği alandır. Belirlenen özellik kodları, verilen sıra numarasına göre grid ekranda sıralanır. Bu alana 1'den başlamak üzere istenen (tam sayı) değer girilir. Aynı ürün içinde sıra numarası tekrar edemez. |
| Özellik Kodu | Ürünün sahip olduğu özelliğe ait kodun girildiği alandır. Bu alana girilecek özelliğin daha önceden "Özellik Tanımlamaları" sekmesinde tanımlanması gerekir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, tanımlı özellik kodlarına ulaşılır. |
| Sütun | 'Yapılandırma Kodu Tanımlamaları' sekmesinde kolon başlığı olacak özellik kodunun belirlenmesini sağlayan seçenektir. Sütun seçeneği, tek bir özellik için işaretlenebilir. |

#### Özellik Değer Kısıtları

"Esnek Yapılandırma" yapılacak ürüne ait özellikler "Ürün Profil Tanımlamaları" sekmesinde belirlendikten sonra, ürünün sahip olduğu konfigürasyonlar "Yapılandırma Kodu Tanımlamaları" sekmesinde seçilir. "Yapılandırma Kodu Tanımlamaları" matrisine, "Ürün Profil Tanımlamaları" sekmesinde bulunan özelliklere ait tüm değerler gelir. "Özellik Değer Kısıtları" sekmesinde yapılacak seçimler sayesinde, birden fazla özelliğe sahip ürünler arasında seçim yapmayı kolaylaştırmak için matrise gelecek değerlerin kısıtlanması sağlanır. Verilen kısıt sonucu, matrisin boyutu küçüleceği için, tanımlama yapmak daha kolay hale gelir.

"Özellik Değer Kısıtları" sekmesinde, ürünün sahip olduğu özelliklere ait değerler listelenir. Bu değerlerden hangilerinin matriste bulunması isteniyorsa, ilgili değerin solunda bulunan kutucuk işaretlenir. "Yapılandırma Kodu Tanımlamaları" sekmesine geçmek için, ekranda bulunan her özellik için en az bir değerin seçilmesi gerekir. "Özellik Değer Kısıtları" sekmesinde bulunan değerlerin hepsinin matrise getirilmesi isteniyorsa, kısıt ekranındaki stok kodunun solunda yer alan kutucuğun işaretlenmesi gerekir. Böylece, sekmede bulunan değerlerin hepsi program tarafından matrise aktarılır. İlgili stok için daha önceden tanımlanmış yapılandırma kodları varsa, bu kodlar için kullanılan değerler "Özellik Değer Kısıtları" sekmesine otomatik olarak seçili halde gelir. Kısıt sekmesinde, seçili gelen değerlerden farklı değer belirlenerek matrise geçiş yapılabilir.

Ekranda, sadece matrise gelmesi için seçilen değerlerin görüntülenmesi istendiğinde "Sadece Seçilenler" ![](../../../../../_assets/5eb464fd98279c2a48fe.png) butonu kullanılır. Seçilmemiş değerlerin tekrar ekrana gelmesi için ikinci kez butona basılması gerekir.

#### Yapılandırma Kodu Tanımlamaları

Ekranda boş hücrelerin üzerinde çift tıklandığı zaman ya da klavyedeki boşluk çubuğu ile devam edildiğinde yeni bir yapılandırma kodu tanımlanır. Bu işlem ile oluşturulan yapılandırma kodları, program tarafından otomatik olarak aktarılır . Oluşturulan yapılandırma kodlarının belli bir düzende olması isteniyorsa "Yapılandırma Başlangıç Numaraları" menüsünde gerekli tanımlamaların yapılması gerekir. Program tarafından otomatik olarak oluşturulan yapılandırma kodlarının açıklamaları, "Stok Parametreleri" bölümünde "Yapılandırma Açıklaması Kullanım Şekli" alanında yapılan tercihe göre oluşur.

"Yapılandırma Açıklaması Kullanım Şekli" ile ilgili detaylı bilgi için; Stok → Kayıt → [Stok Parametreleri](<../Stok Parametreleri.md>) İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır. Yapılan kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
