---
title: "İleri Üretim Planlama Fırın Tipli Makine Örneği"
page_id: "135825115"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "İleri Üretim Planlama Fırın Tipli Makine Örneği"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / İleri Üretim Planlama Fırın Tipli Makine Örneği"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTdlOWNmOTI4LWVmNDgtNDA3ZC1iMDNhLWNjM2Y4OWJmZmVmMiZsaW5rPTRkNmNjMWIzLTE4MGItNDI5Mi1hNTk4LTY4NGY0NmZhMjQzOCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=7e9cf928-ef48-407d-b03a-cc3f89bffef2&link=4d6cc1b3-180b-4292-a598-684f46fa2438&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ileri-uretim-planlama-firin-tipli-makine-ornegi_135825126_135825115.html"
source_version: "2024-04-01T12:49:40.473+03:00"
source_bytes: 530889
fetched_at: "2026-09-13T04:22:54+00:00"
generator: "netsis-scraper 1.0.0"
---
# İleri Üretim Planlama Fırın Tipli Makine Örneği

Bu dokümanda ileri üretim planlama ile fırın tipli makineler üzerinde bir çizelgeleme örneğine yer verilmiştir.

Fırın tipli makinelerde kapasite önemlidir. Boş kapasitesi olduğu sürece yeni ürün alabilir. Bu yönüyle gerçek ekmek fırınları gibi düşünülebilir ve yine bu özelliğiyle kazan tipli makinelerden ayrılmaktadır. Farklı ürünleri aynı anda işleme özelliği vardır. Her ürün fırında kendi proses süresi kadar işlenir.

Ayrıca bu makine tipinde "İşe Başlayabilmek için Min. Kapasite Doluluk Oranı" alanı bulunmaktadır. 1 değeri %100 anlamına gelmektedir. Buraya girilen oran makinenin çalışmaya başlaması için önünde kapasitesinin en az yüzde kaçı kadar iş birikmesini bekleyeceğini ifade eder. Örneğin bu değer 0,8 girilirse ve fırının kapasitesi 100 birimse, fırına girmeye hazır en az 80 birim ürün birikmeden fırın çalışmaya başlamayacaktır.

Fırın tipli makinelerde Operasyon-Makine eşleştirme sırasında girdiğimiz "Üretim Miktarı" bilgisi "Kapasite" anlamına gelir.

Örneğin A ve B mamulleri için aşağıdaki gibi operasyon-makine eşleştirmeleri yapıldığını düşünelim:

- Stok Kodu: A \>\> Üretim Süresi: 4 Saat // Üretim Miktarı: 10 M3 (Ölçü-Br2)
- Stok Kodu: B \>\> Üretim Süresi: 6 Saat // Üretim Miktarı: 20 M3 (Ölçü-Br2)

Yukarıdaki tanımlamalar şu anlama gelir: Fırını sadece A ürünü ile doldurmak istersek fırın en fazla 10 M3 ürün alabilir ve üretim süresi de miktar bağımsız olarak 4 saat sürer. Aynı şekilde fırını tamamen B ürünü ile doldurmak istersek en fazla 20 M3 ürün alabilir ve üretim süresi de miktar bağımsız olarak 6 saat sürer.

Stok kart tanımlamalarımız aşağıdaki şekildedir.

![](../_assets/76ab0d84b6fb316eee72.png)

![](../_assets/c6ca1e1257f3756691c2.png)

Makine tanımlama ekranı aşağıdaki şekildedir.

![](../_assets/261e486c663097e25c0a.png)

Örneğe göre Operasyon – Makine Eşleştirme tanımları alttaki şekildedir.

![](../_assets/eb31def8c0f75664f480.png)

![](../_assets/f008c600ae581689fb04.png)

Rota tanımları aşağıdaki şekilde ve ürünlerle eşleştirilmesi yapılmıştır.

![](../_assets/56c9229c8885acbe4cf1.png)![](../_assets/9430ca2f6960ad0903ba.png)

Bu ürünlere ait iş emirleri çizelgelendiğinde sonuç aşağıdaki şekildedir.

![](../_assets/a5f8b7ab82a5ead14a1b.png)

![](../_assets/79e4b0d131c869fde014.png)

![](../_assets/84a1d7ba5b6a558e7246.png)

İlk olarak 4 adet B ürünü (20 M3) fırının tamamını dolduracak şekilde tek başına fırına alınır ve 6 saat sonra fırından çıkar. (07.12.2023 08:00- 07.12.2023 14:00)

Daha sonra kalan 2 adet B ürünü (10 M3) fırının %50'sini doldurur ve bunun yanında diğer üründen ne kadar alabileceğini hesaplar. A ürünü 10 M3 ile tüm fırını dolduruyordu fakat %50 boş yerimiz kaldığı için en fazla A ürününden 5 M3 daha yanına alabilir. Fakat A ürününün birim çevrimlerine bakıldığında 1 adet A ürünü 2 M3 olduğundan en fazla fırına 2 adet (4 M3) alabiliriz. Böylece %40 (4 M3 /10 M3) daha kapasite dolar ve fırın A ve B ürününü birlikte işleyerek toplamda %90 kapasite ile çalışır.

(B ürünü 07.12.2023 14:00-07.12.2023 20:00 - A ürünü 07.12.2023 14:00-07.12.2023 18:00)

07.12.2023 18:00 de 2 Adetlik A ürünü fırından çıkar ve kapasite %40 azalarak toplamda %50 seviyesine gelir, B ürününü işlemi 6 saat olduğu için hala fırında kalmaya devam eder. Boşalan kapasite için kalan 1 adetlik A ürünü de fırına alınır ve bu işlem de 4 saat daha devam eder. (A ürünü 07.12.2023 18:00- 07.12.2023 22:00)

Bu şekilde fırın tipli makine üzerinde aynı anda birden fazla ürünün çizelgelemesi tamamlanmış olur.
