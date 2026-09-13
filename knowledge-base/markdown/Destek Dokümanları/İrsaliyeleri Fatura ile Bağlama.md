---
title: "İrsaliyeleri Fatura ile Bağlama"
page_id: ""
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "İrsaliyeleri Fatura ile Bağlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / İrsaliyeleri Fatura ile Bağlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWJjY2NlNWY3LTkyNTgtNDZhOC05OWQxLTFhNjBiYWE3NTk3NyZsaW5rPWRiM2JiY2Y0LTc2ODQtNDhmYi04MDVjLTUwN2I1OGJlZWRlYyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=bccce5f7-9258-46a8-99d1-1a60baa75977&link=db3bbcf4-7684-48fb-805c-507b58beedec&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "irsaliyeleri-fatura-ile-baglama.html"
source_version: ""
source_bytes: 4872
fetched_at: "2026-09-13T04:21:43+00:00"
generator: "netsis-scraper 1.0.0"
---
# İrsaliyeleri Fatura ile Bağlama

Bazı uygulamalarda firmalar, müşterilerine kesmiş oldukları irsaliyeleri fatura haline getirmez ve bu irsaliyelere farklı bir stok kodu kullanarak tek fatura keser ya da önce fatura kesme işlemleri yapılıp sonradan irsaliye kesilmesi gibi durumlarda, ilgili satış irsaliyeleri için kesilen fatura ile irsaliyeleri bağlamak gerekir.

Normal uygulamada bu işlem, "Satış Fatura Parametreleri Genel 4" bölümündeki “İrsaliyeler Fatura ile Bağlansın” parametresi işaretlenerek, satış faturası kaydı sırasında yapılır. Bu bölümden, daha önce fatura ile bağlanmış irsaliyelerin bağlantıları kesileceği gibi, irsaliyeleri fatura ile bağlama işlemi de yapılabilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/9ed7a67c-5e23-4a6a-b310-1370b0ac0d74/ifb1.jpg)

Parametre aktif hale getirildikten sonra satış faturası kalemler sekmesine geçiş sırasında İrsaliyeleri Fatura Bağlama ekranı açılır. Bu ekranda faturada girilmiş olan cari koduna sahip faturalaşmamış irsaliyeler listelenir. Fatura hangi irsaliyeler için kesilecek ise bu ekran üzerinden “Ekle” butonu ile seçilip eklenir ya da sonradan kaldırılmak istenir ise ilgili fatura tekrar açılıp irsaliye seçilerek “Çıkar” butonuna basılabilir.

Bu işlem sonrasında faturada ilgili kalemler girilip fatura belgesi oluşturulur. Bu işlem ile girilen irsaliye faturalaşmış gibi TBLFATUIRS tablosundaki S_YEDEK1 alanı fatura numarası ile güncellenir. Stok hareketlerinde ise hem irsaliye hareketi hem fatura hareketi görünmektedir. İrsaliyenin fatura ile bağlama işleminde herhangi bir miktar ya da tutar kontrolü bulunmamaktadır.

Örnek irsaliye hareketi ve fatura bağlama sonrası hareketler aşağıdaki şekildedir. İrsaliye H10 stoğu üzerinden girilmiş olup S0000000002015 fatura numarası ile kalemlere geçiş aşamasında S00000000000425 irsaliye numarasına bağlanmıştır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/4aa542ea-d1b2-441f-aec1-2cb7c2957406/ifb2.jpg)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/672a8d0d-9976-4edf-ad92-cbf1dd0eabf8/ifb3.jpg)

Yardımcı programlar özel parametre tanımlama ekranında aşağıdaki özel parametre tanımlı ise bu durumda irsaliye üzerinden faturalaştırma yapılmış gibi irsaliye hareketi A tipli saklanmış irsaliyeye çevrilmekte ve stok hareketlerinde irsaliye görünmemektedir.

Grup Kodu: FATURA

Anahtar: IRSBAGLAVESIL

Değer: 0

Özel parametre tanımlı iken örnek irsaliye hareketi ve fatura bağlama sonrası hareketler aşağıdaki şekildedir. İrsaliye H10 stoğu üzerinden girilmiş olup S0000000002016 fatura numarası ile kalemlere geçiş aşamasında S00000000000426 irsaliye numarasına bağlanmıştır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/dedcf8a2-0bd0-434d-9bb0-f008e25276c8/ifb4.jpg)

H10 kodlu stokta yer alan irsaliye hareketi fatura ile bağlandığına TBLSTHAR tablosunda STHAR_GCMIK=0, STHAR_FTIRSIP=A, STHAR_HTUR=N, IRSALIYE_NO=FATURA NUMARASI, F_YEDEK3=MIKTAR olarak güncellenmekte ve stok hareket kayıtlarında görünmemektedir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/de612e2d-52b4-4912-9fbe-26d2fdf6abf3/ifb5.jpg)

```text
Bu işlemler fatura girişinde yapılabildiği gibi belgeyi bağlama işlemi sonradan yapılmak istenir ise de Lojistik - Satış Bölümü'nde, "İşlemler/Fatura" menüsünün altında yer alan “İrsaliyeleri Fatura ile Bağlama” ekranı üzerinden de ekleme ya da çıkarma işlemleri yapılabilir.
```
