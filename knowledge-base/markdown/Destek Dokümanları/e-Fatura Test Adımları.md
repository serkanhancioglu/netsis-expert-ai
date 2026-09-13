---
title: "e-Fatura Test Adımları"
page_id: "50680062"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "e-Fatura Test Adımları"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / e-Fatura Test Adımları"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWFmZTI0Zjg1LWY0ZjgtNDRkNS1iNDZmLWU3NjY5MjVjNDRjYyZsaW5rPTQzMTM3MWMxLWE2MDctNDU0MS1hMDQzLWE3MWRjOGYxYzRiYSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=afe24f85-f4f8-44d5-b46f-e766925c44cc&link=431371c1-a607-4541-a043-a71dc8f1c4ba&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "e-fatura-test-adimlari_82576487_50680062.html"
source_version: "2022-11-03T09:43:52.587+03:00"
source_bytes: 2624777
fetched_at: "2026-09-13T04:26:11+00:00"
generator: "netsis-scraper 1.0.0"
---
# e-Fatura Test Adımları

e-Fatura Test Adımları ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

## ![](../_assets/d5c7c5924cf26c93a6d7.png)

Bu döküman Netsis'te entegrasyon lisansına sahip, Entegrasyon çalışmalarına başlayabileceği Başkanlık tarafından kendisine bildirilen ve mali mühürleri kendilerine ulaşan mükelleflerin yerine getirmeleri gereken test çalışmalarını açıklamak amacıyla hazırlanmıştır.

Ön hazırlıklarını tamamlayan Kurumlar entegrasyon testleri için aşağıdaki sıralamayı takip edeceklerdir:

- e-Fatura Test Uygulamasına erişim sağlayacaklar.
- Gönderici Birim entegrasyonlarını test edecekler.
- Posta Kutusu entegrasyonlarını test edeceklerdir.

Bu testleri başarı ile tamamladığı Başkanlık tarafından tespit edilen kullanıcılara e-Fatura Uygulamasını entegrasyon yolu ile kullanma izni verilecektir. Bu dokümanda bahsedilen testlere başlamadan önce, kullanıcının bilgi işlem sisteminin Netsis setindeki son e-Fatura uygulaması "test" parametresi işaretlenerek kurulumunu yaptığını kabul etmektedir. Gelir idaresinin açıkladığı test adımları [{+}](http://www.efatura.gov.tr/dosyalar/kilavuzlar/e-FaturaTestPlani.pdf)[http://www.efatura.gov.tr/dosyalar/kilavuzlar/e-FaturaTestPlani.pdf+](http://www.efatura.gov.tr/dosyalar/kilavuzlar/e-FaturaTestPlani.pdf+) adresinde detaylı olarak belirtilmektedir. Dokümanda ilk 4 bölüm e-fatura uygulamasını özetlemektedir. 5., 6. ve 7. bölümlerde ise Netsis uygulamasından yapılması gereken adımlar bulunmaktadır.

Test adımlarına geçilmeden önce mutlaka hem Netsis web servislerinin kurulu olduğu makinede hem de faturaları mühürleyip gönderme işlemini yapan Netsis istemci makinesinde aşağıdaki adrese girilip sayfanın açılıp açılmadığı kontrol edilmelidir. [{+}](https://merkeztest.efatura.gov.tr/EFaturaMerkez/services/EFatura?wsdl)[https://merkeztest.efatura.gov.tr/EFaturaMerkez/services/EFatura?wsdl+](https://merkeztest.efatura.gov.tr/EFaturaMerkez/services/EFatura?wsdl+) Bu link her iki makineden de açıldığında aşağıdaki gibi bir sayfa gelmiyorsa, bu durumda test tanım formlarında belirtilen IP ve servis uç noktası adreslerinin GİB tarafında düzeltilmesi gerekmektedir. Sayfa her iki makineden de düzgün bir şekilde açılıyorsa test adımlarına başlanabilir.

#### Gönderici Birim ve Posta Kutusu Testleri

e-Fatura Uygulamasında **Gönderici** **Birim**, Merkez ve **Posta** **Kutusu** olmak üzere 3 temel rol bulunmaktadır. Bu rollerden **Gönderici Birim e-fatura göndermeyi, Posta Kutusu e-fatura almayı**, Merkez ise Posta Kutusu ile Gönderici Birim arasındaki iletişimi sağlamaktadır.

#### Gönderici Birim Çalışma Testleri

Entegrasyon başvurusu onaylandığında Gelir idaresi ilgili mükellef için test amaçlı bir kullanıcı yaratmaktadır. Bu kullanıcı ile Gelir idaresinin test portalına [{+}](https://gbpktest.efatura.gov.tr/efatura/)[https://gbpktest.efatura.gov.tr/efatura/+](https://gbpktest.efatura.gov.tr/efatura/+) giriş yapılabilmelidir.

![](../_assets/dcd2cb98e487f3f2b198.png)

Bu kullanıcı bilgisinin Netsis veritabanındaki efatcari tablosunda tutulan e-fatura mükellefleri listesine **manuel** eklenmesi gerekmektedir. Bu işlemden sonra test kullanıcısının vergi numarasıyla Netsis fatura modülünde satış faturalarını kesmek için cari kart tanımlanması, unvan adres ve vergi numarası bilgilerinin girilmesi gerekmektedir.

![](../_assets/32ef405b1819473e1ae2.png)

Bu tanımlamalar yapıldıktan sonra Netsis fatura modülünden yukarıda tanımladığımız test carisine fatura kesilip, e-fatura gönderme işlemi yapılmalıdır. Bu işlem sonucunda Netsis fatura modülündeki e-fatura işlemleri/**giden** **kutusunda** ilgili faturanın başarıyla iletildiği görülmelidir.

![](../_assets/df9680a167ff9a806679.png)![](../_assets/9f8ab079bc05e4bd38db.png)

Benzer bir kontrolde gelir idaresinin test kullanıcısı için girilen test portalının **gelen kutusunda** ilgili fatura izlenmelidir.

#### Gönderici Birim Performans Testleri

Yukarıda belirtilen şekilde Netsis ve test portalı kayıtları düzgün oluştuğu teyit edildikten sonra performans testlerine geçilebilir.

Bu test adımlarında aşağıda belirttiğim sayıda Netsis'te test carisine faturalar kaydedilmelidir:

- İçerisinde 10 adet e-fatura içeren bir zarf ile gerçekleştirilmelidir.
- İçerisinde 1 adet e-fatura içeren ardı ardına 10 zarf ile gerçekleştirilmelidir. Gönderme işlemi bütün zarflar için 1 dakika içerisinde bitmelidir.
- İçerisinde 100 adet e-fatura içeren bir zarf ile gerçekleştirilmelidir.
- İçerisinde 100 adet e-fatura içeren ardı ardına 10 zarf ile gerçekleştirilmelidir. Gönderme işlemi bütün zarflar için 5 dakika içerisinde bitmelidir.

Test faturalarının oluşturulabilmesi için Netsis fatura modülündeki efatura işlemlerinde bulunan test faturası oluştur işlemi kullanılabilir.

![](../_assets/f0abae7187c0519767a9.png)

Bu ekranda sorulan numara kısmına Netsis fatura modülünden daha önce test yapılacak tarih için ve test kullanıcısı için kaydedilmiş bir fatura seçilmelidir. Bu seçimde sonra test fatura adedi kısmına hangi test adımında isek o kadarlık değer girilerek test faturaları oluşturulabilir. Test adımlarının 2. Ve 4. Adımında 10 farklı zarf oluşturulması istenmektedir. Bu amaçla Netsis'te kullanıcıya verilen test mükellefinin vergi numarasıyla 10 adet farklı cari oluşturulmalı ve bu test faturalarıda 2. Ve 4. adım için 10 farklı cariye kaydedilmelidir.

![](../_assets/0fbee0494120f11056ba.png)

Test fatura oluştur adımıyla faturalar oluşturulmuş ise; bu faturaların taslaklarının oluşturulup iletilebilmesi için toplu efatura oluşturma ekranında tip olarak API-Ara Tablo seçimi yapılmalıdır. 2. Ve 4. adımda aynı zamanda süre kısıtları olduğu için 10 farklı cari için faturalar oluşturulmalı ve aynı anda hepsi için taslak oluşturup benzer şekilde tüm taslaklar seçilip aynı anda gönderme işlemi yapılmalıdır. Performans testlerindeki her bir adımdan sonra Netsis fatura modülündeki giden kutusu ekranında mutlaka sorgula işlemi çalıştırılmalı ve gönderilen faturaların başarıyla iletildikleri izlenmelidir. Benzer şekilde GİB portalından da bu faturaların başarıyla alındığı portalın gelen kutusundan izlenmelidir.

**Netsis giden kutusu ekranında aşağıdaki şekilde durum kolonunda "BAŞARIYLA TAMAMLANDI"** **ve** **gönderim durumu kolonunda da "Zarf Başarıyla Teslim Edildi" ifadesi gönderilen tüm zarflar için** **görülmelidir.**

#### Posta Kutusu Çalışma Testleri

Posta kutusu testi ile alış faturalarının uygun bir şekilde alınıp alınamadığı kontrol edilmektedir. Dolayısıyla bu işlemler test portalından yapılmalıdır. Bu işleme öncelikle Portalın fatura oluştur menusünden test kayıdı yapılarak başlanmalıdır.

![](../_assets/06d606ba7fa92a255deb.png)

Bu ekrandan fatura kaydedilirken VKN alanına mükellefin gerçek vergi numarası (Netsis şirket parametrelerinde yazan bilgi) girilmelidir. Bununda ekrandaki zorunlu alanlar kaydedilerek fatura oluşturulmalı ve Netsis fatura modülündeki **gelen** **kutusunda** ilgili fatura izlenebilmelidir.

#### Posta Kutusu Performans Testleri

Yukarıda belirtilen şekilde test portalı ve Netsis kayıtları düzgün oluştuğu teyit edildikten sonra performans testlerine geçilebilir.

Bu test adımlarında aşağıda belirttiğim sayıda portaldan faturalar kaydedilmelidir:

- İçerisinde 10 adet e-fatura içeren bir zarf ile gerçekleştirilmelidir.
- İçerisinde 1 adet e-fatura içeren ardı ardına 10 zarf ile gerçekleştirilmelidir. Gönderme işlemi bütün zarflar için 1 dakika içerisinde bitmelidir.
- İçerisinde 100 adet e-fatura içeren bir zarf ile gerçekleştirilmelidir.
- İçerisinde 100 adet e-fatura içeren ardı ardına 10 zarf ile gerçekleştirilmelidir. Gönderme işlemi bütün zarflar için 5 dakika içerisinde bitmelidir.

![](../_assets/a0355a84ff0ffb6ccb2a.png)

Bu adımlar için portaldaki test araçlarında bulunan test alanı kullanılabilir. Bu ekranda alıcı VKN alanına mükellefin gerçek vergi numarası, alias etiketi alanına da mükellefin gerçek alias bilgisi girilmelidir. Zarf sayısı ve fatura adeti kısmınada test adımında istenen sayıda fatura adeti girilmelidir.

**Test aracından girilen belgeler daha sonra Netsis fatura modülündeki gelen kutusundan kontrol** **edilmelidir. Her bir adımdan sonra mutlaka Netsis fatura modülündeki gelen kutusu ekranındaki** **sorgula işlemi yapılmalıdır ve her bir zarf için durum kolonunda "ZARF BAŞARIYLA İŞLENDİ"** **ve** **Gönderim** **durumu** **kolonunda** **"Zarf** **başarıyla** **teslim** **alındı"** **ifadesi** **görülmelidir.**

#### Gönderici Birim ve Posta Kutusu Hata Testleri

Bu test adımlarında Gelir idaresi hem test kullanıcısı hemde mükellef adına hatalı test faturaları

oluşturup göndermete ve bu faturaları uygun sistem yanıtlarının dönülmesi beklenmektedir. Bu test adımları için Netsis uygulaması içinden herhangi bir çalışma yapılmasına gerek yoktur, bu çalışmalar web servisleri üzerinden yapılmaktadır.

#### Ticari Fatura Senaryosu Testleri

##### Gönderici Birim Testleri

Ticari fatura senaryosu gönderici birim testlerinde entegre olacak kurumun ticari fatura oluşturması ve göndermesi ile posta kutusundan gelecek uygulama yanıtını alabilmesi, doğrulayabilmesi ve ilgili uygulama yanıtı için sistem yanıtı gönderebilmesi test edilecektir. Gönderici birim ticari fatura testi için öncelikle test carisi olarak tanımlanan carilerin efatura senaryo tipinin TİCARİ olarak değiştirilmesi gerekmektedir. Bu işlem için efatura cari güncelle ekranında test kullanıcısının kaydı üzerinde iken sağ klikte gelen ekrandan senaryo tipini TİCARİ olarak kaydetmelidir.

![](../_assets/75ddd4c9df238e3d5deb.png)

Bu işlem tamamlandıktan sonra TİCARİ senaryo tipindeki cari kartına 2 adet satış fatura kaydı yapılmalıdır. Bu faturalar ayrı ayrı zarflanıp gelir idaresine iletilmelidir. Daha sonrada portala login olup TİCARİ tipte kaydedilen faturalardan bir tanesinin kabul bir tanesinide red edilmesi gerekmektedir.

#### Fatura Kabul İşlemi

Gelen Kutusu, Fatura Bazında Listeleme kısmından faturalar incelenir.

![](../_assets/430a503c1ff6e35ca119.png)

![](../_assets/c0421334df3b038e3f45.png)

Kabul edilecek fatura çift tıklanarak görüntülenir ve Kabul Et butonuna basılır.

![](../_assets/7cf7f076145ed53b8c71.png)

Gelen Kutusu Posta Kutusu Yanıtları menüsünden ilgili kabul uygulama yanıtı seçilerek onaylanır.

Onaylanan uygulama yanıtı seçilip Gönder butonuna basılır ve çıkan ekranda Tamam' a basılarak kabul uygulama yanıtı fatura göndericiye iletilmiş olur Fatura Red İşlemi Gelen Kutusu, Fatura Bazında Listeleme kısmından faturalar incelenir. Fatura durumu ticari fatura olanlar kabul ve ya red edilebilir. Reddedilecek fatura çift tıklanarak görüntülenir ve Reddet butonuna basılır. Gelen ekranda reddetme nedeni yazılır ve Kaydet'e basılır.

![](../_assets/593c973ff34c4095ca37.png)![](../_assets/fb4e792b6ec9093b46b2.png)

Gelen Kutusu Posta Kutusu Yanıtları menüsünde ilgili red uygulama yanıtı seçilerek onaylanır. Onaylanan uygulama yanıtı seçilip Gönder butonuna basılır ve çıkan ekranda Tamam' a basılarak kabul uygulama yanıtı fatura göndericiye iletilmiş olur.

#### Posta Kutusu Testleri

Ticari fatura senaryosu posta kutusu birimi testlerinde entegre olacak kurumun ticari fatura alabilmesi, doğrulayabilmesi ile ilgili ticari fatura için uygulama yanıtı oluşturabilmesi, mühürleyebilmesi, uygulama yanıtını gönderebilmesi ve gönderilen uygulama yanıtı için sistem yanıtlarını alabilmesi test edilecektir.

Bu işlem için portaldan Ticari tipli 2 adet fatura kaydedilmelidir. Daha sonra Netsis efatura işlemlerinde Uygulama Yanıt (Kabul/Red) ekranına girilmelidir.

![](../_assets/7ab1a873fecf55d5bc82.png)

Bu ekranda kabul veya red edilecek belgeye çift tıklayarak ekranın sağ alt tarafından tipi değiştirilebilir.

![](../_assets/f8688c84d17ec3d80f23.png)

Bu işlemden sonra ilgili belge için taslak oluşturulup gönder işlemi yapılmalıdır.

#### Diğer Testler

Netsis'te KDV oranı 0(sıfır) olan bir adet temel fatura kaydedilip gönderilmelidir.
