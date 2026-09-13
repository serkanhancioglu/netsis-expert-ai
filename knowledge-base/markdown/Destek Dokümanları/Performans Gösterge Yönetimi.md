---
title: "Performans Gösterge Yönetimi"
page_id: "104104454"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Performans Gösterge Yönetimi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Performans Gösterge Yönetimi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTMxMDU1ZGFkLTUwZDgtNDg1NS04N2U3LTFmMTZkOTRmYTI3MyZsaW5rPTM3MGIzNjM3LWFkYTgtNGU0Mi04NWMxLWNmMzBjZTQ1YzFkNiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=31055dad-50d8-4855-87e7-1f16d94fa273&link=370b3637-ada8-4e42-85c1-cf30ce45c1d6&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "performans-gosterge-yonetimi_104104474_104104454.html"
source_version: "2023-02-06T13:51:33.820+03:00"
source_bytes: 677924
fetched_at: "2026-09-13T04:23:40+00:00"
generator: "netsis-scraper 1.0.0"
---
# Performans Gösterge Yönetimi

Performans gösterge yönetimi hakkında ayrıntılı bilgiye bu dokümandan ulaşılır.

9.0.44 sürümü ile sürdürülebilirlik kapsamında performans göstergelerinin tanımlanması, verilerinin girilmesi ve görsel raporların hazırlanması desteklenmiştir. Bu geliştirme ile Yardımcı Programlar menüsü altına Performans Gösterge Yönetimi ekranları eklenmiştir.

![](../_assets/a850c8af5aa8c08ba1ce.png)

**Boyut ve Değer Tanımlama**

Boyut tanımlama ekranı ile performans değerlendirmesine tabi tutulacak verilerin hangi bilgilerden (kolonlardan) oluşacağı belirlenecektir. Boyut ve Değer Tanımlama ekranında "Boyut Tanımları" sekmesi ile boyutlar tanımlanır ve "Değer Tanımları" sekmesi aracılığı ile ilk sekmede tanımlanan boyutların alabileceği değerler tanımlanabilecektir.
Boyut Kodu: Kullanılmak istenen boyut kodu bilgisi girilir.
Açıklama: Kullanıcı tanımlamamak istediği boyut için açıklama bilgisi girilir.
Sadece Tanımlı Değerler Kullanılsın: Bu seçenek işaretli ise veri girişi gerçekleştirilirken kullanıcının sadece her bir boyut için tanımlanacak olan değerlerden birini seçebilmesi sağlanacaktır, yani boyutlar için tanımlanan değerler hariç herhangi bir değer veri girişi ekranında girilemeyecektir. Varsayılan olarak işaretsiz gelmektedir.

İlgili bir boyut gösterge tanımında kullanıldıysa ilgili boyut silinmek istendiğinde kullanıcıya "Boyut tanımı gösterge tanımında kullanılmıştır" şeklinde bir uyarı mesajı vererek silinmesine izin verilmemektedir.

İlgili seçenek işaretli değil ise değer tanımlarındaki tanımlamaların dışında veri girişine de izin verilir.

Değer: Seçilen boyutun alabileceği değerler bu alanda tanımlanır.

![](../_assets/0050f470224151424338.png)![](../_assets/0607a4a9f2260a893294.png)

**Performans Gösterge Tanımları**

Performans gösterge tanımları ekranında öncelikle göstergenin ana tanımı yapılır. Bu tanımda göstergenin ait olduğu başlangıç ve bitiş tarihi, göstergenin sorumlu kişileri, veri girişi ekranından girilecek değer verisinin birim bilgisi yer alır. İstenirse burada tanımlanan göstergeler için bitiş tarihine belirli bir gün kala kullanıcılara hatırlatıcı mesajı gönderilebilir.

![](../_assets/d458fe0f99a8366ec382.png)

**Gösterge Tanımı**

Gösterge Kodu: Kullanıcı tanımlamak istediği gösterge için (KPI) tekil olarak bir kod girilir.

Aktif: Göstergenin aktif/pasif olması bu alan ile takip edilir.

Açıklama: Tanımlanan gösterge için belirlenecek bir açıklama bilgisidir.

Başlangıç Tarihi: Göstergenin başlangıç tarihi bilgisi girilir.

Bitiş Tarihi: Göstergenin bitiş tarihi bilgisi girilir.

Belirtilen Tarihler Dışında Veri Girilemesin: Bu seçenek işaretli ise Veri Giriş ekranından veri girişi gerçekleştirilirken başlangıç tarihinden önce veya bitiş tarihinden sonrasında herhangi bir veri girişine izin verilmez.

Sorumlu Kişi: Bu bölümde birden fazla sorumlu kişi girilebilir, rehber üzerinde Netsis kullanıcıları getirilir.

Sadece Sorumlu Kişiler Veri Girebilsin: Bu seçenek işaretli ise sadece sorumlu kişi alanında tanımlı Netsis kullanıcıları bu gösterge için veri giriş işlemini yapabilir. Eğer sorumlu kişi alanı boş ise bu gösterge için tüm kullanıcılar veri girişi yapabilecektir.

Gösterge Birimi: Veri girişi ekranından girilecek olan değerlerin birim bilgisi raporlama amacıyla bu alana yazılacaktır.

Gruplama Fonksiyonu: Performans göstergeleri hesaplanırken kullanılacak gruplama fonksiyonu seçilir. "Toplam", "Ortalama", "Maksimum", "Minimum" fonksiyonları desteklenmektedir.

Hatırlatıcıya Ekle: Bu ekran ile göstergenin bitiş tarihinden, hatırlatma tarihi alanında seçilen gün sayısı kadar geriye gidilerek bu tarihte seçili kullanıcılar için hatırlatma kaydı oluşturulabilir.

Ekran açıldığında tüm Netsis kullanıcıları listede gelecektir ve sorumlu kişi alanında seçilen Netsis kullanıcıları bu ekrandaki kullanıcı listesi alanına otomatik olarak seçili gelir. İstenirse yanındaki rehber butonunu tıklayarak bu kullanıcılar düzenlenebilir.

![](../_assets/e76dd53e7c1042ba10c7.png)

![](../_assets/a23a91ed751f44db27c4.png)

**Boyut Eşleştirme**

Boyut eşleştirme sekmesinde bu göstergede kullanılacak boyut tanımlamaları yapılır.

![](../_assets/a6cb0251580095dfa451.png)

Gösterge Kodu-Açıklaması: İlk sekmede seçilen göstergenin kodu ve açıklama bilgisi pasif olarak gösterilir.

Boyut Kodu: İlk sekmede seçilen gösterge için kullanılacak olan boyut bilgileri seçilir. Bu alanın yanındaki rehberde tanımlı boyutlar listelenecektir.

Sıra: Her bir boyut 1'den başlayarak otomatik olarak sıralanır. Boyutların sırası değiştirilmek istenirse Boyut Sıra alanındaki değeri manuel olarak düzenlenip kaydedilebilir. Sıra bilgisinin değiştirilebilmesi için ilgili göstergeye ait herhangi bir veri girişinin yapılmamış olması gerekmektedir.

Gruplamada Kullan: Seçilen toplam fonksiyonuna göre eğer ilgili boyutun gruplanması isteniyorsa bu seçenek işaretlenmelidir. Bir gösterge için birden fazla boyut için gruplamada kullanılsın seçilebilir.

Girilmiş olan verilerdeki değer alanının göstergenin değerlendirilmesi aşamasında hangi boyut/boyutlara göre gruplanacağı burada seçilen boyutlara göre yapılacaktır.

**Not:** Boyut eşleştirme sekmesi üzerinden herhangi bir boyut ekleme, silme işleminin yapılabilmesi için ilgili gösterge için herhangi bir veri giriş işleminin yapılıp yapılmadığı kontrol edilir. Veri girişi yapılmış olmasına rağmen yeni bir boyut eklenmek istenirse veya silme yapılmak istendiğinde kullanıcı "İlgili gösterge için veri girişi yapıldığından dolayı boyut eşleştirme tanımları değiştirilemez" şeklinde bir uyarı mesajı ile karşılaşılacaktır.

**Aralık Tanımları**

Belirlenen boyutlara göre bulunan gösterge sonuçlarının hangi aralığa dahil olduğunun tespiti yapılmaktadır.

Gösterge için aralık tanımlamaları bu sekme üzerinden yapılır. Bu tanımlama sırasında yazılan başlangıç ve bitiş değerleri kontrol edilirken buradaki değerlerin mevcutta tanımlı farklı bir aralığa karşılık gelip gelmediği kontrol edilir. Çakışma yaşanması durumunda *"Tanımlamaya çalıştığınız min ve maks aralıklar bu gösterge için tanımlı farklı bir aralığa dahil edilmiştir."* uyarısı ile karşılaşılacaktır.

![](../_assets/1fdafbd3077ae3cfe99f.png)
Gösterge Kodu-Açıklaması: İlk sekmede seçilen göstergenin kodu ve açıklama bilgisi pasif olarak gösterilir.

Değer Aralıkları (Min - Maks): Göstergelerin değerlendirmesi aşamasında bulunan değerin hangi aralığa girdiği bu tanımlamalar kontrol edilerek bulunur.

Değerlendirme Açıklama: Bu aralığa giren değerlerin raporlanacak açıklama bilgisi girilir.

**Dinamik Veri Tanımı**

Veri girişleri sadece manuel olarak değil otomatik olarak bir sistemden veya Excel' den getirilecek ise bu sekme üzerinde yazılacak olan script kodlar ile veri girişi sağlanabilir.

**Sürdürülebilirlik 360**

Bu sekmede sürdürülebilirlik 360 raporunda kullanılacak grafikler tanımlanır.

Grafik Türü: Bu alanda sürdürülebilirlik raporuna eklenecek grafik türü seçilir. Burada sütun grafik, pasta grafik, çizgi grafik, tablo gösterimi seçenekleri kullanılabilir.
Kayıt Sayısı: Grafiklerde gösterilecek kayıt sayısıdır. 0 yazıldığında herhangi bir kısıt olmadan tüm satırlar grafikte gösterilecektir.
Sıralama: Grafikte gösterilecek satırların değer alanına göre artan veya azalan olarak nasıl sıralanacağı seçilecektir.
Farklı Gösterge ile Karşılaştır: Bu seçenek ile mevcut grafiğin aynı boyutlara sahip farklı bir göstergedeki grafik ile ikili sütun veya ikili çizgi olarak izlenebilir. Bu alan Grafik Türü çizgi ve sütun seçildiğinde aktif olmaktadır.
Karşılaştırılacak Gösterge: "Farklı Gösterge ile Karşılaştır" seçeneği işaretlendiğinde aktif olur. Aynı boyutlara ve aynı gruplama boyutlarına sahip diğer bir göstergeyi seçebilir.

Örneğin 2021 yılındaki kayıtları değerlendiren "2021 Satışlar" adındaki bir gösterge ile "2022 Satışlar" adındaki iki gösterge karşılaştırılmak istenebilir. Her iki göstergenin de Plasiyer, Proje, Bölge, Yıl boyutları olduğunu ve gruplama boyutunun Plasiyer olduğunu düşündüğümüzde bu iki grafik için hesaplanan değerler karşılaştırılırken grafiğin X eksenine plasiyerler yazılacak ve her bir plasiyer için ikili sütun grafiği çizilecektir. Sütunlardan biri bir göstergeden gelen değeri, diğeri ikinci göstergeden gelen değeri gösterecektir.

**Not:** Sürdürülebilirlik 360 raporundaki "Veri Seçimi" butonuna aktif olan göstergelerin "Sürdürülebilirlik 360" sekmesinde belirlenen görseller dinamik olarak eklenecektir. Kullanıcı raporlamak istediği görseli buradan seçtiğinde Sürdürülebilirlik 360 raporunda görüntülenecektir.

"Farklı Gösterge ile Karşılaştır" seçeneği işaretli ise grafik türü olarak sütun grafik seçilmiş ise grafiği çizerken ikili sütun grafik çizilecektir, benzer şekilde çizgi grafik için de ikili çizgi grafik çizilecektir.

![](../_assets/af82a5142cc6d425317b.png)
![](../_assets/42c0911858cf7acd1c41.png)

**Performans Göstergesi Veri Girişi**

Veri girişleri bu ekran üzerinden gerçekleştirilir.

![](../_assets/2eb045875788ee4afbb5.png)

Gösterge Kodu: Veri girişi yapılmak istenen aktif durumdaki gösterge kodu burada seçilir.

Boyut Alanları: Form üzerinde boyutlar için sabit 10 adet alan eklenebilir. Seçilen gösterge için belirlenen boyutlar, gösterge tanımında belirlenen sıra ile form üzerindeki alanlara getirilir. Birinci boyut bilgisi form üzerindeki birinci alana yazılır ve bu alanın yanındaki comboboxda ilgili boyut için tanımlanan değerler getirilir. Boyut tanımındaki "Sadece Tanımlı Değerler Kullanılsın" seçeneği işaretli ise bu alanda sadece tanımlı alanlar seçilebilir, manuel girişe izin verilmeyecektir. Eğer bu seçenek işaretli değil ise kullanıcı manuel veri girişi yapabilir.

Değer: Seçilen gösterge için belirlenen boyutlara ait değer bilgisi bu alana girilir.

Değer Birimi: Gösterge tanımında belirlenen gösterge birim bilgisi pasif olarak bu alana yazılacaktır.

Veri Kopyalama: Mevcut göstergedeki verilerin diğer göstergelere kopyalanmasını sağlar. Bu seçim yapıldıktan sonra "Aktarılacak Veri Seçimi" başlığında bir ekran daha çıkacaktır. Ekran ilk açıldığında ilgili kaynak gösterge için girilmiş tüm veriler gelecektir, kullanıcı burada aktarmak istediği kayıtları seçerek sadece seçtiği verilerin hedef göstergeye aktarılmasını sağlayacaktır.

![](../_assets/d9c753eeea931cbacce6.png)

![](../_assets/72c0501b79480db9eafb.png)

Dinamik Verileri Getir: Eğer seçili göstergenin "Dinamik Veri Girişi" sekmesinde yapılmış bir script tanımlaması mevcut ise bu buton aktif gelir. Varsayılan olarak tıklandığında "Dinamik Veri Girişi" sekmesinde tanımlanan script çalıştırılır.

Butonun yanında bulunan kulakçığa tıklandığında "Zamanlanmış Görev Ekle" seçeneği ile zamanlanmış görevler üzerinden dinamik kodlamanın çalışması sağlanabilir.

Gösterge tanımında "Sadece sorumlu kişi veri girebilsin" seçeneği işaretli ise ekranı açan kullanıcı eğer izin verilen bir kullanıcı değilse dinamik verileri getir işlemini de çalıştıramayacaktır.

![](../_assets/057a2e664da166d5d6cc.png)

**Performans Göstergesi Veri Giriş Raporu**

Veri girişi ekranından gerçekleştirilen veri girişleri gösterge ve boyut bazında tarih aralığına göre rapor alınabilmektedir.

![](../_assets/8e4e194a995aea37c15b.png)

![](../_assets/953bc389ae6e67e8cd94.png)

**Sürdürülebilirlik 360**

Sürdürülebilirlik 360 raporları ekranı üzerinden istenilen veri seçimleri yapılarak gösterge seçimlerine göre görsel grafikler hazırlanabilir.

![](../_assets/25d35ca4b0edf6b2b442.png)
