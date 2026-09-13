---
title: "Dinamik Kodlama"
page_id: "47084402"
product: "netsis-3-enterprise"
depth: 3
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Giriş"
  - "Dinamik Kodlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Giriş / Dinamik Kodlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTk3ZTU2OGUzLWIyN2MtNDFmMy05MDNhLTIwZjk2MWEyYTMwYiZsaW5rPTI1YTk1ZDhhLWQzNDItNDRjZS05ZjUxLTQ0YmQ4ZjE3MjgwOCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=97e568e3-b27c-41f3-903a-20f961a2a30b&link=25a95d8a-d342-44ce-9f51-44bd8f172808&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "dinamik-kodlama_94634041_47084402.html"
source_version: "2022-10-21T14:04:39.730+03:00"
source_bytes: 8764
fetched_at: "2026-09-13T04:01:24+00:00"
generator: "netsis-scraper 1.0.0"
---
# Dinamik Kodlama

Netsis ürünlerinde, kullanıcı arabirimlerinin her yerine eklenen dinamik kodlama özelliği ile, programın standart davranışını değiştirecek kod yazılması, ekranların istendiği şekilde değiştirilmesi ve yeni özellikler kazandırılması gibi programlama tekniği ile yapılacak fonksiyonların kodlanmasını sağlar. "Dinamik Kodlama" özelliğinde kodlama VBScript dili ile yapılır. VBScript kodlarını, sadece admin olan kullanıcı tanımlayabilir ve gerektiğinde geçersiz hale getirebilir.

Dinamik kod desteğinin aktif hale gelmesi için; Yardımcı Programlar → Kayıt → [Şirket/Şube Parametreleri](<../Muhasebe/Muhasebe Modülü/Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/Genel Tanımlar/Yardımcı Programlar-Şirket-Şube Parametreleri.md>) → Parametreler → "Dinamik Kod Desteği" parametresinin işaretlenmesi gerekir.

**Netsis Script Kod Desteği**

"Dinamik Kod Girişi" parametresinin işaretli olduğu durumlarda, formların sol üst köşesinde bulunan "N" Harfine tıklandığında, "Netsis Script Kod Desteği" seçeneği ekrana gelir. İlgili seçenek kullanılarak VBScript kodlama ekranı görüntülenir. "Netsis Script Kod Desteği" seçildiğinde, kod geliştirme ortamı ekrana gelir. VBScript yazılması istenen program bilgisi başlık olarak görüntülenir.

**Örneğin;** "Cari Hesap Kayıtları" bölümünde iken "Netsis Scirpt Kod Desteği" seçildiğinde, "Cari Hesap Kayıtları" için script yazılacağı anlaşılır.

İstendiği zaman, kullanıcının tanımlayacağı menüler eklenebilir ve bu menülere VBScript kodu yazılabilir veya kodlama Netsis’te bulunan Text, Radiobutton, Label gibi form özellikleri için yapılabilir.

**Örneğin;** SCRIPT isimli bir menü eklenmesi için "Menü Adı" kısmına kodlama sırasında görünmesi istenen açıklama girildiğinde, söz konusu adın başına mnCustonItem\_ eklenir. "Açıklama" kısmına yazılan değer ise ekranda görülecek menü ismidir.

**Satır Ekle:** Yeni bir menü eklemek için boş bir satır açar.

**Çizgi Ekle:** Menüler arasına yatay çizgi eklenmesini sağlar.

**Satır Sil:** Üzerinde bulunulan satırı siler.

**Hepsini Sil:** Ekranda bulunan tüm tanımlamaları siler.

**Menü Test:** Menü görünümünün test edilmesini sağlar.

**Kısıtlamaya Geç:** Kodlama ekranına geçilmesini sağlar. "Kısıtlamaya Geç" seçildiğinde, kullanılacak nesneleri sorgulayan bir ekran görüntülenir. VBScript kodu sadece eklenen menüye yazılacaksa, ekrana gelen listeden sadece TMenuItem’ın seçilmesi yeterlidir. Kullanılmayan nesnelerin eklenmesi, formun açılma hızını etkiler. Çünkü, form her açılışta buradaki nesneleri yükleyerek açılır.

Script kodlamaya geçildiğinde TMenuItem nesnesinin altında, kullanıcı tarafından eklenen mnCustonItem_VB görüntülenir. Üzerine tıklandığında, Nesne Olayı (Event) kısmında sadece OnClick seçilebilir. Yani, buraya yazılacak olan kod, kullanıcı menüye tıkladığında çalışır.

"Kod Geliştirme" kısmında yazılan kodlar "Sakla "seçeneği ile kaydedilir ve "Temizle" seçeneği ile silinir. Kod şablonu hazırlanıp kaydedilerek, daha sonra ilgili şablon ekrana getirtilebilir.

"Uygulama Global" isimli seçenek ile tüm formlarda, tüm şirketlerde ortak kullanılması istenen tanımlamalar varsa uygulama globalde tanımlanması sağlanır. Yazılan bir fonksiyon veya sub her yerde ortak olarak kullanılması istendiğinde, bu tanımlamayı uygulama global kısmında yaparak tüm modüllerde ve şirketlerde ilgili fonksiyona erişerek çalıştırılır. Söz konusu özellik ile, ortak olan bir fonksiyon tanımlamasının, kullanılacak olan her ekranda tekrar tekrar yazılması önlenir.

**Örnek**

sub mail(kime,cc,subject,ek,body)

call NETSISCORE.NetLibEMail.EPostaGonder(kime,cc,subject,ek,body)

end sub

şeklinde Uygulama Global’de yapılan bir tanımlamayı kullanıcının hazırladığı bir menüde kullanmak için:

call appglobal.mail(MAIL,"","MEKTUP","",ICERIK) şeklinde ekrana getirilmesi gerekir.

Yukarıdaki sub tanımlamasında NETSISCORE.NetLibEMail.EpostaGonder şeklinde bir tanımlama vardır. Bu tanımlama ile Netsis nesnelerinin kullanıldığı belirtilir. Nesneler hakkında bilgi almak için "Kod Geliştirme" kısmında bulunan "Nesne Tarayıcısı" kısmına tıklayarak diğer nesneler hakkında da bilgi alınabilinir. Nesnelerin neler olduğu, hangi sınıflardan oluştuğu ve tanımlanana fonksiyonlarının parametreleri, nesne tarayıcısı ile görüntülenebilir.

**Örnek 1**

"Cari Hesap Kayıtları" bölümünde, "Cari Kod" kısmında bulunan cari koda ait anlık borç ve alacak bakiyesini, cari hesabın mail adresine yollanmasını sağlayan bir uygulamanın yazılması istendiğinde aşağıdaki durumlar gerçekleşir:

- Cari Hesap Kayıtları'nda cari kodu editbox’ında bulunan değeri CARI isimli bir değişkene atılır ve Netsis’in nesnelerinden NETSISCORE.NetLibDb.GetNewQuery ile QUERY isimli yeni bir sorgu nesnesi yaratılır. SORGU değişkenine çalıştırılması istenen sorgu - TBLCAHAR tablosundan borç ve alacak toplamı ile günün tarihini çeken - yazılır ve daha sonra QUERY nesnesi ile sorgu çalıştırılır.
- Carinin ismi ve mail adresi gerektiği için, bu bilgiler de QUERY1 ile çekilir. İçerik isminde mailin içeriğini saklayan bir değişken - veritabanından çekilen verilerin de eklenmesi gerekir - tanımlanır. QUERY1 ile çekilen değerlerden CARI_ISIM sahasını içeriğe eklemek için QUERY1.fields(1).assstring tanımlaması kullanılır. Carinin e-Mail adresini eklemek için de, QUERY1.fields(0).assstring tanımlaması kullanılır ve sorgudaki ilk saha için 0 indeks’ten başlanarak veriler alınır.

ICERIK değişkeni tamamlandıktan sonra Uygulama Global’de tanımlanan mail sub’ın kullanılarak cariye mail atılması sağlanır.

**Örnek 2**

"Stok Kodu" girildiğinde, girilen koda bakılarak "Depo Kodu" alanına bir değer atılması istenebilir. Stok koduna IZM001,IZM002 gibi kodlar yazıldığında stokun depo koduna "1" yazılması, IST001,IST002 şeklinde kodlar yazıldığında depo koduna "2" yazılması, aksi durumda da "3" yazılması istendiğinde, Stok Kodu bilgisi düzenlenebilir olduğu için TDBNEdit altında bulunabilir. Yukarıdaki tanımlamaya bakıldığında Stok_kodudb’nin OnExit olayında script yazılmış. Stok koduna yazılan değerin ilk 3 hanesini alarak IZM olup olmadığı kontrol edildiğinde eğer IZM ise depo koduna "1" yazılır. Depo Kodu bilgisi de düzenlenebilir olduğu için Depo_Kodu.TEXT olarak atama yapılmış. Eğer IZM değilse kontrole devam edilerek IST olup olmadığına bakılır. Doğru ise "2", aksi durumda ise depo kodu "3" olarak belirlenir.
