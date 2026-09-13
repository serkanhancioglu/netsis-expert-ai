---
title: "Talep/Teklif Devir"
page_id: "24753404"
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
  - "Talep/Teklif Devir"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Sene Sonu Devir / Kayıt / Sene Sonu Devir / Lojistik Satış / Talep/Teklif Devir"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWU2MDg0ZjQzLTIzZWMtNDE3ZC04M2MxLTQ0MzY2Y2Q0OTU2YSZsaW5rPWI5M2Y2MWZjLTRkOGYtNGYyYS05MTlhLTI5NDc4YmZiZmE4MCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=e6084f43-23ec-417d-83c1-44366cd4956a&link=b93f61fc-4d8f-4f2a-919a-29478bfbfa80&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "talep-teklif-devir_47073445_24753404.html"
source_version: "2022-12-12T14:50:21.700+03:00"
source_bytes: 109550
fetched_at: "2026-09-13T04:18:05+00:00"
generator: "netsis-scraper 1.0.0"
---
# Talep/Teklif Devir

Talep/Teklif Devir, Genel Bölümü'nde, "Kayıt/Sene Sonu Devir" menüsünün altında yer alır. Talep/Teklif devrinin yapılmasını sağlayan bölümdür. Talep Teklif Devir işlemi ile eski sene şirketindeki teslimatı yapılmamış talep ve tekliflerin takibine, yeni senede de devam edilmesini sağlamak için talep ve tekliflerin yeni sene şirketine aktarılması işlemini gerçekleştirir. Talep/Teklif Devir ekranı; Giriş, İşlem ve İşlem Sonucu sekmesinden oluşur. Talep/Teklif Devir işleminin, tüm versiyonlarda her işletme ve şube için ayrı ayrı çalıştırılması gerekir. Talep/Teklif uygulamasının kullanılması halinde, stok devrinden önce mutlaka Talep/Teklif devrinin yapılması gerekir.

**Giriş**

Devir tarihinden sonraki Talepler/Teklifler aynen aktarılır. Bu tarihten önceki Taleplerin/Tekliflerin bakiyeli - siparişi yapılmamış - olanları aktarılır.

![](../../../../../_assets/409b36533321df74d240.png)

**İşlem**

![](../../../../../_assets/28a5b6fae34946f5fb8c.png)

Talep/Teklif Devir ekranı İşlem sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Talep/Teklif Devir Ekranı |  |
| --- | --- |
| Devir Şirketi | Yeni yılda kullanılacak şirket isminin girildiği alandır. Girilen şirketin önceden açılmaması gerekir. Girilen şirket program tarafından açılır. "Yeni Yıl Kopyalama" işlemi aynı yeni yıl şirketinin ismi kullanılarak birden fazla tekrarlanıyorsa, "Yeni Yıl Kopyalama" işlemi öncesinde devir şirketinin "Şirket Silme işlemiyle silinmesi gerekir. |
| Devir Baz Tarihi | Talep/Teklif devri için baz alınacak tarihin girildiği alandır. Devir baz tarihi olarak verilecek tarihten önceki talep ve tekliflerden - talep/teklif kayıt tarihi baz alınır - sadece teslimatı tamamlanmayan ve bu tarihten sonraki tüm talep/ teklif kayıtları yeni sene şirketine aktarılır. Talep/Teklif modülü kullanılmayan durumlarda, bu bölümde herhangi bir şey yapılmasına gerek yoktur. |
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
