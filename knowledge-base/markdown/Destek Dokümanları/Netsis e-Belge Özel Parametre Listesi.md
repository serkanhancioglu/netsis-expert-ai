---
title: "Netsis e-Belge Özel Parametre Listesi"
page_id: "108660605"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis e-Belge Özel Parametre Listesi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis e-Belge Özel Parametre Listesi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTc5ZTE4MTUzLTFlYzEtNGY2Ni1hMDQzLTZjOGUwYzEyZWFhYiZsaW5rPTA0ZTgyYjVjLTgyYTctNGNmMi1iNTcwLTNkOGFhZDVkMWVjNCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=79e18153-1ec1-4f66-a043-6c8e0c12eaab&link=04e82b5c-82a7-4cf2-b570-3d8aad5d1ec4&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-e-belge-ozel-parametre-listesi_113248425_108660605.html"
source_version: "2024-02-02T13:22:57.337+03:00"
source_bytes: 40235
fetched_at: "2026-09-13T04:23:28+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis e-Belge Özel Parametre Listesi

Netsis e-Belge özel parametreleri hakkında ayrıntılı bilgiye bu dokümandan ulaşılır.

| **GRUP** **KODU** | ANAHTAR | DEĞER | AÇIKLAMA |
| --- | --- | --- | --- |
| **EARSIV EFATURA EIRSALIYE** | **DOVIZLIOLUSTUR** | **E/H** | Dövizli e-Belgelerin taslak oluşturulması sırasında ekrana gelen "**Fiyat ve Tutarlar Dövizli Oluşturulsun mu?"** sorusunun özel parametre ile ekrana gelmemesi sağlandı. Özel parametrenin Değer alanına; dövizli belgelerden dövizli taslak oluşması için E, TL taslak Oluşması için H yazılması gerekir. |
| **EARSIV EFATURA EIRSALIYE** | **TASLAKBASIM** | **0** | e-Fatura, e-irsaliye, e-Arşiv belgelerinde "**TASLAK**" ibaresinin gösterilmemesi sağlandı. |
| **EBELGE** | **DIZAYNZORUNLU** | **0** | e-Belge taslağı oluştururken dizayn seçiminin zorunlu olabilmesi için sağlanmıştır. e-Fatura, e-Arşiv, e-İrsaliye ve e-Müstahsil' de desteklenmiştir. |
| **EFATURA** | **NET_FIYAT** | **E/0** | e-Fatura, e-Arşiv faturalarında kalemlerde net fiyatların basılması ve satırda iskontoların 0 gözükmesi sağlandı ve Taxableamount değerinin iskonto düşülmüş değer<br>olarak basılması sağlandı |
| **EFATURA** | **OLCUBIRIMI** | **E** | Farklı ölçü birimlerinden girilmiş faturanın her zaman 1.<br>ölçü birimine göre basılması sağlanır. |
| **EFATURA** | **FATNOSERIDEGISKEN** | **0/C** | Değer 0 tanımlandığında, aktarımla gelen faturlarda e- Fatura, e-Arşiv seri kontrolü yapılmaması sağlamaktadır. Ancak programın içinden girilir ise, kontrol yapılmaktadır. Değer C tanımlandığında Toplu e-Fatura /e-Arşiv Oluşturma ekranına sadece e- Fatura/e-Arşiv serisi ile girilmiş faturalar gelmektedir. |
| **EARSIV** | **YABANCIMUSTERI** | **0** | Ülke kodu TR olmayan cariler için; e-Arşiv faturası oluşturulduğunda, e-Arşiv faturada TCKN alanına "11111111111" atılması sağlandı. |
| **EARSIV** | **FATURAYURTDISI** | **0** | Dış Ticaret lisansı olsa bile, Toplu e-Arşiv Oluşturma ekranında "**Yurtdışı Faturalar Getirilsin**" seçeneği işaretlendiğinde, fatura modülünden İhr/İth tipli faturalar listelenmekte, Bu özel parametre tanımlanmadığında ise, dış ticaret modülünden İhr/İth<br>tipli faturalar listelenmektedir. |
| **EARSIV** | **KODDEGISTIRILMESIN** | **0** | e-Arşiv faturası oluşmuş faturada cari kod<br>değişikliği yapılamaması sağlandı. |
| **EFATURA** | **MENUGOSTER** | **0** | E-Fatura Görüntüleme ekranında sağ tık ile gelen menülerin gösterilmesi sağlanmıştır. |
| **EFATURA** | **SIFIRLARITEMIZLE** | **0** | E- Fatura Görüntüleme ekranında İrsaliye No alanında ve xml de DespatchDocumentReference ID değerinde soldaki sıfırların atılarak gösterilmesi desteklendi. Değer kısmına 6 yazılır, ise sondan 6 rakamı yazar. |
| **EFATURA** | **EFATURAESLESTIRILMESIN** | **0** | E-Fatura parametrelerine "**E-Fatura Eşleştirme Ekranı Fatura Girişinde Gösterilmesin**" ve "**E- Fatura Eşleştirme Ekranı Dekont Kaydında Gösterilmesin**" seçenekleri eklendi. Bu seçenekler işaretlendiğinde fatura veya dekont kaydı girerken e-fatura listesi çıkmaması sağlandı. Ayrıca fatura modülü için kullanılan özel parametre yerine bu seçenekler de kullanılabilir. |
| **EFATURA** | **IHRACATIRSALIYEKILITLEME** | **0** | İhracat dosyasına bağlanan irsaliyelerde değişiklik yapılabilmesi sağlandı. |
| **EFATURA** | **DISTICARETTUMBELGELER** |  | Toplu efatura oluşturma ekranında belge tipi "**İhracat** **faturaları**" ve "**dış** **ticaret** **modülünden oluşsun**" seçenekleri ile liste alındığında ihraç kayıtlı belgelerin de getirilmesi desteklenmektedir. |
| **EFATURA** | **FATURA_KAYIT_TARIHI_KULLANILSIN** | **0** | Satış faturası kaydında fiili tarih yerine fatura tarihinin TBLMUHFISEK tablosundaki tarih alanına gelmesi ve Fatura tarihinin edeftere evrak tarihi olarak yansıması sağlanmıştır. |
| **EFATURA** | **ALISFATNOYIL** | **0** | e-Faturadan alış faturası oluşturma ekranında oluşan fatura numarasında yıl kodu olması<br>desteklendi. Özel parametre olmadığı durumda oluşan fatura numarasında yıl kodu bilgisi bulunmamaktadır. |
| **EFATURA** | **TASLAKISARETLEME** | **0** | İhracat e-Faturasında kalemlerin toplam tutarı ile faturanın toplam mal hizmet tutarı arasında fark oluşması durumu düzeltilmiştir. |
| **EFATURA** | **KALEMOTVBAS** | **0** | Oluşturulan e-Faturada ÖTV'li stok varsa, ÖTV bilgisinin e-Faturanın XML' inde, kalem bilgilerinde de yazması sağlandı. Bu özel parametrenin **'EFATURA','NET_FIYAT'** ile birlikte kullanılmaması gerekiyor. |
| **EFATURA** | **COKLU_ISTISNA** | **0** | İhraç kayıtlı irsaliyelerde e-Fatura oluşturmadan önce kalem bazında ötv kapsamındaki stoklar için istisna kodu girilebilmesi desteklenmiştir. Ayrıca "**EFATURA\\KALEMOTVBAS**" özel parametresiyle oluşan e-Fatura xml belgesinin InvoiceLine tag değerine ötv bilgilerinin yazılması sağlanabilir. |
| **EFATURA** | **OTOALISFATNO** | **0** | e-Fatura carileri için alış faturası kaydı sırasında tarih alanı çıkışında resmi fatura numarasının otomatik doldurulması desteklenmiştir. |
| **EFATURA** | **IHRACKAYITLIOZELKOD** | **0** | Satış irsaliyesinde ihracat tipi İhraç Kayıt' tan farklı olan belgeler için Toplamlar sekmesine "**Özel Matrah/İstisna Tip Atama"** seçeneği eklenmiştir. İhraç kayıtlı belgelerde bu seçeneğin gelmesi için özel parametre tanımlanmalıdır. |
| **EFATURA** | **SEVKYUKLEME** | **0** | Fiş Oluşturma ekranında "**e-Fatura** **Fiş** **Oluştur**"<br>butonu desteklenmiştir. |
| **EFATURA** | **EFATAPI** | **0** | Api üzerinden e-Fatura gönderimi sağlanmaktadır. |
| **EFATURA** | **TAXARATABLOKULLAN** | **0** | e-Faturalar Api Ara tablo aracılığı ile oluşturulduğunda e-Fatura belgesindeki vergiler TBLEFATMASTAX ve TBLEFATKALEMTAX tablolarından alınır. Faturada iskonto olduğu zaman satır bilgilerindeki KDV tutarı iskontosuz fiyat üzerinden hesaplanarak gösteriliyor. XML'de de taxsubtotal alanına iskonto düşülmeden hesaplanan KDV tutarı yazmaktadır. |
| **EFATURA** | **EFATAPIDIZAYNSOR** | **0** | Api ara tablo ile e-Fatura oluştururken dizayn sorgulama ekranının gelmesi için tanımlanmalıdır. |
| **EFATURA** | **LINETAXABLEOTV** | **0** | Ötv' li e-Fatura belgelerinde, kalem satırında "**TaxableAmount**" tutarının "LineExtensionAmount" tutarıyla eşit gelmesi sağlanmıştır. |
| **EFATURA** | **UYGULAMAYANITSUBEKONTOLU** | **1** | e-Faturada uygulama yanıt ekranında her şube kendi e-Faturaları görmesi sağlanmıştır. |
| **FATURA** | **HATATASLAK** | **0** | Toplu e-Fatura taslak oluşturmada taslak oluşturulup göndermek istendiğinde herhangi bir sebepten hata oluştuğunda, gönderinin giden kutusuna düşmeyip taslak olarak kalması desteklenmiştir. |
| **EFATURA** | **PARCALIEIRSGETIR** | **0** | Satış Faturası ekranından "**Sipariş Bilgileri**" sekmesinden faturalaştırılan irsaliyelerin, "**Toplu e-İrsaliye Oluşturma**" ekranında "**Faturalaştırılan İrsaliyeler Getirilsin**" parametresi işaretli olduğunda listelenmesi<br>desteklenmiştir |
| **EFATURA** | **ISKONTOORAN** | **0** | Özel parametrenin değerine gönderilerin vergi numaraları ";" ile ayrılarak yazıldığında satırbazında iskonto değerleri oran olarak 4 kabul edilmesi desteklenmiştir. |
| **EFATURA** | **SIGARAKDV** | **0** | Toplu e-Fatura Oluşturma ekranına "**Sigara** **Faturası Oluşturulsun**" seçeneği eklenir. Seçenek<br>işaretlendiğinde, "**Sigara** **Uygulaması**" kullanılmayan durumlarda da e-Fatura oluştururken, sigara faturası gibi oluşturulması sağlanır. |
| **EFATURA** | **CHARSETUYARI** | **0** | Toplu e-Fatura basımında Türkçe karakterlerin düzgün görünmemesinin sebebi, farklı karakter kümeli belgelerden kaynaklandığı tespit edildiği için toplu basım yapıldığında fark edilmesi için bu özel parametre tanımlanmalıdır. |
| **EFATURA** | **SEVKBELGESECIM** | **0** | Fiş Oluşturma ekranına "**e-İrsaliye Oluşturulsun**" seçeneği eklenmiştir. e-Fatura cari hesapları için, ekranda seçilen tipte belgenin oluşturulması için özel parametre tanımlanmalıdır. |
| **FATURA** | **EFATHARICIBELGE** | **0** | Harici Yolla Fatura İptali sonrasında aynı fatura numarasının kullanılmasına izin verilmemesi sağlanmıştır. |
| **EFATURA** | **HALFATURASI_RUSUM_EKMALIYETKULLANILSIN** | **1,2,3** | Gelen hal fatursında rüsum vergisinin alış faturasına yansıması sağlanmıştır. Özel parametrenin değer alanına 1 yazılırsa ek maliyet 1, 2 yazılırsa ek maliyet 2, farklı bir değer yazılırsa ise ek maliyet 3 alanına rüsum vergisi toplamı yazılacaktır. Ek olarak rüsum vergisinin kdvsinin hesaplanması için alış parametrelerinde rüsum vergisi için kullanılan ek maliyet alanının kdv oranı tanımlanmış olmalıdır. |
| **FATURA** | **TASLAKISARETLEME** | **0** | Satış İrsaliyesi toplamlar sekmesinde "**Taslak** **Oluşturma Ekranı açılsın**" parametresinin işaretsiz gelmesi sağlanmıştır. |
| **EFATURA** | **DIZAYNRETBASMA** | **0** | Red almış e-Faturalar için basım yapıldığında basım<br>üzerinde "**Red**" yazısının gösterilmesi desteklenmiştir. Bu<br>özel parametresiyle eski kullanıma dönülebilir. |
| **EFATURA** | **SORGULA** | **0** | e-İrsaliye belgelerinde sorgulama işleminin istendiğinde "**Sadece Sorgula**" veya "**Sadece İndir**" olarak ayrı ayrı çalışabilmesi sağlanmıştır. |
| **EFATURA** | **ESKISORGULA** | **0** | e-Belge zarf bazı ekranlarda sorgulama seçeneğine ek olarak "Sadece sorgula" ve "Sadece İndir" seçenekleri eklenmiştir. Eski yönteme geçiş için bu parametre tanımlanmalıdır. |
| **FATURA** | **NOTALISISTISNAZORUNLU** | **0** | FATURA/ISTISNAONDEGER özel parametresi tanımlıyken e-Fatura carisi için muhasebeleştirilmiş hal alış faturası tekrar alış faturası ekranına çağrılıp değişiklik yapılmadan kapatılmak istendiğinde kayıtların son hali saklanmamış uyarısı alınması durumu 'FATURA','NOTALISISTISNAZORUNLU' özel<br>parametresi ile düzeltilmiştir. |
| **EFATURA** | **PASIFMUKELLEFGUNCELLE** | **0** | Pasif olan e-fatura carileri yeniden mükellef olması durumunda cari güncelleme işlemi çalıştırılınca durumunun aktif olarak güncellenmesi desteklenmiştir. |
| **FATURA** | **ESKITASLAKVARMI** | **0** | "**Toplu e-Arşiv Oluşturma**" ekranında "bu özel parametre tanımlı ise, tamama basınca "invalid pointer operation" uyarısının alınması engellenmiştir. |
| **DEKONT** | **EFATALISUYARI** | **0** | Genel dekont kaydı girişinde hesap koduna girilen cari e-Fatura mükellefi ise, "**e-Fatura carisi için belge oluşturmaktasınız**" uyarı mesajının parametreye bağlı olarak çıkması desteklenmiştir. |
| **EFATURA** | **IHRACATNUMARAKONTROL** | **1** | İhracat dosya işlemlerinde proforma fatura numarası alanında e-Arşiv ya da e-Fatura serili<br>numara girişi sonrasında ihracat dosyasına bağlan dendiğinde fatura numarası e-belge serileri için |
|  |  |  | uyumsuz uyarısı alınmaktadır. Bu özel<br>parametrenin tanımlanması gerekmektedir.<br>Offline e-Fatura kullanan yerlerde hem e-Fatura hem e-İhracat faturasında FYS serisi kullanılmak istendiğinde bu özel parametre tanımlanmalıdır. |
| **FATURA** | **EIRSALIYESAKLAKONTROL** | **0** | e-İrsaliye kullanılması durumunda, Satış Parametrelerinde "**Faturalaştırılan İrsaliyeler Saklansın**" seçiminin otomatik olarak seçilmesi sağlanmıştır. "e-İrsaliye Uygulamasından" bağımsız olarak, ilgili parametrenin kullanımı için özel parametresinin kullanılması gerekir |
| **EFATURA** | **SUBEVERGINO** | **0** | Gelen e-Faturada "**Şube Değişikliği**" yapılırken gönderilen şube ile zarfın ait olduğu VKN bilgisinin kontrol edilmesi ve aynı değilse bu işleme izin verilmemesi desteklenmiştir. |
| **EIRSALIYE** | **DATONAYKONTROLETME** | **0** | Onay parametresi açık olsa bile, onaylanmamış belgelerin de "**e-İrsaliye Oluşturma"** ekranına gelmesi sağlanmıştır. |
| **FATURA** | **GIBFATIRSNOYILSONKAR** | **0** | Fatura numarası "ABC202100000001" olarak girilen bir e-Belgede, "Resmi Belge Numarası"nın "ABC2021000000001" olarak oluşturulması desteklenmiştir. Önceki hali gibi, "ABC2021100000001" olarak, oluşturulması için özel parametre tanımlanmalıdır. |
| **FATURA** | **ASYAKIT** | **0** | e-Fatura üzerinde yer alan Sistem Fatura No alanının alış faturasındaki açıklama alanına yazılması desteklenmiştir. |
| **EFATURA** | **3065IHRKAYITLIACIKLAMAYAZILSIN** | **0** | İhraç kayıtlı belgelerde irsaliye faturaya dönüştürülürken atanan istisna kodunda "3065 Sayılı Kanunun 11-1/c Maddesi Kapsamındaki |
|  |  |  | İhraç Kayıtlı Satış" seçildiğinde ve özel parametre tanımlandığında oluşturulacak olan ebelgenin Notes alanına "3065 sayılı kanuna göre ihraç kayıtlı satış olup KDV tahsil edilmemiştir". ifadesinin yazılması sağlanmıştır. |
| **EBELGE** | **TEKRARLIBASIMSORULSUN** | **0** | Basımı yapılmış e-belgelerin tekrar basılmak istenmesi durumunda uyarı verilmesi sağlanmıştır. Değer 0 ise tüm e-belgeler, 1 ise e- fatura, 2 ise e-arşiv, 3 ise e-irsaliye, 4 ise e- müstahsil belgeleri için bu kontrol yapılmaktadır. İstendiğinde değer alanına noktalı virgül ayracı kullanılarak birden fazla belge tipi yazılabilmektedir. |
| **FATURA** | **EFATALISUYARI** | **0** | alış faturası girişinde gelen "**E-fatura carisi için belge oluşturmaktasınız**." uyarısının gelmemesi sağlanmıştır. |
| **EFATURA** | **FIYAT_OLCUBIRIMI** | **0** | Belge girişinde 2. ölçü birimi kullanılırsa ve<br>**"EFATURA/OLCUBIRIMI"** tanımlı ise 2. ölçü<br>biriminden belge oluşturulabilir. |
| **EFATURA** | **DIZAYNBASIMLOGAKAYDET** | **1** | e-Fatura parametrelerine "**E-Fatura basımları loglansın**" parametresi işaretlendiğinde, otomatik olarak bu özel parameter eklenir. |
