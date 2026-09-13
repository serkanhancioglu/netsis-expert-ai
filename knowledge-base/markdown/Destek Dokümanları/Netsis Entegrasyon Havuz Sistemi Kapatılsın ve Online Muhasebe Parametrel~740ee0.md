---
title: "Netsis Entegrasyon Havuz Sistemi Kapatılsın ve Online Muhasebe Parametrelerinin Kullanımı"
page_id: "90673762"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Netsis Entegrasyon Havuz Sistemi Kapatılsın ve Online Muhasebe Parametrelerinin Kullanımı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Netsis Entegrasyon Havuz Sistemi Kapatılsın ve Online Muhasebe Parametrelerinin Kullanımı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTBkY2EwMWFiLWNjMTAtNDY5MC04NjBjLTY4OGJmYzgwMGQ1ZSZsaW5rPWJmZjFhY2M5LTMxMTgtNDU5My1hNGJhLTM4ZWE2ZmQzN2U0NCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=0dca01ab-cc10-4690-860c-688bfc800d5e&link=bff1acc9-3118-4593-a4ba-38ea6fd37e44&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "netsis-entegrasyon-havuz-sistemi-kapatilsin-ve-online-muhasebe-parametrelerinin-kullanimi_90673783_90673762.html"
source_version: "2022-11-02T14:14:16.953+03:00"
source_bytes: 1773374
fetched_at: "2026-09-13T04:23:54+00:00"
generator: "netsis-scraper 1.0.0"
---
# Netsis Entegrasyon Havuz Sistemi Kapatılsın ve Online Muhasebe Parametrelerinin Kullanımı

Netsis Entegrasyon Havuz Sistemi Kapatılsın ve Online Muhasebe Parametrelerinin Kullanımı ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

Netsis 3 Entegre, Netsis 3 Standard, Netsis 3 Enterprise ve Netsis Wings Enterprise ürünlerimiz ile; hem genel hem de kullanıcı ve işlem bazında belirlenebilecek parametrelere göre, yapılan işlemlerin entegrasyon havuzu üzerinden muhasebeleştirilmesi ya da entegrasyon havuzuna atılmadan doğrudan muhasebeye aktarılabilmesi sağlanabilir.

Entegrasyon havuzunun istenen şekilde kullanılmasını ya da devre dışı bırakılmasını sağlamak için, Muhasebe\\Entegre\\Kayıt\\Entegrasyon Kodları ekranındaki parametrelerden seçim yapılmalıdır.

Entegrasyon Havuz Sistemi Kapatılsın: Doğrudan muhasebeleştirme fonksiyonlarının kullanılabilmesi için, Entegrasyon Havuz Sistemi Kapatılsın parametresinin işaretlenmesi gerekir. Entegrasyon Havuz Sistemi Kapatılsın parametresi işaretliyken, doğrudan aktarımın yanı sıra, bazı işlemler için entegrasyon havuzu kullanılmaya devam edilebilir. Entegrasyon Havuz Sistemi Kapatılsın parametresi işaretlenmezse, doğrudan muhasebeleştirme fonksiyonları kullanılamaz.

Muhasebeye Doğrudan Aktarım Yapılsın: Muhasebeye Doğrudan Aktarım Yapılsın, tüm kullanıcı ve modüller için doğrudan aktarımın yapılıp yapılmayacağını gösteren genel ve varsayılan değerdir. Kullanıcı ve işlem bazındaki parametrelerde varsayılan seçeneği işaretlendiğinde, buradaki değere göre işlem yapılır.

![](../_assets/fb29f70b28f8fe20b438.png)

![](../_assets/49e745c677310c8d7ace.png)

İki parametrenin çalışma şekillerini örneklerle inceleyelim.

1-Her iki parametrenin de işaretli olmaması durumunda;

![](../_assets/70327e4bc61c19ee6926.png)

Belge girişi yapılır.

![](../_assets/3b97cee5f470636ad8da.png)
İlgili belgeye ait muhasebesel kayıtlar entegrasyon havuzuna düşer.

![](../_assets/4da73c6493ee3b154c9a.png)

Seçenekli aktarma ile yevmiye fişi oluşturulur.

![](../_assets/3fcc848eafd30c991bb9.png)

Belgeye tekrar girildiğinde muhasebeleşmiş belge gibi belge üzerinden muhasebe detayına gidilemez.

Belge üzerinde düzeltme yapılmamalıdır. Yapılması durumunda entegrasyonda 4 veya 5 tipli kayıtlar oluşacaktır. Mutlaka düzeltme yapılması gerekiyor ise öncelikle yevmiye fişi silinmeli sonrasında entegrasyon kayıtlarından tipi 1 veya 2 olarak değiştirilip tekrar seçenekli aktarma yapılmalıdır.

![](../_assets/3ec822bc58dc46a1164c.png)

2-Entegrasyon havuz sistemi kapatılsın işaretli, Muhasebeye doğrudan aktarım yapılsın işaretli değil ise;

![](../_assets/8e87d0451cc602a934d5.png)

Belge girişi yapılır.

![](../_assets/b5fbdec1f5620b1d6e2c.png)

İlgili belgeye ait muhasebesel kayıtlar entegrasyon havuzuna düşer. Seçenekli aktarma ile yevmiye fişi oluşturulur.

![](../_assets/ac614e77e4a8f1bb0fa9.png)

Muhasebeleştirme yapıldıktan sonra belgeye tekrar girildiğinde belgenin muhasebe ile bağlantısı oluşur ve yevmiye kaydına doğrudan belge üzerinden gidilebilir.

![](../_assets/679ccf9f1e23eba91bdf.png)![](../_assets/b228001b1f8758cc68ba.png)

![](../_assets/d55680d8003a9708a8af.png)

Belge üzerinde düzeltme yapılmamalıdır. Yapılması durumunda entegrasyonda 4 veya 5 tipli kayıtlar oluşacaktır. Mutlaka düzeltme yapılması gerekiyor ise öncelikle yevmiye fişi silinmeli sonrasında entegrasyon kayıtlarından tipi 1 veya 2 olarak değiştirilip tekrar seçenekli aktarma yapılmalıdır.

3-Entegrasyon havuz sistemi kapatılsın işaretli, Muhasebeye doğrudan aktarım yapılsın işaretli ise;

![](../_assets/7e0654747f2b2f1b46ea.png)

İlgili belge girişi yapılır. Entegrasyon kayıtlarına muhasebe kayıtları gitmez, doğrudan yevmiye fişi olarak kayıt atılmaktadır. Belge üzerinden yevmiye fişine ulaşılabilir.

![](../_assets/9571c184b01574953d96.png) ![](../_assets/51f7d568c673260d5aff.png)

![](../_assets/e1250d7e1ba14994a14b.png)

Belge üzerinde değişiklik yapıldığında ise bu değişiklik yevmiye fişine yansıyacaktır.
