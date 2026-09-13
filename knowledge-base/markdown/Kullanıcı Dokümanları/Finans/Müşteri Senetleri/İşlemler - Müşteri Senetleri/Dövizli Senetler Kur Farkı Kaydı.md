---
title: "Dövizli Senetler Kur Farkı Kaydı"
page_id: "24740115"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Müşteri Senetleri"
  - "İşlemler / Müşteri Senetleri"
  - "Dövizli Senetler Kur Farkı Kaydı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Müşteri Senetleri / İşlemler / Müşteri Senetleri / Dövizli Senetler Kur Farkı Kaydı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWQ4MzQ2MzkxLTlmZWEtNGU1NS04ZDcxLTViNzZmZTlkYWY5YyZsaW5rPWQwMTg4NjU3LTkxNDAtNGE3Yi05NjYxLTlhNDA1ZWE3MDE3ZiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=d8346391-9fea-4e55-8d71-5b76fe9daf9c&link=d0188657-9140-4a7b-9661-9a405ea7017f&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "dovizli-senetler-kur-farki-kaydi_34217790_24740115.html"
source_version: "2022-09-20T15:13:15.267+03:00"
source_bytes: 22305
fetched_at: "2026-09-13T04:11:56+00:00"
generator: "netsis-scraper 1.0.0"
---
# Dövizli Senetler Kur Farkı Kaydı

Dövizli Senetler Kur Farkı Kaydı, Finans Bölümü'nde, "İşlemler/Müşteri Senetleri " menüsünün altında yer alır. Dövizli Senetler Kur Farkı Kaydı, Müşteri Senetleri → Kayıt → Müşteri Parametreleri → "Döviz Uygulaması Var" parametresinin işaretlenerek dövizli senet kayıtlarının oluşturulduğu durumlarda, oluşacak kur farkı tutarlarına ait muhasebe kayıtlarının oluşmasını sağlayan bölümdür.

Dövizli Senetler Kur Farkı Kaydı bölümü çalıştırılmadan önce, Müşteri Senetleri → Raporlar → "Dövizli Senetler Yeniden Değerleme Listesi" bölümünden liste alınarak gerekli kontrollerin yapılması gerekir.

![](../../../../_assets/2e00ddffa98372b3b76a.png)

Dövizli Senetler Kur Farkı Kaydı ekranında yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| Dövizli Senetler Kur Farkı Kaydı Ekranı |  |
| --- | --- |
| Yeniden Değerleme Tarihi | Girilen senetlerin döviz bilgilerindeki döviz tutarları, yeniden değerleme tarihinde sorgulanan tarihteki kur değerlerine göre tekrar hesaplanarak "Senet Tutarı" alanından çıkarılıp (artı ya da eksi) kur farkı olarak entegre edilir. Kur farkı hesaplamalarının yapılması için; "Yeniden Değerlendirme Tarihi" alanından ve girilen tarihteki kur değerinin "Döviz Kurları Girişi" bölümünden daha önceden girilmesi gerekir. Yeniden değerleme tarihinde herhangi bir kur değeri bulunmazsa, kur farkı hesaplamaları 0 (sıfır) olarak sonuçlanır. Bu bölümden yapılan işlemlere portföy, banka tahsil/teminat hesabı ya da satıcılara ciro edilmiş olup henüz ödenmemiş senetler dahil edilir. Oluşan kur farkı tutarları "Devir Senet Girişi" bölümünden, senetlere göre ayrı ayrı izlenir. Oluşan kur farkı tutarlarının muhasebeye entegre edilmesi için; Muhasebe → Entegre → Kayıt → [Entegrasyon Kodları](<../../../Muhasebe/Entegre/Kayıt - Entegre/Entegrasyon Kodları.md>) → Senet/Çek sekmesinde yer alan "Kur Farkı Borçlu Hesap" ve "Kur Farkı Alacaklı Hesap" alanlarına ilgili muavin kodlarının girilmesi gerekir. |
| Kur Farkı Oluşturulan Kayıt | Kur farkı oluşturulan senetlerin numaralarının izlendiği alandır. |
| Döviz Çevrim Tipi | Kur farkı kaydı oluşturulacak senetler için, çevrim tipinin belirlendiği alandır. Döviz Çevrim Tipi; Döviz Alış, Döviz Satış, Efektif Alış ve Efektif Satış seçeneklerinden oluşur. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilgilerin onaylanmasını sağlayan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
