---
title: "İhraç Kayıtlı e-Belgelerde Çoklu İstisna Kodu Desteği"
page_id: "90669117"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "İhraç Kayıtlı e-Belgelerde Çoklu İstisna Kodu Desteği"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / İhraç Kayıtlı e-Belgelerde Çoklu İstisna Kodu Desteği"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTYxZjEwZGViLTc5YTgtNDdlMS1iYjRhLTI0ZjkzNTJjYzUxOSZsaW5rPTIxZTZkNzEzLTUzYTMtNDY2Yi1iZjUxLTBmYWY3ODI5OTJmZSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=61f10deb-79a8-47e1-bb4a-24f9352cc519&link=21e6d713-53a3-466b-bf51-0faf782992fe&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ihrac-kayitli-e-belgelerde-coklu-istisna-kodu-destegi_90670231_90669117.html"
source_version: "2022-12-15T10:30:45.637+03:00"
source_bytes: 1246824
fetched_at: "2026-09-13T04:23:56+00:00"
generator: "netsis-scraper 1.0.0"
---
# İhraç Kayıtlı e-Belgelerde Çoklu İstisna Kodu Desteği

İhraç Kayıtlı e-Belgelerde Çoklu İstisna Kodu Desteği ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

**9.0.42** sürümüyle birlikte desteklenen **ihraç kayıtlı** belgelerde kalem bazlı "istisna kodu" desteği getirilmiştir. Bu geliştirme kapsamında ihraç kayıtlı irsaliyeleri faturalaştırma adımında istisna kodu atabilmesi özelliğine ek olarak ÖTV kapsamındaki stoklar için de kalem bazlı istisna kodu girilebilmesi desteklenmiştir.

Çoklu İstisna Kodu desteğinin program genelinde yapılabilmesi için aşağıdaki özel parametrenin tanımlanması gerekir:

Grup Kodu: **EFATURA**, Anahtar: **COKLU_ISTISNA**, Değer:**1**

![](../_assets/2914d437d6f085f505ba.png)

Sadece ihraç kayıtlı satış irsaliyesi belgelerinde ÖTV' li stoklar için, kalem bilgileri sekmesinde gride atılan ilgili kalem üzerinde sağ click menüsüne "**İstisna Kodu Atama/İptali**" seçeneği eklenmiştir. Bu menu altına da "**İstisna** **Kodu** **Ataması**" ve "**İstisna** **Kodu İptali**" seçenekleri eklenmiştir.

İstisna Kodu Atama işlemiyle ihraç kayıtlı belgeler için, 701 (3065 s.Kanununun 11/1- c md. Kapsamındaki ihraç kayıtlı satış), 702 (DİİB ve Geçici Kabul Rejimi Kapsamındaki Satışlar), 702 (4760 s. ÖTV Kanununun 8/2 md. Kapsamındaki ihraç kayıtlı satış) kodlu istisna kodları seçilebilmektedir.

Ayrıca Grup Kodu: **EFATURA**, Anahtar: **KALEMOTVBAS**, Değer:**1** özel parametresiyle de oluşacak olan e-Fatura Xml belgesinin InvoiceLine tag değerine ÖTV bilgilerinin de yazılması sağlanmaktadır.

![](../_assets/13f095830c692c777c3f.png)
![](../_assets/4b0a0e39aa008ac9e711.png)

İhraç kayıtlı belge için taslak oluşturulduğunda e-Belge görüntüsünde ÖTVli stok için satır bazında ÖTV tutarı, dip toplamda da vergi istisna ve ÖTV istisna muafiyet sebebi yazmaktadır. Xmle de bakıldığında InvoiceLine tag inde hem ihraç kayıtlı belgeler için satır bazında seçilen istisna kodu hem de ÖTV istisna kodu bilgileri yazmaktadır.

![](../_assets/53b207785e5e28eebd5b.png)

![](../_assets/bd2e26bef818117a7edb.png)
