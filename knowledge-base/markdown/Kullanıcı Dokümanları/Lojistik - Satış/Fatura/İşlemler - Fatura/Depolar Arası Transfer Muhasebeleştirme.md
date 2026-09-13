---
title: "Depolar Arası Transfer Muhasebeleştirme"
page_id: "24764257"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Fatura"
  - "İşlemler / Fatura"
  - "Depolar Arası Transfer Muhasebeleştirme"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Fatura / İşlemler / Fatura / Depolar Arası Transfer Muhasebeleştirme"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTE0ZmEyMmI0LWEzY2ItNGU5OS04NTc2LWU3ZWVmZjAyMDhkYSZsaW5rPTc1MGQ4MmIxLWVjNjEtNDU5MS1iZTg0LWIxNjZkOWRmYTcyOSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=14fa22b4-a3cb-4e99-8576-e7eeff0208da&link=750d82b1-ec61-4591-be84-b166d9dfa729&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "depolar-arasi-transfer-muhasebelestirme_24764290_24764257.html"
source_version: "2022-10-24T21:28:58.310+03:00"
source_bytes: 14635
fetched_at: "2026-09-13T04:02:50+00:00"
generator: "netsis-scraper 1.0.0"
---
# Depolar Arası Transfer Muhasebeleştirme

Depolar Arası Transfer Muhasebeleştirme, Lojistik - Satış Bölümü'nde, "İşlemler/Fatura" menüsünün altında yer alır.

Depolar Arası Transfer Muhasebeleştirme, Depolar Arası Transfer modülünden yapılan merkez ve şubeler arası stok transferlerinin ay bazında muhasebeleştirilmesi için kullanılan bölümdür.

Depolar Arası Transfer fişleri bu bölümden muhasebeleştirilecekse, Entegrasyon → Entegrasyon Kodları → Depolar Arası Transfer Entegre parametresi işaretlenmez.

Depolar Arası Transfer Muhasebeleştirme ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Depolar Arası Transfer Muhasebeleştirme Ekranı |  |
| --- | --- |
| Yıl Kodu | Depolar arası transfer hareketlerinin muhasebeleştirileceği yıl kodunun girildiği bölümdür. |
| Ay Kodu | Depolar arası transfer hareketlerinin muhasebeleştirileceği ay kodunun girildiği bölümdür. |
| Hammadde-Ambalaj-Ticari Mal | Sadece, Stok Kartı Kayıtları → Ek Bilgiler → Türü alanındaki hammadde, ambalaj veya ticari mal seçilmiş stoklara ait transfer belgelerinin muhasebeleşmesi için işaretlenen seçenektir. |
| Mamul-Yarı Mamul-Yan Ürün | Sadece, Stok Kartı Kayıtları → Ek Bilgiler → Türü alanındaki mamul, yarı mamul ya da yan ürün seçilmiş stoklara ait transfer belgelerinin muhasebeleşmesi için işaretlenen seçenektir. |
| Hepsi | Stok Kartı Kayıtları → Ek Bilgiler → Türü alanında yapılan seçime bakılmaksızın, tüm stoklara ait transfer belgelerinin muhasebeleşmesi için işaretlenen seçenektir. |
| Detaylı/Kümüle | **Kümüle** seçeneğinin işaretlenmesi durumunda ilgili ay içinde farklı fişlerde bulunan stok hareketleri, stok kodu bazında kümüle edilerek muhasebeleştirilir. **Detaylı** seçeneği işaretlendiğinde ise, her stok için ayrı ayrı muhasebeleştirme işlemi yapılır. |
| Muhtelif Tipli Hareketler Dahil Edilsin | Depolar arası transfer modülünden "Muhtelif Tipi" seçilerek yapılan kayıtların muhasebeleştirilmesi için işaretlenmesi gereken parametredir. Parametrenin işaretlenmemesi durumunda sadece “Depolar Tipi" ile yapılan kayıtlar dikkate alınır. |
| Entegrasyon Bilgileri Merkezde Oluşturulsun | Merkez ile şubeler arasında yapılan depolar arası transfer işlemlerine ait tüm kayıtların, merkez entegrasyon havuzunda oluşması için işaretlenmesi gereken parametredir. Parametrenin işaretlenmemesi durumunda, merkezden şubeye yapılacak transferlerde, çıkış hesapları merkezin entegrasyon havuzunda, giriş hesapları ise şubenin entegrasyon havuzunda yer alır. |
| Fark/Transfer Muhasebe Kodu | Transfer yapılacak stokların giriş hareketlerinde borç çalışacak muhasebe hesabının kodudur. Girilen hesabın açıklaması, entegrasyon havuzunda (aktarım yapılan ayın son gününde) “Depolar Arası Transfer Farkı" olarak yer alır. ![](../../../../_assets/088477bb321d1b20c939.jpg) Rehber butonu yardımı ile muhasebe kodları arasından seçim yapılır. |
| Çıkış Hesap Tipi | Transfer yapılacak stoklar için çıkış hareketlerinde alacak çalışacak muhasebe hesabının seçildiği alandır. Stok modülü → Muhasebe Detay Kod girişinden tanımlanan alış hesabı, satış hesabı, satış diğer 1/2/3 hesaplarından biri seçilir. |
| Alış Hesap Tipi | Alış hesabı olarak çalışacak muhasebe hesabının seçildiği alandır. Stok modülü → Muhasebe Detay Kod girişinden tanımlanan alış hesabı, satış hesabı, satış diğer 1/2/3 hesaplarından biri seçilir. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Depolar arası transferlerin, ay bazında muhasebeleştirme işlemini gerçekleştirmek için kullanılan butondur. |
| ![](../../../../_assets/21b5276f2871a4221e55.png) Çıkış | Depolar arası transferlerin, ay bazında muhasebeleştirme işlemini gerçekleştirmekten vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
