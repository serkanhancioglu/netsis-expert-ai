---
title: "Masraf Yönetimi"
page_id: "115608342"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Masraf Yönetimi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Masraf Yönetimi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWY1M2FhNzJlLWNhNjktNDBkNS1hNDNjLWFlMTFhZWY1MTkwMSZsaW5rPTAwNDQzYWE5LWQ4MzMtNDU4NC04ZTY4LTRmN2JiODIzMDI5YSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=f53aa72e-ca69-40d5-a43c-ae11aef51901&link=00443aa9-d833-4584-8e68-4f7bb823029a&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "masraf-yonetimi_115608342_115608342.html"
source_version: "2023-07-21T09:36:46.373+03:00"
source_bytes: 1751134
fetched_at: "2026-09-13T04:23:19+00:00"
generator: "netsis-scraper 1.0.0"
---
# Masraf Yönetimi

Masraf yönetimi hakkında ayrıntılı bilgiye bu dokümandan ulaşılır.

Çalışanlarımız tarafından yapılan masrafların kayıt altına alınması, çalışanlara geri ödenmesi ve raporlanması desteklenmektedir. Genel / Yardımcı Programlar modülü altında masraf yönetimi grubu bulunmaktadır. Bu grup altındaki ekranları kullanarak çalışanlarımıza yaptığımız ödemeleri takip edebiliriz.

**Masraf Tip Tanımları**

Bu ekran aracılığı ile masraflar tip bazında detaylandırılır. **Masraf** **Tip Kodu,** **Tip** **Açıklaması** ve bu tip kullanıldığında çalışacak muhasebe **Hesap** **Kodu** tanımlanır.

İlgili masraftan bir alış faturası oluşturulacaksa **Fatura** **Hizmet** **Stoğu** doldurulur.

![](../_assets/6fcd74b55806a013a330.png)

Seçilen **Fatura Hizmet Stoğu** Binek Oto Kira ya da Binek Oto Masraf için açılmış bir stoksa, fatura kaydı oluşturulurken seçilen mevzuat tipine uygun şekilde kayıtlar oluşur.

**Masraf Neden Tanımları**

Girilecek masrafın tipi dışında nedeni de takip edilir. Bu ekran aracılığı ile belirlemiş olduğumuz **Neden** **Kodu** ve **Açıklama** bilgisi girilir.

![](../_assets/93f42a1f40bae5830c9d.png)

**Detaylı Masraf Muhasebe Tanımları**

Masrafların neden kodu ve tip kodu bazında detaylandırılması için kullanılan ekrandır. Bu ekran aracılığı ile aynı neden kodunda ama tipi farklı masrafların farklı hesapları çalıştırması sağlanır. İlgili alanlarda -1 (Hepsi) yöntemi kullanılarak da tanımlama yapılır.

![](../_assets/1c65ad5f206950c7bb24.png)

**Masraf Yönetim Parametreleri**

![](../_assets/b2f303e65b6754f3decd.png)

**Muhasebe** **Hesapları** **Detaylı** **Takip** **Edilsin:** Bu parametre işaretli olması durumunda oluşacak olan muhasebe fişlerinde Masraf Tip Tanımlarındaki muhasebe kodu yerine Detaylı Masraf Muhasebe Tanımlarında yer alan, masraf merkezi tip kodu ve neden kodu bazında tanımlanmış olan muhasebe hesap kodları kullanımı sağlanır.

**Ödeme Ekranından Açılan Masraf Formları Değiştirilebilsin:** Bu parametrenin işaretli olması durumunda Masraf Ödeme Kayıtları ekranından ilgili masraf formuna ulaşılabilir ve belirlenen alanlarda düzenleme gerçekleştirilebilir. Parametre işaretlenmezse ödeme ekranında açılan masraf formlarında herhangi bir değişiklik yapılamaz.

**Ödeme Ekranında Yapılan Değişiklikler İş Akışa Dahil Edilsin:** Ödeme ekranında yapılan değişiklikler iş akışa dahil edilebilmesi sağlanır.

**Masraf Formu**

Masraf formlarımızı aşağıdaki ekran üzerinden takip ederiz.

![](../_assets/de3ad025d150011a8a6b.png)

Ekrandaki alanların açıklaması aşağıdaki gibidir:

**Masraf** **No:** Program tarafından artan sırada atanan masraf numarası alanıdır.

**Personel Kodu:** Masraf formunun ait olduğu personel seçilir. Personeller Stok / Kayıt / Personel Tanımlama ekranından tanımlanır.

**Tarih:** Masraf Formunun oluşturulan tarihinin girildiği alandır.

**Masraf** **Merkezi:** Formun masraf merkezi seçilir.

**Döviz** **Tipi:** Döviz tipinin girildiği alandır.

**Masraf** **Neden Kodu:** Masrafa sebep olan neden kodu girilir.

**Açıklama:** Varsa açıklama bilgisi girilir.

**Masraf** **Tarihi:** Masrafın gerçekleştiği fiili tarih girilir.

**Açıklama:** Varsa açıklama bilgisi girilir.

**Tutar:** Masrafın tutarının KDV Dahil olarak girildiği alandır.

**KDV** **Oran:** KDV Oranının girildiği alandır.

**KDV** **Tutar:** KDV oranına göre hesaplanmış KDV tutarıdır.

**Masraf Tip** **Kodu**: Daha önce yukarıda anlatılan masraf tip kodunun seçildiği alandır.

**Müşteriye Faturalanacak:** Raporlama amaçlı kullanılır. Hangi müşteriye faturalanacak ise cari kodu seçilmelidir.

**Faturası Var Mı? :** Yapılan masraf için alınan fatura var ise işaretlenmelidir. Örneğin: Masrafımız karşılığında bir fiş yada fatura aldığımızda işaretlememiz gereklidir.

**Fiş** / **Fatura** **No:** Yapılan masrafın fiş veya fatura numarası girilmelidir.

**Ödeme Yöntemi:** Yapılan masrafın ödeme bilgisinin seçileceği alandır. Nakit, Firma Kredi Kartı , Şahsi Kredi Kartı , Harcırah seçenekleri bulunmaktadır. Nakit veya Şahsi Kredi Kartı seçeneği seçildiğinde masraf formunda seçilen personele geri ödeme yapılmaktadır. Diğer ödeme yöntemleri raporlama amaçlı kullanılır.

**Belge** **Ekle:** Masraf formunun geneline resim ve belge eklemek için kullanılır.

**Satıra** **Belge** **Ekle:** Seçilen satırlara resim ve belge eklemek için kullanılır.

**Formu** **Sil:** İlgili masraf formunun silinmesini sağlar.

**Masraf Ödeme Kayıtları**

![](../_assets/3bad236d6eeb6f2c904e.png)

Masraf formu oluşturulduktan sonra masraf ödeme kayıtları ekranında görüntülenmektedir. Yeni girilen kaydın durum bilgisi Muhasebeleştirilecek olarak görünür.

![](../_assets/eddcb289be002f0e3e7e.png) **Muhasebeleştir:** İlgili kayıt seçimi yapıldıktan sonra Muhasebeleştir butonuna basılır. İlgili Personele alacak kaydı atacak şekilde dekont kaydı oluşur.
Masraf formunda Faturası Var Mı işaretli ise ve alış faturası oluşturulacak ise Masraf Muhasebeleştirme ekranında **Alış Faturası Oluşturulsun** seçeneği işaretlenir. İşaretlenmemesi durumunda oluşacak olan dekont masraflara ait ilgili Muhasebe Kodu ve KDV tutarı borç olacak şekilde kayıt oluşturur.
![](../_assets/038bb126660651002904.png)

![](../_assets/f8627fc3d03cdf57f7c2.png) **Ödeme Yap:** İlgili masraf için ödeme kaydı atılacak dekont ve banka bilgisi seçilerek personele ödeme gerçekleştirilir. İlgili masraf formu "ÖDENDİ" durumuna dönmüş olur.
![](../_assets/ec6e95311adccfc012c0.png)

![](../_assets/d03b2ba78d14b72657d0.png) **Muhasebeleştirme** **İptali:** Muhasebeleştirme işlemi iptal edilebilir. Böylece masraf
formu tekrar "MUHASEBELEŞTİRİLECEK" durumuna geri döner.
![](../_assets/6ca1481f8ac6443e9c47.png) **Ödeme İptali:** Ödeme işlemi iptal edilebilir. Böylece masraf formu tekrar "ÖDEME BEKLİYOR" durumuna geri döner.

**Masraf Kayıtlarının Raporlanması**

Masraf kayıtlarının raporlanabilmesi için; Yardımcı Programlar / Raporlar menüsü altında Masraf Kayıtları Raporlarından alınmaktadır. Genel kısıtlardan Tarih Aralığı verilerek masraf formunun durumuna göre Mesaj Durumu seçilerek rapor alınır.
![](../_assets/4052ae6f8bdd372b4769.png)![](../_assets/b310692f1f9f37c73d11.png)
