---
title: "Montaj Hattı Dengeleme"
page_id: ""
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Montaj Hattı Dengeleme"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Montaj Hattı Dengeleme"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWQ3NTAxODM5LTdkM2UtNDJiMS1iYzAzLWQzNzRlOTlhYjczNCZsaW5rPWI1NjJlN2FlLWNkYTYtNGEzMy05NDJiLTYxOWMwOTgzY2FiYyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=d7501839-7d3e-42b1-bc03-d374e99ab734&link=b562e7ae-cda6-4a33-942b-619c0983cabc&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "montaj-dengeleme-hatti.html"
source_version: ""
source_bytes: 14790
fetched_at: "2026-09-13T04:21:51+00:00"
generator: "netsis-scraper 1.0.0"
---
# Montaj Hattı Dengeleme

Montaj hattı dengeleme ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

İlgili özelliğin anlatımını içeren video kaydını izlemek için aşağıdaki bağlantıya tıklayınız:

[Montaj Hattı Dengeleme](https://youtu.be/4zCo1fQGTsg?si=U_0Ya2FhgOlyPwSl) (YouTube – Logo Destek)

Montaj Hattı Dengeleme (Assembly Line Balancing), bir üretim hattı üzerindeki operasyonların, belirlenen çevrim süresi ve öncül-ardıl ilişkileri korunarak iş istasyonlarına en verimli şekilde dağıtılması sürecidir. Bu uygulama, üretim hattının verimliliğini artırmayı, darboğazları önlemeyi ve kaynak kullanımını optimize etmeyi amaçlar. Özellikle iş istasyonları arasındaki süre farklarını azaltarak operatör ve makinelerin boşta bekleme sürelerini minimuma indirmek, belirlenen çevrim süresine ulaşmak için gerekli olan minimum iş istasyonu sayısını belirlemek ve iş yükünü istasyonlar arasında dengeli dağıtarak bir istasyonun aşırı yüklü çalışmasını (darboğaz oluşumunu) ve diğerinin beklemede kalmasını önlemek hedeflenmektedir.

Aşağıdaki örnek uygulamada, Netsis üzerinde kurgulanan bir montaj hattı dengeleme senaryosu ele alınmıştır. Analiz sonucunda, her bir operasyonun işlem süresi ve öncül–ardıl ilişkileri dikkate alınarak hat üzerindeki iş istasyonlarının minimum sayıda açılması hedeflenmektedir.

| Operasyon Kodu | İşlem Süresi (sn) | Öncül Operasyonlar |
| --- | --- | --- |
| 1 | 12 | --- |
| 2 | 24 | --- |
| 3 | 42 | 1 |
| 4 | 6 | 1, 2 |
| 5 | 18 | 2 |
| 6 | 6.6 | 3 |
| 7 | 19.2 | 3 |
| 8 | 36 | 3, 4 |
| 9 | 16.2 | 6, 7, 8 |
| 10 | 22.8 | 5, 8 |
| 11 | 30 | 9, 10 |
| 12 | 7.2 | 11 |

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/716828db-f44e-48df-81f5-8d2dcc860a11/MS_MHD_1_oncelik_diyagrami_1.png)

Görsel 1) Öncelik Diyagramı

Hat dengeleme çalıştırabilmesi için aşağıdaki işlem adımları sırasıyla gerçekleştirilmelidir:

**1. Mamul Reçetesinin Tanımlanması**

*Menü: Gezgin\\Üretim\\Üretim\\Kayıt\\Reçete Kaydı*

Üretilecek mamul veya yarı mamulün reçetesi tanımlanır.

**2. İstasyon Tanımlanması**

*Menü: Gezgin\\Üretim\\MRP\\Kayıt\\İleri Üretim Çizelgeleme\\İş İstasyonu Tanımlama*

Üretim hattındaki iş istasyonları tanımlanır.

**3. Montaj Hattı Tipli Makine Tanımlanması**

*Menü: Gezgin\\Üretim\\MRP\\Kayıt\\İleri Üretim Çizelgeleme\\Makine Tanımlama*

Üretimin gerçekleşeceği makine "Montaj Hattı" tipiyle tanımlanır. Bu makine tipinin seçilmemesi durumunda, "Montaj Hattı Dengeleme" ekranındaki makine rehberinde ilgili makine görüntülenemeyecektir.

**4. Operasyon Tanımlanması**

*Menü: Gezgin\\Üretim\\MRP\\Kayıt\\İleri Üretim Çizelgeleme\\Operasyon Tanımlama*

a. Montaj Operasyonunun Tanımlanması

b. Alt Operasyonların Tanımlanması

**5. Rotanın Tanımlanması ve Rota-Ürün Eşleşmesi**

*Menü: Gezgin\\Üretim\\MRP\\Kayıt\\İleri Üretim Çizelgeleme\\Rota Tanımlama*

Üretim için gerekli operasyon akış sırası belirlenir ve rota ile ürün ilişkilendirilir.

**6. Operasyon-Makine Eşleştirmelerinin Yapılması**

*Gezgin\\Üretim\\MRP\\Kayıt\\İleri Üretim Çizelgeleme\\Operasyon - Makine Eşleştirme*

Hangi operasyonun hangi makinelerde yapılabileceği, üretim ve çevrim süreleri tanımlanır.

**7. Operasyon Öncül-Ardıl İlişkilerin Belirlenmesi ve Alt Operasyon Sürelerinin Tanımlanması**

*Menü: Gezgin\\Üretim\\MRP\\Kayıt\\İleri Üretim Çizelgeleme\\Montaj Hattı Dengeleme*

Her bir alt operasyonun süresi ve hangi operasyonun diğerinden önce bitmesi gerektiği (öncelik ilişkisi) belirlenir.

**8. Montaj Hattı Dengeleme Çalıştırılması**

*Menü: Gezgin\\Üretim\\MRP\\Kayıt\\İleri Üretim Çizelgeleme\\Montaj Hattı Dengeleme*

Hat dengeleme işlemi ile tanımlanan operasyon süreleri ve öncelik ilişkileri dikkate alınarak, montaj hattındaki iş istasyonlarına optimum operasyon dağılımı yapılır ve hat çevrim süresi hesaplanır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/a6362e33-7d83-4bf7-9e02-abb2fff83a2e/MS_MHD_2_makine_tanimlama.png)

Görsel 2) Makine Tanımlama

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/d81c3125-e184-4086-99df-32173aa90d45/MS_MHD_3_operasyon_tanimlama.png)

Görsel 3) Operasyon Tanımlama

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/a3388858-41fb-4904-9cc5-581304aa8ee4/MS_MHD_4_operasyon_tanimlama.png)

Görsel 4) Operasyon Tanımlama

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/a2faaa6b-2434-44dd-b91e-13ae0b701a11/MS_MHD_5_rota_tanimlama.png)

Görsel 5) Rota Tanımlama ve Rota Eşleştirme

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/ffc743cc-f7cf-4d77-ac11-a54978983109/MS_MHD_6_operasyon_makine_eslesmesi.png)

Görsel 6) Operasyon-Makine Eşleştirmeleri

## Montaj Hattı Dengeleme

Hat dengeleme çalıştırılması için *Gezgin \> Üretim \> MRP \> Kayıt \> İleri Üretim Çizelgeleme \> Montaj Hattı Dengeleme* yolu izlenir. Bu ekranda, her operasyon için o iş bittikten sonra başlayabilecek operasyonlar (ardıl) tek tek seçilir ve operasyon süreleri girilir. Operasyon süreleri ve ardıl ilişkileri içeren montaj hattı tasarımı oluşturulduktan sonra **“Kaydet”** butonu ile veriler kaydedilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/e12360b2-4454-441f-aed3-9074a5297006/MS_MHD_7_montaj_hatti_dengeleme.png)

Görsel 7) Montaj Hattı Tasarımı

Kayıt işlemi tamamlandıktan sonra ekranın sağ alt köşesinde bulunan **"Montaj Hattı Dengeleme"** butonu tıklanarak dengeleme sekmesine geçilir. Açılan ekranda yer alan **"Hat Dengele"** butonu ile dengeleme işlemi başlatılır.

Hat Dengeleme, tanımlanan 12 operasyonu ve 60 saniyelik hedef çevrim süresini dikkate alarak en uygun istasyon dağılımını belirlemek amacıyla algoritmayı eş zamanlı olarak çalıştırır:

- Largest Candidate Rule (LCR)
- Ranked Positional Weights (RPW)
- Kilbridge and Wester's Method (KWM)

Her bir yöntem (LCR, RPW ve KWM) için ayrı ayrı **Hat Verimliliği (Line Efficiency)** değeri hesaplanır. Eğer algoritmalar arasında dengeleme verimliliği aynı çıkarsa minimum çevrim süresini veren yöntem seçilerek üretim akış hızı maksimize edilir.

## İstasyon Yerleşimi ve Yeni Çevrim Süresi Hesaplaması

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/f484f9e7-d339-4dfc-b590-d3fe6b5c6e10/MS_MHD_8_dengeleme_sonucu.png)

Görsel 9) Hat Dengeleme Sonucu

Hat dengeleme sonucunda, toplam 12 operasyon, öncelik ilişkileri korunacak şekilde 5 ayrı iş istasyonuna dağıtılmıştır. Aşağıdaki tabloda, dengeleme sonrası her bir operasyonun hangi iş istasyonuna atandığı detaylı olarak gösterilmektedir.

| İstasyon No | Operasyon | Süre |
| --- | --- | --- |
| İstasyon 1 | MS01, MS03 | 54.0 |
| İstasyon 2 | MS02, MS04, MS05, MS06 | 54.6 |
| İstasyon 3 | MS08, MS07 | 55.2 |
| İstasyon 4 | MS10, MS09 | 39.0 |
| İstasyon 5 | MS11, MS12 | 37.2 |

Detay Bilgileri sekmesinde tüm operasyonların standart süreleri, istasyon bazlı gruplandırılmış şekilde tablo görünümünde incelenebilir.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/5bcf6e75-de45-4072-88ee-100a2ee154ca/MS_MHD_9_dengeleme_sonucu.png)

Görsel 9) Hat Dengeleme Sonucu

Hesaplanan yeni çevrim süresi, “Kaydet” butonu ile “Operasyon-Makine Eşleştirmeleri” ekranına otomatik olarak aktarılır.

![](https://dys.logo.cloud/asset/cdd87e13-3009-4dd1-a5b8-2a005c0e58da/219997d8-4017-4202-a6c6-b37461da3040/MS_MHD_10_yeni_cevrim_süresi.png)

Görsel 10) Hesaplanan Çevrim Süresi
