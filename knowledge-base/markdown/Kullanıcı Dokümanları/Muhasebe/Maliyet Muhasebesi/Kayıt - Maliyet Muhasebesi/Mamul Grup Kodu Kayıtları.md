---
title: "Mamul Grup Kodu Kayıtları"
page_id: "24748848"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Muhasebe"
  - "Maliyet Muhasebesi"
  - "Kayıt / Maliyet Muhasebesi"
  - "Mamul Grup Kodu Kayıtları"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Maliyet Muhasebesi / Kayıt / Maliyet Muhasebesi / Mamul Grup Kodu Kayıtları"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTQ5MjkzM2U4LTYyNGYtNDNhZi04OTgwLWYzZTMyYTc2MjE4YSZsaW5rPTliNTlhOTdkLTExN2MtNGI4YS04MzkwLWYwNjRkNzNlYjI0OCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=492933e8-624f-43af-8980-f3e32a76218a&link=9b59a97d-117c-4b8a-8390-f064d73eb248&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "mamul-grup-kodu-kayitlari_50675182_24748848.html"
source_version: "2022-10-17T14:20:14.283+03:00"
source_bytes: 31678
fetched_at: "2026-09-13T04:14:55+00:00"
generator: "netsis-scraper 1.0.0"
---
# Mamul Grup Kodu Kayıtları

Mamul Grup Kodu Kayıtları, Muhasebe Bölümü'nde, "Kayıt/Maliyet Muhasebesi Modülü" menüsünün altında yer alır. Mamul Grup Kodu Kayıtları, Maliyet Ana Grup Kodu olan yarı mamul ve mamulün alt seviyede grubunun tanımlandığı bölümdür. Grubun oluşturulması; hem ana mamul kodunun alt seviyede izlenmesini, hem de mamul, yarı mamul, ambalaj muhasebe hesap kodları ve sarf hesaplarının yansıtma kodlarının kaydedilmesini sağlar.

Maliyet ana grup kodunun alt seviyesi bazında tanımlama yapılması istenmese dahi, maliyet ana grup bilgilerini içerecek şekilde bir adet grup kodunun tanımlanması gerekir. Çünkü; mamul, yarı mamul hesap kodları ve yansıtma hesapları, bu bölümden grup bazında girilebilir.

Mamul Grup Kodu Kayıtları ekranı; Grup Kodu Tanımı/Katsayılar, Mamul/Hammadde Hesap Kodları ve Yansıtma Hesapları sekmesinden oluşur.

**Grup Kodu Tanımı/Katsayılar**

Mamul Grup Kodu Kayıtları ekranı Grup kodu Tanımı/Katsayılar sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Mamul Grup Kodu Kayıtları Ekranı |  |
| --- | --- |
| Grup Kodu | Maliyet grup koduna verilen koddur. Buradan tanımlanan maliyet grup kodlarının, Stok Kartı Kayıtları → Ek Bilgiler sekmesinde yer alan Mamul Grup sahalarına girilmesi gerekir. Maliyet hesaplarında, stok kodlarına girilen maliyet grup kodları filtrelenir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, grup kodlarına ulaşılır. **Örneğin;** MM1 grubunu MAMUL1 olarak tanımladıktan sonra, Stok modülündeki MM1’e ait stok kartının Ek Bilgiler sekmesindeki Mamul Kodu alanına MAMUL1 girilmesi gerekir. Örneğe göre 1. aşamada üretilen "Yarı Mamul 1" ve "Yarı Mamul 2" için de mamul grupları tanımlanması ve ilgili stok kartlarına, tanımlanan mamul grup kodlarının mutlaka girilmesi gerekir. |
| Grup İsmi | Maliyet grup kodunun isminin girildiği alandır. |
| Ana Grup Kodu | Tanımlanan maliyet grup kodunun ait olduğu maliyet ana grup kodunun girildiği alandır. Maliyet hesaplamaları için bu kodun mutlaka doğru girilmesi gerekir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, ana grup kodlarına ulaşılır. Yukarıdaki örnekte, "Yarı Mamul 1" ve "Yarı Mamul 2" için açılan mamul grup kodlarında bu alana 1. AŞAMA, "Mamul 1" için açılan mamul grup kodunda ise bu alana 2. AŞAMA girilmesi gerekir. |
| Proje Kodu | Yardımcı Programlar → Kayıt → [Şirket/Şube Parametreleri](<../../Muhasebe Modülü/Ekler - Muhasebe/Ek-1 Enflasyon Muhasebesi/Genel Tanımlar/Yardımcı Programlar-Şirket-Şube Parametreleri.md>) → “Proje Uygulaması Var” parametresinin işaretlenmesi ile aktif hale gelen alandır. İlgili mamul grup kodu için mutlaka proje kodunun girilmesi gerekir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, proje kodlarına ulaşılır. |
| Tür | Kaydı oluşturulan maliyet grup kodu için tür girilen alandır. Muhasebede mahsup işlemleri oluşturulurken, burada tanımlanan tür bazında hesaplamalar yapılacağı için doğru girilmesi şarttır. Alanın sağ tarafında yer alan aşağı ok butonu ile; M-Mamul, Y-Yarı Mamul ve A-Yan Ürün türleri arasından seçim yapılır. |
| Ölçü Birimi | Stoklarda tanımlanan ölçü birimlerinden, maliyet grup kodu bazında istenenin seçilmesine olanak sağlar. Aynı maliyet grubuna ait stok kartlarına ortak ölçü birimi tanımlanması gerekir. Program, mamul grubuna ait ilk stok kodunun ölçü birimini buraya aktarır. Üzerinde değişiklik yaparken, bu gruba ait stok sabit kartlarında da aynı ölçü biriminin kullanılması gerektiği unutulmamalıdır. Seçilmiş maliyet grup kodu ölçü birimi ile, ilgili stok sabit kayıtlarının ölçü birimleri farklı olursa, maliyet hesaplamalarında yanlış tutarlar oluşabilir. Aynı ölçü birimi standardı oluşturulamayan durumlarda, stok kartı kayıtlarında tanımlanan ölçü birimleri kullanılmadan buradaki 4. sırada belirtilen birim ağırlık seçeneği üzerinden tanımlama yapılması gerekir. Birim ağırlık seçeneği, maliyet muhasebesi için program tarafından geliştirilen dördüncü ölçü birimi olarak algılanabilir. Stok Kartı Kayıtları ekranındaki Birim Ağırlık alanları kullanılarak, aynı maliyet grubuna ait stok kayıtlarının aynı düzeydeki ölçü birimine denk getirilmesi sağlanabilir. |
| Birim Katsayılar | Maliyet Ana Grup kod tanımlamasında, maliyet hesaplatma anahtarlarını birim katsayı olarak seçenler için maliyet grup kodları bazında, ilgili katsayıların - gider yerlerine göre - girildiği alanlardır. Bu alanlara girilen birim katsayılar mühendislik çalışmalarının sonunda oluşacak değerlerdir. Birim katsayı tipi dışındaki diğer maliyet hesaplama anahtarlarını seçen kullanıcılar bu alanları boş bırakır. |

**Mamul/Hammadde Hesap Kodları**

Mamul/Hammadde Hesap Kodları, maliyet grup kodunun işlem göreceği mamul, yarı mamul ve hammadde ile ambalaj sarf ve satılan malın maliyeti hesaplarının girildiği sekmedir. Maliyet hesaplamalarında oluşturulacak sarf maliyet ve satılan malın maliyeti mahsup fişlerinde, ilgili hesap kodları program tarafından bu ekrandan okunur.

Mamul Grup Kodu Kayıtları ekranı Mamul/Hammadde Hesap Kodları sekmesinde yer alan alanlar ve içerdiği bilgiler şunlardır:

| Mamul/Hammadde Hesap Kodları Ekranı |  |
| --- | --- |
| Grup Kodu | Grup Kodu Tanımı/Katsayılar sekmesinde girilen Grup kodu bilgisinin izlendiği alandır. |
| Ana Grup Kodu | Grup Kodu Tanımı/Katsayılar sekmesinde girilen Ana Grup Kodu bilgisinin izlendiği alandır. |
| Grup İsmi | Grup Kodu Tanımı/Katsayılar sekmesinde girilen Grup İsmi bilgisinin izlendiği alandır. |
| Yarı Mamul/Mamul Transfer Hesabı | İlgili yarı mamul/mamuller için çıkış hareketlerinin işleneceği hesaptır. Giriş hareketleri ise Yarı Mamul ve Mamul alanlarına girilen hesaplara işlenir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile muhasebe kodlarına ulaşılır. **Örneğin;** Bir yarı mamul için Yarı Mamul hesabı 151-01-001, Yarı Mamul Transfer Hesabı ise 151-01-002 olarak tanımlandığında, yarı mamulün üretim nedeniyle oluşan giriş hareketlerinde 151-01-001 hesabının mamul için sarf edilmesi sonunda ya da satışı yapıldığında fatura işlemleri ile çıkışında, 151-01-002 hesabı çalışır. Giriş/çıkış hesapları için böyle bir detaylandırma yapılması istenmiyorsa mamul/yarı mamul transfer hesabı ile mamul/yarı mamul hesabının aynı olması gerekir. |
| Satılan Malın Maliyeti | Bir mamulün yurtiçi satışlarına ait satılan mal maliyetlerinin, ayrı hesaplarda izlenmesi için kullanılan alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, muhasebe hesap kodlarına ulaşılır. |
| Yurtdışı Satılan Malın Maliyeti | Bir mamulün yurtdışı satışlarına ait satılan mal maliyetlerinin, ayrı hesaplarda izlenmesi için kullanılan alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, muhasebe hesap kodlarına ulaşılır. [Maliyet Muhasebesi Parametreleri](<Maliyet Muhasebesi Parametreleri.md>) → “Yurtdışı Satılan Malın Maliyeti Ayrı Çalışsın” parametresi işaretlendiğinde aktif hale gelir. "Yurtdışı Satılan Malın Maliyeti” alanında belirlenen muhasebe hesap koduna, İhracat tipli Satış Faturası ile satışı yapılan mamullerin maliyeti işlenir. |

**Yansıtma Hesapları**

Yansıtma Hesapları, maliyet grup kodunun işlem göreceği ilk madde malzeme, ambalaj, işçilik, enerji, amortisman, yardımcı servis, yedek parça, yakıt, su gibi maliyet mahsubunda yansıtma işlemlerinin yapılacağı hesap kodlarının girildiği sekmedir. Maliyet hesaplamalarında oluşturulacak maliyet mahsubunda, ilgili değerler, bu ekranda girilecek hesap kodlarına yansıtılarak alacaklandırılır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, muhasebe hesap kodlarına ulaşılır.

İlgili kayıtlar girildikten sonra “Kaydet” ![](../../../../_assets/865524a70e225c89c107.jpg) butonu ile kayıt tamamlanır. Açılan bir kayıt, kayıt sil ![](../../../../_assets/2df4b343310bcd16b01e.jpg)butonu ile iptal edilir veya üzerinde değişiklik yapılması için kaydet ![](../../../../_assets/865524a70e225c89c107.jpg) tuşu kullanılarak düzeltilir.
