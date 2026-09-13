---
title: "Rezervasyon Bakiye Takibinin Fatura Modülünde Uyarlanması"
page_id: ""
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Rezervasyon Bakiye Takibinin Fatura Modülünde Uyarlanması"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Rezervasyon Bakiye Takibinin Fatura Modülünde Uyarlanması"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWMxMjMxNWJiLWFkMmUtNDY1NS1hNTgxLTlkNWUzYThhN2JmNSZsaW5rPTRkNGM5Njk4LTVjMmEtNDIxNy04MzI4LTg2MGRiOTNhYWE3MCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=c12315bb-ad2e-4655-a581-9d5e3a8a7bf5&link=4d4c9698-5c2a-4217-8328-860db93aaa70&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "rezervasyon-bakiye-takibinin-fatura-modulunde-uyarlanmasi.html"
source_version: ""
source_bytes: 5809
fetched_at: "2026-09-13T04:21:53+00:00"
generator: "netsis-scraper 1.0.0"
---
# Rezervasyon Bakiye Takibinin Fatura Modülünde Uyarlanması

İş emri malzeme rezervasyonu uygulaması ile iş emirleri için depolardan yapılan malzeme çekimleri, fatura modülü belgelerinde de dikkate alınacak şekilde yapılandırılabilir. Bu sayede çekilen malzemelerin rezerve bakiyeleri kullanmaması için aşağıdaki uyarlama adımları uygulanabilir.

Çıkış tipli fatura belgelerinde (alış/satış faturası, alış/satış irsaliyesi, DAT, Ambar Çıkış Fişi) sipariş rezervasyon bakiyelerinin takibi için aşağıdaki parametreler işaretli olmalıdır.

\1. “MRP Parametreleri” ekranında “Sipariş Bazında Rezervasyon Sistemi” seçeneği işaretli olmalıdır.

2. “Üretim Parametreleri” ekranında “Rezervasyon Bakiyelerinin Takibi Yapılsın” parametresi için “Rezerve Bakiyelere Bakılsın” veya “Rezerve ve Serbest Bakiyelere Bakılsın” seçeneği işaretli olmalıdır.

3. “Stok Parametreleri” ekranında “Lokal Depo Uygulaması” seçeneği işaretli olmalıdır.

4. “Fatura \> Satış Parametreleri” ekranında “Mal Çıkışlarda Eksi Bakiye Gösterilsin” parametresi işaretli olmalıdır.

5. “Fatura \> Satış Parametreleri” ekranda “Sipariş Stok Kontrolü” parametresi işaretli olmalıdır.

6. “Fatura \> Satış Parametreleri” ekranda “Eksi Bakiyede İşlem Durdurulsun” parametresi işaretli olmalıdır.

7. “Stok \> Lokal Depo Tanımları” ekranında çıkış yapılan depo kodu için “Eksi Bakiye Kontrol” parametresi işaretli olmalıdır.

8. “Stok \> Stok Planlama Kayıtları” ekranında çıkış yapılacak stok kodu için “Rezervasyon Bakiyelerinin Takibi Yapılsın” parametresi işaretli olmalıdır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/8a18000f-5d84-4eb6-8406-58d307d052d0/ismal_1.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/70e1a6be-48dc-4718-9f59-460fa0c18245/ismal_2.png)

Örneğin; REZM01 mamulü 1 adet REZMH01 hammaddesinden oluşmaktadır.

Hammaddeye ait hareketler aşağıdaki şekildedir ve 1 nolu depoda 40 adet bakiyesi bulunmaktadır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/b7dbde6e-09c7-4e02-b8dd-4f95c70eeeb8/isml_3.png)

Mamul için 15 adetlik bir sipariş gelmiş ve bu sipariş için iş emri girişi yapılmıştır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/57b23b67-cf6c-4883-ba01-e9bc4c779af5/ismal_4.png)

İş emri rezervasyonu ile REZH01 hammaddesinden 15 adet aynı depo için rezerve edilmiştir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/5020cf97-dd3c-46a3-b633-d62fbd0379f5/ismal_5.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/7249f3ab-e4d7-4af3-93fe-1ab86d0c129d/ismal_6.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/e23aa8c9-36b9-45ce-82ba-60e7ee83c539/isml_7.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/51b85392-8f96-42f7-b9b2-77162ed28101/ismal_8.png)

İş emri rezervasyon raporunda da aşağıdaki şekilde rezerve edildiği görülmektedir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/19be17cd-f3a0-4b1b-9d4a-1588bdf7fd41/ismal_9.png)

Aslında 40 adet bakiyemizin 15 adeti ilgili sipariş için rezerve edilmiştir. Fatura modülündeki belgelerde 25 adet üzeri çıkış yapılmak istendiğinde bu kontrolü yaparak “Rezervasyon Miktarı Aşıldı. Eksi Bakiye” uyarısı alınması sağlanacaktır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/868f15ca-8978-4d09-8edf-0ab701b763e0/ismal_10.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/c170f336-1e8b-452b-a3db-211e3f46cab4/ismal_11.png)

25 adetlik bir çıkış yapılmak istenildiğinde ise program izin verecektir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/0490edf3-c1f1-4252-bb6b-510899ce6191/ismal_12.png)
