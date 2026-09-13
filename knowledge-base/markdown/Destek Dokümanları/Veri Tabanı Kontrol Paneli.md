---
title: "Veri Tabanı Kontrol Paneli"
page_id: "128583244"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Veri Tabanı Kontrol Paneli"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Veri Tabanı Kontrol Paneli"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPThkYzJhNWZiLTI3NTctNGM1MC1iMGZkLWI1Zjg1MjExZmM1YSZsaW5rPTRhODY0MGFmLTNmYjUtNDJmYy1hMTAwLWJkZjk0OTY2M2FmZCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=8dc2a5fb-2757-4c50-b0fd-b5f85211fc5a&link=4a8640af-3fb5-42fc-a100-bdf949663afd&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "veri-tabani-kontrol-paneli_128583244_128583244.html"
source_version: "2023-12-25T09:29:26.127+03:00"
source_bytes: 3070720
fetched_at: "2026-09-13T04:23:06+00:00"
generator: "netsis-scraper 1.0.0"
---
# Veri Tabanı Kontrol Paneli

Veri Tabanı Kontrol Paneli hakkında ayrıntılı bilgiye bu dokümandan ulaşılır.

Genel\\Yardımcı Programlar\\Raporlar menüsünde yer almaktadır. Veri tabanı kontrol paneli ekranı üzerinden, veri tabanına ait genel bilgiler, tablo ve index bilgileri, şema/nesne farkları ve performans testi gibi konularda raporlama yapılabilmektedir. Veri Tabanı Kontrol Paneli, MS SQL üzerinde çalışan Netsis paketlerinde desteklenmektedir.

### Genel Bilgiler

Genel bilgiler sekmesinde veri tabanı sunucusuna ait bilgiler, veri tabanı bilgileri ve istemci bilgileri yer almaktadır.

![](../_assets/8eb14f17abcb9cbc324f.png)

**Tablo Bilgileri**

Tablo bilgileri sekmesinde, raporun alındığı aktif şirkete ait veri tabanında bulunan tablolar listelenir. Tablo adı, tabloda bulunan kayıt sayısı, veri boyutu, tablodaki index boyutu, ilgili tablo için sql serverda ayrılmış fakat kullanılmayan alan boyutu ve disk boyutu alanında da toplam alan boyutu MB olarak görüntülenebilir. Akıllı grid üzerinde filtreleme ve sıralama yapılabilir.

![](../_assets/ce026ca116dac70f4ffe.png)

### Index Bilgileri

Index bilgileri sekmesinde, tablo adı, tablodaki index adı, index tipi, indexin içerdiği kolon listesi, index boyutu ve fragmentation (parçalanma) seviyesi yüzde olarak raporlanmaktadır.

![](../_assets/e94acb0e458d853f5e50.png)

Fragmentation seviyesine göre sıralama yapılarak, parçalanma düzeyinin en fazla olduğu kayıtlar için inceleme yapılabilir. Indexler ile ilgili bakım yapılmak istenir ise, seçim kolonundan bakım yapılmak istenilen index veya indexler seçilebilir. Seçim yapılan indexler için **Index Bakım** butonuna basıldığında 2 farklı seçenek gelmektedir.
![](../_assets/8c60e867685f4c47467f.png)

**Seçilenler İçin Çalıştır:** Grid üzerinde "Seçim" kolonu işaretli olan indexler için veri tabanı bakım cümlesi çalıştırılır, bu işlem ile fragmentation seviyesi düşürülmektedir.

![](../_assets/5f562fe352b2e3ae4dc3.png)

"Seçilenler İçin Çalıştır" seçeneğine tıklandığında aşağıdaki index bakım parametreleri
sorulmaktadır:

- **İstatistikler Güncellensin: Varsayılan** olarak işaretli gelmektedir. Bu seçenek işaretli olduğunda index bakımının sonunda istatistiklerin de güncellenmesi sağlanmaktadır.
- **Fragmentation Sınır Değeri (%):** Varsayılan olarak 40 değeri gelmektedir. %40dan fazla parçalanma olan indexlerde rebuild (yeniden oluşturma) işlemi yapılır, %40'ın altında fragmentation olanlarda ise reorganize (yeniden düzenleme) yapılmaktadır.

**Tümü İçin Zamanlanmış Görev:** "Zamanlanmış Görev Tanımı" ekranı açılır ve "Ön Tanımlı İşlem" kısmından "Veritabanı Bakım İşlemleri" seçili gelerek zamanlanmış görev olarak tanımlama yapılabilmesi sağlanır.

**Şema/Nesne Farkları**

Şema/nesne farkları sekmesinde, raporun alındığı şirket (hedef şirket) ile seçilen veya otomatik olarak oluşturulan kaynak bir şirket arasındaki şema/nesne farkları raporlanabilir.

![](../_assets/01e0052a7796d2d7dd1c.png)

Raporun hazırlanması için "Rapor Hazırla" butonuna tıklamak gerekmektedir. Butona tıklandığında; **Kaynak** **Test** **Şirketi** **Oluştur** ve **Kaynak** **Şirket** **Seç** seçenekleri bulunmaktadır.

![](../_assets/4b6d95515751c9c68fca.png)

- **Kaynak Test Şirketi Oluştur:** Bu seçenek seçildiğinde karşılaştırmayı yapabilmek için yeni bir isimle test şirketi oluşturulur ve raporun alındığı şirket ile oluşturulan test şirketi arasında nesnelerin karşılaştırması yapılır. Oluşturulacak test şirketi kullanılmakta olan sürümün güncel veri tabanı cümleleri ile yaratılmaktadır. Rapor hazırlandıktan sonra yeni oluşturulan test şirketi silinir.
- **Kaynak Şirket Seç:** Bu seçenek seçildiğinde daha önceden tanımlanmış mevcut şirketler listelenmektedir, bu listeden kaynak şirket seçimi yapılabilir. "Tamam" butonuna tıklandığında seçilen şirket veri tabanı ile aktif şirket için nesne karşılaştırması yapılır.

Rapor hazırlandıktan sonra grid üzerinde, Nesne Tipi, Nesne Adı, Tablo/View Adı, Fark Durumu, Fark Açıklama, Detay bilgileri yer alır.

Nesne Tipi ve Nesne Adı kolonunda fark veren nesnenin tipi ve adı raporlanırken, Tablo/View ismi kolonunda ise fark veren nesnenin bağlı bulunduğu bir tablo/view varsa bu bilgi raporlanmaktadır.
![](../_assets/4fb5182a6c149649307d.png)

Fark durumu kolonunda; Eksik Nesne, Fazla Nesne, Farklı Nesne, Eksik Kolon, Fazla Kolon olarak 5 farklı fark durumu raporlanmaktadır. Bu fark durumlarının detayı aşağıdaki gibidir:

- **Fazla** **Nesne:** Raporun çalıştırıldığı hedef şirket üzerinde bulunan ancak kaynak şirket üzerinde bulunmayan nesneleri göstermektedir.
- **Eksik Nesne:** Raporun çalıştırıldığı hedef şirket üzerinde bulunmayan ancak kaynak şirket üzerinde bulunan nesneleri göstermektedir.
- **Eksik** **Kolon:** Bu fark durumu sadece Tablo veya View tipindeki nesneler için raporlanmaktadır Raporun çalıştırıldığı hedef şirket üzerindeki ilgili Tablo/View'da bulunmayan kolonun kaynak şirket üzerinde bulunduğunu ifade etmektedir. Fark Açıklama alanında kolon detayı şu örnek format ile raporlanmaktadır: "Eksik Kolon: TESTCOLUMN1"
- **Fazla** **Kolon:** Bu fark durumu sadece Tablo veya View tipindeki nesneler için raporlanmaktadır. Raporun çalıştırıldığı hedef şirket üzerindeki ilgili Tablo/View'da bulunan kolonun kaynak şirket üzerinde bulunmadığını ifade etmektedir. Fark Açıklama alanında kolon detayı şu örnek format ile raporlanmaktadır: "Fazla Kolon: TESTCOLUMN1"

- **Farklı Nesne:** Bu fark durumunda Tablo ve View tipindeki nesneler için kolon tiplerindeki farklılıklar, Primary Key/Foreign Key/Index tipindeki nesneler için kullanılan kolonlar ve sıralamasındaki farklılıklar raporlanır. Fark Açıklama alanında fark veren kolonlar için detay bilgi verilir. Öte yandan Trigger/Procedure/Function tipindeki nesneler için de nesne create cümleleri birebir karşılaştırılarak bulunan farklar raporlanır ve bu nesne tipleri için "Detay" kolonundaki üç noktaya tıklayarak cümleler arasındaki farkların detayı görülebilir.

Detay kolonuna tıklandığında açılan ekranda; sol tarafta nesneye ait kaynak şirket üzerindeki sql cümlesi gösterilirken, sağ tarafta ise aktif şirket için sql cümlesi gösterilmektedir. Ekranın üst bölümündeki "Önceki Fark" ve "Sonraki Fark" butonlarına tıklayarak iki cümle arasında fark veren satırlara hızlıca odaklanılması sağlanabilir.
![](../_assets/e6c012755d0cf34b1430.png)

### Performans Testi

"Rapor Hazırla" butonuna basıldığında bir test tablosu oluşturularak sırasıyla aşağıdaki işlemler yapılır ve bu işlemlerin maksimum süre, minimum süre, ortalama süre ve standart sapma değerleri hesaplanarak raporda gösterilir:

- 10.000 adetlik 3 farklı yöntem ile INSERT işlemi
- Tabloya atılan 30.000 adetlik kaydın SELECT sorgusu ile getirilmesi ve okunması
- Tabloya atılan ilk 10.000 kaydın tek tek çalışacak sql sorguları ile UPDATE edilmesi
- Tabloya atılan son 10.000 kaydın verilen bir kısıta göre tek seferde toplu UPDATE edilmesi
- Tabloya atılan ilk 10.000 kaydın tek tek çalışacak sql sorguları ile DELETE edilmesi
- Tabloya atılan son 10.000 kaydın verilen bir kısıta göre tek seferde toplu DELETE edilmesi
- STHAR, CAHAR, MUHFIS, DEKOTRA, FATUIRS, ISEMRI tablolarında rastgele seçilen en fazla 1000 adet kayıt için tek tek SELECT sorgularının çekilmesi

![](../_assets/69fdc16c95d3c65bc7c0.png)
