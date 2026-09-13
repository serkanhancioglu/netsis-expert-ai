---
title: "Alternatif Reçete Kaydı"
page_id: "50662535"
product: "netsis-3-enterprise"
depth: 4
is_section: true
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Üretim"
  - "Kayıt/Üretim"
  - "Alternatif Reçete Kaydı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Üretim / Kayıt/Üretim / Alternatif Reçete Kaydı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTI2OTIwZmUyLTc1YjAtNDUzOS1iZmZkLWJmNGZmMDg2ZTYyMiZsaW5rPTYyOWZjYTIwLTM0MzQtNGU1Zi1iYzlmLWMxNzJmNjhlMzlkMSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=26920fe2-75b0-4539-bffd-bf4ff086e622&link=629fca20-3434-4e5f-bc9f-c172f68e39d1&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "alternatif-recete-kaydi_50662536_50662535.html"
source_version: "2022-10-13T10:58:12.743+03:00"
source_bytes: 23096
fetched_at: "2026-09-13T04:18:40+00:00"
generator: "netsis-scraper 1.0.0"
---
# Alternatif Reçete Kaydı

Alternatif Reçete Kaydı, Üretim Bölümü'nde Kayıt/Üretim menüsünün altında yer alır. Alternatif Reçete Kaydı, belirli bir mamulün üretimi için var olan mamul reçetesine alternatif yeni bir reçete oluşturmak için kullanılır. Yani, program içinde aynı mamul/yarı mamule ait birden çok reçetenin saklanması mümkündür.

Alternatif Reçete Kaydı ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Alternatif Reçete Kaydı Ekranı |  |
| --- | --- |
| Mamul Kodu | Görüntülenmesi veya düzenlenmesi istenen mamul kodunun rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile seçildiği alandır. Seçili mamulün var olan tüm reçeteleri, grid ekranda listelenir. **Örneğin;** Alternatif reçete kaydı olmayıp sadece ana reçetesi kaydedilen bir mamul seçilmişse, grid alanda sadece 1 adet ana reçete görüntülenir. "Reçete Kaydı" ekranından kaydı yapılan ana reçeteler<br>grid alanda “0” koduyla görüntülenir. "Alternatif Reçete Kaydı" ekranında, 0 kodlu reçete üzerinde değişiklik yapılmasına izin verilmez. |
| ![](../../../../_assets/55c98e9bdb025ccc0932.png) Yeni | Yeni bir alternatif reçete kaydetmek için kullanılır. Grid ekrandaki reçetelerden çift tıklanarak seçili hale getirilen reçete, ![](../../../../_assets/55c98e9bdb025ccc0932.png) Yeni butonuna tıklandığında kopyalanarak yeni bir alternatif kodu ile gride eklenir. Daha sonra bu kopyalanan reçete üzerinde değişiklikler yapılarak yeni alternatif reçete oluşturulması gerekir. ![](../../../../_assets/55c98e9bdb025ccc0932.png) Yeni butonu ile bir reçete alternatif olarak düzenlenmek için kopyalandığında, grid alanın yanındaki boş alanda, kopyalanan reçeteye ait seviyeler görüntülenir. Reçetenin herhangi bir seviyesi çift tıklanarak seçildikten sonra, ekranın alt kısmına bu seviyeye ait detaylar getirilir. Bu seviyede yapılacak değişimler ekranın altındaki alanlar yardımıyla yapılabilir. **Örneğin;** Alternatif reçetede aynı seviyenin miktarının değiştirilmesi için “Miktar” alanı düzenlenerek, klavyedeki F5 tuşu ile kaydedilmesi gerekir. |
| ![](../../../../_assets/f3f13b883913e649c95e.png) Sil | Seçili alternatif reçeteyi silmek için kullanılan butondur. |
| ![](../../../../_assets/b8d6d64da76940522816.png) Bileşen Sil | Seçilen seviyenin tamamen silinmesi için kullanılan butondur. |
| ![](../../../../_assets/3eac7b956a760c34c878.png) Bileşen Ekle | Seçili alternatif reçeteye yeni bir seviye eklemek için kullanılır. Eklenen bileşene ait detaylar, yine ekranın altındaki alanların kullanılarak girilmesi (Bileşen Kodu, Bileşen Bilgileri, Miktar gibi) ve daha sonra F5 tuşu ile kaydedilmesi gerekir. |
| Sıra No | Reçeteye kaydedilen bileşenler için kullanılan sıra numarasıdır. Kaydedilen her bileşenin sıra numarası olması gerekir. Sıra numarası sayesinde, bileşenlerin hangi sırada kullanıldığı anlaşılır. Bunun dışında, reçetede aynı bileşen birden fazla kullanıldığında, kullanım sırası da tanımlanır. Sıra numaraları en fazla 8 karakter uzunluğunda tanımlanabilir. Program 4 karakterden oluşan sıra numarasını otomatik olarak getirir. Reçete kayıtları tamamlandıktan sonra araya yeni bileşen eklemek gerektiğinde, sıra numarası kullanılarak yapılabilir. **Örneğin;** 0004 ve 0005 sıra numarasına sahip iki bileşen kaydının arasına yeni bir bileşen eklenecek ise; sıra numarasının 00041, 000401,0004001, 00040001 şeklinde verilerek araya girmesi sağlanabilir. |
| Operasyon/Bileşen/Yan Ürün | Reçeteye kaydedilen kalemin Operasyon/Bileşen/Yan Ürün olduğu belirlenir. Operasyon seçeneği, sadece MRP modülüne sahip olan firmalarda kullanılır. Bu firmalar, operasyon tanımlamalarını MRP modülünden yapar ve bu alana operasyon (rota) kodlarını girebilir. Operasyon bir üretim aşamasıdır. Yani, mamule belli bir bileşen veya bileşenlerin kullanılmasından sonra bazı operasyonlardan - yıkama, kurutma, yapıştırma gibi - geçirilmesi gerekebilir. Örneğin; 100 derece sıcaklıkta 10 dk. kaynatılması gibi. MRP modülüne sahip olmayan firmalarda bu alanın "Bileşen" olarak seçilmesi gerekir. Yan Ürün seçeneği ile de, eklenmesi istenen bileşen seçildikten sonra reçeteye eklenir. Yan ürün tipli bileşenler de mamul gibi giriş yapılacak bileşenler olarak düşünülebilir. |
| Bileşen Kodu | Mamul reçetesinde bulunan hammadde, yarı mamul veya yan ürünlerin Stok Kartı Kayıtları ekranından girilen kodlarıdır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile kodlar arasından seçim yapılır. |
| ![](../../../../_assets/4d5937e5d0ca7cc09b74.png)Arama | Yapılandırma bilgilerinden arama yapmak için kullanılan butondur. |
| ![](../../../../_assets/3d053588ba4269cdcdda.png) Asorti | Asorti bilgisi girmek için kullanılan butondur. |
| Asorti Kodu | Asorti kodunun girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, tanımlanan özellik kodlarına ulaşılır. |
| Asorti Kodu Açıklaması | Asorti koduna ait açıklama bilgisinin otomatik olarak ekrana girildiği alandır. |
| Ölçü Birimi | Reçeteye kaydedilen bileşen için ölçü birimi tanımlanan alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile tanımlı ölçü birimlerine ulaşılır. |
| Miktar | Reçete içinde kullanılan bileşen için kullanılacak miktarın tanımlandığı alandır. Reçete toplamında girilen rakama göre, bileşen miktarının katsayısı bu alan üzerinden belirlenir. |
| Sarf Edilen Mamul Kodu | Fiktif mamul için kullanılan alandır. Bazı uygulamalarda hammadde ya da yarı mamullerin üretime girmesi sonucu, birden fazla mamul oluşur. "Reçete Kaydı" bölümünde bileşenler, tek bir mamul için tanımlandığından, bu uygulamayı destelemek için fiktif bir mamul oluşturulur. Bileşenler ve sarf oldukları mamuller, fiktif mamulün reçetesinde tanımlanır. Bunun için öncelikle Stok Modülünde fiktif mamul için bir stok kartı açılması ve Stok Kartı Kayıtları → "Ek Bilgiler" sekmesindeki “Fiktif Mamul” parametresinin işaretlenmesi gerekir. Daha sonra "Reçete Kaydı" bölümünde fiktif mamule ait bir reçete tanımlanması gerekir. Mevcut uygulamadan farklı olarak, reçetedeki bileşenlerin birden fazla mamule sarf olacağı biliniyordu. Bunun için fiktif mamule ait reçetede, bileşenlerin sarf edileceği farklı mamuller için bileşen bazında “Sarf Edilen Mamul Kodu” alanına mamul kodlarının girilmesi gerekir. Üretilen mamuller için de, bileşen kodu “URETIM” olan ve “Sarf Edilen Mamul Kodu” alanında üretilen mamulün kodu yazan bir kaydın girilmesi gerekir. Fiktif mamullere ait işleyişi "Üretim Sonu Kayıtları" bölümünde yer alır. |
| Alt Kodu | Alternatif reçetesi oluşturulmak istenen bir mamulün altında birden çok bileşen olabilir ve bu bileşenlerden bazılarının da kaydedilmiş alternatif reçeteleri bulunabilir. Bu durumda sisteme bileşene ait hangi alternatif reçetenin kullanılacağının söylenmesi mümkündür. Bunun için “Alt. Kodu” alanının kullanılması gerekir. |
| Açıklama | İlgili bileşen için reçete bazında açıklama girilmesini sağlayan alandır. **Örneğin;** Kullanılan bileşenin, mamule yavaş yavaş karıştırılması gibi açıklamalar girilebilir. |
