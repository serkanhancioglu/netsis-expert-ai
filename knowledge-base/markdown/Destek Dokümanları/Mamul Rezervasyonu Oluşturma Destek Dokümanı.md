---
title: "Mamul Rezervasyonu Oluşturma Destek Dokümanı"
page_id: "50684710"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Mamul Rezervasyonu Oluşturma Destek Dokümanı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Mamul Rezervasyonu Oluşturma Destek Dokümanı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTAzOWFkZTk5LWM4N2ItNDY1NS1iMjQ3LWMyMGU5YjcxNmZkMSZsaW5rPTkxYTdlNTBmLTFiMjEtNDBlNC1iMjM2LTVlZjUwMGUxZjBlYyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=039ade99-c87b-4655-b247-c20e9b716fd1&link=91a7e50f-1b21-40e4-b236-5ef500e1f0ec&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "mamul-rezervasyonu-olusturma-destek-dokumani_90669811_50684710.html"
source_version: "2022-11-03T09:57:02.620+03:00"
source_bytes: 1248355
fetched_at: "2026-09-13T04:26:32+00:00"
generator: "netsis-scraper 1.0.0"
---
# Mamul Rezervasyonu Oluşturma Destek Dokümanı

Mamul Rezervasyonu Oluşturma ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Mamul rezervasyonu oluşturma ekranı sayesinde daha önceden herhangi bir müşteri siparişine rezerve edilmemiş serbest mamul stoklarının toplu bir şekilde siparişlere rezerve edilebilmesi ve daha önceden yapılmış
rezervasyonların iptali mümkündür.

Mamul rezervasyonu oluşturma ekranının kullanılabilmesi için; MRP parametrelerinden "Sipariş Bazında Rezervasyon Sistemi" parametresinin işaretli olması gerekir, aynı zamanda Satış Parametreleri/Fatura Sipariş sekmesinde "Siparişte Stoktan Ayırma Yapılsın" parametresi işaretli olmamalıdır. Bu parametre işaretli ise sistemde sipariş bazında rezervasyon açık olsa bile Mamul Rezervasyon Oluşturma ekranı gelmez. Bu ekrana MR İşlemler menüsü altından ulaşılabilir.

Halihazırda üretimi yapılan mamul bakiyelerinin müşteri siparişine rezervasyonu; müşteri sipariş bağlantısı olan bir iş emri ile üretim sonu kaydı yapıldığında otomatik olarak giriş yapan mamul bakiyesi müşteri siparişine rezerve edilir, müşteri sipariş bağlantılı depolar arası transfer kaydı sayesinde mamul rezervasyonu yapılabilir olarak iki şekilde desteklenmekteydi.

Mamul rezervasyonu oluşturma ekranı sayesinde DAT kaydına gerek duymadan mamul bakiyelerinin bulundukları depolara rezerve edilebilmesi de desteklenmiştir. Eğer mamul bakiyesinin kendi deposu üzerinde rezervasyonu
istenmiyorsa bu ekran üzerinden DAT kayıtları da oluşturulabilmektedir.

![](../_assets/d90742a0abd727185d7b.png)

Mamul rezervasyonu oluşturma ekranı üzerinde; Müşteri Siparişine Mamul Rezervasyonu ve Mamul Rezervasyon İptali olmak üzere iki farklı işlem yapılabilmektedir.

**Müşteri** **Siparişine** **Mamul** **Rezervasyonu** işlem tipinde öncelikle "Çıkış yapılacak depolar" bölümünden rezerve edilecek mamul bakiyesinin aranacağı depolar seçilmelidir. Daha sonrasında "Giriş yapılacak depolar" bölümünden mamul rezervasyonunun yapılacağı depo kodu seçilmelidir. Eğer mamul bakiyelerinin bulundukları depolar üzerinde rezervasyonu isteniyorsa "Mamuller bulundukları depoya rezerve edilsin" seçeneği seçilmelidir.

![](../_assets/058d4e9f136dc9063ac4.png)

Depo bilgilerinin girilmesinin ardından sipariş kısıtları sekmesine geçilerek gerekli görülen müşteri siparişi ve stok kısıtları verilebilir. "Kayıtları Getir" butonu sayesinde girilmiş kısıtlara uygun olan ve teslimatı tamamlanmamış açık müşteri siparişleri listelenmektedir. Listelenen müşteri siparişleri içinden tek tek seçim yapmak suretiyle işlem yapılabileceği gibi, tümünü seç butonu kullanılarak otomatik bir şekilde mamul bakiyesinin müşteri siparişlerine dağıtılması sağlanabilir.

![](../_assets/62b48c26724e8daa9a07.png)

Ekran üzerinde yapılan seçim işlemleri sırasında mamule ait stok bakiyesi yürüyen bir şekilde azaltılmaktadır ve güncel serbest stok bakiyesi ekranın alt kısmında gösterilmektedir. Seçim işlemleri ardından yapılacak rezervasyon miktarları Rzv Edilecek Mik. alanına yazılmaktadır. Kullanıcı bu alan üzerinde değişiklik yaparak rezervasyon miktarlarını değiştirebilmektedir. Daha önceden yapılmış olan rezervasyon işlemleri "Rzv Mik." alanında kümüle olarak gösterilmektedir. Son aşamada "Rezervasyonları Oluştur" butonu yardımıyla toplu bir şekilde mamul rezervasyon işlemi yapılmaktadır. Yapılan rezervasyon işlemleri son sekmede raporlanmaktadır.

![](../_assets/110bffe350019a2dbd4e.png)

**Mamul** **Rezervasyon** **İptali** işlem tipinde öncelikle "giriş yapılacak depolar" bölümünden daha önceden yapılmış mamul rezervasyonlarının hangi depolarda aranacağı seçilmelidir. Daha sonrasında sipariş kısıtları sekmesine geçilerek gerekli görülen kısıtların verilmesinin ardından "Kayıtları Getir" butonu yardımıyla rezervasyon miktarı sıfırdan büyük olan açık müşteri siparişleri listelenir. Listelenen rezervasyon satırları toplu bir şekilde iptal edilebileceği gibi satır bazında tek tek iptal etmek de mümkündür.
![](../_assets/07c86efced7a74ecc753.png)

Rezervasyon iptali yapılacak olan siparişin istenirse tüm bakiyesinin istenirse belirlenen miktar kadarlık kısmının rezervasyon iptali gerçekleştirilebilir. Bunun için Serbest Bırakılacak Miktar alanına iptal edilecek bakiye miktarı yazılmalıdır.

Ardından Rezervasyon İptali butonu ile seçilen siparişler için rezervasyon iptali gerçekleştirilir.

![](../_assets/e34e48cdf4b0e61353d9.png)

İptal işlemi sonrasında sipariş miktarı, rezerve miktar ve ne kadarlık miktar kaldığı aynı ekran üzerinden izlenebilmektedir.

![](../_assets/3d98f9dab95ed3814881.png)

**Ek bilgiler**

MRP Parametreleri - "Sipariş Bazında Rezervasyon Sistemi" parametresinin aktif olmasıyla, MRP modülü işlemlerinin altında "Mamul Rezervasyonu Oluşturma" kullanılarak siparişe rezerve yapılıyor. Aynı mamulün başka siparişi ile satış irsaliyesi kesilmesi istendiğinde Üretim Parametreleri - "Rezerve ve Serbest Bakiyelere Bakılsın" ve Satış Parametreleri - "Eksi Bakiye Kontrolü", "Sipariş Stok Kontrolü" seçilmişse parametre koşulunun sağlanması durumunda serbest stok miktarı kadar siparişe irsaliye kesilmesi sağlanır.
