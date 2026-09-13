---
title: "Esnek Kodu Üretim Parametreleri"
page_id: "29993555"
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
  - "Esnek Kodu Üretim Parametreleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Stok / Kayıt / Stok / Esnek Yapılandırma / Esnek Kodu Üretim Parametreleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWVlZDAwYmJlLWE1ZTktNDBlMy05MTRmLTZhZDk3MWI4YmVhZiZsaW5rPTg2M2ExODVkLTQwMDYtNGVmMS05MDdmLTY5YzA1NTQwOTBiNSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=eed00bbe-a5e9-40e3-914f-6ad971b8beaf&link=863a185d-4006-4ef1-907f-69c0554090b5&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "esnek-kodu-uretim-parametreleri_29993565_29993555.html"
source_version: "2022-10-25T15:25:52.410+03:00"
source_bytes: 19334
fetched_at: "2026-09-13T04:03:59+00:00"
generator: "netsis-scraper 1.0.0"
---
# Esnek Kodu Üretim Parametreleri

Esnek Kodu Üretim Parametreleri, Lojistik - Satış Bölümü'nde, "Kayıt/Stok" menüsünün altında yer alır. Esnek Kodu Üretim Parametreleri; Ürün Profil, Yapılandırma Kodu Tanımlama ve matris ekranda program tarafından yaratılan yapılandırma kodlarının, belli bir formül ve düzen içinde yaratılması için kullanılan bölümdür. Esnek Kodu Üretim Parametreleri; Esnek Yapılandırma Kod Parametreleri ve Geçerli Stoklar olmak üzere iki sekmeden oluşur.

**Esnek Yapılandırma Kod Parametreleri**

Esnek Kodu Üretim Parametreleri ekranı Esnek Yapılandırma Kod Parametreleri sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Esnek Kodu Üretim Parametreleri Ekranı |  |
| --- | --- |
| Otomatik Üretim Kodu | Yapılan tanımlama için kod bilgisi girilen alandır. Yapılandırılan çeşitli stok grupları için farklı formüllerle birden fazla yapılandırma kodu üretme tanımı yapılabilir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, otomatik üretim kodlarına ulaşılır. |
| Sabit/Değişken | Oluşturulacak yapılandırma kodu başlangıç karakterinin, girilen sabit değerle başlaması istendiğinde "Sabit" seçeneğinin işaretlenmesi gerekir. Otomatik yapılandırma kodu başlangıcına, SQL cümlesinden dönen sonucun, karakter olarak aktarılması istendiğinde ise "Değişken" seçeneğinin işaretlenmesi gerekir. |
| Başlangıç Numarası | Otomatik yapılandırma kodunun, başlangıç karakterinden sonraki bölümde yer alacak sıra numarasının başlangıç değerini ifade eden alandır. |
| Uzunluk | Otomatik Yapılandırma kodunun kaç karakterden oluşacağının belirlendiği alandır. |
| Aktif | Otomatik üretim kodunun geçerli olup olmadığını ifade eden alandır. Program tarafından kod üretilirken, tanımlanan kod parametresinin dikkate alınmaması istendiğinde aktif seçeneğinin işaretlenmemesi gerekir. |
| Başlangıç Karakteri | "Sabit" seçeneği işaretlendiğinde yapılandırma kodları, belirtilen sabit değer ile başlar." Değişken" seçeneği işaretlendiğinde ise başlangıç karakteri ekranına, bir SQL cümlesi yazılarak değişken bir şekilde başlangıç karakteri oluşturulması sağlanır. "Başlangıç Karakteri" alanında iken, farenin sağ tuşu ile ekrana gelen "Stok Kodu Değişkeni" seçeneğine tıklanarak imlecin bulunduğu yere "($StokKodu)" ifadesi eklendiğinde ve bu şekilde başlangıç karakteri verildiğinde, seri numarası üretileceği sırada içinde bulunulan stok kodu bilgisinin, üretilecek seri numarasının başlangıç karakteri olarak yazılır. |
| İşletmelerde Ortak | Tanımlanan yapılandırma kodu parametrelerinin geçerli olacağı işletmenin seçildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, işletme kodları arasından seçim yapılır. |
| Şubelerde Ortak | Tanımlanan yapılandırma kodu parametrelerinin geçerli olacağı şubenin seçildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, şube kodları arasından seçim yapılır. |
| Hariç Tutulacak Şube Tanımlamaları | Tanımlanan yapılandırma kodu parametrelerinin birden fazla şubede geçerli, fakat tüm şubelerde geçerli olmaması istendiğinde kullanılır. Bu seçenek üzerinde fare ile bir kez tıklandığında, tanımlamaların geçerli olmayacağı şubelerin seçileceği ekran görüntülenir. |
| ![](../../../../../_assets/c07a85a800d667cfabc8.png) Test | Girilen formüle uygun olarak oluşan ilk yapılandırma kodunun görüntülenmesi için kullanılan butondur. Yukarıdaki ekranda verilen örnek test edildiğinde, yapılandırma kodu aşağıdaki şekilde görüntülenir. ![](../../../../../_assets/11fc09eccb03fdfa97ba.png) |

**Geçerli Stoklar**

Program tarafından üretilecek yapılandırma kodlarına ait tanımlanan formülün, hangi stoklar için geçerli olacağı "Geçerli Stoklar" sekmesinde belirlenir.

Esnek Kodu Üretim Parametreleri ekranı Geçerli Stoklar sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Esnek Kodu Üretim Parametreleri |  |
| --- | --- |
| Giriş Yöntemi | Giriş yöntemi olarak "Kısıt Girişi" kullanıldığında, kısıt verilen stoklarda ilgili otomatik üretim kodu çalışır. "Çoklu Stok Seçimi" seçildiğinde ise ekrana grid gelir ve "Kayıtları Getir" butonuna tıklandığında gride esnek yapılandırmalı stoklar getirilir. Bu stoklar seçildikten sonra "Kaydet" butonuna tıklandığında, seçili stoklar için ilgili otomatik üretim kodunun çalışması sağlanır. İleri kısıt ile de, "Kayıt Getir" ile gride getirilecek stoklar filtrelenebilir. |

Otomatik yapılandırma kodu oluşturulacağı zaman, ilgili stok için mevcut otomatik kod üretim tanımlarına bakılır. Birden fazla aktif kod üretme tanımı olması halinde, ilk bulunan tanıma göre kod üretilir.

"Yapılandırma Başlangıç Numaraları" bölümünün kullanımı ile ilgili detaylı bilgi için; Stok → Ekler → [Ek-3 (Esnek Yapılandırma Uygulaması)](<../../Ekler (Stok)/Ek-3 (Esnek Yapılandırma Uygulaması).md>) dokümanına bakılabilir.
