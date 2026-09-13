---
title: "İş Emri Girişi"
page_id: "50663777"
product: "netsis-3-enterprise"
depth: 4
is_section: true
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Üretim"
  - "Kayıt/Üretim"
  - "İş Emri Girişi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Üretim / Kayıt/Üretim / İş Emri Girişi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTg2NDc1ZWJhLWUzMWEtNDRkOC1hYmVmLWQ2YzU1NzdlZDgyMSZsaW5rPTJiMjFmNTY4LWJmMjItNGU3Mi04NWM1LTEzZjY5NWYwMjc0NSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=86475eba-e31a-44d8-abef-d6c5577ed821&link=2b21f568-bf22-4e72-85c5-13f695f02745&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "is-emri-girisi_50663782_50663777.html"
source_version: "2022-11-08T16:34:57.527+03:00"
source_bytes: 31079
fetched_at: "2026-09-13T04:18:56+00:00"
generator: "netsis-scraper 1.0.0"
---
# İş Emri Girişi

İş Emri Girişi, Üretim modülünde Kayıt/Üretim menüsünün altında yer alır. İş emri, ambardan üretim için malzeme çekmeye (İş emrine bağlı hammadde listesi) ve kararı verilen üretimin ne kadarının yapıldığını bilmeye yarar (İş emrinden gerçekleşen üretim). Planlamaya ışık tutar.

İş emri ile reçete saklama sisteminde yapılanlar şunlardır:

- Her iş emri ile mamulün anlık reçetesi saklanır.
- Reçete değişiklikleri sisteminin çalışmamasına sebep olur.
- Üretim sonu kaydında desteklenir.
- Ambar Giriş/Çıkış ve Depolar Arası Transfer işlemlerinde desteklenir (Reçete getirme fonksiyonu).

İş Emri Girişi ekranı; Sabit Bilgiler, Ek Bilgiler, İş Emrine Bağlı Reçete Kayıtları Toplam Hammadde Kullanımı sekmelerinden oluşur.

**Sabit Bilgiler**

İş Emri Giriş ekranı Sabit Bilgiler sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| İş Emri Girişi Ekranı |  |
| --- | --- |
| İş Emri No | İş emri numarasının kaydedildiği alandır. Program tarafından otomatik olarak sıra takip edilerek numara atanır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, iş emri numaralarına ulaşılır. |
| Tarih | İş emrinin açıldığı kayıt tarihinin girildiği alandır. |
| Stok Kodu | İş emri girişinin yapılacağı, üretilecek mamul ya da yarı mamulün stok kodunun girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile stok kodlarına ulaşılır. |
| Asorti Kodu | Asorti kodunun girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, tanımlanan özellik kodlarına ulaşılır. |
| Asorti Kodu Açıklaması | Asorti koduna ait açıklama bilgisinin otomatik olarak ekrana girildiği alandır. |
| Açıklama | İş emri için açıklama bilgisi girilen alandır. Sadece raporlama yapmaya yönelik kullanılır. |
| Ölçü Birimi | İş emri için ölçü birimi girilen alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile tanımlanan ölçü birimlerine ulaşılır. |
| Miktar | İş emri girişi yapılan mamulün, ilgili iş emriyle bağlantılı olarak üretileceği miktar bilgisinin girildiği alandır. |
| Sipariş No | Girilen iş emrinin belli bir sipariş için verildiği durumlarda, sipariş numarasının girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile sipariş numaralarına ulaşılır. |
| Öncelik | İş emrinde öncelik girilmesi, iş emrinin kullanıldığı her yerde (Depolar Arası Transfer, Üretim Sonu Kayıtları gibi) ilgili önceliğe sahip alternatif malzemelerin kullanılmasını sağlar. Verilen önceliğe sahip alternatif malzeme bulunamazsa, reçetedeki malzeme kullanılır. |
| Teslim Tarihi | Girilen mamul koduna göre üretilecek mamulün, tahmini üretim tamamlanma tarihinin girildiği alandır. |
| Revizyon No | İş emri belli bir revizyon numarası ile üretilecekse, ilgili revizyon numarasının girildiği alandır. Bu durumda, iş emri ile üretim gerçekleştirildiğinde, ilgili revizyon numarasıyla yapılan değişiklikteki reçete ile üretim gerçekleştirilir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, revizyon numaralarına ulaşılır. |
| Depo Kodu | Üretim safhaları ya da ambarlarını lokal depo olarak tanımlayan firmalar için, üretilecek mamuldeki bileşenlerin girişinin yapılacağı depo kodunun girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, depo kodlarına ulaşılır. |
| Çıkış Depo Kodu | Üretim safhaları ya da ambarlarını lokal depo olarak tanımlayan firmalar için, üretilecek mamuldeki bileşenlerin çıkışının yapılacağı depo kodunun girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, depo kodlarına ulaşılır. |
| Proje Kodu | Yardımcı Programlar → Kayıt → Şirket/Şube Parametreleri → “Proje Uygulaması Var” parametresinin işaretlenmesi ile aktif hale gelen alandır. İlgili üretim hareketi için mutlaka proje kodu girilmesi gerekir. Yapılan üretim, "İş Emri bağlantılı" ise bu kez iş emrinden girilen proje kodu bu alana otomatik olarak yansıtılır ve istendiği zaman üzerinde değişiklik yapılabilir. Girilen proje kodları, stok hareket kayıtlarına aktarılır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile proje kodları arasından seçim yapılır. |
| Referans İş Emri No | Bir mamule ait iş emri numarası ile yarı mamuller için verilen iş emirlerinin takibinin yapılması için kullanılan alandır. Bu durumda yarı mamuller için açılan iş emirlerinde, mamul için açılan iş emri numarasının girilmesi gerekir. > [!NOTE]<br>> Bu uygulama ile; Üretim Sonu Kaydı, Serbest Üretim Sonu Kaydı ve Ters Üretim Sonu Kaydı ekranlarındaki iş emri rehberinde, referans iş emri numaralarının da izlenmesi sağlanır. |
| Sipariş Kontrol | Sipariş satırları bazında iş emri oluşması ile ilgili alandır. İş emrinde bulunan mamulün sipariş kalemlerindeki satır numarası gösterilir. Böylece, aynı stokun bir siparişte birden fazla tekrarlanması halinde, kaçıncı satırdaki stok için iş emri oluşturulduğu takip edilir. |
| Kapalı | Kaydedilen iş emrinin hala işlemde olması ya da kapatılmış olması ile ilgili alandır. Bakiyesi kalan fakat üretilmeyecek olan iş emirleri için işaretlenmesi gerekir. Böylece, tamamı üretilmemiş olsa bile, kalan bakiye üretim olarak düşünülmez ve raporlarda dikkate alınmaz. |
| Reçete Saklansın | Üretim Parametreleri → “İş Emriyle Reçete Sakla” parametresi işaretlendiğinde aktif hale gelen alandır. İşaretlendiğinde, iş emrinde girilen malzemeye ait o anki reçete saklanarak, istediği zaman üzerinde değişiklik yapılabilir. Böylece, ilgili iş emri ile üretim yapıldığında, malzemenin o anki reçetesi ne olursa olsun, reçetenin saklandığı şekliyle üretim yapılır. |
| İlişkili İş Emri Kayıtları Güncellensin | Mamullere ait iş emirlerinde yapılan tarih değişikliğinin, "Referans İş Emri No" alanında mamulün iş emri numarası girilen yarı mamullerin iş emirlerinde de yapılmasını sağlayan seçenektir. |
| Rework (Tamir) İş Emri | Tamir amacıyla açılan iş emirleri için işaretlenmesi gereken seçenektir. Rework iş emirleri MRP sırasında dikkate alınmaz. Sadece, tamir süreçlerinin yönetilmesi için üretim sahasında kullanılır. |
| Sıralama Önceliği | İleri Üretim Planlama uygulamasında algoritma opsiyonlarında "İş Emri Önceliğinin" seçildiği durumlarda kullanılan alandır. İlgili iş emrinin, çizelgeleme sırasında dikkate alınacak öncelik bilgisi girilir. |
| Seri No/Seri No-2 | Seri uygulamasının aktif olduğu durumlarda iş emrine bağlı üretim sonu kaydı yapılırken otomatik olarak iş emrinden seri veya seri-2 bilgisinin ekrana getirilmesi için seri ve seri-2 bilgisi girilen alandır. |
| USK Durumu | İlgili iş emrinin üretim durumunu gösteren alandır. İş emrine bağlı üretim sonu kaydı veya üretim akış kaydı atıldıkça, üretilen miktara bağlı olarak bu alan otomatik olarak güncellenir. Alanın sağ tarafında yer alan aşağı ok butonu ile durum seçimi yapılır. İş emrinin tamamı üretilmiş ise "Üretimi Tamamlandı" değerini alır, iş emrinin belli bir kısmı üretilmiş ise "Üretimine Başlandı" değerini alır. "İptal Edildi" veya "Durduruldu" seçenekleri program tarafından otomatik olarak atanmaz. Bu seçenekleri kullanıcı isterse kendisi seçebilir. |
| Rezervasyon Durumu | İlgili iş emrinin üretim sırasında sarf edeceği bileşenlerin rezervasyon durumunu gösteren alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile durumlar arasından seçim yapılır. İş emrinin üretim sırasında gereksinim duyduğu malzemelerin rezervasyonu için "İş Emri Malzeme Rezervasyonu" ekranı kullanılabilir veya iş emrine bağlı depolar arası transfer fişiyle girilebilir. Rezerve edilen malzemelerin hangi depoya rezerve edildiğine ve depo tipine bağlı olarak "Rezervasyon Durumu" bilgisi otomatik olarak ayarlanır. **Örneğin;** iş emrinin gereksinim duyduğu malzemelerin hepsi "Mamul Ambarı" tipindeki bir depoya rezerve edilmişse "Rezervasyon Durumu" olarak "Mamul Ambarına Rezerve" değeri seçilir. İş emri basımı yapıldığında "Rezervasyon Durumu" otomatik olarak "Yayımlandı" durumuna geçer. |

**Ek Bilgiler**

İş emrine ilişkin ekstra bilgi girişinin yapılmasını sağlayan sekmedir. Üretim → Saha Tablo Eşleştirmeleri bölümünde tanımlanarak iş emrine eklenen sahalar bulunur.

Kullanıcı Tanımlı Sahalar bölümünde Saha Tablo Eşleştirmesi bölümünde "İş Emri" seçilerek tanımlanan sahalar listelenir.

**İş Emrine Bağlı Reçete Kayıtları**

Kayıt menüsünün altında bulunan bu işleme, iş emri ekranından kolayca erişim sağlamak için kullanılan sekmedir.

> [!NOTE]
> İş Emrine Bağlı Reçete Kayıtları bölümü ile ilgili ayrıntılı bilgi için bakınız; İş Emrine Bağlı Reçete Kayıtları

**Toplam Hammadde Kullanımı**

İlgili iş emrindeki mamulün üretim adedini de göz önünde bulundurarak, o üretim için hangi ham maddeden ne kadar tüketileceğini en alt seviyeye kadar gösteren sekmedir.
