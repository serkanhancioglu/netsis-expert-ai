---
title: "Sayım Bağlantısız Bakiye Sıfırlama"
page_id: "95650749"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Dinamik Depo"
  - "Kayıt / Dinamik Depo"
  - "Hücre Sayım İşlemleri"
  - "Sayım Bağlantısız Bakiye Sıfırlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Dinamik Depo / Kayıt / Dinamik Depo / Hücre Sayım İşlemleri / Sayım Bağlantısız Bakiye Sıfırlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWZlNGU2NjEyLWE1YzAtNGNkNy04OTQzLTM0NTJiM2I5MTU5NyZsaW5rPWEwMjM1N2NhLTBjOTEtNDQxNi1hMWY1LWY1OGJmNGNhOTg4ZCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=fe4e6612-a5c0-4cd7-8943-3452b3b91597&link=a02357ca-0c91-4416-a1f5-f58bf4ca988d&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "sayim-baglantisiz-bakiye-sifirlama_95650749_95650749.html"
source_version: "2022-10-31T11:49:09.407+03:00"
source_bytes: 16254
fetched_at: "2026-09-13T04:06:12+00:00"
generator: "netsis-scraper 1.0.0"
---
# Sayım Bağlantısız Bakiye Sıfırlama

Sayım Bağlantısız Bakiye Sıfırlama, Dinamik Depo-Kayıt menüsünün altında yer alır. Sayım Bağlantısız Bakiye Sıfırlama, hücrelerdeki bakiyelerin girilen sayım bilgilerine bakılmaksızın giriş/çıkış hareketleri oluşturarak sıfır bakiyeye getirilmesi için kullanılan bölümdür. Sayım Bağlantısız Bakiye Sıfırlama işlemi çalıştırıldığında, hücrelerin son bakiyelerine bakılır ve bu bakiyeler sıfıra eşitlenir.

Sayım Bağlantısız Bakiye Sıfırlama ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Sayım Bağlantısız Bakiye Sıfırlama |  |
| --- | --- |
| Hücre Kodu | Sıfırlama işleminin belirli bir hücre kodu aralığı için yapılması istendiği zaman kullanılan alandır. Rehber butonu ile hücre kodları listesine ulaşılır. |
| Fiş No | Sıfırlama işlemi işlenirken bir fiş numarasına bağlanması istendiği zaman kullanılan alandır. |
| Stok Hareketlere İşlensin | Hücre sıfırlama işlemi stoklara işlensin istenirse kullanılan parametredir. Bu parametre işaretlendiğinde aşağıdaki bölüm aktif hale gelir ve burada stoklar için istenen kısıtlar girilebilir. Sayım bağlantısız stok sayım sıfırlama işlemi hücre ile birlikte gerçekleşmiş olur. |
| Depo Kodu | Belirli bir depo içindeki hücreler için sıfırlama işlemi yapılmak istendiği zaman kullanılan alandır. Rehber butonu ile depo kodları listesine ulaşılır. |
| Hareket Tarihi | İlgili stok hareketlerini sıfırlamak için, aktarılacak giriş/çıkış hareketine verilen tarihtir. |
| Maliyet İçin Sınır Tarihi | Bakiyelerin sıfırlanması amacıyla, aktarılacak giriş/çıkış hareketlerinde hesaplanan birim fiyat hesaplaması için girilen sınır tarihidir. |
| Maliyet Tipi | Aktarılacak hareketlerde hesaplanan birim fiyat için kullanılacak maliyet tipinin seçildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile maliyet tipleri arasından seçim yapılır. |
| Açıklama | Stok hareket kayıtlarına aktarılacak hareket için açıklama bilgisi girilen alandır. **Örneğin:** Stok sıfırlama sebebi girilebilir. |
| Stok Bakiye Sınır Tarihi | Stok hareket kayıtlarında hangi tarihe ait bakiyenin sıfırlanacağı ile ilgili sınır tarihi girilen alandır. |
| Stok Kodu (Başlangıç) | Bakiyelerin sıfırlanması amacıyla, başlangıç stok kodunun girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, stok kodları arasından seçim yapılır. |
| Stok Kodu (Bitiş) | Bakiyelerin sıfırlanması amacıyla, bitiş stok kodunun girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, stok kodları arasından seçim yapılır. |
| Sadece Eksi Bakiyeye Düşen Stoklar İşlensin | Stok hareketlerindeki bakiyelerin sıfırlanması ile ilgili işlemin, sadece eksi bakiyeli stoklar için çalışmasını sağlayan seçenektir. Bu seçeneğin işaretlenmesi halinde, bakiyesi sıfırdan büyük stokların bakiyeleri sıfırlanmaz. Sadece eksi bakiyeli stokların bakiyesi sıfırlanır. Program, Dövizli muhasebe kullanıldığında, bakiye kapatma satırlarını işlerken birim döviz maliyetini de bulur ve operasyon döviz tutarına aktarır. Bu işlem sırasında, döviz tipi olarak tanımlanan firma döviz tipini kullanır. Birim döviz maliyetini hesaplarken, girilen tarih aralığında stok hareket kayıtlarındaki firma döviz tutarlarından faydalanır. Dolayısıyla, bu işlemden önce firma döviz tutarlarının oluşması için önceden Stok → İşlemler → [Stok Döviz Çevrim](<../../../Stok/İşlemler - Stok/Stok Döviz Çevrim.md>) bölümünün çalıştırılması gerekir. |
| ![](../../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilginin onaylanmasını sağlayan butondur. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgiden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
