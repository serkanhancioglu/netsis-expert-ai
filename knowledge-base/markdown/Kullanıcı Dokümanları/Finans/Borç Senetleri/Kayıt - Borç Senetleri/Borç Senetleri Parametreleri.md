---
title: "Borç Senetleri Parametreleri"
page_id: "24740275"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Borç Senetleri"
  - "Kayıt / Borç Senetleri"
  - "Borç Senetleri Parametreleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Borç Senetleri / Kayıt / Borç Senetleri / Borç Senetleri Parametreleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWNhNWEzMTRiLWJlZmEtNDc5ZS1iZjRjLWEyMWY3NTc5YzVkMyZsaW5rPTJjYTBhZWE4LTNlMWMtNDc4ZS05MzA4LWVhYWMzN2NhZmVhNCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=ca5a314b-befa-479e-bf4c-a21f7579c5d3&link=2ca0aea8-3e1c-478e-9308-eaac37cafea4&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "borc-senetleri-parametreleri_34218388_24740275.html"
source_version: "2022-09-27T09:53:35.367+03:00"
source_bytes: 46033
fetched_at: "2026-09-13T04:12:16+00:00"
generator: "netsis-scraper 1.0.0"
---
# Borç Senetleri Parametreleri

Borç Senetleri parametresi, Finans Bölümü'nde, "Kayıt/Borç Senetleri" menüsünün altında yer alır. Borç Senetleri Parametresi bölümünden kaydedilen bilgiler, "Borç Senetleri" modülünün kullanımında yardımcı olur. Kayıtlar, işaretlenen seçimler doğrultusunda işlem görür.

![](../../../../_assets/9f62f63249ae878ae3fd.png)

Borç Senetleri Parametreleri ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Borç Senetleri Parametreleri Ekranı |  |
| --- | --- |
| Cariye Tek Tek Aktarılsın | Cariye Tek Tek Aktarılsın parametresi işaretlenmediğinde; cari hesabın hareket kayıtlarına, alındı/verildi bordroları toplam tutar olarak tek bir harekette aktarılır. Cariye Tek Tek Aktarılsın parametresinin işaretlenmesi durumunda; bir bordro içindeki senetler, ilgili cari hesabın hareket kayıtlarına detaylı olarak ayrı ayrı aktarılır. Bu durumda, cari hareket kayıtlarına alındı/verildi senetlerinin satır adedi kadar bir aktarım olacağı için, cari hareketlerde satır sayısı artabilir. Satır sayısının artması istenmiyorsa, parametre işaretlenmeyerek, ilgili bordroya ait senetler cari hareket kayıtlarında "Hareket Detayı İzleme" tuşu ile ayrıntılı olarak izlenebilir. Cariye Tek Tek Aktarılsın parametresi işaretlenmezse, senetleriniz ilgili cari hesabın hareket kayıtlarına, verildi bordro numarası ile toplam bir tek hareket olarak aktarılacaktır. Parametre işaretlenir ise, bir bordro içindeki senetler ilgili cari hesabın hareket kayıtlarına tek tek aktarılacaktır. |
| Muhasebeye Tek Tek Aktarılsın | Senet modülünün muhasebe ile entegre kullanımında geçerli olan bir parametredir. Parametre işaretlenmediğinde; alındı ve verildi bordroları, numaralarına göre entegrasyona toplam tutar olarak aktarılır. Entegrasyona aktarım sırasında bordroda toplanan senetlerin, ayrıntılı olarak muhasebeye aktarılması istendiğinde bu parametrenin işaretlenmesi gerekir. Entegrasyona aktarılan alındı/verildi senet bordrosunun içinde kaç adet senet varsa, entegrasyona bu senetler de ayrı ayrı aktarılır. Böylece; entegrasyonda ve entegrasyondan aktarılarak muhasebede oluşturulan fişlerde, senet adedi kadar satır kaydı oluşur ve fişlerdeki satır sayısı artabilir. |
| Çıkışta Verilen Kodu Aransın | Çıkışta Verilen Kodu Aransın parametresi, sadece "Devir Senet Girişi" bölümü için geçerlidir. Cari hesap çek işlemleri yapılırken "Verilen Kodunun" cari hesaplarda mutlaka tanımlanması gerekir. Senet kayıtları sırasında, "Verilen Kodu" kod sistemi kullanılmadan, cari hesaplarda ilgili kod aranmadan, sadece isim girilerek kaydedilmesi istendiğinde, bu parametrenin işaretlenmemesi gerekir. Daha sağlıklı rapor alınması için bu parametrenin işaretlenmesi tavsiye edilir. Böylece, "Verilen Kodu" cari hesaplardan aranarak, ilgili cari hesapların hareketleri de düzgün bir şekilde kaydedilerek işlem görür. Senet girişlerinin/çıkışlarının "Ön Muhasebe" ve "Genel Muhasebe" bölümleri ile entegre çalışması için, alındı ve verildi kayıtlarının "Cari Hesap Senet İşlemleri" ile ilgili menülerden yapılması gerekir. "Devir Senet Girişi" bölümü kullanılmaz. |
| Verildi Bordrolarına Ortalama Gün Basılsın | Verildi bordrolarının basımı sırasında, ortalama günlerin bordro basımına eklenmesi için işaretlenmesi gereken parametredir. |
| Döviz Uygulaması Var | Döviz Uygulaması Var, Borç Senetleri modülünü dövizli olarak takip ederek, döviz birimleri ile senet kayıtları oluşturan firmalar için geçerli parametredir. Dövizli senet takibi ve işlemi yapmayan ve senet bilgilerini sadece Türk Lirası değerlerinden takip eden firmaların bu parametreyi işaretlememesi gerekir. Dövizli senet işlemlerinin yapılması için bu parametrenin işaretlenmesinin dışında, Yardımcı Programlar → Kayıt → [Şirket-Şube Parametre Tanımları](<../../../Genel/Yardımcı Programlar/Kayıt - Yardımcı Programlar/Şirket - Şube - Parametre Tanımları.md>) → "Döviz Uygulaması Var" parametresinin işaretlenmesi gerekir. Dövizli kayıt işlemleri; Devir Senet Girişi, Cari Hesap Senet Alındı Kaydı ve Cari Hesaba Senet Cirosu, Banka Tahsil Teminata Senet Cirosu bölümlerinde yapılan işlemlerden sorgulanır. Her senet girişi için döviz birimi, kuru ve döviz tutarı tek tek sorgulanarak kayıt yapılır. Dövizli senet girişlerinde program, ilgili senedin tutarını (kur bilgilerinden) Türk Lirasına çevirerek muhasebe entegrasyonuna Türk Lirası değerinden aktarır. Böylece, döviz birimi ve döviz tutarının da hem izlenmesini hem de raporlanmasını sağlar. Dövizli senetlerde kur farkının oluşması durumunda, Müşteri Senetleri → Raporlar → "Dövizli Senetler Yeniden Değerleme Listesi" bölümünden kur farkı değerleri senetler bazında listelenir. Oluşan kur farkı değerlerinin muhasebe ve cariye aktarılması istendiğinde, Müşteri Senetleri → İşlemler → "[Dövizli Senetler Kur Farkı Kaydı](<../../Müşteri Senetleri/İşlemler - Müşteri Senetleri/Dövizli Senetler Kur Farkı Kaydı.md>)" bölümü çalıştırılarak entegre edilir. |
| Matbu Senet Basımı | Matbu Senet Basımı parametresi; "Cari Hesap Senet Alındı Kaydı" ve "Senet Tanzim" bölümlerinden senet kaydı yapıldığında, senet bilgilerinin önceden hazırlanan özel dizayna göre basımının yapılması için işaretlenmesi gereken parametredir. Parametrenin işaretli olduğu durumlarda, senet kaydı yapıldığı sırada program tarafından basımın yapılacağı dizaynın seçileceği "Dizayn Sorgulama" penceresi ekrana gelir. "Dizayn Kodu", tipi "Müşteri Senetleri" olan dizaynlardan biri seçilerek girilir. Dizayn tip ve tanımlamaları ile ilgili detaylı bilgi için; Genel → Dizayn Modülü → Kayıt → [Dizayn](<../../../Genel/Dizayn Modülü/Kayıt - Dizayn/Dizayn.md>) dokümanına bakılabilir. |
| Bordro Basımında Açıklama Bulunsun | Senet kayıt işlemlerinde bordro dökümü alınması istendiğinde ve bu parametre işaretlendiğinde, ekrandaki bordrolara (kullanıcının isteği doğrultusunda) üç satırlık bir açıklama hanesi gelir. Bu satırlara girilen bilgiler bordro basımlarının altında yazıcıya aktarılır. Açıklama alanına girilen bilgiler saklanmaz. Tekrar aynı bordronun yazıcı basımının istendiği durumlarda ilgili bilgilerin yeniden girilmesi gerekir. |
| Bordro Basım Kağıt Uzunluğu | Senet kayıtlarından sonra bordro basımı yapılması istendiğinde, kağıt uzunluğunun 33,66 olarak ayarlanmasını veya kağıdın perforesine göre tanımlama yapılmasını sağlayan parametredir. |
| Bordro Basımında Sıralama | Alındı ve Verildi Bordrolarının basımı sırasında, bordroda bulunan senetlerin Vade Tarihi, Giriş Sırası veya Senet Numarasına göre sıralanması için işaretlenmesi gereken parametredir. |
| Cari Hareket Kayıt Tarihi Olarak (Giriş-Çıkış Tarihi/Adat Baz Tarihi) | Cari hareket kayıtlarına girilen senetlerin hareket kayıt tarihinin seçildiği alandır. Giriş/Çıkış tarihi ile işlenmesi istendiğinde, "Giriş/Çıkış Tarihi" seçeneğinin işaretlenmesi gerekir. "Adat Baz Tarihi" seçeneğinin işaretlenmesi durumunda, senet kayıtlarının cari hareketlere aktarılması aşamasında, hareket kayıt tarihi olarak bilgisayarın tarihi baz alınır. |
| Ek Açıklama Bilgi Girişi Yapılsın | Ek açıklama alanlarının eklenmesi ve açıklama bilgisi girilmesini sağlayan parametredir. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilgilerin onaylanmasını sağlayan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
