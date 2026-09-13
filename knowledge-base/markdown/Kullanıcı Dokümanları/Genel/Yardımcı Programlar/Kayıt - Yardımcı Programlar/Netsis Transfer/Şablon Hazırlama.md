---
title: "Şablon Hazırlama"
page_id: "24753083"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Genel"
  - "Yardımcı Programlar"
  - "Kayıt / Yardımcı Programlar"
  - "Netsis Transfer"
  - "Şablon Hazırlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Yardımcı Programlar / Kayıt / Yardımcı Programlar / Netsis Transfer / Şablon Hazırlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTFlYWY2NDgyLTBlYmMtNDBjYS05NTVhLWJlMTliZWNlOTQyZCZsaW5rPTA1OWUzYTJhLWNkNWMtNDkyOS05Y2FhLTk4Nzg3ZjZjMGY2NCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=1eaf6482-0ebc-40ca-955a-be19bece942d&link=059e3a2a-cd5c-4929-9caa-98787f6c0f64&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "sablon-hazirlama_41170197_24753083.html"
source_version: "2022-10-04T14:57:05.063+03:00"
source_bytes: 676798
fetched_at: "2026-09-13T04:17:14+00:00"
generator: "netsis-scraper 1.0.0"
---
# Şablon Hazırlama

Şablon Hazırlama, Genel Bölümü'nde, "Kayıt/Yardımcı Programlar" menüsünün altında yer alır. Şablon Hazırlama ekranı, Şablon Sabit ve Satır Bilgileri olmak üzere iki sekmeden oluşur. "Şablon Hazırlama" ekranından, dışarıya veri aktaracak veya dışarıdan program içine veri alacak şablon tanımlamaları yapılır.

**Şablon Sabit**

Şablon Sabit, hazırlanacak şablona ait genel tanımlamaların yapıldığı sekmedir.

![](../../../../../_assets/34e5aadcd7921db458ad.png)

Şablon Hazırlama ekranı Şablon Sabit sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Şablon Hazırlama Ekranı |  |
| --- | --- |
| Şablon Adı | Oluşturulacak şablon için isim tanımlanan alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, şablon adlarına ulaşılır. |
| Yükle/Sakla | Bilgiler programa aktarılacağı zaman "Yükle", Programdan dışarıya alınacağı zaman "Sakla" seçeneğinin işaretlenmesi gerekir. |
| Text Dosya Adı | Bilgilerin içeri alınmasında ya da dışarı verilmesinde kullanılacak dosyanın, disk üzerinde bulunduğu dizin ve dosya adının girildiği alandır. Veriler program içine aktarılırken, bilgiler bir TXT ya da XLS dosya içinden alınır. Oluşturulacak şablon, verilerin bulunduğu dosyanın yapısına göre hazırlanır veya veriler programdan dışarı gönderildiğinde, bilgiler TXT/XLS dosya içinde oluşturulur. |
| Log Adı | Hazırlanan şablon kullanılarak yapılacak transfer işlemleri sırasında, aktarmayla ilgili bilgilerin yazılacağı dosya adının girildiği alandır. Boş bırakılabilir. |
| Log Görüntülensin | Transfer sırasında bir uyarı alınmışsa, transfer bitiminde Log dosyasının görüntülenmesi için kullanılan seçenektir. İşaretlenmediği zamanlarda bile, transferde alınan uyarılar Log dosyasına yazılır. |
| Text Karakter Tipi | Aktarım sırasında kullanılacak veya oluşturulacak Text dosyanın karakter setinin belirlenmesi için kullanılan alandır. Text dosyası "Dos" ortamında açıldığında, görüldüğü şekilde alınması için "Dos" seçeneğinin seçilmesi gerekir. Dosyanın Windows formatında görüntülenmesi için "Windows" seçeneğinin seçilmesi gerekir. İlgili dosya formatında herhangi bir değişiklik yapılması istenmediğinde olduğu gibi görüntülenmesi için "Hiçbiri" seçeneğinin seçilmesi gerekir. |
| Başlangıç Satırı | Transferin yapılacağı Text dosyada bilgileri alınması istenen satırın girildiği alandır. Bazı Text dosyalarının başında başlık gibi bilgiler bulunduğu için, aktarımda bu satırların dikkate alınmaması gerekir. |
| Hareket Türü | Aktarım yapılacak hareketin türünün seçildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile hareket türleri arasından seçim yapılır. **Örneğin;** Txt dosyasından, programın "Alış İrsaliyesi" bölümüne aktarım yapılacağı zaman, "Hareket Türü" alanından "Alış İrsaliyesi" seçeneğinin seçilmesi gerekir. |
| Dosya Tipi | Aktarım yapılacak dosya türünün belirlendiği alandır. Alanın sağ tarafında bulunan aşağı ok butonu ile, Text Dosya ve Excel Dosyası seçenekleri arasından seçim yapılır. |
| Hata Durumunda İşlemi Kes | Aktarım sırasında herhangi bir hata oluştuğunda, işleme devam edilmesi için kullanılan seçenektir. |
| Sipariş Oluşturulurken İrsaliye Oluşturulsun | Hareket türü "Sipariş" seçilerek yapılan aktarımlarda - yükle seçeneği işaretli - irsaliyelerin de aynı anda oluşması için kullanılan seçenektir. Diğer hareket türlerinde bu alan aktif gelmez. |
| Full Trans | Aktarım sırasında herhangi bir hata sonucu işlem kesildiğinde, o ana kadar yapılan aktarımların geri alınması için kullanılan seçenektir. Seçeneğin işaretli olmadığı şablonlara göre aktarım yapıldığında, aktarım sırasında herhangi bir hata oluşması durumunda, hata oluşana kadar aktarılan bilgiler silinir. |
| Fatura/İrsaliye Varsa Kayıt Etme | Programa Fatura/İrsaliye aktarımı yapılırken, sistemde aktarılan Fatura/İrsaliye olması durumunda aktarımın yapılmaması için kullanılan seçenektir. |
| Barkod Kontrolü Yapılsın | Aktarım yapılacak dosyada "Stok Kodu" yerine "Barkod Numarası" tanımlı ise, "Barkod Kontrolü Yapılsın" seçeneği işaretlendiğinde, aktarım yapılırken barkod numaraları stok koduna çevrilerek aktarılır. Bu işlemin yapılması için her stok koduna barkod numarasının tanımlanması gerekir. |
| ![](../../../../../_assets/a1dd8a33b453401054d5.png) Makrolar | Şablon hazırlarken bazı alan aktarımlarının, yapıldığı andaki bilgilere göre oluşması için kullanılan butondur. Alanın sağ tarafında yer alan çubuğa tıklanarak seçim yapılır. **Örneğin** Aktarım yapılan tarihin, son işlem tarihine aktarılması için şablon tanımı yapılırken, makrolar ile tarih bilgisi aktarılırsa her paket çalıştırmada son işlem tarihine paketin çalıştığı tarih aktarılır. Alana makrodan değer aktarılması için, "Saha Adı" alanında ilgili saha seçildikten sonra öndeğer alanına gelerek, makro alanından aktarılması istenen saha seçilir ve öndeğer alanına aktarılır. ![](../../../../../_assets/7c95c106430ef6cae50e.jpg) |
| ![](../../../../../_assets/9d4c535fb00c01186c88.png) Sorgular | "Şablon Sabit" sekmesinde "Sakla" *s*eçilen paketlerde aktif hale gelen alandır. Oluşturulacak dosyadaki kayıtlar için kısıt verilmesini sağlar. **Örneğin** Cari hesaplara ait fatura bilgileri aktarıldığında, "Cari Kodu" alanında ilgili cari hesaplar için kısıt tanımlaması yapılabilir. İlgili paket çalıştığında, sadece kısıt verilen cari hesaplara ait fatura bilgileri aktarılır. ![](../../../../../_assets/584aa9d73586408cff53.png) |

**Satır Bilgileri**

Satır Bilgileri, Text dosyanın içerdiği verilere ait başlangıç ve bitiş kolonlarının şablonda belirlenmesi için kullanılan sekmedir.

![](../../../../../_assets/f4ef8adf0bca874a8e2b.png)

Şablon Hazırlama ekranı Satır Bilgileri sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Şablon Hazırlama Ekranı |  |
| --- | --- |
| Ön İzleme | Aktarımı yapılacak Text dosyasının içeriğinin izlendiği alandır. Text dosya içeriğinin, satır bazında kolon numaralarına göre ayrıntılı bir şekilde izlenmesini sağlar. Böylece, ilgili sahaların şablondaki başlangıç ve bitiş kolonlarına göre tanımlaması dosya içeriği görülerek yapılır. |
| Saha Adı | Aktarılacak tablo veya dosyadaki alan isminin izlendiği alandır. Şablon hazırlarken Text dosyadaki ilgili sahanın, programdaki tablonun hangi alanına aktarılacağı belirlenir. Programa aktarım değil, program içinden dosyaya veri gönderilmesi için, gönderilecek bilginin tablodaki hangi alan olduğu da yine "Saha Adı" alanından belirtilir. Böylece belirtilen tablodaki alan, Text dosyasının şablonda belirtilen koordinatlarına göre aktarılır. Saha isimleri "Saha Adı" başlığının sol tarafındaki alanda yer alır. Farenin sol tuşu ile tıklanarak seçim yapılır. |
| Satır | Gönderilecek/alınacak dosyadaki satırların tipi farklı ise, şablon tanımı yapılırken alınacak sahanın bulunacağı satırın girildiği alandır. **Örneğin** Dosya içinde bir satır stok sabit, diğer satır stok sabit ek satırlarının bilgilerini içeriyorsa ve dosyadaki sıra bir stok sabit, bir stok sabit ek şeklinde geliyorsa "Stok Sabit" sahalarını tanımlarken satır numarasına 1, "Stok Sabit Ek" sahalarını tanımlarken satır numarasına 2 değerinin girilmesi gerekir. Ya da, aktarılacak dosyadaki satırların birinci satırı başlık bilgisini içeriyor ve veriler ikinci satırdan başlıyorsa, şablonu hazırlarken satır numarasına 2 değerinin girilmesi gerekir. Böylece, programın içine aktarım yapılırken veriler ikinci satırdan alınarak aktarılır. |
| Sütun | Aktarılacak/gönderilecek saha için başlangıç sütunu girilen alandır. İçeriğe aktarım yapılıyorsa bilgilerin alınacağı sütunun, dışarıya bilgi gönderiliyorsa da gönderilecek bilginin dosyada hangi sütuna gönderileceği belirlenir. |
| Uzun | Aktarılacak saha için karakter uzunluğu belirlenen alandır. Belirlenen uzunluk değeri kadar karakter aktarılır. Bu yüzden, aktarılacak saha için olabilecek en büyük değerin verilmesi gerekir. **Örneğin** Aktarılacak saha yıl ise bu alan için uzunluk değerinin 4 olarak girilmesi gerekir. |
| Öndeğer | Alınan değer boş olduğunda aktarılan değerdir. **Örneğin** Alınan bilgi tarih ise, "Tarih" alanı boş olan kayıtlar için girilecek sabit - günün tarihi gibi - tarihtir. İçeri alınacak dosya içinde hareket türü sabit olarak A tanımlı ve "Saha Adı" alanında şablonda stok hareket türü seçilmişse, "Öndeğer" alanına A girildiği zaman hareketlerin stok hareket türü A olarak aktarılır. |
| Ondalık | Aktarılacak/gönderilecek saha ondalıklı bir saha ise, ondalık değerden sonraki alanların da aktarılması için değerden sonraki basamak sayılarının girildiği alandır. Uzunluk alanının, basamak sayısı göz önüne alınarak tanımlanması gerekir. |
| Rakamsal Grup Ayracı | Aktarılan saha sayısal bir saha ve binler basamağına göre ayrılmış ise - 1.000.000 gibi - grup ayracının belirlendiği alandır. Örneğe göre bu sahanın virgül (,) olması gerekir. |
| Ondalık Ayracı | Aktarılan saha sayısal bir saha ve ondalıklı ise - 1,000,000.75 gibi - ondalık ayracının belirlendiği alandır. Örneğe göre bu sahanın nokta (.) olması gerekir. |
| Baştan Sondan Boşluklar Silinsin | Tanımlanan sahadaki verilerin uzunlukları farklı olduğunda, uzunluğun maksimum uzunluğa göre verilmesinden dolayı, uzunluğu az olan kayıtlarda boşluklar oluşur. Bu boşluklar silinmezse, aktarılan sahada da boşluklar oluşur. Bu tür kayıtların oluşmaması için "Baştan Sonran Boşluklar Silinsin" seçeneğinin işaretlenmesi gerekir. **Örneğin** "Stok Kodu" için uzunluk değeri 15 olarak girildiğinde; alınacak dosyadaki "Stok Kodu" alanlarında 3, 8, 10 gibi uzunluklara sahip stok kodları bulunabilir. Seçenek işaretlenmediği zaman, 15 uzunluk değerinden az olan stoklar boşluklu - 123\_\_\_\_\_\_\_\_ gibi - oluşur. |
| ![](../../../../../_assets/a1dd8a33b453401054d5.png) Makrolar | Şablon hazırlarken bazı alan aktarımlarının, yapıldığı andaki bilgilere göre oluşması için kullanılan butondur. Alanın sağ tarafında yer alan çubuğa tıklanarak seçim yapılır. **Örneğin** Aktarım yapılan tarihin, son işlem tarihine aktarılması için şablon tanımı yapılırken, -makrolar ile tarih bilgisi aktarılırsa her paket çalıştırmada son işlem tarihine paketin çalıştığı tarih aktarılır. Alana makrodan değer aktarılması için, "Saha Adı" alanında ilgili saha seçildikten sonra öndeğer alanına gelerek, makro alanından aktarılması istenen saha seçilir ve öndeğer alanına aktarılır. ![](../../../../../_assets/7c95c106430ef6cae50e.jpg) |
| ![](../../../../../_assets/9d4c535fb00c01186c88.png) Sorgular | "Şablon Sabit" sekmesinde "Sakla" *s*eçilen paketlerde aktif hale gelen alandır. Oluşturulacak dosyadaki kayıtlar için kısıt verilmesini sağlar. **Örneğin** Cari hesaplara ait fatura bilgileri aktarıldığında, "Cari Kodu" alanında ilgili cari hesaplar için kısıt tanımlaması yapılabilir. İlgili paket çalıştığında, sadece kısıt verilen cari hesaplara ait fatura bilgileri aktarılır. ![](../../../../../_assets/584aa9d73586408cff53.png) |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır. Şablon Hazırlama kaydının iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
