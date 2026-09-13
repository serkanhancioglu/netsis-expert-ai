---
title: "Ek-1 (Dizayn SQL Desteği)"
page_id: "41164582"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Genel"
  - "Dizayn Modülü"
  - "Dizayn/Ekler"
  - "Ek-1 (Dizayn SQL Desteği)"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Dizayn Modülü / Dizayn/Ekler / Ek-1 (Dizayn SQL Desteği)"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTVkYWExMzc4LTcxNDgtNGE5YS1hNmY0LWRmZjRjMTMyNTZmOCZsaW5rPTQ2NTQ4NTUwLTU0OGUtNGIwYS1hNmRkLWMyZjBlY2NjNTcxMyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=5daa1378-7148-4a9a-a6f4-dff4c13256f8&link=46548550-548e-4b0a-a6dd-c2f0eccc5713&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ek-1-dizayn-sql-destegi_41164802_41164582.html"
source_version: "2022-12-07T10:08:22.820+03:00"
source_bytes: 321254
fetched_at: "2026-09-13T04:15:30+00:00"
generator: "netsis-scraper 1.0.0"
---
# Ek-1 (Dizayn SQL Desteği)

Dizayn SQL Desteği ile ilgili detaylı bilgiye bu dokümandan ulaşılabilir.

SQL tipi, basım sırasında veri tabanından değer getirilmesi için kullanılır.

**Örneğin;**

"Müşteri Çekleri" kaydı sırasında "Cari Rapor Kodu", çekin verildiği bankaya ait şube kodu ve adının girilmesi için kullanılabilir. Bu bilgilerin dizayn ile basımı, Dizayn → Kayıt → [Dizayn](<../Kayıt - Dizayn/Dizayn.md>) → Kalem Bilgileri → Tip → "Program" seçeneği kullanılarak yapılamaz. Bunun sebebi, "Cari Rapor Kodu" alanı için alan numarasının olmamasıdır. SQL seçeneği, basımın yapılmasını sağlar.

![](../../../../_assets/710260c2324d53653ea1.png)

Yukarıdaki ekranda SQL seçeneğinin kullanımı yer alır. Bu örnekte, MCEK View’unda bulunan RAP_KOD alanının basımı gerçekleşir. Bu da "Cari Rapor Kodunun" tutulduğu alandır. SQL seçeneği ile TBLMCEK tablosu kullanılarak, aynı bilgi bastırılabilir.

Yapılan basım sonucu; Banka Kodu/Adı sütununa, çek kaydı sırasında "Cari Rapor Kodu" alanına girilen bilgi basılır.

**SQL tipli alan kullanımında dikkat edilmesi gereken konular;**

- Cümlede, “Select” komutundan sonraki kısmın yazılması gerekir. Select komutu, yazılacak cümlenin başına program tarafından otomtik olarak getirilir.
- Yazılan cümle sonucu tek bir değerin dönmesi gerekir. Bunun için de kısıt verilmesi gerekebilir.

Çek Alındı Bordrosunda, tek bir çekin olduğu varsayıldığında ve kısıt olarak da çek numarası verildiğinde;

Çek Alındı bordrosunda birden fazla çek olması halinde, her çeke ait "Cari Rapor Kodu" farklı olabileceği için, örnekte verilen cümle istenen sonucu getirmez. Çünkü, bu cümleye göre sadece “B00000000000051” numaralı çek için girilen "Cari Rapor Kodu" bastırılabilir (SC_NO=’B00000000000051’).

Bunun gibi kısıt verilecek alanın değişken olduğu durumlarda, fonksiyon kullanılması gerekir. Dizaynda kullanılabilecek 3 adet fonksiyon vardır.

Bunlar;

VT_Sayisal(),

VT_Karakter() ve

VT_Tarih() şeklindedir.

**VT_Sayisal():** Sayısal kısıt vermek için kullanılır.

**VT_Karakter():** Alfa sayısal kısıt vermek için kullanılır.

**VT_Tarih():** Tarih kısıdı vermek için kullanılır.

> [!NOTE]
> Bu fonksiyonlara SQL cümlesinin yazıldığı alanda sağ klik yapılarak ulaşılabilir.

![](../../../../_assets/a2eeea20f8272b6aec07.png)

Yukarıdaki ekranda görüntülenen "Fonksiyon Ekle" seçeneği kullanıldığında ("Karakter" fonksiyonu gibi), seçilen fonksiyon program tarafından ekrana getirilir.

![](../../../../_assets/07b48bdb06c67b149999.png)

Fonksiyon seçildikten sonra, bu fonksiyonun hangi alana kısıt verilmesi için seçildiğinin belirtililmesi gerekir. Örnekte, alındı bordrosundaki her çek için girilen "Cari Rapor Kodunun" bastırılması amacı ile, kısıt olarak çek numarasının kullanılması gerekir. Bu durumda, çek numarasının dizayn alan numarasının, fonksiyonun parametresi olarak belirtilmesi gerekir.

![](../../../../_assets/6735187ea7e9a557cdb3.png)

Alındı bordrosunda çek numarası basımı 6000 numaralı alan ile yapılır. Ayrıca, kısıt olarak belirlenen "Çek Numarası" alanı alfa sayısal olduğu için, örnekte kısıt **VT_Karakter({6000})** olarak girilmiştir. SQL cümlesinin girişi sırasında, mevcut dizayn alanlarının hepsine, farenin sağ tuşuile ekrana gelen "Saha Rehberi" seçeneğinden ulaşılır.

Yukarıdaki tanımlama ile, bordrodaki çek numaraları değiştikçe, program MCEK view’unda ilgili çeke ait satırın "Cari Rapor Kodunu" basar.

VT_Sayisal() ve VT_Tarih() fonksiyonlarının kullanımı da VT_Karakter’de olduğu gibidir. Tek fark, fonksiyonlarda girilecek alan numarasına sahip sahanın sayısal ya da tarih formatında olmasıdır.
