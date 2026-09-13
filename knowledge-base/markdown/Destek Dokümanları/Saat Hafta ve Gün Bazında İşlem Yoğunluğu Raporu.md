---
title: "Saat Hafta ve Gün Bazında İşlem Yoğunluğu Raporu"
page_id: "90669155"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Saat Hafta ve Gün Bazında İşlem Yoğunluğu Raporu"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Saat Hafta ve Gün Bazında İşlem Yoğunluğu Raporu"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTdkYWYxNzhjLWJmYmUtNDJkZS04OTQxLWJkZDM5MDQ3MmE0MCZsaW5rPWM1OWNkODUxLTk0ZjUtNDRkZS05ZTYyLWJiMmQ4YzdiMGUwNyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=7daf178c-bfbe-42de-8941-bdd390472a40&link=c59cd851-94f5-44de-9e62-bb2d8c7b0e07&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "saat-hafta-ve-gun-bazinda-islem-yogunlugu-raporu_90670260_90669155.html"
source_version: "2022-12-15T09:38:48.000+03:00"
source_bytes: 114343
fetched_at: "2026-09-13T04:23:52+00:00"
generator: "netsis-scraper 1.0.0"
---
# Saat Hafta ve Gün Bazında İşlem Yoğunluğu Raporu

Saat Hafta ve Gün Bazında İşlem Yoğunluğu Raporu ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

9.0.32 sürümü ile Netsis içerisinde Saat- Hafta- Gün Bazında İşlem Yoğunluğu Raporu" desteklenmiştir.

Bu düzenleme ile kullanıcıların belge bazında log tutulan tablolarda yaptığı işlemlerin yoğunluğu (kümüle veya ortalama olarak) raporlanabilecektir.

Bu özelliği kullanabilmek için "Log Parametreleri" içerisinde "Log Uygulaması Kullanılsın" ve "Kullanıcı Oturum İşlemleri Log Kayıtları Tutulsun" parametreleri işaretli olmalıdır.

![](../_assets/aa4191e535508df37175.png)

Saat Hafta ve Gün Bazında İşlem Yoğunluğu Raporu'na, Log Modülü \> Raporlar \>Saat- Hafta-Gün Bazında İşlem Yoğunluğu Raporu menüsünden ulaşılır.

![](../_assets/29430c59e31b8eefb88f.png)

Kısıt sekmesi üzerinden rapor alınmak istenilen tarih aralığı ve hangi işlem tiplerinin dahil edileceği seçimi yapılmalıdır. Merkez şubeden diğer şubelerin verilerini de rapora dahil etmek istenir ise şubeler dahil seçeneği işaretlenerek rapor alınabilir.

Raporlama türü: Saatlik/Günlük/Haftalık olarak üç seçenek mevcuttur. Ayrıca hesaplanan ilgili değerlerin ortalamasını mı yoksa kümülesini mi raporlayacağının dair seçim yapılabilmektedir.

Bu alanda seçilen değere göre verilen tarih aralığı içerisindeki sayılar kümüle edilip veya ortalaması alınarak gruplanmaktadır. Örneğin, 01.01.2020 - 05.02.2020 şeklinde bir tarih aralığı verilmiş olsun ve raporlama türü günlük seçildi ise raporda pazartesi, salı,...pazar olarak şekilde 7 gün üzerinden sonuçlar raporlanacaktır. Bu tarih aralığında pazartesi gününe denk gelen ilgili işlemler pazartesi alanına eklenecek. Tip seçimine göre kümüle olarak veya ortalama seçeneği seçili ise " toplam işlem sayısı/ tarih aralığındaki pazartesi sayısı " şeklinde ortalama hesaplanmaktadır.

Eğer saatlik seçilmiş ise 00:00:01-01:00, 01:00:01-02:00,23:00:01-00:00 arasında 24 sütunluk bir grafik oluşturulmaktadır. Örneğin burada 00:00:01 ile 01:00 arasındaki işlemleri 00 sütununda raporlanmaktadır.

Haftalık seçilmiş ise yıldaki hafta detayı ile raporlanabilmektedir.

Örnek uygulama

Rapor ekranında aşağıdaki kısıtlarla rapor alındığında;

![](../_assets/29430c59e31b8eefb88f.png)

Aşağıdaki şekilde günlük sonuçlar karşımıza çıkacaktır.

![](../_assets/206ebc21ccc2a2ad683e.png)

Görsel grafikte ilgili gün üzerine girildiğinde ise tarih aralığında ilgili güne karşılık gelen detay bilgilere erişilebilmektedir.

![](../_assets/b614b05a845cca49120a.png)

Raporlama türü ortalama seçildiğinde ise;

![](../_assets/8ac0ae299648be3ff413.png)![](../_assets/807564e48d4b0cdce296.png)

Seçilen tarih aralığında 109 adet Çarşamba günü vardır. Kümüle raporda işlem sayısı 56 olarak görünmektedir.

Oran: İşlem sayısı/ tarih aralığındaki gün sayısı =56/109=0,51 olarak hesaplanmaktadır.
