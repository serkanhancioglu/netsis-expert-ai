---
title: "Dönemsel Demirbaş Enflasyon Taşıma İşlemleri"
page_id: "135825055"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Dönemsel Demirbaş Enflasyon Taşıma İşlemleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Dönemsel Demirbaş Enflasyon Taşıma İşlemleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTY3MWE3N2Q0LTFmMDYtNGMxMi1hMjQwLWUxZGJkYmMzNjBlMyZsaW5rPTg0Y2U5N2VkLTI1YjMtNDNkOS1hOTk3LTM4MDY3ZmQ3N2M2ZiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=671a77d4-1f06-4c12-a240-e1dbdbc360e3&link=84ce97ed-25b3-43d9-a997-38067fd77c6f&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "donemsel-demirbas-enflasyon-tasima-islemleri_135825072_135825055.html"
source_version: "2024-03-29T13:08:08.940+03:00"
source_bytes: 896480
fetched_at: "2026-09-13T04:22:55+00:00"
generator: "netsis-scraper 1.0.0"
---
# Dönemsel Demirbaş Enflasyon Taşıma İşlemleri

Demirbaş amortisman giderleştirme işleminin aylık ya da dönemsel yapılması isteğe bağlıdır. Amortisman giderleştirme işlemini dönemsel olarak takip eden firmalar enflasyon taşıma işlemlerinide dönem verileri üzerinden yapabilirler.
Enflasyon düzeltmelerinin dönemsel yapılabilmesi için;

- Parametre Girişi ekranında Dönem Sayısı girilmeli
- Aylık Amortisman Uygulaması kapalı olmalı
- Değerleme Oran girişi ekranından sadece dönem ile uyumlu olan aylar için oran indirilmelidir.

Bu şekilde Değerleme Oran Girişi ekranından ilgili ay için Enf.Oran Getir butonuna basıldığında program o ayın değil, ayın ait olduğu dönemin katsayısını getirecektir.

Örneğin dönem sayınız 4 iken siz 2024/3 için Enf.Göre Oran Getir çalıştırısanız, program 31.03.2024 endeksini 31.12.2023 endeksine bölecek ve katsayıyı getirecektir.
![](../_assets/5a8e7461042beae4a12f.png)

Örnek:01.01.2020 tarihinde alınmış bir demirbaş, 31.12.2023 tarihinde enflasyon düzeltmesine tabi tutulacak ve ardından 2024-3 taşıması yapılacaktır.

Döviz Takibi /Döviz Kurları Girişi ekranıdan 31.12.2023 ve 31.03.2024 endeksleri indirilmiş olmalı ve Değerleme Oran Girişi ekranıdan 2024 3. Ay için katsayı indirilmiş olmalıdır.
![](../_assets/1923e690232bfff6f07e.png)![](../_assets/6d6157830f524ddcd6a8.png)

Not:2024 Mart katsayısı doküman tarihinde yayınlanmadığı için tahmini bir değer girilmiştir.

2023 12. Ay için Değerleme ve Amortisman Ayırma işlemi çalıştırıldıktan sonra Enflasyona Başlama işlemi çalıştırılmış ve Enflasyon Devir bilgilerinin dolması sağlanmıştır.
![](../_assets/53707ff7cd28ca2cc128.png)

2024-3 için değerleme ve amortisman ayırma işlemi Enflasyon Düzeltmesi kapsamında yapılmıştır.

![](../_assets/7320fd1796445218f786.png)

Elle girilen Mart katsayısı: 6,246320 Oran karşılığı : 1,0624632

![](../_assets/b7474e2f63fc816d20ed.png)

2023-12 Enflasyon Devir Bilgileri ekranındaki tutarlar baz alınıp 2024-3 katsayısı kullanılarak enflasyon taşıması yapılmıştır. Birikmiş amortismanda baz alınan değer bir önceki dönemin toplam amortismanıdır.
