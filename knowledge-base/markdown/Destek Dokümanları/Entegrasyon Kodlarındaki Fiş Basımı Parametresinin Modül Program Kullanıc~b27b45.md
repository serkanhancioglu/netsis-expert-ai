---
title: "Entegrasyon Kodlarındaki Fiş Basımı Parametresinin Modül Program Kullanıcı Bazında Ayrıştırılması"
page_id: "111249174"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Entegrasyon Kodlarındaki Fiş Basımı Parametresinin Modül Program Kullanıcı Bazında Ayrıştırılması"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Entegrasyon Kodlarındaki Fiş Basımı Parametresinin Modül Program Kullanıcı Bazında Ayrıştırılması"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTc3NzVkZTNkLWFkODEtNDgzZC05ZmVhLWY3OWE0ODk1MDE4YyZsaW5rPTM0ZmJhNGFiLWZmMDktNDAzZC05OTFhLTViNzY4OGRlNTE0YyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=7775de3d-ad81-483d-9fea-f79a4895018c&link=34fba4ab-ff09-403d-991a-5b7688de514c&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "entegrasyon-kodlarindaki-fis-basimi-parametresinin-modul-program-kullanici-bazinda-ayristirilmasi_111249183_111249174.html"
source_version: "2023-05-22T10:33:21.277+03:00"
source_bytes: 744780
fetched_at: "2026-09-13T04:23:21+00:00"
generator: "netsis-scraper 1.0.0"
---
# Entegrasyon Kodlarındaki Fiş Basımı Parametresinin Modül Program Kullanıcı Bazında Ayrıştırılması

Entegrasyon kodlarındaki Fiş Basımı parametresinin Modül/Program/Kullanıcı bazında ayrıştırılması hakkında ayrıntılı bilgiye bu dokümandan ulaşılır.

Bu özelliğin kullanılabilmesi için öncelikle Gezgin\\Muhasebe\\Entegre\\Kayıt \\Entegrasyon Kodları ekranında "Muhasebeye Doğrudan Aktarım Yapılsın" parametresinin işaretli olması gerekmektedir. Bu parametre

işaretlendiğinde sağ taraftaki menü aktif hale gelecektir.

![](../_assets/2b5fbc23ad2a6bae630d.png)

"Fiş Basımı Yapılmasın" seçeneği seçilir ise girilen kayıtlardan sonra muhasebe fiş basımı yapılması engellenebilir.

"Fiş Basımı Yapılsın" seçeneği seçilir ise fiş basımı desteklenmiş olan tüm ekranlarda kullanıcı ve modül ayrımı yapılmaksızın fiş basımı yapılması sağlanabilir.

"Fiş Basımı Seçilen Kullanıcı/Program" seçilir ise SSO üzerindeki kullanıcı yetkilerini baz almaktadır. Kullanıcının ilgili ekranlarda basım yetkisi var ise girilen kayıtlardan sonra muhasebe fiş basımı yapılabilmektedir. Fiş basımının Modül/Program/Kullanıcı bazında ayrıştırılması bu seçenek ile sağlanmaktadır.

SSO'da kullanıcı hakları alanında "Fiş Basımı" adı ile bir kolon eklenmiştir. Bu alan Evet/Hayır olmak üzere iki seçenekli bir yapıdadır. Fiş basımı yapılmak istenen modüller veya modül içerisinde yer alan programlar için evet seçeneği seçilerek fiş basımının Modül/Program/Kullanıcı bazında yapılması sağlanabilir.

![](../_assets/08047d2b8d166ff33e66.png)

Yukarıdaki SSO ekranında satış faturası için fiş basımı "Evet", alış faturası için ise "Hayır" seçilmiş olup örnek belge üzerinden inceleyelim:

Satış fatura belgesinin toplamlar sekmesinde belgeyi tamamladıktan sonra "Muhasebe fiş basımı yapılsın mı" uyarısı gelmiştir. Evet seçildiğinde dizayn seçimi ekranı açılıp ilgili dizayn seçildikten sonra fiş basımı

yapılabilmektedir. Fiş basımı yapılmasın isteniyor ise hayır ile çıkış yapılabilir.

![](../_assets/ea856d5fe9271ee993cb.png)

Alış fatura belgesinde ise SSO'da fiş basımı seçeneği hayır olduğundan belge tamamlamada fiş basımı ekranı açılmamıştır.

![](../_assets/5076524ba62a9f1ac714.png)
