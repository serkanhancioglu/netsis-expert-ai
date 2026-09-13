---
title: "Özel Kod-2 Bazında KDV"
page_id: "153157708"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Özel Kod-2 Bazında KDV"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Özel Kod-2 Bazında KDV"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTcyNTZjNTg4LWYyOGEtNDMyZC04YzM1LTg0NmYwMWE4M2I0MyZsaW5rPWNhYzA0YjM5LTE1YTYtNDY1OC1iNjAyLWEwYTRjNDAzMTdjOSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=7256c588-f28a-432d-8c35-846f01a83b43&link=cac04b39-15a6-4658-b602-a0a4c40317c9&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ozel-kod-2-bazinda-kdv_153157708_153157708.html"
source_version: "2024-09-26T15:36:58.113+03:00"
source_bytes: 946885
fetched_at: "2026-09-13T04:22:38+00:00"
generator: "netsis-scraper 1.0.0"
---
# Özel Kod-2 Bazında KDV

Netsis 9.0.35 sürümü ile fatura modülünde "Özel Kod-2" bazında farklı KDV hesaplarının çalışması desteklenmiştir. Bunun için "Entegrasyon Kodları" ekranının "Fatura KDV" sekmesine eklenen "Özel Kod-2 Bazında KDV" seçeneğinin işaretlenmesi gerekir.

![](../_assets/ba2d7023be74a778155b.png)

Bu seçeneğin işaretlenmesiyle, "Entegre/Kayıt" menüsü altında "Özel Kod-2 Bazında KDV Hesap Tanımları" ekranı aktif hale gelecektir. Bu ekranda faturanın "Üst Bilgiler" sekmesinde girilecek olan "Özel Kod-2" değeri için çalışması istenen KDV hesaplarının tanımı yapılabilecektir. İlgili ekran için SSO üzerinden yetki verilmelidir.

![](../_assets/605e244a92b5e86d9787.png)
![](../_assets/25c10666bb76edccb277.png)

Özel Kod-2 Bazında KDV Hesap Tanımları ekranında Entegrasyon Kodları Fatura KDV sekmesi üzerindeki Değişik KDV oranları sayısı kadar Özel Kod 2 bazında Hesaplanan KDV, İndirilecek KDV, İade Hesaplanan KDV ve İade İndirilecek KDV Hesap tanımlamaları yapılabilmektedir.

Örnek 1: Satış faturası özel kod 2 değeri "A" seçilerek belge tamamlandığında oluşan yevmiye fişinde muhasebe kodu %10 KDV hesabına karşılık gelen 391-03-0010 hesabını çalıştırmaktadır.

![](../_assets/9e219b95ed1df43dbfda.png)

Örnek 2: İade tipli %20 KDV oranına sahip bir alış fatura belgesi girişi yapıldığında ise 20 KDV oranı için tanımlı İade İndirilecek KDV hesabı 191-04-0020 hesabı çalışmaktadır.

![](../_assets/d60656565405678ab6a7.png)

Örnek 3: Özel Kod 2 Bazında KDV Hesap Tanımlama ekranında tanımlı olmayan özel kodlar için entegrasyon kodlarında yer alan hesaplar çalışmaktadır.

![](../_assets/40fdce4ddba54bf1b94f.png)

Not: Özel Kod 2 Bazında KDV uygulaması ile Mal Bazında KDV uygulaması aynı anda kullanılamamaktadır.
