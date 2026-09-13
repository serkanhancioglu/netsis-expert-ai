---
title: "Yan Ürün Uygulaması"
page_id: ""
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Yan Ürün Uygulaması"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Yan Ürün Uygulaması"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTRlOGZkNGZkLWNmZTYtNDkzZi05MTcxLThmZDdjNjIxODEzMSZsaW5rPWMwYzUxMzU0LTg2NWYtNGYwNi1iMGUzLTVjZTMwMmI5ODMzMCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=4e8fd4fd-cfe6-493f-9171-8fd7c6218131&link=c0c51354-865f-4f06-b0e3-5ce302b98330&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "yan-urun-uygulaması.html"
source_version: ""
source_bytes: 10729
fetched_at: "2026-09-13T04:21:58+00:00"
generator: "netsis-scraper 1.0.0"
---
# Yan Ürün Uygulaması

Bu dokümanda Netsis içerisinde yan ürün uyarlamalarının nasıl yapılabileceğinden bahsedilecektir.

Yan ürün, üretimin nihai amacı olmayan, üretim aşamalarında yan ürün olarak çıkan ve satışı da yapılan üründür. Program içerisinde yan ürün uyarlaması 2 farklı şekilde yapılabilmektedir.

\1. Yöntem; **Reçete Kaydı** ekranında yan ürün tipli bileşenlerin eklenerek üretim fişleri ile süreçlerin yönetilmesi

\2. Yöntem; Yan ürünün, **Ambar Giriş Fişi** ile Tipi: Üretim, Çıkış Yeri: Stok Kodu ve Masraf Merkezi ise ilgili mamul kodu seçilerek kalem bilgilerinde çıkan yan ürün seçimi yapılarak süreçlerin yönetilmesi

Örneğin; Ana ürün yoğurt, yan ürün kaymak ise ambar giriş fişinde Çıkış yeri; Stok kodu, Masraf Kodu: Yoğurt seçilmeli, kalemlerde ise Kaymak stoğu girilmelidir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/d6c4626e-edb1-4699-8f58-a1b335e6e4c4/au_yanurun1.png)

Dokümanımızda 1. yöntem üzerinden süreç ilerletilecektir.

Örnek reçetemiz aşağıdaki şekildedir. Yan ürün tipi ile yan ürün bileşeni reçeteye eklenmiştir. Bu durumda yapılan üretim sonu kayıtlarında ilgili mamul ve yan ürün için giriş, diğer bileşenlerden ise çıkış hareketi atılacaktır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/cdc760f6-0f02-4fea-af30-320dc1e7cc6b/au_yanurun2.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/69914d49-ec6b-4ed7-be60-5b2f1a5762d3/au_yanurun3.png)

Yan ürünlerin üretimi sonrasında yan ürün maliyetlerinin ilgili mamul ve yarı mamul maliyetinden düşürebilmek için yapılması gereken işlem adımları şu şekildedir.

o Maliyet parametrelerinden bir tanesi için YAN URUN açıklaması ile bir gider tanımlanmalıdır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/61d27557-1cba-409a-991f-0b2f446770aa/au_yanurun4.png)

o Yan ürünün çıktığı ana grup için (yani kendisinden yan ürün oluşan mamul ve yar mamuller) Ana grup kayıtlarındaki "Yan Ürün Ortalama Satış Tutarı Mamul Maliyetinden Düşülecek” parametresi işaretlenir. Bu sayede program yan ürün maliyetlerini üretilen mamul ya da yarı mamul maliyetlerinden düşerek mamul/yarı mamul maliyetini düşürmektedir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/0c23ee1b-88ec-4988-a2fd-530a55a70f28/au_yanurun5.png)

o Yan ürünler için mamul grup kodu kayıtları ekranından yeni kod tanımlanmalı ve tipi yan ürün seçili olmalıdır. İlgili yan ürün hangi safhaya aitse o ana grup koduna bağlanmalıdır. Yan ürün için ilgili mamul hammadde hesap kodları ve yansıtma hesapları doldurulmalıdır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/e2628ee0-327f-4246-86da-a5becfffd28e/au_yanurun6.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/026fb5c2-ddb3-4d2f-8765-54dcc6ecd311/au_yanurun7.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/d6074264-0392-4295-8a9f-0b3a21ee066d/au_yanurun8.png)

o Yan ürüne ait Stok Kartı Kayıtları Ek Bilgiler sekmesinde yer alan Maliyet Bilgileri kısmında yan ürün seçilmeli ve tipi yan ürün seçili olan mamul grup kodu seçilmelidir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/03e634bc-9106-42c7-8804-7f7bd57caa5b/au_yanurun9.png)

o İlgili mamul ve yarı mamuller için Mamul Grup Kodu Tanımlamaları ekranında YAN URUN gider yeri için yazılan yansıtma hesapları dolu olmalıdır.

o Yan ürünün bir satışı var ise program ortalama bir satış fiyatı hesaplar ve maliyet muhasebesi çalıştırıldığında bu fiyat üzerinden maliyet bilgi girişi ekranında yan ürün isimli gider kısmında -20,-30 gibi bu değeri göstermektedir. Eğer yan ürün satılmıyor ise bu durumda yan ürün için maliyet bilgi girişi ekranında 12/2078 tarihine ortalama satış fiyatı girilmelidir. Program yarı mamul ve mamul maliyetinden düşürme işlemini bu değer üzerinden yapacaktır.

Örneğimizde üretilen yan ürünün 5 TL üzerinden satışı yapılmıştır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/45917243-3124-431c-b6d1-5207ca45abbc/au_yanurun10.png)

Sırasıyla maliyet oluşturma ve maliyet hesaplatma işlemleri çalıştırıldığında oluşan maliyetler aşağıdaki şekildedir.

Yan üründen 20 tane üretilmiş olup ortalama satış fiyatında ise 5 TL olarak görüntülenmiştir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/ee4404e9-81a4-4510-9955-7da1e2755a3b/au_yanurun11.png)

Mamul maliyetinde ise üretilen yan ürün 5\*20=100 TL olarak maliyete etkisi aşağıdaki şekildedir.

Normalde (600+1000) /20 =80 TL lık bir maliyeti var iken yan ürünün etkisi ile (600+1000-100)/20=75 TL olarak ürünün maliyeti azalmıştır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/2f523be5-8e79-416b-a693-660011f6da37/au_yanurun12.png)

**Özel parametreler;**

Yan ürün farklı ana mamul gruplarında da çıkıyor ise bu durumda 'MALIYET','YANURUN_ORTAK' ,0 özel parametresinin kullanımı ile yan ürünün aynı olduğu farklı ana mamul grubuna bağlı mamullerin, maliyet hesaplama sürecine dahil edilebilmesi sağlanabilir.

Yan ürün miktarlarının da mahsup fişine aktarılabilmesi için; ‘MALIYET’, ‘MAHSUP_YANURUN_MIKTAR_ZORUNLU’, 1 özel parametresi tanımlanmalıdır.

Örnek kullanım şu şekildedir.

Özel parametre aşağıdaki şekilde tanımlanır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/e6e2bf2e-9e72-447f-9394-f607e8bef4f4/YAN1 (3).jpg)

90 ve 100 ana grup kodu aşağıdaki şekilde tanımlı ve bu iki ana gruptan aynı yan ürün çıkmaktadır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/30e7fb24-bfe1-4232-896d-a51c7eb2724a/YAN2.jpg)

90 ve 100 stok kodları için de aynı isim ile grup kodları açılmış ve 90 ve 100 ana gruplarına bağlanmıştır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/60275059-a987-4200-9255-9b51de918bb7/YAN3.jpg)

Yan ürün için açılan mamul grubunda ise tipinin yan ürün seçili olması ve yan ürünün çıktığı üretimi olan herhangi bir ana gruba bağlanması yeterlidir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/2479c53c-a777-4a9a-8930-fee1fecfcdbf/YAN4.jpg)

Yan ürünün stok kartı ek bilgiler sekmesinde ilgili mamul grup kodu seçilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/e2825efe-6b27-40ce-a0a6-3e7b4f6cab0c/YAN5.jpg)

90 ve 100 stoklarının üretiminde 10 adet ve 60 adetlik yan ürünler aşağıdaki şekilde çıkmış olup satış faturası ile de yan ürün satılmıştır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/e43a39f5-66cd-436a-9a74-ca9958ed1ad6/YAN6.jpg)

Maliyet oluşturma ve hesaplatma sonucu oluşan maliyetler aşağıdaki şekildedir.

Yan ürün için 70 adetlik üretim gerçekleşmiş olup ve aylık maliyeti de 80 liradır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/461947d9-18c0-4d74-8d1c-f30cd2491159/YAN7.jpg)

90 ve 100 stok kodları için yan ürünün maliyete etkisi ise ;

90 kodlu stoktan 10 adetlik yan ürün çıktığından maliyeti 10\*80=800 lira, 100 kodlu stoktan ise 60 adetlik yan ürün çıktığından maliyeti 60\*80=4800 lira düşürerek maliyetler hesaplanmıştır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/20054058-c886-4322-8a18-8920fbd028c7/YAN8.jpg)
