---
title: "Muhasebe Detay Kod Girişi"
page_id: "22803700"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Stok"
  - "Kayıt / Stok"
  - "Muhasebe Detay Kod Girişi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Stok / Kayıt / Stok / Muhasebe Detay Kod Girişi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTA4YTIzZjU1LTk3ZTMtNDk2My05YzNlLWMwZjI1ODFhY2UyNyZsaW5rPTQ0YWFiM2E4LTFjMjUtNDk2Yy1iYWIwLWY2Zjk5OTQzYTQ2NCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=08a23f55-97e3-4963-9c3e-c0f2581ace27&link=44aab3a8-1c25-496c-bab0-f6f99943a464&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "muhasebe-detay-kod-girisi_29994152_22803700.html"
source_version: "2022-10-25T20:09:43.367+03:00"
source_bytes: 19841
fetched_at: "2026-09-13T04:04:09+00:00"
generator: "netsis-scraper 1.0.0"
---
# Muhasebe Detay Kod Girişi

Muhasebe Detay Kod Girişi, Lojistik - Satış Bölümü'nde, "Kayıt/Stok " menüsünün altında yer alır. Programın muhasebe ile entegre kullanımında (günlük kayıtların "Entegrasyon Modülünde" bulunan aktarım işlemleri ile muhasebe fişleri haline dönüştürülmesi) gereken koşullardan biri, stok kayıtlarının muhasebe ile koordinasyonunun hangi şekilde yapılacağının belirlenmesidir.

Entegre modüllerden girilen kayıtlar sonucu, muhasebe fişlerinin program tarafından oluşturulması ile ilgili detaylı bilgi için; Muhasebe → Entegre → İşlemler → [Seçenekli Aktarma](<../../../Muhasebe/Entegre/İşlemler - Entegre/Seçenekli Aktarma.md>) dokümanına bakılabilir.

Stok modülünden elle (manuel) yapılan kayıtlar muhasebeye entegre olarak işlenmez. Burada entegrasyonun kurulmasındaki amaç, programın diğer entegre bölümlerinden (Fatura, Müstahsil, İhracat vb.) oluşturulacak stokları ilgilendiren kayıtların stoklarla ilgili bölümlerinin muhasebeye doğru olarak aktarılmasını sağlamaktır.

Stok kalemlerinin muhasebeleştirilmesi sırasında, bütün stokların aynı alış/satış hesap kodlarında muhasebeleştirilmesi istendiğinde gerekli tanımlamalar entegrasyon modülünden yapılır. Stok kalemlerini muhasebede tek tek veya gruplar halinde detaylandırıp, ayrı alış/satış hesapları altında muhasebeleştirilmesi halinde ise, "Muhasebe Detay Kod Girişi" bölümünden gerekli tanımlamaların yapılması gerekir.

Muhasebe Detay Kod Girişi bölümünde 0 (sıfır) dan başlayarak 32.767 adet sayısal detay kodu oluşturulabilir. Burada detay kodlarının altında alış ve satışlara ilişkin bir takım muhasebe hesap kodları kaydedilir. Bu bilgilerin girişinden sonra herhangi bir malın veya bir grup malın "Stok Sabit Kayıtları" bölümündeki "Muhasebe Detay" alanına, burada tanımlanan muhasebe detay kodu yazıldığında, mal/malların alış ve satış muhasebe kodları tanımlanmış hale gelir. Böylece, muhasebe ile entegre olarak gerçekleştirilen stok giriş ve çıkış hareketlerinde (örneğin; alış/satış faturası gibi), hareket gören stokun kartında bulunan muhasebe detay kodunda tanımlı muhasebe kodları çalışır.

Muhasebe Detay Kod Girişi ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Muhasebe Detay Kod Girişi Ekranı |  |
| --- | --- |
| Detay Kodu | Muhasebe detay kod girilen alandır. Rehber butonu![](../../../../_assets/088477bb321d1b20c939.jpg) ile, detay kodları arasından seçim yapılır. |
| Alış Hesabı | Muhasebe detay kod girişi için alış hesabının girildiği alandır. Rehber butonu![](../../../../_assets/088477bb321d1b20c939.jpg) ile, muhasebe kodları arasından seçim yapılır. |
| Alıştan İade Hesabı | Muhasebe detay kod girişi için alıştan iade hesabının girildiği alandır. Rehber butonu![](../../../../_assets/088477bb321d1b20c939.jpg) ile, muhasebe kodları arasından seçim yapılır. |
| Satış Hesabı | Muhasebe detay kod girişi için satış hesabının girildiği alandır. Rehber butonu![](../../../../_assets/088477bb321d1b20c939.jpg) ile, muhasebe kodları arasından seçim yapılır. |
| Satıştan İade Hesabı | Muhasebe detay kod girişi için satıştan iade hesabının girildiği alandır. Rehber butonu![](../../../../_assets/088477bb321d1b20c939.jpg) ile, muhasebe kodları arasından seçim yapılır. |
| Satış Diğer 1/2/3/4/5/6/7/8 | Muhasebe detay kod girişi için satış diğer hesabının girildiği alanlardır. Rehber butonu![](../../../../_assets/088477bb321d1b20c939.jpg) ile, muhasebe kodları arasından seçim yapılır. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır. Kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
