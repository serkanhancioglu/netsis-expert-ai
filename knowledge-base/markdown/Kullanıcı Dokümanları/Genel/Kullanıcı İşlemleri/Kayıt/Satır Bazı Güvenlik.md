---
title: "Satır Bazı Güvenlik"
page_id: "47074999"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Genel"
  - "Kullanıcı İşlemleri"
  - "Kayıt"
  - "Satır Bazı Güvenlik"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Kullanıcı İşlemleri / Kayıt / Satır Bazı Güvenlik"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTMzY2RiZWIzLTc2NmEtNGU2Ny1iYWEzLTQ0OTQwY2Q0MDBhMiZsaW5rPTI2OTA5MGI0LTc2MTYtNDI0YS1iYTFiLWZiNWY4MmZjNWIwZCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=33cdbeb3-766a-4e67-baa3-44940cd400a2&link=269090b4-7616-424a-ba1b-fb5f82fc5b0d&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "satir-bazi-guvenlik_47075000_47074999.html"
source_version: "2022-12-01T14:51:40.130+03:00"
source_bytes: 97193
fetched_at: "2026-09-13T04:17:46+00:00"
generator: "netsis-scraper 1.0.0"
---
# Satır Bazı Güvenlik

Satır Bazı Güvenlik, Genel Bölümü'nde Kayıt/Kullanıcı İşlemleri menüsünün altında yer alır. "Tüm Kullanıcılar", "Grup" ya da tek bir "Kullanıcı" için satır bazında kısıtlama verilen bölümdür. Böylece; "Satır Bazı Güvenlik Uygulaması" ile bir kullanıcı veya kullanıcı grubunun programda tanımlanan bir alana, verilen kısıda uygun olmayan kayıtları girmesi engellenir. "Satır Bazı Güvenlik Uygulaması" ile kısıtlama yapılan kullanıcı yada kullanıcı grubunun kısıt kapsamındaki alanlara sahip kayıtları görmemesi de sağlanır.

Bu bölüm, Yardımcı Programlar → [Şirket-Şube Parametre Tanımları](<../../Yardımcı Programlar/Kayıt - Yardımcı Programlar/Şirket - Şube - Parametre Tanımları.md>) → Parametreler → “Satır Bazı Güvenlik Sistemi” veya “Hepsi” seçeneğinin işaretlenmesi ile aktif hale gelir.

Satır Bazı Güvenlik Uygulaması; veritabanı olarak hem Oracle hem de MsSQL'de - MsSQL 2016 ve üzeri versiyonunun kullanılması koşulu ile - desteklenir.

![](../../../../_assets/bdcf48fba60f0ba912be.png)

Satır Bazı Güvenlik Düzenleme ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Satır Bazı Güvenlik Düzenleme Ekranı |  |
| --- | --- |
| Kısıt Kapsamı | Kısıt kapsamına girecek seçeneğin belirlendiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile seçim yapılır. Tüm Kullanıcılar, Grup ve Kullanıcı seçeneklerinden oluşur. |
| Kullanıcı Kodu | "Kısıt Kapsamı" alanında "Kullanıcılar" seçeneğinin seçilmesi ile aktif hale gelen alandır. Satır bazı güvenlik düzenlemesi yapılacak kullanıcı kodunun girilmesini sağlar. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, kullanıcı kodları arasından seçim yapılır. |
| Grup Kodu | "Kısıt Kapsamı" alanında "Grup" seçeneğinin seçilmesi ile aktif hale gelen alandır. Satır bazı güvenlik düzenlemesi yapılacak grup kodunun girilmesini sağlar. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, grup kodları arasından seçim yapılır. > [!NOTE]<br>> "Kullanıcı Grup Kayıtları" bölümünde tanımlanan ve seçilen gruba ait kullanıcılar için geçerlidir. |
| Veritabanı Nesnesi | Satır bazı kısıtlamasının yapılacağı tablonun seçildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile tablo seçenekleri arasından seçim yapılır. **Örneğin;** "Stok Kartı Kayıtları" bölümündeki bir alan için kısıtlama yapılacaksa TBLSTSABIT seçeneğinin seçilmesi gerekir. "Veritabanı Nesnesi" altındaki boş alanda ise kısıtlamanın hangi alan için yapılacağına dair SQL cümlesi yazılır. **Örneğin;** Satır bazı kısıtlaması bir kullanıcı grubu için, "Cari Hesap Kayıtları" bölümünde "Grup Kodu" alanı için yapılması istendiğinde, "Veritabanı Nesnesi" alanından TBLCABIT seçeneğinin seçilmesi gerekir. "Veritabanı Nesnesi" altındaki boş alanda GRUP_KODU\<\>’OZEL’ şeklinde bir tanımlama yapılması gerekir. Tanımlaması yapılan kullanıcı grubu, "Cari Hesap Kayıtları"bölümünde "Grup Kodu" OZEL olan cari hesapları göremez. Ayrıca, bu kullanıcı grubu yeni bir cari hesap tanımlaması yaparken ya da bir cari hesapta düzeltme yaparken, ilgili hesabın "Grup Kodu" alanına ‘OZEL’ grup kodunu veremez. İlgili kullanıcı grubu, verilen kısıtlamaya aykırı bir işlem yaparsa (Cari hesap tanımlaması yaparken "Grup Kodu" alanına OZEL girmeye çalışırsa) “Satır bazında güvenlik kısıtlamalarına uygun kayıt girmelisiniz” şeklinde bir uyarı ekrana gelir ve kullanıcı grubunun kısıtlamaya aykırı bir kayıt girmesine izin verilmez. |
| ![](../../../../_assets/cb9a8c2a8d6dc86d66d2.png) Tablo Sahaları | "Veritabanı Nesnesi" alanında seçilen tabloya ait sahaların izlenmesi için kullanılan butondur. Böylece, kısıt verilecek tablonun saha isimlerine bu ekrandan bakılabilir. ![](../../../../_assets/f4bb05205bbb8fb0d7d2.png) |
| ![](../../../../_assets/3674465223b5a1cc198a.png) Tüm Tabloları Kontrol Et | Bu alan ile "Satır Bazı Güvenlik" uygulamasında verilen kısıtlar sonucu oluşan nesnelerde sorun yaşanması durumunda, bu nesnelerin tekrar oluşturulması için kullanılan butondur. Butona basılması ile uyarı ekranı görüntülenir ve ekranın onaylanması ile işlem başlatılır. Bu işlem yapılırken güvenlik nedeniyle diğer kullanıcıların programdan çıkmaları gerekir. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır.

Yapılan kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
