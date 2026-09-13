---
title: "Borç Çekleri Parametreleri"
page_id: "24740204"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Borç Çekleri"
  - "Kayıt / Borç Çekleri"
  - "Borç Çekleri Parametreleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Borç Çekleri / Kayıt / Borç Çekleri / Borç Çekleri Parametreleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTUyNTA0Y2Q3LTcyOWQtNGU2YS1iMzk5LTlkYWQ2YjhmNmI4NiZsaW5rPTU5NzUzNGNhLTg5MTYtNGE5YS04NTA4LTE1NmExNjQ1ZTkzYiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=52504cd7-729d-4e6a-b399-9dad6b8f6b86&link=597534ca-8916-4a9a-8508-156a1645e93b&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "borc-cekleri-parametreleri_34218788_24740204.html"
source_version: "2022-12-13T13:57:54.123+03:00"
source_bytes: 50259
fetched_at: "2026-09-13T04:12:32+00:00"
generator: "netsis-scraper 1.0.0"
---
# Borç Çekleri Parametreleri

Borç Çekleri Parametreleri, Finans Bölümü'nde, "Kayıt/Borç Çekleri" menüsünün altında yer alır. Borç Çekleri Parametreleri ekranından kaydedilen bilgiler, "Borç Çekleri" modülünün kullanımında yardımcı olur. Kayıtlar, işaretlenen seçimler doğrultusunda işlem görür.

![](../../../../_assets/996f9b978fb27855024a.png)

Borç Çekleri Parametreleri ekranında yer alan parametreler ve içerdiği bilgiler şunlardır:

| Borç Çekleri Parametreleri Ekranı |  |
| --- | --- |
| Cariye Tek Tek Aktarılsın | Bu parametre işaretlenmediğinde; cari hesabın hareket kayıtlarına, alındı/verildi bordroları toplam tutar olarak tek bir harekette aktarılır. Parametrenin işaretlenmesi durumunda; bir bordro içindeki çekler, ilgili cari hesabın hareket kayıtlarına detaylı olarak ayrı ayrı aktarılır. Bu durumda, cari hareket kayıtlarına alındı/verildi çeklerinin satır adedi kadar bir aktarım olacağı için, cari hareketlerde satır sayısı artabilir. Satır sayısının artması istenmiyorsa, parametre işaretlenmeyerek, ilgili bordroya ait çekler cari hareket kayıtlarında "Hareket Detayı İzleme" tuşu ile ayrıntılı olarak izlenebilir. Bu parametre işaretlenmez ise, çekleriniz ilgili cari hesabın hareket kayıtlarına, verildi bordro numarası ile toplam bir tek hareket olarak aktarılacaktır. Parametre işaretlenir ise, bir bordro içindeki çekler ilgili cari hesabın hareket kayıtlarına tek tek aktarılacaktır. |
| Muhasebeye Tek Tek Aktarılsın | Çek modülünün muhasebe ile entegre kullanımında geçerli olan bir parametredir. Parametre işaretlenmediğinde; alındı ve verildi bordroları, numaralarına göre entegrasyona toplam tutar olarak aktarılır. Entegrasyona aktarım sırasında bordroda toplanan çeklerin, ayrıntılı olarak muhasebeye aktarılması istendiğinde bu parametrenin işaretlenmesi gerekir. Entegrasyona aktarılan alındı/verildi çek bordrosunun içinde kaç adet çek varsa, entegrasyona bu çekler de ayrı ayrı aktarılır. Böylece; entegrasyonda ve entegrasyondan aktarılarak muhasebede oluşturulan fişlerde, çek adedi kadar satır kaydı oluşur ve fişlerdeki satır sayısı artabilir. |
| Çıkışta Verilen Kodu Aransın | Bu parametre sadece "Devir Çek Girişi" bölümü için geçerlidir. Cari hesap çek işlemleri yapılırken "Verilen Kodunun" cari hesaplarda mutlaka tanımlanması gerekir. Çek kayıtları sırasında, "Verilen Kodu" kod sistemi kullanılmadan, cari hesaplarda ilgili kod aranmadan, sadece isim girilerek kaydedilmesi istendiğinde, bu parametrenin işaretlenmemesi gerekir. Daha sağlıklı rapor alınması için bu parametrenin işaretlenmesi tavsiye edilir. Böylece, "Verilen Kodu" cari hesaplardan aranarak, ilgili cari hesapların hareketleri de düzgün bir şekilde kaydedilerek işlem görür. Çek girişlerinin/çıkışlarının "Ön Muhasebe" ve "Genel Muhasebe" bölümleri ile entegre çalışması için, alındı ve verildi kayıtlarının "Cari Hesap Çek İşlemleri" ile ilgili menülerden yapılması gerekir. "Devir Çek Girişi" bölümü kullanılmaz. |
| Verildi Bordrolarına Ortalama Gün Basılsın | Verildi bordrolarının basımı sırasında, ortalama günlerin bordro basımına eklenmesi için işaretlenmesi gereken parametredir. |
| Döviz Uygulaması Var | Borç Çekleri modülünü dövizli olarak takip ederek, döviz birimleri ile çek kayıtları oluşturan firmalar için geçerli parametredir. Dövizli çek takibi ve işlemi yapmayan ve çek bilgilerini sadece Türk Lirası değerlerinden takip eden firmaların bu parametreyi işaretlememesi gerekir. Dövizli çek işlemlerinin yapılması için bu parametrenin işaretlenmesinin dışında, Yardımcı Programlar → Kayıt → [Şirket-Şube Parametre Tanımları](<../../../Genel/Yardımcı Programlar/Kayıt - Yardımcı Programlar/Şirket - Şube - Parametre Tanımları.md>) → "Döviz Uygulaması Var" parametresinin işaretlenmesi gerekir. Dövizli kayıt işlemleri; Devir Çek Girişi, Cari Hesap Çek Alındı Kaydı ve Cari Hesaba Çek Cirosu, Banka Tahsil Teminata Çek Cirosu bölümlerinde yapılan işlemlerden sorgulanır. Her çek girişi için döviz birimi, kuru ve döviz tutarı tek tek sorgulanarak kayıt yapılır. Dövizli çek girişlerinde program, ilgili çek tutarını (kur bilgilerinden) Türk Lirasına çevirerek muhasebe entegrasyonuna Türk Lirası değerinden aktarır. Böylece, döviz birimi ve döviz tutarının da hem izlenmesini hem de raporlanmasını sağlar. Dövizli çeklerde kur farkının oluşması durumunda, Borç Çekleri → Raporlar → "Dövizli Çekler Yeniden Değerleme Listesi" bölümünden kur farkı değerleri çekler bazında listelenir. Oluşan kur farkı değerlerinin muhasebe ve cariye aktarılması istendiğinde, Borç Çekleri → İşlemler → "[Dövizli Çekler Kur Farkı Kaydı](<../../Müşteri Çekleri/İşlemler - Müşteri Çekleri/Dövizli Çekler Kur Farkı Kaydı.md>)" bölümü çalıştırılarak entegre edilir. |
| Matbu Çek Basımı | "Cari Hesap Çek Alındı Kaydı" ve "Çek Tanzim" bölümlerinden çek kaydı yapıldığında, çek bilgilerinin önceden hazırlanan özel dizayna göre basımının yapılması için işaretlenmesi gereken parametredir. Parametrenin işaretli olduğu durumlarda, çek kaydı yapıldığı sırada program tarafından basımın yapılacağı dizaynın seçileceği "Dizayn Sorgulama" penceresi ekrana gelir. "Dizayn Kodu", tipi "Borç Çekleri" olan dizaynlardan biri seçilerek girilir. > [!NOTE]<br>> Dizayn tip ve tanımlamaları ile ilgili detaylı bilgi için; Genel → Dizayn Modülü → Kayıt → [Dizayn](<../../../Genel/Dizayn Modülü/Kayıt - Dizayn/Dizayn.md>) |
| Bordro Basımında Açıklama Bulunsun | Çek kayıt işlemlerinde bordro dökümü alınması istendiğinde ve bu parametre işaretlendiğinde, ekrandaki bordrolara (kullanıcının isteği doğrultusunda) üç satırlık bir açıklama hanesi gelir. Bu satırlara girilen bilgiler bordro basımlarının altında yazıcıya aktarılır. > [!NOTE]<br>> Açıklama alanına girilen bilgiler saklanmaz. Tekrar aynı bordronun yazıcı basımının istendiği durumlarda ilgili bilgilerin yeniden girilmesi gerekir. |
| Çekin Serisi Cari Açıklamaya Aktarılsın | Çekin seri numarasının cari açıklamaya aktarılması için işaretlenmesi gereken parametredir. |
| Bordro Basım Kağıt Uzunluğu | Çek kayıtlarından sonra bordro basımı yapılması istendiğinde, kağıt uzunluğunun 33,66 olarak ayarlanmasını veya kağıdın perforesine göre tanımlama yapılmasını sağlayan parametredir. |
| Bordro Basımında Sıralama | Alındı ve Verildi Bordrolarının basımı sırasında, bordroda bulunan çeklerin Vade Tarihi, Giriş Sırası veya Çek Numarasına göre sıralanması için işaretlenmesi gereken parametredir. |
| Cari Hareket Kayıt Tarihi Olarak (Giriş-Çıkış Tarihi/Adat Baz Tarihi) | Cari hareket kayıtlarına girilen çeklerin hareket kayıt tarihinin seçildiği alandır. Giriş/Çıkış tarihi ile işlenmesi istendiğinde, "Giriş/Çıkış Tarihi" seçeneğinin işaretlenmesi gerekir. "Adat Baz Tarihi" seçeneğinin işaretlenmesi durumunda, çek kayıtlarının cari hareketlere aktarılması aşamasında, hareket kayıt tarihi olarak bilgisayarın tarihi baz alınır. |
| Ek Açıklama Bilgi Girişi Yapılsın | Ek açıklama alanlarının eklenmesi ve açıklama bilgisi girilmesini sağlayan parametredir. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) | Girilen bilgilerin onaylanmasını sağlayan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
