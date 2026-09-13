---
title: "e-Fatura için İlaç-Tıbbi Cihaz Senaryosu Desteği"
page_id: ""
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "e-Fatura için İlaç-Tıbbi Cihaz Senaryosu Desteği"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / e-Fatura için İlaç-Tıbbi Cihaz Senaryosu Desteği"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTc4Yjg4YmQ0LWJkZjMtNDdjZS04MmIwLTRmNTUzMTU1NWJmYyZsaW5rPTA5OGQ3YTRhLWU1ZTMtNDYxOS04NTYwLWEwNWM5MmNhOTQ5NyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=78b88bd4-bdf3-47ce-82b0-4f5531555bfc&link=098d7a4a-e5e3-4619-8560-a05c92ca9497&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "e-fatura-icin-ilac-tibbi-cihaz-senaryosu-destegi.html"
source_version: ""
source_bytes: 28988
fetched_at: "2026-09-13T04:21:57+00:00"
generator: "netsis-scraper 1.0.0"
---
# e-Fatura İçin İlaç-Tıbbi Cihaz Senaryosu Desteği

9062.5 (LTS sürümü) ve 9064 sürümüyle birlikte e-Fatura belgeleri için İlaç-Tıbbi Cihaz Senaryosu desteklenmiştir. Yapılan düzenlemeyle birlikte Gelir İdaresi Başkanlığı tarafından yayınlanan İlaç-Tıbbi Cihaz teslimlerine ilişkin fatura teknik kılavuzuna göre e-Faturaların oluşturulup, ihtiyaç duyulan alanların form üzerinden eklenmesi sağlanmıştır. Ayrıca Gelir İdaresi Başkanlığı tarafında 01.10.2025 tarihinde devreye alınacak İlaç/Tıbbi Cihaz e-fatura güncellemelerini de içeren yeni e-Fatura Şematron değişiklikleri de, 9.0.66.1 (LTS sürümü) ve 9.0.62.11 (LTS sürümü) dosyaları ile geçerli olacaktır.

İlaç-Tıbbi Cihaz e-Faturalarında bulunması zorunlu alanlar; **Ürün Numarası, Parti-Lot Numarası, Seri/Sıra Numarası, ilaçlar için Son Kullanma Tarihi v**e tıbbi cihazlar için **Üretim Tarihi** bilgileridir.

Bu kapsamda Alış ve Satış Parametre ekranlarında Genel 3 sekmesine **“İlaç-Tıbbi Cihaz Fatura Uygulaması”** parametresi eklenmiştir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/764ad8cb-361b-49c7-a673-07cad639d0a0/tıbbiilaçresim1.png)

Alış ve Satış Fatura Parametre ekranlarında “**İlaç-Tıbbi Cihaz Fatura Uygulaması”** parametresi işaretlendiğinde, aynı zamanda Yardımcı Programlar Modülünde Şirket Şube Parametre Tanımları ekranında “**Seri Takibi Var**” parametresi işaretli ise, **Ürün Numarası, Parti-Lot Numarası, Seri/Sıra Numarası, ilaçlar için Son Kullanma Tarihi (İlaç) ve tıbbi cihazlar için Üretim Tarihi (Tıbbi Cihaz)** adındaki bu 5 alan, Alış ve Satış Fatura parametre ekranlarında aktif olmaktadır. Bu parametre işaretli değilse, bu alanlar pasif gelmektedir.

İlaç/Tıbbı Cihaz e-Faturalarında olması zorunlu bilgilerin, Seri Ekranında yer alan alanlarla eşleştirilmesi gerekmektedir. Örneğin, Ürün Numarası bilgisinin seri ekranındaki hangi alan bilgisine girileceği buradan seçilmelidir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/4e82fd90-b1b6-4fad-a5ca-83d67720aa67/image (9).png)

Satış/Alış Parametre ekranındaki “**İlaç-Tıbbi Cihaz Fatura Uygulaması”** parametresi altındaki gerekli alanların eşleştirilmesinde, seri uygulamasının temel alanları ve Seri Parametre ekranında “**Seri Girişinde Kullanılacak Opsiyonel Sahalar”** kısmında seçilen alanlar gelmektedir. Bu listede gelen seri alanları ile eşleştirilmeler yapılır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/04143a1f-7a13-4b5b-b07c-dbb729ddd199/Resim1.png)

İlaç-Tıbbi Cihaz tipli bir Satış Faturası girildiğinde, Kalem Bilgileri sekmesinde stok kaleminin miktar girişi sonrasında çıkan Seri Takibi ekranından bu zorunlu alanlar girilmelidir.

Bu uygulama aktif edildiğinde, İlaç-Tıbbi Cihaz faturalarını belirlemek için, satış tarafında Satış İrsaliyesi ve Satış Faturasının Üst Bilgiler sekmesine ve alış tarafı için de Alış Faturası Üst Bilgiler sekmesine **“İlaç-T.Cihaz**” parametresi eklenmiştir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/954f7f69-b38b-498b-8dcb-06d64551e034/Resim2.png)

Bu seçenek işaretlendiğinde, belge içinde kullanılacak stokları kontrol edebilmek için, Stok Kartı Kayıtları Ek Bilgiler sekmesinde yer alan Stok Mevzuat Tipi kısmına “**İlaç**” ve “**Tıbbi Cihaz**” olmak üzere 2 yeni Stok Mevzuat Tipi eklenmiştir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/a8ec9aa3-27b8-4c73-a6ff-65d7a3739aff/Resim3.png)

Ürün Numarası, Parti-Lot Numarası, Seri/Sıra Numarası, Son Kullanma Tarihi ve Üretim Tarihi gibi zorunlu alanların girilmesi program içerisinde 3 farklı yerden yapılabilmektedir.

\1. Program genelinde Seri Uygulaması aktifse, Satış Fatura Parametre ekranında “**İlaç-Tıbbi Cihaz Fatura Uygulaması**” altında yer alan zorunlu alanların seri ekranındaki alanlarla eşleştirilip, bu alanlara zorunlu bilgilerin seri ekranından girilmesi gerekmektedir. Dokümanın yukarısında bu tanımlamalardan bahsedilmiştir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/3dd25012-cce4-4fa8-a20b-8b0b75cdab24/Resim4.png)

\2. Seri Uygulamasının program içinden kullanılmayıp, zorunlu girilecek bilgilerin third party sistemler ile takip edildiği durumda, bu düzenleme ile oluşturulan **TBLEFATILACDETAY** tablosuna fatura girişi sonrasında zorunlu bilgilerin manuel kayıt edilmesi gerekmektedir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/7431dbd9-71fc-462f-8d2c-0c680d6a242c/Resim5.png)

\3. Kullacıların elinde ilaç stokları için Sağlık Bakanlığı’ na iletilen XML tipli paket transfer servisi yani pts dosyaları mevcutsa, belge girişinde stoklar gride atıkdıktan sonra sağ tık menüsünde “**İlaç Tıbbi Cihaz İşlemleri/Detay Ekle (PTS)**” seçeneğiyle pts dosyası seçilip dosya içinden zorunlu bilgilerin yer aldığı satırlar seçilmelidir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/592b78f6-5162-4725-89de-496f67cdb310/tıbbiilaçresim2.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/c2a6d784-d741-4867-b656-530618f3de20/Resim7.png)

Ya da tıbbi cihazlar ve ilaç stokları için zorunlu bilgiler excel dosyasına girilmişse,excel dosyasından aktarım yapılması için, belge girişinde stoklar gride atıldıktan sonra, sağ tık menüsünde “**İlaç Tıbbi Cihaz İşlemleri/Detay Ekle (Excel)**” seçeneğiyle excel dosyasındaki bilgilerin içeri alınması sağlanır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/7c8ab849-72f2-404d-8e18-28587f1ce62a/tıbbiilaçresim3.png)![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/c1ddf4f8-10d7-47b7-8f0d-5fb0512af411/tıbbiilaçresim4.png)

İlaç stokları için zorunlu alan girişi sırasında miktar kadar zorunlu satır girişi yapılmalıdır. Örneğin 10 adetlik bir parol ilacı satışında, seri kullanımı varsa, seri ekranında zorunlu alan girişi 10 satır olarak girilmelidir. Ancak tıbbi cihaz stokları için **seri uygulaması olduğunda** seri girişi yapılmak istendiğinde miktar kadar seri girişi zorunluluğu yoktur. Yani tıbbi cihaz stokları için seri girişi yapılmak istendiğinde miktar kadar seri satırı yerine, stok miktarlarına eşit tek satır seri girişi de yapılabilir. Seri uygulaması dışında zorunlu alanların girişi excel ya da **TBLEFATILACDETAY** tablosuna manuel kayıt girişi şeklinde olacaksa bu durumda zorunlu alan satırları aynı bilgileri içerse bile miktar kadar kayıt girişi yapılmalıdır.

Satış Faturası girişinde “**İlaç-T.Cihaz”** parametresi işaretlenerek oluşturulan faturada Stok Mevzuat Tipi “**İlaç**” veya “**Tıbbi Cihaz**” dışında olan bir stok kalemi eklenebilmektedir.

Yurt içi tipli irsaliye bağlantılı bir İlaç-Tıbbi Cihaz Satış Faturası oluşturulduğunda zorunlu alanların girişi fatura belgesi sırasında yapılmalıdır.

Satış Faturası üst bilgiler sekmesinde “**İlaç-T.cihaz**” parametresi işaretlenerek oluşturulan belge için taslak oluşturulduğunda, oluşan e-Faturanın senaryosu “**ILAC_TIBBICIHAZ**” olmaktadır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/fad889cc-09dd-4f86-beeb-4869d5ebee33/Resim9.png)

Taslak oluşturulduğunda ilk bakılan yer, **TBLEFATILACDETAY** tablosundaki kayıtlardır. Eğer tabloda ilgili stok hareket satırına ait kayıtlar bulunuyorsa (ilaç, tıbbi cihaz stokları için girilmesi zorunlu bilgiler TBLEFATILACDETAY tablosuna manuel kayıt edilmiş, belge girişinde pts dosyası içerisinden seçilmiş ya da excel dosyasından aktarılmış olabilir), bu tablodaki değerler kullanılarak taslak oluşturulmaktadır. Seri parametresi açıksa ve Satış Fatura Parametrelerinde seri alanları ile gerekli alanlar arasında bir eşleştirme yapılmışsa, seri ekranına girilen zorunlu bilgiler ile taslak oluşturulmaktadır. Seri uygulaması açık olmasına rağmen zorunlu alanların girişi seri bilgilerinden girilmiyorsa, **TBLEFATILACDETAY** tablosuna pts veya excel aktarımıyla ya da manuel olarak kayıt atılarak istenilen bilgilerle taslak oluşması sağlanabilmektedir.

Taslak sonrasında oluşan XML’ de satır bazında **\<cac:AdditionalItemIdentification\>\<cbc:ID shemeID=”ILAC”\>, \<cac:AdditionalItemIdentification\>\<cbc:ID shemeID=”TIBBICIHAZ”\>** tagleri içerinde gerekli bilgiler yer almaktadır. E-belge görüntüsünde satır bazında gerekli bilgilerin basılması istenirse dizayn bilgilerinde gerekli taglerin eklenmesi ile ilgili düzenleme yapılmalıdır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/3c2fe04d-662d-4550-a0db-87e13fef7768/Resim10.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/d103840b-697a-4f49-9da1-75c87ac7ebe6/Resim11.png)

ILAC_TIBBICIHAZ, bir e-Fatura senaryosu olarak desteklendiği için, SATIS, ISTISNA, TEVKIFAT, TEVKIFATIADE, IADE ve IHRAC KAYITLI fatura tipinde tüm faturalar için ILAC_TIBBICIHAZ senaryolu e-Fatura oluşturulabilmektedir.

Bu sebeple ihraç kayıtlı belgelerin faturalanma süreçlerinde de düzenlemeler yapılmıştır.

İhraç kayıtlı için süreç siparişten başlaması durumunda,

Dış Ticaret Modülü’ nde yurt dışı tipli sipariş dosyaya bağlanırken Siparişlerim sekmesinde “**İlaç-T.Cihaz**” seçeneği işaretlenerek proforma oluşturulur.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/e989f0bd-4cb1-427e-a527-927b53e26d79/Resim12.png)

Oluşan proforma fatura taslak oluşturularak e-Belge olarak gönderilecekse,

Proformada yer alan stoklar için, belge kalemlerinde ilgili stok satırı seçili iken sağ tık menüsünde **İlaç Tıbbi Cihaz İşlemleri** altında **Detay Ekle (PTS), Detay Ekle (Excel) ve İlaç/Tıb. Cihaz Seri Seçimi** seçenekleri eklenmiştir. Bu seçenekler yardımıyla zorunlu alanların girişi yapılır. Ayrıca third party uygulamalar aracılığıyla ya da manuel olarak **TBLEFATILACDETAY** tablosuna manuel kayıt girişi yapılabilir.

**Detay Ekle (PTS**) seçeneği ile zorunlu alanlar pts dosyası üzerinden seçilebilir. **Detay Ekle (Excel)** seçeneği ile zorunlu alanlar excel dosyası yardımıyla içeri alınabilir.

Proformada serili olan stoklar için, **İlaç/Tıb. Cihaz Seri Seçimi** seçeneğiyle, daha önceden ilgili stok için girilmiş olan seri bilgisi seçimi yapılır. Sipariş ve proforma fatura bazında seri uygulaması desteği olmadığı için bu ekranda yeni seri girişi değil varolan seri bilgilerinden seçim yapılır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/1487c316-1b83-412c-ac51-a055fb45d0cb/tıbbiilaçresim5.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/ce467c60-732d-4bc5-b6c0-bc5e95334f3f/Resim14.png)

İhracat dosyasında proforma fatura için Detay Gösterme ekranında Toplam Bilgileri sekmesinde sağ tık menüsünde “**e-Fatura Özel/İstisna Tip Atama**” menüsünden ihraç kayıtlı belgeler için e-Devlet Özel Kod ataması yapılmalıdır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/a0c04878-db80-4d25-9f94-37482ed13209/Resim15.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/1f966fc6-637e-47a0-8037-674ad57c47b5/Resim16.png)

Proforma Fatura yerine İhracat Kapatma sonrası oluşan satış faturası üzerinden e-Belge oluşturulup gönderilecekse,

Proforma fatura içindeki kalemler üzerinde zorunlu alanların girişi yapılmaz. Çünkü proforma fatura kalemlerinde girilen zorunlu alanlar ihracat kapatmayla oluşacak satış faturasına taşınmamaktadır. Proforma fatura üzerinden Çeki Listesi, Çeki listesi üzerinden satış irsaliyeleri oluşturulur. Oluşan bu irsaliyeler Sevkiyatlar sekmesinde görüntülenir. Sevkiyatlar sekmesinde irsaliyede bulunan stoklara ait zorunlu alanların girişi yapılır.

Belge kalemlerinde ilgili stok satırı seçili iken sağ tık menüsünde **İlaç Tıbbi Cihaz İşlemleri** altında **Detay Ekle (PTS), Detay Ekle (Excel) ve İlaç/Tıb. Cihaz Seri Seçimi** seçenekleri yer almaktadır. Bu seçenekler yardımıyla zorunlu alanların girişi yapılır.

**Detay Ekle (PTS)** seçeneği ile zorunlu alanlar pts dosyası üzerinden seçilebilir. **Detay Ekle (Excel)** seçeneği ile zorunlu alanlar excel dosyası yardımıyla içeri alınabilir.

İrsaliye üzerinde serili olan stoklar için, İlaç/Tıb. Cihaz Seri Seçimi seçeneğiyle, daha önceden ilgili stok için girilmiş olan seri bilgisi seçimi yapılır.

Ayrıca third party uygulamalar aracılığıyla ya da manuel olarak **TBLEFATILACDETAY** tablosuna manuel kayıt girişi yapılabilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/f825a3c0-790e-472c-92c9-340c6c85271e/tıbbiilaçresim6.png)

Fatura Modülü’ nde ise, yurt dışı tipli girilen müşteri siparişi ihraç kayıtlı satış irsaliyesine dönüştürülür ve süreç irsaliyeden başlıyormuş gibi ilerler.

İhraç kayıtlı için süreç irsaliyeden başlaması durumunda,

Satış irsaliyesi üst bilgiler sekmesinde **“İlaç-T.Cihaz**” seçeneği işaretlenerek ihraç kayıtlı satış irsaliyesi oluşturulur. Bu şekilde kaydedilen ihraç kayıtlı satış irsaliyeleri,

• Fatura modülünde irsaliye üzerinden toplamlar sekmesinde **Fat** butonu ile faturalaştırılabilir.

• Dekont modülünde ihracat kapatma yapılarak faturalaştırılabilir.

Ancak her şekilde ilaç, tıbbi cihaz stoklarına ait zorunlu alanların girişi irsaliye belgesi sırasında yapılmalıdır.

Dış Ticaret Modülü’ nde ise,

Oluşan proforma fatura taslak oluşturularak e-Belge olarak gönderilecekse,

İhracat dosyası içerisinde, İrsaliyelerim sekmesinde ihraç kayıtlı satış irsaliyesi “**İlaç-T.Cihaz**” parametresi işaretlenerek dosyaya bağlanır ve proforma fatura oluşturulur. Bu durumda irsaliye belgesinde girilmiş zorunlu alanlar proforma faturaya taşınmaktadır. Ayrıca proforma fatura içindeki kalemler üzerinde bu taşınan bilgilerde düzenlemeler yapılabilmektedir.

Eğer irsaliye aşamasında kalemler kısmında bu zorunlu alanlar girilmemiş ise, proforma fatura aşamasında kalemler üzerinde bu zorunlu alanların girişi yapılabilir.

Proforma Fatura yerine İhracat Kapatma sonrası oluşan satış faturası üzerinden e-Belge oluşturulup gönderilecekse,

Proforma fatura içindeki kalemler üzerinde zorunlu alanların girişi yapılmaz. Dosyaya bağlanan irsaliyeler Sevkiyatlar sekmesinde görüntülenmektedir. İrsaliyelerde bulunan stoklar üzerinden zorunlu alanların girişi yapılır.

**Satış sürecinde desteklenen senaryolar,**

\1. Yurt içi satış faturası girişinde “**İlaç-T.Cihaz**” parametresi işaretlenerek oluşan belgelerde, kalemlere ait zorunlu alanların girişi, **TBLEFATILACDETAY** tablosuna manuel kayıt atılması, belge kalemlerinde sağ tık menüsünde yer alan “**Detay Ekle (PTS)**” ile pts dosyasından seçerek, “**Detay Ekle (Excel)**” ile excel dosyasından aktarılarak veya serili stoklarda serilerden oluşması parametrik olarak desteklenmektedir.

!!!Yurtiçi bir irsaliye belgesi için, **TBLEFATILACDETAY** tablosuna manuel kayıt atılmış ise, irsaliye faturaya çevrildiğinde **TBLEFATILACDETAY** tablo kayıtları faturaya taşınmıyor. Bu senaryoda kullanıcının bu detayları irsaliye üzerine değil fatura üzerine girmesi gerekmektedir.

\2. İhraç kayıtlı irsaliye fatura modülünden yürütülürse, **“İlaç-T.Cihaz”** parametresi işaretlenerek oluşan satış irsaliyesinde, kalemlere ait zorunlu alanların girişi, **TBLEFATILACDETAY** tablosuna manuel kayıt atılması, belge kalemlerinde sağ tık menüsünde yer alan “**Detay Ekle (PTS)**” ile pts dosyasından seçerek, “**Detay Ekle (Excel)**” ile excel dosyasından aktarılarak veya serili stoklarda serilerden oluşması parametrik olarak desteklenmektedir. İrsaliye toplamlar sekmesinden faturalaştırılırsa **TBLEFATILACDETAY** tablosundaki irsaliye için girilen kayıtlar faturaya aktarılmaktadır ve taslağın **TBLEFATILACDETAY** kayıtlarından veya serili stoklarda serilerden oluşması parametrik olarak desteklenmektedir.

\3. İhraç kayıtlı sipariş dış ticaret modülünden yürütülürse, ihraç kayıtlı sipariş kaydedilir. Proforma oluştururken “**İlaç-T.Cihaz**” parametresi işaretlenerek oluşturulur. Oluşan proforma üzerinde kalemlere ait zorunlu alanların girişi, **TBLEFATILACDETAY** tablosuna manuel kayıt atılması, belge kalemlerinde sağ tık menüsünde yer alan “**Detay Ekle (PTS)**” ile pts dosyasından seçerek, “**Detay Ekle (Excel)**” ile excel dosyasından aktarılarak veya serili stoklarda seri seçim ekranından serilerin seçimi desteklenmektedir. Proforma fatura üzerinden taslak oluşturulur. Bu durumda taslağın **TBLEFATILACDETAY** kayıtlarından veya serili stoklarda serilerden oluşması parametrik olarak desteklenmektedir.

\4. İhraç kayıtlı sipariş dış ticaret modülünden yürütülürse, ihraç kayıtlı sipariş kaydedilir. Proforma oluştururken “**İlaç-T.Cihaz**” parametresi işaretlenerek oluşturulur. Oluşan proforma fatura üzerinde herhangi bir detay girilmeden proforma fatura üzerinden çeki listesi, çeki listesinden de irsaliye belgesi oluşturulur. Sevkiyatlar sekmesinde kalemlere ait zorunlu alanların girişi, **TBLEFATILACDETAY** tablosuna manuel kayıt atılması, belge kalemlerinde sağ tık menüsünde

yer alan “**Detay Ekle (PTS)**” ile pts dosyasından seçerek, “**Detay Ekle (Excel)**” ile excel dosyasından aktarılarak veya stok serili ise, seri seçim ekranından serilerin seçimi yapılır. İhracat kapatma işlemi ile satış faturası oluşturulur. Oluşan satış faturası üzerinden taslak oluşturulur. Bu durumda taslağın **TBLEFATILACDETAY** kayıtlarından veya serili stoklarda serilerden oluşması parametrik olarak desteklenmektedir.

\5.  İhraç kayıtlı irsaliye dış ticaret modülünden yürütülürse, ihraç kayıtlı satış irsaliyesi kaydedilir. Eğer irsaliye girişinde **“İlaç-T.Cihaz**” parametresi işaretli ise, irsaliye kalem girişinde zorunlu alanları girişi yapılırsa, proforma oluştururken “**İlaç-T.Cihaz”** parametresi işaretlenerek irsaliye dosyaya bağlanmalıdır. Bu durumda irsaliyede girilmiş zorunlu alanlar proforma faturaya taşınmaktadır. Ayrıca proforma fatura üzerinden de bu taşınan bilgiler üzerinde düzenleme yapılabilmektedir. Eğer irsaliye aşamasında kalem girişinde zorunlu alanlar girilmemiş ise, proforma fatura aşamasında da bu bilgiler girilebilir. Proforma fatura üzerinden e-Fatura oluşturulduğunda, taslağın **TBLEFATILACDETAY** kayıtlarından veya serili stoklarda serilerden oluşmasını parametrik olarak desteklenmektedir.

6.   İhraç kayıtlı irsaliye dış ticaret modülünden yürütülürse, ihraç kayıtlı satış irsaliyesi kaydedilir. İrsaliye girişinde **“İlaç-T.Cihaz**” parametresi işaretli, irsaliye kalem girişinde zorunlu alanların girişi yapılmadığında, proforma oluştururken “**İlaç-T.Cihaz”** parametresi işaretlenerek irsaliye dosyaya bağlanmalıdır. Oluşan proforma fatura üzerinde herhangi bir detay girilmeden proforma fatura üzerinden çeki listesi, çeki listesinden de irsaliye belgesi oluşturulur. Sevkiyatlar sekmesinde kalemlere ait zorunlu alanların girişi, **TBLEFATILACDETAY** tablosuna manuel kayıt atılması, belge kalemlerinde sağ tık menüsünde yer alan **“Detay Ekle (PTS)”** ile pts dosyasından seçerek, **“Detay Ekle (Excel)”** ile excel dosyasından aktarılarak veya stok serili ise, seri seçim ekranından serilerin seçimi yapılır. İhracat kapatma işlemi ile satış faturası oluşturulur. Satış faturası üzerinden e-Fatura oluşturulduğunda, taslağın **TBLEFATILACDETAY** kayıtlarından veya serili stoklarda serilerden oluşmasını parametrik olarak desteklenmektedir.

Alış tarafı için, e-Faturadan Alış Faturası Oluşturma adımında,

• e-Faturada yer alan kalemler ile program içindeki stokların eşleştirildiği durumda, eğer eşleştirilmesi yapılan stok kodu serili bir stok ve girişlerde seri takibi yapılıyorsa, oluşan alış faturasında seri kayıtları da otomatik olarak oluşturulmaktadır.

• e-Faturada yer alan kalemler ile program içindeki stokların eşleşmediği durumda, alış faturası içerisinde EFATURA_STOK koduyla atılan kalemlerin düzenlenmesi sırasında seçilen stok kodu serili bir stok olsa bile, e-Fatura içindeki kaleme ait seri kayıtları, seri ekranına ve ilgili seri tablosuna aktarılmamaktadır.

Ancak her durumda gelen İlaç/Tıbbi Cihaz e-Faturalarındaki kalemlere ait detay bilgiler yeni oluşturulan TBLEFATILACDETAY tablosuna kaydedilmektedir.
