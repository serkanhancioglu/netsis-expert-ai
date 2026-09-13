---
title: "Bankadan Gelen Protestolu Senet Dekontu"
page_id: "22805845"
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
  - "Bankadan Gelen Protestolu Senet Dekontu"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Dekont / Kayıt / Dekont / Bankadan Gelen Protestolu Senet Dekontu"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTA4MmNjMmRhLWJlMzgtNDgyZC04MWFjLTk5NjI3NTY3NzBjZSZsaW5rPWMyYzdjMjhmLTU1MTctNGYyYi1hZThlLTViMGY1MDVmZDQxYSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=082cc2da-be38-482d-81ac-9962756770ce&link=c2c7c28f-5517-4f2b-ae8e-5b0f505fd41a&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "bankadan-gelen-protestolu-senet-dekontu_34226640_22805845.html"
source_version: "2022-11-30T10:27:38.613+03:00"
source_bytes: 194442
fetched_at: "2026-09-13T04:09:08+00:00"
generator: "netsis-scraper 1.0.0"
---
# Bankadan Gelen Protestolu Senet Dekontu

Bankadan Gelen Protestolu Senet Dekontu, Finans Bölümü'nde, "Kayıt/Dekont" menüsünün altında yer alır. Bankadan Gelen Protestolu Senet Dekontu, bankalardaki tahsil/teminat hesaplarına ciro edilen müşteri senetlerinin protesto olmaları durumunda, ilgili entegre kayıtların oluşturulması için kullanılan bölümdür.

![](../../../../_assets/6953fe8ad8a089258b19.png)

Bankadan Gelen Protestolu Senet Dekontu alanları ve içerdiği bilgiler aşağıdaki şekildedir:

| Bankadan Gelen Protestolu Senet Dekontu Ekranı |  |
| --- | --- |
| Senet No | Protestolu senet numarasının girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, senet numaralarına ulaşılır. |
| Seri No | Girilen dekontun seri numarasının kaydedildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, seri numaralarına ulaşılır. Boş bırakılmaz. |
| Dekont No | Program tarafından otomatik olarak her bir dekont serisi 1 rakamından başlar. Kaydedilen her dekont için bir sayı arttırılarak devam eder. Farklı bir numaradan başlaması istendiğinde ise; Dekont → İşlemler → "[Dekont Numarası Düzenleme](<../İşlemler - Dekont/Dekont Numarası Düzenleme.md>)" bölümü kullanılarak serilere başlangıç numarası verilir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, kayıtlı dekont numaralarına ulaşılır. |
| Fiş No | Bankadan gelen protestolu senet dekont kaydı için fiş numarası girilen alandır. Bu alana girilen numara Muhasebe Entegrasyonu ve Cari Hareket Kayıtları bölümlerinde yer alan "Fiş No" alanına aktarılır. |
| İşlem Tarihi | Bankadan gelen protestolu senet dekont kaydının girildiği tarihtir. Yapılacak işlem sonucu oluşacak kayıtlar ,diğer modüllere (Banka-Entegrasyon-Senet) bu tarih ile kaydedilir. |
| Tahsil/Teminat Banka Kodu | Girilen senet numarasına göre; verilen (ciro edilen) banka kodu, muhasebe hesap kodu veya cari hesap kodunun, "Tahsil/Teminat Banka Kodu" alanına otomatik olarak aktarıldığı alandır. |
| Borç Cari Kodu | Veren (ciro eden/asıl borçlu) kodunun otomatik olarak "Borç Cari Kodu" alanına aktarıldığı alandır. Alanın sağ tarafında cari kodun ismi yer alır. |
| Tutar | Girilen senet numarasına göre tutarın program tarafından otomatik olarak aktarıldığı alandır. |
| Protesto Masrafı | Senedi veren kişinin üstleneceği masraflara (varsa) ait toplam tutarın girildiği alandır. |
| Genel Gider Masrafı | Protestolu senet ile ilgili masraflara ait toplam tutarın girildiği alandır. |
| Genel Gider Hesap Kodu | "Genel Gider Masrafı" alanında girilen tutarın aktarılacağı muhasebe hesap kodunun girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodlarına ulaşılır. |
| Alacaklı Banka Kodu | "Genel Gider Masrafı" alanında girilen tutarın alacak kaydedileceği banka hesabı, cari hesap kodu veya muhasebe hesap kodunun girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, hesap kodlarına ulaşılır. |
| Cari Rapor Kodu (C.R.K.) | Cari → Kayıt → [Cari Parametreleri](<../../Cari/Kayıt - Cari/Cari Parametreleri.md>) → "Hareketlerde Rapor Kodu Girilsin" parametresinin işaretlenmesi ile aktif hale gelen alandır. Hareketlere aktarılması ve raporlanması amacıyla 1 karakterden oluşan rapor kodu girişi yapılır. |
| Plasiyer Kodu | Yardımcı Programlar → Kayıt → [Şirket-Şube Parametreleri](<../../../Muhasebe/Muhasebe Modülü/Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/Genel Tanımlar/Yardımcı Programlar-Şirket-Şube Parametreleri.md>) → "Plasiyer Uygulaması Var" parametresinin işaretlenmesi ile aktif hale gelen alandır. Dekont kaydı sırasında ilgili plasiyer kodunun girilmesi gerekir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, plasiyer kodlarına ulaşılır. Boş bırakılmaz. |
| Proje Kodu | Yardımcı Programlar → Kayıt → [Şirket-Şube Parametreleri](<../../../Muhasebe/Muhasebe Modülü/Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/Genel Tanımlar/Yardımcı Programlar-Şirket-Şube Parametreleri.md>)→ "Proje Uygulaması Var" parametresinin işaretlenmesi ile aktif hale gelen alandır. Dekont kaydı sırasında ilgili plasiyer kodunun girilmesi gerekir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, proje kodlarına ulaşılır. Boş bırakılmaz. Girilen proje kodları, cari hareketlere ve entegrasyona aktarılır. |
| Referans Kodu | Muhasebe → Kayıt → [Muhasebe Parametreleri](<../../../Muhasebe/Muhasebe Modülü/Kayıt - Muhasebe/Muhasebe Parametreleri.md>) → "Fişlerde Referans Kodu Sorulsun" parametresinin işaretlenmesi ile aktif hale gelen alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, referans kodlarına ulaşılır. Boş bırakılmaz. |
| Cari Açıklama | Cari hareket kayıtlarına aktarılması istenen açıklama bilgisinin girildiği alandır. |
| Yevmiye Açıklama | Yevmiye maddelerine aktarılması istenen açıklama bilgisinin girildiği alandır. |
| Özel Basım | Dekont kaydının basımı için "Dizayn Modülü" ile hazırlanan özel bir basımın kullanılması istendiğinde işaretlenen seçenektir. Özel bir basım değil, standart bir basım yapılması istendiğinde bu seçenek işaretlenmemesi, sadece "Basım "alanındaki "Evet" seçeneğinin işaretlenmesi gerekir. İşlemler bittikten sonra Tamam ![](../../../../_assets/39d77b8716226638d9ce.jpg) butonuna basıldığında; borçlu cari hesaba senet tutarı + senet masrafı kadar borç, alacaklı cari hesaba senet tutarı + senet masrafı + senet gider tutarı kadar alacak hareket kaydı işlenir. "Müşteri Senetleri Modülünde" ilgili senedin durumu program tarafından **“Ödendi**” olarak değiştirilir. İlgili yevmiye maddeleri oluşturularak Entegre → Kayıt → [Entegrasyon Kayıtları](<../../../Muhasebe/Entegre/Kayıt - Entegre/Entegrasyon Kayıtları.md>) → Dekont sekmesinden izlenir. |
| Masraflar Cariye Ayrı İşlensin | Borçlu/Alacaklı cari hesaba, senet tutarları ile masrafların ayrı satırlar halinde işlenmesi için kullanılan seçenektir. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilginin onaylanmasını sağlayan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgiden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |

**Bankadan Gelen Protestolu Senet Dekontu İptali**

Bankadan Gelen Protestolu Senet Dekontunun iptali yerine ters kayıt oluşturulur. Bu dekont kaydına ait ters kayıtların nasıl oluşturulacağı ile ilgili detaylı bilgi; [Çek Tahsil Dekontu](<Tahsil-Teminat-Ciro Çekleri Ödeme Dekontu/Çek Tahsil Dekontu/index.md>) bölümünde yer alır.
