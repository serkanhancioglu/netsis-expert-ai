---
title: "TUİK-Netsis ERP Paketi Entegrasyonu ve Yıllık İş İstatistikleri Sanayi ve Hizmet Araştırması (YSHİ) Anketi"
page_id: "50679904"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "TUİK-Netsis ERP Paketi Entegrasyonu ve Yıllık İş İstatistikleri Sanayi ve Hizmet Araştırması (YSHİ) Anketi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / TUİK-Netsis ERP Paketi Entegrasyonu ve Yıllık İş İstatistikleri Sanayi ve Hizmet Araştırması (YSHİ) Anketi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTVmMzQ2NWYzLTY2ZjktNDhkZi05YzUwLTk0OTRlYjAxZTM1NCZsaW5rPTNkYjA1MzA4LTIxNzQtNGM1Yi1hNzIwLWE1NzQ4NThkYjU2NCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=5f3465f3-66f9-48df-9c50-9494eb01e354&link=3db05308-2174-4c5b-a720-a574858db564&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "tuik-netsis-erp-paketi-entegrasyonu-ve-yillik-is-istatistikleri-sanayi-ve-hizmet-arastirmasi-yshi-anketi_82576032_50679904.html"
source_version: "2022-11-03T09:27:33.797+03:00"
source_bytes: 1172277
fetched_at: "2026-09-13T04:25:54+00:00"
generator: "netsis-scraper 1.0.0"
---
# TUİK-Netsis ERP Paketi Entegrasyonu ve Yıllık İş İstatistikleri Sanayi ve Hizmet Araştırması (YSHİ) Anketi

TUİK-Netsis ERP Paketi Entegrasyonu ve Yıllık İş İstatistikleri Sanayi ve Hizmet Araştırması (YSHİ) Anketi ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

#### Uygulamanın Amacı

Uygulama amacı, Netsis Erp paketi ile bağlantı kurarak Türkiye İstatistik kurumu (TUİK) Yıllık İş İstatistikleri Sanayi ve Hizmet Araştırması (YSHİ) uygulamasını oluşturmak ve Elektronik veri transferi (e-vt) yöntemi ile TUİK'e anket formonun aktarılmasıdır. Uygulama Netsis Erp paketi ile bağlantı kurmak için Netopenx50.dll kullanarak iletişim sağlar. Uygulama içerisinde belli kontroller olduğu gibi, xml paket oluşturma aşamasında TUİK tarafından hazırlanan "tuik_evt_yshi.sch" dosyasını kullanarak, şematron kontrolü yapar ve hata sonuçlarını result.xml dosyası ile son kullanıcıya belirtir. Hata alınmayan veri şeması ve tutarlılığı düzgün dosyalar için belge tamamlandı uyarısı verilir ve TUİK, e-vt sistemine aktarıma hazır hale gelir.

#### Kurulum

Uygulama 8.0.6 seti ile birlikte Temelset dizini altında TUIK klasöründe bulunmaktadır. Çalıştırılmadan önce güncel dbupdate cümleleri edinilmelidir. NETSIS TUIK E- VT ENTEGRASYONU.xlsm çalıştırılarak uygulama başlatılır.

#### Netsis Entegrasyonu ile Veri Getirme ve Soru Formu Doldurma Şekli

Uygulama Netsis Erp paketi üçüncü parti iletişim dosyası olan "Netopenx50.dll" kullanarak iletişim sağlar. Uygulamaya Netsis kurulumu ile birlikte servis edilecek olan "Yıllık Sanayi ve Hizmet İstatistikleri_FV1.00" excel dosyası ile giriş yapılmaktadır. Uygulamanın kullandığı DbUpdate cümleleri kurulum adımında güncel Dbupdate dosyalarından edinilebilir. "Netsis'den Veri Getir" butonuna basıldığı anda uygulama ilk olarak Netsis bağlantı bilgileri arayacaktır ve Netsis bağlantı ekranına benzer bir login ekranı çıkacaktır.

Netsis bağlantı bilgilerinin doğru olarak tanımlanmasının ardından, proje içerisinde verilecek olan kısıtlara göre veri getirilecektir.

#### Kısıt Sahaları ve Kullanımları

Temel olarak üç tip kısıt sahasına ve bir adet veri giriş sahası bulunmaktadır.

**Sarı Alanlar:** Veri giriş sahalarıdır. Netsis tarafından getirilen veriler ile birlikte otomatik olarak dolacaktır. Erp paketi üzerinden alınamayan ve ya bulunamayan veriler için kullanıcılar elle müdahele edebilecektir.

**Yeşil Alanlar:** Kısıt verilerek kullanılan viewdan veri getirecek olan sahalardır. Ör; 150% gibi bir kısıt verildiği zaman, tüm "150" ile başlayan hesapların tutarları getirilecektir.

**Kırmızı Alanlar:** Hariç hesap sahasıdır. Ör; "150-01-001" gibi bir kısıt verildiği zaman, yeşil alanda tanımlanmış olan tüm 150 hesapların tutarları getirilecek fakat kırmızı alanda "150- 01-001" kısıt verildiği için sadece bu hesabın tutarı diğer 150 hesaplardan düşürülerek getirilecektir.

**Mavi Alanlar:** Bir önceki sahalarda verilen kısıtların yeterli olmaması durumunda, SQL yazılarak kısıt verilebilecek olan ileri kısıt sahasıdır. Burada SQL cümle yapısının "WHERE" bloğundan sonra yazılması gerken kısıtlar direk olarak yazılmalıdır. "WHERE" kelimesi YAZILMAMALIDIR! Ör; "BA\<\>2" gibi bir kısıt verilirse, daha önce verdiğimiz kısıtlara ek olarak sadece borç tipli hareketlerin tutarlarının getirilmesi sağlanacaktır.

Uygulama Notları aşağıdaki şekildedir:

- Uygulamadan ile veri alışverişi, TBLMUHFIS tablosundaki veri sahalarına göre yapılmaktadır. İleri kısıt sahası kullanılırken bu tablodaki ilgili alanlara göre sorgulama yapılmalıdır.

- Tüm kısıt sahalarını kullanırken, (Yeşil, kırmızı ve mavi) sql syntax ı kullanılmaktadır. Ör; tüm 15 ile başlayan hesalpları getirmek için "15%", tüm "150-01" grubunu çağırmak için "150-01%" gibi kısıtlar kullanılabilir.
- Bir alana birden fazla kısıt tanımlanması için noktalı virgül (![(wink)](../_assets/e46673a5e6cd21ed1531.svg) karakteri ile hesaplar birbirinden ayrılmalıdır. Ör; Dahil hesap olarak sadece "150-01-001" ve "150-01-002" hesapları getirilmek isteniliyorsa yeşil alana "150-01-001; 150-01-002" olarak yazılmalıdır. Grup ve ana hesaplar için de aynı kondisyonlar geçerlidir.

#### Ek Belge Girişleri

Uygulama içerisinde istenen bazı ek bilgiler için excel üzerinde ek veri giriş sayfaları oluşturulmuştur. Uygulamanın ilgili yerlerinde bu sayfalara geçiş için buton bulunmakta ve tekrar soru formu üzerinde geri dönmek için gidilen sayfada "Ankete Dön" butonu bulunmaktadır.

![](../_assets/57b03c478338b801f482.png)![](../_assets/1c16fab4053c8532905c.png)

#### Belge Kontrolü ve Veri Tutarlılığı

Belge üzerinde veri girişinin tamamlanmasının ardından belgenin sonunda bulununan XML paket oluştur düğmesine tıklanarak TUİK e-vt sistemine iletilmek üzere ilgili XML dosyası hazırlanmaktadır. Burada oluşturulan xml dosyası TUİK tarafından hazırlanan "tuik_evt_yshi.xsd" şema dosyası ve "tuik_evt_yshi.sch" şematron dosyası kontrollerinden geçmektedir. Kontrol sonucunda uygulama üzerinde uyarı verileceği gibi, hata oluşması durumunda kullanıcı tekrar uyarılarak "Result.xml" dosyası ile kullanıcılar yaptıkları hatalar ile alakalı uyarılacaktır.

Yukarıdaki örnekte olduğu üzere; "failed-assert" olarak gösterilen bold alanlarda hatalı ve tutarsız veri giriş örnekleri görülebilmektedir. Bu dosyaya istinaden ilgili sahalar tekrar düzenlenmeli ve tekrar XML dosyası, hatalar tükenene dek, oluşturulmalıdır. Aksi halde TUİK e-vt sistemi tarafından uyarı alınacaktır.

#### Belge Gönderimi

TUİK e-vt uygulamasına [{+}](https://harzemli.tuik.gov.tr/ed/EdUygulamaDis/zul/giris.zul?lang=tr)[https://harzemli.tuik.gov.tr/ed/EdUygulamaDis/zul/giris.zul?lang=tr+](https://harzemli.tuik.gov.tr/ed/EdUygulamaDis/zul/giris.zul?lang=tr+) linkinden ulaşılabilir. Uygulama kullanımı ile alakalı daha detaylı bilgi için lütfen aşağıdaki linklerde gösterilmiş olan ve TUİK tarafından hazırlanan dokümanları, dikkatle inceleyiniz.

![](../_assets/8ac31f83661a2cfeab17.png)

Uygulamaya TUİK tarafından verilen kullanıcı no ve parola ile giriş yaptıktan sonra; "İşyerleri Evt İşlemleri Yazılım Entegrasyonu" adımı üzerinden ilgili sayfaya yönleniniz.

Burada aşamada gelen sayfada XML yükleme tabını seçerek "Dolu Anket Dosyası Yükleme" butonu yardımı ile, Netsis ERP paketi tarafından hazırlanan XML dosyasını TUİK web sitesine yükleyiniz. Yükleme aşaması da tamamlandıktan sonra ilgili kullanıcıya TUİK tarafından anket sonucunun geçerliliği ve doğruluğu ile alakalı bir bilgilendirme maili gönderilecektir. Dokümanın önceki aşamalarında da belirtildiği üzere TUİK e-vt uygulamasının kullanımı, detaylı işlem adımları ve izlenmesi gereken işlem adımları için TUİK web sitesi ve ilgili dokümanları dikkatle incelenmesini önemle önermekteyiz.

![](../_assets/d90a2d539ceafb3e654d.png)
