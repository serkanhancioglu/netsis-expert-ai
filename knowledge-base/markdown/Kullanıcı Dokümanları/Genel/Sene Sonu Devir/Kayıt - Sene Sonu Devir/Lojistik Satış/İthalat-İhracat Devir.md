---
title: "İthalat/İhracat Devir"
page_id: "24753437"
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
  - "İthalat/İhracat Devir"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Sene Sonu Devir / Kayıt / Sene Sonu Devir / Lojistik Satış / İthalat/İhracat Devir"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTUwMWMyZGRmLWZiZmYtNDg0MS04NDU5LTVlMDQ3OTA4MTI1OCZsaW5rPWMxODI5NWI0LWY2ZDgtNGI2ZS04M2Q0LTA3MmVjZjc0OGQ3OSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=501c2ddf-fbff-4841-8459-5e0479081258&link=c18295b4-f6d8-4b6e-83d4-072ecf748d79&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ithalat-ihracat-devir_47073577_24753437.html"
source_version: "2022-10-19T13:57:56.693+03:00"
source_bytes: 74928
fetched_at: "2026-09-13T04:18:08+00:00"
generator: "netsis-scraper 1.0.0"
---
# İthalat/İhracat Devir

İthalat/İhracat Devir, Genel Bölümü'nde, "Kayıt/Sene Sonu Devir" menüsünün altında yer alır. "İthalat/İhracat Devir" işleminin, tüm versiyonlarda her işletme ve şube için ayrı ayrı çalıştırılması gerekir. İthalat/İhracat Devir, ithalat ve ihracat uygulaması olan firmaların, henüz kapatılmamış kayıtlarının devir şirketine aktarılması için kullanılan bölümdür. İthalat/İhracat Devir işlemi ile ithalat kapatması henüz tamamlanmayan ithalat irsaliyeleri - "Miktar" alanları boş, "Export Miktarı" alanları dolu olan hareketler - devir şirketindeki stok hareket kayıtlarına aktarılır. Dekont → Kayıt → "Genel Dekont Kaydı" bölümünden IT ve IH seri numarasıyla kaydedilen tüm dekontlar devir şirketine aktarılır. Fatura modülünde bulunan “İhracat/ İthalat miktarları stoklara geçsin” parametresi işaretli ise tüm ithalat/ihracat kayıtlarının eski yılda kapatılması gerekir. İhracat/ İthalat miktarları stoklara geçsin parametresini kullanan firmaların, stok devirlerini yapmadan önce gerekirse yeni yılda oluşacak masraflar için de karşılık ayırarak, eski sene şirketinde tüm ithalat/ihracat kapatmalarını yapması gerekir.

İthalat/İhracat Devir ekranı; Giriş, İşlem ve İşlem Sonucu sekmesinden oluşur.

**Giriş**

![](../../../../../_assets/a71cb447d5ffb1be3c2f.png)

**İşlem**

**![](../../../../../_assets/72cf3c93bce45f746e95.png)**

İthalat/İhracat Devir ekranı İşlem sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| İthalat/İhracat Devir Ekranı |  |
| --- | --- |
| Devir Şirketi | Yeni yılda kullanılacak şirket isminin girildiği alandır. Girilen şirketin önceden açılmaması gerekir. Girilen şirket program tarafından açılır. "Yeni Yıl Kopyalama" işlemi aynı yeni yıl şirketinin ismi kullanılarak birden fazla tekrarlanıyorsa, "Yeni Yıl Kopyalama" işlemi öncesinde devir şirketinin "Şirket Silme işlemiyle silinmesi gerekir. |
| Kapatılmış Kayıtlar Devredilmesin | Kapatması yapılan ithalat\\ihracat dekontlarının yeni sene şirketine devredilmemesi için kullanılan seçenektir. |
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
