---
title: "Döviz Çevrim"
page_id: "24740609"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Muhasebe"
  - "Muhasebe Modülü"
  - "İşlemler / Muhasebe"
  - "Döviz Çevrim"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / İşlemler / Muhasebe / Döviz Çevrim"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTE1MWIzMDVhLTc1MmItNGI1ZS04MTFhLTBiMGY5ZDZlNmQ1NSZsaW5rPTVkZGM5NTk1LTliMzAtNGFlOC1iMGE2LTFmNTU4ZTIwMzQ1NSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=151b305a-752b-4b5e-811a-0b0f9d6e6d55&link=5ddc9595-9b30-4ae8-b0a6-1f558e203455&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "doviz-cevrim_41157558_24740609.html"
source_version: "2022-10-06T12:12:02.220+03:00"
source_bytes: 28362
fetched_at: "2026-09-13T04:13:22+00:00"
generator: "netsis-scraper 1.0.0"
---
# Döviz Çevrim

Döviz Çevrim, Muhasebe Bölümünde, "İşlemler/Muhasebe Modülü" menüsünün altında yer alır.

Döviz Çevrim bölümünün enflasyon muhasebesi ile ilgili kullanımı hakkında detaylı bilgi için; Muhasebe → Ekler → [Ek-1 Enflasyon Muhasebesi](<../Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/index.md>) dokümanına bakılabilir.

Döviz Çevrim, muhasebe yevmiye fiş kayıtlarının döviz değeri üzerinden takip edilmesi için kullanılan bölümdür. İşlem sırasında, yevmiye fişlerinde yer alan evrak tarihine göre, yevmiye fişlerinin "Tutar" alanındaki TL tutarların (Döviz Takibi modülünden girilen günlük kur değerleri baz alınarak) satır bazında döviz değerleri oluşturulur. Döviz değerleri, yevmiye fişlerinin firma döviz alanlarında oluşur. Döviz Çevrim işleminin güvenli bir şekilde yapılması için “Döviz Takip Modülünde” günlük kurların düzenli girilmesi gerekir. İşlemin çalıştırılıp değerlerin oluşturulması durumunda, yevmiye kayıtlarının hem TL hem de (belirlenen döviz tipine göre) döviz bazında görülmesi sağlanır.

![](../../../../_assets/dbec54de6dcfc5e0160a.png)

Döviz Çevrim ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Döviz Çevrim Ekranı |  |
| --- | --- |
| Yıl Kodu | İşlemin çalıştırılacağı yılın izlendiği alandır. |
| Ay Kodu Aralığı | Firma döviz tutarları oluşturulacak ay aralığının girildiği alandır. Her iki ay koduna aynı ay kodu girildiğinde, sadece girilen ay için firma döviz tutarları oluşturulur. |
| Firma Döviz Tipi | Yardımcı Programlar → Kayıt → [Şirket Şube Parametre Tanımları](<../../../Genel/Yardımcı Programlar/Kayıt - Yardımcı Programlar/Şirket - Şube - Parametre Tanımları.md>) → "Döviz Tipi" alanında girilen değerin otomatik olarak aktarıldığı alandır. Üzerinde değişiklik yapılamaz. Firma döviz tutarları, bu alanda izlenen döviz tipi bazında oluşturulur. Farklı döviz tipleri bazında firma döviz tutarlarının oluşturulması için, Yardımcı Programlar → Kayıt → [Şirket Şube Parametre Tanımları](<../../../Genel/Yardımcı Programlar/Kayıt - Yardımcı Programlar/Şirket - Şube - Parametre Tanımları.md>) → "Döviz Tipi" alanının değiştirilmesi gerekir. |
| Çevrim Türü | Yardımcı Programlar → Kayıt → [Şirket Şube Parametre Tanımları](<../../../Genel/Yardımcı Programlar/Kayıt - Yardımcı Programlar/Şirket - Şube - Parametre Tanımları.md>) → "Döviz Çevrim Tipi" alanında seçilen tipin otomatik olarak aktarıldığı alandır. Üzerinde değişiklik yapılamaz. |
| Baz Tarihi | Hesap planında açılan hesapların (hesap türünde verilen tarih seçilmişse), "Baz Tarihi" alanında girilen tarihin kuru baz alınarak firma döviz tutarları oluşturulur. Diğer hesaplama türleri için baz tarihinin önemi yoktur. |
| Şubeler Dahil | Merkez işletme dışında, tanımlı tüm işletmelerde “Şubeler Dahil” sorgulaması bulunur. Ancak, merkez işletmede “İşletmeler Dahil” şeklinde sorgulanır ve işaretlenmesi halinde "Döviz Çevrim" işlemini tüm işletmeler için yapar. Yevmiye fişlerinde kullanılan hesaplar için firma döviz tutarının oluşturulması, "Hesap Planı Kayıtları" bölümündeki “Düzeltilecek Hesap” parametresine bağlıdır. Bu parametrenin işaretli olmadığı hesaplar için firma döviz tutarı hesaplanmaz. Döviz tutarları oluşturulurken, yevmiye fiş kayıtlarında aranan koşullar ve hesaplama şekli aşağıdaki şekildedir: - Fişlerdeki hesapların operasyon döviz tipleri ile hesaplanacak firma döviz tipi aynı ise; operasyon döviz tip ve tutarı, "Firma Döviz Tipi" ve "Firma Döviz Tutarı" alanlarına aktarılır. Böyle bir durumda firma döviz tutarı tekrar hesaplanmaz.<br>- Fişlerdeki hesapların, operasyon döviz tipleri ile hesaplanacak firma döviz tipi farklı ise; firma döviz tipine göre fişlerdeki evrak tarihleri baz alınarak firma döviz tutarları hesaplanır.<br>- Fişlerdeki hesapların operasyon döviz tipleri dolu, operasyon döviz tutarları boş ise; bu tür satırlarda, firma döviz tutarı hesaplamasının yapılmayacağı anlaşılır. Böyle bir durumda operasyon döviz tipi, hesaplanacak firma döviz tipi ile aynı/farklı da olsa, firma döviz tipi fişlerdeki firma döviz tipi alanına aktarılır fakat firma döviz tutarı hesaplanamaz. Örneğin, kur farkı kayıtları, (ön muhasebeden) "Operasyon Döviz Tipi" dolu, "Operasyon Döviz Tutarı" boş olarak aktarılır.<br>- Fişlerdeki hesapların, operasyon döviz tipleri ve tutarları boş ise TL tutarlarından, ilgili hesabın hesap planında belirlenen “Hesaplama Türü” baz alınarak firma döviz tutarları hesaplanır. Yukarıda anlatılan operasyon döviz tipi ve tutarının dolu fakat firma döviz tipinin operasyon dövizinden farklı olduğu durumlarda; firma döviz tutarı, parite hesaplaması kullanılarak bulunur. Yani, ilgili evrak tarihindeki her iki döviz tipinin kurları oranlanır ve bulunan pariteye göre firma döviz tutarları oluşturulur. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilgilerin onaylanarak işlemin başlatılmasını sağlayan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
