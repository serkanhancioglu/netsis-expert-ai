---
title: "Akıllı Kod Uygulaması"
page_id: "50679800"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Akıllı Kod Uygulaması"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Akıllı Kod Uygulaması"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTdhYWQ1NmZlLWIwNDItNGRhYy1hNTMxLWI5ODQ4ODQ3YjkwYiZsaW5rPTE1NjIxMDg2LWMxZTgtNDk0MC05ODhiLTBlZjdmMGY3NjRhZSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=7aad56fe-b042-4dac-a531-b9848847b90b&link=15621086-c1e8-4940-988b-0ef7f0f764ae&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "akilli-kod-uygulamasi_82575756_50679800.html"
source_version: "2022-11-03T09:13:47.207+03:00"
source_bytes: 1101240
fetched_at: "2026-09-13T04:25:49+00:00"
generator: "netsis-scraper 1.0.0"
---
# Akıllı Kod Uygulaması

Akıllı Kod Uygulaması ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Akıllı Kod Uygulaması, ekranın üst kısmında yer alan "Ekstra" adlı menünün listesinde bulunan bir özelliktir.
![](../_assets/b270ec44b73c79e92594.png)
"Akıllı Kod" özelliği ile stok, sipariş, cari gibi istenen tüm kayıt kodlarının (önceden belirlenen bir şablona göre) program tarafından üretilmesi ve kodlarda standardizasyon sağlanır.
![](../_assets/be604c3a69183bdb61de.png) "Akıllı Kod" uygulamasının kullanılması için, öncelikle bu kodların "Akıllı Kod Tasarım Ekranı" kullanılarak tasarlanması gerekir.

#### Akıllı Kod Tasarım Girişi Kod Tanım Ekranı

"Kod Tanımı" ekranında, kodun numarası, açıklaması ve kod bölümleri arasında kullanılacak ayraç bilgisi gibi alanlar tanımlanır.
![](../_assets/ca8f944e456dd38bc660.png)

#### Akıllı Kod Tasarım Girişi Kod Bölümleri Tanım Ekranı

"Kod Bölümleri Tanım" ekranında ilgili kod için detaylı bölüm bilgileri ve varsa kısıtları ayrıntılı olarak belirlenir.
![](../_assets/feea89e28fef59b0e40a.png)
Görünüm kısmındaki tanımlamalar, kod bölümünün üretme ekranındaki görüntüsüyle ilgilidir.

| **Akıllı Kod Tasarım Girişi -** **Kod Bölümleri Tanım** **Ekranı** | Görünüm |
| --- | --- |
| Sıra | Tanımlanan kod bölümünün, kodda hangi sırada yer alacağını gösteren sayının girildiği alandır. |
| Açıklama | Tanımlanan kod bölümünün açıklamasının girildiği alandır. Bu bilgi aynı zamanda, kod üretildiği sırada araç ipucu bilgisi olarak da görülür. |
| Başlık | "Kod Üretme" ekranında görünmesi istenen başlık isminin girildiği alandır. |
| Uzunluk (Karakter) | "Kod Üretme" ekranında, tanımlanan kod bölümünün uzunluğunun, kodun toplam görünüm uzunluğuna oranını gösterir. |

Hesaplama kısmındaki tanımlamalar ise, kod bölümünün içeriğini belirler.

| **Akıllı** **Kod** **Tasarım** **Girişi** - **Kod** **Bölümleri** **Tanım** **Ekranı** | Hesaplama |
| --- | --- |
| Tür | Sabit, SQL ve Script olmak üzere üç tür seçenek yer alır. Sabit seçeneği, sabit değerlerin SQL seçeneği, programın başka alanlarında bulunan kodlara göre belirlenen değerlerin Script seçeneği ise, script yoluyla hesaplanan değerlerin kodda kullanılmasını sağlar. |
| Önceki Bölüm Değerlerinden Etkilenecek | SQL ve Script türleri seçildiğinde aktif olan bu seçenek, mevcut bölüm<br>değeri hesaplanırken, daha önceki pozisyon değerlerinin de etkili olacağını gösterir. |
| Ekrandan Sorulacak | "Ekrandan Sorulacak" seçeneği işaretlenmediğinde üretilen kod "Akıllı Kod Üretme" ekranında sadece başlık olarak görünür. İşaretlendiğinde ise, "Akıllı Kod Üretme" ekranında kod başlığı alanının altına seçenek listesinin de yer aldığı bir hücre eklenir. Böylece, kullanıcının kodlar arasından seçim<br>yapması sağlanır.<br>**Örneğin;** \<ac:structured-macro ac:macro-id="9bdfb284-b136-42ed-8c51-373db3c77c0f" ac:name="unmigrated-wiki-markup" ac:schema-version="1"\>\<ac:plain-text-body\>\[CDATA\[\* \<strongSQL **türündeki** bir kod bölümü için yazılmış SQL cümlesiyle, ilk kod bölümündeki (DIV\[0\]) grup koduna benzeyen kodlar ekrana getirilerek, bunlar arasından kullanıcının seçim yapması \]\]\> sağlanabilir.<br>\<ac:structured-macro ac:macro-id="7b3cbc16-4fdc-4a54-93cd-7fda922b0a0c" ac:name="unmigrated-wiki-markup" ac:schema-version="1"\>\<ac:plain-text-body\>\[CDATA\[\<strongSELECT **GRUP_KOD,GRUP_ISIM** **FROM** **STOKKOD1** **WHERE** **GRUP_KOD** **LIKE** **'{$DIV\[0\]}%'**<br>\]\]\><br>**Script türündeki** bir kod bölümü için yazılmış script örneği, Akıllı Kod için oluşturulmuş olan "SMARTCODE" nesnesini kullanır. Bu nesne ile, istenen kod bölümü scriptte hesaplamaya kolayca dahil edilebilir. Yazılan script ile oluşturulan kod bölümü, "SONUC" adlı değişkene atanır.<br>**if** **SMARTCODE.Divs(1)=1** **then** **sonuc=11**<br>**else** **sonuc=22**<br>**end** **if** |

#### Akıllı Kod Eşleme

"Akıllı Kod Tasarımı" yapıldıktan sonra, akıllı kodlama yapılması istenen alanın üzerine gidilerek "Akıllı Kod Eşleme" programı çalıştırıldığında, bu alan için "Akıllı Kod" üretilmesi sağlanır.
Örneğin; Stok Kodu alanındayken "Akıllı Kod Eşleme" ekranı açıldığında, "Stok Kodu" alanına tanımlı akıllı kodlardan birisi eşlenebilir. Kullanıcıya hangi alanın eşlenme aşamasında olduğunu ekran başlığı gösterir.
![](../_assets/bf887e85c6a152b76310.png)
Ekranın alt kısmında hem içinde bulunulan şube, hem de diğer şubelerde bu kod için eşlenmiş olan akıllı kodlar görünür.

#### Akıllı Kod Üretme

İstenen alan için bir "akıllı kod" eşlendikten sonra, kayıt girişi aşamasında iken "Akıllı Kod Üretme" (Ctrl-J) programı çağrıldığında, eşlenmiş akıllı kod tanımı çalışır. Aşağıda, yeni bir stok kaydı girilirken, stok kodu alanına eşlenmiş bir akıllı kod üretme ekranının görüntüsü yer alır. ("Akıllı Kod Tasarım" ekranında, tasarım tamamlandıktan sonra "Test" butonuna basılarak da bu ekran çağrılabilir ve çalışması test edilebilir.)
![](../_assets/0fd3ef095d003986f922.png)
"Akıllı Kod Üretme" ekranında seçimler yapılıp ![](../_assets/f7512c988eece9aff28e.png) Tamam butonuna basıldığında, oluşturulan kod ilgili alana yazılır. ![](../_assets/43e3af10bf42183adbe3.png) Test butonuyla kod üretme test edildiğinde, oluşan kod ekrana gelir.
![](../_assets/d5270b0666b7da207899.png)
