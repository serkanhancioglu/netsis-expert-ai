---
title: "Netsis MT940 Entegrasyonu Sıkça Sorulan Sorular"
page_id: "50684985"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis MT940 Entegrasyonu Sıkça Sorulan Sorular"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis MT940 Entegrasyonu Sıkça Sorulan Sorular"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTAwY2ViMTNiLTBjYTgtNDZkNC04OGMwLTQ2ZWJiNTZjYWVlMCZsaW5rPTBmM2NkMjY3LTM4YWMtNDMyMy1iODdkLTViNDg5YjU3MTNiNyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=00ceb13b-0ca8-46d4-88c0-46ebb56caee0&link=0f3cd267-38ac-4323-b87d-5b489b5713b7&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-mt940-entegrasyonu-sikca-sorulan-sorular_80090628_50684985.html"
source_version: "2022-12-09T14:48:04.967+03:00"
source_bytes: 254112
fetched_at: "2026-09-13T04:25:21+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis MT940 Entegrasyonu Sıkça Sorulan Sorular

**MT940** **dosyasının** **geldiği** **banka** **hesabı** **Netsis'te** **nasıl** **tanımlanır?**

MT940 dosyasında 25 numaralı satırda yer alan banka hesabının netsis içinde tanımlanması gerekir. Netsis içerisinde bu hesabın tanımlanabilmesi için sırasıyla Banka Ana Kod Kayıtları, Banka Şube Kayıtları ve Banka Hesap Kayıtlarının tanımlanması gerekmektedir.

**Banka** **Ana** **Kod** **Kayıtları** ekranında banka ana kod, banka ismi tanımlaması sonrasında dosyada yer alan "**0111**" değerini TCMB Banka Ana Kod alanına girilerek kaydedilir.

![](../_assets/ce7678551ee429632e6d.png)

Banka Şube Kayıtları ekranında banka ana kod, banka şube kodu, banka şube ismi tanımlaması sonrasında dosyada yer alan "**00452**" değerini Banka Şube Kodu alanına girilerek kaydedilir.

![](../_assets/b665479eabfb7041b33f.png)

Banka Hesap Kayıtları ekranında, hesap kodu, ana kod, şube kodu, banka hesap ismi tanımlaması sonrasında dosyada yer alan "**23373473**" değerini Banka Hesap No alanına girilerek kaydedilir.

![](../_assets/24379e84939f2537d8df.png)

**MT940** **dosyasındaki** **işlem** **kodları** **bazında çalışma** **tipleri** **(b/a)** **nasıl** **belirlenir?**

:61:151007**C**T0000000005523,50N**MSC**NONREF//
:61:151007**D**T0000000028250,00N**EFT**NONREF//

MT940 dosyası içinde 61 numaralı satırlarda geçen işlem kodlarına göre Borç (D-Debit) / Alacak (C- Credit) çalışacağı anlaşılır. Yukarıda örnek 61 numaralı satırlara göre MSC işlem tipindeki hareketin Alacak, EFT işlem tipindeki hareketin Borç olarak çalışacağı anlaşılır.

**MT940 entegrasyonu sonrasında aktarılan kayıtlarda herhangi bir sorun olması** **durumunda** **ne yapılmalıdır?**

MT940 entegrasyonu sonrasında, aktarılan kayıtlarda herhangi bir sorun olması durumunda, aktarılan kayıtlar netsisten manuel olarak temizlendikten sonra, gerekli düzenlemeler sonrasında tekrar bu kayıtların aktarılabilmesi için, yeniden aktarılacak kayıt satırları için ekrandaki "Aktarıldı" parametresi kaldırılıp "Bilgileri Kaydet" dendikten sonra grid ekranda durum kısmı "Aktarılmadı" ya döner ve aktarım tekrarlanır.

**MT940 Entegrasyonu sırasında kontrol işlemi sonrası "can not open data** **connection** **for** **transfer** **/" uyarı** **mesajı alınırsa** **ne yapmalıyım?**

Dosya seçimi sonrası bu uyarı mesajı alındığında, dosyanın geldiği bankaya ait tanımlamalarda sorun var demektir. Özellikle banka hesap bilgileri kısmında girilen banka hesap numarası kontrol edilmelidir.

**MT940** **banka** **dosyasında** **yeni** **bir** **işlem** **kodu** **geldiğinde ne** **yapılmalıdır?**

Program tarafından desteklenen işlemler, otomatik olarak tanımlı gelir. Yeni bir işlem kodu tanımlaması İşlem Kodları ekranı üzerinden yapılmaz. Yeni bir işlem kodu olması durumunda destek departmanları ile iletişime geçilmelidir.

**Tanımlanan kuralların şirketin tüm şubelerinde çalışması isteniyorsa ne** **yapılmalıdır?**

Kural bilgileri ekranında ilgili kural tanımlaması için şube kodu kısmına "-1" girilerek kaydedilmelidir.

**MT940 Entegrasyonunun çalışabilmesi için Logo Connect ek modülü gerekli** **midir?**

MT940 Entegrasyonunun dizin veya ftp yönteminde çalışması için, Logo Connect ek modülü gerekmektedir. Lisansta bu modül olduğunda MT940 parametreleri ekranında "Web Servis Parametreleri" sekmesi gelmektedir.

Elogo portalına giriş yapılabilen geçerli bir kullanıcı adı ve şifre bilgisi girilmelidir. Servis ile kontör harcama işlemleri yapılıyor. e-Logo dan bir dosya indirilmiyor. Servis ile iletişim kurulup kontör harcanıyor ve kontör bilgileri görüntülenebiliyor.

![](../_assets/4de45e3337d00ad62e10.png) **Soru 8: MT940 Entegrasyon****edilmesi hata ile karşılaşıldı. Hata Detayı: Kontrol esnasında hata ile karşılaşıldı. Hata**

**Detayı:** **Invalid** **argument** **to** **date** **encode"** **uyarı** **mesajı** **alınırsa ne** **yapmalıyım?**

MT940 dosyasındaki tarih bilgilerinin formatı nedeniyle hata alınmaktadır. Tarih formatı yıl ay gün formatında olup 6 karakterden oluşmaktadır. Hata alınmaması için 60F, 61, 62 numara ile başlayan satırlarda tarih formatı düzenlemesi yapılabilir.
