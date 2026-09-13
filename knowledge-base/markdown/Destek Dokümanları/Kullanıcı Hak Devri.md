---
title: "Kullanıcı Hak Devri"
page_id: "163414047"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Kullanıcı Hak Devri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Kullanıcı Hak Devri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTU5MWNhN2ZhLTFjZjQtNDc2Yi1hMjUwLTQ1NTc5NjI5MzRjZiZsaW5rPWQwNmQ2YTJmLTkyNDMtNDA1MC1hNGJlLTk2OGQ0NjY5YmE2YyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=591ca7fa-1cf4-476b-a250-4557962934cf&link=d06d6a2f-9243-4050-a4be-968d4669ba6c&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "kullanici-hak-devri_163414058_163414047.html"
source_version: "2025-01-03T14:04:45.367+03:00"
source_bytes: 719690
fetched_at: "2026-09-13T04:22:19+00:00"
generator: "netsis-scraper 1.0.0"
---
# Kullanıcı Hak Devri

Kullanıcıların belirli bir tarih aralığında tüm modüller ya da seçtiği modüller için kendi kullanıcı haklarını bir başka kullanıcıya devredebileceği ekrandır. Bu özellik 9.0.31 sürümü itibariyle desteklenmiştir.

Admin olmayan kullanıcıların haklarının devredilebilmesi için tasarlanmıştır.

Gezgin\\Genel\\Kullanıcı İşlemleri\\Kayıt\\Kullanıcı Hak Devri program yolundan ulaşılır.

İlgili ekranın Kulanıcı İşlemleri modülü altında görebilmek için öncelikle Şirket/Şube/Parametre Tanımları'ndan Kullanıcı Hak Devri Kullansın parametresinin işaretlenip kaydedildikten sonra programdan çıkış giriş yapılması gerekmektedir.

![](../_assets/364856f8de6e34a18473.png)

![](../_assets/9433540447a5f3fd810f.png)

## Hak Devri Yapacak Kullanıcı:

Hak devrini yapacak olan kullanıcının seçildiği alandır. Kullanıcı Admin olmayan bir kullanıcı ise Hak Devri Yapacak Kullanıcı kısmında kendi kullanıcı adını, Admin kullanıcı ise de tüm kullanıcı adllarını görebilecektir.

## Geçerli Tarih Aralığı:

Kullanıcının hangi tarih aralığında haklarını devreceğinin belirtildiği alandır.

## Modül:

Belirtilen tarih aralığı ve seçilen kullanıcının hangi modül yada modüllerle ilgili olan hakların devredileceği bilgisi belirlenmektedir. Tüm modüllerdeki hakları devredilecekse -1 Tüm modüller seçilmelidir.

## Hakkın Devredileceği Kullanıcı:

Hak devri için seçilen kullanıcının girilen tarih aralığında ve belirtilen modüllerdeki hakkın devredileceği kullanıcının belirlendiği kısımdır.

## Durumu:

İlk kayıt esnasında Aktif olarak görünmektedir. Kaydın kapanması durumunda ise Pasif durumuna geçmektedir.

## Kaydın Kapanma Tarihi:

Kayıt kapandıktan sonra kapanma tarihi ile dolacak alandır.

## Kullanıcıyı Bilgilendir:

Hakkın devredileceği kullanıcıya bildirim türü seçimi doğrultusunda bildirim mesajı/e-posta/sms şeklinde olacak şekilde bilgilendirme sağlayan seçenektir.

## Bildirim Türü:

Kullanıcı Bilgilendir seçeneğinin işaretlenmesiyle Bildirim Mesajı, E-Posta ve SMS olarak 3 seçenek aktif hale gelmektedir. Bu seçeneklerden biri ya da birkaçı seçilebilir. E-Posta ve SMS seçeneklerinin işlevinin sağlanması için gerekli e-posta ve sms ayarlarının yapılması gerekmektedir.
![](../_assets/aea4f440787086a392dd.png)

Hak devrini gerçekleştirecek olan kullanıcı Geçerli Tarih Aralığının başlangıcından önce olmak koşuluyla "Kaydı Kapat" butonu ile hak devrini geçersiz hale getirebilmektedir. Bu durumda Kaydın Kapanma Tarihi alanı kaydın kapatıldığı tarih bilgisi, Durumu ise Pasif olarak güncellenecektir.

![](../_assets/05b5f6f8fde35dd4da5c.png)

"Kullanıcıma Devredilen Haklar" Butonu programa giriş yaptığımız kullanıcıya devredilen hakların görülebildiği ekran açılmaktadır. Açılan ekranda programa giriş yaptığımız kullanıcıya dair devredilen aktif ve pasif durumda kullanıcı hak devirlerini görülmektedir. Admin olan kullanıcılara hak devredilemeyeceği için programa Admin kullanıcı ile giriş yapan kullanıcılarda Kullanıcıma Devredilen Haklar ekran içeriği boş gelmektedir.

![](../_assets/b3a24363d4a2dfd60ea4.png)

Gride atılan kayıtlar tekrar çağrıldığında herhangi bir alanında düzeltme yapılamamaktadır.
![](../_assets/a648de00a8899b114ac0.png)

**NOT:**

Kullanıcı E-posta Tanımları ekranında Kullanıcı Hak Devri yapan kullanıcının yapmış olduğu kaydın giridde seçilen kullanıcılara e-posta olarak bildirilmesi için T-Kullanıcı Hak Devri işleminin seçilip "Kaydet" butonuna basılması yeterlidir.

![](../_assets/866f5f4b691a3d69a574.png)

İş Akış Kayıtları ekranında Kullanıcı Hak Devri işlemi onay süreçlerine dahil edilebilmektedir.

![](../_assets/a82ec853976708d38ec0.png)

**ÖRNEKLEME**
DERYA isimli kullanıcının Stok modülü haklarını USER isimli kullanıcıya 18.12.2024 – 20.12.2024 tarihleri arasında devretmek istenmektedir. Aynı zamanda yapılan hak devri işlemi ile kullanıcıya bildirim mesajı
olarak bilgilendirme yapılması istendiğinde alanlar aşağıdaki gibi doldurulup tab tuşu ya da "Kaydet" butonu ile gride kayıt atılır.

![](../_assets/4955ad0b3fc23494170f.png)

USER kullanıcısına programda kullanıcı hak devri sonrası ekrandaki gibi bildirim mesajı görüntülenecektir.
![](../_assets/3f48f9efd5124ad15e90.png)
