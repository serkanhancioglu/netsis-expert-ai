---
title: "Rehber"
page_id: "50682908"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "NDI - (Netsis Data Inspector)"
  - "İşlemler / NDI"
  - "XML Dışarı Aktar - İçeri Yükle"
  - "Rehber"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / NDI - (Netsis Data Inspector) / İşlemler / NDI / XML Dışarı Aktar - İçeri Yükle / Rehber"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWViMGQyMTA3LTY4MWUtNGZmMi1iYmNhLTBlZGJkOThmY2Q5MyZsaW5rPTdiNjA4ODQ0LWU0YzAtNDc4OC05MWU4LTQxYTg0NTkzMDRjYSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=eb0d2107-681e-4ff2-bbca-0edbd98fcd93&link=7b608844-e4c0-4788-91e8-41a8459304ca&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "rehber_50682915_50682908.html"
source_version: "2022-09-16T11:13:29.087+03:00"
source_bytes: 9226
fetched_at: "2026-09-13T04:20:55+00:00"
generator: "netsis-scraper 1.0.0"
---
# Rehber

Rehber XML Dışarı Aktar/İçeri Yükle Ekranı; Rehber XML Dışarı Aktar ve Rehber XML İçeri Yükle olmak üzere iki sekmeden oluşur.

**Rehber XML Dışarı Aktar**

Rehber XML Dışarı Aktar sekmesi, NDI uygulamasında hazırlanan bir rehberin dış ortama XML formatında aktarılması için kullanılan sekmedir.

Rehber XML Dışarı Aktar ekranında yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| Rehber XML Dışarı Aktar/İçeri Yükle Ekranı |  |
| --- | --- |
| Dosya Adı | Aktarılması istenen fiziksel dosya ismi olup, rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, klasör ve dosya isminin belirlendiği alandır. |
| Kullanıcı Tanım | Kullanıcı Tanımları'nın aktarılması, aktarılan bu nesnenin yüklenmesi sırasında, karşı taraftaki NDI uygulamasında bulunan tüm kullanıcılara bu nesne ile ilgili tüm hakların verileceği anlamına gelir. Kullanıcı Tanımları aktarılmamışsa, nesnenin yüklenmesi sırasında karşı taraftaki NDI uygulamasında herhangi bir kullanıcı hakkı tanımlanmayacak ve kullanıcılar yüklenen bu nesneyi göremeyecekler. Kullanıcı haklarının yükleme sonrası ayrıca yapılması gerekir. |
| Veritabanı Bağlantı Bilgisi | Veritabanı bağlantı bilgisinin de nesneyle birlikte transfer edilip edilmeyeceğini belirlemek için kullanılan seçenektir. Veritabanı bağlantısı transfer edilmediği zaman, başka NDI paketine bu XML yüklendiğinde, rehber tanımında veritabanı bağlantısının oluşturulması gerekir. |
| Kaydet | Girilen tanımların kaydedilmesi için kullanılan butondur. |
| İptal | Girilen tanımlardan vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |

**Rehber XML İçeri Yükle**

Rehber XML İçeri Yükle sekmesi, NDI uygulaması tarafından XML dosyaya Export edilmiş bir rehberin, başka bir NDI uygulamasına yüklenmesi için kullanılan sekmedir.

Rehber XML İçeri Yükle ekranında yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| Rehber XML Dışarı Aktar/İçeri Yükle Ekranı |  |
| --- | --- |
| Dosya Adı | Yüklenmesi istenen fiziksel dosya ismi olup, rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, klasör ve dosya isminin belirlendiği alandır. |
| Nesne Adı | Yüklenecek nesnenin kodu, XML dosyadan bulunarak ekrana getirilir. İstenirse, değiştirilerek farklı bir kodla da yüklenebilir. |
| Veritabanı Bağlantı Kodu | Yüklenecek nesnenin XML dosyaya aktarımı sırasında veritabanı bağlantı kodu aktarılmışsa, bu bilgi otomatik olarak ekrana getirilir. İstenirse değiştirilip mevcut veritabanı bağlantılarından biri kullanılabilir. Eğer, veritabanı bağlantı bilgisi aktarılmamışsa bu saha okutulmaz ve nesnenin veritabanı bağlantı bilgisi oluşmaz. Bu durumda nesnenin tasarlandığı bölümden bu bilginin düzenlenmesi gerekir. |
| Kaydet | Girilen tanımların kaydedilmesi için kullanılan butondur. |
| İptal | Girilen tanımlardan vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
