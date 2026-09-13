---
title: "Kural Bilgileri"
page_id: "22806250"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Banka"
  - "Kayıt / Banka"
  - "MT940 Kayıtları"
  - "Kural Bilgileri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Banka / Kayıt / Banka / MT940 Kayıtları / Kural Bilgileri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTY2MTk1OWRlLTNjYmYtNDdhZS1iYWU0LWRmZTc1ZDYxMDhmNyZsaW5rPThhZWQ2YTg2LWU3N2EtNGNmNy04YjliLTk5OGQ2MDllNGY5OCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=661959de-3cbf-47ae-bae4-dfe75d6108f7&link=8aed6a86-e77a-4cf7-8b9b-998d609e4f98&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "kural-bilgileri_34221563_22806250.html"
source_version: "2022-12-02T12:10:21.023+03:00"
source_bytes: 15027
fetched_at: "2026-09-13T04:10:04+00:00"
generator: "netsis-scraper 1.0.0"
---
# Kural Bilgileri

Kural Bilgileri, Finans Bölümü'nde, "Kayıt/Banka" menüsünün altında yer alır. Banka hesap hareketlerinin entegrasyon sürecinde, Logo Netsis ERP sisteminden çeşitli belgeler oluşturulur. Kural Bilgileri, MT940 satırlarında yer alan bilgi kalıpları doğrultusunda, oluşturulacak belgelerin belirlenmesi ve bu belgelerin sistemde ilişkili olduğu Cari, Muhasebe, Banka ve Çek bağlantılarının tespitine yönelik tanımlamaların yapıldığı bölümdür.

Kural Bilgileri ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Kural Bilgileri Ekranı |  |
| --- | --- |
| Kural Kodu | Banka hesap hareketlerinin entegrasyon sürecinde belge oluşturulurken kullanılacak kural kodunun tanımlandığı alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, kural kodlarına ulaşılır. |
| Kural Adı | "Kural Kodu" alanında tanımlanan koda ait ismin girildiği alandır. |
| Metin | Bu alanda yer alan bilgi, bankadan (sistem üzerinden) alınan dosyanın hesap hareket satırları içinde metin bazlı aranarak, ilişkili kural tespiti sağlar. Tanımlanacak kural, tanımlanan metnin içinde geçen satırlar için çalışır. |
| Bilgi Amaçlı | Seçeneğin işaretlendiğinde, tanımlaması yapılan kural ile eşleşen kayıt varsa MT940 entegrasyonu sırasında bu kaydın aktarımı yapılmaz. |
| Belge Tipi | İlgili satır için sistemde oluşturulması istenen belgenin seçildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile belge tipleri arasından seçim yapılır. Belge Tipleri; Genel Dekont, Havale/EFT/Bankalar Arası Virman, Çek Tahsil, Çek Ödendi, Senet Tahsil, Senet Ödendi, Bankadan Gelen Karşılıksız Çek, Bankadan Gelen Protestolu Senet, İade Çek, İade Senet. |
| İşlem Tipi | İlgili belgenin ilişkilendirileceği varlık (cari hesap, banka hesabı, muhasebe hesabı, çek ya da senet) ile, bu varlığın sistemdeki kod karşılığının belirlenmesini sağlayan alandır. Alanın sağ tarafında, işaretlenen belgeye ait kod girişi yapılmasını sağlayan alan yer alır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, ilgili belgeye ait kodlar arasından seçim yapılır. |
| Şube Kodu | Tanımlanan kural kodu için şube kodu girilen alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, şube kodları arasından seçim yapılır. Şube Kodu girildiğinde, ilgili kuralın sadece girildiği şube kodunda çalışması sağlanır. Tüm şubelerde çalışması isteniyorsa "-1" değerinin girilmesi gerekir. |
| Para Birimi | Tanımlanan kural kodu için para birimi tanımlanan alandır. Para birimi girildiğinde, ilgili kuralın MT940 dosyasında para biriminin kısıda göre çalışması sağlanır. MT940 dosyasında para biriminin son karakteri USD olduğunda "D" bulunuyor. Kural bilgilerinde de bu tek karakter girildiğinde ilgili kuralın ilgili para birimi ile eşleşmesi sağlanır. |

İlgili alanlara bilgi girişi yapıldıktan sonra "Kaydet" ![](../../../../../_assets/865524a70e225c89c107.jpg) butonuna basılarak kayıt oluşturulur. Kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
