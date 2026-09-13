---
title: "Cari Devir"
page_id: "24753449"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Genel"
  - "Sene Sonu Devir"
  - "Kayıt / Sene Sonu Devir"
  - "Finans / Sene Sonu Devir"
  - "Cari Devir"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Sene Sonu Devir / Kayıt / Sene Sonu Devir / Finans / Sene Sonu Devir / Cari Devir"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTE1OGFmZGY5LWFiN2EtNGIyZi04OWE5LTFmZDA2Y2IyOTRkNCZsaW5rPTA5ZThiNTA1LTVhZTAtNGNhZS05MDhjLTIxOWQ2OGY1OTExNSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=158afdf9-ab7a-4b2f-89a9-1fd06cb294d4&link=09e8b505-5ae0-4cae-908c-219d68f59115&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "cari-devir_47073736_24753449.html"
source_version: "2022-12-12T15:49:17.037+03:00"
source_bytes: 297507
fetched_at: "2026-09-13T04:18:12+00:00"
generator: "netsis-scraper 1.0.0"
---
# Cari Devir

Cari Devir, Genel Bölümü'nde, "Kayıt/Sene Sonu Devir" menüsünün altında yer alır. Cari Devir işlemi, **Enterprise** ürününü kullanan ve birden fazla işletme tanımlanan firmalarda işletmelerin merkezinde, **Standard** ve **Entegre** ürünleri ile **Enterprise** ürününde işletme tanımlanmayan firmalarda ise merkezde çalıştırılması gerekir. Cari Devir, cari hareketlerin her çeşit devri, şube bazında ayrı ayrı otomatik olarak oluşturulur. Cari Devir, cari hesapların devir işleminin yapılmasını sağlayan bölümdür. Cari Devir işleminden önce, cari hesap sabit bilgilerinin yeni sene şirketine aktarılma işleminin "Yeni Yıl Kopyalama" bölümünden önceden yapılması gerekir. "Yeni Yıl Kopyalama" işleminden sonra eski yıl şirketinde oluşturulan cari hesap sabit bilgisi varsa, bu bilgiler "Sabit Kayıt Kontrolü" ile yeni yıl şirketine aktarılabilir. Burada, sabit kayıtlara bağlı hareketlerin devri yapılarak, sonuç devir hareketi yeni sene şirketindeki hareketlere işlenir.

Yeni yıla ait kayıtları yeni yıl şirketine girmeyi tercih eden firmalar, modül devirleri yapılana kadar, eski yıla ait devir bilgilerini yeni yıl şirketinde göremez. Dolayısıyla firmalar, modül devri yapılıncaya kadar, Yaşlandırmalı Ödeme Emri, Cari Risk Takibi ve Özel Hesap Kapatma yapamaz. Bu tür uygulamaları olan firmalar, cari hesap mutabakatları yapılana kadar, yani yıla ait kayıtları eski yıl şirketine girmek şartıyla işlemlerini gerçekleştirebilir.

"Cari Devir" ekranı girişinde, ilk olarak uyarı ekranı görüntülenir.

![](../../../../../_assets/8a2bfc741b7361e227b4.png)

Program cari döviz farkı kapatma işlemini çalıştırınız uyarısını dövizli çalışma varsa devir yapılmadan önce cari modülde kur farklarının kapatılma işleminin yapılması için verir.

Cari Devir Ekranı; Giriş, İşlem ve İşlem Sonucu olmak üzere üç sekmeden oluşur.

**Giriş**

**![](../../../../../_assets/46daabcaa155ec0ba6e7.png)**

**İşlem**

İşlem sekmesi Genel Parametreler ve Cari Kısıtları olmak üzere iki sekmeden oluşur.

**Genel Parametreler**

**![](../../../../../_assets/b761839466141a6fb809.png)**

Cari Devir ekranı İşlem sekmesi Genel Parametreler bölümünde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Cari Devir Ekranı |  |
| --- | --- |
| Devir Şirketi | Yeni yılda kullanılacak şirket isminin girildiği alandır. Girilen şirketin önceden açılmaması gerekir. Girilen şirket program tarafından açılır. "Yeni Yıl Kopyalama" işlemi aynı yeni yıl şirketinin ismi kullanılarak birden fazla tekrarlanıyorsa, "Yeni Yıl Kopyalama" işlemi öncesinde devir şirketinin "Şirket Silme işlemiyle silinmesi gerekir. |
| Devir Tipi | Cari devirler yapılmadan önce kullanılacak devir tipinin seçildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile, Bakiyeli Devir ve Cari Hesap Tipine Göre seçenekleri arasından seçim yapılır. **Bakiyeli Devir:** Devir baz tarihinden sonraki kayıtlar aynen aktarılır. Bu tarihten önceki kayıtların devri oluşturulur. **Cari Hesap Tipine Göre:** Cari sabit karttaki hesap tipine göre devir yapılır. Yaşlandırma ile çalışan dövizli cariler için yaşlandırma işlemi yapılmaz, bakiyeli devir gibi çalışır. Özel hesap kapatmalı çalışan dövizli cari hesaplarda kur farkı otomatik aktarılır. Kur farkı hesaplaması, devir döviz tarihi baz alınarak yapılır. |
| Devir Baz Tarihi - Bakiyeli Devir | "Tarih Aralıklı Devir" mantığına göre devredilecek cari hesaplarına, aktarılacak hareket devirleri için sınır tarihi belirlenen alandır. |
| Devir Baz Tarihi - Cari Hesap Tipine Göre Devir | Yaşlandırmalı devir için, en son hangi tarihe kadar olan hareketlerin devrinin yapılacağının gösterildiği sınır tarihi alanıdır. Cari hareket kayıt tarihleri baz alınır. Bu tarihten sonraki kayıtlar aynen aktarılır. "Cari Hesap Tipine Göre Devir" seçeneğinde, cari sabit kayıtlarında, her cari için ayrı ayrı belirlenen Cari Hesap Tipine (Yaşlandırma/Özel Hesap Kapatma) göre Borç/Alacak yaşlandırması yapılarak, kalan açık hareketler yeni yıla ayrı ayrı devir kaydı olarak devredilir. "Cari Hesap Tipine Göre Devir" seçeneğine göre yaşlandırma, borçlu çalışan cari hesaplarda borç hareketlerini alacak hareketleriyle, alacaklı çalışan cari hesaplarda alacak hareketlerini borç hareketleriyle otomatik kapatır ve açıkta kalan (ödenmemiş) hareketleri devir olarak yeni seneye aktarır. Özel hesap kapatma ile çalışan firmaların, cari devirden önce, Cari → Ek Listeler → Denetim Listeleri → "Özel Hesap Kapatma Denetimi Listesi" ekranından eksik kapatmaları ve yapılan kapatmaların doğruluğunu kontrol etmesi gerekir. Plasiyer uygulamasının kullanıldığı durumlarda, yaşlandırma sonucu bulunan ve yeni yıl şirketine aktarılan hareketlere plasiyer kodları da taşınır. Plasiyer bazında yaşlandırma yapılmaz. |
| Devir Tarihi | Devir hareketlerinin yeni sene şirketine işleneceği kayıt tarihinin girildiği alandır. Büyük çoğunlukla yeni yılın ilk günü girilir. |
| Sabit Kayıt Kontrolü Yapılsın | Cari devir yapılırken sabit kayıt kontrolünün yapılması için kullanılan seçenektir. |
| Proje Kırılımlı Devir | Devrin, proje kırılımlı yapılması için kullanılan seçenektir. İşaretlenmediği zaman, alanın sağ tarafında yer alan rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, proje kodları arasından seçim yapılır. İşaretlendiğinde, rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg)pasif olarak görünür. |
| Cari Devir Ekranı | Bakiyeli Devir Parametreleri ![](../../../../../_assets/7e6605eb4e4295b67d16.png) |
| Bakiyeli Devir Tipi | **Tarih Aralıklı:** Devir yapılacak tarihten sonrasına kaydedilen hareketler olduğunda kullanılan seçenektir. **Örneğin;** Yeni sene şirketinde, eski senenin 11. aya kadar devir bilgisini ve 12. ayın bilgilerini direkt görmek için kullanılabilir. **Son Bakiye:** Cari hesabın son borç/alacak bakiyesinin, tek devir hareketi olarak yeni sene şirketine aktarılması için kullanılan seçenektir. Proje kodu ve/veya döviz kullanımı varsa, proje/döviz kırılımında bakiyeler ayrı ayrı islenir. Eğer eski sene şirketinde hiç yeni sene kaydı girilmemiş ve cari kayıtlarında özel hesap kapatma kullanılmamışsa, hız açısından tavsiye edilen devir yöntemidir. Eski yıl şirketine yeni yıl kaydı girilmesi halinde, yeni yıla ait kayıtlar olduğu gibi yeni sene şirketine aktarılır. |
| Devir Kayıtlarında Ortalama Vade Tarihi Hesaplansın | Geçmiş yıl şirketindeki cari hareketlerin, devir tarihine göre ortalama vade gününün bulunmasını sağlayan seçenektir. Bulunan gün değeri devir tarihine eklenerek, devredilen hareketlerin vade tarihi alanına aktarılır. Cari hesaplarda "Puan Uygulamasının" kullanıldığı durumlarda, puan bakiyelerinin de cari hareketlere taşınması sağlanır. Sadece "Bakiyeli Devir" seçeneği için desteklenir. |
| Plasiyerlere Göre Kırılım Yapılsın | "Plasiyer Uygulaması" kullanan firmalarda "Plasiyerlere Göre Kırılım Yapılsın" seçeneği işaretlendiğinde, devir olarak aktarılan cari hareketler için plasiyer koduna göre kırılım yapılır. Yardımcı Programlar → Kayıt → Şirket/Şube Parametreleri → Plasiyer Uygulaması Var parametresinin işaretlenmesi ile aktif hale gelen seçenektir. |
| Bakiyesi 0 Olan Carinin Puan Bilgisi Aktarılsın | Cari devri yapılırken bakiyesi sıfır olan cari hesabın puan bilgisinin aktarılması için kullanılan seçenektir. |
| Cari Devir Ekranı | Cari Hesap Tipine Göre Devir Parametreleri ![](../../../../../_assets/2a4a06899761cbd9067f.png) |
| Eski Kayıtlara Devir Tarihi Atılsın | Eski sene şirketindeki cari hareketlerden kapatması yapılmayanları yeni sene şirketine aktarırken, "Kayıt Tarihi" alanına işlem sırasında belirlenen devir tarihinin aktarılması için kullanılan seçenektir. Bu şekilde yapılan devirde kayıt tarihleri düzenlenerek vade tarihlerinde değişiklik yapılmaz. Seçenek işaretlenmeden devir yapılması halinde ise, kayıt tarihleri olduğu gibi aktarılır. |
| Devir Döviz Tarihi | Dövizli devir yapıldığı durumlarda ve "Yaşlandırma Kur Türü" alanında “Devir Döviz Tarihi Kuru” seçildiğinde, bu alana girilen tarih baz alınarak işlem yapılır. |
| Cari Devir Ekranı | Yaşlandırma Parametreleri |
| Yaşlandırma Tarihi | Cari hesap tipine göre devir seçeneği için yapılacak yaşlandırma tarih türünün seçildiği alandır. Kayıt Tarihi ve Vade Tarihi olarak iki seçenekten oluşur. Yaşlandırma sırasında otomatik olarak yapılacak borç/alacak kapatma hareketlerinin yapılacağı tarih sırası belirlenir. |
| Dövizli Yaşlandırma | Cari hesaplarda "Dövizli" seçeneği işaretlenen cari kartlar için geçerlidir. Alanın sağ tarafında yer alan aşağı ok butonu ile seçim yapılır. Yapılmasın, Firma Döviz Tipine Göre, Cari Hareket Döviz Tiplerine Göre olmak üzere üç seçenekten oluşur. **Yapılmasın:** Yaşlandırma ile çalışan dövizli cariler için yaşlandırma işlemi yapılmaz, bakiyeli devir gibi çalışır. **Firma Döviz Tipine Göre:** Yardımcı Programlar → [Şirket Şube Parametre Tanımlamaları](<../../../Yardımcı Programlar/Kayıt - Yardımcı Programlar/Şirket - Şube - Parametre Tanımları.md>) → "Düzeltme Tipi" alanında seçilen döviz tipine göre yaşlandırma yapılması için kullanılan seçenektir. Öncelikle, firma döviz değerlerinin hesaplanması, Cari → İşlemler → "Döviz Tutarlarını Oluşturma" işleminin çalışması ve cari hareketlerde firma döviz tutarlarının oluşması gerekir. Yaşlandırma sadece firma döviz tipinde bulunan döviz tutarlarına göre yapılır. Yeni yıl şirketine aktarılan cari hareketlerde, firma dövizi cinsinden bulunan döviz bakiyeleri “Döviz Tutarı” alanına, “Yaşlandırma Kur Türü” bölümünde kur bilgisine göre hesaplanan TL değerleri ise borç/alacak alanlarına - özel hesap kapatmalı cari hesaplar için firma dövizine göre işlem yapılmaz - aktarılır. Yeni yıl şirketine firma dövizine göre devir yapılmadan önce, eski yıl şirketinde Cari → Raporlar → Ek Listeler → "Tarih Aralıklı Yaşlandırma Listesi" ekranından gerekli kısıtlamalar yapılarak ve “Firma Döviz Tipine Göre Dökülsün” seçeneği işaretlenerek, oluşacak hareketlerin kontrol edilmesi sağlanır. **Cari Hareket Döviz Tiplerine Göre:** Yaşlandırma ile çalışan dövizli cariler için yaşlandırma işlemi carinin hareketi bulunan döviz tiplerine göre yapılır. Dövizli cari hesaplar İçin, hareket girişi sırasında girilen operasyon dövizlerine göre yaşlandırmalı devir yapılması için kullanılan seçenekti. Bu durumda her bir döviz tipi için, kendi içinde yaşlandırma yapılır ve yeni yıl şirketinde devir hareketleri bu kırılıma göre oluşur. Cari kartında "Özel Hesap Kapatma" seçeneği işaretli olan dövizli carilere, açıkta kalan döviz hareketleri aktarılır. Yeni yıl şirketinde oluşacak hareketler, eski yıl şirketinde Cari → Raporlar → Ek Listeler → "Tarih Aralıklı Yaşlandırma Listesi" ekranından gerekli kısıtlamalar yapılarak ve “Döviz Tipine Göre Kırılım” seçeneği işaretlenerek, oluşacak kayıtların kontrol edilmesi sağlanır. "Yurtiçi Dövizli Cariler" için de yaşlandırmalı devir yapılabilir. Eğer cari kartında" Yurtiçi Döviz Tipi" seçilmişse ve "Dövizli Yaşlandırma" bölümünde “Cari Hareket Döviz Tiplerine Göre” seçeneği işaretlenmişse, yurtiçi döviz tipine göre yaşlandırmalı devir yapılabilir. "Firma Döviz Tipine Göre" seçeneği "Yurtiçi Dövizli Cariler" için kullanılamaz. |
| Yaşlandırma Kur Türü | "Firma Döviz Tipine Göre" ya da "Cari Hareket Döviz Tipine Göre" devir seçildiğinde, yaşlandırma sonucu bulunan döviz bakiyelerinin TL tutarlarının oluşacağı kur bilgisi türünün seçildiği alandır. Hareket Kuru ve Devir Döviz Tarihi Kuru olmak üzere iki seçenekten oluşur. **Hareket Kuru:** Yaşlandırma sonucu bulunan hareketlerin, girildiği tarihteki kur ile yeni yıl şirketine aktarılması için kullanılan seçenektir. **Devir Döviz Tarihi Kuru:** Yaşlandırma sonucu bulunan hareketlerin, "Devir Döviz Tarihi" alanında girilen tarihteki kur bilgisi ile aktarılması için kullanılan seçenektir. Geçmiş yıl şirketinde, yıl sonunda kur farkı hesaplama çalıştırılmışsa, “Devir Döviz Tarihi Kuru” seçilerek işlem yapılması gerekir. |
| Proje Bazında Yaşlandırma Yapılsın | Proje Uygulaması kullanıldığı zaman aktif hale gelen seçenektir. Proje kodu bazında yaşlandırma yaparak devirlerin oluşması için kullanılır. İşaretlenmediği zaman, yaşlandırma sırasında proje kodları dikkate alınmaz; fakat yaşlandırma sonucu kalan rakamlara, hangi hareketten kaldıysa o hareketin proje kodu aktarılır. |
| Cari Alt Kodlarıyla Beraber | Cari devrin cari alt kodlarıyla beraber yapılması için kullanılan seçenektir. |
| Özel Hesap Kapatmalı Carilerde Kur Farkı Atmasın | Cari devri yapılırken özel hesap kapatmalı cari hesaplarda kur farkı atmaması için kullanılan seçenektir. |
| ![](../../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilgilerin onaylanmasını sağlayan butondur. |
| ![](../../../../../_assets/249197106fa4d90d9fe9.png) Çıkış | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |

**Cari Kısıtları**

Cari Kısıtları, devri yapılması istenen cari hesaplarla ilgili kısıtlamaların yapılmasını sağlayan sekmedir. Ekranda, cari sabit kayıtlarında girilen bilgiler listelenir. Carilerin bölüm bölüm devrinin yapılması için kullanılır. Ekrana yeni bir satır eklemek için klavyeden "Insert", seçili olan satırı silmek için de "Delete" tuşuna basılması gerekir.

**![](../../../../../_assets/c2427668fa1f996b95bf.png)**

Cari devrinde oluşacak kayıtları birkaç örnek ile açıklamak gerekirse aşağıdaki örneklerde, Cari Hesap Tipine Göre devir tipi belirlendiği kabul edilir.

**Örnek 1**

Cari Hesap Tipi: Yaşlandırma

Cari Hesap: Dövizli

Döviz Tipi: 0 ve

Dövizli Yaşlandırma “Yapılmasın” işaretlendiği zaman, "Döviz Yaşlandırma" seçilmediği için döviz kırılımlı tarih aralıklı bakiye devri yapılır. Döviz tipi bazında ve proje kodu - kullanılıyorsa - bazında borç/alacak bakiyeleri bulunur ve her bir kırılım için ayrı bir devir hareketi yeni senede oluşturulur. TL dışındaki döviz tipleri için oluşturulan satırlardaki TL değerler, döviz bakiyesine ve verilen kur tarihine göre yeniden hesaplanır.

**Örnek 2**

Cari Hesap Tipi: Yaşlandırma

Cari Hesap: Dövizli

Döviz Tipi: 0 ve

Dövizli Yaşlandırma “Cari Hareket Döviz Tiplerine Göre” seçeneği işaretlendiği zaman, döviz tipine göre yaşlandırma yapılarak her döviz tipi için açıkta kalan hareketler, kendi döviz tipleriyle yeni senede oluşturulur. Proje kodu - kullanılıyorsa - varsa, her bir devir satırının eski senedeki kendi proje kodu, yeni senedeki devir hareketine taşınır. TL dışındaki döviz tipleri için, oluşturulan satırlardaki TL değerler, döviz bakiyesine ve verilen kur tarihine göre yeniden hesaplanır. Yaşlandırma işleminde "Yaşlandırma" alanında belirlenen Kayıt Tarihi/Vade Tarihi seçeneği geçerlidir.

**Örnek 3**

Cari Hesap Tipi: Yaşlandırma

Cari Hesap: Dövizli

Döviz Tipi: 0 (sıfır)’dan farklı ve

Dövizli Yaşlandırma “Yapılmasın” işaretlendiği zaman, Döviz Yaşlandırma seçilmediği için, tarih aralıklı bakiye devri yapılır. Döviz tipi bazında ve proje kodu - kullanılıyorsa - bazında borç/alacak bakiyeleri bulunur ve her bir kırılım için ayrı bir devir hareketi yeni senede oluşturulur. Sene içinde, cari karttaki döviz tipi değiştirilmiş ve birden fazla farklı döviz tipine ait hareket mevcutsa, sadece cari karttaki döviz cinsinden kayıtlı hareketler dikkate alınır. Oluşturulan satırlardaki TL değerler, döviz bakiyesine ve verilen kur tarihine göre yeniden hesaplanır.

**Örnek 4**

Cari Hesap Tipi: Yaşlandırma

Cari Hesap: Dövizli

Döviz Tipi: 0 (sıfır)’dan farklı ve

Dövizli Yaşlandırma “Cari Hareket Döviz Tiplerine Göre” seçeneği işaretlendiği zaman, cari karttaki döviz tipine göre yaşlandırma yapılarak, açıkta kalan hareketler ilgili döviz tipiyle yeni senede oluşturulur. Proje kodu - kullanılıyorsa - her bir devir satırının eski senedeki kendi proje kodu, yeni senedeki devir hareketine aktarılır. Sene içinde, cari karttaki döviz tipi değiştirilmiş ve birden fazla farklı döviz tipine ait hareket mevcutsa, sadece cari karttaki döviz cinsinden kayıtlı hareketler dikkate alınır. Oluşturulan satırlardaki TL değerler, döviz bakiyesine ve verilen kur tarihine göre yeniden hesaplanır. Yaşlandırma işleminde, "Yaşlandırma" alanında belirlenen Kayıt Tarihi/Vade Tarihi seçeneği geçerlidir.

**Örnek 5**

Cari Hesap Tipi: Yaşlandırma

Cari Hesap: Dövizli

Dövizli Yaşlandırma “Firma Döviz Tipine Göre” seçeneği işaretlendiği zaman, cari hareketler İçin firma dövizine göre yaşlandırma yapılarak, açıkta kalan hareketler firma döviz tipiyle yeni senede oluşturulur. Proje kodu - kullanılıyorsa - yaşlandırma sonucu bulunan her bir devir satırının eski senedeki kendi proje kodu yeni senedeki devir hareketine aktarılır. Oluşturulan satırlardaki TL değerler döviz bakiyesine ve seçilen kur türüne göre, Kayıt Tarihi hareket tarihindeki kura göre, Devir Döviz Tarihi ise devir döviz tarihindeki kura göre hesaplanır.

**Örnek 6**

Cari Hesap Tipi Özel Hesap Kapatma ve Cari Hesap Dövizli seçildiği zaman, Döviz bazında kapatılan tutarların farkları, her bir döviz tipi için ayrı ayrı yeni senede oluşturulur. TL dışındaki döviz tipleri için oluşturulan satırlardaki TL değerler, hareket tarihindeki kur ile bakiye döviz tutarı çarpılarak hesaplanır. TL dışındaki her bir döviz tipinin, devir tarihindeki kur üzerinden TL bakiyesi ile, önceki maddede hesaplanan TL bakiyesi arasındaki fark, ayrı bir kur farkı kaydı olarak TL değeri hesaplanarak yeni senede oluşturulur. TL dışındaki bu döviz tipleri için eski senede kaydedilen kur farkı hareketleri dikkate alınmaz. "Özel Hesap Kapatması" olan cari hesaplarda, "Dövizli Yaşlandırma" seçeneğinin işaretlenip-işaretlenmemesi, cari kartta döviz tipinin sıfır ya da sıfırdan farklı olması, yaşlandırma işleminin kayıt/vade sırasında yapılması etkilemez. Devir yukarıdaki şekliyle yapılır. Ayrıca, "Firma Döviz Tipine Göre" devir yapılamaz.

**İşlem Sonucu**

İşlem sırasında oluşan hatalar "İşlem Sonucu" sekmesinde görüntülenerek farenin sağ tuşuna tıklanarak dosyaya kaydedilir. Gelen hataların incelenmesi gerekir.

"Yeni Yıl Kopyalama" işlemi, devir şirketi oluşturulduktan sonra, herhangi bir hatadan dolayı yarım kalabilir. İşlemin kesilmesine sebep olan problem çözüldükten sonra; yeni sene için açılan şirketi sıfırlayarak ya da, yeni sene hazırlık işlemine kalınan yerden devam etmek mümkündür.

Açılan şirketi sıfırlayarak yeni yıl kopyalama işlemine baştan başlamak için, "Şirket Silme" işlemi ile yeni şirketin silinmesi gerekir.

Kalınan yerden "Yeni Yıl Kopyalama" işlemine devam etmek için, işlem tekrar çalıştırılarak, sorgulanan sahalara daha önceden girilen bilgilerin girilmesi ve "Evet" butonuna tıklanması gerekir.

Bu durumda, kalınan yerden işleme devam etmek istenip istenmediğinin sorgulandığı bir ekran görüntülenir. “Evet” butonuna tıklanması ile yeni yıl şirketinin tekrar kopyalanmasına gerek kalmadan devir işlemine devam edilir.

İşlemler bittiğinde, modül devirleri öncesi, yeni sene kayıtlarına başlama ortamının hazırlanması işlemi tamamlanır. İstendiğinde eski senenin kayıtları bitene kadar, hiç bir modülün devri yapılmadan eski sene şirketinde ve yeni sene şirketinde ayrı ayrı çalışılarak kayıtlara devam edilebilir. Eski senenin devir kayıtları, eski sene kapatılıp devir yapıldığında yeni sene bilgilerine aktarılır. İstendiğinde modül devirleri programın içinden yapılmayıp, açılan yeni sene şirketinde elle kaydedilebilir. Bu işlemlerden biri yapılmadan yeni sene bakiyelerini doğru olarak izlemek mümkün değildir.

"Yeni Yıl Kopyalama" işlemi ile devri oluşturulan eski şirkete girerken, “Şirket devri yapılmıştır. Devir Şirketi: DEVIR. Bu şirketin sadece rapor amaçlı kullanılması tavsiye edilmektedir. Yeni yıla ait kayıtlarınızı veya düzeltme işlemlerinizi DEVIR şirketine yapabilirsiniz!” şeklinde bir uyarı mesajı görüntülenir.

Dosyaya bağlanan ve dosyası kapatılan dış ticaret belgelerinin yeni yıl şirketine aktarılmaması sağlanır.
