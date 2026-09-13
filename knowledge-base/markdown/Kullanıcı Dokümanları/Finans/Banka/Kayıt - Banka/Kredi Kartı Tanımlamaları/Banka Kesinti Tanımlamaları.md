---
title: "Banka Kesinti Tanımlamaları"
page_id: "22806213"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Banka"
  - "Kayıt / Banka"
  - "Kredi Kartı Tanımlamaları"
  - "Banka Kesinti Tanımlamaları"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Banka / Kayıt / Banka / Kredi Kartı Tanımlamaları / Banka Kesinti Tanımlamaları"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTZiZjkyNDg0LTc4YmEtNDg0OC04YmRmLTI5ZThlNThjY2E5YyZsaW5rPTMzZDYwNTExLTJhMGEtNGI0OC1iOWM3LTg4ZTFkOWIxMDg1MCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=6bf92484-78ba-4848-8bdf-29e8e58cca9c&link=33d60511-2a0a-4b48-b9c7-88e1d9b10850&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "banka-kesinti-tanimlamalari_34221166_22806213.html"
source_version: "2022-04-04T10:45:11.883+03:00"
source_bytes: 53186
fetched_at: "2026-09-13T04:10:00+00:00"
generator: "netsis-scraper 1.0.0"
---
# Banka Kesinti Tanımlamaları

Finans Bölümü'nde, "Kayıt/Banka" menüsünün altında yer alır. Banka Kesinti Tanımlamaları, farklı bankaların uyguladığı çeşitli kesinti tiplerinin ve komisyon oranlarının tanımlanmasını sağlayan bölümdür. Tanımlanan kesinti tipleri, daha sonra bankalar ile yapılan sözleşmelerin kaydı sırasında kullanılır.

**Örneğin:** Bir banka ile yapılan birden fazla sözleşmede, aynı kesintiler aynı oranlarla kullanılabilir. Kesintilerin, sözleşme kaydı sırasında her seferde tek tek tanımlanması yerine, bu bölümde bir kez tanımlanıp daha sonra sözleşme kaydında kullanılması mümkündür.

![](../../../../../_assets/355714b22a061ecf19af.png)

Banka Kesinti Tanımlamaları ekranında yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| Banka Kesinti Tanımlamaları Ekranı |  |
| --- | --- |
| Kesinti Kodu | Banka bazında tanımlanacak kesinti kodunun girildiği alandır. Kesinti kodu en fazla 15 karakterden oluşur. Bir bankaya ait birden fazla kesinti tanımlaması yapılabilir. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, kesinti kodlarına ulaşılır. |
| Açıklama | Tanımlanan kesinti koduna ait açıklama girilen alandır. |
| Tip Kodu | Tanımlanan kesintiye ait kesinti tipinin belirlendiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg)ile, kesinti tip kodlarına ulaşılır. |
| Banka Kodu | Tanımlanan kesintinin ait olduğu bankanın girildiği alandır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, tanımlı bankalara ulaşılır. |
| Kesinti Zamanı | Kesinti zamanının seçildiği alandır. "İlk Tahsilat" ve "Vadeli" olmak üzere iki seçenekten oluşur. Banka ile yapılan sözleşmede, kesintinin tamamının ilk ödemede yapılması gerektiğinde "İlk Tahsilat", banka ile yapılan sözleşmede, yapılacak kesintinin takside bölünmesi gerektiğinde ise "Vadeli" seçeneğinin işaretlenmesi gerekir. **Örneğin:** 4 takside bölünen bir alışveriş için, kesintiler de 4 takside bölünür. |
| Kesinti Kullanımı | Tanımlaması yapılan kesintinin kullanımı ile ilgili seçim yapılan alandır. "Brüt" veya "Net" olarak iki seçenekten oluşur. |
| Kesinti Oranı | Tanımlanan kesinti koduna ait oran girilen alandır. Kesinti kodunun kullanıldığı sözleşmelerde, bu alana girilen oran üzerinden kesinti hesaplaması yapılır. Kesintiler, kredi kartı ile yapılan ödemenin toplamı üzerinden hesaplanır. |
| Masraf Muhasebe Kodu | Banka → Kayıt → Banka Şube Bazında Parametreler → "Kart Masrafları Satış Anında Entegrasyona Atılsın" parametresinin işaretli olduğu durumlarda aktif hale gelen alandır. Parametre işaretli olduğunda, "Kapalı" tipli fatura kesildiğinde "Entegrasyon" bölümünde yer alan "Masraf Muhasebe Kodu" alanına girilen hesapta, kesinti bazında ve sözleşmede belirlenen koşullara uygun borç hareketleri oluşur. Parametre işaretli olmadığında, "Kapalı" tipli fatura kesildiğinde masraf kodundaki hesap çalışmaz. Tahsilat kayıtlarının yapıldığı sırada, kesinti tutarı kadar borç hareketi oluşur. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, muhasebe kodlarına ulaşılır. |
| Tahakkuk Muhasebe Kodu | Banka → Kayıt → Banka Şube Bazında Parametreler → "Kart Masrafları Satış Anında Entegrasyona Atılsın" parametresinin işaretli olduğu durumlarda aktif hale gelen alandır. Parametre işaretli olduğunda, "Kapalı" tipli fatura kesildiğinde "Entegrasyon" bölümünde yer alan "Tahakkuk Muhasebe Kodu" alanına girilen hesapta, kesinti bazında ve sözleşmede belirlenen koşullara uygun alacak hareketleri oluşur. Parametre işaretli olmadığında, "Kapalı" tipli fatura kesildiğinde masraf kodundaki hesap çalışmaz. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, muhasebe kodlarına ulaşılır. |

İlgili alanlara bilgi girişi yapıldıktan sonra klavyeden \<tab\> tuşuna basılarak ilerlendiğinde oluşturulması istenen kayıt alt ekrana aktarılır. Yapılan kaydın iptali için, silinmesi istenen kaydın üzerinde çift tıklandıktan sonra “Kayıt Sil” ![](../../../../../_assets/2df4b343310bcd16b01e.jpg) butonuna tıklanması gerekir.
