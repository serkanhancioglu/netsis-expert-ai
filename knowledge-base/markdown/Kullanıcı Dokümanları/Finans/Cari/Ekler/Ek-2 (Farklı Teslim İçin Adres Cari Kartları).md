---
title: "Ek-2 (Farklı Teslim İçin Adres Cari Kartları)"
page_id: "22805757"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Cari"
  - "Ekler"
  - "Ek-2 (Farklı Teslim İçin Adres Cari Kartları)"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Cari / Ekler / Ek-2 (Farklı Teslim İçin Adres Cari Kartları)"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWM3YTIwZGZlLThlY2QtNDg2MC1iMzQ3LWQ4ZDUwNTI5ZTMwNCZsaW5rPTFkZTJlNjM0LTU3NDMtNGU1My04NDMyLTNmYjcyYzg0ODk0ZSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=c7a20dfe-8ecd-4860-b347-d8d50529e304&link=1de2e634-5743-4e53-8432-3fb72c84894e&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ek-2-farkli-teslim-icin-adres-cari-kartlari_29990762_22805757.html"
source_version: "2022-11-01T14:45:40.947+03:00"
source_bytes: 2440
fetched_at: "2026-09-13T04:08:50+00:00"
generator: "netsis-scraper 1.0.0"
---
# Ek-2 (Farklı Teslim İçin Adres Cari Kartları)

Ek 2 Farklı Teslim İçin Adres Cari Kartları uygulaması ile birlikte farklı teslim adresleri için cari kart açılır fakat bu kartların tipleri belirlenerek birbirleri ile ilişkilendirilebilir.

Örnek uygulama için yapılması gerekenler:

- B001 cari hesabı, teslim adresleri için açılan B001-ADR1 cari hesabı ile irsaliye işlemlerinde ve B002-ADR2 cari hesabı ile fatura işlemlerinde çalışması için ilişkilendirilir. Bunun için adres cari kartlarındaki “Bağlı Cari Kodu” alanına B001 ana cari hesabı seçilip, adres tipi için de Fatura, İrsaliye veya Ziyaret seçeneklerinden biri işaretlenir. Bu şekilde sınırsız kart açılarak birbiri ile ilişkilendirilebilir. Örnekteki gibi adres tipi "İrsaliye" olan B001-ADR1, B001-ADR2, B001-ADR3 ... gibi sınırsız sayıda kart ilişkilendirilebilir. Bu ekranda tanımlanan bağlantı adres tipinin "Dağıtım Modülü" ile ilgili uygulamalarda kullanılması için farklı değerler alması sağlanmıştır. Mevcut uygulamada, faturalama işlemlerinde adres tipi ne olursa olsun, bağlantılı adres cari hesabı olarak işlem görür.
- İrsaliye ekranındaki "Cari Kod" alanında ana cari kod çağrıldıktan sonra \<tab\> tuşu ile ilerlendiğinde, “Bağlantı Cari Seçimi” rehberi ile bağlı olan adres kartlarının listelendiği bir pencere açılır. Bu seçimle birlikte gelen rehberden adres cari hesabı seçilerek hem cari kodun hem de teslim cari kodu bilgilerinin aynı anda gelmesi sağlanır.
