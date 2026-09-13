---
title: "Ebat Uygulamasının Hacim Olarak Hesaplanması"
page_id: "128583270"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Ebat Uygulamasının Hacim Olarak Hesaplanması"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Ebat Uygulamasının Hacim Olarak Hesaplanması"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTM1NDFkZDY5LTc1ZjUtNGIyYi04Y2JiLWIyY2JjOTc5NzQ2YiZsaW5rPTU3YWM0ZWM5LTQ2MTktNDU1MS1hODMxLWU3OGM3YTM3ZmMwNCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=3541dd69-75f5-4b2b-8cbb-b2cbc979746b&link=57ac4ec9-4619-4551-a831-e78c7a37fc04&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ebat-uygulamasinin-hacim-olarak-hesaplanmasi_128583270_128583270.html"
source_version: "2023-12-25T11:02:18.290+03:00"
source_bytes: 1494110
fetched_at: "2026-09-13T04:23:04+00:00"
generator: "netsis-scraper 1.0.0"
---
# Ebat Uygulamasının Hacim Olarak Hesaplanması

9.0.47 setiyle birlikte, ebat uygulamasının metreküp olarak hesaplanabilmesi desteklenmiştir.

Metreküp olarak ebat hesaplama uygulamasının çalışabilmesi için, Satış Fatura Parametreleri / Genel-2 Sekmesinde yer alan **Ebat Bilgisi Girilsin** ve **Ebat Hacim Hesaplansın** parametrelerinin işaretlenmesi gerekmektedir.
![](../_assets/0e9b7de51ff1113a693e.png)

Bu parametre işaretli olduğunda faturada ek alan sahasına **"En X Boy X Yükseklik"** şeklinde üç değişken için giriş yapılabilmesi sağlanır. Ek alanda 2 çarpan varsa metrekare , 3 çarpan varsa metreküp olduğu anlaşılabilir. **"En X Boy X Yükseklik"** hesabı yapılırken metrekare hesaplamasında olduğu gibi ebatların kaça bölündüğü bilgisi dikkate alınarak işlem yapılmaktadır.

Ek alan sahasına girilen değişkenler çarpılıp, miktar sahasına çarpım sonucu yazılır.
![](../_assets/be546cf172dea45d4611.png)

Belli bir adet sayısı için metreküp hesaplaması yapılması isteniyorsa, miktar sahasına girilen adet değeri, ek alanda girilmiş olan **"En X Boy X Yükseklik"** hesabından elde edilen çarpım değeri; adet değeri ile çarpılarak ve ebatların kaça bölündüğü bilgisi dikkate alınarak girilen adet bilgisi için metreküp hesabı miktar sahasına yazılır. Miktar 2 de ise girilmiş adet bilgisi yer almaktadır.
![](../_assets/ad03ba3b96a713d6f8b0.png)
En, boy, yükseklik bilgisi, stoklar için önceden biliniyorsa bu durumda; stok kartı kaydı ekranında **Stok** **Kart-2** sekmesinde yer alan ebat bilgileri alanları kullanılabilir.

Stok kartında ebat bilgileri dolu ve satış parametrelerinde hacim hesaplansın parametresi işaretliyse, bu durumda fatura kalemlerinde, ek alan1 sahasına stok kartında yer alan en-boy-genişlik bilgileri **"En X Boy X** **Yükseklik"** şeklinde otomatik yazılır ve hesaplama yapılır.

![](../_assets/9565ed33b5f4f1d6ab63.png)

![](../_assets/828186d0ecb9f2a2d22c.png)

Metrekare ebat hesaplamasında olduğu gibi, metreküp hesaplamasında da 1.ölçü birimine metreküp, 2. ölçü biriminde en-boy-yükseklik hangi ölçü biriminden girilecekse bu bilgi girilmelidir, 3. bir ölçü birimi varsa istenirse bu bilgi de stok kartına tanımlanabilir.
