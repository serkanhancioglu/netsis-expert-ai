---
title: "Hat Bazında Maliyet Muhasebesi"
page_id: "34213382"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Hat Bazında Maliyet Muhasebesi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Hat Bazında Maliyet Muhasebesi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTE3YzcxNjRhLTMzNTItNDU2NC1hNzZjLTVjNTBlOTY5MjE3YyZsaW5rPWVhMWVlNGIyLTZhNmQtNDE0MC1hODc5LWE4NThhYmYwNGJkOCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=17c7164a-3352-4564-a76c-5c50e969217c&link=ea1ee4b2-6a6d-4140-a879-a858abf04bd8&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "hat-bazinda-maliyet-muhasebesi_50677757_34213382.html"
source_version: "2022-11-03T09:09:48.160+03:00"
source_bytes: 648540
fetched_at: "2026-09-13T04:25:42+00:00"
generator: "netsis-scraper 1.0.0"
---
# Hat Bazında Maliyet Muhasebesi

Hat Bazında Maliyet Muhasebesi ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Üretim hatları bazında Maliyet Muhasebesi hesaplaması yapmak amacıyla hat tanımı, Üretim Sonu Kaydı sırasında Hat Kodu girişi ve hatlara ilişkin mamul ana grubu bazında farklı gider hesaplarının tanımlanmasını sağlar. Böylece, aynı ürünün farklı hatlardaki maliyet bilgisinin raporlanması sağlanır.

Bu çalışma kapsamında müşteri siparişi ve proje kodu bazında maliyet bilgisinin de detaylı olarak raporlanması sağlanır. Hat, Müşteri Siparişi ve Proje Kodu bazında maliyet hesabı sadece rapor amaçlı kullanılır. Hat, Müşteri Siparişi ve Proje Kodu bazında maliyet hesabı yapmak için [Maliyet Muhasebesi Parametreleri](<../Kullanıcı Dokümanları/Muhasebe/Maliyet Muhasebesi/Kayıt - Maliyet Muhasebesi/Maliyet Muhasebesi Parametreleri.md>) ekranından "Detaylı Maliyet Hesabı” seçeneğinin işaretlenmesi gerekir.

Üretim Hattı tanımının da, Üretim-Kayıt-[Hat Tanımlama](<../Kullanıcı Dokümanları/Üretim/Kayıt-Üretim/Hat Tanımlama.md>) ekranı üzerinden yapılması gerekir. Üretim hatları, tek bir mamul ana grubunun üretildiği ayrı hatları belirteceği gibi, birden fazla mamul ana grubunu da kapsayabilir. Aşağıdaki ilk örnek, iki mamul ana grubu için tanımlanmış 4 adet üretim hattını gösterir. Bu örnekte, Preshane ana grubunda maliyetleri farklılaşan iki ayrı hat mevcuttur. Aynı şekilde montaj ana grubunda da iki ayrı hat

olup, preshane ana grubunda üretilen ürünler, hat takibi dikkate alınmadan montaj ana grubunda tüketilir. Yani Preshane'de HAT1 veya HAT2’de üretilen bir yarı mamul, montajda HAT3 veya HAT4 üzerinden sarf edilebilir.

![](../_assets/6462cb82c346f2455214.png)![](../_assets/36b79e8f2765b51c93fa.png)

İkinci örnekte ise (Şekil-2), işlem sırası olarak birbirini takip eden iki mamul ana grubunun maliyetlerinin farklılaştığı üretim hatları görülür. Bu iki ayrı hat Preshane'de başlayıp, üretilen yarı mamuller montajda aynı hat üzerinde devam eder.

Şekil-2’deki gibi bir üretim sisteminde, yarı mamul sarflarının hat bazında takip edilmesi ve maliyet hesabının da hat bazındaki yarı mamul sarfiyatlarına göre hesaplanması için "Hat Tanımlama" ekranındaki “Yarı Mamul Sarfları Hat Bazında” parametresinin işaretlenmesi gerekir.

**Örneğin;** HAT1 için bu parametrenin işaretli olduğu varsayıldığında; montaj mamul ana grubunun HAT1 hattındaki yarı mamul sarfiyatı hesaplanırken, daha önceki ana grubun (Preshane), HAT1 üzerinde üretilen yarı mamul bilgisi aranır ve yarı mamulün hat bazındaki maliyet bilgisi kullanılarak yarı mamul sarf tutarı hesaplanır. “Yarı mamul Sarfları Hat Bazında” parametresi işaretli değilse, yarı mamul sarfiyatı hesaplanırken, yarı mamulün daha önceki ana gruptan (Preshane) gelen ortalama maliyet bilgisi kullanılarak hesaplama yapılır.

Maliyet Muhasebesi-Kayıt-[Mamul Ana Grup Kayıtları](<../Kullanıcı Dokümanları/Muhasebe/Maliyet Muhasebesi/Kayıt - Maliyet Muhasebesi/Mamul Ana Grup Kayıtları.md>) ekranındaki “Hat Tanımları” sekmesi kullanılarak, mamul ana grubunda üretim hatları bazında ayrı gider hesapları tanımlanır. Üretim Sonu Kaydı ekranında Hat Kodu girilmişse, mamul ana grubunun hat tanımında belirtilen gider hesapları üzerinden dağıtım yapılır. Üretim Sonu Kaydı ekranında Hat Kodu girilmemişse, mamul ana grubu için belirtilen gider hesapları üzerinden dağıtım yapılır. Proje Kodu bazında maliyet hesaplaması istenirse, buradaki gider hesaplarının proje bazında bakiyeleri dikkate alınır.

#### Örnek Uygulama-1

Mamul Ana Grup Tanımları ve işlem sırası aşağıdaki gibi tanımlanmış bir üretim sisteminde HAT1 ve HAT2 şeklinde iki ayrı üretim hattı bulunur. HAT1 otomasyona dayalı daha teknolojik bir üretim hattıdır ve bu yüzden giderleri daha düşüktür. Tanımlanan Hat Kodları için “Yarı Mamul Sarfları Hat Bazında” parametresi işaretlenir.

| İşlem Sırası | Mamul Ana Grup Kodu | Hat Tanımları |
| --- | --- | --- |
| 1 | Enjeksiyon | HAT1 – HAT2 |
| 2 | Boyama | HAT1 – HAT2 |

![](../_assets/34113beec4f65d057b07.png)

Mamul ana grupları için hat bazında işçilik ve enerji giderleri aşağıdaki gibi tanımlanır:

| Mamul Ana Grup Kodu | Hat Kodu | İşçilik Gider Hesabı | Enerji Gider Hesabı |
| --- | --- | --- | --- |
| Enjeksiyon | HAT1 | 720-001-001 (1000 TL) | 730-002-001 (2000 TL) |
| Enjeksiyon | HAT2 | 720-001-002 (2000 TL) | 730-002-002 (3000 TL) |
| Boyama | HAT1 | 720-001-003 (2000 TL) | 730-002-003 (1000 TL) |
| Boyama | HAT2 | 720-001-004 (3000 TL) | 730-002-004 (2000 TL) |

İşçilik ve enerji giderleri için dağıtım anahtarı olarak “Üretim Miktarları Oranı” seçilir.

Aşağıdaki tepe mamul reçetesi kullanılarak üretim yapılır. YARIMAMUL10 ve MAMUL10 için ayrı birer mamul grubu tanımlanır.

![](../_assets/bacad559af7bea39d9d2.png)

| Stok Kodu | Mamul Grup Kodu | Mamul Ana Grup Kodu |
| --- | --- | --- |
| YARIMAMUL10 | YARIMAMUL10 | Enjeksiyon |
| MAMUL10 | MAMUL10 | Boyama |

HM10 için satın alımlar sonucu oluşan aylık ortalama maliyet 15 TL olarak hesaplanır. MAMUL10 için sistemde iki adet müşteri siparişi bulunur. Bu siparişler için açılmış iş emirleri aşağıdaki gibidir:

M00000000000001 siparişi için HAT1 üzerinden üretim yapılırken, M00000000000002 siparişi için HAT2 üzerinden üretim yapılmıştır.

| Müşteri Siparişi | İş Emri No | Stok Kodu | İş Emri Miktarı |
| --- | --- | --- | --- |
| M00000000000001 | IE0000000000001 | MAMUL10 | 100 |
| M00000000000001 | IE0000000000002 | YARIMAMUL10 | 100 |
| M00000000000002 | IE0000000000003 | MAMUL10 | 150 |
| M00000000000002 | IE0000000000004 | YARIMAMUL10 | 150 |

İş emirleri için hat bazında üretim sonu kayıtları aşağıdaki gibi girilmiştir:

| İş Emri No | Stok Kodu | Üretim Miktarı | Hat Kodu |
| --- | --- | --- | --- |
| IE0000000000001 | MAMUL10 | 100 | HAT1 |
| IE0000000000002 | YARIMAMUL10 | 100 | HAT1 |
| IE0000000000003 | MAMUL10 | 150 | HAT2 |
| IE0000000000004 | YARIMAMUL10 | 150 | HAT2 |

Maliyet Muhasebesi Parametreleri ekranında Detaylı Maliyet Hesabı bölümünde “Hat Bazında Maliyet” ve “Sipariş Bazında Maliyet” seçenekleri işaretlenmiştir. Maliyet Muhasebesi → Kayıt → Maliyet Hesaplatma işlemi ilgili ay için çalıştırıldığında aşağıdaki sonuçlar elde edilir. Mamul Grup Kodu bazında elde edilen maliyet sonuçları aşağıdaki gibidir:

| Mamul Grup Kodu | Hammadde Sarf Tutarı | Yarı mamul Sarf Tutarı | İşçilik | Enerji | Aylık Maliyet | Ortalama Maliyet |
| --- | --- | --- | --- | --- | --- | --- |
| YARIMAMUL10 | 3750 | 0 | 3000 | 5000 | 47 | 47 |
| MAMUL10 | 0 | 11750 | 5000 | 3000 | 79 | 79 |

Enjeksiyon ana grubu altındaki iki hat için tanımlanan gider hesaplarının toplam bakiyesi işçilik için 3000 TL, enerji için ise 5000 TL eder. Bu yüzden enjeksiyon ana grubunda üretilen YARIMAMUL10 grubu için işçilik tutarı 3000 TL iken, enerji tutarı 5000 TL olarak hesaplanmıştır. Aynı mantıkla BOYAMA ana grubunda üretilen MAMUL10 grubu için de gider tutarları hesaplanmıştır.

Hat bazında hesaplanan maliyet bilgileri aşağıdaki gibidir:

| Stok Kodu | Hat Kodu | Hammadde Sarf Tutarı | Yarı mamul Sarf Tutarı | İşçilik | Enerji | Aylık Maliyet | Ortalama Maliyet |
| --- | --- | --- | --- | --- | --- | --- | --- |
| YARIMAMUL10 | HAT1 | 1500 | 0 | 1000 | 2000 | 45 | 45 |
| YARIMAMUL10 | HAT2 | 2250 | 0 | 2000 | 3000 | 48.33 | 48.33 |
| MAMUL10 | HAT1 | 0 | 4500 | 3000 | 1000 | 75 | 75 |
| MAMUL10 | HAT2 | 0 | 7250 | 4000 | 2000 | 81.66 | 81.66 |

YARIMAMUL10 grubunun ortalama maliyeti 47 TL iken, HAT1 bazında 45 TL, HAT2 bazında 48.33 TL olarak hesaplanmıştır. Bu durumun sebebi ENJEKSIYON ana grubunda HAT2 için tanımlanan giderlerin HAT1 için tanımlanan giderlerden fazla olmasıdır. Görüldüğü üzere HAT1 üzerinde 1000 TL işçilik kullanılırken, HAT2 üzerinde 2000 TL işçilik kullanılmıştır. MAMUL10 grubunun ortalama maliyeti 79 TL iken, HAT1 bazında 75 TL, HAT2 bazında 81.66 TL olarak hesaplanmıştır. Yine HAT2 için tanımlanan giderler HAT1 için tanımlanan giderlerden fazladır. Ayrıca HAT2 için hesaplanan yarı mamul sarf tutarı da HAT1’e göre fazladır. HAT1 için birim fiyat 45 TL’den yarı mamul sarfı yapılırken, HAT2 için 48.33 TL’den yarı mamul sarfı yapılmıştır. Bu durumun sebebi de, Hat Tanımlama ekranında işaretlenen “Yarı Mamul Sarfları Hat Bazında” seçeneğinden kaynaklanır. HAT1 için tüketilen yarı mamuller, HAT1 üzerinde üretilen yarı mamullerin ortalama maliyetiyle sarf edilmiştir. Aynı durum HAT2 için de geçerlidir. Yani, her üretim hattı safhalar boyunca kendi ürettiği yarı mamulleri sarf eder ve bu yüzden yarı mamul sarf tutarları farklı olur.

Sipariş bazında hesaplanan maliyet bilgileri aşağıdaki gibidir:

| Stok Kodu | Hat Kodu | Hammadde Sarf Tutarı | Yarı Mamul Sarf Tutarı | İşçilik | Enerji | Aylık Maliyet | Ortalama |
| --- | --- | --- | --- | --- | --- | --- | --- |
| YARIMAMUL10 | MS1 | 1500 | 0 | 1000 | 2000 | 45 | 45 |
| YARIMAMUL10 | MS2 | 2250 | 0 | 2000 | 3000 | 48.33 | 48.33 |
| MAMUL10 | MS1 | 0 | 4500 | 2000 | 1000 | 75 | 75 |
| MAMUL10 | MS2 | 0 | 7250 | 3000 | 2000 | 81.66 | 81.66 |

M00000000000001 siparişi HAT1 üzerinde üretilirken M00000000000002 siparişi HAT2 üzerinde üretilmiştir. Bu yüzden M00000000000001 siparişi için ortalama maliyetler daha düşük çıkmıştır.

#### Örnek Uygulama-2

Mamul Ana Grup Tanımları ve işlem sırası aşağıdaki gibi tanımlanmış bir üretim sisteminde maliyet hesabı yapılacaktır. Tanımlanan hat kodları için “Yarı Mamul Sarfları Hat Bazında” parametresi işaretlenmemiştir. Bu durumda Montaj ana grubundaki yarı mamul sarfiyatı hat bazında yapılmaz ve ortalama maliyet tutarından sarf edilir.

| İşlem Sırası | Mamul Ana Grup Kodu | Hat Tanımları |
| --- | --- | --- |
| 1 | Enjeksiyon | HAT1 – HAT2 |
| 2 | Boyama | HAT3 – HAT4 |

![](../_assets/26a28d97f2add2b14db4.png)

Mamul Ana Grupları için hat bazında işçilik ve enerji giderleri aşağıdaki gibi tanımlanmıştır:

| Mamul Ana Grup Kodu | Hat Kodu | İşçilik Gider Hesabı | Enerji Gider Hesabı |
| --- | --- | --- | --- |
| Enjeksiyon | HAT1 | 720-001-001 (1000 TL) | 730-002-001 (2000 TL) |
| Enjeksiyon | HAT2 | 720-001-002 (2000 TL) | 730-002-002 (3000 TL) |
| Boyama | HAT3 | 720-001-003 (2000 TL) | 730-002-003 (1000 TL) |
| Boyama | HAT4 | 720-001-004 (3000 TL) | 730-002-004 (2000 TL) |

İşçilik ve enerji giderleri için dağıtım anahtarı olarak “Üretim Miktarları Oranı” seçilmiştir. Aşağıda tepe mamul reçetesi kullanılarak üretim yapılmıştır. Her bir ürün kodu için ayrı bir mamul grubu tanımlanmıştır.

| Stok Kodu | Mamul Grup Kodu | Mamul Ana Grup Kodu |
| --- | --- | --- |
| YARIMAMUL10 | YARIMAMUL10 | Enjeksiyon |
| MAMUL10 | MAMUL10 | Boyama |

HM10 için satınalma sonucu oluşan aylık ortalama maliyet 15 TL olarak hesaplanmıştır. MAMUL10 için sistemde iki adet müşteri siparişi bulunur. Bu siparişler için açılmış iş emirleri aşağıdaki gibidir:

| Müşteri Siparişi | İş Emri No | Stok Kodu | İş Emri Miktarı |
| --- | --- | --- | --- |
| M00000000000001 | IE0000000000001 | MAMUL10 | 100 |
| M00000000000001 | IE0000000000002 | YARIMAMUL10 | 100 |
| M00000000000002 | IE0000000000003 | MAMUL10 | 150 |
| M00000000000002 | IE0000000000004 | YARIMAMUL10 | 150 |

İş emirleri için hat bazında üretim sonu kayıtları aşağıdaki gibi girilmiştir:

| İş Emri No | Stok Kodu | Üretim miktarı | Hat Kodu |
| --- | --- | --- | --- |
| IE0000000000001 | MAMUL10 | 100 | HAT3 |
| IE0000000000002 | YARIMAMUL10 | 100 | HAT1 |
| IE0000000000003 | MAMUL10 | 150 | HAT4 |
| IE0000000000004 | YARIMAMUL10 | 150 | HAT2 |

Maliyet Muhasebesi Parametreleri ekranındaki Detaylı Maliyet Hesabı alanından “Hat Bazında Maliyet” seçeneği işaretlenmiştir.

Maliyet Muhasebesi-Kayıt-Maliyet Hesaplatma işlemi ilgili ay için çalıştırıldığında aşağıdaki sonuçlar elde edilir.

Mamul Grup Kodu bazında elde edilen maliyet sonuçları aşağıdaki gibidir:

| Mamul Grup Kodu | Hammadde Sarf Tutarı | Yarı mamul Sarf Tutarı | İşçilik | Enerji | Aylık Maliyet | Ortalama Maliyet |
| --- | --- | --- | --- | --- | --- | --- |
| YARIMAMUL10 | 3750 | 0 | 3000 | 5000 | 47 | 47 |
| MAMUL10 | 0 | 11750 | 5000 | 3000 | 79 | 79 |

Enjeksiyon ana grubu altındaki iki hat için tanımlanan gider hesaplarının toplam bakiyesi işçilik için 3000 TL, enerji için ise 5000 TL eder. Bu yüzden enjeksiyon ana grubunda üretilen YARIMAMUL10 grubu için işçilik tutarı 3000 TL iken, enerji tutarı 5000 TL olarak hesaplanır. Aynı mantıkla BOYAMA ana grubunda üretilen MAMUL10 grubu için de gider tutarları hesaplanır.

Hat bazında hesaplanan maliyet bilgileri aşağıdaki gibidir:

| Stok Kodu | Hat Kodu | Hammadde Sarf Tutarı | Yarı Mamul Sarf Tutarı | İşçilik | Enerji | Aylık Maliyet | Ortalama Maliyet |
| --- | --- | --- | --- | --- | --- | --- | --- |
| YARIMAMUL10 | HAT1 | 1500 | 0 | 1000 | 2000 | 45 | 45 |
| YARIMAMUL10 | HAT2 | 2250 | 0 | 2000 | 3000 | 48.33 | 48.33 |
| MAMUL10 | HAT3 | 0 | 4700 | 2000 | 1000 | 77 | 77 |
| MAMUL10 | HAT4 | 0 | 7050 | 3000 | 2000 | 80.33 | 80.33 |

YARIMAMUL10 grubunun ortalama maliyeti 47 TL iken, HAT1 bazında 45 TL, HAT2 bazında 48.33 TL olarak hesaplanmıştır. Bu durumun sebebi ENJEKSIYON ana grubunda HAT2 için tanımlanan giderlerin HAT1 için tanımlanan giderlerden fazla olmasıdır. Görüldüğü üzere HAT1 üzerinde 1000 TL işçilik kullanılırken, HAT2 üzerinde 2000 TL işçilik kullanılmıştır.

MAMUL10 grubunun ortalama maliyeti 79 TL iken, HAT3 bazında 77 TL, HAT4 bazında 80.33 TL olarak hesaplanmıştır. Yine HAT4 için tanımlanan giderler HAT3 için tanımlanan giderlerden fazladır. Ayrıca HAT3 ve HAT4 için hesaplanan yarı mamul sarf tutarlarının birim maliyeti eşittir. Çünkü yarı mamul sarfları hat bazında takip edilmemiştir. Bu yüzden YARIMAMUL10 sarfiyatı ortalama maliyet -47 TL- üzerinden hesaplanmıştır.
