---
title: "Muhasebe Açılış Fişi"
page_id: "24753469"
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
  - "Muhasebe Açılış Fişi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Sene Sonu Devir / Kayıt / Sene Sonu Devir / Muhasebe / Sene Sonu Devir / Muhasebe Açılış Fişi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTI0NmJjYWFhLTg5ZGUtNGY0My05MjZmLTIxNzBhYjM0MjJmYyZsaW5rPWY2OTg2MDk0LTA2MTctNDMzYy04ZGQ4LTM2YzYzOGIxZjExMyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=246bcaaa-89de-4f43-926f-2170ab3422fc&link=f6986094-0617-433c-8dd8-36c638b1f113&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "muhasebe-acilis-fisi_47073832_24753469.html"
source_version: "2022-10-20T09:52:44.400+03:00"
source_bytes: 79544
fetched_at: "2026-09-13T04:18:14+00:00"
generator: "netsis-scraper 1.0.0"
---
# Muhasebe Açılış Fişi

Muhasebe Açılış Fişi, Genel Bölümü'nde, "Kayıt/Sene Sonu Devir" menüsünün altında yer alır. Muhasebe açılış fişinin her işletme ve şube için ayrı ayrı oluşturulması gerekir. Muhasebe Açılış Fişi, yeni sene şirketine aktarılması gereken açılış fişinin oluşturulduğu ve program tarafından otomatik olarak aktarıldığı bölümdür. Muhasebe Açılış Fişi işlemini çalıştırmadan önce "Dönem Sonu Kapanış Fişi" işlemini çalıştırmanız gerekir. Kapanış fişi baz alınarak yeni senedeki açılış fişi oluşturulur. Devir yapılmadan yeni sene şirketinde muhasebe kayıtlarına başlandığı zaman ilk ayın yevmiye fiş numaralandırmasını, açılış fişi için bir numara ayıracak şekilde yapılması gerekir.

**Örneğin;** 1 numaralı fişi açılış fişi için ayırıp, kayıtlara 2 numaralı fişten başlanması gerekir.

Muhasebe Açılış Fişi ekranı; Giriş, İşlem ve İşlem Sonucu olmak üzere üç sekmeden oluşur.

**Giriş**

![](../../../../../_assets/bedf2ed80987ace06791.png)

Muhasebe Açılış Fişi ekranı İşlem sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Muhasebe Açılış Fişi Ekranı |  |
| --- | --- |
| Devir Şirketi | Yeni yılda kullanılacak şirket isminin girildiği alandır. Girilen şirketin önceden açılmaması gerekir. Girilen şirket program tarafından açılır. "Yeni Yıl Kopyalama" işlemi aynı yeni yıl şirketinin ismi kullanılarak birden fazla tekrarlanıyorsa, "Yeni Yıl Kopyalama" işlemi öncesinde devir şirketinin "Şirket Silme işlemiyle silinmesi gerekir. |
| Kapanış Ayı | Devir yapılan şirkette, kapanış fişinin oluşturulduğu ay kodunun girildiği alandır. |
| Kapanış Fiş No | Devir yapılan şirkette, oluşturulan kapanış fiş numarasının girildiği alandır. Program tarafından, "Kapanış Ayı" alanında girilen aya ait son fiş numarası otomatik olarak ekrana getirilir. Kapanış fişi otomatik olarak getirilen fiş numarasından farklı ise kullanıcı tarafından değiştirilebilir. |
| Açılış Tarihi | Yeni yıl için açılan şirkette oluşturulacak açılış fişi için tarih girilen alandır. Yılın ilk ayı program tarafından otomatik olarak ekrana getirilir. **Örneğin;** 01.01.2020 |
| İlk Fiş No | Yeni yıl şirketinde oluşturulacak açılış fişi için fiş numarası girilen alandır. Yeni yıl şirketinin "Muhasebe" modülünde işlemler yapılsa bile, ilk ayın ilk fiş numarasının açılış kaydı için boş bırakılması gerekir. Böyle olacağı düşünülerek 1. Ay için bu alana 000000000000001 numaralı fiş program tarafından otomatik olarak ekrana getirilir. |
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
