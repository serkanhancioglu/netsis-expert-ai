---
title: "Yabancı Para Cinsinden Defter Tutan Mükellefler İçin Defter Oluşturma"
page_id: ""
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Yabancı Para Cinsinden Defter Tutan Mükellefler İçin Defter Oluşturma"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Yabancı Para Cinsinden Defter Tutan Mükellefler İçin Defter Oluşturma"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTFjMDI5OTY5LTA4YmItNDBiNi1iY2EwLTgwNjUyYjZmYjJiNyZsaW5rPTViNzY5NzFlLTAxZGItNGRiNC05YzYzLTFkNDMwZWE3ZDlkYSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=1c029969-08bb-40b6-bca0-80652b6fb2b7&link=5b76971e-01db-4db4-9c63-1d430ea7d9da&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "yabanci-para-cinsinden-defter-tutan-mukellefler-icin-defter-olusturma.html"
source_version: ""
source_bytes: 8115
fetched_at: "2026-09-13T04:22:10+00:00"
generator: "netsis-scraper 1.0.0"
---
# Yabancı Para Cinsinden Defter Tutan Mükellefler İçin Defter Oluşturma

Türk Ticaret Kanunu ve Vergi Usul Kanunu’na göre, işletmeler kayıtlarını Türk Lirası ile tutmalıdır. Ancak, belirli şartları sağlayan yabancı sermayeli şirketler ile serbest bölgelerdeki firmalara, yabancı para cinsinden defter tutma imkânı sağlanmıştır.

Ana para biriminin yabancı para birimi olduğu ve defterin yabancı para biriminden tutulacağı senaryoda:

- Döviz uygulaması açık olmalıdır.
- Mükellef ve Düzenleyen Bilgileri / Defter Bilgileri ekranından E-Defterin Tutulduğu Para Birimi belirlenir.
- Farklı para birimlerinde yapılan dövizli işlemlerde TCMB Çapraz Kur (parite) kullanılarak kayıt yapılır. Mükellef ve Düzenleyen Bilgileri / Defter Bilgileri ekranından Kaynak Döviz Kuru alanına Çapraz Kur bilgisi girilmelidir.
- E-Defter onaylama ekranında Döviz Değerleri Oluşturulsun parametresi işaretlenerek defter oluşturulmalıdır.

Örnek bir senaryo ile anlattıklarımız görselleştirip, sonuçlarını yorumlayalım.

**Senaryo**

Ana para birimi EURO olan bir şirketin defteri EURO cinsinden tutulacak ve farklı para birimlerinde işlem yapılacaktır.

- Ana para biriminin EURO olması, uygulama içindeki tüm fiyat alanlarında EURO değerlerinin tutulduğu anlamına gelir. Varsayılanda Türk Lirası değerleri için kullandığımız bu sahalar, ana para birimi yabancı para birimi olduğunda ilgili döviz türüne hizmet eder.
- Mükellef ve Düzenleyen Bilgileri / Defter Bilgileri ekranında E-Defter'in Tutulduğu Para Birimi EURO, Kaynak Döviz Kuru ise bu senaryoda parite kullanılacağı için TCMB Çapraz Kur olarak belirlenir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/490997ae-09a5-4ce8-b23d-a88ca5a6ece5/ddmukellef.jpg)

Ana para biriminden ve farklı bir para biriminden 2 fatura girilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/55e6b778-1e7c-4afc-a4d4-17740b2eac49/dd1nolufat.jpg)

000000000000001 No’lu fatura ana para biriminden 10.000 Euro olarak girilmiştir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/f5e05429-fdc5-453d-8885-e9ad459f51cb/dd2nolufat.jpg)

000000000000002 No’lu fatura Dolar para birimi kullanılarak kaydedilmiştir. Döviz Fiyat sahasına 1.000 Dolar, döviz kuruna günün Euro/Dolar paritesi olan 0,92 girilmiş ve Euro karşılığı olarak 920 Euro hesaplamıştır.

<u>Defter oluşturma;</u>

E-Defter Onaylama ekranında Döviz Değerleri Oluşturulsun parametresi işaretlenerek defter oluşturulur. Bu aşamada program Mükellef ve Düzenleyen Bilgileri / Defter Bilgileri ekranından E-Defterin Tutulduğu Para Birimi olan Eur biriminden defter oluşturulacağı bilgisini verir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/b17d54d7-a39a-4362-a934-bd6fac5f2f15/ddDEFTERONAYLAMA.jpg)

Oluşan defterin yorumlanması;

Yevmiye kayıtları, detaylı olarak yevmiye XML dosyasında yer alır. Defter, yevmiye ve yevmiye özel olarak iki farklı formatta görüntülenir. GİB’e gönderilecek dosya yevmiye.xml dosyasıdır.

Yevmiye.xml dosyasının görüntüsünde para birimi yer almaz. Ancak, XML dosyasındaki UNITREF taginde EUR bilgisi bulunur. Defterin para birimi, bu tagden anlaşılır.

Borç ve alacak sütunlarındaki tutarlar, ana para birimi olan EURO cinsindendir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/0fe6f96c-a3d7-41ed-a09f-057126cdbf11/ddyevmiyehtml.jpg)

Yevmiye kayıtlarının dövizli bilgileri, yevmiye özel XML dosyasında yer alır ve sadece görüntüleme amacıyla kullanılır; GİB’e yüklenmez.

Borç ve Alacak sütunlarındaki tutarlar, girilen para birimi olan Doların, parite aracılığıyla hesaplanmış EURO karşılığıdır. Döviz Borç ve Alacak sütunlarında, girilen Dolar tutarları yer alır.

Kur sütunu, bu örnekte pariteyi gösterir. Kur Detay sütunu ise kullanılan kurun hangi işlem tarihinde hangi kaynak kurdan hesaplandığını gösterir. Kur detay, işlemin tarihi ve Mükellef Düzenleyen Bilgileri / Defter Bilgileri ekranındaki Kaynak Döviz Kuru alanındaki verilerden oluşur.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/1a98ba0a-6d6d-409a-80b1-4a7ebf241cc5/ddyevmiyeozelhtml.jpg)
