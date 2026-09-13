---
title: "Lokal Depo Bazında Muhasebe Entegrasyonu"
page_id: "91718649"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Lokal Depo Bazında Muhasebe Entegrasyonu"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Lokal Depo Bazında Muhasebe Entegrasyonu"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTAwNDI0NzQ0LWI4NDEtNGVlOS04OWY0LWI5NWNjYzliMGZmNiZsaW5rPWRiMTlmZjA2LTNhZjktNDk1My04ZmNmLWEyNDMzMDBjNGYxMSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=00424744-b841-4ee9-89f4-b95ccc9b0ff6&link=db19ff06-3af9-4953-8fcf-a243300c4f11&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "lokal-depo-bazinda-muhasebe-entegrasyonu_91718658_91718649.html"
source_version: "2022-11-02T14:12:52.423+03:00"
source_bytes: 1473050
fetched_at: "2026-09-13T04:23:50+00:00"
generator: "netsis-scraper 1.0.0"
---
# Lokal Depo Bazında Muhasebe Entegrasyonu

Lokal Depo Bazında Muhasebe Entegrasyonu ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Lokal depo uygulaması ile, firmalar ürünlerini hangi depoda kaç adet olduğu detayı ile takip edebilir. Bunun muhasebe karşılığında ise stok kartında detay kodu ve detay kodunda satışa-alışa bağlı tek hesap bağlanabilir. Bu takibin depo bazında farklı hesaplar çalışacak şekilde düzenlenmesi lokal depo bazında muhasebe entegrasyonu uygulaması ile mümkündür. Bu uygulama ile karta tek detay kodu bağlanır, depo bazında detay kodları ayrıca tanımlanır ve belgede seçilen depoya göre bu farklı detay kodlarının çalışması sağlanır.

Lokal depolara göre muhasebe entegrasyonunun gerçekleşmesi için; öncelikle Satış/Alış Fatura Parametreleri ekranı, Depolar Arası Transfer/Ambar Giriş Çıkış sekmesinde bulunan, "Lokal Depo Bazında Muhasebe Entegrasyonu Yapılsın" parametresi işaretlenmelidir.

![](../_assets/ee1c43f593846b5d3328.png)

Lokal Depo Bazında Muhasebe Entegrasyonu Yapılsın parametresinden sonra yapılacak işlem, depo bazında Stok detay kodlarını tanımlamak olacaktır. Yapılacak yeni detay kodu tanımında ilk iki karakter depo kodunu, son iki karakter ise stok kartındaki detay kodunu içermelidir.

Bunu bir örnek ile açıklayalım; havlu stokunun satışı eğer defolu ürün ya da zayi ürün deposundan yapılıyorsa satış hesaplarının değişmesi istenmektedir. Bu durumda zayi deposu ve defolu ürün deposu için iki ayrı stok detay kodu tanımlanmalıdır. Bu detay kodları tanımlanırken ilk iki karakter depo kodunu, son iki karakter stok kartındaki detay kodunu içermelidir.

![](../_assets/2e3fc9e7bb7ba91d2bab.png)![](../_assets/3472a1a5afd7230494bc.png)

12 depo kodu 1 detay kodu için 1201, 13 depo kodu 1 detay kodu için 1301 detay kodları tanımlanır.

![](../_assets/22f3e2d32022e7f0869d.png)![](../_assets/55ed241a5690d04dc5fb.png)![](../_assets/55ed241a5690d04dc5fb.png)

Faturada seçilen depo koduna göre detay kodları program tarafından taranır, ilk iki karakteri ve stok kartındaki detay kodu uyumlu olan detay kodu çalıştırılır.

![](../_assets/0fb8a30a6151dd1f7e7d.png)

Havlu stoku 13 numaralı depodan 1 adet 100 TL olarak, 12 numaralı depodan 1 adet 80 TL olarak satılmıştır. Faturanın yevmiye fişine baktığımızda 100 TL için 1301 detay koduna bağlanmış olan 600-00-004 hesap kodu, 80 TL için 1201 detay koduna bağlanmış olan 600-00-003 hesap kodu çalışmıştır. Detay kodu 4 karakter ile sınırlıdır. Taranacak detay kodu oluşturulurken sondan başlanır ve öncelikle stok kartından detay kodu alınır. Stok kartındaki detay kodu tek karakterse başına 0 eklenir. Örneğin detay kodu 1 ise 01 olarak alınır. Bunun önüne ise satış-alış evrakında kullanılan depo kodu eklenir. Bu aşamada depo kodu 1 karakter ise olduğu şekilde kullanılmalı başına 0 konulmamalıdır. Depo kodumuzun 1 olduğunu varsayarsak tanımlanması gereken detay kodu 101'dir. Stok kartındaki depo kodu ya da lokal depo kodunun iki karakter uzunluktan fazla olması kullanılacak detay kodunun bulunmasını engelleyecektir.
