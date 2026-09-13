---
title: "e-Fatura Gelen Kutusu Kısıdı"
page_id: "47084816"
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
  - "e-Fatura Gelen Kutusu Kısıdı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Fatura / Kayıt / Fatura / E-Fatura İşlemleri / e-Fatura Gelen Kutusu Kısıdı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTM3ZDBkZTMwLTlhYzItNDliYy05YzUyLTM2MTIwNzVlNjBjZSZsaW5rPThjNDUwZjVmLTg3MzQtNGE0Yy04ZWZiLTFmNmY0MjQ5N2UxMyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=37d0de30-9ac2-49bc-9c52-3612075e60ce&link=8c450f5f-8734-4a4c-8efb-1f6f42497e13&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "e-fatura-gelen-kutusu-kisidi_47084821_47084816.html"
source_version: "2022-10-24T13:41:17.347+03:00"
source_bytes: 3300
fetched_at: "2026-09-13T04:02:08+00:00"
generator: "netsis-scraper 1.0.0"
---
# e-Fatura Gelen Kutusu Kısıdı

e-Fatura Gelen Kutusu Kısıdı, kullanıcı ya da grup bazında kısıt verilerek, gelen kutusundaki e-Faturaların görüntülenmesi için kullanılan bölümdür.

e-Fatura Gelen Kutusu Kısıdı ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| e-Fatura Gelen Kutusu Kısıdı Ekranı |  |
| --- | --- |
| Kısıt Kapsamı | Gelen kutusundaki e-Faturaların görüntülenmesi için kısıt verilen alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile, Grup veya Kullanıcı seçenekleri arasından seçim yapılır. |
| Kullanıcı Kodu | "Kısıt Kapsamı" alanında "Kullanıcı" seçildiğinde aktif hale gelen alandır. Kullanıcı kodunun girilmesini sağlar. |
| Grup Kodu | "Kısıt Kapsamı" alanında "Grup" seçildiğinde aktif hale gelen alandır. Grup kodunun girilmesini sağlar. |
| Veritabanı Nesnesi | Gelen kutusundaki e-Faturaların görüntülenmesi için veritabanı nesnesi kısıdı verilen alandır. |
| Saha Adı | Veritabanı nesnesi için bilgi girişi yapıldıktan sonra ilgili "Saha Adı" için kısıt verilen alandır. |

**Örnek-1**

1 numaralı kullanıcının, sadece 5.000 TL üzeri e-Faturaları görüntülemesi,

2 numaralı kullanıcının, Grup Kodu A olan carilere ait e-Faturaları görüntülemesi için kısıt verilebilir.

Herhangi bir kısıt verilmezse, tüm kullanıcılar tüm e-Faturaları görüntüleyebilir.

**Örnek-2**

Kısıt Kapsamı: Kullanıcı

Kullanıcı Kodu:50

Veritabanı Nesnesi: TBLCASABIT

Saha Adı: CARI_KOD

Kısıt Alanı: ='S2013'

şeklinde bilgi girişi yapıldığında; 50 numaralı kullanıcının, gelen kutusunda sadece S2013 carisine ait e-Faturaları görüntülemesi sağlanır.
