---
title: "Banka Modülü Yenilikleri"
page_id: "50680033"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Banka Modülü Yenilikleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Banka Modülü Yenilikleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWM1MmMxNGJhLTBiMWEtNDIxYi1iYTAwLTZiNDNmOGIxYmJhOCZsaW5rPTc3ZDY2ZGUyLTkxZTAtNDg1OS04YTllLWZmZDQyOTU4Yjc3ZSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=c52c14ba-0b1a-421b-ba00-6b43f8b1bba8&link=77d66de2-91e0-4859-8a9e-ffd42958b77e&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "banka-modulu-yenilikleri_82576416_50680033.html"
source_version: "2022-11-03T09:40:34.497+03:00"
source_bytes: 5532227
fetched_at: "2026-09-13T04:26:10+00:00"
generator: "netsis-scraper 1.0.0"
---
# Banka Modülü Yenilikleri

Banka Modülü Yenilikleri ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

|  |  |
| --- | --- |
| Amaç ve Fayda | Netsis ERP paketlerinde, banka entegrasyonları ile ilgili aşağıdaki yenilikler kullanıma sunulmuştur: - MT940 (Uluslararası standart hesap mutabakatı formatı) Entegrasyonu<br>- TÖS (Toplu Ödeme Sistemi)<br>- DBS (Doğrudan Borçlanma Sistemi)<br>- Çek/Senet Entegrasyonu |
| Ürün Grubu | \[X\] Netsis Enterprise<br>\[X\] Netsis Standard<br>\[X\] Netsis Entegre |
| Modül | \[X\] Banka |
| Kategori | \[X\] Yeni Fonksiyon |
| Versiyon Önkoşulu | 7.0.4 |

**Kurum** **Kodları**
Bankalarla ilgili toplu ödeme, doğrudan borçlandırma ve çek tahsilat süreçlerinde kullanılacak kurum kod bilgileri Kurum Kodları bölümde tanımlanacaktır. Kurum Kodları ekranına Banka modülünde T.C.M.B kayıtları bölümünden Banka kurum bilgileri üzerinden erişim sağlayabilirsiniz.
![](../_assets/36aa05885c64698bc241.png)

![](../_assets/5f24feeccd96d3beeab1.png)![](../_assets/f23bbf2ab3f85a588c13.png)

#### SWIFT MT940 Elektronik Hesap Özeti Entegrasyonu

MT940, uluslararası standartlarda belirlenmiş elektronik hesap ekstresi formatıdır. Bankalardan firmanıza alınan ve hesaplarınızda oluşan hareketleri içeren bu dosyanın Netsis ERP sistemine entegrasyonu sağlanmıştır.
Bankadan MT940 formatında aldığınız hesap hareketleri ile sisteminizde otomatik olarak cari, banka, muhasebe ve çek ile ilgili kayıtlarının oluşturulması sağlanabilmektedir.
Entegrasyon süreci ile ilgili kullanım bilgilerinin tanımlanmasına yönelik ekranlara Banka modülünde Kayıt bölümü MT940 Kayıtları içerisinden erişim sağlayabilirsiniz.
![](../_assets/9f6e876377dd596dcc4f.png)![](../_assets/dbbb93244255874d98db.png)

#### İşlem Kodları

Banka hesap hareketine ait işlem kodları bu bölümde tanımlanabilecektir. Sistem üzerinde standart işlem kodları otomatik olarak oluşturulmaktadır. Mevcut işlem kodları dışında çalışılan banka tarafında desteklenen ek işlem kod kayıtları da bu bölümde yapılabilecektir. Desteklenen standart işlem kodları tanımlamaları ile ilgili detay bilgi için bakınız Ek-1 (MT940 Standart İşlem Kodları).
![](../_assets/c2c4789281d5ffca1198.png)

#### Kural Bilgileri

Banka hesap hareketlerinizin entegrasyon sürecinde Netsis ERP sisteminde çeşitli belgeler oluşturulabilecektir. MT940 satırlarında yer alan bilgi kalıpları doğrultusunda hangi belgelerin oluşturulacağının belirlenmesi ve sistemde ilişkili oldukları Cari-Muhasebe-Banka-Çek bağlantılarının tespitine yönelik tanımlamalar bu bölümde yapılabilecektir.
**Metin:** Bu alanda yer alan bilgi sistem tarafından bankadan alınan dosyanın hesap hareket satırları içinde metinsel olarak aranarak ilişkili kural tespiti sağlanacaktır. Yani tanımlanacak kural, tanımlanan metnin içinde geçtiği satırlar için çalışacaktır.
**Belge** **Tipi:** İlgili satır için sistemde hangi tip belgenin oluşturulacağıdır. Belge Tipi olarak oluşturulabilecek belgeler; Genel Dekont, Havale/EFT/Bankalar Arası Virman, Çek Tahsil, Çek Ödendi, Senet Tahsil, Senet Ödendi, Bankadan Gelen Karşılıksız Çek, Bankadan Gelen Protestolu Senet, İade Çek, İade Senet.

**Cari-Banka-Çek/Senet-Muhasebe Kodları:** İlgili satırın ilgili belgede hangi varlık (cari hesap, banka hesabı, muhasebe hesabı, çek ya da senet) ile ilişkilendireceği ve bu varlığın sistemdeki kodunun karşılığı belirtilebilir.
Banka modülünde Kayıt bölümü MT940 Kayıtları menüsünün altından ulaşılabilecek bu adımda, bankadan alınan metinsel (txt uzantılı) dosyanın sisteme entegrasyon süreci bu bölümde yapılabilmektedir. **Banka** **Entegrasyonu** **(SWIFT** \*MT940)\*MT940 dosyasında yer alan işlem kodlarının yukarıdaki hangi kurallarla eşleşeceğinin tanımlandığı bölümdür. Bir işlem kodu birden fazla kuralla eşleştirilerek opsiyonel olarak ilgili kuralda tanımlanan belgenin oluşması ve ilgili hesabın işlem görmesi sağlanabilir.

#### İşlem Kodları ve Kuralları Eşleştirme

![](../_assets/15591aa223710b87d5d1.png)![](../_assets/0b0db43af85a6375d9d3.png)
**Dosya Adı:** Bankadan alınan MT940 desenindeki dosya, dizin adresi ile seçilebilecektir. Seçim sonrasında dosya içeriği alt bölümde görüntülenecektir.
**Kontrol:** Kontrol işlemi ile dosya içeriği ayrıştırılıp; tespit edilen bilgiler ile hesap hareketleri görüntülenecektir. Kontrol işlemi yapılmaksızın daha önce görüntülenmiş ve düzeltilmiş hesap hareketleri bölümüne geçmek için mevcut kayıtlar seçeneği kullanılabilir.
İşlem Kodları ve Kural Eşleştirme bölümünde, görüntülenen hesap hareketlerine dair bilgiler üzerinde güncelleme yapılabilecektir.
Sistem tarafından işlem kodları ve kuralları eşleştirme bölümünde tanımlanmış bilgiler kullanılarak hesap hareketi ile eşleşen kural tespit edilecek ve oluşacak belge içerikleri listelenecektir. Kural tespitinde işleyiş önceliklendirmesi aşağıda belirtildiği sıradadır (Bir önceki adımda kural tespit edilememesi durumunda sonraki adım işletilmektedir):

- İşlem kodu ve borç/alacak durumuna bağlı olarak bulunan kurallar içerisinde metin alanı, hesap hareket açıklamasında bulunan.
- İşlem kodu ve borç/alacak durumuna bağlı olarak bulunan kurallar içerisinde varsayılan kural olarak seçilen 3- İşlem kodu ve borç/alacak durumuna bağlı olarak bulunan tek kural.

Yukarıda belirtilen öncelikler ile ilgili hesap hareketi için uygun bir kural mevcut ise bu bilgi sistem tarafından otomatik olarak tespit edilip kullanıcıya sunulacaktır. Bununla birlikte kural kodu ve detayları kullanıcı tarafından değiştirilebilecektir.

#### Kural Kaydet

Aynı ekran üzerinde hesap hareketlerinde ilgili işlem kodunun ilk defa kullanılması, vs. sebeplerden ötürü uygun bir kuralın sistem tarafından tespit edilememesi durumunda kullanıcı açıklama, işlem tipi ve kod rehberi yardımı ile kod bilgilerini oluşturup kısayol yardımı ile yeni bir kural tanımlayabilecektir.
Bu bölümde yapılan kayıt işlemi ile sistem tarafından kural tanımlama ve eşleştirme bölümlerine dair kayıtlar, otomatik olarak oluşturulacaktır.

#### Geri

Kısıtlar sekmesine geri döner

#### Bilgileri Kaydet

Bu ekranda yapılan düzeltme çalışması tamamlanmadığı durumda, belgeleri oluşturmaksızın ekrandaki bilgileri kaydeder.

#### Hepsini Aktar

Hepsini aktar işlemi ile bankadan alınan hesap hareketleri için kural ve hesap hareket açıklama bilgileri kullanılarak sistem üzerinde belirlenen belge tiplerine uygun kayıtlar oluşturulacaktır. Sistem genelinde yapılan tanımlamalara göre oluşacak belgelerde kullanılmak üzere eksik bilgiler, kullanıcıdan alınacaktır.
![](../_assets/0b5501596ef748cef5d1.png)![](../_assets/817311a882589aac7792.png)
İşlem esnasında hareket bazında gerekli kontroller yapılıp; sorun olmaması durumunda entegrasyon işlemi tamamlanacaktır.

#### Toplu Ödeme Sistemi

Toplu ödeme sistemi (TÖS), satıcı firmalara yapılacak ödeme bilgilerinin bankaya elektronik olarak aktarımı sistemidir. Netsis ERP sistemi içinde satıcılara havale/eft ile yapılacak ödemeler, Cari Hesap Modülü/Ödeme Emri Oluşturma adımından hazırlanarak, Ödeme Emirleri Listesi adımından çeşitli bankalara göre text formatında alınarak iletilebilmektedir.

#### Ödeme Emri Akıbetleri

Ödeme emirleri, TÖS öncesinde bankaya iletildikten sonra herhangi bir akıbet bilgisi sorgulanmadan sistemde Ödeme Emri Entegrasyonu adımından entegre edilebiliyordu. TÖS ile birlikte firmanızın bankaya göndermiş olduğu ödeme talimatlarının akibetlerini sorgulayabileceksiniz. İlgili ekrana Cari modülünde İşlemler bölümü Ödeme Emirleri içerisinde Ödeme Emri Akibetleri seçimi ile erişim sağlayabilirsiniz. Banka hesap kodu belirtildikten sonra bankadan alınan akibet dosyası seçilerek işlem başlatılacaktır. Dosya içeriği incelenerek ekrana ilgili ödeme emirlerinin banka tarafında gördüğü işlem neticeleri görüntülenecektir. Entegrasyon işlemi ile görüntülenen ve tahsil edilemeyen ödemelerin durumları onaysız hale getirilecektir.
![](../_assets/d9fd4dcd1f110a298769.png)

Tamamlanmış ödemeler için ise, açılan entegrasyon penceresi ile işlemler tamamlanabilecektir.

#### Doğrudan Borçlandırma Sistemi

Doğrudan borçlandırma sistemi ile firmanızın müşterilerine/bayilerine yapmış olduğu satışların tahsilat işlemleri pratik bir şekilde yürütülebilecektir. Sistem tarafından oluşturulan talimatların bankaya iletilmesinin ardından banka tarafında tahsilatlar takip edilecek ve otomatik olarak Netsis ERP sistemine yansıtılabilecektir. Tahsilatlar, Netsis'te oluşan dekontlar yardımı ile kontrol edilebilecektir. Benzer şekilde olumlu-olumsuz tahsilat işlem sonuçları da izlenebilecektir.
Doğrudan borçlandırma sistemi ile ilgili ekranlara Banka modülünde İşlemler bölümü üzerinden erişim sağlayabilirsiniz.

#### Fatura Aktarımı

Firma tarafından sistem aracılığıyla bankaya iletilecek fatura bilgileri bu bölümden oluşturulmaktadır. Sorgulama seçenekleri kullanılarak daha önce bankaya aktarılmayan (tahsilat adayı) fatura listeleri görüntülenebilecektir. Görüntülenen faturalar içerisinde tahsilat sürecine dahil edilmek istenen faturalar seçilecektir. Ekran üzerinde işlemi kolaylaştırmaya yönelik bazı fonksiyonlar (tümünü seç-seçimleri kaldır) yer almaktadır. Seçilen faturaları içeren tahsilat dosyasının oluşturulması için dosya oluştur seçeneği seçilmelidir. Sonrasında dosyanın kaydedileceği yer belirtilerek oluşan dosya, bankaya iletilebilecektir.
![](../_assets/9552a47799cae0ab3ad9.png)

#### Fatura Bilgileri

Bankaya iletilen fatura bilgileri bu bölümden izlenebilecektir. Sorgulama seçenekleri kullanılarak daha önce bankaya aktarılan fatura listeleri görüntülenebilecektir. Görüntülenen liste içerisinde banka gönderimi iptal edilmek istenen faturalarda değişiklik yapılabilecektir.

#### Fatura Akıbetleri

Tahsilat akıbetleri, Fatura Akıbetleri bölümünden kontrol edilebilecektir. Bankadan alınan akıbet dosyası seçilerek işlem başlatılacaktır.

Dosya içeriği incelenerek ekrana ilgili faturaların banka tarafında gördüğü işlem neticeleri görüntülenecektir. Dosya kontrol sürecinde tespit edilen durumlar kullanıcı bilgilendirme ekranında görüntülenecektir.
![](../_assets/b609b6e5064d870ec3d8.png)

Entegrasyon işlemi ile görüntülenen ve başarılı şekilde tahsil edilen faturalar için sistemde dekont oluşturulacaktır.

#### Limit Risk Yönetimi

Banka tarafında takibi yapılan ve müşterilere/bayilere ait limit-kredi detayları sisteme entegre edilecek ve yine bu bölümden incelenebilecektir. Limit Risk Akıbetleri bölümü yardımıyla bankadan alınan dosya seçilip; limit-risk dosyası sisteme entegre edilerek sistemdeki carilere ait limit-risk detaylarının güncellenmesi sağlanacaktır. Entegrasyon süreci banka abone numarası üzerinden yürütülmektedir. Abone numarası bilgisi, cari kartı KULL5S alanında tutulmaktadır.
![](../_assets/2312d3a5dd70f4791fde.png)
Limit Risk Kayıtları bölümü yardımıyla bankadan alınan limit-risk cari kısıt yardımıyla incelenebilecektir. Risk oran hesaplaması ile ilgili cariler de tespit edilebilecektir.

#### Çek/Senet Tahsilat Sistemi

Çek/Senet tahsilat sistemi ile, firmanızın müşteri çekleri/senetleri tahsilat işlemleri banka ile kurulacak entegrasyon kapsamında pratik bir şekilde yürütülebilecektir. Çek/Senet bilgilerinin bankaya aktarımı, bankadan alınan tahsilat akıbetlerinin izlenmesi ve sisteme entegrasyonu işlemlerinin yapılabilmesini sağlayacak bu yenilik, Netsis 7.0.4 onaylı sürümü ile birlikte kullanılabilir. Çek/Senet tahsilat sistemi ile ilgili ekranlara Banka modülünde İşlemler bölümü üzerinden erişim sağlayabilirsiniz.
![](../_assets/c478d5a8c0a1824811c7.png)![](../_assets/28e9ef276f625c8be415.png)

#### Çek/Senet Aktarımı

Firma tarafından sistem aracılığıyla bankaya iletilecek çek/senet bilgileri bu bölümden oluşturulmaktadır. Görüntülenen çekler/senetler içerisinde tahsilat sürecine dahil edilmek istenenler seçilecektir. Ekran üzerinde işlemi kolaylaştırmaya yönelik bazı fonksiyonlar (tümünü seç-seçimleri kaldır) yer almaktadır. Seçilen çekleri/senetleri içeren tahsilat dosyasının oluşturulması için dosya oluştur seçeneği kullanılmalıdır. Sonrasında dosyanın kaydedileceği yer belirtilerek oluşan dosya, bankaya iletilebilecektir.

#### Çek/Senet Bilgileri

Bankaya iletilen çek/senet bilgileri bu bölümden izlenebilecektir. Sorgulama seçenekleri kullanılarak daha önce bankaya aktarılan çek/senet listeleri görüntülenebilecektir. Görüntülenen liste içerisinde banka gönderimi iptal edilmek istenen çek veya senetlerde değişiklik yapılabilecektir.
![](../_assets/e80c767e0f499c05c8a0.png)![](../_assets/e1b75327504052142c95.png)

#### Çek/Senet Akıbetleri

Çek/senet tahsilatlarının akıbetleri bu bölümden kontrol edilebilecektir. Bankadan alınan akıbet dosyası seçilerek işlem başlatılacaktır. Dosya içeriği incelenerek ekrana ilgili çek/senetlerin banka tarafında gördüğü işlem neticeleri görüntülenecektir. Entegrasyon işlemi ile görüntülenen ve başarılı şekilde tahsil edilen çek/senetler için sistemde entegrasyon kayıtları oluşturulacaktır. Dosya kontrol sürecinde tespit edilen durumlar kullanıcı bilgilendirme ekranında görüntülenecektir.

Not: Ödeme emri akıbeti (TÖS), doğrudan borçlandırma sistemi ve çek/senet işlemleri bölümlerinde halihazırda Vakıfbank banka desenleri desteklenmiştir. Farklı banka desenleri ileri
sürümlerimizde desteklenecektir.

#### EKLER

Ek-1 (MT940 Standart İşlem Kodları) aşağıdaki şekildedir:

| İŞLEM | B/A | AÇIKLAMA |
| --- | --- | --- |
| BOE | + | Senet tahsilatı / Bill of exchange |
| BOE | - | Senet ödemesi / Bill of exchange |
| CHG | + | Banka masrafları (ters işlem) / Charges and other expenses |
| CHG | - | Banka masrafları / Charges and other expenses |
| CHK | + | Çek tahsilatı / Cheques Collection |
| CHK | - | Çek ödemesi / Cheques Collection |
| COM | + | Teminat mektubu komisyonu (ters işlem ) / Letter of Credit Commission |
| COM | - | Teminat mektubu komisyonu / Letter of Credit Commission |
| EFT | + | Gelen EFT / Incoming EFT |
| EFT | - | Çıkan EFT / Outgoing EFT |
| EXP | + | ihracat tahsilatı / Export |
| EXP | - | ihracat tahsilatı (ters işlem )/ Export |
| FEX | + | Döviz satışı / Foreign Exchange (Versiyon 2 olabilir) |
| FEX | - | Döviz alışı / Foreign Exchange (Versiyon 2 olabilir) |
| FND | + | Stopaj üzerinden fon kesintisi (ters işlem ) / Fund Reduction (over Stopaj) |
| FND | - | Stopaj üzerinden fon kesintisi / Fund Reduction (over Stopaj) |
| IMC | + | ithalat masrafı (ters işlem ) / Import Commission |
| IMC | - | ithalat masrafı / Import Commission |
| IMP | + | ithalat ödemesi (ters işlem ) |
| IMP | - | ithalat ödemesi / Import |
| MSC | + | Diğer işlemler / Miscellaneous |
| MSC | - | Diğer işlemler / Miscellaneous |
| PRO | + | Karşılıksız senet protesto masrafı (ters işlem ) / Expenses for protested bills |
| PRO | - | Karşılıksız senet protesto masrafı / Expenses for protested Bills |
| TRF | + | Gelen havale / Incoming Fund Transfer (TL) |
| TRF | - | Satıcı hesabına gönderilen havale ve EFT ler / Outgoing Fund Transfer (TL) |
