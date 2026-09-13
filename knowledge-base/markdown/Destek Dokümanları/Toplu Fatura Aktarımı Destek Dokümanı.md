---
title: "Toplu Fatura Aktarımı Destek Dokümanı"
page_id: "78282760"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Toplu Fatura Aktarımı Destek Dokümanı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Toplu Fatura Aktarımı Destek Dokümanı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTIwYjliMmE0LTJlYWMtNGZmNS1iMmMzLWRmMTY4ODg0YjZlMCZsaW5rPTUxZWQwZjdlLWM1NTctNDRmYS1hMDA3LTlmNjkwNWJjY2QzMSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=20b9b2a4-2eac-4ff5-b2c3-df168884b6e0&link=51ed0f7e-c557-44fa-a007-9f6905bccd31&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "toplu-fatura-aktarimi-destek-dokumani_80087441_78282760.html"
source_version: "2022-11-02T14:46:20.870+03:00"
source_bytes: 1078840
fetched_at: "2026-09-13T04:24:12+00:00"
generator: "netsis-scraper 1.0.0"
---
# Toplu Fatura Aktarımı Destek Dokümanı

Toplu Fatura Aktarımı ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

9028 setiyle birlikte, alış ve satış faturalarının Json formatta istenen klasöre toplu olarak aktarılması ve ilgili dosyadan da toplu olarak içeri alınması desteklenmiştir. Toplu Fatura Aktarımı, Fatura Modülü/İşlemler/**Toplu Fatura Aktarımı** menüsü üzerinden yapılmaktadır. Toplu Fatura Aktarımı ekranı, **Dışarı Aktar** ve **İçeri Aktar** olmak üzere 2 sekmeden oluşmaktadır. **Dışarı Aktar** sekmesinde, **Dosya Yolu** kısmında belirtilen dizine belge tipi, tarih aralığı, fatura numarası ve cari kodu alanlarına göre verilen kısıtlara uyan faturaların, json formatında aktarımı sağlanmaktadır.
![](../_assets/6d470cff52bc9abbe0a7.png)
Belge tipi, tarih aralığı, fatura numarası ve cari kodu alanlarına göre kısıtlar verildikten sonra **Kayıtları Getir** butonuna basılarak kısıtlara uyan belgeler listelenir. Sonrasında json formatında kaydedilecek belgeler seçildikten sonra **Dosya** **Kaydet** butonuna basılır. "**Seçtiğiniz** **belgeler** **dosya haline getirilecektir, emin misiniz?**" uyarı mesajına "**Evet**" dendikten sonra, "**Aktarım tamamlandı**" uyarı mesajı ile faturalar json formatında belirtilen dizine kaydedilmiş olur.
![](../_assets/f7fa7a7cf4a27e15aa0c.png)
![](../_assets/6ee48851ca2d3b839f3f.png)
**İçeri Aktar** sekmesinde, toplu bir şekilde json formatındaki dosyaları fatura olarak içeri alınması sağlanmaktadır. **Dosya yolu** kısmında, içeri alınmak istenen json formatındaki dosya seçilir. **Kayıtları Getir** butonuna basılarak, json dosyasında bulunan fatura belgeleri listelenir. İçeri aktarılmak istenen belgeler seçildikten sonra **Belge Kaydet** butonuna basılır.
![](../_assets/10a22563b9b3b0f1beab.png)
Sonrasında, ekrana içeri aktarılmak istenen belgelerin numara ve seri bilgilerinin girildiği **Yeni** **Numara Girişi** başlıklı ekran gelir. "**Öncelikle** **Kaynak** **Belge** **Numarasını** **ve** **Serisini** **Kullan**" parametresi işaretlenirse, listede yer alan belgeler, fatura no kolonunda yazan fatura numaraları ile içeri alınacaktır. Eğer bu numaralar netsis içinde varsa, bu durumda ilgili serinin son numarası bulunarak sıradaki numara verilerek aktarım yapılacaktır. "Öncelikle Kaynak Belge Numarasını ve Serisini Kullan" parametresi işaretlenmeyip, **Fatura Serisi** alanına bir seri girilmesi durumunda netsise aktarılacak belgelerin numaraları burada girilen serinin son numarası bulunarak sıradaki numara verilerek faturaların içeri alımı sağlanmaktadır.
![](../_assets/4f3aaf9754e1da336e74.png)
![](../_assets/22f43c3cc841fcec0a5f.png)
Aktarım sonrasında herhangi bir sorun yoksa, durum kolonunda "**Aktarıldı**" yazmaktadır. Eğer aktarım sırasında bir hata varsa, hata detayı durum kolonunda yazar. İçeriye aktarılan faturaların yeni numaraları da **Netsis Belge No** kolonunda yazmaktadır. Ayrıca Netsis Belge No kolonunda link desteği de bulunmaktadır. Fatura numarasına tıklandığında ilgili belge içeriğine gidilmektedir.
![](../_assets/55da9830bc61d8c1681a.png)
