---
title: "Ek-1 (Yurt İçi Döviz Uygulaması)"
page_id: "22805755"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Cari"
  - "Ekler"
  - "Ek-1 (Yurt İçi Döviz Uygulaması)"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Cari / Ekler / Ek-1 (Yurt İçi Döviz Uygulaması)"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWEwYzA1YjZjLWIwNzctNGJjOS04ZGY1LWZlMjJkYTRjMDRlNSZsaW5rPWMwZmI2OTNhLTA3M2YtNDE0ZC05ZGE1LTQ0Njg3YzFmNDY4MyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=a0c05b6c-b077-4bc9-8df5-fe22da4c04e5&link=c0fb693a-073f-414d-9da5-44687c1f4683&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ek-1-yurt-ici-doviz-uygulamasi_29990239_22805755.html"
source_version: "2022-11-21T11:47:55.513+03:00"
source_bytes: 565266
fetched_at: "2026-09-13T04:08:50+00:00"
generator: "netsis-scraper 1.0.0"
---
# Ek-1 (Yurt İçi Döviz Uygulaması)

Yurt İçi Döviz uygulaması hakkında ayrıntılı bilgiye bu dokümandan ulaşılır.

Ek 1 Yurt içi döviz uygulamasında, faturalar dövizli olarak kesilir fakat tahsilat ve ödemeler TL olarak yapılabilir. Ayrıca bu uygulamada, fatura KDV tutarları ayrı hesaplarda takip edilir. TL. olarak yapılan tahsilat veya ödemelerin, dövizli olarak takip edilmesi gerekir. Dövizli olarak takip edilmediğinde, faturalardan kalan döviz bakiyesi bilinemez ve dövizli kapatma işlemi yapılamaz.

Bu uygulamanın yapılması için; programda bulunan alanlar, menü seçeneklerinde yapılması gereken tanımlamalar ve uygulama örnekleri aşağıdaki gibidir.

**Gerekli Tanımlamalar**

**Cari Hesap Kayıtlarında Yapılması Gereken Tanımlamalar**

"Cari Hesap Kayıtları" bölümünde bulunan “Yurtiçi Döviz Tipi” alanı kullanılarak, cari hesabın yurt içi dövizli faturaların hangi döviz tipi ile takip edileceği belirlenir. Bu alan dolu olduğunda program, ilgili cari hesabın yurt içi dövizli fatura işlemi yaptığını algılar ve girilen döviz tipi dışında bir döviz tipi ile fatura girişi yapmaz. TL tahsilatların yapılması için “Döviz Tipi” alanının 0 (sıfır) olarak bırakılması gerekir. Eğer bu alana bir döviz tipi girilirse, TL olarak tahsilat ve ödeme yapılamaz.

Uygulamada; yurt içi döviz tipi dolu, döviz tipi boş bırakılan cari hesapların (senet/çek modülleri dışında) yurt içi döviz tipinden farklı bir döviz tipi ile işlem görmesi engellenmiştir. (Kasa Modülü, Dekont Modülü).

![](../../../../_assets/dad1eba931b235d907f4.png)

Eğer aynı cari ile yurt içi kesilen faturalarda farklı döviz tipleri kullanılıyorsa, kullanılan her bir döviz tipi için ilgili cari hesaba farklı cari hesap kartları açmak gerekir.

Yukarıdaki açıklamalarda, dövizli yurt içi faturaların KDV tutarlarının ayrı hesaplarda takip edildiği ile ilgili bilgiler yer alır. Bu uygulamaya göre, çalışan cari hesaplara KDV tutarlarının aktarılacağı bir cari kart açmak gerekir.

Tüm cari hesaplar için, açılacak KDV cari hesap kodlarının aynı standartta olması gerekir. Program fatura kaydı sırasında, her cari hesabın KDV cari hesap kodunu ayrı ayrı sorgulamaz. Aşağıda açıklaması yer alan “KDV Cari Kod Maskesi” ile KDV cari hesap koduna ulaşılır. Cari kodları açarken; her cari kodun son iki karakteri aynı tanımlanabilir.

**Örneğin:** 00001TL, 00002TL, A0001TL gibi.

**Fatura Modülü Parametrelerinde Yapılması Gereken Tanımlamalar**

Fatura bilgisi kaydedildiğinde, KDV hariç rakamın faturanın kesildiği cari koda, KDV tutarının ise ayrı bir cari koda yazılması için; Fatura → Kayıt → Alış/Satış Parametrelerinin düzenlenmesi gerekir.

“Faturalarda KDV Ayrılsın (C/H Kaydında)” parametresi işaretlenir. Daha sonra, hangi faturalarda KDV tutarının ayrılacağının belirlenmesi için “KDV ile ilgili özel kodun değeri (kod1 veya kod2)” kaydedilir. Parametrede girilecek bilgiye göre fatura kayıtlarında KDV tutarının ayrılacağı anlaşılır.

“KDV Cari Kod Maskesi” alanına, KDV tutarlarının aktarılacağı cari kod maskesinin girilmesi gerekir. Maskede değişken olan ve sabit olan değerler belirtilir. Faturanın kesildiği cari kodla aynı olan karakterler alt çizgi (\_) ile belirtilir. Farklı olan karakterler ise mutlaka belirtildiği şekliyle girilir.

**Örneğin:** Yurt içi döviz uygulaması olan cari kodların 00001DV, 00002DV, 00003DV, 00004DV şeklinde olduğu, bu kodlara karşılık açılan KDV cari kodlarının ise 00001TL,00002TL,00003TL,00004TL olduğu varsayıldığında;

Maskeye beş adet alt çizgi (\_) ve hemen arkasına da TL karakteri girilir. Bunun anlamı; ilk beş karakter fatura kesilen cari hesaba göre değişebilir, bu kodu aynen koru, cari kodun son iki karakterine TL’yi ekleyerek oluşan yeni cari koda KDV tutarlarını aktar.

Bu kodlama sisteminde, 00001DV kodlu cari hesaba bir fatura kesildiğinde, KDV tutarını aktarmak için 00001TL kodlu bir cari aranır. Bulunamazsa KDV tutarı 00001DV cari koduna aktarılır.

**Uygulama**

**Fatura Modülü ve Senet/Çek Modülü**

Örnek ekranlarda bu uygulama nasıl işler? Cari Modülde, yurt içi döviz uygulaması yapan ve kesilen faturaların aktarıldığı 00001DV numaralı bir kod ile kdv tutarlarının aktarıldığı 00001YTL numaralı iki cari kod açıldığında; 00001DV numaralı cari kartta “dövizli cari” alanı işaretlenerek “döviz tipi” alanı 0 (sıfır) bırakılsın ve “yurtiçi döviz tipi” olarak "1" değeri girilsin.

"Satış Parametreleri" bölümünde KDV ile ilgili özel kod değeri olarak “K” ve KDV cari kod maskesi olarak \_\_\_\_\_YTL girilsin.

"Satış Faturası" bölümünde "Ön Sorgulama" sekmesinde yer alan "Özel Kod 2" alanına "K" değeri girilerek, KDV dahil alanı ise işaretlenmeden geçilsin.

![](../../../../_assets/a9c19069d91e9f8cfeee.png)

"Kalem Bilgileri" sekmesine döviz tipi 1, döviz tutarı 100, kuru 1,5 TL olan bir adet kalem girilsin. (Program, döviz tipi 1’den farklı bir tip için kalemin kaydedilmesine izin vermez)

"Toplamlar" sekmesinde "Tamam" butonuna basılarak fatura kaydedilsin.

![](../../../../_assets/2d57e9d3c34514ed6476.png)

"Cari Hareket Kayıtları" bölümünde aşağıda görüldüğü gibi, döviz bilgileriyle,150 TL tutarında bir borç hareketi işlenir.

![](../../../../_assets/2930fb24130b964bdcbd.png)

Faturanın KDV tutarının 00001TL numaralı cari kodun haraketlerine aktarıldığı izlenebilir.

![](../../../../_assets/f418a2d5ae60462c8380.png)

Bu faturaya karşılık, "Müşteri Çekleri" bölümünden döviz değerleri olmayan, 100 TL tutarında bir tahsilat yapılsın ve bu çeki tahsile verilsin.

Yurt içi döviz uygulaması olan cari kodlara, sadece senet ve çek modüllerinden TL tutarlı kayıt girilebilir. Diğer modüllerden TL tutarlı girilemez.

![](../../../../_assets/e3efaac8d3cfa28a4104.png)

"Cari Hareket Kayıtları" bölümünde, girilen TL tutarındaki kaydın alacak olarak işlendiği görülür.

![](../../../../_assets/a7c2596acb828c1c46ea.png)

Çekin vadesi geldiğinde, Dekont → Kayıt → Tahsil-Teminat-Ciro Çekleri Ödeme Dekontu → Çek Tahsil Dekontu bölümünden 2 TL tutarındaki kur ile tahsil işlemi gerçekleştirilir.

![](../../../../_assets/0774ee9f8587ee0ef3a6.png)

Dekont ekranını incelendiğinde, "Alacak Cari Kod" ve "Borç Cari Kod" alanlarına, çeki veren kişinin (00001DV) kodu otomatik olarak ekrana gelir.

Bunu nedeni; Dövizli çalışan cari hesaplarda kapatma işlemi ve dövizli bakiye kontrolünün yapılması için, tüm kayıtlarda döviz bilgisinin olması gerekir. Yukarıdaki caride, 100 TL tutarında bir kayıt mevcut. Tahsil işlemi sırasında, TL tutarındaki çek kaydı ters bir kayıtla kapatılır. TL tutarındaki çek tutarı, girilen döviz kuruna bölünerek yeni döviz tutarı hesaplanır ve bu döviz tutarları ile cari hareket kayıtlarına yeni bir alacak kaydı oluşturulur. Aşağıdaki örnek ekranda, 100 TL tutarındaki kaydın, hem borç hem de alacak olarak işlendiği görüntülenir.

![](../../../../_assets/a62ff07da6d85af37fde.png)

Borç olan harekette döviz bilgisi bulunmaz fakat alacak hareketinde tahsil işlemi sırasında girilen ve döviz kuruna göre hesaplanan döviz tutarı bulunur. (100/2=50)

Aynı yöntemle, cari için kuru 1,5 TL, döviz tutarı 100 olan bir fatura daha kaydedilsin.

**Kasa Modülü ve Dekont Modülü**

"Kasa Modülü" kullanılarak 50 TL tutarında bir kayıt girilsin (Döviz kuru:2, döviz tutarı:25).

Kasa ve Dekont modülünden, yurt içi döviz tipi tanımlanmış cari hesaplardan yapılacak tahsilat ve ödemelerde, işlemin yapıldığı kasa TL olarak tanımlanmış bile olsa mutlaka döviz tipi girilmesi gerekir. Program döviz bilgileri ekranını açar ve "Döviz Tipi" alanına, cari kartta girilen yurt içi döviz tipini ekrana getirir. Program, bu döviz tipinin değiştirilmesine izin vermez.

Bu uygulamanın kullanıldığı durumlarda; Yaşlandırma mantığı ile döviz tutarlarında yaşlandırma yapılması, hareketlerden kaynaklanan bakiye döviz tutarlarının TL tutarlar ile gecikme veya erken ödemelerinin listelenmesi amacıyla, Cari → Raporlar → Ek Listeler → Dövizli Listeler → [Yurtiçi Cariler Dövizli Yaşlandırma Listesi](<../Raporlar - Cari/Ek Listeler - Cari/Dövizli Listeler/Yurtiçi Cariler Dövizli Yaşlandırma Listesi.md>) bölümü kullanılabilir. Ayrıca kapatılmış dövizli faturalar baz alınarak oluşturulan kur farklarının listelenmesi için yine Cari → Raporlar → Ek Listeler → Dövizli Listeler [Yurtiçi Cariler Dövizli Yaşlandırma Listesi](<../Raporlar - Cari/Ek Listeler - Cari/Dövizli Listeler/Yurtiçi Cariler Dövizli Yaşlandırma Listesi.md>)→ bölümü kullanılabilir.
