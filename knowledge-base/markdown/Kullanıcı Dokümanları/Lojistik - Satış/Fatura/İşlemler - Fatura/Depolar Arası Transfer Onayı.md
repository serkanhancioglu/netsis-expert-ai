---
title: "Depolar Arası Transfer Onayı"
page_id: "24764093"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Fatura"
  - "İşlemler / Fatura"
  - "Depolar Arası Transfer Onayı"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Fatura / İşlemler / Fatura / Depolar Arası Transfer Onayı"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTYwMTFkZjQzLWI5YTktNDM5My1hZTllLTMyYWEyYzA5NzJmYSZsaW5rPTQxMDgyZjg2LTg4ZmMtNDFjYS05NWE2LTcwMDg4MDE2MDRkNSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=6011df43-b9a9-4393-ae9e-32aa2c0972fa&link=41082f86-88fc-41ca-95a6-7008801604d5&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "depolar-arasi-transfer-onayi_24764145_24764093.html"
source_version: "2022-10-24T21:26:28.170+03:00"
source_bytes: 182985
fetched_at: "2026-09-13T04:02:50+00:00"
generator: "netsis-scraper 1.0.0"
---
# Depolar Arası Transfer Onayı

Depolar Arası Transfer Onayı, Lojistik - Satış Bölümü'nde, "İşlemler/Fatura" menüsünün altında yer alır.

Depolar Arası Transfer Onayı, şubeler veya lokal depolar arası transfer kayıtlarının gönderildiği şube/lokal depo için onaylanarak stok hareket kayıtlarına giriş olarak işlenmesi amacıyla kullanılan bölümdür.

Depolar Arası Transfer Onayı işleminin çalıştırılabilmesi ve karşı ambardan onaylanmadığı sürece stok hareket kayıtlarına işlenmemesi için öncelikle, Satış Parametrelerindeki “Şubeler Arası Transfer Fişi Karşı Ambardan Onaylansın" parametresinin işaretlenmiş olması gerekir. Parametrenin işaretlenmesiyle birlikte “Bu Parametre Kullanıldığında, Depolar Arası Transfer Fişinde Düzeltme ve İptal İşlemi Yapılamaz” uyarısı ekrana gelir. Böylece, girilen "Depolar Arası Transfer" fişleri onaylanmadığı sürece, fişlerde değişiklik/iptal yapılabilir. Bu parametrenin işaretlenmesinden sonra kesilen "Depolar Arası Transfer" kayıtlarında, işlemin yapıldığı depodan çıkışlar stok hareket kayıtlarına işlenir ve giriş hareketleri ise 0 (sıfır) olarak aktarılır. Böylece, "Depolar Arası Transfer" kayıtlarından kaynaklanan giriş hareketlerinden dolayı stok miktarlarında değişiklik olmaz.

"Depolar Arası Transfer" kayıtlarından kaynaklanan giriş miktarlarının stok hareket kayıtlarına girişlerinin yapılması için mutlaka "Depolar Arası Transfer Onayı" bölümünden onaylanması gerekir. Onaylama işlemi, **lokal depolar arası transfer** yapılmışsa işlemin yapıldığı şirket veya şubede, **şubeler arası transfer** işlemi yapılmışsa stok hareketlerine giriş yapılacak olan yerde yapılır.

**Örneğin:** Şubeler Arası Transfer Fişi, Merkezden Şube 1’e yapılmışsa, onay işlemi de Şube 1’e geçilerek yapılır.

Depolar Arası Transfer Onayı ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Depolar Arası Transfer Onayı Ekranı |  |
| --- | --- |
| Onayla/Onayı Geri Al | Depolar arası transfer onayı için "Onayla", transfer onayının geri alınması için "Onayı Geri Al" seçeneğinin seçildiği alandır. |
| Lokal Depo | Onaylama işlemi, **lokal depolar arası** yapılan bir transfer işlemi için yapılacaksa işaretlenmesi gereken alandır. **Şubeler arası** bir transfer işlemi onaylanacak ise bu alan işaretlenmez. |
| İrsaliye No | "Lokal Depo" alanı işaretlenmişse, ![](../../../../_assets/088477bb321d1b20c939.jpg) rehber butonuna basıldığında onaylanmamış "Lokal Depolar Arası Transfer" kayıtları listelenir. "Lokal Depo" alanı işaretlenmemişse, merkez veya şubelerden yapılan onaylanmamış "Depolar Arası Transfer" kayıtları listelenir. ![](../../../../_assets/088477bb321d1b20c939.jpg)Rehber butonu yardımıyla onaylanacak irsaliye numaraları arasından seçim yapılır. |
| Cari Kodu | Şubeler arası yapılan depolar arası transfer kayıtlarında, cari kod alanına girilmiş olan kod, bu alana program tarafından otomatik olarak aktarılır. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | Tamam butonuna basılmasıyla birlikte, verilen kısıtlara uygun olan transfer kaydının detay ekranı görüntülenir. ![](../../../../_assets/60c55eb56f4f591f3619.png) Ekranda görüntülenen fiş, onaylanması istenen fiş ise tekrar Tamam ![](../../../../_assets/39d77b8716226638d9ce.jpg) butonuna basılır ve işlem tamamlanır. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | "Depolar Arası Transfer Onayı" için ekrana girilen bilgilerin iptal edildiği butondur. |
