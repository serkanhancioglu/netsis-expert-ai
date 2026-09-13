---
title: "Yardımcı Servis Dağıtım Fişleri"
page_id: "80088373"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Yardımcı Servis Dağıtım Fişleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Yardımcı Servis Dağıtım Fişleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTUyZGFjMDQwLThjNmItNGVlOC05YzIzLTJjYzRlMjdhMGIwMCZsaW5rPTU5MDUwMmRhLTZkZjAtNGViOS04NzJmLTQ5Mjg5ODg4OWYxMiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=52dac040-8c6b-4ee8-9c23-2cc4e27a0b00&link=590502da-6df0-4eb9-872f-492898889f12&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "yardimci-servis-dagitim-fisleri_90669620_80088373.html"
source_version: "2022-11-02T14:38:04.120+03:00"
source_bytes: 540068
fetched_at: "2026-09-13T04:24:06+00:00"
generator: "netsis-scraper 1.0.0"
---
# Yardımcı Servis Dağıtım Fişleri

Yardımcı Servis Dağıtım Fişleri ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Dağıtım fişi oluşturma işleminin genel işlevi, hesap içerisinde ilgili aydaki bakiyenin farklı hesaplara oran ya da miktar bazında dağıtılmasıdır. En yoğun kullanım alanı gider hesaplarıdır. 730 genel üretim giderlerinin içinde üretimle ilgili direkt ve endirekt giderler vardır. Endirekt giderlerin hangi üretim gider yerinde ne kadar kullanıldığı belli değildir. Örneğin elektrik tüketimi endirekt üretim gideridir. Gelen fatura 730 hesaba işlendikten sonra fabrikanın bölümlerinde yapılan harcama oranlarına göre dağıtılması bu uygulama ile sağlanabilir.

**Dağıtım Tablosu**

Dağıtım tablosu ekranı üzerinden kaynak hesaplar, dağıtılacak hesaplar ve dağıtım oranları gibi detaylar belirlenmektedir.

![](../_assets/959ca50507ff8f699915.png)

**İşlem Sıra No**

İşlem sıra no, girilen işleme kullanıcılar tarafından verilen sıra numarasıdır. Her dağıtım kaydı için bir işlem sıra numarası tanımlaması yapılmalıdır. Birden fazla defa aynı işlem sıra numarası kullanılamaz. Dağıtım fişi oluşturulurken bu sıra numarası kısıtı ile oluşturulabilir.

**Fiş No**

Farklı işlem sıra numarası ile girilmiş dağıtım kayıtlarının aynı dağıtım fişine yazılabilmesi için kullanılacak numaradır. Aynı fişe yazılacak dağıtım işlemleri için kullanılan fiş numarası, birden fazla işlem sıra numarasında kullanılabilir. Böylece, dağıtım fişi oluşturulurken aynı fiş numarasına ait dağıtım işlemleri kümüle edilerek aynı fişe aktarılacaktır.

**Kaynak Kodu**

Dağıtımı yapılacak olan hesap kodunun girileceği sahadır. Bu sahaya ana, grup ya da muavin kodu girilebilir. Ana hesap girildiğinde ana hesabın, grup hesap girildiğinde grup hesabın, muavin hesap girildiğinde ise muavin hesabın Borç/ Alacak bakiyesi, dağıtım kodu sahasında girilen hesaba yansıtılacaktır.

**Kaynak Ref.Kodu / Kaynak Proje Kodu**

Kaynak referans kodu ve proje kodu, referans ve proje uygulamalarının kullanıldığı durumlarda kaynak hesaptan aktarılacak bakiyenin proje ya da referans bazında belirlenmesi sağlanabilir. Boş geçilmesi halinde hesabın toplam bakiyesi baz alınacaktır.

**Dağıtım Kodu**

Dağıtım kodu, Kaynak kodunda girilen hesabın borç veya alacak bakiyesinin transfer edileceği hesaptır. Bu sahaya sadece muavin hesap kodu girişi yapılabilir. Aynı kaynak kodu için birden fazla dağıtım kodu tanımlanabilir.

**Oran**

Oran, kaynak kodunda girilen hesabın yüzde bazında dağıtımının yapılabilmesi için sayısal olarak girilecek oran bilgisi sahasıdır. Kaynak hesap bazında oranlar toplamı 100 olmalıdır. Kaynak koduna göre oran bazında girilen bilgilerin listesi, kaynak oran/miktar denetim listesi bölümünden alınabilir.

**Alacak Kodu**

Alacak kodu, dağıtım kodunda girilen hesaba aktarılan borç veya alacak tutarının karşı hesabını oluşturacak olan hesabın, yani alacak veya borç tarafını oluşturacak hesabın kodunun girileceği sahadır. Bu sahaya sadece muavin hesap kodu girilebilir. Program dağıtım fişi oluşturma bölümünde kaynak hesap borç bakiyesi veriyor ise alacak koduna alacak, kaynak hesap alacak bakiyesi veriyor ise alacak koduna borç yazacaktır.

**Miktar**

Miktar, oransal dağıtım yerine sabit bir tutarın dağıtım hesabına aktarılması için tanımlanabilir.

**Açıklama**

Girilen dağıtım için istenilen açıklamanın girilebileceği sahadır.

Ekran görüntüsündeki örneği bu bilgiler ışığında yorumlarsak; 730-00-001 hesabın proje kodu 1, referans kodu 1 olan kayıtlara ait bakiyesi 730-01-001 hesaba %10, 730-01-002 hesaba %30, 730-01-003 hesaba %40, 730-01-004 hesaba %20 oranında aynı proje ve referans kodları ile aktarılacaktır.

**Dağıtım fişi oluşturma**

Dağıtım tablosu oluşturulduktan sonra dağıtım fişi oluşturma işlemi ile tanımlanan tablonun detaylarına uygun fiş oluşturulması için dağıtım fişi oluşturma işlemi yapılır.

![](../_assets/d4e87f09d1b9310dca43.png)

**Fiş Tarihi**

Fiş tarihi, dağıtım fişinin oluşturulması istenen tarihin, gün, ay ve yıl olarak girileceği sahadır. Program bu bölümde girilen ay kodunu baz alarak ilgili aydaki kaynak hesaplara ait borç/alacak bakiyelerini dağıtacaktır. İlgili aydan daha önceki aylarda dağıtım yapılmamış dahi olsa, sadece bu sahada girilen ay kodu için dağıtım yapılacaktır.

**Fiş No**

Dağıtım kayıtlarının aktarılacağı yevmiye fişinin, kullanıcı tarafından verilen numarasıdır. Bu sahaya girilen fiş numarası önceden mevcut ise program "Fiş Mevcut Ekleme Yapılacak mı?" ikazı vererek onay isteyecektir. Buradaki amaç parça parça yapılan dağıtımların istenildiği durumda aynı fişte toplanabilmesidir. Boş geçildiğinde sıradaki fiş numarası kullanılacaktır.

**Başlangıç İşlem Sıra No / Bitiş İşlem Sıra No**

Dağıtım Tablosu bölümünden girilen işlem sıra numarasına göre kısıt verilebilmesi için başlangıç- bitiş sıra no aralığı kullanılmaktadır.

**Başlangıç Dağıtım Fiş No / Bitiş Dağıtım Fiş No**

Dağıtım Tablosu bölümünden girilen fiş numarasına kısıt verilebilmesi için başlangıç – bitiş fiş no kısıtı kullanılmaktadır.

**Fiş Açıklama**

Dağıtım Fişi Oluşturma bölümü çalıştırılarak oluşturulan yevmiye fişlerinin açıklama sahalarına aktarılacak olan bilgidir.

**Dağıtım Türü**

Yapılacak dağıtımın oransal mı, yoksa miktarsal mı olduğunun belirlendiği alandır.

**Proje Kodu Kontrolü Yapılsın**

Proje kodu kontrolü yapılsın, eğer proje kodu uygulaması varsa ve dağıtım fişi oluşturma işleminde proje kodu kontrolünün yapılması isteniyorsa işaretlenmesi gereken parametredir.

Dağıtım fişi oluşturma bölümündeki işlemler bittiğinde fiş no sahasında girilen numaraya, fiş tarihi sahasında belirtilen tarihe, işlem tipi sahasında ve fiş numarası sahasında girilen numara aralığına göre, yevmiye fişi program tarafından oluşturulacaktır.

![](../_assets/de28a57e0014cf8e3b10.png)

İlgili fişin Açıklama-1 sahasına hangi işlem sıra numarası aralığı çalıştırılmış ise bu aralık, Açıklama- 2 sahasına da fişin adı raporlanabilmesi için program tarafından atanacaktır. Eğer herhangi bir yanlışlık var ise bu fiş iptal edilerek gerekli düzeltmeler yapılıp daha sonra dağıtım fişi oluşturma işlemi tekrar çalıştırılabilir.

Oluşan fişi incelemek ve doğruluğunu kontrol etmek için dağıtım tablosundaki oran ve hesapların yanında ilgili ay için alınmış muavinden faydalanabiliriz.

![](../_assets/09111f0ab4cb571c6aad.png)

İlgili ay için muavin alındığında ilgili referans ve proje koduna bağlı tek bir elektrik faturası hareketi olduğunu ve hesabın bakiyesinin 10000 TL borç olduğunu görüyoruz. Tabloda 730-01-001 hesaba %10, 730-01-002 hesaba %30, 730-01-003 hesaba %40, 730-01-004 hesaba %20 oranında aynı proje ve referans kodları ile aktarılmasını sağlamak üzere tanım yapılmıştır.

Oluşan fişte bu dağıtımın bakiye üzerinden oranlanarak yapıldığı gözlemlenmektedir. 730-00-001 kaynak hesabına atılan alacak hareketleri ile hesap bakiyesi kapatılmış ve oran bazında belirlenen hesaplara borç hareketi atılarak aktarılmıştır.

Dağıtım tablosu tanımında alacak kodu kısmına kaynak hesap kodundan farklı bir hesap girilmesi halinde kaynak hesap kodu bakiyesi kullanılacak ancak oluşan yevmiye fişinde alacak kodu ve dağıtım kodu karşılıklı olarak çalışacaktır.
