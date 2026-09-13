---
title: "Düzeltilecek Stok Hesapları"
page_id: "140247961"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Düzeltilecek Stok Hesapları"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Düzeltilecek Stok Hesapları"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTYzYjE2ODRhLTNkNWItNDE2OC04OTA3LTQ1Njk3OGE2Y2JmZCZsaW5rPTE1ODlhYmI0LWVmMzUtNDU4ZS1iOTNlLTExY2QxZmE2MGJhZiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=63b1684a-3d5b-4168-8907-456978a6cbfd&link=1589abb4-ef35-458e-b93e-11cd1fa60baf&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "duzeltilecek-stok-hesaplari_140247974_140247961.html"
source_version: "2024-05-14T10:18:18.777+03:00"
source_bytes: 484956
fetched_at: "2026-09-13T04:22:51+00:00"
generator: "netsis-scraper 1.0.0"
---
# Düzeltilecek Stok Hesapları

**Stokların** **Enflasyon** **Düzeltmesine Tabi Tutulmasına** **İlişkin** **Yöntemler**

Enflasyon düzeltmesinde esas yöntem düzeltme katsayısının hesaplanıp(gerçek yöntem), ilgili katsayısının düzeltmeye konu olacak bilanço kalemine uygulanması suretiyle düzeltme işleminin tamamlanmasıdır. Ancak tebliğde stoklara ilişkin düzeltmede toplulaştırılmış yöntemin kullanılmasını mükelleflerin tercihine bırakılmıştır.

Yöntem tercihleri hesap bazında Düzeltilecek Stok Hesapları ekranından tanımlanır.

Seçilen hesap için Yöntem seçimli alanınından kullanılacak yöntem belirlenir. Yöntem Stok Devir Hızı seçildiğinde Oran ve Durma günleri doldurulmalıdır.

![](../_assets/ea3fa0417414ad9d45ba.png)

**Basit Ortalama** **Yöntemi**

Basit ortalama yönteminde düzeltme katsayısı, mali tabloların ait olduğu aya ilişkin fiyat endeksinin, bu endeks ile bir önceki geçici vergi döneminin sonundaki fiyat endeksi toplamının ikiye bölünmesi sonucu bulunan endekse bölünmesiyle elde edilen katsayı olarak hesaplanır.

Bilançonun ait olduğu aya ait Yİ-ÜFE

Dönem Ortalama Düzeltme Katsayısı= ----------------------------------------------------------------------------------------------------------------------------------------------------------

(Bilançonun ait olduğu aya ait Yİ-ÜFE + Bilanço günü itibarıyla bir önceki geçici vergi döneminin sonundaki Yİ-ÜFE) / 2

Basit ortalama için Stok Hesapları Düzeltme işlemi "Dönem Son Ay İçin Düzeltme" parametresi işaretlenerek çalıştırılır. Stok devir hızı ay ay çalıştırılırken, basit ortalama sadece dönem sonralarında ve "Dönem Son Ay İçin Düzeltme" parametresi işaretlenerek çalıştırılmalıdır.

Program Yöntem seçimi Basit Ortalama olan hesaplara sadece bu parametrenin işaretlendiği aylarda düzeltme kaydı atar.

Örnek: 31/12/2023 tarihi itibariyle 153-01-002 hesabın bakiyesi 600.000TL'dir. İşletme ilgili hesabın enflasyon düzeltmesini gerçekleştirirken toplulaştırılmış yöntemlerden basit ortalama yöntemi seçmiştir.

![](../_assets/42aefe2655a93c9a5caa.png) ![](../_assets/afacde9f0203a7864250.png)

Aralık 2023 Yİ-ÜFE = 2.915,02

Eylül 2023 Yİ-ÜFE=2.749,98

Dönem Ortalama Düzeltme Katsayısı =2.915,02/ ((2.915,02+2.749,98) / 2) =1,02913

Enflasyon Farkı= 600.000,00-TL x 0,02913 =17.479,96-TL

İşlem sonucunda Mahsup tipli ve Açıklama 1 alanı "TOPLULAŞTIRILMIŞ YÖNTEM ENFLASYON DÜZELTMELERİ" olan yevmiye fişi oluşur. 153-01-002 hesabın kartında tanımlanmış olan enflasyon fark hesabı ile muhasebe parametrelerinde tanımlanmış olan enflasyon düzeltme hesabı karşılıklı olarak çalışır.

![](../_assets/a25cec0ffb7f8fc1df2a.png)
![](../_assets/0a4857666a5961bc5738.png)

**Stok Devir** **Hızı** **Yöntemi**

Stok devir hızı yönteminde düzeltme katsayısı mali tabloların ait olduğu aya ilişkin fiyat endeksinin,stok hesabı bazında belirlenen durma gününe göre geriye giderek tespit edilen aya ilişkin fiyat endeksine bölünmesi sonucu elde edilen katsayı olarak hesaplanır.

Bu aşamada öncelikli olan hesap bazında durma günlerini belirlemek olacaktır.

Ticari mal, yarı mamul ve mamuller ile ilgili girişleri bir örnek üzerinden detaylandıralım.

İlk madde malzeme

Hammadde ortalama durma günü 60 ise tablo aşağıdaki şekilde doldurulur.

![](../_assets/d155a02b23fa735bc16d.png)

Yarı Mamul

Yarı mamul mamul haline gelinceye kadar stokta bekleme süresi 30 gün, yarı mamul maliyetinde ilk madde malzeme oranı %70, işçilik, amortisman ve genel üretim giderleri payları %10'ar ise tablo aşağıdaki gibi doldurulur.

![](../_assets/ac0866642417aa277e33.png)

İlk madde malzeme durma günü 90 = İlk madde malzeme durma günü + yarı mamul durma günü olarak verilir(Önceki ekran görselinde ilk maddenin durma günü 60 olarak belirtilmiştir).İlk madde malzeme dışındaki diğer giderler (işçilik ve genel üretim giderleri gibi) yarı mamul aktifleştiğinde yarı mamule girdiği için bu kalemlerin durma günü yarı mamulün stokta bekleme süresi kadar olur. İlk madde malzeme ise, yarı mamul haline gelmeden önce ve yarı mamul olarak stokta beklemiştir. Bu nedenle iki süre toplanarak belirtilir. Amortisman giderleri için durma günü sorgulanmaz. Çünkü amortisman gideri, eğer tarihi değerlerle yarı mamule girmişse, belli bir katsayı ile (düzeltilmiş toplam amortisman / tarihi toplam amortisman) çarpılarak düzeltilir. Eğer düzeltilmiş değerlerle yarı mamule girmişse, olduğu gibi alınır.

Mamul

Mamulümüzün sevk edilinceye kadar stokta bekleme süresi 30 gün, mamul maliyetinde ilk madde malzeme oranı %70, işçilik, amortisman ve genel üretim giderleri payları %10'ar ise tablo aşağıdaki gibi doldurulur.

![](../_assets/f6d10ef9fb905597c2a4.png)

İlk madde malzeme durma günü 120 = İlk madde malzeme durma günü + yarı mamul durma günü + mamul durma günü olarak verilmiştir. Hesabın içinde bulunan her bir kalem için öncelikle hesabın TL bakiyesi bulunacak ve verilen oranlar uygulanarak her kalemin TL tutardan aldığı pay hesaplanacaktır. Sonra her kalemin bulunan TL payı, verilen durma gününe göre endekslenerek her kalem için ayrı ayrı düzeltilmiş tutarlar hesaplanacaktır. Bu düzeltilmiş değerlerin toplamı ise, hesabın sonuç düzeltilmiş değerini verir. Ancak hesabın amortisman kaleminin TL payı çıkarılır, bu hesabın amortisman payının düzeltilmiş amortisman tutarından alacağı pay hesaplanarak eklenir

**Not:** Durma günü \< 30 ise düzeltme yapılmaz Durma günü \>=30 ve Durma günü \<60 ise bir aylık endeksle Durma günü \>=60 ve Durma günü \<90 ise iki aylık endeksle vb. endekslenir.

**Örnek;**

2023 Aralık sonu bakiyesi 100.000-TL olan bir stok hesabı için tablodaki tanım yapılmıştır. 2023.12 düzeltilmiş tutar nasıl hesaplanır?

![](../_assets/b7e1b1ef0c7ff891ce6b.png)

Tabloda, hesap bakiyesinin %70'lik ilk madde malzeme durma günü + yarı mamul durma günü + mamul durma günü olan 90 gün, %10'luk işçilik giderlerlerinin ise 30 gün öncesine ait endeks ile düzeltileceği belirtilmiştir.

Stok Hesapları Düzeltme işlemi 12. Ay için çalıştırılır.

![](../_assets/5a25e660a7b305e7fb35.png)

Bu durumda hesaplamalar aşağıdak şekilde olacaktır.

![](../_assets/18b19699a8e0338bd12d.png)

![](../_assets/6c8311da620a72e13cdb.png)
