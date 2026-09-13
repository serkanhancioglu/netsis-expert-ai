---
title: "Dizayn / NDI"
page_id: "50682904"
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
  - "Dizayn / NDI"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / NDI - (Netsis Data Inspector) / İşlemler / NDI / XML Dışarı Aktar - İçeri Yükle / Dizayn / NDI"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTUxOGY5OTk2LTkyNGMtNGI5My05MmE5LTk0Mzg4MjJmOWFmNSZsaW5rPWFkN2ZhNjY3LWZiOTYtNDJiYy1hOTYyLWEyYjhmODY2MDExZSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=518f9996-924c-4b93-92a9-9438822f9af5&link=ad7fa667-fb96-42bc-a962-a2b8f866011e&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "dizayn-ndi_50682906_50682904.html"
source_version: "2022-09-16T11:12:05.430+03:00"
source_bytes: 9036
fetched_at: "2026-09-13T04:20:54+00:00"
generator: "netsis-scraper 1.0.0"
---
# Dizayn / NDI

Dizayn XML Dışarı Aktar/İçeri Yükle Ekranı; Dizayn XML Dışarı Aktar ve Dizayn XML İçeri Yükle olmak üzere iki sekmeden oluşur.

**Dizayn XML Dışarı Aktar**

Dizayn XML Dışarı Aktar sekmesi, NDI uygulamasında hazırlanan bir dizaynın dış ortama XML formatında aktarılması için kullanılan sekmedir.

Dizayn XML Dışarı Aktar/İçeri Yükle ekranında yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| Dizayn XML Dışarı Aktar/İçeri Yükle Ekranı |  |
| --- | --- |
| Dizayn Kodu | Aktarılması istenen dizaynın, dizayn tanımlamada belirlenen kodudur. |
| Dosya Adı | Aktarılması istenen fiziksel dosya ismi olup, Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, klasör ve dosya isminin belirlendiği alandır. |
| Kullanıcı Tanım | Kullanıcı Tanımları'nın aktarılması, aktarılan bu nesnenin yüklenmesi sırasında, karşı taraftaki NDI uygulamasında bulunan tüm kullanıcılara bu nesne ile ilgili tüm hakların verileceği anlamına gelir. Kullanıcı Tanımları aktarılmamışsa, nesnenin yüklenmesi sırasında karşı taraftaki NDI uygulamasında herhangi bir kullanıcı hakkı tanımlanmayacak ve kullanıcılar yüklenen bu nesneyi göremeyecekler. Kullanıcı haklarının yükleme sonrası ayrıca yapılması gerekir. |
| Veritabanı Bağlantı Bilgisi | Veritabanı bağlantı bilgisinin de nesneyle birlikte transfer edilip edilmeyeceğini belirlemek için kullanılan seçenektir. Veritabanı bağlantısı transfer edilmediği zaman, başka NDI paketine bu XML yüklendiğinde, dizayn tanımında veritabanı bağlantısının oluşturulması gerekir. |
| Kaydet | Girilen tanımların kaydedilmesi için kullanılan butondur. |
| İptal | Girilen tanımlardan vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |

**Dizayn XML İçeri Yükle**

Dizayn XML İçeri Yükle sekmesi, NDI uygulaması tarafından XML dosyaya Export edilmiş bir dizaynın, başka bir NDI uygulamasına yüklenmesi için kullanılan sekmedir.

| Dizayn XML Dışarı Aktar/İçeri Yükle Ekranı |  |
| --- | --- |
| Dosya Adı | Yüklenmesi istenen fiziksel dosya ismi olup, Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, klasör ve dosya isminin belirlendiği alandır. |
| Nesne Adı | Yüklenecek nesnenin kodu, XML dosyadan bulunarak ekrana getirilir. İstenirse, değiştirilerek farklı bir kodla da yüklenebilir. |
| Veritabanı Bağlantı Kodu | Yüklenecek nesnenin XML dosyaya aktarımı sırasında veritabanı bağlantı kodu aktarılmışsa, bu bilgi otomatik olarak ekrana getirilir. İstenirse değiştirilip mevcut veritabanı bağlantılarından biri kullanılabilir. Eğer, veritabanı bağlantı bilgisi aktarılmamışsa bu saha okutulmaz ve nesnenin veritabanı bağlantı bilgisi oluşmaz. Bu durumda nesnenin tasarlandığı bölümden bu bilginin düzenlenmesi gerekir. |
| Kaydet | Girilen tanımların kaydedilmesi için kullanılan butondur. |
| İptal | Girilen tanımlardan vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
