---
title: "Form Bazında Veri Görselleştirme"
page_id: "102282902"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Form Bazında Veri Görselleştirme"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Form Bazında Veri Görselleştirme"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTM4Nzg3OGI4LWMxNmItNDEzNS1iN2MyLTI1NGM1ZGNiMTMzZiZsaW5rPTU5MmZmY2Y2LTQyNTItNGNlMS1hZmExLTA3MDI3ZWI4ODZhMiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=387878b8-c16b-4135-b7c2-254c5dcb133f&link=592ffcf6-4252-4ce1-afa1-07027eb886a2&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "form-bazinda-veri-gorsellestirme_102282912_102282902.html"
source_version: "2023-01-09T11:18:33.767+03:00"
source_bytes: 253720
fetched_at: "2026-09-13T04:23:43+00:00"
generator: "netsis-scraper 1.0.0"
---
# Form Bazında Veri Görselleştirme

9.0.43 sürümü ile veri görselleştirme panelinde tanımlanan görsellerin, Netsis' de bulunan formlar üzerinden istendiğinde ilgili formdaki alanlara göre kısıtlar verilerek kullanıcıya gösterimi sağlanmıştır. Form bazında veri görselleştirme ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Netsis' deki veri tabanı işlemleri araç çubuğuna "Veri Görselleştirme" adında bir buton eklenmiştir. İlgili ekranda aktif bir kayıt çağrıldığında buton aktif olmaktadır.

![](../_assets/709bf557e20784e13617.png)

Bu butonun düzenleme modunda çalışabilmesi için sso yetkileri Yardımcı Programlar modülü altına "Form Bazında Veri Görselleştirme Yönetimi" adında yeni bir hak eklenmiştir.

Bu buton tıklandığında kullanıcı admin kullanıcı veya SSO üzerinde "Form Bazında Veri Görselleştirme Yönetimi" yetkisine sahip ise;

- Butona bağlı bir görsel bağlı olup olmadığı kontrol edilir, herhangi bir tanımlı görsel yoksa direkt olarak "Form Bazında Veri Görselleştirme" formu açılmaktadır.
- Butona bağlı bir görsel mevcut ise "Form Bazında Veri Görselleştirme Yönetimi yetkisine sahip olduğunuz için düzenleme modunda açmak istiyor musunuz?" şeklinde bir soru ile karşılaşılır.

![](../_assets/20244c2dad3669151dac.png)

- Kullanıcı soruya "Evet" derse bu durumda veri görselleştirme bağlantılarının yapılacağı "Form Bazında Veri Görselleştirme" formu açılır.

![](../_assets/2a46b35e1f0eed213217.png)

- Kullanıcı soruya "Hayır" derse normal bir kullanıcı gibi kendisinin kullanabildiği tanımlı görsellerin olduğu netgridbox ekran açılır. Eğer kullanıcının görebileceği tek bir görsel mevcut ise bu durumda netgridbox ekranı açmadan direkt olarak görsel gösterilir.

![](../_assets/3ebe6362db5e79ee7502.png)

Eğer kullanıcı admin değilse ve "Form Bazında Veri Görselleştirme Yönetimi" yetkisine sahip değilse;

-
  - Bağlı görsel tanımı yoksa "Bu ekran için bağlantılı bir görsel rapor kaydı bulunmamaktadır." şeklinde bir mesaj karşımıza gelmektedir.
  - Bağlı görsel var ise görsellerin listelendiği netgridbox ekran açılır. Eğer kullanıcının görebileceği tek bir görsel mevcut ise bu durumda netgridbox açılmadan direkt olarak görsel gösterilmektedir.

**Form Bazı Veri Görselleştirme Ekranı**

Bu form ile kullanıcılar butona atayacakları görselleri seçip, istendiğinde bu görselin veri setindeki alanlarına kısıtlar verebilir. Form iki sekmeden oluşmaktadır. Birinci sekmede kullanılacak olan görsellerin seçimi gerçekleştirilir, ikinci sekmede ise istendiğinde bu görselin alanlarına kısıtlar verilebilmektedir.

Kullanıcı ilk sekmeye gelip "Görsel Kodu" rehberine tıkladığında bu kullanıcının aktif işletme ve şubede görmeye yetkisi olduğu ayrıca veri seti tanımı içinde kendisine yetkilendirilmiş veri setlerinden oluşan görselleri seçebilir. Aynı zamanda bu görsel atamayı yapmak istediği işletme ve şube bilgisi seçimini de yapabilir. İşletme/şubelerde ortak seçilmesi durumunda veri seti tanımları işletme/şubelerde ortak değil ise "Veri setinin de işletme/şubelerde ortak olması gereklidir" şeklinde uyarı mesajı ile karşılaşılacaktır.

![](../_assets/23facad303b67800a9d1.png)

Kullanıcı görsel seçimi sekmesinde kullanacağı görseli seçtikten sonra veri setine bir kısıt vermek istiyorsa kısıt seçimi sekmesinden seçilen alanlara kısıtlar verebilir. Kısıt seçimi REST harici diğer veri setini kullanan görseller için de yapmak zorunlu değildir, kullanıcı herhangi bir kısıt vermeden de ilgili görseli açabilir.

![](../_assets/9b1d5c38ae6dca3b3960.png)

Görsel rapor sahası alanında veri seti tanımlama ekranlarındaki Nesne Seçimi veya Sorgu girişindeki tanımlamalardan dönen tüm alanlar listelenmektedir.

Kısıt kaynağı alanında ise;

- Form sahaları: Bu değer seçildiğinde kısıt değeri bölümünde ilgili form üzerinde bulunan netedit ve TDBnetedit tipli bileşenlerin isimleri listelenir.
- Değişken: Bu değer seçildiğinde kısıt değeri bölümünde bir memo alan aktif hale gelir ve buraya sabit bir değer veya bir SQL sorgusu yazılabilir.

Bu ekran üzerinde yeni kayıt, kayıt sil ve kaydet işlemleri yapılabilir. Yazılan sorgu sonucu test butonuna basılarak görsel kontrol edilebilir.

![](../_assets/915c4b9923b2bcbb201d.png)

**Tanımlı Görseller**

Form bazında veri görselleştirme ekranlarından yapılan tanımlamalar veri seti tanımlama ekranındaki yetki tanımlarına göre sadece aktif kullanıcının görebileceği görseller tanımlı görseller ekranına getirilmektedir.

![](../_assets/25e6c3655b152a3edb89.png)

Açılan tanımlı görseller ekranında çoklu seçim yapıldığında veri görselleştirme panelindeki gibi 4'erli olarak sekmelere yerleştirilmektedir. Tamam butonuna basıldığında ise verilen kısıtlara uygun widgetlar ekrana getirilmektedir.

![](../_assets/f0fe83c1699d287082c4.png)
