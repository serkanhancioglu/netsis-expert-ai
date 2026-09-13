---
title: "Hesap Planı"
page_id: "24740369"
product: "netsis-3-enterprise"
depth: 5
is_section: true
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Muhasebe"
  - "Muhasebe Modülü"
  - "Kayıt / Muhasebe"
  - "Hesap Planı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / Kayıt / Muhasebe / Hesap Planı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTAwMTUyZjk4LThmZDQtNGVkMS1hNTJlLTlkMmRmY2MxMzk3OSZsaW5rPTBmYzAxOTJlLTY0MmUtNDQ5NS1iZThiLTgwMDMwODQyM2JjNiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=00152f98-8fd4-4ed1-a52e-9d2dfcc13979&link=0fc0192e-642e-4495-be8b-800308423bc6&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "hesap-plani_24740372_24740369.html"
source_version: "2022-09-27T10:22:18.077+03:00"
source_bytes: 621974
fetched_at: "2026-09-13T04:12:48+00:00"
generator: "netsis-scraper 1.0.0"
---
# Hesap Planı

Hesap Planı, Muhasebe Bölümü'nde, "Kayıt/Muhasebe Modülü" menüsünün altında yer alır. Hesap Planı bölümü; hesap planı kayıtlarının oluşturulmasını, oluşturulan kayıtların izlenmesini, düzenlenmesini ve iptal edilmesini sağlayan bölümdür.

Hesap planı kayıtları yapılırken program tarafından bazı kontroller yapılır ve bazen girilen hesap kodları kabul edilmez. Hesap kodları tanımlanırken yapılan seviye takibine göre, ana, grup, muavin sırasında kayıtların girilmesine özen gösterilmesi gerekir. Bu konuda kullanıcıya yardımcı olması için Muhasebe → Kayıt → [Muhasebe Parametreleri](<../Muhasebe Parametreleri.md>) → Seviye → "Seviye Takibi" parametresi işaretlendiğinde, "Hesap Planı" ekranının üstünde, parametrelerde tanımlanan seviye formatı izlenir.

Hesap Planı ekranı; Hesap Planı, Döviz Bilgileri, Ek Bilgiler ve Tutar/Miktar Bilgileri olmak üzere dört sekmeden oluşur.

**Hesap Planı**

![](../../../../../_assets/df9a328d77cb7ce0a231.png)

Hesap Planı ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Hesap Planı Ekranı |  |
| --- | --- |
| Hesap Kodu | Parametre seçimlerindeki seviye takibi ve uzunluklara göre hesap planının kodlarının tanımlandığı alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodlarına ulaşılır. |
| Hesap Türü | Hesap kodu kaydedildikten sonra, hesap kodunun Ana-Grup-Muavin olarak türünün belirtileceği bir ekran görüntülenir. Program, (seviye takibinin yapıldığı durumlarda) yazılan hesap koduna göre ne tür bir hesap girildiğini algılar ve otomatik olarak ilgili seçenek işaretli şekilde ekrana gelir. Bu seçeneğe, sadece yeni bir hesap kodu açılırken müdahale edilebilir. Program, açılan bir hesap üzerinde hesap türünün değiştirilmesine izin vermez. |
| Hesap İsmi | Kaydı oluşturulan hesap koduna ait isim bilgisinin girildiği alandır. |
| Yabancı Hesap İsmi | Muhasebe → Kayıt → [Muhasebe Parametreleri](<../Muhasebe Parametreleri.md>) → Genel → "Yabancı Hesap İsmi" parametresinin işaretlenmesi ile aktif hale gelen alandır. Tanımlanan hesap için istenen yabancı hesap isminin girilmesini sağlar. |
| Grup Kodu | 1994 yılı başından itibaren uygulanan standart hesap planı sisteminde hesaplar, ilk iki hanelerindeki rakamlara göre gruplandırıldığı için, hesap kodunun ilk iki hanesi program tarafından otomatik olarak "Grup Kodu" alanına aktarılır. Üzerinde düzenleme yapılabilir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, grup kod girişi bölümünde tanımlanan grupların rehberine ulaşılır. |
| Hesap Tipi | Kaydedilen hesap kodlarına ait hesap tipi belirlenen alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile, Aktif, Pasif, Bilanço, Gelir, Gider ve Nazım tipleri arasından seçim yapılır. Tip belirlemeleri, Bilanço Kar/ Zarar dökümleri için gereklidir. "Aktif" ve "Pasif" hesaplar "Bilanço" tablolarını oluşturulurken, "Gelir/Gider" hesapları ise "Kar/Zarar" tablolarının oluşturulmasında kullanılır. |
| Cari Bağlantılı | Cari hesapları ilgilendiren hesaplar için (120, 320 gibi) kullanılan seçenektir. "Cari Modülde" cari hesap açılmış ve bu hesaba ait "Muhasebe Modülünde" de bir muavin hesap tanımlanmış ise, muavin hesapta bu alanın işaretlenmesi gerekir. Program; dekont işlemlerinden girilen kayıtlarda ve muhasebe kodunun kullanıldığı durumlarda, cari kodun girilmesi gerektiği ile ilgili uyarı vererek, sadece cari kodun kullanılmasını sağlar. |
| Banka Bağlantılı | Banka hesaplarını ilgilendiren hesaplar için kullanılan seçenektir. "Banka Modülünde" cari hesap açılmış ve bu hesaba ait "Muhasebe Modülünde" de bir muavin hesap tanımlanmış ise, muavin hesapta bu alanın işaretlenmesi gerekir. Program; dekont işlemlerinden girilen kayıtlarda ve muhasebe kodunun kullanıldığı durumlarda, banka kodunun girilmesi gerektiği ile ilgili uyarı vererek, sadece banka kodunun kullanılmasını sağlar. |
| Bağlantısız | İlgili hesap kodunun cari bağlantısız olarak kullanıldığı, ön muhasebe modüllerinde işlem yaparken bu hesabın cari hesap kartı olup olmadığı ile ilgili kontrol **yapılmaması** için işaretlenmesi gereken seçenektir. |
| Enflasyon Fark Hesabı | VUK, enflasyon düzeltmelerinin enflasyon fark hesaplarında takip edilmesini öngörür. SPK ise, ayrı bir enflasyon defteri tutulmasını önerir. Enflasyon Fark Hesaplarının ilk olarak "Hesap Planı" girişi bölümünde tanımlanması gerekir. "Enflasyon Fark Hesabı" alanında, enflasyon düzeltmesine tabi tutulacak olan ilgili hesap için kullanılması istenen fark hesabı belirlenir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile hesap kodlarına ulaşılır. Fark hesabı, birden fazla muavin hesap için geçerli olabilir. İstenirse ana hesap için tek fark hesabı tanımlanabilir. Bu hesap alt muavinler için de geçerli olur. (Muavin hesapta tanımlı bir fark hesabı yoksa). Ancak muavin hesapta, ve bağlı ana hesabında tanımlı fark hesabı yoksa, program enflasyon düzeltmelerini, hesabın kendisi üzerinde yapar. Bu durumda Enflasyon Muhasebesi (VUK) uygulamasına göre, enflasyon düzeltmelerini ayrı satırlar halinde aynı hesaba TL olarak yazar. **IAS29** uygulamasında ise bu alanın bir önemi yoktur. Bu uygulamada "Enflasyon Fark Hesapları" çalışmaz. Aynı hesap kodu üzerinde ikinci defterdeki alanlar çalışır. Bazı hesaplarda her bir muavin hesap için bir de enflasyon fark hesabı açma zorunluluğu vardır. |
| Ölçü Birimi | Sadece raporlara yönelik ölçü birimleri (Kg, Ad vb.) kullanılması istendiğinde bilgi girişi yapılan alandır. Bu alan, muhasebe tutarları ile birlikte miktar açısından da izleme yapılacaksa önem kazanır. Belirli hesapları içeren bir rapor hazırlanması istendiğinde, ilgili hesap kodlarına aynı işaretin kaydedilmesi şartıyla "Rapor Modülünden" maskeleme yaparak istenen bilginin alınması kolaylaşır. |
| Çalışma Tipi (Borç/Alacak) | Tanımlanan hesap bakiyesinin çalışma tipinin seçildiği alandır. Borç ve Alacak olmak üzere iki seçenekten oluşur. İşaretlenen seçeneğe göre Muhasebe → Raporlar → Denetim Listeleri → "[Borç-Alacak Karşılaştırma](<../../Raporlar - Muhasebe/Denetim Listeleri - Muhasebe/Borç-Alacak Karşılaştırma Raporu.md>)" raporundan, ters bakiye veren hesapların listeleri ay koduna göre alınır. |
| İşletmelerde Ortak | Açılan muhasebe hesap kodunun hangi işletmede kullanılacağının belirlendiği alandır. Tanımlanan muhasebe hesap kodunun hangi işletmede kullanılması isteniyorsa, o işletmenin kodu girilir. Tüm işletmelerde ortak olarak kullanılması istendiğinde, "-1" değerinin girilmesi gerekir. |
| Şubelerde Ortak | Açılan muhasebe hesap kodunun hangi şubede kullanılacağının belirlendiği alandır. Tanımlanan muhasebe hesap kodunun hangi şubede kullanılması isteniyorsa, o şubenin kodu girilir. Tüm şubelerde ortak olarak kullanılması istendiğinde, "-1" değerinin girilmesi gerekir. |
| Hariç Tutulacak Şube Tanımlamaları | İlgili hesap kodunun hangi şubelerde kullanılmayacağının belirtildiği alandır. |

**Döviz Bilgileri**

![](../../../../../_assets/16bb90bb26944af6f0f7.png)

Hesap Planı ekranı Döviz Bilgileri sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Hesap Planı Ekranı |  |
| --- | --- |
| Dövizli Hesap | Muhasebe → Kayıt → [Muhasebe Parametreleri](<../Muhasebe Parametreleri.md>) → Dövizli Muhasebe → FAS52 seçeneğinin işaretlenmesi ile ekrana gelen alandır. Hesapların, firma döviz tutarlarının hesaplanması için kullanılır. "Dövizli Hesap" parametresinin işaretli olmadığı hesaplarda firma döviz tutarları oluşturulamaz. Kur farkı gelir/gider hesapları ve değer artış fonu hesaplarında bu parametrenin işaretlenmemesi gerekir. "Dövizli Hesap" seçeneği, enflasyon muhasebesi kullanıldığında da işlev kazanan bir seçenektir. Enflasyon muhasebesi ile ilgili, bu seçeneğin kullanımı hakkında detaylı bilgi için; Muhasebe → Ekler → Ek-1 Enflasyon Muhasebesi dokümanına bakılabilir. |
| Parasal Hesap | Tanımlanacak hesap kodunun parasal hesap olarak işlem görmesi istendiğinde işaretlenmesi gereken seçenektir. Parasal ve parasal olmayan hesapların ayrılması için kullanılır. Parasal Hesap; para değerindeki değişmeler karşısında nominal değerlerini koruyan fakat satın alma güçleri düşen kalemlerdir. Parasal Olmayan Hesap; parasal hesapların dışında kalan tüm hesaplardır. Parasal Hesap seçeneği ile ilgili detaylı bilgi için; Muhasebe → İşlemler → [Döviz Çevrim](<../../İşlemler - Muhasebe/Döviz Çevrim.md>) dokümanına bakılabilir. "Parasal Hesap" seçeneği, enflasyon muhasebesi kullanıldığında da işlev kazanan bir seçenektir. Enflasyon muhasebesi ile ilgili, bu seçeneğin kullanımı hakkında detaylı bilgi için; Muhasebe → Ekler → [Ek-1 Enflasyon Muhasebesi](<../../Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/index.md>) dokümanına bakılabilir. |
| Döviz Tipi | İlgili hesabın takip edileceği döviz tipinin girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, döviz tipleri arasından seçim yapılır. Bir hesabın dövizli çalışması ve yevmiye fişlerinden mutlaka döviz tutarları ile kaydedilmesi istendiğinde, ilgili hesaba döviz tipi girilmesi gerekir. Döviz tipi girilen hesaplarda, yevmiye fiş girişinde ilgili hesap için sorgulanan "Döviz Tutarı" alanı boş bırakılamaz. "Döviz Tipi" alanı 0 (sıfır) olarak bırakıldığında, yevmiye fiş girişinde ilgili hesap için döviz girişi zorunlu tutulmaz ve istendiğinde döviz bilgisi girişi yapılabilir. Döviz Tipi, Döviz Takibi → Kayıt → [Döviz İsimleri Tanımlama](<../../../../Genel/Döviz Takibi/Kayıt - Döviz Takibi/Döviz İsimleri Tanımlama.md>) bölümünden tanımlanır. "Döviz Tipi" alanı, ekrandaki diğer alanlarda olduğu gibi enflasyon muhasebesi kullanıldığında da işlev kazanan bir seçenektir. Enflasyon muhasebesi ile ilgili, bu seçeneğin kullanımı hakkında detaylı bilgi için; Muhasebe → Ekler → [Ek-1 Enflasyon Muhasebesi](<../../Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/index.md>) dokümanına bakılabilir. |
| Hesaplama Türü | Muhasebe → İşlemler → Döviz Çevrim bölümünden oluşturularak, firma döviz tutarı alanlarına aktarılacak döviz değerlerinin hesaplatılması sırasında, kullanılacak hesaplama türünün seçildiği alandır. Kayıt Tarihi, Ortalama Kur ve Verilen Tarih olmak üzere üç seçenekten oluşur. Hesaplama türleri, yevmiye fiş kayıtlarında operasyon tipi ve tutarı boş olan hesaplar için önem taşır. Operasyon tipi veya tutarı dolu olan hesaplarda, her zaman yevmiye fişlerindeki evrak tarihi baz alınır. |
| Enflasyon Fark Hesap Kodu | Enflasyon muhasebesi kullanıldığında işlev kazanan alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılır. Enflasyon muhasebesi ile ilgili, bu seçeneğin kullanımı hakkında detaylı bilgi için; Muhasebe → Ekler → Ek-1 Enflasyon Muhasebesi dokümanına bakılabilir. |

**Ek Bilgiler**

![](../../../../../_assets/dbbfd6ea05fe5fbb91b1.png)

Hesap Planı ekranı Ek Bilgiler sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Hesap Planı Ekranı |  |
| --- | --- |
| Hesap Kodu | Tanımlanan hesap kod ve adının izlendiği alandır. |
| Kayıt Yapan/Kayıt Tarihi | İlgili hesap kodunun oluşturulma tarihi ve hesap kodunu ilk tanımlayan kullanıcı bilgisinin izlendiği alandır. |
| Değişiklik Yapan/Değişiklik Tarihi | İlgili muhasebe kodunda son yapılan değişikliğin tarihi ve değişikliği yapan kullanıcı bilgisinin izlendiği alandır. |
| Sayısal Sahalar/Alfa Sayısal Sahalar | Muhasebe → Kayıt → Muhasebe Parametreleri → "Kullanıcı Tanımlı Sahalar" sekmesinde tanımlanan başlık alanlarına göre, muhasebe kodları için girilen ek bilgi alanlarıdır. Rapor amaçlı kullanılır. |

**Tutar/Miktar Bilgileri**

Tutar/Miktar Bilgileri sekmesi; "Hesap Planı" sekmesinde seçilen hesabın, içinde bulunulan günün tarihine kadar oluşan Borç/Alacak tutar ve miktarlarının aylık bazda görüntülenmesini sağlayan sekmedir. Muavin butonu kullanılarak rapor alınabilir.

![](../../../../../_assets/61ff3e69b4aae64fbe1d.png)

Hesap ile ilgili kayıtlar girildikten sonra “Kaydet” ![](../../../../../_assets/865524a70e225c89c107.jpg) butonu ile kayıt tamamlanır. Açılan bir kayıt, kayıt sil ![](../../../../../_assets/2df4b343310bcd16b01e.jpg)butonu ile iptal edilir veya üzerinde değişiklik yapılması için kaydet ![](../../../../../_assets/865524a70e225c89c107.jpg) tuşu kullanılarak düzeltilir.
