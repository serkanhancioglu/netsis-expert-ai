---
title: "Toplu Ciro Çekleri Ödeme Dekontu"
page_id: "22805832"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Dekont"
  - "Kayıt / Dekont"
  - "Tahsil/Teminat/Ciro Çekleri Ödeme Dekontu"
  - "Toplu Ciro Çekleri Ödeme Dekontu"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Dekont / Kayıt / Dekont / Tahsil/Teminat/Ciro Çekleri Ödeme Dekontu / Toplu Ciro Çekleri Ödeme Dekontu"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTU4ZTFhOGM3LTUwYTctNDkzOS1iZDkyLTc5ZWZhMTJhNzZkMCZsaW5rPTExNzE4MDk2LTg1NmYtNDdiZC05NWEwLWNmNDk3NmQ4ODk4NCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=58e1a8c7-50a7-4939-bd92-79efa12a76d0&link=11718096-856f-47bd-95a0-cf4976d88984&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "toplu-ciro-cekleri-odeme-dekontu_34226532_22805832.html"
source_version: "2022-11-30T10:14:47.433+03:00"
source_bytes: 177944
fetched_at: "2026-09-13T04:09:05+00:00"
generator: "netsis-scraper 1.0.0"
---
# Toplu Ciro Çekleri Ödeme Dekontu

Toplu Ciro Çekleri Ödeme Dekontu, Finans Bölümü'nde, "Kayıt/Dekont" menüsünün altında yer alır.

Toplu Ciro Çekleri Ödeme Dekontu bölümü, sadece müşteri çek alımları ve alınan çeklerin tahsilatı için farklı cari kodlar kullanan firmalar için düzenlendi. Normalde, satıcılara ciro edilen çekleri tahsilatı ile ilgili herhangi bir işlem yapılmasına gerek yok.

Farklı cari kullanımında, müşteri çeklerinin tahsil edilene kadar riskte olduğu düşünülür ve alınan çekler fatura cari hesabına aktarılarak bakiyenin kapanması istenmez. Bu nedenle, çekler müşteriden alındığında, başka bir cari hesap kodu kullanılır. Çekler tahsil edildiğinde, çeki alırken kullanılan cari hesaba borç, verilen alacak cari hesap koduna (fatura cari hesabı) alacak kaydedilir. İki cari kullanımında, alınan çekler bankaya verilmişse bankalardan gelen dekontlar, "Çek Tahsil Dekontu" veya "Toplu Çek Tahsil Dekontu" kullanılarak bu işlemler yapılabilir. Satıcılara ciro edilmiş çeklerde herhangi bir tahsil dekontu dönmediği için, bu işlemin daha önce yapılması mümkün değildi. "Toplu Ciro Çekleri Ödeme Dekontu" bölümü ile, vade tarihi geçmiş ciro çeklerinin fatura cari hesabına aktarılması sağlanır.

![](../../../../../_assets/80b43a9df713f9d57087.png)

Toplu Ciro Çekleri Ödeme Dekontu alanları ve içerdiği bilgiler aşağıdaki şekildedir:

| Toplu Ciro Çekleri Ödeme Dekontu Ekranı |  |
| --- | --- |
| İşlem Tarihi | Yapılan kayıt için baz alınacak tarihin girildiği alandır. Girilen tarih hem cari hem de entegrasyon kayıtlarında kullanılır. |
| Vade Tarihi Aralığı | Yapılan kayıt için baz alınacak vade tarihi aralığının girildiği alandır. |
| Döviz Tipi | Tahsil edilmesi istenen çekler için döviz tipi girilen alandır. Herhangi bir döviz tipi girildiğinde, tahsil edilecek çeklerdeki döviz tipinin, girilen döviz tipi ile eşit olması gerekir. |
| Döviz Kuru | "Döviz Tipi" girildiğinde, döviz kuru varsa otomatik olarak ekrana gelir ve üzerinde değişiklik yapılabilir. Girilen kur, dövizli çekler için kur farkı hesaplanırken kullanılır. |
| Tüm Çekler Getirilsin | Girilen bilgiler doğrultusunda, grid ekrana tüm çeklerin getirilmesi için kullanılan seçenektir. |
| Çek Seri No | Çekin üzerinde yer alan seri numaranın girildiği alandır. |
| Seri Kodu | Daha önce seri kodu tanımlama bölümünden tanımlanan ve ilgili dekont kaydı için kullanılacak olan seri kodunun girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, seri kodları arasından seçim yapılır. |
| Fiş No | İlgili kayda ait fiş numarasının girildiği alandır. |
| Cari Rapor Kodu | Cari → Kayıt → [Cari Parametreleri](<../../../Cari/Kayıt - Cari/Cari Parametreleri.md>) → "Hareketlerde Rapor Kodu Girilsin" parametresinin işaretlenmesi ile aktif hale gelen alandır. Hareketlere aktarılması ve raporlanması amacıyla 1 karakterden oluşan rapor kodu girişi yapılır. |
| Plasiyer Kodu | Yardımcı Programlar → Kayıt → [Şirket-Şube Parametreleri](<../../../../Muhasebe/Muhasebe Modülü/Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/Genel Tanımlar/Yardımcı Programlar-Şirket-Şube Parametreleri.md>) → "Plasiyer Uygulaması Var" parametresinin işaretlenmesi ile aktif hale gelen alandır. Dekont kaydı sırasında ilgili plasiyer kodunun girilmesi gerekir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, plasiyer kodlarına ulaşılır. Boş bırakılmaz. |
| Proje Kodu | Yardımcı Programlar → Kayıt → [Şirket-Şube Parametreleri](<../../../../Muhasebe/Muhasebe Modülü/Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/Genel Tanımlar/Yardımcı Programlar-Şirket-Şube Parametreleri.md>) → "Proje Uygulaması Var" parametresinin işaretlenmesi ile aktif hale gelen alandır. Dekont kaydı sırasında ilgili plasiyer kodunun girilmesi gerekir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, proje kodlarına ulaşılır. Boş bırakılmaz. Girilen proje kodları, cari hareketlere ve entegrasyona aktarılır. |
| Referans Kodu | Muhasebe → Kayıt → [Muhasebe Parametreleri](<../../../../Muhasebe/Muhasebe Modülü/Kayıt - Muhasebe/Muhasebe Parametreleri.md>) → "Fişlerde Referans Kodu Sorulsun" parametresinin işaretlenmesi ile aktif hale gelen alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, referans kodlarına ulaşılır. Boş bırakılmaz. |
| Alacak Cari Kodu | Bazı firmalar çalışma prensipleri gereği, müşterilerden aldığı çekleri ilk kayıt esnasında farklı bir hesaba işler (çekler ödenene kadar riskli olduğu için) ve çek tahsil edildiğinde müşterilerinin asıl hareket kayıtlarına virman yapar. Bu işlemin "Çek Tahsil Dekont Kaydı" sırasında otomatik olarak yapılmasını sağlamak için, dekont ekranında "Alacak Cari Kodu" alanı kullanılır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, cari kodlara ulaşılır. Boş bırakılmaz. Çekin tahsilatı sırasında, **Borç Cari Kodu** alanına otomatik olarak çek alındığında kaydedilen cari kod gelir. Yapılması gereken; çek tahsilatının hangi cari koda **alacak** **hareketi** olarak kaydedilmesi isteniyorsa, ilgili cari kodun **Alacak Cari Kodu** alanına girilmesidir. Böylece; dekont işleminin tamamlanması ile **Borç Cari Kodu** alanına girilen cari koda **borç hareketi** kaydedilerek, çek alımında kaydedilen alacak hareketi kapatılır. **Alacak Cari Kodu** alanına girilen koda **alacak hareketi** kaydedilerek çekin asıl cari harekete yansıtılması sağlanır. Bu tür uygulamaları olmayan firmalar için bu alan kullanılmaz. "Borç Cari Kodu" alanında veren kodundan farklı bir kod belirtilmesi istendiğinde, çek tahsilatının bu bölümden değil önceden olduğu gibi "Çek Tahsil Dekontu" bölümünden yapılması gerekir. Bu dekont adımında, birden fazla cari hesaptan alınan senetler için tahsilat yapılır. Bu sebeple, "Alacak Cari Kodu" alanında cari kod maskesi desteklenir. Maskenin düzgün kullanılması için, açılan cari kodların belli bir standartta olması gerekir. **Örneğin:** A0001, A0002, A0003 şeklindeki kodlarının fatura cari hesapları için A00012, A00022, A00032 şeklindeki kodlarının senet takip cari hesapları için açıldığı varsayıldığında; her üç cari için aynı anda doğru hesaplar çalıştırılarak tahsilat işlemi yapılaması için, "Alacak Cari Kodu" alanına "**?????2**" girilmesi gerekir. Böylece, soru işareti (?) girilen alanlara, çeklerdeki veren kodlar aktarılarak kodun sonuna 2 eklenir. |
| Açıklama | Bu alana program tarafından otomatik olarak başında ? (soru işareti) bulunan bir açıklama aktarılır. Herhangi bir değişiklik yapılmazsa tahsil edilen çek numaraları açıklama alanının başına eklenerek, cari ve entegrasyon kayıtlarına aktarılır. |
| Tamam | Girilen koşullara uygun çeklerin, grid ekranda listelenmesi için kullanılan butondur. |
| Kayıtları Yap | Listelenen çekler içinde tahsil edilecek olanların üzerinde iken fare ile çift tıklanarak, oluşacak kayıtların ilgili modüllere aktarılması için kullanılan butondur. Butona tıklanması ile, ekrana gelen uyarı onaylanarak işlem tamamlanır. ![](../../../../../_assets/895cfbe5158af7609e06.png) |
| ![](../../../../../_assets/ab9047f06dcf17f8b154.png) Hepsini Seç | Grid alana aktarılan tüm satırların seçilmesi için kullanılan butondur. |
| ![](../../../../../_assets/ca4e3e18d9df15206767.png) Hepsini Sil | Grid alanda seçilen satırların tümünün seçimini kaldırmak için kullanılan butondur. |
| İptal | Toplu ciro çekleri ödeme dekontu için girilen kaydın iptal edilmesi için kullanılan butondur. |
