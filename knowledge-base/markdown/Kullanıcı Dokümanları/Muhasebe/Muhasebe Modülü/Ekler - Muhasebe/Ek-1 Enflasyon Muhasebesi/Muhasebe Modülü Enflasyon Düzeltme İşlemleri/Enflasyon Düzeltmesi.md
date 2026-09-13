---
title: "Enflasyon Düzeltmesi"
page_id: "24740860"
product: "netsis-3-enterprise"
depth: 7
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Muhasebe"
  - "Muhasebe Modülü"
  - "Ekler / Muhasebe"
  - "Ek-1 Enflasyon Muhasebesi"
  - "Muhasebe Modülü Enflasyon Düzeltme İşlemleri"
  - "Enflasyon Düzeltmesi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / Ekler / Muhasebe / Ek-1 Enflasyon Muhasebesi / Muhasebe Modülü Enflasyon Düzeltme İşlemleri / Enflasyon Düzeltmesi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWIzMWJjODhkLTM5NTEtNDc2YS1hN2I5LTM5ZjAxNTQzNWZlNyZsaW5rPWNlYjBiOTY0LTc3ZGYtNDM4OC05MzVmLTZkNmExYzMzNTA2NiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=b31bc88d-3951-476a-a7b9-39f015435fe7&link=ceb0b964-77df-4388-935f-6d6a1c335066&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "enflasyon-duzeltmesi_41162265_24740860.html"
source_version: "2022-12-12T16:23:24.607+03:00"
source_bytes: 15369
fetched_at: "2026-09-13T04:14:28+00:00"
generator: "netsis-scraper 1.0.0"
---
# Enflasyon Düzeltmesi

Enflasyon Düzeltmesi ile ilgili ayrıntılı bilgiye bu dokümandan ulaşılabilir.

Farklı yöntemlerle düzeltilen muhasebe hesapları dışında kalan tüm muhasebe hesapları için, bir döneme ait (aylık) enflasyon düzeltmelerini yapan işlemdir.

**Yıl Kodu:** İşlemin çalıştırılacağı yıl kodudur.

**Ay Kodu Aralığı:** Mali yılın ilk ayı ile düzeltmenin yapılacağı ay kodudur.

**Örneğin;**

XXX hesabı düzeltme işlemi

Enflasyon fark hesabı = YYY

\2. ayın 1. aya göre enflasyon oranı %10 olarak varsayıldığında (Düzeltme katsayısı 1.1);

| Ay Kodu | Hesap Kodu | Aylık TL.Mizan | Düzeltilmiş Mizan | Açıklama |
| --- | --- | --- | --- | --- |
| 1 | XXX | 100 | 100 | 1.ay işlemleri toplamı |
| 2 | XXX | 120 | 120 | 2.ay işlemleri toplamı |
| 2 | YYY | 10 |  | 1.ayın düzeltmesi (enflasyon fark hesabı) |
| 2 | XXX |  | 10 | 1.ayın düzeltmesi (düzeltilmiş tutar) |
| **Toplam** |  | **230** | **230** |  |

Düzeltme işlemi 1. ay bakiyesini 2. ay sonuna taşır. Düzeltme yapılan ayda (2. ay) işlem yapılmaz. 1. ayın farkları 2. ay tarihi ile aktarılır.

**Örneğin;**

\3. ayda, 100 TL mizanı ve %10 enflasyon oranı düşünülerek ilerleme yapılsaydı;

| Ay Kodu | Hesap Kodu | Aylık TL.Mizan | Düzeltilmiş Mizan | Açıklama |
| --- | --- | --- | --- | --- |
| 2 | XXX | 220 | 230 | 2.ay sonu mizan |
| 2 | YYY | 10 |  | 2.ay sonu mizan (enflasyon fark hesabı) |
| 3 | XXX | 100 | 100 | 3.ay işlemleri toplamı |
| 3 | YYY | 22 |  | XXX hesabın 2.ay düzeltmesi |
| 3 | YYY | 1 |  | YYY hesabın 2.ay düzeltmesi |
| 3 | XXX |  | 23 | XXX hesabın 2.ay düzeltmesi |
| **Toplam** |  | **353** | **353** |  |

\3. aydaki düzeltmeler sonucu, hesaplarda oluşan mizan aşağıdaki gibidir:

| Hesap Kodu | Aylık TL.Mizan | Düzeltilmiş Mizan |
| --- | --- | --- |
| XXX | 320 | 353 |
| YYY | 33 |  |
| **Toplam** | **353** | **353** |

İşlem sırasında düzeltmelere ait hareketler yevmiye fişlerine kaydedilir. Bu fişler izlenebilir, istendiği zaman silinip tekrar oluşturulabilir.

**Tarih:** Düzeltme işlemi sırasında oluşan yevmiye fişlerinin tarihidir. Düzeltme ayının (bitiş ayı) son günü ön değer olarak getirilir.

Düzeltme işlemi sırasında birden fazla yevmiye fişi oluşturulur;

Enflasyon Muhasebesi (VUK) için 2 adet fiş,

IAS 29 (SPK) için; Muhasebe - Kayıt - [Muhasebe Parametreleri](<../../../Kayıt - Muhasebe/Muhasebe Parametreleri.md>) - "Enflasyon kar/zararı Parasal Olmayan Hesaplardan Bulunsun" parametresi işaretlendiğinde 2 adet fiş,

Muhasebe - Kayıt - [Muhasebe Parametreleri](<../../../Kayıt - Muhasebe/Muhasebe Parametreleri.md>) - "Enflasyon kar/zararı Parasal Hesaplardan Bulunsun" parametresi işaretlendiğinde ise 3 adet fiş oluşturulur.

Her iki uygulamada da son fiş aynıdır. Vadeli hareketleri peşine indirgemek amaçlıdır.

**Enflasyon Muhasebesi (VUK) 1. Fiş;**

Parasal olmayan hesaplar örneklerde anlatıldığı şekilde düzeltilir. Düzeltmeler, enflasyon fark hesaplarının TL tutarlarına, düzeltme farkları ise karşılık olarak enflasyon düzeltme hesabına yazılır.

**IAS 29 (SPK) 1.Fiş;**

Muhasebe - Kayıt - [Muhasebe Parametreleri](<../../../Kayıt - Muhasebe/Muhasebe Parametreleri.md>) - "Enflasyon kar/zararı Parasal Olmayan Hesaplardan Bulunsun" parametresi işaretlendiğinde, parasal olmayan hesaplar örneklerde anlatıldığı şekilde düzeltilir. Düzeltmeler hesapların düzeltilmiş tutarlarına, düzeltme farkları ise enflasyon düzeltme hesabına ("Düzeltilmiş Tutar" alanına) yazılır. Muhasebe - Kayıt - Muhasebe Parametreleri - "Enflasyon kar/zararı Parasal Hesaplardan Bulunsun" parametresi işaretlendiğinde, parasal ve parasal olmayan tüm hesaplar örneklerde anlatıldığı şekilde düzeltilir. Düzeltmeler, hesapların düzeltilmiş tutarlarına yazılır.

**IAS 29 (SPK) 2. Fiş;**

Muhasebe - Kayıt - [Muhasebe Parametreleri](<../../../Kayıt - Muhasebe/Muhasebe Parametreleri.md>) - "Enflasyon kar/zararı Parasal Hesaplardan Bulunsun" parametresi işaretlendiğinde oluşturulur. 1. Fişteki parasal hesapların düzeltme farkları, bu fişte ters çevrilir. Her hesap için farklar, enflasyon düzeltme hesabına yazılır. Bu fiş ile parasal hesaplar kendi nominal değerlerine geri döndürülür. İlgili fiş raporlanarak parasal hesaplardan kaynaklanan kazanç/kayıplar gözlenebilir.

> [!NOTE]
> İki uygulama aynı anda kullanıldığında, her ikisi için de ayrı ayrı fişler oluşur.

**Vadeli Alış/Satışlar Enflasyon Payı İndirgenmesi:**

Yüksek enflasyon dönemlerinde, Türk Lirası üzerinden vadeli olarak alınan/satılan varlıkların fiyatı, enflasyondan korunması amacıyla bir enflasyon payını da içerir. Alım ve satımın içerdiği enflasyon payının arındırılarak düzeltme işlemine tabi tutulması gerekir. Logo Netsis Enflasyon Muhasebesi için ön muhasebeden gelen kayıtlar, vade günü içerir. Vade farkı (enflasyon payı) arındırması, ilgili vade günleri üzerinden yapılır.

**Faiz Oranı:** Enflasyon payı tespitinde, alacak ve borç senetlerinin reeskont işlemine tabi tutulmasında esas alınan ve "Merkez Bankası" tarafından uygulanan faiz oranının kullanılması önerilir. İşlemin çalıştırılması sırasında bu oranın, "Faiz Oranı" alanında belirtilmesi gerekir.

**Aylık/Yıllık Oran:** Girilen faiz oranının yıllık faiz oranı mı, aylık faiz oranı mı olduğu belirlenir.

**Yıllık Gün Sayısı:** Vadelerin arındırılmasında yıllık faiz oranı verilmişse, Bileşik Faiz formülü kullanılır. Bu formülde kullanılması istenen yıllık gün sayısı 360 veya 365 olarak belirtilir.

**Peşine İndirgenecek Minimum Gün Sayısı:** Belli bir vade gününün altında, vadesi olan kayıtların vade arındırmalarının yapılmaması için girilen değerdir. Gün değerinin üzerindeki vadeli kayıtlar peşine indirgenir.

**Örneğin;**

1000 TL tutarında 100 gün vadeli alış yapıldığı ve aylık faiz oranının %5 olduğu düşünüldüğünde;

Vadesinden arındırılmış değer = 1000/(1+(0.05/30\*100)) = 857 olması gerekir. Bu durumda 1000 – 857 = 143 TL tutarında enflasyon farkı işlenmesi gerekir.

| Hesap Kodu | TL.Tutar | Düzeltilmiş Tut. | Açıklama |
| --- | --- | --- | --- |
| 153-001 | \<1000\> | \<1000\> |  |
| 153-999 | 143 |  | Enflasyon Fark Hesabı |
| 153-001 |  | 143 | IAS 29 uygulaması varsa |
| 698-001 | \<143\> | \<143\> | Enflasyon Düzeltme Hesabı |

> [!NOTE]
> Düzeltilmiş tutarlar IAS 29 uygulaması varsa oluşur.

Aynı örnekte yıllık faiz oranı %70 ve yıllık gün sayısı 360 girildiğinde;

Vadesinden arındırılmış değer = 1000/(1+(0.70/360\*100)) = 837 olması gerekir.

**Enflasyon Muhasebesi (VUK) 3. Fiş;** Peşine indirgemeden kaynaklanan farklar enflasyon fark hesaplarına ve karşılık olarak enflasyon düzeltme hesaplarının TL tutarlarına işlenir.

**IAS 29 (SPK) 3. Fiş;** Peşine indirgemeden kaynaklanan farklar, hesapların ve karşılık olarak enflasyon düzeltme hesaplarının düzeltilmiş tutarlarına işlenir.

> [!NOTE]
> Vade arındırması, sadece ilgili ay içinde yapılan vadeli kayıtlar için yapılır. Önceki aylarda yapılan vadeli kayıtların, daha önceki düzeltmeler sırasında indirgendiği düşünülür ve bu kayıtlar için indirgenmiş düzeltilmiş tutarları üzerinden sadece düzeltme işlemi yapılır.

> [!NOTE]
> İki uygulama aynı anda kullanıldığında, her ikisi için de ayrı ayrı fişler oluşur.
