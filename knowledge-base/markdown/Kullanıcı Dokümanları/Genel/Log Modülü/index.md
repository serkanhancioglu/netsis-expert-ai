---
title: "Log Modülü"
page_id: "22803552"
product: "netsis-3-enterprise"
depth: 3
is_section: true
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Genel"
  - "Log Modülü"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Log Modülü"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTdjMTE0NzJhLWUxMjEtNDA5Mi1iNjhiLTcwMzE1NzRhNGU0MyZsaW5rPTgzN2NjZmRiLTcwMTUtNGEwNS1hN2NkLWFkNTZhNGUwODg3ZSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=7c11472a-e121-4092-b68b-7031574a4e43&link=837ccfdb-7015-4a05-a7cd-ad56a4e0887e&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "log-modulu_24753528_22803552.html"
source_version: "2022-09-16T14:13:14.890+03:00"
source_bytes: 3804
fetched_at: "2026-09-13T04:18:21+00:00"
generator: "netsis-scraper 1.0.0"
---
# Log Modülü

Log Modülü, yazılım veya işletim sisteminin bir özelliği olarak yerleştirilen "Log" sisteminde, yapılan çalışma süresi içinde kimin, hangi zamanda ne iş yaptığının sürekli kaydının tutulduğu modüldür. Log Modülü, güvenlik açısından herhangi bir hata ortaya çıktığı durumlarda kullanılır. Bilerek veya bilmeyerek, hatanın kim tarafından ve hangi zamanda yapıldığı bu modül sayesinde tespit edilir. Log, daha çok bankaların bilgi işlem sistemlerinde uygulanır. Yerli ve yabancı denetleme kuruluşlarının, güvenlik açısından bilgisayar yazılımlarında öncelikli olarak aradıkları bir özelliktir. Netsis programında Log kayıtları, kullanıcıların program üzerinde yaptıkları her türlü işlemde, Netsis kullanıcı isimleri, işlemin yapıldığı menü seçeneği, dosya ismi, saat, tarih, işlem türü detaylarını kapsar.

Sistemde dört temel işlem türü baz alınır ve bunlar; Kayıt, Düzeltme, İptal ve Operasyon'dur.

**Kayıt:** Fatura kaydı gibi programda yapılan kayıt işlemlerinin detaylarını saklar.

**Düzeltme:** Daha önce programda kaydı yapılmış bir işlemin, düzenlenmeden önceki eski hali ve düzeltilmiş hali ile detaylarını saklar.

**İptal:** Kaydın, iptal edildiği şekliyle detayını saklar.

**Operasyon:** Program içinde, "Hareket Kontrolü", "Kod Değişikliği" gibi işlemler çalıştırıldığında ya da uyarı alındığında, belli bir operasyonun gerçekleştirildiğine dair log kaydı saklanır. Log sisteminde, isteğe bağlı olarak programdaki hangi tablolar için ve tanımlanan tablolarda yapılan hangi tür işlemler için (Kayıt, İptal, Düzeltme, Operasyon) log tutulacağı "[Log Tutulacak Tablolar](<Kayıt - Log Modülü/Log Tutulacak Tablolar/index.md>)" bölümü ile tanımlanır.

"Log Uygulaması" için tanımlama yapılırken, ihtiyaca göre hangi tablolar için Log tutulması isteniyorsa o tablolar için tanımlama yapılması gerekir. Bu nedenle, Log tutulurken veritabanının yapılan kayıtların yoğunluğuna bağlı olarak hızla büyüyeceği ve sistemde yeterli disk alanının olması gerektiği konularına dikkat edilmesi gerekir.

Log Modülü, kullanıcıların program içinde yaptığı her türlü işlemin, veritabanındaki kayıt yerinin dışında Log alanına kaydedilmesini sağlar. Log alanındaki kayıtlar, isteyerek veya istemeyerek kullanıcının yaptığı hatayı tespit etmek için tutulur. Log edilen bilgiler, ihtiyaç duyulduğunda, özel uygulamalar ile geri dönüşü sağlayacak detayda tutulur.
