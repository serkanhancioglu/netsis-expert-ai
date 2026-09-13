---
title: "Kredi Kartı"
page_id: "22806376"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Banka"
  - "Ekler / Banka"
  - "Kredi Kartı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Banka / Ekler / Banka / Kredi Kartı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTZkYmVkMDk2LTM2NjUtNDRiMy04MTRkLTUzNjMxMzJmNTViZCZsaW5rPTgxYWJmMTY0LTBkMTItNDUwNi1hM2FlLThmODg1NTk3ZThlOCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=6dbed096-3665-44b3-814d-5363132f55bd&link=81abf164-0d12-4506-a3ae-8f885597e8e8&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "kredi-karti_34224661_22806376.html"
source_version: "2022-12-05T17:03:16.187+03:00"
source_bytes: 22788
fetched_at: "2026-09-13T04:10:41+00:00"
generator: "netsis-scraper 1.0.0"
---
# Kredi Kartı

Kredi Kartı ile ilgili ayrıntılı bilgiye bu dokümandan ulaşılır.

**Kredi Kartı Banka Hesabının Tanımlanması**

Kredi kartları için ayrı banka hesapları tanımlanır. Kredi kartı hesapları, hesap tiplerine eklenen “Kredi Kartı Hesabı” seçilerek tanımlanır.

Tipi "Kredi Kartı Hesabı" olarak seçildiğinde, "Bağlantılı Hesap Kodu" alanı aktif hale gelir. Bu alana, bir banka hesabı girilmeden yapılan kaydın tamamlanmasına izin verilmez. Bağlı hesap kodu, kredi kartı tahsilat işlemi sonucu, banka tarafından ödenen tutarın kaydedileceği hesaptır. Bağlı hesap kodu olarak vadesiz mevduat hesapları seçilebilir.

Banka tarafından yapılan ödeme ile kredi kartı tahsilat kayıtlarında hesaplanan ödeme rakamının farklı olması durumunda; elle (manuel) müdahaleye izin verilir ve hesaplanan değer ile düzenlenen değer arasındaki fark, bu hesaplara aktarılır.

#### Fatura Modülünde Kredi Kartı Uygulamaları

Kredi kartı ile yapılan bir alışverişin faturası kaydedilirken, kredi kartı ile ilgili tahsilat bilgilerinin de girilmesini sağlayan uygulamadır. Kapalı kesilen faturada parametrik olarak açılan "Hızlı Tahsilat Kayıtları" ekranında tahsilat bilgileri girilip aynı anda Banka ve Kasa Modülüne, parametrik olarak da Entegrasyon ve Cari Modülüne kayıt yapılması sağlanır.

Kapalı tipli kesilen faturada "Hızlı Tahsilat Kayıtları" ekranının açılması için; Fatura → Kayıt → [Satış Parametreleri](<../../../Lojistik - Satış/Fatura/Kayıt - Fatura/Satış Parametreleri.md>) → Genel 3 → "Kapalı Faturada Tahsilat Ekranı Çıksın” parametresinin işaretlenmesi gerekir.

**Hızlı Tahsilat Kayıtları**

Kapalı kesilen satış faturasında, "Toplamlar" sekmesinde yer alan Tamam ![](../../../../_assets/39d77b8716226638d9ce.jpg) butonuna basıldıktan sonra "Hızlı Tahsilat Kayıtları" ekranı açılır. Bu ekran; bir kısmı nakit, bir kısmı kredi kartı ile, tamamı kredi kartı ya da tamamı nakit olan ödemelerde kullanılır.

#### Cari Kodu

Bilgi amaçlı olarak faturanın "Üst Bilgiler" sekmesinde seçilen cari kodu bu alanda izlenir.

#### Belge No

Faturanın belge numarasının izlendiği alandır.

#### Tahsilat Şekli

Yapılan alışverişte hangi sözleşmenin kullanılacağı ile ilgili seçim yapılan alandır. Tahsilat şekli rehberinde, "Banka Sözleşme Tanımlamaları" bölümünde kaydedilen kayıtlar listelenir. Tahsilat şekli boş bırakıldığında, fatura toplamının bir kısmının ya da tamamının nakit olarak ödeneceği anlaşılır ve "Tahsil Şekli" alanına “Nakit” değeri aktarılır.

#### Taksit Sayısı

Satışın kaç taksitli olacağının belirlendiği alandır. Müşterinin ödeyeceği taksit sayısı girilir.

**Örneğin:** Bu sahaya 4 rakamı yazıldığında, müşterinin bankaya 4 taksitte ödeme yapacağı, bankanın da firma ile yapılan sözleşmede 4 taksitli satış için belirlenen koşullarda ödeme yapacağı anlaşılır.

#### Kart Numarası

Müşterinin kullandığı kredi kartının 16 haneli numarasının girildiği alandır. Bu saha boş bırakılmaz.16 karakterden eksik ya da fazla girilemez.

#### Tutar

Müşterinin ödeme tutarının girildiği alandır. Ödemenin bir kısmı nakit, bir kısmı puanla, bir kısmı da taksitlendirilme şeklinde yapılıyorsa, her üç ödeme için ayrı ayrı kayıt girilir.

Girilen tutar toplamının fatura toplamına eşit olması gerekir. Toplam rakam fatura toplamına eşit değilse; Tamam ![](../../../../_assets/39d77b8716226638d9ce.jpg) butonuna basıldığında aşağıdaki şekilde bir uyarı mesajı görüntülenir.

"Girilen kayıtlar kontrol edilip fatura toplamı ile karşılaştırılmalıdır." İptal ![](../../../../_assets/973111d004995dca0113.jpg) butonuna basıldığında ise, "Yapılan kayıtlar yanlış ise düzeltilmeli, doğru ise tamam butonuna basılarak kayıtlar tamamlanmalıdır." şeklinde bir uyarı mesajı görüntülenir. Faturanın tamamı nakit ödense bile, girişin hızlı tahsilat ekranından yapılması gerekir.

#### Hızlı Tahsilat Kaydı Sonucunda Kasa Modülünde Oluşan Kayıtlar

"Hızlı Tahsilat Kaydı" sonucu, kasanın fatura sekmesinde işlemin yapıldığı tarihte toplam tutar kadar gelir kaydı oluşur.

#### Hızlı Tahsilat Kaydı Sonucunda Cari Modülünde Oluşan Kayıtlar

Kapalı tipli faturanın cari hareketlerde de izlenmesi istendiğinde; Fatura → Kayıt → Satış Parametreleri → Genel 3 → “Kapalı Fatura Cari Harekete İşlensin” parametresi işaretlenmesi gerekir.

Bu parametrenin işaretli olduğu durumlarda; fatura kaydı sonrası, cari hareketlere fatura toplamı kadar borç ve alacak kaydı aktarılır.

#### Hızlı Tahsilat Kaydı Sonucunda Banka Modülünde Oluşan Kayıtlar

Kesilen kapalı tipli fatura sonucu, sözleşmede belirtilen banka hesap kodunda taksit tutarları için borç, kesinti tutarları için de alacak hareketleri oluşur. Hareket ya da hareketlerin vadeleri, sözleşmede belirlenen koşullara göre oluşur. "Banka Hesap Hareketleri" bölümünde, kesintilerin tür alanında masraf, bankadan tahsil edilecek olan alacakların tür alanında da virman yazılır.

**Örneğin:**

Alışveriş Tarihi: 27.07.2006

Blokaj: İlave 10 gün

Vade: İlave gün

Ödemelerin bankadan taksitli olarak tahsil edileceği, kesintilerden bir tanesinin ilk tahsilatta diğerinin de vadeli olarak yapılacağı varsayıldığında, iki taksitli olarak kesilen 3599 TL tutarındaki fatura için kayıtlar, kredi kartı hesabında aşağıdaki şekilde oluşur.

Oluşan hareketlerin açıklamalarında cari adı, belge numarası, sözleşme kodu, taksit sayısı ve kesinti kodu görüntülenir. Borç kısmında taksit tutarları için ayrı, alacak kısmında her bir kesinti için ayrı kayıtlar oluşur.

İlk vade; 27/07/2006+10 gün = 07/07/2006 olarak hesaplanır.

Sonraki vade; 07/07/2006+30 gün = 06/08/2006 olarak hesaplanır.

#### Hızlı Tahsilat Kaydı Sonucunda Entegrasyon Modülünde Oluşan Kayıtlar

Entegrasyon modülünde oluşacak kayıtlar iki farklı şekilde olabilir:

- **“Kart Masrafları Satış Anında Entegrasyona Atılsın” parametresinin işaretli olması durumu:** Böyle bir durumda, banka kesinti tanımlamalarında belirtilen "Masraf Muhasebe Kodu" borç, "Tahakkuk Muhasebe Kodu" alacak olacak şekilde, faturanın kaydedildiği sırada çalışır. Bu hesaplar sözleşmede belirtilen koşullara göre taksit sayısı kadar ya da bir defa çalışır. Bunların dışında, yine sözleşme koşullarına göre banka hesap kodunda ve kasa hesap kodunda kayıtlar oluşur. Aşağıdaki örnekte iki taksitle yapılan bir satış kaydı yer alır. Banka ile yapılan sözleşmeye göre, iki taksitli satış için iki ayrı kesinti yapılır ve banka tarafından da ödemeler vadeli olarak işleme alınır. 108 ile başlayan kredi kartının banka hesap kodunda taksit sayısı kadar hareket oluşur. Tahakkuk ve masraf kodları da dörder defa, herbir taksit bazında ayrı ayrı çalışır (birinci taksit için iki kesinti, ikinci taksit için iki kesinti olacak şekilde). Kısaca, masraflar faturanın kesilmesi anında gider kaydedilir.

Kredi kartı tahsilat işlemi çalıştırıldığında, 381 hesaplar borç olarak çalışır. Bu durumda da 780 hesap kesinti tutarı kadar borç bakiyesi verir.

- **“Kart Masrafları Satış Anında Entegrasyona Atılsın” parametresinin işaretli olmaması durumu:** Bu durumda "Masraf Muhasebe Kodu" ve "Tahakkuk Muhasebe Kodu" hesapları faturanın kaydı sırasında çalışmaz (Kredi kartı tahsilat işlemi çalıştırıldığında, masraf muhasebe kodu kesinti tutarları kadar borç çalışır). Sözleşmede belirtilen koşullara göre banka hesap kodunda taksit sayısı kadar ya da tek kayıt oluşur. Aşağıdaki örnekte iki taksitle yapılan bir satış kaydı yer alır. Banka ile yapılan sözleşmeye göre iki taksitli alışveriş için, banka tarafından yapılan ödemeler vadeli olarak işleme alınır. 108 ile başlayan kredi kartının banka hesap kodunda taksit sayısı kadar hareket oluşur. Kesintilerin giderleşmesi, "Kredi Kartı Tahsilat Kayıtları" bölümü yardımı ile gerçekleşeceği için, kesinti tutarları satış anında entegrasyon kayıtlarına yansımaz.

“Kart masrafları entegrasyona toplu atılsın” parametresi, aynı hesap koduna sahip kesintilerin vadelerine göre kümüle edilerek entegrasyona atılmasını ifade eder.

#### Kredi Kartı Tahsilat Kayıtları

Bankaların yaptığı ya da yapacağı ödemelerin tespit edilmesini, banka ve entegrasyon modüllerinde ödeme kayıtlarının oluşmasını sağlayan işlemdir.

#### Vade Başlangıç Tarihi

Hazırlık işleminin çalıştırılacağı vade aralığının başlangıç tarihinin belirlendiği alandır.

#### Vade Bitiş Tarihi

Hazırlık işleminin çalıştırılacağı vade aralığının bitiş tarihinin belirlendiği alandır.

#### Hareket Tarihi

Tahsilatların, banka ve entegrasyon modüllerinde hangi tarihte oluşacağının seçildiği alandır.

#### Şube Kodu

Merkez şubeden girildiğinde aktif olan alandır. Hangi şube için işlem yapılacağı bu alandan seçilir. İşlemin tüm şubeler için çalıştırılması istendiğinde, bu alana -1 değeri girilir.

#### Banka Hesap Kodu

Tahsilat işleminin çalıştırılacağı banka hesap kodunun seçildiği alandır.

#### Kayıtlar Şube Kırılımlı Oluşturulsun

Birden fazla şube için aynı anda tahsilat kaydı yapıldığında, bu parametre işaretlenerek kayıtların şube bazında oluşması sağlanır. Bu parametre, sadece merkez şubeden giriş yapıldığında aktif olarak ekrana gelir.

#### Kayıtlar Proje Kırılımlı Oluşturulsun

Proje uygulamasının açık olması durumunda aktif hale gelen parametredir. Oluşacak tahsilat kayıtlarının proje bazında kırılımlı olarak oluşmasını sağlar.

#### Kayıtlar Plasiyer Kırılımlı Oluşturulsun

Plasiyer uygulamasının açık olması durumunda aktif hale gelen parametredir. Oluşacak tahsilat kayıtlarının plasiyer bazında kırılımlı olarak oluşmasını sağlar.

#### Tutar

Hazırlık işleminden sonra grid ekranda listelen kayıtlardan seçilen kayda ait tutarın görüntülendiği ve düzenlendiği alandır.

#### Kayıt Onay

Hazırlık işleminden sonra grid ekranda listelen kayıtlardan seçilen kayda ait tutarın onaylanıp onaylanmadığının sorgulandığı alandır. Rakam değiştilip onaylı hale getirilebilir.

#### Detay Kısıt

Ekrandaki kısıtlar dışında başka kısıtların da verilmesini sağlayan butondur. Detay kısıt butonuna basıldığında, "İleri Kısıt Tanımlama" ekranı görüntülenir.
