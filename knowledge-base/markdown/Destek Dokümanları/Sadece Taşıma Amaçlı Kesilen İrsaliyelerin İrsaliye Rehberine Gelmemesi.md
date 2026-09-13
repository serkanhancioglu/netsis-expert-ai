---
title: "Sadece Taşıma Amaçlı Kesilen İrsaliyelerin İrsaliye Rehberine Gelmemesi"
page_id: "102281809"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Sadece Taşıma Amaçlı Kesilen İrsaliyelerin İrsaliye Rehberine Gelmemesi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Sadece Taşıma Amaçlı Kesilen İrsaliyelerin İrsaliye Rehberine Gelmemesi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWM3ZDFhNWRkLWRkM2EtNGUxNS05ODJkLTM0ZTEzNjM1NWQ0NiZsaW5rPTM0MGFlMTY0LWNmMDMtNDllNC05Y2Q4LWI0ZmU5NTUxNDQ3NiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=c7d1a5dd-dd3a-4e15-982d-34e136355d46&link=340ae164-cf03-49e4-9cd8-b4fe95514476&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "sadece-tasima-amacli-kesilen-irsaliyelerin-irsaliye-rehberine-gelmemesi_102281820_102281809.html"
source_version: "2022-12-29T15:47:38.267+03:00"
source_bytes: 1108843
fetched_at: "2026-09-13T04:23:45+00:00"
generator: "netsis-scraper 1.0.0"
---
# Sadece Taşıma Amaçlı Kesilen İrsaliyelerin İrsaliye Rehberine Gelmemesi

Sadece Taşıma Amaçlı Kesilen İrsaliyelerin İrsaliye Rehberine Gelmemesi ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

9.0.44 seti ile fatura edilmeyecek sadece taşıma amaçlı kesilen yurtiçi tipli satış irsaliyelerinin üst bilgilerine "Faturalanmayacak" şeklinde bir parametre eklenerek irsaliyelerin, irsaliye rehberine gelmemesi sağlanmıştır.

Üst bilgilerde "faturalanmayacak" parametresi işaretli ise; Satış irsaliyesi toplamlar sekmesinde bulunan faturalaştır butonu pasif olacaktır.

![](../_assets/031430f0fc80d2c84dda.png)![](../_assets/fd0700a769919910fc61.png)

İrsaliyelerin Parçalı Faturalaştırılması ekranındaki irsaliye rehberinde ve kalem bilgileri sekmesinde yer alan İrsaliye No rehberinde bu irsaliyeye bağlı kalemler gelmemektedir.

![](../_assets/e861ece30fe2ef2d74d7.png)![](../_assets/6fb1eb21ebbc36e6e8c8.png)

![](../_assets/9cac9863cde0ec510bba.png)

Satış irsaliyesi toplu faturalama ekranında "İrsaliye Tanım Aralığı" sekmesindeki irsaliye numarası rehberinde bu tip irsaliyeler yer almamaktadır ve geniş olarak verilen bir irsaliye numara bilgisi var ise bu tip irsaliyeler hariç bırakılmıştır.

![](../_assets/69078a1a0ce46e74dc84.png)![](../_assets/765e3626b79d02e45efe.png)![](../_assets/f970049c8a47ad12509d.png)

Siparişten oluşturulan irsaliyelerde "Faturalanmayacak" alanı işaretli olmamaktadır, kullanıcı sonradan ilgili irsaliyeyi çağırıp bu alanı manuel olarak değiştirebilir.

Faturalanmamış İrsaliye Listesi raporunda Genel Kısıt-1 sekmesine "Faturalanmayacak" İrsaliyeler Gösterilmesin" parametresi eklenmiştir. Bu parametre ile yurtiçi tipli satış irsaliyelerinde "Faturalanmayacak " seçilen irsaliyelerin rapora getirilmemesi sağlanabilir. Rapora varsayılan olarak "Faturalanmayacak İrsaliyeler Gösterilmesin" seçeneğini işaretli olarak gelmektedir.

![](../_assets/6e01a49be7db4ab83f10.png)![](../_assets/e38c93da1a1778f0ae9d.png)
