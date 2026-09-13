---
title: "Firma Takvimi"
page_id: "24753241"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Genel"
  - "Yardımcı Programlar"
  - "Kayıt / Yardımcı Programlar"
  - "Firma Takvimi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Yardımcı Programlar / Kayıt / Yardımcı Programlar / Firma Takvimi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWY1NmVkN2MyLTMzNjAtNDRmNC05YTAxLTI2ZWI2NDgwNzQ2NyZsaW5rPWVjMThkNzdlLTFjYTgtNDQ1Ny1iN2Q3LTc3NGY1YWI2OWMxYiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=f56ed7c2-3360-44f4-9a01-26eb64807467&link=ec18d77e-1ca8-4457-b7d7-774f5ab69c1b&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "firma-takvimi_24753246_24753241.html"
source_version: "2022-10-05T09:37:02.330+03:00"
source_bytes: 120007
fetched_at: "2026-09-13T04:17:18+00:00"
generator: "netsis-scraper 1.0.0"
---
# Firma Takvimi

Firma Takvimi, Genel Bölümü'nde, "Kayıt/Yardımcı Programlar" menüsünün altında yer alır. Firma Takvimi, firma için genel veya özel takvimler hazırlanarak takvim kontrollerinin program tarafından otomatik olarak yapılması için kullanılan bölümdür. Böylece hafta tatillerinin, dini veya resmi tatillere denk gelen tarihlerin kullanıcı tarafından değil program tarafından takip edilmesi sağlanır. Ayrıca her cari için, farklı takvim ve çalışma günleri tanımlanarak, tek bir takvim yerine birçok takvime göre gün takibi de yapılabilir.

Firma Takvimi ekranı; Sabit ve Detay olmak üzere iki sekmeden oluşur.

**Sabit**

Sabit sekmesi, takvime ait bazı genel tanımlamaların yapıldığı sekmedir.

![](../../../../_assets/3f5067bb87d2e11878fe.png)

Firma Takvimi ekranı Sabit sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Firma Takvimi Ekranı |  |
| --- | --- |
| Kod | Tanımlanacak takvim için kod numarası girilen alandır. Takvim, bu alanda verilen kod ile program genelinde ekrana getirilebilir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile firma takvimi kod listesine ulaşılır. En fazla 10 sayısal karaktere sahip kod tanımlaması yapılabilir. Boş bırakılmaz. |
| Açıklama | Kod bilgisine ait açıklamanın girildiği alandır. |
| Sorgula | Takvimler tanımlanırken, hafta tatilleri, dini veya resmi tatillerin belirlenmesi gerekir. Program genelindeki modüllerde kayıt oluştururken, vade tarihi olarak çalışılmayan bir gün hesaplandığında, programın uyarı vermesi için kullanılan seçenektir. İşaretlendiğinde, çalışılmayan bir gün vade tarihi olarak girildiğinde, girilen günün tatil gününe denk geldiğini gösteren bir uyarı ekranı görüntülenir. Vadenin alınması istenen tarih sorgulanır. Yapılan seçime göre ileri veya geri bir çalışılan gün hesaplanır. İşaretlenmediği zaman uyarı ekranı ile karşılaşılmaz. Yapılan takvim tanımlaması baz alınarak, çalışılan vade günü program tarafından otomatik olarak değiştirilir. |
| Genel Rehber | Firma için geçerli olan genel bir rehber tanımlanması için kullanılan seçenektir. Her firma için sadece bir adet "Genel Rehber" tanımlaması yapılabilir. Tanımlanan bir rehberden sonra, başka bir rehber için "Genel Rehber" sorgulaması işaretlenmez. Her cari hesap için istenirse, ayrı bir takvim tanımlanabilir ve tanımlanan takvim kodu cari hesap kayıtlarında "Firma Takvimi" alanında belirtilir. Cari hesaba ait kartta "Firma Takvimi" alanı boş bırakılırsa, takvim hesaplaması için program "Genel Takvimi" baz alır. |
| Hafta Göster | "Detay" sekmesinde her hafta numarasının - kaçıncı hafta olduğu - kullanıcıyı bilgilendirmek için görüntülenmesini sağlayan seçenektir. İşaretlenmediği zaman, "Detay" sekmesinde yer alan takvimde sadece günler görüntülenir. |
| Bugünü Göster | Detay" sekmesinde içinde bulunulan günün tarihinin, kullanıcıyı bilgilendirmek amacıyla görüntülenmesini sağlayan seçenektir. İşaretlenmediği zaman, "Detay" sekmesinde yer alan takvimde sadece günler görüntülenir. |
| İşlem Türü (İleriye Git/Geriye Git) | İşlemler sırasında hesaplanan vade tarihinin kullanılan takvimde tanımlanan çalışılmayan bir güne denk gelmesi halinde, programın vade tarihinin ileri bir güne alınması için "İleriye Git", geri bir güne alınması için "Geriye Git" seçeneğinin kullanılması gerekir. **Örneğin** 18.12.2019 tarihinin Şeker Bayramına denk geldiği varsayıldığında, "İleriye Git" seçeneği işaretlendiğinde, program vade tarihine ilerideki ilk çalışma gününü getirir. Yani, 19.12.2019 takvim tanımlamasında, "Sorgula" seçeneği işaretlendiği zaman bu bilgi işlemler sırasında tekrar sorgulanır ve üzerinde değişiklik yapılabilir. Takvim tanımlamasında "Sorgula" seçeneği işaretli değilse, belirlemeye göre yeni vade tarihi otomatik olarak ileriye veya geriye alınır. |
| Hafta Başlangıcı | Takvimde görülmesi istenen haftanın başlangıç gününün belirlendiği alandı. Buradaki belirlemeye göre "Detay" sekmesindeki haftanın başlangıç günü değişir. **Örneğin** Hafta başlangıcı olarak "Çarşamba" gününün seçildiği varsayıldığında, takvimde haftanın ilk günü olarak "Çarşamba" günü gelir. Hafta başlangıç günü ile ilgili özel bir tanımlama yapılması için standart "Windows" takvim görüntüsü olan "Windows" seçeneğinin kullanılması gerekir. Son alan da - Hafta Başlangıcı - belirlendikten sonra klavyedeki \<tab\> tuşu ile ilerleyerek takvim kaydedilir. Aynı takvim kaydının ekrana getirilmesi sağlanarak "Detay" sekmesine geçildikten sonra detayların kaydedilmesi gerekir. Örneğin hafta sonları, dini ve resmi tatillerin belirlenmesi gibi. |

**Detay**

Detay sekmesi; tanımlanan takvime, istenen tatil günlerinin eklendiği ya da çıkartıldığı sekmedir. Tatil günleri belirlenirken programdaki kolaylıklardan faydalanılabilir. Standart olan tatil günleri - resmi tatiller, dini tatiller ve hafta sonu tatilleri gibi - program tarafından otomatik olarak hesaplanır.

![](../../../../_assets/860487535e75f4bc707c.png)

Firma Takvimi ekranı Detay sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Firma Takvimi |  |
| --- | --- |
| **![](../../../../_assets/8c39327920ccab35e464.png)**Tatilleri Ekle | Tatil günlerini takvime eklemek için kullanılan butondur. Alanın sağ tarafında yer alan gri dikey çubuğa tıklandığında; Resmi Tatiller, Dini Bayramlar ve Hafta Sonları olmak üzere üç seçenek görüntülenir. Takvime eklenmesi istenen tatil seçeneğine, farenin sol tuşu ile tıklanır. Seçilen tatil günleri ekranının sağ tarafında listelenir. |
| **![](../../../../_assets/50ac4192fff8f1f9ec50.png)**Tatilleri Çıkar | Takvime eklenen tatil günlerinin silinmesi için kullanılan butondur. Alanın sağ tarafında yer alan gri dikey çubuğa tıklandığında; Resmi Tatiller, Dini Bayramlar, Özel Tatiller ve Hafta Sonları olmak üzere dört seçenek görüntülenir. Çıkarılması istenen tatil seçeneğine farenin sol tuşu ile tıklanır. Tek tek seçilerek çıkarılan tatiller ekranın sağ tarafında listelenen günlerden silinir. |
| **![](../../../../_assets/9a0386e1d775dcd6b712.png)**Tatilleri Seç | Tatilleri Ekle ![](../../../../_assets/8c39327920ccab35e464.png) butonu kullanılarak ekranın sağ tarafına tüm tatiller eklendiğinde, hepsi tarih sırasına göre listelenir. İzlerken farklı olanları ayırt etmek için Tatilleri Seç *![](../../../../_assets/9a0386e1d775dcd6b712.png)*butonu kullanılır. Bu buton, yapılan seçime göre tatil günlerinin renklerini farklı hale getirir. Resmi tatiller mavi, dini tatiller yeşil, hafta sonları kırmızı ve özel tatiller lacivert olarak izlenir. |
| Tarih | Tatil günleri içinde tanımlı olmayan yeni bir tatil gününü eklemek için kullanılan alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile görüntülenen takvimden, eklenecek tatil günü seçilir. |
| Tatil Türü | Girilen tarih için tatil türü tanımlanan alandır. Resmi, Dini, Özel ve Hafta Sonu olmak üzere dört türden oluşur. Griddeki herhangi bir günün üzerinde farenin sol tuşu ile çift tıklayarak tatil türünün değiştirilmesi sağlanır. |
| Açıklama | Seçilen tatil türü için açıklama bilgisi girilen alandır. |

Tanımlı bir tatil gününü iptal etmek için; tatil günlerinin izlendiği grid üzerinden iptal edilmesi istenen tatil günü üzerine farenin sol tuşu ile çift tıklayarak, klavyede yer alan F7 tuşu ile ya da araç çubuğundaki Kayıt Sil ![](../../../../_assets/2df4b343310bcd16b01e.jpg) butonu kullanılarak silinmesi gerekir.

Tanımlı bir tatil gününün türünü değiştirmek için; grid üzerinden değiştirilmesi istenen tatil günü üzerine farenin sol tuşu ile çift tıklayarak, seçilen günün türü değiştirilir.

**Örneğin;** özel tatil olarak tanımlı olan bir tatil Hafta Sonu tatili olarak değiştirilebilir.

Bir tatil gününün tek bir türü olabilir. Belli bir tarih, hem resmi hem de dini tatil olarak tanımlanamaz.

Firma Takvimi bölümünde takvim ile ilgili tanımlamalar yapıldıktan sonra Cari modülde hesap bazında tanımlamalar yapılabilir:

**Cari Modülde Firma Takvimi İle İlgili Yapılacak Tanımlamalar**

Cari Hesap Kayıtları bölümünde, her cari hesabın farklı bir takvimden çalışmasını sağlayan "Firma Takvimi" alanı ve çalıştığı günlerin ayarlanmasını sağlayan "Çalışma Günleri" alanı bulunur.

Cari Hesap Kayıtları bölümü Firma Takvimi ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Cari Hesap Kayıtları Ekranı |  |
| --- | --- |
| Firma Takvimi | Cari hesabın çalıştığı takvimin belirlendiği alandır. Cari hesabın çalıştığı özel bir takvim varsa, Yardımcı Programlar → Kayıt → "Firma Takvimi" bölümünden önceden tanımlanması gerekir. Özel bir takvim yoksa, genel takvime göre çalışacaksa boş bırakılabilir veya genel takvimin kodu girilebilir. Böylece, program genelinde ilgili cari hesap ile ilgili işlem yapıldığı zaman, "Firma Takvimi" alanında girilen koda göre tarih hesaplaması yapılır. |
| Çalışma Günleri | Firmanın çalışma günlerinin işaretlendiği alandır. Firma için girilen kayıtlarda, vade tarihi olarak çalışma günlerinin dışında bir gün bulunursa, program buradaki çalışma günlerine göre vade tarihini ayarlar. **Örneğin** Cari hesabın firma takvimini kullandığı, çalışma günlerinin de Pazartesi, Salı ve Cuma olduğu varsayıldığında, kesilen bir faturanın vade tarihi Çarşamba gününe denk geldiğinde, işlem türüne göre Vade tarihi Cuma veya Salı gününe alınır. Bu tanımlamaların yapılmasından sonra artık Fatura, Çek/Senet ve Dekont - Genel Dekont Kaydı, Serbest Meslek Makbuz Kaydı, Genel Gider Cari Hesap Fatura Kaydı - gibi modüllerin vade tarihlerinde takvim kontrolü yapılır. "Sorgula" seçeneği işaretlenerek hazırlanan bir genel takvimde, vade tarihi tatil gününe geldiyse bir uyarı ekranı görüntülenir. **Örneğin** Vade tarihi Cumhuriyet Bayramına denk geldiğinde, vade tarihinin Cumhuriyet Bayramına gelmesi ve seçilecek işlem türü sorgulanır. Yapılan seçime uygun çalışma günü bulunarak "Vade Tarihi" alanına gelir. Tanımlanan takvimde "Sorgula" alanı işaretlenmediği zaman bu uyarı ekrana gelmez ve uygun çalışma günü otomatik olarak "Vade Tarihi" alanına gelir. |
