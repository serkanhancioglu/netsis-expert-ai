---
title: "Demirbaş Satışı"
page_id: "50683398"
product: "netsis-3-enterprise"
depth: 4
is_section: true
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Demirbaş"
  - "Kayıt / Demirbaş"
  - "Demirbaş Satışı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Demirbaş / Kayıt / Demirbaş / Demirbaş Satışı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTc3YWFkZmRjLTNiOGItNGQxOS05OTUyLWY1NGNhZmNhM2I3YyZsaW5rPTY2ZjQ2YWM0LTZiNTgtNGJkOC04N2VjLWQxNGU0OTUxOWQ0NyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=77aadfdc-3b8b-4d19-9952-f54cafca3b7c&link=66f46ac4-6b58-4bd8-87ec-d14e49519d47&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "demirbas-satisi_50683402_50683398.html"
source_version: "2022-09-23T13:37:41.320+03:00"
source_bytes: 13953
fetched_at: "2026-09-13T04:21:05+00:00"
generator: "netsis-scraper 1.0.0"
---
# Demirbaş Satışı

Demirbaş Satışı, demirbaşın kısmen veya tamamen satılması durumunda kullanılan bölümdür. Satış bilgileri yapıldığı an karta işlenmez. Yeniden Değerleme ve Amortisman Ayırma işlemi çalıştırıldığında, ilgili ayda satışı yapılan demirbaşların, satış bilgileri, amortisman bilgilerinden düşülerek devam ettirilir. Demirbaş Satışı bölümünde, son değerleme ayından öncesine satış bilgisi girilmesine izin verilmez. Eğer yanlış bir satış tarihi girilmişse, önce Son Değerleme Yılı/Ayı Değiştirme adımı ile satışın yapıldığı aya dönülmesi gerekir. Daha sonra, o aydan sonraki amortisman bilgilerinin silinmesi için Amortisman Bilgileri Silme adımı çalıştırılarak ilerideki aylara ait amortisman bilgilerinin silinmesi gerekir. Bu işlemden sonra satış bilgilerinin düzeltilmesi ve Değerleme ve Amortisman Ayırma adımı çalıştırılarak güncel aya dönülmesi gerekir.

Demirbaş satış girişi sırasında, demirbaşın son değerleme ve amortisman ayırma işlemi sonrasında oluşan Sabit Kıymet, Birikmiş Amortisman ve Fon Değerleri ekrana otomatik olarak getirilir. Bu değerler üzerinde düzeltme yapılabilir. Düzeltilen ve kaydedilen değerler, bir sonraki Değerleme ve Amortisman Ayırma adımında olduğu gibi dikkate alınır. Burada girilecek hatalı bir değer, düşme işleminin hatalı yapılmasına yol açar. Satış anında programın getirdiği son değerler ile, satışın girilmesinden sonra, ilgili satıştan öncesine ait Değerleme ve Amortisman Ayırma işlemi çalıştırılırsa - geçmişe yönelik oran bilgisi veya ilgili kayda ait bir bilgi üzerinde değişiklik yapılmışsa - oluşan son değerler arasında farklılık ihtimali meydana gelir. Bu farklar, satış amortisman kontrol listesinden kontrol edilebilir.

Demirbaş Satışı ekranında yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| Demirbaş Satışı Ekranı |  |
| --- | --- |
| Demirbaş Kodu | Satışı yapılan demirbaş için kod tanımlanan alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, demirbaş kodlarına ulaşılır. |
| Satış Kodu | Satışı yapılan demirbaş için satış kodu tanımlanan alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, satış kodlarına ulaşılır. |
| Satış Tarihi | Demirbaş satışının yapıldığı tarihin girildiği alandır. |
| Satış Belge No | Demirbaş satış belgesinin numarasının girildiği alandır. |
| Satış Miktarı | Demirbaş satış miktarının girildiği alandır. |
| Alıcı İsmi | Demirbaş alıcı isminin girildiği alandır. |
| Satış Açıklama | Demirbaş satışı ile ilgili açıklama bilgisinin girildiği alandır. |
| Çıkış Türü | Satışı yapılan demirbaş için çıkış türü seçilen alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, çıkış türlerine ulaşılır. |
| Satış Fiyatı | Demirbaş satış fiyatının girildiği alandır. |
| Sabit Kıymet Değeri | Demirbaş sabit kıymet değerinin sistem tarafından otomatik olarak getirildiği alandır. |
| Birikmiş Amortisman | Demirbaş birikmiş amortisman değerinin sistem tarafından otomatik olarak getirildiği alandır. |
| Fon Tutarı | Demirbaş fon tutarı değerinin sistem tarafından otomatik olarak getirildiği alandır. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır. Demirbaş Satışı kaydının iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
