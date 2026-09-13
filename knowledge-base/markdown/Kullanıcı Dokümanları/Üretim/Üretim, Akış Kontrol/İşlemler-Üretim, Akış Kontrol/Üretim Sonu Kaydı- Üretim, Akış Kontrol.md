---
title: "Üretim Sonu Kaydı/ Üretim, Akış Kontrol"
page_id: "29994329"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Üretim"
  - "Üretim, Akış Kontrol"
  - "İşlemler/Üretim, Akış Kontrol"
  - "Üretim Sonu Kaydı/ Üretim, Akış Kontrol"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Üretim / Üretim, Akış Kontrol / İşlemler/Üretim, Akış Kontrol / Üretim Sonu Kaydı/ Üretim, Akış Kontrol"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTE5Y2FmZmJiLWRiZGUtNGZjZi1iZDY1LTBmZTA1ZDk4MWYzZiZsaW5rPTBjOTliMmM3LTZjOWUtNGZkMy1iZjA2LTg5OTIzNTk2MDk4ZSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=19caffbb-dbde-4fcf-bd65-0fe05d981f3f&link=0c99b2c7-6c9e-4fd3-bf06-89923596098e&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "uretim-sonu-kaydi-uretim-akis-kontrol_50665372_29994329.html"
source_version: "2022-11-08T09:38:04.877+03:00"
source_bytes: 28620
fetched_at: "2026-09-13T04:20:40+00:00"
generator: "netsis-scraper 1.0.0"
---
# Üretim Sonu Kaydı/ Üretim, Akış Kontrol

Üretim Sonu Kaydı, Üretim Bölümü'nde, "İşlemler/Üretim-Akış Kontrol" menüsünün altında yer alır. Üretim Sonu Kaydı, Üretim Akış Kaydı kullanılarak girilen üretim bilgilerinden, üretim sonu kaydı oluşturulması ve istendiği zaman üretimin stok hareketlerine yansıtılması için kullanılan bölümdür. Üretim Sonu Kaydı, Üretim Akış Kontrol bölümünde girilen iş emirleri bazında ayrı ayrı oluşturulur. Ayrıca, ilgili iş emirlerinde girilen operasyonlardan, reçete kayıtlarında "Son Operasyon" olarak işaretlenen ve Aktivite Kodu "İşlem" olanlar dikkate alınır. Stok Planlama Kayıtları bölümünde ilgili mamul için, üretim sonu kayıt yerinin “Üretim Akış Kontrol” olarak işaretlenmesi gerekir.

Üretim Sonu Kaydı ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Üretim Sonu Kaydı Ekranı |  |
| --- | --- |
| İş Emri No Aralığı | Üretim sonu kaydı oluşturulacak iş emirleri için kısıt verilen alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, iş emirleri arasından seçim yapılır. |
| Tarih Aralığı | Üretim sonu kaydı oluşturulacak iş emirleri için tarih kısıdı verilen alandır. |
| Vardiya Aralığı | MRP Parametreleri bölümünde tanımlanan vardiya dilimlerinin öndeğer olarak program tarafından otomatik getirildiği alandır. |
| Fişler İş Emri Bazında Tek Tek Oluşturulsun | Verilen aralıklarda, bir iş emrine ait tüm son operasyon üretim kayıtlarının toplam miktarının üretim sonu fiş satırını oluşturması için kullanılan seçenektir. **Örneğin;** ```text<br>İş Emri No İş Emri Mik. Opr.Kodu Ak.Kodu Miktar<br>``` ```text<br>00000089 500 OP1 İşlem 150<br>``` ```text<br>00000090 800 OP1 (Son op.) İşlem 300<br>``` ```text<br>00000089 500 OP2 (Son op.) İşlem 80<br>``` ```text<br>00000089 500 OP1 İşlem 180<br>``` ```text<br>00000090 800 OP1 (Son op.) İşlem 250<br>``` ```text<br>00000089 500 OP2 (Son op.) İşlem 200<br>``` şeklinde üretim akış kayıtları olduğunda, bu kayıtlardan oluşacak üretim sonu kayıtları aşağıdaki şekildedir: ```text<br>İş Emri No İş Emri Mik. Ür.Miktar<br>``` ```text<br>00000089 500 280 (OP2 miktarlarının toplamı)<br>``` ```text<br>00000090 800 550<br>``` Bu üretim miktarı tespit edildikten sonra program ilk olarak üretilecek mamullerin üretim sonu fişlerini oluşturur. Üretim sonu fişlerinin üretilmesi (Stokların çalıştırılması) istendiğinde bu bölümden otomatik yapılır. İsteğe bağlı oluşan bu fişler, üretim modülünden açılarak, üretim işlemi burada gerçekleştirilir. Eğer üretim sonu fişleri, Üretim modülünden üretilecek ve Serbest Üretim Sonu kaydı kullanılacaksa, her bir üretim sonu fişinde bir tek mamul satırının bulunma zorunluluğu vardır. Birden fazla mamul satırı içeren üretim sonu fişi, Serbest Üretim Sonu Kaydı bölümünden açılamaz. Üretim işlemi için bu bölüm kullanılacaksa, her fişte tek satır oluşması için "Fişler İş Emri Bazında Tek Tek Oluşturulsun" seçeneğinin işaretlenmesi gerekir. Seçenek işaretlendiğinde yukarıdaki örnek için oluşacak fişler aşağıdaki şekildedir: ```text<br>Ür.Sonu Fiş No. İş Emri No Ür.Miktar<br>``` ```text<br>00000078 00000089 280<br>``` ```text<br>00000079 00000090 550<br>``` Aksi halde oluşacak fişler aşağıdaki şekildedir: ```text<br>Ür.Sonu Fiş No. İş Emri No Ür.Miktar<br>``` ```text<br>00000078 00000089 280<br>``` ```text<br>00000078 00000090 550<br>``` Eğer Seri/Lot takibi varsa, bu seçenek aktif olmaz. Zaten her bir satır ayrı fişlerde oluşturulur. Bunun nedeni; seri/lot kullanımında, üretim sonu kaydı sırasında, seri/lot bilgisi girilmesi için mutlaka Serbest Üretim Sonu Kaydı kullanılmasının zorunlu olmasından kaynaklanır. |
| Fiş No Serisi | Oluşturulan üretim sonu kaydı fiş numarasının oluşturulması istenen seri numarasının girildiği alandır. |
| Kayıt Tarihi | Oluşan üretim sonu fişleri için tarih girilen alandır. Program tarafından günün tarihi ve sistemin saati otomatik olarak getirilir. |
| Öncelik | Alternatif malzeme tanımlarını kullanmak için giriş yapılan alandır. Böylece, Üretim Sonu Kaydı sırasında alternatif malzeme tanımına göre malzeme sarfı yapılabilir. |
| Depo Önceliği | Üretim sonu kaydı için depo önceliğinin seçildiği alandır. Alanın sağ tarafında yer alan aşağı ok butonu ile; Stok Depo Kullan, İş Emri Depo Kullan, UAK Depo Kullan, Üretim Depo Kullan ve Hiçbiri seçenekleri arasından seçim yapılır. |
| Lokal Depo | Üretim sonu kaydı için lokal depo seçilen alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, depolar arasından seçim yapılır. |
| Çıkış Depo | Üretim sonu kaydı için çıkış deposunun seçildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, depolar arasından seçim yapılır. |
| Oluşturulan Fişler Otomatik Üretilsin | Oluşturulan üretim sonu kayıtlarının stok hareketlerine de işlenmesi için kullanılan seçenektir. Aksi halde, oluşan üretim sonu kayıtlarının üretilmesi için, Üretim modülünde yer alan "[Üretim Sonu Kaydı](<../../Kayıt-Üretim/Üretim Sonu Kaydı.md>)" bölümünden ilgili fişlerin çağrılarak kayıtlara geçmesinin sağlanması gerekir. |
| Otomatik Yarı Mamullerde Girdi/Çıktı | Otomatik reçete olarak tanımlanmış yarı mamullerin, üretim sonu kaydı sırasında anlık olarak üretilmesi (Giriş yapması) ve anlık sarf edilmesi (Çıkış yapması) için kullanılan seçenektir. |
| Otomatik Yarı Mamullerde Stoktan Kullan | Üretim Reçete Kayıtlarında, yarı mamuller için tanımlanan reçetelerde, bu yarı mamullerin kullanıldığı mamullerin üretimi sırasında, yarı mamullerin otomatik üretilmesi için “Otomatik Reçete” parametresi seçilir. Bu durumda, ilgili yarı mamullerin bulunduğu mamullerin üretimi sırasında, otomatik olarak bu yarı mamuller de üretilir. Bu üretimlerde, üretilen mamul için yarı mamul bakiyesinin yeterli olup olmadığına bakılmaz ve mamulün üretimi için gerekli olan miktarda yarı mamul, stokta yok kabul edilerek üretilir. Bu şekilde yapılan üretimlerde, yarı mamulün stokta bulunup bulunmadığına bakılmadığı için, yarı mamul stoklarında mamulün üretiminden kaynaklanan gereksiz bir çoğalma söz konusudur. Üretim sonu kayıtlarında bu parametre kullanılabilir. Parametre seçildiğinde, bu tür yarı mamullerin bakiyelerine bakılır ve mamulün üretimi için gerekli olan miktar varsa yarı mamul üretilmez. Yarı mamul bakiyesi mamulün üretimi için yeterli değilse yarı mamul üretilir. Üretim Sonu Kaydı yapılan herhangi bir iş emri, üretim akış kaydı ekranına sadece izleme amaçlı getirilebilir. Bu kayıtla ilgili düzeltme yapılması için, üretim sonu kaydının Üretim modülünden (Üretim Sonu Kaydı, Serbest Üretim Sonu Kaydı, Ters Üretim Sonu Kaydı) fiş iptalinin yapılması gerekir. |
| Mamuller Ölçü Birimi | Üretim Sonu Kaydı yapılan mamul stok kodunun, sabit kayıtlarda girilen değişik ölçü birimlerinden hangisi ile kayıtların yapılacağı tercihinin seçildiği alandır. 1,2 veya 3 seçenekleri arasından seçim yapılır. |
| Bakiye | Üretim safhalarının, lokal depolar veya şubeler olarak tanımlandığı ve hangi şube veya lokal depoların üretimle ilgili olduklarının üretim parametrelerinde belirlendiği durumlarda, bakiye kontrollerinin, üretimin yapıldığı tek depodan mı, yoksa üretimi ilgilendiren tüm depolardan mı yapılacağının seçildiği alandır. "Bütün Depolar" seçeneğinde, malzeme miktarı olarak, üretim parametrelerinde tanımlanan bütün depolardaki bakiyeler baz alınır. "Verilen Depo" seçeneğinde ise, üretimin yapıldığı ana depo, şube veya üretim sonu kaydında belirtilen lokal depodaki bakiyeler baz alınır. |
| Hatalı Kayıtlar Politikası | Üretim sonu kayıtları oluşturulurken hatalı kayıtların atlanması veya hatalı kayıtlarda işlemin durdurulması için kullanılan seçenektir. |
| ![](../../../../_assets/e43f49d8f9cd9c5fc08e.png) | Girilen kısıtlara uygun olarak üretim sonu kayıtlarının oluşturulması için kullanılan butondur. |
| ![](../../../../_assets/fc7bddd3d02962e3f0a0.png) | Üretim sonu kayıtlarının seçilerek oluşturulması için kullanılan butondur. Butona tıklandığında "Sonuç" sekmesi açılarak listelenen iş emirleri arasından seçim yapılır. İş emirlerinin hepsinin seçilmesi için ekranda yer alan ![](../../../../_assets/d15ca1ad68365b9a1a84.png) butonu, seçimleri kaldırmak için ![](../../../../_assets/92e38aeec2af64dd59c6.png) butonu, seçilen kayıtları Excel'e aktarmak için ![](../../../../_assets/d0d615df44d602f6775d.png) butonu ve üretim sonu kaydının oluşturulması için ![](../../../../_assets/a5aa236ff6e1502f9606.png) butonu kullanılır. |
