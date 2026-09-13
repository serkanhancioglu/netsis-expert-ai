---
title: "Çek Tahsil Dekontu"
page_id: "22805822"
product: "netsis-3-enterprise"
depth: 6
is_section: true
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Dekont"
  - "Kayıt / Dekont"
  - "Tahsil/Teminat/Ciro Çekleri Ödeme Dekontu"
  - "Çek Tahsil Dekontu"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Dekont / Kayıt / Dekont / Tahsil/Teminat/Ciro Çekleri Ödeme Dekontu / Çek Tahsil Dekontu"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWZkYzRmZGZhLTkzNjUtNDE2ZS1hZDhhLTE1ZTY0MmFjNmMwMyZsaW5rPTdmYjkyMjdjLTMzNjUtNGYxMC05YWQxLTI5ZjA3ZWE0OGI2YyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=fdc4fdfa-9365-416e-ad8a-15e642ac6c03&link=7fb9227c-3365-4f10-9ad1-29f07ea48b6c&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "cek-tahsil-dekontu_22805826_22805822.html"
source_version: "2022-11-30T10:07:42.017+03:00"
source_bytes: 66249
fetched_at: "2026-09-13T04:09:03+00:00"
generator: "netsis-scraper 1.0.0"
---
# Çek Tahsil Dekontu

Çek Tahsil Dekontu, Finans Bölümü'nde, "Kayıt/Dekont" menüsünün altında yer alır. Çek Tahsil Dekontu, bankaya tahsile çıkan çekin bir adet olması halinde, ödeme kaydı oluşturulmak için kullanılan bölümdür.

![](../../../../../../_assets/0d4dcf84b629d4e9fbbd.png)

Çek Tahsil Dekontu alanları ve içerdiği bilgiler aşağıdaki şekildedir:

| Çek Tahsil Dekontu Ekranı |  |
| --- | --- |
| Çek No | Ödendi kaydının yapılacağı çeke ait numara girilen alandır. Rehber butonu ![](../../../../../../_assets/088477bb321d1b20c939.jpg) ile, kayıtlı çek numaralarına ulaşılır. |
| Seri Kodu | İlgili dekonta ait seri numarasının girildiği alandır. Boş bırakılmaz. Seri numaralarının mutlaka Dekont → İşlemler → [Seri Kodu Tanımlama](<../../../İşlemler - Dekont/Seri Kodu Tanımlama.md>) bölümünden daha önce kaydedilmesi gerekir. |
| Dekont No | Program tarafından otomatik olarak her bir dekont serisi 1 rakamından başlar. Kaydedilen her dekont için bir sayı arttırılarak devam eder. Farklı bir numaradan başlaması istendiğinde ise; Dekont → İşlemler → "[Dekont Numarası Düzenleme](<../../../İşlemler - Dekont/Dekont Numarası Düzenleme.md>)" bölümü kullanılarak serilere başlangıç numarası verilir. Rehber butonu ![](../../../../../../_assets/088477bb321d1b20c939.jpg) ile, kayıtlı dekont numaralarına ulaşılır. |
| Fiş Numarası | Çek tahsil dekontunun üzerindeki dekont numarasının girildiği alandır. |
| Kayıt Tarihi | Dekont kayıt tarihi olarak, günün tarihinin program tarafından otomatik olarak getirildiği alandır. TL tutarlı çek tahsil dekontlarında, klavyedeki \<tab\> tuşu ile ilerlendiğinde "Döviz Bilgileri" ekranı görüntülenir. |
| İşlem Tarihi | Çek tahsil dekont kaydının girildiği tarihtir. Yapılacak işlem sonucu oluşacak kayıtlar ,diğer modüllere (Banka-Entegrasyon-Senet) bu tarih ile kaydedilir. |
| Tahsil/Teminat Hesap Kodu | Seçilen çek numarasının hangi bankaya tahsile verildiği, "[Müşteri Çekleri Parametreleri](<../../../../Müşteri Çekleri/Kayıt - Müşteri Çekleri/Müşteri Çekleri Parametreleri.md>)" bölümünde işaretlenen seçeneklere göre ekrana gelir. (Cari Kod-Muhasebe Kodu veya Banka Hesap Kodu). Rehber butonu ![](../../../../../../_assets/088477bb321d1b20c939.jpg) ile hesap kodlarına ulaşılır. |
| Tutar | Girilen çek numarasına göre, tutarın program tarafından otomatik olarak aktarıldığı alandır. |
| Kur Farkı | Seçilen çekin dövizle kaydedilen bir çek olması halinde, programın tahsilde oluşacak kur farkını hesaplaması için döviz kurunu sorgulaması gerekir. Girilen kur, çekin kaydedildiği günün kurundan farklı ise, kur farkı hesaplanarak kur farkı alanına aktarılır. Şirket genelinde dövizli çalışılması fakat girilen çekin döviz bilgilerini içermemesi durumunda farklı döviz bilgileri sorgulanır. Bunlar; Döviz Tipi, Kur ve Döviz Tutarıdır. Bu bilgiler cari hareketlere ve entegrasyona aktarılır. |
| Tahsil Masrafı | Çek tahsilinde bankaya ödenecek tahsil masrafının (varsa) girildiği alandır. |
| Gider Hesap Kodu | Tahsil masrafında girilen tutarın işleneceği karşılık muhasebe kodunun girildiği alandır. Rehber butonu ![](../../../../../../_assets/088477bb321d1b20c939.jpg) ile hesap kodlarına ulaşılır. |
| Banka Borç Bedeli | Tahsil masrafları düşüldüğünde, bankanın ödemesi gereken (kalan) tutarın otomatik hesaplanarak aktarıldığı alandır. Bu tutar aynı zamanda virman hesabına işlenir. |
| Virman Hesap Kodu | Çek tutarının virman edileceği banka (bankalar cari hesaplarda tanımlamışsa; cari hesap kodu, muhasebede tanımlamışsa; muhasebe hesap kodu) kodunun girildiği alandır. Rehber butonu ![](../../../../../../_assets/088477bb321d1b20c939.jpg) ile hesap kodlarına ulaşılır. |
| Açıklama | İlgili yevmiye maddelerinde işlenmesi istenen açıklamanın girildiği alandır. |
| Borç Cari Kodu/Alacak Cari Kodu | Bazı firmalar çalışma prensipleri gereği, müşterilerden aldığı çekleri ilk kayıt esnasında farklı bir hesaba işler ve çek tahsil edildiğinde müşterilerinin asıl hareket kayıtlarına virman yapar. Bu işlemin "Çek Tahsil Dekont Kaydı" sırasında otomatik olarak yapılmasını sağlamak için, dekont ekranında Borç Cari Kodu ve Alacak Cari Kodu olmak üzere iki alan kullanılır. Çek tahsilatı sırasında, **Borç Cari Kodu** alanına otomatik olarak, çek alındığında kaydedilen cari kod gelir. Yapılması gereken; çek tahsilatının hangi cari koda **alacak** **hareketi** olarak kaydedilmesi isteniyorsa, ilgili cari kodun **Alacak Cari Kodu** alanına girilmesidir. Böylece; dekont işleminin tamamlanması ile **Borç Cari Kodu** alanına girilen cari koda **borç hareketi** kaydedilerek, çek alımında kaydedilen alacak hareketi kapatılır. **Alacak Cari Kodu** alanına girilen koda **alacak hareketi** kaydedilerek çekin asıl cari harekete yansıtılması sağlanır. Bu tür uygulamaları olmayan firmalar için bu alan kullanılmaz. |
| Plasiyer Kodu | Yardımcı Programlar → Kayıt → Şirket-Şube Parametreleri → "Plasiyer Uygulaması Var" parametresinin işaretlenmesi ile aktif hale gelen alandır. Dekont kaydı sırasında ilgili plasiyer kodunun girilmesi gerekir. Rehber butonu ![](../../../../../../_assets/088477bb321d1b20c939.jpg) ile, plasiyer kodlarına ulaşılır. Boş bırakılmaz. |
| Proje Kodu | Yardımcı Programlar → Kayıt → Şirket-Şube Parametreleri → "Proje Uygulaması Var" parametresinin işaretlenmesi ile aktif hale gelen alandır. Dekont kaydı sırasında ilgili plasiyer kodunun girilmesi gerekir. Rehber butonu ![](../../../../../../_assets/088477bb321d1b20c939.jpg) ile, proje kodlarına ulaşılır. Boş bırakılmaz. Girilen proje kodları, cari hareketlere ve entegrasyona aktarılır. |
| Referans Kodu | Muhasebe → Kayıt → Muhasebe Parametreleri → "Fişlerde Referans Kodu Sorulsun" parametresinin işaretlenmesi ile aktif hale gelen alandır. Rehber butonu ![](../../../../../../_assets/088477bb321d1b20c939.jpg) ile, referans kodlarına ulaşılır. Boş bırakılmaz. |
| Cari Rapor Kodu | Cari → Kayıt → Cari Parametreleri → "Hareketlerde Rapor Kodu Girilsin" parametresinin işaretlenmesi ile aktif hale gelen alandır. Hareketlere aktarılması ve raporlanması amacıyla 1 karakterden oluşan rapor kodu girişi yapılır. |
| Özel Basım | Dekont kaydının basımı için "Dizayn Modülü" ile hazırlanan özel bir basımın kullanılması istendiğinde işaretlenen seçenektir. Özel bir basım değil, standart bir basım yapılması istendiğinde bu seçenek işaretlenmemesi, sadece "Basım "alanındaki "Evet" seçeneğinin işaretlenmesi gerekir. |
| Basım | Dekont kaydının basımı için kullanılan seçenektir. İşlemler bittikten sonra Tamam ![](../../../../../../_assets/39d77b8716226638d9ce.jpg) butonuna basıldığında, "Müşteri Çekleri Modülünde" ilgili çekin durumu program tarafından **“Ödendi**” olarak değiştirilir. İlgili yevmiye maddeleri oluşturularak Entegre → Kayıt → Entegrasyon Kayıtları → Dekont sekmesinden izlenir. |

**Çek Tahsil Dekontu İptal İşlemi**

Çek tahsil dekont kaydı kullanılarak, tahsil işlemi yapılmış bir çek tahsilatının iptali, yine çek tahsil dekont kaydından yapılır. Bunun için daha önceden tahsil işlemi yapılmış çek numarasının, "Çek No" alanına girilmesi gerekir. Çek numarasının girilmesi ile birlikte program tarafından kontrol edilen çek, uygun koşullara sahip (tahsilatı yapılmış) ise “Bu kayıt ödenmiş olduğu için ters işlem yapılabilir. Devam etmek istiyor musunuz?” şeklinde bir uyarı ekrana gelir.

Bu aşamada yapılması gereken; ilk tahsilat işlemi sırasında “Virman Hesap Kodu” alanına girilen hesap kodunun aynısı yine “Virman Hesap Kodu” alanına girilir. Dekont kayıt işlemlerinin tamamlanması ile, cari Hareketlerde ve entegrasyon havuzunda ters kayıt oluşarak, çekin durumu tekrar “B” (beklemede) durumuna gelir.
