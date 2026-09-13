---
title: "Gereksinim Planlama Oluşturma"
page_id: "50668660"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Üretim"
  - "MRP"
  - "İşlemler / MRP"
  - "Gereksinim Planlama Oluşturma"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Üretim / MRP / İşlemler / MRP / Gereksinim Planlama Oluşturma"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWJkNGQ1YTBlLTE3MGMtNGIyYS05Y2M3LTg5YzhiMGMyYWQ5NyZsaW5rPTQwMjI0YmRmLTdiZmQtNDQxYS04Y2M4LWI1ZDVmNDQyMTM2MSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=bd4d5a0e-170c-4b2a-9cc7-89c8b0c2ad97&link=40224bdf-7bfd-441a-8cc8-b5d5f4421361&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "gereksinim-planlama-olusturma_50668771_50668660.html"
source_version: "2022-11-10T10:44:59.770+03:00"
source_bytes: 34376
fetched_at: "2026-09-13T04:20:04+00:00"
generator: "netsis-scraper 1.0.0"
---
# Gereksinim Planlama Oluşturma

Gereksinim Planlama Oluşturma, Üretim Bölümü'nde, "İşlemler/MRP" menüsünün altında yer alır. Gereksinim Planlama Oluşturma, malzeme gereksinim planlamasına baz oluşturacak mamul gereksinimlerinin oluşturulmasını sağlayan bölümdür. Bunun için müşteri siparişlerinin tarih bazında yapılacak teslimatları bulunur.

Gereksinim Planlama Oluşturma ekranı; Kayıtlı Planlar, Gereksinim Plan Kısıt ve Gereksinim Plan Oluşturma olmak üzere üç sekmeden oluşur.

**Kayıtlı Planlar**

Kayıtlı planların listelendiği sekmedir. Liste üzerinden seçilen kayda çift tıkadıktan sonra, planın silinmesi için MRP Sil ![](../../../../_assets/b183bdebfaefc12ca3c7.png) butonunun kullanılması gerekir. Geri Dön ![](../../../../_assets/05b4ba6507370b800c3f.png) butonu, plana geri dönülmesi veya aktif planın yedeklenmesi için kullanılır. Mrp Yedekle ![](../../../../_assets/1180bb1c97a39538729a.png) butonu, aktif planın yedeklenmesi için kullanılır. İleri ![](../../../../_assets/509ca33f831549923dcb.png) butonu bir sonraki sekmeye ilerlemek için kullanılır.

**Gereksinim Plan Kısıt**

Gereksinim Planlama Oluşturma ekranı Gereksinim Plan Kısıt sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Gereksinim Planlama Oluşturma Ekranı |  |
| --- | --- |
| Fabrika Kodu | Gereksinim planlaması oluşturulacak fabrika için kod tanımlanan alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile tanımlı fabrika kodlarına ulaşılır. |
| Açıklama | Gereksinim planlaması için açıklama bilgisi girilen alandır. |
| Tarih Aralığı | Plan kayıtlarının oluşturulacağı tarih aralığının girildiği alandır. Bu tarihlere girilen plan kayıtları program tarafından silinerek, yeni kayıtlar oluşturulur. |
| Günlük, Baz Tarihi | Müşteri siparişlerinin teslimat günlerinde veya belli bir periyoda ait teslimatların toplanarak tek bir güne planlanması için seçim yapılan alandır. |
| Baz Tarihi | Belli periyotlarda planlama yapıldığı zaman plan kayıtlarının yazılacağı tarihin girildiği alandır. **Örnek** ```text<br>Teslim Tarihi Mamul Miktar01/08/2003 M1 10 adet03/08/2003 M1 12 adet06/08/2003 M1 8 adet11/08/2003 M1 14 adet<br>``` müşteri siparişleri yukarıdaki şekilde olduğunda ve planlama "Günlük" yapıldığı taktirde, yukarıdaki kayıtlar olduğu gibi planlama girişinde oluşur. Planlama "Baz Tarihi" ile çeşitli şekillerde yapılabilir. 10 günlük periyotlar için planlama yapılıyorsa, yukarıdaki kayıtlar için Planlama Oluşturma iki kez çalıştırılmalıdır. 1. Tarih Aralığı : 01/08/2003 - 09/08/2003 ```text<br>Baz Tarihi : 01/08/2003<br>``` \2. Tarih Aralığı : 10/08/2003 - 19/08/2003 ```text<br>Baz Tarihi : 10/08/2003 şeklinde parametrelerin girilmesi gerekir.<br>``` Bu durumda oluşacak planlama kayıtları şöyledir: ```text<br>Tarih Mamul Miktar01/08/2003 M1 30 adet10/08/2003 M1 14 adet<br>``` 1 aylık periyotlar için planlama yapılıyorsa, yukarıdaki kayıtlar için Planlama Oluşturma çalıştırılırken Tarih Aralığı : 01/08/2003 - 31/08/2003 Baz Tarihi : 01/08/2003 şeklinde parametrelerin girilmesi gerekir. Bu durumda oluşacak planlama kayıtları şöyledir: ```text<br>Tarih Mamul Miktar01/08/2003 M1 44 adet<br>``` |
| Tüm Mamuller, Sipariş Bakiye, Tüm Mamuller+Sipariş Bakiye, AÜP | Tüm mamullerin sadece bir baz tarihinde planlama giriş ortamına kaydedilmesi için "Tüm Mamuller" seçeneğinin - bu seçenek çok çeşitli mamulü bulunan işletmelerde tüm mamullerin tek tek elle girilmemesi için tercih edilebilir - kullanılması gerekir. Sipariş Bakiyelerinin sadece bir baz tarihinde planlama giriş ortamına kaydedilmesi için "Sipariş Bakiye" seçeneğinin kullanılması gerekir. Tüm Mamuller ve Sipariş Bakiye toplamının sadece bir baz tarihinde planlama giriş ortamına kaydedilmesi için "Tüm Mamuller+Sipariş Bakiye" seçeneğinin kullanılması gerekir. Ana Üretim Planlamanın sadece bir baz tarihinde planlama giriş ortamına kaydedilmesi için "AÜP" seçeneğinin kullanılması gerekir. |
| Başlangıç Öncesi Siparişler İçin Tarih | Gereksinim planlama oluştururken başlangıç öncesi siparişler için tarih belirlenen alandır. |
| Sipariş No Aralığı | Müşteri siparişlerinin bir kısmının plana dahil edilmesi için kullanılan alandır. Bu durumda program, sadece girilen aralıktaki siparişlere ait mamul gereksinimlerini Plan Girişi bölümünde oluşturur. |
| Sipariş Bazında Ayrım | Gereksinim planının, her mamul için müşteri siparişleri bazında ayrı ayrı oluşması için kullanılan seçenektir. Aksi halde mamuller için gereksinim miktarları sipariş detayına inmeden toplam miktarları ile oluşturulur. Bunu belirlerken yukarıda yer alan Günlük/Baz Tarihi sorgusu da etkili hale gelir. **Örnek** ```text<br>Mamul Kodu Sip.Teslim Tarihi Sip. No Sip. MiktarıMM1 15.10.2003 00000001 10MM1 20.10.2003 00000002 20MM2 15.10.2003 00000003 25MM2 20.10.2003 00000004 15MM2 20.10.2003 00000005 7<br>``` Sipariş bazında ayrım parametresi **işaretlenir ve günlük seçilirse;** mamul gereksinimleri, yukarıdaki tablo şeklinde oluşur. Sipariş bazında ayrım parametresi **işaretlenmez ve günlük seçilirse;** MM1 için 10, 20.10.2003 MM1 için 20, MM2 için 25, MM2 için **22** adet gereksinim oluşur. Sipariş bazında ayrım parametresi **işaretlenir ve baz tarihi seçilirse:** Baz tarihi : 15.10.2003 MM1 için 10 15.10.2003 MM1 için 20 15.10.2003 MM2 için 25 15.10.2003 MM2 için 15 15.10.2003 MM2 için 7 adet gereksinim oluşur. Sipariş bazında ayrım parametresi **işaretlenmez ve baz tarihi seçilirse:** Baz tarihi : 15.10.2003 MM1 için 30 15.10.2003 MM2 için 47 adet gereksinim oluşur. |
| Siparişte Revizyonun Tutulduğu Saha | Müşteri siparişinde Revizyon No (Planlanan Bileşen Değişikliği) bilgisinin tutulduğu alanın seçilmesini sağlar. Böylece, MGP sırasında müşteri siparişindeki revizyon numarasına uygun olacak şekilde reçete getirilir ve ihtiyaçlar revize reçeteye göre hesaplanır. Alanın sağ tarafında yer alan aşağı ok butonu ile seçim yapılır. |
| Sipariş | Müşteri siparişlerindeki Planlanan/Kesinleşen bilgisine göre kısıt vermek için kullanılan alandır. "Hepsi" seçeneği seçildiğinde, tüm müşteri siparişleri dikkate alınır. |
| ![](../../../../_assets/76096e940be333e40ae7.png) Tümünü Oluştur | Girilen tarih aralığında gereksinim planlama oluşturulması için kullanılan butondur. Butonun sağ tarafında yer alan aşağı ok butonu ile, Zamanlanmış Görevlere Ekle seçilerek bazı işlemlerin görev olarak tanımlanması ve bu görevlerin sunucu üzerinde çalıştırılması sağlanır. |
| ![](../../../../_assets/de3efa43edecd09d055e.png) Seçimli Oluştur | Gereksinim Plan Oluşturma sekmesine ilerlenmesini ve ileri kısıt verilerek gereksinim planlama oluşturulmasını sağlayan butondur. |

**Gereksinim Plan Oluşturma**

Gereksinim Plan Oluşturma ekranında yer alan butonlar ve içerdiği bilgiler şunlardır:

| Gereksinim Planlama Oluşturma Ekranı |  |
| --- | --- |
| İleri Kısıt Girişi | Artı + butonuna tıklanması ile rapor kısıt alanının görünmesi sağlanır. Ayrıntılı şekilde kısıtlama yapılması için kullanılan alandır. |
| ![](../../../../_assets/88d16927ea783fbf1fc5.png) Kayıtlar Getir | Girilen kısıtlara uygun tüm bilgilerin ekranın alt bölümündeki grid alanda listelenmesi için kullanılan butondur. |
| ![](../../../../_assets/7c6379e763f2484dbe5c.png) Tüm Kırılımları Aç | Grid ekranda listelenen malzemelerin - varsa - kırılımlarını açmak için kullanılan butondur. |
| ![](../../../../_assets/10ee217bbc9538900cd7.png) Tüm Kırılımları Topla | Grid ekranda listelenen malzemelerin "Tüm Kırılımları Aç" butonu ile kırılımları açıldıktan sonra açılan kırılımların geri kapatılması için kullanılan butondur. |
| ![](../../../../_assets/d15ca1ad68365b9a1a84.png) Tümünü Seç | Ekrana gelen listede yer alan malzemelerin hepsinin seçilmesi için kullanılan butondur. |
| ![](../../../../_assets/f5ffb212771284b3d8d5.png) Tümünü Kaldır | Liste üzerinden seçilen tüm malzemelerin seçiminin kaldırılması için kullanılan butondur. |
| ![](../../../../_assets/0bbdbcaeac99ce2b64b0.png) MGP Oluştur | MGP oluşturulması için kullanılan butondur. |
