---
title: "Netsis Dil Düzenleyici"
page_id: "74711395"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis Dil Düzenleyici"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis Dil Düzenleyici"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTc3YWRiYWQ0LTgwNTUtNDJmZC1iNDdjLTI3NGZmYjk5OWUwNiZsaW5rPWMxYjI5MGRkLWM5MTItNGVlMy04MjEwLTNhMWNlMDc3ZTU2ZiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=77adbad4-8055-42fd-b47c-274ffb999e06&link=c1b290dd-c912-4ee3-8210-3a1ce077e56f&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-dil-duzenleyici_80088167_74711395.html"
source_version: "2022-11-02T14:50:13.763+03:00"
source_bytes: 317868
fetched_at: "2026-09-13T04:24:20+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis Dil Düzenleyici

Netsis Dil Düzenleyici ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Netsis Dil Düzenleyici modülü Genel\\Yardımcı Programlar\\Kayıt altında yer alır. Netsis Dil Düzenleyici modülü ile Netsis içerisindeki başlıklar ve ekranlardaki alan isimleri istenilen dile göre düzenlenebilmektedir.
Düzenleme yapılacak olan alanların kolay tespit edilebilmesi için Netsis Temelset kısayoluna farenin sağ tuşuna basılarak Özellikler bölümü seçilir, açılan ekranda hedef yolunun sonuna boşluk bırakılır ve SHOWRESOURCEID parametresi yazılarak "Tamam" butonuna basılır.
![](../_assets/522698da1577ff7943dd.png)
SHOWRESOURCEID parametresi kullanılarak Netsis'e giriş yapılırsa, tespit edilecek başlıklar ve sahalar aşağıdaki gibi kod değerleri ile birlikte görünecektir.
![](../_assets/df71850951d37af294c8.png)
SHOWRESOURCEID parametresi kullanılarak değiştirilmek istenen alan tespit edildikten sonra, Temelset kısayoluna farenin sağ tuşuyla basılarak hedef yolunun sonuna yazılmış olan SHOWRESOURCEID parametresi kaldırılarak kaydedilir. Programa tekrar giriş yapılır. Netsis dil düzenleyici ekranında, mevcut kullanılan dil **kaynak dil** olarak, değiştirilmek istenen dil ise **hedef dil** olarak seçilir ve değişiklik yapılmak istenilen modül kodu **Netsis Modül** alanından seçilerek raporla butonuna basılmalıdır. Düzenleme yapılacak olan alan, hedef açıklama kısmında düzenlendikten sonra **"Değişiklikleri Kaydet"** butonuna basılarak uygulamadan çıkılmalıdır.
![](../_assets/5176de1af1249742dcaf.png)
Netsis uygulamasına tekrar giriş yapıldığında, yapılmış olan değişiklikler geçerli olacaktır.
![](../_assets/057f7b3b3c884168f7e9.png)
