---
title: "Kargo - Gönderi Modülü"
page_id: "163414181"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Kargo - Gönderi Modülü"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Kargo - Gönderi Modülü"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTUxYzlkZWExLThiODAtNDM5Zi05YTM1LTFlMTc1ZGYzZWU1MSZsaW5rPTk0MzNlMTdjLTI4YTAtNDVjMy1hZjkyLTkyMmQ3NjZlYWEzNSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=51c9dea1-8b80-439f-9a35-1e175df3ee51&link=9433e17c-28a0-45c3-af92-922d766eaa35&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "kargo-gonderi-modulu_163414193_163414181.html"
source_version: "2025-01-06T10:38:04.550+03:00"
source_bytes: 1789298
fetched_at: "2026-09-13T04:22:20+00:00"
generator: "netsis-scraper 1.0.0"
---
# Kargo - Gönderi Modülü

Kargo Modülü sayesinde işletme içinde satışa yönelik yapılan işlemler, dağıtım şirketleri ile entegre edilir. Tasarlanan yapı ile satış faturası veya irsaliyesiyle entegrasyon sağlanır. Diğer modüller ile bütünleşik çalışan Kargo Modülü sayesinde satış irsaliyesi ve faturası oluşturulduktan sonra işlemler otomatik olarak kargo sürecine aktarılır. Kargo aktarımında kullanılmak üzere dizayn modülü üzerinden görsel dizayn hazırlanarak basım işlemleri gerçekleştirilebilir.

Kargo modülü Netsis 7.0 ve üzeri onaylı sürümlerde kullanılabilmektedir. Kargo modülü ile ilgili uygulama ve dil dosyaları: Ephesus.exe, Kargo.dll, Kargodzn.dll, Fatura.dll, Dzyntrk.dll, Kultrk.dll ve Nettk.dll dosyalarıdır.

### Kargo Kullanıcı Kayıtları

Kargo Kullanıcı Kayıtları, Lojistik- Satış Bölümü'nde Kayıt/Kargo-Gönderi menüsünün altında yer alır.

Netsis-Kargo Kullanıcı Tanımları ekranında, kargo şirketlerine yapılacak işlemlerde kullanılmak üzere kargo şirketi tarafından verilen kullanıcı adı ve şifre bilgileri, netsis kullanıcı bilgileri ile eşleştirilir.

![](../_assets/6493c36386c19b0c4146.png)

## Netsis Kullanıcı Bilgileri

**Kullanıcı** **No:** Kargo Kullanıcısı ile eşleştirilecek olan Netsis kullanıcı numarasının girildiği alandır.

## Kargo Kullanıcı Bilgileri

**Kargo** **Şirketi:** Listeden kargo şirketi seçilir. (Yurtiçi ve UPS Kargo desteklenmektedir.)

**Kullanıcı** **Adı:** Kargo şirketi tarafından verilen kullanıcı adının girildiği alandır.

**Şifre:** Kargo şirketi tarafından verilen kullanıcıya ait şifrenin girildiği alandır.

**Karakter** **Göster:** Girilen şifrenin doğruluğunun kontrolü için karakterlerin gösterilmesini sağlayan parametredir.

### [Gönderi Oluştur](<../Kullanıcı Dokümanları/Lojistik - Satış/Kargo - Gönderi/İşlemler - Kargo - Gönderi/Gönderi Oluştur.md>)

Lojistik - Satış\\Kargo-Gönderi\\İşlemler menüsünün altında yer alır.

Fatura Modülünden girilen "Satış Faturası" veya "Satış İrsaliyesi" belgelerinin kargo şirketlerine gönderiminin yapılmasını sağlar.

**Kargo** **Şirketi:** Kargonun gönderileceği kargo şirketi seçilir.

**İrsaliye/Fatura:** Kargo gönderilecek belge tipi seçilir.

**Fatura** **Numarası:** Seçilen belge tipine göre kargo gönderilecek irsaliye/fatura numarasının girildiği alandır.

![](../_assets/867ca2861c8d9b36c91e.png)

Kargo şirket seçimi, belge tipi ve numarası girişi sonrasında kargo bilgilerinin, kargo portalına gitmesi için **"Kargo** **Gönder"** butonuna basılır.

Kargo gönderimi işleminin yapılması sonrasında kullanıcı ve mevcut kargo bilgilerinin sorgulandığı login ekranı açılacaktır. Kargo kullanıcı bilgileri sistemde yapılan tanımlama mevcut ise otomatik olarak getirilir. Bu ekranda Kargo Bilgileri kısmında kargo sayısı girilir. Örneğin, belgedeki stok kalem sayısı 1 olsun. Kargo 2 paket halinde gitmesi durumunda kargo sayısı olarak 2 girilmelidir.

![](../_assets/1963b73d3027d5a31c03.png)

**Yanıt** **Xml:** Kargo gönderimi sonrasında Kargo şirketi tarafından gönderi ile ilgili gelen yanıt xml olarak gösterilir.

**Sonuç Açıklama:** Kargo şirketinden gelen cevabı gösteren alandır. Gönderim sırasında herhangi bir hata söz konusu değilse "Başarılı" cevabı gelir. Gönderim sırasında hata oluşmuşsa hata ile ilgili açıklama görünür.

## Dikkat Edilmesi Gereken Tanımlamalar;

Satış işlemleri sonrası, Kargo şirketlerine yapılan aktarımların hatasız sonuçlanması için mevcut Cari (Alıcı) kartlarının düzenlenmesi gerekmektedir.

Cari Hesap Kayıtları ekranında cari isim minimum 5 karakter olmalı en az 4 harf içermelidir.

Cari Adres: Kargonun gönderildiği sevk adresidir. Minimum 5 (Harf/rakam) maksimum 200 karakter olmalıdır.

Telefon: Alan kodu ile 10 adet rakamdan oluşmalıdır.

![](../_assets/df63f9205106c23af8e8.png)

# [Gönderi İptal](<../Kullanıcı Dokümanları/Lojistik - Satış/Kargo - Gönderi/İşlemler - Kargo - Gönderi/Gönderi İptal.md>)

Kargo şirketlerine iletilen belgelerin iptaline yönelik bildiriler bu ekrandan yapılmaktadır. İptal talebinin sonrasında kargo şirketlerinden alınan sonuçlar (kargo teslim durumuna göre), ekrana getirilmektedir.

Kargo Şirketi, belge tipi ve numarası girildikten sonra gönderimin iptali için **"Kargo** **Gönderimini** **İptal** **Et"** butonuna basılır.

Butona basıldıktan sonra **"Kargo** **Gönderimi** **İptal** **Edilecek.** **Emin** **misiniz?"** sorusunun onaylanması gerekir.

Kargo iptal işleminin yapılmasından sonra kullanıcı ve mevcut kargo bilgilerinin sorgulandığı Yurt İçi Kargo/Ups Kargo Login Ekranı açılır. Kargo kullanıcı bilgileri sistemde yapılan tanımlama mevcut ise otomatik olarak tespit edilir.

Login ekranını geçtikten sonra kargo şirketi tarafından iptal işlemi için gönderilen cevap bilgisi grid ekranında görülür.

![](../_assets/d64528426ee6c0d9e465.png)

![](../_assets/4f35205f02c18428226c.png)

![](../_assets/096a60ce51c6b8e63043.png)

# ![](../_assets/4707425741862536ff6d.png)

# [Kargo Bilgilerinin Basımı](<../Kullanıcı Dokümanları/Lojistik - Satış/Kargo - Gönderi/İşlemler - Kargo - Gönderi/Kargo Bilgilerinin Basımı.md>)

Lojistik - Satış\\Kargo-Gönderi\\İşlemler menüsünün altında yer alır.

Kargo şirketlerine fiziki olarak iletilecek dokümanların oluşumu ve basımının yapılmasını sağlar.

![](../_assets/b113da92f53cdf7e816c.png)

![](../_assets/2d57e89d17712ce4ed39.png)

Dizayn tipi "Kargo Basımı" seçilip, KARGOISLEMOTR viewı kullanılarak görsel dizayn oluşturulabilir ve basım alınması sağlanabilir.

Kargo modülünün fatura modülü içerisinden entegre kullanımı için aşağıdaki özel parametre tanımlanabilir.

Grup Kodu: FATURA Anahtar: KARGO_KULLANIM Değer: 0

Özel parametre tanımlaması sonrasında fatura ve irsaliye belgesinin toplamlar sekmesinde "**Kargo** **Kullanılsın**", "**Kargo Basımı**", "**Kargo Şirketi**" parametreleri gelmektedir. Bu parametreler kullanılarak Kargo modülüne gitmeden de direkt fatura üzerinden kargo gönderimi sağlanabilir.

![](../_assets/3f4529eece479accb36f.png)

Ek olarak daha önce kargosu gönderilmiş bir belge için tekrar kargo gönderimi ile ilgili program içerisinde kontrol yapılmaktadır. Kargo tekrar gönderilmek istendiğinde ekrana "Girilen Belge Daha Önce Gönderilmiş durumdadır" yazılı uyarı ekranı çıkmaktadır ve gönderim işlemi sonlandırılmaktadır.

**NOT:** Kargo modülü için TBLKARGOISLEM, TBLKARGOKULLANICI tabloları ve KARGOISLEMOTR, KARGOKULLANICI, KARGOKULLANICIEKR viewları kullanılmaktadır.
