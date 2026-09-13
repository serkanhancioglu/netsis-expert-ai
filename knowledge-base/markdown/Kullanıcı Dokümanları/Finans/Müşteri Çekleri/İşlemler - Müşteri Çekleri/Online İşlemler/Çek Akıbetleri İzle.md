---
title: "Çek Akıbetleri İzle"
page_id: "24739902"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Müşteri Çekleri"
  - "İşlemler / Müşteri Çekleri"
  - "Online İşlemler"
  - "Çek Akıbetleri İzle"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Müşteri Çekleri / İşlemler / Müşteri Çekleri / Online İşlemler / Çek Akıbetleri İzle"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTVmMWU2MzQ2LWY5NzItNDA0NC04YWM2LTc4ZmIwYzQ4MzA0ZiZsaW5rPWIxNDYyMzVhLTVkMzQtNGNhOS1hMjNlLTFlMmE4MDE2YWNkMyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=5f1e6346-f972-4044-8ac6-78fb0c48304f&link=b146235a-5d34-4ca9-a23e-1e2a8016acd3&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "cek-akibetleri-izle_34211351_24739902.html"
source_version: "2022-09-23T08:07:09.150+03:00"
source_bytes: 36188
fetched_at: "2026-09-13T04:11:19+00:00"
generator: "netsis-scraper 1.0.0"
---
# Çek Akıbetleri İzle

Çek Akıbetleri İzle, Finans Bölümü'nde, "İşlemler/Müşteri Çekleri " menüsünün altında yer alır. Çek Akıbetleri İzle, bankaya tahsile gönderilen çeklerin son durumlarını gösteren bölümdür. Çek Akıbetleri İzle uygulaması, şu an için sadece TEB, HSBC, Akbank, ICBC, Finansbank, Ziraat Bankası bankaları için destek verir. "Çek Akıbetleri İzle" bölümünün kullanılması için, "Tahsil Hesabına Çek Cirosu" ekranında yer alan "Verilen Kodu" alanına Banka Hesap Kodunun girilmesi gerekir. Bunun için de, Banka Modülünün entegre olması gerekir. Sorgu bölümünde, izlenmesi istenen çeklerle ilgili kısıt verilir.

![](../../../../../_assets/8ac0ba589cedea9d7679.png)

Çek Akıbetleri İzle ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Çek Akıbetleri İzle Ekranı |  |
| --- | --- |
| Tarih1/Tarih2 | Çeklerin son durumlarının gösterilmesi için baz alınacak tarih aralığının girildiği alandır. Girilecek tarihin, çeklerin tahsile gönderildiği tarih olması gerekir. "Tarih1" başlangıç tarihini, "Tarih2" ise bitiş tarihini ifade eder. |
| Hesap No | Banka Modülünde tanımlanan çeklerin tahsile gönderildiği hesap numarasının girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, banka hesap numaraları arasından seçim yapılır. |
| IBAN | "Hesap No" alanında seçilen hesap kodunun ait olduğu IBAN numarasının program tarafından otomatik olarak ekrana getirildiği alandır. |
| Banka | "Hesap No" alanında seçilen hesap kodunun ait olduğu banka ana kodunun program tarafından otomatik olarak ekrana getirildiği alandır. |
| Şube | Banka modülünde tanımlanan çeklerin tahsile gönderildiği şube kodunun girildiği alandır. |
| ![](../../../../../_assets/2263a0c544f294f6e7c0.png) Online Getir | Gerekli kısıtlar verildikten sonra butonuna basıldığında, çeklerin akıbetleri aşağıda yer alan grid ekrandan izlenir. Grid alanda yer alan Karşılıksız, Tahsil, Müşteri İade ve XML Mesaj sekmeleri sayesinde, tahsil edilen, karşılıksız çıkan veya müşteriye iade edilen çekler izlenir. Bu bölümlerde yer alan çek bilgileri, bankanın göndermiş olduğu XML Mesaj sekmesinde bulunur. |
| Adet | Çeklerin miktar bilgilerinin izlendiği alandır. |
| Toplam | Çeklerin toplam tutar bilgilerinin izlendiği alandır. |
