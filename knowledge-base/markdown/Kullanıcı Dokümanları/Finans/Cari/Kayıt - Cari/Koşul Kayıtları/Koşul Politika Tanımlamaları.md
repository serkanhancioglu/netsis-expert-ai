---
title: "Koşul Politika Tanımlamaları"
page_id: "22805114"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Cari"
  - "Kayıt / Cari"
  - "Koşul Kayıtları"
  - "Koşul Politika Tanımlamaları"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Cari / Kayıt / Cari / Koşul Kayıtları / Koşul Politika Tanımlamaları"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWQ0YWU3MGFkLWNkY2YtNDQ0Mi04N2I0LTc3N2IwOGQyMjJjOCZsaW5rPTdiMjBhOThkLTE0YmEtNGE4Yi1iMTA3LTNhMmFkMDRkMGM1NiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=d4ae70ad-cdcf-4442-87b4-777b08d222c8&link=7b20a98d-14ba-4a8b-b107-3a2ad04d0c56&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "kosul-politika-tanimlamalari_28155450_22805114.html"
source_version: "2022-10-27T11:30:40.143+03:00"
source_bytes: 84303
fetched_at: "2026-09-13T04:07:46+00:00"
generator: "netsis-scraper 1.0.0"
---
# Koşul Politika Tanımlamaları

Koşul Politika Tanımlamaları, Finans Bölümü'nde Kayıt/Cari menüsünün altında yer alır. Bu bölümde yazılacak Visual Basic script’ i ile, "Ek Koşul Kayıtları" bölümünde "İlave Şekli" ile uygulanacak politikalardan daha geniş kapsamlı politika tanımlaması yapılabilir.

Koşul Politika Tanımlamaları bölümünün aktif olması için, Finans → Cari → Kayıt → Cari Parametreleri → "Koşul Politika Tanımlaması Yapılsın" parametresinin işaretlenmesi gerekir.

"Koşul Politika Tanımlaması" bölümünde belirlenen vade günü, iskonto ve fiyat gibi bilgilerin belgelere getirilmesi isteniyorsa, bu bilgilerin bulunduğu detay koşulların mutlaka "Ek Koşul Kayıtları" yapılmalı ve bu ek koşulların belge üzerindeki cari kod için geçerli olması gerekir.

**Örneğin:** Bir firmanın tanımlı olan detay koşullarının aşağıdaki gibi olduğu ve müşterinin İzmir'de olduğu düşünüldüğünde, Haziran ayında mal satışı yapıldığında her üç koşul da geçerli hale gelir. Koşul politika tanımlamaları ile bu koşullardan hangilerinin ne şekilde kullanılacağı belirlenir.

| Koşul Kodu | Koşul Kapsamı | Sat.İsk.1 |
| --- | --- | --- |
| K10 | Türkiye Geneli Kampanya | 10 |
| K20 | Ege Bölgesi Kampanyası | 12 |
| K30 | Yaz Kampanyası | 5 |

Aşağıdaki ekranda yapılan politika tanımlaması sonucunda, geçerli koşulların 1. satır iskontolarının ortalaması hesaplanarak, belgeye yine 1. satır iskontosu olarak getirilmesi sağlanır. Buna göre, yukarıda örneği verilen müşteriye ait belgelerde, 1. satır iskontosu oranı 9 ((10+12+5)/3) olarak ekrana gelir.

![](../../../../../_assets/c1bb2aefbba246e1bb74.png)

Yukarıda tanımlanan script, fatura belgesinin her satırında, bir program parçacığı gibi, baştan sona çalışır. Script içerisinde kullanılan “DetSayısı” ile, "Detay Koşul Kayıtları" bölümünde tanımlanmış ve ilgili cari hesap için ek koşul olarak girilmiş koşul sayısı ifade edilir. Ek koşullarla belirlenmiş olan bu detay koşulların tümü, program parçacığı içerisinde aktiftir ve “KosulDetaylar” dizisinin içinde bulunur. Script içinde kurulan döngü ile, bu ek detay koşullar (“KosulDetaylar” dizisi), baştan sona kontrol edilir. Bu döngü içinde, "KosulDetaylar" dizisinin her bir elemanı, “AktifDetay” değişkenine aktarılır. "AktifDetay" olarak atanan detay koşulun, 1. iskonto oranı “Isk” değişkenine eklenir. Böylece, tüm ek detay koşulların 1. iskonto oranları toplamı alınır. Döngü sonunda, belgede girilen koşulun da 1. iskonto oranı, toplama eklenir. Bunun sebebi, belgede girilmiş olan koşulun, ek koşul olarak tanımlanmış olsa dahi, "KosulDetaylar" dizisinin içinde bulunmamasıdır. Yazılan script ile, belgede girilen koşul kodu için belirlenen 1. satır iskontosu ve bu belgede girilen cari hesaba "Ek Koşul Kayıtları" bölümünden bağlanmış koşullar için detay koşulda belirlenen 1. satır iskontoları toplanır. Bulunan değerin toplam geçerli koşul sayısına bölünmesi ile, ortalama 1. satır iskontosu oranı hesaplanır.

Koşul Politika Tanımlamaları ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Koşul Politika Tanımlamaları Ekranı |  |
| --- | --- |
| ![](../../../../../_assets/4463b36aacf10587495e.png) Nesne Tarayıcısı | Nesne tarayıcısı butonu, koşul politika tanımlaması esnasında kullanılacak nesnelerin izlenmesini sağlar. Butona basıldığında, "Nesne Tarayıcısı" başlıklı bir ekran görüntülenir. Bu ekranda politika tanımlarken kullanılacak alanlar bulunur. Koşul Politika Tanımlamasında, "Detay Koşul" ve Ek Koşul Kayıtları" bölümünde bulunan alanlar kullanılarak politika tanımlaması yapılır. ![](../../../../../_assets/ee8ba322d207c00e547d.png) |
| ![](../../../../../_assets/295cfaf5b973345b1bce.png) Kod İçeriği | Kod içeriği (Ctrl-Space) butonu, Script editor içerisinde kullanılan nesnelerin yardım pencerelerinin ekrana getirilmesini sağlar. Yani, script editörde nesne ismi yazılıp yanına “.” Nokta işareti konup, ctrl-space tuşlarına basıldığında, ya da araç çubuğundan bu fonksiyon çağrıldığında, nesnenin içerdiği alanlar bir pencerede gösterilir ve alanların içinden seçim yapılır. ![](../../../../../_assets/f9792866395023cebb4e.png) |
| ![](../../../../../_assets/cdbbe91745c5df19bc45.png) Kod Tamamlama | Kod tamamlama (kod içeriği aktif ise enter) butonu; Script editor içerisinde, nesne ismi yazılıp kod içeriği penceresi aktif halde iken kullanılmak istenen alan isminin başlangıç harf/harfleri yazıldığında, kod içeriği imleci ilgili alanın üzerine gider ve klavyeden "Enter" tuşuna basıldığında (bu fonksiyon çalıştırıldığında)kullanılmak istenen alanın tam adının otomatik olarak ekrana getirilmesini sağlar. |
| ![](../../../../../_assets/c79b7873a39c84349697.png) Satıra Git | Satıra Git butonu, koşul politika ekranı üzerinde istenilen satıra gitmek için kullanılır. Bu butona basıldığında açılan ekranda, imlecin hangi satıra gitmesi istendiği program tarafından sorulur. |
| ![](../../../../../_assets/c132a04433c009673a2f.png) Bul, Sonraki Arama, Önceki Arama ve Değiştir Butonu | Sırasıyla bul, sonraki arama, önceki arama, değiştir butonları yardımıyla, ekranda girilen script içinde istenilen karakter dizisi aratılabilir (Bul), birden fazla yerde geçmesi halinde sırayla her birinin üzerine gidilebilir (Sonraki Arama/Önceki Arama) ya da script içinde geçen herhangi bir değerin farklı bir değerle değiştirilmesi (Değiştir) sağlanabilir. |
| ![](../../../../../_assets/ee111bf6ceea60e23bb1.png) Yükle Ve Kaydet Butonu | Yükle ve kaydet butonları, koşul politika tanımı editöründe aktif değildir. |
