---
title: "Kasa Tanımlama"
page_id: "22806423"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Kasa"
  - "Kayıt / Kasa"
  - "Kasa Tanımlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Kasa / Kayıt / Kasa / Kasa Tanımlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTIxNmNkNGJjLTA0NDEtNDQzOS05YTFhLWIzMjRmZjgxNjNlMCZsaW5rPThiZDdkZDliLTBmMzUtNGZmZC05Y2EyLTA4OGIyMzUzM2E0NSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=216cd4bc-0441-4439-9a1a-b324ff8163e0&link=8bd7dd9b-0f35-4ffd-9ca2-088b23533a45&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "kasa-tanimlama_24771189_22806423.html"
source_version: "2022-04-05T15:45:36.413+03:00"
source_bytes: 69189
fetched_at: "2026-09-13T04:10:46+00:00"
generator: "netsis-scraper 1.0.0"
---
# Kasa Tanımlama

Kasa Tanımlama, Finans Bölümü'nde, "Kayıt/Kasa" menüsünün altında yer alır. Başlangıçta hiçbir kasa tanımlaması olmayan bu modülün kullanılması için en az bir adet kasanın tanımlanması gerekir.

![](../../../../_assets/b711b987ec96aac9901f.png)

Kasa Tanımlama ekranının alanları ve içerdiği bilgiler aşağıdaki şekildedir:

| Kasa Tanımlama Ekranı |  |
| --- | --- |
| Kasa Kodu | Tanımlaması yapılacak kasanın kodunun girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile kasa kodları arasından seçim yapılabilir. Kasa kodları girilirken işletme/şubeli çalışmalarda aynı kasa kodu farklı işletme/şubelerde tekrar edilemez. |
| Adı | Kasa ad ve açıklamasının tanımlanacağı alandır. En fazla 50 karakter uzunluğunda kod ve açıklama tanımlanabilir. Örneğin; Merkez Kasa, Şube Kasası gibi. |
| Son Devir Tarihi | Tanımlanan kasanın kayıtlarına, başlanması istenen tarihten bir gün önceki tarihin girildiği alandır. Örneğin; Günün tarihi 22.02.2018 ise kasanın devir tarihi 21.02.2018 olmalıdır. |
| Son Devir Tutarı | Başlanması istenen devir tarihindeki bakiye tutarının girildiği alandır. Örneğin; Kasanın devir tarihi 21.02.2018 ise; bu tarihten bir gün sonraya yani 22.02.2018’ e devreden tutarının girilmesi gerekir. Son devir tarihi ve tutarı “Yeni Güne Devir” işlemi yapıldığında otomatik olarak güncellenir. |
| Muhasebe Kodu | Muhasebe ile entegre çalışan firmalar için, Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile muhasebe kodunun seçildiği alandır. Kasa ile ilgili hareketler, tanımlanacak hesap kodunda muhasebeleşir. Muhasebe Kodu alanının kullanılması için, [Yardımcı Programlar](<../../../Genel/Yardımcı Programlar/index.md>) → Kayıt → Şirket/Şube Parametre Tanımları → "Muhasebe Entegre" parametresinin işaretlenmesi gerekir. |
| Basım Türü | Tanımlanan kasa ile ilgili kayıtlar için basım türünün seçildiği alandır. "Basım Yapma", "Standart Basım" ve "Özel Basım" olmak üzere üç tür seçenekten oluşur. |
| Basım Yapma | Kasa ile ilgili basım yapılmasının istenmediği durumlarda işaretlenmesi gereken seçenektir. |
| Standart Basım/Özel Basım | Kasa kaydı basımı için "Standart Basım" veya "Özel Basım" tercihlerinden birinin belirlendiği seçeneklerdir. Standart Basım ile tüm kayıtlar için sabit bir basım yapılırken, Özel Basım seçeneği ile "Dizayn Modülü" kullanılarak istenilen şekilde hazırlanan dizayn kullanılır. |
| Basım | Basımın tek sayfa mı yoksa çift sayfa olarak mı basılacağının belirlendiği alandır. |
| Tek Sayfa/Çift Sayfa | Kasanın günlük defter basımlarının yazıcı dökümünde tek sayfa mı yoksa çift sayfa olarak mı basılacağının belirlendiği alandır. Bu alan boş bırakılamaz. Kayıtların tek sayfaya gelir/gider şeklinde birlikte yazılması istendiğinde “Tek Sayfa”, önce gelir sonra gider sayfasının ayrı ayrı dökümünün alınması istendiğinde ise “Çift Sayfa” seçeneği işaretlenir. |
| Döviz Takip | Dövizli kasa takibinin yapılması istendiğinde işaretlenmesi gereken seçenektir. |
| Döviz Tipi | "Döviz Takip" seçeneği işaretlendiğinde aktif hale gelen alandır. Kasanın hangi döviz tipi ile çalışacağı bu alan tarafından belirlenir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile döviz tipi seçimi yapılabilir. |
| Çevrim Tipi (Alış, Satış, Efektif Alış, Efektif Satış) | Dövizli kasa kayıtları için döviz işlem tipinin tanımlanacağı alandır. Program, kayıt sırasında sorgulanan döviz ekranındaki "İşlem Tipi" alanına, burada girilen bilgiyi aktarır ve üzerinde değişiklik yapılmasına izin verir. |
| Son Döviz Tutarı | Dövizle takip edilecek kasalar için, döviz devir tutarının girildiği alandır. "Son devir tutarı" alanı gibi bu alan da yeni güne devir yapıldıkça güncellenir. |
| Kur Farkı Gelir Kodu | Dövizle takip edilen kasalar için, oluşan kur farkı gelirlerinin aktarılacağı muhasebe kodunun girildiği alandır. rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile muhasebe kodları arasından seçim yapılabilir. |
| Kur Farkı Gider Kodu | Dövizle takip edilen kasalar için, oluşan kur farkı giderlerinin aktarılacağı muhasebe kodunun girildiği alandır. rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile muhasebe kodları arasından seçim yapılabilir. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır. Yapılan kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
