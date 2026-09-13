---
title: "Devir Amortisman Bilgileri Girişi Destek Dokümanı"
page_id: "106726726"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Devir Amortisman Bilgileri Girişi Destek Dokümanı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Devir Amortisman Bilgileri Girişi Destek Dokümanı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWJlMTg0ZmE2LWQ1MzMtNDhhZS1iNjk2LWVhZGZhNDY3NjQwMSZsaW5rPThiYjcxNGQ4LTIyZmUtNDI0MS1hMjIxLTljZmFiZWNlZGIyZCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=be184fa6-d533-48ae-b696-eadfa4676401&link=8bb714d8-22fe-4241-a221-9cfabecedb2d&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "devir-amortisman-bilgileri-girisi-destek-dokumani_106726726_106726726.html"
source_version: "2023-03-13T09:11:49.907+03:00"
source_bytes: 539995
fetched_at: "2026-09-13T04:23:37+00:00"
generator: "netsis-scraper 1.0.0"
---
# Devir Amortisman Bilgileri Girişi Destek Dokümanı

Devir amortisman bilgileri girişi hakkında ayrıntılı bilgiye bu dokümandan ulaşılır.

Demirbaş yönetimi üzerinde sabit kıymetlerin takibi alındığı tarih itibari ile kartlarının tanımlanması ile yapılabildiği gibi, uygulama kullanılmadan önce alınmış olan sabit kıymetlerin belirlenen bir tarih itibari ile girilecek olan devir rakamları üzerinde de yapılabilir.

Devir Amortisman Bilgileri Girişi programın kullanılmaya başlanmasından önce alınan demirbaşların, devir rakamlarının girilmesi amacıyla kullanılan bölümdür. Bu bölümden girilen devir rakamları baz alınarak ilk çalıştırılan Değerleme ve Amortisman Ayırma işleminde, hesaplanan tutarlar Demirbaş Bilgi Kartı/ Amortisman Bilgileri bölümüne atılır.

![](../_assets/7be20c44dc1c471b9069.png)

**Yıl/ Ay**

Devir girilen demirbaş için, devir bilgilerinin kapsadığı son yıl/ ay değeridir. Program 2022/1. ayından itibaren kullanılacak ise bu sahaya 2021/12 girilmelidir

**Sabit Kıymet**

Devir alınan ay sonu itibariyle, son değerleme sonucu oluşmuş olan sabit kıymet tutarının girileceği sahadır.

**Birikmiş Amortisman**

Devir alınan ay sonu itibariyle ilgili demirbaş için ayrılan amortisman toplamıdır.

**Yıllık Amortisman**

Devir girilen yıl içerisinde ayrılmış amortisman tutarıdır. Örneğin; 2021 3. aya devir giriliyor ise 1., 2. ve 3. ay dahil 3

aylık amortisman tutarıdır.

**Devreden Amortisman**

Kıstalyum uygulamasına giren demirbaşlar için son yılda ayrılacak amortisman tutarına eklenecek olan çalışmayan kısım amortisman tutarıdır.

**Kümüle Fon**

Devir girilen yıl ve ay sonu itibariyle ayrılan toplam fon tutarıdır.

**Pas Birikmiş Amortisman**

Devri girilen demirbaş için devir girdiği yıl ve aya kadar ayrılmamış amortismanlarının toplamıdır.

**Pas Yıllık Amortisman**

Devri girilen demirbaş için o yıl amortisman ayrılmayacak ise, bu sahaya o yıl için ayrılması gereken amortisman tutarı girilmelidir.

Örnek: Demirbaş Yönetimi 2022 Ocak ayında kullanılmaya başlanacaktır. 2019/1 ayında 53.000.000,00TL'ye satin alınmış olan sabit kıymetin 2021/12 itibari ile devir rakamları girilecek ve 2022/1 ayında amortisman ayrılmaya başlanacaktır.

![](../_assets/9c59dd99aa9cbe5c3329.png)

Sabit kıymetin kartı 2019/1 alış tarihi ile alındığı tutar üzerinden kaydedilir.

Hesaplamada sınır tarih 2021/12 olacağı için normal amortisman 6,66 üzerinden birikmiş amortisman ve yıllık amortisman hesaplanır.

Birikmiş amortisman: 2021/12 de toplam değeri girileceği için tam 3 yıllık amortisman alınır.

53.000.000 \* 0,0666 = 3.529.800\*3 =10.589.400

Yıllık amortisman: Devrin girildiği yıl/aya kadar o yıl içerisinde ayrılan amortisman girilir. Burada zaten 12. ay olduğu için tam 1 yıllık amortisman girilir.

53.000.000 \* 0,0666 = 3.529.800

Aşağıda görüldüğü üzere Amortisman Bilgileri sayfasında birikmiş amortismana, içerisinden yıllık değerin ayrılığı tutar gider.

![](../_assets/814547aad95e19dc3e15.png)

2022/1 ayında değerleme ve amortisman ayırma işlemi çalıştırıldığında ilgili sabit kıymet için amortisman ayrılır.

![](../_assets/26fc0f7d28d69e6a4c4a.png)

Örnek: Demirbaş Yönetimi 2022 Mart ayında kullanılmaya başlanacaktır. 2019/1 ayında 53.000.000,00TL'ye satin alınmış olan sabit kıymetin 2022/2 itibari ile devir rakamları girilecek ve 2022/3 ayında amortisman ayrılmaya başlanacaktır.

Sabit kıymetin 2022/2 için birikmiş amortisman ve yıllık amortismanı hesaplanır.

Birikmiş amortisman: 2022/2 de baz alındığı için 3 yıl(2019-2020-2021) 2 aylık(Ocak,Şubat) ayrılan amortisman toplamı birkmiş amortisman sahasına girilir.

Yıllık amortisman : 53.000.000 \* 0,0666 = 3.529.800Aylık amortisman : 3.529.800/12 =294.150 Birikmiş amortisman=(3.529.800 \* 3 yıl)+ (294.150\*2ay)=11.177.700

Yıllık amortisman = 2022/2 ayı dahil ayrılan 2 aylık amortisman 3. Ay girilecek devir bilgileri için yıllık amortisman değeridir.

Yıllık amortisman : 294.150\*2ay = 588,300

![](../_assets/df0f96bf947186e93ada.png)

2022/3 ayında değerleme ve amortisman ayırma işlemi çalıştırıldığında ilgili sabit kıymet için amortisman ayrılır.

![](../_assets/50097105d8068383be6b.png)
