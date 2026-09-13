---
title: "Online Hesap Özeti SSS"
page_id: "90669073"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Online Hesap Özeti SSS"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Online Hesap Özeti SSS"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTM0MDhiMTQyLTE3ZWYtNGFkYy1iNjI1LTcxNjJjMTQ2ZjQwZSZsaW5rPTkyNDQ5YjFiLWI4YWItNGE4ZC1iNzA2LWYxNGNlYzU2Y2EwMiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=3408b142-17ef-4adc-b625-7162c146f40e&link=92449b1b-b8ab-4a8d-b706-f14cec56ca02&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "online-hesap-ozeti-sss_90670209_90669073.html"
source_version: "2022-11-03T09:39:33.160+03:00"
source_bytes: 274306
fetched_at: "2026-09-13T04:23:57+00:00"
generator: "netsis-scraper 1.0.0"
---
# Online Hesap Özeti SSS

**Online** **Hesap** **Özeti** **uygulaması** **hangi** **ürünler** **ile** **birlikte** **kullanılabilir?**

Netsis3 Standart, Netsis3 Entegre, Netsis3 Enterprise ve Netsis Wings Enterprise ürünlerinde kullanılır. Online Hesap Özeti uygulaması kullanımı için önerilen minimum versiyonumuz 9.0.38 'dir.

**Satın** **alma** **işlemleri** **nasıl** **gerçekleşir?**

Online Hesap Özeti uygulamasının kullanılabilmesi için sipariş portali [https://siparis.elogo.com.tr/](https://siparis.elogo.com.tr/) adresi üzerinden aylık veya yıllık paket alımı yapılır.

**Uygulama** **nasıl** **aktif** **edilir**?

Satın alma işlemi tamamlandıktan sonra Netsis ana ekrandan eklenti ekle adımından, Logo Store'dan yükle seçeneği ile uygulama yüklenir ve ilk girişte gelen sözleşme onaylanarak aktif hale getirilir.

**Online anlaşma olan bankalarımız uygulamaya nasıl eklenir?**

Online Hesap Özeti uygulamasına ilk girişte gelen banka ekle seçeneğinden ya da daha sonra Banka Entegrasyonları ekranından eklenir. Banka Entegrasyonları ekranında banka tarafından verilen bilgiler girilerek bağlantı kur butonu ile kaydedilir.

**Banka başvuru formlarına nasıl ulaşabilirim?**

Banka başvuru formları sipariş portali [https://siparis.elogo.com.tr/](https://siparis.elogo.com.tr/) adresi üzerinden paket alım ekranından indirilir.

**Bağlantı kurduğumuz bankaları Netsis ERP tarafında tanımladığımız bankalar ile nasıl eşleştirmeliyiz?**

Bankadan verilen bilgi doğrultusunda bankanın Netsis ERP tarafındaki tanımında IBAN ya da Banka Hes. No alanı üzerinden eşleştirme sağlanır.

Örnek görselde iki kullanım şekli mevcuttur. Örnekte görüleceği gibi hesap bilgisinde bulunan veriler | işareti ile ayrılarak yazılır.

![](../_assets/c00a2710c78f33384bf4.png)

**Aktarılacak kayıtların Netsis ERP'de kayıtlı cari muhasebe hesapları ile otomatik eşleşmesi sağlanabilir mi?**

Eşleştirme işlemi aktarım anında manuel yapılmaktadır. Sadece çek, senet ödeme hareketlerinde açıklamada bulunan seri no üzerinden çek senet numarası otomatik olarak bulunur.

**Fiş türünün işlem açıklamasına göre otomatik belirlenmesi sağlanabilir mi?**

"Eşleşme Parametreleri" ekranından, hesap hareketlerinde belirlediğiniz şekilde işlem koduna göre veya işlem açıklamasına göre fiş türü belirlenir.

**Ekstre aktar işleminde "Eksik bilgi bulunuyor" uyarısı ne anlama gelir?**

Kaydın ERP'ye aktarılabilmesi için gerekli tüm sahalar doldurulmamıştır.

**Ekstre aktar işleminde "Kaydedilebilir" uyarısı ne anlama gelir?**

Kayıt Netsis ERP'ye aktarılabilir durumdadır.

**Ekstre aktar işleminde "Eşlendi" uyarısı ne anlama gelir?**

Netsis ERP'ye daha önceden aktarılmış bir kayıt olduğu anlamına gelir.

**Aktarım esnasında "Hata kodu :500 Detay hata kodu:700" neden alınır?**

Veri Netsis'e akarken ERP tarafında eksik bir tanımdan dolayı alınır. Hatanın detayında cari / banka entegre edilemedi gibi bir açıklama vardır. Bu gelen detay doğrultusunda hesap kartlarının muhasebe bağlantıları kontrol edilir.

**Aktarım esnasında "Hata kodu :500 Detay hata kodu:500" neden alınır?**

Hatanın detayında verilen açıklama yönlendirici olur. Örneğin kayıt yapmaya hakkınız yok uyarısı ile modül ve program numarası detayı ile hata açıklaması oluşur. Netsis ERP tarafında hatada geçen modül ve programa yetki verilmelidir.

**Ekstre aktar dedikten sonra "Banka Hesap kodu bulunamadı. Banka hesap kayıtlarında ZZZZZZ iban nolu hesabı kontrol ediniz" uyarısı neden alınır?**

Ekstre aktarda seçtiğimiz bankaya ait IBAN/Hesap no bilgisi ile Netsis ERP tarafında eşleşen bir banka bulunamadığında alınır.

**"Dekont seri no bilgisi zorunludur" uyarısı neden alınır?**

Aktarım ile oluşacak olan dekonların hangi seriden oluşacağı önceden tanımlanır. Bu tanım Ayarlar ekranı fiş ayarları üzerinden yapılır. Fiş tipi için bir dekont serisi girilmedi ise bu uyarı alınır.

**Aktarılan kayıt geri alınabilir mi?**

Aktarılan kayıt Netis ERP tarafından silindikten sonra Hesap Özeti Aktarım ekranı üzerinde tekrar aktarılabilir hale gelir.

**Admin olmayan bir kullanıcıya Online Hesap Özeti uygulama yetkisi nasıl verilir?**

Netsis ERP'ye admin hakkı olan bir kullanıcı login olup Eklenti Ekle ekranına ulaşır. Bu ekrandan App Yetkilendirme butonu ile App Yetkilendirme ekranına ulaşılır. Açılır listeden eLogoBankingNetsis Elogo Online Hesap Özeti uygulaması seçilip Ekle butonu ile tüm kullanıcılar eklenir ve kaydedilir. Daha sonra açılır listeden App Erişim Yetkileri seçilir ve yetki verilecek kullanıcının eLogoBankingNetsis Elogo Online Hesap Özeti Uygulaması kutucuğu işaretlenir. Son olarak bu kullanıcı ile Netsis ERP'ye giriş yapılır ve Eklenti Ekle ekranı açılır. Kullanılabilir ekler ekranından eLogoBankingNetsis Elogo Online Hesap Özeti Kullanımda seçeneği işaretlenip kaydedilir.
