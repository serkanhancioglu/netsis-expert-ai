---
title: "Netsis Demirbaş KKEG Uygulaması"
page_id: "126485156"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis Demirbaş KKEG Uygulaması"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis Demirbaş KKEG Uygulaması"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTA2YTRjNGQ0LTU4Y2EtNGRjNy1iOTgzLWIxZGU0OTc4ZTE0OSZsaW5rPWMxYjZiZGUyLWJjOTEtNGE3MC05Y2JjLTdiNDYyZGJmYjUzMSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=06a4c4d4-58ca-4dc7-b983-b1de4978e149&link=c1b6bde2-bc91-4a70-9cbc-7b462dbfb531&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-demirbas-kkeg-uygulamasi_126485156_126485156.html"
source_version: "2023-11-11T09:17:14.990+03:00"
source_bytes: 291530
fetched_at: "2026-09-13T04:23:11+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis Demirbaş KKEG Uygulaması

Demirbaşlarda KKEG uygulaması hakkında ayrıntılı bilgiye bu dokümandan ulaşılır.

9.0.27 seti ile birlikte binek oto amortismanlarına getirilen gider sınırlandırmaları kapsamında hesaplanmasının desteklenmesi ile birlikte demirbaş ekranlarında da geliştirmeler yapılmıştır. ÖTV ve KDV tutarı ilk ay gider olarak yazılabilmekte ya da maliyete eklenip amortisman tutarına dahil edilebilmektedir.

Netsis Demirbaş modülünde gider ve maliyetlerin takibi için yapılması gereken tanımlamalar aşağıdaki gibidir.
Öncelikle "Parametre Girişi" ekranında sıfır araçların ÖTV ve KDV sinin gider yazıldığı, maliyet olarak takip edildiği ya da ikinci el araçlar için üst sınır bedellerinin tanımlandığı alanlar bulunmaktadır. Bu alanlara 7194 sayılı Kanun ile GVK madde 40/1., 5. ve 7. Bentleri ile GVK madde 68/4. ve 5.

Bentlerinde yapılan değişikle, kiraladıkları veya iktisap ettikleri binek otomobillerin giderlerinin vergi matrahı tespit edilirken indirim olarak dikkate alınmasında her yıl belirlenen kanuni üst sınır değerleri girilmelidir.

![](../_assets/af19deb708a2c4eebd5e.png)

Daha sonrasında "Masraf Kodu Muhasebe Hesapları Tanımlama" ekranında kanunen kabul edilmeyen giderler (KKEG) yani üst sınır değerini aşan gider tutarları için hangi muhasebe kodu ile takip edileceği bu ekranda "KKEG Hesabı" işaretlenerek belirlenmektedir. Temelset entegrasyonu var ise buradan KKEG hesabı tanımlanmalıdır.
![](../_assets/1f6eda50a598746a72ff.png)

Bu tanımlamaların dışında demirbaş bilgi kartında ilgili demirbaş için hangi senaryonun uygulanacağı "Binek Oto Uygulaması" alanından seçilerek "Kıstalyum" uygulaması işaretlenmelidir.

![](../_assets/7d21febfa194b1ac2447.png)

İlgili tanımlamalar gerçekleştirildikten sonra amortisman ayırma işlemi sonrası demirbaş bilgi kartı "Amortisman Bilgileri" sekmesinden KKEG olarak aylık amortisman bilgileri izlenebilmektedir.

![](../_assets/8fbcee1c9cefc6e4bba9.png)

Amortisman ayırma işleminden sonra eğer masraf kodu tanımı ile muhasebe takibi sağlanıyor ise "Amortisman Hisse Muhasebeleştirme" sonrasında Temelset tarafında oluşan yevmiye fişinde tanımlı KKEG hesabında ilgili tutar ayrı olarak gösterilmektedir.

![](../_assets/3731e0de32f6dc582f6e.png)

Bazı hesaplama örnekleri aşağıdaki gibidir.

**Binek oto uygulaması Sıfır Araç (Gider) senaryosuna göre;**
Demirbaş alış fiyatı: 450.000,00 TL
Sıfır araç gider sınır bedeli: 440.000,00 TL
450.000,00\*0,20= 90.000,00 TL (Demirbaş Yıllık Amortismanı)
90.000,00/12 =7.500,00 TL (Aylık Amortisman Tutarı)
440.000,00\*0,20= 88.000,00 TL (KKEG Üst Sınır Üzerinden Hesaplanan Yıllık Amortisman Tutarı)
90.000,00-88.000,00= 2.000,00 TL (Yıllık KKEG Gider Amortismanı)
2.000,00/12= 166,67 TL (KKEG Aylık Amortisman Değeri)
7.500,00-166,67= 7.333,33 TL (Gider Yazılabilen Amortisman Tutarı)

**Binek oto uygulaması Sıfır Araç** **(Maliyet) ÖTV ve KDV'nin maliyete eklendiği senaryoya göre;**
Demirbaş alış fiyatı: 520.000,00 TL (ÖTV ve KDV dahil)
Sıfır araç maliyet sınır bedeli: 500.000,00 TL
520.000,00\*0,20 = 104.000,00 TL (Demirbaş Yıllık Amortisman)
104.000,00/12= 8.666,00 TL (Aylık Amortisman Tutarı)
500.000,00\*0,20 = 100.000,00 TL (KKEG Üst Sınır Üzerinden Hesaplanan Yıllık Amortisman Tutarı)
104.000,00-100.000,00 = 4.000,00 TL (Yıllık KKEG Maliyet Amortismanı)
4.000,00/12=333,33 TL (KKEG Aylık Amortisman Değeri)
8.666,66-333,33= 8.3333,33 TL (Maliyet Yazılabilen Amortisman Tutarı)
