---
title: "Ek-2 (Fason Uygulaması)"
page_id: "24752313"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Muhasebe"
  - "Maliyet Muhasebesi"
  - "Ekler / Maliyet Muhasebesi"
  - "Ek-2 (Fason Uygulaması)"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Maliyet Muhasebesi / Ekler / Maliyet Muhasebesi / Ek-2 (Fason Uygulaması)"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWNkYmMyOTVjLTkyNGUtNDAxNC04ZDkzLTE4MDc2N2RmMmZiMSZsaW5rPTY2NzllMDgzLTI0NTktNDIyOS1iMmQ5LWRkY2I2MTRiZTk0ZiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=cdbc295c-924e-4014-8d93-180767df2fb1&link=6679e083-2459-4229-b2d9-ddcb614be94f&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ek-2-fason-uygulamasi_50678066_24752313.html"
source_version: "2022-12-02T15:08:33.010+03:00"
source_bytes: 5486
fetched_at: "2026-09-13T04:15:17+00:00"
generator: "netsis-scraper 1.0.0"
---
# Ek-2 (Fason Uygulaması)

Fason uygulaması, üretim yapan firmaların fason işçilik giderlerinin, direkt olarak mamul/yarı mamul maliyetlerine yansıtılması için kullanılır. Bu uygulamanın başlatılması için programda bazı düzenlemeler yapmak gerekir. Fason uygulamasında maliyetler hakkında ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Öncelikle, fason işçiliklerin takip edileceği yeni stok kartlarının açılması gerekir. Bu kartlarda, Stok Kartı Kayıtları → Ek Bilgiler → Türü alanında yer alan "Fason" seçeneğinin işaretlenmesi gerekir. Fason kartları için açılacak detay kodlarında, gider hesap kodlarından olan 730 hesapların tanımlanması gerekir.

Maliyet Muhasebesi modülünde ise Maliyet Muhasebesi Parametreleri → Maliyet Parametreleri-2 sekmesinden tanımlanabilir. 5 gider tanımından birine **DETAYLI FASON** isminin yazılması gerekir. Maliyet işlemlerinde "Fason" işçiliklerin dikkate alınması için Mamul Ana Grup Kodu tanımlamasında, fason işçilikle ilgili herhangi bir muhasebe kodunun girilmemesi gerekir. Mamul Grup Kodu tanımlamalarında ise, yansıtma hesaplarında **DETAYLI FASON** için 731 yansıtma hesap kodunun girilmesi gerekir.

Stok sabit kayıtlarında, Türü alanı "Fason" olarak işaretlenen kartlarda, Fatura modülünde sadece alış işlemlerine - Satıcı Siparişleri, Alış İrsaliyeleri, Alış Faturaları- ve satış işlemlerinde de sadece iade işlemine izin verilir. Bunun dışındaki Fatura modülü işlemlerinde, fason olarak tanımlanmış kartla ilgili satış işlemi yapılması istenirse, “fason malın satışı olamaz. Sadece iade edilebilir.” şeklinde bir uyarı verilerek izin verilmez. Aynı şekilde, fason olarak tanımlanmış bir kartla ilgili alış iade işlemi yapılması istenirse “Fason stokun alış iadesi yapılamaz.” uyarısı verilerek işleme izin verilmez. Bu uyarılar, fason işçilik satışının ve satılmayan işçiliğin iadesinin olamayacağı düşünülerek verilir.

Fason işçilik faturalarının, alış faturalarından kaydedildiği sırada hangi mamul/yarı mamule ait bir işçilik gideri olduğunun anlaşılması için Maliyet Grup Kodu - Maliyet Muhasebesi → Mamul Grup Kodu Kaydı bölümünden kaydedilen - satır bazında sorgulaması yapılır. Girilen maliyet grup kodları stok hareket dosyasında, Muhasebe Kodu sahasında saklanır. Maliyet Muhasebesi işlemleri sırasında işçilik giderleri, Muhasebe Kodu alanındaki mamul grup koduna göre, direkt ilgili mamul/yarı mamulün tanımlı fason giderlerine yazılır.

Eğer, bir mamul/yarı mamul tamamen fason olarak üretilmişse, fason alış girişlerinde hem miktar hem de fiyat girilmesi gerekir. Bu durumda, girilen miktarlar Maliyet Muhasebesi'nde fason miktar olarak kabul edilir ve maliyetlerin paylaştırılması sırasında, üretim miktarından fason miktarlar düşülerek hesaplama yapılır.

Eğer, üretimin bir kısmı için fason işçilik gideri ödenmişse, fason girişlerinde miktarsız maliyet kaydı yapılarak kayıtların girilmesi gerekir.

Bu uygulamayı kullanan firmalarda, fason işçilik giderlerinin tanımlı olduğu kartlardaki tutarlar ile muhasebe modülü 730 hesap tutarlarının tutması gerekir.

Maliyet işlemlerinin tamamlanmasından sonra, Maliyet Muhasebesi'nden üretim miktarı ve fason miktarının kontrol edilmesi gerekir. Fason miktarının üretim miktarından büyük olmaması gerekir.
