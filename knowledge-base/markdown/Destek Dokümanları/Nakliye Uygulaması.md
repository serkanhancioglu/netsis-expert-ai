---
title: "Nakliye Uygulaması"
page_id: "83498277"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Nakliye Uygulaması"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Nakliye Uygulaması"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWI0YjAyMDVkLTg1MzUtNDU0Mi05MjJlLTM4NTVkZDhmYWU5MCZsaW5rPWQzMWEwNGRiLTE3OGEtNDZhOC1hODcwLTIyN2RhNzdkMjI0YSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=b4b0205d-8535-4542-922e-3855dd8fae90&link=d31a04db-178a-46a8-a870-227da77d224a&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "nakliye-uygulamasi_90670122_83498277.html"
source_version: "2022-11-02T14:37:19.183+03:00"
source_bytes: 1144124
fetched_at: "2026-09-13T04:24:05+00:00"
generator: "netsis-scraper 1.0.0"
---
# Nakliye Uygulaması

Nakliye Uygulaması ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Stokların sevkiyatı sırasında belgelerde girilen nakliye masrafları stok hesaplarından bağımsız olarak gider hesaplarında gösterilebilir. Fatura modülünde Alış/ Satış İrsaliyelesi/Faturası veya Depolar Arası Transfer kayıtları girildikten sonra nakliyesi gerçekleşen stoklar için nakliye masrafları, İrsaliye, Fatura veya Depolar Arası Transfer kayıtlarının toplamlar sayfasında bulunan Ek Maliyet-1 sahasında takip edilmektedir.

Fatura Parametrelerinde Ek Maliyet sekmesinde yer alan "**Ek Maliyet(1)=Birim Ağırlık** Nakliye\* **Katsayısı** **Hesaplansın** **Mı**" parametresi işaretlendiğinde, nakliye masraf tutarının program tarafından hesaplanması sağlanmaktadır.

![](../_assets/34e8766ea13793dd3906.png)

**Ek Maliyet \[1\]**

Ambalaj, nakliye gibi belge tutarına ilave olan değerlerin girilmesi isteniyorsa ek maliyet parametreleri kullanılabilir. Bu parametrenin işaretlenmesi durumunda, belge kaydı sırasında birinci ek maliyet değeri girilebilecektir.

**Ek Maliyet \[1\] İsmi**

Ek Maliyet \[1\] parametresi işaretlendiğinde bu maliyete ait isim bilgisi girilir.

**Ek Maliyet \[1\] =Birim Ağırlık\*Nakliye Katsayısı Hesaplansın Mı**

Ek Maliyet \[1\] parametresi işaretlendiğinde, ilgili parameter aktif olmaktadır.

**Nakliye Tutarı=Stok Sabit Kayıtlarındaki Birim Ağırlık\* Stok Sabit Kayıtlarındaki Nakliye Tutarı\* Cari Hesap Kayıtlarındaki Nakliye Katsayısı alanlarına giriken değerlerle çarpılarak bulunup program tarafından Ek Maliyet \[1\] alanına getirilir. Hesaplanan değer üzerinde düzenleme yapılabilir.**

**Ek Maliyet \[1\] KDV Oranı**

Maliyet tutarının KDV’sinin, toplam KDV tutarına yansıtılması isteniyorsa, bu parametreye, ek maliyet üzerinden, % olarak hesaplatılacak KDV oranı girilir.

![](../_assets/1aecabea8a9bdfb4f2c4.png)

![](../_assets/47e741db92795940c79e.png)

Yukarıdaki Stok Kartı Kayıtları ve Cari Hesap Kayıtları ekranlarında görüldüğü gibi Birim Ağırlık: 2, Nakliye Tutar: 5 ve Nakliye Katsayısı: 2 girilmesi durumunda, girilen belge sonrasında Toplamlar sekmesinde Ek Maliyet \[1\] alanında Nakliye Masraf tutarının otomatik olarak 20 geldiği görülmektedir.

Hesaplanan nakliye tutarı: 2\*5\*2=20 TL olarak gelmektedir.

Ayrıca Ek Maliyet \[1\] için parametrelerde bir KDV oranı girilmişse bu nakliye tutarı üzerinden KDV hesaplaması yapılır. Örneğe göre KDV oranı:8 ise, hesaplanan KDV tutarı: 20\*0,08=1,6 TL’ dir.

![](../_assets/b493c063cddacb992487.png)
