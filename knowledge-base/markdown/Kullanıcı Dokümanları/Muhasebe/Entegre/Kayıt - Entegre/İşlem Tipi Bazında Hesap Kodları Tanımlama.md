---
title: "İşlem Tipi Bazında Hesap Kodları Tanımlama"
page_id: "24741010"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Muhasebe"
  - "Entegre"
  - "Kayıt / Entegre"
  - "İşlem Tipi Bazında Hesap Kodları Tanımlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Entegre / Kayıt / Entegre / İşlem Tipi Bazında Hesap Kodları Tanımlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWMzZjU1ODAxLThhYmMtNDM3Ni05NTU3LWY4YjEzM2Q0NmMzOCZsaW5rPWU0NTJmNzU5LTM5NzUtNDhkYS05NzIzLTUxOTQ2ZWY2MDAxZSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=c3f55801-8abc-4376-9557-f8b133d46c38&link=e452f759-3975-48da-9723-51946ef6001e&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "islem-tipi-bazinda-hesap-kodlari-tanimlama_41164169_24741010.html"
source_version: "2022-09-22T11:08:32.977+03:00"
source_bytes: 56555
fetched_at: "2026-09-13T04:14:46+00:00"
generator: "netsis-scraper 1.0.0"
---
# İşlem Tipi Bazında Hesap Kodları Tanımlama

İşlem Tipi Bazında Hesap Kodları Tanımlama, Muhasebe Bölümü'nde, "Kayıt/Entegre" menüsünün altında yer alır. İşlem Tipi Bazında Hesap Kodları Tanımlama bölümü ile entegrasyona aktarılan kayıtlarda kullanılacak hesap kodlarının, işlem sırasında seçilen işlem tipi bazında belirlenmesi sağlanır. Bunun için öncelikle, Entegrasyon Kodları → Genel sekmesinde yer alan “İşlem Tipi Bazında Hesap Kodu Değişimi” parametresinin işaretlenmesi gerekir. Daha sonra “İşlem Tipi Bazında Hesap Kodları Tanımlama” bölümünden belgenin kaydı sırasında çalışan muhasebe hesap kodlarının hangi hesap kodu ile değiştirileceği belirlenerek, belge kaydı sırasında işlem tipi seçilir ve istenen hesapların çalışması sağlanır.

![](../../../../_assets/278ca984ca4ea0abc6d7.png)

İşlem Tipi Bazında Hesap Kodları Tanımlama ekranında yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| İşlem Tipi Bazında Hesap Kodları Tanımlama Ekranı |  |
| --- | --- |
| İşletmelerde Ortak | Yapılacak tanımlamaların geçerli olacağı işletme kodunun girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, işletme kodları arasından seçim yapılır. |
| Şubelerde Ortak | Yapılacak tanımlamaların geçerli olacağı şube kodunun girildiği alandır. Tanımlamaların tüm şubelerde geçerli olması için "-1" değerinin girilmesi gerekir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, şubeler arasından seçim yapılır. |
| İşlem Tipi | Hesap kodu değiştirilecek işlem tipinin tanımlandığı alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, işlem tipleri arasından seçim yapılır. |
| Kaynak Hesap Kodu | İlgili işlem sonucu değiştirilmesi istenen hesap kodunun girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılır. |
| Hedef Hesap Kodu | "Kaynak Hesap Kodu" alanında yapılan tanıma uyan hesapların hedef hesap kodunun girildiği aladır. **Örneğin,** Satış faturası kaydı sırasında çalışan 120-01 grup kodlu tüm cari hesapların, 120-02 grup kodu ile değiştirilmesi isteniyorsa, ilgili işlem tipi için "Kaynak Hesap Kodu" alanına 120-01-???, "Hedef Hesap Kodu" alanına da 120-02-??? girilmesi gerekir. Bu durumda, satış faturasının kesildiği cari hesaba ait muhasebe kodu 120-01-001 ise, bu hesap "Kaynak Hesap Kodu" alanında verilen maskelemeye uyduğu için, "Hedef Hesap Kodu" alanındaki tanımlamaya göre değiştirilir. "Hedef Hesap Kodu" alanında, Grup Kodu (120-02) için maskeleme yapılmadığı için bu kodlar doğrudan alınır. Maskeleme yapılan muavin kısmı ise cari hesaba ait muhasebe kodundan alınır. Böylece, çalışacak olan hesap 120-02-001 olur. Bu uygulama "Demirbaş Paketinden" aktarılan kayıtlar için de kullanılabilir. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır.

İşlem Tipi Bazında Hesap Kodları Tanımlama kaydının iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
