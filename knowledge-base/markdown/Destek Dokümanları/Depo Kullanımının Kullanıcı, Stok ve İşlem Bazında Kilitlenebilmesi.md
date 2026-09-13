---
title: "Depo Kullanımının Kullanıcı, Stok ve İşlem Bazında Kilitlenebilmesi"
page_id: "150569091"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Depo Kullanımının Kullanıcı, Stok ve İşlem Bazında Kilitlenebilmesi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Depo Kullanımının Kullanıcı, Stok ve İşlem Bazında Kilitlenebilmesi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTUxMWQzODVjLTU1N2EtNDhiOS05NDViLWU1NzFlZTUzNjcxZCZsaW5rPTBhZmUyMWNmLTIwYjYtNGY4NC05ZDBhLTA1NDkzMTc2N2E3ZCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=511d385c-557a-48b9-945b-e571ee53671d&link=0afe21cf-20b6-4f84-9d0a-054931767a7d&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "depo-kullaniminin-kullanici-stok-ve-islem-bazinda-kilitlenebilmesi_150569091_150569091.html"
source_version: "2024-09-03T08:39:05.543+03:00"
source_bytes: 209314
fetched_at: "2026-09-13T04:22:38+00:00"
generator: "netsis-scraper 1.0.0"
---
# Depo Kullanımının Kullanıcı, Stok ve İşlem Bazında Kilitlenebilmesi

Depo kilit uygulaması ile depo kodu kullanımın kullanıcı, stok kodu ve işlem bazında kilitlenebilmesi mümkündür. Kilit tanımlarının yapılması için *Gezgin\\Lojistik - Satış\\Stok\\Kayıt\\Lokal Depo İşlemleri\\Depo* *Tanımlama* menüsü kullanılır.

Kilit tanımları yapılmadan önce depo bazında kilit politikalarının belirlenmesi için Depo Tanımlama\>"Genel Bilgiler" sekmesinde Kilit Politikası alanından seçim yapılmalıdır.

![](../_assets/ffbb20e906012b6e9107.png)

**Kilit** **Politikası**

- **"Kilitliler** **Seçilsin"** işaretli olduğunda "Kilit Bilgileri" sekmesinden yapılan tanımlamalar ile depolarda kilitli olacak stok, kullanıcı ve program seçimleri yapılabilecektir.
- **"Kilitli Olmayanlar Seçilsin"** işaretli olduğunda "Kilit Bilgileri" sekmesinden yapılan tanımlamalar ile depolarda kilitli olmayan yani kullanımına izin verilen stok, kullanıcı ve program seçimleri yapılabilecektir.

Kilit politikası belirlendikten sonra **Kilit Bilgileri** sekmesinde kullanıcı tipi, stok tipi, işlem seçimi alanları için uygun kısıtlar belirlenmelidir.

**Kullanıcı** **Tipi:** Bu alanda belirli kullanıcılar veya belirli kullanıcı grupları ya da tüm kullanıcılar bazında kilit tanımı için seçim yapılabilir.

**Kullanıcı** **Değer:** Kullanıcı Tipi alanında Kullanıcı Kodu ya da Kullanıcı Grubu seçim yapıldığında, rehberden
kullanıcı ve grup kodu seçilmelidir.

**Stok** **Tipi:** Kısıtlanacak stok tipleri için aşağıdaki kriterlere göre tanımlama yapılabilir.

- Stok Kodu Bazında
- Grup Kodu Bazında
- Kod-1 Bazında
- Kod-2 Bazında
- Kod-3 Bazında
- Kod-4 Bazında
- Kod-5 Bazında,
- Ürün Grubu Bazında
- Tüm Stoklar

**Stok** **Değer:** Stok Seçimi alanında yapılan seçim bazında kısıt verilmelidir. Örn; Grup Kodu Bazında seçeneği işaretli ise rehberden grup kodu bilgisi seçilmelidir.

**İşlem** **Seçimi:** Bu alanda Fatura, Stok, Talep/Teklif, Dekont, Üretim, Müstahsil Faturası modüllerinde depo kodunun kullanıldığı aşağıdaki ekranlarda işlem tipi bazında kilit tanımı yapılabilir.

- Alış Faturası
- Satış Faturası
- Alış İrsaliyesi
- Satış İrsaliyesi
- Müşteri Siparişleri
- Satıcı Siparişleri
- Depolar Arası Transfer
- Ambar Giriş Fişi
- Ambar Çıkış Fişi
- Satış Talep,
- Satış Teklif
- Satın Alma Teklif
- Satın Alma Talep
- Stok Hareket Kayıtları
- Müstahsil Makbuz Girişi
- Genel Dekont Kaydı
- İş Emri Girişi
- Üretim Sonu Kaydı
- Serbest Üretim Sonu Kaydı
- Ters Üretim Sonu Kaydı
- Mamul Parçalama
- Üretim Akış Kaydı
- ÜAK - Üretim Sonu Kaydı
- İş Emri Malzeme Rezervasyonu
- Mamul Rezervasyonu Oluşturma

Aşağıdaki gibi tanımlanan kilit politikaları kaydedildiğinde "-3" numaralı kullanıcı grubuna bağlı herhangi bir kullanıcı tarafından, "3" numaralı depoda "HM102" stok kodu için işlem yapıldığında uyarı verilerek kayıt girişi engellenecektir.

![](../_assets/d174ecc7f702d7d96b28.png)

![](../_assets/4de5e2b1fc6d63d00b3d.png)

![](../_assets/0ec979636006968b5a31.png)
