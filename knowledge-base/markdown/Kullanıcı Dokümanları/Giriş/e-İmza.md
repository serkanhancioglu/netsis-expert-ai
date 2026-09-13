---
title: "e-İmza"
page_id: "47084396"
product: "netsis-3-enterprise"
depth: 3
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Giriş"
  - "e-İmza"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Giriş / e-İmza"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWU5ZTM1MmEyLTY0MjUtNDg2NS1iMWExLTgxMTQ5Yjc3ZmZjNCZsaW5rPTkzZjUzYjVjLTNkY2QtNDAwYi1iMDBmLTllODFkMTZlMDEzNSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=e9e352a2-6425-4865-b1a1-81149b77ffc4&link=93f53b5c-3dcd-400b-b00f-9e81d16e0135&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "e-imza_94634039_47084396.html"
source_version: "2022-10-21T13:59:22.507+03:00"
source_bytes: 16072
fetched_at: "2026-09-13T04:01:25+00:00"
generator: "netsis-scraper 1.0.0"
---
# e-İmza

e-İmza ile Netsis uygulamalarında dijital imza desteklenir. Bu uygulama ile raporlarda, program içinden e-Posta gönderme işlemlerinde, iş akış yönetiminde, onay mekanizmasında ve program bazında güvenlik kontrollerinde, dijital imza ile şifreleme yapılması sağlanır. Ayrıca "Personel Paketi" kullanılıyorsa internet ortamından izlenen personellere ait bordrolarında imzalanması mümkündür. Şifreleme işlemi için uygulamayı kullanacak kişinin "TÜRKTRUST" firmasına kişisel başvurusu sonucunda, şahsına verilen e-İmza kartına ihtiyaç vardır. Böylece, standart bir dijital dosya düzeni oluşur ve Netsis tarafından saklanan dosyalar sadece Netsis uygulamaları tarafından açılır.

e-İmza uygulamasının kullanılması için aranan makine ve sistem özellikleri aşağıdaki gibidir:

- Minimum-Windows XP (Dijital imza API desteği için).
- Minimum 30 Mb disk space.
- 100 MB memory.

e-İmza uygulamasının aktif hale getirilmesi için ilgili makinede e-İmza kartının takılı olması gerekir. Netsis uygulamalarının bağlantı ekranında e-İmza kartı takılı ise, uygulama otomatik olarak algılanır ve pin kodu sorgulanır. Bu şekilde programa giriş yapıldığında, pin kodu geçici bir veriyi imzalar ve sonrasında onay ister. Onayın olumlu olması sonucu uygulama, kullanıcı sertifikası bilgisi ve Netsis’in kullanıcı bilgisi değerlerini karşılaştırıp bağlantı ekranından "Ana Menü" ekranına geçişe izin verir. Böylece kullanıcı pin kodunu yazdığında, gelen sertifika ile Netsis güvenlik bilgilerini eşleştirir ve sisteme giriş yapmak isteyen kullanıcı tespit edilebilir.

Girişte sorgulanan pin kodu ile kullanıcı sertifika bilgisinin eşleştirilmesi için; Kullanıcı İşlemleri → Kayıt → "[Kullanıcı Kayıtları](<../Genel/Kullanıcı İşlemleri/Kayıt/Kullanıcı Grup Kayıtları.md>)" ekranında bazı tanımlamaların yapılması gerekir.

**Kullanıcı Kayıtlarında Şifreleme İle İlgili Tanımlamalar**

"Kullanıcı Kayıtları" ekranında "Nitelikli Elektronik Sertifika (NEK) Bilgileri" bölümündeki alanlarda tanımlama yapılması gerekir.

Kart Seri Numarası: Kullanıcının NES (Nitelikli Elektronik Sertifika) kartına ait seri numarası değerinin girildiği alandır. Bu değer, program dizini olan Servis’in altında bulunan cardinfo.exe dosyası ile okunur. Kullanıcı, karta ait pin kodunu gidiğinde, öncelikle pin kodu kart üzerinden onaylanır ve daha sonra karta ait seri numarası alınıp "Kullanıcı Kayıtları" ekranındaki "Kart Seri Numarası" ile eşleştirilerek ilgili kullanıcı bulunur.

Girişlerde Kart Zorunlu: Bu parametrenin işaretlenmesi durumunda, Netsis’e bağlantı ekranından giriş yapmak isteyen kullanıcı, kart olmadan Netsis uygulamalarına giriş yapamaz. Bu özellik, programa girişlerde artı bir güvenlik faktörü olarak da kullanılabilir.

**Menülerde e-İmza İşlemleri**

e-İmza uygulaması kullanılıyorsa, tüm modül menülerinde Araçlar\\Fonksiyonlar alt menüsünde e-İmza işlemleri seçeneği görüntülenir. e-İmza İşlemleri; Kart Sahibine Ait Bilgiler, Dosya İmzala ve İmzalanmış Dosyayı Aç bölümlerinden oluşur.

Menülerde e-İmza işlem alanları ve içerdiği bilgiler şunlardır:

| Menülerde e-İmza İşlemleri |  |
| --- | --- |
| Kart Sahibine Ait Bilgiler | Aktif takılı karta ait kullanıcı bilgilerinin izlendiği ekrandır. |
| Dosya İmzala | Dışarıdan seçilen dosya aktif kart bilgisi ile şifrelenir. İmzalanacak dosya adı uzantısının, mutlaka NED olması gerekir. Kullanıcının yazmaması veya başka bir uzantı yazması durumunda, uygulama otomatik olarak dosyanın uzantısını NED haline çevirir. |
| İmzalanacak Dosya Adı | İmzalanacak dosyanın girildiği alandır. İlgili dosya, alanın sağ tarafında yer alan seçenek kutucuğundan seçilir. |
| İmzali Saklanacak Dosya Adı | Bir önceki alanda seçilen dosyanın dijital ortamda imzalandıktan sonra saklanması istenen ismin girildiği alandır. |
| Dosyayı İmzala | "İmzalanacak Dosya Adı" alanında seçilen dosyanın aktif kart bilgisi ile şifrelenmesi için onaylanan alandır. |
| İmzalanmış Dosyayı Aç | Netsis e-İmza uygulaması tarafından imzalanan dosyaların açılmasını sağlar. Başka uygulamalardan imzalanan dosyalar bu ekrandan açılamaz. Açılması istenen dosya, önce program tarafından kontrol edilir ve Netsis tarafından imzalanmamışsa uyarı verir. Dosya açıldıktan ve saklandıktan sonra, dosyayı imzalayan kart sahibinin bilgileri ekranda izlenebilir. |

**Rapor Dosyalarının Şifrelenmesi**

Netsis içinden alınan standart yada genel raporlar dosya olarak saklanabilir. Saklanan dosyaların kullanıcı tarafından dijital imza ile onaylanması için e-İmza uygulaması, rapor dosyasının istenen düzende saklandıktan sonra - XLS, HTML, TXT - ek olarak NED dosyasını da hazırlar. Bu dosya herhangi bir amaçla saklanabilir ve e-Posta ile gönderilip korunması istenebilir. Dosyanın içeriği daha sonra Netsis uygulamaları içinden - Araçlar/NED Dosyalarını Görüntüle - ya da dışından - NED Shell, Explorer, Extension - izlenebilir.

**Rapor Modülündeki Raporların e-İmza ile Şifrelenmesi**

Rapor modülünden alınan raporların dosyaya saklanması durumunda - e-İmza sistemi açık ise - dosyalar hem kullanıcının verdiği isimle hem de aktif kart bilgisi ile saklanır. İmzalı dosyaların uzantıları, girilen dosya adına ilave olarak “.ned” olur.

Rapor modülünden hazırlanan raporların e-İmza uygulaması ile şifrelenmesi için, öncelikle "Yazıcı Seçenekleri" sekmesinden “Dosya İmzala” seçeneğinin işaretlenmesi gerekir. Raporun Excel, Text ya da Html olarak saklanması için dosya adı verilmsi gerekir. Başka bir ortama aktarılmadan normal rapor dosyası olarak saklanması için Excel, Text, Html dosya adı alanlarında bir tanımlama yapılmadan önce raporun ekranda listelenmesi gerekir. Raporun tamamı ekranda listelendikten sonra “Netsis Akıllı Kart Uygulaması” ekrana gelir ve kullanıcının Pin Kodu sorgulanır. Pin Kodu girildikten sonra “Tamam” butonuna tıklanması ile, rapor dosyası ilgili kart sahibi tarafından şifrelenir.

Rapor dosyası Xls, Txt ya da Html olarak saklanmışsa, şifrelendiği zaman dosya "ned" uzantısı ile oluşur.

**Örneğin;** rapor.xls.ned, rapor.txt.ned yada rapor.htm.ned gibi bir rapor, normal bir rapor dosyası olarak ekrana alındığı zaman, uzantısı "nrp" olarak oluşur. ilgili rapor dosyası e-İmza ile şifrelendiği zaman, yine isminin sonuna "ned" uzantısı eklenir.

Örneğin; rapor.nrp.ned gibi.

**Standart Raporların Şifrelenmesi**

Standart raporların "Ön Sorgulama" sekmesinde - e-İmza Uygulaması açık ise - “Dosya İmzala” sorgusu görüntülenir.

Standart raporların e-İmza uygulaması ile şifrelenmesi için öncelikle "Yazıcı Seçenekleri" sekmesinden “Dosya İmzala” seçeneğinin işaretlenmesi ve daha sonra raporun hangi ortama gönderilmesi isteniyorsa - Excel, Text, Html - aynı ekrandan dosya adı verilerek raporun ekrana alınması gerekir. Raporun tamamı ekranda listelendikten sonra “Netsis Akıllı Kart Uygulaması” ekrana gelir ve kullanıcının Pin Kodu sorgulanır. Pin kodu girilip “Tamam” butonuna tıklandığında, Excel, Text ya da Html olarak kaydedilen rapor dosyası ilgili kart sahibi tarafından şifrelenir.

Bu özellik aktif hale getirildiğinde, rapor sonucu oluşturulacak tüm dosyalara (Excel, Html, Text) ilave olarak ".ned" uzantılı dosyalar program tarafından otomatik olarak oluşturulur. Kullanıcı Excel dosya adına “C:\\Temp\\Rapor.xls” yazmışsa, imza sonucu oluşacak dosya “C:\\Temp” dizini altında “rapor.xls.ned” şeklinde oluşur.

**Rapor E-Posta Gönderiminde Şifreleme**

e-Posta uygulaması kullanıldığında - e-Posta uygulamasının aktif hale gelmesi için Yardımcı Programlar → Kayıt → Şirket/Şube Parametreleri → “e-Posta Uygulaması Var” parametresinin işaretlenmesi gerekir. - Netsis raporları ekrana geldikten sonra “Netsis e-Posta” seçeneği işaretlendiğinde - e-İmza uygulaması açıksa - aktif rapor bilgisi saklanır ve daha sonra imzalanarak istenen e-Posta adresine .ned uzantılı gönderilir. e-Posta ile gönderilecek NED dosyası, programa giriş yapan kullanıcının windows\\temp dizini altında oluşturularak e-Posta ile ekli şekilde gönderilir.

Raporun e-Posta olarak gönderilmesi için tanımlama yapılan e-Posta ekranında “Dosya İmzala” seçeneğinin işaretlenerek e-Posta gönderilecek dosya e-İmza uygulaması ile şifrelenir.

**Duyuru E-Posta Gönderme İşleminde Şifreleme**

Cari modülünde yer alan "Duyuru e-Posta Gönderme" ekranında - e-Posta uygulamasının aktif hale gelmesi için Yardımcı Programlar → Kayıt → [Şirket/Şube Parametreleri](<../Muhasebe/Muhasebe Modülü/Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/Genel Tanımlar/Yardımcı Programlar-Şirket-Şube Parametreleri.md>) → “e-Posta Uygulaması Var” parametresinin işaretlenmesi gerekir. - e-İmza uygulaması açıksa - aktif rapor bilgisi saklanır ve daha sonra imzalanarak .ned şeklinde dosyaların bulunduğu dizinin altına saklanır. e-Posta sistemi imzalanmış .ned dosyaları e-Postaya ilişkilendirerek gruba gönderilir. Birden fazla dosyanın “;” ayracı ile yazılması durumunda, imzalama sistemi bu dosyaları tek tek imzalar.

**İş Akış Yönetimi’nde (Workplace) e- İmza İle Şifreleme**

İş Akış Yönetimi (Workplace) uygulaması kullanıldığında, uygulamanın aktif hale gelmesi için Yardımcı Programlar → Kayıt → [Şirket/Şube Parametreleri](<../Muhasebe/Muhasebe Modülü/Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/Genel Tanımlar/Yardımcı Programlar-Şirket-Şube Parametreleri.md>) → “Workplace Uygulaması Var” parametresinin işaretlenmesi gerekir.

e-İmza uygulaması aktif ise, kullanıcı "Onay" yerine “İmzalı Onay” yapabilir. "İmzalı Onay" fatura belgelerinde desteklenir. Seçildikten sonra, ekrana onay için JPG biçiminde bilgi getirilir ve daha sonra kullanıcıdan onay vermesi beklenir. Kullanıcının, ekranda gösterilen bilgileri okuyup imzalaması gerekir. İmza sonucu, silme ve düzeltme işlemlerinin yapılmadığı, raporlanan TBLIMZALOG tablosuna kayıt aktarılır.

İmzalamak İstiyorum: Seçeneğin işaretlenmesi ile ilgili fatura belgesi, kullanıcıya gösterildiği şekilde saklanır ve imzalanır. Böylece Netsis fonksiyonlarından çıkan bilginin yıllar sonra bile değişmeyecek düzende saklanması sağlanır.

İmzalamak İstemiyorum: Ekrana gelen fatura belgesinin kullanıcı tarafından imzalanması istenmediğinde kullanılan seçenektir.

**Windows Explorer’dan Dosyaların İmzalanması ve İmzalı Dosyaların Açılması**

"Netsis e-İmza Uygulaması" servis program dizini altındaki regkontrol.exe’nin çalıştırılması ile istemciye kaydedildikten sonra Windows Explorer ile uyumlu, çalışır hale gelir. Herhangi bir dosya seçildiğinde ve farenin sağ tuşuna tıklandığında “Netsis Dosya İmzalama” menüsü ekrana gelir.

Bu menü çalıştırıldığında bir sonraki pencere ile seçilen dosyalar imzalanır. İmzalanan dosyalar, varsayılan olarak \*.NED şeklinde saklanır. Regkontrol ile kayıt sonrasında Windows Explorer Shell sistemi, otomatik olarak ned dosyalarını tanır ve dosyalar ikon bilgisi ile gösterilir. İlgili dosyalar üzerinde fare ile iki kez tıklandığı zaman, gelen ekrandan ilgili dosyanın açılması sağlanır.

İmzalanmış Dosya Adı: e-İmza uygulaması ile imzalanan dosya adının ve bulunduğu dizinin izlendiği alandır.

Açılacak Dosyanın Adı: e-İmza uygulaması ile imzalanan dosyanın gerçek adının ve bulunduğu dizinin - dosyanın e-İmza ile imzalanmamış hali - izlendiği alandır.

İmzalanmış Dosyayı Aç: İlgili dosyanın açılmasını sağlayan butondur.

Dosyayı İmzalayan Kart Sahibinin Bilgileri: Dosyayı imzalayan kart sahibine ait bilgilerin izlendiği alandır.

Açılan Dosya Hakkında: Açılan dosyaya ait bilgilerin izlendiği alandır.
