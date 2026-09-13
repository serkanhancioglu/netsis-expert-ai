---
title: "KDV Beyannamesi e-Beyan Entegrasyonu"
page_id: ""
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "KDV Beyannamesi e-Beyan Entegrasyonu"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / KDV Beyannamesi e-Beyan Entegrasyonu"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWY3OTk1NGI1LTA3MGYtNGViZS1hYTA1LWM5ZmQ2MjliY2JjMSZsaW5rPWE5N2NhN2Q4LTVlNzEtNGQzYy05NTA4LTc0ODE3MjdlOGM2YyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=f79954b5-070f-4ebe-aa05-c9fd629bcbc1&link=a97ca7d8-5e71-4d3c-9508-7481727e8c6c&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "kdv-beyannamesi-e-beyan-entegrasyonu.html"
source_version: ""
source_bytes: 8454
fetched_at: "2026-09-13T04:21:47+00:00"
generator: "netsis-scraper 1.0.0"
---
# KDV Beyannamesi e-Beyan Entegrasyonu

Gelir İdaresi Başkanlığı tarafından 2025 Ağustos ayı itibarıyla pilot bölge uygulamasıyla başlatılan ve 2026 yılı başından itibaren kapsamı genişletilen "Yeni e-Beyan Sistemi"ne geçiş süreci, vergi süreçlerinin dijitalleşmesi ve veri tutarlılığının artırılması amacını taşımaktadır.

Bu yasal düzenlemelere uyum çalışmaları kapsamında, **9.0.70.5** ve **9.0.71.2** sürümleri ile birlikte; sistem üzerinden düzenlenen KDV1 ve KDV2 beyannamelerinin **eLogo Portalı** aracılığıyla doğrudan yeni e-Beyan sistemine iletilmesi özelliği devreye alınmıştır. Bu entegrasyon, beyanname süreçlerini otomatize ederek operasyonel riskleri minimize etmeyi ve kullanıcı deneyimini iyileştirmeyi hedeflemektedir.

Söz konusu entegrasyonun sağlıklı çalışabilmesi için uygulama üzerinde yapılması gereken tanımlamalar ve sisteme eklenen yeni fonksiyonel alanlar aşağıda maddeler halinde sunulmuştur.

##### Mükellef ve Düzenleyen Bilgileri

eLogo ile entegrasyonu sağlayacak parametrelerin tanımlanabilmesi için Mükellef ve Düzenleyen Bİlgileri ekranına “Beyanname” sekmesi eklenmiştir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/d647ac9c-ad9b-4b0c-b7ac-a8ac3253bcf3/es_ebyn_mukduzenleyen.jpg)

**Mükellef Tipi :** Vergi mükelleflerinin türüne, gelir şekline ve hukuki yapısına göre beyanname gönderme süreçlerini belirleyen kategoridir.

**GIB Token :** Uygulamanın Gelir İdaresi Başkanlığı (GİB) sistemleriyle doğrudan ve güvenli bir şekilde iletişim kurmasını sağlayan, kullanıcıya özel dijital erişim anahtarı girilir.

**E-Logo Kullanıcı Adı :** eLogo portalına giriş yaparken seçilen firma kodu girilir.

**E-Logo Şifre :** eLogo portalına (efatura.elogo.com.tr) giriş yaparken seçilen firma koduna ait webservis şifresi girilir.

##### Beyanname Kayıtları

Yeni e-Beyan sistemiyle birlikte beyanname gönderim sürecinin uçtan uca dijitalleşmesi, ERP sisteminden gönderilen verilerin nihai beyan formatında olmasını gerektirmektedir. Bu yasal ve teknik zorunluluğu karşılamak adına, daha önce paketleme aşamasında manuel tamamlanan veya dış kaynaklı yönetilen alanlar, doğrudan Beyanname Kayıtları ekranına eklenmiştir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/5a592df9-4a11-40de-bb87-ec701d69b683/es_ebyn_beyannamekayitlari.jpg)

**GİB Durum**

Oluşturulan beyannamenin GIB Portalındaki statüsü GİB Durum sahası üzerinden takip edilir.

**Durum**

Oluşturulan beyannamenin uygulama içerisinde hangi süreçte olduğu Durum sahası üzerinden takip edilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/9467abe9-d9f4-4ae5-a6ec-03f32484b6c1/es_ebyn_gibdurumlari.jpg)

**Özel Onay**

**Özel Onay Seçim /Ceza İşlem Türü :**Gönderilen beyannamenin yasal süreci ve içeriğine bağlı olarak (Düzeltme, Pişmanlık, Kanuni Süresinden Sonra vb.) GİB tarafından talep edilen onay türünü ifade eder. ERP sistemi üzerinden beyanname gönderilirken, beyan türüne uygun özel onay kodu seçilerek iletim gerçekleştirilmelidir. Özel Onay Seçimi ile Cezai İşlem Türü arasında yapısal bir kural seti bulunmaktadır. Bu doğrultuda, Cezai İşlem Türü alanındaki seçenekler, Özel Onay Seçimi alanında yapılan tercihe bağlı olarak dinamik bir şekilde aktif veya pasif hale gelmektedir.

Ekran üzerindeki bazı sahalar, yapılan seçimlere göre dinamik olarak aktifleşmektedir: Gerekçe alanı yalnızca **'İhtirazi Kayıt'** seçildiğinde; Referans Numarası ve Tebliğ Tarihi sahaları **'İzah'** seçeneği tercih edildiğinde giriş yapılabilir hale gelir. Düzeltme Beyannamesi Açıklaması sahası ise **Düzeltme Beyannamesi** parametrenin işaretlenmesiyle birlikte kullanıma açılır.

##### Beyanname Görüntüleme

Beyanname Kayıtları ekranından Beyanname Görüntüleme butonuna basıldığına açılan ekrana Gönder, Onay,Tahakkuk, GIB’den Sil ve PDF butonları eklenmiştir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/273315d2-9caf-4883-9189-b6337d779e96/es_ebyn_genelbilgiler.jpg)

###### Beyanname Gönderim ve Onay Süreci

**• Gönder:** Beyanname parametreleri tanımlanıp kaydedildikten sonra Gönder butonu aktifleşir. Bu buton ile beyanname verileri eLogo Portalı üzerinden sisteme iletilir. Bu aşamada gönderilen beyannamenin hangi versiyon ile içeri alınacağını beyannamenin yıl/ay bilgisi belirler.

**• Tahakkuk:** İletim sonrası aktifleşen Tahakkuk butonu, gönderilen beyannameye ait hesaplanan sonuçların portal üzerinden çekilerek uygulama içerisindeki sonuç hesaplarına aktarılmasını sağlar.

**• Onay:** Tahakkuk işleminin ardından aktif hale gelen Onay butonu, tüm süreci tamamlayarak beyannamenin son halini kesinleştirir.

**• GİB’den Sil:** Gönderim işlemi tamamlandıktan sonra aktifleşen bu buton, sonraki tüm aşamalarda beyannamenin sistemden kaldırılması için kullanılabilir.

Gönderilmiş bir beyanname üzerinde herhangi bir değişiklik yapılması durumunda sistem, mevcut beyannamenin silinmesi gerektiğine dair kullanıcıyı uyarır. Onay verilmesi halinde eski beyanname silinerek güncel veri girişi sağlanır; düzeltme işleminin ardından beyannamenin tekrar **Gönder** adımıyla işleme alınması gerekmektedir.

**• PDF:** PDF kulakçığında Beyanname, Tahakkuk, İhbarname seçenekleri bulunur. Beyanname Gönder butonuna tıklandıktan sonra aktif hale gelirken, Tahakkuk ve İhbarname son adım olan Onay işleminden sonra aktif hale gelir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/b6a708f8-1ae4-407f-8ef9-db1e23989d0c/es_ebyn_PDF.jpg)

İşlem Takibi ve Kullanıcı Bilgilendirmesi: Söz konusu butonlar aracılığıyla yürütülen işlemlerin süresine bağlı olarak, uygulamanın "Yanıt Vermiyor" (Not Responding) durumuna düşmesini engellemek amacıyla bir ilerleme çubuğu (progress bar) mekanizması devreye alınmıştır. Bu sayede işlem devam ederken ekranın alt kısmında "**PDF İndiriliyor**", "**Gönderim Yapılıyor**" gibi anlık durum bilgilendirmeleri yapılarak, kullanıcının süreci şeffaf bir şekilde takip etmesi sağlanmaktadır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/1916ff6f-b32c-4f05-8c5c-206b22852fb4/es_ebyn_ilerleme.jpg)
