---
title: "İşlem Sırası Tanımlama"
page_id: "24748847"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Muhasebe"
  - "Maliyet Muhasebesi"
  - "Kayıt / Maliyet Muhasebesi"
  - "İşlem Sırası Tanımlama"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Maliyet Muhasebesi / Kayıt / Maliyet Muhasebesi / İşlem Sırası Tanımlama"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTE4NTM4NGJiLTIzYmQtNGY2Yy05M2JkLTNkZWJmNTE2OGI0ZCZsaW5rPTMyOTdjOTJhLTViMTYtNGM3OS1iNTY4LWY1ODQwZmQwNTllNyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=185384bb-23bd-4f6c-93bd-3debf5168b4d&link=3297c92a-5b16-4c79-b568-f5840fd059e7&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "islem-sirasi-tanimlama_50675270_24748847.html"
source_version: "2022-10-17T14:28:50.847+03:00"
source_bytes: 45514
fetched_at: "2026-09-13T04:14:55+00:00"
generator: "netsis-scraper 1.0.0"
---
# İşlem Sırası Tanımlama

İşlem Sırası Tanımlama, Muhasebe Bölümü'nde, "Kayıt/Maliyet Muhasebesi Modülü" menüsünün altında yer alır. İşlem Sırası Tanımlama, Maliyet Muhasebesi modülünde kullanılacak işlem sırasının tanımlanmasını sağlayan bölümdür.

İşlem Sırası Tanımlama ekranında yer alan alanlar ve içerdiği bilgiler şunlardır:

| İşlem Sırası Tanımlama Ekranı |  |
| --- | --- |
| Sıra No | İşlem sırasının numarasının girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, sıra numaralarına ulaşılır. 1 rakamından başlayarak tanımlanır. Bu bölümdeki örneklerde, ilk sıraya 1 numaralı aşamanın girilmesi gerekir. Çünkü, önce yarı mamullerin maliyetleri bulunur daha sonra mamul maliyetine geçilir. |
| Ana Grup Kodu | Maliyet Ana Maliyet Grubu kodunun girildiği alandır. İlgili bilgi girilmeden önce maliyet ana grup kodlarının mutlaka önceden tanımlanması gerekir. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, grup kodlarına ulaşılır. |
| Şube Kodu | Bir ana mamul/yarı mamul grubuna ait üretim işlemlerinin tamamı, merkez şirket dışındaki şubelerden birinde yapıldığında, maliyet hesaplaması sırasında sadece bu şubede işlem yapılmasını sağlamak için, şube numarasının girildiği alandır. Böylece, maliyet hesaplaması sırasında, ilgili ana grubun maliyet hesapları için sadece tek şubeden işlem yapılmasını, diğer şubeler için tarama yapılmamasını ve böylece işlemin hızlanmasını sağlar. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, şube kodlarına ulaşılır. Örneğin; MM1’in üretiminde, önce 1. Aşama Maliyet Ana Grup Kodu işlem görerek YM1 ve YM2’nin maliyeti hesaplanıyor ve bu işlemden sonra MM1’in üretimine bu yarı mamuller sarf ediliyor. YM1 ve YM2’nin maliyetinin hesaplanması için burada 1 numaralı maliyet ana grup kodunun 1 numaralı sıraya, MM1’in üretimi için 2 numaralı maliyet ana grup kodunun 2. sıraya girilmesi gerekir. Safha üretiminde öncelik sırası tanımlanmamışsa, maliyet hesaplamalarında karışıklık oluşur ya da bazı sarf tutarları sarf mahsubuna yansıtılmaz. |
| Lokal Depo Kodu | Maliyet hesaplaması sırasında işlem yapılacak lokal depo kodunun girildiği alandır. Rehber butonu ![](../../../../_assets/088477bb321d1b20c939.jpg) ile, depo kodları arasından seçim yapılır. |
| Safha Adedi | Üretim yapılırken, hammaddeden mamule kadar geçirilen seviye sayısının girildiği alandır. Safhalar ana grup kodu bazında belirlenir. Eğer aynı ana grup kodu altında birden fazla safha adedi belirleniyorsa, en büyük safha girilir. **Örneğin;** Bir firmanın mamul üretim aşaması aşağıdaki gibi olsun. ![](../../../../_assets/2b0e54e3df333270e089.jpg) H1 ve H2 hammaddeleri Yarı Mamul 1’i, H3 hammaddesi de Yarı Mamul 2’yi oluştursun. Hammaddelerden mamule kadar üretim ve çıkışlardan yapılan stok hareket kayıtlarının performansı ile program mamul maliyetine ulaşıncaya kadar olan aşamaları hammaddeden başlayarak, Hammadde - Yarı Mamul - Mamul olarak sıralar. Buradaki mamulü içerecek şekilde, tanımlanan ana maliyet koduna göre safha adedinin, ilgili sahaya 3 (üç) olarak girilmesi gerekir. Safha adedine, en geniş maliyet safha aşaması olan mamule göre giriş yapılması gerekir. Program önce hammadde maliyetlerini stok hareket kayıtlarının çıkışını baz alarak hesaplar ve yarı mamullere işler. Daha sonraki turda ise yarı mamullerin maliyetlerini mamule kaydederek mamulün maliyetini hesaplar. Bu tür yöntemle işlem gören firmalarda dikkat edilmesi gereken konu; aynı ana maliyet gruplarında değişik aşamalı ve değişik safha adedi olan mamuller için en geniş üretim aşaması olan mamul baz alınarak safha adedinin girilmesidir. Diğer durumlarda yani safha adedi konusunda yapılacak bir hatada, mamule malın maliyeti yanlış ve eksik olarak yansır. |

İlgili kayıtlar girildikten sonra “Kaydet” ![](../../../../_assets/865524a70e225c89c107.jpg) butonu ile kayıt tamamlanır. Açılan bir kayıt, kayıt sil ![](../../../../_assets/2df4b343310bcd16b01e.jpg)butonu ile iptal edilir veya üzerinde değişiklik yapılması için kaydet ![](../../../../_assets/865524a70e225c89c107.jpg) tuşu kullanılarak düzeltilir.
