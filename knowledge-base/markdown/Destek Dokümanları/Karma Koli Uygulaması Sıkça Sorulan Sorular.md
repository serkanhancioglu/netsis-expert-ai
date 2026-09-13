---
title: "Karma Koli Uygulaması Sıkça Sorulan Sorular"
page_id: "50684982"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Karma Koli Uygulaması Sıkça Sorulan Sorular"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Karma Koli Uygulaması Sıkça Sorulan Sorular"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWU2NWY4MGIwLTYyZDgtNGQzZi1iZjlhLTRkZThiODhmOTk4NSZsaW5rPWE3YjdjYmNhLTRkODctNDZmZi05YTA3LWEyMjg5NTVkN2NkNSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=e65f80b0-62d8-4d3f-bf9a-4de8b88f9985&link=a7b7cbca-4d87-46ff-9a07-a228955d7cd5&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "karma-koli-uygulamasi-sikca-sorulan-sorular_80090642_50684982.html"
source_version: "2022-05-25T11:22:36.090+03:00"
source_bytes: 4610
fetched_at: "2026-09-13T04:25:21+00:00"
generator: "netsis-scraper 1.0.0"
---
# Karma Koli Uygulaması Sıkça Sorulan Sorular

**Karma koli nedir? Program genelinde karma koli uygulamasını nasıl aktif hale getirebilirim?**

Birden fazla ürünün bir araya getirilerek, tek bir ürün halinde satılması durumunda, koliyi oluşturan ürünlerin çıkışının ve takibinin yapılabilmesi için kullanılan uygulamadır. Stok parametrelerinde Karma Koli Uygulaması parametresinin işaretlenmesi gerekmektedir.

**Fatura işlemleri sonrasında karma koli stok hareketlerinden giriş/çıkış işlemi** **yapılması isteniyorsa ne yapılmalıdır?**

Karma Koli Kayıtları ekranında tanımlama sırasında “Bilgi Amaçlı” parametresinin işaretlenmesi gerekmektedir. Aksi takdirde karma koli bileşenlerin hareketlerinden giriş/çıkış işlemi yapılır.

**Stok Kartı Kayıtlarında tanımlı her stok kodu karma koli stoğu olarak kullanılabilir mi?**

Stok hareket kayıtlarında hareketi olan stok, karma koli stoğu olarak tanımlanamaz. Tanımlanmak istediğinde kaydetme esnasında “Sthar’da kullanılan karma koliye bileşen eklenemez!” uyarı ekranı gelir ve kaydetme işlemi program tarafından engellenir.

**Karma Koli kayıtları ekranında bileşenlere ait oran hesaplaması nasıl yapılır?**

Karma Koli Kayıtları ekranında "Fiyat" alanı dolu ise, "Oran" alanı boş bırakılabilir. Bu durumda oranın, “Oran Hesapla” butonu kullanılarak hesaplatılması gerekir. "Fiyat" alanı boş bırakılmışsa, "Oran" alanının mutlaka dolu olması ve bileşen oran toplamlarının 100 değerini tamamlaması gerekir.
Her bir bileşen için bu oran: \[(bileşen miktarı \* bileşen fiyatı) / toplam (miktar \* fiyat)\]\*100 şeklinde hesaplanmaktadır.

**e-Belge basımlarında karma koli stok ve bileşenleri aynı anda basılır mı?**

Dizayn tanımı içinde “Kid Master Kodu Basılsın Mı?”, “Kid Bileşen Kodu Basılsın Mı?” parametreleri e-Belge basımlarında da kullanılmaktadır. Karma Koli bileşenlerinin basımı için dizayn içinde “Kid Bileşen Kodu Basılsın Mı?” parametresi işaretli olmalıdır. Karma Koli stokunun basımı için dizayn içinde “Kid Master Kodu Basılsın Mı?” parametresi işaretli olmalıdır.

**Karma Koli Uygulaması ile birlikte kullanılmayan fatura kalemlerinde gelen Nakliye İskontosu nasıl pasif edilir?**

Fatura Parametreleri Iskonto sekmesinde Genel İskonto \[3\] parametresi ile aktif olan “Genel İskonto \[3\] = Birim Ağırlık\*Ağırlıklı İskonto Hesaplansın” ve “Her Satırda Değer Sorulsun” parametrelerinin işareti olmaması gerekiyor. VeritabanındaTBLSFATUPRM tablosunda BOLGF_HERSATIR alanının H olması gerekiyor.

**Karma Koli Kayıtları ekranında “Bilgi Amaçlı” parametresi işaretli olmadığında fatura belgesinde karma koli girişi sırasında miktar alanı neden pasif gelir?**

Belge tamamlandığında karma koli bileşenlerinden giriş/çıkış yapılacağı için karma koli stokunun miktarı, miktar yerine miktar-2 alanına girilmektedir. İlgili kayıt gride atıldığında da ağaç yapısı şeklinde görüntülenmektedir.
