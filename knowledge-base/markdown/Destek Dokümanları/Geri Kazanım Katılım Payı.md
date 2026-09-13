---
title: "Geri Kazanım Katılım Payı"
page_id: "50671871"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Geri Kazanım Katılım Payı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Geri Kazanım Katılım Payı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWUwNDI4OGE5LWYwYTAtNDUzYi04ZWUzLWFjZjg1OGY3YWVjNCZsaW5rPWE4NjVmYjlhLWRlMjktNGM1Ny1hZTM5LTMxZmYzMmRmMjliYyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=e04288a9-f0a0-453b-8ee3-acf858f7aec4&link=a865fb9a-de29-4c57-ae39-31ff32df29bc&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "geri-kazanim-katilim-payi_50671879_50671871.html"
source_version: "2022-11-03T08:59:12.613+03:00"
source_bytes: 829543
fetched_at: "2026-09-13T04:25:28+00:00"
generator: "netsis-scraper 1.0.0"
---
# Geri Kazanım Katılım Payı

Geri Kazanım Katılım Payı ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Çevre Kanunu'na eklenen Geri Kazanım Katılım Payı başlıklı Ek 11. Madde uyarınca Ek-1 sayılı listede yer alan plastik poşetler için Geri Kazanım Katkı Payı uygulaması 1 Ocak 2019 tarihinde başladı.Söz konusu listede yer alan diğer kalemlerden **Lastik, Akümülatör, Pil, Madeni Yağ, Bitkisel Yağ, Elektrikli ve Elektronik Eşya, İlaç, Plastik Ambalaj, Metal Ambalaj, Cam Ambalaj, Ahşap Ambalaj** için Geri Kazanım Katılım Payı uygulaması 1 Ocak 2020 tarihi itibariyle devreye alındı.
1 Ocak 2020 tarihi itibariyle yürürlüğe giren Geri Kazanım Katılım Payına İlişkin Yönetmelik'te, uygulamaya ilişkin açıklama ve düzenlemeler yapıldı. Yönetmelik kapsamında yer alan ürünlerden sadece **yurt içinde** piyasaya arz edilenlere geri kazanım katılım payı uygulanır.

Bu kapsamda Netsis ERP'de GEKAP ile ilgili yapılması gerekenler aşağıda yer alır:

- Alış ve satış faturalarında GEKAP hesaplamalarının aktif olması için öncelikle Lojistik/Satış-Fatura-Kayıt-Satış Parametreleri/Alış Parametreleri-Genel-3 sekmesinde bulunan "Geri Kazanım Katılım Payı Desteği Uygulaması (GEKAP)" parametresinin seçilmesi gerekir.

![](../_assets/801e8beb9693ccab7921.png)

- GEKAP kapsamındaki **Lastik, Akümülatör, Pil, Madeni Yağ, Bitkisel Yağ, Elektrikli ve Elektronik Eşya, İlaç, Plastik Ambalaj, Metal Ambalaj, Cam Ambalaj, Ahşap Ambalaj** gibi stok kartlarında Stok Mevzuat Tipi olarak GEKAP Stok seçeneğinin seçilmesi gerekir.

![](../_assets/64d883552a7b7576b425.png)

- Belgelere ait muhasebe kayıtlarında, GEKAP ve Ambalaj Tutarı için kullanılacak muhasebe hesapları ise Muhasebe-Entegre-Kayıt-Entegrasyon Kayıtları-Fatura Genel-2 sekmesinden tanımlanması gerekir.

![](../_assets/1292b8d73e0b56828d87.png)

- Tüm bunlara ek olarak, bazı cari hesaplar GEKAP kapsamı dışında kalır. Bu cari hesaplarda GEKAP hesaplamasının yapılmaması için, Finans-Cari-Kayıt-Cari Hesap Kayıtları → Cari Kart 2 sekmesinden "Geri Dönüşüm Katılım Payı Hesaplamasın" parametresinin işaretlenmesi gerekir.

![](../_assets/f580ba4d3a169e8dbd9e.png)

**Fatura**
Mevzuat Tipi olarak GEKAP Stok seçilen bir stok için, fatura işlemlerinin "Kalemler" sekmesinde GEKAP uygulamasına ait alanlar aktif hale gelir.
![](../_assets/af8429532b05e7299994.png)

Yukarıdaki örnekte 16 Kg'lık bir yağ stoğu için 228 TL birim fiyat ve 8 TL (Yönetmelik gereği Kg başına 0,50 kuruş) GEKAP tutarı girilmiştir. Stok kartına 24,01 ÖTV tutarı tanımlanmıştır.
Belge kaleminin KDV'si, Mal Bedeli+GEKAP Tutarı+GEKAP Ambalaj Tutarı+ÖTV tutarı üzerinden hesaplanır.
\*Örnekte GEKAP Ambalaj Bedeli yoktur.
Bu durumda KDV aşağıdaki şekilde hesaplanır:
KDV= (228 TL + 8 TL +24,01 TL ) \* 0,18 =46,08

![](../_assets/73172057be765757b83a.png)
Belgeye ait oluşan muhasebe kaydı ise aşağıdaki şekildedir:

![](../_assets/50ea6584450def364515.png)

- GEKAP Tutarı olan 8 TL, Entegrasyon kodlarından tanımlanan Gekap Satış Hesabı'na aktarılmıştır.
- Mal bedeli olan 228 TL, stok kartında bulunan detay kodunun bağlı olduğu satış hesabına aktarılmıştır.
