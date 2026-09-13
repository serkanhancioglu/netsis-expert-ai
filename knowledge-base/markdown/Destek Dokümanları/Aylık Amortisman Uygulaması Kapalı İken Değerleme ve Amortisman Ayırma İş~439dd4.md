---
title: "Aylık Amortisman Uygulaması Kapalı İken Değerleme ve Amortisman Ayırma İşleminde Baz Yıl-Ay Kullanımı"
page_id: ""
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Aylık Amortisman Uygulaması Kapalı İken Değerleme ve Amortisman Ayırma İşleminde Baz Yıl-Ay Kullanımı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Aylık Amortisman Uygulaması Kapalı İken Değerleme ve Amortisman Ayırma İşleminde Baz Yıl-Ay Kullanımı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTRkNmRjNDc4LTkxYjktNDI1NS1iODMzLTkwNjFhODNkNDY2YyZsaW5rPTJmN2JjYjA2LWQ4YmEtNDRiYy1iYjQ1LTc0NjZkNjAzNWJlNCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=4d6dc478-91b9-4255-b833-9061a83d466c&link=2f7bcb06-d8ba-44bc-bb45-7466d6035be4&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "aylik-amortisman-uygulamasi-kapali-iken-degerleme-ve-amortisman-ayirma-isleminde-baz-yil-ay-kullanimi.html"
source_version: ""
source_bytes: 15270
fetched_at: "2026-09-13T04:22:03+00:00"
generator: "netsis-scraper 1.0.0"
---
# Aylık Amortisman Uygulaması Kapalı İken Değerleme ve Amortisman Ayırma İşleminde Baz Yıl-Ay Kullanımı

Demirbaş yeniden değerleme ile hayatımıza giren baz yıl-ay bilgisi, enflasyon düzeltme işleminde de büyük önem taşır.

Girilen baz yıl-ay bilgisi baz alınacak birikmiş amortisman tutarından, Değerleme ve Amortisman Raporunda izlenen birikmiş amortisman bilgisine kadar birçok hesaplamayı etkiler. Bu nedenle işlem anında doğru bilgi girişi yapmak önem taşır.

Baz yıl-ay alanına girilecek değer ENFDUZYILHARIC özel parametre kullanımına, aylık amortisman uygulaması parametresine, dönem bilgisine bağlı olarak değişkenlik gösterir.

Enflasyon düzeltmesinde, düzeltilecek birikmiş amortismanı bulmak için iki farklı yöntem bulunmaktadır. Birinci yöntemde, düzeltme yapılan aya kadar ayrılan amortismanlar, birikmiş amortismana dahil edilerek hesaplanan birikmiş amortisman enflasyon düzeltmesine tabi tutulur. Diğer yöntemde, mali dönem içinde ayrılan amortismanlar birikmiş amortismana dahil edilmez; mali dönem başındaki birikmiş amortisman yıl sonuna kadar taşınır ve geçmiş aya ait ayrılan amortismanların enflasyon farkları, enflasyon düzeltmesi yapılan ayın amortismanına eklenir(ENFDUZYILHARIC özel parametresi kullanımı

Aylık Amortisman Uygulaması parametresinin kapalı olduğu 2 farklı senaryo üzerinden baz yıl ay sahasının kullanıldığını inceleyelim.

**Senaryo 1 :** Demirbaş parametrelerinde dönem sayısı 4, Aylık Amortisman Uygulaması kapalı ve düzeltilecek birikmiş amortisman hesabına mali dönem içinde ayrılan amortismanların da dahil edilmesi istendiği için ENFDUZYILHARIC özel parametresi kullanılmamaktadır.

2023-12 tarihinde enflasyona başlama çalıştırılmıştır. Sadece çeyrek dönemlerde amortisman ayrılmaktadır. 2., 3. ve 4. çeyreklerde enflasyon düzeltmesi yapılacaktır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/2ee4ec02-e1b7-4ad1-a95d-e45f8203ed60/es_senaryo1parametregirisi.jpg)

Aylık amortisman uygulamasının kapalı olması halinde Değerleme Oran Girişinde amortisman ayırma yapılacak aylara ait satır bulunmalıdır. 3. Ayda bir taşıma olmayacağı için oran 0 geçilmiştir. 6-9-12.aylarda taşıma yapılacağı için Enf.Göre Oran Getir butonu ile oran indirilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/4f11a197-d6e7-439c-8234-66885678d450/es_donem_degerlemeoran.jpg)

2023 Aralık ayında enflasyona başlama, 2024 Mart ayında ise Değerleme ve Amortisman Ayırma işlemi 'Değerleme Yapılmayacaktır' seçeneği ile çalıştırılmıştır. Aylık amortisman uygulaması kapalı olduğu için amortisman bilgilerinde 2024 yılına ait yalnızca 3. ayda bir satır görünür ve bu satır 3 aylık toplam amortisman tutarını yansıtır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/f261129c-aa95-45f2-9002-1dd03c66ac0e/es_senaryo1amortismanbilgileri.jpg)

2024 Haziran ayında ise Değerleme ve Amortisman Ayırma işlemi ‘Enflasyon Düzeltmesi’ seçeneği ile çalıştırılır. Burada girilecek baz yıl/ay, amortisman ayırma işleminin gerçekleştiği son ay olacaktır. Senaryoda dönem amortisman uygulaması kullanıldığı için amortisman ayrılan son ay Mart'tır. Bu nedenle, ‘Yeniden Değerleme İşleminde Baz Alınacak Yıl/Ay’ alanına 2024/3 girilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/7d39ad56-7c00-44ef-b04e-cba83c7ac944/es_senaryo1amortayir.jpg)

Aynı mantıkla;

2024 Eylül ayında Değerleme ve Amortisman Ayırma işlemi ‘Enflasyon Düzeltmesi’ seçeneği ile çalıştırılır ve ‘Yeniden Değerleme İşleminde Baz Alınacak Yıl/Ay’ alanına 2024/6 girilir.

2024 Aralık ayında ise Değerleme ve Amortisman Ayırma işlemi ‘Enflasyon Düzeltmesi’ seçeneği ile çalıştırılır ve ‘Yeniden Değerleme İşleminde Baz Alınacak Yıl/Ay’ alanına 2024/9 girilir.

**Sonuç;**

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/0ef708e9-8fa4-408f-9092-8b8b7a01e47c/es_donem_s1_sonuc.jpg)

<u>6.ay düzeltilmiş sabit kıymet nasıl hesaplanır?</u>

Düzeltme katsayısı : 1,19493

Düzeltme öncesi sabit kıymet = 946.408,76

Düzeltilmiş sabit kıymet = 946.408,76\*1,19493=1.130.892,22

<u>6. ay düzeltilmiş birikmiş amortisman nasıl hesaplanır?</u>

ENFDUZYILHARIC özel parametresi tanımlı olmadığı ve dönem amortismanı kullanıldığı için, önceki dönemin birikmiş amortismanına, yine önceki dönemde hesaplanan toplam amortisman eklenerek düzeltilecek birikmiş amortisman bulunur. Senaryoda 6. ay düzeltmesi için önceki dönem 1. çeyrek olduğundan, Mart ayı satırında görünen birikmiş amortismana, aynı ayda görünen dönem amortismanı eklenerek düzeltilecek birikmiş amortismana ulaşılır.

2024 Mart ayı düzeltilmemiş birikmiş amortisman =189.281,75

Ocak + Şubat + Mart (1.dönem) ayrılan amortisman = 47320,44

Düzeltilecek birikmiş amortisman =189.281,75 + 47.320,44 = 236.602,19

Düzeltilmiş birikmiş amortisman = 236.602,19 \* 1,19493 = 282.723,05

Aynı mantıkla 9 ve 12.ay hesaplamaları yapılır.

<u>9. ay </u>

2024 Haziran ayı düzeltilmemiş birikmiş amortisman = 282.723,05

Nisan + Mayıs + Haziran (2.dönem) ayrılan amortisman = 56.544,61

Düzeltilmiş birikmiş amortisman (282.723,05 +56.544,61) \* 1,0507 = 356.468,53

<u>12.ay</u>

2024 Eylül ayı düzeltilmemiş birikmiş amortisman = 356.468,53

Temmuz + Ağustos + Eylül (3.dönem) ayrılan amortisman =59.411,42

Düzeltilmiş birikmiş amortisman (356.468,53+59.411,42) \* 1,02368=425.727,99

\*\*\*ENFDUZYILHARIC özel parametresinin tanımlı olmadığı bu senaryoda Aylık Amortisman uygulaması açık olsaydı, dönem sayısı ne olursa olsun baz yıl/ay hep bir önceki ay olarak verilecekti.

**Senaryo 2:** Demirbaş parametrelerinde dönem sayısı 4, Aylık Amortisman Uygulaması kapalı ve düzeltilecek birikmiş amortisman hesabına mali dönem içinde ayrılan amortismanların dahil edilmesi istenmediği için ENFDUZYILHARIC özel parametresi kullanılmaktadır.

2023-12 tarihinde enflasyona başlama çalıştırılmıştır. Sadece çeyrek dönemlerde amortisman ayrılmaktadır. 2., 3. ve 4. çeyreklerde enflasyon düzeltmesi yapılacaktır. Düzeltilecek birikmiş amortisman hesabına mali dönem içinde ayrılan amortismanların dahil edilmemesi istenmektedir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/2ee4ec02-e1b7-4ad1-a95d-e45f8203ed60/es_senaryo1parametregirisi.jpg)

Aylık amortisman uygulamasının kapalı olması halinde Değerleme Oran Girişinde amortisman ayırma yapılacak aylara ait satır bulunmalıdır. 3. Ayda bir taşıma olmayacağı için oran 0 geçilmiştir. 6-9-12.aylarda taşıma yapılacağı için Enf.Göre Oran butonu ile oran indirilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/4f11a197-d6e7-439c-8234-66885678d450/es_donem_degerlemeoran.jpg)

2023 Aralık ayında enflasyona başlama, 2024 Mart ayında ise Değerleme ve Amortisman Ayırma işlemi 'Değerleme Yapılmayacaktır' seçeneği ile çalıştırılmıştır. Aylık amortisman uygulaması kapalı olduğu için amortisman bilgilerinde 2024 yılına ait yalnızca 3. ayda bir satır görünür ve bu satır 3 aylık toplam amortisman tutarını yansıtır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/f261129c-aa95-45f2-9002-1dd03c66ac0e/es_senaryo1amortismanbilgileri.jpg)

2024 Haziran ayında, Değerleme ve Amortisman Ayırma işlemi ‘Enflasyon Düzeltmesi’ seçeneği ile çalıştırılır. Burada girilecek baz yıl/ay, en son 'Enflasyon Düzeltmesi' seçeneği ile değerleme ve amortisman ayırma işleminin yapıldığı ay olacaktır. Senaryoda, en son 2023 Aralık ayında enflasyon düzeltmesi yapılmış olup, sonrasında herhangi bir enflasyon düzeltmesi yapılmamıştır. Bu nedenle, 'Yeniden Değerleme İşleminde Baz Alınacak Yıl/Ay' alanına 2023/12 girilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/7eef4bd4-4487-4227-a50b-3736e7109652/es_senary2amortayir.jpg)

Aynı mantıkla;

2024 Eylül ayında Değerleme ve Amortisman Ayırma işlemi ‘Enflasyon Düzeltmesi’ seçeneği ile çalıştırılır ve ‘Yeniden Değerleme İşleminde Baz Alınacak Yıl/Ay’ alanına 2024/6 girilir.

2024 Aralık ayında ise Değerleme ve Amortisman Ayırma işlemi ‘Enflasyon Düzeltmesi’ seçeneği ile çalıştırılır ve ‘Yeniden Değerleme İşleminde Baz Alınacak Yıl/Ay’ alanına 2024/9 girilir.

**Sonuç;**

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/fdd192b8-6050-4a82-8374-3945ba440f03/es_donem_s2_sonuc.jpg)

<u>6.ay düzeltilmiş sabit kıymet nasıl hesaplanır?</u>

Düzeltme katsayısı : 1,19493

Düzeltme öncesi sabit kıymet = 946408,76

Düzeltilmiş sabit kıymet = 946408,76\*1,19493 = 1.130.892,22

```text
6. ay düzeltilmiş birikmiş amortisman nasıl hesaplanır?
ENFDUZYILHARIC özel parametresi tanımlı olduğu için,  en son enflasyon düzeltmesi yapılmış olan dönemin birikmiş amortismanı bir ekleme yapılmadan düzeltmeye tabi tutulur. Bu durumda düzeltilecek birikmiş amortisman 2023 Aralık ayı enflasyona başlama işlemi ile düzeltilmiş birikmiş amortismandır.
2023 Aralık ayı düzeltilmiş birikmiş amortisman = 189.281,75
Düzeltilmiş birikmiş amortisman                           = 189281,75* 1,19493 = 226.178,44
```

```text
6.ay aylık amortismanı nasıl hesaplanır?
ENFDUZYILHARIC özel parametresi tanımlı olduğu için, birikmiş amortisman, mali dönemde ayrılan amortisman dahil edilmeden düzeltilmiştir. Mali dönem içinde ayrılan amortismanların enflasyon farkı, ilgili dönem amortismanına yedirilir.
Aylık amortisman uygulaması kapalı olduğu için, 6. aya yani 2. çeyreğe, 1. çeyreğin enflasyon farkı yansıtılır. Bunun için öncelikle yeni sabit kıymet üzerinden yeni dönem amortismanına ulaşılır.
Yeni dönem amortismanı     = Eski dönem amortismanı * Katsayı
                                               = 47.320,44*1,19493
                                               = 56.544,61
1.Çeyrek farkı                        = 56.544,61-47.320,44=9.224,17
```

2.Çeyrek dönem amortismanı =Yeni dönem amortismanı + 1. Çeyrek farkı

2.Çeyrek dönem amortismanı = 56.544,61+ 9.224,17 = 65.768,79

```text
Aynı mantıkla 9 ve 12.ay hesaplamaları yapılır.
9. ay
Yeni dönem amortismanı     = Eski dönem amortismanı * Katsayı
                                               = 56.544,61*1,0507
                                               = 59.411,43
```

```text
1.+2.Çeyrek farkı                  = 59.411,43 -56.544,61=2.866,81* 2(önceki dönem sayısı) =5.733,62
```

3.Çeyrek dönem amortismanı =Yeni dönem amortismanı + geçmiş dönem farkları

3.Çeyrek dönem amortismanı = 59.411,43 + 5.733,62 = 65145,05

```text
12.ay
Yeni dönem amortismanı     = Eski dönem amortismanı * Katsayı
                                               = 59.411,43*1,02368
                                               = 60.818,29
1.+2.+3.Çeyrek farkı             = 60.818,29- 59.411,43 = 1.406,86 * 3(önceki dönem sayısı) = 4.220,59
4.Çeyrek, dönem amortismanı     =Yeni dönem amortismanı + geçmiş dönem farkları
4.Çeyrek, dönem amortismanı    = 60.818,29+ 4.220,59= 65.038,88
```
