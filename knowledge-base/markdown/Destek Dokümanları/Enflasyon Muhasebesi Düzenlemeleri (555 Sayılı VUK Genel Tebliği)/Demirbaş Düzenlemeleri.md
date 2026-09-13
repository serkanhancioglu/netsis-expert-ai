---
title: "Demirbaş  Düzenlemeleri"
page_id: "134053894"
product: "netsis-3-enterprise"
depth: 3
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Enflasyon Muhasebesi Düzenlemeleri (555 Sayılı VUK Genel Tebliği)"
  - "Demirbaş  Düzenlemeleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Enflasyon Muhasebesi Düzenlemeleri (555 Sayılı VUK Genel Tebliği) / Demirbaş  Düzenlemeleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWY2OTYyNjZlLTFhZWMtNGEzNC05MGE1LTI5Yjk1ZjMyZmVkYSZsaW5rPTU3Nzg5MTUwLWI2YmItNGMxYi1hYjUwLWZjNTE4ZjEyODY2NyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=f696266e-1aec-4a34-90a5-29b95f32feda&link=57789150-b6bb-4c1b-ab50-fc518f128667&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "demirbas-duzenlemeleri_134054310_134053894.html"
source_version: "2024-02-12T08:53:01.017+03:00"
source_bytes: 525449
fetched_at: "2026-09-13T04:22:42+00:00"
generator: "netsis-scraper 1.0.0"
---
# Demirbaş Düzenlemeleri

## Demirbaş Modülü

31 Aralık 2023 tarihi itibariyle birikmiş amortismanlar, ait oldukları kıymetin bilanço tarihindeki değerinde, düzeltme sonrasında ortaya çıkan artış oranı dikkate alınarak düzeltilmelidir.

## Döviz Takibi

Temelset uygulamasını kullanan kullanıcılar için Demirbaş uygulamasında döviz tanımlama ve kur girişi yapması gerekmemektedir. Demirbaş Temelset üzerinden bu bilgileri otomatikman alacaktır. Temelset uygulamasını kullanmayan kullanıcılar için Döviz Takibi ekranından aşağıda anlatılan tanımlamaların yapılması gereklidir.
Enflasyon düzeltmesi işleminin çalıştırılabilmesi için öncelikle, enflasyon endekslerinin ilgili ay ve yıllar için girilmesi gerekmektedir. Bu işlem için enflasyon endekslerinin girilebileceği bir döviz tipi tanımlanmalıdır. Bu tanım sırasında Netsis Sıra Numarası olarak AYLIK ENFLASYON ORANI değerinin seçilmesi gerekmektedir.

![](../../_assets/2b6fda0f179fe5ee2752.png)

Sonrasında Döviz Kurları Girişi ekranındaki Tüm Enflasyon Oranlarını Güncelle butonu ile veya manuel olarak her ayın son gününe, kullanılacak olan endeks tipine göre ilgili değerler girilmelidir. Tüm Enflasyon Oranlarını Güncelle butonu tıklandığında çıkan ekran üzerinden hangi endeks tipinin kullanılacağı seçilebilecektir ve burada seçilen endeksler servis üzerinden getirilerek kaydedilmiş olacaktır. Endeks değerlerinin istenen hassasiyette tanımlanabilmesi için Netsis Ondalık Sisteminde Kur alanı için gerekli düzenlemeler yapılabilir.

![](../../_assets/aba1ee4d85334889c575.png)

**Parametre Girişi**

Netsis Demirbaş uygulamasında ilk olarak Parametre Girişi ekranında Enf.Muh. Düz.Tipi alanında enflasyon muhasebesi işlemlerinde kullanılacak olan enflasyon düzeltme tipinin tanımlanması gereklidir. Aynı zamanda VUK kapsamında enflasyon düzeltme işlemlerinin yapılabilmesi için TL Muhasebe seçeneğinin de işaretli olması gereklidir.

![](../../_assets/d021c4048b9c0086cea5.png)

### Enflasyon Muhasebesine Başlama

Demirbaş modülünde, Sabit Kıymet bilgilerinin enflasyon muhasebesi başlangıç tarihine getirilmesi için kullanılacak işlemdir. Sabit Kıymetleri, her bir sabit kıymetin tanımındaki alış tarihine ya da varsa yeniden değerleme tarihine tanımlı endeks ve form üzerinde verilen tarihe tanımlı endeks değerlerini kullanarak bulduğu katsayı ile çarparak düzeltilmiş sabit kıymet değerini bulur. Aynı katsayı ile birikmiş amortisman tutarı da hesaplanır.

![](../../_assets/fdfe9022268332d2dc61.png)

### Enflasyon Muhasebesi Devir Bilgileri

Enflasyon muhasebesine başlama adımı ile oluşturulmuş olan devir kayıtlarının izlenebileceği bölümdür. İstenirse bilgiler üzerinde değişiklik yapılabilir.

![](../../_assets/4188f9ca85a24a6038f8.png)

### Enflasyon Muhasebesi Devir Bilgileri Listesi

Netsis Demirbaş/ Rapor Modülünde yer alan bu rapor ile enflasyon muhasebesine başlangıç işlemi yapıldıktan sonra mevcut kayıtlarla düzeltilmiş kayıtlar arasındaki sabit kıymet ve birikmiş amortisman farkları raporlanabilir. Bu bilgiler ile, fark fişleri kolaylıkla işlenebilir.

![](../../_assets/f345a929a436d39b00a2.png)

### Değerleme ve Amortisman Ayırma

Enflasyon muhasebesine başlama işleminden sonra değerleme ve amortisman ayırma işlemi çalıştırıldığında bulunan katsayılara göre gerekli düzenlemeler demirbaş kayıtlarına yansıtılmış olacaktır.
**Örnek:** 50.000 TL değerinde 01.01.2022 tarihinde alınmış bir sabit kıymet için 2023/12 tarihinde enflasyon muhasebesine başlama işlemi çalıştırılmıştır. Bu işlem sonrası elde edilen tutarların hesaplanması su şekildedir:

![](../../_assets/ba84c2758255b3ae5a9c.png)

Netsis döviz kur giriş ekranında aşağıdaki endeks değerlerinin tanımlı olması gereklidir.
Sabit kıymetin alış tarihindeki endeksi (31.01.2022) : 1.129,03
31.12.2023 tarihindeki endeks : 2.915,02
Enf.düz katsayısı : 2.915,02 / 1.129,03 = 2,58188
Düz. Sabit Kıymet : 50.000 \* 2,58188 = 129.094,00
Düz. Birikmiş Amortisman: 20.000 \* 2,58188 = 51.637, 6
Hesaplanan bu değerler Enflasyon Muhasebesi Devir Bilgileri ekranından izlenebilir.

Bu işlemin ardından 2024/01 için değerleme ve amortisman ayırma işlemi çalıştırıldığında demirbaşın sabit kıymet ve birikmiş amortisman değerlerini endekslere göre bulunan katsayılar ile düzeltilerek bulunan yeni değerler üzerinden amortisman ayrılmaya devam etmektedir. Bu hesaplama şu şekildedir:

Döviz kurları ekranında enflasyon düzeltme endeksleri tanımlanmalı:
31.01.2024 endeksi : 3.035,59
31.12.2023 endeks : 2.915,02
Değerleme Oran Girişi ekranından 2024/1 için Enf.Göre Oran Getir butonu ile veya manuel olarak değer artış oranının girilmesi gereklidir.

![](../../_assets/04251abf1e50c92b482c.png)

Değerleme oranı : ((3.035,59 / 2.915,02) -1) \* 100 = 4,13616
Düz.Sabit Kıymet: 129.094,00
Düz. Birikmiş Amort: 51.637, 6
Değerleme oran girişi yapıldıktan sonra Değerleme ve Amortisman Ayırma ekranında 2024/1 için amortisman ayırma işlemi çalıştırılır. Enflasyon muhasebesi kullanıldığı müddetçe Değerleme Durumu alanı pasif ve Enflasyon Düzeltmesi olarak seçili gelecektir.

![](../../_assets/adcf052797ec76000f31.png)

Amortisman ayırma işlemi sonrasında Ocak ayı için yeni sabit kıymet ve birikmiş amortisman değeri aşağıdaki gibi hesaplanır. Ocak ayı için aylık amortisman değeri yeni sabit kıymet değeri üzerinden hesaplanacaktır.

Ocak ayı Düz. Sabit Kıymet : 129.094,00 + ((129.094,00 \* 4,13616) / 100) = 134.433,33

Ocak ayı Düz. Birik Amort : 51.637, 6 + ((51.637, 6 \* 4,13616) / 100) = 53.773,33

![](../../_assets/5aefad3755ba1874afd2.png)

Demirbaş Bilgi Kartı ekranında enflasyon muhasebesi başlatıldığı ay için gridde Düzeltme alanı E olarak görülecektir. Ayrıca yine gridde enflasyon düzeltmesi yapılan aylar için Değerleme Durumu alanında Enflasyon Düzeltmesi bilgisi yer alacaktır.
Enflasyon muhasebesi devam ettiği sürece ilerleyen aylar için yine benzer şekilde amortisman ayrılacak ay/dönem endeksi ile bir önceki ay/dönem endeksi dikkate alınarak hesaplamalar yapılacaktır.
Değerleme ve Amortisman Raporu ekranından da düzeltilmiş ve düzeltmemiş değerler ile yine bunlar arasındaki fark değerleri izlenebilir.

![](../../_assets/30da036f86c5260b6460.png)

### Enflasyon Muhasebesi Devir Bilgileri İptali

Enflasyon muhasebesine başlama ile atılan kayıtların silinmesi istendiğinde bu ekran ile istenen kayıtlar iptal edilebilir.

![](../../_assets/f3c1f29d5110d3efa0fb.png)

## Reel Olmayan Finansman Maliyetleri

Stokların, satılan malın ve maddi duran varlıkların maliyet bedeline ve mali duran varlıkların alış bedeline intikal ettirilen finansman maliyeti, faiz ve kur farkı gibi maliyetler olup, öncelikle içerdikleri enflasyon payından arındırılıp sonra kalan değerleri üzerinden düzeltmeye tabi tutulmalıdır. Alış ve maliyet bedellerine intikal ettirilen bu finansman maliyetlerinin içerdiği enflasyon payı, Reel Olmayan Finansman Maliyeti olarak adlandırılır.

**Örnek:** 3.000.000 TL sına alınmış bir maddi duran varlık için, bir sonraki dönemde, %30 kredi faizi karşılığı olan 900.000 TL finansman maliyeti olarak aktifleştirilmiştir. Maddi duran varlığın değeri; 3.900.000 TL 'sına yükselmiştir. Ancak bu dönemde enflasyon %10 oranında gerçekleşmiştir. Söz konusu finansman maliyetinin %10 enflasyon payını içeren kısmı, reel olmayan finansman maliyetidir.
Reel olmayan finansman maliyeti = 0,1/0,3 \* 900.000 = 300.000
Finansman maliyeti reel kısmı = 900.000 – 300.000 = 600.000
Maddi duran varlık reel değeri = 3.000.000 + 600.000 = 3.600.000
Bu dönemin sonrasında düzeltmeye tabi tutulacak olan maddi duran varlık bedeli 3.600.000 olmalıdır. VUK'na göre reel olmayan finansman maliyeti ihtiva eden iktisadi kıymetler; Stoklar, Maddi duran varlıklar, Mali duran varlıklar ve Özel tükenmeye tabi varlıklardır. Bu kalemlerde aktifleştirilmiş finansman maliyeti bulunuyorsa düzeltme işlemlerinden önce reel olmayan kısımların arındırılmasına dikkat edilmelidir.
Örneğimizde, aktifleştirilen finansman maliyetinin kredi faiz oranı (%30) biliniyordu. Ancak farklı faiz oranları ile birçok kredi kullanılmış ve bunlar zaman içinde birçok farklı kalemler üzerinde aktifleştirmiş ise, finansman maliyetlerinin reel olmayan kısımlarını arındırma işlemi için faiz oranı belirlenmesi güçleşir. Bu durumda mükellefler; reel olmayan finansman maliyetini, toplam finansman maliyetlerine, ilgili döneme ait TEFE artış oranının dönem ortalama ticari kredi faiz oranına bölünmesi suretiyle belirlenen oranı uygulayarak da tespit edebilirler. Söz konusu bu ortalama ticari kredi faiz oranları Maliye Bakanlığı'nca açıklanır.
Bu açıklama dikkate alınarak,
Reel olmayan finansman maliyeti = Enflasyon oranı / Ortalama ticari kredi faiz oranı \* Finansman maliyeti şeklinde hesaplanabilir.

**Dikkat;** Netsis Enflasyon Muhasebesinde, Reel olmayan finansman maliyeti arındırması için otomatik bir yöntem bulunmamaktadır. Aktifleştirme işlemi sırasında, yukarıda verilen oranlama yapılarak finansman maliyetinin reel olan kısmı ayrıştırılıp ilgili hesaba (stok, sabit kıymet vb.) yazılmalı, reel olmayan kısmı ise muhasebede finansman giderine yazılmalıdır. Stok ve sabit kıymet gibi modüllerde de aynı mantıkla reel finansman maliyeti girilmelidir. Reel ve reel olmayan finansman maliyetleri tüm modüllerde TL tutarlara kaydedilmelidir.
