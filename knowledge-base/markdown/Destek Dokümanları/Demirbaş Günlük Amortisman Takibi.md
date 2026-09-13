---
title: "Demirbaş Günlük Amortisman Takibi"
page_id: "108659224"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Demirbaş Günlük Amortisman Takibi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Demirbaş Günlük Amortisman Takibi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTA3MzM4MTg5LTJiMTctNDUzMi1hZTFiLWU5ODgxNGRmN2ViMCZsaW5rPTM1OWIyN2Y2LTRiMmMtNDkzYy05ZDY5LTI2OGMyZWJiNjM2MyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=07338189-2b17-4532-ae1b-e98814df7eb0&link=359b27f6-4b2c-493c-9d69-268c2ebb6363&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "demirbas-gunluk-amortisman-takibi_108659230_108659224.html"
source_version: "2023-03-31T09:23:04.130+03:00"
source_bytes: 616529
fetched_at: "2026-09-13T04:23:31+00:00"
generator: "netsis-scraper 1.0.0"
---
# Demirbaş Günlük Amortisman Takibi

7338 Sayılı Vergi Usul Kanunu 34 üncü Madde Kapsamında Günlük Esasa Göre Amortisman Takibi hakkında ayrıntılı bilgiye bu dokümandan ulaşılır.

Amortisman süresi, iktisadi kıymetlerin aktife girdikleri hesap döneminden itibaren başlamakta ve iktisadi kıymetler Hazine ve Maliye Bakanlığınca tespit ve ilan edilen faydalı ömürlerine göre amortismana tabi tutulmaktadırlar.

7338 Sayılı Kanunun 34 üncü maddesi ile VUK'un 320 nci maddesinde yapılan değişiklikle, işletme aktifine yeni kaydedilecek amortismana tabi iktisadi kıymetler için aktife girme tarihinden itibaren günlük esasa göre amortisman ayrılabilmesi seçime bağlı bir imkan olarak mükelleflere tanınmış ve bunun yanı sıra daha uzun faydalı ömürler dikkate alınarak amortisman sürelerini uzatabilme imkanı getirilmiştir. Yıl veya gün esasına göre amortisman ayırma yöntemlerinden biri ile amortisman hesaplanmasına başlandıktan sonra hesaplama şekli değiştirilemez.

Netsis Demirbaş Yönetimi uygulamasında 9.0.46.0 sürümü ile birlikte günlük esasa göre amortisman takibi desteklenmiştir. Uygulamanın kullanılabilmesi için DEMIRBAS\\DEMGUNLUK\\1 özel parametresinin tanımlanması ve gün esasına göre amortisman ayrılacak sabit kıymetin kartı açılırken "Günlük Amort" kutucuğunun işaretlenmesi gerekir. Kıstalyum ve günlük amortisman aynı anda kullanılamaz. Daha önceden amortisman ayrılmış sabit kıymetler için günlük amortisman seçeneği işaretlenemez ve işaretli iken amortisman ayrılmaya başlandı ise günlük amortisman parametresi kaldırılamaz.

Aşağıdaki ekran görüntüsünde aynı tarihte, aynı fiyatla ve aynı amortisman oranı ile iki sabit kıymet kartı açılmış ve G001 günlük amortisman olarak belirlenmiştir.

![](../_assets/770d35a32eab28239b46.png)

İlk gözlemlenen Amort. Bitiş Yılı alanının günlük amortisman olan sabit kıymet için dönemsellik üzerinden değil alındığı ay, gün üzerinden hesaplandığıdır. 15.02.2023 alış tarihli ve 5 yıl faydalı ömür yılı olan bu sabit kıymet için amortisman bitiş yılı 14.02.2028 olarak hesaplanır. Aynı bilgiler ile ay esasına göre amortisman takibi yapılan sabit kıymetin ise amortisman bitiş yılı 2027/12 şeklindedir.

Sabit kıymetlerin aktife alınışını takiben ayrılan ilk amortisman sonrası oluşan değerler aşağıdaki gibi olur.

![](../_assets/ca10b5b39f0dfc7642f3.png)

Hesaplanan amortisman günlük amortisman işaretli olan sabit kıymette gün esası üzerinden bulunur. Günlük amortisman tutarı, yıllık amortisman tutarı 365 ile bölünerek bulunur. Bulunan günlük tutar sabit kıymetin alındığı tarihten ilgili ay sonuna kadar geçen gün ile çarpılarak ayrılacak amortisman hesaplanır. G001 için;

Aylık amortisman(15.02.2023 alış tarihi): (200.000\*0,2)/365)\*14(28.02-15.02)=1534,25

**Ayın gün sayısı**

Aylık amortisman tutarı normal amortismandan farklı olarak ayın gün sayısından etkilenir. Yıllık amortisman tutarı 365 ile bölündükten sonra bulunan günlük amortisman tutarı ayın gün sayısı ile çarpılarak aylık amortisman tutarı bulunur.

![](../_assets/1aae434c86f3e4da39cc.png)

12. ay için aylık amortisman; (200.000\*0,2)/365)\*31 = 3397,26

11. ay için aylık amortisman; (200.000\*0,2)/365)\*30 = 3287,67

**İtfa**

Alış tarihinde olduğu gibi itfa tarihinde de amortisman hesaplaması gün üzerinden yapılır. G001 için;

Aylık amortisman(14.02.2028 itfa tarihi): (200.000\*0,2)/365)\*14(14.02-01.02) = 1534,25

![](../_assets/cc1af21fff09cd646fbc.png)
