---
title: "Tarih Kilidi İşlemleri"
page_id: "66238155"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Tarih Kilidi İşlemleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Tarih Kilidi İşlemleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWM3NTNjMTY3LWI4ZTQtNDA4Yi05ZTQwLTYxZTUxY2FiMDlkYiZsaW5rPTIyOGRjMzY3LWMxNTMtNDdmMy05MmExLWE0NTI5MTlhOGM4MCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=c753c167-b8e4-408b-9e40-61e51cab09db&link=228dc367-c153-47f3-92a1-a452919a8c80&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "tarih-kilidi-islemleri_82576763_66238155.html"
source_version: "2022-11-03T09:51:07.700+03:00"
source_bytes: 682745
fetched_at: "2026-09-13T04:26:17+00:00"
generator: "netsis-scraper 1.0.0"
---
# Tarih Kilidi İşlemleri

Tarih Kilidi İşlemleri ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Programın kullanımı sırasında belli bir tarihe kadar bütün kayıtların yapılıp, (örneğin mizanların tutturulup) bu tarihten öncesine herhangi bir kayıt eklenmesi veya yapılmış kayıtlar üzerinde düzeltme, iptal işlemlerinin yapılmasının engellenmesi için **"Tarih** **Kilitleme"** işlemi kullanılmaktadır. Tarih kilitleme işlemi program genelinde belli bir tarih aralığında tanımlanabileceği gibi istenirse modül bazında da kilitleme işlemleri yapılabilmektedir. Tarih kilitleme işleminin yapılabilmesi için önceilkle ***Tarih Kilitleme Sınır Aralığı Belirleme*** ekranından açık tarih aralığı tanımlanmalıdır. Burada tanımlanmış olan alt-üst sınır tarih aralığına göre tarih kilidi, modül bazında tarih kilitleme işlemleri için tarih kısıtları verilebilecektir. Sınır tarihi aralığında yer almayan tarih bilgileri tarih kilitleme ekranlarında kullanılamayacaktır.
![](../_assets/5a0a3390452def95a6de.png)![](../_assets/8faf1aadc77101bb80de.png)Şekil 1
**Örneğin**, Şekil 1'de tanımlanmış olan açık tarih aralığı 01.01.2021-31.12.2021 tarih aralığı dışında kalan tarihler için tarih kilitleme ekranlarında kısıt verilemeyeceğine dair sistem uyarı verecektir. Tarih kilitleme sınır aralığı belirlendikten sonra program üzerinde genel bir kilitleme yapılacak ise ***Tarih*** ***Kilitleme*** ekranı üzerinden, istenirse kullanıcı bazında istenirse tüm kullanıcılar için geçerli olacak şekilde tarih kısıtı verilebilir.
![](../_assets/caa2cdfc54f6d32c860a.png)Şekil 2
Tarih kilitleme ekranında verilecek olan kısıtın kullanıcılar için ayrı ayrı çalışması isteniyorsa, bu işlem grup bazında ya da kullanıcı bazında yapılabilir ve her kullanıcının farklı tarih aralığında işlem yapmasına izin verilebilir.
Kullanıcıların çalışmasına izin verilecek tarih aralığı belirlenirken sabit tarih aralığı verilebileceği gibi dinamik tarih aralığı da verilebilir. ***Sabit tarih aralığı***, kullanıcıların programda hangi açık tarih aralığında işlem yapması isteniyorsa sabit olarak bu tarihin belirlendiği alandır.
![](../_assets/ff10a4acda945de16383.png)Şekil 3
**Örneğin** Şekil 3'te D1 kullanıcısı için Sabit tarih aralığı seçilmiş ve açık tarih aralığı 01.06.2021-30.06.2021 olarak belirlenmiştir. Bu durumda bu kullanıcı sadece bu tarih aralığında kayıt, düzeltme, iptal işlemlerini yapabilirken diğer tarihlerde işlem gerçekleştiremeyecektir.
***Dinamik tarih aralığı,*** kullanıcıların programda belirlenen gün sayısı kadar geçmiş ve gelecek dönem kayıtlarında işlem yapabilmesi sağlanır. Yazılacak gün değerlerinin, önceden belirlenen sınır tarih aralığı içinde olması gerekir. Dinamik tarih aralığı tanımlanan kullanıcı programa her giriş yaptığında, verilen gün değerlerine göre açık tarih başlangıç/bitiş tarihleri yeniden düzenlenir.
![](../_assets/faf4bd27d9862a52cc2f.png)Şekil 4
**Örneğin**, Şekil 4'te "Geçmiş Açık Gün" ve "Gelecek Açık Gün" alanlarına 30 değeri verildiğinde, D1 kullanıcısı bulunduğu günden 30 gün öncesi veya sonrası için *- sınır tarih aralığı aşılmamışsa-* işlem yapabilir. Bu alanlara en fazla 365 değeri verilebilir. Çok kullanıcılı ortamlarda (birçok kişinin kayıtlar üzerinde işlem yaptığı durumlarda) yanlışlıkla bile olsa, mizanı tutturulmuş ve resmi defter raporu alınmış dönemlerin kayıtlarında yapılacak herhangi bir değişiklik sonradan problem çıkarabilir. Bunu engellemek için ***Modül Bazında Tarih Kilitleme*** ekranı kullanılarak, modül ve program bazında geçerli olacak, açık tarih aralığı istenirse tüm kullanıcılar istenirse kullanıcı bazında tanımlanabilir.
![](../_assets/29d275284ee03c642456.png)Şekil 5
Modül bazında tarih kilitleme ekranında grup bazında kilitleme seçeneği seçildiğinde sistem, hani grup için hangi modül ve programa dair açık tarih aralığı girişi yapılacağını sorgular. Kullanıcı bazında kilitleme seçildiğinde ise
kullanıcı no bazında modül ve program için açık tarih aralığı sorgulanır. Grup ya da kullanıcı kilidi seçimi yapıldıktan sonra, modül ya da program seçimi yapılarak açık tarih aralığının hangi modül ya da program için geçerli olacağı belirlenir. Modül seçimi yapıldıysa sistem alt gride kullanıcı ya da grubun sahip olduğu modül yetkilerini getirecektir ve bunlar için işlem yapılmasına izin verecektir. (Şekil 6)
![](../_assets/c65fb3d4c9519b40ea00.png)Şekil 6
Açık tarih aralığı program seçildiyse, modül no alanı aktif olur ,buradan ilgili modül seçilir ve bu modül içinde yer alan kullanıcının yetkisi olduğu alt akranlar grid bölümde listelenerek, hangi programlar için açık tarih aralığı tanımlanacağı belirlenir. (Şekil 7)
![](../_assets/975a5629bcd479f88d70.png)Şekil 7
Modül no rehberinden, kullanıcının yetkisi olmayan bir modül seçilirse sistem yetki verilmesi gerektiğine dair uyarı verecektir. Yetkilendirme sonrasında bu program için tarih kısıtı verilebilir. (Şekil 8)
![](../_assets/8e8204420ffc829d06b5.png)Şekil 8
Tarih kilitleme ekranında bahsedilen sabit tarih ve dinamik tarih aralığı modül bazında tarih kilitleme ekranında da kullanılabilmektedir. **Örneğin**, Şekil 9'da D1 kullanıcısının Fatura modülüne yetkisi bulunmakta ve bu modül içinde yetkisi olan Satış Faturası ve Satış İrsaliyesi ekranlarında işlem yapacağı açık tarih aralıkları belirlenmiştir. Buna göre kullanıcı Satış Faturası girerken 01.07.2021-20.07.2021 tarihleri arasında işlem yapabilecekken, Satış İrsaliyesi girerken bulunduğu günden 30 gün öncesi ve sonrasına kayıt girişinde bulunabileceğine dair tanımlama yapılmıştır.
![](../_assets/c1db43191cf1bdccc2e9.png)Şekil 9
