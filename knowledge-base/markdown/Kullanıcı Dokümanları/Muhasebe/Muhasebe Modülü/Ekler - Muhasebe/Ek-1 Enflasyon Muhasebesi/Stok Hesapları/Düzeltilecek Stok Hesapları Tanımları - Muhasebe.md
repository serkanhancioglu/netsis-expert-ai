---
title: "Düzeltilecek Stok Hesapları Tanımları / Muhasebe"
page_id: "24740866"
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
  - "Stok Hesapları"
  - "Düzeltilecek Stok Hesapları Tanımları / Muhasebe"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / Ekler / Muhasebe / Ek-1 Enflasyon Muhasebesi / Stok Hesapları / Düzeltilecek Stok Hesapları Tanımları / Muhasebe"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWI1N2I5ZDQwLTVmYzktNDVhNy05ZDE0LTM4NjJkNDI5NGVmNiZsaW5rPTJiYjlkYzUzLTJjMmEtNDE2My1iYzgwLThmNTIwNGNlN2JiOSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=b57b9d40-5fc9-45a7-9d14-3862d4294ef6&link=2bb9dc53-2c2a-4163-bc80-8f5204ce7bb9&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "duzeltilecek-stok-hesaplari-tanimlari-muhasebe_41162301_24740866.html"
source_version: "2022-12-12T16:34:56.720+03:00"
source_bytes: 10840
fetched_at: "2026-09-13T04:14:33+00:00"
generator: "netsis-scraper 1.0.0"
---
# Düzeltilecek Stok Hesapları Tanımları / Muhasebe

Düzeltilecek Stok Hesapları Tanımları ile ilgili ayrıntılı bilgiye bu dokümandan ulaşılabilir.

Stok hesapları için toplulaştırılmış yöntemler kullanılacak ise, hesap kodu bazında ilgili tanımların yapılacağı bölümdür. Toplulaştırılmış yöntemler; Muhasebe Parametreleri bölümünde belirlenen Enflasyon Muhasebesi (VUK), IAS29 (SPK) ya da Enflasyon Muhasebesi + IAS29 uygulamaları için çalışır. Bu parametrede "Hiçbiri" seçilmişse, toplulaştırılmış yöntem uygulanmaz.

**Yöntem:** Hesap bazında hangi toplulaştırılmış yöntemin kullanılacağına dair seçimin yapılacağı alandır.

**Basit Ortalama Yöntemi:** Dönem ortalama düzeltme katsayısının bulunarak stok hesapları TL değerlerinin bu katsayıyla çarpılması suretiyle düzeltilmesidir.

```text
Dönem Ortalama Düzeltme Katsayısı = Dönem Sonu Endeksi
```

```text
                                                               Bir Önceki Dönem Sonu Endeksi + Dönem Sonu Endeksi/2
```

şeklinde hesaplanır. Mal girişlerinin dönem içine eşit şekilde dağıldığı ve elde kalan malın dönem ortasında stoka girdiği varsayımından yola çıkılarak tespit edilen bir yöntemdir. Düzeltmeler, dönem sonu endeksinin dönem ortalama endeksine oranlanması ile elde edilen katsayı ile yapılır.

**Stok Devir Hızı Yöntemi:** Stok hesapları bazında, ortalama stokta durma günü hesaplanarak kalan stokun bu tarihte alındığı varsayılır. Kalan stokun dönem sonu TL değeri, dönem sonu endeksinin stoka giriş tarihindeki (dönem sonu - durma günü tarihindeki) endekse oranlanması ile elde edilen katsayı ile düzeltilir.

| Kırılım | Oran | Durma Günü |
| --- | --- | --- |
| İlk Madde Malzeme |  |  |
| İşçilik |  |  |
| Amortisman |  | - |
| Genel Üretim Giderleri |  |  |
| Finansman Gideri |  |  |

Bu yöntem seçildiğinde stok hesapları için yukarıdaki tabloda yer alan durma günü değerleri ve oranların girilmesi gerekir.

**Örneğin;**

İlk Madde Malzeme.

Ham maddenin ortalama durma günü 60 ise; tablonun aşağıdaki şekilde doldurulması gerekir.

| Kırılım | Oran | Durma Günü |
| --- | --- | --- |
| İlk Madde Malzeme | 100 | 60 |
| İşçilik |  |  |
| Amortisman |  |  |
| Genel Üretim Giderleri |  |  |
| Finansman Gideri |  |  |

**Örneğin;**

Yarı Mamul.

Yarı mamulün mamul haline gelinceye kadar stokta bekleme süresi 30 gün, yarı mamul maliyetinde ilk madde malzeme oranı %70, işçilik, amortisman ve genel üretim giderleri payları %10 ise;

| Kırılım | Oran | Durma Günü |
| --- | --- | --- |
| İlk Madde Malzeme | 70 | 90 |
| İşçilik | 10 | 30 |
| Amortisman | 10 | - |
| Genel Üretim Giderleri | 10 | 30 |
| Finansman Gideri |  |  |

> [!NOTE]
> İlk madde malzeme durma günü 90 = ilk madde malzeme durma günü + yarı mamul durma günü olarak verilir.

İlk madde malzeme dışındaki diğer giderler (işçilik ve genel üretim giderleri gibi) yarı mamul aktif hale geldiğinde, yarı mamule girdiği için bu kalemlerin durma günü yarı mamulün stokta bekleme süresi kadar olması gerekir. İlk madde malzeme ise, yarı mamul haline gelmeden önce ve yarı mamul olarak stokta bekler. Bu nedenle iki süre toplanarak belirtilir.

Amortisman giderleri için durma günü sorgulanmaz. Çünkü amortisman gideri, tarihi değerlerle yarı mamule girmişse, belli bir katsayı ile (düzeltilmiş toplam amortisman/tarihi toplam amortisman) çarpılarak düzeltilir. Eğer düzeltilmiş değerlerle yarı mamule girmişse, olduğu gibi alınır.

**Örneğin;**

Mamul.

Mamulün sevk edilinceye kadar stokta bekleme süresi 30 gün, mamul maliyetinde ilk madde malzeme oranı %70, işçilik, amortisman ve genel üretim giderleri payları %10 ise;

| Kırılım | Oran | Durma Günü |
| --- | --- | --- |
| İlk Madde Malzeme | 70 | 120 |
| İşçilik | 10 | 60 |
| Amortisman | 10 | - |
| Genel Üretim Giderleri | 10 | 60 |
| Finansman Gideri |  |  |

> [!NOTE]
> İlk madde malzeme durma günü 120 = ilk madde malzeme durma günü + yarı mamul durma günü + mamul durma günü olarak verilir.

Hesabın içinde bulunan her bir kalem için, öncelikle hesabın TL bakiyesi bulunur ve verilen oranlar uygulanarak her kalemin TL tutardan aldığı pay hesaplanır. Daha Sonra her kalemin bulunan TL payı, verilen durma gününe göre endekslenerek her kalem için ayrı ayrı düzeltilmiş tutarlar hesaplanır. Düzeltilmiş değerlerin toplamı ise, hesabın sonuç düzeltilmiş değerini verir. Hesabın amortisman kaleminin TL payı çıkarılır, bu hesabın amortisman payının düzeltilmiş amortisman tutarından alacağı pay hesaplanarak eklenir.

**Not:** Durma günü = 1...30 arası ise düzeltme yapılmaz, 31...60 arası ise bir aylık endeksle, 61...90 ise iki aylık endeksle endekslenir.
