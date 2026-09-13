---
title: "Koşul Sabit Kayıtları"
page_id: "22803683"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Cari"
  - "Kayıt / Cari"
  - "Koşul Kayıtları"
  - "Koşul Sabit Kayıtları"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Cari / Kayıt / Cari / Koşul Kayıtları / Koşul Sabit Kayıtları"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTZkYTI0MmYzLTczMDAtNDQ3Ny04Mzk1LTJjMTNjOWVmYzg5NyZsaW5rPTgyMGI4MDdmLTNiNjEtNGUxOC04NGZmLTJiZGQ4NDYyMDE3ZSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=6da242f3-7300-4477-8395-2c13c9efc897&link=820b807f-3b61-4e18-84ff-2bdd8462017e&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "kosul-sabit-kayitlari_28154720_22803683.html"
source_version: "2022-10-27T10:29:07.823+03:00"
source_bytes: 26779
fetched_at: "2026-09-13T04:07:40+00:00"
generator: "netsis-scraper 1.0.0"
---
# Koşul Sabit Kayıtları

Koşul Sabit Kayıtları, Finans Bölümü'nde, "Kayıt/Cari " menüsünün altında yer alır. Koşul kayıtlarının ilk aşaması "Koşul Sabit Kayıtları" bölümüdür. Koşul Sabit Kayıtları bölümünde, tanımlanan koşula ait baz alınacak parametreler tanımlanır. Tanımlanan parametreler doğrultusunda, ilgili koşula ait hesaplamalar yapılır. Her farklı uygulama için başka bir koşul sabit tanımlanır. Koşul sabit kayıtları; Koşul Kartı ve Koşul Kartı-2 olarak iki sekmeden oluşur.

**Koşul Kartı**

Koşul Sabit Kayıtları ekranı Koşul Kartı sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Koşul Sabit Kayıtları Ekranı |  |
| --- | --- |
| Koşul Kodu | Tanımlanacak koşul için girilen koddur. Koşul kodu, "Cari Hesap Kayıtları" bölümündeki "Koşul Kodu" alanında kullanılır. Böylece, ilgili cari kodla ilgili fatura işlemi yapıldığında koşul kodunda tanımlı parametreler baz alınır. |
| Koşul Açıklama | Girilen koşul koduna ait açıklamanın kaydedildiği alandır. **Örneğin:** Bayi Satış, Ege Bölgesi Müşteriler, Akdeniz Bölgesi Müşteriler gibi. |
| Koşul Tipi | Koşul Politika Tanımlamaları için kullanılan alandır. Bu alanın kullanımı hakkında detaylı bilgi için; Cari → Kayıt → Koşul Kayıtları → Koşul Tip Kayıtları. |
| Kayıt Tarihi | Koşul kodu kaydının yapıldığı tarihtir. Bu tarih, sistem tarihi olarak program tarafından otomatik şekilde ekrana getirilir. Kullanıcılar tarafından müdahale edilemez. |
| Koşul Rapor Kodu (Stok Grup Kod/Stok Kod1/Stok Kod2/Stok Kod3/Stok Kod4/Stok Kod5/Stok Fiyat Kod) | Tanımlanan koşulun hangi stoklar için geçerli olacağının seçildiği alandır. **Örneğin:** Bu koşul belli bir grup koduna sahip stoklar için uygulanacaksa, stok grup kodu seçilir. Bu bölümde girilecek seçeneğe göre, "Detay Koşul Kayıtları" bölümünde grup kodu, kod–1,2,3,4,5 veya stok fiyat kodu sorgulanır. "Koşul Rapor Kodu" alanı sadece, "Detay Koşul Kayıtları" bölümünde kullanılır. |
| Çoklu Seçim | "Detay Koşul Kayıtları", "Koşul Sabit Kayıtları" bölümünde belirlenen Koşul Rapor Koduna göre yapılır. **Örneğin:** "Detay Koşul Kayıtları" stokların sahip olduğu grup koduna göre yapılacaksa, ilgili koşul kodu için "Koşul Sabit Kayıtlar" bölümünde "Koşul Rapor Kodu" olarak "Stok Grup Kodu" seçilir. Böylece, koşulun sadece belirtilen grup koduna sahip stoklar için geçerli olacağı belirlenir. Ancak bazı durumlarda, koşulun geçerli olacağı stokların tek bir alana göre (örneğin grup kodu) belirlenmesi mümkün değildir. Bu yüzden," Detay Koşul Kayıtları" bölümünün geçerli olacağı stokların, birden fazla koşul rapor kodu ya da stok kartında bulunan diğer alanlara göre belirlenmesi için "Çoklu Seçim" seçeneği işaretlenir. Bu seçenek işaretlenerek, tanımlanan koşul kodları için "Detay Koşul" tanımlanırken, Cari → Kayıt → Koşul Kayıtları → Detay Koşul Kayıtları → Geçerli Stoklar sekmesinde, koşulun hangi stoklar için geçerli olduğunun belirlenmesi gerekir. |
| Faturada Sadece Koşul Detaydaki Stoklar Girilsin | "Koşul Detay Kayıtları" bölümünde belirlenen stok kodları dışındaki kodların, faturada kullanılmaması için işaretlenmesi gereken seçenektir. Bu seçenek işaretlendiğinde, "Koşul Rapor Kodu" alanında belirlenen stoklar faturada kullanılamaz. Dolayısıyla, ilgili koşulların geçerli olacağı stok kodlarının, "Detay Koşul Kayıtları" bölümünden tek tek girilmesi gerekir. Bu durumda, Fatura Modülünde, Detay Koşul Kayıtlarında belirtilmemiş bir stok kodu ile işlem yapılmak istendiğinde program uyarı vererek işlemi gerçekleştirmez. |
| Faturada İlave Koşullar Girişindeki Üste Yaz Koşulları Kullanılsın | "Ek Koşul Kayıtları" bölümünde yer alan "İlave Şekli" alanında belirlenecek "Sıfır değerler dahil üstüne yaz" ve "Sıfır değerleri değiştirmeden üstüne yaz" koşullarından işaretli olanının kullanılmasını sağlamak için kullanılan seçenektir. Bu seçenek işaretlenmediğinde, ek koşul tanımlaması yapılmış olsa bile üstüne yazma ile ilgili olan seçenekler kullanılamaz. |
| Faturada İlave Koşullar Girişindeki Toplam Koşulları Kullanılsın | "Ek Koşul Kayıtları" bölümünde yer alan "İlave Şekli" alanında belirlenecek, "Normal Toplam Al" koşulunun kullanılması için işaretlenmesi gereken seçenektir. Bu parametre işaretlenmediğinde ek koşul kayıtlarında, toplam koşul işaretlenmiş olsa bile kullanılamaz. |
| Cari Hesap Vadelere Bölünerek Atılsın | İlgili koşul kodu ile işlem gören cari hesaplara ait fatura toplamlarının, cari hesaplarına aktarılırken vadelere bölünerek aktarılması için işaretlenmesi gereken seçenektir. Bu seçenek işaretlenmediğinde, faturadaki vadeler dikkate alınmadan, fatura toplamları cari hareket kayıtlarına tek bir satır olarak aktarılır. |
| Cari Hesaba KDV Ayrı Kayıt Olarak Atılsın | İlgili koşul kodunu taşıyan cari kartlara kesilen faturalarda, KDV hariç tutarın ayrı, KDV tutarının ayrı satırlar halinde cari hareketlere aktarılması istendiğinde işaretlenmesi gereken seçenektir. Bu seçenek işaretlenmediğinde, fatura toplamı cari hareketlere tek bir satır olarak aktarılır. |
| Siparişteki Döviz Fiyatları Faturada Türk Lirasına Çevrilsin | Dövizli olarak girilen sipariş kayıtlarının, siparişin faturalandığı tarihteki kurla çarpılarak, TL'ye çevrilmesi istendiğinde işaretlenmesi gereken seçenektir. Bu seçeneğin işaretlenmesiyle eski tarihteki kurla girilmiş siparişlerin, teslimatın yapıldığı tarihteki kurla güncellenmesi sağlanır. |
| Siparişteki Fiyatları Yeni Geçerlilik Tarihine Göre Güncellensin Mi | Sipariş girişi yapıldıktan sonra koşulla ilgili herhangi bir değişiklik yapıldıysa bu siparişlerin teslimatları yapılırken, siparişlerin koşuldaki son duruma göre düzenlenmesi istendiğinde işaretlenmesi gereken seçenektir. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır. Yapılan kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.

**Koşul Kartı-2**

Koşul Sabit Kayıtları ekranı Koşul Kartı-2 sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Koşul Sabit Kayıtları Ekranı |  |
| --- | --- |
| Vade Bazında Liste Fiyatı Uygulaması | Belirlenecek vade bazında farklı fiyat listelerinin kullanılması istendiğinde işaretlenmesi gereken seçenektir. Vadelerde kullanılacak liste fiyatları "Genel Koşul Kayıtları" bölümünden tanımlanır. Bu seçenek işaretlendiğinde, aşağıdaki dört seçenek kullanılamaz. Bu seçenekle, stok kartlarında tanımlı olan dört satış fiyatı veya kullanılıyorsa stok liste fiyatları koşul uygulamasında kullanılabilir. |
| Vade İskontosu veya Faiz Uygulaması | Vadelere göre farklı iskontoların olması veya geciken ödemelerde faiz uygulaması yapılması istendiğinde işaretlenmesi gereken seçenektir. "Vade Bazında Liste Fiyatı Uygulaması" işaretlenmişse bu seçenek pasif hale gelir. Bu seçenek işaretlendiğinde, fatura modülünde ilgili koşul koduna sahip cari koda ait işlem yapılırsa, vadesinden önce yapılacak ödemeler için vade iskontosu yapılır, geç ödemeler için ise faiz uygulanır. |
| Peşin İskonto Fiyattan Düşülsün | "Vade İskontosu veya Faiz Uygulaması" seçeneği işaretlendiğinde aktif olan seçenektir. Peşin alışverişlerde uygulanacak iskonto tutarının fiyattan düşülmesi istendiğinde işaretlenmesi gereken seçenektir. Bu seçenek işaretlenmediğinde, fiyat belirlendiği gibi gelir ve yapılacak peşinat iskontosu faturalardaki satır veya genel iskontolarda gösterilir. |
| Peşin İskonto İçin Genel İskonto (0...3) | "Peşin İskonto Fiyattan Düşülsün" seçeneği işaretlendiğinde aktif olan seçenektir. Yapılacak peşinat iskontosunun fatura altı iskontosu olan genel iskontolardan hangisine yazılması isteniyorsa ilgili iskonto girilir. **Örneğin:** Peşinat iskontosunun genel iskonto–1 alanına yazılması isteniyorsa bu alana "1" değerinin girilmesi gerekir. |
| Peşin İskonto İçin Satır İskonto (0...6) | "Peşin İskonto Fiyattan Düşülsün" seçeneği işaretlendiğinde aktif olan seçenektir. Yapılacak peşinat iskontosunun satır iskontolarından hangisine yazılması isteniyorsa ilgili satır iskontosu girilir. 0 (sıfır) girilmesi peşinat iskontosunun satır iskontolarına yazılmayacağı anlamına gelir. |
| İrsaliye Faturalandırmada Koşullar Güncellensin | İrsaliyedeki koşulla ilgili herhangi bir değişiklik yapıldıysa, koşulun son durumuna göre fatura oluşturulması istendiğinde işaretlenmesi gereken seçenektir. |
| Koşul Tablosundaki Fiyatlar Netleştirilsin | Herhangi bir sipariş girilirken koşul tablosundaki tüm iskontoların düşülerek, hesaplanan net tutarın fiyat hanesine getirilmesi istendiğinde işaretlenmesi gereken seçenektir. Bu durumda iskontolar, iskonto alanlarında görünmez. |
| Koşul Tablosuna girilen Değerler Fiyat Kabul Edilsin | "Detay Koşul Kayıtları" bölümünde girilen tutar iskonto değerlerinin, fiyat olarak kabul edilmesi ve faturaya bu fiyatların getirilmesi istendiğinde işaretlenmesi gereken seçenektir. |
| Koşul Ciro Primi İçin Kullanılsın | Ciro primi uygulamasının desteklenmesi istendiğinde işaretlenmesi gereken seçenektir. Ciro Primi Uygulaması ile ilgili detay bilgi için; Cari → Ekler → Ek–4 (Ciro Primi Uygulaması). |
| Fatura Satırında Maks. Mal Fazlası İsk. Oran(%) | "Ciro Primi Uygulaması" ile ilgili olarak bu alana yazılan oran, faturada girilen miktarın maksimum ne kadarının mal fazlası olarak işleneceğini belirler. Ciro Primi Uygulaması ile ilgili detay bilgi için; Cari → Ekler → Ek–4 (Ciro Primi Uygulaması). |
| İşletmelerde Ortak | Tanımlanan "Koşul Sabit Kayıtlarının" işletmelerde geçerli olması istendiğinde kullanılan alandır. Tüm işletmelerde geçerli olması isteniyorsa, -1 değerinin girilmesi gerekir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, işletme kodları arasından seçim yapılır. |
| Şubelerde Ortak | Tanımlanan "Koşul Sabit Kayıtlarının" şubelerde geçerli olması istendiğinde kullanılan alandır. Tüm şubelerde geçerli olması isteniyorsa, -1 değerinin girilmesi gerekir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, şube kodları arasından seçim yapılır. |
| Hariç Tutulacak Şube Tanımlamaları | Tanımlaması yapılan "Koşul Sabit Kayıtlarının" hangi şubelerde hariç tutulacağının belirtildiği alandır. |
