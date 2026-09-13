---
title: "Demirbaş Yönetimi SSS"
page_id: "111249163"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Demirbaş Yönetimi SSS"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Demirbaş Yönetimi SSS"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTkxYWU5NTYzLWIyMjItNDA4NC1iMTkzLWEwZDBkOGUyYjBlOSZsaW5rPWQzNzNmNjU1LTgyOTQtNDZlYi1hNzU0LTQ1N2UwNjA1YTUxYyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=91ae9563-b222-4084-b193-a0d0d8e2b0e9&link=d373f655-8294-46eb-a754-457e0605a51c&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "demirbas-yonetimi-sss_111249168_111249163.html"
source_version: "2023-05-22T10:08:30.797+03:00"
source_bytes: 12049
fetched_at: "2026-09-13T04:23:22+00:00"
generator: "netsis-scraper 1.0.0"
---
# Demirbaş Yönetimi SSS

**Demirbaş Yönetimi Temelset ve Personel uygulaması ile entegre çalışır mı?**

Demirbaş/Parametre Girişi/Veritabanı Bilgileri ekranından yapılacak tanımlamalar ile Demirbaş Yönetimi Temelset ve Personel uygulaması ile entegre çalışabilir.

**Demirbaş Yönetiminde yapılan işlemler için Temelset tarafında yevmiye kayıtları oluşturulabilir mi?**

Temelset veritabanı bağlantısının sağlandığı durumda, demirbaş kartlarına bağlanacak muhasebe hesapları ile amortisman hisseleri, KKEG tutarlar ya da satış ile oluşan tutarlar muhasebeye aktarılabilir.

**Demirbaş yönetiminde tanımlanan demirbaşın, alış belgesi Temelset tarafında oluşturulabilir mi?**

Temelset veritabanı bağlantısının sağlandığı ve Demirbaş Bilgi Kartı üzerinde satıcı bilgisinin doldurulduğu durumda Demirbaş Bilgi kartı üzerinde sağ click Dekont Oluşturma işlemi ile Netsis Temelset üzerinde alış belgesi Genel Dekont kaydı olarak oluşturulabilir.

Detaylı bilgi için [tıklayınız](<Demirbaş Modülünden Dekont Oluşturma.md>).

**Demirbaşlar Personel modülünde tanımlı sicil kartları ile ilişkilendirilebilir mi?**

Personel veritabanı bağlantısının sağlandığı durumda, Demirbaş Zimmetleme işlemi ile demirbaşların personellere zimmetlenmesi uygulama üzerinden sağlanabilir.

**Demirbaş değer artışı/azalışı nasıl takip edilir?**

Demirbaş Bilgi Kartı/Ek Bilgiler sayfasında bulunan Demirbaş Faiz Bilgileri Girişine tıklanarak açılan ekran üzerinden değer artışı![(plus)](../_assets/8bc1079dc378a6219e99.svg)/ azalışı![(minus)](../_assets/1b0d15e570bf80d3a5bb.svg) tutar olarak girilir. Girilen bu tutar sonraki aylarda ayrılacak amortisman tutarına etki eder. Detaylı bilgi için [tıklayınız](<Demirbaş Fon-Faiz Girişi.md>).

**Demirbaş kartları dövizli takip edilebilir mi?**

Demirbaşların alış bedelleri, bu bedel üzerinden ayrılan amortisman tutarı ve muhasebesel karşılıkları döviz değerleri ile takip edilebilir.

Dövizli muhasebe "FAS 52" seçeneği işaretli olmalı ve düzeltme tipi seçilmeli Sabit kıymet kartı dövizli olarak tanımlanmalı, döviz tipi ve fiyatı doldurulmalı Dövizli Muhasebeye Başlama çalıştırılmalı

Demirbaş Düzeltme Bilgileri girişi ekranında düz. Ömür yılı girilmeli

Döviz\\Enflasyon çevirim çalıştırılmalı

**Tek bir kart üzerinde birden fazla miktarla takip edilen demirbaşlar için kısmi satış nasıl yapılır?**

Kısmi satış varsa öncelikle demirbaşın ayrı kartlara ayrılması gerekir. Birden fazla miktarda alınmış demirbaşların tutarsal ya da miktarsal olarak parçalanabilmesi için Demirbaş Parçalama işlemi yapılır. Tutarsal/miktarsal olarak parçalanan demirbaşın her parçası için yeni kart oluşur ve tanımda belirtilen tutar kadarlık kısım bu yeni kart üzerine aktarılır. Satış işlemi bu yeni kart üzerinden gerçekleşir.

Detaylı bilgi için [tıklayınız.](https://www.youtube.com/watch?v=j5uSKJJst7s)

**Demirbaş Yönetimi uygulamasında açılmış farklı şirketler arasında demirbaş transferi yapılabilir mi?**

Demirbaş Transferi işlemi ile demirbaşlar şirketler arasında transfer edilebilir. Bu işlem ile demirbaşın biriken amortismanı da transfer şirketinde takip edilir.

**Uygulama kullanılmaya başlanmadan önce alınmış olan demirbaşlar güncel verileri ile takip edilebilir mi?**

Eski demirbaşlar için gerçek alım tarihleri ile demirbaş kartları tanımlanır ve Devir Amortisman Bilgileri ekranından bu demirbaşlara ait istenilen tarih itibari ile güncel fiyat, biriken amortisman, pas geçilen amortisman gibi tüm bilgiler girilir. Böylece sonraki aylarda bu girilen tutarlar üzerinden amortisman hesaplaması sağlanabilir.

Detaylı bilgi için [tıklayınız](<Devir Amortisman Bilgileri Girişi Destek Dokümanı.md>).

**Demirbaşın birikmiş amortismanı, fon tutarı ya da aylık amortismanı gibi sahalarda elle düzenleme yapılabilir mi?**

Amortisman bilgileri düzenleme ekranı ile bu bilgiler üzerinde kalıcı düzeltme sağlanır. Sonraki aylarda tutarlar bu düzeltmiş bilgiler üzerinden oluşur.

**Amortisman ayırma işlemi yapıldıktan sonra geçmiş ayda bir düzeltme yapılabilir mi?**

Geçmiş aya dönülüp yapılacak işlemin sonraki aylara yansıması için değerleme ve amortisman ayırma işlemi çalıştırılması gerekir. Bu da sonraki aylara ait amortisman bilgilerini siler.

**Yatırım aşamasındaki bir varlık edinimi takip edilebilir mi?**

Yatırım sürecinde yapılan tüm harcamalar Yatırım Girişi ekranı üzerinden takip edilebilir. Yatırım tamamlandığında ise bu harcamalara istinaden demirbaş kartının aktife geçiş işlemi ile otomatik olarak açılması sağlanır.

**Kiralama usulü edinilen demirbaşların takibi sağlanabilir mi?**

Kiralamaya ait sözleşme, sözleşme kapsamında kiralanan demirbaş kartları, yapılacak ödemeye ait ödeme planı ve bunlara ait muhasebe işlemleri Finansal Kiralama ekranlarından takip edilebilir.

**KKEG nedir?**

Kanunen kabul edilmeyen giderin kısaltmasıdır. Sıfır binek araç maliyet, masraf ve ikinci el araçlar için belirlenmiş üst sınıra kadar olan amortisman tutarı gider olarak gösterilebilir. Bu limitleri aşan kısım ise KKEG olarak adlandırılır. Bu takip Demirbaş Bilgi Kartlarında Binek Oto Uygulaması yönteminin seçilmesi ve Demirbaş Parametrelerinde üst limitlerin belirlenmesi ile mümkündür.

Detaylı bilgi için [tıklayınız.](https://www.youtube.com/watch?v=yPy7rkX4P34)

**Amortisman tutarları günlük hesaplanabilir mi?**

Günlük amortisman takibi yapılabilir. Uygulamanın kullanılabilmesi için DEMIRBAS\\DEMGUNLUK özel parametresinin tanımlanması ve gün esasına göre amortisman ayrılacak sabit kıymetin kartı açılırken "Günlük Amort" kutucuğunun işaretlenmesi gerekir.

Detaylı bilgi için [tıklayınız](<Demirbaş Günlük Amortisman Takibi.md>).

**Farklı günlerde farklı işlerde kullanılan demirbaşların çalışma günü kadar farklı muhasebe hesabını çalıştırması sağlanabilir mi?**

Demirbaş devam bilgileri takibi ile demirbaşın kullanıldığı proje ve günü bazında amortisman tutarının farklı muhasebe hesaplarına gitmesi sağlanabilir.

**Yeniden değerleme nedir?**

Yeniden değerleme iktisadi kıymetlerin net defter değerlerini fiyat endeksindeki artış kadar arttırıp, bu varlıkların maliyetlerinin güncellenmesine olanak sağlayan bir işlemdir. Bu yöntemle değerlenen varlığımız üzerinden

gösterdiğimiz gider artar.

Detaylı bilgi için [tıklayınız](<7338 Sayılı Kanun 537 nolu Tebliğe İstinaden Taşınmazların ve Amortismana~1abe73.md>).

**Yeniden değerleme yapılınca ömür yılı uzar mı?**

Yeniden değerleme ömür yılını uzatmaz. Kalan ömründeki amortisman tutarını arttırır.

**Bazı durumlarda bir süreliğine amortisman ayrılmaması gereken demirbaşlar için ne yapılabilir?**

Demirbaş Bilgi Kartında bulunan Pas Geçilsin parametresi işaretlenmelidir. İşaretli olduğu dönemlerde ilgili demirbaş için amortisman ayrılmayacak, hesaplanan amortisman pas amortisman sahasında tutulacaktır. Tekrar amortisman ayrılacağı dönemde parametrenin kaldırılması gerekir.

**Kıstalyum uygulaması nedir?**

Faaliyetleri kısmen veya tamamen binek otomobillerin kiralanması veya çeşitli şekillerde işletilmesi olanların, işletmelere ait binek otomobillerinin aktife girdiği hesap dönemi için ay kesri tam ay sayılmak suretiyle kalan ay süresi kadar amortisman ayrıldığı yöntemdir. Amortisman ayrılmayan süreye isabet eden bakiye değer, itfa süresinin son yılında tamamen yok edilir.

**Eski kıstalyum uygulaması nedir?**

Kıstalyum uygulamasında demirbaşın alındığı yıl ayrılmayan amortisman son yıla yedirilirken, eksi kıstalyum uygulamasında, demirbaşın alımından bir sonraki yıl amortisman ayrılırken , alındığı yıl ayrılmayan amortisman sanki ayrılmış gibi birikmiş amortisman hesaplanmaktadır.

**Demirbaş Yönetiminde özel dönem takibi yapılabilir mi?**

Parametre girişinde bulunan mali başlangıç ayı kullanılarak özel dönem takip edilebilir. Demirbaşlar için hesaplanacak ömür, çalışmayan kısım gibi bilgiler özel dönemi dikkate alarak hesaplanacaktır.
