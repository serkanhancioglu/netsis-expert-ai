---
title: "KDV Oran Değişikliği İçin Netsis ERP'de Yapılacak Düzenlemeler"
page_id: "115606545"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "KDV Oran Değişikliği İçin Netsis ERP'de Yapılacak Düzenlemeler"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / KDV Oran Değişikliği İçin Netsis ERP'de Yapılacak Düzenlemeler"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPWY5MDU1NGI4LWE3NTUtNGI0Ni05YWQyLWYyNWM0NzUyZjRmOCZsaW5rPWZhYWRmMDBjLTRiZTYtNDE4Mi05YTc4LTEzMmNhNGEwY2U2NSZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=f90554b8-a755-4b46-9ad2-f25c4752f4f8&link=faadf00c-4be6-4182-9a78-132ca4a0ce65&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "kdv-oran-degisikligi-icin-netsis-erp-de-yapilacak-duzenlemeler_115606573_115606545.html"
source_version: "2023-07-07T15:24:35.930+03:00"
source_bytes: 646525
fetched_at: "2026-09-13T04:23:19+00:00"
generator: "netsis-scraper 1.0.0"
---
# KDV Oran Değişikliği İçin Netsis ERP'de Yapılacak Düzenlemeler

**7346 Sayılı Kanun ile 7 Temmuz 2023 Tarihli Resmi Gazete'de Yayımlanan KDV Oran Değişikliği**

7 Temmuz 2023 Sayılı Resmi Gazete'de yayımlanan 7346 sayılı Cumhurbaşkanlığı kararı uyarınca, Türkiye'deki genel ve indirimli KDV oranları ile temizlik ürünleri tesliminde uygulanan KDV oranları aşağıdaki şekilde değiştirilmiştir.

- Genel KDV oranı %18 'den %20'ye yükseltilmiştir.
- %8' lik indirimli KDV oranı %10'a yükseltilmiştir.
- %1' lik indirimli KDV oranında herhangi bir değişikliğe gidilmemiştir.
- Diş fırçası, macunu ve diş ipleri dışındaki temizlik ürünlerinde daha önce %8 olarak uygulanan KDV oranı %20'ye yükseltilmiştir.

**Stok Kartı Kayıtlarında Yapılması Gereken Değişiklikler**

Stok Kartı Kayıtları ekranında **"Satış KDV Oranı"** ve **"Alış KDV Oranı"** alanları manuel olarak değiştirilebilmektedir.

Ayrıca Stok\>İşlemler\>Hızlı Değişiklik menüsü ile de toplu olarak değiştirilebilir.

Stokların kartlarında **"Satış KDV Oranı"** ve **"Alış KDV Oranı"** değeri 8 iken, bu değerin 10 olarak değiştirilmesi aşağıdaki adımlarla sağlanabilir.

![](../_assets/90ffe404771eb10b8a03.png)

Hızlı değişiklik ekranında **"Tablo Seçimi"** sekmesinde **"Stok Sabit"** seçeneği işaretlenir.

![](../_assets/2154d7342e2d054aca95.png)

**"Aralık/Maske"** sekmesinde KDV oranlarının değişmesi istenen stoklar için, **"Stok Kartı Sahaları"** alanından kısıt verilmek istenen alan seçilir. Seçilen saha çift tıklanarak **"Kısıt Verilecek Sahalar"** alanına atılır.

Örnekte, **"Satış KDV Oranı"** ve **"Alış KDV Oranı"** sahası 8 olan stokların KDV oranlarına kısıt verebilmek için; **"Stok Kartı Sahaları"** kısmında bu sahalar seçilir ve "**Kısıt Verilecek Sahalar**" kısmına eklenir. Eklenen alanlara çift tıklanarak "**Eşit**","8" tanımlaması yapılıp aşağı ok işareti ile kaydedilir.

![](../_assets/41dcd5a66684bd469fbb.png)

![](../_assets/7717ccc2a2784a91a372.png)

Sonraki adımda **"Değiştir"** sekmesinde, aynı şekilde **"Stok Kartı Sahaları"** kısmından değiştirilmek istenen saha seçilip çift tıklanarak **"Kısıt Verilecek Sahalar"** kısmına atılması sağlanır. Ardından bu alanlar çift tıklanarak
**"Hangi Sahaya Göre"** = **"Satış KDV Oranı"**
**"Hesap Tipi"** = **"Sabit"**
**"Sabit Değer"** = **"10"** tanımlaması yapılıp aşağı ok işareti ile kaydedilir.
![](../_assets/431ac41c4158ac11e8a4.png)
![](../_assets/e20d400aaaf13b3f21a2.png)

Son olarak **"Onaylı değiştir"** veya **"Değiştir"** butonu ile yapılan değişikliğin stok kartlarına yansıtılması sağlanır. **"Onaylı değiştir"** butonu ile işlem yapılırsa her stok için tek tek onaylama yapılması gerekecektir. Kontrollü değişiklik yapılmak istendiği durumlarda kullanılabilir.
**"Değiştir"** butonu ile de verilen kısıtlara uyan stoklara toplu şekilde güncelleme yapılacaktır.

![](../_assets/e4b75b7615a6b068125d.png)

Aynı işlem adımları KDV oranı 18 'den 20 'ye çıkarılacak olan stoklar içinde uygulanabilir.

**Entegrasyon Kodlarında** **Yapılması Gereken Değişiklikler**

Entegrasyon Kodlarında **"Fatura KDV"** ve **"Fatura İade KDV"** sekmelerindeki KDV oran sayısı arttırılarak yeni oranlara ait KDV hesapları tanımlanabilir.

KDV oran değişikliği öncesindeki tanımlar;

![](../_assets/25a13e58f3cd3d48d53f.png)
![](../_assets/d433e85bbc87732773e6.png)
KDV oran değişikliği sonrasındaki tanımlar;
![](../_assets/330c60e31f4c95d1b316.png)
![](../_assets/2ae359fbf4324ac66a43.png)
