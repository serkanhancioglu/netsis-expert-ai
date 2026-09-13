---
title: "Sayım Girişi"
page_id: "22803736"
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
  - "Sayım Girişi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Stok / İşlemler / Stok / Stok Sayım İşlemleri / Sayım Girişi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTYzNmVhYjYyLTc1MTMtNGM3Mi05NWY0LTJkMzY2ZDJkMjVmNSZsaW5rPWQxYTA1ZTRiLTczODMtNDllYS05ZmJiLWZlMmQxZmFjZWU3MyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=636eab62-7513-4c72-95f4-2d366d2d25f5&link=d1a05e4b-7383-49ea-9fbb-fe2d1facee73&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "sayim-girisi_22804475_22803736.html"
source_version: "2022-10-26T09:52:09.600+03:00"
source_bytes: 16351
fetched_at: "2026-09-13T04:04:39+00:00"
generator: "netsis-scraper 1.0.0"
---
# Sayım Girişi

Sayım Girişi, Lojistik - Satış Bölümü'nde, "İşlemler/Stok" menüsünün altında yer alır. Sayım Girişi, stok kayıtlarının sayım miktarlarının tarih bazında girildiği bölümdür. Sayım Girişi ekranı ile, stok sayım miktarının girilmesi veya önceden girilmiş bir değerin düzeltilmesi sağlanır.

Stok sayım bilgilerinin kaydı, sadece rapora yönelik olarak bu bölümden oluşturulur. Stoklarda herhangi bir hareket kaydı veya bakiye düzenlemesi, bu bölümde oluşturulmaz.

Lokal depo kullanımı olan firmaların sayım sonuçları bu bölümden kaydedilir.

Sayım Girişi ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Sayım Girişi Ekranı |  |
| --- | --- |
| Tarih | Sayımın yapıldığı tarihin girildiği alandır. |
| Cari Kodu | Lokal depoların cari bazında tutulduğu durumlarda kullanılan alandır. Bu tür uygulamalarda lokal depolardaki stokların sayım girişlerinin yapılması için, lokal depo için tanımlanmış cari kod girilir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, cari kodlar arasından seçim yapılır. |
| Sıralama Türü | Sayımı yapılan stokların, grid ekranda sıralama şeklinin belirlendiği alandır. Burada yapılan seçime göre, sayım girişi yapılan stoklar için kod veya isim sıralaması yapılır. |
| Yeni Kayıtta Sayım Miktarı 1 Gelsin | Sayım girişi yapılacak stoklar için, sayım miktarının otomatik olarak 1 gelmesi için işaretlenmesi gereken seçenektir. |
| Depo | Sayım girişi yapılacak depoya ait kod girişinin yapıldığı alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, depo kodları arasından seçim yapılır. |
| Proje Kodu | Sayım miktarlarının proje kodu bazında girilmesi için kullanılan alandır. Yardımcı Programlar → Kayıt → Şirket - Şube Parametreleri → “Proje Uygulaması Var” parametresini işaretlenmesiyle aktif hale gelen alandır. Boş bırakılmaz. |
| Fiş No | Stok → Kayıt → [Stok Parametreleri](<../../Kayıt - Stok/Stok Parametreleri.md>) → “Sayımda Açıklama ve Fiş No Girilsin” parametresinin işaretlenmesiyle aktif hale gelen alandır. En fazla 9 karakterden oluşan fiş numarası girilir. |
| Stok Kodu | Sayım girişi yapılacak stok kodunun girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, stok kodları arasından seçim yapılır. |
| Stok Adı | Sayım girişi yapılacak stok koduna ait isim bilgisinin izlendiği alandır. |
| Yapılandırma Kodu | Sayımı yapılacak stoka ait yapılandırma kodunun girildiği alandır. Stok → Kayıt → [Stok Parametreleri](<../../Kayıt - Stok/Stok Parametreleri.md>) → “Esnek Yapılandırma” parametresinin işaretli olması ve sayım girişinde seçilen stokun, yapılandırılacak stok olarak stok kartında belirlenmesi ile aktif hale gelen alandır. Boş bırakılmaz. |
| Yapılandırma Adı | Sayımı yapılacak stoka ait yapılandırma isim bilgisinin izlendiği alandır. |
| Çevrim Değeri | Stoka ait sayımın, stok kartındaki birinci ölçü birimi dışında diğer ölçü birimleri cinsinden yapılması halinde, miktarın sayım yapılan cinsten girilmesi için kullanılan alandır. Alanın sağ tarafında bulunan aşağı ok butonu ile, stok kartında tanımlı ölçü birimleri arasından seçim yapılır. |
| Miktar | Sayım sonucu oluşan miktarın girildiği alandır. |
| Açıklama | Stok Parametre Kayıtlarında bulunan “Sayımda Açıklama ve Fiş No Girilsin” parametresinin işaretlenmesiyle aktif hale gelen bölümdür. Sayım girişi ile ilgili olarak istenilen bir açıklama girilebilir. |
| Bakiye | Sayım miktarı girilecek stokun kodu yazıldığında, seçilen depoya ait stok bakiyesinin izlendiği alandır. Bakiye, sayımın yapıldığı tarihe değil içinde bulunulan tarihe aittir. Bu alan program tarafından ekrana getirilir ve elle müdahale edilmez. |
| Sayılan Stok Miktarı | Stoklara ait sayım miktarları girildikçe oluşan alandır. Birden fazla stoka ait sayım miktarının kümüle olarak izlenmesini sağlar. Program tarafından otomatik olarak oluşturulur ve elle müdahale edilmez. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır.

Kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
