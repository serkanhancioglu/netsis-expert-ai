---
title: "Devirsiz Çalışma Sıkça Sorulan Sorular"
page_id: "128583663"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Devirsiz Çalışma Sıkça Sorulan Sorular"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Devirsiz Çalışma Sıkça Sorulan Sorular"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTQzMTIwZmI1LTM1NzgtNGU3YS04OTBlLTkzMjZhY2M3NjNlYiZsaW5rPTljMjQ0ZDg4LTJhMjktNGYxYS1iM2Y4LWQ5NmIwY2VmMmUxMiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=43120fb5-3578-4e7a-890e-9326acc763eb&link=9c244d88-2a29-4f1a-b3f8-d96b0cef2e12&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "devirsiz-calisma-sikca-sorulan-sorular_134054786_128583663.html"
source_version: "2024-03-13T08:24:06.867+03:00"
source_bytes: 152599
fetched_at: "2026-09-13T04:22:58+00:00"
generator: "netsis-scraper 1.0.0"
---
# Devirsiz Çalışma Sıkça Sorulan Sorular

**Soru 1:Devirsiz çalışma hangi setle desteklenmiştir?**

Devirsiz çalışma 9.0.43 seti itibariyle desteklenmiştir.

**Soru 2:Devirsiz çalışma hangi paketlerde desteklenmektedir?**

Devirsiz çalışma Logo Netsis 3 Entegre, Logo Netsis 3 Standard, Logo Netsis 3 Enterprise, Logo Netsis Wings Entegre, Logo Netsis Wings ve Logo Netsis Wings Enterprise paketlerinde desteklenmektedir.

**Soru3 : Devirsiz çalışma için program tarafında yapılması gereken tanımlamalar nelerdir?**

Devirsiz çalışma için programda herhangi bir tanımlaya ihtiyaç duyulmamaktadır. Mevcut database(şirket) üzerinde çalışılmaya devam edilecektir. Bu durumda yeni yıl kopyalama ve modül devri işlemleri yapılmayacaktır.

**Soru 4: Devirsiz çalışmanın avantajları nelerdir?**

- Yeni yıl şirketi oluşturma ve modül devri işlemlerine ihtiyaç duyulmamaktadır.
- e-Belgelerin gönderimi mevcut şirketten yapılacaktır.
- Yeni şirket oluşturulmayacağı için kullanıcıların yetkilendirme işlemine gerek kalmayacaktır. Ancak hali hazırda kullanılan tarih kilitleme uygulaması varsa kısıtlanacak tarih aralığı güncellenmelidir.
- e-Faturaların doğru şirkete düşmesi için e-devlet ayarlarının yapılması ihtiyacı ortadan kalmış olacaktır.
- Netopenx /Rest third party uygulamaları için db connection değişikliğine gerek kalmayacaktır.
- Devirsiz çalışma ile yeni eklenen Yıl Kodu bilgisine göre aynı şirket içinde farklı yılların tutulması sağlandığından muhasebe raporları için eski yıl şirketlerine geçiş yapılmasına gerek kalmamıştır. (Ancak devirsiz çalışmadan önceki yıllara eski yöntemdeki gibi geçmiş yıl şirketlerine geçiş yapılarak bakılabilir.)
  - Devirsiz çalışma ile hibrit çalışma imkanı sağlanmıştır.Bir süre devirsiz çalışıldıktan sonra istenilen bir dönemde tekrardan devirli çalışma sistemine geçilebilir. Aynı hibrit çalışma durumu devirli çalışma için de geçerlidir.

**Soru 5: Dönem sonu muhasebe kapanış/açılış işlemleri devirsiz çalışmada nasıl yapılmalıdır?**

Muhasebe\\İşlemler\\Dönem Sonu İşlemleri program yolundan Dönem Sonu Kapanış-Açılış İşlemi ekranından Dönem Sonu Kapanış Fişi sekmesinden öncelikle kapanış fişi oluşturulur. Daha sonra Dönem Başı Açılış Fişi sekmesine geçerek, oluşturulmuş kapanış fişini baz alarak açılış fişi oluşturulur. Oluşan açılış fişi sonrasında ilgili şirket altında TBLDEVIRSIZLOG adlı tabloya yeni dönem için açılış fişi numarası ve bu fişe ait ay/yıl bilgisi atılmaktadır. Manuel yapılan açılış fişlerinde bu tabloda belitilen kayıt oluşmamaktadır.

TBLDEVIRSIZLOG tablosunda oluşan açılış fişi kaydının bitiş tarihi bilgisi dikkate alınarak Netsis database altındaki SIRKETLER30 tablosunda ilgili SIRKETYILI bilgisi de güncellenecektir.

Yeni geçiş sonrasında oluşturulan açılış fişinin silinmesi durumunda TBLDEVIRSIZLOG tablosundaki açılış kaydı bilgisini silip SIRKETLER30 tablosundaki SIRKETYILI bilgisini geri çekecektir. (2023 kapanış, 2024 açılış olduğu durumda şirket yılını 2024'den 2023 yılına geri çekecektir.)

TBLDEVIRSIZLOG tablosunda her yıl yapılan açılış fişi kaydı sonrasında kayıt oluşacaktır. (2023,2024,2025,...)Programda herhangi bir yıla ait açılış fişinin silinmesi durumunda TBLDEVIRSIZLOG tablosundaki en yakın tarihli bitiş tarihi satırı dikkate alınarak SIRKETLER30 tablosunun SIRKETYILI bilgisini güncelleyecektir.

Örneğin, (2023,2024,2025,2026 ) 4 yıldır devirsiz çalıştığımızı düşünürsek 2024 yılına ait açılış fişini silmemiz durumunda max. bitiş tarihi bilgisini kontrol ettiğinden SIRKETYILI bilgisi 2023 şeklinde geri sarılmayacak 2026 yılında kalacaktır.

![](../_assets/29b87d0c0bc758d396d5.png)

![](../_assets/5e5f371d994b9650b29f.png)![](../_assets/c499dc4d16d46e255b41.png)

**Soru 6: Devirsiz çalışma durumunda e-Fatura, e-Arşiv, e-İrsaliye ve e-Müstahsil gibi belgelerin yeni yıla geçişi sonrasında belge serisi nasıl düzenlenmelidir?**

Yıl geçişlerinde fatura/irsaliye/müstahsil kayıt girişinde üst bilgilerdeki 15 haneli belge numarası için önceki yıldan farklı bir seri tanımlanıp yeni seriden devam edilebilir. Mevcut seri ile devam edilmek istenirse de seri yanına yıl bilgisi eklenebilir. Yıl bilgisi eklenmesi durumunda fatura numarası ABC024000000001 ya da ABC202400000001 formatında oluşturulabilir. Resmi fatura numarası her iki durumda da ABC202400000001 şeklinde oluşacaktır.

**Soru 7: Devirsiz çalışma durumunda e-Defter ve e-Belgeler için e-devlet ayarlarının tanımı nasıl olmalıdır?**

Devirsiz çalışmada yeni şirket oluşturulmayacağı için e-devlet ayarlarında düzenleme yapılmasına gerek kalmayacaktır.

**Soru 8: Muhasebe modülü ekranlarındaki Yıl Kodu alanı hangi amaçla getirilmiştir?**

Muhasebe modülü altındaki yevmiye fiş girişi başta olmak üzere bir çok kayıt ve işlem ekranlarına hangi yıla ait işlemlerin yapılacağını belirtebilmek için Yıl Kodu alanı eklenmiştir. Bu alan boş geçilememektedir. Böylece girilen muhase kayıtları ayrıştırılmış olacaktır. YIL_KODU alanının eklendiği tablolar; TBLMUHFIS, TBLMUHFISEK, TBLMUHMAS ve TBLMUPLANSUBE tablolarıdır. Yevmiye fişi rehberinde de Yıl Kodu bilgisine göre sorgulama yapılabilmektedir.

**Soru 9: Tarih aralığı bulunmayan muhasebe modülü raporlarında Yıl Kodu alanı hangi raporlarda getirilmiştir.**

Aşağıda belirtilen raporlara yıl kodu alanı eklenmiştir. Bu sayede alınacak raporlara yıl kodu kısıtı verilerek istenen yıla ait veriler listelenecektir. Ayrıca hazırlanmış özel raporlara da yıl kodu alanının eklenmesi gerekmektedir.

- Yevmiye Fiş Listesi
- Klasik Yevmiye Fiş Listesi
- Borç/Alacak Karşılaştırma Raporu
- Mizan
- Yevmiye Defteri
- Aylık İcmal
- İşletme Bilançosu
- İşletme Gelir Tablosu
- Satışların Maliyeti
- Kapatılmamış Fişler
- Çalışmayan Hesaplar

![](../_assets/8568ccc66cbd00063aa6.png)
![](../_assets/61182610a5b85c97dae4.png)

**Soru 10: Devirsiz çalışma durumunda dönem sonu yansıtma fişleri nasıl oluşturulur?**

Yansıtma fişi oluşturma ve gelir hesapları kar zarar devir fişi işlemlerinde yıl kodu girişi yapılıp ay aralığı verilerek yansıtma fişleri oluşturulabilmektedir.

![](../_assets/24247bcb3e2a9a477862.png)

**Soru 11: Özel hesap dönemi kullanılması durumunda devirsiz çalışma işlemleri nasıl yürütülür?**

Özel hesap dönemi başlangıç ayı olarak muhasebe parametrelerinde belirtilmektedir. Bu şekilde tüm ekranlarda yıl ve ay bilgisi mevcuttur. Program altyapısal olarak özel dönem kullanılan durumda muhasebe parametrelerindeki ay ve dönem yılı ile onu takip eden 12 aylık dönemi kontrol etmektedir.

**Soru 12: Lojistik/Satış, Finans ve Üretim kategorilerine ait modül hareketleri devirsiz çalışma durumunda aktif yıl hareketleri nasıl ayırt edilebilir?**

Fatura, Stok, Cari, Çek/Senet, Dekont, Banka, Sipariş, Talep/Teklif, İthalat/İhracat İşlemleri ve Üretim modüllerinde rehberlerde, hareket kayıtlarında yıl kısıtı olmaksızın tüm kayıtlar görülebilecektir. Ancak rapor alınırken tarih aralığı verilerek ilgili yıla ait bilgiler süzülebilir.

**Soru 13: Devirsiz çalışmanın database boyutuna etkisi nasıl olacaktır?**

Devredilmediği için yıllar boyunca bilgiler tek bir database altında birikeceğinden database boyutu büyüyecektir. Fakat istenildiği takdirde tekrar devirli çalışma şekline dönülebilmektedir.

**Soru 14: Devirsiz çalışma durumunda e-defter oluşturma işleminde dikkat edilmesi gereken hususlar nelerdir?**

Defter oluşturma öncesinde yapılan Hazırlık Bilgi Girişi ekranına Yıl Kodu bilgisi eklenmiştir. İlgili yıl ve ay bilgisi seçilerek hazırlık oluşturulacaktır. Defter oluşturma esnasında yıl ve ay bilgisi seçilmesi durumunda muhasebe fişlerinde seçilen yıl ve ay bilgilerindeki fişleri baz alarak e-defter oluşturacaktır. E-Defter Onaylama ekranında bulunan ay ve yıl seçimine göre defter oluşturulur. Buradaki yıl bilgisi alanındaki seçenekler Muhasebe/Kayıt menüsü altındaki Mükellef ve Düzenleyen Bilgileri
ekranından Dönem Bilgileri sekmesindeki Dönem Başlangıç ve Bitiş Tarihi alanlarından getirilmektedir.
![](../_assets/77074d84f2b35ed46999.png)

![](../_assets/3f595924a2eac988bae5.png)

SQL Express Edition versiyonlarında devirsiz çalışma desteklenmektedir. SQL Express Edition kullanımı olması durumunda, SQL'in Express Edition için desteklediği maksimum database boyutunun 10 GB olduğu göz önünde bulundurulmalıdır. Bu durumda belirli yıllar devirsiz çalışıp boyut olarak database 10 GB sınırına yaklaştığında devirli çalışma durumuna geçiş yapılabilir.

**Soru 15: SQL Express Edition kullanımında devirsiz çalışma desteklenmekte midir?**

SQL Express Edition versiyonlarında devirsiz çalışma desteklenmektedir. SQL Express Edition kullanımı olması durumunda, SQL'in Express Edition için desteklediği maksimum database boyutunun 10 GB olduğu göz önünde bulundurulmalıdır. Bu durumda belirli yıllar devirsiz çalışıp boyut olarak database 10 GB sınırına yaklaştığında devirli çalışma durumuna geçiş yapılabilir.
