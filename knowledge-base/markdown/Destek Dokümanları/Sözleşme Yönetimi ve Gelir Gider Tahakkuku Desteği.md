---
title: "Sözleşme Yönetimi ve Gelir Gider Tahakkuku Desteği"
page_id: "160039512"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Sözleşme Yönetimi ve Gelir Gider Tahakkuku Desteği"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Sözleşme Yönetimi ve Gelir Gider Tahakkuku Desteği"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWNmZmE3MTUwLTVkYzktNGFmZi1iOTEwLTU2MDkxNGNhMzU2NSZsaW5rPWI2NjE3NDMzLWMwZWItNGJlOS04YzJhLTE0MGM0MTU0N2Q1NSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=cffa7150-5dc9-4aff-b910-560914ca3565&link=b6617433-c0eb-4be9-8c2a-140c41547d55&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "sozlesme-yonetimi-ve-gelir-gider-tahakkuku-destegi_160039512_160039512.html"
source_version: "2024-12-11T12:58:40.657+03:00"
source_bytes: 3794934
fetched_at: "2026-09-13T04:22:27+00:00"
generator: "netsis-scraper 1.0.0"
---
# Sözleşme Yönetimi ve Gelir Gider Tahakkuku Desteği

Netsis 9.0.52 sürümü ile Sözleşme Yönetimi ve Gelir/Gider Tahakkuku desteklenmiştir. Bu düzenleme ile müşterilerimizin firmalar ile yaptığı sözleşme bilgilerinin tanımlanması, sözleşme tanımına istendiği kadar fatura kaydının bağlanabilmesi ve bağlanan faturalardaki tutarların fatura satırı detayında belirlenen dağıtım tutarlarına göre gelecek ay ve yıllara yansıtılabilmesi sağlanmıştır.

Sözleşme Tanımları ekranı ile gelir veya gider tipli sözleşmelerin kayıtları yapılabilir. Bu ekran üzerinde sözleşmenin numarasını ve cari kodunu belirledikten sonra sözleşmeye ait diğer bilgiler doldurulabilir. Sözleşmeye ait gelir veya gider tutarlarının gelecek ay ve yıllara yansıtılması istenirse, Gelecek Aylar Gid. Hs. ve Gelecek Yıllar Gid. Hs. alanlarına muhasebe hesapları tanımlanır. Bu alanlarda ??? kullanarak ay bazında farklı muavin ya da grup hesapların çalışması da sağlanabilir. Gelir Hesap Kodu alanında seçilen hesap kodu, dağıtım işlemi sırasında kullanılır.

Parametre tanımlarına göre Plasiyer, Proje ve Referans Kodu alanları da ekran üzerinde aktif olarak görülür. 3 adet açıklama alanı da talebe bağlı olarak kullanılabilir.

![](../_assets/6215a57256264780919d.png)
Ayrıca "Belge Ekle" butonu ile Sözleşme Tanımları ekranına istendiği kadar belge eklenebilir ve "Hatırlatıcı Kaydı Oluştur" butonu ile istendiğinde bir hatırlatıcı kaydı oluşturulabilir.

![](../_assets/2a07c2d6c20f692dee29.png)

Sözleşme için bir saha tablo eşleştirme tanımı gerçekleştirildiyse, Ek Bilgiler sekmesinde eşleştirmesi yapılan kullanıcı tanımlı sahalar yer alır.

![](../_assets/a90e64416b325a2a8353.png)

Bağlı Faturalar sekmesinden bu sözleşmeye bağlanabilecek faturalar seçilebilir. Seçilen faturalar için otomatik dağıtım planı oluşturulacak ise tutarların nasıl dağıtılacağı, dağıtım süresi alanında belirtilebilir. Bu alanda "Sözleşme Süresi" ve "Kalan Süre" seçenekleri bulunmaktadır. "Sözleşme Süresi" seçildiğinde ilgili tutar sözleşmenin ay sayısına bölünerek, "Kalan Süre" seçildiğinde ise ilgili tutar fatura tarihi ile sözleşmenin bitiş tarihi arasındaki ay sayısına bölünerek dağıtılır.

![](../_assets/e8053c684f937d330f7c.png)

Dağıtım Planı sekmesinden, Bağlı Faturalar sekmesinde seçilen faturaların kalemleri bazında bir dağıtım planı oluşturulabilir. Dağıtım planı "Dağıtım Planı Oluştur" butonu ile otomatik olarak oluşturulabileceği gibi istenirse "Dağıtım Tutarı" alanından manuel olarak tek tek girilebilir.

![](../_assets/87518ddd4c5fa878ce17.png)

Dağıtım planı oluşturulduktan sonra "Sözleşme Açılış Kaydı" ile faturanın ilk kaydı esnasında atılan alış veya satış hesaplarının gelecek ay ve yıl tahakkuk şeklinde tekrar düzenlenmesi sağlanır.

![](../_assets/8f9b0c68fa6a451126fd.png)

Örneğin bir alış faturası düzenlendiğinde oluşan yevmiye fişinin ilk hali aşağıdaki şekilde görünürken;

![](../_assets/c20029f1319440408073.png)

Bu alış faturası için "Sözleşme Açılış Kaydı" atıldığında yevmiye fişi, sözleşme formu üzerinde belirtilen gelecek ay ve yıl hesapları dikkate alınarak aşağıdaki şekle dönüşür;

![](../_assets/95de5612c0b7f0013938.png)

"Sözleşme Açılış Kaydı İptali" işlemi ile yevmiye fişi tekrar eski haline getirilebilir.

![](../_assets/9f79ae0519075835852a.png)

Sözleşme Açılış Kaydından sonra belirlenen tutarlar, Sözleşme Tanımları formundaki "Dağıtım Kaydı" butonu veya Sözleşme Takibi menüsündeki "Sözleşme Dağıtım" ekranı ile aylar bazında Gelir Hesap Kodu alanında belirtilen hesaba taşınır. Bu işlemde kullanıcının belirteceği bir dekont serisinden dekont kaydı oluşturulur.

![](../_assets/fc5d564463e259c4874d.png)![](../_assets/3695c5c1d67a253e0bb7.png)

Oluşturulan bu dekontların, Sözleşme Tanımları/Dağıtım Planı sekmesindeki "Dağıtım Kaydı İptali" butonu ile veya Sözleşme Takibi menüsündeki Sözleşme Dağıtım İptali ekranından silinmesi sağlanabilir.

![](../_assets/3c5760dbd3e33e23114f.png)

Bu dekontların bilgisi, Sözleşme Tanımları/Dağıtım Planı sekmesindeki grid üzerinden de izlenebilir. Ayrıca Finans\\Cari\\Raporlar menüsü altındaki Sözleşme Tanım Raporu ve Sözleşme Dağıtım Raporu ile sözleşmeye ait tanım ve detay bilgilerin raporlanabilmesi sağlanır.

![](../_assets/e60084c2ba019af0cb9e.png)
