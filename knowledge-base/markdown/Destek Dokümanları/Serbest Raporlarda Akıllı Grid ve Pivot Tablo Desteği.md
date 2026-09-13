---
title: "Serbest Raporlarda Akıllı Grid ve Pivot Tablo Desteği"
page_id: "111247783"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Serbest Raporlarda Akıllı Grid ve Pivot Tablo Desteği"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Serbest Raporlarda Akıllı Grid ve Pivot Tablo Desteği"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTcyNWFiNDY2LTk0ZTctNDYzMy05NDA3LWJlZmUxM2MwYzE4MSZsaW5rPTE4OWVhMTE4LWRlYmItNDM2MS05NmRlLTc4NjNhNzRjZTlkMiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=725ab466-94e7-4633-9407-befe13c0c181&link=189ea118-debb-4361-96de-7863a74ce9d2&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "serbest-raporlarda-akilli-grid-ve-pivot-tablo-destegi_111247783_111247783.html"
source_version: "2023-05-05T14:26:01.687+03:00"
source_bytes: 303484
fetched_at: "2026-09-13T04:23:25+00:00"
generator: "netsis-scraper 1.0.0"
---
# Serbest Raporlarda Akıllı Grid ve Pivot Tablo Desteği

Netsis serbest raporlarında akıllı grid ve pivot tablo desteğiyle ilgili ayrıntılı bilgiye bu dokümandan ulaşılır.

Netsis 9.0.42 sürümü ile serbest raporlarda **Pivot Rapor** ve **Grid Rapor** seçenekleri desteklenmiştir.

Grid Rapor desteği ile rapor verileri dinamik olarak filtrelenebilir, belirli verilere göre gruplanabilir, rapor sütunları dinamik olarak istenen sırada konumlandırılabilir ve sıralama yapılabilir.

Pivot Rapor desteği ile raporun sonuç gösterimi dinamik bir biçimde düzenlenerek veriler gruplandırılabilir, sıralanabilir ve büyük veri kümeleri için özet görünümler oluşturulabilir. Pivot Rapor desteği ayrıca, genişletme ve daraltma seçenekleri ile rapor sonucuna esnek bir görünüm kazandırır.

**Pivot Rapor**

Yeni bir pivot rapor oluşturmak için Serbest Rapor menüsünden, raporlanacak nesne ve sahaların seçimi yapılır. "Rapor" butonunun sağında bulunan ok işaretine tıklanarak açılan menüden **"Pivot Rapor"** seçilir.

Daha önce kaydedilmiş olan tablo raporları "Kayıtlı Raporu Aç" menüsü kullanılarak aynı yöntem ile Pivot görünümünde açılabilir.
![](../_assets/0738c9088164cc1666d7.png)
![](../_assets/869e44b4a8717da5c523.png)
Açılan ekrandan Pivot tablonun tasarımı yapılmaktadır. Ekranın sağındaki Filtre alanında rapor kaynağı olarak seçilen alanların listesi yer alır. Bu alanlar ile Pivot tablonun satır, sütun ve veri alanları belirlenir. Filtre alanından pivot tablonun satır, sütun ve veri sahaları, görüntülenmek istenen alana sürüklenir.

Örneğin; Pivot görünümünde bölgesel aylık satış raporu için satır verisi olarak Bölge\\İl ve sütunlarda Ay bilgisinin, değer olarak satış miktarlarının görüntülenmesi için rapor tasarımı aşağıdaki gibi oluştulmuştur.

![](../_assets/c6b136b2a4180e763d59.png)

Satırlarda sağ klik menüsü ile kullanılabilen **genişletme** ve **daraltma** seçenekleri ile detay verilerin gösterimi esnek olarak sağlanabilir.

![](../_assets/ca1ff67163f772e31787.png)

Mevcut Pivot raporun tasarımında yapılan değişikliklerin tekrar kaydedilmesi için rapor kapatılırken alınan uyarıda Evet seçeneği işaretlenmelidir.

![](../_assets/3daa38ba810242fe941f.png)

**Grid Rapor**

Kayıtlı bir raporun Grid Rapor olarak görüntülenmesi için "Rapor" butonunun sağında bulunan ok işaretine tıklanarak, açılan menüden **"Grid Rapor"** seçilir.

![](../_assets/7f860e4fd0941c58f8aa.png)

Grid raporlarında verilerin gösterimiyle ilgili özel filtreler tanımlanabilir. Tablodaki belirli verilere göre gruplamalar ve sıralamalar yapılabilir.

![](../_assets/0db50c24b6c421271c86.png)
