---
title: "Kaynak Tanımlama"
page_id: "50666785"
product: "netsis-3-enterprise"
depth: 6
is_section: true
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Üretim"
  - "MRP"
  - "Kayıt / MRP"
  - "Kaynak Yönetimi/MRP"
  - "Kaynak Tanımlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Üretim / MRP / Kayıt / MRP / Kaynak Yönetimi/MRP / Kaynak Tanımlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPThmZTVkMzAxLTk0NWUtNDM1ZC1hNjAyLWFiNWEwN2RmYzU0NSZsaW5rPWNkN2IxOGU1LTdlNjAtNGEzYS04ZGU1LTkxMWY1ZWU0OTg1MSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=8fe5d301-945e-435d-a602-ab5a07dfc545&link=cd7b18e5-7e60-4a3a-8de5-911f5ee49851&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "kaynak-tanimlama_50666799_50666785.html"
source_version: "2022-10-19T14:33:30.847+03:00"
source_bytes: 22679
fetched_at: "2026-09-13T04:19:53+00:00"
generator: "netsis-scraper 1.0.0"
---
# Kaynak Tanımlama

Kaynak Tanımlama, Üretim Bölümü'nde Kayıt/MRP menüsünün altında yer alır. Üretimde kullanılan kaynakların tanımlanması için kullanılan bölümdür.

Kaynak Tanımlama ekranı; Kaynak Bilgileri ve Ömür Takibi sekmesinden oluşur.

**Kaynak Bilgileri**

Kaynak Tanımlama ekranı Kaynak Bilgileri sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Kaynak Tanımlama Ekranı |  |
| --- | --- |
| Kaynak Tipi | Kaynak tanımında kullanılacak üç farklı kaynak tipi bulunur. Alanın sağ tarafında yer alan aşağı ok butonu ile Stok, Demirbaş ve Personel kaynak tipleri arasından seçim yapılır. **Stok:** Kaynak kodu olarak sistem üzerinde tanımlı stok kodlarından biri kullanılır. Stok tipli kaynakların hareketleri, stok hareketleriyle bütünleşerek çalışır. **Örneğin;** Stok için alış faturası girildiğinde, kaynak hareketlerine ömür artışı olarak yansır. Üretim kaydı sırasında girilen kaynak kullanımları da stok hareketlerine sarf miktarı olarak yansır. **Demirbaş:** Demirbaş paketiyle bağlantılı olarak kaynak tanımı yapılır. Bu durumda kaynak kodu olarak demirbaş paketindeki demirbaş kodlarından biri kullanılır ve demirbaş paketindeki kart tanımı dikkate alınır. Ayrıca, demirbaş paketinden yapılacak satış ve transfer hareketleri, kaynak hareketlerine otomatik olarak yansır. **Personel:** Personel paketiyle bağlantılı kaynak tanımı yapılır. Personel tipli kaynaklar için ömür takibi yapılamaz ve kaynak hareketleri izlenemez. |
| Demirbaş Bağlantılı/Personel Bağlantılı | "Demirbaş Bağlantılı" seçeneği demirbaş tipli kaynaklarda aktif hale gelirken, "Personel Bağlantılı" seçeneği de personel tipli kaynaklarda aktif hale gelir. Bu seçenek işaretlenmediği zaman, personel veya demirbaş paket bağlantısı olmadan serbest tanım yapılabilir. Bu durumda kullanıcı tarafından yeni bir kaynak kodu verilir. |
| Şirket Kodu | Demirbaş veya personel paketleriyle bağlantısı bulunan kaynaklar için kullanılan alandır. İlgili uygulamada kullanılan şirket kodunun seçilmesi gerekir. Rehber butonu ![](../../../../../../_assets/088477bb321d1b20c939.jpg) ile, şirket kodları arasından seçim yapılır. Paket bağlantısı yoksa bu alana değer girilemez. |
| Kaynak Kodu | Stok tipli kaynaklar için stok kodunun, demirbaş paketiyle bağlantılı kaynaklar için demirbaş kodunun, personel paketiyle bağlantılı kaynaklar için personel kodunun seçildiği alandır. Paket bağlantısı olmadan tanımlanan personel veya demirbaş tipli kaynaklar için kullanıcı tarafından yeni bir kaynak kodu verilmesi gerekir. Rehber butonu ![](../../../../../../_assets/088477bb321d1b20c939.jpg) ile, ilgili kodlar arasından seçim yapılır. |
| Kaynak İsmi | Paket bağlantısı olmayan demirbaş veya personel tipli kaynak tanımlarında kullanılan alandır. Aksi durumda bu alana giriş yapılmaz ve kaynak ismi ilgili kart tanımından (Stok Kartı, Demirbaş Kartı gibi) otomatik olarak ekrana getirilir. |
| Kaynak Grup Kodu | Kaynak tanımlarını gruplamak için kullanılan alandır. Rehber butonu ![](../../../../../../_assets/088477bb321d1b20c939.jpg) ile, grup kodları arasından seçim yapılır. |
| İstasyon Kodu | Kaynağın kullanıldığı istasyon bilgisinin girildiği alandır. Rehber butonu ![](../../../../../../_assets/088477bb321d1b20c939.jpg) ile istasyon kodları arasından seçim yapılır. Boş bırakılabilir. |
| Birim Maliyet | Kaynağın birim maliyet bilgisinin girildiği alandır. Rapor amaçlı kullanılır. |
| Durum | "Aktif" veya "Pasif" seçeneklerinin yer aldığı alandır. Durumu "Pasif" olarak seçilen kaynaklar için hareket girişi yapılamaz ve bu kaynaklar ileri üretim planlama sırasında kullanılamaz. |
| Toplam Miktar | Paket bağlantısı olmayan demirbaş veya personel tipli kaynak tanımları yapıldığında kullanılan alandır. Aksi durumda bu alana giriş yapılamaz ve kaynak miktarı, ilgili kartın hareketlerinden (Stok Kartı, Demirbaş Kartı gibi) otomatik olarak ekrana getirilir. **Örneğin;** Stok tipli bir kaynağın toplam miktar bilgisi, stok hareketlerindeki bakiyeden getirilir. Demirbaş tipli bir kaynağın toplam miktar bilgisi ise, demirbaş kartındaki miktar değeri ve demirbaş satış hareketlerine bakılarak hesaplanır. |
| Öncelik Sırası | Kaynak tanımına ait öncelik bilgisinin girildiği alandır. Bu alana girilen öncelik değeri, ileri üretim planlama uygulamasında kullanılır. Öncelik değeri daha küçük olan kaynaklar, planlamada daha öncelikli olarak kullanılır. |
| Ömür Takibi Yapılsın | Ömür takibi yapılacak kaynaklar için kullanılan seçenektir. Seçenek işaretlendiğinde "Ömür Takibi" sekmesinde yer alan "Toplam Ömür" alanına bilgi girilmesi zorunlu hale gelir. |
| Açıklama | Tanımlanan kaynak için açıklama bilgisi girilen alandır. |

**Ömür Takibi**

Kaynak Tanımlama ekranı Ömür Takibi sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Kaynak Tanımlama Ekranı |  |
| --- | --- |
| Kaynak Kodu | "Kaynak Bilgileri" sekmesinde girilen kaynak kodunun izlendiği alandır. |
| Son Kullanma Tarihi | Kaynak için son kullanma tarihinin girildiği alandır. İleri üretim planlama sırasında bu tarihten sonrası için kaynağa iş planlanamaz. |
| Toplam Ömür | Kaynağın bir birimi için toplam ömür bilgisinin girildiği alandır. Kaynakla ilgili tahmini ömür bilgisidir, kesinlik içermez. Herhangi bir anda kaynağın kalan ömür bakiyesi ve ömür yüzdesi hesaplanırken, toplam ömür bilgisi kullanılır. Toplam ömür bilgisinin birimi, kullanıcı tarafından serbest olarak belirlenir. **Örneğin;** Vuruş, Kesim gibi birimler tanımlanabilir. Kaynak kullanımları ve hareketleri de bu tanımlama sırasında girilen birim üzerinden gösterilir. |
| Kalıp Göz Sayısı | Tanımlanan kaynak "Kalıp" olduğunda ve birden fazla gözü bulunduğunda kullanılan alandır. Kaynak kullanımları girilirken, tanımlamada verilen göz sayısı otomatik olarak ekrana getirilir. Kullanıcı tarafından değiştirilebilir. Göz sayısına bağlı olarak kaynağın ömür tüketimi değişir. **Örneğin;** 2 gözlü bir kaynakla 100 adetlik üretim 50 vuruş ömür tüketirken, 1 gözlü bir kaynakla aynı üretim 100 vuruşluk ömür tüketimine sebep olur. Kaynak kullanımlarının girişi sırasında göz sayısının girilmesi için kaynak tanımlarında göz sayısının 1'den büyük olduğu en az bir tanım bulunması gerekir. |
| Tamir Edilebilir | Tanımlanan kaynak için tamir yapıldığında kullanılan seçenektir. İşaretlendiğinde, tamirle ilgili genel bilgilerin girilmesi gerekir. |
| Ortalama Bakım Süresi | Kaynak için tahmini bakım süresinin girildiği alandır. İleri üretim planlama sırasında tamir edilebilir kaynakların ortalama bakım süresi dikkate alınır. Tamir dönüşünde kaynağa tekrar iş planı tanımlanabilir. |
| Maksimum Bakım Sayısı | Kaynak için yapılacak maksimum tamir sayısının girildiği alandır. İleri üretim planlama sırasında bakım planı çıkarılırken maksimum bakım sayısı dikkate alınır. Maksimum bakım sayısına ulaşan kaynaklara iş planlaması yapılmaz. Sıfır olarak tanımlandığında, maksimum bakım sayısı sınırsız olarak kabul edilir. |
| Bakımda Yıpranma Payı (%) | Kaynağın bakım sonrası toplam ömründe beklenen yıpranma payının yüzde olarak girildiği alandır. Bu bilgi ileri üretim planlama sırasında dikkate alınır ve bakımdan dönen kaynakların toplam ömür bilgisi bu değere göre belirlenir. **Örneğin;** Toplam ömrü 1000 vuruş olan bir kaynağın bakımda yıpranma payı %10 olarak tanımlanmışsa, bu kaynağın ilk bakım dönüşünde toplam ömrünün 900 vuruş olacağı varsayılır. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır.

Kaynak Tanımlama kaydının iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
