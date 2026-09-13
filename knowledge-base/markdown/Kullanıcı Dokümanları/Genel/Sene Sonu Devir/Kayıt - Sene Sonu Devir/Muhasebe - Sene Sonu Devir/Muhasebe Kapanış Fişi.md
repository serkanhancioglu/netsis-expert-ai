---
title: "Muhasebe Kapanış Fişi"
page_id: "24753463"
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
  - "Muhasebe / Sene Sonu Devir"
  - "Muhasebe Kapanış Fişi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Sene Sonu Devir / Kayıt / Sene Sonu Devir / Muhasebe / Sene Sonu Devir / Muhasebe Kapanış Fişi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTk4YWNkOWY4LWUxYWUtNDFlYi05NDRkLTA0OTIzYTNjNmFiZiZsaW5rPTZhNmNmMDQzLTFkZmEtNGJlOS1hNTY0LThkMDdhNmM4MGMzYyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=98acd9f8-e1ae-41eb-944d-04923a3c6abf&link=6a6cf043-1dfa-4be9-a564-8d07a6c80c3c&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "muhasebe-kapanis-fisi_47073655_24753463.html"
source_version: "2022-10-20T09:38:26.990+03:00"
source_bytes: 113927
fetched_at: "2026-09-13T04:18:14+00:00"
generator: "netsis-scraper 1.0.0"
---
# Muhasebe Kapanış Fişi

Muhasebe Kapanış Fişi, Genel Bölümü'nde, "Kayıt/Sene Sonu Devir" menüsünün altında yer alır. Muhasebe kapanış fişinin her işletme ve şube için ayrı ayrı oluşturulması gerekir. Eski sene muhasebe kayıtları tamamlandığında, "Muhasebe" bölümünün devri iki aşamalı yapılır. İlk aşama, dönem kapanış fişidir.

Muhasebe kayıtlarının bittiğinden ve mizanın tuttuğundan emin olmadan bu işlemin çalıştırılmaması gerekir. Aksi halde, kapanış ve açılış fişlerinde yapılacak herhangi bir düzenlemenin elle yapılması gerekir.

"Muhasebe Kapanış Fişi" ekranı; Giriş, İşlem ve İşlem Sonucu olmak üzere üç sekmeden oluşur.

**Giriş**

**![](../../../../../_assets/0d30596c64fbb386e3e5.png)**

**İşlem**

**![](../../../../../_assets/0edd2c272891c7a4a5a1.png)**

Muhasebe Kapanış Fişi ekranı İşlem sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Muhasebe Kapanış Fişi Ekranı | Genel Parametreler |
| --- | --- |
| Kapanış Tarihi | İçinde bulunulan şirket için program tarafından otomatik olarak oluşturulacak kapanış fişine verilen tarihin girildiği alandır. Girilen tarihe, yılın son ayının son fiş numarasının bir fazlası kapanış fiş numarası olarak program tarafından otomatik oluşturulur. |
| Proje Kodu Bazında Devir | "Proje Kodu Uygulaması" olan firmalarda kapanış fişinin proje kodu kırılımı ile yapılmasını sağlayan seçenektir. Her bir muavinin hesap kapanışı, proje kodu bazında bakiyeleri dikkate alınarak yapılır. |
| Dövizli Devir | Muhasebe kayıtlarını döviz bazında takip eden firmaların kapanış fişinin, döviz değerleri ile oluşması için kullanılan seçenektir. IAS29, FAS52 seçeneklerinden biriyle çalışan firmaların bu seçeneği işaretlemesine gerek yoktur. İşlem sırasında, kapanış fişi döviz tipi kırılımı ile oluşturulur ve kayıtlara her bir döviz tipine göre hesaplanan döviz tutarları ve firma döviz tutarları - varsa - aktarılır. |
| IAS29/FAS52/Enflasyon Muhasebesi | IAS29/FAS52/Enflasyon Muhasebesi seçeneği ile aşağıdaki işlemlerin yapılması gerekir: - Kapanış fişini oluşturacak firmaların, Muhasebe → Kayıt → Muhasebe Parametreleri → IAS29, FAS52 veya Enflasyon Muhasebesi seçeneklerinden birini mutlaka işaretlemesi gerekir.<br>- Kapanış fişi oluşturulmadan önce, devir öncesi son dönem için enflasyon muhasebesi işlemlerinin mutlaka çalıştırılması gerekir. IAS29 ya da FAS52 için kapanış fişi ile firma döviz tutarlarının hesap kodu bazında bakiyeleri, TL’si sıfır (0), firma döviz tipi ve tutarı alanları dolu olan kayıtlar oluşturulur. IAS29’a göre muhasebe yapılması halinde ve muavin hesabın kapanış fişine aktarılacak TL ve Firma Döviz Tutarları ayrı yönde ise (TL bakiyesi borç, Firma Döviz bakiyesi alacak ya da tam tersi), kapanış fişinde TL için ayrı Firma Dövizi için ayrı satırlar oluşturulur. |
| Referans Kodu Bazında Devir | Referans kodu bazında devir yapılması için kullanılan seçenektir. |
| 0 Tutar Kontrolünde Firma Döviz Tutarı Dikkate Alınsın | Kapanış fişi oluşturulurken tutar 0, döviz tutarı 0 ve firma döviz tutarı 0 değerinden farklı olan hesap kodlarının fişe eklenmesi için kullanılan seçenektir. |
| Şubeler İçin Kapanış Fişi Oluşturulabilsin | Şubeler için kapanış fişi oluşturulması için kullanılan seçenektir. |
| Muhasebe Kapanış Fişi Ekranı | Hesap Planı Kısıtları **Devri yapılması istenen hesaplarla ilgili kısıtlamaların yapıldığı sekmedir. Ekranda, hesap planı kayıtlarında girilen bilgiler listelenir. Hesapların bölüm bölüm devrinin yapılmasını sağlamak için kullanılır.** |
| Saha Adı | "Hesap Planı Kısıtları" sekmesine tıklanması ile görüntülenir. Muhasebe kapanış işleminde baz alınacak saha adı için kısıt verilen alandır. İlgili hücre üzerinde iken klavyede yer alan **Boşluk Çubuğuna** basılarak aktif hale gelen aşağı ok butonu, kısıt verilmesi istenen sahalara ulaşılmasını sağlar. Satırın silinmesi için klavyedeki "Delete" tuşuna basılması gerekir. ![](../../../../../_assets/c8c47daa08384cd8f0a6.png) |
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
