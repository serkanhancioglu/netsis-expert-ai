---
title: "e-İhracat Belgelerinin Satış Tipli Oluşturulabilmesi"
page_id: "140249277"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "e-İhracat Belgelerinin Satış Tipli Oluşturulabilmesi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / e-İhracat Belgelerinin Satış Tipli Oluşturulabilmesi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWE0Nzg3NjkxLTMzYWMtNDI0Zi05MzRlLWM5NmM1M2ViY2FiNiZsaW5rPTE2NmYzNjQ4LWFlMDQtNDc2OS1hOWM3LWZjOGM0ZGFmZjllYyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=a4787691-33ac-424f-934e-c96c53ebcab6&link=166f3648-ae04-4769-a9c7-fc8c4daff9ec&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "e-ihracat-belgelerinin-satis-tipli-olusturulabilmesi_140249303_140249277.html"
source_version: "2024-06-24T08:59:26.083+03:00"
source_bytes: 1819930
fetched_at: "2026-09-13T04:22:52+00:00"
generator: "netsis-scraper 1.0.0"
---
# e-İhracat Belgelerinin Satış Tipli Oluşturulabilmesi

9.0.56 seti ile serbest bölge işlem formu ile oluşturulan e-İhracat belgelerinin satış tipi ile oluşturulabilmesi desteklenmektedir.

Dış ticaret modülünden kesilen proforma faturalar gümrüğe gönderilen ve senaryo tipi IHRACAT olan e-belgeler olarak gönderimi sağlanmaktadır. Ancak 5000$ altında olan e-ihracat belgeleri için gümrüğe gönderilmeden direkt müşteriye gönderilmesi ve bu işlemlerin serbest bölge işlem formu ile gerçekleşmesi durumunda aşağıdaki adımlar uygulanır.

![](../_assets/ccb3f875deff1d922644.png)

5000$ altında olan e-ihracat belgesinin gümrüğe gönderilmeden direkt müşteriye gönderilmesi ve senaryo tipinin IHRACAT olmaması için Toplu E-fatura Oluşturma ekranında İşlem Tipi Seçimi sekmesinde Belge Tipi İhracat Faturaları ve Dış Ticaret Modülünden Oluşsun(Proforma) parametreleri ile Ön Sorgulama sekmesinde "Gümrük Beyannamesi Düzenlenmesin" parametresi işaretlenmelidir.

![](../_assets/f49b61e1a19a399b66e8.png)![](../_assets/8bbca31a7d7d8e4284b9.png)

Toplu e-Fatura Oluşturma ekranında yukarıdaki seçenekler seçilip Tamam butonuna basıldığında e-fatura carileri için Dış Ticaret modülünden girilen proforma faturalar listelenir. Eğer cari e-fatura mükellefi değil ise ilgili proforma belgesi taslak oluşturma listesine gelmeyecektir.

![](../_assets/c0bd288f3ff907dbfe4b.png)

"Gümrük Beyannamesi Düzenlenmesin" parametresi işaretlenerek taslak oluşturulması durumunda e-fatura senaryosu ilgili carinin kartındaki e-fatura senaryosuna(Temel/Ticari) göre oluşmaktadır.

![](../_assets/0a42edc365ac472de211.png)

![](../_assets/16e1f82e6f297e914ae5.png)

"Gümrük Beyannamesi Düzenlenmesin" parametresi işaretlenmeden taslak oluşturulması durumunda ise e- faturanın senaryosu IHRACAT olarak oluşmaktadır.

![](../_assets/bc140a9a349549abdd51.png)
