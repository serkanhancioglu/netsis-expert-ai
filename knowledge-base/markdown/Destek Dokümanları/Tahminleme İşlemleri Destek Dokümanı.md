---
title: "Tahminleme İşlemleri Destek Dokümanı"
page_id: "90669114"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Tahminleme İşlemleri Destek Dokümanı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Tahminleme İşlemleri Destek Dokümanı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTYxN2JkNzFjLTY4YzItNDBkOS04NmJhLWI2ZDc4Nzg0YTZmMCZsaW5rPWFlNTE4ZWFjLWNiNTEtNGNiNy1iNzA1LTJhZTI0ODU5YmVjOCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=617bd71c-68c2-40d9-86ba-b6d78784a6f0&link=ae518eac-cb51-4cb7-b705-2ae24859bec8&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "tahminleme-islemleri-destek-dokumani_90670223_90669114.html"
source_version: "2022-11-02T14:16:45.263+03:00"
source_bytes: 1372331
fetched_at: "2026-09-13T04:23:57+00:00"
generator: "netsis-scraper 1.0.0"
---
# Tahminleme İşlemleri Destek Dokümanı

Tahminleme İşlemleri ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

**Tahminleme İşlemleri**

Tahminleme işlemleri, belirli istatistiksel yöntemlerin geçmiş satış verilerine uygulanması ile gelecek dönemlere ait satış tahminlerinin oluşturulmasını sağlar. Oluşturulan satış tahminleri sonrasında Ana Üretim Planlama işlemlerinde kullanılabilir.

**Tahminleme Parametreleri**

Tahminleme parametreleri, MRP parametreleri / Tahminleme sekmesinde yer alır. Bu parametrelerin bazıları istenirse tahminleme işlemi sırasında da değiştirilebileceğinden bu bölümde öndeğer olarak bırakılabilir.

![](../_assets/e8d91c21a4652aba68fc.png)

**Tahmin** **Değeri** **Periyot** **Tipi:** Tahminleme işleminin hangi periyot cinsiyle yapılacağını belirleyen parametredir. Gün, Hafta, Ay, Çeyrek, Yıl bazında tahminler yapılabilir. Örneğin, aylık tahminleme seçeneği işaretlendiğinde, aylık kümülatif satış miktarları dikkate alınarak, aylık satış tahminleri oluşturulacaktır. Aynı şekilde çeyrek seçeneği işaretlendiğinde, yılın 3'er aylık 4 çeyreği için kümülatif satış miktarları dikkate alınacak, geleceğe yönelik olarak yine çeyrekler bazında satış tahminleri oluşturulacaktır.

**Gruplama** **Seçeneği:** Tahminleme işlemleri yapılırken kullanılacak gruplama seçeneğini belirleyen parametredir. Tahminleme, stok kodu bazında yapılabileceği gibi Grup Kodu, Ürün Grubu, Kod-1… Kod-5 alanları bazında gruplanarak da yapılabilir.

**Tahmin** **Çarpan** **Sahası:** Bulunan tahminleme sonuçlarının belli bir oranda artırılarak kaydedilmesi isteniyorsa bu parametredeki alanlardan biri seçilebilir. Bu parametrede stok kartının ilgili alanı seçildikten sonra, çarpan değeri verilecek stok kartlarında ilgili alanlar doldurulabilir. Parametrenin alabileceği değerler: Hiçbiri veya stok kartındaki kullanıcı tanımlı sayısal sahalardır.

**Hareketli** **Ortalama** **Periyod** **Uzunluğu:** Tahminleme yöntemlerinden biri olan hareketli ortalama yöntemindeki ortalama hesabı için ne kadarlık geçmiş verinin dikkate alınacağını periyod cinsinden belirlendiği parametredir.

**Sezon** **Periyod** **Uzunluğu:** Tahminleme yöntemlerinden biri olan sezona dayalı yöntem için sezon uzunluğunun periyod cinsinden belirlendiği parametredir.

**Aykırı Değerler Ayıklansın:** Tahminleme yöntemleri uygulanırken standart sapmanın üzerinde ve altında bulunan değerlerin dikkate alınmadan işlem yapılması için işaretlenmelidir.

**Faturalaştırılmamış İrsaliyeler Dahil Edilsin:** Geçmiş dönemlere ait satış verilerinde faturalaştırılmamış irsaliyelerin dahil edilmesi istendiğinde işaretlenmesi gereken parametredir.

**İadeler** **Dahil** **Edilsin:** İlgili dönemde iadelerin satış verilerine dahil edilmesi istendiğinde işaretlenmelidir.

Tahminleme işlemlerine MRP modülünde kayıt menüsü altından ulaşılabilir. Bu ekran dört ayrı sekmeden oluşmaktadır. Tahminleme işlemlerinin yapılması için sırasıyla; Tahmin Kayıtları, Satış Verisi Oluşturma, Tahminleme Çalıştırma ve Tahminleme Sonuçları sekmelerinden sırasıyla işlemler yapılmalıdır.

**Tahmin Kayıtları**

İstenen parametreler ve belirli bir yöntem ile hesaplanarak oluşturulmuş satış tahminleri kümesi, bir numara verilerek, ileride erişilebilmek üzere saklanabilir. Bu sekmenin gridinde saklanmış tahmin kayıtları izlenebilir, istenirse yeni bir tahminleme kaydı oluşturulabilir, mevcut tahminlemelerin aktif/pasif durumları değiştirilebilir.

Yine bu sekmede, aktif tahmin kaydı içerisinde yapılacak tahminleme işlemi için parametreler belirlenebilir. MRP parametrelerinde belirlenen tahminleme parametreleri varsayılan olarak getirilir, kullanıcı isterse farklı tahminleme işlemlerinde bu parametreleri farklı şekilde belirleyebilir.

Başlangıç zamanı ve bitiş zamanı alanlarına oluşturulacak satış tahmin dönemi başlangıç ve bitiş tarihleri girilmelidir. Ölçü birimi alanında tahmin miktarlarının oluşturulması istenen ölçü birimi girilmelidir.

Satış Verisi: tahmin verileri oluşturulurken geçmiş dönemlere ait hangi verilerin baz alınacağının belirlendiği alandır. Geçmiş dönem satış verileri müşteri siparişlerinden, satış faturalarından, üretim sonu kayıtlarından oluşturabilir. Ayrıca, stok kodu, yapılandırma kodu, periyot, miktar bilgilerini içerecek şekilde oluşturulan Excel dosyalarının geçmiş dönem verisi olarak sisteme aktarımı sağlanabilir.

Tahmin kayıtlarının yönetimi için ekranda üç adet buton bulunmaktadır:

- **Yeni** **Tahmin** **Kaydı:** Yeni bir tahminleme kaydı için kullanılacak butondur.
- **Tahmin** **Kaydını** **Sil:** Seçili olan tahmin kaydını silmek için kullanılacak butondur.
- **Aktif-Pasif:** Seçili olan tahminleme kaydını aktif ya da pasif hale getirmek için kullanılacak butondur.

Not: Ana üretim planlama sırasında sadece aktif tahmin kayıtları kullanılabilir.

**Satış Verisi Oluşturma**

![](../_assets/e60322b6c2b7b83180a6.png)

Bu sekmede geçmişte gerçekleşen satışların yıl ve periyod bazında analizi sağlanmaktadır. Ekranın sol bölümünde şirket listesi bulunmaktadır, geçmiş satış verisinin alınacağı şirketler bu listeden seçilmelidir. Şirket seçimin ardından **"Satış Verisi Oluştur"** butonuna tıklayarak geçmiş satış verilerinin, belirtilen gruplama, periyod ve ölçü birimi bazında analizi oluşturulabilir. Oluşan satış analizleri ekranın sağ bölümündeki listede izlenebilir.

**Tahminleme Çalıştırma**

![](../_assets/7b8b958216bcc14fe845.png)

Bu sekmeye geçildiğinde ürün/ürün grubu listesi sol bölümde izlenebilir. "Tahminleme Çalıştırma" butonuna tıklayarak bütün ürünler/ürün grupları için tahminleme çalıştırılabilir.

Bu aşamada birçok istatistiksel yöntem için tahminleme çalıştırılmış olur. Sistem, en iyi sonucu veren yöntemi, kod bazında seçerek grafik üzerine yansıtır. İstenirse sistem tarafından belirlenen yöntem yerine kod bazında farklı bir yöntem seçilerek grafik üzerinde izlenebilir ve tahmin verileri seçilen yönteme göre kaydedilebilir.

Grafikte kırmızı olan çizgi geçmiş dönemlere ait gerçek satış verilerini göstermektedir. Diğer renkteki çizgiler ise seçilen yöntemin hem geçmiş dönemlere hem de gelecek dönemlere uygulanmış halini göstermektedir. Grafikte farklı renkte olan bu çizgiler kıyaslanarak, ilgili yöntemin gerçek satış verilerinden ne kadarlık bir sapma ile tahminde bulunduğu gözlemlenebilir.

Tahminleme sonuçlarını kaydetmek için ekranın sağ alt köşesinde bulunan "Kaydet" butonuna tıklanmalıdır.

**Tahminleme** **Sonuçları**

Kaydedilmiş olan tahminleme sonuçları bu sekme üzerinden detaylı şekilde izlenebilir. Güncel Satış Verilerini Göster butonu ile seçilen kod bazında güncel döneme ait gerçekleşen satışların grafik üzerinde satış tahminleri ile karşılaştırılması sağlanabilir.

![](../_assets/794beb6f5c4b0af07f7a.png)
