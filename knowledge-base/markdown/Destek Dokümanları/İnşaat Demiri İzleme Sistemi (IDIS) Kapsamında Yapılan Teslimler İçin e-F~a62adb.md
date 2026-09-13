---
title: "İnşaat Demiri İzleme Sistemi (IDIS) Kapsamında Yapılan Teslimler İçin e-Fatura ve e-İrsaliye Düzenlemeleri"
page_id: ""
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "İnşaat Demiri İzleme Sistemi (IDIS) Kapsamında Yapılan Teslimler İçin e-Fatura ve e-İrsaliye Düzenlemeleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / İnşaat Demiri İzleme Sistemi (IDIS) Kapsamında Yapılan Teslimler İçin e-Fatura ve e-İrsaliye Düzenlemeleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWM1NzI1NzIxLTc2OGYtNDExMi05YWViLTcxMjUyYjE0Y2EzOSZsaW5rPWYyZjZmZjU5LTU5MjQtNDAxNi1iNzU4LTBiMWRmMTgxZDU1YSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=c5725721-768f-4112-9aeb-71252b14ca39&link=f2f6ff59-5924-4016-b758-0b1df181d55a&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "insaat-demiri-izleme-sistemi-idis-kapsaminda-yapilan-teslimler-icin-e-fatura-ve-e-irsaliye-duzenlemeleri.html"
source_version: ""
source_bytes: 38926
fetched_at: "2026-09-13T04:21:55+00:00"
generator: "netsis-scraper 1.0.0"
---
# İnşaat Demiri İzleme Sistemi (IDIS) Kapsamında Yapılan Teslimler İçin e-Fatura ve e-İrsaliye Düzenlemeleri

**İnşaat Demiri İzleme Sistemi (İDİS)**, Darphane ve Damga Matbaası Genel Müdürlüğü tarafından kurulup işletilen ve Türkiye’de inşaat demirinin tüm üretimden teslim aşamasına kadar elektronik ortamda takip edilmesini sağlayan bir izleme sistemidir. Vergi güvenliğini sağlamak, kayıt dışı ekonomiyi azaltmak, yapı güvenliğini artırmak, yapı malzemelerinin güvenilirliğini ölçmek, inşaat demirinin üretimden sahada kullanım ve laboratuvar testlerine kadar tüm süreçlerinin izlenmesini mümkün kılmak İDİS’ in Temel amaçları arasında yer alır.

Gelir İdaresi Başkanlığı tarafından e-Fatura ve e-İrsaliye uygulamalarına dâhil olan mükellefler tarafından, Darphane ve Damga Matbaası Genel Müdürlüğü’ne İnşaat Demiri İzleme Sistemi (IDIS) üzerinden bildirimi yapılan ürünler için düzenlenecek e-Fatura ve e-İrsaliyelerde kullanılması gereken alanların belirlendiği teknik kılavuz, [https://ebelge.gib.gov.tr/](https://ebelge.gib.gov.tr/) adresinde yayımlanmıştır. Güncel GİB kılavuzuna [buradan](https://ebelge.gib.gov.tr/dosyalar/kilavuzlar/IDIS_Kapsaminda_Yapilan_Teslimlere_Iliskin_Fatura_ve_Irsaliye_Teknik_Kilavuzu_V.1.0.pdf) ulaşabilirsiniz.

**9062.16 (LTS sürümü), 9066.6 (LTS sürümü) ve 9069.1** sürümleriyle birlikte, İnşaat Demiri İzleme Sistemi (IDIS) üzerinden bildirimi yapılan ürünler için düzenlenecek e-Fatura ve e-İrsaliyeye ilişkin düzenlemeler desteklenmiştir.

**Fatura/ İrsaliye Senaryosu/Tipleri**

e-Fatura uygulamasına dahil olan mükellefler tarafından İDİS kapsamında yapılan teslimler için düzenlenecek e-Faturalarda “**IDIS**” fatura senaryosu benzer şekilde e-İrsaliye uygulamasına dahil olan mükellefler tarafından İDİS kapsamında yapılan teslimler için düzenlenecek e-İrsaliyelerde “**IDISIRSALIYE**” senaryosu kullanılacaktır. Mükellefin dahil olduğu uygulamaya (e-Fatura ve e-İrsaliye) göre kullanılacak senaryo ve fatura/irsaliye tipleri aşağıdaki gibidir.

| e-Fatura | e-İrsaliye |
| --- | --- |
| **Senaryo:** IDIS <u>Örnek UBL Alanı:</u> \<cbc:ProfileID\>IDIS\</cbc:ProfileID\> | **Senaryo:** IDISIRSALIYE <u>Örnek UBL Alanı:</u> \<cbc:ProfileID\>IDISIRSALIYE\</cbc:ProfileID\> |
| **Fatura Tipleri:** SATIS, ISTISNA, TEVKIFAT, TEVKIFATIADE, IADE, IHRACKAYITLI <u>Örnek UBL Alanı:</u> \<cbc:InvoiceTypeCode\>SATIS\</cbc: InvoiceTypeCode\> \<cbc:InvoiceTypeCode\>IADE\</cbc: InvoiceTypeCode\> \<cbc:InvoiceTypeCode\>ISTISNA\</cbc: InvoiceTypeCode\> \<cbc:InvoiceTypeCode\>TEVKIFAT\</cbc: InvoiceTypeCode\> \<cbc:InvoiceTypeCode\>TEVKIFATIADE\</cbc: InvoiceTypeCode\> \<cbc:InvoiceTypeCode\>IHRACKAYITLI\</cbc: InvoiceTypeCode\> | **İrsaliye Tipleri:** SEVK, MATBUDAN <u>Örnek UBL Alanı:</u> \<cbc:DespatchAdviceTypeCode\>SEVK\</cbc: DespatchAdviceTypeCode \> \<cbc:DespatchAdviceTypeCode \>MATBUDAN\</cbc: DespatchAdviceTypeCode \> |

Bu kapsamda Satış Parametreleri ekranına, Genel 4 sekmesine “**İDİS Uygulaması**” seçeneği eklenmiştir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/df7ddf1a-2456-4bbb-8eb9-dbe8679f8f85/inşaat 1.png)

Bu uygulama aktif edildiğinde, İnşaat Demiri İzleme Sistemi (İDİS) kapsamında yapılan teslimlere ilişkin belgeleri belirlemek için, satış tarafında Satış Faturası ve Satış İrsaliyesi belgelerinin Üst Bilgiler sekmesine “**İDİS**” seçeneği eklenmiştir.

Satış Faturası belgesinde, e-Fatura serisinden girilen ve e-fatura mükellefi olan bir cariye kesilen faturaların üst bilgilerinde “**İDİS**” seçeneği aktif olmaktadır. Benzer şekilde satış irsaliyesi belgesinde “**İDİS Uygulaması**” seçeneğinin aktif olması durumunda, Satış İrsaliyesinin Üst Bilgiler sekmesinde, "**İDİS**" seçeneği aktif olmaktadır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/f69e5a01-b27e-4792-a672-a6bbea5d8656/inşaat 2.png)

Satış Faturası Kalemler sekmesinde stok kodu satırı üzerinde sağ tıkta gelen menüde “**İDİS Detay Girişi”** tıklanır ve “**İDİS Detay Girişi”** ekranı açılır. Açılan ekranda **Sevkiyat No** ve **Etiket No** bilgileri girilerek kaydedilir. Sevkiyat ve Etiket No bilgileri satırda girilen miktardan bağımsız olarak istenildiği kadar girilebilir.

## ![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/fda0fdd3-db7d-4602-8f77-8f27afabcf93/inşaat 3.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/28470f72-2f59-4671-9f7c-30a5abf4190e/inşaat 4.png)

Sevkiyat No alanına yazılacak değerin ilk 2 karakteri “**SE**”, sonra “-“ ifadesi ve sonrasında 7 karakter rakam olmak üzere toplam 10 karakter olması gerekmektedir. Bu kurala aykırı bir değer yazılıdığında veya bu alan boş geçildiğinde ekrana "**Sevkiyat No bilgisi formata uygun girilmemiştir. SE-XXXXXXX şeklinde olmalıdır.**" şeklinde bir uyarı çıkacak ve detay satır kaydedilmeyecektir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/b2817ad8-05c4-41f5-bcb7-7622d5684526/inşaat 5.png)

Etiket No alanına yazılacak değerin ilk 2 karakteri text veri ve sonrasında 7 karakter rakam olmak üzere toplam 9 karakter olması gerekmektedir. Bu kurala aykırı bir değer yazıldığında veya bu alan boş geçildiğinde ekrana "**Etiket No bilgisi formata uygun girilmemiştir. XX1111111 şeklinde olmalıdır."** şeklinde bir uyarı çıkacak ve detay satır kaydedilmeyecektir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/d820336c-d2f0-4194-8fc2-561364cd5e70/inşaat 6.png)

Ayrıca İDİS Detay Girişi ekranında “**Excel Aktarımı**” seçeneği ile Sevkiyat No ve Etiket No bilgilerinin excelden aktarımı sağlanabilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/99589135-892c-4607-a50b-90f4d28b623f/inşaat 7.png)

Kalemler sekmesinde İnşaat Demiri İzleme Sistemi (İDİS) kapsamındaki teslimler için düzenlenen belgelerde ürünlere ait zorunlu bilgilerin girilmesi sonrasında belge kaydedilir. Bu zorunlu bilgiler, e-İrsaliye olarak gönderilecek Satış İrsaliyesi belgelerinde de girilmelidir.

Taslak sonrası oluşan E-fatura ve e-İrsaliye görüntüleri ve xml detayları aşağıdaki gibidir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/a38e7bc8-e69e-4daa-ab9d-8310c2461b33/inşaat 8.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/aa478e97-44b1-4c0b-b34b-c432cb0e8b6d/inşaat 9.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/36a4bfb0-644e-4951-9a30-8213f009b76a/inşaat 10.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/62f69fcc-378e-465e-8123-eb403ae1b8e8/inşaat 11.png)

Zarf/Fatura Bazında Giden/Gelen e-Fatura ekranlarında İDİS kapsamındaki e-Fatura belgelerinin senaryo bilgileri İDİS olarak görünmektedir. Benzer şekilde Zarf/Fatura Bazında Giden/Gelen e-İrsaliye ekranlarında İDİS kapsamındaki e-İrsaliye belgelerinin senaryo bilgileri IDISIRSALIYE olarak görünmektedir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/8ef3f1e9-94c2-4f7c-bd41-ed887823b334/idis11 (2).png)![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/686e1dbf-7a45-4ee4-ad45-2d532216ad41/inşaat 12.png)

- “**İDİS**” seçeneği işaretlenerek kaydedilen bir satış irsaliyesi, satış faturasına dönüştürülürken;

\*İrsaliyenin **Toplamlar** sekmesinden her bir irsaliye bir faturaya dönüştürülüyorsa irsaliyede girilen İDİS detayları oluşan faturaya aktarılmaktadır.

\*İrsaliyenin parçalı faturalanması durumunda eğer satır içindeki miktar parçalanmıyorsa, irsaliyedeki ilgili satır için girilmiş İDİS detayları faturaya aktarılmaktadır.

\*İrsaliyenin parçalı faturalanması durumunda eğer satır içindeki miktar parçalanıyorsa oluşan faturaya herhangi bir İDİS bilgisi aktarılmayacaktır.

**\*Satış İrsaliyeleri Toplu Faturalama** ekranından irsaliyeler faturalaştırılırken, “**İDİS**” seçeneği işaretli irsaliyeler ile “**İDİS**” seçeneği işaretli olmayan irsaliyelerin birleştirilmemesi, İDİS tipine göre kırılım yapılması sağlanacaktır. Buradan oluşturulan faturalara İDİS detay bilgileri aktarılacaktır.

\*Satış Faturası, Sipariş Bilgileri sekmesindeki **Belge Getir** butonu ile satır seçimi yapılarak faturalaştırılıyorsa, bu durumda “**İDİS**” seçeneği işaretli irsaliye satırı ile “**İDİS**” seçeneği işaretli olmayan bir irsaliye satırının birlikte seçilmesi engellenmiştir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/9ac0893b-7637-4c3c-8de8-a3bd91d6a9b2/inşaat 13.png)

IDIS kapsamında yapılacak teslimlerde düzenlenecek e-Faturalar için, Fatura Tipi: **IHRACKAYITLI** olması durumunda,

- İhraç kayıtlı faturalar dış ticaret modülünden takip edilmiyorsa yani fatura modülünden ihraç kayıtlı satış irsaliyesi girilip, dekont modülünden ihract kapatma ile faturalaştırılıyorsa, satış irsaliyesi “**İDİS**” seçeneği işaretlenerek ve İDİS detayları girilerek oluşturulmalıdır. İhracat kapatma yapıldığında satış irsaliyesinde girilen İDİS detayları ihraç kayıtlı faturaya aktarılmaktadır.

Satış Parametrelerinde "**İDİS Uygulaması**" seçeneği işaretli olması durumunda, Dış Ticaret Modülünde proforma oluşturma ekranına "**İDİS**" seçeneği eklenmiştir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/d84a1a5a-1334-4efc-ab11-cff598627244/inşaat 14.png)

- İhraç kayıtlı faturalar dış ticaret modülünden takip ediliyorsa ve ihracat süreci **siparişten** başlıyorsa, dosyaya bağlanacak tüm sipariş kayıtları ihraç kayıtlı ise, “**İDİS**” seçeneği aktif olmaktadır.

Proforma faturaya bağlanacak olan ihraç kayıtlı sipariş satırları seçimi sonrasında fatura numarası girilir ve “**İDİS**” seçeneği işaretlenerek proforma fatura oluşturulur.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/d946f95b-38b1-4f44-af19-d8b142b3182d/inşaat 15.png)

Proforma fatura üzerinden Detay Gösterme ekranı Üst Bilgiler/Kalem Bilgileri sekmesinde, seçili kalem üzerinde sağ tık menüsünde İDİS detay bilgilerinin girilmesi için “**İDİS Detay Girişi”** eklenmiştir. Satış İrsaliyesi/Faturasında sağ tık'a eklenen menü ile aynı şekilde çalışmaktadır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/a0e94788-5678-4cc2-aa57-1ab31594e6f2/inşaat 16.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/6c43808e-1acd-4961-b90c-161aeb31d0c5/inşaat 17.png)

Ayrıca çeki listesinden irsaliye oluşturma sürecinde çıkan **İrsaliye Oluştur** isimli ekrana da "**İDİS**" seçeneği eklenmiştir. Eğer proformadaki “**İDİS**” seçeneği işaretli ise, irsaliye oluştururken bu seçenek varsayılan olarak işaretli gelmekte olup kullanıcı isterse kaldırabilmektedir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/cbaf244a-c4a2-49cd-b383-0380998a96a5/inşaat 18.png)

Çeki listesinden irsaliye oluşturduğunda Sevkiyatlar sekmesindeki Sabit Bilgiler bölümünde yer alan grid üzerinde de satır seçili iken sağ tık menüsüne "**İDİS Detay Girişi**" eklenmiştir. Proforma fatura satırlarında girilen İDİS detay bilgileri bu ekrana taşınır. İstenirse üzerinden değişiklik yapılabilir veya oluşan irsaliye için farklı İDİS detay bilgileri girilebilir. Bu ekrandan girilen bilgiler irsaliye satırı ile bağlanır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/ce1f69b4-d7d6-461d-995e-01032047fd39/inşaat 19.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/28dcce55-1b01-4341-905f-7616bcbb4dd5/inşaat 20.png)

Zorunlu bilgilerin girilmesi sonrasında ihracat kapatma işlemi ile nihai ihraç kayıtlı fatura oluşturulur ve bu belge ihraç kayıtlı e-Fatura olarak gönderilir.

- İhraç kayıtlı faturalar dış ticaret modülünden takip ediliyorsa ve ihracat süreci **irsaliyeden** başlıyorsa, irsaliye üzerinde “**İDİS**” seçeneğini işaretleyip İDİS detayları irsaliye üzerinde girilebilir. Bu durumda irsaliyede girilen İDİS detay bilgileri oluşan proforma faturaya taşınmaktadır. Kullanıcı istediğinde bu detay bilgileri düzenleyebilir.

İrsaliyeler proformaya bağlanırken eğer seçili irsaliye satırlarında “**İDİS**” seçeneği işaretli ise, proforma oluştururken form üzerinde yer alan “**İDİS**” seçeneği de işaretli ve pasif olarak gelir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/47d2ed2d-438e-4a8c-be50-d6d562b0a7a3/inşaat 21.png)

Eğer seçili irsaliye satırlarının tümünde “**İDİS**” seçeneği işaretli değilse proforma ekranında da “**İDİS**” seçeneği işaretsiz olarak gelir kullanıcı isterse işaretler.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/c287ef5d-6e09-4379-a464-f3c4679b75d5/inşaat 22.png)

Proformadan çeki listesi ve çeki listesinden de irsaliye oluşturulursa ve proformadaki satır miktarları ile bağlı olduğu irsaliye satır miktarları eşit ise, bu durumda irsaliye belgesine, bağlı olduğu proforma satırındaki İDİS detay bilgileri aynen taşınacaktır.

Burada çeki listesinde miktar parçalanmış ise yani irsaliyenin satırında bulunan miktarlar ile proformanın bağlı olduğu satırın miktarı eşit değilse bu durumda irsaliye belgesine proformadaki İDİS detayları taşınmayacaktır. Sevkiyat bilgilerinde Sabit Bilgiler kısmında sağ tık menüsünden İrsaliye için İDİS detayları ayrıca girilmelidir.

Zorunlu bilgilerin girilmesi sonrasında ihracat kapatma işlemi ile nihai ihraç kayıtlı fatura oluşturulur ve bu belge ihraç kayıtlı e-Fatura olarak gönderilir.

- İDİS kapsamındaki e-Faturalar için uygulama yanıtı verilememektedir. Temel fatura yapısı şeklinde ilerlenmektedir. Ancak İDİS kapsamındaki e-İrsaliyeler için eskisi gibi irsaliye yanıtı verilmektedir.
- İDİS kapsamındaki e-Fatura ve e-İrsaliye belgelerine İDİS ile ilgili olmayan stok kalemleri girilmemelidir.
- İDİS kapsamındaki e-Faturalarda **IADE** fatura tipi kullanılıyorsa, iadesi yapılan faturaya ait İade Fatura Numarası ve İade Fatura Tarihi bilgilerinin girişi zorunludur. (cac:BillingReference/cac:InvoiceDocumentReference)

İDİS Kapsamında yapılan teslimler için düzenlenen e-Faturalar için [Örnek dizayn](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/51dc5909-6c86-4be2-857c-e5b9ce5216b5/IDIS.rar)
