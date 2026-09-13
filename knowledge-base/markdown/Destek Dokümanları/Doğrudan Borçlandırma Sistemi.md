---
title: "Doğrudan Borçlandırma Sistemi"
page_id: "50691463"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Doğrudan Borçlandırma Sistemi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Doğrudan Borçlandırma Sistemi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWUyNzY1MWNlLTVkMmQtNDI4MS04OWNkLTVhYzJmNmUyMDU0MiZsaW5rPWM3M2NlNzIwLTA2YTUtNGRmYS1hYjQ0LWU2OWIyYTVhYjU4OCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=e27651ce-5d2d-4281-89cd-5ac2f6e20542&link=c73ce720-06a5-4dfa-ab44-e69b2a5ab588&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "dogrudan-borclandirma-sistemi_80090253_50691463.html"
source_version: "2022-11-02T16:07:53.430+03:00"
source_bytes: 1248477
fetched_at: "2026-09-13T04:25:08+00:00"
generator: "netsis-scraper 1.0.0"
---
# Doğrudan Borçlandırma Sistemi

Doğrudan Borçlandırma Sistemi ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Doğrudan borçlandırma sistemi ile firmanızın müşterilerine/bayilerine yapmış olduğu satışların tahsilat işlemlerini pratik bir şekilde yürütebilirsiniz. Sistem tarafından oluşturulan talimatların bankaya iletilmesinin ardından banka tarafında tahsilatlar takip edilecek ve otomatik olarak Netsis ERP sistemine yansıtılabilecektir. Tahsilatlar, Netsis'te oluşan dekontlar yardımı ile kontrol edilebilecektir. Benzer şekilde olumlu-olumsuz tahsilat işlem sonuçları da izlenebilecektir.
Bankalarla ilgili doğrudan borçlandırma süreçlerinde kullanılacak kurum kod bilgileri Finans\\Banka\\Kayıt\\Banka Ana Kod Kayıtları ekranından ilgili banka için tanımlanmalıdır.
![](../_assets/384343374197de69e79b.png)
Bankaya gönderilecek dosyaların veya bankadan gelecek akibet dosyalarının içerik desenlerinin Netsis'de tanımlanması gerekmektedir. Vakıfbank için önceden desteklenen sabit bir desen kullanılmaktadır, diğer bankalar için DBS sistemini kullanmak isteyen müşterilerimiz, bankanın talep ettiği fatura gönderim ve akıbet dosya desenlerini Finans\\Banka\\İşlemler\\Dosya Desen Oluşturma ekranından oluşturmalıdır.

#### Desen Oluşturma

Desen oluştururken bu desenin Aktarım veya Akıbet olduğu bilgisini Desen Tipi bölümünde belirtmemiz gerekmektedir. Elinizde bulunan örnek dosyayı, dosya seç butonu ile Örnek Dosya bölümünde tanımlarsanız; desen detayları sekmesinden tanımlamaları yaparken, dosyada bulunan veriler size gösterilecek ve deseni daha kolay oluşturmanızı sağlayacaktır, zorunlu bir alan değildir.
![](../_assets/30651efaa83efa891465.png)

**Dosya Adı Banka Bilgilerine Göre Oluşturulsun** seçeneği işaretlendiğinde DBS, TÖS, çek veya senet aktarımlarında dosya adının banka ana kod kayıtlarındaki "Müşteri Numarası" ve "Kurum Kodları" alanlarında girilen bilgiler olarak gelmesi sağlanır.

#### Aktarım Desen Detayı

![](../_assets/00af220cc60630950b45.png)
Desen detayları üç bölümden oluşmaktadır; Başlık Bilgisi, Detay Bilgi, Alt Bilgi. Eklenen her saha için sıra no değeri, ilgili konum (başlık, detay veya alt bilgi) bazında otomatik olarak artmaktadır. Başlık ve alt bilgi için birden fazla satır desteklenmiştir. Eğer başlık veya alt bilgi birden fazla satırdan oluşuyorsa, satır numarasını arttırarak çok satırlı bir başlık veya alt bilgi oluşturulabilir.
![](../_assets/78f32effa481fb135b17.png)
Eklenen her sahadan sonra üst kısımdaki ön izleme ekranına da bu saha eklenir, böylece oluşturulan dosya deseni her an izlenebilir.
![](../_assets/812cee2838300b3361ff.png)
Desen bilgileri sekmesinde örnek dosya seçildiyse, desen detayları kısmında dosyanın içeriği görüntülenecektir. Ve bu kısımdaki bir veriyi fareniz ile seçtiğinizde sütun ve uzunluk bilgileri sahaları otomatik olarak doldurulacaktır.
Bağlantı tipi olarak üç farklı çeşit veri kullanılabilir; Sabit, Fonksiyonlar ve Veri Tabanı.

Sabit bağlantı tipini oluşacak dosya içine sabit bir değer yazmak için kullanabiliriz.

Fonksiyon olarak başlık ve detay bilgiler kısmında sistem tarihi, gün, ay, yıl, saat, dakika gibi sabit tanımlı fonksiyonlar kullanılabilir. Alt bilgilerde bunlara ek olarak; Toplam Fatura Sayısı ve Toplam Satır Sayısı sahaları da kullanılabilir.

Veri tabanı olarak, seçilen konum bilgisine göre farklı tablolar ve farklı sahalar gelmektedir. Başlık bilgisi seçildiğinde BNKHESSABIT ve BNKSABIT'de bulunan sahalar, Detay bilgi seçildiğinde CASABIT, CASABITEK, FATUIRS'deki sahalar kullanılabilmektedir. Ayrıca bağlantı tipi veritabanı olarak seçim yapıldığında script desteğimiz de mevcuttur.

Örnek script kullanımı aşağıdaki şekildedir.
![](../_assets/273f2a427cc23f403097.png)
Alt bilgi seçildiğinde ise sadece FATUIRS gelmektedir. (Detay bilgilerde sayısal bir saha kullanıldıysa, Alt Bilgilerde o sahaya SUM() fonksiyonu uygulanmış hali kullanılabilmektedir. Örneğin Detaylarda GenelToplam sahası kullanıldıysa, alt bilgilerde SUM(GenelToplam) sahası seçilebilecektir.)
Veri tabanı kısmında bir tablo ve saha seçildiğinde seçilen sahanın veritabanındaki uzunluğu sağındaki alanda gösterilmektedir. Güncelle butonu ile buradaki değeri uzunluk değerine aktarabiliriz. Uzunluk alanına, otomatik olarak getirilen değerden daha küçük bir değer girildiğinde; ilgili saha değeri, dosya içerisinde tam olarak görünmeyebilir.
Seçilen sahanın sayısal bir veri olup olmamasına göre ondalık, binlik ayracı ve ondalık ayracı bilgileri aktif olmaktadır.

#### Akıbet Desen Detayı

Akıbet desen tasarımı, aktarım desen tasarımı ile aynı şekilde yapılmaktadır. Buradaki tek fark, akıbet deseni hazırlarken bankadan gelecek olan durum kodlarını Detay Bilgi kısmında bir sahada tanımlanması gerekmektedir.
![](../_assets/6528d1e2e487c8c4d31b.png)
Durum Göstergesinin aktif olması için konum olarak detay bilgi ve bağlantı tipi sabit seçilmelidir. Ardından aktif olan Durum Detaylarını Görüntüle butonuna tıklandığında bankadan gelecek olan değerleri ve hangi değerin başarılı olarak kabul edileceği belirtilmelidir. Buraya tanımlayacağınız kodlar, bankadan bankaya farklılık gösterecektir. Durum Adı kısmına ise her bir değer için ekranda görmek istediğiniz kendi açıklamanızı girebilirsiniz.
Eklenecek değerlerden sadece birine Başarılı Durum seçilebilir, fakat birden fazla başarısız durum mevcut olabilir. Varsayılan olarak da bir saha tanımı yapabilirsiniz. Tanımlamalar bittikten sonra ,Fatura Akıbetleri ekranında durum kodlarının nasıl görüntüleneceğini Ön izleme butonu ile izleyebilirsiniz.
![](../_assets/50ccf43e9ccdd7609a36.png)
Akıbet işleminde kullandığınız bir desen üzerinde Durum Göstergesi olan saha üzerinde bir değişiklik yapmanıza izin verilmeyecektir.

#### Fatura Aktarımı

![](../_assets/7a99c6a7d8b1e2bd3783.png)
Firma tarafından sistem aracılığıyla bankaya iletilecek fatura bilgileri bu bölümden oluşturulmaktadır. Sorgulama seçenekleri kullanılarak daha önce bankaya aktarılmayan (tahsilat adayı) fatura listeleri görüntülenebilecektir. Görüntülenen faturalar içerisinde tahsilat sürecine dahil edilmek istenen faturalar seçilecektir. Ekran üzerinde işlemi kolaylaştırmaya yönelik bazı fonksiyonlar (tümünü seç-seçimleri kaldır) yer almaktadır.
Seçilen hesap Vakıfbank'a ait bir hesap ise Desen Kodu alanı pasif olacaktır, çünkü mevcut yapıda Vakıfbank ile sabit bir desen üzerinden çalışıyoruz. Diğer bankalara ait bir hesap kodu yazıldığında, sizden desen kodu seçmenizi isteyecektir.
Görüntüle seçeneği ile cari kartlarında kullanıcı tanımlı sahalar alanındaki alfasayısal sahası (KULL5S) dolu olan carilere ait satış faturaları seçimi yapılıp, dosya oluşturulur. Sonrasında dosyanın kaydedileceği yer belirtilerek oluşan dosya, bankaya iletilebilecektir.

#### Fatura Sorgulama

![](../_assets/66865270a7ec507226d9.png)
Bankaya iletilen fatura bilgileri bu bölümden izlenebilecektir. Sorgulama seçenekleri kullanılarak daha önce bankaya aktarılan fatura listeleri görüntülenebilecektir. Görüntülenen liste içerisinde banka gönderimi iptal edilmek istenen faturalarda değişiklik yapılabilecektir.

#### Fatura Akıbetleri

![](../_assets/e59c64f3bb1e7f7ae293.png)
Tahsilat akibetleri bu bölümden kontrol edilebilecektir. Seçilen hesap Vakıfbank'a ait bir hesap ise Desen Kodu alanı pasif olacaktır, diğer bankalarda desen kodu seçilmesi gerekmektedir. Bankadan alınan akibet dosyası seçilerek işlem başlatılacaktır. Dosya içeriği incelenerek ekrana ilgili faturaların banka tarafında gördüğü işlem neticeleri görüntülenecektir. Dosya kontrol sürecinde tespit edilen durumlar kullanıcı bilgilendirme ekranında görüntülenecektir. Entegrasyon işlemi ile görüntülenen ve başarılı şekilde tahsil edilen faturalar için sistemde dekont oluşturulacaktır.
![](../_assets/85107badb7bc9e0712cf.png)
![](../_assets/250a67ff7c30779a35dd.png)

#### Limit Risk Yönetimi

![](../_assets/f03ce62f05e55d69bee2.png)
![](../_assets/886a7da5ac216f7cf5ec.png)
Banka tarafında takibi yapılan ve müşterilere/bayilere ait limit-kredi detayları sisteme entegre edilecek ve yine bu bölümden incelenebilecektir. Limit Risk Akıbetleri bölümü yardımıyla bankadan alınan dosya seçilip; limit-risk dosyası sisteme entegre edilerek sistemdeki carilere ait limit-risk detaylarının güncellenmesi sağlanacaktır. Entegrasyon süreci banka abone numarası üzerinden yürütülmektedir. Abone numarası bilgisi, cari kartı KULL5S alanında tutulmaktadır. Limit Risk Kayıtları bölümü yardımıyla bankadan alınan limit-risk cari kısıt yardımıyla incelenebilecektir. Risk oran hesaplaması ile ilgili cariler de tespit edilebilecektir. Limit-risk işlemleri Vakıfbank için desteklenmektedir.
