---
title: "Alternatif Malzeme Tanımlama"
page_id: "50662660"
product: "netsis-3-enterprise"
depth: 4
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Üretim"
  - "Kayıt/Üretim"
  - "Alternatif Malzeme Tanımlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Üretim / Kayıt/Üretim / Alternatif Malzeme Tanımlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWU5N2Y0NGY2LTNlMTQtNGEwNy1iMDNmLWY2ZmZhNDVkNWE4MCZsaW5rPTQxOWJhZDRkLWFhZDgtNDFlZi05YjExLTA4MGQ4MmQ1MWU2MiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=e97f44f6-3e14-4a07-b03f-f6ffa45d5a80&link=419bad4d-aad8-41ef-9b11-080d82d51e62&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "alternatif-malzeme-tanimlama_50662954_50662660.html"
source_version: "2022-10-13T11:40:48.487+03:00"
source_bytes: 21843
fetched_at: "2026-09-13T04:18:45+00:00"
generator: "netsis-scraper 1.0.0"
---
# Alternatif Malzeme Tanımlama

Alternatif Malzeme Tanımlama, Üretim modülünde Kayıt/Üretim menüsünün altında yer alır. Reçetelerdeki bileşen ve/veya operasyonlar için alternatif tanımı yapılan bölümdür.

Malzeme Tanımı-1 ve Malzeme Tanımı-2 olmak üzere iki sekmeden oluşur.

**Malzeme Tanımı-1**

Alternatif Malzeme Tanımlama ekranı Malzeme Tanımı-1 sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Alternatif Malzeme Tanımlama Ekranı |  |
| --- | --- |
| Operasyon/Bileşen | Alternatif tanımı yapılacak kaydın reçetedeki durumunun belirtildiği seçeneklerdir. Operasyon ve Bileşen olmak üzere iki seçenekten oluşur. |
| Bileşen Kodu/Operasyon Kodu | Alternatif tanımı yapılacak bileşen/operasyon kodunun girildiği alandır. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile, kodlar arasından seçim yapılır. |
| Alternatif Kodu | Seçilen bileşen/operasyon için alternatif kod girilen alandır. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile, kodlar arasından seçim yapılır. |
| Asorti Kodu | Asorti kodunun girildiği alandır. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile, tanımlanan özellik kodlarına ulaşılır. |
| Asorti Kodu Açıklaması | Asorti koduna ait açıklama bilgisinin otomatik olarak ekrana getirildiği alandır. |
| Mamul Kodu | Alternatif tanımı yapılacak bileşen/operasyona ait mamul/yarı mamul kodunun girildiği alandır. Bileşen/operasyonunun birden çok mamul/yarı mamulde kullanıldığı durumda bu alana tek bir mamul kodu girilirse, alternatif malzeme sadece bu mamul reçetesi için geçerli olur. Mamul Kodu boş bırakıldığında ise, bileşenin kayıtlı olduğu tüm mamul/yarı mamul reçetelerinde tanımlanan alternatif malzeme kullanılabilir. |
| Öncelik | Bir bileşen için birden fazla alternatif malzeme tanımlanabilir. Malzemelerin önceliklerinin belirlenmesi için kullanılan alandır. Öncelik Kodu küçük olan malzeme önceliği en başta olan malzeme olacaktır. |
| Sıra No | Reçetede seçilen bileşen, aynı reçetede farklı sıralarda kullanılabilir. Reçetede belirli bir sıradaki bileşen için alternatif malzeme tanımlanıyorsa sıra numarası belirtilmesi gerekir. Sıra numarası belirtilmezse, bileşenin reçetedeki sırası dikkate alınmadan, bulunduğu tüm sıralar için aynı alternatif malzeme geçerli olacaktır. |
| Planlama Oranı | Ürün ağacında tanımlı olan bir malzemenin ve alternatif malzemelerin oran bazında gereksiniminin karşılanması için kullanılan alandır. Mamulün üretimi sırasında, yarı mamulden ne kadar kullanılacağı, burada belirtilen orana göre hesaplanır. **Örneğin;** Reçetedeki H1 hammaddesi için oran %60, H1’in alternatifi olan H2 hammaddesi için %40 girildiği varsayıldığında, mamulün üretimi için 100 adet H1’e ihtiyaç duyuluyorsa, bunun 60’ı H1’den, geri kalan 40’ı ise H2’den karşılanır. |
| Kat | Alternatif malzeme miktarının, reçetedeki bileşen miktarının belirli bir katı olarak girilmesi için kullanılan seçenektir. **Örneğin;** 1 birim M1 için reçetede 2 birim H1 kullanıldığı ve H1’in alternatifi olan H2 için miktar tipi “kat” seçildiği ve "Miktar" hanesine 1,5 girildiği varsayıldığında; bir birim M1 üretildiğinde H2’nin kullanılması gerekiyorsa, 3 (2x1,5) birim kullanılır. |
| Sabit | Alternatif malzeme miktarı için sabit bir değer girileceği zaman kullanılan seçenektir. Bu durumda sarf edilen bileşen miktarı, mamulün üretim miktarı ile alternatif malzeme tanımlama sayfasındaki miktar değerinin çarpımından oluşur. **Örneğin;** M1 mamulünün reçetesinde H1 hammaddesinden kullanıldığı, H1’in alternatifi olan H2 için de Miktar Tipi “Sabit” seçildiği ve "Miktar" alanına 3 girildiği varsayıldığında, bir birim M1 üretildiğinde H2’nin kullanılması gerekiyorsa 3 birim kullanılır. |
| Miktar | Alternatif malzemeye ait miktar/kat bilgisinin girildiği alandır. |
| Fire Miktarı | Alternatif malzemeye ait fire miktarının girildiği alandır. |
| Sabit Fire Miktarı | Değişmeyen fire tanımları için kullanılan alandır. |

> [!NOTE]
> **"Alternatif Malzeme Tanımlama Sağ Tuş Seçenekleri**" için bkz. [Reçete Kaydı Ekranında Kullanılan Sağ Tuş Seçenekleri](<Reçete Kaydı/Reçete Kaydı Ekranında Kullanılan Sağ Tuş Seçenekleri.md>)

**Malzeme Tanımı-2**

Malzeme Tanımı-2 sekmesine, reçetedeki operasyonların alternatiflerine ait süre ve maliyet bilgilerinin girilmesi gerekir.

Malzeme Tanımı-2 sekmesindeki alanlara değer girişi yapmak için; Malzeme Tanımı-1 sekmesindeki "Operasyon" seçeneğinin işaretlenmesi ve Bileşen Kodu alanına MRP’de tanımlanan bir operasyon kodunun girilmesi gerekir.

Malzeme Tanımı-1 sekmesinde "Mamul Kodu" boş bırakılırsa, operasyonun kayıtlı olduğu tüm mamul/yarı mamul reçetelerinde, alternatif operasyon kullanılabilir.

Mamul Kodunun girilmesi durumunda alternatif operasyon sadece o mamul/yarı mamul için geçerli olur.

Alternatif Malzeme Tanımlama ekranı Malzeme Tanımı-2 sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Alternatif Malzeme Tanımı Ekranı |  |
| --- | --- |
| İstasyon Kodu | Tanımlanan alternatif operasyonun yapıldığı iş istasyonunun girildiği alandır. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile, istasyon kodlarına ulaşılır. |
| Kat | Alternatif operasyona ait hazırlık, üretim ve geçiş sürelerinin, reçetedeki operasyona ait sürenin belirli bir katı olarak girilmesi için kullanılan seçenektir. |
| Sabit | Alternatif operasyona ait hazırlık, üretim ve geçiş süreleri için sabit bir değer girilmesi için kullanılan seçenektir. |
| Hazırlık Süresi | Tanımlanan alternatif operasyona başlanması için ne kadar gereken sürenin girildiği alandır. **Örneğin;** Operasyonda kullanılan makinenin ısınması için 30 dk. gerekmesi gibi. |
| Üretim Süresi | Tanımlanan alternatif operasyonda üretime başlanması ile, bir birim üretimin tamamlanması arasında geçen sürenin girildiği alandır. |
| Geçiş Süresi | Bir operasyonun bitiminden bir sonraki operasyona geçiş aşamasına kadar geçen sürenin kaydedildiği alandır. **Örneğin;** M1 mamulünün reçetesindeki Y1 kodlu operasyonun hazırlık süresi 10 dk. Y1’in alternatifi olan Y2 operasyonu için Süre Tipi “Kat” seçilmiş ve Hazırlık süresine 2 girildiği varsayıldığında bir birim M1 üretildiğinde Y2 operasyonu kullanılıyorsa, hazırlık süresi 20 (2\*10) dk. olarak hesaplanır. Y2 operasyonu için süre tipi “sabit” seçilmiş ve 25 dk. girilmişse, Y2 operasyonu kullanıldığında hazırlık süresi 25 dk. olacaktır. |
| Geçiş Miktarı | Bir sonraki operasyona geçiş miktarının girildiği alandır. |
| Simültane Tezgah Miktarı | Alternatif operasyonun bir anda yapılacağı tezgah sayısının girildiği alandır. Aynı işlem birden fazla makinede yapılabilir. Mevcut makineler aynı anda aynı mamul için bir işi yapabiliyorsa, toplam makine sayısının girilmesi gerekir. Makinelerin kalıp, aparat gibi malzeme gereksinimlerinden dolayı sadece 1 makinede işlem yapılabiliyorsa 1 değerinin girilmesi gerekir. |
| Maliyet | Maliyet seçiminin yapıldığı alandır. Kat ve Sabit seçenekleri arasından seçim yapılır. **Kat:** Alternatif operasyona ait işçilik, genel üretim ve diğer maliyetlerin, reçetedeki operasyona ait maliyetin belirli bir katı olarak girilmesi için kullanılan seçenektir. **Sabit:** Alternatif operasyona ait işçilik, genel üretim ve diğer maliyetlerin için sabit bir değer girileceği zaman kullanılan seçenektir. **Örneğin;** M1 mamulünün reçetesindeki Y1 kodlu operasyonun birim işçilik maliyetinin 1.000 TL olduğu, Y1’in alternatifi olan Y2 operasyonu için maliyet tipi “Kat” seçildiği ve işçilik maliyetine 2 girildiği varsayıldığında, Bir birim M1 üretildiğinde Y2 operasyonu kullanılıyorsa, işçilik maliyeti 2.0000 TL (2\*1.000) dk. olarak hesaplanır. Y2 operasyonu için maliyet tipi “Sabit” seçildiğinde ve birim işçilik maliyeti 2.500 TL girildiğinde ise, Y2 operasyonu kullanıldığında birim işçilik maliyeti 2.500 TL olacaktır. |
| İşçilik Maliyeti | Alternatif operasyon ile ilgili, standart birim işçilik maliyet tutarlarının girildiği alandır. Alana bir tutar girildiğinde, kapasite planlamada, ihtiyaç işçilik kapasitesi karşılığı gereken standart işçilik maliyeti hesaplanır. |
| Diğer Maliyetler | Alternatif operasyona ait yukarıda sayılan maliyetler dışında bir maliyet olduğunda, ilgili tutarın girildiği alandır. |
| Genel Maliyetler | Alternatif operasyona ait genel üretim maliyetlerinin girildiği alandır. Bu maliyetler, MRP modülünde yer alan "Kapasite Planlama Raporu" bölümünden görüntülenir. |
| Açıklama | Malzeme tanımı için açıklama girilen alandır. |
