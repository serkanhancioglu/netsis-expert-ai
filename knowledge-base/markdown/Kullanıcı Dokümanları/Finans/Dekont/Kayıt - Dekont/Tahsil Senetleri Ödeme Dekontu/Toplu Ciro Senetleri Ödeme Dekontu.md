---
title: "Toplu Ciro Senetleri Ödeme Dekontu"
page_id: "22805814"
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
  - "Tahsil Senetleri Ödeme Dekontu"
  - "Toplu Ciro Senetleri Ödeme Dekontu"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Dekont / Kayıt / Dekont / Tahsil Senetleri Ödeme Dekontu / Toplu Ciro Senetleri Ödeme Dekontu"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTUzZjkxY2U5LWQwOTctNGM1Zi05YjkzLWRkODgyMDM1MDQyZCZsaW5rPTZmMWNiYWNjLWRjNjUtNDcxZi1hZGVmLTUwMmJhNzMyODlkMSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=53f91ce9-d097-4c5f-9b93-dd882035042d&link=6f1cbacc-dc65-471f-adef-502ba73289d1&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "toplu-ciro-senetleri-odeme-dekontu_34226381_22805814.html"
source_version: "2022-11-30T10:03:54.220+03:00"
source_bytes: 72215
fetched_at: "2026-09-13T04:09:00+00:00"
generator: "netsis-scraper 1.0.0"
---
# Toplu Ciro Senetleri Ödeme Dekontu

Toplu Ciro Senetleri Ödeme Dekontu, Finans Bölümü'nde, "Kayıt/Dekont" menüsünün altında yer alır.

Toplu Ciro Senetleri Ödeme Dekontu bölümü, sadece müşteri senet alımları ve alınan senetlerin tahsilatı için farklı cari kodlar kullanan firmalar için düzenlendi. Normalde, satıcılara ciro edilen senetlerin tahsilatı ile ilgili herhangi bir işlem yapılmasına gerek yok.

Farklı cari kullanımında, müşteri senetlerinin tahsil edilene kadar riskte olduğu düşünülür ve alınan senetler fatura cari hesabına aktarılarak bakiyenin kapanması istenmez. Bu nedenle, senetler müşteriden alındığında, başka bir cari hesap kodu kullanılır. Senetler tahsil edildiğinde, senedi alırken kullanılan cari hesaba borç, verilen alacak cari hesap koduna (fatura cari hesabı) alacak kaydedilir. İki cari kullanımında, alınan senetler bankaya verilmişse bankalardan gelen dekontlar, "Senet Tahsil Dekontu" veya "Toplu Senet Tahsil Dekontu" kullanılarak bu işlemler yapılabilir. Satıcılara ciro edilmiş senetlerde herhangi bir tahsil dekontu dönmediği için, bu işlemin daha önce yapılması mümkün değildi. Programa eklenen "Toplu Ciro Senetleri Ödeme Dekontu" bölümü ile, vade tarihi geçmiş ciro senetlerinin fatura cari hesabına aktarılması sağlanır.

![](../../../../../_assets/9590f31a462c6897672a.png)

Toplu Ciro Senetleri Ödeme Dekontu alanları ve içerdiği bilgiler aşağıdaki şekildedir:

| Toplu Ciro Senetleri Ödeme Dekontu Ekranı |  |
| --- | --- |
| İşlem Tarihi | Yapılan kayıt için baz alınacak tarihin girildiği alandır. Girilen tarih hem cari hem de entegrasyon kayıtlarında kullanılır. |
| Vade Tarihi Aralığı | Yapılan kayıt için baz alınacak vade tarihi aralığının girildiği alandır. |
| Tüm Senetler Getirilsin | Girilen bilgiler doğrultusunda, grid ekrana tüm senetlerin getirilmesi için kullanılan seçenektir. |
| Döviz Tipi | Tahsil edilmesi istenen senetler için döviz tipi girilen alandır. Herhangi bir döviz tipi girildiğinde, tahsil edilecek sentlerdeki döviz tipinin, girilen döviz tipi ile eşit olması gerekir. |
| Döviz Kuru | "Döviz Tipi" girildiğinde, döviz kuru varsa otomatik olarak ekrana gelir ve üzerinde değişiklik yapılabilir. Girilen kur, dövizli senetler için kur farkı hesaplanırken kullanılır. |
| Seri Kodu | Daha önce seri kodu tanımlama bölümünden tanımlanan ve ilgili dekont kaydı için kullanılacak olan seri kodunun girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, seri kodları arasından seçim yapılır. |
| Fiş No | İlgili kayda ait fiş numarasının girildiği alandır. |
| Cari Rapor Kodu | Cari → Kayıt → [Cari Parametreleri](<../../../Cari/Kayıt - Cari/Cari Parametreleri.md>) → "Hareketlerde Rapor Kodu Girilsin" parametresinin işaretlenmesi ile aktif hale gelen alandır. Hareketlere aktarılması ve raporlanması amacıyla 1 karakterden oluşan rapor kodu girişi yapılır. |
| Plasiyer Kodu | Yardımcı Programlar → Kayıt → [Şirket-Şube Parametreleri](<../../../../Muhasebe/Muhasebe Modülü/Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/Genel Tanımlar/Yardımcı Programlar-Şirket-Şube Parametreleri.md>) → "Plasiyer Uygulaması Var" parametresinin işaretlenmesi ile aktif hale gelen alandır. Dekont kaydı sırasında ilgili plasiyer kodunun girilmesi gerekir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, plasiyer kodlarına ulaşılır. Boş bırakılmaz. |
| Proje Kodu | Yardımcı Programlar → Kayıt → [Şirket-Şube Parametreleri](<../../../../Muhasebe/Muhasebe Modülü/Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/Genel Tanımlar/Yardımcı Programlar-Şirket-Şube Parametreleri.md>) → "Proje Uygulaması Var" parametresinin işaretlenmesi ile aktif hale gelen alandır. Dekont kaydı sırasında ilgili plasiyer kodunun girilmesi gerekir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, proje kodlarına ulaşılır. Boş bırakılmaz. Girilen proje kodları, cari hareketlere ve entegrasyona aktarılır. |
| Referans Kodu | Muhasebe → Kayıt → [Muhasebe Parametreleri](<../../../../Muhasebe/Muhasebe Modülü/Kayıt - Muhasebe/Muhasebe Parametreleri.md>) → "Fişlerde Referans Kodu Sorulsun" parametresinin işaretlenmesi ile aktif hale gelen alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, referans kodlarına ulaşılır. Boş bırakılmaz. |
| Alacak Cari Kodu | Tahsilatı yapılan senetler için "Alacak Cari Kodu" girilen alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, cari kodlara ulaşılır. Boş bırakılmaz. Bu dekont adımında, birden fazla cari hesaptan alınan senetler için tahsilat yapılır. Bu sebeple, "Alacak Cari Kodu" alanında cari kod maskesi desteklenir. Maskenin düzgün kullanılması için, açılan cari kodların belli bir standartta olması gerekir. **Örneğin:** A0001, A0002, A0003 şeklindeki kodlarının fatura cari hesapları için A00012, A00022, A00032 şeklindeki kodlarının senet takip cari hesapları için açıldığı varsayıldığında; her üç cari için aynı anda doğru hesaplar çalıştırılarak tahsilat işlemi yapılaması için, "Alacak Cari Kodu" alanına "**?????2**" girilmesi gerekir. Böylece, soru işareti (?) girilen alanlara, senetlerdeki veren kodlar aktarılarak kodun sonuna 2 eklenir. Senedin tahsilatı sırasında, **Borç Cari Kodu** alanına otomatik olarak senet alındığında kaydedilen cari kod gelir. Yapılması gereken; senet tahsilatının hangi cari koda **alacak** **hareketi** olarak kaydedilmesi isteniyorsa, ilgili cari kodun **Alacak Cari Kodu** alanına girilmesidir. Böylece; dekont işleminin tamamlanması ile **Borç Cari Kodu** alanına girilen cari koda **borç hareketi** kaydedilerek, senet alımında kaydedilen alacak hareketi kapatılır. **Alacak Cari Kodu** alanına girilen koda **alacak hareketi** kaydedilerek senedin asıl cari harekete yansıtılması sağlanır. |
| Açıklama | Bu alana program tarafından otomatik olarak başında ? (soru işareti) bulunan bir açıklama aktarılır. Herhangi bir değişiklik yapılmazsa tahsil edilen senet numaraları açıklama alanının başına eklenerek, cari ve entegrasyon kayıtlarına aktarılır. |
| **![](../../../../../_assets/39d77b8716226638d9ce.jpg)**Tamam | Girilen koşullara uygun senetlerin, grid ekranda listelenmesi için kullanılan butondur. |
| ![](../../../../../_assets/6774caf5b4c523cda5fc.png) Kayıtları Yap | Listelenen senetler içinde tahsil edilecek olanların üzerinde iken fare ile çift tıklanarak, oluşacak kayıtların ilgili modüllere aktarılması için kullanılan butondur. Butona tıklanması ile, ekrana gelen uyarı onaylanarak işlem tamamlanır. ![](../../../../../_assets/895cfbe5158af7609e06.png) |
| ![](../../../../../_assets/ab9047f06dcf17f8b154.png) Hepsini Ekle | Grid alana aktarılan tüm satırların seçilmesi için kullanılan butondur. |
| ![](../../../../../_assets/ca4e3e18d9df15206767.png) Hepsini Çıkar | Grid alanda seçilen satırların tümünün seçimini kaldırmak için kullanılan butondur. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) İptal | Toplu ciro senetleri ödeme dekontu için girilen kaydın iptal edilmesi için kullanılan butondur. |
