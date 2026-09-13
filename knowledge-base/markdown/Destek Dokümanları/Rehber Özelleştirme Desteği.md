---
title: "Rehber Özelleştirme Desteği"
page_id: "66248558"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Rehber Özelleştirme Desteği"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Rehber Özelleştirme Desteği"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWE2YWQ2NTgxLTIyNWQtNDA1Zi04MGE0LTc1ZjJkNzY5MDFkYSZsaW5rPTk1M2ExOTc5LTM3YjYtNGU5Yy1hNzUyLWUyMDhhNjhkYjRhNiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=a6ad6581-225d-405f-80a4-75f2d76901da&link=953a1979-37b6-4e9c-a752-e208a68db4a6&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "rehber-ozellestirme-destegi_80088537_66248558.html"
source_version: "2022-11-02T14:56:08.567+03:00"
source_bytes: 210914
fetched_at: "2026-09-13T04:24:27+00:00"
generator: "netsis-scraper 1.0.0"
---
# Rehber Özelleştirme Desteği

Rehber Özelleştirme ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

#### Rehber Özelleştirme

Rehber özelleştirme desteği, Netsis'in standart rehberlerinde özelleştirme ve yetkilendirme işlemlerini gerçekleştirmeyi sağlar.
Rehber özelleştirme ile birlikte sağlanan işlemler aşağıdaki şekildedir:

- Modül ve program bazında rehber özelleştirme sağlanabilir.
- Standart rehber sorgularına kısıt verebilme sağlanabilir.
- Özel view veya tablo kullanarak standart rehberlere yeni alanlar ekleyebilme sağlanabilir.
- Kullanıcı veya kullanıcı grubu bazında rehber özelleştirerek yetki tanımlayabilme işlemleri sağlanabilir.

Rehber özelleştirme işlemleri için özelleştirme yapılmak istenen rehber açılarak rehberin sol üst köşesinde bulunan Rehber Özelleştirme menüsüne girilmelidir.
![](../_assets/ef5fc1b5c7738500e0a1.png)
Not: Rehber özelleştirme işlemleri yalnızca merkez şubede ve admin kullanıcılar tarafından yapılabilmektedir.
![](../_assets/f2fb1b2f6db5f5e951d5.png)
Açıklama alanı, özelleştirilen rehber için açıklama girilmesini sağlayan alandır.
Rehber Başlığı alanı, özelleştirilen rehberin ekranda görüntülenmesi istenen başlığın girildiği alandır. Başlık bilgisi daha sonra değiştirilebilir.
Modül/Program Ortak alanı, rehberin kullanıldığı diğer modül ve programlarda özelleştirmenin ortak olması için işaretlenebilecek alandır. Parametre işaretlenmediğinde Modül No ve Program No alanlarından özelleştirilen rehberin kullanılabileceği modül ve program numarası belirtilmelidir.
![](../_assets/8906522d6e7ef62c446d.png)
Mevcut View/Tablo İsmi alanı ile, standart rehberin hangi view/tabloyu kullandığı bilgisinin gösterimi sağlanır.
Özel View/Tablo İsmi alanı, standart rehbere, özel olarak oluşturulmuş farklı bir view veya tablodan saha eklenmesi için kullanılabilecek alandır.
Örneğin; Müşteri siparişleri ekranındaki cari rehberine T.C. Kimlik No bilgisinin eklenmesi için Özel View/Tablo alanında CASABITEKEKR view'ı seçilerek Eklenecek Alan bölümünden TCKIMLIKNO bilgisi seçilerek rehbere ekleme yapılabilir.
Not: Rehberde standart olarak mevcut alanlar alt bölümdeki tabloda Standart/Özel Alan sütununda belirtilmektedir. Bu standart alanların rehberden çıkarılmasına izin verilmemektedir.
Eklenecek Alan, Özel View/Tablo kullanılarak rehbere eklenecek sahanın seçildiği alandır.
Alan Başlığı alanı, eklenen alan için rehberde gösterilmek üzere başlık bilgisinin girildiği alandır.
NDS Tip alanı, eklenen alan için Netsis ondalık tipinin seçildiği alandır. Miktar, Oran Tutar, Döviz Tutarı, Firma Döviz, Fiyat, Kur, Döviz Fiyatı ve Yok seçenekleri arasından seçim yapılır. Ondalık tanımı olmadığı zaman "Yok" seçeneğinin seçilmesi gerekir.
Özel Sorgu Kısıt alanı, rehber açıldığında çalıştırılacak sorgunun kısıtlanabilmesi için dinamik kod yazılmasını sağlar.
Not: Rehber sorgusuna kısıtlama için yazılan ifade RESULT değişkenine atanmalıdır.
Örneğin; Cari Hesap Kartı Kayıtları ekranındaki Grup Kodu alanında carilerin bölge bilgileri bulunmaktadır. Kullanıcılar cari rehberi açtığında yalnızca kullanıcı grubu bazında yetkili olduğu bölgenin kayıtlarını görmeleri istenmektedir.
Özel Sorgu Kısıt bölümünde; *RESULT = "GRUP_KODU='EGE'" vb.* kısıtlama ifadeleri yazılarak ve kullanıcı grubu bazında yetki düzenlemesi yapılarak kullanıcının yalnızca belirtilen kısıtlara uygun kayıtları rehberde görmesi sağlanabilir.
Rehber Test seçeneği, özelleştirilen rehberin ekranda nasıl görüneceğinin izlenmesi için kullanılan seçenektir.
Kaydet seçeneği, hazırlanan rehberin kaydedilmesi için kullanılan seçenektir.
Yetki Düzenleme seçeneği, özelleştirilen rehberin kullanıcı bazında yetkilendirilebilmesi için kullanılan seçenektir. Yetki Düzenleme seçeneği bölümünde; Bana Özel, Kullanıcı Bazında, Grup Bazında ve Tüm Kullanıcılar olmak üzere 4 farklı yetki düzenleme tipi bulunmaktadır.

Bana Özel tipinde, seçilen rehberin yalnızca rehberi oluşturan kullanıcı tarafından görüntülenmesi istendiği durumda seçim yapılmalıdır.

Kullanıcı Bazında tipinde, rehberin yalnızca belirli kullanıcılar tarafından görüntülenmesi istenirse kullanıcı bazında yetki seçeneği işaretlenerek, açılan yetkilendirme listesi ekranından kullanıcılar seçilmelidir.

Grup Bazında tipinde, rehberin yalnızca belirli kullanıcı grupları tarafından görüntülenmesi istenirse grup bazında yetki seçeneği işaretlenerek, açılan yetkilendirme listesi ekranından kullanıcı grupları seçilmelidir.

Tüm Kullanıcılar tipinde, rehberin tüm kullanıcılar tarafından görüntülenmesi istendiği durumda seçim yapılmalıdır.

Örneğin; Ekran Görüntüsü-2'de bulunan ve özel sorgu kısıtı belirtilen 1 no'lu rehber için **Yetkilendirme** **Listesi** ekranından kullanıcı grup kodu "EGE" olarak seçim yapıldığında; rehberde sadece grup kodu "EGE" olan cari hesap kayıtları gösterilmektedir.
![](../_assets/84e3f7a6d039d4e8b14c.png)
