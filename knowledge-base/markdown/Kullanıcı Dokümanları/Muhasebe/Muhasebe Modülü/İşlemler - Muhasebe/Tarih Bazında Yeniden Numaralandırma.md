---
title: "Tarih Bazında Yeniden Numaralandırma"
page_id: "24740541"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Muhasebe"
  - "Muhasebe Modülü"
  - "İşlemler / Muhasebe"
  - "Tarih Bazında Yeniden Numaralandırma"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / İşlemler / Muhasebe / Tarih Bazında Yeniden Numaralandırma"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWJhNThlMmMxLWRiNTMtNDAzMy05ZTZhLWY2MTU2YWExYzY2ZCZsaW5rPTA5ODExOTUzLWZkNjktNDMyZi05ZmU4LTU2ZTYyODUwMDY3ZCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=ba58e2c1-db53-4033-9e6a-f6156aa1c66d&link=09811953-fd69-432f-9fe8-56e62850067d&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "tarih-bazinda-yeniden-numaralandirma_41157049_24740541.html"
source_version: "2022-10-06T11:17:55.877+03:00"
source_bytes: 38716
fetched_at: "2026-09-13T04:13:08+00:00"
generator: "netsis-scraper 1.0.0"
---
# Tarih Bazında Yeniden Numaralandırma

Tarih Bazında Yeniden Numaralandırma, Muhasebe Bölümünde, "İşlemler/Muhasebe Modülü" menüsünün altında yer alır. Tarih Bazında Yeniden Numaralandırma, ay bazındaki fiş kayıtlarının numara sırası, tarih sırasında değilse (geçmiş tarihlere ait fiş kayıtlarının sonraki numaralara aktarılması sırayı bozar) fişlerin tarih sırasında numaralandırılması için, yevmiye defteri basımı öncesinde (istendiği zaman) çalıştırılması gereken bölümdür. Tarih Bazında Yeniden Numaralandırma bölümü çalıştırıldıktan sonra, karışık tarihlerde girilen yevmiye fişlerinin numaraları değişir.

![](../../../../_assets/96ceaf12992a87d2f971.png)

Tarih Bazında Yeniden Numaralandırma ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Tarih Bazında Yeniden Numaralandırma Ekranı |  |
| --- | --- |
| Ay Kodu | Sıralanması istenen fiş numaraları için ay kodu girilen alandır. |
| İlk Fiş No | İlgili ay kodundaki fişlere verilmesi istenilen ilk numaranın girildiği alandır. Girilecek numara, bir önceki ayın son fiş numarasının bir fazlası olabilir. Fişler, verilen fiş numarası baz alınarak sıralanır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, yevmiye fiş numaralarına ulaşılır. |
| Fiş Tipi Bazında Numaralansın | Yeniden numaralandırma işleminin fiş tipi bazında yapılması için kullanılan seçenektir. Açılış, Tahsil, Tediye, Mahsup ve Kapanış olan fiş tipleri Yukarı![](../../../../_assets/b4e8b49186512aee23a1.png) ve Aşağı ![](../../../../_assets/551f4717c636667c2cca.png) butonları ile istenen şekilde sıralanarak, bu sıraya göre numaralandırma işlemi yapılmasını sağlar. |
| Değişen Fiş Numarası Açıklama-2’ye Atılsın | Tarih bazında numaralandırma yapıldığında, fişlerin numaraları değişir ve eski numaralardan bu fişlere ulaşmak zorlaşır. Bu seçeneğin işaretlenmesi ile, fişlerin eski numaraları "Açıklama-2" alanlarına aktarılır ve eski numaralardan ilgili fişlere ulaşmak kolaylaşır. |
| Değişen Fiş Numarası Açıklama-2 Boş İse Yazılsın | “Değişen Fiş Numarası Açıklama-2’ ye Atılsın" seçeneği işaretlendiğinde aktif hale gelen seçenektir. Bu seçeneğin işaretlenmesi ile, yevmiye fişlerinin "Açıklama-2" alanlarında herhangi bir bilgi varsa bu bilgiler bozulmaz. Bazen, tarih bazında numaralandırma işlemi yapıldıktan sonra geriye dönük yevmiye fişleri girilebilir. Böyle bir durumda, numaralandırma işlemi tekrar çalıştırıldığı zaman “Açıklama-2 Boş İse Yazılsın” seçeneği işaretli değilse, "Açıklama-2" alanlarına aktarılan eski fiş numaraları bozulur. İşaretli ise; eski numaralar bozulmaz ve sadece, sonradan kaydedilen fişlerin "Açıklama-2" alanları boş bırakılacağı için bu fişlerin "Açıklama-2" alanlarına eski fiş numaraları aktarılır. |
| Şubeler Dahil Mi? | Tarih bazında yeniden numaralandırma işlemine şubelerin dahil edilmesi istendiğinde kullanılan seçenektir. |
| Sadece Merkez Şube için Çalışsın | "Şubeler Dahil Mi?" seçeneği işaretli değil iken aktif hale gelen seçenektir. Tarih bazında yeniden numaralandırma işleminin sadece merkez şube için çalışması istendiğinde kullanılan seçenektir. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilginin onaylanmasını sağlayan butondur. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgiden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
