---
title: "Ambar Fişi Muhasebeleştirme"
page_id: "24764044"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Fatura"
  - "İşlemler / Fatura"
  - "Ambar Fişi Muhasebeleştirme"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Fatura / İşlemler / Fatura / Ambar Fişi Muhasebeleştirme"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTFiYmYxYTNkLTBhMTktNGQyZi1hZGU1LTAyNTQ3MmQ3OTY2OCZsaW5rPTgxYjkxOTBiLWU5YWMtNDNjZC1iMjc3LTg1MGI0NDZlZjE2YiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=1bbf1a3d-0a19-4d2f-ade5-025472d79668&link=81b9190b-e9ac-43cd-b277-850b446ef16b&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ambar-fisi-muhasebelestirme_24764062_24764044.html"
source_version: "2022-10-24T21:24:25.943+03:00"
source_bytes: 15770
fetched_at: "2026-09-13T04:02:47+00:00"
generator: "netsis-scraper 1.0.0"
---
# Ambar Fişi Muhasebeleştirme

Ambar Fişi Muhasebeleştirme, Lojistik - Satış Bölümü'nde, "İşlemler/Fatura" menüsünün altında yer alır.

Ambar Fişi Muhasebeleştirme bölümü, özellikle "Maliyet Muhasebesi" kullanan firmaların, ay içinde yapmış oldukları ambar giriş/çıkış fişlerinin, ay sonunda aylık ağırlıklı ortalama metoduyla muhasebeye aktarılması için kullanılır. Bu firmalar ay içinde ambar giriş/çıkış fişlerini kullanarak, sarflarını stok hareket kayıtlarına aktarır. Bu bilgilerin daha sonra muhasebeye de aktarılması gerekir. Sarf bilgileri, sorgulanan ay kodu, yıl ve gün baz alınarak stok hareket kayıtlarındaki masraf kodlarına göre, aylık ağırlıklı ortalama ile entegrasyona aktarılır. Ambar fişi muhasebeleştirmede kullanılacak muhasebe kodları olarak, stok detay kodları girişindeki alış hesabı, satış hesabı, satış diğer 1/2/3 hesaplarından biri seçilir.

Ambar çıkış fişleri bu bölümden muhasebeleştirilecekse, Entegrasyon → Entegrasyon Kodları → Depolar Arası Transfer → Entegre parametresi işaretlenmez.

Proje uygulamasının kullanıldığı durumlarda, önce masraf kodları "Ek Alan" sahasına girilir ve muhasebeleştirme sırasında masraf tanımlama bölümündeki muhasebe kodu kullanılır. Bu uygulamada ise, ek alana girilen proje kodu artık "Proje Kodu alanına girilir. Muhasebeleştirme işlemi, proje ve referans kodu bazında kırılım şeklinde yapılır.

Proje uygulamasının kullanılmadığı ve sadece referans uygulamasının kullanıldığı durumlarda, ambar fişi muhasebeleştirme işlemi, işlemler sırasında girilen referans koduna göre yapılır.

Ambar Fişi Muhasebeleştirme bölümü kullanılmadan önce "Stok" modülünden "Maliyet Oluşturma" bölümünün çalıştırılması gerekir.

Ambar Fişi Muhasebeleştirme ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Ambar Fişi Muhasebeleştirme Ekranı |  |
| --- | --- |
| Ay/Yıl/Gün | Ambar fişi muhasebeleştirmek için ay, yıl ve gün bilgisinin girildiği alandır. |
| Açıklama | Muhasebeleştirilecek ambar fişi için açıklama bilgisinin girildiği alandır. |
| Grup Kodu | Muhasebeleştirilecek ambar fişi için grup kodu aralığının girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, kodlar arasından seçim yapılır. |
| Fiş No Aralığı | Muhasebeleştirilecek ambar fişi için, fiş numarası aralığının girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, fiş numaraları arasından seçim yapılır. |
| Ambar Fişleri Numaralarına Göre Kırılımlı Olarak Aktarılsın | Ambar fişlerinin numaralarına göre muhasebe kayıtlarına kırılımlı olarak aktarılması için kullanılan seçenektir. |
| Şube Dahil | Şubeli çalışan firmalar için, “şubeler dahil” parametresi işaretlendiğinde, merkezden şubelere ait ambar çıkış fişleri de muhasebeleştirilir. |
| Mamul Parçalama Fişleri Dahil Edilsin | Ambar fişi muhasebeleştirme işlemine mamul parçalama fişlerinin de dahil edilmesi istendiğinde işaretlenmesi gereken seçenektir. |
| Hesap Tipi | Muhasebeleştirilecek ambar fişi için hesap tipi seçilen alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile Alış Hesabı, Satış Hesabı, Satış Diğer 1, Satış Diğer 2 ve Satış Diğer 3 seçeneklerinden oluşur. |
| Hammadde-Ambalaj-Ticari Mal Mamul-Yarı Mamul-Yan Ürün Hepsi | Muhasebeleştirilecek ambar fişi için kısıt verilen alandır. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilgilerin onaylanmasını sağlayan butondur. Ambar Fişi Muhasebeleştirme işlemi sonucunda "Muhasebe Fiş Listesi" raporu açılarak, oluşan fiş gösterilir. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
