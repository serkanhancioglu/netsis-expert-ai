---
title: "Detay Rapor Şablon Tanımlama"
page_id: "24740445"
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
  - "Detay Rapor Şablon Tanımlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / Kayıt / Muhasebe / Proje Kodu Girişi / Detay Rapor Şablon Tanımlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTIxNWQwODg0LWZjZWEtNGMwNi05ZDM4LWE5ZWQyNzYxYTcwZCZsaW5rPTU4ZTU2NWYyLTk0YTUtNGUyNS05M2RmLTNjMGIxZGM1MTQ3NSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=215d0884-fcea-4c06-9d38-a9ed2761a70d&link=58e565f2-94a5-4e25-93df-3c0b1dc51475&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "detay-rapor-sablon-tanimlama_34232328_24740445.html"
source_version: "2022-09-27T14:11:27.500+03:00"
source_bytes: 300087
fetched_at: "2026-09-13T04:12:54+00:00"
generator: "netsis-scraper 1.0.0"
---
# Detay Rapor Şablon Tanımlama

Detay Rapor Şablon Tanımlama, Muhasebe Bölümü'nde, "Kayıt/Muhasebe Modülü" menüsünün altında yer alır. "Proje Takibi Uygulaması" ile program bazında proje kodu sorgulanır. Her modülde, yapılan kayda ait ilgili proje kodu girilir. Böylece, "Proje Detay Raporu" ile farklı modüllerden yapılan kayıtlar proje kodu bazında toplu olarak tek bir rapordan alınabilir.

**Örneğin,** "Proje Detay Raporu" ile proje kodu bazında fatura ve çek-senetlere ait rapor bir arada alınabilir.

Muhasebe → Raporlar → Proje Takip Raporları → [Proje Detay Rapor](<../../Raporlar - Muhasebe/Proje Takip Raporları/Proje Detay Rapor.md>) alınması için, ilk olarak "[Detay Rapor Şablon Tanımlama](<Detay Rapor Şablon Tanımlama.md>)" bölümünden hangi alanlara ve kısıtlamalara göre rapor alınacağı tanımlanır. Bu bölümde şablon tanımlandıktan sonra, "Proje Detay Rapor" bölümünden ilgili şablon sorgulanır ve hazırlanan şablona göre rapor listelenir.

Detay Rapor Şablon Tanımlama ekranı; Rapor Bilgileri, Rapor Grup Tanımlamalar ve Rapor Kolonları sekmelerinden oluşur.

**Rapor Bilgileri**

![](../../../../../_assets/74af7cc797ebf59a48e2.png)

Detay Rapor Şablon Hazırlama ekranı Rapor Bilgileri sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Detay Rapor Şablon Hazırlama Ekranı |  |
| --- | --- |
| Rapor Kodu | Hazırlanacak şablon için kod bilgisi girilen alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile rapor kodlarına ulaşılır. Girilen kod, "Proje Detay Rapor" bölümünde sorgulanır. |
| Rapor Açıklaması | Hazırlanacak şablon için açıklama bilgisi girilen alandır. Girilen açıklama, "Proje Detay Rapor" bölümünde başlık olarak izlenebilir. |
| Detaylar Kümüle Edilsin | Raporda listelenecek kolonların proje kodu bazında kümüle edilmesi istendiğinde işaretlenmesi gereken seçenektir. |
| Çoklu Yıl Desteği | Raporu alınacak proje, eskiden beri devam eden bir proje ise (ilgili projeye ait geçmiş yıl veri tabanında kayıt varsa) bu bilgilerin de raporlanması için işaretlenmesi gereken seçenektir. İşaretlenmediğinde, projeye ait kayıtlar, sadece içinde bulunulan şirketten getirilir. Projenin eski yıllara ait bilgilerinin bulunduğu veri tabanları, Muhasebe → Kayıt → [Proje Kodu Girişi](index.md) → Proje Sabit Tanımları → Veri Tabanı Bilgileri sekmesinden tanımlanır. |
| Proje Kısıtı Ekle | Alanın sağ tarafında yer alan üç nokta ![](../../../../../_assets/5098b020c5e814c92501.png) butonu ile, "Kısıt Girişi" ekranı görüntülenir. Rapor alınması istenen proje koduna ait kısıt verilerek istenen alana göre sıralama yapılmasını sağlar. ![](../../../../../_assets/2158eb86709c35ee6bc9.png) |
| İşletmelerde Ortak | Tanımlanacak rapor şablonunun hangi işletmede geçerli olacağının belirlendiği alandır. Rapor şablonunun tüm işletmelerde görülmesi istendiğinde -1 değerinin girilmesi gerekir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile işletme kodlarına ulaşılır. |
| Şubelerde Ortak | Tanımlanacak rapor şablonunun hangi şubelerde geçerli olacağının belirlendiği alandır. Rapor şablonunun tüm şubelerde görülmesi istendiğinde -1 değerinin girilmesi gerekir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile şube kodlarına ulaşılır. |
| Hariç Tutulacak Şube Tanımlamaları | "Şubelerde Ortak" alanına -1 değeri girildiği zaman aktif hale gelen alanda, şablonun görülmesinin istenmediği şubeler belirtilerek, bu şubeler hariç tutulabilir. |

**Rapor Grup Tanımlamalar**

Proje detay raporu hazırlanırken farklı view’lerden bilgi alınabilir. Farklı view’lerden rapor alırken her bir view değişiminde konuya göre gruplama yapılarak farklı başlık tanımlanabilir. "Rapor Grup Tanımlamalar" sekmesi, gruplara ait başlıkların tanımlamasını sağlar.

![](../../../../../_assets/fece39ddf565df9765b3.png)

Detay Rapor Şablon Hazırlama ekranı Rapor Grup Tanımlamalar sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Detay Rapor Şablon Hazırlama Ekranı |  |
| --- | --- |
| Grup Açıklaması | Raporda gruplama yapılacak alan için, gruba ait üst ana başlık açıklamasının girildiği alandır. Alan üzerine fare ile çift tıklanarak veya klavyede yer alan \<tab\> tuşu ile ilerlenerek bilgi girişi yapılır. |
| Açıklama | "Grup Açıklaması" alanından sonra gruplama yapılacak alan için gruba ait alt başlığın girildiği alandır. Alan üzerine fare ile çift tıklanarak veya klavyede yer alan \<tab\> tuşu ile ilerlenerek bilgi girişi yapılır. **Örneğin,** "Grup Açıklaması" alanına "Proje Siparişleri" başlığı tanımlandığında, "Açıklama" alanına "Verilen Siparişler" ve "Alınan Siparişler" başlığı verilebilir. Bu durumda, önce raporda "Proje Siparişleri" şeklinde bir ana başlık ve bu başlıktan sonra "Alınan Siparişler" şeklinde bir alt başlık izlenir. |
| Görüntü Adı | Raporun hangi view’den alınacağının seçildiği (rapora bilgilerin nereden aktarılacağı) alandır. Alan üzerine fare ile çift tıklanarak veya klavyede yer alan \<tab\> tuşu ile ilerlenerek seçim yapılır. **Örneğin,** Sipariş Hareketleri, Stok Sabit Kayıtları gibi. |
| Kısıtlama | Alan üzerine fare ile çift tıklandığında, "Görüntü Adı" alanında seçilen view ile ilgili kısıtın verileceği ekran açılır ve bu ekrandan ilgili view ile alakalı kısıt verilmesi sağlanır. **Örneğin,** "View Adı" kısmında “Stok Hareketleri” seçilmişse, stok hareket türü giriş olanlar raporda listelensin şeklinde kısıt verilebilir. |
| Satır Ekle | "Rapor Grup Tanımlamalar" sekmesine yeni satır eklenmesini sağlayan alandır. |
| Satır Sil | "Rapor Grup Tanımlamalar" sekmesine eklenen satırın iptal edilmesini sağlayan alandır. |

**Rapor Kolonları**

Rapor Kolonları, "Rapor Grup Tanımlamalar" sekmesinde tanımlaması yapılan view’lere ait raporda listelenmesi istenen kolonların belirlenmesini sağlayan sekmedir.

![](../../../../../_assets/c79dfd203c446987b730.png)

Detay Rapor Şablon Hazırlama ekranı Rapor Kolonları sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Detay Rapor Şablon Hazırlama Ekranı |  |
| --- | --- |
| Grup Detay Seçimi | Hangi view’e ait kolonların listeleneceğinin seçildiği alandır. "Rapor Grup Tanımlamalar" sekmesinde yapılan tanımlamalar, bu alana otomatik olarak aktarılır ve kullanıcı bu alandan kolonlarını tanımlayacağı view’i seçer. Alanın sağ tarafında yer alan aşağı ok butonu ile seçim yapılır. |
| Alan İsim | Grup Detay Seçimi alanında seçilen view’e ait raporda listelenmesi istenen isim bilgisinin belirtildiği alandır. |
| Alan Açıklama | “Alan İsim” alanında tanımlanan view’e ait kolonun raporda listelenmesi istenen açıklama bilgisinin belirtildiği alandır. **Örneğin,** kolonun adı stok_kodu olduğu halde, raporda STOK KODLARI şeklinde (kullanıcının tanımladığı) açıklama ile izlenebilir. |
| Ondalık Tipi | Bu alan, “Alan İsim” alanında sayısal bir kolon seçildiği zaman aktif hale gelir. Seçilen sayısal alanın, raporda listelenirken alması istenen ondalık değerinin belirtildiği alandır. Bu alanda, ilgili şirket için tanımlanan Yardımcı Programlar → Kayıt → "[Netsis Ondalık Sistemi](<../../../../Genel/Yardımcı Programlar/Kayıt - Yardımcı Programlar/Netsis Ondalık Sistemi.md>)" bölümündeki alanlar aktarılır (miktar, fiyat, oran, tutar vb...) ve hangi kolona ait ondalık değer isteniyorsa o alan seçilir. |
| Toplam Al | Bu alan, “Alan İsim” alanında sayısal bir kolon seçildiği zaman aktif hale gelir. Seçilen sayısal alan için toplam alınması istendiğinde işaretlenmesi gerekir. |
| Satır Ekle | Raporda listelenmesi istenilen kolonlara yeni bir kolon ilave edilmesini sağlayan butondur. Butona tıklanması ile yeni bir satır ekrana gelir ve bu yeni satırda yeni kolon tanımlaması yapılır. |
| Satır Sil | Raporu alınacak şablona eklenen kolonun silinmesini sağlayan butondur. Silinmesi istenen satırın üzerine gelerek Satır Sil butonuna tıklanır. |
| Değişiklikleri Sakla | Rapor şablonuna eklenen kolonlarda değişiklik yapıldığı zaman, yapılan son değişikliklerin kaydedilmesi için kullanılan butondur. |
| Alan Bilgilerini Sakla | Raporda hangi kolonların ne şekilde izlenmesi istendiği belirlendikten sonra, kolonlara ait tanımlamaların şablon içinde saklanması için kullanılan butondur. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır. Detay Rapor Şablon Hazırlama kaydının iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
