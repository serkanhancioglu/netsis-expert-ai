---
title: "Kapasite Planlama"
page_id: "50679981"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Kapasite Planlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Kapasite Planlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTRkMGZhNjc2LThkYWYtNDk4Yi04ZWM0LTJkNzA0ZWJlYTE3ZCZsaW5rPWQxMzIyOWM1LTY0YzgtNDViZS05NzA4LWE1NmQ3NzQ4NzJiYiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=4d0fa676-8daf-498b-8ec4-2d704ebea17d&link=d13229c5-64c8-45be-9708-a56d774872bb&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "kapasite-planlama_82576272_50679981.html"
source_version: "2022-11-03T09:30:07.400+03:00"
source_bytes: 892632
fetched_at: "2026-09-13T04:25:59+00:00"
generator: "netsis-scraper 1.0.0"
---
# Kapasite Planlama

Kapasite Planlama ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

|  |  |
| --- | --- |
| Ürün Grubu | \[X\] Netsis Enterprise<br>\[X\] Netsis Standard |
| Modül | \[X\] MRP2 |
| Kategori | \[X\] Yeni Fonksiyon |
| Versiyon Önkoşulu | 8.0.6 |
| Uygulama | MRP çalıştırılırken kapasite kısıtlarının da dikkate alınmasını ve MRP sonuçlarından açılacak belgelerin kapasite planına uygun şekilde oluşmasını sağlayacak uygulamadır.<br>Kapasite planlama için kullanılacak varsayılan parameteler MRP modülü parametreleri üzerinden belirlenebilir. **Planlama Verisi:** Kapasite planlama sırasında kullanılacak rota, üretim süreleri ve vardiya planı verilerinin nereden alınacağının seçimi için bu parametre kullanılabilir. Planlama Verisi parametresinin alabileceği değerler ve açıklamaları aşağıdaki gibidir: **Kapasite planlama verisi kullanılsın:** Kapasite planlama işleminde, MRP modülünde bulunan istasyon, operasyon, makine ve fabrika takvimi tanımları ile yeni hazırlanan rota tanımlama (MRP \\ Kayıt) bölümünde tanımlanacak rotaların kullanılması için bu seçenek seçilmelidir. **Reçeteden getirilsin:** Rota bilgileri (operasyon ve üretim süreleri) hali hazırda reçete kayıtlarında bulunan müşteriler bu seçeneği kullanabilir. **Çizelgeme üzerinden getirilsin:** Çizelgeleme uygulaması kullanan ve ayrıntılı rota tanımları bulunan müşteriler isterse bu seçeneği seçebilir. Çizelgeleme detayında işlem yapılmak istenmediği durumda "Kapasite Planlama Verisi" seçilebilir. **Dengeleme Politikası:** Kapasite planlama sırasında ilgili periyotta yeterli kapasite bulunamadığı durumlarda geriye doğru dengeleme yaparak ihtiyacı önceki dönemlerde yeterli kapasitenin bulunduğu tarihlere planlamak için bu parametre seçilebilir. Parametrenin alabileceği değerler: Geriye doğru dengeleme yapılsın, Dengeleme yapılmasın **İhtiyaçlar Bölünebilsin:** Geriye doğru dengeleme yapılırken veya aynı periyod içinde bulunan alternatif kapasite merkezlerinin kullanımı sırasında ihtiyaç miktarlarının farklı tarihlere ve/veya kapasite merkezlerine bölünebilmesi için bu parametre işaretlenebilir. Örneğin böyle bir durumda geriye doğru dengeleme yapılıyorsa 2. haftaya ait 1000 adetlik bir ihtiyacın 500 adetlik kısmı 2. haftaya planlanırken, geri kalan kısmı da kapasite aşımından dolayı 1. haftaya planlanabilir. |

#### ![](../_assets/7c62c3bb4f5a11577a23.png)

Rota Tanımlama

Rota Tanımlama ekranı, kapasite planlama parametrelerinde planlama verisi olarak "kapasite planlama verisi kullanılsın" seçildiğinde aktif olan ekrandır. Bu ekran üzerinden seçilecek ürün veya ürün gruplar için toplu halde rota tanımı yapılabilir ve rotada yer alan operasyonlar için üretim süreleri belirlenebilir.
Ekran iki sekmeden oluşmaktadır. Bu sekmeler ve yapılabilecek işlemlerin ayrıntısı aşağıda sırasıyla anlatılmaktadır.

Stok Seçim Sekmesi

Stok Seçim bölümünde ürün kodu, ürün grubu veya tüm ürünler bazında işlem yapılabilmektedir. Ekranın alt bölümündeki listede seçilen ürün tipine göre kayıtlar listelenmektedir. Daha önceden bu ürünler için yapılmış olan rota tanımları da raporlanmaktadır.
Listeden işlem yapılacak ürünler seçildikten sonra "İleri" butonuna tıklayarak bir sonraki sekmeye geçilebilir. Aynı zamanda seçili satırlar için "Rota Sil" butonu yardımıyla daha önceden tanımlanmış olan rotalar toplu halde silinebilir.

![](../_assets/61553a2d17353cc571b9.png)![](../_assets/b141d803175727eb2377.png)

#### Rota Sekmesi

Rota sekmesi bölümünde, seçili ürünler için ortak rota tanımlanabilir ya da eğer seçilen ortak rota mevcutsa güncelleme yapılabilir. Rotaya operasyon ekleyip çıkarmak için rota ağacının üstünde yer alan aşağıdaki butonlar kullanılabilir:
Rotaya yeni operasyon eklemek için kullanılır. Rotadaki seçili operasyonu silmek için kullanılır. Rotadaki bir operasyon seçildiğinde tanımlı üretim süresi alt bölümdeki grid ekranda listelenir. Üretim süresinde güncelleme yapılabilir. Aynı operasyon için alternatif bir istasyon veya makine seçilerek yeni üretim süresi girilebilir. Yapılan tanımlamaları kaydetmek için "Rota Bilgilerini Kaydet" butonuna tıklanmalıdır.
![](../_assets/c6cb0eabb43a647ecdd8.png)

#### MRP'de Kapasite Kullanımı

MRP çalıştırılmadan önce ekrana gelen parametreler içinden "Kapasite kullanımları kontrol edilsin" parametresi seçildiğinde MRP sırasında kapasite planlama işlemi yapılacaktır ve mrp sonuçları da kapasite planına uygun olacak şekilde oluşturulacaktır. Bu parametre işaretlendiğinde "kapasite planlama" sekmesi aktif hale gelmektedir ve MRP öncesinde kapasite planlama parametreleri bu bölümden değiştirilebilir.
Not: MRP sırasında kapasite planlama uygulamasının aktif olabilmesi için MRP2 ek lisansının bulunması gerekmektedir. Ayrıca MRP parametrelerinden "sipariş bazında rezervasyon sistemi" seçilmiş olmalıdır.
Kapasite planlama sekmesinde sonuç raporunun gösteriminde kullanılacak periyod cinsi seçilebilir. Kapasite planlama sonuçlarını günlük, haftalık, aylık periyod tiplerinde raporlamak mümkündür.
MRP parametrelerinde kapasite planlama verisi parametresi "çizelgeleme üzerinden getirilsin" seçildiyse "Vardiya Tercihleri" bölümü aktif olmakta ve farklı vardiya planı senaryolarına göre kapasite planı yapılabilmektedir.
Kapasite kullanımlarını dikkate alarak çalıştırılan MRP sırasında stok planlama kayıtlarındaki üretim/bildirim süreleri dikkate alınmayacaktır. Bunun yerine rota üzerindeki üretim süreleri kullanılmakta ve üretimler istasyon/makinelere yerleştirilerek, süreler gerçeğe çok daha yakın bir şekilde hesaplanmaktadır.
MRP çalıştırıldıktan sonra gelen rapordaki "Kapasite Grafik Sonuçları" sekmesinde aşağıdaki şekilde kapasite kullanımlarının gösterildiği bir grafiksel rapor bulunmaktadır.
![](../_assets/686cdb7c2e03f22c04f9.png)![](../_assets/17bf6e5f2e5ec2107716.png)
Bu raporda fabrika ve istasyonlar bazında doluluk oranlarını dönemler bazında izlemek mümkündür. Herhangi bir dönemde veya istasyonda kapasite kullanımı %100 üzerine çıkıyorsa, bu bilgiyi tarih veya istasyon kodları yanındaki kırmızı ünlem işaretinden anlamak mümkündür. Kapasite kullanımlarının gösterildiği herhangi bir kutuya tıklandığında o istasyonun ilgili dönemdeki iş listesine ulaşılabilir. Ekranın sol üst bölümündeki "Döndür" butonuna tıklayarak tarih ve istasyon kodlarını gösteren eksenlerin yer değiştirmesi sağlanabilir. İstasyon koduna ait detay bilgiye makineler bazında ulaşmak için istasyon kodunun üzerine tıklanabilir. Bu durumda istasyon bazında detaylı kapasite raporuna ulaşılabilir:
İstasyon bazında kapasite raporunun sol bölümünde istasyonda yer alan makineler listelenmekte ve makineler bazında ortalama doluluk oranları görülmektedir. Ayrıca her makine için zaman ekseninde değişkenlik gösteren doluluk oranları sağ bölümde gösterilmektedir. Zaman ekseninde gösterilen çizgi grafiğindeki herhangi bir noktaya tıklandığında ilgili makine ve döneme ait ayrıntılı iş listesine ulaşılabilir.
MRP raporundaki "Kapasite Detay Sonuçları" sekmesinde ise elde edilen bütün sonuçların detaylı dökümü bulunmaktadır. Bu rapor üzerinde makine ve periyot bazında gruplama yapılarak incelemeler yapılabilir.
