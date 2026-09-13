---
title: "Modül Bazında Tarih Kilitleme"
page_id: "41168987"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Genel"
  - "Kullanıcı İşlemleri"
  - "Kayıt"
  - "Modül Bazında Tarih Kilitleme"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Kullanıcı İşlemleri / Kayıt / Modül Bazında Tarih Kilitleme"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWI1ZmU0ZGI4LWQwYmEtNDJlMi1iMTJlLWQyMDc2NTc5NzIzOCZsaW5rPWIwMWNjOTY0LTBlNzgtNGI4NC1iYTcxLTgwNTAxNmNhNjlkYyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=b5fe4db8-d0ba-42e2-b12e-d20765797238&link=b01cc964-0e78-4b84-ba71-805016ca69dc&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "modul-bazinda-tarih-kilitleme_47074272_41168987.html"
source_version: "2022-12-01T15:13:31.457+03:00"
source_bytes: 9679
fetched_at: "2026-09-13T04:17:49+00:00"
generator: "netsis-scraper 1.0.0"
---
# Modül Bazında Tarih Kilitleme

Modül Bazında Tarih Kilitleme, Genel Bölümü'nde Kayıt/Kullanıcı İşlemleri menüsünün altında yer alır. Çok kullanıcılı ortamlarda (birçok kişinin kayıtlar üzerinde işlem yaptığı durumlarda) yanlışlıkla bile olsa, mizanı tutturulmuş ve resmi defter raporu alınmış dönemlerin kayıtlarında yapılacak herhangi bir değişiklik sonradan problem çıkarabilir. Bu bölüm, modül ve program bazında tarih kilitleme yapılmasını sağlar. Böylece, modül ve program bazında farklı kilidi kısıdı verilerek modül ve program bazında farklı kilit tarihleri atanır. Belli bir döneme ait kayıtlara müdahale edilmemesi tarih aralığı verilerek - tüm modüller bazında - sağlanır. Bu kontrol grup-kullanıcı ve/veya modül-program seçimi yapılarak alınan program listesine başlangıç ve bitiş tarih aralığı verilerek yapılır.

Modül Bazında Tarih Kilitleme ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Modül Bazında Tarih Kilitleme Ekranı |  |
| --- | --- |
| Grup Bazında Kilitleme/Kullanıcı Bazında Kilitleme Modül/Program | Tarih kilitleme için seçim yapılan alandır. Kullanıcı Bazında veya Grup Bazında tarih kilitleme yapılmasını sağlar. **Kullanıcı Bazında Kilitleme** seçildiğinde, **"Modül"** seçeneği de seçilirse sadece "Kullanıcı No" alanı sorgulanır. **"Program"** seçeneği ile birlikte seçildiğinde, "Kullanıcı No" ve "Modül No" alanları sorgulanır. **Grup Bazında Kilitleme** seçildiğinde, **"Modül"** seçeneği de seçilirse sadece "Grup Kodu" alanı sorgulanır. **"Program"** seçeneği ile birlikte seçildiğinde, "Grup Kodu" ve "Modül No" alanları sorgulanır. |
| Kullanıcı No | Kullanıcı Bazında Kilitleme seçeneği seçildiğinde aktif hale gelen alandır. Kullanıcı numarasının girilmesini sağlar. |
| Modül No | Kullanıcı Bazında veya Grup Bazında Kilitleme seçildiğinde, her iki seçim için de modül belirlenmesi için kullanılan alandır. |
| Grup Kodu | Grup Bazında Kilitleme seçeneği seçildiğinde aktif hale gelen alandır. Grup kodunun girilmesini sağlar. |
| ![](../../../../_assets/7b6676635e7f4b4eca03.png) Değişiklikleri Kaydet | Girilen bilgilerin onaylanması için kullanılan butondur. |
| ![](../../../../_assets/321481ed082d64434ce8.png) Değişiklikleri İptal Et | Gridden değiştirilen tarihin iptal edilmesi ve değişiklik yapılmadan önceki tarihin getirilmesini sağlayan butondur. |
| ![](../../../../_assets/3c9e16279dc7534277d7.png) Varsayılan Değerleri Ata | "[Tarih Kilitleme](<../İşlemler/Tarih Kilitleme Şifresini Değiştirme.md>)" bölümünden girilen tarihin, "Modül Bazında Tarih Kilitleme" ekranına varsayılan olarak aktarılmasını sağlayan butondur. |
| ![](../../../../_assets/a8993debd75a604f9349.png) Satırlara Kopyala | Gridde seçili satır değerlerinin diğer satırlara kopyalanması için kullanılan butondur. |
| ![](../../../../_assets/1fddc8bc787befa318b7.png) Çıkış | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana (gride) aktarılır.
