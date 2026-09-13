---
title: "Kredi Kartı Tahsilat Kayıtları"
page_id: "22806231"
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
  - "Kredi Kartı Tanımlamaları"
  - "Kredi Kartı Tahsilat Kayıtları"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Banka / Kayıt / Banka / Kredi Kartı Tanımlamaları / Kredi Kartı Tahsilat Kayıtları"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWZmYTFjNzJkLWY3MGEtNDMzOC05NTI0LTI1ZGVmMzU3OGFlNyZsaW5rPTA1MzA4NTJjLWI2YzYtNGYxYy1hNzBhLWUwOTQwYTg1MWNjMSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=ffa1c72d-f70a-4338-9524-25def3578ae7&link=0530852c-b6c6-4f1c-a70a-e0940a851cc1&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "kredi-karti-tahsilat-kayitlari_34221434_22806231.html"
source_version: "2022-04-04T11:28:43.140+03:00"
source_bytes: 251282
fetched_at: "2026-09-13T04:10:01+00:00"
generator: "netsis-scraper 1.0.0"
---
# Kredi Kartı Tahsilat Kayıtları

Finans Bölümü'nde, "Kayıt/Banka" menüsünün altında yer alır. Kredi Kartı Tahsilat Kayıtları, bankaların yaptığı/yapacağı ödemelerin tespit edilmesi ve "Banka" ile "Entegrasyon" modüllerinde ödeme kayıtlarının oluşmasını sağlayan bölümdür.

![](../../../../../_assets/9860264af9076f752283.png)

Kredi Kartı Tahsilat Kayıtları ekranında yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| Kredi Kartı Tahsilat Kayıtları Ekranı |  |
| --- | --- |
| Vade Başlangıç Tarihi | Çalıştırılacak hazırlık işlemine ait vade aralığının başlangıç tarihinin girildiği alandır. |
| Vade Bitiş Tarihi | Çalıştırılacak hazırlık işlemine ait vade aralığının bitiş tarihinin girildiği alandır. |
| Hareket Tarihi | Tahsilatların, "Banka" ve "Entegrasyon" modüllerinde hangi tarihte oluşacağı ile ilgili tarih girilen alandır. |
| Şube Kodu | Merkez şubeden girildiğinde aktif hale gelen alandır. İşlem yapılacak şubenin seçilmesini sağlar. İşlemin tüm şubeler için çalıştırılması istendiğinde bu alana "-1" değerinin girilmesi gerekir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, şube kodlarına ulaşılır. |
| Banka Hesap Kodu | Çalıştırılması istenen tahsilat işlemine ait hesap kodunun girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, banka hesap kodlarına ulaşılır. |
| Kayıtlar Şube Kırılımlı Oluşturulsun | Birden fazla şube için aynı anda tahsilat kaydı yapıldığında, kayıtların şube bazında oluşturulması için işaretlenmesi gereken seçenektir. Kayıtlar Şube Kırılımlı Oluşturulsun seçeneği sadece merkez şubeden giriş yapıldığında aktif hale gelir. |
| Kayıtlar Proje Kırılımlı Oluşturulsun | Proje uygulamasının açık olduğu durumlarda aktif hale gelen seçenektir. Oluşacak tahsilat kayıtlarının proje bazında kırılımlı olarak oluşmasını sağlar. |
| Kayıtlar Plasiyer Kırılımlı Oluşturulsun | Plasiyer uygulamasının açık olduğu durumlarda aktif hale gelen seçenektir. Oluşacak tahsilat kayıtlarının plasiyer bazında kırılımlı olarak oluşmasını sağlar. |
| Tutar | Hazırlık işleminden sonra, grid ekranda listelen kayıtlar arasından seçilen kaydın tutarını gösteren alandır. |
| Kayıt Onay | Hazırlık işleminden sonra, grid ekranda listelen kayıtlar arasından seçilen kayda ait tutarın onaylanması ile ilgili sorgulama yapılmasını sağlayan seçenektir. Rakam değiştirilerek onaylı hale getirilebilir. |
| Açıklama | Kredi kartı tahsilat kaydı için açıklama bilgisi girilen alandır. |
| Detay Kısıt | Ekrandaki kısıtlar dışında başka kısıtların da girilmesini sağlayan butondur. Detay kısıt butonuna basıldığında "İleri Kısıt Tanımlama" ekranı görüntülenir. ![](../../../../../_assets/62fcd2247ac58f7464da.png) **Örneğin:** Birden fazla banka hesap kodu için aralık verilerek tahsilat kaydı oluşturulması istendiğinde, aşağıdaki şekilde bir kısıt tanımlaması yapılabilir. ![](../../../../../_assets/0d77ada6e8bd23958162.png) "İleri Kısıt Tanımlama" ekranında, ilgili alan üzerinde iken klavyedeki boşluk çubuğuna basılarak bilgi girişi yapılır. Örneğin; Banka Hesap No için kısıt verilmesi isteniyorsa, Saha Adı alanında **boşluk tuşuna** basılması ve **aşağı ok** tuşuna basılarak "BANKAHESNO" alanının seçilmesi gerekir. Daha sonra **Enter tuşuna** basıldığında girilen bilgi saklanır ve sağdaki alana geçilir. Birden fazla alana kısıt verilmesi isteniyorsa, klavyede bulunan **Insert** **tuşuna** basılarak satır eklenebilir veya **Delete tuşuna** basılarak eklenen satırlar silinebilir. Sağ klik tuşu ile açılan özel tuşlar sayesinde de aynı işlemler yapılabilir. |
| Hazırlık | Kayıt yapılmadan önce girilen kısıtlar doğrultusunda hazırlık işleminin çalıştırılmasını sağlayan butondur. Butona basıldığında ekranda görüntülenen uyarı mesajına "Evet" butonu ile cevap verildiğinde grid ekrana kayıtlar listelenir. Grid ekranda listelenen tüm kayıtlar onaylı olarak ekrana gelir. Gerekli görüldüğünde onay kaldırılarak, oluştur işlemi sırasında banka ve entegrasyona kayıt atılmaması sağlanır. Listelenen rakamlar üzerinde değişiklik yapılabilir. ![](../../../../../_assets/941d4028f6a7e75a061c.png) |
| Oluştur | Hazırlık sonucu listelenen kayıtların "Banka" ve "Entegrasyon" bölümüne işlenmesi için kullanılan butondur. |
| Tümünü Onayla | Tüm kayıtların onaylanması için kullanılan butondur. Butona basıldığında aşağıdaki onay ekranı görüntülenir. ![](../../../../../_assets/78cacbf0c1b66ba49140.png) |
| Tüm Onayı Kaldır | Onaylı olarak grid alanda listelenen tüm kayıtların onayının kaldırılmasını sağlayan butondur. Butona basıldığında aşağıdaki onay ekranı görüntülenir. ![](../../../../../_assets/1fe35bb4d755eb036dae.png) |
