---
title: "Ambar Fişi Muhasebeleştirme İşleminde Enflasyon Farkının Oluşması"
page_id: "135825801"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Ambar Fişi Muhasebeleştirme İşleminde Enflasyon Farkının Oluşması"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Ambar Fişi Muhasebeleştirme İşleminde Enflasyon Farkının Oluşması"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTkxYmQ1ODZjLTU4NGYtNDIyOS05MmIwLTk3MDE1ZTE3Yzk5MSZsaW5rPTNkNjcwMjUxLTdkM2YtNGU0YS1iNmRiLTYzNWYwZjQ4YTUzZSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=91bd586c-584f-4229-92b0-97015e17c991&link=3d670251-7d3f-4e4a-b6db-635f0f48a53e&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ambar-fisi-muhasebelestirme-isleminde-enflasyon-farkinin-olusmasi_135825801_135825801.html"
source_version: "2024-04-15T12:34:18.470+03:00"
source_bytes: 424362
fetched_at: "2026-09-13T04:22:53+00:00"
generator: "netsis-scraper 1.0.0"
---
# Ambar Fişi Muhasebeleştirme İşleminde Enflasyon Farkının Oluşması

9.0.54.2 patchiyle birlikte Ambar Fişi Muhasebeleştirme işleminde enflasyon farkının da atılması desteklenmiştir. Ambar Çıkış Fişlerinin muhsabeleştirilebilmesi için Çıkış Yeri Masraf Merkezi seçilir.

Ambar Fişi Muhasebeleştirme işleminde enflasyon farkının da atılması için;

- Toplulaştırılmış Yöntem Uygulaması “Hiçbiri” seçili olmalıdır.
- Ambar Çıkış Fişi Çıkış Yeri Masraf Merkezi seçili olmalıdır.
- İlgili ay için Stok Döviz Çevrim çalıştırılmış olmalıdır.
- İlgili ay için Stok Enflasyon Düzeltme işlemi yapılmış olmaldır.
- İlgili ay için Maliyet Oluşturma çalıştırılmış olmalıdır.

Örnek: Ay içinde girilmiş bir ambar çıkış fişinin muhasebeleştirilmesi adımında enflasyon farkının oluşması

Ambar Çıkış Fişi Çıkış Yeri Masraf Merkezi seçili olarak girilir.

![](../_assets/02fe77640120a9cee955.png)

Ay içi işlemler tamamlandıktan sonra Stok Döviz Çevrim işlemi çalıştırılır. Bu işlem tüm stok hareketlerinin firma döviz tipi ve firma döviz tutarı sahalarının güncellenmesini sağlar.

![](../_assets/f119d47c9e9fd064f9a1.png)

Stok Döviz Çevrimi ile firma döviz tipi ve tutarlarının oluşturulduktan sonra Stok Enflasyon Düzeltme çalıştırılabilir. Bu işlem ile ilgili hareketlerden hesaplanan enflasyon fark tutarı E tipli hareket olarak kayıtlara geçer. Bu işlemin doğru çalışması için endekslerin indirilmiş olması gerekir.

![](../_assets/1a3c1f4c26ff4ec73da9.png)

31.01.2024 Enflasyon endeksi 3.035,59

```text
31.12.2023 Enflasyon endeksi 2.915,02
```

Taşıma katsayısı 3.035,59/2.915,02 =1,04136 olarak bulunur.

Giriş fiyatı ile endeks çarpılır ve enflasyon etkisindeki birim fiyata ulaşılır.

100 \* 1,04136= 104,136

Enflasyon etkisindeki birim fiyat giriş miktarıyla çarpılır ve enflasyon etkisindeki giriş tutarına ulaşılır.

104,136 \* 10= 1041,36

Enflasyon farkı; 1041,36- (100\*10)= 41,36 olarak bulunur.

![](../_assets/85796a41d568b77f49bc.png)

Enflasyon etkisi Ocak ayına yedirildikten sonra maliyet oluşturma çalıştırılır.

![](../_assets/c9c182176d30e1a0aa4d.png)

Reel maliyet 100 TL iken çıkış hareketi üzerinde sağ klik “Stok hareket Diğer Bilgiler” ekranından kontrol ettiğimizde

Firma Döviz Maliyetinde 104,14 enflasyon düzeltme tutarının dahil edildiği birim maliyeti görürüz.

![](../_assets/8d9f3b748d28d41877d1.png)

Bu aşamadan sonra ambar fişi muhasebeleştirme yapabiliriz. İşlem sonrasında enflasyon etkisindeki maliyet ile reel maliyet arasındaki fark tutarı çıkış miktarı kadar enflasyon fark hesaplarını çalıştırır.

![](../_assets/ad8bd5586dad44d6f010.png)

Oluşan fişte ;

![](../_assets/3daa3cb16dfb7997d153.png)

100\* 5 =500 reel maliyet üzerinden hesaplanan çıkış tutarı Ambar Çıkış Fişinde seçilmiş olan masraf hesabı ve alış hesabını borç / alacak olacak şekilde çalışır.

![](../_assets/cceaa4799c01a1720ded.png)

\[(enflasyon etkisindeki birim maliyet-gerçek maliyet)\*çıkış miktarı\] yani (104,136-100) \*5 = 20,68 düzeltilmiş maliyet ve reel maliyet arasındaki fark çıkış miktarı ile çarpılır ve masraf hesabı ile alış hesabının enflasyon fark hesabı borç/alacak çalışacak şekilde kapatılır.

![](../_assets/dc247b2cdf005432c39e.png)
