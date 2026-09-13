---
title: "Puan Uygulaması"
page_id: "85197150"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Puan Uygulaması"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Puan Uygulaması"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTQwNWYxOGRmLWMzODAtNDg1Ny1iODgxLWZkOWMyN2U2MmFjNCZsaW5rPWViYmZiYThlLTI2MmEtNDRjNC05YzA1LTAyNDYxZWYyODQwOSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=405f18df-c380-4857-b881-fd9c27e62ac4&link=ebbfba8e-262a-44c4-9c05-02461ef28409&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "puan-uygulamasi_90670147_85197150.html"
source_version: "2022-11-02T14:32:38.887+03:00"
source_bytes: 4230515
fetched_at: "2026-09-13T04:24:06+00:00"
generator: "netsis-scraper 1.0.0"
---
# Puan Uygulaması

Puan Uygulaması ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Puan uygulaması, birçok sektörde yaygın olarak uygulanan puanlama kampanyalarının program tarafından otomatik takibine yönelik sistemdir. Satıcı firmaların, müşterilerine, alımları üzerinden puan hesaplatması ve puanlarına istinaden hediye vermesi işlemlerinin programda takibi yapılabilmektedir.

Bu sistemde, her bir ürün için ayrı puanlar belirlenebilmekte, müşterilerin toplam hak ettiği, kullandığı ve bakiye puanları takip edilebilmektedir. Toplanan puanlar karşılığı verilecek hediye ürünlerde, bakiye puan dikkate alınmaktadır.

Bu sitemin uygulanabilmesi için Stok Kartı Kayıtlarında bulunan **Birim Puan** sahasına stoka ait birim puan girilmelidir. Böylece, fatura modülünden bu ürün için yapılan satış ve alışlarda **miktar** **puan** değeri ile puan toplamı hesaplanacaktır.

![](../_assets/7defb5c82279a1c44aea.png)

Örneğin; Bir ürünün birim puanı 20 olsun. Satış faturasından bu üründen 100 adet alındığında, faturanın kesildiği müşterinin 2000 puanı olacaktır.
İlgili ürünün kaç puan karşılığında hediye verileceği bilgisi de **Puan** **Değeri** sahasında belirlenmelidir. Bu üründen bir adet hediye olarak verilebilmesi için cari hesabın, en az bu değer kadar puanının olması gerekmektedir. Örneğin, 10000 puanı olan müşteri, puan değeri 12000 olan bir üründen alamayacaktır.

Uygulamada, birim puanı dolu olan her stok kartının satışında otomatik olarak puan hesaplanacaktır. Puan değeri dolu olan stok kartları da hediye ürün olarak verilebilecektir.

Fatura modülünde, belgede yer alan ürünlerden, birim puan girilmiş olan ürün veya ürünler için faturada puan hesaplaması otomatik yapılacaktır. Puan kazandıran ürünlerin bulunduğu fatura kayıtlarında toplamlar sayfasında, o faturaya ait puan bilgisi, **Hediye** **Puan** alanında izlenmektedir.

![](../_assets/1943ded7c17f9e78bbf6.png)

Ayrıca fatura üzerinde üst bilgiler sekmesinde sağ click menüsünde "**Cari** **Kartı** **İzleme**" ekranında ise, işlem yapılan carinin o ana kadar biriken puanlarını **Puan** **Toplamı** alanından izlenebilmektedir.

![](../_assets/805775f1e92b08fef0b5.png)

Cari hareket kayıtları ekranında, cari hesabın satır bazında puanlarını **Puan** kolonundan, toplam puanını da dip toplamdaki **Puan** **Toplamı** alanından izlenebilmektedir. Puan kazandıran ürünlerden satın alındıkça puanlar toplanmakta, bu üründen iade edildiğinde de toplam puandan düşülmektedir.

![](../_assets/678d680fd6abb107132e.png)

Fatura modülünde yapılan işlemlerde, hangi tip faturalarda puan karşılığı hediye ürün verileceğinin anlaşılabilmesi için, Özel Kod-2 parametresi kullanılmaktadır. Bunun için fatura parametrelerinde, Özel Kod ve Açıklama sekmesinde, "**Özel** **Kod-2**" ve "**Özel** **Kod-2** **Değeri** **Tablodan** **mı** **Kontrol** **Edilecek**" parametrelerinin işaretlenmesi gereklidir.

![](../_assets/f1492c0d982749a7dcfd.png)

Özel Kod-2 tanımında, Kod kısmı istenilen formatta girilebilirken, Açıklama kısmında sadece "**PUAN**" kelimesi yazmalıdır. Puan kelimesinin başında veya sonunda başka bir açıklama yer almamalıdır (Puan Uygulaması, Puan Sistemi, vb). Bu durumda, puan karşılığı hediye amaçlı kesilen fatura kayıtları sırasında özel kod-2 değeri girilmelidir.

![](../_assets/d2799f3851e926630d9d.png)

**Örnek:**

Carinin toplam 23800 hediye puanı olduğunu ve puanına karşılık ilgili stoktan hediye almak istediğini ve stokun 10.000 puan değeri olduğunu düşünelim.

![](../_assets/4803963655ad88491b14.png)
Hediye için kesilecek faturada bazı koşullara dikkate edilmesi gereklidir. Yukarıda da belirtildiği gibi, bu tür faturaları keserken Özel Kod-2 sahasına, puan uygulaması için tanımlanan (Açıklaması PUAN olan) özel kod-2 değerinin girilmesi gereklidir.
![](../_assets/1ba5c6503ae20e45e1ae.png)

Kalemler sahasında puan değeri 10.000 olan stoktan 3 adet hediye verilmek istendiğinde, aşağıdaki gibi bir uyarı ekranı ile karşılaşılacaktır. Bu üründen 3 adet verilebilmesi için müşterinin en az 30.000 puanının olması gereklidir. Bu durumda, bu üründen bir veya iki adet hediye verilebilir.

![](../_assets/370bedf9a6c4cb23df8a.png)

Hediye ürün verilen faturalarda, aşağıda görüldüğü gibi, fatura toplamı kadar (% 100) satır iskontosu yapılacak ve genel toplam sıfırlanacaktır.
![](../_assets/3040888fa9d9ef962b63.png)![](../_assets/eac896c333dd0e1e9267.png)

Bu tür faturalarda, hediye ürünler dışındaki ürünlerden (puan değeri olmayan) satılamaz. Satılmak istendiğinde, program tarafından "**Bu** **ürün** **hediye** **faturasında** **kullanılamaz**" uyarısı verilecektir.

![](../_assets/74f38eb8573cf10d0097.png)

Hediye faturaları cari hareket kayıtlarına tutarsız olarak aktarılmakta ve kullanılan puan cari hesabın toplam puanından düşülmektedir.

![](../_assets/5f665727b509134716bb.png)
