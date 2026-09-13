---
title: "Netsis Ondalık Sistemi"
page_id: "24753107"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Genel"
  - "Yardımcı Programlar"
  - "Kayıt / Yardımcı Programlar"
  - "Netsis Ondalık Sistemi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Yardımcı Programlar / Kayıt / Yardımcı Programlar / Netsis Ondalık Sistemi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWQ5MGFjNjJlLWRlOTAtNDYwOC05NDc4LTJmZjJiZmU3NDYzYiZsaW5rPTgwNGI1MjJhLWU3NjktNDRkMi05YzQ1LWNjZTM1NTRjOTI4NyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=d90ac62e-de90-4608-9478-2ff2bfe7463b&link=804b522a-e769-44d2-9c45-cce3554c9287&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-ondalik-sistemi_41170434_24753107.html"
source_version: "2022-10-04T15:08:13.243+03:00"
source_bytes: 70606
fetched_at: "2026-09-13T04:17:15+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis Ondalık Sistemi

Netsis Ondalık Sistemi, Genel Bölümü'nde, "Kayıt/Yardımcı Programlar" menüsünün altında yer alır. Netsis Ondalık Sistemi, program genelinde Miktar, Tutar, Döviz Tutarı, Firma Döviz Tutarı, Oran, Fiyat, Kur, Döviz Fiyatı sahalarında kullanılacak ondalık hanelerinin Grup, Kullanıcı ve Modül, Program bazında ayrı ayrı tanımlanmasını sağlayan bölümdür.

![](../../../../_assets/a993ca3f248940731ceb.png)

Netsis Ondalık Sistemi ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Netsis Ondalık Sistemi Ekranı |  |
| --- | --- |
| Kısıt Kapsamı | Ondalık tanımlaması Kullanıcı, Grup veya Tüm Kullanıcılar bazında yapılabilir. Alanın sağ tarafında yer alan aşağı ok butonu ile seçim yapılır. **Kullanıcı:** Tek bir kullanıcı için tanımlama yapılır. **Grup:** "Kullanıcı İşlemleri" modülünde kayıtlı bir gruba dahil olan kullanıcılar için ondalık tanımlaması yapılır. **Tüm Kullanıcılar:** Programda kayıtlı olan tüm kullanıcılar için tanımlama yapılır. **Örneğin** Satış irsaliyelerinin, yurtiçi satış ve ihracat amaçlı kullanıldığı ve ayrı kullanıcılar tarafından kaydedildiği varsayıldığında ihracat amaçlı satış irsaliyesi kaydı yapan kullanıcının "Tutar" sahalarında ondalıklı veri girişi ihtiyacı, "Kısıt Kapsamı - Kullanıcı" seçilip ilgili kullanıcı için ondalık tanımlaması yapılarak karşılanır. Böylece, program içinde aynı menünün iki kullanıcı için ayrı çalışması sağlanır. |
| Kullanıcı Kodu | "Kısıt Kapsamı" alanında "Kullanıcı" seçeneğinin seçilmesi ile aktif hale gelen alandır. Ondalık hane tanımlaması yapılacak kullanıcı için, ilgili kullanıcının kodunun girilmesini sağlar. |
| Grup Kodu | "Kısıt Kapsamı" alanında "Grup" seçeneğinin seçilmesi ile aktif hale gelen alandır. Ondalık hane tanımlaması yapılacak kullanıcı için, ilgili kullanıcılara ait grup kodunun girilmesini sağlar. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, "Kullanıcı İşlemleri" modülünde tanımlanan grupların listesine ulaşılır. |
| Modül No | Ondalık hane tanımlaması yapılacak modül numarasının girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, tanımlama yapılacak modül numarası seçilir. Tüm modüller için ondalık hane tanımlamasına -1 değerinin girilmesi gerekir. |
| Program No | Ondalık hane tanımlaması yapılacak program numarasının girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, tanımlama yapılacak program numarası seçilir. Tüm programlar için ondalık hane tanımlamasına -1 değerinin girilmesi gerekir. Böylece, tek satırda tanımlanan ondalık haneler, belirtilen modülün veya modüllerin içinde yer alan programların hepsi için geçerli hale gelir. |
| Dövizli İşlemlerde Saha Değişimi | Döviz Fiyat, Kur ve Fiyat olmak üzere üç seçenekten oluşur. Alanın sağ tarafında bulunan aşağı ok butonu ile seçim yapılır. Netsis ondalık sisteminde dövizli değer alan sayısal alanların ondalık tanımlamalarının programda tanımlanan şekliyle uygulanması için - Döviz Fiyat 4 ondalık, Döviz Tutar 2 ondalık gibi - söz konusu üç seçenekten birinin değişmesi gerekir. **Örneğin** Değişmesi için "Kur" seçildiğinde, Döviz Fiyat ve Döviz Tutar alanlarının tanımlanan ondalık değerine ulaşması için "Kur" alanındaki değer değişir. Yani, faturada dövizli bir fiyat girilirken, girilen döviz fiyat ve tutar sabit kalır. "Kur" alanının değeri, bu alanların ondalık sayısını sağlayacak şekilde değişir. Seçim yapılan alan Fatura, Dekont gibi modüllerde "Değişim" alanlarında otomatik olarak gelir. Kullanıcı isterse değişiklik yapabilir. "Değişim" seçeneği "Fiyat" olarak seçildiğinde, Dekont modülündeki "Değişim" alanı otomatik şekilde "Fiyat" olarak ekrana gelir. |
| Ondalıklarda Sondaki Sıfırlar Gösterilsin | Ondalık tanımlaması yapılan sahalarda, sondaki sıfırların gösterilmesi için kullanılan seçenektir. İşaretlendiğinde; program genelindeki işlemler için - ondalık sisteminde modül ve programlar için ayrı ayrı tanımlama yapılabilir - tanımlanan ondalık değerleri kadar sıfır gösterilir. **Örneğin** "Satış Faturası" için bu seçenek işaretlendiği zaman, tüm ondalık değerler - miktar, tutar, dövizli tutar, firma dövizli tutar, oran, fiyat, kur, dövizli fiyat - için söz konusu seçenek geçerli hale gelir. |
| Ondalık | Miktar, Tutar, Döviz Tutar, Firma Döviz Tutar, Oran, Fiyat, Kur, Döviz Fiyat sahalarına girilmesine izin verilecek ondalık hane adedinin tanımlandığı alandır. **Örneğin** Miktar alanına 0 değeri girilmesi halinde, ilgili modüldeki miktar hanesine ondalıklı sayı girilemez. "Miktar" alanına 2 değeri girildiği zaman programdaki miktar hanesine 2 basamak ondalık girilebilir. Ondalık tanımlanan sahalar grid alandan izlenir. Daha önceden kaydedilen ondalık tanımlamalarında değişiklik yapılması için, grid üzerindeki tanımlamaya farenin sol tuşu ile çift tıklanması gerekir. Kullanıcı tanımlamaları şube bazında yapıldığı için, ondalık tanımlamalarının da şube bazında yapılması gerekir. Yapılan ondalık tanımlamaları, kayıt ekranlarında, grid ekranlarda ve raporlarda geçerlidir. Program tarafından desteklenen ondalık hane sayısı en fazla 15’tir. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır. Netsis Ondalık Sistemi kaydının iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.

**Kullanıcı ve Grup Bazında Ondalıkta Öncelik**

Bir kullanıcı; hem kendisi, hem içinde bulunduğu grup, hem de tüm kullanıcılar için ayrı ayrı ondalık tanımlaması yapılabilir.

Kayıt sırasında geçerli olacak ondalık tanımlamaları şunlardır:

- **Kullanıcı Bazında Ondalık Tanımlama:** Tanımlamalarda verilen ondalık miktarlarının farklı olması durumunda, en detaylı olan tanımlamaya öncelik verilir. Stok - Tüm Programlar ve Stok - Stok Hareket Kayıtları için iki ayrı ondalık tanımlaması yapıldığında, Stok - Stok Hareket Kayıtları daha detaylı bir tanımlama olduğu için diğer tanıma göre önceliklidir.
- **Grup Bazında Ondalık Tanımlama:** Grup ve Kullanıcı bazında ondalık tanımlaması yapıldığı zaman öncelik, kullanıcı bazında yapılan ondalık tanımlamasındadır. Grup bazında ondalık tanımlaması yapıldığı zaman ise, kullanıcı bazında olduğu gibi en detaylı tanımlama daha önceliklidir.
- **Tüm Kullanıcılar Bazında Ondalık Tanımlama:** "Kısıt Kapsamı" alanına "Tüm Kullanıcılar", Modül ve Program alanlarına ise -1 değerinin girilmesi halinde, bir şubeye ait kullanıcıların hepsi için tüm modül ve programlarda geçerli ondalık sistemi tanımlaması yapılabilir. Ancak, Kullanıcı ve Grup bazında yapılmış bir tanımlama varsa, tüm kullanıcılar için yapılan ondalık tanımlaması üçüncü öncelikte olur.
