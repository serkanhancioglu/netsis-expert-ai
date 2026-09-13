---
title: "Stok ve Maliyet Muhasebesi Modülleri"
page_id: "24740882"
product: "netsis-3-enterprise"
depth: 6
is_section: true
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Muhasebe"
  - "Muhasebe Modülü"
  - "Ekler / Muhasebe"
  - "Ek-1 Enflasyon Muhasebesi"
  - "Stok ve Maliyet Muhasebesi Modülleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / Ekler / Muhasebe / Ek-1 Enflasyon Muhasebesi / Stok ve Maliyet Muhasebesi Modülleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTM5YjljMzk1LTFhNTAtNDUyNC05ZmJiLTYzOTgyMjczMGM4ZiZsaW5rPTZlMGI0NjM2LWVmMjUtNGRjNi1hYTVhLTY0MmFiMDVkYmZkOSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=39b9c395-1a50-4524-9fbb-639822730c8f&link=6e0b4636-ef25-4dc6-aa5a-642ab05dbfd9&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "stok-ve-maliyet-muhasebesi-modulleri_41162330_24740882.html"
source_version: "2022-12-13T08:16:16.210+03:00"
source_bytes: 7231
fetched_at: "2026-09-13T04:14:35+00:00"
generator: "netsis-scraper 1.0.0"
---
# Stok ve Maliyet Muhasebesi Modülleri

Stok ve Maliyet Muhasebesi Modülleri ile ilgili ayrıntılı bilgi bu dokümandan alınabilir.

Stoklar, satın alma tarihlerinden itibaren düzeltmeye tabi tutulur ve çıkış maliyetlerinin hesaplanmasında düzeltme etkisinin dikkate alınması gerekir. Kayıtlarını TL mevzuata göre yapan firmalarda stok maliyetlendirme işlemini, dönem sonunda tüm alışları dikkate alacak şekilde yapılması zor olacağı için, ister SPK tebliği ister VUK olsun toplulaştırılmış yöntemler önerir. Logo Netsis’te Stok Modülü, enflasyon düzeltmelerini her adımda yapabildiği için, Toplulaştırılmış Yöntem kullanmadan da düzeltmeler en hassas şekilde yapılabilir.

> [!NOTE]
> Enflasyon Muhasebesi (VUK) + IAS29 (SPK) her iki uygulamayı da yapan firmalar, Stok Modülünde ancak uygulamaların birine ait, düzeltilmiş maliyet hesaplatma işlemini yapabilir. Diğer uygulama için, "Toplulaştırılmış Yöntem" uygulamak zorundadır. Hangi uygulama için "Toplulaştırılmış Yöntem", hangisi için "Stok Modülünün" kullanılacağı muhasebe parametrelerinde belirlenir.

> [!NOTE]
> Stok Modülü, düzeltme işlemi ve düzeltilmiş maliyet hesaplamasını ikinci defter mantığında yapar. Bu işlemlerde enflasyon fark hesapları düşünülmez. Satılan malın maliyeti gibi muhasebeleştirilen işlemlerde, muhasebeleştirme sırasında fark hesaplarına ayrıştırılarak atılır.

Stoklarda düzeltmelerin etkisi bir örnekle açıklanacak olursa;

İlk Madde;

Aşağıdaki tabloda X malının 1. ayda 100 TL tutarından 100 adet alındığı ve 50 adet sarf edildiği, 2. ayda ise 120 TL tutarından 100 adet alındığı ve 100 adet sarf edildiği varsayıldığında;

(Tablodaki sarf işlemi, ticari mallar için satış hareketi olarak da düşünülebilir.)

| Ay Kodu | İşlem | G/Ç | Miktar | TL.Fiyat | TL.Tutar |
| --- | --- | --- | --- | --- | --- |
| 1 | Satın Alma | G | 100 | 100 | 10.000 |
| 1 | Sarf | C | 50 | **100** | 5.000 |
| 2 | Satın Alma | G | 100 | 120 | 12.000 |
| 2 | Sarf | C | 100 | **113.33** | 11.333 |

Örnekte, 1. ve 2. ayda yapılan sarf hareketlerinin TL maliyetleri, aylık ağırlıklı ortalama yöntemine göre hesaplanır.

\2. ay Sarf Maliyeti = (50 \* 100 (Ocak bakiye) + 100 \* 120 (Şubat giriş)) / 150 = 113.33

\2. ayda enflasyon oranı %10 ve düzeltme katsayısı 1.1 ise, aşağıdaki tabloda gösterildiği gibi düzeltmeden kaynaklanan bir maliyet etkisi oluşur.

| Ay Kodu | İşlem | G/Ç | Miktar | TL.Fiyat | TL.Tutar | Düzeltilmiş Tutar |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Kalan | G | 50 | 100 | 5.000 | 5.000 |
| 2 | Satın Alma | G | 100 | 120 | 12.000 | 12.000 |
| 2 | Sarf | C | 100 | 113.33 | 11.333 | ? |
| 2 | Düzeltme | G |  |  |  | 500 |

Bu durumda,

Düzeltilmiş Sarf Maliyeti = (50 \* 100 + 500 (Düzeltme) + 100 \* 120) / 150 = 116.67

Düzeltilmiş Sarf Tutarı = 116.67 \* 100 = 11,667 olur.

Düzeltme işlemleri stok maliyetlerini etkilediği için, Enflasyona Çevrim ve Enflasyon Düzeltmesi işlemlerinin, Maliyetlendirme ve Maliyet Muhasebesi işlemlerinden önce yapılması gerekir.
