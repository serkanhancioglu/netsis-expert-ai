---
title: "Parçalı İthalat Antrepo Takibi"
page_id: "50680020"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Parçalı İthalat Antrepo Takibi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Parçalı İthalat Antrepo Takibi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWNjODM1NmVlLTc3Y2UtNDlhZC1iY2Q4LTE3YjEzZjg0NWQ5NyZsaW5rPTc1ZTllYzk3LTFlYzQtNDQ1Yi1hMGMyLWUzMjVjZGEyNTQ2MCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=cc8356ee-77ce-49ad-bcd8-17b13f845d97&link=75e9ec97-1ec4-445b-a0c2-e325cda25460&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "parcali-ithalat-antrepo-takibi_50690780_50680020.html"
source_version: "2022-11-03T09:39:24.913+03:00"
source_bytes: 538919
fetched_at: "2026-09-13T04:26:02+00:00"
generator: "netsis-scraper 1.0.0"
---
# Parçalı İthalat Antrepo Takibi

Parçalı İthalat Antrepo Takibi ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Firmalar bazı durumlarda ithal edilen mallar geldiğinde, bunları başka bir depoda (antrepoda) tutmakta ve belli dönemlerde veya mala ihtiyaçları olduğunda bu depolardan malları parçalı olarak almaktadırlar. Dış ticaret modülünde yer alan "Parçalı İthalat" parametresi yardımıyla antrepoya ya da fiktif depoya çekilen mallar ve buradan yapılan ithalatlar takip edilebilmekte ve antrepo depo stoğu izlenebilmektedir. Bu işlem için öncelikle antrepo depo olarak takip edilecek olan depo kodlarının tanımlanması gerekmektedir. Depo kodlarında "Antrepo Depo" parametresinin işaretlenmesi yeterlidir.

![](../_assets/52c268451e161d2a7164.png)

Yapılan ithalat işlemi antrepolu olarak yapılacaksa, öncelikle açılan dosyada "parçalı ithalat" parametresi işaretlenmelidir.

![](../_assets/4785921ff32a02379a43.png)

Parçalı ithalat parametresi işaretli olan dosyalarda, dosya kapanana kadar verilen gümrük beyannameleri ayrı ayrı takip edilebilmektedir. Parametre işaretlenmediğinde mevcut halde olduğu gibi dosyaya sadece bir tane beyanname bağlanabilmektedir. Her beyanname bilgisinde dosyano/1 , dosyano/2 şeklindeki referans numaraları sistem tarafından otomatik atanmaktadır.

![](../_assets/5fdb7cf0d8175303d16f.png)

#### Masrafların Takibi

Yapılan ithalatla ilgili mal bedeli ve diğer tüm masraf kayıtlarının *Dekont* *Modülü/Genel* *Dekont Kaydı* ya da *Dış* *Ticaret/ İthalat Masraf Dekont Kayıtları* bölümlerinden birinde girilmiş olması gerekmektedir. Mal bedeli ve masraf kayıtları gerçekleştirilirken dikkat edilmesi gereken konulardan ilki bu tür dekont kayıtlarının seri numarası sahasına mutlaka *"IT"* (ithalat kaydı anlamındadır) girilmiş olmasıdır. İthalat Masraf Dekont Kaydı bölümünden girilen belgelerde IT serisi otomatik gelmektedir.

İkinci olarak hem mal bedeli hem de ilgili ithalat masrafları için muhasebe kodu sahasında **159** veya **259** hesapların kullanılmış olmasıdır. Kayıtta girilen ithalat bilgilerinde **159** veya **259** hesaplar dışında başka bir hesap kullanılır ise ilgili ithalat için bu kayıt dikkate alınmayacaktır. Kayıtta girilen mal bedeli kaydı mutlaka döviz cinsinden kaydedilmeli ve export tipi olarak da "*Mal Bedeli* " seçilmelidir. Referans numarası, *dosya no./parçalı ithalat sıra no.* şeklinde girilmelidir.

Daha sonra ambardan çekilecek mallar için eğer ödenen bir masraf (nakliye) var ise bu masraf yine genel dekont kaydı ya da ithalat masraf dekontu bölümünden **159** veya **259** hesaplar kullanılarak ve export referans numarası, mal bedeli kaydında kullanılan aynı referans numarası ile kaydedilmelidir. Masraflara ait referans numaralarının bu şekilde kaydedilmesi, girilen masrafların sadece çekilen mal veya mallara ait olduğu durumlar için geçerli olduğu anlamına gelecektir.

Bunun dışında ilgili referans numarasıyla ithal edilen mal bedelinin tümü için geçerli bir masraf kaydedilecek ise referans numarası olarak normal export referans numarasının girilmesi gereklidir. Bu referans numarasıyla kaydedilmiş masraf tutarı, parçalama ekranında seçilecek olan stok kalemlerine dağıtılacaktır.

İthalat kapatma işlemi yapılırken irsaliyeden kaydedilen döviz tutarı ile dekont modülünden mal bedeli olarak kaydedilmiş kayıtların toplam döviz tutarları karşılaştırılacak ve ancak birbirine eşit ise ithalat dosyası tamamen kapatılacaktır.

![](../_assets/64944181e967cd8594e9.png)

![](../_assets/ec96e890f6c3b4b89bd2.png)

#### İthalat Kapatma

Antrepodan her mal çekildiğinde ithalat kapatma işlemi çalıştırılmalıdır. İthalat kapatırken kullanıcı tarafından girilen dosya numarasının "parçalı ithalat" özelliği aktif ise GCBNo, GCB Tarihi, parçalı ithalat seçimi otomatik gelmektedir. Bununla birlikte GCB no alanından beyanname seçimi yapılabilmekte ve referans numarası tekrar otomatik oluşturulmaktadır. İlgili özellik işaretlendiğinde depo kodu seçimi zorunlu hale gelmektedir.

![](../_assets/7bb5a58d1dc6dad9dcf7.png)

Parçalı ithalat referans no seçilip tab ile ilerlendiğinde yeni bir ekranda ilgili cari hesaba ait irsaliyeler, irsaliye no rehberinden izlenebilecek ve seçilecektir. İrsaliye no rehberi kullanılarak seçilen irsaliyelerdeki mal kalemlerinin seçimi için ise stok kodu rehberi kullanılacaktır.

Seçilen irsaliyelere ait stok kalemleri ekranda izlenebilecek ve istenir ise miktarları değiştirilebilecektir. "TAMAM" tuşuna basıldığında ithalat kapatma işlemi gerçekleşecektir.

![](../_assets/6b4601fe4d8d5b443588.png)

Yapılan parçalı ithalat kapatıldıktan sonra seçilen depoya, yani yurt içi operasyonlarının yapılacağı depoya depolar arası transfer kaydı da otomatik olarak oluşturulmaktadır. Parçalı yapılan ithalatlara ait irsaliye hareketleri, ithalat tamamen kapatılana kadar stok hareket kayıtlarından izlenebilecektir.

![](../_assets/945c4dd86c7bf14c5abc.png)

Antrepo işleminde dikkat edilmesi gerekenler aşağıdaki şekildedir:

- Satıcı siparişi oluşturulur.
- Ithalat faturası oluşturulur.
- İthalat mal kabul işlemi ile alış irsaliyesi oluşturulur.
- Mal bedeli ve ithalat masraf dekontları girilir. Mal bedeli dekontu, toplam döviz tutarını içerecek şekilde oluşturulur. Her antrepo için ayrı mal bedeli oluşturulmaz, masraflar için ayrı ayrı oluşturulur.
- Alış irsaliyesi ve dekont kayıtları oluşturulduktan sonra ithalat kapama işlemi antrepo bazında yapılabilir.

Not: ithalat dosyası içinde Gümrük Beyanname bilgileri opsiyonel olarak girilebilir. Bu bilgiler girilmediğinde "İthalat Kapatma" ekranında Export Ref. No alanına referans numarası parçalı olarak gelmemektedir. Parçalı görülebilmesi için Gümrük Beyannamelerinde ayrı ayrı girilmelidir.
