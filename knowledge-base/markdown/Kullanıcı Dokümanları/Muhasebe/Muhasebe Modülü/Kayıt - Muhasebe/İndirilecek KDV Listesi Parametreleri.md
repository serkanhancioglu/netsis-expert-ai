---
title: "İndirilecek KDV Listesi Parametreleri"
page_id: "24740547"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Muhasebe"
  - "Muhasebe Modülü"
  - "Kayıt / Muhasebe"
  - "İndirilecek KDV Listesi Parametreleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / Kayıt / Muhasebe / İndirilecek KDV Listesi Parametreleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTcwYThmYTBjLWExOGMtNDhmZi1hNjM3LTExMmNkMDBmNmRmMSZsaW5rPTBiNjZlYzdkLTA3ZDctNGNiMC05ODQyLWRiNmI2M2Y4MWU1OCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=70a8fa0c-a18c-48ff-a637-112cd00f6df1&link=0b66ec7d-07d7-4cb0-9842-db6b63f81e58&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "indirilecek-kdv-listesi-parametreleri_41156709_24740547.html"
source_version: "2022-09-28T14:45:42.153+03:00"
source_bytes: 628637
fetched_at: "2026-09-13T04:13:01+00:00"
generator: "netsis-scraper 1.0.0"
---
# İndirilecek KDV Listesi Parametreleri

İndirilecek KDV Listesi Parametreleri, Muhasebe Bölümü'nde, "Kayıt/Muhasebe Modülü" menüsünün altında yer alır. İndirilecek KDV Listesi Parametreleri ekranı; Fatura, Kasa, Muhasebe, Dekont, Genel sekmelerinden oluşur. İndirilecek KDV Listesi’ne, Fatura, Kasa, Dekont ve Muhasebe modüllerinden girilmiş olan alış faturaları aktarılır. Aktarılan fatura kayıtlarının, girilecek kısıtlara göre getirilmesi için, "İndirilecek KDV Listesi Parametreleri" ekranı kullanılır. İndirilecek KDV Listesi Parametreleri bölümü sayesinde; İndirilecek KDV Listesi’ne, Fatura, Kasa, Dekont ve Muhasebe modüllerinden yapılan kayıtlardan hangilerinin ekleneceği ve hangi sıra ile görüntüleneceği belirlenir.

**Fatura**

![](../../../../_assets/e56a0baa8a6b0f5c9eda.png)

İndirilecek KDV Listesi Parametreleri ekranı Fatura sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| İndirilecek KDV Listesi Parametreleri Ekranı |  |
| --- | --- |
| Alış Faturası Girişlerinde İndirilecek KDV Bilgileri Alınsın | Alış faturası kaydı sırasında indirilecek KDV bilgilerinin bu ekranda belirlenecek kısıt ve sıralamalara göre alınması istendiği zaman işaretlenmesi gereken seçenektir. “Alış Faturası Sırasında İndirilecek KDV Bilgileri Alınsın” parametresi işaretlendiğinde, alış faturası saklandığında, alış irsaliyesi faturalandırma işlemi yapıldığında veya alış irsaliyelerini toplu faturalama işlemi sonucunda oluşan fatura bilgileri ile ilgili "İndirilecek KDV Bilgileri Ekranı" görüntülenir ve üzerinde düzeltme yapılabilir. |
| Saha Adı | Kısıt sekmesine Kısıt tıklanması ile görüntülenir. Fatura modülünde, indirilecek KDV bilgileri alınırken baz alınacak saha adı için kısıt verilen alandır. İlgili hücre üzerinde iken klavyede yer alan **Boşluk Çubuğuna** basılarak aktif hale gelen aşağı ok butonu, kısıt verilmesi istenen sahalara ulaşılmasını sağlar. İndirilecek KDV Listesi bölümüne, Fatura modülünden getirilecek alış faturaları için herhangi bir kısıt verilmesine gerek duyulmaması ile birlikte, istendiği zaman “Saha Adı” bölümünde bulunan fatura alanlarından herhangi biri kullanılarak kısıt verilebilir. **Örneğin,** "KDV’si 0’dan büyük olanlar aktarılsın" gibi. ![](../../../../_assets/457e16224ea9c7cc7900.png) |
| Sıralama | Faturaların ekrana aktarılma sırasının belirlenmesini sağlayan sekmedir. İlgili sıralama, sadece rapora getirilecek olan sıralamadır. Rapordaki verilerden Excel’e aktarım yapılırken, sıralama tarihe göre yapılır. **![](../../../../_assets/3019e04e59bb0513b52c.png)** |
| Kaydet | Girilen kısıtların kaydedilmesini sağlayan butondur. |

**Kasa**

İndirilecek KDV Listesine "Kasa" modülünden aktarılacak bilgiler, gider faturası olarak "Fatura" sekmesinden girilen kayıtlardır. Bu kayıtlarda, "B Formu" seçeneğinin işaretlenmesi koşulu aranır. "B Formu" seçeneği işaretli olmayan kayıtlar rapora getirilmez. "B Formu" alanının yanında yer alan "Cari Kodu" alanına bilgi girilmesi durumunda, oluşacak KDV listesine, cari hesaba ilişkin vergi dairesi ve vergi numarası gibi bilgiler de aktarılır.

**![](../../../../_assets/cc6601126f86c5802b4f.png)**

İndirilecek KDV Listesi Parametreleri ekranı Kasa sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| İndirilecek KDV Listesi Parametreleri Ekranı |  |
| --- | --- |
| Kasa Modülünde İndirilecek KDV Bilgileri Alınsın | Kasa modülünde girilen kayıt gride aktarıldıktan sonra, "İndirilecek KDV Bilgileri" ekranının görüntülenmesi ve üzerinde düzeltme yapılması için işaretlenen seçenektir. |
| Saha Adı | Kısıt sekmesine Kısıt tıklanması ile görüntülenir. Kasa modülünde, indirilecek KDV bilgileri alınırken baz alınacak saha adı için kısıt verilen alandır. İlgili hücre üzerinde iken klavyede yer alan **Boşluk Çubuğuna** basılarak aktif hale gelen aşağı ok butonu, kısıt verilmesi istenen sahalara ulaşılmasını sağlar. ![](../../../../_assets/3ec23b9411bc97447c6f.png) |
| Sıralama | Kasa kayıtlarının ekrana aktarılma sırasının belirlenmesini sağlayan sekmedir. İlgili sıralama, sadece rapora getirilecek olan sıralamadır. Rapordaki verilerden Excel’e aktarım yapılırken, sıralama tarihe göre yapılır. ![](../../../../_assets/c17dc7ed2541e4cd28a6.png) |
| Kaydet | Girilen kısıtların kaydedilmesini sağlayan butondur. |

**Muhasebe**

**![](../../../../_assets/07cdf282a013d8761863.png)**

İndirilecek KDV Listesi Parametreleri ekranı Muhasebe sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| İndirilecek KDV Listesi Parametreleri Ekranı |  |
| --- | --- |
| Yevmiye Fiş Girişinde İndirilecek KDV Bilgileri Alınsın | Yevmiye fiş kaydı gride aktarıldıktan sonra, "İndirilecek KDV Bilgileri" ekranının görüntülenmesi ve üzerinde düzeltme yapılması için işaretlenen seçenektir. |
| Saha Adı | Kısıt sekmesine Kısıt tıklanması ile görüntülenir. Muhasebe modülünde, indirilecek KDV bilgileri alınırken baz alınacak saha adı için kısıt verilen alandır. İlgili hücre üzerinde iken klavyede yer alan **Boşluk Çubuğuna** basılarak aktif hale gelen aşağı ok butonu, kısıt verilmesi istenen sahalara ulaşılmasını sağlar. ![](../../../../_assets/6a260d2f52561b855e25.png) |
| Sıralama | Yevmiye fiş kayıtlarının ekrana aktarılma sırasının belirlenmesini sağlayan sekmedir. İlgili sıralama, sadece rapora getirilecek olan sıralamadır. Rapordaki verilerden Excel’e aktarım yapılırken, sıralama tarihe göre yapılır. ![](../../../../_assets/b0b4e1195acfe977bfc3.png) |
| KDV Tutar Kısıt | Muhasebe kaydında KDV tutarının hangi satırdan getirileceğinin belirlendiği sekmedir. İlgili hücre üzerinde iken klavyede yer alan **Boşluk Çubuğuna** basılarak aktif hale gelen aşağı ok butonu, kısıt verilmesi istenen sahalara ulaşılmasını sağlar. **Insert** tuşu ile satır eklenir. ![](../../../../_assets/ff0377aee05f7a4abf91.png) |
| Gruplama | Aynı yevmiye fişinde birden fazla belge bulunması durumunda, tutarların neye göre gruplandırılacağı belirlenir. Hepsini seç butonu ![](../../../../_assets/791c70a62e1a8ade02a1.png) ile, gruplama yapılacak alanların hepsinin işaretlenmesi, hepsini sil butonu ![](../../../../_assets/76e42b0269d9532b9a8d.png) ile de seçilen tüm gruplama alanlarının işaretinin kaldırılması sağlanır. ![](../../../../_assets/1de975c2dbc8ade1eea2.png) |
| Kaydet | Girilen kısıtların kaydedilmesini sağlayan butondur. |

**Dekont**

![](../../../../_assets/27c847e8b940369fa6a3.png)

İndirilecek KDV Listesi Parametreleri ekranı Dekont sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| İndirilecek KDV Listesi Parametreleri Ekranı |  |
| --- | --- |
| Dekont Modülünde İndirilecek KDV Bilgileri Alınsın | Dekont kaydı gride aktarıldıktan sonra, "İndirilecek KDV Bilgileri" ekranının görüntülenmesi ve üzerinde düzeltme yapılması için işaretlenen seçenektir. |
| Saha Adı | Kısıt sekmesine Kısıt tıklanması ile görüntülenir. Muhasebe modülünde, indirilecek KDV bilgileri alınırken baz alınacak saha adı için kısıt verilen alandır. İlgili hücre üzerinde iken klavyede yer alan **Boşluk Çubuğuna** basılarak aktif hale gelen aşağı ok butonu, kısıt verilmesi istenen sahalara ulaşılmasını sağlar. ![](../../../../_assets/9b093f0df5d4fdc27fc5.png) |
| Sıralama | Dekont kayıtlarının ekrana aktarılma sırasının belirlenmesini sağlayan sekmedir. İlgili sıralama, sadece rapora getirilecek olan sıralamadır. Rapordaki verilerden Excel’e aktarım yapılırken, sıralama tarihe göre yapılır. ![](../../../../_assets/85e1807d1af0b2ac3b39.png) |
| KDV Tutar Kısıt | Dekont kaydında, KDV tutarının hangi satırdan getirileceğinin belirlendiği sekmedir. ![](../../../../_assets/fc2ede01db10b42124b3.png) |
| Gruplama | Aynı dekont kaydında birden fazla belge olması halinde, tutarların neye göre gruplandırılacağı belirlenir. Hepsini seç butonu ![](../../../../_assets/791c70a62e1a8ade02a1.png) ile, gruplama yapılacak alanların hepsinin işaretlenmesi, hepsini sil butonu ![](../../../../_assets/76e42b0269d9532b9a8d.png) ile de seçilen tüm gruplama alanlarının işaretinin kaldırılması sağlanır. Öncelikli olarak "Dekont No" ve Fiş No alanları işaretli şekilde ekrana gelir. Bunun dışında bir alan kullanılması istendiğinde değişiklik yapılabilir. ![](../../../../_assets/45a1f1ab0ba5156cfea1.png) |
| Kaydet | Girilen kısıtların kaydedilmesini sağlayan butondur. |

Dekonttan girilen kayıtların, İndirilecek KDV Listesine aktarılması için, gider kaleminin bulunduğu satırda "B Formu" parametresini işaretlenmesi ve "Cari Kodu" alanınına bilgi girilmesi gerekir. KDV Matrahı, gider satırındaki tutar olarak rapora aktarılır. Aynı satırda KDV tutarı da girilmişse, bu tutar da rapora aktarılır. KDV'nin ayrı satırda girilmesi halinde, "KDV Tutar Kısıtları" sekmesinden girilecek kısıtlar yardımı ile rapora aktarılır.

**Genel**

**![](../../../../_assets/b08c678bcb16b136c40a.png)**

İndirilecek KDV Listesi Parametreleri ekranı Genel sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| İndirilecek KDV Listesi Parametreleri Ekranı |  |
| --- | --- |
| Malın Cinsi Sahası Karakter Sınırını Aştığında Kullanılacak Değer | "Malın Cinsi" alanında karakter sınırının aşıldığı durumlarda kullanılacak değerin tanımlandığı alandır. |
| Sadece KDV'li Satırlar Dikkate Alınsın | İndirilecek KDV listesi alınırken sadece KDV'li satırların dikkate alınması istendiğinde işaretlenen parametredir. |
| Kaydet | Girilen kısıtların kaydedilmesini sağlayan butondur. |
