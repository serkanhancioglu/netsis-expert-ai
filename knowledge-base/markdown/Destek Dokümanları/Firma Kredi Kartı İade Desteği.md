---
title: "Firma Kredi Kartı İade Desteği"
page_id: "160039435"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Firma Kredi Kartı İade Desteği"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Firma Kredi Kartı İade Desteği"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWZlMDRhNDA1LTlkNjUtNDdlOC1iYTNjLTdmZjRlOTAyMjVjMiZsaW5rPTc1YWNiNmUwLWE0MDgtNDdmNC1iNDdjLWZhZDYwMzhmMmE5MCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=fe04a405-9d65-47e8-ba3c-7ff4e90225c2&link=75acb6e0-a408-47f4-b47c-fad6038f2a90&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "firma-kredi-karti-iade-destegi_160039435_160039435.html"
source_version: "2024-12-10T15:57:34.800+03:00"
source_bytes: 825540
fetched_at: "2026-09-13T04:22:28+00:00"
generator: "netsis-scraper 1.0.0"
---
# Firma Kredi Kartı İade Desteği

9.0.53 seti ile birlikte Firma Kredi Kartı İade uygulaması programda desteklenmiştir.

Bu özellik ile ödemesi firma kredi kartı ile gerçekleşen alış faturalarına ait iade işlemleri ile birlikte ilgili alış belgesine ait Firma Kredi Kartı Kayıtları' ndaki kayıtlar içinde iade işlemlerinin yapılabilmesi sağlanmıştır. Bunun için öncelikle Satış Fatura Parametreleri ekranında Genel 4 altında "Alıştan İadeler Detaylı Takip Edilsin" parametresinin işaretlenmesi gerekmektedir.

![](../_assets/fc1e39f100a59fcf8f76.png)

Bu parametrenin işaretlenmesi ile birlikte iade tipli satış faturalarının tamamlanması sırasında Detaylı İade Fatura Bilgileri ekranı açılarak ilgili satış iade faturasının hangi alış faturasına karşılık düzenlendiğini eşleştirip ilgili iade kayıtları oluşturulmaktadır.

Aynı zamanda Geri Ödeme Detay Bilgileri ile birlikte ilgili ödeme kayıtlarının iade işlemleri de gerçekleştirilmektedir.

![](../_assets/77ea8fbc9c5f6f639a7d.png)

Detaylı İade Fatura Bilgileri ekranından ilgili satış faturasına ait iade işleminin hangi alış faturasını kaynak alacağı Kaynak Fatura alanındaki rehberden seçilerek belirlenmektedir. Rehbere tıklandığında ilgili cariye ait alış faturaları listelenmektedir. Bu ekranda doğru belgenin seçilebilmesi için program fiyat ve miktar kontrolü yapmaktadır. İade tipli satış belgesinde girilen fiyat ve miktar bilgisi kaynak belgedeki miktar ve fiyat bilgisi ile satır bazında kontrol edilmektedir. Bunlar arasında farklılık olması durumunda program kullanıcıya uyarı vermektedir.

![](../_assets/21d1e26d5b93a5c742ee.png)

Detaylı İade Fatura Bilgileri ekranında Geri Ödeme Detayı-İade Ödeme Türü alanından alış faturasına ait ödeme kayıtları girildi ise bunun iade işlemi esnasında nasıl bir iade gerçekleştirileceğinin belirlendiği alandır.

Bu ekranda İade Tutarı bölümünde ne kadarlık bir tutarda iade işlemi olacaksa bu bilgi girilmektedir. Kalem tutarı alanında ilgili kaynak belgenin kalem tutarının izlendiği alandır. Bu ekranda kalem tutarı ile iade tutarı eşit olana kadar iade kayıtlarının girilmesi gerekmektedir.

![](../_assets/90f3961f57d9c316aa74.png)

İlgili alış faturasına ait daha önce girilen nakit ve firma kredi kartı ile gerçekleşen ödeme kayıtları eklenmektedir. İade türü alanında ödemede kullanılan firma kredi kartı no listeye gelmektedir.
![](../_assets/53527a94944bf1cb955c.png)

İade tipli satış belgesinde Kaynak Fatura seçimi ve İade Ödeme Türü girişi tamamlanıp Tamam tuşuna basıldıktan sonra program ilgili kayıtları düzenleyerek daha önce 4000 TL nakit 6000 TL 3 taksit olarak yapılan ödeme kayıtlarının aynı olacak şekilde iade işlemlerini kaydetmektedir. İlgili iade hareketleri ödeme kayıtlarında olduğu gibi cari hareket kayıtlarından izlenebilmektedir.

![](../_assets/50a5b9b5234650df5b46.png)

Aynı zamanda Banka Hesap Hareketleri ekranından da ilgili iade kayıtlarının borç tutarlarına işlendiği görülmektedir.

![](../_assets/e9254bdb0cd3fc343e89.png)

İade işleminden sonra Firma Kredi Kartı Ödeme Kayıtları ekranında iade yapılan dönemde ödeme kaydı olmadığı halde Ödenen Kayıtları Getir denerek hazırlık çalıştırıldığında iadeye ait tutar ve iade tarihi bilgisi görülmektedir.

![](../_assets/1dfe3c56bd2ac57b61b5.png)
