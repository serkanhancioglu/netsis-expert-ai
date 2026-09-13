---
title: "Bağlantı - Sipariş Kayıtları"
page_id: "22803704"
product: "netsis-3-enterprise"
depth: 5
is_section: true
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Cari"
  - "Kayıt / Cari"
  - "Bağlantı - Sipariş Kayıtları"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Cari / Kayıt / Cari / Bağlantı - Sipariş Kayıtları"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWRhNThhM2Q3LWFmMDUtNDRhYy05NDA0LTdiMDY4Y2I4YTljNSZsaW5rPTk3NGE3ZjEyLWRkZTAtNGY4ZS05YzRmLTAxMWYzZTIxMjU1MyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=da58a3d7-af05-44ac-9404-7b068cb8a9c5&link=974a7f12-dde0-4f8e-9c4f-011f3e212553&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "baglanti-siparis-kayitlari_28154646_22803704.html"
source_version: "2022-10-27T10:12:49.090+03:00"
source_bytes: 4740
fetched_at: "2026-09-13T04:07:36+00:00"
generator: "netsis-scraper 1.0.0"
---
# Bağlantı - Sipariş Kayıtları

Bağlantı Sipariş Kayıtları, Finans Bölümü'nde Kayıt/Cari menüsünün altında yer alır. Müşteri/satıcı ile yapılan bağlantı anlaşmalarının takip edilmesi için kullanılan bölümdür.

Bağlantı Sipariş Kayıtlarındaki takip; bağlantıdan doğan cari hesap (tahsilat/ödeme ) takibi ve bağlantı ile belirlenen tutar, fiyat, iskonto gibi koşulların sistem tarafından denetlenmesinin sağlanması olmak üzere iki şekilde sağlanır.

Sipariş cari hesap takip sistemi ise, sipariş bazında tahsilât/ödeme takibinin yapılmasını sağlar.

Her iki uygulamada da, benzer cari hesap takip sistemi bulunur. Bağlantı uygulamalarına örnek verilecek olursa; özellikle fiyat zamlarında, eski fiyattan belli ürün grubunda ve tutarda anlaşma yapılır ve bunun karşılığında müşteri, anlaşılan vadede ödeme yapar. Bu uygulamada iki problem söz konusudur. İlki bağlantının tamamlanıp tamamlanmadığı, ikincisi de anlaşma şartlarında ödeme yapılıp yapılmadığıdır. Bağlantı/Sipariş Kayıtları uygulaması bu iki durum için de kullanılabilir. Sipariş uygulamasını daha detaylı örneklemek gerekirse, bazı sektörlerde tahsilat için esas belge sipariş olup, fatura sadece iş bitiminde kesilen belge niteliğini taşır. Dolayısı ile sipariş kaydı tahsilat/ödeme için baz alınır ve cari hesap takibi açısından faturalar bir şey ifade etmez. Bağlantı/sipariş takibinin yapılması için ilk olarak, bu uygulamada kullanılacak cari kartların açılması gerekir. Hem bağlantı hem de sipariş takibinde, cari kartlardan bir ana kod tanımlaması yapmak gerekir.

**Örneğin:** NETSISANA. Bağlantı ve sipariş tanımlaması yapılırken, tanımlanan ana kodlara bağlı olarak alt kodlar sorgulanır. Alt kodların sorgulanma sebebi, faturaların kesileceği cari kodun ve tahsilatların yapılacağı cari kodun ayrı takip edilmesinden kaynaklanır. Bu nedenle cari hesap kayıtlarından, fatura takibi ve tahsilat takibi için ayrı cari kodlar tanımlanması gerekir.

**Örneğin:** NETSISBF (bağlantı fatura hesabı), NETSISBC (bağlantı cari hesabı) gibi. Aynı mantıkla bağlantı harici sipariş takibi yapılması istendiğinde de cari kod tanımlamaları yapılır. NETSISSF (sipariş fatura hesabı), NETSISSC (sipariş cari hesabı) Tanımlanan bu alt kodlar için muhasebe kodu olarak sipariş avansları hesap kodlarının kullanılması tavsiye edilir. Cari hesap kayıtlarının tamamlanmasından sonra, bağlantı kayıtlarının tanımlamasına geçilir. Tahsilatların takip edileceği bağlantı cari hesap kodlarında (NETSISBC, NETSISSC), Hesap Tipi olarak **Özel Hesap Kapatma** kullanılması tavsiye edilir.
