---
title: "Mamul Parçalama"
page_id: "50663733"
product: "netsis-3-enterprise"
depth: 4
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Üretim"
  - "Kayıt/Üretim"
  - "Mamul Parçalama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Üretim / Kayıt/Üretim / Mamul Parçalama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWYwMjdhMWI0LTQzOWQtNGU1MC04ZTYxLTA4ZmY5ZmNkMzM4MyZsaW5rPTMwZjdlZmRjLWUxMWMtNDU3MC05MjExLWVlMmI0MmVmOWI4NiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=f027a1b4-439d-4e50-8e61-08ff9fcd3383&link=30f7efdc-e11c-4570-9211-ee2b42ef9b86&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "mamul-parcalama_50663775_50663733.html"
source_version: "2022-10-13T12:13:16.100+03:00"
source_bytes: 37929
fetched_at: "2026-09-13T04:18:56+00:00"
generator: "netsis-scraper 1.0.0"
---
# Mamul Parçalama

Mamul Parçalama, Üretim modülünde Kayıt/Üretim menüsünün altında yer alır.

Mamul parçalama, iade olarak gelen ya da mamul halde satın alınan mamulün parçalanarak bileşenlerine ayrılmasını ve oluşan parçaların maliyet hesabının yapılmasını sağlar. Mamul maliyeti bileşenler üzerine dağıtılırken, reçetedeki kullanım miktarları oranında hesaplama yapılır.

Mamul Parçalama ekranı; Sabit Bilgiler ve Ek Bilgiler olmak üzere iki sekmeden oluşur.

**Sabit Bilgiler**

Mamul Parçalama ekranı Sabit Kıymet sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Mamul Parçalama Ekranı |  |
| --- | --- |
| Fiş No | Mamul parçalama kaydının stok hareketlerine işlenecek fiş numarasının girildiği alandır. Mamul parçalama kaydının herhangi bir nedenle iptal edilmesi gerektiğinde, yine bu bölümden işlem yapılması için fiş numarasının girilerek ekrana kaydın getirtilmesi gerekir. Fiş numarası olmayan bir üretim sonu kaydı iptal edilemez. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile, fiş numaralarına ulaşılır. |
| Tarih | Mamul parçalama kaydının stok hareketlerine aktarılacak tarihin girildiği alandır. |
| Lokal Depo | Üretim safhaları olarak lokal depoları kullanan firmalar için, üretilecek mamulün hangi lokal depoda üretildiği bilgisinin girildiği alandır. Özellikle lokal depoların, üretim safhaları olarak kullanıldığı durumda, her mamul ve yarı mamul üretiminin yapılacağı bir lokal deposu bulunur. Bu lokal depo kodu, ilgili mamul ya da yarı mamulün stok kartı ek bilgilerine işlenir. Mamul parçalama kaydında ise mamul/yarı mamulün stok kartındaki lokal depo kodu kontrol edilir. Burada girilen lokal depo koduyla aynı değilse kullanıcılar uyarılır. İsteğe bağlı olarak üretime devam edilebilir. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile, lokal depo kodlarına ulaşılır. |
| Giriş Depo | Üretim safhaları ya da ambarlarını lokal depo olarak tanımlayan firmalar için, üretilecek mamuldeki bileşenlerin girişinin yapılacağı depo kodunun girildiği alandır. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile, depo kodlarına ulaşılır. |
| Mamul Kodu | Mamul parçalama kaydı ile üretimi yapılacak mamul kodunun girildiği alandır. Kaydedilecek mamullerin reçetelerinin mutlaka girilmiş olması gerekir. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile, stok kodlarına ulaşılır. |
| Yapılandırma Kodu | Mamul parçalama kaydı için yapılandırma kodunun girildiği alandır. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile, tanımlanan yapılandırma kodlarına ulaşılır. |
| Yapılandırma Açıklama | Yapılandırma koduna ait açıklama bilgisinin otomatik olarak ekrana girildiği alandır. |
| Miktar | Mamul parçalama kaydında, ilgili mamul için miktar bilgisi girilen alandır. |
| 2.Miktar | Üretim → Kayıt → Üretim Parametreleri → “2. Miktar Girilecek” parametresinin işaretlenmesi ile aktif hale gelen alandır. Üretilen mamule ait 2. miktar takibi yapılması için kullanılır. **Örneğin;** 10 kg. üretilen bir mamulün 1 çuval yaptığı varsayıldığında, çuval miktarı 2. Miktar alanına kaydedilebilir. Fire Uygulaması kullanılacaksa, 2. Miktar alanı fire miktarlarının takibi için de kullanılır. |
| Proje Kodu | Yardımcı Programlar → Kayıt → Şirket/Şube Parametreleri → “Proje Uygulaması Var” parametresinin işaretlenmesi ile aktif hale gelen alandır. İlgili üretim hareketi için mutlaka proje kodu girilmesi gerekir. Yapılan üretim, "İş Emri bağlantılı" ise bu kez iş emrinden girilen proje kodu bu alana otomatik olarak yansıtılır ve istendiği zaman üzerinde değişiklik yapılabilir. Girilen proje kodları, stok hareket kayıtlarına aktarılır. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile proje kodları arasından seçim yapılır. |
| Öncelik | Bileşenler için alternatif malzeme tanımlanması durumunda herhangi bir öncelik kodu girildiğinde, reçete kayıtlarında “Belgede Öncelik Değişebilsin” parametresi işaretli iken, mamule ait her kalem için alternatif politikası "Öncelik" seçilmiş gibi düşünülerek, seçilen önceliğe sahip malzemelerin getirilmesini sağlayan alandır. Diğer alternatif politikalar dikkate alınmaz. |
| İş Emri/Sipariş No | Sipariş No: Sipariş modülünde "Müşteri Siparişleri" bölümü çalıştırılıyor ve "Üretim Sonu Kayıtlarının" sipariş bağlantılı takip edilmesi istendiği zaman ilgili siparişin numarasının girildiği alandır. İş Emri No: Üretimde iş emirleriyle çalışılıyor ve üretim sonu kayıtlarının iş emri bağlantılı takip edilmesi istendiği zaman, ilgili iş emrinin numarasının girildiği alandır. Bu numara, stok hareketlerinde "Sipariş Numarası" alanına kaydedilir. Hem sipariş hem iş emri takibi varsa, iş emri numarasının girilmesi gerekir. İlgili siparişin numarasının iş emri kaydına yazılması gerekir. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile, iş emri/sipariş numaralarına ulaşılır. |
| Tüm Seviyeler Parçalansın | Mamul parçalama işleminde tüm seviyelerin parçalanması için kullanılan seçenektir. |
| Açıklama | Mamul parçalama kaydında raporlama amacıyla açıklama bilgisinin girildiği alandır. |
| ![](../../../_assets/8d716c0a4850af7b4aa5.png) Fiş Üret | Mamul parçalama Kaydı tamamlandıktan sonra, üretim sonu raporunun alınması ve istenirse kayıtların gerçekleştirilmesi için kullanılan butondur. Butona tıklandığında belirlenen mamul parçalama için gerekli olan reçete kaydı ekrana gelir. Ekranın alt kısmına sıralanan mamul, yarı mamul veya hammadde kullanım miktarlarını, ilgili stok kodu üzerinde iken fare ile çift tıklayarak yukarıdaki ekrana getirterek miktar değişimi yapılabilir. İlgili mamul için kullanılan herhangi bir bileşen kodu, o anlık üretim için silinebilir ve reçetede olmayan bir bileşen kodu eklenebilir. Butona tıklandığında belirlenen mamul üretim miktarı için gerekli olan reçete kaydı ekranınıza gelecektir. Ekranın alt kısmına sıralanan mamul, yarı mamul veya hammadde kullanım miktarlarını, ilgili stok kodu üzerinde iken farenizi çift tıklayarak yukarıdaki ekrana çağırabilir ve miktarını değiştirebilirsiniz. İlgili mamul için kullanılan herhangi bir bileşen kodu, o anlık üretim için silinebilir ve reçetede olmayan bir bileşen kodu eklenebilir. Yapılacak değişiklikler tamamlandıktan sonra tekrar "Fiş Üret" butonuna tıklanarak son hali ile üretim kaydı gerçekleştirilir. |
| ![](../../../_assets/5f665fe4e15cf4e69c54.png) Fiş İptal | Fişe ait mamul parçalama kayıtlarının iptal edilmesi için kullanılan butondur. |
| ![](../../../_assets/172b96533f18652997a3.png) Yeni Fiş | Ekran üzerindeki bilgilerin temizlenerek yeni kaydın girilmesi için kullanılan butondur. |
| Stok Kodu | Parçalanacak mamul ya da yarı mamul için stok kodu girilen alandır. Reçetede yer alan bir stok kodunun ekrana getirilmesi sağlanarak başka bir stokla değiştirilmesi için kullanılır. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile, stok kodlarına ulaşılır. |
| Asorti Kodu | Asorti kodunun girildiği alandır. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile, tanımlanan özellik kodlarına ulaşılır. |
| Asorti Kodu Açıklaması | Asorti koduna ait açıklama bilgisinin otomatik olarak ekrana girildiği alandır. |
| Giriş/Çıkış | Mamul parçalama kaydı yapılan işlemin giriş/çıkış olarak seçiminin yapıldığı alandır. |
| Miktar | Mamul parçalama kaydında, ilgili mamulün üretileceği miktar bilgisinin girildiği alandır. |
| 2.Miktar | Üretim → Kayıt → Üretim Parametreleri → “2. Miktar Girilecek” parametresinin işaretlenmesi ile aktif hale gelen alandır. Üretilen mamule ait 2. miktar takibi yapılması için kullanılır. **Örneğin;** 10 kg. üretilen bir mamulün 1 çuval yaptığı varsayıldığında, çuval miktarı 2. Miktar alanına kaydedilebilir. Fire Uygulaması kullanılacaksa, 2. Miktar alanı fire miktarlarının takibi için de kullanılır. |
| Lokal Depo | Üretim safhaları olarak lokal depoları kullanan firmalar için, üretilecek mamulün hangi lokal depoda üretildiği bilgisinin girildiği alandır. Özellikle lokal depoların, üretim safhaları olarak kullanıldığı durumda, her mamul ve yarı mamul üretiminin yapılacağı bir lokal deposu bulunur. Bu lokal depo kodu, ilgili mamul ya da yarı mamulün stok kartı ek bilgilerine işlenir. Ters üretim sonu kaydında ise mamul/yarı mamulün stok kartındaki lokal depo kodu kontrol edilir. Burada girilen lokal depo koduyla aynı değilse kullanıcılar uyarılır. İsteğe bağlı olarak üretime devam edilebilir. Rehber butonu ![](../../../_assets/088477bb321d1b20c939.jpg) ile, lokal depo kodlarına ulaşılır. |

**Ek Bilgiler**

Üretim modülündeki Saha Tablo Eşleştirmesi ekranından Mamul Parçalama Kaydı seçilerek yapılan tanımlamaların listelendiği sekmedir. Rapor amaçlı olarak kullanılan alanlar yer alır.
