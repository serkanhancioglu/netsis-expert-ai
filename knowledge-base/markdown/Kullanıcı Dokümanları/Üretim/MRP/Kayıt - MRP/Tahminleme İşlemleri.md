---
title: "Tahminleme İşlemleri"
page_id: "50667654"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Üretim"
  - "MRP"
  - "Kayıt / MRP"
  - "Tahminleme İşlemleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Üretim / MRP / Kayıt / MRP / Tahminleme İşlemleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPThlMDA0YTBlLWQ5MzgtNDRmMi1iODIzLTQyOGYwYmMxYWQ3YiZsaW5rPTA5OWQ5MTEzLTBiMmUtNGRlMi05YmQyLTBlOGVlNTY0YmM2YSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=8e004a0e-d938-44f2-b823-428f0bc1ad7b&link=099d9113-0b2e-4de2-9bd2-0e8ee564bc6a&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "tahminleme-islemleri_50667687_50667654.html"
source_version: "2022-10-19T15:08:16.327+03:00"
source_bytes: 91518
fetched_at: "2026-09-13T04:19:58+00:00"
generator: "netsis-scraper 1.0.0"
---
# Tahminleme İşlemleri

Tahminleme İşlemleri, Üretim Bölümü'nde Kayıt/MRP menüsünün altında yer alır. Tahminleme İşlemleri, belirli istatistiksel yöntemlerin geçmiş satış verilerine uygulanması ile gelecek dönemlere ait satış tahminleri oluşturulmasını sağlar.

Geçmiş satış bilgilerinin baz alınarak geleceğe yönelik satış tahminlerinin çeşitli yöntemlerle yapılmasını, oluşan tahmin verilerinin elle (Manuel) düzenlenmesini ve tahminlerden bütçe tablosunun oluşturulmasına yardımcı olur.

Tahminleme İşlemlerinde işleyişi aşağıdaki şekilde yapılır:

- Tahminleme yapılırken dikkate alınacak şirketlerin - geçmiş yıl veri tabanlarının - belirlenmesi ve bu verilerden hazırlık verileri oluşturulması.
- Oluşan hazırlık verilerinden farklı modellerle oluşan tahminlerin test edilmesi ve onaylanan modele göre oluşan tahmin verilerinin kaydedilmesi.
- Tahmin verilerinin gerekiyorsa elle düzenlenmesi.
- Tahmin verilerinden bütçe verileri oluşturulması.

Tahminleme İşlemleri ekranı; Tahmin Kayıtları, Satış Verisi Oluşturma, Tahminleme Çalıştırma ve Tahminleme Sonuçları sekmesinden oluşur.

**Tahmin Kayıtları**

İstenen parametreler ve belirli bir yöntem ile hesaplanarak oluşturulmuş satış tahminleri kümesi, bir numara verilerek, ileride erişim sağlanması için saklanır. "Tahmin Kayıtları" sekmesinin grid ekranında saklanan tahmin kayıtları izlenebilir ve istendiği zaman yeni bir tahminleme kaydı oluşturulabilir. Mevcut tahmin işleminin aktif/pasif durumu değiştirilebilir.

Aktif tahmin kaydı içinde yapılacak tahminleme işlemi için parametreler belirlenir. MRP Parametreleri bölümünde belirlenen tahminleme parametreleri, varsayılan olarak ekrana getirilir. Kullanıcı isterse, farklı tahminleme işlemlerinde bu parametreleri farklı şekilde belirleyebilir.

Tahmin kayıtlarının yönetimi için ekranda; Yeni Tahmin Kaydı, Tahmin Kaydını Sil ve Aktif-Pasif olmak üzere üç adet buton bulunur.

Yeni Tahmin Kaydı: Yeni bir tahminleme kaydı için kullanılacak butondur.

Tahmin Kaydını Sil: Seçili olan tahmin kaydını silmek için kullanılacak butondur.

Aktif-Pasif: Seçili olan tahminleme kaydını aktif ya da pasif hale getirmek için kullanılacak butondur. Ana üretim planlama sırasında sadece aktif tahmin kayıtları kullanılabilir.

![](../../../../_assets/add81064aac40dec6938.png)

Tahminleme İşlemleri Ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Tahminleme İşlemleri Ekranı |  |
| --- | --- |
| Tahmin No | Tahmin için girilen numaradır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, tahmin numaralarına ulaşılır. |
| Başlangıç Zamanı/Bitiş Zamanı | Oluşturulacak satış tahmin dönemi için başlangıç ve bitiş tarihlerinin girildiği alanlardır. |
| Tahmin Değeri Periyot Tipi | Tahmin periyot tipinin belirlendiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile; Gün, Hafta, Ay, Çeyrek veya Yıl periyotları arasından seçim yapılır. |
| Gruplama Seçeneği | Tahminleme işlemi için gruplama seçeneğinin girildiği alandır. Alanın sağ tarafında yer alan Stok Kodu, Grup Kodu, Ürün Grubu, Kod-1,2,3,4,5 seçenekleri arasından seçim yapılır. |
| Ölçü Birimi | Tahmin miktarlarının oluşturulması istenen ölçü biriminin seçildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile ölçü birimi seçenekleri arasından seçim yapılır. |
| Tahmin Çarpan Sahası | Tahminleme miktarını Kullanıcı Tanımlama Sahaları bölümünde girilen herhangi bir değer ile arttırılması ya da azaltılması için kullanılan alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile çarpan sahası seçimi yapılır. |
| Açıklama | Tahminleme işlemi için açıklama bilgisi girilen alandır. |
| Satış Verisi | Tahmin kaydı için satış verisi tanımlanan alandır. Satış faturalarına ek olarak, müşteri siparişleri ve üretim sonu kayıtları için de satış verisi oluşturulabilir. Alanın sağ tarafında yer alan aşağı ok butonu ile satış verileri arasından seçim yapılır. |
| ![](../../../../_assets/0b82b8be7ee48c1c868c.png) Yeni Tahminleme Kaydı | Yeni bir tahminleme kaydı için kullanılan butondur. |
| ![](../../../../_assets/72a18abca0fa9a6d1b73.png) Tahmin Kaydını Sil | Seçili olan tahmin kaydını silmek için kullanılan butondur. |
| ![](../../../../_assets/cbf63da88af3c351df16.png) Aktif Pasif | Seçili olan tahminleme kaydını aktif ya da pasif hale getirmek için kullanılan butondur. Ana Üretim Planlama sırasında sadece aktif tahmin kayıtları kullanılabilir. |

**Satış Verisi Oluşturma**

Satış Verisi Oluşturma, geçmişte gerçekleşen satışların yıl ve periyot bazında analizinin sağlandığı sekmedir. Ekranın sol bölümünde şirket listesi bulunur. Geçmiş satış verisinin alınacağı şirketlerin bu listeden seçilmesi gerekir. Şirket seçimden sonra ![](../../../../_assets/f17c031a01ae6ad85c8c.png) Satış Verisi Oluştur butonuna tıklayarak geçmiş satış verilerinin, belirtilen gruplama, periyot ve ölçü birimi bazında analizi oluşturulur. Oluşan satış analizleri ekranın sağ bölümündeki listeden izlenir.

**Tahminleme Çalıştırma**

Ürün/Ürün Grubu listesi ekranın sol bölümünden izlenir. ![](../../../../_assets/60936648582146580202.png) Tahminleme Çalıştırma butonuna tıklayarak tüm ürünler/ürün grupları için tahminleme çalıştırma işlemi yapılır. Bu aşamada birçok istatistiksel yöntem için tahminleme çalıştırılmış olur. Sistem, en iyi sonucu veren yöntemi, kod bazında seçerek grafik üzerine yansıtır. İlgili kod seçildiğinde bu koda ait grafik izlenir.

Grafikte kırmızı olan çizgi gerçek satış verilerini, mavi çizgi ise yöntemin hem geçmiş dönemlere hem de gelecek dönemlere uygulanmış halini gösterir. Grafikte iki farklı renkte olan bu çizgiler kıyaslanarak, ilgili yöntemin gerçek satış verilerinden ne kadar sapma ile tahminde bulunduğu gözlemlenir.

Kod bazında çalıştırılan tahmin yöntemlerine ve bu yöntemlerin ürettiği sonuçlara “Kod Bazında Çalıştırılan Tahmin Yöntemleri” bölümünden ulaşılır. Tahmin yöntemi buradan değiştirilerek farklı yöntemlerin grafiklerine erişilir. Sistemin seçtiği yöntemden daha farklı bir yöntemin sonucu beğenildiği zaman bu yöntem tercih edilebilir. Tahminleme sonuçlarını kaydetmek için ekranın sağ alt köşesinde bulunan ![](../../../../_assets/7c1ed84f54082c570a92.png) Kaydet butonuna tıklanması gerekir.

**Tahminleme Sonuçları**

Tahminleme Sonuçları, kaydedilen tahminleme sonuçlarının detaylı şekilde izlenmesini sağlayan sekmedir.

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır.

Kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
