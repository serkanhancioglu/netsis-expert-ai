---
title: "Seçenekli Aktarma"
page_id: "24741017"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Muhasebe"
  - "Entegre"
  - "İşlemler / Entegre"
  - "Seçenekli Aktarma"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Entegre / İşlemler / Entegre / Seçenekli Aktarma"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTkzMjM4OGY2LTc1OTYtNDNhYS1hNjJhLTEwYWIxZjZjMmQ4MCZsaW5rPTQ4MTcyNjliLTIzYzEtNDkzMi05NDFiLTRkY2EyNjQzYzMxNSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=932388f6-7596-43aa-a62a-10ab1f6c2d80&link=4817269b-23c1-4932-941b-4dca2643c315&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "secenekli-aktarma_24741030_24741017.html"
source_version: "2022-11-11T15:25:01.967+03:00"
source_bytes: 253363
fetched_at: "2026-09-13T04:14:47+00:00"
generator: "netsis-scraper 1.0.0"
---
# Seçenekli Aktarma

Seçenekli Aktarma, Muhasebe Bölümü'nde, "İşlemler/Entegre" menüsünün altında yer alır. Seçenekli Aktarma, Entegrasyondaki bilgilerin aktarılmasında, aktarma işleminin birden fazla seçenekle yönlendirilmesini ve kullanıcının aktarılacak kayıtlar için kısıt vermesini sağlar. Seçenekli Aktarma ekranı; Aktarma Sorgulama, Tarih Aralık Belirleme, Şube Sorgulama ve İleri Kısıt Tanımlama sekmesinden oluşur.

**Aktarma Sorgulama**

Aktarma Sorgulama sekmesi, aktarım yapılacak kayıtlar için kısıt verilmesini sağlayan sekmedir.

![](../../../../_assets/2bd84bd3180d38088d8b.png)

Seçenekli Aktarma ekranı Aktarma Sorgulama sekmesi alanları ve içeriği bilgiler aşağıdaki şekildedir:

| Seçenekli Aktarma Ekranı |  |
| --- | --- |
| Başlangıç Fiş No | Muhasebe → Kayıt → Yevmiye Fiş Girişi kayıtlarında, son girilen fişten sonra fiş numarası aralığının verilmesi, birkaç fiş ayırıp daha sonraki bir numaradan başlanarak fiş oluşturulması için, aktarmanın yapılacağı ilk fiş numarasının girildiği alandır. Burada belirlenen fiş numarasından başlayarak aktarım yapılır. Herhangi bir başlangıç fiş numarası girilmesi istenmediğinde ise, klavyede bulunan \<tab\> tuşu ile ilerlenerek boş bırakılır. |
| Sıra No Aralığı | Entegrasyonda oluşan tüm kayıtların program tarafından atanmış sıra numaraları mevcuttur. Kayıtların "Muhasebe" modülüne aktarımı sırasında “Sıra No” aralığı verilmesi şartıyla, sadece istenen kayıt adedinin muhasebeye aktarılmasını sağlayan alandır. **Örneğin,** tek bir fatura veya birkaç fatura kaydının muhasebeye aktarımı istendiğinde, entegrasyondaki faturaya ait kayıtların sıra numaralarına bakılır. Aktarılması istenen ilk bilgi satırının sıra numarası ve aktarılması istenen son bilgi satırının sıra numaraları alınarak bu bölüme girilir. Program, verilen numara aralığına giren kayıtları "Muhasebe" modülüne aktarır. |
| İşlem Tipi | Entegrasyon → Kayıt → "İşlem Tipi Tanımlama" bölümünden işlem tipleri tanımlanarak, modüllerden işlem tiplerine göre kayıtlar oluşturulmuşsa, belli bir işlem tipi girilerek, entegrasyondan sadece bu işlem tipine sahip kayıtların muhasebeye aktarılması sağlanır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, işlem tipleri arasından seçim yapılır. Herhangi bir işlem tipi kısıtı verilmesi istenmediğinde, klavyede yer alan \<tab\> tuşu ile ilerlenerek boş bırakılır. |
| Kasa Kodu | Çok kasalı çalışan firmalarda, kasa fişlerinin ayrı ayrı muhasebeleştirilmesi için aktarılacak kasa kodunun girildiği alandır. Daha sonra diğer kasaların aktarım işleminin ayrı ayrı çalıştırılması gerekir. "Kasa Kodu" alanı boş bırakılarak klavyede yer alan \<tab\> tuşu ile ilerlendiğinde, program tarafından tüm kasalar arka arkaya muhasebeye entegre edilir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, kasa kodları arasından seçim yapılır. |
| Kullanıcı No | Belli bir kullanıcı tarafından kaydedilen fişlerin aktarılması için kullanıcı numarası girilen alandır. Klavyede yer alan \<tab\> tuşu ile boş bırakılarak ilerlendiğinde, kullanıcı ayrımı yapılmaksızın tüm kayıtlar aktarılır. Bu durumda diğer kullanıcı kayıtlarının aktarılması için tekrar aktarma işleminin çalıştırılması gerekir. "Kullanıcı No" alanın aktif hale gelmesi için; Yardımcı Programlar → Kayıt → Şirket-Şube Parametreleri → “Entegre Kullanıcı No. Sorulsun” parametresinin işaretlenmesi gerekir. |
| Evrak Bazında Aktarım Yapılsın | Entegrasyon mahsup fişlerinde bulunan kayıtların, muhasebeye tek tek yevmiye fişi olarak aktarılması için kullanılan seçenektir. İşaretlendiğinde, her bir işlem muhasebeye ayrı bir fiş olarak aktarılır. İşaretlenmediği zaman, mahsup fişindeki bilgilerin girilecek tarih aralığındaki kayıtları, muhasebeye tek fiş olarak aktarılır. |
| Evrak Tarihi Yevmiye Tarihi Olarak Kullanılsın | “Evrak Bazında Aktarım Yapılsın" seçeneğinin işaretlenmesi ile aktif hale gelen seçenektir. Genelde, "Seçenekli Aktarma" yapıldığında muhasebeye aktarılacak bilgiler için tek bir yevmiye tarihi verilir. Yani 01/09/2003 ile 10/09/2003 tarih aralığı verildiğinde bile, sadece tek bir yevmiye tarihi sorgulanır ve bu örneğe göre 10 günlük bilginin aktarıldığı fişe aynı yevmiye tarihi aktarılır. Evrak bazında aktarım yapıldığında, her bir işlem muhasebeye ayrı bir fiş olarak aktarılır. İşaretlendiğinde, seçenekli aktarma sırasında sorgulanan yevmiye tarihi dikkate alınmaz ve entegrasyon kayıtlarındaki evrak tarihi muhasebe fişlerine yevmiye tarihi olarak aktarılır. |
| Gün Bazında Aktarma Yapılsın | Entegrasyonda yedi adet mahsup bölümünde bulunan kayıtların gün bazında muhasebeye aktarımını sağlayan seçenektir. Bu seçeneğin işaretlenmesi durumunda program, sistem tarihine bakarak o ay içerisinde yapılan 1 ve 2 numaralı kayıt tipindeki tüm işlemleri "Muhasebe" modülüne gün bazında aktarır. Seçenek işaretlendikten sonra, “Tarih Aralığı Belirleme” bölümüne gelindiğinde, sadece “Başlangıç Tarihi” ve “Bitiş Tarihi” alanlarına müdahale edilebilir. “Yevmiye Tarihi” alanı pasif olarak ekrana gelir. Sistem tarihine göre tarih aralığının belirlenmesi gerekir. Girilen tarih aralığındaki ay kodlarının sistem tarihinin ay kodu ile aynı olması gerekir. **Örneğin,** sistem tarihi 06/06/2003 ise girilecek tarih aralığı 01/06/2003-30/06/2003 olabilir. Eğer sistem tarihi dışında farklı bir aya ait tarih aralığı girilecek olursa, program verilen tarih aralığının uymadığını “Fişteki Tarih ile Ay Kodu Uyumsuz” mesajıyla kullanıcıya bildirir ve aktarım yapılmaz. "Gün Bazında Aktarma Yapılsın" seçeneğinin aktif hale gelmesi için, “Evrak Bazında Aktarma Yapılsın” seçeneğinin işaretlenmemesi gerekir. |
| Muhasebe Fiş Basımı Yapılsın | Entegrasyondan aktarma işlemi yapıldıktan sonra fiş basım ekranının görüntülenmesi ve "Dizayn" modülünden oluşturulan dizayna göre yevmiye fiş basımının yapılması için kullanılan seçenektir. |
| Kullanıcı Bazında Aktarım Yapılsın | Her bir kullanıcı numarasına ait kayıtlar için ayrı yevmiye fişinin oluşturulmasını sağlayan seçenektir. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilgilerin onaylanmasını sağlayan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
| ![](../../../../_assets/67af647263b81e237bf2.jpg) Hepsi | Ekranda yer alan seçeneklerin hepsinin işaretlenmesi için kullanılan butondur. |
| ![](../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | "Aktarma Sorgulama" sekmesinde verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. "Seçenekli Aktarma" için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki seçenekli aktarma işleminde kullanılmak üzere saklanır. |

**Tarih Aralık Belirleme**

Tarih Aralık Belirleme, "Entegrasyon Kayıtlarında" bulunan yedi adet mahsup fişinden aktarılması istenen fiş/fişlerin seçilmesini tarih aralığı belirlenmesini sağlayan sekmedir.

![](../../../../_assets/a26b68c964ef76ee582c.png)

Seçenekli Aktarma ekranı Tarih Aralık Belirleme sekmesinde yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| Seçenekli Aktarma Ekranı |  |
| --- | --- |
| Aktar | Entegrasyonda fiş isimlerinin yanında bulunan "Aktar" seçeneğinin işaretlenmesi ile, ilgili mahsup fişinin muhasebe aktarılması sağlanır. Herhangi bir fişin "Aktar" seçeneği işaretlenmediği zaman bu fiş muhasebeye aktarılmaz. Dolayısıyla, entegrasyondan muhasebeye aktarılması istenilen fişlerin “Aktar” seçeneklerinin işaretlenmesi gerekir. |
| Başlangıç Tarihi | Entegrasyonda bulunan ve aktarılması istenen kayıtlar için başlangıç tarihi girilen alandır. Entegrasyonda, bu tarihten daha küçük tarihli kayıtlar varsa, küçük tarihli kayıtlar aktarılmaz. Girilen tarih ve bu tarihten büyük tarihli kayıtlar muhasebeye aktarılır. |
| Bitiş Tarihi | Entegrasyonda bulunan ve aktarılması istenen kayıtlar için girilen sınır tarihtir. Entegrasyonda, bu tarihten büyük tarihe sahip kayıtlar muhasebeye aktarılmaz. |
| Yevmiye Tarihi | Verilen kısıtlara uygun olarak muhasebede oluşacak yevmiye fişleri için girilen tarihtir. Oluşturulan yevmiye fişlerine, girilen tarih atanır. "Seçenekli Aktarma" işlemi ile aktarılan yedi adet mahsup için yine muhasebede yedi adet yevmiye fişi oluşturulur. Dolayısıyla, girilen tarih aralığı 1 günden daha fazla tarih içeriyorsa, entegrasyonda bu tarih aralığındaki ve aynı fişteki kayıtlar için birer "Yevmiye Fişi" oluşturulur. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilgilerin onaylanmasını sağlayan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
| ![](../../../../_assets/67af647263b81e237bf2.jpg) Hepsi | Ekranda yer alan seçeneklerin hepsinin işaretlenmesi için kullanılan butondur. |
| ![](../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | "Tarih Aralık Belirleme" sekmesinde verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. "Seçenekli Aktarma" için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki seçenekli aktarma işleminde kullanılmak üzere saklanır. |

**Şube Sorgulama**

**![](../../../../_assets/98051ece6888038c45b4.png)**

Seçenekli Aktarma ekranı Şube Sorgulama sekmesinde yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| Seçenekli Aktarma Ekranı |  |
| --- | --- |
| ![](../../../../_assets/791c70a62e1a8ade02a1.png) Hepsini Seç | Ekranda yer alan seçeneklerin hepsinin işaretlenmesi için kullanılan butondur. |
| ![](../../../../_assets/76e42b0269d9532b9a8d.png) Hepsini Kaldır | Ekranda tamamı işaretlenen seçeneklerin hepsinin işaretinin kaldırılması için kullanılan butondur. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg)Tamam | Girilen bilgilerin onaylanmasını sağlayan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
| ![](../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur.<br>**Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | "Tarih Aralık Belirleme" sekmesinde verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. "Seçenekli Aktarma" için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki seçenekli aktarma işleminde kullanılmak üzere saklanır. |

**İleri Kısıt Tanımlama**

İleri Kısıt Tanımlama, listede bulunan alanlar ile ilgili kısıtlamaların yapılmasını sağlayan sekmedir. Muhasebeye aktarma işlemi istenen dönemlerde, günlük, haftalık, aylık olarak çalıştırılabilir. Aktarma yapılmadan, ön muhasebe kayıtlarına istendiği kadar devam edilebilir. Girilen tarih aralıklarına göre sadece belli bir dönemin kayıtları aktarılabilir. Sadece, aktarılan kayıtlar entegrasyon bölümlerinden silinir. Diğerleri yine entegrasyonda izlenebilir. Aktarma sırasında "Entegrasyon Kayıtları" bölümlerinden her biri için muhasebede (Kasa Tahsil, Tediye, Müşteri/ Satıcı Borç, Alacak, Dekont) ayrı ayrı fiş kaydı düzenlenir. "Şube Uygulaması" varsa, şubelerin entegrasyon aktarım işlemi, ilgili şubenin içine girilerek şube bazında yapılması gerekir.

![](../../../../_assets/e4a426b4e890fac4b746.png)

Seçenekli Aktarma ekranı İleri Kısıt Tanımlama sekmesinde yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| Seçenekli Aktarma Ekranı |  |
| --- | --- |
| Saha Adı | Kısıt sekmesine ![](../../../../_assets/b549ef7a3208cdf4829b.png) tıklanması ile görüntülenir. Seçenekli Aktarma işleminde baz alınacak saha adı için kısıt verilen alandır. İlgili hücre üzerinde iken klavyede yer alan **Boşluk Çubuğuna** basılarak aktif hale gelen aşağı ok butonu, kısıt verilmesi istenen sahalara ulaşılmasını sağlar. ![](../../../../_assets/e7224de9115c5b4c6164.png) |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Butona tıklanması ile birlikte "Seçenekli Aktarma İşlemi Yapılacaktır. Emin Misiniz?" şeklinde bir onay sorusu ekran gelir. Bu sorgulamada "Hayır" butonuna tıklandığında aktarma işlemi kesilir. "Evet" butonuna tıklanması ile aktarma işlemi başlar. ![](../../../../_assets/1e868482d79f12d71f4b.png) |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
| ![](../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | "İleri Kısıt Tanımlama" sekmesinde verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. "Seçenekli Aktarma" için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki seçenekli aktarma işleminde kullanılmak üzere saklanır. |

"Seçenekli Aktarım" sonrası oluşan fiş numaraları bilgi olarak aktarım referans numarası ile birlikte gösterilir. Aktarılacak kayıtlarda "Muhasebe Kodu" olmayan kayıtların bulunduğu durumlarda program işlemi keserek entegrasyonun devam etmesine izin vermez. Özellikle 5 numaralı kayıt tipi olan bölümlerin entegrasyonunda, program hesap kodu hatası vererek entegrasyonun aktarım işlemini keser. Muhasebede kayıt tipi 1 ve 2 olanlar dışında, 3,4 ve 5 tipli kayıtlar muhasebeye aktarılmaz. Entegrasyon kayıtlarında 3,4,5 tipli kayıtlar varsa, aktarım sırasında “Geçersiz Kayıt Tipine Rastlandı” uyarısı ile kullanıcı bilgilendirilir. Raporlar alındıktan sonra, gereksiz kayıt tiplerinin silinmesi için, Seçenekli ya da Toplu Aktarım öncesi "[Entegrasyon Kontrolü](<Entegrasyon Kontrolü.md>)" bölümünün çalıştırılması gerekir.
