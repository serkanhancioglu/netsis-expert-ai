---
title: "MRP - Tedarikçi Dağıtım Oranlamada Dönemsel Değerlendirme"
page_id: "50669110"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "MRP - Tedarikçi Dağıtım Oranlamada Dönemsel Değerlendirme"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / MRP - Tedarikçi Dağıtım Oranlamada Dönemsel Değerlendirme"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWQ0ZTNlOTU4LTQ1YWYtNDgzNS04ODc1LThhODI3NjdiZjFlNyZsaW5rPWJmMDY4YjM3LWFhMjktNDdkMy04OWUwLTRjNjhlMWY4NjcyZiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=d4e3e958-45af-4835-8875-8a82767bf1e7&link=bf068b37-aa29-47d3-89e0-4c68e1f8672f&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "mrp-tedarikci-dagitim-oranlamada-donemsel-degerlendirme_50669159_50669110.html"
source_version: "2022-12-13T09:58:27.057+03:00"
source_bytes: 147812
fetched_at: "2026-09-13T04:25:35+00:00"
generator: "netsis-scraper 1.0.0"
---
# MRP - Tedarikçi Dağıtım Oranlamada Dönemsel Değerlendirme

MRP-Tedarikçi Dağıtım Oranlamada Dönemsel Değerlendirme ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

MRP'de malzemelerin tedarik edileceği tedarikçilerin belirlenmesinde malzeme bazında oransal dağılım ya da belirtilen önceliklere göre tedarikçilerin kapasitelerini doldurma yöntemleri kullanılabilir. Bunun için MRP Parametreleri-Genel-1- MGP Oluşturmada Satıcı Belirleme Yöntemi parametresinin kullanılması gerekir.

![](../_assets/d7aba92fee800e7fbdb0.png)

Dağıtım Oranlama uygulamasının kullanıldığı durumlarda dönemsel kota değerlendirmesi desteklenir. Bu şekilde, ilgili tedarikçiden alınacak miktar hesaplanırken geçmiş dönem içinde yapılan alımlar da dikkate alınır.

> [!NOTE]
> Uygulamanın kullanılması için MRP Parametreleri-"Sipariş Bazında Rezervasyon Sistemi" parametresinin seçilmesi gerekir.

Dağıtım oranlamada değerlendirme için dönem tipi seçimi Stok Planlama Kayıtları ekranındaki "Planlama-2" sekmesinden yapılır.

![](../_assets/ec0e59bac4a9581e2190.png)

Dağıtım oranlamada değerlendirme için aşağıdaki dönem tipleri desteklenir:

**Aylık:** MRP'nin çalıştığı tarih göz önünde bulundurularak içinde bulunulan ayın başından itibaren gerçekleşen satınalma hareketleri dikkate alınır.

**Üç** **Aylık:** MRP'nin çalıştığı tarih göz önünde bulundurularak içinde bulunulan üç aylık dönemin başından itibaren gerçekleşen satınalma hareketleri dikkate alınır.

**Altı** **Aylık:** MRP'nin çalıştığı tarih göz önünde bulundurularak içinde bulunulan altı aylık dönemin başından itibaren gerçekleşen satınalma hareketleri dikkate alınır.

**Yıllık:** MRP'nin çalıştığı tarih göz önünde bulundurularak içinde bulunulan yılın başından itibaren gerçekleşen satınalma hareketleri dikkate alınır.

MRP tarafından fason yarı mamuller için açılan iş emri veya satıcı siparişinde de dağıtım oranları ve dönemsel değerlendirme yöntemi kullanılabilir.

Örnek vermek gerekirse,HAMMADDE1 için Müşteri-Satıcı Stok Kayıtları ekranında SATICI1 cari hesabına %30 ve SATICI2 cari hesabına %70 dağıtım oranlarının tanımlandığı varsayıldığında, HAMMADDE1 için stok planlama kayıtlarında dağıtım değerlendirme yöntemi olarak "Aylık" seçilmiş olsun.

HM1 için SATICI1 ve SATICI2'den dönem içinde yapılan alım miktarları aşağıdaki gibidir:

| Tarih | Cari Kodu | Miktar |
| --- | --- | --- |
| 01.05.2020 | SATICI2 | 1,000 |
| 05.05.2020 | SATICI2 | 800 |
| 10.05.2020 | SATICI1 | 200 |

Alım Miktarı, ilgili dönemde satıcıdan sipariş bağlantılı olarak irsaliye ve fatura ile yapılan tüm alımları kapsar. Dönemsel Dağıtım Oranı uygulamasının olmadığı durumda MRP çalıştırıldığında, dağıtım oranlarına göre açılacak satıcı siparişi miktarları; SATICI1: 300, SATICI2: 700 olur. Dönemsel Dağıtım Oranı uygulamasında "Aylık" seçeneği işaretli iken, Şubat ayı içinde çalıştırılacak MRP'nin önereceği satıcı siparişleri aşağıdaki gibidir:

![](../_assets/79206a685550eef3a51e.png)

SATICI1'den 1 aylık dönemde yapılan toplam satın alma: 200
SATICI2'den 1 aylık dönemde yapılan toplam satın alma: 1800
MRP'nin dönemsel değerlendirme kapsamında önerdiği SATICI1 sipariş miktarı: 700
MRP'nin dönemsel değerlendirme kapsamında önerdiği SATICI2 sipariş miktarı: 300

Dönem Toplamı Dağılım Oranları aşağıdaki şekilde sağlanır:
SATICI1 : (200 + 700) / 3000 = %30
SATICI2 : (1800 + 300) / 3000 = %70
