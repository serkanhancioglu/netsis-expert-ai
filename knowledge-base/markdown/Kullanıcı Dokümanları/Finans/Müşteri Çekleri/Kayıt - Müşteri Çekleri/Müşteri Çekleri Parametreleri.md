---
title: "Müşteri Çekleri Parametreleri"
page_id: "24739855"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Müşteri Çekleri"
  - "Kayıt / Müşteri Çekleri"
  - "Müşteri Çekleri Parametreleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Müşteri Çekleri / Kayıt / Müşteri Çekleri / Müşteri Çekleri Parametreleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTgwYzc3YzE3LTZkYTEtNDg5My05Njk0LTVhNzJjZWMyZTMyOSZsaW5rPThlMGE2OTBmLWE3MjAtNGYxYy04ZDZhLTRmMTQ5OGVlNDIyZiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=80c77c17-6da1-4893-9694-5a72cec2e329&link=8e0a690f-a720-4f1c-8d6a-4f1498ee422f&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "musteri-cekleri-parametreleri_34210925_24739855.html"
source_version: "2022-09-19T16:18:14.327+03:00"
source_bytes: 54174
fetched_at: "2026-09-13T04:11:08+00:00"
generator: "netsis-scraper 1.0.0"
---
# Müşteri Çekleri Parametreleri

Müşteri çekleri parametreleri, Finans Bölümü'nde Kayıt/Müşteri Çekleri menüsünün altında yer alır. Bu bölümde kaydedilen bilgiler Müşteri Çekleri modülünün kullanımında yardımcı olur. Kayıtlar, işaretlenen seçimler doğrultusunda işlem görür.

![](../../../../_assets/a688d72ede988865f1b6.png)

Müşteri çekleri parametreleri ekranında yer alan parametreler ve içerdiği bilgiler şunlardır:

| Müşteri Çekleri Parametreleri Ekranı |  |
| --- | --- |
| Cariye Tek Tek Aktarılsın | Cariye tek tek aktarılsın parametresi işaretlenmediğinde; cari hesabın hareket kayıtlarına, alındı/verildi bordroları toplam tutar olarak tek bir harekette aktarılır. Parametrenin işaretlenmesi durumunda; bir bordro içindeki çekler, ilgili cari hesabın hareket kayıtlarına detaylı olarak ayrı ayrı aktarılır. Bu durumda, cari hareket kayıtlarına alındı/verildi çeklerinin satır adedi kadar bir aktarım olacağı için, cari hareketlerde satır sayısı artabilir. Satır sayısının artması istenmiyorsa, parametre işaretlenmeyerek, ilgili bordroya ait çekler cari hareket kayıtlarında Hareket Detayı İzleme tuşu ile ayrıntılı olarak izlenebilir. |
| Muhasebeye Tek Tek Aktarılsın | Muhasebeye tek tek aktarılsın, Çek modülünün muhasebe ile entegre kullanımında geçerli olan bir parametredir. Parametre işaretlenmediğinde; alındı ve verildi bordroları, numaralarına göre entegrasyona toplam tutar olarak aktarılır. Entegrasyona aktarım sırasında bordroda toplanan çeklerin, ayrıntılı olarak muhasebeye aktarılması istendiğinde bu parametrenin işaretlenmesi gerekir. Entegrasyona aktarılan alındı/verildi çek bordrosunun içinde kaç adet çek varsa, entegrasyona bu çekler de ayrı ayrı aktarılır. Böylece; entegrasyonda ve entegrasyondan aktarılarak muhasebede oluşturulan fişlerde, çek adedi kadar satır kaydı oluşur ve fişlerdeki satır sayısı artabilir. |
| Tahsil/Teminata Çıkış Cariden | Tahsil/Teminata çek çıkışı yapılırken sorulacak banka kodunun, cari hesaplardan mı, banka hesaplarından mı yoksa muhasebe hesap planında tanımlanan bankanın hesap kodundan mı aranacağının sorgulandığı parametredir. Tahsil ve teminat hesapları cari hesaplarda açılan ve takibinin cari hesaplardan yapılması durumunda bu parametrenin işaretlenmesi tek başına yeterli değildir. Banka → Kayıt → [Banka Genel Parametreleri](<../../Banka/Kayıt - Banka/Banka Genel Parametreleri.md>) → Banka Entegre parametresinin işaretlenmemesi gerekir. Fakat, Tahsil/Teminat Hesapları Banka Modülünde açıksa, Banka Entegre parametresinin işaretlenmesi gerekir. Her iki seçeneği de kullanmayıp Tahsil/Teminat hesaplarının Muhasebe Hesap Planı bölümünden kullanılması istendiğinde Tahsil/Teminata Çıkış Cariden ve Banka Entegre parametrelerinin işaretlenmemesi gerekir. |
| Karşılıksız Çek Uyarısı Verilsin | Karşılıksız çek/çekleri bulunan ve kara liste kaydına aktarılan müşteri ve asıl borçluya göre, çek/senet girişi sırasında uyarı verilmesini sağlayan parametredir. |
| Girişte Veren Kodu Aransın | Girişte veren kodu aransın parametresi sadece Devir Çek Girişi bölümü için geçerlidir. Cari hesap çek işlemleri yapılırken Veren Kodunun cari hesaplarda mutlaka tanımlanması gerekir. Çek kayıtları sırasında, Veren Kodu kod sistemi kullanılmadan, cari hesaplarda ilgili kod aranmadan, sadece isim girilerek kaydedilmesi istendiğinde, bu parametrenin işaretlenmemesi gerekir. Daha sağlıklı rapor alınması için bu parametrenin işaretlenmesi tavsiye edilir. Böylece, Veren Kodu cari hesaplardan aranarak, ilgili cari hesapların hareketleri de düzgün bir şekilde kaydedilerek işlem görür. Çek girişlerinin/çıkışlarının Ön Muhasebe ve Genel Muhasebe bölümleri ile entegre çalışması için, alındı ve verildi kayıtlarının Cari Hesap Çek İşlemleri ile ilgili menülerden yapılması gerekir. Devir Çek Girişi bölümü kullanılmaz. |
| Çıkışta Verilen Kodu Aransın | Bu parametre sadece Devir Çek Girişi bölümü için geçerlidir. Cari hesap çek işlemleri yapılırken Verilen Kodunun cari hesaplarda mutlaka tanımlanması gerekir. Çek kayıtları sırasında, Verilen Kodu kod sistemi kullanılmadan, cari hesaplarda ilgili kod aranmadan, sadece isim girilerek kaydedilmesi istendiğinde, bu parametrenin işaretlenmemesi gerekir. Daha sağlıklı rapor alınması için bu parametrenin işaretlenmesi tavsiye edilir. Böylece, Verilen Kodu cari hesaplardan aranarak, ilgili cari hesapların hareketleri de düzgün bir şekilde kaydedilerek işlem görür. Çek girişlerinin/çıkışlarının Ön Muhasebe ve Genel Muhasebe bölümleri ile entegre çalışması için, alındı ve verildi kayıtlarının Cari Hesap Çek İşlemleri ile ilgili menülerden yapılması gerekir. Devir Çek Girişi bölümü kullanılmaz. |
| Alındı Bordrolarında Ortalama Gün Basılsın | Alındı bordrolarının basımı sırasında, ortalama günlerin bordro basımına eklenmesi için işaretlenmesi gereken parametredir. |
| Verildi Bordrolarında Ortalama Gün Basılsın | Verildi bordrolarının basımı sırasında, ortalama günlerin bordro basımına eklenmesi için işaretlenmesi gereken parametredir. |
| Döviz Uygulaması Var | Müşteri Çekleri modülünü dövizli olarak takip ederek, döviz birimleri ile çek kayıtları oluşturan firmalar için geçerli parametredir. Dövizli çek takibi ve işlemi yapmayan ve çek bilgilerini sadece Türk Lirası değerlerinden takip eden firmaların bu parametreyi işaretlememesi gerekir. Dövizli çek işlemlerinin yapılması için bu parametrenin işaretlenmesinin dışında, Yardımcı Programlar → Kayıt → [Şirket-Şube Parametre Tanımları](<../../../Genel/Yardımcı Programlar/Kayıt - Yardımcı Programlar/Şirket - Şube - Parametre Tanımları.md>) → Döviz Uygulaması Var parametresinin işaretlenmesi gerekir. Dövizli kayıt işlemleri; Devir Çek Girişi, Cari hesap Çek Alındı Kaydı ve Cari Hesaba Çek Cirosu, Banka Tahsil Teminata Çek Cirosu bölümlerinde yapılan işlemlerden sorgulanır. Her çek girişi için döviz birimi, kuru ve döviz tutarı tek tek sorgulanarak kayıt yapılır. Dövizli çek girişlerinde program, ilgili çekin tutarını (kur bilgilerinden) Türk Lirasına çevirerek muhasebe entegrasyonuna Türk Lirası değerinden aktarır. Böylece, döviz birimi ve döviz tutarının da hem izlenmesini hem de raporlanmasını sağlar. Dövizli çeklerde kur farkının oluşması durumunda, Müşteri Çekleri → Raporlar → [Dövizli Çekler Yeniden Değerleme Listesi](<../Raporlar - Müşteri Çekleri/Dövizli Çekler Yeniden Değerleme Listesi.md>) bölümünden kur farkı değerleri çekler bazında listelenir. Oluşan kur farkı değerlerinin muhasebe ve cariye aktarılması istendiğinde, Müşteri Çekleri → İşlemler → [Dövizli Çekler Kur Farkı Kaydı](<../İşlemler - Müşteri Çekleri/Dövizli Çekler Kur Farkı Kaydı.md>) bölümü çalıştırılarak entegre edilir. |
| Bordro Basımında Açıklama Bulunsun | Çek kayıt işlemlerinde bordro dökümü alınması istendiğinde ve bu parametre işaretlendiğinde, ekrandaki bordrolara (kullanıcının isteği doğrultusunda) üç satırlık bir açıklama hanesi gelir. Bu satırlara girilen bilgiler bordro basımlarının altında yazıcıya aktarılır. Açıklama alanına girilen bilgiler saklanmaz. Tekrar aynı bordronun yazıcı basımının istendiği durumlarda ilgili bilgilerin yeniden girilmesi gerekir. |
| Bordro Basım Uzunluğu | Çek kayıtlarından sonra bordro basımı yapılacak ise; kağıt uzunluğunun 33,66 olarak veya kağıdın perforesine göre tanımlamasının yapılmasını sağlayan parametredir. |
| Cari Hareket Kayıt Tarihi Olarak (Giriş/Çıkış Tarihi -Adat Baz Tarihi) | Cari hareket kayıtlarına girilen çeklerin hareket kayıt tarihi olarak giriş/çıkış tarihiyle işlenmesi istendiğinde Giriş/Çıkış Tarihi, hareket kayıt tarihi olarak günün tarihinin baz alınması istendiğinde ise, Adat Baz Tarihi seçeneğinin işaretlenmesi gerekir. |
| Bordro Basımında Sıralama | Alındı ve Verildi bordrolarının basımı sırasında, bordroda bulunan çeklerin Vade Tarihi, Giriş Sırası veya Çek Numarası alanlarına göre sıralama yapılmasını sağlayan parametredir. |
| Çekin Serisi Cari Açıklamaya Aktarılsın | Çekler için belirtilen seri bilgisinin, cari hareket kayıtlarındaki açıklamaya aktarılmasını sağlayan parametredir. |
| Ek Açıklama Bilgi Girişi Yapılsın | Çek girişlerinde ek açıklama bilgi girişi yapılması istendiğinde işaretlenmesi gereken parametredir. İşaretlendiğinde, Çek girişi ekranına ek açıklama alanları eklenir. |
| Tamam | Girilen bilgilerin onaylanmasını sağlayan butondur. |
| İptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
