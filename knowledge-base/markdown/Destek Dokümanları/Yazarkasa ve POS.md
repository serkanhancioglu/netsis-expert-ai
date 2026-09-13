---
title: "Yazarkasa ve POS"
page_id: "163414084"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Yazarkasa ve POS"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Yazarkasa ve POS"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTUxOGM3MmM1LTM2ZmMtNDY3OC1hYWRmLWY4ZGRjZTViNjkyZSZsaW5rPTljOWNhNmFmLTVmZjYtNDcwZi1iOWM5LWU4ZGQ0ZDhkNGI1OCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=518c72c5-36fc-4678-aadf-f8ddce5b692e&link=9c9ca6af-5ff6-470f-b9c9-e8dd4d8d4b58&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "yazarkasa-ve-pos_163414094_163414084.html"
source_version: "2025-01-06T08:52:59.400+03:00"
source_bytes: 1341004
fetched_at: "2026-09-13T04:22:21+00:00"
generator: "netsis-scraper 1.0.0"
---
# Yazarkasa ve POS

Lojistik - Satış\\P.O.S menüsünde yer almaktadır.

## POS Parametreleri

Lojistik - Satış\\P.O.S \\Kayıt menüsünde yer alan POS Parametreleri ekranından, parametre tanımlamaları yapılır.

Netsis içerisinde desteklenen POS'lar, POS Tipi listesinde (IBM Genius, IBM Sps, InterPOS, IBM POS, NCR 7400 (Tera), SIEMENS(Market+), SIEMENS(Tera), Escort POS, BBS POS) yer almaktadır.

![](../_assets/b19e6a3095b6ffe70104.png)

**POS** **Tipi:** Transferlerin yapılacağı POS seçimi yapılır.

**POS'a Giden Dosyaların Dizini:** POS'a gönderilen dosyaların oluşacağı dizindir. Bu dizinde stok sabit ve cari sabit bilgilerinin text dosyaları oluşur.

Eğer şubelerde stok veya cari bilgileri farklı ise bu dizin farklı girilmelidir. Örnek olarak; C:\\POS\\Giden merkez parametrelerinde, C:\\POS\\Giden\\sube1 şubenin parametrelerinde tanımlandığında merkezin ve şubenin stok textleri farklı dizinlerde oluşur.

**POS'tan** **Gelen** **Dosyaların** **Dizini:** POS'lardan gelen satış dosyalarının olduğu dizindir.

Örneğin; C:\\temp\\Gelen veya C:\\POS\\Gelen şeklinde tanımlanabilir. Hem merkez hem de şubede bu dizin aynı şekilde tanımlanmalıdır.

Gelen dizin tanımlandıktan sonra o dizin altına bir yedek dizini açılmalıdır. Satış dosyaları işlendikten sonra dosyalar otomatik olarak yedek dizinine taşınır. Yedek dizin açılmadığı durumda satış dosyaları işleme başlatıldığında program uyarı verir.

**POS'a** **Giden** **Stok** **Dosya** **Adı:** POSlara bilgi gönderirken oluşacak dosyanın adıdır.

**Barkodsuz** **Stok** **Kodları** **Uzunluğu:** Barkod karakter uzunluğunun tanımlanacağı alandır.

Bazı POSlarda (IBMSPS, IBMPOS, NCR7400, Siemens Bettle) stok kodunun soldan 0 ile doldurulması nedeni ile satışları işlerken stok kodunun anlaşılabilmesi için bu değere ihtiyaç vardır. Barkodlu ürünler 13 karakter uzunluğunda kabul edilir. Diğer stoklar da burada girilen parametreye göre işlem görür. Stok Sabit Kartında 13 ve 8 uzunluklu stok kodları var ise bu parametre değeri 8 olarak girilmelidir.

**Gönderilecek** **Fiyat** : POS'a gönderilecek satış fiyatının(1,2,3,4) seçileceği alandır. Özel fiyat uygulaması kullanılıyorsa liste fiyatı seçilir.

**Depatman** **Kodu:** Grup kodu, Kod1, Kod2 den hangisi seçilmişse ilgili departman kodu olarak gider. Departman Kodu boş olan stoklar POS'a gönderilmez.

- Siemens(Market+) POSta departman kodu olmadığı için bu parametre dikkate alınmaz.
- Hepsi Seçilmesi durumunda Sadece NCR için Grup+Kod1+kod2 gönderilir.

**POS'a** **Gönderilecek** **Stok** **Adı:** Stok Adı/Grup Kodu/kod1/kod2/Alfasayısal 1/2/3/4 sahalarından herhangi biri ürün adı olarak POS'a gönderilebilir.

**KDV** **Oranları:** POS'a gönderilen stok kartlarında tanımlı olan KDV oranları seçilmelidir.

**POS'a** **Cari Aktarım Yapılacak**: Bazı POSlarda cari bilgileri tutulabildiğinden dolayı, bu POS'larda taksitli satış ya da kredili satış yapılabilmektedir. Parametre işaretli ise, cari ile ilgili bu işlemler yapılabilir.(IBM Genius,InterPOS Siemens, NCR)

**POS'a** **Giden** **Cari** **Dosya** **Adı:** POS'a giden dizininde oluşacak cari dosyasının adı girilir.

**POS'tan** **Gelen** **Cari** **Dosya** **Adı:** POS'tan gelen ödeme dosyasının ismi sadece IBM Genius' ta kullanılmaktadır. Satış dosyası gibi işlem görür.

**Kasa** **Kodu:** Carilerin ödemelerinin işleneceği Kasa Kodu'nun girileceği alandır.

**POS** **Gelen Dosya** **Dizin Yapısı**

- Şube yoksa ancak lokal depo uygulaması varsa oluşturulması gereken gelen dizin yapısı aşağıdaki gibi oluşturulmalıdır;

C:\\POS\\gelen\\

C:\\POS\\gelen\\yedek\\

C:\\POS\\gelen\\00000001

C:\\POS\\gelen\\00000001\\yedek

0000001, merkezdeki 1 numaralı lokal depoya işlenecek satış dosyalarının dizinidir. İlk 5 basamak merkezi ifade eder, diğer 3 basamak ise lokal depo numarasıdır.

Parametrede tanımlanması gereken dizin ise; C:\\POS\\gelen olmalıdır.

- Lokal depo uygulaması yoksa, fakat şube var ise olması gereken dizin yapısı aşağıdaki gibi oluşturulmalıdır;

C:\\POS\\gelen\\

C:\\POS\\gelen\\yedek\\

C:\\POS\\gelen\\00001 veya C:\\POS\\gelen\\00001000 ikisi de aynı

C:\\POS\\gelen\\00001\\yedek veya C:\\POS\\gelen\\00001000\\yedek

C:\\POS\\gelen\\ dizinine atılan satış dosyaları merkeze, 001 altına atılan satış dosyaları ise şube 1' e işlenir.

Parametrede tanımlanması gereken dizin C:\\POS\\gelen şeklinde olmalıdır. POS modülü merkezde çalıştırılırsa hem merkezin, hem de şubenin satışları işlenir. Şubede çalıştırılırsa, sadece şube C:\\POS\\gelen\\00001 altındaki dosyalar şube 1' e işlenir.

- Hem Şube Hem de lokal depo varsa dizin yapısı aşağıdaki gibi oluşturulmalıdır;

C:\\POS\\gelen\\merkez 0 lokal dePOSuna

C:\\POS\\gelen\\yedek\\merkez yedek

C:\\POS\\gelen\\00000001\\ merkez 1 lokal dePOSuna

C:\\POS\\gelen\\00000001\\yedek\\ merkez 1 lokal depo yedek

C:\\POS\\gelen\\00001001\\ Şube1 1 lokal dePOSuna

C:\\POS\\gelen\\00001001\\yedek Şube1 1 lokal depo yedek

C:\\POS\\gelen\\00001002\\ Şube1 2 lokal dePOSuna

C:\\POS\\gelen\\00001002\\yedek Şube1 2 lokal depo yedek

şeklinde dizinler tanımlanmalıdır. Merkezde ve şubede parametre tanımı;

C:\\POS\\gelen şeklinde olmalıdır.

POS Parametreleri/ Diğer Parametreler

![](../_assets/b003089735f58a806dce.png)

**Entegrasyon:** Satışların entegrasyona işlenmesi için kullanılan parametredir.

**Kümülasyon:** Entegrasyon parametresi açıksa, ödeme tiplerinde aynı muhasebe koduna ait ödemeleri kümüle ederek entegrasyona atılmasını sağlar.

**Stok** **Kodu** **POSa** **Gönderilsin:** Stok kodunda barkod tutuluyor ve POS'a gönderilmesi isteniyor ise bu parametre işaretlenmelidir.

**Dosyadaki İlk** **Tarih:** Dosyadaki ilk tarih parametresi işaretlendiğinde, satış dosyasındaki ilk oluşan belgede yazan tarih baz alınarak, ilgili dosyadaki tüm kayıtlar o tarih olacak şekilde aktarılır.

**Update Kodu** **Sıfırlansın:** Bu parametre stok sabit dosyasındaki update kodu sahasındaki 'X' I boşaltır. Eğer POS'a bilgi gönderirken sadece değişen bilgiler gönderiliyor ise bu parametre işaretli olmalıdır. (Örneğin; bir markette iki ayrı marka POS var ise ilk stok gönderilen POS' ta bu parametre işaretsiz, ikinci POS' ta ise işaretli olmalıdır.)

**İadeler** **Dikkate** **Alınmasın:** Bu parametre ile satış dosyasındaki iade satırları dikkate alınmadan geçilir.

**Fat** **Enteg.Ayrı** **İşlensin:** Bu parametre işaretlenirse satış hareketlerinde gelen fatura belgeleri entegrasyona atarken ayrı satırlar halinde işler, parametre işaretli olmadığında satışları kümüle olarak oluşturur.

**Stok** **Açıklama** **Aktarılan** **Dosya** **Adı** **Olsun:** Parametre işaretlenirse, TBLSTHAR tablosundaki açıklama kolonuna aktarılan dosyanın adı yazılır.

Parametre işaretli olmadığında, satışlar işlenirken TBLSTHAR tablosuna açıklama kolonuna satışa göre aşağıdaki açıklamalardan biri atılır;

-
  - POS FİŞ SATIŞ
  - POS SATIŞ İADE
  - POS FAT.SATIŞ
  - POS FAT.SATIŞ İADE
  - POS KREDİLİ SATIŞ

## POS Parametreleri/ Ödeme Detay Kayıtları

![](../_assets/a32420083e0d14d41370.png)

**Ödeme** **Tipi:** POS'ta tanımlı ödeme tuşu tipidir.

**Kasa** **/Cari:** Ödeme tipinin cari ya da kasa olarak seçimi yapılır.

**Kasa/Cari:** Ödemenin hangi Kasa/Cariye işleneceği bilgisi seçilir.

## POS'a Ürün Gönderme

Lojistik - Satış\\P.O.S\\Kayıt menüsü altında yer alır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/21148d53-d5a1-4260-8bb5-1096d0b619a5/posa ürün gönder.png)

**Stokların** **Gönderileceği** **POS:** POS tipi seçimi yapılacak alandır.

**Fiyat** **Grubu:** Özel fiyat sistemi açık olduğu durumda hangi fiyat grubundaki fiyatların POS'a gideceği bilgisi girilir.

**Fiyat** **Tarihi:** Özel fiyat sisteminde fiyatların gönderileceği tarih alanıdır.

**Aktarılacak** **Stoklar:** "Hepsi" seçildiginde verilen kısıtlara uyan stoklar POS'a gönderilir. "Değişenler" seçildiğinde ise girilen kısıtlara uygun olan kayıtlardan update kodu 'X' olanları gönderir.

**Update** **Kodu** **Sıfırlansın:** Varsayılan olarak POS parametrelerinde seçilen gelmektedir.

Fiyat uygulaması açık olduğu durumda gönderilecek fiyat belirlenirken; geçerli fiyat listelerinden en büyük başlangıç tarihli ve fiyat grubu girilen veya fiyat grubu boş olan fiyat listesindeki fiyat, listede fiyat yoksa stok kartındaki fiyat gönderilir.

# POS'a Gönderilecek Stokların Özellikleri

- Seçilen Stok fiyatı\>0 olması gerekir.

İnterPOS'ta stok kartındaki zaman birimine 'P' girildiğinde, satış fiyatı 0 olsa bile POSa gönderilir ve bu tür stokların fiyatları satış anında girilir.

- Seçilen departmanın boştan farklı olması gerekir.
- Stokun genel kilidinin veya satış kilidinin olmaması gerekmektedir. (Sadece IBM Geniusta, kilitlenen stoklar kilit flagi ile POS'a gönderilmektedir.)
- "Değişenler" seçildiyse update kodlarının 'X' olması gerekir.

IBMSPS, IBMPOS,Siemens(Market+) barkodlar 0 ile tamamlandığı için gönderilen kodun uzunluğu uygun olmalıdır. Kod 13 karakter uzunlukta olmalı ya da parametrelerde girilen barkodsuz stok kodları uzunluğunda olmalıdır.

- Stokun Satış KDV oranının POS Parametrelerindeki tanımlı oranlardan birisi olmalıdır.
- Stok kodu barkod parametresi kapalıyken, barkodlardan en az birinin boştan farklı olması

gerekmektedir.

# POS'a Gönderilecek Stokların Özellikleri-İnterPOS

- InterPOS' ta her stokun tekrarsız bir **PLU** **kodu** olmalı ve bu kod 6 basamaklı nümerik bir kod olmalıdır.

(Örnek; 000006)

- Bu PLU kodunun stok kartında **ÜRETİCİ** **KODU** sahasına girilmesi gerekmektedir.
- PLU numarası başka bir stok ile aynı olmamalıdır.
- Satışların işlenmesinde sorun olmaması için Plu Numarası ile stok kodu birbirinden farklı olmalıdır.

# Tartılı Ürünler

- POS'a gönderilecek tartılı ürünler için stok kartındaki "Tartı Ürünü" checkbox'i işaretlenmelidir.

![](../_assets/cfdfd70020b5f1068414.png)

# POS'a Gönderilen Barkodlar

- Eğer Barkod1, Barkod2, Barkod3 sahalarından boş değerden farklı olanlar uzunluk kurallarına uyuyorsa(IBMSPS, IBMPOS, NCR7400, Siemens Bettle POSları için) POS'a gönderilir.

- Stok Kodu Barkod parametresi işaretli ise ve stok kodu uzunluk kurallarına uyuyorsa POS'a gönderilir.
- Eğer Satış Parametrelerinde "Barkod/Üretici kodu dosyadan okunsun mu" parametresi seçiliyse ve ilgili stok için barkod dosyasında kayıt varsa POS'a gönderim yapılır.

## POS'a Cari Gönderme

Lojistik - Satış\\P.O.S\\Kayıt menüsü altında yer alır. POS'lara cari sabitten bilgi gönderilmesi amacıyla kullanılır.

Carilerin gönderileceği POS bilgisi, Aktarılacak cari seçimi ve Kod bilgisi seçilerek "Tamam" butonuna tıklanıp POS'a cari gönderimi sağlanır.

Sadece INTERPOS, IBM GENIUS ve NCR (Tera) POS'larda çalışmaktadır.

![](../_assets/3c29565e7744cc2283e6.png)

## POS'tan Satış İşleme

Lojistik - Satış\\P.O.S\\Kayıt menüsü altında yer alır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/44219b6c-7b1c-421d-99b9-16c99fecdf0f/postan satış işleme.png)![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/eea1aa5b-3e24-43b5-aa33-c64d4b2bf601/genius.png)

**Satışların** **Alınacağı** **POS:** Satışların alınacağı POS tipi seçilir.

**İşlenecek** **Dosyalar:** Bu alanda görülen dosyalar dizinlerine göre satışları işler.

Satışlar işlenmeden önce bütün satış dosyası kontrol edilir. Stoklar, ödeme tipleri, cari kodlar, kasa kodlarından olmayan değerler varsa uyarı verip olmayan kayıtları gösterir.

Satışlar önce bir temp tabloya işlenir(POStemp), temp tabloya kaydetme işlemi bittikten sonra, text dosya yedek dizinine taşınır.

Her işlenen satış dosyası bulunduğu dizin altındaki yedek dizinine taşınır.
