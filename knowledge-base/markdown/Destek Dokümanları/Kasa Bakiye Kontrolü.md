---
title: "Kasa Bakiye Kontrolü"
page_id: "95652806"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Kasa Bakiye Kontrolü"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Kasa Bakiye Kontrolü"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTBhYTQwOWJlLWFmNWQtNGNjNi1iZjk4LTMwODA4NzZjNzFmOSZsaW5rPTZjNGEwMTY4LTRmYzUtNGQ2ZC04N2FjLWEzMzVhZGNhZGU2ZCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=0aa409be-af5d-4cc6-bf98-3080876c71f9&link=6c4a0168-4fc5-4d6d-87ac-a335adcade6d&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "kasa-bakiye-kontrolu_95652810_95652806.html"
source_version: "2022-11-11T13:18:14.120+03:00"
source_bytes: 266091
fetched_at: "2026-09-13T04:23:47+00:00"
generator: "netsis-scraper 1.0.0"
---
# Kasa Bakiye Kontrolü

Kasa Bakiye Kontrolü ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

9.0.43. seti ile birlikte kasayı etkileyen işlemlerde kasa bakiyesinin belirli bir tutarın üzerine çıkması ya da altına düşmesi durumunda uyarı verilmesi ya da işlemin durdurulması kasa bakiye kontrolü ile sağlanmıştır.

Gelir-gider limit tutarları ve bu tutarların aşılması durumunda programın nasıl davranacağı kasa bazında belirlenir. Bu kontroller için kasa bazında kontrol türü, kontrol politikası, gider-gelir limiti kasa tanımlama ekranından girilir.

![](../_assets/8dc0edb74879ded2d46c.png)

Limit kontrolünün hangi tür evraklarda yapılacağı kontrol türü alanından belirlenir. Kasadaki nakdin belirli bir tutarın altına düşmesi istenmiyorsa giderler kontrol edilsin seçeneği kullanılarak kontrolün devreye gireceği gider limit tutarı belirlenir. Kasadaki nakdin belirli bir tutarın üzerine çıkması istenmiyorsa gelirler kontrol edilsin seçeneği kullanılarak kontrolün devreye gireceği gelir limit tutarı belirlenir. Burada kontrol girilen evrağın tutarı ya da kayıt yapılan güne ait toplam tutarlar değil, kasanın tüm hareketlerini kapsayan kasa bakiyesi üzerindedir.

![](../_assets/b772444b13e754c73a97.png)

Kontrol türü belirlendikten sonra, belirlenen kriterler aşıldığında uygulanacak olan kontrol politikası belirlenir. Burada işlem durdurulur ya da kullanıcı ekranına uyarı verilip işleme devam etmesi sağlanır.

Gider limitinin 1.000,00 TL, gelir limitinin 100.000,00 TL olarak belirlendiği bu tanımda kasa bakiyesini 1.000,00 TL'nin altına düşürecek ya da 100.000,00 TL'nin üzerine çıkarak bir evrak kaydında işlem durdurulur.

Örnekte kasa bakiyesinin 1.200,00 olduğu durumda girilen 250,00 TL'lik bir gider kaydı kasayı gider limit tutarının altına düşüreceği için kontrol politikası işlem durdurulsun ise "Kasa Limit Tutarı Aşıldı. İşlem Durduruldu." İkazı ile işlemi durdurur. Koşul politikasının uyarı verilsin olması durumunda ise "Kasa Limit Tutarı Aşıldı" uyarısı alınır ancak işlem devam eder. Aynı kontrol gelir tarafında 100.000 TL limiti üzerinden sağlanır.

![](../_assets/2c75c09d15667799724e.png)

Kasa bakiye kontrolü; Kasa kayıtları. Hızlı tahsilat/ödeme kayıtları, Kapalı fatura kaydı, Hızlı kasa – banka kayıtları ve Netopenx ile aktarılan kayıtlarında devreye girer.
