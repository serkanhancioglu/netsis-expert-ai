---
title: "Netsis Sıkça Sorulan Sorular-Kredi Kartı"
page_id: "50683540"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis Sıkça Sorulan Sorular-Kredi Kartı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis Sıkça Sorulan Sorular-Kredi Kartı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWJjYmRhNGY4LWU5ZGYtNDgyMS1iNjBkLTIzMjBlNTY4NTM3NyZsaW5rPTQ3YjMwMDkyLWFmNDgtNDVkNS1hY2Y3LWRiNzc4MjAzYmI2NiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=bcbda4f8-e9df-4821-b60d-2320e5685377&link=47b30092-af48-45d5-acf7-db778203bb66&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-sikca-sorulan-sorular-kredi-karti_50683541_50683540.html"
source_version: "2020-10-26T17:49:20.357+03:00"
source_bytes: 9529
fetched_at: "2026-09-13T04:26:25+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis Sıkça Sorulan Sorular-Kredi Kartı

**Soru 1: Kredi kartı uygulamasının amacı nedir?**

Uygulamanın amacı kredi kartı ile yapılan tahsilatların takip edilmesidir. Bunu sağlarken mağaza ile banka arası kart sözleşmelerine ait detayların tanımlanabilmesi ve kart ile tahsilattan doğan alacakların banka bazında takibini sağlanır.

**Soru 2: Banka ve mağaza arasındaki sözleşme hangi detayda takip edilebilir?**

Uygulama aracılığı ile taksit bazında komisyon, kesinti ve masraf takipleri sağlanır. Hangi bankada, hangi karttan, hangi tarihte hesaba ne kadar para geçecek izlenir

**Soru 3: Kredi kartı uygulamasını hangi Logo Netsis çözümleri ile kullanabilirim?**

Kredi Kartı uygulaması tüm Logo Netsis çözümleri ile kullanılır.

**Soru 4: Birden fazla bankaya ait sözleşmeyi aynı anda takip edebilir miyim?**

Sözleşmeler banka ana kodu bazında takip edilir. Her banka için ayrı bir sözleşme tanımlanabildiği gibi aynı banka için birden fazla sözleşme de tanımlanabilir.

**Soru 5: Taksitlere uygulanacak kesintiler ne şekilde takip edilir?**

Kesintiler tıpkı sözleşmeler gibi banka ana kod bazında brüt ve net olmak üzere iki farklı şekilde tanımlanır. Brüt kesinti ana paranın içinde takip edilirken, net kesinti tahsilattan itibaren ana paradan düşülüp ayrı takip edilir.

Kesintiler vadesi geldiğinde ana para üzerinden hesaplanıp ilk taksitten düşülebileceği gibi, taksitlere yansıyacak şekilde vadeli olarak da uygulanabilir.

**Soru 6: Kesinti tanımındaki tahakkuk ve masraf muhasebe kodları ne zaman çalışır?**

Banka Şube Bazında Parametreler ekranında "Kart Masrafları Satış Anında Entegrasyona Atılsın" parametresinin işaretli olduğu durumda, masraf muhasebe koduna yazılan hesap brüt tipli kesintiler için borç çalışır. Parametrenin işaretli olmaması durumunda kesintiler "Kredi Kartı Tahsilat Kayıtları" yapıldığı sırada masraf hesabına borç olarak yansır.

Tahakkuk muhasebe koduna yazılan hesapta, brüt tipli kesintiler için alacak hareketleri oluşur. Net tipli kesintiler ise kredi kartı tahsilat kayıtlı işlemi esnasında tahakkuk hesabına yansır.

**Soru 7: Tahsilat anında puan kullanımı varsa nasıl bir tanım yapmalıyım?**
Eğer puan ile ödeme olacaksa Banka Sözleşme Tanımlamaları / Sözleşme Detayları ekranında taksit aralığı 0-0 olan bir tanım yapılmalı ve tahsilat işleminde puan ile ödeme yapmak için taksit sayısı 0 geçilmelidir.

**Soru 8: Sözleşme detayında taksit sayısı kadar tanım olmalı mı?**

Hayır. Vade, blokaj ve kesinti gibi takside uygulanan veriler taksit sayısına göre değişmiyorsa tam taksit aralığında tek tanım yapmak yeterlidir. Örneğin; taksit sayısı ne olursa olsun %3 komisyon, 15 gün blokaj ve 30 gün vade söz konusu ise, taksit aralığı 1-12 (Max. taksit) vererek tek satır tanım yapmak yeterlidir. Ancak taksit sayısına göre koşullarda bir değişiklik olduğu durumlarda tanım çoğaltılmalıdır. Örneğin; 6 takside kadar %3, 6 taksit ve üzeri %5 kesinti söz konusu ise 1-5, 6-12 taksit aralığı için iki ayrı tanım yapılmalıdır.

**Soru 9: Sözleşmelerde kullanılacak banka tanımlarında nelere dikkat etmeliyim?**

Sözleşmeye bağlanacak banka için hesap tipi "Kredi Kartı Hesabı" olan bir banka tanımlanmalıdır. Bu banka tanımında "Bağ.Hes.Kod" alanına kredi kartı tahsilat kayıtları işleminde çalışacak vadesiz mevduat hesabı seçilmelidir. Sözleşme, kesinti, vadesiz mevduat hesabı ve kredi kartı hesabı tüm bu tanımlar aynı banka ana koduna bağlı olmalıdır.

**Soru 10: Banka tanımında bulunan Fark A.M.K. ve Fark B.M.K. ne anlama gelmektedir?**

Sözleşme tanımında belirlenen kesinti oranı üzerinden hesaplanan kesinti tutarı ile bankanın vadesi geldiğinde uyguladığı kesinti arasında fark oluşabilir. Bu fark kredi kartı tahsilat kayıtları anında düzenlenebilir. Düzenlen değer ile programın ilk aşamada hesapladığı değer arasındaki fark kredi kartı hesabı tipli bankanın tanımındaki fark alacak muhasebe kodu ve fark borç muhasebe kodu alanlarında tanımlanan muhasebe hesaplarına aktarılır.

**Soru 11: Tanımladığımız sözleşmeleri hangi modüllerde kullanabiliriz?**

Kapalı kesilen satış faturalarını tamamlarken açılan "Hızlı Tahsilat Kayıtları" ekranında ve kasa modülünde "Hızlı Tahsilat Kayıtları" ekranında kullanılabilir. Kapalı tipli kesilen faturada "Hızlı Tahsilat Kayıtları" ekranının açılabilmesi için Satış Fatura Parametreleri Genel-3 sekmesindeki "Kapalı Faturada Tahsilat Ekranı Çıksın" parametresi işaretlenmelidir.

**Soru 12: Kredi kartı ile aldığım tahsilat hangi modülleri etkiler?**

Cari hesap alacak, kredi kartı banka hesabı borç çalışır. Buna bağlı olarak muhasebe modülünde cari, banka ve sözleşme tanımındaki kesinti hesapları çalışır.

**Soru 13: Yaptığım tahsilat kaydı üzerinde düzeltme – silme işlemi yapabilir miyim?**

Eğer tahsilat kaydına ait taksit "Kredi Kartı Tahsilat Kayıtları" ekranından vadesiz hesaba alınmadı ise, kasa modülünden girilen tahsilat kaydı "Hızlı Tahsilat Kayıtları" ekranından tekrar çağırılarak düzenlenebilir ve F7 ile silinebilir. Faturaya bağlı alınan tahsilat ise fatura iptali ile silinebilir ve düzeltme yapılacaksa fatura, toplamlarından tekrar onaylanarak tahsilat üzerinde düzenleme yapılabilir.

**Soru 14: Kredi kartı tahsilat kayıtları işlemi ne işe yarar?**

Tahsilat aldığımızda cari bankaya borçlanır, mağaza ise bankadan alacaklanır. Kredi kartı tahsilat kayıtları bu alacağa istinaden vadesi gelen taksitlerin vadesiz mevduat hesabına yani mağazanın varlığına eklenmesini sağlar.

**Soru 15: Yaptığım kredi kartı tahsilat kaydı işlemini geri alabilir miyim?**

Bu işlem sonrasında Banka modülünde "Banka Hesapları Arası Virman" ekranında virman kayıtları oluşur. Geriye alınmak istenen işlemin virman dekontu silinerek iptal edilebilir.

**Soru 16: Kredi kartı tahsilat kayıtları işlemi içerisinden sadece bir evraka ait kaydın tahsilatı geri alınabilir mi?**

Eğer hazırlık-oluştur işlemi "Kayıtlar Belge Detaylı Oluşsun" parametresi ile yapılır ise her tahsilat işlemi ayrı bir virman dekontu oluşturur. Böylece istenilen taksitin tahsilatı iptal edilebilir.

**Soru 17: Tahsilat işlemlerinde kart numarasının sorulmaması sağlanabilir mi?**

Kart numarası sorulur ancak programın doğruluğunu kontrol etmesi engellenebilir. Bunun için BANKA/KREDIKARTIKONTROLETME özel parametresi tanımlanmalıdır.
