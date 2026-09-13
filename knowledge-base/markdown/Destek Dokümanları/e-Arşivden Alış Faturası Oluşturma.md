---
title: "e-Arşivden Alış Faturası Oluşturma"
page_id: "66239589"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "e-Arşivden Alış Faturası Oluşturma"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / e-Arşivden Alış Faturası Oluşturma"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTI1ZGNmYjBiLTFmZDQtNDllMS04ZjEyLWQ1ZWJmY2M3YjZkNSZsaW5rPWE3YjYzMGU0LTc1NmEtNGIxNS1hNTExLTg1ZmU1ZDIyZGM2MCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=25dcfb0b-1fd4-49e1-8f12-d5ebfcc7b6d5&link=a7b630e4-756a-4b15-a511-85fe5d22dc60&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "e-arsivden-alis-faturasi-olusturma_80088722_66239589.html"
source_version: "2022-11-02T15:00:48.487+03:00"
source_bytes: 1497104
fetched_at: "2026-09-13T04:24:33+00:00"
generator: "netsis-scraper 1.0.0"
---
# e-Arşivden Alış Faturası Oluşturma

e-Arşivden Alış Faturası Oluşturma ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Kullanıcıların e-Posta adreslerine yapmış oldukları satın almalara ait e-Arşiv belgelerinin xml dosyaları gönderilebilmektedir. 9.0.37 setinde e-Arşiv xmllerinden Alış Faturası Oluşturulması desteklenmiştir.
Fatura\>Kayıt\>e-Arşiv İşlemleri\>**e-Arşivden Alış Faturası Oluşturma** menüsü yardımıyla e-Arşiv belgelerinden alış faturası oluşturulabilmektedir.
![](../_assets/e63c03b558e0a727de7f.png)
**Dosya Seçimi** menüsüyle kullanıcılar, ellerinde bulunan e-Arşiv belgelerinin xml dosyaları çoklu bir şekilde seçerek Netsis içine aktarılmaktadır. Kullanıcılar çoklu olarak ellerindeki e-Arşiv xml belgelerini Netsise aktarabilecek, aktarım sonrasında bazılarını silebilecek veya alış faturası oluşturabileceklerdir.
![](../_assets/e22c16570b20f6353749.png)
![](../_assets/06673fcd813b67924461.png)
Ekranın altındaki barda **seçilen dosya adedi** ile, **işlenen dosya adedi** sayıları görülmektedir. Aşağıdaki örnekte görüldüğü gibi çoklu seçim ile 3 adet dosya seçilip Netsis içerisine de 3 adet dosya işlenmiştir. Eğer Netsis'e işleme sırasında herhangi bir hata olursa, işlenen dosya sayısı seçilen dosya sayısına göre daha az olacaktır.
![](../_assets/5d98f02393a120f681c4.png)
Bu şekilde Netsise işlenen dosyalar **Fatura** **Detay** kolonundaki ilgili satıra tıklandığında e-Belge Görüntüsü görüntülenebilmektedir.
![](../_assets/0ff70a78b01bc7d3c673.png)
Tanımlı olan Vergi Kimlik Numarası veya TC Kimlik Numarası bilgisinden Netsis'te kayıtlı bir cari kod bilgisine erişilebiliyorsa **Oluşturulacak Cari Kodu** alanına bu tanımlı cari kod bilgisi gelmektedir. İstenirse Oluşturulacak Cari Kod alanına tıklanarak gelen cari rehber yardımıyla farklı bir cari kod seçimi de yapılabilir.
![](../_assets/8e486ba859995ce02bae.png)
**Tarih** kolonuna, e-Arşiv faturası xmli içindeki fatura tarihi gelmektedir. **Kayıt** **Tarihi** kolonuna da günün tarihi gelmektedir. Dosya seçimi ile Netsis içerisine alınan e-Arşiv fatura xml dosyaları sonrasında ekran kapatılıp tekrar açıldığında, içeri alınan kayıtlar grid ekranda faturalaştırılmak üzere hala durmaktadır. Alış faturası oluşturulmak istenen e-Arşiv belgesi veya belgeleri seçildikten sonra **Alış Faturası Oluştur** menüsüne tıklanır. Fatura oluşturulurken cari veya stok kodundan eşleştirilemeyen kayıtlar varsa belge oluşturma işlemi yarıda kesilecektir. Fakat plasiyer kodu, depo kodu, vb alanlarda bir eksiklik varsa belge tamamlanmamış belge olarak kaydediliyor olacaktır.
![](../_assets/98a4d56dc3e2325b1264.png)
Fatura oluşturulduğunda Alış Faturaları sekmesinde durumu "**Tamamlandı**" şeklinde gösterilmektedir. E-belge Listesi sekmesinden faturalaşan e-Arşiv kaydı silinmektedir.
**Belgeye** **Git** kolonunda oluşan Alış Faturasına hızlıca ulaşılmaktadır.
![](../_assets/bcb3b1931d46b4d6dd9d.png)
