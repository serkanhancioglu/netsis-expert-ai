---
title: "Şube Bazında Maliyet Muhasebesi"
page_id: "50680083"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Şube Bazında Maliyet Muhasebesi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Şube Bazında Maliyet Muhasebesi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWVmMTBjYmY0LWNjODMtNDZkOC1iYmY5LTM0MDM2MDIzNGNhOSZsaW5rPTBhNmFhYmM5LTUyNGItNGMyYy05ZmJmLWEyMmNjODkyNWFiNyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=ef10cbf4-cc83-46d8-bbf9-340360234ca9&link=0a6aabc9-524b-4c2c-9fbf-a22cc8925ab7&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "sube-bazinda-maliyet-muhasebesi_82576540_50680083.html"
source_version: "2022-11-03T09:47:40.887+03:00"
source_bytes: 7877
fetched_at: "2026-09-13T04:26:09+00:00"
generator: "netsis-scraper 1.0.0"
---
# Şube Bazında Maliyet Muhasebesi

Şube Bazında Maliyet Muhasebesi ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

|  |  |
| --- | --- |
| Amaç ve Fayda | Şube bazında ayrı maliyet hesaplama ve mahsup oluşturma işlemlerinin yapılabilmesini sağlayacak bu yenilik ile Maliyet muhasebesi sürecinde şubelerin etkinliğinin ortaya konabilmesi hedeflenmiştir.<br>Mevcut kullanımlarda yapılan alternatif çözümlerin –aynı stok kartının her şube için ayrı ayrı açılması, vb.- zorluğu düşünülerek geliştirilen yapımız içerisinde aynı stok kodu tüm şubeler için geçerli olabilecek, her şube için ayrı kartların açılmasına gerek kalmayacaktır. |
| Ürün Grubu | \[X\] Netsis Enterprise |
| Modül | \[X\] Maliyet Muhasebesi |
| Kategori | \[X\] Yeni Fonksiyon |
| Versiyon Önkoşulu | 7.0.0 |

Şubeli maliyet muhasebesi uygulamasında, maliyet değerlendirmelerinde ele alınan mamul gruplarının şube bazında farklılaştırılabilmesi sağlanmıştır. Bu sayede mamul grupları için şube bazında farklı stok kartı açılmasına gerek kalmadan stoklar ile şube bazında detaylandırılan mamul gruplarının eşleşmeleri desteklenmiştir.
Eşleştirmenin kolay ve hızlı yapılabilmesi için "Şube Bazında Mamul Grup ve Stok Kodu Eşleştirme" tanımlama ekranı tasarlanmıştır. Eşleştirme tanımlarının yeterliliğini veya uygunluğunun kontrol edebilmesi içinde kod ilişki kontrol raporu kullanılabilecektir. Bu sayede tanımlamalar sistem tarafından kontrol edilerek varsa eksiklikler, yanlış eşleştirmeler hakkında bilgiler kullanıcılara sunulacaktır.
Bununla birlikte şubeli maliyet muhasebesi kullanımında maliyet hesaplamalarında kullanılmak üzere ana kod işlem sıra tanımlamalarının eksiksiz olarak yapılmış olması ve şube kodlarının girilmiş olması gerekmektedir. Mevcut mali sıra tanımlama ekranı ile ilgili bilgiler sisteme girilebilecektir.

#### Parametreler

Şubeli maliyet muhasebesi kullanımı aşağıda belirtilen durumlarda çalışmaktadır:

- İşletmelerde şube uygulaması bulunmalıdır.
- Stok modül parametrelerinde Şubeler Dahil Maliyet Sistemi kullanılmaması gerekmektedir.
- Maliyet modül parametrelerinde Şube Bazında Maliyet Kullanımı İçin Üretim Merkezi Şube Kodu olarak "Tüm Şubeler için" seçilmiş olması gerekmektedir.
- 'MALIYET'-'SUBE_BAZINDA_MALIYET' özel parametre tanımlanmalıdır.

#### Kod İlişki Kontrol

Bu bölümde hatalı veya eksik durumların tespitine yönelik maliyet muhasebesi işlemler menüsünde Kod İlişki Kontrolü işleminde şubeli maliyet muhasebesi kullanımında öncelikle mali grup kodlarının ana kod tanımları kontrol edilmekte;
sonrasında stok-mamul grup kodları ile ana grup kod bilgilerinin karşılıklı olarak farklı olması kontrol edilmektedir. Bu bölümden alınabilecek rapor ile maliyet hesaplatma çalıştırılmadan önce eksik ve hatalı durumdaki kayıtlar görüntülenebilecektir.

#### Şube Bazında Mamul Grup ve Stok Kodu Eşleştirme

Şubeli maliyet muhasebesi kullanımı için maliyet muhasebesi modülünde şube bazında mamul grup ve stok kodu eşleştirme ekranı tasarlandı. İlgili ekrana Maliyet Muhasebesi/Kayıt bölümünde erişim sağlayabilirsiniz. Şube bazında maliyet
muhasebesi kullanımında ilgili stok kodu-mamul grup kayıtlarının bu bölümünde yapılması gerekmektedir.
Yukarıda belirtilen parametreler ve tanımlamalar yapıldığında mevcut maliyet oluşturma fonksiyonları kullanılarak şube bazında ayrı maliyet hesaplama ve mahsup oluşturma işlemlerinin yapılabilecektir.

#### Uyarılar

Şubeli maliyet muhasebesi kullanılmadığı durumda maliyet hesaplatma hazırlık süreci çalıştırıldığında TBLSTMGRUP tablosu tamamen silinir ve STSABITEK-MGRUP bağlantısı ile Y, A, M stok türleri için TBLSTMGRUP tablosu yeniden oluşturulur. Şubeli maliyet muhasebesi kullanılıyor ise herhangi bir silme işlemi yapılmaz. Stok-mamul grup kod bilgileri, kullanıcılar tarafından oluşturulmalıdır. Bu nedenle şubeli maliyet kullanımı esnasında stok veya maliyet muhasebesi parametrelerinde yapılabilecek değişiklik neticesinde (şubeli maliyet kullanımı iptal edildiğinde) mevcut STMGRUP kayıtları silinebilecektir, dikkatli olunmalıdır. Stok Modülü stok kartı bilgileri ek bilgiler bölümünde yer alan mali grup kod seçim bölümü şube bazında maliyet muhasebesi kullanımında görünmeyecektir.
