---
title: "Dövizli Senetler Kur Farkı Kaydı / Borç Senetleri"
page_id: "24740309"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Borç Senetleri"
  - "İşlemler / Borç Senetleri"
  - "Dövizli Senetler Kur Farkı Kaydı / Borç Senetleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Borç Senetleri / İşlemler / Borç Senetleri / Dövizli Senetler Kur Farkı Kaydı / Borç Senetleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWFkYjRlZWI0LTYyY2MtNDIxMy04YTJjLTA4ZjI4NmMxNDJhZSZsaW5rPWRkNGM4ZjE3LTBlMjgtNGVjNy04YjYyLTc4ODFkNDBjYjJkYyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=adb4eeb4-62cc-4213-8a2c-08f286c142ae&link=dd4c8f17-0e28-4ec7-8b62-7881d40cb2dc&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "dovizli-senetler-kur-farki-kaydi-borc-senetleri_34218442_24740309.html"
source_version: "2022-12-13T09:58:35.687+03:00"
source_bytes: 23193
fetched_at: "2026-09-13T04:12:20+00:00"
generator: "netsis-scraper 1.0.0"
---
# Dövizli Senetler Kur Farkı Kaydı / Borç Senetleri

Borç Senetleri modülü Dövizli Kur Farkı Kaydı bölümü, Finans Bölümü'nde, "İşlemler/Borç Senetleri " menüsünün altında yer alır. Borç Senetleri modülü Dövizli Kur Farkı Kaydı bölümü, Borç Senetleri → Kayıt → Borç Senetleri Parametreleri → "Döviz Uygulaması Var" parametresinin işaretlenerek dövizli senet kayıtlarının oluşturulduğu durumlarda, oluşacak kur farkı tutarlarına ait muhasebe kayıtlarının oluşmasını sağlayan bölümdür.

> [!NOTE]
> Borç Senetleri modülü Dövizli Kur Farkı Kaydı bölümü çalıştırılmadan önce, Borç Senetleri → Raporlar → "[Dövizli Senetler Yeniden Değerleme Listesi](<../../Müşteri Senetleri/Raporlar - Müşteri Senetleri/Dövizli Senetler Yeniden Değerleme Listesi.md>)" bölümünden liste alınarak gerekli kontrollerin yapılması gerekir.

![](../../../../_assets/67816bc3583be1546106.png)

Borç Senetleri modülü Dövizli Kur Farkı Kaydı ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Dövizli Senetler Kur Farkı Kaydı Ekranı |  |
| --- | --- |
| Yeniden Değerleme Tarihi | Girilen senetlerin döviz bilgilerindeki döviz tutarları, yeniden değerleme tarihinde sorgulanan tarihteki kur değerlerine göre tekrar hesaplanarak "Senet Tutarı" alanından çıkarılıp (artı ya da eksi) kur farkı olarak entegre edilir. Kur farkı hesaplamalarının yapılması için; "Yeniden Değerlendirme Tarihi" alanından ve girilen tarihteki kur değerinin "Döviz Kurları Girişi" bölümünden daha önceden girilmesi gerekir. Yeniden değerleme tarihinde herhangi bir kur değeri bulunmazsa, kur farkı hesaplamaları 0 (sıfır) olarak sonuçlanır. Bu bölümden yapılan işlemlere portföy, banka tahsil/teminat hesabı ya da satıcılara ciro edilmiş olup henüz ödenmemiş senetler dahil edilir. Oluşan kur farkı tutarları "Devir Senet Girişi" bölümünden, senetlere göre ayrı ayrı izlenir. Oluşan kur farkı tutarlarının muhasebeye entegre edilmesi için; Muhasebe → Entegre → Kayıt → [Entegrasyon Kodları](<../../../Muhasebe/Entegre/Kayıt - Entegre/Entegrasyon Kodları.md>) → Senet/Çek sekmesinde yer alan "Kur Farkı Borçlu Hesap" ve "Kur Farkı Alacaklı Hesap" alanlarına ilgili muavin kodlarının girilmesi gerekir. |
| Kur Farkı Oluşturulan Kayıt | Kur farkı oluşturulan senetlerin numaralarının izlendiği alandır. |
| Döviz Çevrim Tipi | Kur farkı kaydı oluşturulacak senetler için, çevrim tipinin belirlendiği alandır. Döviz Alış, Döviz Satış, Efektif Alış ve Efektif Satış seçeneklerinden oluşur. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) | Girilen bilgilerin onaylanmasını sağlayan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
