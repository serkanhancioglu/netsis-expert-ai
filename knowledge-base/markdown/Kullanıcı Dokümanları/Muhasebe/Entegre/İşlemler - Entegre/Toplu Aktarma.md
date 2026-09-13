---
title: "Toplu Aktarma"
page_id: "24741033"
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
  - "Toplu Aktarma"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Entegre / İşlemler / Entegre / Toplu Aktarma"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTNmNTMxNDUwLTk0OGMtNDA1Ni04ZjUxLWQxZDQ0M2QzMmFlMSZsaW5rPTg4MGU1NzBkLTRmMWUtNGJjNy05ZmNkLWQyZDEyMjc0OGMyNSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=3f531450-948c-4056-8f51-d1d443d32ae1&link=880e570d-4f1e-4bc7-9fcd-d2d122748c25&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "toplu-aktarma_41164278_24741033.html"
source_version: "2022-09-22T13:13:02.090+03:00"
source_bytes: 152484
fetched_at: "2026-09-13T04:14:48+00:00"
generator: "netsis-scraper 1.0.0"
---
# Toplu Aktarma

Toplu Aktarma, Muhasebe Bölümü'nde, "İşlemler/Entegre" menüsünün altında yer alır. Toplu Aktarma, Entegrasyon modülündeki bir diğer aktarma seçeneğidir. Toplu aktarmanın kullanılması için günlük muhasebeleştirme yapılması gerekir. Entegrasyonda oluşan tüm kayıtlar, tarihlerine bakılmaksızın toplu aktarmanın yapıldığı güne aktarılır.

Toplu Aktarma ekranı; Aktarma Sorgulama ve İleri Kısıt Tanımlama olmak üzere iki sekmeden oluşur.

**Aktarma Sorgulama**

![](../../../../_assets/a9003e4fbb6d562d14d8.png)

Toplu Aktarma ekranı Aktarma Sorgulama sekmesinde yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| Toplu Aktarma Ekranı |  |
| --- | --- |
| Başlangıç Fiş No | Muhasebe → Kayıt → [Yevmiye Fiş Girişi](<../../Muhasebe Modülü/Kayıt - Muhasebe/Yevmiye Fiş Girişi/index.md>) kayıtlarında, son girilen fişten sonra fiş numarası aralığının verilmesi, birkaç fiş ayırıp daha sonraki bir numaradan başlanarak fiş oluşturulması için, aktarmanın yapılacağı ilk fiş numarasının girildiği alandır. Burada belirlenen fiş numarasından başlayarak aktarım yapılır. Herhangi bir başlangıç fiş numarası girilmesi istenmediğinde ise, klavyede bulunan \<tab\> tuşu ile ilerlenerek boş bırakılır. |
| Sıra No Aralığı | Entegrasyonda oluşan tüm kayıtların program tarafından atanmış sıra numaraları mevcuttur. Kayıtların "Muhasebe" modülüne aktarımı sırasında “Sıra No” aralığı verilmesi şartıyla, sadece istenen kayıt adedinin muhasebeye aktarılmasını sağlayan alandır. **Örneğin,** tek bir fatura veya birkaç fatura kaydının muhasebeye aktarımı istendiğinde, entegrasyondaki faturaya ait kayıtların sıra numaralarına bakılır. Aktarılması istenen ilk bilgi satırının sıra numarası ve aktarılması istenen son bilgi satırının sıra numaraları alınarak bu bölüme girilir. Program, verilen numara aralığına giren kayıtları "Muhasebe" modülüne aktarır. |
| İşlem Tipi | Entegrasyon → Kayıt → "İşlem Tipi Tanımlama" bölümünden işlem tipleri tanımlanarak, modüllerden işlem tiplerine göre kayıtlar oluşturulmuşsa, belli bir işlem tipi girilerek, entegrasyondan sadece bu işlem tipine sahip kayıtların muhasebeye aktarılması sağlanır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, işlem tipleri arasından seçim yapılır. Herhangi bir işlem tipi kısıtı verilmesi istenmediğinde, klavyede yer alan \<tab\> tuşu ile ilerlenerek boş bırakılır. |
| Kasa Kodu | Çok kasalı çalışan firmalarda, kasa fişlerinin ayrı ayrı muhasebeleştirilmesi için aktarılacak kasa kodunun girildiği alandır. Daha sonra diğer kasaların aktarım işleminin ayrı ayrı çalıştırılması gerekir. "Kasa Kodu" alanı boş bırakılarak klavyede yer alan \<tab\> tuşu ile ilerlendiğinde, program tarafından tüm kasalar arka arkaya muhasebeye entegre edilir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, kasa kodları arasından seçim yapılır. |
| Kullanıcı No | Belli bir kullanıcı tarafından kaydedilen fişlerin aktarılması için kullanıcı numarası girilen alandır. Klavyede yer alan \<tab\> tuşu ile boş bırakılarak ilerlendiğinde, kullanıcı ayrımı yapılmaksızın tüm kayıtlar aktarılır. Bu durumda diğer kullanıcı kayıtlarının aktarılması için tekrar aktarma işleminin çalıştırılması gerekir. "Kullanıcı No" alanın aktif hale gelmesi için; Yardımcı Programlar → Kayıt → Şirket-Şube Parametreleri → “Entegre Kullanıcı No. Sorulsun” parametresinin işaretlenmesi gerekir. |
| Evrak Bazında Aktarım Yapılsın | Entegrasyon mahsup fişlerinde bulunan kayıtların, muhasebeye tek tek yevmiye fişi olarak aktarılması için kullanılan seçenektir. İşaretlendiğinde, her bir işlem muhasebeye ayrı bir fiş olarak aktarılır. İşaretlenmediği zaman, mahsup fişindeki bilgilerin girilecek tarih aralığındaki kayıtları, muhasebeye tek fiş olarak aktarılır. |
| Evrak Tarihi Yevmiye Tarihi Olarak Kullanılsın | “Evrak Bazında Aktarım Yapılsın" seçeneğinin işaretlenmesi ile aktif hale gelen seçenektir. Genelde, "Toplu Aktarma" yapıldığında muhasebeye aktarılacak bilgiler için tek bir yevmiye tarihi verilir. Yani 01/09/2003 ile 10/09/2003 tarih aralığı verildiğinde bile, sadece tek bir yevmiye tarihi sorgulanır ve bu örneğe göre 10 günlük bilginin aktarıldığı fişe aynı yevmiye tarihi aktarılır. Evrak bazında aktarım yapıldığında, her bir işlem muhasebeye ayrı bir fiş olarak aktarılır. İşaretlendiğinde, toplu aktarma sırasında sorgulanan yevmiye tarihi dikkate alınmaz ve entegrasyon kayıtlarındaki evrak tarihi muhasebe fişlerine yevmiye tarihi olarak aktarılır. |
| Gün Bazında Aktarma Yapılsın | Entegrasyonda yedi adet mahsup bölümünde bulunan kayıtların gün bazında muhasebeye aktarımını sağlayan seçenektir. Bu seçeneğin işaretlenmesi durumunda program, sistem tarihine bakarak o ay içerisinde yapılan 1 ve 2 numaralı kayıt tipindeki tüm işlemleri "Muhasebe" modülüne gün bazında aktarır. |
| Muhasebe Fiş Basımı Yapılsın | Entegrasyondan aktarma işlemi yapıldıktan sonra fiş basım ekranının görüntülenmesi ve "Dizayn" modülünden oluşturulan dizayna göre yevmiye fiş basımının yapılması için kullanılan seçenektir. |
| Kullanıcı Bazında Aktarım Yapılsın | Her bir kullanıcı numarasına ait kayıtlar için ayrı yevmiye fişinin oluşturulmasını sağlayan seçenektir. |
| Kasa Tahsilat/Tediye Aktarımları Detaylı Yapılsın | Toplu aktarım sırasında, kasa tahsilat/tediye aktarımlarının detaylı yapılması için kullanılan seçenektir. |
| Gün Bazı Aktarımda Farklı Kasa Kodlu Kayıtlar Aynı Fişe Atılsın | Gün bazlı aktarımlarda, farklı kasa kodlu kayıtların aynı fişe aktarılması için kullanılan seçenektir. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilgilerin onaylanmasını sağlayan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
| ![](../../../../_assets/67af647263b81e237bf2.jpg) Hepsi | Ekranda yer alan seçeneklerin hepsinin işaretlenmesi için kullanılan butondur. |
| ![](../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | "Aktarma Sorgulama" sekmesinde verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. "Toplu Aktarma" için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki toplu aktarma işleminde kullanılmak üzere saklanır. |

**İleri Kısıt Tanımlama**

İleri Kısıt Tanımlama, listede bulunan alanlar ile ilgili kısıtlamaların yapılmasını sağlayan sekmedir. Muhasebeye aktarma işlemi istenen dönemlerde, günlük, haftalık, aylık olarak çalıştırılabilir. Aktarma yapılmadan, ön muhasebe kayıtlarına istendiği kadar devam edilebilir. Girilen tarih aralıklarına göre sadece belli bir dönemin kayıtları aktarılabilir. Sadece, aktarılan kayıtlar entegrasyon bölümlerinden silinir. Diğerleri yine entegrasyonda izlenebilir. Aktarma sırasında "Entegrasyon Kayıtları" bölümlerinden her biri için muhasebede (Kasa Tahsil, Tediye, Müşteri/ Satıcı Borç, Alacak, Dekont) ayrı ayrı fiş kaydı düzenlenir. "Şube Uygulaması" varsa, şubelerin entegrasyon aktarım işlemi, ilgili şubenin içine girilerek şube bazında yapılması gerekir.

**![](../../../../_assets/2a330a5749e4f21b5011.png)**

Toplu Aktarma ekranı İleri Kısıt Tanımlama sekmesinde yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| Toplu Aktarma Ekranı |  |
| --- | --- |
| Saha Adı | Kısıt sekmesine ![](../../../../_assets/b549ef7a3208cdf4829b.png) tıklanması ile görüntülenir.Seçenekli Aktarma işleminde baz alınacak saha adı için kısıt verilen alandır. İlgili hücre üzerinde iken klavyede yer alan **Boşluk Çubuğuna** basılarak aktif hale gelen aşağı ok butonu, kısıt verilmesi istenen sahalara ulaşılmasını sağlar. ![](../../../../_assets/8c0ed831ced3941a3d3f.png) |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Butona tıklanması ile birlikte "Bu işlem ile entegrasyonda oluşan tüm kayıtlar, tarihlerine bakılmaksızın toplu aktarımın yapıldığı güne aktarılır. Devam edilsin mi" şeklinde bir onay sorusu ekran gelir. Bu sorgulamada "Hayır" butonuna tıklandığında aktarma işlemi kesilir. "Evet" butonuna tıklanması ile aktarma işlemi başlar. ![](../../../../_assets/6238d3ad59afa58e474c.png) |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
| ![](../../../../_assets/e3223333470668512f5f.jpg) Oku | Daha önceden saklanan kısıtların aynısının ekrana getirilmesini sağlayan butondur. **Oku** butonu ile sadece "en son saklanan kısıtlar" ekrana getirilir. |
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | "İleri Kısıt Tanımlama" sekmesinde verilen kısıtlar ve işaretlenen tüm seçeneklerin saklanması için kullanılan butondur. "Toplu Aktarma" için kısıt verildikten sonra bu butona basıldığında, onaylama ekranı görüntülenir. Onaylama ekranında "Evet" butonuna basılması ile belirlenen kısıtlar bir sonraki toplu aktarma işleminde kullanılmak üzere saklanır. |

Toplu Aktarmada, Seçenekli Aktarmada yönteminde olduğu gibi tarih aralıklarını belirlemek, entegrasyon bölümlerinden bazılarının aktarılmasını, bazılarının aktarılmamasını sağlamak mümkün değildir. Bu nedenle, dikkatli kullanılması gereken bir aktarma işlemidir.

Entegrasyonda bulunan kayıtların, "Seçenekli" veya "Toplu Aktarma" işlemleri ile aktarımı sonrası oluşan fişlerde yuvarlamadan kaynaklanan farklar program tarafından kapatılır.

[Muhasebe Parametreleri](<../../Muhasebe Modülü/Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/Muhasebe Modülü Tanımlamaları/Muhasebe Parametreleri - Muhasebe.md>) bölümünde yuvarlama kapatma parametreleri tanımlanmışsa, aktarım sırasında program tarafından fişlerde yuvarlama işlemi yapılır. Yuvarlama bilgileri, aktarım tamamlandıktan hemen sonra çıkan "Fiş Bazında Yuvarlama Farkı Sonuç Raporunda" listelenir.

Fiş Bazında Yuvarlama Farkı Sonuç Raporu ile, yuvarlama işleminin yapıldığı kayıtlar, yuvarlama farkı olduğu halde bir hatadan dolayı farkın kapatılamadığı kayıtlar, ya da fark tutarının parametrelerde belirtilen maksimum farktan büyük olmasından dolayı yuvarlama yapılmayan kayıtlar izlenebilir.
