---
title: "Ortak Paket Çalıştırma Tanımlamaları"
page_id: "24753261"
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
  - "Ortak Paket Çalıştırma Tanımlamaları"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Yardımcı Programlar / Kayıt / Yardımcı Programlar / Ortak Paket Çalıştırma Tanımlamaları"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTM5NDU0NmVjLTk1NWQtNGI2ZC1hZGIzLWY4YmEwZDdkNTNkZSZsaW5rPTQ1MDkyOTkxLWFhOWQtNGJiYy05ZDZlLTgwNzI3MzZmZTk4NCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=394546ec-955d-4b6d-adb3-f8ba0d7d53de&link=45092991-aa9d-4bbc-9d6e-8072736fe984&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ortak-paket-calistirma-tanimlamalari_47072964_24753261.html"
source_version: "2022-10-05T10:06:18.570+03:00"
source_bytes: 88418
fetched_at: "2026-09-13T04:17:23+00:00"
generator: "netsis-scraper 1.0.0"
---
# Ortak Paket Çalıştırma Tanımlamaları

Ortak Paket Çalıştırma Tanımlamaları, Genel Bölümü'nde, "Kayıt/Yardımcı Programlar" menüsünün altında yer alır. Ortak Paket Çalıştırma Tanımlamaları, uygulamaya ait temel tanımlamaların yapılmasını sağlar. Netsis Temelset, Personel ve Demirbaş paketlerinin kullanıldığı durumlarda, bu paketlere giriş için farklı uygulama dosyaları - Ephesus.exe, Netper.exe ve NetDemir.exe - kullanılır. Ayrıca, bu paketlerden herhangi birine giriş yapıldığında mutlaka şirket seçimi, kullanıcı adı ve şifre girişi zorunluluğu bulunur.

Temelset, Personel, Demirbaş paketlerine ve bu paketlerde tanımlı şirketlere tek bir uygulama dosyası ile girilmesi ve kullanılacak Temelset, Personel ve Demirbaş şirketlerinin, birbirleri ile eşleştirilmesi için kullanılan bölümdür. Yapılan eşleştirme sonucu uygulama açıldığında, birbiriyle ilişkili Temelset, Personel ve Demirbaş paketlerindeki şirket ve şubeler aynı satırda gösterilir. Bu uygulama kullanıldığında, şirketlere giriş sırasında kullanıcı adı ve şifre sorgulanmaz. Ayrıca, yapılan tanımlamalar sonucu sık kullanılan sayfalar ve dokümanlar için, uygulama üzerinde kısa yollar oluşturulabilir.

Temelset, Personel ve Demirbaş paketlerine tek bir uygulama ile girilmesi için, program dizini altındaki "Ortak" klasöründe bulunan NetsisPK.Exe dosyasının çalıştırılması gerekir. NetsisPK.exe çalıştırıldığında, uygulamaya giriş için isim ve şifre sorgulanır. Sorgulanan isim ve şifre alanlarının açıklamaları şunlardır:

| Alan | Açıklama |
| --- | --- |
| İsim | “Güvenlik kontrolünün yapılacağı Temelset şirket ve şube bilgisi” alanında seçilen şubede, geçerli kullanıcı adının girildiği alandır. Burada girilen kullanıcının, ilgili şirkette/şubede tanımlı olması gerekir. |
| Şifre | "İsim" alanında girilen kullanıcıya ait şifre bilgisinin girildiği alandır. Bilgiler girildikten sonra Tamam ![](../../../../_assets/39d77b8716226638d9ce.jpg) butonuna basıldığında, "Netsis Paketlerinin Ortak Kullanımı" başlıklı sayfa açılır. Bu ekranın sol tarafında, Yardımcı Programlar → Ortak Paket Çalıştırma Tanımlamaları → Sayfa Adresleri sekmesinden eklenen sayfa bilgileri bulunur. Sayfa bilgileri, tanımlama sırasında belirlenen "Grup Başlığı" bilgisine göre gruplandırılarak ekrana getirilir. Ekranın sağında ise şirket bilgileri ve paket seçimleri bulunur. "Şirket Adı" sütununda, Yardımcı Programlar → "Ortak Paket Çalıştırma Tanımlamaları" bölümünde belirlenen açıklama bilgisi bulunur. Bu açıklamalardan yola çıkılarak, hangi şirkete girileceği belirlenir. Çalışılacak şirketin sağında bulunan sağ ok tuşları ile, girilecek paket bilgisi seçilir. **Örneğin;** ABC şirketinin İzmir şubelerine ait 2019 personel bilgilerinin tutulduğu şirkete giriş yapılması için, "Şirket Adı" sütununda bulunan açıklamadan yola çıkarak, ilgili şirket için eşleştirmenin yapıldığı satırda ve "Personel" başlıklı sütunda bulunan sağ ok tuşuna tıklanması yeterlidir. Bu bölümden paketlere giriş sırasında tekrar kullanıcı adı ve şifre bilgisi sorgulanmaz. |

Ortak Paket Çalışma Tanımlamaları ekranı, Güvenlik ve Paket Eşleştirme, Sayfa Adresleri olmak üzere iki sekmeden oluşur.

**Güvenlik ve Paket Eşleştirme**

Güvenlik ve Paket Eşleştirme sekmesi, güvenlik kontrolü yapılacak şirketin belirlenmesi ve ortak girişlerin yapılacağı şirketlerin eşleştirilmesi için kullanılır.

![](../../../../_assets/64b9257d673a79e03b01.png)

Ortak Paket Çalıştırma Tanımlamaları ekranı Güvenlik ve Paket Eşleştirme sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Ortak Paket Çalıştırma Tanımlamaları Ekranı |  |
| --- | --- |
| Güvenlik Kontrolünün Yapılacağı Temelset Şirket ve Şube Bilgisi | "Ortak Paket Çalıştırma" uygulamasında, Temelset, Personel ve Demirbaş paketlerine giriş için tek bir uygulama dosyası kullanılır ve seçilen şirketlere bağlantı yapmak için kullanıcı şifresinin girilmesi gerekmez. Ancak, Ortak Paket Çalıştırma ile ilgili uygulama dosyası çalıştırıldığında, bir defaya mahsus kullanıcı adı ve şifre sorgulanır. "Güvenlik Kontrolünün Yapılacağı Temelset Şirket ve Şube Bilgisi" alanı, "Ortak Paket Çalıştırma" uygulamasına girişte sorgulanan "Kullanıcı Adı" ve "Şifre" bilgisinin tanımlanacağı şirket ve şubenin girilmesi için kullanılır. Böylece, "Ortak Paket Çalıştırma" uygulamasına bağlanmak için girilen kullanıcı adı ve şifre bilgisinin, bu alanda seçilen şirketteki şubede geçerli olup olmadığı kontrol edilir. Ortak paket kullanımında sadece bir defa isim/şifre sorgulanır. Farklı şirketlere geçişte bir daha isim/şifre sorgulanmaz. Belirlenen şirketteki kullanıcıların, ortak paketle girilecek tüm şirketlerde geçerli haklarının olduğu varsayılır. |
| **Paket Eşleştirme Bilgileri** | Ortak uygulama ile girilmesi istenen şirket bilgilerinin tanımlandığı alandır. |
| **![](../../../../_assets/a6d9b16dcee989ae7d09.png) Şirket Ekle** | Temelset, Personel ve Demirbaş paket eşleştirmesinin yapılacağı boş bir satır eklemek için kullanılan butondur. |
| **![](../../../../_assets/dce9e24e321dfe8fb7c4.png) Şirket Sil** | Eklenen satırın silinmesi için kullanılan butondur. Silinmesi istenen satır fare ile seçildikten sonra bu butona basıldığında daha önceden eklenen satır silinir. |
| ![](../../../../_assets/53859e19eb2737b88a17.jpg) Sakla | Girilen bilgilerin saklanması ve değişikliklerin kaydedilmesi için kullanılan butondur. |
| Açıklama | Satırda yapılan eşleştirmelere ait açıklamanın girildiği alandır. "Ortak Paket Çalıştırma" uygulamasında, eşleştirmelerde seçilen şirket bilgileri yerine girilen açıklama gösterilir. Bu yüzden açıklamanın, eşleştirme sırasında seçilen şirketlere ait bilgi verecek şekilde girilmesinde fayda vardır. **Örneğin** Temelset paketindeki bir şirketin birden fazla şubesinin olduğunu ve Personel ile Demirbaş paketlerinde de şube bazında takip edildiği varsayıldığında, Temelset paketindeki İzmir şubesi ile "Personel" ve "Demirbaş" paketlerindeki İzmir şirketleri eşleştirildiği zaman açıklamada, eşleştirilen paket bilgilerinin İzmir şubesine ait olduğunu belirten bir ibare olması kullanım sırasında kolaylık sağlar. Açıklama alanı, alan üzerine fare ile geldikten sonra, farenin sol tuşu ile iki kez tıklandığında veya klavyede yer alan boşluk tuşuna basıldığında aktif hale gelir. Açıklama girildikten sonra klavyede yer alan \<enter\> tuşuna basılarak diğer alanlara ilerlenir. |
| Temelset | Eşleştirmesi yapılacak Temelset paketindeki şirketin belirlendiği alandır. Alan üzerine farenin sol tuşu ile iki kez tıklandığında veya klavyede yer alan boşluk tuşuna basıldığında, Temelset paketinde tanımlı tüm şirketlere ait şubeler listelenir. Alanın sağ tarafında bulunan aşağı ok butonuna basarak tüm şirketlere ulaşılır. Eşleştirmesi yapılacak şirket şubesi seçildikten sonra klavyede yer alan \<enter\> tuşuna basılarak diğer diğer alanlara ilerlenir. |
| Temelset Kulanıcı | Temelset alanında seçilen şubeye giriş sırasında kullanılacak kullanıcı adının girildiği alandır. Girilecek kullanıcı bilgisinin, seçilen şubedeki "Kullanıcı Kayıtları" bölümünden tanımlanması gerekir. |
| Personel | Eşleştirmesi yapılacak Personel paketindeki şirketin girildiği alandır. Alan üzerine farenin sol tuşu ile iki kez tıklandığında veya klavyede yer alan boşluk tuşuna basıldığında, Personel paketinde tanımlı tüm şirketlere ait şubeler listelenir. Alanın sağ tarafında bulunan aşağı ok butonuna basarak tüm şirketlere ulaşılır. Eşleştirmesi yapılacak şirket şubesi seçildikten sonra klavyede yer alan \<enter\> tuşuna basılarak diğer diğer alanlara ilerlenir. |
| Personel Kullanıcı | Personel alanında seçilen şirkete giriş sırasında kullanılacak kullanıcı adının girildiği alandır. Girilecek kullanıcı bilgisinin, seçilen şirketteki "Kullanıcı Kayıtları" bölümünden tanımlanması gerekir. |
| Demirbaş | Eşleştirmesi yapılacak Demirbaş paketindeki şirketin girildiği alandır. Alan üzerine farenin sol tuşu ile iki kez tıklandığında veya klavyede yer alan boşluk tuşuna basıldığında, Demirbaş paketinde tanımlı tüm şirketlere ait şubeler listelenir. Alanın sağ tarafında bulunan aşağı ok butonuna basarak tüm şirketlere ulaşılır. Eşleştirmesi yapılacak şirket şubesi seçildikten sonra klavyede yer alan \<enter\> tuşuna basılarak diğer diğer alanlara ilerlenir. |
| Demirbaş Kullanıcı | Demirbaş alanında seçilen şirkete giriş sırasında kullanılacak kullanıcı adının girildiği alandır. Girilecek kullanıcı bilgisinin, seçilen şirketteki "Kullanıcı Kayıtları" bölümünden tanımlanması gerekir. |

**Sayfa Adresleri**

Sayfa Adresleri, sık kullanılan sayfa ve dokümanlara ait adres bilgilerinin tanımlandığı sekmedir.

![](../../../../_assets/a199bb8f69c151b6d33d.png)

Ortak Paket Çalıştırma Tanımlamaları ekranı Sayfa Adresleri sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Ortak Paket Çalıştırma Tanımlamaları Ekranı |  |
| --- | --- |
| ![](../../../../_assets/7d423e87f871348568d8.png) Sayfa Ekle | Tanımlama alanına satır eklemek için kullanılan butondur. Sık kullanılan sayfa ya da belgelere adres verilmesi için öncelikle bu buton kullanılarak tanımlama alanında boş bir satır oluşturulması gerekir. |
| ![](../../../../_assets/ffeea578cc95ddf68075.png) Sayfa Sil | Tanımlama alanına eklenen satırların silinmesi için kullanılan butondur. |
| **![](../../../../_assets/9ad00862780643033a02.png)**Sayfa Aç | Tanımlama alanında adresi bilgisi girilen sayfanın açılması için kullanılan butondur. Açılması istenen sayfaya ait adresin bulunduğu satırdaki hücrelerden herhangi biri seçildikten sonra "Sayfa aç" butonuna tıklanması gerekir. |
| Grup başlığı | Tanımlanan sayfaların "Ortak Paket Çalıştırma" uygulamasında belli gruplar halinde listelenmesi için kullanılan alandır. Örneğin; Netsis ile ilişkili sayfaların Netsis başlığı altında listelenmesi için, bu sayfalara ait tanımlamalarda grup başlığı olarak Netsis girilmesi gerekir. Tanımlanan sayfa adresinin herhangi bir grup altında listelenmemesi için boş bırakılabilir. |
| Başlık | "Ortak Paket Çalıştırma" uygulamasında, bu bölümde belirlenen sayfa adresleri yerine başlık bilgisi görüntülenir. Dolayısıyla, herhangi bir sayfa ya da belgenin, bu uygulamada görüntülenmesi ve açılması için mutlaka başlık bilgisinin girilmesi gerekir. |
| Sayfa adresi | "Ortak Paket Çalıştırma" uygulamasına eklenen sayfa ve doküman adresinin girildiği alandır. Uygulama ile dokümanların açılması için, doküman isimlerinde boşluk bırakılmaması gerekir. |
