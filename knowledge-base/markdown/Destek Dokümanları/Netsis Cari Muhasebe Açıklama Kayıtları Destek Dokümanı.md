---
title: "Netsis Cari Muhasebe Açıklama Kayıtları Destek Dokümanı"
page_id: "50680285"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis Cari Muhasebe Açıklama Kayıtları Destek Dokümanı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis Cari Muhasebe Açıklama Kayıtları Destek Dokümanı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTBhMjM1OWIzLWEwMjYtNGY1OS1hOGI2LWU2NDBjMzU1YTYwYSZsaW5rPTc2M2ExNWZhLWU0NjEtNDMwYi05ZDMyLTkzOWJlN2VhODc3ZSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=0a2359b3-a026-4f59-a8b6-e640c355a60a&link=763a15fa-e461-430b-9d32-939be7ea877e&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-cari-muhasebe-aciklama-kayitlari-destek-dokumani_66238075_50680285.html"
source_version: "2022-11-03T09:52:45.227+03:00"
source_bytes: 247705
fetched_at: "2026-09-13T04:26:19+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis Cari Muhasebe Açıklama Kayıtları Destek Dokümanı

Netsis Cari Muhasebe Açıklama Kayıtları ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Yardımcı programlar modülündeki Cari Muhasebe Açıklama kayıtları ekranı ile Temelset içinde yer alan modüllerden (fatura, banka, çek, senet vb.) girilen belgelerin, entegre oldukları modüllerdeki standart açıklamalarının özelleştirilebilmesi sağlanmaktadır.

Tanımlamalar VbScript kullanılarak, her şirket için ayrı ayrı yapılabilmektedir.

![](../_assets/2caff0dcf6ed3d8a14fa.png)

**Modül No:** Temelset'te belgenin kaydedildiği modüldür. Örn:Fatura.

**Program No:** Üst bölümde seçilen modül içinde bulunan programlardan, kaydın girileceği program numarasının seçileceği sahadır.Örn: Fatura, Satış Faturası.

**Kayıt Tipi:** Değiştirilmek istenen açıklamanın seçileceği bölümdür.

![](../_assets/a87c27fe0d93b6f906f2.png)

**Örn** **1:** Modül=Fatura , Program= Satış Faturası, Kayıt Tipi= Cari Genel Açıklama seçildiği durumda, Satış Faturası kesildiğinde Cari Hareket Kayıtlarında görülen açıklama bilgisi değişecektir.
**Örn** **2:** Modül=Banka , Program= Müşteri/Satıcı Havale/Eft Kayıtları, Kayıt Tipi= Entergasyon Banka Genel Açıklama seçildiği durumda, eft kaydı girildiğinde Entegrasyon Kayıtlarında banka muavin hesabının açıklama bilgisi değişecektir.

**Script Girişi**

"Script kodunu buradan girebilirsiniz" butonuna tıklandığında açılan ekrandan VbScript girişi yapılmaktadır. Netsis içindeki sahaların script içinde kullanılabilmesi için sağ klikte bulunan "Saha Rehberi" kullanılmalıdır.

![](../_assets/e39f0ed9836afe180f59.png)

Saha rehberi butonuna tıklandığında açıklaması değiştirilecek olan belgenin sahalarının bulunduğu pencere açılmakta ve script içinde kullanılmak istenen alan seçilebilmektedir.

![](../_assets/a7d08a77939024be870c.png)

Bu listeden herhangi bir alan seçildiğinde ,seçilen saha aşağıdaki gibi görülmektedir.

![](../_assets/0a1ddcebc2585dd3cd30.png)

Saha listesinde, belge başlık bilgisi ve kalem bilgilerinden oluşan bir belge ise (örn: Fatura, sipariş, teklif), sadece belgenin başlık bilgisinin bulunduğu alanlar listelenir. Kalemlerden getirilmek istenen bilgiler için SQL sorgusu hazırlanmalıdır.

Aşağıdaki örnekte SQL sorgusunda belgenin üst bilgilerde girilen açıklama1 bilgisinin gelmesi sağlanmıştır. Üst bilgilerden veri alınabileceği gibi kalemler için sorgu yazıalrak veri gelmesi sağlanabilir. Kalem bilgileri ile ilgili sorgulama sonucu dönecek olan satırın hangisi olduğuna dikkat edilmelidir. Kalemler ile ilgisi olmayan başka dosyalardan da SQL sorgusu yazarak bilgi getirmek mümkündür.

**Örnek:**

Satış faturası kesildiğinde entegrasyon modülüne giden "Entegrasyon Stok Genel Açıklama" sının "Belge Numarası + Açık1 " sahalarının birleşiminden oluşan açıklamanın yazması istenmektedir. Bu durumda aşağıdaki şekilde tanımlama yapılabilir.

![](../_assets/a1dc17bf11bbf5494c99.png)

![](../_assets/f49ed283c2c5bb6814dd.png)

*Dim* *cahar_aciklama*
*Set* *QRY* = *Netsiscore.Netlibdb.Getnewquery*
*QRY.RecSQL* *"(SELECT* *FATIRSNO,* *ACIK1* *FROM* *TBLFATUEK* *WITH(NOLOCK)* *WHERE* *FATIRSNO='"* &
*GetProgValue("FATIRS_NO")* & "' *AND* *CKOD='"* & *GetProgValue("CARI_KODU")* & "')"
*If* *QRY.FieldByName("ACIK1").asstring* \<\> "" *Then*
*cahar_aciklama* = *QRY.FieldByName("FATIRSNO").asstring* & "-" & *QRY.FieldByName("ACIK1").asstring* *RESULT* = *cahar_aciklama*
*Else*
*cahar_aciklama = QRY.FieldByName("FATIRSNO").asstring* *RESULT* = *cahar_aciklama*
*End* *If*
*QRY.close*
*Set* *QRY* = *Nothing*

Tanımlamalar bu şekilde yapıldığında satış faturası girildikten sonra entegrasyon kayıtlarında oluşan kaydın açıklaması bu tanıma uygun şekilde oluşacaktır.

![](../_assets/a701c43700dbfcbd3a12.png)
![](../_assets/8372e0c3d904d95f632c.png)
Entegrasyon kayıtlarında yevmiye açıklama kısmında görülen açıklama scriptte yazdığı gibi Belge Numarası – Açıklama1 olacak şekilde "*EFT000000000100-YENI* *FATURA* *ACIKLAMASI*" bilgilerinden oluşmuştur.
