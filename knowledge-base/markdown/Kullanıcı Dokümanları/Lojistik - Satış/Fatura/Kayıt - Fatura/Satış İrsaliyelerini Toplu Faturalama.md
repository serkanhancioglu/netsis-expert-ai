---
title: "Satış İrsaliyelerini Toplu Faturalama"
page_id: "22803815"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Fatura"
  - "Kayıt / Fatura"
  - "Satış İrsaliyelerini Toplu Faturalama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Fatura / Kayıt / Fatura / Satış İrsaliyelerini Toplu Faturalama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTVmZjk3YzdmLTRkYzAtNDQ2MC1hYjJjLTRmNTIyZWIzNTEwZCZsaW5rPTQwNDBmNjBmLWRkYmYtNDI3NS1hYjRlLTBhNmFhMmI2MGM5ZCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=5ff97c7f-4dc0-4460-ab2c-4f522eb3510d&link=4040f60f-ddbf-4275-ab4e-0a6aa2b60c9d&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "satis-irsaliyelerini-toplu-faturalama_22804862_22803815.html"
source_version: "2022-11-03T14:14:25.107+03:00"
source_bytes: 57392
fetched_at: "2026-09-13T04:01:44+00:00"
generator: "netsis-scraper 1.0.0"
---
# Satış İrsaliyelerini Toplu Faturalama

Satış İrsaliyelerini Toplu Faturalama, birden fazla irsaliyeyi, bir kerede toplu faturalandırmak için kullanılan bölümdür. Satış İrsaliyelerini Toplu Faturalama ekranı; İrsaliye Sınırlama ve İrsaliye Listesi sekmelerinden oluşur.

**İrsaliye Sınırlama**

İrsaliye Sınırlama, Satış İrsaliye Kayıtları bölümünden kaydedilen irsaliyelerin, "İrsaliye Sınırlama" bölümü ile aralık tanımlamaları belirlenerek faturalandırılmasını sağlar.

Satış İrsaliyelerini Toplu Faturalama ekranı İrsaliye Sınırlama sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Satış İrsaliyelerini Toplu Faturalama Ekranı | İrsaliye Tanım Aralığı |
| --- | --- |
| Cari Kodu Başlangıç | Faturalandırılması istenen irsaliyelerin, hangi müşteri koduna/kodlarına ait olduğunu belirleyen alandır. Birden fazla müşteriye ait irsaliyenin faturalandırılması isteniyorsa, irsaliyeleri bulunan müşterilerin arasından rehber ![](../../../../_assets/088477bb321d1b20c939.jpg) tuşu yardımı ile, en küçük cari koda sahip olan girilir. |
| Cari Kodu Bitiş | İrsaliyeleri bulunan müşterilerin arasından rehber ![](../../../../_assets/088477bb321d1b20c939.jpg) tuşu yardımı ile, en büyük cari koda sahip olan girilmelidir. Böylece program, burada verilen cari başlangıç ve bitiş kodlarına bakarak, sadece bu aralıklardaki müşterilerin irsaliyelerini faturalandırır. Sadece bir müşterinin irsaliyesi faturalandırılmak isteniyorsa, cari kod başlangıç ve bitiş alanına, müşterinin cari hesap kodu yazılır. Müşteri kodlarına ait bir aralık tanımlanması istenmiyor ise bu alanlar boş geçilir. |
| İrsaliye Tarihi Başlangıç | Faturalandırılacak olan irsaliyelerin, hangi tarih/tarihlere ait olduğunu belirleyen alandır. Belli bir tarih aralığında kaydedilen irsaliyeler faturalandırılacak ise, irsaliyelerin kayıt tarihleri arasından en küçük tarihe sahip olan yazılır. Program, bu alana otomatik olarak sistem tarihi getirir. Üzerinde istenen değişiklik yapılabilir. |
| İrsaliye Tarihi Bitiş | Faturalandırılacak olan irsaliyelerin, hangi tarih/tarihlere ait olduğunu belirleyen alandır. Belli bir tarih aralığında kaydedilen irsaliyeler faturalandırılacak ise, irsaliyelerin kayıt tarihleri arasından en büyük tarihe sahip olan yazılır. Böylece program burada verilen başlangıç ve bitiş tarihlerine bakarak, sadece bu tarihlerin aralığındaki irsaliyeleri faturalandırır. Sadece bir günün irsaliyeleri faturalandırılacak ise, başlangıç ve bitiş tarihlerine söz konusu tarih yazılır. |
| İrsaliye Numarası Başlangıç | Bu alan, faturalandırılması istenen irsaliyelerin hangi numara/numaralara ait olduğunun belirlendiği yerdir. Belli bir numara aralığında kaydedilen irsaliyeler faturalandırılacak ise buraya irsaliye numaralarından en küçük numaraya sahip olanın numarası yazılır. Rehber ![](../../../../_assets/088477bb321d1b20c939.jpg) tuşu yardımı ile, irsaliye numarası seçilir. |
| İrsaliye Numarası Bitiş | Faturalandırılması istenen irsaliyelerden numarası en büyük irsaliye ![](../../../../_assets/088477bb321d1b20c939.jpg) rehber tuşu yardımı ile seçilir. Böylece program burada verilen başlangıç ve bitiş numaralarına bakarak, sadece bu numara aralığındaki irsaliyeleri faturalandırır. İrsaliye numaralarında mutlaka aralık tanımlamanız gerekir. Program tarafından getirilen değerler onaylanırsa, kayıtlı olan tüm irsaliyeler faturalandırılır. Eğer irsaliyelerin faturalanması düzenli olarak yapılıyorsa, (örneğin; gün içinde girilen irsaliyelerin hepsi gün sonunda faturalandırılıyorsa) faturalanan irsaliye kayıtları iptal edilir ve sadece faturalanacak olan kayıtlar kalır. Böyle bir durumda, programın standart olarak getirdiği başlangıç ve bitiş numaraları aralığını onaylayarak, kalan irsaliyelerin tamamı faturalandırılabilir. |
| Fatura Tarihi | İrsaliyeler fatura haline geldiğinde, bu faturaların kayıt tarihinin hangi tarih olacağını belirleyen alandır. Program, bilgisayarın sistem tarihini bu alana otomatik olarak getirir fakat, kullanıcı bu tarihi değiştirerek istenen tarihe fatura kesebilir. Herhangi bir irsaliyenin fatura tarihi kanunen en fazla 7 gündür. Toplu faturalama modülünü kullanan firmalar, faturalandırılacak irsaliyeler için 1 haftalık periyodu içeren tarih aralığını vermelidir. Fatura Tarihi alanına, irsaliye tarih aralığında girilmiş olan bitiş tarihinin program tarafından otomatik olarak getirilmesi mümkündür. Bu uygulama için Yardımcı Programlar/ Özel Parametre Tanımları bölümünde Grup Kodu “FATURA”, Anahtar “IRSBITTARFATTAR”, Değer “0” tanımlamasının yapılması gerekir. |
| Entegre Tarihi | Faturaların entegrasyona aktarılmasında kullanılacak olan tarihtir. İrsaliye tarih aralığında verilen bitiş tarihinin program tarafından bu alana getirilmesi mümkündür. Bunun için yapılması gereken tanımlama "Fatura Tarihi" alanında açıklanmıştır. |
| Fatura Numarası | İrsaliyelerin faturalanması sırasında oluşacak faturaların hangi numaradan başlayacağının belirlendiği alandır. İşlem sonucunda oluşacak olan faturalar, verilen numaradan itibaren sıra takip edecek şekilde program tarafından numaralandırılır. Satış faturası kayıtlarındaki son fatura numarasının bir fazlası, program tarafından otomatik olarak ekrana getirilir. Numara istenildiği gibi düzenlenebilir. Sıra takip etme durumu, alış irsaliyelerinin faturalandırılmasında da aynı şekilde uygulanır. |
| Plasiyer Kodu | Faturalandırılması istenen irsaliyelere plasiyer kodu bazında kısıt vermek amacıyla kullanılan alandır. Bu alana ![](../../../../_assets/088477bb321d1b20c939.jpg) rehber tuşu yardımı ile kod seçilerek girildiğinde, sadece o plasiyer koduna sahip irsaliyeler faturalandırılır. |
| İrs. Tip Aralığı | Sadece belirli tipteki irsaliyelerin toplu olarak faturalandırılması için kullanılan alandır. Burada tip aralığı verilerek, sadece o aralığın içindeki tiplerde olan irsaliyeler faturalandırılır. |
| Koşul Kodu | Sadece belirli bir koşul koduna sahip irsaliyelerin faturalandırılması için kullanılan alandır. Koşul kodları için ![](../../../../_assets/088477bb321d1b20c939.jpg) rehber tuşu kullanılarak aralık verilebilir. |
| Faturalandırma Kırılımı | İrsaliyelerin faturalandırılması aşamasında, irsaliyelerin hangi sıra ile faturalandırılacağının belirlendiği alandır. Bu bölümde İrsaliye Numarası, Cari Kodu, Teslim Cari Kodu veya Koşul Kodu seçeneklerinden birisi işaretlenebilir. |
| Şubelere Ait İrsaliyelerin Faturalandırılması | Şube seçimi yapılarak, sadece seçilen şubeye ait irsaliyelerin faturalandırılması için kullanılan alandır. |
| E-Fatura Carileri Getirilsin | E-Fatura seçimi yapılarak, sadece seçilen E-Faturalara ait carilerin getirilmesi için kullanılan alandır. |
| Belge İstisna Kodu | e-Arşiv belgeleri için belge istisna kodu girilen alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, istisna kodları arasından seçim yapılır. |
| KDV'siz Belge İstisna Kodu | "E-Fatura Cari Getirilsin" seçeneği işaretlendiğinde aktif hale gelen alandır. e-Fatura oluşturulurken belirtilen istisna kodu ile e-Fatura oluşturulmasını sağlar. Fatura oluşturma adımında kullanıcıya sorulmaz. |
| Özel Kod 1 | Faturalanması istenen irsaliyeler için, Özel Kod1 alanına girilen değerlere kısıt verebilmek amacıyla kullanılan alandır. Sadece belli "Özel Kod1" değerine sahip irsaliyelerin toplu faturalandırılması isteniyorsa, işleme dahil edilmesi istenen irsaliyelerde girilen "Özel Kod 1" değerinin belirtilmesi yeterlidir. |
| Özel Kod 2 | Faturalanması istenen irsaliyeler için, Özel Kod-2 alanına girilen değerlere kısıt verebilmek amacıyla kullanılan alandır. Sadece belli Özel Kod-2 değerine sahip irsaliyelerin toplu faturalandırılması isteniyorsa, işleme dahil edilmesi istenen irsaliyelerde girilen Özel Kod-2 değerinin belirtilmesi yeterlidir. |
| Açıklama | Faturalanması istenen irsaliyeler için, "Üst Bilgiler" sayfasında bulunan "Açıklama" alanına girilen değerlere göre kısıt verilebilir. Sadece belli açıklama değerine sahip irsaliyelerin toplu faturalandırılması isteniyorsa, işleme dahil edilmesi istenen irsaliyelerde girilen Açıklama değerinin belirtilmesi yeterlidir. |
| Mallar Birleştirilsin | Bu seçenekle bir veya birden fazla irsaliyede bulunan aynı kodlu malların, faturada tek kalem haline getirilmesi sağlanır. "İrsaliyeler Birleştirilsin" kutucuğu işaretlenmemiş ise, her bir irsaliye ayrı bir fatura haline getirileceği için, kendi içinde aynı kodlu maldan birden fazla satır varsa tek satır haline gelir. "İrsaliyeler Birleştirilsin" kutucuğu işaretlenmiş ise, tek bir fatura haline gelecek birden fazla irsaliyede tekrarlayan mallar, faturada tek satır haline gelir. Malların tek satır halinde birleştirilebilmesi için birim fiyatlarının da aynı olması gerekir. Aynı kodlu maldan ayrı satırlarda ve ayrı fiyatlarda kayıt yapılmışsa bunlar tek satır haline getirilmeyip, ayrı satırlarda kaydedilir. Birleştirilen mallar farklı siparişlerden geliyorsa, bu parametrenin işaretlenmemesi gerekir. Satır bazında tek bir sipariş numarası tutulabildiği için sipariş bağlantıları silinir ve tek bir sipariş numarası görüntülenir. |
| İrsaliyeler Birleştirilsin | Müşteriye ait birden fazla irsaliyenin, tek fatura haline getirilmesi istenilen durumda kullanılan seçenektir. Bu kutucuğun işaretlenmemesi durumunda, her irsaliye ayrı bir fatura haline getirilecektir. İşaretli olması durumunda ise, irsaliyelerin kesildiği cari hesapların aynı olmasına rağmen, irsaliyelerin bazen birleşmediği görülebilir. Bunun sebebi, irsaliyelerin bazılarının KDV dahil, bazılarının ise KDV hariç kesilmiş olması, Özel Kod-1 veya Özel Kod-2 değerlerinin plasiyer ya da proje kodları gibi bilgilerinin farklı olmasıdır. |
| Deneme Basımı | İrsaliyelerin faturalandırılması aşamasında kontrol amaçlı kullanılan seçenektir. Bu bölüm işaretlendiğinde, işlem sonunda oluşturulacak bütün faturaların yazıcıdan basımı yapılır (düz beyaz kağıda), fakat işlemler kayıtlara geçmez. Yapılan basım üzerinde gerekli kontroller ve (gerekiyorsa irsaliyelere dönerek) düzeltmeler yapıldığında, faturalandırma işlemi güncellenerek kayıtlara geçer. Seçenek işaretlenmediğinde ise, oluşan faturalar kayıtlara geçer ve matbu forma fatura basımları yapılır. |
| Faturalar Tek Tek Onaylansın | İrsaliyelerin faturalandırılması aşamasında, oluşacak faturaların ekranda görüntülenmesini ve kullanıcı tarafından onaylatılmasını sağlamak için kullanılan seçenektir. Bu kutucuk işaretlenmez ise, verilen kısıtlara uyan irsaliyelerin tamamı program tarafından faturalandırılır. Kullanıcının herhangi bir işlem yapmasına gerek kalmaz. Faturaların oluşturulması sırasında, isteniyorsa arka arkaya yazıcıdan fatura basımı da yapılabilecektir. Oluşan faturaların bilgilerinin ekranda tek tek onaylatılması isteniyorsa, bu sorgulama işaretlenmelidir. |
| Kapalı İrsaliye İçin Kasa Kodu | Kapalı tipte oluşturulan irsaliyeler için kullanılan kasa kodudur. Eğer faturalandırılan irsaliyelerde kapalı tipte kaydedilen irsaliye var ise, bu irsaliyeler kapalı fatura olarak düzenlenir ve tahsilat tutarları bu alandaki kasa koduna aktarılır. |
| Basım | İrsaliyelerin faturalandırılması aşamasında, oluşturulan faturalar "Toplamlar" ekranına program tarafından yansıtılır. Bu faturaların basımının yapılması için "Toplamlar" ekranında bulunan "Basım" seçeneğinin işaretlenerek "Tamam" butonuna basılması gerekir. |
| Dizayn Kodu Tüm Faturalar İçin Sorulmasın | İşlem sırasında oluşturulan faturaların basımı için, her fatura sonrasında dizayn kodunun sorulmaması için kullanılan seçenektir. İlk oluşturulan faturanın basım dizaynının, diğer faturalarda da geçerli olmasını sağlar. |
| İşlem Sonunda Faturalar Açılsın | İşlem tamamlandıktan sonra oluşturulan tüm faturaların, program tarafından açılması için kullanılan seçenektir. |
| Döviz Kurları Güncellensin | Dövizli belgelerde, irsaliyelerin kaydı sırasında girilen kur bilgisinin fatura tarihindeki kurdan farklı olması halinde, fatura kalemlerinde girilen kurun güncellenerek, fatura TL tutarının tekrar hesaplanmasını sağlayan seçenektir. |
| Döviz Kuru | “Döviz Fiyatları Güncellensin Mi” seçeneği işaretlendiğinde aktif olan, döviz fiyatlarının güncellenmesi durumunda dikkate alınacak kurun belirlendiği alandır. "D.Alış, D.Satış, E.Alış, E.Satış seçeneklerini içerir. |
| Teslim Carisi Farklı İrsaliyeler Birleştirilsin | Aynı cari kod için kesilen irsaliyeler birleştirilirken, teslim cari kodu farklı olan irsaliyelerin de birleştirilmesi için kullanılan seçenektir. |
| Koşul Kodu Farklı İrsaliyeler Birleştirilsin | Aynı cari kod için kesilen irsaliyeler birleştirilirken, koşul kodu farklı olan irsaliyelerin de birleştirilmesi için kullanılan seçenektir. |
| Tevkifat Hesaplansın | Tevkifat hesaplaması yapılması için kullanılan seçenektir |
| Proje Kodu Farklı İrsaliyeler Birleştirilsin | Aynı cari kod için kesilen irsaliyeler birleştirilirken, proje kodu farklı olan irsaliyelerin de birleştirilmesi için kullanılan seçenektir. |
| Tevkifat Hesaplama Şekli | Tevkifat hesaplama şeklinin seçildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile seçim yapılır. "Hesaplanmasın" seçeneği, irsaliyelerde tevkifat olsa bile faturada tevkifat hesaplanmaması için kullanılır. "Tümü İçin Hesaplansın" seçeneği, irsaliyede tevkifat olmasa bile faturasında tevkifat hesaplanması için kullanılır. "İrsaliyedeki Değerler ile Hesaplansın" seçeneği, irsaliyede tevkifat olup olmaması durumuna göre irsaliyedeki tevkifat bilgisinin faturaya taşınması için kullanılır. |
| ![](../../../../_assets/e3223333470668512f5f.jpg) Oku Butonu | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) Sakla Butonu | İrsaliye Tanım Aralığı, Ek Saha Tanım Aralığı ve İleri Tanım Aralığı sayfalarında verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. Faturalandırması istenen irsaliyeler için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki toplu faturalama işleminde kullanılmak üzere saklanır. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam Butonu | Faturalandırması istenen irsaliyeler için verilen kısıtların kaydedildiği butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal Butonu | Faturalandırması istenen irsaliyeler için verilen kısıtların iptal edildiği butondur. |

Fatura Tarihi ve Plasiyer Kodu alanları "**Yardımcı Programlar**" sayesinde, Özel Kod 1, Özel Kod 2, Açıklama, Teslim Carisi Farklı İrsaliyeler Birleştirilsin, Koşul Kodu Farklı İrsaliyeler Birleştirilsin, Proje Kodu Farklı İrsaliyeler Birleştirilsin alanları ise "Satış Parametreleri" sayesinde isteğe bağlı olarak ekranda yer alabilir/almayabilir.

Satış İrsaliyelerini Toplu Faturalama ekranı Ek Saha Tanım Aralığı bölümünde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Satış İrsaliyelerini Toplu Faturalama Ekranı | Ek Saha Tanım Aralığı |
| --- | --- |
| Ek Açıklamalar | İrsaliye kayıtları sırasında ek açıklama bilgisi giren firmaların, girilen açıklamaya göre kısıt vererek irsaliyelerini faturalandırmaları için kullanılan alanlardır. Örneğin; İrsaliyelerin açıklama sahasına İzmir, İstanbul gibi bilgiler giren bir firmada, açıklama sahasında “Alsancak” yazan irsaliyelerin faturalandırılması için, ek saha tanım aralığı kullanılabilir. |
| Kamyon Plaka No | Dağıtım/Vasıta Bilgileri bölümünden tanımlanan kamyona ait plakanın rehber ![](../../../../_assets/088477bb321d1b20c939.jpg) tuşu yadımı ile seçim yapılarak girildiği alandır. |

Ek Saha Tanım Aralığı; toplu faturalama işlemlerinde "İrsaliye Tanım Aralığı" sekmesinde bulunan kısıtların yetersiz kalması halinde, faturalandırılacak irsaliyeler için daha detaylı kısıt verilebilmesi amacıyla kullanılan bölümdür.

İleri Tanım Aralığı sekmesinde, ilgili alan üzerinde iken klavyedeki boşluk çubuğuna basılarak bilgi girişi yapılır. Örneğin; Özel Kod-1 için kısıt verilmesi isteniyorsa, Saha Adı alanında **boşluk tuşuna** basılması ve **aşağı ok** tuşuna basılarak Özel Kod-1 alanının seçilmesi gerekir. Daha sonra **Enter tuşuna** basıldığında girilen bilgi saklanır ve sağdaki alana geçilir.

Birden fazla alana kısıt verilmesi isteniyorsa, klavyede bulunan **Insert** **tuşuna** basılarak satır eklenebilir veya **Delete tuşuna** basılarak eklenen satırlar silinebilir. Sağ klik tuşu ile açılan özel tuşlar sayesinde de aynı işlemler yapılabilir.

**İrsaliye Listesi**

İrsaliye Listesi, İrsaliye Sınırlama bölümünde bulunan sayfalarda verilen kısıtlara uyan irsaliyelerin listelendiği ve bu listeden faturalandırılacak irsaliyelerin kullanıcı tarafından seçildiği sekmedir.

Faturalandırılması istenen irsaliyelerin seçimi için, ilgili irsaliyelerin üzeri çift tıklanır. Seçilen irsaliyenin bulunduğu satır gri renge dönecektir. Listede bulunan irsaliyelerin tamamını seçmek için her birinin üzerini iki kez tıklamak yerine, sayfa üzerinde iken sağ klik tuşu ile ekrana gelen “Tümünü Seç” seçeneğinin işaretlenmesi yeterlidir. İrsaliye seçimi yapıldıktan sonra, faturalandırma için “Tamam”, işlemden çıkmak için “İptal” butonuna basılır. "Tamam" butonuna basılması ile birlikte fatura numarası, cari hesap kodu, ismi, irsaliye numarası (birden fazla irsaliye aynı faturada birleştiriliyorsa numaraları), irsaliye tarihleri ve tutarları, ekranın alt kısmındaki "Toplam Tutar" alanında görülür ve işlem için program onay ister. “Faturalandırmak için emin misiniz?” sorusu için “Evet” butonuna basıldığında faturalandırma işlemi yapılmış olur. “Hayır” butonuna basıldığında bir sonraki irsaliyeye geçilir, “İptal” butonuna basıldığında ise işlem yapılmadan toplu faturalamadan çıkılır. Onaylanması halinde, toplu faturalandırılacak irsaliyelerin tutarı, "Satış faturaları/Toplamlar" sekmesine yansır.

"Toplamlar" sekmesinde gerekli düzenlemeler yapıldıktan sonra Tamam ![](../../../../_assets/39d77b8716226638d9ce.jpg) butonuna basıldığında faturalandırma işlemi tamamlanmış olur.

İrsaliyelerin faturalandırılması durumunda, irsaliye kayıtları sırasında işlenmiş olan stok hareketleri fatura bilgilerine göre tekrar düzenlenir. Fatura bilgileri doğrultusunda cari hesap hareketleri ve muhasebeyle ilgili kayıtlar yapılır. İrsaliyelerin faturalandırılmasından sonra ilgili irsaliyeler kayıtlardan silineceğinden, bu kayıtlar artık irsaliye numarası ile izlenemez. Satış Faturaları modülü kullanılarak, sistemin vermiş olduğu fatura numaralarıyla kayıtlar izlenebilir.
