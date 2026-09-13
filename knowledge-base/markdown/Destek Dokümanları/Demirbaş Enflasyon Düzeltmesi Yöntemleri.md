---
title: "Demirbaş Enflasyon Düzeltmesi Yöntemleri"
page_id: "150569236"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Demirbaş Enflasyon Düzeltmesi Yöntemleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Demirbaş Enflasyon Düzeltmesi Yöntemleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTIyMTU1ODg3LTBiNDgtNDVjZC05ZThjLTcyZTRhYjU2MDM4YSZsaW5rPTcxNjFkZDIyLWI4ZTgtNDA0MS05ZmEwLTA1MjJlNDEzOGU2ZiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=22155887-0b48-45cd-9e8c-72e4ab56038a&link=7161dd22-b8e8-4041-9fa0-0522e4138e6f&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "demirbas-enflasyon-duzeltmesi-yontemleri_150569236_150569236.html"
source_version: "2024-09-05T11:34:16.403+03:00"
source_bytes: 636552
fetched_at: "2026-09-13T04:22:38+00:00"
generator: "netsis-scraper 1.0.0"
---
# Demirbaş Enflasyon Düzeltmesi Yöntemleri

**2. Geçici Vergi Dönemi Demirbaş Enflasyon** **Düzeltmesi** **Yöntemleri**

lk geçici vergi döneminde enflasyon taşıması yapılmamasına karar verilmiş ve bu nedenle ikinci geçici vergi döneminde 6 aylık taşıma yapılması gereği doğmuştur.

Bu aşamada farklı görüşler ortaya çıkmış ve bu görüşlere uygun çalışma yöntemleri desteklenmiştir.

**Yöntem 1**

**Haziran** **ayı** **aylık** **amortisman** **tutarının** **düzeltilmemiş** **değerlerden** **oluşması, düzeltme** **farklarının** **muhasebe** **kayıtlarının** **oluşması** **ve** **Temmuz** **ayının** **düzeltilmiş** **değerlerden** **devam** **etmesi** **gerektiği**

Mevcut yapıda Haziran ayında yapılan enflasyon düzeltmesi işlemi sonucunda Haziran ayı aylık amortismanı düzeltilmiş değerlerden oluşur. Ancak farklı bir görüş olarak Haziran ayı amortismanının düzeltilmemiş değerlerden ayrılması, düzeltme farklarının sadece muhasebesel olarak işlenmesi gerektiği belirtilmiştir. Bu yapının Netsis Demirbaş uygulamasında çalışması için;

1-Haziran ayı için Değerleme ve Amortisman Ayırma İşlemi Değerleme Durumu "Değerleme Yapılmayacaktır" seçilerek çalıştırılır. Bu aşamada program düzeltilmemiş değerlerden Haziran amortismanını ayırır.

![](../_assets/b33c45de40a180f95a14.png)
![](../_assets/32d8ffb24874c38272d1.png)

2-Enflasyona Başlama işlemi Haziran ayı için "Rapor Amaçlı" seçeneği işaretlenerek çalıştırılır.

![](../_assets/508b9062cf6aa6902faf.png)

Bu aşamada program Haziran sonu değerleri üzerinden düzeltilmiş değerleri hesaplar ve TBLAMORTISMANDEV tablosuna yazar.

![](../_assets/4b14a42f7605c3f8df8e.png)

Düzeltilmiş sabit kıymet = 7.537,09\*1,19493=9.006,29

Düzeltilmiş birikmiş amortisman = (3.014,84+753,71)\*1,19493=4.503,17

\*\*Düzeltilecek birikmiş amortisman önceki dönem sonu amortismanına yıl içine ayrılan amortismanlar dahil edilerek bulunur.

3-Temelset ile entegrasyon mevcutsa Amortisman Hisse Muhasebeleştirme işlemi çalıştırılır. Program bu aşamada sabit kıymet, birikmiş amortisman ve aylık amortisman farklarını detay kodu ve masraf kodu ekranlarında tanımlanmış olan enflasyon hesaplarına aktarır.

Birikmiş amortisman farkı : 4503,17 – 3768,55 = 734,61

Sabit kıymet farkı: 9006,29 – 7537,09 = 1469,2
![](../_assets/d40aaac2477d304b603f.png)

**Yöntem 2**

**Düzeltmeye tabi birikmiş** **amortismanı** **bulurken** **dönem** **içinde** **ayrılan** **amortismanların** **birikmiş** **amortismana** **dahil** **edilmeyip, dönem** **farkının** **gider** **olarak** **işlenmesi** **gerektiği**

Mevcut yapıda düzeltmeye tabi birikmiş amortisman bulunurken 2023/12 düzeltilmiş birikmiş amortisman tutarına 2024 yılının ilk 5 ayında ayrılan amortisman eklenir. Eğer düzeltmeye tabi birikmiş amortisman hesabına dönem içinde ayrılan amortismanlar dahil edilmesin ve 5 ayın farkı Haziran ayına gider olarak işlensin isteniyor ise;

1. DEMIRBAS/ENFDUZYILHARIC özel parametresi tanımlanır.
2. Haziran ayı için Değerleme ve Amortisman Ayırma işlemi Yeniden Değerlemede Baz Alınacak Yıl/Ay bilgisine 2023/12 girilerek çalıştırılır.

![](../_assets/bf0617fd850ddf1aa80b.png)

İşlem anında baz yıl/ay 2023/12 girildiği için 2023/12 düzeltilmiş birikmiş tutarı olan 27.694,00 üzerinden düzeltme yapılır. Ilk 5 ay bu tutara dahil edilmez.

\*\*2024-9 . ayda yapılacak düzeltmede baz yıl/ay 2024/6 girilecektir.

![](../_assets/43ebbcad1d3d0dbca214.png)

Düzeltilmiş sabit kıymet : 138.470,00 \* 1,19493 = 165.461,96

Düzeltilmiş birikmiş amortisman : 27.694,00 \* 1,19493 = 33.092,39

Yeni dönem amortismanı: 165.461,96 \* 0,20 /12 = 2757,70

5 aylık geçmiş ay amortisman farkı : (2757,7 – 2.307,83)\*5 : 2249,35

Haziran aylık amortismanda görünen tutar : 2757,7 + 2249,35 : 5007,05

**Yöntem 3**

**Düzeltmeye tabi birikmiş** **amortismanı** **bulurken** **dönem** **içinde** **ayrılan** **amortismanların** **birikmiş** **amortismana** **dahil** **edilmesi** **gerektiği**

Mevcut yapıda düzeltmeye tabi birikmiş amortisman bulunurken 2023/12 düzeltilmiş birikmiş amortisman tutarına 2024 yılının ilk 5 ayında ayrılan amortisman eklenir.

1. Haziran ayı için Değerleme ve Amortisman Ayırma işlemi Yeniden Değerlemede Baz Alınacak Yıl/Ay bilgisine 2024/5(değerleme yapılan aydan bir önceki ay) girilir.

![](../_assets/f3d0e9e982d7885f376e.png)

İşlem anında baz yıl/ay 2024/5 girildiği için Mayıs dahil birikmiş amortisman düzeltmeye tabi tutulur. 2024 yılında ayrılan amortismanlar birikmiş amortismanın içerisinde düzeltildiği için ayrıca bir fark atılmaz.

![](../_assets/350140f7c5fc79ba5bee.png)

Düzeltilmiş sabit kıymet : 138.470,00 \* 1,19493 = 165.461,96

Düzeltilmiş birikmiş amortisman : (2023 sonu birikmiş amortismanı + 5 aylık toplam amortisman) \* 1,19493

Düzeltilmiş birikmiş amortisman : (27.694,00+11.539,15) \* 1,19493 = 46.880,87

Haziran amortismanı: 165.461,96 \* 0,20 /12 = 2757,70
