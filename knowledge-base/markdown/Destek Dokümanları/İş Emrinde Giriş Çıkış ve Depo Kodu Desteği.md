---
title: "İş Emrinde Giriş Çıkış ve Depo Kodu Desteği"
page_id: "50667342"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "İş Emrinde Giriş Çıkış ve Depo Kodu Desteği"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / İş Emrinde Giriş Çıkış ve Depo Kodu Desteği"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTgxZGVkNTE2LWNhOTQtNGZiNC04YjZmLTc5OWIzZjkyYmM3OSZsaW5rPWQ5ZGZmZmIzLWY0MDMtNGU3ZS1hNmIxLTYzYmNjYzBjYTViYyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=81ded516-ca94-4fb4-8b6f-799b3f92bc79&link=d9dfffb3-f403-4e7e-a6b1-63bccc0ca5bc&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "is-emrinde-giris-cikis-ve-depo-kodu-destegi_82575456_50667342.html"
source_version: "2022-11-03T09:08:05.603+03:00"
source_bytes: 390812
fetched_at: "2026-09-13T04:25:39+00:00"
generator: "netsis-scraper 1.0.0"
---
# İş Emrinde Giriş Çıkış ve Depo Kodu Desteği

İş Emrinde Giriş Çıkış ve Depo Kodu Desteği ile ilgili ayrıntılı bilgiye bu dokümandan ulaşabilirsiniz.

İş Emri ve iş emrine bağlı Reçete Kaydı ekranında bileşen bazında giriş-çıkış depo kodu desteği getirilmiştir.

![](../_assets/eea9a87d2679d4d04333.png)

Depo Kodları iş emrine öndeğer olarak, Üretim Parametreleri-üretim yapılan Depo Kodu (Öndeger) parametresinden getirilir ve değiştirilebilir.

![](../_assets/3ae8eaffc4f7e3780b7d.png)

İş emrine bağlı reçetedeki bileşenler için de farklı depo kodları tanımlanır.

![](../_assets/2cfbc1c652898fe8ed39.png)

Buradaki depo kodları içi, iş emri ana bilgisinde Üretim Sonu kaydı sırasında, iş emrinde girilen depo kodlarının kullanılması için depo önceliği seçeneği eklenmiştir.

**![](../_assets/8d1d55c9375335431686.png)**

**Hiçbiri**: ÜSK ekranından girilen depo kodlarına işlem yapılır. ÜSK ekranına depo kodları, öndeğer olarak üretim parametrelerinden getirilir.

**Stok Depo Kullan**: Stok kartında girilen depo koduna, mamul için giriş deposu, bileşen için çıkış deposu olarak işlem yapılır. Stok kartında depo kodu yoksa "**Hiçbiri"** seçeneği çalışır.

**İş Emri Depo Kullan**: Mamul ve bileşenler için iş emrinde girilen depolara işlem yapılır. İş emrinde depo kodu yoksa **"Hiçbiri"** seçeneği çalışır.
