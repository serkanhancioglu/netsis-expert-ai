---
title: "İş Emri Malzeme Rezervasyonu Destek Dokümanı"
page_id: "50684707"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "İş Emri Malzeme Rezervasyonu Destek Dokümanı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / İş Emri Malzeme Rezervasyonu Destek Dokümanı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWY4ZWRkOTlhLWIxNzEtNGFmOC1iNWFmLWI0ZDViNTBjN2VkNyZsaW5rPTg2MjY3ZGMxLTZhNWMtNGI1MC1iYmYxLWIyMWNhZDU2MzAxNCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=f8edd99a-b171-4af8-b5af-b4d5b50c7ed7&link=86267dc1-6a5c-4b50-bbf1-b21cad563014&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "is-emri-malzeme-rezervasyonu-destek-dokumani_90669822_50684707.html"
source_version: "2022-11-03T09:56:44.103+03:00"
source_bytes: 496040
fetched_at: "2026-09-13T04:26:31+00:00"
generator: "netsis-scraper 1.0.0"
---
# İş Emri Malzeme Rezervasyonu Destek Dokümanı

İş Emri Malzeme Rezervasyonu ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

İş Emri Malzeme Rezervasyonu, depolardan malzeme çekilmesini kolaylaştırmak için kullanılan bir ekrandır.

**İş Emri Seçimi**

İş emri seçimi sekmesinde, hangi depodan hangi depoya malzeme rezervasyonu gerçekleştirilecek ise Rezervasyon Yap ya da Rezervasyon Taşıma seçeneklerine göre rezervasyon tipi belirlenir.

Rezervasyon yap seçeneği ile daha önceden rezervasyon işlemi gerçekleşmemiş malzemeler için işlem gerçekleştirilir. Rezervasyon taşıma ise, halihazırda bir depoda ya da kendi deposunda yapılmış rezervasyonu, olduğu gibi farklı bir depoya taşımaya yarar. Örneğin malzeme ambarında rezerve edilmiş malzemeleri, fiziksel olarak transfer edildiği sırada üretim hattına taşımak için kullanılabilir.

İş emri seçimi sekmesinde, "Malzemeler bulundukları depoya rezerve edilsin" seçeneği işaretlendiği takdirde , Giriş Depo Kodu sorgulanmayacak, yapılacak rezervasyon işlemi kendi deposu içinde yapılacaktır.

![](../_assets/f28db81ac30f260afea2.png)

**İş Emri Kısıt Girişi**

Bu ekranda iş emirlerinin durumuna, mamul ve hammadde bilgisine göre rezervasyonu yapılacak iş emirlerinin belirlenmesi sağlanabilir.

İş Emri seçeneği ile iş emirlerinin mevcut malzemeleri dikkate alarak ihtiyacın karşılanma durumuna göre listelenmesi sağlanmıştır. İş emri seçenekleri; Hepsi, Tamamı transfer edilmiş iş emirleri getirilsin, Tamamı transfer edilmiş iş emirleri getirilmesin ve Tamamı transfer edilebilecek iş emirleri getirilsindir.

Ayrıca iş emri seçimini kolaylaştırmak adına, listelenen iş emirlerine ait üretilebilecek set miktarı cinsinden, halihazırda rezerve edilmiş toplam miktar (rezv.miktar), bu miktarın toplam ihtiyaca oranı (rezv.yüzdesi), varsa giriş depo dışındaki depolarda rezerve edilmiş miktar (top.rezv.miktar), mevcut stoklarla rezerve edilebilecek miktar (set miktarı) ve bu miktarın toplam ihtiyaca oranı (set yüzdesi) gibi bilgilerde bulunmaktadır. Bu ekranda listelenen malzeme ihtiyacı karşılama oranları, her iş emri için ayrı ayrı rezervasyon yapılacağı düşünülerek hesaplanır.

Kümülasyon yapılmamaktadır. Herhangi bir iş emri için rezervasyon yapılacak olursa diğerleri için karşılama oranları değişebilir.

![](../_assets/63b89f2e71110f9724b8.png)

Toplu rezervasyon butonu ile iş emirlerinin ekrandaki sıralaması ve toplu rezervasyon politikası seçimine göre işlem gerçekleşmektedir.

"Bileşen ihtiyacının tamamı rezerve edilebilen iş emirleri rezerve edilsin" parametresi ile Toplu rezervasyon yapılırken iş emrinin ihtiyaç duyduğu bileşen miktarının tamamı rezerve edilebiliyorsa, **yani yeterli stok** **bakiyesi varsa**, ancak bunlar rezerve edilir. **Örneğin** HM1 için 1000 adet gereksinim var ve depoda da 1000 adet bakiye varsa bu iş emrine rezervasyon yapılacaktır. Ancak depoda 500 adet bakiye var ise rezervasyon yapılamayacaktır.

"Bileşen ihtiyacı kısmi şekilde rezerve edilebilen iş emirleri rezerve edilsin" parametresi işaretlendiğinde yeterli stok bakiyesi olmasa da mevcut bakiye kadar rezervasyon gerçekleştirilir. Örneğin HM1 için 1000 adet gereksinim var ve depoda da 500 adet bakiye varsa bu iş emrine kısmi olarak rezervasyon yapılacaktır.

Normalde rezervasyon sırasında DAT kaydı oluşuyorsa, her iş emrinin ihtiyaç duyduğu miktar için ayrı satır olarak DAT belgesinde kayıt oluşmaktadır. "DAT belgeleri için miktarlar stok bazında kümüle edilsin" parametresi işaretlendiğinde ise stok kodu ve giriş-çıkış depoya göre kümüle edip satır sayısını azaltabilmektedir.
