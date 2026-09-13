---
title: "Faturada Stopaj Uygulaması"
page_id: "127697030"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Faturada Stopaj Uygulaması"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Faturada Stopaj Uygulaması"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWExOTNjNmJiLTY1YjUtNDAzMS1hNGRlLWY4NmNlZjg1Y2ZkMCZsaW5rPTRiMTcyMDJhLTFmOTktNDM4Mi04ZTBmLTk1OTM2Yzk1ZTQ0NSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=a193c6bb-65b5-4031-a4de-f86cef85cfd0&link=4b17202a-1f99-4382-8e0f-95936c95e445&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "faturada-stopaj-uygulamasi_127697039_127697030.html"
source_version: "2023-11-24T09:41:17.197+03:00"
source_bytes: 2379924
fetched_at: "2026-09-13T04:23:11+00:00"
generator: "netsis-scraper 1.0.0"
---
# Faturada Stopaj Uygulaması

Faturada stopaj uygulaması hakkında ayrıntılı bilgiye bu dokümandan ulaşılır.

9.0.31 sürümü ile gelir vergisi stopaj uygulaması alış ve satış faturalarında desteklenmiştir.

Uygulamanın kullanılabilmesi için alış ve satış fatura parametrelerinde yer alan stopaj uygulamasında kullanılacak olan ek maliyet alanının seçilmesi gerekmektedir.
![](../_assets/413759d58dce4e26ca03.png)![](../_assets/bee5fb85cc238ef85bce.png)

Bu parametre hizmet uygulaması parametresi ile birlikte çalışmaktadır. Hizmet uygulaması parametresi aktif ise stopaj uygulamasında kullanılacak olan saha seçimi yapılabilir. Eğer stopaj uygulaması kullanılmasın isteniyorsa bu parametrede "Stopaj Kullanılmasın" seçeneği seçilmelidir.

Tüm stoklar için stopaj uygulaması kullanımı için 'FATURA','STOPAJTUMSTOKLAR' özel parametresi tanımlanmalıdır.

Örneğin, satış fatura parametrelerinde stopaj uygulaması için saha olarak Ek Maliyet-3 alanı seçilirse, Ek Maliyet sekmesinde Ek Maliyet-3 alanı aktif edilip Stopaj adlandırması yapılabilir.

![](../_assets/490b07807e5f1b1cc296.png)

Stopaj uygulaması aktif edildiğinde belge kaleminde stopaj oranı girilebilmektedir.

![](../_assets/63f8ffd167c76902f744.png)

Fatura toplamlarına ise belirlenen ek maliyet sahasında stopaj tutarı görülmektedir.

![](../_assets/3cb198d5602884901412.png)

HIZ001 kodlu belge kalemi için hesaplama; (Birim fiyat\*Stopaj oranı/100)  100\*10/100= 10 HIZ002 kodlu belge kalemi için hesaplama; (Birim fiyat\*Stopaj oranı/100)  300\*15/100 = 45 Toplam Stopaj: 10 + 45 = 55 olarak hesaplanmaktadır.

Satış faturasının e-belgesi oluşturulduğunda stopaj tutarları, kalem bazında Diğer Vergiler alanında ve toplamlarda ise Hesaplanan STP alanında oran bazında görülmektedir.

![](../_assets/dd73ab89713a4131bfb2.png)
