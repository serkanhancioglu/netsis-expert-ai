---
title: "Parasal Olmayan Hesaplar Virman Dekontu / Muhasebe"
page_id: "24740876"
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
  - "Diğer Parasal Olmayan Hesaplar"
  - "Parasal Olmayan Hesaplar Virman Dekontu / Muhasebe"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / Ekler / Muhasebe / Ek-1 Enflasyon Muhasebesi / Diğer Parasal Olmayan Hesaplar / Parasal Olmayan Hesaplar Virman Dekontu / Muhasebe"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTY2OTQzYWQ2LWRlZjMtNDliYS1hNWQ1LWU5MWIzN2Q1YzQ0YSZsaW5rPTVjMGU4ZjE3LTc4ZjUtNDY5MS1hYmNjLWUzZDVlMjQwYmJiMSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=66943ad6-def3-49ba-a5d5-e91b37d5c44a&link=5c0e8f17-78f5-4691-abcc-e3d5e240bbb1&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "parasal-olmayan-hesaplar-virman-dekontu-muhasebe_41162244_24740876.html"
source_version: "2022-12-12T16:14:06.107+03:00"
source_bytes: 4101
fetched_at: "2026-09-13T04:14:24+00:00"
generator: "netsis-scraper 1.0.0"
---
# Parasal Olmayan Hesaplar Virman Dekontu / Muhasebe

Parasal Olmayan Hesaplar Virman Dekontu ile ilgili ayrıntılı bilgiye bu dokümandan ulaşılabilir.

Parasal olmayan hesapların, dönem sonunda bir rapor yardımıyla maliyetlendirme işlemi yapılır. Ancak, dönem içinde çok fazla bu türden hesap çalışıyorsa, dönem sonunda elle düzenleme zor bir işlem haline gelir. İstendiğinde maliyetlendirme işleminin program tarafından yapılmasını sağlamak için, parasal olmayan hesaplarda yapılan çıkış/virman işlemleri, özel bir dekont ile yapılarak program tarafından maliyetlendirme işlemi yapılır.

[Parasal Olmayan Hesaplar Enflasyon Raporu](<Parasal Olmayan Hesaplar Enflasyon Raporu.md>) / Muhasebe bölümündeki örneğe göre;

| Hesap Kodu | TL.Tutar |
| --- | --- |
| 159-001 | \<150.000\> |
| 150-001 | 150.000 |

şeklinde girilmesi gereken fiş, programın maliyetlendirme işlemini otomatik yapmasını sağlamak için dekont adımından kaydedilir.

Bu bölümde "Genel Dekont Kaydı" benzeri bir ekrandan giriş yapılır. Ancak, dikkat edilmesi gereken bazı konular vardır.

**Miktar:** Çıkış/Virman yapılan parasal olmayan hesap miktarının mutlaka doldurulması gerekir. Burada çıkış yapılan birimin, ilgili hesapta hangi birim baz alınarak girişler yapılmışsa buna göre toplam olarak girilmesi gerekir. Yukarıdaki örnekte, 159-001 hesabından yapılan çıkış için "Miktar" alnına 150 birim yazılması gerekir.

**Dağıtılacak:** Çıkış/Virman yapılan satır/satırların dağıtılacak satır olarak işaretlenmesi gerekir. Örnekte; 159-001 hesabından 150 birim, 150.000 TL tutarındaki çıkış hareketine "dağıtılacak" işaretinin konması gerekir.

Değer taşınma işlemi yapılacak olan diğer satırlarda, "Miktar" alanı doldurularak "dağıtılacak" işaretinin konması gerekir.

| Hesap Kodu | TL.Değer | Miktar | Dağıtılacak |
| --- | --- | --- | --- |
| 159-000 | \<150.000\> | 150 |  |
| 150-001 | 300.000 | - | - |
