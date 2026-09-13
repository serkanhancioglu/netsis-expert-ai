---
title: "Netsis Kalite Kontrol Modülü SSS"
page_id: "74711374"
product: "netsis-3-enterprise"
depth: 3
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis Kalite Kontrol Modülü"
  - "Netsis Kalite Kontrol Modülü SSS"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis Kalite Kontrol Modülü / Netsis Kalite Kontrol Modülü SSS"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWZiYjIxZWQ4LWEwZjQtNDk3NC1iYjAwLTA4OTNmMzc5MzE1YiZsaW5rPTY2NzIyZDA2LWZmNTUtNGIxYS1iNTUwLWJmYzUwMTJmZGEwMSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=fbb21ed8-a0f4-4974-bb00-0893f379315b&link=66722d06-ff55-4b1a-b550-bfc5012fda01&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-kalite-kontrol-modulu-sss_80088193_74711374.html"
source_version: "2022-05-12T16:02:13.373+03:00"
source_bytes: 1775703
fetched_at: "2026-09-13T04:24:54+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis Kalite Kontrol Modülü SSS

**Kalite kontrol kaydı kapatılmayan irsaliyelerin faturalandırılmaması sağlanabilir mi?**
**Soru 1: Kalite kontrol kaydı kapatılmayan irsaliyelerin faturalandırılmaması sağlanabilir** **mi?**
Evet sağlanabilir. Kalite Kontrol Parametrelerinde "Kalite kontrol kaydı kapatılmayan alış irsaliyesi faturalaştırılmasın" parametresinin işaretlenmesiyle kalite kontrol kaydı kapanmayan alış irsaliyelerinin faturalaştırılmaması sağlanmaktadır.

**Hangi belge ve işlemler için kalite kontrol testleri yapılmaktadır?**

Alış İrsaliyesi, Depolar Arası Transfer Fişleri, Ambar Giriş Fişleri, Müstahsil Faturası, İş Emri ve Üretim Sonu Kaydı belgeleri, İade işlemlerinde iade belgeleri ve belge bağımsız işlemler (örneğin satış sonrası servis kayıtları vb) için kalite kontrol kayıtları yapılmaktadır.

**Personel tanımlama erkanında rehber seçimi alanında personel seçeneği ne zaman aktif gelir?**

Personel paketi varsa, rehber seçimi kısmında personel seçeneği yer alır. Personel paketiyle bağlantı, Yardımcı Programlar\>Kayıt\> Diğer Paketlerle bağlantı ekranından kullanılan veritabanı, kullanıcı adı ve şifre bilgileri girilerek bağlantı sağlanır.

**Kalite** **Grup** **Tanımları** **ekranında** **yer** **alan** **Revizyon** **No** **ne** **işe** **yarar?**

Revizyon bağlantısı ile aynı grup içerisinde farklı revizyona bağlı ölçüm kümeleri oluşturulabilir. Revizyon numarası sistem tarafından belirlenen bir sayısal değer ile ifade edilir. Örneğin, A ölçümünün artık kullanılmayacağı, A yerine artık B ölçümünün kullanılacağı durumda veya A ölçümüne ait standartlar değiştiğinde minimum, maksimum değerleri değiştiğinde revizyon kullanımına gidilir. Revizyon kopyalama ile mevcut revizyon farklı bir numara ile oluşturulur ve ölçüm kayıtlarında değiştirilmesi gereken değerler değiştirilir veya kullanılmayacak ölçümler varsa pasif yapılabilir. 100 birimlik bir belge için oran: %50, örneklem miktarı: 2 girilmiş ve kabul edilebilir red oranı: 2 girilmiş. "**Kalite** **Kontrol** **Ölçümleri** **Örnekleme** **Göre** **Oluşsun**" parametresi işaretli olmadığında, 100 birimlik belgenin örneklem miktarı 2. Bu durumda 100/2=50 bulunur. 2' şerli partilerden toplam 50 adet kalite kontrol kaydı oluşur. Bu 2'şerli partilerden %50 oranında yani 1 adedi için kalite kontrol testlerinin yapılacağı anlaşılmaktadır. Kabul edilebilir red oranı 2 olduğuna göre, 2'şerli partiler halinde oluşan 50 adet kalite kontrol kayıtlarından 2' den fazla kalite kontrol kaydı red olmuşsa belge red sayılmaktadır. Her bir kalite kontrol kaydının red olması için ölçümlerden 1' nin red olması yeterlidir.

![](../../_assets/f6d78200fe3e5c31716d.png)
![](../../_assets/54dc839a49335dece8a9.png)

**Muayene Tanımlama ekranındaki Muayene Aralık Tanımlama sekmesinde Iso standardı seçeneği seçildiğinde, Iso standartlarına göre seviyelere, parti** **büyüklüklerine, kabul edilebilir hata oranlarına göre gride gelen kayıtlar nereden** **beslenir?**

ISO Standardı seçildiğinde, ıso standartlarına göre seviyelere, parti büyüklüklerine, kabul edilebilir hata oranlarına göre düzenlenmiş tablo değerleri program içerisine gömülmüştür.

Ekran üzerinden seçilen standart tipi, seviye kodu ve kabul edilebilir hata oranlarına göre grid program tarafından otomatik olarak doldurulmaktadır. Ekran üzerinde yer alan seviye kodları, standart tipleri ve miktar kodları Kalite Kontrol Seviyeleri ekranı ve Kalite Kontrol Miktar Kodları ekranlarından beslenmektedir.

Kalite Kontrol seviyeleri aşağıdaki şekildedir:

ISO 2859 standardında, üç farklı muayene seviyesi belirlenmiştir. Bu seviyeler, İndirgenmiş (Reduced), Normal ve Sıkı (Tight) seviyeler ayrıca S1, S2, S3, S4 olmak üzere 4 farklı özel seviyede belirlenmiştir. Bu tanımlar program tarafından otomatik olarak getirilir.
Seviye Kodu II (Normal): Herhangi bir özel durum olmadığında ve genellikle piyasada kullanılan seviyedir.
Seviye kodu I (Reduced – İndirgenmiş): Parti büyüklük aralıkları daha geniş ama içerisinden seçilen numune sayıları daha az olduğu durumlarda kullanılabilir. Belli dönemde yapılan kontrollerde belli oranda hatasızlık durumu arandığı durumlarda kullanılabilir.
Seviye Kodu III (Sıkı-Tight): Hata oranı yüksek yani daha dar aralıklarla daha çok numune kontrolleri yapılması gerekiyorsa bu seviye tercih edilir. Örneğin daha hassas kalite kontrolünün yapılması gereken sektörlerde örneği ilaç sektöründe kullanılabilir.
![](../../_assets/91440bfdda360299f1f6.png)

Kalite Kontrol Miktar Kodları aşağıdaki şekildedir:

![](../../_assets/34e71318581231efaf7c.png)

Sistem üzerinde kalite kontrol seviye verileri otomatik olarak oluşturulmaktadır. "A" miktar kodu, normal seviyede 8'lik parti büyüklüğünü ifade ederken, gevşek seviyede 15'lik parti büyüklüğünü ifade eder. "B" miktar kodu, normal seviyede 15'lik parti büyüklüğü iken, indirgenmiş seviyede 25'lik, sıkı seviyede ise 8'lik parti büyüklüğünü ifade eder şeklinde yorumlanabilir.

**Örneğin,1000 adetlik hoparlör alımı için %1 hata oranına ve Normal Seviyede** **(II) kalite kontrol yapılacağı düşünüldüğünde örneklem ve numune miktar ne olmalıdır?**
Muayene Tanımlama ekranında ISO standardı seçeneği seçilir sonrasında standart olarak ISO 2859- Normal seçilip seviye kodu normal olduğu için II seçilir hata oranı %1 olduğu için hata payı kısmında 1 seçildikten sonra "Tanımlı muayene aralık bilgisi silinecek ve seçtiğiniz standarda göre yeniden oluşturulacaktır" şeklinde uyarı ekranı gelir ve evet dendiğinde bu seçimlere göre grid program tarafından dolar.
![](../../_assets/498b05ca3ee927f06672.png)
1000 adetlik dendiği için 1000' i içeren aralık ve miktar kodu satırı bulunur. Bu seçime göre 1000' lik parti için sabit miktar 1 olduğundan 1' erlik toplam 80 adet hoparlör seçilecek ve 80 adet hoparlöre kalite kontrol testleri gerçekleştirileceği sonucuna ulaşılır. Belgenin kabul ve reddedilmesi şartı için kabul miktarı: 2, red miktarı:3' dür. Bu tanıma göre de bu 80 adet hoparlör için yapılan kalite kontrol testlerinde 2 tane ve daha fazla hoparlör kabul edilmişse belge kabul edilmekte, 3 ve daha fazla hoparlör kalite kontrol sonucu reddedilmişse belge reddedilmektedir anlamına gelmektedir.

**Kalite Kontrol Kaydı ekranında, departman kodları rehberinde üretim departman kodları gelmiyorsa ne yapılmalıdır?**

Departman kodları Merkezi Kimlik Yönetimi ekranında kullanıcı haklarına göre gelir. Kullanıcının sadece kalite satın alma kayıtlarına yetkisi varsa departman kodları olarak sadece satın alma için seçilenler gelmektedir. Üretim departman kodları gelmiyorsa, kullanıcıya sso üzerinde Kalite Üretim Kayıtları yetkisi verilmelidir.
![](../../_assets/86cf89f6f7f3b2270a5f.png)

**Kapatılan kalite kontrol kaydı nasıl açılır?**

Kapatılan kalite kontrol kaydının açılması için öncelikle Depolar Arası Transfer kaydının iptal edilmesi sonra Kayıt Açma butonu ile kaydın açılması sağlanır. Depolar Arası Transfer fişi iptal edilmeden kayıt açılmaya çalışıldığında aşağıdaki gibi "İlgili kalite kontrol kaydı daha önce kapatılmış ve depolar arası transfer işlemi yapılmış. Bu yüzden açma yapılamaz" uyarı verir.
![](../../_assets/f933415184fd0699f616.png)
**Kalite** **kontrol** **kaydı** **sonrasında** **iade** **irsaliyesi** **ne** **zaman** **oluşturulur?**

Oluşan kalite kontrol sonucunda hem red hem kabul miktarları varsa kayıt kapama sonucunda reddedilen stok miktarını red deposuna, kabul edilen stok miktarları da kabul deposuna DAT kaydı yapılır. Eğer istenirse reddedilen ürünler için iade irsaliyesinin oluşturulması sağlanır.

**Kalite kontrol modülünde üretim sonu kaydı yapılıyormuş gibi olup işlem tamamlandı yazmasına rağmen üretim sonu kaydı fişi neden oluşmaz?**

Kalite Kontrol modülünde üretim sonu kaydının yapılabilmesi için, kalite kontrol kaydında olan stok için, stok planlama kayıtları ekranında planama-2 sekmesinde Üretim Sonu Kaydı Yeri "**Kalite Kontrol"** olmalıdır.
![](../../_assets/6107897d599b3cc246e7.png)
