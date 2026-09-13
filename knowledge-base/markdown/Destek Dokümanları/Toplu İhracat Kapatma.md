---
title: "Toplu İhracat Kapatma"
page_id: "128583342"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Toplu İhracat Kapatma"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Toplu İhracat Kapatma"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTUxNjk2NDY3LWE4N2UtNDM0NS04YjNjLTk3NTAzMWJkOGNjOSZsaW5rPTA2ZGQwNTIwLTAzNDEtNGU4ZC1iYjk3LTFiNTQxMDk3NTFkNyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=51696467-a87e-4345-8b3c-975031bd8cc9&link=06dd0520-0341-4e8d-bb97-1b54109751d7&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "toplu-ihracat-kapatma_128583342_128583342.html"
source_version: "2023-12-25T11:27:46.087+03:00"
source_bytes: 1910818
fetched_at: "2026-09-13T04:23:02+00:00"
generator: "netsis-scraper 1.0.0"
---
# Toplu İhracat Kapatma

Toplu İhracat Kapatma hakkında ayrıntılı bilgiye bu dokümandan ulaşılır.

Toplu İhracat Kapatma menüsü ile dış ticaret modülü üzerinden girilen ihracat belgelerinin toplu kapatması yapılır.Gezgin\\Lojistik-Satış\\Dış Ticaret\\İşlemler\\İhracat İşlemleri menüsü altında yer alır. Toplu İhracat Kapatma erkanında kodu rehberinde çoklu seçim ve/veya tarih aralığı kısıtı verildikten sonra **Kayıtları** **Getir** butonuna basılarak gride kayıtlar getirilir.

![](../_assets/3a11a188e0dd677b5f41.png)

Grid ekranı dosya no, dosya tarihi, ihracat referans numarası, proforma tarih, cari kodu, cari adı, vb. kolonlarından oluşur. Grid akıllı grid özelliğine sahiptir. Ayrıca grid üzerinde sağ click\>Gönder\>Excel ile kayıtların excele gönderimi sağlanır.

![](../_assets/cd4bf5e0bba485c705c2.png)

Toplu ihracat kapatma yaparken aynı döviz cinsinden belgelerin bir arada kapatılması gerekmektedir. Farklı döviz cinslerinden dosyalar seçilirse **"Farklı** **döviz** **tipindeki** **kayıtlar** **birlikte**

**kapatılamaz"** uyarısı alınmaktadır.
![](../_assets/b843b7ccca94cca7f188.png)

**Tümünü Seç** butonuna basıldığında program ilk bulduğu belgenin döviz cinsi ne ise sonraki belgelerde o belgenin döviz cinsinden olan belgeleri işaretlemektedir. **Tümünü** **Kaldır** butonuna basıldığında ise, seçimli olan tüm belgelerin seçimi kaldırılmaktadır.

![](../_assets/499907c48cbecec90697.png)

İhracat kapatması yapılacak dosyalar seçildikten sonra **İleri** butonuna basılır.

İhracat kapatma bilgileri sekmesinde fiili ihracat tarihi günün tarihi gelir istenirse değiştirilir. Fiili kur bilgisi seçilen tarihe göre kur bilgisi getirilir.

İhracat dosyalarında navlun ve sigorta girilmişse, ilgili tutarların muhasebeye hangi hesaplara atılacaksa muhasebe kodları girilir.

Fatura numarası alanına girilen fatura numarasına göre program tarafından Resmi Fatura Numarası getirilir. Bedelsiz bir ihracat kapatma yapılıyorsa "**Bedelsiz** **Kapatma** **Yapılsın**" parametresi işaretlenmelidir.

Sonrasında İhracat Kapatma butonuna basılarak toplu ihracat kapatma gerçekleşir.
![](../_assets/fbb75fd4f271460351df.png)

Toplu kapatma işleminin sonucu ekrana detaylı bir şekilde gelmektedir. Hangi dosyalardaki hangi proformalar kapatıldı veya hangileri kapatılamadı, kapatılmama nedenleri detaylı bir şekilde listelenmektedir. Kapatılmadıysa fatura no kolonunda kapatılamama nedeni getirilmektedir. Düzeltmeler yapıldıktan sonra tekrar toplu kapatma ekranından kapatması yapılabilir

![](../_assets/a59795f09a784e02d224.png)
