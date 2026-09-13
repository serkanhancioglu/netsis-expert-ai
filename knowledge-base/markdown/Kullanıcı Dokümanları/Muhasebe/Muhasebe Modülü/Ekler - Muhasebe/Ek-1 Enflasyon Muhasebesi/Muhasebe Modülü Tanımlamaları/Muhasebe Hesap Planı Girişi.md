---
title: "Muhasebe Hesap Planı Girişi"
page_id: "24740854"
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
  - "Muhasebe Hesap Planı Girişi"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / Ekler / Muhasebe / Ek-1 Enflasyon Muhasebesi / Muhasebe Modülü Tanımlamaları / Muhasebe Hesap Planı Girişi"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTgwYzNmMmQxLTYxZDgtNDVkZi1hNGE3LWNkNmE1YjNiMmM3YSZsaW5rPTAwMWMyMTY4LWI4ZWYtNDgzZi04ZTgwLTFhYmQyZmUzN2FlNSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=80c3f2d1-61d8-45df-a4a7-cd6a5b3b2c7a&link=001c2168-b8ef-483f-8e80-1abd2fe37ae5&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "muhasebe-hesap-plani-girisi_41162273_24740854.html"
source_version: "2022-12-12T16:25:11.353+03:00"
source_bytes: 3638
fetched_at: "2026-09-13T04:14:30+00:00"
generator: "netsis-scraper 1.0.0"
---
# Muhasebe Hesap Planı Girişi

Muhasebe Hesap Planı Girişi ile ilgili ayrıntılı bilgiye bu dokümandan ulaşılabilir.

"Muhasebe Hesap Planı" girişi sırasında, her bir hesap için çalışma şekli belirlenmesi gerekir.

**Düzeltilecek Hesap:** Muhasebe Modülünde hesaplar, Düzeltilecek Hesap veya Düzeltilmeyecek Hesap olarak belirlenebilir. Böylece; yeniden değerleme fon hesapları gibi, TL muhasebede işlem gören ancak IAS 29 uygulamasında anlam ifade etmeyen hesapların ayrıştırılması sağlanır. Bu tür hesaplar için "Düzeltilecek" seçeneğinin kaldırılması gerekir. Diğer hesapların tümü, düzeltilecek hesaptır ve bu seçeneğin işaretlenmesi gerekir. Enflasyon Muhasebesi (VUK) Uygulamasında bu alan anlamsızdır ve tüm hesaplar düzeltilir. Zaten, bu tip hesapların Enflasyon Muhasebesi başlangıcında sıfırlanması ve bir daha çalıştırılmaması gerekir.

**Parasal Hesap:** Parasal ve parasal olmayan hesapların ayrıştırılması için belirlenecek seçenektir. Doküman eklerinde, ana hesap bazında parasal/parasal olmayan ayrımı verilir. "Parasal Hesap" seçeneğinde, muavin bazında istenen tanımın yapılması gerekir. Gelir tablosu hesaplarında "Parasal Hesap" alanı aktif değildir. Bu hesapların tamamı parasal olmayan hesap olarak işlem görür.

**Enflasyon Fark Hesabı:** Vergi Usul Kanunu, enflasyon düzeltmelerinin enflasyon fark hesaplarında takip edilmesini öngörür. SPK ise, ayrı bir enflasyon defteri tutulmasını önerir. Enflasyon fark hesaplarının öncelikle "Hesap Planı Girişi" bölümünden tanımlanması gerekir. Daha sonra, enflasyon düzeltmesine tabi tutulacak ilgili hesap için, bu alanda kullanılacak fark hesabı belirlenir. Bir fark hesabı, birden fazla muavin hesap için geçerli olabilir. İstendiği zaman, ana hesap için tek fark hesabı tanımlanabilir. Bu hesap alt muavinler için de geçerli olur (Muavin hesapta tanımlı bir fark hesabı yoksa). Ancak muavin hesapta ve bağlı ana hesabında tanımlı fark hesabı yoksa, program enflasyon düzeltmelerini hesabın üzerinde yapar Bu durumda, Enflasyon Muhasebesi (VUK) uygulamasına göre, enflasyon düzeltmelerini ayrı satırlar halinde aynı hesaba TL olarak işler. IAS 29 uygulamasında ise, bu alanın bir önemi yoktur. Bu uygulamada "Enflasyon Fark Hesapları" çalışmaz, aynı hesap kodu üzerinde ikinci defterdeki alanlar çalışır. Bazı hesaplarda, her bir muavin hesap için bir de enflasyon fark hesabı açma zorunluluğu vardır.
