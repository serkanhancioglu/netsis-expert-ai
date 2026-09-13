---
title: "Sipariş ve Teklif Belgelerinde Revizyon"
page_id: ""
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Sipariş ve Teklif Belgelerinde Revizyon"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Sipariş ve Teklif Belgelerinde Revizyon"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTI0MmQ4MDhiLTc3NjgtNDFjZS1hZjVmLTc4MmE0MGY3ZGMxOCZsaW5rPTIwZjA5YzRkLTkxOTQtNGZlZC04YzM5LWIwMTY3ODExZTAyMCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=242d808b-7768-41ce-af5f-782a40f7dc18&link=20f09c4d-9194-4fed-8c39-b0167811e020&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "siparis-ve-teklif-belgelerinde-revizyon.html"
source_version: ""
source_bytes: 10832
fetched_at: "2026-09-13T04:21:49+00:00"
generator: "netsis-scraper 1.0.0"
---
# Sipariş ve Teklif Belgelerinde Revizyon

Bu dokümanda sipariş ve teklif belgelerinde revizyon işlemlerine değinilecektir. Belge üzerinden yapılacak revizyon işlemleri, Müşteri -Satıcı Siparişleri, Satış Teklif ve Satın Alma Teklif belgelerinde desteklenmektedir.

Belge üzerinden revizyon yapabilmek için ilgili belgenin üst bilgiler sekmesi üzerinden sağ klik “Revizyon- Sipariş Revize Edilsin” seçeneği ile yeni oluşturulan sipariş belgesinde güncelleme yapılabilir.

**Örnek 1:** Sipariş belgesi aşağıdaki şekildedir. İlgili sipariş üzerinde miktar bilgisi azaltılarak revizyon değişikliği yapılmak istenmiştir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/4feba9ce-cddf-4a31-9808-8bf1d18357af/rev1.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/bdb9129d-569e-4bc1-a4e0-56dcc1c784e8/rev2.png)

İlgili belge üzerinde sağ klik “Revizyon – Sipariş Revize Edilsin” seçeneğine tıklandığında, oluşacak yeni sipariş belgesine ait numara ve eski belgede girilmiş olan kalemlerde kapalı satırlar var ise onların da yeni belgeye aktarılmasını sağlayan parametrenin olduğu bir ekran karşımıza çıkacaktır. Satır Bazında Teslim Tarihi Sorulsun parametresi açık ise Başlangıç Teslim Tarihi alanı aktif gelmektedir. Buradaki Başlangıç Teslim Tarihi alanı kalemler girilen teslim tarihi için verilecek başlangıç tarihini ifade eder. Örneğin belge kalemlerinde 15.10.2024 ve 20.10.2024 teslim tarihli iki kalem mevcut ise ve başlangıç teslim tarihi 18.10.2024 tarihi verildi ise bu tarihten büyük olan 20.10.2024 tarihli belge yeni belge kalemine eklenecektir. Teslim tarihi alanı olarak kalemlerin yükleme tarihi dikkate alınmaktadır. Tamam butonuna basıldığında ise “Revizyon işlemi yapılacak devam edilsin mi?” sorusuna “Evet” denildiğinde yeni belge onaylanmamış şekli ile oluşturulup tamamlanması beklenecektir. Verilen başlangıç tarihinden sonraki tarihler için sipariş kalemlerinde uygun kalem bulunamaz ise "ZZ tarihinde ve veya sonrasında teslim edilecek kalem bulunamadı" uyarısı ile karşılaşılacaktır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/36c43305-e90a-42e1-9fd1-35076bd26a67/rev3.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/ef891d0b-27b2-429f-bf8b-7a34e5e6a50e/rev4.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/5b99b927-b29a-4c5b-832c-f1e9b714ba1d/rev5.png)

Oluşan yeni belge üzerinde değişiklikler yapılıp, belge tamamlanır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/129063f9-3e71-4b26-808a-951a25181def/rev6.png)

Yeni belge üzerinden bir önceki sipariş belgesine de üst bilgiler sağ klik “Revizyon – Önceki Sipariş” seçeneği ile ulaşılabilmektedir. Yine aynı şekilde eski belge üzerinden de “Sonraki Sipariş” seçeneği ile yeni belgeye ulaşılabilmektedir. (Yeni belgeye ait TBLSIPAMAS tablosundaki S_YEDEK1 kolonunda eski sipariş belgesinin numarası tutulmaktadır.)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/dd0d1d5e-6302-4f3d-85f9-013aac33920e/rev7.png)

Önceki belgeye giriş yapıldığında artık ilgili belgenin kalemlerinin ve sipariş belgesinin tamamı kapatılmış durumuna gelmiştir ve siparişin kapatıldığına dair uyarı mesajı ekrana gelecektir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/c19ebbe3-e0d3-41a6-aa8f-09928fb0b8d3/rev8.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/7214deab-3525-47a8-b3a2-37703fc36403/rev9.png)

**Örnek 2:** Sipariş belgesi aşağıdaki şekildedir. İlgili sipariş üzerinde miktar bilgisi arttırılarak revizyon değişikliği yapılmak ve fakat sipariş numarası değişmeden ilk girilen belgenin numarası ile kullanıma devam edilmek istenmesi durumunda, Yardımcı Programlar – Özel Parametre Tanımları ekranı üzerinden Grup Kodu: BELGEREVIZYON, Anahtar: ALTERNATIF, Değer:0 olan özel parametre tanımı yapılmalıdır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/eb8c6445-f3b4-42ef-b982-f05ff8d3ef4a/rev10.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/e8b2ddcd-cf29-4fd1-ad02-4a4b629e50ab/rev111.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/708b651d-8ca0-469f-a645-2dc42833e479/rev12.png)

Tamamlanan belge üzerinde sağ klik Revizyon- Sipariş Revize Edilsin seçeneğine tıklanır. Bu durumda karşımıza “Belge Revizyon” isimli bir ekran çıkmakta ve bu ekrana açıklama girişi yapılabilmektedir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/e29c80d6-1728-4bde-b428-24abd2088e9e/rev13.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/422ffeaf-740e-4bdf-92f8-2e41f4c7091d/rev14.png)

Tamam butonuna basıldığında program otomatik olarak REV ile başlayan son kalınan numara üzerinden belgenin ilk halini sipariş kapatılmış olarak saklayacaktır. Böylece aynı sipariş numarası üzerinden güncelleme yapılmaya devam edilebilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/8ad82798-d346-40b1-b121-8ec4a7f513e4/rev15.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/be630d24-bf56-4207-9e22-951f662763df/rev16.png)

Özel parametre tanımlı iken yapılan revizyona ait detay bilgileri TBLFATUREV tablosunda yer almaktadır.
