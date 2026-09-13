---
title: "Grup Koşul Yenilikleri"
page_id: "50680152"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Grup Koşul Yenilikleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Grup Koşul Yenilikleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTBiODU1NjQ0LTJjOWItNDJmOS1hZTk3LTQwODFiNjc0ZjQwZSZsaW5rPWQwZmZhOGQ2LTU3ZTEtNDk0Ny04NGEwLTZiODJkZGE0YWExZSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=0b855644-2c9b-42f9-ae97-4081b674f40e&link=d0ffa8d6-57e1-4947-84a0-6b82dda4aa1e&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "grup-kosul-yenilikleri_82576646_50680152.html"
source_version: "2022-11-03T09:50:04.097+03:00"
source_bytes: 995840
fetched_at: "2026-09-13T04:26:15+00:00"
generator: "netsis-scraper 1.0.0"
---
# Grup Koşul Yenilikleri

Grup Koşul Yenilikleri ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

|  |  |
| --- | --- |
| Amaç ve Fayda | Koşul uygulamasında yapılan yenilikler ile; stok grupları bazında "miktar" aralığı verilerek tanımlanabilen mal fazlası iskontolarının, belgedeki koşulun geçerli olduğu tüm kalemlerin "tutarlarının" toplamına göre de getirilmesi sağlanmıştır. Ayrıca detay koşul kaydında iskonto aralığı verilmesi halinde, satır iskonto oranının tespitinde, belgede girilen koşulun geçerli olduğu tüm kalemler yerine seçilen stokların toplam miktar ya da tutarının dikkate alınması desteklenmiştir. |
| Yayın Tarihi | 21/12/2011 |
| Ürün Grubu | \[X\] Redcode Enterprise<br>\[X\] Redcode Standard<br>\[X\] Entegre.Net |
| Modül | \[X\] Fatura<br>\[X\] Cari |
| Yükleme Sonrası İşlemler | \[X\] DBUPDATE Programının Çalıştırılması |
| Modül | \[X\] İyileştirme |
| Versiyon Önkoşulu | 5.0.10 |

Yapılan düzenlemeler sonucunda aşağıdakine benzer koşul isteklerinin karşılanması sağlanmıştır:

- X ürün grubundan 10 adet alana Y ürün grubundan %2 indirim.
- X ürün grubundan 10 TL lik ürün alana aynı ürün grubundan 2 adet hediye.
- X ürün grubundan 10 TL lik ürün alana Y ürün grubundan 2 adet hediye.
- X ürün grubundan 10 TL lik ürün alana Y ürün grubundan %2 indirim.
- X ürün grubundan 10 kg lık(1. Ölçü birimi hariç diğer ölçü birimi) ürün alana aynı ürün grubundan 2 adet hediye.
- X ürün grubundan 10 kg lik (1. Ölçü birimi hariç diğer ölçü birimi) ürün alana Y ürün grubundan 2 adet hediye.
- X ürün grubundan 10 kg lık (1. Ölçü birimi hariç diğer ölçü birimi) ürün alana aynı ürün grubundan %2 indirim.
- X ürün grubundan 10 kg lık (1. Ölçü birimi hariç diğer ölçü birimi) ürün alana Y ürün grubundan %2 indirim.

#### Koşul kayıtlarında yapılan değişiklikler

Farklı ürün gruplarına satır iskontosunu tanımlayabilmek için Detay Koşul Bilgileri ekranındaki "Detay Koşul Bilgileri-2" sekmesine "Grup İskonto İçin Farklı Ürün Grubu Seçimi" bölümü eklenmiştir.

![](../_assets/01f1de7404b8f30799a4.png)
Öncelikle Grup Koşul seçeneği işaretlenmelidir. Daha sonra "İskonto Aralığı var mı" bölümü işaretlenerek, miktar ya da tutar aralıkları belirlenir. Hangi ürünler ya da ürün grubu için bu iskontolar uygulanacaksa "Grup İskonto İçin Farklı Ürün Grubu Seçimi" ekranından aşağıdaki gibi seçilmelidir.
![](../_assets/4809443fe85c9c458ba1.png)

Bu ekrandaki saha adı bölümünde raporlama kodlarının tamamı, kullanıcı tanımlı sahalar, stok kodu ve stok adı seçimi yapılabilir. Ve/veya kısıtları kullanılarak çoklu kısıtlar da uygulanabilir.
Bir ürün grubundan birinci ölçü birimi dışında belirli miktar ya da tutarda alış/satış yapıldığında başka bir ürün grubu için mal fazlası iskontosu tanımlanması ve mal fazlası stoklarının miktar kontrolünün yapılması sağlanmıştır. Mal fazlası stoklarının miktarlarının doğru girilip girilmediğinin kontrol edilebilmesi için "FATURA", "KOSULMALFAZKONTROL" özel parametresi kullanılabilir.

![](../_assets/e56cd6fc99424b7e1a5f.png)![](../_assets/238735ef6a061aa36b3c.png)

#### ÖRNEKLER

**Örnek 1:** X ürün grubundan(Grup Kodu: PR) alındığında, Kod1'i CM olan Çamaşır Suyu stoklarından da alınmışsa, bunlara miktar aralıklarına göre satır iskontosu 2 uygulanması istenmektedir(stokların ölçü birimi 1'i AD olarak tanımlanmıştır).
PR ürün grubundan 10- 20 adet alınmışsa, Kod1'i CM olan stoklara %1, PR ürün grubundan 20- 30 adet alınmışsa, Kod1'i CM olan stoklara %2 PR ürün grubundan 30+ adet alınmışsa, Kod1'i CM olan stoklara %3 iskonto uygulanacaktır.

#### Uygulama1

Öncelikle koşul tanımı aşağıdaki şekilde yapılmalıdır. Bu örnekte satır iskontosu 2 olarak belirtildiği için Hangi S.İsk alanına 2 yazılmıştır. Bu koşulun faturadaki kullanımı aşağıdaki şekilde olacaktır. İlgili koşul, fatura koşul sekmesinde seçilmelidir. Ardından faturaya ait kalem bilgileri girilmelidir. İskontoların hesaplanabilmesi için fatura kalemler sayfasında üst ekranda sağ klik yapılmalı ve "Grup Koşulları Çalıştır" seçeneği çalıştırılmalıdır.
Bu adımdan sonra açılan ekranda "İskontoları Yansıt" seçeneği kullanılarak, verilen aralığa uygun olan iskontonun hesaplanması sağlanmalıdır.
![](../_assets/e4a628ac70fbedf64930.png)![](../_assets/b3af9ee5a90c66bec051.png)
Örneğimize göre, faturada PR ürün grubundan toplam 12 adet vardır. Bu da ilk miktar aralığına denk gelmektedir, bu durumda fatura kalmelerinde buluna Kod1'i CM olan, CM2 kodlu stok için %1 iskonto hesaplanıp İskonto 2 alanına yazılmıştır.
**Örnek2:** Grup Kodu PR olan X ürün grubundaki stokların 1. Ölçü birimleri AD(Adet), 2. Ölçü birimleri de KG(kilogram) olarak tanımlanmıştır. PR grup koduna sahip olan ürünlerden 10 KG ve üzerinde kayıt girildiğinde, Kod1'i CM olan Çamaşır Suyu stoklarında 2 adet mal fazlası verilecektir. 20 KG ve üzerine ise 5 adet mal fazlası verilecektir. Ölçü birimi tanımları aşağıdaki gibidir.
Stok1.ölçü2.ölçü
PR1ADKG3/1
PR2ADKG1/1

#### Uygulama2

Buna göre koşula ait tanımlamalar aşağıdaki gibi olacaktır:

- Detay Koşul kayıtlarındaki ilk ekranda Ölçü Birimi sahasında Ölçü Birimi 2 seçilmelidir.
- Detay Bilgiler2 sekmesinde Grup Koşul seçeneği işaretlenmelidir.
- Mal fazlası sekmesinde de "Mal Fazlası Grup Mu" seçeneği işaretlenmeli ve miktar aralıklarına göre verilecek mal fazlası miktarları girilmeli, Geçerli Mal Fazlası stokları tanımlanmalıdır.

Bu koşulun faturadaki kullanımı aşağıdaki gibi olacaktır:
İlgili koşul, fatura koşul sekmesinde seçilmelidir. Ardından faturaya ait kalem bilgileri girilmelidir. Örneğe göre PR1'den 3 AD(yani 9 KG), PR2'den 1 AD(yani 1KG), toplamda 4 AD ancak 10 KG satış yapılmıştır. Bu durumda en fazla 2 AD mal fazlası girilebilecektir.
![](../_assets/4919aed48c22074254a7.png)
İskontoların hesaplanabilmesi için fatura kalemler sayfasında üst ekranda sağ klik yapılmalı ve "Grup Koşulları Çalıştır" seçeneği işaretlenmelidir. Bu durumda ekrana, uygulanabilecek mal fazlası miktarı ve koşula uyan stok kodları listelenecektir. İstenilen kalem seçilip mal fazlası girişi yapılmalı ve "İskontoları Yansıt" butonuna basılmalıdır. Bu durumda görünüm aşağıdaki gibi olacaktır.

![](../_assets/24d50ae54bc6e40bd763.png)
