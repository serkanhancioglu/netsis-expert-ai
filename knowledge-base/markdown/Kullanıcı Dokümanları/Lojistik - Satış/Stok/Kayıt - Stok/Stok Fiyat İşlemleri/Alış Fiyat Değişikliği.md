---
title: "Alış Fiyat Değişikliği"
page_id: "29994397"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Stok"
  - "Kayıt / Stok"
  - "Stok Fiyat İşlemleri"
  - "Alış Fiyat Değişikliği"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Stok / Kayıt / Stok / Stok Fiyat İşlemleri / Alış Fiyat Değişikliği"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTU4ZjIxNTY2LTVlMDYtNDE0Mi05Mjk0LTBmZjY1YWZmM2Y3NSZsaW5rPTU5OWQyYTFlLTI0MzYtNDY1OS1hY2NlLTk0NWY5Mjc3ODk0ZiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=58f21566-5e06-4142-9294-0ff65aff3f75&link=599d2a1e-2436-4659-acce-945f9277894f&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "alis-fiyat-degisikligi_29994408_29994397.html"
source_version: "2022-10-25T20:34:45.583+03:00"
source_bytes: 28071
fetched_at: "2026-09-13T04:04:15+00:00"
generator: "netsis-scraper 1.0.0"
---
# Alış Fiyat Değişikliği

Alış Fiyat Değişikliği, Lojistik - Satış Bölümü'nde, "Kayıt/Stok" menüsünün altında yer alır. Alış Fiyat Değişikliği, stoklar için, farklı amaçlı birden fazla alış fiyat listesi tanımlanması amacıyla kullanılan bölümdür. Alış Fiyat Değişikliği, Stok Kısıt Tanımları, Fiyat Seçenekleri ve Fiyat Girişi olmak üzere üç sekmeden oluşur.

**Stok Kısıt Tanımları**

Stok Kısıt Tanımları, fiyat listesi hazırlanacak veya mevcut listesinde değişiklik yapılacak stoklar için kısıt verilmesini sağlayan ya da bu stoklar için "Fiyat Girişi" sekmesindeki sıralamanın nasıl yapılacağının belirlenmesi amacıyla kullanılan sekmedir.

Stok Kısıt Tanımları/Kısıt ekranında, ilgili hücre üzerinde iken klavyede yer alan **Boşluk Çubuğuna** basıldığında bilgi girişi yapılır.

**Örneğin:** Kod-2 için kısıt verilmesi isteniyorsa, "Saha Adı" sütununun üzerinde iken boşluk çubuğuna basılması ve aşağı ok butonuna basılarak Kod-2 alanının seçilmesi gerekir. Daha sonra **Enter** tuşuna basıldığında, girilen bilgi kaydedilir ve sağdaki hücreye ilerlenir.

Birden fazla saha için kısıt verilmesi isteniyorsa, klavyede yer alan **Insert** tuşuna basarak satır eklenir. **Delete** tuşuna basılarak eklenen satırlar silinir. Sağ klik ile açılan menüden de aynı işlemler yapılabilir.
Bu sekmede girilen kısıtlara uygun stoklar, "Fiyat Girişi" ekranında listelenir.

Stok Kısıt Tanımları/Sıralama ekranında, "Fiyat Girişi" sekmesinde listelenecek stokların hangi sahaya göre sıralanacağı belirlenir. Sıralamada kullanılacak sahanın sol tarafında bulunan onay işareti fare ile çift tıklanarak veya klavyede yer alan boşluk çubuğu kullanılarak değiştirilir.

**Fiyat Seçenekleri**

Alış Fiyat Değişikliği ekranı Fiyat Seçenekleri sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Alış Fiyat Değişikliği Ekranı | Fiyat Bilgileri |
| --- | --- |
| Başlangıç Tarihi | Hazırlanacak listenin geçerlilik süresi için girilen başlangıç tarihidir. Yeni fiyatlar bu tarihten sonra geçerli hale gelir. |
| Bitiş Tarihi | Hazırlanacak listenin geçerlilik süresi için girilen bitiş tarihidir. Yeni fiyatlar bu tarihten sonra geçerliliğini yitirir. |
| Fiyat Grubu | Farklı carilere farklı liste fiyatları ile satış yapılması ve/veya bir malın farklı satıcılardan alınması durumunda, satıcılara göre farklı fiyat listelerinin oluşturulması amacıyla kullanılan alandır. Bu alana "Fiyat Grup Tanımları" bölümüne kaydedilen herhangi bir kod girildiğinde, fiyat tablosunda tüm stoklar için "Fiyat Grubu" alanına girilen kod yazılır. "Alış Fiyat Değişikliği" ekranında yer alan "Listele" seçeneği seçildiğinde, "Stok Kısıt Tanımlamaları" bölümünde verilen kısıtlara uyan tüm stok kodları ekrana gelir ve fiyatlarıyla ilgili istenen düzenleme yapılır. Yapılan düzenleme ile fiyatlar saklandığında, girilen fiyat grubuna sahip cariler için ilgili fiyatlar geçerli hale gelir. (Fatura Modülünde).<br>Bu bölümden belirlenen fiyat grubuna ait fiyatların, istenen carilerde geçerli olması için, fiyat grubunun Cari → Kayıt → Cari Hesap Kayıtları → Cari Kart-2 sekmesinde yer alan "Fiyat Grubu" alanına kaydedilmesi gerekir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, fiyat grupları arasından seçim yapılır. |
| Fiyat Kodu | "Fiyat Kodu Tanımlamaları" bölümünden kaydedilen kodun girildiği alandır. Stok kartlarında girilmiş belli bir fiyat koduna ait stok kartlarında, fiyat değişikliği yapılacak veya yeni bir liste oluşturulacaksa ilgili fiyat kodu bu alana girilir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, fiyat kodları arasından seçim yapılır. |
| Satıcı Kodu | Toplu alış/satış fiyat listesi hazırlanacak veya var olan listede değişiklik yapılacak stoklar için satıcı kodu girilen alandır. Fiyat listesi, bu alana girilen satıcı koduna sahip stoklarda hazırlanır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, cari kodlar arasından seçim yapılır. |
| Alış Fiyat Değişikliği Ekranı | Fiyat Artış Bilgileri |
| Fiyat Artış Oranı | Alış fiyatlarında yapılacak fiyat değişikliği için, artış oranının yüzde olarak girildiği alandır. Eğer var olan listede bir değişiklik yapılacaksa, listedeki fiyat baz alınarak belli oranda artış yapılır. Alış fiyatları hesaplanırken de bu oranda artış yapılır. Bu sekmede bulunan "Fiyat Kodu" alanına kod girilmesi ve girilen fiyat koduna ait tanımlamada fiyat artış oranı belirlenmiş olması halinde, "Fiyat Kodu Tanımlamaları" bölümünde belirlenen artış oranı program tarafından ekrana getirilir. |
| Alış Fiyatı/Satış Fiyatı | Alış fiyat değişikliğinde aktif olmaz ve kullanılmaz. Satış fiyat değişikliği bölümünde ise, belirlenen fiyat artış oranına göre hesaplanacak fiyatların, alış fiyatları üzerinden mi yoksa satış fiyatları üzerinden mi hesaplanacağı bu alanda belirlenir. |
| Yuvarlama | Küsuratlı çıkan fiyatlar için yuvarlama yapılması istendiğinde işaretlenmesi gereken seçenektir. |
| Yuvarlama Şekli | Yuvarlama seçeneği işaretlenmişse, ne kadar yuvarlama yapılacağının belirlendiği alandır. En fazla 0.01 kuruşa kadar yuvarlama yapılır. |
| Listele/Hesapla | Girilen kısıtlara göre herhangi bir hesaplama yapmadan, mevcut fiyatların listelenmesi için "Listele", girilen fiyat artışına göre yeni alış/satış fiyatlarının hesaplanarak listelenmesi için de "Hesapla" seçeneği kullanılır. |

**Fiyat Girişi**

Fiyat Girişi sekmesi, fiyat listesi tanımlamak için kullanılan sekmedir. "Stok Kısıt Tanımları" sekmesinde girilen kısıtlara uygun stoklar bu sekmede listelenir.

Alış Fiyat Değişikliği ekranı Fiyat Girişi sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Alış Fiyat Değişikliği Ekranı |  |
| --- | --- |
| Stok Kodu | Rehber butonu![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, stok kodu seçildikten sonra \<tab\> tuşu ile ilerlendiğinde, seçilen stokun durumu grid üzerinde yer alan listeden takip edilir. Fiyat listesi tanımlanması istenen stok kartı seçildiğinde, ilgili satır kırmızı renkte görünür. Fiyat listesi düzenlerken, fare ile fiyat alanlarının üzerine gelerek bilgi girişi yapıldıktan sonra, "Enter" tuşuna basılması gerekir. Eski fiyat alanları sadece izleme amaçlı olup, üzerinde değişiklik yapılmaz. Stok fiyat listesi tanımlamaları, stokun birinci fiyatını belirledikten sonra, diğer fiyatlara oran girmek için de kullanılır. Bunun için, birinci satış fiyatı girildikten sonra **O (Oran)** başlıklı sütun üzerinde iken, klavyede yer alan boşluk çubuğuna basarak oran seçeneğinin işaretlenmesi gerekir. Daha sonra, ikinci fiyat alanına, fiyat bilgisi yerine fiyatın hesaplanmasında kullanılacak oran girilir. "Fiyat Girişi" sekmesindeki ekranda yer alan örneğe göre; 11 kodlu stokun birinci satış fiyatı 2 TL. Birinci satış fiyatının yanındaki oran seçeneği işaretlenerek, stokun ikinci satış fiyatı için oran girileceği belirtilmiş. İkinci satış fiyatının birinci satış fiyatından %10 fazla olması isteniyorsa, fiyat alanına 110 girilerek fiyat hesaplatılır. Bu durumda stokun ikinci satış fiyatı 2.2 TL (2\*110/100) olarak hesaplanır. Hesaplamalar, oran bilgisi girilerek oluşturulan fiyat listesinde birinci fiyat üzerinden yapılır. Örneğe göre, üçüncü satış fiyatı için girilen 120 değeri ile, satış fiyatı 2.4 TL (2\*120/100) olarak hesaplanır. Oluşan fiyatlar "Stok Kartı Kayıtları" veya "Fiyat Listelerinde" görüntülenir. Fatura Modülünde, belgeler üzerine getirilen fiyatlar, belirlenen oranlarda hesaplanarak ekrana gelir. |
| ![](../../../../../_assets/b895cfce1aaec1691f5e.png) Tüm Fiyat Bilgilerini Sakla | "Fiyat Girişi" sekmesinde yer alan stoklar için yapılan fiyat tanımlamalarının saklanması için kullanılan butondur. Bu sekmede listelenen stoklar arasında fiyat girilmeyen varsa ,ilgili stoklar için de fiyat listeleri oluşmasını sağlar. |
| ![](../../../../../_assets/774159f6a159ecbe2624.png) Değişen Fiyatları Sakla | Sadece fiyat girişi yapılan stoklar için fiyat listesi oluşturulması istendiğinde kullanılan butondur. |
| ![](../../../../../_assets/f3b4c5c391c5cdd62f47.png) Aktif Kaydı Tüm Gride Yansıt | Üzerinde bulunulan satırdaki fiyat bilgilerinin, ekranda görülen tüm satırların fiyat bilgilerine program tarafından aktarılması için kullanılan butondur. Bu işlemden sonra, "Tüm Fiyat Bilgilerini Sakla" ya da "Değişen Fiyatları Sakla" butonu ile girilen fiyatlar saklanır. |
