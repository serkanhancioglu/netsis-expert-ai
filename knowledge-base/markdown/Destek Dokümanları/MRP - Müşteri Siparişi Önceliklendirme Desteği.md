---
title: "MRP - Müşteri Siparişi Önceliklendirme Desteği"
page_id: "50669161"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "MRP - Müşteri Siparişi Önceliklendirme Desteği"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / MRP - Müşteri Siparişi Önceliklendirme Desteği"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWVkNDA4YWZiLTE1ZjAtNDFmMS1iYjYwLTMzNmU5YWUyNjEyNSZsaW5rPTQzMzVkZDhlLWUxOGItNDEyYS04MGVlLWVjM2M0NDJlYmQ3NSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=ed408afb-15f0-41f1-bb60-336e9ae26125&link=4335dd8e-e18b-412a-80ee-ec3c442ebd75&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "mrp-musteri-siparisi-onceliklendirme-destegi_50669167_50669161.html"
source_version: "2022-11-03T09:03:29.713+03:00"
source_bytes: 385550
fetched_at: "2026-09-13T04:25:34+00:00"
generator: "netsis-scraper 1.0.0"
---
# MRP - Müşteri Siparişi Önceliklendirme Desteği

MRP-Müşteri Siparişi Önceliklendirme Desteği ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

MRP'de müşteri siparişi önceliklendirme desteği sayesinde müşteri siparişlerine öncelik verilmesi ve böylece MRP'nin aynı teslim tarihine sahip müşteri siparişlerini verilen önceliklere göre sıralaması sağlanır. Böylece MRP'de serbest hammadde ve mamul stoklarının müşteri sipariş ihtiyaçlarına tahsis edilmesi, verilen öncelik sırasında yapılır. Müşteri siparişi önceliklendirme özelliği, sipariş bazında rezervasyon sistemiyle desteklenir. Müşteri siparişi için önceliklendirme yapmak amacıyla MRP Parametreleri-"Genel 2" sekmesinde iki parametre bulunur.

![](../_assets/87a368296cae31736924.png)

1- Müşteri Siparişi Sıralama Kriterinin Tutulacağı Saha: Bu alanda müşteri siparişi içinde satır bazında bilgi tutulacak alanlar listelenir. Bu alanlardan herhangi biri seçildiğinde, müşteri siparişinin öncelik bilgisi seçilen alandan okunur.

2- Müşteri Sipariş Önceliği İçin Planlama Kayıtlarına Bakılsın: Parametre sayesinde MRP'nin müşteri siparişi öncelik bilgisini planlama kayıtlarından okuması mümkün hale gelir. Bu aşamada planlama kayıtlarındaki "Öncelik" alanı dikkate alınır.

Planlama kayıtlarından gelecek öncelik bilgisinin belirlenmesi için sırasıyla şu tanımlara bakılır; Müşteri/Satıcı Stok Kayıtları ekranındaki öncelik bilgisi, Cari Planlama Kayıtları ekranındaki öncelik bilgisi ve Stok Planlama Kayıtları ekranındaki öncelik bilgisi.

Yukarıdaki iki parametre birlikte seçilirse, ilk olarak sipariş sıralama kriterinin tutulacağı sahaya bakılır. Eğer bu sahaya herhangi bir değer girilmemişse planlama kayıtlarından gelen öncelik bilgisi dikkate alınır. Müşteri siparişi önceliklendirme özelliği aynı tarihli ihtiyaçlar arasında sıralama yapılması amacıyla geliştirildi. İhtiyaçların haftalık, aylık gibi periyotlarda kümüle edildiği durumlarda, önceliklendirme özelliği kümüle edilen gün içinde kullanılabilir.

#### Örnek Uygulama

Sipariş bazında takip edilen MAMUL1 stok kodlu mamul için aynı tarihli iki adet ihtiyaç satırı bulunur.

Bu ihtiyaçlar aşağıdaki gibi iki ayrı müşteri siparişinden ortaya çıkar:

![](../_assets/c1209fd0e263f8712571.png)

![](../_assets/4914a8ef5b3437280b8e.png)![](../_assets/9eef16f0373a0a329d65.png)

MRP Parametreleri-Genel 2-"Müşteri Siparişi Önceliği İçin Planlama Kayıtlarına Bakılsın" parametresinin işaretlendiği ve müşteri bazında önceliklendirme yapmak amacıyla Cari Planlama Kayıtları ekranında ALICI1 ve ALICI2 için aşağıdaki kayıtların girildiği varsayıldığında, görüldüğü gibi ALICI1 için öncelik değeri olarak 1 ve ALICI2 için de 2 şeklinde tanımlama yapılır. Bu şekilde yapılan bir tanımlamayla beraber ALICI1 carisi daha öncelikli durumdadır. Önceden, herhangi bir müşteri siparişine rezerve edilmemiş 2500 adetten oluşan MAMUL1 bakiyesinin olduğu bir durumda MRP çalıştırıldığında, elde edilen sonuç ve serbest stok bakiyesinin müşteri siparişlerine dağıtımı aşağıdaki şekilde gerçekleşir:

![](../_assets/007ecfa9a40fdec0f185.png)

Görüldüğü gibi 2500 adetten oluşan stok bakiyesinin 1000 adetten oluşan kısmı, öncelikli cariye (ALICI1) açılan M00000000000001 numaralı müşteri siparişine atanır. Geri kalan 500 adetten oluşan MAMUL1 bakiyesi ise M00000000000002 numaralı müşteri siparişine atanır.
