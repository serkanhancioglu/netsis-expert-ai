---
title: "Log Parametreleri"
page_id: "24753630"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Genel"
  - "Log Modülü"
  - "Kayıt / Log Modülü"
  - "Log Parametreleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Log Modülü / Kayıt / Log Modülü / Log Parametreleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTRmYjEwYmYyLWU1YzctNDk2Zi1hMTFmLTI5ZDM4NTc5ZDJjZCZsaW5rPTgwZDllY2EyLTNhZTctNGQ3ZS1iM2U1LWNkY2UxMmIzOGU0ZSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=4fb10bf2-e5c7-496f-a11f-29d38579d2cd&link=80d9eca2-3ae7-4d7e-b3e5-cdce12b38e4e&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "log-parametreleri_41169720_24753630.html"
source_version: "2022-09-16T15:09:52.143+03:00"
source_bytes: 9907
fetched_at: "2026-09-13T04:18:24+00:00"
generator: "netsis-scraper 1.0.0"
---
# Log Parametreleri

Log Parametreleri, Genel Bölümü'nde, "Kayıt/Log Modülü" menüsünün altında yer alır.

Log Parametreleri ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Log Parametreleri Ekranı |  |
| --- | --- |
| Log Uygulaması Kullanılsın | Yapılan işlemlerin Log'a aktarılması için kullanılan parametredir. İşaretlenmediği zaman, kayıtlar Log'a atılmaz. Parametre işaretlendiğinde, "Log Tutulacak Tablolar" ekranında Log tutulması istenen tablolara "Evet" olarak yetki verilmezse, söz konusu tablolar için log tutulmaz. Log Uygulaması, ilgili işletmenin şubeleri bazında tanımlanır ve istenen şube veya şubelerde log takibi yapılabilir. Örneğin, ilgili işletmenin merkezinde "Log Uygulaması" kullanıldığı ve parametrenin aktif hale getirildiği varsayıldığında; Şube 2’de Log tutulması isteniyorsa, Şube 2’ye girilip "Log Uygulaması Kullanılsın" parametresinin işaretlenmesi gerekir.<br>"Log Uygulaması Kullanılsın" parametresi işaretlenip, log tutulacak tabloların hepsinin "Hayır" olması durumunda, sadece operasyon ve hataların Log'u alınabilir. |
| Raporlar Loga Yazılsın | Alınan raporların Log'a kaydedilmesi için kullanılan parametredir. Tablo adı, raporun adıdır ve operasyon Log'u olarak kayıt aktarılır. "Açıklama" alanına ilgili raporun adı yazılacağı için, hangi raporun hangi kullanıcı tarafından ve hangi tarihte alındığı gibi bilgiler kolay bir şekilde görülebilir. |
| Düzeltme İşlemlerinde Kaydın Eski Hali Tutulsun | Düzeltme işlemi yapıldığında, düzeltilen kaydın hem eski hem de yeni halinin Log'a kaydedilmesi için kullanılan parametredir. Parametre işaretlenmediği zaman, sadece kaydın son hali Log'a kaydedilir. |
| Kullanıcı Oturum İşlemleri Log Kayıtları Tutulsun | Logo Netsis programına giriş ve çıkış yapan kullanıcıların Log'unun tutulması ve "Log Raporunda" listelenmesi için kullanılan parametredir. |
| Uyarlama Araçlarından Manuel Atılan Kayıtlar İçin Log Tutulsun | "[Log Tutulacak Tablolar](<Log Tutulacak Tablolar/index.md>)" bölümüne "Kullanıcı Tabloları" sekmesinin getirilmesini ve uyarlama araçlarından atılan manuel kayıtlar için log tutulmasını sağlayan parametredir. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | İşaretlenen parametrelerle ilgili işlemlerin gerçekleşmesini sağlayan butondur. Parametrelerle ilgili işlemlerin programa yansıması için programın kapatılıp tekrar açılması gerekir. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | İşaretlenen parametrelerden vazgeçilmesi halinde kullanılan butondur. |
