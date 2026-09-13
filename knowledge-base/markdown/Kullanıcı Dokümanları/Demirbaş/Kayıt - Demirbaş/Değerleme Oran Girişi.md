---
title: "Değerleme Oran Girişi"
page_id: "50683771"
product: "netsis-3-enterprise"
depth: 4
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Demirbaş"
  - "Kayıt / Demirbaş"
  - "Değerleme Oran Girişi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Demirbaş / Kayıt / Demirbaş / Değerleme Oran Girişi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPThjZjM1MjczLTJhNjctNDhhYi1iMTU5LWJkODE1NDBlNDM2NCZsaW5rPTliZGM4NGFkLTlkYWQtNDA1Mi05NDA5LTQ5YzY3YWVmOWE5OCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=8cf35273-2a67-48ab-b159-bd81540e4364&link=9bdc84ad-9dad-4052-9409-49c67aef9a98&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "degerleme-oran-girisi_90670083_50683771.html"
source_version: "2022-09-23T14:55:58.490+03:00"
source_bytes: 6250
fetched_at: "2026-09-13T04:21:18+00:00"
generator: "netsis-scraper 1.0.0"
---
# Değerleme Oran Girişi

Değerleme Oran Girişi bölümü, yıl bazında aylık değerleme oranlarının girilmesi için kullanılır. Değerleme oranları girilirken dikkat edilmesi gereken nokta; değerleme oranının, ilgili ay dahil olarak girilmesi gerektiğidir. Yani, 1. ay için değerleme oranının yıllık düşünülmesi gerekir fakat, 1 aya düşen değerin girilmesi gerekir.

**Örneğin,** yıllık % 60 değerleme düşünülüyorsa 1. aya % 5 oranının girilmesi gerekir. 2. ay için de 2 aylık toplam değerleme oranının girilmesi gerekir. Yani % 10 3. ay değerleme oranına şu anki uygulamaya göre, devletin 1. dönem için açıkladığı oranın girilmesi gerekir. Herhangi bir aya ait değerleme oranı girilmezse, program amortisman tutarlarını hesaplamaz. Ancak sıfır oranı bile olsa, oran tanımlı her ay için amortisman ayrılır. Oran sıfır ise, değerleme yapılmaz.

Aylık amortisman uygulaması yapan firmalar 3.6.9. ve 12. aylarda devletin açıkladığı oranları, diğer aylarda ise tahmini oranları girer. Dönemsel amortisman hesaplaması yapan firmaların sadece 3. 6. 9. ve 12. aylarda açıklanan değerleme oranlarını girmesi yeterlidir.

Program, değerleme ve amortisman ayırma işlemi çalıştırıldığında, çalıştırılan aya ait değerleme oranına göre, olması gereken tutarları hesaplar ve daha önceki aylarda hesaplanan amortisman tutarlarını düşerek ilgili aya kalan tutarı atar. Sonuç olarak, her zaman amortisman tutarları son değerleme oranına göre hesaplanır.

Değerleme Oran Girişi ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Değerleme Oran Girişi Ekranı |  |
| --- | --- |
| Yıl | Değerleme oranı için yıl girilen alandır. |
| Ay | Değerleme oranı için ay girilen alandır. |
| Değerleme Oranı | Değerleme oranının girildiği alandır. |
| Enflasyona Göre Oran Getir | Yeniden Değerleme Oranları yerine kullanılacak olan enflasyon endekslerine göre değerleme oranlarının oluşturulması için kullanılan butondur. Enflasyona Göre Oran Getir butonu ile, Döviz Modülünde girilen/indirilen enflasyon endekslerine göre, istenen dönem için değerleme oranları oluşturulur. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır. Değerleme Oran Girişi kaydının iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
