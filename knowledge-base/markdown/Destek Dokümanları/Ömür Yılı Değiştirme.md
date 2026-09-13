---
title: "Ömür Yılı Değiştirme"
page_id: ""
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Ömür Yılı Değiştirme"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Ömür Yılı Değiştirme"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTU1ZDFhOWQ3LTgxYmUtNDg2ZC1iYzA3LWVkY2QyNmMyZmY4ZiZsaW5rPTBiNjg3MzMzLWZkODQtNDZlZi1iNDhkLTM4YTI2OWVhMGMyYiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=55d1a9d7-81be-486d-bc07-edcd26c2ff8f&link=0b687333-fd84-46ef-b48d-38a269ea0c2b&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "omur-yili-degistirme.html"
source_version: ""
source_bytes: 5609
fetched_at: "2026-09-13T04:22:11+00:00"
generator: "netsis-scraper 1.0.0"
---
# Ömür Yılı Değiştirme

**Faydalı Ömür Yılı Nedir?**

Mükelleflerin kullanmakta oldukları iktisadi kıymetlerin kullanım sürelerinin belirli sınırlar dâhilinde olması kaydıyla, kullanım ömürlerinin mükellefler tarafından belirlenmesinin önünü açan amortisman süresinin belirlenmesine yönelik bir uygulamadır. Mükellef tarafından belirlenen faydalı ömür süresi izleyen dönemde değiştirilemez.

Ancak, beyan edilenden farklı olarak sehven girilmiş amortisman oranı ya da faydalı ömür yılı içerisinde hızlı amortisman yönteminden normal amortisman yöntemine geçme gereksinimi, kalan amortismanın kalan ömür yılına yeniden pay edilmesini gerektirir.

Beklenti, kalan amortisman bedelinin kalan amortisman süresine eşit pay edilmesidir.

Kalan amortismanın kalan amortisman süresine yeniden pay edilmesinin gerektiği tüm durumlar için **Demirbaş Ömür Yılı Değiştirme** işlemi kullanılır.

**Demirbaş Ömür Yılı Değiştirme Nasıl Yapılır?**

Demirbaş Ömür Yılı Değiştirme, Demirbaş Bilgi Kartında bulunan **Yeni Ömür Yılı** ve **Tarih** alanlarına müdahale edilerek sağlanır.

Bunu 2 örnek üzerinden açıklayalım:

**Senaryo-1**

Alındığı yıl amortisman oranı 20 girilmesi gerekirken 2,5 girilmiş ve ilk yıl bu şekilde amortisman ayrılmış bir iktisadi kıymet için kalan amortismanın, kalan ömür yılına eşit olarak pay edilmesi istenmektedir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/42cebbda-f937-4b0a-a75a-32a505e9a62e/ES_Omuryilidegistirme_1.jpg)

Senaryoda belirtildiği gibi, iktisadi kıymetin amortisman oranı sehven 2,5 olarak tanımlanmış ve bu nedenle faydalı ömür yılı 40 yıl olarak hesaplanmıştır.

2023 yılında ayrılan toplam amortisman = 4.463,58

Yapılacak düzenleme:

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/ec9b98ec-fc73-41c8-8453-350f98d6a158/ES_Omuryilidegistir_2.jpg)

Senaryoda doğru oran 20 olduğu için 100/20 üzerinden faydalı ömür yılı 5 olarak hesaplanır. Bu nedenle **Yeni Ömür Yılı** alanına 5, 01.01.2024 tarihinden itibaren düzenleme geçerli olduğu için **Tarih** alanına 01.01.2024 girilir.

Bu bilgiler kaydedildiğinde iktisadi kıymet kartındaki amortisman bitiş yılı, program tarafından 2027-12 olacak şekilde güncellenir. Ve kalan amortisman, kalan ömür yılı olan 4 yıla eşit olarak bölünür.

Hesaplamalar aşağıdaki gibidir:

İktisadi kıymet bedeli = 178.543,23

2023 yılı ayrılan toplam amortisman = 4.463,58

Kalan Amortisman = 178.543,23 – 4.463,58 = 174.079,65

Yeni ömür yılına göre yıllık amortisman = 174.079,65 / 4 = 43.519,91

Aylık amortisman = 43.519,91 / 12 = 3.626,66

**Senaryo-2**

Alındığı yıl hızlı amortisman yöntemi ile amortisman ayrılan bir iktisadi kıymet için normal amortisman yöntemine geçilmek istenmektedir.

Vergi Usul Kanunu, sadece hızlı amortismandan normal amortisman yöntemine geçilmesine izin verir ve bunu da mali yıl ortasında değil, sadece mali yıl başında mümkün kılar.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/9e92041c-3a58-46d7-80fb-35da2bef9ed2/ES_Omuryilidegistirme_3.jpg)

Senaryoda belirtildiği gibi, iktisadi kıymetin amortisman tipi **Hızlı** olarak belirlenmiş ve 2024 yılı bu yöntem ile amortisman ayrılmıştır.

2024 yılında ayrılan toplam amortisman = 400.000

Yapılacak düzenleme:

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/ec8cb474-7bf5-47d4-a35e-7053da91f9b1/ES_Omuryilidegistirme_4.jpg)

Senaryoda oran değil, yöntem değişikliği olduğu için faydalı ömür yılında bir değişiklik olmaz. Bu nedenle **Yeni Ömür Yılı** alanına 5, 01.01.2025 tarihinden itibaren düzenleme geçerli olduğu için **Tarih** alanına 01.01.2025 girilir.

Bu bilgiler kaydedildiğinde, iktisadi kıymetin kalan amortismanı, kalan ömür yılı olan 4 yıla eşit olarak bölünür.

Hesaplamalar aşağıdaki gibidir:

İktisadi kıymet bedeli = 1.000.000

2023-4 yılı ayrılan toplam amortisman = 400.000

Kalan Amortisman = 1.000.000 – 400.000 = 600.000

Yeni ömür yılına göre yıllık amortisman = 600.000 / 4 = 150.000

Aylık amortisman = 150.000 / 12 = 12.500
