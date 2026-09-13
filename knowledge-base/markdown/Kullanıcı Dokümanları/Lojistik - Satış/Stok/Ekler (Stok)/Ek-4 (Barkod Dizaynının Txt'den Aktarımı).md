---
title: "Ek-4 (Barkod Dizaynının Txt'den Aktarımı)"
page_id: "29993149"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Stok"
  - "Ekler (Stok)"
  - "Ek-4 (Barkod Dizaynının Txt'den Aktarımı)"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Stok / Ekler (Stok) / Ek-4 (Barkod Dizaynının Txt'den Aktarımı)"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTcwOTI4YmMxLTFiYTYtNDQ3Ny1iMTc0LWRkN2E2MDM4MTFmMiZsaW5rPTY4ZTU2N2ZjLTZmNTEtNDU4ZC1hZjJhLTYyMWQ2NThiYzRhNCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=70928bc1-1ba6-4477-b174-dd7a603811f2&link=68e567fc-6f51-458d-af2a-621d658bc4a4&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ek-4-barkod-dizayninin-txt-den-aktarimi_30001157_29993149.html"
source_version: "2022-11-22T11:36:21.963+03:00"
source_bytes: 567282
fetched_at: "2026-09-13T04:05:28+00:00"
generator: "netsis-scraper 1.0.0"
---
# Ek-4 (Barkod Dizaynının Txt'den Aktarımı)

Barkod Dizaynının TXT'den Aktarımı ile ilgili detaylı bilgiye bu dokümandan ulaşılır.

**Barkod Programı İle TXT Oluşturma**

Barkod yazıcının dizaynı, istenen program (barkod yazıcıların orijinal programları veya çoğu barkod yazıcıyı destekleyen label view programı) ile yapılabilir. Bu programlardan yapılmış barkod dizaynının, Logo Netsis içinde kullanılması için; bu programlardan yapılmış dizaynın dışarıya **TXT** dosya olarak verilmesi gerekir. Bu TXT yeni barkod dizaynı ekranından Logo Netsis içerisine aktarılır.

Barkod yazıcı haricinde herhangi bir yazıcının Windows yazıcı ayarlarında görülmesi ile ilgili durumun sağlanması gerekir.

Yazıcı üzerinde iken fare ile "Yönet" butonuna basılarak "Bağlantı Noktaları" sekmesinde yer alan "Ports" seçenekleri arasından "Print To File (dosyaya yönlendir)" seçilir. ![](../../../../_assets/a5934f7d9fe91afa47fe.png)

Daha sonra seçilen yazıcının paylaşıma açılması gerekir.

![](../../../../_assets/661ee1569c0c5f5e3373.png)

Dos prompta çıkıp; Net use lpt1: \\\\bilgisayaradı\\{anchor:\_Hlt115770296}yazıcıpaylaşımadı (file:///\\\\\\\\bilgisayaradı\\\\yazıcıpaylaşımadı) komutu uygulanır.

(Örnek: net use lpt1: \\\\genel-nb\\tecb431)

Yukarıdaki adımlar uygulandıktan sonra label view'dan kullanılan yazıcıya etiket bastırılması istendiğinde, dosyanın saklanacağı yere dair bir sorgulama ekranı görüntülenir. Bu sayede ilgili çıktı txt olarak alınır. Net use lpt1: /delete komutu ile delpt1 yönlendirmesi iptal edilir.
Yukarıdaki örnekte, seçilmiş yazıcının barkod yazıcısı olması sadece bir örnek olup herhangi bir yazıcı tanımı ile de bu işlemlerin yapılması sağlanabilir.

Bu adımlar yazıcı Lpt1'den bağlı iken uygulanır.

**Hazırlanan TXT'nin Logo Netsis'e Aktarımı**

Barkod yazıcıların orjinal programlarından örnek bir dizayn hazırlanır. Aşağıdaki ekranda, label view programından oluşturulmuş bir txt örneği görüntülenir. Bu dizaynda barkod (11234567890128), stok kodu (000004) ve fiyat (5,00) bilgilerinin bastırıldığı görüntülenir.

Daha sonra, Logo Netsis'ten değerlerin basımı için, TXT dosyasının düzenlenmesi gerekir. Logo Netsis'ten bir alan bastırmak için, alanın TXT'de basıldığı yere Logo Netsis alan numaralarının (barkod dizaynı alan bilgilerinde bulunan "Basılacak Alan" sahasında listelenir) girilmesi gerekir.

![](../../../../_assets/337ea6bd1f0b1bc8af78.png)

Programın, bu değerlerin Logo Netsis sahası olduğunu anlaması için de saha numaralarının başına ve sonuna özel imleçlerinin konması gerekir. Böylece, yukarıdaki örnekte yer alan TXT, aşağıdaki hale gelir.

Basılması istenen alanlar, barkod dizaynında basılacak alan bilgilerinde bulunmuyorsa, alan numarası olarak "Dizayn" modülündeki alan numaralarının kullanımı da desteklenir.

**Örneğin;** "Barkod Dizaynı" ekranındaki "Basılacak Alan" sahasında "Seri No" seçeneği bulunur. Bu seçeneğin "Dizayn" modülünde yer alan numarasından faydalanarak basılması mümkün. "Dizayn" modülünde "Seri No" alanı 4431 numaralı alandan basılır ve TXT içeriği de bu alan numarasına göre düzenlenir.

Text dosyada yapılacak değişiklikler tamamlandıktan sonra, Satış → Stok → İşlemler → Stokbar İşlemleri→ Barkod Dizaynı → Genel sekmesinde yer alan Dosya Yükle ![](../../../../_assets/8ac32bb3a254429f996d.png) butonu ile, Text Logo Netsis'e yüklenir.

![](../../../../_assets/9611e8daf05436d8c0ab.png)

Bu durumda, barkod dizaynının genel bilgilerinde sadece **Port** bilgisinin girilmesi yeterlidir. Çünkü; diğer alanlar (Yazıcı ismi, Ribbon, Etiketin Genişliği, Etiketin Boyu, Etiket Sayısı, vb.) TXT de diğer program tarafından önceden belirlenir. Böylece, kalem bilgilerine herhangi bir kayıt girilmesine gerek kalmaz.
