---
title: "Konaklama Vergisi Düzenlemeleri"
page_id: "100666832"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Konaklama Vergisi Düzenlemeleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Konaklama Vergisi Düzenlemeleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTBmYjQwZDRiLWQ3ZjQtNDZkMC1hMGY5LWI0MTFmNDZkY2E2NCZsaW5rPTk4NzYyMjA5LThlNWItNGY2NC04NTM3LTNiYzFiZGNiZDI0YSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=0fb40d4b-d7f4-46d0-a0f9-b411f46dca64&link=98762209-8e5b-4f64-8537-3bc1bdcbd24a&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "konaklama-vergisi-duzenlemeleri_102268933_100666832.html"
source_version: "2022-12-30T18:19:14.467+03:00"
source_bytes: 1623448
fetched_at: "2026-09-13T04:23:46+00:00"
generator: "netsis-scraper 1.0.0"
---
# Konaklama Vergisi Düzenlemeleri

Konaklama Vergisi Düzenlemeleri hakkında ayrıntılı bilgiye bu dokümandan ulaşılabilir.

01.01.2023 tarihinde aktif olacak konaklama vergisinin Netsis’de desteklenmesi için gerekli işlem adımları ve desteklenen özellikler aşağıda özetlenmiştir.

Bu uygulama kapsamında fatura kesilecekse Alış ve Satış parametrelerine eklenen Konaklama Vergisi alanında kullanıcıların “Konaklama Vergisi Hesaplanmasın” haricinde bir ek maliyet alanı seçmesi gerekmekte.

![](../_assets/b7b57d60803190aef2b3.png)

Kullanıcı burada bir ek maliyet alanı seçince alt kısmında uygulanacak olan konaklama vergisi oranı da aktif olmakta. Şu an için bu oran %2.

Bu parametre işaretlendiğinde faturaların üst bilgilerinde “Konaklama” adında bir seçenek geliyor olacak. Eğer kesilecek olan fatura konaklama vergisi ise bu seçeneğin işaretlenmesi gerekmekte.

Konaklama seçeneği işaretli ise bu belgelerin satırlarında “Özel Fiyat” alanı aktif olacaktır ve ilgili satır için hesaplanacak olan konaklama vergisinin fiyatı buraya yazılan fiyat üzerinden hesaplanacaktır.

![](../_assets/464e650b319b32e90af3.png)![](../_assets/b3b9358e5c98d7e7f917.png)

Bunun sebebi dövizli olarak belirlenen fiyatlarda otel mevzuatına göre KDV hesabının kişinin otele giriş yaptığı tarihteki kur üzerinden hesaplanması fakat konaklama vergisinin otelden çıkış tarihli kur üzerinden hesaplanması gerekliliğidir.

Bu durumda beklentimiz dövizden TL’ye çevirerek fatura kalemlerine giriş yaptıkları durumda fiyat alanına yazılan fiyat\* miktar değeri üzerinden kdv hesaplanacak ve özel fiyat \* miktar değeri üzerinden de konaklama vergisi hesaplanacaktır.

Konaklama işaretlenen fatura için her satırda konaklama vergisi olması gerekmemekte, bu tip faturalar için eğer özel fiyat alanı 0 geçilmiş ise bu satır üzerinden bir konaklama vergisi hesaplanmayacaktır.

![](../_assets/d75b2f84cb6e6362d74b.png)

Bu örnekte miktar=1 olduğu için fiyat alanına yazılan 5.000 TL üzerinden %8 kdv hesapladı = 400 TL

Ve özel fiyat alanında da 5.000 yazdığı için 5.000 TL üzerinden %2 Konaklama vergisi hesapladı = 100 TL

Faturanın toplamı 5.000 + 400 +100 = 5.500 olarak hesaplanmış oldu.

Not: Bazı durumlarda herhangi bir konaklama bedeli olmadan da otellerin müşterilerine sadece konaklama vergisini içeren bir fatura kesmesi gerekmektedir. Bu tip bir fatura kesilmek istendiğinde fiyat alanı 0 olarak geçilecek ve özel fiyat alanına konaklama vergisinin hesaplanacağı fiyat girilecektir. Bu durumda eğer başka bir fatura satırı girilmiyorsa konaklama vergisi ile faturanın genel toplamı aynı olacaktır. KDV tutarı 0 olduğu için otomatik olarak istisna kodu ilgili belgeye atanıyor olacaktır.

![](../_assets/25fb6c25b92f7c6dc45f.png)

Bu faturadan efatura/earşiv oluşturulduğunda yukarıdaki gibi hem ilgili satırda hem de belge toplamlarında konaklama vergisini görüyor olacağız.

Bu ebelgenin xml’i incelendiğinde konaklama vergisinin 0059 vergi kodu ile hem faturanın genel bilgilerinde hem de satırlarında yer aldığını görebiliriz.

![](../_assets/f0515f7a7ae044fcd10a.png)

Ayrıca gelen kutusuna düşecek olan efaturalarınızda konaklama vergili bir fatura mevcut ise gelen kutusunda alış faturası oluşturma adımında ve dekont oluşturma işlemlerinde eğer belge içinde 0059 vergi kodu geçiyorsa alış faturasındaki ilgili satırların da yukarıda belirtildiği şekilde yani özel fiyat alanı dolu ve konaklama vergisi hesaplayacak şekilde oluşturulması sağlanmıştır.

Oluşacak dekont ekranın ise 0059 vergisi için ayrı bir satır gösterilmesi desteklenmiştir.

![](../_assets/6671a2b2b437b799db6b.png)

Son olarak NetopenX ile kaydedilecek faturalarda da bu şekilde konaklama vergisinin hesaplanması için gerekli alanlar eklenmiş bulunmaktadır.

Konaklama Vergisi Faturası Acentanın müşterilere vergiler hariç bir konaklama satışı yapması durumunda müşterinin otelden ayrılması ile birlikte otelin müşteriye herhangi bir konaklama bedeli içermeyen sadece konaklama vergisi tutarını içeren bir fatura kesmesi gerekmektedir. Bu tip bir fatura kesilmek istendiğinde fiyat alanı 0 olarak geçilecek ve özel fiyat alanına konaklama vergisinin hesaplanacağı fiyat girilecektir. Bu durumda konaklama vergisi tutarı ile faturanın genel toplamı aynı olacaktır. KDV tutarı 0 olduğu için otomatik olarak istisna kodu ilgili belgeye atanıyor olacaktır. Bu şekilde kesilen ebelgelerin Fatura Tipi:KONAKLAMAVERGISI olacaktır.

![](../_assets/039317ca6b9243177add.png)

Diplomatik İstisnali Fatura Diplomatik istisnanın uygulanacağı konaklama faturalarında kullanmak için E-Devlet Özel Kod Tanımları ekranından “001- Diplomatik İstisna” olarak bir istisna tanımının yapılması gerekmektedir.

![](../_assets/3863213f29725e582e01.png)

Diplomatik istisna olarak kesilmek istenen ebelgelerin Fatura Tipi : ISTISNA olacaktır ve kullanıcılarımızın belgenin toplamlar sekmesinden sağ tık menüsü ile açılan “Özel Matrah/İstisna Tip Atama” işlemi ile tanımlamış olduğu 001 istisna kodunu seçmeleri gerekecektir. Bu seçim yapıldığında belge üzerinde hesaplanmış olan konaklama vergisi tutarı 0 olarak güncellenecektir.

![](../_assets/0dd07f54135715bf5203.png)
