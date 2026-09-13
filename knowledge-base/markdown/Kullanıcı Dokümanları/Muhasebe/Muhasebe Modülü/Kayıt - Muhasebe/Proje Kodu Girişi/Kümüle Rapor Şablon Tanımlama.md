---
title: "Kümüle Rapor Şablon Tanımlama"
page_id: "24740456"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Muhasebe"
  - "Muhasebe Modülü"
  - "Kayıt / Muhasebe"
  - "Proje Kodu Girişi"
  - "Kümüle Rapor Şablon Tanımlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / Kayıt / Muhasebe / Proje Kodu Girişi / Kümüle Rapor Şablon Tanımlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWY4ZDYwNWJlLTJjYjAtNDU5NS1hMDVjLWUxMDVlN2M0MDRjYiZsaW5rPTliNjg3OGI0LWNmMzUtNDFkZS04NDJhLTM3OTFhMGJjMzVhYSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=f8d605be-2cb0-4595-a05c-e105e7c404cb&link=9b6878b4-cf35-41de-842a-3791a0bc35aa&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "kumule-rapor-sablon-tanimlama_38994023_24740456.html"
source_version: "2022-09-27T14:29:17.620+03:00"
source_bytes: 326726
fetched_at: "2026-09-13T04:12:54+00:00"
generator: "netsis-scraper 1.0.0"
---
# Kümüle Rapor Şablon Tanımlama

Kümüle Rapor Şablon Tanımlama, Muhasebe Bölümü'nde, "Kayıt/Muhasebe Modülü" menüsünün altında yer alır. "Proje Kümüle Rapor" alınması için, öncelikle "Kümüle Rapor Şablon Tanımlama" bölümünden hangi alanlara ve kısıtlamalara göre rapor alınacağının tanımlanması gerekir. Şablon tanımlandıktan sonra, "[Proje Kümüle Rapor](<../../Raporlar - Muhasebe/Proje Takip Raporları/Proje Kümüle Rapor.md>)" bölümünde ilgili şablon sorgulanır ve rapor, hazırlanan şablona göre alınır.

Kümüle Rapor Şablon Tanımlama ekranı; Genel Tanımlamalar, Detay Tanımlamalar ve ../../.... Tarihli Rapor olmak üzere üç sekmeden oluşur.

**Genel Tanımlamalar**

![](../../../../../_assets/e88e6bbbd001cae406f1.png)

Kümüle Rapor Şablon Tanımlama ekranı Genel Tanımlamalar sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Kümüle Rapor Şablon Tanımlama Ekranı |  |
| --- | --- |
| Rapor Kodu | Hazırlanacak şablon kodunun girildiği alandır. "Proje Kümüle Rapor" bölümünde bu alanda tanımlanan kod sorgulanır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, rapor kodlarına ulaşılır. |
| Açıklama | Hazırlanacak şablon için açıklama bilgisi girilen alandır. Girilen açıklama, "Proje Kümüle Rapor" alındığında başlık olarak izlenir. |
| İşletmelerde Ortak | Tanımlanacak rapor şablonunun geçerli olacağı işletmenin belirlendiği alandır. Rapor şablonunun tüm işletmelerde görülmesi istendiğinde -1 değerinin girilmesi gerekir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, işletme kodları arasından seçim yapılır. |
| Şubelerde Ortak | Tanımlanacak rapor şablonunun geçerli olacağı şubenin belirlendiği alandır. Rapor şablonunun tüm şubelerde görülmesi istendiğinde -1 değerinin girilmesi gerekir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, şube kodları arasından seçim yapılır. |
| Hariç Tutulacak Şube Tanımlamaları | Şubelerde ortak alanına -1 değeri girildiğinde aktif hale gelir. Şablonun görülmesi istenmeyen şubelerin belirlenerek, hariç tutulmasını sağlar. |
| Hazırlık Çalıştır | Hazırlanan şablona göre raporun güncel değerler ile alınması için kullanılan butondur. En son çalıştırılan hazırlık değerleri dikkate alınarak raporun alınmasını sağlar. |
| Çoklu Yıl Desteği | Rapor alınacak proje, önceden devam eden bir proje ise (ilgili projeye ait geçmiş yıl veri tabanlarında kayıt varsa) bu bilgilerin raporlanması için işaretlenmesi gereken seçenektir. İşaretlenmediğinde, projeye ait kayıtlar sadece içinde bulunulan şirketten aktarılır. |
| Grafik Seçim | Şablon hazırlandıktan sonra Muhasebe → Rapor → "[Proje Takip Raporları](<../../Raporlar - Muhasebe/Proje Takip Raporları/index.md>)" bölümünden rapor alınacağı gibi, şablon hazırlama ekranından da "grafik" olarak rapor izlenir. Pasta Grafiği ve Çubuk Grafiği olmak üzere iki farklı grafik seçeneği vardır: **Pasta Grafiği;** izlenecek raporun, "Pasta Grafiği" şeklinde görüntülenmesi için işaretlenmesi gereken seçenektir. **Çubuk Grafiği;** izlenecek raporun, Çubuk Grafiği şeklinde görüntülenmesi için işaretlenmesi gereken seçenektir. |
| Proje Kısıtı Ekle | Alanın sağ tarafında yer alan üç nokta ... butonu ile, "Kısıt Girişi" ekranı görüntülenir. Rapor alınması istenen proje koduna ait kısıt verilerek istenen alana göre sıralama yapılmasını sağlar. ![](../../../../../_assets/2158eb86709c35ee6bc9.png) |

**Detay Tanımlamalar**

Şablonu hazırlanacak raporda çıkması istenen kolonların seçildiği sekmedir. Raporda hangi alanlar ile ilgili rapor alınması isteniyorsa, şablona alanın ait olduğu tablonun eklenmesi gerekir.

![](../../../../../_assets/109105222205afbefe63.png)

Kümüle Rapor Şablon Tanımlama ekranı Detay Tanımlamaları sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Kumüle Rapor Şablon Tanımlama Ekranı |  |
| --- | --- |
| Sıra No | Raporda listelenmesi istenen kolon için, program tarafından otomatik olarak atanan alandır. |
| Giriş/Çıkış | Raporu alınacak proje kodu ile ilgili listelenmesi istenen hareketler için seçim yapılan alandır. Giriş ve Çıkış olmak üzere iki seçenekten oluşur. Alanın sağ tarafında yer alan aşağı ok butonu ile seçim yapılır. |
| Detay Açıklama | “View Adı” alanında seçilen view’in raporda listelenirken görüntülenmesi istenen başlığın girildiği alandır. |
| Tip | Raporu alınacak alanların, getirilmesi istenen yerin seçildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile; Temelset, Demirbaş ve Personel seçenekleri arasından seçim yapılır. **Örneğin,** raporda," Ticari Paket" ile ilgili alanların listelenmesi istendiğinde Temelset, "Personel Paketi" ile ilgili alanların listelenmesi istendiğinde Personel, "Demirbaş" ile ilgili alanların listelenmesi istendiğinde ise Demirbaş seçeneği seçilir. Tip alanında "Personel" ve "Demirbaş" seçildiği zaman View Adı, Miktar, Tutar alanları aktif gelmez. Bilgiler, program tarafından özel olarak hazırlanan view’den aktarılır. |
| View Adı | İçinde bulunulan veri tabanına ait, proje kodu ile ilgili tüm view’lerin listelendiği alandır. Rapor alınacak view'in seçilmesini sağlar. Bu alanda, ilgili veritabanına ait tüm view’ler listelendiği için, kullanıcıların kendi hazırladıkları özel view’lerden de rapor alınabilir. Kullanıcının, özel hazırladığı view’e proje ile ilgili bilgileri aktarması için, “Proje_Kodu” şeklinde proje kodunun kolonunu da ilave etmesi gerekir. |
| Proje Kısıtı Ekle | "View Adı" alanında seçilen view ile ilgili kısıt verilen alandır. Alanın sağ tarafında yer alan üç nokta ... butonu ile, "Kısıt Girişi" ekranı görüntülenir. Rapor alınması istenen proje koduna ait kısıt verilerek istenen alana göre sıralama yapılmasını sağlar. ![](../../../../../_assets/2158eb86709c35ee6bc9.png) **Örneğin,** "View Adı" alanında "SIPATRA" seçilmişse, sipariş hareketleri ile ilgili bir rapor alınacağı anlamına gelir ve "Proje Kısıdı Ekle" alanında sipariş giriş hareketleri listelensin şeklinde kısıt verilebilir. "View Adı" alanında seçilen view ile ilgili kısıt verilen alandır. Alanın sağ tarafında yer alan üç nokta ... butonu ile, "Kısıt Girişi" ekranı görüntülenir. Rapor alınması istenen proje koduna ait kısıt verilerek istenen alana göre sıralama yapılmasını sağlar. ![](../../../../../_assets/2158eb86709c35ee6bc9.png) **Örneğin,** "View Adı" alanında "SIPATRA" seçilmişse, sipariş hareketleri ile ilgili bir rapor alınacağı anlamına gelir ve "Proje Kısıdı Ekle" alanında sipariş giriş hareketleri listelensin şeklinde kısıt verilebilir. |
| Miktar | Seçilen view ile ilgili miktar bakımından raporda listelenmesi istenen alanın seçilmesini sağlar. |
| Miktar Tahmin | Raporlanacak miktar değeri için, gerçekleşmesi düşünülen tahmini değerin girildiği alandır. Girilen tahmini miktar, raporda gerçekleşen miktar alanı ile karşılaştırılarak iki alanın farkı daha sonra raporda izlenebilir. **Örneğin,** rapor alırken ilgili projede tahmini ne kadar sipariş verileceği tanımlanarak, daha sonra raporda gerçekleşen rakam ile karşılaştırabilir. |
| Birim | Raporda listelenecek miktar alanının ölçü birimi cinsinden listelenmesini sağlayan alandır. |
| Tutar | Seçilen view ile ilgili tutar bakımından raporda listelenmesi istenen alanın seçilmesini sağlar. |
| Tutar Tahmin | Raporlanacak tutar değeri için, gerçekleşmesi düşünülen tahmini değerin girildiği alandır. Girilen tahmini tutar, raporda gerçekleşen tutar alanı ile karşılaştırılarak iki alanın farkı daha sonra raporda izlenebilir. **Örneğin,** rapor alırken ilgili projede tahmini ne kadar sipariş verileceği tanımlanarak, daha sonra raporda gerçekleşen rakam ile karşılaştırabilir. |
| Firma Döviz Tutarı | Seçilen view ile ilgili, raporda listelenmesi istenen döviz tutarı alanının belirlendiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile seçim yapılır. |
| Döviz Tutar Tahmin | Raporlanacak dövizli tutar değeri için, gerçekleşmesi düşünülen tahmini değerin girildiği alandır. Girilen tahmini dövizli tutar, raporda gerçekleşen dövizli tutar alanı ile karşılaştırılarak iki alanın farkı daha sonra raporda izlenebilir. **Örneğin,** rapor alırken ilgili projede tahmini ne kadar dövizli tutarda sipariş verileceği tanımlanarak, daha sonra raporda gerçekleşen değer ile karşılaştırabilir. |

**../../.... Tarihli Rapor**

Hazırlık çalıştırıldıktan sonra “Detay Tanımlamalar” sekmesinin yanına bir sekme daha eklenir. Bu sekmenin başlığına da hazırlığın yapıldığı tarih aktarılır. Hazırlık çalıştırıldıktan sonra gelen bu ekranda “Genel Tanımlamalar” sekmesindeki “Grafik Seçim” alanında yapılan seçime göre şablonu hazırlanan rapor; "Tutar", "Miktar" ya da "Firma Döviz Tutar" alanlarına göre "Çubuk Grafiği" yada "Pasta Grafiği" şeklinde görüntülenir.

![](../../../../../_assets/2f5d907c01ae704252d0.png)
