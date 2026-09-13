---
title: "Otomatik Barkod Oluşturma"
page_id: "160040335"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Otomatik Barkod Oluşturma"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Otomatik Barkod Oluşturma"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWVmMGZiNWFhLWJiMDMtNGNkNC04NjI1LTlmMDZlOTEyZjQ5NiZsaW5rPTMyOGY3MTIwLTY5Y2EtNDhhMC1hNWFhLTc3Njc1NDAyODFmYSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=ef0fb5aa-bb03-4cd4-8625-9f06e912f496&link=328f7120-69ca-48a0-a5aa-7767540281fa&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "otomatik-barkod-olusturma_160040335_160040335.html"
source_version: "2024-12-23T09:33:35.764+03:00"
source_bytes: 1171208
fetched_at: "2026-09-13T04:22:21+00:00"
generator: "netsis-scraper 1.0.0"
---
# Otomatik Barkod Oluşturma

9.0.50 sürümü ile birlikte "Otomatik Barkod Oluşturma" özelliği desteklenmiştir.

Yeni açılan stok kartlarında otomatik barkod üretilebilmesi için Lojistik-Satış/Stok/İşlemler/Stokbar İşlemleri altında bulunan Barkod Parametreleri ekranına "Otomatik Barkod-1 Üretilsin" parametresi eklenmiştir. Bu parametre işaretlendiğinde, altta bulunan "Sabit Değer" ve "Değişken Karakter Sayısı" alanları aktif hale gelir.

![](../_assets/3c0b008e215e2d5e976f.png)

## Sabit Değer

Oluşturulacak barkodun ön değerinin belirlendiği alandır. Örnekte girilen 3 karakterli "123" değeri, barkod bilgisinin ilk 3 satırını oluşturur.

## Değişken Karakter Sayısı

Oluşturulacak barkodun sabit değeri dışında kaç karakterden oluşacağının belirlendiği alandır. Örnekte girilen "7" değeri ön değerden sonra 7 karakterli numerik olarak sırayla artacak bir barkod bilgisinin oluşturulmasını sağlar.

Parametre tanımlamaları yapıldıktan sonra, Stok Kartı Kayıtları bölümünden yeni eklenen stok kartının Stok Kartı 2 sekmesinde bulunan Barkod-1 alanına "1230000001" barkod bilgisinin otomatik olarak program tarafından getirildiği görülür. Bu doğrultuda, sıradaki eklenecek olan stok kartının barkod bilgisi de "1230000002" olarak getirilir.

![](../_assets/670a7f9e15ba727737c1.png)

Ayrıca, Barkod 1-2-3 alanlarının sağ tarafına eklenen "+" butonu ile stok kartlarında kullanılan barkod bilgilerine göre sıradaki barkod bilgisinin otomatik getirilmesi sağlanabilir.

![](../_assets/6c79a6ea2b18d462f4a7.png)

Aşağıdaki örnekte, stok kartları içerisinde son kullanılan Barkod-2 bilgisi "DNM000011" olduğundan,

![](../_assets/4b6fdb04ec66960f604d.png)

Barkod-2 alanın sağ tarafında bulunan "+" butonuna tıklandığında alfa sayısal sıralama ile sıradaki barkod bilgisi olan "DNM000012" barkod bilgisinin ilgili alana otomatik olarak program tarafından getirildiği görülür.

![](../_assets/4c4893d03fed603dfd6e.png)
