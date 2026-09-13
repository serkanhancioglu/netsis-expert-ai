---
title: "Dağıtım Tablosu"
page_id: "24740624"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Muhasebe"
  - "Muhasebe Modülü"
  - "İşlemler / Muhasebe"
  - "Yardımcı Servis Dağıtım İşlemleri"
  - "Dağıtım Tablosu"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / İşlemler / Muhasebe / Yardımcı Servis Dağıtım İşlemleri / Dağıtım Tablosu"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWVjMTM3ODcwLTg2MTItNGFkYi05ZDYzLWNjZGEzMmI4ZDIzMiZsaW5rPWZkOWRjOWI0LTQ2YTktNDA4NC1iNTE5LTNhYjExMTgwOTk3OSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=ec137870-8612-4adb-9d63-ccda32b8d232&link=fd9dc9b4-46a9-4084-b519-3ab111809979&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "dagitim-tablosu_41157600_24740624.html"
source_version: "2022-10-06T12:40:39.483+03:00"
source_bytes: 59420
fetched_at: "2026-09-13T04:13:26+00:00"
generator: "netsis-scraper 1.0.0"
---
# Dağıtım Tablosu

Dağıtım Tablosu, Muhasebe Bölümünde, "İşlemler/Muhasebe Modülü" menüsünün altında yer alır. Dağıtım Tablosu, dağıtımı yapılacak ve aktarılacak hesapların tanımlanmasını sağlayan bölümdür.

![](../../../../../_assets/ff60a10dc3b37f89ac14.png)

Dağıtım Tablosu ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Dağıtım Tablosu Ekranı |  |
| --- | --- |
| İşlem Sıra No | Girilen dağıtım tablo kaydına, kullanıcı tarafından en fazla 10 karakter uzunluğunda, sadece sayısal bir değerin girildiği alandır. Her dağıtım kaydı için bir işlem sıra numarası tanımlanması gerekir. Birden fazla aynı işlem sıra numarası kullanılamaz. |
| Fiş No | Farklı işlem sıra numarası ile girilen dağıtım kayıtlarının aynı dağıtım fişine yazılmasını sağlamak için numara girilen alandır. Aynı fişe yazılacak dağıtım işlemleri için kullanılan fiş numarası, birden fazla işlem sıra numarasında kullanılabilir. Böylece, dağıtım fişi oluşturulurken aynı fiş numarasına ait dağıtım işlemleri kümüle edilerek aynı fişe aktarılır. |
| Kaynak Kodu | Dağıtımı yapılacak hesap kodunun girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile; ana, grup ya da muavin kodu girilir. Ana hesap girildiğinde ana hesabın, grup hesap girildiğinde grup hesabın, muavin hesap girildiğinde ise muavin hesabın borç/alacak bakiyesi, "Dağıtım Kodu" alanında girilen hesaba aktarılır. Tanımlanan hesapların borç/alacak bakiyesi vermesi gerekir. Alacak ya da borç bakiyesi olmayan hesaplarda, "Dağıtım Fişi Oluşturma" işlemi kesilir. |
| Kaynak Referans Kodu | Muhasebe → Kayıt → [Muhasebe Parametreleri](<../../Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/Muhasebe Modülü Tanımlamaları/Muhasebe Parametreleri - Muhasebe.md>) → “Fişlerde Referans Kodu Sorulsun” parametresinin işaretlenmesi ile aktif hale gelen alandır. Referans kodu uygulaması olan ve işlemlerinde referans kodu kullanan firmalar için, "Kaynak Kodu" alanında girilen koda ait, hangi referans koduyla girilmiş kayıtların dağıtılacağı belirlenir. Herhangi bir referans kodu girildiğinde, ilgili kaynak koduna ait bu referansa sahip borç veya alacak bakiyeleri dağıtılır. Boş bırakılmaz. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, referans kodları arasından seçim yapılır. |
| Kaynak Proje Kodu | Yardımcı Programlar → Kayıt → [Şirket-Şube Parametre Tanımları](<../../../../Genel/Yardımcı Programlar/Kayıt - Yardımcı Programlar/Şirket - Şube - Parametre Tanımları.md>) → "Proje Uygulaması Var" parametresinin işaretlenmesi ile aktif hale gelen alandır. Proje kodu uygulaması olan ve gider yerlerine ait kayıtlarda proje kodu kullanan firmalar için, "Kaynak Kodu" alanında girilen koda ait, hangi proje kodu ile girilmiş kayıtların dağıtılacağı belirlenir. Herhangi bir proje kodu girildiğinde, ilgili kaynak koduna ait yevmiye fiş kayıtlarında bu proje koduyla kaydedilen hareketlerin tutarları dağıtılır. bakiyeleri dağıtılır. Boş bırakılmaz. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, proje kodları arasından seçim yapılır. |
| Dağıtım Kodu | "Kaynak Kodu" alanında girilen hesabın borç veya alacak bakiyesinin transfer edileceği hesabın girildiği alandır. "Dağıtım Fişi Oluşturma" bölümü ile, kaynak kodunda girilen hesabın borç veya alacak bakiye tutarı, "Oran" alanında girilen değer ile hesaplanarak, bu alanda girilen hesaba borç/alacak kaydı oluşturulur. "Dağıtım Kodu" sadece muavin hesap kodu girişi yapılır. Aynı kaynak kodu için birden fazla dağıtım kodu tanımlanabilir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılır. |
| Dağıtım Referans Kodu | Muhasebe → Kayıt → [Muhasebe Parametreleri](<../../Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/Muhasebe Modülü Tanımlamaları/Muhasebe Parametreleri - Muhasebe.md>) → “Fişlerde Referans Kodu Sorulsun” parametresinin işaretlenmesi ile aktif hale gelen alandır. Gider yerlerine ait kayıtlarda referans kodunun kullanıldığı durumlarda, referans koduna göre dağıtım tablosu girişi ve dağıtım işlemleri için referans kodu girilmesi gerekir. Girilen referans kodu, fişlerde dağıtım hesaplarına işlenecek olan referans kodudur. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile referans kodları arasından seçim yapılır. |
| Dağıtım Proje Kodu | Yardımcı Programlar → Kayıt → [Şirket-Şube Parametre Tanımları](<../../../../Genel/Yardımcı Programlar/Kayıt - Yardımcı Programlar/Şirket - Şube - Parametre Tanımları.md>) → "Proje Uygulaması Var" parametresinin işaretlenmesi ile aktif hale gelen alandır. Gider yerlerine ait kayıtlarda proje kodunun kullanıldığı durumlarda, proje koduna göre dağıtım tablosu girişi ve dağıtım işlemleri için proje kodu girilmesi gerekir. Girilen proje kodu, fişlerde dağıtım hesaplarına işlenecek olan proje kodudur. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, proje kodları arasından seçim yapılır. |
| Oran | "Kaynak Kodu" alanında girilen hesabın, yüzde bazında dağıtımının yapılması için sayısal olarak oran bilgisi girilen alandır. Girilen oran bilgileri aynı kaynak koduna göre toplanarak kullanıcıyı bilgilendirir. Girilen kaynak koduna ait borç veya alacak bakiye yekununun tümü tek bir muavine aktarılacak ise, "Oran" alanına 100 değerinin girilmesi gerekir. Kaynak koduna göre oran bazında girilen bilgilerin listesi, "Kaynak Oran/Miktar Denetim Listesi" bölümünden alınabilir. **Örneğin** 800 ana hesabın 010 referans koduna ait bakiye tutarının % 20’si 730-1010 hesaba 010 referans kodu ile, % 80’i 730-1012 hesaba 012 referans koduna aktarılmak üzere oranlandığı varsayıldığında; her iki dağıtım işleminde de aynı fiş numarasının verildiğini düşünelim. Bu durumda program, yevmiye fişlerini dolaşarak 800 ana hesabına ait kayıtlarda, referans kodu 010 olanların bakiyesini kontrol eder. Bu hesaplar borç bakiyesi veriyorsa, bunun %20'si bulunarak 730-1010 hesaba 011 referans koduyla, %80’i bulunarak 730-1012 hesaba 012 referans koduyla alacak olarak aktarılır. 800 hesapta bulunan borç bakiyesinin 100.000.000 TL olduğu varsayıldığında, yansıtma işlemi aşağıdaki şekilde oluşur. 100.000.000\*20/100=20.000.000 TL 730-1010 numaralı hesaba, 100.000.000\*80/100=80.000.000 TL ise 730-1012 numaralı hesaba aktarılır. |
| Alacak Kodu | "Dağıtım Kodu" alanında girilen hesaba aktarılan borç veya alacak tutarının karşı hesabını oluşturacak hesabın (alacak veya borç tarafını oluşturacak hesabın) kodunun girildiği alandır. Bu alana sadece muavin hesap kodu girilebilir. Program, "Dağıtım Fişi Oluşturma" bölümünde kaynak hesap borç bakiyesi veriyorsa; alacak koduna alacak, kaynak hesap alacak bakiyesi veriyorsa alacak koduna borç yazılır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile hesap kodları arasından seçim yapılır. |
| Alacak Referans Kodu | "Alacak Kodu" alanında girilen hesaba aktarılacak referans kodunun girildiği alandır. "Kaynak Referans Kodu" bölümünde girilen referans kodu otomatik olarak aktarılır. İlgili referans koduna ait bakiye tutarlarının kapatılması açısından bu şekilde bırakılması önerilir. |
| Alacak Proje Kodu | "Alacak Kodu" alanında girilen hesaba aktarılacak proje kodunun girildiği alandır. "Kaynak Referans Kodu" bölümünde girilen proje kodu otomatik olarak aktarılır. İlgili proje koduna ait bakiye tutarlarının kapatılması açısından bu şekilde bırakılması önerilir. |
| Miktar | Oransal dağıtım yapılması yerine, sabit bir tutarın dağıtım hesabına aktarılması için miktar tanımlanan alandır. |
| Açıklama | Girilen dağıtım için açıklama bilgisi girilen alandır. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır. Dağıtım Tablosu kaydının iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
