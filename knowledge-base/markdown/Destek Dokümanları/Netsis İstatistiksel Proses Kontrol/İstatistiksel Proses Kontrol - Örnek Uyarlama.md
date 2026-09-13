---
title: "İstatistiksel Proses Kontrol - Örnek Uyarlama"
page_id: "80089293"
product: "netsis-3-enterprise"
depth: 3
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis İstatistiksel Proses Kontrol"
  - "İstatistiksel Proses Kontrol - Örnek Uyarlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis İstatistiksel Proses Kontrol / İstatistiksel Proses Kontrol - Örnek Uyarlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWIwNjE0ZmQ0LTFlMTUtNGQ2YS05NTlkLTgyZTQzZjcyMjZmMyZsaW5rPTY3MjY0M2UwLWJjZDctNDc5My1iNWQ3LWIyMDZlNmY4YTA2YSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=b0614fd4-1e15-4d6a-959d-82e43f7226f3&link=672643e0-bcd7-4793-b5d7-b206e6f8a06a&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "istatistiksel-proses-kontrol-ornek-uyarlama_80089309_80089293.html"
source_version: "2022-11-02T15:51:52.073+03:00"
source_bytes: 1541466
fetched_at: "2026-09-13T04:24:52+00:00"
generator: "netsis-scraper 1.0.0"
---
# İstatistiksel Proses Kontrol - Örnek Uyarlama

Netsis İstatistiksel Proses Kontrol-Örnek Uyarlama ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Logo Netsis'in istatistiksel proses kontrol desteğinin neleri kapsadığını ve desteğe ait ekranların kullanım detaylarını içeren "İstatistiksel Proses Kontrol Tanıtım Dokümanı" sistemde halihazırda bulunmaktadır. Bu dokümanda ise tanıtım dokümanında verilen detayların örnek bir senaryo üzerinden anlatılarak pekiştirilmesi amaçlanmıştır. Örnek uyarlama dokümanı incelenirken tanıtım dokümanından da yararlanılması önerilmektedir.
Logo Netsis istatistiksel proses kontrol desteği kalite kontrol modülü ile birlikte çalışmaktadır. Bu anlamda istatistiksel olarak kontrolü sağlanacak proseslerin kalite kontrol gruplarının tanımlı olması gerekmektedir. Bu uyarlamada bir sayısal ve bir de sayısal olmayan kalite kontrol testine ait istatistiksel proses kontrol takibi yapılması hedeflenmiştir.
Bu bilgilerden sonra test sonucu sayısal olmayan bir "Görsel Kontrol" testimiz olduğunu varsayalım. Bu kontrole ait kalite grup tanımı kaydı Ekran Görüntüsü 1'de gösterilmiştir. Benzer şekilde bir de kalite kontrol test sonucu sayısal olan bir "Boy Ölçüm" testimiz olduğunu varsayalım. Bu kontrole ait kalite grup tanımı kaydı ise Ekran Görüntüsü 2'de gösterilmiştir
![](../../_assets/e42c6369379cea1a5424.png)![](../../_assets/b03763e1c141b6380136.png)**Ekran** **Görüntüsü** **1** **Ekran** **Görüntüsü** **2**
Görsel kontrol ve boy ölçüm kalite testlerini istatistiksel olarak takip edeceğimiz için öncelikle Lojistik- Satış-Kalite Kontrol-Kayıt-Kalite Kontrol Parametreleri yolunu izleyerek gerekli parametre kayıtlarını yapalım. Kontrol grafiklerini hep son 2 haftalık veriye dayanarak takip etmek istediğimizi varsayalım. Ayrıca kontrol limitlerinin dışına çıkacak her noktanın proses için tehlikeli olduğunu düşünelim. Bunlara ek olarak ilgili kontrollerde trend takibi yapmak istediğimizi varsayalım, sürekli artış ya da azalış trendini takip etmek istediğimiz gibi dalgalı hareketi de takip edelim. Bahsedilen kontrollere uygun parametre tanımları Ekran Görüntüsü 3'teki şekilde olacaktır.
![](../../_assets/8d5033fddbc4b26ffcea.png)**Ekran** **Görüntüsü** **3**
Parametre tanımlarını yapıp kaydettikten sonra ilgili kalite kontrol testlerinden boy ölçümünün 2 numaralı kesme makinesinde ve 20 dakikada bir yapıldığını varsayalım. Bu teste dair ölçümleri istatistiksel olarak takip etmeye ise 20 Mart 2020 saat 17:00 itibariyle başlayacağımızı düşünelim. Bu varsayımlara uygun proses kontrol tanımı için 4. Ekran Görüntüsü'ne bakılmalıdır.
![](../../_assets/eca8c3cc6622f119715e.png)**Ekran** **Görüntüsü** **4**
Yukarıda bahsedilen proses takibi için "Proses Kontrol Tanımları" ekranından sabit bir tanım yapılması zorunlu değildi ancak Kesme 2 makinesi için 20 dakika gibi yüksek bir sıklıkla sürekli yapılacak bir kontrol girişinin otomatik olarak getirilmesi kullanıcıya kolaylık ve hız sağlayacağından bu şekilde bir tanımlama yapmak işimizi pratikleştirecektir.
4. Ekran Görüntüsü'nde gösterildiği şekilde tamamlanan tanımın ardından "Proses Kontrol Girişi" ekranına girilirse, tanıma uygun kayıtların otomatik olarak oluşturulduğu, kontrol grafiği çizilebilmesi için kontrol sonuçlarının girişinin beklendiği görülecektir. (Bkz. Ekran Görüntüsü 5)
![](../../_assets/69807a3186f3f398180b.png)**Ekran** **Görüntüsü** **5**
Bu işlemlerin ardından bekleyen kayıtlardan 10 tanesine boy ölçüm kontrol değeri girelim ve kontrol grafiğini kontrol edelim. (Bkz. Ekran Görüntüsü 6) Ölçüm sonucu girilen kontroller için kontrol grafiği kuralları ihlal edilmediğinden grafiğin üzerinde "Proses Kontrol Altında" yazmaktadır.
![](../../_assets/9fd2ca0b2c5dc566e940.png)**Ekran** **Görüntüsü** **6**
Şimdi seçtiğimiz kurallardan "Alt veya Üst Kontrol Limitlerinin Dışında Bir veya Daha Fazla Nokta Olması" kuralını ihlal edecek bir kontrol sonucu daha girip grafiğe yeniden bakalım. (Bkz. Ekran Görüntüsü 7)
![](../../_assets/f412963a02815a41152e.png)**Ekran** **Görüntüsü** **7**
Yukarıdaki örnekte görüldüğü gibi üst kontrol limitinin dışına çıkan 1 adet ölçüm sonucu "Proses Kontrol Altında Değil" uyarısının verilmesine sebep olmuştur.
Şimdi de kontrol limiti dışındaki bu tek ölçümü silip yerine 6 adet sürekli yükselen kontrol değeri girelim ve "Ardışık Altı Noktanın Sürekli Artış ya da Azalış Göstermesi" kuralımızı ihlal edip kontrol grafiğine bakalım. (Bkz. Ekran Görüntüsü 8)
![](../../_assets/9d13a9df97e497776244.png)**Ekran** **Görüntüsü** **8**
Yukarıdaki ekran görüntüsünde görüldüğü gibi işaretli 6 noktanın sürekli artış trendinde olduğu kontrol sonuçları "Proses Kontrol Altında Değil" uyarısının verilmesine sebep olmuştur.
Proses kontrol girişi ekranının grid alanında bulunan her bir ölçüm satırı altında yalnızca 1 adet ölçüm girişi olduğu için ve bu, tüm satırlarda aynı şekilde olduğu için kontrol sonuçlarına ait I-Chart çizilmiştir ve kontrol sonuçlarının değişimi de grafiksel olarak gösterilmiştir. (Bkz. Ekran Görüntüsü 9)
![](../../_assets/cdb5d6f8644c69165f1e.png)**Ekran** **Görüntüsü** **9**
Şimdi de diğer kalite kontrol testimiz olan "Görsel Kontrol" için kontrol grafiği çizilmesini sağlayalım. Bu kontrolün günde 1 kez yapıldığını ve bir makine, istasyon ya da kaynak bazında sonuç girilmediğini varsayalım. Bu durumda proses kontrol tanımı girilmesi kolaylık açısından çok da fark yaratmayacağından doğrudan proses kontrol girişi ekranını kullanabiliriz.
Bu anlamda proses kontrol girişi ekranına 7 tane ölçüm sonucu girelim ve bunlardan 3. ve 6. sonuçlar görsel kontrol testinden geçememiş olsun. (Bkz. Ekran Görüntüsü 10)
Örnekte bahsettiğimiz kontroller her bir ölçüm altında 1 adet (tüm kontrol satırları altında eşit sayıda kontrol sonucu var) olduğundan NP-Chart çizilecek ve kontrol testinden geçemeyen noktalar tek tek sayılacaktır. Bu yüzden 3. ve 6. noktalar aşağıdaki grafikte "1" olarak gösterilmiştir.
![](../../_assets/b5c117f696afc6cf1aeb.png)**Ekran** **Görüntüsü** **10**
Şimdi de yeni bir örnek olarak görsel kontrol grafiğini "Kontrol Grafiği İzleme" ekranından görüntüleyelim ve aynı grafiği "Kontrol Grafiği İzleme" eklentisinden görüntüleyebilmek için gerekli ayarları yapalım.
Kontrol grafiği izleme ekranı için Lojistik-Satış-Kalite Kontrol-Kayıt-Kontrol Grafiği İzleme yolunu takip edip gerekli alanları dolduralım. (Bkz. Ekran Görüntüsü 11)
![](../../_assets/609cbc47db7ba6bf2555.png)**Ekran** **Görüntüsü** **11**
Şimdi de son olarak Netsis panelinden "Eklenti Ekle'ye" tıklayalım ve "Kalite kontrol için kontrol grafiği izleme" eklentisinin ayarlar butonuna tıklayarak gerekli parametreleri ayarlayalım. (Bkz. Ekran Görüntüsü 12)
![](../../_assets/de8a732d3a528bd8d4b2.png)**Ekran** **Görüntüsü** **12**
Yaptığımız son parametre ayarlarıyla örneklerimiz tamamlanmış oldu. Bu uyarlama dokümanında gösterilmiş ve gösterilmemiş tüm detaylara ulaşmak için istatistiksel proses kontrol tanıtım dokümanından ve istatistiksel proses kontrol webinar'ından yararlanılabilir. Kalite kontrol modülü tarafındaki ihtiyaçlar için ise kalite kontrol modülü tanıtım dokümanı ve webinar'ı da sistemde bulunmaktadır.
