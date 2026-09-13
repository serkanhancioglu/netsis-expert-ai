---
title: "İthalat Kapatma"
page_id: "22805889"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Dekont"
  - "Kayıt / Dekont"
  - "İthalat/İhracat İşlemleri"
  - "İthalat Kapatma"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Dekont / Kayıt / Dekont / İthalat/İhracat İşlemleri / İthalat Kapatma"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWY2NDJiYzc3LWM3Y2ItNDM0OS05MGRiLTE0ZjRlZjkxZjYzNSZsaW5rPWU3ODBlMmRiLWZjOTQtNDYyNS1iYjE1LWY1M2ZiNzNlMmUxNyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=f642bc77-c7cb-4349-90db-14f4ef91f635&link=e780e2db-fc94-4625-bb15-f53fb73e2e17&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ithalat-kapatma_34230314_22805889.html"
source_version: "2022-11-30T17:00:28.857+03:00"
source_bytes: 312489
fetched_at: "2026-09-13T04:09:14+00:00"
generator: "netsis-scraper 1.0.0"
---
# İthalat Kapatma

İthalat Kapatma, Finans Bölümü'nde, "Kayıt/Dekont" menüsünün altında yer alır. İthalat Kapatma, ithalat kapatma işleminin yapıldığı bölümdür. İthalat Kapatma; [İthalat Ön Sorgulama](<İthalat Kapatma.md>), [İthalat Kapatma](<İthalat Kapatma.md>) ve [İthalat Parçalı Kapatma](<İthalat Kapatma.md>) olmak üzere üç sekmeden oluşur. İlk olarak, Fatura → Alış İrsaliyesi bölümünden "Tipi" alanı "İthalat/İhracat" olarak işaretlenen ve döviz tutarı girilen bir irsaliye kaydının oluşturulması gerekir.

Yapılan ithalatın "Export (Dosya No) Numarası" ithalat irsaliyesinin kesilmesinden sonra belirleniyorsa, bu numaranın daha sonra da irsaliyeye girmesi veya Dekont Modülü → İthalat/İhracat İşlemleri → [İthalat/İhracat Referans No Atama](<İthalat-İhracat Referans No Atama.md>) bölümünden aktarılması mümkün. "İthalat Kapatma" sırasında belirlenen export referans numarası, oluşacak faturaya bu işlemle aktarılır. "Parçalı İthalat Kapatma" yapılacaksa; export referans numarası, stok hareket kayıtlarında tutulan "Export Referans No" alanına aktarılır.

Girilen ithalat irsaliyesi kaydındaki "Miktar" bilgisi normal şartlarda stok hareket kayıtlarında izlenmez. Bu bilgi başka bir alanda program tarafından tutulur. "İthalat Kapatma" işlemi gerçekleştiğinde, "Miktar" bilgisi stok hareket kayıtlarında izlenebilir. Ancak, Fatura → Kayıt → [Alış Parametreleri](<../../../../Lojistik - Satış/Fatura/Kayıt - Fatura/Alış Parametreleri.md>) → "İthalat/İhracat Miktarları Stoklara Geçsin" parametresi işaretlenirse, mal fiilen stoklara girmese bile miktar bilgisi stoklarda izlenir.

Yapılan ithalatla ilgili mal bedeli ve diğer tüm masraf kayıtlarının Dekont → Kayıt → "[Genel Dekont Kaydı](<../Genel Dekont Kaydı/index.md>)" bölümünden girilesi gerekir.

Mal bedeli ve masraf kayıtları gerçekleştirilirken dikkat edilmesi gereken noktalar şunlardır:

- Bu tür dekont kayıtlarının "Seri Numarası" alanına mutlaka **IT** (ithalat kaydı anlamına gelir) girilmesi.
- Hem mal bedeli hem de ilgili ithalat masrafları için "Muhasebe Kodu" alanında 159 veya 259 hesapların kullanılması ("Genel Dekont Kaydı" ekranında girilen ithalat bilgilerinde 159 veya 259 hesaplar dışında başka bir hesabın kullanılması durumunda, ilgili ithalat için bu kayıt dikkate alınmaz).
- "Genel Dekont Kaydı" bölümünden girilen mal bedelinin mutlaka döviz cinsinden kaydedilmesi ve "Export Tipi" olarak "Mal Bedeli" seçilmesi gerekir.

"İthalat Kapatma" işlemi yapılırken, "İrsaliye" ekranından kaydedilen döviz tutarı ile, "Dekont" modülünden "Mal Bedeli" olarak kaydedilen işlemin döviz tutarları karşılaştırılır ve sadece birbirine eşit ise işlem yapılır.

İlgili ithalata ait mal bedeli ve masraf kayıtlarının (masrafların stok hareketlerine yansıtılması istendiği zaman) "Export Referans No" alanlarının dolu ve aynı olması gerekir. Çünkü, aynı "Export Referans No" kaydedilen ithalat irsaliyesinde de aranır ve bu numaraya göre ithalat kapatma işlemi gerçekleştirilir. Tüm kayıtların tamamlanmasından sonra "İthalat Kapatma" işlemi düzgün çalışır.

**İthalat Ön Sorgulama**

![](../../../../../_assets/76fa752a4eb6f1aaee6d.png)

İthalat Ön Sorgulama sekmesinin alanları ve içerdiği bilgiler aşağıdaki şekildedir:

| İthalat Kapatma Ekranı |  |
| --- | --- |
| Cari Kodu | Listelenmesi istenen alış irsaliyeleri için ilgili cari kodun seçildiği alandır. Girilen cari koda kayıtlı irsaliyelerin listelenmesi sağlanır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, cari kodlar arasından seçim yapılır. |
| İthalat Referans No | İthalat kapatma için referans numarası girilen alandır. Girilen referans numarası ile kaydedilen irsaliyelerin listelenmesi sağlanır. Boş bırakıldığında ilgili cari koda ait tüm irsaliyeler listelenir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, referans numaraları arasından seçim yapılır. |
| Fiili İthal Tarihi | Kapatma işlemi sonucu oluşacak alış faturası için tarih girilen alandır. |
| GÇB No | İthalat kapatma işlemi için "Gümrük Çıkış Beyanname" numarasının girildiği alandır. |
| GÇB Tarihi | İthalat kapatma işlemi için "Gümrük Çıkış Beyanname" tarihinin girildiği alandır. |
| Masraflar İçin Hesap Kodu | "Genel Dekont Kaydı" bölümünde girilen masraf kayıtları için hesap kodu seçilen alandır. 159 veya 259 olmak üzere iki seçenektir. |
| İthalat Masraflarının Dağıtılması Birim Ağırlığa Göre Yapılsın | İthalat masraflarının, stoktaki birim ağırlığa göre yapılması için kullanılan seçenektir. |
| İthalat Masrafları Bedelsiz Kalemlere Dağıtılsın | İthalat masraflarının bedelsiz kalemlere dağıtılması için kullanılan seçenektir. |
| Parçalı İthalat | Seçilecek alış irsaliyeleri tamamen kapatılmayacak ise "Parçalı İthalat" seçeneği işaretlenir. Bu sorgulama işaretlendiğinde, ilgili cari koda ait irsaliyelerin birden fazlasının içinde kayıtlı olan stok kalemleri arasında seçim yapılarak kapatılması sağlanır. Parçalı ithalat kullanılacak ise; "Genel Dekont Kaydı" kullanılarak girilecek kayıtlarda dikkat edilmesi gereken bazı koşullar vardır: Firmalar, genellikle ithal edilen mallar geldiğinde bunları başka bir depoda tutar ve belli dönemlerde veya mala ihtiyaçları olduğunda bu depolardan malları parçalı olarak alır. Bu durumda, mal yurt dışından geldiğinde mal bedeli tutarı yine "Genel Dekont Kaydı" bölümünden IT Seri Numarası, Export Referans Numarası ve 159/259 hesaplar kullanılarak girilir. Ambardan çekilecek mallar için ödenen bir masraf (nakliye) varsa, "Genel Dekont Kaydı" bölümünden 159 veya 259 hesaplar kullanılarak ve Export Referans Numarası, mal bedeli kaydında kullanılan "Referans Numarasının" sonuna bölme (/) ekleyerek numaralandırılır. **Örneğin:** Mal bedeli kaydındaki Export Referans Numarası 20 ise, ilk çekilecek malların masrafı için belirlenecek referans numarasının 20/1 olması gerekir. Daha sonraki dönemlerde ambardan çekilecek mallar için yapılacak masraflarda da Export Referans Numaralarının 20/2…..9 şeklinde kaydedilmesi gerekir. Masraflara ait referans numaralarının 20/1,20/2.. şeklinde kaydedilmesi, girilen masrafların sadece çekilen mal veya mallara ait olduğu durumlar için geçerlidir. İlgili referans numarasıyla ithal edilen mal bedelinin tümü için geçerli bir masraf kaydedilecekse, Referans Numarası olarak normal Export Referans Numarasının girilmesi gerekir (Örneğin; 20). Bu referans numarasıyla kaydedilmiş masraf tutarı, parçalama ekranından seçilecek stok kalemlerine dağıtılır. **Parçalı İthalat** işaretlendikten sonra klavyede yer alan \<tab\> tuşu ile "İthalat Parçalı Kapatma" sekmesine geçilir. |

**İthalat Kapatma**

Yukarıda girilen bilgiler doğrultusunda, irsaliye/irsaliyeler ("Parçalı Kapatma" seçeneği **işaretlenmeden** klavyedeki \<tab\> tuşu ile ilerlendiğinde) açılan "İthalat Kapatma" sekmesinin alt kısmında listelenir.

![](../../../../../_assets/f6b46832bc24a9b0ffad.png)

İthalat Kapatma sekmesinin alanları ve içerdiği bilgiler aşağıdaki şekildedir:

| İthalat kapatma İşlemi Ekranı |  |
| --- | --- |
| İrsaliye Numarası Aralığı | Kapatma işlemi gerçekleştirilecek ithalata ait alış irsaliyesi numarasının girildiği alandır. Girilen numara aralığı kısıdı, kesilen alış irsaliyelerinin bulunarak listelenmesini sağlar. |
| İrsaliye Tarih Aralığı | Listelenmesi istenen irsaliyeler için tarih aralığı kısıdı verilen alandır. |
| ![](../../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Listelenen irsaliyeler arasında, kapatması yapılacak irsaliyeler işaretlendikten sonra kapatma işleminin yapılması için kullanılan butondur. Butona tıklanması ile birlikte, ilgili referansa sahip irsaliyeler ile dekonta aynı referans koduyla kaydedilen mal bedeli kayıtlarının döviz tutarları karşılaştırılır. Tutuyorsa, alış irsaliyesindeki stok kodlarına dekonttan aynı Export Referans Numarası ile kaydedilen masraflar dağıtılarak alış faturası oluşturulur. Masraf rakamları toplamı da faturadaki "Ek Maliyet" alanına aktarılır. İlgili kapatma işlemine ait, "Genel Dekont Kaydı" bölümünde seri numarası IT olan yeni bir dekont oluşturularak entegrasyon kayıtları (dekonttan kaydedilen 159 veya 259 hesaplara alacak, stok alış hesap koduna borç hareketi aktarılır) yapılır. |
| ![](../../../../../_assets/249197106fa4d90d9fe9.png) Çıkış | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |

**İthalat Parçalı Kapatma**

"Parçalı İthalat" seçeneğinin işaretlenmesi ile açılan sekmedir.

![](../../../../../_assets/d1f9d48cd23ddf5096fe.png)

İthalat Parçalı Kapatma sekmesinin alanları ve içerdiği bilgiler aşağıdaki şekildedir:

| İthalat Kapatma Ekranı |  |
| --- | --- |
| İrsaliye No | İlgili cari hesaba ait irsaliyenin seçildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, irsaliye numaraları arasından seçim yapılır. |
| Stok Kodu | "İrsaliye No" alanında girilen irsaliyedeki mal kalemlerinin seçimi için kullanılan alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, stok kodları arasından seçim yapılır. Girilen irsaliyeye ait stok kalemleri ekran üzerinden izlenir. İstendiğinde miktarları değiştirilebilir. |
| Miktar/Miktar-2 | İthalat parçalı kapatma için miktar girilen alandır. Dekont → Kayıt → [Dekont Parametreleri](<../Dekont Parametreleri.md>) → "Miktar Girişi Yapılsın" parametresinin işaretlenmesi ile ekrana gelir. |
| Depo Kodu | İthalat parçalı kapatma için depo kodu girilen alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile depo kodları arasından seçim yapılır. |
| ![](../../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | "İthalat Kapatma" işleminin gerçekleşmesi için kullanılan butondur. Parçalı ithalat kapatmada birden fazla irsaliyenin seçilmesi halinde, her bir irsaliye için ayrı alış faturaları oluşturulur. Oluşan ithalat faturalarına alış irsaliyesinin numarası verilir. Parçalı yapılan ithalatlara ait irsaliye hareketleri, ithalat tamamen kapatılana kadar stok hareket kayıtlarından izlenebilir. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
