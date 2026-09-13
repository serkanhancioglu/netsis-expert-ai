---
title: "Entegrasyon Havuz Sistemi Kullanımı SSS"
page_id: "90673759"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Entegrasyon Havuz Sistemi Kullanımı SSS"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Entegrasyon Havuz Sistemi Kullanımı SSS"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWI1MmRkNzQ4LTE2YWItNDdjNS1hM2I0LWNjYzhjNzVlMGUzMyZsaW5rPTQ3YjU0OWUxLWEwMzYtNGUxZi1hOTg2LTIwMWM2MTZmNWI2ZiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=b52dd748-16ab-47c5-a3b4-ccc8c75e0e33&link=47b549e1-a036-4e1f-a986-201c616f5b6f&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "entegrasyon-havuz-sistemi-kullanimi-sss_90673759_90673759.html"
source_version: "2022-09-27T10:46:19.353+03:00"
source_bytes: 234102
fetched_at: "2026-09-13T04:23:52+00:00"
generator: "netsis-scraper 1.0.0"
---
# Entegrasyon Havuz Sistemi Kullanımı SSS

**Soru 1: Entegrasyon modülü menüler içerisinde gelmemektedir, ne yapılmalıdır?**

Gezgin\\Genel\\Yardımcı Programlar\\Kayıt\\Şirket- Şube Parametre Kayıtları ekranında ilgili şube için parametreler sekmesindeki muhasebe entegre parametresinin işaretli olması gerekmektedir.

![](../_assets/5c6dfc8c488619cef5ac.png)

**Soru 2: Entegrasyon havuz sistemi kapatılsın işaretli değil ise kayıtlar nasıl muhasebeleşmektedir?**

Entegrasyon havuz sistemi kapatılsın işaretli olmasa bile kayıtlar entegrasyon havuzuna düşmektedir. Seçenekli aktarma ile muhasebeleştirme işlemi yapılabilmektedir.

**Soru 3: Muhasebeye doğrudan aktarım yapılsın seçeneği işaretlenemiyor ise sebebi ne olabilir?**

Entegrasyon havuz sistemi kapatılsın parametresi işaretlendikten sonra muhasebeye doğrudan aktarım yapılsın parametresi işaretlenebilir.

**Soru 4: Entegrasyon havuz sistemi açık iken seçenekli aktarma sonrasında fiş basımı yapılabilir mi?**

Fiş basımı muhasebeye doğrudan aktarım yapılsın parametresi işaretli olduğunda yapılabilmektedir.

**Soru 5: Muhasebeye doğrudan aktarım yapılsın parametresi işaretli olmasına rağmen fiş basımı parametresi neden pasif gelir?**

Gün bazında aktarım parametresi işaretli ise fiş basımı yapılamamaktadır.

**Soru 6: İlgili belgeye girildiğinde muhasebeleşmesi yapılmasına rağmen üst bilgiler ekranında muhasebeleşmiş belge yazmamaktadır sebebi ne olabilir?**

Entegrasyon havuz sistemi kapatılsın işaretli değil ise oluşan muhasebe kaydı ile muhasebe arasında bağlantı oluşmamaktadır. Bu şekilde belgelerin muhasebe fişlerine ulaşılmak isteniyor ise entegrasyon havuz sistemi kapatılsın işaretli olmalı ya da entegrasyon havuz sistemi kapatılsın parametresi ile muhasebeye doğrudan aktarım yapılsın parametresi de işaretlenmelidir.

**Soru 7: Kullanıcı bazında bazı modüller ve menüler için online entegrasyon bazılarında ise entegrasyon havuz sistemine atılması sağlanabilir mi?**

SSO ekranında ilgili kullanıcı için hangi modüllerde nasıl işlem yapması isteniyor ise muhasebe doğrudan aktarım kolonu için ilgili değerin seçimi yapılabilir.

![](../_assets/5613c834b3158092da1c.png)

**Soru 8: Muhasebeye doğrudan aktar işaretli değil iken SSO üzerinden bir kullanıcı için muhasebe doğrudan aktarım evet seçilirse kayıtlar doğrudan muhasebeleşir mi?**

İlgili kişinin muhasebeye doğrudan kayıt atabilmesi için muhasebeye doğrudan aktar parametresinin muhakkak işaretli olması gerekmektedir.

**Muhasebeye Doğrudan Aktarım Yapılsın:** Tüm kullanıcı ve modüller için doğrudan aktarımın yapılıp yapılmayacağını gösteren genel ve varsayılan değerdir. Kullanıcı ve işlem bazındaki parametrelerde varsayılan seçeneği işaretlendiğinde, buradaki değere göre işlem yapılır.
