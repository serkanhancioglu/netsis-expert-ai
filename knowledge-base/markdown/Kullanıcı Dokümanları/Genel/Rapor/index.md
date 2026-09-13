---
title: "Rapor"
page_id: "22803435"
product: "netsis-3-enterprise"
depth: 3
is_section: true
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Genel"
  - "Rapor"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Rapor"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTE1ZTJhMTNlLTkxMGEtNDg0YS1hNTUwLTZkY2FkMDllNjQ3MSZsaW5rPTZiNGRkYjJhLTMxMjYtNDgwYS05NWFkLWIwMGIzZmRlMTllYyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=15e2a13e-910a-484a-a550-6dcad09e6471&link=6b4ddb2a-3126-480a-95ad-b00b3fde19ec&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "rapor_24752465_22803435.html"
source_version: "2022-12-05T17:10:54.443+03:00"
source_bytes: 5734
fetched_at: "2026-09-13T04:15:32+00:00"
generator: "netsis-scraper 1.0.0"
---
# Rapor

Rapor modülü, “Rapor Menüsü” ile kullanıcı tarafından istenen içerikte bir raporun formatını, kıstaslarını ve sıralama tanımlamalarını yapıp rapor alınmasını sağlar. Tanımlanan formatın, gelecek zamanda tekrar aynı listeyi almak için saklanması için kullanılır.

> [!NOTE]
> Rapor modülündeki menülerden, entegre programdaki bilgileri içeren çok çeşitli ve değişik amaçlara yönelik raporlar düzenlenebilir.

Rapor hazırlanması için, ilgili modülde hangi sahadan ne tür bilgilerin tutulduğunun bilinmesi gerekir.

Rapor modülünden hazırlanan raporlar şunlardır;

- Sabit ve Hareket Raporları,
- Ek Analizler,
- Serbest Raporla
- İlişkisel Serbest Rapor.

**Sabit ve Hareket Raporları**

Sabit Bilgi Raporları; Stok, Cari, Muhasebe ve diğer modüllerde bulunan sabit kayıtlardan hazırlanan raporlardır. Sabit kayıtlarda, tarih bazında kayıt tutulmadığı için bu tür raporlarda tarih aralığı girilmez. Sabit kayıtlardan bakiye bilgilerinin alınması istendiği zaman, son bakiye bilgisi verilir.

Hareket Bilgi Raporları ise, hareket bilgilerinin girildiği yerlerden alınacak raporlardır.

**Örneğin;**

Stok Hareket, Cari Hareket, Fatura/İrsaliye Raporları, Sipariş Hareket Listesi gibi raporlarda, işlem kayıtları tarih bilgileriyle birlikte verildiği için, tarih aralığı girilerek rapor alınabilir.

Stok-Cari Analiz Raporu, diğer rapor sahalarından tümüyle farklı bir rapordur. Diğer raporlarda sadece kaydın girildiği bölümdeki bilgiler alınır.

**Örneğin;**

“Stok Sabit Listesi”, Stok modülünde sabit kartlar bölümünden girilen kayıtları verir.

Stok-Cari Analiz Raporu ise, stok hareketlerindeki alanlardan, bağlantılı olarak stok sabit ve cari sabit bilgilerindeki alanları içeren detaylı raporların tanımlandığı rapordur. "Tarih" ve "Tip" aralıklarında, cari hesap bazında hareket dökümlerinin düzenlenmesini sağlar.

> [!NOTE]
> Alış/Satış Parametrelerinde "Teslim Yeri" alanını kullanan firmalar için, teslim yerine göre stok/cari analiz raporu bu bölümden alınabilir.

Cari, stok ve fatura bilgilerinin detaylı olarak bir arada alınmasını sağlar.

> [!NOTE]
> İlgili modüllerden alınan raporlarda, tüm bu bilgileri bir arada bulunduran bir rapor mevcut değildir.

**Ek Analiz Raporları**

Programda bulunan bilgi dosyalarının bir veya birkaçının birleşmesiyle ve bazı hesaplamaların yapılmasıyla oluşacak raporlara ihtiyaç duyulabilir. Bu tür detaylı raporlar, "[Ek Analizler](<Ek Analizler/index.md>)" bölümünde yer alır. Ek Analizlerdeki raporların tanımlanması için öncelikle, ilgili bölümün "Ek Analiz Sorgulama" sekmesinde yer alan "Rapordan Önce Ek Analiz Hazırlığı Çalıştırılsın" seçeneğinin işaretlenmesi gerekir. Analiz hazırlığı çalıştırılmadan sağlıklı rapor alınamaz. Her bir rapor için ilk olarak "Ek Analiz Sorgulama" sekmesi ekrana gelir. Bu sorgulama ekranının kullanılması ile program, diskte istenen bilgilerden oluşan bir dosya yaratır. Listelenen bilgilerde de oluşturulan bu dosya baz alınır. Dolayısıyla, ek analizlerden alınan raporların güncel olması, raporların her kullanımda analiz hazırlığının yapılması ile mümkündür.

**Serbest Rapor**

Programın var olan tüm raporlarının (view) bulunduğu rapor seçeneğidir. Bu seçenek ile; hem var olan rapor seçenekleri kullanılır, hem de hazırlanan raporlar kullanılarak bilgi alınır.

**İlişkisel Serbest Rapor**

Birden fazla tablo ya da görüntü birbirleriyle ilişkilendirilerek, kapsanan kayıtların raporlanmasını sağlayan rapor seçeneğidir. Şöyle ki; İlişkisel Rapor, bir ana tablo/görüntü (Stok Sabit Kayıtları, Cari Sabit Kayıtları, Personel Sabit Bilgileri gibi) ve bu ana görüntüye bağlı tablo/görüntüler (Stok Hareketleri, Cari Hesap Hareketleri, Personel Kartoteks Kayıtları gibi) şeklinde bağlantılarla oluşturulur. Rapor listelenirken de ana kayıtlar (Stok Sabit Bilgisi) ve her bir ana kayda bağlı alt kayıtlar ilgili kaydın hareketleri olarak listelenir.
