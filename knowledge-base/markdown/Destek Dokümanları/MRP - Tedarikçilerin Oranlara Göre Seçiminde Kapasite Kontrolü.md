---
title: "MRP - Tedarikçilerin Oranlara Göre Seçiminde Kapasite Kontrolü"
page_id: "50684701"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "MRP - Tedarikçilerin Oranlara Göre Seçiminde Kapasite Kontrolü"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / MRP - Tedarikçilerin Oranlara Göre Seçiminde Kapasite Kontrolü"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTc2MzFkZjRjLTA1MzEtNDE1MS1iNzNhLTA0YjBjOGJmMDg2YiZsaW5rPTZiNmJjM2UzLTU0MGMtNGMyMS05ZDhiLWJjYTJjZDEzYTA2ZiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=7631df4c-0531-4151-b73a-04b0c8bf086b&link=6b6bc3e3-540c-4c21-9d8b-bca2cd13a06f&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "mrp-tedarikcilerin-oranlara-gore-seciminde-kapasite-kontrolu_90669835_50684701.html"
source_version: "2022-11-03T09:56:26.483+03:00"
source_bytes: 367332
fetched_at: "2026-09-13T04:26:30+00:00"
generator: "netsis-scraper 1.0.0"
---
# MRP - Tedarikçilerin Oranlara Göre Seçiminde Kapasite Kontrolü

MRP-Tedarikçilerin Oranlara Göre Seçiminde Kapasite Kontrolü ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

MRP'de malzemelerin tedarik edileceği tedarikçilerin belirlenmesinde malzeme bazında oransal dağılım ya da belirtilen önceliklere göre tedarikçilerin kapasitelerini doldurma yöntemleri kullanılabilir. (MRP Parametreleri/MGP oluşturmada satıcı belirleme yöntemi).

![](../_assets/6f31e30ea1c29c3ddf86.png)

Oransal dağılım yapıldığı durumda malzeme ihtiyacı çok yüksek ise tedarikçiye sağlayamayacağı miktarlarda sipariş gidebilmektedir. Buna önlem olarak istenirse oransal dağılımda da kapasite kontrolü yapılması sağlanabilir.

Uygulamanın kullanılabilmesi için MRP modül parametrelerinde "Sipariş Bazında Rezervasyon Sistemi" işaretli olmalıdır. Tedarikçi/Malzeme bazında kapasite bilgileri cari planlama kayıtları ve müşteri/satıcı stok kayıtları ekranında tanımlanabilir. Tedarikçinin ilgili malzemeden hangi periyotta ne miktarda sağlayabileceği, kapasite periyod tipi ve kapasite miktarı tanımlamalarında belirtilmelidir.

![](../_assets/06bc4bc16aff94f45190.png)

**Örnek:** HM1 hammaddesi için aşağıdaki müşteri/satıcı stok kayıtları tanımları yapılmıştır.

İhtiyacın %60'lık kısmı SATICI1 carisi (Kapasite: 600) tarafından, %40'lık kısmı ise SATICI2 carisi (Kapasite: 500) tarafından karşılanmaktadır. Bu durumda MRP çalıştırıldığında, HM1 için çıkan 1500 adetlik ihtiyaç aşağıdaki şekilde dağıtılır.

![](../_assets/a7f12259e9709079ab3a.png)

![](../_assets/1f9b555970151ba21c4c.png)

Yalnızca dağıtım oranları dikkate alınsaydı, SATICI1 : 1500 \* 0.60 = 900 Adet, SATICI2: 1500 \* 0.40 = 600 Adet sipariş geçilecekti. Ancak dağıtım oranlarıyla beraber kapasite kontrolü de yapıldığı için satıcıların kapasitesi aşılmayacak şekilde dağıtım yapılmaktadır ve toplam kapasitenin yeterli olmadığı kalan ihtiyaç için satıcı kodu verilmeden sipariş önerisi getirilmektedir.

SATICI1 : 600 Adet, SATICI2 : 500 Adet, Kapasitenin yeterli olmadığı kalan ihtiyaç: 400 Adet MRP tarafından fason işlem yarı mamuller için açılacak iş emirlerinde veya satıcı siparişlerinde oransal dağılım ve kapasite kontrolü yapılabilmektedir.

![](../_assets/32c1abab320a1e53f7a5.png)
