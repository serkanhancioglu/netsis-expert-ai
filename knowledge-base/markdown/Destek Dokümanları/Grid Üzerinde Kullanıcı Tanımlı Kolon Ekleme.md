---
title: "Grid Üzerinde Kullanıcı Tanımlı Kolon Ekleme"
page_id: "90669103"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Grid Üzerinde Kullanıcı Tanımlı Kolon Ekleme"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Grid Üzerinde Kullanıcı Tanımlı Kolon Ekleme"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTcwM2ZmYTQ4LTA5MzgtNGNmNy1hNTExLTc2NmFhYTZjOTA2OSZsaW5rPWI4YzBhYjQxLWE1MDQtNDU0ZC05NDYxLWNhYTUzODdiZTM1ZSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=703ffa48-0938-4cf7-a511-766aaa6c9069&link=b8c0ab41-a504-454d-9461-caa5387be35e&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "grid-uzerinde-kullanici-tanimli-kolon-ekleme_90670240_90669103.html"
source_version: "2022-11-02T14:15:46.097+03:00"
source_bytes: 311572
fetched_at: "2026-09-13T04:23:54+00:00"
generator: "netsis-scraper 1.0.0"
---
# Grid Üzerinde Kullanıcı Tanımlı Kolon Ekleme

Grid Üzerinde Kullanıcı Tanımlı Kolon Ekleme ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Netsis 9.0.42 sürümü ile sabit tanım ekranlarında bulunan grid nesnelerine, kullanıcı tanımlı kolon ekleme desteği sağlanmıştır. grid üzerinde kullanıcı tanımlı kolon ekleme özelliği ile program genelinde bulunan sabit tanım ekranlarına (Cari Hesap Kayıtları, Stok Kartı Kayıtları, Hesap Planı, Banka Hesap Kayıtları vb.) kullanıcı tanımlı kolonlar eklenebilmektedir.

Mevcut gride yeni bir kolon eklemek için grid üzerinde sağ klik yapılarak açılan menüde bulunan "Kullanıcı Tanımlı Kolon Ekleme" seçeneği tıklanmalıdır.

![](../_assets/842871341fe974102ce1.png)

"Kullanıcı Tanımlı Kolon Ekleme" ekranının üst bölümünde, gridin hangi veritabanı nesnesinden hangi alanları listelediğini içeren mevcut sorgusu gösterilmektedir. Gride bir veya birden fazla kolon eklemek için aşağıda bulunan kolon başlığı, alan adı, kolon sorgusu, NDS tip alanları doldurulmalıdır.

Örneğin; Stok kartı kayıtları ekranında bulunan gride stok bakiyelerinin yeni bir kolon olarak eklenmesi için tanımlama aşağıdaki gibi yapılabilir.

![](../_assets/e62cbc359d9a293c0582.png)

Kayıt işlemi başarıyla tamamlandığında eklenen tüm kullanıcı tanımlı kolonları da listeleyecek şekilde çalıştırılacak sorgunun son hali ekranda gösterilmektedir.
![](../_assets/d7a96ad565ad4f230353.png)

![](../_assets/f394550e444a966c229d.png)
