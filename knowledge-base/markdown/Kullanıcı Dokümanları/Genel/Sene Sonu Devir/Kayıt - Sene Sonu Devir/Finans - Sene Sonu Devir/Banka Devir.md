---
title: "Banka Devir"
page_id: "24753458"
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
  - "Banka Devir"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Sene Sonu Devir / Kayıt / Sene Sonu Devir / Finans / Sene Sonu Devir / Banka Devir"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTQzZmEyYmFmLTRjNGUtNGUwMy1iZDNlLThlMDQ5Nzc1OTIyNyZsaW5rPWY3NmMyY2U2LThmZDktNGM0ZC05YWU4LWU2ZmI2OWYxMDE2MyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=43fa2baf-4c4e-4e03-bd3e-8e0497759227&link=f76c2ce6-8fd9-4c4d-9ae8-e6fb69f10163&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "banka-devir_47073717_24753458.html"
source_version: "2022-10-20T09:28:55.267+03:00"
source_bytes: 115143
fetched_at: "2026-09-13T04:18:12+00:00"
generator: "netsis-scraper 1.0.0"
---
# Banka Devir

Banka Devir, Genel Bölümü'nde, "Kayıt/Sene Sonu Devir" menüsünün altında yer alır. Banka modülü devri **Enterprise** ürünü ile merkez işletmede, **Standard** ve **Entegre** ürünleri ile - şubeli uygulama varsa - merkez şubeden yapılması gerekir. Banka Devir, banka hesaplarının devir işlemlerinin yapılması için kullanılan bölümdür. Banka Devir işleminden önce "Banka Hesap Sabit Bilgilerinin" yeni sene şirketine "Yeni Yıl Kopyalama" bölümünden önceden aktarılması gerekir. Burada sabit kayıtlara bağlı hareketlerin devri yapılarak, sonuç devir hareketi yeni sene şirketindeki hareketlere işlenir. Devir işlemine başlamadan önce; tüm banka hesapları için döviz farkları kapatma işleminin - Vadesiz ve Rotatif hesaplar için - faiz kapatma işleminin önceden çalıştırılması gerekir.

Program kapatma işlemi ile ilgili uyarıyı aşağıdaki şekilde ekrana getirir:

![](../../../../../_assets/bf72d335bd03e421f85d.png)

Banka → İşlemler → Döviz Farklarını Kapatma ve Faiz Kapatma işlemleri çalıştırılmışsa “Evet”, değilse devir işleminden çıkmak için “Hayır” butonuna tıklanması gerekir.

Banka hesapları devrinde, Vadeli, Spot, Taksitli Kredi, Uzun/Orta Vadeli Kredi ve Repo hesap hareketleri için, hesabın bakiye verip vermediğine bakılır. Eğer hesabın bakiyesi varsa, son hesap açma işleminde girilen tutar devir baz tarihine bakılmadan yeni sene şirketine devredilir.

Rotatif, Vadesiz ve Kredi Kartı hesaplarının devirleri vade tarihine göre yapılır. Vade tarihi devir tarihinden büyük olan kayıtlar yeni yıl şirketine aynen aktarılır.

Bunun dışındaki tüm hesap hareketleri, "Cari Tarih Aralıklı Devir" mantığına göre yeni sene şirketine aktarılır Yani, belirlenen devir baz tarihine kadar olan hareketlerin sadece bakiyesi devredilir ve bu tarihten sonraki hareketler aynen yeni sene şirketine aktarılır.

Banka Devir ekranı; Giriş, İşlem ve İşlem Sonucu olmak üzere üç sekmeden oluşur.

**Giriş**

**![](../../../../../_assets/88f65cd623c11c1d3139.png)**

**İşlem**

![](../../../../../_assets/47b1bcaed26841f52a32.png)

Banka Devri ekranı İşlem sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Banka Devri Ekranı |  |
| --- | --- |
| Devir Şirketi | Yeni yılda kullanılacak şirket isminin girildiği alandır. Girilen şirketin önceden açılmaması gerekir. Girilen şirket program tarafından açılır. "Yeni Yıl Kopyalama" işlemi aynı yeni yıl şirketinin ismi kullanılarak birden fazla tekrarlanıyorsa, "Yeni Yıl Kopyalama" işlemi öncesinde devir şirketinin "Şirket Silme işlemiyle silinmesi gerekir. |
| Devir Baz Tarihi | "Cari Tarih Aralıklı Devir" mantığına göre devredilecek banka hesaplarına, aktarılacak hareket devirleri için sınır tarihi belirlenen alandır. |
| Devir Tarihi | Devir hareketlerinin yeni sene şirketine işleneceği kayıt tarihinin girildiği alandır. Büyük çoğunlukla yeni yılın ilk günü girilir. |
| Döviz Tarihi | Banka hareketlerinde dövizli kayıt bulunan firmaların sene sonu devirlerinde kullanılacak kur tarihinin girildiği alandır. Dövizli banka hesapları devredilirken, program döviz tiplerine göre ayrı ayrı devir alır ve döviz bazında bakiyeleri ayrı ayrı yeni sene devri olarak oluşturur. Döviz bazında yapılan bu devir hareketlerinin TL tutarları ise, her döviz tipi için burada girilen tarihin kurundan tekrar hesaplanır. Eski sene şirketinde, devir yapılan tarih itibariyle kur farkı kapatma işlemi yapılmadıysa, yeniden hesaplama sonucu bakiye - eski sene şirketiyle yeni sene şirketi arasında fark - verebilir. Bu nedenle devir programı, banka devir seçeneğine giriş sırasında kur farkı kapatma yapılması gerektiğine dair uyarı verir. |
| Banka Hesap Kodu Aralığı | Belirli bir aralıktaki banka hesaplarına ait hareketlerin yeni yıl şirketine aktarılması için kullanılan alandır. Sadece devredilmesi istenen banka hesap kodları için kısıt verilebilir. Buraya girilen banka hesap kodları için daha önce devir yapılmışsa, önceki devirde oluşturulan hareketler silinerek tekrar oluşturulur. |
| Proje Kırılımlı Devir | Devrin, proje kırılımlı yapılması için kullanılan seçenektir. İşaretlenmediği zaman, alanın sağ tarafında yer alan rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, proje kodları arasından seçim yapılır. İşaretlendiğinde, rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg)pasif olarak görünür. |
| Eski Kayıtlara Devir Tarihi Atılsın | Banka devri yapılırken eski kayıtlara devir tarihinin atılması için kullanılan seçenektir. |
| Devir Sonunda Kur Farkı Kapatma Yapılsın | Banka devri sonrasında kur farkı kapatmalarının yapılması için kullanılan seçenektir. |
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
