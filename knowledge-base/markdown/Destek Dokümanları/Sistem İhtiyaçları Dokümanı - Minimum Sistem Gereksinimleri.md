---
title: "Sistem İhtiyaçları Dokümanı / Minimum Sistem Gereksinimleri"
page_id: "50679743"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Sistem İhtiyaçları Dokümanı / Minimum Sistem Gereksinimleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Sistem İhtiyaçları Dokümanı / Minimum Sistem Gereksinimleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTlkZThkNGI4LWJmMDItNGRjOS04MWNhLTU2MjFkNTM1OTQzMSZsaW5rPThlYWRkZmEzLTc0ZTMtNDRhNy1hZWNjLWIxY2NlNDc2ZDZmMiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=9de8d4b8-bf02-4dc9-81ca-5621d5359431&link=8eaddfa3-74e3-44a7-aecc-b1cce476d6f2&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "sistem-ihtiyaclari-dokumani-minimum-sistem-gereksinimleri_82575631_50679743.html"
source_version: "2023-03-17T14:50:53.310+03:00"
source_bytes: 7388
fetched_at: "2026-09-13T04:25:46+00:00"
generator: "netsis-scraper 1.0.0"
---
# Sistem İhtiyaçları Dokümanı / Minimum Sistem Gereksinimleri

Netsis Wings Enterprise, Netsis Wings, Netsis Wings Entegre, Netsis 3 Enterprise, Netsis 3 Standard, Netsis 3 Entegre ile ilgili sistem ihtiyaçları bilgisine bu dokümandan ulaşabilirsiniz.

#### SİSTEM İHTİYAÇLARI

##### Sunucu

Sistem ihtiyaçları için donanım gereksinimleri aşağıdaki şekildedir:

- Intel ve Intel uyumlu işlemci (Tavsiye edilen)
- 1-5 kullanıcı için Intel Xeon Processor E5607 (8M Cache, 2.26 GHz, 4.80 GT/s Intel QPI) ve üzeri işlemci, 8 GB ve üzeri bellek, RAID 5 disk, Minimum 20 GB boş disk alanı.
- 6-10 kullanıcı için Intel Xeon Processor L5618 (12M Cache, 1.87 GHz, 5.86 GT/s Intel QPI) ve üzeri işlemci, 16 GB ve üzeri bellek, RAID 5 disk, Minimum 40 GB boş disk alanı.
- 11-20 kullanıcı için çift işlemcili Intel Xeon Processor E5620 (12M Cache, 2.40 GHz, 5.86 GT/s Intel QPI) ve üzeri, 32 GB bellek ve üzeri bellek, RAID 1 + 0 disk, Minimum 60 GB boş disk alanı.
- 21-50 kullanıcı arası en az çift işlemcili Intel Xeon Processor L5638 (12M Cache, 2.00 GHz, 5.86 GT/s Intel QPI) X 2, 64 GB bellek ve üzeri, RAID 1 + 0 disk, Minimum 80 GB boş disk alanı.
- 51-100 kullanıcı arası Intel Xeon Processor E5645 (12M Cache, 2.40 GHz, 5.86 GT/s Intel QPI) X 4, 128 GB bellek ve üzeri, FIBER SAN Storage, en az 16 SCSI SAS disk ile RAID 1 + 0 disk, Minimum 100 GB boş disk alanı.
- 101-200+ kullanıcı arası Intel Xeon Processor E5649 (12M Cache, 2.53 GHz, 5.86 GT/s Intel QPI) X 8, 256 GB bellek ve üzeri, FIBER SAN Storage, en az 16 SCSI SAS disk ile RAID 1 + 0 disk, Minimum 200 GB boş disk alanı.
- Disk sistemi için pil yedeklemeli, yüksek ön bellekli (512 MB ve üstü) RAID control kartı ve RAID seviyesi olarak, RAID 5 veya RAID 1 + 0 tercih edilmelidir. 100 kullanıcı ve üzerindeki sistemlerde Fiber Channel SCSI SAN Storage önerilir.
- Sunucu üzerinde, tüm disk yedeğini alabilecek kapasitede yedekleme ünitesi bulunmalıdır. (LTO (Linear Tape- Open), DLT (Digital Linear Tape), AIT (Advanced Intelligent tape) vb.)
- Gigabit LAN

```text
           Not: Donanım gereksinimleri sadece Logo uygulaması içindir. Ek uygulamalar ayrıca değerlendirilmelidir. Aksi takdirde ciddi performans problemlerine sebep olabilir.
```

##### Yazılım

Sistem ihtiyaçları için yazılım gereksinimleri aşağıdaki şekildedir:

- MS SQL
- MS SQL Server 2008 R2 ve üzeri versiyonlar tavsiye edilmektedir.
- MS Windows Server 2012 işletim sistemi
- Net Framework 4.7.2
- MS Internet Explorer 10+
- Office uygulamaları ile entegre işlemler yapılacak ise (e-posta gönderimi, Excel 'den veri aktarımı) MS Office 2010 ve üzeri olmalıdır.

SQL Server/2012/2014 ve 2016 Express en fazla 1 CPU (4 core), 1 GB bellek ve tüm veritabanlarının veri toplamı 10 GB'la sınırlıdır. Logo tarafından production ortam için önerilmemektedir.

- Oracle 10G (11.2.0.5) ve üzeri veri tabanlarını tavsiye eder.
- 11G R2 (11.2.0.4) ve 12C (Multitenant Container Databases) tarafından desteklenen işletim sistemleri.
- Net Framework 4.7.2
- MS Internet Explorer 10+
- Office uygulamaları ile entegre işlemler yapılacak ise (e-posta gönderimi, Excel 'den veri aktarımı) MS Office 2010 ve üzeri olmalıdır.

Sunucu üzerinde bir başka "Server" uygulaması (örneğin Microsoft Exchange Server) çalıştırılmamalıdır. Bu tip uygulamalar için ayrı bir sunucu kullanılmalıdır.

#### İstemci (Uzak Masaüstü veya Yerel Kurulum Üzerinden Kullanım)

İstemci (Uzak Masaüstü veya Yerel Kurulum Üzerinden Kullanım) için Donanım gereksinimleri aşağıdaki şekildedir:

- Intel Core i3-4130 Processor (3M Cache, 3.40 GHz)
- En az 2 GB Bellek (Tavsiye edilen 2 GB ve üzeri)
- Gigabit LAN (<u>Wi-Fi kesinlikle önerilmemektedir</u>)

İstemci için Yazılım gereksinimleri aşağıdaki şekildedir:

- MS Windows 7 Professional ve üzeri (8/10)
- En az 2 GB bellek ve üzeri
- Oracle Veritabanı kullanılan sistemler için Oracle istemci yazılımı (11G R2 ve üzeri).
- Oracle Veritabanı kullanılan sistemler için Oracle OLE DB sürücüsü (11G R2 ve üzeri).
- İstemci makinada e-defter kullanılacak ise Oracle JRE 1.6 ya da üzeri kurulu olmalıdır.
- İstemci makinada e-fatura oluşturulacak ise Msxml 4.0 yüklü olmalıdır.
- İstemci makinada Office uygulamaları ile entegre işlemler yapılacak ise (e-posta gönderimi, Excel 'den veri aktarımı) MS Office 2010 ve üzeri olmalıdır.
- Net Framework 4.5
- MS Internet Explorer 10+

Ağ ortamında işletim sistemlerinin "Starter","Single Language" sürümü kullanılamaz. "Home" sürümlerinin kullanılması tavsiye edilmez.

#### İstemci (Wings Üzerinden Kullanım)

İstemci Wings Üzerinden Kullanım) için Donanım gereksinimleri aşağıdaki şekildedir:

- HTML5 desteği sunan web tarayıcısı.
- Tavsiye edilen web tarayıcıları: Chrome, Firefox, Opera, IE 10+
