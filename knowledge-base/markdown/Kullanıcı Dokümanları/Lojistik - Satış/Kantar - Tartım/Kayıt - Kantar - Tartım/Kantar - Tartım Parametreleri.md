---
title: "Kantar - Tartım Parametreleri"
page_id: "22804226"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Kantar - Tartım"
  - "Kayıt / Kantar - Tartım"
  - "Kantar - Tartım Parametreleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Kantar - Tartım / Kayıt / Kantar - Tartım / Kantar - Tartım Parametreleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTU0NTMzZDhmLWJmMTUtNDY1OC04MWY3LTA3YzU3OGFmY2VjZSZsaW5rPWJhNzFjN2E0LWI2NTAtNDQwNi1hMzUxLWFiNTI1NzMwNDViZSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=54533d8f-bf15-4658-81f7-07c578afcece&link=ba71c7a4-b650-4406-a351-ab52573045be&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "kantar-tartim-parametreleri_28149502_22804226.html"
source_version: "2022-11-07T10:05:53.390+03:00"
source_bytes: 14867
fetched_at: "2026-09-13T04:06:55+00:00"
generator: "netsis-scraper 1.0.0"
---
# Kantar - Tartım Parametreleri

Kantar Tartım Lojistik-Satış Bölümü'nde, "Kayıt/Kantar-Tartım" menüsünün altında yer alır. Kantar Parametreleri ve Kantar İletişim Parametreleri olmak üzere iki sekmeden oluşur.

**Kantar Parametreleri**

Kantar Parametreleri sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Kantar - Tartım Parametreleri Ekranı |  |
| --- | --- |
| Kantar Parametreleri - Tartım Parametreleri |  |
| Kantar Kodu | Hangi kantara ait parametreler işaretlenecekse o kantara ait kod bilgisinin girildiği alandır. |
| Kantardan Miktar Okunsun | Kantarda yapılan tartımdan gelen miktar bilgisinin, programda tartım girişlerine aktarılarak kayıt oluşturulması istendiğinde işaretlenmesi gereken parametredir. Böylece, tartım miktarı kantardan okutulur. "Hareket Girişi Bölümünde", tartım miktarı manuel girilecekse bu parametrenin işaretlenmemesi gerekir. |
| Son Tartım Aktarılsın | Tartım girişlerinden son tartımın aktarılması için işaretlenmesi gereken parametredir. Bir araca ait ilk ve son tartım yapıldıktan sonra aynı plakalı araba için girilen ilk tartıma, ilgili aracın son tartım miktarının getirilmesini sağlar. Bu parametre işaretlendiğinde, "Hareket Girişi" ekranında “Son Tartım Aktarılsın” butonu aktif hale gelir. Bu butona basıldığında aktarım gerçekleşir. |
| Birinci Tartımda Fiş Basılsın | Kamyonların ilk tartımında tartım fişinin basılması istendiğinde işaretlenmesi gereken parametredir. Tartım fişi basımlarının yapılması istenmediğinde, bu parametrenin işaretlenmemesi gerekir. |
| İkinci Tartımda Fiş Basılsın | Kamyonun İkinci tartımında tartım fişinin basılması istendiğinde işaretlenmesi gereken parametredir. |
| Dara Aktarılsın | "Kamyon Sabit Bilgileri" bölümünden tanımlanan dara bilgisinin tartım fişlerine aktarılması istendiğinde işaretlenmesi gereken parametredir. Parametre işaretlendiğinde, "Hareket Girişi" ekranında “Dara İlk Tartıma Aktarılsın mı?” sorusu ekrana gelir ve onaylandığında, kamyonun darası "İlk Tartım Değerine" aktarılır. Girilen tartım ise, son tartım olarak kaydedilir. |
| Stok Bağlantısız Kantar Kullanımı | Bu parametrenin işaretlenmediği durumlarda, "Hareket Girişi" bölümünde son tartımın girilmesiyle "İrsaliye Tamamlama" ekranı açılır ve daha önce girilmiş olan stok bilgilerine göre irsaliye oluşturulur. Ancak, “Stok Bağlantısız Kantar Kullanımı” parametresinin işaretli olduğu durumlarda, "Hareket Girişi" sonucunda irsaliye oluşturulmaz. |
| Tartım Fişi Çıkışı (LPT1/LPT2) | Tartım basımlarının yazıcı portunun tercihinin girileceği sahadır. |
| Ek Açıklama Sorulsun | Ek açıklama alanlarının "Hareket Girişi" ekranında yer alması istendiğinde işaretlenmesi gereken parametredir. |
| Script İle Sayı Okunsun | Bu parametre işaretlendiğinde, "Kantar İletişim Parametreleri" bölümünde VBScript yazılması sağlanır. Kantar ile Logo Netsis arasındaki iletişim bu VBScript ile sağlanır. Döndürülecek değerin **"GeriDegerDondur**" değişkenine atanması gerekir. Aşağıdaki örnekte kantarın desteklediği **WeightLib.EW1613** kütüphanesi kullanılmıştır. Script yazılması için kantarın desteklediği örnekteki gibi bir kütüphanenin olması ve register edilmesi gerekir. **Örnek VBScript aşağıdaki şekildedir:**<br>dim Kantar<br>set Kantar = createobject("WeightLib.EW1613") Kantar.Baud = 9600 Kantar.ConversionUnit = 3 Kantar.PortName = "COM1" Kantar.SlaveAddress = "A"<br>Kantar.Enabled = True<br>GeriDegerDondur = Kantar.ConvertedValue<br>set Kantar = nothing |
| Fire Oranı Girilsin | Fire oranlarının girilmesi istendiğinde işaretlenmesi gereken alandır. |
| Kantar - Tartım Parametreleri Ekranı |  |
| İrsaliye/Sipariş/Fatura Parametreleri |  |
| Sipariş Entegre Yapılsın | Tartım kayıtlarının irsaliyeye aktarılırken sipariş bağlantısının da yapılması istendiğinde işaretlenmesi gereken parametredir. Eğer, alışta ve satışta önceden siparişler giriliyorsa ve bu siparişler karşılığında irsaliyelerin oluşturulması isteniyorsa bu parametrenin kullanılması gerekir. Parametrenin işaretlenmesi durumunda, aşağıdaki “Sipariş No Boş Geçilsin” parametresi işaretli değilse, irsaliyelerin oluşturulması sırasında yer alan "Sipariş Numarası" alanı boş bırakılamaz. |
| Sipariş No Boş Geçilsin | "Sipariş Entegre Yapılsın" parametresi işaretlenmişse tartım girişlerinde yer alan" Sipariş Numarası" alanının boş bırakılarak kayıt oluşturulması için işaretlenmesi gereken parametredir. Parametre işaretlenmezse, "Hareket Girişi" bölümünden yapılan kayıtlarda "Sipariş Numarası" alanı yine ekranda yer alır fakat boş bırakılarak işleme devam edilebilir. |
| İrsaliye Numarası Düzeltme | Program tarafından oluşturulan numaraların, kullanıcılar tarafından değiştirilmesi istendiğinde işaretlenmesi gereken parametredir. |
| İrsaliyede Miktar Düzeltilsin | Kullanıcıların kantardan gelen miktarı değiştirmesine izin vererek, irsaliyedeki "miktar" alanı üzerinde değişiklik yapılmasını sağlamak için işaretlenmesi gereken parametredir. Özellikle "kg" ile yapılan tartım ile, stok ölçü biriminin "adet" olduğu durumlarda, buçuklu miktarların oluşmasında irsaliyedeki "miktar" alanına müdahale etmek gerekebilir. Bu parametre işaretlendiğinde, girilen tartım ölçü birimi, stokların 1. ölçü birimine çevrilir. **Örneğin:** 100 kg olarak tartılan bir ürün çevrildiğinde 8.5 adet olur. Kullanıcılar istedikleri takdirde 8.5 adet ürünü 8 veya 9 olarak değiştirebilirler. Bu parametre işaretlendiğinde, yukarıda verilen örnekten de anlaşılacağı gibi tartım miktarı ile dağıtım miktarı (100,8.5) birbirine eşit değildir. Bu nedenle her iki miktar eşit olmasa da irsaliyenin kesilmesine izin verilir. |
| Farklı Cari/Mal Teslimatı Sorulsun | Kamyon bilgilerinde girilen cari kodun tartım işlemlerinde de sorgulanması istendiğinde kullanılması gereken parametredir. Tartım sonuçlarının (kullanıcı bazında) irsaliye kaydı şeklinde dağıtımının yapılması ve aynı zamanda cari ve stok kodunun sorgulanmadan geçilmesi isteniyorsa bu parametrenin işaretlenmesi gerekir. |
| Fatura Basımı Yapılsın | Çıkış olarak yapılan tartım kayıtlarında fatura basımlarının yapılması istendiğinde işaretlenmesi gereken parametredir. Girilen kayıtların irsaliye olarak kaydedilmesi ve fatura basımlarının başka bir bölümden basımının yapılması istendiğinde bu parametrenin işaretlenmesi gerekir. |
| Çoklu Seri | Tartımları oluşacak alış/satış irsaliyelerinde birden fazla seri numarası kullanılması istendiğinde işaretlenmesi gereken parametredir. Bu parametre işaretlendiğinde, aşağıda ön değer olarak kullanılacak "Seri No" alanı sorgulanır. Girilen seri numarası ön değer olarak "İrsaliye Numarası" olarak ekrana gelir. "Çoklu Seri" parametresi işaretliyse, ön değer olarak getirilen seri, kullanıcı tarafından değiştirilebilir. |
| Seri NO (A..Z) | Ön değer olarak kullanılacak seri numarasının girildiği alandır. Bu seri, irsaliye numaralarında kullanılır. Her irsaliye kaydında bu serinin boş olan son numarası, program tarafından ekrana getirilir. "Çoklu seri" uygulaması yoksa, ön değer seri numarası kullanıcı tarafından değiştirilemez. |
| Ambar Giriş Çıkış Fişi Oluşturulsun | İrsaliye, sipariş ve faturalarda ambar giriş çıkış fişlerinin oluşturulması için kullanılan parametredir. |
| Çıkış Yeri | Çıkış yerinin belirlendiği parametredir. Alanın sağ tarafında yer alan aşağı ok butonu ile çıkış yeri belirlenir. |

#### Kantar İletişim Parametreleri

Kantar İletişim Parametreleri ekranından sorgulanan parametreler teknik içerikli olup kantar ile program arasındaki bağlantılarda kullanılır. Ekrandaki alanlar teknik ekip ve Logo Netsis bayi elemanları tarafından düzenlenir. Kullanıcılar tarafından bu alanlara girilen bilgiler değiştirilmemelidir.
