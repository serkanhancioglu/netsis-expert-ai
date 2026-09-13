---
title: "Serisiz Stok Devir"
page_id: "24753431"
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
  - "Serisiz Stok Devir"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Sene Sonu Devir / Kayıt / Sene Sonu Devir / Lojistik Satış / Serisiz Stok Devir"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTE1OWI0NzI3LTRjZWMtNDdmMi1hN2IwLWQ1MWNjMmIxNDA3YiZsaW5rPTlmMjAyZTRhLWFkNTMtNDVmZC1hZmNhLTY1NDVhYmFlY2E0YSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=159b4727-4cec-47f2-a7b0-d51cc2b1407b&link=9f202e4a-ad53-45fd-afca-6545abaeca4a&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "serisiz-stok-devir_47073486_24753431.html"
source_version: "2022-10-19T13:52:12.253+03:00"
source_bytes: 133519
fetched_at: "2026-09-13T04:18:06+00:00"
generator: "netsis-scraper 1.0.0"
---
# Serisiz Stok Devir

Serisiz Stok Devir, Genel Bölümü'nde, "Kayıt/Sene Sonu Devir" menüsünün altında yer alır. Serisiz Stok Devir, eski yöntemle stok devri, serisiz stok devri ile adlandırılarak, seri uygulaması kullanmayan firmalar tarafından uygulanır. Stok kartlarında hem girişte hem de çıkışta "Seri Uygulaması" işaretlenen stokların devri, "[Serili Stok Devri](<Serili Stok Devri.md>)" bölümünden yapılır. Sadece çıkışta ya da girişte seri takibi yapılıyorsa, "Serisiz Stok Devri" adımından devrin yapılması gerekir fakat seri bilgileri aktarılmaz. "Serisiz Stok Devir" işleminin, tüm versiyonlarda her isletme ve şube İçin ayrı ayrı çalıştırılması gerekir. Serisiz Stok Devir ekranı; Giriş, İşlem ve İşlem Sonucu Sekmesinden oluşur.

**Giriş**

**![](../../../../../_assets/5b95e2ae5a480d97f2ce.png)**

**İşlem**

Sabit işlemlere bağlı hareketlerin devri yapılarak, sonuç devir hareketi/hareketleri yeni sene şirketindeki stok hareketlerine işlenir. Sipariş ve talep/teklif takibi kullanılıyorsa ve sipariş ile talep/teklif devirleri henüz yapılmamışsa, stok devrini yapmadan önce sipariş ve talep/teklif kayıtlarının devredilmesi gerekir. Esnek Yapılandırma Uygulamasının kullanıldığı firmalarda, stok hareketleri yapılandırma kodu bazında kırılımlı olarak program tarafından oluşturulur.

Lokal Depo Uygulamasının kullanıldığı firmalarda, lokal depolara göre devir işlemi, stok devri sırasında program tarafından yapılacağı için, lokal depolardaki tüm çalışmaların önceden tamamlanması gerekir.

![](../../../../../_assets/bbcd5b01861924ba5f7d.png)

Serisiz Stok Devir ekranı İşlem sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Serisiz Stok Devri Ekranı | Genel Parametreler |
| --- | --- |
| Devir Şirketi | Yeni yılda kullanılacak şirket isminin girildiği alandır. Girilen şirketin önceden açılmaması gerekir. Girilen şirket program tarafından açılır. "Yeni Yıl Kopyalama" işlemi aynı yeni yıl şirketinin ismi kullanılarak birden fazla tekrarlanıyorsa, "Yeni Yıl Kopyalama" işlemi öncesinde devir şirketinin "Şirket Silme işlemiyle silinmesi gerekir. |
| Devir Baz Tarihi | Stok devri için baz alınacak tarihin girildiği alandır. Yılın son günü otomatik olarak gelir. Devir baz tarihinden önceki stok hareketleri, seçilen maliyet türüne göre devredilir. Bu tarihten sonraki hareketler aynen yeni şirkete aktarılır. |
| Devir Tarihi | Yeni şirkete aktarılacak stok devirleri için kullanılması istenen tarihin girildiği alandır. |
| Maliyet Türü | FIFO (ilk giren ilk çıkar), LIFO (son giren ilk çıkar), Ağırlıklı Ortalama, Hareketli Ortalama, Aylık Ağırlıklı Ortalama, Maliyet Muhasebesi Fiyatı ve Alış Fiyatı maliyet türlerinden oluşan alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile maliyet türleri arasından seçim yapılarak kısıt verilir. Maliyet Muhasebesi kullanan firmaların maliyet türü olarak "Maliyet Muhasebesi Fiyatını" seçmeleri gerekir. Böyle bir durumda stok devrinde, stok kartlarındaki maliyet fiyatları baz alınır. |
| İthalat/İhracat Hareketleri Aktarılmasın | "Fatura" modülünde bulunan “İhracat/İthalat miktarları stoklara geçsin” parametresinin kullanıldığı durumlarda, kapatılmayan ithalat/ihracat kayıtlarının da yeni sene şirketine aktarılması İçin kullanılan seçenektir. İhracat/İthalat Uygulamaları olan firmalar için "İhracat/İthalat Devri" işleminin ayrıca çalıştırılması gerekir. “İhracat/İthalat miktarları stoklara geçsin” parametresi kullanılmıyorsa, bu seçenek işaretlenmeden sadece "İhracat/İthalat Devri" işlemi çalıştırılır. |
| Dinamik Depo İçin Devir Yapılsın | "Dinamik Depo" modülü kullanan firmalarda merkez işletme ya da şubede işaretli olarak gelir ve değiştirilemez. Devir için verilen tarih itibari ile hücre bakiyeleri, yeni seneye devir olarak işlenir. |
| Eksi Bakiyeliler Devredilsin | Bakiyesi eksiye düşen stokların da yeni yıl şirketine aktarılması için kullanılan seçenektir. Kullanılmadığı zaman, eksi bakiyeli olan stokların devri yeni yıl şirketine aktarılmaz. |
| Devirden Sonra Stok Hareket Kontrol İşlemi Çalıştırılsın | Devir sonrası stok hareket kontrolünün çalıştırılması için kullanılan seçenektir. |
| Devirde Hücre Kodu Dikkate Alınsın | "Bakiye Verenler" seçeneği işaretlendiğinde aktif hale gelen alandır. "Dinamik Depo" modülünün kullanıldığı durumlarda, bakiye veren seri kayıtları aktarılırken, bakiye kontrolünün hem seri hem de seri kayıtlarında bulunan hücre koduna göre yapılması İçin kullanılan seçenektir. Bu seçeneğin işaretlenmesi halinde, "Seri" ve "Hücre Kodu" kırılımında aktarım gerçekleşir. |
| Devir Kayıtları Detaylandırılsın | "Maliyet Türü" alanında FIFO seçilmesi halinde sorgulanan seçenektir. Stok hareketlerinin FIFO’ya göre bulunan bakiyeler bazında detaylı oluşturulması için işaretlenmesi gerekir. İşaretlenmemesi halinde ise, FIFO’ya göre bulunan stok bakiyeleri, stok hareketlerine kümüle olarak aktarılır. |
| Dövizli Stok Devri İçin | Dövizli stok devri, FAS52, IAS29 veya Enflasyon Muhasebesi seçeneklerinden birinin kullanılması durumunda mutlaka gereklidir. Dövizli stok devri yapılması için öncelikle maliyet türü olarak "Aylık Ağırlıklı Ortalama", "FIFO", "LIFO" veya "Maliyet Muhasebesi Fiyatı" seçeneklerinden birinin işaretlenmesi gerekir. Bu durumda program, seçilen maliyet türüne göre her stokun dövizli birim maliyet fiyatını bularak, yeni yıl şirketinde döviz tutarına aktarır. Döviz tipi olarak "Genel Parametre Kayıtları" bölümündeki firma döviz tipi kullanılır. |
| Sabit Kayıt Kontrolü Yapılsın | Serisiz stok devri işleminde sabit kayıt kontrolünün yapılması için kullanılan seçenektir. |
| Proje Kırılımlı Devir | Devrin, proje kırılımlı yapılması için kullanılan seçenektir. İşaretlenmediği zaman, alanın sağ tarafında yer alan rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, proje kodları arasından seçim yapılır. İşaretlendiğinde, rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg)pasif olarak görünür. |
| Serisiz Stok Devri Ekranı | Stok Kısıtları **Stok Kısıtları sekmesi, devri yapılması istenen stoklarla ilgili kısıtlamaların yapıldığı sekmedir. Ekranda, stok sabit kayıtlarında girilen bilgiler listelenir. Stokların bölüm bölüm devrinin yapılmasını sağlamak için kullanılır.** |
| Saha Adı | "Stok Kısıtları" sekmesine tıklanması ile görüntülenir. Serisiz Stok işleminde baz alınacak saha adı için kısıt verilen alandır. İlgili hücre üzerinde iken klavyede yer alan **Boşluk Çubuğuna** basılarak aktif hale gelen aşağı ok butonu, kısıt verilmesi istenen sahalara ulaşılmasını sağlar. Satırın silinmesi için klavyedeki "Delete" tuşuna basılması gerekir. ![](../../../../../_assets/118817d565d3feaa2a58.png) |
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
