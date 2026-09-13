---
title: "Kaynak Hareketleri"
page_id: "50666864"
product: "netsis-3-enterprise"
depth: 6
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Kullanıcı Dokümanları"
  - "Üretim"
  - "MRP"
  - "Kayıt / MRP"
  - "Kaynak Yönetimi/MRP"
  - "Kaynak Hareketleri"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Kullanıcı Dokümanları / Üretim / MRP / Kayıt / MRP / Kaynak Yönetimi/MRP / Kaynak Hareketleri"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTlhMzZkYWUwLTdmMjEtNGY3Ny04NWZlLWE0NzU1MWE4ZGI1NyZsaW5rPWYyMGQ2ODcwLWNjNTAtNDg1Mi04YjIxLTY4M2FiNzU3ZmFkNyZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=9a36dae0-7f21-4f77-85fe-a47551a8db57&link=f20d6870-cc50-4852-8b21-683ab757fad7&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "kaynak-hareketleri_50667038_50666864.html"
source_version: "2022-10-19T14:22:54.240+03:00"
source_bytes: 1074669
fetched_at: "2026-09-13T04:19:54+00:00"
generator: "netsis-scraper 1.0.0"
---
# Kaynak Hareketleri

Kaynak Hareketleri, Üretim Bölümü'nde Kayıt/MRP menüsünün altında yer alır. Kaynak kullanımlarını, ömür tüketimlerini ve kaynakların anlık durumunu detaylı olarak incelemek için kullanılan bölümdür. Demirbaş tipli kaynaklar için tamire gidiş ve tamirden dönüş hareketlerinin de girilmesi sağlanır.

Kaynak Hareketleri ekranı; Özel Bilgiler ve Kaynak Hareketleri olmak üzere iki sekmeden oluşur.

**Özet Bilgiler**

Tüm kaynakların toplu listesinin ve bazı özet raporların gösterildiği sekmedir.

![](../../../../../_assets/f5e89b7737b3d3c3cb4d.png)

Özet Bilgiler sekmesinde ekranın sol üst bölümünde "Ömrü Azalan Kaynaklar" listelenir. Bu bölümde ömür yüzdesi en küçük olan ilk 5 kaynak gösterilir. Ekranın sağ üst bölümünde "Bakımdaki Kaynaklar" listelenir. Bu bölümde de tamire gitmiş ancak henüz tamirden dönmemiş kaynak kodları gösterilir. Bu kaynakların bakımda geçen süreleri ve kaynak kartlarında tanımlanan ortalama bakım süreleri izlenir. Ekranın alt bölümünde, ömür takibi yapılan kaynakların bir listesi ve bu kaynaklara ait özet bilgiler -Ömür Bakiyesi, Ömür Yüzdesi gibi- bulunur. Kaynak listesindeki herhangi bir kaydın üzerine fare ile çift tıklayarak veya üst bölümdeki grafiklerde ilgili kaynak koduna tıklayarak kaynağın hareket kayıtlarına ulaşılır.

**Kaynak Hareketleri**

Kaynak kodu bazında hareket kayıtlarını detaylı olarak incelemek için kullanılan sekmedir.

![](../../../../../_assets/5bce5a3feb4544bb64f5.png)

"Kaynak Hareketleri" sekmesinde kaynak kodu girilerek geçmişe yönelik hareketler raporlanır ve kaynağın yürüyen ömür bakiyesi izlenir. Demirbaş tipli kaynakların tamire gidiş ve tamirden dönüş hareketleri girilebilir. Üretim sırasında girilen kaynak kullanımları ekranda gösterilir fakat bu kayıtlar üzerinde düzenleme yapılamaz. Aynı şekilde stok tipli kaynakların fatura gibi hareketleri de "Kaynak Hareketleri" ekranında gösterilir fakat bu kayıtlar üzerinden düzenleme yapılamaz.

Kaynak Hareketleri sekmesinin sağ üst köşesindeki sembole tıklayarak grafik için görünüm seçeneği değiştirilir. Varsayılan olarak grafikte tüm kayıtlar gösterilir. Haftalık, Günlük gibi seçenekler sayesinde gösterilen kayıt sayısının kısıtlanması sağlanır. Daha detaylı kısıt vermek için tarih aralığı girilir.

**Örneğin;**

"Haftalık" görünüm seçildiğinde, grid üzerinden seçilen kaydın bulunduğu haftadaki tüm hareketler gösterilir.

![](../../../../../_assets/6b8162ef6abee6d9c777.png)

Kaynak Hareketleri grafiğindeki noktalara tıklandığında, grid üzerindeki hareket satırı otomatik olarak seçilir. Bu satır üzerinden hareketin detayı - hangi üretim fişinde kullanıldığı, tarih ve ömür tüketim bilgileri - görüntülenir.

Stok tipli kaynaklar için üretim sırasında girilen kullanım bilgileri, stok hareketlerine de yansır fakat "Kaynak Hareketleri" ekranında ömür birimi üzerinden raporlama yapılır.

**Örneğin;**

TESTERE_01 kaynağı stok tipli bir kaynaktır ve kaynak hareketleri aşağıdaki şekilde görüntülenir.

![](../../../../../_assets/37386066cdbc720db00a.png)

Kaynak Hareketleri ekranındaki miktarlar, "kesim" birimi üzerinden raporlanır. Aynı şekilde üretim belgelerinde kullanılan kaynak girişi yapılırken de miktarlar "kesim" birimi üzerinden girilir. Oluşan ömür tüketimleri, stok kartının birinci ölçü birimine çevrilerek stok hareketlerine aşağıdaki şekilde işlenir. Birinci ölçü birimine çevrim sırasında aşağıdaki formül kullanılır:

Hareket Satırındaki Ömür Miktarı / Kaynak Tanımındaki Toplam Ömür Değeri

![](../../../../../_assets/398d7491e437f57bdec4.png)
