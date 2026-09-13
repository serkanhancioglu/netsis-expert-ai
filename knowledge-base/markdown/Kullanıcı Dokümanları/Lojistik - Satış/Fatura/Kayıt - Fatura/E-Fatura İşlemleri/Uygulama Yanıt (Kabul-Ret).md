---
title: "Uygulama Yanıt (Kabul/Ret)"
page_id: "47084732"
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
  - "E-Fatura İşlemleri"
  - "Uygulama Yanıt (Kabul/Ret)"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Fatura / Kayıt / Fatura / E-Fatura İşlemleri / Uygulama Yanıt (Kabul/Ret)"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWJjMzNmY2Q1LTY2NzUtNDIzZC1iNTA4LWZhNTQyMjA2YTE2MiZsaW5rPTFiZjA4OWZkLWQ3YWQtNDg2My05NzI3LWZhNDA5Nzk0MjdhYiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=bc33fcd5-6675-423d-b508-fa542206a162&link=1bf089fd-d7ad-4863-9727-fa40979427ab&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "uygulama-yanit-kabul-ret_47084737_47084732.html"
source_version: "2022-10-24T13:38:32.203+03:00"
source_bytes: 18506
fetched_at: "2026-09-13T04:02:05+00:00"
generator: "netsis-scraper 1.0.0"
---
# Uygulama Yanıt (Kabul/Ret)

Gelen Ticari Fatura, "Uygulama Yanıt Kabul\\Ret" ekranına düşer. Gelen kutusu fatura bazlı liste ekranında, ticari fatura üzerinde iken farenin sağ klik tuşu ile görüntülenen "Uygulama Yanıt (Kabul/Ret)" seçeneği ile uygulama yanıtının iletilebileceği gibi, bu ekran üzerinden de faturalara ait yanıt bilgisi iletilebilir. Gelen tüm ticari faturalar detaylı şekilde - GİB Fatura Numarası, Tarih, Fatura Tipi, Zarf Numarası, Basım Bilgisi, UUID, Kabul/Ret Durumu, Kayıt Tarihi - görüntülenir.

Uygulama Yanıt (Kabul/Ret) ekranı; Faturalar ve Taslaklar (e-Fatura) sekmesinden oluşur.

**Faturalar**

Uygulama Yanıt (Kabul/Ret) ekranı Faturalar sekmesindeki butonlar ve içerdiği bilgiler şunlardır:

| Uygulama Yanıt (Kabul/Ret) Ekranı |  |
| --- | --- |
| ![](../../../../../_assets/d15ca1ad68365b9a1a84.png) Tümü Seç Butonu | Gelen faturaların hepsinin seçilmesini sağlayan butondur. |
| ![](../../../../../_assets/9f77dcdb92897fa07bf9.png) Seçimleri Kaldır Butonu | Seçilen faturaların, seçimlerinin kaldırılmasını sağlayan butondur. |
| ![](../../../../../_assets/b6684d1cadab5da9413e.png) Seçilenler Kabul Butonu | Seçilen faturaların kabul edilmesini sağlayan butondur. |
| ![](../../../../../_assets/33ae8ce547ad4b4cb9c1.png) Seçilenler Ret Butonu | Seçilen faturaların reddedilmesini sağlayan butondur. |
| ![](../../../../../_assets/86bb575f446b6ff6f8d4.png) Yenile Butonu | Ekranın yenilenmesini ve gelmeyen kayıt varsa gelmesini sağlayan butondur. |
| ![](../../../../../_assets/9487c7f0eacf4833a039.png) Taslak Oluştur Butonu | Verilen yanıta ait XML dosyasının mühürlenerek oluşturulmasını sağlayan butondur. |
| İşlem Özeti | Yanıta ait taslak oluşturulurken, işleme ait log sonucunun görüntülendiği alandır. |

Faturalar üzerinde fare ile çift tıklandığında XSLT detaylı fatura görüntüsü alınır. e-Fatura görüntüsü alındıktan sonra dışarı aktarılabilir, e-Posta gönderilebilir ve basım yapılabilir.

e-Fatura görüntülendikten sonra, faturanın sol alt köşesinde yer alan kabul/ret alanı ile yanıt verilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/768482f0-c858-402a-bf15-5fa88f1ca333/uygulamayanıtkabulred1.png)

Faturaya ait yanıtın taslağı oluşturulduğunda "Taslaklar" sekmesinde listelenir.

**Taslaklar (e-Fatura)**

Uygulama Yanıt (Kabul/Ret) ekranı Taslaklar sekmesindeki butonlar ve içerdiği bilgiler şunlardır:

| Uygulama Yanıt (Kabul/Ret) Ekranı |  |
| --- | --- |
| ![](../../../../../_assets/d15ca1ad68365b9a1a84.png) Tümü Seç Butonu | Taslaktaki faturaların hepsinin seçilmesini sağlayan butondur. |
| ![](../../../../../_assets/9f77dcdb92897fa07bf9.png) Seçimleri Kaldır Butonu | Seçilen faturaların, seçimlerinin kaldırılmasını sağlayan butondur. |
| ![](../../../../../_assets/cc908c3c9a5c1e33cd42.png) Taslak Sil Butonu | Taslak listesinde oluşturulan yanıtın değiştirilmesi için kullanılan butondur. Bu işlem ile, oluşan taslaklara ait faturalar, "Faturalar" sekmesine geçer. |
| ![](../../../../../_assets/a80136e472f79a3a32e2.png) Gönder Butonu | Taslağı oluşturulan faturaların, zarf olarak gönderilmesini sağlayan butondur. |
