---
title: "Konfigüratör Parametreleri"
page_id: "50663330"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Üretim"
  - "Kayıt/Üretim"
  - "Konfigüratör Tanımlamaları"
  - "Konfigüratör Parametreleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Üretim / Kayıt/Üretim / Konfigüratör Tanımlamaları / Konfigüratör Parametreleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTM4MGVkNmI2LWE5ZTQtNDcyZi1hYTM1LTQ1YzAxYzA1ZGY0MyZsaW5rPWZmZTU1NmUzLTBkNzktNGJkYi04MGI3LTQyMDI4ZjdkYzZkYiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=380ed6b6-a9e4-472f-aa35-45c01c05df43&link=ffe556e3-0d79-4bdb-80b7-42028f7dc6db&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "konfigurator-parametreleri_50663348_50663330.html"
source_version: "2022-10-13T11:47:00.173+03:00"
source_bytes: 15345
fetched_at: "2026-09-13T04:18:48+00:00"
generator: "netsis-scraper 1.0.0"
---
# Konfigüratör Parametreleri

Konfigüratör Parametreleri, Üretim modülünde Kayıt/Üretim menüsünün altında yer alır.

Konfigüratör Parametreleri ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| Konfigüratör Parametreleri Ekranı |  |
| --- | --- |
| Yönetici Mail | Ürün Konfigüratörü ekranında bir taslak onaya gönderildiğinde, ilgili kişilere mail gönderilir. Kime mail gönderileceği “Yönetici Mail” alanından tanımlanır. Birden fazla kişiye mail gönderilmesi için mail adreslerinin arasına “;” noktalı virgül girilmesi gerekir. |
| Ön Onay Sistemi | Satış teklifi aşamasında konfigürasyon taslaklarının Ön Onay’a gönderilmesi için kullanılan parametredir. Ürün Geliştirme birimi tarafından ürün taslakları kontrol edilir ancak bir değişiklik yapılamaz. Ön Onay'da kabul edilen bir taslak daha sonraki aşamada tekrar onaya gönderilebilir. “Ön Onay Sistemi” işaretlenmediği zaman ürün taslakları direkt onaya gönderilir. |
| Ürün Konfigürasyon Onaylamada Bağlantılı Satış Talepleri Güncellensin | Onaya gelen konfigürasyonda, konfigürasyon yeni bir tepe mamul stok kodu ile onaylandığında, sistem otomatik olarak bu konfigürasyonun bağlantılı olduğu satış talebindeki ilgili kalemin içinde önceden “KONFIG” yazan stok kodunu yeni verilen stok kodu ile günceller. Benzer şekilde bu parametrenin altında bulunan “Satış Teklifleri” ve “Müşteri Siparişleri” ile ilgili güncelleştirme parametrelerinde de aynı şekilde bağlantılı oldukları belge kalemlerindeki eski “KONFIG” stok kodlarını günceller. |
| Ürün Konfigürasyon Onaylamada Bağlantılı Satış Teklifleri Güncellensin | Onaya gelen konfigürasyonda, konfigürasyon yeni bir tepe mamul stok kodu ile onaylandığında, sistem otomatik olarak bu konfigürasyonun bağlantılı olduğu satış teklifindeki ilgili kalemin içinde önceden “KONFIG” yazan stok kodunu yeni verilen stok kodu ile günceller. |
| Ürün Konfigürasyon Onaylamada Bağlantılı Müşteri Siparişleri Güncellensin | Onaya gelen konfigürasyonda, konfigürasyon yeni bir tepe mamul stok kodu ile onaylandığında, sistem otomatik olarak bu konfigürasyonun bağlantılı olduğu müşteri siparişlerindeki ilgili kalemin içinde önceden “KONFIG” yazan stok kodunu yeni verilen stok kodu ile günceller. |
| Satış Talebinde Ürün Konfigüre Edilebilsin | "Satış Talebi" ekranında "Stok Kodu" alanına farenin sağ tuşu ile tıklandığında açılan listede “Ürün Konfigüratörü” bölümünün gelmesini sağlayan parametredir. Böylece, satış talebinde kullanılan ürünler konfigüre edilir. |
| Satış Teklifinde Ürün Konfigüre Edilebilsin | "Satış Teklifi" ekranında "Stok Kodu" alanına farenin sağ tuşu ile tıklandığında açılan listede “Ürün Konfigüratörü” bölümünün gelmesini sağlayan parametredir. Böylece, satış teklifinde kullanılan ürünler konfigüre edilir. |
| Müşteri Siparişinde Ürün Konfigüre Edilebilsin | "Müşteri Siparişi" ekranında "Stok Kodu" alanına farenin sağ tuşu ile tıklandığında açılan listede “Ürün Konfigüratörü” bölümünün gelmesini sağlayan parametredir. Böylece, müşteri siparişinde kullanılan ürünler konfigüre edilir. |
| Ön Onaya Gönderilen Taslak Reddedildiğinde Bağlantılı Belge Satırını Kapat | Ön onaya gelen bir belge reddedildiğinde, bağlantılı belge satırının otomatik olarak kapatılmasını sağlayan parametredir. |
| Konfigürasyonlarda Birliktelik Kontrolü Yapılsın | Ürün konfigüratörünün ana ekranındaki birliktelik kontrollerinin açılıp kapatılmasını sağlayan parametredir. |
| Hata Bulunduğunda Belgede Kullanılamasın/Onaya Gönderilemesin | Yapılan konfigürasyonda bir birliktelik hatası tespit edildiğinde konfigürasyonun belgede kullanılamamasını veya onaya gönderilememesini sağlayan parametredir. |
| Hata Bulunduğunda Konfigürasyon Onaylanamasın | Ürün onay aşamasında birliktelik kuralı ihlaliyle karşılaşıldığında ilgili konfigürasyonun onaylanamamasını sağlayan parametredir. |
| Birliktelik Seti Değişiminde Tek Kalan Alternatifin Otomatik Seçilmesi | Ürün Konfigüratörü ekranında birliktelik kuralı değiştirildiğinde, ilgili kurala uygun olan tek bir alternatif bileşen varsa otomatik olarak bu bileşenin seçilmesini sağlayan parametredir. |
| Ortak Özellikler Otomatik Değişsin | Ürün Konfigüratörü ekranında bir özelliğin değeri değiştirildiğinde aynı özelliğe sahip diğer reçete bileşenlerinin de ilgili özelliklerinin, aynı değere otomatik olarak geçişinin sağlanması için kullanılan parametredir. Değişiklik yapılacak bileşenin ilgili özelliğe karşılık gelen bir eşleşmesi yoksa (Stok kodu veya Yapılandırma Kodu yoksa), bu bileşenin YENI moduna geçer ve yeni açılacak stok kodunun bu özellik ile eşleştirilerek açılması gerekir. |
| Ürün Konfigüratörü Güncelleme Modunda Açılsın | Ürün Konfigüratörü açılırken otomatik olarak güncelleme modunda açılması için kullanılan parametredir. Normal şartlarda reçete ağacı üzerinde bir değişiklik yapıldığında, üst seviyedeki bileşenler otomatik olarak "Yeni" moduna geçer. Ekran güncelleme modunda açıldığında bu durum olmayarak direkt olarak üst bölümdeki "Bileşeni Güncelle" butonuna tıklanmış gibi reçete güncelleme modunda çalışır. Bu parametre sadece ürün konfigüratörününÜüretim modülünden açıldığı durumlarda çalışır. Güncelleme modu açıkken "Reçete Kontrol" ve "Bileşeni Güncelle" butonları pasif görünür. |
| ![](../../../../_assets/39d77b8716226638d9ce.jpg) Tamam | İşaretlenen parametrelerle ilgili işlemlerin gerçekleşmesini sağlayan butondur. Parametrelerle ilgili işlemlerin programa yansıması için programın kapatılıp tekrar açılması gerekir. |
| ![](../../../../_assets/973111d004995dca0113.jpg) İptal | İşaretlenen parametrelerden vazgeçilmesi halinde kullanılan butondur. |
