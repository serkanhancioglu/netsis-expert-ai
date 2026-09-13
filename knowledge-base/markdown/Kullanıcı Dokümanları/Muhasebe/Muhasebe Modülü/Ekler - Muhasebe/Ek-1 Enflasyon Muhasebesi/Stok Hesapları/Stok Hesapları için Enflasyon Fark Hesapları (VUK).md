---
title: "Stok Hesapları için Enflasyon Fark Hesapları (VUK)"
page_id: "24740870"
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
  - "Stok Hesapları"
  - "Stok Hesapları için Enflasyon Fark Hesapları (VUK)"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Muhasebe / Muhasebe Modülü / Ekler / Muhasebe / Ek-1 Enflasyon Muhasebesi / Stok Hesapları / Stok Hesapları için Enflasyon Fark Hesapları (VUK)"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTU0M2FjN2Y0LWE3OTktNGNkMS1iMTA3LTQ0ZWE5ZWE1YTk2OSZsaW5rPTY0ZjYzZGE0LWMzNzgtNDIzMy04NDA5LWJmNzFiNTE3ZjY1NyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=543ac7f4-a799-4cd1-b107-44ea9ea5a969&link=64f63da4-c378-4233-8409-bf71b517f657&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "stok-hesaplari-icin-enflasyon-fark-hesaplari-vuk_41162324_24740870.html"
source_version: "2022-12-13T08:12:47.180+03:00"
source_bytes: 5080
fetched_at: "2026-09-13T04:14:35+00:00"
generator: "netsis-scraper 1.0.0"
---
# Stok Hesapları için Enflasyon Fark Hesapları (VUK)

Stok Hesapları için Enflasyon Fark Hesapları ile ilgili ayrıntılı bilgiye bu dokümandan ulaşılabilir.

Stoklar için "Toplulaştırılmış Yöntem" aylık olarak uygulandığında, dönem sonu stokları aşağıdaki formülle düzeltilir;

Tarihi değer \* düzeltme katsayısı = Hesaplanan Dönem Sonu Düzeltilmiş Stok (Düzeltme katsayısı: Basit ortalama ya da durma günü yöntemine göre hesaplanan katsayı)

Düzeltme Farkı = Hesaplanan Dönem Sonu Düzeltilmiş Stok – Mevcut Düzeltilmiş Stok

Aşağıdaki örnek, iki dönem için yürütülmüş ve her dönem için ortalama düzeltme katsayısı 1.1 düşünülerek verilmiştir:

<table><tbody><tr><td><strong>TARİH</strong></td><td><strong>HESAP KODU</strong></td><td><strong>AÇIKLAMA </strong></td><td><strong>TL.TUTAR</strong></td></tr><tr><td> 01/01/2004</td><td> 150-001</td><td> Açılış Kaydı</td><td>100</td></tr><tr><td> 01/01/2004</td><td> 150-999</td><td> Açılış Kaydı (Enflasyon fark hesabı)</td><td>10</td></tr><tr><td> 31/03/2004</td><td> 150-001</td><td> Dönem içi işlemler</td><td>20</td></tr><tr><td colspan="4"><br/></td></tr><tr><td colspan="3"> Dönem Sonu Stok (150-001)</td><td>300</td></tr><tr><td colspan="3"> Dönem Sonu Düzeltilmiş Stok (Hesaplanan)</td><td>330</td></tr><tr><td colspan="3"> Mevcut Düzeltilmiş Stok Mizanı (150-001 + 150-999)</td><td>310</td></tr><tr><td colspan="3"><strong>İşlenecek Fark (330 - 310)</strong></td><td><strong>20</strong></td></tr><tr><td colspan="4"><p><br/></p></td></tr><tr><td> 31/03/2004</td><td> 150-999</td><td> Düzeltme Kaydı (Enflasyon fark hesabı)</td><td>20</td></tr><tr><td> 30/06/2004</td><td> 150-001</td><td> Dönem içi işlemler</td><td>100</td></tr><tr><td colspan="4"><br/></td></tr><tr><td colspan="3">Dönem Sonu Stok (150-001)</td><td>400</td></tr><tr><td colspan="3"> Dönem Sonu Düzeltilmiş Stok (Hesaplanan)</td><td>440</td></tr><tr><td colspan="3"> Mevcut Düzeltilmiş Stok Mizanı (150-001 + 150-999)</td><td>430</td></tr><tr><td colspan="3"><strong>İşlenecek Fark (440 – 430)</strong></td><td><strong>10</strong></td></tr><tr><td colspan="4"><br/></td></tr><tr><td> 30/06/2004</td><td> 150-999</td><td> Düzeltme Kaydı (Enflasyon fark hesabı)</td><td>10</td></tr></tbody></table>

Program, işleyeceği düzeltme farkını bulurken öncelikle olması gereken düzeltilmiş stok değerini bulur, daha sonra mevcut düzeltilmiş stok mizanını bulunan değere getirecek şekilde dengeler. Her dönem düzeltme işleminde, her bir stok için stok hesabı + stok için enflasyon fark hesabı değeri önem taşıdığından dolayı, her bir stok için enflasyon fark hesaplarının ayrıştırılması gerekir. Yani, birebir her stok muavini için bir fark hesabı açılması gerekir.
