---
title: "Enflasyon Muhasebesine Başlama"
page_id: "50683926"
product: "netsis-3-enterprise"
depth: 4
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Demirbaş"
  - "İşlemler / Demirbaş"
  - "Enflasyon Muhasebesine Başlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Demirbaş / İşlemler / Demirbaş / Enflasyon Muhasebesine Başlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTMwNDliOGVjLTg1YjYtNDYzZS1hMGZjLTdjNzI2ODgwZDgxOSZsaW5rPWZkZDE3MDY0LWI4ZmYtNDdlMC1iMmIzLTNlMDk5Mzc1Yjg3MiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=3049b8ec-85b6-463e-a0fc-7c726880d819&link=fdd17064-b8ff-47e0-b2b3-3e099375b872&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "enflasyon-muhasebesine-baslama_50683928_50683926.html"
source_version: "2022-09-26T09:58:09.223+03:00"
source_bytes: 9534
fetched_at: "2026-09-13T04:21:26+00:00"
generator: "netsis-scraper 1.0.0"
---
# Enflasyon Muhasebesine Başlama

Enflasyon Muhasebesine Başlama, Demirbaş modülünde, sabit kıymet bilgilerinin enflasyon muhasebesi başlangıç tarihine getirilmesi için kullanılan bölümdür. Sabit kıymetleri alış tarihinden, verilen tarihe kadar endeksleyerek düzeltilmiş sabit kıymet değeri bulunur. Düzeltilmiş sabit kıymet değerinin mevcut sabit kıymet değerine oranı hesaplanır ve birikmiş amortisman da bu oranda - 328 Sayılı Vergi Usul Kanunu Genel Tebliği’nde önerildiği şekilde - düzeltilir.

Enflasyon Muhasebesine Başlama ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Enflasyon Muhasebesine Başlama Ekranı |  |
| --- | --- |
| Rapor Amaçlı Son İşlem Yıl/Ay | Mevcut amortisman bilgileri bozulmadan istenen tarihlere bilgi amaçlı enflasyon başlangıcı - ilgili tarihe getirme - yapılabilir. Bu olanağı sağlanın amacı; 5024 sayılı kanun gereğince 31/12/2004 tarihli bilançonun düzeltilecek ve düzeltme farklarının geçici 2. vergi döneminin sonuna kadar kayıtlara alınacak olmasıdır. Firmalar kayıtlarını yaptıkları bu tarihe kadar, eski yöntemle yeniden değerleme yapmaya ve amortisman ayırmaya devam edebilir. Dolayısıyla 31/12/2004 açılış kayıtlarının farkının girilmesinden sonra bir de açılış kayıtlarının girildiği bu tarihe kadar yapılan işlemlerin farklarının bulunması ve ayrıca bir fark fişi daha işlenmesi gerekir. **Örneğin,** X firması 30/06/2004 tarihine kadar eski yöntem ile yeniden değerleme yapmaya ve amortisman ayırmaya devam ediyor. İlk dönem yeniden değerleme oranı % 3.4 kullanılmış, ikinci dönemde ise yeniden değerleme yapılmadan devam edilmiş. 31/12/2003 için açılış kayıtlarının ve 30/06/2004 tarihine kadar farkların girilmesi isteniyor. Firmanın, öncelikle Haziran/2004’e ait işlemlerini tamamlaması gerekir. Daha sonra iki kez "Enflasyon Muhasebesine Başlama" işlemini çalıştırması gerekir. İlk çalıştırmada "Rapor Amaçlı" işaretlenir ve Son İşlem Yıl/Ay, 2003/12 verilir. İkinci çalıştırmada ise "Rapor Amaçlı" işaretlenmez ve Son İşlem Yıl/Ay, 2004/06 verilir. Rapor amaçlı olmayan tek bir enflasyon başlangıç kaydı bulunması gerekir. Program bu konuda gerekli korumayı sağlar. Rapor amaçlı olmayan gerçek devir kaydından sonraki tarihlerde program, "Değerleme ve Amortisman Ayırma" işlemini enflasyon muhasebesi mevzuatına göre yapar. Gerçek devir tarihinden önce ve sonra istendiği kadar rapor amaçlı devir bulunabilir. |
| Şirketler | Enflasyon Muhasebesine Başlama işlemi için şirket bilgisi girilen alandır. |
| ![](../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilgilerin onaylanmasını sağlayan butondur. |
| ![](../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
