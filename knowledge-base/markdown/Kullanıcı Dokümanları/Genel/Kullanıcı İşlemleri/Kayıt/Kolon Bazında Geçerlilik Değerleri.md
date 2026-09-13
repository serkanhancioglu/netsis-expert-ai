---
title: "Kolon Bazında Geçerlilik Değerleri"
page_id: "47075019"
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
  - "Kolon Bazında Geçerlilik Değerleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Kullanıcı İşlemleri / Kayıt / Kolon Bazında Geçerlilik Değerleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTgwM2RiNGM4LWM3MDEtNDdjOC04ZmIyLWRhMzQwMzZjMTU3MCZsaW5rPTg2NDdjMzhhLTEzMmQtNGU3OC1iMDc3LWRmMTU4ZWE2N2QxNyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=803db4c8-c701-47c8-8fb2-da34036c1570&link=8647c38a-132d-4e78-b077-df158ea67d17&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "kolon-bazinda-gecerlilik-degerleri_47075032_47075019.html"
source_version: "2022-12-01T14:54:59.177+03:00"
source_bytes: 50907
fetched_at: "2026-09-13T04:17:48+00:00"
generator: "netsis-scraper 1.0.0"
---
# Kolon Bazında Geçerlilik Değerleri

Kolon Bazında Geçerlilik Değerleri, Genel Bölümü'nde Kayıt/Kullanıcı İşlemleri menüsünün altında yer alır. Kullanıcılara kolon bazında kısıtlama verilmesini sağlar. Kullanıcılar, kısıta uygun olmayan bir kayıt girmeye çalıştıkları zaman program tarafından işleme izin verilmeyerek uyarı verilir.

Kolon Bazında Geçerlilik Değerleri bölümü, veritabanının Oracle olması ve Yardımcı Programlar → [Şirket-Şube Parametre Tanımları](<../../Yardımcı Programlar/Kayıt - Yardımcı Programlar/Şirket - Şube - Parametre Tanımları.md>) → Parametreler → “Kolon Bazında Geçerlilik Sistemi” veya “Hepsi” seçeneğinin işaretlenmesi ile aktif hale gelir.

![](../../../../_assets/d0bf8e3aad0d00edd6b9.png)

Kolon Bazında Geçerlilik Değerleri ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Kolon Bazında Geçerlilik Değerleri Ekranı |  |
| --- | --- |
| Kısıt Kapsamı | Kolon bazında yapılacak kısıtlamanın geçerli olacağı kullanıcı yada kullanıcıların belirlendiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile seçim yapılır. Tüm Kullanıcılar, Grup ve Kullanıcı seçeneklerinden oluşur. |
| Kullanıcı Kodu | "Kısıt Kapsamı" alanında "Kullanıcılar" seçeneğinin seçilmesi ile aktif hale gelen alandır. Kısıt yapılacak kullanıcı kodunun girilmesini sağlar. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, kullanıcı kodları arasından seçim yapılır. |
| Grup Kodu | Kısıt Kapsamı" alanında "Grup" seçeneğinin seçilmesi ile aktif hale gelen alandır. Kısıt yapılacak grup kodunun girilmesini sağlar. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, grup kodları arasından seçim yapılır. |
| Veritabanı Nesnesi | Kolon bazı kısıtlamaların geçerli olacağı tablonun seçildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile tablo seçenekleri arasından seçim yapılır. **Örneğin;** "Stok Hareket Kayıtları" bölümündeki bir alan için kısıtlama yapılacaksa TBLSTHAR seçeneğinin seçilmesi gerekir. |
| Saha Adı | "Veritabanı Nesnesi" alanında tablo adı seçilmesi halinde, bu tablonun hangi sahasına ait kısıtlamanın raporu alınması isteniyorsa, ilgili saha adının seçildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile, ilgili saha seçilir. "Saha Adı" alanının altındaki boş alanda ise kısıtlamanın hangi alan için yapılacağına dair SQL cümlesi yazılır. |
| Silme Kontrolü | Kolon Bazı Geçerlilik uygulamasında verilen kısıta uymayan kayıtların kullanıcı tarafından silinmesinin engellenmesini sağlayan seçenektir. Kullanıcı yada kullanıcı grubunun verilen kısıta uygun olmayan kayıtları girmesine izin verilmeyeceği gibi, seçeneğin işaretlenmesi ile - kısıt kapsamı dışındaki bir kullanıcı tarafından kısıta aykırı bir kayıt girildiyse - kısıt dışı kayıtları silmesini engeller. |
| Null Kontrolü Yapılsın | Verilen kısıt için boş bırakılan kayıtların da kontrol edilmesi için kullanılan seçenektir. **Örneğin;** KDV Oranının her zaman 18 olarak girilmesi şeklinde bir kısıt verildiğinde, kullanıcı "KDV Oranı" alanını boş bıraktığında uyarı ekranı görüntülenir. |
| Aktif Mi? | Girilen kısıtlara uygun kayıt yapmayan kullanıcının uyarılması için kısıt tanımlamalarının aktif hale getirilmesini sağlayan seçenektir. |
| Hata Açıklama | Tanımlaması yapılan bir kısıtlamaya uygun olmayan kayıt girildiğinde, görüntülenmesi istenen uyarı ekranı açıklamasının girildiği alandır. **Örneğin;** Kullanıcı için, programda kayıt girerken yada düzeltme yaparken stoklarda KDV Oranı alanına sadece 18 girilmesi şeklinde bir kısıt verilmesi istendiğinde; "Kısıt Kapsamı" alanında "Kullanıcı" seçeneği seçilmeli, "Veritabanı Nesnesi" alanına "TBLSTSABIT", "Saha Adı" alanına "KDV_ORANI" şeklinde bir tanımlama yapılması gerekir. Kısıt tanımlaması yapılacak olan ekran da =18 şeklinde tanımlanması gerekir. Kullanıcılar verilen kısıtlara aykırı kayıt girdiklerinde, çıkacak uyarı ekranındaki açıklama da “KDV ORANINI 18 OLMALIDIR” şeklinde tanımlanabilir. Böylece kullanıcılar programda kayıt girerken - KDV Oranı olarak 18 rakamı dışında bir değer girmek isterlerse - uyarı ekranı görüntülenir ve kullanıcının verilen kısıta aykırı kayıt girmesine izin verilmez. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır.

Yapılan kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
