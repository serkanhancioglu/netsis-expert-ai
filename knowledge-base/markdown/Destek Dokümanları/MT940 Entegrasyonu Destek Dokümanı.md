---
title: "MT940 Entegrasyonu Destek Dokümanı"
page_id: "50680010"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "MT940 Entegrasyonu Destek Dokümanı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / MT940 Entegrasyonu Destek Dokümanı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPThlZWE4ZDgxLWNjYWYtNDRiMy1iZWJjLTRjYWY5NjZkNzc2ZiZsaW5rPTYwMjg0MDJmLTE3M2EtNGZkMi1hYjRhLTQ2N2M2MzA5YjNjYSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=8eea8d81-ccaf-44b3-bebc-4caf966d776f&link=6028402f-173a-4fd2-ab4a-467c6309b3ca&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "mt940-entegrasyonu-destek-dokumani_82576345_50680010.html"
source_version: "2022-11-03T09:39:02.233+03:00"
source_bytes: 819840
fetched_at: "2026-09-13T04:26:01+00:00"
generator: "netsis-scraper 1.0.0"
---
# MT940 Entegrasyonu Destek Dokümanı

MT940 Entegrasyonu ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

**Amaç** **ve** **Fayda**
MT940, uluslararası standartlarda belirlenmiş elektronik hesap ekstresi formatıdır. Bankalardan firmanıza alınan ve hesaplarınızda oluşan hareketleri içeren bu dosyanın Netsis ERP sistemine entegrasyonu sağlanmıştır.
**Ürün** **Grubu:** Netsis Enterprise Netsis Standard Netsis Entegre
**Modül:** Banka
![](../_assets/9ffffa3f3907222a915c.png)

#### SWIFT MT940 Elektronik Hesap Özeti Entegrasyonu

![](../_assets/63d0ad99f5362c9e4a70.png)

Bankadan MT940 formatında aldığınız hesap hareketleri ile sisteminizde otomatik olarak cari, banka, muhasebe ve çek ile ilgili kayıtlarının oluşturulması sağlanabilmektedir. Entegrasyon süreci ile ilgili kullanım bilgilerinin tanımlanmasına yönelik ekranlara Banka modülünde Kayıt bölümü MT940 Kayıtları içerisinden erişim sağlayabilirsiniz.
![](../_assets/8aac12df42cf1d5da323.png)![](../_assets/6ac498e72c440ebf3ee1.png)

#### İşlem Kodları

Sistem üzerinde standart işlem kodları otomatik olarak oluşturulmaktadır. Mevcut işlem kodları dışında çalışılan banka tarafında desteklenen ek işlem kod kayıtları da bu bölümde yapılabilecektir. Desteklenen standart işlem kodları tanımlamaları ile ilgili detay bilgi için bakınız Ek-1 (MT940 Standart İşlem Kodları)

#### Kural Bilgileri

Banka hesap hareketlerinizin entegrasyon sürecinde Netsis ERP sisteminde çeşitli belgeler oluşturulabilecektir. MT940 satırlarında yer alan bilgi kalıpları doğrultusunda hangi belgelerin oluşturulacağının belirlenmesi ve sistemde ilişkili oldukları Cari-Muhasebe-Banka-Çek bağlantılarının tespitine yönelik tanımlamalar bu bölümde yapılabilecektir.
**Metin:** Metin alanında yer alan bilgi sistem tarafından bankadan alınan dosyanın hesap hareket satırları içinde metinsel olarak aranarak ilişkili kural tespiti sağlanacaktır. Yani tanımlanacak kural, tanımlanan metnin içinde geçtiği satırlar için çalışacaktır.
**Bilgi Amaçlı:** Bilgi Amaçlı seçeneği işaretlendiğinde, bilgi amaçlı olarak işaretli olan kural ile eşleşen kayıt varsa MT940 entegrasyonu sırasında bu kaydın aktarımı yapılmıyor.
![](../_assets/fe802c549a8a52574047.png)

**Belge Tipi:** İlgili satır için sistemde hangi tip belgenin oluşturulacağıdır. Belge Tipi oluşturulabilecek belgeler; Genel Dekont, Havale/EFT/Bankalar Arası Virman, Çek Tahsil, Çek Ödendi, Senet Tahsil, Senet Ödendi, Bankadan Gelen Karşılıksız Çek, Bankadan Gelen Protestolu Senet, İade Çek, İade Senet.

**Cari-Banka-Çek/Senet-Muhasebe Kodları:** İlgili satırın ilgili belgede hangi varlık (cari hesap, banka hesabı, muhasebe hesabı, çek ya da senet) ile ilişkilendireceği ve bu varlığın sistemdeki kodunun karşılığı belirtilebilir.

#### İşlem Kodları ve Kuralları Eşleştirme

MT940 dosyasında yer alan işlem kodlarının yukarıdaki hangi kurallarla eşleşeceğinin tanımlandığı bölümdür. Bir işlem kodu birden fazla kuralla eşleştirilerek opsiyonel olarak ilgili kuralda tanımlanan belgenin oluşması ve ilgili hesabın işlem görmesi sağlanabilir.

#### MT940 Entegrasyonu (Banka Entegrasyonu)

Banka modülünde Kayıt bölümü MT940 Kayıtları menüsünün altından ulaşılabilecek bu adımda, bankadan alınan metinsel (txt uzantılı) dosyanın sisteme entegrasyon süreci bu bölümde yapılabilmektedir.
![](../_assets/aa8bbd10ba264f2517cd.png)![](../_assets/9257385d726a48c84716.png)
**Dosya Adı:** Bankadan alınan MT940 desenindeki dosya, dizin adresi ile seçilebilecektir. Seçim sonrasında dosya içeriği alt bölümde görüntülenecektir.
**Kontrol:** Kontrol işlemi ile dosya içeriği ayrıştırılıp; tespit edilen bilgiler ile hesap hareketleri görüntülenecektir. Kontrole tıklandığında MT940 dosyası ilk defa okunuyorsa kullanıcının mevcut kontör sayısından kontör düşülecektir. Tekrar eden okumalarda kontör sayısı değişmeyecektir.
**Mevcut** **Kontör** **Sayısı:** Tanımlı kullanıcı bilgilerine ait kalan kontör sayısını göstermektedir.
Kontrol işlemi yapılmaksızın daha önce görüntülenmiş ve düzeltilmiş hesap hareketleri bölümüne geçmek için mevcut kayıtlar seçeneği kullanılabilir.
Bu bölümde görüntülenen hesap hareketlerine dair bilgiler üzerinde güncelleme yapılabilecektir.
Sistem tarafından işlem kodları ve kuralları eşleştirme bölümünde tanımlanmış bilgiler kullanılarak hesap hareketi ile eşleşen kural tespit edilecek ve oluşacak belge içerikleri listelenecektir. Kural tespitinde işleyiş önceliklendirmesi aşağıda belirtildiği sıradadır (Bir önceki adımda kural tespit edilememesi durumunda sonraki adım işletilmektedir):

- İşlem kodu ve borç/alacak durumuna bağlı olarak bulunan kurallar içerisinde metin alanı, hesap hareket açıklamasında bulunan.
- İşlem kodu ve borç/alacak durumuna bağlı olarak bulunan kurallar içerisinde varsayılan kural olarak seçilen.
- İşlem kodu ve borç/alacak durumuna bağlı olarak bulunan tek kural.

Yukarıda belirtilen öncelikler ile ilgili hesap hareketi için uygun bir kural mevcut ise bu bilgi sistem tarafından otomatik olarak tespit edilip kullanıcıya sunulacaktır. Bununla birlikte kural kodu ve detayları kullanıcı tarafından değiştirilebilecektir.

#### Kural Kaydet

Aynı ekran üzerinde hesap hareketlerinde ilgili işlem kodunun ilk defa kullanılması, vs. sebeplerden ötürü uygun bir kuralın sistem tarafından tespit edilememesi durumunda kullanıcı açıklama, işlem tipi ve kod rehberi yardımı ile kod bilgilerini oluşturup kısayol yardımı ile yeni bir kural tanımlayabilecektir.
Bu bölümde yapılan kayıt işlemi ile sistem tarafından kural tanımlama ve eşleştirme bölümlerine dair kayıtlar, otomatik olarak oluşturulacaktır.

Geri, Kısıtlar sekmesine geri döner.

Bilgileri Kaydet, ekranda yapılan düzeltme çalışması tamamlanmadığı durumda, belgeleri oluşturmaksızın ekrandaki bilgileri kaydeder.

Hepsini Aktar işlemi ile bankadan alınan hesap hareketleri için kural ve hesap hareket açıklama bilgileri kullanılarak sistem üzerinde belirlenen belge tiplerine uygun kayıtlar oluşturulacaktır. Sistem genelinde yapılan tanımlamalara göre oluşacak belgelerde kullanılmak üzere eksik bilgiler, kullanıcıdan alınacaktır.
![](../_assets/bb043960b7ab1f57f891.png)
İşlem esnasında hareket bazında gerekli kontroller yapılıp; sorun olmaması durumunda entegrasyon işlemi tamamlanacaktır.

#### MT940 Parametreleri

![](../_assets/c673a741336d70cf6645.png)

Web Servis Parametreleri Mt940 servisi için verilecek olan kullanıcı bilgilerinin girileceği yerdir. Servisin çalışıp çalışmadığının kontrolünü "Web Servis Erişimini Kontrol Et" düğmesine tıklayarak kontrol edilebilir. Servis'in çalışma durumuna göre ekranda başarılı veya başarısız yazacaktır. Burada girilecek bilgiler hatalı veya boş olduğunda MT940 entegrasyonu ekranı açılışında "Geçersiz kullanıcı adı/şifre" uyarısı gelecektir.

#### SWIFT MT940 Deseni

Uluslararası standartlarda belirlenmiş elektronik hesap ekstresi formatı, MT940 deseninde yer alan özellikler açıklanmaktadır.
Desen içerisindeki satırlar, bölüm başlıkları ile ele alınmaktadır. Bölüm başlıkları için Tag Numarası/Alan adı belirteçleri kullanılmaktadır. Bölüm başlığı altında ilgili satırın içeriğindeki detaylar ve açıklamaları yer almaktadır.

#### Desen Özellikleri

**:20:** Hesap ekstresi, :20: tag numarasıyla başlamaktadır. Bu alanda referans numarası bilgisi yer almaktadır.
**:25:** Bu alanda hesap bilgileri yer almaktadır. Hesap bilgileri 2 farklı şekilde değerlendirilebilecektir.

1. IBAN numarası yer almaktadır.
2. Banka kodu-Şube kodu/Hesap no ayraç kullanımları ile bulunmaktadır. (–) ve ![(tick)](../_assets/72b3afd8b2fe319fbd82.svg) banka kodu (4 karakter) ile şube kodu (5 karakter) arasında ![(minus)](../_assets/1b0d15e570bf80d3a5bb.svg) ayracı kullanılması beklenmektedir. Banka Hesap no bilgisi ![(tick)](../_assets/72b3afd8b2fe319fbd82.svg) ayracı ile diğer bilgilerden ayrılmaktadır.

**:28:** Ekstre numarası yazılmaktadır.
**:60F:** Hesap ile ilgili borç/alacak bilgisi, tarih, döviz-cinsi ve o günkü açılış bakiyesi yazılmaktadır.
Borç/Alacak: 1 karakter
Tarih: 6 karakter (yıl/ay/gün) Döviz cinsi: 3 karakter
Açılış bakiyesi : 15 karakter
**:61:** Hesabın o gün yapılmış olan hareket bilgisi yer almaktadır. Bu alanda tarih, borç/alacak, hesabın döviz cinsinin son karakteri ve yapılmış olan işlemin kodu yer almaktadır. İlgili hesap detayı NONREF kodu tamamlanmaktadır. Duruma göre devamında yer alan // anahtarından sonra bankanın dekont/belge numarası gönderimi sistem tarafından tespit edilerek entegrasyon sürecinde oluşacak kayıtlarda belge numarası alanına taşınabilecektir.
Tarih: 6 karakter (yıl/ay/gün)
Giriş Tarihi: 4 karakter (ay/gün) zorunlu bir alan değildir.
Borç/Alacak: 1 karakter Döviz cinsi (Son harfi): 1 karakter Tutar: 15 karakter
İşlem kodu: 4 karakter (Başlangıç karakteri(1) + İşlem kodu (3))
NONREF: Bölüm sonu belirteci
**:86:** :61: satırında yapılmış olan hareketin açıklaması yer almaktadır.
**:62F:** Hesap ile ilgili borç/alacak bilgisi, tarih, döviz-cinsi ve o günkü kapanış bakiyesi yer almaktadır.
: 15 karakterKapanış bakiyesi: 3 karakterDöviz cinsi: 6 karakter (yıl/ay/gün)Tarih: 1 karakterBorç/Alacak
