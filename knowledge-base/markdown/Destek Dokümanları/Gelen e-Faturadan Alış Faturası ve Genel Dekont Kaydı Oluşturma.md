---
title: "Gelen e-Faturadan Alış Faturası ve Genel Dekont Kaydı Oluşturma"
page_id: "153159293"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Gelen e-Faturadan Alış Faturası ve Genel Dekont Kaydı Oluşturma"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Gelen e-Faturadan Alış Faturası ve Genel Dekont Kaydı Oluşturma"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTY4OTJkYTE2LTUyYjctNGFhNy04ZjA0LWI2YzI1N2RlODFmNCZsaW5rPWNhODY3ZTQzLWNlYTUtNDRjMi04MTIwLWQwODQzM2Y1MTZiNCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=6892da16-52b7-4aa7-8f04-b6c257de81f4&link=ca867e43-cea5-44c2-8120-d08433f516b4&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "gelen-e-faturadan-alis-faturasi-ve-genel-dekont-kaydi-olusturma_153159293_153159293.html"
source_version: "2024-12-09T08:04:48.047+03:00"
source_bytes: 4879482
fetched_at: "2026-09-13T04:22:35+00:00"
generator: "netsis-scraper 1.0.0"
---
# Gelen e-Faturadan Alış Faturası ve Genel Dekont Kaydı Oluşturma

#### Gelen e-Faturadan Alış Faturası Oluşturma

Netsis içerisinde gelen e-Faturadan Alış Faturası ve Genel Dekont Kaydı oluşturulabilmektedir. Gelen e-Faturadan alış faturası oluşturulabilmesi için aşağıdaki koşulların sağlanması gerekmektedir.

1. Gelen e-Fatura zarfının durum kodunun 1300 olması gerekmektedir.
2. Ticari senaryolu e-Faturalar için, uygulama yanıtının "kabul" olarak verilmiş olması gerekmektedir.
3. TBLEFATURA tablosundaki RESPONSECODE alanının 2 olması gerekmektedir.

(Temel senaryolu e-Faturalar için TBLEFATURA.RESPONSECODE alanı program tarafından otomatik 2 olarak oluşturulmaktadır. Ancak dışarıdan aktarılan e-Faturalar için bu alan otomatik 2 olarak güncellenmediğinden manuel olarak bu alanın da 2 olarak güncellenmesi gerekmektedir.)

Gelen e-Faturadan Alış Faturası oluşturulabilmesi 3 farklı yöntemle yapılabilmektedir.

1. Fatura Bazında Gelen e-Fatura ekranında ilgili e-Fatura kaydı üzerinde sağ tuş ile e-Faturadan

Alış Faturası Oluşturma seçeneği ile

1. e-Faturadan Alış Faturası Oluşturma menüsü ile
2. Alış Faturası ekranında sağ tuş menüsüne eklenen E-Belge Eşleştir seçeneği ile

#### Fatura Bazında Gelen e-Fatura ekranından sağ tuş e-Faturadan Alış Faturası Oluşturma seçeneği ile gelen e-Faturadan alış faturası oluşturma

Gelen e-Faturadan alış faturası oluşturulabilmesi için **Fatura Bazında Gelen e-Fatura** ekranında ilgili fatura üzerinde sağ tuş menüsüne **e-Faturadan Alış Faturası Oluşturma** seçeneği eklenmiştir.

![](../_assets/a988e8dc22bfb8e3b908.png)

Örneği aşağıdaki belgede sağ tuş **e-Faturadan Alış Faturası Oluşturma** seçeneği ile işlem yapıldığında alış faturası CS00…198802 olarak kaydedilmiştir.

![](../_assets/7582525ae8ee4d8b9761.png)

Gelen uyarı ekranında tamam seçeneği işaretlendiğinde, oluşan alış faturası ekrana gelecektir. Eğer gelen e-Faturanın Xml'indeki vergi numarası Cari Hesap Kayıtları ekranında vergi numaralarından bulunamazsa uyarı verilip cari kartın açılması beklenmektedir.

Benzer şekilde Xml de fatura kalemlerinin Netsiste bulunup belgeleye getirilmesi adımında xml dosyada SellerssItemIdentification, BuyersItemIdentification ve ManufacturersItemIdentification tagleri ile gelen bilgiler için sırasıyla stokkodu, barkod bilgisi, üretici kodu, cari stok kodu ve Müşteri Satıcı Stok Kayıtları ekranındaki alanlar kontrol edilir. Eğer stok kodu bulunamazsa "EFATURA_STOK" şeklinde açılmış olan sabit bir stok kodu için kalemler oluşmaktadır. İlgili kalemler üzerinde kullanıcı gerçek stok kodları ile düzenleme yapmalıdır. Toplamlar sekmesinde tamam seçeneği ile gelen e-Faturadan alış faturası oluşturma işlemi tamamlanır.

![](../_assets/bbcf89208f373e28984c.png)

![](../_assets/bf79dba5292840c4f96e.png)

![](../_assets/691165738f6175183ae0.png)

#### e-Faturadan Alış Faturası Oluşturma menüsü ile Gelen e-Faturadan Alış Faturası Oluşturma

**Gezgin\\Lojistik -** **Satış\\Fatura\\Kayıt\\e-Fatura** **İşlemleri** menüsü altında yer alan **e-Faturadan** **Alış** **Faturası** **Oluşturma** ekranında alış faturası oluşturulmak istenen e-belge seçilir.

**Alış Faturası Oluştur** seçeneği ile gelen ekrandaki belge çift tıklandığında açılan **Alış Faturası** ekranında Üst Bilgiler, Kalemler ve Toplamlar sekmesi kontrol edilerek Toplamlar sekmesinde tamam seçeneği ile gelen e-Faturadan alış faturası oluşturma işlemi tamamlanır.

![](../_assets/b9125ed0eaa53dd00d7b.png)![](../_assets/d6d4aa8fca270e73e9fb.png)![](../_assets/112331cd976c5b26fd30.png)

#### Alış Faturası ekranında sağ tuş menüsüne eklenen E-Belge Eşleştir seçeneği ile Gelen

**e-Faturanın** **Alış** **Faturası** **ile** **Eşleştirilmesi** Alış faturası manuel oluşturularak **Alış** **Faturası** ekranında sağ tuş menüsüne eklenen **"E-Belge** **Eşleştir"** seçeneği ile Gelen e-Fatura, alış faturası ile eşleştirilmektedir.

![](../_assets/3a7b96a2b83a397a74b0.png)![](../_assets/739aae080122e370ddbf.png)

3 yöntemin sonunda **Fatura** **Bazında** **Gelen** **e-Fatura** ekranında Netsis Fatura Numarası alanı dolmaktadır.

![](../_assets/64a82996c5cf3cbb4806.png)

**Fatura Bazında Gelen e-Fatura** ekranında ilgili fatura üzerinde sağ tuş **e-Faturadan Alış Faturası Oluşturma** ile oluşturulan alış faturası yine aynı ekran üzerinde sağ tuş **E-Belge** **Eşleştirme** **İptali** ile iptal edilmektedir.

![](../_assets/3ffd9aaccc0375364b95.png)

Benzer şekilde, Alış Faturası ekranının Üst Bilgiler sekmesinde sağ tuş menüsünde de "**e**-**Belge** **Eşleştirme** **İptali"** seçeneği bulunmaktadır.

![](../_assets/69c29c722b457fc444b1.png)

E-Belge Eşleştirme İptali ile belge iptal edildikten sonra oluşturulan alış faturası silinebilmektedir.

#### Gelen e-Faturadan Genel Dekont Oluşturma

Gelen e-Faturadan alış faturası oluşturulduğu gibi genel dekont kaydı da oluşturulabilmektedir.

**Fatura** **Bazında** **Gelen** **e-Fatura** ekranında sağ tuş menüsüne **Dekont** **Oluşturma** seçeneği eklenmiştir.

![](../_assets/2b4362c10c0a5090dafa.png)

Dekont oluşturma seçeneği ile açılan **e-Faturadan** **Genel** **Dekont** **Oluşturma** ekranında bilgiler girilerek kaydet seçeneği ile gelen e-Faturadan Dekont Oluşturma işlemi tamamlanır.

![](../_assets/218a7dad236bffcb8440.png)![](../_assets/54557eae4b64adfefd88.png)

Alış Faturası ekranında olduğu gibi **Genel** **Dekont** **Kaydı** ekranında da sağ tuş menüsünde **e-Fatura** **Eşleştirme** seçeneği ile girilen dekont kaydı gelen e-Fatura ile eşleştirebilmektedir.

![](../_assets/823d4d49a2ffe0900afb.png)
