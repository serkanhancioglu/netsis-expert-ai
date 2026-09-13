---
title: "Malzeme Detaylı Maliyet Raporu Destek Dokümanı"
page_id: "50679908"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Malzeme Detaylı Maliyet Raporu Destek Dokümanı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Malzeme Detaylı Maliyet Raporu Destek Dokümanı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWI0NjE4MzcwLTdmY2ItNDI4Yi05MzIxLTQ2ODFlZGRlNzg3YSZsaW5rPWQ0OTcwMjY0LWFmZWItNGNkNC1iNTE2LTQyNzZjYzAxMmVkZCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=b4618370-7fcb-428b-9321-4681edde787a&link=d4970264-afeb-4cd4-b516-4276cc012edd&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "malzeme-detayli-maliyet-raporu-destek-dokumani_82576086_50679908.html"
source_version: "2022-11-03T09:27:59.240+03:00"
source_bytes: 317136
fetched_at: "2026-09-13T04:25:54+00:00"
generator: "netsis-scraper 1.0.0"
---
# Malzeme Detaylı Maliyet Raporu Destek Dokümanı

Malzeme Detaylı Maliyet Raporu ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Malzeme Detaylı Maliyet Raporu ile ilgili destek dokümanı bilgileri aşağıdaki şekildedir:

| Tanım | Açıklama |
| --- | --- |
| Amaç ve Fayda | İşletme içerisinde maliyet muhasebesi işlemleri sonrasında mamul malzeme maliyetlerinin değerlendirilmesine yönelik "Malzeme Detaylı Maliyet Raporu" raporu oluşturulmuştur.<br>Yeni eklenen raporu yardımı ile ana grup ve mali gruplar bazında mamullerin reçetelerinde (alt seviyelerde göz önünde bulundurularak) yer alan malzemelerin reçete maliyetleri ile fiili maliyetlerinin karşılaştırılabilmesi desteklenmiştir. |
| Ürün Grubu | \[X\] Netsis Enterprise<br>\[X\] Netsis Standard |
| Modül | \[X\] Maliyet Muhasebesi |
| Kategori | \[X\] Yeni Fonksiyon |
| Versiyon Önkoşulu | 7.0.0 |
| Uygulama | Üretim sürecinde sarf değerlerinde oluşabilecek farklılıkların (kayıpların) takip edilebilmesine ve tespitine ışık tutacak bu rapor, Mamul ürünün kendi ve alt seviyelerinde yer alan tüm stok malzeme bileşenleri de değerlendirilmektedir.<br>Yapılan değerlendirmeyle ilk malzeme ve ambalajlar (sarflar) üzerinde planlanan (reçete) maliyet ile gerçekleşen (detaylı maliyet) maliyet arasındaki sapma oranı da detaylarıyla ele alınmaktadır. Mali grupta tespit edilen sapma oranı üretim reçete bileşenlerine ayrı ayrı yansıtılıp; fiili maliyet bölümünde oluşan değerler kullanıcıya sunulmaktadır.<br>Not: Reçete kontrollerinde mali grupların mamul ürünler ile birebir (1-1) eşlendiği öngörülmekte ve bu doğrultuda miktarsal hesaplamalar gerçekleştirilmektedir. |

## ![](../_assets/c7a8f5f7808dc70cb8fd.png)

Kısıtlar: Genel Kısıtlar bölümünde ana-mamul grup kodu aralığı ve ay-yıl seçenekleri ile değerlendirme kapsamı belirlenebilecektir. Rapor işlemi ile sonuçlar görüntülenebilecektir.

Rapor: Rapor ekranında kısıtlara göre belirlenen mali gruplar ve mamul ürünlerin reçete detayları görüntülenmektedir. Reçete detayları kapsamında sadece ilk malzemeler yer almaktadır. Mali grupların raporda görüntülenebilmesi için belirtilen ay içerisinde bakiyesinin bulunması gerekmektedir.

Reçete maliyeti, reçetede belirtilen miktar ve mali grup bakiye miktarı kullanılarak hesaplanmaktadır. Fiili maliyet toplamı, detaylı maliyet analiz verileri **(HAMORT+** **AYNAKHAMORT+AMBORT+OAYNAKAMBALAJORT)** ve mali grup bakiye
miktarı kullanılarak hesaplanmaktadır.

Bileşen bazında görüntülenen fiili maliyet ise, sapma oranının reçete maliyetlerine yansıtılması sonucunda oluşmaktadır.

Mali Grup Kodu ifadesi ile yer alan özet bölümde reçete maliyetleri ile fiili (gerçekleşen) maliyet takibi yapılabilecektir. Ayrıca, beklenen reçete maliyeti ve fiili maliyetin karşılaştırıldığı sapma oranı (%) alanında değişim, yüzde olarak ifade edilmektedir.
