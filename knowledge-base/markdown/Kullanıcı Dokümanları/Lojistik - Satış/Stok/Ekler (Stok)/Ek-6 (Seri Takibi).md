---
title: "Ek-6 (Seri Takibi)"
page_id: "29993153"
product: "netsis-3-enterprise"
depth: 5
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Lojistik - Satış"
  - "Stok"
  - "Ekler (Stok)"
  - "Ek-6 (Seri Takibi)"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Lojistik - Satış / Stok / Ekler (Stok) / Ek-6 (Seri Takibi)"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTA4ZTY3MTY2LTdkODctNGZmMi1iNzI5LTVkZWZlMWFkYWUxOSZsaW5rPTQ5ZmZkMDlkLTMwZWUtNGI5Yi05MTdjLTFjNTM3NGE2MWIwYiZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=08e67166-7d87-4ff2-b729-5defe1adae19&link=49ffd09d-30ee-4b9b-917c-1c5374a61b0b&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "ek-6-seri-takibi_30001176_29993153.html"
source_version: "2022-11-22T11:39:47.593+03:00"
source_bytes: 276616
fetched_at: "2026-09-13T04:05:30+00:00"
generator: "netsis-scraper 1.0.0"
---
# Ek-6 (Seri Takibi)

Seri Takibi ile ilgili ayrıntılı bilgiye bu dokümandan ulaşılır.

Stoklara ait miktar giriş ve çıkışlarından sonra gelen seri takibi ekranında yapılan değişiklikler sonucu, seri kodlarının grid alandan girişi program tarafından desteklenir. Bu ekrana eklenen butonlar ve alanların kullanımı aşağıda yer alır.

Seri Takibi ekranı; Seri Girişi ve Hızlı Seri Girişi sekmesinden oluşur.

**Seri Girişi**

Seri Girişi sekmesi bilgileri aşağıdaki şekildedir:

![](../../../../_assets/c2ad0edd181e2612e929.png)

| Seri Takibi Ekranı |  |
| --- | --- |
| ![](../../../../_assets/633ea9ceb9ed0d5db489.png) Yeni Satır | Seri girişi yapmak üzere, grid alana ekstra satır ilave etmek için kullanılan butondur |
| ![](../../../../_assets/8331e8838c2eb68b2684.png) Satır Sil | Seçilen satırın, girilen bilgilerle birlikte grid alandan silinmesi için kullanılan butondur. Grid alanda sadece tek bir satır olması halinde bu butona basıldığında, satır silinmez ve sadece satırda girilmiş bilgiler iptal edilir. |
| ![](../../../../_assets/a9bf0d0fdcad8652ef8a.png) Serileri Yapıştır | Bir "Excel" dosyasından veya "tab delimited" formatındaki bir dosyadan kopyalanan bilgilerin yapıştırılarak seri girişlerinin kolaylaştırılmasını sağlar. "Serileri Yapıştır" butonu yerine, grid alanda CTRL+V tuşları kullanılarak da seriler yapıştırılır. Dikkat edilmesi gereken nokta, bilgilerin Seri 1, Seri 2, Miktar, Açıklama 1 ve Açıklama 2 sırasında girilmiş olmasıdır. Miktar bölümü boş ise Otomatik 1 değeri aktarılır. |
| ![](../../../../_assets/9feb168968a5db2dd7ed.png) Seri Rehberi | İlgili stok için daha önce girilmiş seriler arasından, bakiyesi olanların listelenmesi için kullanılan butondur. Seri kodları, butona basılmasıyla birlikte ekrana gelen rehberde, bakiye miktarları ve diğer bilgiler ile birlikte listelenir. Rehberde yer alan satırlar, fare ile çift tıklanarak seçilir ve Tamam ![](../../../../_assets/39d77b8716226638d9ce.jpg)butonuna basılarak seri takibi ekranına aktarılır. |
| ![](../../../../_assets/ec5572c3e315494816bb.png) Üretim Rehberi | Stoklara ait üretim kaynaklı serilerin bakiye miktarları ile listelenmesini sağlayan butondur. Rehberde yer alan satırlar, fare ile çift tıklanarak seçilir ve Tamam ![](../../../../_assets/39d77b8716226638d9ce.jpg)butonuna basılarak seri takibi ekranına aktarılır. |
| ![](../../../../_assets/8bf1211c16c1186ab460.png) FIFO Çıkış Seri | Stok çıkış hareketi sonrası, seri girişi sırasında kullanılan butondur. Bu butona basıldığında, seri kodları program tarafından "ilk giren ilk çıkar" mantığına göre ekrana getirilir. Stoka ait seri hareketlerinin aşağıdaki gibi olduğu varsayıldığında; bu stoktan 6 adet çıkış yapılması istendiğinde, seri kodlarının FIFO yöntemine göre ekrana getirilecek olması halinde, çıkış hareketindeki seri kodları aşağıdaki şekilde oluşur. ![](../../../../_assets/539f7d881466a631ce1b.png) ![](../../../../_assets/e6935400ae4f8f10fdcc.png) |

**Hızlı Seri Girişi**

Hızlı Seri Girişi sekmesi bilgileri aşağıdaki şekildedir:

| Seri Takibi Ekranı |  |
| --- | --- |
| Öndeğer | Hızlı seri girişi için öndeğer tanımlaması yapılan alandır. |
| Başlangıç Seri | Hızlı seri girişi için başlangıç seri numarasının tanımlandığı alandır. |
| Bitiş Seri | Hızlı seri girişi için bitiş seri numarasının tanımlandığı alandır. |
| Miktar | Hızlı seri girişi için miktar tanımlanan alandır. |
| Parti Büyüklüğü | Seri girişinin parti büyüklüğü verilerek yapılmasını sağlar. |
| Stok Planlama Kayıtlarından Getir | Parti Büyüklüğü tanımının Stok Planlama Kayıtları ekranından getirilmesini sağlar. |
