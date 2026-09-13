---
title: "İki Adımlı Doğrulama (2FA)"
page_id: "66248540"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "İki Adımlı Doğrulama (2FA)"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / İki Adımlı Doğrulama (2FA)"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWMxZGQ3NGZhLThhMTMtNDM1Ni04MDVmLTJhYWFmMGY4OTk2MyZsaW5rPWFiMWJiZDQzLTE3ZDUtNDFlMy05OTAyLTA3MDUzMmZjNzAzNCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=c1dd74fa-8a13-4356-805f-2aaaf0f89963&link=ab1bbd43-17d5-41e3-9902-070532fc7034&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "iki-adimli-dogrulama-2fa_80088577_66248540.html"
source_version: "2022-12-12T16:57:17.090+03:00"
source_bytes: 519584
fetched_at: "2026-09-13T04:24:28+00:00"
generator: "netsis-scraper 1.0.0"
---
# İki Adımlı Doğrulama (2FA)

İki Adımlı Doğrulama (2FA) ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Logo Netsis Wings çözümlerinde iki adımlı doğrulama sistemi, Netsis kullanıcı hesabınızın daha güvenli olmasını sağlayan, isteğe bağlı bir özelliktir. İki adımlı doğrulamayı etkinleştirdikten sonra kötü niyetli kişiler tarafından şifreniz çalınmış olsa bile, bu kişilerin hesabınızı ele geçirmesi engellenmiş olur. Kullanıcıların mobil cihazlarına kurdukları authenticator (kimlik doğrulayıcı) uygulamaları tarafından zaman tabanlı tek kullanımlık şifreler (TOTP) oluşturulmaktadır. Netsis uygulamasına giriş sırasında kullanıcıların mobil cihazlarında oluşturulan tek kullanımlık kodları kullanarak hesabına daha güvenli bir şekilde giriş yapmaları sağlanabilir.

Mobil cihazlarda iki adımlı doğrulama için önerdiğimiz bazı authenticator uygulamalarına aşağıdaki bağlantılardan erişim sağlayabilirsiniz:

**Google Authenticator**

App Store: [https://apps.apple.com/tr/app/google-authenticator/id388497605?l=tr](https://apps.apple.com/tr/app/google-authenticator/id388497605?l=tr)

Google Play Store: [https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=tr≷=US](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=tr&gl=US)

**Microsoft Authenticator**

App Store: [https://apps.apple.com/tr/app/microsoft-authenticator/id983156458?l=tr](https://apps.apple.com/tr/app/microsoft-authenticator/id983156458?l=tr)

Google Play Store: [https://play.google.com/store/apps/details?id=com.azure.authenticator&hl=tr](https://play.google.com/store/apps/details?id=com.azure.authenticator&hl=tr)

#### İki Adımlı Doğrulama Sisteminin Etkinleştirilmesi

İki adımlı doğrulama sisteminin işletme-şube bazında aktif hale getirilmesi için **Şirket/Şube/Parametre** **Tanımları** ekranında bulunan **"İki** **Adımlı** **Doğrulama** **Yeri"** parametresinin belirlenmesi gereklidir.

Web seçeneği, iki adımlı doğrulama yalnızca Netsis Wings uygulamasında aktifleştirilmek istenirse seçilmelidir.

Masaüstü seçeneği, iki adımlı doğrulama yalnızca Netsis masaüstü uygulamasında aktifleştirilmek istenirse seçilmelidir.

Tümü seçeneği, iki adımlı doğrulama Netsis Wings ve Netsis masaüstü uygulamasında aktifleştirilmek istenirse seçilmelidir.

![](../_assets/dcf9d16edbd928b84bab.png)

![](../_assets/eb0dd8f9fb33986dba3a.png)

Bir sonraki işlemde iki adımlı doğrulama ayarlarının kullanıcı bazında tanımlanması için **"Genel\>Kullanıcı İşlemleri\>Kayıt"** menüsünden **"İki** **Adımlı** **Doğrulama** **Ayarları"** ekranına girilmelidir. TOTP Ayarları sekmesinde programa giriş yapan kullanıcı için bir gizli anahtar ve QR kod türetilmektedir.

!worddav02fec658f5159f49e67236f037db8bf0.png|height=349,width=236!Mobil cihazdan authenticator uygulamasına giriş yapılarak "QR kodunu tara" seçeneği ile ekrandaki barkod kodu okutulabilir veya "Kurulum anahtarı gir" seçeneği ile ekrandaki "Gizli Anahtar" mobil uygulamadaki alana giriş yapılarak etkinleştirme işlemi tamamlanabilir.

![](../_assets/2bd2cdf688383f0d4754.png)

Etkinleştirme işlemi tamamlandığında "İki adımlı doğrulama başarıyla etkinleştirilmiştir" mesajı alınacak ve uygulama tarafından 7 adet kurtarma kodu türetilecektir. İki adımlı doğrulama sistemini kullanan ve mobil cihazına doğrulama kodu alan bir kullanıcı mobil cihazına erişimini kaybederse, hesabını kurtarmak ekranda belirtilen kurtarma kodlarını kullanmalıdır.

**Önemli:** Mobil cihazınıza erişiminiz yoksa, iki adımlı doğrulamanın etkin olduğu hesapta oturum açmanın yöntemi kurtarma kodu kullanmaktadır. Bu nedenle kurtarma kodlarının "Dışa Aktar" seçeneği ile yedeklenmesi ve saklanması önemlidir.

**Not:** Her kurtarma kodu sadece bir kez kullanılabilir.

![](../_assets/65aa3f75d0741a0a8edf.png)

**Kullanıcı Yönetimi** sekmesi "admin" veya Merkezi Kimlik Yönetimi uygulamasında "İki Adımlı Doğrulama Ayarları Kullanıcı Yönetimi" yetkisine sahip kullanıcılar tarafından görüntülenebilmektedir. Bu sekmede, iki adımlı doğrulama sistemini kullanan kullanıcıların etkinleştirme zamanları gösterilmektedir. Ayrıca, iki adımlı doğrulama sistemini kullanan kullanıcıların "Etkin Mi?" parametresindeki işareti kaldırılarak seçilen kullanıcı için iki adımlı doğrulamanın devre dışı bırakılması sağlanabilir.

!worddav9beec44ed29757bcd38c248668ddfe31.png|height=326,width=228!Kullanıcı bazında iki adımlı doğrulama ayarları tanımlandığında, Netsis Wings veya Netsis masaüstü uygulamasına girişte kullanıcı adı ve şifre bilgisi girildikten sonra doğrulama kodu istenecektir.

!worddav4b4750fc329dd22e9d7572794ea5af62.png|height=346,width=225!Mobil cihazdan authenticator uygulamasına giriş yapılarak alınan kod, doğrulama kodu alanına girilerek uygulamaya daha güvenli bir şekilde başarıyla giriş yapılabilir.
