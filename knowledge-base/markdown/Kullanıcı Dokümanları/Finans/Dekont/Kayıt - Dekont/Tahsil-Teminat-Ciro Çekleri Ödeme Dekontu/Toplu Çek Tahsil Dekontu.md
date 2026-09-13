---
title: "Toplu Çek Tahsil Dekontu"
page_id: "22805829"
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
  - "Toplu Çek Tahsil Dekontu"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Dekont / Kayıt / Dekont / Tahsil/Teminat/Ciro Çekleri Ödeme Dekontu / Toplu Çek Tahsil Dekontu"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTFmYzEwNGRhLTM2MzctNDU4Ny05Nzk0LWNkOTEwOGMzMWI5ZSZsaW5rPTNkYWY5NjY1LTdjMzYtNGQxOC04M2NhLTAzNTljMDEyMGJlYSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=1fc104da-3637-4587-9794-cd9108c31b9e&link=3daf9665-7c36-4d18-83ca-0359c0120bea&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "toplu-cek-tahsil-dekontu_34226510_22805829.html"
source_version: "2022-11-30T10:11:30.307+03:00"
source_bytes: 80055
fetched_at: "2026-09-13T04:09:04+00:00"
generator: "netsis-scraper 1.0.0"
---
# Toplu Çek Tahsil Dekontu

Toplu Çek Tahsil Dekontu, Finans Bölümü'nde, "Kayıt/Dekont" menüsünün altında yer alır. Toplu Çek Tahsil Dekontu, bankaya tahsile çıkan ve aynı tarihte ödenen birden fazla çekin tahsilat kaydını oluşturmak için kullanılan bölümdür.

![](../../../../../_assets/16122739365d2378e412.png)

Toplu Çek Tahsil Dekontu alanları ve içerdiği bilgiler aşağıdaki şekildedir:

| Toplu Çek Tahsil Dekontu Ekranı |  |
| --- | --- |
| İşlem Tarihi | Yapılan kayıt için baz alınacak tarihin girildiği alandır. Girilen tarih hem cari hem de entegrasyon kayıtlarında kullanılır. |
| Vade Tarihi Aralığı | Yapılan kayıt için baz alınacak vade tarihi aralığının girildiği alandır. |
| Döviz Tipi | Tahsil edilmesi istenen çekler için döviz tipi girilen alandır. Herhangi bir döviz tipi girildiğinde, tahsil edilecek çeklerdeki döviz tipinin, girilen döviz tipi ile eşit olması gerekir. |
| Döviz Kuru | "Döviz Tipi" girildiğinde, döviz kuru varsa otomatik olarak ekrana gelir ve üzerinde değişiklik yapılabilir. Girilen kur, dövizli çekler için kur farkı hesaplanırken kullanılır. |
| Çek Seri No | Çekin üzerinde yer alan seri numaranın girildiği alandır. |
| Tahsil/Teminat Hesap Kodu ve Adı | Çeklerin tahsile verildiği banka (bankalar cari hesaplarda tanımlanmışsa cari, muhasebede tanımlanmışsa muhasebe) hesap kodunun girildiği alandır. Bu alana girilen banka/cari/muhasebe koduna ciro edilen çekler bulunarak tahsil işlemi yapılır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodları arasından seçim yapılır. Boş bırakılmaz. |
| Seri Kodu | Daha önce seri kodu tanımlama bölümünden tanımlanan ve ilgili dekont kaydı için kullanılacak olan seri kodunun girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, seri kodları arasından seçim yapılır. |
| Fiş No | İlgili kayda ait fiş numarasının girildiği alandır. |
| Cari Rapor Kodu | Cari → Kayıt → [Cari Parametreleri](<../../../Cari/Kayıt - Cari/Cari Parametreleri.md>) → "Hareketlerde Rapor Kodu Girilsin" parametresinin işaretlenmesi ile aktif hale gelen alandır. Hareketlere aktarılması ve raporlanması amacıyla 1 karakterden oluşan rapor kodu girişi yapılır. |
| Plasiyer Kodu | Yardımcı Programlar → Kayıt → [Şirket-Şube Parametreleri](<../../../../Muhasebe/Muhasebe Modülü/Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/Genel Tanımlar/Yardımcı Programlar-Şirket-Şube Parametreleri.md>) → "Plasiyer Uygulaması Var" parametresinin işaretlenmesi ile aktif hale gelen alandır. Dekont kaydı sırasında ilgili plasiyer kodunun girilmesi gerekir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, plasiyer kodlarına ulaşılır. Boş bırakılmaz. |
| Proje Kodu | Yardımcı Programlar → Kayıt → [Şirket-Şube Parametreleri](<../../../../Muhasebe/Muhasebe Modülü/Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/Genel Tanımlar/Yardımcı Programlar-Şirket-Şube Parametreleri.md>) → "Proje Uygulaması Var" parametresinin işaretlenmesi ile aktif hale gelen alandır. Dekont kaydı sırasında ilgili plasiyer kodunun girilmesi gerekir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, proje kodlarına ulaşılır. Boş bırakılmaz. Girilen proje kodları, cari hareketlere ve entegrasyona aktarılır. |
| Referans Kodu | Muhasebe → Kayıt → [Muhasebe Parametreleri](<../../../../Muhasebe/Muhasebe Modülü/Kayıt - Muhasebe/Muhasebe Parametreleri.md>)→ "Fişlerde Referans Kodu Sorulsun" parametresinin işaretlenmesi ile aktif hale gelen alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, referans kodlarına ulaşılır. Boş bırakılmaz. |
| Virman Hesap Kodu ve Adı | Çek tutarının virman edileceği banka kodunun girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodlarına ulaşılır. |
| Alacak Cari Kodu | Bazı firmalar çalışma prensipleri gereği, müşterilerden aldığı çekleri ilk kayıt esnasında farklı bir hesaba işler (çekler ödenene kadar riskli olduğu için) ve çek tahsil edildiğinde müşterilerinin asıl hareket kayıtlarına virman yapar. Bu işlemin "Çek Tahsil Dekont Kaydı" sırasında otomatik olarak yapılmasını sağlamak için, dekont ekranında "Alacak Cari Kodu" alanı kullanılır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, cari kodlara ulaşılır. Boş bırakılmaz. Çekin tahsilatı sırasında, **Borç Cari Kodu** alanına otomatik olarak çek alındığında kaydedilen cari kod gelir. Yapılması gereken; çek tahsilatının hangi cari koda **alacak** **hareketi** olarak kaydedilmesi isteniyorsa, ilgili cari kodun **Alacak Cari Kodu** alanına girilmesidir. Böylece; dekont işleminin tamamlanması ile **Borç Cari Kodu** alanına girilen cari koda **borç hareketi** kaydedilerek, çek alımında kaydedilen alacak hareketi kapatılır. **Alacak Cari Kodu** alanına girilen koda **alacak hareketi** kaydedilerek çekin asıl cari harekete yansıtılması sağlanır. Bu tür uygulamaları olmayan firmalar için bu alan kullanılmaz. "Borç Cari Kodu" alanında veren kodundan farklı bir kod belirtilmesi istendiğinde, çek tahsilatının bu bölümden değil önceden olduğu gibi "Çek Tahsil Dekontu" bölümünden yapılması gerekir. Bu dekont adımında, birden fazla cari hesaptan alınan senetler için tahsilat yapılır. Bu sebeple, "Alacak Cari Kodu" alanında cari kod maskesi desteklenir. Maskenin düzgün kullanılması için, açılan cari kodların belli bir standartta olması gerekir. **Örneğin:** A0001, A0002, A0003 şeklindeki kodlarının fatura cari hesapları için A00012, A00022, A00032 şeklindeki kodlarının senet takip cari hesapları için açıldığı varsayıldığında; her üç cari için aynı anda doğru hesaplar çalıştırılarak tahsilat işlemi yapılaması için, "Alacak Cari Kodu" alanına "**?????2**" girilmesi gerekir. Böylece, soru işareti (?) girilen alanlara, çeklerdeki veren kodlar aktarılarak kodun sonuna 2 eklenir. |
| Açıklama | Bu alana program tarafından otomatik olarak başında ? (soru işareti) bulunan bir açıklama aktarılır. Herhangi bir değişiklik yapılmazsa tahsil edilen çek numaraları açıklama alanının başına eklenerek, cari ve entegrasyon kayıtlarına aktarılır. |
| **![](../../../../../_assets/39d77b8716226638d9ce.jpg)**Tamam | Girilen koşullara uygun çeklerin, grid ekranda listelenmesi için kullanılan butondur. |
| ![](../../../../../_assets/6774caf5b4c523cda5fc.png) Kayıtları Yap | Listelenen çekler içinde tahsil edilecek olanların üzerinde iken fare ile çift tıklanarak, oluşacak kayıtların ilgili modüllere aktarılması için kullanılan butondur. Butona tıklanması ile, ekrana gelen uyarı onaylanarak işlem tamamlanır. ![](../../../../../_assets/895cfbe5158af7609e06.png) |
| ![](../../../../../_assets/ab9047f06dcf17f8b154.png) Hepsini Seç | Grid alana aktarılan tüm satırların seçilmesi için kullanılan butondur. |
| ![](../../../../../_assets/ca4e3e18d9df15206767.png) Hepsini Sil | Grid alanda seçilen satırların tümünün seçimini kaldırmak için kullanılan butondur. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) İptal | Toplu çek tahsil dekontu için girilen kaydın iptal edilmesi için kullanılan butondur. |
