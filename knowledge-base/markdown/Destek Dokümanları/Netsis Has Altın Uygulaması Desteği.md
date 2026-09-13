---
title: "Netsis Has Altın Uygulaması Desteği"
page_id: "50690625"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis Has Altın Uygulaması Desteği"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis Has Altın Uygulaması Desteği"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTkxZTk4NmU5LTAwMzQtNDg2MC04ZGNjLTdmOWQyMGExYjAzNiZsaW5rPWE2MDk0ZDYyLTNlZjktNGNkZi05ZDVhLTc1ZGM1NmNiMDk2YiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=91e986e9-0034-4860-8dcc-7f9d20a1b036&link=a6094d62-3ef9-4cdf-9d5a-75dc56cb096b&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-has-altin-uygulamasi-destegi_80090297_50690625.html"
source_version: "2022-11-02T16:09:58.413+03:00"
source_bytes: 854983
fetched_at: "2026-09-13T04:25:11+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis Has Altın Uygulaması Desteği

Netsis Has Altın Uygulaması ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Netsis Has Altın Uygulaması, kuyumcu ve sarraflar tarafından kullanılan ve altın ayar farkından oluşan işçilik bedelinin kdv hesaplamasına yöneliktir. Has altın sisteminde hesaplanmayan işçilik KDV tutarı, işçilik oranları üzerinden hesaplanarak fatura işlemlerine dahil edilebilmektedir.

Kdv hesaplarında Has Altın sistemi'ni kullanılmak için yapılması gerekenler:

- Fatura Modülü\\Satış parametreleri\\Fatura Ek 1 sekmesinde "Kdv Hesaplarında Has Altın Sistemi " parametresi işaretlenmelidir.

![](../_assets/f8f17c732d60583fcaf9.png)

- Döviz takibi modülünde Has Altın döviz tipi tanımlanmalı ve bu tip ile ilgili has altın değerleri döviz kurları girişi ekranından günlük olarak girilmelidir.

![](../_assets/061414c4c2015df5754c.png)
![](../_assets/adf9ab032166c08ac2f1.png)

- İlgili ürünün stok kartı kayıtlarında ölçü birimi çevirim değerleri ile birlikte tanımlanmalı, ayrıca Has Altın için tanımlanmış olan döviz tipi ilgili stok kartının döviz tipi sahasında seçilmelidir.

![](../_assets/d7318edbdda9bee20855.png)
![](../_assets/b854b22dbe1358f4b74d.png)
Aşağıdaki gibi bir örnek üzerinden KDV hesaplaması şu şekilde yapılmaktadır:
Kdv oranı = %18 Döviz Birim Fiyat=10 Altın Döviz Kuru=410 Miktar= 10 Gr
![](../_assets/41185948841f027610fd.png)
![](../_assets/3be2675713077d8f8bda.png)
Fatura işlemleri sırasında stoklarda belirtilmiş olan çevrim değerlerindeki has altın katsayıları ile döviz işlemlerindeki has altın değerini çarparak girilen değer arasındaki farkı bulur. Bulunan bu fark işçiliktir. Has altın sisteminde KDV hesaplaması yapılmadığından, burada bulunan farkın yani işçiliğin KDV'sini oran üzerinden hesaplayarak fatura işlemlerine dahil eder.
Miktar X Döviz Kuru (Has Altına ait) = 10 X 410= 4100 4100 X pay1/payda1= 4100 X (240/60) = 16400
16400 X 0,18= 2952
Altın uygulaması olmasaydı çıkması gereken KDV tutarı 41000 X 0,18 üzerinden 7380 tl olacaktı. Bu 7380 değerinden 2952'yi çıkardığımızda kalan 4428 tl faturamızdaki KDV tutarı olmaktadır.
