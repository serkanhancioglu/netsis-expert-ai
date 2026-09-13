---
title: "Sayım Bağlantısız Bakiye Sıfırla"
page_id: "22803745"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Stok"
  - "İşlemler / Stok"
  - "Stok Sayım İşlemleri"
  - "Sayım Bağlantısız Bakiye Sıfırla"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Stok / İşlemler / Stok / Stok Sayım İşlemleri / Sayım Bağlantısız Bakiye Sıfırla"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWFkYTc2NWJlLWQwMTYtNDcxOC04YTBhLTU1ZThmZDUxZjg0NCZsaW5rPWIyOWE0YTVmLThmOGUtNDJjMy05MmEzLWQxNGQ0NjIyMDQ2OSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=ada765be-d016-4718-8a0a-55e8fd51f844&link=b29a4a5f-8f8e-42c3-92a3-d14d46220469&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "sayim-baglantisiz-bakiye-sifirla_22804486_22803745.html"
source_version: "2022-10-26T09:56:39.827+03:00"
source_bytes: 21929
fetched_at: "2026-09-13T04:04:40+00:00"
generator: "netsis-scraper 1.0.0"
---
# Sayım Bağlantısız Bakiye Sıfırla

Sayım Bağlantısız Bakiye Sıfırla, Lojistik - Satış Bölümü'nde, "İşlemler/Stok" menüsünün altında yer alır. Sayım Bağlantısız Bakiye Sıfırla, stoklardaki bakiyelerin girilen sayım bilgilerine bakılmaksızın giriş/çıkış hareketleri oluşturarak sıfır bakiyeye getirilmesi için kullanılan bölümdür. Sayım Bağlantısız Bakiye Sıfırla işlemi çalıştırıldığında, stokların son bakiyelerine bakılır ve bu bakiyeler sıfıra eşitlenir.

Sayım Bağlantısız Bakiye Sıfırla ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Sayım Bağlantısız Bakiye Sıfırla Ekranı |  |
| --- | --- |
| Hareket Tarihi | İlgili stok hareketlerini sıfırlamak için, aktarılacak giriş/çıkış hareketine verilen tarihtir. |
| Maliyet İçin Sınır Tarihi | Bakiyelerin sıfırlanması amacıyla, aktarılacak giriş/çıkış hareketlerinde hesaplanan birim fiyat hesaplaması için girilen sınır tarihidir. |
| Maliyet Tipi | Aktarılacak hareketlerde hesaplanan birim fiyat için kullanılacak maliyet tipinin seçildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile maliyet tipleri arasından seçim yapılır. |
| Açıklama | Stok hareket kayıtlarına aktarılacak hareket için açıklama bilgisi girilen alandır. **Örneğin:** Stok sıfırlama sebebi girilebilir. |
| Stok Bakiye Sınır Tarihi | Stok hareket kayıtlarında hangi tarihe ait bakiyenin sıfırlanacağı ile ilgili sınır tarihi girilen alandır. |
| Depo Kodu Aralığı | Lokal depo uygulamasının kullanıldığı ve stok bakiyelerinin lokal depo bazında takip edildiği durumlarda, stokların hangi depolardaki bakiyelerinin sıfırlanacağı ile ilgili depo kodu aralığı girilen alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, depo kodları arasından seçim yapılır. |
| Stok Kodu (Başlangıç) | Bakiyelerin sıfırlanması amacıyla, başlangıç stok kodunun girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, stok kodları arasından seçim yapılır. |
| Stok Kodu (Bitiş) | Bakiyelerin sıfırlanması amacıyla, bitiş stok kodunun girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, stok kodları arasından seçim yapılır. |
| Sadece Eksi Bakiyeye Düşen Stoklar İşlensin | Stok hareketlerindeki bakiyelerin sıfırlanması ile ilgili işlemin, sadece eksi bakiyeli stoklar için çalışmasını sağlayan seçenektir. Bu seçeneğin işaretlenmesi halinde, bakiyesi sıfırdan büyük stokların bakiyeleri sıfırlanmaz. Sadece eksi bakiyeli stokların bakiyesi sıfırlanır. Program, Dövizli muhasebe kullanıldığında, bakiye kapatma satırlarını işlerken birim döviz maliyetini de bulur ve operasyon döviz tutarına aktarır. Bu işlem sırasında, döviz tipi olarak tanımlanan firma döviz tipini kullanır. Birim döviz maliyetini hesaplarken, girilen tarih aralığında stok hareket kayıtlarındaki firma döviz tutarlarından faydalanır. Dolayısıyla, bu işlemden önce firma döviz tutarlarının oluşması için önceden Stok → İşlemler → Stok Döviz Çevrim bölümünün çalıştırılması gerekir. |
| Proje Kodu (Başlangıç) | Bakiyelerin sıfırlanması amacıyla, başlangıç proje kodunun girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, proje kodları arasından seçim yapılır. |
| Proje Kodu (Bitiş) | Bakiyelerin sıfırlanması amacıyla, bitiş proje kodunun girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, proje kodları arasından seçim yapılır. |
| ![](../../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilginin onaylanmasını sağlayan butondur. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgiden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
