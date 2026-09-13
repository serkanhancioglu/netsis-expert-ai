---
title: "Senet/Çek Devir"
page_id: "24753454"
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
  - "Finans / Sene Sonu Devir"
  - "Senet/Çek Devir"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Sene Sonu Devir / Kayıt / Sene Sonu Devir / Finans / Sene Sonu Devir / Senet/Çek Devir"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTFlOTA4MjQ1LTY5ZWYtNDY0Ny04MjA2LWU3MTdhOGMzMmU2NSZsaW5rPTYxYmI4MmIxLWE3N2UtNGU4NS05NTFhLTc0MWM0Mzg3OTFkNyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=1e908245-69ef-4647-8206-e717a8c32e65&link=61bb82b1-a77e-4e85-951a-741c438791d7&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "senet-cek-devir_47073607_24753454.html"
source_version: "2022-10-20T09:20:44.807+03:00"
source_bytes: 79792
fetched_at: "2026-09-13T04:18:10+00:00"
generator: "netsis-scraper 1.0.0"
---
# Senet/Çek Devir

Senet/Çek Devir, Genel Bölümü'nde, "Kayıt/Sene Sonu Devir" menüsünün altında yer alır. Senet/Çek Devir işleminin her işletme ve şube için ayrı ayrı çalıştırılması gerekir. Senet/Çek Devir, Müşteri Çekleri/Müşteri Senetleri ile Borç Çeklerinin/Borç Senetlerinin devredilmesini sağlayan bölümdür.

Senet/Çek Devir ekranı; Giriş, İşlem ve İşlem Sonucu olmak üzere üç sekmeden oluşur.

**Giriş**

![](../../../../../_assets/b29046427222af304a4f.png)

**İşlem**

**![](../../../../../_assets/798e72d53cc3d622bf45.png)**

Senet/Çek Devir ekranı İşlem sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Senet/Çek Devir Ekranı |  |
| --- | --- |
| Devir Şirketi | Yeni yılda kullanılacak şirket isminin girildiği alandır. Girilen şirketin önceden açılmaması gerekir. Girilen şirket program tarafından açılır. "Yeni Yıl Kopyalama" işlemi aynı yeni yıl şirketinin ismi kullanılarak birden fazla tekrarlanıyorsa, "Yeni Yıl Kopyalama" işlemi öncesinde devir şirketinin "Şirket Silme işlemiyle silinmesi gerekir. |
| Modül | Devri yapılacak senet/çek modüllerinin listelendiği alandır. Modüller sırasıyla seçilerek senet/çek devirleri tamamlanır. Alanın sağ tarafında yer alan aşağı ok butonu ile seçim yapılır. Devir işlemi çalıştırılmadan önce Çek/Senet Modülü → İşlemler → "Toplu Ödeme Bildirimi" bölümünün daha önceden çalıştırılması gerekir. Senet ya da çekin ödeme tarihi, devir baz tarihinden büyükse yeni yıl şirketine aynen aktarılır. |
| Devir Baz Tarihi | Girilecek tarihten daha ileri vade tarihine sahip senetlerin/çeklerin tamamı yeni sene şirketine aktarılır. Vade tarihleri baz tarihinden önceki vadeli senetler/çekler yeni sene şirketine aktarılmaz. |
| Bekleyenleri Aktar | Vade tarihleri devir baz tarihinden önce ve durumu "Beklemede" olan senetlerin/çeklerin yeni sene şirketine aktarılması için kullanılan seçenektir. Senet/çek durumu "Beklemede" olanlarının takibine yeni yıl şirketinde devam edilmesini sağlar. Alan işaretlenmediği zaman senedin/çekin durumuna bakılmaksızın baz tarihinden önceki senetler/çekler yeni sene şirketine aktarılmaz. Yeni yıl için oluşturulan şirkette çek/senet ve alındı/verildi numaralarının, eski sene bilgilerinin kaldığı son numaradan takip edilerek kullanılmaya devam edilmesi gerektiğinin unutulmaması gerekir. Senet/Çek devri yapıldıktan sonra bir hata yapıldığı tespit edilirse, devir işlemi tekrar çalıştırılabilir. Bu durumda önceden devredilen kayıtlar silinerek, yeni kayıtlar yeni yıl şirketinde oluşur. |
| Daha Önce Devredilenler Silinsin | Senet/Çek devri yapılırken daha önce devredilenlerin silinmesi için kullanılan seçenektir. |
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
