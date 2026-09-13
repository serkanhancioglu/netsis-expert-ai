---
title: "Alış Satış Faturalarında KDV Hesabının Tevkifata Göre Detaylandırılması Desteği"
page_id: "66256009"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Alış Satış Faturalarında KDV Hesabının Tevkifata Göre Detaylandırılması Desteği"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Alış Satış Faturalarında KDV Hesabının Tevkifata Göre Detaylandırılması Desteği"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTdiYTQxNmE2LWNkMzUtNDZjMi05NTg1LWFmODMyZDUxYmYxNCZsaW5rPTQ1ZTgzNzk0LTE2YmYtNDgzMi1iZWY5LTkzZTZiMjRiYWZhMiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=7ba416a6-cd35-46c2-9585-af832d51bf14&link=45e83794-16bf-4832-bef9-93e6b24bafa2&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "alis-satis-faturalarinda-kdv-hesabinin-tevkifata-gore-detaylandirilmasi-destegi_80088276_66256009.html"
source_version: "2023-05-05T10:25:25.847+03:00"
source_bytes: 2573813
fetched_at: "2026-09-13T04:24:23+00:00"
generator: "netsis-scraper 1.0.0"
---
# Alış Satış Faturalarında KDV Hesabının Tevkifata Göre Detaylandırılması Desteği

Alış Satış Faturalarında KDV Hesabının Tevkifata Göre Detaylandırılması ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Alış ve satış faturalarında KDV Hesabının Tevkifata göre Detaylandırması desteklenmiştir. Bu kapsamda Alış ve Satış Fatura Parametreleri Ek Maliyet sekmesinde bulunan "**KDV** **Hesabı** **Tevkifata** **Göre** **Detaylandırılsın**" parametresinin işaretlenmesi gerekmektedir.

![](../_assets/e34b70612c8e3690f10b.png)![](../_assets/3a5d3691f3fee98d5cd7.png)

Parametre işaretlendiğinde, tevkifatlı satış faturalarındaki KDV tutarı içerisindeki tevkifat tutarının Tevkifat KDV Hesabı'na; KDV ve tevkifat tutarları arasındaki farkın da Hesaplanan KDV Hesabı' na atılması sağlanmıştır. "**KDV** **Hesap** **Kodlarınızı** **Buradan** **Girebilirsiniz**" yazısına tıklandığında açılan "**Tevkifat** **KDV** **Hesap** **Kodu** **Girişi**" ekranından KDV oranı bazında tevkifat KDV hesap kodları girilir.

**Örnek1**: 100 Liralık KDV tevkifatına tabi olan satış faturası kesilmiştir. KDV tevkifat oranı 3/10' dur.

![](../_assets/c93d05ef81a4ff9cb30e.png)

- Satış Fatura Parametreleri Ek Maliyet sekmesinde bulunan "**KDV Hesabı Tevkifata Göre** **Detaylandırılsın**" parametresi işaretli olduğunda,

Satış faturası girişi sonrasında oluşan yevmiye fişinde,

- Hesaplanan tevkifat tutarı entegrasyon kodlarındaki Ek Maliyet-2 hesabına borç kaydı,
- KDV tevkifat tutarı, Satış parametrelerinde "KDV tevkifata göre detaylandırılsın" parametresi işaretli olduğunda KDV bazında girilen tevkifat KDV hesabına alacak kaydı,
- Toplam KDV – KDV tevkifatı arasında kalan tutar ise, entegrasyon kodlarındaki hesaplanan KDV hesabına alacak olarak atılmaktadır.

```text
Mal tutarı                        100,00 TL
```

```text
KDV (%18)                       18,00 TL (100*0,18=18)
```

```text
KDV Tevkifatı (3/10)         5,40 TL (18*0,03=5,4)
```

```text
Tahsil Edil.KDV (%70)       12,60 TL (18-5,4=12,6)
```

```text
TOPLAM                           112,60 TL (100+12,6)
```

- Satış Fatura Parametreleri Ek Maliyet sekmesinde bulunan "**KDV Hesabı Tevkifata Göre** **Detaylandırılsın**" parametresi işaretli olmadığında, çoklu tevkifat oranı ve tevkifat ile ilgili özel parametreler tanımlı olmadığı durumunda oluşan yevmiye fişinde;

KDV tevkifat tutarı, entegrayon kodlarındaki satış ek maliyet-2 hesabına borç kaydı olarak, toplam KDV tutarı ise, entegrasyon kodlarındaki hesaplanan KDV hesabına alacak olarak atılmaktadır.

![](../_assets/6cb800c69d34920da98f.png)
![](../_assets/f0fad5572e6743a740fe.png)

**Örnek2**: 100 Liralık KDV tevkifatına tabi olan alış faturası kesilmiştir. KDV tevkifat oranı 3/10' dur.

![](../_assets/c3b428efe7d78f2f41e8.png)

- Alış Fatura Parametreleri Ek Maliyet sekmesinde bulunan "**KDV** **Hesabı** **Tevkifata** **Göre** **Detaylandırılsın**" parametresi işaretli olduğunda,

Alış faturası girişi sonrasında oluşan yevmiye fişinde,

- Hesaplanan tevkifat tutarı entegrasyon kodlarındaki Ek Maliyet-2 hesabına alacak kaydı,
- KDV tevkifat tutarı, Alış parametrelerinde "KDV tevkifata göre detaylandırılsın" parametresi işaretli olduğunda KDV bazında girilen tevkifat KDV hesabına borç kaydı,
- Toplam KDV – KDV tevkifatı arasında kalan tutar ise, entegrasyon kodlarındaki indirilecek KDV hesabına borç olarak atılmaktadır.

![](../_assets/4bd8fa852c716d5a5946.png)

- Alış Fatura Parametreleri Ek Maliyet sekmesinde bulunan "**KDV Hesabı Tevkifata Göre** **Detaylandırılsın**" parametresi işaretli olmadığında, çoklu tevkifat oranı ve tevkifat ile ilgili özel parametreler tanımlı olmadığı durumunda oluşan yevmiye fişinde;

KDV tevkifat tutarı, entegrayon kodlarındaki alış ek maliyet-2 hesabına alacak kaydı olarak, toplam KDV tutarı ise, entegrasyon kodlarındaki indirilecek KDV hesabına borç kaydı olarak atılmaktadır.

![](../_assets/5a6b0375d2a85b0fdfa4.png)
![](../_assets/3218486352991791b4f4.png)
