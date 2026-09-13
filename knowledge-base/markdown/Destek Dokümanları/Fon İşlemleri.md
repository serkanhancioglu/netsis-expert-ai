---
title: "Fon İşlemleri"
page_id: "123603434"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Fon İşlemleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Fon İşlemleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWMzNGIwZTgxLWFlYzItNGExMC1iMmI2LTg2YWIwZmRkZmNlMyZsaW5rPTgwZGI0MzE0LThlZGMtNDc1ZS1iMjAxLTVjNzc4MTk3ZmZhNiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=c34b0e81-aec2-4a10-b2b6-86ab0fddfce3&link=80db4314-8edc-475e-b201-5c778197ffa6&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "fon-islemleri_123603455_123603434.html"
source_version: "2023-10-23T15:41:21.010+03:00"
source_bytes: 1616140
fetched_at: "2026-09-13T04:23:13+00:00"
generator: "netsis-scraper 1.0.0"
---
# Fon İşlemleri

Fon işlemleri hakkında ayrıntılı bilgiye bu dokümandan ulaşılır.

9.0.49 seti ile birlikte Logo Netsis ERP'de fon alış/satış takibi desteklenmiştir. Bu destek kapsamında Banka/Kayıt/Fon İşlemleri menüsü altında yeni ekranlar eklenmiştir.
Fon takibini banka modülü üzerinde yapabilmek için öncelikle fon hareketlerinde kullanılacak banka tanımlanır. Bunun için Banka Hesap Kayıtları ekranında Hesap Tipi sahasına Fon Hesabı seçeneği eklenmiştir. Hesap tipi fon hesabı seçilen banklalar için Banka Hesap Bilgi-2 sayfasında Fon Kar M.K. ve Fon Zarar M.K alanları aktif hale gelir. Fon alış-satış işlemlerinden doğan kar/zarar tutarının muhasebe kaydının oluşması için bu alanlar doldurulur.
![](../_assets/eabdc38f601ab96b3f6d.png)

Fon hareketlerinin atılacağı banka tanımlandıktan sonra takibi yapılmak istenilen fon tanımlamasına geçilir.

**Fon Tanımlama**

Fon Tanımlama ekranına Banka\\Kayıt\\Fon İşlemleri menüsünden ulaşılır. Netsis ERP'de takibi yapılacak fonun tanımlandığı ekrandır. Fon tanımlandıktan sonra fon alış-satış işlemi yapılabilir.

![](../_assets/80772c3b303e1fe25079.png)

**Fon** **Alış-Satış**
Fon tanımlama ekranından tanımlanan fonlar için alış ve satış işlemlerinin takip edildiği ekrandır. Banka\\Kayıt\\Fon İşlemleri menüsünden ulaşılır. Ön Sorgulama ve Fon Alım – Satım Bilgileri Ekranı olmak üzere iki ekrandan oluşur.

![](../_assets/33fe2b8f0f9f3322658a.png)

Ön Sorgulama Ekranı
**Referans** **No:** Ekran ilk açıldığında sıradaki banka referans kodu dolu olarak gelir. Kullanıcı farklı bir referans numarası verebilir.
**İşlem** **Tipi:** Yapılacak olan işlemin tipi (alış veya satış) seçilir.
**Fon** **Banka** **Hesap** **Kodu:** Rehbere Banka Hesap Kayıtları ekranında hesap tipi Fon Hesabı olarak tanımlanan bankalar gelir. Fon alış-satış hareketlerinin atılacağı bankadır.
**Vadesiz Banka Hesap Kodu:** Rehbere Banka Hesap Kayıtları ekranında hesap tipi Vadesiz Hesap olarak tanımlanan ve fon banka hesap kodu ile aynı banka ana koduna sahip bankalar gelir. Fon alış-satış işlem tutarlarının aktarılacağı banka hesabıdır.
Kural:Kayıt silme işleminde silinecek kayıt bir alış işlemi ise içinde bulunan fonların dip bakiyesi eksi miktara düşecekse "ZZZ fonunun bakiyesi negatif olacağı için işlem gerçekleştirilemedi" uyarısı alınır. Bu durumda öncelikle bağlı satış işlemleri silinmelidir.

Kural:Mükellef düzenleyen bilgilerindeki "E-Defter oluşturulan aya ait belgelerde değişiklik yapılmasın" parametresi işaretli ise defter gönderilmiş aylara ait fon alış-satış işlemleri üzerinde yeni kayıt, silme ve değişiklik ve "Fon Kar/Zarar Hesaplama" işlemleri yapılamaz.
F5 ile Fon Alım-Satım Bilgileri ekranına geçilir.

Fon Alım-Satım Bilgileri Ekranı

![](../_assets/adaba6c94f2e5b756602.png)

**Fon** **Kodu:** Ön sorgulamada seçilen Fon Banka Hesap Kodu ile aynı banka ana koduna sahip fon tanımlarının geldiği alandır. Bu alandan fon alış-satış işlemi yapılacak fon kodu seçilir.
**Birim** **Fiyat:** İşlem görecek fonun birim fiyatı girilir.
**Adet:** İşlem yapılmak istenen adet bilgisi yazılır. Eğer işlem tipi satış ise fonun ön sorgulamadan seçilen fon bankasında bulunan bakiye miktarı kontrol edilir. Bakiye miktardan fazla satış yapılması engellenir.
**Kar/Zarar:** Bu alan her zaman pasiftir. Satış işleminde ilgili fondan kar ediliyor ise Kar, zarar ediliyor ise
Zarar olarak alan adı değişir ve kar/zarar tutarı pasif olarak bilgi amaçlı görüntülenir.
**Kar/Zarar** **Hesap** **Kodu:** Bu alan yeni kayıt sırasında fon tipli banka hesabının Fon Kar M.K ve Fon Zarar M.K alanlarında yazılan muhasebe kodları ile otomatik olarak doldurulur. Kullanıcı isterse farklı bir hesap kodu seçebilir.
**Komisyon/Stopaj:** İşlem üzerinden bir komisyon/stopaj hesaplanacaksa bu alan işaretlenir.
![](../_assets/375bd7b7d1e8945bc05a.png)

Alış işlemlerinde alan adı komisyon, satış işlemlerinde ise Stopaj olarak görünür. Alış işleminde alış tutarı üzerinden belirlenen oranda bir komisyon hesaplanır. Satış işleminde ise eğer ilgili satış işleminden bir kar elde edilmiş ise, bu kar üzerinden yazılan oranda bir stopaj vergisi hesaplanır.
**Komisyon/Stopaj Hesap Kodu:** Komisyon/stopaj tutarının aktarılacağı muhasebe hesap kodu seçilir. Satış işlemlerinde bu alana Banka Şube Bazında Parametreler ekranındaki Stopaj Muhasebe Kodu, alış işlemlerinde ise Komisyon Muhasebe Kodu varsayılan olarak getirilir. Kullanıcı isterse farklı bir hesap kodu seçebilir.
**Komisyon/Stopaj** **Oran:** Komisyon/stopaj oranının girileceği alandır.
**Tutar:** Komisyon/stopaj seçimi işaretli olan referanslar için fon tutarı üzerinden hesaplanan komisyon/stopaj tutarının pasif olarak gösterildiği alandır.
**BSMV:** Bu seçenek sadece alış işleminde komisyon varsa aktif olur.
**BSMV** **Hesap** **Kodu:** BSMV tutarının aktarılacağı muhasebe hesap kodu seçilir. Bu alana Banka Şube Bazında Parametreler ekranındaki BSMV Muhasebe Kodu varsayılan olarak getirilir. Kullanıcı isterse farklı bir hesap kodu seçebilir.
**BSMV** **Oran:** BSMV oranının girileceği alandır.
**Tutar:** BSMV seçimi işaretli olan referanslar için komisyon tutarı üzerinden hesaplanan BSMV tutarının pasif olarak gösterildiği alandır.
Tüm alanlar doldurulduktan sonra kayıt gride atılır. Aynı referans içerisine birden fazla fon işlemi Satır Ekle
butonu ile eklenebilir. Tüm satırlar eklendikten sonra Kaydet butonuna basılır.

**Kaydet**

Fon alış kaydetme işlemi sırasında ön sorgulamada seçilen vadesiz banka hesap kodunda fon tutarı kadar çıkış, fon banka hesap kodunda ise bu tutar kadar giriş hareketi oluşur.
Satışlarda ise ön sorgulamada seçilen vadesiz banka hesap kodunda satış tutarı kadar giriş, fon banka hesap kodunda ise çıkış hareketi oluşur.
Fon alış-satış, kar/zarar hesaplama işlemlerinde genel tarih kilidi, modül ve program bazında tarih kilidi kontrolü mevcuttur. Belgede belirtilen işlem tarihinin açık tarih aralığında olması gerekir. Aynı zamanda fon işlemleri iş akış kayıtları aracılığı ile onaya tabii tutulabilir.

**Fon Kar/Zarar Hesaplama**

Kar/zarar hesaplaması fon satış tarihine göre yapılır. Fon satış tarihine bakılarak, fon satış miktarı FIFO mantığı ile fon alış miktarları ile eşleştirilir. Kar/zarar, fon satış miktarının eşleştiği alış birim fiyatı üzerinden hesaplanan yeni tutar ile ilk satış anındaki tutar arasındaki farktır.

## ![](../_assets/1746ed232db4cd6b2e5f.png)

Ekran ilk açıldığında varsayılan olarak gelen ay/yıl bilgisi en eski işleme ait işlem tarihidir. Gelen tarih itibari ile tüm kar/zarar hesaplamaları tekrar yapılacak ve banka-muhasebe kayıtları güncellenecektir. Kullanıcı isterse bu tarihi değiştirebilir ancak seçtiği ay öncesinde fon satışı olmasına rağmen kar/zarar hesaplatılmamış kayıtlar varsa kullanıcı uyarılarak işlem sonlandırılır.

![](../_assets/40959386920f0616bd3c.png)

Fon satış tutarları FIFO eşleşmesi ile bulunan kar/zarar tutarına göre yeniden oluşur. Bu doğrultuda fon satış işlemine ait yevmiye fişi de revize edilir. Revize edilen yevmiye fişinde fon banka hesabı fon satış tutarı kadar çalışırken, işlemden kar doğduysa fon alış-satış kaydında girilen kar hesap kodu, zarar doğduysa zarar hesap kodu kar/zarar tutarı kadar çalışır.
**Fon** **Hareketleri**
Fon kodu bazında hareketlerin izlenebileceği ve link aracılığı ile gösterilen veriye ait detaylara ulaşılabileceği ekrandır. Fona ait tüm alış satış işlemleri ve bu işlemler sonrasında hesaplanan kar izlenebilir.

![](../_assets/929095b63a2d550820e7.png)

**Banka** **Fon** **Hareketleri** **Dökümü**
Fonlara ait tüm hareketler bu rapor aracılığı ile izlenebilir.
![](../_assets/f0fbd1d17acc3b362b17.png)

**Örnek** **senaryo**
01.10.2023 tarihinde birim fiyatı 29,103263 liradan 1000 adet, 10.10.2023 birim fiyatı 29,433408 liradan 2000 adet fon satın alınmıştır. 12.10.2023 tarihinde fonların 1500 adeti birim fiyatı 29,475958 liradan satılmıştır.

1-Fon hesabı ve fon tipi tanımlama

Hesap tipi fon hesabı olan banka ve bu banka ana kodu ile aynı banka ana koduna sahip fon tanımlaması yapılır.

![](../_assets/2df54ab6b723161eff27.png)

2-Fon alış işlemleri

01.10.2023 tarihinde birim fiyatı 29,103263 liradan 1000 adet, 10.10.2023 birim fiyatı 29,433408 liradan 2000 adet fon satın alınır.

## ![](../_assets/d74ad147f80d248c6d87.png)

İşlem sonrasında fon banka hesabı ve bağlı muhasebe kodu fon alış tutarı kadar borç, vadesiz mevduat hesabı ve bağlı muhasebe kodu alacak çalışır.

![](../_assets/b111b12b7bda4bba5d15.png)

NOT:Stopaj,BSMV,Komisyon gibi tutarlar karşılık olarak vadesiz mevduat hesabını çalıştırır.

3-Fon satış işlemleri
12.10.2023 tarihinde fonların 1500 adeti birim fiyatı 29,475958 liradan satılır.
![](../_assets/dafb8b394b88aadbd650.png)

İşlem sonrasında fon banka hesabı satış tutarı kadar alacak, vadesiz mevduat hesabı ise borç çalışır.

4-Fon Kar/Zarar Hesaplama

Satılan fonların FIFO yöntemi ile alış işlemi ile eşleştirilip kar/zarar hesaplanmasını ve satış sonrası oluşan hareketlerdeki tutarların bu eşleşmelere göre güncellenerek kar/zarar tutarının satış hareketine yedirilmesini sağlar. Bu bağlamda eşleşmelerin ve yeni tutarların aşağıdaki gibi olması beklenir.

![](../_assets/ed00a702c039fd0d82da.png)

Alış – satış işlemleri Ekim ayında yapıldığı için Kar/Zarar Hesaplama Ekim ayı için çalıştırılır.

![](../_assets/1746ed232db4cd6b2e5f.png)

İşlem 1500 adet satışı FIFO yöntemi ile alışlarla eşleştirir. 01.10.2023 tarihindeki 1000 adet alış öncelikli olarak kullanılır. 1000\*29,103263 üzerinden 1000 adetin maliyeti 29103,263 bulunur. Kalan 500 adet için bir sonraki alış hareketi olan 10.10.2023 tarihindeki 2000 adete başvurulur. 500\*29,433408 üzerinden 500 adetin maliyeti 14716,706 olarak bulunur. 1500 adet fon satışı için toplam maliyet 43419,967 bulunurken satış tutarı 44213,937 olduğu için aradaki fark olan 393,97 lira kar olarak işlenir.
İşlem sonunda fon banka hesabındaki çıkış tutarı 43419,967 olarak güncellenirken, vadesiz mevduat hesabına gerçek satış tutarı olan 44213,937 lira aktarılır. Böylece fon alış anında vadesiz hesaptan çıkan tutarın üstünde bir girişle kar vadesiz hesaba aktarılmış olur. Oluşacak yevmiye fişine ise vadesiz hesap muhasebe kodu 44213,937 lira borç çalışırken, fon hesabı muhasebe kodu 43419,967 alacak, kar hesap kodu 393,97 lira alacak çalışır.

![](../_assets/fa72e7bdb0a7372397f4.png)

Kar/Zarar hesaplama işlemi sonrasında oluşan yevmiye kaydı

Fon satışı anında oluşan yevmiye fişi silinir yerine yine fon satış tarihine ait kar/zarar kaydına göre düzeltilmiş tutarların yer aldığı yevmiye fişi oluşur.
![](../_assets/8b19854e6ddec8fcd637.png)

İşlemler sonrasında fon alış-satış bilgileri ekranından satış işlemine ait kar/zarar izlenebilir.

![](../_assets/4f8eee4ac79e873c2ebf.png)
