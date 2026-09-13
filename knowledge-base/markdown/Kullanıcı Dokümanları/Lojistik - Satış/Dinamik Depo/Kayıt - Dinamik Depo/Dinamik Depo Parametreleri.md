---
title: "Dinamik Depo Parametreleri"
page_id: "22803878"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Dinamik Depo"
  - "Kayıt / Dinamik Depo"
  - "Dinamik Depo Parametreleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Dinamik Depo / Kayıt / Dinamik Depo / Dinamik Depo Parametreleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTM1NDEzMzZhLTgzZjktNGYxNy1iM2IwLWUyMDZlYTg4YTgzYiZsaW5rPTZjYzJhZjM3LTIxZjUtNGNjMi1iNjQ0LTNiZmFlNGE1ZTE4MiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=3541336a-83f9-4f17-b3b0-e206ea88a83b&link=6cc2af37-21f5-4cc2-b644-3bfae4a5e182&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "dinamik-depo-parametreleri_34211703_22803878.html"
source_version: "2022-11-01T09:43:28.370+03:00"
source_bytes: 12305
fetched_at: "2026-09-13T04:06:14+00:00"
generator: "netsis-scraper 1.0.0"
---
# Dinamik Depo Parametreleri

Dinamik Depo Parametreleri, Dinamik Depo-Kayıt menüsünün altında yer alır. Dinamik Depo Parametreleri, Dinamik Depo kayıtları sırasında kullanılacak özel uygulamaların sağlandığı bölümdür.

Dinamik Depo Parametreleri ekranında yer alan parametreler ve içerdiği bilgiler şunlardır:

| Dinamik Depo Parametreleri Ekranı |  |
| --- | --- |
| Seri Bilgisi Depoda Sorulsun | Stokta seri/lot takibi yapılıyorsa, Fatura modülündeki giriş ve çıkış belgelerinde, seri/lot numaraları sorgulanır. Stok seri bilgilerinin, bu belgeler üzerinde sorgulanmayıp, Dinamik Depo modülünde, yerleştirme veya toplama sırasında sorgulanması isteniyorsa **Seri Bilgisi Depoda Sorulsun** parametresinin işaretlenmesi gerekir. Aksi halde stok serileri, Dinamik Depo modülünde değil Fatura modülünde sorgulanacaktır. |
| İrsaliyeler İle Kayıtlar Tutsun | İrsaliye/faturalardaki miktarlar ile, depoya yerleştirilen/toplanan miktarların eşit olması ve kontrolünün yapılması için **İ****rsaliyeler İle Kayıtlar Tutsun** parametresinin işaretlenmesi gerekir. Parametrenin işaretlenmemesi durumunda miktar kontrolü yapılmaz. |
| Ürün Hacim Grubu Kontrolü Yapılsın | Dinamik Depo modülünde, mallar hacimlerine göre gruplanır ve raflara hangi hacim gruplarındaki malların yerleştirilebileceği tanımlanır. **Ürün Hacim Grubu Kontrolü Yapılsın** parametresi işaretlendiğinde, stok kartlarında girilen hacim kodları kontrol edilerek, stokların ait olmadığı bir raf grubuna yerleştirilmeleri engellenir. **Ürün Hacim Grubu Kontrolü Yapılsın** parametresi işaretlenmemiş ise, stoklar farklı hacim gruplarına yerleştirilir. Örneğin; A rafına küçük hacimli ürünlerin, B rafına büyük hacimdeki ürünlerin yerleştirilmesinin planlandığı varsayıldığında, parametre işaretlenmiş ise, küçük hacimli ürünler B rafına hiçbir zaman yerleştirilemez. |
| Bir Hücreye Aynı Mal Grubu Ürün Yerleştirilsin | Bir hücreye yeni bir mal yerleştirilirken, aynı hücreye daha önceden yerleştirilen ürünün mal grubuyla aynı olması isteniyorsa **Bir Hücreye Aynı Mal Grubu Ürün Yerleştirilsin** parametresinin işaretlenmesi gerekir. Eğer bir hücreye farklı mal grubu ürünlerin yerleştirilmesi isteniyorsa **Bir Hücreye Aynı Mal Grubu Ürün Yerleştirilsin** parametresinin işaretlenmemesi gerekir. Örneğin; A rafının 1 numaralı hücresine makarna grubu bir ürün yerleştirildiği varsayıldığında, parametre işaretlenmiş ise, 1. numaralı hücreye makarna grubu dışında bir ürün yerleştirilemez. |
| Kapasite Kontrolü Yapılsın | **Kapasite Kontrolü Yapılsın** parametresi işaretlendiğinde, tanımlı raf hacmi kontrol edilecek ve kapasitenin üstünde yerleştirme yapılmasına izin verilmez. **Kapasite Kontrolü Yapılsın** parametresi işaretlenmemişse, kapasite kontrolü yapılmaz. |
| Bakiye Kontrolü Yapılsın | Çıkış işlemlerinde, hücrede olmayan veya hücrede olan miktarlardan fazla çıkış yapılması istenmiyorsa **Bakiye Kontrolü Yapılsın** parametresinin işaretlenmesi gerekir. **Bakiye Kontrolü Yapılsın** parametresi işaretlenmemişse, bakiye kontrolü yapılmaz ve hücrede olmayan ürünlerin çıkışına izin verilir. |
| Brüt/Net Kg. Takibi Yapılacak | Tartılı ürünlerde, ürünün birlikte tartıldığı darası düşülerek net miktarların hesaplanması ve bu net miktarların depo kayıtlarına işlenmesi istendiğinde **Brüt/Net Kg. Takibi Yapılacak** parametresinin işaretlenmesi gerekir. **Brüt/Net Kg. Takibi Yapılacak** parametresi işaretlendiğinde, depo hareketlerinde, miktar bilgisi girildikten sonra gelen ekranda, netten brüte ya da brütten nete hesaplatma yapılabilir. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | İşaretlenen parametrelerle ilgili işlemlerin gerçekleşmesini sağlayan butondur. Parametrelerle ilgili işlemlerin programa yansıması için programın kapatılıp tekrar açılması gerekir. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | İşaretlenen parametrelerden vazgeçilmesi halinde kullanılan butondur. |
