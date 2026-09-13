---
title: "Netsis Transfer Destek Dokümanı"
page_id: "135825035"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis Transfer Destek Dokümanı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis Transfer Destek Dokümanı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTFmNzAxN2I2LWI4MGQtNDczNy05NDc4LWFkNTJhNThkN2UwOCZsaW5rPTRjODA1ZTk2LTY4NTAtNGRkOC1iZGQ2LWRhNDgxMjVlYTAwMyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=1f7017b6-b80d-4737-9478-ad52a58d7e08&link=4c805e96-6850-4dd8-bdd6-da48125ea003&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-transfer-destek-dokumani_135825035_135825035.html"
source_version: "2024-03-29T13:03:55.947+03:00"
source_bytes: 3464381
fetched_at: "2026-09-13T04:22:58+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis Transfer Destek Dokümanı

Netsis Transfer ile, excel veya text dosyası olarak belirli bir şablon kurallarına göre hazırlanan verilerin veritabanına toplu bir şekilde aktarılması, sistemde mevcut verilerin excel veya text dosyalarına hızlı bir biçimde aktarılması sağlanır.

Netsis Transfer, Yardımcı Programlar Modülü Kayıt Menüsü altında yer alır. Netsis Transfer menüsü altında Şablon Hazırlama, Paket Çalıştırma ve Şablon Sakla/Yükle menüleri yeralır.

![](../_assets/46d54a4a06d200a56da4.png)

# Şablon Hazırlama

Şablon Hazırlama ekranında veritabanındaki tablolara aktarılacak veya dışarıya alınacak kayıtlarla ilgili şablon tanımlaması yapılır. Bu ekran Şablon Sabit ve Satır Bilgileri adında 2 sekmeden oluşur.

Şablon Sabit sekmesinde, hazırlanacak şablona ait genel tanımlamalar yapılır. Örneğin; alış irsaliyelerinin excel dosyasından netsise aktarımı için bir şablon tasarlandığını varsayalım.

![](../_assets/2e704229e2bbf036a069.png)

**Şablon** **Adı**: Yeni bir şablon tanımı yapılacaksa, yeni şablon adı girilir. Daha önce tanımlanan şablon bilgileri ekrana getirilecekse rehber yardımıyla daha önceden tanımlanan şablonlar seçilir.

**Yükle/ Sakla**: Kayıtların dışarıdan Netsis' e aktarımı için "**Yükle**", Netsis' ten dışarı aktarım için "**Sakla**" seçeneği seçilmelidir. Alış irsaliyeleri Netsis' e aktarılacağı için yükle seçeneği seçilir.

**Text** **Dosya** **Adı**: Aktarımda kullanılacak dosyanın disteki dizin ve dosya adı bilgisi girilmelidir.

**Dosya** **Tipi:** Aktarım sırasında excel dosyası kullanılacaksa "**Excel** **Dosyası**", text dosyası kullanılacaksa "**Text** **Dosya**" seçilmelidir.

**Log Adı:** Paket Çalıştırma işlemi sırasında şablondan kaynaklanan bir hata alınması durumunda, hata loglarının kaydedilmesi ve sonradan incelenebilmesi için log adı kısmında txt uzantılı log dosyasının oluşturulacağı dizin seçilir.

**Log Görüntülensin:** Eğer işlem sonrasında log kayıtlarının otomatik olarak gösterimi istenirse bu parametre işaretlenir. Parametre işaretli olmasa da işlem sonrasında oluşan log kayıtları ilgili dosyaya kaydedilir.

**Hareket** **Türü**: Aktarımın yapılacağı işlem türü seçilir. Buradaki hareket türlerine göre satır bilgileri sekmesindeki alanlar otomatik olarak listelenecektir.

![](../_assets/09c0476391d1309e6da0.png)

Eğer listede mevcut olmayan hareket türüne ait kullanıcı tanımlı bir tabloya kayıt aktarımı yapılacaksa "**K-Serbest**" seçeneği seçilmelidir. Hareket türü Serbest seçildiğinde Tablo Adı alanı aktif olur ve bu alana kayıtların aktarılacağı tablo adı girilir.

![](../_assets/d64199cb6cb6538881ec.png)

**Başlangıç Satırı:** Transferin yapılacağı dosyada eğer başlık bilgileri bulunuyorsa, Başlangıç Satırı alanına kayıtların başladığı satır bilgisi girilir. Örneğin excel dosyası içinde, başlık bilgisi ilk satırda tanımlı ise, kayıtlar 2. satırdan başlamaktadır. Bu sebeple başlangıç satırı 2 girilir.

![](../_assets/1c2522dead2b822c37a1.png)

**Hata Durumunda İşlemi Kes**: Aktarım sırasında bir hata oluşması durumunda işlemin kesilmesi için bu parametre işaretlenmelidir.

**Sipariş** **Oluşturulurken** **İrsaliye** **Oluşturulsun:** Hareket türü Sipariş (Satıcı veya Müşteri) seçildiğinde, bu parametre aktif olur ve siparişler aktarılırken varsa irsaliyelerin de aktarılması istenirse işaretlenmelidir.

**Full** **Trans:** Aktarım sırasında herhangi bir hatada işlem kesildiğinde, o ana kadar yapılan aktarımların geri alınması için bu parametre işaretlenmelidir. Bu parametre işaretli değilse, aktarım belli bir yerde hata alarak tamamlandığında, hata alınan satıra kadar aktarılan kayıtlar sistemde saklanmaktadır.

**Fatura** **İrsaliye** **Varsa** **Kayıt** **Etme:** Fatura, İrsaliye tipli hareket türü seçildiğinde, sistemde aktarılmak istenen Fatura, İrsaliye varsa kaydedilmemesi için bu parametre işaretlenmelidir.

**Barkod Kontrolü Yapılsın:** Aktarım yapılacak dosyada stok kodu yerine barkod numarası tanımlı ve bu parametre işaretlenirse, aktarım yapılırken barkod kodları stok kodlarına çevrilerek aktarım yapılır.

**Script Alanı:** Aktarım Öncesi/Aktarım Sonrası Çalıştırılacak Script olmak üzere 2 kısımdan oluşur. Yardımcı Programlar Modülü Şirket Şube Parametre Tanımları ekranında, "**Dinamik Kodlama** **Sistemi**" parametresi işaretli olduğunda bu alanlar aktif olur. Aktarım öncesi ve aktarım sonrasında çalışmak üzere script kodları yazılabilir.

Şablon Sabit Bilgileri kaydedildikten sonra, satır bilgilerinin seçilip kaydedildiği **Satır Bilgileri** sekmesine gelinir. Burada seçilen hareket türü veya serbest tablo adına göre sol tarafta ilgili alan bilgileri, ilişkili tablolardaki kolon isimleri listelenir.

Örnekte alış irsaliyelerinin program içine aktarılması olduğu için sol tarafta alış irsaliyesi kaydı sırasında kullanılan tablolar ve kolonları listelenmektedir.

![](../_assets/c1385f6db5f24ab2a893.png)

**Ön izleme:** Aktarımı yapılacak dosyanın içeriğinin izlendiği alandır. Text dosya içeriğinin, satır bazında kolon numaralarına göre ayrıntılı bir şekilde izlenmesini sağlar. Böylece, ilgili sahaların şablondaki başlangıç ve bitiş kolonlarına göre tanımlaması dosya içeriği görülerek yapılır.

**Saha Adı:** Şablon hazırlarken text veya excel dosyasındaki ilgili bilginin, programdaki tablonun hangi kolonuna aktarılacağı belirlenir. Şablon dosyadan programa aktarım değil, program içinden excel ya da text dosyaya veri gönderilmesi için şablon hazırlanırsa, gönderilecek bilginin tablodaki hangi kolon olduğu da yine bu alanından belirtilir. Böylece belirtilen tablodaki kolon, text ya da excel dosyasının şablonda belirtilen koordinatlarına göre aktarılır.

Saha isimleri sol tarafındaki alanda yer alır. Seçim yapılmak istenen kayıt çift tıklanarak saha adı kısmına getirilir.

**Satır:** İçeriye alınacak veya programdan dosyaya aktarılacak kayıtlar hangi satırda yer alıyorsa ilgili satır bilgisi girilir.

Örneğin, stokların aktarılacağı bir excel dosyası içinde, bir satır stok sabit, diğer satır stok sabit ek tablolarının bilgilerini içeriyorsa ve dosyadaki bir sıra bir stok sabit, diğer sıra stok sabit ek şeklinde geliyorsa "Stok Sabit" sahalarını tanımlarken satır numarasına 1, "Stok Sabit Ek" sahalarını tanımlarken satır numarası 2 değeri girilebilir.

Örnekte olduğu gibi aktarılacak dosyada ilk satırda başlık bilgisi ve veriler ikinci satırdan başlıyorsa, Şablon Sabit sekmesinde Başlangıç Satırı 2 girilmişse, bu durumda dosyanın verilerinin başlama satırı olarak 1 girilir.

**Sütun:** İçeriye alınacak veya programdan dosyaya aktarılacak kayıtlar için başlangıç sütun bilgisi girilir. Netsis' e aktarım yapılıyorsa bilgilerin alınacağı sütunun, dışarıya bilgi gönderiliyorsa da gönderilecek bilginin dosyada hangi sütuna gönderileceği belirlenir.

Örnek dosyada alış irsaliyelerinin aktarılacağı şube kodu bilgisi 1. Sütunda yer alıyor. Şablon içinde şube kodu için kolon seçimlerinde sütun bilgisi 1 girilir. (İrsaliye kaydedildiğinde hem TBLFATUIRS tablosuna, hem de TBLSTHAR tablosuna kayıt atılır). FATUIRSV.SUBE_KODU ve STHAR.SUBE_KODU kolonları için sütun 1 girilir.

Benzer şekilde alış irsaliyelerinin numara bilgileri 2. Sütunda yer alıyor. Şablon içinde irsaliye numarası için kolon seçimlerinde sütun bilgisi 2 girilir. (FATUIRSV.FATIRS_NO, STHAR.FISNO ve STHAR.IRSALIYE_NO alanları için sütun bilgisi 2 girilir. Bu şekilde dosyada olan tüm kolonlardaki bilgilerin aktarılacağı kolonlar için sütun bilgileri girilir.

![](../_assets/9adc4150439024914544.png)

![](../_assets/34b49461709944c786fb.png)

**Uzunluk:** Aktarılacak saha için karakter uzunluğu girilir. Belirlenen uzunluk değeri kadar karakter aktarılır. Bu yüzden, aktarılacak saha için olabilecek en büyük değerin verilmesi gerekir.

Örneğin, aktarılacak saha yıl bilgisi ise, bu alan için uzunluk değerinin 4 olarak girilmesi gerekir.

Serbest olmayan alanlarda uzunluk alanına müdahale edilememektedir. Bu alan tablodaki alanın uzunluk değerine göre otomatik olarak belirlenmektedir.

**Öndeğer:** Excel veya text dosyasında seçilen kolonda bir bilgi mevcut değilse veya o kolona varsayılan olarak sabit bir değer atanmak istenirse, öndeğer alanına bu değerin yazılarak kaydedilmesi sağlanır. İlişkili tablolardaki kolonlar için ön değer tanımlaması yapıldığında sütun bilgisi 0 olarak geçilir.

Örnek dosyadan alış irsaliyelerinin aktarımında, alış irsaliyelerinin TBLFATUIRS tablosunda FTIRSIP kolon değeri ve TBLSTHAR tablosunda STHAR_FTIRSIP kolon değeri 4' tür. Aktarım dosyasında her kayıt için bu alanın girilmesine gerek olmadığından, bu 2 kolon için ön değer bilgisi 4 olarak girilebilir.

Benzer şekilde alış irsaliyesi girişi sonrası TBLSTHAR tablosunda STHAR_GCKOD alanı G yani giriş hareketi olarak atıldığı için dosyadaki her kayıt için bu alanın ön değer bilgisi G olarak girilip kaydedilir.

![](../_assets/124bda5303a53e4cece1.png)
![](../_assets/5b73e3e2afca6b142c5c.png)

Önizleme tanımında kullanılacak diğer bir seçenekte ekranın sol köşesinde yer alan **Makrolar** kısmıdır.

![](../_assets/8174456551d2d30b40e4.png)

**Makrolar**: Şablon hazırlarken bazı alan aktarımlarının, yapıldığı andaki bilgilere göre oluşması için kullanılır. Alanın sağ tarafında yer alan çubuğa tıklanarak seçim yapılır.

Örneğin, aktarım yapılan tarihin, son işlem tarihine aktarılması için şablon tanımı yapılırken, makrolar ile tarih bilgisi aktarılırsa her paket çalıştırmada son işlem tarihine paketin çalıştığı tarih aktarılır.

Alış irsaliyesi aktarımında, tablolara Kayıt Tarihi bilgisinin aktarımında aktarımın yapıldığı tarih bilgisi aktarımında Makrolar kullanılabilir. Sol tarafta Kayıt Tarihi bilgisi için TBLFATUIRSV.KAYITTARIHI gün, ay, yıl olarak ayrı ayrı tanımlı olduğu için makrolar kısmından da GUN, AY, YIL bilgileri ayrı ayrı seçilir.

Alana makrodan değer aktarılması için, Saha Adı alanında ilgili saha seçildikten sonra cursor Öndeğer alanında iken, makro alanından aktarılması istenen saha seçilir ve Öndeğer alanına aktarılır.

Benzer şekilde alış irsaliyesi aktarımında Kayıt Yapan Kullanıcı bilgisi için, Netsis'te işlemi gerçekleştiren kullanıcı bilgisinin aktarımında, sol taraftan ilgili TBLFATUIRSV.KAYITYAPANKUL alanı seçilip, cursor Önizleme alanında iken Makrolardan NETSISKULLANICIADI seçilerek bilginin Öndeğer alanına gelmesi sağlanır.

**Baştan** **ve** **Sondan** **Boşluklar** **Silinsin:** Tanımlanan sahadaki verilerin uzunlukları farklı olduğunda, uzunluğun maksimum uzunluğa göre verilmesinden dolayı, uzunluğu az olan kayıtlarda boşluklar oluşur. Bu boşluklar silinmezse, aktarılan sahada da boşluklar oluşur. Bu tür kayıtların oluşmaması için bu parametre işaretlenmelidir.

**Örneğin**

"Stok Kodu" için uzunluk değeri 15 olarak girildiğinde; alınacak dosyadaki "Stok Kodu" alanlarında 3, 8, 10 gibi uzunluklara sahip stok kodları bulunabilir. Seçenek işaretlenmediği zaman, 15 uzunluk değerinden az olan stoklar boşluklu "123 " oluşur.

**Ondalık**: Aktarılacak/gönderilecek saha sayısal bir saha ise, aktif olur ve ondalık değerden sonra kaç hane aktarılması isteniyorsa basamak sayısı girilir.

**Rakamsal** **Grup** **Ayracı:** Aktarılan saha sayısal bir saha ise, aktif olur ve binlik ayraç belirlenir. (Nokta/ Virgül)

**Ondalık** **Ayracı:** Aktarılan saha sayısal bir saha ise, aktif olur ve ondalık ayracı belirlenir. (Nokta/ Virgül)

**Script Alanı:** Programlar Modülü Şirket Şube Parametre Tanımları ekranında, "**Dinamik Kodlama Sistemi**" parametresi işaretli olduğunda bu alanlar aktif olur. Aktarım da çalışmak üzere script kodları yazılabilir.

![](../_assets/42a05e5a9865e60c6274.png)

**Sorgular:** "Şablon Sabit" sekmesinde "**Sakla**" seçilen paketlerde aktif hale gelir. Oluşturulacak dosyadaki kayıtlar için kısıt verilmesini sağlar.

Örneğin, stok kartları aktarımında stok kartları için kısıt tanımlaması yapılabilir. İlgili paket çalıştırıldığında Grup kodu Makarna olan stok bilgileri dosyaya aktarılır.

Sakla seçili şablon çağrıldıktan sonra Sorgulara tıklandığında gelen ekranda Kısıt sekmesindeki Sahalar kısmından STSABIT.GRUP_KODU seçilir ve kısıt verilecek sahalar kısmına atılır. Sonra ilgili kayıt üzerinde çift tıklanır ve ilgili kısıt girilir.

![](../_assets/3eeb0aaa7b0b85f057ff.png)

# Paket Çalıştırma

Şablon Tanımlama işlemi tamamlandıktan sonra şablonda belirtilen sütunlara göre oluşturulan excel dosyasındaki verilerin Netsise aktarımı için Paket Çalıştırma menüsü kullanılır. Şablon rehberinden çalıştırılması istenen Şablon Adı seçimi yapılarak aktarım yapılır. Aktarılacak verilerde veya tanımlamalarda bir sorun yoksa, Netsise aktarım yapılacaktır.

# ![](../_assets/ffedf00de99e0c204762.png)

Şablon Sakla/Yükle

Hazırlanan şablonların başka şirkete gönderilmesi ve gönderilen şirkette tekrar hazırlanmasına gerek kalmadan kullanılmasını sağlayan bölümdür.

![](../_assets/a41261fbeb7f07b38594.png)

# Yükle/Sakla:

**Sakla:** Netsis içinde tanımlanan transfer şablonunun verilen dizine aktarılarak saklanması durumunda seçilir.

**Yükle:** Netsis Transfer şablonlarının Nesis içine yüklenebilmesi için seçilir.

**Dosya Adı:** Netsis' teki transfer şablonunun saklanarak dışarıya alınması durumunda şablonun kaydedileceği dizin bilgisi girilir. Transfer şablonlarının Netsis içine yüklenmesi durumunda şablonun bulunduğu dizin bilgisi girilir.

**Şablon Adı:** Netsis' ten dışarıya alınacak şablonun Netsis'teki şablon adı seçilir. Dışarıdan Netsis' e alınacak şablon için Netsis' te hangi isimle kaydedileceği bilgisi girilir.
