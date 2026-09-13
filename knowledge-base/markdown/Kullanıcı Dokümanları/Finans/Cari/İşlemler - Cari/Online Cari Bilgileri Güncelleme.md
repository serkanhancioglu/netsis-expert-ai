---
title: "Online Cari Bilgileri Güncelleme"
page_id: "22805252"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Cari"
  - "İşlemler / Cari"
  - "Online Cari Bilgileri Güncelleme"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Cari / İşlemler / Cari / Online Cari Bilgileri Güncelleme"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTI3NTZlMTM4LTE5MjYtNDMwNi1iZDBlLTQzYzU2ZTZkOGQwZCZsaW5rPTYzM2VjMzcyLTU4NGMtNGMzNy05NjdlLTYyZDQyMGYxMmZhMCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=2756e138-1926-4306-bd0e-43c56e6d8d0d&link=633ec372-584c-4c37-967e-62d420f12fa0&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "online-cari-bilgileri-guncelleme_29985800_22805252.html"
source_version: "2022-11-17T13:35:01.293+03:00"
source_bytes: 13653
fetched_at: "2026-09-13T04:08:08+00:00"
generator: "netsis-scraper 1.0.0"
---
# Online Cari Bilgileri Güncelleme

Online Cari Bilgileri Güncelleme işlemi, Finans Bölümü'nde İşlemler/Cari menüsünün altında yer alır. Cari → Kayıt → Cari Hesap Kayıtları bölümünden kaydedilen cari hesaplara ait bilgilerin, programdan çalışılan bankaya online olarak gönderildiği bölümdür. Bankaya gönderilecek cari hesapların bilgileri, istenen kısıtlar verilerek seçilir ve Tamam butonuna basılarak bilgiler bankaya aktarılır. Aktarım sırasında dosyanın fazla büyük olması sistemde yavaşlığa neden olacağı için, cari hesap bilgilerinin parçalı olarak gönderimi önerilir.

Online Cari Bilgileri Güncelleme ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Online Cari Bilgileri Güncelleme Ekranı |  |
| --- | --- |
| Tip | Online cari bilgileri güncellemek için tip kısıdının verildiği alandır. Alıcı, Satıcı, Diğer ve Hepsi olmak üzere dört seçenekten oluşur. Alanın sağ tarafında yer alan aşağı ok butonu ile tipler arasından seçim yapılır. |
| Hesap Tipi | Online cari bilgileri güncellemek için hesap tipi kısıdının verildiği alandır. Yaşlandırma, Özel Hesap Kapatma ve Hepsi olmak üzere üç seçenekten oluşur. Alanın sağ tarafında yer alan aşağı ok butonu ile hesap tipleri arasından seçim yapılır. |
| Grup Kodu | Online cari bilgileri güncellemek için grup kodu kısıdının verildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile grup kodları arasından seçim yapılabilir. |
| Cari Kodu | Online cari bilgileri güncelleme işleminin belli aralıktaki cari kodlar için yapılması istendiğinde kısıt verilen alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, cari kodlar arasından seçim yapılır. |
| Tüm Cariler Aktarılsın | Seçeneğin işaretlenmesi ile birlikte daha önceden aktarılan cari hesapların bankadaki bilgileri tekrar güncellenir. Daha önceden bilgileri aktarılmış cari hesapların TBLCASABIT tablosunda UPDATE_KOD sahasına X kodu verilir. Bu parametre işaretlendiğinde, tablonun update_kod sahasında X bulunup bulunmamasını dikkate almaz ve cari hesabın güncellenmiş bilgileri ile aktarımı yeniden yapar. **Örneğin:** Grup Kodu 01 olan cari hesapların aktarımı daha önce yapılmış olsa dahi, grup kodu alanına 01 kısıtı verilerek "Tüm Cariler Aktarılsın" parametresi işaretlendiğinde, grup kodu 01 olan tüm cari hesaplar yeninden aktarılır. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Online cari bilgileri güncellemek için verilen kısıtların onaylanmasını sağlayan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
