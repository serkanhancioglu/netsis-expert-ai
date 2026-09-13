---
title: "e-Arşiv İnternet Satış Belgeleri İçin Dizayn Örneği"
page_id: "140249558"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "e-Arşiv İnternet Satış Belgeleri İçin Dizayn Örneği"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / e-Arşiv İnternet Satış Belgeleri İçin Dizayn Örneği"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWI1NTA5YmMzLWEwNmYtNDBjZi05NzkxLTE4ZWI5ZmI0NmYyMiZsaW5rPTVkZjgwMzM5LTNlM2MtNGUzNC1iNzRjLWIyZmQwZWU1OTA2YyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=b5509bc3-a06f-40cf-9791-18eb9fb46f22&link=5df80339-3e3c-4e34-b74c-b2fd0ee5906c&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "e-arsiv-internet-satis-belgeleri-icin-dizayn-ornegi_140249558_140249558.html"
source_version: "2024-07-01T14:50:20.323+03:00"
source_bytes: 6488662
fetched_at: "2026-09-13T04:22:56+00:00"
generator: "netsis-scraper 1.0.0"
---
# e-Arşiv İnternet Satış Belgeleri İçin Dizayn Örneği

İnternet Satış tipli e-Arşiv belgeleri için hazırlanacak dizaynın tipi "**e-Arşiv** **İnternet**" olmalıdır.

![](../_assets/285a21a8fbb59999e73d.png)

Genel Bilgiler sekmesinde e-Devlet Şablon kısmında arşiv belgesi için olan xslt dosyası seçilir ve Kalem Bilgileri sekmesinde geçilir.
![](../_assets/c60a6c2664c4810102da.png)
İnternet üzerinden gerçekleştirilen satışlara ait faturalarda **internetSatisBilgi** grubuna ait elemanlara gerekli bilgilerin yazılması zorunludur. Bu grupta **WebAdresi,** **odemeSekli,** **odemeAracisiAdi,** **odemeTarihi,** **gonderiBilgileri** yer almaktadır. İnternet üzerinden gerçekleştirilen satışlara ait faturalarda bu gruba ait elemanlara gerekli bilgilerin yazılması zorunludur.

Logo Netsis ERP ürününde, internetSatisBilgi grubuna ait bilgiler, e-Arşiv İnternet tipli dizaynların içerisinde **AdditionalDocumentReference.ID,** **AdditionalDocumentReference.Issuedate** **ve** **AdditionalDocumentReference.DocumentType** tagleri kullanılarak basılabilmektedir.

- **WebAdresi:** Bu elemana alış veriş yapılan web sitesinin adresi yazılmalıdır. Bu elemana birden fazla web adresi yazılması gerektiği takdirde, her bir web adresi arası noktalı virgül ile ayrılarak yazılmalıdır.

internetSatisBilgigrubununbuelemanıiçin,dizayn kalemlerinde AdditionalDocumentReference.ID tagi, **internetSatisBilgi/webAdresi** yazısı ile eşleştirilmelidir. Bu tanım için Tip: Sql seçilerek 'internetSatisBilgi/webAdresi' yazısı sql alanına yazılır.

Satır, sütun, uzunluk bilgisi girilir. Bu tag bilgileri internetSatisBilgi grubundaki her elemanı için kullanılacağından her eleman tanımı için kayıt no bilgisi birer artırılarak ilerlenir. Kayıt No alanı 1 seçilir.

![](../_assets/f794678094d5fd67bf1b.png)

AdditionalDocumentReference.Issuedate tagi ile fiş tarihi bilgisi eşleştirilmelidir. Belge tarihi bilgisi ile eşleştirilebilir. Bu tanım için Tip:Program seçilerek Alan No:1003 (Belge Tarihi) seçilir. Satır, sütun, uzunluk bilgisi girilir ve Kayıt No alanı 1 seçilir.

![](../_assets/aecffb93092ab27069a3.png)

AdditionalDocumentReference.DocumentType tagine internet web adresi bilgisi girilmelidir. İster sql, ister alan numarası kullanılarak web adresi bilgisinin getirileceği yer seçilerek bu tag ile eşleştirilir. Bu örnekte Tip:Program, Alan No 1104 olarak seçilmiştir (Fatura Üst Bilgiler Açıklama 2 alanına girilen bilgi). Satır, sütun, uzunlık bilgisi girilir ve Kayıt No alanı 1 seçilir.

![](../_assets/0832155d474407cfc3b2.png)

- **odemeSekli:** Bu elemana ödeme şekli yazılmalıdır. Değer olarak KREDIKARTI/BANKAKARTI, EFT/HAVALE, KAPIDAODEME, ODEMEARACISI, DIGER - "Bu alana açıklama girilmelidir" değerlerini alabilir. DIGER seçildiğinde yapılan ödeme şekli mutlaka yazılmalıdır.

internetSatisBilgi grubunun bu elemanı için, dizayn içerisinde AdditionalDocumentReference.ID tagi ile **internetSatisBilgi/odemeSekli** yazısı ile eşleştirilmelidir. Bu tanım için Tip: Sql seçilerek 'internetSatisBilgi/odemeSekli' yazısı sql alanına yazılır.

Satır, sütun, uzunluk bilgisi girilir. Bu tag bilgileri internetSatisBilgi grubundaki her elemanı için kullanılacağından, her eleman tanımı için kayıt no bilgisi birer artırılarak ilerlenir. Kayıt No alanına 2 girilir.

![](../_assets/0423ca0029c477f42cec.png)

AdditionalDocumentReference.Issuedate tagi ile fiş tarihi bilgisi eşleştirilmelidir. Belge tarihi bilgisi ile eşleştirilebilir. Bu tanım için Tip:Program seçilerek Alan No:1003 (Belge Tarihi) seçilir. Satır, sütun, uzunluk bilgisi girilir ve Kayıt No alanı 2 seçilir.

![](../_assets/c0b7e30a687a00bcc572.png)

AdditionalDocumentReference.DocumentType tagine ödeme şekli bilgisi girilmelidir. İster sql, ister alan numarası kullanılarak ödeme şekli bilgisinin getirileceği yer seçilerek bu tag ile eşleştirilir. Bu örnekte Tip:Program, Alan No 1106 olarak seçilmiştir (Fatura Üst Bilgiler Açıklama 4 alanına girilen bilgi). Satır, sütun, uzunlık bilgisi girilir ve Kayıt No alanı 2 seçilir.

![](../_assets/46b0f6b8ee39ccb1ceee.png)

- **odemeAracisiAdi:** Ürün bedeli bir ödeme platformu ya da ödeme aracısı üzerinden tahsil ediliyorsa bu platformun ya da aracının adı veya unvanı yazılmalıdır.

internetSatisBilgi grubunun bu elemanı için, dizayn içerisinde AdditionalDocumentReference.ID tagi ile **internetSatisBilgi/odemeAracisiAdi** yazısı ile eşleştirilmelidir. Bu tanım için Tip: Sql seçilerek 'internetSatisBilgi/odemeAracisiAdi' yazısı sql alanına yazılır.

Satır, sütun, uzunluk bilgisi girilir. Bu tag bilgileri internetSatisBilgi grubundaki her elemanı için kullanılacağından her eleman tanımı için kayıt no bilgisi birer artırılarak ilerlenir. Kayıt No alanına 3 girilir.

![](../_assets/8813626a795ddcfad9ec.png)

AdditionalDocumentReference.Issuedate tagi ile fiş tarihi bilgisi eşleştirilmelidir. Belge tarihi bilgisi ile eşleştirilebilir. Bu tanım için Tip:Program seçilerek Alan No:1003 (Belge Tarihi) seçilir. Satır, sütun, uzunluk bilgisi girilir ve Kayıt No alanı 3 seçilir.

![](../_assets/b79a6a4284e58d8c9017.png)

AdditionalDocumentReference.DocumentType tagine ödeme aracısı adı bilgisi girilmelidir. İster sql, ister alan numarası kullanılarak ödeme aracısı adı bilgisinin getirileceği yer seçilerek bu tag ile eşleştirilir. Bu örnekte Tip:Program, Alan No 1105 olarak seçilmiştir (Fatura Üst Bilgiler Açıklama 3 alanına girilen bilgi). Satır, sütun, uzunlık bilgisi girilir ve Kayıt No alanı 3 seçilir.

![](../_assets/49aef0a713820c8cf372.png)

- **odemeTarihi:** Bu elemana ödemenin yapıldığı tarih yazılmalıdır. Ödeme türü "KAPIDAODEME" veya "DIGER" ise bu eleman seçimli, "KREDIKARTI/BANKAKARTI", "EFT/HAVALE", "ODEMEARACISI" ise, zorunludur.

internetSatisBilgi grubunun bu elemanı için, dizayn içerisinde AdditionalDocumentReference.ID tagi ile **internetSatisBilgi/odemeTarihi** yazısı eşleştirilmelidir. Bu tanım için Tip: Sql seçilerek 'internetSatisBilgi/odemeTarihi' yazısı sql alanına yazılır.

Satır, sütun, uzunluk bilgisi girilir. Bu tag bilgileri internetSatisBilgi grubundaki her elemanı için kullanılacağından her eleman tanımı için kayıt no bilgisi birer artırılarak ilerlenir. Kayıt No alanına 4 girilir.

![](../_assets/c8c4d27b4bcfa9c12227.png)

AdditionalDocumentReference.Issuedate tagi ile fiş tarihi bilgisi eşleştirilmelidir. Belge tarihi bilgisi ile eşleştirilebilir. Bu tanım için Tip:Program seçilerek Alan No:1003 (Belge Tarihi) seçilir. Satır, sütun, uzunlık bilgisi girilir ve Kayıt No alanı 4 seçilir.

![](../_assets/f39feaf8d2a9658ef4b4.png)

AdditionalDocumentReference.DocumentType tagine ile ödeme tarihi bilgisi girilmelidir. İster sql, ister alan numarası kullanılarak ödeme tarihi bilgisinin getirileceği yer seçilerek bu tag ile eşleştirilir. Bu örnekte Tip:Program, Alan No 1107 olarak seçilmiştir (Fatura Üst Bilgiler Açıklama 5 alanına girilen bilgi). Satır, sütun, uzunlık bilgisi girilir ve Kayıt No alanı 4 seçilir.

![](../_assets/9254ab6d6019ca8c9a11.png)

- **gonderiBilgileri:** Bu elemana ürünün alıcıya gönderildiği tarih ve taşıyıcı bilgileri yazılmalıdır. Ürün mükellefin kendisi tarafından alıcıya teslim ediliyorsa kendisine ait bilgiler yazılacaktır. Kargo veya Lojistik Kurumu ile taşıma yaptırılıyorsa bu kurumun bilgileri yazılmalıdır. **gonderimTarihi,** bu elemana gönderinin yapıldığı veya satışa konu hizmetin ifa edildiği tarih yazılmalıdır. **gonderiTasiyan**, Gönderi taşıyana ait bilgiler yazılmalıdır.

**gonderimTarihi** için,

internetSatisBilgi grubunun bu elemanı için, dizayn içerisinde AdditionalDocumentReference.ID tagi ile **internetSatisBilgi/gonderiBilgileri/gonderimTarihi** yazısı ile eşleştirilmelidir. Bu tanım için Tip: Sql seçilerek 'internetSatisBilgi/gonderiBilgileri/gonderimTarihi' yazısı sql alanına yazılır.

Satır, sütun, uzunluk bilgisi girilir. Bu tag bilgileri internetSatisBilgi grubundaki her elemanı için kullanılacağından her eleman tanımı için kayıt no bilgisi birer artırılarak ilerlenir. Kayıt No alanına 5 girilir.

![](../_assets/d9652ebe96852c6ebfad.png)

AdditionalDocumentReference.Issuedate tagi ile fiş tarihi bilgisi eşleştirilmelidir. Belge tarihi bilgisi ile eşleştirilebilir. Bu tanım için Tip:Program seçilerek Alan No:1003 (Belge Tarihi) seçilir. Satır, sütun, uzunluk bilgisi girilir ve Kayıt No alanı 5 seçilir.

![](../_assets/643f9b957e2106b458d4.png)

AdditionalDocumentReference.DocumentType tagine ile gönderi tarihi bilgisi girilmelidir. İster sql, ister alan numarası kullanılarak gönderi tarihi bilgisinin getirileceği yer seçilerek bu tag ile eşleştirilir. Bu örnekte Tip:Program, Alan No 1003 olarak seçilmiştir (belge tarihi). Satır, sütun, uzunlık bilgisi girilir ve Kayıt No alanı 5 seçilir.

![](../_assets/c423bc475641cf46decc.png)
**gonderiTasiyan** elemanında Tüzel kişinin vergi kimlik numarası için,

internetSatisBilgi grubunun bu elemanı için, dizayn içerisinde AdditionalDocumentReference.ID tagi ile **internetSatisBilgi/gonderiBilgileri/gonderiTasiyan/tuzelKisi/vkn** yazısı eşleştirilmelidir. Bu tanım için Tip: Sql seçilerek '**internetSatisBilgi/gonderiBilgileri/gonderiTasiyan/tuzelKisi/vkn**' yazısı sql alanına yazılır.

Satır, sütun, uzunluk bilgisi girilir. Bu tag bilgileri internetSatisBilgi grubundaki her elemanı için kullanılacağından her eleman tanımı için kayıt no bilgisi birer artırılarak ilerlenir. Kayıt No alanına 6 girilir.

![](../_assets/3a42e8dcee7fe71a6663.png)

AdditionalDocumentReference.Issuedate tagi ile fiş tarihi bilgisi eşleştirilmelidir. Belge tarihi bilgisi ile eşleştirilebilir. Bu tanım için Tip:Program seçilerek Alan No:1003 (Belge Tarihi) seçilir. Satır, sütun, uzunluk bilgisi girilir ve Kayıt No alanı 6 seçilir.

![](../_assets/a91d104180aa4f7b9bab.png)

AdditionalDocumentReference.DocumentType tagine gönderi taşıyan tüzel kişinin vergi kimlik numarası bilgisi girilmelidir. İster sql, ister alan numarası kullanılarak gönderi taşıyan tüzel kişinin vergi kimlik numarasının getirileceği yer seçilerek bu tag ile eşleştirilir. Bu örnekte Tip:Program, Alan No 1108 olarak seçilmiştir (Fatura Üst Bilgiler Açıklama 6 alanına girilen bilgi). Satır, sütun, uzunlık bilgisi girilir ve Kayıt No alanı 6 seçilir.

![](../_assets/924fc4f94e83744a50e3.png)

**gonderiTasiyan** elemanında Tüzel kişinin ünvanı için,

internetSatisBilgi grubunun bu elemanı için, dizayn içerisinde AdditionalDocumentReference.ID tagi ile **internetSatisBilgi/gonderiBilgileri/gonderiTasiyan/tuzelKisi/unvan** yazısı eşleştirilmelidir.ButanımiçinTip:Sql seçilerek 'internetSatisBilgi/gonderiBilgileri/gonderiTasiyan/tuzelKisi/unvan' yazısı sql alanına yazılır.
Satır, sütun, uzunluk bilgisi girilir. Bu tag bilgileri internetSatisBilgi grubundaki her elemanı için kullanılacağından her eleman tanımı için kayıt no bilgisi birer artırılarak ilerlenir. Kayıt No alanına 7 girilir.

![](../_assets/e3bdd68326bec36907b4.png)

AdditionalDocumentReference.Issuedate tagi ile fiş tarihi bilgisi eşleştirilmelidir. Belge tarihi bilgisi ile eşleştirilebilir. Bu tanım için Tip:Program seçilerek Alan No:1003 (Belge Tarihi) seçilir. Satır, sütun, uzunluk bilgisi girilir ve Kayıt No alanı 7 seçilir.

![](../_assets/9b232cc9bc3c3f589187.png)

AdditionalDocumentReference.DocumentType tagine gönderi taşıyan tüzel kişinin vergi kimlik numarası bilgisi girilmelidir. İster sql, ister alan numarası kullanılarak gönderi taşıyan tüzel kişinin vergi kimlik numarasının getirileceği yer seçilerek bu tag ile eşleştirilir. Bu örnekte Tip:Program, Alan No 1109 olarak seçilmiştir (Fatura Üst Bilgiler Açıklama 7 alanına girilen bilgi). Satır, sütun, uzunlık bilgisi girilir ve Kayıt No alanı 7 seçilir.

![](../_assets/bea3ae244ef6dfa6c60a.png)

**gonderiTasiyan** elemanında Gerçek kişinin TC Kimlik numarası için, internetSatisBilgi grubunun bu elemanı için, dizayn içerisinde AdditionalDocumentReference.ID tagiile **internetSatisBilgi/gonderiBilgileri/gonderiTasiyan/gercekKisi/tckn** yazısı eşleştirilmelidir. ButanımiçinTip:Sql seçilerek 'internetSatisBilgi/gonderiBilgileri/gonderiTasiyan/gercekKisi/tckn' yazısı sql alanına yazılır.

Satır, sütun, uzunluk bilgisi girilir. Bu tag bilgileri internetSatisBilgi grubundaki her elemanı için kullanılacağından her eleman tanımı için kayıt no bilgisi birer artırılarak ilerlenir. Kayıt No alanına 8 girilir.

![](../_assets/b63efad9e1aa18d1de7e.png)

AdditionalDocumentReference.Issuedate tagi ile fiş tarihi bilgisi eşleştirilmelidir. Belge tarihi bilgisi ile eşleştirilebilir. Bu tanım için Tip:Program seçilerek Alan No:1003 (Belge Tarihi) seçilir. Satır, sütun, uzunluk bilgisi girilir ve Kayıt No alanı 8 seçilir.

![](../_assets/1a8310280b9e98414896.png)

AdditionalDocumentReference.DocumentType tagine gönderi taşıyan tüzel kişinin vergi kimlik numarası bilgisi girilmelidir. İster sql, ister alan numarası kullanılarak gönderi taşıyan tüzel kişinin vergi kimlik numarasının getirileceği yer seçilerek bu tag ile eşleştirilir. Bu örnekte Tip:Program, Alan No 1110 olarak seçilmiştir (Fatura Üst Bilgiler Açıklama 8 alanına girilen bilgi). Satır, sütun, uzunlık bilgisi girilir ve Kayıt No alanı 8 seçilir.

![](../_assets/4229dcff833bb48b24c7.png)

**gonderiTasiyan** elemanında Gerçek kişinin adı soyadı için,

internetSatisBilgi grubunun bu elemanı için, dizayn içerisinde AdditionalDocumentReference.ID tagi ile **internetSatisBilgi/gonderiBilgileri/gonderiTasiyan/gercekKisi/adiSoyadi** yazısı eşleştirilmelidir.ButanımiçinTip:Sql seçilerek 'internetSatisBilgi/gonderiBilgileri/gonderiTasiyan/gercekKisi/adiSoyadi' yazısı sql alanına yazılır.

Satır, sütun, uzunluk bilgisi girilir. Bu tag bilgileri internetSatisBilgi grubundaki her elemanı için kullanılacağından her eleman tanımı için kayıt no bilgisi birer artırılarak ilerlenir. Kayıt No alanına 9 girilir.

![](../_assets/aace0fc6032b4bdb8e5a.png)

AdditionalDocumentReference.Issuedate tagi ile fiş tarihi bilgisi eşleştirilmelidir. Belge tarihi bilgisi ile eşleştirilebilir. Bu tanım için Tip:Program seçilerek Alan No:1003 (Belge Tarihi) seçilir. Satır, sütun, uzunluk bilgisi girilir ve Kayıt No alanı 9 seçilir.

![](../_assets/673ef761fb3c95340a19.png)

AdditionalDocumentReference.DocumentType tagine gönderi taşıyan tüzel kişinin vergi kimlik numarası bilgisi girilmelidir. İster sql, ister alan numarası kullanılarak gönderi taşıyan tüzel kişinin vergi kimlik numarasının getirileceği yer seçilerek bu tag ile eşleştirilir. Bu örnekte Tip:Program, Alan No 1368 olarak seçilmiştir (Fatura Üst Bilgiler Açıklama 9 alanına girilen bilgi). Satır, sütun, uzunlık bilgisi girilir ve Kayıt No alanı 9 seçilir.

![](../_assets/d8fd83a27b439c9393bf.png)

Girilen örnek e-Arşiv Fatura örneği

![](../_assets/317a0d6d78b6f1c6c07d.png)

Oluşan İnternet Satış tipli e-Arşiv faturası örneği

![](../_assets/c6b151da8bd0f60a98ae.png)
