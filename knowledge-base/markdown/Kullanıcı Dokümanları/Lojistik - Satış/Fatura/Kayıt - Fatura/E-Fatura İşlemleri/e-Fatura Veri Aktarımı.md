---
title: "e-Fatura Veri Aktarımı"
page_id: "47084837"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Fatura"
  - "Kayıt / Fatura"
  - "E-Fatura İşlemleri"
  - "e-Fatura Veri Aktarımı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Fatura / Kayıt / Fatura / E-Fatura İşlemleri / e-Fatura Veri Aktarımı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTY3MDEwMWVhLTZmOTItNDdiMS04NTgzLTY3YjM2NTU2MjU3OCZsaW5rPTZiOWY2ZjVkLWM3MzktNGUxOS1hMWU1LWMwNzkzZmZkMGY2NCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=670101ea-6f92-47b1-8583-67b365562578&link=6b9f6f5d-c739-4e19-a1e5-c0793ffd0f64&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "e-fatura-veri-aktarimi_47084845_47084837.html"
source_version: "2022-10-24T13:44:15.643+03:00"
source_bytes: 8255
fetched_at: "2026-09-13T04:02:09+00:00"
generator: "netsis-scraper 1.0.0"
---
# e-Fatura Veri Aktarımı

e-Fatura veri aktarımının yapılması için kullanılan bölüm, e-Fatura Veri Aktarımı bölümüdür. e-Fatura Veri Aktarımı, Tarih Aralığı kısıdı verilerek, belirlenen tarih aralığındaki e-fatura verilerinin aktarılmasını sağlar. Gelen ve giden e-faturaların şirket veritabanında tutulmasıyla birlikte data boyutunda e-Faturaların XML verileri nedeniyle büyüme yaşanır. Yapılan düzenleme ile e-Fatura verisinin veri tabanında sıkıştırılmış şekilde tutulması ve tüm işlemlerin sıkıştırılmış veri üzerinden yapılması sağlanır. Mevcut kayıtların da sıkıştırılmış şekilde saklanması için e-Fatura veri aktarımı işleminin mutlaka çalıştırılması gerekir. Bu işlem çalıştırıldığında, ekranda sorulan tarih aralığındaki faturalar ve bununla ilişkili zarflar ve yanıtları sıkıştırılarak tabloda saklanır.

Ekranda sorulan dosya yollarının düzgün şekilde girilmesi gerekir. Özellikle gelen dizininde e-fatura parametrelerindeki dosya yolunun yazılmaması gerekir. Sisteme ilk düşen e-Faturaların tutulduğu Web servisin kurulu olduğu makinede, e-Faturaların tutulduğu dizin veya dizinlerin belirtilmesi gerekir.

Gelen ve giden dosya yolu olarak eklenecek dizinler için ağ sürücüsü (Mapped Drive) yerine makine ismi (\\\\MakineAdı\\Path) kullanılabilir.

Gelen dosya yolu olarak entegrasyon çözümlerinde Web servis/servisler üzerinde kullanılan dizin/dizinlerin seçilmesi gerekir. Özel dizin belirtilmemişse Web servisin kurulu olduğu makinedeki temp dizini kullanılır. Özel dizin Web servisin kurulu olduğu dizinde bulunan web.config dosyasının içindeki ReceivedDocumentsPath değişkeninin değeri ile belirtilmiş olabilir. Özel dizin belirtilmiş de olsa, ilgili makinedeki temp dizininin eklenmesi ReceivedDocumentsPath değişkenin tanımlandığı zamandan önceki zarflar için faydalı olur. Temp dizini, makine üzerindeki Windows dizini altındaki Temp dizinidir (C:\\Windows\\Temp gibi).

Aktarım uygulaması farklı bir makinede çalışıyorsa, bu dizinlere okuma yetkisi ile paylaşım verilmesi gerekir.

Web servisin kullandığı dizinlerden emin olmak için SELECT INFOLOG FROM TBLEFATURALOG WHERE INFOLOG LIKE '%CONTENT%ZARFID%PATH%' sorgusunun sonucunda dönecek PATH bilgileri aşağıdaki şekilde kullanılabilir:

- Bu işlem e-Faturaların herhangi bir değişikliğe uğramadan orijinal hallerinin sıkıştırılmış olarak veritabanında tutulmasına imkan vermesi nedeniyle veri güvenliğini arttırıcı bir işlemdir.
- Aynı zamanda da yeni yıl devirlerinin daha hızlı yapılması için gerekli bir işlemdir.
- Veri aktarımı, e-Faturaların mevcut saklandıkları tablo (TBLEFATZARF) üzerinde sıkıştırarak tablo boyutunu küçültür.
- Veri aktarımı, verilen klasörde bulabildiği e-Faturaları orijinal halleriyle alarak, klasörde bulunamıyorsa veritabanındaki haliyle alır ve sıkıştırılır. Herhangi bir sebepten sıkıştırma işlemi yapılamayan faturalar, veritabanındaki hali ile kalır.
- Sonuç olarak bu işlemin çalıştırılması, mevcut e-Fatura işleyişinde herhangi bir değişikliğe neden olmaz.

Klasörlerin içinden giden dosya yolunu seçmek için üç nokta ![](../../../../../_assets/5098b020c5e814c92501.png) butonu, aşağıdaki alana eklemek için de Ekle ![](../../../../../_assets/53d410e2b7bef2eff3e8.png) butonu kullanılır. Aynı şekilde gelen dosya yolunu seçmek için üç nokta ![](../../../../../_assets/5098b020c5e814c92501.png) butonu, seçileni aşağıdaki alana eklemek için de Ekle ![](../../../../../_assets/53d410e2b7bef2eff3e8.png) butonu kullanılır.

Verilen tarih aralığındaki zarfların aktarılmaya başlanması için Başla ![](../../../../../_assets/0ba3437d42ec67ccfcba.png), Log bilgilerini kaydetmek için de Log Bilgilerini Kaydet ![](../../../../../_assets/374323c2e2e4248f8ccb.png) butonuna tıklanır.
