---
title: "Binek Araç Giderlerinin Kısıtlanması"
page_id: ""
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Binek Araç Giderlerinin Kısıtlanması"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Binek Araç Giderlerinin Kısıtlanması"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTQ3NDAzMTAwLTk2NjYtNGMyNS1iODA4LTc3YzU3ZWY4NmZkZCZsaW5rPWFlYzRhOTU0LWM2ZDYtNDU2My05M2IwLTVhMzgwODg3OWZiNiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=47403100-9666-4c25-b808-77c57ef86fdd&link=aec4a954-c6d6-4563-93b0-5a3808879fb6&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "binek-arac-giderlerinin-kisitlanmasi.html"
source_version: ""
source_bytes: 13586
fetched_at: "2026-09-13T04:21:49+00:00"
generator: "netsis-scraper 1.0.0"
---
# Binek Araç Giderlerinin Kısıtlanması

7194 sayılı Kanun’un 13. maddesine istinaden, 193 sayılı Gelir Vergisi Kanunu’na bazı hükümler eklenmiştir. Bu hükümlere kısaca değinecek olursak:

"Faaliyetleri, kısmen veya tamamen binek otomobillerinin kiralanması veya çeşitli şekillerde işletilmesi olanların bu amaçla kullandıkları araçlar hariç olmak üzere; kiralama yoluyla edinilen binek otomobillerinin her birine ilişkin aylık kira bedelinin **45.000** Türk lirasına kadarlık kısmı ile binek otomobillerinin iktisabına ilişkin özel tüketim vergisi ve katma değer vergisi toplamının en fazla **1.200.000** Türk lirasına kadarlık kısmı gider olarak dikkate alınabilir.

Yine aynı şekilde, faaliyetleri kısmen veya tamamen binek otomobillerinin kiralanması veya çeşitli şekillerde işletilmesi olanların bu amaçla kullandıkları hariç olmak üzere, binek otomobillere ilişkin giderlerin en fazla **%70**’i indirilebilir.

##### 1)Binek Oto Gider Kısıtlaması Üst Sınırlarının Belirlenmesi

Üst sınır bedelleri Fatura/ Alış Parametreleri/Genel 3 sekmesinde bulunan Binek Oto Parametreleri kısmından girilir.

\*\*Dokümanda 2026 yılı üst sınırları baz alınmıştır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/55f4e15d-a3c4-47e5-a6e7-d10bef5ef328/es_binekoto_alfatprm.jpg)

<u>Masraf KKEG Oranı:</u> Masraf faturalarının kanunen kabul görmeyen kısmına ait oran girilir.

<u>Kiralama Üst Sınır Bedeli:</u> Kiralama faturaları için araç başına belirlenen gider kabul edilen üst sınır girilir.

<u>Alış KDV+ÖTV Üst Sınır Bedeli:</u> Araç alımlarında KDV ve ÖTV üzerinden yapılacak gider indirimi üst sınırı girilir.

##### 2) Binek Oto Gider Kısıtlamasında Çalışacak Muhasebe Hesaplarının Belirlenmesi

Binek oto uygulaması kapsamında kanunen kabul edilmeyen giderler farklı hesaplarda takip edilir. Bu hesaplar Entegre/Entegrasyon Kodları/Fatura Genel-2 sekmesinde bulunan Kanunen Kabul Edilmeyen Giderler(KKEG) kısmından tanımlanır.

KKEG hesaplarının değişkenlik göstermesi halinde, **KKEG Hesapları Stok Bazında Takip Edilsin** parametresi işaretlenerek Stok/Muhasebe Detay Kod Girişi ekranındaki Satış Diğer hesaplarında da takip edilebilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/86ba0c3a-561a-4df9-8f17-06f9ed947216/es_binekoto_entegrasyunkodlari.jpg)

<u>Gider Hesabı:</u> Binek otomobil alım işlemlerinde, vergisiz matrahın aktarılacağı ilgili muhasebe hesap kodunun girildiği alandır.

<u>KKEG:</u> KKEG kapsamına giren tutarların aktarılacağı muhasebe hesap kodunun girildiği alandır.

<u>KDV Detay Hesabı: </u>KKEG hesabına kaydedilen tutar üzerinden hesaplanan KDV’nin aktarılacağı muhasebe hesap kodunun girildiği alandır.

<u>Nazım Hesaplar Kullanılsın:</u> KKEG, gider olarak kaydedilmesine rağmen vergi matrahından düşülemeyen bir tutardır. Bu tutarın dönem sonunda kolayca izlenebilmesi ve raporlanabilmesi için nazım hesapların kullanılmasını sağlar. Bu parametre aktif edildiğinde; **KKEG + KKEG KDV** toplam tutarı, belirlenen nazım hesaplara borç/alacak kaydı şeklinde otomatik olarak kaydedilir.

##### 3) Binek Oto Uygulamasında Kullanılacak Stok Kartlarının Tanımlanması

Uygulama üzerinde binek otomobil gider kısıtlamasının takibi ve muhasebeleştirilmesi için Hizmet Uygulaması kullanılır. **Fatura / Alış Parametreleri / Genel 1** sekmesinde bulunan **Hizmet Uygulaması** parametresi açılır.

Vergi kanunundaki sınırlandırmalara tabi her bir gider kalemi (kira, bakım-onarım, yakıt, oto alım vb.) için hizmet stok kartları açılır. KKEG (Kanunen Kabul Edilmeyen Gider) üst sınırlarının kullanılabilmesi için bu stokları tanımlarken, Stok Kartı / Ek Bilgiler sayfasındaki Stok Mevzuat Tipi belirlenir. "Binek Oto Alım (Gider)", "Binek Oto Alım (Maliyet)", "Binek Oto Kira" ve "Binek Oto Masraf" mevzuat tipleri; açılan hizmet kartının kullanılacağı amaca yönelik olarak doğru eşleştirilmelidir.

##### Örnek uygulamalar;

Stok Mevzuat Tipi Binek Oto Kira

Şirket, kiralamış olduğu binek otomobil için aylık 55.000 TL kiralama bedeli ödemektedir.

Kiralama hizmeti için açılacak olan stok kartında, mevzuat tipi olarak Binek Oto Kira seçilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/0bc439f9-c9cf-475b-ad54-4a52571916bd/es_binekoto_kirastokkarti.jpg)

Faturada stok mevzuat tipi Binek Oto Kira olan hizmet stoğu seçilir ve kiralama bedeli girilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/7a555e7b-51a6-4b4e-8a5d-1944c9fdba64/es_binekoto_kirafatkalem.jpg)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/d699c83b-aa05-4b04-b68d-5d1aa96bd801/es_binekoto_kirafattoplam.jpg)

Fatura/ Alış Parametreleri/Genel 3 sekmesinde **Kiralama Üst Sınır Bedeli 45.000TL** olarak belirtilmiştir. Bu nedenle kiralama faturasında araç başına en fazla KDV hariç 45.000 TL gider olarak yazılır, kalan tutar kanunen kabul edilmeyen gider olarak kaydedilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/e66d5bd5-d60b-4a16-8d0e-00e9c20d7cea/es_binekoto_kiramuhfis.jpg)

<u>Gider yazılabilecek tutar : </u>**45.000 TL** Araç başına gider gösterilebilen kiralama üst sınırı

Fatura kaleminde seçilen (760-00-001) hesap koduna kaydedilir.

<u>Kanunen kabul edilmeyen gider :</u> **10.000 TL** Kiralama üst sınırını aşan tutar (55.000 TL – 45.000 TL)

Entegre/Entegrasyon Kodları/Fatura Genel-2 sekmesinde bulunan KKEG hesabına(689-00-001) kaydedilir.

<u>Kanunen kabul edilmeyen gidere ait KDV :</u> **1.800 TL** (10.000 TL x 0,18) Üst sınırı aşan tutar üzerinden hesaplanan KDV

Entegre/Entegrasyon Kodları/Fatura Genel-2 sekmesinde bulunan KDV Detay hesabına(689-00-002) kaydedilir.

<u>İndirilecek KDV :</u> **8.100 TL** (45.000 TL x 0,18) Gider Kabul edilen tutar üzerinden hesaplanan KDV

Entegre/Entegrasyon Kodları/Fatura KDV sekmesinde bulunan ilgili KDV hesabına kaydedilir.

Nazım hesaplar KKEG ve KKEG KDV’si toplamı kadar borç alacak olacak şekilde çalışır.

\*Hesaplama 1 adet araç kiralama üzerinden yapılmıştır. Miktar arttıkça üst sınır da miktarla doğru orantılı olarak artacaktır.

##### Stok Mevzuat Tipi Binek Oto Masraf

Şirket, binek olarak kullanılan araç için 10.000,00 TL tutarında masraf yapmıştır.

Masraf faturası için açılacak olan stok kartında, mevzuat tipi olarak Binek Oto Masraf seçilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/689b43de-bc89-48e3-8997-e890a1707c5a/es_binekoto_masrafstokkarti.jpg)

Faturada stok mevzuat tipi Binek Oto Masraf olan hizmet stoğu seçilir ve masraf tutarı girilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/be989533-0f94-4a50-b7cc-58cabce6fb7d/es_binekoto_masraffatkalem.jpg)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/faea68f5-ed6b-4c0c-b02b-bc2f9a24a4d2/es_binekoto_masraffattoplam.jpg)

Fatura/ Alış Parametreleri/Genel 3 **Masraf KKEG Oranı 30** olarak belirtilmiştir. Bu nedenle masraf faturası toplam tutarının%70’i gider olarak yazılır, kalan tutar kanunen kabul edilmeyen gider olarak kaydedilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/918f62f9-4a9e-499c-b2ff-3f6fdb763211/es_binekoto_masrafmuhfis.jpg)

<u>Gider yazılabilecek tutar :</u> **7.000 TL** (10.000TL %70)

Fatura kaleminde seçilen (730-00-004) hesap koduna kaydedilir.

<u>Kanunen kabul edilmeyen gider :</u> **3.000 TL** (10.000TL %30)

Entegre/Entegrasyon Kodları/Fatura Genel-2 sekmesinde bulunan KKEG hesabına(689-00-001) kaydedilir.

<u>Kanunen kabul edilmeyen gidere ait KDV :</u> **600 TL** (3.000 TL x 0,20) Üst sınırı aşan tutar üzerinden hesaplanan KDV

Entegre/Entegrasyon Kodları/Fatura Genel-2 sekmesinde bulunan KDV Detay Hesabına(689-00-002) kaydedilir.

<u>İndirilecek KDV :</u> **1.400 TL** (7.000 TL x 0,20) Gider Kabul edilen tutar üzerinden hesaplanan KDV

Entegre/Entegrasyon Kodları/Fatura KDV sekmesinde bulunan ilgili KDV hesabına kaydedilir.

Nazım hesaplar KKEG ve KKEG KDV’si toplamı kadar borç alacak olacak şekilde çalışır.

##### Stok Mevzuat Tipi Binek Oto Alım(Gider)

Şirket, 1.050.000TL araç bedeli, 840.000TL ÖTV ve 378.000TL KDV bedeli ile araç satın almıştır. KDV+ÖTV bedelini doğrudan gider olarak göstermek istemektedir.

KDV+ÖTV bedelinin doğrudan gider yazılacağı araç alımı için açılacak olan stok kartında, mevzuat tipi olarak Binek Oto Alım(Gider) seçilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/2ee11669-06a5-4b79-ad78-4cce500e28f9/es_binekoto_alimgiderstokkarti.jpg)

Faturada stok mevzuat tipi Binek Oto Alım(Gider) olan hizmet stoğu seçilir ve alış tutarı girilir.

(Örnek KDV hariç olarak yapılmıştır)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/6b3994ed-d0b5-4f13-8cc9-3d924ea7ed87/es_binekoto_alimgiderfatkalem.jpg)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/b30a90ac-6ea8-4218-aa6d-ca0fb8870584/es_binekoto_alimgiderfattoplam.jpg)

Fatura/ Alış Parametreleri/Genel 3 **Alış KDV+ÖTV Üst Sınır Bedeli 1.200.000TL** olarak girilmiştir. Bu nedenle ÖTV+KDV tutarının 1.200.000 TL’sı gider olarak yazılır, kalan tutar kanunen kabul edilmeyen gider olarak kaydedilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/e170b293-3d66-464d-9298-ee7aee98ee63/es_binekoto_alimgidermuhfis.jpg)

<u>Vergisiz matrah :</u> **1.050.000 TL**

Entegre/Entegrasyon Kodları/Fatura Genel-2 sekmesinde bulunan Gider Hesabına (254-00-001) kaydedilir.

<u>ÖTV + KDV tutarının gider yazılabilen kısmı :</u> **1.200.000 TL**

Fatura kaleminde seçilen muhasebe hesabına(760-00-002) kaydedilir.

<u>KDV+ÖTV üst sınır bedelini aşan tutar(KKEG):</u> **18.000 TL**(1.200.000 – (840.000+378.000))

Entegre/Entegrasyon Kodları/Fatura Genel-2 sekmesinde bulunan KKEG hesabına(689-00-001) kaydedilir.

##### Stok Mevzuat Tipi Binek Oto Alım(Maliyet)

Şirket, 1.050.000TL araç bedeli, 840.000TL ÖTV ve 378.000TL KDV bedeli ile araç satin almıştır. KDV+ÖTV bedelini doğrudan maliyete eklemek istemektedir.

Stok kartında mevzuat tipi olarak Binek Oto Alım(Maliyet) seçilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/2cec6eec-3ec4-4f5b-aef1-79b10b54fc80/es_binekoto_maliyetstokkarti.jpg)

Faturada stok mevzuat tipi Binek Oto Alım(Maliyet) olan hizmet stoğu seçilir ve alış tutarı girilir.

(Örnek KDV hariç olarak yapılmıştır)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/00abe1e8-28b9-428a-8e13-4668c62d3d1d/es_binekoto_alimmaliyetfatkalem.jpg)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/d267c3d9-d1e1-4c39-b996-fc6b0fabd2e3/es_binekoto_alimmaliyetfattoplam.jpg)

Binek oto KDV+ÖTV maliyete eklendiği için indirim konusu yapılmaz.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/ee1ebe63-5009-4b44-bb61-7aa3e3cdb3df/es_binekoto_alimmaliyetmuhfis.jpg)

Vergiler dahil matrah Entegre/Entegrasyon Kodları/Fatura Genel-2 sekmesinde bulunan Gider Hesabına (254-00-001) kaydedilir.
