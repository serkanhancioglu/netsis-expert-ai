---
title: "Fatura Özel Parametreleri"
page_id: "47075709"
product: "netsis-3-enterprise"
depth: 4
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Fatura"
  - "Fatura Özel Parametreleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Fatura / Fatura Özel Parametreleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWY1ODIxMGQwLTIwNWItNGFhMS04NTllLTk4YzliYWY0YTM0YyZsaW5rPTA2MjdmYWU4LWY4MGUtNDRjZC1iODk3LWUwNDM5ZjE0MTMxMCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=f58210d0-205b-4aa1-859e-98c9baf4a34c&link=0627fae8-f80e-44cd-b897-e0439f141310&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "fatura-ozel-parametreleri_47075711_47075709.html"
source_version: "2022-10-25T14:21:21.083+03:00"
source_bytes: 24031
fetched_at: "2026-09-13T04:03:24+00:00"
generator: "netsis-scraper 1.0.0"
---
# Fatura Özel Parametreleri

Fatura özel parametrelerinin tanımlanması için "[Özel Parametre Tanımlamaları](<../../Genel/Yardımcı Programlar/Kayıt - Yardımcı Programlar/Özel Parametre Tanımları.md>)" ekranı kullanılır.

KDV Tutarından Tevkifat Tutarının Düşülerek Tevkifat Satış Hesabına Satır Bazında Aktarılmasının Sağlanması için tanımlanacak özel parametre aşağıdaki şekildedir:

| Özel Parametre Tanımlamaları Ekranı |  |
| --- | --- |
| Grup Kodu | FATURA |
| Anahtar | SATIRBAZITEVKIFAT |

KDV Tutarından Tevkifat Tutarının Düşülerek Tevkifat Satış Hesabına Aktarılmasının Sağlanması için tanımlanacak özel parametre aşağıdaki şekildedir:

| Özel Parametre Tanımlamaları Ekranı |  |
| --- | --- |
| Grup Kodu | FATURA |
| Anahtar | TEVKIFAT |
| Değer | K |

Teslim Caride Kullanılan Cari Hesap Kilitli Olsa Bile İşlemin Devam Etmesinin Sağlanması için tanımlanacak özel parametre aşağıdaki şekildedir:

| Özel Parametre Tanımlamaları Ekranı |  |
| --- | --- |
| Grup Kodu | FATURA |
| Anahtar | TESLIMCARIKILITLENMESIN |

Toplam KDV Alanında Değişiklik Yapıldığında, Muhasebe Fişinde Yer Alan KDV Hesabına Da Aynı Tutarın Aktarılmasının Sağlanması için tanımlanacak özel parametre aşağıdaki şekildedir:

| Özel Parametre Tanımlamaları Ekranı |  |
| --- | --- |
| Grup Kodu | FATURA |
| Anahtar | KDVYUVFARK |

KDV Tutarı 0 (sıfır) Olan Belge İçin 351 istisna kodunun Otomatik Atılmamasının Sağlanması için tanımlanacak özel parametre aşağıdaki şekildedir:

| Özel Parametre Tanımlamaları Ekranı |  |
| --- | --- |
| Grup Kodu | FATURA |
| Anahtar | ISTISNAONDEGER |

Tevkifat Tutarının Cari Hesaptan Düşülmeden Ayrı Bir Satıra Atılmasının Sağlanması için tanımlanacak özel parametre aşağıdaki şekildedir:

Bu parametre kullanıldığında, belge kalemleri bazında farklı proje ve referans kodu girişinin yapılmaması gerekir.

| Özel Parametre Tanımlamaları Ekranı |  |
| --- | --- |
| Grup Kodu | FATURA |
| Anahtar | TEVKIFATBORCALACAK |

"Ambar Fişi Muhasebeleştirme" İşlemi Aynı Tarih İçin Tekrar Çalıştırıldığında “Eski fişin üzerine yazılsın mı?” Sorgusuna Göre Oluşacak Muhasebe Kaydının Eski Kaydı Silerek Ya Da Ayrı Bir Kayıt Olarak Oluşturulmasının Sağlanması için tanımlanacak özel parametre aşağıdaki şekildedir:

| Özel Parametre Tanımlamaları Ekranı |  |
| --- | --- |
| Grup Kodu | FATURA |
| Anahtar | AMBARMUHFISTEKRAR |

İade Tipli Satış Faturasının İskonto Muhasebe Hesap Kodlarının Ters Çalışmasının Sağlanması için tanımlanacak özel parametre aşağıdaki şekildedir:

**Örneğin:** Aşağıdaki tanımlama yapıldığında, iade tipli ve iskontolu satış faturası girildiğinde, alış iskonto muhasebe kodunun çalışması sağlanır.

| Özel Parametre Tanımlamaları Ekranı |  |
| --- | --- |
| Grup Kodu | FATURA |
| Anahtar | SATISIADEISK |

İade Tipli Alış Faturasının İskonto Muhasebe Hesap Kodlarının Ters Çalışmasının Sağlanması için tanımlanacak özel parametre aşağıdaki şekildedir:

| Özel Parametre Tanımlamaları Ekranı |  |
| --- | --- |
| Grup Kodu | FATURA |
| Anahtar | ALISIADEISK |

Alış Faturası ve Satış İrsaliyesinde Akıllı Grid Yapısının Kullanılmamasının Sağlanması için tanımlanacak özel parametre aşağıdaki şekildedir:

| Özel Parametre Tanımlamaları Ekranı |  |
| --- | --- |
| Grup Kodu | GRID |
| Anahtar | PERFORMANS |
| Değer | 1_2;1_3 (modül numarası\_program numarası) |

Fatura, İrsaliye, Sipariş, DAT ve Ambar Fiş Girişlerinde Gönderilen e-Postanın "Yeni Kayıt" veya "Düzeltme Kaydı" Başlığı İle Gönderilmesinin Sağlanması için tanımlanacak özel parametre aşağıdaki şekildedir:

| Özel Parametre Tanımlamaları Ekranı |  |
| --- | --- |
| Grup Kodu | FATURA |
| Anahtar | EPOSTA_KONU_DETAYLANDIRILSIN |

İrsaliye Faturalandırma İşleminde, Yeni Fatura Bilgileri Ekranına, Faturanın Varsayılan Seri Değerinin Getirilmesinin Sağlanması için tanımlanacak özel parametre aşağıdaki şekildedir:

Varsayılan bir seri değeri tanımlı değilse, irsaliyenin serisi getirilir.

| Özel Parametre Tanımlamaları Ekranı |  |
| --- | --- |
| Grup Kodu | FATURA |
| Anahtar | FATSERIDEGER |

Alış Parametrelerinde "İade Faturada Tahsilat Ekranı Çıksın" Parametresinin Kullanılması Durumunda; İade Tipli Alış Faturası Kaydında Görüntülenen "Hızlı Tahsilat Kaydı" Ekranının, Tahsilat Bilgisi Girilmeden Kapatılmasının Sağlanması için tanımlanacak özel parametre aşağıdaki şekildedir:

| Özel Parametre Tanımlamaları Ekranı |  |
| --- | --- |
| Grup Kodu | FATURA |
| Anahtar | ALISIADETAHSILSEC |

Özel Hesap Kapatmalı Çalışan Cariye Ait Açık Tipli Satış Fatura Bakiyesinin, Faturada Girilen Tahsilat Tutarı Kadar Kapatılmasının Sağlanması için tanımlanacak özel parametre aşağıdaki şekildedir:

| Özel Parametre Tanımlamaları Ekranı |  |
| --- | --- |
| Grup Kodu | FATURA |
| Anahtar | ACIKFATURAOZELHESAP |

Entegrasyon Kodları - "Fatura Genel" sekmesindeki "Depolar Arası Transfer Entegre" Seçeneği Kullanıldığı Zaman, Ambar Giriş/Çıkış Belgelerinde Çalışacak Olan Muhasebe Hesabının Belirlenmesinin Sağlanması için tanımlanacak özel parametre aşağıdaki şekildedir:

| Özel Parametre Tanımlamaları Ekranı |  |
| --- | --- |
| Grup Kodu | FATURA |
| Anahtar | AMBARHESKODGETIR |

"Depolar Arası Transfer Entegre" seçeneği ile Satış Diğer-3 hesabı çalışırken, özel parametrenin "Değer" alanına yazılan değere göre stokun muhasebe detay kodundaki diğer hesapların da çalıştırılması sağlanır. Satış Diğer 1, 2, ..., 8 hesapları için parametrenin "Değer" alanına 1, 2, ..., 8 , Alış Hesabı için 9, Alıştan İade için 10, Satış Hesabı için 11 ve Satıştan İade Hesabı için de 12 değerinin yazılması gerekir.

Alış İrsaliyesinden Fatura Oluştururken Kalite Kontrol Kaydı Kontrolünün Sağlanması için tanımlanacak özel parametre aşağıdaki şekildedir:

| Özel Parametre Tanımlamaları Ekranı |  |
| --- | --- |
| Grup Kodu | FATURA |
| Anahtar | KALITE_ZORUNLU |

"Ambar Çıkış Fişi" Ekranının "Kalemler" sekmesindeki "Sipariş No" Rehberinde, Siparişe Bağlı Yapılan D.A.T. Miktarlarının Teslimat Olarak Gösterilmemesinin Sağlanması için tanımlanacak özel parametre aşağıdaki şekildedir:

| Özel Parametre Tanımlamaları Ekranı |  |
| --- | --- |
| Grup Kodu | FATURA |
| Anahtar | SIPAMBARREHBER |

"Sipariş bağlantılı Depolar Arası Transfer Kaydında Teslimat Ayrı Takip Edilsin" parametresi ile birlikte kullanılması gerekir.

"e-İrsaliye Uygulamasından" Bağımsız Olarak, "Faturalandırılan İrsaliyeler Saklansın" Parametresinin Kullanılmasının Sağlanması için tanımlanacak özel parametre aşağıdaki şekildedir:

| Özel Parametre Tanımlamaları Ekranı |  |
| --- | --- |
| Grup Kodu | FATURA |
| Anahtar | EIRSALIYESAKLAKONTROL |

Toplu e-İrsaliye Oluşturma Ekranında Yükleme Emri Numarası'nın Görünmesinin Sağlanması için tanımlanacak özel parametre aşağıdaki şekildedir:

| Özel Parametre Tanımlamaları Ekranı |  |
| --- | --- |
| Grup Kodu | FATURA |
| Anahtar | 'SEVKYUKLEME' ,'YUKLEMENO' |

Birden fazla Yükleme Emri Numarası'nın Saklanmasının Sağlanması için tanımlanacak özel parametre aşağıdaki şekildedir:

| Özel Parametre Tanımlamaları Ekranı |  |
| --- | --- |
| Grup Kodu | FATURA |
| Anahtar | 'SEVKYUKLEME','COKLUYUKTEKRARKULLAN' |

e-Fatura Cari Hesapları İçin Ekranda Seçilen Tipte Belgenin Oluşturulmasının Sağlanması için tanımlanacak özel parametre aşağıdaki şekildedir:

| Özel Parametre Tanımlamaları Ekranı |  |
| --- | --- |
| Grup Kodu | EFATURA |
| Anahtar | SEVKBELGESECIM |
