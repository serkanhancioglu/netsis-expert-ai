---
title: "Netsis Dil Düzenleyicisi"
page_id: "24753254"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Genel"
  - "Yardımcı Programlar"
  - "Kayıt / Yardımcı Programlar"
  - "Netsis Dil Düzenleyicisi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Yardımcı Programlar / Kayıt / Yardımcı Programlar / Netsis Dil Düzenleyicisi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTgyZDRiOTI2LTAzOTAtNDVmMi04M2ZiLWNmODBhZDEzNmQyOSZsaW5rPTFjMWE2Y2FmLTM0YWMtNGFlMi05NWQzLWE4OTJkNTRkMDQ1OCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=82d4b926-0390-45f2-83fb-cf80ad136d29&link=1c1a6caf-34ac-4ae2-95d3-a892d54d0458&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-dil-duzenleyicisi_47072903_24753254.html"
source_version: "2022-10-05T09:48:14.610+03:00"
source_bytes: 350618
fetched_at: "2026-09-13T04:17:20+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis Dil Düzenleyicisi

Netsis Dil Düzenleyicisi, Genel Bölümü'nde, "Kayıt/Yardımcı Programlar" menüsünün altında yer alır. Menü ve saha başlıklarının kullanıcılar tarafından değiştirilmesini sağlar. Netsis Dil Düzenleyicisi uygulaması ile ayrıca; Türkçe, İngilizce, Farsça dışında program tarafından desteklenmeyen herhangi bir dilde kullanım için; saha başlıklarının, menü seçeneklerinin ve açıklamalarının istenen dile göre karşılıkları programa tanıtılabilir.

Netsis’in tüm modüllerindeki başlık, açıklama, uyarı gibi ifadeler program dosyalarından ayrı bir kaynak kütüphanesi durumundadır. Bu kütüphanede tüm ifadelerin Türkçe ve İngilizce karşılıkları yer alır. Kaynak kütüphanede yer alan ifadeler, kullanıcı isteklerine göre değiştirilebilir ya da aynı ifadelerin karşılıkları tamamen farklı bir lisanda girilerek programın yeni bir lisan ile çalışması sağlanabilir.

Kaynak Dil, Hedef Dil ve Netsis Modül alanlarında verilen kısıtlara göre; modüller, açıklamalar ve bu açıklamaların kaynak kütüphanedeki mevcut durumu listelenir.

![](../../../../_assets/48aab7246a941cdacab4.png)

Netsis Dil Düzenleyicisi ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Netsis Dil Düzenleyicisi Ekranı |  |
| --- | --- |
| Kaynak Dil/Hedef Dil | Kaynak Açıklama ve Hedef Açıklama alanlarına aktarılacak ifade dilinin belirlendiği alandır. Programda mevcut ifadelerin görüntüleneceği dil seçimi "Kaynak Dil" alanından yapılır. "Hedef Dil" alanı ise, değişiklik yapılacak ifadeler için dil seçiminde kullanılır. Alanın sağ tarafında yer alan aşağı ok butonu ile seçim yapılır. **Örneğin,** İngilizce açıklamalara göre Farsça açıklamalar düzenlenecek ise; Kaynak Dil alanında İngilizce, Hedef Dil alanında ise Farsça seçilmesi gerekir. Netsis Dil Düzenleyicisi şu an için; Türkçe, İngilizce, Farsça, Rusça, Azerice ve Arapça dillerini destekler. |
| Netsis Modül | Açıklamaları listelenecek modülün belirlendiği alandır. Seçilen modülde bulunan tüm menü ve saha başlıkları ile açıklamalar, seçilen dillere göre listelenir. Alanın sağ tarafında yer alan aşağı ok butonu ile seçim yapılır. |
| **![](../../../../_assets/acc30dfb93fdf7e123ee.png)**Raporla | Belirlenen dil ve modül seçeneklerine göre kaynak ve hedef açıklamalarının listelenmesi için kullanılan butondur. |
| **![](../../../../_assets/fb48615af1abcfa9ec6a.png)** XLS, HTML, XML, TXT | Hedef ve Kaynak Açıklama sahaları listelendikten sonra aktif hale gelen butonlardır. "Dışarı al" butonları kullanılarak, listelenen ifadeler Excel, Html, Xml veya Metin Dosyası olarak saklanabilir. Bu sayede mevcut yapıda desteklenmeyen bir dile ait bilgiler girilerek yapılan değişiklikler, daha sonra DTS ile istenen herhangi bir Netsis veritabanında bulunan NETKULDILLERI tablosuna aktarılır. Kaynak Dil, Hedef Dil ve Netsis Modül alanlarında tanımlama yapıldıktan sonra Raporla *![](../../../../_assets/acc30dfb93fdf7e123ee.png)* butonuna tıklandığında, kısıtlara uygun satırlar Modül, Kod, Kaynak Açıklama ve Hedef Açıklama başlıkları altında listelenir Gelen bilgilerin, herhangi bir sütuna göre artan veya azalan şekilde sıralanması mümkündür. **Örneğin;** bilgilerin "Kaynak Açıklama" sütununa göre artan şekilde sıralanması için, farenin sol tuşu ile “Kaynak Açıklama” yazısının üzerine tıklanması gerekir. Sütun başlıklarının yanında bulunan aşağı ok tuşuna basıldığında görüntülenen ekranda, ilgili sütunda yer alan bilgiler için kısıt verilebilir. ![](../../../../_assets/b2ca581bcc6f3bb94e86.png) (All) seçeneğine farenin sol tuşu ile tıklandığında, ilgili sütuna ait tüm bilgiler ekrana gelir. ![](../../../../_assets/49708120fadbe7a35d9d.png) (Custom...) seçeneğine tıklandığında, ilgili sütun için kısıt verilmesini sağlayan bir ekran görüntülenir. ![](../../../../_assets/88eafebcfac7bc1b6047.png) Kişisel filtreleme ekranındaki alanların sağ tarafında yer alan aşağı ok butonları ile; Benzer, Benzemez, Boşluktur, Boşluk Değildir seçenekleri seçilerek maskeleme yapılabilir. Benzer ve Benzemez seçenekleri, verilen kısıtı sağlayan ya da sağlamayan kayıtları, Boşluktur ve Boşluk Değildir seçenekleri ise, ilgili satır açıklaması boşluk olan ya da boş olmayan - dolu olan - kayıtları ifade eder. **Örneğin,** herhangi bir dildeki alanın satır açıklaması boşsa ve bu boş olan satırların listelenmesi isteniyorsa, kısıt verilirken "Boşluktur" alanının kullanılması gerekir. Kısıt verilirken “\_” tek bir karakteri, “%” ise birden fazla karakteri ifade eder. Birden fazla kısıt verilirken "Ve" seçeneği kullanılırsa iki koşulu da aynı anda sağlayan kayıtları, "Veya" seçeneği kullanılırsa iki kısıt arasından en az birini sağlayan kayıtlar listelenir. Maskeleme yapılırken Benzer %kod% şeklinde bir kısıt verilirse Hedef ya da Kaynak Açıklaması içinde kod geçen kayıtlar listelenir. Ekrana getirilmesi istenen açıklamalara kısıt verilmesi halinde, verilen kısıta uygun ifadeler listelenir. Kısıtı kaldırarak listelemek için, ekranda sol alt köşede oluşan seçenek tuşu kullanılır. Tuşa bir kez tıklandığında kayıtlar, verilen kısıt dikkate alınmadan listelenir. İkinci kez basıldığında ise kısıta uyan kayıtlar tekrar ekrana getirilir. Herhangi bir sütun için verilen kısıt bilgisi yine bu ekrandan izlenir. Ayrıca, "Netsis Modül" alanında "Bütün Modüller" seçeneğinin seçilmesi halinde alt tarafa gelecek açıklamalar için modül bazında gruplandırma yapılır. Gruplandırma yapmak için “Modül” saha başlığının, fare ile sürüklenerek yukarı taşınması gerekir. Böylece her modülde bulunan açıklama sayısı izlenebilir. Bu işlem yapıldıktan sonra ekran, "Modül" alanına göre gruplanarak görüntülenir. "Netsis Dil Düzenleyicisi" ekranında "Hedef Açıklama" alanında görülen ifadeler değiştirilebilir. Açıklamasında “&” sembolü bulunan kayıtlarda, önce “&” sembolü gelen karakter kısa yol tuşu için kullanılır. Bu kayıtlar, menülerde kullanılır. Netsis Dil Düzenleyicisi ile, birden fazla kaydın açıklaması toplu olarak değiştirilebilir. Bunun için, açıklaması değiştirilecek satırlar seçildikten sonra farenin sağ tuşuna basılması gerekir. Açılacak menüdeki "Ortak Atama" seçeneği ile, seçilen sahalara atanacak ortak açıklamanın girilmesini sağlayan ekran görüntülenir. |
| ![](../../../../_assets/89e57093bea74b501643.png) Değişiklikleri Kaydet | Değişikliklerin saklanması için kullanılan butondur. Değişiklerin programa yansıması için programdan tamamen çıkartılıp tekrar girilmesi gerekir. Programdan çıkılıp tekrar girildikten sonra artık menü başlığı programda kullanıcının değiştirdiği şekilde görünür. |
