---
title: "Dövizli Çekler Kur Farkı Kaydı / Borç Çekleri"
page_id: "24740221"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Borç Çekleri"
  - "İşlemler / Borç Çekleri"
  - "Dövizli Çekler Kur Farkı Kaydı / Borç Çekleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Borç Çekleri / İşlemler / Borç Çekleri / Dövizli Çekler Kur Farkı Kaydı / Borç Çekleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPThiOWI5M2ExLTFlOWEtNDhiNS1iODZmLTdmNjIzZGI2MWUyOCZsaW5rPWUwMThlNmIzLWE2ODMtNDFjOS1iN2VhLWVlYjNiZWFhYjVmOCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=8b9b93a1-1e9a-48b5-b86f-7f623db61e28&link=e018e6b3-a683-41c9-b7ea-eeb3beaab5f8&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "dovizli-cekler-kur-farki-kaydi-borc-cekleri_34218965_24740221.html"
source_version: "2022-12-13T14:52:39.437+03:00"
source_bytes: 22999
fetched_at: "2026-09-13T04:12:36+00:00"
generator: "netsis-scraper 1.0.0"
---
# Dövizli Çekler Kur Farkı Kaydı / Borç Çekleri

Borç Çekleri modülü Dövizli Çekler Kur Farkı Kaydı bölümü, Finans Bölümü'nde İşlemler/Borç Çekleri menüsünün altında yer alır. Borç Çekleri modülü Dövizli Çekler Kur Farkı Kaydı bölümü, Borç Çekleri → Kayıt → Borç Çekleri Parametreleri → "Döviz Uygulaması Var" parametresinin işaretlenerek dövizli senet kayıtlarının oluşturulduğu durumlarda, oluşacak kur farkı tutarlarına ait muhasebe kayıtlarının oluşmasını sağlayan bölümdür.

Borç Çekleri modülü Dövizli Çekler Kur Farkı Kaydı bölümü çalıştırılmadan önce, Borç Çekleri → Raporlar → "[Dövizli Çekler Yeniden Değerleme Listesi](<../../Müşteri Çekleri/Raporlar - Müşteri Çekleri/Dövizli Çekler Yeniden Değerleme Listesi.md>)" bölümünden liste alınarak gerekli kontrollerin yapılması gerekir.

![](../../../../_assets/c41abcf22da5d3a20b44.png)

Borç Çekleri modülü Dövizli Çekler Kur Farkı Kaydı ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Dövizli Çekler Kur Farkı Kaydı Ekranı |  |
| --- | --- |
| Yeniden Değerleme Tarihi | Girilen çeklerin döviz bilgilerindeki döviz tutarları, yeniden değerleme tarihinde sorgulanan tarihteki kur değerlerine göre tekrar hesaplanarak "Çek Tutarı" alanından çıkarılıp (artı ya da eksi) kur farkı olarak entegre edilir. Kur farkı hesaplamalarının yapılması için; "Yeniden Değerlendirme Tarihi" alanından ve girilen tarihteki kur değerinin "Döviz Kurları Girişi" bölümünden daha önceden girilmesi gerekir. Yeniden değerleme tarihinde herhangi bir kur değeri bulunmazsa, kur farkı hesaplamaları 0 (sıfır) olarak sonuçlanır. Bu bölümden yapılan işlemlere portföy, banka tahsil/teminat hesabı ya da satıcılara ciro edilmiş olup henüz ödenmemiş çekler dahil edilir. Oluşan kur farkı tutarları "Devir Çek Girişi" bölümünden, senetlere göre ayrı ayrı izlenir. Oluşan kur farkı tutarlarının muhasebeye entegre edilmesi için; Muhasebe → Entegre → Kayıt → Entegrasyon Kodları → Senet/Çek sekmesinde yer alan "Kur Farkı Borçlu Hesap" ve "Kur Farkı Alacaklı Hesap" alanlarına ilgili muavin kodlarının girilmesi gerekir. |
| Kur Farkı Oluşturulan Kayıt | Kur farkı oluşturulan çeklerin numaralarının izlendiği alandır. |
| Döviz Çevrim Tipi | Kur farkı kaydı oluşturulacak çekler için, çevrim tipinin belirlendiği alandır. Döviz Alış, Döviz Satış, Efektif Alış ve Efektif Satış seçeneklerinden oluşur. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilgilerin onaylanmasını sağlayan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
