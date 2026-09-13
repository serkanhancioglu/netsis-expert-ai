---
title: "ÖTV Hesaplaması Yenilik Dokümanı"
page_id: "50680274"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "ÖTV Hesaplaması Yenilik Dokümanı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / ÖTV Hesaplaması Yenilik Dokümanı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWY3OTMxMDBjLTVhYWItNDVkOS04MzRlLTg3ZjY1ZTIxZmU0NyZsaW5rPTkyNWQyMjM3LTA1MmYtNDU4Zi1hYTRlLTFmNTU5MTgwMTA0NCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=f793100c-5aab-45d9-834e-87f65e21fe47&link=925d2237-052f-458f-aa4e-1f5591801044&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "otv-hesaplamasi-yenilik-dokumani_82576780_50680274.html"
source_version: "2022-11-03T09:51:47.063+03:00"
source_bytes: 403893
fetched_at: "2026-09-13T04:26:18+00:00"
generator: "netsis-scraper 1.0.0"
---
# ÖTV Hesaplaması Yenilik Dokümanı

ÖTV Hesaplaması ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

|  |  |
| --- | --- |
| **Ürün** **Grubu** | \[X\] Fusion@6<br>\[X\] Fusion@6 Standard<br>\[X\] Entegre@6 |
| **Kategori** | \[X\] İyileştirme |
| **Versiyon** | @6 |
| **Önkoşulu** | Fatura.dll (4.0.12.7910) |
|  | Dizayn.dll (4.0.12.1796) |
|  | Dbupdate |

8 Temmuz 2008 tarihli 26930 sayılı Resmi Gazete'de yayımlanan 14 Seri No'lu Özel Tüketim Vergisi Genel Tebliği ile ÖTV Kanunu uygulamasına göre; "...(II) sayılı listedeki mallardan alınacak verginin, mükellefin bu malları alış bedeli üzerinden malın tabi olduğu orana göre hesaplanan vergi tutarından az olamayacağı hükme bağlanmıştır.
İthalatçıların alış bedeli olarak, ithalatta hesaplanan KDV matrahı esas alınacaktır. Verginin alış bedeli üzerinden hesaplandığı durumlarda, mükellefin malı teslim tarihine kadar bu malı mükellefe teslim eden tarafından % 10'a kadar yapılan indirimler alış bedelinden indirilecektir.
Buna göre, mükelleflerin teslim ettikleri (II) sayılı listedeki mallara ilişkin hesapladıkları (varsa ticari teamüllere uygun iskonto tutarının da düşülmesi sonucu oluşan) ÖTV'nin matrahı alış bedelinden daha düşük ise, ÖTV alış bedeli üzerinden hesaplanacaktır. Bu malların mükellef tarafından teslimi tarihine kadar, malları mükellefe satanların satış bedeli üzerinden indirim yapmış olması halinde, mükellefin alış bedelinin %10'unu aşmamak üzere yapılan indirim tutarının düşülmesi sonucu kalan tutar ÖTV'nin matrahının tespitinde dikkate alınacaktır.
Mükellefin satış bedelinin ÖTV matrahının tespitinde dikkate alınacak olan bu tutardan düşük olması halinde, ÖTV matrahının tespitinde dikkate alınan bu tutar üzerinden ÖTV hesaplanacaktır."
Netsis paketlerinde, satış belgelerinde ÖTV'nin tebliğde belirtilen içeriğe uygun olarak hesaplanması desteklenmiştir. Satış faturası, satış irsaliyesi, müşteri siparişi, satış talep ve teklif kayıtlarında, ÖTV'ye tabi kalemler için alış fiyatı sorgulanacaktır. Belgede girilen satış fiyatı alış fiyatından düşük ise, ÖTV tutarının hesaplaması alış fiyatı üzerinden yapılacaktır.
Hesaplamanın yukarıda açıklanan şekilde yapılabilmesi için öncelikle Yardımcı Programlar/Özel Parametre Tanımlamaları bölümünde aşağıdaki tanımlama yapılmalıdır.
![](../_assets/3b6427996ca849eea3d4.png)

Bu durumda satış belgelerinde kalem girişi sırasında, satışta ÖTV'ye tabi stoklar için ÖTV Alış Fiyatı sahası sorgulanır. Stoğa ait alış fiyatı, sahanın sağında bulunan ve önceden girilen alış faturalarındaki fiyatları içeren rehberden seçilebilir.
Eğer stok ÖTV'ye tabi değil ise, bu saha pasif gelecektir.
ÖTV Alış Fiyatı sahası 0 (sıfır) geçildiğinde ya da bu sahaya girilen fiyat satış fiyatından düşük olduğunda, ÖTV hesaplaması satış fiyatı üzerinden yapılacaktır.
Yukarıdaki örneğimizde bulunan araç stoğu için satışta uygulanacak ÖTV oranı %10 olarak tanımlanmıştır. Ayrıca 22.000 TL'ye alınan araç 20.000 TL'ye satılmaktadır. Bu durumda ÖTV matrahı 22.000 YTL olacaktır. Hesaplanacak ÖTV tutarı ise, 2.200 TL'dir.
![](../_assets/815813b815d6cfb2b787.png)
Dizaynlarda basım için, kalem bilgilerinde girilen ÖTV Alış Fiyatı 4511 no'lu alan kullanılarak basılabilir.
