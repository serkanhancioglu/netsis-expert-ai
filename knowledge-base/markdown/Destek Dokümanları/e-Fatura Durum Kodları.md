---
title: "e-Fatura Durum Kodları"
page_id: "50684268"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "e-Fatura Durum Kodları"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / e-Fatura Durum Kodları"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWQ3N2EwOGRhLTg2YmUtNDVkMS1iZmMxLTAyZDMxZTVkZTIxZSZsaW5rPWM4YTIwOTk0LTcxZWEtNDE1NS04Y2Y4LTM0MTJmNjU5MjE0OCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=d77a08da-86be-45d1-bfc1-02d31e5de21e&link=c8a20994-71ea-4155-8cf8-3412f6592148&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "e-fatura-durum-kodlari_50684269_50684268.html"
source_version: "2022-11-03T09:55:17.727+03:00"
source_bytes: 48992
fetched_at: "2026-09-13T04:26:27+00:00"
generator: "netsis-scraper 1.0.0"
---
# e-Fatura Durum Kodları

e-Fatura Durum Kodları ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

e-Fatura GİB durum kodları şunlardır:

| **GIB** **DURUM** **KODLARI** |  | AÇIKLAMALARI | SEBEP | ÇÖZÜM | **İlgili durumda** **yapılması** **gereken** |
| --- | --- | --- | --- | --- | --- |
| \*1000 | ZARF KUYRUĞA EKLENDİ | Gönderici birim, içerisinde FATURA belgesi olan zarfı oluşturur ve Merkez Birime (GİB' e) gönderir. Bu zarf Merkez Birimde kuyruğa alınır. Zarfın durumu "ZARF KUYRUĞA EKLENDİ" olur. | GİB'teki yoğunluk | - | Durum kodunun güncellenmesi **beklenmelidir.** |
| \*1100 | ZARF İŞLENİYOR | Merkez Birimde kuyruğa alınan zarf, kuyrukta sırası geldiğinde işlenmeye başlar. Burada zarfın durumu "ZARF İŞLENİYOR" olmaktadır. "1000" ve "1100" statülerinde zarf GİB' e iletilmiştir. Bu aşamalarda Gönderici Birim Merkez'de durum sorgular ve bu iki durum kodundan biri cevap olarak dönerse faturanın ERP statüsü "GİB'e gönderildi" olur. | GİB'teki yoğunluk | - | Durum kodunun güncellenmesi **beklenmelidir**. |
| 1110 | ZIP DOSYASI DEĞİL | **NOT:** Zarf gönderim aşamalarında çeşitli işlemlerden, şema ve schematron kontrolünden geçer. Gönderilen zarfın GİB'in belirlediği standartlara uygun olmamasından dolayı hata alınırsa ilgili durum kodları alınır.<br>Faturanın bulunduğu zarfa GİB'de işlenmesi sırasında ilgili hata kodlarından birini alırsa faturanın statüsü "GİB'de işlenemedi" olarak güncellenir. Bu aşamadan sonra süreç sonlanır, işlem alıcıya iletilemeden bu aşamada kalır. | Zarf formatı ".ZIP" formatında değilse ilgili hata alınır. | Gönderilen zarf formatı ".ZIP" olmalıdır. | Faturalar yeniden gönderilmeli<br>(faturanın aynı ETTN ile tekrar gönderimine<br>izin verilir.) |
| 1111 | ZARF ID UZUNLUĞU GEÇERSİZ |  | ZARF ID uzunluğu 32 karakterden farklıysa ilgili hata alınır. | ZARF ID uzunluğu 32 karakter olmalıdır. | Faturalar yeniden gönderilmeli.<br>(faturanın aynı ETTN<br>ile tekrar gönderimine izin verilir.) |
| 1120 | ZARF ARŞİVDEN KOPYALANAMADI |  |  |  | Faturalar yeniden gönderilmeli.<br>(faturanın aynı ETTN<br>ile tekrar gönderimine izin verilir.) |
| 1130 | ZIP AÇILAMADI |  | Zarf okunamadığı durumlarda ilgili hata alınır. | GIB sisteminde geçici bir durum<br>olabilir ve ya zarfın dosyasında hata da olabilir. Dosyada hata var ise, yeniden zarflanıp gönderilmesi gerekmektedir.<br>Aksi halde faturalar yeniden gönderilmeli | Faturalar yeniden gönderilmeli.<br>(faturanın aynı ETTN ile tekrar gönderimine izin verilir.) |
| 1131 | ZIP BİR DOSYA İÇERMELİ |  | Zarf içerisinde dosya bulunmadığında ilgili hata alınır. | Zarf içerisinde dosya (Fatura, uygulama yanıtı, sistem yanıtı) olmalıdır. | Faturalar yeniden gönderilmeli.<br>(faturanın aynı ETTN<br>ile tekrar gönderimine izin verilir.) |
| 1132 | XML DOSYASI DEĞİL |  | Dosyalar (Fatura, U&S Yanıtı)<br>.XMLformatında olmadığında ilgili hata alınır. | Dosyalar (Fatura, U&S Yanıtı) .XML formatında olmalıdır. | Faturalar yeniden gönderilmeli.<br>(faturanın aynı ETTN<br>ile tekrar gönderimine izin verilir.) |
| 1133 | ZARF ID VE XML DOSYASININ ADI AYNI OLMALI |  | ZARF ID<br>(\<sh:documentidentification\>) ile XML ID(xxxxxxxx.xml) aynı karakterleri içermez ise ilgili hata alınır. | ZARF ID<br>(\<sh:documentidentification\>) ile XML ID(xxxxxxxx.xml) aynı karakterleri içermelidir. | Faturalar yeniden gönderilmeli.<br>(faturanın aynı ETTN<br>ile tekrar gönderimine izin verilir.) |
| 1140 | DOKUMAN<br>AYRIŞTIRILAMADI |  | Zarftaki faturalar doğru şekilde çıkarılamadığı için ilgili hata alınır. |  | Faturalar yeniden gönderilmeli(faturanın aynı ETTN ile tekrar<br>gönderimine izin verilir.) |
| 1141 | ZARF ID YOK |  | Zarf ID alanı boş ise ilgili hata alınır. | Zarf ID alanı boş olmamalıdır. | Faturalar yeniden gönderilmeli(faturanın aynı ETTN ile tekrar<br>gönderimine izin verilir.) |
| 1142 | ZARF ID VE ZIP DOSYASI ADI AYNI OLMALI |  | Zarf ID ve ZIP dosyası adı aynı değil ise ilgili hata alınır. | Zarf ID ve ZIP dosyası adı aynı olmalıdır. | Faturalar yeniden gönderilmeli.<br>(faturanın aynı ETTN ile tekrar gönderimine izin verilir.) |
| 1143 | GEÇERSİZ VERSİYON |  |  |  | Faturalar yeniden gönderilmeli.<br>(faturanın aynı ETTN ile tekrar gönderimine<br>izin verilir.) |
| 1150 | SCHEMATRON KONTROL SONUCU HATALI |  | GIB'in belirlediği standartlarda olması gereken bilgiler yanlış girilmiştir. | Bilgiler kontrol edilip GIB'in belirlediği standartlara uygun hale getirilmelidir. | Faturalar yeniden gönderilmeli.<br>(faturanın aynı ETTN<br>ile tekrar gönderimine izin verilir.) |
| 1160 | XML SEMA KONTROLÜNDEN GEÇEMEDİ |  | GİB şema kontrollerinden geçebilen bir faturanın alıcının sisteminde de XML<br>kontrollerinden geçebilmesi gerekir. Alıcıyı uyarınız. |  | Faturalar yeniden gönderilmeli.<br>(faturanın aynı ETTN<br>ile tekrar gönderimine izin verilir.) |
| 1161 | İMZA SAHİBİ TCKN VKN ALINAMADI |  |  |  | Faturalar yeniden gönderilmeli.<br>(faturanın aynı ETTN<br>ile tekrar gönderimine izin verilir.) |
| 1162 | İMZA<br>KAYDEDİLEMEDİ |  |  | Hatasız gönderim için gönderimden önce "imza doğrulama" kontrolü yapılmalıdır. | Faturalar yeniden gönderilmeli.<br>(faturanın aynı ETTN ile tekrar gönderimine<br>izin verilir.) |
| \*\*1163 | GÖNDERİLEN ZARF SİSTEMDE DAHA ÖNCE KAYITLI OLAN BİR FATURAYI İÇERMEKTEDİR | Merkez birim zarfı posta kutusuna gönderir. Eğer gönderim başarılı olmuşsa öncelikle zarfın merkezdeki durum kodu posta kutusundan sistem yanıtı gelene kadar 1220 "HEDEFTEN SİSTEM YANITI GELMEDİ" şeklinde<br>olur. Bu zarftaki faturaların herhangi birinin yeni bir zarf ile tekrar gönderilmesi durumunda yeni gönderilen zarf 1163 "GÖNDERİLEN ZARF SİSTEMDE DAHA ÖNCE KAYITLI OLAN BİR FATURAYI İÇERMEKTEDİR"<br>durum kodunu içeren sistem yanıtını alacaktır.<br>**NOT:** 1300 durum kodu almış zarflar da tekrar gönderilirse aynı hata alınır. | Merkez birim zarfı posta kutusuna gönderir. Eğer gönderim başarılı olmuşsa öncelikle zarfın merkezdeki durum kodu posta kutusundan sistem yanıtı gelene kadar 1220 "HEDEFTEN SISTEM<br>YANITI GELMEDI" şeklinde olur.Bu zarftaki faturaların herhangi birinin yeni bir zarf ile tekrar gönderilmesi durumunda yeni gönderilen zarf 1163 "GONDERILENZARF SISTEMDE DAHA ONCE KAYITLI OLAN BIRFATURAYI<br>ICERMEKTEDIR" durum kodunu içeren sistem yanıtını alacaktır. | 1163 "GONDERILEN ZARF SISTEMDE DAHA ONCE KAYITLI OLANBIR FATURAYI<br>ICERMEKTEDIR" durumu aynı fatura numarası ya da ETTN numarası ile daha önce gönderim (yükleme) yapıldığı durumlarda oluşur (farkında olmadan aynı fatura ya da ETTN numarası ile ikinci kez gönderim yapmaya çalışıyor olabilirsiniz. | Faturalar yeniden<br>**Gönderilmemeli.**<br>**Bu hata** **kodunun** **alınması durumunda** **dokümanın** **en** **altında**<br>**yer alan işlem** **adımlarını**<br>**uygulayablirsiniz.** |
| 1170 | YETKİ KONTROL EDİLEMEDİ |  |  |  | Faturalar yeniden gönderilmeli.<br>(faturanın aynı ETTN ile tekrar gönderimine<br>izin verilir.) |
| 1171 | GÖNDERİCİ BİRİM YETKİSİ YOK |  | Gönderici birim etiketinde "GB" yerine "PK" tanımlanmış olabilir. | Gönderici birin etiketinde "GB" tanımlı olmalıdır. | Faturalar yeniden gönderilmeli.<br>(faturanın aynı ETTN |
|  |  | **NOT:** Zarf gönderim aşamalarında çeşitli işlemlerden, şema ve schematron kontrolünden geçer. Gönderilen zarfın GİB'in belirlediği standartlara uygun olmamasından dolayı hata alınırsa ilgili durum kodları alınır.<br>Faturanın bulunduğu zarfa GİB'de işlenmesi sırasında ilgili hata kodlarından birini alırsa faturanın statüsü "GİB'de işlenemedi" olarak güncellenir. Bu hata kodlarını içeren Sistem Yanıtı doğrudan merkez tarafından Gönderici Birim'e iletilir ve bu aşamadan sonra süreç sonlanır, işlem alıcıya iletilemeden bu aşamada kalır. |  |  | ile tekrar gönderimine izin verilir.) |
| 1172 | POSTA KUTUSU YETKİSİ YOK |  | Posta kutusu etiketinde "PK" yerinde "GB" tanımlanmış olabilir. | Posta kutusu etiketinde "PK" tanımlı olmalıdır. | Faturalar yeniden gönderilmeli.<br>(faturanın aynı ETTN ile tekrar gönderimine izin verilir.) |
| 1175 | İMZA YETKİSİ KONTROL<br>EDİLEMEDİ |  | İmza yetkisi kontrol edilemedi yanıtı imzanın yetersiz olduğu anlamına **gelmemektedir**. Müşterinin ekstra kontrol istediği durumlarda ilgili hata alınır. | . | Faturalar yeniden gönderilmeli.<br>(faturanın aynı ETTN ile tekrar gönderimine<br>izin verilir.) |
| 1176 | İMZA SAHİBİ YETKİSİZ |  |  |  | Faturalar yeniden gönderilmeli.<br>(faturanın aynı ETTN ile tekrar gönderimine izin verilir.) |
| 1177 | GEÇERSİZ İMZA |  | İmza doğrulama geçersizdir. | Hatasız gönderim için gönderimden önce "imza doğrulama" kontrolü yapılmalıdır. | Faturalar yeniden gönderilmeli.<br>(faturanın aynı ETTN<br>ile tekrar gönderimine izin verilir.) |
| 1180 | ADRES KONTROL EDİLEMEDİ |  |  |  | Faturalar yeniden gönderilmeli.<br>(faturanın aynı ETTN<br>ile tekrar gönderimine izin verilir.) |
| 1181 | ADRES BULUNAMADI |  | Etiket bilgisi ve VKN eşleşmesi yapılamıyor. | Alıcının VKN/TCKN ve etiket bilgisinin güncel olduğundan emin olunuz. (Etiket ya da yöntem değiştirmiş olabilir.)Göndericinin VKN/TCKN ve etiket bilgisinin güncel olduğundan emin olunuz.<br>(Etiket ya da yöntem değiştirmiş olabilir.) | Faturalar yeniden gönderilmeli.<br>(faturanın aynı ETTN ile tekrar gönderimine<br>izin verilir.) |
| 1182 | KULLANICI<br>EKLENEMEDİ |  |  |  | Faturalar yeniden gönderilmeli.<br>(faturanın aynı ETTN ile tekrar gönderimine<br>izin verilir.) |
| 1183 | KULLANICI SİLİNEMEDİ |  |  |  | Faturalar yeniden gönderilmeli.<br>(faturanın aynı ETTN ile tekrar gönderimine izin verilir.) |
| 1190 | SİSTEM YANITI HAZIRLANAMADI |  |  |  | Faturalar yeniden gönderilmeli.<br>(faturanın aynı ETTN |
|  |  |  |  |  | ile tekrar gönderimine izin verilir.) |
| 1195 | SİSTEM HATASI |  |  |  | Faturalar yeniden gönderilmeli.<br>(faturanın aynı ETTN ile tekrar gönderimine izin verilir.) |
| 1200 | ZARF BAŞARIYLA İŞLENDİ | Zarf işlenmiş, kontrollerden geçmiş ve merkez sistemde bir hata almamışsa zarfın durumu "ZARF BAŞARIYLA İŞLENDİ" olmaktadır. Bu aşamada zarfın durumu sistem yanıtı ile Gönderici Birime gönderilir. GİB' ten 1200 durum kodu "Zarf Başarıyla İşlendi" metni ile sistem yanıtı gönderildiğinde ERP statüsü "GİB' de işlendi- Alıcıya gönderilecek" olarak güncellenir. Aynı statü kodu Alıcı tarafından gönderildiğinde ise; bu zarfın alıcı tarafında işlendiği anlamına gelecektir. | - | - | - |
| \*1210 | DOKUMAN BULUNAN ADRESE GÖNDERİLEMEDİ | Zarf merkezde işlendikten sonra alıcıya gönderilir. Alıcıya gönderme sırasında herhangi bir sorun yaşanır ve zarfın gönderimi başarısız olur ise; göndericiye 1210 durum kodu döner. (Merkez birim zarfı dört defa göndermeyi dener, ilki göndericinin gönderip GİB'den geçerek alıcıya iletildiği saattir. 1210 durumu alınırsa GİB aynı zarfı 3 kere daha göndermeyi dener. 3 deneme saat 06.00 ve 18.00 saatleri arasında sırayla yapılmaktadır.) | - | GIB'in tekrar gönderim denemesi başarılı olur ise, 1300 BAŞARIYLA TAMAMLANDI durum kodu alınır. Eğer bu süre sonlandıktan sonra gönderim hala başarısız ise, 1215 DOKÜMANGÖNDERİMİ BAŞARISIZ, TEKRAR GÖNDERME<br>SONLANDI durum kodu alınır. | 1210 durumunun<br>1215, 1220, 1230<br>ya da 1300 durumuna dönmesi<br>**beklenmelidir.** **(2 gün)** |
| 1215 | DOKÜMAN GÖNDERİMİ<br>BAŞARISIZ. TEKRAR GÖNDERME SONLANDI | Gönderim sırasında bir hata oluşması halinde zarf 1210 durum kodunun alındığı andan itibaren Merkez birim aynı zarfı dört defa ikişer saat arayla toplam sekiz saat içerisinde tekrar göndermeyi dener. Son denemede (dördüncü deneme) zarf hala karşı tarafa başarıyla iletilememiş ise zarfın durumu 1215 "DOKÜMAN GÖNDERİMİ BAŞARISIZ. TEKRAR GÖNDERME SONLANDI"<br>durum kodunu alır. 1215 durum kodunun alınmasının ardından ilgili zarftaki faturalar aynı Fatura ID' si ile tekrar gönderilebilecektir. | - | - | Faturalar yeniden gönderilmeli.<br>(faturanın aynı ETTN ile tekrar gönderimine izin verilir.) |
| \*1220 | HEDEFTEN SİSTEM YANITI GELMEDİ | Zarf merkezde işlendikten sonra alıcıya gönderilir, eğer **gönderim** **başarılı** olmuş ise; alıcıdan merkeze sistem yanıtı gelene kadar zarfın merkezdeki durumu 1220 "HEDEFTEN SİSTEM YANITI GELMEDİ " şeklinde olur<br>ve buna göre faturanın ERP statüsü de "Alıcıya gönderildi" olmaktadır. | 1220 "HEDEFTEN SISTEM YANITI GELMEDI" durum<br>kodunda alıcı zarfı sistemine aldığını GİB'e bildirmiş ancak zarfı sorunsuzca işleyip işleyemediğine dair olumlu ya da olumsuz bir cevap dönmemiştir. | Bu durumda GİB yanıt dönmeyen mükelleflere otomatik uyarı maili atar. Ancak alıcı ile iletişime geçilerek yanıt dönmeleri sağlanabilir. Bu durumdaki zarfların içerisindeki faturaların tekrar gönderilmesi mükerrer gönderim<br>olacağından ikinci kez **gönderilmemesi**<br>gerekmektedir | 1220 durumunun<br>1230 ve ya 1300 durumuna dönmesi **beklenmelidir.**<br>İki gün<br>içerisinde durum kodu güncellenmez ise; bu konuda alıcı ile görüşülebilir. |
| 1230 | HEDEFTEN SİSTEM YANITI BAŞARISIZ GELDİ | Zarfın başarısız işlendiğine dair bir kod dönülmesi halinde Merkezde 1220 durum koduyla bekleyen zarfın yeni durumu 1230 "HEDEFTEN SİSTEM YANITI<br>BAŞARISIZ GELDİ" olur. 1230 durum kodunun alınmasının ardından ilgili zarftaki faturalar aynı Fatura ID' si ile tekrar gönderilebilecektir. Bu nedenle fatura iptal süreçleri başlatılmaz. Gönderici birim merkeze sorgu gönderdiğinde faturanın ERP statüsü de "Alıcıda işlenemedi" olur. | - | - | Faturalar yeniden gönderilmeli.<br>(faturanın aynı ETTN ile tekrar gönderimine izin verilir.) |
| \*1300 | BAŞARIYLA TAMAMLANDI | Hedeften sistem yanıtının 1200 "ZARF BAŞARIYLA İŞLENDİ" durum kodu ile gelmesi halinde Merkezde 1220 durum koduyla bekleyen zarfın yeni durumu 1300 "BAŞARIYLA TAMAMLANDI" olur. Buna göre de gönderici birim, merkeze sorgu gönderdiğinde faturanın ERP statüsü "Alıcıda işlendi – Başarıyla işlendi" hale gelir. | - | - | - |

**Faturaların** **yeniden** **gönderilme** **aşamaları:**

- Kodların başında "\*" işareti var ise;

İlgili durum kodları alındığında, satış faturasının aynı ETTN ile gönderimine izin **verilmez.** e-Fatura uygulaması normal işleyişinde bu faturaların tekrar gönderimine gerek **duyulmamaktadır**.

- Kodların başında "\*" işareti yok ise;

İlgili durum kodları alındığında, satış faturasının aynı ETTN ile tekrar gönderimine izin **verilir.**

-
  - İlgili zarfın üzerinde zarf sil işlemi yapılır
  - Toplu efatura oluşturma ekranında taslaklar sekmesine gelen fatura taslaklardan silinir.
- Satış faturası üst bilgiler ekranından satış faturası silinir.
- Kaydedilen yeni satış faturası gönderilir.

- \*\*1163 Durum kodunun alınmasının sebepleri;
- İlgili zarf içerisindeki faturanın daha önce gönderilmiş olup durum kodunu almadan silinip tekrar gönderim yapılmış olabilir.
- İlgili zarf içerisinde birden fazla efatura olması durumunda bunların sadece bir tanesi bile daha önce gönderildi ise aynı durum kodunu alır.

1163 durumundaki zarflarınız için şu işlemleri yapabilirsiniz. (online e-Fatura kullanılması durumunda)

- 1163 durum kodundaki zarflar, sağ klik \> zarf sil ile silinir. (Eğer zarf içerisinde birden fazla fatura var ise; efaturaları tek tek zarflayıp gönderim yapıp, içerisindeki hangi faturanın 1163 durum kodunu aldığını tespit edebilirsiniz. Bu şekilde diğer faturalarınız da karşı tarafa başarılı bir şekilde ulaşacaktır. Sonrasında tekrar 1163 durum kodunu alan zarfı silip aşağıdaki adımları uygulayabilirsiniz)
- Fatura numarası ve tarihi ile efatura parametrelerinde gelen/giden dizinindeki giden klasörünün içerisinde fiziki olarak giden ilk zarf bulunmalıdır.
- e-Fatura giden kutusu zarf bazında açılarak zarf yükle butonu ile gönderdiğiniz ilk zarf yüklenmelidir. Sonrasında tekrar sorgula yapabilirsiniz.

1163 durumundaki zarflarınız için şu işlemleri yapabilirsiniz. (entegratör kullanılması durumunda)

- 1163 durum kodundaki zarflar, sağ klik \> zarf sil ile silinir.
- Entegratör içerisinde zarf bazında 1300 durum kodlu zarf bulunup indirilir.
- Efaturaaktarım.exe uygulaması ile ilgili zarfı içeriye alabilirsiniz. (Efaturaaktarım.exe uygulamasını [netsisdestek@logo.com.tr](mailto:netsisdestek@logo.com.tr)adresine mail atarak temin edebilirsiniz.
