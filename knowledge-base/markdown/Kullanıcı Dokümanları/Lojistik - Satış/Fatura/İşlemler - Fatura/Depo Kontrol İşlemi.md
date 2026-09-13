---
title: "Depo Kontrol İşlemi"
page_id: "24764160"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Fatura"
  - "İşlemler / Fatura"
  - "Depo Kontrol İşlemi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Fatura / İşlemler / Fatura / Depo Kontrol İşlemi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTNhYmVlZWI2LTk2MzMtNDMxNC05YWMzLTQxNWMxZTk3MTUzMCZsaW5rPWY0NDU1NzEzLTYzYWQtNDhiYi1hM2YzLWIxYTU1YWRkZTRmMCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=3abeeeb6-9633-4314-9ac3-415c1e971530&link=f4455713-63ad-48bb-a3f3-b1a55adde4f0&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "depo-kontrol-islemi_24764208_24764160.html"
source_version: "2022-10-24T21:28:04.413+03:00"
source_bytes: 77019
fetched_at: "2026-09-13T04:02:50+00:00"
generator: "netsis-scraper 1.0.0"
---
# Depo Kontrol İşlemi

Depo Kontrol İşlemi, Lojistik - Satış Bölümü'nde, "İşlemler/Fatura" menüsünün altında yer alır.

Depo Kontrol İşleminin çalıştırılabilmesi ve karşı ambardan onaylanmadığı sürece stok hareket kayıtlarına işlenmemesi için öncelikle, Satış Parametrelerindeki “Şubeler Arası Transfer Fişi Karşı Ambardan Onaylansın" parametresinin işaretlenmiş olması gerekir. Parametrenin işaretlenmesiyle birlikte “Bu Parametre Kullanıldığında, Depolar Arası Transfer Fişinde Düzeltme ve İptal İşlemi Yapılamaz” uyarısı ekrana gelir. Böylece, girilen "Depolar Arası Transfer" fişleri onaylanmadığı sürece, fişlerde değişiklik/iptal yapılabilir. Bu parametrenin işaretlenmesinden sonra kesilen "Depolar Arası Transfer" kayıtlarında, işlemin yapıldığı depodan çıkışlar stok hareket kayıtlarına işlenir ve giriş hareketleri ise 0 (sıfır) olarak aktarılır. Böylece, "Depolar Arası Transfer" kayıtlarından kaynaklanan giriş hareketlerinden dolayı stok miktarlarında değişiklik olmaz. Depo Kontrol İşlemi, Ön Sorgulama ve Depo Kontrol sekmelerinden oluşur.

Depo Kontrol İşlemi'nin sağladığı durumlar aşağıdaki şekildedir:

- Alış/satış irsaliyelerindeki stok miktarı ile depoya giren ya da sevkiyat sırasında depodan çıkan miktarı karşılaştırarak aradaki farkı listeler.
- İsteğe bağlı olarak, irsaliye miktarının depodan giren/çıkan miktar olarak değişmesini sağlar.

**Ön Sorgulama**

Depo Kontrol İşlemi ekranı Ön Sorgulama sekmesi, depo Kontrolü yapılacak belgelerin seçimi için kullanılan sekmedir.

Depo Kontrol İşlemi ekranı Ön Sorgulama sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Depo Kontrol İşlemi Ekranı |  |
| --- | --- |
| Tipi | Depo kontrolü yapılacak belge tipinin seçileceği bölümdür. Sevk edilecek ürünler için **satış irsaliyesi**, depoya girecek ürünler için ise **alış irsaliyesi** seçilir. |
| Belge No | Seçilen belge tipine göre miktar karşılaştırmasının yapıldığı alış/satış irsaliye numarasının girileceği bölümdür. ![](../../../../_assets/088477bb321d1b20c939.jpg) Rehber butonu yardımı ile belge numaraları arasından seçim yapılabilir. Bu alan boş bırakılamaz. |
| Cari Kodu | Girilen belge numarasına ait cari kod bilgisi, program tarafından otomatik olarak ekrana getirilir. |
| ![](../../../../_assets/f2915bdc16553bced2f1.png) İrsaliyeleri Getir | Verilen kısıtlara uygun irsaliyenin ekrana getirilmesi için kullanılan butondur. |
| ![](../../../../_assets/34a9caf62c728e48271a.png) Diğer Sayfa | "Depo Kontrol" sayfasına geçmek için kullanılan butondur. |

**Depo Kontrol**

Seçilen irsaliyedeki stoklar depo kontrol ekranına aktarılır. Barkod sistemi ile çalışan firmalar, barkod cihazlarını kullanarak depoya giren/çıkan ürün miktarını saydırarak programa aktarılabilirler. Aktarılan kayıtlar teslim miktarı alanında izlenir. Manuel giriş yapılacaksa stok kodu ve miktar alanına, stokların depoya giriş/çıkış miktarları girilir.

Depo Kontrol İşlemi ekranı Depo Kontrol sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Depo Kontrol İşlemi Ekranı |  |
| --- | --- |
| Stok Kodu | Stok kod bilgisinin girildiği alandır. |
| Miktar | Stok miktar bilgisinin girildiği alandır. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Tamam butonuna basıldığında, "Fark Verenler" başlıklı bir pencere ekrana gelir. İrsaliye miktarı ile depoya giriş/çıkış miktarı arasındaki fark bu ekrandan izlenir. ![](../../../../_assets/70fec53deb5aac87a9b1.png) Tekrar Tamam ![](../../../../_assets/39d77b8716226638d9ce.jpg) butonuna basıldığında, "İrsaliye miktarları güncellenecektir, onaylıyor musunuz?" şeklinde bir onay ekranı görüntülenir. Onaylandığında, irsaliye miktarı teslim miktarı ile değişir ve böylece irsaliye miktarı güncellenir. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerin iptal edildiği butondur. |
