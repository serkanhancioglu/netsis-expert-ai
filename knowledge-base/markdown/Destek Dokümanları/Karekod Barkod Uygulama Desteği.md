---
title: "Karekod Barkod Uygulama Desteği"
page_id: "111249063"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Karekod Barkod Uygulama Desteği"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Karekod Barkod Uygulama Desteği"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTIwMDA5ZjM1LWU5YmItNGZkMy05NGY2LWQ5NzM0MmJjMzUxYyZsaW5rPTBhYmYxNjljLWY2NTAtNDc1Mi1iZjYyLWFkNzRiZTAyZjYyNSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=20009f35-e9bb-4fd3-94f6-d97342bc351c&link=0abf169c-f650-4752-bf62-ad74be02f625&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "karekod-barkod-uygulama-destegi_111249128_111249063.html"
source_version: "2023-05-22T09:57:50.740+03:00"
source_bytes: 5399745
fetched_at: "2026-09-13T04:23:28+00:00"
generator: "netsis-scraper 1.0.0"
---
# Karekod Barkod Uygulama Desteği

Karekod barkod uygulama desteği hakkında ayrıntılı bilgiye bu dokümandan ulaşılır.

2 Şubat 2008 tarihli ve 26775 sayılı Resmî Gazete' de yayımlanan "BEŞERİ TIBBI ÜRÜNLER AMBALAJ VE ETİKETLEME YÖNETMELİĞİ DEĞİŞİKLİK YAPILMASINA DAİR YÖNETMELİK" in Geçici 2'nci maddesine göre 16.05.2009 tarihinden itibaren ilaç ambalajlarında karekod bulundurma mecburiyeti olacaktır.

İlaç takip sistemi (İTS) gereği ilaç ambalajlarında halen kullanılmakta olan barkodların yanı sıra, yine üretici firma tarafından ürün kodu, seri numarası, her seri için yeniden başlayan sıra numarası, üretim tarihi ve son kullanma tarihi bilgilerini içeren bir Kare kod basılacaktır. İlaç takip sisteminde ilaçların eczanelerde satışı yine karekod (Datamatrix) barkod ile yapılacaktır.

**Karekod Nedir ?**

Karekod en basit anlamıyla orijinal adı "Datamatrix" olan iki boyutlu barkodlara verilen Türkçe isimdir. Karekod (Datamatrix) tipi barkodlar, klasik tek boyutlu (çizgilerden oluşan) barkodlardan farklı olarak beyaz ve siyah kare veya dikdörtgenlerden oluşan matris yapıdaki bir barkod türüdür.

![](../_assets/17b6570a1de48febaa92.png)

**Karekod Tipi Barkodların Avantajı Nedir?**

Karekod tipi barkodların avantajı, klasik tek boyutlu barkodlara nazaran daha çok veriyi içerebilmesidir. Karekod barkod, 2.335 karakter içerebilir.

**Karekod Barkod İzleme**

**ALT+CTRL+K** tuş kombinasyonu ile karekod barkod ekran açılmaktadır. Açılan ekranda, karekod barkod okuyucu ile okunan barkod bilgisi, karekod barkod içerisindeki bilgilere (GTIN, Sıra No, Son. Kul. Tar ve Parti No) ayrıştırılabilir. Kullanıcıların herhangi bir modülde iken bu programı açarak, okuttukları karekod barkodun içeriğini hızlıca izleyebilmelerini sağlamak amaçlanmıştır. Ayrıca bu seçenek ile programda bilgi amaçlı barkodun içeriği izlenebildiği gibi, karekod barkodlar bu ekrandan okutulduktan sonra, barkod içindeki istenen bilgi kopyalanarak istenilen alana yazdırılabilir.

Karekod barkod okuma ekranı açılması için "CTRL+ALT+K" tuşuna basılır.

Karekod barkod okutulduğu zaman aşağıdaki gibi karekod barkodu verisi ekrana gelecektir.

![](../_assets/4b1fdc756a89ac9b9e64.png)

Karekod un ayrıştırma işlemi örnek koda göre aşağıdaki şekilde yapılırÖrnek kare barkod= **01**08699546020478**21**425366555404**17**120731**10**trt005h

GTINSıra NumarasıSon Kullanma TarihiParti Numarası

**01** 08699546020478 **21** 425366555404 **17** 120731 **10** trt005h

![](../_assets/195022aa273b69795b79.png)

Ekran üzerinden" barkod ayrıştırıcı tasarım ortamını aç " butonu yer almaktadır. Bu şekilde açılan karekod barkod ekranının iki temel işlevi vardır.

- KareKod Barkod okuyucu ekranından açık olan programdaki hangi alanlara bilgilerin döndürüleceğinin (script ekranı yardımıyla) tanımlamaların yapılması.
- KareKod Barkodtan istenen alana değerin getirilebilmesi.

**KareKod Barkod Tanımlamaları**

Alt + Ctrl + K tuş kombinasyonu ile açılan karekod barkod ekranından programın genelinde açık olan ekrandaki herhangi bir alana değer döndürülebilmesi için öncelikle script yardımıyla tanımlamalarının yapılması gerekmektedir. "Barkod ayrıştırıcı tasarım ortamına geçiş" butonu yardımıyla kodlama ekranı açılmalı ve karekod barkodun her bir parçasının kullanımını belirlemek için uygun kod yazılmalıdır.

Örnek Kod,

DATAMATRIX.SetValueToControl "Kod",

DATAMATRIX.DMGTIN DATAMATRIX.DoTab

![](../_assets/bd8bb4933e3cbe6dc25f.png) DATAMATRIX.FinalizeScriKarekod barkod kısayol tuşu ile karekod barkod ekranı hangi alanda açıldıysa, script kod o alan için geçerli olacaktır. Açılan script ekranın alt kısmında bilgilendirme amaçlı yazılan scriptin hangi alan için geçerli olacağı belirtilmektedir.

Karekod Barkod için script giriş ekranı yardımıyla; tuşa basma mesajları gönderme (enter, tab, esc, vb.), barkod içerisindeki bilgilere ulaşma, form üzerindeki herhangi bir alana, grid üzerindeki herhangi bir hücreye veri yazma işlemleri yapılabilir. Script giriş ekranında "yükle" tuşu kullanılarak, daha önce yazılan scriptlerin yüklenmesi de mümkündür.

![](../_assets/9477db27d347b261d231.png)

DATAMATRIX nesnesinin özellikleri ve yöntemleri ile ilgili özellik ve yöntemlerinin listesi kodlama ortamında "nesne tarayıcı"dan görülebilir.

![](../_assets/0d0bc133cb0d544b41d7.png)

**KareKod Barkod Değer Döndürme İşlemi**

Kayıt girişleri sırasında okutulan karekod barkodların program tarafından gerektiği şekilde anlaşılabilmesi için, barkodun okutulacağı alan (ya da işlemin başlamasının istendiği alan) içerisindeyken Alt + Ctrl + K tuş kombinasyonu ile karekod ekranı açılmalıdır. Karekod barkod okuyucu ekranının barkod alanı içerisindeyken karekod barkod okutulmalıdır. Barkod okutulduktan sonra, ilgili alan için daha önceden yazılan script çalışır ve barkod bilgisi kullanılarak scriptte belirtilen adımlar gerçekleştirilir.

Kod örnekleri aşağıdaki gibidir,

**Alış İrsaliyesi Kalem Bilgilerinden Stok** **Girişi**

DATAMATRIX.SetValueToControl "Kod",

DATAMATRIX.DMGTIN DATAMATRIX.DoTab

DATAMATRIX.FinalizeScript

![](../_assets/a025bacca6fde4f04e1d.png)

![](../_assets/a10a5b66cc1bddf315d5.png)

GTIN alanı barkodda tanımlı olduğundan otomatik stok eşleşmesi yapıldı ve kalem girişi ekranına getirdi.

![](../_assets/b49ba83f333a146aa296.png)

**Alış İrsaliyesi-Seri Takip Ekranı** **Örneği**

DATAMATRIX.DoFocusGrid DATAMATRIX.DoEnter DATAMATRIX.DoLeft

DATAMATRIX.SendKeys DATAMATRIX.DMSerialNo DATAMATRIX.DoEnter

DATAMATRIX.SendKeys DATAMATRIX.DMExpDate DATAMATRIX.DoEnter

DATAMATRIX.SendKeys "1" DATAMATRIX.DoEnter

DATAMATRIX.SendKeys DATAMATRIX.DMLotNo DATAMATRIX.DoEnter

DATAMATRIX.DoRight DATAMATRIX.DoEnter

![](../_assets/5033c735f0cd5659754e.png)

![](../_assets/52fbafe87e0feb785fc5.png)

![](../_assets/4041fd49f45ccabf3918.png)

1. **Alış İrsaliyesi Seri Rehber Kare Kod** **Örneği**

'Kare barkod işlemleri için "DataMatrix" nesnesini kullanabilirsiniz.

DATAMATRIX.DoFocusGrid DATAMATRIX.DoEnter DATAMATRIX.DoLeft

set rs = NETSISCORE.NETLibDB.GetNewQuery

query = "select SERI_NO,STOK_KODU from TBLSERITRA where SERI_NO ='"& DATAMATRIX.DMSerialNo &"' and STOK_KODU =(select STOK_KODU from TBLSTSABIT where BARKOD1 ='"&datamatrix.DMGTIN&"') "

rs.recsql(query)

if rs.fieldbyname("SERI_NO").asstring = "" then

DATAMATRIX.SendKeys DATAMATRIX.DMSerialNo DATAMATRIX.DoEnter

DATAMATRIX.SendKeys DATAMATRIX.DMExpDate DATAMATRIX.DoEnter

DATAMATRIX.SendKeys "1" DATAMATRIX.DoEnter

DATAMATRIX.SendKeys DATAMATRIX.DMLotNo DATAMATRIX.DoEnter

DATAMATRIX.DoRight DATAMATRIX.DoEnter

else

netsiscore.NetLibWin32.ShowNetsisMesaj "KAREKOD SİSTEMDE KAYITLI!",2

end if

set rs = nothing

![](../_assets/773f705738853d49a749.png)

![](../_assets/2446925aa034a058f0d6.png)

![](../_assets/97283049ce64a86125c0.png)

**Alış Faturası Kalem Bilgilerinden Stok** **Girişi**

DATAMATRIX.SetValueToControl "Kod", DATAMATRIX.DMGTIN DATAMATRIX.DoTab

DATAMATRIX.FinalizeScript

![](../_assets/88bf938ea89dc661be92.png)

![](../_assets/e22a520dd63b80a4cd0c.png)

![](../_assets/3d46ed74d3a0abe06181.png)

**Alış Faturası Seri Takip Sayfası** **Örneği**

DATAMATRIX.DoFocusGrid DATAMATRIX.DoEnter DATAMATRIX.DoLeft

DATAMATRIX.SendKeys DATAMATRIX.DMSerialNo DATAMATRIX.DoEnter

DATAMATRIX.SendKeys DATAMATRIX.DMExpDate DATAMATRIX.DoEnter

DATAMATRIX.SendKeys "1" DATAMATRIX.DoEnter

DATAMATRIX.SendKeys DATAMATRIX.DMLotNo DATAMATRIX.DoEnter

DATAMATRIX.DoRight DATAMATRIX.DoEnter

![](../_assets/87d0a457060788953110.png)

![](../_assets/efd44ab005e60d819757.png)

![](../_assets/2448c4786447136a997d.png)

**Stok-İşlemler-Sayım Girişi** **Örneği**

DATAMATRIX.SetValueToControl "STOK_KODU", DATAMATRIX.DMGTIN DATAMATRIX.DoTab

DATAMATRIX.FinalizeScript

![](../_assets/172f648955b03f6dfc33.png)

![](../_assets/ef83eb4a8e3dad4579ff.png)

![](../_assets/551a50e9fc430cfb6d43.png)

**Stok Kartı Kayıtları-Barkod1 Girişi** **Örneği**

DATAMATRIX.SetValueToControl "BARKOD1",

DATAMATRIX.DMGTIN DATAMATRIX.DoTab

DATAMATRIX.FinalizeScript

![](../_assets/500cda4976c31fb85150.png)

![](../_assets/c9b4af360ce508f727e1.png)

![](../_assets/36b89938829989fef271.png)

**Stok Kartı Kayıtları-Kullanıcı Tanımlı Sahalar** **Örneği**

DATAMATRIX.SetValueToControl "kull1s", DATAMATRIX.DMGTIN DATAMATRIX.DoTab

DATAMATRIX.FinalizeScript

![](../_assets/e3ecfbae93f1d1f71a90.png)

![](../_assets/fcaa61a9e41843ba8919.png)

![](../_assets/5e129999e4dc46ec6d3c.png)
