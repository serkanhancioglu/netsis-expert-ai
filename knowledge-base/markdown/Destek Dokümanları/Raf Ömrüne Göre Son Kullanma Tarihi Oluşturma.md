---
title: "Raf Ömrüne Göre Son Kullanma Tarihi Oluşturma"
page_id: "50679712"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Raf Ömrüne Göre Son Kullanma Tarihi Oluşturma"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Raf Ömrüne Göre Son Kullanma Tarihi Oluşturma"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWM2Nzg1YzE0LTQ1OTAtNDE3MS1hNmY5LTYxODM1Mzc1MmVhOCZsaW5rPWM2MjIyYTYyLTI5ZTYtNDY0Ni04ZTI2LTJiOGFiY2NjZjhhNSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=c6785c14-4590-4171-a6f9-618353752ea8&link=c6222a62-29e6-4646-8e26-2b8abcccf8a5&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "raf-omrune-gore-son-kullanma-tarihi-olusturma_90670009_50679712.html"
source_version: "2022-11-03T09:54:32.443+03:00"
source_bytes: 746094
fetched_at: "2026-09-13T04:26:23+00:00"
generator: "netsis-scraper 1.0.0"
---
# Raf Ömrüne Göre Son Kullanma Tarihi Oluşturma

Raf Ömrüne Göre Son Kullanma Tarihi Oluşturma ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Serili ürünlerde girişi yapılan serinin son kullanma tarihinin, raf ömrüne(risk süresi) göre giriş anında otomatik olarak hesaplanması sağlanabilmektedir.

Raf ömrüne göre son kullanma tarihinin oluşturulabilmesi için Seri Parametreleri ekranında "Seri Girişinde Kullanılacak Olan Opsiyonel Sahalar, Son Kullanma Tarihi ve Son Kullanma Tarihi Risk Süresine Göre Hesaplansın parametreleri işareti olmalıdır.

![](../_assets/a563a88370b383b6f409.png)

Hesaplanan son kullanma tarihinin kullanıcı tarafından değiştirilmemesi isteniyorsa "Hesaplanan Son Kullanma Tarihi Değiştirilemesin" parametresi işaretli olmalıdır.

Son kullanma tarihi hesaplanırken kullanılacak olan raf ömrü "Stok Kartı Kayıtları" "Stok Kartı 1" Risk Süresi ve Zaman Birimi sahalarından alınacaktır.

![](../_assets/9b30e69a2a1547b8bfb2.png)

Risk süresi raf ömrüne karşılık gelmektedir ve mutlaka dolu ve 0 dan büyük bir değer olmalıdır. Zaman birimi risk süresine girilen değerin zaman birimi olarak karşılığının belirlendiği sahadır. GN- Gün , HF-Hafta, AY-Ay olarak girilecek risk süresinde kullanılabilecek olan zaman birimleridir.

Örnek ekran görüntüsünde S001 stokunun raf ömrü 5 gün olarak belirlenmiştir. Bu stok için yapılan girişler son kullanma tarihi giriş tarihinin üzerine risk süresi eklenerek bulunacaktır.

![](../_assets/775e32fe03af91df71b6.png)

Örneğin 15.09 alış tarihi ve 5 gün risk süresi üzerinden son kullanma tarihi 20.09 olarak hesaplanmıştır.
