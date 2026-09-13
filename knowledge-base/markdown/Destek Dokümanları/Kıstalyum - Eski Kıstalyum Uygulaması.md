---
title: "Kıstalyum - Eski Kıstalyum Uygulaması"
page_id: ""
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Kıstalyum - Eski Kıstalyum Uygulaması"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Kıstalyum - Eski Kıstalyum Uygulaması"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTkyNWI5YzNkLWEwZTAtNDEyZC05MTViLTYzYWIzNjU4NWFjYiZsaW5rPTA5NGQ3YzljLWM1MDctNDk3My1hMTYyLTllYTBkMzNiNzI3MCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=925b9c3d-a0e0-412d-915b-63ab36585acb&link=094d7c9c-c507-4973-a162-9ea0d33b7270&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "kistalyum-eski-kistalyum-uygulamasi.html"
source_version: ""
source_bytes: 10260
fetched_at: "2026-09-13T04:21:59+00:00"
generator: "netsis-scraper 1.0.0"
---
# Kıstalyum - Eski Kıstalyum Uygulaması

Binek otomobillerinin aktife dahil edildiği ilk yıl amortismanları VUK madde 320 gereği kıst olarak ayrılmaktadır. Kanun maddesi gereği ilk yıl ayrılmayan amortisman, itfa süresinin son yılında dikkate alınmaktadır.

Normal amortisman yönteminin uygulandığı, yani amortisman oranının binek otomobilinin maliyet bedeline uygulandığı yöntemde ilk yıl ayrılmayan amortismanın herhangi bir önemi, etkisi bulunmamakta, itfa süresinin son yılında ilaveten dikkate alınmaktadır.

Ancak, azalan bakiyeler usulüyle (hızlandırılmış) amortisman ayrılması durumunda, yani, her yıl net defter değerine (maliyet bedelinden birikmiş amortisman düşüldükten sonraki değerine) amortisman oranının uygulanması yönteminde, net değere ulaşırken ilk yıl ayrılmayan kıst amortismanın ne şekilde dikkate alınması gerektiği konusunda iki farklı görüş bulunmaktadır.

Bu dokümanda demirbaş modülünde yer alan kıstalyum ve eski kıstalyum uygulamasının azalan bakiyeler usulüne göre (hızlandırılmış) farklı görüşlerin kullanımına değinilecektir.

Örnek: 16.11.2005 tarihinde 25.000 TL maliyet bedeli ile aktife dahil edilen bir binek otomobil için azalan bakiyeler usulünde ve %40 oranında amortisman uygulanacaktır. İşletmenin söz konusu binek otomobili için yıllar itibariyle ayıracağı amortisman tutarları aşağıdaki gibi olacaktır.

\1) İlk yıl ayrılmayan amortismanın devam eden yılda ayrılmış olarak kabulü ile amortisman matrahının tespiti görüşüne göre:

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/93de70a8-3f7a-4715-9835-7e1a8bb4c3e6/ekran 1.jpg)

Bu görüşe göre demirbaş modülü Parametre Girişi ekranında **eski kıstalyum** parametresi işaretli **olmamalı,** Demirbaş Bilgi Kartında ise **kıstalyum** parametresi ve amortisman tipi **hızlı** seçili olmalıdır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/996c93ba-604a-4aa9-9660-90573e23c97e/dem1_1.jpg)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/2a1f3398-fdfa-4d4f-b305-68098fa69142/dem1.jpg)

**1. Yıl aylık amortisman tutarı;**

25000\*0,40=10000/12=833,33 (11.ay)

833,33\*2=1666,67 (11. ve 12. ay toplam birikmiş amortisman)

Devreden Amortisman Tutarı = 10000-1666,67=8333,33

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/14ad56ea-7413-4135-8f98-b38eb4814adf/dem2.jpg)

**2. Yıl aylık amortisman tutarı;**

Bu yöntemde ilk yıl amortismanın tam ayrıldığı kabul edilmektedir. Bu yüzden birikmiş amortisman 10000 üzerinden hesaplamalar yapılmaktadır.

25000-10000=15000 (sabit kıymet- birikmiş amortisman tutarı)

15000\*0,40=6000 (yıllık amortisman tutarı)

Aylık amortisman=6000/12=500

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/4e8a537e-12ae-4fa0-ac3e-919d0b6c608c/dem3.jpg)

**3. Yıl aylık amortisman tutarı;**

25000-16000=9000 (sabit kıymet- birikmiş amortisman tutarı)

9000\*0,40=3600 (yıllık amortisman tutarı)

Aylık amortisman=3600/12=300

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/a36bb848-a41e-4813-829f-079296f70638/dem4.jpg)

**4. Yıl aylık amortisman tutarı;**

25000-19600=5400 (sabit kıymet- birikmiş amortisman tutarı)

5400\*0,40=2160 (yıllık amortisman tutarı)

Aylık amortisman=2160/12=180

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/123eb00d-6eec-42a4-8d67-5733da21fd52/dem5.jpg)

**5. Yıl aylık amortisman tutarı;**

25000-21760=3240 (sabit kıymet- birikmiş amortisman tutarı)

Son yıl ilk yıl ayrılmayan tutar da eklenir. 3240 +8333,33 =11573,33 (yıllık amortisman tutarı)

Aylık amortisman=11573,33/12=964,44

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/1e5d6793-311c-420a-96f0-ef80be8a48bc/dem6.jpg)

\2) İlk yıl ayrılan kıst amortismanın birikmiş amortisman kabulü ile amortisman matrahında dikkate alınması gerektiği görüşüne göre:

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/a894be78-f49c-49b4-a2ac-a0edf23f9a9b/ekran 2.jpg)

Bu görüşe göre demirbaş modülü Parametre Girişi ekranında **eski kıstalyum** parametresi işaretli **olmalı,** Demirbaş Bilgi Kartında ise **kıstalyum** parametresi ve amortisman tipi **hızlı** seçili olmalıdır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/e39f3d37-a7f9-4e6c-8e51-6aa3f6870950/dem7.jpg)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/c5512224-e989-4d64-8bfb-de567ff4dfba/dem8.jpg)

**1. Yıl aylık amortisman tutarı;**

25000\*0,40=10000/12=833,33 (11.ay)

833,33\*2=1666,67 (11. ve 12. ay toplam birikmiş amortisman)

Devreden Amortisman Tutarı = 10000-1666,67=8333,33

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/d2599895-2984-44fe-8ec2-3fed57dd5696/au_dem1 (2).jpg)

**2. Yıl aylık amortisman tutarı;**

25000-1666,67=23333,33 (sabit kıymet- birikmiş amortisman tutarı)

23333,33 \*0,40=9333,33 (yıllık amortisman tutarı)

Aylık amortisman=9333,33 /12=777,78

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/2abe4a80-8593-47b8-ab95-b85b4b82c913/dem9.jpg)

**3. Yıl aylık amortisman tutarı;**

25000-11000=14000 (sabit kıymet- birikmiş amortisman tutarı)

14000 \*0,40=5600 (yıllık amortisman tutarı)

Aylık amortisman=5600 /12=466,67

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/6c66e604-5251-4b44-8e98-53d6f4951fa0/dem10.jpg)

**4. Yıl aylık amortisman tutarı;**

25000-16600=8400 (sabit kıymet- birikmiş amortisman tutarı)

8400 \*0,40=3360 (yıllık amortisman tutarı)

Aylık amortisman=3360 /12=280

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/5f7ab18e-6318-4d52-ab86-d46baa93058a/dem11.jpg)

**5. Yıl aylık amortisman tutarı;**

25000-19960=5040 (sabit kıymet- birikmiş amortisman tutarı)

Aylık amortisman=5040 /12=420

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/6228fa7d-58a7-4955-8413-ed16e992d21b/dem12.jpg)

Görüldüğü gibi sonuç itibariyle her iki yöntemde de ayrılacak amortisman tutarı aynıdır. Sadece ikinci görüşte birinci görüşe göre 2., 3. ve 4. yıllarda daha fazla amortisman gideri yazılmaktadır.
