---
title: "Taksitli Satış Parametreleri"
page_id: "24740091"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Müşteri Senetleri"
  - "Kayıt / Müşteri Senetleri"
  - "Taksitli Satış"
  - "Taksitli Satış Parametreleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Müşteri Senetleri / Kayıt / Müşteri Senetleri / Taksitli Satış / Taksitli Satış Parametreleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTExY2E4NzdhLWJhMDUtNGQ5Yi1hMDk0LTAxNWE4MWQ4ZDNhNiZsaW5rPWUxNmM0OWEzLWI5ZDYtNDc2OS04Y2UwLWI3YzQzOTJkZWMyZCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=11ca877a-ba05-4d9b-a094-015a81d8d3a6&link=e16c49a3-b9d6-4769-8ce0-b7c4392dec2d&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "taksitli-satis-parametreleri_34217681_24740091.html"
source_version: "2022-12-06T14:17:54.133+03:00"
source_bytes: 53871
fetched_at: "2026-09-13T04:11:49+00:00"
generator: "netsis-scraper 1.0.0"
---
# Taksitli Satış Parametreleri

Taksitli Satış Parametreleri, Finans Bölümü'nde, "Kayıt/Müşteri Senetleri" menüsünün altında yer alır. Taksitli Satış Parametreleri bölümünden kaydedilen bilgiler, "Müşteri Senetleri" modülünün kullanımında yardımcı olur. Taksitli Satış Parametre kayıtları, işaretlenen seçimler doğrultusunda işlem görür.

![](../../../../../_assets/d148525a305c846cdefc.png)

Taksitli Satış Parametreleri ekranında yer alan parametreler ve içerdiği bilgiler aşağıdaki şekildedir:

| Taksitli Satış Parametreleri Ekranı |  |
| --- | --- |
| Senet Tahsil Makbuzu Basılsın | Senet tahsilatları yapıldığında, yazıcıdan makbuz basımı istendiğinde işaretlenmesi gereken parametredir. |
| Senet Tahsilde Cariye Kayıt Yapılsın | Senetlerin tahsili yapıldıkça cariye işlemesi için işaretlenmesi gereken parametredir. Böylece, senetler ödendikçe cari hareketlere aktarılır ve senet tutarlarının tümü aktarılmadığı için ilgili carinin hesabı kapanmaz. Senetler ödendikçe hesap kapanır ve istendiğinde hesap bakiyeleri izlenebilir. Parametre işaretlenmediğinde, senetler tanzim edildiği anda cari hareketlere vadelerine göre işlenir ve borç bakiyesi kapatılır. Böylece, senet tahsil edildiğinde sadece kasaya kayıt işlenir. "Senet Tanzim" bölümünde "Cariye Kayıt Yapılsın" parametresi işaretlendiğinde bu parametrenin işaretlenmemesi gerekir. Aksi takdirde cariye hatalı kayıt aktarılır. |
| Senet Tanzimde Cariye Kayıt Yapılsın | Senet tanziminin tamamlanması sırasında, senet toplamlarının cari hareketlere işlenmesi istendiği zaman işaretlenmesi gereken parametredir. Bu parametre işaretlenerek işlem yapıldığında, borç hareketi için alınan senetler cariye işlenir ve ilgili borç tutarı henüz senetler tahsil edilmeden kapatılır. "Senet Tahsilde Cariye Kayıt Yapılsın" parametresinin işaretlendiği durumlarda bu parametrenin işaretlenmemesi gerekir. Aksi takdirde cariye hatalı kayıtlar aktarılır. |
| Taksit Sayısı | Senet tanzim bölümünde, program tarafından otomatik olarak taksit sayısının ekrana getirildiği alandır. Taksitler için uygulanan standart bir "ay" adedi varsa, bu alana adet girilmesi kolaylık sağlar. Belirli bir "ay" adedi yoksa boş bırakılabilir veya genel bir değer girilerek "Senet Tanzim" bölümüne aktarılır. Bu değer üzerinden değişiklik yapılabilir. |
| Gecikme Faizi Hesaplansın | Vade tarihinden sonra ödenen senetler için gecikme faizi hesaplanmasını sağlayan parametredir. İsteğe bağlı olarak tahsilatlara hesaplanan rakam eklenebilir. Gecikme faizi hesaplatmak için, "Tolerans Günü" ve "Faiz Oranı" bilgilerinin girilmesi gerekir. |
| Tolerans Günü | "Gecikme Faizi Hesaplansın" parametresi işaretlendiğinde kullanılması gereken parametredir. **Örneğin;** Tolerans günü olarak "45 gün" girildiği varsayıldığında, program faiz hesaplaması yaparken senedin vade tarihinden itibaren 45 gün tolerans tanır. 45 günlük gecikme için faiz hesaplanmaz. |
| Faiz Oranı | Gecikme faizi hesaplaması için kullanılacak faiz oranının girildiği alandır. Bu oran "Senet Tahsil" bölümünde kullanılır. |
| Ödeme Planı Dizayndan Basılsın | "Senet Tanzim" bölümünde bulunan Ödeme Planı Bas ![](../../../../../_assets/6551448d5eb942291a27.png) butonuna basıldığında "Dizayn" modülünde tanımlaması yapılan dizayna göre basım yapılması için işaretlenmesi gereken parametredir. İşaretlenmediğinde, standart ödeme planı basılır. |
| Taksit Tipi | "Senet Tanzim" işleminde vade tarihlerinin hangi taksit tipine göre oluşturulacağı belirlenir. Alanın sağ tarafında bulunan aşağı ok butonu ile "Ay" seçeneği seçildiğinde, senetlerin vade tarihleri arasında bir ay olacak şekilde düzenlenir. "Gün" seçeneği seçildiğinde ise, senetlerin vade tarihleri arasındaki gün sayısı değişken olup, kullanıcı tarafından belirlenen durumlarda kullanılır. |
| Taksit Aralığı | "Taksit Tipi" alanında "Gün" seçeneğinin seçilmesi ile aktif hale gelen alandır. Senetler düzenlenirken vade tarihleri arasında olması istenen gün sayısı girilir. Girilen gün bilgisi, "Senet Tanzim" ekranında program tarafından otomatik olarak ekrana getirilir. Kullanıcı, üzerinde değişiklik yapabilir. |
| Rapor Kodu Bazında Ayrı Portföy Hesabı Tutulsun | "Senet Tanzim" bölümünden girilen senetlerin, rapor kodu bazında farklı muhasebe hesaplarına işlenmesi istendiği zaman işaretlenmesi gereken parametredir. |
| K, N, A, B, C Kodu | “Rapor Kodu Bazında Ayrı Portföy Hesabı Tutulacak” parametresinin işaretlenmesi halinde, hangi rapor kodu ile hangi muhasebe hesap kodunun çalışacağı ile ilgili kod belirlenen alanlardır. Böylece, "Senet Tanzim" sırasında girilecek rapor kodu için, tanımlanan portföy hesabının çalışması sağlanır. Rehber butonu ![](../../../../../_assets/088477bb321d1b20c939.jpg) ile, muhasebe kodları arasından seçim yapılır. |
| Senet Tanziminde Çoklu Kefil Girişi Yapılsın | "Senet Tanzim" bölümünde çoklu kefil girişi yapılması istendiği zaman işaretlenmesi gereken parametredir. |
| ![](../../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | İşaretlenen parametrelerin kaydedilmesini sağlayan butondur. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) İptal | İşaretlenen parametrelerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
