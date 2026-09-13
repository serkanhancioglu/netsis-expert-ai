---
title: "e-Posta Dizaynı"
page_id: "50680281"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "e-Posta Dizaynı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / e-Posta Dizaynı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTIyOGFlZjFiLTZlYzYtNDJkMy04YWYzLTc4ZWZhZDM5MjY3NSZsaW5rPTBiY2M1NWQ5LWViYzctNGEwMi05OGQwLTYxYzliNmMwNWZhYiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=228aef1b-6ec6-42d3-8af3-78efad392675&link=0bcc55d9-ebc7-4a02-98d0-61c9b6c05fab&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "e-posta-dizayni_82576844_50680281.html"
source_version: "2022-11-03T09:52:23.937+03:00"
source_bytes: 1337546
fetched_at: "2026-09-13T04:26:20+00:00"
generator: "netsis-scraper 1.0.0"
---
# e-Posta Dizaynı

e-Posta Dizaynı ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

e- Posta Dizaynı ile, E-posta uygulaması ile gönderilen olay bazlı e-postaların dizayn edilebilmesi sağlandı. Ekranlarda ve uygulamada yapılan değişiklikler aşağıda anlatılacaktır.

#### Dizayn Modülündeki Yenilikler

Dizayn kayıtları ekranına Modül/Eposta seçeneği eklenmiştir. Eposta için yapılan dizaynlarda Eposta seçeneği işaretlenmelidir. Diğer dizaynların tamamında Modül seçeneği işaretlenmelidir. Var olan dizaynlarda da bu bölüm “Modül” seçili olarak gelecektir. Eposta dizaynı yapılırken dizayn genel bilgiler bölümünde, Printer Port sahasında sadece E-Netsis ve Word seçenekleri kullanılacaktır. Diğer sahaların seçilmesine izin verilmemektedir.

![](../_assets/8820fa1c064b6d0f4552.png)

Eposta dizaynı kalem bilgilerinin tanımlaması, modül dizaynlarının kalem tanımlamaları ile tamamen aynıdır. Ayrıca kullanılmakta olan modül dizaynları kopyalanıp, kopya üzerinde, yukarıda verilen bilgiler doğrultusunda değişiklik yapılarak eposta gönderiminde kullanılabilir. Eposta dizaynlarının içinde resim kullanılamamaktadır. Daha sonraki versiyonlarda bu özellik de desteklenecektir.

#### Cari E-Posta Tanımlamalarındaki Yenilikler

Cari e-posta tanımlama ekranına “Dizayn” başlıklı üçüncü bir sekme eklenmiştir. Dizayna göre eposta gönderilmek istenen işlemler bu bölümde belirlenecektir. Eposta gönderimi yapıldığı halde bu bölümde dizayn seçilmemiş olan işlemler, eskiden olduğu gibi, Netsis’in standart formatlarına göre gönderilecektir.

![](../_assets/a2bee357b8c11514f75e.png)

**İşlem Tipi:** Bu bölümde e-posta gönderiminde dizayn kullanılabilecek işlemlerin listesi bulunmaktadır. Şuan için listede görülen işlemlerden, Sipariş, Đrsaliye, Fatura, Genel Dekont Kaydı, Kasa Tahsil/Tediye, Müşteri/Satıcı Havale/Eft, Talep ve Teklif‘in eposta olarak dizayn edilebilmesi desteklenmiştir. 4.0.06 versiyonu süresince diğer işlemlerin de desteklenmesi hedeflenmektedir.
**Eposta/Dizayn:** Eposta/Dizayn kolonunda bulunan ![](../_assets/df2e0ff56caa09a536d5.png) x ikonları çift tıklandığında onay ![](../_assets/ea71d4032822381c336b.png) ikonuna dönüşecek ve ilgili satırda bulunan işlem için e-posta gönderimi sırasında dizayn kullanılacağı anlaşılacaktır.
**Dizayn:** Eposta gönderimi sırasında hangi dizaynın kullanılacağı bu bölümde seçilebilmektedir.
Örn: faturanın e-posta olarak gönderilmesi sırasında hep aynı dizayn kullanılacak ise ilgili dizayn rehberden seçilerek kaydedilmelidir. Bir işlem için birden fazla dizayn kullanılacak ise bu bölüm boş bırakılabilir.
**Sorulsun:** Sorulsun işaretlendiğinde, ilgili işlem yapılırken hangi dizayna göre eposta gönderileceği program tarafından sorgulanacaktır. Eğer dizayn bölümünde bir dizayn belirlenmiş ise dizayn adı sahasına bu bilgi öndeğer olarak gelecektir.

![](../_assets/ffb82a49c89176c9283b.png)

Sorulsun işaretlenmediğinde ise dizayn bölümünde seçilen dizayna göre eposta gönderilecek, gönderim sırasında herhangi bir sorgulama yapılmayacaktır.

Cari E-Posta Tanımlamaları/Dizayn sekmesinde yapılan düzenlemelerin kaydedilebilmesi için “Değişiklikleri Kaydet” butonuna basılmalıdır.
Dizayn yapılarak gönderilmiş e-posta örneği:

![](../_assets/84e23f79af425942c93a.png)

Word seçeneği işaretlenerek dizayn yapıldığında, şablon belgenin içerisinde bulunan tablo ve kenarlıkların basımı için Grup Kodu: DIZAYN, Anahtar: WITHBORDER, Değer: 0 olan özel parametre tanımlanması gerekmektedir.
