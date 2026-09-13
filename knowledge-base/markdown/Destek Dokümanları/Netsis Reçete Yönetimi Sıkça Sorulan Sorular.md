---
title: "Netsis Reçete Yönetimi Sıkça Sorulan Sorular"
page_id: "50684113"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis Reçete Yönetimi Sıkça Sorulan Sorular"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis Reçete Yönetimi Sıkça Sorulan Sorular"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTRmZjYxNWExLWQ4ZGYtNGE0OC1hYWQ1LTU5ZGM3ODNlMmE0MiZsaW5rPThjZTlkMjQ0LTBhZTctNGExNi05NGQ4LTVjYjk2M2ZiM2JkNCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=4ff615a1-d8df-4a48-aad5-59dc783e2a42&link=8ce9d244-0ae7-4a16-94d8-5cb963fb3bd4&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-recete-yonetimi-sikca-sorulan-sorular_50684116_50684113.html"
source_version: "2020-11-13T17:53:07.607+03:00"
source_bytes: 688239
fetched_at: "2026-09-13T04:26:27+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis Reçete Yönetimi Sıkça Sorulan Sorular

**Soru 1: Reçete Nedir?**

Üretimi gerçekleştirilecek olan mamulün, üretiminde kullanılacak bütün bileşen ve operasyonların miktar ver süre bilgilerinin yer aldığı listedir.

**Soru 2: Netsis'te kaç farklı şekilde reçete oluşturulabilir?**

Temel reçete kaydı ile toplamda altı farklı yöntem ile reçete oluşturulabilir. Bu yöntemler reçete kaydı, ürün konfigüratörü, alternatif malzemeler, alternatif reçete, iş emrine bağlı reçete kaydı, süper reçete ve planlanan bileşen değişiklikleri ekranlarıdır.

**Soru 3: Üretimde gerçekleşen fire kayıplarının takibi reçete üzerinde nasıl yapılmaktadır?**

Üretim parametrelerinde "2. Miktar girilecek" parametresi işaretli olmalıdır. Bu parametre işaretlendiği takdirde reçete kaydı ve üretim sonu kayıtlarında 2.miktar alanına girilen değerler fire olarak kabul edilir.

**Soru 4: Ürün konfigüratörü neden kullanılır ve nasıl çalışır?**

Ürün konfigüratörü ekranı mevcut reçetelerin güncellenmesi ya da yeni bir reçetenin oluşturulması için kullanılan, reçete kaydı ekranından daha pratik ve hızlı bir ekrandır. Ürün konfigüratörü ekranından oluşturulan reçetelerde kullanılan bileşen ve operasyonların daha önceden sistemde kartlarının açılması zorunlu değildir. Bu ekran sayesinde stok kartları, operasyon kartları ve bunlara bağlı reçete kayıtları otomatik açılır. Bu ekranda sistemdeki stok ve operasyonlarla beraber henüz sisteme tanımlanmamış stok ve operasyonlar beraber kullanılabilir.

**Soru 5: Alternatif reçete nedir?**

Alternatif reçete, üretimi gerçekleşecek olan mamul/yarı mamulün orijinal reçetelerini değiştirmeden, bu reçeteye alternatif birden fazla reçete oluşturulmasına olanak sağlar.

**Soru 6: Alternatif reçete kayıtları nasıl oluşturulur?**

Üretim\\Kayıt altından alternatif reçete ekranına erişilebilir. Bu ekranda Alt.Kodu "0" olan değer orijinal reçeteyi gösterir. Burada yeni denilerek birden fazla alternatif kodlu reçete istenilen bileşen ve operasyonu içerecek şekilde oluşturulabilir.

![](../_assets/2005d0af4bffdce6d6bc.png)

**Soru 7: Alternatif reçete hangi ekranlarda desteklenmektedir?**

Alternatif reçete kodu , iş emri girişi esnasında, üretim sonu kaydı /serbest üretim sonu kaydı ve MRP ekranında desteklenmiştir. MRP ekranında kullanılabilmesi için sipariş bazında rezervasyon sisteminin kullanılıyor olması gerekmektedir. Aynı zamanda üretim parametrelerinde alternatif reçete bilgisinin müşteri siparişlerinde hangi alanda tutulacağı bilgisi tanımlanmalıdır. Böylece MRP çalışırken, müşteri siparişlerinde girilmiş olan alternatif kodu dikkate alacak ve ihtiyaçlar bu alternatif reçeteye göre belirlenecektir.

**Soru 8: Alternatif malzeme tanımlaması ne işe yarıyor?**

Orijinal reçeteyi bozmadan, bu reçete içinde yer alan herhangi bir bileşen ya da operasyonun yerine kullanılabilecek alternatif başka bir bileşen ya da operasyonun tanımlanmasıdır. Bir bileşen ya da operasyonun birden fazla alternatif malzemesi olabilir. Bu tanımlama ekranı ile gerçek reçete bozulmadan, içindeki malzemelerin alternatifleri kullanılarak aynı mamulün farklı malzemelerle üretilmesi sağlanabilir.

![](../_assets/cfcde94abedfc9e1fc4a.png)

**Soru 9: Alternatif malzeme tanımının çalışması için sistemde yapılması gereken diğer tanımlamalar nelerdir?**

Alternatif malzemeler, alternatif politikalarla birlikte çalışır. Bu nedenle reçete kaydı ekranında ve alternatif malzeme ekranında politikalar için gerekli olan bilgiler girilmelidir. Aynı zamanda reçete kaydı üzerinde alternatif malzemenin hangi işlem esnasında çalışacağı da belirtilmelidir. Alternatif malzemelere depolar arası transfer, ambar çıkış fişi, üretim sonu kaydı ve MRP ekranlarında desteklenir.

**Soru 10: Planlanan bileşen değişikliği ekranında reçeteler nasıl yönetilmektedir?**

Planlanan bileşen değişikliği ile belirli bir tarihten sonra ilgili reçete kaydı içinde istenen bileşenlerin kaldırılması ya da yeni bir bileşenin eklenmesi sağlanabilir. Alternatif malzemeden farklı olarak, bu ekrandan orijinal reçetenin değiştirilmesi sağlanabilir. Bu ekranda yer alan "Plana Yansıt" butonu ile orijinal reçete değişmeden, belirlenen politikalara ve tarih aralığına göre bileşenler kullanılır. "Reçete Yansıt" butonu ile de orijinal reçete içinde yer alan bileşenin yeni bileşenle belirlenen tarihe göre yer değiştirmesi sağlanır.

**Soru 11: İş emrinden reçete oluşturma ile reçete nasıl oluşmaktadır?**
İş emri kaydı ekranında iş emri saklansın parametresi işaretlenerek ilgili iş emrinin reçete kaydı orijinal reçeteden oluşturulur. İş emri ekranından yer alan iş emri reçetesi sekmesine geçildiğinde bu alan istenen bileşen ve operasyonlarda değişiklik yapılarak iş emri reçetesi oluşturulur.

**Soru 12: İş emrinden reçete oluşturma ekranı ile reçete içindeki tüm seviyelere müdahale edilebilir mi?**

İş emrinden reçete oluşturma ekranı tepe mamulün bir alt seviyesinde değişiklik yapılmasına izin verir. Tepe mamul altında yer alan yarı mamullerin içinde de değişiklik yapılmak isteniyorsa bu yarı mamullerin reçetelerinde "Oto.Reç" seçili olmalıdır. Aksi takdirde müdahale edilemez.

**Soru 13: Esnek yapılandırma kullanıldığında, yapılandırma kodu bazında reçete nasıl oluşturulur?**

Süper reçete ekranı ile esnek yapılandırmalı mamuller için istenen özelliklere göre farklı reçeteler oluşturulabilir. Bu ekranında kullanılabilmesi için stok parametrelerinden "Esnek Yapılandırma" uygulaması açık olmalıdır. Aynı zamanda bu ekrandan tanımlanacak reçetelerde yer alan mamullerin stok kartlarında esnek yapılandırma ve süper reçete parametreleri açık olmalıdır.

**Soru 14: Süper reçete oluşturma nasıl yapılır?**

Süper reçete ekranında yer alan script bölümü ile yapılandırma kodu bazında reçetelerin oluşturulabilmesi sağlanır. Bu işlemleri gerçekleştirebilmek için, reçetesi tanımlanacak mamullerin, yarı mamullerin ve bileşenlerin esnek yapılandırma tanımları yapılmış olmalıdır.

**Soru 15: Sistemde reçete önceliklendirmesi hangi sırayla gitmektedir?**

Sistemde öncelikli olarak iş emri reçetesine bakılır. Hemen ardından aynı hiyerarşi sırasında olan alternatif reçete ve ürün konfigüratörü gelir. İkisinin de bulunması halinde her ikisi birden kullanılır. Ardından planlanan bileşen değişikliklerine ve alternatif malzemelere bakılır. Bu iki uygulama da hiyerarşik olarak aynı seviyede bulunur ve iki tanımın da bulunduğu durumda her ikisi de kullanılır. Son olarak ise temel reçeteye bakılır.
