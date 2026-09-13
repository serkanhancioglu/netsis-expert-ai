---
title: "e-Faturadan Alış Faturası Oluşturmada Otomatik Cari Kart Oluşturma"
page_id: ""
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "e-Faturadan Alış Faturası Oluşturmada Otomatik Cari Kart Oluşturma"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / e-Faturadan Alış Faturası Oluşturmada Otomatik Cari Kart Oluşturma"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTExZTQ3OTFkLThlZDEtNGQ1My05MzAxLWY2ZDI2YTQwMzg0OCZsaW5rPWJiMjdkYTUyLWJmYjMtNGU5OC05NTYyLWRmMGU0Y2M4NzJhNCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=11e4791d-8ed1-4d53-9301-f6d26a403848&link=bb27da52-bfb3-4e98-9562-df0e4cc872a4&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "e-faturadan-alis-faturasi-olusturma-isleminde-cari-karti-olusturma-destegi.html"
source_version: ""
source_bytes: 3713
fetched_at: "2026-09-13T04:22:02+00:00"
generator: "netsis-scraper 1.0.0"
---
# e-Faturadan Alış Faturası Oluşturmada Otomatik Cari Kart Oluşturma

9062 setiyle birlikte Fatura Bazında Gelen e-Fatura ekranında e-Faturadan Alış Faturası Oluşturma işleminde otomatik cari kart oluşturma desteği getirilmiştir.

Fatura Bazında Gelen e-Fatura ve e-Faturadan Alış Faturası Oluşturma ekranlarında Alış Faturası Oluşturma işleminde, ilgili e-Belgeye ait cari için vergi kimlik numarası veya tc kimlik numarasının geçtiği bir Cari Hesap Kaydı’ nın bulunmaması durumunda hızlı bir şekilde bu cariye ait kayıt oluşturulabilmesi desteklenmiştir.

Fatura Bazında Gelen e-Fatura ekranında ilgili kayıt üzerinden sağ click e-Faturadan Alış Faturası Oluşturma işleminde veya e-Faturadan Alış Faturası Oluşturma işleminde ilgili kayıt seçilerek Alış Faturası Oluştur işlemiyle e-Belgede yer alan cari için vergi kimlik numarası veya Tc Kimlik Numarası kayıtlı bir cari kart yoksa karşımızda “**Cari Bilgilerine Ulaşılamadı. e-Fatura bilgileri ile yeni bir cari hesabı kaydedilsin mi?**” uyarı ekranı gelir. Bu uyarıya “**Evet**” denildiğinde hızlı bir şekilde cari kartın oluşturulması sağlanmaktadır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/f26e8642-3f1f-4376-938f-410d133d42ec/image (2).png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/a4bf89fe-566e-4d87-92b8-71c8e9a35427/image (3).png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/04b7aee5-1348-4f35-887e-25f9a08692fa/image (4).png)

Bu ekranda e-Fatura xml içerisinde yer alan vergi dairesi, vergi numarası veya tc kimlik numarası, adres, il, ilçe ve cari isim bilgisi otomatik olarak doldurulacaktır.

Ekran ilk açıldığında cari kodu alanı, **EFAT_CARI** isminde geçici bir cari kod bilgisi ile dolu olarak gelmektedir. Bu cari kod bilgisi istenen cari kod bilgisi ile değiştirilebilir. Hesap tipi ve alış faturası oluşturulmak için gereken muhasebe kodu bilgileri de bu ekran üzerinden tanımlanabilmektedir.

e-Fatura belgesi dövizli olması durumunda, bu ekranda “Dövizli Cari” parametresi işaretli olarak gelmektedir. Döviz tipi alanı da aktif olarak gelmekte ve istenirse döviz tipi seçilebilmektedir.

Bu şekilde cari kart hızlı bir şekilde tanımlanmış olacak ve e-Faturadan Alış Faturası Oluşturma işlemi devam etmiş olacaktır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/46baa85f-e9db-47e0-af4b-b37305dffaa6/image (5).png)
