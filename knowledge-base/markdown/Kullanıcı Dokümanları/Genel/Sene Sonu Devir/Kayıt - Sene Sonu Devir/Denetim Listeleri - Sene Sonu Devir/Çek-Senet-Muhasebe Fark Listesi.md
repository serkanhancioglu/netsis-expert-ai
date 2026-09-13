---
title: "Çek/Senet-Muhasebe Fark Listesi"
page_id: "24753514"
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
  - "Çek/Senet-Muhasebe Fark Listesi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Sene Sonu Devir / Kayıt / Sene Sonu Devir / Denetim Listeleri / Sene Sonu Devir / Çek/Senet-Muhasebe Fark Listesi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWRjZDIzOWViLTBiM2EtNGRjZi05MjcxLTI0NzBkYTU3M2NkOSZsaW5rPTJiZjRkOWRjLWFmMTItNDUwMS04MmU0LWRhMjUzY2RkM2E1MiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=dcd239eb-0b3a-4dcf-9271-2470da573cd9&link=2bf4d9dc-af12-4501-82e4-da253cdd3a52&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "cek-senet-muhasebe-fark-listesi_47074014_24753514.html"
source_version: "2022-10-20T11:39:18.673+03:00"
source_bytes: 86072
fetched_at: "2026-09-13T04:18:19+00:00"
generator: "netsis-scraper 1.0.0"
---
# Çek/Senet-Muhasebe Fark Listesi

Çek/Senet-Muhasebe Fark Listesi, Genel Bölümü'nde, "Kayıt/Sene Sonu Devir" menüsünün altında yer alır. Çek/Senet-Muhasebe Fark İşlemi, Enterprise ürünlerini kullanan ve birden fazla işletme tanımlanan firmalarda işletmelerin merkezinde, Standard ve Entegre ürünleri ile Enterprise ürünlerinde işletme tanımlanmayan firmalarda ise merkez şubede çalıştırılması gerekir. Çek/Senet-Muhasebe Fark Listesi işlem,, Entegrasyon Modülünde tanımlanan çek/senet hesap kodlarına göre, yeni sene şirketinde devirden kaynaklanan çek/senet bakiyeleri ile çek/senet kodlarının yeni sene şirketindeki açılış fişinde yer alan bakiyesi arasındaki farkın belirlenmesini sağlar. Bulunan fark tutarları, isteğe bağlı olarak muhasebe kayıtlarına işlenebilir.

Entegrasyon modülünde “Dövizli Senet/Çek İçin Özel Hesap Kodu Uygulaması Var” parametresi işaretli ise, Entegrasyon kodlarında çek ve senetler için girilen muhasebe hesap kodları değil, çek ve senetlerin girişlerinde kullanılan döviz tipleri için kullanılan hesap kodları kontrol edilir.

Çek/Senet-Muhasebe Fark Listesi ekranı; Giriş, İşlem ve İşlem Sonucu olmak üzere üç sekmeden oluşur.

**Giriş**

![](../../../../../_assets/73f7c6d208cf6e15d9e6.png)

**İşlem**

**![](../../../../../_assets/0df294c87aace57a3fa1.png)**

Çek/Senet-Muhasebe Fark Listesi ekranı İşlem sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Çek/Senet-Muhasebe Fark Listesi Ekranı |  |
| --- | --- |
| Devir Şirketi | Devredilen çek/senet tutarları ile muhasebe hesap bakiyelerinin kontrol edileceği yeni sene şirketinin girildiği alandır. "Yeni Yıl Kopyalama" işlemi ile açılan yeni sene şirketi, program tarafından otomatik olarak ekrana getirilir. |
| Modül | Fark kontrolünün yapılacağı modülün belirlendiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile, Müşteri Çekleri, Müşteri Senetleri, Borç Çekleri ya da Borç Senetleri modüllerinden biri seçilir. |
| Yuvarlama Borç/Yuvarlama Alacak Hesap Kodu | Bulunan farkın muhasebe fişi olarak işlenmesi için çek/senet hesap kodlarıyla karşılıklı çalışacak muavin hesapların girilmesi gerekir. "Çek/Senet" modülündeki devir değeri ile muhasebe açılış fişindeki devir değerini eşitlemek için gerekli fark ilgili muhasebe hesap koduna işlenir ve karşılığında da borç ya da alacak olarak yuvarlama hesapları çalışır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılır. |
| Kayıtlara Geçsin | Bulunan fark tutarlarının, yeni sene şirketinde yevmiye fişi haline getirilmesi için kullanılan seçenektir. Oluşturulan fişin tarihi 01/01/2019, açıklaması ise “Çek/Senet-Muhasebe Fark Listesi” olacaktır. İşlem, bu seçenek işaretlenmeden çalıştırılırsa, bulunan fark tutarları işlem tamamlandıktan sonra sadece listelenir. Muhasebe kayıtlarına geçmez. |
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
