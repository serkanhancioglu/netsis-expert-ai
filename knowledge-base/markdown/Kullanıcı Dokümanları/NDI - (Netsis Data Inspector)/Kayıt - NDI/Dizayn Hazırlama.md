---
title: "Dizayn Hazırlama"
page_id: "50682705"
product: "netsis-3-enterprise"
depth: 4
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "NDI - (Netsis Data Inspector)"
  - "Kayıt / NDI"
  - "Dizayn Hazırlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / NDI - (Netsis Data Inspector) / Kayıt / NDI / Dizayn Hazırlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTM0NGFhZGI4LTM3MjMtNGZmMy1hNzY3LWI0YzdmYjQ5NmE4YyZsaW5rPWMyYjgwODg5LTg5MzctNGZkYy05NjQ5LTczMjg5MTFjMTdlMSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=344aadb8-3723-4ff3-a767-b4c7fb496a8c&link=c2b80889-8937-4fdc-9649-7328911c17e1&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "dizayn-hazirlama_50682710_50682705.html"
source_version: "2022-09-16T09:41:27.257+03:00"
source_bytes: 14951
fetched_at: "2026-09-13T04:20:48+00:00"
generator: "netsis-scraper 1.0.0"
---
# Dizayn Hazırlama

Dizayn Hazırlama bölümü ile, NDI aracılığıyla hazırlanan tüm ekran dizaynlarının toplu şekilde izlenmesi sağlanır. Dizayn Hazırlama bölümünde, dizaynların ana bilgileri yönetilir ve seçili dizaynla ilgili olarak dizayn ortamına geçilebilir. Dizaynların yönetimini ve dizayn ortamında yapılacaklardan önce dikkat edilmesi gereken, NDI uygulamasında dizayn hazırlamak ve görsel bir programlama aracı ile program yazmaktan farklı değildir.

Örneğin; Visual Basic ile program yazmaya benzer. O nedenle NDI kullanacak kişilerin programlama mantığı ve görsel programlama aracıyla program yazma deneyiminin bulunması gerekir. NDI uygulamasında ve bu dokümandaki birçok deyim programlama jargonu olup, açıklamaları programlama bilgisi olmadığı durumda anlaşılmayabilir.

Dizayn Hazırlama ekranında yer alan bilgiler ve açıklamaları aşağıdaki şekildedir:

| Dizayn Hazırlama Ekranı |  |
| --- | --- |
| Kod | NDI aracılığıyla yapılan her dizayn için tekrarsız bir kod verme zorunluluğu bulunur. Kullanıcı, kendi sistematiğine göre kodlama yapabilir. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile, dizayn rehberine ulaşılır. |
| Başlık | Dizayn başlığı bilgisidir. Bu bilgi aynı zamanda kullanım sırasında açılan ekranın başlığı olacağı için açıklayıcı bir bilgi yazılmasında fayda vardır. |
| Veritabanı İlişkili | Hazırlanan dizaynın veritabanı ile ilişkili olması halinde kullanılan seçenektir. |
| Tarih | Dizaynın yapıldığı ilk tarih bilgisi olarak saklanabilecek alandır. |
| Tablo Adı | Dizayn ile ilişkili olan, veri girişi yapılacak tablonun veritabanındaki adıdır. Tablonun dizayn öncesi, veritabanında SQL komutları yardımıyla oluşturulması gerekir. NDI, tablo oluşturma işlevini içermez. |
| Veritabanı Kodu | NDI ile birden fazla veritabanında bulunan tablolar için dizayn yapılabilir. **Örneğin;** Hem Temelset hem de Personel veritabanlarına ait dizaynlar yapılabilir. Her bir veritabanı bağlantısı tanımına bir kod verilir. Bu alanda ise, tanımlanan veri tabanı bağlantılarından<br>hangisinin kullanılacağı, veri tabanı bağlantı kodu verilerek belirlenir. Tanımlı veri tabanı bağlantıları, rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg)ile de, belirlenebilir. |
| Grup Kodu | Hazırlanan dizaynların gruplanması için, ilgili dizaynın içinde yer alacağı grubun belirlendiği alandır. Kullanıcı, kendi sistematiğine göre gruplandırma yapabilir. Herhangi bir grup kodu verilmezse NDI,<br>dizaynı GENELDIZAYN grubu altına alır. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile, grup kodlarına ulaşılır. |
| Ortam | NDI dizaynlarda, birden fazla ortam desteklenir. Dizayn; D-Win32, WWML, H-HTML, ya da P-Pocket PC ortamlarında çalıştırılması için hazırlanır. Alanın sağ tarafında yer alan aşağı ok butonu ile seçim yapılır. Ancak her bir dizayn sadece bir ortamda çalışabilir. Dizayn için ortam belirlenip dizayn saklandıktan sonra ortam değişikliği yapılması mümkün değildir. Win-32; Windows ortamında çalışacak ekran, HTML ise; İnternet Browser’de çalışacak ekran anlamına gelir. |
| Form Tipi | Tasarlanan formun belirlendiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile; N-Normal ya da C-Child seçenekleri arasından seçim yapılır. "Normal" formlar açıldıkları pencereden bağımsız olup yeni bir ekran şeklinde düşünülebilir. "Child" formlar ise açıldıkları pencere içinde çalışırlar. **Örneğin;** "Stok" modülü ana menüsü Normal formdur, bu modülün içinde açılan "Stok Kartı Kayıtları" ekranı ise Child formdur. Stok modülü Task olarak görünür ve geçiş yapılabilir ancak Stok Kartı Kayıtları, stok modülünden ayrı bir Task olarak görünmez. İlgili dizayn için yukarıdaki bilgiler belirlendikten sonra dizayn saklanır. |
| Sıra No | Tanımlanan dizaynın sıra numarasının girildiği alandır. |
| Aktif | Tanımlanan dizaynın aktif olup olmadığının belirlendiği seçenektir. |
| Dizayn Görüntüle | Dizaynın görüntülenmesi için kullanılan butondur. |
| Dizayn Ortamı | Dizaynı seçtikten sonra, dizaynın hazırlanması için kullanılan butondur. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır. Dizayn Hazırlama kaydının iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
