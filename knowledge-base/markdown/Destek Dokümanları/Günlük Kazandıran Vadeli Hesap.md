---
title: "Günlük Kazandıran Vadeli Hesap"
page_id: "74711903"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Günlük Kazandıran Vadeli Hesap"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Günlük Kazandıran Vadeli Hesap"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWE4YWFhZTA3LTMxM2EtNDE4ZC04Yjc1LTQ0MjAyZTFiOWE3YyZsaW5rPWQyMGZiZWQ0LWUwMjMtNGM2MS1hMGUzLTk2YTY1MjMzMmM1MiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=a8aaae07-313a-418d-8b75-44202e1b9a7c&link=d20fbed4-e023-4c61-a0e3-96a652332c52&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "gunluk-kazandiran-vadeli-hesap_80087938_74711903.html"
source_version: "2022-11-02T14:48:58.807+03:00"
source_bytes: 688547
fetched_at: "2026-09-13T04:24:16+00:00"
generator: "netsis-scraper 1.0.0"
---
# Günlük Kazandıran Vadeli Hesap

Günlük Kazandıran Vadeli Hesap ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Vadeli mevduat hesapları anında nakit paraya dönüştürülemeyen, bankadan çekilmesi için belirli bir zamanın dolması gerektiği, bu süre dolunca faiz getirisiyle birlikte çekilebilen ya da başka bir vadeye yatırılan hesap türüdür. Ancak artık birçok banka vadeli hesaplarda günlük faiz kazanımını ve bu hesaplardan vade bozulmadan para çekilip yatırılabilmesini sağlamaktadır. Netsis üzerinde günlük kazandıran ve ara dönemde para çekilip yatırılabilecek vadeli hesaplar açılırken, Repo/Vadeli Hesap Açma ekranında "Günlük Kazandıran Hesap" parametresinin işaretli olması gerekir.

İşlem aşağıdaki örnek senaryo üzerinden detaylı aktarılacaktır:
**Örnek**: Günlük %1 faiz oranı ile alt sınır 10.000 TL, üst sınır 100.000 TL olacak şekilde bir hesap açılmalı ve faiz işleme kapatma işlemi izlenmelidir. Hesaba para yatırılmalı ve sonrasında faiz işleme kapatma çalıştırılıp oluşan tutarlar izlenmelidir.

#### Adımlar

##### Vadeli Hesap Açma

Repo/Vadeli Hesap Açma ekranından 1 ay vadeli, 2,06 faiz oranı ile 40.000 TL'lik "Günlük Kazandıran Hesap" parametresi ile hesap açılışı yapılır.
![](../_assets/d22c492b7be1835e3fcb.png)

Günlük kazandıran hesapta minimum tutar kısıtı varsa, bu tutar faiz işlenmeyecek bakiye alanına girilir. Örnekte 10.000 TL kadarlık kısma faiz hesaplanmayacaktır. Aynı şekilde belli bir tutarın üzerine faiz işlenmeyecekse, bu tutar üst limit tutarına girilir. Yine örnekte 100.000TL üstüne faiz işlenmeyecektir. Günlük kazandıran hesap parametresi işaretlendiğinde vadesinden önce çekilebilir parametresi program tarafından pasif işaretli hale getirilir. Bunun nedeni bu tip hesapların amacının günlük kazanılan faizin kullanılabilir olması ve hesaba para yatırma/çekme yapılabilmesidir.

##### Faiz İşleme Kapatma

Hesap açıldıktan sonra faiz işleme/kapatma çalıştırılır. Günlük faiz geliri program tarafından hesaplanır ve faiz geliri alanına yazılır.
![](../_assets/e2d774a35e8eebe3a576.png)
Hesap açılışı 40.000 TL olarak yapıldığı halde faiz 30.000 TL üzerinden hesaplanır. Bunun nedeni hesap açılırken belirlenen faiz işlenmeyecek hesap bakiyesi alt sınırıdır.
Hesaplanan faiz tutarı= ((40000-10000)\*2,06\*1(gün))/36000= 1,72 TL
![](../_assets/e235b000a1054b6519ff.png)
İşlem sonunda vadeli hesaba 1,72 TL faiz girişi olur.

##### Vadeli Hesap Para Yatırma

Ara dönemde vadeli hesaba para yatırma işlemi yapılır.
![](../_assets/b3ccc2e907ef8d79f39e.png)![](../_assets/dd9660f213a167c9974e.png)
Bu işlem anında program tarafından yapılan kontroller mevcuttur. Bunlardan ilki yatırılan tutarın hesabın açılışında belirlenen üst limiti aşıp aşmadığıdır. Eğer üst limitin aşmasına sebep olan bir tutar yatırılıyorsa program uyarı verir.
Ancak işleme devam edilebilir. Bir diğer kontrol para yatırılacak olan tarihtir. Para yatırılan tarihte ya da bu tarihten daha ileri bir tarihte faiz işleme kapatma yapıldı ise program işlemi keser ve faiz işleme kapatma yapılan tarihten sonraki bir tarihe işlem yapılmasını bekler. Aynı kontrol faiz tahakkuk işlemi içinde sağlanır. İşlem sonunda banka hesapları arası virman dekontu oluşur. Vadeli hesaba para girişi banka hareketlerinde izlenir.
Para yatırma işlemi sonrasında hesabın bakiyesi 110.001,72 TL olur.
![](../_assets/c9fb071502d4c519c62d.png)
Eğer para yatırma işlemi iptal edilmek istenirse banka hesapları arası virman ekranından, para yatırma işlemi sonunda gelen bilgi ekranında verilen referans numarasına ait işlem iptal edilir.
![](../_assets/0615e900966c9ce6e707.png)
İptal işleminde program para yatırma sonrasında faiz işlenip işlenmediğini kontrol eder. Eğer faiz işlendi ise para yatırma işleminin iptal edilmesine izin vermez. Öncelikle faiz işleme kapatma işlemini iptal edilmesini bekler.
![](../_assets/d60def783e6e01a2cfef.png)
Yeni günde yeniden faiz işleme/kapatma çalıştırılır. Burada dikkat edilecek nokta hesap bakiyesi 110.001,72 olmasına rağmen faiz üst sınır ve faiz işlenmeyecek bakiye dikkate alınarak faiz 100.000 TL üzerinden hesaplanır.
![](../_assets/1e96d199e8b9fe845b40.png)
Hesaplanan faiz tutarı= ((100000\*2,06\*1)/36000= 5,72 TL
![](../_assets/25e356f3d3cef5fe68fc.png)
Bu hesaptan para yatırma yapılabildiği gibi para çekme işlemide yapılabilir. Hesaplamalar yine aynı kontrollerle sağlanır ve faiz kalan para üzerinden günlük olarak hesaplanır.

##### Raporlama

Spot Kredi/Vadeli -Repo Hesapların Dökümü raporunda hesaba yatan, çekilen tutarlar ve faiz tutarı izlenir.
![](../_assets/8698b9cfd0ed6e735219.png)
