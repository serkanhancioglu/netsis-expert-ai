---
title: "İleri Üretim Planlamada Geçiş Miktarı Politikası"
page_id: "166396046"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "İleri Üretim Planlamada Geçiş Miktarı Politikası"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / İleri Üretim Planlamada Geçiş Miktarı Politikası"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTAyNTFhMGJjLTU0ZWMtNGFkNC04ZDFjLTMzYTFjNjFlZjE3YSZsaW5rPTRhNjA2NDg0LTM0MDAtNDJiOC05MzgwLWQzNGRkY2FkMTgyYiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=0251a0bc-54ec-4ad4-8d1c-33a1c61ef17a&link=4a606484-3400-42b8-9380-d34ddcad182b&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ileri-uretim-planlamada-gecis-miktari-politikasi_166396052_166396046.html"
source_version: "2025-02-18T10:48:27.323+03:00"
source_bytes: 13312
fetched_at: "2026-09-13T04:22:16+00:00"
generator: "netsis-scraper 1.0.0"
---
# İleri Üretim Planlamada Geçiş Miktarı Politikası

Bu dokümanda ileri üretim planlama uygulamasında geçiş miktarı politikası üzerinde bir çizelgeleme örneğine yer verilmiştir.

**Tek** **Parça** **Akışı** **(One-Piece** **Flow):** Yalın üretim yöntemlerinden biri olan Tek Parça Akışı veya Sürekli Akış, her bir üretim aşamasında yalnızca bir ürünün veya parçanın işlenmesi ve bir sonraki aşamaya geçmesi ilkesine dayanan bir üretim yöntemidir. Herhangi bir iş merkezinde parçanın nihai halini alması için gereken makinelerin, üretim akışına bağlı olarak birbiri ardına yerleştirilmesi ve parçanın bir önceki proses için kullanılan makineden sonraki proses için kullanılacak makineye beklemeden geçmesidir. Bu yöntem, iş gücünü daha verimli kullanmak ve üretim hatlarında bekleme sürelerini ortadan kaldırmak amacıyla tercih edilmektedir.

**Parti Üretimi (Batch Production):** Belirli bir sayıda ürünün aynı anda üretildiği bir üretim yöntemidir. Bu yöntemde, belirli bir üretim miktarı (parti) tamamlanana kadar gruplar halinde üretim yapılır. Batch Production, belirli ürünlerin ya da aynı türdeki ürünlerin büyük miktarlarda üretildiği ve sonrasında işlem sırasına göre sıralandığı bir yapıyı ifade eder. Belirli gruplar halindeki parçalar sürecin bir aşamasından geçer ve ardından üretimin sonraki aşaması için sırada bekler. Parti ne kadar büyükse, her bir sonraki sürece geçmeden önce partinin geri kalanının tamamlanması için o süre boyunca beklenir.

İleri üretim çizelgeleme uygulamasında desteklenen geçiş miktarı politikası ile tek parça akışı yönteminde olduğu gibi ürünlerin birer birer veya parti üretim yöntemi gibi gruplar halinde sıradaki operasyona geçiş miktarları belirlenebilir.

Operasyon tanımlama ekranında bulunan **"Geçiş** **Miktarı"** alanında 2 seçenek bulunmaktadır. Geçiş miktarı elle girilebilir ya da "Otomatik Hesaplansın" parametresi açılabilir. Buraya girilecek değer, tanımlanmakta olan operasyon tamamlandıktan sonra, ürünlerin sıradaki operasyona kaç birimlik yığınlar halinde geçeceğini belirlemektedir. Bu alanda geçiş miktarının hiç tanımlanmamış olması durumda ise, ilgili iş emrinin tamamının bitmesi beklenecek şekilde çizelgeleme yapılacaktır. Yani parti miktarı, operasyon miktarı kadar işlem görecektir.

Aşağıdaki görselde, sürekli akış ve parti üretimi yöntemlerine yönelik bir süreç şeması yer almaktadır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/015412b6-cd8a-4b97-9503-2829906f9286/MS_GMP_1.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/af9d8fdd-7706-4391-8baa-cf9fab381f8d/MS_GMP_2.png)

Aşağıdaki örnek uygulamada, belirli hammaddeler sırasıyla 3 aşamadan geçerek son ürün halini almaktadır. Bu ürünler için PROCESS_01 \> PROCESS_02 \> PROCESS_03 işlem sırasıyla rota tanımları yapılmıştır.

Üretim süreleri ve geçiş miktarı tanımları aşağıda verilmiştir. Ürün bazında üretim süresi ve geçiş miktarı/süreleri,

"Operasyon-Makine Eşleştirme" ekranından tanımlanır.

Bu veriler doğrultusunda:

MAMUL001 stoğu için 10 adetlik üretimde işlem gören parçaların, PROCESS_01'den PROCESS_02'ye geçişi sırasında 10 adetin tamamlanması beklenecektir.

MAMUL002 stoğunda ise geçiş miktarı 5 adet olduğundan, 5'er adetlik yığınlar halinde PROCESS_02'ye geçiş yapılacaktır. MAMUL003 stoğunda ise her bir parçanın işlemi tamamlandıktan sonra beklemeden PROCESS_02'ye geçiş yapılacaktır.

| **Ürün** **Kodu** | Operasyon Kodu | Makine Kodu | Üretim Süresi | **Üretim Süresi** **Tipi** | Üretim Miktarı | **Üretim Miktarı**<br>**Tipi** | **Geçiş Tanım** **Tipi** | **Geçiş**<br>**Miktarı/Süresi** | Geçiş Birimi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MAMUL001 | PROCESS_01 | MAK_101 | 60 | Saniye | 1 | Ölçü Br-1 | Miktar | 0 | Ölçü Br-1 |
| MAMUL001 | PROCESS_02 | MAK_102 | 60 | Saniye | 1 | Ölçü Br-1 | Miktar | 0 | Ölçü Br-1 |
| MAMUL001 | PROCESS_03 | MAK_103 | 60 | Saniye | 1 | Ölçü Br-1 | Miktar | 0 | Ölçü Br-1 |
| MAMUL002 | PROCESS_01 | MAK_201 | 60 | Saniye | 1 | Ölçü Br-1 | Miktar | 5 | Ölçü Br-1 |
| MAMUL002 | PROCESS_02 | MAK_202 | 60 | Saniye | 1 | Ölçü Br-1 | Miktar | 5 | Ölçü Br-1 |
| MAMUL002 | PROCESS_03 | MAK_203 | 60 | Saniye | 1 | Ölçü Br-1 | Miktar | 5 | Ölçü Br-1 |
| MAMUL003 | PROCESS_01 | MAK_301 | 60 | Saniye | 1 | Ölçü Br-1 | Miktar | 1 | Ölçü Br-1 |
| MAMUL003 | PROCESS_02 | MAK_302 | 60 | Saniye | 1 | Ölçü Br-1 | Miktar | 1 | Ölçü Br-1 |
| MAMUL003 | PROCESS_03 | MAK_303 | 60 | Saniye | 1 | Ölçü Br-1 | Miktar | 1 | Ölçü Br-1 |

Geçiş miktarı ile ilgili yapılan tanımların, ileri üretim çizelgelemede dikkate alınabilmesi için çizelge modelindeki algoritma opsiyonlarından **"Geçiş Miktarı Politikası"** seçeneği **"Dikkate Alınsın"** olarak belirlenmelidir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/7d324c5e-942f-41a3-8606-2b2933ad5105/MS_GMP_3.png)

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/84824d0e-0445-40bd-84d9-aa2b97958c7c/MS_GMP_4.png)

Çizelgeleme sonucunda;

WS_01 istasyonunda MAMUL001, WS_02 istasyonunda MAMUL002,

WS_03 istasyonunda MAMUL003 son ürünlerinin hat üzerindeki akışı aşağıdaki gibi görüntülenir.

Bu doğrultuda, MAMUL001'in toplam sistemde kalma süresi 30 dakika, MAMUL002'nin toplam sistemde kalma süresi 20 dakika, MAMUL003'ün sistemde kalma süresi ise 12 dakika olarak hesaplanır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/5235fb1f-faf9-42c3-80d9-ece012544375/MS_GMP_5.png)
