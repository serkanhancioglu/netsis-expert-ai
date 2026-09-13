---
title: "Toplu Borç Çeki Ödentisi"
page_id: "22805861"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Dekont"
  - "Kayıt / Dekont"
  - "Toplu Borç Çeki Ödentisi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Dekont / Kayıt / Dekont / Toplu Borç Çeki Ödentisi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTlmNWI0MmU0LTkzNjMtNDBjZC04NWY2LTJkYzNlNjM5NzNiNyZsaW5rPTMxNDhkMzVkLTllOTItNDI0Yi05N2NjLTQ5ODc5ZWVmNzAxZiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=9f5b42e4-9363-40cd-85f6-2dc3e63973b7&link=3148d35d-9e92-424b-97cc-49879eef701f&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "toplu-borc-ceki-odentisi_34229033_22805861.html"
source_version: "2022-11-30T13:34:43.583+03:00"
source_bytes: 73420
fetched_at: "2026-09-13T04:09:11+00:00"
generator: "netsis-scraper 1.0.0"
---
# Toplu Borç Çeki Ödentisi

Toplu Borç Çeki Ödentisi, Finans Bölümü'nde, "Kayıt/Dekont" menüsünün altında yer alır. Toplu Borç Çeki Ödentisi, Tedarikçi firmalara ciro edilen ve aynı tarihte ödenen birden fazla borç çekinin ödeme kaydının oluşturulmasını sağlayan bölümdür.

| Toplu Borç Çeki Ödentisi Ekranı |  |
| --- | --- |
| Seri Kodu | Girilen dekontun seri numarasının kaydedildiği alandır. Boş bırakılmaz. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, seri kodlarına ulaşılır. |
| Fiş No | Toplu borç çeki ödenti kaydı için fiş numarası girilen alandır. Bu alana girilen numara Muhasebe Entegrasyonu ve Cari Hareket Kayıtları bölümlerinde yer alan "Fiş No" alanına aktarılır. |
| İşlem Tarihi | Toplu borç çeki ödenti kaydının girildiği tarihtir. Yapılacak işlem sonucu oluşacak kayıtlar ,diğer modüllere (Banka-Entegrasyon-Senet) bu tarih ile kaydedilir. |
| Vade Tarihi | Toplu borç çeki ödenti kaydı için vade tarihi girilen alandır. |
| Döviz Tipi/Döviz Kuru | Ödenecek çekler döviz tipi girilen alandır. Herhangi bir döviz tipi girildiğinde, ödenecek çeklerdeki döviz tipinin, girilen döviz tipi ile eşit olması gerekir. Döviz tipi girildiğinde, döviz kuru var ise otomatik olarak gelir ve üzerinde değişiklik yapılabilir. Girilen kur, dövizli çekler için kur farkı hesaplanmasında kullanılır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, döviz tiplerine ulaşılır. |
| Proje Kodu | Toplu borç çeki ödenti kaydı için proje kodu girilen alandır. Ödeme dekontuna, bu alana girilen proje kodunun aktarılması sağlanır. |
| Çekin Bankası | Çekin verildiği bankaya ait kod bilgisinin girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, banka kodlarına ulaşılır. |
| Plasiyer Kodu | Yardımcı Programlar → Kayıt → [Şirket-Şube Parametreleri](<../../../Muhasebe/Muhasebe Modülü/Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/Genel Tanımlar/Yardımcı Programlar-Şirket-Şube Parametreleri.md>) → "Plasiyer Uygulaması Var" parametresinin işaretlenmesi ile aktif hale gelen alandır. Dekont kaydı sırasında ilgili plasiyer kodunun girilmesi gerekir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, plasiyer kodlarına ulaşılır. Boş bırakılmaz. |
| Cari Rapor Kodu | Cari → Kayıt → [Cari Parametreleri](<../../Cari/Kayıt - Cari/Cari Parametreleri.md>) → "Hareketlerde Rapor Kodu Girilsin" parametresinin işaretlenmesi ile aktif hale gelen alandır. Hareketlere aktarılması ve raporlanması amacıyla 1 karakterden oluşan rapor kodu girişi yapılır. |
| Cari/Muhasebe/Banka | Çek tutarının alacak olarak kaydedileceği hesabın seçildiği alandır. Cari, Muhasebe ve Banka olmak üzere üç seçenekten oluşur. Muhasebe seçildiğinde; program muhasebe kodu sorgular ve çek tutarını, girilen muhasebe koduna alacak olarak kaydeder. Banka seçildiğinde; program banka kodu sorgular ve çek tutarını, girilen banka koduna alacak olarak kaydeder. Cari seçildiğinde ise; program cari kod sorgular ve çek tutarını, girilen cari koda alacak olarak kaydeder. |
| Banka No | Çekler için ödeme işleminin yapıldığı banka kodunun girildiği alandır. |
| Açıklama | Bu alana açıklama olarak “?? NOLU ÇEK ÖDE.” program tarafından otomatik olarak aktarılır. Kullanıcı tarafından değişiklik yapılabilir. |
| **![](../../../../_assets/39d77b8716226638d9ce.jpg)** Tamam | Girilen koşullara uygun çeklerin grid ekranda listelenmesi için kullanılan butondur. |
| ![](../../../../_assets/6774caf5b4c523cda5fc.png) Kayıtları Yap | Listelenen çekler içinde tahsil edilecek olanların üzerinde iken fare ile çift tıklanarak, oluşacak kayıtların ilgili modüllere aktarılması için kullanılan butondur. Butona tıklanması ile, ekrana gelen uyarı onaylanarak işlem tamamlanır. ![](../../../../_assets/d0aebd89ae472e694a6a.png) |
| ![](../../../../_assets/ab9047f06dcf17f8b154.png) Hepsini Seç | Grid alana aktarılan tüm satırların seçilmesi için kullanılan butondur. |
| ![](../../../../_assets/ca4e3e18d9df15206767.png) Hepsini Çıkar | Grid alanda seçilen satırların tümünün seçimini kaldırmak için kullanılan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Toplu borç çeki ödentisi için girilen kaydın iptal edilmesi için kullanılan butondur. |
