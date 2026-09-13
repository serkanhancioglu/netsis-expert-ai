---
title: "Zamanlanmış Görevler"
page_id: "50661395"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Giriş"
  - "Ana Menü"
  - "Çalışma Alanı"
  - "Eklentiler"
  - "Zamanlanmış Görevler"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Giriş / Ana Menü / Çalışma Alanı / Eklentiler / Zamanlanmış Görevler"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTk4YmIxMmVlLTBlYjAtNGU5Zi05ZDM0LTkzYzRiMGVkNGIzYSZsaW5rPTRlMjhhOTk3LTBmMmEtNDlkNS04YTY4LWZiNWU5ZWNjM2FjZCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=98bb12ee-0eb0-4e9f-9d34-93c4b0ed4b3a&link=4e28a997-0f2a-49d5-8a68-fb5e9ecc3acd&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "zamanlanmis-gorevler_50661397_50661395.html"
source_version: "2022-10-21T13:36:36.973+03:00"
source_bytes: 16275
fetched_at: "2026-09-13T04:01:22+00:00"
generator: "netsis-scraper 1.0.0"
---
# Zamanlanmış Görevler

Zamanlanmış Görevler eklentisi ile 7x24 planlanan zamanlanmış görevlerin sunucu tarafında arka planda çalışması sağlanır. Böylece, mesai saatleri dışında veya bilgisayar başında olunmadığı durumlarda da arka planda planlanan görevlerin gerçekleştirilmesi sağlanır. Zamanlanmış Görevler uygulaması ile çalıştırılacak görevler SSO kurulumunun bulunduğu sunucu üzerinde çalışır. Bu yüzden, bilgisayar kapalı olsa bile planlanan görevler arka planda çalışmaya devam eder.

Eklentiyi kullanıcıların eklemesi için SSO üzerinde Netsis Widget Modülü altında Zamanlanmış Görevler programı için yetki verilmesi gerekir. Admin kullanıcı eklentiyi her türlü kullanırken, diğer kullanıcılara yetki verilmesi zorunludur.

Eklenti ekrana getirildiğinde, Zamanlanmış Görevler eklentisinde öncelikli olarak daha önceden tanımlanan görevlerin durumu ve tanımları ile ilgili detay bilgiler grid ekran üzerinde listelenir. Durum, İlgili Görevin Açıklama Bilgisi, Şube Kodu, Sonraki Çalışma Zamanı, Son Çalışma Zamanı, Çalışma Süresi, Kullanıcı Adı (Görevin kim tarafından tanımlandığı), Aktif, Yineleme Sıklığı gibi bilgiler görüntülenir. Herhangi bir görev üzerinde güncelleme işlemi yapmak için, ilgili göreve çift tıklayarak, açılan ekran üzerinden gerekli güncellemeler yapılabilir. Yeni bir zamanlanmış görev tanımlamak için ekranın alt bölümünde yer alan artı ![(plus)](../../../../../_assets/8bc1079dc378a6219e99.svg) butonu kullanılır. Tıklandığında Zamanlanmış Görev ekranı görüntülenir.

Zamanlanmış Görev tanımındaki görev tipleri şunlardır; Script, Ön Tanımlı İşlem, Uygulama Çalıştır, Rapor Çalıştır ve Rest.

**Script** seçeneği ile; dinamik kodlamada olduğu gibi Script dili kullanılarak yazılacak Script'lerin planlanan zamanlarda çalışması sağlanır.

**Örneğin;** Script işleminin tanımlanması istendiğinde, Netsiscore nesnesine ulaşılıp sorgu yazılabilir.

**Ön Tanımlı İşlem** seçeneği ile; Ön Tanımlı İşlem seçenek kutusunda listelenen, program üzerindeki belli işlemlerin seçimi yapılarak, planlanan zamanlarda çalışması sağlanır. Herhangi bir işlem seçildiğinde, bu işlem ile ilgili parametreler alt bölümde listelenir. İlgili parametreler seçildikten sonra görev tanımı gerçekleştirilir.

**Örneğin;** Ön Tanımlı işlemin tanımlanması istendiğinde "Açıklama" alanına "Stok Hareketleri Kontrol" işleminin tanımlanacağı varsayıldığında, Ön Tanımlı İşlem seçenek kutusunda "Stok Hareket Kontrol" seçilir. Ekrana stok hareketi ile ilgili parametreler gelir. Parametreler tanımlanarak devam edilir. Yineleme Sıklığı alanı tanımlandıktan sonra Bitiş Tarihi alanının da tanımlanması zorunludur. Görev tanımlandığında nasıl bir bilgilendirme yapılacağı "Bilgilendirme Yöntemi" alanından girilir. Bilgilendirme Yöntemi; Bildirim Mesajı, e-Posta ve SMS seçeneklerinden oluşur.

Zamanlanmış Görev Tanımı ekranında "Bilgilendirme Yöntemi" seçeneği ile çoklu seçim yapılabilir. Böylece, "Zamanlanmış Görev" sonucunda, bildirim yöntemleri birden fazla seçilir. Bildirim gönderilecek kullanıcılar, "Kullanıcılar" alanında yer alan rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile seçilir. Gönderilecek birimin başlığı "Mesaj Başlığı" alanından tanımlanır. Mesaj İçeriği alanına, gönderilecek mesajın içeriği girilerek Tamam ![](../../../../../_assets/39d77b8716226638d9ce.jpg) butonu tıklandığında ilgili görev tanımlaması gerçekleşir.

Görev tanımı bittiğinde "Zamanlanmış Görevler" ekranında ilgili görev "Çalışıyor" durumuna gelir.

İleri Üretim Planlama İşlemi seçildiğinde; "Çizelgeleme Başlangıç Tarihi" ve "Çizelgeleme Başlangıç Saati" alanları yer alır. "Çizelgeleme Başlangıç Tarihi" ve "Çizelgeleme Başlangıç Saati" şeklinde iki ayrı alan bulunur. "Dinamik Tarih Aralığı" seçildiğinde "Çizelgeleme Başlangıç Tarihi" pasif olur fakat "Çizelgeleme Başlangıç Saati" aktif halde kalır.

**Uygulama Çalıştır** seçeneği ile; ilgili uygulama yolu sunucu üzerindeki exe veya bat uzantılı dosyanın sunucu üzerindeki yolunun "Uygulama Yolu" alanına girilmesi gerekir. Bu uygulamaya parametre eklenmesi istendiğinde "Parametreler" alanı tanımlanır. Zaman Aşımı alanında da ilgili uygulamanın en fazla ne kadar çalışması gerektiği bilgisinin dakika cinsinden tanımlanması gerekir. Bu süre aşıldığında, ilgili uygulama otomatik olarak sonlandırılır.

**Rapor Çalıştır** seçeneği ile; modül ve program seçimi yapıldıktan sonra "Taslak No" rehberinden daha önce kaydedilen bir taslak seçilerek, ilgili görev tanımlanıp, istenen zamanlarda otomatik olarak çalışması sağlanır.

**Rest** seçeneği ile; Rest tipinde zamanlanmış görev tanımlaması yapılması sağlanır. Web Metodu, URL ve Kimlik Doğrulama bilgileri tanımlanır. "Kimlik Doğrulama" alanından "Yok" seçeneği seçildiğinde herhangi bir Token bilgisi vermeden ilerlenebilir. Temel Seçeneği seçildiğinde, Kullanıcı Adı ve Şifre bilgilerinin girilmesi gerekir. Token seçeneği seçildiğinde Token bölümü aktif hale gelir ve Token bilgisi girilir. Netsis - Rest seçeneği seçildiğinde Netsis tarafında desteklenen rest sunucusu üzerinde, oradaki metotları kullanacak şekilde işlem yapılması sağlanır. Kullanıcı Adı ve Şifre bilgileri girilerek otomatik şekilde Token alınması sağlanır. Header ve Body alanlarından, gönderilecek istek yazılarak zamanlanmış görev tanımlaması yapılır.

Herhangi bir görevin geçmişini göstermek için "Geçmişi Göster" butonu kullanılır. Böylece, ilgili görevin en son ne zaman çalıştırıldığı, sonucunun ne olduğu ve çalışma süresinin ne olduğu gibi bilgiler bu bölümden görüntülenir.

"Zaman Çizelgesi" butonuna tıklayarak, ilgili görevin önümüzdeki dönemlerde ne zaman çalıştırılacağı izlenir.

Görevi silmek için ilgili görevin üzerine tıklayarak "Sil" butonu ile silinir.

Görevin kopyalanması için, "Kopyala" butonu kullanılır. İlgili görevin tanımı ile bilgilerin otomatik olarak yeni bir tanım ekranına kopyalanması sağlanır.

Herhangi bir görevin çalışma zamanını beklemeden çalıştırılması istendiğinde, "Şimdi Çalıştır" butonu kullanılır.

Ekranın alt bölümünde yer alan butonların her biri, ekran üzerinde iken farenin sağ tuşu ile seçenek şeklinde de görüntülenebilir.

**Örneğin;** "Malzeme Gereksinim Planlama" ekranına girildiğinde, ilgili parametreler seçildikten sonra "Rapor" butonunun yanında bulunan aşağı ok butonu ile ekrana gelen seçenekler arasından "Zamanlanmış Göreve Ekle" seçeneği ile, seçilen parametreler otomatik olarak zamanlanmış görev ekranına gelir. Malzeme Gereksinim Planlama ön tanımlı işlemde "Dinamik Tarih Aralığı" seçeneği aktif hale gelir. Bu seçenek işaretlendiğinde parametrelerdeki tarih ile ilgili bilgiler pasif hala gelir. Böylece, zamanlanmış görevin çalıştığı tarihe uygun olarak başlangıç ve bitiş tarihlerini dinamik olarak ayarlanması sağlanır.

Öncül Görev alanı ise, daha önceden tanımlanmış görevlerin izlenmesini sağlar.

Zamanlanmış Görevlerin yürütüldüğü Netsis.Notification.WinService ilk çalıştığı anda Netsis Yeni Sürüm ve Netsis ERP Youtube kanalında bulunan ürün videoları için otomatik sistem görevleri oluşturulabilir. Servis ilk çalıştığında her gün saat 10:00'da çalışması için görevler oluşturur ve kullanıcılara yeni sürüm ve yeni video içerikleri ile ilgili bilgilendirme maili gönderir. Kullanıcının, bu tipteki bildirim mesajlarını görmesi istenmiyorsa (“SYSTEMTASK”,”NOSHOW”) özel parametresinin kullanılması gerekir.
