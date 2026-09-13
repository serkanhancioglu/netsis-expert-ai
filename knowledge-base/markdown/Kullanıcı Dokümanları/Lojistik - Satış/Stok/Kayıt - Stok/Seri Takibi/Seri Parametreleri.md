---
title: "Seri Parametreleri"
page_id: "22803664"
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
  - "Seri Takibi"
  - "Seri Parametreleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Stok / Kayıt / Stok / Seri Takibi / Seri Parametreleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWE5NDM4NzhhLWI1ODYtNDVhNC1hYjk5LTRlZDJkNDg3MzEyOCZsaW5rPWEwMzViZmY1LTc2MTQtNGRkMS1hOWViLWViMjc5YThiNmU0YyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=a943878a-b586-45a4-ab99-4ed2d4873128&link=a035bff5-7614-4dd1-a9eb-eb279a8b6e4c&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "seri-parametreleri_29994925_22803664.html"
source_version: "2022-10-25T21:13:23.617+03:00"
source_bytes: 26765
fetched_at: "2026-09-13T04:04:25+00:00"
generator: "netsis-scraper 1.0.0"
---
# Seri Parametreleri

Seri Parametreleri, Lojistik - Satış Bölümü'nde, "Kayıt/Stok" menüsünün altında yer alır. Seri Parametreleri, seri uygulamasında sektörlere göre farklı seçeneklerin belirlenmesi ve düzenli bir seri takibinin yapılması için kullanılacak parametrelerden oluşan bölümdür.

Seri Parametreleri, Yardımcı Programlar → Kayıt → [Şirket-Şube Parametre Kayıtları](<../../../../Genel/Yardımcı Programlar/Kayıt - Yardımcı Programlar/Şirket - Şube - Parametre Tanımları.md>) → “Seri Takibi Yapılsın” parametresinin işaretlenmesi ile aktif hale gelir. İşaretlenmediğinde ekranda pasif olarak görüntülenir.

Seri uygulamasının ne şekilde kullanılacağı, seçilecek parametreler ile belirlenir.

Seri Parametreleri ekranı Genel ve Otomatik Seri sekmesinden oluşur.

**Genel**

Seri Parametreleri ekranı Genel sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Seri Parametreleri Ekranı |  |
| --- | --- |
| Seri Stok Bazında Tek Olsun | Serilerin stok bazında tek olması için kullanılan parametredir. |
| Seri Girişinde Kullanılacak Opsiyonel Sahalar | Seçilen sahaların "Seri Girişi" ekranında kullanılması için işaretlenmesi gereken parametre alanıdır. Miktar-2, Seri No-3, Açıklama-3, Son Kullanma Tarihi, Seri No-4, Açıklama-4 seçeneklerinden oluşur. |
| Tarihsel Seri Bakiye Kontrolü Yapılsın | "Seri Takibi" ekranındaki seri rehberinde, seri bakiye bilgilerinin belge tarihine göre hesaplanması ve "FIFO Çıkış Seri" butonunun girilen belge tarihine göre tarihsel bakiye kontrolü yaparak çalışması için kullanılan parametredir. |
| Seri Takibi Ekranında Seri Girişi Zorunlu Olsun | "Seri Takibi" ekranında, girilen seri miktarı "0" olduğunda ekranın kapanmasını engelleyerek, seri girişini zorunlu tutan parametredir. |
| Miktarsız Kalem İçin Seri Girişi Yapılsın | Fatura belgelerinde miktar "0" girildiğinde de "Seri Takibi" ekranının açılmasını sağlayan parametredir. |
| İade Tipli Girişlerde Seri Girişi Yapılsın | "Girişlerde Seri Takibi" parametresi işaretli değilken, iade tipli alış faturasında seri ekranının açılmasını sağlayan parametredir. |
| İş Emri Reçetesinde Seri Girişi Yapılsın | İş emri reçetesinde sarf edilecek bileşenler için seri girişinin yapılmasını sağlayan parametredir. |
| Seri Rehberinden Miktar Bilgisi 1 Olarak Alınsın | Seri rehberinden seçilen serili stokların miktarı seri ekranına 1 olarak aktarılması için kullanılan parametredir. Seri miktarının birden fazla ayrı seriden kullanılması durumunda, seri miktarlarını "0" olarak düzeltip miktar girilmesi sürecinde kolaylık sağlar. |
| FIFO Seri İçin Sıralama Kriteri | "Seri Takibi" ekranındaki FIFO çıkış seri işleminde serilerin seçili değere göre sıralanarak ekrana getirilmesi için kullanılan parametre alanıdır. Alanın sağ tarafında yer alan aşağı ok butonu ile seçenekler arasından seçim yapılır. |
| FIFO Seri İçin Proje Kodu Kontrol Edilsin | FIFO çıkış seri işleminde, hareketteki proje kodu kontrol edilerek ekrana ilgili proje koduna ait serilerin sıralanarak getirilmesi için kullanılan parametredir. |
| Son Kullanma Tarihi Risk Süresine Göre Hesaplansın | Giriş tipli seri hareketleri için son kullanma tarihi (SKT) bilgisinin, stok kartındaki risk süresi ve zaman birimine göre otomatik hesaplanması için kullanılan parametredir. Seri girişinde SKT'nin, belge tarihi+risk süresi kadar hesaplanıp otomatik doldurulmasını sağlar. |
| Hesaplanan Son Kullanma Tarihi Değiştirilemesin | Kullanıcıların SKT'yi değiştirememesi için kullanılan parametredir. |
| ![](../../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilgilerin onaylanması için kullanılan butondur. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |

**Otomatik Seri**

Seri Parametreleri ekranı Otomatik Seri sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Seri Parametreleri Ekranı |  |
| --- | --- |
| Seri Ürün Bazında Tek Olsun | Sadece stok giriş hareketlerinde baz alınır. Seri numaralarının her bir stok kartı bazında tek (tekrarsız) olması istendiği durumlarda işaretlenmesi gereken parametredir. Böylece, stok girişlerinde girilen seri numarasının daha önce girilip girilmediği kontrol edilir ve girilmişse aynı serinin girişine izin verilmez. Parametrenin işaretlenmemesi durumunda, aynı seriden birden fazla girişe izin verilir. |
| Seri Kodu Girişler İçin Otomatik Hesaplansın | Diğer parametrelere verilecek yanıtlara göre, Stok Hareket Kayıtlarından elle (manuel), Fatura/Üretim Modülünden otomatik yapılacak stok girişlerinde seri numarasının program tarafından otomatik hesaplanmasını sağlayan parametredir. Parametre işaretlendiğinde Stok Hareket Kayıtları, Üretim ve Fatura Modülünden yapılan girişlerde, açılan seri penceresinde en az 1 adet (stok kartı seri parametrelerine bağlı olarak değişir) seri otomatik hesaplanarak gelir. Stok → Kayıt → Stok Kartı Kayıtları → Seri Takibi → “Miktar Kadar Seri Sorulsun” parametresi işaretlendiğinde, stok girişlerinde girilen miktar kadar seri otomatik hesaplanır. İşaretlenmediğinde, girilen miktar için 1 adet seri hesaplanır ve istendiğinde bu seriye ait miktar düzeltilip, kalan miktarlar için elle seri girilmesine izin verilir. "Seri Kodu Girişler İçin Otomatik Hesaplansın" parametresi işaretlenmediğinde, stok kartlarında ayrıca sorgulanan otomatik hesaplama yapılmaz. Bazı kartlarda otomatik hesaplama, bazı kartlarda ise elle (manuel) seri girişi yapılacak ise, bu parametrenin işaretlenmesi ve ayrımın kartlar bazında yapılması tavsiye edilir. |
| Seri Kodu Çıkışlar İçin Otomatik Hesaplansın | Diğer parametrelere verilecek yanıtlara göre, Stok Hareket Kayıtlarından elle (manuel), Fatura/Üretim Modülünden otomatik yapılacak stok çıkışlarında seri numarasının program tarafından otomatik hesaplanmasını sağlayan parametredir. Parametre işaretlendiğinde Stok Hareket Kayıtları, Üretim ve Fatura Modülünden yapılan çıkışlarda, açılan seri penceresinde en az 1 adet (stok kartı seri parametrelerine bağlı olarak değişir) seri otomatik hesaplanarak gelir. Stok → Kayıt → Stok Kartı Kayıtları → Seri Takibi → “Miktar Kadar Seri Sorulsun” parametresi işaretlendiğinde, stok çıkışlarında girilen miktar kadar seri otomatik hesaplanır. İşaretlenmediğinde, çıkılan miktar için 1 adet seri hesaplanır ve istendiğinde bu seriye ait miktar düzeltilip, kalan miktarlar için elle seri girilmesine izin verilir. Stok → Kayıt → Stok Kartı Kayıtları → Seri Takibi → "Bakiye Kontrolü Yapılsın" parametresi işaretlendiğinde, çıkışlarda otomatik seri hesaplanmaz. "Seri Kodu Girişler İçin Otomatik Hesaplansın" parametresi işaretlenmediğinde, stok kartlarında ayrıca sorgulanan otomatik hesaplama yapılmaz. Bazı kartlarda otomatik hesaplama, bazı kartlarda ise elle (manuel) seri çıkışı yapılacak ise, bu parametrenin işaretlenmesi ve ayrımın kartlar bazında yapılması tavsiye edilir. |
| Stok Kodu Başlangıç Değer Kabul Edilsin | “Seri Kodu Girişler/Çıkışlar İçin Otomatik Hesaplansın” parametrelerinden herhangi biri işaretlendiğinde aktif hale gelen parametredir. Parametre işaretlendiğinde, otomatik hesaplanan seri kodunun başına ilgili stokun kodu eklenir. **Örneğin:** "CEPTEL" koduna sahip bir stok için seri hesaplandığında, oluşan seri "CEPTEL1" gibidir. |
| Seri Numarasında Yıl Bilgisi Olsun | “Seri Kodu Girişler/Çıkışlar İçin Otomatik Hesaplansın” parametrelerinden herhangi biri işaretlendiğinde aktif hale gelen parametredir. Parametre işaretlendiğinde, otomatik hesaplanacak seri numarasının içinde, yıl bilgisinin de bulunması sağlanır. **Örneğin:** "CEPTEL" koduna sahip bir stok için seri hesaplandığında, oluşan seri "CEPTEL20011" gibidir. |
| Seri Numarasında Ay Bilgisi Olsun | “Seri Kodu Girişler/Çıkışlar İçin Otomatik Hesaplansın” parametrelerinden herhangi biri işaretlendiğinde aktif hale gelen parametredir. Parametre işaretlendiğinde, otomatik hesaplanacak seri numarasının içinde, yıl bilgisinin de bulunması sağlanır. **Örneğin:** "CEPTEL" koduna sahip bir stok için seri hesaplandığında, oluşan seri "CEPTEL2001101" gibidir. |
| Seri Numarasında Gün Bilgisi Olsun | “Seri Kodu Girişler/Çıkışlar İçin Otomatik Hesaplansın” parametrelerinden herhangi biri işaretlendiğinde aktif hale gelen parametredir. Parametre işaretlendiğinde, otomatik hesaplanacak seri numarasının içinde, yıl bilgisinin de bulunması sağlanır. **Örneğin:** "CEPTEL" koduna sahip bir stok için seri hesaplandığında, oluşan seri "CEPTEL200110261" gibidir. |
| Seri Numarası Uzunluğu | “Seri Kodu Girişler/Çıkışlar İçin Otomatik Hesaplansın” parametrelerinden herhangi biri işaretlendiğinde aktif hale gelen alandır. Otomatik hesaplanacak seri numaraları için, en fazla girilecek uzunluk belirlenir. Burada belirlenen uzunluk kadar seri numarası oluşturulur. |
| ![](../../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilgilerin onaylanması için kullanılan butondur. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
