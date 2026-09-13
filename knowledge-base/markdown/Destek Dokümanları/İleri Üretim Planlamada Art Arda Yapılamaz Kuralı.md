---
title: "İleri Üretim Planlamada Art Arda Yapılamaz Kuralı"
page_id: "166396056"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "İleri Üretim Planlamada Art Arda Yapılamaz Kuralı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / İleri Üretim Planlamada Art Arda Yapılamaz Kuralı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWM5MTA0MWYxLWUyMWUtNDY5Zi1hOGJjLTNmM2ExMTJlNjU1OSZsaW5rPTA5MTFlMGU2LWQ3OWYtNDg0MS04M2RhLWQ0MzA1MGU4MzVhOCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=c91041f1-e21e-469f-a8bc-3f3a112e6559&link=0911e0e6-d79f-4841-83da-d43050e835a8&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ileri-uretim-planlamada-art-arda-yapilamaz-kurali_166396061_166396056.html"
source_version: "2025-02-18T13:51:56.700+03:00"
source_bytes: 12693
fetched_at: "2026-09-13T04:22:15+00:00"
generator: "netsis-scraper 1.0.0"
---
# İleri Üretim Planlamada Art Arda Yapılamaz Kuralı

Bu dokümanda ileri üretim planlama uygulamasında **"Art Arda Yapılamaz"** kural tipi üzerine bir çizelgeleme örneğine yer verilmiştir.

Kural Tanımlama, ileri üretim planlamada, operasyon, makine ve ürün bazında belirli kuralların tanımlanabildiği bir ekrandır. "Art Arda Yapılamaz" Kuralı, önceki operasyon-makine-ürün setinden sonra, sonraki operasyon-makine-ürün setinin planlanmasının önüne geçmek için tanımlanır. Ancak, başka bir planlama seçeneği bulunamadığı takdirde, tanımlanan kural seti göz ardı edilerek iş emirleri planlanabilir.

Aşağıdaki ekran görüntüsünde gösterilen "art arda yapılamaz" kural tanımına göre, "YM1001" ürünü için "OPE1" operasyonu "MKN1" makinesinde tamamlandıktan sonra, sıradaki operasyon olan "OPE2" operasyonuna "MKN5" makinesinde devam edilememektedir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/5c93cbd3-ef57-4106-a1c6-5894db53d06d/MS_AAYK_1.png)

YM1001 stok kodu için operasyon-makine eşleştirmelerinin aşağıdaki gibi olduğu varsayıldığında, YM1001 ürünü "OPE1" operasyonu için üç farklı alternatif makinede (MKN1, MKN2, MKN3) işlenebilecektir. "OPE2" operasyonu için ise (MKN4, MKN5, MKN6) makineleri kullanılabilecektir.

| Ürün Kodu | **Operasyon** **Kodu** | **Makine** **Kodu** | **Üretim** **Süresi** | **Süre** **Tipi** | **Üretim** **Miktarı** |
| --- | --- | --- | --- | --- | --- |
| YM1001 | OPE1 | MKN1 | 5 | Dakika | 1 |
| YM1001 | OPE1 | MKN2 | 5 | Dakika | 1 |
| YM1001 | OPE1 | MKN3 | 5 | Dakika | 1 |
| YM1001 | OPE2 | MKN5 | 5 | Dakika | 1 |
| YM1001 | OPE2 | MKN6 | 5 | Dakika | 1 |
| YM1001 | OPE2 | MKN4 | 5 | Dakika | 1 |

Ancak, MKN1 makinesinden çıkan ürünün bir sonraki operasyonunun, diğer alternatif makineler yerine yalnızca MKN4 makinesinde yapılması istenmektedir. Benzer şekilde, diğer makine seçimleri için de aşağıdaki gibi kural setleri tanımlanmıştır.

| **Kural** **Tipi** | Ürün Kodu | **Operasyon** **Kodu** | **Makine** **Kodu** | **Sonraki** **Operasyon** **Kodu** | **Sonraki** **Makine** **Kodu** |
| --- | --- | --- | --- | --- | --- |
| Art arda yapılamaz | YM1001 | OPE1 | MKN1 | OPE2 | MKN5 |
| Art arda yapılamaz | YM1001 | OPE1 | MKN1 | OPE2 | MKN6 |
| Art arda yapılamaz | YM1001 | OPE1 | MKN2 | OPE2 | MKN4 |
| Art arda yapılamaz | YM1001 | OPE1 | MKN2 | OPE2 | MKN6 |
| Art arda yapılamaz | YM1001 | OPE1 | MKN3 | OPE2 | MKN4 |
| Art arda yapılamaz | YM1001 | OPE1 | MKN3 | OPE2 | MKN5 |

Kural tanımlamaları yapıldıktan sonra çizelgeleme çalıştırıldığında, iş emirlerinin 2. operasyon bazında makine seçimi aşağıdaki gibi gerçekleşir.

| 1. Operasyon |  | 2.Operasyon |
| --- | --- | --- |
| MKN1 | ► | MKN4 |
| MKN2 | ► | MKN5 |
| MKN3 | ► | MKN6 |

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/2ac67ef6-d255-4219-af18-e6b2ebfab0f4/MS_AAYK_2.png)

Buna göre, ileri üretim planlama ekranında bulunan iş emirlerinin çizelgeleme sonucu aşağıdaki gibi gerçekleşir.

MSTF00000000001 **MKN3 ► MKN6**

MSTF00000000002 **MKN2 ► MKN5**

MSTF00000000003 **MKN1 ► MKN4**

MSTF00000000004 **MKN3 ► MKN6**

MSTF00000000005 **MKN2 ► MKN5**

MSTF00000000006 **MKN1 ► MKN4**

**![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/e36a2ed0-fe53-4324-a817-aa2e690f7a96/MS_AAYK_3.png)**

"Art Arda Yapılamaz" kural setinin dikkate alınmadığı bir senaryoda, iş emirlerinin ikinci operasyonu için makine seçimi aşağıdaki şekilde gerçekleşebilir.

MSTF00000000003 **MKN1 ► MKN5**

MSTF00000000002 **MKN2 ► MKN4**

MSTF00000000001 **MKN3 ► MKN6**

MSTF00000000006 **MKN1 ► MKN5**

MSTF00000000005 **MKN2 ► MKN4**

MSTF00000000004 **MKN4 ► MKN6**

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/0763ddda-68ca-4701-b0a8-dd362edfc8dd/MS_AAYK_4.png)
