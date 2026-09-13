---
title: "Döviz İsimleri Tanımlama"
page_id: "24753648"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Genel"
  - "Döviz Takibi"
  - "Kayıt / Döviz Takibi"
  - "Döviz İsimleri Tanımlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Genel / Döviz Takibi / Kayıt / Döviz Takibi / Döviz İsimleri Tanımlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTgxMjBkMDZjLWM4MjktNDg2Mi1iMTk5LTA3Y2ZiYWMyODE0OSZsaW5rPTY2N2YxY2RhLTdlYWMtNGE5Ni1hOWRhLTE4NzkxZTU4ZjJhNyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=8120d06c-c829-4862-b199-07cfbac28149&link=667f1cda-7eac-4a96-a9da-18791e58f2a7&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "doviz-isimleri-tanimlama_24753666_24753648.html"
source_version: "2022-09-19T15:49:23.393+03:00"
source_bytes: 36115
fetched_at: "2026-09-13T04:18:31+00:00"
generator: "netsis-scraper 1.0.0"
---
# Döviz İsimleri Tanımlama

Döviz İsimleri Tanımlama, Genel Bölümü'nde, "Kayıt/Döviz Takibi" menüsünün altında yer alır. Dövizli işlemler sırasında kullanılacak veya geriye yönelik takibi yapılacak kur bilgilerinin döviz tipleri girilir. Girilen her bir döviz tipine program tarafından sıra numarası verilir. Bu dövizlere ait kur bilgileri girildikten sonra, döviz isimlerinde değişiklik yapılmaması gerekir.

**Örneğin;** İlk sırada yer alan USD açıklaması silinerek yerine DM yazılmaması gerekir. Çünkü, sıra anlık değişmiş gibi görünür fakat geriye yönelik kur bilgileri değişmez.

![](../../../../_assets/1ce927dd4a0f6382bcf3.png)

Döviz İsimleri Tanımlama ekranında yer alan alanlar ve içerdiği bilgiler aşağıdaki şekildedir:

| Döviz İsimleri Tanımlama Ekranı |  |
| --- | --- |
| Sıra | Tanımlanan döviz cinsinin sıra numarasının girildiği alandır. Girilen her bir döviz tipine program otomatik olarak sıra numarası verir. Tanımlanan dövizlere ait kur bilgileri girildikten sonra, döviz isimlerinde değişiklik yapılmaması gerekir. Programın entegre bölümlerinde döviz cinsi belirleme ile ilgili sorgulamalarda, bu alanda girilecek sıra numarasına göre belirleme yapılır. **Örneğin;** Dolar döviz cinsinin sıra numarası 1 olarak girildiğinde, bundan sonra herhangi bir bölümde döviz cinsi belirlerken "Dolar" cinsini kullanmak için döviz tipi değerinin 1 olarak girilmesi gerekir. |
| Birim | Günlük kur girişinde, döviz için girilecek kur biriminin belirlendiği alandır. Genelde değer "1" olarak girilir. Program genelinde döviz ile ilgili yapılan işlemlerde kur hesaplaması, günlük kur girişinde yazılan kur değeri ile "Birim" alanına yazılan değer çarpılarak yapılır. **Örneğin;** Kur girişinde 1,3 yazılıp "Birim" alanına 2 değeri girildiğinde, modüllerde bu döviz tipi için kur 2,6 ((1,3)\*2) olarak hesaplanır. |
| Döviz İsmi | Tanımlaması yapılan döviz cinsinin isim bilgisinin girildiği alandır. |
| Netsis Sıra Numarası | Günlük kur bilgilerinin programdan girilmesine gerek kalmadan, Netsis’ten bu bilgiler temin edilebilir. "Döviz İsimleri Tanımlama" bölümünden gerekli bağlantılar yapıldığında, kur bilgileri günlük olarak Netsis’ten kullanılan şirketin "Döviz Kurları Girişi" bölümüne aktarılır. Bu işlemin gerçekleştirilmesi için online veya modem ile, internet bağlantısının olması gerekir. "Döviz İsimleri Tanımlama" ekranında “Netsis Sıra Numarası” alanında tanımlama yapılması gerekir. Bu alanda Netsis’in döviz isimleri sırası bulunur. Her firmanın, kendi döviz sıraları ile Netsis’in döviz sırasını eşitlemesi gerekir. **Örneğin;** Bir firmanın Euro değerinin 3. sırada tanımlandığı varsayıldığında, firmanın, Euro değerini grid ekrandan farenin sol tuşu ile çift tıklayarak kayda hazır hale getirmesi gerekir. Daha sonra "Netsis Sıra Numarası" alanının sağ tarafında yer alan rehber butonundan faydalanarak Euro değerinin, Netsis’teki sırasından bulunarak farenin sol tuşu ile tıklanması ve \<tab\> butonuna basılarak kaydedilmesi gerekir. Böylece firmada 3. sırada tanımlı olan Euro için Netsis’in 20. sıradaki tanımının birbiriyle bağlantısı oluşur. Aynı işlemin "Merkez Bankası" kurlarıyla güncellenmesi istenen diğer döviz tiplerine de uygulanması gerekir. Netsis sıra numarası verilmemiş döviz tipleri için kur güncellemesi yapılmaz. |

Döviz İsimleri Tanımlama ekranında ilgili kayıtlar girildikten sonra “Kaydet” ![](../../../../_assets/865524a70e225c89c107.jpg) butonu ile kayıt tamamlanır. Açılan bir kayıt, kayıt sil ![](../../../../_assets/2df4b343310bcd16b01e.jpg)butonu ile iptal edilir veya üzerinde değişiklik yapılması için kaydet ![](../../../../_assets/865524a70e225c89c107.jpg) tuşu kullanılarak düzeltilir.
