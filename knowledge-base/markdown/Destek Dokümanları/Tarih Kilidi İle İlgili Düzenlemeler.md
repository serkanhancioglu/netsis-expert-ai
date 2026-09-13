---
title: "Tarih Kilidi İle İlgili Düzenlemeler"
page_id: "50680139"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Tarih Kilidi İle İlgili Düzenlemeler"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Tarih Kilidi İle İlgili Düzenlemeler"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTRmMmNkNDFkLTgxNTktNDEyNS05NzVjLTJkZWM2OWI2YjViZSZsaW5rPWJlOGVlNDMxLWFlOTEtNGFiNC04MjIyLTY5NzJkMWYwNWRlOCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=4f2cd41d-8159-4125-975c-2dec69b6b5be&link=be8ee431-ae91-4ab4-8222-6972d1f05de8&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "tarih-kilidi-ile-ilgili-duzenlemeler_82576576_50680139.html"
source_version: "2022-11-03T09:49:16.463+03:00"
source_bytes: 114752
fetched_at: "2026-09-13T04:26:13+00:00"
generator: "netsis-scraper 1.0.0"
---
# Tarih Kilidi İle İlgili Düzenlemeler

Tarih Kilidi ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

```text
Ürün Grubu: [X] Redcode Enterprise                      [X] Redcode Standart                      [X] Entegre.NETKategori: [X] İyileştirmeVersiyon Önkoşulu:  5.0.12 Onaylı Sürüm
```

Müşterilerimizden gelen geri bildirimlere göre modül bazında tarih kilitleme özelliği desteklenmiştir. Kullanıcı işlemleri modülüne eklenen Modül Bazında Tarih Kilitleme ekranı ile, kullanıcılara modül ve program bazında tarih kilidi kısıtı verebilme imkanı sağlanmıştır. Bu sayede program bazında farklı kilit tarihleri atanabilecektir. Ayrıca tarih kilidine sınır aralığı desteği de getirilmiştir. Bu ekrana girilecek sınır tarih aralığının dışında bir tarih girilmesi engellenmektedir. Modül bazında kilitleme yapılmamışsa, eski sisteme göre tarih kilitleme yapılacaktır.

**Modül Bazında Tarih Kilitleme**

![](../_assets/c1486903b238890041b6.png)Şekil 1

Programın kullanımı sırasında belli bir tarihe kadar bütün kayıtların yapılıp, (örneğin mizanların tutturulup) bu tarihten öncesine herhangi bir kayıt eklenmesi veya yapılmış kayıtlar üzerinde düzeltme, iptal işlemlerinin yapılmasının engellenmesi için bu "Tarih Kilitleme" işlemi kullanılmaktadır. Çok kullanıcılı ortamlarda, birçok kişinin kayıtlar üzerinde işlem yaptığı durumlarda, yanlışlıkla olsa bile mizanı tutturulmuş, resmi defteri çekilmiş dönemlerin kayıtlarında yapılabilecek herhangi bir değişiklik sonradan problem çıkarabilmektedir. Bu nedenle belli bir döneme ait kayıtlara müdahale edilememesi bu bölümden tarih aralığı vererek (tüm modüller bazında) sağlanabilmektedir. Yeni desteklenen özellik yardımıyla artık bu kontrol grup-kullanıcı ve/veya modül-program seçimi yapılarak alınan program listesine başlangıç ve bitiş tarih aralığı verilebilmesi desteklenmektedir.

**Tarih** **Kilitleme** **Sınır** **Aralığı** **Belirleme**
![](../_assets/5ad96bb739e2b113b053.png)Şekil 2

Mevcut "tarih kilitleme" ekranına veya yeni eklenen "program bazında tarih kilitleme" ekranında girilebilecek olan tarih değerlerine verilebilecek sınır atamaları bu ekranda yapılmaktadır. Bu ekranda Admin kullanıcı kontrolü bulunmaktadır.
