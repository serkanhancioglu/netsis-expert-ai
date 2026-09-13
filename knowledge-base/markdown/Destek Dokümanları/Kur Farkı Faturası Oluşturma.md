---
title: "Kur Farkı Faturası Oluşturma"
page_id: "74718662"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Kur Farkı Faturası Oluşturma"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Kur Farkı Faturası Oluşturma"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTQxZDVhYzU5LWM5NjQtNGQyNS1hMThlLThhZjgzZTJjMWI1OSZsaW5rPTE4MjZlMGM4LWExYjEtNDIzZi1iNDAwLWY5YjBhZmYxNTNlZiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=41d5ac59-c964-4d25-a18e-8af83e2c1b59&link=1826e0c8-a1b1-423f-b400-f9b0aff153ef&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "kur-farki-faturasi-olusturma_80087702_74718662.html"
source_version: "2022-11-02T14:47:15.923+03:00"
source_bytes: 923838
fetched_at: "2026-09-13T04:24:13+00:00"
generator: "netsis-scraper 1.0.0"
---
# Kur Farkı Faturası Oluşturma

Kur Farkı Faturası Oluşturma ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

9.0.39 setiyle birlikte Cari Modülü/İşlemler/Döviz İşlemleri menüsü altına **Kur** **Farkı** **Faturası** ekranı ve Cari Modülü/Raporlar/Ek Listeler/Dövizli Listeler/**Detaylı** **Kur** **Farkı** **Listesi** **Raporu** eklenmiştir.
Özel hesap kapatma ile çalışan carilere ait, mevcut faturalar ile bu faturalar ile eşleşen tahsilat ve ödeme kayıtları için kur farkından doğan bir karın olması durumunda bu tutarın kur farkı faturası olarak oluşturulması sağlanmıştır.
Ayrıca Detaylı Kur Farkı Listesi Raporu ile oluşturulan kur farkı fatura tutarlarının belge bazında detaylı rapor alınması da sağlanmıştır.

Kur Farkı Faturalarının oluşması için aşağıdaki işlemlerin yapılması gerekir:

- Carilerin özel hesap kapatma ile çalışması gerekmektedir.
- Fatura, tahsilat ve ödeme kayıtlarının girilerek özel hesap kapatma işleminin yapılması gerekmektedir.
- Satış Fatura Parametreleri ekranında, "**Hizmet** **Uygulaması**" parametresinin işaretlenmesi ve sonrasında Cari Parametreleri ekranında ise, "**Kur** **Farkı** **Faturası** **Hesaplansın**" parametresinin işaretlenmesi gerekmektedir.

![](../_assets/3228aedf915c89d60160.png)
![](../_assets/8cc3020f968a3cf89496.png)
Gerekli tanımlama ve parametrelerin işaretlenmesi sonrasında kdvli satış faturaları için kur artışı veya alış faturaları için kur düşüşü sebebiyle kur kaynaklı bir karın olması durumunda, bu tutarın kdv dahil bir satış faturası ile karşı cariye faturalaştırılması sağlanmaktadır.

#### Kur Farkı Faturası Oluştur

![](../_assets/803c5a649688170674c3.png)
Kur Farkı Faturası Oluştur ekranı; Ön Sorgu, Cari Seçimi, Kur Farkı Kayıtları ve Fatura Bilgileri sekmelerinden oluşur.
Başlangıç/Bitiş Tarihi alanından, kur farkı faturası oluşturulacak belgeler için, tarih aralığı kısıtı verilir.
Cari Kodu Aralığı alanından, kur farklı faturası oluşturulacak cariler için, cari kodu aralığı kısıtı verilir.
Tip, Grup Kodu, Kod-1,2,3,4,5 alanları, kur farkı faturası oluşturulacak carilerin seçiminde kullanılacak kısıt alanlarıdır.
Fatura Detayında Getirilsin seçeneği; verilen tarih aralığında ve kısıtlara göre kur farkı faturası oluşturulacak birden fazla belge varsa, bu faturalar için kümüle olarak tek bir kur farklı faturası oluşturulacaksa bu parametre işaretlenmelidir. Fatura Detayında Getirilsin seçeneği işaretlenmediği durumda her belge için ayrı ayrı kur farklı faturası oluşturulacaktır.
Fatura Detayında Getirilsin parametresi işaretlendiğinde, Fatura no aralığı aktif hale gelir. Fatura No Aralığı alanında da kur farkı faturası oluşturulacak belge veye belge aralığının seçimi yapılabilir.
**İlerle** butonu ile Cari Seçimi sekmesine gelinir. Ön sorgulama sekmesinde seçilen kriterlere göre kur farkı faturası oluşturulacak carilerin listesi görüntülenir.
**Hesapla** butonuna basılarak Kur Farkı Kayıtları sekmesine gelinir.
![](../_assets/3b8bf3f15fe87a30dda2.png)
Örneğe göre cariye kesilen 01.03.2022 tarihinde 13,8535 kurundan 1180 dolarlık bir satış faturası ve 11.03.2022 tarihinde 14,74350 kurundan yapılan 300 dolarlık tahsilat kaydı mevcuttur.
![](../_assets/e6d5ce3ee94676042722.png)
Kur farkı faturası oluştur ekranında tahsilat kaydı ile satış faturası arasındaki kurdan kaynaklı (satış faturası kesilirken 13,8535 olan kur tahsilat sırasında 14,74350 ye yükselmiştir) bir kar söz konusudur. Bu oluşan kar kur farkı tutar alanında pozitif bir değer olarak getirilmektedir.
Kur farkı tutar hesabı:
11.03.2022  300\*14,74350= 4423,05
01.03.2022 300\*13,8535= 4156,05
4423,05-4156,05= **267** **(%18** **kdv** **dahil** **267 TL'****lik** **kur** **farkı** **tutarı** **bulunur)**
![](../_assets/c967def78acaad72f2e9.png)
Kur farkı faturası tutar kısmında bir link desteği bulunmaktadır. İlgili tutara tıklandığında Kur Farkı Detay Bilgileri ekranı açılır. Bu ekranda kur farkı hesaplamasına kaynak olan belge ve bu belgeye tıklandığında eşleşen hareketler kısmında özel hesap kapatmada karşı bacağında eşleştirilen hareketler listelemektedir.
![](../_assets/6f7057ff75f3e17ca629.png)
Kur farkı tutar hesabı sonrasında **İleri** butonuna basılarak Fatura Bilgileri sekmesine geçilir.
Fatura Bilgileri ekranında oluşturulacak kur farkı faturası için fatura serisi, tarih, kur farkı faturası için kullanılacak hizmet stok kodu ve Muhasebe kodu bilgileri girilir. Sonrasında **Faturayı Kaydet** butonuna basılarak kur farkı faturası oluşur.
![](../_assets/102b58350a7cdd6384b1.png)
Oluşan fatura, kdv dahil bir kur farkı faturası olarak oluşmaktadır ve cari hareket kayıtlarına atılmaktadır.
![](../_assets/14c1af21dfde5bee1811.png)
Kur farkı faturası oluştuktan sonra, Kur Farkı Faturası Oluştur ekranında Kur Farkı Kayıtları sekmesinde, kur farkı fatura no kolonunda oluşan kur farkı faturası numarası yazmakta olup, link desteğiyle ilgili numaraya tıklandığında kur farkı faturasına gidilmektedir.
![](../_assets/c05b834852f337d0f6f8.png)
Oluşan kur farkı faturası üzerinde herhangi bir düzenleme yapılamamaktadır. "**Kur farkı için** **oluşturulmuş fatura! Bu belgede düzeltme yapamazsınız**" uyarı ekranı gelmektedir. Kur farkı tutarlarında bir sorun olması durumunda ilgili kur farkı faturası silinerek yeniden oluşturulmalıdır.
![](../_assets/cabf3e15d2820aad40bd.png)
Kur Farkı Faturası Oluştur ekranında, Kur Farkı Kayıtları sekmesinde, kaynak fatura belgesi içerisinde birden çok kdv oranına sahip birden çok satır varsa, bu sekmede farkı kdv oranları bazında farklı kur farkı tutar satırları oluşacaktır.
![](../_assets/8b4e085fc8be6cc83649.png)
Cari Modülü/Raporlar/Ek Listeler/Dövizli Listeler/Detaylı Kur Farkı Listesi Raporunda da belge bazında kur farkı tutarları listelenir.
![](../_assets/45deac665e790f82eec8.png)
