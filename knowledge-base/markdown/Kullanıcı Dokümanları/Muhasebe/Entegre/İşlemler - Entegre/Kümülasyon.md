---
title: "Kümülasyon"
page_id: "24741037"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Muhasebe"
  - "Entegre"
  - "İşlemler / Entegre"
  - "Kümülasyon"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Entegre / İşlemler / Entegre / Kümülasyon"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTJmMzdjOWQ0LTBjMmQtNGJlOS05Y2QxLTI0ZWEwYjUwYzg1MCZsaW5rPWMxNGI0ZTkzLTgxZWQtNGE1YS1hODM1LTVkZTkwNWQxYTY1ZCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=2f37c9d4-0c2d-4be9-9cd1-24ea0b50c850&link=c14b4e93-81ed-4a5a-a835-5de905d1a65d&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "kumulasyon_41164320_24741037.html"
source_version: "2022-09-22T13:32:54.987+03:00"
source_bytes: 112358
fetched_at: "2026-09-13T04:14:48+00:00"
generator: "netsis-scraper 1.0.0"
---
# Kümülasyon

Kümülasyon Muhasebe Bölümü'nde, "İşlemler/Entegre" menüsünün altında yer alır. Entegrasyondaki bilgilerden, aynı muhasebe hesap koduna sahip olan kayıt tutarlarının kümüle edilerek muhasebeye aktarılması için kullanılan bölümdür. Kümülasyon işlemi ile, sadece Entegrasyon → Kayıt → [Kümülasyon Muhasebe Kodları](<../Kayıt - Entegre/Kümülasyon Muhasebe Kodları.md>) bölümünde tanımlanan hesapların kümüle edilmesi sağlanır. Kümülasyon ekranı; Tarih Aralık Belirleme ve Ek Sorgu olmak üzere iki sekmeden oluşur.

**Tarih Aralık Belirleme**

Tarih Aralık Belirleme sekmesi, entegrasyonda bulunan yedi adet fiş arasından, aktarılması istenen fiş/fişlerin seçilerek, tarih aralığının belirlenmesini sağlayan sekmedir.

![](../../../../_assets/80e666967b0eb40eb982.png)

Kümülasyon ekranı Tarih Aralık Belirleme sekmesinde yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| Kümülasyon Ekranı |  |
| --- | --- |
| Kümüle | Entegrasyonda fiş isimlerinin yanında bulunan "Kümüle" seçeneğinin işretlenmesi ile, ilgili mahsup fişi içinde kümüle edilecek hesap kodu varsa, kümülasyon işleminin yapılmasını sağlayan seçenektir. |
| Başlangıç/Bitiş Tarihi | "Kümüle" seçeneği işaretlenen mahsup fişlerinde aktif hale gelen alandır. Girilen tarih aralığı ile, hesap kodlarının sadece o tarihler arasında kümüle edilmesi sağlanır. |
| Kayıt Tarihi | Kümülasyon sonucu oluşacak kaydın tarihinin girildiği alandır. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilgilerin onaylanmasını sağlayan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
| ![](../../../../_assets/67af647263b81e237bf2.jpg) Hepsi | Ekranda yer alan seçeneklerin hepsinin işaretlenmesi için kullanılan butondur. |
| ![](../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | "Tarih Aralık Belirleme" sekmesinde verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. "Kümülasyon" için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki kümülasyon işleminde kullanılmak üzere saklanır. |

**Ek Sorgu**

Ek Sorgu, kümülasyon ile ilgili kısıt tanımlamasının yapıldığı sekmedir.

![](../../../../_assets/cb5527da2bbfc48a84e4.png)

Kümülasyon ekranı Ek Sorgu sekmesinde yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| Kümülasyon Ekranı |  |
| --- | --- |
| Başlangıç/Bitiş Hesap Kodu | Kümülasyon yapılarak aktarılacak kayıtların başlangıç ve bitiş hesap kodu aralığının girildiği alandır. "Başlangıç" ve "Bitiş Hesap Kodu" alanlarına aynı hesap kodu girildiğinde, sadece girilen hesabın kümülasyonu yapılır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılır. Girilen hesap kodlarının daha önceden "[Kümülasyon Muhasebe Kodları](<../Kayıt - Entegre/Kümülasyon Muhasebe Kodları.md>)" bölümünden tanımlanması gerekir. |
| Kasa Kodu | Kasa hesaplarının kümülasyonunun yapılması için, ilgili hesabın ait olduğu kasa kodunun girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, kasa kodları arasından seçim yapılır. |
| Tarih Ve Açıklama Kümülasyona İlave Edilsin | "Tarih" ve "Yevmiye Açıklama" alanlarına göre kırılım yapılarak kümülasyon işleminin yapılması için kullanılan seçenektir. Aynı tarih ve aynı açıklama bilgisine ait hesap kodları kendi içinde kümüle edilir. İşlem sonucu, entegrasyon mahsup fişlerinde bulunan kayıtlardan, belirlenen muhasebe hesap koduna sahip olan kayıt tutarları kümüle edilir. Daha sonra bu kayıtlar, "Seçenekli Aktarma" veya "Toplu Aktarma" işlemlerinden biriyle "Muhasebe" modülüne aktarılır. |
| İşlem Tipine Göre Kümüle | Kümülasyon işleminin işlem tipine göre yapılması için kullanılan seçenektir. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilgilerin onaylanmasını sağlayan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
| ![](../../../../_assets/67af647263b81e237bf2.jpg) Hepsi | Ekranda yer alan seçeneklerin hepsinin işaretlenmesi için kullanılan butondur. |
| ![](../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | "Ek Sorgu" sekmesinde verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. "Kümülasyon" için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki kümülasyon işleminde kullanılmak üzere saklanır. |
