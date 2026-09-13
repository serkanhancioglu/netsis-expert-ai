---
title: "Ters Bakiyeli Hesap Kontrolü"
page_id: "74716057"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Ters Bakiyeli Hesap Kontrolü"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Ters Bakiyeli Hesap Kontrolü"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTU5YTViYmJmLWU3ZTEtNDE3NC1iOWE4LWEyNzQ0Yjk0ZDgyMyZsaW5rPTg1ZjQzYjAzLTUwYjktNDZmYi1iYjYxLTEyMjgzZTVlMzQ1NCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=59a5bbbf-e7e1-4174-b9a8-a2744b94d823&link=85f43b03-50b9-46fb-bb61-12283e5e3454&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ters-bakiyeli-hesap-kontrolu_80087930_74716057.html"
source_version: "2022-11-02T14:48:34.400+03:00"
source_bytes: 504807
fetched_at: "2026-09-13T04:24:15+00:00"
generator: "netsis-scraper 1.0.0"
---
# Ters Bakiyeli Hesap Kontrolü

Ters Bakiyeli Hesap Kontrolü ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Satıcı/Alıcı hesapların dönem sonlarında ters bakiye verip vermediği ters bakiyeli hesap kontrol raporu ile tespit edilir. 120/320 bilanço hesaplarının ters bakiye vermesinin en önemli nedeni malı henüz teslim almadan ödeme yapılmasıdır.
Dönem sonu işlemlerinden bir tanesi ters bakiye veren bu hesapların tespiti ve 159-340 sipariş avansları hesaplarına virmanlanmasıdır. Netsis içerisinde Ters Bakiyeli Hesap Yansıtma Girişi ve Ters Bakiyeli Hesap Kontrol Raporu ekranları aracılığı ile ters bakiye veren hesapların tespiti ve belirlenecek hesaplara virmanlanması sağlanmaktadır.

#### Ters Bakiyeli Hesap Yansıtma Girişi
![](../_assets/742b499eea255425332b.png)

Ters bakiye veren hesapların ve bu hesapların virmanlanacağı yansıtma hesaplarının tanımlanması Ters Bakiyeli Hesap Yansıtma Girişi ekranından yapılır. Eğer tüm hesaplar için aynı yansıtma hesabı çalışacaksa, gridden ana hesap seçilip yansıtma kodu girilir. Bu durumda tüm grup ve muavin hesaplara aynı yansıtma hesabı atanır. Eğer grup bazında değişen yansıtma hesapları varsa grup hesap seçilir ve yansıtma hesabı doldurulur. Bu durumda o gruba bağlı tüm muavin hesaplara ilgili yansıtma hesabı atanır. Muavin bazında yansıtma hesabı tanımlanacak olması durumunda her bir muavin tek tek seçilip yansıtma hesabı doldurulmalıdır.

#### Ters Bakiyeli Hesap Kontrol Raporu

120/320 bilanço hesaplarının ters bakiye verip vermediği ters bakiyeli hesap kontrol raporu ile kontrol edilip, bu bakiyelerin sipariş avansları hesaplarına virmanlanması sağlanır.
![](../_assets/af006044e173c2be5ded.png)

**Bakiye Düzeltme Fişi Atılsın** seçeneği, ters bakiye veren hesapların ters bakiyeli hesap yansıtma girişi ekranından belirlenmiş olan yansıtma hesaplarına virmanlanacağı fişin oluşması için işaretlenmelidir.
**Atılan** **Düzeltme** **Fişi** **Ters** **Çevrilsin:** Ters bakiye veren 120/320 hesapların sipariş avanslarına aktarılması bir dönem sonu işlemidir. Dönem sonu raporları alınıp kontrolleri sağlandıktan sonra sipariş avanslarına aktarılan tutarların tekrar ilgili 120/320 hesaplara geri alınmak istenmesi halinde Atılan Düzeltme Fişi Ters Çevrilsin seçeneği işaretlenmelidir.
Yukarıdaki örnek rapor kısıt görselinde hesapların Aralık sonu bakiyesi dikkate alınarak ters bakiye kontrolü yapılması, bu kontrol sonucunda çıkan kayıtların 30.11 tarihi ve 000010000000074 numarası ile bakiye düzeltme fişinin oluşması ve oluşacak olan 000010000000074 nolu bakiye düzeltme fişinin tam tersi çalışacak şekilde 01.12 tarihli bir fiş oluşması sağlanmak istenmiştir.
Alınan raporun sonucunda Aralık sonunda ters bakiye veren hesaplar ve tutarları tespit edilmiştir.
![](../_assets/9b2b17ec9563546139e0.png)
120/320 hesapların ters bakiyeli hesap yansıtma girişi ekranında belirlenen hesaplara virmanlanlandığı 30.11 tarihli 74 numaralı fiş ve bu fişi ters çeviren yani yine tutarları 120/320 hesaplara virmanlayan 01.12 tarihli fişler program tarafından otomatik olarak oluşturulmuştur.
![](../_assets/1af779866d57aa0e3f77.png)
