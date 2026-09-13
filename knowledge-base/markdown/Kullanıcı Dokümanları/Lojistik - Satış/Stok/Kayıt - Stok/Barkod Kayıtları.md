---
title: "Barkod Kayıtları"
page_id: "22803705"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Stok"
  - "Kayıt / Stok"
  - "Barkod Kayıtları"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Stok / Kayıt / Stok / Barkod Kayıtları"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTA3M2Y5YTYwLTAzYmItNDY3OS05M2M4LTBmMDUxN2MzNDA4NiZsaW5rPWE1NDUwYTEzLTUzNDItNDJmNS1hYmIxLWRiMGQ4YWNmNzIwZCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=073f9a60-03bb-4679-93c8-0f0517c34086&link=a5450a13-5342-42f5-abb1-db0d8acf720d&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "barkod-kayitlari_29994210_22803705.html"
source_version: "2022-10-25T20:11:27.290+03:00"
source_bytes: 11826
fetched_at: "2026-09-13T04:04:10+00:00"
generator: "netsis-scraper 1.0.0"
---
# Barkod Kayıtları

Barkod Kayıtları, Lojistik - Satış Bölümü'nde, "Kayıt/Stok" menüsünün altında yer alır. Aynı stok koduna ait birden fazla barkod kodunun bulunduğu durumlarda, stok sabit kayıtları için barkod kaydedilen bölümdür. Burada tanımlanan barkod bilgileri, fatura belgelerinde kullanılır. Fatura Parametrelerinde bulunan “Barkod kayıtları dosyadan okunsun” parametresinin işaretlendiği durumlarda, burada tanımlanan bir barkod, fatura kalem bilgilerindeki "Stok Kodu" alanına girildiğinde, program barkod bilgisini otomatik olarak stok koduna dönüştürür.

"Barkod kayıtları dosyadan okunsun" parametresi ile ilgili detaylı bilgi için; Fatura → Kayıt → [Satış Parametreleri](<../../Fatura/Kayıt - Fatura/Satış Parametreleri.md>) dokümanına bakılabilir.

Barkod Kayıtları ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Barkod Kayıtları Ekranı |  |
| --- | --- |
| Stok Kodu | "Stok Sabit Kayıtları" bölümünden tanımlanan ve barkodları girilmesi gereken stoka ait kod bilgisinin girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, stok kodları arasından seçim yapılır. |
| Barkod | Stok koduna ait barkodun girildiği alandır. Aynı barkod, aynı mal için birden fazla tanımlanamaz. Bir stoka ait birden fazla barkod kodu, "Stok Kodu" alanına aynı stok kodu girilerek ayrı ayrı tanımlanır. Fatura, irsaliye ve siparişlerde ürünün barkod numarasına göre yapılan kayıtlar, ilgili stok koduna ait hareketlere, bu bölümden girilen bağlantı sayesinde aktarılır. |
| C.D | "Stok Parametreleri" bölümünde bulunan ‘Check Digit Kontrolü’ parametresinin işaretlendiği durumlarda, "Barkod" alanının yanında ‘C.D.’ şeklinde bir seçenek oluşur. "Check Digit Kontrolü" parametresi ile ilgili detaylı bilgi için; Stok → Kayıt → [Stok Parametreleri](<Stok Parametreleri.md>) dokümanına bakılabilir. Barkod numaraları belirli bir düzen içinde tanımlanır. Barkodun en sonunda yer alan numara bir tür hesaplamayla bulunur ve bu hesaplama tüm barkodlar için aynı şekilde yapılır. **Örneğin:** 7 karakterlik bir barkod girip C.D. seçeneğinin işaretlenmesi halinde, girilen karakterler için hesaplama yapılır ve bulunan rakam 8. karakter olarak barkod alanına eklenir. |
| Açıklama | Barkoda ait açıklama bilgisinin girildiği alandır. |
| Barkod Tipi | Girilen barkodun tipinin seçildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile, barkod tipleri arasından seçim yapılır. |
| Kayıt Tarihi | Barkodların girildiği tarihtir. |
| Ölçü Birimi | Barkod kayıtlarını kullanarak faturaya girilen stokun, (Fatura Modülünde yapılacak düzenlemelere göre) burada belirlenen ölçü birimi ile ekrana getirilmesi amacı ile kullanılan alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile ölçü birimleri arasından seçim yapılır. |
| Kilit | Tanımlanan barkod bilgisinin kullanılmayacağı durumlarda, kilitlenmesi için işaretlenmesi gereken seçenektir. |
| Yapılandırma Kodu | "Esnek Yapılandırma Uygulamasının" kullanıldığı durumlarda ekrana gelen alandır. Bu alan, sadece stok kartında "Esnek Yapılandır" seçeneği işaretli olan stoklar için aktif hale gelir. Bir stokun sahip olduğu özellikler bazında farklı barkod numaraları olduğunda, girilen barkod bilgisinin hangi konfigürasyonu için kullanılacağı bu alanda belirlenir. "Ürün Yapılandırma Tanımlamaları" bölümünden kaydedilen yapılandırma kodlarından biri girilebilir. "Esnek Yapılandırma Uygulaması" ile ilgili detaylı bilgi için; Stok → Kayıt → [Esnek Yapılandırma](<Esnek Yapılandırma/index.md>) dokümanına bakılabilir. |
| Yapılandırma Kodu Açıklaması | "Yapılandırma Kodu" alanında girilen konfigürasyona ait açıklamanın program tarafından ekrana getirildiği alandır. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır. Kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
