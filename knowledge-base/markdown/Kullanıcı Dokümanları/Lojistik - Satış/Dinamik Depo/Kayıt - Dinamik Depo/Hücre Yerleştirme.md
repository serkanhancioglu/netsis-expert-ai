---
title: "Hücre Yerleştirme"
page_id: "22803909"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Dinamik Depo"
  - "Kayıt / Dinamik Depo"
  - "Hücre Yerleştirme"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Dinamik Depo / Kayıt / Dinamik Depo / Hücre Yerleştirme"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTk2YTdiODA5LWJhMjctNDFjNy1iMDQzLWE3YzkzYjVjOGE2YiZsaW5rPWRiOTE0NTE2LWU5M2YtNGNlOS1hMWQyLWIyMTRiMWYxOTkzNSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=96a7b809-ba27-41c7-b043-a7c93b5c8a6b&link=db914516-e93f-4ce9-a1d2-b214b1f19935&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "hucre-yerlestirme_22804625_22803909.html"
source_version: "2022-10-31T10:29:46.357+03:00"
source_bytes: 83156
fetched_at: "2026-09-13T04:06:07+00:00"
generator: "netsis-scraper 1.0.0"
---
# Hücre Yerleştirme

Hücre Yerleştirme, Dinamik Depo-Kayıt menüsünün altında yer alır. Hücre Yerleştirme, daha önceden kaydedilen/girişi yapılan ürünlerin hücrelere yerleştirilmesi için kullanılan bölümdür. Hücre Yerleştirme bölümünde, Fatura modülündeki Alış İrsaliyesi, Alış Faturası, Ambar Giriş Fişi ve Depolar Arası Transfer seçenekleri kullanılarak girilen stoklar hücrelere yerleştirilir.

Hücre Yerleştirme ekranı Ön Sorgulama ve Yerleştirme olmak üzere iki sekmeden oluşur.

**Ön Sorgulama**

![](../../../../_assets/a35b13c81b8a811e07f8.png)

Hücre Yerleştirme ekranı Ön Sorgulama sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Hücre Yerleştirme Ekranı |  |
| --- | --- |
| Tipi | Hangi bölümden girilen stokların hücrelere yerleştirileceği bilgisinin seçildiği alandır. Tipi alanı; Alış İrsaliyesi, Alış Faturası, Ambar Giriş Fişi, Depolar Arası Transfer ve Üretim seçeneklerinden oluşur. Örneğin, Alış Faturası ile girilen bir faturadaki kalemler hücrelere yerleştirilecek ise, Alış Faturası seçeneğinin seçilmesi gerekir. |
| Belge No | Tipi alanından seçilen belge tipine göre; ilgili belgelerin listesi, Belge No alanındaki Rehber butonu ile ekrana getirilebilir veya elle yerleştirme yapılacak belge numarası girilebilir. |
| Cari Kodu | Girilen belge numarasındaki cari kod, bu alana otomatik olarak gelir. |
| Kalemleri Getir | Kalemleri Getir butonuna tıklandığında; ilgili belgede lokasyon takibi yapılan depo kodu ile kaydedilmiş stok kalemleri grid ekranında listelenir. Gelen kalemlerin hepsinin yerleştirileceği düşünüldüğünden, tüm kalemler seçili gelir. Eğer listelenen stok kalemlerinden yerleştirme yapılması istenmeyen kalem varsa, ilgili kalem üzerine fare ile çift tıklanır. |

**Yerleştirme**

![](../../../../_assets/40b1ae3be7b7d4a1cad4.png)

Seçilen stok kalemleri, yukarıda görüldüğü gibi yerleştirme ekranına gelir. Ekranda listelenen ürünlerden yerleştirilmesi istenenler, fare ile çift tıklanarak seçilir. Seçilen ürünün yerleştirileceği hücre kodunun ve net miktarın girilmesi gerekir. Yerleştirme Bilgileri bölümünde; parametrelerde “İrsaliyeler ile Kayıtlar Tutsun mu” parametresi işaretlenmiş ise, seçilen stokların belgedeki miktarı ile yerleştirilen miktarının eşit olması koşulu aranır. Aksi halde yerleştirme ekranından çıkılamaz.

![](../../../../_assets/6c014a88b44fadbd8604.png)

Eğer, Dinamik Depo Parametre Kayıtlarında, “Brüt/ Net Kg. Takibi Yapılacak Mı” parametresi işaretlenmiş ise, kayıt tamamlanmadan önce yukarıda görülen ekran açılır.

Yerleştirilecek/toplanacak tartılı mallar; içinde taşındıkları kutu, palet, el arabası vb. ile birlikte tartılıyor, fakat içindeki net miktar kadar mal yerleştiriliyor/toplanıyor ise, bu ekranda net miktar veya brüt miktar otomatik hesaplanır. Otomatik hesaplamanın yapılması için öncelikle; malların taşındığı kutu, palet, el arabası vb. eşyalar için birer stok kartı açılması gerekir. Bu stokların Grup Kodu sahasına "DARA" ifadesinin girilmesi gerekir. Her birinin birim ağırlık bilgisinin stok kartında tanımlanması gerekir. Ekranda Stok Kodu alanında, daranın stok kodu ve tartım miktarının içinde kaç adet bulunduğu mutlaka yazılmalıdır. Daranın miktarı kadar birim ağırlık değeri, brüt miktardan düşülerek, net miktar otomatik bulunur ve yerleştirme bu miktarlar için yapılır.

Hücre Yerleştirme bölümünden yapılan yerleştirme kayıtlarının silinmesine izin verilmez. Silme işleminin, İşlemler menüsünün altındaki Yerleştirme/Toplama İptali bölümü kullanılarak yapılması gerekir.

Hücre Yerleştirme ekranında farenin sağ tuşu ile ekrana gelen seçenekler ve içerdiği bilgiler şunlardır:

| Hücre Yerleştirme Ekranı Sağ Tuş Seçenekleri |  |
| --- | --- |
| Düzeltme Kaydı | İstenirse yerleştirme işlemi sırasında düzeltme kaydı yapılabilir. Düzeltme kaydı için farenin sağ tuşunda bulunan Düzeltme Kaydı seçeneği kullanılır. Girilen bir yerleştirme bilgisi yanlış ise ve düzeltilecek ise Düzeltme Kaydı seçeneği kullanılabilir. Düzeltme Kaydı seçeneği kullanıldığında, ekranda düzeltme miktar bilgisi ve düzeltmenin giriş mi yoksa çıkış mı olduğu sorgulanır. Düzeltme kaydı yeni bir yerleştirme hareketi gibi kaydedilir. Örneğin, yanlışlıkla yapılmış bir giriş hareketi, aynı miktarda çıkış hareketi ile düzeltilebilir. |
| Basım | Basım seçeneği ile, ilgili deponun fiş basımı gerçekleştirilir. |
| Seri Bilgisi İzleme | Ticari pakette, Genel Parametre Kayıtları ekranındaki “Seri Takibi Var mı” parametresini seçerek işlem yapan firmalarda kullanılan seçenektir. Yerleştirme ekranında Seri Bilgisi seçeneğine tıklandığında, seçilen stok kalemine ait seri numaraları bazında bakiye izlenir. |
| Gönder | Gönder seçeneği ile, grid alandaki yerleştirme kayıtları Excel'e ya da akıllı gride gönderilip grafik hazırlanabilir. |

Yerleştirme sekmesinin üst bölümünden seçilen kalemler bölümünde iken farenin sağ tuşu tıklandığında, aşağıdaki seçenekler ekrana gelir:

| Sağ Tuş Seçenekleri |  |
| --- | --- |
| Hücre Bakiye Listesi | Hücre Bakiye Listesi ile, hangi hücrede hangi stoklardan kaç tane olduğu bilgisi izlenir. |
| Seri Bilgisi İzleme | Ticari pakette, Genel Parametre Kayıtları ekranındaki “Seri Takibi Var mı” parametresini seçerek işlem yapan firmalarda kullanılan seçenektir. Yerleştirme ekranında Seri Bilgisi seçeneğine tıklandığında, seçilen stok kalemine ait seri numaraları bazında bakiye izlenir. |
| Gönder | Gönder seçeneği ile, grid alandaki yerleştirme kayıtları Excel'e ya da akıllı gride gönderilip grafik hazırlanabilir. |
