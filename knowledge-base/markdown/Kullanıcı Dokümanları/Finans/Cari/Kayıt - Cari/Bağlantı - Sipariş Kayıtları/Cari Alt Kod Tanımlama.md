---
title: "Cari Alt Kod Tanımlama"
page_id: "22803697"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Cari"
  - "Kayıt / Cari"
  - "Bağlantı - Sipariş Kayıtları"
  - "Cari Alt Kod Tanımlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Cari / Kayıt / Cari / Bağlantı - Sipariş Kayıtları / Cari Alt Kod Tanımlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTM3YTFmNjI5LTNkYjktNGY1OS04YTU0LWI5ZmU2MTI1NTEyZCZsaW5rPWFlMmNiMTFlLWUwNDgtNDhlOC1hNTY4LTFhYTBjMTgwOTk0OSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=37a1f629-3db9-4f59-8a54-b9fe6125512d&link=ae2cb11e-e048-48e8-a568-1aa0c1809949&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "cari-alt-kod-tanimlama_28154665_22803697.html"
source_version: "2022-10-27T10:18:40.063+03:00"
source_bytes: 10813
fetched_at: "2026-09-13T04:07:37+00:00"
generator: "netsis-scraper 1.0.0"
---
# Cari Alt Kod Tanımlama

Cari Alt Kod Tanımlama, Finans Bölümü'nde Kayıt/Cari menüsünün altında yer alır. Cari Alt Kod Tanımlama, Bir firmanın yapmış olduğu bağlantıların/siparişlerin takibi için cari hesap kayıtları bölümünden açılan ana kod ile yine cari hesap kayıtları bölümünden açılan alt kodların bağlantılarının yapılmasını sağlayan bölümdür. Ana kodun fatura takibinin ve tahsilatlarının hangi cari kodda takip edileceği bu bölümde belirlenir. Hem bağlantı hem de sipariş kayıtlarının alt kod tanımlamasında kullanılır.

Cari alt kod tanımlaması yapmadan, bağlantı kayıtlarının oluşturulması mümkün değildir.

Cari Alt Kod Tanımlama ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Cari Alt Kod Tanımlama Ekranı |  |
| --- | --- |
| Cari Ana Kodu | Alt kodları tanımlanacak ana kodun girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, kodlar arasından seçim yapılabilir. Örneğin; NETSISANA. |
| İşlem (Bağlantı/Sipariş) | Yapılan tanımlamanın işlem cinsinin belirlendiği alandır. Bağlantı takibi için (alt kod tanımlaması yapılıyorsa) "Bağlantı", sipariş takibi için (alt kod tanımlaması yapılıyorsa) "Sipariş" seçeneği seçilir. Alanın sağ tarafında yer alan aşağı ok butonu ile işlem cinsi seçilir. |
| Cari Alt Kodu | Ana koda bağlı ilk alt kodun girildiği alandır. Cari hesap kayıtları bölümünden tanımlanan, bağlantı/sipariş için fatura takip kodunun veya cari hesap takip kodunun girilmesi gerekir. İşlem alanında "Bağlantı" seçeneği seçilmişse, bağlantılar için açılan cari kodlar, "Sipariş" seçeneği seçilmişse siparişler için açılan cari kodlar girilir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, kodlar arasından seçim yapılabilir. |
| Tip/Kullanım Yeri(Bağ.Fat.Kontrol Hs./ Bağlantı Ch.) | "Cari Alt Kod" alanına girilen cari kodun hangi işlemler için kullanılacağının belirlendiği alandır. "Cari Alt Kod" alanına girilen kod, faturaların takip edileceği kod ise, "**Bağlantı/Sipariş Fatura Kontrol Hesabı**" seçilir. Eğer, alt kod olarak girilen cari kod, tahsilatların takip edileceği kod ise, **"Bağlantı/Sipariş Cari Hesabı"** seçilir. Bu şekilde alt kod tanımlamalarının yapılması ile bağlantı/sipariş kayıtları sırasında program, fatura kayıtları (sipariş/irsaliye/fatura) için hangi cari kodun, tahsilat işlemleri (Senet/çek/kasa/dekont) için hangi cari kodun kullanılacağını saptar ve kontrollerini ona göre yapar. **Örneğin:** Tahsilatlar için açılan cari kodun fatura kayıtlarında kullanılmasına izin vermez. |
| ![](../../../../../_assets/d3e8345fcb9816ffca37.png) Yeni Altkod Kayıt | Bir ana koda ait alt kod tanımlamasının bitirilmesinden sonra ekranın temizlenerek yeni tanımlamalara hazır hale getirilmesi için kullanılan butondur. |
| ![](../../../../../_assets/9ea037c46d02a3a7bf96.png) Altkod İptal | Bir ana koda ait tanımlanmış olan alt kodların iptali için kullanılan butondur. Ana kodu yazılarak ekrana çağrılan bütün alt kodlar iptal edilir. |
