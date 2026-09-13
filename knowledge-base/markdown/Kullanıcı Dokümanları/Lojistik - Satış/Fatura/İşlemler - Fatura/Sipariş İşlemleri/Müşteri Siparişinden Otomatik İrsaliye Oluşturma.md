---
title: "Müşteri Siparişinden Otomatik İrsaliye Oluşturma"
page_id: "24764961"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Fatura"
  - "İşlemler / Fatura"
  - "Sipariş İşlemleri"
  - "Müşteri Siparişinden Otomatik İrsaliye Oluşturma"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Fatura / İşlemler / Fatura / Sipariş İşlemleri / Müşteri Siparişinden Otomatik İrsaliye Oluşturma"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTcwMzc2MjhkLTgxYWMtNDZlMC05NzQzLWMwZjVmMzAzNmY1NSZsaW5rPTYyNjYxNzA5LWE3MWMtNGNmMy1iNzU1LWJhMjdmNzMzM2MwMSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=7037628d-81ac-46e0-9743-c0f5f3036f55&link=62661709-a71c-4cf3-b755-ba27f7333c01&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "musteri-siparisinden-otomatik-irsaliye-olusturma_24764993_24764961.html"
source_version: "2022-10-25T09:49:57.443+03:00"
source_bytes: 17506
fetched_at: "2026-09-13T04:02:56+00:00"
generator: "netsis-scraper 1.0.0"
---
# Müşteri Siparişinden Otomatik İrsaliye Oluşturma

Müşteri Siparişinden Otomatik İrsaliye Oluşturma, Lojistik-Satış Bölümü'nde, "İşlemler/Fatura" menüsünün altında yer alır.

Müşteri Siparişinden Otomatik İrsaliye Oluşturma, kaydedilmiş müşteri siparişlerinden, satış irsaliyesi oluşturulmasını sağlayan bölümdür.

Müşteri Siparişinden Otomatik İrsaliye Oluşturma ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Müşteri Siparişinden Otomatik İrsaliye Oluşturma Ekranı |  |
| --- | --- |
| Sipariş Tarihi | Belirli tarih aralığındaki siparişlerin, irsaliyeye çevrilmesi istendiğinde kullanılan alandır. |
| Teslim Tarihi | Belirli teslim tarihindeki siparişlerin, irsaliyeye çevrilmesi istendiğinde kullanılan alandır. |
| Sipariş No | Belirli aralıktaki siparişlerin irsaliyeye çevrilmesi için sipariş numara aralığının girildiği alandır. ![](../../../../../_assets/088477bb321d1b20c939.jpg) Rehber butonu yardımıyla sipariş numaraları arasından seçim yapılır. **Örneğin:** Teslim tarihi 14.10.2003 olan 10 siparişten bir kısmını teslim edebilmek için sipariş numara aralığı verilebilir. |
| Cari Kodu | Müşteri siparişlerinin irsaliyeye çevrilmesi için cari kod aralığının girildiği alandır. ![](../../../../../_assets/088477bb321d1b20c939.jpg) Rehber butonu yardımıyla cari kodlar arasından seçim yapılır. |
| İrsaliye No | Oluşacak satış irsaliyesi numarasının girildiği alandır. Alanın boş bırakılması durumunda, sistemde son kaydedilen irsaliye numarasının bir büyüğü program tarafından ekrana getirilir. |
| Açıklama | Müşteri siparişi kaydedilirken girilen açıklamaya göre irsaliye oluşturulacak ise ilgili açıklama bilgisinin girildiği alandır. Bu alana girilen açıklamaya sahip müşteri siparişleri, satış irsaliyesine çevrilir. |
| Özel Kod-1 | Müşteri siparişleri kaydedilirken girilen özel kod-1 değerine göre irsaliye oluşturulacak ise ilgili kod-1 değerinin girildiği alandır. Bu alana girilen kod-1 değerine sahip müşteri siparişleri, satış irsaliyesine çevrilir. |
| Özel Kod-2 | Müşteri siparişleri kaydedilirken girilen özel kod-2 değerine göre irsaliye oluşturulacak ise ilgili kod-2 değerinin girildiği alandır. Bu alana girilen kod-2 değerine sahip müşteri siparişleri, satış irsaliyesine çevrilir. |
| Eksi Bakiye Kontrolü | Müşteri siparişleri satış irsaliyesine çevrilirken, stoklarda eksi bakiye kontrolünün yapılması istendiğinde işaretlenmesi gereken parametredir. Bu durumda, siparişlerdeki stok kalemlerinin bakiyeleri kontrol edilir ve eksi bakiyeye düşen stok kalemleri irsaliyeye çevrilmez. |
| Onaysız Siparişler | Sipariş onay sisteminin kullanıldığı durumlarda, onaylanmayan siparişlerin de irsaliyelerinin oluşturulması için kullanılması gereken parametredir. Aksi takdirde, onaylanmayan siparişlere ait irsaliye kayıtları oluşturulmaz. |
| Basım | Oluşturulacak satış irsaliyelerinin basımı için işaretlenmesi gereken parametredir. Bu işlem sonucu, yukarıdaki alanlara verilen kısıtlar dikkate alınarak, her bir müşteri siparişi için ayrı satış irsaliyeleri oluşturulur. |
| Koşul Tarihi | Müşteri siparişleri kaydedilirken girilen koşul tarihine göre irsaliye oluşturulacak ise ilgili koşul tarihinin girildiği alandır. Bu alana girilen koşul tarihine sahip müşteri siparişleri, satış irsaliyesine çevrilir. |
| Fiyat Tarihi | Müşteri siparişleri kaydedilirken girilen fiyat tarihine göre irsaliye oluşturulacak ise ilgili fiyat tarihinin girildiği alandır. Bu alana girilen fiyat tarihine sahip müşteri siparişleri, satış irsaliyesine çevrilir. |
| Plasiyer Kodu | Belirli plasiyer kodu aralığındaki siparişlerin irsaliyeye çevrilmesi için plasiyer kodu aralığının girildiği alandır. ![](../../../../../_assets/088477bb321d1b20c939.jpg) Rehber butonu yardımıyla plasiyer kodları arasından seçim yapılır. |
| ![](../../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Müşteri siparişinde otomatik irsaliye oluşturma işleminin gerçekleşmesi için kullanılan butondur. |
| ![](../../../../../_assets/973111d004995dca0113.jpg) İptal | Müşteri siparişinde otomatik irsaliye oluşturma işleminden vazgeçilmesi durumunda kullanılan butondur. |
