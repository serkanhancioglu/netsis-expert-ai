---
title: "NDI Nesneleri"
page_id: "41170618"
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
  - "NDI Nesneleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Yardımcı Programlar / Kayıt / Yardımcı Programlar / NDI / NDI Nesneleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTgzMTdhYjBiLWEwZjUtNDMxYy05YTMwLWNlMzE4ZDBhMTczOCZsaW5rPTI5NTc1YTgzLWJlMDktNGUxMS05YzllLTdjNzA4NzhlM2E2ZSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=8317ab0b-a0f5-431c-9a30-ce318d0a1738&link=29575a83-be09-4e11-9c9e-7c70878e3a6e&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ndi-nesneleri_47072948_41170618.html"
source_version: "2022-10-05T09:58:11.617+03:00"
source_bytes: 47493
fetched_at: "2026-09-13T04:17:22+00:00"
generator: "netsis-scraper 1.0.0"
---
# NDI Nesneleri

NDI Nesneleri, Yardımcı Programlar → Kayıt → [İşletme/Şube/Parametre Tanımlamaları](<../Şirket - Şube - Parametre Tanımları.md>) → “NDI Uygulaması Var” parametresinin işaretlenmesi ile aktif hale gelen NDI menüsünün altında yer alır. NDI Nesneleri, NDI paketinde hazırlanan ekran ve rehberlerin listelenmesi ve bu nesnelerin Temelset modüllerine eklenmesi için kullanılan bölümdür. Temelset içinden kullanılacak her bir NDI nesnesinin mutlaka tanımlanması gerekir.

![](../../../../../_assets/6a23255dc406be01559f.png)

Paket için NDI Nesnelerini Tanımlama ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Paket için NDI Nesnelerini Tanımlama Ekranı |  |
| --- | --- |
| Program Numarası | Pakete eklenen her bir NDI nesnesine tekrarı olmayan serbest bir numara verilmesi gerekir. Verilen program numaraları daha sonra "Kullanıcı İşlemleri" modülünde, kullanıcılara nesne ile ilgili hakların belirlenmesi sırasında gerekir. NDI paketinde tanımlanan nesne ve rehberler, Temelset paketine eklendikten sonra, Admin yetkisine sahip olmayan kullanıcılar için, bu nesnelere ait hak tanımlaması yapılır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, program numaralarına ulaşılır. Eklenen nesnelere ait yetki tanımlamaları ile ilgili detaylı bilgi için; Ek-2 (NDI Kullanıcı Hakları ve Rehber Tanımlamaları) dokümanına bakılabilir. |
| Kullanılacak Modül Numarası | NDI paketinde tanımlanan ekranların kullanılacağı Temelset modülünün seçildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile seçim yapılır. İlgili ekranın bütün modüllerde kullanılması için "Tüm Modüller" seçeneğinin seçilmesi gerekir. NDI’da tanımlanan rehberlerin Temelset paketine eklenmesi sırasında, seçilen "Kullanılacak Modül Numarası" bilgisinin herhangi bir geçerliliği yoktur. Rehberler, Temelset paketi içinden hazırlanan diğer ek rehberler gibi tüm modüllerde kullanılabilir. |
| Başlık | Eklenen ekran ve rehberlerin başlık bilgisi olup,Merkezi Kimlik Denetimi → "Kullanıcı Program Yetkileri Tanımlama" bölümünde, bu alanda belirlenen isimleri ile listelenir. Ayrıca, tanımlı ekranların Temelset modüllerine eklenmesi halinde, ekranlar için "Başlık" alanında girilen bilgiler, modül ana menüsüne gelecek "NDI Uygulamaları" başlığının altında listelenir. Örneğin; NDI paketinde hazırlanan “Vardiya Çalışanları” başlıklı ekranın, "Üretim" modülüne eklenmesi sırasında, başlık bilgisi olarak “Vardiya Çalışan Kayıtları” girilmesi durumunda, Üretim → NDI Uygulamaları menüsü aşağıdaki şekilde görüntülenir. |
| Grup Başlığı | Modül ana menüsüne eklenen ekranın, menüde bir alt başlık altında listelenmesi için kullanılan alandır. Nesne, ilgili modüldeki "NDI Uygulamaları" menüsünde, tanımlamada verilen grup başlığının altında listelenir. Program Numarası, Kullanılacak Modül Numarası, Başlık bilgisi ve isteğe bağlı Grup Başlığı bilgisi girildikten sonra eklenecek nesne, NDI paketinde hazırlanan nesnelerin bulunduğu listeden seçilir. |

**Grid ile NDI Nesneleri Seçimi**

Grid listesinde bulunan nesneler, Nesne Tipleri bazında sıralanır. Nesne Tipi sütununda **E** olması halinde ilgili nesnenin ekran, **R** olması halinde ise nesnenin rehber olduğu anlaşılır. Nesnenin seçimi için, nesne üzerinde iken farenin sol tuşuna iki kez tıklanması gerekir. Ekrana gelen onay sorusuna, seçilen nesnenin Temelset paketine eklenmesi için "Evet" yanıtı verilir.

Eklenen nesneler ile ilgili değişiklik yapılması için, grid ekrandan istenen değişiklik yapılarak tekrar kaydedilmesi gerekir. Temelset paketinden çıkartılması istenen nesneye ait tanımlama seçildikten sonra klavyede bulunan F7 tuşuna basılması ya da ekranın araç çubuğunda yer alan ![](../../../../../_assets/2df4b343310bcd16b01e.jpg) Kayıt Sil butonuna tıklanması gerekir.

Grid ile NDI Nesneleri Seçimi için yapılması gerekenler şunlardır:

- NDI paketinde tanımlanan ekran ve rehberlerin bu listede görüntülenmesi ve dolayısıyla Temelset paketine eklenmesi için, ilgili ekranın NDI paketindeki tanımlamaları sırasında seçilen veri tabanı bağlantı koduna ait tanımlamada paket bilgisi olarak "Temelset" ve "Hesaplanacak" seçeneklerinin işaretlenmesi gerekir.
- NDI paketinde ekran tanımlaması yapılırken, form tipi olarak "Normal" seçeneğinin seçilmesi gerekir. "Child" olarak tanımlanan ekranlar Temelset paketine eklenemez.
- Birden fazla NDI şirketinin olması ve bunlardan birisi için, içinde bulunulan şube ile bağlantı tanımlanması halinde, söz konusu liste için bağlantı tanımlaması yapılsın veya yapılmasın tüm NDI şirketlerinde tanımlanan nesneler görüntülenir. Ancak, bağlantı tanımlanmamış NDI şirketinde oluşturulan nesneler, bu bölümden Temelset menüsüne eklenmesine rağmen, menüde görülmez. Bu yüzden, nesnelerin tanımlı olduğu NDI şirketi için mutlaka NDI-Temelset bağlantı tanımlamasının yapılması gerekir.
