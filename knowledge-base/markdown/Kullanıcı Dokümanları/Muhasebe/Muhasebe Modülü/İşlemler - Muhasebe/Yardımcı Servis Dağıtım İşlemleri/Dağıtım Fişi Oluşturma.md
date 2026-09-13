---
title: "Dağıtım Fişi Oluşturma"
page_id: "24740627"
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
  - "Dağıtım Fişi Oluşturma"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / İşlemler / Muhasebe / Yardımcı Servis Dağıtım İşlemleri / Dağıtım Fişi Oluşturma"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTU0YTc5Mzc2LThiMDMtNDIwNy1hN2NiLTU1NGQ1NzU5NTQ2MyZsaW5rPWMwNWVhYTY5LTQ0NGItNGEzNi05NDI4LThjN2YzOGZhNWY1YyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=54a79376-8b03-4207-a7cb-554d57595463&link=c05eaa69-444b-4a36-9428-8c7f38fa5f5c&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "dagitim-fisi-olusturma_41157672_24740627.html"
source_version: "2022-10-06T12:42:18.180+03:00"
source_bytes: 38704
fetched_at: "2026-09-13T04:13:27+00:00"
generator: "netsis-scraper 1.0.0"
---
# Dağıtım Fişi Oluşturma

Dağıtım Fişi Oluşturma, Muhasebe Bölümünde, "İşlemler/Muhasebe Modülü" menüsünün altında yer alır. Dağıtım Fişi Oluşturma, dağıtım tablosu kayıtları oluşturulduktan sonra, istenen dönemlerde yardımcı servis dağıtım fişinin oluşturulmasını sağlayan bölümdür.

![](../../../../../_assets/75382b04952162d6f9b1.png)

Dağıtım Fişi Oluşturma ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Dağıtım Fişi Oluşturma Ekranı |  |
| --- | --- |
| Fiş Tarihi | Dağıtım fişinin oluşturulması istenen tarihin; gün, ay ve yıl olarak girildiği alandır. Program, girilen ay kodunu baz alarak ilgili aydaki kaynak hesaplara ait borç veya alacak bakiyelerini dağıtır. İlgili aydan daha önceki aylarda dağıtım yapılmasa bile, sadece bu alanda girilen ay kodu için dağıtım yapılır. |
| Fiş No | Dağıtım kayıtlarının aktarılacağı yevmiye fişi için kullanıcı tarafından oluşturulan numaranın girildiği alandır. Girilen fiş numarasının, daha önce dağıtım fişi amacının dışında kullanılmaması gerekir. Bu alana girilen ama yevmiye fişlerinde halihazırda mevcut olan fiş numarası varsa program, “Fiş Mevcut Ekleme Yapılacak Mı?” uyarısı vererek onay ister. Dağıtım fişi daha önce oluşturulmuş fakat bu alanda unutulan ya da dağıtım fişine ekleme yapılması istenen işlem sıra numarasının, girilecek fişin altına eklenmesi istendiğinde “Ekleme Yapılması” için "Evet" butonuna tıklanarak onay verilmesi gerekir. Yanlış girişlerde ise onay verilmeden "Hayır" butonu ile geri dönülerek, daha önce kullanılmamış yeni bir fiş numarasının ilgili alana girilmesi gerekir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, fiş numaraları arasından seçim yapılır. |
| Başlangıç İşlem Sıra No | "Dağıtım Tablosu" bölümünden girilen işlem sıra numarası başlangıç numarasının tanımlandığı alandır. İşlem tipi ile yapılan tüm tanımlamaların aktarılması için en küçük sıra numarasının girilmesi gerekir. |
| Bitiş İşlem Sıra No | "Dağıtım Tablosu" bölümünden girilen işlem sıra numarası bitiş numarasının tanımlandığı alandır. İşlem tipi ile yapılan tüm tanımlamaların aktarılması için en büyük sıra numarasının girilmesi gerekir. Sadece bir tek dağıtım tablosu bilgisinin aktarılması için, her iki alanın başlangıç ve bitiş kodu alanlarına aynı işlem tipinin girilmesi gerekir. |
| Başlangıç Dağıtım Fiş No | "Dağıtım Tablosu" bölümünden girilen fiş numarası başlangıç numarasının tanımlandığı alandır. Fiş numarası girilerek yapılan tüm tanımlamaların aynı fişe aktarılması için en küçük fiş numarasının girilmesi gerekir. |
| Bitiş Dağıtım Fiş No | "Dağıtım Tablosu" bölümünden girilen fiş numarası bitiş numarasının tanımlandığı alandır. Fiş numarası ile yapılan tüm tanımlamaların aynı fişe aktarılması için en büyük fiş numarasının girilmesi gerekir. Sadece aynı fiş numarası ile girilmiş bir dağıtım tablosu bilgisinin aynı fişe aktarılması için, her iki alanın başlangıç ve bitiş kodu alanlarına aynı fiş numarasının girilmesi gerekir. |
| Fiş Açıklama | "Dağıtım Fişi Oluşturma" bölümü çalıştırılarak oluşturulan yevmiye fişlerinin açıklama alanlarına aktarılacak bilginin girildiği alandır. Boş bırakıldığında, yevmiye fişlerinin açıklama alanları boş kalır. |
| Dağıtım Türü | Yapılacak dağıtımın belirlendiği alandır. Oransal Dağıtım ve Miktarsal Dağıtım olmak üzere iki seçenekten oluşur. |
| Proje Kodu Kontrolü Yapılsın | "Proje Kodu" uygulaması varsa ve "Dağıtım Fişi Oluşturma" işleminde proje kodu kontrolünün yapılması istendiğinde kullanılan seçenektir. Bu bölüm çalıştırılmadan önce dağıtım tablosu kayıt girişlerinin tamamlanması gerekir. Aynı zamanda "Kaynak Kodu" alanında girilen ana, grup ya da muavin hesabın borç veya alacak bakiyesi vermesi kontrol edilir. Program borç veya alacak bakiyesi vermeyen hesapların dağıtımını yapmaz. "Dağıtım Fişi Oluşturma" bölümündeki işlemler bittiğinde "Fiş Numarası" alanında girilen numaraya, "Fiş Tarihi" alanında belirtilen tarihe ve "İşlem Tipi" ile "Fiş Numarası" alanlarında girilen numara aralığına göre yevmiye fişi program tarafından oluşturulur. İlgili fişin "Açıklama-1" alanına, hangi işlem sıra numarası aralığı çalıştırılmışsa ilgili aralık, "Açıklama-2" alanına da raporlanması için fiş adı program tarafından otomatik olarak aktarılır. Herhangi bir yanlışlık varsa, bu fişin iptal edilerek gerekli düzeltmeler yapıldıktan sonra "Dağıtım Fişi Oluşturma" bölümü tekrar çalıştırılır. |
| Kümüle Bakiye Kontrolü Yapılsın | Dağıtım fişi oluşturulurken kümüle bakiye kontrolünün yapılması için kullanılan seçenektir. |
| ![](../../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilginin onaylanmasını sağlayan butondur. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgiden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
