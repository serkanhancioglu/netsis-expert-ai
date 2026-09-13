---
title: "Cari Risk Girişi"
page_id: "22803578"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Cari"
  - "Kayıt / Cari"
  - "Cari Risk Girişi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Cari / Kayıt / Cari / Cari Risk Girişi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTEwYWNiOGE1LTM0MDAtNGUzNC05MGU3LTk3Yzk0ODM4MDk1MiZsaW5rPWY1Y2Y0YzlmLWZkNzAtNDdkYy04ZGEwLTI1NzdiNzkzNTU2NyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=10acb8a5-3400-4e34-90e7-97c948380952&link=f5cf4c9f-fd70-47dc-8da0-2577b7935567&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "cari-risk-girisi_28150006_22803578.html"
source_version: "2022-10-26T16:05:17.240+03:00"
source_bytes: 19599
fetched_at: "2026-09-13T04:07:29+00:00"
generator: "netsis-scraper 1.0.0"
---
# Cari Risk Girişi

Cari Risk Girişi, Finans Bölümü'nde Kayıt/Cari menüsünün altında yer alır. Cari Risk Girişi; Cari risk uygulaması ile müşteri risklerinin, satış ve/veya sipariş anında online tespit ile önlenmesi, risk oluşturan faktörlerin riske etkilerinin oranlanması, risk gruplarının tanımlanarak birden fazla müşteri için tek toplam risk hesaplanması, belge üzerinde teminat dahilindeki tutar için artı vade uygulaması gibi işlemlerin yapıldığı bölümdür.

Cari Risk Girişi ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Cari Risk Girişi Ekranı |  |
| --- | --- |
| Cari Kodu | Cari risk giriş kaydı oluşturmak için cari kod bilgisinin girildiği alandır. Risk takibi yapıldığı halde, yeni açılan cari kod bu bölümden kaydedilmezse, fatura modülünden işlem yapılması istendiğinde, program tarafından “Müşteri Risk Bilgisi Bulunamadı” uyarısı ekrana gelir ve işlem yapılamaz. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile cari kodlar arasından seçim yapılır. |
| Risk Grup Kodu | Birden fazla müşterinin toplam riskinin tek bir müşteri gibi kontrol edilmesi istendiğinde kullanılan alandır. Bazı uygulamalarda, firmalar aynı müşteri için birden fazla cari kart açabilir. Risk kontrolü yapılırken, aynı müşteriye ait tüm kartlardaki risk toplamının kontrol edilmesi istenir. Bu durumda, riskleri toplanacak cari hesaplar için ortak risk gruplarının belirlenmesi gerekir. **Örneğin:** F001 numaralı cari kartın 100.\_ ve C001 numaralı cari kartın 200.\_ riski olduğu varsayıldığında, bu müşterilerden herhangi birine işlem yapıldığı zaman toplam riskin 300.\_ olarak görülmesi için her iki cari hesaba da aynı "Risk Grup Kodu" girilir. |
| Sipariş/İrsaliye/Fatura/Sevk/Yükleme Risk Kontrolü | Riskin işlem sırasındaki kontrolünü sağlayan alanlardır. Alanların sağ tarafında yer alan aşağı ok tuşlu ile "İşlem Durdurulsun" ve "Yapılmasın" seçeneklerinden biri seçilebilir. Risk uygulaması kullanıldığı halde, bazı müşterilerde risk kontrolünün yapılması istenmediğinde üç belge için de “Yapılmasın” seçeneğinin seçilmesi gerekir. Bunun dışında risk takibi yapılan müşterilerde, hangi belgelerde risk kontrolü yapılacaksa ilgili belge için “İşlem Durdurulsun” seçeneği seçilir. Risk kontrolü yapılan belgelerde program, belgeye ilk giriş aşamasında, cari kodun verildiği sırada risk kontrolü yapar. Riskini aşmış bir müşteri için program uyarı verir ve işlem yapılmasına izin vermez. Eğer risk durumu müsaitse, belge sonunda risk tekrar kontrol edilir ve riskli değilse işleme devam edilir. |
| Risk Limiti | Bir şirketin müşterilerine herhangi bir teminatı olmadan verdiği kredi limitinin girildiği alandır. İstendiğinde sadece "Borç Bakiyesi" üzerinden de risk takibi yapılabilir. Risk takibi ile ilgili detaylı bilgi için; Fatura → Kayıt → [Satış Parametreleri](<../../../Lojistik - Satış/Fatura/Kayıt - Fatura/Satış Parametreleri.md>) → Genel 1 |
| Teminatı | Müşterinin, şirkete alınan teminat mektuplarının dışında gösterdiği ek teminatlar için kullanılan alandır. Bu bilgi elle (manuel) girilir. Müşteri teminat senedi, çeki, mektubu vs. vermişse, bu bilgilerin Cari → Kayıt → "[Alınan Teminat Mektubu Kayıtları](<Alınan Teminat Mektubu Kayıtları/index.md>)" bölümünden kaydedilmesi gerekir. Bu alana girilen teminat bilgisi ile, "Alınan Teminat Mektupları" bölümünden kaydedilen teminat tutarları toplanarak, ekranın sağ kısmındaki "teminatı" alanında izlenir. |
| Risk Oranları % Alanları | Risk/teminat kontrolünde baz alınan ve girilen bilgilerin, hangi oranlarda dikkate alınacağının belirlendiği alanlardır. **Örneğin:** "Risk limiti" alanına girilen tutarın tamamı limit olarak kabul edildiğinde, ilgili alan "100" olarak bırakılır. Eğer girilen tutarın sadece % 80’i risk limiti olarak kabul edilecekse, bu alana "80" değeri girilir. Risk hesaplanmasında dikkate alınmayacak faktörler için ilgili alanlara sıfır (0) değerinin girilmesi gerekir. |
| Cari Hareket Bakiyesi | Risk takibi uygulamasında, müşterinin anlık borç bakiyesinin tamamı, toplam riskini etkiler (Borç bakiyesi, riski %100 oranında etkiler) Cari Hareket Bakiyesi risk kalemi ile, borç bakiyesinin toplam riski belli bir oranda etkilemesi sağlanır. Bu alanda 0’dan farklı bir değer olması, bakiye kontrolünün cari hareketlerden yapılacağı anlamına gelir. Oran 0’a eşit ise anlık bakiye (cari sabit kartındaki) kontrol edilir. **Örneğin:** Cari hesabın, Cari Hareket Bakiyesinin %80’i risk hesaplamaya dahil edildiğinde, "Cari Hareket Bakiyesi" alanına "80" değeri girilir. Cari hesabın Risk limiti "1000" ve Teminatı da "200" olduğunda, Cari hesaba kesilen çek, senet, irsaliye ve sipariş tutarlarının %80’i riskine yansır. Cari harekete elle girilen 100 TL’lik bir borç hareketinin 80 TL’lik kısmı borç toplamına yansır ve cari hesabın riski -1120 TL’ye düşer. |
| İrsaliye/Sipariş/Çek/Senet/Yükleme Riski | Girilen sipariş, irsaliye, çek, senet tutarlarının riske dahil edilmesi istendiğinde kullanılan alandır. Bu alanlara girilecek riske dahil edilen tutarlar, ekranın sağ tarafındaki İrsaliye Riski, Sipariş Riski Senet/Çek Riski alanlarından izlenir. Herhangi bir oran girilmediğinde, sipariş ve irsaliyeler faturalanana kadar riske dahil edilmez. Sadece 0 (riske dahil etme), veya 100 (riske dahil et) olarak kayıt girişine izin verilir. |
| Toplam Risk Bilgileri Alanları | Riske ait detay bilgilerin bulunduğu bölümdür. Riski artırıcı değerler artı (+), azaltıcı değerler eksi (-) ile ifade edilir. |
| Borç Toplamı | Cari hesaba ait toplam borç tutarının izlendiği alandır. |
| Alacak Toplamı | Cari hesaba ait toplam alacak tutarının izlendiği alandır. |
| Borç/Alacak Bakiyesi | Cari hesaba ait toplam bakiyenin izlendiği alandır. |
| Teminatı | Teminatı alanına elle (manuel) girilen teminat tutarı ile girilen teminat mektupları toplamının izlendiği alandır. Risk kontrolünde, bu alandaki toplam bilgi dikkate alınır. |
| Senet Asıl Riski | Müşteriden alınan, (asıl borçlunun kendi olduğu) henüz ödenmemiş senetler toplamının izlendiği alandır. |
| Senet Ciro Riski | Müşteriden alınan, (asıl borçlunun kendi olmadığı) ciro ve henüz ödenmemiş senetler toplamının izlendiği alandır. |
| Çek Asıl Riski | Müşteriden alınan, (asıl borçlunun kendi olduğu) henüz ödenmemiş çekler toplamının izlendiği alandır. |
| Çek Ciro Riski | Müşteriden alınan, (asıl borçlunun kendi olmadığı) ciro ve henüz ödenmemiş senetler toplamının izlendiği alandır. Müşteri çek ve senetlerinde satıcıya ciro edilip henüz ödenmemiş olanların içinden, vadesi riskin hesaplandığı günden 2 gün önce olan senet/çekler ödenmiş gibi kabul edilip riskten düşülür. Senet/çek risklerine senet/çek oranları girilmişse, hesaplanan risk tutarı bu oran bazında hesaplanarak ekrana getirilir. |
| İrsaliye Riski | Oran bilgileri girişinde, irsaliye riskine "100" (yüz) değeri girilmişse, ilgili müşterinin faturalanmamış irsaliyelerinin toplam tutarının izlendiği alandır. Oran "0" (sıfır) girilmişse, bu alan boş gelir. |
| Sipariş Riski | Oran bilgileri girişinde, sipariş riskine "100" (yüz) değeri girilmişse, ilgili müşterinin açık siparişlerinin toplam tutarının izlendiği alandır. Oran "0" (sıfır) girilmişse bu alan boş gelir. |
| Toplam Riski | Müşterinin o anki toplam riskinin izlendiği alandır. Risk limiti ve teminatı (-) eksi, diğer riski oluşturan faktörler ise (+) artı değer alarak hesaplamaya girer. **Örneğin:** Risk Limiti = 2.000 - Teminatı = 1.000 - Borç Bakiye = 250 - Çek Asıl Riski = 100 - Çek Ciro Riski = 150 - İrsaliye Riski = 200 - ise, Toplam Risk= - (2.000. +1.000.)+ (250. +100. +150. +200.) = - 2.300 olur. Örnekteki gibi riski (-) olan müşteri, (-) olduğu değer kadar satınalma yapabilir. Yani yukarıdaki müşteriye 2.300 - tutarında belge (sipariş/irsaliye/fatura) girilebilir. Riski 0 veya (+) artı olan müşteri ise risk sınırını aştığı için satınalma yapamaz. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır. Kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
