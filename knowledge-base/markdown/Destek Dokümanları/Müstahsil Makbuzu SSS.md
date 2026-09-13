---
title: "Müstahsil Makbuzu SSS"
page_id: "66250680"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Müstahsil Makbuzu SSS"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Müstahsil Makbuzu SSS"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWM1ZWJmYjM0LWRiNDQtNDIzNS1hOTU3LThmZmU2NWU3YTcyZSZsaW5rPWNhODMxNDEzLTY5OWQtNGE3NC1hMDEwLWExMDE2OTBiNDRhMSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=c5ebfb34-db44-4235-a957-8ffe65e7a72e&link=ca831413-699d-4a74-a010-a101690b44a1&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "mustahsil-makbuzu-sss_80088442_66250680.html"
source_version: "2022-12-07T16:10:06.740+03:00"
source_bytes: 749945
fetched_at: "2026-09-13T04:24:23+00:00"
generator: "netsis-scraper 1.0.0"
---
# Müstahsil Makbuzu SSS

**Müstahsil** **makbuzu** **girişinden** **girilen** **belgenin** **yevmiye** **fişi** **oluşmamaktadır.** **Neler** **kontrol** **edilmelidir?**

Müstahsil parametrelerindeki muhasebe hesapları tanımlı olmalıdır. Belgede seçilen stokun bağlı olduğu muhasebe detay kodunda muhasebe hesapları tanımlı olmalıdır. Cari hesap kartında cari muhasebe kodu hesabı tanımlı olmalıdır.

**Müstahsil** **faturasında** **bağkur** **kesintisi** **yapılmayacak** **olan** **carilerle** **ilgili** **ayrım** **nasıl** **yapılabilir?**

MUSTAHSIL, BAGKURHESAPLAMA özel parametresi tanımlanmalıdır. DEGER alanına CASABITEK tablosundaki kullanıcı tanımlı sahalardan birinin adı yazılarak, ilgili yazılan değerin karşılığı cari kartta E olarak tanımlanmalıdır.
![](../_assets/bca6e2c76efba477aed3.png)![](../_assets/2a9d627448eb5db5a88b.png)

**Müstahsil** **makbuzu** **girişinde** **hesaplanan** **bağkur** **tutarına** **nasıl** **müdahale** **edilmektedir?**

MUSTAHSIL\\BAGKUR özel parametresi tanımlanmalıdır.

**Müstahsil** **faturası** **nasıl** **kaydedilmektedir?**

Kalem girişinden sonra F5 tuşu ile kaydedilmektedir.

**e-müstahsil** **işlemleri** **menüsü** **gelmemektedir.** **Neler** **kontrol** **edilmelidir?**

Merkezi Kimlik Yönetiminde lisanslarda e-müstahsil lisansı olmalıdır. Netsis E-devlet Ayarlarında e-müstahsil ayarlarının ilgili şirket için tanımlanmış olması gerekmektedir.
![](../_assets/a1e1e353317fdd7d4108.png)

**E-Defter berat dosyasının durumunun “Berat dosyası gönderildi” olarak kalması sorun teşkil eder mi?**

E-müstahsil dizaynında invoicenotes tagi desteği bulunmaktadır.

**e-Müstahsil belgesinde Brüt toplam-stopaj-bağkur-mera hesaplaması sonrasında** **kalan** **tutar** **üzerinden borsa** **hesaplanması** **isteniyor.** **Nasıl yapılabilir?**

Müstahsilparametrelerinde"BorsaTesciliÜcretDüzenlemesiYapılsın" parametresi işaretlenmelidir.

**Müstahsil** **belgesinde vadelere** **bölme** **işlemi** **desteklenmekte** **midir?**

Müstahsil Faturası Parametreleri ekranının "Genel Parametreler" sekmesine "C/H Vadelere Bölünerek Geçsin" parametresi işaretlenmelidir. Bu parametre işaretlendiğinde, Müstahsil Makbuz Girişi yapılırken "Ödeme Kodu" alanı ile önceden tanımlanmış vade planının getirilmesi veya elle (manuel) vade girişi yapılabilmektedir.

![](../_assets/550364abf6a6661f234e.png)
