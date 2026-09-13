---
title: "Muhasebe Parametreleri / Muhasebe"
page_id: "24740852"
product: "netsis-3-enterprise"
depth: 7
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Muhasebe"
  - "Muhasebe Modülü"
  - "Ekler / Muhasebe"
  - "Ek-1 Enflasyon Muhasebesi"
  - "Muhasebe Modülü Tanımlamaları"
  - "Muhasebe Parametreleri / Muhasebe"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / Ekler / Muhasebe / Ek-1 Enflasyon Muhasebesi / Muhasebe Modülü Tanımlamaları / Muhasebe Parametreleri / Muhasebe"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTMzOTFjMTlkLTFmZjAtNGI4Ni04YzdiLTE5MDNmNGUyNDRmOSZsaW5rPWY4NTgyNTkzLThhNGMtNDdjYS1iODY5LWVlMzA1NjQ2MmQxMyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=3391c19d-1ff0-4b86-8c7b-1903f4e244f9&link=f8582593-8a4c-47ca-b869-ee3056462d13&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "muhasebe-parametreleri-muhasebe_41162281_24740852.html"
source_version: "2022-12-12T16:26:11.217+03:00"
source_bytes: 7419
fetched_at: "2026-09-13T04:14:31+00:00"
generator: "netsis-scraper 1.0.0"
---
# Muhasebe Parametreleri / Muhasebe

Muhasebe Parametreleri ile ilgili ayrıntılı bilgiye bu dokümandan ulaşılabilir.

**Ana Uygulama**

**Enflasyon Muhasebesi:** Sadece Vergi Usul Kanununda öngörüldüğü şekliyle enflasyon muhasebesi yapılacağı zaman (aynı zamanda "SPK Uygulaması" yoksa) işaretlenmesi gereken parametredir.

**IAS29:** Sadece SPK uygulamasına göre enflasyon muhasebesi yapılacağı zaman işaretlenmesi gereken parametredir.

**Enflasyon Muhasebesi + IAS 29 :** Hem Vergi Usul Kanununda öngörüldüğü şekliyle hem de "SPK Uygulamasına" göre enflasyon muhasebesi yapmak isteyen firmaların işaretlemesi gereken parametredir.

**Enflasyon Muhasebesi (VUK) İle IAS 29 (SPK) Arasındaki Farklar:**

Uygulamada en temel farklılık, sabit kıymet ve amortisman hesaplarının işleyişindedir. IAS29 uygulamasında, amortismanlar için Kıst uygulanması zaruridir ve sabit kıymetlerin tükenme süreleri farklıdır. Enflasyon Muhasebesi (VUK) uygulamasında ise Kıst, sadece binek otolarda uygulanır. Firmalar, bu konuda önceden uyguladıkları metotla amortisman ayırmaya devam edebilir. Bu temel farklılık sadece sabit kıymet ve amortisman hesaplarını değil, maliyet ve gider hesaplarını da etkiler.

Logo Netsis uygulamasında ise en temel farklılık; IAS29 (SPK) uygulamasının ikinci defter (enflasyon defteri) şeklinde yapılması ve Enflasyon Muhasebesi (VUK) uygulamasının ise tamamen TL kayıtlar ile, enflasyon düzeltmelerinin enflasyon fark hesaplarına işlenmesi suretiyle yapılmasıdır. Her iki uygulamanın bulunduğu firmalarda, IAS29 uygulaması ile ilgili düzeltmeler ikinci defterde, VUK uygulaması ile ilgili düzeltmeler ise enflasyon fark hesaplarından takip edilir.

**Toplulaştırılmış Yöntem:** Stok hesapları için toplulaştırılmış yöntem uygulanıp uygulanmayacağı belirlenir.

**Enf.Muh:** VUK uygulamasına göre toplulaştırılmış yöntem çalıştırılacağı anlamına gelir.

**IAS29:** SPK uygulamasına göre toplulaştırılmış yöntem çalıştırılacağı anlamına gelir.

**Enflasyon Muhasebesi + IAS29:** Her iki uygulamada da toplulaştırılmış yöntemler kullanılır.

**Hiçbiri:** Toplulaştırılmış yöntem uygulanmayacağı, enflasyona göre düzeltilmiş değerlerin stok ve maliyet hesaplarına ön muhasebeden (Stok ve Maliyet Muhasebesi Modüllerinden) geleceği düşünülür. Ancak, bir önceki parametrede Enflasyon Muhasebesi + IAS29 seçeneği belirlenmişse, "Toplulaştırılmış Yöntem" parametresinde bu seçenek geçerli olmaz. Çünkü, ön muhasebede (Stok ve Maliyet Muhasebesi Modüllerinden) her iki uygulama için düzeltilmiş değerler bulunmaz. Düzeltilmiş maliyetlerini bulmak isteyen firmalar; uygulamalarının birinde "Detay", diğerinde ise "Toplulaştırılmış Yöntem" tercih etmek durumundadır. Bu durumda "Toplulaştırılmış Yöntem" uygulamak için, Enflasyon Muhasebesi ya da IAS29 seçeneklerinden birinin işaretlenmesi gerekir.

**Enflasyon Kar/Zararı Parasal Hesaplardan/Parasal Olmayan Hesaplardan:**

Enflasyon Muhasebesi kullanıldığı zaman iki şekilde parasal kar/zarar değerine ulaşılabilir.

**Örneğin;**

Öncelikle, parasal olmayan hesapların düzeltme farklarının bulunup parasal kar/zarar değerine ulaşması sağlanır. Daha sonra, aynı değerin parasal hesapların değerlenmesiyle ne şekilde bulunacağı anlaşılır.

Uygulamada parasal olmayan hesaplar tercih edilirse, düzeltme sırasında sadece parasal olmayan hesapların düzeltmeleri yapılarak düzeltmelerden kaynaklanan fark parasal kar/zarar hesabına aktarılır. Vergi Usul Kanununda önerilen yöntem bu şekildedir. "Parasal Hesaplardan" seçeneği, parasal ve parasal olmayan tüm hesapların düzeltilmesini sağlar. Parasal hesaplar nominal değerlerine geri çekilir ve geri çekme sırasında oluşan farklar parasal kar/zarar hesabına aktarılır. Sermaye Piyasası Kanununda, her iki yöntem geçerlidir. Her iki yöntemde de sonuç değişmez. İkinci yöntemde, parasal hesaplardaki düzeltmeden kaynaklanan kazanç/kayıplar izlenebilir. Parametrelerde, IAS29 ya da Enflasyon Muhasebesi + IAS29 seçenekleri işaretlendiğinde, "Parasal Hesaplardan" seçeneği geçerli hale gelir ve bu şekilde çalışma sadece IAS29 (SPK) uygulamasında yapılır.

**Enflasyon Düzeltme Hesabı (698):** 5024 sayılı VUK ile kullanılmaya başlandı. Parasal olmayan kıymetlerin düzeltilmesi sonucu oluşan farkların kaydedildiği hesaplardır. Enflasyon fark hesapları ile karşılıklı çalışır. Programdaki işlemler sırasında, yapılan her türlü düzeltme işleminde karşılık olarak çalışacak hesap kodudur. Tüm düzeltme işlemleri, ilgili hesap kodlarına detaylı olarak aktarılır. Parasal olmayan aktif kalemlerin enflasyona göre düzeltilmesi sonucu ortaya çıkan artışlar, ilgili hesabın alacağına, parasal olmayan pasif kalemlerdeki artışlar ise borcuna yazılır. Gelir tablosu kalemlerinin düzeltilmesi ile ortaya çıkan farklar da "Enflasyon Düzeltme Hesabına" kaydedilir. Bu hesap, alacak ve borç kalanı vermesi durumuna göre, “648-Enflasyon Düzeltmesi Karları” veya “658- Enflasyon Düzeltmesi Zararları” hesabına devredilerek kapatılır. Tüm değerleme işlemlerinde, bu hesaplara detaylı kayıt yapılması, kontrol ve parasal kar/zarar değerinin nereden kaynaklandığının izlenmesi açısından yardımcı olur.

**Parasal Kar/Zarar Hesabı (648-Enflasyon Düzeltmesi Karları/ 658-Enflasyon Düzeltmesi Zararları):** Dönem sonunda, enflasyon düzeltme hesaplarında oluşan net kar/zararın gelir tablosuna taşınacak hesap kodlarıdır. Bu hesapların değerleri, dönem sonunda Muhasebe → İşlemler → Enflasyon Düzeltmeleri → [Parasal Kar/Zarar Virmanı](<../Muhasebe Modülü Enflasyon Düzeltme İşlemleri/Enflasyon Düzeltmeleri - Parasal Kar-Zarar Virmanı.md>) işlemi ile oluşturulur.
