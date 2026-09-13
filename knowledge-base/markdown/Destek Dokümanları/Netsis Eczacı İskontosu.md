---
title: "Netsis Eczacı İskontosu"
page_id: "50680331"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis Eczacı İskontosu"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis Eczacı İskontosu"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWE2OWE0MjBkLTY0Y2EtNGMwMS1hNzI3LTNiYjE4NjRmNmUyYyZsaW5rPWRmYTlmMjE5LTE2ZjQtNDc0Mi1iYjMwLTJkNDEzY2QwNzlhMSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=a69a420d-64ca-4c01-a727-3bb1864f6e2c&link=dfa9f219-16f4-4742-bb30-2d413cd079a1&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-eczaci-iskontosu_80085346_50680331.html"
source_version: "2022-11-03T09:53:08.730+03:00"
source_bytes: 849833
fetched_at: "2026-09-13T04:26:21+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis Eczacı İskontosu

Netsis Eczacı İskontosu ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Eczacı iskontosu uygulaması ile, ecza depolarının eczacılara kestikleri satış faturalarında, ilaçların perakende ve depo satış fiyatları baz alınarak, eczacı iskontosunun program tarafından hesaplanması sağlanmıştır.

İlaç satışlarında iki türlü fiyat bulunmaktadır. Bunlardan ilki, perakende satış fiyatıdır. Diğer bir fiyat ise, ecza depoları tarafından eczanelere uygulanan ve iskontolu fiyat olan depo satış fiyatıdır. Eczacılara kesilen faturalarda, ilaca ait perakende fiyatı kullanılmakta, ancak hesaplamalar ve muhasebe kayıtları, depo satış fiyatı ile oluşmaktadır. Sonuç olarak ilaç depo fiyatı ile satılmaktadır. Netsis paketlerinde yapılan düzenlemeler ile, eczacılara kesilen faturalarda uygulanan eczacı iskontosunun, yani eczacı karının, program tarafından hesaplanabilmesi ve muhasebe kayıtları ile stok hareketlerinin depo satış fiyatı üzerinden oluşması sağlanmıştır.

Bu uygulamanın desteklenebilmesi için yapılması gereken işlem adımları aşağıdaki şekildedir.

**1-Stok Fiyatlarının Belirlenmesi**

İlaca ait fiyat bilgileri stok kartına giriliyor ya da özel fiyat sistemi ile bu fiyatlardan fiyat listesi oluşturuluyor ise, perakende satış fiyatı 1. fiyat sahasına girilmelidir. Ayrıca faturalar, eczacılara KDV dahil olarak kesiliyor ise, 1. fiyat sahasına KDV dahil perakende satış fiyatı girilmelidir. Depo satış fiyatı ise, 2, 3 ya da 4. fiyat sahalarından birisine mutlaka KDV hariç olarak girilmelidir. Aksi takdirde, eczacı iskontosu yanlış hesaplanacaktır.

Satışı yapılan bir ilacın perakende ve depocu satış fiyatlarının aşağıdaki gibi olduğunu varsayalım.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Stok Kodu | Perakende |  | Depocu |  |  | KDV |  |  |
|  | KDV Dahil | KDV Hariç |  | KDV Dahil | KDV Hariç |  |  |  |
| G001 | 10,08 | 10 |  | 8,72 | 8 |  | 8 |  |

Eğer satış faturaları KDV dahil olarak kesiliyorsa, 1. satış fiyatı sahasına KDV dahil perakende satış fiyatı (10,8 TL) girilmelidir. Ancak, KDV hariç fatura uygulaması var ise, bu sahaya, KDV hariç perakende satış fiyatı (10 TL) girilmelidir. Depo satış fiyatı ise, diğer satış fiyatı sahalarından herhangi birine girilebilir. Ancak dikkat edilmesi gereken nokta, KDV dahil ve KDV hariç uygulamalarının her ikisi için de KDV hariç depo satış fiyatının (8 TL) girilmesi gerektiğidir. Aksi takdirde, iskonto ve fatura toplamı hesaplamaları doğru çıkmayacaktır.

![](../_assets/a6a244bb9fc87abfdfaf.png)

Bu durumda, eczacılara kesilen satış faturasında KDV dahil birim fiyat 10,8 TL olacak, ancak ürünün bedeli 8 TL olacaktır. Böylece, KDV hariç perakende ve depo fiyatları arasındaki 2 TL’lik fark, eczacı iskontosu olarak hesaplanacaktır. Eczacı iskontosunun program tarafından hesaplanabilmesi için, stok kartı ya da fiyat listelerindeki fiyatların, yukarıda anlatılan şekilde girilmesi gerekmektedir. Ancak, perakende satış fiyatının stok kartında ya da fiyat listesinde belirtilmediği durumlarda, yani faturada elle girildiğinde de eczacı iskontosu hesaplanabilir. Yine de depo satış fiyatının stok kartında ya da fiyat listesinde bulunması ve özel parametrelerde fiyat sahasının belirlenmesi gerekmektedir. Ayrıca, dövizli satış uygulamasının kullanılması halinde, stok kartında bulunan satış fiyatı sahalarına döviz fiyatları girilmeli ve Satış Fatura Parametrelerinde bulunan “Satış fiyatı döviz fiyatı olarak kullanılsın mı” parametresi işaretlenmelidir.

**2-Cari Hesap Kayıtlarında Yapılması Gerekenler:**

Eczacı iskontosunun hesaplanacağı cari hesapların belirlenmesi gerekmektedir. Eczacı olan cari hesaplar için, Cari Hesap Kayıtları/Kullanıcı Tanımlı Sahalar bölümünde bulunan alfa sayısal sahalardan herhangi birisine ECZACI yazılmalıdır. Bunun için öncelikle kullanıcı tanımlı sahalardan birisi için, Cari Parametre Kayıtlar/Kullanıcı Tanımlı Sahalar bölümünden başlık bilgisi girilmelidir.

![](../_assets/e5fd1b26293a42aff1b6.png)

Böylece, cari hesap kayıtlarında parametrelerde başlık girişi yapılan alfa sayısal saha aktif olacaktır.

![](../_assets/1b7d7a0e90c05346703b.png)

Alfa sayısal sahaya verilen başlığın herhangi bir önemi olmayıp, sadece cari kartta bu sahaya girilen ECZACI değeri kontrol edilecektir.

**3-Özel Parametre Tanımlarında Yapılması Gerekenler:**

Eczacı iskontosunun hesaplanmasında kullanılacak depo satış fiyatının, stok kartı ya da fiyat listesindeki kaçıncı fiyat olduğunun ve hangi cari hesaplara eczacı iskontosu yapılacağının belirlenmesi için Yardımcı Programlar/Özel Parametre Tanımları bölümünde iki ayrı tanımlama yapılmalıdır.

![](../_assets/988b53ec77698cf50729.png)

Depo satış fiyatının girildiği sahanın belirlenmesi için tanımlanması gereken parametre, Grup Kodu: FATURA, Anahtar: ECZACIFATURASI_FIYAT, Değer: Fiyat sahası (stok kartında ya da fiyat listesinde depo fiyatının kaçıncı fiyat sahasına yazıldığı) şeklindedir.

Örneğimize göre depo satış fiyatı (8 TL), stok kartındaki 2. fiyat sahasına yazıldığından, bu parametre tanımlanırken Değer sahasına 2 girilmelidir. Bu durumda, eczacıya kesilen faturada girilen perakende satış fiyatı, bu parametrede belirlenen fiyat sahasındaki fiyat bilgisinden büyük ise, aradaki fark eczacı karı olacak ve faturada satır iskontosu olarak gösterilecektir.

Eczacı iskontosunun sadece eczanelere kesilen faturalarda uygulanabilmesi için, eczacı cari hesapların kartlarında Kullanıcı Tanımlı Sahalardan birine ECZACI değeri girilmesi gerektiği daha önce belirtilmişti. Özel Parametre Tanımlarında ise, bu bilginin kaçıncı alfa sayısal sahaya girildiği belirlenmektedir. Bunun için tanımlanması gereken parametre ise, Grup Kodu: FATURA, Anahtar: ECZACIFATURASI_SAHA, Değer: KULL1S....KULL8S (örneğin KULL1S, 1. alfa sayısal saha) şeklindedir. Örneğimizde, ECZACI bilgisi 2. alfa sayısal sahaya girildiğinden, özel parametredeki Değer sahasına KULL2S yazılmalıdır. Böylece, satış faturası kaydı sırasında, faturada girilen cari hesaba ait karttaki 2. alfa sayısal saha kontrol edilecek ve eğer burada ECZACI yazıyor ise eczacı iskontosu hesaplanacaktır.

**4-Satış Faturasında Eczacı İskontosu**

Yukarıda anlatılan tanımlamalar yapıldıktan sonra, KDV dahil fatura kesiliyor ise, eczacı iskontosunun doğru olarak hesaplanabilmesi için Satış Fatura Parametrelerinde bulunan “KDV dahil faturada iskontodan önce KDV düşülsün mü?” parametresinin işaretlenmiş olması gerekmektedir. Bu parametre işaretlendiğinde, KDV dahil fatura kaydında, öncelikle KDV hariç perakende satış fiyatı hesaplanacak, bu fiyat ile KDV hariç depo satış fiyatı arasındaki fark eczacı iskontosu olarak gösterilecektir. Satış faturalarının KDV hariç fiyat üzerinden kesilmesi halinde ise, fatura kaydında girilen fiyat zaten KDV hariç perakende satış fiyatı olacağından, yukarıda belirtilen fatura parametresinin işaretlenmesine gerek yoktur.

![](../_assets/3e5106fcd8c00378b777.png)

İlaca ait perakende satış fiyatı stok kartına girildiğinde ya da fiyat listesinde tanımlandığında, fatura kaydının fiyat sahasına program tarafından getirilecektir. Örnekte, stokun kartındaki 1. satış fiyatı 10.8 TL girildiğinden, bu fiyat faturaya getirilecektir. Ayrıca, Özel Parametre Tanımlarında, depo satış fiyatlarının 2. fiyat sahasında olduğu belirtilmiş ve stok kartındaki 2. fiyat sahasına KDV hariç depo satış fiyatı olarak 8 TL girilmiştir. stoka ait KDV hariç perakende satış fiyatı (PSF), KDV hariç depo satış fiyatından (DSF) büyük olduğunda, eczacı karı olduğu anlaşılacak ve program tarafından eczacı iskontosu hesaplanacaktır. İskonto hesaplamasında kullanılan formül aşağıdaki gibidir.

% Eczacı İskontosu= \[(KDV Hariç PSF-KDV Hariç DSF) /KDV Hariç PSF\] \*100

PSF= Perakende Satış Fiyatı, DSF= Depo Satış Fiyatı KDV dahil fatura kesildiğinde, KDV oranı %8 iken, öncelikle stoka ait KDV hariç perakende satış fiyatı bulunacaktır (10,8 TL/1,08 = 10 TL). Buna göre, eczacı iskontosu oranı %20 olarak hesaplanacaktır. % Eczacı iskontosu= \[(10-8)/10\]\*100 = 20 Bulunan eczacı iskontosu oranı, kalem bilgilerinde, 1. satır iskontosu sahasına yazılmaktadır. Böylece KDV hariç perakende satış fiyatı üzerinden %20 satır iskontosu (2 TL) yapılarak KDV hariç depo satış bulunmaktadır.

![](../_assets/3eb5d29be4d22977ae67.png)

Fatura toplamlar sekmesinde, Brüt Toplam sahasına KDV hariç perakende satış fiyatı (10 TL) getirilmektedir. Bu tutardan eczacı iskontosu (2 TL) çıkarılarak bulunan KDV hariç depo satış fiyatı (8 TL), Ara Toplam sahasına yazılır ve bu tutar üzerinden KDV (8\*0,08=0,64) hesaplanır. Fatura kaydında, mal fazlası iskontosu ve 1. satır iskontosu dışındaki satır iskontolarının kullanılması halinde ise, öncelikle yine KDV hariç fiyat üzerinden 1. satır iskontosu (eczacı iskontosu) hesaplanacak, daha sonra ise kalan tutardan sırasıyla mal fazlası ve diğer satır iskontoları düşülecektir. Eczacı iskontosu uygulamasında, Entegrasyon Kayıtlarında oluşan kayıtların tutar sahaları, depo satış fiyatı üzerinden hesaplanacaktır. Dolayısıyla, eczacı iskontosu Entegrasyon Kayıtlarında gösterilmeyecektir.

![](../_assets/52be2afe564aa3a28225.png)

Stok Hareket Kayıtlarında ise, fiyat sahasında depo satış fiyatı olacaktır.

![](../_assets/a505a51b4917df1e8ce6.png)

stoka ait KDV dahil perakende satış fiyatı ve iskonto oranı, hareket kaydı üzerinde fare ile sağ klik yapıldığında gelen Stok Hareket Diğer Bilgiler bölümünden izlenebilir.
