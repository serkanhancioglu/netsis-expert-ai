---
title: "Stok-Muhasebe Fark İşlemi"
page_id: "24753507"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Genel"
  - "Sene Sonu Devir"
  - "Kayıt / Sene Sonu Devir"
  - "Denetim Listeleri / Sene Sonu Devir"
  - "Stok-Muhasebe Fark İşlemi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Sene Sonu Devir / Kayıt / Sene Sonu Devir / Denetim Listeleri / Sene Sonu Devir / Stok-Muhasebe Fark İşlemi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTlhMjZlNGQxLWRkYmMtNDZiYi05ZDM0LWQxYmUxZTcxYzkxMSZsaW5rPTRmY2U3YmYzLTNjY2ItNDVlZC04YThjLWZkM2I5MzQxMzQwMiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=9a26e4d1-ddbc-46bb-9d34-d1be1e71c911&link=4fce7bf3-3ccb-45ed-8a8c-fd3b93413402&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "stok-muhasebe-fark-islemi_47073907_24753507.html"
source_version: "2022-10-20T10:00:59.927+03:00"
source_bytes: 183593
fetched_at: "2026-09-13T04:18:18+00:00"
generator: "netsis-scraper 1.0.0"
---
# Stok-Muhasebe Fark İşlemi

Stok-Muhasebe Fark İşlemi, Genel Bölümü'nde, "Kayıt/Sene Sonu Devir" menüsünün altında yer alır. Stok-Muhasebe Fark İşlemi, Enterprise ürünlerini kullanan ve birden fazla işletme tanımlanan firmalarda işletmelerin merkezinde, Standard ve Entegre ürünleri ile Enterprise ürünlerinde işletme tanımlanmayan firmalarda ise merkez şubede çalıştırılması gerekir. Stok-Muhasebe Fark İşlemi işlemi, Stok Hesap Kayıtları - Muhasebe Hesap Koduna göre, yeni sene şirketinde devirden kaynaklanan cari hareketlerdeki bakiyeler ile cari hesapların muhasebe hesap kodlarının yeni sene şirketindeki açılış fişinde yer alan bakiyesi arasındaki farkın belirlenmesini sağlar. Bulunan fark, isteğe bağlı olarak muhasebe kayıtlarına işlenebilir.

Stok-Muhasebe Fark İşlemi ekranı; Giriş, İşlem ve İşlem Sonucu olmak üzere üç sekmeden oluşur.

**Giriş**

**![](../../../../../_assets/6d9f997b2161adbb9daf.png)**

**İşlem**

![](../../../../../_assets/97877322ecb64c474b48.png)

Stok-Muhasebe Fark İşlemi ekranı İşlem sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Stok-Muhasebe Fark Listesi Ekranı |  |
| --- | --- |
| Devir Şirketi | Stok devirleri ile muhasebe hesap bakiyelerinin kontrol edileceği yeni sene şirketinin girildiği alandır. "Yeni Yıl Kopyalama" işlemi ile açılan yeni sene şirketi, program tarafından otomatik olarak ekrana getirilir. |
| Stok Kodu | Belli bir stok için fark kontrolü yapılması istendiği zaman stok kodu aralığı girilen alandır. Alanın boş bırakılması halinde işlem tüm stok kodları için çalıştırılır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, |
| Muhasebe Detay Kodu | Sadece belli muhasebe detay kodlarında bulunan alış hesap kodları için fark kontrolü yapılması istendiği zaman muhasebe detay kodu aralığı girilen alandır. Alanın boş bırakılması halinde işlem, muhasebe hesap kayıtlarında girilen tüm muhasebe hesap kodları için çalıştırılır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, muhasebe kodları arasından seçim yapılır. |
| Mali Grup Kodu | "Maliyet Muhasebesi" kullanan firmalarda "Mali Grup Kodu" kayıtlarında girilen mamul ve yarı mamul hesabına göre fark kontrolü yapılır. "Stok Kartı Kayıtları" ekranında, tipi mamul ya da yarı mamul işaretlenen stokların Mamul Grup Kodları için aralık girilen alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile grup kodları arasından seçim yapılır. |
| Yuvarlama Borç/Alacak Hesap Kodu | Bulunan farkın muhasebe fişi olarak işlenmesi için, cari muhasebe hesap kodlarıyla karşılıklı çalışacak muavin hesapların girilmesi gerekir. "Stok" modülündeki devir değeri ile muhasebe açılış fişindeki devir değerini eşitlemek için gerekli fark ilgili muhasebe hesap koduna işlenir ve karşılığında da borç ya da alacak olarak yuvarlama hesapları çalışır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılır. |
| Kayıtlara Geçsin | Bulunan fark tutarlarının, yeni sene şirketinde yevmiye fişi haline getirilmesi için kullanılan seçenektir. Oluşturulan fişin tarihi 01/01/2019, açıklaması ise “Stok-Muhasebe Fark İşlemi” olacaktır. İşlem, bu seçenek işaretlenmeden çalıştırılırsa, bulunan fark tutarları işlem tamamlandıktan sonra sadece listelenir. Muhasebe kayıtlarına geçmez. |
| ![](../../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilgilerin onaylanmasını sağlayan butondur. |
| ![](../../../../../_assets/249197106fa4d90d9fe9.png) Çıkış | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |

**İşlem Sonucu**

İşlem sırasında oluşan hatalar "İşlem Sonucu" sekmesinde görüntülenerek farenin sağ tuşuna tıklanarak dosyaya kaydedilir. Gelen hataların incelenmesi gerekir.

"Yeni Yıl Kopyalama" işlemi, devir şirketi oluşturulduktan sonra, herhangi bir hatadan dolayı yarım kalabilir. İşlemin kesilmesine sebep olan problem çözüldükten sonra; yeni sene için açılan şirketi sıfırlayarak ya da, yeni sene hazırlık işlemine kalınan yerden devam etmek mümkündür.

Açılan şirketi sıfırlayarak yeni yıl kopyalama işlemine baştan başlamak için, "Şirket Silme" işlemi ile yeni şirketin silinmesi gerekir.

Kalınan yerden "Yeni Yıl Kopyalama" işlemine devam etmek için, işlem tekrar çalıştırılarak, sorgulanan sahalara daha önceden girilen bilgilerin girilmesi ve "Evet" butonuna tıklanması gerekir.

Bu durumda, kalınan yerden işleme devam etmek istenip istenmediğinin sorgulandığı bir ekran görüntülenir. “Evet” butonuna tıklanması ile yeni yıl şirketinin tekrar kopyalanmasına gerek kalmadan devir işlemine devam edilir.

İşlemler bittiğinde, modül devirleri öncesi, yeni sene kayıtlarına başlama ortamının hazırlanması işlemi tamamlanır. İstendiğinde eski senenin kayıtları bitene kadar, hiç bir modülün devri yapılmadan eski sene şirketinde ve yeni sene şirketinde ayrı ayrı çalışılarak kayıtlara devam edilebilir. Eski senenin devir kayıtları, eski sene kapatılıp devir yapıldığında yeni sene bilgilerine aktarılır. İstendiğinde modül devirleri programın içinden yapılmayıp, açılan yeni sene şirketinde elle kaydedilebilir. Bu işlemlerden biri yapılmadan yeni sene bakiyelerini doğru olarak izlemek mümkün değildir.

"Yeni Yıl Kopyalama" işlemi ile devri oluşturulan eski şirkete girerken, “Şirket devri yapılmıştır. Devir Şirketi: DEVIR. Bu şirketin sadece rapor amaçlı kullanılması tavsiye edilmektedir. Yeni yıla ait kayıtlarınızı veya düzeltme işlemlerinizi DEVIR şirketine yapabilirsiniz!” şeklinde bir uyarı mesajı görüntülenir.

Dosyaya bağlanan ve dosyası kapatılan dış ticaret belgelerinin yeni yıl şirketine aktarılmaması sağlanır.
