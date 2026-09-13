---
title: "Kişisel Koruyucu Donanım Yönetimi"
page_id: "108659361"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Kişisel Koruyucu Donanım Yönetimi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Kişisel Koruyucu Donanım Yönetimi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWFiZmJkM2RjLTg3MzctNDZiOC05NzRhLTg5MzdhZmI5MDIxMSZsaW5rPTMxYTYzMThjLTJmODQtNDc4Ny04ZWExLWEzYmY2NjVjYmUwZSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=abfbd3dc-8737-46b8-974a-8937afb90211&link=31a6318c-2f84-4787-8ea1-a3bf665cbe0e&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "kisisel-koruyucu-donanim-yonetimi_108659370_108659361.html"
source_version: "2023-03-31T10:14:13.710+03:00"
source_bytes: 647887
fetched_at: "2026-09-13T04:23:30+00:00"
generator: "netsis-scraper 1.0.0"
---
# Kişisel Koruyucu Donanım Yönetimi

9.0.42 sürümü ile sürdürülebilirlik kapsamında Kişisel Koruyucu Donanım Ekipmanları' nın program içerisinde tanımlanması ve takibi desteklenmiştir. Kişisel koruyucu donanım yönetimiyle ilgili ayrıntılı bilgiye bu dokümandan ulaşılır.

Üretim sırasında gerçekleşen operasyonlarda kullanılan iş elbisesi, baret, gözlük, ayakkabı vb. kişisel koruyucu ekipmanların tanımlanıp operasyonlarla eşleştirilip Üretim Akış Kaydı sırasında kullanıcıların isteğe bağlı uyarı almasını sağlanabilir.

**Kişisel Koruyucu Donanım Grubu Tanımlama**

Kişisel Koruyucu Donanım Grubu Tanımlama ekranı ile takibi yapılmak istenilen kişisel korucu donanım grupları tanımlanabilir ve malzeme eşleştirmeleri yapılabilir.

Mesaj politikaları ile üretim akış kaydı sırasında uyarı mesajının gösterilmesi, uyarı mesajının gösterilmesi ve onay alınması sağlanabilir ya da hiçbir uyarı mesajının gelmemesi seçimi de yapılabilmektedir.

![](../_assets/3bf0f628c7bc44294707.png)

Mesaj: Bu alanda ise mesaj politikasına uygun istenilen mesaj girilebilmektedir.

KKD Grubu Malzeme Eşleştirme: Bu sekme üzerinden ilgili Kişisel Koyucu Donanım (KKD) Grubu için kullanılacak olan donanımların stoklar ile eşleşmesi sağlanmaktadır.

- "Henüz eşlenmeyen stoklar getirilsin" parametresi ile herhangi bir KKD grubu ile eşlenmemiş olan stoklar listelenir.
- "Kayıtları Getir" butonu ile verilen kısıtlara uygun stoklar listelenir.
- "Eşlenenleri Getir" butonu ile verilen kısıtlara uygun daha önceden KKD grubu ile eşlenmiş kayıtlar varsa sadece bu kayıtların gelmesi sağlanır.

Gridde listelenen stoklar arasından seçim yapılarak "Değişiklileri Kaydet" butonu ile eşleştirme tamamlanacaktır.

![](../_assets/cc1e931ab92d01778623.png)

**Operasyon – KKD Grubu Eşleştirme**

MRP\> Kayıt ve Üretim\>Kayıt altında yer alan "Operasyon Tanımlama" ekranlarına "Kişisel Koruyucu Donanım Grubu" alanı eklenmiştir. Bu alanda seçilen KKD Grubu "Üretim Akış Kaydı" ekranlarında kullanılır.

![](../_assets/335549c9951887f07789.png) ![](../_assets/f6dc5cc4f4ce0309688c.png)

Üretim akış kayıtlarında ilgili operasyonların kullanımı sırasında KKD grup tanımlarına göre mesaj politikası var ise kullanıcının karşısına ilgili mesajlar çıkmaktadır.

1. "Mesaj Göster ve Onay Al" politikası seçildiğinde kayıt esnasında gelen uyarı ekranında, uyarı altında "Evet/Hayır/İptal butonları yer alır. Kullanıcının tıkladığı butona göre bu onay bilgisi ayrı bir tabloda tarih/saat ve belge detayında kullanıcı bazında TBLUAKMAS_KKDONAY tablosunda saklanmaktadır. Kullanıcı belge kaydı esnasında bu tür bir mesajla karşılaştığında onay alınmadan işlemi tamamlayamaz. "Evet" ya da "Hayır" onayı verildikten sonra, onay bilgisi veri tabanında tutulup, işleme devam edilebilir.
2. "Sadece Mesaj Gösterilsin" politikasında gelen uyarı ekranında ise sadece "Tamam" butonu gelmektedir.

![](../_assets/78c72b6f3f531f2e06be.png)
![](../_assets/b4554a4791f41475eb80.png)

**Sürdürülebilirlik 360**
Sürdürülebilirlik 360 ekranlarında ise KKD Grupları ve detaylarına ait gösterimlere kolaylıkla ulaşılabilir.

- En Sık Kullanılan Kişisel Koruyucu Donanım Grupları- Verilen tarih aralığı için "Kişisel Koruyucu Donanım Grubu Tanımlama" ekranından girilen ve stoklarla eşleştirmesi yapılmış kişisel koruyucu malzemeleri için en çok kullanılan 5 donanım grubunun pasta grafiğinde yer alır.
- En Sık Kullanılan 50 Kişisel Koruyucu Donanım Grubu- Detayda grid bölümde en sık kullanılan 50 adet kişisel koruyucu donanım grubunun sayısı gösterilir.
- En Sık Kullanılan Kişisel Koruyucu Donanım Malzemeleri- Verilen tarih aralığı için "Kişisel Koruyucu Donanım Grubu Tanımlama" ekranından girilen ve stoklarla eşleştirmesi yapılmış kişisel koruyucu malzemeler için en çok kullanılan 5 donanım grubuna bağlı stoğun pasta grafiğinde yer alması sağlanır.
- En Sık Kullanılan 50 Kişisel Koruyucu Donanım Malzemesi- Detayda grid bölümde en sık kullanılan 50 adet kişisel koruyucu donanım grubuna dahil stoğun UAK'ta geçen kullanım sayısı gösterilir.

![](../_assets/9a51c69f0a7082de7edc.png)
![](../_assets/b7d5324cd0c53492657b.png)
