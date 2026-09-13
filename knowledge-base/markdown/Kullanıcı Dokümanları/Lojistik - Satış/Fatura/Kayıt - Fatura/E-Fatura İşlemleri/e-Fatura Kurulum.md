---
title: "e-Fatura Kurulum"
page_id: "47084867"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Fatura"
  - "Kayıt / Fatura"
  - "E-Fatura İşlemleri"
  - "e-Fatura Kurulum"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Fatura / Kayıt / Fatura / E-Fatura İşlemleri / e-Fatura Kurulum"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWU2NzkyMzVhLTQxYzItNDEyYy1hNzcxLTFkZTEzZmI4N2UyMyZsaW5rPWE5MjdmNTRlLTM2MjctNGM0My1hMWQ4LWI0MTdlZWE5MWJlNiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=e679235a-41c2-412c-a771-1de13fb87e23&link=a927f54e-3627-4c43-a1d8-b417eea91be6&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "e-fatura-kurulum_47084869_47084867.html"
source_version: "2022-10-24T12:33:40.033+03:00"
source_bytes: 4278
fetched_at: "2026-09-13T04:01:53+00:00"
generator: "netsis-scraper 1.0.0"
---
# e-Fatura Kurulum

e-Fatura kurulumunun yapılabilmesi için, öncelikle e-Fatura lisansının satın alınması gerekir.

3 çeşit lisans vardır. Lisans çeşitleri şunlardır; e-Fatura Entegratör -Logo, Cybersoft, Veriban, Vakıfbank, Akbank, Isis, e-Fatura Online ve e-Fatura Offline.

İhtiyaca yönelik olan lisans satın alınarak kurulum işlemlerine başlanır ve aşağıdaki adımlar takip edilir:

- Merkezi Kimlik Yönetimi (SSO) ekranından yüklemesi yapılır. Temel Set lisanslarının içine satın alınan lisans gelir.
- Lisans indirildikten sonra ilk fatura gönderilmeden önce programdan bazı tanımlamaların yapılması gerekir.
- Netsis Servis klasöründe bulunan "EFaturaAyarlar.exe" klasörüne tıklandığında görüntülenen "Netsis e-Devlet Ayarları" ekranından e-Devlet ayarlarının ve mühür tanımlamalarının yapılması gerekir.

**Örneğin;** Mühür kullanımı olacaksa ve imzalama işlemini kullanıcının bağlı olduğu firma yapacaksa "Netsis e-Devlet Ayarları" ekranından "Yeni Sertifika Tanımlama" seçeneği ile Cihaz Bilgileri (Mühür Bilgileri) tanımlanır. Mührün kullanılması için AKIS Uygulamasının kurulması gerekir. Bu program aracılığı ile sertifika ve mühür bilgileri okunur. Bu aşamadan sonra ekrana mührün slot bilgileri ve şifresi gelir. "Yenile" butonuna tıklandığında mührün Sertifika Bilgileri, Genel Anahtar Bilgileri ve Özel Anahtar Bilgileri listelenir.

Entegratör lisansının olduğu varsayıldığında, Entegratör Kullanıcı Bilgilerinin de girilmesi gerekir. Logo tarafından verilen Kullanıcı Adı ve Şifre bilgisi girilip kaydedildiğinde, portala bilgi aktarımı yapılır. Portal da gelen faturaları GİB'ne gönderme işlemini yapar. Burada yer alan "Şube Bazında Değerlendir" yazısına tıklandığında - Entegratör kullanan firmalar için geçerli - bir firma için birden fazla portal tanımının şube bazında yapılması sağlanır.

"Netsis e-Devlet Ayarları" ekranından "Var Olan Ayarlar" seçeneği ile, daha önceden tanımlanan ayarları takip edip, değişikliklerin kaydedilmesi, kontrol edilmesi, kopyalanması veya silinmesi sağlanır.

"Netsis e-Devlet Ayarları" ekranından "Efatura.dll Kayıtla" seçeneği ile, kullanılan e-Fatura dosyasının programa kayıtlanması sağlanır.

"Netsis e-Devlet Ayarları" ekranından "Web Servis Ayarları" seçeneği, online e-Fatura için kullanılır.

Lisans yüklendikten sonra programa giriş yapılır.

Faturaların sağlıklı gönderilmesi için GİB'nin bazı standartları vardır. Bu standartlara göre fatura gönderilmesi gerekir.

**Örneğin;** Ölçü Birimi, Döviz Birimi Tanımlama gibi.

Fatura → e-Fatura İşlemleri → e-Fatura Parametreleri → "e-Fatura Uygulaması Kullanılsın" parametresinin işaretlenmesi ile e-Fatura bölümleri aktif hale gelir.

Kurulum işlemleri tamamlandıktan sonra, [e-Fatura Parametreleri](<e-Fatura Parametreleri.md>) ekranından gerekli tanımlamaların yapılması gerekir. İlgili tanımlamalar yapıldıktan sonra e-Fatura kullanımına geçilir.
