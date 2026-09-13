---
title: "Ters Üretim Sonu Kaydı"
page_id: "50663707"
product: "netsis-3-enterprise"
depth: 4
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Üretim"
  - "Kayıt/Üretim"
  - "Ters Üretim Sonu Kaydı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Üretim / Kayıt/Üretim / Ters Üretim Sonu Kaydı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWQ0MmQ5M2VjLTU0ZjUtNDQ1MS05N2IxLTk1OTkxZTFjZjE2ZiZsaW5rPTM3YzUzZjU1LTBkNDktNDY2ZS1hNDcwLTRjYjg5YjFiNGRlMSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=d42d93ec-54f5-4451-97b1-95991e1cf16f&link=37c53f55-0d49-466e-a470-4cb89b1b4de1&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ters-uretim-sonu-kaydi_50663727_50663707.html"
source_version: "2022-10-13T12:11:01.837+03:00"
source_bytes: 37556
fetched_at: "2026-09-13T04:18:54+00:00"
generator: "netsis-scraper 1.0.0"
---
# Ters Üretim Sonu Kaydı

Ters Üretim Sonu Kaydı, Üretim modülünde Kayıt/Üretim menüsünün altında yer alır. Hammaddenin parçalanarak birden fazla mamul oluşturduğu durumlarda kullanılan bölümdür. Bu işlemin yapılması için reçete oluşturulması gerekir fakat reçete tanımı da terstir. Mamul aslında hammaddedir.

**Örneğin;**

Dana

Bileşenler ise, parçalama sonucu oluşan mamullerdir.

**Örneğin;**

Bonfile, kuşbaşı gibi.

Bu bölümün kullanılması için ürün ölçü biriminin Kg. olması gerekir. Adet gibi tam sayıları içeren ölçü birimlerinde bu alandan işlem yapıldığında sonuçlar yanlış çıkar.

Ters üretim sonu kaydı sonucu, mamulden her bir bileşen için aynı miktarda çıkış - açıklama her bir çıkış hareketinde, ilgili bileşen kodudur - bileşenlere giriş yapılır. Serbest üretim sonu kaydı gibi hareketler düzeltilebilir.

Ters Üretim Sonu Kaydı ekranı; Sabit Bilgiler ve Ek Bilgiler olmak üzere iki sekmeden oluşur.

**Sabit Bilgiler**

Ters Üretim Sonu Kaydı ekranı Sabit Bilgiler sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Ters Üretim Sonu Kaydı Ekranı |  |
| --- | --- |
| Fiş No | Ters üretim sonu kaydının stok hareketlerine işlenecek fiş numarasının girildiği alandır. Ters üretim sonu kaydının herhangi bir nedenle iptal edilmesi gerektiğinde, yine bu bölümden işlem yapılması için fiş numarasının girilerek ekrana kaydın getirtilmesi gerekir. Fiş numarası olmayan bir üretim sonu kaydı iptal edilemez. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile, fiş numaralarına ulaşılır. |
| Tarih | Ters üretim sonu kaydının stok hareketlerine aktarılacak tarihin girildiği alandır. |
| Lokal Depo | Üretim safhaları olarak lokal depoları kullanan firmalar için, üretilecek mamulün hangi lokal depoda üretildiği bilgisinin girildiği alandır. Özellikle lokal depoların, üretim safhaları olarak kullanıldığı durumda, her mamul ve yarı mamul üretiminin yapılacağı bir lokal deposu bulunur. Bu lokal depo kodu, ilgili mamul ya da yarı mamulün stok kartı ek bilgilerine işlenir. Ters üretim sonu kaydında ise mamul/yarı mamulün stok kartındaki lokal depo kodu kontrol edilir. Burada girilen lokal depo koduyla aynı değilse kullanıcılar uyarılır. İsteğe bağlı olarak üretime devam edilebilir. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile, lokal depo kodlarına ulaşılır. |
| Giriş Depo | Üretim safhaları ya da ambarlarını lokal depo olarak tanımlayan firmalar için, üretilecek mamuldeki bileşenlerin girişinin yapılacağı depo kodunun girildiği alandır. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile, depo kodlarına ulaşılır. |
| Mamul Kodu | Ters üretim sonu kaydı ile üretimi yapılacak mamul kodunun girildiği alandır. Kaydedilecek mamullerin reçetelerinin mutlaka girilmiş olması gerekir. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile, stok kodlarına ulaşılır. |
| Yapılandırma Kodu | Ters üretim sonu kaydı için yapılandırma kodunun girildiği alandır. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile, tanımlanan yapılandırma kodlarına ulaşılır. |
| Yapılandırma Açıklama | Yapılandırma koduna ait açıklama bilgisinin otomatik olarak ekrana girildiği alandır. |
| Miktar | Üretim sonu kaydında, ilgili mamulün üretileceği miktar bilgisinin girildiği alandır. |
| 2.Miktar | Üretim → Kayıt → Üretim Parametreleri → “2. Miktar Girilecek” parametresinin işaretlenmesi ile aktif hale gelen alandır. Üretilen mamule ait 2. miktar takibi yapılması için kullanılır. **Örneğin;** 10 kg. üretilen bir mamulün 1 çuval yaptığı varsayıldığında, çuval miktarı 2. Miktar alanına kaydedilebilir. Fire Uygulaması kullanılacaksa, 2. Miktar alanı fire miktarlarının takibi için de kullanılır. |
| Proje Kodu | Yardımcı Programlar → Kayıt → Şirket/Şube Parametreleri → “Proje Uygulaması Var” parametresinin işaretlenmesi ile aktif hale gelen alandır. İlgili üretim hareketi için mutlaka proje kodu girilmesi gerekir. Yapılan üretim, "İş Emri bağlantılı" ise bu kez iş emrinden girilen proje kodu bu alana otomatik olarak yansıtılır ve istendiği zaman üzerinde değişiklik yapılabilir. Girilen proje kodları, stok hareket kayıtlarına aktarılır. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile proje kodları arasından seçim yapılır. |
| Öncelik | Bileşenler için alternatif malzeme tanımlanması durumunda herhangi bir öncelik kodu girildiğinde, reçete kayıtlarında “Belgede Öncelik Değişebilsin” parametresi işaretli iken, mamule ait her kalem için alternatif politikası "Öncelik" seçilmiş gibi düşünülerek, seçilen önceliğe sahip malzemelerin getirilmesini sağlayan alandır. Diğer alternatif politikalar dikkate alınmaz. |
| İş Emri/Sipariş No | Sipariş No: Sipariş modülünde "Müşteri Siparişleri" bölümü çalıştırılıyor ve "Üretim Sonu Kayıtlarının" sipariş bağlantılı takip edilmesi istendiği zaman ilgili siparişin numarasının girildiği alandır. İş Emri No: Üretimde iş emirleriyle çalışılıyor ve üretim sonu kayıtlarının iş emri bağlantılı takip edilmesi istendiği zaman, ilgili iş emrinin numarasının girildiği alandır. Bu numara, stok hareketlerinde "Sipariş Numarası" alanına kaydedilir. Hem sipariş hem iş emri takibi varsa, iş emri numarasının girilmesi gerekir. İlgili siparişin numarasının iş emri kaydına yazılması gerekir. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile, iş emri/sipariş numaralarına ulaşılır. |
| Mamul Tek Kayıt Atılsın | Mamulün tek kayıt atılması için kullanılan seçenektir. |
| Açıklama | Ters üretim sonu kaydında raporlama amacıyla açıklama bilgisinin girildiği alandır. |
| ![](../../../_assets/8d716c0a4850af7b4aa5.png) Fiş Üret | Ters Üretim Sonu Kaydı tamamlandıktan sonra, üretim sonu raporunun alınması ve istenirse kayıtların gerçekleştirilmesi için kullanılan butondur. Butona tıklandığında belirlenen mamul üretim miktarı için gerekli olan reçete kaydı ekrana gelir. Ekranın alt kısmına sıralanan mamul, yarı mamul veya hammadde kullanım miktarlarını, ilgili stok kodu üzerinde iken fare ile çift tıklayarak yukarıdaki ekrana getirterek miktar değişimi yapılabilir. İlgili mamul için kullanılan herhangi bir bileşen kodu, o anlık üretim için silinebilir ve reçetede olmayan bir bileşen kodu eklenebilir. Butona tıklandığında belirlenen mamul üretim miktarı için gerekli olan reçete kaydı ekranınıza gelecektir. Ekranın alt kısmına sıralanan mamul, yarı mamul veya hammadde kullanım miktarlarını, ilgili stok kodu üzerinde iken farenizi çift tıklayarak yukarıdaki ekrana çağırabilir ve miktarını değiştirebilirsiniz. İlgili mamul için kullanılan herhangi bir bileşen kodu, o anlık üretim için silinebilir ve reçetede olmayan bir bileşen kodu eklenebilir. Yapılacak değişiklikler tamamlandıktan sonra tekrar "Fiş Üret" butonuna tıklanarak son hali ile üretim kaydı gerçekleştirilir. |
| ![](../../../_assets/5f665fe4e15cf4e69c54.png) Fiş İptal | Fişe ait ters üretim kayıtlarının iptal edilmesi için kullanılan butondur. |
| ![](../../../_assets/172b96533f18652997a3.png) Yeni Fiş | Ekran üzerindeki bilgilerin temizlenerek yeni kaydın girilmesi için kullanılan butondur. |
| Stok Kodu | Üretilecek mamul ya da yarı mamul için stok kodu girilen alandır. Reçetede yer alan bir stok kodunun ekrana getirilmesi sağlanarak başka bir stokla değiştirilmesi için kullanılır. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile, stok kodlarına ulaşılır. |
| Asorti Kodu | Asorti kodunun girildiği alandır. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile, tanımlanan özellik kodlarına ulaşılır. |
| Asorti Kodu Açıklaması | Asorti koduna ait açıklama bilgisinin otomatik olarak ekrana girildiği alandır. |
| Giriş/Çıkış | Ters üretim sonu kaydı yapılan işlemin giriş/çıkış olarak seçiminin yapıldığı alandır. |
| Miktar | Üretim sonu kaydında, ilgili mamulün üretileceği miktar bilgisinin girildiği alandır. |
| 2.Miktar | Üretim → Kayıt → Üretim Parametreleri → “2. Miktar Girilecek” parametresinin işaretlenmesi ile aktif hale gelen alandır. Üretilen mamule ait 2. miktar takibi yapılması için kullanılır. **Örneğin;** 10 kg. üretilen bir mamulün 1 çuval yaptığı varsayıldığında, çuval miktarı 2. Miktar alanına kaydedilebilir. Fire Uygulaması kullanılacaksa, 2. Miktar alanı fire miktarlarının takibi için de kullanılır. |
| Lokal Depo | Üretim safhaları olarak lokal depoları kullanan firmalar için, üretilecek mamulün hangi lokal depoda üretildiği bilgisinin girildiği alandır. Özellikle lokal depoların, üretim safhaları olarak kullanıldığı durumda, her mamul ve yarı mamul üretiminin yapılacağı bir lokal deposu bulunur. Bu lokal depo kodu, ilgili mamul ya da yarı mamulün stok kartı ek bilgilerine işlenir. Ters üretim sonu kaydında ise mamul/yarı mamulün stok kartındaki lokal depo kodu kontrol edilir. Burada girilen lokal depo koduyla aynı değilse kullanıcılar uyarılır. İsteğe bağlı olarak üretime devam edilebilir. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile, lokal depo kodlarına ulaşılır. |

**Ek Bilgiler**

Üretim modülündeki Saha Tablo Eşleştirmesi ekranından Üretim Sonu Kaydı seçilerek yapılan tanımlamaların listelendiği sekmedir. Rapor amaçlı olarak kullanılan alanlar yer alır.
