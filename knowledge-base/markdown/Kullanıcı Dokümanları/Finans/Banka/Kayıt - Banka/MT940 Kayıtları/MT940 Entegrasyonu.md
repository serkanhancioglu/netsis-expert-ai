---
title: "MT940 Entegrasyonu"
page_id: "22806255"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Banka"
  - "Kayıt / Banka"
  - "MT940 Kayıtları"
  - "MT940 Entegrasyonu"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Banka / Kayıt / Banka / MT940 Kayıtları / MT940 Entegrasyonu"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTI3YmQyZGM1LTNhMjQtNDM4YS05MTc4LTQ2ZTg4NmRkZDA3NyZsaW5rPTQ5ZDYxMzBkLTU4OTAtNGRiMS05YjY4LWVmMGFiNTQyZjg1ZSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=27bd2dc5-3a24-438a-9178-46e886ddd077&link=49d6130d-5890-4db1-9b68-ef0ab542f85e&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "mt940-entegrasyonu_34221653_22806255.html"
source_version: "2022-12-02T14:57:52.337+03:00"
source_bytes: 655391
fetched_at: "2026-09-13T04:10:05+00:00"
generator: "netsis-scraper 1.0.0"
---
# MT940 Entegrasyonu

Finans Bölümü'nde, "Kayıt/Banka" menüsünün altında yer alır. MT940 Entegrasyonu, bankadan alınan metin içerikli (TXT uzantılı) dosyanın sisteme entegrasyonunun yapılması için kullanılan bölümdür. MT940 Entegrasyonu; Kısıtlar ve Transfer Bilgileri olmak üzere iki sekmeden oluşur.

**Kısıtlar**

![](../../../../../_assets/be527cd322e9f0d2b028.png)

MT940 Entegrasyonu ekranı Kısıtlar sekmesinde yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| Banka Entegrasyonu Ekranı |  |
| --- | --- |
| Dosya Adı | Banka entegrasyonu için dosya adı girilen alandır. Bankadan alınan MT940 desenindeki dosya, dizin adresi ile seçilebilir. Dosya seç ![](../../../../../_assets/2371f29deb9fb9434ca2.png) butonu ile, kaydedilen dosyalar arasından seçim yapılır. |
| Dosya İçeriği | Dosya seçimi sonrası, içeriğin görüntülendiği alandır. |
| ![](../../../../../_assets/05fc97239146be1676ad.png) Kontrol | Dosya içeriğinin ayrıştırılıp, tespit edilen bilgiler ile hesap hareketlerinin görüntülenmesini sağlayan butondur. Butona tıklandığında MT940 dosyası ilk defa okunuyorsa, kullanıcının mevcut kontör sayısından kontör düşer. Tekrar eden okumalarda kontör sayısı değişmez. |
| ![](../../../../../_assets/3745280670b101ce5af6.png) Mevcut Kayıtları | Kontrol işlemi yapılmaksızın daha önce görüntülenen ve düzeltilen hesap hareketleri bölümüne geçmek için kullanılan butondur. |

**Transfer Bilgileri**

![](../../../../../_assets/8933ec30ca546a810235.png)

Ekranda görüntülenen hesap hareketlerine dair güncelleme yapılabilir.

Program tarafından "İşlem Kodları ve Kuralları Eşleştirme" bölümünde tanımlanan bilgiler kullanılarak hesap hareketi ile eşleşen kural tespit edilir ve oluşacak belge içerikleri listelenir.

Kural tespitinde işleyiş şu sıralamaya göre yapılır; işlem kodu ve borç/alacak durumuna bağlı olarak bulunan kurallar içerisinde, metin alanı ve hesap hareket açıklamasında bulunan, işlem kodu ve borç/alacak durumuna bağlı olarak bulunan kurallar içerisinde, varsayılan kural olarak seçilen, işlem kodu ve borç/alacak durumuna bağlı olarak bulunan tek kural.
Yukarıda belirtilen öncelikler ile ilgili hesap hareketi için uygun bir kural mevcut ise, bu bilgi sistem tarafından otomatik olarak tespit edilip kullanıcıya sunulur.

Kural kodu ve detayları kullanıcı tarafından değiştirilebilir.

MT940 Entegrasyonu ekranı Transfer Bilgileri sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Banka Entegrasyonu Ekranı |  |
| --- | --- |
| ![](../../../../../_assets/b191e8b10c4fed8f91a3.png) Kural Kaydet | Aynı ekran üzerindeki hesap hareketlerinde, ilgili işlem kodunun ilk defa kullanılması gibi sebeplerden dolayı, uygun bir kuralın sistem tarafından tespit edilemediği durumlarda, kullanıcı açıklama, işlem tipi ve kod rehberi yardımı ile kod bilgilerinin oluşturulup kısa yol yardımı ile yeni bir kuralın tanımlanmasını sağlayan butondur. ![](../../../../../_assets/e41a56bc54fbd4bdd08b.png) Bu bölümde yapılan kayıt işlemi ile, kural tanımlama ve eşleştirme bölümleri ile ilgili kayıtlar sistem tarafından otomatik olarak oluşturulur. |
| ![](../../../../../_assets/b2508ce7f935f040d0f0.png) Bilgileri Kaydet | Düzeltme çalışmasının tamamlanmadığı durumlarda, belgeleri oluşturmadan ekrandaki bilgilerin kaydedilmesini sağlayan butondur. |
| ![](../../../../../_assets/724487e4922bc4275f2b.png) Geri | "Kısıtlar" sekmesine geri dönmek için kullanılan butondur. |
| ![](../../../../../_assets/0e218b8c2bd13392f4b1.png) Hepsini Aktar | Hepsini aktar butonu ile, bankadan alınan hesap hareketleri için kural ve hesap hareket açıklama bilgileri kullanılarak sistem üzerinde belirlenen belge tiplerine uygun kayıtlar oluşturulur. Sistem genelinde yapılan tanımlamalara göre oluşacak belgelerde kullanılması için gereken eksik bilgiler kullanıcıdan alınır. ![](../../../../../_assets/87c2fc6457f31d4c69fd.png) İşlem sırasında hareket bazında gerekli kontroller yapıldıktan sonra, sorun olmaması durumunda entegrasyon işlemi tamamlanır. Belge tipi "Genel Dekont" olan kayıtlar için kalem bazlı Proje Kodu, Seri Kodu ve Referans Kodu girişi yapılır. Aktarım sırasında açılan "Gerekli Belge Bilgileri" ekranı üzerinden Referans Kodu girişi yapılabilir. |
