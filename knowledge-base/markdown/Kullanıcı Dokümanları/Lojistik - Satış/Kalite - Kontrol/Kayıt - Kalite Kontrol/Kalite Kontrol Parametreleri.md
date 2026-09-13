---
title: "Kalite Kontrol Parametreleri"
page_id: "22804206"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Kalite - Kontrol"
  - "Kayıt / Kalite Kontrol"
  - "Kalite Kontrol Parametreleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Kalite - Kontrol / Kayıt / Kalite Kontrol / Kalite Kontrol Parametreleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTI3ZTEwNmQ4LWZjMTQtNGE2MC04OTE0LWM0NGNhODhlNTIwNSZsaW5rPWUwYjY5OTA5LTY4OTAtNDAxMi04N2I2LTU4OWRkZDY1MTA4MyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=27e106d8-fc14-4a60-8914-c44ca88e5205&link=e0b69909-6890-4012-87b6-589ddd651083&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "kalite-kontrol-parametreleri_28148653_22804206.html"
source_version: "2022-10-25T09:26:07.240+03:00"
source_bytes: 13324
fetched_at: "2026-09-13T04:06:37+00:00"
generator: "netsis-scraper 1.0.0"
---
# Kalite Kontrol Parametreleri

Kalite Kontrol Parametreleri, firmaların kalite kontrol kayıtları sırasında, tercihlerine göre özel uygulamalar yapacakları bölümdür.

Kalite Kontrol Parametreleri modülü, "Lojistik - Satış Bölümünde" Kayıt/Kalite Kontrol menüsünün altında yer alır.

Kalite Kontrol Parametreleri ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Kalite Kontrol Parametreleri Ekranı |  |
| --- | --- |
| Satın Almada Kalite Kontrol Yapılsın | Alış irsaliyesi ile lokal depoya girişi yapılan mallar için kalite kontrol yapılması istendiğinde işaretlenmesi gereken parametredir. Bu parametre işaretlendiğinde kayıt menüsü altında bulunan "Kalite Kontrol Kaydı" bölümündeki "Departman Kodu" rehberine "Satın Alma" seçeneği eklenir. |
| Üretimde Kalite Kontrol Yapılsın | İş emrine bağlı üretilen mamul/yarı mamuller için kalite kontrol yapılması istendiğinde işaretlenmesi gereken parametredir. Bu parametre işaretlendiğinde kayıt menüsü altında bulunan "Kalite Kontrol Kaydı" bölümündeki "Departman Kodu" rehberine "Üretim" seçeneği eklenir. |
| İadede Kalite Kontrol Yapılsın | Alış irsaliyesi ile iade olarak gelen ve lokal depoya girişi yapılan mallar için kalite kontrol yapılması istendiğinde işaretlenmesi gereken parametredir. Bu parametre işaretlendiğinde kayıt menüsü altında bulunan "Kalite Kontrol Kaydı" bölümündeki "Departman Kodu" rehberine "İade" seçeneği eklenir. |
| Depolar Arası Transferde ve Ambar Giriş Fişinde Kalite Kontrol Yapılsın | Depolar arası transfer ve ambara giren mallar için kalite kontrol yapılması istendiğinde işaretlenmesi gereken parametredir. Bu parametre işaretlendiğinde kayıt menüsü altında bulunan "Kalite Kontrol Kaydı" bölümündeki "Belge Tipi" alanına "Depolar Arası Transfer" ve "Ambar Giriş Fişi" seçeneği eklenir. |
| Müstahsil Faturasında Kalite Kontrol Yapılsın | Müstahsil faturası kesilmiş mallar için kalite kontrol yapılması istendiğinde işaretlenmesi gereken parametredir. Bu parametre işaretlendiğinde kayıt menüsü altında bulunan "Kalite kontrol Kaydı" bölümündeki "Belge Tipi" alanına "Müstahsil Faturası" seçeneği eklenir. |
| Kalite Kontrol Kaydı Kapatılmayan Alış İrsaliyeleri Faturalandırılamasın | Kalite kontrol kaydı olmayan alış irsaliyelerinin faturalandırılmasının engellenmesi için kullanılan parametredir. |
| Kalite Kontrol Hareketleri Otomatik Oluşsun | Kalite kontrol hareketlerinin Grup/Ölçüm Kayıtları ve Stok/Cari Grup Eşleştirme bölümlerinde yapılan tanımlamalarına göre program tarafından otomatik olarak ekrana getirilmesi istendiğinde işaretlenmesi gereken parametredir. |
| Kalite Kontrol Ölçümleri Otomatik Oluşsun | “Kalite Kontrol Hareketleri Otomatik Oluşsun” parametresi işaretlendiğinde aktif hale gelen parametredir. Satın Alma ve Üretim işlemlerinde kalite kontrol yapılırken Stok/Cari Grup Eşleştirme bilgilerinden faydalanarak, ölçüm bilgilerinin otomatik olarak oluşmasını sağlar. Yani bir stoka hangi ölçümlerin yapılacağını ve ölçüm değerlerine göre kabul/red edilip edilmeyeceğini belirlemeye yarar. Bunun için, “Kalite Ölçüm Bilgileri” ve “Grup Ölçüm Bilgi Girişi” bölümlerinin, kalite kontrolü yapılacak stok için eksiksiz olarak doldurulması gerekir. Hareket/Ölçüm Bilgileri bölümündeki Ölçüm Değeri alanı kullanıcı tarafından tüm hareket girişleri için doldurulur. Bu durumda, "Ölçüm Sonucu" alanı, “Ölçüm Grup Bilgileri” bölümünde yapılan tanımlamalara göre program tarafından otomatik olarak oluşturulur. |
| Kalite Kontrol Numune Aralıkları Tanımlama | Kalite grup tanımlamalarında örnekleme miktarı ve diğer bilgilerin, miktar aralıkları bazında belirlenmesi için işaretlenmesi gereken parametredir. Bu parametre işaretlendiğinde, Kalite Grup Tanımlamalarına eklenen "Muayene Aralıklı Grup Tanımlama" sekmesinde örnekleme miktarları, miktar aralığı bazında belirlenir. "Muayene Tipi Tanımlama" bölümü kullanıldığında, aynı miktar aralığı için muayene kodları bazında birden fazla örnekleme miktarının tanımlanmasını sağlar. |
| Seri-Lot Girişi | Seri-Lot girişinin tanımlandığı alandır. |
| Kalite Kontrol Kayıt Kapatmadan Sonra Otomatik DAT Yapılsın | Kalite kontrol kaydı ile ilgili işlemi kapatmadan sonra depolar arası transfer işleminin otomatik olarak yapılması istendiğinde işaretlenmesi gereken parametredir. |
| Ölçüm Tanımlarında Girilen Ondalık Değerleri Kullanılsın | Ölçüm tanımlarında girilen ondalık değerlerinin kullanılması için işaretlenmesi gereken parametredir. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | İşaretlenen parametrelerle ilgili işlemlerin gerçekleşmesini sağlayan butondur. Parametrelerle ilgili işlemlerin programa yansıması için programın kapatılıp tekrar açılması gerekir. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | İşaretlenen parametrelerden vazgeçilmesi halinde kullanılan butondur. |
