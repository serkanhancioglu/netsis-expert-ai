---
title: "Enflasyon Muhasebesine Başlama (Enflasyon Muhasebesi Vergi Usul Kanunu)"
page_id: "24740902"
product: "netsis-3-enterprise"
depth: 7
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Muhasebe"
  - "Muhasebe Modülü"
  - "Ekler / Muhasebe"
  - "Ek-1 Enflasyon Muhasebesi"
  - "Demirbaş Modülü"
  - "Enflasyon Muhasebesine Başlama (Enflasyon Muhasebesi Vergi Usul Kanunu)"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / Ekler / Muhasebe / Ek-1 Enflasyon Muhasebesi / Demirbaş Modülü / Enflasyon Muhasebesine Başlama (Enflasyon Muhasebesi Vergi Usul Kanunu)"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTViYzFiOTIzLTAzZmEtNDVhNC1iZTM5LTkwNDVjZjVkOTM0MCZsaW5rPWIyYzk4YmQ1LTZkYjItNGE1ZC04Y2U1LWFkMmI2YWY5MGM5MSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=5bc1b923-03fa-45a4-be39-9045cf5d9340&link=b2c98bd5-6db2-4a5d-8ce5-ad2b6af90c91&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "enflasyon-muhasebesine-baslama-enflasyon-muhasebesi-vergi-usul-kanunu_41162201_24740902.html"
source_version: "2022-12-12T16:06:10.900+03:00"
source_bytes: 3765
fetched_at: "2026-09-13T04:14:21+00:00"
generator: "netsis-scraper 1.0.0"
---
# Enflasyon Muhasebesine Başlama (Enflasyon Muhasebesi Vergi Usul Kanunu)

Enflasyon Muhasebesine Başlama ile ilgili ayrıntılı bilgiye bu dokümandan ulaşılabilir.

Demirbaş Modülünde, sabit kıymet bilgilerinin enflasyon muhasebesi başlangıç tarihine getirilmesi için kullanılan bölümdür. Alış tarihinden verilen tarihe kadar sabit kıymetleri endeksleyerek, düzeltilen sabit kıymet değerini bulur. Düzeltilen sabit kıymet değerinin mevcut sabit kıymet değerine oranı hesaplanır ve birikmiş amortisman da bu oranda düzeltilir. (328 Sayılı Vergi Usul Kanunu Genel Tebliğinde önerildiği şekilde).

**Rapor Amaçlı:** Mevcut amortisman bilgileri bozulmadan, istenen tarihlere bilgi amaçlı enflasyon başlangıcı (ilgili tarihe getirme) yapılabilir. Bu olanağı sağlamanın amacı, 5024 sayılı kanun gereğince 31/12/2004 tarihli bilançonun düzeltilmesi ve düzeltme farklarının geçici 2. vergi döneminin sonuna kadar kayıtlara alınmasıdır. Firmalar, kayıt yaptıkları bu tarihe kadar, eski yöntemle yeniden değerleme yapmaya ve amortisman ayırmaya devam edebilir. Dolayısıyla, 31/12/2004 açılış kayıt farklarının girilmesinden sonra, açılış kayıtlarının girildiği bu tarihe kadar yapılan işlemlerin farklarının bulunması ve ayrıca bir fark fişi daha işlenmesi gerekir.

**Örneğin;**

X firmasının 30/06/2004 tarihine kadar eski yöntem ile yeniden değerleme yapmaya ve amortisman ayırmaya devam ettiği varsayıldığında;

İlk dönem yeniden değerleme oranı % 3.4 kullanılıyor ve ikinci dönem yeniden değerleme yapılmadan devam ediliyor. 31/12/2003 için açılış kayıtları ve 30/06/2004 tarihine kadar olan farkların girilmesi isteniyor.

Firmanın, öncelikle Haziran 2004’e ait işlemleri tamamlaması gerekir. Daha sonra iki kez "Enflasyon Muhasebesine Başlama" işleminin çalıştırılması gerekir. İlk çalıştırmada "Rapor Amaçlı" seçeneği işaretlenir ve "Son İşlem Yıl/Ay" 2003/12 girilir. İkinci çalıştırmada ise "Rapor Amaçlı" seçeneği işaretlenmez ve "Son İşlem Yıl/Ay" 2004/06 girilir.

**Not:** Rapor amaçlı olmayan tek bir enflasyon başlangıç kaydının bulunması gerekir. Program bu konuda gerekli korumayı sağlar. Rapor amaçlı olmayan gerçek devir kaydından sonraki tarihlerde "Değerleme ve Amortisman Ayırma" işlemi program tarafından enflasyon muhasebesi mevzuatına göre yapılır. Gerçek devir tarihi öncesi ve sonrasında, istenen miktarda rapor amaçlı devir bulunabilir.
