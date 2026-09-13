---
title: "Sipariş Devir"
page_id: "24753426"
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
  - "Lojistik Satış"
  - "Sipariş Devir"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Sene Sonu Devir / Kayıt / Sene Sonu Devir / Lojistik Satış / Sipariş Devir"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWMwYzU5ZmMzLWIxM2UtNDRkNi04MjRiLWU2YmJiYTEzYjdlYiZsaW5rPTEwNmNiODQ0LTY3NDYtNDIzYi1iNTk0LTVmNWY0MGQ5OGFjZSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=c0c59fc3-b13e-44d6-824b-e6bbba13b7eb&link=106cb844-6746-423b-b594-5f5f40d98ace&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "siparis-devir_47073456_24753426.html"
source_version: "2022-10-19T13:40:43.367+03:00"
source_bytes: 79626
fetched_at: "2026-09-13T04:18:06+00:00"
generator: "netsis-scraper 1.0.0"
---
# Sipariş Devir

Sipariş Devir, Genel Bölümü'nde, "Kayıt/Sene Sonu Devir" menüsünün altında yer alır. Sipariş devrinin yapılmasını sağlayan bölümdür. Sipariş Devir, eski sene şirketindeki teslimatı yapılmamış siparişlerin takibine, yeni senede de devam edilmesini sağlamak için siparişlerin yeni sene şirketine aktarılması işlemini gerçekleştirir. Sipariş Devir; Giriş, İşlem ve İşlem Sonucu sekmesinden oluşur. Sipariş Devir işleminin, tüm versiyonlarda her işletme ve şube için ayrı ayrı çalıştırılması gerekir. Sipariş uygulamasının kullanılması halinde, stok devrinden önce mutlaka sipariş devrinin yapılması gerekir.

**Giriş**

Sipariş Devir ekranı Giriş sekmesinde, devir tarihinden sonraki siparişler aynen aktarılır. Bu tarihten önceki siparişlerin bakiyeli olanları aktarılır.

![](../../../../../_assets/36e917d4cb5196356e79.png)

**İşlem**

**![](../../../../../_assets/959cc3f2eac0c39c2b9e.png)**

Sipariş Devir ekranı İşlem sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Sipariş Devir Ekranı |  |
| --- | --- |
| Devir Şirketi | Yeni yılda kullanılacak şirket isminin girildiği alandır. Girilen şirketin önceden açılmaması gerekir. Girilen şirket program tarafından açılır. "Yeni Yıl Kopyalama" işlemi aynı yeni yıl şirketinin ismi kullanılarak birden fazla tekrarlanıyorsa, "Yeni Yıl Kopyalama" işlemi öncesinde devir şirketinin "Şirket Silme işlemiyle silinmesi gerekir. |
| Devir Baz Tarihi | Sipariş devri için baz alınacak tarihin girildiği alandır. Devir baz tarihi olarak verilecek tarihten önceki siparişlerden - sipariş kayıt tarihi baz alınır - sadece teslimatı tamamlanmayan ve bu tarihten sonraki tüm sipariş kayıtları yeni sene şirketine aktarılır. Sipariş modülünün kullanılmadığı durumlarda, bu bölümde herhangi bir şey yapılmasına gerek yoktur. |
| Sipariş Tipi | Müşteri Siparişi, Satıcı Siparişi ya da Hepsi seçenekleri kullanılarak devir yapılması için sipariş tipi kısıdı verilen alandır. |
| Parçalanmış Siparişler Devredilsin | Merkezden girilen ve şube kodları verilerek şube bazında parçalanan siparişlerden, teslimatı tamamlanmayan siparişlerin devir şirketine aktarılması için kullanılan seçenektir. Merkez işletme veya şubenin siparişleri devrediliyorsa, bu alan işaretli olarak ekrana gelir ve değişiklik yapılmaz. Merkez olmayan bir işletme veya şubenin siparişleri devrediliyorsa işaretli olarak ekrana gelmez. Bunun sebebi, parçalı siparişin sadece merkezden girilmesinden kaynaklanır. |
| ![](../../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilgilerin onaylanmasını sağlayan butondur. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |

**İşlem Sonucu**

İşlem sırasında oluşan hatalar "İşlem Sonucu" sekmesinde görüntülenerek farenin sağ tuşuna tıklanarak dosyaya kaydedilir. Gelen hataların incelenmesi gerekir.

"Yeni Yıl Kopyalama" işlemi, devir şirketi oluşturulduktan sonra, herhangi bir hatadan dolayı yarım kalabilir. İşlemin kesilmesine sebep olan problem çözüldükten sonra; yeni sene için açılan şirketi sıfırlayarak ya da, yeni sene hazırlık işlemine kalınan yerden devam etmek mümkündür.

Açılan şirketi sıfırlayarak yeni yıl kopyalama işlemine baştan başlamak için, "Şirket Silme" işlemi ile yeni şirketin silinmesi gerekir.

Kalınan yerden "Yeni Yıl Kopyalama" işlemine devam etmek için, işlem tekrar çalıştırılarak, sorgulanan sahalara daha önceden girilen bilgilerin girilmesi ve "Evet" butonuna tıklanması gerekir.

Bu durumda, kalınan yerden işleme devam etmek istenip istenmediğinin sorgulandığı bir ekran görüntülenir. “Evet” butonuna tıklanması ile yeni yıl şirketinin tekrar kopyalanmasına gerek kalmadan devir işlemine devam edilir.

İşlemler bittiğinde, modül devirleri öncesi, yeni sene kayıtlarına başlama ortamının hazırlanması işlemi tamamlanır. İstendiğinde eski senenin kayıtları bitene kadar, hiç bir modülün devri yapılmadan eski sene şirketinde ve yeni sene şirketinde ayrı ayrı çalışılarak kayıtlara devam edilebilir. Eski senenin devir kayıtları, eski sene kapatılıp devir yapıldığında yeni sene bilgilerine aktarılır. İstendiğinde modül devirleri programın içinden yapılmayıp, açılan yeni sene şirketinde elle kaydedilebilir. Bu işlemlerden biri yapılmadan yeni sene bakiyelerini doğru olarak izlemek mümkün değildir.

"Yeni Yıl Kopyalama" işlemi ile devri oluşturulan eski şirkete girerken, “Şirket devri yapılmıştır. Devir Şirketi: DEVIR. Bu şirketin sadece rapor amaçlı kullanılması tavsiye edilmektedir. Yeni yıla ait kayıtlarınızı veya düzeltme işlemlerinizi DEVIR şirketine yapabilirsiniz!” şeklinde bir uyarı mesajı görüntülenir.

Dosyaya bağlanan ve dosyası kapatılan dış ticaret belgelerinin yeni yıl şirketine aktarılmaması sağlanır.
