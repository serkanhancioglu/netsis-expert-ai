---
title: "Kalite Kontrol Departman Girişi"
page_id: "22804119"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Kalite - Kontrol"
  - "Kayıt / Kalite Kontrol"
  - "Kalite Kontrol Departman Girişi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Kalite - Kontrol / Kayıt / Kalite Kontrol / Kalite Kontrol Departman Girişi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTdkNmJkOGI5LTg3MzQtNDVlYS1hZGQ1LWUxYzI5MjMxYjljZSZsaW5rPTk5Njg5M2QxLTc3NTktNDc0MS04ODE1LWE5YzNlZTgxZmMzOSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=7d6bd8b9-8734-45ea-add5-e1c29231b9ce&link=996893d1-7759-4741-8815-a9c3ee81fc39&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "kalite-kontrol-departman-girisi_22804677_22804119.html"
source_version: "2022-10-24T17:26:20.003+03:00"
source_bytes: 49700
fetched_at: "2026-09-13T04:06:24+00:00"
generator: "netsis-scraper 1.0.0"
---
# Kalite Kontrol Departman Girişi

Kalite Kontrol Departman Girişi, Kalite Kontrol yapılan departmana ait bilgi girişinin yapıldığı bölümdür. Lojistik - Satış Bölümü'nde, "Kayıt/Kalite Kontrol" menüsünün altında yer alır.

![](../../../../_assets/ae14419b1b2acc0d8370.png)

Kalite Departman Kayıtları ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Kalite Kontrol Departman Kayıtları Ekranı |  |
| --- | --- |
| Departman Kodu | Kalite kontrol yapılan her departman için kod tanımlamasının yapıldığı alandır. En fazla 8 karakterlik alfa sayısal kod kullanılabilir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, departman kodları izlenebilir. |
| Departman Tipi | Kalite kontrol işlemleri için 4 farklı departman tipi belirlenir; Satınalma, Üretim, İade ve Diğer. Satın alma, Üretim ve İade tipli departman tipleri; irsaliye, fatura ya da iş emri gibi belgelere bağlı, ölçüm detayı içeren kalite kontrol işlemleri için kullanılır. Diğer tipi ise; ölçüm detayı içermeyen kalite kontrol kayıtları girmek için kullanılır. **Örneğin:** Satış sonrası servis kayıtları. Aynı departman tipi için, birden fazla departman tanımlaması yapılabilir. **Örneğin:** Metal levha ve motor satın alan bir firmadaki iki ürünün kalite kontrolü, satın alma departmanın farklı birimleri tarafından yapılıyor olabilir. Bu durumda, departman tipi satın alma olan iki farklı departman tanımı yapılması gerekir. Aşağı ok tuşu yardımı ile departman tipleri izlenebilir. |
| Açıklama | Kalite kontrol yapılan departmanlara ait 50 karakterlik açıklama bilgisinin girildiği alandır. |
| Seri Karakter | Departman bazında, kalite kontrol numaralarına ait başlangıç seri karakterinin girildiği alandır. Kalite kontrol kayıtları, bu alana girilen seri karakter ile başlar. Tek karakterlik, sayısal ya da alfa sayısal seriler belirlenebilir. **Örneğin:** Satın alma departmanı için, seri karakteri “S” olarak belirlendiğinde, kalite kontrol numaraları S0000001, S0000002.. şeklinde oluşur. |
| Depo Kodu | Satın alma ve iade işlemlerine ait kalite kontrol kayıtları için, alış irsaliyesi ile mal girişinin yapıldığı depo kodunun girildiği alandır. Üretim işlemlerine ait kalite kontrol kayıtları için, üretim sonu kayıtlarında kullanılan giriş depo kodu da bu alana yazılır. Alış irsaliyesindeki giriş depo kodu, bu alana girilen depo kodundan farklı ise, satın alma ve iade tipli kalite kontrol kayıtları sırasında bu tür kayıtlara ulaşılamaz. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, depo kodları izlenebilir. Bu depoların, önceden Stok Modülü-Kayıt-Lokal Depo İşlemleri-Depo Tanımlama bölümünden tanımlanmış olması gerekir. |
| Kabul Depo Kodu | Kalite kontrol kayıtları sonucunda kabul edilen malların girişinin yapıldığı üretim/satış depo kodunun girildiği alandır. Departman bazında, farklı kabul depolarına giriş yapılabilir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, kabul depo kodları izlenebilir. Bu alana girilen kod, sonraki aşamalarda “Kabul KK DAT” işlemi sırasında kullanılacak ve kabul edilen malların depolar arası transfer işlemi ile kabul deposuna aktarımı sağlanacak. Bu depoların, önceden Stok Modülü-Kayıt-Lokal Depo İşlemleri-Depo Tanımlama bölümünden tanımlanmış olması gerekir. |
| Red Depo Kodu | Kalite kontrol kayıtları sonucunda reddedilen malların girişinin yapıldığı hurda/iade depo kodunun girildiği alandır. Departman bazında, farklı red depolarına giriş yapılabilir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, red depo kodları izlenebilir. Bu alana girilen kod, sonraki aşamalarda “Red KK DAT” işlemi sırasında kullanılacak ve kabul edilen malların depolar arası transfer işlemi ile red deposuna aktarımı sağlanacak. |
| Hurda Depo Kodu | Kalite kontrol kayıtları sonucu, kontrolü yapılan stokların test edilmesi sırasında kullanılamaz hale gelen (hurda) malların depo kodu girişinin yapıldığı alandır. Departman bazında, farklı hurda depolarına giriş yapılabilir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hurda depo kodları izlenebilir. Bu alana girilen kod, sonraki aşamalarda “Red KK DAT” işlemi sırasında kullanılacak ve kabul edilen malların depolar arası transfer işlemi ile hurda deposuna aktarımı sağlanacak. |
| Şartlı Kabul Depo Kodu | Kalite kontrol kayıtları sonucunda şartlı kabul edilen malların girişinin yapıldığı üretim/satış depo kodunun girildiği alandır. Departman bazında, farklı şartlı kabul depolarına giriş yapılabilir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, şartlı kabul depo kodları izlenebilir. Bu alana girilen kod, sonraki aşamalarda “Şartlı Kabul KK DAT” işlemi sırasında kullanılacak ve şartlı kabul edilen malların depolar arası transfer işlemi ile kabul deposuna aktarımı sağlanacak.<br>Bu depoların, önceden Stok Modülü-Kayıt-Lokal Depo İşlemleri-Depo Tanımlama bölümünden tanımlanmış olması gerekir. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır.

Kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
