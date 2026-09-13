---
title: "Muhasebe Dönem Sonu İşlemleri"
page_id: ""
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Muhasebe Dönem Sonu İşlemleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Muhasebe Dönem Sonu İşlemleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWM4ZTE5Nzk2LWQzYWUtNDhiOS05OWJjLTE3OWMzM2NmMWVjMiZsaW5rPTlkMDI0ZjE0LTZlODYtNDM0YS05YzA2LWQwOTJmNmU4NjEyYiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=c8e19796-d3ae-48b9-99bc-179c33cf1ec2&link=9d024f14-6e86-434a-9c06-d092f6e8612b&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "muhasebe-donem-sonu-islemleri.html"
source_version: ""
source_bytes: 12330
fetched_at: "2026-09-13T04:21:47+00:00"
generator: "netsis-scraper 1.0.0"
---
# Muhasebe Dönem Sonu İşlemleri

##### Yansıtma İşlemlerinin Amacı ve Süreçteki Önemi

Uygulama üzerinde gerçekleştirilen yansıtma işlemleri, işletmenin operasyonel giderlerinin mali tablolara doğru şekilde aktarılmasını sağlayan standart bir muhasebe prosedürüdür. Bu süreç, giderlerin türlerine göre sınıflandırılmasından, dönem sonu sonuç hesaplarına taşınmasına kadar olan döngüyü kapsar.

##### 1. 7’li Gider Hesaplarının İşlevi

İşletmenin faaliyetleri süresince oluşan tüm giderler (personel, enerji, amortisman, kira vb.), 7’li Gider Hesapları (740, 760, 770 gibi) altında kaydedilir. Bu hesaplar, yapılan harcamanın işletme fonksiyonuna göre ayrıştırılmasını sağlar. Bu sayede yönetim, hangi departmanın veya hangi faaliyetin ne kadar gider ürettiğini detaylı olarak izleyebilir.

##### 2. Yansıtma Hesaplarının Görevi ve Kullanım Nedeni

```text
Muhasebe sisteminde 7’li hesaplar ile 6’lı sonuç hesapları arasında doğrudan bir bağlantı kurulmaz. Yansıtma hesaplarının kullanılmasının temel nedeni, giderlerin izleme aşaması ile sonuç aşamasının birbirinden bağımsız ve kontrol edilebilir olmasını sağlamaktır. Yansıtma hesapları, bu noktada ara köprü görevi görür.
•    7’li hesaplardaki giderler, "Yansıtma Hesapları" (741, 761, 771 gibi) aracılığı ile fonksiyonlarına uygun olan ilgili 6’lı hesaplara (620, 631, 632 gibi) aktarılarak gelir tablosuyla ilişkilendirilirler.
```

##### 3. 6’lı Hesapların 690 Dönem Kârı veya Zararı Hesabına Aktarılması

```text
Dönem içerisinde yansıtma işlemleri ile 6'lı hesaplara aktarılan giderler ve oluşan gelirler, işletmenin faaliyet performansını gösterir. Bu sürecin son halkası, 6’lı grupta biriken tüm gelir ve giderlerin 690 Dönem Kârı veya Zararı hesabında birleştirilmesidir.
Görevi
Bu adım, dönem içerisindeki tüm "Gelir" (600, 601 vb.) ve "Gider/Maliyet" (620, 631, 632 vb.) hesaplarının bakiyelerinin tek bir hesapta toplanmasını sağlar. Böylece işletmenin faaliyet dönemini kârla mı yoksa zararla mı kapattığı net bir şekilde ortaya konulur.
Neden Yapılır?
•    Dönemsellik İlkesi: Muhasebenin temel ilkelerinden biri olan dönemsellik gereği, her dönem kendi gelir ve gideriyle hesaplanmalıdır. 6'lı hesaplar 690 hesabına aktarılarak kapatılır; böylece bir sonraki faaliyet dönemine "sıfır" bakiyeyle başlanır.
•    Net Performans Ölçümü: İşletmenin tüm operasyonel başarısı, 690 hesabının bakiyesinde (Net Kâr veya Zarar olarak) birleşir. Bu hesap, şirketin mali sağlığını gösteren nihai özet noktasıdır.
```

**Dönem sonu muhasebe yansıtma ve kapanış işlemleri, Tekdüzen Hesap Planı'na (THP) göre belirli ve kesin bir silsile ile yapılır. Uygulama ekranlarında bu akışı gerçekleştirmek için izlemeniz gereken teknik adımlar aşağıda detaylandırılmıştır:**

##### 1.Yansıtma Girişi

Dönem içinde 7'li hesaplarda (710, 720, 730, 740, 770 vb.) biriken tüm giderler, ilgili yansıtma hesapları (711, 721 vb.) kullanılarak 6'lı Gelir Tablosu hesaplarına (veya üretici işletme ise önce 151/152 stok hesaplarına, oradan da maliyet hesabına) aktarılır.

7’li hesaplardaki giderlerin, hangi yansıtma hesabına aktarılacağı Muhasebe/İşlemler/Dönem Sonu İşlemleri/Yansıtma Girişi ekranından belirlenir. Grid alandan 7’li muavin hesap seçildikten sonra Yansıtma Kodu belirlenip kaydedilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/ec708b73-49ec-4207-9d39-3c7d2b0c6cb0/es_yansitmagirisi.jpg)

##### 2.Yansıtma Fişi Oluşturma

Yansıtma Girişi ekranından yapılan tanımlamalar doğrultusunda 7’li gider hesaplarının bakiyesini yansıtma hesaplarına aktarmak için Yansıtma Fişi Oluşturma işlemi çalıştırılır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/e4f9932f-39f4-41fa-9a75-3ec0d74e1ca0/es_yansitmafisiolusturma.jpg)

Fiş Tarihi: Yansıtma fişinin oluşturulacağı tarih bilgisidir.

Fiş No: Yansıtma fişinin yevmiye fiş girişi ekranındaki fiş no bilgisidir.

Açıklama: Yansıtma fişinin yevmiye fiş girişi ekranındaki "Açıklama 1" sahasına aktarılacak olan açıklama bilgisidir.

Muhasebe Kodu: İşlemin belli bir hesap kodu aralığı için çalışmasının istenmesi hâlinde, hesap kodu aralığının girileceği alandır.

Başlangıç-Bitiş Yıl / Ay: 7’li gider hesaplarının bakiyesinin alınacağı tarih aralığının girileceği alandır.

**Uygulama Özel Notu:** Bu işlem sonucunda oluşan fiş "Kapanış Fişi" tipindedir. Bu sayede 7’li asıl hesaplar raporlarda "sıfırlanmış" görünmez; dönem sonuna kadar asıl gider bakiyeleri izlenmeye devam edilebilir.

Muhasebe Kaydı: 7’li Yansıtma Hesabı (Borç) / 7’li Asıl Gider Hesabı (Alacak).

##### 3.Yansıtma Girişi(Diğer Hesaplar)

Yansıtma hesaplarına aktarılan 7’li hesap bakiyelerinin gelir tablosu ile ilişkilendirilmesi için Muhasebe/İşlemler/Dönem Sonu İşlemleri/Yansıtma Girişi ( Diğer Hesaplar) ekranından tanımlama yapılır. Grid ekrandan 7’li muavin hesap seçildikten sonra Yansıtma Kodu belirlenip kaydedilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/c06270ca-3e98-4a9b-be51-0ad4ba5e1999/es_yansitmadigergirisi.jpg)

##### 4.Yansıtma Fişi Oluşturma (Diğer Hesaplar)

Yansıtma Girişi (Diğer Hesaplar) ekranından yapılan tanımlar doğrultusunda yansıtma hesaplarındaki bakiyenin, fonksiyonlarına uygun olan ilgili 6’lı hesaplara (620, 631, 632 gibi) aktarılması için Yansıtma Fişi Oluşturma (Diğer Hesaplar) işlemi çalıştırılır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/7a1e6ca8-dc4a-4a82-80e6-c8d4018be809/es_yansitmafisiolusturmadiger.jpg)

Fiş Tarihi: Yansıtma fişinin oluşturulacağı tarih bilgisidir.

Fiş No: Yansıtma fişinin yevmiye fiş girişi ekranındaki fiş no bilgisidir.

Açıklama: Yansıtma fişinin yevmiye fiş girişi ekranındaki "Açıklama 1" sahasına aktarılacak olan açıklama bilgisidir.

Muhasebe Kodu: İşlemin belli bir hesap kodu aralığı için çalışmasının istenmesi hâlinde, hesap kodu aralığının girileceği alandır.

Başlangıç-Bitiş Yıl / Ay: 7’li gider hesaplarının bakiyesinin alınacağı tarih aralığının girileceği alandır.

**Uygulama Özel Notu:** Bu aşamada oluşan fiş "Mahsup Fişi" tipindedir. Gider artık bir fonksiyonel maliyete (620, 631, 632 vb.) dönüşerek gelir tablosuna dahil edilir.

Muhasebe Kaydı: 6’lı Gider Hesabı (Borç) / 7’li Yansıtma Hesabı (Alacak).

##### 5.Gelir Hesapları Yansıtma Girişi

Dönem içerisinde 6’lı grupta toplanan tüm gelir ve giderlerin 690 Dönem Kârı veya Zararı hesabında birleştirilmesi için tanımlar Gelir Hesapları Yansıtma Girişi ekranından yapılır. Grid alandan 6’li muavin hesap seçildikten sonra Yansıtma Kodu belirlenip kaydedilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/21f7ad87-f7ec-482f-8419-50bf3c3f5725/es_gelirhesyansitmagirisi.jpg)

##### 6.Gelir Hesapları Kâr-Zarar Devir Fişi

Gelir tablosundaki tüm 6'lı gider hesapları (620, 632 vb.) alacaklandırılarak, 6'lı gelir hesapları (600, 642 vb.) ise borçlandırılarak 690 Dönem Kârı veya Zararı hesabına devredilir ve kapatılır.

Gelir Hesapları Yansıtma Girişi ekranından yapılan tanımlamalar doğrultusunda; dönem içerisinde 6'lı hesaplara aktarılan giderlerin ve oluşan gelirlerin 690 hesabına aktarılması için Gelir Hesapları Kâr-Zarar Devir Fişi oluşturma işlemi çalıştırılır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/b296e7f2-fe5e-449c-979e-72ac79ae0fcb/es_gelirhesyansfisiolustur.jpg)

Fiş Tarihi: Yansıtma fişinin oluşturulacağı tarih bilgisidir.

Fiş No: Yansıtma fişinin yevmiye fiş girişi ekranındaki fiş no bilgisidir.

Açıklama: Yansıtma fişinin yevmiye fiş girişi ekranındaki "Açıklama 1" sahasına aktarılacak olan açıklama bilgisidir.

Muhasebe Kodu: İşlemin belli bir hesap kodu aralığı için çalışmasının istenmesi hâlinde, hesap kodu aralığının girileceği alandır.

Başlangıç-Bitiş Yıl / Ay: 6’lı hesapların bakiyesinin alınacağı tarih aralığının girileceği alandır.

**Uygulama Özel Notu:** Bu işlem sonucunda oluşan fiş "Kapanış Fişi" tipindedir. Bu sayede 6’li asıl hesaplar raporlarda "sıfırlanmış" görünmez; dönem sonuna kadar asıl bakiyeleri izlenmeye devam edilebilir.

##### 7.Vergi Karşılığının Ayrılması

Eğer 690 hesabı alacak bakiyesi veriyorsa (işletme kâr etmişse), ödenecek kurumlar/gelir vergisi hesaplanarak 691 hesabına atılır.Vergi sonrası kalan net kâr ise 692 hesabına aktarılır. 690 hesabının 691 ve 692'ye aktarıldığı bu fiş uygulamadan manuel olarak oluşturulur. Fiş tipi mahsup olmalıdır.

691 hesaba aktarılan ödenecek kurumlar/gelir vergisi tutarı bilançodaki 370 hesaba aktarılır. Bu fiş uygulamadan manuel olarak oluşturulur ve fişin tipi kapanış olmalıdır.

##### 8. Bilançoya Aktarım

692 hesabı kapatılarak, sonuç kâr ise bilançonun özkaynaklar grubundaki 590 Dönem Net Kârı hesabına; sonuç zarar ise 591 Dönem Net Zararı (-) hesabına aktarılır. Bu fiş uygulamadan manuel olarak oluşturulur ve fişin tipi mahsup olmalıdır.

##### 9. Kapanış Kaydı (Kesin Mizan)

Gelir tablosu hesapları tamamen kapandıktan sonra çıkarılan kesin mizanda sadece Bilanço (1, 2, 3, 4, 5 numaralı) hesapları bakiye verir. Aktif karakterli hesaplar alacaklandırılarak, pasif karakterli hesaplar borçlandırılarak "Kapanış Fişi" kesilir ve tüm dönem tamamen kapatılır. Bu fiş uygulamadan Kapanış Fişi adımından oluşturulur.

**Dip not :** Netsis içerisinde yansıtma işlemlerinin iki aşamalı ve farklı fiş tipleriyle (Kapanış ve Mahsup) yönetilmesi, muhasebe disiplini açısından "izlenebilirliği" maksimize eder. 7'li asıl hesapların kapanış fişiyle yansıtılması, mizan kontrolü sırasında giderlerin kaynağını görmemizi sağlarken; mahsup fişiyle 6'lı hesaplara aktarım, gelir tablosunun anlık ve doğru oluşmasını garanti altına alır.
