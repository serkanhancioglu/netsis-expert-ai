---
title: "Farklı Şubeden Sipariş Sevkiyatı"
page_id: "160040266"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Farklı Şubeden Sipariş Sevkiyatı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Farklı Şubeden Sipariş Sevkiyatı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWRhNjBiN2ZmLTE5OTQtNDBiMS04ODQ0LTJkMzc1ZjEzMmQ3MCZsaW5rPTAzYTFlNGQ3LWQwZWQtNDEwYi05MTExLTFhZWExZDlhOGQyNCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=da60b7ff-1994-40b1-8844-2d375f132d70&link=03a1e4d7-d0ed-410b-9111-1aea1d9a8d24&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "farkli-subeden-siparis-sevkiyati_160040266_160040266.html"
source_version: "2024-12-23T09:11:51.177+03:00"
source_bytes: 3132743
fetched_at: "2026-09-13T04:22:26+00:00"
generator: "netsis-scraper 1.0.0"
---
# Farklı Şubeden Sipariş Sevkiyatı

İlgili özelliğin programda kullanılabilmesi için merkez şube içerisinden Satış Parametreleri / Fatura Sipariş sekmesindeki "Farklı Şubeden Sipariş Sevkiyatı Yapılsın" parametresi işaretlenir.

![](../_assets/a18a5190d625f2b32a6c.png)

Bu parametre ile birlikte merkezde ve diğer şubelerde Lokal Depo uygulaması kullanılıyor olması gerekir. İlgili parametre sadece Merkez şubeden işaretlenir.

Farklı Şubeden Sipariş Sevkiyatı Yapılsın parametresi şubelerde pasif, merkezde aktif olarak görünür. İlgili uygulamanın kullanılabilmesi için stokların ve carilerin şubelerde ortak olması gerekir.

Farklı Şubeden Sipariş Sevkiyatı Yapılsın parametresi Merkez içerisinden aktif edildiğinde menüye iki tane yeni ekran gelir. Farklı Şube Sevk Depo Yetkileri ve Farklı Şube Sevk Cari Eşleştirme ekranlarıdır.
![](../_assets/422cb126838f46b48edd.png)

Farklı Şube Sevk Depo Yetkileri ekranında hangi şubeler hangi şubelerin depolarını görebilir olduğu belirlenir. Depodan ürünler talep edildiğinde bilgilendirmelerin nasıl yapılacağı bu ekran ile belirlenir.

![](../_assets/ca407329469374742120.png)

**Yetkili** **Şube** **Kodu:** İlgili şube seçimi yapalır.

**Farklı Şube** **Depo Kodu :** Farklı şubede olan depo kodları seçimi yapılır. Bilgilendirme yöntemi olarak Bildirim Mesajı ve E-posta seçeneği bulunmaktadır.

**Bildirim** **Mesajı** :Kullanıcıların programa giriş yaptığında bildirim merkezinden ilgili mesajların görünmesi sağlanır.

**E-Posta** : Kullanıcılara e-posta gönderilmesi sağlanır.

**Kullanıcılar** : Bildirim yönetimi seçildikten sonra ilgili kullanıcıların seçileceği alandır.Hangi kullanıcılara bildirim gitmesi isteniyorsa bu alandan seçilir.

**Mesaj** **Başlığı** : Bildirimin nasıl bir mesaj ile görüneceği bilgisi girilir.

Farklı Şube Sevk Cari Eşleştirme ekranında yapılan tanımlama sonrası herhangi bir ürün talebinde bulunulduğunda otomatik DAT kaydı oluşur ve burada oluşan DAT kaydı tanımlamaya göre belirlenir.

Şube kodu ve ilgili şubedeki cari koduna karşılık gelerek eşleştirilir.

![](../_assets/1a2c8187b430766faba4.png)

Örnek olarak Şube 1 de Müşteri Siparişi kaydı oluşturuyorum.

![](../_assets/cd920201294d937a4736.png)

İlgili ekranda Stok Depo Kodu alanı Merkez Şubede işaretlemiş olduğumuz Farklı Şube Sipariş Sevkiyatı Yapılsın parametresine bağlı olarak gelir.Rehberden depo seçimi yapılır. İlgili rehberde içinde bulunulan şubenin diğer şubelerdeki hangi depolara yetkisi var ve ne kadar bakiyesi olduğunu gösterir.

![](../_assets/06d2d7e1c7754e885d89.png)

Siparişte girilen miktar eğer seçilen depoda yetersiz ise program "Geçerli ve bakiyesi bulunan bir depo girilmesi gerekmektedir." şeklinde uyarı vermektedir.

![](../_assets/ec10181228fc419ee0af.png)
İlgili depoda yeterli bakiye var ise şube depo kodu seçimi sonrası müşteriye sevk kutucuğu işaretlenirse talep edilen şube direkt ürünleri müşteriye sevk edecek anlamına gelir.

![](../_assets/e3f30c16993dcbac864a.png)

Şubeye gelen talepleri izleyebilmek için Fatura İşlemler altında Farklı Şubeden Sipariş Sevkiyatı ekranı kontrol edilmeldir.

![](../_assets/fda8e3cf79d18d053610.png)

Bu ekranda farklı şubelerden gelen taleplerin listelenmiş hali görünür. İlgili ekranda Kayıtları Getir butonu ile seçim yapılmalıdır.
Listelenen kayıtlar henüz transferi gerçekleşmemiş kayıtlardır.İlgili siparişler için seçim grid ekranından yapılıp DAT oluştur butonuna basılır.
![](../_assets/716ea437e5bdaeebe15d.png)

Bu seçimle birlikte ilgili siparişlerin Depolar Arası Transfer kayıtları oluşur.

DAT kayıtlarını oluştururken öncelikli olarak Sipariş Numarasına ,Cari Koduna ve Müşteriye Sevk olup olmayacağına göre gruplandırma yapılmaktadır.

DAT oluştur butonu ile Yeni Numara Girişi Ekranı açılır.

![](../_assets/2310fe56bdc663e404d1.png)

**Sipariş** **Şube** **Kodu** : Hangi şubeden talep edildiğini gösterir.

**Sipariş** **No** : Hangi sipariş numarasına ait kayıt oluşacağını gösterir.

**Sipariş** **Cari** **Kodu** : Sipariş cari bilgisini gösterir.

**Müşteriye Sevk** : Müşteriye sevk olup olmayacağını gösterir.

**Belge** **No** : İlgili belge numarası girileceği alandır.

**Belge** **Tari**hi : İlgili belge tarihinin girileceği alandır.

Oluşacak olan belge bilgilerine girdikten sonra herhangi bir uyarı alınmadıysa işlem sonucu ekranından Durum bölümünde oluşan DAT kayıtlarının numarası görünür.

![](../_assets/b6e49ead51a2d19fe5b8.png)
