---
title: "e-Defter Raporu Beratı ve Dosya Boyutu Bilgisi"
page_id: "50679797"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "e-Defter Raporu Beratı ve Dosya Boyutu Bilgisi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / e-Defter Raporu Beratı ve Dosya Boyutu Bilgisi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTUyZTgwMGU3LTZlZmQtNGMwMi1iYzAyLTczMzYzNzliMWNjYyZsaW5rPWI4ZDA4MTM4LTk0ZjUtNGZmMy1hMjY5LWRjMzAwYTRmMTQ0ZiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=52e800e7-6efd-4c02-bc02-7336379b1ccc&link=b8d08138-94f5-4ff3-a269-dc300a4f144f&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "e-defter-raporu-berati-ve-dosya-boyutu-bilgisi_82575682_50679797.html"
source_version: "2022-11-03T09:13:22.510+03:00"
source_bytes: 895025
fetched_at: "2026-09-13T04:25:48+00:00"
generator: "netsis-scraper 1.0.0"
---
# e-Defter Raporu Beratı ve Dosya Boyutu Bilgisi

e-Defter Raporu Beratı ve Dosya Boyutu Bilgisi ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

![](../_assets/9a14de3e83ffa60b3ef3.png)

E-Defter mükellefleri, Ocak/ 019 döneminden itibaren GİB'e gönderdikleri e-Defter Berat dosyalarının yanı sıra Defter Raporu Beratı olarak isimlendirilen yeni bir dosyayı da Başkanlığa iletmekle yükümlü olacaklardır. [Defter_Raporu_Berati_Duyurusu.pdf](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/59db98f3-6b24-4b2d-aba3-0e2aec1d960d/Defter_Raporu_Berati_Duyurusu.pdf)

2019/Ocak döneminden başlamak üzere aylık dönemler halinde ve aynı sürede (İlgili olduğu ayı takip eden üçüncü ayın son gününe kadar) Berat dosyalarına ek olarak Defter Raporu Beratının da Gelir İdaresi Başkanlığına gönderilmesi gerekmektedir. Kılavuzda da belirtildiği gibi Defter Raporu Beratı dokümanı temel olarak; revize edilmiş berat yapısının genişletilmiş bir şekli olarak düşünülebilir. Defter Raporu Beratı aylık üretilecektir ve parça numarası 000000'dan başka bir değer alamayacaktır. Oluşacak olan defter raporu beratında tekil no alanı EDR karakterleri ile başlayacak, yıl ve ay bilgisinden sonra artan sırayla devam edecektir.

Berat dosyalarının tekli veya çoklu olarak oluşmasından bağımsız bir şekilde, defter oluşturulan ay için sadece bir adet Defter Raporu Beratı oluşturulmalıdır. Şubeli yapı kullanılmış ise aynı şekilde ilgili ayda her şube için 1 adet Defter Raporu Beratı üretilmelidir.

![](../_assets/b3ae155608e6671b9b47.png)

Mevcut beratlarda sadece vergi hesaplarının detayları bilgilendirilmekteydi, Defter Raporu Beratında ise ilgili dönemde çalışmış olan tüm hesapların detayı şeklinde bilgilendirilecektir.

Defter raporu beratında, defter oluşturulmak istenen ayda her bir ana hesap için; borç kayıt sayısı, borç tutarı, alacak kayıt sayısı ve alacak tutarı bilgileri yer alacaktır. Bir hesabın defter raporu beratına gelebilmesi için ilgili ayda borç veya alacak olarak çalışmış olması gerekmektedir.

Netsis içerisinde yer alan ve otomatik olarak E-Defter berat dosyasının gönderilmesini ve bu berata ait cevap dosyasının alınması işlemini gerçekleştiren "Gönder/Al" ve manuel olarak kayıtlı XML dosyalarından Netsis içine E-Defterin yüklenmesini sağlayan "Defter Yükle" işleminde Defter Raporu Beratı dosyasının işlemlere dahil edilmesi sağlanmıştır.

Tasfiye işlemleriyle ilgili, Berat Raporunun özelinde yeni bir düzenleme bulunmuyor, aynı işlemler yapılıyor olacak, sadece o dönemde iki tane defter rapor beratının yüklenmesi söz konusu olacağı için Gelir idaresiyle iletişime geçilmesi gerekecektir.

![](../_assets/afe9bc4a71b138dfa355.png)

Bu işlemler sonucunda oluşan defter raporu beratı dosyasının görüntüsü aşağıdaki gibi olmaktadır.

![](../_assets/2b9e3ab54e1090be23c3.png)

Ayrıca Büyük defter ve Yevmiye Defteri beratlarına **dosya** **boyutu** bilgisi eklenmiştir. Bu düzenleme ile, oluşan berat dosyası içerisinde ilgili XML dosyasının boyutu yazılmaktadır.

Bahsedilen düzenlemeleri, Netsis 9.0.19 versiyonundan itibaren kullanabilirsiniz.
