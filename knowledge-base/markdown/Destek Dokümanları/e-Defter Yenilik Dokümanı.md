---
title: "e-Defter Yenilik Dokümanı"
page_id: "50680025"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "e-Defter Yenilik Dokümanı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / e-Defter Yenilik Dokümanı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWU0MGU4YzU2LWE1NjEtNGZhMy04NDU4LWZlMTYzMThmNTQyZiZsaW5rPWRjY2NmYjYyLTVkNTQtNDYyMS05MjU3LWIwZDE4OTE3OGU5NCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=e40e8c56-a561-4fa3-8458-fe16318f542f&link=dcccfb62-5d54-4621-9257-b0d189178e94&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "e-defter-yenilik-dokumani_82576402_50680025.html"
source_version: "2022-11-03T09:39:55.350+03:00"
source_bytes: 620055
fetched_at: "2026-09-13T04:26:03+00:00"
generator: "netsis-scraper 1.0.0"
---
# e-Defter Yenilik Dokümanı

e-Defter Yenilikleri ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

|  |  |
| --- | --- |
| **Amaç** **ve** **Fayda** | e-Defter uygulaması ile ilgili Gelir İdaresi Başkanlığı'nın Mart 2016'da yayınladığı uygulama kılavuzundaki düzenlemeler ve Gelir İdaresi Başkanlığı'nın onay almış yazılım firmalarının e-defter uygulamalarına eklenmesini istediği ilave özellikler/kontroller Netsis e-defter uygulamasında desteklenmiştir. |
| **Ürün** **Grubu** | \[X\] Netsis Enterprise<br>\[X\] Netsis Standard<br>\[X\] Netsis Entegre |
| **Modül** | \[X\] Muhasebe |
| **Uygulama** | **Mükellef** **Bilgileri** **Ekranında** **Düzenleme**<br>![](../_assets/f75ddb874f58ed2ae386.png) e-defterde gösterilen mükellef ve düzenleyen bilgilerin kaydedildiği ekranda çeşitli kontroller eklenmiştir: - Faaliyet Konusu alanına girilen NACE kodlarının maksimum uzunluğu olan 64 karakter uzunluğuna göre girilebilecek olan karakter sayısı 64 olarak kısıtlanmıştır.<br>- Dönem Bilgisi alanı, eğer ilgili dönemde oluşturulmuş olan bir e-defter parçası varsa, bu alanın değiştirilememesi desteklendi.<br>- e-Defter şube uygulamasında, eğer dönem bilgisinde belirtilen tarih aralığında kayıtlı bir e-defter parçası varsa şube bilgilerinin değiştirilmemesi sağlandı. Böylece dönem<br>ortasında şubeli e-defter oluşturulamaması desteklenmiş oldu. |

![](../_assets/940e0c3e14b8501facef.png)![](../_assets/779b0e0f12dd79fb0a1b.png)

#### e-Defter Silme İşlemde Düzenleme

e-Defter silme işleminde açıklama girilmesi zorunlu tutulmuştur. Admin hak kontrolü ile açılan ve onay almış e-defterlerin de silinebilmesini destekleyen e-defter silme işleminde bu düzenleme ile artık açıklama bilgisi girilmeden e-defterlerin silinmesi mümkün olamayacaktır.

#### e-Defter Yükleme İşleminde Düzenleme

Onay almış başka bir e-defter uygulamasından, Netsis e-defter uygulamasına geçiş durumunda önceki uygulamadan oluşturulan e-defterlerin ve beratların yüklenmesinde kullanılan "e-Defter Yükleme" işleminde de şema ve şematron kontrolü desteklenmiştir.

#### e-Defter Log Bilgileri Ekranı

e-Defter oluşturma, e-Defter silme işlemleri ve bu işlemler sırasında alınan uyarı ve hataların tutulduğu log kayıtların takip edilebilmesi için Log Bilgileri ekranı e-Defter uygulamasına eklenmiştir.

![](../_assets/adbeffa9ebe39c85f892.png)

#### Manuel e-Defter Bölme

Netsis e-defter uygulamasında e-defter oluşturma işleminde oluşan e-defterlerin boyutları program tarafında kontrol edilerek uygun büyüklüklerde e-defter bölünerek oluşturuluyor. Bu özellik aynen devam etmektedir, bu özelliğe ilave olarak çok nadir olarak mükelleflerin unvan değişikliği vb. sebeplerle istedikleri tarih veya madde numarasına göre e-defterlerini manuel oluşturabilmelerine olanak veren manuel e-defter bölme işlemi de desteklendi.

Tarih/Madde Numarası Bazında Defter oluşturma ekranında kullanıcı belirlediği madde numaraları aralıklarını ekle butonu ile ekledikten sonra e-Defter Oluştur işlemini çalıştırdığında belirlediği aralıklara göre e-defterlerin oluşmasını sağlayabilmektedir.

*Not: Bu ekranda ay seçimi yapılmamaktadır, kullanıcılar standart e-defter oluşturma ekranında* *ay ve yıl seçimi ve ekrandaki parametreleri düzenledikten sonra işlemler altındaki manuel e-* *defter* *oluşturma işlemini çalıştırmalıdır.*

#### Boş e-Defter oluşturulmasında düzenleme

Mükelleflerin çeşitli sebeplerle boş e-Defter oluşturması gerekebilmektedir. Bu işlemin tüm ayı kapsayan bir şekilde oluşması engellenerek sadece manuel defter bölme işleminde ayın sadece son parçası için boş defter oluşturulabilmesi kontrolü eklenmiştir.

#### UniqueId kotrolünde düzenleme

Geçmiş ay e-defterlerden bir tanesinin tekrar oluşturulup beratlarının gelir idaresine gönderildiği durumlarda oluşturulan tekil numarasının manuel e-defter oluşturma işlemide düşünülerek düzgün oluşturulmasına yönelik çalışma tamamlanmıştır.

#### Online Entegrasyonda Faturaların aynı fişte birleştirilebilmesi

Gelir İdaresi Başkanlığı'nın [www.edefter.gov.tr](http://www.edefter.gov.tr/) internet sitesinde yayınlanan duyuruya göre "E- Defter Uygulama Kılavuzu V-1.4" yayımlanmıştır. Kılavuzda yapılan güncellemelerden Netsis uygulamasında da değişiklik gerektiren, muhasebe kaydına konu edilecek faturaların en fazla 10'ar günlük muhasebe kayıt periyodunun dikkate alınması, en fazla 50 adet faturaya yer verilmesi ve her bir faturanın ait olduğu hesabın altında ayrı ayrı gözükecek şekilde belgenin türü, tarihi ve numarasına yer verilmesi kaydıyla, bir yevmiye maddesi içinde kaydedilebilmesi ile ilgili çalışmamız online entegrasyon için desteklenmiştir.
