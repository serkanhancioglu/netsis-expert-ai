---
title: "Netsis Ana Üretim Planlama"
page_id: "95651521"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis Ana Üretim Planlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis Ana Üretim Planlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWNjNzcxNjdjLTdmNDctNDUwOS04ODMwLWI1YTUzNjFlZDllYSZsaW5rPWMzNTE1ZDg5LWU5ZTgtNDQ4OC04NmI5LTcyNGM5ODE5YWRhYSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=cc77167c-7f47-4509-8830-b5a5361ed9ea&link=c3515d89-e9e8-4488-86b9-724c9819adaa&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-ana-uretim-planlama_95651534_95651521.html"
source_version: "2022-11-03T09:38:33.723+03:00"
source_bytes: 1440840
fetched_at: "2026-09-13T04:26:03+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis Ana Üretim Planlama

Ana Üretim Planlama ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

**Ana Üretim Planlama İşlemleri**

Ana Üretim Planlama (AÜP) işlemleri, satış tahminlerine ve müşteri siparişlerine dayalı olarak ihtiyaçların karşılanabilmesi için dönemsel üretim miktarlarını hesaplayan işlemler topluluğudur. AÜP işlemlerinin sonucunda her bir son ürün için hangi zamanda ne kadar üretim yapılması gerektiği raporlanır. Çeşitli parametre ve girdilere dayalı olarak hesaplanan AÜP miktarları malzeme gereksinim planına aktarılabilir.

**Ana Üretim Planlama Parametreleri**

Ana Üretim Planlama parametreleri, MRP parametreleri / Ana Üretim Planlama sekmesinde yer alır. Bu parametreler istenirse ana üretim planlama işlemi sırasında da değiştirilebileceğinden bu bölümde öndeğer olarak bırakılabilir.
![](../_assets/e4cb7b85ef07768c5982.png)

**AÜP Değeri Periyot Tipi:** Ana üretim planlama işleminin hangi periyot cinsiyle yapılacağını belirleyen parametredir. Gün, Hafta, Ay, Çeyrek, Yıl seçilebilir.

**Gruplama** **Seçeneği:** Ana üretim planlama işlemlerini yaparken kullanılacak gruplama seçeneğini belirleyen parametredir. Ana üretim planlama stok kodu bazında yapılabileceği gibi grup kodu, ürün grubu vs. bazında gruplanarak da yapılabilir. Stok Kodu, Grup Kodu, Kod1...Kod5, Ürün Grubu, Stok Kodu+Yapkod seçilebilir.

**İhtiyaç Belirleme Yöntemi:** Ana üretim planı ihtiyaç miktarının hesaplanmasında, baz alınacak ihtiyaç kalemlerinin seçimi için kullanılır. Seçenekler, tahmin ve müşteri sipariş miktarları karşılaştırılarak büyük olanın alınması, sadece müşteri sipariş miktarının ya da sadece tahmin miktarının alınması olabilir.

**Sipariş Düzleme Yöntemi:** Ana üretim planı oluşturulurken periyotlar bazında değişkenlik gösteren ihtiyaç miktarları, teslim tarihlerine uygun şekilde düzlenerek (periyotlara olabildiğince eşit dağıtılarak) üretim miktarlarının periyotlar bazında dengeli oluşması sağlanabilir.

Backward yöntemi, ihtiyaçların teslim tarihinin bulunduğu periyottan geriye doğru giderek ilk ve sonraki uygun periyodları bularak teslimatları yerleştirir.

Forward yöntemi ise, bugünden siparişin teslim tarihine doğru ileriye giderek uygun periyotları bulur, ancak siparişin teslim tarihi geçilmemektedir.

**Sipariş** **Parçalama:** Sipariş düzleme sırasında teslimat miktarılarının farklı periyotlara parçalanıp parçalanmayacağı belirlenmektedir. Bu parametre "evet" olarak seçilirse, sipariş miktarı farklı periyotlardaki üretimlerden karşılabilecek şekilde parçalanacaktır. Aksi durumda sipariş teslimatının tamamı tek periyotta karşılanacak şekilde yerleştirilecektir.

**Düzlenecek Periyot Sayısı:** Sipariş düzleme yapılırken ilgili siparişin teslim tarihinden en fazla kaç periyot uzağa yerleştirilebileceği bu parametre ile belirlenmektedir.

**Dondurulacak** **Periyot** **Sayısı:** Ana üretim planı çalıştırıldığında daha önceden kaydedilmiş üretim miktarlarının bozulmaması için günümüz tarihinden itibaren kaç periyotluk döneminin sabitleneceği bu parametre ile belirlenir. Örneğin haftalık çalıştırılan bir ana üretim planında bu değer 2 olarak seçilirse, önümüzde 2 haftalık ana üretim planı miktarları tekrar hesaplanarak değiştirilmeyecektir.

**AÜP Miktarı Hesaplanırken Azami Stok Miktarı Dikkate Alınsın:** Gruplama seçeneğinin stok kodu seçildiği durumlarda geçerli olan bir parametredir. Bu parametre işaretlenirse ilgili periyodtaki ana üretim planı miktarı hesaplanırken o dönem için elde kalacak stok bakiyesini azami limite tamamlayacak şekilde hesap yapılır.

**Reçetesi olmayan stokları Ana Üretim Planına Dahil Et:** Reçete kaydı bulunmayan stokların ana üretim planına dahil edilmesini sağlayan parametredir. Firma bünyesinde üretilmeyen, ticari mal şeklinde işlem gören stoklar için kullanılır.

Ana üretim planlama ekranına MRP modülünde kayıt menüsü altından ulaşılabilir. Bu ekran üç ayrı sekmeden oluşmaktadır.

1. Tahmin Kayıtları
2. AÜP Çalıştırma
3. AÜP Sonuçları

![](../_assets/975140c9006345c751af.png)
Sırasıyla bu sekmelerde yapılan işlemler ve açıklamaları aşağıdaki gibidir.

**Tahmin Kayıtları Sekmesi**

Tahmin Kayıtları sekmesinde daha önce üzerinde çalışılmış ve saklanmış olan tahmin kayıtlarından ana üretim planında kullanılması istenen kayıt seçilebilir, ekranın alt kısmında bulunan grid üzerinde tahmin kayıtları raporlanabilir ve mevcut kayıtlar üzerinde güncelleme veya yeni kayıt ekleme işlemleri yapılabilir.

**Tahmin** **No:** Daha önce saklanmış tahmin kayıtlarından birinin seçim yapıldığı alandır.

**Serbest Veri Girişi:** Tahminleme işlemi yapılmaksızın, satış tahminlerinin elle girilmesi ya da Excel'den aktarılması istendiği durumda işaretlenebilecek seçenektir. Alt bölümdeki grid ekran üzerinde aşağıdaki butonlar yardımıyla tahmin kayıtlarının yönetimi sağlanmaktadır.

**Yeni Tahmin:** Yeni bir tahmin kaydı ekleme için bu buton kullanılabilir. Stok kodu, yıl, periyot ve miktar bilgileri girilerek yeni kayıt eklenebilir.

**Tahmin** **Sil:** Alt bölümdeki listeden seçilen bir tahmin satırını silmek için bu buton kullanılabilir.

**Tümünü Sil:** Bu seçenek sadece serbest veri girişinde aktif olmaktadır. Daha önceden serbest olarak girilen bütün tahmin kayıtlarını silmek için kullanılabilir.

**Grupla:** Tahmin kayıtlarını Stok Kodu, Grup Kodu, Kod1...Kod5, Ürün Grubu, Stok Kodu+Yapkod bazında gruplamak için kullanılabilir. Seçilen gruplama yöntemine göre grid ekran üzerindeki görünüm değişecektir.

**Tüm** **Kırılımları** **Aç:** Tahminleme verisi grup bazında oluşturulduğunda alt bölümdeki grid ekrandaki kayıtlar da gruplanarak gelmektedir. Bu grupların tümünü açmak için bu buton kullabilir.

**Tüm** **Kırılımları** **Topla:** Tahminleme verisi grup bazında oluşturulduğunda alt bölümdeki grid ekrandaki kayıtlar da gruplanarak gelmektedir. Bu grupların tümünü kapamak için bu buton kullabilir.

**Excel'e** **Aktar:** Tahmin kayıtları listesini excel'e aktarmak için kullanılacak butondur.

**Excel'den Yükle:** Bu özellik serbest veri girişi yönteminde aktif olmaktadır. Daha önceden serbest olarak girilen bütün kayıtları silerek seçilecek excel dosyadaki kayıtların toplu olarak kaydedilmesini sağlar. Excel'den yükleme seçeneği tıklandığında aşağıdaki gibi bir ekran üzerinden excel dosyanın bulunduğu yol istenmektedir.

![](../_assets/bf8f1c78bb69ac355d11.png)
Bu ekran üzerinden toplu şekilde tahmin kayıtlarının bulunduğu excel dosyası seçilerek "İleri" butonuna tıklanır. Sonraki ekranda ise tahmin kayıtları alanlarının excel dosyasında hangi kolonlara karşılık geldiği seçilmelidir. Excel'den tahmin kayıtlarının aktarılması için dosyada olması zorunlu kolonların boş bir biçimde şablon olarak oluşturulması için "Boş bir şablon yaratmak için buraya tıklayın" seçeneğine tıklanmalıdır.
![](../_assets/cf05e97b4f38fc2b609f.png)
Excel dosyasında aynı isimle bulunan kolon eşleştirmeleri otomatik sağlanmaktadır. Kolon başlıkları farklı ise eşleşme elle yapıldıktan sonra ileri butonuna tıklanarak aktarılacak kayıtların toplu halde listesi görülebilir. Liste üzerinden hatalı olan kayıtlar kırmızı ile gösterilerek durum açıklaması sütununda hatanın nedeni belirtilmektedir. Bu listedeki kayıtlar üzerinden güncellemeler yapılarak hatalı kayıtların düzeltmesi sağlanabilir.
![](../_assets/7feacd59dabbfa5f251f.png)
Gerek görülen değişikliklerden sonra "Aktar" butonuna tıklanarak ilgili excel listesi toplu halde tahmin kayıtlarına atılabilir. Tahmin kayıtlarıyla ilgili seçimler ve güncellemeler yapıldıktan sonra "İleri" butonuna tıklayarak bir sonraki sekmeye geçilebilir.

**AÜP Çalıştırma Sekmesi**

Bu sekme üzerinde kod ve periyot bazında müşteri siparişi, tahmin ve daha önceden kaydedilmiş ana üretim miktarları raporlanabilmektedir. Güncel duruma uygun olarak tekrardan üretim miktarlarını hesaplamak için "AÜP Çalıştırma" butonuna tıklanabilir, ardından hesaplanan yeni üretim miktarlarını kaydetmek için ekranın sağ alt köşesindeki "Kaydet" butonu kullanılmalıdır.
Ekranın sol üst bölümündeki "AÜP Çalıştırma Parametreleri" bölümünden ana üretim planında kullanılacak parametreler seçilebilir. Bu parametreler MRP modül parametrelerinde belirlendiği şekliyle varsayılan olarak gelmektedir. Ancak işlemler öncesinde bu parametreler değiştirilebilir, farklı parametrelerle oluşacak sonuçlar incelenebilir.
Kapasite Planlama Yapılsın parametresi evet seçilerek AÜP çalıştırıldığında üretim planı kapasiteye uygun şekilde oluşturulmaktadır. İstasyon ve makinelerde oluşacak kapasite doluluk oranları, seçilen vardiya planı dikkate alınmaktadır.
Ekran sol orta bölümünde stok kodlarının listesi bulunmaktadır. Seçilen koda ait güncel bilgiler ekranın sağ bölümünde raporlanabilir.
Sağ üst bölümde AÜP tablosu bulunmaktadır. Bu tabloda seçili olan kod için AÜP hesabına dahil edilecek bilgiler (müşteri siparişi ve tahminleme miktarları), son olarak kaydedilmiş olan AÜP miktarları ve bu miktarlara göre hesaplanan mevcut değerler periyotlar bazında raporlanmaktadır (Düzeltilmiş ihtiyaç miktarı, Teslim edilebilir miktar vs.). Tekrardan AÜP çalıştırıldığında bu değerler güncellenecektir. AÜP tablosu üzerinde sağ tıklayarak "detaylı görünüm" seçildiğinde daha detaylı bilgilere ulaşılabilir.
Sağ alt bölümde ise AÜP tablosundaki değerlerin zaman ekseninde grafiği izlenebilir.
![](../_assets/e703bdda85722d27dbdd.png)
Ekranın sol alt bölümündeki "Stok Planlama Bilgileri" bölümünde seçili olan koda ait stok planlama bilgileri raporlanabilir.
Teslim Edilebilir Miktar (Available To Promise): Dönem bazında ilgili stok için ne kadarlık bir sipariş ihtiyacının karşılanabileceğini doğrulamak için hesaplananan bir değerdir.
AÜP miktarları hesaplandıktan sonra seçili olan düzleme yöntemi parametrelerine göre müşteri siparişlerinin karşılanacağı periyodlar belirlenir ve buna göre düzeltilmiş müşteri siparişi, düzeltilmiş ihtiyaç miktarı, hedeflenen bakiye ve teslim edilebilir miktar değerleri tekrardan hesaplanır.
Sipariş düzleme işlemlerinin AÜP miktarlarına bir etkisi yoktur. Düzleme işlemleri sonrasında müşteri siparişleri ve düzeltilmiş müşteri siparişleri satırları karşılaştırılarak aradaki farklar gözlenebilir.

**AÜP Sonuçları Sekmesi**

Kaydedilmiş olan AÜP sonuçları bu ekran üzerinden raporlanabilir ve üzerinde değişiklik yapılabilir.
Bu sekmedeki kullanıcı miktarı kolonu, hesaplanan değerler olarak getirilir ve üzerinde değişiklik yapılabilir. Orijinal AÜP miktarları da bozulmadan miktar kolonunda yer alır.
![](../_assets/e1470ee20f223144e47d.png)

**Ana Üretim Planı Bilgilerinin Gereksinim Planlamaya Aktarılması**

Ana üretim planındaki üretim miktarlarının işletme kapasitesine uygunluğunu belirlemek ve malzeme satın alma planını oluşturmak için, planın MRP'ye aktarılması ve plana ait MRP çalıştırılması gerekmektedir.
Planın MRP'ye aktarımı için, gereksinim planı oluşturma ekranında ihtiyaç tipi olarak "AÜP" seçilmelidir.
Not: Bu seçeneğin seçilebilmesi için MRP parametrelerinde "sipariş bazında rezervasyon sistemi" parametresinin işaretli olması gerekmektedir.
![](../_assets/7f0d44d0fb05ba663800.png)
Gereksinim planına aktarılan ihtiyaçlar, planlanan ihtiyaçlar ve müşteri siparişlerinden kaynaklanan ihtiyaçlar olarak, sipariş detay bilgileri ile birlikte ayrıştırılıp aktarılacaktır.

**Ana Üretim Planı Bilgilerinin Müşteri Siparişinde Kullanılması**

Ana üretim planlama sonucunda hesaplanan teslim edilebilir miktar değerleri fatura modülünden girilecek müşteri siparişleri sırasında kullanılabilmektedir. Bu şekilde satış ekibi ile planlama ekibi arasında ortak bir değer üzerinden iletişim kurulabilmesi amaçlanmakta ve satış ekibinin gireceği sipariş sırasında plana uygunluk kontrolünü yapabilmesi mümkün olmaktadır. Böylece müşteri siparişi girilirken hangi teslim tarihine ne kadarlık teslimat yapılabileceği raporlanabilmektedir.
İlgili fonksiyona müşteri siparişi ekranı kalemler sekmesinde stok kodu girildikten sonra sağ tıklanarak ulaşılabilir.
*Not: Ana üretim planlama işlemlerinin müşteri siparişi ekranında kullanılabilmesi için AÜP ek lisansı bulunmalıdır.* *Ayrıca* *satış* *fatura* *parametelerinden* *"sipariş* *kaydında* *her* *satırda* *teslim* *tarihi* *sorulsun"* *seçeneği* *işaretli* *olmalıdır.* *(Satış* *fatura* *parametreleri* / *Fatura Sipariş* *sekmesi)*
![](../_assets/787448354a7672e428b1.png)
![](../_assets/ddb5ce6296be15be83fb.png)
Bu rapor ekranı üzerinde girilen miktar ve teslim tarihine göre ana üretim planına uygun teslimat önerileri sunulmaktadır. Eğer ilgili miktarın bulunuğu periyotta yeterli teslim edilebilir miktar var ise siparişin teslim tarihinde sorun yoktur ve farklı bir öneri sunulmayacaktır. Ancak istenilen teslim tarihinde girilen miktarı karşılayacak teslim edilebilir miktar (ATP) yok ise sipariş düzleme yöntemleri kullanılarak yeni teslimat önerileri sunulmaktadır. Kullanıcı bu önerileri kabul eder ise ilgili öneriler sipariş kalemlerine otomatik olarak yansıtılacaktır. Kullanıcı bu önerileri kabul etmez ise girilen teslim tarihine tek bir satır olarak kayıt atılacaktır. Ancak önerileri kabul etmeyerek kaydedilen müşteri sipariş kalemleri sonrasında ana üretim planına uygun olmayan durumlar oluşabilir ve bu durumu düzeltmek için planlama ekibinin tekrardan ana üretim planı çalıştırması gerekmektedir.
Örneğin; Ana üretim planlama bilgileri aşağıdaki gibi olan bir stok için müşterinin 12.03.2022 (10. Hafta) tarihine 600 adet ürün istediğini varsayalım. Ana üretim planlama sonucunda 10. periyotta teslim edilebilir stok miktarı 140 olarak hesaplanmıştır. İlgili periyot için bu miktardan fazlası stok bakiyesinde probleme neden olacağından 600 adetlik siparişin bir kısmı 10. haftaya kalan sipariş bakiyesi ise diğer periyotlara ana üretim planına uygun şekilde dağıtılmaktadır.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 2022 / 9 | 2022 / 10 | 2022 / 11 | 2022 / 12 | 2022 / 13 | 2022 / 14 | 2022 / 15 | 2022 / 16 |
| Tahminleme Miktarı | 146,00 | 140,00 | 141,00 | 135,00 | 168,00 | 171,00 | 168,00 | 139,00 |
| Müşteri Siparişleri | 123,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| Düzelt. İhtiyaç Miktarı | 146,00 | 140,00 | 141,00 | 135,00 | 168,00 | 171,00 | 168,00 | 139,00 |
| Teslim Edilebilir Miktar | 23,00 | 140,00 | 141,00 | 135,00 | 168,00 | 171,00 | 168,00 | 139,00 |
| **AÜP** **Miktarı** | **146,00** | **140,00** | **141,00** | **135,00** | **168,00** | **171,00** | **168,00** | **139,00** |

Ekranda belirtilen teslimat önerileri "Siparişe Kaydet" butonu ile onaylanabilir. Onaylanan teslim tarihlerine göre sipariş kalemleri belgeye otomatik olarak yansıtılmaktadır.
![](../_assets/f49adbf5253693a4f6b5.png)![](../_assets/e20d56b63d70c4d8df1c.png)
