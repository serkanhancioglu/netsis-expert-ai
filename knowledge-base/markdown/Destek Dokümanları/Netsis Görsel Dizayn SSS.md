---
title: "Netsis Görsel Dizayn SSS"
page_id: "66248534"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis Görsel Dizayn SSS"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis Görsel Dizayn SSS"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTlkMmRlN2Y4LTc1MWQtNDQ1MC1iYTdlLTdiM2U5M2M2NTQzNyZsaW5rPTc4ZWYzNzE3LWM3MzMtNDFhYS1hMmM1LTJiNzFmNTc0NDdlZCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=9d2de7f8-751d-4450-ba7e-7b3e93c65437&link=78ef3717-c733-41aa-a2c5-2b71f57447ed&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-gorsel-dizayn-sss_80088595_66248534.html"
source_version: "2022-06-02T10:56:17.950+03:00"
source_bytes: 678036
fetched_at: "2026-09-13T04:24:29+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis Görsel Dizayn SSS

**Görsel dizaynda birden fazla dataset kullanılabilir mi?**

Görsel dizayn ve görsel raporlarda dizayn data bölümünde birden fazla data nesnesi eklenerek dizaynda kullanılabilir.

![](../_assets/ac6422cf3615a6a85b9f.png)![](../_assets/88c8700f99ad5368e9af.png)

**Farklı kağıt ebatları için sayfa ayarı nasıl yapılır?**

File menüsünden Page Settings ile veya sayfa üzerinde çift tıklanıp sayfa seçeneklerine girilerek Paper sekmesindeki Size alanından istenen kağıt türü seçilebilir. Seçilen kağıt türüne göre yükseklik ve genişlik değerleri otomatik gelmektedir.

![](../_assets/55a25ca3746763ffb83d.png)

**Görsel dizaynda veritabanındaki barkod kodu için barkod basımı nasıl yapılır?**

Object Toolbar’dan barcode aracı dizayna eklenerek DataField bölümünden barkod olarak basılmak istenen alan seçilip kullanılabilir.

![](../_assets/ce765683e80f234b5f69.png)

**Görsel dizayn veya görsel raporda MasterData bandı üzerinde gösterimi yapılacak veriler belirli filtrelere göre kısıtlanabilir mi?**

MasterData üzerinde sağ tıklanarak edit menüsünden select dataset ekranına girilip filter bölümünde istenen kısıtlayıcı ifade yazılarak masterdata üzerindeki veriler kısıtlanabilir. Örneğin; Ekran görüntüsünde belirtilen görsel rapor için masterdata’da miktar değeri 10’dan küçük olanların gösterilmemesi için expression editor’de kısıtlama yapılarak işlem sağlanmıştır.

![](../_assets/5d6eff4ca7bdc29dc653.png)![](../_assets/e0a214c2ee7617353529.png)

Expression’da birden fazla alan seçilerek bir ifade yazılabilir.
Örn; (\<dznsiparis."sthar_gcmik"\>\*\<dznsiparis."sthar_nf"\>)\>1

**Dizayn ve rapor sayfalarına sayfa numarası nasıl eklenir?**

Dizayn veya görsel rapora sayfa numarası eklemek için object toolbar’dan system text aracı dizayna eklenerek system variable alanında \[PAGE#\] ve \[TOTALPAGES#\] değişkenleri için ekleme yapılabilir.

Dizaynın yazdırılması sırasında dizayndaki bir bilginin çıktıda gösterilmemesi isteniyor. Herhangi bir alan için yazıcı çıktısında gizleme yapılabilir mi?

Önizlemede gösterilen bir alanın yazıcı çıktısında saklanması için, seçilen memo nesnesinin properties’inde bulunan visibilty özelliği vsPrint=False yapılarak gözükmemesi sağlanabilir.

**Stok kartına eklenen resimler görsel dizayn ve raporda gösterilebilir mi?**

Stok kartına eklenen png, jpg formatındaki görsellerin dizaynda kullanılabilmesi için dizaynda kullanılan data view’ın TBLEVRAK tablosu ilişkilendirilmesi gerekir. Stok kartı kayıtları ekranından kaydedilen evraklar için TABLOTIPI alan değeri 1 olarak kaydedilmektedir. Evrak tablosundaki bilgi sütununda görsel bilgisi saklanmaktadır. BILGI sütunu data view’a eklendikten sonra object toolbar’dan picture object dizayna eklenerek, nesnenin properties’ından dizaynda kullanılan dataset seçilip datafield alanında BILGI sütunu seçilebilir. Bu sayede dizayn üzerinde dinamik olarak stok kartına eklenen görsellerin gösterimi sağlanabilir.
Örneğin;
SELECT
/\*\*\*/
EVRAK.BILGI
FROM DZNSIPARIS SIPARIS
LEFT OUTER JOIN TBLEVRAK EVRAK ON SIPARIS.STOK_KODU=EVRAK.KOD AND EVRAK.TABLOTIPI=1

**Görsel dizayn ve görsel raporda band nesnelerinin kullanımı zorunlu mudur?**

Band nesneleri kullanılmadan da dizayn oluşturulabilmektedir. Ancak tablo içeren ve bir veri kümesini barındıran dizaynlarda doğru sonuca ulaşmak için band kullanımı gereklidir.

**MasterData’daki verilerin toplamı nasıl alınabilir?**

Dizayna eklenen memo nesnesi çift tıklanarak insert aggragate seçeneğine tıklanmalıdır. Function bölümünden Sum fonksiyonu seçilerek DataBand ve toplam alınmak istenen DataField bilgisi belirtilip band üzerindeki alanın toplam değeri gösterilebilir.

![](../_assets/c56fed07a7c864aa1640.png)

**MasterData’da bulunan tablo verilerinin belirli sütun değerlerine göre gruplandırılması nasıl sağlanır?**

Band seçeneklerinde bulunan Group Header kullanılarak masterdata verileri belirli ilkelere göre gruplandırılabilir.
Örneğin; Ekran görüntüsündeki dizaynda sipariş kalemlerindeki ürünler grup kodu alanına göre gruplandırılarak gösterilsin isteniyor. Bunun için dizaynda masterdata’nın üzerinde yer alacak şekilde group header eklenerek data field bölümünde gruplandırılmak istenen alan seçilmelidir. Her grup değişiminde yeni bir sayfa oluşturulması için start new page seçeneği işaretlenebilir.

![](../_assets/1f02183571af24aa4266.png)

**Basım yapılan dizaynların (log) takibi sağlanabilir mi?**

Modül dizaynları ekranından Log Tutulsun parametresi evet seçilerek yazdırma işlemlerinde log kayıtlarının oluşturulması sağlanabilir. Dizayn modülünden Basım Log Raporu alınarak dizaynın ne zaman, hangi kullanıcı tarafından ve bilgisayar kullanılarak hangi yazıcıya gönderildiği gibi bilgiler geriye dönük raporlanabilmektedir.

**Daha önce basımı bir belgenin ikinci kez yazdırılması engellenebilir mi?**

Modül dizaynları ekranında bulunan Tekrarlı Basım Kontrolü parametresi Reddet seçilerek daha önce yazdırılan bir belgenin ikinci kez yazdırılması engellenebilir.

**Dizayn bazında varsayılan yazıcı ataması yapılabilir mi?**

Toplu Yazıcı Atama ekranı kullanılarak dizayn kodu bazında yazıcı seçilip varsayılan olarak atanabilir. Bu sayede farklı dizaynlarda farklı yazıcıların kullanımı söz konusu ise yazdırma işlemi sırasında yazıcı seçimine gerek olmadan varsayılan olarak tanımlanan yazıcıdan çıktı alınması sağlanabilir.

**Netsis’in önceki sürümlerinde oluşturulan fr3 uzantılı görsel dizayn dosyaları güncel sürümlerde kullanılabilir mi?**

Netsis 9.0.30 sürümü ile birlikte fr3 uzantılı dizayn dosyalarının veritabanında saklanması sağlanmıştır. Eski sürümlerde oluşturulan fr3 uzantılı dizayn dosyası görsel dizaynda şablon dosya adı kısmından seçilerek dizayn kaydedildiğinde otomatik olarak veritabanına kaydedilmektedir. Eski dosyaların kullanımı için özel bir işleme gerek bulunmuyor.

**Dizayn ve raporlarda Drill-Down (data drilling) özelliği kullanılabilir mi?**

Drill-Down rapor üzerinde hiyerarşik bir yapı ile detay bilgilere ulaşmak için kullanılır. Görsel dizaynlarda group header bandı drill-down özelliğine sahiptir. Group header’da drill-down özelliğinin seçilmesi durumunda grup etkileşimli bir hale dönüşecektir. Bu sayede görsel rapor veya görsel dizaynın önizleme modunda grup başlığına tıklanarak detay kayıtların gösterimi sağlanabilir.

![](../_assets/433b3414335b1a905e42.png)![](../_assets/bae8bc61b132453fe20d.png)

Drill-Down ile oluşturulmuş örnek rapor önizlemesi aşağıdaki gibidir. (Dizaynda bölge ve il grup başlığına tıklanarak detay kayıtların listelenmesi sağlanabilir.)

![](../_assets/8cc2910dfbe934bb7617.png)

**Band içindeki satırlara satır numarası verilebilir mi?**

Band içindeki satırların satır numaralarını göstermek üzere Line değişkeni kullanılabilir. Bunun için object toolbar’dan system text nesnesi dizayna eklenerek system variable’dan \[#Line\] seçilmelidir.
Not: Raporda gruplama varsa ve detay kayıtlarda numaralandırmanın yeniden başlatılması isteniyorsa grup başlığında \[#Line\] detay kayıtlar için \[Line\] etiketi kullanılmalıdır.

![](../_assets/17aae856284fbc02a32e.png)![](../_assets/8cc2910dfbe934bb7617.png)![](../_assets/bef5a1ca97bdf2b301e2.png)

**Görsel dizayn veya görsel raporda highlight kullanımı nasıl yapılır?**

Highlight kullanılmak istenen alan üzerinde çift tıklanarak memo nesnesinin özelliklerine girilmelidir. Üst kısımda bulunan highlight sekmesine geçilerek conditions alanında istenen koşul yazılabilir. Aynı nesne üzerinde birden fazla koşul uygulanabilmektedir. Aşağıdaki örnekte Miktar alanı için değerin 100’den büyük olması durumunda alan için özel biçimlendirme yapılmıştır.

![](../_assets/d2d1cb96fd6329c7bfc2.png)![](../_assets/4c18ad91f83a72e247aa.png)![](../_assets/716659449b2b51ae0312.png)

**Görsel dizayn veya görsel raporda grafik kullanımı nasıl yapılır?**

Görsel rapor veya görsel dizayna grafik eklemek için object toolbar’dan chart object rapor sayfasına eklenmelidir. Eklenen chart object’in edit menüsüne girilerek add series bölümünden gösterimi istenen grafik türü belirlenmelidir. Chart Editor sekmesinde grafik için kullanılacak DataSet ve Values alanları belirlenmelidir.
Not: Dataset üzerinden grafik oluşturulabileceği gibi dizayndaki bir band nesnesi de grafik için veri kaynağı olarak kullanılabilmektedir.

![](../_assets/b8e8151d28f673c718bc.png)

Görsel rapor üzerinde grafiklerin örnek gösterimi aşağıdaki gibidir:

![](../_assets/0e2265ac4643880b5a1e.png)![](../_assets/a09a7a909afc9a452172.png)
