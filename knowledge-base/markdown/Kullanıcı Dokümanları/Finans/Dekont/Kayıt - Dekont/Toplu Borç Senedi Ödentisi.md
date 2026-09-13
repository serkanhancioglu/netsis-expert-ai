---
title: "Toplu Borç Senedi Ödentisi"
page_id: "22805866"
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
  - "Toplu Borç Senedi Ödentisi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Dekont / Kayıt / Dekont / Toplu Borç Senedi Ödentisi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTI5NDQ2NDk1LTk3MGYtNGEzZi1iNjE5LWVlNzJiMzllMzIzZiZsaW5rPTY2YmEwOGZjLTM1MzgtNGY4MC04Yjc2LWI3OTM2OWMxMzdkOCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=29446495-970f-4a3f-b619-ee72b39e323f&link=66ba08fc-3538-4f80-8b76-b79369c137d8&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "toplu-borc-senedi-odentisi_34229045_22805866.html"
source_version: "2022-11-30T13:39:55.160+03:00"
source_bytes: 226480
fetched_at: "2026-09-13T04:09:11+00:00"
generator: "netsis-scraper 1.0.0"
---
# Toplu Borç Senedi Ödentisi

Toplu Borç Senedi Ödentisi, Finans Bölümü'nde, "Kayıt/Dekont" menüsünün altında yer alır. Toplu Borç Senedi Ödentisi, tedarikçi firmalara ciro edilen ve aynı tarihte ödenen birden fazla borç senedinin ödeme kaydının oluşturulmasını sağlayan bölümdür.

![](../../../../_assets/5668404735410688c2d0.png)

Toplu Borç Senedi Ödentisi alanları ve içerdiği bilgiler aşağıdaki şekildedir:

| Toplu Borç Senedi Ödentisi Ekranı |  |
| --- | --- |
| Seri Kodu | Girilen dekontun seri numarasının kaydedildiği alandır. Boş bırakılmaz. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, seri kodlarına ulaşılır. |
| Fiş No | Toplu borç senedi ödenti kaydı için fiş numarası girilen alandır. Bu alana girilen numara Muhasebe Entegrasyonu ve Cari Hareket Kayıtları bölümlerinde yer alan "Fiş No" alanına aktarılır. |
| İşlem Tarihi | Toplu borç senedi ödenti kaydının girildiği tarihtir. Yapılacak işlem sonucu oluşacak kayıtlar ,diğer modüllere (Banka-Entegrasyon-Senet) bu tarih ile kaydedilir. |
| Vade Tarihi | Toplu borç senedi ödenti kaydı için vade tarihi girilen alandır. |
| Döviz Tipi/Döviz Kuru | Ödenecek senet için döviz tipi girilen alandır. Herhangi bir döviz tipi girildiğinde, ödenecek senetlerdeki döviz tipinin, girilen döviz tipi ile eşit olması gerekir. Döviz tipi girildiğinde, döviz kuru var ise otomatik olarak gelir ve üzerinde değişiklik yapılabilir. Girilen kur, dövizli senetler için kur farkı hesaplanmasında kullanılır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, döviz tiplerine ulaşılır. |
| Plasiyer Kodu | Yardımcı Programlar → Kayıt → [Şirket-Şube Parametreleri](<../../../Muhasebe/Muhasebe Modülü/Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/Genel Tanımlar/Yardımcı Programlar-Şirket-Şube Parametreleri.md>) → "Plasiyer Uygulaması Var" parametresinin işaretlenmesi ile aktif hale gelen alandır. Dekont kaydı sırasında ilgili plasiyer kodunun girilmesi gerekir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, plasiyer kodlarına ulaşılır. Boş bırakılmaz. |
| Cari Rapor Kodu | Cari → Kayıt → [Cari Parametreleri](<../../Cari/Kayıt - Cari/Cari Parametreleri.md>) → "Hareketlerde Rapor Kodu Girilsin" parametresinin işaretlenmesi ile aktif hale gelen alandır. Hareketlere aktarılması ve raporlanması amacıyla 1 karakterden oluşan rapor kodu girişi yapılır. |
| Cari/Muhasebe/Banka | Senet tutarının alacak olarak kaydedileceği hesabın seçildiği alandır. Cari, Muhasebe ve Banka olmak üzere üç seçenekten oluşur. Muhasebe seçildiğinde, program muhasebe kodu sorgular ve senet tutarını, girilen muhasebe koduna alacak olarak kaydeder. Banka seçildiğinde, program banka kodu sorgular ve senet tutarını, girilen banka koduna alacak olarak kaydeder. Cari seçildiğinde ise, program cari kod sorgular ve senet tutarını, girilen cari koda alacak olarak kaydeder. |
| Banka No | Senetler için ödeme işleminin yapıldığı banka kodunun girildiği alandır. |
| Açıklama | Bu alana açıklama olarak “?? NOLU ÇEK ÖDE.” program tarafından otomatik olarak aktarılır. Kullanıcı tarafından değişiklik yapılabilir. |
| **![](../../../../_assets/39d77b8716226638d9ce.jpg)**Tamam | Girilen koşullara uygun çeklerin grid ekranda listelenmesi için kullanılan butondur. |
| ![](../../../../_assets/6774caf5b4c523cda5fc.png) Kayıtları Yap | Listelenen senetler içinde tahsil edilecek olanların üzerinde iken fare ile çift tıklanarak, oluşacak kayıtların ilgili modüllere aktarılması için kullanılan butondur. Butona tıklanması ile, ekrana gelen uyarı onaylanarak işlem tamamlanır. ![](../../../../_assets/d0aebd89ae472e694a6a.png) |
| ![](../../../../_assets/ab9047f06dcf17f8b154.png) Hepsini Seç | Grid alana aktarılan tüm satırların seçilmesi için kullanılan butondur. |
| ![](../../../../_assets/ca4e3e18d9df15206767.png) Hepsini Kaldır | Grid alanda seçilen satırların tümünün seçimini kaldırmak için kullanılan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Toplu borç senedi ödentisi için girilen kaydın iptal edilmesi için kullanılan butondur. |
