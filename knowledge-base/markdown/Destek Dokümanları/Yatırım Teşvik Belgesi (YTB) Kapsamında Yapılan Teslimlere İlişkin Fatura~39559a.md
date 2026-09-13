---
title: "Yatırım Teşvik Belgesi (YTB) Kapsamında Yapılan Teslimlere İlişkin Fatura Düzenlemeleri"
page_id: ""
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Yatırım Teşvik Belgesi (YTB) Kapsamında Yapılan Teslimlere İlişkin Fatura Düzenlemeleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Yatırım Teşvik Belgesi (YTB) Kapsamında Yapılan Teslimlere İlişkin Fatura Düzenlemeleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTQ3ZmZmODg1LTM4MzktNGUyZS04M2ZhLTA1ZWNmNGZlNDI4MyZsaW5rPTYzNzZmYjgwLTBmYjgtNDI3MC05MzFkLWQ1YWNmMGIxN2JmZCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=47fff885-3839-4e2e-83fa-05ecf4fe4283&link=6376fb80-0fb8-4270-931d-d5acf0b17bfd&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "yatirim-tesvik-belgesi-ytb-kapsaminda-yapilan-teslimlere-iliskin-fatura-duzenlemeleri.html"
source_version: ""
source_bytes: 30323
fetched_at: "2026-09-13T04:21:56+00:00"
generator: "netsis-scraper 1.0.0"
---
# Yatırım Teşvik Belgesi (YTB) Kapsamında Yapılan Teslimlere İlişkin Fatura Düzenlemeleri

Gelir İdaresi Başkanlığı tarafından 21.11.2025 ve 09.12.2025 tarihlerinde ebelge.gib.gov.tr adresinde e-Fatura ve e-Arşiv Fatura uygulamasına dâhil olan mükellefler tarafından Yatırım Teşvik Belgesi (YTB) kapsamında düzenlenecek Faturalarda kullanılması gereken alanların belirlendiği **Yatırım Teşvik Kapsamında Yapılan Teslimlere İlişkin Fatura Teknik Kılavuzu** yayımlanmıştır. Güncel GİB kılavuzuna [buradan](https://ebelge.gib.gov.tr/dosyalar/kilavuzlar/Yatirim_Tesvik_Kapsaminda_Yapilan_Teslimlere_Iliskin_Fatura_Teknik_Kilavuzu_V1.1.pdf)ulaşabilirsiniz.

**9062.15 (LTS sürümü), 9066.5 (LTS sürümü) ve 9068.2 sürümleriyle birlikte,** Yatırım Teşvik Belgesi (YTB) kapsamında yapılan teslimlere ilişkin fatura düzenlemeleri desteklenmiştir.

**Fatura Senaryosu**

Mükellefin dahil olduğu uygulamaya (e-Fatura veya e-Arşiv) göre kullanılacak senaryo ve fatura tipleri aşağıdaki gibidir.

| e-Fatura | e-Arşiv |
| --- | --- |
| **Senaryo**: YATIRIMTESVIK <u>Örnek UBL Alanı:</u><br>\<cbc:ProfileID\>YATIRIMTESVIK\</cbc:ProfileID\> | **Senaryo**: EARSIVFATURA <u>Örnek UBL Alanı:</u><br>\<cbc:ProfileID\>EARSIVFATURA\</cbc:ProfileID\> |
| ```text<br>Fatura Tipleri: SATIS<br>ISTISNA<br>IADE<br>``` ```text<br>TEVKIFAT<br>``` ```text<br>TEVKIFATIADE<br>``` <u>Örnek UBL Alanı:</u><br>\<cbc:InvoiceTypeCode\>SATIS\</cbc: InvoiceTypeCode\><br>\<cbc:InvoiceTypeCode\>IADE\</cbc: InvoiceTypeCode\><br>\<cbc:InvoiceTypeCode\>ISTISNA\</cbc: InvoiceTypeCode\> \<cbc:InvoiceTypeCode\>TEVKIFAT\</cbc: InvoiceTypeCode\> \<cbc:InvoiceTypeCode\>TEVKIFATIADE\</cbc:InvoiceTypeCode\> | ```text<br>Fatura Tipleri: YTBSATIS<br>YTBISTISNA<br>YTBIADE<br>``` ```text<br>YTBTEVKIFAT<br>``` ```text<br>YTBTEVKIFATIADE<br>``` <u>Örnek UBL Alanı:</u><br>\<cbc:InvoiceTypeCode\>YTBSATIS\</cbc: InvoiceTypeCode\><br>\<cbc:InvoiceTypeCode\>YTBIADE\</cbc: InvoiceTypeCode\><br>\<cbc:InvoiceTypeCode\>YTBISTISNA\</cbc: InvoiceTypeCode\> \<cbc:InvoiceTypeCode\>YTBTEVKIFAT\</cbc: InvoiceTypeCode\>\<cbc:InvoiceTypeCode\>YTBTEVKIFATIADE\</cbc:InvoiceTypeCode\> |

Bu kapsamda Satış ve Alış Parametreleri ekranlarına, Genel 4 sekmesine “**Yatırım Teşvik Uygulaması**” seçeneği eklenmiştir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/687e5dfb-f7a2-4dde-9c37-740e255dccaf/yatırım teşvik 1.png)

Satış Parametreleri Genel 4 sekmesine eklenen “**Yatırım Teşvik Uygulaması**” seçeneği altına, <u>9.0.69 setiyle birlikte</u> “**Makine ID**” ve “**Makine Sıra No**” alanları eklenmiştir. Yardımcı Programlar\\Kayıt\\Şirket-Şube Parametre tanımları ekranında “**Seri Uygulamas**ı” seçeneği işaretli ise, bu alanlar aktif olarak gelmektedir. Bu seçenek işaretli değilse, bu alanlar pasif gelmektedir.

Yatırım Teşvik Belgesi kapsamında düzenlenecek faturalarda, "**Makine\\Teçhiza**t" mevzuat tipinde bir stok girildiğinde, faturanın kalemlerinde Makine ID ve Makine Teçhizat Sıra No bilgilerinin girilmesi gerekmektedir. Bu mevzuat tipine sahip stokların serili olması durumunda, istenirse zorunlu bilgilerin, seri ekranında yer alan alanlarla eşleştirilerek bu alanlara girilmesi sağlanabilir. Örneğin, Makine ID ve Makine Sıra No bilgilerinin seri ekranındaki hangi kolonlara girileceği buradan seçilebilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/91dc18d7-6261-48a2-930b-39ab51c4f5ba/yatırım teşvik 2.png)

Bu uygulama aktif edildiğinde, Yatırım Teşvik Belgesi (YTB) kapsamında yapılan teslimlere ilişkin faturaları belirlemek için, satış tarafında Satış Faturası ve Satış İrsaliyesi belgelerinin Üst Bilgiler sekmesine ve alış tarafında Alış Faturasının Üst Bilgiler sekmesine “**Y.Teşvik**” seçeneği eklenmiştir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/99351e15-4ec3-4525-99c3-1b6b0e72fbc4/yatırım teşvik 3.png)

Bu seçenek işaretlendiğinde, belge içinde kullanılacak stokları kontrol edebilmek için, Stok Kartı Kayıtları Ek Bilgiler sekmesinde yer alan Stok Mevzuat Tipi kısmına **“YTB-Makine/Teçhizat”, “YTB-İnşaat”, “YTB-Arsa/Arazi” ve “YTB-Diğer Harcamalar”** olmak üzere 4 yeni Stok Mevzuat Tipi eklenmiştir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/6d59089f-dc9c-4b77-a274-ee7a29c5a0fb/yatırım teşvik resim 3.png)

Yatırım teşvik belgelerinde kullanılan kalemlerin mevzuat tipi yukarıda da belirtildiği gibi "**Makine\\Teçhizat", "İnşaat", "Arsa \\ Arazi", "Diğer Harcamalar"** tiplerinden biri olmalıdır.

Stok kartlarında seçilen bu mevzuat tipleri e-Belgede **Harcama Tipi** olarak InvoiceLine alanında yer almaktadır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/2c3239b5-aa71-42c1-8077-f812dbd828e3/yatırım teşvik resim 4.png)

Bu alanın alabileceği kodlar ve açıklamaları aşağıdaki gibidir.

**01**: Makine ve teçhizat teslimleri ile yazılım ve gayri maddi hak satış ve kiralamalar

**02**: İnşaat işlerine ilişkin mal teslimleri ve hizmet ifaları

**03**: Arsa / Arazi Satışları

**04**: Diğer harcamalar

Örneğin, Stok kartında yer alan Mevzuat Tipi “**YTB-Makine/Teçhizat**” seçildiğinde, e-Belgede Harcama Tipi “01” olarak gelmektedir.

\*\*Yatırım teşvik belgesi kapsamında düzenlenecek faturalarda, "**Makine\\Teçhizat**" mevzuat tipinde bir stok girildiğinde, **Makine ID** ve **Makine Teçhizat Sıra No** bilgilerinin girilmesi gerekmetedir. Ayrıca stok kartlarında stok adlarının dolu olması gerekmektedir. Makine Adı bilgisi ModelName taginde yar almaktadır. Stok kartında stok adı kısmına girilen bilgi (ebelgede Item altındaki Name alanında) ModelName alanına varsayılan olarak yazılır. Kullanıcı bu bilgiyi değiştirmek isterse dizayn içerisinde ilgili ModelName tagine değer göndererek düzenleyebilir.

Satış Faturası Kalemler sekmesinde stok kodu satırı üzerinde sağ clickte gelen menüde “**Makine\\Teçhizat Detay Bilgileri**” tıklanır ve **Makine\\Teçhizat Detay Bilgileri** ekranı açılır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/ca349e3c-fa15-48f6-910e-295938a81e6d/yatırım teşvik resim 5.png)

Açılan ekranda Makine ID ve Makine Sıra No Bilgisi girilerek kaydedilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/c927edc0-4a39-49d1-928a-ecfc99eeba79/yatırım teşvik 4.png)

Ayrıca Makine\\Teçhizat Detay Bilgileri ekranında “**Excel Aktarımı**” seçeneği ile Makine ID ve Makine Sıra No bilgilerinin excelden aktarımı sağlanabilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/04dfbe7f-3c07-4dc6-87c8-931a54c9d3fb/yatırım teşvik 5.png)

YTB-Makine\\Teçhizat stok mevzuat tipinde girilen stok serili bir stok ise, Satış Parametre ekranında “**Yatırım Teşvik Uygulaması**” seçeneği altında Makine ID ve Makine Sıra No alanları seri ekranında hangi kolonlarla eşleştirildiyse, belgede kalemler kısmında açılan seri erkanında ilgili kolonlara bu bilgiler girilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/6fcf0e99-4c64-4bf4-9f6c-baebc453e39b/yatırım teşvik 6.png)

Bu girilen bilgiler xmlde InvoiceLine alanı altında aşağıdaki taglere yazılır.

**Item/Name:** Stok Adı

**Item/ModelName:** Makine Adı

**Item/ItemInstance/SerialID**: Makine ID

**Item/ItemInstance/ProductTraceID**: Makine Teçhizat Sıra No

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/35eb76a5-b97d-48ba-8719-4971e375fca3/ytesvik11.png)

Yatırım teşvik belgesi kapsamında düzenlenecek faturalarda, girilmesi gereken diğer zorunlu bilgiler ise, **Yatırım Teşvik Belgesi Kontrat Doküman** bilgileridir. 6 haneden ve sadece rakamlardan oluşan Yatırım Teşvik numarası ve tarih bilgisi girilmesi zorunlu alanlardır. Yatırım Teşvik Belgesi Kontrat Doküman bilgileri faturada sadece 1 adet bulunmalıdır.

Satış Faturasının Toplamlar sekmesinde sağ click menüsünde gelen “**Yatırım Teşvik Bilgi Girişi**” tıklanır ve “**Yatırım Belgesi Bilgi Girişi**” ekranı açılır ve zorunlu bilgiler girilerek kaydedilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/96b21aa5-1014-4c2f-b09a-309b17cd881c/yatırım teşvik resim 8.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/ef23a1d7-4fb6-4464-b020-6692144cf11a/yatırım teşvik resim 9.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/b47b6f80-f235-46d6-975a-b1ca85d9276c/yatırım teşvik resim 10.png)

Satış Faturası Üst Bilgiler sekmesinde “**Y. Teşvik**” parametresi işaretlendiğinde, Toplamlar sekmesinde **e-Fatura Senaryosu: Yatırım Teşvik** yazmaktadır.

Fatura ekranlarında üst bilgilerde **"Y. Teşvik**" parametresi işaretlenerek belge oluşturulduğu durumda Toplamlar sekmesinde sağ clickte **e-Devlet Özel Matrah/İstisna** menüsü altında **Özel Matrah/İstisna Atama** ekranında istisna kodu ataması yapıldığında istisna kodunun işleyişi aşağıdaki gibi olacaktır.

• "**Makine\\Teçhizat"** mevzuat tipinde bir stok için istisna varsa kalemde bu stok için kdv değeri girilir ve Toplamlarda "**308 - (13/d) Teşvikli Yatırım MallarınınTeslimi"** istisna kodu seçilmelidir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/a8e80e91-430f-4648-a84f-017952fdc5ab/yatırım teşvik resim 11.png)

• "**İnşaat**" mevzuat tipinde bir stok için istisna varsa kalemde bu stok için kdv değeri girilir ve Toplamlarda "**339 - İmalat Sanayi ile Turizme Yönelik Yatırım Teşvik Belgesi Kapsamındaki İnşaat İşlerine İlişkin Teslim ve Hizmetler"** istisna kodu seçilmelidir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/1bac67ef-da27-4d33-9acf-4b166904c76d/yatırım teşvik resim 12.png)

Yatırım Teşvik Belgesi (YTB) olan bir yatırımcıya yapılan bazı mal ve hizmet satışlarında KDV alınmaz. Bu durumda normalde fatura üzerinde KDV hesaplanır ama YTB olduğu için KDV tahsil edilmez. Alınmayan bu KDV tutarına “**Vazgeçilen KDV Tutarı**” denir. e-Fatura uygulamasında “**YATIRIMTESVIK**” senaryosunun altında “**ISTISNA**” fatura tipinde ve e-Arşiv Fatura uygulamasında “EARSIVFATURA” senaryosunun altında “**YTBISTISNA**” fatura tipinde düzenlenen faturalarda hesaplamaya dahil edilmeyen KDV tutarı **Vazgeçilen KDV Tutarı** alanında izlenmektedir.

Yatırım Teşvik Belgesi (YTB) kapsamında düzenlenen faturalarda istisna ataması olduğu durumda (308 ya da 339 varsa) Hesaplanan KDV tutarı e-belge görüntüsünde görülmeyecektir.

Belirtilen fatura tipleri için, xml tarafında aşağıdaki detaylar yansımaktadır.

- TaxTotal/ TaxSubtotal / **TaxCategory** elemanı altına istisna kodu girilir (308 veya 339).
- TaxTotal/ TaxSubtotal / **CalculationSequenceNumeric** elemanına, yazılan KDV tutarının (Vazgeçilen KDV Tutarı) fatura tutarların hesaplamasında dikkate alınmayacağının belirtilmesi için, “-1” değeri yazılır. Bu alan sadece XML üzerinden gösterilir.

İstisna Kodu girilmiş e-Belge görüntüsü aşağıdaki gibidir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/999cc06e-5529-4334-b8c0-b5a5353bb55d/ytesvık10.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/2cf186a7-c292-4e4d-8282-1644524ee427/ytesvık12.png)

**İşlem Türüne Göre Uygulama Senaryoları**

Yatırım teşvik belgesi kapsamında düzenlenecek faturalarda; yatırımın konusu ve teslim türüne göre (Makine, İnşaat, Arsa vb.) kullanılacak parametreler aşağıda kategorize edilmiştir.

1- Makine ve teçhizat teslimleri ile yazılım ve gayri maddi hak satış ve kiralamalarına ilişkin faturalarda yer alacak kalemlerin mevzuat tipi "Makine\\Teçhizat" olacaktır. Bu faturalar için senaryo, fatura tipleri ve varsa istisna bilgileri aşağıdaki tabloda özetlenmiştir.

• e-Fatura uygulamasında “YATIRIMTESVIK” fatura senaryosu altında “SATIS”, ”IADE” veya “ISTISNA” fatura tipinden,

• e-Arşiv Faturalarda “EARSIVFATURA” senaryosu altında “YTBSATIS”, “YTBIADE” veya “YTBISTISNA” fatura tipinden düzenlenmelidir.

• KDV tutarının “0” geçilmesi durumunda belirtilen fatura tiplerinden sadece “ISTISNA” veya “YTBISTISNA” fatura tipleri seçilerek, istisna kodlarından; “308- 13/d Teşvikli Yatırım Mallarının Teslimi” seçeneği kullanılmalıdır.

| Uygulama | Fatura Tipi (KDV var istisnaya tabi değil | Fatura Tipi (Vazgeçilen KDV Tutarı yansıtılacaksa) |
| --- | --- | --- |
| e-Fatura Senaryo:<br>YATIRIMTESVIK | SATIS veya IADE | ISTISNA<br>**İstisna Kod ve Açıklama**<br>308- (13/d) Teşvikli Yatırım Mallarının Teslimi |
| e-Arşiv Senaryo:<br>EARSIVFATURA | YTBSATIS veya YTBIADE | YTBISTISNA<br>**İstisna Kod ve Açıklama**<br>308- (13/d) Teşvikli Yatırım Mallarının Teslimi |

2- İnşaat işlerine ilişkin mal teslimleri ve hizmet ifalarına ait faturalarda yer alacak kalemlerin mevzuat tipi "İnşaat" olacaktır. Bu faturalar için senaryo, fatura tipleri ve varsa istisna bilgileri aşağıdaki tabloda özetlenmiştir.

• e-Fatura uygulamasında “YATIRIMTESVIK” fatura senaryosu altında “SATIS”, ”IADE” veya “ISTISNA” fatura tipinden,

• e-Arşiv Faturalarda “EARSIVFATURA” senaryosu altında “YTBSATIS”, ”YTBIADE” veya “YTBISTISNA” fatura tipinden düzenlenmelidir.

• KDV tutarının “0” geçilmesi durumunda belirtilen fatura tiplerinden sadece “ISTISNA” veya “YTBISTISNA” fatura tipleri seçilerek, istisna kodlarından; “339- İmalat Sanayi ile Turizme Yönelik Yatırım Teşvik Belgesi Kapsamındaki İnşaat İşlerine İlişkin Teslim ve Hizmetler” seçeneği kullanılacaktır.

| Uygulama | Fatura Tipi (KDV var istisnaya tabi değil | Fatura Tipi (Vazgeçilen KDV Tutarı yansıtılacaksa) |
| --- | --- | --- |
| e-Fatura Senaryo:<br>YATIRIMTESVIK | SATIS veya IADE | ISTISNA<br>İstisna Kod ve Açıklama<br>339- İmalat Sanayi ile Turizme Yönelik Yatırım Teşvik Belgesi Kapsamındaki İnşaat İşlerine İlişkin Teslim ve Hizmetler |
| e-Arşiv Senaryo:<br>EARSIVFATURA | YTBSATIS veya YTBIADE | YTBISTISNA<br>İstisna Kod ve Açıklama<br>339- İmalat Sanayi ile Turizme Yönelik Yatırım Teşvik Belgesi Kapsamındaki İnşaat İşlerine İlişkin Teslim ve Hizmetler |

3- Arsa ve Arazi Satışına ait faturalarda yer alacak kalemlerin mevzuat tipi "Arsa\\ Arazi" olacaktır. Bu faturalar için senaryo, fatura tipleri ve varsa istisna bilgileri aşağıdaki tabloda özetlenmiştir. Bu faturalar "0" KDV'li olarak düzenlenemez.

| Uygulama | Fatura Tipi<br>(KDV’ li) | Fatura Tipi<br>(KDV=0 ise) |
| --- | --- | --- |
| e-Fatura Senaryo:<br>YATIRIMTESVIK | SATIS | “0” KDV’ li olarak düzenlenemez. |
| e-Arşiv Senaryo:<br>EARSIVFATURA | YTBSATIS | “0” KDV’ li olarak düzenlenemez. |

4- “**Makine ve teçhizat teslimleri ile yazılım ve gayrimaddi hak satış ve kiralamaları”, “İnşaat işlerine ilişkin mal teslimleri ve hizmet ifaları” ile “Arsa ve Arazi Satışı”** haricinde yapılan teslim ve hizmetlere ait faturalarda yer alacak kalemlerin mevzuat tipi "Diğer Harcamalar" olacaktır. Bu faturalar için senaryo, fatura tipleri ve varsa istisna bilgileri aşağıdaki tabloda özetlenmiştir. Bu faturalar **"0" KDV'li olarak düzenlenemez.**

| Uygulama | Fatura Tipi<br>(KDV’ li) | Fatura Tipi<br>(KDV=0 ise) |
| --- | --- | --- |
| e-Fatura Senaryo:<br>YATIRIMTESVIK | SATIS | “0” KDV’ li olarak düzenlenemez. |
| e-Arşiv Senaryo:<br>EARSIVFATURA | YTBSATIS | “0” KDV’ li olarak düzenlenemez. |

- Yatırım Teşvik e-Faturaları için uygulama yanıtı verilememektedir. Temel fatura yapısı şeklinde ilerlenmektedir.
- Yatırım Teşvik Faturalarında IADE ve e-Arşiv faturalarda YTBIADE fatura tipi kullanılıyorsa, iadesi yapılan faturaya ait İade Fatura Numarası ve İade Fatura Tarihi bilgilerinin girişi zorunludur. (cac:BillingReference/cac:InvoiceDocumentReference)

**e-Arşiv Fatura Örneği**

EARSIVFATURA senaryolu YTBSATIS fatura tipli, belgede "Makine\\Teçhizat" mevzuat tipinde bir stok olan faturaya ait örnek e-Belge görüntüsü ve xml görüntüleri aşağıdaki gibidir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/b200ffc2-9426-433e-b1ef-e3907ca9f040/yatırım teşvik resim 15.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/42167d18-246c-42e6-9f50-71bf2fc59c73/yatırım teşvik resim 16.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/dd581f8d-5e25-481b-a088-2ef18ff6e4b8/yatırım teşvik resim 17.png)

**e-Fatura Örneği**

YATIRIMTESVIK senaryolu ISTISNA fatura tipli, belgede "Makine\\Teçhizat" mevzuat tipinde bir stok olan faturaya ait örnek e-Belge görüntüsü ve xml görüntüleri aşağıdaki gibidir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/999cc06e-5529-4334-b8c0-b5a5353bb55d/ytesvık10.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/83f0f047-deb2-40c4-b514-f99fbead3fea/ytesvık13.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/053cd757-2fa4-46b3-aff3-d59ee673eccd/ytesvık15.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/04842936-1b93-49b7-a067-bebd9fbf5ffc/ytesvık14.png)

Satış İrsaliyelerini Toplu Faturalama ve Müşteri Siparişlerini Toplu Faturalama ekranlarına “**Yatırım Teşvik**” adında bir seçenek eklenmiştir. Bu seçenek işaretlenerek oluşacak faturaların yatırım teşvik tipinde oluşması sağlanmıştır.

Bu seçenek işaretlenerek fatura oluşturuluyorsa, fatura satırlarındaki stok kodlarının stok mevzuat tiplerinin izin verilen tiplerden biri olup olmadığı kontrol edilmektedir. Eğer aykırı bir değer varsa, o fatura oluşturulmayarak kullanıcıya işlem sonunda mesaj verilecektir.

Ayrıca satış irsaliyesileri toplu faturalaştırılırken “Yatırım Teşvik” işaretli bir irsaliye ile “Yatırım Teşvik” işaretli olmayan irsaliyelerle birleştirilmeyecek, “Yatırım Teşvik” seçimine göre oluşacak faturalar kırılımlı olarak oluşacaktır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/5323dcf1-8b79-4241-9a83-24156a32d19a/yatırım teşvik 7.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/15e74a8a-7c01-4312-99eb-e1f312ba1b01/yatırım teşvik 8.png)

Zarf/Fatura Bazında Gelen e-Fatura ekranlarında yatırım teşvik faturalarının senaryo bilgileri Yatırım Teşvik olarak gelmektedir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/fac5d712-d2db-4993-8a0b-df49acf67dd2/yatırım teşvik 9.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/1ea562c4-87c9-4ffa-aa6d-a889cd65f0b8/yatırım teşvik 10.png)

Gelen e-Faturadan Alış Faturası Oluşturma adımında oluşan alış faturasında e-Belgede yer alan yatırım teşvik ile ilgili bilgilerin aktarılması ve bu bilgilerin izlenmesi sağlanmaktadır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/2e916a1b-f959-4897-9ef7-e9ba1a0342a6/yatırım teşvik 11.png)

Yatırım Teşvik Belgesi (YTB) Kapsamında Yapılan Teslimlere İlişkin e-Fatura [dizayn örneği](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/8edf43e3-885a-4f8c-91b4-82dcce87c7d2/YTESVIK1.rar)
