---
title: "e-Fatura Parametreleri"
page_id: "28147722"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Fatura"
  - "Kayıt / Fatura"
  - "E-Fatura İşlemleri"
  - "e-Fatura Parametreleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Fatura / Kayıt / Fatura / E-Fatura İşlemleri / e-Fatura Parametreleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTFmZDNmZGYyLTA0NTEtNDA1My1iY2RlLTI3NDA4OGJkM2IyOSZsaW5rPWU3OWU4MDNmLTcyNmUtNDhjYy04YTEyLWM1NzdiZDkyM2FlMSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=1fd3fdf2-0451-4053-bcde-274088bd3b29&link=e79e803f-726e-48cc-8a12-c577bd923ae1&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "e-fatura-parametreleri_47084562_28147722.html"
source_version: "2022-10-24T14:21:01.263+03:00"
source_bytes: 11593
fetched_at: "2026-09-13T04:02:13+00:00"
generator: "netsis-scraper 1.0.0"
---
# e-Fatura Parametreleri

e-Fatura parametrelerinin tanımlandığı bölüm e-Fatura Parametreleri bölümüdür. e-Fatura Parametreleri, "Lojistik - Satış Bölümünde" Fatura/Kayıt menüsünün altında yer alır.

e-Fatura Parametreleri ekranında yer alan parametreler ve içerdiği bilgiler şunlardır:

| e-Fatura Parametreleri Ekranı |  |
| --- | --- |
| e-Fatura Uygulaması Kullanılsın | İçinde bulunulan şubede e-Fatura uygulamasının kullanılması için işaretlenen parametredir. Aynı veritabanında farklı işletmeler olduğunda, tüm işletmelerde e-Fatura kontrollerinin geçerli olmamasını sağlar. |
| Belge Birim Kod | e-Fatura olarak oluşturulacak faturaların takip edileceği ve gelir idaresine iletilecek olan 3 haneden oluşan fatura numarasının seri kodu bilgisinin tanımlandığı alandır. Boş bırakıldığında faturalar GIB serisinden oluşur. e-Fatura mükelleflerine, uygulama genelinde farklı bir seriden numara verilmesi engellenmiş olup, bu tür faturalar kayıt esnasında yeniden numaralandırılarak burada belirtilen serinin son kaldığı numara ile kaydedilir. e-Fatura Offline lisansı kullanılıyorsa FYS ve GIB serilerinin kullanılması gerekir. Online ve Entegratör lisansında ise herhangi bir üç hanenin tanımlanması yeterlidir. GİB, firmaya iki adet etiket gönderir. Bunlar; Gönderici Birim Etiketi ve Posta Kutusu Birim Etiketi'dir. **Gönderici Birim Etiketi:** VKN veya TC Kimlik Numarası ile birim etiketi eşleştirilir. **Posta Kutusu Birim Etiketi:** Gelen faturalarda posta kutusunu belirten etikettir. |
| Gönderici Birim Etiketi | Gelir idaresinin başvuru sırasında bildirdiği entegrasyon kullanıcı bilgilerindeki GB ETİKET bilgisinin tanımlandığı alandır. |
| Oluşturulacak Zarf Dizini | Gönderilen zarfların kaydedileceği dizindir. Boş bırakıldığında kayıtlar Registry'deki Temelset dizinin altında oluşturulur. |
| Çoklu Belge Birim Kod Kullanılsın | Birden fazla seri kullanılması istendiğinde kullanılan parametredir. İşaretlendiğinde görüntülenen "Çoklu Seri Giriş" ekranı ile seri tanımlamaları yapılır. |
| e-Fatura Basımları Loglansın | Basım loglarının tutulması için kullanılan parametredir. |
| e-Fatura Tevkifat Kodu | Tevkifat uygulamasını kullanan firmaların, e-faturalarını göndereceği tevkifat kodunun tanımlandığı alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, tevkifat kodu seçimi yapılır. |
| İhracat Faturaları e-Fatura Olarak Oluşturulsun | İhracat faturalarının e-Fatura olarak oluşturulması istendiğinde kullanılan parametredir. "İhracat faturaları belge birim kodlarınızı buradan girebilirsiniz." yazısının üzerine tıklandığında görüntülenen "Çoklu Giriş Ekranı" ile birim kodları tanımlaması yapılabilir. |
| e-Fatura Kapsamına Girmeyen İhracat Belgesi Oluşturulabilsin | Bazı firmaların her kapattığı ihracat belgesi e-Fatura kapsamına girmez. Bu şekilde e-Fatura kapsamına girmeyen ihracat belgelerinin oluşturulması için kullanılan parametredir. |
| e-Fatura Senaryosu Değiştirilebilsin | e-Fatura Cari Güncelleme ekranında hangi cari ve hangi e-Fatura senaryosu ile çalışıldığı bellidir. **Örneğin:** Bir firmayla ticari anlaşmalar kapsamında çalışılıyorsa, gönderilen e-Faturalar "Ticari Fatura" kapsamında değerlendirilir. e-Faturanın Temel ve Ticari olarak iki tip senaryosu vardır. Temel Fatura: Anlaşmaya tabi olmayan faturadır. Onay süreci yoktur. Karşı taraf faturayı direkt kabul eder. Ticari Fatura: Anlaşmaya tabi olan faturadır. Onay süreci vardır. Senaryoların değiştirilmesi için "e-Fatura Senaryosu Değiştirilebilsin" parametresinin işaretlenmesi gerekir. "e-Fatura Cari Güncelleme" ekranında yer alan "e-Fatura Senaryosu" kolonu ile senaryo değişikliği yapılır. Cari Hesap Kayıtları ekranından da senaryo değişikliği yapılabilir. **Örneğin:** Ekranda yer alan e-Fatura Mükellefi (Ticari) yazısının üzerine farenin sağ tuşu ile tıklanarak "e-Fatura Senaryosu Değiştirme" seçeneği ile istenen değişiklik yapılabilir. Ürün bazlı senaryo değişikliğinin yapılması için de, faturanın "Toplamlar" sekmesinden senaryo değişikliği yapılabilir. |
| e-İrsaliye Kullanılsın | e-İrsaliye uygulamasının kullanılması için işaretlenmesi gereken parametredir. "e-İrsaliye Belge Birim Kodlarınızı Buradan Girebilirsiniz." yazısının üzerine tıklandığında görüntülenen "Çoklu Giriş Ekranı" ile birim kodları tanımlaması yapılabilir. |
| e-İrsaliye Gönderici Birim Etiketi | e-İrsaliye için e-Faturadan ayrı gönderici birim etiketi tanımlanması amacıyla kullanılan alandır. Eğer bu alan boş bırakılırsa, “Gönderici Birim Etiketi” alanı hem e-Fatura hem de e-İrsaliye için geçerli olacaktır. |
| e-Fatura Eşleştirme Ekranı Fatura Girişinde Gösterilmesin | e-Fatura eşleştirme ekranının fatura girişinde gösterilmemesi için kullanılan parametredir. |
| e-Fatura Eşleştirme Ekranı Dekont Kaydında Gösterilmesin | e-Fatura eşleştirme ekranının dekont kaydında gösterilmemesi için kullanılan parametredir. |
| Cari Etiket Bilgisi Seçilebilsin | Cariye ait birden fazla etiket varsa e-Fatura zarf gönderme aşamasında "Cari Etiket Seçimi" ekranının açılması ve faturanın bu ekrandan seçilen etiket bilgisi ile gönderilmesi için kullanılan alandır. |
| Harici Yolla Yapılan İptallerde Fatura 8 Gün İçinde Silinebilsin | Harici yolla iptali yapılan faturanın, sadece 8 gün içinde silinmesi için kısıt verilmesi istendiğinde seçilmesi gereken parametredir. Fatura iptal işlemi yapıldıktan sonra e-Faturaya ait satış faturası ve ona bağlı hareketler silinir. Faturanın iptal edildiği tarih "Fatura Bazında Giden Kutusu" ekranına eklenen "İptal Tarihi" kolonundan izlenir. |
