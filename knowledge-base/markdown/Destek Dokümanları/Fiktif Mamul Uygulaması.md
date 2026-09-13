---
title: "Fiktif Mamul Uygulaması"
page_id: ""
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Fiktif Mamul Uygulaması"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Fiktif Mamul Uygulaması"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTk0NGU4MDRkLTMwOTYtNGYzNC1iN2JhLTYxMzY2Y2QwNDk2OCZsaW5rPTU5MTRhZDFmLTgxM2YtNDQ0NC05NDg1LWM2YWY3NjE4NDVhMyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=944e804d-3096-4f34-b7ba-61366cd04968&link=5914ad1f-813f-4444-9485-c6af761845a3&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "fiktif-mamul-uygulamasi.html"
source_version: ""
source_bytes: 7988
fetched_at: "2026-09-13T04:21:47+00:00"
generator: "netsis-scraper 1.0.0"
---
# Fiktif Mamul Uygulaması

Bu dokümanda, üretim modülünde fiktif mamul kullanımına ilişkin uygulama detaylarına yer verilecektir.

Bazı üretim senaryolarında, hammadde veya yarı mamullerin işlenmesi sonucunda birden fazla mamul ortaya çıkabilmektedir. Bu durumda, aynı reçetede yer alan bileşenlerin sarf edildiği mamuller, bileşen bazında farklılık gösterebilir.

Örneğin, rulo kâğıt ve boya kullanılarak aynı anda hem antetli hem de antetsiz kâğıt üretiliyorsa; rulo kâğıt bileşeni her iki mamule de sarf edilmektedir.

Mevcut sistemde, reçete tanımlama bölümünde bileşenler yalnızca tek bir mamule atanabildiğinden, bu tür senaryoları desteklemek amacıyla fiktif bir mamul tanımlanır. Bu fiktif mamulün reçetesi üzerinden, bileşenlerin ve bu bileşenlerin sarf edildiği mamullerin ilişkisi tanımlanır. Üretim sonu kayıtlarında da fiktif mamul kullanılarak hem birden fazla mamulün aynı anda üretimi hem de bileşenlerin sarfı sağlanır.

Fiktif mamul uygulaması için öncelikle stok modülünde bir stok kartı oluşturulmalı ve bu kartın "Ek Bilgiler" sekmesinde yer alan “**Fiktif Mamul”** parametresi işaretlenmelidir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/a3cb002c-fe37-4e0e-9d45-0b6442a9b193/fiktif1.png)

Ardından, fiktif mamule ait bir reçete tanımlanmalıdır.

**Reçete Kaydı**

Fiktif mamul uygulaması kapsamında, reçete kayıtlarına **“Sarf Edilen Mamul Kodu”** alanı eklenmiştir. Bu alan yalnızca “Fiktif Mamul” parametresi işaretli stoklar için reçete tanımlanırken aktif hale gelir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/8d1c23b1-3fa9-4448-bb0f-e2d94a5c2fb2/fiktif2.png)

Her bir bileşen için, “Sarf Edilen Mamul Kodu” alanına, bileşenin sarf edildiği mamul(ler)in kodu girilmelidir. “Miktar” alanına ise, ilgili mamule sarf edilecek miktar yazılır.

Örneğin:

• Rulo kâğıt bileşeni için “Sarf Edilen Mamul Kodu” alanına hem antetli hem de antetsiz kâğıt girilir.

• Boya bileşeni sadece antetli kâğıt için tanımlanır.

Üretilen mamulleri tanımlamak amacıyla, **URETIM** kodlu bir stok kartı açılır. Bu kart, fiktif mamul reçetesi içinde, hangi mamullerin üretileceğini belirler. Üretilen tüm mamuller için, bileşen kodu “URETIM” olan, “Sarf Edilen Mamul Kodu” sahasında, üretilen mamulün kodu yazan satırlar girilmelidir.

Örneğimizde; bileşen kodu “URETIM” olan ve sarf edilen mamul kodları antetli ve antetsiz kâğıt olan iki satır yer almalıdır.

URETIM kodlu stok kartı ile ilgili dikkat edilecekler;

• Yalnızca “Fiktif Mamul” parametresi işaretli stokların reçetesinde bileşen olarak kullanılabilir.

• Kendisine reçete tanımlanamaz.

• Alternatif malzeme olarak tanımlanamaz ve kullanılamaz.

Fiktif Mamuller ile ilgili dikkat edilecekler;

• Alternatif politika, öncelik ve planlama oranı tanımlanamaz.

• Operasyon tanımı yapılamaz.

• Planlama yapılamaz. (MRP I ve MRP II)

• Üretim Planı Dengeleme yapılamaz.

• Ters Üretim Sonu Kaydı yapılamaz.

• Planlanan Bileşen Değişikliği (Revizyon) yapılamaz.

• Anlık Üretim Planlama yapılamaz.

• Bütçe Planlama yapılamaz.

Fiktif mamulün reçetesindeki üretilen mamuller için planlama (MRP I ve MRP II) yapılacaksa, her mamul için ayrıca reçete tanımlaması yapılmalıdır.

**Üretim Sonu Kayıtları**

Üretim sonu kayıtları sırasında, mamul kodu alanına fiktif mamulün kodu yazılmalıdır. Üretim sonu kaydının tamamlanması ile fiktif mamule herhangi bir giriş çıkış yapılmaz. Reçetede, “Sarf Edilen Mamul Kodu” sahası dolu olan hammadde ve yarı mamullerden çıkış (-), bileşen kodunda URETIM yazan mamuller için ise giriş (+) yapılır.

```text
Örneğin;
Reçeteye göre:
•    Girdi: 2 rulo kâğıt ve 10 gr boya
       o    1 rulo antetli, 1 rulo antetsiz kâğıt için
       o    10 gr boya sadece antetli kâğıt için
•    Çıktı: 30 adet antetli, 30 adet antetsiz kâğıt
```

Stok Kodu: ANTETLI KAGIT----Stok Adı: ANTETLI KAGIT

Stok Kodu: ANTETSIZ KAGIT ---Stok Adı: ANTETSIZ KAGIT

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/455f4ed7-4928-4770-9d89-e4e0d3d13c1e/fiktif3.png)

1 adet fiktif mamulün üretime girmesi sonunda oluşan üretim sonu raporu aşağıdadır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/6754408e-2ccf-4a77-b14b-316c19b31f9a/fiktif4.png)

Rapora göre; 10 gr. boya ve 2 rulo kâğıt harcanmış, 30 adet antetli ve 30 adet antetsiz kâğıt üretilmiştir. Fiktif mamule ise herhangi bir giriş/çıkış yapılmamıştır.

**Serbest Üretim Sonu Kayıtları**

Serbest üretim sonu kayıtları sırasında, mamul kodu alanına, fiktif mamulün kodu yazılmalıdır. “Fiş Üret” butonuna basıldığında, fiktif mamule herhangi bir giriş/çıkış yapılmaz. Reçetede, “Sarf Edilen Mamul Kodu” sahası dolu olan hammadde ve yarı mamullerden çıkış (-), bileşen kodunda URETIM yazan mamuller için ise giriş (+) yapılır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/14ef78c6-0e95-4a92-a4fc-2eb8120aabfb/fiktif5.png)

Serbest üretim sonu kaydında, fiktif mamulün reçetesine yeni bir bileşen ya da mamul eklenebilir, çıkarılabilir ya da miktarı değiştirilebilir.

**Bileşen** eklenmesi durumunda, giriş/çıkış sahasında **çıkış** seçilmeli ve Açıklama sahasına, bileşenin sarf olduğu mamul kodunu girilmelidir.

**Mamul** eklenmesi durumunda, giriş/çıkış sahasında **giriş** seçilmeli, Açıklama sahası program tarafından “Uretim” olarak belirlenecek ve değiştirilemeyecektir.
