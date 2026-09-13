---
title: "Taksitli ve Uzun-Orta Vadeli Kredi"
page_id: "50680406"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Taksitli ve Uzun-Orta Vadeli Kredi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Taksitli ve Uzun-Orta Vadeli Kredi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTQ4NzdiZTljLWM3MzctNGFhZS04NzE4LTFhZGM5YmRmNjVlYiZsaW5rPTBhOTZmYTE4LWFlZDktNDU3Ni04ZGRiLWM1YmQwNDQ1NGU2MyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=4877be9c-c737-4aae-8718-1adc9bdf65eb&link=0a96fa18-aed9-4576-8ddb-c5bd04454e63&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "taksitli-ve-uzun-orta-vadeli-kredi_79167538_50680406.html"
source_version: "2022-11-03T09:54:12.907+03:00"
source_bytes: 671243
fetched_at: "2026-09-13T04:26:23+00:00"
generator: "netsis-scraper 1.0.0"
---
# Taksitli ve Uzun-Orta Vadeli Kredi

Taksitli ve Uzun-Orta Vadeli Kredi ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Banka modülünde yapılan iyileştirmeler sonucunda, taksitli ve uzun/orta vadeli kredilerin program içinden takip edilebilmesi desteklenmiştir. Taksitli ve uzun-orta vadeli krediler hakkında ayrıntılı bilgiye ilgili dokümandan ulaşılır.

**Taksitli** **Kredi**

Taksitli kredi, firmaların genel finansman ihtiyaçlarını karşılamaya yönelik olarak kullandıkları kredi türüdür. Bu tip kredide, genellikle kredi tutarının tamamı bir defada kullanılır ve anapara+faiz+diğer kesintiler toplamından oluşan geri ödeme tutarı, belirlenen vade içerisinde eşit taksitler halinde ödenir. İşletme kredisi, araç, makine/ekipman ve hammadde alım kredisi bu tip krediye örnek olarak gösterilebilir.

Krediye başvurunun kabul edilmesi ile birlikte, banka tarafından müşteriye ödeme planı verilir. Ödeme planında, her dönemde ödenmesi gereken ana para, faiz, fon ve vergi tutarı belirtilir.

Banka modülünde desteklenen taksitli kredi işlemleri, taksitli kredi hesabının açılması ile başlar. Banka Hesap Kayıtları menüsünden tanımlanan taksitli kredi hesabı, Banka modülü/İşlemler/Taksitli Kredi Açma işlemi ile açılır. Hesap açıldığında, taksitli kredi hesabı, alınan kredi tutarı kadar alacaklanırken, vadesiz mevduat hesabı aynı tutarda borçlanır. Kredinin taksitleri, hesap açılışı sırasında belirlenen dönemlerde Banka modülü/İşlemler/Faiz İşleme/Kapatma işlemi ile kapatılır. Taksit dönemleri bazında, ödenmesi gereken taksit tutarları ve kapanmış ana para tutarı gibi bilgiler Banka modülü/Raporlar/Banka Faiz Raporlarında bulunan Uzun Vadeli/Taksitli Kredi Hesapları Faiz Raporu yardımıyla raporlanabilir.

Taksitli kredi takibi için Banka modülüne eklenen menü ve kullanımları aşağıda açıklanmıştır.

**Banka Hesap** **Kayıtları**

Taksitli kredinin takip edileceği banka hesabı Banka Hesap Kayıtları menüsünden tanımlanırken, Hesap Tipi olarak programa eklenen Taksitli Kredi seçeneği işaretlenmelidir.

![](../_assets/1faa1ea2262ed919276f.png)

Taksitli kredi tipindeki hesaplar sadece, Banka modülünde bulunan Taksitli Kredi Açma ve Faiz İşleme/ Kapatma işlemlerinde kullanılabilecektir.

**Taksitli Kredi Açma**

Bankadan alınan taksitli kredinin sisteme girilebilmesi için, Banka modülü/İşlemler menüsüne eklenen Taksitli Kredi Açma işlemi kullanılır.

![](../_assets/cf77b79d458b3d140616.png)

Bu işlemde bulunan sahaların açıklamaları aşağıda verilmiştir.

**Referans No:** Program tarafından getirilen 15 karakterlik alfanümerik takip numarasıdır.

**Devir Kaydı:** Bu seçenek işaretlenerek hesap açma işlemi yapıldığı zaman sadece "Taksitli Kredi Banka Hesap Kodu" alanında yazılan banka hesabının hareketlerine alacak kaydı atılacak, virman banka hesap kodunun hareketlerine ve entegrasyona kayıt atılmayacaktır. Devir tipli kredi açılışı, taksitli kredi hesabından vadesiz mevduat hesabına virman yapılması istenmediğinde, ancak taksitli kredi hesabı için faiz hesaplatılması istendiğinde kullanılabilir.

**İhracat Taahhütlü:** Bu seçenek işaretlenerek açılan kredi hesaplarının kapanışı sırasında BSMV hesaplanmayacaktır. Ayrıca hesap açılışı sırasında hesaplanan bileşik faiz oranı ve taksit tutarı da BSMV dikkate alınmadan hesaplanacaktır.

**Taksitli Kredi Banka Hesap Kodu:** Hesap tipi Taksitli Kredi olan hesabın girileceği alandır. Taksitli kredi açılışı yapılabilmesi için, kredi hesabının bakiye vermemesi gerekmektedir. Taksitli kredi açılışı ile birlikte, bu sahada girilen hesap, kredi tutarı kadar alacaklanır.

**Virman Banka Hes. Kodu:** Kredi tutarının hangi vadesiz mevduat hesabına virman yapılacağının belirlendiği sahadır. Taksitli kredi açılışı ile birlikte, burada girilen hesap kredi tutarı kadar borçlanır.

**İşlem Tarihi:** Hesap açılışına ait işlem tarihinin belirtildiği sahadır. Program tarafından günün tarihi getirilmektedir. İstenirse değiştirilebilir.

**Dekont No:** Yapılan işleme ait banka tarafından verilen işlem numarasının rapor amaçlı takibinin yapılabileceği alandır.

**Efektif Tarih:** Kredi tutarının taksitli kredi ve vadesiz mevduat hesaplarına işleneceği tarihtir.

**Taksit Sayısı:** Kredi tutarının kaç taksitte kapatılacağının belirlendiği sahadır.

**Dönem:** Taksitlerin kaçar aylık dönemler halinde kapatılacağının belirlendiği sahadır. Örneğin bu sahaya 2 ay, taksit sayısı sahasına da 3 girilir ise, geri ödemenin 2 ayda bir olmak üzere 3 taksit ile yapılacağı anlaşılacaktır.

**Libor /Spread Oranı:** Bankalar tarafından açıklanan faiz oranları, günlük bazda her banka için aynı olan Libor Oranını ve bu oran üzerine her bankanın eklediği ek bir faiz oranı olan Spread Oranını içerir. Kredi açılış işlemlerinde bu oranlar ayrı ayrı sorgulanmaktadır. Böylece zaman içinde faiz oranlarında meydana gelen değişikliklerin hangi orandan kaynaklandığı, program içinden hazırlanabilecek raporlar ile izlenebilir. Bu bilginin detaylı olarak takibi yapılmayacak ise, Libor ve Spread Oranı sahaları boş geçilebilir.

**Faiz Oranı:** Libor ve spread oranları girilmiş ise, bu oranların toplamının program tarafından getirileceği sahadır. Libor ve Spread oranları boş geçilerek doğrudan faiz oranı girilebilir.
Bileşik Faiz Oranı= Faiz Oranı + (Faiz Oranı \* (BSMV Oranı + KKDF Oranı))

**Bileşik Faiz Oranı:** Taksit tutarının hesaplaması sırasında kullanılacak faiz oranıdır. Hesap açılışında verilen faiz oranı ve Banka modülü/Kayıt/Genel Parametreler bölümünde verilen BSMV ve KKDF oranları dikkate alınarak hesaplanır.
Taksitli kredi açılışında verilen faiz oranı %10, BSMV %5 ve KKDF %5 olduğunda bileşik faiz oranı aşağıdaki şekilde hesaplanacaktır.
Bileşik Faiz Oranı=10+(10\*(0,05+0,05))= 11
Kredi açılışı "İhracat Taahhütlü" seçeneği işaretlenerek yapıldığında ise, yukarıdaki formülde BSMV oranı dikkate alınmaz. Bu durumda aynı örnek için bileşik faiz oranı 10,5 olarak hesaplanır.

**Döviz Tutar/Tutar:** Kredi tutarının döviz ve/veya YTL cinsinden girildiği sahalardır.

**Döviz Taksit Tutarı/Taksit Tutarı:** Faiz oranı, taksit sayısı ve kredi tutarına göre aylık geri ödeme tutarının program tarafından hesaplanarak getirildiği sahadır. Bu tutara müdahale edilerek istenen taksit tutarı manuel olarak girilebilir. Program tarafından aşağıdaki formüle göre hesaplanan taksit tutarı manuel değiştirildiğinde, hesaplanan ve yeni girilen taksit tutarı arasındaki fark, faiz giderine eklenerek ya da bu giderden çıkarılarak sıfırlanır.

![](../_assets/d888b334d7b97e64aa6e.png)
Bu formüle göre, faiz oranı %10 olan ve 6 ay geri ödemeli 10.000 YTL tutarındaki kredinin hesaplanması aşağıdaki gibidir;
Taksit Tutarı = 10.000 x (1+0,11)<sup>3</sup> x 0,11=4.092,13 YTL
(1+0,11)<sup>3</sup> - 1

**Muh.Ref.Kod.:** Muhasebe modülü parametrelerinde "Fişlerde referans kodu sorulsun" parametresi açık ise seçilen hesap tiplerine göre referans kodu sorulacaktır.

**Plasiyer Kodu:** Yardımcı Programlar/Şirket/Şube Parametre tanımlarında "Plasiyer uygulaması var" parametresinin işaretli olması halinde sorgulanan sahadır. İlgili plasiyer kodu bu alanda girilmelidir.

**Proje Kodu:** Yardımcı Programlar/Şirket/Şube Parametre tanımlarında "Proje uygulaması var" parametresinin işaretli olması halinde sorgulanan sahadır. İlgili proje kodu bu alanda girilmelidir.

**1.3 Taksitli Krediler için Faiz İşleme/Kapama**

Diğer banka hesaplarında olduğu gibi, taksitli krediler için de faiz işletilmesi ve hesap kapanışı Banka modülü/İşlemler/Faiz İşleme/Kapama işlemi ile yapılmaktadır. İşlem Ön Sorgulama ekranında taksit ödemesi yapılacak kredi hesabı seçilerek Faiz Bilgileri sayfasına geçilebilir.
![](../_assets/9176e0376a46acb3b6f8.png)

Faiz Bilgileri sayfasında Başlangıç ve Kapanış Tarihleri, kaçıncı taksitin kapatılacağı göz önünde bulundurularak, program tarafından getirilecektir. **Faiz Hesapla** butonuna basıldığında, kredi açılışı sırasında da hesaplanan taksit tutarına ait faiz gideri, BSMV ve KKDF tutarları, ekrandaki ilgili sahalara yansıtılır. Bu tutarların toplamı Net Faiz Gideri sahasında, ana paranın ilgili taksitte kapatılacak kısmı ise Anapara Taksiti sahasında gösterilir. Bu iki sahanın toplamı ise, kapatılacak taksit tutarını verir.
Girilen bilgiler kaydedildiğinde, taksitli kredi hesabı borç, vadesiz mevduat hesabı ise alacak çalışır.
Herhangi bir taksidin kapatma kaydı oluşturulurken "Tüm Taksitler Tek Seferde Kapatılsın" seçeneği işaretlendiğinde, ilgili taksit ile birlikte, kendisinden sonra gelen tüm taksitlere ilişkin kapanış kayıtları da, ayrı ayrı olacak şekilde, program tarafından oluşturulur.

**Orta/Uzun Vadeli Kredi**

İşletmelerin kuruluş, modernizasyon ve işletme sermayelerini karşılamak amacıyla 2- 5 yıl vadeyle aldıkları krediler orta, 5 yılın üzerinde vadeyle aldıkları krediler uzun vadeli krediler olarak adlandırılır. Krediyi alan işletmelerin geri ödemeyi gelecek dönemlerdeki kaynaklarıyla yapacak olmaları, işletmeler için avantajlı bir durumdur. İşletmeler uzun süreli yatırımlarında bu kredilerden yararlanmakta ve kredilerde başlangıçta uygulanan ödemesiz dönem onlara zaman tanımaktadır.
İşletmeler tarafından alınan orta/uzun vadeli kredilerin programda takibi, kredi hesabının açılması ile başlar. Banka Hesap Kayıtları menüsünden tanımlanan uzun/orta vadeli kredi hesabı, Banka modülü/İşlemler/ Uzun/Orta Vadeli Kredi Açma işlemi ile açılır. Hesap açıldığında, uzun/orta vadeli kredi hesabı, alınan kredi tutarı kadar alacaklanırken, vadesiz mevduat hesabı aynı tutarda borçlanır. Kredinin taksitleri, hesap açılışı sırasında belirlenen dönemlerde Banka modülü/İşlemler/Faiz İşleme/Kapatma işlemi ile kapatılır. Taksit dönemleri bazında, ödenmesi gereken taksit tutarları ve kapanmış ana para tutarı gibi bilgiler Banka modülü/Raporlar/Banka Faiz Raporlarında bulunan Uzun Vadeli/Taksitli Kredi Hesapları Faiz Raporu yardımıyla raporlanabilir.
Uzun/orta vadeli kredilerin takibi için yapılması gereken işlemler aşağıda açıklanmaktadır.

**Banka Hesap Kayıtları**

Orta/uzun vadeli kredilerin takip edileceği banka hesapları Banka Hesap Kayıtları menüsünden tanımlanırken, Hesap Tipi olarak, programa eklenen Uzun/Orta Vadeli Kredi seçeneği işaretlenmelidir.

![](../_assets/5c379ff6328ddf7048fa.png)

Taksitli kredi tipindeki hesaplar sadece, Banka modülünde bulunan Orta/Uzun Vadeli Kredi Açma ve Faiz İşleme/Kapatma işlemlerinde kullanılabilecektir.

**Uzun/Orta Vadeli Kredi Açma**

Bankadan alınan uzun/orta vadeli kredilerin sisteme girilebilmesi için Banka modülü/İşlemler menüsüne eklenen Uzun/Orta Vadeli Kredi Açma işlemi kullanılmalıdır.

![](../_assets/9dd8c182d8a708762c33.png)

**Uzun/Orta Vadeli Kredi Banka Hesap Kodu:** Hesap tipi Uzun/Orta Vadeli Kredi olan hesabın girilebileceği alandır. Açılışı yapılacak olan kredi hesabının bakiye vermemesi gerekmektedir. Açılış kaydının oluşturulması ile birlikte, bu sahada girilen hesap, kredi tutarı kadar alacaklanır.

**Virman Banka Hes. Kodu:** Kredi tutarının hangi vadesiz mevduat hesabına virman yapılacağının belirlendiği sahadır. Kredi açılışı ile birlikte, burada girilen hesap kredi tutarı kadar borçlanır.

**Ana Para Ödeme Tarihi:** Uzun/orta vadeli kredilerde ana paranın taksitler halinde, tamamının son taksitte ya da tamamının son taksitten sonraki bir tarihte kapatılması mümkündür. Açılış işlemi sırasında sorgulanan "Ana Para Taksitlendirilsin Mi?" seçeneği işaretlenmez ise, ana paranın tamamı son taksit ile birlikte kapatılabilir.

Ancak son taksitte de ana para kapanışı yapılmadığında, ödeme bu sahada belirlenen tarihte gerçekleşecektir. Bu sahanın kullanımına ilişkin örneği, dokümanın *2.3* *Uzun/Orta* *Vadeli* *Krediler* *için* *Faiz* *İşleme/Kapama/Örnek* *2* bölümünde bulabilirsiniz.

**Ana Para Taksitlendirilsin Mi?:** Ana paranın taksitlendirilerek kapatılacak olması halinde işaretlenmesi gereken sahadır. Bu seçenek işaretlendiğinde Ana Para Ödeme Tarihi sahası pasif olacak, bunun yerine Taksit Başlangıcı değeri sorgulanacaktır.

**Taksit Başlangıcı:** Ana paranın kaçıncı taksitten itibaren ödenmeye başlanacağı bu sahada belirlenir. Örneğin 36 ay vadeli alınan kredinin ilk 12 ayında sadece faiz ödemesi yapılacak ve 13. taksitten itibaren ana para ödemesine de başlanacak ise, bu sahaya 13 değeri girilmelidir. Böylece, ana para tutarı, kalan taksit sayısına bölünür ve toplam giderlere bu tutar eklenerek taksit tutarı hesaplanır.
Hesap açılışı sırasında bulunan ve yukarıda anlatılmayan diğer sahaların kullanımı Taksitli Kredi Açma işleminde olduğu gibidir.

**2.3 Uzun/Orta Vadeli Krediler için Faiz İşleme/Kapama**

Uzun/orta vadeli krediler için faiz işletilmesi ve hesap kapanışı Banka modülü/İşlemler/Faiz İşleme/Kapama işlemi ile yapılmaktadır. İşlem Ön Sorgulama ekranında taksit ödemesi yapılacak kredi hesabı seçildikten sonra Faiz Bilgileri sayfasına geçilebilir.

![](../_assets/080d9344dde098256095.png)

Faiz Bilgileri sayfasında Başlangıç ve Kapanış Tarihleri, kaçıncı taksitin kapatılacağı göz önünde bulundurularak, otomatik olarak gelecektir. **Faiz Hesapla** butonuna basıldığında, kapanışı yapılan taksit dönemi için kalan ana para üzerinden hesaplanan faiz gideri, BSMV ve KKDF tutarları, ekrandaki sahalara yansıtılır. Bu tutarların toplamı Net Faiz Gideri sahasında gösterilir.

**Örnek 1:** Yukarıdaki örnekte, faiz oranı %10 iken alınan 10.000 TL'lik banka kredisinin ilk taksiti işlenmektedir. Ana para kapanışı, taksitli olarak 13. taksitten itibaren yapılacaktır. Dolayısıyla ilk 12 taksitte sadece Net Faiz Gideri hesaplanır. Faiz tutarı aşağıdaki formül ile hesaplanmaktadır.

![](../_assets/1d0dc450ab7cfc50fb62.png)

Formülde bulunan gün değeri, ilgili ayda bulunan gün sayısını ifade eder. Dolayısıyla her ay ödenecek faiz gideri farklı olacaktır. Verilen örnekteki faiz gideri aşağıdaki gibi hesaplanır.
Faiz Gideri= 30 x 10.000 x 10 = 83,33 TL
360x100
BSMV ve KKDF tutarları faiz gideri üzerinden hesaplanır. BSMV ve KKDF oranlarının %5 olduğunu varsayarsak aşağıdaki değerlere ulaşırız.
BSMV= Faiz Gideri\*0,05=4,17 TL
KKDF= 4,17 TL

Bu durumda Net Faiz Gideri 91,67 TL (83,33+4,17+4,17) olacaktır.

Girilen bilgiler kaydedildiğinde, vadesiz mevduat hesabı alacak, gider hesapları borç çalışır. Ana para kapanışı yapılmayan taksitlerde orta/uzun vadeli kredi hesabı çalışmayacaktır.

Ana para taksitlendirilerek kapatılacak ise, taksit dönemi geldiğinde program tarafından uyarı verilir. Örneğimizde ana paranın 13. taksitten itibaren kapatılmaya bağlanacağını belirtmiştik. Yani ana para son 24 ayda taksitler halinde kapatılacaktır. Faiz İşleme/Kapama işleminde 13. Taksit ödemesi

için Faiz Hesapla butonuna basıldığında aşağıdaki uyarı gelir.
![](../_assets/93532be750dde71a1310.png)

Uyarı ekranında Tamam butonuna basıldığında, ana paranın 416,67 TL'lik (10.000 TL /24) kısmı, taksit tutarı olarak Anapara Taksiti sahasına yansıtılır.

![](../_assets/b0ea837ae210290f9c25.png)

İşlem kaydedildiğinde; Orta/uzun vadeli kredi hesabı anapara taksiti kadar borçlanır, Faiz gideri, BSMV ve KKDF hesapları borçlanır, Vadesiz mevduat hesabı, net faiz gideri ve ana para taksiti kadar alacaklanır.

**Örnek 2:** 01/09/2019 yılında 36 ay vade ile alınan kredi için Ana Para Ödeme Tarihi 05/09/2021'dir. Ana paranın taksitler halinde kapatılmadığı durumda, son taksit kapanışı aşağıdaki şekilde gerçekleşir.

![](../_assets/f5225f559ab9f135c8ca.png)

Taksit ile birlikte ana paranın kapatılıp kapatılmayacağı sorgulanır. Onay ekranında Evet butonuna basılması halinde, ana para kapatılır. Hayır butonuna basılması halinde ise, ana paranın daha sonra kapatılacağı varsayılarak, sadece taksit kapatılır.

Ana para kapatılmadan, sadece son taksit kapatıldığında aşağıdaki uyarı gelir.

![](../_assets/08e8c4238bc51f329c68.png)

Tamam butonuna basıldığında Faiz İşleme/Kapama işleminde Başlangıç Tarihi olarak 01/09/2019, Kapanış Tarihi olarak da 05/09/2021 gelecektir. F5 butonuna basıldığında ise, 05/09/2021 tarihi ile ana para kapanışı gerçekleşir.

**3. Uzun Vadeli/Taksitli Kredi Hesapları Faiz Raporu**

Banka modülü/Raporlar/Banka Faiz Raporlarına eklenen Uzun Vadeli/Taksitli Kredi Hesapları Faiz Raporu yardımıyla, taksitli veya uzun vadeli kredilerin son durumlarını detaylı bir şekilde incelemek mümkündür. Alınan kredinin kaç taksitinin ödendiği ve ne kadarının beklemede olduğu gibi bilgiler, kalan ana para tutarı, ödenen faiz tutarı gibi detaylar ile raporlanmaktadır.

![](../_assets/1f04be4b5a51468181db.png)
