---
title: "İleri Üretim Planlama Manuel Montaj Tipli Makine Örneği"
page_id: "166395963"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "İleri Üretim Planlama Manuel Montaj Tipli Makine Örneği"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / İleri Üretim Planlama Manuel Montaj Tipli Makine Örneği"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWRjMDAwYTcwLTY1NGMtNGEzYS04YTJiLWI4MWYwYTk1MWMxZCZsaW5rPWM2MjM2OTQzLWM1ZDctNGU1OS1hZjhhLTllZDQ0YmI1MzAyOSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=dc000a70-654c-4a3a-8a2b-b81f0a951c1d&link=c6236943-c5d7-4e59-af8a-9ed44bb53029&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ileri-uretim-planlama-manuel-montaj-tipli-makine-ornegi_166395969_166395963.html"
source_version: "2025-02-04T08:45:33.607+03:00"
source_bytes: 86132
fetched_at: "2026-09-13T04:22:17+00:00"
generator: "netsis-scraper 1.0.0"
---
# İleri Üretim Planlama Manuel Montaj Tipli Makine Örneği

Bu dokümanda ileri üretim planlama ile manuel montaj tipli makineler üzerinde bir çizelgeleme örneğine yer verilmiştir.

İleri üretim planlama modülünde, **"Manuel Montaj"** tipli makinelerde aynı anda farklı sayılarda kaynağın çalışması mümkündür. Bu makineler, bir montaj masası etrafında birden fazla operatörün aynı anda çalışması olarak düşünülebilir. "Manuel Montaj" makine tipi seçildiğinde, **"Min.** **Çalışabilecek Kaynak Seti Sayısı"** ve **"Maks. Çalışabilecek Kaynak Seti** **Sayısı"** alanları önem kazanır. Bu alanlarda, makinede aynı anda çalışabilecek minimum ve maksimum kaynak sayısı tanımlanmalıdır. Bu değerler, "Makine Tanımlama" ekranından makine için tanımlanabileceği gibi,

"Operasyon-Makine Eşleştirme" ekranı kullanılarak ürün bazında da tanımlanabilir.

İleri üretim planlama algoritması, tanımlanan bu değerleri ve iş emrinin gecikme durumunu göz önünde bulundurarak, optimum seviyede kaynak kullanımı sağlayacak şekilde çizelgeleme yapacaktır. Bu tip makinelerde aynı anda farklı ürünlerin işlenebilmesi de mümkündür. Buna göre gerekli kaynak ataması algoritma tarafından yapılacaktır. Bu operasyonu yapabilecek maksimum ve minimum operatör sayıları da kaynak seti sayıları olacaktır.

![](../_assets/7bec19de34292f87c819.png)

Makine Tanımı

![](../_assets/bc64fb9fff459f38ee92.png)

Kaynak Tanımı

("Toplam Miktar" alanında ilgili kaynağın sayısı girilmelidir.)

![](../_assets/46570849a136ee080207.png)

Operasyon-Kaynak Eşleştirme

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/9d63bbb8-17b4-41d4-abd4-651a8bc306b5/Resim2.png)

Operasyon-Makine Eşleştirme Tanımı

Yukarıda belirtilen tanımlara göre, "OP_GOVDE_MONTAJ" operasyonu için minimum kaynak kullanıldığında 125 adet ürünün üretimi için ilgili operasyonun süresi aşağıdaki gibi hesaplanır:

(240\*125)/1=30000 (8 Saat 20 Dakika)

Maksimum kaynak kullanıldığında ise süre aşağıdaki gibi hesaplanır:

(240\*125)/8=3750 (1 Saat 2 Dakika 30 Saniye)

Algoritma, operasyonda kullanılacak kaynak sayısını belirlerken iş emrinin gecikme durumunu göz önünde bulundurur. Eğer en düşük kaynak sayısı kullanıldığında iş emrinde gecikme meydana gelmiyorsa, algoritma minimum kaynak sayısını ilgili operasyon için ayırır. Ancak, eğer en düşük kaynak sayısı kullanıldığında iş emrinde gecikme meydana geliyorsa, algoritma kaynak sayısını artırarak gecikmeyi minimize etmeye çalışır. Bu durumda, teslim tarihine en yakın şekilde operasyona kaynak ayrılması sağlanarak kaynak kullanımı optimize edilir.

Teslim tarihi 28.01.2025 olan siparişe ait yarı mamul iş emri operasyonuna, öncül iş emri operasyonlarının tamamlanması da dikkate alınarak, 28.01.2025 21:48:45'te başlandığında ilgili iş emri minimum kaynak kullanımı ile 6 saat 8 dakika 45 saniye gecikme yaşar. Bu durumda algoritma, iş emrinin gecikmemesi için kaynak sayısını artırarak 4 kaynak kullanır ve ilgili işi 2 saat 5 dakika sürede tamamlar.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/eb141638-b4dc-4144-9815-040c2604d738/MS1.png)
