---
title: "e-Arşiv Parametreleri"
page_id: "50659751"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Fatura"
  - "Kayıt / Fatura"
  - "E-Arşiv İşlemleri"
  - "e-Arşiv Parametreleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Fatura / Kayıt / Fatura / E-Arşiv İşlemleri / e-Arşiv Parametreleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTQwMWJjMzljLTZhOGMtNGY2OC1iZjVlLTkwMzc2ZTRmZjg4MiZsaW5rPTcyZDc0Yzc5LTE3ZGUtNGM1NC1iM2E4LTQwNzM1ZGI4NjVkMCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=401bc39c-6a8c-4f68-bf5e-90376e4ff882&link=72d74c79-17de-4c54-b3a8-40735db865d0&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "e-arsiv-parametreleri_50659769_50659751.html"
source_version: "2022-10-24T14:55:45.187+03:00"
source_bytes: 7875
fetched_at: "2026-09-13T04:02:23+00:00"
generator: "netsis-scraper 1.0.0"
---
# e-Arşiv Parametreleri

e-Arşiv parametrelerinin tanımlandığı bölüm e-Arşiv Parametreleri bölümüdür. e-Arşiv Parametreleri, "Lojistik - Satış Bölümünde" Fatura/Kayıt menüsünün altında yer alır.

e-Arşiv Parametreleri ekranında yer alan parametreler ve içerdiği bilgiler şunlardır:

| e-Arşiv Parametreleri Ekranı |  |
| --- | --- |
| e-Arşiv Uygulaması Kullanılsın | İçinde bulunulan şubede e-Arşiv uygulamasının kullanılması için işaretlenen parametredir. Aynı veritabanında farklı işletmeler olduğunda, tüm işletmelerde e-Arşiv kontrollerinin geçerli olmamasını sağlar. |
| Belge Birim Kod | e-Arşiv olarak oluşturulacak belgelerin takip edileceği ve gelir idaresine iletilecek olan 3 haneden oluşan belge numarasının seri kodu bilgisinin tanımlandığı alandır. |
| Gönderici Birim Etiketi | Gelir idaresinin başvuru sırasında bildirdiği entegrasyon kullanıcı bilgilerindeki GB ETİKET bilgisinin tanımlandığı alandır. |
| e-Arşiv Tevkifat Kodu | Tevkifat uygulamasını kullanan firmaların, e-arşiv göndereceği tevkifat kodunun tanımlandığı alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, tevkifat kodu seçimi yapılır. |
| Çoklu Belge Birim Kod Kullanılsın | Birden fazla e-Arşiv birim kod kullanılması için işaretlenecek parametredir. “Belge birim kodlarınızı buradan girebilirsiniz” yazısı üzerine tıklandığında “Çoklu Seri Giriş Ekranı” açılır. Bu ekran üzerinden belge birim kodları tanımlanır. İnternet üzerinden satış yapan firmalar internet fatura serisi kullanmak zorundadır. İnternet satışı yaptıktan sonra gönderdikleri e-Arşiv'leri internet fatura serisi ile göndermek zorundalar. "İnternet Faturası" olarak tanım yapılması için "İnternet Fatura Serisi" seçeneğinin işaretlenmesi gerekir. |
| Netsis e-Arşiv Gönderim Servisi | Netsis e-Arşiv Servis Uygulaması, entegratöre gönderilen e-Arşiv faturalarının; gönderme, arşivleme ve sorgulama işleminin bekleme olmadan yapılmasını sağlayan yardımcı servis uygulamasıdır. e-Arşiv Servis Uygulaması, her 10 saniyede bir sorgulama yaparak, arşivlenecek belge varsa bulur ve arşivleme işlemi yapar.<br>e-Arşiv taslağı oluşturulduktan sonra "Arşivle" butonuna tıklandığında; devrede olan servis, arşivlenecek kayıtları tespit ederek gönderilmeyi bekleyen e-Arsiv faturalarını entegratöre iletir. Daha önce entegratöre iletilen ve imzalanan belgeleri sisteme indirir ve son olarak e-Arşiv faturalarının entegratördeki durum kodu ve açıklamalarını alarak işlemi gerçekleştirir. Dolayısıyla, bu işlemler mevcut e-Arşiv ekranlarından yapıldığında, oluşan performans sorunları ve kullanıcıların bekleme süresi en az seviyeye iner. Arşivleme işlemi sırasında entegratörden dönen hata cevapları servis tarafından loglanır. Bu kayıtlara Fatura → Kayıt → e-Arşiv İşlemleri → "[e-Arşiv Log Kayıt İnceleme](<e-Arşiv Log Kayıt İnceleme.md>)" ekranından ulaşılabilir. |
| e-Arşiv Sıralı Belge Kontrolü | e-Arşiv sıralı belge kontrolünün sistem tarafından otomatik olarak yapılması için kullanılan parametredir. Belgelerin sıralı olarak ve aradaki numarayı atlamadan (sırayı bozmadan) gönderilmesini sağlar. Alanın sağ tarafında yer alan aşağı ok butonu ile; e-Arşiv Sıralı Belge Kontrolü Yapılmasın, e-Arşiv Sıralı Belge Kontrolü Yapılsın - Uyarı Versin, e-Arşiv Sıralı Belge Kontrolü Yapılsın - İşlem Durdurulsun seçenekleri arasından tercih yapılabilir. |
| Belge Kontrolü Gün Sayısı | e-Arşiv Sıralı Belge Kontrolü alanında e-Arşiv Sıralı Belge Kontrolü Yapılsın - Uyarı Versin veya e-Arşiv Sıralı Belge Kontrolü Yapılsın - İşlem Durdurulsun seçenekleri seçildiğinde aktif hale gelen alandır. Belge kontrolünün yapılacağı gün sayısının tanımlanarak, belirlenen gün sayısı kadar kontrol sağlar. En fazla 30 gün tanımlanabilir. |
