---
title: "Arızalar Arası Ortalama Süre Analizi"
page_id: ""
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Arızalar Arası Ortalama Süre Analizi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Arızalar Arası Ortalama Süre Analizi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTdhMjY1Y2EzLWM2MDgtNDJjOS05ZjU2LWM1NjIxMGRjY2QzYiZsaW5rPWVlYmQ3NDYxLTBiMmUtNDA2YS05NDIxLWU4NmNmYjQ1NDJlMyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=7a265ca3-c608-42c9-9f56-c56210dccd3b&link=eebd7461-0b2e-406a-9421-e86cfb4542e3&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "arizalar-arasi-ortalama-sure-analizi.html"
source_version: ""
source_bytes: 33542
fetched_at: "2026-09-13T04:21:51+00:00"
generator: "netsis-scraper 1.0.0"
---
# Arızalar Arası Ortalama Süre Analizi

Arızalar Arası Ortalama Süre Analizi Raporu, makine bakım süreçlerinde ekipman performansını ve sistem sürekliliğini değerlendirmek için kullanılan MTBF, MTTR ve Reliability göstergelerini sunar. Bu göstergeler, makinelerin arıza eğilimlerinin izlenmesi, bakım etkinliğinin değerlendirilmesi ve önleyici/kestirimci bakım stratejilerinin planlanmasında referans sağlar.

**MTBF (Mean Time Between Failures – Arızalar Arası Ortalama Süre):** Onarılabilir bir sistemde ardışık iki arıza arasında geçen ortalama çalışma süresini ifade eder. MTBF, makinelerin arıza sıklığını belirlemeye ve gelecekteki arıza davranışını kestirmeye olanak sağlar.

**MTTR (Mean Time To Repair – Ortalama Tamir Süresi):** Bir arızanın başlangıcından ekipmanın yeniden çalışır duruma gelmesine kadar geçen ortalama süredir. MTTR, bakım ekiplerinin müdahale etkinliği ve onarım performansını ölçmek için kullanılır.

**Reliability (Güvenilirlik):** Bir makinenin belirlenen üretim koşulları altında, planlanan süre boyunca arıza yapmadan çalışabilme olasılığıdır. Reliability, MTBF ile doğrudan ilişkilidir ve makinelerin güvenilirliğini ölçmek için temel bir göstergedir. ,

Bu üç gösterge birlikte değerlendirildiğinde, makinelerin arıza eğilimleri, bakım etkinliği ve üretim sürekliliği hakkında kapsamlı bir değerlendirme yapılabilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/d1d2f0a4-9b4b-457a-9826-4c568f1db841/ms_mtbf_mttr_1.png)

**“Analiz Çalıştır”** butonuna tıklandığında:

- Duruşlu bakım emri olan makineler/kaynaklar için **MTBF, MTTR** ve **Güvenilirlik** hesaplamaları yapılır.
- Analize duruşlu ve belge durumu **“Kapandı”** olan bakım emirleri dahil edilir.
- Her bakım kaydında bakım başlangıç ve bitiş tarihleri kullanılarak; arızaların ne sıklıkla meydana geldiği, oluşan arızaların ne kadar sürdüğü hesaplanır.

Böylece, iki arıza arasındaki ortalama süre ve her bir arızanın ortalama çözülme süresi saat cinsinden raporlanır.

Yukarıdaki ekran görüntüsünde yer alan **“CNC_02_001”** makinesi için MTBF, MTTR ve Güvenilirlik değerlerinin hesaplama detayları ve formülasyonları aşağıda açıklanmaktadır.

MTBF değerlerinin doğru hesaplanabilmesi için makinenin toplam çalışma süresi ve vardiya sayısı dikkate alınır. Toplam çalışma süresi, MRP parametrelerinde belirtilen vardiya süreleri ve gün bazında toplam vardiya sayısına göre hesaplanır. Vardiya sayısı, fabrika çalışma takvimi ve varsa istasyon bazlı çalışma takvimine göre belirlenir. Vardiya sayısının 0 olduğu günler, makinenin çalışmadığı günler olarak kabul edilir ve MTBF hesaplamasına dahil edilmez.

MRP parametrelerinde her vardiya için çalışma süresi 7 saat olarak tanımlanmıştır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/bb4ab7a1-575b-45c4-b736-13ff1fddf140/ms_mtbf_mttr_2.png)

Fabrika çalışma takviminde haftasonu günleri tatil olup vardiya sayısı 0’dır. Haftanın diğer günlerinde makine 3 vardiya ile çalışmaktadır. “CNC_02_001” makinesi için istasyon özelinde ayrı bir takvim tanımı bulunmamaktadır dolayısıyla fabrika genel takvimi geçerlidir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/4c4c6527-f2e5-4bd5-bde0-6fb4699ba79b/ms_mtbf_mttr_3.png)

Hesaplamaya dahil edilecek bakım emirleri ve her bir arızanın toplam süresi (saat cinsinden) aşağıdaki tablo en sağdaki sütunda gösterilmektedir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/fc2e049a-8961-4501-86ff-e203660a12bc/ms_mtbf_mttr_4.png)

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Bakım Emri No | Kodu | Bakım Kodu | Belge Durumu | Bakım Baş. Tar. | Bakım Bit. Tar. | Arıza Süresi (Saat) |
| A00000000000001 | CNC_02_001 | B000025 | Kapandı | 25.05.2025 10:00:00 | 25.05.2025 15:00:00 | **5** |
| A00000000000002 | CNC_02_001 | B000025 | Kapandı | 12.06.2025 08:30:00 | 12.06.2025 14:00:00 | **5,5** |
| A00000000000003 | CNC_02_001 | B000025 | Kapandı | 28.07.2025 16:00:00 | 29.07.2025 00:30:00 | **8,5** |
| A00000000000004 | CNC_02_001 | B000025 | Kapandı | 20.08.2025 11:00:00 | 20.08.2025 16:30:00 | **5,5** |
| A00000000000005 | CNC_02_001 | B000025 | Kapandı | 10.09.2025 09:00:00 | 10.09.2025 17:00:00 | **8** |
| A00000000000006 | CNC_02_001 | B000025 | Kapandı | 14.07.2025 09:00:00 | 14.07.2025 16:30:00 | **7,5** |
|  |  |  |  |  | **Toplam Arıza Süresi** | **40** |

Yukarıda belirtilen veriler doğrultusunda, 11.05.2025 başlangıç tarihinden 11.02.2026 tarihine kadar analiz çalıştırıldığında, MTBF, MTTR ve Güvenilirlik hesaplamaları aşağıdaki formüllere göre gerçekleştirilmektedir.

```text
Analiz Başlangıç Tarihi                              : 01.05.2025
Günün Tarihi                                              : 11.02.2026
Vardiya Gün Sayısı                                    : 199 (3 Vardiya)
Toplam Vardiya Süresi                              : 21 Saat ⮕14900400 Saniye
```

```text
MTTR (Mean Time To Repair)                 : Toplam Onarım Süresi / Toplam Arıza Sayısı
                                                                    : 40 / 6 = 6,67 Saat
```

```text
Downtime (Total DownTime)                    : 144000 Saniye
Availability (Total UpTime)                        : Vardiya Planı Toplam Çalışma Süresi – UAK Duruş Süreleri
                                                                    : 14900400 – 144000 =14900400 ⮕ 4139 Saat
                                                                      >>> Arızalar Düşüldükten Sonra Toplam İş Yapılan Süre
```

**MTBF (Mean Time Between Failures)** : Availability / (Arıza Sayısı -1)

: 4319 / (6-1) = **827,80 Saat**

**Reliability (Güvenilirlik)** ![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/bbac1ed7-c58d-4590-957d-0a9a1b02b3ef/ms_mtbf_mttr_6.png)

: (Exp(-GivenTime / MTBF)) \* 100

: (Exp(−3/827,80))\*100 = **%99,64**
