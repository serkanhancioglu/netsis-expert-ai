---
title: "e-Belgelerde Tevkifat İade Senaryosu"
page_id: "66241220"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "e-Belgelerde Tevkifat İade Senaryosu"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / e-Belgelerde Tevkifat İade Senaryosu"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWI1NjhkM2Y4LWI1MTItNDBjOS1iYTRmLWE2MzJkMTZhMjhlZSZsaW5rPTRmYjI2ODVlLTI4NDEtNGMwYi05NzA0LTZkMzQ1Mjc3Mjc3MyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=b568d3f8-b512-40c9-ba4f-a632d16a28ee&link=4fb2685e-2841-4c0b-9704-6d3452772773&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "e-belgelerde-tevkifat-iade-senaryosu_80088663_66241220.html"
source_version: "2022-11-02T14:59:35.813+03:00"
source_bytes: 927953
fetched_at: "2026-09-13T04:24:32+00:00"
generator: "netsis-scraper 1.0.0"
---
# e-Belgelerde Tevkifat İade Senaryosu

e-Belgelerde Tevkifat İade Senaryosu ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Tevkifatlı e-Belgelerin iade sürecinde sadece tevkifatsız kdv kısmının iade olarak gönderilmesi gerekiyor. Bu tip belgelerde, belge toplamında tevkifatsız kdv tutarı manuel girilip bu şekilde kaydedilse bile, taslak oluşturma sırasında kdv tekrardan kdv oranına göre hesaplandığı için 9.0.36 setine kadar bu tipteki belgelerin oluşturulması, Api Ara tablo Kullanımı seçeneği ile sağlanıyordu. Ancak bu uygulama adımları oldukça uzun ve karmaşık olması sebebiyle 9.0.36 setinden itibaren e-Arşiv ve e-Fatura belgelerinde **Tevkifat İade** **Senaryosu** desteklenmiştir.
Tevkifat İade Seneryosunun uygulanabilmesi için, Satış Fatura Parametreleri-Fatura KDV sekmesinde "**Tevkifat** **İade** **Yapılsın**" parametresinin işaretlenmesi gerekmektedir. Bu parametrenin işaretlenmesi ile birlikte **Tevkifat İade KDV** **Kodu** alanı aktif olacaktır. Fatura girilirken yazılan kdv kodu için tanımlı bir muhasebe hesap kodu tanımlı değilse, Tevkifat İade Kdv Kodu alanında tanımlanan muhasebe kodu kullanılacaktır.
![](../_assets/819247393916d19ee755.png)
Bu parametre ile birlikte satış faturası belgesinin üst bilgiler sekmesinde "**Tevkifat İade**" parametresi yer almaktadır. Tevkifat İade parametresinin işaretlenebilmesi için fatura tipinin **iade** olması gerekmektedir.
![](../_assets/ab0c2ba5f83b7213a9bd.png)
Üst bilgiler sekmesinde Tevkifat İade parametresinin işaretlenmesiyle kalem bilgileri sekmesinde **Kdv Tutar** adında bir alan aktif olmaktadır. Bu alana iade edilecek kdv tutarı bilgisi girilmektedir. Birden fazla kalem için kalemler bazında iade edilecek kdv tutarı girilebilmektedir. Toplamlar sekmesinde Toplam Kdv alanına kalemler bazında girilen kdv tutar toplam bilgisi getirilmektedir. İade tipli fatura girişinde tevkifat girmeye gerek yoktur. Yukarıda anlatıldığı gibi iade edilecek kdv tutar bilgisinin girilmesi yeterlidir.
![](../_assets/9fb1e751d05c3d8cbd1e.png)
İlgili belge tamamlandıktan sonra bu belge için oluşturulacak olan e-Arşiv veya e-Fatura taslağında, kalem bilgilerinde tanımlanmış olan kdv tutar üzerinden bir kdv tutarı gösterilecektir. Tevkidat İade Senerayo desteği öncesinde, toplamlar sekmesinde toplam kdv alanına müdahale edilse bile, taslak oluşturma kısmında toplam kdv tekrardan hesaplanmaktaydı. Bu parametre ile kalem bilgilerinde yazılan kdv tutarı taslakta basılıyor olacaktır.
Örneğin, 9/10 tevkifatlı gelen bir e-Belgede 180 tl kdv, 162 tl (9/10 tevkifat tutarı) tevkifat görülmektedir. 9/10 tevkifatlı gelen e-Faturanın iadesinde kdv tutarı tevkifat düşülmüş tutar olarak gitmesi gerekmektedir.

Aşağıdaki örneğe göre %18 kdv 180 iken iade faturasında bu değer 180-162=18 olmalıdır.
![](../_assets/67bb4492d64118ab48fb.png)
Örneğe göre Netsis içerisinde tevkifat iade tipinde oluşturulacak fatura aşağıdaki gibi olmalıdır. Oluşturulacak satış faturasının tipi iade olması ve Tevkifat İade parametresinin işaretlenmesi gerekir.
![](../_assets/452f6b32f1724f1f0b8b.png)
Kalemler sekmesinde tevkifat düşülmüş kdv tutarı olarak 18 girilmelidir. Toplamlar sekmesinde Toplam Kdv tutarı Kdv Tutar kadar gelmektedir. Toplamlar kısmında tekrar tevkifat bilgisi girmeye gerek yoktur.
![](../_assets/2c7bae66f45f9ff19de5.png)
![](../_assets/174d0035b01da3cda1f6.png)
Taslak sonrası oluşan e-Belge görüntüsünde; fatura tipinin TEVKİFATIADE, kalemlerde kdv tutarının ve dip toplamda hesaplanan kdv'nin tevkifat düşülmüş kdv olarak geldiği görülmektedir.
![](../_assets/437ec8ccb38501febe65.png)
