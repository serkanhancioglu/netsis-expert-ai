---
title: "Netsis e-Fatura UBL-TR v1.2 Geçişi"
page_id: "50680048"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis e-Fatura UBL-TR v1.2 Geçişi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis e-Fatura UBL-TR v1.2 Geçişi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTE2MWYwOTlkLWVlMDUtNGMzZi1iYzhkLTcxYjY4OTBjMjFiZiZsaW5rPTQxZmY1NzhkLWYxZjctNGNhNC04ZDQwLWU4MDQ4NmMwZTBmZSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=161f099d-ee05-4c3f-bc8d-71b6890c21bf&link=41ff578d-f1f7-4ca4-8d40-e80486c0e0fe&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-e-fatura-ubl-tr-v1-2-gecisi_82576459_50680048.html"
source_version: "2022-11-03T09:42:54.830+03:00"
source_bytes: 1601069
fetched_at: "2026-09-13T04:26:06+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis e-Fatura UBL-TR v1.2 Geçişi

Netsis e-Fatura UBL-TR v1.2 Geçişi ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

|  |  |
| --- | --- |
| Amaç ve Fayda | Gelir İdaresi Başkanlığı tarafından yürütülen elektronik fatura çalışmaları kapsamında oluşturulan UBL-TR v1.2, UBL 2.1 standardında yer alan belgelerden fatura ve uygulama yanıtının ülkemiz koşullarına göre özelleştirilmesi sonucunda elde edilmiştir. UBL-TR1.2 ile gelen değişiklikler veya yenilikler, XML seviyesinde teknik düzenlemeler ve iş mantığı seviyesinde içerik düzenlemeler olarak Netsis e-fatura uygulamasında desteklenmiştir. |
| Ürün Grubu | \[X\] Netsis Enterprise<br>\[X\] Netsis Standard<br>\[X\] Netsis Entegre |
| Modül | \[X\] Fatura |
| Kategori | \[X\] Yeni Fonksiyon |
| Versiyon Önkoşulu | **7.0.4**/**8.0.4**/**8.0.6** setlerinde desteklendi, tüm setlerde aktif olabilmesi için **8.0.6** onaylı sürüm kontrolü yapılmaktadır. |
| Dosyalar | Fatura.dll, dekont.dll, e-fatura.dll, EFaturaConsole.exe, EfaturaAyarlar.exe Netsis.EFatura.WebService.dll ve XSD klasöründeki dosyalar **DBUpdate** (Sadece 8.0.6 seti için desteklenmiştir, 7.0.4 ve 8.0.4 setleri için dışarıdan scriptlerin çalıştırılması gerekmektedir) |

**UBL-TR** **v1.2** **ile** **Gelen** **Değişiklikler**

XML yapısındaki değişikliklerle birlikte fatura içeriğine bir çok yeni alan eklenmiştir. Yeni eklenen alanların yanında güncel versiyonda kullanımda olan bazı alanların da kullanım şekli ve içeriğinde değişiklikler olmuştur.

Yayınlanan değişiklik veya yeniliklerden Netsis e-fatura uygulamasında desteklenen özellikleri şunlardır:

- Para birimi kodları Para birimi kodları için kullanılan ISO 4217 listesinin en son sürümü entegre edildi. Bu sürümde Türk Lirası için kod TRY'dir.
- UBL versiyon numarası değişti: cbc:UBLVersionID değeri 2.1 olarak oluşturuluyor.
- Özelleştirme numarası değişti: cbc:ProfileID değeri TR1.2 olarak oluşturuluyor.
- Fatura tipi elemanı içeriğine yeni değerler eklendi: Daha önce zorunlu olmayan bu alan zorunlu olmuştur ve sadece SATIS ve IADE değerlerini alırken artık ilave olarak ISTISNA, OZELMATRAH, TEVKIFAT ve IHRACKAYITLI değerlerini de alabilmektedir.
- Ölçü birimi kodları Birim kodlarında öncelikli olarak T.C. Gümrük ve Ticaret Bakanlığı'nın ölçü birimi kodları kullanılacaktır.

Tevkifat konusunda yapılan değişiklikler aşağıdadır:

- Tevkifat kalemleri Toplam Vergi elemanında (cac:TaxTotal) yer almamalı.
- Tevkifat kalemleri Tevkifat Bilgileri elemanında (cac:WithholdingTaxTotal) yer alıyor.

- KDV tevkifat 9015 kodu yerine tevkifat kodları ile gönderiliyor.
- 6 ile başlayan, 3 haneli tevkifat kodları kullanılıyor.

Vergi istisnaları konusunda yapılan değişiklikler aşağıdadır:

- Vergi istisnaları olduğu zaman muafiyet sebebi kodu doldurulması zorunlu hale geldi.
- İstisna kapsamında ise kod listesinde açıklanan kodlar istisna kodları olarak kullanılmalı
- Özel matrah kapsamında ise kod listesinde açıklanan kodlar özel matrah kodları olarak kullanılmalıdır.

#### İskonto ve Ek Maliyet Bilgileri (cac:AllowanceCharge)

Netsis faturasının toplamlarında oluşan genel iskontolar, toplam satır iskontosu, toplam mal fazlası iskontosu ve ek maliyet bilgileri detaylı olarak xml de desteklenmektedir.

Bu destek için xml şu değişiklik yapılmıştır:

- Sıra numarası bilgisi eklendi(cbc:SequenceNumeric)
- Mal fazlası iskontosu yapıldığında kullanılması için ürün adeti bilgisi eklendi (cbc:PerUnitAmount)

Fatura Kalemlerine aşağıdaki alanlar eklendi:

- **Sipariş** **Bilgileri (cac:OrderReference)** Önceki versiyonda sadece xml in üst bilgilerinde gösterilebilen sipariş bilgileri, yeni xml versiyonuyla artık kalem bilgilerinde de desteklenmektedir. Bu destek için xml in kalemlerine Netsis faturasının kalemlerindeki sipariş numarası ve sipariş sıra numarası yazılmaktadır.
- **İrsaliye Bilgileri (cac: DespatchDocumentReference)** Önceki versiyonda sadece xml in üst bilgilerinde gösterilebilen irsaliye bilgileri, yeni xml versiyonuyla artık kalem bilgilerinde de desteklenmektedir. Bu destek için xml in kalemlerine Netsis faturasının kalemlerindeki irsaliye numarası ve irsaliye sıra numarası yazılmaktadır.

#### Tevkifat bilgileri (cac:WithholdingTaxTotal)

Bu alanların dışında kalan alanlarla ilgili detaylı bilgi için UBL 2.1 paketinde yer alan fatura belgesinde geçen elemanlara ait XSD, tanımlama, kullanım şekilleri, kardinaliteler hakkında bilgi almak için gelir idaresinin web sayfası incelenebilir.

#### Netsis e-fatura Uygulamasındaki Değişiklikler

Gelir idaresi yayınladığı duyuru ile, 15.09.2015 saat 10:00 itibariyle UBL 2.1 standardı esas alınarak Gelir İdaresi Başkanlığı tarafından oluşturulan **UBL-TR1.2** şeması e-fatura GERÇEK ortamında uygulamaya koyacaktır. Müşterilerimizin yeni özellikleri destekleyebilmeleri için gerekli olan set dosyalarını güncellemeleri ve gerekiyorsa dizaynlarındaki düzenlemeleri geçiş tarihinin öncesinde bitirmiş olmaları gerekmektedir.

#### E-fatura Parametreleri

15.09.2015 saat 10:00 itibariyle yeni versiyona göre e-faturaların oluşturulabilmesi için öncelikle e-fatura parametrelerinden e-fatura XML versiyonu alanından UBLTR1.2 seçimi yapılmalıdır. Bu seçim yapılmadan önce taslaklarda bekleyen belge olmamalıdır, daha önceden oluşturulan taslakların gelir idaresinin açıkladığı saatten önce gönderilmiş olması, eğer süreden sonra eski versiyonda oluşturulan taslaklar varsa da onların silinip parametreyi işaretledikten sonra tekrar taslak oluşturulması gerekmektedir.
![](../_assets/9b9d83c93e308e4c3ce4.png)![](../_assets/f03e0e24d01097a73bb6.png)
**Fatura Tip Kodu (InvoiceTypeCode):** Daha önce SATIS ve IADE değerlerini alan e-faturalar, düzenleme amaçlarına göre yeni değerler getirilmiştir. Her türlü mal ve hizmet satışı ile ilgili düzenlenen faturalar için "SATIS" değerini; bir malın iadesi amacıyla alıcı tarafından düzenlenen faturalar ise "IADE" değerini; tevkifat içeren faturalar için "TEVKIFAT" değerini; vergi istisnası içeren faturalar için "ISTISNA" değerini ve özel matrah faturaları için "OZELMATRAH" değerini ve ihraç kayıtlı faturalar için "IHRACKAYITLI" değerini alacaktır.

#### Vergi İstisnası

Vergi istisnası veya özel matrah kapsamında olan faturalar için Netsis fatura ekranında toplamlar sayfasında sağ klikte yeni eklenen istisna ve özel matrah kodunun seçilmesi yeterli olacaktır. Bu durumda xml dosya oluşturulurken InvoiceTypeCode alanına seçilen koda göre ISTISNA veya OZELMATRAH getirilecektir. Bu durumların dışında kalan faturalar eskisi gibi SATIS veya IADE tipinde oluşturulmaya devam edilecektir.
Belgenin ISTISNA veya OZELMATRAH olarak belirtilmesi için toplamlardan tip seçimi yapılmalıdır. Seçilen tip bilgisi XML deki (TaxExemptionReasonCode) alanına yazılacaktır. Bu işlem sırasında kullanılacak olan tip tanımları uygulamaya yeni eklenen "e-fatura özel kod tanımlama" ekranından yapılmalıdır.
![](../_assets/4a1d1717d59e76011491.png)![](../_assets/583d251197d8f7e0ab4e.png)![](../_assets/9ed1026b29b6028e02c1.png)
**Tevkifat** **(WithholdingTaxTotal):** Netsis faturasında tevkifatlı bir satır eklenmiş ise oluşturulan faturanın xml dosyasında InvoiceTypeCode alanına otomatik olarak TEVKIFAT getirilmektedir. Xmlde Önceki versiyonda vergilerin içerisinde (TaxTotal alanında) gösterilen tevkifat bilgileri, yeni düzenleme ile xmlde kendi alanında (WithHoldingTaxTotal) gösterilecektir. Bu alanda gösterilirken tevkifat ile ilgili detay bilgiler (Tevkifat oranı, Tevkifat tipi gibi) de bu alanın içinde gösterilecektir.
Netsis uygulamasında öncelikle gelir idaresinin açıkladığı firmada kullanılan tevkifat kodlarının tanımlamasının yapılması gerekmektedir. Bunun için uygulamaya yeni eklenen e-fatura özel kod tanımlama ekranında tipi tevkifat olan tanımlamalar yapılmalıdır.
Daha sonra Netsis'te takip edilen tevkifat uygulamasına göre tanımlamalar yapılmalıdır. Buna göre sadece genel tevkifat uygulaması kullanılıyorsa, e-fatura parametrelerine eklenen e-fatura Tevkifat kodu alanına gerekli tanımlama yapılmalıdır.
Eğer satır bazında tevkifat takibi yapılıyor ise bu durumda tevkifat oran tanımlama ekranından kullanılan kodlar için efatura tevkifat kodlarının seçimi yapılmalıdır.
![](../_assets/73a28bb4ee1670dc5eb4.png)![](../_assets/dc1b0b4e216926c3b0ca.png)
Bu şekilde sabit tanımlamalar yapıldıktan sonra, kaydedilen fatura belgesinde tevkifat bilgisi varsa belgenin tipi kullanıcının ek bir tanımlama yapmasına gerek kalmadan otomatik olarak TEVKIFAT yapılmakta ve XML tevkifatla ilgili bilgilerde (WithholdingTaxTotal) alanında doldurulmaktadır. Seçilen tip bilgisi XML deki (TaxTypeCode) alanına yazılacaktır.

#### İhraç Kayıtlı Fatura

İhraç kayıtlı olarak kesilen ihracat faturları için xml dosya oluşturulurken InvoiceTypeCode alanına IHRACKAYITLI getirilecektir. Bunun için ihracat kapatma ekranlarına yeni eklenen "İhraç Kayıtlı Fatura Sebebi" alanından uygun bilginin seçilmesi gerekmektedir. Bu durumda xml dosya oluşturulurken InvoiceTypeCode alanına IHRACKAYITLI getirilecek, istisna sebebini bildiren alanada (TaxExemptionReasonCode) İhraç kayıtlı Satışlar seçildiğinde 701 diğer alan seçildiğinde ise 702 kodu getirilecektir.

**Genel İskontolar ve Alt Maliyetler(AllowanceCharge):** Önceki versiyonda sadece bir adet desteklenen iskonto yeni düzenleme ile çoklanabilir hale gelmiştir. Aynı zamanda mal bazı iskonto ve ek maliyet desteği de aynı şekilde desteklenmiştir. Netsis fatura kaydında bu destek için özel yapılması gereken bir durum bulunmamamktadır, yeni haliyle xml oluşturulurken eğer birden fazla genel iskonto tespit edildi ise hepsi ayrı ayrı olarak kaydedilmektedir.
Daha önce belgeye ek kalem olarak eklenen ek maliyet bilgileri ise artık ek kalem olarak gösterilmeyip AllwanceCharge içinde desteklenmiştir.
Not: AllowanceCharge kalemde de kullanılan bir yapıdır, Netsis'te satır bazında birden fazla iskonto kullanılsa bile bu iskontolar mevcut xml de olduğu gibi kümüle satır iskontosu olarak xml de desteklenmektedir. Satır bazında detaylı iskonto desteklenmemiştir.

**OrderLineReference:** Daha önce XML de sadece üst bilgilerde tutulan sipariş bilgileri artık kalemlerde de takip edilebilmektedir. Bu destek için uygulamada ilave bir tanımlama yapılmasına gerek bulunmamaktadır. Mevcut fatura kayıtlarındaki bilgiler kalemlere de taşınmaktadır.

**DespatchLineReference:** Daha önce XML de sadece üst bilgilerde tutulan irsaliye bilgileri artık kalemlerde de takip edilebilmektedir. Bu destek için uygulamada ileve bir tanımlama yapılmasına gerek bulunmamaktadır. Mevcut fatura kayıtlarındaki bilgiler kalemlere de taşınmaktadır.

#### XSLT Fatura Dizaynları Hakkında

UBL TR 1.2 ile e-Fatura'daki mevcut alanlarda ve içerikte değişiklikler olduğu için UBL TR 1.0 formatındaki e- Faturaları görüntülemek üzere hazırlanmış XSLT fatura dizaynlarının UBL TR 1.2 e-Fatura formatına göre yeniden düzenlenmesi gerekmektedir.

XSLT Değişikliğinde Dikkat Edilecek Noktalar:

- TRL kısaltmasına göre yapılmış yerlerin TRY kısaltmasına uyumlu çalışmasını sağlamak gerekmektedir. Yeni dosyalarla birlikte oluşturulmuş olan e-faturaların izlenmesinde varsa tutarların yanında bulunan Türk Lirası kısaltmaları görünmüyor veya yanlış görünüyorsa XSLT'niz bu UBL değişikliğini desteklemiyor olabilir. Bu sorunu giderilmesi için XSLT dosyanızda gerekli düzenlemelerin yapılması gerekmektedir.
- Tevkifatların TaxTotal yerine WithholdingTaxtotal alanından gösterilmesi gerekmektedir. Fatura içerisinde WithholdingTaxTotal alanı dolu ise ve bu alanda bulunan tevkifatlar görüntülenmiyorsa XSLT'nizde gerekli düzenlemelerin yapılması gerekmektedir. Tevkifatlı faturaya örnek xslt kodu incelenebilir.

- KDV tevkifatların tevkifat kodlarınının gösterilmesi isteniyorsa XSLT'nizde gerekli düzenlemelerin yapılması gerekmektedir.
- Satırdaki sipariş (InvoiceLine/ OrderLineReference) bilgilerinin veya irsaliye bilgilerinin (DespatchLineReference) elemanları kullanılarak XSLT'nizde görünmesi sağlanabilir.
- Satırdaki ve dip toplamdaki vergilerin içerisinde muafiyet sebebi ile birlikte muafiyet sebebi kodu (TaxExemptionReasonCode) alanının içeriğinin gösterilmesi isteniyorsa XSLT'nizde gerekli düzenlemelerin yapılması gerekmektedir.
- Netsis'te farklı genel iskonto veya ek maliyet kullanıldığı durumlarda xml de bu bilgiler artık detaylı gönderilebilmektedir. XSLT'nizde detaylı gösterilmesi istendiğinde fatura dizaynında düzenleme yapılması gerekmektedir. Detaylı gösterilmeyip mevcut haliyle devam etmesi isteniyorsa değişiklik yapılmasına gerek yoktur.
- FaturaTipi bilgisi kısmında SATIS ve IADE'nin yanında OZELMATRAH, TEVKIFAT, ISTISNA ve IHRACKAYITLI değerlerinin de gösterilebilmesi için XSLT'nizde gerekli düzenlemelerin yapılması gerekmektedir.
