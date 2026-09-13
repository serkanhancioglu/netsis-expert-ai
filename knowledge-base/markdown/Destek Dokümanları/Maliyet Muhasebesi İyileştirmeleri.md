---
title: "Maliyet Muhasebesi İyileştirmeleri"
page_id: "50679810"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Maliyet Muhasebesi İyileştirmeleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Maliyet Muhasebesi İyileştirmeleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTBhMjBhMTUwLTdiOGYtNGFhYy04ZTM0LTA3ZDU2MDc4ZjkwYSZsaW5rPTA3Yjk2ZjNmLTc5NTUtNDU1ZC05YzA2LWZiMDc0NjdlNDNjMyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=0a20a150-7b8f-4aac-8e34-07d56078f90a&link=07b96f3f-7955-455d-9c06-fb07467e43c3&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "maliyet-muhasebesi-iyilestirmeleri_82575847_50679810.html"
source_version: "2022-11-03T09:15:51.370+03:00"
source_bytes: 252264
fetched_at: "2026-09-13T04:25:50+00:00"
generator: "netsis-scraper 1.0.0"
---
# Maliyet Muhasebesi İyileştirmeleri

Maliyet Muhasebesi İyileştirmeleri ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Güncelleme Tarihi: 12.12.2016
![](../_assets/fe06a1771bcbe1807c93.png)

**Genel**

|  |  |
| --- | --- |
| Ürün Grubu | \[X\] Netsis Enterprise \[X\] Netsis Standard |
| Kategori | \[X\] Yeni Fonksiyon |
| Modül | Maliyet Muhasebesi, Üretim |
| Versiyon Önkoşulu | 9.0.4 Onaylı Versiyon |
| Gerekli Dosyalar | 9.0.4 Seti Dosyaları |

#### Üretim Sürelerini Kullanarak Birim Katsayı Güncelleme Desteği

Maliyet Muhasebesi-İşlemler-Birim Katsayı Güncelleme ekranı üzerinden mamul grupları için topluca birim katsayı hesaplama ve güncelleme desteği sağlanmıştır. Üretim akış kontrol modülünden elde edilen üretim süreleri, reçetelerdeki üretim süreleri veya çizelgeleme tanımlarındaki üretim süreleri kullanılarak birim katsayı hesaplanabilir.
Bu ekranın ana amacı, mamul grupları bazında birim üretim sürelerini hesaplamak ve bu süreleri, verilen tarih aralığında mamul ana grubu altında üretilmiş ürünlerin toplam üretim süresine oranlayarak 0-1 arasında birim katsayı hesaplamaktır.
![](../_assets/788486e7b18277e1e50c.png)

"Hesaplama" sekmesinde aşağıdaki parametreler ve kısıtlar seçilmelidir:

- Birim Katsayı Hesaplama Verisi: Bu bölümde üretim akış kontrol, reçete veya çizelgeleme seçeneklerinden biri seçilebilir. Üretim akış kontrol seçilirse, üretim akış kontrol modülünde girilen kayıtlar kullanılarak mamul grupları için birim üretim süreleri hesaplanacaktır. Reçete seçilirse, mamul grupları için reçetelerdeki operasyonların üretim süreleri kullanılarak birim üretim süreleri hesaplanacaktır. Çizelgeleme seçilirse, mamul grupları için çizelgeleme uygulamasında yapılan operasyon-makine eşleşmelerindeki üretim süreleri kullanılarak birim üretim süreleri hesaplanacaktır.
- UAK Tarih Aralığı: Hesaplama verisi olarak "Üretim akış kontrolden getirilsin" seçilirse bu kısıt aktif hale gelmektedir. Hesaplama sırasında kullanılacak üretim akış kontrol kayıtlarının tarih aralığını filtrelemek için kullanılabilir.
- Mamul Ana Grup Kodu: Birim katsayı hesabının yapılacağı mamul ana grubu için kısıt verilebilir.
- Güncellenecek Gider Hesapları: Birim katsayı bilgisinin hangi giderler için güncelleneceği bu bölümde seçilmelidir.

"Hesaplama sonuçları" sekmesinde mamul grupları için hesaplanan yeni birim katsayılar "yeni değer" kolonunda görülmektedir. Mamul grubu için giderler bazında daha önceden tanımlı olan birim katsayılar da ayrı kolonlarda raporlanmaktadır (işçilik, enerji vs.). Yeni değer kolonundaki birim katsayılar grid üzerinden değiştirilebilir. Eğer ilgili mamul ana grubunun gider hesabının dağıtım anahtarı "birim katsayılar oranı" değilse, bu satırlar için birim katsayılar güncellenmeyecektir ve ekranda pasif olarak görünecektir. "Kaydet" butonuna tıklanarak birim katsayıların topluca güncellenmesi sağlanır.
Örnek uygulamada, Preshane mamul ana grubu altında aşağıdaki mamul grupları bulunmaktadır ve bu mamul gruplarına ait üretim akış kontrol kayıtlarından elde edilen birim üretim süreleri görülmektedir:

| **Mamul** **Grup** **Kodu** | **Birim** **Üretim** **Süresi** |
| --- | --- |
| YARIMAMUL1 | 15 sn |
| YARIMAMUL2 | 25 sn |
| YARIMAMUL3 | 30 sn |

Mamul grubuna ait birim katsayı hesabında aşağıdaki formül kullanılmaktadır:

`𝐵𝐵𝐵𝑟𝐵𝐵𝑚 𝐾𝑎𝑡𝑠𝑎𝑦𝐾𝐾 = 𝑀𝑎𝑚𝑢𝑙 𝑔𝑟𝑢𝑏𝑢𝑛𝑢𝑛 𝑏𝐵𝐵𝑟𝐵𝐵𝑚 ü𝑟𝑒𝑡𝐵𝐵𝑚 𝑠ü𝑟𝑒𝑠𝐵𝐵 ÷``𝑀𝑎𝑚𝑢𝑙 𝑎𝑛𝑎 𝑔𝑟𝑢𝑏𝑢𝑛𝑑𝑎 ü𝑟𝑒𝑡𝐵𝐵𝑙𝑒𝑛 𝑏ü𝑡ü𝑛 ü𝑟ü𝑛𝑙𝑒𝑟𝐵𝐵𝑛 𝑡𝑜𝑝𝑙𝑎𝑚 𝑏𝐵𝐵𝑟𝐵𝐵𝑚 ü𝑟𝑒𝑡𝐵𝐵𝑚 𝑠ü𝑟𝑒𝑠𝐵𝐵`
Bu örnek için mamul gruplarının birim katsayı hesapları aşağıdaki gibi olmaktadır:

| **Mamul** **Grup** **Kodu** | **Birim** **Üretim** **Süresi** |
| --- | --- |
| YARIMAMUL1 | 15/(15+25+30) = 15/70 = 0.2143 |
| YARIMAMUL2 | 25/(15+25+30) = 25/70 = 0.3571 |
| YARIMAMUL3 | 30/(15+25+30) = 30/70 = 0.4286 |

## ![](../_assets/ac6fa698dc674a478a46.png)

#### Ürün Konfigüratöründe Ön Maliyet Desteği

Ürün konfigüratörü ekranında "maliyet hesapla" butonu yardımıyla ön maliyet hesabının yapılabilmesi desteklendi. Daha önceki aylarda maliyet muhasebesi hesabına dahil edilmiş yarı mamul ve mamuller için birim gider bilgileri (işçilik, enerji vs.) otomatik olarak getirilmektedir. Daha önceki aylarda maliyet muhasebesi hesabına dahil edilmemiş ürünler veya yeni tanımlanan bileşenler için, reçeteye eklenen operasyonlar üzerinden işçilik veya diğer gider girişi yapılabilir.
Ön maliyet hesabında hammaddelerin maliyeti anlık olarak üretim modülündeki maliyet tipine göre hesaplanmaktadır.
Yarı mamuller ve mamuller için maliyet muhasebesinden getirilen birim gider tutarları "reçete üst bilgileri" sekmesinde raporlanabilir. "Otomatik kontrol ayarları" butonuyla açılan bölümde "Maliyet Kontrol" sekmesinde maliyet hesaplama yöntemi olarak "Bileşen maliyetleri ve üretim giderleri" veya "Sadece bileşen maliyetleri" seçeneklerinden biri seçilebilir. "Sadece bileşen maliyetleri" seçeneği işaretlenirse maliyet hesabına gider tutarları dahil edilmeyecektir. Tepe mamulün toplam maliyet bilgisi ekranın alt bölümünde görülebilir. Taslak olarak kaydedilen reçete ve gider bilgilerinin basımı için görsel basım desteği getirilmiştir. "Konfigürasyon basımı" butonuyla görsel basım yapılabilir.

#### Maliyet Muhasebesi Veri Kontrol Raporu

Maliyet muhasebesi çalıştırmadan önce verilerdeki tutarsızlıkları, eksikleri ve hataları raporlamak amacıyla *Maliyet Muhasebesi-Raporlar* menüsüne "maliyet muhasebesi veri kontrol raporu" eklenmiştir.
Bu rapor kapsamında kontrol edilen hata türleri aşağıdaki gibidir:

-
  - Üzerinde sarf olmasına rağmen üretim girişi olmayan stok kodları.
  - Tanımı veri tabanı seviyesinde eksik olan stok kartları (TBLSTSABITEK).
  - Reçetesi olduğu halde stok kartındaki türü yan ürün-yarı mamul-mamul seçilmemiş veya mamul grubu boş olan stok kodları.
  - Stok kartındaki türü yan ürün, yarı mamul veya mamul olmasına rağmen mamul grubu tanımsız stoklar.
  - Stok kartındaki mamul grup kodunun maliyet muhasebesi modülünde tanımı bulunmuyor.
  - Mamul grubu tanımlı olmasına rağmen stok kartındaki türü seçilmemiş stok kodları.
  - Stok kartındaki tür bilgisiyle mamul grubundaki tür bilgisi aynı olmayan stok kodları.
  - Üretim hareketi olmasına rağmen stok tanımı bulunmayan stok kodları.
  - Sarf edilmesine rağmen stok tanımı bulunmayan stok kodları.
  - Sarf hareketi olmasına rağmen sarf edildiği mamul ana grubu bulunamayan stok kodları.
  - Üretim hareketi olmasına rağmen mamul grubu tanımlı olmayan stok kodları.
  - Mamul grubu üzerinde sarf hareketi olmasına rağmen mamul grup tanımı bulunmuyor.
  - Yarı mamul ve yarı mamul transfer hesabı tanımsız olan mamul grup kodları.
  - Mamul veya yan ürün türünde olmasına rağmen mamul hesap kodu tanımsız olan mamul grup kodları.
  - Hammadde sarf hesabı tanımsız olan mamul grup kodları.
  - Mamul türünde olmasına rağmen satılan malın maliyeti hesabı tanımsız olan mamul grup kodları.
  - Türü yarı mamul, yan ürün veya mamul olmasına rağmen satın alması yapılan stok kodları.
  - Mamul ana grubu tanımlı olmayan mamul grup kodları.
  - İşlem sırası tanımında kullanılmayan mamul ana grup kodları.
  - Türü mamul, yarı mamul veya yan ürün olmasına rağmen satın alması yapılan fiş numaraları.

![](../_assets/e876766df65e843645ed.png)
