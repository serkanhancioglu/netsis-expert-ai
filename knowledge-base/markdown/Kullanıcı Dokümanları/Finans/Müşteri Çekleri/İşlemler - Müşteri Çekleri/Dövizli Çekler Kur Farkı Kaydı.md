---
title: "Dövizli Çekler Kur Farkı Kaydı"
page_id: "24739892"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Müşteri Çekleri"
  - "İşlemler / Müşteri Çekleri"
  - "Dövizli Çekler Kur Farkı Kaydı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Müşteri Çekleri / İşlemler / Müşteri Çekleri / Dövizli Çekler Kur Farkı Kaydı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTI0YTkxOWM0LTYzNjMtNDNjNC05YmI3LTUxODVlYWYxNzk3YyZsaW5rPTVmNWU1ODgwLTE0MmEtNGE0ZC04ZjkzLTFhNzhhMWM1ODc1NyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=24a919c4-6363-43c4-9bb7-5185eaf1797c&link=5f5e5880-142a-4a4d-8f93-1a78a1c58757&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "dovizli-cekler-kur-farki-kaydi_34211184_24739892.html"
source_version: "2022-09-22T16:48:56.283+03:00"
source_bytes: 22243
fetched_at: "2026-09-13T04:11:16+00:00"
generator: "netsis-scraper 1.0.0"
---
# Dövizli Çekler Kur Farkı Kaydı

Dövizli Çekler Kur Farkı Kaydı, Finans Bölümü'nde, "İşlemler/Müşteri Çekleri " menüsünün altında yer alır. Dövizli Çekler Kur Farkı Kaydı, Müşteri Çekleri → Kayıt → [Müşteri Parametreleri](<../Kayıt - Müşteri Çekleri/Müşteri Çekleri Parametreleri.md>) → "Döviz Uygulaması Var" parametresinin işaretlenerek dövizli çek kayıtlarının oluşturulduğu durumlarda, oluşacak kur farkı tutarlarına ait muhasebe kayıtlarının oluşmasını sağlayan bölümdür.

Dövizli Çekler Kur Farkı Kaydı bölümü çalıştırılmadan önce, Müşteri Çekleri → Raporlar → "[Dövizli Çekler Yeniden Değerleme Listesi](<../Raporlar - Müşteri Çekleri/Dövizli Çekler Yeniden Değerleme Listesi.md>)" bölümünden liste alınarak gerekli kontrollerin yapılması gerekir.

![](../../../../_assets/93533b1ff9fa14798c55.png)

Dövizli Çekler Kur Farkı Kaydı ekranında yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| Dövizli Çekler Kur Farkı Kaydı Ekranı |  |
| --- | --- |
| Yeniden Değerleme Tarihi | Girilen çeklerin döviz bilgilerindeki döviz tutarları, yeniden değerleme tarihinde sorgulanan tarihteki kur değerlerine göre tekrar hesaplanarak "Çek Tutarı" alanından çıkarılıp (artı ya da eksi) kur farkı olarak entegre edilir. Kur farkı hesaplamalarının yapılması için; "Yeniden Değerlendirme Tarihi" alanından ve girilen tarihteki kur değerinin "Döviz Kurları Girişi" bölümünden daha önceden girilmesi gerekir. Yeniden değerleme tarihinde herhangi bir kur değeri bulunmazsa, kur farkı hesaplamaları 0 (sıfır) olarak sonuçlanır. Bu bölümden yapılan işlemlere portföy, banka tahsil/teminat hesabı ya da satıcılara ciro edilmiş olup henüz ödenmemiş çekler dahil edilir. Oluşan kur farkı tutarları "Devir Çek Girişi" bölümünden, çeklere göre ayrı ayrı izlenir. Oluşan kur farkı tutarlarının muhasebeye entegre edilmesi için; Muhasebe → Entegre → Kayıt → [Entegrasyon Kodları](<../../../Muhasebe/Entegre/Kayıt - Entegre/Entegrasyon Kodları.md>) → Senet/Çek sekmesinde yer alan "Kur Farkı Borçlu Hesap" ve "Kur Farkı Alacaklı Hesap" alanlarına ilgili muavin kodlarının girilmesi gerekir. |
| Kur Farkı Oluşturulan Kayıt | Kur farkı oluşturulan çeklerin numaralarının izlendiği alandır. |
| Döviz Çevrim Tipi | Kur farkı kaydı oluşturulacak çekler için, çevrim tipinin belirlendiği alandır. Döviz Çevrim Tipi; Döviz Alış, Döviz Satış, Efektif Alış ve Efektif Satış seçeneklerinden oluşur. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilgilerin onaylanmasını sağlayan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
