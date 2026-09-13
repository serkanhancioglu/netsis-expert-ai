---
title: "Netsis İskonto-İştira Kredi"
page_id: "50690702"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis İskonto-İştira Kredi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis İskonto-İştira Kredi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTQ0OGFkYTllLWYzMWMtNDg3Ny1hYTllLTIzMTA4MDAyYmRjOCZsaW5rPWUyOWUxMzEwLWNmZDctNGJiZC05MzE2LTc2MDg3MjUzY2M3NiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=448ada9e-f31c-4877-aa9e-23108002bdc8&link=e29e1310-cfd7-4bbd-9316-76087253cc76&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-iskonto-istira-kredi_80090272_50690702.html"
source_version: "2022-11-02T16:09:05.857+03:00"
source_bytes: 2098658
fetched_at: "2026-09-13T04:25:11+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis İskonto-İştira Kredi

Netsis İskonto-İştira Kredi ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Bankacılık terimi olarak **İskonto kredisi**, senet/çek borçlusunun banka şubesi ile aynı belediye sınırları içerisinde ikamet etmesine istinaden verilen kredidir. Senet-çek borçlusunun, banka şubesi ile farklı belediye sınırlarında ikamet etmesi durumunda ise aynı kredi **iştira kredisi** olarak adlandırılır. Netsis ERP tarafında teminata verilmiş olan senet/çeklere istinaden kredi çekilebilmesi desteklenmektedir.
Çekilecek kredi tutarını karşılayacak kadar ya da daha fazla tutarda çek/senedin kredi hesabına bağlanarak kredi açılışı sağlanır. Ve çek/senet ödeme işlemleri yapıldıkça kredi hesabı kapanır.

#### Tanımlar

Öncelikle kredinin takip edileceği Nakit-İskonto (İştira) tipli ve çekilen tutarın aktarılacağı vadesiz mevduat tipli iki banka hesabı tanımlanmalıdır.
![](../_assets/d6912fdaa236fa3a8a63.png)
Tanımlanan Nakit Kredi-İskonto(İştira) hesabı teminatta olan senet/çeklerin bağlanarak kredinin açılacağı hesaptır. Vadesi gelmemiş çek/senetlere istinaden bu hesaptan çıkış yapılacağı için kredi açılışında alacaklanır, çek/senet tahsil işlemleri yapıldıkça borçlanarak kapanır. Tanımlanan vadesiz mevduat hesabı çekilen kredinin aktarıldığı hesaptır. Çekilen krediden hesaplanan kesintiler düşüldükten sonra ele geçen para vadesiz mevduat hesabına aktarılır.

#### İskonto/İştira Kredi Açma

Banka/İşlemler/İskonto-İştira Kredi Açma ekranından kredinin açılış işlemi yapılmaktadır.
![](../_assets/402a1df140295148fc21.png)
Kredi Hesabı hesap tipi Nakit Kredi-İskonto(İştira) olarak seçilmiş, kredinin açılış ve ödeme işlemlerinin takibinin yapılacağı hesaptır. Hesap kredi açılışında alacak, çek/senet ödeme işlemlerinde borç çalışır.
Vadesiz Hesap, çekilen kredinin kullanılmak üzere aktarılacağı hesaptır. Para girişi nedeni ile borç çalışır.
Faiz Oranı, çekilen krediye banka tarafından uygulanan faiz oranının girileceği alandır. Teminattaki çek/senetlerin ortalama vadesine göre banka tarafından belirlenir. Girilen oran "Kredi Tutarı" alanında yazan tutara uygulanır.
**Belge** **Türü:** Kredinin çek karşılığı mı yoksa senet karşılığı mı kullanılacağı seçilmektedir. Bir belge türü seçilip, bu türde bir belge eklendiğinde alan pasif hale gelir.
**Çek/Senet Numarası:** Krediye kaynak olarak kullanılacak teminattaki senet/çeklerin seçileceği alandır. Belge türü senet ise teminattaki senetler, çek ise teminattaki çekler rehbere gelecektir. Rehberden belge seçildikten sonra "Ekle" butonu ile seçilen belge gride atılır. Ve eklenecek diğer senet/çekler için işlem tekrarlanır.
**Ortalama** **Vade** **Günü**: Seçilen tüm çeklerin vade günü ve tutar ağırlığına göre hesaplanan ortalama vadenin izleneceği alandır.
**Çeklerin** **Toplam** **Tutarı**: Seçilen çeklerin toplam tutarının izleneceği alandır.
**Kredi** **Tutarı**: Kullanılacak kredi tutarının girileceği alandır. Bu tutar seçilen çeklerin tutarına eşit ya da küçük olabilir.
**Faiz** **Tutarı**: Kredi tutarına uygulanan faiz tutarın izlendiği alandır. Bankada belirlenen tutar hesaplanandan farklı ise manuel değiştirilebilir.
**BSMV Hesaplansın**: İşaretlendiğinde hesaplanan faiz tutarı üzerinden BSMV hesaplanacaktır **KKDF Hesaplansın**: İşaretlendiğinde hesaplanan faiz tutarı üzerinden KKDF hesaplanacaktır. **Komisyon**: Sabit bir komisyon tutarı varsa bu alana girilmektedir.
**Vadesiz** **Hesaba** **Geçecek** **Tutar**: Kredi tutarındanFaiz Tutarı - BSMV - KKDF – Komisyon düşüldükten sonra hesaba geçecek olan tutardır.
**Kalan** **Tutar:** Kredi hesabına bağlanmış çek/senetler ödendikçe bu alanda kredinin kalan borcu izlenmektedir.
**Kredi** **Kaydet**: Belirlenen tutar ve hesaplara göre kredi açma işlemini gerçekleştirir.
**Kredi İptal**: Eğer ilgili kredide seçilen senet/çekler için herhangi bir ödeme işlemi yapılmadıysa kredi için atılan kayıtlar iptal edilmektedir.
**Karşılıksız** **Çek/Senet** **İçin** **Kredi** **Kapatma**: Krediye bağlanmış olan çek/senetlerden herhangi biri için karşılıksız kaydı girildi ise o belge için krediyi vadesiz hesap ile kapatır.

**Örnek**

Aşağıdaki ekran görüntüsünde vadesine göre 10.000 TL, 1.000 TL ve 5.000 TL olacak şekilde 3 çek seçilmiş ve bu çeklerin toplamı olan 16.000 TL yerine 14.000 TL kredi kullanılmıştır. Ortalama vade tüm çeklerin ağırlığına ve vadesine göre oranlanarak 46 gün bulunmuş ve kredi tutarı üzerinden %2 faiz belirlenmiştir.
![](../_assets/402a1df140295148fc21.png)
**Faiz** **Hesaplaması**
Tutar: 14.000 TL - Gün: 46 - Faiz Oranı: 2
Faiz = (Tutar \* Faiz Oranı \* Gün) / 36000= (14.000x2x46)/36000=**35.78TL**
BSMV ve KKDF varsa bu Faiz tutarı üzerinden hesaplanacaktır.
Hesaba Geçecek Tutar = Tutar - (Faiz + BSMV + Komisyon)=14.000 - (35.78)= 13.964,22 TL
Tüm bu bilgiler doğrultusunda kredi kaydet butonuna basıldığında kredi hesabı 14.000TL Alacak
ve vadesiz mevduat hesabı 14.000TL Borç ve 35,78TL(faiz) Alacak çalışacaktır.
![](../_assets/639e23fbc69566f43572.png)
Vadesi gelip çek/senetler ödendikçe kredi hesabı borç çalışarak kapanacaktır. Aşağıdaki ekran görüntüsünde 10.000TL değerindeki çek teminatta ödenmiştir.
![](../_assets/f10c8f1a39f24c095086.png)
Bu ekranda, seçilen çek/senedin tutarı ve kredi bakiye tutarı kontrol edilmektedir. Eğer kredi bakiyesi çek/senet tutarından fazla ise ekrandaki "Virman Hesap Kodu" alanına girilen vadesiz mevduat hesabına herhangi bir tutar atılmamakta ve tüm tutar krediyi kapatmaktadır. Ekrandaki "Tahsil Masrafları" alanı ise masraf zaten kredi açılışında hesaplandığı için pasif olmaktadır. Ancak çekin tutarı, kredi bakiyesinden fazla ise önce kredinin kalan tutarı kapatılacak, ardından senet/çekten kalan tutar "Virman Hesap Kodu" alanında seçilen vadesiz mevduat hesabına normal tahsilat işlemi gibi aktarılacak ve vadesiz hesaba gidecek tutar içerisinde bir masraf olabileceği için "Tahsil Masrafları" alanı aktif olacaktır.
10.000TL kredi bakiyesinden küçük olduğu için direk kredi hesabı çek tutarı kadar borçlanmıştır.
![](../_assets/1edecac1c700816aa096.png)
Not: Kalan kredi bakiyesi için yine kredi açılışında bağlanmış olan 1.000TL'lik çek için ödeme işlemi yapılmış ve kredi bankasının bakiyesi 3.000 TL kalmıştır.
Krediye bağlanan son çek olan 5.000 TL'lik çek kalan kredi bakiyesinden büyük olduğu için tahsili anında "Tahsil Masrafları" alanı aktif olacaktır.
![](../_assets/d1c505e4002639c12f80.png)
Yukarıdaki işlem sonrasında 5.000TL'nin 3.000TL'si kredi hesabına, kalan 2.000 TL'si ise "Çek Tahsil Dekontu" ekranında seçilmiş olan "Virman Hesap Kodu" alanındaki vadesiz mevduat hesabına aktarılacaktır.
![](../_assets/25a3114e880ac815fd6c.png)
Kredi bakiyesi bu son ödeme ile kapandığı için artık bu referanstaki kredi çağırıldığında aşağıdaki uyarı alınacaktır.
![](../_assets/00f0d013f9302c7472e6.png)

#### Krediye bağlanan bir çek/senedin teminatta karşılıksız çıkması

Teminattaki senet ya da çekler banka tarafından protesto/karşılıksız işlemi görebilir. Bu durumda karşılığında kredi kullanılan bu çek ya da senet için kredi yükümlülüğü krediyi çeken firmaya aittir, yani bankaya krediden dolayı karşılıksız çek/senet tutarı kadar ödeme yapması gerekmektedir.
Ekran görüntüsünde kredinin kalan bakiyesi 3.000 TL'dir.
![](../_assets/7dc3c14bb27b1eaec7a1.png)
Yukarıdaki çeklerden 5.000TL için karşılıksız çek kaydı girildiğinde artık bu kredinin kalan bakiyesi için bu çekin kullanılması mümkün olmayacaktır. Bu nedenle çek karşılıksız dekontu düzenlendikten sonra, İskonto/İştira Kredi Açma ekranındaki "Karşılıksız Çek/Senetler İçin Kredi Kapatma" butonuna tıklanmalıdır. Buton tıklandığında aşağıdaki ekran açılacaktır.
![](../_assets/44a9f7085a83275fd26e.png)
"Kredi Kapat" butonuna tıklandığında, kredi bakiyesi "Vadesiz Hesap" alanında seçilen vadesiz mevduat hesabı kullanılarak kapatılacaktır.
![](../_assets/94cc57b747609ddda93f.png)
