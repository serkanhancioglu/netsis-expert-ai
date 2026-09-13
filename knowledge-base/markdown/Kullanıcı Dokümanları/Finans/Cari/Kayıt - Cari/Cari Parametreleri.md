---
title: "Cari Parametreleri"
page_id: "22805127"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Cari"
  - "Kayıt / Cari"
  - "Cari Parametreleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Cari / Kayıt / Cari / Cari Parametreleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTZmMWMwMDA1LTY3MjYtNDA1ZC04YWM3LWIyMTNiNDFkMjNjNyZsaW5rPWQ1MGU1MzQ3LTE5NjYtNGJjYi04N2M3LTFkNDg5N2FlMzM2ZSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=6f1c0005-6726-405d-8ac7-b213b41d23c7&link=d50e5347-1966-4bcb-87c7-1d4897ae336e&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "cari-parametreleri_22805131_22805127.html"
source_version: "2022-10-31T09:18:12.443+03:00"
source_bytes: 28934
fetched_at: "2026-09-13T04:07:49+00:00"
generator: "netsis-scraper 1.0.0"
---
# Cari Parametreleri

Cari Parametreleri, Cari Modülü ile ilgili parametre tanımlarının yapıldığı bölümdür. Cari Parametreleri ekranı; Genel, Kullanıcı Tanımlı Sahalar ve Özel Hesap Kapatma olmak üzere üç sekmeden oluşur.

**Genel**

Cari Parametreleri ekranı Genel sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Cari Parametreleri Ekranı |  |
| --- | --- |
| Aylık Faiz Oranı | Vade farkı raporlarının alınmasında önem kazanan ve hesaplanacak faizin aylık oranının yüzdesel olarak kaydedilmesini sağlayan parametredir. Vade farkı raporlarında bu alana girilen faiz oranı, ilgili alana aktarılır ve üzerinde istenilen değişiklik yapılabilir. İsteğe bağlı olarak boş bırakılabilir. |
| Grup Açıklama | Cari hesap sabit bilgileri girişi sırasında oluşturulan grup kodlarının isimlerinin veya açıklamalarının aynı ekran üzerinde bir pencere yardımıyla tanımlanmasını sağlayan parametredir. Böylece, sabit bilgi girişi sırasında daha önceden grup kodu kayıtları bölümünde tanımlanmamış yeni bir grup kodunun açıklaması da anında kaydedilir. Parametre işaretlenmezse, ilk defa kullanılan bir grup kodunun ismi veya açıklamasının, "Grup Kodu Kayıtları" bölümünden girilmesi gerekir. |
| Hareketlerde Rapor Kodu Girilsin | Elle girilecek cari hareketlerde veya kasa, dekont, çek/senet gibi işlemlerden yapılan entegre kayıtlarda, açılan ekrana maksimum bir karakterlik rapor kodu girilmesini sağlayan parametredir. Her hareket için ayrı ayrı girilebilen bu kod sayesinde, rapor alırken kullanıcıya kolaylık sağlanır. |
| Hareketlerde Miktar Girilsin | Elle girilen cari hareket kayıtlarında ve entegre olan kasa, dekont işlemlerinde miktar girilmesini sağlayan parametredir. Girilen miktar bilgileri, Genel → Rapor → Raporlar → Cari Raporlar bölümünden listelenebilir. |
| Cari Kullanım Tipi | Bu alanda seçilen kullanım tipine göre merkez ve şubelerde cari hesapların çalışma mantığı değiştirilebilir. Cari kullanım tipi; Tüm Cari Hareketleri, İşletme/Şirket/Şube ve Şubeli Cari olmak üzere 3 çeşittir. Alanın sağ tarafında yer alan aşağı ok butonu ile seçim yapılır. **Tüm Cari Hareketleri:** Merkez ve şubede tüm cari hareketlerin ortak olarak izlenmesini sağlar. Yani şubeden/merkezden de bir kayıt girildiğinde, girilen kayıt merkezin/şubenin cari hareketlerinde görülebilir. **İşletme/Şirket/Şube:** Bu seçenek sadece "Logo Netsis Enterprise" paketinin kullanılmasıyla aktif hale gelir. İşletmelerin merkezinden programa girilmesi halinde, cari hesabın tüm işletmelere ve şubelere ait hareketlerinin izlenmesini sağlar. Merkez olmayan işletmeden programa girildiğinde, sadece ilgili cari hesaba ait kendi bünyesindeki ve şubelerindeki hareketler izlenebilir. İşletmenin şubesinden programa girildiğinde ise, sadece o şubeye ait hareketler izlenir. **Şubeli Cari:** Bu seçenek, her şubenin kendi hareketlerini, merkezin ise tüm hareketleri görmesi ve hareket raporlarının da bu mantıkta listelenmesini sağlar. "Şubeli Cari" seçeneği işaretlendiğinde, cari sabit kayıtlarında "İlgili Şube" alanı ekrana eklenir ve bu alanda carinin hangi şubeye ait olduğu sorgulanır. Müşteri/Satıcı, sadece belli bir şube ile çalışıyor ve diğer şubelerin bu kartla ilgili işlem yapılmasını istemiyorsa, bu alana çalıştığı şube kodu girilir. Bir cari kart merkezden açıldığında ise, hangi şubede kullanılan cari olduğu bu alana girilecek şube kodundan anlaşılır ve hangi şubede hangi hareketlerin görüleceği buna göre belirlenir. |
| Ciro Primleri İçin Kullanılacak Cari Rapor Kod | Ciro Primi Uygulaması ile ilgili bir parametredir. "Ciro Primi Hak Ediş Bilgileri" bölümünde, burada belirlenecek rapor kodlarından birine göre tanımlama yapılır. Ciro Primi Uygulaması ile ilgili detay bilgi için; Cari → Ek-4 (Ciro Primi Uygulaması). |
| Koşul Politika Tanımlaması Yapılsın | Koşul kayıtları ile ilgili olarak, Koşul Politika Tanımlamasının kullanılması istendiğinde işaretlenmesi gereken parametredir. "Koşul Politika Tanımlama" bölümünde yazılacak Visual Basic script’ i ile, "Ek Koşul Kayıtları" bölümünde "İlave Şekli" tercihi ile uygulanabilecek politikalardan daha geniş kapsamlı politika tanımlamasının yapılmasını sağlar.<br>Koşul politika tanımlaması ile ilgili detay bilgi için; Cari → Kayıt → Koşul Kayıtları → Koşul Politika Tanımlamaları. |
| Koşul Politikaları Ek Koşula Bağlanmasın | Koşul politikalarının ek koşula bağlı çalışmasının istenmediği durumlarda işaretlenmesi gereken parametredir. |
| Cari İsim Sorgulama Kaynağı | Alanın sağ tarafında yer alan aşağı ok butonu ile; Sorgulama Yapılmasın, e-Fatura Mükellef Listesi ve Noterler Birliği Servisi seçeneklerinden biri seçilerek sorgulama kaynağı belirlenir. **e-Fatura Mükellef Listesi:** Cari Hesap Kayıtları → "Cari Kod" rehber butonunun yanında bulunan "Cari Ünvan Bilgisi Getir" butonunu aktif hale gelir. Böylece, cari hesabın vergi numarasına denk gelen e-Fatura mükellefinin resmi adı cari isim alanına getirilir ve istendiği zaman bu isim ile cari isim güncellenebilir. **Noterler Birliği Servisi:** Ekran üzerinde "Noterler Birliği Bağlantı Bilgileri" kısmının aktif hale gelmesini sağlar. Kimlik Bilgisi ve Şifre bilgileri girilerek bilgiler doğrulanır. Cari hesapların TCKN veya VKN numaraları eşleştirilerek cari hesabın eksik veya hatalı olan adresi, unvanı, TCKN veya VKN bilgilerinin getirilmesi için kullanılır. "Noterler Birliği Servisi" seçildiğinde; Noterler Birliği bağlantı bilgilerinde servise bağlanılacak olan kullanıcının TCKN/VKN numarası ve şifresi girildikten sonra bağlantı bilgilerinin kaydedilmesi gerekir. Bilgiler kaydedildikten sonra "Cari Hesap Kayıtları" ekranında seçilen cari kodun, cari rehberinin sağındaki sorgulama tuşu ile noterler birliğinden sorgulama yapılabilir veya Cari → İşlemler → "Toplu Online Cari Sorgulama" ekranı kullanılabilir. |
| Cari Bazında Tanımlanan Döviz Kurları Belgede Değiştirilemesin | Cariler için tanımlanan kur bilgisinin değiştirilmesinin engellenmesi için kullanılan parametredir. |

**Kullanıcı Tanımlı Sahalar**

Cari Parametreleri ekranı Kullanıcı Tanımlı Sahalar sekmesindeki rapor amaçlı olarak kullanılabilen alanlar Sayısal ve Alfa sayısal olmak üzere iki bölümden oluşur.

| Cari Parametreleri Ekranı |  |
| --- | --- |
| Sayısal Saha Başlıkları | Cari hesap kayıtları için, ek bilgi alanı olarak ve rapor bazlı kullanılmak üzere sekiz adet sayısal saha başlık tanımlamasının yapıldığı alanlardır. Sahaların başlıkları bu ekrandan tanımlanır. "Cari Hesap Kayıtları" ekranındaki "Kullanıcı Tanımlı Sahalar" sekmesinde, burada girilen başlıkların karşılığı kayıtlar girilir. Burada boş geçilen alanlar, kullanılması istenmeyen alanlar olarak nitelendirilir ve ek bilgiler bölümünde ekrana gelmez. Genel → Rapor → Raporlar → Cari Raporlar bölümündeki Cari Sabit ve Hareket listelerinden girilen bu alanların raporları alınabilir. |
| Alfa Sayısal Saha Başlıkları | Cari hesap kayıtları için, ek bilgi alanı olarak ve rapor bazlı kullanılmak üzere sekiz adet alfa numerik saha başlık tanımlamasının yapıldığı alanlardır. Sahaların başlıkları bu ekrandan tanımlanır. "Cari Hesap Kayıtları" ekranındaki "Kullanıcı Tanımlı Sahalar" sekmesinde, burada girilen başlıkların karşılığı kayıtlar girilir. Burada boş geçilen alanlar, kullanılması istenmeyen alanlar olarak nitelendirilir ve ek bilgiler bölümünde ekrana gelmez. Genel → Rapor → Raporlar → Cari Raporlar bölümündeki Cari Sabit ve Hareket listelerinden girilen bu alanların raporları alınabilir. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | İşaretlenen parametrelerle ilgili işlemlerin gerçekleşmesini sağlayan butondur. Parametrelerle ilgili işlemlerin programa yansıması için programın kapatılıp tekrar açılması gerekir. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | İşaretlenen parametrelerden vazgeçilmesi halinde kullanılan butondur. |

**Özel Hesap Kapatma**

Cari Parametreleri ekranı Özel Hesap Kapatma sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Cari Parametreleri Ekranı |  |
| --- | --- |
| Özel Hesapta Proje Kodu Kontrol Edilsin | Proje kodu uygulamasının kullanıldığı yerlerde ve özel hesap kapatma ile çalışan cari hesaplarda, proje kodu kontrolünün yapılmasını sağlayan parametredir. Parametre işaretlendiğinde, kapatılacak hareketlerin proje kodlarının aynı olmasına dikkat edilmesi gerekir. İşaretlenmediğinde ise, özel hesap kapatma ekranlarında proje kodu kontrolü yapılmaz ve dolayısıyla proje kodları farklı olan hareketlerde birbirleriyle kapatılabilir. |
| Özel Hesap Kapatma Opsiyon Günü | Özel hesap kapatma opsiyon gününün Sayısal, Alfasayısal, Sabit Gün veya Kullanılmasın seçilerek belirlenmesini sağlayan seçenektir. Sabit Gün seçildiğinde alanın sağ tarafında yer alan sahaya gün sayısı girilir. Seçilen borç/alacak hareketlerinin ortalama vade günlerinin arasında "Özel Hesap Kapatma Opsiyon Günü" alanında seçilmiş olan değerden daha büyük bir fark olup olmadığını kontrol edilmesi ve daha büyük bir fark varsa, kullanıcıya uyarı mesajı gösterilmesi için kullanılır. |
| Özel Hesap Kapatma İşleminde Döviz Tipi Kontrol Edilsin | Özel hesap kapatma işlemi yapılırken döviz tiplerinin kontrol edilmesi için kullanılan seçenektir. Aynı döviz tipleri arasında özel hesap kapatma işleminin yapılmasını destekler. İşaretlenmediği zaman farklı döviz tiplerinin birbirleri ile kapatması yapılabilir. Seçenek, varsayılan olarak işaretli şekilde ekrana gelir. |
| Özel Hesap Kapatma İşlemi Yapılmadan Ekrandan Çıkılmasın | Özel hesabın kapatma işleminin zorunlu tutularak, hesap kapatma yapılmadan ekrandan çıkılmasının engellenmesi için kullanılan seçenektir. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | İşaretlenen parametrelerle ilgili işlemlerin gerçekleşmesini sağlayan butondur. Parametrelerle ilgili işlemlerin programa yansıması için programın kapatılıp tekrar açılması gerekir. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | İşaretlenen parametrelerden vazgeçilmesi halinde kullanılan butondur. |
