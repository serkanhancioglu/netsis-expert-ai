---
title: "Faturada Özel İletişim Vergisi Hesaplama"
page_id: "108659413"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Faturada Özel İletişim Vergisi Hesaplama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Faturada Özel İletişim Vergisi Hesaplama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWE2MTViZjkzLTgxMzQtNDhmOS1hYjhiLWQyOGNiOTdiMzFjOCZsaW5rPWY5MzRlN2U3LTU5YmQtNDQwNS1iYzU2LTc4N2FlNmEyOWFkNSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=a615bf93-8134-48f9-ab8b-d28cb97b31c8&link=f934e7e7-59bd-4405-bc56-787ae6a29ad5&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "faturada-ozel-iletisim-vergisi-hesaplama_108659423_108659413.html"
source_version: "2023-03-31T14:12:37.313+03:00"
source_bytes: 2428857
fetched_at: "2026-09-13T04:23:31+00:00"
generator: "netsis-scraper 1.0.0"
---
# Faturada Özel İletişim Vergisi Hesaplama

Faturada özel iletişim vergisi hesaplanmasıyla ilgili ayrıntılı bilgiye bu dokümandan ulaşılır.

Faturanın toplamlar sekmesinde Özel İletişi Vergisi (ÖİV) hesaplanabilmesi için FATURA/OZELILETISIMVERGISI/0 özel parametresinin tanımlanması gerekmektedir.

![](../_assets/71c44d1c6ba90777fb83.png)

Özel parametre tanımlaması yapıldıktan sonra Stok Kartı Kayıtları ekranın Ek Bilgiler sekmesi alanında gerekli düzenlemelerin yapılması gerekmektedir. Özel parametre tanımlamadan önce Stok Kartı Kayıtları ekranı Ek Bilgiler sekmesinde ÖTV alanı gelmektedir.

![](../_assets/9088aee4f188f98ac7f1.png)

Özel parametre tanımlandıktan sonra Stok Kartı Kayıtları ekranındaki ÖTV alanı ÖİV olarak değişmektedir.

![](../_assets/d339fae092b955630c9b.png)

Satış faturasında ÖİV hesaplanması için satış, alış faturasında ÖİV hesaplanması için alış parametrelerinin işaretlenmesi gerekmektedir. ÖİV vergisi oran olarak hesaplanması isteniyor ise oran, tutar olarak hesaplanması isteniyor ise tutar alanının seçilmesi gerekmektedir.

Faturalama işlemi sonrasında muhasebe kaydının yapılabilmesi için Entegrasyon kodları ekranı Fatura Ek Maliyet sekmesinde ÖİV için gerekli olan hesap kodlarının tanımlı olması gerekmektedir.

![](../_assets/bcaa3c64ad5b315b451e.png)

Aşağıdaki örneklerde satış faturasında tutar ve oran olarak ÖİV vergisinin hesaplanması gösterilmiştir.

![](../_assets/fec23ea5cad719b588a5.png)

![](../_assets/c54e73c541ee7fa921d1.png)

![](../_assets/240586f92927acff0746.png)

Stok Kartı Kayıtları ekranında Oran %20 olarak tanımlanmıştır. Brüt tutar 200,00 TL üzerinden %20 ÖİV 40,00 TL olarak hesaplandığı görülmüştür.

![](../_assets/5edbba8ed21bd57c244e.png)

Toplu E-Fatura Oluşturma ekranından general.xslt dizayn ile e-Fatura oluşturulduğunda e-Belge görüntüsünde ÖİV alanı gelmektedir.

![](../_assets/7c5401a6bd44a951d38d.png)
