---
title: "Demirbaş Entegrasyonu"
page_id: "113246898"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Demirbaş Entegrasyonu"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Demirbaş Entegrasyonu"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWQwM2M4MjlmLTZmNmYtNGFmMS1iNjJkLTllMDZjZjlkMzU0ZSZsaW5rPTQyZGJjMWE0LWU2YTMtNDQ3ZS1hMTJmLTk1MzllZjFjZGJiZiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=d03c829f-6f6f-4af1-b62d-9e06cf9d354e&link=42dbc1a4-e6a3-447e-a12f-9539ef1cdbbf&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "demirbas-entegrasyonu_113246923_113246898.html"
source_version: "2023-06-08T11:10:01.183+03:00"
source_bytes: 3012805
fetched_at: "2026-09-13T04:23:23+00:00"
generator: "netsis-scraper 1.0.0"
---
# Demirbaş Entegrasyonu

Demirbaş entegrasyonu hakkında ayrıntılı bilgiye bu dokümandan ulaşılır.

Demirbaş Yönetimi üzerinde yapılan işlemlerin Netsis Temelset tarafında muhasebe kaydının oluşturulması iki paket arasında veritabanı bağlantısı ile sağlanır. Örneğin yeni açılan bir demirbaş kartının alış belgesi Netsis Temelset tarafına Genel Dekont Kaydı olarak atılabilir. Ya da değerleme ve amortisman ayırma ile oluşan birikmiş amortisman tutarlarının, yeniden değerleme ile oluşan fon tutarlarının, demirbaş satışı ile oluşan tutarların yevmiye kayıtlarının oluşturulması mümkündür.

**Parametre Girişi**

Netsis Temelset tarafı ile Demirbaş Yönetiminin veri tabanı bağlantısı Demirbaş\\Kayıt\\Parametre Girişi ekranları üzerinden sağlanır. Öncelikle Genel sekmesinde bulunan Entegrasyon yapılsın seçeneği işaretlenir. Demirbaş şirketinin Temelset tarafında hangi şirketten veri alacağı ve hangi şirkete veri aktaracağı Veritabanı Bilgileri sekmesinden belirlenir.
![](../_assets/a6966443abb1e52eff78.png) ![](../_assets/8743ffdecf2d4358ec69.png)
Veritabanı İsmi: Netsis Temelset tarafında veri alışverişinin yapılacağı şirket ismi girilir.
Veritabanı Kullanıcı ismi: TEMELSET olarak girilir. Eğer VTGUVENLIK klasörü devre dışı bırakıldı ise sa gibi veritabanı
ismine erişimi olan bir kullanıcı adı verilir.
Veritabanı Şifresi: Standart kullanımda TEMELSET kullanıcısının şifresi yoktur. Özellikle şifrelendi ya da farklı bir kullanıcı belirtildi ise şifresi girilir.
Şube Kodu: Temelset tarafında veri alışverişinin hangi şubeye yapılacağı seçilir.
Bu tanımlar ile Netsis Temelset ile Demirbaş Yönetimi arasında haberleşme sağlanmış olur. Bu aşamadan sonra yapılması gereken hangi işlemde hangi hesapların çalışacağını tanımlamaktır.
Demirbaş yönetiminden atılan kayıtlar direk muhasebeye aktarılacaksa havuz sistemi kapatılmalı ve doğrudan aktarım açılmalıdır. Parametrelerin işaretlenmemesi halinde kayıtlar Temelset entegrasyon havuzuna düşecektir.

**Entegrasyon**

Demirbaş Bilgi Kartı ekranında demirbaşın çalıştıracağı muhasebe hesaplarını belirleyen detay kodu ve masraf kodu sahaları vardır. Bu sahalar Entegrasyon modülünde detaylandırılır.

![](../_assets/d69a625040e05ed4e2c9.png)

**Detay Kodu Tanımlama**

Demirbaş kartına bağlanan detay kodunun çalıştıracağı muhasebe hesaplarının belirlendiği ekrandır.

![](../_assets/c63d6ab34d4d724d16e7.png)
Sabit Kıymet Muh.Kodu: Sabit kıymet alış fiyatının ve alış fiyatındaki artışların aktarılacağı hesap kodudur.
Birik. Amort.Muh.Kodu: Ayrılan amortismanın aktarılacağı muhasebe kodudur.
Çalışmayan Kısım Hesabı: Dönem ortası alınan demirbaşlar için alındığı aya kadar olan kısım amortismanın aktarılacağı
muhasebe kodudur.
Değer Artış Fonu: Yeniden değerleme sonrası oluşan fon tutarının aktarılacağı muhasebe kodudur.
Faiz Girişi Hesap Kodu: Demirbaş bilgi kartından girilen değer artış/azalış tutarının aktarılacağı muhasebe kodudur.

**Masraf Kodu Muhasebe Hesapları Tanımlama**

Demirbaş amortisman tutarı birikmiş amortisman hesabını çalıştıracağı gibi gider olarak gösterileceği için karşılığında masraf hesabını çalıştırır. Demirbaş kartından masraf kodu olarak seçilen masraf kodunun çalıştıracağı hesaplar Masraf Kodu Muhasebe Hesapları Tanımlama ekranından tanımlanır.
![](../_assets/f79215b2325bfbe08dc1.png) ![](../_assets/0a6661c1d6276d90969f.png)
Masraf Muhasebe Kodu: Ayrılan amortismanın gider olarak aktarılacağı muhasebe kodudur.
Ref.Kodu/Proje Kodu: Referans ve ya proje uygulaması açık ise aktarılacak tutar için atanacak referans ve proje kodu seçilir.
Oran: Ayrılan amortisman tutarının oransal olarak farklı gider hesaplarına dağıtılması sağlanır. Masraf kodunun tüm satırlarının toplamı oran olarak 100 olacak şekilde tanımlanır.
KKEG Hesabı: Binek oto uygulamasında gider gösterilebilecek tutarlarda üst limit vardır. Üst limiti aşan kısımlar kanunen kabul edilmeyen gider olarak adlandırılır. Masraf kodu bazında bu tutarın farklı gider hesabına yazması sağlanır. KKEG için tanımlanan hesapta KKEG Hesabı parametresi işaretlenir.

**Çıkış Kodu Muhasebe Hesapları Tanımlama**

Aktife alınmış demirbaşlar demirbaş satışı işlemi ile satılır. Bu satış anında uygulama çıkış türünü sorar. Detay kodu bazında çıkış türüne göre farklı hesapların çalışması için tanımlamalar Çıkış Kodu Muhasebe Hesapları Tanımlama ekranından yapılır. Aynı detay kodu için çıkış türü bazında farklı hesaplar tanımlanabilir.
![](../_assets/983dfe667ea9581fc0ca.png)

Program çıkışları entegre ederken sabit kıymet değerinden satış işlemi sırasında girilen birikmiş amortisman ve fon tutarını düşer, aradaki fark tutarını da bu bölümden kaydedilen hesap koduna atar.

**Demirbaş Bilgi Kartı Muhasebeleştirme**

Demirbaş kartları açıldıktan sonra bu işleme ait muhasebe kayıtları Temelset tarafına atılacak bir dekont kaydı ile oluşturulur. Bu işlem için Demirbaş Bilgi Kartı ekranından Satıcı bilgisi doldurulmuş olmalıdır. Demirbaş Bilgi Kartı üzerinde sağ tık Dekont Kaydı Oluşturma menüsü seçilir.
![](../_assets/04049a3bc8102a04d54a.png)![](../_assets/a8ece83d4ce50fc42604.png)

Gelen ekrandan oluşacak olan dekontun bilgileri doldurulup Tamam butonu ile onaylanır. İşlem sonrasında Netsis Temelset tarafında bu alışa istinaden bir dekont ve bu dekonta istinaden muhasebe fişi oluşur.

![](../_assets/8f730c1a2dba9e4714f5.png)

Oluşan muhasebe fişindeki demirbaşa ait satıcı cari alacak, demirbaş kartında tanımlı olan detay koduna bağlı sabit kıymet muhasebe hesap kodu ise borç çalışır.

**Amortisman Hisse Muhasebeleştirme**

Değerleme ve amortisman ayırma işlemi sonrasında oluşan amortisman hisseleri Amortisman Hisse Muhasebeleştirme işlemi ile entegre edilir.
Örnek demirbaş 10. ayda alınmış ve 10. ay için değerleme ve amortisman ayırma işlemi çalıştırılmıştır. Demirbaş kartı üzerinden dekont oluşturma çalıştırıldığı için muhasebe mutabakat icmali sabit kıymet hesap kodu fark vermezken, birikmiş amortisman hesabında fark oluştuğunu görürüz.

![](../_assets/f6e41d510464c9640b50.png)
Bu farkı gidermek ve birikmiş amortismanı muhasebeleştirmek için amortisman hisse muhasebeleştirme işlemi çalıştırılır.
![](../_assets/48e48a456201c2a093b3.png)![](../_assets/9a8496003c91c44532a7.png)![](../_assets/dd4916db1e533aaef12e.png)

Bu işlem anında demirbaş kartındaki detay koduna bakılır ve çalışacak hesaplar belirlenir.
![](../_assets/6d376ad51906955e6c05.png)

Demirbaşın 10. ay aylık amortisman 169.317,42'dir. Bunun 152.385,68TL'lik kısmı ilk 9 aya, 16.931,74TL'lik kısmı 10.aya aittir. İşlem sonunda aşağıdaki fiş oluşur.

![](../_assets/9c9813ee15dbdaa531cc.png)

Birikmiş amortisman hesabı çalışmayan kısım karşılığı ve aylık amortisman karşılığı olacak şekilde iki satır toplamda 169.317,42TL alacak olarak çalışır.

Bunların karşılığında 16.931,74 10. ay amortismanı masraf muhasebe hesabına, 152.385,68 çalışmayan kısım karşılığı olarak detay kodunda tanımlı çalışmayan kısım hesabına borç olarak aktarılır. Bu işlem sonrasında muhasebe mutabakat icmali fark vermez.

Not: Çalışmayan kısım sadece demirbaşın alındığı ay çalışır.

![](../_assets/14c8e42dbf34d40eaa60.png)

**Yeniden değerleme varsa;**

Demirbaş yeniden değerlemeye tabii tutulduğunda amortisman tutarı dışında hem sabit kıymet bedelinde, hem birikmiş amortismanında artış olur ve fon tutarı hesaplanır. Fon tutarı detay kodu tanımlama ekranında bulunan değer artış fonu hesabını çalıştırır.

![](../_assets/4de511cc7ac3d8f88fc3.png)

Fon tutarı demirbaş sabit kıymet bedeli hesabına borç olarak işlerken, fon hesabına alacak olarak yansır. Aylık amortisman tutarı için birikmiş amortisman hesabı alacak ve masraf muhasebe kodu borç olacak şekilde karşılıklı olarak çalışır.

![](../_assets/6623c1bb3340310026b3.png)

\11. ay içinde amortisman hisse muhasebeleştirme yapıldıktan sonra alınan muhasebe mutabakat icmalinde fon tutarı da izlenir.
![](../_assets/b1f08d0ef4fcf54e9afe.png)

Raporda "A" sütunu detay koduna bağlı hesap bilgisini verir. Sabit kıymet hesap kodu, birikmiş amortisman hesap kodu ve fon hesap kodu olacak şekilde detaylandırılmıştır.

"C" sütunu demirbaş tarafındaki tutarları verir. Örneğin demirbaş modülündeki sabit kıymet toplamı, demirbaş modülündeki birikmiş amortisman toplamı ya da fon tutarı gibi.

"D" sütunu Netsis Temelset tarafında bağlı muhasebe kodunun bakiyesini çeker.

Rapor tüm detay kodlarını gezer aynı hesap kodlarını kümüle eder ve aynı zamanda tutarları da kümülatif basar. Yani birikmiş amortismanda gördüğümüz değer raporu çektiğimiz aydaki toplam amortismanı verir. Bu nedenle Temelset tarafında karşılaştırılmak istendiğinde ilgili muavinin kümülatif mizan tutarına bakılmalıdır.

Örneğin;

![](../_assets/737f17c6e464fdb88f2c.png)

**Satış Muhasebeleştirme**

Demirbaş satışı da muhasebeye kaynak teşkil eden bir işlemdir ve Satış Muhasebeleştirme işlemi ile Temelset tarafında muhasebe fişi oluşması sağlanır. Demirbaş/ Entegrasyon modülünde çıkış kodları ve bunlara bağlı hesapların tanımlanmış olması gerekir.

![](../_assets/ce605a039eae8914159e.png)

Satış işleminde çıkış kodu 1 olarak seçilmiştir. Bu nedenle çıkış muhasebe kodu olarak 1 çıkış koduna bağlı hesap çalışacaktır. Bu aşamada çıkış hesap koduna gidecek tutar birikmiş amortisman ve fon tutarı düşüldükten sonra bulunur. Fon tutarı ve birikmiş amortisman için demirbaşın bağlı bulunduğu detay kodundaki hesaplardan çıkış olur.

![](../_assets/3ec771ed88b1e3032622.png)
Birikmiş amortisman muhasebe hesabı toplam amortisman tutarı kadar borç çalışır. Demirbaş satıldığı için sabit kıymet muhasebe kodu demirbaş bedeli kadar alacak çalışır. Yeniden değerleme ile oluşan fon tutarı değer artış fonu hesabında borç hareketi atılarak çıkılır. Ve sabit kıymetten birikmiş amortisman ile fon düşüldükten sonra kalan tutar ise çıkış muhasebe koduna borç olarak atılır.
![](../_assets/3d0e76b72d47d24a1c0a.png)

**Transfer Muhasebeleştirme**

Demirbaş transferi işlemi mevcut şirketteki bir demirbaşın farklı bir şirkete aktarılmasıdır. Bu aktarımında muhasebeleştirilmesi isteniyor ise Demirbaş/Entegrasyon modülünde bulunan Transfer Muhasebeleştirme işlemi kullanılır. Bu işlem ile demirbaşın mevcut detay koduna bağlı hesaplarda biriken tutarlar işlem anında seçilecek olan yeni detay koduna taşınacak şekilde yevmiye fişi oluşur.
