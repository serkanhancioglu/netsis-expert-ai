---
title: "Yeni Güne Devir"
page_id: "22806447"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Kasa"
  - "İşlemler / Kasa"
  - "Yeni Güne Devir"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Kasa / İşlemler / Kasa / Yeni Güne Devir"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTNjMTViNjRkLTE2ZGEtNDFhMS04MTFiLTU0MGEzOTcwMzdjNCZsaW5rPTc3YjU0NjQyLTkyNTctNDE2YS1iYjRmLWY1ZjRiN2MwY2JhNSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=3c15b64d-16da-41a1-811b-540a397037c4&link=77b54642-9257-416a-bb4f-f5f4b7c0cba5&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "yeni-gune-devir_24771217_22806447.html"
source_version: "2022-04-05T15:53:19.473+03:00"
source_bytes: 2338
fetched_at: "2026-09-13T04:10:50+00:00"
generator: "netsis-scraper 1.0.0"
---
# Yeni Güne Devir

Kasanın belli bir güne ait işlemleri ve defter dökümleri tamamlandıktan sonra, o günle ilgili herhangi bir düzenleme veya kayıt işlemine ihtiyaç kalmadığından emin olunduğunda, "Yeni Güne Devir" bölümü çalıştırılır. Yeni Güne Devir işlemi sırasında dikkat edilecek noktalar şunlardır:

- Devir yapılması istenen tarihten önceki tarihlerde devredilmemiş günlük kayıtlar varsa, program devredilmemiş kayıtlar olduğuna ve bunların hangi tarihten itibaren kayıtlı olduklarına dair uyarı mesajı verir. Üzerinde bulunulan günün devrini yapmadan önce bu kayıtların devredilmesi gerekir. Devredilmesi gereken kayıtlar kontrol edildikten sonra, Kasa Modülü → İşlemler → Ek İşlemler → "[Kasa Tarihi/Kodu Değiştirme](<Ek İşlemler/Kasa Tarihi - Kodu Değiştirme.md>)" bölümüne girilerek, ilgili tarihe geçip "Yeni Güne Devir" işlemi çalıştırılmalıdır.
- Yeni Güne Devir işlemi çalıştırıldığında ilgili tarihteki kasa hareketlerinin tamamında sadece izleme yapılabilir. Bu işlemden sonra ilgili tarihteki kasa hareketlerinde iptal, değişiklik veya yeni kayıt yapılamaz.
- Yeni Güne Devir yapılmadan, birden fazla gün için kasa kayıtları oluşturulduğunda, son devir rakamı eski bir tarih itibariyle izlenir ve “Kasa Son Durum” ekranında son durum görülemez. Kasa ile ilgili son durumun listesi "Raporlar" bölümünden alınır.
