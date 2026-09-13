---
title: "MRP - İş Emri Reçetesi Desteği"
page_id: "50669169"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "MRP - İş Emri Reçetesi Desteği"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / MRP - İş Emri Reçetesi Desteği"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTFmNDhiYzMzLTkzOTktNDEwMy1hZjEyLTBjNTFlODQ4MGYyYiZsaW5rPTIyNmYwODQzLTBjMGYtNDIxMC1iNDA0LWUxZDM3NWIxNTVhZCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=1f48bc33-9399-4103-af12-0c51e8480f2b&link=226f0843-0c0f-4210-b404-e1d375b155ad&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "mrp-is-emri-recetesi-destegi_50669176_50669169.html"
source_version: "2022-11-03T09:02:00.947+03:00"
source_bytes: 516949
fetched_at: "2026-09-13T04:25:33+00:00"
generator: "netsis-scraper 1.0.0"
---
# MRP - İş Emri Reçetesi Desteği

MRP-İş Emri Reçetesi Desteği ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

MRP'nin iş emri reçetelerini dikkate alarak çalışması desteklendi. Bu sayede MRP, çıkan mamul/yarı mamul ihtiyaçlarını karşılamak için sistemdeki mevcut iş emirlerini kullanır ve bu iş emirlerine ait düzenlenmiş reçeteler varsa, bunları dikkate alarak hammadde ihtiyaçlarını hesaplar.

> [!NOTE]
> Bu uygulamanın kullanılması için MRP Parametreleri → "Sipariş Bazında Rezervasyon Sistemi" parametresinin seçilmesi gerekir.

İş emri reçetelerinin dikkate alınması için MRP ekranında "İş Emri Reçetesi Kontrol Edilsin" parametresi mevcuttur.

MRP'nin, ihtiyaçları karşılama aşamasında reçetesi bulunan iş emirleriyle eşleşmesi için farklı kondisyonlar bulunur:

- İş emri müşteri siparişine rezerve-iş emrinde müşteri sipariş numarası ve sipariş satırı bilgileri varsa-edilmişse: Bu durumda iş emrinin bağlantılı olduğu müşteri siparişi ile eşleşme sağlanır ve mevcut iş emri reçetesi üzerinden işlem yapılır.
- Mamul/yarı mamul sipariş bazında takip edilmiyorsa: Bu durumda iş emirleri tüm ihtiyaçların kullanabileceği serbest durumdadır. İhtiyaçların karşılanması sırasında serbest iş emirleri kullanılır. Kullanılan iş emrindeki mamulün, iş emri reçetesi varsayılan reçetesinden farklı ise, iş emri reçetesi dikkate alınır ve bileşen ihtiyaçları iş emri reçetesine göre belirlenir. Kondisyonun bu şekilde oluşması için iş emrindeki mamul kodunun sipariş bazında takip edilmemesi - Stok Planlama Kayıtları → İş Emri ve Planlama Yöntemi - gerekir.
- İş emri müşteri siparişine rezerve değil ve mamul kodu sipariş bazında takip ediliyorsa: Böyle bir durumda serbest iş emrinin reçetesi ancak varsayılan reçete ile aynı ise mamul ihtiyaçlarına tahsis edilebilir. Varsayılan reçeteden farklı ise, iş emrinin ihtiyaçlar ile eşleşmesi mümkün değildir. Eşleşme sağlanamadığı için, iş emrine kapatma önerisi getirilir ve ihtiyaçlar için yeni iş emirleri açılır.

Örnek Uygulama olarak varsayılan reçetesi aşağıdaki gibi olan bir mamul için 500 adet iş emri bulunur ve bu iş emrine ait reçete yine aşağıda gösterilen şekildedir:

![](../_assets/9d3573870b4c0e07afcd.png)

STOK1 mamulü için iş emri ve planlama yöntemi olarak "Sipariş Bazında" seçilmiştir.

![](../_assets/f9a6555d1b3d83c596a2.png)

STOK1 için açılan iş emrine ait reçetede varsayılan reçeteden farklı olarak HM3 bileşeni de bulunur. İş emri müşteri siparişine rezerve durumdadır.

İş emrinin bağlantılı olduğu müşteri sipariş kalemine ait bilgiler aşağıdaki şekildedir:

![](../_assets/eb28a176f1193af68d67.png)

Yukarıda 1000 adet STOK1 ihtiyacı için aşağıdaki parametreler ile MRP çalıştırıldığında, önerilen satıcı siparişi kalemleri aşağıdaki şekildedir:

![](../_assets/28243603e609d6ffdd02.png)

![](../_assets/152555a11fa8de8d0dad.png)

Görüldüğü gibi MRP işlemi sonucu mevcut iş emri ile eşleşme sağlanmış ve mevcut iş emrinin reçetesine göre ihtiyaçlar çıkarılmıştır. HM3 bileşeni, varsayılan reçetede olmamasına rağmen iş emri reçetesinde bulunduğu için MRP tarafından HM3 bileşenine satıcı siparişi önerilmiştir.

MRP çalıştırılması sırasında "İş Emri Reçetesi Kontrol Edilsin" parametresi seçilmediği zaman sonuç aşağıdaki gibi olacaktır:

![](../_assets/8db0bac3bbd9f5f37328.png)
