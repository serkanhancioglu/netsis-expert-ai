---
title: "Netsis Rezervasyon Sistemi Sıkça Sorulan Sorular"
page_id: "50684098"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis Rezervasyon Sistemi Sıkça Sorulan Sorular"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis Rezervasyon Sistemi Sıkça Sorulan Sorular"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTc4Yzc4MmRlLWFiMjYtNGRjOS1hNDgwLTQ3ZDBlYjU3YTRhZSZsaW5rPTI3YmVkN2U1LWE5MDctNDRlZi1iM2FhLTZiODRkNWZjNmM3ZCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=78c782de-ab26-4dc9-a480-47d0eb57a4ae&link=27bed7e5-a907-44ef-b3aa-6b84d5fc6c7d&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-rezervasyon-sistemi-sikca-sorulan-sorular_50684103_50684098.html"
source_version: "2020-11-13T14:02:20.383+03:00"
source_bytes: 913420
fetched_at: "2026-09-13T04:26:27+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis Rezervasyon Sistemi Sıkça Sorulan Sorular

**Soru 1: Sipariş bazında rezervasyon sistemi nasıl çalışır?**

Sipariş bazında rezervasyon sistemi ile ihtiyaç çıkarılan malzemeler siparişlere rezerve edilerek, bu ihtiyaçların başka siparişler tarafından kullanımı engellenir.

**Soru 2: Sipariş bazında rezervasyon sisteminin kullanılabilmesi için ne yapılması gereklidir?**

Sistemin aktifleşebilmesi için MRP parametrelerinde *"Sipariş Bazında Rezervasyon* *Sistemi"* parametresi işaretli olmalıdır.

![](../_assets/f61ee689068736012877.png)

**Soru 3: Sipariş bazında rezervasyon sistemi kullanıldığında dengeleme ekranları nasıl çalışacaktır?**

Bu sistem kullanıldığında MRP parametrelerinde iş emri ve satıcı sipariş dengeleme parametreleri otomatik işaretlenir. Böylece dengeleme ekranlarından açılan iş emri ve satıcı siparişlerinin ilgili müşteri siparişine rezervasyonu otomatik gerçekleşir.

**Soru 4: Stokların rezervasyon sistemine dahil olması için yapılması gereken işlem nedir?**

MRP parametrelerinde Genel-2 sekmesinde *"Varsayılan Satıcı Siparişi Planlama Yöntemi"* ve *"Varsayılan İş Emri Planlama Yöntemi"* parametreleri için *"Sipariş Bazında"* seçili olmalıdır. Bununla beraber Stok Planlama Kayıtları ekranında ilgili stoklar için *Satıcı Siparişi Planlama* *Yöntemi* ve *İş Emri Planlama Yöntemi* parametreleri "*Varsayılan"* ya *da* *"Sipariş Bazında"* seçili olmalıdır.

**Soru 5: Rezervasyon sistemine dahil edilmek istenmeyen, stok bazında kümülasyon yapılmak istenen stoklar varsa ne yapılmalı?**

Stok Planlama Kayıtları ekranında ilgili stoklar için *Satıcı Siparişi Planlama Yöntemi* ve *İş Emri* *Planlama Yöntemi* parametreleri *"Sipariş Bazında Değil"* seçili olmalıdır. Bu tür stoklar için rezervasyon sistemi geçerli olmaz. Bütün hammadde ve mamullerde kümülasyon işleminin çalışması istenirse MRP parametrelerinde *"Sipariş Bazında"* bilgisinin *"Sipariş Bazında* *Değil"* olarak değiştirilmesi yeterlidir.

![](../_assets/5978aeac36aafa560141.png)

**Soru 6: MRP süreci talepten takip ediliyorsa, sipariş bazında rezervasyon sistemi bunu destekliyor mu?**

Evet. Rezervasyon sisteminin talepten başlaması için MRP parametrelerinde Genel-1 sekmesinde "*Sipariş Bazında* *Rezervasyon Sistemi"* ile "*MRP için satıcı siparişi yerine satın alma* *talebi oluşturulsun"* parametresi işaretlenmelidir. Böylece MRP ihtiyaçları belirlerken süreç talepten başlar ve ilgili müşteri siparişine bu talepler rezerve olur.

**Soru 7: Sipariş bazında rezervasyon sistemi kullanılırken hangi durumlarda stoklarda kümülasyon gerçekleşir?**

Rezervasyon sistemi açık ve Stok Planlama Kayıtları ekranında sipariş bazında seçili olsa bile, bu ekran üzerinde ***parti büyüklüğü ve minimum sipariş*** bilgisi yer alan stokların müşteri siparişlerindeki teslim tarihlerinin aynı ya da farklı olduğuna bakılmaksızın, fazla ihtiyaç çıkarmamak adına kümülasyon işlemi otomatik yapılır.

Kümülasyon yapılması istenen malzeme ve yarı mamuller için ne şekilde kümüle edilmesi gerektiği, Stok Planlama Kayıtları ya da Müşteri/Satıcı Stok Kayıtlarında *Yükleme Günü* sahalarında belirtilir.

**Soru 8: Sipariş bazında rezervasyon sistemi kullanıldığında MRP çalışmasında bir farklılık oluyor mu?**

Sipariş bazında rezervasyon sistemi kullanıldığında MRP raporu alınırken gelen parametre ekranında, stok bakiye kontrol ve mamul bakiye kontrol parametrelerine ek olarak, iş emri- satıcı siparişi- satın alma talep bakiyeleri, ileri tarihli belgelerle eşleştirme gibi parametrelerde aktifleşir. Bu parametreler işaretlendiği takdirde MRP çalışırken bu bakiyeleri ve eşlenen belgeleri dikkate alarak ihtiyaçları belirler.

![](../_assets/7bdc56b8ff7825f93dc5.png)

**Soru 9: Alımı yapılan malzemelerin satıcı siparişlerinde müşteri sipariş numarasının yer alması rezervasyon yapıldığı anlamına mı gelir?**

Hayır, bu şekilde olan malzemeler hala serbest stok olarak değerlendirilir. Bu şekildeki malzemeler için iş emri rezervasyonunun yapılması gerekir.

**Soru 10: İş emri rezervasyonu nasıl yapılabilir?**

İş emri rezervasyonu iki şekilde yapılabilir.

1. Üretim modülünde İşlemler menüsü altından "İş Emri Malzeme Talep Ekranı" yardımıyla rezerve edilebilir.
2. Depolar arası transfer yardımıyla iş emrine stok rezerve edilebilir. Bu işlemin yapılabilmesi için satış fatura parametrelerinde "*Üretim reçeteleri getirilsin mi*?" parametresinin işaretli olması gerekir.

**Soru 11: Malzeme rezervasyonunda alt reçeteler rezervasyon ekranında neden gelmiyordur?**

İş emri malzeme rezervasyon işlemi esnasında bileşenlerde bakiye bulunması gereklidir. Bu bakiye miktarlarına göre gerekli set miktarları ve öneri-transfer miktarları oluşur. Bileşenlerde bakiye olmadığında mamul için set miktarı oluşamadığından rezervasyon işlemi de gerçekleşemez.

**Soru 12: Mamul rezervasyonu nasıl gerçekleşir?**

İki şekilde yapılabilir:

1. İş emrine bağlı üretim sonu kaydı yapıldığında, iş emri için müşteri sipariş bilgisi yer alıyorsa, sistem bu üretim sonu kaydında oluşan mamulü ilgili siparişe rezerve eder. Dengeleme ekranları kullanılıyorsa iş emrine müşteri siparişi otomatik gelir.
2. Mamullerin, Depolar Arası Transfer Kaydı ile müşteri siparişine rezervasyonu yapılabilir. Bunun için satış fatura parametrelerinde "*DAT ve Ambar Giriş-Çıkış fişinde* *sipariş no sorulsun mu*?" parametresinin işaretlenmesi ve DAT kaydı sırasında ilgili müşteri sipariş numarasının girilmiş olması gerekir.

![](../_assets/539e4fb138461d831689.png)

**Soru 13: Mamul rezervasyonu oluşturma ekranında depo kodları neden gelmiyordur?**

MRP parametrelerinde "Sipariş bazında rezervasyon" parametresi işaretli ise Üretim modülünde Şube-Depo tanımlamalarının yapılmış olması gereklidir.
