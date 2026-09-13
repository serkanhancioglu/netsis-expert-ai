---
title: "Otomatik Seri Kodu Üretme Tanımlamaları"
page_id: "22803713"
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
  - "Seri Takibi"
  - "Otomatik Seri Kodu Üretme Tanımlamaları"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Stok / Kayıt / Stok / Seri Takibi / Otomatik Seri Kodu Üretme Tanımlamaları"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTlhNTg4YTI2LTU5MjgtNDI0My05YWI2LTZkNjMyZmE4ZTg1YiZsaW5rPTllMjM0Y2ZiLWVmN2QtNGE3OC04YzJhLTY5ZmEzY2M0ZWVkMSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=9a588a26-5928-4243-9ab6-6d632fa8e85b&link=9e234cfb-ef7d-4a78-8c2a-69fa3cc4eed1&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "otomatik-seri-kodu-uretme-tanimlamalari_22804437_22803713.html"
source_version: "2022-10-25T21:10:30.173+03:00"
source_bytes: 20889
fetched_at: "2026-09-13T04:04:25+00:00"
generator: "netsis-scraper 1.0.0"
---
# Otomatik Seri Kodu Üretme Tanımlamaları

Otomatik Seri Kodu Üretme Tanımlamaları, Lojistik - Satış Bölümü'nde, "Kayıt/Stok " menüsünün altında yer alır. Otomatik Seri Kodu Üretme Tanımlamaları, seri kodlarının program tarafından otomatik olarak üretildiği durumlarda, kodların belli bir formüle göre, düzen içinde yaratılması için kullanılan bölümdür. Otomatik Seri Kodu Üretme Tanımlamaları; Otomatik Seri Kodu Parametreleri ve Geçerli Stoklar olmak üzere iki sekmeden oluşur.

**Otomatik Seri Kodu Parametreleri**

Otomatik Seri Kodu Üretme Tanımlamaları ekranı Otomatik Seri Kodu Parametreleri sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Otomatik Seri Kodu Üretme Tanımlamaları Ekranı |  |
| --- | --- |
| Otomatik Üretim Kodu | Otomatik seri kodu üretilmesi için kod girilen alandır. Farklı stok grupları için, farklı formüllerle birden fazla seri kodu üretme tanımı yapılabilir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, otomatik üretim kodlarına ulaşılır. |
| Sabit/Değişken | Oluşturulacak yapılandırma kodu başlangıç karakterinin, girilen sabit değerle başlaması istendiğinde "Sabit" seçeneğinin işaretlenmesi gerekir. Otomatik yapılandırma kodu başlangıcına, SQL cümlesinden dönen sonucun, karakter olarak aktarılması istendiğinde ise "Değişken" seçeneğinin işaretlenmesi gerekir. |
| Başlangıç Numarası | Otomatik seri kodunun, başlangıç karakterinden sonraki bölümde yer alacak sıra numarasının başlangıç değerini ifade eden alandır. |
| Uzunluk | Otomatik seri kodunun kaç karakterden oluşacağının belirlendiği alandır. |
| Aktif | Otomatik üretim kodunun geçerli olup olmadığını ifade eden alandır. Program tarafından kod üretilirken, tanımlanan kod parametresinin dikkate alınmaması istendiğinde aktif seçeneğinin işaretlenmemesi gerekir. |
| Başlangıç Karakteri | "Sabit" seçeneği işaretlendiğinde seri kodları, belirtilen sabit değer ile başlar." Değişken" seçeneği işaretlendiğinde ise başlangıç karakteri ekranına, bir SQL cümlesi yazılarak değişken bir şekilde başlangıç karakteri oluşturulması sağlanır. "Başlangıç Karakteri" alanında iken, farenin sağ tuşu ile ekrana gelen "Stok Kodu Değişkeni" seçeneğine tıklanarak imlecin bulunduğu yere "($StokKodu)" ifadesi eklendiğinde ve bu şekilde başlangıç karakteri verildiğinde, seri numarası üretileceği sırada içinde bulunulan stok kodu bilgisinin, üretilecek seri numarasının başlangıç karakteri olarak yazılır. |
| İşletmelerde Ortak | Tanımlanan seri kodu parametrelerinin geçerli olacağı işletmenin seçildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, işletme kodları arasından seçim yapılır. |
| Şubelerde Ortak | Tanımlanan seri kodu parametrelerinin geçerli olacağı şubenin seçildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, şube kodları arasından seçim yapılır. |
| Hariç Tutulacak Şube Tanımlamaları | Tanımlanan seri kodu parametrelerinin birden fazla şubede geçerli, fakat tüm şubelerde geçerli olmaması istendiğinde kullanılır. Bu seçenek üzerinde fare ile bir kez tıklandığında, tanımlamaların geçerli olmayacağı şubelerin seçileceği ekran görüntülenir. |
| ```text<br>Test<br>``` | Girilen formüle uygun olarak oluşan ilk yapılandırma kodunun görüntülenmesi için kullanılan butondur. Başlangıç Karakteri T, Otomatik Üretim Kodu K1 olan bir yapılandırma kodu test edildiğinde, bir sonraki yapılandırma kodu aşağıdaki şekilde görüntülenir. ![](../../../../../_assets/5818501f9839fdbff77e.png) |

**Geçerli Stoklar**

Geçerli Stoklar, program tarafından üretilecek seri kodlarına ait tanımlanan formülün, hangi stoklar için geçerli olacağı ile ilgili tanımlamalar yapılan sekmedir.

Otomatik seri kodu oluşturulacağı zaman, ilgili stok için mevcut otomatik kod üretim tanımlarına bakılır. Eğer birden fazla aktif kod üretme tanımı varsa, ilk bulunan tanıma göre kod üretilir.

Otomatik Seri Kodu Üretme Tanımlamalarında yapılan tanımlamanın geçerli olması için; Stok → Kayıt → [Stok Kartı Kayıtları](<../Stok Kartı Kayıtları/index.md>) → Seri Takibi → “Otomatik Hesaplansın” seçeneğinin işaretlenmesi gerekir. İşaretlenmediğinde, seri kodlarının giriş/çıkış kayıtları sırasında kullanıcı tarafından elle (manuel) girilmesi gerekir.

Herhangi bir stok için, Stok → Kayıt → [Stok Kartı Kayıtları](<../Stok Kartı Kayıtları/index.md>) → Seri Takibi → “Otomatik Hesaplansın” seçeneği işaretlense de, "Başlangıç Karakteri” alanına karakter girişi yapılması halinde, öncelikle Otomatik Seri Kodu Üretme Tanımlamalarına bakılır. Burada ilgili stoka uygun herhangi bir tanımlama bulunmaması halinde, stok kartında verilen başlangıç karakteri dikkate alınarak seri kodu üretilir.

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır.

Yapılan kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../../_assets/604869e96ca2f8104a00.png) butonuna tıklanması gerekir.
