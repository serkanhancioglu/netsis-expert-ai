---
title: "Kullanıcı Parametreleri"
page_id: "41168985"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Genel"
  - "Kullanıcı İşlemleri"
  - "Kayıt"
  - "Kullanıcı Parametreleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Kullanıcı İşlemleri / Kayıt / Kullanıcı Parametreleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWExZTUwOGYxLWNjNGMtNGE3YS05ZjQ1LTA2YWRlYTM1NTk3ZCZsaW5rPTZlYWU0YWNhLTcxZGUtNGM2NS1iZmEzLTY4YzNkNzljNDA0NSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=a1e508f1-cc4c-4a7a-9f45-06adea35597d&link=6eae4aca-71de-4c65-bfa3-68c3d79c4045&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "kullanici-parametreleri_47074213_41168985.html"
source_version: "2022-12-01T15:07:00.643+03:00"
source_bytes: 136006
fetched_at: "2026-09-13T04:17:51+00:00"
generator: "netsis-scraper 1.0.0"
---
# Kullanıcı Parametreleri

Kullanıcı Parametreleri, Genel Bölümü'nde Kayıt/Kullanıcı İşlemleri menüsünün altında yer alır. Her kullanıcının tanımlamalarına öndeğer olarak aktarılacak parametrelerin seçildiği bölümdür. Kullanıcılar ile ilgili genel tanımlamaların yapılmasını sağlar.

Kullanıcı Parametreleri ekranı; Temel Güvenlik Parametreleri, İleri Güvenlik Parametreleri, Kullanıcı Güvenlik Parametreleri olmak üzere üç sekmeden oluşur.

**Temel Güvenlik Parametreleri**

![](../../../../_assets/2e0ab6ac32989667e055.png)

Temel Güvenlik Parametreleri ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Kullanıcı Parametreleri Ekranı |  |
| --- | --- |
| Minimum Kullanıcı İsmi Uzunluğu | Program kullanıcı isimlerinin en az kayıt uzunluğunun girildiği parametredir. Programdaki kullanıcı isminin uzunluğu en fazla 12 karakterdir. Kullanıcı tanımlanırken, bu parametrede girilen sayıdan daha az karakterde isim uzunluğunun girilmemesi için kullanılır. Alan 0 (sıfır) olarak bırakıldığında, isim için en az uzunluk barajı dikkate alınmaz. |
| Maksimum Şifre Değiştirme Süresi (Gün) | Program kullanıcı şifrelerinin değiştirilme süresinin girildiği parametredir. Sürenin gün bazında girilmesi gerekir. **Örneğin;** Program kullanıcısının aynı şifre ile 10 gün çalışması, 10. günden sonra aynı şifre ile programa girmeleri istenmediği zaman, belirlenen gün sayısının (10) bu alana kaydedilmesi gerekir. Değer 0 (sıfır) olarak bırakılırsa, kullanıcının belli sürelerde şifre değiştirme zorunluluğu ortadan kalkar. > [!NOTE]<br>> Bu parametrenin önemi, belli aralıklarda program kullanıcı şifrelerini değiştirmeye zorlayarak yetkisiz kişilerin program kullanımına engel olunmasıdır. |
| İzinsiz Girişler Takip Edilsin | En fazla geçersiz şifre sayısı, geçersiz iki giriş arasının iptal edilme süresi ve kilitli kalacağı süre tanımlanarak, kullanıcıların programa hatalı girişlerinin takip edilmesi için kullanılan parametredir. |
| Geçersiz Girişlerin İptal Edilme Süresi (Dakika) | "İzinsiz Girişler Takip Edilsin" parametresinin işaretlenmesi ile aktif hale gelen parametredir. Arka arkaya girilen yanlış şifrelerin takip edildiği ve kullanıcının belli sayıda yanlış şifre girmesinden sonra bloke edildiği durumda, iki yanlış şifre girilmesi arasında geçen sürenin dakika olarak belirlenmesini sağlar. **Örneğin;** 1 dk. girildiği varsayıldığında, yanlış girilen şifreden sonra ikinci denemesini 1 dk içinde yaparsa ve tekrar yanlış şifre girerse, ikinci yanlış şifre olarak sayılarak maksimum geçersiz şifre sayısı ile kontrol edilir. Kullanıcı, ikinci denemesini 1 dakikalık süre geçtikten sonra yaparsa, ilk yanlış deneme program tarafından unutulur ve ikinci deneme sanki ilk kez yanlış girilmiş gibi düşünülür. Bu durumda, maksimum geçersiz şifre sayısı ile kontrol edilecek olan yanlış şifre sayısı 1 olur. Kullanıcıların hatalı girdikleri şifre denemeleri, hatalı deneme yapıldığı andan itibaren tarih ve saat olarak program tarafından hafızaya alınarak tutulur. |
| Otomatik | Merkezi Kimlik Yönetimi (SOS) bölümünden tanımlanan kullanıcıların, bu alanda belirlenen süre ile programa giriş yapmamaları durumunda, kullanıcı isminin ve tüm tanımlamasının otomatik olarak program tarafından silinmesi için kullanılan parametredir. Bunun için "Maksimum Şifre Değiştirme Süresi (Gün)" alanına gün değerinin girilmesi ve bu parametrenin işaretlenmesi gerekir. |
| Maksimum Kullanıcı Sayısı | Program kullanıcısının, programa aynı anda gireceği terminal sayısının belirlendiği parametredir. Program kullanıcılarının aynı anda sadece bir makineden programa girmeleri için 1 sayısının girilmesi gerekir. Böylece kullanıcı aynı anda bir terminalden programa girer. Diğer kullanıcılar bu kişinin isim ve şifresini bilseler bile giriş yapamaz. 0 (sıfır) değeri sonsuz giriş hakkıdır. Aynı kullanıcı, isim ve şifresi ile programa istediği sayıda giriş yapabilir. |
| Admin Tarafından Verilen Şifreyi Değiştirme Süresi (Gün) | Admin kullanıcısı, Merkezi Kimlik Yönetimi (SOS) ekranından diğer kullanıcıların şifrelerini belirleyebilir. Admin kullanıcısının verdiği şifrenin kullanılacağı gün sayısının girildiği parametredir. Girilen gün dolduktan sonra, kullanıcı şifresinin değiştirilmesi istenir. |
| Minimum Şifre Uzunluğu | Program kullanıcı şifrelerinin en az kayıt uzunluğunun girildiği parametredir. Programdaki kullanıcı şifresi uzunluğu en fazla 12 karakterdir. Kullanıcı tanımlanırken, bu parametrede girilen sayıdan daha az karakterde şifre uzunluğunun girilmemesi için kullanılır. Alan 0 (sıfır) olarak bırakıldığında, şifre için en az uzunluk barajı dikkate alınmaz. |
| Maksimum Geçersiz Şifre Sayısı | "İzinsiz Girişler Takip Edilsin" parametresinin işaretlenmesi ile aktif hale gelen parametredir. Kullanıcı ismi girildikten sonra şifrenin girileceği hatalı kayıt sayısının belirlenmesini sağlar. Tanımlanan sayısal değer kadar şifre yanlış girildikten sonra program “Yanlış şifre girme limitiniz doldu. Program kapatılacak!” uyarısı ile şirket seçme ekranına geri döner. Aynı kullanıcının tekrar şifre denemelerine geçmesi için bir süre geçmesi gerekir. Kullanıcı bu süre içinde bloke edilir. Bloke edilme süresi parametrik olarak belirlenir. |
| Kullanıcının Kilitli Kalacağı Süre (Dakika) | "İzinsiz Girişler Takip Edilsin" parametresinin işaretlenmesi ile aktif hale gelen parametredir. Maksimum geçersiz şifre sayısında belirtilen sayı kadar şifresini hatalı giren kullanıcının, tekrar isim ve şifresini girmek üzere programa girmeyi denediğinde bloke edilme (giriş yapamama) süresinin belirlenmesini sağlar. Girilen değer dakika olarak girilir. Program, kullanıcının kilitlendiği gün ve kilitli kaldığı süreyi log eder. Merkezi Kimlik Yönetimi (SOS) ekranından en son kilitlendiği tarih ve kilitli kaldığı saat izlenebilir. |
| Gün Login Olmayan Kullanıcılar Silinsin | Merkezi Kimlik Yönetimi (SOS) bölümünden tanımlanan kullanıcıların, bu alanda belirlenen süre ile programa giriş yapmamaları durumunda kullanıcı isminin ve tüm tanımlamasının otomatik olarak program tarafından silinmesini sağlayan parametredir. Bunun için "Maksimum Şifre Değiştirme Süresi (Gün)" alanına gün değerinin girilmesi ve bu parametrenin işaretlenmesi gerekir. Bunun için gün sahasına gün değerinin girilmesi, bu parametrenin işaretlenmesi gereklidir. |
| Program Girişinde Boş Şifre Kontrolü Yapılsın | Programa girişte şifre yazmadan boş şifre ile girilmesinin engellenmesi için kullanılan parametredir. İşaretlendiği zaman, kullanıcı için şifre tanımlanmamış olsa da şifrenin boş bırakılması istendiğinde “Boş şifre girişi yapamazsınız!” şeklinde uyarı mesajı ekrana gelir ve kullanıcının programa girişi engellenir. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilgilerin onaylanmasını sağlayan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) iptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |

**İleri Güvenlik Parametreleri**

**![](../../../../_assets/e9e202dec6a0f84784dd.png)**

İleri Güvenlik Parametreleri ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Kullanıcı Parametreleri Ekranı |  |
| --- | --- |
| Şifre İçerisinde Boşluk Geçmesin | Şifre içinde boşluk bırakılmaması için kullanılan parametredir. |
| Şifre Rakam ve Harf Kombinasyonu İçersin | Şifrenin rakam ve harf kombinasyonu içermesi, sadece rakamdan veya sadece harften oluşmaması için kullanılan parametredir. |
| Şifre Özel Karakterler İçersin | Şifrenin özel karakterler içermesi için kullanılan parametredir. |
| Şifre Büyük Küçük Harf İçersin | Şifrenin hem büyük hem de küçük harf içermesi için kullanılan parametredir. |
| Şifre İçerisinde Kullanıcı Adı Geçmesin | Şifre içinde kullanıcı adının geçmemesi için kullanılan parametredir. |
| Şifre İçerisinde Kullanıcının İsmi ve Soyadı Geçmesin | Şifre içinde kullanıcı isim ve soyadının geçmemesi için kullanılan parametredir. |
| Şifre İçerisinde Aynı Karakter Sıralı Olarak 3 Kez Tekrarlamasın | Şifre içinde aynı karakterin sıralı olarak 3 kere tekrarlanmaması için kullanılan parametredir. |
| Şifre İçerisinde Kullanıcı Adının Sıralı 3 Karakteri Geçmesin | Şifre içine kullanıcı adının sıralı olarak 3 karakteri geçmemesi için kullanılan parametredir. |
| Şifre ! veya ? Karakteri İle Başlamasın | Şifrenin ! veya ? karakteri ile başlamaması için kullanılan parametredir. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilgilerin onaylanmasını sağlayan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |

**Kullanıcı Güvenlik Parametreleri**

**![](../../../../_assets/69b96d50e73299b5c68e.png)**

Kullanıcı Güvenlik Parametreleri ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Kullanıcı Parametreleri Ekranı |  |
| --- | --- |
| Kullanıcı Tanımlama Hakkı Olan Kullanıcı, Kendisini Admin Yapamasın | Kullanıcı tanımlama hakkı olan kullanıcının, kendisini admin yapamaması için kullanılan parametredir. |
| Kullanıcı Tanımlama Hakkı Olan Kullanıcı, Kendisi Admin Değilse Başkasını Da Admin Yapamasın | Kullanıcı tanımlama hakkı olan kullanıcının, kendisi admin değilse başkasını da admin yapamaması için kullanılan parametredir. |
| Kullanıcı Yetkileri Tanımlama Yetkisi Olan Bir Kişi, Kendisine Yetki Veremesin | Kullanıcı yetkileri tanımlama yetkisi olan bir kişinin, kendisine yetki verememesi için kullanılan parametredir. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilgilerin onaylanmasını sağlayan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
