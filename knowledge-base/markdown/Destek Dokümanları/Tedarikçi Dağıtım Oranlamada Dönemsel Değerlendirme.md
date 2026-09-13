---
title: "Tedarikçi Dağıtım Oranlamada Dönemsel Değerlendirme"
page_id: "90673814"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Tedarikçi Dağıtım Oranlamada Dönemsel Değerlendirme"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Tedarikçi Dağıtım Oranlamada Dönemsel Değerlendirme"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTQ1ZjAxZDk3LWJhODgtNDZmMS1iZmYzLWFhYTU0MjE0NTlmNSZsaW5rPTcwZDlhZGM0LTU4OGMtNDllYS1iZmQ1LWEwNGI2ODJiMTMxYiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=45f01d97-ba88-46f1-bff3-aaa5421459f5&link=70d9adc4-588c-49ea-bfd5-a04b682b131b&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "tedarikci-dagitim-oranlamada-donemsel-degerlendirme_90673820_90673814.html"
source_version: "2022-11-02T14:13:49.330+03:00"
source_bytes: 327657
fetched_at: "2026-09-13T04:23:51+00:00"
generator: "netsis-scraper 1.0.0"
---
# Tedarikçi Dağıtım Oranlamada Dönemsel Değerlendirme

Tedarikçi Dağıtım Oranlamada Dönemsel Değerlendirme ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

**MRP-Tedarikçi** **Dağıtım** **Oranlamada** **Dönemsel** **Değerlendirme**

MRP'de malzemelerin tedarik edileceği tedarikçilerin belirlenmesinde malzeme bazında oransal dağılım ya da belirtilen önceliklere göre tedarikçilerin kapasitelerini doldurma yöntemlerinin kullanılması için, MRP Parametreleri/Genel-1/**MGP Oluşturmada** **Satıcı** **Belirleme** **Yöntemi** parametresi kullanılır.

![](../_assets/4dfbeadd2e5d2f4d0c0b.png)

Dağıtım Oranlama uygulamasının kullanıldığı durumlarda, dönemsel kota değerlendirmesi desteklenir. Bu şekilde, ilgili tedarikçiden alınacak miktar hesaplanırken geçmiş dönem içinde yapılan alımlar da dikkate alınır.

**Not:** Dağıtım Oranlama uygulamasının kullanılması için, MRP Parametreleri "Sipariş Bazında Rezervasyon Sistemi" parametresinin seçilmesi gerekir.

Dağıtım oranlamada değerlendirme için dönem tipi seçimi, Stok Planlama Kayıtları ekranındaki "Planlama-2" sekmesinden yapılır.

![](../_assets/1b24aa93a1ef023931ed.png)

Dağıtım oranlamada değerlendirme için aşağıdaki dönem tipleri desteklenir:

- **Aylık:** MRP'nin çalıştığı tarih göz önünde bulundurularak içinde bulunulan ayın başından itibaren gerçekleşen satınalma hareketleri dikkate alınır.
- **Üç** **Aylık:** MRP'nin çalıştığı tarih göz önünde bulundurularak içinde bulunulan üç aylık dönemin başından itibaren gerçekleşen satınalma hareketleri dikkate alınır.
- **Altı** **Aylık:** MRP'nin çalıştığı tarih göz önünde bulundurularak içinde bulunulan altı aylık dönemin başından itibaren gerçekleşen satınalma hareketleri dikkate alınır.
- **Yıllık:** MRP'nin çalıştığı tarih göz önünde bulundurularak içinde bulunulan yılın başından itibaren gerçekleşen satınalma hareketleri dikkate alınır.

MRP tarafından fason yarı mamuller için; açılan iş emri veya satıcı siparişinde de, dağıtım oranları ve dönemsel değerlendirme yöntemi kullanılabilir.

Örneğin; HAMMADDE01 ürünü 3 farklı tedarikçiden alım yapılmaktadır. Müşteri – Satıcı Stok Kayıtları tanımlamalarında tedarikçi bazında sipariş oranları aşağıdaki gibi tanımlıdır.

|  |  |
| --- | --- |
| Cari | Sipariş Oranı |
| A Tedarikçi | 50% |
| B Tedarikçi | 20% |
| C Tedarikçi | 30% |

![](../_assets/194035f19a5ca7e240a0.png)

Stok Planlama Kayıtları ekranında HAMMADDE01 için **Dağıtım** **Oranlamada** **Değerlendirme** yöntemi **"3 Aylık"** seçilidir.

HAMMADDE01 ürünü için son 3 aylık dönemde tedarikçi bazında yapılan alış miktar ve oranları aşağıdaki gibidir.

|  |  |  |
| --- | --- | --- |
| Son 3 Aylık Dönemsel Alış Miktarları |  |  |
| Cari | Miktar | Oran |
| A Tedarikçi | 450 | 32,61% |
| B Tedarikçi | 620 | 44,93% |
| C Tedarikçi | 310 | 22,46% |

Eylül ayı içinde HAMMADDE01 için MRP sonucunda **1670** adet gereksinim olduğu varsayılmıştır.

MRP Sonucunda, dağıtım oranlamada değerlendirme yöntemine göre tedarikçi bazında tanımlanan hedeflenen oranda sipariş miktarları aşağıdaki formül ile hesaplanmaktır:
A2 = A Tedarikçisi Planlama Dönemi Hedeflenen Alış Miktarı
B2 = B Tedarikçisi Planlama Dönemi Hedeflenen Alış Miktarı
C2 = C Tedarikçisi Planlama Dönemi Hedeflenen Alış Miktarı
K1 = Geçmiş 3 Aylık Dönem Alış Miktarı Toplamı (1380)
K2 = Gereksinim Miktarı (1670)

A Tedarikçisi;
(A1+A2)/(K1+K2)\*100=(Hedeflenen Oran)
Örnekteki A carisinin hedeflenen oranı %50 olduğundan hedeflenen orana 50 değeri yazılmıştır.
(450+A2)/(1380+1670)\*100=50
(450+A2)/(1380+1670)=0.5
(450+A2)=3050x0.5
450+A2=1525
A2=1525-450
**A2=1075**
A Tedarikçisinden toplam alış oranının %50 olarak hesaplanması için 1075 adet ürün alınmalıdır.
B Tedarikçisi için hedeflenen %20 oranda sipariş miktarı aşağıdaki gibi hesaplanmaktadır.
(B1+B2)/(K1+K2)\*100=20 (Hedeflenen Oran)
(620+B2)/(1380+1670)\*100=20
(620+B2)/(1380+1670)=0.2
620+B2=0.2x3050
620+B2=610
**B2=-10** (Sonuç 1'den küçük olduğu için B tedarikçisine sipariş önerilmemektedir.)
B Tedarikçisi için yapılan hesaplamada geçmiş dönemde %44 oranda 620 adet alım yapılmış iken gelecek dönem sonu ortalamasının %20 oranına düşürülmesi imkansızdır.
Toplam orana bakıldığında son 3 ayda 620 adet alım yapıldıktan sonra önümüzdeki dönemde hiç alım yapılmasa dahi B tedarikçisinin oranı %20,32 olarak hesaplanmaktadır.
B Tedarikçisi oranının %20 olabilmesi için toplam alışının 610 adet olması gerekirdi.
C Tedarikçisinde hedeflenen oranda sipariş miktarı aşağıdaki gibi hesaplanmaktadır.
(C1+C2)/(K1+K2)\*100=30 (Hedeflenen Oran)
(310+C2) /(1380+1670)\*100=30
(310+C2)/(3050)=0.3
310+C2=0.3x3050
310+C2=915
**C2=605**
Ancak; MRP sonucuna göre ihtiyaç miktarı olan 1670 ürün vardı ve A tedarikçisinden 1075 adet için sipariş önerisi yapıldı. Bu durumda kalan ihtiyaç miktarı **595**'tir. Aradaki 10 adet ürün farkı ise B tedarikçisinden yapılan alış oranındaki fazlalıktan kaynaklanmaktadır.

Yukarıdaki örneğin sonucuna göre 10 adet alışın hangi firmada eksik kalacağı konusunda sipariş oranı yüksek firmada (A Tedarikçisi %50) hedeflenen tam oran hesaplandıktan sonra diğer firmalara dağıtım yapılmaktadır.

Yukarıdaki örneğin MRP sonuç raporları ekran görüntüsündeki gibidir:

![](../_assets/505c97b30dbb338bf12b.png)
![](../_assets/e63b8936a3f4544731ee.png)
