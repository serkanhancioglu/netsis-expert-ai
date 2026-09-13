---
title: "Tarih Kilitleme"
page_id: "41168997"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Genel"
  - "Kullanıcı İşlemleri"
  - "İşlemler"
  - "Tarih Kilitleme"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Kullanıcı İşlemleri / İşlemler / Tarih Kilitleme"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWFkNmM3MDlmLTJmYTItNDY4YS1iNjU1LWE5NDM0NjA4MTA1OSZsaW5rPWY1YzQyMjQ4LTJjMWEtNGQzZS04NGQzLTJhYmVjYjQzNzk4ZSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=ad6c709f-2fa2-468a-b655-a94346081059&link=f5c42248-2c1a-4d3e-84d3-2abecb43798e&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "tarih-kilitleme_47074271_41168997.html"
source_version: "2022-12-01T15:39:01.740+03:00"
source_bytes: 9708
fetched_at: "2026-09-13T04:17:53+00:00"
generator: "netsis-scraper 1.0.0"
---
# Tarih Kilitleme

Tarih Kilitleme, Genel Bölümü'nde İşlemler/Kullanıcı İşlemleri menüsünün altında yer alır. Programın kullanımı sırasında belli bir tarihe kadar tüm kayıtların yapılıp - örneğin, mizan raporlarının tutturulup - bu tarihten öncesine herhangi bir kayıt eklenmesi veya yapılan kayıtlar üzerinde düzeltme ve iptal işlemlerinin yapılmasının engellenmesi için kullanılan bölümdür.

Tarih Kilitleme ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Tarih Kilitleme Ekranı |  |
| --- | --- |
| Tarih Kilitleme Şifresi | Tarih kilitleme şifresinin girildiği alandır. |
| Kullanıcılar Tek Tek Kilitlensin | Kullanıcıların tek tek kilitlenmesi için kullanılan seçenektir. |
| Tüm Kullanıcılar Kilitlensin | Tüm kullanıcıların kilitlenmesi için kullanılan seçenektir. |
| Grup Bazında Kilitleme | Tarih kilitleme işleminin grup bazında yapılması için kullanılan seçenektir. |
| Kullanıcı Bazında Kilitleme | Tarih kilitleme işleminin kullanıcı bazında yapılması için kullanılan seçenektir. |
| Grup Kodu | "Grup Bazında Kilitleme" seçeneğinin işaretlenmesi ile aktif hale gelen alandır. Grup kodunun girilmesini sağlar. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, grup kodları arasından seçim yapılır. |
| Kullanıcı No | "Kullanıcı Bazında Kilitleme" seçeneğinin işaretlenmesi ile aktif hale gelen alandır. Kullanıcı numarasının girilmesini sağlar. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, kullanıcı numaraları arasından seçim yapılır. |
| Sabit Tarih Aralığı | Kullanıcıların, geçmiş ve gelecek döneme ait işlem yapılmasına izin vereceği sabit tarih aralığının girildiği alandır. |
| Dinamik Tarih Aralığı | Açık tarih aralığı belirlenmesini sağlayan alandır. Kullanıcıların, geçmiş ve gelecek döneme ait kaç günlük bir açık tarih aralığına işlem yapmasına izin verileceği belirlenir. Belirlenen gün sayısı kadar geçmiş ve geleceğe yönelik işlem yapılması sağlanır. Bu kapsamda, "Tarih Kilitleme" ve "Modül Bazında Tarih Kilitleme" ekranlarından gün sayısı tanımlanabilir. Yazılacak gün değerlerinin, önceden belirlenen sınır tarih aralığı içinde olması gerekir. Dinamik Tarih Aralığı tanımlanan kullanıcı programa her giriş yaptığında, verilen gün değerlerine göre açık tarih başlangıç/bitiş tarihleri yeniden düzenlenir. Dinamik Tarih Kilidi ile, "Tarih Kilitleme" ekranından ve "Modül Bazında Tarih Kilitleme" ekranından modül veya program detayı verilir. "Modül Bazlı Tarih Kilitleme" ekranında bazı satırların tarih aralığı ile, bazılarının ise dinamik tarih aralığı ile takip edilmesi sağlanır. "Geçmiş Açık Gün" sütununa girilecek sıfır değeri, sadece ilgili gün içinde işlem yapılması anlamına gelir. |
| Açık Tarih Aralığı Başlangıcı/Açık Tarih Aralığı Bitişi | Açık tarih aralığı girilen alandır. Başlangıç ve bitiş tarih aralığı verilmesini sağlar. "Geçmiş Açık Gün" ve "Gelecek Açık Gün" alanlarına verilen değerlere göre, açık gün tarihinin otomatik değişmesi sağlanır. **Örneğin;** "Geçmiş Açık Gün" ve "Gelecek Açık Gün" alanlarına 30 değeri verildiğinde, ilgili kullanıcı bulunduğu günden 30 gün öncesi veya sonrası için - sınır tarih aralığı aşılmamışsa - işlem yapabilir. Bu alanlara en fazla 365 değeri verilebilir. |
