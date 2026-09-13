---
title: "Risk Onay Sistemi ve Dekont Risk Takibi"
page_id: "104104840"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Risk Onay Sistemi ve Dekont Risk Takibi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Risk Onay Sistemi ve Dekont Risk Takibi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTc0MWM5M2Q2LWUyMDUtNGVjYS05NzNkLTA4YmM3ZjIxMGY0NiZsaW5rPWE1YzBmYjNlLTc0NmEtNGQyMS1hYzIwLTg4Y2Q3YjYwYTZkYSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=741c93d6-e205-4eca-973d-08bc7f210f46&link=a5c0fb3e-746a-4d21-ac20-88cd7b60a6da&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "risk-onay-sistemi-ve-dekont-risk-takibi_104104840_104104840.html"
source_version: "2023-02-13T13:21:53.260+03:00"
source_bytes: 1549620
fetched_at: "2026-09-13T04:23:39+00:00"
generator: "netsis-scraper 1.0.0"
---
# Risk Onay Sistemi ve Dekont Risk Takibi

9044 sürümü ile Netsis içerisinde risk limitini aşan cariler için kaydedilen belgelerin iş akış sistemine dahil edilerek onaylanması desteklenmiştir. Cari risk onay sistemi ve dekont risk takibi hakkında ayrıntılı bilgiye bu dokümandan ulaşılır.

Cari risk girişi ekranında mevcut olarak yer alan "Sipariş Risk Kontrolü", "İrsaliye Risk Kontrolü", "Fatura Risk Kontrolü" seçeneklerine "Onay Sistemi" seçeneği eklenmiştir. Bu seçeneğin aktif olabilmesi için şirket şube parametrelerindeki iş akış sisteminin aktif olması gerekir. Aynı zamanda yeni desteklenen dekont risk kontrolü için de onay sistemi seçeneği kullanılabilmektedir.

"Fatura Risk Kontrolü" altında yer alan "Onay Sistemi" seçeneğinin aktif olması için entegrasyon havuzunun kullanılması gerekir.

![](../_assets/5d7b62311839fb8a7e04.png)

Onay sistemini aktif hale getirebilmek için öncelikle "Cari Risk girişi" ekranında "Risk Kontrolü" parametresi "Onay Sistemi" seçilmeli ve "Risk Onayında Kullanılsın" seçeneği işaretli iş akış kayıtları tanımlanmalıdır.

![](../_assets/1f4bbc49daac312f1b1a.png)

Örneğin RISK5 carisi için toplam risk 7500 liradır. Faturada risk kontrolü onay sistemi seçilmiştir.

10000 liralık bir satış faturası girişi yapıldığında aşağıdaki şekilde onay sistemine dahil edileceği yönünde bilgilendirme formu ile karşılaşılacaktır.

![](../_assets/afb5f199c114bbe11947.png)

Açık işlerin kapatılması ekranına düşen onay riski için işlem açıklaması alanında risk onayına ait olduğu izlenebilmektedir.

![](../_assets/53a1b5e9c9b6d05deb83.png)

Riskli olan bir cari için belge girilmek istendiğinde ise risk uyarısı giriş ekranında verilmekte olup onay sürecine dahil edilmektedir.

![](../_assets/6af43b97ca1b9063ad88.png)

Açık işlerin onaylanması ekranına eklenen risk izleme butonu ile ilgili cari için risk bilgileri kolaylıkla görüntülenebilir.

![](../_assets/ddc5825ecc4c980b06a7.png)

Onay sürecindeki kullanıcılar tarafından onaylanması durumunda ise ilgili belge onaylı olarak kayıt altına alınır ve cari hareketlere yansıtılır. (Not: Risk onayından geçen belge için normal iş akış süreci olması durumunda bu iş akış ile süreç devam ettirilir.)

![](../_assets/b00d21c7060a601cf818.png)

Cari risk girişi ekranında onay sistemi açık olmasına rağmen iş akış kayıtlarında risk onayında kullanılsın parametresi işaretli iş akış yolu tanımlı değil ise iş akış kaydı bulunamadığına dair uyarı ile karşılaşılacaktır.

![](../_assets/b00fc82eddd6243dbf0f.png)

Birden fazla iş akış yolu tanımlamasında risk onayında kullanılsın parametresi işaretli ise bu durumda belge sonunda hangi iş akışa düşmesi isteniyor ise iş akış seçimi ekranından seçim yapılmalıdır.

![](../_assets/d9c483fb57c47c37ed71.png)

**DEKONT MODÜLÜ RİSK UYGULAMASI**

Dekont modülü içerisinde risk takibini açabilmek için dekont parametreleri içerisinde yer alan risk takibi parametresinin seçimi yapılmalıdır.

![](../_assets/17cb397952ec969be881.png)

**Risk takibi yapılmasın:** Dekont modülünde risk takibi yapılmayacak ise seçilmelidir.

**Tüm carilerde risk takibi yapılsın**: Riskin tüm cariler için kontrol edilmesi isteniyor ise seçilmelidir.

**Seçilen carilerde risk takibi yapılsın**: Cari hesap kayıtları ek bilgiler sekmesinde yer alan risk kontrolü yapılsın seçili olan cariler için risk takibi yapılması isteniyor ise seçilmelidir.

![](../_assets/47e30e1cc320d5d9b4eb.png)

İlgili cariler için cari risk girişi ekranı üzerinden dekont risk kontrolü için uygulanmak istenilen seçim yapılmalıdır.

![](../_assets/b160c37166cc819ad883.png)

Riskli cari için borç hareketi girişi yapılmak istendiğinde ise aşağıdaki şekilde uyarı mesajı ile karşılaşılacaktır.

![](../_assets/edaab8c842a3fabd9384.png)

Belge tamamlandıktan sonra onay sistemi açık ise açık işler ekranına düşen belge için onay verilip süreç tamamlanır.

![](../_assets/05b2166eff75248b5823.png)

![](../_assets/882bf7055feb78926cf1.png)
