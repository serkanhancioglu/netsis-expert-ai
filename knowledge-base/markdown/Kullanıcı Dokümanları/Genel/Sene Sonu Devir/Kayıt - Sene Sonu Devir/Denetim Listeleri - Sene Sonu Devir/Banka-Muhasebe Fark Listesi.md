---
title: "Banka-Muhasebe Fark Listesi"
page_id: "24753519"
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
  - "Banka-Muhasebe Fark Listesi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Sene Sonu Devir / Kayıt / Sene Sonu Devir / Denetim Listeleri / Sene Sonu Devir / Banka-Muhasebe Fark Listesi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTgxMThjMzlhLTU4NzEtNDdmMi1iNzYxLWUwNmU2MWU3N2Y5ZiZsaW5rPTRhMjMzMDJlLWFkOTMtNDNjNC1hYmI1LTJjODhkYjI5Y2QyMiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=8118c39a-5871-47f2-b761-e06e61e77f9f&link=4a23302e-ad93-43c4-abb5-2c88db29cd22&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "banka-muhasebe-fark-listesi_47074045_24753519.html"
source_version: "2022-10-20T11:47:19.227+03:00"
source_bytes: 92024
fetched_at: "2026-09-13T04:18:20+00:00"
generator: "netsis-scraper 1.0.0"
---
# Banka-Muhasebe Fark Listesi

Banka-Muhasebe Fark Listesi, Genel Bölümü'nde, "Kayıt/Sene Sonu Devir" menüsünün altında yer alır. Banka-Muhasebe Fark İşlemi, Enterprise ürünlerini kullanan ve birden fazla işletme tanımlanan firmalarda işletmelerin merkezinde, Standard ve Entegre ürünleri ile Enterprise ürünlerinde işletme tanımlanmayan firmalarda ise merkez şubede ve eski sene şirketinde çalıştırılması gerekir.

Banka-Muhasebe Fark Listesi işlemi, banka hesap kayıtlarındaki "Muhasebe Hesap Koduna" göre, yeni sene şirketinde devirden kaynaklanan banka hareket bakiyeleri ile banka muhasebe hesap kodlarının yeni sene şirketindeki açılış fişinde yer alan bakiyesi arasındaki farkın belirlenmesini sağlar. Bulunan fark tutarları, isteğe bağlı olarak muhasebe kayıtlarına işlenebilir.

"Banka-Muhasebe Fark Listesi" ekranı; Giriş, İşlem ve İşlem Sonucu olmak üzere üç sekmeden oluşur.

**Giriş**

**![](../../../../../_assets/a563c6826a32608e3b24.png)**

**İşlem**

![](../../../../../_assets/69a69eab061048c998cd.png)

Banka-Muhasebe Fark Listesi ekranı İşlem sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Banka-Muhasebe Fark Listesi Ekranı |  |
| --- | --- |
| Devir Şirketi | Devredilen banka hesap tutarları ile muhasebe hesap bakiyelerinin kontrol edileceği yeni sene şirketinin girildiği alandır. "Yeni Yıl Kopyalama" işlemi ile açılan yeni sene şirketi, program tarafından otomatik olarak ekrana getirilir. |
| Banka Hesap Kodu | Sadece belirli banka hesap kodları için fark kontrolü yapılması istendiği zaman banka hesap kodu aralığı girilen alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, banka hesap kodları arasından seçim yapılır. |
| Hesap Muhasebe Kodu | Sadece belirli banka muhasebe hesap kodları için fark kontrolü yapılması istendiği zaman muhasebe hesap kodu aralığı girilen alandır. Boş bırakılması halinde işlem, "Banka Hesap Kayıtlarında" girilen tüm muhasebe hesap kodları için çalıştırılır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, muhasebe hesap kodları arasından seçim yapılır. |
| Yuvarlama Borç/Alacak Hesap Kodu | Bulunan farkın muhasebe fişi olarak işlenmesi için, banka muhasebe hesap kodlarıyla karşılıklı çalışacak muavin hesapların girilmesi gerekir. Banka modülündeki devir değeri ile muhasebe açılış fişindeki devir değerini eşitlemek için gerekli fark ilgili muhasebe hesap koduna işlenir ve karşılığında da borç ya da alacak olarak yuvarlama hesapları çalışır. |
| Kayıtlara Geçsin | Bulunan fark tutarlarının, yeni sene şirketinde yevmiye fişi haline getirilmesini sağlayan seçenektir. Oluşturulan fişin tarihi 01/01/2020, açıklaması ise “Banka-Muhasebe Fark İşlemi” olarak geçer. İşaretlenmediği zaman, bulunan fark tutarları işlem tamamlandıktan sonra sadece listelenir. Muhasebe kayıtlarına geçmez. |
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
