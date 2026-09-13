---
title: "Aylık Amortisman Uygulaması Açık İken Değerleme ve Amortisman Ayırma İşleminde Baz Yıl-Ay Kullanımı"
page_id: ""
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Aylık Amortisman Uygulaması Açık İken Değerleme ve Amortisman Ayırma İşleminde Baz Yıl-Ay Kullanımı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Aylık Amortisman Uygulaması Açık İken Değerleme ve Amortisman Ayırma İşleminde Baz Yıl-Ay Kullanımı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTI4NmFkOGQ4LTE1MzAtNGI5Zi1hNzk0LTRlMTIzNzg5Njg4YyZsaW5rPWFhNTJlOTMxLWEwOTEtNDk2OC1hMjg0LWViZDA4YzI1NmQ4NyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=286ad8d8-1530-4b9f-a794-4e123789688c&link=aa52e931-a091-4968-a284-ebd08c256d87&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "aylik-amortisman-uygulamasi-acik-iken-degerleme-ve-amortisman-ayirma-isleminde-baz-yil-ay-kullanimi.html"
source_version: ""
source_bytes: 12800
fetched_at: "2026-09-13T04:22:02+00:00"
generator: "netsis-scraper 1.0.0"
---
# Aylık Amortisman Uygulaması Açık İken Değerleme ve Amortisman Ayırma İşleminde Baz Yıl-Ay Kullanımı

Demirbaş yeniden değerleme ile hayatımıza giren baz yıl-ay bilgisi, enflasyon düzeltme işleminde de büyük önem taşır.

Girilen baz yıl-ay bilgisi baz alınacak birikmiş amortisman tutarından, Değerleme ve Amortisman Raporunda izlenen birikmiş amortisman bilgisine kadar birçok hesaplamayı etkiler. Bu nedenle işlem anında doğru bilgi girişi yapmak önem taşır.

Baz yıl-ay alanına girilecek değer ENFDUZYILHARIC özel parametre kullanımına, aylık amortisman uygulaması parametresine, dönem bilgisine bağlı olarak değişkenlik gösterir.

Enflasyon düzeltmesinde, düzeltilecek birikmiş amortismanı bulmak için iki farklı yöntem bulunmaktadır. Birinci yöntemde, düzeltme yapılan aya kadar ayrılan amortismanlar, birikmiş amortismana dahil edilerek hesaplanan birikmiş amortisman enflasyon düzeltmesine tabi tutulur. Diğer yöntemde, mali dönem içinde ayrılan amortismanlar birikmiş amortismana dahil edilmez; mali dönem başındaki birikmiş amortisman yıl sonuna kadar taşınır ve geçmiş aya ait ayrılan amortismanların enflasyon farkları, enflasyon düzeltmesi yapılan ayın amortismanına eklenir(ENFDUZYILHARIC özel parametresi kullanımı).

Aylık Amortisman Uygulaması parametresinin açık olduğu 2 farklı senaryo üzerinden baz yıl ay sahasının nasıl kullanıldığını inceleyelim.

**Senaryo 1 :** Demirbaş parametrelerinde dönem sayısı 12, Aylık Amortisman Uygulaması açık ve düzeltilecek birikmiş amortisman hesabına mali dönem içinde ayrılan amortismanların da dahil edilmesi istendiği için ENFDUZYILHARIC özel parametresi kullanılmamaktadır.

2023-12 tarihinde enflasyona başlama çalıştırılmıştır. Her ay amortisman ayrılmaktadır.6,9 ve 12. aylarda enflasyon düzeltmesi yapılacaktır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/7d0c60d8-e9d4-4805-be28-af3a59d088fd/es_aylik_parametre.jpg)

Aylık amortisman uygulaması açık olduğunda, Değerleme Oran Girişinde yalnızca enflasyon düzeltmesi yapılacak aylar için 'Enf. Göre Oran Getir' butonu ile oran indirme işlemi yapılır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/87a5753b-f059-40ea-a68a-ab4bb8e8cd01/es_aylik_degerlemeoran.jpg)

2023 Aralık ayında enflasyona başlama işlemi yapılmış, ilk 5 ay için ise Değerleme ve Amortisman Ayırma işlemi 'Değerleme Yapılmayacaktır' seçeneği ile çalıştırılmıştır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/2b56661b-b504-48d4-aa19-c60a1154f88a/es_aylik_amortismanbil.jpg)

2024 Haziran ayında Değerleme ve Amortisman Ayırma işlemi ‘Enflasyon Düzeltmesi’ seçeneği ile çalıştırılır. Burada girilecek baz yıl/ay, amortisman ayırma işleminin gerçekleştiği son ay olacaktır. Senaryoda aylık amortisman uygulaması kullanıldığı için amortisman ayrılan son ay Haziran’dır. Bu nedenle, ‘Yeniden Değerleme İşleminde Baz Alınacak Yıl/Ay’ alanına 2024/5 girilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/20074f39-2b31-443d-b5df-1c1fc01aba2b/es_aylik_s1_amortayir.jpg)

Aynı mantıkla;

2024 Eylül ayında Değerleme ve Amortisman Ayırma işlemi ‘Enflasyon Düzeltmesi’ seçeneği ile çalıştırılır ve ‘Yeniden Değerleme İşleminde Baz Alınacak Yıl/Ay’ alanına 2024/8 girilir.

2024 Aralık ayında ise Değerleme ve Amortisman Ayırma işlemi ‘Enflasyon Düzeltmesi’ seçeneği ile çalıştırılır ve ‘Yeniden Değerleme İşleminde Baz Alınacak Yıl/Ay’ alanına 2024/11 girilir.

\*\*Diğer aylar ‘Değerleme Yapılmayacaktır’ seçeneği ile çalıştırılmalıdır.

**Sonuç**

**![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/34427619-9da0-42f4-a426-b2c4445c526a/es_aylik_s1_sonuc.jpg)**

6.ay düzeltilmiş sabit kıymet nasıl hesaplanır?

Düzeltme katsayısı : 1,19493

Düzeltme öncesi sabit kıymet = 946.408,76

Düzeltilmiş sabit kıymet = 946.408,76\*1,19493=1.130.892,22

\6. ay düzeltilmiş birikmiş amortisman nasıl hesaplanır?

ENFDUZYILHARIC özel parametresi tanımlı olmadığı ve aylık amortisman uygulaması kullanıldığı için, düzeltilecek birikmiş amortisman, düzeltme yapılan aya kadar ayrılmış olan toplam amortismandır. 2024 5. Ay satırında gördüğümüz birikmiş amortismana, yine aynı satırdaki eklenen amortisman tutarını ya da 5 aylık toplam amortismanı ekleyerek düzeltilecek birikmiş amortismana ulaşırız.

2024 Mayıs ayı birikmiş amortisman =189.281,75

Ocak + Şubat + Mart +Nisan + Mayıs ayrılan amortisman = 78.867,40

Düzeltilecek birikmiş amortisman =189.281,75 + 78.867,40 = 268.149,15

Düzeltilmiş birikmiş amortisman = 268.149,15\* 1,19493 = 320.419,46

Aynı mantıkla 9 ve 12.ay hesaplamaları yapılır.

9. ay

2024 Ağustos ayı birikmiş amortisman = 320.419,46

Haziran + Temmuz + Ağustos ayı ayrılan amortisman = 56.544,61

Düzeltilmiş birikmiş amortisman (320.419,46+56.544,61) \* 1,0507 = 396.076,14

12.ay

2024 Kasım ayı birikmiş amortisman = 396.076,14

Eylül + Ekim + Kasım ayı ayrılan amortisman =59.411,42

Düzeltilmiş birikmiş amortisman (396.076,14+59.411,42) \* 1,02368=466.273,52

\*\*\*ENFDUZYILHARIC özel parametresinin tanımlı olmadığı bu senaryoda Aylık Amortisman uygulaması kapalı olsaydı, baz yıl/ay amortisman ayrılan son dönem olarak verilecekti.

**Senaryo 2:** Demirbaş parametrelerinde dönem sayısı 12, Aylık Amortisman Uygulaması açıktır.Düzeltilecek birikmiş amortisman hesabına mali dönem içinde ayrılan amortismanların dahil edilmemesi istendiği için ENFDUZYILHARIC özel parametresi kullanılmaktadır.

2023-12 tarihinde enflasyona başlama çalıştırılmıştır. Her ay amortisman ayrılmaktadır.6,9 ve 12. aylarda enflasyon düzeltmesi yapılacaktır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/7d0c60d8-e9d4-4805-be28-af3a59d088fd/es_aylik_parametre.jpg)

Aylık amortisman uygulaması açık olduğunda, Değerleme Oran Girişinde yalnızca enflasyon düzeltmesi yapılacak aylar için 'Enf. Göre Oran Getir' butonu ile oran indirme işlemi yapılır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/87a5753b-f059-40ea-a68a-ab4bb8e8cd01/es_aylik_degerlemeoran.jpg)

2023 Aralık ayında enflasyona başlama işlemi yapılmış, ilk 5 ay için ise Değerleme ve Amortisman Ayırma işlemi 'Değerleme Yapılmayacaktır' seçeneği ile çalıştırılmıştır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/2b56661b-b504-48d4-aa19-c60a1154f88a/es_aylik_amortismanbil.jpg)

2024 Haziran ayında Değerleme ve Amortisman Ayırma işlemi ‘Enflasyon Düzeltmesi’ seçeneği ile çalıştırılır. Burada girilecek baz yıl/ay, enflasyon düzeltmesi işleminin gerçekleştirildiği son ay olacaktır. Senaryoda, Haziran öncesinde enflasyon düzeltmesi yapılan son ay 2023 Aralık ayı olduğu için, ‘Yeniden Değerleme İşleminde Baz Alınacak Yıl/Ay’ alanına 2023/12 girilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/4b34ae66-c796-4860-a4eb-ab76ee50ae10/es_aylik_s2_amortayir.jpg)

Aynı mantıkla;

2024 Eylül ayında Değerleme ve Amortisman Ayırma işlemi ‘Enflasyon Düzeltmesi’ seçeneği ile çalıştırılır ve ‘Yeniden Değerleme İşleminde Baz Alınacak Yıl/Ay’ alanına 2024/6 girilir.

2024 Aralık ayında ise Değerleme ve Amortisman Ayırma işlemi ‘Enflasyon Düzeltmesi’ seçeneği ile çalıştırılır ve ‘Yeniden Değerleme İşleminde Baz Alınacak Yıl/Ay’ alanına 2024/9 girilir.

**Sonuç;**

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/0a53f2fd-8b4c-44a6-bddf-bc5822d4519e/es_aylik_s2_sonuc.jpg)

6.ay düzeltilmiş sabit kıymet nasıl hesaplanır?

Düzeltme katsayısı : 1,19493

Düzeltme öncesi sabit kıymet = 946408,76

Düzeltilmiş sabit kıymet = 946408,76\*1,19493 = 1.130.892,22

\6. ay düzeltilmiş birikmiş amortisman nasıl hesaplanır?

ENFDUZYILHARIC özel parametresi tanımlı olduğu için, en son enflasyon düzeltmesi yapılmış olan dönemin birikmiş amortismanı

bir ekleme yapılmadan düzeltmeye tabi tutulur. Bu durumda düzeltilecek birikmiş amortisman 2023 Aralık ayı enflasyona başlama

işlemi ile oluşan düzeltilmiş birikmiş amortismandır.

2023 Aralık ayı düzeltilmiş birikmiş amortisman = 189.281,75

Düzeltilmiş birikmiş amortisman = 189281,75\* 1,19493 = 226.178,44

6.ay aylık amortismanı nasıl hesaplanır?

ENFDUZYILHARIC özel parametresi tanımlı olduğu için, birikmiş amortisman, mali dönemde ayrılan amortisman dahil edilmeden

düzeltilmiştir. Mali dönem içinde ayrılan amortismanların enflasyon farkı, düzeltme yapılan ayın amortismanına yedirilir.

Aylık amortisman uygulaması açık olduğu için, 6. aya , ilk 5 ayın enflasyon farkı yansıtılır.

Yeni ay amortismanı = Eski ay amortismanı \* Katsayı

= 15.773,48\*1,19493

= 18.848,20

İlk 5 ay için enflasyon farkı = (18.848,20 - 15.773,48)\*5 = 15.373,62

6. ay amortismanı =Yeni ay amortismanı + ilk 5 ay farkı

6. ay amortismanı = 18.848,20 + 15.373,62 = 34.221,82

Aynı mantıkla 9 ve 12.ay hesaplamaları yapılır.

9. ay

Yeni ay amortismanı = Eski ay amortismanı \* Katsayı

= 18.848,20\*1,0507

= 19.803,81

İlk 8 ay için enflasyon farkı = (19.803,81 – 18.848,20) \* 8 = 7.644,83

9. ay amortismanı = Yeni ay amortismanı + ilk 8 ay farkı

9. ay amortismanı = 19.803,81+ 7.644,83 = 27.448,64

12.ay

Yeni ay amortismanı = Eski ay amortismanı \* Katsayı

= 19.803,81\* 1,02368

= 20.272,76

İlk 11 ay farkı = (20.272,76 - 19.803,81) \* 11 = 5.158,51

12. ay amortismanı = Yeni ay amortismanı + ilk 11 ay farkı

12. ay amortismanı = 20.272,76 + 5.158,51 = 25431,28

İki senaryoda da mali dönem sonunda toplam amortisman ve sabit kıymet aynı sonucu verir. Bu iki senaryoyu birbirinden ayıran şey yıl içinde ayrılan amortismana ait enflasyon farkının nereye işleneceğidir. İlk senaryoda yıl içerisinde ayrılan amortisman birikmiş amortismana dahil edilip, birikmiş amortisman içerisinde düzeltilirken, ikinci senaryoda yıl içerisinde ayrılan amortismanın enflasyon farkı aylık amortismana eklenerek giderleştirilir.
