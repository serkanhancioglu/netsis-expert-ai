---
title: "Ek-1 (Çek/Senet No Rehberi Kullanımı)"
page_id: "24740023"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Finans"
  - "Müşteri Çekleri"
  - "Ekler / Müşteri Çekleri"
  - "Ek-1 (Çek/Senet No Rehberi Kullanımı)"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Finans / Müşteri Çekleri / Ekler / Müşteri Çekleri / Ek-1 (Çek/Senet No Rehberi Kullanımı)"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTI4NGIyZDkwLWU0MGYtNGJkNS04YzZmLWIwM2I0Y2YyM2RhZSZsaW5rPWU5NmFkOWU0LWQwZWQtNDZhOS1iNTRiLTQ3OGU1NjY4NjQwMyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=284b2d90-e40f-4bd5-8c6f-b03b4cf23dae&link=e96ad9e4-d0ed-46a9-b54b-478e56686403&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ek-1-cek-senet-no-rehberi-kullanimi_34212209_24740023.html"
source_version: "2022-12-06T10:30:00.137+03:00"
source_bytes: 239414
fetched_at: "2026-09-13T04:11:36+00:00"
generator: "netsis-scraper 1.0.0"
---
# Ek-1 (Çek/Senet No Rehberi Kullanımı)

Çek senet no rehberi kullanımı hakkında ayrıntılı bilgiye bu dokümandan ulaşılır.

Programın genelinde ve en çok çek senet ile ilgili modüllerde sorgulanan ve çek/senet numarası alanlarının sağında bulunan rehber ![](../../../../_assets/088477bb321d1b20c939.jpg) butonuna basıldığında, çekler/senetler listelenmeden önce rehberde listelenecek çekler/senetler için kısıt verilen Çek Rehberi/Senet Rehberi başlıklı sorgulama ekranı görüntülenir.

![](../../../../_assets/306ac0a0daf9cff5cf1b.png)

Çek Rehberi ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Çek Rehberi Ekranı |  |
| --- | --- |
| Yer Kodu | Rehberde listelenmesi istenen çekler için yer kodu kısıdı verilen alandır. **Örneğin;** Rehberde sadece "Portföy" olan çeklerin listelenmesi istendiğinde "Portföy" seçeneğinin işaretlenmesi gerekir. Program, bazı işlemlerde "Yer Kodu" seçeneğini işaretli olarak ekrana getirir. **Örneğin;** Müşteri Çekleri → Kayıt → "Tahsil Hesabına Çek Cirosu" işleminde, "Yer Kodu" olarak "Portföy" seçeneği işaretli olarak ekrana gelir. Çünkü, tahsil hesabına sadece portföyde bulunan çekler gönderilir. Dekont → Kayıt → "Bankadan Gelen Karşılıksız Çek Dekontu" bölümünde rehber butonuna ![](../../../../_assets/088477bb321d1b20c939.jpg) basıldığında, "Yer Kodu" olarak "Tahsil" seçeneği işaretli olarak ekrana gelir. Çünkü, bu işlemin yapılacağı çeklerin daha önce banka tahsil hesabına gönderilmesi gerekir. |
| Durum Kodu | Rehberde listelenmesi istenen çekler için durum kodu kısıdı verilen alandır. **Örneğin;** Rehberde sadece durum kodu "Beklemede" olan çeklerin listelenmesi istendiğinde "Beklemede" seçeneğinin işaretlenmesi gerekir. Program, bazı işlemlerde "Durum Kodu" seçeneğini işaretli olarak ekrana getirir. **Örneğin;** Müşteri Çekleri → Kayıt → "Tahsil Hesabına Çek Cirosu" işleminde, "Durum Kodu" olarak "Beklemede" seçeneği işaretli olarak ekrana gelir. Çünkü, tahsil hesabına sadece beklemede olan çekler gönderilir. |
| Vade Tarihi Aralığı | Rehberde listelenmesi istenen çekler için tarih kısıdı verilen alandır. |
| Tutar Aralığı | Rehberde sadece belirlenen tutardaki çeklerin listelenmesi istendiğinde, ilgili tutar için aralık girilen alandır. |
| Veren Kodu | Rehberde sadece belirli bir cari hesaptan alınan çeklerin listelenmesi istendiğinde, ilgili cari hesabın girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile kodlar arasından seçim yapılır. |
| Verilen Kodu | Rehberde sadece belirli bir cari hesaba ya da banka hesabına ciro edilen çeklerin listelenmesi istendiğinde ilgili hesabın girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile kodlar arasından seçim yapılır. |
| Bankası | "Cari Hesap Çek Alındı Kaydı" işleminde "Bankası" alanına girilen çekin banka bilgisi için kısıt verilmesini sağlayan alandır. Rehberde, bu alana girilen bankaya ait çekler listelenir. |
| Numarası | Rehberde listelenmesi istenen çeklere ait banka hesap numaraları için kısıt verilen alandır. |
| Banka Bilgisi Basılacak Mı? | Rehberde çeklere ait banka bilgilerinin de listelenmesi için kullanılan seçenektir. |
| Çek Seri | Rehberde listelenmesi istenen çekler için seri numarası kısıdı verilen alandır. |
| Hesap No | Rehberde listelenmesi istenen çekler için hesap numarası kısıdı verilen alandır. |
| Dövizli Çekler/TL Çekler/Hepsi | Rehberde listelenmesi istenen dövizli ya da TL çekler için kısıt verilen alandır. Para birimi ne olursa olsun tüm çeklerin rehberde listelenmesi istendiğinde "Hepsi" seçeneğinin işaretlenmesi gerekir. |
| Döviz Tipi | "Dövizli Çekler" seçeneğinin işaretlenmesi ile aktif hale gelen alandır. Rehberde, seçilen döviz tipi ile girilen çekler listelenir. Alanın sağ tarafında bulunan rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, "Döviz Takibi" modülünde tanımlanan döviz tipleri izlenir. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Girilen bilgilerin onaylanması için kullanılan butondur. Butona basıldığında, "Çek/Senet Rehberi" ekrana gelir. ![](../../../../_assets/37fc305a8e57364fd0ea.png) |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | Girilen bilgilerden vazgeçilmesi halinde ekrandan çıkmak için kullanılan butondur. |
