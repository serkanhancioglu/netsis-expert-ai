---
title: "Sayım Farkını Hücre Hareketlerine İşleme"
page_id: "22803883"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Dinamik Depo"
  - "Kayıt / Dinamik Depo"
  - "Hücre Sayım İşlemleri"
  - "Sayım Farkını Hücre Hareketlerine İşleme"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Dinamik Depo / Kayıt / Dinamik Depo / Hücre Sayım İşlemleri / Sayım Farkını Hücre Hareketlerine İşleme"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWIxNGRkYWU0LWRiMTMtNDFjZS1iOGVjLWExMWFhNTBmNDU0YSZsaW5rPWU3NzUxOGZmLWJlNDYtNGQ3NS04MDU4LTM5MzVkODBjMDFhZiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=b14ddae4-db13-41ce-b8ec-a11aa50f454a&link=e77518ff-be46-4d75-8058-3935d80c01af&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "sayim-farkini-hucre-hareketlerine-isleme_74716180_22803883.html"
source_version: "2022-11-18T13:41:22.113+03:00"
source_bytes: 35612
fetched_at: "2026-09-13T04:06:13+00:00"
generator: "netsis-scraper 1.0.0"
---
# Sayım Farkını Hücre Hareketlerine İşleme

Sayım Farkını Hücre Hareketlerine İşleme, Dinamik Depo-Kayıt menüsünün altında yer alır. Sayım Farkını Hücre Hareketlerine İşleme, hücrelerdeki stok bakiyelerinin, sayım sonuçlarına eşitlenmesi amacıyla kullanılacak olan bölümdür.

![](../../../../../_assets/572621ef24d87aa4714d.png)

Sayım Farkını Satış Hareket İşleme ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Sayım Farkını Satış Hareket İşleme |  |
| --- | --- |
| Sayım Tarihi | Hücrelerdeki stok bakiyeleri, hangi tarihte girilen sayıma eşitlenecek ise ilgili tarihin girildiği alandır. |
| Hücre Kodu | Sayım eşitleme işlemi belli hücre kodları için yapılacak ise, ilgili hücre kodlarının girildiği alandır. Boş bırakılması durumunda işlem, hücre kodu kısıdı olmaksızın, tüm hücreler için yapılır. Rehber butonu ile hücre kodları listesine ulaşılır. |
| Hücre Grup Kodu | Belli grup koduna sahip hücreler için işlem yapılacak ise, ilgili grup kodu aralığının girildiği alandır. Rehber butonu ile grup kodları listesine ulaşılarak aralık verilebilir. |
| Fiş No | Oluşturulacak kayıtta kullanılacak fiş numarasıdır. |
| Stok Hareketlere İşlensin | Hücrelere stok bakiyeleri işlenirken aynı zamanda stok hareketlerine de işlenmesi istendiğinde işaretlenmesi gereken seçenektir. Bu durumda ekranda kapalı olan alan aktif hale gelir ve stoklar için sayım kısıtları verilebilir. |
| Hareket Tarihi | Hücrelere yapılacak kayıt için kullanılacak olan tarihtir. |
| Maliyet İçin Sınır Tarihi | Bakiyelerin sıfırlanması amacıyla, aktarılacak giriş/çıkış hareketlerinde hesaplanan birim fiyat hesaplaması için girilen sınır tarihidir. |
| Stok Bakiye Sınır Tarihi | Stok hareket kayıtlarında hangi tarihe ait bakiyenin sıfırlanacağı ile ilgili sınır tarihi girilen alandır. |
| Maliyet Tipi | Aktarılacak hareketlerde hesaplanan birim fiyat için kullanılacak maliyet tipinin seçildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile maliyet tipleri arasından seçim yapılır. |
| Açıklama | Hareket kayıtlarına aktarılacak hareket için açıklama bilgisi girilen alandır. **Örneğin:** Stok sıfırlama sebebi girilebilir. |
| Mahsup Yapılsın | Mahsup yapılması istendiğinde işaretlenmesi gereken seçenektir. |
| Yuvarlama İçin Ondalık | Yuvarlama için ondalık bilgisinin tanımlandığı alandır. |
| Hareket Türü | Hareket türü olarak "Sayım Farkı", program tarafından otomatik olarak ekrana getirilir ve değiştirilemez. |
| Eksiler Giriş İşlensin | Sayım bakiyesi, bilgisayardaki hücre stokundan az ise, hücre stokunu sayım bakiyesine eşitlemek için otomatik çıkış hareketi işlenir. Sayım bakiyesi, bilgisayardaki hücre stokundan fazla ise, hücre stokunu sayım bakiyesine eşitlemek için giriş hareketi işlenmesi gerekir. Bu hareketin işlem sırasında otomatik yapılması istendiğinde **Eksiler Giriş İşlensin** seçeneği işaretlenir. Giriş hareketlerinin işlenmeyip, daha sonra birtakım kontroller yapıp manuel işlenmesi isteniyorsa, **Eksiler Giriş İşlensin** seçeneği işaretlenmez. |

Girilen bilgilerin onaylanması için Tamam butonu, girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için İptal butonu kullanılır.
