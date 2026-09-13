---
title: "1 Nisan Şematron Güncellemeleri"
page_id: ""
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "1 Nisan Şematron Güncellemeleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / 1 Nisan Şematron Güncellemeleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWE1OWM1ZTU5LWE5MGYtNGU5ZS1hNzQ5LTIzZWJiYzEyZWU5NSZsaW5rPTY0Y2I1ZTVmLWM0MjctNDdiMi05NGZlLTI1YjAzMzNkZDBlOCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=a59c5e59-a90f-4e9e-a749-23ebbc12ee95&link=64cb5e5f-c427-47b2-94fe-25b0333dd0e8&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "1-nisan-sematron.html"
source_version: ""
source_bytes: 10110
fetched_at: "2026-09-13T04:21:51+00:00"
generator: "netsis-scraper 1.0.0"
---
# 1 Nisan Şematron Güncellemeleri

16.03.2026 tarihinde yayınlanan "GİB Sicil ve Faaliyet Kodu Kontrolleri 1 Nisan 2026 İtibarıyla Şematron Uygulamaları" duyurusunda, sicil ve faaliyet kodu kayıtları üzerinden çeşitli kontrollerin yapılacağı ve belirtilen kontrollerin e-Fatura ve e-Arşiv belge türleri için zorunlu olacağı duyurulmuştur.

Bu kapsamda, 9.0.66.11 ve 9.0.70.3 LTS patchleri ile 04.05.2026 tarihinde yayınlanacak olan 9.0.71 sürümünde belge oluşturma ve gönderim süreçlerinin kesintisiz bir şekilde ilerleyebilmesi için aşağıdaki bilgilerin kontrol edilmesi gerekir. E-belge gönderiminde bu kurallara uyulmaması durumunda uyarı verilecektir.

**1. Satıcı Sicil Bilgileri**

Belge üzerinde yer alan gönderici unvan / ad-soyad ve vergi dairesi bilgilerinin, Dijital Vergi Dairesi’ ndeki güncel sicil bilgileri ile birebir aynı olması gerekmektedir.

Logo Netsis üzerinde Yardımcı Programlar/ Kayıt/ **Şirket Şube Parametre Tanımları** ekranında **Unvan ve Vergi Dairesi** alanlarının kontrol edilmesi gerekmektedir. Bu bilgilerde kısaltma, noktalama veya yazım farklılıkları bulunuyor ise, Dijital Vergi Dairesi’ ndeki güncel sicil bilgileri ile aynı olacak şekilde güncellenmelidir.

Unvan alanına müdahale edilmek istenmediğinde, e-Belge basımlarında kullanılan dizaynlarda, farklı alanlara girilen Dijital Vergi Dairesi’ ndeki güncel sicil bilgisi **Supplier-PartyName** tagi ile eşleştirme yapılarak getirilebilir.

**2. Alıcı Sicil Bilgileri**

Belge üzerinde yer alan alıcıya ait unvan/ad-soyad ve vergi dairesi bilgilerinin, alıcının Dijital Vergi Dairesi’ ndeki güncel sicil bilgileri ile birebir aynı olması gerekmektedir. Alıcının unvan veya vergi dairesi alanları için hatalı bir bilgi gönderildiğinde gelecek yanıt içerisinde olması beklenen değer de gösterilmektedir.

Logo Netsis üzerinde **Cari Hesap Kayıtları** ekranında **Cari İsim ve Vergi Dairesi** alanlarının kontrol edilmesi gerekmektedir. Bu bilgilerde kısaltma, noktalama veya yazım farklılıkları bulunuyor ise, alıcıların Dijital Vergi Dairesi’ndeki güncel sicil bilgileri ile aynı olacak şekilde güncellenmelidir.

Cari Parametrelerinde Cari İsim Sorgulama Kaynağı **TÜRMOB** seçilmesi durumunda, Cari Hesap Kayıtları ekranında cariye ait unvan, adres, il, ilçe, vergi dairesi, vb bilgilerin TÜRMOB servisi aracılığı ile güncel sicil bilgilerin getirilmesi sağlanmaktadır.

Farklı sebeplerden dolayı carilerin birden fazla Cari Hesap Kartlarında takip edilmesi durumunda (Cari İsim alanında unvan bilgisine ek olarak farklı açıklamaların girilmesi durumunda), Cari İsim alanına müdahale edilmek istenmediğinde, e-Belge basımlarında kullanılan dizaynlarda, farklı alanlara girilen Dijital Vergi Dairesi’ ndeki güncel sicil bilgisi **Customer-PartyName** tagi ile eşleştirme yapılarak getirilebilir.

**3. Faaliyet Kodu (NACE) – KDV Oranı Uyumu**

Belgede kullanılan KDV oranlarının, firmanın faaliyet kodları (NACE) ile uyumlu olması gerekmektedir. Bu kapsamda, Dijital Vergi Dairesi üzerinden faaliyet kodları kontrol edilmelidir. Gerektiği durumda güncelleme/ekleme başvurusu yapılması gerekebilir.

Logo Netsis üzerinde oluşturulan satış faturası (e-Fatura veya e-Arşiv serili) sonrasında Toplu e-Fatura/ e-Arşiv Oluşturma ekranlarında ilgili belge için taslak oluşturulur ve gönderilir. Taslak oluşturma ve gönderim sırasında Faaliyet Kodu (NACE)- KDV Oran Uyum kontrolü yapılmamaktadır. Gönderilen e-Belgenin durum bilgisi alınma aşamasında, belgede kullanılan KDV oranları ile firmanın faaliyet kodu (NACE) ile uyumsuz olması durumunda “**Şirketinizin faaliyet alanı kapsamında XXX, YYY, .. KDV oranları kullanılamaz**” uyarısı alınacaktır. Hata alınan belge için zarf sil işlemi yapılır, belgenin kdv oranı mükellefin NACE koduna uygun şekilde güncellenir ve belge başarılı bir şekilde tekrardan taslak oluşturulup gönderilir.

Faaliyet Kodu (NACE)-KDV oran kontrolünün uygulanmayacağı belge tipleri: **IADE, TEVKIFATIADE, YTBIADE, YTBTEVKIFATIADE**

**4. “555- KDV Oran Kontrolüne Tabi Olmayan Satışlar” Kodunun Kullanımı**

Faaliyet koduna (NACE) karşılık gelen KDV oranı ile fatura düzenlenmeyen satış işlemlerinde (yansıtma faturaları, mükellefin aktifine kayıtlı demirbaş/ taşıt satışları, vb) “**555 - KDV Oran Kontrolüne Tabi Olmayan Satışlar**” muafiyet kodu kullanılmalıdır.

Bu muafiyet kodu bulunan belgelerde Faaliyet- KDV oran uyum kontrolleri yapılmayacaktır. e-Belgenin Not bölümünde KDV oran kontrolü yapılmayan durumların detay açıklamaları yer almalıdır.

Program içinde satış faturası girişi sonrasında Toplamlar sekmesinde sağ tık menüsünde yer alan "**E-Devlet Özel Matrah / İstisna Tipleri \> KDV Oran Kontrolüne Tabi Olmayan Satış / Açıklama Kaydı**" seçeneği seçilir. Bu seçeneğe tıklandığında Açıklama isminde bir popup ekran açılır. Açılan bu ekranda neden kdv oran kontrolüne tabi olmayan satış yapıldığına dair açıklama bilgisi girilir. Bu alan boş geçilemez. Girilen açıklama bilgisi e-Faturanın notlar bölümünde otomatikman yer alacaktır. Açıklama bilgisi girildikten sonra istisna kodu alanı altında yer alan bilgi, **E-Devlet Özel /İstisna Kodu: 555** yazar.

Toplamlar sekmesinde sağ tık menüsünde yer alan "**E-Devlet Özel Matrah/ İstisna Tipleri\> Özel Matrah/ İstisna Tip İptali**" seçeneği seçildiğinde 555 kod ataması iptal edilir ve girilen açıklama silinir. Girilen açıklama değiştirilmek istendiğinde ise, **E-Devlet Özel Matrah/ İstisna Tipleri\> KDV Oran Kontrolüne Tabi Olmayan Satış/ Açıklama Kaydı** seçeneğine tekrardan tıklanması yeterlidir.

555- KDV Oran Kontrolüne Tabi Olmayan Satışlar muafiyet kodu sadece TEMELFATURA, TICARIFATURA veya EARSIVFATURA senaryoları için geçerlidir. IHRACAT, YATIRIMTESVIK, İDİS, vb diğer senaryolarda, IHRACKAYITLI, ISTISNA vb. fatura tipli belgelerde ve senaryosu EARSIVFATURA fatura tipi YTB ile başlayan belgelerde kullanılamaz. Bu belge türlerinde Toplamlar sekmesinde 555 muafiyet kodu atanabilmekte ancak taslak oluşturma işlemi esnasında kullanıcıya uyarı mesajı verilerek taslak oluşturulmamaktadır.

Vergi istisna/muafiyet kodu 555 kullanıldığında, KDV satırlarında veya toplam KDV değerinde % KDV oranı veya KDV tutarı sıfır (0) olamaz. Bu şekilde oluşmuş belgelerde Toplamlar sekmesinde sağ tık menüsünde **"E-Devlet Özel Matrah / İstisna Tipleri\> KDV Oran Kontrolüne Tabi Olmayan Satış / Açıklama Kaydı"** seçeneği gelmemektedir.

**4. 1 UBL Alanı**

Belgeye 555 kodu atandığı durumda oluşan xml içinde yer alan Invoice ve InvoiceLine altına

cac:TaxTotal/TaxSubtotal/TaxCategory/cbc:TaxExemptionReasonCode ve

cac:TaxTotal/TaxSubtotal/TaxCategory/TaxExemptionReason elemanları eklenir.

XML içinde bu bilgiler yer aldığı durumda Nace-KDV uyumluluğu kontrolü yapılmayacaktır. Bu elemanlar yer almadığında NACE Kodu-KDV oran uyumluluğu kontrol edilecektir.

**Toplam Vergi Alanı Örnek UBL**

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/145e275c-3e02-4461-98a4-d3fdc9a9ce87/1nisan.png)
