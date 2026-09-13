---
title: "Netsis Firma Kredi Kartı İşlemleri"
page_id: "66237118"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis Firma Kredi Kartı İşlemleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis Firma Kredi Kartı İşlemleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTE2Y2RlYWFmLWExZjYtNGRmYy1iNTljLWEzNDFhZDU3MDk4NCZsaW5rPTA0YWY4M2RlLWNiOGMtNGNiMC1iZTVlLTNiZjVlZjMxZTlmYiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=16cdeaaf-a1f6-4dfc-b59c-a341ad570984&link=04af83de-cb8c-4cb0-be5e-3bf5ef31e9fb&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-firma-kredi-karti-islemleri_80089039_66237118.html"
source_version: "2023-02-21T13:24:15.267+03:00"
source_bytes: 1081021
fetched_at: "2026-09-13T04:24:42+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis Firma Kredi Kartı İşlemleri

Netsis Firma Kredi Kartı işlemleri ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Firmalar satın alma işlemlerini ve kendi ödemelerini her zaman nakit veya çek-senet ile gerçekleştirmemektedir. Bu tip ödemeler için firmaya ait kredi kartları da kullanılmaktadır. Logo Netsis olarak kullanıcılarımızın bu tip ödemeleri Netsis içerisinden gerçekleştirebilmelerini desteklemiş bulunuyoruz.

#### Alış Fatura Parametreleri

Netsis içerisinden kaydedilen kapalı tipli faturalar için ödeme ekranının görüntülenebilmesi için Alış Fatura Parametreleri ekranında-Genel 3 sekmesinde yer alan "Kapalı Faturada Ödeme Ekranı Çıksın" parametresinin işaretli olması gerekmektedir. (Bkz. Ekran Görüntüsü 1)
![](../_assets/709ec641af58f1f89325.png) **Ekran** **Görüntüsü** **1**
Kapalı Faturada Ödeme Ekranı Çıksın parametresi işaretli olduğunda kapalı faturanın toplamlar sekmesinde Kaydet butonu tıklandığında kullanıcının karşısına "Hızlı Ödeme Kayıtları" ekranı beliriyor olacaktır. Kullanıcı bu ekran üzerinden faturanın toplam tutarını nakit ve/veya firma kredi kartı olarak tanımlanmış olan kredi kartları ile ödeme kaydını girebilecektir.

#### Kredi Kartı Tanımları

Finans-Banka-Kayıt-Kredi Kartı Tanımlamaları yolu izlenerek ilgili ekrana ulaşılabilir. Uygulamanın kullanılabilmesi için firma kredi kartlarının Kredi Kartı Tanımlama ekranından "Firma Kredi Kartı" işaretlenerek tek tek tanımlanmış olması gerekmektedir.
![](../_assets/c348b6037bb06c85c5b9.png) **Ekran** **Görüntüsü** **2**
Firma Kredi Kartı seçeneği işaretli olduğunda firma kredi kartına ait detay bilgilerin girilebildiği "Firma Kredi Kartı Bilgileri" sekmesi görünür olacaktır.
![](../_assets/519b9a431e74a341b459.png) **Ekran** **Görüntüsü** **3**
Firma Kredi Kartı sekmesinde buluna alanların açıklamaları aşağıda detaylandırılmıştır:
Kart Numarası: Firma kredi kartının numarasının girildiği alandır.
Ek Kart: Eğer tanımladığınız firma kredi kartı bir ek kart ise bu seçenek işaretlenebilecektir.
Bağlı Olduğu Kart: Ek Kart seçeneği işaretlendiğinde aktif olan bir alandır, rehberden tanımladığınız kartın bağlı olduğu ana kartı seçebilirsiniz.
Kart Limiti: Kartınızın toplam limitinin yazılabildiği alandır.
Limit Kontrolü Yapılsın: Bu seçenek işaretlendiğinde kaydetmeye çalıştığınız belgedeki tutar ile birlikte toplam borç tutarı, tanımladığınız kart limitinin üzerine çıkıyorsa size uyarı mesajı verecek veya işlemin yapılmasına izin verilmeyecektir. Bu durumda nasıl davranılacağına ilişkin parametrenin detayı, Banka Şube Bazında Parametreler ekranında açıklanacaktır.
Son Kullanma Tarihi Ay/Yıl: Kartınızın son kullanma tarihini ay ve yıl olarak girebileceğiniz alandır.
Hesap Kesim Günü: Hesap kesiminin her ayın kaçıncı günü olduğu bilgisini bu alana yazabilirsiniz.
Ödeme Günü: Ödemelerinizin hesap kesim tarihinden kaç gün sonra yapılacağını bu alana yazabilirsiniz.
Hesap Özeti Muhasebe Kodu: Banka Şube Bazında Parametreler ekranında Hesap Özeti Uygulaması kullanılıyorsa, hesap özeti kaydı atıldığında kullanılacak olan hesap kodunun yazılabileceği alandır. Kullanım detayı Banka Şube Bazında Parametreler ekranında açıklanacaktır.
Verilen Personel: Eğer "Diğer Paketlerle Bağlantı" ekranından bir personel veri tabanına bağlantı yapıldıysa bu alandaki rehberde tanımlı personeller geliyor olacak.
![](../_assets/bbaeb11095a17901da3f.png) **Ekran** **Görüntüsü** **4**
Faiz Muhasebe Kodu: Hesap özeti kaydı sırasında eğer ekrana bir faiz tutarı yazılıyorsa, bu tutarın muhasebeleşmesinde kullanılacak hesap kodun yazıldığı alandır.
Kredi Kartı Banka Hesabı: "Firma Kredi Kartı" tipinde tanımlanan banka hesabının seçildiği, bağlı olduğu firma kredi kartı banka hesabıdır.

#### Banka Şube Bazında Parametreler

Banka Şube Bazında Parametreler ekranına "Firma Kredi Kartlarında Limit Aşıldığında" ve "Hesap Özeti Kullanılsın" parametreleri eklenmiştir. "Firma Kredi Kartlarında Limit Aşıldığında" parametresi, Kredi Kartı Tanımları ekranında "Limit Kontrolü Yapılsın" işaretlendiğinde anlamlı olan bir seçenektir. Eğer Kartınızın limit kontrolü yapılsın isteniyorsa ve kartın limiti ilgili işlemle birlikte aşılıyorsa, bu parametre ile kullanıcı "Uyarı Ver" veya "İşlemi Durdur" seçeneklerinden hangisini seçti ise, Netsis tarafından seçilen aksiyon alınacaktır.
![](../_assets/431b6c17e865a29303c0.png) **Ekran** **Görüntüsü** **5**
"Hesap Özeti Kullanılsın" parametresi, hesap özeti kullanıcıların ellerine ulaştığında ödeme tarihine kadar geçen sürede ilgili ödenecek tutarın 300 (Firma Kredi Kartı tipindeki bankanın muhasebe hesap kodu) hesaptan, 103 hesaba ( Kredi Kartı Tanımlarındaki Hesap Özeri Muh. Kodu) aktarılması ve ödeme işleminin 103 hesap ile 102 hesap arasında olması istendiği durumda işaretlenmesi gerekmektedir. Bu parametre işaretli değil ise "Firma Kredi Kartı Ödeme Kayıtları" ekranında bulunan "Hesap Özeti Kaydı Oluştur" butonu aktif olarak gelmeyecektir. Dolayısıyla ödeme işlemi 300 hesap ile 102 ( Firma Kredi Kartı Ödeme Kayıtları ekranında ödemenin yapıldığı vadesiz banka hesabının muhasebe hesap kodu) arasında yapılacaktır. "Firma Kredi Kartı Ödeme Kayıtları" ekranı açıklanırken bu işlemlere ait örneklere yer verilecektir.

#### Firma Kredi Kartı Ödeme Kayıtları

Finans-Banka-Kayıt-Kredi Kartı Tanımlamaları-Firma Kredi Kartı Ödeme Kayıtları yolu izlenerek ilgili ekrana ulaşılabilir. (Bkz. Ekran Görüntüsü 6)
![](../_assets/6bee65c528a2b8202764.png) **Ekran** **Görüntüsü** **6**
Hazırlık: Hazırlık işlemi ile ekran üzerinde verilen Hesap Özeti Tarihi, Firma Kredi Kartı ve Son Ödeme Tarihi alanlarına göre verilen kısıtlara uygun olan hesap özeti kayıtlarının gride dökülmesini sağlayabilirsiniz.
Tümünü Seç: Bu buton aracılığı ile gride dökülmüş olan satırlardan eğer hesap özeti kaydı atılmamış olan satırları seçmek istiyorsanız kulakçığa tıklayarak gelen listede "Hesap Özeti Kayıtları" seçeneğini, eğer hesap özeti kaydı atılmış (Hesap Özeti Kullanılsın parametresi aktif ise) ve ödeme kaydı atılmamış olan satırları seçmek istiyorsanız kulakçığa tıklayarak gelen listede "Ödeme Kayıtları" seçeneğini seçebilirsiniz. Böylece kayıtlar hızlı ve toplu şekilde seçilmiş olacaktır.
![](../_assets/5640336664c98acf5c12.png) **Ekran** **Görüntüsü** **7**
Seçimi Kaldır: Grid üzerinde seçilmiş olan satırların seçimini kaldırır.
Hesap Özeti Kaydı Oluştur: Hesap Özeti Kullanılsın parametresi aktif ise bu buton aktif olacaktır. Ve seçilmiş olan satır/satırlar için hesap özeti kaydını oluşturacaktır.
Ödeme Kaydı Oluştur: Hesap Özeti Kullanılsın parametresi aktif ise hesap özeti kaydı atıldıktan sonra, değil ise Hazırlık işleminden sonra seçtiğiniz satırlar için bu butonu kullanarak ödeme kaydınızı atabilirsiniz.
Hızlı Ödeme Kaydı: Belge kaydı sonrasında kullanıcının karşısına gelen "Hızlı Ödeme Kayıtları" ekranına hızlı bir şekilde erişim sağlayacaktır. Bu ekrandayken atlanmış olan bir ödeme veya kart sahibinin yaptığı şahsi bir harcama görülüyorsa yani gerçekte gelen hesap özeti tutarı ile Netsis'deki tutar arasında fark varsa, bu ekrandan hızlı şekilde bu kayıtların işlenmesi sağlanabilecektir. Hızlı Ödeme Kayıtları ekranının açılabilmesi için, ilgili ekrandan hem nakit hem de firma kredi kartı ile işlem yapılabildiğinden dolayı, nakit kayıtları bir kasaya atabilmek için form üzerinde yer alan "Hızlı Ödeme Kaydı İçin Kasa Kodu" alanına bir kasa seçilmiş olması gerekmektedir.
Hesap Özeti Baş. - Bit. Tar: Sorgulanacak olan hesap özeti döneminin başlangıç ve bitiş tarih aralığının verildiği alandır.
Firma Kredi Kartı: Sorgulanacak olan firma kredi kartının belirlenebildiği alandır, boş bırakıldığında tüm
kartlar gelecektir.
Son Ödeme Tar. Baş. - Bit. Tar: Sorgulanacak olan son ödeme tarihinin başlangıç ve bitiş tarih aralığının verildiği alandır.
Hızlı Ödeme Kaydı İçin Kasa Kodu: Bu ekrandan Hızlı Ödeme Kaydı ekranına gidebilmek için
belirlenmesi gereken kasa kodudur.
Hesap Özeti Tutarı: Yapılan ödemelere göre ilgili kart için hesaplanan hesap özeti tutarı bilgisidir.
Faiz Tutarı: Önceki dönemlerden tam olarak ödenmeyen bir hesap özeti mevcut ise bir sonraki dönem bu tutar için faiz ödenecektir. Buradaki tutar hesap özeti kaydı atılırken kullanıcı tarafından manuel olarak belirlenecektir.
Ödenecek Tutar: Hesap Özeti Tutarı ve varsa Faiz Tutarı alanlarından sonra bulunan toplam tutarın ne
kadarının ödeneceği kullanıcı tarafından bu alanda belirlenecektir.
Ödenecek Vadesiz Hesap: Kullanıcı tarafından belirlenen ödenecek tutarın hangi vadesiz hesaptan ödeneceği bu alanda belirlenecektir.
Ödeme Tarihi: Gerçekleştirilen ödeme işlemi için atılacak olan kayıtların hangi tarihli olacağının belirlendiği alandır.

#### Senaryo-1 Hesap Özeti Uygulaması Kullanılıyor

Banka Şube Bazında Parametreler ekranında Hesap Özeti Kullanılsın parametresi işaretliyken, 02.08.2020 tarihine 108 TL tutarında bir alış faturası kaydediyorum. Ve Hızlı Ödeme Kayıtları ekranında 8 TL Nakit ve 100 TL KART01 kodlu firma kredi kartı ile 5 taksit olarak ödenmiştir. (Bkz. Ekran Görüntüsü 8)
![](../_assets/f062a3bcf8d515b97c52.png)
**Ekran** **Görüntüsü** **8**
Kredi Kartı Tanımları ekranında ise Hesap Kesim Günü 10 olarak belirlenmiş olsun. Yani Firma Kredi Kartı Ödeme Kayıtları ekranında 10.08.2020 tarihi kapsayacak şekilde hesap özeti tarihine kısıt verip hazırlık işlemini çalıştırıldığında 100 TL'nin ilk taksiti olan 20 TL'yi görmemiz gerekmektedir.
![](../_assets/438690e2cf7d45e2ee25.png) **Ekran** **Görüntüsü** **9**
Grid satırlarına gelen ve hesap özeti atmak istediğim kaydı çift tıklayarak varsa faiz tutarını yazdıktan sonra Hesap Özeti Kaydı Oluştur butonu ile kayıt atılabilir.

Oluşan muhasebe fiş kayıtları şu şekildedir:
Hesap Kodu Borç Alacak
300-01-00126
103-01-00126
780-01-0016
300-01-0016
Sonrasında Ödeme Kaydı Oluştur tıklanarak ödeme işlemi gerçekleştirdiğimde eğer 20 TL Hesap Özeti Tutarı+6 TL Faiz Tutarı, Toplamda 26 TL ödeme yaptığımda oluşan muhasebe fişi aşağıdaki gibi olacaktır:
Hesap Kodu Borç Alacak
103-01-00126
102-01-00126
Eğer 26 TL'nin hepsini ödemeyip bir kısmını örneğin 10 TL lik kısmını ödediğimde oluşacak olan muhasebe fişi aşağıdaki gibi olacaktır:
Hesap Kodu Borç Alacak
103-01-00110
102-01-00110
103-01-00116
300-01-00116
Yani hesap özeti kullanıldığında 300'den 103'e taşınan tutarın ödenmeyen kısmı tekrar 103 hesaptan 300 hesaba taşınacaktır. Bu tutar bir sonraki ay hesaplanacak olan hesap özeti tutarına eklenecektir.

#### Senaryo-2 Hesap Özeti Uygulaması Kullanılmıyor

Banka Şube Bazında Parametreler ekranında Hesap Özeti Kullanılsın parametresi işaretli değilken, 02.08.2020 tarihine 108 TL tutarında bir alış faturası kaydediyorum. Ve Hızlı Ödeme Kayıtları ekranında 18 TL Nakit ve 90 TL KART02 kodlu firma kredi kartı ile 3 taksit olarak ödenmiştir. (Bkz. Ekran Görüntüsü 10)
![](../_assets/29d807b42a06f9b3a426.png)
**Ekran** **Görüntüsü** **10**
Kredi Kartı Tanımları ekranında ise Hesap Kesim Günü 7 olarak belirlenmiş olsun. Yani Firma Kredi Kartı Ödeme Kayıtları ekranında 07.08.2020 tarihi kapsayacak şekilde hesap özeti tarihine kısıt verip hazırlık işlemini çalıştırıldığında 90 TL'nin ilk taksiti olan 30 TL'yi görmemiz gerekmektedir.
![](../_assets/291aa526bdd7ad5d2345.png) **Ekran** **Görüntüsü** **11**
Grid satırlarına gelen ve hesap özeti atmak istediğim kaydı çift tıklayarak varsa faiz tutarını yazdıktan sonra (bu örnekte 5 TL faiz tutarı yazılmıştır) Ödeme Kaydı Oluştur butonu tıklandığında (Hesap Özeti uygulaması kullanılmadığı için Hesap Özeti Kaydı Oluştur butonu pasif olarak görünmektedir) oluşan muhasebe fiş kayıtları şu şekildedir:
Hesap Kodu Borç Alacak
300-01-00135
102-01-00135
780-01-0015
300-01-0015
Bu örnekte tüm tutar ödenmiştir, eğer toplam tutar olan 35 TL ödenmediği durumda bu aydan kalan ödenmemiş tutar bir sonraki ay hesaplanacak olan hesap özeti tutarı alanına ekleniyor olacaktır.
