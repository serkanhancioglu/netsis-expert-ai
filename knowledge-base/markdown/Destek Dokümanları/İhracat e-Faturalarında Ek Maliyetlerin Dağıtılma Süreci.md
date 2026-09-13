---
title: "İhracat e-Faturalarında Ek Maliyetlerin Dağıtılma Süreci"
page_id: "127697000"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "İhracat e-Faturalarında Ek Maliyetlerin Dağıtılma Süreci"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / İhracat e-Faturalarında Ek Maliyetlerin Dağıtılma Süreci"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTJiMGJlYzU4LTk0MDEtNDI3Zi1hM2E1LWM1YTA2MDJmOTg3ZCZsaW5rPTY4NDYzMzgxLWQ0ZmUtNGRlOS1iOWZhLTg4MGVmZDM2ODVhYSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=2b0bec58-9401-427f-a3a5-c5a0602f987d&link=68463381-d4fe-4de9-b9fa-880efd3685aa&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ihracat-e-faturalarinda-ek-maliyetlerin-dagitilma-sureci_127697000_127697000.html"
source_version: "2023-11-24T09:25:16.407+03:00"
source_bytes: 1010250
fetched_at: "2026-09-13T04:23:11+00:00"
generator: "netsis-scraper 1.0.0"
---
# İhracat e-Faturalarında Ek Maliyetlerin Dağıtılma Süreci

İhracat e-Faturalarında ek maliyetlerin dağıtılma süreci hakkında ayrıntılı bilgiye bu dokümandan ulaşılır.

İhracat e-fatura süreçlerinde gümrük firmaları gönderilen mallara ait bilgileri sistemlerine işlemektedir. Bu süreçte navlun & sigorta ve varsa diğer maliyetleri toplu olarak girip kalem bazında birim ağırlığa göre kullandıkları sistemde belgelerine yansıtmaktadır. Netsis içerisinde de ihracat belgelerinde Navlun ve Sigorta gibi ek maliyetlerin kalemlere dağıtılması işlemi aşağıdaki yöntemler ile gerçekleştirilebilir.

1-İrsaliye belgesinde kalem olarak eklenebilir.

İrsaliye belgesinde ayrı kalem olarak girilmesi durumunda; ilgili navlun ya da sigorta kalemi gride atıldıktan sonra üzerinde sağ klik yapıldığında gelen menülerden "E-İhracat Alt Maliyet Kalemi Ekle" seçeneği seçilir.

![](../_assets/bd5bb81a7a3d6b99c5b5.png)

Eğer Proforma üzerinden süreç yürütülüyorsa; sigorta ve\\veya navlunun ayrı kalem olarak girilmesi durumunda, proforma belgesi düzenlenirken ilgili kalem üzerinde sağ klik yapılarak gelen menülerden "E-ihracat Alt Maliyet Kalemi Ekle" seçeneği seçilir.

![](../_assets/9a8369610f6f842496fc.png)

2-İrsaliye belgesinin toplamlar sekmesindeki Ek Maliyet-1/Ek Maliyet-2 alanlarında girilebilir.

![](../_assets/f9fc5b73e915863c0031.png)

3-Proforma faturasında Navlun/Sigorta sekmelerinde girilebilir.

Dış ticarette Sigorta ve Navlun sekmelerinden girilen değerlerin Proforma belgesine yansıtılması için Sigorta Proformaya Eklensin/Nakliye Proformaya Eklensin seçenekleri işaretlenir. Bu durumda girilen değerler belgede Ek Maliyet-1 ve Ek Maliyet-2 alanlarına yansır.

![](../_assets/5f9ec8224caabdebffc8.png)![](../_assets/9b8e031d61bffc08c3ba.png)

**İhracat E-faturası** **Oluşturma**

Bu yöntemlerden biri ile giriş yapıldığında Toplu e-fatura oluşturma ekranında "Ek Maliyetler Kalemlere Dağıtılsın" seçeneği işaretlenerek taslak oluşturulup belgedeki kalemlerin birim ağırlık değerlerine göre ek maliyetler kalemlere dağıtılır. Bunun için Stok Kartı Kayıtlarında ilgili stokların birim ağırlık alanları dolu olmalıdır. Kalemlere dağıtılabilmesi için belgenin toplam ağırlık değerinin sıfırdan farklı olması gerekmektedir.

![](../_assets/5030b22e1a1b368c1bcb.png)
![](../_assets/d8f90f057e7eb4439b45.png)

Ek maliyet bedelleri, (Birim Ağırlık x Miktar) hesaplaması ile kalemlere yansıtıldığında XML'de Allowance Charge tagi içerisinde gösterilmektedir.

![](../_assets/b6dfd91c2624b0043f92.png)
![](../_assets/dae8523c82555093a105.png)

Yukarıdaki ekran görüntülerinde yer alan bilgiler ile örneklendirecek olursak, ek maliyetler aşağıdaki gibi kalemlere dağıtılır.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Stok Kodu | Birim Ağırlık | Miktar | Dağıtım Oranı (Birim Ağırlık\*Miktar) | Navlun Tutarı\*(Dağıtım Oranı/Toplam Dağıtım Oranı) | Sigorta Tutarı\*(Dağıtım Oranı/Toplam Dağıtım Oranı) |
| S003 | 2 | 10 | 2\*10=20 | 300\*20/30=200 | 600\*20/30=400 |
| S004 | 5 | 2 | 5\*2=10 | 300\*10/30=100 | 600\*10/30=200 |
